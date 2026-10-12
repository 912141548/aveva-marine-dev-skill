# Marine 横切命令族大全·卷十一（穷举级·源码实证）

> 来源：PMLLIB\common\(764 文件) + global\(196) + admin\(254) + limbo\(99) 逐目录扫描穷举（findstr 行号实测；多路径 /S 会静默丢命中，故按目录逐一重扫）。
> 适用：AVEVA Marine (PDMS 系) 12.1 SP4。AID/GPH/CLAIM/命名服务/会话/$ 命令/VAR/CONSTRUCT 全收录。
> 路径约定：`<B>` = `E:\AVEVA\Marine\OH12.1.SP4\PMLLIB`。

---

## 族 1：AID 图形辅助命令族

### 1.1 全部 AID 子命令与语法变体（9 种子命令 + CLEAR 的 9 个子型）

| 子命令 | 完整语法变体（全部实测形态） |
|---|---|
| `AID SPHERE` | `AID SPHERE NUMBER n pos DIAMETER d` / `... DIAM d` / `... DIAMETER d MM` / `AID SPHERE NUMB n pos DIAM d` |
| `AID ARROW` | `AID ARROW NUMBER n AT pos DIRECTION dir HEIGHT h` / `... DIR dir HEI h` / `... NUMB n AT pos DIR dir HEIGHT h` / `... PROP r` / `... PROPORTION 0.1` / `... DIRECTION N/E/U HEIGHT h MM`（罗盘方位） |
| `AID BOX` | `AID BOX NUMBER n AT pos ORIENTATION ori XLENGTH x YLENGTH y ZLENGTH z` / `... XLEN x YLEN y ZLEN z AT pos` / `... POSITION pos ORIENTATION ori ... FILLED ON` / `... FILL ON` / `AID BOX NUMB n XLEN x YLEN y ZLEN z POSITION pos` |
| `AID LINE` | `AID LINE NUMBER n pos1 TO pos2` / `... linestyle dashed` |
| `AID TEXT` | `AID TEXT NUMBER n 'txt' AT pos` / `AID TEXT NUMB n \|txt\| AT pos` |
| `AID CYLINDER/CYLI` | `AID CYLINDER NUMBER n AT pos DIAMETER d HEIGHT h` / `... POSITION pos ORIENTATION ori DIAMETER d HEIGHT h [FILLED ON]` / `AID CYLI NUMBER n DIAMETER d HEIGHT 1mm POSITION pos ORIENTATION ori FILLED OFF` |
| `AID ARC` | `AID ARC NUMBER n arcStart TO arcEnd THRU midPoint` |
| `AID CIRCLE` | 无文本调用（仅封装对象 GPHCIRCLE 与拾取提示） |
| `AID CLEAR` | `AID CLEAR ALL [n]`、`AID CLEAR LINE/TEXT/SPHERE/CYLI/CYLINDER/BOX/ARROW/ARC n`、`AID CLEAR $!type $!i`（类型变量化） |

参数词全集（含缩写对）：`NUM/NUMB/NUMBER`、`AT/POSITION`、`DIR/DIRECTION`（N/E/U/方向变量）、`HEI/HEIGHT`、`DIAM/DIAMETER`、`PROP/PROPORTION`、`XLEN/XLENGTH`、`YLEN/YLENGTH`、`ZLEN/ZLENGTH`、`ORI/ORIENTATION`、`FILL ON/FILLED ON/FILLED OFF`、`TO`、`THRU`、`linestyle dashed`、单位后缀 `mm/MM`。

### 1.2 真实调用示例

