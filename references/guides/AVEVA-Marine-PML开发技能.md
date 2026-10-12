# AVEVA Marine 12.1 PML 开发技能(环境·源码组织·部署实证版)

> 定位:与本项目已有三份文件配套使用——
> ①《PML生成规范的冲突文件 2026-09-08….md》(下称**生成规范**)②《PML审核规范.md》(下称**审核规范**)③《PML记忆-语法硬约束….md》(下称**记忆**)。
> **语法怎么写看那三份;本文回答:环境怎么搭、源码树长什么样、Marine 特有什么写法、代码放哪里、部署怎么走。**
> 表单/gadget 语法另有权威速查:**《Marine-PML表单语法精要.md》**(Guide ch13-20 实证,setup form 体系,Marine 1380 个表单所用语法)——写表单前先查它。
> 对象方法签名查证:**《Marine-PML对象API字典精要.md》**(Reference Manual §2.5 实证,高频 46 类全方法 + 75 节行号目录)。
> 错误处理查:**《Marine-PML错误码速查.md》**(330 码+模块号对照);任务级写法查:**《Marine-PML任务写法速查.md》**(34 任务官方频次与样例)。
> 实证基线:`E:\AVEVA\Marine\OH12.1.SP4`(AVEVA Marine 12.1 SP4,Hull & Outfitting 安装目录),2026-09-25 勘察,全部结论有文件/统计证据。

---

## 1. 产品布局与启动链

### 1.1 目录布局

| 路径 | 内容 |
|---|---|
| `OH12.1.SP4\`(exe 目录 = `%pdmsexe%`) | 全部 exe、AVEVA DLL、`*Addins.xml`、`*.uic`、PMLNet.dll 等 |
| `OH12.1.SP4\PMLLIB\` | **PML2 源码树**(6071 个 .pmlfnc/.pmlfrm/.pmlobj) |
| `OH12.1.SP4\PDMSUI\` | PML1 界面宏树(9704 文件,绝大多数无扩展名) |
| `OH12.1.SP4\Documentation\` | 全部 CHM 帮助 + 示例 txt + `pmlscan.exe` 等说明 |
| `OH12.1.SP4\Samples\` | .NET addin 官方范例(见 .NET 技能文档) |
| `OH12.1.SP4\Vitesse\` | Python(KCS API)脚本树(船体/制图第三轨) |
| `E:\AVEVA\Marine\Projects12.1.SP4\` | 项目(`Mas`=Master 通用项目、`Mar`=Marine 项目,各有 evars*.bat) |
| `E:\AVEVA\Marine\Data12.1.SP4\` | `pdmsuser`/`pdmswk`/`DFLTS` 等用户数据 |

### 1.2 启动链(marine.bat → evars.bat 实文)

```
marine.bat  设 AVEVA_MARINE=YES / MARINE=YES / pdms_installed_dir=%~dp0
   → call evars.bat  设全部环境变量(pythonpath 指向 Vitesse 四目录)
      → call %projects_dir%Mas\evarsMaster.bat / Mar\evarsMarine.bat(项目级变量)
         → 启动模块 exe(缺省 mon.exe)
