# -*- coding: utf-8 -*-
"""Theme mining v2: tree-aware DEX chain building, cleaned tokens, cross-validation."""
import io, os, re, glob

TSV = r"E:\aveva开发文档\PML语料\xls_tables"
OUT = os.path.join(TSV, "_ANALYSIS.md")
rep = []
def w(s=""):
    rep.append(s)

def read_tsv(name):
    with io.open(os.path.join(TSV, name), encoding="utf-8") as f:
        return [line.rstrip("\n").split("\t") for line in f]

# ---------- 1. All_logical_names ----------
w("## 1. All_logical_names.xls —— 实际内容：环境变量总表（非 DB 属性清单）\n")
rows = read_tsv("All_logical_names__Sheet1.tsv")
hdr, data = rows[0], [r for r in rows[1:] if any(c.strip() for c in r)]
w("表头: %s；数据行 %d\n" % (" | ".join(hdr), len(data)))
types = collections_C = __import__("collections").Counter()
for r in data:
    types[r[1].strip() if len(r) > 1 and r[1].strip() else "(空)"] += 1
w("- 按类型: %s\n" % ", ".join("%s=%d" % kv for kv in types.most_common()))
databanks = sorted(r[0] for r in data if len(r) > 1 and r[1].strip() == "databank")
w("- databank 型环境变量 %d 个: %s\n" % (len(databanks), ", ".join(databanks)))

# ---------- 2. Attributes_func ----------
w("\n## 2. Attributes_func.xls —— TDM 支持矩阵与功能访问控制\n")
rows = read_tsv("Attributes_func__App1._TDM_Basic_Attributes.tsv")
objs = [r[0].strip() for r in rows[2:] if r and r[0].strip()]
w("- App1. TDM Basic Attributes（%d 对象）: %s —— 每个 Tribon 对象支持 TDM 属性/用户自定义属性与否的 X 矩阵\n" % (len(objs), "、".join(objs)))
rows = read_tsv("Attributes_func__App4._TDM_FuncAccContr.tsv")
funcs = [r[0].strip() for r in rows[1:] if r and r[0].strip()]
gr = __import__("collections").Counter(f.split(".")[0] for f in funcs)
w("- App4. TDM FuncAccContr: %d 个受控功能（模块.操作→描述），分布 %s\n" % (len(funcs), ", ".join("%s=%d" % kv for kv in gr.most_common())))

# ---------- 3. DEX extraction ----------
w("\n## 3. DEX 关键词 → DB 属性映射\n")

def split_alts(kw):
    """'LONGITUDINAL / TRANSVERSAL' -> ['LONGITUDINAL','TRANSVERSAL']"""
    return [p.strip() for p in kw.split("/") if p.strip()]

def expand_kw(kw):
    """'STIF[FENER] (i)' -> full='STIFFENER', abbrev='STIF' ; strip (i)/() markers."""
    kw = kw.strip()
    kw = re.sub(r"\([^)]*\)", "", kw).strip()          # drop (i), (), (1:n)
    m = re.match(r"^([A-Za-z][A-Za-z0-9_]*)\[([^\]]*)\]$", kw)
    if m:
        return m.group(1) + m.group(2).replace("_", "").replace("S", "S"), m.group(1)
    return kw, kw

# 3a. master file (flat rows)
master_rows = read_tsv("Data_Extraction_to_Attributes__Sheet1.tsv")
master_data = [r for r in master_rows[1:] if any(c.strip() for c in r)]
kw_tokens = set()                 # cleaned FULL-form keyword tokens
kw_rawcells = set()               # raw keyword cells (kept verbatim)
chains_master = set()
noun_counter = __import__("collections").Counter()
attr_counter = __import__("collections").Counter()
pair_set = set()
na_rows = 0
sec_header_rows = []
for r in master_data:
    r = (r + [""] * 12)[:12]
    kws = [r[c].strip() for c in range(7) if r[c].strip()]
    if not kws:
        continue
    for cell in kws:
        kw_rawcells.add(cell)
        for alt in split_alts(cell):
            full, abbr = expand_kw(alt)
            if re.match(r"^[A-Z][A-Z0-9_]*$", full) and len(full) >= 2:
                kw_tokens.add(full)
    chains_master.add(" ".join(kws))
    noun = r[7].strip()
    attr = r[8].strip()
    if attr == "#N/A" or not noun:
        na_rows += 1
    elif noun:
        noun_counter[noun] += 1
    if attr and attr != "#N/A":
        for tok in attr.split("/"):
            tok = tok.strip().split()[0] if tok.strip() else ""
            if re.match(r"^[A-Z][A-Z0-9_]*$", tok):
                attr_counter[tok] += 1
        if noun and noun != "#N/A":
            pair_set.add("%s.%s" % (noun, attr.split()[0]))

