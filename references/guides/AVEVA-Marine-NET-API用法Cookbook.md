# AVEVA Marine .NET API 用法 Cookbook(官方 Samples 精读)

> 来源:逐类精读 `E:\AVEVA\Marine\OH12.1.SP4\Samples\` 全部 20 个 C# 源文件(2026-09-25 第 1 轮)。
> 配套:框架 API 全表在 `PML语料\net_api_applicationframework.md` 与 `net_api_presentation.md`(由官方 XML 文档自动生成,grep 查签名)。
> **重要修正**:官方示例中服务获取一律 `GetService(typeof(XxxManager))` 强转,**不是字符串**;`CommandManager/WindowManager/CommandBarManager` 另有静态 `.Instance` 单例写法(旧示例用),新代码统一 GetService。

---

## 1. IAddin 入口范式(ExamplesAddin.cs)

```csharp
void Aveva.ApplicationFramework.IAddin.Start(ServiceManager serviceManager)
{
    sCommandManager    = (CommandManager)serviceManager.GetService(typeof(CommandManager));
    sCommandBarManager = (CommandBarManager)serviceManager.GetService(typeof(CommandBarManager));

    sCommandManager.Commands.Add(new ExampleCommand());           // 注册命令

    CommandBar myToolBar = sCommandBarManager.CommandBars.AddCommandBar("ExampleCommandBar");
    ComboBoxTool tool = sCommandBarManager.RootTools.AddComboBoxTool("ExampleCommand", "Examples", null, "ExampleCommand");
    tool.SelectedIndex = 0;
    myToolBar.Tools.AddTool("ExampleCommand");                    // 工具栏挂命令
}
```

IAddin 显式实现 4 成员:`Start(ServiceManager)` / `Stop()` / `Name` / `Description`。

## 2. Command 基类(下拉分发器范式,ExampleCommand.cs)

```csharp
public ExampleCommand()
{
    Key = "ExampleCommand";
    this.List.Add("Attributes");   // List 项会喂给 ComboBoxTool 下拉
    // ...16 项:Attributes/PseudoAttribute/CE/Collections/Database/Element/Events/
    //          Filters/MDB/NameTable/Project/Spatial/Clash/TreeNavigator/Undo/UserChanges
    this.Value = "Attributes";     // 当前选中值
}
public override void Execute()
{
    string example = (string)this.Value;   // 按 Value 分发到 ExampleXxx.Run()
}
```

## 3. 数据库元素操作(ExampleElement.cs —— 最重要的一个)

入口全部走静态类,**不走 ServiceManager**:

```csharp
DbElement.GetElement("/ExampleSite")            // 按名取元素(.IsValid 判有效)
mWorld.Create(0, DbElementTypeInstance.SITE)    // 建(owner.Create(位置, 类型))
mSite.SetAttribute(DbAttributeInstance.NAME, "/ExampleSite")
mPipe.GetString(att); mPipe.GetBool(att); mPipe.GetInteger(att); mPipe.GetDouble(att)
mBran.GetElement(att) / GetDirection(att) / mEqui.GetPosition(att) / GetOrientation(att)
equi2 = equi1.CreateAfter(DbElementTypeInstance.EQUIPMENT); equi2.Copy(equi1)
equi2.CopyHierarchy(equi1, options)             // DbCopyOption{FromName/ToName/Rename} 整树复制改名
mBran.FirstMember(); headTube.Next(); .Previous; mEqui.FirstMember(NOZZLE); nozz1.Next(NOZZLE)
mBran.Members(); mEqui.Members(DbElementTypeInstance.NOZZLE); mEqui.Member(2)   // 0 基
mEqui.GetElementArray(DbAttribute.GetDbAttribute("MEMB"), DbElementType.GetElementType("NOZZ"))
nozz1.EvaluateDouble(DbExpression.Parse("HEIGHT OF PREV * 2"), DbAttributeUnit.DIST)
mCyli.SetRule(att, DbRule.CreateDbRule(expr, DbRuleStatus.DYNAMIC, DbExpressionType.REAL))
     .ExecuteAllRules(); .PropagateRules(att)
