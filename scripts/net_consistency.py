# -*- coding: utf-8 -*-
"""net_consistency.py —— .NET addin 一致性审计(第 36 轮)。

检查三项(对应《AVEVA-Marine-uic定制与部署调试手册》§3.4 排错树):
  1) uic 中的 Instance CommandId/Key 是否都能在 .cs 源里找到同名字符串(Key = "...");
  2) Macro 型命令标记为 informational;
  3) Addins.xml 登记的程序集名在指定目录是否存在对应 .dll。

用法:python net_consistency.py <exe或源码根目录> [--src <cs源码目录>] [--out report.tsv]
  默认在 <根目录> 同时找 .uic/.cs/.xml。
"""
import os, re, sys, io

def find_files(root, exts, skip_samples=False):
    out = []
    for dp, dn, fn in os.walk(root):
        if skip_samples and 'Samples' in dp:
            continue
        for f in fn:
            if os.path.splitext(f)[1].lower() in exts:
                out.append(os.path.join(dp, f))
    return out

def main():
    argv = sys.argv[1:]
    src_dir = None
    dll_dir = None
    out = 'net_consistency.tsv'
    if '--src' in argv:
        i = argv.index('--src'); src_dir = argv[i+1]; argv = argv[:i] + argv[i+2:]
    if '--dll' in argv:
        i = argv.index('--dll'); dll_dir = argv[i+1]; argv = argv[:i] + argv[i+2:]
    if '--out' in argv:
        i = argv.index('--out'); out = argv[i+1]; argv = argv[:i] + argv[i+2:]
    uic_filter = None
    if '--uic' in argv:
        i = argv.index('--uic'); uic_filter = argv[i+1]; argv = argv[:i] + argv[i+2:]
    root = argv[0] if argv else '.'
    # Samples 子树仅在"审计安装根且未显式指定源"时跳过
    skip = (src_dir is None and uic_filter is None) and ('Samples' not in root)

    cs_files = find_files(src_dir or root, ('.cs',), skip)
    uic_files = find_files(uic_filter or root, ('.uic',), skip)
    xml_files = [f for f in find_files(root, ('.xml',), skip) if f.lower().endswith('addins.xml')]

    # 1) 收集 C# 里的命令 Key
    re_key = re.compile(r'Key\s*=\s*"([^"]+)"')
    cs_keys = set()
    key_where = {}
    for f in cs_files:
        text = io.open(f, encoding='utf-8', errors='replace').read()
        for m in re_key.finditer(text):
            k = m.group(1)
            if not k.startswith('Macro:'):
                cs_keys.add(k)
                key_where.setdefault(k, os.path.relpath(f, root))

    # 2) 收集 uic 里的命令引用
    re_inst = re.compile(r'<Type>\s*Instance\s*</Type>\s*(?:<CommandId>([^<]+)</CommandId>|<Key>([^<]+)</Key>)', re.S)
    re_macro = re.compile(r'<Type>\s*Macro\s*</Type>', re.S | re.I)
    re_class = re.compile(r'<Type>\s*Class\s*</Type>')
    findings = []
    n_inst = n_macro = n_class = 0
    for f in uic_files:
        text = io.open(f, encoding='utf-8', errors='replace').read()
        rel = os.path.relpath(f, root)
        for m in re_inst.finditer(text):
            cid = (m.group(1) or m.group(2) or '').strip()
            n_inst += 1
            if cid and cid not in cs_keys:
                findings.append(('Blocker', 'UIC-KEY', rel, 0, 'CommandId "%s" not found in any .cs Key' % cid))
        n_macro += len(re_macro.findall(text))
        n_class += len(re_class.findall(text))

    # 3) Addins.xml 登记与 DLL 存在性
    n_addin = 0
    for f in xml_files:
        rel = os.path.relpath(f, root)
        text = io.open(f, encoding='utf-8', errors='replace').read()
        base = os.path.dirname(f)
        for m in re.finditer(r'<string>([^<]+)</string>', text):
            name = m.group(1).strip()
            n_addin += 1
            # DLL 存在性:优先 --dll 指定的真实 exe 目录
            bases = [dll_dir, base] if dll_dir else [base]
            dlls = [os.path.join(b, os.path.basename(name) + '.dll') for b in bases]
            alt = os.path.join(root, name + '.dll')
            if not any(os.path.isfile(d) for d in dlls) and not os.path.isfile(alt):
                findings.append(('Major', 'ADDIN-DLL', rel, 0, '"%s" registered but %s not found' % (name, dlls[0])))

    with io.open(out, 'w', encoding='utf-8') as f:
        f.write('severity\trule\tfile\tline\tmessage\n')
        for s, r, p, l, t in findings:
            f.write('%s\t%s\t%s\t%d\t%s\n' % (s, r, p, l, t))
    print('cs_files=%d uic=%d instance_cmds=%d macro_cmds=%d class_cmds=%d addin_entries=%d'
          % (len(cs_files), len(uic_files), n_inst, n_macro, n_class, n_addin))
    print('findings=%d' % len(findings))
    for s, r, p, l, t in findings[:15]:
        print('  [%s] %s %s: %s' % (s, r, p, t))
    print('report ->', out)

if __name__ == '__main__':
    main()
