# Marine Spooler 管件车间命令大全（穷举级·源码实证）

> 来源：`PMLLIB\spooler\` 全部 81 文件（34 forms + 28 functions + 19 objects）+ `PMLLIB\pipefabricationmanager\` 全目录约 115 文件（common/design/draft/spooler），全部读取或方法级穷举扫描。
> 适用：AVEVA Marine (PDMS 系) 12.1 SP4。管段划分、编号、焊接管理、MTO、iso 出图、批处理全收录。

## 1. 元素类型清单

| 类型 | 层级 | 出处 |
|---|---|---|
| ISODEP(Department)/ISOREG(Registry)/SPLDRG(Spool Drawing) | ISOD 库容器 | splcreate.pmlfnc:38-42 |
| SPOOL、FIELD | SPLDRG 成员 | spldelete.pmlfnc:83 |
| SPLTMP(临时)/WLDGRP(焊缝组)/JNTGRP(接头组) | SPLDRG 成员 | splmainbartrack:46、splwelds:38、spljoints:38 |
| WELD(IWELD/RWELD/AWELD)、IJOINT、AITEMS、ATTA、BEND、TUBI、FTUB、OLET、TEE | 管网元素 | splmainbartrack:46、splwelddata:50-105 |
| PSPOOL、PPIECE、PSDB | PFM Design 库（制造 Spool/管件/活动表） | pfIsoDrawingManager.pmlobj:102-105、pfPartNo.pmlobj:144 |

## 2. Spooler Ace 命令全集

**创建/命名**（splcreate.pmlfnc:30-64）：
```pml
NEW $!type                          $* ISODEP/ISOREG/SPLDRG
handle any
  !!alert.error(!!error.text)
  return error 1 noalert
elsehandle none
  if (!type.eq('SPLDRG')) then
    SFLimit $!!<splGenOpt.constraint>       $* Search Within 约束
  endif
  NAME $!<name>
```
表单版（splcreate.pmlfrm:153-203）：`NAME $!<this.name.val>`、`SPLPREFIX '$!!<splNumOpt.splPrefix>'`（Spool 编号前缀）、取消时 `DELETE $!!<ce.type>`。

**删除/划分**（spldelete.pmlfnc:83-103）：
```pml
SPOOLING REMOVE $!element                   $* SPOOL/FIELD 专用删除
SPOOLING REMOVESPLTMPS $!<element.owner>
SPOOLING REMOVE $!element MEMBERS
Smaximum 0 / Wmaximum 0 / Jmaximum 0 / Pmaximum 0 / Bmaximum 0   $* 重置编号计数器
DELETE $!<element.type> [MEMBERS]
```

**Spool Break（车间断点）命令族**（splsfbreak.pmlobj）：
```pml
asfbreak true|false                 $* Arrive 端断点（:470/572）
lsfbreak true|false                 $* Leave 端断点（:508/610）
TSFBREAK $!setting                  $* 管件(Ileave tube)断点（:288-357）
CSFBREAK $!setting                  $* 组件断点
goto cref / tsfbreak true / csfbreak true   $* Offleg 断点（:539-546）
```
!!splSfBreak 8 模式：`ADD/ADDPA/ADDPL/ADDPO/REMOVE/REMOVEPA/REMOVEPL/REMOVEPO`（splsfbreak.pmlfnc:28）。

**Drawlist**（spldrawlistadd.pmlfnc:51-62）：
```pml
REM $!<element>
ADD $!<element> COLOUR GREY
ADD $!<element> COLOUR $!<colourNum>
```

**导航/查询**：`ILEAVE TUBE OF $!element`（splnavigate:32、splpcref:47）；SPLDRG 爬升（spldrg:39，handle (2,111) 时 sfref 回退）。

## 3. 成员收集函数族

| 函数 | 逻辑 |
|---|---|
| `!!splMem(!splDrg)` | 经 `!member.splMem` 收集 SPOOL/FIELD 成员并剔除 WELD |
| `!!splWelds(!splDrg)` | WLDGRP 组员 = WELD 列表 |
| `!!splJointS(!splDrg)` | JNTGRP 组员 = IJOINT 列表 |
| `!!splBends(!splDrg)` | skey 匹配 `PB?D` 的拉制弯头 |
| `!!splJntOwners(!ijoint)` | `!ijoint.jntOwners` 2×4 实数解码；`ILEAVE TUBE OF $!ref`（710633=TUBI 标志） |
| `!!splIwdOwners(!iweld)` | `!iweld.iwdOwners` 解码 |
| `!!splAwdOwner(!aweld)` | `!aweld.awdOwner` 3 实数解码 |
| `!!splPcref(!component,!pPoint)` | `!component.pcref[!pPoint]` 连接件数据 |
| `!!splWeldData(!weld,!options)` | BORE/ckey(BW\|SW)/oletHdrWeld/shop/spoolNumber；内含 `var !skeyData COMPSKEYS $!connData[3]`（:128） |

## 4. 编号系统（六套编号对象）

对象族：`SPLSPOOLN/SPLFIELDN/SPLWELDN/SPLJOINTN/SPLBENDN/SPLPARTN`（各有 align/update/check/renumber/highlight/trackSelect/validate/setAttribute；基类 SPLCOMMONN :60 提供 .start/.autoAssign/.renumber/.nextNumber/.chooseData/.checkData/.merge/.undo 等）。关键命令：
```pml
SPOOLING REMOVESPLTMPS $!<this.ce>          -- splcommonn.pmlobj:158
```
handle 码：`(83,14)(83,6)` SPOOL/FIELD、`(83,15)` WELD/JOINT、`(61,299)` PARTN。

**编号更新链**（splupdate.pmlfrm .apply :440-651）：align SPLDRG → update SPOOL → FIELD → alignBoth WELD+JOINT → update weld → joint → bend → partn；交互模式 'ASK' 转交 `!!splInteractive`。检查结果经 `!!messageFile.messageString(154, 27|30|60|61|68|78, ...)`。

## 5. MTO（材料表）命令

**MTO 状态**（splmtostatus.pmlfrm .setCompMto :453-476）：
```pml
!!ce = !element
if (!element.type eq 'TUBI') then
  PREVIOUS
  handle (2,113)
    END
  endhandle
  if (!!ce.type eq 'BRAN') then
    MTOH $!status          $* 头管 MTO 状态
  else
    MTOT $!status          $* 离开管 MTO 状态
  endif
