---
name: canvas-lms-api
description: >
  Use this skill whenever working with the Canvas LMS REST API — including creating or
  updating modules, pages, and files for a course, building sync scripts, managing course
  structure programmatically, or uploading files and linking them in pages. Trigger this
  skill any time the user mentions Canvas, LMS, course sync, module pages, or file uploads
  to Canvas. Also use when writing or debugging any Python script that calls the Canvas API.
---

# Canvas LMS API Skill

A comprehensive reference for building Python scripts that interact with the Canvas LMS REST API, specifically for course content management: modules, pages, and file uploads.

## Project Context

This skill supports building a course content sync system for **Ethics and Governance** at UTS. The system reads HTML content files and a course structure config from a local folder, then syncs everything to Canvas via the API.

**Local project folder:** `~/path/to/CanvasDev-EthicsGov/`

> ⚠️ Replace with the actual folder location on your machine.

**Key files:**
- `config.py` — stores credentials and course IDs (NEVER commit this to GitHub)
- `course_structure.json` — master blueprint of all modules/pages/files
- `sync.py` — main sync script
- `module-XX-name/` — one folder per module containing HTML page files and a `files/` subfolder

---

## Setup & Authentication

### config.py pattern
```python
CANVAS_DOMAIN = "canvas.uts.edu.au"
COURSE_ID = "XXXXX"           # sandpit — replace with your sandpit course ID
# COURSE_ID = "YYYYY"         # live course (comment out sandpit when ready)
ACCESS_TOKEN = "your_token_here"
```

> ⚠️ Replace XXXXX with your sandpit course ID, YYYYY with your live Ethics and Governance
> course ID, and paste your API token in place of "your_token_here".

### Standard headers and base URL
```python
import requests
from config import CANVAS_DOMAIN, COURSE_ID, ACCESS_TOKEN

BASE_URL = f"https://{CANVAS_DOMAIN}/api/v1"
HEADERS = {"Authorization": f"Bearer {ACCESS_TOKEN}"}
```

### Getting a token
Canvas → Profile picture → Settings → Approved Integrations → + New Access Token

---

## Core API Patterns

### ALWAYS use "find or create" — never blindly create
Before creating anything, check if it already exists. This prevents duplicates on re-runs.

```python
def get_or_create_module(name, position):
    """Find an existing module by name, or create it."""
    response = requests.get(f"{BASE_URL}/courses/{COURSE_ID}/modules", headers=HEADERS)
    modules = response.json()
    for m in modules:
        if m["name"] == name:
            print(f"  Found existing module: {name}")
            return m["id"]
    # Create new
    response = requests.post(
        f"{BASE_URL}/courses/{COURSE_ID}/modules",
        headers=HEADERS,
        data={"module[name]": name, "module[position]": position, "module[published]": False}
    )
    module = response.json()
    print(f"  Created module: {name}")
    return module["id"]
```

### Pagination
Canvas paginates responses — always handle it:
```python
def get_all_pages(url):
    results = []
    while url:
        response = requests.get(url, headers=HEADERS)
        results.extend(response.json())
        url = response.links.get("next", {}).get("url")
    return results

all_modules = get_all_pages(f"{BASE_URL}/courses/{COURSE_ID}/modules")
```

---

## Modules API

### Create a module
```python
response = requests.post(
    f"{BASE_URL}/courses/{COURSE_ID}/modules",
    headers=HEADERS,
    data={
        "module[name]": "Module 1: Introduction to Ethics and Governance",
        "module[position]": 1,
        "module[published]": False
    }
)
module_id = response.json()["id"]
```

### Update a module (e.g. set position)
```python
requests.put(
    f"{BASE_URL}/courses/{COURSE_ID}/modules/{module_id}",
    headers=HEADERS,
    data={"module[position]": 1}
)
```

### Delete a module
```python
requests.delete(f"{BASE_URL}/courses/{COURSE_ID}/modules/{module_id}", headers=HEADERS)
```

---

## Module Items API

Module item types: `File`, `Page`, `Discussion`, `Assignment`, `Quiz`, `SubHeader`, `ExternalUrl`, `ExternalTool`

**CRITICAL:** For `Page` type, use `page_url` (the slug), NOT `content_id`. Using `content_id` for pages will silently fail.

### Add a SubHeader (section heading)
```python
requests.post(
    f"{BASE_URL}/courses/{COURSE_ID}/modules/{module_id}/items",
    headers=HEADERS,
    data={
        "module_item[title]": "Topic 1 - Foundations of Ethics",
        "module_item[type]": "SubHeader",
        "module_item[indent]": 0
    }
)
```

### Add a Page to a module
```python
# page_url is the slug — Canvas generates this from the title
# e.g. "Lecture - Foundations of Ethics" → "lecture-foundations-of-ethics"
requests.post(
    f"{BASE_URL}/courses/{COURSE_ID}/modules/{module_id}/items",
    headers=HEADERS,
    data={
        "module_item[title]": "Lecture - Foundations of Ethics",
        "module_item[type]": "Page",
        "module_item[page_url]": "lecture-foundations-of-ethics",
        "module_item[indent]": 1
    }
)
```

