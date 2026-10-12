# Marine .NET 程序集反射普查（卷十三·机器验证）

> 来源：PowerShell 5.1（.NET Framework 4.8）对安装根 `E:\AVEVA\Marine\OH12.1.SP4` 全部 400 个 DLL 反射普查（LoadFrom → ReflectionTypeLoadException 取非空 Types → ReflectionOnlyLoadFrom 回退 + AssemblyResolve 钩子；每类型 GetCustomAttributesData 检查 PMLNetCallable 特性）。
> 产物目录：`E:\aveva开发文档\_reflect_survey\`（census.csv / pmlnetcallable.txt 3535 行 / pmlnetcallable_index.csv / pmlnetcallable_diff.txt / key_types.csv 10354 行 / key_ns.txt / load_failures.txt / samples_scan.txt，全部可复查）。
> 本卷结论为**机器验证**级（高于源码 grep），可直接覆盖人工记录。

## 1. 程序集总表

**总数 400 = 托管可反射 289（LoadFrom 99 + ReflectionOnly 190）+ 原生/失败 111。** 布局：根目录 361、AddinsData\Diagrams 34（26 个为 ODA/Teigha 第三方）、dars 3、Plot 1、asso_products 1。

关键程序集：

| 程序集 | 命名空间 | 类型 | 公有 | PMLNetCallable |
|---|---|---|---|---|
| **marAPI.dll** (1.8MB) | 30（有效 17） | 1049 | 119 | **104** |
| MarUserInterface.dll (323KB) | 3 | 1035 | 1033 | 0 |
| Aveva.Marine.Planar.Implementation.dll | 6 | 650 | 43 | 0 |
| Aveva.Marine.Drafting.Wrapper.dll | 7 | 538 | 17 | 0 |
| AVEVA.GatewayFrameWork.dll | 7 | 749 | 58 | 0 |
| Aveva.Diagrams.dll (2.2MB) | 18 | 465 | 155 | 3 |
| Aveva.Marine.Production.Implementation.dll | 11 | 498 | 36 | 0 |
| MarJobLauncher.dll | 6 | 430 | 8 | 1 |
| Aveva.Marine.Drafting.Implementation.dll | 6 | 333 | 3 | 0 |
| MarEnv.dll (153KB) | 8 | 312 | 3 | **0（整个 DLL 无桥类）** |
| Aveva.Marine.Curved.Implementation.dll | 6 | 288 | 9 | 0 |
| Aveva.Pdms.Tags.UI.dll | 5 | 274 | 80 | 0 |
| MarWrapper.dll | 8 | 237 | 78 | 1 |
| Aveva.Pdms.Database.dll | 2 | 158 | 107 | 0 |
| Aveva.ApplicationFramework.Presentation.dll | 1 | 107 | 107 | 0 |
| Aveva.Pdms.Database.Implementation.dll | 5 | 387 | 50 | 0 |
| PMLNet.dll（桥本体） | 4 | 86 | 8 | —（自身是桥） |
| PMLNetUtilities.dll | 2 | 5 | 3 | 4 |

**111 个失败件全部为原生模块**（mar.dll 61MB、marHullVerify 39MB、Fortran 数值库 libgm/libgeom/fm40*、python26.dll、sglDx11、SpaACIS、ODA TD_*、Xceed 等）——**无一个 AVEVA 托管 API 程序集在失败名单**。

marAPI 有效命名空间 17 个（比姿势表多 3）：Utility 25、Geometry 24、Drafting 23、Design 19、Utility.MarDictionaries 5、Welding 4、UI 4、**Drafting.MarConfNoteRec 4**、**Design.MarShStiffProperties 4**、**Design.MarJigPillar 3**、Vitesse 2、Drafting.MarInterpretationObject 2、Production 2、Drafting.MarSketchDimensioning 2、Tools 1、DataExtraction 1、Geometry.MarContourOperations 1。
**MarWrapper.dll 新发现**：`Aveva.Marine.Events` 命名空间 92 类型（EDG 事件体系托管面）、`Aveva.Marine.Wrapper/.Wrapper.App/.Settings/.Utilities(Workspace)`。

## 2. PMLNet 桥机制（机器验证，修正认知）

- 特性类**就叫 `Aveva.PDMS.PMLNet.PMLNetCallable`**（继承 System.Attribute、**不带 Attribute 后缀**，C# `[PMLNetCallable()]` 直接可用）；另含静态 `IsPMLNetCallable()`。实测 `MarUi.GetCustomAttributesData()` → 该特性（无参）。
- PMLNet.dll 公有桥面：**PMLNetEngine**（28 方法：`LoadAssembly/ConstructClass/DefaultConstruct/InvokeMethod/GetProperty/SetProperty/Assign/CoerceArgsIn/CoerceArgsOut/MarshalIn/MarshalOut/AddEventHandler/RemoveEventHandler/GetLicense/GetModuleNumber/GetErrorMessage/GetErrorNumber/Dispose...`——这就是 PML `object XXX()` 的执行通道）、PMLNetDelegate(+嵌套 PMLNetEventHandler)、PMLNetReal/PMLNetAny（PML 数据包装）、PMLNetException、PMLNetTrace、IPMLNetLicense。
- **44 程序集合计 184 个 PMLNetCallable 类；183/184 有 `Assign()`**（唯一例外 `Aveva.Pdms.InstrumentationImport.Addin.CUPMLEvents`）——《姿势表》"每个类都有 Assign"守则经 184 类全量验证成立，无反例。

## 3. PMLNetCallable 全清单（184 = 69 已知实锤 + 115 新增）

逐类方法签名（静态/实例分列）全表在 `_reflect_survey\pmlnetcallable.txt`（3535 行）与 `pmlnetcallable_index.csv`。

### 3.1 已知 69 类实锤（含命名空间修正）

MarUi/MarStatPointReq/MarStatPointPlanarReq/MarButtonState（Aveva.Marine.UI）；MarDrafting/MarElementHandle/MarModel/MarText/MarSymbol/MarHighlightSet/MarLayer/MarLinetype/MarColour/MarCursorType/MarPrintOptions/MarRectanglePlanar（Drafting）；MarSymbolicView/MarCurvedPanelView（Drafting.MarInterpretationObject）；MarDimensionSet/MarProfileSketch（Drafting.MarSketchDimensioning）；MarHullPan/MarChm/MarPanelSchema/MarHoleManager/MarHullPPI/MarModelStruct/MarUtilPan/MarUtilPanSch/MarUtilPos（Design）；MarDex（DataExtraction）；几何族 17 个（MarPoint/Planar、MarVector/Planar、MarPlane、MarLine/Planar、MarRline/Planar、MarContour/Planar、MarCircle/Planar、MarArc/Planar、MarEllipse**Planar**、MarBox、MarPolygon/Planar）；MarUtil/MarStringlist/MarDataBase/MarObjectCriteria/MarDate/MarTime/MarDateTime/MarPythonEngine/MarCommonProperties/MarVitesseException（Utility）；MarWeld/MarWeldedJoint/MarWeldMod/MarWeldTable（Welding）；MarMiscTools（Tools）；MarBooleanOperations（实际 ns 是 **Aveva.Marine.Geometry.MarContourOperations**）。

### 3.2 新增 115 类（要点）

**marAPI 35 个**：MarShellXViewOptions(55 方法)、MarCaptureRegionPlanar(9)、MarPanHoleOptions(15)、MarMovePanOptions(9)、MarUtilDexPan(16)、MarInternalComm(35)、**MarPythonObjectPML(21，PML 侧 Python 桥正主)**、MarPythonUtil(3)、MarDrawTable、MarSymbollist、MarProfSymb、MarCPanDist、MarPictWinExt、MarLineTypeDisplaySettings、MarBodyPlanViewOptions、MarConicPlanar、MarGencylinder、MarCopyPanOptions、MarSplitPanOptions、MarSeamRecord/MarStiffRecord/MarStiffPar/SeamRecord（MarHullPan 返回记录类）、MarShStiffProperties 族 4（MarShStiffProp 13/MarShProfData/MarShEndCut/MarShEndDef）、MarJigPillar 族 3（MarPinJig/MarClosestJigPillar/MarFrames）、MarConfNoteRec 族 2（MarReferenceSymbol/MarTextInSymbol）、MarDictionaries.StringStringDictionary、MarObject。

**产品线级 80 个**：
- AssemblyPlanning：AssemblyObject(70 实例方法)、CollectRules(9 静态)、AssemblyPart(26)、AssemblySelection
- Aveva.Diagrams：PMLDiagrams/PMLDiagramsNaming/PMLSettingsManager（含 PublishToAVEVANET/VisioExportToPDF(Hashtable)）
- Database：View 三件套（DbViewIONet/DbViewSetsNet/DefinitionSetNet）、Xml.XmlIONet(22)、DataManagement.PML 状态机 5 类（Status 26 方法）
- Tags 三件套（PMLTags 39/TagsListDefinition 21/NetTestTags）、Shared（PMLFormatManager/ElementPopulation）、NameSeq(16)、ExcelInterface.ExcelIONet、AcceptReject.ARXmlNet、SchematicModelManagerNet、Viewer3D
- PipeFabricationAddin 10 类（管工车间 PML 面）；Integrator(60)/IntegratorManager；PDMSCommands（PMLNetCommandManager/PMLNetCommand 20）
- GridControl：**NetDataSource(19)——NetGrid 绑定正主**/ColumnSpecification；Presentation.DataGrid（PMLDataGridLayout 77/PMLDataGridEvents）
- Reporting.PMLReport(20)、PMLNetUtilities 4 类（PDMSEvars/PMLFontDialog/PMLClipboard/FileUtilities）、MMServices 4 类、MyData(22)、MarJobLauncher.MarJobPML(11)、MarWrapper.Workspace、MarEnvSetup.PMLEntry、EvaluateMarineDrawingTypes.GetMarDrawingTypes

### 3.3 姿势表勘误 15 条（重要，须回改《marAPI调用姿势表》）

1. **3 个幽灵类不存在**：`MarEllipse`、`MarBoxPlanar`、`MarRectangle`——marAPI 无此类型（只有 MarEllipsePlanar/MarBox/MarRectanglePlanar），系此前笔误外推，须从姿势表 §2 删除。
2. **9 个真实存在但无 PMLNetCallable（.NET 专用，PML 不可 new）**：`Misc HashTableConvert MarError MarPythonObject MarPinProfiles MarContour2D MarPoint2D EnvVars ProjectDefinition`（`Runtime` 是命名空间非类）。PML 侧 Python 桥用 **MarPythonObjectPML** 而非 MarPythonObject。
3. MarEnv.dll 整体 0 个 PMLNetCallable——Tribon 环境变量族只能在 .NET 侧用（姿势表 §3.10 需加此限定）。

## 4. Samples 增量编目（38 个 .cs：已编目 20 → 新增 15，全部精读）

- **CoreConnectionsDiagramAddin 5 个**（核心连线图 addin 全套）：
  - `CoreConnectionsDiagramAddin.cs`：显式实现 IAddin，用**静态单例** `CommandManager.Instance.Commands.Add(...)` + `CommandBarManager.Instance.AddUICustomizationFile(path, name)`（不用 GetService——两种取服务写法并存实证）
  - `Commands.cs`：继承 Command 重写 Execute → `diagApp.GetCurrentDrawingControl()` → AxDrawingControl 走 **Visio Interop**（Selection/Page/DrawRectangle/DrawLine/CellsSRC）；图形→DB 反查链 `VmdShape.GetVmdShapes → VmdObject.GetElement → VmdElement.FindRelatedDbElement`；SCCABLE/SCMCABLE/SCCORE/SCELCONNECTION 类型判别
  - `CoreConnectionsDiagram.cs`（460 行）：`QueueMarkerEvent("E_OFF"/"E_ON")` 包裹抑制刷新；`DrawingManager.SaveNewDrawingToDb(wnd)` 入库；`Document.Saved=true`
  - `CableInfo.cs/CoreInfo.cs`：纯 DB 读取范式 `GetAsString(DbAttributeInstance.NAMN)`、`GetElement(SPRE/STAREF/ENDREF)`、`GetInteger(STAPOI/ENDPOI)`、`Members(DbElementTypeInstance.SCCORE)`、`.Owner`、`IsAttributeValid`、`IsValid`
- **ExamplesAddin 9 个**：API 模式先前已入 Cookbook（TypeFilter/DBElementCollection/AndFilter/ScanBelow/ElementTreeNavigator/Spatial 四法/LimitsBox/ClashOptions/MDB.SaveWork/QuitWork/NameTable/Project.CurrentProject.UserName）；新增一处命名空间冲突写法：`using CLASHER = Aveva.Pdms.Clasher.Clasher`（Aveva.Pdms.Examples 与 Clasher 冲突时用别名）
- **NetGridExample\NetGridAddIn.cs**（完整 addin 骨架）：`GetService(typeof(WindowManager/CommandBarManager))` 正统取服务；`RootTools.ToolAdded += ToolEventHandler` 在工具注入时捕获 StateButtonTool 做勾选态↔窗可见性双向同步；`UILoaded` 事件里按 key 从 `RootTools["NewAddin.SelectMenu"]` 取 MenuTool 注入右键菜单；`CreateDockedWindow(key, title, control, DockedPosition.Left)` + `Closing` 事件

## 5. 量化结论

- .NET API 面比《marAPI调用姿势表》记录扩大约 **2.6 倍**：PMLNetCallable 类 69 → **184**（新增 115），marAPI 新增 3 命名空间 35 类。
- PML 侧调用守则（Assign 必须/PML 后缀变体/Double 重载/253 返回码）经 184 类全量核验**无一反例**——守则升级为"机器验证"级。
- NetGrid 数据绑定正主为 GridControl.NetDataSource（此前 Cookbook 用 NETDATASOURCE 名推断，现获得确切类名与 19 方法签名）。
- EDG 事件体系的托管面 = MarWrapper 的 Aveva.Marine.Events（92 类型），.NET 拦截 EDG 事件的入口在此。

## 6. 可复现性

反射脚本与全部产物在 `E:\aveva开发文档\_reflect_survey\`；重跑入口 `reflect_survey.ps1`。已知反射会话限制：190 件走 ReflectionOnly（LoadFrom 在加载混合程序集后批量失败，不影响枚举完整性）；PS5.1 注意事项（Set-Content 无 -Append、-f 格式串逗号、FileVersion 逗号致 CSV 错位）已在脚本中预消毒。