mEqui.Claim();  /* LCLM 属性查认领态; Release 前须 SaveWork */  mEqui.Release(); mEqui.ClaimHierarchy()
mTee.ChangeType(DbElementType.GetElementType("OLET"))
mSite.IsDescendant(mZone);  mElbo.AtDefault(uda); mElbo.SetAttributeDefault(uda)
```

工程/MDB 开关(Example.cs / ExampleMDB.cs):

```csharp
Project.CurrentProject.IsOpen(); Project.CurrentProject.Open("BAS","SYSTEM","/XXXXXX"); .Close()
MDBSetup.CreateMDBSetup("/CTBATEST"); MDB.CurrentMDB.Open(setUp)
MDB.CurrentMDB.GetDBArray(DbType.Design); .GetFirstWorld(DbType.Design); .Name
MDB.CurrentMDB.SaveWork("Changes made by tests"); .Close(); .QuitWork()
```

## 4. 属性读写全类型(ExampleAttributes.cs)

| 类型 | 写 | 读 |
|---|---|---|
| STRING | `SetAttribute(DbAttributeInstance.DESC, "text")` | `GetString(att)` |
| BOOLEAN | `SetAttribute(DbAttributeInstance.BUIL, true)` | `GetBool(att)` |
| INTEGER | `SetAttribute(DbAttributeInstance.REV, 3)` | `GetInteger(att)` |
| REAL | `SetAttribute(DbAttributeInstance.PRES, 60.0)` | `GetDouble(att)` |
| DBREF | `SetAttribute(HREF, el)` | `GetElement(att)` |
| DIRECTION/POSITION/ORIENTATION | `SetAttribute(HDIR, dir)` | `GetDirection/GetPosition/GetOrientation(att)` |

通用:`GetAsString(att)`、`GetAttributes()` 枚举全部属性(AttributeBrowser 用它填充列表)。

## 5. 事件体系(三个层次)

**元素生命周期回调**(ExampleEvents.cs)——静态注册,5 种:

```csharp
DbPostElementChange.AddPostCreateElement(DbElementTypeInstance.PIPE, new DbPostElementChange.PostCreateDelegate(PostCreate));
DbPostElementChange.AddPreDeleteElement(...);        // void (DbElement)
DbPostElementChange.AddPostMoveElement(...);         // void (DbElement, DbElement oldOwner, int oldpos)
DbPostElementChange.AddPostAttributeChange(DbAttributeInstance.AREA, ...);      // void (DbElement, DbAttribute)
DbPostElementChange.AddPostRefAttributeChange(DbAttributeInstance.CREF, ...);   // void (DbElement, DbAttribute, DbElement oldref)
```

**CE 变更**(ExampleCE.cs / AttributeBrowser):`CurrentElement.CurrentElementChanged += handler;`(e.Element 取新 CE);赋值 `CurrentElement.Element = ele` 也触发。

**批量变更清单**(ExampleUserChanges.cs):`DatabaseService.Changes += handler;` → `e.ChangeList.GetCreations()/GetDeletions()/GetMemberChanges()/GetModified()`;注意每次改动后需 `Pdms.Utilities.CommandLine.Command.Update()` 刷新变更队列。

## 6. 集合/过滤/树导航(ExampleCollections/Filters/TreeNavigator)

```csharp
TypeFilter filt = new TypeFilter(DbElementTypeInstance.NOZZLE);
DBElementCollection coll = new DBElementCollection(mEqui, filt);  coll.IncludeRoot = true; coll.Filter = ...;
foreach (DbElement ele in coll) { ... }

AndFilter andF = new AndFilter(); andF.Add(new TypeFilter(EQUIPMENT)); andF.Add(new TrueFilter()); andF.Valid(mEqui)
AttributeTrueFilter f1 = new AttributeTrueFilter(DbAttributeInstance.ISNAME);
BelowOrAtType f3 = new BelowOrAtType(EQUIPMENT); f3.ScanBelow(mEqui)
filt.Parent(nozz1)                       // 向上按类型找父
filt.FirstMember(mEqui); filt.Next(nozz1); filt.Members(mEqui)

CompoundFilter cf = new CompoundFilter(); cf.AddShow(filt);
ElementTreeNavigator navi = new ElementTreeNavigator(world, cf);
navi.FirstMemberInScan(world); navi.NextInScan(zone); navi.Parent(mEqui); navi.MembersInScan(mPipe)
```

## 7. 空间与碰撞(ExampleSpatial/ExampleClash)

```csharp
LimitsBox box = LimitsBox.Create(Position.Create(0,0,0), Position.Create(10000,10000,10000));
Spatial.Instance.ElementsInBox(box, false)          // false=相交即中,true=完全包含
Spatial.Instance.ElementsInElementBox(mEqui, false); .ElementInElementBox(mEqui, mBran)

