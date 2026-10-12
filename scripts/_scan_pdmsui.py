# -*- coding: utf-8 -*-
"""PDMSUI PML1 树全量索引:路径/大小/前缀类型/宏名/$m依赖/同义词。输出 pdmsui_index.tsv + 统计。"""
import os, io, re, collections

ROOT = r'E:\AVEVA\Marine\OH12.1.SP4\PDMSUI'
OUT = r'E:\aveva开发文档\PML语料'

re_macro = re.compile(r'^\s*Macro:\s*(\S+)', re.M)
re_generic = re.compile(r'Macro Generic Type:\s*(.*)', re.M)
re_syn = re.compile(r'^\s*(synonym|SYNONYM)\s*[: ]\s*(\S+)', re.M)
re_mcall = re.compile(r'\$m\s+"?%?(?:PDMSUI|pmllib|PDMSDFLTS)?[^"\n]*?/([A-Za-z0-9_\-$]+)"?', re.I)

rows = []
prefix_counter = collections.Counter()
top_counter = collections.Counter()
mcall_counter = collections.Counter()

for dirpath, dirnames, filenames in os.walk(ROOT):
    for fn in sorted(filenames):
        full = os.path.join(dirpath, fn)
        rel = os.path.relpath(full, ROOT)
        top = rel.split(os.sep)[0]
        try:
            size = os.path.getsize(full)
            text = io.open(full, encoding='utf-8', errors='replace').read(20000)
        except OSError:
            continue
        top_counter[top] += 1
        macro = ''
        m = re_macro.search(text)
        if m:
            macro = m.group(1)
        gtype = ''
        m2 = re_generic.search(text)
        if m2:
            gtype = m2.group(1).strip()[:40]
        # 前缀类型:无扩展名文件名首字母约定(仅 DRA/des 等 app 目录)
        base = os.path.splitext(fn)[0]
        prefix = ''
        if len(base) > 1 and base[0] in 'fimurvpx' and not fn.lower().endswith(('.png', '.bmp')):
            prefix = base[0]
            prefix_counter[(top, base[0])] += 1
        mdeps = set(mm.upper() for mm in re_mcall.findall(text))
        for md in mdeps:
            mcall_counter[md] += 1
        syn = ''
        m3 = re_syn.search(text)
        if m3:
            syn = m3.group(2)
        rows.append((rel, top, str(size), macro, gtype, prefix, syn, ';'.join(sorted(mdeps))[:200]))

with io.open(os.path.join(OUT, 'pdmsui_index.tsv'), 'w', encoding='utf-8') as f:
    f.write('path\ttopdir\tbytes\tmacro\tgeneric\tkind\tsynonym\tmdeps\n')
    for r in rows:
        f.write('\t'.join(r) + '\n')

print('files=%d' % len(rows))
print('top dirs:', dict(top_counter.most_common()))
print('prefix top:', [(k, v) for k, v in prefix_counter.most_common(15)])
print('most $m-called macros:', mcall_counter.most_common(15))
