# Marine 规格库（Paragon/Catalogue）操作命令大全（穷举级·源码实证）

> 来源：逐文件读取 PMLLIB\paragon\ 全部 105 文件（44 pmlobj + 18 pmlfnc + 51 pmlfrm）+ PDMSUI\CAT\ 31 个 PML1 宏 + common\objects 规格对象 + design\objects 规格对象 + 根目录 nominal_bore.mac(191行)。
> 所有代码块均带源文件路径与行号。

## 0. 术语勘误（12.1 实测）

- 元素类型名是 `SPWLD`（规格世界），但属性查询写法用 `SPWL`（如 `SPWL OF $!spec`、`PURP OF SPWL`）——两者都在官方代码出现。
- **SPWE 层不存在**：12.1 中 SPEC 直接挂在 SPWLD 下，无中间规格元素层。
- 经典 PDMS 的 `CDATE/CATL` 在本版本体现为 SPCO 的引用属性 `CATR/DETR/PRTREF/TMPREF`（指向目录 SCOM 元件 / SDTE 明细文本 / GPART 零件），未见 CDATE/CATL 命令。
- `SELE`（选择器）与选择表（TABGRO 系）并存：旧式规格用 SELE/SPCO，新式选择表用 TABGRO/CTABLE/TABHEA/TABHQU/TABITE/TABQUE。

## 0.1 源码地图

| 目录 | 内容 |
|---|---|
| `PMLLIB\paragon\objects\` | 44 对象：SELECTIONTABLE、CATUPGRADESPEC、SPCSPEC/SPCSPECCOMPONENT/SPCSCOM/SPCSKEY/SPCSKEYRULE/SPCPOINTSET/SPCPOINTRULE/SPCPCONNLIST、PARTSFROMSPEC、CATSPECVIEWS(10048行)、CATSELTABVIEWS(2511行) 等 |
| `PMLLIB\paragon\functions\` | !!catCreate、!!creCataElements、!!creCocoElements、!!creNominBoreElements、!!catgetspecdiscipline、!!catValidateNameField/RefField、!!catSetCateReferences |
| `PMLLIB\paragon\forms\` | 51 窗体：!!catCreate、!!convertspec、!!insuDefineMain、!!stchoose、!!spcSpecReport 等 |
| `PDMSUI\CAT\specs\` | 31 个 PML1 宏（f/i/m/x 前缀 = Form/Init/Method/eXecute） |
| `PDMSUI\CAT\gen|pipe|clib\` | 组件/SKEY/PARAM 创建宏；`dflts\purpose`、`dflts\standard-headings` |
| `PMLLIB\common\objects\` | SPCSEARCH、SPCSPECIFICATION、SPCLINK、SPECDATA、NAMOPT、CHECKNAME |
| `PMLLIB\design\objects\` | SPECIFICATION(22KB)、SPECIFICATIONS、SPECDFLTS、SCTNSPEC、HVACDETAILSPEC |

---

## 1. 规格世界（SPWLD）操作

### 1.1 创建 SPWLD（PML2，含 PURP 一步完成）

`paragon\forms\insudefinemain.pmlfrm:2236-2248`（保温规格自动建库）：
```pml
var !spwld collect all SPWLD with PURP eq 'INSU'
if (!spwld.unset() OR !spwld.size().eq(0)) then
    NEW SPWLD PURP INSU                $* 创建+目的一步完成
    NEW TABGRO PURP INSU
    NEW CTABLE DESC 'INSULATION'
    NEW TABHEADER
else
    !!CE = !spwld[1].dbref()
    var !tabgro collect all TABGRO with PURP eq 'INSU' for CE
endif
```

`design\objects\hvacDetailSpec.pmlobj:109-111`（宏文本数组式）：
```pml
!lines.append(|OLD SPWLD /HVAC_Detailing_Specifications|)
!lines.append(|  NEW SPWLD /HVAC_Detailing_Specifications|)
```

### 1.2 PML1 宏创建（PDMSUI\CAT\specs）

`specs\mcrtspwl:30-34`：
```
 NEW SPWLD
 CALLIB UNAMECHK _CDTCRTSPWL_NAME      $* 名字校验例程
 PURP $!TSPWL
 DESC |$!DESC|
```
`mcrtspec:51-64`（自动补建 SPWLD）：
```
   confirm |No SpecWorld found, OK to create one.|
   if($_CALERT_USERDATA) then
     World
     New SPWL
     handle ANY
       return error 1 |Unable to create a SpecWorld. $!!error.text|
     endhandle
     PURP $!TSPWL
     DESC '$!DSPWL'
```
`mcrtspec:66-84`（SPWLD 上溯导航 + 只读检查 + 建 SPEC）：
```
 !elem = !!ce
 do
   break if (!elem.owner.unset() or !elem.type eq |SPWL|)
   !elem = !elem.owner
 enddo
 if (!elem.type ne |SPWL|) then
   return error 1 |Specifications can only be created beneath a specification world|
 elseif (dbwrite ne true) then
   return error 1 |The specification could not be created - the database is read only|
 endif
