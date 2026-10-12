# Marine Hull 船体建模语句大全（穷举级·源码实证）

> 来源：PMLLIB\hulldesign\ 全部命中文件（stmtExec 仅命中此 5 文件）+ Vitesse\Examples\Hull\ 15 个 .py 全读 + Vitesse\Basic_Design\KcsMenuTBD01~10 + Vitesse\Lib\_TBhook_*/cPanel/KcsPanelSchema/KcsUtilPanSch + design\objects\hmholefromprofile.pmlobj。
> 适用：AVEVA Marine (PDMS 系) 12.1 SP4。船体面板（HML 语句）、marAPI MARHULLPAN、kcs_hull/kcs_chm Python API、开孔管理全收录。
> 先行结论：`SDE3` 全树 0 匹配；`SCYL/DMLT` 仅出现在 Paragon/MDS 注释中（非船体建模语句）；`kcs_hull/kcs_chm/kcs_hullpan` 是编译进 Vitesse 运行时的内置模块（源码不随安装发布，穷举依据为官方示例与 Lib 支撑库）；HOL/OPE/LEP/QUI 等语句关键字全树 0 命中（平面面板域开孔 = CUT 语句，曲面面板域 = kcs_chm.cpan_hole_create）。

---

## 1. Hull 元素类型与 DB 级 NEW

### 1.1 Hull DB 元素类型总表

| 元素类型 | 含义 | 出处 |
|---|---|---|
| HPANEL / CPANEL | 平面/曲面船体面板 | hulldesign\functions\hullCheckManpkg.pmlfnc:50；design\objects\hmholefromprofile.pmlobj:263 |
| HPLATE | 船体板 | hmholefromprofile:263,691；assembly\forms\hullreport.pmlfrm:332 |
| HBRCKT / HSTIFF / HCLIP | 肋板/骨材/肘板 | hullreport.pmlfrm:333-335 |
| MPLNST MAPLNS MPRNST | 板/型材套料 | hullCheckManpkg.pmlfnc:50 |
| MPLATE/MPROF/MBPRO | 制造零件 | hulldesign\functions\hullDeleteUnrefMANUParts.pmlfnc:22 |
| HBLWLD | 分段 Block world | hulldesign\functions\hullNewBlock.pmlfnc:41 |
| RPLTAB / RAWPLA | 原材料板表/原材料板 | hullDefineRawPlates.pmlfnc:112,138 |
| SOLI/SOLEXT/TDEN/SDEN | 材质等级固体/密度 | hullCreateQualityList.pmlfnc:118-137 |
| LINKWL/LNFOLD/LNDESC/LNLINK | 船体链接 | hullDeleteObsoleteLinks.pmlfnc:21-47 |
| TABWLD / MATW | 板表 world / 材质 world | hullDefineRawPlates:27、hullCreateQualityList:28 |

### 1.2 DB 级 NEW 完整代码块

创建分段（hullNewBlock.pmlfnc:56-66）：
```pml
   handle (2,109)                       $* 名称不存在才创建
     new GBLOCK $!gName $!dbCmd
     new OBJHD $!oName
     new BLOCK $!bName $!dbCmd
     new GOBELE
     PROTECTION OFF
     GOBREF $!oName
     OWN
     PROTECTION ON
     return !!ce
   endhandle
```

创建原材料板（hullDefineRawPlates.pmlfnc:111-147）：
```pml
            handle (2,109)
               new RPLTAB /$!RplElement
            endhandle
            handle (2,109)
               new RAWPLA /$!RawPlateName
            endhandle
            if ( NOT !RAWexists) then
               Height $!RawPlatethickn
               Length $!RawPlateLength
               Matref /$!RawPlateQuality
               Width  $!RawPlateWidth
               Charge $!RawPlateCharge
               Purch  $!PurchaseInfo
```

创建材质等级（hullCreateQualityList.pmlfnc:112-138）：
```pml
               handle (2,109)
                  if ( NOT !first) then
                     owner
                     owner
                  endif
                  new SOLI /$!Quality
                  new SOLEXT
               endhandle
               QuaCd $!QualityCode
               Preppr $!Paint
               new TDEN
               new SDEN
               Density $!Dens
```

开孔虚拟 FIXING（hmholefromprofile.pmlobj:413-443）：
```pml
  !!ce    = !this.penetratingElementLocation
  NEW FRMW
  NEW FIXING
  !this.virtualHoleRef = !!ce
  CALL !!autonamece(false)
  NEW TMPL
  NEW EXTR
  !!ce.height = (!thickness * 2 )
  NEW LOOP
  !this.penetratingProfile.dbWrite(!!ce)
  EXTR
  MOVE $!<direction> THROUGH $!<position>
```

