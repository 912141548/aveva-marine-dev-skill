# -*- coding: utf-8 -*-
"""提取 chm_extract 下全部内嵌 PDF 文本到 pdf_text/。"""
import os, io, re
from pypdf import PdfReader

SRC = r'E:\aveva开发文档\PML语料\chm_extract'
OUT = r'E:\aveva开发文档\PML语料\pdf_text'
os.makedirs(OUT, exist_ok=True)

found = []
for root, dirs, files in os.walk(SRC):
    for fn in files:
        if fn.lower().endswith('.pdf'):
            found.append(os.path.join(root, fn))

for src in sorted(found):
    stem = re.sub(r'[^\w\-]+', '_', os.path.splitext(os.path.basename(src))[0])[:80]
    out_path = os.path.join(OUT, stem + '.txt')
    if os.path.exists(out_path):
        print('SKIP %s' % stem)
        continue
    try:
        reader = PdfReader(src)
        n = len(reader.pages)
        with io.open(out_path, 'w', encoding='utf-8') as w:
            w.write('SOURCE: %s\nPAGES: %d\n' % (os.path.basename(src), n))
            for i, page in enumerate(reader.pages):
                try:
                    t = page.extract_text() or ''
                except Exception as e:
                    t = '[page extract error: %s]' % e
                w.write('\n===== PAGE %d =====\n' % (i + 1))
                w.write(t)
        print('OK  %4d pages  %s' % (n, stem))
    except Exception as e:
        print('ERR %s : %s' % (stem, e))
