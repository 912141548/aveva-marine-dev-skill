# -*- coding: utf-8 -*-
"""PML 审计器 —— 《PML审核规范》A 类机器可查规则的可执行实现(第 33/85 轮)。

用法:
  python pml_audit.py <目录或文件> [--out report.tsv]
默认扫描整个目录树的 .pmlfnc/.pmlfrm/.pmlobj/.pmlmac/.mac 与 .py。

预处理三步(第 2/17 轮定稿):
  1) 剔注释行(-- / $* 开头)与 $( ... $) 块注释;
  2) 拼接行尾 $ 续行;
  3) 剔除字符串内容('...' 与 |...|,避免 |====| 之类误报)。
已含官方豁免:!CE 成对 save/restore(第 2 轮)。内置方法白名单用于回调检查略(本工具只做 A 类静态)。

第 85 轮新增(官方全树 0 命中验证后启用):
  P2-RESET-01  PML2 侧属性关键字复位 !!ce.x = unset|default(官方 0 处;复位只走命令式四关键字)
  CMD-GHOST-01 幽灵命令行首 RUNLOCK / NEW SPWE / CDATE / CATL(12.1 全树 0 命中)
  HML-01a/b    stmtExec 字面量语句与 HML 语句赋值必须以 ';' 结尾(官方 0 违规;& 拼接豁免)
  VIT-01/02    .py 独立管线:f-string / Py3 类型注解(Vitesse 为 Python 2.6;.py 严禁进 PML 规则管道)
"""
import os, io, re, sys, collections

EXTS = ('.pmlfnc', '.pmlfrm', '.pmlobj', '.pmlmac', '.mac', '.py')
re_cmt_line = re.compile(r'^\s*(--|\$\*)')
re_block_open = re.compile(r'^\s*\$\(')
re_block_close = re.compile(r'\$\)\s*$')
re_str = re.compile(r"'[^']*'|\|[^|]*\|")
re_cont = re.compile(r'\$\s*$')
ALL_FUNCS = set()   # 由 functions.tsv 装载(可选)
rules = collections.Counter()
findings = []   # (severity, rule, file, line, excerpt)

def note(sev, rule, path, ln, text):
    rules[rule] += 1
    findings.append((sev, rule, path, ln, text[:110]))

def preprocess(lines):
    """返回逻辑行列表 [(lineno, text)];注释剔除+续行拼接。字符串内容另行处理。"""
    out = []
    in_block = False
    buf, buf_ln = '', None
    for i, raw in enumerate(lines, 1):
        line = raw.rstrip('\n')
        if in_block:
            if re_block_close.search(line):
                in_block = False
            continue
        if re_block_open.match(line):
            if not re_block_close.search(line):
                in_block = True
            continue
        if re_cmt_line.match(line):
            continue
        # 续行拼接
        if re_cont.search(line):
            if buf_ln is None:
                buf_ln = i
            buf += re_cont.sub(' ', line)
            continue
        if buf_ln is not None:
            out.append((buf_ln, buf + line))
            buf, buf_ln = '', None
        else:
            out.append((i, line))
    if buf_ln is not None:
        out.append((buf_ln, buf))
    return out

re_if = re.compile(r'^\s*if\b', re.I)
re_then = re.compile(r'\bthen\b', re.I)
re_var_ce = re.compile(r'(?<![!])!CE\b')
re_save = re.compile(r'!\s*CE\s*=\s*!!\s*CE\b')
re_restore = re.compile(r'!!\s*CE\s*=\s*!\s*CE\b')
re_dollar_ce = re.compile(r'\$!CE\b|\$!!CE\b')
# ERR-01:建/删/改库痕迹(不含 object DBREF() 空引用构造,第 34 轮校准)
re_write = re.compile(r'^\s*new\s+|^\s*delete\s+|!!ce\.[a-z]\w*\s*=[^=]', re.I)
re_handle_any = re.compile(r'^\s*handle\b', re.I)
# FRM-01:回调提取
re_cb = re.compile(r"\.(callback|initcall|okcall|cancelcall|quitcall|validatecall)\s*=\s*['|\"]([^'|\"]*)", re.I)
re_this_call = re.compile(r"!this\s*\.\s*([A-Za-z_]\w*)\s*\(", re.I)
re_glob_call = re.compile(r"!!([A-Za-z_]\w*)\s*\(", re.I)
BUILTIN_FORM_METHODS = set('''hide show shown setactive setgadgetsactive setpopup removepopup
getpickedpopup newmenu setopacity subtype setundoable undoable refresh clear'''.split())
# B2:results()/members 后直接下标
re_results = re.compile(r'\.results\s*\(\s*\)|!!ce\.members\b|\.members\b', re.I)
# ---- 第 85 轮新增规则 ----
# P2-RESET-01:PML2 属性关键字复位(LHS 必须带点=属性形态;字符串哨兵 'unset' 已被 nostr 剔成 '')
re_p2reset = re.compile(r"^\s*!{1,2}[\w.]*\.\w+\s*=\s*(?:unset|default)\s*$", re.I)
# CMD-GHOST-01:幽灵命令(行首+词边界;官方全树 0 命中,第 85 轮实证)
re_ghost = re.compile(r"^\s*(?:RUNLOCK\b|NEW\s+SPWE\b|CDATE\b|CATL\b)", re.I)
# HML-01a:stmtExec(Single) 字面量语句参数
re_hml_call = re.compile(r"\bstmtExec(?:Single)?\s*\(\s*[^,()]+,\s*'([^']*)'", re.I)
# HML-01b:HML 语句单字面量赋值(& 拼接行因 $ 锚天然豁免)
re_hml_assign = re.compile(r"^\s*!\w[\w.]*\s*=\s*(['\"])([^'\"]*)\1\s*$", re.I)
re_hml_head = re.compile(r"^(?:PAN|BOU|PLA|STI|NOT|CUT|POI|CUR|SEA|EXC|WEL|FLA)\s*[,;]", re.I)
# VIT:Python 侧(独立管线,严禁套用 PML 规则)
re_ann = re.compile(r'def\s+\w+\s*\([^)]*:\s*(?:int|str|float|bool|list|dict|object|None)\b')

