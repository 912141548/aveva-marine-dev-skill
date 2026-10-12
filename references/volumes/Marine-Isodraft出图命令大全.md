# Marine Isodraft 轴测图命令大全（穷举级·源码实证）

> 来源：PDMSUI\iso\ 全部 331 宏（676 条命令实例穷举提取）+ PMLLIB\isodraft\（11 表单/5 对象/全部函数）+ PMLLIB\isometricadp\（26 表单/35 对象/48 函数/15 用户函数）+ design\isdpreview 系列 + pipefabricationmanager 出图链 + 根级配置文件。
> 适用：AVEVA Marine (PDMS 系) 12.1 SP4。管道轴测图（Isometric）生成/选项/批处理/输出全收录。
> 先行结论：安装根下不存在 `marine\`、`marineadm\` 目录；iso 配置集中在 `PDMSUI\iso\`、`PMLLIB\isodraft\`、`PMLLIB\isometricadp\`、`template_project\_proj_mar\def\` 与根下 `isovir.dat`。`TXPR` 关键字不落盘为文本（ISOD 库内部记录类型）。

---

## 1. 模块进入与状态查询

### 1.1 模块进入/退出

| 命令 | 出处 |
|---|---|
| `ISODRAFT`（TTY 宏一行进入） | pipefabricationmanager\draft\functions\pfPipeMakeIsoView.pmlfnc:66 |
| `ISODRAFTMODE`（Design/Spooler 内进入） | design\functions\isdruniso.pmlfnc:57,68；pfIsoDrawingManager.pmlobj:50 |
| `EXIT` / `FINISH` | isdruniso:62,73 / pfPipeMakeIsoView:89 |
| `CREATE TEAM ISOADMIN DESC 'Team used for ISODRAFT Administration'`（安装） | admin\functions\installcadc.pmlfnc:161 |
| 消息模块号 148 | common\objects\msgmodules.pmlobj:100 `!this.isodraft = 148` |

### 1.2 状态查询命令（var ... 语法，isdpreviewisocontrol.pmlobj）

```pml
var !status isodraw status                                    -- :498
var !isoCountTemp isodraw number                              -- :525  出图计数
var !plotFile isodraw plotfile $!plot filename                -- :539
var !drawingType isodraw plotfile $!plot type                 -- :544  PLOT/BOTH/PDF
var !unusedNumberOfDrawings isodraw plotfile $!plot number    -- :555
var !pipeName isodraw plotfile $!plot drawing 1 title         -- :557
var !sheet isodraw plotfile $!plot drawing 1 sheet            -- :558
var !plotStatus isodraw plotfile $!plot drawing 1 status      -- :561
```
其它：`var !BOLTF boltfile`（gen\mstdiso:106）、`var !UNIT output units`（opt\mdime:40）、`var !ISOTYPE1 ISOTYPE`（mstdiso:147）、`var !textdp TEXTPOS DETAILPLOTS`（mstdiso:152）。

---

## 2. ISODRAFT 命令全集（按动词）

### 2.1 出图核心

```pml
DETAIL $!item                          $* gen\mstdiso:252/334
detail isodrawing $!NAME               $* gen\mbatch:110-115
detail PIPE /$!pipeName                $* gen\mbatch:138
detail all                             $* gen\mbatch:167 / gen\udeta:19(detail empty)
detail all as /$!sysName               $* gen\mbatch:194（系统 iso）
detail all as $!EQUI '$!TITLE'         $* gen\mbatch:218（equipment 前缀）
DETAIL $!TYPE $!NAME                   $* gen\mstdiso:205,289
detail SPOOL $!allspool[$!i]           $* gen\mstdiso:196
DETAIL /$!PNAME                        $* caps\batiso:165,198
add $!addText / add $!branch           $* gen\mstdiso:104,133,370
drawing $!COUNT                        $* gen\mstdiso:179
FILE "$!FILES$!NAME"                   $* gen\xbatchiso:104；caps\batiso:125（+SINGLE 后缀）
FILE /plot single                      $* gen\mcreopt:112
FILE AND DXF "..." SINGLE              $* pfPipeMakeOverlyingView.pmlfnc:193
HYPERPLANT ON / OFF                    $* gen\xbatchiso:107,199
monitor                                $* gen\mbatch:225（批处理宏收尾）
boltreport all [with position]         $* gen\mstdiso:136
process transferfile "$!filename"      $* gen\mtrans:38
recreate options "<path>" overwrite    $* gen\usavopt:31,40,43
options default                        $* gen\icomments:26 等
$M "<options 文件>"                    $* gen\mbatch:85-89（PROJ %$:ISODIR$:%/APPW %PDMSDFLTS%/本地）
detailTypes = 'PIPE BRAN PSLIST PSPOOL ZONE GROU DRAWI ISODEP ISOREG SPLDRG SPOOL FIELD'  $* mstdiso:49 合法类型表
```

### 2.2 材料表选项（opt\mmatl OK 回调，全部命令词）

```pml
materiallist partnumbers $_PERSPOOL $_PARTNO charheight $_CHAR lspacing $_LSPA   -- :33
materiallist $_DRWG $_DUMM SINGLE                                                -- :34-39
materiallist code $_CODE $_DESC                                                  -- :40
materiallist $_MATLPOS [ON]                                                      -- :41-45
equipmentnumbering $_EQUI                                                        -- :48
dtext $_DTEX / mtext $_MTEX                                                      -- :51,54
delimiter $_DELI                                                                 -- :57
itemcode from spref | itemcode from $_UDA                                        -- :61-63
itemcode for supports from $_UDA|spref|$_ISUPP                                   -- :72-78（handle (47,15)）
itemcode $_ITEM / itemcode length $_LENG                                         -- :82,85
bolting off | bolting units metimp|metric|imperial                               -- :88-98
bolt length description on [prefix|append|insert at |text|]                      -- :102-114
bolt length itemcode [append|insert at |text|]                                   -- :118-126
cuttinglist off | cuttinglist $_CUTT itemcodes $_CUTTITEM endpreparations $_CUTTEND  -- :130-133
ppiece off | ppiece on [CUT|TAG] | ppiece on after x |delim| [CUT|TAG]           -- :137-151
looseflangeallowance $_LOOS                                                      -- :158
spoolnumbers off|fromdb|on|perdrawing [+ prefix fromdb|prefix |text|]            -- :161-180
psname off | psname on [after x |delim|]                                         -- :184-191
matlistfilename "<file>" $_PERPLOT with $_LINES lines                            -- :197-202
```

### 2.3 输出文件选项（opt\moutput）

```pml
matcontrol "<file>" [extended] | matcontrol off                                  -- :27-32
cutpipelistfile "<file>" [formatfile "<fmt>"] | cutpipelistfile off              -- :46-51
cllengthfile [insulation] "<file>" | cllengthfile off                            -- :62-67
supportfilename "<file>" | supportfilename off                                   -- :73-78
boltfile "<file>" with N lines | boltfile off                                    -- :84-89
transferfilename "<file>" | transferfilename off                                 -- :95-100
symbolfilename "<file>" write|readonly | symbolfilename off                      -- :107-147
```

### 2.4 标注/坐标/轴/键图（opt\manno、madmin、mdime、msheet、mweldopt、mposi1/2）

```pml
-- anno（标注）
charheight $_CHAR                                                   -- :25
jointnumbers $_JOINT / contjoints $_CONTJOINTS                      -- :28-29
contnotes $_CONT descriptions $_TCONT [$_CONTUDA]                   -- :33,35
contsheets $_CONTSH contudeftext |$_CONSTR|                         -- :40
pbendnumbers $_PBENDNUM                                             -- :74
messageaccuracy radial $_RADIAL | iterations $_ITERATIONS           -- :77,81
itemcode FILT|INST|PCOM|TRAP|VALV|VENT default|on|off               -- :107-146
coordinates $_PIPE at pipe / $_NOZZ at nozzle / $_OPEN at open /
  $_CLOS at close / $_VENT at vent / $_DRAN at dran / $_SHEE at shee /
  $_MISC at miscellaneous                                           -- :164-171
