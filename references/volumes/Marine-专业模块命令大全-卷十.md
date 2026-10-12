# Marine 专业模块命令大全·卷十（剩余 20 模块穷举·源码实证）

> 来源：PMLLIB 全部 33 个顶层目录中，排除已编目 13 卷（design/draft/paragon/router/isometricadp/isodraft/hulldesign/spooler/pipefabricationmanager/common/global/admin/limbo + icons）后，**剩余 20 个目录**逐目录扫描穷举。
> 适用：AVEVA Marine (PDMS 系) 12.1 SP4。MDS 支吊架/ASL 梯栏杆/舱室/PSI 应力/ABA 模板/装配/VNET/Integrator/关联规则全收录。

## 〇 模块总览

| 模块 | pmlfrm/pmlobj/pmlfnc | 用途 |
|---|---|---|
| mds | 424/137/1943 | 多专业支吊架（MDS）设计/Draft/Paragon |
| aba | 51/14/50 | Marine Drawing Templates 图纸模板（ABA 绘图任务） |
| accommodation | 36/26/21 | 舱室布置（房间/墙/天花板/地板/家具） |
| assembly | 13/25/53+1mac | 组件（Assembly）出图与装配 |
| asl | 17/50/17 | 梯子/斜梯/栏杆/走道（Access） |
| psi | 15/8/9 | 管道应力分析接口（Stress） |
| vnet | 4/24/19 | AVEVA NET（VNET）XML 数据导出 |
| integrator | 4/5/2 | Integrator 数据集成（喷嘴/支撑/HVAC） |
| assocs | 0/11/0 | AVEVA 关联（Association）规则创建 |
| marinedrafting | 3/2/26 | Marine Drafting（MDRA）应用外壳 |
| monitor | 12/2/17 | Monitor 登录/MDB/IDB 宏管理 |
| designreuse | 1/1/43 | Design Reuse 命名替换/导入导出触发器 |
| diagrams | 1/1/6 | Diagrams 自动命名/SVG/PDF 导出 |
| PBS | 0/0/10 | P&ID 桥接表达式/系统-对象查询函数 |
| smm | 1/5/0 | Schematic Model Manager 应用外壳 |
| lexicon | 1/1/1 | 词库应用 + PSI 节点 UDA 工具 |
| avevamarine | 0/2/3 | AVEVA Marine 启动/Block 模板 |
| tags / viewer3d / reviewinterface | 各 1 | Tags 外壳 / 3D 查看器 / Review 属性转储 |

---

## 一 mds（Multi-Discipline Supports 多专业支吊架）

**体系**：DATUM 支撑点 + ATTA 附件 + STRU 框架结构。创建类型：STRU/FRMW/SCTN/SUBS/BOX/PANE/PLOO/ATTA/PLAT/BRAC/HANG/VSPR/REDU/TEE/BRAN/PNODE/PJOI/DDSE/DDSF/GAIDTEXT；Draft 侧 SLAB/GLAB/LAYE。

### 1.1 FT15 框架吊架完整创建序列（CURSOR 模式）

`mds\design\functions\mdscreateft15.pmlfnc`（函数 `!!mdsCreateft15(!method)`，1878 行）：
```pml
-- 164-168  根据_DATUM_生成定位 PIN
PIN 1 COPY PL OF $!datum
PIN 1 plane PIN 1 CLEAR 0 BEH $!datum
PIN 1 DIR $!planeDir
PIN 2 COPY PIN 1
PIN 2 plane PIN 2 THRO $!datum
-- 389-398  探测被支撑梁截面高度
pin 1 at ppline NA start
pin 1 dir u wrt /*
pin 2 copy pin 1
pin 1 plane pin 1 clear 0 beh $!pick1
pin 2 plane pin 2 clear 0 inf $!pick1
var !pin1 pin 1 pos wrt world
!pick1size = !!kStrReal('const dist pin 1 to plane pin 2 ')
-- 1071-1099  删除旧框架并按模板重建
!!ce = !stru
delete STRU MEM
  handle (41,66) (2,113) (2,113)
  endhandle
:mdscheck $!mdstemp.:mdscheck
:mdsframirror $!mdstemp.:mdsframirror
at p9 of $!datum
NEW FRMW $!name/MAIN
-- 1116-1121  复制模板成员并改名
COPY ATTRIB OF $!frmw[1]
COPY MEM OF $!frmw[1] RENAME $!frameFormat $!name
-- 1148-1150  移动与定向
MOVE $!moveDir THRO P9 OF $!datum
ORI X IS $!orix AND Z IS $!oriz
-- 1165-1171  延伸横梁
extend start thro pin 4
extend end thro pin 9
-- 1176-1198  连接节点 UDA
:MDSConn default / :MDSXConn default / :MDSConn $!pick1 / :MDSXConn $!pick2
-- 1217  180° 旋转
ROTATE THRO PIN 1 ABOUT PIN 1 BY 180
-- 1247-1250  SREF 附件与 DATUM 对位
!!mdsMConn('ORI','ORI')
POS PA AT $!datum
SAME
-- 1638-1639  SPREF 规格选择（STYP 分类）
SEL SPREF WITH STYP 'FT15-$!styp-$!selection' SPEC /MDF
!!mdsSetSuppCode('MODIFY',!name,'FT15','FT15-N-1')
-- 1664-1666  附件引用 UDA + 派生长度
:MDSAttaRef $!references
!support.barLen[1] = deri length of CE
-- 1725  尺寸参数写回 SREF
DESPAR $!!mdsFt15.dim1.val $!!mdsFt15.dim2.val $!!mdsFt15.dim3.val $!!mdsFt15.dim4.val $!!mdsFt15.dim5.val
```