```pml
-- common\forms\comspacemanagement.pmlfrm:1946
AID ARROW NUM $!this.clippingAidNumber AT $!xArrowPos DIR $!xArrowDir HEI $!aidArrowHeight PROP 0.5
-- :1926-1929 / :2044-2057
AID CLEAR TEXT/ARROW $!this.clippingAidNumber
aid line number $!n $!cornerPos1 to $!cornerPos2 linestyle dashed   $* 十二条包围盒
-- common\forms\polylineui.pmlfrm:625-627 / :712
AID ARROW NUMB $!this.meAidCurrentEdge AT $!position DIR $!xDir HEIGHT $!axesLength
AID SPHERE NUMBER $!this.meAidCurrentVertex $!position DIAM $!diameter
-- common\forms\testposlink.pmlfrm:346
AID BOX NUMB 100 XLENGTH $!xLength YLENGTH $!yLength ZLENGTH $!zLength POSITION $!newPosition
-- common\functions\tagendexcess.pmlfnc:70,73（预定义号段 14000）
AID CLEAR ALL 14000
AID TEXT NUMBER 14000 |$!tagEnd Excess $!distance| AT $!<tagPosition>
-- common\objects\gate.pmlobj:248（全局对象号引用）
AID SPHERE NUMBER $!!<aslCentralData.aidVolMain> $!<this.position> DIAM 250mm
-- common\objects\gphangledimension.pmlobj:244
AID ARC NUMBER $!<aidNumber> $!<arcStart> TO $!<arcEnd> THRU $!<midPoint>
-- common\objects\gphspine.pmlobj:168
AID CYLI NUMBER $!<aidNumber> DIAMETER $!diameter HEIGHT 1mm POSITION ... ORIENTATION ... FILLED OFF
-- common\objects\comgridruler.pmlobj:1917-1929（船基线 AP/FP 标注）
AID TEXT NUMBER $!this.baseAid 'AP' AT $!<from>
-- limbo\functions\aidaxes.pmlfnc:42-44 / aidorientate.pmlfnc:53 / aidline.pmlfnc:35
AID ARROW NUMBER $!number AT $!position DIRECTION N/E/U HEIGHT $!size MM
AID BOX NUMBER $!number XLEN 2000MM YLEN 2000MM ZLEN 10MM ORIENTATION $!oriString AT $!posString FILL ON
AID LINE NUMBER $!number $!startPos TO $!endPos
```

### 1.3 PIN 位置拾取辅助

```pml
var !pinPosition PIN $!pinNumber POS          -- edgpicktype.pmlobj:427,571,800 等（大小写两种）
var !pinDirection pin $!pinNumber dir         -- :802
var !ppos POS PIN$!number WRT WORLD           -- limbo\functions\posofpin.pmlfnc:36
var !pdir DIR PIN$!number WRT WORLD           -- limbo\functions\dirofpin.pmlfnc:35
```
PIN 1 COPY PL OF / PIN n plane / PIN n OFF：不在 common/global/admin/limbo（属 Design 交互建模，见 Router 卷 §6）。

### 1.4 封装对象全方法

- **AIDNUMBERS**（aidnumbers.pmlobj，14 方法）：`aidNumbers() globalInstance() registered(n) isRegistered(n) default() addNumber(n,data) add(data)→REAL next() remove(n) replace(entry,data) replaceNoUpdate(...) get(entry) draw(entry)（内部 AID CLEAR 六族 :502-520）hide(n)`。
- **AIDCONSTRUCTORS**（aidconstructors.pmlobj，55 方法）：`save(file) load(file) stores() store(gphType) definedText(option) definedNumbers(option) recursion(state) refresh() add(...)`×12 重载（POSITION/GPHPOSITION/ARC/GPHCIRCLE/ARRAY/LINE/GPHLINE/PLANE/GPHPLANE/GPHRADIALGRID/GPHLINEARGRID/GPHPLANTGRID）`remove()`×4 `position() radius() length() edit() explicit(type) copy/delete/paste/orientate(pickData) blobSize(diameter,option)` + Packet 族 13 个（circlePacket/linePacket/planePacket/pointPacket/modifyPacket/copyPacket/orientatePacket/deletePacket/pastePacket/radialGridPacket/linearGridPacket/plantGridPacket/editPacket）。
- **AIDMODIFY**（aidmodify.pmlobj，17 方法）：`add(n) remove(n) clear() isAdded(n) rotate(...)`×3 `rotationLine(...) mirror()`×2 `mirrorPlane(plane) offset()`×4。
- limbo 旧式封装函数（每函数 = 一条 AID 命令包装）：`aidaxes aidclear aidline aidorientate aidsphere clearaid drawaidarrow drawaidbox drawaidcylinder drawaidsphere drawaidtext`；common 侧另有 `aidvolumedraw drawarrow drawaxes drawvolume`。

---

