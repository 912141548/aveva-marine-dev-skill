# PDMS .NET Public Interface 使用总纲

> **来源与核对结论（2026-10-12）**：本文档及配套的 `references/dotnet-api/` 全量 API 文档（18 命名空间 360 类型）来自开源技能
> [garychemis/PDMS-12.1-Net-skill](https://github.com/garychemis/PDMS-12.1-Net-skill)（MIT License, Copyright (c) 2026 圆肥），已并入本技能并保留原许可。
> 并入前已对照本机 AVEVA Marine 12.1 SP4（`Aveva.Pdms.*` v12.1.4.64）的反射数据逐类型核对：**360 个类型命中 357（99.2%）**；
> 成员级抽查通过（DbElement.IsNull/IsDeleted、DbAttributeInstance 全部属性实例字段含 NAMN/APOS/ASORI、DbExpression.Parse 等）。
> 仅 3 个类型在本版不存在，属版本差异，遇到时按新式命名替换：
> `AttributeCompoundFilter`→用 `CompoundFilter`+`CombineType`；`BooleanOperator`→用 `CombineType`；`AssemblyPlanningFilter`→本版无（PDMSFilters.dll 68 类型中未收录）。
> 原文档源自 12.0 时代官方 CHM，本项目在 12.1 SP4 上实测可用。

# AVEVA PDMS .NET 开发

帮助用户使用 AVEVA PDMS 的 .NET Public Interface 进行二次开发：查找 API、编写代码、解释现有代码。

## 背景与适用范围

- **版本**：2007/2008 版 AVEVA PDMS 12.0 时代的 .NET Public Interface（`Aveva.*.dll`，.NET Framework 2.0 风格）。
- **注意**：新版 AVEVA Everything3D (E3D) 的 API 可能与本套文档有差异；使用本技能时先确认用户的目标版本。
- 文档正文为英文原文，本技能说明为中文。

## 使用流程（定位 API）

1. **确定命名空间**：先判断任务属于哪个领域，对应命名空间如下：

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

2. **打开类型文档**：到 `references/docs/<命名空间>/<完整类型名>.md` 查看该类型概述、语法与全部成员（属性/方法/事件/字段/运算符），每个成员含完整签名、参数、返回值与备注。
3. **浏览索引**：`references/docs/INDEX.md` 列出全部命名空间；每个命名空间目录下的 `INDEX.md` 列出全部类型及一句话描述——适合快速定位。

## 核心概念（务必先理解）

- **`DbElement`**：数据库元素的句柄，几乎所有操作的对象。判断"空"元素必须用 `IsNull` 属性（`element.IsNull`），不能与 null 比较。
- **`DbAttribute`**：属性标识（系统属性与 UDA 通用）。系统属性用 `DbAttributeInstance` 的静态字段引用（字段名是 PDMS 属性代码，如 `NAME`、`DESC`、`OWNER`、`APOS`（位置）、`ASORI`（方向）、`QUAL`）。传属性永远传 `DbAttribute` 对象，不要传字符串。
- **`DbElementType`**：元素类型标识（`DbElementTypeInstance` 有全部系统类型静态字段，如 `DbElementTypeInstance.EQUIPMENT`）。创建元素时必须传类型对象。
- **`Db`**：一个数据库（按 `DbType` 区分类型，如 `Design` 设计库、`Catalogue` 目录库、`Draft` 草图库）；**`MDB`**（Model Database）是模型的集合入口；**`Project`** 是项目（含多个 DB）。
- **属性值**：用 `DbElement.GetAttribute(DbAttribute)` 拿属性对象再取值，或用 `GetAsString/GetBool/GetDouble/GetInteger` 等直接取；写值用 `SetAttribute(DbAttribute, 值)`，重载覆盖 string/int/double/bool/DbElement/DbElement[]/Position/Orientation/Direction/ParameterList 等。
- **表达式**：`EvaluateString/EvaluateBool/EvaluateDouble/EvaluateElement` 可求值数据库表达式，参数是 `DbExpression` 对象，用 `DbExpression.Parse("...")` 从文本创建（如 `'A1(1,1,1)'`、`'Q1'`）；`EvaluateDouble` 还需传 `DbAttributeUnit` 单位参数（未知用 `DbAttributeUnit.NONE`）。

## 任务模式

按任务类型选用以下模式，所有代码均为真实 API 的示意（以对应 .md 文档中的签名为准）。

### 1. 独立应用（Standalone）生命周期

场景：不依赖 PDMS 交互界面的控制台/WinForms 程序。

```csharp
using Aveva.Pdms.Standalone;
using Aveva.Pdms.Database;

// 初始化独立应用（加载配置、许可等）
if (!PdmsStandalone.Start()) { PdmsStandalone.ExitError("Failed to start"); }

// 打开项目与 MDB（注意 MDB 名不带前导 '/'）
bool ok = PdmsStandalone.Open("PROJECT_NAME", "USER", "PASSWORD", "MDB_NAME");
if (!ok) { PdmsStandalone.ExitError("Failed to open"); }

// ... 业务代码：此时 Project.CurrentProject、MDB.CurrentMDB 已可用 ...

PdmsStandalone.Close();   // 关闭项目与 MDB
PdmsStandalone.Finish();  // 结束独立应用
```

- `PdmsStandalone.Project` / `PdmsStandalone.MDB` 属性直接返回当前 Project / MDB。
- 出错时用 `ExitError(Exception)` 或 `ExitError(string)` 退出并显示信息。

### 2. 打开项目 / MDB / 数据库

```csharp
using Aveva.Pdms.Database;

// 项目
Project proj = Project.CurrentProject;              // 当前项目（静态字段）
bool opened = proj.Open("proj", "user", "pass");    // 按名字打开项目（实例方法，返回 bool）
MDB mdb = Project.OpenMDB(MDBSetup.CreateMDBSetup("MDBNAME")); // OpenMDB 为静态方法，参数是 MDBSetup
proj.Close();

// MDB
MDB current = MDB.CurrentMDB;                       // 当前 MDB（静态字段）
current.Open(MDBSetup.CreateMDBSetup("MDBNAME"));   // 需要时打开：Open(MDBSetup setup)
DbElement worldEl = current.GetFirstWorld(DbType.Design); // WORLD 元素（参数 DbType，返回 DbElement）

// 数据库枚举
Db[] dbs = current.GetDBArray();                    // 全部 DB
Db db = current.GetFirstDB(DbType.Design);          // 按类型取 DB（GetDB 只接受 int 编号，见下）
DbElement world = db.World;                         // 该 DB 的 WORLD 元素
```

- `Db` 常用：`db.Name`、`db.Number`、`db.Type`、`db.World`（WORLD 元素）、`db.FindElement(...)`、`db.WorldMembers()`（官方备注：对 world 成员的常规查询会**跨数据库**）、`db.ElementExists(...)`。
- `MDB.GetDB(int dbNumber)` 按编号取 DB；按类型取用 `GetFirstDB(DbType)` / `GetDBArray(DbType)`。
- `DbType` 枚举在 `Aveva.Pdms.Database` 命名空间，值如 `Design`, `Catalogue`, `Draft`, `System` 等。

### 3. 查找元素

```csharp
using Aveva.Pdms.Database;

Db designDb = MDB.CurrentMDB.GetFirstDB(DbType.Design);
DbElement world = designDb.World;   // WORLD 元素

// 按名字在数据库中查找（签名：FindElement(string Name, DbAttribute attributeName)；找不到返回 IsNull 为 true 的空元素）
DbElement eq = designDb.FindElement("PUMP-100", DbAttributeInstance.NAME);
if (!eq.IsNull) { /* 找到 */ }

// 遍历 WORLD 直属成员（签名：WorldMembers()，返回 DbElement[] 数组）
DbElement[] members = designDb.WorldMembers();
// 遍历层级用 FirstMember / LastMember / Next / Previous 等成员方法

// 在 MDB 中用 FindElements 查找（签名：FindElements(DbType, DbAttribute, string key)）
// 官方文档只说明"按给定字符串 key 匹配"，未记载通配符行为——不要依赖 "PUMP-*" 这类写法
DbElement[] found = MDB.CurrentMDB.FindElements(DbType.Design, DbAttributeInstance.NAME, "PUMP-100");
```

- `DbElement` 导航：`Owner`（父元素）、`Previous`（前一个兄弟）、`FirstMember()` / `FirstMember(DbElementType)` / `LastMember()`、`Next()` / `Next(DbElementType)` 等。
- 空间查找：`Spatial` 类的 `ElementsInBox`、`ElementsInElementBox`、`ElementsInElementExact`、`LimitsBox` 等（按包围盒查找元素）。

### 4. 读写属性

```csharp
using Aveva.Pdms.Database;

DbElement el = ...;

// 读（属性用 DbAttributeInstance 静态字段；字段名是 PDMS 属性代码）
string name = el.GetAsString(DbAttributeInstance.NAME);
string desc = el.GetAsString(DbAttributeInstance.DESC);
double d = el.GetDouble(DbAttributeInstance.DIAM);   // 按实际属性选择（如 DIAM 等数值属性）
DbElement owner = el.GetElement(DbAttributeInstance.OWNER);  // 元素型属性

// 写
el.SetAttribute(DbAttributeInstance.NAME, "NEW-NAME");
el.SetAttribute(DbAttributeInstance.DESC, "New description");

// 引用型属性（SetAttribute 有 DbElement 重载）
// 注意：OWNER 等层级伪属性（pseudo attribute）不可通过 SetAttribute 修改——官方文档未记载其可写；
// 移动元素层级请用 InsertAfter/InsertBefore/InsertAfterLast 等成员方法（见 DbElement 的 Insert* 方法）

// 表达式求值（参数为 DbExpression 对象，用 DbExpression.Parse 从文本创建）
DbExpression refExpr = DbExpression.Parse("'A1(1,1,1)'");   // 单引号表示引用（reference）表达式
DbElement e = el.EvaluateElement(refExpr);                   // 引用表达式求值 → 元素
DbExpression numExpr = DbExpression.Parse("(DIAM * 2)");     // 数值表达式（如 (DIAM * 2)）
double dval = el.EvaluateDouble(numExpr, DbAttributeUnit.NONE);  // EvaluateDouble 还需单位参数
```

- 系统属性字段名可在 `Aveva.Pdms.Database/Aveva.Pdms.Database.DbAttributeInstance.md` 查全（2800+ 预定义属性）。

- 属性名大小写敏感；用 `DbAttributeInstance` 的静态字段避免拼写错误。
- 取值有多个重载：`GetAsString(DbAttribute)`、`GetAsString(DbAttribute, Int32)`（整数限定符/qualifier）、`GetAsString(DbAttribute, String)`（文本限定符，如 "P:"）等；数组属性用 `GetAttributeArray` / `GetAsStringArray`。
- `DbAttribute` 元数据：`Name`、`Description`、`Type`、`IsArray`、`IsPseudo`、`IsUDA`、`Units`、`AllowedValues()` 等。

### 5. 创建 / 删除元素

```csharp
using Aveva.Pdms.Database;

DbElement parent = ...;  // 父元素

// 在子列表末尾创建
DbElement el = parent.CreateLast(DbElementTypeInstance.EQUIPMENT);
// 或 CreateFirst(type) / CreateAfter(type) / CreateBefore(type) / Create(index, type)

// 复制层级（参数：被复制元素 + DbCopyOption 复制选项）
DbCopyOption opt = new DbCopyOption { IncludeRules = true, Rename = true };
DbElement copy = parent.CreateCopyHierarchyAfterLast(el, opt);

// 删除（先检查可删）
if (el.IsDeleteable) el.Delete();

// 修改类型
el.ChangeType(DbElementTypeInstance.NOZZLE);
```

- 创建后必须 `SetAttribute` 设置必要属性并保存；数据库保存用 `MDB.SaveWork(string comment)`（或 `SaveWork(Db[], string)` 保存指定 DB），工作集操作 `GetWork()` / `QuitWork()`；extract 工作流见下（"常见错误与注意事项 → 保存"）。
- `Create` 系列方法失败时抛异常。

### 6. 位置 / 方向 / 几何

```csharp
using Aveva.Pdms.Database;
using Aveva.Pdms.Geometry;

DbElement el = ...;

// 位置与方向（使用静态 Create 工厂）
Position p1 = Position.Create(1.0, 2.0, 3.0);
Position p2 = Position.Create(4.0, 5.0, 6.0);
Direction d1 = Direction.Create(p1);                 // 由位置构造方向（Create(Position)）
Direction d2 = Direction.Create(p2);                 // 同上（Create(Position)）
Orientation o = Orientation.Create(d1, d2);          // 方向合成朝向（Create(Direction, Direction)）
// 字符串重载存在（Position.Create(string)/Orientation.Create(string)），
// 但官方 CHM 未记载字符串解析格式，建议用数值重载

// 元素位置属性（APOS=位置、ASORI=方向）
el.SetAttribute(DbAttributeInstance.APOS, p1);
el.SetAttribute(DbAttributeInstance.ASORI, o);
Position pos = el.GetPosition(DbAttributeInstance.APOS);

// 几何计算
double dist = p1.Distance(p2);
Position mid = p1.MidPoint(p2);
Line line = Line.Create(p1, p2);                    // 两点成线
double dLine = p1.Distance(line);
```

- 角度/向量精细计算在 `Aveva.Pdms.Maths.Geometry`（如 `D2Angle` 支持弧度/角度、`D2Vector`、`D2Line`）。
- `LimitsBox` 用于包围盒计算；`Spatial.ElementsInBox` 用于空间查询。

### 7. 过滤器查询（Aveva.PDMS.Database.Filters）

```csharp
using Aveva.PDMS.Database.Filters;
using Aveva.Pdms.Database;

// 属性值过滤器（构造：(DbAttribute, TestOperator, Object)）
BaseFilter f1 = new AttributeValueFilter(DbAttributeInstance.NAME, TestOperator.Equals, "PUMP-100");

// 组合过滤器（AndFilter 构造：() / (BaseFilter, BaseFilter) / (BaseFilter[])）
// 注意：测试值是否支持通配符，官方 CHM 未记载——示例用精确值，避免依赖未记载行为
BaseFilter f2 = new AndFilter(
    new AttributeValueFilter(DbAttributeInstance.NAME, TestOperator.NotEquals, ""),
    new AttributeValueFilter(DbAttributeInstance.NAME, TestOperator.Equals, "PUMP-100")
);
// 判断单个元素是否匹配
bool match = f2.Valid(el);
// BaseFilter 也提供 FirstMember / Next / Members / Parent / ScanBelow 等遍历方法
```

- `TestOperator` 枚举：`None`、`Equals`、`NotEquals`、`GreaterOrEquals`、`GreaterThan`、`LessOrEquals`、`LessThan`。
- 常用过滤器：`AttributeValueFilter`（值匹配）、`AttributeRangeFilter`（范围）、`AttributeLikeFilter`（LIKE）、`AttributeListFilter`（属性+允许值数组）、`AttributeTrueFilter`/`AttributeFalseFilter`（布尔）、`AttributeRefFilter`（引用）、`AttributeCompoundFilter`、`AndFilter`/`OrFilter`（组合）、`TypeFilter`、`TrueFilter`/`FalseFilter` 等。
- **注意**：官方文档将 `AttributeValueFilter`、`AttributeRangeFilter`、`AttributeLikeFilter`、`AttributeCompoundFilter`、`BaseAttributeFilter` 标注 "CLASS IS UNDER REVIEW - DO NOT USE"，仅建议用于教学/试验（`AttributeListFilter`、`AttributeRefFilter`、`AttributeTrueFilter`/`AttributeFalseFilter` 无此标注）；正式代码优先用 `AndFilter`/`OrFilter`/`TypeFilter`/`TrueFilter`/`FalseFilter` 等。
- 查看 `Aveva.PDMS.Database.Filters/INDEX.md` 获取完整清单与签名。

### 8. 数据库事件

> **重要**：`DatabaseService` 的事件多数被官方标注 **Deprecated**（如 `Changes` 页注明 "use DbEvents.AddHandleUserChanges to add a delegate"；`Claim`/`Release`/`PreUndo`/`PostUndo` 等注明 "use DbEvents.*"）；`DbChangesEventArgs` / `DbChangesEventHandler` 官方直接标注 "Deprecated - do not use"。**新代码应优先使用 `DbEvents` 类的订阅方法**（`AddHandleUserChanges`、`AddClaimedEventHandler`、`AddReleasedEventHandler`、`AddLocalChangedEventHandler`、`AddLocalChangingEventHandler`、`AddDBFileChangedEventHandler`、`AddDBFileChangingEventHandler`、`AddDBFileChangesAllowed`、`AddCommitPendingEventHandler`、`AddFailedEventHandler`、`AddClearCacheEventHandler`），详见 `Aveva.Pdms.Database/Aveva.Pdms.Database.DbEvents.md`。

```csharp
using Aveva.Pdms.Database;

// 官方推荐的 DbEvents 订阅方式
DbEvents.AddHandleUserChanges(OnUserChanges);          // 用户数据库更改
DbEvents.AddClaimedEventHandler(OnClaimed);            // claim 事件

void OnUserChanges(DbUserChanges changes) { /* 遍历 changes 中的修改 */ }
void OnClaimed(DbElement[] eles) { }

// 旧方式（DatabaseService 静态事件）——官方标注 Deprecated，仅维护旧代码时参考
DatabaseService.Changes += OnChanges;                  // Changes 事件页注明改用 DbEvents.AddHandleUserChanges
DatabaseService.MDBOpened += OnMDBOpened;              // MDBOpened 注明将改由 DbEvents 机制替代
DatabaseService.PostOpenProject += OnPostOpenProject;

void OnChanges(object sender, DbChangesEventArgs e) { /* Deprecated：不要在新代码中使用 */ }
void OnMDBOpened(object sender, EventArgs e) { }
```

- `DatabaseService` 提供的事件：`Changes`、`Claim`、`Release`、`MDBOpened`、`MDBClosing`、`MDBClosed`、`PreGetWork`/`PostGetWork`、`PreRedo`/`PostRedo`、`PreUndo`/`PostUndo`、`PostOpenProject` 等——官方逐一标注 Deprecated 或"将由 DbEvents 机制替代"。
- 事件参数类型在 `Aveva.Pdms.Database`（如 `DbChangesEventArgs`，官方标注 Deprecated - do not use）。

### 9. 插件（Addin）

```csharp
using Aveva.ApplicationFramework;

public class MyAddin : IAddin
{
    // 注意：目标平台是 .NET Framework 2.0 时代，用传统属性语法（旧编译器不支持 => 表达式体）
    public string Name { get { return "MyAddin"; } }
    public string Description { get { return "My first addin"; } }

    public void Start(ServiceManager serviceManager)
    {
        // 注册菜单/命令/服务
    }

    public void Stop() { }
}
```

- `IAddin` 接口：`Name`、`Description`、`Start(ServiceManager)`、`Stop()`。
- `AddinManager` 负责加载/启动/停止插件（`Load`/`StartAddins`/`StopAddins`/`Unload`），事件有 `AddinLoaded`、`AddinStarted` 等。
- `ServiceManager` 获取框架服务（菜单、工具栏、窗体等，见 `Aveva.ApplicationFramework.Presentation`）。
- 完整的插件宿主项目可参考 `references/docs/Aveva.ApplicationFramework/INDEX.md`。

## 常见错误与注意事项

- **元素有效性**：任何返回 `DbElement` 的方法都可能返回空元素——永远先检查 `.IsNull` 再用，否则后续调用抛异常。
- **属性名**：优先用 `DbAttributeInstance` 静态字段；自定义 UDA 用 `DbAttribute` 对象传递。字符串属性名不匹配会抛异常。
- **MDB 名**：`PdmsStandalone.Open` 的 MDB 名不带前导 `/`。
- **线程安全**：类型页中 "Thread Safety" 注明：public static 成员线程安全，实例成员不保证。
- **版本差异**：本技能文档对应 2007/2008 版 PDMS 12.0；E3D 及更高版本的 API 名/命名空间可能有变化（例如部分类型已重构），编写代码前确认目标版本，必要时查新版文档。
- **保存**：`MDB.SaveWork(string comment)` 保存全部更改（`SaveWork(Db[], string)` 保存指定 DB）；`MDB.GetWork()` 取得工作集、`QuitWork()` 放弃更改。extract 工作流按官方签名区分两组方法：`Claim(DbElement[])` / `Release(DbElement[])`（**只收元素数组，不带注释**），`Issue(DbElement[], string)` / `Flush(DbElement[], string)` / `Drop(DbElement[], string)`（收元素数组 + 注释）；官方另提供 extract 专用的 `ExtractClaim(DbElement[])` / `ExtractRelease(DbElement[])`。修改后记得 `SaveWork` 或按项目规范提交，避免数据丢失。
- **单位**：属性值单位随数据库设置（如 `DbAttribute.Units`）；写尺寸类属性前确认单位一致。

## 参考文档

完整 API 参考（每个类型的全部成员签名与描述）位于本 skill 的：

- `references/docs/INDEX.md` — 全部命名空间索引
- `references/docs/<Namespace>/INDEX.md` — 每个命名空间的类型索引（含一句话描述）
- `references/docs/<Namespace>/<完整类型名>.md` — 单个类型文档（front-matter 含 `namespace`/`assembly`/`kind`，正文含 Syntax、Inheritance、成员小节）

给出 API 建议后，若用户需要精确签名，务必打开对应类型文档核对，不要凭记忆写。
