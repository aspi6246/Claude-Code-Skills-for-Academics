#!/usr/bin/env python3
"""
beamer_check.py — Compile a Beamer .tex file and render each slide
to a PNG image for visual inspection.

Usage:
    python beamer_check.py <path-to-tex-file> [--output-dir <dir>] [--dpi <dpi>]

Outputs:
    - Compilation log summary (errors, warnings, overfull/underfull boxes)
    - One PNG per slide in the output directory
    - A JSON summary file with structured compilation diagnostics
"""

import argparse
import json
import os
import re
import subprocess
import sys
from pathlib import Path


def compile_tex(tex_path: Path, work_dir: Path) -> dict:
    """Compile the .tex file twice with pdflatex and capture diagnostics."""

    pdf_name = tex_path.stem + ".pdf"
    log_name = tex_path.stem + ".log"

    result = {
        "success": False,
        "errors": [],
        "warnings": [],
        "overfull_hbox": [],
        "overfull_vbox": [],
        "underfull_hbox": [],
        "underfull_vbox": [],
        "missing_files": [],
        "pdf_path": None,
        "log_path": None,
        "num_pages": 0,
    }

    # Run pdflatex twice (for TOC/cross-references)
    for pass_num in (1, 2):
        proc = subprocess.run(
            [
                "pdflatex",
                "-interaction=nonstopmode",
                "-halt-on-error",
                f"-output-directory={work_dir}",
                str(tex_path),
            ],
            capture_output=True,
            text=True,
            cwd=str(tex_path.parent),
            timeout=120,
        )

    # Parse the log file
    log_path = work_dir / log_name
    result["log_path"] = str(log_path)

    if not log_path.exists():
        result["errors"].append("No log file produced — pdflatex may have crashed.")
        return result

    log_text = log_path.read_text(errors="replace")

    # Extract errors
    for m in re.finditer(r"^! (.+?)$", log_text, re.MULTILINE):
        result["errors"].append(m.group(1).strip())

    # Extract LaTeX warnings
    for m in re.finditer(r"^LaTeX Warning: (.+?)$", log_text, re.MULTILINE):
        result["warnings"].append(m.group(1).strip())

    # Package warnings
    for m in re.finditer(r"^Package \w+ Warning: (.+?)$", log_text, re.MULTILINE):
        result["warnings"].append(m.group(1).strip())

    # Overfull/underfull boxes — these are the layout problems
    for m in re.finditer(
        r"^(Overfull \\hbox) \((.+?)\) .+? at lines? (\d+)(?:--(\d+))?",
        log_text,
        re.MULTILINE,
    ):
        result["overfull_hbox"].append(
            {
                "severity": m.group(2),
                "line_start": int(m.group(3)),
                "line_end": int(m.group(4)) if m.group(4) else int(m.group(3)),
            }
        )

    for m in re.finditer(
        r"^(Overfull \\vbox) \((.+?)\) .+? at lines? (\d+)(?:--(\d+))?",
        log_text,
        re.MULTILINE,
    ):
        result["overfull_vbox"].append(
            {
                "severity": m.group(2),
                "line_start": int(m.group(3)),
                "line_end": int(m.group(4)) if m.group(4) else int(m.group(3)),
            }
        )

    for m in re.finditer(
        r"^(Underfull \\hbox) .+? at lines? (\d+)(?:--(\d+))?",
        log_text,
        re.MULTILINE,
    ):
        result["underfull_hbox"].append(
            {
                "line_start": int(m.group(2)),
                "line_end": int(m.group(3)) if m.group(3) else int(m.group(2)),
            }
        )

    for m in re.finditer(
        r"^(Underfull \\vbox) .+? at lines? (\d+)(?:--(\d+))?",
        log_text,
        re.MULTILINE,
    ):
        result["underfull_vbox"].append(
            {
                "line_start": int(m.group(2)),
                "line_end": int(m.group(3)) if m.group(3) else int(m.group(2)),
            }
        )

    # Missing files (images, packages)
    for m in re.finditer(
        r"^! LaTeX Error: File `(.+?)' not found", log_text, re.MULTILINE
    ):
        result["missing_files"].append(m.group(1))
    for m in re.finditer(
        r"^Package graphicx/graphics Error:.+?`(.+?)'",
        log_text,
        re.MULTILINE,
    ):
        result["missing_files"].append(m.group(1))

    # Check if PDF was produced
    pdf_path = work_dir / pdf_name
    if pdf_path.exists():
        result["success"] = True
        result["pdf_path"] = str(pdf_path)
    else:
        if not result["errors"]:
            result["errors"].append("No PDF produced (unknown reason).")

    return result


def count_pdf_pages(pdf_path: str) -> int:
    """Count pages in a PDF using pdfinfo or pdflatex log."""
    try:
        proc = subprocess.run(
            ["pdfinfo", pdf_path], capture_output=True, text=True, timeout=30
        )
        for line in proc.stdout.splitlines():
            if line.startswith("Pages:"):
                return int(line.split(":")[1].strip())
    except (subprocess.TimeoutExpired, FileNotFoundError):
        pass

    # Fallback: try pdftk
    try:
        proc = subprocess.run(
            ["pdftk", pdf_path, "dump_data"],
            capture_output=True,
            text=True,
            timeout=30,
        )
        for line in proc.stdout.splitlines():
            if "NumberOfPages" in line:
                return int(line.split(":")[1].strip())
    except (subprocess.TimeoutExpired, FileNotFoundError):
        pass

    return 0