```
下拉数据装载：`fcrtspwl:51-59` 用 `var list _CDCSPECKEY_SPWL sel $!INDX` + `var !DATA split ... |\|`。
目的枚举全集（`PDMSUI\CAT\dflts\purpose`）：`STL STFX PIPE BRAN REDU PTAP HVAC EQUI ROOM TRAY CORE REPR`。

### 1.3 规格世界导航/遍历

- 命令导航：`SPWL`（跳到规格世界）——selectiontable.pmlobj:240、catcreate.pmlfrm:1079。
- 属性式：`!spwlEl = SPWL OF $!spec`（spcspecselect.pmlfrm:201 等多处）。
- 表达式：`object EXPRESSION(|PURP EQ 'NOZZ' AND PURP OF SPWL EQ 'EQUI'|)`（equmeicreatenozzle.pmlfrm:191）。
- 链式：`var !spwlPurp PURP OF SPWL OF SPREF`（spchvacspecsel.pmlfrm:223）。
- 多类型收集：`var !spwl COLLECT ALL ( SPWL PRTWLD TABGRO )`（design\forms\tmplpropagate.pmlfrm:506）。
- 世界层收集（common\objects\spcsearch.pmlobj:134-141）：
```pml
goto frstw CATA
var !spwlds SPLIT MEMB SPWL
do !i indices !spwlds
  var !c COLLECT ALL SPEC WITH ( $!<rule> ) for $!spwlds[$!i]
  !collection.appendArray(!c)
enddo
```
- 判定：`!list[!n].type inset('SPWL','SPEC')`；HVAC 识别用 `specification.namn` 前缀 `CADCHVAC/AVEVAHVA`（catgetspecdiscipline.pmlfnc:113）。

---

## 2. 规格定义（SPEC）操作

### 2.1 NEW SPEC 全部变体

`paragon\forms\catcreate.pmlfrm:1074-1096`（双写法兜底）：
```pml
if (!name.set() and !name.empty().not()) then
  new spec $!name question TYPE          $* 主写法：首问题 TYPE
  handle ANY
    SPWL                                 $* 导航到规格世界
    !dbpos = !!ce
    speconmode                           $* 进入规格写模式
    !!ce = !dbpos
    new specification $!name             $* 备用写法
    handle any
    exit                                 $* 退出 speconmode
    return error 1 |$!!<error.text>|
  endhandle
exit
endhandle
```
复制式创建（11.6→12.0 规格升级，`catupgradespec.pmlobj:492-512`）：
```pml
speconmode
handle (47,15) endhandle
!!ce = !specWorld
!partSpecName = !this.specPrefix & !specification.name
new spec $!partSpecName COPY $!specification.name RENAME $!specification.name $!partSpecName
handle (17,19)
    !!alert.error(!!error.text)
    exit