def load_functions(tsv):
    funcs = set()
    p = os.path.join(os.path.dirname(os.path.abspath(__file__)), tsv)
    if os.path.isfile(p):
        with io.open(p, encoding='utf-8') as f:
            next(f, None)
            for line in f:
                parts = line.split('\t')
                if len(parts) > 1:
                    funcs.add(parts[1].strip().lower().lstrip('!'))
    return funcs

def audit_python(path, lines):
    """Vitesse Python 2.6 独立管线(第 85 轮)。严禁套用 PML 规则:
    Py2.6 的 # 注释/for/while/== 会撞 PML 规则;print 语句与 except X, e 为官方合法,不得报。"""
    rel = path
    for i, raw in enumerate(lines, 1):
        line = raw.rstrip('\n')
        s = line.strip()
        if s.startswith('#'):
            continue
        # VIT-01:f-string(Py3 独有;引号配对行走,排除字符串尾部 f 与 %f 格式串假阳性)
        in_str = False
        q = ''
        j, n = 0, len(line)
        while j < n:
            ch = line[j]
            if in_str:
                if ch == '\\':
                    j += 2
                    continue
                if ch == q:
                    in_str = False
            else:
                if ch == '#':
                    break
                if ch in ('f', 'F') and j + 1 < n and line[j + 1] in ('\'', '"'):
                    prev = line[j - 1] if j > 0 else ' '
                    if not (re.match(r'\w', prev) or prev in '_%"\''):
                        note('Blocker', 'VIT-01', rel, i, line)
                        break
                if ch in ('\'', '"'):
                    in_str = True
                    q = ch
            j += 1
        # VIT-02:Py3 函数类型注解(Warning 级,先观察)
        if re_ann.search(line):
            note('Warning', 'VIT-02', rel, i, line)

