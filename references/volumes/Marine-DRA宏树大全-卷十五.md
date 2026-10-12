# Marine PDMSUI-DRA 宏树大全·卷十五（穷举级·源码实证）

> 来源：`E:\AVEVA\Marine\OH12.1.SP4\PDMSUI\DRA\` 全部 30 子目录 1456 文件（三条正则全树扫描 + 20+ 关键宏精读），PML1 前缀约定：f*=Form / i*=Init / m*=Method / x*=Execution / r*=Report / u*=Utility / d*=dbar。
> 定位：DRAFT 模块 UI 宏（用户在 DRAFT 里点每个按钮背后下发的命令），补 PMLLIB 十四卷（进程内逻辑）之外的 PDMSUI 侧。

## 1. PDMSUI 全树覆盖图（9704 文件）

| topdir | 文件数 | 状态 |
|---|---|---|
| des | 6228 | 部分编目（设计 UI） |
| **DRA** | **1456** | **本卷编目** |
| icons | 515 | 位图资源 |
| clib | 393 | 未编目（Draft 公共库，本卷 clib 子目录覆盖其 DRA 用量） |
| plots | 317 | 未编目（按专业笔表/出图模板） |
| **iso** | 331 | 已编目（卷六） |
| **cat** | 294 | 已编目（卷四） |
| reports 48 / intf 44 / mon 28 / spl 12 / adm 4 / data 5 / hdes 5 / lex 4 / mdra 8 / diagrams 3 / smm 3 / tags 3 / opsys 3 | ~140 | 未编目（小体量） |

## 2. DRA 树结构（30 子目录）

gen 476（General：图纸/视图/图层/注释/出图/DXF）· edraught 182（2D 图元 CALLEDR）· clib 121（CALLIB 公共库）· symb 110（CALLDRS 标签）· adpgdp 84（CALLADPG 自动标注）· dim 81（CALLDRD 尺寸）· supp 56（CALLSUP Marine 支撑）· ADDINS 24 · editor 37（CALLDRE AutoDRAFT）· adpcore 38（CALLADPC）· libmiso 35（CALLMISO 符号库）· libmshe 21 / libmlab 19 / libmrep 18 / libmsym 14 / libmgen 13 / libmtag 6 / libmdrl 6 / libmsty 10 / Libmaba 2（各库管理 CALLM*）· data 14 · track 13（CALLTRACK 属性跟踪）· plot 17 · upgrade 12 · admin 19（CALLDRA 启动链）· adpsched 8 · core 10（CALLCORE 捕捉）· dflts 6 · adptag 4。

**CALL\* 分派频次**（全树实测）：CALLDRG 705、CALLIBM 521、CALLADPC 290、CALLIB 282、CALLSUP 230、CALLEDR 163、CALLDRS 112、CALLADPG 100、CALLDRD 62、CALLMREP 34、CALLDRE 26、CALLMISO 21、CALLDRA 16、CALLCORE 16、CALLTRACK 12、其余 CALLM*/CALLIB* 各 1-11。

**NEW 对象频次 Top**（排除 data）：ADDE 4126、TEXP 3242、STRA 3209、VNOT 1118、TEXTPRIMITIVE 633、SYTM 603、DPPT 589、SYMB 542、SLAB 438、MRKP 401、LAYE 373、HSTYLE 330、NOTE 276、HRULE 237、RECT 236、CIRC 204、DPOI 202、RRUL 181、LDIM 147、HRST 132、STRAIGHT 123、IDLI 85、LIBY 81、RPLB 71、ARC 62、TRLB 56、VIEW 55、DLLB 54、PLLB 53、RRST 53、STYL 50、BACK 49、DRWG 47、SHEE 47、OLAY 39、VSEC 38、TABL 36、FPLA 36、VRTX 31、TAGR 29。

---

## 3. 图纸/视图/图层链（gen）

**新建图纸标准库挂接**（gen\udrwgcr:27-37）：
```pml
NEW LIBY $!NAME/LIBY
NEW DLLB $!NAME/DRAWLIST
NEW IDLI $!NAME/DRAWLIST/DRWG
NEW TRLB $!NAME/TAGRULE
$!NAME
IDLN $!NAME/DRAWLIST/DRWG
```

**新建视图全流程**（gen\uviewcr:35-105）：`VRATIO 3inch 1'`（英制比例）→ `SIZE $!XSIZE $!YSIZE` + `LFRAME TRUE` → `var !VLIM SPLIT VLIMITS` + `:CDLIMITS |...$!FRU...$!TOU|`（14 参限界写回）→ DRWG 导航（handle (41,222)(2,111)）→ 补建 LIBY/DLLB/IDLI/TRLB → `NEW PLLB $!NAME/PLANES` → 自动建层循环（`var list _CDRLAYCREATE_LAYERLIST SELECT $!X exit` → `NEW LAYE / NAME $!NAME$n/$!SUFFIX` → `CALLDRG USETLAYPRP $<$!PURP$>`）。