axes world | axes $!AXNAME                                          -- :176,195
keys $!NUMB [ |$!VALUE| ]                                           -- :209-211
-- admin
messagefilename "<f>" $_MESSMODE | "<dir>/<f>"                      -- :178-180
hyperplant $_HYPERPLANT                                             -- :184
mark detail $_MDEta / mark revision $_MREV / mark ignore $_MIGNO    -- :200-202
wastage area 1..9 $_WAST1..9                                        -- :224-232
-- mdime（尺寸）
units $_UNIT [PREFIXBOREUNITS]                                      -- :29-31
precision bores $_PRECIBORES                                        -- :49
tolerance offset $_TOLOFF / tolerance angle $_TOLANG                -- :66,73
dimensions off                                                      -- :77
dimensions composite off|on                                         -- :80-82
dimensions overall off|on|centreline [only]|critical [only]         -- :87-100
dimensions support                                                  -- :110,115
dimensions hangers $_HANG strings                                   -- :120
dimdist $_DIMD | dimdist overall $_OVED | dimdist support $_SUPD    -- :144-146
dimlabels in | dimlabels above                                      -- :150-152
dimall $_DIMAWD                                                     -- :156
fallinglines $_FALL $_LIMIT accuracylevel $_ACCU                    -- :159
angleaccuracy $_ANGLE                                               -- :162
fallskews $_FSKEW on | fallskews $_FSKEW off $_FNUMB                -- :169-171
skewbox full | skewbox triangle $!NSTD standout $_STAND hatch $!HATCH $!PARTIAL $!TAGS  -- :176,201
overallskews $_OVERSK / zerolengthskews $_ZERO                      -- :205,208
weldangles off | weldangles on weldangmin $_MINWA                   -- :212-214
refdimensions $_REFD / elevation $_ELEV                             -- :218,224
bendradius off|distance|standard $_BSTAN|diameters|outdiam [standard $_BSTAN]  -- :228-260
-- msheet（图面）
size height W width H | size $_SIZE | size A$_SIZE                  -- :26-30
stackingarrangement $_STACKN $_STACKD                               -- :34
iso $_ISO [box]                                                     -- :38-40
cutmarks $_CUTM / continuationsymbols $_CONT                        -- :54,57
underlay off all | underlay "<file>" $!COUNT                        -- :60-78（%$:ISODIR$:%/UND/）
insulationcontrol $_INSU / tracingcontrol $_TRAC                    -- :83-84
specbreak $_SPECB dimensiontype specchanges $_SPECC                 -- :87
flowarrows $_FLOW | flowarrows inline off|scale $_FSCALE [automatic] -- :90-105
margin left R right R top R bottom R                                -- :121
reserve $_RES / reserve materiallist $_MRES                         -- :130-131
linethickness $_LINE / picturescale $_PICT                          -- :137,140
-- mweldopt（焊缝编号）
weldnumbers off                                                     -- :38
weldnumbers charheight S $_WELDSUNIT M F $!WACRS $!BOX $!WADDT $!WSTYL $!WBMAX  -- :67
contwelds $_WCONT / weldid $_WELDI / weldtype $_WELDT               -- :71-77
textpos weldtable off | textpos weldtable $!SORTBY corner C at x X y Y char height H | fileonly  -- :81-94
textpos weldtable add column N heading |T| FILL width W             -- :133-148
weldtablefilename "<f>" with N lines | off                          -- :159-164
-- mposi1/2（自定义文本位置）
textpos attribute off / textpos systemattribute off / TEXTPOS SYSTEMNAME OFF    -- :25,45,48
textposition $!ATT at x X y Y charheight H angle A                  -- :40
textposition system $!ATT at x X y Y charheight H angle A           -- :63
textposition |$!TEXT| at x X y Y charheight H angle A [BOXED]       -- mposi2:43-45
-- 其它
titleblock $!NUMB ['$!TITLETEXT']                                   -- opt\utitle:42-44
spoolnumbers update ce                                              -- caps\ulabunits:182
trace off / mark ignore on / units imperial                         -- caps\ucutctest:25-47
UNITS <units>                                                       -- editor\udxfunits:18
```

### 2.5 表格定义

```pml
-- mmatlopt（材料表列定义）
materiallist tabledefinition off                                    -- :19
materiallist gridlines OFF|ON                                       -- :49-51
materiallist tabledefinition column N $!ATT in $!UNIT with width W  -- :80
materiallist tabledefinition column N $!ATT $!REMARKS with width W  -- :82
materiallist tabledefinition column N other heading |$!TITLE| with width W  -- :140
materiallist tabledefinition column N other|noheading with width W  -- :143,172,175
-- mhistory（修订表）
textpos revisiontable off | ... corner C at x X y Y char height H   -- :25-27
textpos revisiontable add column N heading |$!TITLE| $!FILL width W -- :65-80
-- mbendf（弯管表）
textpos bendtable corner C at x X y Y char height H | fileonly | off -- :26-31
bendtablefilename "<f>" | off                                       -- :37-42
-- 实战例（pfPipeMakeOverlyingView.pmlfnc:224-230）
MaterialList TableDefinition Column 1 PARTNUMBER with Width 3 ...
  Column 6 REMARKS and ANGL on ELBO with Width 12
  Column 7 OTHER Heading 'SPOOLNAME' PCRFA with Width 50