## 族 2：GPH 图形命令族

**结论性事实**：4 目录中**不存在文本式 `GPH XXX` 监视器命令调用**（全部 0 命中）。GPH 族完全通过 **32 个 gph*.pmlobj 封装对象**消费：
`gphangledimension gphasl gphautocolour gphaxes gphbox gphcircle gphclipbox gphclipplane gphcolopt gphdimension gphdrawlists gphline gphlineargrid gphlocalvolume gphplane gphplantgrid gphpointvector gphpolygon gphposition gphradialgrid gphrepdefinition gphreplink gphreplst gphrepopt gphshipgrid gphsphere gphspine gphthreedplantgrid gphthreedradialgrid gphviewopt gphviews gphvolume`（均在 common\objects\）。

**GPHSPINE 落图序列**（gphspine.pmlobj .draw :141-193）——GPH 对象最终全由 AID 命令实现：
```pml
AID CLEAR LINE/CYLINDER/ARROW/TEXT $!<aidNumber>
AID ARROW NUMBER n AT line.startPosition DIR direction HEIGHT length
AID TEXT 'Start'/'End' AT ...
AID CYLI ... FILLED OFF
AID TEXT '$!text' AT midPoint
```

**GPHVIEWS 视图命令中枢**（gphviews.pmlobj，60+ 方法）：`globalInstance add×2 addDesignForm/addDesign/checkAddDesign/addNavigate remove viewIndex close×2 nextAvailable bar lMenus/sMenus longMenus measure align tag windowPacket/window×3 rotatePacket/rotate×3 rotateElement/rotatePick/rotateBox/rotateExplicit limitsPacket/limits×2 limitsPick/limitsElement/limitsRestore/limitsList/limitsBox/limitsExplicit copyPacket/copy×2 navigate colour auto toDrawlist/fromDrawlist look×2 plan lookExplicit isometric clipButton clipboxPacket/clipboxLimitsPacket clipbox clipCapColour clipboxElement×2 clipboxExplicit/Box/Pick clipPlanes drawlistButton/drawlistButtonPick/drawlistMenu/drawlist×2 axesButton graphicsToggles doMenuAction saveViews saveRestoreViews advancedViewControl restoreViews convertVolumeToLimits refreshAllViews removeAll`。

表单级函数：`!!gph3DDesign(!number) is FORM`、`!!gph3DNavigate(!number) is FORM`、`!!gphMinimumMenus(!form)`。

---

## 族 3：CLAIM 工作共享命令族

### 3.1 CLAIM / EXTRACT CLAIM / UNCLAIM 全变体（lstclaim.pmlfrm 为主）

```pml
CLAIM CE HIERARCHY                 -- lstclaim.pmlfrm:646
CLAIM CE / CLAIM CE MEM            -- :722 / :786
CLAIM $!item.type MEM HIERARCHY    -- :856
CLAIM $!claimPicked / CLAIM $!entriesStr[$!i] / CLAIM $!dbRef

EXTRACT CLAIM CE HIERARCHY         -- :631；admextractcntrol.pmlfrm:1641
EXTRACT CLAIM ELEMENT / LATEST     -- admextractcntrol:1647 / admextracthier:150
EXTRACT CLAIM CE / CE MEM          -- :707 / :771
EXTRACT CLAIM $!dbRef              -- mmsclearattributes.pmlfnc:79

UNCLAIM CE HIERARCHY / CE MEM HIERARCHY / CE / CE MEM   -- :1196/:1235/:1273/:1312
UNCLAIM $!!ce / UNCLAIM ALL        -- :1359 / :1403
```

### 3.2 Admin 侧 DDL（admin 目录专属）

```pml
CREATE DB <name> <type> ... ACCESS <mode> CLAIM <mode> ...        -- admdb.pmlfrm:486
CHANGE <db> CLAIM <mode>                                           -- admdb:731、admworkmod:207
CREATE VARIANT <db> FROM <from> ... CLAIM ... REFBLOCKS ...        -- admextract.pmlfrm:375,377
CREATE EXTRACT <db> FROM <from> ...                                -- admextract:382,384
CREATE WORK VARIANT FROM <db> FOR '<user>' ...                     -- admwork.pmlfrm:428,431
CHECKOPTION CLAIM $!claim                                          -- admdic.pmlfrm:549
OPCLAIM <mode>（DAC 权限操作）                                      -- admperop.pmlobj:494,572
var !extractClaim CLAIMLIST EXTRACT $!elementName（CLAIMLIST 类型化 VAR）-- adminelem.pmlfrm:573
```

