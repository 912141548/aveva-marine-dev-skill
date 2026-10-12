> **并入说明**：本目录（及上级 guides/PDMS-NET-API使用总纲.md）来自 [garychemis/PDMS-12.1-Net-skill](https://github.com/garychemis/PDMS-12.1-Net-skill)，已并入 aveva-marine-dev-skill 并保留原 MIT 许可（见同目录 LICENSE.txt）。原仓库中 `aveva-pdms-dotnet/` 的技能结构在本仓库中对应 `references/dotnet-api/`（API 文档）与 `references/guides/PDMS-NET-API使用总纲.md`（使用总纲）。

# AVEVA PDMS 12.1 SP4 — .NET 二次开发 Skill

本目录是一个面向 **AVEVA PDMS 12.1 SP4** 平台的 .NET（C#/VB.NET）二次开发技能（skill），专门用于帮助编写、调试、解释和审查 AVEVA PDMS 的 .NET Public Interface 代码。

> **目标平台：AVEVA PDMS 12.1 SP4**
> 本 skill 内置的 API 参考文档源自 **2007/2008 版 AVEVA PDMS 12.0 时代**的 .NET Public Interface（`Aveva.*.dll`，.NET Framework 2.0 风格），与 PDMS 12.1 SP4 的 .NET API 基本同源、可直接使用。**新版 AVEVA Everything3D (E3D)** 的 API 可能与本套文档存在差异，使用前请先确认目标版本；必要时查阅新版文档。

## Skill 内容概述

`aveva-pdms-dotnet/SKILL.md` 是本 skill 的使用说明书，正文为中文。它帮助用户在 PDMS 中进行 .NET 二次开发，覆盖从"定位 API"到"编写/解释代码"的完整流程，并内置了完整的 API 参考文档。

- **文档规模**：18 个命名空间、约 360 个类型（380 个 .md 文档，含各命名空间 INDEX）。
- **文档语言**：参考文档正文为英文原文，skill 说明为中文。
- **触发条件**：当用户提到 "PDMS"、"E3D"、"AVEVA"、"PML"、"二次开发"、"DB 操作"、"MDB"、"Project"、"DbElement" 等词，即使没有明说写代码，也应使用本技能。

## 核心能力

- **Standalone 独立应用**：`PdmsStandalone.Start()/Open()/Close()/Finish()` 生命周期，打开项目与 MDB。
- **项目 / MDB / 数据库**：`Project`、`MDB`、`Db`、`DbElement`、`DbAttribute`、`DbElementType`、`DatabaseService`、`Spatial`。
- **查找与遍历元素**：`FindElement` / `FindElements`、`WorldMembers()`、`FirstMember/Next/Previous/Owner`，及 `Spatial.ElementsInBox` 等空间查询。
- **读写属性**：`GetAsString/GetDouble/GetPosition` 与 `SetAttribute` 系列重载；系统属性用 `DbAttributeInstance` 静态字段。
- **创建 / 删除元素**：`CreateLast/CreateFirst/CreateAfter/CreateBefore`、`CreateCopyHierarchyAfterLast`、`Delete`、`ChangeType`。
- **位置 / 方向 / 几何**：`Position`、`Direction`、`Orientation`、`Line`、`LimitsBox`；精细角度/向量计算在 `Aveva.Pdms.Maths.Geometry`。
- **过滤器查询**：`Aveva.PDMS.Database.Filters` 下的 `AttributeValueFilter`、`AndFilter`/`OrFilter`、`TypeFilter` 等。
- **数据库事件**：优先使用 `DbEvents` 类的订阅方法（官方推荐），`DatabaseService` 事件多为 Deprecated。
- **插件（Addin）**：`IAddin`、`AddinManager`、`ServiceManager`，配合 `Aveva.ApplicationFramework.Presentation` 进行界面呈现。
- **通用工具**：命令行、消息、单位、撤销/重做、字符串、跟踪等 `Aveva.Pdms.Utilities.*`。

## 命名空间速查

| 领域 | 命名空间 | 关键类型 |
|------|----------|----------|
| 独立应用入口 | `Aveva.Pdms.Standalone` | `PdmsStandalone` |
| 项目/MDB/数据库 | `Aveva.Pdms.Database` | `Project`, `MDB`, `Db`, `DbElement`, `DbAttribute`, `DbElementType`, `DatabaseService`, `Spatial` |
| 数据库过滤器查询 | `Aveva.PDMS.Database.Filters` | `AndFilter`, `AttributeValueFilter`, `AttributeListFilter`, `AttributeRangeFilter`, `AttributeLikeFilter`, `BaseFilter` |
| 几何（点/线/面/方向） | `Aveva.Pdms.Geometry` | `Position`, `Orientation`, `Direction`, `Line`, `Plane`, `LimitsBox`, `Axis` |
| 数学几何（角度/向量运算） | `Aveva.Pdms.Maths.Geometry` | `D2Angle`, `D2Vector`, `D2Line`, `D3Plane`, `D2Point` 等 |
| 管道预制/管段 | `Aveva.Pdms.Piping.Fabrication` | `PipePieceManager`, `PipeSpoolManager`, `FabricationMachineManager`, `BendingMachineResult` |
| 插件框架 | `Aveva.ApplicationFramework` | `IAddin`, `AddinManager`, `ServiceManager`, `SettingsManager` |
| 界面呈现 | `Aveva.ApplicationFramework.Presentation` | 菜单/工具栏/窗体相关 |
| 绘图 | `Aveva.Pdms.Graphics` | `DrawListManager`, `DrawList`, `Colour` |
| 共享工具 | `Aveva.Pdms.Shared` | `Selection`, `Clipboard`, `CurrentElement` |
| 命令行/消息/单位/撤销 | `Aveva.Pdms.Utilities.*` | `Command`, `PdmsMessage`, `Bore` 等 |
| 设计辅助 | `Aveva.Pdms.Design` | `Aid` |

## 使用流程（定位 API）

1. **确定命名空间**：先判断任务属于哪个领域（见上表），确定对应命名空间。
2. **打开类型文档**：到 `references/docs/<命名空间>/<完整类型名>.md` 查看该类型概述、语法与全部成员（属性/方法/事件/字段/运算符），每个成员含完整签名、参数、返回值与备注。
3. **浏览索引**：`references/docs/INDEX.md` 列出全部命名空间；每个命名空间目录下的 `INDEX.md` 列出全部类型及一句话描述，适合快速定位。给出 API 建议后，若需精确签名，务必打开对应类型文档核对，不要凭记忆写。

## 核心概念（务必先理解）

- **`DbElement`**：数据库元素的句柄，几乎所有操作的对象。判断"空"元素必须用 `IsNull` 属性（`element.IsNull`），不能与 null 比较。
- **`DbAttribute`**：属性标识（系统属性与 UDA 通用）。系统属性用 `DbAttributeInstance` 的静态字段引用（字段名是 PDMS 属性代码，如 `NAME`、`DESC`、`OWNER`、`APOS`、`ASORI`、`QUAL`）。传属性永远传 `DbAttribute` 对象，不要传字符串。
- **`DbElementType`**：元素类型标识（`DbElementTypeInstance` 有全部系统类型静态字段，如 `DbElementTypeInstance.EQUIPMENT`）。创建元素时必须传类型对象。
- **`Db`**：一个数据库（按 `DbType` 区分类型，如 `Design`、`Catalogue`、`Draft`）；**`MDB`**（Model Database）是模型的集合入口；**`Project`** 是项目（含多个 DB）。
- **属性值**：用 `DbElement.GetAttribute(DbAttribute)` 拿属性对象再取值，或用 `GetAsString/GetBool/GetDouble/GetInteger` 等直接取；写值用 `SetAttribute(DbAttribute, 值)`，重载覆盖 string/int/double/bool/DbElement/DbElement[]/Position/Orientation/Direction/ParameterList 等。
- **表达式**：`EvaluateString/EvaluateBool/EvaluateDouble/EvaluateElement` 可求值数据库表达式，参数是 `DbExpression` 对象，用 `DbExpression.Parse("...")` 从文本创建（如 `'A1(1,1,1)'`、`'Q1'`）；`EvaluateDouble` 还需传 `DbAttributeUnit` 单位参数（未知用 `DbAttributeUnit.NONE`）。

## 任务模式

`SKILL.md` 按任务类型提供了 9 种模式的可编译代码示例：

1. 独立应用（Standalone）生命周期
2. 打开项目 / MDB / 数据库
3. 查找元素
4. 读写属性
5. 创建 / 删除元素
6. 位置 / 方向 / 几何
7. 过滤器查询（`Aveva.PDMS.Database.Filters`）
8. 数据库事件
9. 插件（Addin）

完整代码示例与说明见 `aveva-pdms-dotnet/SKILL.md` 正文。

## 注意事项

- **元素有效性**：任何返回 `DbElement` 的方法都可能返回空元素——永远先检查 `.IsNull` 再用，否则后续调用抛异常。
- **属性名**：优先用 `DbAttributeInstance` 静态字段；自定义 UDA 用 `DbAttribute` 对象传递。字符串属性名不匹配会抛异常。
- **MDB 名**：`PdmsStandalone.Open` 的 MDB 名不带前导 `/`。
- **线程安全**：公开静态成员线程安全，实例成员不保证（以各类型页 "Thread Safety" 为准）。
- **版本差异**：本 skill 文档对应 2007/2008 版 PDMS 12.0；虽然与 12.1 SP4 基本同源，但 E3D 及更高版本的 API 名/命名空间可能有变化，编写代码前确认目标版本，必要时查新版文档。
- **保存**：`MDB.SaveWork(string comment)` 保存全部更改（`SaveWork(Db[], string)` 保存指定 DB）；`MDB.GetWork()` 取得工作集、`QuitWork()` 放弃更改。extract 工作流按官方签名区分两组方法：`Claim(DbElement[])` / `Release(DbElement[])`（只收元素数组，不带注释），`Issue(DbElement[], string)` / `Flush(DbElement[], string)` / `Drop(DbElement[], string)`（收元素数组 + 注释）。修改后记得 `SaveWork` 或按项目规范提交，避免数据丢失。
- **单位**：属性值单位随数据库设置（如 `DbAttribute.Units`）；写尺寸类属性前确认单位一致。
- **数据库事件**：`DatabaseService` 的事件多数被官方标注 **Deprecated**，新代码应优先使用 `DbEvents` 类的订阅方法。
- **过滤器**：官方文档将 `AttributeValueFilter`、`AttributeRangeFilter`、`AttributeLikeFilter`、`AttributeCompoundFilter`、`BaseAttributeFilter` 标注 **"CLASS IS UNDER REVIEW - DO NOT USE"**，仅建议用于教学/试验；正式代码优先用 `AndFilter`/`OrFilter`/`TypeFilter`/`TrueFilter`/`FalseFilter` 等。且官方未记载过滤测试值支持通配符，不要默认 `"PUMP-*"` 这类写法可用。

## 评测用例

`aveva-pdms-dotnet/evals/evals.json` 内置 3 个评测用例，用于验证 skill 的准确性：

1. Standalone 打开项目/MDB 并遍历 WORLD 下所有 EQUIPMENT 元素、打印名字。
2. 判断元素是否被删除（`IsDeleted`）以及设置位置/方向（`APOS` + `Position.Create`、`ASORI` + `Orientation.Create`）。
3. 用过滤器查找名字以 `PUMP-` 开头的元素并遍历，含对 "Review 中过滤器" 与通配符限制的提醒。

## 目录结构

```
AVEVA .NET 开发/PDMS 12.1/
└── aveva-pdms-dotnet/
    ├── SKILL.md                          # skill 使用说明书（中文）
    ├── references/docs/
    │   ├── INDEX.md                      # 全部命名空间索引（含类型数）
    │   └── <Namespace>/INDEX.md          # 每个命名空间的类型索引
    │   └── <Namespace>/<Type>.md         # 单个类型文档（含签名/成员）
    └── evals/
        └── evals.json                    # 3 个评测用例
```
