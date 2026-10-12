# -*- coding: utf-8 -*-
"""回调字符串→方法存在性批量校验(官方语料 FRM-01 回归)。
对每个 .pmlfrm 的回调字符串(callback/initcall/okcall/...):
  - '!this.NAME(' → 表单方法,查同文件 define method
  - '!!NAME('     → 全局函数,查 functions.tsv
  - 其他(纯命令/宏)→ 归类 command
输出:callback_validation.tsv + 控制台统计
"""
import json, io, re, collections, os

OUT = r'E:\aveva开发文档\PML语料'
with io.open(os.path.join(OUT, 'corpus.json'), encoding='utf-8') as f:
    corpus = json.load(f)
with io.open(os.path.join(OUT, 'functions.tsv'), encoding='utf-8') as f:
    next(f)
    all_funcs = set()
    for line in f:
        parts = line.split('\t')
        if parts and len(parts) > 1:
            all_funcs.add(parts[1].lower().lstrip('!'))

re_this = re.compile(r"!this\s*\.\s*([A-Za-z_]\w*)\s*\(", re.I)   # 必须紧跟 '(' 才是方法调用
re_chain = re.compile(r"!this\s*\.\s*[A-Za-z_]\w*(?:\s*\.\s*[A-Za-z_]\w*)+\s*\(", re.I)  # !this.成员.方法( 链
BUILTIN_FORM_METHODS = set('''hide show shown setactive setgadgetsactive setpopup removepopup
getpickedpopup newmenu setopacity subtype setundoable undoable refresh'''.split())
re_glob = re.compile(r"!!([A-Za-z_]\w*)\s*\(", re.I)
re_dollar = re.compile(r'\$[!<]')          # 含 $! 动态展开 → 无法静态判定
re_cmd = re.compile(r'^\s*[A-Z][A-Z0-9 ]+$')  # 全大写=产品命令

stats = collections.Counter()
unresolved = []
resolved_forms = collections.Counter()

for rec in corpus:
    if rec['ext'] != '.pmlfrm':
        continue
    methods = set(m.lower().lstrip('.') for m in rec.get('methods', []))
    form_names = set(x.lower().lstrip('!') for x in rec.get('forms', []))
    for cbname, cbstr in rec.get('callbacks', []):
        s = (cbstr or '').strip()
        if not s:
            continue
        stats['total'] += 1
        if re_dollar.search(s):
            stats['dynamic($!)'] += 1
            continue
        open_style = s.rstrip().endswith('(')   # open callback '!this.M('
        hits_this = re_this.findall(s)
        hits_glob = re_glob.findall(s)
        if re_chain.search(s) and not hits_this:
            stats['member-chain(不校验)'] += 1
            continue
        ok = True
        checked = False
        for name in hits_this:
            checked = True
            key = name.lower()
            if key in methods or key in form_names:
                stats['this→method ok'] += 1
                resolved_forms['.' + key] += 1
            elif key in BUILTIN_FORM_METHODS:
                stats['this→builtin ok'] += 1
            else:
                ok = False
                if open_style:
                    # open 回调只写左括号,方法名照样可查
                    stats['this→MISSING'] += 1
                    unresolved.append((rec['path'], cbname, s[:80], 'this.' + key))
                else:
                    stats['this→MISSING'] += 1
                    unresolved.append((rec['path'], cbname, s[:80], 'this.' + key))
        for name in hits_glob:
            checked = True
            if name.lower() in all_funcs:
                stats['!!→function ok'] += 1
            else:
                ok = False
                stats['!!→MISSING'] += 1
                unresolved.append((rec['path'], cbname, s[:80], '!!' + name))
        if not checked:
            if re_cmd.match(s) or not re.search(r'[!(]', s):
                stats['command-like'] += 1
            else:
                stats['other(macro/var)'] += 1

with io.open(os.path.join(OUT, 'callback_validation.tsv'), 'w', encoding='utf-8') as f:
    f.write('file\tcallback\tstring\tmissing\n')
    for row in unresolved:
        f.write('\t'.join(row) + '\n')

print('stats:', dict(stats))
print('unresolved files:', len(set(r[0] for r in unresolved)))
print('top missing this-methods:', resolved_forms.most_common(0))
for row in unresolved[:15]:
    print('  ', row[0], '|', row[1], '|', row[2], '|', row[3])