```

**模块参数 → exe 映射**(marine.bat 实文,决定 addin 挂到哪个 Addins.xml):

| marine.bat 参数 | exe | 对应 Addins.xml |
|---|---|---|
| Admin | adm.exe | AdminAddins.xml |
| Lexicon | lex.exe | LexiconAddins.xml |
| Paragon | des.exe -module=81 | ParagonAddins.xml |
| Propcon | des.exe -module=27 | DesignAddins.xml |
| Spooler | des.exe -module=83 | SpoolerAddins.xml |
| (Design 缺省) | des.exe | DesignAddins.xml |
| IsoDraft | iss.exe | IsodraftAddins.xml |
| HullDesign | marhdes.exe | HullDesignAddins.xml |
| MarineDrafting | mardra.exe | marinedraftingaddins.xml(全小写文件名!) |
| Outfitting | marodes.exe | OutfittingAddins.xml |
| OutfittingDraft | marodra.exe | OutfittingDraftAddins.xml |
| Monitor(缺省) | mon.exe | — |

### 1.3 关键环境变量(evars.bat 实文)

- `pdmsexe`、`pmllib`(缺省 `%pdmsexe%pmllib\`)、`pdmsui`(缺省 `%pdmsexe%pdmsui\`)、`pdmsuser`、`pdmswk`、`pdmsdflts`、`pdmshelpdir=%pdmsexe%Documentation\`、`projects_dir`、`plotcadc`、`pythonpath=%pdmsexe%Vitesse;%pdmsexe%Vitesse\Basic_Design;%pdmsexe%Vitesse\Lib;%pdmsexe%python`
- 脚本末尾会把所有路径变量统一规范成**带尾斜杠**形式;自定义覆盖时要保持此格式。
- 查询:PDMS 命令行 `q evar pmllib`(部署验证第一动作)。

---

## 2. PMLLIB 源码树组织

### 2.1 结构规律

- 顶层 34 个模块目录 + `pml.index`;**每模块固定分 `forms / functions / objects` 三个子目录**。
- 复合模块再按应用域分层:`mds\{common,design,draft,paragon}\{forms,functions,objects}`、`pipefabricationmanager\{common,design,draft,spooler}`、`assembly` 另有 `tasks/templates/data/userfunctions`、`vnet` 另有 `settings`。
- 图标集中在各模块 `icons\`(全树 1372 个 .png)。

### 2.2 文件统计(2026-09-25 `dir /s` 实测)

| 类型 | 数量 | 类型 | 数量 |
|---|---|---|---|
| .pmlfnc | 3703 | .pmlobj | 988 |
| .pmlfrm | 1380 | .pmlmac/.mac | 3 / 1 |
| .png | 1372 | 目录 | 190 |

模块规模排序(前几名):mds 2504、common 763、pipefabricationmanager 128、assembly 91、accommodation 83、spooler 80、vnet 47;Marine 特有模块:hulldesign 28、marinedrafting 31、avevamarine 5、PBS 10、smm 6。

### 2.3 pml.index

7643 行,格式 = **目录行(`\模块\子目录\`)后跟该目录下全部文件名清单**。是 PML 装载机制的文件清单索引(配合安装根的 `pmlscan.exe` 工具)。新建文件后 `pml rehash` 重建的就是这类索引。

### 2.4 PDMSUI 树(PML1 遗留界面宏)

- 20 个目录:`adm cat clib data des diagrams DRA hdes icons intf iso lex mdra mon opsys plots reports smm spl tags`。
- `des\pipe` 等用单字母前缀命名:`f*`(表单)/`i*`(init)/`m*`(菜单宏)/`u*`(实用);`admin` 下固定 `binload/macload/start/vars` 四个启动宏。
- `DRA` 下 Marine 专属库:`libmaba libmdrl libmgen libmiso libmlab libmrep libmshe libmsty libmsym libmtag` + `adpcore adpgdp adpsched adptag`。
- 定位:PML1 宏 + PML2 混写的界面层;**新定制一律放 PMLLIB(PML2),不动 PDMSUI**。

---

## 3. Marine 实证代码范式(对生成规范的补充)

生成规范/记忆的语法规则全部适用(见第 6 节核对),以下是本树新增的实证细节:

### 3.1 文件头(带版权行)

```
------------------------------------------------------------------------
--
-- Copyright 1974 to current year. AVEVA Solutions Limited and its subsidiaries. All rights reserved in original code only.
--
-- File:            appmarmain.pmlfrm
--   Type:          Form Definition
--   Module:        marine modules
--   Author:        ...
--   Created:       ...
-- Description:     Main form for Marine modules
------------------------------------------------------------------------
-- Methods defined: ...
```

### 3.2 handle 的实际用法(本树 4 种)

1. `handle ANY ... endhandle` — 兜底(init/可忽略处)。
2. **`handle (1000,0) ... endhandle` — .NET / `import` 抛错的通用捕获码**(Marine 树惯用,记忆文件未载,建议并入)。
3. `handle (2,109) ... endhandle` — DB 命令特定错误码(`new GBLOCK` 等)。
4. `onerror continue` + 循环 — 旧宏风格(avevamarine 函数),**新代码禁用**(与审核规范 ERR 类一致)。

### 3.3 惯用法

- 无效 DBREF 返回:`return =0/0`(`hullNewBlock.pmlfnc`)。
- 表单主流仍是 `setup form !!name ... exit`(1368/1380;`layout form` 仅 27)——印证记忆第 6 章#1 裁决:PDMS 系产品沿用 `setup form`。主表单常见修饰 `at xr 0 yr 0 main VarChars`。
- 主表单套路(`hulldesign\forms\appmarmain.pmlfrm`):`quitcall = |CALLIB XEXIT|`;工具条按钮 `callback |GETWORK|`、`callback |CALLIB ILIST $$_list|`(CALLIB/GETWORK 是 Marine 核心回调命令);构造器里 `!this.initcall = '!this.initialise()'` + `!this.newMenu('sysView')` + `!menu.add('CALLBACK'/'CORECALLBACK'/'TOGGLE', 文本, 回调串, 字段名)`。
- 最简表单(`marinedrafting\forms\mdradim.pmlfrm`)三行:button + `call |!!dimcreate(2)|`。
- 对象构造器方法名 = 类名**小写**(`define object PHULLNOTCH` ↔ `define method .phullnotch(...)`)。

### 3.4 应用/菜单注册:PML Add-in 机制(官方标准入口注入)

每个 AVEVA 应用本身就是 PML add-in(Guide ch23)。给标准模块注入自己的菜单/工具条/表单行为,官方姿势是**三件套**,全部零改动标准文件:

**(1) addin 定义文件**:`%PDMSUI%\<module>\DFLTS\ADDINS\<addin>`(如 `DES\DFLTS\ADDINS\MYADDIN`),key:value 格式:

```
Name: MYADDIN                      ← 必填
Object: APPMYADDIN                 ← addin 对象类型(PMLLIB 里的 pmlobj)
StartupModify: PIPE:!!myPipeStartupCall()   ← 给既有应用挂启动回调(可选)
SwitchModify:  PIPE:!!myPipeSwitchCall()    ← 切换回调(可选)
```

其他键:`Title/ShowOnMenu/ModuleStartup/Menu/Directory/Group/Type(DRA|DIM|LAB|USR1-5)/StartupCall/SwitchCall`。装载入口 `!!appReadAppDefns(!module)` 建 `!!appCntrl`。

**(2) addin 对象**(放 PMLLIB,`define object APPMYADDIN`)三钩子,缺哪个都不报错:
- `.modifyMenus()` —— 模块启动时建菜单(用 APPMENU);
- `.modifyForm()` —— 主表单构建期加工具条(frame .名 toolbar;主表单 Design=`!!appDesMain`,Draft=`!!appDraMain`);
- `.initialiseForm()` —— 切到本应用时(仅应用级 addin)。

**(3) APPMENU/APPTBARCNTRL/APPFORMCNTRL 对象**:

```pml
define method .modifyMenus()
  !menu = object APPMENU('sysQry')                       -- 挂到主表单的 sysQry 菜单
  !menu.add('CALLBACK', 'Query Owner', 'q owner', 'QueryOwner')   -- 加字段(同名字段自动去重→幂等)
  !menu.insertAfter('CE', 'CALLBACK', 'CE', '!!customDelete()', 'customDelete')  -- 替换既有字段:先 remove 再插
  !!appMenuCntrl.addMenu(!menu, 'PIPE')                  -- 注册到 PIPE 应用可见;'ALL'=全部应用
