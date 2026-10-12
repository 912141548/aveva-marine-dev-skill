# AVEVA Marine uic 定制语法与部署调试手册(实文实证)

> 来源(第 8 轮,2026-09-25):42 个根目录 .uic 节点类型普查 + 7 个代表文件全文/分区精读 + 13 个 *Customization.xml 全集。
> 定位:.NET addin 的 UI 挂接语法权威速查 + 从建工程到调试的实战手册。配合《AVEVA-Marine-NET开发技能.md》《AVEVA-Marine-NET-API用法Cookbook.md》。

---

## 1. uic 文件全语法

### 1.1 文件骨架(design.uic 实文,全部 16 个节点)

```xml
<?xml version="1.0" encoding="utf-8"?>
<UserInterfaceCustomization xmlns:xsi="..." xmlns:xsd="..." xmlns="www.aveva.com">
  <Version>1.0</Version>
  <Tools />                  <!-- 工具定义(全局池) -->
  <InstanceTools />          <!-- 实例化引用(工具放入具体容器) -->
  <CommandBars />            <!-- 工具条 -->
  <TaskPanes />              <!-- 任务面板 -->
  <ContextMenus />           <!-- 右键菜单(引用已定义工具) -->
  <AreaLeftTools /> <AreaRightTools /> <FooterTools />
  <NavigationMenuTools />    <!-- 左侧导航条 -->
  <QATTools />               <!-- 快速访问工具条 -->
  <ContextualTabGroups /> <TabToolbarTools /> <Tabs /> <MiniToolbarTools />
  <Namespace>资源命名空间</Namespace>   <!-- 尾部;ImageResourceId 的前缀 -->
</UserInterfaceCustomization>
```

最小合法 uic = 骨架 + 你的 Tools/CommandBars + Namespace(PBSAddin.uic 358 字节;AttributeBrowser.uic 即标准样板)。

### 1.2 工具类型(根目录 uic 实证全集)

| 类型 | 用途 | 关键子元素 |
|---|---|---|
| `ButtonTool` | 普通按钮 | Command/Image(Image 或 ImageResourceId)/Caption/Tooltip/DisplayStyle/Category |
| `StateButtonTool` | 状态按钮(勾选↔Command.Checked 双向绑定) | 同上 |
| `MenuTool` | 下拉子菜单 | `<Tools><Tool Name="子项名"/></Tools>` 嵌套引用 |
| `LabelTool` | 纯文本标签 | Caption/DisplayStyle(TextOnlyAlways) |
| `ControlContainerTool` | 宿主 .NET 控件 | `<Control>完整类型名</Control>`(如 Aveva.Pdms.Presentation.HistoryCombo) |
| `PopupControlContainerTool` | 弹出控件容器(带下拉列表的按钮) | Command + Control |

### 1.3 Command 四种形态(实文)

```xml
<!-- ① Instance + CommandId(= Command.Key,最常见,ConnMap.uic) -->
<Command><Type>Instance</Type><CommandId>AVEVA.ConnectionMap.Center</CommandId><Arguments /></Command>

<!-- ② Instance + Key(等价写法,HistoryToolbar.uic) -->
<Command><Type>Instance</Type><Key>Aveva.Pdms.Presentation.HistoryBackwardCommand</Key><Arguments /></Command>

<!-- ③ Class + 构造参数(泛型类命令,MarineDrafting.uic)——停靠窗开关的官方泛型命令 -->
<Command><Type>Class</Type><Key>DockedWindowStateCommand</Key>
         <Arguments><String>DesignExplorer</String></Arguments></Command>

<!-- ④ Macro(直接挂 PML,MarineDrafting.uic;Key 固定 Macro:GUID 由系统生成) -->
<Command><Type>Macro</Type><Macro>!!assyInit('MAIN')</Macro>
         <Key>Macro:44b598be-546e-4a7f-aa5e-fbe76476f04b</Key><Arguments /></Command>
<Command><Type>Macro</Type><Macro>show !!adpsteel</Macro>...</Command>
```

图标两种给法:`<ImageResourceId>资源名:图标.png</ImageResourceId>`(资源文件名 = Namespace 尾节点值,如 `History:BACKHISTORY` ↔ `<Namespace>HistoryAddin</Namespace>`…实际注册名以 AddUICustomizationFile/资源载入为准)或省略(显示 Caption 文本,HistoryToolbar 原话情形)。