w("### 3a. Data_Extraction_to_Attributes.xls（主映射表）\n")
w("- 数据行 %d（其中 Noun=#N/A 即无直接 DB 映射的行 %d），唯一关键词链 %d 条\n" % (len(master_data), na_rows, len(chains_master)))
w("- DB Noun（记录类型）%d 种，DB Attribute（属性名）%d 种，Noun.Attribute 组合 %d 组\n"
  % (len(noun_counter), len(attr_counter), len(pair_set)))
w("- Noun 频次前 20: %s\n" % ", ".join("%s(%d)" % kv for kv in noun_counter.most_common(20)))
w("- Attribute 频次前 30: %s\n" % ", ".join("%s(%d)" % kv for kv in attr_counter.most_common(30)))

# 3b. DatExt files (tree layout, carry-forward chains)
datext_files = sorted(set(glob.glob(os.path.join(TSV, "Dat[Ee]xt_*.tsv"))))
chains_ext = set()
ext_rows = 0
ext_files_info = []
for fp in datext_files:
    rowsx = read_tsv(os.path.basename(fp))
    hdr2 = rowsx[0]
    kcols = sum(1 for h in hdr2 if h.strip().lower().startswith("keyword"))
    parents = []          # carried-forward chain
    nfile = 0
    for r in rowsx[1:]:
        if not any(c.strip() for c in r):
            continue
        r = (r + [""] * (kcols + 5))[:kcols + 5]
        cells = [r[c].strip() for c in range(kcols)]
        if not any(cells):
            continue
        depth = max([i for i, c in enumerate(cells) if c and c != "*"] or [-1])
        kwcell = cells[depth] if depth >= 0 else ""
        ext_rows += 1
        if not kwcell or kwcell.lower().startswith("see "):
            continue
        full, abbr = expand_kw(split_alts(kwcell)[0])
        parents = parents[:depth] + [full]
        chain = " ".join(parents)
        if re.match(r"^[A-Z][A-Z0-9_]*$", full.strip()) and len(full.strip()) >= 2:
            chains_ext.add(" ".join(parents))
            kw_tokens.add(full.strip())
        nfile += 1
    ext_files_info.append((os.path.basename(fp).replace(".tsv", ""), kcols, nfile))

w("\n### 3b. 28 个 DatExt/Datext 文件（25 个 DatExt_* + 3 个 Datext_Drawing/TDM/Volume；树状层级，父关键词向上继承；关键词为缩写[X]括号记法，* 为层级占位符）\n")
w("- 数据行 %d，继承展开后唯一 DEX 关键词链 %d 条\n" % (ext_rows, len(chains_ext)))
w("- 合计：主表 + DatExt 唯一关键词 token %d 个\n" % len(kw_tokens))
w("- 各文件（sheet 关键词列数 / 数据行）: %s\n" % "; ".join("%s(%d列,%d行)" % t for t in ext_files_info))

# return-type codes in DatExt Output column
out_types = __import__("collections").Counter()
for fp in datext_files:
    rowsx = read_tsv(os.path.basename(fp))
    kcols = sum(1 for h in rowsx[0] if h.strip().lower().startswith("keyword"))
    for r in rowsx[1:]:
        if len(r) > kcols + 2 and r[kcols + 2].strip() and r[kcols + 2].strip() != "Output":
            out_types[r[kcols + 2].strip()] += 1
w("- DatExt Output 返回类型码分布: %s（i=整数 s=字符串 n*r=n个实数）\n" % ", ".join("%s=%d" % kv for kv in out_types.most_common(10)))

# ---------- 4. compare with §6 ----------
w("\n## 4. 与 Marine-Hull船体建模语句大全.md §6 DEX 字符串表对照\n")
hull = io.open(r"E:\aveva开发文档\Marine-Hull船体建模语句大全.md", encoding="utf-8").read()
m6 = re.search(r"## 6\. kcs_dex.*?\n(.*?)\n---", hull, re.S)
sec6 = m6.group(1) if m6 else ""
sec6_upper = {t for t in re.findall(r"\.([A-Za-z][A-Za-z0-9_]*)", sec6) if t.upper() == t and len(t) >= 2}
sec6_upper |= {"HULL", "BLOCK", "PANEL", "CPAN", "CPANEL", "PLATE", "STRUCT", "ITEM", "GROUP", "PART"}
# abbreviations used in DatExt notation
abbrev_forms = set()
for cell in kw_rawcells:
    for alt in split_alts(cell):
        full, abbr = expand_kw(alt)
        if abbr:
            abbrev_forms.add(abbr)
shared = sorted(t for t in kw_tokens if t in sec6_upper)
new_tokens = sorted(t for t in kw_tokens if t not in sec6_upper and t not in sec6_upper and (t in abbrev_forms or t not in sec6_upper))
new_tokens = sorted(t for t in kw_tokens if t not in sec6_upper)
w("- §6 手册样例表关键词 %d 个；XLS 关键词 token（完整形）%d 个；共有 %d；**XLS 新增 %d 个**\n"
  % (len(sec6_upper), len(kw_tokens), len(shared), len(new_tokens)))
w("- §6 已含: %s\n" % ", ".join(sorted(sec6_upper)))
w("- XLS 新增（全部）: %s\n" % ", ".join(new_tokens))