endmethod
```

- 工具条:`!!appTbarCntrl.addToolbar(名, 应用名|数组|'ALL', 缺省可见)`;`hideGadgets/deactivateGadgets` 按应用显隐/置灰;未注册工具条自动隐藏。
- 表单跨会话:`!!appFormCntrl.registerForm(!form, visibleInApps, requiredApps, showOnStartup, showOnSwitch)`;表单实现 `.saveData() is ARRAY` 存状态,下次 `!!appFormCntrl.getFormData(!form)` 取回(首次为空数组必须兜住)。
- **CORECALLBACK 菜单字段类型**(附录 A):PML 定义字段、回调由 .NET addin/核心代码接管(按字段名订阅 'menu field created' 事件)——这是 PML 菜单与 .NET addin 的对接点,`appmarmain.pmlfrm` 的 `'CORECALLBACK','Print Graphics...','','V_PRNG'` 即此类。
- 替换标准按钮回调(零改标准文件):`!!appDesMain.mtbDeleteCe.callback = '!!customDelete()'` 写在 `.modifyForm()` 里。

此前发现的 `appdesavevamarine.pmlobj`(§3.4 开头)就是这套机制的 Marine 实例——对照定义文件与三钩子阅读。

### 3.5 开发调试工具箱与可撤销改库(PDMS 12 Guide ch8-12/14 实证,成品代码禁留调试命令)

**调试**(细节见学习报告第 2 轮):`PML TRACE ON/OFF` 或 `$R100/$R0`(`$HR` 帮助);`$P` 输出;`alpha log /文件 [OVERWRITE|APPEND]` … `alpha log END` 命令日志(`$R102` 把跟踪并入日志);`$M-` 挂起 / `$M+` 恢复(**只对宏有效,函数/方法不可**);`$QM` 查文件调用栈;`q var LOCAL` / `q var GLOBAL` 查全部变量;`$Q` 查下一合法命令词。错误内省:`!!Error.Text/.Command/.Line` + `do !l VALUES !!Error.Callstack`;自造错误 `return error 1 '消息'` 配 `handle 1`。

**索引指令补全**:新文件用 `pml rehash`;**他人加了文件用 `pml index`(只重读 pml.index 不重建)**;离线更新用 `pmlscan <目录>`(exe 工具);顽固不生效就 `kill !!form` + `pml reload form`。
【产品差异】本版 Guide 说 rehash 扫 PMLLIB **全部**目录,E3D 3.1 手册说只扫**第一个**目录——Marine 12.1 以本版 Guide 为准,但自动化脚本统一加等待。

**可撤销改库(官方机制)**:
- 命令式:`MARKDB '描述'` → 改库 → `ENDMARKDB`(在主工具条 Undo/Redo 栈上打标记)。
- 回调级:`member !okUndo is UNDOABLE` → `.description()/.undoAction('PML串')/.redoAction('PML串')` → `!this.setUndoable('OKcall', !okUndo)` 或 `!this.btn.setUndoable(!undo)`——用户改库后可直接点主工具条 Undo/Redo。

**文本保真**:F&M 程序里 `VAR !x ...` 缺省会去掉换行、压缩连续空格,要原始文本必须 `VAR !x RAW ...`;多栏排版用 `VAR !tab COMPOSE |$!a| WIDTH 11 C |$!b| WIDTH 15 R`。
【编码强制】源文件三选一(优先级):UTF8+BOM > UTF16/32+BOM > ASCII 7bit;外部文本缺省按 UTF8+BOM 读、无 BOM 按 `CADC_LANG` 环境变量(缺省 LATIN1),新文件按 `CADC_LANG_NEW`(缺省 UTF8+BOM,支持 CP936 GBK 等);转码工具 `transc.exe`(`!!pmlTranscFile` 已封装)。

**Open Callback(一法管全表单)**:回调串只写左括号 `callback '!this.Control('`,方法签名固定 `define method .Control(!object is FormsAndMenusObject, !action is STRING)`;体内按 `!action`(SELECT/UNSELECT/MODIFIED/VALIDATE…)分支,用 `!object.owner()/.type()/.name()/.PickedField` 反查事件控件——官方推荐的复杂表单回调组织方式(省去每控件一方法)。

### 3.6 增补:防猜快查/类版本陷阱/EDG(TM-1401/1402 实证,学习报告第 5 轮)

- **`q methods !netObj`**:命令行列出任何 .NET/PML 对象的全部可调方法(带签名)——**防猜第一工具**;`q var !obj` 看命名空间+类名。
- **(1000,x) 错误码来源**:C# 侧 `throw new PMLNetException(1000, 1, "文本")` → PML `handle (1000,1)`;桥层模块号 = 1000。
- **类版本一致性陷阱**:变量指向加载时的类定义版本;`pml object reload` 后旧变量与新实例做 `eq/ne` 会报错——`!var.delete()` 后重建。命令变体:`pml object reload OBJECT名 / FORM名`。
- **EDG 事件驱动图形**(3D 拾取的标准姿势,取代 `ID@`):`object EDGPACKET()` → `.elementPick('提示 <esc> 结束')` → `.action = |!!form.cb(!this.return[1])|` → `.close = |...|` → `.description='名'` → `!!EDGCntrl.add(!packet)`;移除 `!!edgCntrl.remove('名')`;高亮用 `!!gphDrawlists.drawlists[1].highlight(!pick, 314)`;表单内 VOLUME 视图拾取先 `!!EDGCntrl.addView()` 注册。
- **追查与发布**:`$r109 /c:\log.log` 全量动作落文件(`$r110` 进窗口,`$r` 关闭);`UndoDB/RedoDB` 回退到最后 MarkDB/Savework;`pmlencrypt.exe` 发布加密(不可逆,留参考副本)。

### 3.7 FMSYS 系统方法(长任务/视图检查,Guide ch22 实证)

```pml
!!FMSYS.setInterrupt(!!fmstop.stopButton)      -- 循环前先设"停止"按钮(按钮来自一个两行小表单)
do !next from 1 to 50
  ...
  !!FMSYS.setProgress(!percent)                -- 循环内报进度(会处理 UI 事件)
  if ( !!FMSYS.Interrupt() ) then              -- 查中断(手册示例错拼 Interruppt,实际 Interrupt)
    return error 1 'Processing aborted'
  endif