### 1.3 DT 类型码（面板数据类型，实测）

| DT 码 | 含义 | 出处 |
|---|---|---|
| DT=101 | 横舱壁 TBHD | KcsMenuTBD04TBHD.py:188 |
| DT=102 | 深肋板 DWeb/平面板 | KcsMenuTBD07DWeb.py:187 |
| DT=123, BRA | 肋板 bracket | _TBhook_CustBracket.py:92-93 |
| DT=191 | 主面板（带 SUB 子板引用） | cPanel.py:455；KcsMenuTBD10KBHD.py:823 |
| DT=201 | 纵舱壁 LBHD | KcsMenuTBD02LBHD.py:213 |
| DT=202 | 纵舱壁折角/纵桁 Girder | KcsMenuTBD03LBHDI.py:215、KcsMenuTBD06Girder.py:229 |
| DT=301 / DT=302 | 平甲板 / 折角斜甲板 | KcsMenuTBD01Deck.py:242,299、KcsMenuTBD05Stringer.py:175 |
| DT=957 / DT=958 | 自动命名前缀 BRA/SUB | _TBhook_AutoPanelName.py:47-50 |

舷侧位置码：`SBP / SP / P / S`（省略 = 全宽）。
符号视图元素类型码（kcs_hullpan.view_detail_new）：`2=Flange, 3=Stiffener, 4=Bracket, 5=Seam`（kcs_ex_hullpan04.py:47-53）。

---

## 2. HML 建模语句（stmtExec 全语法）

语句以 `;` 结尾，多段以 `/ ` 或 `,` 分隔；PML 侧 `MARHULLPAN.stmtExec(组号, 语句)` 执行，组号 0 = 追加新组。

### 2.1 PAN（面板定义）

```python
# 平面甲板（KcsMenuTBD01Deck.py:242）
stmt = "PAN,  '" + name + "', SP, DT=301, Z=" + position + ";"
# 三点平面（同文件 294-299）
ori = "ORI=" + str(origin[0]) + "," + str(origin[1]) + "," + str(origin[2])
uax = "UAX=" + str(uaxis[0]) + "," + str(uaxis[1]) + "," + str(uaxis[2])
vax = "VAX=" + str(vaxis[0]) + "," + str(vaxis[1]) + "," + str(vaxis[2])
# 肋板（_TBhook_CustBracket.py:92-93）
st = "PAN, '" + BracketName +  "', SBP, DT=123, BRA, X=" + FRTerm + ";"
# 块名+子板通配（KcsMenuTBD10KBHD.py:823,825）
st = "PAN, '%s', SP, BLO='%s', DT=191, SUB='%sK*';"
st = "PAN, '%s', SP, BLO='%s', DT=191, SUB='%sK###';"
# 子板（同文件 757-773）
stPAN = "PAN, '" + nameSub + "', SP, SUB, " + Pos[n] + ";"
stPAN = stPAN + "ORI=" + stmp + ",5000, UAX=" + RPos[n] + ",..., VAX=" + stmp + ",10000;"
# 删除面板（cPanel.py:123）
kcs_hullpan.stmt_exec(0, "PAN, '%s', DELETE;" % panel)
# 官方格式样例（_TBhook_PPanScheme.py:65）
"PAN, 'TEST', P, BLO='BLO', DT=102, X=FR30;"
```
语法要素：`PAN, '<名称>', <SBP|SP|P|S>[, BRA][, SUB][, BLO='<块>'][, DT=<码>], <X=|Y=|Z=<定位>|ORI=,UAX=,VAX=>;`

### 2.2 BOU（边界）

```python
# 限位引用 + LIM=（KcsMenuTBD03LBHDI.py:223）
stmt = "BOU,  '" + deck + "', LIM=" + str(pslim) + "/ " + aftlim + "/ '" + longbulk + "', LIM=" + str(lblim) + "/ " + forlim + ";"
# 肋板三边（_TBhook_CustBracket.py:98-99）
st = "BOU, SUR='MTP'" + "/ '" + tanktop[1] + "'/ '" + girder[1] + "';"
# 点引用边界（同文件 176）
st = "BOU, Z=P1 / 'BOU1' / Z=P3 / 'BOU2';"
# SUR= + ZMIN/ZMAX（_TBhook_PPanScheme.py:66-67）
"BOU, SUR=1/ 'BASIC-DECK1'/ Y=LP13/ 'BASIC-TANKTOP';"
"BOU, SUR=1, ZMIN=3000, ZMAX=7000/ 'BASIC-DECK1'/ Y=LP13+450/ 'BASIC-TANKTOP';"
# 舷侧镜像 YMI=（KcsMenuTBD01Deck.py:307-308）
stmt = stmt + ", YMI=" + sblim[2:]
# 对称同限 + REF（同文件 252-255）
if sblim == pslim: stmt = stmt + ", REF"
# 外板 '__HULLFORM__'（KcsUtilPanSch.py:141-145）
"'__HULLFORM__'" (+ ", REF")
# 舱壁子板 __HIGH__/__LOW__ 伪限位 + CON 连接码（KcsMenuTBD10KBHD.py:671-686, 744-753）
stBOU, HighY = stBOU + "__HIGH__/ ", 1
lim = "Y=" + stringutils.TrimNum(Y0,1) + CON
```
限位三型（cPanel.py:209-333 类层次）：
- `CoordinateLimit`：`X=2000`、`FR20`、`FR20+200`、`LP-5+500`
- `PanelLimit`：`'PANELNAME'[, REF]`
- `OuterShellLimit`：`'__HULLFORM__'`

