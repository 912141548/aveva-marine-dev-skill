# -*- coding: utf-8 -*-
"""任务→写法 习语统计:对 PMLLIB 全库按任务模式计数并采样代表行。输出 task_idioms.tsv"""
import os, io, re, collections

ROOT = r'E:\AVEVA\Marine\OH12.1.SP4\PMLLIB'
OUT = r'E:\aveva开发文档\PML语料'

tasks = {
    '收集-COLLECTION对象': re.compile(r'object\s+COLLECTION\(\)', re.I),
    '收集-VAR COLL': re.compile(r'\bvar\s+!\w+\s+coll(ect)?\b', re.I),
    '收集-kcollect': re.compile(r'!!kcollect', re.I),
    '遍历-members伪属性': re.compile(r'\.members\b', re.I),
    '批量求值-evaluate': re.compile(r'\.evaluate\s*\(', re.I),
    '求值-VAR EVALUATE': re.compile(r'\bvar\s+!\w+\s+eval(?:uate)?\b', re.I),
    '写库-savework': re.compile(r'^\s*savework\b', re.I),
    '写库-claim': re.compile(r'\.claim\s*\(\s*\)|claimhierarchy', re.I),
    '进度-fmsys.setProgress': re.compile(r'fmsys\.setprogress', re.I),
    '显示-show !!form': re.compile(r'^\s*show\s+!!', re.I),
    '显示-loadform': re.compile(r'^\s*loadform\s+!!', re.I),
    '显示-.show()': re.compile(r'\.show\s*\(\s*(\'free\'|\'at\'|\'cen\')?', re.I),
    '高亮-drawlists': re.compile(r'gphdrawlists', re.I),
    '高亮-comenhance': re.compile(r'comenhance', re.I),
    '文件-FILE对象': re.compile(r'object\s+FILE\s*\(', re.I),
    '文件-ReadFile': re.compile(r'\.readfile\s*\(', re.I),
    '单位-comUnitsConvert': re.compile(r'comunitsconvert', re.I),
    '单位-isImperialLength': re.compile(r'isimperiallength', re.I),
    'DBREF构造-object DBREF': re.compile(r'object\s+DBREF\s*\(', re.I),
    'DBREF-串转换.dbref()': re.compile(r'\.dbref\s*\(\s*\)', re.I),
    'Excel-exportToExcel': re.compile(r'exporttoexcel', re.I),
    'Excel-SaveGridToExcel': re.compile(r'savegridtoexcel', re.I),
    '撤销-MARKDB': re.compile(r'^\s*markdb\b', re.I),
    '撤销-setUndoable': re.compile(r'setundoable', re.I),
    '属性赋值-CE属性写': re.compile(r'!!ce\.[a-z]\w*\s*=[^=]', re.I),
    'EDG-EDGPACKET': re.compile(r'object\s+EDGPACKET\(\)', re.I),
    'EDG-EDGCntrl': re.compile(r'edgcntrl\.add|!!edgcntrl', re.I),
    '定义-define object TOTAL': re.compile(r'^\s*define\s+object\s', re.I),
    '弹窗-alert总计': re.compile(r'!!alert\s*\.\s*\w+', re.I),
    '消息文件-messageFile': re.compile(r'messagefile\s*\.\s*(warning|error|message)', re.I),
    '字符串-split': re.compile(r'\.split\s*\(', re.I),
    '字符串-matchwild': re.compile(r'matchwild', re.I),
    '提示-$p输出': re.compile(r'^\s*\$p\b', re.I),
    '重载-pml reload': re.compile(r'^\s*pml\s+reload', re.I),
    '事务-getwork': re.compile(r'^\s*getwork\b|comgetwork', re.I),
}

samples = {k: [] for k in tasks}
counts = {k: 0 for k in tasks}
file_sets = {k: set() for k in tasks}

for dirpath, dirnames, filenames in os.walk(ROOT):
    for fn in filenames:
        if os.path.splitext(fn)[1].lower() not in ('.pmlfnc', '.pmlfrm', '.pmlobj'):
            continue
        rel = os.path.relpath(os.path.join(dirpath, fn), ROOT)
        try:
            lines = io.open(os.path.join(dirpath, fn), encoding='utf-8', errors='replace').readlines()
        except OSError:
            continue
        for i, raw in enumerate(lines, 1):
            if re.match(r'^\s*(--|\$)', raw):
                continue
            line = raw.rstrip()
            for k, rx in tasks.items():
                if rx.search(line):
                    counts[k] += 1
                    file_sets[k].add(rel)
                    if len(samples[k]) < 3:
                        samples[k].append((rel, i, line.strip()[:130]))

with io.open(os.path.join(OUT, 'task_idioms.tsv'), 'w', encoding='utf-8') as f:
    f.write('task\tlines\tfiles\texamples\n')
    for k in sorted(counts, key=lambda x: -counts[x]):
        ex = ' || '.join('%s:%d %s' % s for s in samples[k])
        f.write('%s\t%d\t%d\t%s\n' % (k, counts[k], len(file_sets[k]), ex.replace('\t', ' ')))

for k in sorted(counts, key=lambda x: -counts[x]):
    print('%-24s lines=%-6d files=%-4d' % (k, counts[k], len(file_sets[k])))
    for s in samples[k][:2]:
        print('     %s:%d %s' % s)