enddo
!!FMSYS.setProgress(0)                         -- 结束复位
```

其他常用:`!!FMSYS.OKCurfnView('g2d'|'g3d'|'ANY'[,'subtype'])` 光标函数前置检查(无合适视图会抛 (61,115),用户退出是 (61,528));`!!FMSYS.currentDocument()` / `!!FMSYS.loadForm('名')` is FORM;`!!FMSYS.setDefaultFormLayout('VarChars')` 测旧表单两模式差异;`!!FMSYS.checkRefs(true)` 跳过表单引用检查提性能;`!!FMSYS.refresh()` 刷全部视图;`!!FMSYS.setDefaultFormat(!!fmt)` 全局缺省格式**只能调一次**。Alert 细节:全部阻塞;第 2/3 参定位(0.25,0.1);`!!Alert.Input` 是 `VAR !x READ` 的 GUI 等价,慎用;视图 gadget 有 `.saveview(n)/.restoreview(n)`(n=1..4)。

---

## 4. Marine 特有:PML 直调 .NET(import / using namespace / marAPI)

### 4.1 import 惯用法(全树 329 个文件使用)

```pml
import 'marapi'
  handle(1000,0)
    -- This error means that marapi has already been imported, ignore.
  endhandle
using namespace 'Aveva.Marine.Design'
!runObject = object MARHULLPAN()
!runObject.stmtExec(0, !statement)
```

要点:`import '程序集名'`(不带 .dll,在 exe 目录解析);**重复 import 会报错,惯用 `handle(1000,0)` 吞掉**;`using namespace` 后 `object 类名()` 实例化。

### 4.2 PML 实证用到的 marAPI 类

| 命名空间 | 类 | 实证用法 |
|---|---|---|
| AVEVA.Marine.UI | MARUI | `!mUi.PointPlanarReqPML('Indicate component', !point)` 图面点取 |
| AVEVA.Marine.Drafting | MARDRAFTING | `ComponentIdentify(!point)`、`ElementDbrefGet(!handle)` |
| AVEVA.Marine.Geometry | MARPOINTPLANAR / MarElementHandle | 几何点 / 元素句柄 |
| Aveva.Marine.Utility | MarUtil | `!util.TBEnvironmentGet('SB_SHIPDATA')` 读 Tribon 环境变量 |
| Aveva.Marine.DataExtraction | MARDEX | `extractPML()/nextResultPML()/getIntPML()/getString()` 数据抽取 |
| AVEVA.Marine.Design | MARHULLPAN | `stmtExec(0, stmt)`、`getNearbySeams()` 船体板语句执行 |

范式文件:`PMLLIB\marinedrafting\functions\mDraPickElement.pmlfnc`、`PMLLIB\hulldesign\objects\phullnotch.pmlobj`。

### 4.3 PMLNET 体系(PML 嵌 .NET 控件/服务,174 个文件)

- **控件嵌入表单**(`aba\forms\abaarea.pmlfrm` 范式):
  ```pml
  frame .outer 'Areas'
    container .netFrame nobox pmlNetControl 'NET' width 56 height 8   -- .NET 宿主容器
  exit
  using namespace 'Aveva.Pdms.Presentation'
  member .displayCtrl is NETGRIDCONTROL
  !this.displayCtrl = object NETGRIDCONTROL()
  !this.displayCtrl.addEventHandler('afterSelectChange', !this, 'netAfterSelectChange')  -- 事件→PML 方法
  !this.netFrame.control = !this.displayCtrl.handle()                                     -- 挂到容器
  !this.displayCtrl.bindToDataSource(object NETDATASOURCE('Areas', !this.headings, !this.rowSet, '^Name'))
  ```
- **无 UI 服务**:`import 'PDMSCOMMANDS'` → `object PMLNetCommandManager()` → `.executeCommand('AVEVA.Attributes.Show')`。
- **文件对话框 + Excel**:`object PMLFILEBROWSER('SAVE')` → `.show(...)`;`NETGRIDCONTROL` + `NETDATASOURCE` + `.SaveGridToExcel(!file)`(`avevamarine\functions\blockAdminTemplate.pmlfnc`)。
- 对应 .NET 侧写法见《AVEVA-Marine-NET开发技能.md》第 5 节。

---

## 5. 部署流程(定制 PML)

### 5.1 放置位置:平行目录 + 环境变量前置(铁律 PKG-05)

```bat
rem 方式 A:启动机器/用户级,在 marine.bat 调 evars.bat 之前
Set PMLLIB=C:\mydev\pmllib %pmllib%
Set PDMSUI=C:\mydev\pdmsui %pdmsui%