拼接：`BoundaryStmt()`（cPanel.py:429-436）生成 `"BOU, " + join(limits, "/ ") + ";"`。

### 2.3 PLA（板）

```python
# 厚度（KcsMenuTBD01Deck.py:265）
stmt = "PLA,  MAT=" + str(platedim) + ";"
# 材质+切边（_TBhook_CustBracket.py:105）
st = "PLA, MAT=12, MSI=FOR, QUA=A36;"
# 材料边（KcsMenuTBD03LBHDI.py:232）
stmt = "PLA,  MSI=SB, MAT=" + str(platedim) + ";"
# 厚度+偏移+材料边（KcsMenuTBD10KBHD.py:729）
stPLA = "PLA, MAT=" + TrimNum(BHD.Thickness,1) + "," + TrimNum(-BHD.Thickness/2,1) + ", MSI="
# 定位点控制的板轮廓（同文件 785）
stPLA1[:-1] + ", U=P3, V=P3;"
```
MSI 取值：`FOR / AFT / PS / SB / TOP / BOT`（KcsMenuTBD08Stiffener.py:110-157）。

### 2.4 STI（骨材）

```python
# KcsMenuTBD08Stiffener.py:332-351
long_end = "CON=15, CUT=3100"      # 球扁钢 4xx
long_end = "CON=15, CUT=2100"      # 2xx/3xx 型材
long_end = "CON=15, CUT=1100"      # 其它
stmt = "STI,  PRO=" + profdim + ", SID=" + side + ", " + stipos[spno] + rev + ", " + long_end + "/ " + long_end + ";"
# rev 由材料边决定（:304-313）：", REV"
```
位置重复子句由 `KcsUtilPanSch.getGeoRepSSE(axis, prefix, start, step, end)` 生成，形如 `FR5(8)FR96`（KcsUtilPanSch.py:43-62；`getGeoRepT` 生成逗号列表式 :67-121）。

### 2.5 NOT（切口/流水孔）

```pml
-- 角部切口+重复（phullnotch.pmlobj:90）
!notchesStatement = 'NOT,' & !this.notchInCornersSize & ', COR=1(1)' & $!this.nrOfCorners & ';'
   → 'NOT,R100, COR=1(1)5;'
-- 面板缝切口（:152-154）
!statements[!p] = 'NOT,' & size & ',''' & panelName & ''',' & ' SEA=' & seamNo & ';'
   （+ ', REF' 镜像变体）
-- 带 P/S 侧前缀（:268-283）
'NOT,' & size & ', P,''' & name & ''',' & ' SEA=' & no & ';'
'NOT,' & size & ', S,''' & name & ''',' & ' SEA=' & no & ',REF;'
-- 组合切口（phullnotchcombine.pmlfnc:242-289）
!newNotchStmt = 'NOT, VU' & !newNotchLenA & '*' & !radius & ', COR=' & !newNotchC & ', LIM=' & !newNotchLim & ';'
!newNotchStmt = 'NOT, KU' & !newNotchLen.nint() & '*' & !newNotchB & ', LIM=' & !newNotchLim & !coordParam & !newNotchMid.nint() & ';'
   -- coordParam = ', U=' 或 ', V='（:225-229）
-- 拆分切口（phullnotchsplit.pmlfnc:80-163）
!newNotchCorStmt = 'NOT, R' & !oldFirstRad & ', COR=' & !oldCor & ';'
!newNotchSeaStmt = 'NOT, R' & !oldSecondRad & ', ''' & name & ''', SEA=' & no & ';'
-- 简单角切口（_TBhook_CustBracket.py:111）
st = "NOT, R50, COR=1,2,3;"
```
默认尺寸：`R100`(角) / `R75`(面板缝) / `R50`(相邻板缝)（phullnotch.pmlobj:54-56）。

### 2.6 CUT（开孔，按 tag code 前缀分组）