### 1.2 FT45（阀门支架）SUBS+BOX 序列

`mdscreateft45.pmlfnc`：
```pml
-- 310  delete STRU MEM + handle (41,66) (2,113) (2,113)
-- 326  NEW FRMW $!NAME/MAIN
-- 344-351  框架+鞋座 SUBS 模板复制
COPY ATTRIB OF $!Frmw[1]
COPY MEM OF $!Frmw[1] RENAME $!FrameFormat $!NAME
do !I indices !Subs
  NEW SUBS $!NAME/SUBS$!I COPY ATTRIB OF $!Subs[$!I]
  COPY MEM OF $!Subs[$!I] RENAME $!FrameFormat $!NAME
enddo
-- 368-377  定向/翻转/UDA
ORI X IS $!ORIX AND Z IS $!ORIZ
ROTATE ABOUT UP BY 180
:MdsCp2 '$!Where ; $!!MdsFt45.Offset'
-- 414-428  修立柱长度并联动 BOX/NPYR
EXTEND END THRO PIN 7
var !Boxs Coll all Box for $!<Name>/SUBS1
By D $!Move wrt worl Zlen $!NewZlen
NPYR 1
By U $!Move wrt worl
-- 452-454  双卡板（对夹阀）镜像 BOX
NEW BOX COPY PRE
MIRROR PLANE TOWARDS P2 OF CE THRO P2 OF CE
MOVE TOWARDS PRE DIST -$!!CE.XLEN
-- 478-482  SPREF/MATREF
!!MdsSetSuppCode('MODIFY',!Name,'FT45','FT45-A-1')
!!MdsSetIspe()
!!MdsSelLstu(!!CE)
```

### 1.3 TT04（Trunnion 支管托架）

`Mdssetdattt04.pmlfnc`：
```pml
443/454/506   new bran flowdir OFF
              :MDSTrun true
469           new tee
552/589/605   new atta select spref with styp 'COMMENT' spec /MDS
              sel lstu / connect
              handle (7,3)
                fconnect            $* 连接失败回退自由连接
              endhandle
              stex 'DO NOT CUT HOLE IN PIPE'
              atty CCNN
              name /$!callingForm.name.val/NOTE1
569/571       new REDU select spref with styp 'MAKEUP'/'MAKEUPOFF' spec /MDS
633-644       new atta / stext '$!name' / spkbrk true
              select spref with styp 'TT04' spec /MDS
              sel lstu / connect / shop true
              name /$!name/SREF
              :MDSSuppType 'TT04'
648-649       new PLAT despar 0mm 0mm 0mm ...    $* 底板（10 参数 DESPAR）
668-673       select spref with styp '$!sType' spec /MDS
              sel lstu / ori pl is d / name /$!name
696-704       ispe =0                             $* 全部构件去保温
              !!mdssetmatref(!!ce)
```

### 1.4 吊架对象模型与补偿板