```

### 2.6 Compipe / CAPS

```pml
compipefile "<f>" | off                                             -- opt\mcompipe:39-45
compipe mto $_CMTO itemcodes $_CITEM descriptions $_CDESC supports $_CSUPP  -- :43
-- CAPS 系数记录关键字（caps\capscoeffs 等）：COFORMAT COUNITS WELDCOEFF REINFORCECOEFF
--   SLIPWELDCOEFF SEALWELDCOEFF MITRECOEFF CUTCOEFF XRAYCOEFF FLARECOEFF BEVELCOEFF
--   PULLBENDCOEFF THREADCOEFF MISCCOEFF SUPPORTCOEFF FABREDCOEFF CLEANCOEFF2..5
--   TESTCOEFF2..5 SEALCOEFF2..5 DPFN TUBESPLITS ...（CALLCAPS <macro> 调用，123 处）
```

### 2.7 支吊架符号宏（opt\supp_symbs）

```pml
SKEY '10HG' '01HG'
PEN U5 5 PEN U0 10 PEN D10 0 PEN D9.7 0 PEN D0 9.7 PEN U5 5
ENDSKEY
ATEXT 381 / ATEXT 382 |PLAIN END| / ATEXT 383 |BEVEL END| / ATEXT 384 |THREAD| ...
```

---

## 3. 图纸生成流程（五种路径）

### 3.1 交互式（gen\mstdiso OK 回调节选）

```pml
$!CE                                                -- :60
pipe / handle (41,222) (2,111)                      -- :52-56 BRAN 成员上溯 PIPE
if (|$_DETAIL| eq |batch|) then → gen\mbatch        -- :64
CALLIG RPREDET STD                                  -- :72 预处理
add $!TYPE $!NAME                                   -- :104
$_DETAIL isodrawing $!NAME / $_DETAIL $!TYPE $!NAME / $_DETAIL all  -- :168/205/372
MATCONTROL OFF / PREPROCESS 1 OFF / POSTPROCESS 1 OFF               -- :256-258
CALLIG RDISPLAY / CALLIG RLIST                      -- :385-387
-- VPRM: handle 6=MTO 线号/区域未设 7=多工艺线 8=多工艺区（:235-249）
```

### 3.2 批处理宏生成与执行（gen\mbatch → gen\xbatchiso）

```pml
writefile $!TOKEN |Isodraft|                        -- :80
writefile $!TOKEN |options default|                 -- :83
writefile $!TOKEN |$$M "%$:ISODIR$:%/$!SORS/$!FILE"|   -- :85（PROJ）/ %PDMSDFLTS%（:87）/ 本地 $$m"$!FILE"（:89）
writefile $!TOKEN |monitor| / |$$.|                 -- :225-226
closefile $!TOKEN keep
-- TTY 执行（xbatchiso）
$m "$!OPTIONS"                                      -- :75
FILE "$!FILES$!NAME"                                -- :104
HYPERPLANT ON                                       -- :107
DETAIL $!PIPE                                       -- :110
```

PF 车间 TTY 进程（pfPipeMakeIsoView.pmlfnc:61-108）：
```pml
!macfile.writeRecord('$m "/$!path\temp_login.tmp"')
!macfile.writeRecord(!mdb)
!macfile.writeRecord(|ISODRAFT|)
!macfile.writeRecord(|!!pfpipemakeoverlyingview('$!optionFilePath','$!pdmsUserPath')|)
!macfile.writeRecord(|FINISH|)
-- 批处理："...\MON" tty -noconsole -macro="$!pdmsUserPath/makeisoview.mac"
```
出图内命令（pfPipeMakeOverlyingView.pmlfnc:141-232）：`$m /$!isoFile`（载入 pfpipespool.pmldat 选项）→ `Units IMPERIAL` → `Dimension OFF|ON`（PSTYP SITE/FITT）→ `File "$!fileManager.isoPlotName" SINGLE`（或 `File AND DXF ... SINGLE`）→ `MatlistFile "$!materialFile" PERPLOTFILE OVERWRITE with 55 lines` → `Charheight / Size / $!isoViewType(ISO1..4) / Reserve / Margin LEFT|TOP|RIGHT` → `MessageFile "mess_temp" OVERWRITE` → `MaterialList TableDefinition ...` → `detail $!spoolRef` → `var !unusedStatus isodraw status`（:263）。

### 3.3 Design 内预览（ISODRAFTMODE + isdpreviewisocontrol）

`isdruniso.pmlfnc:31` `define function !!isdRunIso(!type is STRING, !toggle is BOOLEAN)`，`!type ∈ {SYS, STA, SHO}`：
```pml
if( not defined(!!isdPreviewIsometric)) then
  !!isdPreviewIsometric = object ISDPREVIEWISOCONTROL()
