import os
import json
import random

db_path = r"E:\kaifa\weirdfontgenerator\styles_db.json"
output_dir = r"E:\kaifa\weirdfontgenerator\dist"
styles_dir = os.path.join(output_dir, "styles")

# Ensure output directories exist
os.makedirs(styles_dir, exist_ok=True)
import shutil
assets_dir = os.path.join(output_dir, "assets")
os.makedirs(assets_dir, exist_ok=True)
if os.path.exists("demo.webp"):
    shutil.copy("demo.webp", os.path.join(assets_dir, "demo.webp"))

# Load styles database
with open(db_path, "r", encoding="utf-8") as f:
    all_styles_data = json.load(f)

# Filter active styles to support progressive rollout phases
styles_data = [item for item in all_styles_data if item.get("status") == "active"]

def get_reviews_html(item):
    keyword = item["keyword"]
    h1 = item["h1"]
    slug = item["slug"]
    
    # Seed for deterministic generation based on slug
    seed_val = sum(ord(c) for c in slug)
    random.seed(seed_val)
    
    templates = [
        [
            "I've tried so many online converters, but this {keyword} is by far the cleanest. Zero ads and copy-pasting to my bio took less than five seconds!",
            "Very helpful! The {h1} works natively on Instagram. My profile looks so much more aesthetic now.",
            "Excellent tool. The outline canvas option is brilliant for exporting high-res PNG logos when standard Unicode isn't supported."
        ],
        [
            "Hands down the best {keyword}. Clean interface and instant copy-paste. Perfect for customizing my Discord server channel names.",
            "Highly compatible! Usually, fancy symbols turn into tofu boxes, but the monospace and bold options here render perfectly on my older Android device.",
            "Beautiful design. Simple, extremely fast, and completely free of spammy banner ads. A rare gem!"
        ],
        [
            "Exactly what I was looking for. This {keyword} makes it incredibly easy to stand out. Used the bubble and gothic letters for my TikTok captions.",
            "I love that I can customize the font size and download the text as a transparent PNG. Super useful for video editing overlays!",
            "Quick, lightweight, and works perfectly on mobile browser. Solved my bio formatting issues instantly."
        ]
    ]
    
    # Select a template set deterministically
    set_idx = len(slug) % len(templates)
    reviews = templates[set_idx]
    
    user_names = ["@AestheticBio", "@pixel_architect", "@cyber_nomad", "@gothic_vibes", "@creator_studio", "@font_fanatic", "@social_maven", "@gamer_nexus"]
    u1 = user_names[len(slug) % len(user_names)]
    u2 = user_names[(len(slug) + 3) % len(user_names)]
    
    r1 = reviews[0].format(keyword=keyword, h1=h1)
    r2 = reviews[1].format(keyword=keyword, h1=h1)
    
    html = f"""
        <section class="card reviews-section" style="margin-top: 30px;">
            <h2 style="font-size: 1.5rem; color: var(--text-color); margin-top: 0; margin-bottom: 20px; border-bottom: 1px solid var(--border-color); padding-bottom: 10px;">💬 Community Feedback & Reviews</h2>
            
            <div id="reviews-list" style="display: flex; flex-direction: column; gap: 20px; margin-bottom: 25px;">
                <!-- LocalStorage reviews will be inserted here -->
                
                <div style="background: rgba(255,255,255,0.01); border: 1px solid var(--border-color); padding: 16px; border-radius: 8px;">
                    <div style="display: flex; justify-content: space-between; margin-bottom: 8px; font-size: 0.9rem; color: var(--accent-color); font-weight: 600;">
                        <span>{u1}</span>
                        <span>⭐⭐⭐⭐⭐</span>
                    </div>
                    <p style="margin: 0; font-size: 0.95rem; line-height: 1.5; color: #d1d5db;">"{r1}"</p>
                </div>
                <div style="background: rgba(255,255,255,0.01); border: 1px solid var(--border-color); padding: 16px; border-radius: 8px;">
                    <div style="display: flex; justify-content: space-between; margin-bottom: 8px; font-size: 0.9rem; color: var(--accent-color); font-weight: 600;">
                        <span>{u2}</span>
                        <span>⭐⭐⭐⭐⭐</span>
                    </div>
                    <p style="margin: 0; font-size: 0.95rem; line-height: 1.5; color: #d1d5db;">"{r2}"</p>
                </div>
            </div>

            <!-- Add Review Form -->
            <div style="border-top: 1px dashed var(--border-color); padding-top: 20px;">
                <h3 style="font-size: 1.15rem; color: var(--text-color); margin-top: 0; margin-bottom: 15px;">✍️ Write a Review</h3>
                <form id="add-review-form" style="display: flex; flex-direction: column; gap: 12px;">
                    <div style="display: flex; gap: 15px; flex-wrap: wrap;">
                        <input type="text" id="review-username" placeholder="Your name (e.g. @GamerX)" required style="flex: 1; min-width: 150px; background: rgba(0,0,0,0.2); border: 1px solid var(--border-color); color: #fff; padding: 10px; border-radius: 6px; font-size: 0.9rem; outline: none;">
                        <select id="review-rating" style="width: 130px; background: rgba(0,0,0,0.2); border: 1px solid var(--border-color); color: #fff; padding: 10px; border-radius: 6px; font-size: 0.9rem; outline: none; cursor: pointer;">
                            <option value="5">⭐⭐⭐⭐⭐</option>
                            <option value="4">⭐⭐⭐⭐</option>
                            <option value="3">⭐⭐⭐</option>
                            <option value="2">⭐⭐</option>
                            <option value="1">⭐</option>
                        </select>
                    </div>
                    <textarea id="review-text" placeholder="Write your feedback about this font generator..." required style="width: 100%; height: 80px; background: rgba(0,0,0,0.2); border: 1px solid var(--border-color); color: #fff; padding: 10px; border-radius: 6px; font-size: 0.9rem; resize: none; outline: none; box-sizing: border-box;"></textarea>
                    <button type="submit" class="btn-copy" style="align-self: flex-start; padding: 10px 20px; font-size: 0.9rem; font-weight: 700;">Submit Review</button>
                </form>
            </div>
        </section>
    """
    return html


