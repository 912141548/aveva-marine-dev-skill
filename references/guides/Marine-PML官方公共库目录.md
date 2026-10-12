# Marine PML 官方公共库目录(PMLLIB\common,764 文件)

> 用途:**写新代码前先查本目录**——字符串/文件/集合/单位/弹窗/进度/Excel/全局单例等能力官方都已有实现,直接复用,避免重复造轮子和编造 API。
> 来源:逐文件清点 `E:\AVEVA\Marine\OH12.1.SP4\PMLLIB\common`(functions 308 + objects 256 + forms 200)。
> 注意:很多文件头 `Module:` 字段写的是 design/draft 等,那只是"最早使用方";头部 `Group/Keyword`(String Handling、File Handling 等)才是真实分类。
> 方法签名明细查 `PML语料\object_methods.tsv`;本目录带出处的调用示例查《Marine-PML学习报告》§3。

---

## 一、基础设施(跨模块通用,新代码优先复用)

| 能力 | 官方实现 | 说明 |
|---|---|---|
| **进度条** | `!!displayProgress(!value is REAL, !max is REAL)` | common\functions\displayprogress.pmlfnc;内部 `!!fmsys.setProgress(int(!value/!max*100))`,完成传 0 复位 |
| **CSV/表格装载** | `!!readCsvRecord(!string is STRING) is ARRAY` | 双引号定界、成对引号转义;**文件级装载用对象 `COMSPREADSHEETLOADER`**(`setDataSource/loadDataSource/getRows/getHeadings`) |
| **文件定位三件套** | `!!uniquePath(!rootFile, !dirlist, !application) is ARRAY` | dirlist `'USER PROJ PDMS CADC'` → %PDMSUSER% / 工程 DFLTS / 系统DFLTS / PMLLIB data;返回去重 FILE 数组 |
| | `!!searchPaths(!file) is ARRAY` | 返回文件实际存在的全部搜索路径 |
| | `!!findFileWild(...)` | 通配符在搜索路径找文件 |
| **单位转换** | `!!comUnitsConvert(!value is REAL, !inputUnit, !outputUnit) is REAL` | 返回无量纲实数;单位中枢对象 **COMUNITS**(getCurrentUnitsByPType/saveCurrentUnits/restoreAllSavedUnits/isImperialSavedDist/setUnits)与 **COMFORMATS**(113 个方法,distance/angle/bore/mass 格式) |
| **全局单例** | `!!comDefineGlobal(!object is ANY)` | 等价调 `!object.globalInstance()`;凡实现 `.globalInstance()` 的选项对象(COMSYSOPT/NAMOPT/RULESTORE/GPHCOLOPT/GPHREPOPT…)都经它建 `!!xxx` |
| **阻塞式输入弹窗** | `!!comListInput(!formTitle, !gadgetTitle, !height, !dText, !value) is STRING` | 动态建 blocking 表单,list 控件(height=1 变 option),返回所选;`!!comTextInput` 同理文本输入 |
| **"只提示一次"弹窗** | `!!comAlertOnce(!question, !answer, !questGlobal, !formType)` | formType = confirm/message/warning;questGlobal 是"不再提示"开关的全局变量名 |
| **Excel 导出** | `!!exportToExcel(!grid, !fileName, !dialogTitle)` | **全树最热门公共函数(115 处调用)**;对象 **EXCELIO** 封装 .NET ExcelInterface(import/export/configurationNames) |
| **错误分发** | `!!anyError(!messageCode is REAL)` | 负数→警告、正数→错误、0→无动作(定义即文档,可作统一错误出口) |
| 字符串 | `!!ascii / !!dehash / !!charactersymbol / !!evarsplit / !!comQuoteIfString / !!namToPdmsName / !!stringRoundupValue / !!checkCsvCount` | ASCII 互转、hash 还原、非 ASCII 符号、环境变量拆分、实数不加引号、非法名清洗、按格式四舍五入 |
| 集合/列表 | `lst*` 函数族 + **LST/LSTSTORE/LSTGLOBAL/LSTLINKLIST** 对象;`!!comSaveLists/!!comRestLists` | 通用列表存储系统(按 tag 增删改查/链接控件);用户列表持久化到 PDMSUSER |
| 校验/权限 | `!!comValidateRange / !!checkName / !!dacCheck / !!dbRefUpdatable / !!comTeamCheck / !!comAdminStatus` | 范围校验(文本控件校验回调)、元素名/DAC 写权限/团队/管理员 |
| DB 遍历 | `!!dtbOwnerOfType(s) / !!dtbMemberOfType / !!dtbWithAttribute / !!elementOfType / !!memberOfType / !!findFirstMember / !!firstParent / !!dbeWorldGet` | 按类型/属性向上找 owner、向下找成员 |
| 系统 | `!!comGetWork / !!comSaveWork / !!admCommand / !!splashScreen / !!pmlDefinition` | savework 确认封装、命令执行+回显、启动画面、**打印 PML 定义目录(开发辅助)** |

