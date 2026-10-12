# -*- coding: utf-8 -*-
"""Marine PMLLIB 全量语料扫描:逐文件学习,产出索引/目录/习语/审核正则回归。
输出到 E:\\aveva开发文档\\PML语料\\
"""
import os, re, io, json, collections

ROOT = r'E:\AVEVA\Marine\OH12.1.SP4\PMLLIB'
OUT  = r'E:\aveva开发文档\PML语料'
EXTS = ('.pmlfnc', '.pmlfrm', '.pmlobj', '.pmlmac', '.mac')

# ---------- regex 库 ----------
re_hdr_file = re.compile(r'^--\s*File:\s*(\S+)', re.I)
re_hdr_type = re.compile(r'^--\s*Type:\s*(.+?)\s*$', re.I)
re_hdr_mod  = re.compile(r'^--\s*Module:\s*(.+?)\s*$', re.I)
re_hdr_auth = re.compile(r'^--\s*Author:\s*(.+?)\s*$', re.I)
re_hdr_desc = re.compile(r'^--\s*Description:\s*(.+?)\s*$', re.I)

re_def_fn   = re.compile(r'^\s*define\s+function\s+(!!\w+)\s*\(([^)]*)\)\s*(?:is\s+([A-Za-z_]\w*))?', re.I)
re_def_obj  = re.compile(r'^\s*define\s+object\s+([A-Za-z_]\w*)', re.I)
re_def_frm  = re.compile(r'^\s*(setup|layout)\s+form\s+(!!\w+)\s*(.*)$', re.I)
re_def_mth  = re.compile(r'^\s*define\s+method\s+\.([A-Za-z_]\w*)\s*\(([^)]*)\)\s*(?:is\s+([A-Za-z_]\w*))?', re.I)
re_member   = re.compile(r'^\s*member\s+\.([A-Za-z_]\w*)\s+is\s+([A-Za-z_]\w*)', re.I)
re_import   = re.compile(r"^\s*import\s+'([^']+)'", re.I)
re_ns       = re.compile(r"^\s*using\s+namespace\s+'([^']+)'", re.I)
re_handle   = re.compile(r'^\s*handle\s+(ANY|\(\s*[\d]+\s*,\s*[\d]+\s*\))', re.I)
re_elseh    = re.compile(r'^\s*elsehandle\s+(ANY|NONE|\(\s*[\d]+\s*,\s*[\d]+\s*\))', re.I)
re_onerror  = re.compile(r'^\s*onerror\s+(\w+)', re.I)
re_cb       = re.compile(r"\.(callback|initcall|okcall|cancelcall|quitcall|validatecall|opencall)\s*=\s*['|\"]([^'|\"]*)", re.I)
re_gadget   = re.compile(r'^\s*(frame|button|toggle|rtoggle|text|option|paragraph|list|combo(?:box)?|selector|textpane|picture|slider|numericinput|container|table|tabset|view|alpha|linklabel|toolbar)\s+\.([A-Za-z_]\w*)', re.I)
re_alert    = re.compile(r'!!alert\s*\.\s*(\w+)', re.I)
re_netobj   = re.compile(r'object\s+((?:NET|PMLNET)\w+)', re.I)
re_comment  = re.compile(r'^\s*(--|\$\*|\$\()')
re_block_cmt= re.compile(r'^\s*\$\(')

# 审核规范 A 类回归(预处理:剔除注释行与分隔线)
re_a_eq     = re.compile(r'==|!=|>=|<=')
re_a_ifthen = re.compile(r'^\s*if\b(?:(?!then).)*$', re.I)
re_a_barelt = re.compile(r"^\s*if\s+\(\s*[^'|\[\]()]*?(?<![$!<])(?<!=)(?<!=)<(?!>)")   # if (...) 内裸 <(粗筛)
re_a_ce     = re.compile(r'(?<![!])!CE\b')
re_a_gosub  = re.compile(r'\bgosub\b', re.I)
re_a_endloop= re.compile(r'\bendloop\b', re.I)

files_meta   = []           # 每文件一行记录
fn_catalog   = []           # 函数目录
obj_catalog  = []           # 对象目录(含方法)
frm_catalog  = []           # 表单目录(含 gadget)
method_names = collections.Counter()
gadget_types = collections.Counter()
import_libs  = collections.Counter()
ns_used      = collections.Counter()
handle_codes = collections.Counter()
alert_kinds  = collections.Counter()
net_objs     = collections.Counter()
cb_dest      = collections.Counter()
member_types = collections.Counter()
ret_types    = collections.Counter()
idiom_examples = collections.defaultdict(list)   # idiom -> [(file,line,text)]

def add_ex(k, f, ln, txt, cap=6):
    if len(idiom_examples[k]) < cap:
        idiom_examples[k].append((f, ln, txt.strip()[:150]))

audit = collections.Counter()   # 审核正则命中
audit_files = collections.defaultdict(set)

total_lines = 0
n_files = 0