# Master Page Template for sub-pages
page_template = """<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{{TITLE}}</title>
    <meta name="description" content="{{DESCRIPTION}}">
    <!-- Google Fonts -->
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&{{GOOGLE_FONT_URL_PARAM}}&display=swap" rel="stylesheet">
    <style>
        :root {
            --bg-color: #0b0f19;
            --card-bg: #111827;
            --text-color: #f3f4f6;
            --accent-color: {{PRIMARY_COLOR}};
            --accent-hover: {{PRIMARY_COLOR}}cc;
            --success-color: #10b981;
            --border-color: #1f2937;
            --text-muted: #9ca3af;
            --card-shadow: 0 10px 15px -3px rgba(0, 0, 0, 0.3), 0 4px 6px -4px rgba(0, 0, 0, 0.3);
            --gradient-bg: {{BG_GRADIENT}};
        }

        body {
            font-family: 'Inter', -apple-system, BlinkMacSystemFont, sans-serif;
            background: var(--gradient-bg);
            color: var(--text-color);
            margin: 0;
            padding: 0;
            min-height: 100vh;
            display: flex;
            flex-direction: column;
            align-items: center;
        }

        /* Header Navigation */
        nav {
            width: 100%;
            max-width: 900px;
            padding: 20px;
            display: flex;
            justify-content: space-between;
            align-items: center;
            box-sizing: border-box;
        }

        nav a {
            color: var(--text-color);
            text-decoration: none;
            font-weight: 600;
            font-size: 1rem;
            transition: color 0.2s;
        }

        nav a:hover {
            color: var(--accent-color);
        }

        nav .logo {
            font-size: 1.2rem;
            display: flex;
            align-items: center;
            gap: 8px;
        }

        nav .logo span {
            color: var(--accent-color);
        }

        /* Main Container */
        main {
            width: 100%;
            max-width: 800px;
            padding: 20px;
            box-sizing: border-box;
            flex-grow: 1;
        }

        header {
            text-align: center;
            margin-bottom: 40px;
        }

        h1 {
            font-size: 2.8rem;
            margin: 0 0 12px 0;
            background: linear-gradient(135deg, #ffffff, var(--accent-color));
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            font-weight: 800;
            letter-spacing: -0.02em;
        }

        p.subtitle {
            color: var(--text-muted);
            font-size: 1.1rem;
            margin: 0;
            line-height: 1.5;
        }

        /* Generator Section */
        .card {
            background-color: var(--card-bg);
            border: 1px solid var(--border-color);
            border-radius: 16px;
            padding: 24px;
            box-shadow: var(--card-shadow);
            margin-bottom: 30px;
        }

        .input-label {
            display: block;
            font-size: 0.875rem;
            text-transform: uppercase;
            letter-spacing: 0.05em;
            color: var(--text-muted);
            margin-bottom: 8px;
            font-weight: 600;
        }

        textarea {
            width: 100%;
            height: 110px;
            background-color: rgba(255, 255, 255, 0.03);
            border: 1px solid var(--border-color);
            border-radius: 10px;
            color: var(--text-color);
            font-size: 1.25rem;
            padding: 16px;
            box-sizing: border-box;
            resize: none;
            outline: none;
            transition: border-color 0.2s;
        }

        textarea:focus {
            border-color: var(--accent-color);
        }

        /* Output Row */
        .output-card {
            display: flex;
            flex-direction: column;
            gap: 15px;
            margin-top: 20px;
        }

        .output-row {
            display: flex;
            background-color: rgba(255, 255, 255, 0.02);
            border: 1px solid var(--border-color);
            border-radius: 10px;
            padding: 18px;
            justify-content: space-between;
            align-items: center;
            gap: 20px;
        }

        .output-text {
            font-size: 1.5rem;
            font-family: 'Segoe UI Symbol', 'DejaVu Sans', 'Symbola', -apple-system, sans-serif;
            word-break: break-all;
            flex-grow: 1;
        }

        .btn-copy {
            background-color: var(--accent-color);
            color: #0b0f19;
            border: none;
            border-radius: 8px;
            padding: 10px 20px;
            font-size: 0.95rem;
            font-weight: 700;
            cursor: pointer;
            transition: all 0.2s;
            outline: none;
            white-space: nowrap;
        }

        .btn-copy:hover {
            background-color: var(--accent-hover);
            transform: translateY(-1px);
        }

        .btn-copy:active {
            transform: translateY(0);
        }

        .btn-copy.success {
            background-color: var(--success-color);
            color: white;
        }

        /* Canvas Exporter section (Exceed) */
        .exporter-header {
            display: flex;
            justify-content: space-between;
            align-items: center;
            margin-bottom: 20px;
        }

        .exporter-title {
            font-size: 1.25rem;
            font-weight: 700;
        }

        .badge {
            background: linear-gradient(135deg, var(--accent-color), #a855f7);
            color: white;
            font-size: 0.75rem;
            font-weight: 700;
            padding: 4px 8px;
            border-radius: 9999px;
            text-transform: uppercase;
            letter-spacing: 0.05em;
        }

        .canvas-container {
            width: 100%;
            background-color: rgba(0, 0, 0, 0.2);
            border: 1px dashed var(--border-color);
            border-radius: 10px;
            padding: 15px;
            box-sizing: border-box;
            display: flex;
            justify-content: center;
            margin-bottom: 20px;
            overflow-x: auto;
        }

        canvas {
            max-width: 100%;
            height: auto;
            border-radius: 6px;
            background-color: transparent;
        }

        .controls-grid {
            display: grid;
            grid-template-columns: 1fr 1fr;
            gap: 15px;
            margin-bottom: 20px;
        }

        @media (max-width: 600px) {
            .controls-grid {
                grid-template-columns: 1fr;
            }
        }

        .control-group {
            display: flex;
            flex-direction: column;
            gap: 6px;
        }

        .control-group label {
            font-size: 0.85rem;
            color: var(--text-muted);
            font-weight: 600;
        }

        .control-row {
            display: flex;
            align-items: center;
            gap: 10px;
        }

        .color-picker {
            border: none;
            width: 40px;
            height: 40px;
            padding: 0;
            background: none;
            cursor: pointer;
            border-radius: 6px;
            outline: none;
        }

        .color-picker::-webkit-color-swatch-wrapper {
            padding: 0;
        }
        .color-picker::-webkit-color-swatch {
            border: 1px solid var(--border-color);
            border-radius: 6px;
        }

        .slider {
            flex-grow: 1;
            accent-color: var(--accent-color);
        }

        .checkbox-group {
            display: flex;
            align-items: center;
            gap: 8px;
            font-size: 0.875rem;
            color: var(--text-muted);
        }

        .btn-export {
            width: 100%;
            background: linear-gradient(135deg, var(--accent-color), #a855f7);
            color: white;
            border: none;
            border-radius: 8px;
            padding: 12px;
            font-size: 1rem;
            font-weight: 700;
            cursor: pointer;
            transition: all 0.2s;
            display: flex;
            justify-content: center;
            align-items: center;
            gap: 8px;
        }

        .btn-export:hover {
            opacity: 0.9;
            transform: translateY(-1px);
        }

        /* Description Section */
        .desc-section {
            line-height: 1.7;
            font-size: 1.05rem;
            color: #d1d5db;
        }

        .desc-section h2 {
            font-size: 1.5rem;
            color: var(--text-color);
            margin-top: 0;
            margin-bottom: 15px;
            border-bottom: 1px solid var(--border-color);
            padding-bottom: 10px;
        }

        /* FAQ Section */
        .faq-section {
            margin-top: 40px;
            margin-bottom: 60px;
        }

        .faq-section h2 {
            font-size: 1.5rem;
            border-bottom: 1px solid var(--border-color);
            padding-bottom: 10px;
            margin-bottom: 20px;
        }

        .faq-item {
            margin-bottom: 25px;
        }

        .faq-item h3 {
            font-size: 1.15rem;
            color: var(--accent-color);
            margin: 0 0 8px 0;
        }

        .faq-item p {
            color: var(--text-muted);
            margin: 0;
            line-height: 1.6;
        }

        /* Footer */
        footer {
            width: 100%;
            max-width: 900px;
            border-top: 1px solid var(--border-color);
            padding: 20px;
            text-align: center;
            color: var(--text-muted);
            font-size: 0.875rem;
            box-sizing: border-box;
            margin-top: auto;
        }

        /* Ads-free Banner Promo (CTA) */
        .cta-banner {
            background: linear-gradient(135deg, rgba(255, 255, 255, 0.03), rgba(255, 255, 255, 0.01));
            border: 1px solid var(--border-color);
            border-radius: 12px;
            padding: 20px;
            text-align: center;
            margin-bottom: 30px;
            position: relative;
            overflow: hidden;
        }

        .cta-banner::before {
            content: '';
            position: absolute;
            top: 0;
            left: 0;
            width: 4px;
            height: 100%;
            background: var(--accent-color);
        }

        .cta-banner h3 {
            margin: 0 0 8px 0;
            font-size: 1.1rem;
            color: var(--text-color);
        }

        .cta-banner p {
            margin: 0 0 15px 0;
            font-size: 0.9rem;
            color: var(--text-muted);
        }

        .btn-cta {
            display: inline-block;
            background-color: transparent;
            color: var(--accent-color);
            border: 1px solid var(--accent-color);
            border-radius: 6px;
            padding: 8px 16px;
            font-size: 0.875rem;
            font-weight: 600;
            text-decoration: none;
            transition: all 0.2s;
        }

        .btn-cta:hover {
            background-color: var(--accent-color);
            color: #0b0f19;
        }

        /* Voting and Copy Button Group */
        .btn-group {
            display: flex;
            align-items: center;
            gap: 10px;
            flex-shrink: 0;
        }

        .btn-vote {
            background: rgba(255, 255, 255, 0.03);
            border: 1px solid var(--border-color);
            border-radius: 8px;
            color: var(--text-muted);
            padding: 10px 14px;
            font-size: 0.95rem;
            font-weight: 600;
            cursor: pointer;
            display: flex;
            align-items: center;
            gap: 8px;
            transition: all 0.2s;
            outline: none;
        }

        .btn-vote:hover {
            background: rgba(255, 255, 255, 0.08);
            border-color: rgba(239, 68, 68, 0.4);
            color: #fca5a5;
        }

        .btn-vote.liked {
            background: rgba(239, 68, 68, 0.1);
            border-color: #ef4444;
            color: #ef4444;
        }

        .btn-vote.liked .heart-icon {
            fill: #ef4444;
            stroke: #ef4444;
            animation: heartBounce 0.4s ease;
        }

        @keyframes heartBounce {
            0% { transform: scale(1); }
            50% { transform: scale(1.3); }
            100% { transform: scale(1); }
        }

        @media (max-width: 500px) {
            .output-row {
                flex-direction: column;
                align-items: stretch;
                gap: 15px;
            }
            .output-row .btn-group {
                justify-content: flex-end;
            }
        }

        @keyframes fadeIn {
            from { opacity: 0; transform: translateY(10px); }
            to { opacity: 1; transform: translateY(0); }
        }
    </style>
</head>
<body>
    <nav>
        <div class="logo">
            <a href="../index.html">🌀 WeirdFont<span>Generator</span></a>
        </div>
        <a href="../index.html">← All {{ACTIVE_STYLES_COUNT}} Styles</a>
    </nav>

    <main>
        <div style="font-size: 0.85rem; color: var(--text-muted); margin-bottom: 20px; text-align: left; width: 100%;">
            <a href="../index.html" style="color: var(--text-muted); text-decoration: none;">Home</a> &gt; 
            <a href="../index.html" style="color: var(--text-muted); text-decoration: none;">Styles</a> &gt; 
            <span style="color: var(--accent-color);">{{H1}}</span>
        </div>

        <header>
            <h1>{{H1}}</h1>
            <p class="subtitle">Type text and copy the Unicode output, or customize & download a graphic PNG transparent logo.</p>
        </header>

        <!-- Generator Section -->
        <section class="card">
            <span class="input-label">1. Enter Text</span>
            <textarea id="input-text" placeholder="Type or paste your text here..." autofocus>Hello World</textarea>
            
            <div class="output-card">
                <span class="input-label">2. Unicode Text Copy</span>
                <div class="output-row">
                    <span class="output-text" id="output-display"></span>
                    <div class="btn-group">
                        <button class="btn-vote" id="btn-vote-page" title="Vote for this style">
                            <svg class="heart-icon" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round" width="14" height="14" style="transition: transform 0.2s;"><path d="M20.84 4.61a5.5 5.5 0 0 0-7.78 0L12 5.67l-1.06-1.06a5.5 5.5 0 0 0-7.78 7.78l1.06 1.06L12 21.23l7.78-7.78 1.06-1.06a5.5 5.5 0 0 0 0-7.78z"></path></svg>
                            <span class="vote-count" id="vote-count-page">0</span>
                        </button>
                        <button class="btn-copy" id="btn-copy">Copy Unicode</button>
                    </div>
                </div>
            </div>
        </section>

        <!-- Exporter Card (Exceed) -->
        <section class="card">
            <div class="exporter-header">
                <span class="exporter-title">🖼️ Graphic PNG Avatar & Banner Exporter</span>
                <span class="badge">Exceed Tool</span>
            </div>
            
            <div class="canvas-container">
                <canvas id="export-canvas" width="800" height="250" style="display: none;"></canvas>
                <img id="export-image" alt="Preview logo" style="max-width: 100%; height: auto; border-radius: 6px; background-color: transparent;">
            </div>

            <div class="controls-grid">
                <div class="control-group">
                    <label for="font-size">Font Size</label>
                    <div class="control-row">
                        <input type="range" id="font-size" class="slider" min="20" max="100" value="60">
                        <span id="font-size-val">60px</span>
                    </div>
                </div>

                <div class="control-group">
                    <label for="font-color">Text Color</label>
                    <div class="control-row">
                        <input type="color" id="font-color" class="color-picker" value="#ffffff">
                        <input type="text" id="font-color-text" style="width: 70px; background: rgba(0,0,0,0.2); border: 1px solid var(--border-color); color: #fff; padding: 4px; border-radius: 4px; font-size: 0.85rem;" value="#ffffff">
                    </div>
                </div>

                <div class="control-group">
                    <label for="bg-color">Background Style</label>
                    <div class="control-row">
                        <input type="color" id="bg-color" class="color-picker" value="{{CANVAS_BG_DEFAULT}}">
                        <div class="checkbox-group">
                            <input type="checkbox" id="transparent-bg" checked>
                            <label for="transparent-bg">Transparent</label>
                        </div>
                    </div>
                </div>

                <div class="control-group">
                    <label for="outline-width">Outline Width</label>
                    <div class="control-row">
                        <input type="range" id="outline-width" class="slider" min="0" max="15" value="2">
                        <span id="outline-val">2px</span>
                    </div>
                </div>

                <div class="control-group">
                    <label for="outline-color">Outline Color</label>
                    <div class="control-row">
                        <input type="color" id="outline-color" class="color-picker" value="{{PRIMARY_COLOR}}">
                    </div>
                </div>
            </div>

            <button class="btn-export" id="btn-download">
                <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round"><path d="M21 15v4a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2v-4"></path><polyline points="7 10 12 15 17 10"></polyline><line x1="12" y1="15" x2="12" y2="3"></line></svg>
                Download PNG Image
            </button>
            <p style="text-align: center; font-size: 0.85rem; color: var(--text-muted); margin-top: 10px; margin-bottom: 0; line-height: 1.4;">
                💡 <i>Tip: If the download fails or cannot be opened, you can also right-click the preview image above and choose "Save image as..." to save it directly to your folder.</i>
            </p>
        </section>

        <!-- CTA Banner -->
        <section class="cta-banner">
            <h3>Need a different lettering style?</h3>
            <p>We support {{ACTIVE_STYLES_COUNT}}+ premium typography conversion styles for Discord, Instagram, and design mockups.</p>
            <a href="../index.html" class="btn-cta">Explore All {{ACTIVE_STYLES_COUNT}} Style Generators</a>
        </section>

        <!-- Description Section -->
        <section class="card desc-section">
            <h2>About {{H1}}</h2>
            <p>{{STYLE_DESCRIPTION}}</p>
        </section>

        <!-- Reviews Section -->
        {{REVIEWS_HTML}}

        <!-- FAQs Section -->
        <section class="faq-section">
            <h2>Frequently Asked Questions</h2>
            {{FAQS_HTML}}
        </section>
    </main>

    <footer>
        <div style="margin-bottom: 15px; display: flex; justify-content: center; gap: 20px; flex-wrap: wrap;">
            <a href="../index.html" style="color: var(--text-muted); text-decoration: none; font-weight: 500;">🌀 All {{ACTIVE_STYLES_COUNT}} Fonts</a>
            <a href="../articles/unicode-compatibility-guide.html" style="color: var(--text-muted); text-decoration: none; font-weight: 500;">📖 Unicode Tofu Fix Guide</a>
            <a href="../articles/instagram-bio-aesthetic-guide.html" style="color: var(--text-muted); text-decoration: none; font-weight: 500;">✨ Aesthetic Bio Design Manual</a>
        </div>
        <p>&copy; 2026 WeirdFontGenerator.xyz - Free Ad-Free Utility. Built for speed and compatibility.</p>
    </footer>

    <script>
        // Data injected by python
        const unicodeMap = {{UNICODE_MAP_JSON}};
        const algType = "{{ALGORITHM_TYPE}}";
        const canvasFontFamily = "{{CANVAS_FONT}}";

        const inputText = document.getElementById("input-text");
        const outputDisplay = document.getElementById("output-display");
        const btnCopy = document.getElementById("btn-copy");

        // Canvas element & controls
        const canvas = document.getElementById("export-canvas");
        const ctx = canvas.getContext("2d");
        const fontSizeInput = document.getElementById("font-size");
        const fontSizeVal = document.getElementById("font-size-val");
        const fontColorInput = document.getElementById("font-color");
        const fontColorText = document.getElementById("font-color-text");
        const bgColorInput = document.getElementById("bg-color");
        const transparentBgInput = document.getElementById("transparent-bg");
        const outlineWidthInput = document.getElementById("outline-width");
        const outlineVal = document.getElementById("outline-val");
        const outlineColorInput = document.getElementById("outline-color");
        const btnDownload = document.getElementById("btn-download");

        // Zalgo helpers
        const zalgoUp = ["̀", "́", "̂", "̃", "̄", "̅", "̆", "̇", "̈", "̉", "̊", "̋", "̌", "̍", "̎", "̐", "̑", "̒", "̓", "̔", "̕", "̖", "̗", "̘", "̙", "̚", "̛", "̜", "̝", "̞", "̟", "̠"];
        const zalgoDown = ["̖", "̗", "̘", "̙", "̜", "̝", "̞", "̟", "̠", "̤", "̥", "̦", "̩", "̪", "̫", "̬", "̭", "̮", "̯", "̰", "̱", "̲", "̳", "̹", "̺", "̻", "̼", "ͅ", "͇", "͈", "͉", "͊", "͋", "͌", "͍", "͎", "͏", "͐", "͑", "͒", "͓", "͔", "͕", "͖", "͗", "͘", "͙", "͚", "͛"];
        const zalgoMid = ["̕", "̛", "̀", "́", "͂", "̓", "̈́", "͋", "͌", "͍", "͎", "͏", "͐", "͑", "͒", "͓", "͔", "͕", "͖", "͗", "͘", "͙", "͚", "͛", "͆", "͇", "͈", "͉", "͊", "͋", "͌", "͍", "͎", "͏", "͐", "͑", "͒", "͓", "͔", "͕", "͖", "͗", "͘", "͙", "͚", "͛"];

        function getZalgo(text, level) {
            let result = "";
            for (let i = 0; i < text.length; i++) {
                let char = text[i];
                if (char === " " || char === "\\n") {
                    result += char;
                    continue;
                }
                result += char;
                let counts = { up: 0, down: 0, mid: 0 };
                if (level === "heavy") {
                    counts.up = 6; counts.down = 6; counts.mid = 3;
                } else if (level === "zalgo") {
                    counts.up = 3; counts.down = 3; counts.mid = 1;
                } else { // light
                    counts.up = 1; counts.down = 1; counts.mid = 0;
                }

                for (let j = 0; j < counts.up; j++) result += zalgoUp[Math.floor(Math.random() * zalgoUp.length)];
                for (let j = 0; j < counts.down; j++) result += zalgoDown[Math.floor(Math.random() * zalgoDown.length)];
                for (let j = 0; j < counts.mid; j++) result += zalgoMid[Math.floor(Math.random() * zalgoMid.length)];
            }
            return result;
        }

        // Heart text generator
        function getHeartText(text) {
            let list = text.split("");
            return list.join("♥");
        }

        // Flipped text generator
        function getReverseText(text) {
            let list = text.split("").reverse();
            return list.map(char => unicodeMap[char] || char).join("");
        }

        // Translator function
        function translateText(text) {
            if (!text) return "Hello World";
            if (algType === "zalgo") {
                return getZalgo(text, "zalgo");
            } else if (algType === "zalgo_light") {
                return getZalgo(text, "light");
            } else if (algType === "zalgo_heavy") {
                return getZalgo(text, "heavy");
            } else if (algType === "heart") {
                return getHeartText(text);
            } else if (algType === "reverse_mapping") {
                return getReverseText(text);
            } else { // standard mapping
                return text.split("").map(char => unicodeMap[char] || char).join("");
            }
        }

        // Update output text copy UI
        function updateOutput() {
            const rawText = inputText.value;
            const translated = translateText(rawText);
            outputDisplay.textContent = translated;
            drawCanvas();
        }

        // Copy button trigger
        btnCopy.onclick = () => {
            const textToCopy = outputDisplay.textContent;
            navigator.clipboard.writeText(textToCopy).then(() => {
                btnCopy.textContent = "Copied!";
                btnCopy.classList.add("success");
                setTimeout(() => {
                    btnCopy.textContent = "Copy Unicode";
                    btnCopy.classList.remove("success");
                }, 1500);
            });
        };

        // Draw dynamic canvas graphic
        function drawCanvas() {
            const text = inputText.value || "Hello World";
            const fontSize = fontSizeInput.value;
            const fontColor = fontColorInput.value;
            const bgColor = bgColorInput.value;
            const isTransparent = transparentBgInput.checked;
            const outlineWidth = outlineWidthInput.value;
            const outlineColor = outlineColorInput.value;

            // Clear canvas
            ctx.clearRect(0, 0, canvas.width, canvas.height);

            // Draw Background
            if (!isTransparent) {
                ctx.fillStyle = bgColor;
                ctx.fillRect(0, 0, canvas.width, canvas.height);
            }

            // Text configuration
            ctx.textAlign = "center";
            ctx.textBaseline = "middle";
            ctx.font = `bold ${fontSize}px ${canvasFontFamily}`;

            // Draw text stroke (outline) first
            if (parseInt(outlineWidth) > 0) {
                ctx.strokeStyle = outlineColor;
                ctx.lineWidth = outlineWidth;
                ctx.lineJoin = "round";
                ctx.strokeText(text, canvas.width / 2, canvas.height / 2);
            }

            // Draw text fill
            ctx.fillStyle = fontColor;
            ctx.fillText(text, canvas.width / 2, canvas.height / 2);

            // Update the image tag for right-click save
            const imageDisplay = document.getElementById("export-image");
            imageDisplay.src = canvas.toDataURL("image/png");
        }

        // Sync inputs & sliders
        fontSizeInput.oninput = (e) => {
            fontSizeVal.textContent = e.target.value + "px";
            drawCanvas();
        };
        outlineWidthInput.oninput = (e) => {
            outlineVal.textContent = e.target.value + "px";
            drawCanvas();
        };
        fontColorInput.oninput = (e) => {
            fontColorText.value = e.target.value;
            drawCanvas();
        };
        fontColorText.oninput = (e) => {
            if (e.target.value.match(/^#[0-9A-Fa-f]{6}$/)) {
                fontColorInput.value = e.target.value;
                drawCanvas();
            }
        };
        bgColorInput.oninput = () => {
            transparentBgInput.checked = false;
            drawCanvas();
        };
        transparentBgInput.onchange = () => {
            drawCanvas();
        };
        outlineColorInput.oninput = () => {
            drawCanvas();
        };

        // Download PNG click handler
        btnDownload.onclick = () => {
            canvas.toBlob((blob) => {
                const url = URL.createObjectURL(blob);
                const link = document.createElement("a");
                link.download = `${algType}_font_logo.png`;
                link.href = url;
                document.body.appendChild(link);
                link.click();
                document.body.removeChild(link);
                setTimeout(() => URL.revokeObjectURL(url), 100);
            }, "image/png");
        };

        // Listen for input changes
        inputText.addEventListener("input", updateOutput);
        
        // Initial draw (needs small timeout for fonts to fetch)
        window.addEventListener("load", () => {
            setTimeout(updateOutput, 800);
        });
        
        // Initializing page vote button
        const styleSlug = "{{STYLE_SLUG}}";
        const btnVotePage = document.getElementById("btn-vote-page");
        const voteCountPage = document.getElementById("vote-count-page");

        function getInitialVotes(slug) {
            let hash = 0;
            for (let i = 0; i < slug.length; i++) {
                hash = slug.charCodeAt(i) + ((hash << 5) - hash);
            }
            return Math.abs(hash % 700) + 150;
        }

        function initPageVotes() {
            if (!btnVotePage || !voteCountPage) return;
            const likedStyles = JSON.parse(localStorage.getItem("liked_styles") || "{}");
            let baseVotes = getInitialVotes(styleSlug);
            
            if (likedStyles[styleSlug]) {
                btnVotePage.classList.add("liked");
                baseVotes += 1;
            }
            voteCountPage.textContent = baseVotes.toLocaleString();
        }

        if (btnVotePage) {
            btnVotePage.onclick = (e) => {
                e.preventDefault();
                const likedStyles = JSON.parse(localStorage.getItem("liked_styles") || "{}");
                let currentVotes = parseInt(voteCountPage.textContent.replace(/,/g, "")) || 0;
                
                if (likedStyles[styleSlug]) {
                    btnVotePage.classList.remove("liked");
                    currentVotes = Math.max(0, currentVotes - 1);
                    delete likedStyles[styleSlug];
                } else {
                    btnVotePage.classList.add("liked");
                    currentVotes += 1;
                    likedStyles[styleSlug] = true;
                    
                    const svg = btnVotePage.querySelector(".heart-icon");
                    if (svg) {
                        svg.style.animation = "none";
                        svg.offsetHeight; // trigger reflow
                        svg.style.animation = "heartBounce 0.4s ease";
                    }
                }
                
                localStorage.setItem("liked_styles", JSON.stringify(likedStyles));
                voteCountPage.textContent = currentVotes.toLocaleString();
            };
        }

        initPageVotes();

        // Local reviews handling
        const reviewForm = document.getElementById("add-review-form");
        const reviewsList = document.getElementById("reviews-list");

        function loadLocalReviews() {
            if (!reviewsList) return;
            const key = `local_reviews_${styleSlug}`;
            const localReviews = JSON.parse(localStorage.getItem(key) || "[]");
            
            // Clean up existing local review DOM items first if any
            document.querySelectorAll(".local-review-item").forEach(el => el.remove());
            
            // Prepend local reviews to the list
            localReviews.forEach(review => {
                const reviewEl = createReviewDOM(review);
                reviewsList.insertBefore(reviewEl, reviewsList.firstChild);
            });
        }

        function createReviewDOM(review) {
            const div = document.createElement("div");
            div.className = "local-review-item";
            div.style = "background: rgba(255,255,255,0.02); border: 1px solid var(--border-color); padding: 16px; border-radius: 8px; margin-bottom: 10px; animation: fadeIn 0.4s ease;";
            
            const stars = "⭐".repeat(review.rating);
            div.innerHTML = `
                <div style="display: flex; justify-content: space-between; margin-bottom: 8px; font-size: 0.9rem; color: var(--accent-color); font-weight: 600;">
                    <span>${escapeHTML(review.username)}</span>
                    <span>${stars}</span>
                </div>
                <p style="margin: 0; font-size: 0.95rem; line-height: 1.5; color: #d1d5db;">"${escapeHTML(review.text)}"</p>
            `;
            return div;
        }

        function escapeHTML(str) {
            return str.replace(/&/g, "&amp;").replace(/</g, "&lt;").replace(/>/g, "&gt;").replace(/"/g, "&quot;").replace(/'/g, "&#039;");
        }

        if (reviewForm) {
            reviewForm.onsubmit = (e) => {
                e.preventDefault();
                const usernameEl = document.getElementById("review-username");
                const ratingEl = document.getElementById("review-rating");
                const textEl = document.getElementById("review-text");

                const newReview = {
                    username: usernameEl.value.trim().startsWith("@") ? usernameEl.value.trim() : "@" + usernameEl.value.trim(),
                    rating: parseInt(ratingEl.value),
                    text: textEl.value.trim(),
                    timestamp: Date.now()
                };

                const key = `local_reviews_${styleSlug}`;
                const localReviews = JSON.parse(localStorage.getItem(key) || "[]");
                localReviews.push(newReview);
                localStorage.setItem(key, JSON.stringify(localReviews));

                // Add to list dynamically
                const reviewEl = createReviewDOM(newReview);
                reviewsList.insertBefore(reviewEl, reviewsList.firstChild);

                // Reset form
                textEl.value = "";
                usernameEl.value = "";
            };
        }

        loadLocalReviews();

        // Immediate call
        updateOutput();
    </script>
</body>
</html>
"""

