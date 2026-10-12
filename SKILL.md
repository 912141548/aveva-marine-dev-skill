---
name: aveva-marine-dev-skill
description: AVEVA Marine(PDMS 系)12.1 SP4 二次开发全栈知识库与审计工具集。覆盖 PML1/PML2 宏与表单、.NET Addin 与 PDMS .NET Public Interface 全 API 参考(C#/VB.NET,18 命名空间 360 类型:DbElement/DbAttribute/Project/MDB/Filters/Geometry/PdmsStandalone)、marAPI、Vitesse Python、Isodraft/Draft 出图、Hull 船体、Paragon 规格库、Router 布线、Spooler 管件车间、MDS 支吊架等全部模块的穷举命令参考(48 份实证文档+380 份类型级 API 文档,全部带出处)。凡是涉及 AVEVA Marine、PDMS、PML 语言、PML1 宏、Design/Draft 模块、AVEVA 二次开发、addin 开发、uic、C#/.NET 调 PDMS API、DbElement/MDB/过滤器查询、命令写法查询(如 NEW/CONNECT/SPREF/DETAIL)、错误码 (m,c) 解释、PML 代码审查、PML 表单编写、船体 Hull 脚本、Vitesse Python 的任务都应使用本技能——即使用户没有明确说"查知识库",只要提到 AVEVA/PDMS 12.1 开发相关的问题就先加载本技能。
---

# AVEVA Marine 二开知识库技能

本技能是一个基于官方安装目录全量实证的 AVEVA Marine 12.1 SP4 二次开发知识库（源自 6075 个 PML 源码文件逐文件扫描 + 140 本官方手册全文 + 400 DLL 机器反射 + 全部 PDMSUI 宏树编目，约 16000 文件），配套可运行的 PML 审计工具与端到端模板；另并入 PDMS .NET Public Interface 全量 API 参考（18 命名空间 360 类型，已对 12.1 SP4 逐类型核对）。

**使用原则**：先查导航与总索引，再进具体文档；所有结论都带源码行号可回查；不要凭记忆编造 API——本知识库存在的意义就是替代猜测。

## 知识地图

```
references/
├── 00-START HERE-工作区导航.md        ← 【第一入口】三步上手+文档清单+场景决策表
├── AVEVA开发工作流一页纸.md            ← 七阶段 SOP(需求→选轨→写码→自审→部署→TTY验证→归档)
├── Marine-PML学习报告-2026-09-25.md    ← 研究全记录(查"为什么/出处"用)
├── specs/                              ← 规范三件套(写码前必读)
│   ├── PML生成规范.md / PML审核规范.md / PML记忆-语法硬约束.md
│   └── 规范修订建议-待并入.md
├── guides/                             ← 16 份专题速查(按需读)
│   ├── AVEVA-Marine-PML开发技能.md      环境/启动链/部署
│   ├── Marine-PML表单语法精要.md        setup form 体系
│   ├── Marine-PML对象API字典精要.md     对象方法签名(防猜第一步)
│   ├── Marine-PML错误码速查.md          模块号+(m,c) 语义
│   ├── Marine-PML任务写法速查.md        34 任务官方写法
│   ├── Marine-EDG事件系统精要.md        3D 交互拾取
│   ├── PDMS-NET-API使用总纲.md          ← 【.NET 开发必读】DbElement/MDB/Filters 全 API 使用说明+任务模式
│   ├── AVEVA-Marine-NET开发技能.md / NET-API用法Cookbook.md / marAPI调用姿势表.md / uic定制与部署调试手册.md
│   ├── Marine-Vitesse-Python轨道速查.md
│   └── (PDMSUI宏机制/公共库目录/帮助文档地图/TTY自检脚本)
├── dotnet-api/                         ← PDMS .NET Public Interface 全 API 文档(18 命名空间 360 类型,英文原文,带 INDEX)
│   └── 按命名空间分目录: Aveva.Pdms.Database(134)/Filters(45)/Geometry/Presentation/... 每类型一个 .md
├── volumes/                            ← 十七卷穷举命令本+权威表(查命令写法的核心)
│   ├── Marine-总索引.md                 ← 【查命令词第一站】1122 条:674 命令+255 对象+193 kcs 函数
│   ├── Marine-元素操作命令大全.md        卷一:30+元素类型 NEW/属性/连接/定位
│   ├── Marine-Draft出图操作命令大全.md   卷二 + DRA宏树大全-卷十五:标注 15 样式实现
│   ├── Marine-Router布线命令大全.md      卷三:CONNECT 六变体/P&ID 导入
│   ├── Marine-规格库操作命令大全.md      卷四:SPWLD/SPEC/选择表/SPREF
│   ├── Marine-属性操作写法全编.md        卷五:296 属性名频次表/UDA 三式/复位
│   ├── Marine-Isodraft出图命令大全.md    卷六:DETAIL/options/批处理
│   ├── Marine-Hull船体建模语句大全.md    卷七:PAN/BOU/STI/NOT 语句+MARHULLPAN
│   ├── Marine-Vitesse-Python-API全编.md  卷八:kcs_* 全函数+四扩展机制
│   ├── Marine-Spooler管件车间命令大全.md 卷九:SPOOLING/焊接/MTO
│   ├── Marine-专业模块命令大全-卷十.md   卷十:MDS/ASL/舱室/PSI/ABA
│   ├── Marine-横切命令族大全.md          卷十一:AID/GPH/CLAIM/$命令/VAR
│   ├── AVEVA-Marine-NET程序集反射普查.md 卷十三:184 个 PMLNetCallable 类
│   ├── Marine-官方手册增补-卷十四.md     手册增补 42 项(CLEANU/Q BACKREF...)
│   ├── Marine-元素类型属性权威表.md      27 元素×862 条属性+合法层级
│   ├── Marine-官方代码实例精讲.md        ← 【写码前套骨架】8 个完整实例逐段解析
│   └── (des设计UI树卷十六/跨技术等价矩阵/设计模型编目)
└── templates/                          ← 5 个端到端模板(照抄起骨架)
    └── 收集导出/NET停靠窗/批量改库/出图批处理/Vitesse船体

scripts/    ← 可运行工具(python3)
data/       ← 机器索引(functions/object_methods/forms/错误码/任务习语/反射表)
examples/   ← 2 个可部署工程包(starter-kit-mycollect/mybrowser)
```

## 场景 → 文档路由（常用）

| 任务 | 读什么 |
|---|---|
| 不确定用什么轨道( P ML/.NET/Vitesse) | 工作流一页纸 ① + volumes/跨技术等价操作矩阵 |
| 查某命令词/类/函数是否存在 | volumes/Marine-总索引.md → 锚回卷文档 |
| 写 PML 表单 | guides/表单语法精要 → templates/模板① → specs/生成规范 |
| 写 .NET 停靠窗 addin | templates/模板② → guides/NET Cookbook → uic 手册排错表 |
| 查 PDMS .NET API（类/成员签名、DbElement/MDB/Filters 用法） | guides/PDMS-NET-API使用总纲.md → dotnet-api/<命名空间>/<类型>.md |
| 查错误码 (m,c) | guides/错误码速查(§1 模块号+§5 域化表) |
| 查元素合法属性/挂载位置 | volumes/元素类型属性权威表(DMRM 27 类) |
| UDA 怎么写/怎么复位 | volumes/属性操作写法全编 §2/§5 |
| 管道布线/P&ID 导入 | volumes/Router布线命令大全 |
| 船体板/骨材/开孔 | volumes/Hull船体建模语句大全 |
| 出轴测图(Isodraft) | volumes/Isodraft出图命令大全 |
| 规格库/选择表/SPREF | volumes/规格库操作命令大全 |
| 支吊架/梯子/舱室 | volumes/专业模块命令大全-卷十 |
| 查官方手册语法原文 | guides/错误码速查对照 → data/ 索引 grep，或见卷十四增补 |
| 写完代码要审查 | 跑 scripts/pml_audit.py(见下) |
| 找不到答案 | 按"防猜协议"四级: 字典/权威表 → 各卷 grep → 手册(本地 pdf_text) → TODO-UNVERIFIED 标注 |

## 工具用法

```bash
# PML 代码审计(全部规则: 语法/控制流/回调/幽灵命令/属性复位/HML 分号/VIT Python)
python scripts/pml_audit.py <你的源码目录> --out report.tsv
# Blocker=0 才放行;官方 6075 文件回归零误报,audit_test 样本 11/11 检出

# 一键开发自检(审计+ADDIN文件+表单名匹配,可带 .NET 一致性)
python scripts/dev_check.py <PML源码目录> [--net <部署根> --src <cs目录> --uic <uic> --dll <exe目录>]

# .NET addin 一致性(uic CommandId ↔ C# Key/DLL/Addins.xml)
python scripts/net_consistency.py <部署根> --src <cs目录> --uic <uic文件> --dll <exe目录>

# 知识库自身引用完整性
python scripts/check_docs.py
```

`scripts/testdata/` 内含植入错误的回归样本（badtest.pmlfnc 等），改规则后先跑它验证检出率。

## 数据索引 grep 姿势（防猜协议）

```bash
grep -i "方法名" data/object_methods.tsv      # 25804 个对象方法签名
grep -i "函数名" data/functions.tsv            # 3689 个函数签名
grep -i "CommandId" data/forms.tsv             # 1380 个表单+gadget 清单
grep -i "(2,109)" data/errorcode_semantics.tsv # 330 错误码语义配对
grep -i "任务名" data/task_idioms.tsv          # 34 任务官方写法频次
grep -i "MarHullPan" data/marapi_reflection.txt # marAPI 托管 API 全表
```

## 核心硬规则速记（详见 specs/）

- 比较用 `eq ne gt lt ge le`——**没有** `== != > <`；逻辑用 `and or not`
- 当前元素只写 `!!CE`；每项 DB 写操作包 `handle`；批量一个 `savework`
- PML2 复位禁 `!!ce.x = unset`——走命令式四关键字（`unset/default/def/nulref`，经 `$!` 展开）
- HML 船体语句必须以 `;` 结尾；`stmtExec` 前先 `stmtGet` 读懂原语句
- `.py` 走独立 VIT 管线（Python 2.6！），PML 审计规则禁入
- `pml rehash all` 后**等约 10 秒**再调用
- 不修改标准安装目录；定制走平行目录 + 环境变量前置

## 本地语料再生（可选）

`references/` 的结论全部可在**你自己的** AVEVA 安装上回查复现：

1. 源码扫描：`python scripts/_scan_pml.py`（改脚本内源树路径指向你的 PMLLIB）
2. 手册提取：CHM 用 `scripts/_extract_chm_pdfs.py`（`hh.exe -decompile`），PDF 用 `_extract_pdfs.py`
3. XLS 属性表：`scripts/extract_xls.py`
4. 全部脚本路径常量指向 `E:\AVEVA\Marine\OH12.1.SP4`，改这两处即可迁移

## 版权与免责

本知识库为用户研究整理的**原创分析与索引**；引用的命令语法/代码片段仅用于互操作与学习目的，AVEVA、PDMS、AVEVA Marine 等商标与原始文档版权归 AVEVA Solutions Limited 所有。**未随仓库分发任何 AVEVA 原始文件**（手册全文/源码目录需从你的合法安装处生成）。

`references/dotnet-api/` 目录的 .NET API 文档来自开源项目 [garychemis/PDMS-12.1-Net-skill](https://github.com/garychemis/PDMS-12.1-Net-skill)（MIT License, Copyright (c) 2026 圆肥），并入前已对 12.1 SP4 逐类型核对（360 类命中 357）；原许可全文见 `references/dotnet-api/LICENSE.txt`。