if(!type eq 'SYS') then
  ISODRAFTMODE
  !!isdPreviewIsometric.produceSystemIso()
```
`prepareToDetail(!isoType)`（:464-477）：`options default` → 选选项文件（`%PDMSUSER%`/`%<proj>ISO%`/`%PDMSDFLTS%` 下 `\SYS\previewisosys[sysinch].txt` 或 `\STD\previewisostd[stdinch].txt`）→ `$M "$!<this.optionsFile>"`。
`produceStandardIso`（:221-287）：`mess "$!this.messageFile" over` → `DETAIL $!type $!name`。
`produceSystemIso`（:304-337）：`do !branch ... add $!branch` → `DETAIL all as |$!systemName|`。

### 3.4 isometricadp 的 DRAFT 世界建图链（ISODRWG.create，isodrwg.pmlobj:135 起）

```pml
VAR !drawingName EVAL $!<defaults.drwgNameRule> FOR $!<this.elementRefe>     -- :162
VAR !exist EXIST /$!drwgName                                                 -- :223
DRWG /$!drwgName                                                             -- :226（存在则访问）
VAR !allLiveShts COLL ALL SHEE WI :IdpIsoStatus NEQ 'Deleted' FOR CE         -- :232
DELETE DRWG MEM                                                              -- :243（recreate）
NEW DRWG /$!drwgName
 TITLE |$!type ISOMETRIC|
 SPPURP ISOADP
 FUNC |Isometric ADP|                                                        -- :251-255