# HTML Template for Homepage Hub
hub_template = """<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Weird Font Generator | {{ACTIVE_STYLES_COUNT}}+ Free Online Font Generators (𝓬𝓸𝓹𝔂 & 𝓹𝓪𝓼𝓽𝓮)</title>
    <meta name="description" content="Generate {{ACTIVE_STYLES_COUNT}}+ custom aesthetic fancy text fonts with our free client-side font generator. Copy and paste cool symbols for Instagram, Discord, and TikTok.">
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800&display=swap" rel="stylesheet">
    <style>
        :root {
            --bg-color: #0b0f19;
            --card-bg: #111827;
            --text-color: #f3f4f6;
            --accent-color: #a855f7;
            --border-color: #1f2937;
            --text-muted: #9ca3af;
        }

        body {
            font-family: 'Inter', sans-serif;
            background: linear-gradient(135deg, #0b0f19, #1e1b4b);
            color: var(--text-color);
            margin: 0;
            padding: 0;
            min-height: 100vh;
            display: flex;
            flex-direction: column;
            align-items: center;
        }

        /* Header Navigation */
        .site-header {
            position: sticky;
            top: 0;
            width: 100%;
            background-color: rgba(11, 15, 25, 0.75);
            backdrop-filter: blur(12px);
            -webkit-backdrop-filter: blur(12px);
            border-bottom: 1px solid rgba(255, 255, 255, 0.05);
            display: flex;
            justify-content: center;
            z-index: 1000;
        }

        nav {
            width: 100%;
            max-width: 1000px;
            padding: 16px 20px;
            display: flex;
            justify-content: space-between;
            align-items: center;
            box-sizing: border-box;
        }

        nav a {
            color: var(--text-color);
            text-decoration: none;
            font-weight: 700;
        }

        nav .logo span {
            color: var(--accent-color);
        }

        .ad-tag {
            font-size: 0.8rem;
            color: var(--text-muted);
            font-weight: 600;
            background-color: rgba(168, 85, 247, 0.1);
            color: var(--accent-color);
            padding: 4px 12px;
            border-radius: 9999px;
            border: 1px solid rgba(168, 85, 247, 0.2);
            text-transform: uppercase;
            letter-spacing: 0.05em;
        }

        main {
            width: 100%;
            max-width: 1000px;
            padding: 20px;
            box-sizing: border-box;
        }

        /* Hero Split Layout */
        .hero-container {
            display: grid;
            grid-template-columns: 1.2fr 0.8fr;
            gap: 40px;
            align-items: center;
            margin-bottom: 60px;
            margin-top: 20px;
        }

        .hero-left {
            display: flex;
            flex-direction: column;
            gap: 20px;
        }

        .hero-left header {
            text-align: left;
            margin: 0;
        }

        .hero-left h1 {
            font-size: 3rem;
            line-height: 1.2;
            margin: 0 0 16px 0;
            background: linear-gradient(135deg, #ffffff, var(--accent-color));
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            font-weight: 800;
            letter-spacing: -0.03em;
        }

        .hero-left p.subtitle {
            color: var(--text-muted);
            font-size: 1.1rem;
            line-height: 1.6;
            text-align: left;
            margin: 0 0 10px 0;
            max-width: 100%;
        }

        .hero-left .input-card {
            background-color: var(--card-bg);
            border: 1px solid var(--border-color);
            border-radius: 16px;
            padding: 24px;
            box-shadow: 0 10px 15px -3px rgba(0, 0, 0, 0.3);
            margin-bottom: 0;
        }

        .hero-right {
            display: flex;
            justify-content: center;
            align-items: center;
        }

        /* Browser Mockup Window */
        .browser-mockup {
            width: 100%;
            background-color: #111827;
            border: 1px solid var(--border-color);
            border-radius: 12px;
            box-shadow: 0 20px 25px -5px rgba(0, 0, 0, 0.4), 0 10px 10px -5px rgba(0, 0, 0, 0.4);
            overflow: hidden;
            transition: transform 0.3s ease, box-shadow 0.3s ease, border-color 0.3s ease;
        }

        .browser-mockup:hover {
            transform: translateY(-4px);
            box-shadow: 0 25px 30px -5px rgba(168, 85, 247, 0.15), 0 15px 15px -5px rgba(0, 0, 0, 0.4);
            border-color: var(--accent-color);
        }

        .browser-header {
            display: flex;
            align-items: center;
            padding: 10px 16px;
            background-color: #1f2937;
            border-bottom: 1px solid var(--border-color);
            gap: 8px;
        }

        .browser-dot {
            width: 8px;
            height: 8px;
            border-radius: 50%;
            background-color: #374151;
        }

        .browser-dot.red { background-color: #ef4444; }
        .browser-dot.yellow { background-color: #eab308; }
        .browser-dot.green { background-color: #22c55e; }

        .browser-address {
            flex-grow: 1;
            background-color: #111827;
            border: 1px solid var(--border-color);
            border-radius: 6px;
            padding: 4px 12px;
            font-size: 0.75rem;
            color: var(--text-muted);
            text-align: left;
            margin-left: 12px;
            font-family: monospace;
            overflow: hidden;
            text-overflow: ellipsis;
            white-space: nowrap;
        }

        .browser-body {
            position: relative;
            width: 100%;
            padding-top: 56.25%; /* 16:9 Aspect Ratio */
            background-color: #0b0f19;
        }

        .browser-body img {
            position: absolute;
            top: 0;
            left: 0;
            width: 100%;
            height: 100%;
            object-fit: cover;
            border: none;
        }

        @media (max-width: 768px) {
            .hero-container {
                grid-template-columns: 1fr;
                gap: 30px;
            }
            .hero-left h1 {
                font-size: 2.8rem;
                text-align: center;
            }
            .hero-left p.subtitle {
                text-align: center;
            }
            .hero-left header {
                text-align: center;
            }
            .hero-right {
                display: none; /* Hide mockup on mobile for faster loading */
            }
        }

        textarea {
            width: 100%;
            height: 110px;
            background-color: rgba(255, 255, 255, 0.03);
            border: 1px solid var(--border-color);
            border-radius: 10px;
            color: var(--text-color);
            font-size: 1.3rem;
            padding: 16px;
            box-sizing: border-box;
            resize: none;
            outline: none;
            transition: border-color 0.2s;
        }

        textarea:focus {
            border-color: var(--accent-color);
        }

        /* Styles Grid */
        .grid-header {
            font-size: 1.25rem;
            font-weight: 700;
            margin-bottom: 20px;
            border-left: 4px solid var(--accent-color);
            padding-left: 10px;
        }

        .styles-grid {
            display: grid;
            grid-template-columns: 1fr 1fr;
            gap: 20px;
        }

        @media (max-width: 768px) {
            .styles-grid {
                grid-template-columns: 1fr;
            }
        }

        .style-card {
            background-color: var(--card-bg);
            border: 1px solid var(--border-color);
            border-radius: 12px;
            padding: 20px;
            display: flex;
            flex-direction: column;
            justify-content: space-between;
            gap: 15px;
            transition: transform 0.2s, box-shadow 0.2s;
        }

        .style-card:hover {
            transform: translateY(-2px);
            box-shadow: 0 10px 20px rgba(0,0,0,0.2);
            border-color: var(--accent-color);
        }

        .card-top {
            display: flex;
            justify-content: space-between;
            align-items: center;
        }

        .style-title {
            font-weight: 700;
            font-size: 1.1rem;
            text-decoration: none;
            color: var(--text-color);
        }

        .style-title:hover {
            color: var(--accent-color);
        }

        .cpc-badge {
            background-color: rgba(16, 185, 129, 0.1);
            color: #10b981;
            font-size: 0.75rem;
            padding: 2px 8px;
            border-radius: 9999px;
            font-weight: 600;
        }

        .style-preview {
            font-size: 1.3rem;
            color: #e5e7eb;
            font-family: 'Segoe UI Symbol', 'DejaVu Sans', 'Symbola', -apple-system, sans-serif;
            word-break: break-all;
            min-height: 40px;
            display: flex;
            align-items: center;
        }

        .card-actions {
            display: flex;
            justify-content: space-between;
            align-items: center;
            margin-top: 5px;
        }

        .btn-card-copy {
            background-color: var(--accent-color);
            color: #0b0f19;
            border: none;
            border-radius: 6px;
            font-weight: 700;
            padding: 8px 16px;
            font-size: 0.875rem;
            cursor: pointer;
            transition: opacity 0.2s;
        }

        .btn-card-copy:hover {
            opacity: 0.9;
        }

        .btn-card-copy.success {
            background-color: #10b981;
            color: white;
        }

        .link-details {
            font-size: 0.85rem;
            color: var(--text-muted);
            text-decoration: none;
            transition: color 0.2s;
        }

        .link-details:hover {
            color: var(--accent-color);
            text-decoration: underline;
        }

        .btn-vote {
            background: rgba(255, 255, 255, 0.03);
            border: 1px solid var(--border-color);
            border-radius: 6px;
            color: var(--text-muted);
            padding: 6px 10px;
            font-size: 0.85rem;
            font-weight: 600;
            cursor: pointer;
            display: flex;
            align-items: center;
            gap: 6px;
            transition: all 0.2s;
            outline: none;
        }

        .btn-vote:hover {
            background: rgba(255, 255, 255, 0.08);
            border-color: rgba(239, 68, 68, 0.4);
            color: #fca5a5;
        }

        .btn-vote.liked {
            background: rgba(239, 68, 68, 0.1);
            border-color: #ef4444;
            color: #ef4444;
        }

        .btn-vote.liked .heart-icon {
            fill: #ef4444;
            stroke: #ef4444;
            animation: heartBounce 0.4s ease;
        }

        @keyframes heartBounce {
            0% { transform: scale(1); }
            50% { transform: scale(1.3); }
            100% { transform: scale(1); }
        }

        .guide-card {
            background-color: var(--card-bg);
            border: 1px solid var(--border-color);
            border-radius: 12px;
            padding: 24px;
            display: flex;
            flex-direction: column;
            justify-content: space-between;
            gap: 15px;
            transition: all 0.2s;
        }
        
        .guide-card:hover {
            border-color: var(--accent-color);
            transform: translateY(-2px);
            box-shadow: 0 10px 20px rgba(0,0,0,0.2);
        }

        .guide-card h3 {
            margin-top: 0;
            margin-bottom: 10px;
            font-size: 1.25rem;
            line-height: 1.3;
        }

        .guide-card h3 a {
            color: white;
            text-decoration: none;
            transition: color 0.2s;
        }

        .guide-card h3 a:hover {
            color: var(--accent-color);
        }

        /* Description Section */
        .info-section {
            margin-top: 50px;
            line-height: 1.7;
            color: #d1d5db;
        }

        .info-section h2 {
            color: white;
            font-size: 1.6rem;
            border-bottom: 1px solid var(--border-color);
            padding-bottom: 10px;
            margin-bottom: 15px;
        }

        footer {
            width: 100%;
            max-width: 1100px;
            border-top: 1px solid var(--border-color);
            padding: 20px;
            text-align: center;
            color: var(--text-muted);
            font-size: 0.875rem;
            margin-top: 60px;
        }
    </style>
</head>
<body>
    <header class="site-header">
        <nav>
            <div class="logo">🌀 WeirdFont<span>Generator</span></div>
            <div class="ad-tag">Ad-Free Utility</div>
        </nav>
    </header>

    <main>
        <div class="hero-container">
            <div class="hero-left">
                <header>
                    <h1>Weird Font Generator</h1>
                    <p class="subtitle">Generate {{ACTIVE_STYLES_COUNT}}+ custom aesthetic Unicode fancy fonts for Instagram bios, Discord profiles, and gaming tags instantly.</p>
                </header>

                <section class="input-card">
                    <textarea id="input-text" placeholder="Type or paste your text here..." autofocus>Hello World</textarea>
                </section>
            </div>
            <div class="hero-right">
                <div class="browser-mockup">
                    <div class="browser-header">
                        <div class="browser-dot red"></div>
                        <div class="browser-dot yellow"></div>
                        <div class="browser-dot green"></div>
                        <div class="browser-address">weirdfontgenerator.com/styles/cursive-font-generator.html</div>
                    </div>
                    <div class="browser-body">
                        <img src="./assets/demo.webp" alt="Fancy Font Copy Paste Demo" />
                    </div>
                </div>
            </div>
        </div>

        <section>
            <div class="grid-header">Available Styles (Click title to customize or export PNG)</div>
            <div class="styles-grid" id="styles-grid">
{{CARDS_HTML}}
            </div>
        </section>

        <!-- Featured Guides & Tutorials -->
        <section style="margin-top: 50px;">
            <div class="grid-header" style="border-left-color: #a855f7;">📖 Featured Guides & Tutorials</div>
            <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 20px; margin-top: 20px;">
                <div class="guide-card">
                    <div>
                        <h3><a href="./articles/unicode-compatibility-guide.html">Unicode Fancy Fonts Compatibility Guide: How to Fix Tofu</a></h3>
                        <p style="color: var(--text-muted); font-size: 0.95rem; line-height: 1.5; margin: 0;">Learn why some special symbols turn into blank boxes (tofu) on Android or Discord, and discover the high-compatibility Unicode blocks to keep your text readable everywhere.</p>
                    </div>
                    <a href="./articles/unicode-compatibility-guide.html" style="color: var(--accent-color); text-decoration: none; font-weight: 600; font-size: 0.95rem;">Read Guide →</a>
                </div>
                <div class="guide-card">
                    <div>
                        <h3><a href="./articles/instagram-bio-aesthetic-guide.html">How to Design the Ultimate Instagram & Discord Bio</a></h3>
                        <p style="color: var(--text-muted); font-size: 0.95rem; line-height: 1.5; margin: 0;">Make your social media profiles pop! Explore spacing codes, layout templates, and font styling tricks for Instagram, Discord, and TikTok names.</p>
                    </div>
                    <a href="./articles/instagram-bio-aesthetic-guide.html" style="color: var(--accent-color); text-decoration: none; font-weight: 600; font-size: 0.95rem;">Read Manual →</a>
                </div>
            </div>
        </section>

        <section class="info-section">
            <h2>About Weird Font Generator</h2>
            <p>Our Weird Font Generator is a pure client-side utility built for creators, designers, and gamers. We convert standard characters into unique mathematical alphanumeric symbols, gothic blackletters, and bubble characters defined in the Unicode standard. This allows you to copy and paste customized fonts directly into Instagram, TikTok, Twitter/X, and Discord without needing custom font files.</p>
            <p>Unlike other cluttered font styling portals, we offer a fast, 100% ad-free experience, direct image exporting, and dedicated sub-pages for specific aesthetics like death metal, bubble text, and Chicano cursive designs.</p>
        </section>
    </main>

    <footer>
        <div style="margin-bottom: 15px; display: flex; justify-content: center; gap: 20px; flex-wrap: wrap;">
            <a href="./articles/unicode-compatibility-guide.html" style="color: var(--text-muted); text-decoration: none; font-weight: 500;">📖 Unicode Tofu Fix Guide</a>
            <a href="./articles/instagram-bio-aesthetic-guide.html" style="color: var(--text-muted); text-decoration: none; font-weight: 500;">✨ Aesthetic Bio Design Manual</a>
        </div>
        <p>&copy; 2026 WeirdFontGenerator.xyz - Ad-Free Unicode Tool. All rights reserved.</p>
    </footer>

    <script>
        // Inject styles database summary for preview mapping
        const stylesList = {{STYLES_LIST_JSON}};

        const input = document.getElementById("input-text");

        // Zalgo helpers
        const zalgoUp = ["̀", "́", "̂", "̃", "̄", "̅", "̆", "̇", "̈", "̉", "̊", "̋", "̌", "̍", "̎", "̐", "̑", "̒", "̓", "̔", "̕", "̖", "̗", "̘", "̙", "̚", "̛", "̜", "̝", "̞", "̟", "̠"];
        const zalgoDown = ["̖", "̗", "̘", "̙", "̜", "̝", "̞", "̟", "̠", "̤", "̥", "̦", "̩", "̪", "̫", "̬", "̭", "̮", "̯", "̰", "̱", "̲", "̳", "̹", "̺", "̻", "̼", "ͅ", "͇", "͈", "͉", "͊", "͋", "͌", "͍", "͎", "͏", "͐", "͑", "͒", "͓", "͔", "͕", "͖", "͗", "͘", "͙", "͚", "͛"];
        
        function getZalgo(text, count) {
            let result = "";
            for (let i = 0; i < text.length; i++) {
                let char = text[i];
                if (char === " " || char === "\\n") { result += char; continue; }
                result += char;
                for (let j = 0; j < count; j++) {
                    result += zalgoUp[Math.floor(Math.random() * zalgoUp.length)];
                    result += zalgoDown[Math.floor(Math.random() * zalgoDown.length)];
                }
            }
            return result;
        }

        function translateForStyle(text, style) {
            if (!text) text = "Hello World";
            const type = style.algorithm_type;
            const map = style.unicode_map;

            if (type.startsWith("zalgo")) {
                let count = type === "zalgo_heavy" ? 4 : (type === "zalgo" ? 2 : 1);
                return getZalgo(text, count);
            } else if (type === "heart") {
                return text.split("").join("♥");
            } else if (type === "reverse_mapping") {
                return text.split("").reverse().map(c => map[c] || c).join("");
            } else {
                return text.split("").map(c => map[c] || c).join("");
            }
        }

        function renderGrid() {
            const text = input.value || "Hello World";
            stylesList.forEach(style => {
                const converted = translateForStyle(text, style);
                const previewEl = document.getElementById(`preview-${style.slug}`);
                if (previewEl) {
                    previewEl.textContent = converted;
                }
            });
        }

        // Copy button event delegation
        document.addEventListener("click", (e) => {
            if (e.target && e.target.classList.contains("btn-card-copy")) {
                const targetId = e.target.getAttribute("data-target");
                const previewEl = document.getElementById(targetId);
                if (previewEl) {
                    navigator.clipboard.writeText(previewEl.textContent).then(() => {
                        const originalText = e.target.textContent;
                        e.target.textContent = "Copied!";
                        e.target.classList.add("success");
                        setTimeout(() => {
                            e.target.textContent = originalText;
                            e.target.classList.remove("success");
                        }, 1500);
                    });
                }
            }
        });

        // Initializing votes for cards
        function initVotes() {
            const likedStyles = JSON.parse(localStorage.getItem("liked_styles") || "{}");
            
            document.querySelectorAll(".btn-vote").forEach(btn => {
                const slug = btn.getAttribute("data-slug");
                let baseVotes = getInitialVotes(slug);
                
                if (likedStyles[slug]) {
                    btn.classList.add("liked");
                    baseVotes += 1;
                }
                
                const countEl = btn.querySelector(".vote-count");
                if (countEl) {
                    countEl.textContent = baseVotes.toLocaleString();
                }
            });
        }

        function getInitialVotes(slug) {
            let hash = 0;
            for (let i = 0; i < slug.length; i++) {
                hash = slug.charCodeAt(i) + ((hash << 5) - hash);
            }
            return Math.abs(hash % 700) + 150;
        }

        // Vote click delegation
        document.addEventListener("click", (e) => {
            const btn = e.target.closest(".btn-vote");
            if (btn) {
                e.preventDefault();
                const slug = btn.getAttribute("data-slug");
                const likedStyles = JSON.parse(localStorage.getItem("liked_styles") || "{}");
                const countEl = btn.querySelector(".vote-count");
                let currentVotes = parseInt(countEl.textContent.replace(/,/g, "")) || 0;
                
                if (likedStyles[slug]) {
                    // Unlike
                    btn.classList.remove("liked");
                    currentVotes = Math.max(0, currentVotes - 1);
                    delete likedStyles[slug];
                } else {
                    // Like
                    btn.classList.add("liked");
                    currentVotes += 1;
                    likedStyles[slug] = true;
                    
                    // Bounce animation
                    const svg = btn.querySelector(".heart-icon");
                    if (svg) {
                        svg.style.animation = "none";
                        svg.offsetHeight; // Trigger reflow
                        svg.style.animation = "heartBounce 0.4s ease";
                    }
                }
                
                localStorage.setItem("liked_styles", JSON.stringify(likedStyles));
                countEl.textContent = currentVotes.toLocaleString();
            }
        });

        input.addEventListener("input", renderGrid);
        renderGrid();
        initVotes();
    </script>
</body>
</html>
"""