!partSpec = !!ce
endhandle
```
PML1 批量：`mcrtspec:81-84` `New SPEC / CALLIB UNAMECHK ... / PURP $!TSPEC / DESC |$!DESC|`。

### 2.2 SPEC 属性

- `PURPOSE $!purp`（catcreate.pmlfrm:1194、1334）。
- `!!ce.purp = ...`；STFX 特判改 SPTYPE（catcreate.pmlfrm:1058-1068）；`!newSelTab.sptype = !this.disciplineID`（catupgradespec.pmlobj:143-146，`handle (2,793)` 非法字符兜底）。
- 管理属性（catspecviews.pmlobj:4092-4095）：`!!ce.description / .finputby / .fissue / .fstatus`。
- 规格类型→PURP 映射（:4079-4083）：`if (!discipline eq |PIPING|) then !form.specdbref.purpose = |PIPE| else ... = !discipline`。
- 目的枚举全集（catgetspecdiscipline.pmlfnc:35-214）：`PIPING/INSU/TRACING/BOLT`；`EQUI/SUBE/ESPT/NOZZ`；`STL/PLT/PFIT/JOIN/WALL/FLR/WFIT/FFIT/SBFI/FITT`；`HVAC`；`HANG HCFG HMML HCLR SSTL SCFG HSPT`（吊架）；`ASL ASLF HAND`（梯子）；`PENI PENH`（贯穿件）；`TRAY`（托架）；`LIMB`（判断 `!specification.question eq 'LIMB'`）；回退读 `STEXT OF TEXT 1`（行163-200）。

### 2.3 CAD 侧参数

`catspecviews.pmlobj:4507-4528`（applySpecCadAtts）：
```pml
!form.specification.setlineType(!form.opSpeclineType.selection())   -- NULL/FP/FX
!form.specification.setbltmethod(!form.opSpecBltMeth.selection())   -- 螺栓连接方法
!dimension = object MEASURE('Pressure')
!rating = !form.txSpecRating.val.cast(!dimension.currentUnits())
!form.specification.setRating(!rating.dbUnits())                    -- 压力等级(库单位)
!this.setRefStr(!form, !form.specification, |MATREF|, ...)   -- 材质
!this.setRefStr(!form, !form.specification, |FLUREF|, ...)   -- 流体
!this.setRefStr(!form, !form.specification, |BSPEC|, ...)    -- 支管规格表
!this.setRefStr(!form, !form.specification, |NOMREF|, ...)   -- 公称通径表
!this.setRefStr(!form, !form.specification, |BRREF|, ...)    -- BRTAB
!this.setRefStr(!form, !form.specification, |REDREF|, ...)   -- REDTAB
!this.setRefStr(!form, !form.specification, |PDAREF|, ...)   -- PDATAB
```

---

## 3. 元件目录（SPCO/SCOM/GPART/PPOINT/SKEY/COCO）

### 3.1 SPCO 创建全流程（catspecviews.applyCompAdd :6216-6350）

```pml
!specComp = object SPECCOMPONENT(!form.currentHdg)                 -- 核心对象构造
!specComp.addStringAnswer(!type,  !form.currentQues.findFirst(!typeQuestion))  -- TYPE/BTYP/INSU
!specComp.addStringAnswer(!stype, !form.currentQues.findFirst(|STYP|))
!specComp.setRef(|PRTREF|, !prtCatRef)     -- GPART 来源
!specComp.setRef(|CATREF|, !prtCatRef)     -- SCOM 来源
!pbore = !addFromName.dbref().catref.ppbore[!pboreNum]
!specComp.addRealAnswer(!pbore.real(), !val)                       -- 通径答案
!specComp.rename(!form.specification.name() & '/' & ...)
!specComp.setExisting(false)
!form.currentHdg.addComponent(!specComp, 0, true)                  -- 挂入标题
```
类型判定（:6232-6252）：首问题 `TYPE`→普通、`BTYP`→`BOLT`、输入框 `INSU`→`INSU`。
通径组合（:6352-6474）：`USER`（3 PBOR→BRANCH、2→REDUCER）、`BRANCH`（pbores[1]=header, [2]=branch）、`REDUCER`（大/小两两组合）、`INSU/BOLT`（`object BORE(!val.real())` + `object BORE(0)`）。
SCOM/GPART 收集（:6478）：`var !itemRefs collect all (scom gpart) for $!<addFromName>`。

### 3.2 SPCO 删除/移入 Limbo（speconmode 保护）

`catspecviews.pmlobj:3296-3321`：
```pml
!this.speconmode('speconmode')
do !val values !rows.invert()
  !component = object SPECCOMPONENT(!form.currentHdg, !val)
  old specification $!<specName>
  if (!delete) then
    !!ce = $!<name>
    !type = !!ce.type
    delete $!<type>                     -- 永久删除
  else
    remove $!<name>                     -- 移入 Limbo
  endif
enddo
!this.speconmode('exit')
```
安全封装 :1739-1754（`handle (47,15)` 防重复进入）。

### 3.3 SELE 选择器（旧式规格 PML1 全集）

`PDMSUI\CAT\specs\mbldspec:28-148`（Build Specification 完整流程）：
```
 $!SPEC
 LOCK ALL
 UNLOCK CE
 var !SPQU |TYPE|                       $* Spec Question
 var !SEQ1 |PBOR|                       $* Sele Level 1 Question
 var !SCAN1 |answ (PPBORE 1 of CATR)|   $* Spec Component Answer
 var !SCAN2 |maxa (PPBORE 1 of CATR)|
 if(PURP of SPWL eq |STL| and PURP of SPEC eq |STL|) then
   var !SEQ1 |GTYP|                     $* 钢结构改用 GTYP
   var !SCAN1 |tans (gtype of catref)|
 endif
 DESC |$!DESC|
 QUES $!SPQU                            -- 设置 SELE 问题
 do !SELE indices !!CDCADESC
   if($!NFLG) then
     $!SPEC
     NEW SELE DESC |$!SDESC|            -- 新建选择器
   else
     $!SSELE
     UNLOCK CE
   endif
   QUES $!SEQ1                          -- 选择器问题(PBOR/GTYP)
   do !SPCO values $!VNAM
     var !ITEM coll all SPCO with (REFE of CATR eq $!SPCO ) for $!NSELE
     if(arraysize(!ITEM) eq 0) then
       var !NNAM (NAME of $!SPEC + NAME of $!SPCO)
       var !EXIST exists $!NNAM         -- 重名检查
       if($!FLAG) then
         error |$!NNAM is already in Spec.|
         skip
       else
         NEW SPCO $!NNAM                -- 创建规格元件
       endif
     endif
     CATR $!SPCO                        -- 设目录引用
     $!SCAN1                            -- answ (PPBORE 1 of CATR)
     $!SCAN2                            -- maxa (PPBORE 1 of CATR)
   enddo
 enddo
 var !DLST coll all SPCO with (lock) for $!SPEC    -- 收集残留锁定的SPCO
 UNLOCK ALL
 do !DSPCO values !DLST
   $!DSPCO
   DELETE SPCO                          -- 清理
 enddo
 var !SLST coll all SELE with (mcount eq 0) for $!SPEC  -- 空SELE清理
 do !DSELE values !SLST
   $!DSELE
   DELETE SELE
 enddo
