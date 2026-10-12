# -*- coding: utf-8 -*-
"""uic Macro → PML 函数/表单存在性检查(第 39 轮)。
用法:python uic_macro_check.py [根目录] [--pml <PML语料目录>] [--out tsv]
"""
import os, re, sys, io, collections

argv = sys.argv[1:]
root = argv[0] if argv and not argv[0].startswith('--') else r'E:\AVEVA\Marine\OH12.1.SP4'
pml_dir = r'E:\aveva开发文档\PML语料'
out = 'uic_macro_check.tsv'
i = 0
while i < len(argv):
    if argv[i] == '--pml':
        pml_dir = argv[i+1]; del argv[i:i+2]; continue
    if argv[i] == '--out':
        out = argv[i+1]; del argv[i:i+2]; continue
    i += 1

funcs, forms = set(), set()
fp = os.path.join(pml_dir, 'functions.tsv')
if os.path.isfile(fp):
    with io.open(fp, encoding='utf-8') as f:
        next(f)
        for line in f:
            parts = line.split('\t')
            if len(parts) > 1 and parts[1].strip():
                funcs.add(parts[1].strip().lower().lstrip('!'))
fp = os.path.join(pml_dir, 'forms.tsv')
if os.path.isfile(fp):
    with io.open(fp, encoding='utf-8') as f:
        next(f)
        for line in f:
            parts = line.split('\t')
            if len(parts) > 1 and parts[1].strip():
                forms.add(parts[1].strip().lower().lstrip('!'))

re_func = re.compile(r'!!([A-Za-z_]\w*)\s*\(')
re_showform = re.compile(r'show\s+!!([A-Za-z_]\w*)', re.I)

findings = []
stats = collections.Counter()
checked = set()

for dp, dn, fn in os.walk(root):
    for f in fn:
        if not f.lower().endswith('.uic'):
            continue
        full = os.path.join(dp, f)
        rel = os.path.relpath(full, root)
        text = io.open(full, encoding='utf-8', errors='replace').read()
        for mm in re.finditer(r'<Macro>([^<]+)</Macro>', text):
            macro = mm.group(1).strip()
            stats['macros'] += 1
            for name in re_showform.findall(macro):
                key = 'form:' + name.lower()
                if key in checked:
                    continue
                checked.add(key)
                if name.lower() not in forms:
                    findings.append((rel, 'show !!' + name, 'FORM NOT FOUND'))
                    stats['form-missing'] += 1
                else:
                    stats['form-ok'] += 1
            for name in re_func.findall(macro):
                key = 'func:' + name.lower()
                if key in checked:
                    continue
                checked.add(key)
                if name.lower() not in funcs:
                    findings.append((rel, '!!' + name + '()', 'FUNCTION NOT FOUND'))
                    stats['func-missing'] += 1
                else:
                    stats['func-ok'] += 1

with io.open(os.path.join(pml_dir, out), 'w', encoding='utf-8') as f:
    f.write('uic\treference\tproblem\n')
    for r, ref, prob in findings:
        f.write('%s\t%s\t%s\n' % (r, ref, prob))
print('macros=%d distinct-refs=%d' % (stats['macros'], len(checked)))
print('func-ok=%d form-ok=%d' % (stats['func-ok'], stats['form-ok']))
print('MISSING: func=%d form=%d' % (stats['func-missing'], stats['form-missing']))
for r, ref, prob in findings[:20]:
    print('  [%s] %s -> %s' % (prob, ref, r))