### 1.4 CommandBar(工具条,HistoryToolbar.uic)

```xml
<CommandBars>
  <CommandBar Name="History">
    <Tools><Tool Name="Aveva.Pdms.HistoryLabel" /> ... </Tools>
    <DockedColumn>1</DockedColumn><DockedRow>1</DockedRow>
    <DockedPosition>Top</DockedPosition>
    <AllowFloating>true</AllowFloating><AllowHiding>true</AllowHiding>
    <FillEntireRow>false</FillEntireRow><ShowInToolbarList>true</ShowInToolbarList>
    <Caption>History</Caption><ApplicationContext />
  </CommandBar>
</CommandBars>
```

### 1.5 右键菜单 / 页签

- **ContextMenus** 只放引用:`<ContextMenus><Tool Name="连接图右键菜单名" /></ContextMenus>`;菜单本体是 Tools 里的 MenuTool/按钮组(ConnMap.uic:RMB 菜单各按钮即普通 ButtonTool/StateButtonTool)。
- **ContextualTabGroup + Tabs**(DiagramsDiagramViewerAddin.uic 实文):

```xml
<ContextualTabGroups>
  <ContextualTabGroup Name="Module.ContextualTabGroup_DiagramViewer"><Caption>Diagram Viewer</Caption></ContextualTabGroup>
</ContextualTabGroups>
<Tabs>
  <Tab Name="Module.DiagramViewer.Context.Tab">
    <Caption>Actions</Caption>
    <ContextualTabGroup><Item>Module.ContextualTabGroup_DiagramViewer</Item></ContextualTabGroup>
    <Groups>
      <Group Name="...DiagramGroup" ><Tools><Tool Name="...Open" LargeImage="True" /></Tools><Caption>Diagram</Caption></Group>
      ...
    </Groups>
  </Tab>
</Tabs>
```

### 1.6 插入既有菜单位置(InstanceTools 定位)

```xml
<InstanceTools>
  <Tool Name="Aveva.DwgExportAddin.DwgExport2"
        Parent="AVEVA.Diagrams.Menu.File.Export"
        AfterSibling="AVEVA.Diagrams.Button.FileExportDocument" />
</InstanceTools>
```
(`AfterSibling` 换 `BeforeSibling` 亦可——TODO-UNVERIFIED,本机未见 BeforeSibling 实例)

## 2. uic 的三种装载方式与对应表

1. **Customization.xml 登记**(模块级):`<CustomizationFile Name="名字" Path="xxx.uic"/>`;**`Path="$1.uic"` = 项目级定制**(项目目录可放同名 $1.uic 覆盖)。全 13 个 *Customization.xml 对应:Design/Outfitting→design.uic、Draft/OutfittingDraft→draft.uic、HullDesign/marinedrafting→AVEVA.Marine.UI.HullGeneral+HullDesign/MarineDrafting(+HullVNET)、Admin→admin.uic、Paragon→paragon.uic、Spooler→spooler.uic、Isodraft→isodraft.uic、Tags→Tags.uic+Viewer3DAddIn.uic、Diagrams/SMM 多文件。**注意 Outfitting 用的是 design.uic**(与 Design 共享模块层)。
2. **addin 程序化挂载**:`commandBarManager.AddUICustomizationFile("Xxx.uic", "Namespace")`(AttributeBrowserAddin;Diagrams 系用 `CommandBarManager.Instance.AddUICustomizationFile(路径, 名)`)——自研 addin 推荐,不碰标准清单。
3. **相对路径**:登记 Path 可写 `AddinsData\Diagrams\DiagramsDWGExportAddin.uic`(DiagramsCustomization.xml 实例),addin 文件挪子目录免污染主目录。
4. **交互式 Customise 对话框**(TM-1402 ch5):运行中右键图形窗栏 → Customisation,可建 Macro 按钮/Core Command 按钮/命令条/菜单并拖放编排——本质是写运行时定制存储(SettingsManager 持久化,位置 `Local Settings\Application Data\Aveva\<应用名>`,见框架 XML 文档 SettingsManager.Directory);发布级定制仍应走 uic 文件。

## 3. 部署调试实战手册

### 3.1 工程设置(一次配对)

