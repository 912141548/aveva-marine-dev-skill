# -*- coding: utf-8 -*-
"""核对外部 .NET API 文档(PDMS-12.1-Net-skill)与本机安装的反射数据一致性。

用法: 修改下方三个路径常量后 python 运行。
依赖:
  - _reflect_survey/key_types.csv  (离线反射普查产物, 可用 _reflect_survey.ps1 重生成)
  - filters_types.txt              (PDMSFilters.dll 的 ReflectionOnly 类型清单, 见文档备注)
结果: 2026-10-12 实测 360 类命中 357 (99.2%), 3 个版本差异类型见
      references/guides/PDMS-NET-API使用总纲.md 头部说明。
"""
import os, io, csv, collections

DOCS = r'E:\_external\PDMS-12.1-Net-skill\aveva-pdms-dotnet\references\docs'
KEY = r'E:\aveva开发文档\_reflect_survey\key_types.csv'
FILT = r'E:\_external\filters_types.txt'

inst = set()
with io.open(KEY, encoding='utf-8-sig') as f:
    for row in csv.DictReader(f):
        t = row['Type'].strip()
        if t:
            inst.add(t.replace('+', '.'))          # 归一化嵌套类型
with io.open(FILT, encoding='utf-8-sig') as f:
    for line in f:
        line = line.strip()
        if line:
            inst.add(line)

total = ok = 0
miss = []
ns_stat = collections.defaultdict(lambda: [0, 0])
for ns in sorted(os.listdir(DOCS)):
    d = os.path.join(DOCS, ns)
    if not os.path.isdir(d):
        continue
    for fn in os.listdir(d):
        if not fn.endswith('.md') or fn.upper() == 'INDEX.MD':
            continue
        full = fn[:-3]
        total += 1
        ns_stat[ns][0] += 1
        if full in inst:
            ok += 1
            ns_stat[ns][1] += 1
        else:
            miss.append(full)

print('===== 规范化后核对结果 =====')
print('文档类型总数: %d   本机命中: %d (%.1f%%)   仍缺失: %d' % (total, ok, 100.0*ok/total, len(miss)))
print()
for ns in sorted(ns_stat):
    t, o = ns_stat[ns]
    flag = 'OK ' if o == t else '!! '
    print('%s%-42s %3d/%3d' % (flag, ns, o, t))
print()
print('--- 仍缺失清单 ---')
for m in miss:
    print(' ', m)