`Mdsifh01.pmlfnc:131-187`：
```pml
!support = object MDSSUPPORT()
!oRest = object MDSREST(!styp)
!oRest.mode = 'CREATE'
!oRest.create(!!mdsFH01,!callingForm)
```
弹簧重连（MdsHangerType1.pmlfrm:962-1010）：
```pml
var !springs collect all vspr for $!oRest.ref
!oEvalSpref = object BLOCK('!springs[!evalIndex].dbref().spref')
!sprefs = !springs.evaluate(!oEvalSpref)
!!ce.spref = !oldSpre / !!ce.lsrod = !oldLsrod
```
补偿板 PANE（mdscompplate.pmlobj:456-475）：
```pml
new PANE $!ref copy $!source
!!ce.pos = e0 n0 u0 wrt owner
!!ce.ori = Y is E wrt owner and Z is U wrt owner
!!ce.spref = !spref[!c]
!!ce.matref = !!mdsCompplateDflts.matref()
rule rexe
move U wrt ce clear behind $!prev
```
照明/特殊支架（Mdsls01.pmlfrm:782-885）：`new sctn copy prev by u 300mm wrt /*`（英制 12IN）→ `reorder same after last mem` → `new pnod / pjoi 1 / jois $!pjois` → `new ddse copy rename`（handle (41,12) 重名删除重建）→ `!!ce.:MdsWeldData = !NewMdsWeldData`。

### 1.5 MDS Draft 零件表（mdspartslist.pmlfnc）

```pml
61    new laye $!Sheet/PartsList/Header
62    !EleType = Type of $!SuppName/DATUM     $* handle(2,109) DATUM 缺失回退
76-79 new slab ddna $!HeaderDdna Tmrf $!params[3]
      oset FALSE llead fals lfpen template
      xypos $!params[1] $!params[2]
82    new laye $!Sheet/PartsList/Entry
120   new slab copy $!SlabName
125   by y (7 * $!loop9)
126   Atex |$!seq\$!AtexAr[$!Loop9]|
128   ddnm $!DdnmAr[$!Loop9]
138-141 new glab ddnm $!SuppName
      oset fals chei 3.5 align hbody just right llead fals lfra fals
      xypos $!xypos / by y 13 / by x -2
```

### 1.6 mds 特有 handle 错误码（2965 处，按频次）

| 码 | 次数 | 语境 |
|---|---|---|
| (2,109) | 628 | 参数/平面定位不存在；元素查询回退 |
| (61,528) | 455 | DAC/权限与规格选择冲突 |
| (7,3) | 266 | connect 失败 → 回退 fconnect |
| (61,567) | 236 | 选择项非法，回退空选择 |
| (2,752) | 225 | PARAM[n]/DESPAR[n] 越界（源码注释 "param does not exist"） |
| (41,66) | 160 | delete STRU MEM 失败（框架重建前清理） |
| (2,113) | 98 | 名称冲突/成员删除次级错误 |
| (2,252) | 74 | 集合/成员查询空 |
| (99,532) | 54 | 电缆/特殊件处理 |
| (2,822) | 41 | 元素引用失效 |
| (41,12) | 39 | 名称已存在/改名失败（重名重试） |
| (2,357) | 12 | PIN 方向为空防护（mdscreateft15:886-890 `pin 5 dist -10` 补偿） |
| 其他 | — | (2,18/102/107/111/142/201/207/235/253/502/605/614/751/754/756/759/767/779/785/794/812/813)、(41,8/25/52/69/232/322/324/325)、(42,64)(42,94)(43,383)(73,214)(61,7/93/115/251)(160,46) |

---

## 二 asl（Access：梯子/斜梯/栏杆/走道）

创建类型：PLTFRM/STRFLT/STRSTR/RPATH/HANDRA/GENSEC + 标准库 APPDAR/APPLDA/DDSE。

### 2.1 平台（dbepltfrm.pmlobj:1374-1417 .updateDb）

```pml
if !this.dbElement.badref() then
  if !this.dbElement.unset() then
    new PLTFRM
  else
    new PLTFRM ref $!<this.dbElement>      $* 挂到指定参考元素
  endif
endif
UNNAME
!!ce.description = !this.description
!!ce.numb / !!ce.area / !!ce.thickness / !!ce.position / !!ce.orientation
asstmp $!<this.tmplReference>
desp $!this.posType
matref $!<this.matref>
!this.rpathRef = !this.rpath.dbWrite(!this.rpathRef)      $* 边界 RPATH
do !c indices !openings                                    $* 开孔 RPATH
  !rpathRef = !!dtbMemberOfType(!!ce,'RPATH',1)
  !this.openings[!c].dbWrite(!rpathRef)
enddo
```
RPATH 创建：`aslrpath.pmlobj:706-708`（`new RPATH` / `new RPATH REF $!ref`）。

