# AVEVA Marine 12.1 .NET 二次开发技能(IAddin · 部署 · marAPI · PMLNet)

> 实证基线:`E:\AVEVA\Marine\OH12.1.SP4`(AVEVA Marine 12.1 SP4),2026-09-25 勘察。
> 证据来源:官方 `ApplicationFramework.xml`/`ApplicationFramework.Presentation.xml`(框架 XML 文档,即 API 说明)、`Samples\` 六个官方 C# 工程、各 `*Addins.xml`/`*Customization.xml`/`*.uic`、已部署的 `ModelHoverInfoAddin.dll` 反射结果。
> PML 侧互操作写法见《AVEVA-Marine-PML开发技能.md》第 4 节。

---

## 1. 技术栈定位与硬约束

AVEVA Marine 的定制有三条平行轨道:

| 轨道 | 载体 | 适用 |
|---|---|---|
| PML(PML1/PML2) | PMLLIB 树 | 界面表单、DB 操作、宏 |
| **.NET addin** | ApplicationFramework 体系 | 停靠窗、复杂 UI、命令体系、后台逻辑 |
| Vitesse Python | `Vitesse\` 树(KCS API,Tribon 血统,**Python 2.6 语法**) | 船体基本设计/制图脚本、右键菜单、Trigger(速查《Marine-Vitesse-Python轨道速查.md》) |

**硬约束(实测验证)**:

- **必须 x86(32 位)**:64 位进程加载直接 `BadImageFormatException`(PowerShell 反射 ModelHoverInfoAddin.dll 实测);PE 头 `0x014C`。
- **目标框架 .NET Framework 2.0~3.5**:mscorlib v2.0;官方 ReadMe:"made for Microsoft Visual Studio 2008";勿用 4.x 专有 API。
- 引用 AVEVA 程序集为强名,`PublicKeyToken=17c64733a9775004`;版本跟随安装(12.1.x),升级 SP 后需重编译(Sample csproj 用 `Specific Version` 指向安装目录)。
- UI 三方库**随安装自带**:Infragistics 10.3、DevExpress 10.2、Northwoods.Go、FarPoint——项目里引用这些时**不要自带更高版本 DLL**。
- exe.config 无 supportedRuntime/assemblyBinding(全量 findstr 零命中),.NET 版本由宿主 exe 决定,不要指望 config 能救。

---

## 2. Addin 开发写法(Aveva.ApplicationFramework.IAddin)

### 2.1 最小骨架(Samples\ExamplesAddin 范式)

```csharp
using Aveva.ApplicationFramework;

public class ExamplesAddin : IAddin
{
    private CommandManager sCommandManager;
    private CommandBarManager sCommandBarManager;

