# AVEVA Marine marAPI 调用姿势表(反射 + 官方 PML 用法实证)

> 来源(第 4 轮,2026-09-25):
> ① 反射 `marAPI.dll`(1.8MB)/`MarEnv.dll`/`Aveva.Marine.Assemblyplanning.Utilities.dll` 的**托管 API 全表** → `PML语料\marapi_reflection.txt`(1413 行,含每类每方法签名);
> ② PMLLIB 全库 130+ 处 `object MARxxx()` 实例化与真实调用链(逐文件取证)。
> 参考 CHM:`Documentation\NETmarAPI.chm`(1.4MB)/`marAPI.chm`/`NETAveva.Marine.PlanarAPI.chm`。

---

## 1. 机制与铁律

- **marAPI.dll 是 C++/CLI 混合程序集**(反射可见数百个原生 RTTI 残渣类型,忽略;托管类型集中在 `Aveva.Marine.*` 14 个命名空间)。
- PML 侧三步:**`import 'marapi'`(重复 import 报错,惯用 `handle(1000,0)` 吞掉)→ `using namespace 'Aveva.Marine.Xxx'` → `object 类名()`**。
- **每个类都有 `Assign(that)` 方法**——PML 赋值语义(深拷贝约定)的必备成员;实例化一律无参构造或带值构造,不自由 new 内部对象。
- **方法成对出现**:`Foo(...)` 与 `FooPML(...)`——**PML 只能调 `PML` 后缀版**或原生标量重载;凡方法签名带 `out/ref`(C++ 引用)的,PML 侧用 `PML` 变体或 Hashtable 版本。
- **Double/Int32 双重载**到处都是:PML 没有整型,传 REAL 自动匹配 **Double 版**;写文档/示例照抄 Double 版。
- 返回码约定:操作类方法返回状态码,**253 = 用户取消/中断**(见 `mDraPickElement.pmlfnc`:`if (!res eq 253) then return`);错误统一 `handle(1000,0)` 捕获后 `!!alert.error(!!error.text)`。
- **改库后调 `savework`**(PML 命令,如 `mardradrawviewframe.pmlfnc` 尾部)。

## 2. 命名空间与核心类总表(反射实证)