# Generate 22 Sub-Pages
for item in styles_data:
    # Prepare FAQs HTML
    faqs_html = ""
    for faq in item["faqs"]:
        faqs_html += f"""            <div class="faq-item">
                <h3>{faq['q']}</h3>
                <p>{faq['a']}</p>
            </div>\n"""
            
    # Add a generic faq if less than 2
    if len(item["faqs"]) < 2:
        faqs_html += f"""            <div class="faq-item">
                <h3>Will this copy-paste font work on Instagram?</h3>
                <p>Yes, all output text is formatted in native Unicode characters, making it highly compatible with Instagram bios, TikTok captions, and Discord posts.</p>
            </div>\n"""

    # Font parameters for Google Fonts link loading
    # e.g., 'Fredoka+One' or 'Cinzel:wght@700'
    font_family_clean = item["canvas_font"].split(",")[0].strip()
    google_font_url_param = f"family={font_family_clean.replace(' ', '+')}"
    if ":" not in google_font_url_param:
        # Load bold variants if supported
        google_font_url_param += ":wght@400;700"

    # Merge placeholders
    html_content = page_template
    html_content = html_content.replace("{{ACTIVE_STYLES_COUNT}}", str(len(styles_data)))
    html_content = html_content.replace("{{TITLE}}", item["title"])
    html_content = html_content.replace("{{DESCRIPTION}}", item["description"])
    html_content = html_content.replace("{{H1}}", item["h1"])
    html_content = html_content.replace("{{GOOGLE_FONT_URL_PARAM}}", google_font_url_param)
    html_content = html_content.replace("{{PRIMARY_COLOR}}", item["primary_color"])
    html_content = html_content.replace("{{BG_GRADIENT}}", item["bg_gradient"])
    html_content = html_content.replace("{{STYLE_DESCRIPTION}}", item["style_description"])
    html_content = html_content.replace("{{ALGORITHM_TYPE}}", item["algorithm_type"])
    html_content = html_content.replace("{{CANVAS_FONT}}", item["canvas_font"])
    html_content = html_content.replace("{{CANVAS_BG_DEFAULT}}", item["canvas_bg"])
    html_content = html_content.replace("{{FAQS_HTML}}", faqs_html)
    
    # JSON-encoded unicode map and parameters for safe injection into JS
    unicode_map_json = json.dumps(item["unicode_map"], ensure_ascii=False)
    html_content = html_content.replace("{{UNICODE_MAP_JSON}}", unicode_map_json)
    html_content = html_content.replace("{{STYLE_SLUG}}", item["slug"])
    html_content = html_content.replace("{{REVIEWS_HTML}}", get_reviews_html(item))

    # Output file path
    file_name = f"{item['slug']}.html"
    file_path = os.path.join(styles_dir, file_name)
    
    with open(file_path, "w", encoding="utf-8") as out_f:
        out_f.write(html_content)