else
  MTOC $!status            $* 组件 MTO 状态
endif
```
读取属性 `!!ce.mtoh/mtot/mtoc`（空值等价 'ON'）。级联：setBranchMto → `var !members COLLECT ALL BRANCH MEMBERS FOR $!branch`（:543）→ setPipeMto → setSpoolMto → setSpldrgMto。状态值 ON/OFF/mixed。

**MTO 构建引擎**（splmto.pmlobj，SPLMTO 类）：
```pml
var !pipeMembers COLLECT ALL BRAN MEMBERS FOR $!<this.ce>      -- :472
var !boltTotal PA BOLT TOTAL OF $!<member.ce>  / PL BOLT TOTAL OF  -- :629/643
var !joint PA|PL BOLT JOINT OF ...                              -- :823-878
var !composed COMPOSE |PT| WIDTH $!ptnoWidth SPACE 2            -- :1511
```
方法：.buildMto/.setGlobalFormats/.buildSingleMto/.collectGroups/.collectComps/.resolveTubes/.getBolts(!matcFile)/.boltedHead/.boltedNotTail/.getMtorefs/.addAllow/.orderForBom/.listBom×2/.totalWeights(!specGravity)/.print(!filename)。数据类：SPLMTOCOMP/SPLMTOTUBE/SPLMTOBOLT/SPLMTOMTOR/SPLMTOOPTIONS。

## 6. 焊接管理

**Spooler 焊接创建**（splcreatweld.pmlfrm .atPpoint :240-369，完整命令序列）：
```pml
!!ce = !element
if (!pPoint eq !!ce.leave) then
  !where = 'AFTER';  !connect = 'CONNECT TO PREVIOUS'
elseif (!pPoint eq !!ce.arrive) then
  !where = 'BEFORE'; !connect = 'CONNECT TO NEXT'
else
  !!ce = !element.cref            $* handle any 回退 crfa[!pPoint]
endif
!oldTubeRef = ILEAVE TUBE OF $!refElement
NEW WELD $!where
handle (2,605)                    $* 主元素未 CLAIM
  !!alert.error('Cannot create welds if owning branch has not been CLAIMed.')
elsehandle any
endhandle
CHOOSE WITH SHOP $!shop
handle (61,162) (61,164)          $* 规格无匹配元素
  DELETE WELD
endhandle
$!connect
handle (7,41)                     $* 找不到 ppoint
  DELETE WELD