组号前缀：`S`=tag0，`ST`=tag1，`SL`=tag3/4，`L`=tag30(纵骨)，`T`=tag40(横骨)，`TR`=横剖：
```pml
-- tag3/4，位置=骨材号(÷10)，SL 前缀（phullcombine.pmlobj:405-413）
'CUT, ' & type & ',''' & rso & ''', SL' & n & ',REF' & ',C=' & offset & ';'
'CUT, ' & type & ',''' & rso & ''', SL' & n & ',REF' & ',C=' & offset & ',R1=' & radOne & ';'
-- tag0（:823-831）S 前缀；tag1（:1356-1364）ST 前缀；tag30 L；tag40 T
-- 自由命名 SHP=（:1662-1684）
'CUT, ' & type & ', SHP=''' & freeName & ''',REF,' & 'C=' & offset & ';'
'CUT, ' & type & ',SHP=' & 'name1'':''name2'':...' & ';'
-- 多孔合并组（:426-428）
'CUT, ' & type & ',''' & rso & ''' ' & ',SL12,SL14,...' & ',REF;'
```
切口类型码：`' AB'`(角钢) / `' BB'`(球扁钢) / `'TB'`(T 型)（:527,555,1584,1758）。

### 2.7 POI（定位点）

```python
# 交点+侧别（_TBhook_CustBracket.py:160,168,217-223）
st = "POI,  NO=1, INT, '"+deck+"', SID=TOP/ '"+flange+"', SI2=AFT;"
st = "POI,  NO=2, INT, '" + pan1 + "', SID=SB/ '" + pan2 + "', SI2=FOR;"
# 相对偏移点（同文件 162-165, 232-254）
st = "POI,  NO=2, DU=-430, DV=15, X=P1, Z=P1;"
st = "POI,  NO=21, DU=..., DV=..., X=P11, Y=P12;"
# 插值点（同文件 226-229；KcsMenuTBD10KBHD.py:784-786）
st = "POI,  NO=11, XYZ=P1, X2Y=P2, F=0.5;"
"POI, NO=3, DU=3, XYZ=P1, X2Y=P2, F=0.5;"
# 限位交点（KcsMenuTBD10KBHD.py:782-783）
"POI, NO=1, INT, LIM=%d/Y2=%s;"
# 圆柱穿孔（KcsMenuTBD07DWeb.py:259,263）
stmt = "POI,  R3, CRO, F1, " + pilpost[0] + ", TOP, DX=" + str(thoff) + ";"
stmt = "POI,  R3, INT, " + pilpost[0] + "/ " + pillim + ", SI2=TOP, DX=" + str(thoff) + ";"
```

### 2.8 CUR（曲线/轮廓线）

```python
# 圆弧-直线轮廓（_TBhook_CustBracket.py:166-167, 256-260）
st = "CUR, 'BOU1', X=P2 / U=P2, V=P2, T=30 / R=250, U=P3, V=P3, T=83;"
st = "CUR, 'BOU1', X=P21, Y=P21, XT=P31, YT=P31 / X=P31, Y=P31, XT=P32, YT=P32 / X=P32, Y=P32, XT=P23, YT=P23;"
# 官方样例（_TBhook_PPanScheme.py:68）
"CUR,  'C1', CLO, R=100, 'BASIC-DECK1', DIR=SB, M1=300, SID=FOR/ R=100, LIM=2, M1=300/ U=FR4-200, V=300, T=135;"
```

### 2.9 SEA / EXC / WEL / FLA

```python
# 板缝（KcsMenuTBD10KBHD.py:763-767）
stSEA = "SEA" + ", BEV=" + BevelCode + ", EXC=" + SeamExcess + ", Y=" + SeamPos + ";"
# 余量（同文件 803）
stEXC = "EXC, LIM=%d, M1=%s;"
# 焊接（_TBhook_CustBracket.py:181）
st = "WEL,  LIM=2, BEV=V22.5T;"
# 法兰（KcsMenuTBD06Girder.py:258、KcsMenuTBD07DWeb.py:220）
stmt = "FLA,  PRO=" + profdim + ", LIM=3, CON=14, CUT=1402,50/ CON=14, CUT=1402,50;"
```

### 2.10 PML 嵌入标准模板（stmtExec 对象调用）