for dirpath, dirnames, filenames in os.walk(ROOT):
    for fn in sorted(filenames):
        base, ext = os.path.splitext(fn)
        if ext.lower() not in EXTS:
            continue
        full = os.path.join(dirpath, fn)
        rel  = os.path.relpath(full, ROOT)
        module = rel.split(os.sep)[0]
        try:
            with io.open(full, 'r', encoding='utf-8', errors='replace') as fh:
                lines = fh.readlines()
        except OSError:
            continue
        n_files += 1
        total_lines += len(lines)

        hdr = {}
        defines_fn, defines_obj, defines_frm = [], [], []
        methods, members = [], []
        imports, namespaces = [], []
        handles, elsehs = [], []
        callbacks, gadgets = [], []
        block_comment = False
        for i, raw in enumerate(lines, 1):
            line = raw.rstrip('\n')
            if re_block_cmt.match(line):
                block_comment = True
            if block_comment:
                if re.match(r'^.*\$\)', line):
                    block_comment = False
                if i < 40 or True:
                    pass
            in_comment = bool(re_comment.match(line)) or block_comment
            if i <= 30 and not in_comment:
                pass
            # 头部字段(注释区内)
            if i <= 35:
                m = re_hdr_file.match(line)
                if m: hdr.setdefault('File', m.group(1))
                m = re_hdr_type.match(line)
                if m: hdr.setdefault('Type', m.group(1))
                m = re_hdr_mod.match(line)
                if m: hdr.setdefault('Module', m.group(1))
                m = re_hdr_auth.match(line)
                if m: hdr.setdefault('Author', m.group(1))
                m = re_hdr_desc.match(line)
                if m: hdr.setdefault('Description', m.group(1))
            if in_comment:
                continue
            m = re_def_fn.match(line)
            if m:
                defines_fn.append(m.groups())
                fn_catalog.append((rel, m.group(1), m.group(2).strip(), m.group(3) or ''))
                if m.group(3): ret_types[m.group(3)] += 1
                add_ex('define function', rel, i, line); continue
            m = re_def_obj.match(line)
            if m:
                defines_obj.append(m.group(1)); continue
            m = re_def_frm.match(line)
            if m:
                defines_frm.append((m.group(2), m.group(3).strip()))
                add_ex('setup form ' + (m.group(2).strip().split()[0] if m.group(2).strip() else '(plain)'), rel, i, line)
                continue
            m = re_def_mth.match(line)
            if m:
                methods.append(m.groups())
                method_names['.' + m.group(1)] += 1
                obj_catalog.append((rel, m.group(1), m.group(2).strip(), m.group(3) or ''))
                if m.group(3): ret_types[m.group(3)] += 1
                continue
            m = re_member.match(line)
            if m:
                members.append(m.groups())
                member_types[m.group(2)] += 1
                continue
            m = re_import.match(line)
            if m:
                imports.append(m.group(1)); import_libs[m.group(1).lower()] += 1
                add_ex("import '" + m.group(1) + "'", rel, i, line); continue
            m = re_ns.match(line)
            if m:
                namespaces.append(m.group(1)); ns_used[m.group(1)] += 1; continue
            m = re_handle.match(line)
            if m:
                handles.append(m.group(1)); handle_codes[m.group(1)] += 1
                add_ex('handle ' + m.group(1), rel, i, line); continue
            m = re_elseh.match(line)
            if m:
                elsehs.append(m.group(1)); handle_codes['else' + m.group(1)] += 1; continue
            m = re_onerror.match(line)
            if m:
                handle_codes['onerror ' + m.group(1)] += 1
                add_ex('onerror ' + m.group(1), rel, i, line); continue
            m = re_cb.search(line)
            if m:
                callbacks.append((m.group(1), m.group(2)))
                cb_dest[m.group(1)] += 1
                add_ex('callback:' + m.group(1), rel, i, line); continue
            m = re_gadget.match(line)
            if m:
                gadgets.append((m.group(1), m.group(2)))
                gadget_types[m.group(1)] += 1
                if len(idiom_examples['gadget:' + m.group(1)]) < 3:
                    idiom_examples['gadget:' + m.group(1)].append((rel, i, line.strip()[:150]))
                continue
            m = re_alert.search(line)
            if m:
                alert_kinds[m.group(1).lower()] += 1; continue
            m = re_netobj.search(line)
            if m:
                net_objs[m.group(1)] += 1; continue

            # ---- 审核规范 A 类回归(非注释行) ----
            if re_a_eq.search(line):
                audit['OPR-01 ==/!=/>=/<='] += 1; audit_files['OPR-01'].add(rel)
            if re_a_ifthen.match(line):
                audit['CTL-03a if 缺 then'] += 1; audit_files['CTL-03a'].add(rel)
            if re_a_barelt.match(line):
                audit['OPR-02 if 裸 <'] += 1; audit_files['OPR-02'].add(rel)
            if re_a_ce.search(line):
                audit['VAR-02 !CE'] += 1; audit_files['VAR-02'].add(rel)
            if re_a_gosub.search(line):
                audit['CTL-04 gosub'] += 1; audit_files['CTL-04'].add(rel)
            if re_a_endloop.search(line):
                audit['CTL-01 endloop'] += 1; audit_files['CTL-01'].add(rel)

        rec = {
            'path': rel, 'module': module, 'ext': ext.lower(), 'lines': len(lines),
            'hdr': hdr, 'functions': [f[0] for f in defines_fn],
            'objects': defines_obj, 'forms': [f[0] for f in defines_frm],
            'methods': ['.' + m[0] for m in methods],
            'members': ['.' + m[0] + ':' + m[1] for m in members],
            'imports': imports, 'namespaces': namespaces,
            'handles': handles + ['else' + e for e in elsehs],
            'callbacks': callbacks[:20], 'gadgets': [g[0] + '.' + g[1] for g in gadgets[:40]],
        }
        files_meta.append(rec)

        if ext.lower() == '.pmlfrm':
            frm_catalog.append((rel, defines_frm[0][0] if defines_frm else '?',
                                [g[0] for g in gadgets]))