### 3.3 权限 handle 错误码与消息号（穷举）

| 码 | 语义 | 出处 |
|---|---|---|
| (2,201) | isExtr 测试失败 | lstclaim.pmlfrm:626 |
| (2,603) | 已被本人 claim | lstclaim:647-663 |
| (2,614) | ≤5 项被他人 claim | lstclaim |
| (2,616) | >5 项被他人 claim | lstclaim |
| (2,633) | Extract Claim 进行中 | lstclaim |
| (41,243) | make global 后 CE 被删 | moduleswitch 注释 |
| (39,15) | 无 MDB | moduleswitch |

消息号（lstclaim:633-640 注释）：607 无权 claim；613 元素在后续 session 被改需 GETWORK；614 已被他人 claim；623 父 extract 被改需 EXTRACT REFRESH DB；631 父 extract 中已删除；635 无法从父 extract claim。

claim 状态读取：`!!ce.okClaim / !!ce.lclm`（admdb:844）、`!db.claim`（dblistselect:79）、`!dbRef.claimDb`；claim 高亮 `ENHANCE CE WHERE (LCLM EQ TRUE AND USERC EQ '$!user') FROM DRAWLIST COLOUR $!this.claimColour`（lstclaim:670）；写保护检查对象 `comcheckdbwrite.pmlobj .checkDBwrite(DBREF)`。

---

## 族 4：命名服务

### 4.1 !!autoNameCE（内置全局函数，定义不在 PMLLIB）

调用链：`!!autoNameCE(TRUE)`（cuProjectHandler.pmlobj:950）；design 30+ 处 `CALL !!autonamece(false)`（appdesmain.pmlfrm:610-611 菜单 'CE only'/'CE offspring'）；本地包装 `.autoNameCe(!mode)`（cblCable.pmlfrm:4494 等 5 处）。

### 4.2 !!checkName 全逻辑（common\functions\checkname.pmlfnc:33）

```pml
define function !!checkName (!name is STRING, !nameType is STRING) is STRING
-- 空名 → !!messageFile.warning(143,008)
-- NEW 模式：
--   `*` → CE 全名（var !star STAR :54-75）
--   `^` → owner（:80-88）；`~` → CE（:92-100）
--   拒绝 `$@`(:104) / `$$`(:110)
--   去空格 + 补前导 `/`（:116-119）
--   占用检查 var !useName USENAME $!newName（:122）
-- OLD 模式：!newName.dbRef() 失败后加 `/` 重试(:136-145)，warning(143,005/006/007)
```
调用方 15 处（assbrowser:1238/1294 'NEW'、createsyscda:135/228 'OLD'、pos3dexplicit:233 等）；配套 `!!nameGadget(!gadget,!nameType)`（namegadget.pmlfnc:32，内部调 !!checkName）。

### 4.3 NAMOPT 自动命名规则引擎（namopt.pmlobj，17 方法）

`namOpt() / namOpt(BOOLEAN) / default(setCore) / globalInstance() / localCopy()→NAMOPT / copyToGlobal() / coreSettings() / load() / save() / edit() / rules()×2 / auto()×2 / mode()×2 / getName(key)→NAMOPTRULE / nameString(element,key,check,wildCard)→STRING(+STRING 重载)`。
加载链（:250-309）：`!!searchPaths(filename)` → DEFAULTFILE 按 USER/PROJ/DFLTS 分档 → `$m "$!<localName>"` 把规则文件当宏执行 → 失败 `!!messageFile.warning(146,31)`。
配套：NAMOPTRULE 对象（6 参构造 + save()）、表单 !!namOptEdit/!!namOptRulesEdit、升级函数 `!!namOpt111To112(!oldFile)`、全局实例创建器 `!!comDefineGlobal(!object)`（comdefineglobal.pmlfnc:28）。

---

## 族 5：窗口/桌面/会话命令