**FCREATE 创建协议**（卷二未载）：`CALLIBM FCREATE DRWG NO $<SHOW _CDRDRWG$> $!REF`（xdrwg:39）、FCREATE REGI（xregi:45）、FCREATE VIEW 正交/用户（xview:64/66）；修改模式 `!!draSwitchToPadd()` → `ID VIEW @` + (61,528)。

**Scrap 临时视图**（gen\mshspla:41-111）：`NEW SHEE */SCRAP` → `NEW VIEW */VIEW` → `COPY $!VNAME` → 成员循环剔除非 VSEC（handle (41,66)(2,113)）→ `DIR $!DIR / VTYPE WIRELINE / LFRAME TRUE / AUTO` → `CALLIBM UUPDATE DESIGN`。

**详图 Detail View**（gen\mdetview:206-274）：`NEW LAYE $!viewName/DETAILS` → `$m "%PDMSDFLTS%/DRA-LOC-LAYER"`（伪属性级联）→ `PURP CDTS` → `NEW VNOT */$_CDRDETVIEW_DETREF` → 形状采集 `NEW CIRC DEF @` / `NEW RECT ASDEF @`（(61,528) 回滚 DELETE VNOT）→ `HIGHLIGHT */<detref> in _CDRCADCGA1_N1`。

**图层管理**（gen\mlayer:26-91,135-143）：建层 `NEW LAYE` → `NAME`（handle (41,12) 重名）→ **PURP A–Z 后缀自动去重**（`do !c values A..Z: PURP $!purp$!c`，handle (64,12)(64,13)(2,21) 保留字）→ `LVIS` → 删除 `UNNAME` → `DELETE LAYE`；改层遇 TAG 阻碍 → `SORF =0/0`（handle (64,288)(2,21)）→ DELETE 重试。

---

## 4. 尺寸标注族（dim + adpgdp）——15 样式派生的真实实现

**LDIM**（dim\xcrldim:27-96）：
```pml
var !right VIEWDIR RIGHT / LEFT / UP / DOWN      $* 方向查询
NEW LDIM DTANG $!!CDLDTANG PTANG $!!CDLPTANG
  样式1/6/11: DIR $!dirVal + LCHAIN TRUE
  样式2/7/12: DIR + LCHAIN FALSE
  样式3/8/13: DIR + PLDIR -90 + LCHAIN FALSE
  样式4/9/14: DIR + LCHAIN FALSE + TRUNCATE $!!CDDIMTRUNC.IMP|.MET
  样式5/10/15: DIR + PLDIR -90 + TRUNCATE
```
**ADIM**（xcradim:26-66）：`NEW ADIM` → `PROMPT LOAD ESCAPE |Identify the radial point|` → `ON IDP @`（(61,528) → DELETE ADIM 回滚）→ `LCHAIN` + `SENSE CLOCKWISE|ANTICLOCKWISE` + `TRUNCATE`。