### 2.2 斜梯段（dbeaslstrflt.pmlobj）

```pml
3015-3022  !!ce = !owner
           handle(2,822)          $* 表单打开期间元素被删
             !!alert.error('Element $!owner is an invalid Reference...')
3024       NEW STRFLT
3054-3062  !!ce.position / fThickness / lRise / rise / fltDirection
           / tWidth / headRoom / instOptions / assTmpReference
3065-3071  NEW RPATH                       $* 踏步路径
3077-3081  !stringers = !this.readElements('GENSEC','OHTYPE EQ |STRSTR|',!this.refe)
           delete GENSEC                   $* 重建前清旧腹板梁
3084-3087  NEW STRSTR
3112-3114  !lStringerPath.vertex[1].offset(D, !lowLandingOffset)
```

### 2.3 栏杆（aslhandrail.pmlobj:3885-3928）

```pml
!undo = object UNDOABLE()
!undo.description('Create/update handrail')
!undo.undoaction(!this.undoCall) / !undo.redoaction(...)
if !this.refe.badref() then
  new HANDRA
else
  delete HANDRA members             $* 重建成员
endif
UNNAME / !this.refe.name = !this.name
!!ce.railHeight = !this.railSpacing
!!ce.postSpacing = !this.postSpacing
!!ce.tangOffset = !this.tangentSpacing
!!ce.closeFlag / !!ce.ePostOffset / !!ce.pos / !!ce.ori
!!ce.bradius / !!ce.number / !!ce.area / !!ce.desc
```
分段插入 `:1602`；门槛/门 EDG 拾取（aslhandra.pmlfrm:2028-2099）；梯子侧板 `NEW HANDRA copy $!allLdrHandra[1]`（aslladderdata.pmlobj:686）。

### 2.4 标准库（aslcentraldata.pmlobj:1780-1849）

```pml
DELETE APPDAR / NEW APPDAR
!standard.refe.purpose = 'ASL'
DELETE APPLDA / NEW APPLDA
var !dataset collect all DDSE for ce
```
复制建标：`new APPDAR copy $!toCopy`（aslcreatestandard.pmlfrm:255）；`NEW DDSE`（aslfabricatorstandards.pmlfrm:139）。
特有 handle：`handle(2,822)`（dbeaslstrflt.pmlobj:3019，无效 owner 引用）；其余全部 ANY/NONE 对象级容错。

---

## 三 accommodation（舱室布置）

创建类型（穷举 40+）：ROOM/STRWELL/CEILING/CLNCGR/CLNTIL/CLNLAT/CLNPNG/CGRDCP/CGRDLP/HVACFI/INFITT/FPFITT/ELFITT/WLFITT/WLOPEN/WLFEAT/WLPANE/WLCOMP/WLJNTS/WLJOIN/WLPRSE/WLPROF/CTWALL/HATTA/TATTA/RPATH/POINTR/CURVE/DETGRP/BNDLIN/LOOP/AREADEF/AEXTR/FLRCOV/FLRLAY/FCUTPL/INSURQ/OPENSP/RSTARE/BBLOCK/BLEVEL/PANE/PLOO/GENSEC/SPINE/POINSP/JLDAT/PLDAT/FIXING/REST/HANG/SCLA。

### 3.1 ROOM 母序列（accroombasics.pmlobj:118-301）

```pml
NEW BNDLIN
!!ce.description = 'Boundary'
NEW LOOP
!this.definition.outerLoop.dbWrite(CE)
NEW AREADEF
NEW AEXTR
!!ce.obs = 0
RULE SET HEIGHT STATIC (heiDefault of ROOM)     $* 规则驱动高度
NEW LOOP
NEW DETGRP
!!ce.purpose = 'CLN'
NEW CEILING
!ceiling.clnHeight = !element.clnHeight
!ceiling.clnVoid  = !element.heiDefault - !element.clnHeight
!ceiling.colSchema = !element.colSchema
NEW BNDLIN / COPY $!<boundary>
NEW AREADEF / NEW CLNPNG
NEW DETGRP / NEW FLRCOV / NEW FLRLAY / NEW LOOP
```
同构：accceilingbasics.pmlobj:125-231（含 NEW PANE/NEW PLOO）、accstrwelldefinition.pmlfrm:1250-1273、accrstaredefinition.pmlfrm:937-955、accopenspdefinition.pmlfrm:957-1016、accmainrefdata.pmlfrm:2243-2732。