---

## 二、核心对象速查(common\objects,256 个)

| 对象 | 用途 | 关键方法 |
|---|---|---|
| **APPCNTRL** | 应用切换总控 | addApplic/findApplic/isAdmin/appMenu/currentApp(30) |
| **APPMENU / APPMENUCNTRL** | 应用菜单注入与跨应用可见性 | insertAfter/add/activate;addMenu/addBarMenu |
| COMFORMATS | 公共单位/格式中枢 | 113 个方法 |
| COMUNITS | 单位查询/保存/恢复 | 16 方法 |
| COMPROPDATA / COMPROP / COMPROPTABLE | 属性框架(DESIGN 参数模板机制) | setProperties/editProperties/getPropertyTable…(87/60/21) |
| COMSPREADSHEETLOADER | CSV/XLS 装载为 PML 数组 | setDataSource/loadDataSource/firstRowIsHeading/getRows/getHeadings |
| EXCELIO | Excel 读写(.NET ExcelInterface) | import/export/configurationNames |
| REPORTIO / DATASHEETIO | 报告输出 | print/exportAsXlsx/exportAsCsv/exportAsPdf/publishToAVEVANet |
| EDGCNTRL / EDGPACKET / EDGPICKPACKET | **EDG 事件驱动图形/拾取体系总控** | globalInstance/active/add packet/setPrompt/setFilters;elementPick/defineCircle/defineMeasure(36/28/47) |
| EDGPOSCNTRL | 3D 定位工具箱控制 | loadOffsets/pickTypes/setPlane/wpMethods(49) |
| GPHVIEWS | 视图总控 | addDesign/rotatePacket/clipboxPacket/look/measure/saveViews(79) |
| GPH* 绘制族 | 画线/弧/网格/尺寸(gphline/gphcircle/shipgrid/gphdimension…) | draw/edit/definition |
| GMF* 几何族 | 几何计算(弧/盒/线/面/多边形/点) | through3Points/fillet/tanTan/within/nearestEdge/polarPoint |
| POSITIONLINK / ORILINK | **标准 3D/定向定位链接**(表单↔图形联动) | initialise/linkInput/setPosition/setWrt(18) |
| LSTGLOBAL / LSTSTORE | 列表存储全局仓库 | number/exists/add/addLinkList/storedLists |
| NAMOPT | 自动命名规则 | rules/auto/getName/nameString(19) |
| STATUSDATA | 状态管理 | assign/promote/demote/setStatus(49) |
| CHKSTORE / CHKCLASS / CHKDEFINITION | 检查器框架 | globalInstance/save/load/edit/listClasses |
| ELEMENTSTORE | 应用缺省存储区容器 | store/types/rule/collection/evaluate(18) |
| COMENHANCE | Design 增亮集合管理 | addItems/refresh/setColour/setTranslucency(13) |
| VIEWMANAGEMENT | 视图保存/恢复 | saveView/restoreToView/saveDrawLists(12) |
| DELETEMANAGER | 删除管理(可注册特殊处理) | registerObject/dbDelete/errors(9) |
| ANYDATASET | 任意属性柔性容器 | setAttribute/getAttribute/attributeExists/copyAttributesTo |
| EXTERNAL | 外部查询封装 | send/getResult/getAllRows/request/connected(16) |