# mapping samples for a few key new tokens from master
w("\n- 主表新增关键词映射样例:\n")
want = ["COG", "WEIGHT", "XLIMIT", "YLIMIT", "ZLIMIT", "ASSEMBLY_ID", "FUNCTIONALDESC", "QUALITY", "THICKNESS", "DESIGNATION", "TYPE_CODE", "DATE", "DATA_TYPE", "LIMITS", "ISEAM", "SEAM", "CUTOUT", "HOLE", "NOTCH", "BEVEL"]
seen = set()
for r in master_data:
    r = (r + [""] * 12)[:12]
    kws = [r[c].strip() for c in range(7) if r[c].strip()]
    for t in kws:
        for alt in split_alts(t):
            full, _ = expand_kw(alt)
            if full in want and full not in seen:
                seen.add(full)
                w("  - %s -> Noun=%s Attr=%s%s" % (".".join(kws), r[7].strip(), r[8].strip(), (" | " + r[9].strip() if len(r) > 9 and r[9].strip() else "")))
w("\n- DatExt 新增关键词链样例（每文件 3 条）:\n")
for fp in datext_files[:8] + datext_files[-4:]:
    rowsx = read_tsv(os.path.basename(fp))
    kcols = sum(1 for h in rowsx[0] if h.strip().lower().startswith("keyword"))
    parents = []
    shown = 0
    for r in rowsx[1:]:
        if not any(c.strip() for c in r):
            continue
        r = (r + [""] * (kcols + 5))[:kcols + 5]
        cells = [r[c].strip() for c in range(kcols)]
        if not any(cells):
            continue
        depth = max([i for i, c in enumerate(cells) if c and c != "*"] or [-1])
        kwcell = cells[depth] if depth >= 0 else ""
        if not kwcell or kwcell.lower().startswith("see "):
            continue
        full, abbr = expand_kw(split_alts(kwcell)[0])
        parents = parents[:depth] + [kwcell]
        if len(parents) >= 4 and shown < 3:
            w("  - %s: %s → %s" % (os.path.basename(fp).split("__")[0], ".".join(parents), r[kcols + 1].strip()[:60]))
            shown += 1

# ---------- 5. cross-validation with 296 ----------
w("\n## 5. 交叉验证：DEX/DB 属性名 vs Marine-属性操作写法全编.md §1a 296 名清单\n")
att = io.open(r"E:\aveva开发文档\Marine-属性操作写法全编.md", encoding="utf-8").read()
m1a = re.search(r"### 1a\..*?\n(.*?)\n### 1b\.", att, re.S)
sec1a = m1a.group(1) if m1a else ""
names_296 = set()
raw_tokens = []
freq_lines = 0
for line in sec1a.splitlines():
    ls = line.strip()
    if ls.startswith("-") and "次" in ls and "`" in ls:
        freq_lines += 1
        for mt in re.finditer(r"`([^`]+)`", ls):
            for n in mt.group(1).split():
                n = n.strip(",;()")
                if re.match(r"^[A-Za-z][A-Za-z0-9_]*$", n):
                    raw_tokens.append(n)
                    names_296.add(n)
w("- 从 §1a 频次行（%d 行）解析出列名 token %d 个、去重（区分大小写合并）后 %d 个；手册标题声称 296，差值属手册内部计数口径（大小写变体各计/省略项）\n" % (freq_lines, len(raw_tokens), len(names_296)))
low296 = {x.lower() for x in names_296}
db_attrs = set(attr_counter.keys())
inter = sorted(t for t in db_attrs if t.lower() in low296)
diff = sorted(t for t in db_attrs if t.lower() not in low296)
w("- DEX 主表 DB Attribute 名 %d 个（全大写、已滤 #N/A）；与 §1a 交集 %d 个: %s\n" % (len(db_attrs), len(inter), ", ".join(inter) if inter else "（无）"))
w("- **差集（属性表有、296 名清单没有）%d 个（全部列出）**: %s\n" % (len(diff), ", ".join(diff)))
w("- 差集解读: 这批是 Tribon Hull DB 的 DEX 输出属性（如 %s），属 Hull 专用 DB 记录字段；296 名清单来自全树 PML2 `!!ce.x=` 写入（Design/PML 世界，以管件/结构 PML 对象为主）， Hull DB 字段几乎不经过 PML2 直写，故差集大属预期。\n" % ", ".join(diff[:8]))
w("- 反向参考: All_logical_names.xls 为环境变量表（366 项），与属性名无关，未参与本对照。\n")

with io.open(OUT, "w", encoding="utf-8") as f:
    f.write("\n".join(rep))
print("OK")
print("tokens=%d shared=%d new=%d master_chains=%d ext_chains=%d nouns=%d attrs=%d pairs=%d names296=%d inter=%d diff=%d" % (
    len(kw_tokens), len(shared), len(new_tokens), len(chains_master), len(chains_ext),
    len(noun_counter), len(attr_counter), len(pair_set), len(names_296), len(inter), len(diff)))