# ---------- 输出 ----------
def w(name, text):
    with io.open(os.path.join(OUT, name), 'w', encoding='utf-8') as f:
        f.write(text)

# 1) corpus_index.tsv
buf = ['path\tmodule\ttype\tlines\tn_methods\tn_members\timports\tnamespaces\thandles']
for r in files_meta:
    kind = r['hdr'].get('Type', r['ext'])
    buf.append('%s\t%s\t%s\t%d\t%d\t%d\t%s\t%s\t%s' % (
        r['path'], r['module'], kind, r['lines'], len(r['methods']), len(r['members']),
        ';'.join(sorted(set(r['imports']))), ';'.join(sorted(set(r['namespaces']))),
        ';'.join(sorted(set(r['handles'])))))
w('corpus_index.tsv', '\n'.join(buf))

# 2) 目录三本
w('functions.tsv', 'file\tname\targs\treturns\n' + '\n'.join('\t'.join(x) for x in fn_catalog))
w('object_methods.tsv', 'file\tmethod\targs\treturns\n' + '\n'.join('\t'.join(x) for x in obj_catalog))
w('forms.tsv', 'file\tform\tgadgets\n' + '\n'.join('%s\t%s\t%s' % (f, n, ','.join(g)) for f, n, g in frm_catalog))

# 3) 频次与习语
def table(counter, title):
    out = ['## %s\n' % title, '| # | 项 | 次数 |', '|---|---|---|']
    for i, (k, v) in enumerate(counter.most_common(40), 1):
        out.append('| %d | %s | %d |' % (i, k.replace('|', '\\|'), v))
    return '\n'.join(out) + '\n'

parts = ['# Marine PMLLIB 语料自动统计(脚本生成)\n']
parts.append('- 文件数:%d,总行数:%d\n' % (n_files, total_lines))
parts.append(table(gadget_types, 'gadget 类型频次'))
parts.append(table(import_libs, 'import 程序集频次'))
parts.append(table(ns_used, 'using namespace 频次'))
parts.append(table(handle_codes, 'handle/onerror 形态频次'))
parts.append(table(alert_kinds, '!!alert 方法频次'))
parts.append(table(net_objs, 'NET 对象实例化频次'))
parts.append(table(cb_dest, '回调种类频次'))
parts.append(table(ret_types, '函数/方法返回类型频次'))
parts.append(table(member_types, '成员类型频次'))
parts.append(table(method_names, '方法名频次(Top40,查官方惯用方法名)'))

parts.append('\n## 习语实例(带出处)\n')
for k in sorted(idiom_examples):
    parts.append('\n### %s\n' % k.replace('|', '\\|'))
    for f, ln, t in idiom_examples[k]:
        parts.append('- `%s:%d` — `%s`' % (f, ln, t.replace('|', '\\|').replace('`', "'")))

parts.append('\n## 审核规范 A 类正则回归(官方语料,非注释行)\n')
parts.append('| 规则 | 命中行数 | 命中文件数 |')
parts.append('|---|---|---|')
for k in sorted(audit):
    parts.append('| %s | %d | %d |' % (k, audit[k], len(audit_files[k.replace(' ', '-').split()[0]])))
w('stats_and_idioms_auto.md', '\n'.join(parts))

# 4) 审核命中文件明细(供抽样核查)
buf = []
for k in sorted(audit_files):
    for f in sorted(audit_files[k])[:80]:
        buf.append('%s\t%s' % (k, f))
w('audit_hits.tsv', '\n'.join(buf))

# 5) JSON 全量(供后续程序使用)
with io.open(os.path.join(OUT, 'corpus.json'), 'w', encoding='utf-8') as f:
    json.dump(files_meta, f, ensure_ascii=False)

print('files=%d lines=%d' % (n_files, total_lines))
print('functions=%d forms=%d objects=%d methods=%d' % (
    len(fn_catalog), len(frm_catalog), sum(1 for r in files_meta if r['objects']),
    len(obj_catalog)))
print('audit:', dict(audit))
