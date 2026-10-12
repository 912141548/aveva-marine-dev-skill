# -*- coding: utf-8 -*-
"""提取 Guide ch2-7(p9-70)到 pdf_text\Guide_ch2_7.txt"""
import io, re, os

PDFTXT = r'E:\aveva开发文档\PML语料\pdf_text'
src = os.path.join(PDFTXT, 'Software_Customisation_Guide.txt')
text = io.open(src, encoding='utf-8').read()
pages = re.split(r'===== PAGE (\d+) =====', text)
pm = {int(pages[i]): pages[i + 1] for i in range(1, len(pages), 2)}

with io.open(os.path.join(PDFTXT, 'Guide_ch2_7.txt'), 'w', encoding='utf-8') as f:
    f.write('########## Guide ch2-7 (PDF p9-70) ##########\n')
    for p in range(9, 71):
        f.write('\n===== PAGE %d =====\n' % p)
        f.write(pm.get(p, ''))
print('written', sum(len(v) for k, v in pm.items() if 9 <= k <= 70))