    public string Name => "ExamplesAddin";
    public string Description => "Example addin";
    public void Start(ServiceManager ssm)
    {
        sCommandManager    = (CommandManager)ssm.GetService(typeof(CommandManager));      // 官方一律传 typeof
        sCommandBarManager = (CommandBarManager)ssm.GetService(typeof(CommandBarManager));
        sCommandManager.Commands.Add(new ExampleCommand());
        sCommandBarManager.RootTools.AddComboBoxTool(...);
    }
    public void Stop() { ... }
}
```

- 实现 `IAddin` 的四个成员:`Name`、`Description`、`Start(ServiceManager)`、`Stop()`。
- 官方机制(ApplicationFramework.xml 原文):`AddinManager.LoadAddins()` "will attempt to load all the addins that are defined in the XML file called 'Application.Name'Addins.xml located in the same directory as the application executable"。

### 2.2 ServiceManager 服务表(Samples 实证)

| 服务(GetService 的 typeof 参数) | 用法(Samples 出处) |
|---|---|
| `CommandManager` | `.Commands.Add(new MyCommand())`(ExamplesAddin) |
| `CommandBarManager` | `.RootTools.AddButtonTool/AddComboBoxTool`;**`.AddUICustomizationFile("Xxx.uic", "Namespace")`**(AttributeBrowserAddin) |
| `WindowManager` | `.CreateDockedWindow("Aveva.AttributeBrowser.AttributeList", "Attributes", control, DockedPosition.Right)`,返回窗带 `SaveLayout=true` 记忆布局 |
| `ResourceManager` | `.LoadResourceFile("AttributeBrowserAddin")` 载入图标资源 |
| `CurrentElement` | 事件 `.CurrentElementChanged` 监听当前元素变化 |
| `StatusBar` | `.Panels.AddTextPanel(...)` 加状态栏面板 |

### 2.3 命令类(挂按钮的单元)

```csharp
public class ShowCommand : Command   // Aveva.ApplicationFramework.Presentation
{
    public ShowCommand() { Key = "Aveva.AttributeBrowser.Show"; }
    public override void Execute(...) { /* 干活 */ }
}
```

- `Key` 是命令唯一 ID,**必须与 uic 里的 `CommandId` 一致**(见第 4 节)。
- 命令可带 Enabled/Checked 状态事件,由框架管理按钮状态。

### 2.4 官方范例索引(`OH12.1.SP4\Samples\`,另有 Samples.zip)

| 工程 | 学什么 |
|---|---|
| `Samples\ExamplesAddin\` | IAddin 骨架 + 17 个专题示例类(Database/Element/Events/Filters/MDB/Spatial/Clasher/Undo…);**目录里自带一份 DesignAddins.xml(部署模板)** |
| `Samples\AttributeBrowserAddin\` | 最完整:停靠窗 + uic 程序化挂载 + 资源 + CurrentElementChanged + 状态栏 |
| `Samples\NetGridExample\` | WinForms DataGridView 停靠窗(110 行最小完整例) |
| `Samples\PMLNetExample\` | PMLNet 桥(见第 5 节) |
| `Samples\PMLGridExample\` | 纯 PML 对照(`PMLGridExample.pmlfrm`) |
| `Samples\ImportDXF\` | **独立控制台程序**(不开 GUI,见第 6 节) |

csproj 引用写法(照抄即可):`Aveva.ApplicationFramework, Version=1.1.11.0`、`Aveva.ApplicationFramework.Presentation, Version=108.6128.11.0`、`Aveva.Pdms.Database/Shared/Utilities, Version=12.0.0.1023`,HintPath 指向安装目录。

**逐类 API 用法查证入口(第 1 轮循环研究成果)**:
- 《AVEVA-Marine-NET-API用法Cookbook.md》——Samples 全部 20 个 C# 文件逐类精读的 cookbook(元素 CRUD/事件三体系/集合过滤/空间碰撞/撤销/停靠窗/NetGrid/独立进程/Diagrams 绘图),**写代码先查它**;
- `PML语料\net_api_applicationframework.md` / `net_api_presentation.md` —— 官方 XML 文档生成的框架 API 全表(grep 查签名);
- 补充要点:`CommandManager/WindowManager/CommandBarManager` 另有静态 `.Instance` 单例写法(旧示例用,新代码统一 GetService);`SettingsManager.Instance` 可持久化 addin 设置(存到 Local Settings\Application Data\Aveva\<应用名>);`Diagnostics`/`ElapseTimer` 做性能诊断;`LogViewer` 做日志窗。

---

## 3. Addin 部署(零注册,三步走)

1. **放 DLL**:编译出的 x86 DLL 拷到 exe 目录(`OH12.1.SP4\`);依赖的 AVEVA DLL 已在,无需拷贝。
2. **登记**:在目标模块的 `<应用名>Addins.xml` 加一行(格式为 `ArrayOfString`,每项是**程序集名,不带 .dll**):

```xml
<ArrayOfString ...>
  <string>ExplorerAddin</string>
  ...
  <string>ModelHoverInfoAddin</string>   <!-- 自研 addin 就这样加 -->
</ArrayOfString>
```

   也可用相对 exe 目录的路径项把不常用 addin 挪进子目录:`<string>AddinsData\Diagrams\DiagramsDWGExportAddin</string>`(DiagramsAddins.xml 实例)。
3. **重启模块**生效。装载期框架事件:`AddinLoaded / AddinStarting / AddinStarted`。

- **不碰**注册表、GAC、exe.config(全树验证)。
- 模块 ↔ Addins.xml 映射表见《AVEVA-Marine-PML开发技能.md》第 1.2 节(源自 marine.bat);注意 `marinedraftingaddins.xml` 是全小写文件名。
- DLL 被运行中的模块进程锁定,**覆盖新版本前先退出该模块**。

---

## 4. UI 挂接:Customization.xml 与 .uic

> **uic 全语法/命令四形态/排错树查《AVEVA-Marine-uic定制与部署调试手册.md》**(第 8 轮,42 个 uic 普查实证)。

### 4.1 两层机制

- `<应用名>Customization.xml`(如 `DesignCustomization.xml`)只是 **uic 文件清单**:

```xml
<UICustomizationSet ...>
  <UICustomizationFiles>
    <CustomizationFile Name="Module" Path="design.uic" />
    <CustomizationFile Name="Project" Path="$1.uic" />   <!-- $1.uic = 项目级定制 -->
  </UICustomizationFiles>