```
PML2 等价：`!specComps[!ind].prtref = !this.gparts[!ind]`（catupgradespec.pmlobj:134）。

### 3.4 SCOM / PPOINT / PCON / PSKEY / PARAM

对象 `SPCSCOM`（spcscom.pmlobj）方法：`anyPSKeySet()`、`getPSKey(point)`、`getPSKeys()`、`getPConn(point)`、`getPConns()`、`anyCKeyForPConn(...)`、`getReport()`、`check()`、`pConnsEqualTo()`（通配 `matchWild`）、`setPconns()`（:365-456）。

PPOINT 遍历与 PCONN 写入（:369-452）：
```pml
do !point values !this.scomRef.ptref.members        -- PTSET 下的 PPOINT
  !pPointNum = !point.number
  !pconstr = !point.pConn
  if (match(!pconstr, 'PARAM') gt 0) then           -- PCONN=PARAM n 时改 SCOMPONENT 参数
    !paraNum = REAL(after(!pconstr,'PARAM'))
    !!ce = !this.scomRef
    var !oldVal PARAM $!paraNum                     -- 读旧值（须 TRACE OFF）
    PARAM NUM $!paraNum $!newConnType               -- 写参数
  else
    !!ce = !point
    PCON $!newConnType                              -- 直接写连接类型
  endif
enddo
```

SKEY 规则对象 `SPCSKEYRULE`：`includePPRule(REAL,STRING)`、`replacePPRule`、`removePPRule`、`getRule(REAL)`、`print()`（输出可回放 `object SPCPOINTRULE()` 脚本）。`SPCSKEY` 包 SDTEXT 元素：`!this.skeyRef.skey`。

COCO 兼容表：`crecocoelements.pmlfrm:324-349` `NEW COCO` + `NAME /$!name`；属性 `!cocoElem.cType[1]/[2]`、`!cocoElem.cKey`；守卫 `!!ce.type neq 'CCTA' and neq 'COCO'`。
PCONN→公共 CKEY 统计（75% 多数判定）：`spcpconnlist.pmlobj:143-148` `if (!numCKey2Array... GEQ !sum * 0.75)`，否则 `'Ambiguous'`。
SKEY 后缀判定链（spcspeccomponent.pmlobj:74-141）：`FLBL/FLFL/FLLB/FLSC/FL/BW/SC/SW/PL/CP`。

### 3.5 公称通径 NOMINB / NBRWLD

`crenominboreelements.pmlfrm:325-371`：
```pml
NEW NOMINB
NAME /$!name
INCBORE 0          -- 或 INCBORE $!inchBore
MMBORE $!mmBore    -- 或 MMBORE 0
```
守卫：`!!ce.type neq 'NBRWLD' and !!ce.type neq 'NOMINB'`。
全量模板 `nominal_bore.mac:3-190`：`NEW NBRWLD /NOMINALBOREWORLD` + `PURP BORE` + 80 组 `NEW NOMINB /NOMINALBOREnMM / MMBORE n / INCBORE inch`（6–4000mm ↔ 0.25–160"）。

### 3.6 目录元件创建（PDMSUI CAT gen，CDATE 等价）

`gen\mcrcomp`（CTYP 由 GTYP 推导）：
```
 var !CTYP (substr(|H$!GTYP|,1,4))     $* 如 HINST/HTEE
 NEW $!CTYP
 var !PDAT |$!PDAT 0|
 PARAM $!PDAT                          -- 参数缺省行
 name $!NAME
 var !PMAX PARA $!PNUMB                -- 参数个数
 var !NPARA |$!NPARA 0|
 PARAM NUMB $!INDX $!PVAL mm           -- 带单位写参数
 PARAM NUMB $!INDX $!PVAL