elsehandle none
  SHOP $!shop
  LSTU $!<refElement.lstu>
  ISPEC $!<refElement.iSpec>
  TSPEC $!<refElement.tSpec>
  ALLOW $!allowance
  SPOOLING ADD $!<refElement.sfref.owner> $!weld
  !weldTube = ILEAVE TUBE OF $!weld
  SPOOLING ADD $!<oldTubeSfref.owner> $!weldTube
endhandle
```

**PFM 焊接引擎**（design\objects\pfWeldControl.pmlobj，33 方法）：
```pml
-- .createWeldOnBranch(:1112) 核心命令：
NEW WELD $!posKey CHOOSE SPEC /$!specVal WITH $!this.shopConditions STYP $!this.sType   -- :1222
NEW WELD $!posKey CHOOSE SPEC /$!specVal WITH STYP $!this.sType                          -- :1231
NEW WELD $!posKey CHOOSE SPEC /$!specVal WITH $!this.chooseConditions $!this.shopConditions STYP $!this.sType  -- :1246
DESP NUM 1 $!weldGap                                                                     -- :1263
NEW WELD $!posKey                                                                        -- :1271
SELECT SPEC /WELDGAP WITH STYP $!this.sType                                              -- :1279
spref $!weldgapSpec[1]                                                                   -- :1289
```
其他：.removeAllWelds/.renumberAllWelds/.setStartWeldNumber/.setWeldAttributes×2/.moveWeldForSlipOnFlangeInnerPart/.evaluateCkey/.getWeldGapFromConfigTable/.evaluateWallThickness/.evaluateMaterial/.checkDBWritable；`FORWARD`/`$!mode` 模式保存恢复(:373/467)、`UNDODB`(:449 附近)、`var !createdWelds coll all welds for $!element.ref`(:449)。
表单 pfWeldHandling.pmlfrm（57 方法）：createWeld/createWeldWithPickedElements/removeWelds/deleteWelds/changeAttributes/exportWeldList/saveToExcel/highlightWelds。
位置变体（pfModifySpool.pmlfrm:3257-3267）：`NEW WELD FORWARD` / `NEW WELD BACKWARD` / `NEW WELD $!creationPosition`。

## 7. 零件号/切割（PFM）

- `PARTNO CREATE $!pipeRef`（pfPartNo.pmlobj:97）+ 属性回填 `!comp.ptno/.ptnt/.ptnh`、`!spool.melrfa/.belrfa/.pprfa`（:134-192）；斜管/螺纹管修正 `!!collectAllFor('FTUB',|compType inset ('SEND','THRD')|,!pipeRef)`(:112)。
- `partno create ce`（pfspooler.pmlobj:692）、`PARTNU $!count`(:720/725，FTUB 及其 il tube)。
- 弯头切割长度：`!!pfCalculateElbowCuttingLength(!elementName is STRING) is REAL`。
- 零件号一致性检查：`!!splPBendCheck()`（`PARTNO CREATE <gid> PBEND` 后；`ILeave tube of $!tubeOwne` handle (2,121) 跳过 <1mm 管 :130-143）。

## 8. 主菜单 callback 全集（splmainbarconstr.pmlfnc:44-84）

```pml
!!spooler.deleteMenu.add('callback','CE','!!splDelete(!!ce, false, true)')
!!spooler.deleteMenu.add('callback','Spool Break','!!splSfBreak(|remove|)')   $* PA/PL/OFF 同理
!!spooler.modifyMenu.add('callback','SPLDRG Order','!!splReorder()')
!!spooler.modifyMenu.add('callback','MTO Status...','show !!splMtoStatus')
!!spooler.modifyMenu.add('callback','Shop/Field...','show !!splShopFlag')
!!spooler.modifyMenu.add('callback','Detail Plotfile...','show !!splDetailPlt')
!!spooler.modifyMenu.add('callback','Attached Welds...','show !!splNWelds')
!!spooler.modHierarchy.add('callback','Include...','show !!splMemInclu')
!!spooler.modHierarchy.add('callback','Reverse Order','!!membersReverse()')
!!spooler.modHierarchy.add('callback','Reorder...','show !!splMemReord')
!!spooler.numberMenu.add('callback','Update...','!!splUpdate()')
!!spooler.numberMenu.add('callback','Renumber...','!!splRenumber()')
!!spooler.numberMenu.add('callback','Check...','!!splCheck()')
!!spooler.createMenu.add('callback','Department...',|!!splCreate('ISODEP')|)
!!spooler.createMenu.add('callback','Registry...',|!!splCreate('ISOREG')|)
!!spooler.createMenu.add('callback','Spool Drawing...',|!!splCreate('SPLDRG')|)
!!spooler.createMenu.add('callback','Weld...','show !!splCreatWeld')
!!spooler.createMenu.add('callback','Spool Break','!!splSfBreak(|add|)')
-- iso 出图入口（spooler.pmlfrm 构造器 :292-293）：
!!isdRunIso('STA', true) / !!isdRunIso('SYS', true)
```

## 9. Design → Spool 转换与批处理

**交互式**：`!!splFunctions.pick('ADD'|'REMOVE')` → `SPOOLING ADD/REMOVE`（splfunctions.pmlobj:795/831）；`SPOOLING OPTIONS INCLUDEFIELDS $!<this.mainForm.includeFields.val>`(:380)。

**EDG 批量合并**：pfspooler.pmlobj EDGPACKET 挑选过滤 `(type of owner) eq |BRAN| AND (unset(sfref))`(:183-187) → .mergeSpools(:520) 执行 `savework`/`uncl ALL` → `!!pfmergespools` 后台批处理。

**批处理宏生成**（pfmergespools.pmlfnc:29-123）：
```pml
-- 宏内容：登录文件 $m → <mdb> → spooler（模块登录）→
SPOOLING OPTIONS INCLUDEFIELDS <flag>
!!pfspoolingmege('...','...')
QUIT / FINISH
-- 执行："%pdms_installed_dir%\MON" tty -noconsole -macro="$!pdmsuser/pfmergespools.mac"
-- .NET 导入：import 'PipeFabricationAddin' + object RUNBATCHPROCESS()，失败回退 SYSCOM 'START /MIN cmd.exe /C ...'
```
`!!pfspoolingmege`(:27-144)：逐行读 pfspoolmerge.dat，`SPOOLING ADD CE $!element` / `SPOOLING REMOVE $!spoolRef`，再 `FILE /$!macFilePath OVER` + `OUTPUT CE CHANGE SINCE LATEST` + `TERM` 生成回放宏，主会话 `pause 0.1` 后 `$M /$!this.tempMacroPath`（pfspooler.pmlobj:589-590）。

## 10. Spool → Iso 出图链（两条路径）

**A. Isodraft 直连**（pfIsoDrawingManager.pmlobj .createIsometrics :49-232）：
```pml
ISODRAFTMODE
handle (47,15)
  exit
