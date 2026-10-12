# -*- coding: utf-8 -*-
"""Extract all sheets of all XLS files in AVEVA Marine Documentation to TSV + index."""
import os, sys, glob
import xlrd

SRC_DIR = r"E:\AVEVA\Marine\OH12.1.SP4\Documentation"
OUT_DIR = r"E:\aveva开发文档\PML语料\xls_tables"
os.makedirs(OUT_DIR, exist_ok=True)

def cell_str(book, sheet, r, c):
    ct = sheet.cell_type(r, c)
    if ct == xlrd.XL_CELL_EMPTY or ct == xlrd.XL_CELL_BLANK:
        return ""
    v = sheet.cell_value(r, c)
    if ct == xlrd.XL_CELL_NUMBER:
        # keep integers clean
        if v == int(v) and abs(v) < 1e15:
            return str(int(v))
        return repr(v)
    if ct == xlrd.XL_CELL_DATE:
        try:
            dt = xlrd.xldate_as_tuple(v, book.datemode)
            return "-".join(str(x) for x in dt)
        except Exception:
            return str(v)
    if ct == xlrd.XL_CELL_BOOLEAN:
        return "TRUE" if v else "FALSE"
    if ct == xlrd.XL_CELL_ERROR:
        errmap = {0: "#NULL!", 7: "#DIV/0!", 15: "#VALUE!", 23: "#REF!", 29: "#NAME?", 36: "#NUM!", 42: "#N/A"}
        return errmap.get(int(v), "#ERR_%d" % int(v))
    # text
    return str(v).replace("\r\n", "\n").replace("\r", "\n").replace("\t", " ").strip()

results = []   # (file, [ (sheet, nrows, ncols, header, nonempty_cells) ])
failures = []

files = sorted(glob.glob(os.path.join(SRC_DIR, "*.xls"))) + sorted(glob.glob(os.path.join(SRC_DIR, "**", "*.xls"), recursive=True)) + \
        sorted(glob.glob(os.path.join(SRC_DIR, "*.xlsx"))) + sorted(glob.glob(os.path.join(SRC_DIR, "**", "*.xlsx"), recursive=True))
files = sorted(set(files))

for path in files:
    base = os.path.splitext(os.path.basename(path))[0]
    try:
        book = xlrd.open_workbook(path)
    except Exception as e:
        failures.append((path, "OPEN FAIL: %r" % e))
        continue
    sheets_info = []
    for si in range(book.nsheets):
        sheet = book.sheet_by_index(si)
        sname = sheet.name
        nrows, ncols = sheet.nrows, sheet.ncols
        nonempty = 0
        header = []
        safe_sheet = "".join(ch if ch not in '\\/:*?"<>|[] ' else "_" for ch in sname)
        out_name = "%s__%s.tsv" % (base, safe_sheet)
        out_path = os.path.join(OUT_DIR, out_name)
        try:
            with open(out_path, "w", encoding="utf-8", newline="") as f:
                for r in range(nrows):
                    row_vals = [cell_str(book, sheet, r, c) for c in range(ncols)]
                    nonempty += sum(1 for v in row_vals if v != "")
                    f.write("\t".join(row_vals) + "\n")
                    if r == 0:
                        header = row_vals
            sheets_info.append((sname, nrows, ncols, header, nonempty, out_name))
        except Exception as e:
            failures.append((path, "SHEET %s FAIL: %r" % (sname, e)))
    results.append((os.path.basename(path), sheets_info))

# write index
with open(os.path.join(OUT_DIR, "_INDEX.md"), "w", encoding="utf-8") as f:
    f.write("# AVEVA Marine 12.1 SP4 Documentation — XLS 属性表提取索引\n\n")
    f.write("源目录: `%s`\n\n" % SRC_DIR)
    f.write("共 %d 个 XLS 文件，%d 个 sheet 已导出为 TSV（UTF-8，制表符分隔，空白单元格为空串）。\n\n" % (
        len(results), sum(len(s) for _, s in results)))
    f.write("| 源文件 | Sheet | 行×列 | 非空单元格 | 表头(前12列) | TSV 文件 |\n")
    f.write("|---|---|---|---|---|---|\n")
    for fname, sheets in results:
        for (sname, nrows, ncols, header, nonempty, out_name) in sheets:
            hdr = " / ".join(h for h in header[:12] if h)
            hdr = hdr.replace("|", "\\|")[:120]
            f.write("| %s | %s | %d×%d | %d | %s | `%s` |\n" % (fname, sname, nrows, ncols, nonempty, hdr, out_name))
    if failures:
        f.write("\n## 失败项\n\n")
        for p, e in failures:
            f.write("- %s — %s\n" % (p, e))
    else:
        f.write("\n（无失败项）\n")

print("FILES=%d SHEETS=%d FAIL=%d" % (len(results), sum(len(s) for _, s in results), len(failures)))
for p, e in failures:
    print("FAIL:", p, e)