</UICustomizationSet>
```

- `.uic` 才是命令/按钮定义处,顶层节点:`Tools / InstanceTools / CommandBars / TaskPanes / ContextMenus / Tabs / QATTools / NavigationMenuTools / Namespace` 等。

### 4.2 两种按钮命令类型(实文范例)

**挂 .NET Command**(`ConnMap.uic`,Type=Instance,`CommandId` = Command.Key):

```xml
<ButtonTool Name="ConnectionMap.Center">
  <Command><Type>Instance</Type><CommandId>AVEVA.ConnectionMap.Center</CommandId><Arguments /></Command>
  <ImageResourceId>ConnMapResources:ScheModViewCenter.png</ImageResourceId>
  <Caption>Center</Caption>
</ButtonTool>
```

**直接挂 PML**(`AVEVA.Marine.UI.MarineDrafting.uic`,Type=Macro):

```xml
<Command>
  <Type>Macro</Type>
  <Macro>!!assyInit('MAIN')</Macro>
  <Key>Macro:44b598be-...</Key>
</Command>
```

**插入到既有菜单**(用 `InstanceTools` 的定位属性):

```xml
<InstanceTools>
  <Tool Name="Aveva.DwgExportAddin.DwgExport2"
        Parent="AVEVA.Diagrams.Menu.File.Export"
        AfterSibling="AVEVA.Diagrams.Button.FileExportDocument" />
</InstanceTools>
```

### 4.3 addin 加载自己的 uic(推荐,不碰标准清单)

在 `Start()` 里:`commandBarManager.AddUICustomizationFile("MyAddin.uic", "MyNamespace")`;uic 与 DLL 同放 exe 目录(AttributeBrowserAddin 即此做法,其 uic 还演示了 `CommandBars` 自带工具栏停靠配置)。

---

## 5. PML ↔ .NET 互操作(PMLNet 桥)

### 5.1 .NET 侧(`Samples\PMLNetExample\PMLNetExample.cs` 原文范式)

```csharp
using Aveva.PDMS.PMLNet;

[PMLNetCallable()]
public class PMLNetExample
{
    [PMLNetCallable()] public event PMLNetDelegate.PMLNetEventHandler PMLNetExampleEvent;
    [PMLNetCallable()] public PMLNetExample() { }
    [PMLNetCallable()] public void Assign(PMLNetExample that) { }  // PML 赋值语义要求,必写
    [PMLNetCallable()] public void Method() { ... }
}
```

- 只有标了 `[PMLNetCallable]` 的类/构造/方法/事件才能被 PML 调用。
- **`Assign(that)` 是 PML 对象赋值语义的实现,必须有**(参考 PML 深拷贝语义)。

### 5.2 PML 侧调用(本树 174 个文件实证,摘要)

```pml
import 'PMLNetUtilities'          -- 或任何含可调用类的程序集名
  handle(1000,0)                  -- 已导入则吞掉
  endhandle