rem 方式 B:项目级 —— 在 E:\AVEVA\Marine\Projects12.1.SP4\Mar\evarsMarine.bat 里前置
```

- 自定义路径放 **前面**(先搜到先生效),实现覆盖式定制而零改动标准文件。
- 自建目录也按 `模块名\{forms,functions,objects}` 组织,文件名(小写)与内部定义名对应。
- 图标 .png 放自定义 `icons\`,PML 里用 `$!iconSize` 等引用与官方一致。
- **PDMSUI(PML1)侧的三个合法挂载点**:菜单/工具条入口 → `%PDMSUI%\DES\ADDINS\` 加定义文件(实文格式与 CALLxx 同义词机制见《Marine-PDMSUI-PML1宏机制速查.md》);启动钩子 → `%PDMSDFLTS%\DES-INIT-MAC`(macload 自动调用、吞错);其余一律不碰 PDMSUI。

### 5.2 装载与验证

| 动作 | 命令 |
|---|---|
| 新建/改文件后重建索引 | `pml rehash`(只扫第一个路径)/ `pml rehash all`(全路径) |
| **rehash 后等约 10 秒**再调用(RUN-01 铁律) | — |
| 改已加载表单/对象 | `pml reload form !!Name` / `pml reload object NAME` |
| 验证路径顺序 | `q evar pmllib` |
| 验证文件装载源 | `q var !!PML.getpathname('myfile.pmlfnc')` |
| 冒烟 | `show !!myForm` → 逐控件点回调 |

### 5.3 PML 与 .NET 混合部署的边界

- PML `import 'xxx'` 只在 **exe 目录**解析 DLL(或 AddinsData 相对路径,仅 addin 体系);自研 .NET 库要被 PML import,编译出的 DLL 放 exe 目录即可(PMLNet 桥会加载),注册到 Addins.xml 只是让它作为 addin 自动 Start,两种机制独立。
- 详见《AVEVA-Marine-NET开发技能.md》。

---

## 6. 与既有三份规范的核对结果(2026-09-25,本树实测)

| 规范断言 | Marine 树实测 | 结论 |
|---|---|---|
| gosub 官方 0 次使用 | **0 个文件**含 gosub(pmlfnc/frm/obj) | ✅ 成立 |
| `==` 符号比较不存在(OPR-01) | 64 个 pmlfnc 含 `==`,抽样 20 处**全部是注释分隔线 `-- ====`** | ✅ 成立,且证实审核规范"预处理剔除注释行"必要 |
| `loop/endloop` 不存在(CTL-01) | 0 个文件含 endloop | ✅ 成立 |
| `setup form` 为主(PDMS 语境) | 1368/1380 个 pmlfrm 用 `setup form`(layout form 27) | ✅ 记忆第 6 章#1 裁决成立 |
| PML2 面向对象主流 | 2030 个文件含 `define method`;3693/3703 个 pmlfnc 结构合法 | ✅ 成立 |
| —— (新增数据) | 329 个文件 `import` .NET 程序集;174 个文件用 PMLNET 体系 | Marine 混合开发规模,补充进规范 |

**结论:三份规范对 Marine 12.1 全部适用,无需修改;本文第 3、4 节是 Marine 增补**(建议后续并入记忆文件时按其维护约定:语法证据入 R 条目,流程入第 2 章)。

---

## 7. PML 相关文档索引(本安装自带)

| 文档 | 用途 |
|---|---|
| `Documentation\PMLPUG.chm` | **PML 用户指南**(与本 12.1 安装版本匹配) |
| `Documentation\Customisation_Guide.chm` / `SOFTCG.chm` | 软件定制指南(平行目录、部署总则) |
| `Documentation\Setup_Customisation.chm` | Setup/环境变量定制(11MB 大部头) |
| `Documentation\Dictionary.chm` | 属性/对象字典 |
| `Documentation\Toolkit_Concepts.chm` | 编程接口概念总览 |
| `Documentation\Basic.chm` + `basic_macro_dex.txt` 等示例 txt | 基础与宏示例 |
| TM-1401 / TM-1402 培训教材 | 生成规范/记忆已引用 |

---

## 8. 快速上手清单(新会话/AI 开发直接执行)

1. 写码前:读生成规范第 2 章;不确定 API → 防猜协议(先 grep 本 PMLLIB 树,再查 PMLPUG.chm)。
2. 新文件放 `C:\mydev\pmllib\<模块>\{forms,functions,objects}\`,带规范文件头。
3. 部署:evars 前置 `PMLLIB` → `q evar pmllib` 确认顺序 → `pml rehash all` → 等 10 秒 → 调用。
4. 给用户入口:APPMENU 对象注入标准菜单(第 3.4 节),或 .NET uic 挂按钮(见 .NET 文档)。
5. 放行前:过审核规范 A→B→C→D 流程。

---

## 9. 语料库与深读成果(2026-09-25 全量学习)

PMLLIB 全部 6075 文件/206.9 万行已逐文件扫描入库,成果与用法见:

- **`PML语料\`**(README 在内):corpus_index.tsv 逐文件索引、functions.tsv/object_methods.tsv/forms.tsv 三本签名目录、stats_and_idioms_auto.md 频次表+习语实例(带出处)、pdf_text\ 8 份 PDF 全文(含官方两本手册)。**防猜查证走语料库,不再裸 grep 安装目录。**
- **《Marine-PML官方公共库目录.md》**:common 764 文件清点——进度/CSV/文件定位/单位转换/全局单例/阻塞弹窗/Excel(115 处调用)/DAC 等基础设施全部有官方实现,写码前先查。
- **《Marine-PML学习报告-2026-09-25.md》**:工程组织范式(mds 三级入口链、大表单组织、DAC+一次性 savework 事务、KCOLLECT+setProgress 批量操作)、频次数据、审核规范回归(3 条预处理修订:剔字符串、拼 `$` 续行、VAR-02 豁免成对 `!CE = !!CE` save/restore)、`.members` 待核验项关闭。

关键补充惯用法(官方高频,规范未载):
- 遍历带进度:`do !i index !arr` + `!!fmsys.setProgress(!i * (100 / !arr.size()))`,结束 `setProgress(0)`。
- 保存/恢复当前元素:`!CE = !!CE` … `!!CE = !CE`(成对,VAR-02 豁免此模式)。
- 多行条件用行尾 `$` 续行(`if ( !a.set() and $`),审核需先拼行。
- 大表单头部"Methods defined"索引表即目录;paragon 页签范式 = TABSET + 一页签一 `.xxxInit(!mode)` 方法。