### 3.2 墙板分割（accwalldetailing.pmlfrm:2640-2683 .createPanel）

```pml
!collection.type('WLCOMP')            $* 查找墙板组件组
NEW WLCOMP                            $* 不存在则建
NEW WLPANE
!element.name = '/' & !name
!element.description = !this.panDesc.val
!element.spref = !this.panSPREF.val.dbref()
!element.zdistance = !this.panDist.val
!element.posRef = !this.panStart.selection().dbref()
!element.wJusLine = 'CENT'
```
其余：NEW WLJNTS/WLJOIN（墙接缝 6 处）、NEW WLPRSE(2498)、NEW WLPROF(2570/2593)、NEW WLPANE（9 处）。

### 3.3 天花格栅与吊件

```pml
-- accceilingsupports.pmlfrm:1737-1778
NEW JLDAT / NEW PLDAT / NEW FIXING / NEW REST / NEW HANG / NEW SCLA
-- :2434-2469 格栅建模
NEW CLNLAT / NEW GENSEC / NEW SPINE / NEW POINSP ×2
-- accceilinggriddefinition.pmlfrm:3742-4009  12 组龙骨
NEW GENSEC / NEW SPINE / NEW POINSP×2
-- accceilingfittings.pmlfrm:820-902
NEW CLNCGR / NEW CGRDCP / NEW CGRDLP / NEW HVACFI / NEW INFITT / NEW FPFITT / NEW ELFITT
-- :1066-1076  COPY LIKE PREV
NEW CGRDCP COPY LIKE PREV / NEW CLNTIL COPY LIKE PREV / NEW CLNTIL（逐格铺板）
```

### 3.4 壁装件/开孔/家具/平面布置

```pml
new WLFITT copy prev / new WLOPEN copy prev        -- accfittingsdefinition.pmlfrm:3926-3943
NEW WLFEAT → NEW WLOPEN → NEW RPATH                -- accopeningdefinition.pmlfrm:3471-3487
NEW CTWALL / NEW HATTA / NEW TATTA / NEW RPATH / NEW POINTR / NEW CURVE  -- acclayout.pmlfrm:2258-2389
NEW INSURQ / NEW LOOP                              -- dbeinsurq.pmlobj:420-444
NEW FLRCOV / NEW LOOP / NEW FLRLAY / NEW FCUTPL
NEW OPENSP / NEW RSTARE / NEW STRWELL / NEW CEILING / NEW AREADEF / NEW BBLOCK / NEW BLEVEL
NEW ROOM COPY $!<this.baseElement>                 -- acccrestdroom.pmlfrm:888/900
```
特有 handle（34 处）：(2,751)×11、(2,795)×5、(2,707)×4、(61,567)×2、(2,109)/(2,111)×2 等；命名校验统一 `!!checkName(!gadget.val,'NEW')`。

---

## 四 psi（管道应力分析接口）

**体系**：ZONE purp='PSI' 下建 PIPE 应力组、BRAN desc=工况名、REST 约束、TEXT 应力文本；`:PsiSystem` UDA 数组在分支/管件间传递节点与工况。创建类型：ZONE/PIPE/BRAN/BEND/REST/TEXT/动态管件。

```pml
-- stressgroup.pmlobj
299         delete pipe                      $* 删除整个应力组
1488/1511   :PsiSystem default / !!ce.:PsiSystem = !list
1973-1977   delete rest
            elsehandle (2,109)
            new rest                         $* 节点约束重建
1997        new text $!newName
2524        delete text
2804        !branchSize = !this.pipe.:PsiSystem.size()
2826-2831   handle (2,113)
            new bran $!branName
            handle (41,12)                   $* 重名重试
            !!ce.:PsiSystem[1] = !this.pipe.:PsiSystem[!b]
2864-2871   !save = !!ce.:PsiSystem
            copy like $!!ce.:PsiSystem[1]    $* 按源分支复制
            !!ce.:PsiSystem = !save
            !!ce.hpos = !!ce.:PsiSystem[1].hpos / hdir / hconn / hbore
3484/3505   new bend
-- stresscomp.pmlobj:232-299  应力管件动态创建
!!ce = !this.owner
new $!this.type after last mem
handle ANY
   new $!this.type
endhandle
copy $!this.sourceComp
at $!this.sourceComp.position.wrt( /* )
-- psiresetbends.pmlfnc:27-30
var !a coll all bend with spref eq /PSI-SPEC/VARI for ce
delete bend
-- PsiCreateGroup.pmlfrm:56
new pipe $!this.name
-- 查询基架
var !zones Coll all ZONE with purp eq 'PSI'
```
PSI 节点 UDA（lexicon\objects\PSINodeUDAS.pmlobj:73-162）：`:PsiSystem / :PSISifValue / stressdate / PSINodeType / PSINodeGap / PSINodeStiffness / PSINodeFriction / PSISifNumber / :PsiWeight / :PSIDate`。
默认值文件：`%pdmsuser%/Psi-defaults.xml`（PsiDefaults.pmlfrm:420）。

