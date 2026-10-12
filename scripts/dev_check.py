# -*- coding: utf-8 -*-
"""dev_check.py —— AVEVA 开发自检一键跑(SOP 第③步自动化,第 53/89 轮)。

用法:
  python dev_check.py <你的PML源码目录> [--net <部署根>] [--src <cs目录>] [--uic <uic文件>] [--dll <exe目录>] [--out report.txt]

功能:
  1. PML 审计(pml_audit 全部规则——第 85 轮起含 P2-RESET/CMD-GHOST/HML/VIT,子进程调用自动随主脚本升级)
  2. .NET 一致性(net_consistency,如果给了 --net)
  3. ADDIN 文件格式检查(Name:/Object: 必填)
  4. 表单名 ↔ 文件名匹配检查(.pmlfrm 内 setup form 名 == 文件名)
输出:统一 PASS/FAIL 报告,含全部 Blocker/Major 明细。
"""
import os, re, sys, io, subprocess, collections

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))

def find_addin_files(root):
    """查找 ADDIN 定义文件(无扩展名,含 Name: 和 Object: 行)"""
    out = []
    for dp, dn, fn in os.walk(root):
        if 'ADDINS' in dp.upper() or 'addins' in dp:
            for f in fn:
                if os.path.splitext(f)[1] == '':
                    out.append(os.path.join(dp, f))
    return out

def check_addin_file(path):
    issues = []
    text = io.open(path, encoding='utf-8', errors='replace').read()
    has_name = bool(re.search(r'^\s*Name\s*:', text, re.M))
    has_obj = bool(re.search(r'^\s*Object\s*:', text, re.M))
    if not has_name:
        issues.append('missing "Name:" key')
    if not has_obj:
        issues.append('missing "Object:" key')
    return issues

def check_form_names(root):
    """检查 .pmlfrm 文件名与 setup form/layout form 定义的表单名是否一致"""
    issues = []
    re_frm = re.compile(r'^\s*(?:setup|layout)\s+form\s+(!!\w+)', re.M | re.I)
    for dp, dn, fn in os.walk(root):
        for f in fn:
            if not f.lower().endswith('.pmlfrm'):
                continue
            full = os.path.join(dp, f)
            base = os.path.splitext(f)[0].lower()
            try:
                text = io.open(full, encoding='utf-8', errors='replace').read()
            except OSError:
                continue
            m = re_frm.search(text)
            if m:
                form_name = m.group(1).lower().lstrip('!')
                if form_name != base:
                    issues.append((full, 'form name "%s" != file name "%s"' % (form_name, base)))
            else:
                issues.append((full, 'no setup form/layout form definition found'))
    return issues

def run_tool(script, args):
    """调用同目录下的工具脚本,返回 (returncode, stdout)"""
    cmd = [sys.executable, os.path.join(SCRIPT_DIR, script)] + args
    try:
        r = subprocess.run(cmd, capture_output=True, text=True, timeout=120,
                           cwd=SCRIPT_DIR, encoding='utf-8', errors='replace')
        return r.returncode, r.stdout
    except Exception as e:
        return -1, str(e)

