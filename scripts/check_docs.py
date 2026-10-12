# -*- coding: utf-8 -*-
"""知识库自洽性检查 v2:全量文件索引 + basename 匹配,识别真死链 vs 通配/占位符。"""
import os, re, io, fnmatch, collections

ROOT = r'E:\aveva开发文档'
INSTALL = r'E:\AVEVA\Marine\OH12.1.SP4'

# 1) 建立全量文件索引(basename → 真实路径集合)
index = {}
for base_root in (ROOT, INSTALL):
    for dp, dn, fn in os.walk(base_root):
        for f in fn:
            index.setdefault(f.lower(), set()).add(os.path.join(dp, f))

# 2) 扫描 md 引用
re_token = re.compile(r'`([^`\n]{3,200})`')
re_mdlink = re.compile(r'\[[^\]]+\]\(([^)]+)\)')
re_ext = re.compile(r'\.(pmlfnc|pmlfrm|pmlobj|pmlmac|mac|py|tsv|cmd|bat|dll|chm|xml|dat|txt|md)$', re.I)

md_files = [os.path.join(dp, f) for dp, dn, fn in os.walk(ROOT) for f in fn if f.lower().endswith('.md')]
missing, ok_count, wild_count = [], 0, 0
for md in md_files:
    rel_md = os.path.relpath(md, ROOT)
    text = io.open(md, encoding='utf-8', errors='replace').read()
    cands = set()
    for m in re_token.finditer(text):
        tok = m.group(1).strip()
        if re_ext.search(tok):
            cands.add(tok)
    for m in re_mdlink.finditer(text):
        link = m.group(1).strip()
        if link and not link.lower().startswith(('http', 'mailto')) and re_ext.search(link):
            cands.add(link)
    for cand in sorted(cands):
        cand = cand.rstrip('.。').replace('→', '/')
        base = os.path.basename(cand.replace('\\', '/'))
        # 通配符 → glob 验证
        if any(ch in base for ch in '*?'):
            if any(fnmatch.fnmatch(f, base.lower()) for f in index):
                ok_count += 1
            else:
                missing.append((rel_md, cand, 'WILDCARD-NOMATCH'))
            continue
        # 占位符/命令行/纯扩展名 → 跳过
        if '<' in base or base.startswith(('python ', 'findstr', 'pml ')) or base.startswith('.'):
            continue
        # 绝对路径直接查
        if re.match(r'^[A-Za-z]:', cand):
            if os.path.exists(cand.replace('/', '\\')):
                ok_count += 1
            else:
                missing.append((rel_md, cand, 'ABS-MISSING'))
            continue
        # basename 索引匹配
        if base.lower() in index:
            ok_count += 1
        else:
            missing.append((rel_md, cand, 'NOT-IN-INDEX'))

print('md=%d  refs=%d  ok=%d  problems=%d' % (len(md_files), ok_count + len(missing), ok_count, len(missing)))
by_kind = collections.Counter(k for _, _, k in missing)
print('by kind:', dict(by_kind))
for md, cand, kind in missing:
    print('  [%s] %s | %s' % (kind, md, cand))