!!isoDrwgNo(!type, !this.elementRefe, !!ce, !this.defaults)                  -- :257 图号
NEW LIBY /$!libyName ; NEW DLLB /$!dllbName                                  -- :280-281
NEW DLLB /$!dllbSName SPPURP CWSUBS                                          -- :350-351
NEW IDLI /$!idliName FUNC |$!index|                                          -- :300-301
  handle (2,618) → 'Drawings are already claimed by another user'            -- :308-312
NEW IDLI ... SPPURP PARTSL / SPPURP ADJCNT FUNC |Adjacent|                   -- :376-391
ADD $!component / ADD /$!idliAName / ADD /$!idliBName                        -- :320,385,411
do !attrib ... VAR !value EVAL $!bits[2] FOR $!component ; $!bits[1] |$!value[1]|  -- :503-507
NEW SHEE /$!sheeName$!shtNumber SIZE $!shtSize[1] $!shtSize[2]               -- :542-543
TITL |$!rootName| / FUNC |$!type| / SPPURP ISOADP
:IdpSheetNo $!shtNumber / :IdpNumberOff $!numberShts / :IdpIsoStatus '$!dfltStatus'  -- :548-553
!!setmarptype(!sheeRefe, 30)                                                 -- :558 Marine ptype
:IdpTotWeight / :IdpCofG / :IdpSpec ...                                      -- :577-662
REVI /$!sheeName$!shtNumber/Rev:$!revNumber
  handle (41,12) → DELETE REVI; REVI ... REVD |$!date| RVAU |$!drawnBy|      -- :717-726
  elsehandle none → REVD/RVSN/RVAU/APPR/APPD/:IdpInText $!revType            -- :730-735
BSRF UNSET  BSRF $!backRefe                                                  -- :748
VAR !allNote COLL ALL NOTE WI SPPURP EQ 'HISTRY' FOR CE ; DELETE NOTE        -- :754-760
NEW NOTE /$!sheeName$!shtNumber/NorthArrow SPPURP NARNOT                     -- :784
NEW SYMB TMRF $!narrSymbol ORIGIN $!northOrigin                              -- :785-799
VIEW /$!sheeName$!shtNumber/KeyPlan → NEW VIEW ... DIR D / TITLE |Key Plan| /
 VTYPE UNIV / SIZE $!keypXlen $!keypYlen / XYPO $!keypOrigin                 -- :823-827
