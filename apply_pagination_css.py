css_pagination = """
/* ==========================================================================
   KOMPONEN FILTER & PAGINASI MODERN (ARSIP AMAN TANPA HAPUS)
   ========================================================================== */
.table-filter-bar {
    display: flex;
    justify-content: space-between;
    align-items: center;
    flex-wrap: wrap;
    gap: 12px;
    margin-bottom: 16px;
    background: #f8fafc;
    padding: 12px 16px;
    border-radius: 10px;
    border: 1px solid #e2e8f0;
}
.table-filter-search {
    display: flex;
    align-items: center;
    gap: 8px;
    flex: 1;
    min-width: 240px;
}
.table-filter-search input {
    width: 100%;
    padding: 8px 12px;
    font-size: 13px;
    border: 1.5px solid #cbd5e1;
    border-radius: 6px;
    outline: none;
    transition: all 0.2s ease;
    background: #ffffff;
}
.table-filter-search input:focus {
    border-color: #0284c7;
    box-shadow: 0 0 0 3px rgba(2, 132, 199, 0.15);
}
.table-filter-actions {
    display: flex;
    align-items: center;
    gap: 10px;
    flex-wrap: wrap;
}
.table-filter-select {
    padding: 7px 12px;
    font-size: 12.5px;
    font-weight: 600;
    color: #334155;
    background: #ffffff;
    border: 1.5px solid #cbd5e1;
    border-radius: 6px;
    outline: none;
    cursor: pointer;
}
.pagination-container {
    display: flex;
    justify-content: space-between;
    align-items: center;
    flex-wrap: wrap;
    gap: 12px;
    margin-top: 18px;
    padding: 12px 16px;
    background: #f8fafc;
    border-radius: 8px;
    border: 1px solid #e2e8f0;
    font-size: 12.5px;
    color: #475569;
}
.pagination-controls {
    display: flex;
    align-items: center;
    gap: 5px;
    flex-wrap: wrap;
}
.pagination-btn {
    padding: 6px 12px;
    font-size: 12px;
    font-weight: 700;
    color: #334155;
    background: #ffffff;
    border: 1px solid #cbd5e1;
    border-radius: 6px;
    cursor: pointer;
    transition: all 0.15s ease;
    user-select: none;
}
.pagination-btn:hover:not(:disabled) {
    background: #0284c7;
    color: #ffffff;
    border-color: #0284c7;
}
.pagination-btn.active {
    background: #0284c7;
    color: #ffffff;
    border-color: #0284c7;
}
.pagination-btn:disabled {
    opacity: 0.4;
    cursor: not-allowed;
    background: #f1f5f9;
}
.filter-pills-bar {
    display: flex;
    gap: 8px;
    flex-wrap: wrap;
    margin-bottom: 22px;
}
.filter-pill {
    padding: 7px 16px;
    font-size: 12.5px;
    font-weight: 700;
    color: #475569;
    background: #f1f5f9;
    border: 1px solid #cbd5e1;
    border-radius: 999px;
    cursor: pointer;
    transition: all 0.2s ease;
}
.filter-pill:hover {
    background: #e2e8f0;
    color: #0f172a;
}
.filter-pill.active {
    background: #0284c7;
    color: #ffffff;
    border-color: #0284c7;
    box-shadow: 0 2px 6px rgba(2, 132, 199, 0.25);
}
"""

with open("style.css", "r", encoding="utf-8") as f:
    orig = f.read()

if ".table-filter-bar" not in orig:
    with open("style.css", "a", encoding="utf-8") as f:
        f.write(css_pagination)
    print("✔ Pagination CSS appended to style.css!")
else:
    print("Pagination CSS already in style.css")