### 5.1 表单显示运行时命令（实测计数）

`show !!form` common 137 处；`hide !!form` 20 处；`kill !!form` 20 处（attlib.pmlfrm:22、compropreset.pmlfnc:30-37 动态 `kill !!comPropEdit$!<i>`）；`setup form !!name` common 350 处 + admin 206 + global 75。
控件关键字计数（行首，common/admin/global）：button 601/274/192、text 473/149/95、frame 310/76/42、toggle 236/64/164、option 177/97/105、list 130/70/74、paragraph 111/16/24、combo 3/0/0、slider 5/0/0；table/tabset/canvas/tree 0（本版本未用）。
`waiton !!form` 4 处（comlistinput.pmlfnc:66、comalertonce.pmlfnc:47 `waiton _$!form at xr0.4 yr0.45`）。

### 5.2 会话命令（SESSION/MDB/MODULE）

会话文件词表（writesessionfile.pmlfnc:77-96）：`PROJNAME PROJECT PROJNUMB USERNAME MDB MODULE RESTORE READONLY`。
MDB 采集：`var !mdbList collect all MDB`、`!mdbs = MDBS`、`object MDB(!currentMdb)`。
**模块切换中枢**（limbo\functions\moduleswitch.pmlfnc，经 `$M` 调用）：
```pml
$d2=FALSE / $d3=TRUE / $d4=UNSET          $* 入口参数默认值(:31-33)
!switchName = (upcase(|$1|))              $* :46
object USER(!user) → !userInfo.access.upcase() eq 'GENERAL'   $* ADMIN 权限拦截(:53-60)
!nextModule.command = |FINISH|
$!nextModule.command $!readOnly   /   QUIT $!nextModule.command $!readOnly   /   QUIT
savework                                   $* 命令本体
READONLY                                   $* 限定词
handle (39,15)                             $* 无 MDB
```
Banner 查询（limbo\functions\module.pmlfnc）：`var !data BANN NAME/STATUS/COPYRIGHT/COMPANY/SHORT`、`var !data DDL`。
**`DB ATTACH`/`DB DETACH`/`FIRSTDB` 文本命令：4 目录 0 命中**（属 Monitor 会话文件/核心命令，PML 层经 `!db.claim`、`object MDB()`、`MDBS` 访问）。

---

## 族 6：$ 系统命令全集（4 目录实测）

| $ 命令 | 语义 | 真实调用示例 |
|---|---|---|
| `$m "file"` | 执行宏（常规） | runmacro.pmlfrm:85 `$m "$!this.filename"`；appxload.pmlfnc:68 `$m "%PDMSUI%/$!<modName>/$!<appName>/ICONS"` |
| `$M "file"` | 执行宏（模态/启动） | appcntrl.pmlobj:375 `addSwitchCall('$M "..."')`；runmacro.pmlfnc:36 `$M "$!macro" $!<arguments>` |
| `$s name=...` | 定义同义词 | appcntrl.pmlobj:1034 `$s $!synonym=$M "%PDMSUI%/$!moduleDir/$!dir/$S1"`（**$S1 = 同义词形参**） |
| `$1..$9` | 宏位置参数 | moduleswitch.pmlfnc:46,49-56（$1/$3/$4） |
| `$d<n>=<value>` | 宏参数默认值 | moduleswitch:31-33 `$d2=FALSE / $d3=TRUE / $d4=UNSET` |
| `$<...$>` | 命令串内联 PML 求值 | `$<$!action$>`（edggeomdata.pmlfnc:69）；`$<DESIGN$> $<IGNORE$> $<NOWAIT$>`（compdate.pmlobj:1100）；`$<RUN$>/$<MODIFY$>/$<DELETE$>`（loadui.pmlfnc:74-80） |
| `$$` | 字面 $（转义） | deletemembers.pmlfnc:44 `'CE false $$<$$> true'`；commandmenu.pmlfnc:48 `$$r` / `$$r110`（跟踪等级）；syntaxhelp.pmlfrm:36 `'Syntax Help ($$H)'`（**$H = 语法帮助命令**）；group.pmlfrm:96 `'ADD $$!this.explorermember'` |
| `$!...` / `$!!...` | 命令行执行 PML 变量/函数 | moduleswitch `$!!<modExitAction>`、`$!nextModule.command $!readOnly` |
| `$P` | 命令行输出提示文本 | ttymode.pmlfnc:38 `$P Non Graphics Device (Appware will not be loaded).` |
| `$n` | COMPOSE 串内换行 | pmlforms.pmlfrm:824 `\|<$!dataTypes[$!i]$n>\|` |
| `$( ... $)` | 宏注释块定界 | runsynonym.pmlmac:1 `$(H ...` / `$)`；根目录 delmac.mac |
| `$.` | 宏结束符 | delmac.mac 末行 |
| 行尾 `$` | 续行符 | moduleswitch、admcontrol.pmlobj:749,793 |
| `$S1..` | 同义词形参 | appcntrl.pmlobj:1034 |
| `$_NAME` | 环境变量读取（VAR 侧） | getcurrentlist.pmlfnc:38 `var !numb ($_cdList_NAME)` |
| **未出现** | `$U $G $w $+ $- $*`、`$2..$9` 独立用法、`$d`（日期义） | 4 目录 0 命中 |