```pml
import 'marAPI'
handle(1000, 0)            -- 1000,0 = marAPI 已导入，忽略
endhandle

using namespace 'Aveva.Marine.Design'
!runObject = object MARHULLPAN()
!runObject.stmtExec( 0, !statement)                            -- phullnotch.pmlobj:97-98
!objMarHullPan.stmtExec( !this.cutoutGroupNr, !newStatement)   -- phullseparate.pmlobj:627（替换指定组）
!mHullPan.stmtExecSingle(!notchGroup, !newNotchStmt, !firstNotch[2])  -- phullnotchcombine.pmlfnc:313
!statement = !panelObj.stmtGet( !adjacentPanelName, 2)         -- 组2=PAN语句 (phullnotch.pmlobj:314)
!statementT = !panelObj.stmtGet(!this.cutOutPanelName, 3)      -- 组3=SUR语句 (phullcombine.pmlobj:253)
!this.cutoutGroupNr = !panelObj.groupGet(!name, !partId)       -- 部件ID→组号 (phullcombine.pmlobj:249)
```

Python 等价（kcs_hullpan / kcs_hull）：
```python
kcs_hullpan.pan_init(name, scheme)                    # cPanel.py:121
kcs_hullpan.stmt_exec(0, stPAN)                       # cPanel.py:464
kcs_hullpan.stmt_exec_single(0, st, BracketName)      # _TBhook_CustBracket.py:95
kcs_hullpan.stmt_get(panel, group); kcs_hullpan.group_next(panel, -2, 0)  # KcsPanelSchema.py:184-190
kcs_hullpan.pan_store_single(BracketName); kcs_hullpan.pan_skip_single(BracketName)  # _TBhook_CustBracket.py:118,128
kcs_hull.pan_init(name,name); kcs_hull.pan_exec_stmt(0, stmt); kcs_hull.pan_modify(panel,2)
kcs_hull.pan_recreate(); kcs_hull.pan_store(); kcs_hull.pan_skip()  # KcsMenuTBD01Deck.py:240-280
(res, stmt) = kcs_hull.pan_curve_create(viewhandle, panel, curvename, plane[0], contour)  # kcs_ex_hullcurve1.py:91
res = kcs_hull.pan_curve_store(viewhandle, curvename, contour)  # kcs_ex_hullcurve2.py:86
```
语句 Schema 枚举（运行期字典）：`kcs_hullpan.kcsSCHEME_STATEMENTS[语句关键字][关键字] → {'TYPE': n}`；`kcsSCHEME_KEYWORD_TYPES[n] → 类型名`（kcs_ex_hullpan05.py:21-51）。解析器：`KcsPanelSchema.PanelSchema` 类（`SetValue/GetValue/GetStatements/SplitKeyword/MergeStatement/GetStatementFromValues`），分隔符 `(',', ';', '/')`，引号内逗号不拆分（KcsPanelSchema.py:350-356）。

---

## 3. kcs_chm（曲面船体 Python API，全签名）

```python
-- 建模/几何
Model = kcs_chm.curve_principal_create(CurveName, "X=40000", MinPt, MaxPt, SurfaceName)  # shellcurves:78
Model = kcs_chm.curve_planar_create(CurveName, Plane, MinPt, MaxPt, SurfaceName)         # shellcurves:132
ModelList = kcs_chm.run_XML('c:\\temp\\Profile.xml', 'c:\\temp\\Profile.log')            # shellstiff:232
kcs_chm.output_XML(ModelList, 'c:\\temp\\MyXML2.xml')                                    # XML:346
kcs_chm.stiffener_split(ObjToSplit, SplittingObj)                                        # shellstiff:259
Stiff3 = kcs_chm.stiffener_combine(Stiff1, Stiff2)                                       # shellstiff:308
kcs_chm.stiffener_to_profdb(Stiff1)                                                      # shellstiff:291
kcs_chm.recreate(Long)                                                                   # shellstiff:337
kcs_chm.store(Model) / kcs_chm.skip(Model) / kcs_chm.delete(Model)
ret  = kcs_chm.remarking_length(modelFrom, modelAlong, modelTo)                          # remarkinglength:184
ret2 = kcs_chm.remarking_length_ext(act, hullpanname, modelFrom, modelAlong, modelTo)    # :189
     # act 位标志: 1=BEVEL_GAP, 2/4/8/16/32=EXCESS_1..5, 64=COMPENSATION, 128=SHRINKAGE (:22-29)
getProp = kcs_chm.plate_prop_get(model);   kcs_chm.plate_prop_set(model, prop)           # sh_plate_prop:34,41
getProp = kcs_chm.stiffener_prop_get(model); kcs_chm.stiffener_prop_set(model, prop)     # sh_stiff_prop:34,43
kcs_chm.cpan_hole_create(Model.Name, HoleOptions)                                        # cpanhole:124
-- 视图
view = kcs_chm.view_shellexp_new(shellx)          # curved_views01:84（外板展开）
view = kcs_chm.view_bodyplan_new(body)            # :91（横剖）
view = kcs_chm.view_shprof_new(model)             # :97（曲面骨材）
view = kcs_chm.view_devpla_new(object)            # :102（展开板）
view = kcs_chm.view_curvedpanel_new(object, options)  # :106
view_options = kcs_chm.view_modify(view)          # :109
kcs_chm.view_recreate(view)                       # :112
-- 常量：kcsCUTTING_PLANE/kcsFRAME_PLANE/kcsBUTTOCK_PLANE/kcsWATERLINE_PLANE/kcsX|Y|Z_AXIS/
--       kcsPERPENDICULAR/kcsPERP_WHOLE/kcsDUMMY_INTERVAL/kcsPROFILE_TYPES（Lib\KcsShStiffProp.py:8-26）
```