---

## 五 aba（Marine Drawing Templates 图纸模板）

创建类型：DEPT/REGI/DRWG/SHEE/DRTMLB/DRTMPL/SHTMPL/LIBY/DLLB/IDLI/ADDE/PLLB/SPLA/WPOS/VSEC/VIEW/LAYE/TASK/TKPARA/TRLB/TRST/TAGR/NOTE/TEXP/STRA/SYMB/RECT/LDIM/DPOI/GLAB/SLAB/VNOT/OUTL/VRTX/OLAY/LNDESC。

### 5.1 模板层级（abacrhierarchy.pmlfrm:116-184）

```pml
NEW LIBY $!!abaDefaults.alib.val
delete DLLB
NEW LIBY $!!abaDefaults.libr.val
NEW DRTMLB $!!abaDefaults.dlib.val
NEW DLLB $!!abaDefaults.disl.val
NEW SHLB  $!!abaDefaults.keyp.val
NEW SYLB  $!!abaDefaults.symb.val
NEW TRLB  $!!abaDefaults.labl.val
NEW TASKLB $!!abaDefaults.task.val        $* 每条均配 delete + handle 防重
-- abacreregistry.pmlfrm:143-171
NEW DEPT $!element ×2 → NEW REGI /$!this.regi.val
```

### 5.2 图纸模板与变体复制（abatemplatesht.pmlfrm:264-309）

```pml
NEW SHTMPL
  handle(41,8)              $* 该层级不允许建 SHTMPL
    return
  endhandle
Name $!newName
NEW SHTMPL $!newName COPY $!oldName RENAME $!oldName $!newName
title unset
SPPURPOSE ABAT              $* ABA 专用用途标记
FUNCTION '$!func'           $* 'Master' / 'Variant n'
NEW LIBY $!libyname / SpPurpose ABAT
  handle (61,567)
```

### 5.3 视图全子结构（abauserview.pmlfrm:1030-1124 .createView，最具代表性）

```pml
NEW VIEW
  handle (41,8)
    !!alert.error('Cannot create a VIEW at this level.')
do !x
  NAME $!name/V$!x
    handle (41,12)            $* 重名递增编号
    elsehandle none
      break
enddo
title |$!title|
size $!sizeX $!sizeY
SpPURP ABAT
Lframe True
NEW LAYER NAME $!name/Tasks       SpPURP ABAT
lvis false
NEW LAYER NAME $!name/USER_Dims   SpPURP DIMA  PURP DIMA
NEW LAYER NAME $!name/USER_Labs   SpPURP LABA  PURP LABA
NEW LAYER NAME $!name/USER_Notes  SpPURP NOTA  PURP LABB
NEW LAYER NAME $!name/USER_Tags   SpPURP TAGA  PURP TAGA
View
!!ce = $!dName/LIBY
NEW DLLB name $!vName/IDLIST
  handle (41,12)
    delete DLLB
  elsehandle none
    SpPurp ABAT
    NEW IDLI name $!vName/IDLIST/IDLI
      SpPurp ABAT
NEW PLLB name $!vName/PLANES
  handle (41,12) delete PLLB elsehandle none SpPurp ABAT endhandle
NEW TRLB name $!vName/TAGLIB
  handle (41,12) delete TRLB elsehandle none SpPurp ABAT
    NEW TRST name $!vName/TAGLIB/TAGS
      SpPurp ABAT
TRSF $!vName/TAGLIB/TAGS          $* 关联 tag 规则集
$!vName
IDLN $!vName/IDLIST/IDLI
```
复制视图/库（:871-1038）：`NEW VIEW $!newName COPY $!oldName RENAME ...`、`NEW DLLB/IDLI/PLLB/TRLB/TRST ... COPY [RENAME ...]`。

### 5.4 图纸生成（abadrawing.pmlobj）