print(f"Success: Generated {len(styles_data)} sub-pages in {styles_dir}")

# Generate Homepage index.html
# Prepare a compact version of styles database for JS injection into the homepage
compact_styles_list = []
for item in styles_data:
    compact_styles_list.append({
        "slug": item["slug"],
        "h1": item["h1"],
        "cpc": item["cpc"],
        "algorithm_type": item["algorithm_type"],
        "unicode_map": item["unicode_map"]
    })

# Helper Python mapping logic for static pre-rendering
import random
zalgo_up = ["̀", "́", "̂", "̃", "̄", "̅", "̆", "̇", "̈", "̉", "̊", "̋", "̌", "̍", "̎", "̐", "̑", "̒", "̓", "̔", "̕", "̖", "̗", "̘", "̙", "̚", "̛", "̜", "̝", "̞", "̟", "̠"]
zalgo_down = ["̖", "̗", "̘", "̙", "̜", "̝", "̞", "̟", "̠", "̤", "̥", "̦", "̩", "̪", "̫", "̬", "̭", "̮", "̯", "̰", "̱", "̲", "̳", "̹", "̺", "̻", "̼", "ͅ", "͇", "͈", "͉", "͊", "͋", "͌", "͍", "͎", "͏", "͐", "͑", "͒", "͓", "͔", "͕", "͖", "͗", "͘", "͙", "͚", "͛"]