XML 建模 Schema（`CurvedHull.xsd`，`$SB_SYSTEM\xml\`）：根 `Ship`；`ShellProfile@ObjId` → `Material@Type,Parameters,Grade`（如 Type="10" Parameters="200 15"）→ `Branch/Trace/ByPrincipalPlane@Surface,Z` + `Box@XMin=FR50,...` + `ShellStiffener`；`HullCurve@ObjId` → `ByPrincipalPlane@Surface,X|Y|Z` + `Box@XMin..ZMax`。

属性类：`KcsShPlateProp`（SetPartsList/GPS_1..4/SurfaceTreatment/Destination/Thickness/Quality/Posno/LaminateIn/Out/Shrinkage/RawPlate）与 `KcsShStiffProp`（ProfileType/ProfileParameter/Quality/Posno/Perpendicular/Connection/Excess/Offset/WebBevel/FlaBevel/InclAngle/EndCut/FilletWeldDepth/SurfaceTreatment/TraceBevel 全 Set*/Get*）。

曲面开孔选项 `KcsPanHoleOptions`（Vitesse\Lib\KcsPanHoleOptions.py:19-398）：`SetOriginAlongLine/AlongAxis/AsStored`、`SetDirection/SetDesign/SetDevelop/SetBurnOption/SetMarkOption/SetMarkType/SetMarkLen/SetWCOGFictive/SetSymmetry`；对称常量 `SYMM_AS_PANEL=0/SYMM_PS=1/SYMM_SB=12`；标记常量 `MARK_HOLE=0/MARK_CROSS=1/MARK_BOTH=2`。

---

## 4. kcs_hullpan（平面面板管理 Python API，全签名）

```python
kcs_hullpan.pan_activate(hullpanname)                        # kcs_ex_hullpan01.py:45
kcs_hullpan.pan_store() / pan_store(name)                    # :51,57
kcs_hullpan.pan_skip(name) / pan_skip()                      # :63,69
list = kcs_hullpan.pan_list_active()                         # :74
kcs_hullpan.pan_delete(hullpanname)                          # :77
kcs_hullpan.pan_move(model.Name, moveOpt)                    # 02:144
kcs_hullpan.pan_copy(model.Name, opt)                        # 02:182
kcs_hullpan.pan_split(panelName, splitOpt)                   # 02:280
kcs_hullpan.pan_recreate(hullpanname)                        # 02:357
kcs_hullpan.pan_topology(model, 'defining'|'dependent primary'|'dependent all')  # 02:308-312
kcs_hullpan.pan_remove_seam(hullpanname, 5001)               # 03:55
kcs_hullpan.pan_group_delete(hullpanname, dict)              # 03:59
kcs_hullpan.pan_group_divide(hullpanname, dict, [model, model])  # 03:64
kcs_hullpan.pan_sti_split_by_model(dictgroup, dict)          # 03:71
kcs_hullpan.pan_sti_split_by_plane(dictgroup, dict)          # 03:77
nViewHandle = kcs_hullpan.view_detail_new(2|3|4|5, nElemHandle)  # 04:47-53
kcs_hullpan.view_symbolic_recreate(nViewHandle)              # 04:55
SymbolicView = kcs_hullpan.view_symbolic_modify(nViewHandle) # 04:57
```
Options 类：
- `MovePanOptions`：`SetPrincipalPlane(cord,relpos,cordval)` / `SetThreePoints(origin,uaxis,vaxis)` / `SetPlaneObject(name)`；常量 `PRINCIPAL_PLANE=1/THREE_POINTS=2/PLANE_OBJECT=3`
- `CopyPanOptions`：`SetNameMapping(dict)` / `SetBlockName(name)`
- `SplitPanOptions`：`SetCuttingPlane(Plane3D)` / `AddPanelMapping(name, block, symmetryCode)`；对称码仅 `'SP','SBPS','S','P',''`

---

## 5. marAPI MARHULLPAN 全方法（PMLLIB 穷举）

导入固定写法（phullnotchjoinsplit.pmlfnc:29-35）：
```pml
import 'marAPI'
handle(1000, 0)      -- 1000,0 = 已导入，忽略
endhandle
using namespace 'Aveva.Marine.Design'
!obj = object MARHULLPAN()
```

| 方法 | 签名（据调用推断） | 出处 |
|---|---|---|
| stmtExec | `(组号REAL, 语句STRING)` | phullnotch.pmlobj:98,111 等 |
| stmtExecSingle | `(组号, 语句, 面板名)` | phullnotchcombine.pmlfnc:313 |
| stmtGet | `(面板名, 组号) → STRING` | phullnotch.pmlobj:314（组2=PAN、组3=SUR） |
| groupGet | `(面板名, 部件ID) → 组号` | phullcombine.pmlobj:249 |
| panModify | `(面板名, 2)` | phullcombine:351 等多处 |
| panGroupDelete | `(面板名, 组号)` | phullcombine:353 |
| panRecreate | `(ARRAY 面板名)` | phullcombine:369 |
| panStore | `(ARRAY 面板名)` | phullcombine:372 |
| panActivate | `(面板名)` | phullnotchcombine.pmlfnc:312 |
| panSkipSingle | `(面板名)` | phullseparate.pmlobj:106 |
| panListActivePML | `() → ARRAY` | phulltriggerpostboundarycreation.pmlfnc:36 |
| getNearbySeams | `(面板名) → ARRAY[SeamRecord]` | phullnotch.pmlobj:131 |
| getPanelStiffPar | `(面板名, tagCode, refNr, rso名) → ARRAY[StiffPar]` | phullcombine.pmlobj:495 |
| getStiffData | `(面板名, tagCode, refNr, rso名, reflected) → ARRAY[StiffVectors]` | phullcombine:649 |
| getShellStiffData / getShellStiffPar / getShellStiffFreeName | 曲面骨材族 | phullcombine:1544/1460/1415 |
| getCutoutPoints | `(面板名, partId, 0.0, !MARCONTOURPLANAR) → 0/-1` | phullseparate:78 |
| getNotchPoints | `(面板名, partId, !MARCONTOURPLANAR)` | phullnotchsplit.pmlfnc:101 |

返回对象方法：SeamRecord → `isSurfaceSeam()/panelName()/seamNo()/limNo()/uCoord()/vCoord()/reflected()`；StiffPar → `profType()/dimOne()/dimTwo()`；StiffVectors → `flangeDirX/Y/Z()、intersectionPointX/Y/Z()`。

配套 marAPI 类：`MARDEX`（数据抽取）、`MARUI`（`pointPlanarReqPML(prompt,!point)`、`messageNoConfirm`、`AppWindowRefresh`）、`MARUTIL`（`quitPML()/OkPML()/TraCoordShip/TBEnvironmentGet`）、`MARMODEL`（`partType()/name()/partIdPML()`）、`MARDRAFTING`（`modelIdentify`、`DwgCurrent()`）、`MARPOINTPLANAR`（`setCoordinates(u,v)`）、`MARTRANSFORMATION`（`setByRowFromArray/transform`）、`MARCONTOURPLANAR`（`getPointOnContour/contourPML`）。
命名空间：`Aveva.Marine.Design / DataExtraction / Geometry / UI / Drafting / Utility`。

开孔管理（Hole Management）：
```pml
!holeElemColl            = object HOLEELEMCOLL()
!holeElemColl.panel      = !this.pickedItem
!holeElemColl.holeFixing = !this.virtualHoleRef
!holeElemColl.fitting    = !this.penetratingElement
!interface = object HMCONTROL()
!result    = !interface.createFittHole(!holeElemColl, !this.holePosition, 'Free', '', !this.holeType)
```
（hmholefromprofile.pmlobj:478-486）；贯穿体识别 `hardType eq 'HPLATE'/'CPLATE'/'CTWALL'/'BPANEL'`（:263-318）。

---

## 6. kcs_dex 数据抽取字符串全表（Hull）

```python
"HULL.PANEL('N').SYMMETRY" / ".NBOUNDARY" / ".NBOU" / ".BOU(i).COR" / ".BOUNDARY(i).NAME" / ".BOUNDARY(i).REFLECT"
".BOUNDARY(1:n).CORNER" / ".TRANSFORMATION_MATRIX" / ".OUT.NSEG" / ".OUT.SEG(i).START|END" / ".TRA"
".CUTOUT(id).TAG_CODE" / ".CUTOUT(id).PROF_REFERENCE" / ".NOTCH(n).CENTRAL_COORDINATES|CEN" / ".NOTCH(n).PARAMETER"
".STIFFENER(n).PROFILE.TYPE_CODE" / ".STIFFENER(n).PROFILE.PARAMETER" / ".STIFFENER(ref).PROFILE.TYPE_CODE"
".OC1" / ".NSUBPANEL" / ".SUBPANEL(1:n).NAME" / ".COMP_ID" / ".N<COMP>"
"HULL.CPAN('N').ISEAM(id).NAME" / ".STIF(id).NAME" ; "HULL.CPANEL..." ; "HULL.PLATE..."
"HULL.BLOCK('B').PANEL('gen'*).NAME" ; "HULL.PANEL('N').NAME"
"STRUCT.ITEM('N').GROUP(1).NPART" / ".GROUP(1).PART(i).PART_ID|POINT"
```
出处：phullnotch.pmlobj:71-146、phullcombine.pmlobj:159-1073、KcsUtilPan.py:30-164、KcsUtilDexPan.py:99-121、cPanel.py:26-145、_TBhook_AutoPanelName.py:98-133。

返回类型码（`kcs_dex.next_result()`）：1=int, 2=real, 3=string, 4=vec3d, 5=box, 6=vec2d, ≥25=4x4 变换矩阵（get_indexedreal 0..15），>10=索引实数组（typ-10 个）。PML 侧等价：`MARDEX.extractPML/nextResultPML/getIntPML/getReal/getString/getBox/getIndexedReal`。

> **权威全集（第 87 轮 XLS 入库）**：官方 DatExt_*.xls 28 份共 **1502 条唯一关键词链**（576 个完整形 token，返回类型码 s/i/r 标注）——本节源码样例仅为其中 42 个；全部关键词见 `PML语料\xls_tables\_ANALYSIS.md` §3b/§4 与 38 个 TSV。关键词树用缩写括号记法（`STIF[FENER]`、`BOU[NDARY]`）向上继承，`*` 为层级占位符。DEX 关键词→DB 属性权威映射（675 组）在 `Data_Extraction_to_Attributes.xls__*.tsv`。

---

## 7. Panel 层次与套料

**层次**：`HULL.BLOCK → HBLWLD/BLOCK → HPANEL|CPANEL → HPLATE/HBRCKT/HSTIFF/HCLIP`；面板下含语句组（PAN=组2、SUR=组3、后续 STI/NOT/CUT…），部件按 `组号+部件ID`（partId 千位分隔：`divmod(abs(Comp),1000)[1]`，KcsUtilDexPan.py:99）；子板经 `PAN ... SUB=` / `NSUBPANEL/SUBPANEL(n)`。
**套料层**：`MPLNST/MAPLNS/MPRNST` + `MPFIND` 制造包属性（hullCheckManpkg.pmlfnc:50,60）。
**制造零件悬空清理**：`var !HR collect all hrdref where (badref(hdbref) and ((type of own of own eq 'MPLATE') or ...))`（hullDeleteUnrefMANUParts.pmlfnc:22）。
**边界/开口/骨材操作**：加骨材 = STI 语句；开口 = CUT/NOT 语句；开口轮廓 `getCutoutPoints`；边界角点 `BOU(n).COR`；外轮廓 `OUT.NSEG/OUT.SEG(i).START|END`；面板平面 `getPlane`（`TRA` 4x4 矩阵→主平面判定 ±1/±2/±3）。
**勘误**：`PANELEM/TRANSPL/COMPART` 在 PMLLIB 的命中全部属 Marine Outfitting/舱室/孔管理，**不属于 Hull 船体设计建模语句体系**。

---

## 8. handle 错误码（Hull 相关）

| 码 | 语义 | 出处 |
|---|---|---|
| handle(1000, 0) | marAPI 已导入（注释明示可忽略） | phullnotchjoinsplit.pmlfnc:32-35 等 |
| (2,441) | 语法/字符串转实数错误 | phullseparate.pmlobj:229；phullrepetitionsplit.pmlfnc:42-105 |
| (2,109) | 元素名不存在（new 探测） | hullNewBlock.pmlfnc:56-66 等 |
| (2,201) | 属性不存在（MPFIND 无制造包） | hullCheckManpkg.pmlfnc:68-70 |
| (2,107) | DBREF 无效/缺失 | hullDeleteObsoleteLinks.pmlfnc:86-88 |
| (2,822) | CE 复位失败（元素已删除） | hullDeleteObsoleteLinks:167-168 |
| (2,618) | 删除制造零件失败 | hullDeleteUnrefMANUParts:29-31 |
| Python `.error` 对象 | `kcs_hullpan.error`/`kcs_chm.error`/`kcs_hull.error` | kcs_ex_hullpan01.py:48 等 |
| TBException | `e.strError=='kcs_ShrinkageObjectError'`（未设收缩量） | kcs_ex_hull_remarkinglength.py:185-193 |
| 触发器 | `kcs_util.trigger_ok()/trigger_abort()` | trig_hull_nest_structlabel.py:145-149 |
