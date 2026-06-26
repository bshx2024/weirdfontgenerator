import os
import re
from pypdf import PdfReader # not needed here, but just in case

dist_dir = r"E:\kaifa\weirdfontgenerator\dist\styles"
homepage_path = r"E:\kaifa\weirdfontgenerator\dist\index.html"

# Regex patterns for basic HTML auditing
title_pat = re.compile(r"<title>(.*?)</title>", re.IGNORECASE | re.DOTALL)
desc_pat = re.compile(r'<meta\s+name=["\']description["\']\s+content="([^"]*)"', re.IGNORECASE | re.DOTALL)
h1_pat = re.compile(r"<h1>(.*?)</h1>", re.IGNORECASE | re.DOTALL)

errors = []
titles = {}
descs = {}

print("=== STARTING pSEO BUILD AUDIT ===")
print("-" * 50)

# Check Homepage
if os.path.exists(homepage_path):
    with open(homepage_path, "r", encoding="utf-8") as f:
        content = f.read()
        title_m = title_pat.search(content)
        desc_m = desc_pat.search(content)
        h1_m = h1_pat.search(content)
        
        print("✅ Homepage: index.html found")
        print(f"   -> Title: {title_m.group(1).strip() if title_m else '❌ NOT FOUND'}")
        print(f"   -> Desc: {desc_m.group(1).strip() if desc_m else '❌ NOT FOUND'}")
        print(f"   -> H1: {h1_m.group(1).strip() if h1_m else '❌ NOT FOUND'}")
else:
    errors.append("Homepage index.html is missing!")

# Check 22 Sub-pages
if not os.path.exists(dist_dir):
    errors.append("Styles sub-directory is missing!")
else:
    files = [f for f in os.listdir(dist_dir) if f.endswith(".html")]
    print(f"\n🔍 Found {len(files)} sub-pages in dist/styles/")
    
    if len(files) != 22:
        errors.append(f"Expected 22 pages, found {len(files)}")

    for file in files:
        path = os.path.join(dist_dir, file)
        with open(path, "r", encoding="utf-8") as f:
            content = f.read()
            
            title_m = title_pat.search(content)
            desc_m = desc_pat.search(content)
            h1_m = h1_pat.search(content)
            
            # Check Title
            if not title_m:
                errors.append(f"{file} has no <title> tag!")
            else:
                title = title_m.group(1).strip()
                if title in titles:
                    errors.append(f"Duplicate title found: '{title}' in {file} and {titles[title]}")
                titles[title] = file
                
            # Check Meta Description
            if not desc_m:
                errors.append(f"{file} has no meta description!")
            else:
                desc = desc_m.group(1).strip()
                if desc in descs:
                    errors.append(f"Duplicate description found in {file} and {descs[desc]}")
                descs[desc] = file
                if len(desc) < 50 or len(desc) > 160:
                    print(f"⚠️  {file} meta description length is suboptimal ({len(desc)} chars)")

            # Check H1
            if not h1_m:
                errors.append(f"{file} has no <h1> tag!")
            else:
                h1 = h1_m.group(1).strip()
                # Verify that H1 matches the slug keywords roughly
                slug_words = file.replace("-font-generator.html", "").replace(".html", "").replace("-", " ")
                if slug_words not in h1.lower():
                    print(f"⚠️  {file} H1 ('{h1}') might not align with file slug '{file}'")
                    
            # Check Canvas Exporter & Copy Button
            if "export-canvas" not in content:
                errors.append(f"{file} is missing the HTML5 Canvas Exporter element!")
            if "btn-copy" not in content:
                errors.append(f"{file} is missing the Copy Button element!")
            if "faq-section" not in content:
                errors.append(f"{file} is missing the FAQs section!")

print("-" * 50)
if errors:
    print(f"❌ AUDIT FAILED with {len(errors)} errors:")
    for err in errors:
        print(f"  - {err}")
else:
    print("🏆 AUDIT PASSED: All 22 pages and index.html are perfectly formatted, unique, and contain core pSEO and canvas components!")
print("=================================")