// Clasher:命名冲突必须 using CLASHER = Aveva.Pdms.Clasher.Clasher;
SpatialMap.Instance.CheckSpatialMap(db); SpatialMap.Instance.BuildSpatialMap();
ClashOptions opt = ClashOptions.Create(); opt.IncludeTouches = true; opt.Clearance = 10.0;
ClashSet cs = ClashSet.Create();
if (CLASHER.Instance.CheckAll(opt, ObstructionList.Create(), cs))
    foreach (Clash c in cs.Clashes) { c.First; c.Second; c.Type; c.ClashPosition; }
```

## 8. 撤销/重做(ExampleUndo.cs)

```csharp
UndoTransaction trans = UndoTransaction.GetUndoTransaction();
trans.StartTransaction("My Transaction"); /* 改库 */ trans.EndTransaction();
UndoTransaction.PerformUndo(); UndoTransaction.PerformRedo();
// 自定义状态订阅:继承 UndoSubscriber,重写 GetBeginState/GetEndState/RestoreBeginState/RestoreEndState
UndoCaretaker.RegisterUndoSubscriber(subscriber);  UndoCaretaker.RemoveUndoSubscriber(subscriber);
```

## 9. 伪属性计算委托(ExamplePseudoAttribute.cs)

```csharp
DbAttribute uda = DbAttribute.GetDbAttribute(":VOLUME");
Ps.GetDoubleDelegate dele = new Ps.GetDoubleDelegate(VolumeCalculation);
Ps.AddGetDoubleAttribute(uda, NOUN.BOX, dele);      // UDA + 元素类型 → .NET 计算回调
static double VolumeCalculation(DbElement ele, DbAttribute att, DbQualifier qualifier)
{ return ele.GetDouble(ATT.XLEN) * ele.GetDouble(ATT.YLEN) * ele.GetDouble(ATT.ZLEN); }
```

## 10. 停靠窗 Addin 完整范式(AttributeBrowserAddin.cs —— 最全的一条龙)

```csharp
public void Start(ServiceManager serviceManager)
{
    // 1. 停靠窗(内容就是普通 WinForms UserControl)
    WindowManager windowManager = (WindowManager)serviceManager.GetService(typeof(WindowManager));
    attributeListWindow = windowManager.CreateDockedWindow("Aveva.AttributeBrowser.AttributeList",
        "Attributes", new AttributeListControl(), DockedPosition.Right);
    attributeListWindow.Width = 200;
    attributeListWindow.SaveLayout = true;                    // 布局跨会话记忆

    // 2. 命令
    ((CommandManager)serviceManager.GetService(typeof(CommandManager)))
        .Commands.Add(new ShowAttributeBrowserCommand(attributeListWindow));

    // 3. CE 事件驱动刷新
    CurrentElement.CurrentElementChanged += CurrentElement_CurrentElementChanged;

    // 4. 资源(图标)
    ResourceManager rm = (ResourceManager)serviceManager.GetService(typeof(ResourceManager));
    rm.LoadResourceFile("AttributeBrowserAddin");

    // 5. 状态栏面板
    StatusBarTextPanel p = windowManager.StatusBar.Panels.AddTextPanel("Aveva.ProjectName",
        "Project : " + Project.CurrentProject.Name);
    p.SizingMode = PanelSizingMode.Automatic;  p.Image = rm.GetImage("ID_PROJECT_ICON");

    // 6. 程序化挂 uic
    ((CommandBarManager)serviceManager.GetService(typeof(CommandBarManager)))
        .AddUICustomizationFile("AttributeBrowser.uic", "AttributeBrowser");
}
```

**状态按钮命令**(ShowAttributeBrowserCommand.cs)——按钮勾选态与窗可见性双向同步:

```csharp
this.Key = "Aveva.ShowAttributeBrowserCommand";
_window.Closed += delegate { this.Checked = false; };
WindowManager.Instance.WindowLayoutLoaded += delegate { this.Checked = _window.Visible; };
public override void Execute() { if (this.Checked) _window.Show(); else _window.Hide(); }
```

## 11. NetGridControl 数据绑定(NetGridAddinControl.cs)

```csharp
Hashtable atts   = new Hashtable(); atts[1.0]="Name"; atts[2.0]="Type"; atts[3.0]="Owner";
Hashtable titles = new Hashtable(); titles[1.0]="Name of Item"; ...
Hashtable items  = new Hashtable();               // 序号 → DbElement(经 DBElementCollection+TypeFilter 收集)
netGridControl1.BindToDataSource(new NetDataSource("Example Grid", atts, titles, items));
netGridControl1.setNameColumnImage();             // Name 列显示 PDMS 图标
netGridControl1.saveGridToExcel(path); netGridControl1.printPreview(); netGridControl1.setRowColor(1.0, colour);
netGridControl1.AfterSelectChange += new PMLNetDelegate.PMLNetEventHandler(h);   // PMLNet 委托,ArrayList 参数
netGridControl1.PopupMenu = menu;  netGridControl1.PopupMenuHeader = headerMenu; // 右键菜单(MenuTool)
```

设计器属性全集:allGridEvents / ColumnExcelFilter / ColumnSummaries / EditableGrid / ExtendLastColumn / FixedHeaders / FixedRows / HeaderSort / HideGroupByBox / OutlookGroupStyle / RowAddDeleteGrid / SingleRowSelection / Updates 等。
(与 PML 侧对应:表单里 `container ... pmlNetControl` + `object NETGRIDCONTROL()`,见 PML 技能文档 §4.3。)

## 12. PMLNet 可调用类四要素(PMLNetExample.cs,全文范式)

```csharp
using Aveva.PDMS.PMLNet;
[PMLNetCallable()]
public class PMLNetExample
{
    [PMLNetCallable()] public event PMLNetDelegate.PMLNetEventHandler PMLNetExampleEvent;  // 事件也要标
    [PMLNetCallable()] public PMLNetExample() { }
    [PMLNetCallable()] public void Assign(PMLNetExample that) { /* PML 赋值语义,无状态也要写 */ }
    [PMLNetCallable()] public void RaiseExampleEvent()
    { ArrayList args = new ArrayList(); args.Add("ExampleEvent"); PMLNetExampleEvent(args); }
}
```

跨 PML/.NET 传参用 `ArrayList`/`Hashtable` 弱类型容器;每个成员(构造/方法/事件)都要单独标 `[PMLNetCallable()]`。

## 13. Marine 独立进程(ImportDXF.cs,177 行全文范式)

```csharp
using Aveva.PDMS.Shared.StartUp;
public class Options : CommandLineOptions
{   // [OptionInfo(Short="proj")] 标注字段;无 Short 用长名
    [OptionInfo(Short="proj")] public string project = "";
    [OptionInfo(Short="user")] public string username = "";
    [OptionInfo(Short="pass")] public string password = "";
    [OptionInfo()]             public string mdb = "";
}