---

## 三、常用表单(common\forms,200 个,★=高频复用)

| 表单 | 用途 |
|---|---|
| ★`!!fileBrowser` / `!!fileViewer` | 文件浏览 / 文本查看 |
| ★`!!elementList` | 通用元素列表(选择即导航) |
| ★`!!pos3D` 族(pos2D/pos3dexplicit/pos3doffset/pos3drelative) | 标准 2D/3D 定位表单 |
| ★`!!edgPositioning` / `!!edgShipPosition` | EDG 3D 定位工具箱 / 船体定位(Marine) |
| ★`!!spcView` / `!!spcEdit` | 规格查看/编辑 |
| ★`!!alertOnce{,Confirm,Message,Warning}` | "只提示一次"弹窗家族 |
| ★`!!pmlBrowser` / `!!pmlForms` / `!!pmlVariable` | **PML 开发辅助**:定义浏览器/已装载表单/变量浏览器 |
| ★`!!qryDac / !!qryUserAcr / !!qryProject` | DAC/权限/工程信息查询 |
| ★`!!storageAreas` | 通用存储区表单 |
| ★`!!rptOutput` 族 | 标准数据输出 |
| ★`!!dbList` / `!!mdbList` | 数据库/MDB 浏览 |
| ★`!!namOptEdit` | 自动命名规则编辑 |
| ★`!!saverestoreView` | 视图保存/恢复 |
| ★`!!stop` | 过程取消按钮(状态标志轮询) |
| `!!comboBox` / `!!comCombi` | 组合框/组合控件模拟 |
| `!!colourSelect` / `!!comExprBuilder` | 颜色选择 / 表达式构造器 |
| `!!gph3DLook` / `!!gph3DRotate` 等 gph* 编辑族 | 视图与图形对象操作 |
| `!!shipReferenceGrids` | 船体基准网格 |

---

## 四、MDS 子库的公共件(跨模块借用的现成工具)

`PMLLIB\mds\common\`(61 函数 + 13 对象,文件名 k* 前缀)虽然住在 mds 下,但被全树借用:

| 函数/对象 | 次数 | 用途 |
|---|---|---|
| `!!mdsDacControl` | 3573 | DAC claim 总开关(写前 TRUE 写后 FALSE) |
| `!!kgetsetUnits` | 1032 | 记住项目单位并切 mm |
| `!!kstrReal` | 1004 | 字符串距离→mm REAL |
| `!!KCollect(!kcol is KCOLLECT)` | 466 | collect 命令→DBREF 数组(BLOCK evaluate) |
| `!!kcollectAllFor` | 462 | 按 owner+类型通用收集 |
| `!!kenhanceList` | 433 | DBREF 列表高亮 |
| `!!kshowForm` | 336 | 表单统一 show/init |
| `!!kresetActive` | 311 | 恢复 current/active 上下文 |
| `!!kcheckWrite` / `!!kcheckName` / `!!kloadData`(.pmldat)/ `!!kactionCommands`(数组逐条执行命令) | — | 校验/装载/批量命令 |
| **KCOLLECT** 对象 | — | 收集参数包(Search/Class/Expression/Type 成员) |
| MDSREADEXCEL 对象 | — | .NET 读写 Excel(GridControl) |

---

## 五、使用守则

1. **防猜协议落地顺序**:本目录 → `PML语料\object_methods.tsv`(签名)→ 官方源码真实调用(语料库 grep)→ 手册(pdf_text)→ 都无则 `TODO-UNVERIFIED`。
2. 复用基础设施函数时**照抄官方调用姿势**(学习报告 §3 有带 出处 的示例);借 mds\common 的 k* 函数时注意它内部可能依赖 `!!mdsoptiondefs` 等应用单例,先 grep 其初始化路径。
3. 业务控件(EDG 定位工具箱、规格选择、属性框架)是"实例化对象 + 挂到自己的表单"的用法,不要重写其逻辑。