def main():
    argv = sys.argv[1:]
    if not argv:
        print('Usage: python dev_check.py <PML源码目录> [--net <部署根>] [--src <cs目录>] [--uic <uic>] [--dll <exe目录>] [--out report.txt]')
        return
    pml_dir = argv[0]
    if not os.path.isdir(pml_dir):
        print('[ERR] 目录不存在: %s' % pml_dir)
        return

    net_root = None
    net_src = None
    net_uic = None
    net_dll = None
    out = os.path.join(pml_dir, 'dev_check_report.txt')
    i = 1
    while i < len(argv):
        if argv[i] == '--net' and i+1 < len(argv):
            net_root = argv[i+1]; i += 2; continue
        if argv[i] == '--src' and i+1 < len(argv):
            net_src = argv[i+1]; i += 2; continue
        if argv[i] == '--uic' and i+1 < len(argv):
            net_uic = argv[i+1]; i += 2; continue
        if argv[i] == '--dll' and i+1 < len(argv):
            net_dll = argv[i+1]; i += 2; continue
        if argv[i] == '--out' and i+1 < len(argv):
            out = argv[i+1]; i += 2; continue
        i += 1

    report = []
    blockers = 0
    majors = 0

    # === 1. PML 审计 ===
    report.append('=' * 60)
    report.append('1. PML AUDIT (pml_audit.py 16 rules)')
    report.append('=' * 60)
    rc, stdout = run_tool('pml_audit.py', [pml_dir, '--out', 'dev_audit_tmp.tsv'])
    if rc == 0 and os.path.isfile(os.path.join(SCRIPT_DIR, 'dev_audit_tmp.tsv')):
        audit_lines = io.open(os.path.join(SCRIPT_DIR, 'dev_audit_tmp.tsv'), encoding='utf-8').readlines()
        n_issues = len(audit_lines) - 1
        if n_issues == 0:
            report.append('PASS: 0 findings')
        else:
            report.append('FAIL: %d findings' % n_issues)
            for line in audit_lines[1:]:
                parts = line.strip().split('\t')
                if len(parts) >= 5:
                    sev = parts[0]
                    report.append('  [%s] %s %s:%s  %s' % (sev, parts[1], parts[2], parts[3], parts[4]))
                    if sev == 'Blocker':
                        blockers += 1
                    elif sev == 'Major':
                        majors += 1
        os.remove(os.path.join(SCRIPT_DIR, 'dev_audit_tmp.tsv'))
    else:
        report.append('ERROR: audit failed to run')
        blockers += 1

    # === 2. ADDIN 文件检查 ===
    report.append('')
    report.append('=' * 60)
    report.append('2. ADDIN FILE CHECK')
    report.append('=' * 60)
    addin_files = find_addin_files(pml_dir)
    if addin_files:
        for f in addin_files:
            issues = check_addin_file(f)
            if issues:
                report.append('FAIL: %s — %s' % (os.path.basename(f), '; '.join(issues)))
                blockers += len(issues)
            else:
                report.append('PASS: %s' % os.path.basename(f))
    else:
        report.append('(no ADDIN files found — skipping)')

    # === 3. 表单名 ↔ 文件名匹配 ===
    report.append('')
    report.append('=' * 60)
    report.append('3. FORM NAME ↔ FILE NAME CHECK')
    report.append('=' * 60)
    form_issues = check_form_names(pml_dir)
    if form_issues:
        for full, msg in form_issues:
            report.append('FAIL: %s — %s' % (os.path.basename(full), msg))
            blockers += 1
    else:
        report.append('PASS: all form names match file names')

    # === 4. .NET 一致性(可选) ===
    if net_root:
        report.append('')
        report.append('=' * 60)
        report.append('4. .NET CONSISTENCY (net_consistency.py)')
        report.append('=' * 60)
        args = [net_root]
        if net_src: args += ['--src', net_src]
        if net_uic: args += ['--uic', net_uic]
        if net_dll: args += ['--dll', net_dll]
        rc, stdout = run_tool('net_consistency.py', args)
        if rc == 0:
            for line in stdout.strip().split('\n'):
                if line.startswith('findings='):
                    n = int(line.split('=')[1])
                    if n == 0:
                        report.append('PASS: 0 findings')
                    else:
                        report.append('FAIL: %d findings' % n)
                        blockers += n
                elif line.startswith('  ['):
                    report.append('  ' + line.strip())
        else:
            report.append('ERROR: net_consistency failed')
            blockers += 1

    # === 汇总 ===
    report.append('')
    report.append('=' * 60)
    report.append('SUMMARY: %d Blocker, %d Major' % (blockers, majors))
    if blockers == 0 and majors == 0:
        report.append('STATUS: ✅ PASS — ready to deploy')
    elif blockers == 0:
        report.append('STATUS: ⚠ PASS WITH WARNINGS — review Major items')
    else:
        report.append('STATUS: ❌ FAIL — fix Blockers before deploying')
    report.append('=' * 60)

    text = '\n'.join(report)
    io.open(out, 'w', encoding='utf-8').write(text)
    print(text)
    print('\nreport -> %s' % out)

if __name__ == '__main__':
    main()