### Add a File to a module
```python
requests.post(
    f"{BASE_URL}/courses/{COURSE_ID}/modules/{module_id}/items",
    headers=HEADERS,
    data={
        "module_item[title]": "Lecture Slides",
        "module_item[type]": "File",
        "module_item[content_id]": file_id,   # File ID from upload response
        "module_item[indent]": 1
    }
)
```

### Reorder module items
Items are ordered by position (1-based). Set position explicitly when creating items, or update after:
```python
requests.put(
    f"{BASE_URL}/courses/{COURSE_ID}/modules/{module_id}/items/{item_id}",
    headers=HEADERS,
    data={"module_item[position]": 2}
)
```

---

## Pages API

### Create a page
```python
response = requests.post(
    f"{BASE_URL}/courses/{COURSE_ID}/pages",
    headers=HEADERS,
    data={
        "wiki_page[title]": "Lecture - Foundations of Ethics",
        "wiki_page[body]": html_content,   # full HTML string
        "wiki_page[published]": False
    }
)
page = response.json()
page_slug = page["url"]    # e.g. "lecture-foundations-of-ethics"
page_id = page["page_id"]  # numeric ID (less commonly needed)
```

### Update an existing page (by slug)
```python
requests.put(
    f"{BASE_URL}/courses/{COURSE_ID}/pages/{page_slug}",
    headers=HEADERS,
    data={"wiki_page[body]": updated_html_content}
)
```

### Get a page
```python
response = requests.get(
    f"{BASE_URL}/courses/{COURSE_ID}/pages/{page_slug}",
    headers=HEADERS
)
```

### Find or create page pattern
```python
def get_or_create_page(title, html_body):
    slug = title.lower().replace(" ", "-").replace("–", "-")
    import re
    slug = re.sub(r"[^a-z0-9-]", "", slug)
    
    response = requests.get(f"{BASE_URL}/courses/{COURSE_ID}/pages/{slug}", headers=HEADERS)
    if response.status_code == 200:
        # Update existing
        requests.put(
            f"{BASE_URL}/courses/{COURSE_ID}/pages/{slug}",
            headers=HEADERS,
            data={"wiki_page[body]": html_body}
        )
        print(f"  Updated page: {title}")
        return slug
    else:
        # Create new
        response = requests.post(
            f"{BASE_URL}/courses/{COURSE_ID}/pages",
            headers=HEADERS,
            data={"wiki_page[title]": title, "wiki_page[body]": html_body, "wiki_page[published]": False}
        )
        print(f"  Created page: {title}")
        return response.json()["url"]
```

---

## File Upload API

**IMPORTANT:** Canvas file upload is a 3-step process. It is NOT a simple single POST.

### Complete upload function
```python
import os
import requests

def upload_file(local_path, canvas_folder_name):
    """Upload a file to Canvas, return (file_id, file_url). Overwrites if name exists."""
    file_name = os.path.basename(local_path)
    file_size = os.path.getsize(local_path)
    
    # Step 1: Notify Canvas
    step1 = requests.post(
        f"{BASE_URL}/courses/{COURSE_ID}/files",
        headers=HEADERS,
        data={
            "name": file_name,
            "size": file_size,
            "parent_folder_path": canvas_folder_name,
            "on_duplicate": "overwrite"
        }
    )
    if step1.status_code != 200:
        raise Exception(f"Step 1 failed: {step1.status_code} {step1.text}")
    
    info = step1.json()
    upload_url = info["upload_url"]
    upload_params = info["upload_params"]
    
    # Step 2: Upload (NO auth header here — this goes to Canvas's file storage)
    with open(local_path, "rb") as f:
        form_data = {k: (None, v) for k, v in upload_params.items()}
        form_data["file"] = (file_name, f)
        step2 = requests.post(upload_url, files=form_data, allow_redirects=False)
    
    # Step 3: Confirm
    location = step2.headers.get("Location")
    if not location:
        raise Exception(f"Step 2 failed: {step2.status_code} {step2.text}")
    
    step3 = requests.get(location, headers=HEADERS)
    file_data = step3.json()
    
    print(f"  Uploaded: {file_name} → ID {file_data['id']}")
    return file_data["id"], file_data["url"]
```

---

## File Linking in HTML Pages

After uploading a file, embed a download link in your page HTML:

```python
file_id, file_url = upload_file("module-01-foundations/files/lecture-slides.pptx", "Module 1")

html = f"""
<p>Download the slides: 
  <a href="{file_url}" target="_blank">Lecture Slides (PPTX)</a>
</p>
"""
```

**Important:** Use `on_duplicate: overwrite` when uploading. This preserves the file's URL even when the content is replaced — so links in pages remain valid after file updates.

---

## Course Structure JSON

The master blueprint that drives the sync script. Here is an example for Ethics and Governance:

```json
[
  {
    "module_name": "Module 1: Foundations of Ethics",
    "position": 1,
    "items": [
      {
        "type": "subheader",
        "title": "Topic 1 - Ethical Theories and Frameworks",
        "indent": 0
      },
      {
        "type": "page",
        "title": "Lecture - Ethical Theories and Frameworks",
        "file": "module-01-foundations/lecture.html",
        "indent": 1,
        "upload_files": ["module-01-foundations/files/lecture-slides.pptx"]
      },
      {
        "type": "page",
        "title": "Tutorial - Ethical Dilemmas in Practice",
        "file": "module-01-foundations/tutorial.html",
        "indent": 1,
        "upload_files": [
          "module-01-foundations/files/case-study.pdf",
          "module-01-foundations/files/tutorial-questions.docx"
        ]
      }
    ]
  }
]
```

---

## HTML Page Template

Pages use a consistent design system. Adjust the colours below to match your preferred branding.

```html
<div style="font-family: Calibri, sans-serif; max-width: 900px; margin: 0 auto;">

  <!-- Header Banner -->
  <div style="background-color: #0a1628; padding: 30px; border-radius: 8px; margin-bottom: 30px;">
    <h1 style="color: #2ec4b6; font-family: Georgia, serif; margin: 0 0 8px 0;">PAGE TITLE</h1>
    <p style="color: #ffffff; margin: 0; font-size: 16px;">Ethics and Governance</p>
  </div>

  <!-- Section with accent bar -->
  <div style="border-left: 4px solid #2ec4b6; padding-left: 20px; margin-bottom: 30px;">
    <h2 style="font-family: Georgia, serif; color: #0a1628;">Section Title</h2>
    <p>Content here.</p>
  </div>

  <!-- Grey content block -->
  <div style="background-color: #f4f6f9; padding: 24px; border-radius: 8px; margin-bottom: 24px;">
    <h2 style="font-family: Georgia, serif; color: #0a1628;">Section Title</h2>
    <p>Content here.</p>
  </div>

  <!-- Key Takeaway Box -->
  <div style="background-color: #0a1628; border-left: 6px solid #2ec4b6; padding: 20px; border-radius: 4px; margin-bottom: 30px;">
    <h3 style="color: #2ec4b6; font-family: Georgia, serif; margin-top: 0;">Key Takeaway</h3>
    <p style="color: #ffffff; margin: 0;">Takeaway text here.</p>
  </div>

  <!-- File download links -->
  <div style="border-left: 4px solid #2ec4b6; padding-left: 20px; margin-bottom: 30px;">
    <h2 style="font-family: Georgia, serif; color: #0a1628;">Downloads</h2>
    <p><a href="FILE_URL_HERE" target="_blank">Lecture Slides (PPTX)</a></p>
    <p><a href="FILE_URL_HERE" target="_blank">Case Study (PDF)</a></p>
  </div>

</div>
```

### File URL injection pattern
In your HTML files, use a placeholder token:
```html
<a href="{{files/lecture-slides.pptx}}" target="_blank">Lecture Slides</a>
```
The sync script replaces `{{files/lecture-slides.pptx}}` with the real Canvas URL after uploading.

---

## Sync Script Architecture

The main `sync.py` follows this sequence:

1. **Load** `course_structure.json`
2. **Upload all files first** — build a mapping of `local_path → {file_id, file_url}`
3. **For each module:**
   - Find or create the module, set position
   - For each item in the structure:
     - If `subheader`: create SubHeader module item
     - If `page`: read the HTML file, inject file URLs into placeholders, find-or-create the page, add to module
4. **Log** all actions with success/failure status

---

## Common Errors & Fixes

| Error | Cause | Fix |
|-------|-------|-----|
| `ImportError: cannot import CANVAS_DOMAIN` | Typo in config.py | Check exact variable names in config.py |
| Page module item not appearing | Used `content_id` instead of `page_url` | Always use `page_url` (the slug) for Page type |
| `404` on page slug | Slug doesn't match actual page URL | Get actual slug from `response.json()["url"]` after creating page |
| File upload step 2 fails | Sending auth header to S3/upload URL | Do NOT send Authorization header in step 2 |
| Duplicate modules on re-run | No find-or-create logic | Always check existing modules before creating |
| File link breaks after update | Created new file instead of overwriting | Use `on_duplicate: overwrite` in step 1 |
| `400` on module item | Missing required field | Check `type` — SubHeader needs no content_id; Page needs page_url; File needs content_id |
| Pagination cut-off | Only reading first page of results | Use pagination loop with `response.links["next"]` |

---

## Safety Rules

- **Never auto-delete.** The sync script should never call DELETE unless explicitly told to. Flag orphaned items instead.
- **Sandpit first.** Always test with the sandpit `COURSE_ID` before switching to the live course.
- **Two course IDs in config.** Keep both sandpit and live IDs in `config.py`, comment out the one not in use.
- **Unpublished by default.** Always create pages and modules as `published: False`. Publish manually after review.
- **No credentials in code.** `ACCESS_TOKEN` stays in `config.py` only, never hardcoded elsewhere.
- **Always show scripts before running.** Claude should present any sync script for review before execution.
- **Add config.py to .gitignore.** If using Git, ensure `config.py` is never committed.
