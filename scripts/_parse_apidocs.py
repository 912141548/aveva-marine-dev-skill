# -*- coding: utf-8 -*-
"""解析 ApplicationFramework 两个 XML 文档 → .NET API 参考 md;并提取 Guide 21-23 章文本。"""
import os, io, re, xml.etree.ElementTree as ET

ROOT = r'E:\AVEVA\Marine\OH12.1.SP4'
OUT  = r'E:\aveva开发文档\PML语料'
PDFTXT = r'E:\aveva开发文档\PML语料\pdf_text'

# ---------- 1) 解析 XML doc ----------
def parse_doc(path, title, out_lines):
    tree = ET.parse(path)
    members = tree.getroot().find('members')
    types = {}
    for m in members.findall('member'):
        name = m.get('name', '')
        kind = name[0]
        rest = name[2:]
        summ = m.find('summary')
        stext = ''.join(summ.itertext()).strip() if summ is not None else ''
        stext = re.sub(r'\s+', ' ', stext)
        if kind == 'T':
            types.setdefault(rest, {'summary': stext, 'members': []})
        else:
            # M:/P:/F:/E: -> 归属类型
            if '(' in rest:
                tpart, meth = rest.split('(', 1)
                meth = meth.join(['(', ')']) if meth else ''
                # method: "Ns.Type.Method(params)" -> split last dot before (
                idx = tpart.rfind('.')
                owner, mname = tpart[:idx], tpart[idx+1:]
                sig = '(' + rest.split('(', 1)[1]
            else:
                idx = rest.rfind('.')
                owner, mname = rest[:idx], rest[idx+1:]
                sig = ''
            types.setdefault(owner, {'summary': '', 'members': []})
            tag = {'M': 'M', 'P': 'P', 'F': 'F', 'E': 'E'}.get(kind, kind)
            param = m.find('param')
            ptxt = ''
            types[owner]['members'].append((tag, mname + (sig[:80] if sig else ''), stext))
    out_lines.append('\n# %s\n' % title)
    out_lines.append('类型数:%d\n' % len(types))
    for t in sorted(types):
        info = types[t]
        out_lines.append('\n## %s\n' % t)
        if info['summary']:
            out_lines.append(info['summary'] + '\n')
        if info['members']:
            out_lines.append('| 类 | 成员 | 说明 |')
            out_lines.append('|---|---|---|')
            for tag, mn, sm in info['members']:
                sm = sm.replace('|', '\\|')
                out_lines.append('| %s | %s | %s |' % (tag, mn.replace('|', '\\|'), sm[:220]))

out = []
parse_doc(os.path.join(ROOT, 'ApplicationFramework.xml'), 'Aveva.ApplicationFramework API 参考(官方 XML 文档)', out)
with io.open(os.path.join(OUT, 'net_api_applicationframework.md'), 'w', encoding='utf-8') as f:
    f.write('\n'.join(out))

out = []
parse_doc(os.path.join(ROOT, 'ApplicationFramework.Presentation.xml'), 'Aveva.ApplicationFramework.Presentation API 参考(官方 XML 文档)', out)
with io.open(os.path.join(OUT, 'net_api_presentation.md'), 'w', encoding='utf-8') as f:
    f.write('\n'.join(out))

print('xml done')

# ---------- 2) 提取 Guide 第 21/22/23 章 ----------
src = os.path.join(PDFTXT, 'Software_Customisation_Guide.txt')
with io.open(src, 'r', encoding='utf-8') as f:
    text = f.read()
pages = re.split(r'===== PAGE (\d+) =====', text)
# pages: [pre, num, content, num, content...]
page_map = {}
for i in range(1, len(pages), 2):
    page_map[int(pages[i])] = pages[i+1]

targets = {'21 Alert Objects': None, '22 FMSYS Object and its Methods': None, '23 PML Add-ins': None}
endmarks = ['Appendix', 'Index']
for p in sorted(page_map):
    body = page_map[p]
    for t in targets:
        if targets[t] is None and re.search(r'^%s\s*$' % re.escape(t), body, re.M):
            targets[t] = p

bounds = sorted([p for p in targets.values() if p])
print('chapter starts:', targets)
ranges = {}
keys = list(targets.keys())
for i, k in enumerate(keys):
    start = targets[k]
    if start is None:
        continue
    ends = [x for x in bounds if x > start] + [max(page_map) - 2]
    ranges[k] = (start, min(ends))

with io.open(os.path.join(PDFTXT, 'Guide_ch21_22_23.txt'), 'w', encoding='utf-8') as f:
    for k, (s, e) in sorted(ranges.items(), key=lambda kv: kv[1][0]):
        f.write('\n\n########## %s (PDF p%d-%d) ##########\n' % (k, s, e))
        for p in range(s, e + 1):
            f.write('\n===== PAGE %d =====\n' % p)
            f.write(page_map.get(p, ''))
print('guide chapters extracted')