endhandle
$M /$!isoOptionFilePath              $* 装载 ISO 选项文件
MessageFile "$!messageOutputPath" OVERWRITE
if (!isFabrication and !sourceEntryType eq 'PSPOOL') then
  !!pfmarkbendtableonisoview('XYZ'|'FRB')
endif
if (!sourceEntryType inset ('PIPE','BRAN')) then
  MaterialList PartNumbers GENERATED
endif
syscom |del $!outputName*|
!export = !exportOption + |"| + !exportFileName + |"| + !single
$!export                             $* OUTPUT FILE|DXF|PDF|IMAGE|EMF ["name"] [SINGLE]
MatlistFile "$!materialName" PERPLOTFILE OVERWRITE with 55 lines
detail $!entry                       $* 出图主命令
handle (33,157)                      $* Isodraw 出错
var !status isodraw status
var !isoCountTemp isodraw number
do !plot to !isoCount
  var !plotFile isodraw plotfile $!plot filename
enddo
```

**B. Marine Drafting 底层图纸**（pfPipeMakeSpoolDrwg.pmlfnc → makeisoview/makespooldrwg 批处理）：宏登录 `marinedrafting`（Marine）或 `draft`，再 `ISODRAFT`（makeisoview 版）→ `PFPIPESPOOLDWG.makeUnderlyingDrwg`：
```pml
new DRWG $!dwgName / delete DRWG / include $!dwg
copy $!this.dwgTmplName rename ...
sheet 1
marPtype $!this.marPtype
!!ce.author / !!ce.date
NEW LAYE ...                         $* 标注层
NEW SLAB ON $!entry ATEX |$!mtoTag|
var !viewList coll all view for drwg
var !viewDirections eval dir for all view for $!sheetRef
```
完成后写 `spooldwgdone.log`（'DONE'）供轮询。

## 11. 表单编目（34 个，方法数）

主表单 `!!spooler`（MAIN 型，工具栏 GETWORK/MSAVEW/drawlist/REMOVE/MDELCE/splCreate/splUpdate/splModify + pick 三模式）；其余：splcreate、splcreatweld、spladdwithin（18 方法）、splasbuilt、splattatta、splattdisp、splattisodep/isoreg/weld（各 handle (2,111)）、splbooleanatt、splcheck、spldeletenam/sel、spldetailplt（handle (2,113)）、spldrawlist、splgenedit、splinteractive（交互式编号：start/processData/assign/generate/undo/softCancel/hardCancel）、splmembers、splmeminclu/reord/resize、splmodify（主属性修改）、splmtostatus、splnameatt、splnumedit、splnwelds、splrealatt、splrenumber、splshipvol、splshopflag、splstringatt、splupdate（705 行）。

## 12. pipefabricationmanager 编目

- **common**：!!comAutoName/comCallForm/comElementZoomOn3DView/comEvalElementWithType/comIsValidElement/comTranslateRsoPosition；COMMARDRAWINGTYPES、MARDRADRAFTINGAPI（.dwgSave/.dwgClose/.dwgOpen/.dwgRepaint；handle (1000,0)）。
- **design**（24 forms + 18 fnc + 33 obj）：表单 !!pfAssignBendingMachine、!!pfFabMachineMgr(5842 行)、!!pfFabricationCheck(68 方法)、!!pfModifySpool(66 方法)、!!pfWeldHandling 等；对象 PFASSEMBLYACTIVITY(MANAGER)（findSegments/getElbowActivity/getFlangeActivity/getTeeActivity 等 26 方法）、PFBENDING*、PFBRANCHECK(RESULT)/PFBRANTEECHECK/PFFLANGEROTATIONCHECK/PFSPECCHECK/PFVALVEDIRCHECK/PFWELDGAPCHECK(RESULT)/PFPIPECONSISTENCYCHECK、PFPIPESPOOLMANAGER（getBendingTables/getWeldingTables/getBendingVertices）、PFSPOOLVOLUME、PFWELDCONTROL/PFWELDDATA/PFWELDINGTABLE。
- **draft**（3 forms + 24 fnc + 6 obj）：!!pfIsoDrawings(36 方法)、!!pfPipeSpoolDwg(50 方法)；函数 !!pfCalculateAdeg(handle (2,891))、!!pfCreateIsoDrawing、!!pfMarkBendTableOnIsoView、!!pfPipeCreateBarcode、!!pfPipeMakeIsoView/OverlyingView/SpoolDrwg/UnderlyingDrwg(handle (2,779))；对象 PFISODRAWINGMANAGER、PFPARTNO、PFPIPESPOOLDIMENSION（handle (64,277)(2,201)(2,752)(2,870)(2,813)）、PFPIPESPOOLDWG(45 方法)。
- **spooler 子目录**：!!pfsplitmergespools 表单（Multiple Spool）、!!pfSpoolDrwgMemberCreate、!!pfmergespools/!!pfspoolingmege、PFSPOOLER/PFEVALUATESPOOLMEMBER。

## 13. handle 错误码速查

| 码 | 语义 | 出处 |
|---|---|---|
| (2,111) | 无法导航至元素 | spldrg:40、pfspooler:404-424 |
| (2,113) | 列表耗尽/无前一元素 | splcreatweld:644、splmtostatus:461、splnwelds:158 |
| (2,121) | 隐含管不存在 | splpbendcheck:131 |
| (2,201) | 元素未定位/无 sfref | splcreatweld:601、pfFlangeRotationCheck、pfspooler:218 |
| (2,605) | 主元素未 CLAIM | splcreatweld:297/576 |
| (7,41) | ppoint 未选中 | splcreatweld:321 |
| (47,15) | 语法错误 | splcommonn:720、pfIsoDrawingManager |
| (61,162)(61,164) | 规格无匹配元素 | splcreatweld:305/584 |
| (61,299) | PARTN 属性错误 | splpartn:166/308 |
| (61,528)(61,565) | — | spladdwithin:275 |
| (83,6)(83,14)(83,15) | SPOOL/FIELD/WELD/JOINT 网络错误 | splspooln:243/332 等 |
| (2,752)×14 | 表达式求值错误 | pfPipeSpoolDwg、pfPipeSpoolCalcExpr |
| (2,891)×4 | ADEG 计算 | pfcalculateadeg |
| (61,618)×6 | 一致性检查 | pfConsistencyCheck |
| (33,157) | Isodraw 出图失败 | pfIsoDrawingManager:171 |
| (2,822) | 致命 DB 错误 | pfWeldControl:401 |
| (99,532) | UDA 未定义/DESP 失败 | pfWeldControl、pfComEvaluateExpression |
| (64,277) | 尺寸错误 | pfPipeSpoolDimension |
| (1000,0) | marAPI 已导入 | MARDRADRAFTINGAPI、pfWeldHandling |
