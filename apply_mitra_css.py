# Update CSS with Mitra Slider styles
css_snippet = """
/* ==========================================================================
   INTERACTIVE MITRA & KOLABORASI SLIDER (CAROUSEL RESMI SDN INPRES ARSO VIII)
   ========================================================================== */
.mitra-slider-container {
    position: relative;
    background: #ffffff;
    border-radius: 18px;
    border: 1px solid #e2e8f0;
    box-shadow: 0 10px 30px rgba(15, 23, 42, 0.06);
    overflow: hidden;
    margin-bottom: 30px;
    transition: box-shadow 0.3s ease;
}

.mitra-slider-container:hover {
    box-shadow: 0 14px 36px rgba(15, 23, 42, 0.1);
}

.mitra-slider-topbar {
    display: flex;
    justify-content: space-between;
    align-items: center;
    flex-wrap: wrap;
    gap: 12px;
    padding: 14px 22px;
    background: #f8fafc;
    border-bottom: 1px solid #e2e8f0;
}

.mitra-nav-btn {
    width: 38px;
    height: 38px;
    border-radius: 50%;
    background: #ffffff;
    border: 1px solid #cbd5e1;
    color: #0f172a;
    font-size: 15px;
    font-weight: 700;
    cursor: pointer;
    display: inline-flex;
    align-items: center;
    justify-content: center;
    box-shadow: 0 2px 6px rgba(0, 0, 0, 0.05);
    transition: all 0.2s ease;
    user-select: none;
    -webkit-user-select: none;
}

.mitra-nav-btn:hover {
    background: #0284c7;
    color: #ffffff;
    border-color: #0284c7;
    transform: translateY(-1px);
    box-shadow: 0 4px 12px rgba(2, 132, 199, 0.25);
}

.mitra-tabs-nav {
    display: flex;
    gap: 8px;
    overflow-x: auto;
    padding: 12px 20px;
    background: #ffffff;
    border-bottom: 1px solid #f1f5f9;
    scrollbar-width: thin;
    -webkit-overflow-scrolling: touch;
}

.mitra-tab-btn {
    white-space: nowrap;
    display: inline-flex;
    align-items: center;
    gap: 6px;
    padding: 7px 15px;
    border-radius: 9999px;
    border: 1px solid #e2e8f0;
    background: #f8fafc;
    color: #475569;
    font-size: 12.5px;
    font-weight: 700;
    cursor: pointer;
    transition: all 0.2s ease;
    flex-shrink: 0;
}

.mitra-tab-btn:hover {
    background: #e0f2fe;
    color: #0369a1;
    border-color: #7dd3fc;
}

.mitra-tab-btn.active {
    background: #0284c7;
    color: #ffffff;
    border-color: #0284c7;
    box-shadow: 0 4px 12px rgba(2, 132, 199, 0.25);
}

.mitra-slider-viewport {
    position: relative;
    width: 100%;
    min-height: 440px;
}

.mitra-slide {
    display: none;
    padding: 26px 26px 20px;
    animation: mitraSlideIn 0.35s cubic-bezier(0.4, 0, 0.2, 1);
}

.mitra-slide.active {
    display: block;
}

@keyframes mitraSlideIn {
    from { opacity: 0; transform: translateY(6px); }
    to { opacity: 1; transform: translateY(0); }
}

.mitra-slide-grid {
    display: grid;
    grid-template-columns: 42% 58%;
    gap: 26px;
    align-items: start;
}

.mitra-photo-card {
    border-radius: 14px;
    overflow: hidden;
    border: 1px solid #e2e8f0;
    background: #0f172a;
    box-shadow: 0 4px 16px rgba(0, 0, 0, 0.08);
}

.mitra-photo-wrapper {
    position: relative;
    height: 280px;
    overflow: hidden;
    background: #0f172a;
}

.mitra-photo-img {
    width: 100%;
    height: 100%;
    object-fit: cover;
    display: block;
    cursor: pointer;
    transition: transform 0.4s ease;
}

.mitra-photo-img:hover {
    transform: scale(1.03);
}

.mitra-photo-badge {
    position: absolute;
    top: 12px;
    left: 12px;
    background: rgba(15, 23, 42, 0.85);
    color: #ffffff;
    font-size: 11px;
    font-weight: 700;
    padding: 4px 12px;
    border-radius: 9999px;
    backdrop-filter: blur(4px);
    pointer-events: none;
}

.mitra-photo-zoom-btn {
    position: absolute;
    bottom: 12px;
    right: 12px;
    background: rgba(2, 132, 199, 0.92);
    color: #ffffff;
    border: none;
    padding: 6px 14px;
    border-radius: 9999px;
    font-size: 11.5px;
    font-weight: 700;
    cursor: pointer;
    display: inline-flex;
    align-items: center;
    gap: 5px;
    box-shadow: 0 4px 10px rgba(0, 0, 0, 0.35);
    transition: all 0.2s ease;
}

.mitra-photo-zoom-btn:hover {
    background: #0369a1;
    transform: translateY(-1px);
}

.mitra-caption-box {
    background: #f8fafc;
    padding: 12px 16px;
    border-top: 1px solid #e2e8f0;
    display: flex;
    align-items: flex-start;
    gap: 8px;
}

.mitra-checklist-box {
    background: #f8fafc;
    border: 1px solid #e2e8f0;
    border-radius: 12px;
    padding: 18px;
    margin-bottom: 16px;
}

.mitra-checklist-list {
    margin: 0;
    padding-left: 20px;
    font-size: 13.5px;
    color: #334155;
    line-height: 1.7;
}

.mitra-checklist-list li {
    margin-bottom: 6px;
}

.mitra-meta-footer {
    display: flex;
    justify-content: space-between;
    align-items: center;
    flex-wrap: wrap;
    gap: 10px;
    font-size: 12.5px;
    color: #64748b;
    border-top: 1px dashed #cbd5e1;
    padding-top: 12px;
}

.mitra-dots-bar {
    display: flex;
    justify-content: center;
    align-items: center;
    gap: 8px;
    padding: 14px;
    background: #f8fafc;
    border-top: 1px solid #e2e8f0;
}

.mitra-dot {
    width: 10px;
    height: 10px;
    border-radius: 50%;
    background: #cbd5e1;
    border: none;
    cursor: pointer;
    transition: all 0.25s ease;
    padding: 0;
}

.mitra-dot.active {
    width: 28px;
    border-radius: 9999px;
    background: #0284c7;
}

@media (max-width: 900px) {
    .mitra-slide-grid {
        grid-template-columns: 1fr;
        gap: 20px;
    }
    .mitra-photo-wrapper {
        height: 240px;
    }
    .mitra-slide {
        padding: 18px;
    }
    .mitra-checklist-box {
        padding: 14px;
    }
}
"""

with open('css/style.css', 'r', encoding='utf-8') as f:
    css_content = f.read()

# Insert before "/* ===================================================================\n   LIGHTWEIGHT & PERFORMANCE OPTIMIZATIONS"
target_marker = "/* ===================================================================\n   LIGHTWEIGHT & PERFORMANCE OPTIMIZATIONS"

if ".mitra-slider-container" not in css_content:
    if target_marker in css_content:
        css_content = css_content.replace(target_marker, css_snippet + "\n\n" + target_marker)
    else:
        css_content += "\n\n" + css_snippet

    with open('css/style.css', 'w', encoding='utf-8') as f:
        f.write(css_content)
    print("Successfully added Mitra Slider CSS to css/style.css!")
else:
    print("Mitra Slider CSS already in css/style.css.")
