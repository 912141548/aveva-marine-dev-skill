# AVEVA 开发工作流一页纸(需求 → 上线 SOP)

> 七个阶段,每阶段只做一件事;工具与文档就位于本工作区。
> PML 轨与 .NET 轨共用流程,差异在②③内标注。

---

## ① 需求 → 选轨(5 分钟)

| 需求特征 | 轨道 | 起点模板 |
|---|---|---|
| 数据收集/展示/导出、表单交互 | PML | 模板① |
| 停靠窗/树/复杂 WinForms/命令状态 | .NET addin | 模板② |
| 批量写库(带撤销) | PML + 模板③ | 模板③ |
| 出图/图纸批处理 | PML + marAPI(或独立进程) | 模板④ |
| 船体专业算法/批量脚本 | Vitesse Python(2.6!) | 模板⑤ |

## ② 写码

- **PML**:`C:\mydev\pmllib\myco\{forms,functions,objects}\`,照模板抄骨架;API 查对象字典,任务写法查任务速查;**先查公共库目录再自研**。
- **.NET**:x86 + ≤3.5 工程;IAddin/Command/停靠窗照模板②;marAPI 调用查姿势表(桥类全集查反射普查卷十三);**`/*` 是 World、`SWITCH` 是合法命令**(审计器已内置)。
- **防猜协议(四级,第 86/87 轮升级)**:① 对象字典/元素类型属性权威表 → ② 源码 grep(6075 文件+十四卷) → ③ 手册 grep(pdf_text 140 本全文) → ④ 机器验证(_reflect_survey/xls_tables);查命令词先翻《Marine-总索引.md》;都无则 `TODO-UNVERIFIED`。

## ③ 自审(提交前)

```bat
python PML语料\pml_audit.py C:\mydev\pmllib --out audit.tsv
python PML语料\net_consistency.py <部署根> --src <cs目录> --uic <uic> --dll <exe目录>
```
- Blocker=0 才继续;Major 逐条豁免或修;Minor 留档。
- 语义清单过一遍(审核规范 §B):CE 层级/空集合/单位/回调副作用。

## ④ 部署

- **PML**:`q evar pmllib` 顺序确认 → `pml rehash all` → **等 10 秒** → 调用。
- **.NET**:DLL+uic+resources → exe 目录;`<模块>Addins.xml` 加程序集名;重启模块(覆盖 DLL 先退进程)。
- **入口**:PML 路线 = ADDIN 文件 + APPMENU 对象;.NET 路线 = uic + AddUICustomizationFile。
- 项目级定制 = `$1.uic`;启动钩子 = `%PDMSDFLTS%\DES-INIT-MAC`。

## ⑤ TTY 验证(→ TTY 自检脚本九段)

装载三项 → 模板冒烟 → 空集合/坏 scope 边界 → 撤销栈(MARKDB→UNDODB)→ 重复执行幂等。

## ⑥ 调试速查

| 症状 | 查 |
|---|---|
| addin 不加载 | Addins.xml 条目/位数/Start 异常自写日志 |
| 按钮无反应 | uic CommandId ≠ Command Key(跑 net_consistency) |
| 改 PML 不生效 | pml reload / kill+pml reload / rehash 时序 |
| 表单打开即错 | 回调字符串指向(跑 pml_audit FRM-01) |
| 报错 (m,c) 是什么 | 错误码速查 §1 模块号 + §5 域化实证表(87 轮已并入 60+ 码) |
| 元素属性写不上/挂错位置 | 元素类型属性权威表(Legal Attributes + Legal Owners/Members) |

## ⑦ 归档

- 报告 tsv 与代码同仓提交;新发现的官方矛盾/错误码回填速查文档;修订点追加《规范修订建议》。

---

**铁律速记**:不改标准安装目录 · rehash 后等 10 秒 · eq/ne/gt/lt 无符号比较 · `!!CE` 不写 `!CE`(成对豁免除外) · 每项 DB 写包 handle · 批量一个 savework · 防猜四步走 · PML2 复位禁 `= unset`(走命令式四关键字) · HML 语句收 `;` · .py 走 VIT 管线(PML 规则禁入)。