```pml
534/544    DELETE TASK / NEW TASK $!sheeTaskName COPY $!shtmplTasks[$!task]
649-652    delete LAYE / NEW LAYE $!sheeLayeName COPY $!shtmplLaye[1] RENAME $!shTmplRefe.flnm $!sheeName
666        DELETE IDLI MEM
723        NEW SHEET $!newName COPY like $!template
912/938    DELETE DRWG / NEW DRWG $!this.drwgName
988        NEW LIBY $!this.drwgName/LIBY
993        NEW $!membType $!newName COPY $!membRefe RENAME $!this.template.name $!this.drwgName
```
任务参数（abatasklist.pmlobj:232-263）：`DELETE TASK` → `NEW TASK $!taskName` → `NEW TKPARA tpvalue |$!taskobj.paramVal[$!count]|`。

### 5.5 键图/边界框/清单图元

```pml
-- ababuildkeyplan.pmlfnc:69-147
NEW LAYE / NEW VNOT / NEW OUTL
NEW VRTX ORIGIN E $!<minPos.east> N $!<minPos.north> U 0   $* 矩形4顶点
NEW VRTX SPAN TO CLOSE
-- ababuildkeyplan.pmlfrm:345-385
DELETE NOTE / NEW NOTE / NEW TEXP AT X $!xPosS Y $!yPosS
NEW STRA FPT $!lineStart TPT POS $!lineEnd
NEW SYMB AT X $!xPosL mm y $!yPosSymb mm
-- abaequicldimn.pmlfrm:111-191（设备布置图模板）
NEW DEPT/REGI/DRWG/SHEE/NOTE/RECT×2/VIEW/LAYE/LDIM/DPOI POS W25 N26 U0
NEW LAYE $!name/up|down|left|right → NEW LDIM + 3×NEW DPOI（四向尺寸）
-- abaarrange.pmlfrm:155-158
NEW GLAB BTEX '       ' on $!siteRefe → NEW GLAB COPY PREV BY X17 BPOF 0 29.99
-- abadrawlist.pmlfrm:551-592
NEW DLLB / NEW IDLI / NEW ADDE / NEW ADDE IDNA $!idliRefe / DELETE IDLI MEM / DELETE NULL IDLI
-- abaview.pmlobj:368-435
new pllb / NEW SPLA $!view.name/spla1 / new wpos pos e.. n.. [u..] ×8 / NEW VSEC ×2
-- TAG 规则
new tagr / delete tagr（abatagrules.pmlfrm:192-224）
new trlb .../tagrules / new trst .../trst1 / NEW TAGR（abatagging.pmlfrm:339-408）
NEW OLAY $!olayName（abakeyplan.pmlfnc:77）
```
特有 handle：(41,8)（层级禁止创建 VIEW/SHTMPL）、(41,12)（重名循环命名/删除重建）、(61,567)（选择回退）。

---

## 六 assembly（组件出图）

创建类型：DEPT/REGI/DRWG/LIBY/DLLB/IDLI/ADDE/TASK/SHEE/VIEW/LAYE/LNFOLD/AXESYM/SLAB/VNOT/STRA/TEXP/TABL。

```pml
-- assydrwg.pmlobj
89         NEW DRWG
124        DELETE DRWG MEM
204-222    NEW LIBY / DELETE LIBY / DELETE LIBY MEM
           NEW DLLB / NEW IDLI / NEW ADDE IDNM $!<this.asmblyRefe>
301        NEW TASK COPY $!taskRefe NAME $!taskName
466        DELETE SHEE
-- assydrwghier.pmlfrm:323-452
DELETE $!!<ce.type> / NEW DEPT $!name / NEW REGI $!name
-- assydrwgapplication.pmlobj:411-415/835
NEW DEPT / NEW REGI / NEW LNFOLD（折线）
-- assysheet.pmlobj:119-174
NEW SHEE $!sheeName / DELETE SHEE [MEM] / NEW TASK COPY ...
-- assypartslist.pmlfnc（SLAB 表格引擎）
86    NEW VIEW $!viewName IDLN =0
103   NEW LAYE / 110 DELETE LAYE MEM
142   NEW SLAB $!titleName ON $!asmblyRefe TMRF $!<tableObj.titleSytm> OSET FALS
151   NEW SLAB $!headerName COPY PREV BY $!move TMRF $!<tableObj.headerSytm>
212   NEW SLAB $!headerName COPY PREV BY $!move TMRF ... ON $!partRefe
223   NEW SLAB $!cellName COPY $!rowSlab ATEX |$!<values[$!i][$!c]>| TMRF $!tmrf ON $!partRefe
264   NEW SLAB $!cellName COPY PREV BY $!move ATEX |$!bits[$!number]| TMRF $!tmrf
-- assyboundbox.pmlfnc:85-280
DELETE LAYE MEM → NEW LAYE → NEW VNOT → NEW STRA ×13（包围盒12边）
NEW TEXP CHEI $!chei BTEX '$!leng' ADEG $!adeg JUST C ALIG TB|BB
-- assycraxes.pmlfnc:126-156
DELETE AXESYM / NEW AXESYM（中心线符号）
-- 修订区（assybacksheet.pmlobj:51-168，读取型）
VAR !reviArea COLL ALL TABL WI (UPCASE(spPurp)) EQ 'REVISI' FOR $!backRefe
!this.reviOrigin = !this.reviArea.ptrf.xypo
!this.reviXlen = !this.reviArea.xlen
!this.reviFDir = !this.reviArea.fillDirection      $* LEFT/RIGHT/UP/DOWN
!maxEntries = !this.reviArea.ncol | .nrow
```

