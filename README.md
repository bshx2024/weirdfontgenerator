# 🌀 Weird Font Generator (趣味字体生成器)

An ad-free, high-performance programmatically SEO-optimized (pSEO) static website containing 22+ custom aesthetic Unicode fancy font generators. It supports live copying and high-resolution PNG canvas graphics exporting with transparent backgrounds, custom outline widths, and full-color adjustment.

## 🚀 Key Features

*   **Real-time Preview Sync & Secure Export**: Synced with a visible `<img>` preview layer, allowing users to bypass strict browser sandboxing policies and download transparent PNG assets directly using buttons or native "Right-click -> Save image as...".
*   **Programmatic SEO (pSEO) Internal Linking**: Category hubs (`index.html`), tool subpages (`dist/styles/`), and cornerstone guides (`dist/articles/`) are linked together using relative paths to maximize search engine crawl efficiency.
*   **Complete Customization Grid**: Control font size, text colors, background colors, background transparency, and outline styles dynamically on a live canvas renderer.
*   **Audit-Validated Structure**: Features a built-in verification script to ensure metadata uniqueness, HTML validity, and essential component presence across all 22 long-tail subpages.

## 📂 Project Structure

```bash
├── dist/                          # Generated production-ready static site files
│   ├── index.html                 # Main hub categories page
│   ├── sitemap.xml                # Search engine sitemap
│   ├── robots.txt                 # Search engine directives
│   ├── articles/                  # Cornerstone guides (for SEO long-tail keywords)
│   │   ├── unicode-compatibility-guide.html
│   │   └── instagram-bio-aesthetic-guide.html
│   └── styles/                    # 22+ Specific font style generator pages
│       ├── barbie-font-generator.html
│       ├── weird-font-generator.html
│       └── ...
├── generate_pseo.py               # Main compilation and build engine
├── verify_pseo.py                 # Static build integrity auditing script
├── styles_db.json                 # Styles database (unicode mappings, titles, metadata, faqs)
├── weird_font_launch_plan.md      # SEO deployment roadmap & rollout phases
└── README.md                      # Documentation
```

## 🛠️ Usage & Workflow

### 1. Build the Site
Generate or update the entire static site under `dist/` based on configurations in `styles_db.json`:
```bash
python generate_pseo.py
```

### 2. Preview Locally
Start a local development server to test page load times, live canvas updates, and review submission forms:
```bash
python -m http.server 8000
```
Then navigate to `http://localhost:8000` in your web browser.

### 3. Verify Build Integrity
Run the audit check script to ensure all templates compile successfully and no files are malformed:
```bash
python verify_pseo.py
```

## 🎨 Premium UI/UX Design System

The application uses custom CSS variables to implement a modern glassmorphic look:
*   **Colors**: Sleek dark space styling (`#0b0f19`) featuring gradient headers and card boxes bordered with `#1f2937`.
*   **Typography**: Clean `Inter` body typeface, paired with specific aesthetic Google Font APIs (like `Great Vibes`, `Nosifer`, `Fredoka One`) for specific canvas generators.
*   **Interactive Elements**: CSS micro-animations on interactive copy indicators and dynamic heart-bounce animations for upvoting font cards.
