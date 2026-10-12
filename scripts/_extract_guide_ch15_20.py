# -*- coding: utf-8 -*-
"""提取 Guide 第 15-20 章(第 3 轮:Forms/Menus/Form Layout/Frames/Gadgets/Gadget Set)"""
import io, re, os

PDFTXT = r'E:\aveva开发文档\PML语料\pdf_text'
src = os.path.join(PDFTXT, 'Software_Customisation_Guide.txt')
text = io.open(src, encoding='utf-8').read()
pages = re.split(r'===== PAGE (\d+) =====', text)
pm = {int(pages[i]): pages[i + 1] for i in range(1, len(pages), 2)}

titles = ['14 Form and Gadget Callbacks', '15 Forms', '16 Menus', '17 Form Layout',
          '18 Frames', '19 Gadgets and their Attributes', '20 Gadget Set', '21 Alert Objects']
found = {}
for p in sorted(pm):
    for t in titles:
        if t not in found and re.search(r'^%s\s*$' % re.escape(t), pm[p], re.M):
            found[t] = p
print('starts:', found)

keys = [t for t in titles if t in found]
with io.open(os.path.join(PDFTXT, 'Guide_ch15_20.txt'), 'w', encoding='utf-8') as f:
    for i, t in enumerate(keys):
        s = found[t]
        e = found[keys[i + 1]] if i + 1 < len(keys) else 267
        f.write('\n\n########## %s (PDF p%d-%d) ##########\n' % (t, s, e - 1))
        for p in range(s, e):
            f.write('\n===== PAGE %d =====\n' % p)
            f.write(pm.get(p, ''))
print('written')