1. C# 类库;**平台 x86**;目标框架 **.NET Framework 2.0~3.5**(不要 4.x);引用 HintPath 全部指向 `%PDMSEXE%` 下程序集:`Aveva.ApplicationFramework`、`Aveva.ApplicationFramework.Presentation`、`Aveva.Pdms.Database/Shared/Utilities`(按需 + Infragistics 10.3/DevExpress 10.2,**设 Copy Local=false**,版本跟随安装)。
2. ReadMe 原话:VS2008 时代工程;新 VS 打开注意不要被升级到 4.x。
3. 调试页:启动外部程序 = 目标模块 exe(Outfitting→`marodes.exe`,Design→`des.exe`);工作目录 = `%PDMSEXE%`。

### 3.2 部署三步(重申)+ 发布迭代

DLL→exe 目录;`<应用名>Addins.xml` 加 `<string>程序集名</string>`;重启模块。**迭代时先退出模块再覆盖 DLL**(进程锁定);日常调试可写 xcopy 后处理(生成事件),但替换仍需模块已退出。

### 3.3 调试手段

- **F5 直启**:工程启动外部程序设为模块 exe,断点在 IAddin.Start 即命中(启动即加载)。
- **附加进程**:模块已开时 `devenv 附加到 marodes.exe`(x86 进程,注意选对会话)。
- **独立程序**直接 F5(PdmsApplication.Start 路径,见 Cookbook §13)。
- `Aveva.ApplicationFramework.Diagnostics.WriteModules()` / `ElapseTimer` 打性能与模块清单;`LogViewer.LogMessage` 自建日志窗。

### 3.4 排错树(按症状)

| 症状 | 检查顺序 |
|---|---|
| addin 完全没加载(断点不中) | ① Addins.xml 里 `<string>` 是否=程序集名(不带 .dll)、文件名大小写(marinedraftingaddins.xml 全小写) ② DLL 是否在 exe 目录(或 Addins.xml 写相对路径) ③ 位数(x64 编译会静默失败/加载器报错) ④ .NET 版本(4.x 专有 API 会崩) ⑤ Start() 里抛异常——**框架不弹窗,自己 try/catch 写日志** |
| addin 加载了但按钮无反应 | uic 的 `CommandId/Key` ≠ Command 的 `Key`(逐字符核);Macro 型查 PML 函数是否存在(uic 挂 `show !!form` 也行);**部署后逐按钮冒烟**(uic 错误不报错只失灵) |
| 按钮出现但图标空 | ImageResourceId 的资源名:Namespace 未对 / 资源文件没随 DLL 放 / 用 ResourceManager.LoadResourceFile 载入没做 |
| 停靠窗没出现 | CreateDockedWindow 后没 `.Show()`(或 StateButtonTool 未勾选);`SaveLayout=true` 时上次布局记住了隐藏态 |
| 强名/版本 FileLoadException | 引用 Specific Version 与本安装不一致(升级 SP 后重编译) |
| 换 DLL 无效 | 旧进程还在跑(退出模块再覆盖);或 Addins.xml 改了但没重启 |

### 3.5 ModelHoverInfoAddin 案例复盘(活样板)

- 注册:OutfittingAddins.xml `<string>ModelHoverInfoAddin</string>`,DLL 在 exe 目录 → **Outfitting(marodes.exe)启动即加载**。
- 反射事实:x86 / .NET 2.0 / 引用 ApplicationFramework 1.1.20 + Presentation 108.8100.20 + Aveva.Pdms.Database 12.1 + **ExplorerControl 12.1.4**(Explorer 树控件)+ Infragistics 10.3;类型 `HoverInfo/HoverLine/HoverSettings/InfoBuilder/Log/Diagnostics/ExplorerHook/ViewTooltipHook`——挂 Explorer/视图 Tooltip 通道实现悬停信息。
- 复盘要点:①自研不签强名也能加载(Addins.xml 按文件名发现)②引用安装自带 UI 库版本是对的 ③没有 uic 也合法(纯事件钩子型 addin 不需要按钮)——**uic 只在要挂按钮/菜单/工具条时才需要**。

### 3.6 发布前检查清单

- [ ] x86 + 目标框架 ≤3.5 + Copy Local=false 的 AVEVA 引用
- [ ] DLL+uic(如需)在 exe 目录(或登记相对路径)
- [ ] 对应模块 Addins.xml 已登记;改名后旧条目已删
- [ ] 每个 CommandId/Key 与代码逐一核对;每按钮点一遍
- [ ] 退出模块→覆盖 DLL→重启 的迭代流程跑通一次
- [ ] 版本号/程序集名与 Addins.xml、帮助文档一致
