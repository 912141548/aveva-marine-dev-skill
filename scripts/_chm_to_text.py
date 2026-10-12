# -*- coding: utf-8 -*-
"""把 chm_extract 下全部 HTML 转成纯文本(合并成每本 CHM 一个大 txt),便于 grep 挖掘。"""
import os, io, re
from html.parser import HTMLParser

SRC = r'E:\aveva开发文档\PML语料\chm_extract'
OUT = r'E:\aveva开发文档\PML语料\chm_text'
os.makedirs(OUT, exist_ok=True)

class TextExtract(HTMLParser):
    def __init__(self):
        super().__init__()
        self.parts = []
        self.skip = 0
        self.title = ''
        self._in_title = False
    def handle_starttag(self, tag, attrs):
        if tag in ('script', 'style'):
            self.skip += 1
        if tag == 'title':
            self._in_title = True
        if tag in ('p', 'div', 'br', 'tr', 'li', 'h1', 'h2', 'h3', 'h4', 'h5', 'h6', 'table', 'ul', 'ol', 'pre'):
            self.parts.append('\n')
        if tag in ('td', 'th'):
            self.parts.append('\t')
    def handle_endtag(self, tag):
        if tag in ('script', 'style') and self.skip:
            self.skip -= 1
        if tag == 'title':
            self._in_title = False
    def handle_data(self, data):
        if self.skip:
            return
        if self._in_title:
            self.title += data
        self.parts.append(data)

for book in sorted(os.listdir(SRC)):
    bdir = os.path.join(SRC, book)
    if not os.path.isdir(bdir):
        continue
    # 读取 HHC 得到目录顺序与书名
    order = []
    bookname = book
    hhc = None
    for f in os.listdir(bdir):
        if f.lower().endswith('.hhc'):
            hhc = os.path.join(bdir, f)
            break
    if hhc:
        raw = io.open(hhc, 'r', encoding='utf-8', errors='ignore').read()
        m = re.search(r'<param name="Name" value="([^"]{3,120})"', raw)
        if m:
            bookname = m.group(1)
        for m in re.finditer(r'<param name="Local" value="([^"]+)"', raw):
            order.append(m.group(1).split('#')[0])
    # 收集全部 html 文件
    pages = {}
    for root, dirs, files in os.walk(bdir):
        for fn in files:
            if fn.lower().endswith(('.html', '.htm')):
                pages[fn] = os.path.join(root, fn)
    ordered = [p for p in order if p in pages]
    rest = [p for p in sorted(pages) if p not in set(ordered)]
    allfiles = ordered + rest
    out_path = os.path.join(OUT, book + '.txt')
    with io.open(out_path, 'w', encoding='utf-8') as w:
        w.write('SOURCE: %s.chm\nBOOKNAME: %s\nPAGES(files): %d\n\n' % (book, bookname, len(allfiles)))
        for p in allfiles:
            fn = os.path.basename(p)
            try:
                raw = io.open(p, 'r', encoding='utf-8', errors='ignore').read()
            except Exception as e:
                raw = ''
            te = TextExtract()
            try:
                te.feed(raw)
            except Exception:
                pass
            txt = ''.join(te.parts)
            txt = re.sub(r'[ \t]+', ' ', txt)
            txt = re.sub(r'\n\s*\n+', '\n', txt).strip()
            if txt:
                w.write('\n===== FILE %s =====\n' % fn)
                w.write(txt)
    print('OK  %5d files  %-12s  %s' % (len(allfiles), book, bookname[:70]))