---

## 七 vnet / integrator / 小模块

### vnet（AVEVA NET XML 导出，无 DB 元素创建）

```pml
-- VNETExport.pmlfrm:696-749 .ExercuteExport
pml index
!a = object VNETWriteXML()          $* Design（marine designtype 1/3）
!a = object VNETWriteASMXML()       $* Design（designtype 2 装配）
!a = object VNETWriteSPLXML()       $* Spooler 模块
!a = object VNETWriteXML()          $* Draft 模块
REPR UPDATE
!!VNETError.Reset()
```
输出目录默认 `%PDMSUSER%\VNET-DesignXML / VNET-LinksXML / VNET-SpoolerXML / VNET-AssemblyXML / VNET-ManufacturingXML`。XML 头 `<?xml version="1.0" encoding="UTF-8"?>` + 命名空间 `http://www.aveva.com/VNET/List`；特殊字符转义 `!!VNETStripXML(!name)`。

### integrator

```pml
return error 1 |Must be in Lexicon to load UDA definitions|
NEW UWRLD /AVEVA/INTEGRATOR/UWRL
NEW UGROUP /AVEVA/INTEGRATOR/UGRO
NEW UDA /ACCEPT2D3DDIFFERENCE / MATCHINGENABLED / AVINT_UPDATE_DATE / AVINT_COMMENTS / AVINT_UPDATE_USER
OLD UDA /AVINT_UPDATE_DATE        $* ULEN 修复场景
-- 喷嘴（intequinozzspec.pmlfrm:530-557）
DELETE $!type → NEW ELCONN → NEW NOZZ
-- 支撑映射（IntegratorSupportHandler.pmlobj:620/1764）
DELETE $!type / new tmpl
-- HVAC（IntegratorHvac.pmlobj:1334）
:HXYSIZE UDA 缺失告警 write 'UDA definition :HXYSIZE not found'
```

### 小模块扫尾

- **assocs**（关联规则，55 条命令全在 avevaassociation.pmlobj）：`NEW ASSOC` → `ADEFRF /av-exists2` → `NEW RESTRI` → `LNAME /av-exists2-rd1` → `NEW MBRMAP` → `AMAPNME /av-exists2-ref1` → `NEW ASSMBR` → `AMEMRF $!dbref1`；类型 ASSOC/RESTRI/MBRMAP/ASSMBR/DDSE/DDAT。
- **designreuse**（43 函数无 NEW/DELETE）：导入导出触发器 + 35 类元素命名构造器（buildpipename/buildbranname/buildfrmwname/buildcpanelname/...）。
- **diagrams**：autonameelements/autonameceoffspring（批量自动命名）、exporttosvg、visioexporttopdf。
- **marinedrafting**：唯一 DB 命令 `NEW LNDESC`（addtolinkdoc.pmlfnc:64）；其余 gadpcreateshee/gadpcreateview/gadpdimtool/setmarptype 等封装。
- **monitor**：唯一 DB 命令 `DELETE MACRO $!macNumb`（delidbmacro.pmlfnc:46）。
- **PBS**：10 个查询函数（ExecutePBSExpression/GetAllRefNo/getItemsForSystem 等），无 DB 写。
- **smm/tags/viewer3d/reviewinterface/avevamarine**：应用外壳与启动链，无建模命令。