using namespace 'Aveva.Pdms.Presentation'
!ctrl = object NETGRIDCONTROL()
!ctrl.bindToDataSource(object NETDATASOURCE('Areas', !heads, !rows, '^Name'))
!this.netFrame.control = !ctrl.handle()     -- .NET 控件嵌入 PML 表单 container
```

反向:在 PML 里执行框架命令 `object PMLNetCommandManager().executeCommand('AVEVA.Attributes.Show')`。

> 开发 .NET 控件给 PML 用时:PML 表单定义 `container ... pmlNetControl`,成员声明为 .NET 类型(`member .x is NETGRIDCONTROL`),用 `addEventHandler('事件', !this, 'pml方法')` 回接 PML 方法。完整范式:`PMLLIB\aba\forms\abaarea.pmlfrm`。

---

## 6. marAPI(Marine 专属 .NET API 层)

> **API 全表与调用姿势查《AVEVA-Marine-marAPI调用姿势表.md》**(反射 + 130+ 处 PML 实证);签名级查证用 `PML语料\marapi_reflection.txt`。

- 程序集:`marAPI.dll`(1.8MB,SP4 刷新,**C++/CLI 混合程序集**)、`MarWrapper.dll`、`Aveva.Marine.*.dll` 系列;PML 侧 `import 'marapi'` 即桥到这些命名空间。
- PML 实证用到的类(全表见 PML 技能文档第 4.2 节):`AVEVA.Marine.UI.MARUI`(图面点取)、`AVEVA.Marine.Drafting.MARDRAFTING`、`AVEVA.Marine.Geometry.*`、`Aveva.Marine.Utility.MarUtil`(`TBEnvironmentGet`)、`Aveva.Marine.DataExtraction.MARDEX`、`AVEVA.Marine.Design.MARHULLPAN`。
- **参考文档(本安装自带)**:

| 文档 | 内容 |
|---|---|
| `Documentation\NETmarAPI.chm`(1.4MB,2020) | marAPI .NET 参考(最新) |
| `Documentation\marAPI.chm`(452KB) | marAPI 参考(2013) |
| `Documentation\NETAveva.Marine.PlanarAPI.chm` | Planar API 参考 |
| `Documentation\marAPI.chm` + `vitesse_access.xls` | API 访问面清单 |

- 防猜协议(PML 规范 2.14)同样适用:.NET API 先 grep `Samples\` 与 PMLLIB 中真实用法,再查 NETmarAPI.chm,查不到标 `TODO-UNVERIFIED`。

---

## 7. 独立程序(不开 GUI 调 AVEVA 数据)

`Samples\ImportDXF\`(159 行)是官方模板:

- 引用:`Aveva.Pdms / Aveva.Pdms.Implementation / Aveva.Pdms.Standalone / Aveva.Pdms.Utilities / marAPI / MarEnv / PMLNet / StartUp`;x86;TargetFramework v3.5。
- 入口:

```csharp
PdmsApplication.Start(isGraphics, module, isBatch, isNoConsole, logFile);
// module: 91 = Marine Drafting,一般用 95(注释原文)
Aveva.Marine.Utility.Misc.Init(module);
MarDrafting().DwgDxfImport(...);
string sb = Aveva.Marine.Environment.Runtime.EnvVars.Instance().Get("SBDATA", ...);
```

适用:批量导入/导出、夜间作业、与外部系统集成(先起 PdmsApplication 再走 API)。

---

## 8. 调试与常见坑

- **调试**:VS 工程属性把启动外部程序指到目标模块 exe(如 `marodes.exe` / `des.exe`),或独立程序直接 F5;addin 场景也可"先启动模块 → 附加进程"。断点命中前提:DLL 与 PDB 为当前编译版本且已按第 3 节登记。
- 换 DLL 必须先退出加载它的模块(文件锁);模块是 marine.bat 参数起的多个 exe,别看错进程。
- `BadImageFormatException` = 位数不对(把 x64 编译目标改成 x86)。
- `FileLoadException/强名不符` = 引用版本与安装不一致(Specific Version 对准本安装)。
- addin `Start()` 里抛异常会导致该 addin 静默不加载——初始化代码自己 try/catch 并写日志(框架不弹窗)。
- uic 的 `CommandId` 与 Command `Key` 不一致时按钮无反应,不报错——部署后逐按钮冒烟。

---

## 9. 案例:ModelHoverInfoAddin(悬停显示信息工具,已部署验证)

本工具是"三步走部署"的活例证(反射实测):

- **注册**:`OutfittingAddins.xml` 尾部 `<string>ModelHoverInfoAddin</string>` → 由 **Outfitting 模块(marodes.exe)**加载;DLL 位于 exe 目录。
- **程序集**:x86、.NET 2.0(mscorlib v2.0.0.0)、Version 1.0.0.0、强名无(PublicKeyToken=null,自研非官方签名)。
- **引用**:`Aveva.ApplicationFramework 1.1.20.0`、`Aveva.ApplicationFramework.Presentation 108.8100.20.0`、`Aveva.Pdms.Database 12.1.0.0`、`ExplorerControl 12.1.4.0`、`Infragistics.Win.UltraWinTree 10.3`(依赖系统自带)、WinForms/Drawing。
- **类型清单**(反射):`ModelHoverInfo.HoverInfo / HoverLine / HoverSettings / InfoBuilder / Log / Diagnostics / ExplorerHook(+Binding) / ViewTooltipHook` ——通过挂钩 Explorer/3D 视图的 Tooltip 通道实现悬停显示。
- 启示:自研 addin 不签强名也能被加载(Addins.xml 按文件名发现);需要 UI 库直接引用安装自带的 Infragistics 版本。

---

## 10. 文档索引(本安装自带)

| 文档 | 用途 |
|---|---|
| `OH12.1.SP4\ApplicationFramework.xml` / `ApplicationFramework.Presentation.xml` | **框架 API 的官方 XML 注释文档**(VS 引用后智能提示直接可用) |
| `Documentation\Customisation_Guide.chm` / `SOFTCG.chm` | 定制总指南 |
| `Documentation\NETmarAPI.chm` / `marAPI.chm` / `NETAveva.Marine.PlanarAPI.chm` | Marine .NET API 参考 |
| `Documentation\Setup_Customisation.chm` | 环境变量/安装定制(11MB) |
| `Documentation\Toolkit_Concepts.chm` | 编程接口概念 |
| `Documentation\NetInterfaceReferenceFiles.zip` | .NET 接口参考文件包(2011) |
| `Samples\ReadMe.txt` | "VS2008 + 引用路径指向安装目录" |
| `Documentation\Vitesse.chm` / `Python.chm` | 第三轨 Vitesse Python(KCS API;入口 `Vitesse\Lib\Kcs*.py`,示例 `Vitesse\Examples\`,钩子 `_TBhook_*.py`) |