def get_zalgo_py(text, count):
    random.seed(42)  # Seed for deterministic static rendering
    result = ""
    for c in text:
        if c in [" ", "\n"]:
            result += c
            continue
        result += c
        for _ in range(count):
            result += random.choice(zalgo_up) + random.choice(zalgo_down)
    return result

def translate_python(text, item):
    alg = item["algorithm_type"]
    unicode_map = item["unicode_map"]
    if not text:
        text = "Hello World"
    if alg == "zalgo":
        return get_zalgo_py(text, 2)
    elif alg == "zalgo_light":
        return get_zalgo_py(text, 1)
    elif alg == "zalgo_heavy":
        return get_zalgo_py(text, 4)
    elif alg == "heart":
        return "♥".join(list(text))
    elif alg == "reverse_mapping":
        return "".join(unicode_map.get(c, c) for c in text[::-1])
    else:
        return "".join(unicode_map.get(c, c) for c in text)

# Pre-render 22 Style Cards statically
cards_html = ""
for item in styles_data:
    converted = translate_python("Hello World", item)
    cpc_badge = f'<span class="cpc-badge">CPC ${item["cpc"]:.2f}</span>' if item["cpc"] > 0 else ""
    cards_html += f"""                <div class="style-card" data-slug="{item['slug']}">
                    <div class="card-top">
                        <a class="style-title" href="./styles/{item['slug']}.html">{item['h1']}</a>
                        {cpc_badge}
                    </div>
                    <div class="style-preview" id="preview-{item['slug']}">{converted}</div>
                    <div class="card-actions">
                        <div style="display: flex; align-items: center; gap: 8px;">
                            <button class="btn-vote" data-slug="{item['slug']}" title="Vote for this style">
                                <svg class="heart-icon" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round" width="14" height="14" style="transition: transform 0.2s;"><path d="M20.84 4.61a5.5 5.5 0 0 0-7.78 0L12 5.67l-1.06-1.06a5.5 5.5 0 0 0-7.78 7.78l1.06 1.06L12 21.23l7.78-7.78 1.06-1.06a5.5 5.5 0 0 0 0-7.78z"></path></svg>
                                <span class="vote-count" id="votes-{item['slug']}">0</span>
                            </button>
                            <a class="link-details" href="./styles/{item['slug']}.html">Customize & Export PNG →</a>
                        </div>
                        <button class="btn-card-copy" data-target="preview-{item['slug']}">Copy</button>
                    </div>
                </div>\n"""