static bool PDMSStart(int module)
{
    PdmsApplicationImpl.Initialise();                       // 前置必须(命名空间 Aveva.Pdms.Implementation)
    PdmsApplication.Start(false /*isGraphics*/, module, false /*isBatch*/, false /*isNoConsole*/, "Standalone_log.txt");
}

// Main:
int module = 91;   // 91=Marine Drafting;不挑模块直接 PdmsStandalone.Start()(module 默认 95)
PdmsStandalone.Open(opt.project, opt.username, opt.password, opt.mdb);   // 开工程+MDB
Aveva.Marine.Utility.Misc.Init(module);                                  // Marine 模块初始化(必须)
// 注意:DXF 符号路径 —— 把 etc 目录拷到工作路径,或 marine 工程设 SBB_SYMBDIR / SBB_SYNTDIR

Aveva.Marine.Environment.Runtime.EnvVars.Instance().Get("SB_INPUT1", ref dxf_path);   // ref 出参,非返回值
if (dxf_path == "") EnvVars.Instance().Get("SBDATA", ref dxf_path);

MarDrafting drafting = new MarDrafting();                                // Aveva.Marine.Drafting
drafting.DwgDxfImport(dxf_path, name); drafting.DwgSave(); drafting.DwgClose();          // 异常 MarVitesseException

