# 端到端示例:Outfitting .NET 停靠窗 Addin(从零到调试)

> 第 23 轮:第二个可复制模板——CE 属性停靠浏览器(与官方 AttributeBrowserAddin 同构,代码取自 `Samples\Samples\AttributeBrowserAddin\` 实证,零编造)。
> 前置阅读:NET 技能文档、Cookbook、uic 手册。PML 版需求先看《AVEVA-Marine端到端示例-收集导出工具.md》Step 1 的选型表。

---

## 1. 工程设置(一次配对,→ NET 技能 §3.1/§8)

```
MyBrowser.csproj(C# 类库)
  PlatformTarget: x86            ← 64 位直接加载失败
  TargetFramework: .NET Framework 3.5
  引用(HintPath 全部指向 %PDMSEXE%,Copy Local=false):
    Aveva.ApplicationFramework            (v1.1.x)
    Aveva.ApplicationFramework.Presentation
    Aveva.Pdms.Database / Aveva.Pdms.Shared / Aveva.Pdms.Utilities(按需)
  调试页:启动外部程序 = C:\AVEVA\Marine\OH12.1.SP4\marodes.exe;工作目录 = 同目录
```

## 2. 三个类(完整代码)

### 2.1 MyBrowserAddin.cs —— IAddin 入口

```csharp
using System;
using Aveva.ApplicationFramework;
using Aveva.ApplicationFramework.Presentation;
using Aveva.Pdms.Shared;
using Aveva.Pdms.Database;

namespace MyCompany.MyBrowser
{
    public class MyBrowserAddin : IAddin
    {
        private DockedWindow _window;
        private AttributeListControl _control;

        public string Name { get { return "MyBrowserAddin"; } }
        public string Description { get { return "CE attribute docked browser"; } }

        public void Start(ServiceManager serviceManager)
        {
            try
            {
                // 1. 停靠窗(内容=普通 WinForms 控件)
                WindowManager wm = (WindowManager)serviceManager.GetService(typeof(WindowManager));
                _control = new AttributeListControl();
                _window = wm.CreateDockedWindow("MyCompany.MyBrowser.List",
                                                "My Attributes", _control, DockedPosition.Right);
                _window.Width = 260;
                _window.SaveLayout = true;                 // 布局跨会话记忆

                // 2. 命令(状态按钮)
                CommandManager cm = (CommandManager)serviceManager.GetService(typeof(CommandManager));
                cm.Commands.Add(new ShowBrowserCommand(_window));

                // 3. CE 变化 → 刷新
                CurrentElement.CurrentElementChanged += OnCurrentElementChanged;

                // 4. 图标资源(同名 .resources 随 DLL)
                ResourceManager rm = (ResourceManager)serviceManager.GetService(typeof(ResourceManager));
                rm.LoadResourceFile("MyBrowserAddin");

                // 5. uic 挂载
                CommandBarManager cbm = (CommandBarManager)serviceManager.GetService(typeof(CommandBarManager));
                cbm.AddUICustomizationFile("MyBrowser.uic", "MyBrowser");
            }
            catch (Exception ex)
            {
                // Start() 抛异常 addin 会静默不加载——自己兜住写日志
                System.IO.File.WriteAllText(@"C:\mydev\mybrowser_start_err.txt", ex.ToString());
            }
        }

        public void Stop() { }

        private void OnCurrentElementChanged(object sender, CurrentElementChangedEventArgs e)
        {
            if (_window == null) return;
            _window.Title = "Attr: " + CurrentElement.Element.GetAsString(DbAttributeInstance.FLNM);
            _control.Clear();
            foreach (DbAttribute att in CurrentElement.Element.GetAttributes())
                _control.AddAttribute(att.Name, CurrentElement.Element.GetAsString(att));
        }
    }
}
```

### 2.2 ShowBrowserCommand.cs —— 状态按钮命令(与窗可见性双向同步)

```csharp
using System;
using Aveva.ApplicationFramework.Presentation;

namespace MyCompany.MyBrowser
{
    public class ShowBrowserCommand : Command
    {
        private readonly DockedWindow _window;
        public ShowBrowserCommand(DockedWindow window)
        {
            Key = "MyCompany.MyBrowser.Show";          // ← uic 的 CommandId 必须一致
            _window = window;
            _window.Closed += delegate { Checked = false; };                        // 窗关→按钮弹起
            WindowManager.Instance.WindowLayoutLoaded += delegate { Checked = _window.Visible; }; // 布局载入→同步
        }
        public override void Execute()
        {
            if (Checked) _window.Show(); else _window.Hide();
        }
    }
}
```

### 2.3 AttributeListControl.cs —— 普通 WinForms UserControl

ListView(Dock=Fill,Details,两列 Attribute/Value)+ 两个方法:

```csharp
public void AddAttribute(string name, string value)
{ var it = new ListViewItem(name); it.SubItems.Add(value); listView1.Items.Add(it); }
public void Clear() { listView1.Items.Clear(); }
```

## 3. MyBrowser.uic(完整,→ uic 手册 §1.2/§1.4)

```xml
<?xml version="1.0" encoding="utf-8"?>
<UserInterfaceCustomization xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
                            xmlns:xsd="http://www.w3.org/2001/XMLSchema" xmlns="www.aveva.com">
  <Version>1.0</Version>
  <Tools>
    <StateButtonTool Name="MyCompany.MyBrowser.Show">
      <Command><Type>Instance</Type><CommandId>MyCompany.MyBrowser.Show</CommandId><Arguments /></Command>
      <Caption>My Browser</Caption>
    </StateButtonTool>
  </Tools>
  <InstanceTools />
  <CommandBars>
    <CommandBar Name="MyBrowser">
      <Tools><Tool Name="MyCompany.MyBrowser.Show" /></Tools>
      <DockedColumn>1</DockedColumn><DockedRow>1</DockedRow>
      <DockedPosition>Top</DockedPosition>
      <AllowFloating>true</AllowFloating><AllowHiding>true</AllowHiding>
      <FillEntireRow>false</FillEntireRow><ShowInToolbarList>true</ShowInToolbarList>
      <Caption>My Browser</Caption>
    </CommandBar>
  </CommandBars>
  <TaskPanes /><ContextMenus />
  <Namespace>MyBrowserAddin</Namespace>
</UserInterfaceCustomization>
```

## 4. 部署三步(→ NET 技能 §3)

1. `MyBrowserAddin.dll` + `MyBrowser.uic` + `MyBrowserAddin.resources`(若有图标)→ `%PDMSEXE%\`
2. `OutfittingAddins.xml` 加 `<string>MyBrowserAddin</string>`(Outfitting→marodes.exe;Design 则改 DesignAddins.xml)
3. 重启 Outfitting → 工具条出现"My Browser"状态按钮

## 5. 调试(→ uic 手册 §3.3)

- **F5**:csproj 启动外部程序=marodes.exe,断点打在 `Start()` 首行(启动即命中)
- **附加进程**:模块已开时附加 marodes.exe(x86)
- 启动错误已自写 `C:\mydev\mybrowser_start_err.txt`(Step 2.1 的 try/catch)

## 6. 排错对照(症状→检查,→ uic 手册 §3.4)

| 症状 | 查 |
|---|---|
| 断点不中/addin 没加载 | Addins.xml 条目=程序集名?DLL 在 exe 目录?x86?Start 内异常(看自写日志) |
| 按钮=文本无图标 | resources 没随 DLL/ImageResourceId 资源名错 |
| 按钮无反应 | uic CommandId ≠ Command.Key(逐字符) |
| 窗不出现 | SaveLayout 记住了隐藏态;或 StateButtonTool 没勾 |
| FileLoadException | 引用版本与安装不一致,重编译 |

## 7. PML 互操作扩展(→ Cookbook §11/§12)

- 窗里想嵌 Explorer 树:构造 `new ExplorerCtrl(DbType.Design, null)`(TM-1402 §2.9 范式)
- 想被 PML 调:类标 `[PMLNetCallable]` + `Assign` + PML 侧 `import 'MyBrowserAddin'` / `using namespace` / `object MyBrowserXxx()`
- 想发事件给 PML:`public event PMLNetDelegate.PMLNetEventHandler OnXxx;` → PML `!h = !ctrl.addeventhandler('OnXxx', !this, 'cb')`(返回句柄可 removeeventhandler)

## 8. 发布前清单

- [ ] x86 + ≤3.5 + Copy Local=false
- [ ] DLL+uic+resources 三件齐;Addins.xml 已登记旧条目清理
- [ ] CommandId/Key 逐字符一致;按钮点一遍(勾选↔窗显隐双向)
- [ ] CE 切换时列表刷新正确;CE 为 World/无效元素时不崩
- [ ] 退出模块→覆盖 DLL→重启流程通过
