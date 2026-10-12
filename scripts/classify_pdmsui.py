# -*- coding: utf-8 -*-
"""为 pdmsui_index.tsv 补充 Macro Generic Type 分类列(第 72 轮)。
输出 pdmsui_index_v2.tsv(在原列基础上追加 gtype2 列)。
"""
import os, io, re, collections

ROOT = r'E:\AVEVA\Marine\OH12.1.SP4\PDMSUI'
IN = os.path.join(r'E:\aveva开发文档\PML语料', 'pdmsui_index.tsv')
OUT = os.path.join(r'E:\aveva开发文档\PML语料', 'pdmsui_index_v2.tsv')

re_gt = re.compile(r'Macro Generic Type:\s*(.*)', re.I)

# 读原索引
lines = io.open(IN, encoding='utf-8').readlines()
header = lines[0].strip().split('\t')
rows = []
for line in lines[1:]:
    parts = line.rstrip('\n').split('\t')
    rows.append(parts)

# 重新扫描获取 Generic Type
gt_cache = {}
for dp, dn, fn in os.walk(ROOT):
    for f in fn:
        full = os.path.join(dp, f)
        rel = os.path.relpath(full, ROOT)
        try:
            head = io.open(full, encoding='utf-8', errors='replace').read(3000)
        except OSError:
            continue
        m = re_gt.search(head)
        if m:
            gt_cache[rel.lower()] = m.group(1).strip()[:40]

# 输出
with io.open(OUT, 'w', encoding='utf-8') as f:
    f.write('\t'.join(header[:6]) + '\tgtype2\t' + '\t'.join(header[7:]) + '\n')
    for parts in rows:
        path = parts[0].lower()
        gt = gt_cache.get(path, '')
        # 保持原列结构,在 synonyym 之后插入 gtype2
        new_parts = parts[:7] + [gt] + parts[7:]
        f.write('\t'.join(new_parts) + '\n')

# 统计
stats = collections.Counter()
for parts in rows:
    path = parts[0].lower()
    gt = gt_cache.get(path, '')
    if gt:
        stats[gt[:30]] += 1
    else:
        stats['(no Generic Type)'] += 1

print('rows=%d, with gtype=%d' % (len(rows), sum(v for k,v in stats.items() if k != '(no Generic Type)')))
for k, v in stats.most_common(15):
    print('  %-35s %5d' % (k, v))