**RDIM 6 样式**（xcrrdim:68-136）：
```pml
NEW RDIM DFLAG RAD DDEG 45 ON $!from @ DTANG $!!CDPRDTANG
  handle (61,528) → return; elsehandle (64,377) → error + DELETE RDIM
DMTX |$!!CDDIMRAD.RAD$n#DIM|                    $* 模板文本(#DIM=代码字)
样式1: DSTYLE DIMLINE  DTFLAG MID    DTUL OFF   DTRAD 0        DTOF 0 0
样式2: DSTYLE DIMLINE  DTFLAG CIRC   DTUL ON    DTRAD 2*TSIZE  DTOF 0 0
样式3: DSTYLE EXTERNAL DTFLAG CIRC   DTUL ON    DTRAD 2*TSIZE  DTOF 0 0
样式4: DSTYLE LEAD     DTFLAG CENTRE DTUL ON    DTRAD 0        DTOF 1*TSIZE 0
样式5/6: DSTYLE LEAD   DTFLAG CIRC   DTUL ON    DTRAD ±2*TSIZE DTOF 0 0
$m "%PDMSDFLTS%/DRA-DIM-RDIM"                   $* 伪属性级联
```
缩写变体：`DSTYLE EXT`（xcrddim:82）、`DTFLAG CENT`、`DTANG HORIZ|STAND`（xcrpdim:79-99）；PDIM：`NEW PDIM DFLAG DIAM|RAD PCEN @ PCIRC @` + `DDEG TRUE`（xcrpdim:63-75）。

**标注编辑动词**：`GAP AT @ / GAP @ / GAP DELETE @ / GAP DELETE ALL`（dim\mgap:39-68）、`DPOS @`、`DTOFF DEF|@`、`DDEG @/TRUE`、`PKDI 0|1`（mdimep:329-337）、`SORT DIM`、`SENSE`。
**自动标注引擎**：adpgdp\udimmain/udimcomp/udimbranfr/udimbranin/usortdim/usortlev1/usorttyp1 + dim\mautold/mautoad；自动标注层 `NEW LDIM */GDP1/Dims/$!SIDE`（uanotyp1:94）。

---

## 5. 文本/标签族（symb + libmlab）

**GLAB**（symb\mglab:16-63）：
```pml
$_LAYER → NEW GLAB
BTEX |$_GLAB1|                        $* 1~3 行拼接
HANDLE (64,384) → DELETE GLAB + RETURN ERROR
PROMPT OFF / PROMPT LOAD ESCAPE |Identify Design item with the cursors| / ON ID @
HANDLE (61,528) → DELETE GLAB + "Label Creation aborted"
```
变体：`NEW GLAB COPY <slab>`（mmglabed:199）、**代码字取属性** `new GLAB BTEX |#NAME(C2:)| ON ID <type> @`（mmglabed:282）。

**SLAB**（symb\mlabel:228-273）：未开库则 `CALLDRS USHOWLIB SLAB` → `PROMPT LOAD ESCAPE |Identify library label required| / ID SYTM TXTM @` → `CALLIBM UGETLAYE LAYE` → `new SLAB TMRF $!TMPLT ON ID $!IDTYPE @`；copy 式 `new SLAB copy $_CDRLABEL_USERDATA`（handle (64,382) codeword 不可访问）；逻辑端 `PKDI lt 0.5 → PKDI 0 else PKDI 1`（handle (64,285) PPLINE 不存在 → PKEY NA → PKEY 0）。
变体：`NEW SLAB ON PPLINE NA OF <elem>`（supp\usteeldim:126）、`NEW SLAB TMRF X XYSCALE X X ATEX |...|`（gen\ubldslope:105）。

**VNOT/NOTE**（gen\xcrnote:22-38）：建立能力探测 `CALLIB RCREATE NOTE|VNOT false` 读 !!CDRTNSTATUS → `CALLIBM FCREATE VNOT NO $<$>`；变体 `NEW VNOT COPY PREV`（mnvnot:51）、`NEW VNOT ON <elem>`、`NEW VNOT *X LVIS FALSE`（adpsched\mtable:184）。

---

## 6. libmiso：Isodraft 符号库 UI 与 SKEY→ISOTM 翻译器

表单：fisotrans（Import Isodraft Symbols）/ fisoprim / fisosylb / fisolbatt / fisosymf / fisosymt。
回调链（fisotrans:38,74）：`CALLIB XFILEMOTIF $<%PDMSUSER%$> $<callmiso MISOSOPN$> $<Isodraft Symbol File$> $<EXIST$> $<true$>`（文件选择）→ `callmiso MISOTRANS $$_filename $$<$$_lname$$> ...`。