```
`mcopy`：`NEW $!TYPE $!TNAME COPY PREV RENAME $!FNAME $!TNAME` / `NEW $!TYPE COPY $!ONAME` + `NAME $!NNAME`。
`mcompmod`：`DELETE $!TYPE` + `NEW $!NEWTYP`。
SKEY 管理：`iskeys/fskeys/rskeys/eskeys`（读 `%PDMSDFLTS%\UI-SKEY-$!GTYP`，端部类型 **/**-/+ 语法解析生成索引 `BEF$!ENDCON$AFT`）。
参数表单：`fparam/iparam`（`_CDTPARAM<n>` 动态窗体，参数上限 30）。
GPART/族创建（catupgradespec.pmlobj:319-367）：
```pml
NEW PRTELE
!!ce.name = !fsName        -- ≤50字符保护
!!ce.purpose = !gtype
NEW GPART
COPY LIKE $!spcoVal        -- 整体拷贝引用(handle 41,52)
!!ce.pritype = !gtype
!!ce.attribute('description') = !gpartDesc
```
PARTSFROMSPEC（partsfromspec.pmlobj）：`new prtele $!endOfCommand`（行119/168，`after last member` 追加技巧）、`new gpart`（行194）、拷贝 `!!ce.catref/.detref/.matxt/.cmpref/.bltref/.tmpref = ...`（行201-217）、SELE 递归 `!me.ques/!me.tans/!me.answ`。

---

## 4. 选择表操作（TABGRO/CTABLE/TABHEA/TABHQU/TABITE/TABQUE）

### 4.1 SELECTIONTABLE 对象方法总索引（selectiontable.pmlobj，3129 行，57 个方法）

- 组级：`selectionTable(DBREF)`(126)、`createTable()/.createTable(STRING)`(210/234)、`setTableAtts(ARRAY)`(288)、`getTableAtts()`(348)
- 类型(CTABLE)：`newType()/.newType(STRING,STRING,STRING)`(380/427)、`deleteType()`(476)、`setType(REAL|STRING)`(521/569)、`getType()`、`getTypes()`、`getTypeCount()`、`setTypeAtts()`、`getTypeAtts()`
- 表头问题：`newQuestion(STRING)`(764)、`setQuestion(REAL,ARRAY)`(828)、`reorderQuestion(REAL,REAL)`(960)、`getQuestion(...)×4`、`getQuestions()/getQuestions(STRING)`、`getDesAttributes()`、`getQuestionIndex()`、`getQuestionCount()`、`deleteQuestion(DBREF|REAL|STRING)`(1421/1465/1493)、`getDefaultRaw()`(1543)、`checkNewQuesPurp()`(2636)
- 表项：`newItems(ARRAY)/(ARRAY,REAL)`(1650/1674)、`copyItems(ARRAY)`(1605)、`deleteItems(ARRAY)`(1771)、`getItemCount()`、`getItem(DBREF|REAL)`、`convertItemToString()`、`getItems()`、`getItemName(DBREF|REAL)`、`getAnswerRaw(DBREF,REAL)`、`getAnswer(DBREF,REAL|STRING)`、`getAnswers(DBREF)`、`setAnswer(DBREF,REAL,ARRAY)`(2457)、`setItemAtts(DBREF,ARRAY)`(2583)、`setActive(REAL,BOOLEAN)`(2672)
- 选型：`choose×5`(2927/2953/2982/3034)、`chooseItems(DBREF,ARRAY,ARRAY,BOOLEAN)`(2706)、`chooseSpecificItem(DBREF,STRING)`(3065)、`select(DBREF,DBREF)`(3112)

### 4.2 关键创建命令

createTable（:234-263）：
```pml
if (!!ce.type ne 'SPWL' and !!ce.type ne 'TABGRO') then
   SPWL                                   -- 导航兜底
endif
NEW TABGRO
if (!name.set() and !name.empty().not()) then
  if (!name.substring(1,1) ne '/') then
    !tableName = '/' & !name
  endif
  NAME $!<tableName>
  handle any
  endhandle
endif
```
newType（:386-459）：
```pml
!!ce = !this.selTable
if (!!ce.mcount ne 0) then
  LAST MEMBER
endif
NEW CTABLE
!!ce.descr = !heading
!heading = !heading.trim().replace(' ','_')
!!ce.name = !prefix & '/' & !specName & '/' & !heading   -- 命名 /CT/规格/标题
NEW TABHEA
END
!typeSequence = !!ce.tysequence
!this.cTables = !this.selTable.evaluate(object BLOCK('MEM CTABLE'))
```
deleteType：`!!ce = !this.typeTable; DELETE CTABLE`。
newQuestion（:770-794）：
```pml
!!ce = !this.heading
if (!!ce.members.size() ne 0) then
  LAST MEMBER
endif
NEW TABHQU
QTYPE TEXT
ANSTYPE TEXT
!!ce.purpose = !purpose
do !val values !this.items          -- 同步给每个表项建答案
  !!ce = !val
  if (!!ce.members.size() ne 0) then
    LAST MEMBER
  endif
  NEW TABQUE
  RFLAG SING
  WANSWERS UNSET
  !!ce.purpose = !purpose