NEW LAYE /.../KeyPlan/LocationBits SPPURP KEYPLN / PURP KEY / FUNC 'Keyplan' -- :832-835
VIEW /.../Isometric → NEW VIEW ... DIR $!direction（ISO1..ISO4）/
 TITLE |Isometric| / GLOBAL / SIZE $!viewXlen $!viewYlen / XYPO $!viewOrigin -- :869-873
RRSF $!ruleRefe / IDLN $!drawLists[$!shtNumber] / ARCTOL $!arctol            -- :874-876（HVAC arctol=1，其余=5）
SPPURP MAINVW / FUNC 'Main'                                                  -- :877-878
NEW RRUL /.../AdjacentRule USE /TT/Isometric_ADP/Dashed_Style FOR $!adjacentLists[...]  -- :888-889
```
后续：`!!isoDimnFull/isoDimnOverall` 标注、`!!isoCwayElev/isoHvacElev` 高程、ISOMTOENTRY/ISOTABLE MTO 表、`!!isoRevision` 修订表。

### 3.5 输出（PLOT 命令，isomodule.pmlobj）

```pml
PLOT $!sheetRefe PDF "$!pdfFileName" '$!options' $!overwrite   -- :187 handle (44,15)=文件已存在
PLOT $!sheeRefe PRINT '$!colourOption $!dialogOption $!scaleOption'  -- :234
```
批 PDF：`ISOADPAPPLICATION.pdf()`（isoadpapplication.pmlobj:773-836）；Excel 零件表 `ISOPARTSLIST.saveToExcel()`。

---

## 4. 输出格式控制

- ISODRAFT 输出格式（gen\rmess 解析 :59-157）：`.plt`、`.dxf`、`.pdf`、`.svg`、`.img`、`.emf`、`.hit`（Hyperplant）；图像格式词表在 opt\uimgfmt（BMP/JPG/GIF/PNG/TIF/TIF_LZW/TIF_G4）。
- DXF/AutoDRAFT：`gen\mdxfs:108` `CALLDRE MACAD-LINK <dir> <dxffn> <pipe> CREATE`；`editor\udxfunits:18 UNITS <units>`。
- TransferFile（IDF）：`gen\rgetmes` 解析消息记录（`-105`/`-1` 记录头）；`gen\mtrans:38 process transferfile "$!filename"`。
- VNET/VDI 导出：`VNETISOBatchExport.pmlobj`、`VNETWriteISOXML.pmlobj`（`.hit` → `-ISO_VPD.xml`，由 gen\rmess:259/269/318 调用）。

---

## 5. PMLLIB\isodraft（旧式表单/函数编目）

表单：`!!dePlots`、`!!detParams`、`!!isoAtexts`（Alternative Texts）、`!!isoColours`、`!!isoCutBack`、`!!isoCutPipe`、`!!isoDetailLst`、`!!isoMembers`、`!!isoProcessOpts`、`!!isoRevHighlight`、`!!isoSystemLst`。
对象：`DEPLOT`、`ISOCUTPIPECOL`、`ISOCUTPIPEFMT`、`ISOHIGHLIGHT`（.store/.read/.write）、`ISORULE`。
函数：`!!dePlotsConfirm/Copy/Del/End/Init/Mod/New/Validate(...)`（Detail plots 管理族）；`!!detParamsAtts/Browse/Clear/End/File/FileSet/Inc/Init/Remove/Replace/Unique/Val`；`!!isdOptFileList(!optGadget,!listGadget,!stdOpt,!warn)`（选项文件搜索域 PROJ→`$:ISODIR$:`→APPW→`PDMSDFLTS`→Local）；`!!isoCheckReserved(!paper,!marginT,!marginB,!area,!descr,!gadget)`（保留区校验）；`!!isoSaveOptions()`（`$M "%PDMSUI%/ISO/GEN/USAVOPT"` 薄封装）；`!!pipesetuptappingdrwg(!element)` / `!!pipestarttappingdrwg(!element)`（Tapping 图，被 mstdiso:158 调用）。

## 6. PMLLIB\isometricadp（Marine 轴测 ADP）对象总表

| 类 | 关键方法 |
|---|---|
| ISOADPAPPLICATION | .makeDrawings(!searchType) .makePartsList .pdf .print .batch .settings(ARRAY) .showLog .loadConfig .linkDocs .license(REAL) |
| ISODATA | .buildData(!columnData) .getData(!allElements,!filter,!drwgNameRule,!backRefe) .setDrawn(...) .remove(...) |
| ISODRWG | .isoDrwg(!elementRefe,!update) .create()→ISODISPLAYDRWG .getNextRev(!updateDesc) .setSettings |
| ISODISPLAYDRWG | .isoDisplayDrwg(!dbref[,!sheets]) .setSheet .setEntries |
| ISOSPOOLS | .getSpools .getSpoolComponents .splitCway(!cwayRefe,!continuations,!splitMethod) .splitHvac(...) .enhance .getDesignSpools（splitMethod='VOLUME'\|'SPLITPOINT'） |
| ISOSPOOL | .addComponent .addSupport .addPenetration .addCrossData .getData .getMaterial .getVolume .setCtmtrl |
| ISOPARTSLIST | .build .saveToExcel()（NETGRIDCONTROL/NETDATASOURCE） |
| ISOMODULE | .displaySheet .submitToPdf(!sheetRefe,!pdfFileName,!options,!overwrite) .submitToPrinter(...) |
| ISODEFAULTS | .getDflts() .getDrwgNoDflts()（读 %PDMSDFLTS%\IsoADP\DRA-ISO-*） |
| ISODRWGNODFLTS | .readDefaults .saveSettings .saveToFile（method=NSEQ\|FILE） |
| ISOMTOENTRY | .getAtext .getData .getHeaders .getTemplate .setCellAtext .setHeader |
| ISOBRCO | .addBrco .addDimdir .addIntersect .getBrcos .getDimDirs .getIntersects .getPoss |
| ISODIMENSION | .getDflts(!type) .dimension(!arrayOfValues) |
| ISOLOG | .add .read(!file) .write（%PDMSUSER%\LogFiles\isolog*.txt） |
| ISOREVISION | .get() .set(!values) |
| ISOUNITS | .getOffsetIncrement .getTextIncrement .getUnits |
| 其它 | APPISOADP、ISOBACK、ISOCONTENT、ISOCONTTAG、ISOELEVTAG、ISOINSULBRK、ISOMDSTAG、ISOMTOGEN、ISONAMEDTAG、ISOPENETAG、ISORECTANGLE、ISORIGIN、ISOSEARCH、ISOSLAB、ISOSPECBRK、ISOTABLE、ISOVIEW |

主表单 `!!isoMain`（26 表单中最大，方法 50+）：.process .browse .searchMode .singleMode .previewSplit .saveExcel .goToDrawing .goToElement .hiddenPreview .setSplitting .switchMode 等。

**用户函数扩展点**（userfunctions\，MTO/图号/关键图定制）：`!!isoDateStamp !!isoDocLink !!isoDrwgNo !!isoimpKeyPlan !!isoLogin !!isoMarKeyPlan !!isoSamKeyPlan !!isoUserCwayElev !!mtoCwayParameters !!mtoCwayWeight !!mtoDescription !!mtoHvacParam !!mtoHvacParameters !!mtoHvacWeight !!mtoPosNumber !!mtoQuantity`。MTO 单元格由 DB 属性 `:IdpFunc` 指向函数（isomto.pmlfnc:167-202：`!sortFunction = !sorted[1].dbref().:IdpFunc; !entries = $!sortFunction`）。

---

## 7. 配置数据

| 文件/目录 | 内容 |
|---|---|
| `isovir.dat`（根） | 二进制（Isodraft 内部库镜像），非文本 |
| `template_project\_proj_mar\def\isosymb.dat` | "AVEVA to Isogen symbol translation table"：`071 = 01HG`、`358 = ARBW` 等编号→SKEY 映射 |
| `%$:ISODIR$:%/STD|SYS/<optfile>` | 项目级选项文件；`%PDMSDFLTS%/STD|SYS/` 公司级；detail 列表 `%$:ISODIR$:%/LIS/<sys>`；底图 `/UND/` |
| `%PDMSDFLTS%\IsoADP\` | `DRA-ISO-CONTENT / DRA-ISO-ATTRIB(-CWAY) / DRA-ISO-DRWGNO / DRA-ISO-ORIGIN / DRA-ISO-STATUS` |
| `PMLLIB\isometricadp\data\` | `Metric_Library_load.dat / Imperial_Library_load.dat`（符号库装载宏）、`Hvac_Design.dat`、`Hvac_Paragon.dat`、`Lexicon.dat` |

符号库装载宏要点（Metric_Library_load.dat 实测行号）：
```pml
NEW SYMBOL / TMRF SYTM /DRA/MAS/BACKS/LOGO/CADC          -- :1266-1268
NEW SYLB /$3$NIsometric_ADP/Symbols                       -- :2883
NEW SYTM /$3$NIsometric_ADP/MTo_Tag1|2|3 / Ppoint / Arrow1 / SpecBreak / InsulBreak  -- :2896-3178
NEW SYTM .../NSgrid /EWgrid / Keyplan / Plant_North / Origin / Penetration / Support  -- :3241-4291
NEW SYTM .../ISO1..ISO4_N.ARROW（含 _MAR 变体）            -- :4354-5404
NEW SYTM .../Elevation.30|.-30|.150|.-150（FLEX.PA/FLEX.PL）-- :6438-7332
NEW SYTM .../Hvac/MtoHeader-Col1..4、MtoEntry-Col1..4、RevEntry-Col1..8  -- :7938-9687
NEW SYTM .../Cway/ 同构全套                                -- :9772-11521
OLD SYMBOL 1 of SYTM .../SpecBreak ; TMRF SYTM .../Arrow1  -- :11616-11626
-- Hvac_Design.dat 网格线：
NEW GRIDLN /IsometricADP_GridX1..X10 GRDOFF 0..45000 GRDID '1'..'10'   -- :39-48
NEW GRIDLN /IsometricADP_GridYA..YJ GRDOFF 0..45000 GRDID 'A'..'J'     -- :52-61
```

替代文本缺省库（isoatexts.pmlfrm `.defaultAtexts[200..483]` :566-848）：`201 'E'、208 'CONN. TO'、209 'CONT. ON'、230 'VENT'、250 'DATE'、252 'BATCH REF'、253 'PIPING SPEC'、288 'PIPE'、300 'FABRICATION MATERIALS'、303 'COMPONENT DESCRIPTION'、305 'ITEM CODE'、306 'QTY'、332 'PAGE'、360 'F'/361 'C'/362 'S'、371-373 'TOTAL FABRICATION/ERECTION/TOTAL WEIGHT'、380 'PREP.'、386 'CUT START'、400 'TRACED\n PIPE'、451 'TAPPING COORDINATES'、460 'BEAM $?'、470-478 弯管表头 'PT NO','NB','ANGLE','RADIUS','PER 10 FT'`。分组索引 `.drwgAreaIndex/.matListIndex/.titleBlockIndex/.weldBoxIndex/.lineSummIndex/.bendTableIndex/.boltReportIndex`（:876-1092）。

PCODE：ISODRAFT 中无 `PCODE` 命令；支吊架码走 CAPS UDA `new uda /SPCODE.UDA + udname |spcode|`（caps\capsudas:73-74）。

---

## 8. handle 错误码速查（iso 相关）

消息模块号 148。PMLLIB 唯一码全集：

| 码 | 语义 | 出处 |
|---|---|---|
| (2,109) | 名称不存在/已存在 | isodrwg.pmlobj:1198 等多处 |
| (2,618) | 元素被他人占用 | isodrwg.pmlobj:429 |
| (2,111) | 层级不可访问 | isomain.pmlfrm:3919 |
| (2,113) | 列表穷尽 | isodrwg.pmlobj:711 |
| (44,15) | PDF 文件已存在 | isomodule.pmlobj:188 |
| (44,33) | 文件未找到 | isdruniso.pmlfnc:42 |
| (41,12) | 名称已存在（REVI 新建） | isoadpapplication.pmlobj:418 |
| (61,528)/(61,571) | 读取/视图错误 | isoedit.pmlfrm:1986/1090 |
| (64,12)/(64,313/314/324)/(64,347)/(64,353)/(64,510)/(64,548) | 尺寸/几何错误 | isodrwg:1028、isodimnoverall:541、isospool:610 等 |
| (99,532) | UDA 未定义 | isodrwgnumber.pmlfnc:47 |
| (160,9) | 打印错误 | isoprint.pmlfrm:193 |
| handle 6/7/8 | VPRM: 6=MTO 线号/区域未设 7=多工艺线 8=多工艺区 | mstdiso:235-249 |
| (41,222) | 该层级不可访问 | mstdiso:53 |
| (41,324)/(41,319)/(41,322) | 文件已存在/无法访问/被占用 | mbatch:55/68/70 |
| (44,36) | 权限不足 | mcreopt:36 |
| (61,142)/(61,143) | 列表>500 截断/无法访问目录 | isysiso:37/34 |
| (47,15) | 语法错误（选项值非法） | mstdiso:114 |
| (47,62) | 属性语法错 | mweldopt:59 |
| (46,28) | 变量未定义 | ucomini:42 |