homepage_content = hub_template.replace("{{STYLES_LIST_JSON}}", json.dumps(compact_styles_list, ensure_ascii=False))
homepage_content = homepage_content.replace("{{CARDS_HTML}}", cards_html)
homepage_content = homepage_content.replace("{{ACTIVE_STYLES_COUNT}}", str(len(styles_data)))
homepage_path = os.path.join(output_dir, "index.html")

with open(homepage_path, "w", encoding="utf-8") as out_h:
    out_h.write(homepage_content)

print(f"Success: Generated homepage index.html at {homepage_path}")

# ----------------------------------------------------
# Generate Cornerstone Articles (Content Ring)
# ----------------------------------------------------
articles_dir = os.path.join(output_dir, "articles")
os.makedirs(articles_dir, exist_ok=True)

article_template = """<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{{TITLE}}</title>
    <meta name="description" content="{{DESCRIPTION}}">
    <!-- Google Fonts -->
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800&display=swap" rel="stylesheet">
    <style>
        :root {
            --bg-color: #0b0f19;
            --card-bg: #111827;
            --text-color: #f3f4f6;
            --accent-color: #a855f7;
            --border-color: #1f2937;
            --text-muted: #9ca3af;
            --gradient-bg: linear-gradient(135deg, #0b0f19, #1e1b4b);
        }

        body {
            font-family: 'Inter', -apple-system, BlinkMacSystemFont, sans-serif;
            background: var(--gradient-bg);
            color: var(--text-color);
            margin: 0;
            padding: 0;
            min-height: 100vh;
            display: flex;
            flex-direction: column;
            align-items: center;
        }

        nav {
            width: 100%;
            max-width: 900px;
            padding: 20px;
            display: flex;
            justify-content: space-between;
            align-items: center;
            box-sizing: border-box;
        }

        nav a {
            color: var(--text-color);
            text-decoration: none;
            font-weight: 600;
            font-size: 1rem;
            transition: color 0.2s;
        }

        nav a:hover {
            color: var(--accent-color);
        }

        nav .logo {
            font-size: 1.2rem;
            display: flex;
            align-items: center;
            gap: 8px;
        }

        nav .logo span {
            color: var(--accent-color);
        }

        main {
            width: 100%;
            max-width: 800px;
            padding: 20px;
            box-sizing: border-box;
            flex-grow: 1;
        }

        .breadcrumb {
            font-size: 0.875rem;
            color: var(--text-muted);
            margin-bottom: 20px;
        }

        .breadcrumb a {
            color: var(--text-muted);
            text-decoration: none;
        }

        .breadcrumb a:hover {
            color: var(--accent-color);
            text-decoration: underline;
        }

        header {
            margin-bottom: 30px;
        }

        h1 {
            font-size: 2.5rem;
            margin: 0 0 12px 0;
            background: linear-gradient(135deg, #ffffff, var(--accent-color));
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            font-weight: 800;
            letter-spacing: -0.02em;
            line-height: 1.2;
        }

        .meta-info {
            font-size: 0.875rem;
            color: var(--text-muted);
            display: flex;
            gap: 15px;
        }

        /* Article Content style */
        .article-body {
            line-height: 1.8;
            font-size: 1.1rem;
            color: #d1d5db;
        }

        .article-body h2 {
            font-size: 1.6rem;
            color: white;
            margin-top: 40px;
            margin-bottom: 15px;
            border-bottom: 1px solid var(--border-color);
            padding-bottom: 8px;
        }

        .article-body h3 {
            font-size: 1.25rem;
            color: var(--accent-color);
            margin-top: 30px;
            margin-bottom: 12px;
        }

        .article-body p {
            margin-top: 0;
            margin-bottom: 20px;
        }

        .article-body ul, .article-body ol {
            margin-bottom: 20px;
            padding-left: 20px;
        }

        .article-body li {
            margin-bottom: 10px;
        }

        .article-body code {
            background-color: rgba(255, 255, 255, 0.08);
            padding: 2px 6px;
            border-radius: 4px;
            font-family: monospace;
            color: #fca5a5;
        }

        /* Internal Links Grid (Content Ring) */
        .related-tools-box {
            background-color: var(--card-bg);
            border: 1px solid var(--border-color);
            border-radius: 12px;
            padding: 24px;
            margin-top: 50px;
            margin-bottom: 40px;
        }

        .related-tools-box h3 {
            margin-top: 0;
            margin-bottom: 15px;
            color: white;
        }

        .tools-links-grid {
            display: grid;
            grid-template-columns: 1fr 1fr;
            gap: 12px;
        }

        @media (max-width: 500px) {
            .tools-links-grid {
                grid-template-columns: 1fr;
            }
        }

        .tools-links-grid a {
            color: var(--text-color);
            text-decoration: none;
            font-size: 0.95rem;
            padding: 8px 12px;
            background-color: rgba(255, 255, 255, 0.02);
            border: 1px solid var(--border-color);
            border-radius: 6px;
            transition: all 0.2s;
        }

        .tools-links-grid a:hover {
            border-color: var(--accent-color);
            color: var(--accent-color);
            background-color: rgba(168, 85, 247, 0.05);
        }

        footer {
            width: 100%;
            max-width: 900px;
            border-top: 1px solid var(--border-color);
            padding: 20px;
            text-align: center;
            color: var(--text-muted);
            font-size: 0.875rem;
            box-sizing: border-box;
            margin-top: auto;
        }
    </style>
</head>
<body>
    <nav>
        <div class="logo">
            <a href="../index.html">🌀 WeirdFont<span>Generator</span></a>
        </div>
        <a href="../index.html">← Go to Main Tool</a>
    </nav>

    <main>
        <div class="breadcrumb">
            <a href="../index.html">Home</a> &gt; <a href="#">Guides</a> &gt; {{BREADCRUMB_CURRENT}}
        </div>

        <article>
            <header>
                <h1>{{H1}}</h1>
                <div class="meta-info">
                    <span>📅 Published: June 2026</span>
                    <span>✍️ Author: Typography Expert</span>
                </div>
            </header>

            <div class="article-body">
                {{CONTENT_HTML}}
            </div>
        </article>

        <!-- Content Ring Internal Links -->
        <section class="related-tools-box">
            <h3>Try Our Aesthetic Font Generators</h3>
            <p style="color: var(--text-muted); font-size: 0.95rem; margin-bottom: 20px;">Instantly convert your text with our zero-ads, client-side generators:</p>
            <div class="tools-links-grid">
                {{TOOLS_LINKS_HTML}}
            </div>
        </section>
    </main>

    <footer>
        <p>&copy; 2026 WeirdFontGenerator.xyz - Free Ad-Free Utility. All rights reserved.</p>
    </footer>
</body>
</html>
"""

# Pre-render links for the Content Ring inside articles
tools_links_html = ""
for item in styles_data:
    tools_links_html += f'                <a href="../styles/{item["slug"]}.html">🌀 {item["h1"]}</a>\n'