enddo
```
setQuestion（:842-934，全属性复位+重设）：
```pml
PURPOSE UNSET
DESCRIPTION UNSET
QUESTION UNSET
QUSEXPRESSION UNSET
TQUESTION UNSET
QTYPE UNSET
DEFAULT 0
TDEFAULT UNSET
ATTSET NONE          -- handle (47,15)
ANSTYPE TEXT
!!ce.tQuestion / !!ce.question / !!ce.attset / QUSEXPRESSION
!!ce.tdefault (handle 2,441) / !!ce.anstype
TABANSWERS UNSET
TANSWER UNSET
WANSWERS UNSET
COPY LIKE $!question            -- 表头→答案属性同步
!!ce.rFlag = 'SING'             -- NONE/SING/RANG/MULT
```
newItems（:1690-1712）：
```pml
!!ce = !this.typeTable
NEW TABITE
!!ce.prtref = !gParts[!ind]             -- 表项挂 GPART
!newIndices.append(!!ce.tysequence)
do !val values !this.heading.members
  NEW TABQUE
  WANSWERS UNSET
  COPY LIKE $!val
  RFLAG SING
enddo
```
答案形态（setAnswer :2489-2553）：文本 `WANSWERS UNSET`+`rFlag=|SING|`+`tanswer=...`；多选 `rFlag=|MULT|`；区间 `rFlag=|RANG|`；属性族 `tabanswer/tabanswers`。
setItemAtts（:2599-2610）：`!!ce.name=`、`!!ce.prtref=`、`!!ce.lactive=`。

### 4.3 旧规格→选择表迁移（convertspec.pmlfrm:864-1041）

```pml
!pbore[1] = 'PBOA,PBOR 1'  ... !pbore[4] = 'PBOD,PBOR 4'   -- PBOR 端部代码表
!!ce = !tabite.dbref().prtref.catref      -- 失败回退 tmpref/spco 映射 (handle 2,822)
-- 上溯 SELE 收集 !question/!answer/!qualifier (!!.question/!!ce.qualifier/!!ce.tanswer/!!ce.answer)
do !q index !question          -- 给 TABITE 建答案
  NEW TABQUE
  QUALIFIER $!qualifier[$!q]
  PURP  $!question[$!q]         handle (47,62)
  if (!qualifier[!q] ne 0) then
    !pbors = !pbore[!qualifier[!q]].split(',')
    !!ce.purp = !pbors[1]                      -- PBOA..
  endif
  if (!question[!q] eq 'PBOR') then
    !!ce.desc = |PBOR $!qualifier[$!q]|
  endif
  RFLAG SING
  QTYPE WORD
  WANSWERS $!answer[$!q]      handle (47,15)
    tabanswer $!answer[$!q]   handle (47,15)
      TANSWER |$!answer[$!q]|
      qtype TEXT
    elsehandle none
      qtype REAL
    endhandle
  elsehandle (2,113)
    TANSWER |$!answer[$!q]|
    qtype TEXT
  endhandle
enddo
!!ce = !ctable.dbref()
TABHEA 1                       -- 进入/复用表头
handle (2,113)
  NEW TABHEA
endhandle
do !q index !question          -- 表头问题
  NEW TABHQU
  QUALIFIER $!qualifier[$!q]
  RFLAG NONE
  PURP $!question[$!q]
  ANSTYPE REAL
  QTYPE EXPR                   -- 数值问题用表达式型
  (否则 ANSTYPE WORD / QTYPE WORD)
enddo
```
改名重名处理：`name $!newname`（`/ST`→`/CT`、`/P`→`/T` 前缀替换，`handle (41,12)` 重名时 `/T($n)` 递增重试）。

### 4.4 保温/涂层选择表自动建库

`insudefinemain.pmlfrm`：`NEW TABGRO PURP INSU`（:2243/2257）+ `NEW TABITEM`（:2767-2769）；涂层版在 `sftdefinecoatings.pmlfrm`。

### 4.5 选择表 UI（catseltabviews.pmlobj，2511 行）

方法链：`globalInstance/add(×3)/editSelTab/defineForm/init/initOpTableTypes/initType/actionMain/initTasks/actionTasks/managePanels/initTableAtts/actionTableAtts/initAddType/actionAddType/initTypeAtts/actionTypeAtts/initCriteria/actionCriteria/initItems/actionItems/initSearch/actionSearch/netResultsSelected/populateTable/addToTable(form,gparts)/netPopupCallback/tablePopup/linkLabelCall/netAfterSelect/netSelectRows/buttonPick/remove/viewIndex/close×2/nextAvailable/setFormName/updateRecentSelTables/txEmptyToUnset/txUnsetToEmpty/checkVaries/checkNameField`。

---

## 5. 规格引用操作（SPREF/PSPEC/搜索/匹配）

### 5.1 SPREF 全部写法变体（design 侧实测）

| 写法 | 示例出处 |
|---|---|
| `!x.spref = !y` 属性赋值（最常用） | componentcreation.pmlfrm:5392/5911/6129/7171/7404/7451、cblmtrl.pmlfrm:5044+、specborechange.pmlfrm:850+ |
| `SPREF $!变量` 命令式 | cvchangewallspec.pmlfnc:114、sctlcrelem.pmlfnc:232/272、strsctntogensec.pmlfnc:117-244、pltcreate.pmlfrm:661/1366/1369 |
| `SPREF /路径` 字面量 | strsectionedit.pmlfrm:535、pipe1to1pene.pmlfnc:244-475、hvacsplitatta.pmlfnc:67/96/117 |
| 清空 `SPREF NULREF` | cblCableCopy.pmlfrm:414、spcffitspecsel.pmlfrm:1020、strspecref.pmlfnc:114 |
| 清空 `SPREF =0/0`、`SPREF =0` | spchvacspecsel.pmlfrm:581、hvacsplitatta.pmlfnc:41 |
| 清空 `SPREF UNSET` | stchoose.pmlfrm:561 |
| 选型写入 | stchoose.pmlfrm:570 `!!ce.spref = !this.selectedItem`；selectiontable.pmlobj:3116 `!designItem.spref = !tableItem.prtref`（新表项写 GPART） |
| 读取/守卫 | `!element.spref.unset() or badref(!element.spref)`（spcspecification.pmlobj:128）、`!!ce.spref.catref`（catmodelviews.pmlobj:3260） |

### 5.2 PSPE（管路规格命令）

`design\forms\createsyscda.pmlfrm:190-191`：
```pml
if (!this.pspe.val.set()) then
  PSPE $!this.pspe.val