**翻译主宏 misotrans（313 行）**：`openfile read` → 无库 `NEW LIBY`（handle (2,109)）→ 逐行 `readfile`（**handle (41,325) 文件尾 break**——全 DRA 最高频码 1050 处）→ SKEY 块 PEN 命令对拆分 → 页面排版越界换页 → `NEW ISOLB`（重名后缀探测）→ `callmiso MTRANSSKEY` 建 ISOTM → `NEW MRKP / PURP ARRI / ORIG X Y` + 逐笔 MTRANSPEN + `PURP LEAV`。

**SKEY 词→ISOTM 属性映射**（mtransskey:37-108）：`SCALE→SCAL`、`ORIENTATION→ORIN(前4字符)`、`FLOW ON/OFF→FLWA TRUE/FALSE`、`FILL→FILL`、`DIMENSION→DIME`、`INSULATION ONLY→INSL TRUE+TRCG FALSE`、`TRACE ONLY→TRCG TRUE+INSL FALSE`、`SPINDLE ON/OFF/n→SPIN DEFAULT|unset|n`；`NEW ISOTM → NAME /$!SKey → SKEY/BKEY(6字符填充) → XYPO X $3 Y $4`（handle (64,617) 非法符号键）。

---

## 7. ADDINS 注册文件（24 个全读）

键值全集：`name / title / directory / showOnMenu / status(USER|ADMIN) / object / menu / synonym / gadgets / type(GDP|DIM...) / libytype(SYLB LALB ISOLB BACK OVER SHTMPL) / helpAlias / startupModify / modulestartup`。
代表：gen=APPDRAGEN/CALLDRG（gadgets 3, GDP）、dim=CALLDRD（type DIM, 无 object 仅为保同义词）、libmiso=APPLIBMISO（ADMIN, ISOLB）、isoadp=APPISOADP（ShowOnMenu FALSE）、avevamarine=APPDRAAVEVAMARINE（startupModify: ADPCORE:!!appDraStartup()）、assemblyadp=ASSEMBLYDRAWING、apppfmdwg=APPPFDWG、**finaldesign 整体被注释停用**。
`dflts\applications` 旧双轨注册（Form `_CDRxxxAPP` + `CALLIBM XAPPLIC`）；`dflts\dra-genadp-toolbar` 工具栏文本格式：`NEW_GROUP <descr>\<pixmap> [SAME_ROW]` + `<label>\<call>` + `END_OF_FILE`。

---

## 8. 出图/更新（gen + adpgdp + editor）

```pml
-- 层级校验链（xplotit:32-56）：VIEW→SHEE→BACK→OVER→SYLB→ISOLB→LALB→SHTMPL
PLOT $_TYPE "$!FILE" $!plotOptions OVER                                  -- mplotit:145
PLOT $_TYPE FILE PDF "$!FILE" '$!optString$n, VIEW' $!plotOptions OVERWRITE  -- :205
PLOT $_TYPE FILE PRINT '$!optString' $!plotOptions                       -- :398
PLOT $_TYPE DXF "$_DIRECTORY/$_FILE" $_HEADER $_ZCOORD $!SCALEUP $!SIZE $!CUTM $!BORDER $!FRAME [OVER]  -- mdxfit:163（DXF 经 PLOT 直出）
PLOT SHEET DXF /$!dir/$!fName $_header $_zcoord CUTM OFF [OVER]          -- editor\macad:106
-- 更新链（adpgdp\ugdpupdt）：UPDATE DESIGN IGNORE(:71) → CALLADPG UDIMMAIN → CALLADPS UTABLE UPDATE
--   → CALLADPT MTAGGING UPDATE → UPDATE ANNO(:210)
--   标注层自动补建：NEW LAYER */TAGG/x → USETLAYPRP → FONT TEMP / CHEI TEMP /
--   TXCOLOUR TEMPLATE / LFCOLOUR TEMPLATE LFSTYLE TEMPLATE → TRSF $!TRST(:172-185)
OUTPUTDRAWINGS OFF                                                        -- admin\start:30
```
**2D 图元总入口**（edraught\xcrprim:75-142）：SSTRA/MSTRA/HVSTRA/CLOUD/OUTL/VRTX/CIRCENRAD/CIRCDIAM/ARC3PNT/ELLI3PNT/RECTDIAG/ETRIBASE/DMND3PNT/HEXCENRAD/TABLEDIAG/MRKP 全走 `CALLEDR X*`；画前置检 `!!fmsys.OKCurfnView('G2D')` + `!!draSetLayer('', 'DRA')`。
**图层智能选择**（clib\usellayer:50-89）：`collect all LAYE with (subst(PURP,1,3) eq ...)` → `!!draGetApplication(PURP前3)` → `!!draFilterLayers(...)`——**PURP 三码前缀约定**（DIMA/LABA/NOTA/TAGA/SCHD...）。

