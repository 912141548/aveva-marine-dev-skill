# -*- coding: utf-8 -*-
"""官方源码 handle 错误码 → 语义提取:handle (m,c) 块内的第一条 alert/error 文本与码配对。"""
import os, io, re, collections

ROOT = r'E:\AVEVA\Marine\OH12.1.SP4\PMLLIB'
OUT = r'E:\aveva开发文档\PML语料'
re_handle = re.compile(r'^\s*handle\s*\(?\s*(\d+)\s*,\s*(\d+)\s*\)?', re.I)
re_alert = re.compile(r"!!alert\s*\.\s*(?:error|warning|message|confirm|question)\s*\(\s*['\"]?([^'\"$]*)", re.I)
re_ret = re.compile(r"return error\s+\d+\s*['\"]([^'\"]+)['\"]", re.I)
re_comment = re.compile(r'^\s*(--|\$)')
code_msgs = collections.defaultdict(collections.Counter)
code_examples = collections.defaultdict(list)
code_counts = collections.Counter()

for dirpath, dirnames, filenames in os.walk(ROOT):
    for fn in filenames:
        if os.path.splitext(fn)[1].lower() not in ('.pmlfnc', '.pmlfrm', '.pmlobj'):
            continue
        rel = os.path.relpath(os.path.join(dirpath, fn), ROOT)
        try:
            lines = io.open(os.path.join(dirpath, fn), encoding='utf-8', errors='replace').readlines()
        except OSError:
            continue
        i = 0
        while i < len(lines):
            m = re_handle.match(lines[i])
            if m:
                code = '(%s,%s)' % (m.group(1), m.group(2))
                code_counts[code] += 1
                # 块内前 8 行找 alert/return error 文本
                for j in range(i + 1, min(i + 9, len(lines))):
                    line = lines[j].strip()
                    if re.match(r'^\s*endhandle', lines[j], re.I):
                        break
                    if re_comment.match(line):
                        continue
                    am = re_alert.search(line)
                    if am:
                        txt = am.group(1).strip()
                        if txt:
                            code_msgs[code][txt[:90]] += 1
                            if len(code_examples[code]) < 3:
                                code_examples[code].append((rel, j + 1, txt[:90]))
                        break
                    rm = re_ret.search(line)
                    if rm:
                        txt = rm.group(1).strip()
                        if txt:
                            code_msgs[code][txt[:90]] += 1
                            if len(code_examples[code]) < 3:
                                code_examples[code].append((rel, j + 1, txt[:90]))
                        break
            i += 1

with io.open(os.path.join(OUT, 'errorcode_semantics.tsv'), 'w', encoding='utf-8') as f:
    f.write('code\tblocks\tdistinct_msgs\ttop_messages\texample\n')
    for code in sorted(code_counts, key=lambda c: -code_counts[c]):
        msgs = code_msgs.get(code)
        if not msgs:
            f.write('%s\t%d\t0\t\t\n' % (code, code_counts[code]))
            continue
        top = ' || '.join('%s(x%d)' % (m, c) for m, c in msgs.most_common(4))
        ex = code_examples[code][0] if code_examples[code] else ('', 0, '')
        f.write('%s\t%d\t%d\t%s\t%s:%s %s\n' % (code, code_counts[code], len(msgs), top.replace('\t', ' '), ex[0], ex[1], ex[2].replace('\t', ' ')))

print('codes with blocks:', len(code_counts))
for code in sorted(code_counts, key=lambda c: -code_counts[c])[:20]:
    msgs = code_msgs.get(code)
    top = msgs.most_common(2) if msgs else []
    print('%-10s x%-5d %s' % (code, code_counts[code], ' | '.join('%s(x%d)' % (m, c) for m, c in top)))