Misc.Terminate(); PdmsStandalone.Finish();                               // 对称清理
// 异常统一 catch (PdmsException ex) { PdmsStandalone.ExitError(ex); }
```

## 14. Diagrams/Visio 绘图(CoreConnectionsDiagramAddin,概览)

- 用**单例**而非 GetService:`CommandManager.Instance`、`CommandBarManager.Instance.AddUICustomizationFile(path, name)`。
- 图形→DB 反查:`VmdShape.GetVmdShapes(shape)` → `VmdObject.GetElement(vmdShape)` → `VmdElement.FindRelatedDbElement(shape)`;多芯缆 `Members(SCCABLE)` 展开;`SCELCONNECTION` 判接续。
- 新建图纸:`new DrawingControlWindow().NewDiagram()` → 画(AxDrawingControl 的 Visio API,`QueueMarkerEvent("E_OFF"/"E_ON")` 包裹抑制刷新)→ `DrawingManager.SaveNewDrawingToDb(wnd)` 入库。

---

## 15. 总表:服务/入口 → 获取方式 → 核心成员

| 服务/入口 | 获取方式 | 核心 |
|---|---|---|
| CommandManager | `GetService(typeof(CommandManager))` 或 `.Instance` | Commands.Add |
| CommandBarManager | 同上 | CommandBars.AddCommandBar / RootTools.AddButtonTool·AddComboBoxTool / RootTools[key]·Contains·ToolAdded / AddUICustomizationFile / UILoaded |
| WindowManager | 同上 | CreateDockedWindow / StatusBar / WindowLayoutLoaded |
| ResourceManager | 同上 | LoadResourceFile / GetImage |
| DockedWindow | CreateDockedWindow 返回 | Width/SaveLayout/Title/Show/Hide/Visible/Closed/Closing |
| StatusBar | windowManager.StatusBar | Panels.AddTextPanel → SizingMode/Image |
| Command 基类 | 继承 | Key/Visible/Checked/List/Value/Execute() |
| MDB / Project / DbElement / CurrentElement / DatabaseService / DbPostElementChange / Spatial / SpatialMap / Clasher / NameTable / DbPseudoAttribute / UndoTransaction / DBElementCollection / ElementTreeNavigator | 静态入口(§3-§9) | 见各节 |
| PdmsApplication / PdmsStandalone / Misc / EnvVars / MarDrafting | 静态(§13) | 独立进程 |
| SettingsManager(ApplicationFramework) | `.Instance` | AddGroup(name,dir) → SettingsGroup 索引器存取,LoadSettings/SaveSettings —— **addin 设置持久化**(存到 Local Settings\Application Data\Aveva\<应用名>) |
| Diagnostics / ElapseTimer | 静态 | WriteModules / WriteProcessorTime;Start/Stop/WriteDuration —— 性能诊断 |
| LogViewer | new | LogMessage / LogMessageFormat / Running —— 日志窗 |

## 16. Presentation 全景补充(官方 XML 文档精读,高频成员)

**Command 基类完整成员**(除 Key/Checked/Enabled/Visible/List/Value/Execute 外):
- `CancelableExecute(ArrayList)` + 事件 `BeforeCommandExecute`(**可取消的命令执行**)、`CommandExecuted`
- `Refresh(context)` —— 应用上下文变化时刷新按钮可见/可用态;`ApplicationContext`/`IsValid`(上下文有效性)
- `SelectedIndex` + `List` —— ComboBoxTool 选中项回传通道
- `Internal`(true = 不出现在运行时 Customization 对话框)
- `AttachExecutor/DetachExecutor(CommandExecutor)` —— 一个命令挂多个 UI 执行器

**CommandBarManager 增补方法**:
- **`AddOptionSet(key, …)` —— StateButtonTool 单选组**(radio,同时只有一个按下)
- `SaveLayout()/LoadLayout()` —— 命令条布局读写设置文件;`AddUICustomizationFromStream`(从流挂 uic)
- `LoadUI(name, changeMenuBar)` —— 按 uic 重建 UI;**`AddMenuItem(key, parent, …)` 程序化加菜单项**
- `Ribbon` 属性(RibbonBar/RibbonTab/RibbonTabGroup 全套可编程)+ `MiniToolbarTools` + `CustomizationDialog/AllowCustomization`
- 事件:`UILoaded` / `CommandBarLayoutLoaded`(区别于 WindowLayoutLoaded)

**WindowManager 增补**:`CreateMdiWindow(key, title, control)`(**MDI 子窗,非停靠**)、`SaveWindowLayout/LoadWindowLayout`、`SaveWindowPlacement/RestoreWindowPlacement(form)`(防屏幕外)、`MainForm`、`SplashScreen`、**`ProgressBar`(状态栏进度条对象,IProgressIndicator)**、`Windows`(集合,按键索引 IWindow)、`TabbedMdi`、`ActiveWindow`、`PreEventLoop`/`ClipboardChanged` 事件。

**工具类型全集**(RootTools/AddXxx 可建):ButtonTool / StateButtonTool / ComboBoxTool / TextBoxTool / LabelTool / ListTool / MenuTool / **PopupColorPickerTool / PopupContainerTool / PopupGalleryTool / TaskPaneTool / FontListTool / MdiWindowListTool / ContainerTool** + ValueList(下拉值列表)。定制全量成员查 `PML语料\net_api_presentation.md`(1956 行类型表)。