---

## 族 7：Draft 视口输出命令

**结论**：`W`（视口选择）、`REGI`、`DVELT/DVLEV` 在 4 目录 **0 文本命中**——Marine Drafting 的 Draft 运行时命令在 `PMLLIB\marinedrafting\`。4 目录内实测：

```pml
-- PROJ（工程属性）
var !mbchar PROJ MBCHAR                              -- limbo\functions\getmbchar.pmlfnc:45
var !lockResult PROJ LOCK AT $!qryLocId              -- global\forms\glbqrylockisol.pmlfrm:308
var !const CONST LINE PROJ $!lineStr ON PLANE $!pickedPlane.direction THROUGH $!pickedPlane.position
                                                     -- common\functions\lineonextrusion.pmlfnc:219
-- ADD / REM（Drawlist 增删）
ADD CE                                               -- common\functions\addtodrawlist.pmlfnc:25
'ADD $$!this.explorermember' / 'REM $$!this.explorermember'   -- common\forms\group.pmlfrm:96-97
对象化等价：!drawlist.add(!element)（gphdrawlists.pmlobj:746）、COLLECT ALL FROM DRAWLIST、!!gphViews.toDrawlist/fromDrawlist
-- PLOT 输出
'PLOT ' + !plotFile + ' ' + !data.ptyp + ' ' + !data.dTitle    -- compropdata.pmlobj:3333
view .plot at 1 1 plot（绘图预览 gadget）                       -- common\forms\plotview.pmlfrm:65
var !returnString UNITS / TEXTPOS DETAILPLOTS / PLOTDETAILDATA FILENAMES / PLOTDETAILDATA $!arg2 NUM / PLOTDETAILDATA $!arg2 ATTR $!arg3   -- limbo\functions\queryplotdetail.pmlfnc:34-42
-- Draft 模块宏调用
$m "%PDMSUI%/DRA/GEN/MSINGLEV" $<$> $<MAIN$>          -- appformcntrl.pmlobj:554
$M "%PDMSUI%/DRA/CLIB/UUPDATE" $<DESIGN$> $<IGNORE$> $<NOWAIT$>  -- compdate.pmlobj:1100
```

---

## 族 8：VAR 命令全集（含频次统计）

### 8.1 子命令频次（行首 var 过滤，common/global/admin/limbo）

| 子命令 | 合计 | 备注 |
|---|---|---|
| `COLLECT` | **110** | 变体最丰 |
| `COMPOSE` | **47** | 排版输出 |
| `EVAL` | **41** | admin 31 处集中 |
| `EVALUATE` | **26** | FOR ALL DB 变体 |
| `SPLIT` | **23** | CLAIMLIST/UNITS/EVAR... |
| `NUMBER` | 5 | COLOUR/PIN 语境 |
| `EXISTS` | 4 | `EXISTS $!item $!type $!access` |
| `UNIQUE` | 2 | 仅 `SORT UNIQUE ... DESCENDING` 形态 |
| `COUNT` | 1 | |
| **RANGE / LEN / PAIRS** | **0** | **不存在**——这些是 PML2 方法（!array.range()），不是文本 VAR 子命令 |

### 8.2 COLLECT 族全部变体

```pml
var !collection COLLECT ALL FROM DRAWLIST                    $* 无类型（aspcompcmd.pmlfrm:130）
var !gridSystems collect all GRIDSY                          $* 单类型（displaygrids.pmlfrm:188）
COLLECT ALL (CATA SPWL) / COLLECT ALL (MATW CASW RUNW CMPW CONW)   $* 多类型括号式
VAR !dbMasters COLLECT ALL WITH ( badref(EXTOWN) ) FROM !dbRefs    $* FROM 数组（dblist.pmlfrm:157）
COLLECT ALL SCTN WITH (abs(POSS[3] - POSE[3]) EQ DER LENGTH) FOR CE $* FOR 元素+表达式
COLLECT ALL WITH (TYPE NEQ 'SPST') FROM CLAIMLIST EXTRACT    $* CLAIMLIST 来源
COLLECT MEMBERS OF <el> WITH (...)                           $* compropdata.pmlobj:963 等 10 处
COLLECT ALL UDA WITH (...)                                   $* attdefinition.pmlobj:141
var !coll APPEND COLLECT ALL WITH ( $!rule ) FOR $!...       $* APPEND 前导修饰（chkstoreview.pmlfrm:1018）
VAR !localDbSet COLLECT ALL WITH ( type eq 'DBSET') for /*DS $* 世界简写 /*DS /*M
```

### 8.3 EVAL / EVALUATE 族

```pml
var !topTypes old eval type for all from !topDeleted         $* old 前导修饰（admextractcntrol:442）
var !names eval ( substring(NAME, 2) ) for all from !dbrefStrs  $* 括号表达式（qrydac.pmlfrm:261）
VAR !workExtOwners EVALUATE (REFNO OF EXTOWN) FOR ALL DB FOR $!userRefNo  $* FOR ALL DB（:347）
var !dbLocations EVALUATE (FULLNAME OF LOCRF of 1) FOR ALL FROM !dbs IGNORE ANY  $* IGNORE ANY 尾参
VAR !del EVAL ( DACDEL ) for ALL for $!<element> IGNORE ANY |true|  $* 带默认值
```

### 8.4 SPLIT / COMPOSE 族

```pml
var !claimlist SPLIT CLAIMLIST                                $* + extract deleted/OTHER/$!dbName
SPLIT DIRECTORY $!<binFileString> / SPLIT UNITS / SPLIT REPRESENTATION [PROFILE|CABLE] / SPLIT MEMB SPWL
VAR !elementText COMPOSE |ED| WIDTH 3 SPACES 1 |$!x| WIDTH 8  $* 基本排版
COMPOSE SPACE 0 |$!cdbList[$!i]| WIDTH 40 LEFT                $* L/R/C 对齐
VAR !listDtext COMPOSE COLUMN VALUES !arr1 WIDTH $!w SPACES 1 COLUMN VALUES !arr2   $* 多列
var !output compose sort !sort space 2 column values !descriptions ...              $* SORT（admcontrol.pmlobj:793）
var !returnArray COMPOSE $!submission（封装 composetext.pmlfnc:38）
```

### 8.5 类型化 VAR（读命令）全清单（limbo 为存量集中地）

```pml
var !user user                        -- moduleswitch:53
var !star STAR                        -- checkname.pmlfnc:54（星号名解析）
var !useName USENAME $!newName        -- checkname:122（名占用）
var !currentMdb MDB                   -- admextractcntrol:433
var !pinPosition PIN $!pinNumber POS / pin $!pinNumber dir
var !ppos POS PIN$!number WRT WORLD / var !pdir DIR PIN$!number WRT WORLD   -- posofpin/dirofpin
var !col COLOUR NUMBER GREY / COLOUR NUMBER $!<name> $!<table>
var !mbchar PROJ MBCHAR               -- getmbchar:45
var !lockResult PROJ LOCK AT $!qryLocId
var !data CLOCK DATE / MDB / TIME     -- limbo\functions\clock.pmlfnc:37-48
var !data EVAR '$!evar'               -- limbo evar.pmlfnc:38
var !data BANN NAME/STATUS/COPYRIGHT/COMPANY/SHORT / var !data DDL
var !file DIRECTORY "$!name" DIR/FILE/FULLNAME   -- limbo directory.pmlfnc:40-64
var !info FILE "$!filename" $!option  -- limbo findfile.pmlfnc:51
var !exists EXISTS $!item $!type $!access   -- limbo exists.pmlfnc:60
var !units UNITS                      -- limbo getunits.pmlfnc:33
var !ruleList RLIST / var !rule RULE OF $!rules[$!indx]
var !seg ID SEGMENT PPLINE NA/ANY THROUGH $!position VIA PLINE BOUND
var !z PLDIST PPLINE $!ppl THROUGH ... VIA PLINE BOUND   -- limbo poscalczdist.pmlfnc:76-82
var !shape PL CONN / var !ppl JUSL
var !startString PPLINE $!<pLine> OF $!<dbRef> NORMAL START WRT World / PROPORTION 0.5 WRT World / DISTANCE $!<z> FROM START OF $!<curve> WRT World   -- edgpline.pmlobj:270-436
var !volume LVOL OF $!<item> WRT $!<wrt> / var !volString VOL $!item
var !active LACR of /*GRO / var !dacError DACERR $!i of $!this.dbref
var !ruleQuery RULE of $!<attribute> / RULE of DESPARAM
var !worldRef refn of world / var !primaryAt LOCRF OF DBLOC 1
var !attrDummy DEPR ATTR OF OWNER / RDEP NOFF OF OWNER / DEPR RULE OF OWNER / DEPR WRTO OF OWNER   -- UDA 偏置（compropdata:5012-5024）
var !dist (DIST(LDPR DIST OF OWNER)) / var !numb ($_cdList_NAME)
```

### 8.6 CONSTRUCT 几何族（limbo 20+ 封装函数）

```pml
CONSTRUCT ANGLE $!posA TO $!posB TO $!posC / CONSTRUCT ANGLE $!dirA AND $!dirB / CONST ANGLE $!planeStr $!lineStr
CONSTRUCT DIRECTION $!startString TO $!endString / ORTHOGONAL $!dir1 AND $!dir2 / LINE $!line.direction THROUGH $!line.position / NORMAL $!plane
CONSTRUCT LINE JOIN $!from TO $!to / LINE $!dir THROUGH $!pos / LINE PROJECTION LINE $!direction THROUGH ... ON PLANE ...
CONSTRUCT PLANE THROUGH $!a AND $!b AND $!c / PLANE $!dir THROUGH $!pos [DISTANCE $!d] / PLANE UP THROUGH $!endPos
CONSTRUCT POSITION NEAREST/NEAR $!pos ON [LINE|PLANE] ... / INTERSECT LINE $!l1 LINE $!l2 / INTERSECT LINE $!l PLANE $!p / INTER $!line1 $!line2 / POSITION $!plane
CONSTRUCT DISTANCE $!from TO $!to
```
封装文件：limbo\functions\ 的 anglebetweenposs/consdirto/consplanethro/consposinter/consposplaneline/dirposdist/offsetplane/positiononline/positiononplane/linefromto/linetodir/planetovector/distancefromto 等 20+ 文件。

---

## 主要证据文件索引

- common\forms\lstclaim.pmlfrm（CLAIM/UNCLAIM 全族 + handle 码）
- common\objects\aidnumbers.pmlobj / aidconstructors.pmlobj / aidmodify.pmlobj / namopt.pmlobj / gphviews.pmlobj / gphdrawlists.pmlobj
- common\functions\gphalwaysrotate.pmlfnc / checkname.pmlfnc / writesessionfile.pmlfnc
- limbo\functions\moduleswitch.pmlfnc（$ 命令 + 模块切换 + QUIT/SAVEWORK）；limbo\functions\ 下 cons*/aid*/clock/module/evar/exists/queryplotdetail 等 40+ 旧式命令封装
- admin\forms\admdb.pmlfrm / admextract.pmlfrm / admwork.pmlfrm（CREATE/CHANGE ... CLAIM DDL）
- `E:\AVEVA\Marine\OH12.1.SP4\delmac.mac`（$() 注释块、LOCK/UNLOCK、DELETE MODULE n、$. 结束符）