| 命名空间 | 类(数量) | 用途 |
|---|---|---|
| `Aveva.Marine.UI` | **MarUi**、MarStatPointReq/MarStatPointPlanarReq、MarButtonState | 图面点取/输入请求/表单动态读写 |
| `Aveva.Marine.Drafting` | **MarDrafting**(近 400 方法)、MarElementHandle、MarModel、MarText、MarSymbol、MarHighlightSet、MarLayer、MarLinetype、MarColour、MarCursorType、MarPrintOptions、MarRectanglePlanar 等 | 图纸全生命周期/元素创建编辑/视图/尺寸/标记 |
| `Aveva.Marine.Drafting.MarInterpretationObject` | MarSymbolicView、MarCurvedPanelView | 符号视图定义(面板投影) |
| `Aveva.Marine.Drafting.MarSketchDimensioning` | MarDimensionSet、MarProfileSketch | 草图尺寸集 |
| `Aveva.Marine.Design` | **MarHullPan**(面板/船体语句引擎)、MarChm(曲壳)、MarPanelSchema(语句拆分/合并)、MarHoleManager、MarHullPPI、MarModelStruct、MarUtilPan/MarUtilPanSch/MarUtilPos、各 Options 类 | 船体板/骨材操作 |
| `Aveva.Marine.DataExtraction` | **MarDex** | Tribon 式数据抽取语句 |
| `Aveva.Marine.Geometry` | MarPoint/Planar、MarVector/Planar、MarPlane、MarLine/Rline(+Planar)、MarContour/Planar、MarCircle/Arc/Ellipse**Planar**/Box/Polygon/RectanglePlanar、MarTransformation(+Planar)、MarBooleanOperations(实际 ns 为 Geometry.MarContourOperations) | 几何基元【第 86 轮反射勘误:无 MarEllipse/MarBoxPlanar/MarRectangle 幽灵类】 |
| `Aveva.Marine.Utility` | **MarUtil**、HashTableConvert※、MarStringlist、MarError※、MarDataBase/MarObjectCriteria、MarDate/Time/DateTime、**MarPythonEngine/**MarPythonObjectPML(PML 桥正主;MarPythonObject 无桥特性※)、MarCommonProperties、MarVitesseException、字典族 | 环境/坐标/应用判断/Python 桥 |
| `Aveva.Marine.Environment`(MarEnv.dll) | EnvVars※、ProjectDefinition※、Runtime(是命名空间非类※) | Tribon 环境变量(SB_*)——**整 DLL 0 个 PMLNetCallable,仅 .NET 侧可用【第 86 轮反射实证】** |
| `Aveva.Marine.Welding` | MarWeld、MarWeldedJoint、MarWeldMod、MarWeldTable | 焊缝计算 |
| `Aveva.Marine.Production` | MarPinProfiles※(无桥特性,仅 .NET) | 垫板草图生成 |
| `Aveva.Marine.Vitesse` | MarContour2D※、MarPoint2D※(均无桥特性,仅 .NET) | Python 侧几何镜像类 |
| `Aveva.Marine.Tools` | MarMiscTools | 杂项 |

> **第 86 轮反射普查勘误（详见《AVEVA-Marine-NET程序集反射普查.md》）**：标 ※ 的类**真实存在但无 PMLNetCallable 特性**——PML 不可 `object XXX()` 实例化，仅 .NET 侧可用（Misc/HashTableConvert/MarError/MarPythonObject/MarPinProfiles/MarContour2D/MarPoint2D/EnvVars/ProjectDefinition 共 9 个；Runtime 是命名空间）。全安装 PMLNetCallable 类共 **184 个**（69 已知 + 115 新增），183/184 有 Assign()，守则全量核验无反例。

## 3. PML 实证调用姿势(全部带出处)

### 3.1 标准开场(mDraPickElement.pmlfnc 全文范式)

```pml
import 'marapi'
  handle(1000,0)
    -- This error means that marapi has already been imported, ignore this error and continue.
  endhandle
using namespace 'AVEVA.Marine.UI'
using namespace 'AVEVA.Marine.Drafting'
using namespace 'AVEVA.Marine.Geometry'

!mUi    = object MARUI()
!mDraft = object MARDRAFTING()
!point  = object MARPOINTPLANAR()
!handle = object MarElementHandle()      -- 类名大小写不敏感

!res = !mUi.PointPlanarReqPML('Indicate component', !point)
handle(1000,0)
  !!alert.error(!!error.text)
  return
endhandle
if ( !res eq 253 ) then return endif     -- 253 = 用户取消

!handle  = !mDraft.ComponentIdentify(!point)        -- 图面点 → 元素句柄
!strDbRef = !mDraft.ElementDbrefGet(!handle)        -- 句柄 → 设计库 DBREF 串
!!ce = !strDbRef.dbref()                            -- 串转 PML DBREF,后续走标准 PML
```

### 3.2 MarDrafting 图纸生命周期(openmarinesheet.pmlfnc / assyhsv.pmlfnc)

```pml
!drafting = object MARDRAFTING()
if (!drafting.dwgCurrent()) then                    -- 当前有图?
  if (!drafting.dwgIsModified()) then ... !!alert.question ... !drafting.dwgSave() endif
  !drafting.dwgClose()
endif
!drafting.dwgActivate(!name)                        -- 打开已有图
!drafting.dwgSave()  /  !drafting.dwgRepaint()
```
常用方法族(反射全表):`DwgNew/DwgOpen/DwgSave/DwgSaveAs/DwgClose/DwgDelete/DwgExist/DwgCurrent/DwgIsModified/DwgRepaint/DwgZoom/DwgPurge`、导出 `DwgDxfExport/DwgDxfImport/DwgSVGExport/DwgHPGL2Export/DwgTIFExport/DwgWmfExport/DwgPreviewBmpExport/DwgSDBImport`、元素 `ElementDbrefGet/ElementTransform/ElementExtentGet/ElementCopy/ElementDelete/ElementVisibilitySet/ElementColourSet`、点取 `ComponentIdentify/ViewIdentify/TextIdentify/ModelIdentify/ContourIdentify`(入参 MarPointPlanar)、创建 `ViewNew/TextNew/NoteNew/PosnoNew/CloudNew/HatchNew/LineNew/RectangleNew/SymbolNew`、标注 `DimLinearNew/DimDiameterNew/DimRadiusNew/DimAngleNew/DimPoint3d/DimShellNew/RulerNew`、视图操作 `ViewMove/ViewScale/ViewRotate/ViewSlice/ViewProjectionSet`、属性 `ColourSet/LayerSet/TextHeightSet/TextBoldSet`、高亮 `ElementHighlight/HighlightOff`。

### 3.3 绘图几何(mardradrawviewframe.pmlfnc 全文范式)

```pml
!mStartPos = object MARPOINTPLANAR(!xMin, !yMin)    -- 带值构造
!mEndPos   = object MARPOINTPLANAR(!xMax, !yMax)
!saveColour = !mDraft.colourget()
!mColour = object MARCOLOUR(!frameColour)
  handle any
    !mColour = object MARCOLOUR('GRAY')             -- 非法色号回退字符串名
  endhandle
!mDraft.colourSet(!mColour)
!mRectanglePlanar = object MARRECTANGLEPLANAR(!mStartPos, !mEndPos)
!mDraft.rectangleNew(!mRectanglePlanar)
!mDraft.colourSet(!saveColour)
!mDraft.dwgRepaint()
savework
```
(几何类构造:`MARPOINTPLANAR(x,y)`、`MARPOINT(x,y,z)`、`MARVECTORPLANAR(dx,dy)`、`MARRECTANGLEPLANAR(p1,p2)`、`MARTRANSFORMATIONPLANAR()` + `.identityTransf()/.translate(!vec)/.scale(!s)`)

### 3.4 符号视图(assyhsv.pmlfnc —— MarSymbolicView + 平移变换)

```pml
using namespace 'Aveva.Marine.Drafting.MarInterpretationObject'
!symbDefObj = object MARSYMBOLICVIEW()
... SetPlaneByPanel/... 视图定义(反射表:SetPlaneByX/Y/Z/3Points/Panel/Curve/RSO、SetDepth、SetLimits、SetPanelsFilter、SetBlocksFilter)
!transform = object MARTRANSFORMATIONPLANAR()
!transform.scale(!vsca)
!mDrafting.elementTransform(!hSVHandle, !transform)
!hSVRect = !mDrafting.elementExtentGet(!hSVHandle)   -- 包围盒
!hSVPt1 = !hSVRect.corner1()  /  corner2()           -- 点对象有 .x()/.y() 方法
!trancVector = object MARVECTORPLANAR(!toPoint.x() - !fromPoint.x(), ...)
!transform.identityTransf() / !transform.translate(!trancVector)
```

### 3.5 MarUi 交互(反射全表 + dimcreate.pmlfnc)

```pml
!mui = object MARUI()
!mui.dimcreate(!act)                                        -- 尺寸标注交互(moddimension/modlabel 同款)
!res = !mUi.PointPlanarReqPML('提示', !point)                -- 图面点取(PML 版)
!ans = !mUi.AnswerReqPML('提示', '默认值')                    -- 字符串应答
!v   = !mUi.RealReqPML('提示', !default)  /  StringReqPML / IntReqArray / RealReqArray
!mUi.MessageConfirm('消息') / MessageNoConfirm(...)
```
反射表另见:`ChoiceSelect/StringSelect/SymbolSelect/ColourSelect`(选择对话框)、`FormXXXGet/Set(表单名,gadget名)` 动态读写其他表单控件、`AppWindowMinimize/Maximize/Refresh`、`ModelInfo`。
**对应关系**:`DimCreate(!act)` / `ModDimension()` / `ModLabel()` / `LabelCreate()` 正是 Marine 出图 dimcreate/moddimension/modlabel/glabelcreate 四个 PML 函数的全部内容——MarUI 封装了图面交互光标函数。

### 3.6 MarDex 数据抽取(phullnotch.pmlobj 范式)

```pml
using namespace 'Aveva.Marine.DataExtraction'
!getInfoObj = object MARDEX()
!extractString = 'HULL.PANEL(' & '''' & !name & '''' & ').SYMMETRY'   -- Tribon 抽取语句
!dataExtractedResult = !getInfoObj.extractPML(!extractString)
if ( !dataExtractedResult EQ 0 ) then                  -- 0 = 成功
  !getInfoObj.nextResultPML()
  !this.createdPanelSymmetry = !getInfoObj.getIntPML() -- 再取值(getString/getReal/getBoxPML...)
endif
```
反射表另见:`GetReal/GetString/GetBox/GetReavec3dPML(x&,y&,z&)/GetIndexedreal`、几何求交族 `SolveIntersectionCurvePML(String, MarElementHandle|MarPlane)`、`CreateRestrictedPlane(...)`。

### 3.7 MarHullPan 船体面板语句引擎(phullnotch/phullcombine 实证)

```pml
using namespace 'Aveva.Marine.Design'
!runObject = object MARHULLPAN()
!runObject.stmtExec( 0, 'NOT,R100, COR=1(1);' )        -- 执行船体语句(0=错误码占位)
!seamRecords = !runObject.getNearbySeams(!panelName)    -- 返回 MarSeamRecord 数组(.isSurfaceSeam()/.panelName())
!runObject.panActivate(!panelName) / .panStore() / .panSkip()
!data = !runObject.getShellStiffData(...)  / getStiffData(...) / getNotchPoints(...) / panTopology(...)
```
反射表(方法最多的类,100+):`PanInit/PanModify/PanStorageSingle/StmtExec/StmtExecSingle/GroupGet/GroupNext/ComponentGet/PanActivate/PanListActive/PanStore/PanSkip/PanMove/PanCopy/PanDelete/PanRecreate/PanSplit/PanTopology/PanRemoveSeam/PanGroupDelete/PanGroupDivide/PanStiSplitByPlane/PanCurveCreate/PanCurveStore/ViewDetailNew/ViewSymbolicRecreate/GetNearbySeams/GetNotchPoints/GetCutoutPoints/GetStiffData/GetShellStiffData/GetShellStiffPar/GetPanelStiffPar/DefaultValueSet...`。

### 3.8 MarUtil 应用/环境(marinedrafting/avevamarine/hulldesign 实证)

```pml
!util = object MarUtil()
!shipdata = !util.TBEnvironmentGet('SB_SHIPDATA')       -- 读 Tribon 环境变量(TBEnvironmentSet 写)
!util.AddCommand('...') / !util.SwitchApplication('...') / !util.ApplicationNumber('...')
if (!util.AppDrafting()) then ... endif                 -- 当前应用判断(AppBasicDesign/AppCable/AppCurvedHull/AppDiagram/AppDrafting/AppPlanarHull/AppNesting/AppPipe/AppVentilation/AppStructure/AppPlcm)
!util.TraCoordShip(!ptPlanar, 'FR', !pt3d)              -- 船坐标变换(TraCoordPan/CoordToPos/PosToCoord)
!util.TriggerAbort() / TriggerOk() / TriggerOverride()   -- Trigger 回调结束协议
!util.ExitProgram() / CleanWorkspace()
```
(反射表另见状态词法:`.Success()/.Failure()/.Yes()/.No()/.All()/.Undo()/.Options()/.Reject()/.Ok()/.Cancel()/.Quit()/.ULock()/.VLock()/.Unlock()`——Trigger 返回值常量。)

### 3.9 独立进程入口(Misc,Aveva.Marine.Utility)

反射签名:`Misc.Login(project,user,pass,server,bool,module...) → Init(module) → InitMessage()/SetCanvas(...)/DoCommand(String) → Terminate()`——与 Samples\ImportDXF 的 `PdmsApplicationImpl.Initialise()+PdmsApplication.Start()+Misc.Init(module)` 组合一致(module 91=Marine Drafting,95=缺省);异常类型 `MarVitesseException`。

### 3.10 MarEnv(Aveva.Marine.Environment)

`Aveva.Marine.Environment.Runtime.EnvVars.Instance().Get('SBDATA', ref path)`(**ref 出参**);`Aveva.Marine.Environment.ProjectDefinition` 工程定义;`admin\forms\adminapplic.pmlfrm:1335` 亦 `using namespace 'Aveva.Marine.Environment.ProjectSetup'`(Marine 工程安装界面)。

### 3.11 跨语言桥(反射发现,PML 官方未直接用但 .NET 开发可用)

- `HashTableConvert`**:PML Hashtable ↔ 强类型数组**双向打包(PackDoubleArrayToHashtable/PackHashtableToDoubleArray/Point/Vector/ElementHandle/Model/Contour/StringStringDict…共 40 方法)——写 .NET 中间层时 PML 边界数据的标配。
- `MarPythonEngine.RunPythonScript(path)`、`MarPythonObjectPML.CreatePythonObject(...)/InvokeMethod/GetProperty...`、`MarPythonUtil.AppendPythonPath`——.NET/PML 直调 Vitesse Python。
- 字典族 `StringStringDictionary` 等带 `KeysPML()/ValuesPML()`。

## 4. 防猜守则(marAPI 专用)

1. **先查本文件/`marapi_reflection.txt`** 再写调用——方法名、参数个数、是否有 PML 变体都以反射表为准;反射表没有的方法一律视为不存在(禁止凭 NETmarAPI.chm 目录印象编造)。
2. PML 调用**只用 Double 重载**;带 out 参数的方法必须用 `PML` 后缀变体或 Hashtable 版本。
3. 交互类方法(PointPlanarReqPML 等)返回 253=取消,必须判断。
4. 每个类有 `Assign()`——PML 侧 `!a = !b` 赋值依赖它,**自定义 PMLNet 类仿照实现**(见 .NET Cookbook §12)。
5. 改图/改库后:`dwgRepaint()` + `savework`。
