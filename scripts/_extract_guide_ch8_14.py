# -*- coding: utf-8 -*-
"""提取 Guide 第 8-14 章文本(第 2 轮:Using PML in AVEVA Products ~ Form Callbacks)"""
import os, io, re

PDFTXT = r'E:\aveva开发文档\PML语料\pdf_text'
src = os.path.join(PDFTXT, 'Software_Customisation_Guide.txt')
with io.open(src, 'r', encoding='utf-8') as f:
    text = f.read()

pages = re.split(r'===== PAGE (\d+) =====', text)
page_map = {}
for i in range(1, len(pages), 2):
    page_map[int(pages[i])] = pages[i + 1]

chapters = [
    '8 Using PML in AVEVA Products',
    '9 Copies and References (for Advanced Users)',
    '10 Errors and Error Handling',
    '11 Handling Files and Directories',
    '12 Developing PML Code',
    '13 Form Concepts: Getting Started',
    '14 Form and Gadget Callbacks',
]
found = {}
for p in sorted(page_map):
    body = page_map[p]
    for t in chapters:
        if t not in found and re.search(r'^%s\s*$' % re.escape(t), body, re.M):
            found[t] = p

starts = sorted([p for p in found.values()]) + [227]   # 227 = ch21 起点(上轮已知),兜底
print('chapter starts:', found)

with io.open(os.path.join(PDFTXT, 'Guide_ch8_14.txt'), 'w', encoding='utf-8') as f:
    for t in chapters:
        s = found.get(t)
        if s is None:
            f.write('\n\n########## %s NOT FOUND ##########\n' % t)
            continue
        ends = [x for x in starts if x > s]
        e = min(ends) if ends else max(page_map)
        f.write('\n\n########## %s (PDF p%d-%d) ##########\n' % (t, s, e - 1))
        for p in range(s, e):
            f.write('\n===== PAGE %d =====\n' % p)
            f.write(page_map.get(p, ''))
print('done')