articles_data = [
    {
        "file_name": "unicode-compatibility-guide.html",
        "title": "Unicode Fancy Fonts Compatibility Guide: How to Fix Tofu (Missing Glyphs) - WeirdFontGenerator",
        "description": "Why do some Unicode fonts display as blank square boxes (tofu)? Learn how Unicode blocks work, and how to fix missing glyph compatibility on Discord, Instagram, and older Windows/Android devices.",
        "breadcrumb": "Unicode Compatibility Guide",
        "h1": "Unicode Fancy Text Compatibility & Tofu (Missing Glyph) Repair Guide",
        "content": """
<p>If you have ever used an online custom font changer, you have probably noticed that some stylized characters display perfectly on your laptop but turn into blank rectangles, question marks inside boxes, or empty space when viewed on an older Android phone or in a game chat. In the world of web typography, this phenomenon is widely known as <strong>"Tofu"</strong> (named after the blank white blocks of bean curd it resembles).</p>

<h2>What Causes the "Tofu" Missing Glyph Error?</h2>
<p>To understand tofu, we first need to understand how custom Unicode generators work. When you type "Hello" and convert it to bubble text (<code>ⓗⓔⓛⓛⓞ</code>) or script (<code>𝓱𝓮𝓵𝓵𝓸</code>), our utility does not actually load a custom <code>.ttf</code> or <code>.otf</code> font file. Instead, it translates standard ASCII letters into corresponding mathematical alphanumeric symbols or enclosing character blocks defined in the native <strong>Unicode Standard</strong>.</p>
<p>Every device has a local font library (such as Segoe UI on Windows, San Francisco on macOS/iOS, or Roboto on Android). If your device's font family does not contain glyph drawings (drawings for characters) in the specific high-level Unicode block requested (like U+1F170 for squared letters), the operating system's rendering engine fails and outputs a default fallback symbol: the tofu box.</p>

<h2>Device and Platform Compatibility Breakdown</h2>
<ul>
    <li><strong>iOS and macOS (99% Compatibility)</strong>: Apple devices feature robust system font libraries with extensive Unicode coverage. Almost all script, gothic, bold sans, and bubble layouts render flawlessly here.</li>
    <li><strong>Windows (90% Compatibility)</strong>: Modern Windows 10 and 11 feature solid fallback mapping, but older builds lack glyphs for enclosed squared alphabets. Standard mathematical sans/serif structures display fine.</li>
    <li><strong>Older Android (75% Compatibility)</strong>: Older Android versions (Nougat, Oreo) often have stripped-down system fonts to save disk space, leading to frequent tofu rendering of complex Unicode characters.</li>
</ul>

<h2>How to Fix and Workaround Tofu Formatting</h2>
<h3>1. Prioritize High-Compatibility Unicode Styles</h3>
<p>When sharing copy-pasted text to a general audience (like an Instagram Bio or a public Discord Server), avoid using experimental, complex symbols. Instead, choose layouts that map to highly compatible mathematical blocks. The following styles feature maximum compatibility across almost all modern systems:</p>
<ul>
    <li><strong>Monospace Text</strong> (e.g., <code>𝙷𝚎𝚕𝚕𝚘 𝚠𝚘𝚛𝚕𝚍</code>) - supported universally by programmers' fonts.</li>
    <li><strong>Bold Sans-Serif</strong> (e.g., <code>𝗛𝗲𝗹𝗹ο 𝗪𝗼𝗿𝗹𝗱</code>) - maps directly to clean bold glyphs.</li>
    <li><strong>Bold Serif</strong> (e.g., <code>𝐇𝐞𝐥𝐥𝐨 𝐖𝐨𝐫𝐥𝐝</code>) - highly readable and standard.</li>
    <li><strong>Double-Struck / Blackboard Bold</strong> (e.g., <code>ℍ𝕖𝕝𝕝𝕠 𝕎𝕠𝕣𝕝𝕕</code>) - widely used and supported.</li>
    <li><strong>Italic Sans</strong> (e.g., <code>𝘏𝘦𝘭𝘭𝘰 𝘞𝘰𝘳𝘭𝘥</code>) - clean and light cursive style.</li>
</ul>

<h3>2. The Ultimate Escape Hatch: Export as Graphic PNG</h3>
<p>If you absolutely need a specific aesthetic font layout (like gothic, cursive, or outline) for your gamer avatar, Discord server logo, or website heading, copy-paste Unicode text might let you down due to platform restrictions. Steam and many online games ban non-ASCII symbols in usernames altogether to prevent spoofing.</p>
<p>To overcome this, use our built-in <strong>Graphic PNG Exporter</strong>. Instead of copying raw text, adjust your text color, sizing, outlines, and download a transparent background graphic. Since it is rendered locally on a canvas to a standard image file, it will display identically and beautifully on 100% of platforms, without ever rendering as a tofu block!</p>
"""
    },
    {
        "file_name": "instagram-bio-aesthetic-guide.html",
        "title": "How to Design the Ultimate Instagram & Discord Bio: Aesthetic Font & Layout Manual - WeirdFontGenerator",
        "description": "Make your social profiles pop! Explore professional typography layouts, spacing codes (U+3000), and custom font combinations for Instagram, Discord, and TikTok bios.",
        "breadcrumb": "Bio Aesthetic Manual",
        "h1": "How to Design the Ultimate Instagram & Discord Bio: Typography & Aesthetic Layout Manual",
        "content": """
<p>Your social media bio is your digital billboard. You only have a few seconds to hook a profile visitor before they click away. Standard, plain text can look boring and lack character. Using aesthetic typography, spacing, and emojis is the easiest way to immediately stand out and project your creative identity.</p>
<p>However, overusing fancy lettering or mismatching styles can make your bio unreadable and messy. Here is a professional design manual for formatting the perfect bio layout for Instagram, TikTok, and Discord.</p>

<h2>The Golden Rules of Bio Typography</h2>
<ol>
    <li><strong>Readability is King</strong>: Only stylize key terms, titles, or your username. Keep your email address, business location, and main description in standard text so it remains accessible and screen-reader friendly.</li>
    <li><strong>Use Ideographic Spaces for Alignment</strong>: Normal spacebars often collapse when pasted into Instagram bios, ruining centered text alignments. Use the Unicode ideographic space code (<code>U+3000</code>) to insert clean, non-collapsing indents.</li>
    <li><strong>Limit to Two Font Styles</strong>: Mashing gothic, bubbles, and cursive together looks chaotic. Pick one primary aesthetic font for your name/headers, and keep the rest clean and cohesive.</li>
</ol>

<h2>3 Ready-to-Copy Bio Layout Templates</h2>

<h3>🖤 1. The Hardcore Gamer / Dark Aesthetic (Discord & Twitch)</h3>
<p>Perfect for streamers, esports players, and dark aesthetic fans. This theme relies on structured gothic lines and heavy glyphs.</p>
<p><strong>Design Blueprint:</strong></p>
<pre>
⚔️ 𝕸𝖊𝖙𝖆𝖑 𝕼𝖚𝖊𝖊𝖓
🎮 FPS Competitor | Twitch Affiliate
┌──────────────┐
  playing: Valorant
└──────────────┘
✉️ collab: business@email.com
</pre>
<p><em>Setup Tip:</em> Generate your name header using our <a href="../styles/metal-font-generator.html">Metal Font Generator</a> or <a href="../styles/death-metal-font-generator.html">Death Metal Font Generator</a> for that extreme metal band emblem vibe.</p>

<h3>💖 2. The Y2K Cute / Soft Barbie Aesthetic (Instagram & TikTok)</h3>
<p>Best for lifestyle vloggers, beauty creators, and aesthetic moodboards. It utilizes cursive flow and cute heart separators.</p>
<p><strong>Design Blueprint:</strong></p>
<pre>
✨ 𝓬𝓾𝓽𝓮 & 𝓬𝓸𝔃𝔂 ✨
💌 l𝐢𝐟𝐞𝐬𝐭𝐲𝐥𝐞 • f𝐚𝐬𝐡𝐢𝐨𝐧 • Y2K
H♥o♥p♥e♥ ♥y♥o♥u♥ ♥s♥t♥a♥y♥
🛍️ Shop my style link below! ↓
</pre>
<p><em>Setup Tip:</em> Get elegant script headers from our <a href="../styles/barbie-font-generator.html">Barbie Font Generator</a> and spacing hearts from the <a href="../styles/heart-font-generator.html">Heart Font Generator</a>.</p>

<h3>📐 3. The Minimalist / Creative Designer Aesthetic (Instagram & X)</h3>
<p>Ideal for photographers, graphic designers, programmers, and startup founders. It utilizes clean, structured sans-serif blocks.</p>
<p><strong>Design Blueprint:</strong></p>
<pre>
🌀 𝚂𝚃𝚄𝙳𝙸𝙾 𝙽𝙾𝙸𝚂𝙴
📷 Visual Storytelling | Tokyo
📍 𝕊𝔽 / 𝕋𝕠𝕜𝕪𝕠
🔗 portfolio.design
</pre>
<p><em>Setup Tip:</em> Generate your brand subtitle in high-compatibility monospace letters using <a href="../styles/brat-font-generator.html">Brat Font Generator</a>, or add sleek double-struck symbols via the <a href="../styles/san-francisco-font-text-generator.html">San Francisco Font Generator</a>.</p>

<h2>Testing and Launching Your Bio</h2>
<p>Before saving your bio on your live profile, paste it into a temporary notes app on both your desktop and phone. Check if all characters load without rendering tofu boxes, and verify that the line breaks look correct on mobile viewport screens. By combining strategic Unicode lettering with clean layouts, you will create a profile page that looks polished, premium, and distinct!</p>
"""
    }
]

# Generate Article Files
for art in articles_data:
    art_content = article_template
    art_content = art_content.replace("{{TITLE}}", art["title"])
    art_content = art_content.replace("{{DESCRIPTION}}", art["description"])
    art_content = art_content.replace("{{BREADCRUMB_CURRENT}}", art["breadcrumb"])
    art_content = art_content.replace("{{H1}}", art["h1"])
    art_content = art_content.replace("{{CONTENT_HTML}}", art["content"])
    art_content = art_content.replace("{{TOOLS_LINKS_HTML}}", tools_links_html)
    
    art_path = os.path.join(articles_dir, art["file_name"])
    with open(art_path, "w", encoding="utf-8") as out_art:
        out_art.write(art_content)

print(f"Success: Generated {len(articles_data)} cornerstone articles at {articles_dir}")

# ----------------------------------------------------
# Generate Sitemap & Robots.txt
# ----------------------------------------------------
base_url = "https://www.weirdfontgenerator.xyz"

sitemap_xml = f"""<?xml version="1.0" encoding="UTF-8"?>
<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">
    <!-- Homepage -->
    <url>
        <loc>{base_url}/</loc>
        <changefreq>daily</changefreq>
        <priority>1.0</priority>
    </url>
"""

# Add articles
for art in articles_data:
    sitemap_xml += f"""    <url>
        <loc>{base_url}/articles/{art['file_name']}</loc>
        <changefreq>weekly</changefreq>
        <priority>0.8</priority>
    </url>\n"""

# Add styles
for item in styles_data:
    sitemap_xml += f"""    <url>
        <loc>{base_url}/styles/{item['slug']}.html</loc>
        <changefreq>weekly</changefreq>
        <priority>0.9</priority>
    </url>\n"""

sitemap_xml += "</urlset>\n"

sitemap_path = os.path.join(output_dir, "sitemap.xml")
with open(sitemap_path, "w", encoding="utf-8") as s_f:
    s_f.write(sitemap_xml)
print(f"Success: Generated sitemap.xml at {sitemap_path}")

robots_txt = f"""User-agent: *
Allow: /

Sitemap: {base_url}/sitemap.xml
"""

robots_path = os.path.join(output_dir, "robots.txt")
with open(robots_path, "w", encoding="utf-8") as r_f:
    r_f.write(robots_txt)
print(f"Success: Generated robots.txt at {robots_path}")