```
默认规格联动：`appcntrl.pmlobj:746-758` `!!cdpipe.pspe.val = !this.currentSpec`。
PSPEC 属性族：`!current.owner.pspec`、收集 `var !bran collect all BRAN with stext of text1 of pspec EQ 'TRAY'`（cblCableTrayVolumes.pmlfrm:403-405）。

### 5.3 规格搜索/过滤（SPCSEARCH，spcsearch.pmlobj:86-160）

```pml
!searchRules.append('PURPOSE of SPWL eq ''' & !this.spwlType & '''')   -- 规格世界目的
!searchRules.append('PURPOSE eq ''' & !this.type & '''')               -- 规格目的
!searchRules.append('MATREF eq ' & !this.material)
!searchRules.append('FLUREF eq ' & !this.fluid)
!searchRules.append('RATING eq ' & !this.rating)
!searchRules.append('CSTANDARD eq ''' & !this.standard & '''')
!rule = ... ' AND ' 连接
goto frstw CATA / var !spwlds SPLIT MEMB SPWL / COLLECT ALL SPEC WITH (...)
```
`like(DBREF)`（:201-218）：从现有 SPEC 反推 6 项准则再 search。

### 5.4 SELE/SPCO 匹配算法（spcspecification.pmlobj:301-484）

```pml
break if(!this.selector.type eq 'SPCO')          -- 终点
!question = !this.selector.question              -- 当前问题
!qualifier = !this.selector.tQualifier           -- 文本限定符
if(!qualifier.subString(1,2) eq '!!') then
  !result[1] = $!<qualifier>                     -- PML 函数型限定符（直接执行）
else
  !result[1] = !reference.attribute(!qualifier)  -- 属性型限定符
endif
if(!this.selector.qualifier ne 0) then
  !result[1] = !this.selector.qualifier          -- 数值限定符
endif
-- 默认答案：!this.selector.tDefault / !this.selector.default
-- 三种答案形态匹配：
!result.findFirst(!specItem.tAnswer)                          -- TEXT
!result[!j] eq !specItem.tAnswer.boolean()                    -- BOOLEAN
!result[!j].between(!specItem.answer, !specItem.maxAnswer)    -- RANGE/数值区间 ← bore matching 核心
```
其它：`defineWith(DBREF)`（:119-148，`!this.specification = SPEC of $!<this.selector>`）、`answerType()`（:194-209，tAnswer→TEXT / answer ne maxAnswer→RANGE / VALUE）、`valid()`（:544-630）、`question()`（:1018-1042，tQuestion→question→'Selection' 回退）。

### 5.5 设计侧 SPECIFICATION 对象（design\objects\specification.pmlobj:101-766）

方法索引：`specification/setSpecification/bores/loadBores/loadComponents/typeIndex/subTypes(type,arrive,nominalBore)/lastStype×2/componentData/components(type,questions,answers)/questions(type)/answers(type,component)/maxAnswers(type,component)/loadTable(type)/changeTypes/deriveChangeTypes/availableBores`。

批量取元件标准流程（design\functions\getSpecComponents.pmlfnc:26-36）：
```pml
!specifications = object SPECIFICATION(!spec.dbref())
!specifications.allowTubes = TRUE
!specifications.loadComponents()
!specifications.loadBores()
!specifications.loadTable(!type)
!specifications.subTypes(!type, 1, !boreObject)
!questions.append('PBOR1');  !answers.append(!boreObject)
!components = !specifications.components(!type, !questions, !answers)
```

按用途装载规格清单（specifications.pmlobj:193）：
```pml
var !specList collect all SPEC with ((NOT(PURP eq 'HVAC' or PURP OF OWNER eq 'HVAC')) and (match(upcase(PURPOSE), !testString) gt 0 or match(upcase(STEXT of TEXT 1), !testString) gt 0))
```
入口方法：`piping()/tracing()/insulation()/cwpa()/cwma()/cabl()/elco()/epen()`（:118-402）；isItAPipe 判定用 `!comp.lstu.spown / !comp.spown / !comp.pspec`（:271-291）。

选型表匹配（selectiontable.pmlobj:2844-2892）：TEXT 等值；WORD+SING 等值 / +MULT findFirst；REAL+SING 等值 / +RANG 区间（`lt answer[1] or gt [2]`）；BOOL 等值；跳过 `lactive.not()` 项（:2821）；表达式问题 `!designItem.evaluate(object BLOCK(!expression[!index]))`（:2804）。

### 5.6 规格选择窗体骨架（21 个窗体共用）

`spcspecselect.pmlfrm:54-136` 为原型：
```pml
member .specLink is SPCLINK / .specSearch is SPCSEARCH / .specData is SPECDATA / .dflts is SPECDFLTS
!this.specSearch.spwlType = '' / .type = '' / .search()
!this.specLink.specification(!this.specifications, !this.specSearch)
!this.specLink.selection(!this.selected) / .permissible(!this.perms) / .question(...) / .default(...)
!this.specLink.autoSelect(!this.autoSelect) / .setAction('!!spcSpecSelect.specCallback()')
```
`init(DBREF)`（:192-213）：`!specEl = SPEC OF $!spec; !spwlEl = SPWL OF $!spec; !spwlType = !spwlEl.purp`。
`edit(!objectWithSpref)`（:238-251）：读 `!objectWithSpref.spref` 回填。
应用（:276-294）：`!selectedSpre = !this.specLink.selection(); call !!civTransferSpec()`。
同构体：spcffitspecsel、spcwfitspecsel、spchvacspecsel、spchvacpenspecsel、spcsbfispecsel、pltspecification、equmodspref、branpenadd/branpencreate、hmautopipepenetration 等。

---

## 6. PML1 Paragon 宏族（PDMSUI\CAT）

- **specs\**：`fcrtspwl/icrtspwl/mcrtspwl`（建 SPWLD）、`fcrtspec/icrtspec/mcrtspec`（建 SPEC）、`fbldspec/ibldspec/mbldspec/xbldspec`（规格构建器：ADD/REM/CATE/GTYP/DESC/NGTYP/DELETE 分发）、`fnozzspec` 系（喷嘴）、`fprflspec` 系（Profile）、`fgtypspec` 系（GTYP 管理）、`ffmtspec/ifmtspec`（显示格式）、`fspecmap/ispecmap`（映射）、`rcatalst`（CATA 报表）、`init/isystem`（SPECKEY 系统表 `_CDCSPECKEY_*`）。
- **gen\**：`fcrcomp/icrcomp/mcrcomp/xcrcomp`（创建 JOIN/PRFL/FITT 元件）、`fcompmod` 系（改型）、`fcopy/icopy/mcopy`（复制）、`fskeys/iskeys/rskeys/eskeys`（SKEY 表读写）、`fparam/iparam`（参数表单）、`fname/iname`（命名）、`ftabload` 系（表装载）。
- **clib\**：`rcatedat/rcatetyp/rcomptyp/rpafmt/rparmax/rptrfmt/ffnam/ufnam`（类别/元件/参数格式报表）。
- **dflts\**：`purpose`（目的枚举）、`standard-headings`（标准标题问题集，供 `!!catSpecViews.bnHeadingStd` 加载，catspecviews.pmlobj:3261-3262）。

---

## 7. 相关对象速查

- `SPCSPEC.check(ARRAY,STRING)`：输出 `',,PPoint 1, PPoint 2...'` 兼容性报表。
- `CATUPGRADESPEC`：`upgrade(!destPartWorld,!destSpecWorld)`、`copySpec`、`createGparts`（`object COLLECTION(); !colSpco.scope(!specification); !colSpco.type('SPCO'); !spcoRefs = !colSpco.results()`）、`createSelTab`（`object SELECTIONTABLE(); createTable/newType/newItems`）。
- `STCHOOSEDATA`：`setData` 12 个重载（:150-786）、`getSelTabs/getDesignItem/getItemSelectionTable`（`!!dtbOwnerOfTypes(!this.desItem.spref, !tableType)`）。
- 命名校验：`!!catValidateNameField`（`!!checkName(!enteredName, |NEW|)`、`=` 首字符拒绝）、`!!catValidateRefField`（`!name.dbref()` + 类型校验、`=0`=NULREF 放行）。
- 规格报表：`spcspecreport.pmlfrm:89/145-147` `var !specElems COLLECT ALL SPEC [FOR $!owner]`（PCON/SKEY 兼容性报表）。