def render_slides(pdf_path: str, output_dir: Path, dpi: int = 150) -> list:
    """Render each page of the PDF to a PNG using pdftoppm or convert."""
    output_dir.mkdir(parents=True, exist_ok=True)
    rendered = []

    # Try pdftoppm first (from poppler-utils)
    try:
        prefix = str(output_dir / "slide")
        proc = subprocess.run(
            ["pdftoppm", "-png", "-r", str(dpi), pdf_path, prefix],
            capture_output=True,
            text=True,
            timeout=120,
        )
        if proc.returncode == 0:
            # pdftoppm names files as slide-01.png, slide-02.png, etc.
            for f in sorted(output_dir.glob("slide-*.png")):
                rendered.append(str(f))
            return rendered
    except (subprocess.TimeoutExpired, FileNotFoundError):
        pass

    # Fallback: ImageMagick convert
    try:
        proc = subprocess.run(
            [
                "convert",
                "-density",
                str(dpi),
                pdf_path,
                "-quality",
                "90",
                str(output_dir / "slide-%02d.png"),
            ],
            capture_output=True,
            text=True,
            timeout=120,
        )
        if proc.returncode == 0:
            for f in sorted(output_dir.glob("slide-*.png")):
                rendered.append(str(f))
            return rendered
    except (subprocess.TimeoutExpired, FileNotFoundError):
        pass

    return rendered


def main():
    parser = argparse.ArgumentParser(
        description="Compile and render Beamer slides for visual inspection"
    )
    parser.add_argument("tex_file", help="Path to the .tex file")
    parser.add_argument(
        "--output-dir",
        default=None,
        help="Directory for rendered PNGs (default: <tex_dir>/beamer-check-output)",
    )
    parser.add_argument(
        "--dpi",
        type=int,
        default=150,
        help="DPI for rendered slide images (default: 150)",
    )
    args = parser.parse_args()

    tex_path = Path(args.tex_file).resolve()
    if not tex_path.exists():
        print(f"Error: {tex_path} does not exist.", file=sys.stderr)
        sys.exit(1)

    if args.output_dir:
        output_dir = Path(args.output_dir).resolve()
    else:
        output_dir = tex_path.parent / "beamer-check-output"
    output_dir.mkdir(parents=True, exist_ok=True)

    # Step 1: Compile
    print(f"Compiling {tex_path.name}...")
    diagnostics = compile_tex(tex_path, output_dir)

    # Step 2: Count pages and render
    if diagnostics["success"]:
        num_pages = count_pdf_pages(diagnostics["pdf_path"])
        diagnostics["num_pages"] = num_pages
        print(f"Compilation successful: {num_pages} pages.")

        print(f"Rendering slides at {args.dpi} DPI...")
        slides_dir = output_dir / "slides"
        rendered = render_slides(diagnostics["pdf_path"], slides_dir, args.dpi)
        diagnostics["rendered_slides"] = rendered
        print(f"Rendered {len(rendered)} slide images to {slides_dir}/")
    else:
        print("Compilation FAILED. See errors below.")
        diagnostics["rendered_slides"] = []

    # Step 3: Print summary
    print("\n" + "=" * 60)
    print("COMPILATION DIAGNOSTICS")
    print("=" * 60)

    if diagnostics["errors"]:
        print(f"\n  ERRORS ({len(diagnostics['errors'])}):")
        for e in diagnostics["errors"]:
            print(f"    - {e}")

    if diagnostics["missing_files"]:
        print(f"\n  MISSING FILES ({len(diagnostics['missing_files'])}):")
        for f in diagnostics["missing_files"]:
            print(f"    - {f}")

    if diagnostics["overfull_hbox"]:
        print(f"\n  OVERFULL HBOX ({len(diagnostics['overfull_hbox'])}):")
        for o in diagnostics["overfull_hbox"]:
            print(f"    - {o['severity']} at line {o['line_start']}")

    if diagnostics["overfull_vbox"]:
        print(f"\n  OVERFULL VBOX ({len(diagnostics['overfull_vbox'])}):")
        for o in diagnostics["overfull_vbox"]:
            print(f"    - {o['severity']} at line {o['line_start']}")

    if diagnostics["warnings"]:
        print(f"\n  WARNINGS ({len(diagnostics['warnings'])}):")
        for w in diagnostics["warnings"]:
            print(f"    - {w}")

    total_issues = (
        len(diagnostics["errors"])
        + len(diagnostics["overfull_hbox"])
        + len(diagnostics["overfull_vbox"])
        + len(diagnostics["missing_files"])
    )
    if total_issues == 0 and diagnostics["success"]:
        print("\n  No compilation issues detected.")

    print("=" * 60)

    # Step 4: Write JSON summary
    summary_path = output_dir / "diagnostics.json"
    with open(summary_path, "w") as f:
        json.dump(diagnostics, f, indent=2)
    print(f"\nFull diagnostics written to {summary_path}")

    if diagnostics["rendered_slides"]:
        print(f"Slide images in {slides_dir}/")
        print("\nNext step: visually inspect each slide image for layout issues.")


if __name__ == "__main__":
    main()