def audit_file(path):
    rel = path
    try:
        lines = io.open(path, encoding='utf-8', errors='replace').readlines()
    except OSError:
        return
    ext = os.path.splitext(path)[1].lower()
    if ext == '.py':
        audit_python(path, lines)
        return
    whole = ''.join(lines)
    logical = preprocess(lines)
    methods_l = set(m.group(1).lower() for m in re.finditer(r'^\s*define\s+method\s+\.([A-Za-z_]\w*)', whole, re.M | re.I))

    # PKG 结构
    if ext == '.pmlfnc' and not re.search(r'^\s*define\s+function\b', whole, re.M | re.I):
        note('Blocker', 'PKG-01', rel, 0, 'no define function')
    if ext == '.pmlobj' and not re.search(r'^\s*define\s+object\b', whole, re.M | re.I):
        note('Blocker', 'PKG-02', rel, 0, 'no define object')
    if ext == '.pmlfrm' and not re.search(r'^\s*(setup|layout)\s+form\b', whole, re.M | re.I):
        note('Blocker', 'PKG-03', rel, 0, 'no form definition')

    # 保存/恢复对豁免集:本文件内是否存在成对 !CE = !!CE 与 !!CE = !CE
    joined = '\n'.join(t for _, t in logical)
    has_pair = bool(re_save.search(joined) and re_restore.search(joined))

    for ln, text in logical:
        nostr = re_str.sub("''", text)   # 字符串内容剔除
        # CMT-02(不含 /\*:PML 里 /* 是 World 元素语法,第 33 轮实证)
        if re.search(r'//|(^|\s)#', nostr):
            note('Blocker', 'CMT-02', rel, ln, text)
        # CTL-01 / CTL-02(不含 switch:PDMS 有合法 SWITCH 图形命令,第 33 轮实证)/ CTL-04
        if re.search(r'\bendloop\b', nostr, re.I):
            note('Blocker', 'CTL-01', rel, ln, text)
        if re.match(r'^\s*(for|while)\b', nostr, re.I):
            note('Blocker', 'CTL-02', rel, ln, text)
        if re.search(r'\bgosub\b', nostr, re.I):
            note('Blocker', 'CTL-04', rel, ln, text)
        # CTL-03a:if 行缺 then(已拼续行)
        if re_if.match(nostr) and not re_then.search(nostr):
            note('Blocker', 'CTL-03a', rel, ln, text)
        # OPR-01 / OPR-03
        if re.search(r'==|!=|>=|<=', nostr):
            note('Blocker', 'OPR-01', rel, ln, text)
        if re.search(r'&&|\|\|', nostr):
            note('Blocker', 'OPR-03', rel, ln, text)
        # VAR-02(带豁免)
        if re_var_ce.search(nostr) and not has_pair and not re_dollar_ce.search(nostr):
            note('Major', 'VAR-02', rel, ln, text)
        # VAR-01:q var 作声明
        if re.match(r'^\s*q\s+var\s+!\w+\s*$', nostr, re.I):
            note('Minor', 'VAR-01', rel, ln, text)
        # P2-RESET-01:属性关键字复位(第 85 轮)
        if re_p2reset.match(nostr):
            note('Blocker', 'P2-RESET-01', rel, ln, text)
        # CMD-GHOST-01:幽灵命令(第 85 轮)
        if re_ghost.match(nostr):
            note('Warning', 'CMD-GHOST-01', rel, ln, text)
        # HML-01a/b(第 85 轮;须用原文——字面量内容已被 nostr 剔除)
        m_hml = re_hml_call.search(text)
        if m_hml and not m_hml.group(1).rstrip().endswith(';'):
            note('Blocker', 'HML-01a', rel, ln, text)
        m_as = re_hml_assign.match(text)
        if m_as:
            stmt = m_as.group(2)
            if re_hml_head.match(stmt) and not stmt.rstrip().endswith(';'):
                note('Major', 'HML-01b', rel, ln, text)

    # ERR-01(启发式):有建/删/改库痕迹且全文无 handle
    has_write = any(re_write.search(t) for _, t in logical)
    has_handle = any(re_handle_any.match(t) for _, t in logical)
    if has_write and not has_handle:
        note('Major', 'ERR-01', rel, 0, 'db writes without any handle block')

    # FRM-01(需 functions.tsv 在脚本旁):回调指向的方法/函数是否存在
    if ext == '.pmlfrm' and ALL_FUNCS:
        for m in re_cb.finditer(whole):
            s = m.group(2).strip()
            if not s or '$' in s:
                continue
            for name in re_this_call.findall(s):
                if name.lower() not in methods_l and name.lower() not in BUILTIN_FORM_METHODS:
                    # 成员链(!this.a.b() )首段是成员,跳过
                    if not re.search(r"!this\s*\.\s*[A-Za-z_]\w*(?:\s*\.\s*[A-Za-z_]\w*)+\s*\(", s):
                        note('Blocker', 'FRM-01', rel, 0, 'callback -> this.' + name + ' not defined')
            for name in re_glob_call.findall(s):
                if name.lower() not in ALL_FUNCS:
                    note('Blocker', 'FRM-01', rel, 0, 'callback -> !!' + name + ' not found in functions.tsv')

    # B2(Minor 启发式):用 results()/members 且直接 [1] 下标,但全文无 size/empty 防护
    uses_coll = any(re_results.search(t) for _, t in logical)
    has_guard = re.search(r'\.size\s*\(\s*\)|\.empty\s*\(\s*\)|\.defined\s*\(|undefined\s*\(', joined, re.I)
    idx1 = re.search(r'\]\[1\]|\w\[1\]', joined)
    if uses_coll and idx1 and not has_guard:
        note('Minor', 'B2-GUARD', rel, 0, 'collection indexing without size/empty guard')

def main():
    global ALL_FUNCS
    ALL_FUNCS = load_functions('functions.tsv')
    argv = sys.argv[1:]
    # 剔除 --out 及其值,防止报告文件被当成审计目标自吞尾
    if '--out' in argv:
        i = argv.index('--out')
        out = argv[i + 1] if i + 1 < len(argv) else 'report.tsv'
        argv = argv[:i] + argv[i + 2:]
    else:
        out = 'report.tsv'
    args = argv
    targets = []
    for a in args:
        if os.path.isdir(a):
            for dp, dn, fn in os.walk(a):
                for f in fn:
                    if os.path.splitext(f)[1].lower() in EXTS:
                        targets.append(os.path.join(dp, f))
        elif os.path.isfile(a):
            targets.append(a)
    for t in targets:
        audit_file(t)
    findings.sort(key=lambda x: (x[1], x[2], x[3]))
    with io.open(out, 'w', encoding='utf-8') as f:
        f.write('severity\trule\tfile\tline\texcerpt\n')
        for s, r, p, l, t in findings:
            f.write('%s\t%s\t%s\t%d\t%s\n' % (s, r, p, l, t.replace('\t', ' ')))
    print('files=%d  findings=%d' % (len(targets), len(findings)))
    for r, c in rules.most_common():
        print('  %-8s %d' % (r, c))
    print('report ->', out)

if __name__ == '__main__':
    main()