---

## 9. 与卷二的差集（37 增补点，全部带路径行号）

**对象/结构**：NEW BACK/OVER（背页覆盖层）、NEW VSEC（断面）、NEW OLAY、NEW FPLA/SPLA/PPLA（参考面）、NEW TAGR、NEW LALB/SHLB/RPLB、**风格库族 HSTYLE 330/HRST 132/RRST 53/STYL 50/TRST 16**（卷二空白）、FCREATE 创建协议。
**标注/标签**：DSTYLE EXTERNAL(EXT)、DTFLAG CENTRE(CENT)、**GAP 四动词族**（卷二全缺）、DDEG TRUE、DMTX `$n#DIM` 模板、PKDI/PKEY 逻辑端、SLAB ON PPLINE、XYSCALE、GLAB COPY + `BTEX |#NAME(C2:)|` 代码字取属性、VNOT COPY PREV、CIRC DEF @ / RECT ASDEF @。
**视图/导航**：SET/END、UNNAME、SORF =0/0、HIGHLIGHT in pane、VIEWDIR 四向查询、VRATIO、VLIMITS+:CDLIMITS 14 参、VTYPE WIRELINE、**交互输入协议 PROMPT OFF/LOAD ESCAPE + ON ID @ + (61,528)**（卷二完全未覆盖）。
**出图/更新**：PLOT DXF 直出、PLOT FILE PDF ', VIEW' OVERWRITE、UPDATE DESIGN IGNORE、OUTPUTDRAWINGS OFF、属性 TEMP/TEMPLATE 值、TRSF 挂 Tagging Rule。
**机制**：%PDMSDFLTS% 伪属性级联（$m "%PDMSDFLTS%/DRA-DIM-RDIM"）、CALLIB RCREATE 能力探测、!!draSwitchToPadd/!!draGetApplication/!!draFilterLayers、PURP 三码前缀 + A–Z 去重。
**反向勘误（卷二来源标注）**：DESADD/NEW AXESYM/SPAN TO CLOSE/LIEXEC/(43,364) 等源自 PMLLIB\pipetappingdrwg.pmlobj 而非 PDMSUI 树。

## 10. DRA 特有错误码（补入错误码速查 §5）

| 码 | 次数 | 语义 |
|---|---|---|
| (41,325) | 1050 | readfile 文件尾（misotrans:97——循环退出的标准写法） |
| (2,441) | 494 | DB 引用/导航失败 |
| (64,153)/(64,347) | 392/391 | PML 表单/求值错误 |
| (61,528) | 356 | 交互 ID 被 ESC 中断 |
| (41,222)（+2,111 组合） | 135/166 | 当前层不可达目标 |
| (2,109)/(41,69) | 89/44 | 名称/ID 未定义 |
| (64,382) | 54 | codeword 不可访问 |
| (64,288)+(2,21) | 组合 | 删除受阻 → 先 SORF =0/0 |
| (64,12)/(64,13) | 组合 | PURP 非法/保留字 |
| (64,384) | — | GLAB 建立失败 |
| (64,617) | — | 非法符号键 SKEY/BKEY |
| (2,470) | 8 | 不在 SHEE/BACK/OVER 下 |
| (41,221) | 5 | 背页引用原件不存在 |
| (64,377) | 3 | 元件不适用该标注 |
| (39,8)/(72,142) | 8/2 | 资源环境/升级 |
