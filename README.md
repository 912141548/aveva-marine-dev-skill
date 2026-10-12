# AVEVA Marine 二次开发技能库（aveva-marine-dev-skill）

> AVEVA Marine (PDMS 系) 12.1 SP4 二次开发**全栈知识库 + 审计工具 + 端到端模板**，以 ZCode/Claude Skill 形式打包。
> 基于官方安装目录**全量实证**：6075 个 PML 源码文件逐文件编目 + 140 本官方手册全文挖掘 + 400 个 .NET 程序集机器反射 + 全部 PDMSUI 宏树覆盖（约 16000 文件）。

[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](LICENSE)

## 这是什么

一套可直接使用的 AVEVA Marine 二次开发参考资料与工具，覆盖：

| 轨道 | 内容 |
|---|---|
| **PML1 / PML2** | 语法规范、表单体系、对象 API 字典（25804 方法签名）、错误码 390+、任务写法频次 |
| **命令穷举（十七卷）** | 元素操作 / Draft 出图 / Router 布线 / 规格库 / 属性写法 / Isodraft / Hull / Vitesse / Spooler / MDS 支吊架 / 横切命令族 / 设计 UI 宏树，全部带源码文件行号 |
| **.NET Addin** | 184 个 PMLNetCallable 类机器验证全清单、ServiceManager/Command 模式、uic 定制、部署排错 |
| **marAPI** | 调用姿势表 + 反射全表（1413 行）|
| **Vitesse Python** | kcs_* 全函数（193 项索引）、四扩展机制（Trigger/Context_Menu/Basic_Design/_TBhook_）|
| **工具链** | PML 审计器（16 条规则、官方 6075 文件零误报）、.NET 一致性检查、一键自检、知识库自检 |
| **模板** | 5 个端到端模板 + 2 个可部署工程包（PML 表单 / C# 停靠窗 addin）|

## 作为 Skill 安装

```bash
# 方式一：克隆到 ZCode 用户技能目录
git clone https://github.com/erbi112211-boop/aveva-marine-dev-skill.git ~/.zcode/skills/aveva-marine-dev-skill

# 方式二：项目级
git clone https://github.com/erbi112211-boop/aveva-marine-dev-skill.git .agents/skills/aveva-marine-dev-skill
```

安装后，凡是涉及 AVEVA / PDMS / PML / 二次开发的问题会自动触发技能；也可用 `/skill aveva-marine-dev-skill <问题>` 强制加载。

## 目录结构

```
├── SKILL.md                    # 技能主入口：知识地图+场景路由+工具用法
├── references/
│   ├── 00-START HERE-工作区导航.md    # 第一入口
│   ├── AVEVA开发工作流一页纸.md        # 七阶段 SOP
│   ├── specs/    (4)  规范三件套: 生成规范/审核规范/记忆+修订建议
│   ├── guides/   (15) 专题速查: 表单/对象字典/错误码/EDG/marAPI/uic...
│   ├── volumes/  (20) 十七卷穷举命令本 + 元素属性权威表 + 总索引(1122 条) + 实例精讲
│   └── templates/(5)  端到端模板: 收集导出/NET停靠窗/批量改库/出图/Vitesse
├── scripts/                    # 可运行工具 (Python 3)
│   ├── pml_audit.py            # PML 审计器(核心)
│   ├── dev_check.py            # 一键开发自检
│   ├── net_consistency.py      # .NET addin 一致性
│   ├── check_docs.py           # 知识库自检
│   └── testdata/               # 审计回归样本
├── data/                       # 机器索引(防猜协议用)
│   ├── functions.tsv / object_methods.tsv / forms.tsv
│   ├── errorcode_semantics.tsv / task_idioms.tsv
│   ├── marapi_reflection.txt   # marAPI 托管 API 全表
│   └── ...
└── examples/                   # 可部署工程包
    ├── starter-kit-mycollect/  # PML 表单+网格+Excel
    └── starter-kit-mybrowser/  # C# 停靠窗 addin
```

## 快速开始

```bash
# 审查你的 PML 代码
python scripts/pml_audit.py C:/mydev/pmllib --out audit.tsv

# 查一个命令怎么写
grep -n "CONNECT" references/volumes/Marine-总索引.md          # 锚到卷三 §2
grep -n "HBORE" references/volumes/Marine-属性操作写法全编.md    # 属性写法

# 查错误码
grep "61,721" references/guides/Marine-PML错误码速查.md         # ROUTE 布线失败
```

## 知识可信层级

1. **机器验证**（反射/特性级）— 最高
2. **官方源码/手册原文**（全部带文件:行号 或 PAGE n 可回查）
3. **机器统计**（频次表/错误码配对/回调校验）
4. **归纳表述** — 已尽量带出处
5. `TODO-UNVERIFIED` — 少数待真实环境确认项（脚本 `references/guides/AVEVA-Marine-TTY环境自检脚本.md` 可关闭）

## 重新生成语料（用于你自己的安装）

索引与文档中的结论均可对你自己的 AVEVA 安装复现：

1. 修改 `scripts/_scan_pml.py` 等脚本中的源树路径（默认 `E:\AVEVA\Marine\OH12.1.SP4`）
2. 源码索引：`python scripts/_scan_pml.py`；手册：`python scripts/_extract_chm_pdfs.py`（需系统 `hh.exe`）；XLS：`python scripts/extract_xls.py`

## 版权与免责

- 本仓库内容为研究整理的分析、索引与归纳文档，**以 MIT 协议开源**（见 LICENSE）。
- 文档中引用的 AVEVA 命令语法与代码片段仅用于互操作与学习目的；AVEVA、PDMS、AVEVA Marine、Tribon 等商标及原始文档版权归 **AVEVA Solutions Limited** 所有。
- **本仓库不包含任何 AVEVA 原始发行文件**（手册全文、源码树、二进制均需从合法安装处自行生成）。
- 使用本资料进行商业开发前，请确认你持有相应的 AVEVA 软件许可。
