# -*- coding: utf-8 -*-
"""提取项目文件夹全部 PDF 文本到 pdf_text/,并生成每本的章节目录索引。"""
import os, io, re
from pypdf import PdfReader

SRC = r'E:\aveva开发文档'
OUT = os.path.join(SRC, 'PML语料', 'pdf_text')
os.makedirs(OUT, exist_ok=True)

for fn in sorted(os.listdir(SRC)):
    if not fn.lower().endswith('.pdf'):
        continue
    src = os.path.join(SRC, fn)
    stem = re.sub(r'[^\w\-]+', '_', os.path.splitext(fn)[0])[:60]
    try:
        reader = PdfReader(src)
        n = len(reader.pages)
        out_path = os.path.join(OUT, stem + '.txt')
        with io.open(out_path, 'w', encoding='utf-8') as w:
            w.write('SOURCE: %s\nPAGES: %d\n' % (fn, n))
            for i, page in enumerate(reader.pages):
                try:
                    t = page.extract_text() or ''
                except Exception as e:
                    t = '[page extract error: %s]' % e
                w.write('\n===== PAGE %d =====\n' % (i + 1))
                w.write(t)
        # 目录粗提:形如 "1.2 xxx" 或全大写短行的行
        heads = []
        with io.open(out_path, 'r', encoding='utf-8') as r:
            for line in r:
                s = line.strip()
                if 3 < len(s) < 90 and (re.match(r'^\d+(\.\d+){0,3}\s+\S', s) or re.match(r'^[A-Z][A-Z /&\-]{6,}$', s)):
                    heads.append(s)
        idx = os.path.join(OUT, stem + '_toc.txt')
        with io.open(idx, 'w', encoding='utf-8') as w:
            w.write('\n'.join(heads[:600]))
        print('OK  %3d pages  %s' % (n, fn))
    except Exception as e:
        print('ERR %s : %s' % (fn, e))
