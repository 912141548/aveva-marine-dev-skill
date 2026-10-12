# Marine 官方代码实例精讲（卷十七·8 个完整实例逐段解析）

> 来源：官方源码**逐字提取**（带起止行号，已抽查保真），每实例附逐段解析与可复用模式。
> 选例原则：完整可运行的单元（整函数/整方法/整回调链/整宏），覆盖 PML2 交互、事务、表单、批量、Hull 语句、宏生成、批处理、PML1 八大范式。
> 用法：写码前找同类实例 → 照官方结构套骨架 → 对照《PML生成规范》自查。

## 实例索引

| # | 范式 | 来源 | 行 |
|---|---|---|---|
| 1 | EDG 交互拾取回调链 | design\functions\edg3dpick.pmlfnc:37-75 + edg3dpickcb.pmlfnc:39-86（对照 pipecreation.pmlfrm:4376-4390） | 87+15 |
| 2 | UNDOABLE 事务生命周期 | design\forms\pipecreation.pmlfrm:930-1010 | 81 |
| 3 | 带校验表单四件套 | common\forms\createsygpar.pmlfrm:31-186 | 156 |
| 4 | COLLECTION+evaluate 批量 | admin\objects\admtextlist.pmlobj:132-223 + common\functions\getcriteriasetintersection.pmlfnc:44-58 | 107 |
| 5 | Hull 语句读改写 | hulldesign\functions\phullnotchcombine.pmlfnc:52-111+193-320 | 188 |
| 6 | P&ID 导入宏生成 | router\functions\rtrpidprocess.pmlfnc:213-283 | 71 |
| 7 | Isodraft 后台批处理 | pipefabricationmanager\draft\functions\pfPipeMakeIsoView.pmlfnc:29-133 | 105 |
| 8 | PML1 规格构建宏 | PDMSUI\CAT\specs\mbldspec:1-155 | 155 |

---

## 实例 1：EDG 交互拾取回调链

**来源**：`design\functions\edg3dpick.pmlfnc:37-75`（登记段）+ `edg3dpickcb.pmlfnc:39-86`（回调段）
**场景**：登记"拾取单个元素"请求压栈；拾取发生后回调收集 Dbref、调用用户函数、出栈关闭。

```pml
define function !!edg3DPick(!callback is STRING, !elemQualifier is STRING) is BOOLEAN

  !pickStack = object EDGPICKSTACK()
  show !!edg3DPickFrm

  !pickStack.callback  = !callback
  !pickStack.nameOfApp = 'EDG3DPick'
  !pickStack.elements  = ARRAY()
  !pickStack.dText     = 'Please pick a single element.'

  !!edg3DPickFrm.stack.append(!pickStack)
  !!edg3DPickFrm.text.val = 'Please pick a single element.'

  !args              = object EDGPUSHPARAMS()
  !args.pickHandler  = '!!edgPickFast'
  !args.inMode       = 'PICK'
  !args.userFunction = '!!edg3DPickCB(|ONE|)'
  !args.appName      = 'EDG3DPick'
  !args.showPickForm = FALSE
  !args.elementQual  = !elemQualifier
  !args.rootPrompt   = 'Please a single element'

  !bResult = !!edgPush(!args)

  return !bResult

endfunction
```

```pml
define function !!edg3DPickCB(!option is STRING)

  if(!option eq 'MANY') then
    !last = !!edg3DPickFrm.stack.maxIndex()
    !!edg3DPickFrm.stack[!last].elements.append(!!edgGeomData.pickedItem)
    return

  elseif(!option eq 'ONE') then
    !last = !!edg3DPickFrm.stack.maxIndex()
    !!edg3DPickFrm.stack[!last].elements.append(!!edgGeomData.pickedItem)

  elseif(!option eq 'OK') then
    -- OK button pressed, don't do anything but call User Function

  elseif(!option eq 'CANCEL') then
    !bResult = !!edgPop(!!edg3DPickFrm.stack.last().nameOfApp)
    !!edg3DPickFrm.stack.deleteFrom(!!edg3DPickFrm.stack.maxIndex() , 1)
    if(!!edg3DPickFrm.stack.maxIndex() eq 0) then
      !!edg3DPickFrm.hide()
    endif
    return
  endif

  if(!!edg3DPickFrm.stack.maxIndex() eq 1) then
    !!edg3DPickFrm.hide()
  endif

  !function = !!edg3DPickFrm.stack.last().callback
  $!<function>(!!edg3DPickFrm.stack.last().elements)

  !bResult = !!edgPop(!!edg3DPickFrm.stack.last().nameOfApp)
  !!edg3DPickFrm.stack.deleteFrom(!!edg3DPickFrm.stack.maxIndex() , 1)

  if(!!edg3DPickFrm.stack.set()) then
    !!edg3DpickFrm.text.val = !!edg3DPickFrm.stack.last().dText
  endif

endfunction
```

**对照（EDGPACKET 版，同一库并存）**——pipecreation.pmlfrm:4376-4390：
```pml
define method .pickposH()
  !prompt                = 'Modify Pipe - Select Head Position'
  !packet                = object EDGPACKET()
  !packet.initialisation = '!!pipeCreation.pickedHeadPosData  = object EDGPOSITIONDATA()'
  !packet.definePosition(!prompt)
  !packet.description    = 'Branch Head'
  !packet.remove         = TRUE
  !packet.action = '!!pipeCreation.setHeadTailPosition(!this.return[1],|Head| ) '
  !!edgCntrl.add(!packet)
endmethod
```

**解析要点**：
- 对象先于 UI 就绪（`object EDGPICKSTACK()` 后才 `show`），防回调触发时成员未定义；`elements` 显式 `ARRAY()` 保证 `.append()` 必然可用。
- EDGPUSHPARAMS 参数包模式：`userFunction` 存**带参回调串** `'!!edg3DPickCB(|ONE|)'`——竖线字面量嵌套引号是 EDG 传参标准写法。
- 回调按 `!option`（MANY/ONE/OK/CANCEL）分派；**CANCEL 也是一等路径**：`!!edgPop()` 出栈 + `deleteFrom()` 清栈 + 栈空 `hide()` 三步缺一不可。
- `$!<function>(...)` 动态触发字符串回调——callback 存字符串而非引用的原因。
- 每次索引前 `.maxIndex()/.set()` 判界，防空栈访问。
- **勘误**：design\functions 的 edg 系列实际用 EDGPUSHPARAMS+edgPush/edgPop 栈机制；EDGPACKET+edgCntrl.add 在表单回调中（对照段）。两种 API 并存，卷十二 EDG 精要以 packet 版为主。

## 实例 2：UNDOABLE 事务生命周期（.createPipe）

**来源**：`design\forms\pipecreation.pmlfrm:930-1010`（成员声明 `member .undo is UNDOABLE` 在 :412）

```pml
define method .createPipe()

  !message          = ARRAY()

  -- Can we create a pipe at this position in this hierarchy
  !owningTypes      = !!ce.ahList
  !owningTypes.append(!!ce.type)
  !owningTypes.appendArray(!!ce.list)

  -- Have we got creat access
  if(!!ce.dbWrite.not()) then
    !message.append('Unable to create pipe in this database. Navigate')
    !message.append('to database with the right access and press "Done".')

  elseif  (!owningTypes.findFirst('PIPE').unset()) then
    !message.append('Unable to create pipe at this point within the')
    !message.append('hierarchy. Navigate to the appropriate place ')
    !message.append('within database and press "Done".')

  endif

  -- Generate a warning
  if(!message.set()) then
    !this.warning(!message, '!this.createPipe()')
    return
  endif

  -- Define UNDO Information
  if(!this.pipeName.val.empty()) then
    !this.undo.description('Created pipe')
  else
    !this.undo.description('Created pipe ' & !this.pipeName.val)
  endif
  !this.undo.add()

  NEW PIPE
  handle ANY
    !error  = !!error.text.after(')').trim()
    !message.append('Unable to create pipe:')
    !message.append('    "' & !error & '"')
    !this.warning(!message, '!this.createPipe()')
    return
  endhandle

  !this.pipe        = !!ce
  !this.processData = object PIPINGPROCESSDATA(!this.pipe)
  !this.branch      = object DBREF()
  !this.branches    = ARRAY()

  !this.updatePipeData()
  !this.createBranch(false)

  !this.undo.endUndoable()

  !this.modify(!this.branch)

endmethod
```

**解析要点**：
- 层次合法性全基于 CE 祖链（`!!ce.ahList/.type/.list`）——表单类依赖全局 CE 的官方惯例。
- BOOLEAN 统一 `.not()/.unset()/.set()/.empty()`；`findFirst` 找不到返回 UNSET 而非 FALSE，必须 `.unset()` 检测。
- **两级错误路径**：预检级（warning + 回调字符串 `'!this.createPipe()'` 传给警告表单，用户修正后原路重入）与运行级（`handle ANY` + `!!error.text.after(')').trim()` 解析人类可读错误 + return）。
- UNDO 三件套：`.description()` → `.add()` → `.endUndoable()`；**handle 分支 return 跳过收口 = 隐式回退**（UNDO 区间自然废弃）。
- CE 写后快照：NEW 后立即 `!this.pipe = !!ce`。
- **官方瑕疵登记**：973-977 行 UNDO 描述 if/else 条件与语义相反（空名时走不带名分支）——官方库也有逻辑瑕疵，引用时注意。

## 实例 3：带校验表单四件套（createsygpar）

**来源**：`common\forms\createsygpar.pmlfrm:31-186`

```pml
setup form !!createSyGpar

  member .owner is DBREF

  text .name 'Name       ' width 20 scroll 40 is STRING
  path down
  text .func 'Function   ' width 20 scroll 40 is STRING
  text .desc 'Description' width 20 scroll 40 is STRING
  text .purp 'Purpose    ' width 4 is STRING

  button .ok      ' OK '   at xmin form-0    ymax+0.25 ok
  button .cancel  'Cancel' at xmax form-size ymin      cancel

exit

define method .createSyGpar()

  !this.formTitle     = 'Create System Group Area'
  !this.iconTitle     = 'SyGpar'
  !this.initcall      = '!this.initialise()'
  !this.formRevision  = ' $Revision: 1 $ '

  !this.ok.callback     = '!this.ok()'
  !this.name.callback   = '!this.name()'

endmethod

define method .initialise()

 !this.name.val= 'unset'
 !this.func.val= 'unset'
 !this.desc.val= 'unset'
 !this.purp.val= 'unset'
 !this.owner=!!ce

endmethod

define method .name()

 !name = !!checkName(!this.name.val,'NEW')
 if (!name.unset()) then
  !this.name.val = 'unset'
  !this.name.setFocus()
 else
  !this.name.val=!name
 endif

endmethod

define method .ok()

 !!ce=!this.owner

if (!this.name.val.unset()) then
  !answer=!!alert.confirm('Is it OK to leave the System Group Area unnamed')
  if (!answer eq 'YES') then
    NEW SYGPAR
  else
    hide !!createSyGpar
    show !!createSyGpar
    return
  endif
else
  NEW SYGPAR $!this.name.val
endif
!newEle = !!ce
!ownerName = !!ce.owner.name

if (!this.func.val.set()) then
  FUNC '$!this.func.val'
endif
if (!this.desc.val.set()) then
  DESC '$!this.desc.val'
endif
if (!this.purp.val.set()) then
  PURP $!this.purp.val
endif

END

if (!!systemHierarchy.trackCE.val) then
  !!systemHierarchy.trackNewElement(!newEle)
else
  !!systemHierarchy.systemExplorer.selectElement(!ownerName)
endif
endmethod
```

**解析要点**：
- **四件套分工**：同名构造器（接线：标题/initcall/callback）→ `.initialise()`（复位 + `!this.owner=!!ce` CE 快照）→ `.name()`（失焦校验：`!!checkName` 外置全局函数 + `setFocus()` 引导改正）→ `.ok()`（兜底校验 + 建元素 + 收尾联动导航树）。
- 空态统一 `'unset'` 字符串哨兵，使 `.set()/.unset()` 全生命周期可靠。
- ok 必须自带校验兜底（用户可能未触发字段回调）；放弃路径 `hide`+`show` 强刷表单。
- `$!this.xxx.val` 两种内插：带引号（字符串属性 `FUNC '$!...'`）与不带引号（数值属性 `PURP $!...`）。
- **对照讲解点**：本方法 NEW 未包 handle（官方小工具省略）——与实例 2 的 handle 纪律对照，自研代码应从严。

## 实例 4：COLLECTION+evaluate 批量读取

**来源**：`admin\objects\admtextlist.pmlobj:132-223`（主方法）+ `common\functions\getcriteriasetintersection.pmlfnc:44-58`（COLLECTION 对照）

```pml
define method .addUsers(!dbRefArray is ARRAY, !listFormat is USERLISTATTR, !useHeader is BOOLEAN, !list is GADGET )

  !list.clear()
  !this.colFmt = ARRAY()
  !this.colSpace = ARRAY()

  if (!dbRefArray.unset()) then
    return
  endif

  if (!useHeader) then
    !displayText  = |<USER>  |
  else
    !displayText  = ||
  endif

  !objectType = !dbRefArray[1].objectType()
  if(!objectType EQ |DBREF|)then
    !block = object BLOCK( '!dbRefArray[!evalIndex].string()' )
  elseif(!objectType EQ |ADMVIRTUSER|)then
    !block = object BLOCK( '!dbRefArray[!evalIndex].name.dbref().string()' )
  else
    return
  endif
  !stringRefs   = !dbRefArray.evaluate(!block)

  -- old EVAL syntax used for performance
  VAR !names EVAL ( replace(NAME,'/',!displayText,1,1) ) FOR ALL FROM !stringRefs
  if(!listFormat.name) then
    !this.cd[1]     = !names
    !this.colFmt[1] = ''
  endif
  if (!listFormat.password) then
    VAR !temp EVAL (PASSQUALITY ne 0) FOR ALL FROM !stringRefs
    !block          = object BLOCK( '!temp[!evalIndex]' )
    !names          = !temp.evaluate(!block)
    !this.colFmt[2] = ''
    !this.cd[2]     = !names
  endif
  if (!listFormat.security) then
    VAR !temp EVAL SECURITY FOR ALL FROM !stringRefs
    !block          = object BLOCK( '|[| + !temp[!evalIndex] + |]|' )
    !this.cd[3] = !temp.evaluate(!block)
    !this.colFmt[3] = ''
  endif
  if (!listFormat.description) then
    VAR !temp EVAL DESCRIPTION FOR ALL FROM !stringRefs
    !this.cd[4] = !temp
    !this.colFmt[4]  = ''
  endif

  !validHeadings = !!admDisplayConfig.userFormat.order
  do !i indices !validHeadings
    if(!!admDisplayConfig.userFormat.attribute(!validHeadings[!i].upcase())) then
      !heading[!i] = !!admDisplayConfig.userFormat.order[!i]
      if (!heading[!i] eq 'Password') then
        !heading[!i] = 'Password?'
      endif
    endif
   enddo
  !heading.compress()
  !list.setHeadings(!heading)

  !this.buildTable(!list)
  !list.rText = !stringRefs

endmethod
```

COLLECTION 对照段（getcriteriasetintersection.pmlfnc:44-58）：
```pml
    !collection = object COLLECTION()
    !expression = object EXPRESSION('MATCHWILD(DESCRIPTION, |*' & !attributeName.upCase() & '|)')
    !collection.filter(!expression)
    !collection.scope(!allDDSets[1])
    !collection.type('DDAT')
    !allDDat = !collection.results()
    skip if ( !allDDat.empty() )
```

**解析要点**：
- **批量求值双引擎**：新式 `object BLOCK('...[!evalIndex]...') + ARRAY.evaluate()`，旧式 `VAR !x EVAL ... FOR ALL FROM !array`——官方注释明示旧语法**用于性能**。
- `!evalIndex` 是 evaluate 隐式循环变量，BLOCK 串内可任意编排（`.string()`、`.name.dbref().string()`、`'|[| + ... + |]|'` 竖线转义嵌套）。
- 入口防御三连：控件 clear、成员重建、`unset() return`；未知 objectType 也 return。
- 显示/数据分离：`.dText/.cd` 给眼睛，`.rText` 留 DBREF 给程序（双击导航）。
- COLLECTION 标准链：filter(EXPRESSION) → scope → type → results → `skip if (.empty())`。

## 实例 5：Hull 切口语句合并（读语句→改写→再执行）

**来源**：`hulldesign\functions\phullnotchcombine.pmlfnc:52-111 + 193-320`（全函数 L30-320）

```pml
  -- Check if notches are on the same panel
  if (!firstNotch[2] ne !secondNotch[2]) then
    !mUI.messageNoConfirm('Notches not on the same panel!')
    return
  endif

  !firstNotchGroup = !mHullPan.groupGet(!firstNotch[2], !firstNotch[3])
  !secondNotchGroup = !mHullPan.groupGet(!secondNotch[2], !secondNotch[3])
  !firstNotchStmt = !mHullPan.stmtGet(!firstNotch[2], !firstNotchGroup)
  !secondNotchStmt = !mHullPan.stmtGet(!secondNotch[2], !secondNotchGroup)
  !firstNotchStmtArr = !firstNotchStmt.split(',')
  !secondNotchStmtArr = !secondNotchStmt.split(',')

  -- First notch selected is corner notch
  if (!firstNotchStmt.matchWild('*COR*')) then
    if (!firstNotchStmt.substring(!firstNotchStmt.match('COR=') + 5, 1).matchWild('(')) then
      !corString = !firstNotchStmt.after('COR=').substring(1,5)
      !corners = !!phullrepetitionsplit(!corString, 1)
      do !in indices !corners
        !coord = !!phullretrievecorner(!firstNotch[2], !corners[!in])
        if ((!coord[1] eq !firstNotch[0].real()) and (!coord[2] eq !firstNotch[1].real())) then
          !firstCor = !corners[!in]
          !corDefType = 1
          !corners.remove(!corners.findFirst(!firstCor))
          break
        endif
      enddo

    elseif (!firstNotchStmt.substring(!firstNotchStmt.match('COR=') + 5, 1).matchWild(',') and !firstNotchStmt.replace(' ','').substring(!firstNotchStmt.match('COR=') + 3, 1).matchWild('L').not()) then
      !corString = !firstNotchStmt.after('COR=').before(', ').before(';')
      !corners = !corString.split(',')
      do !in indices !corners
        !coord = !!phullretrievecorner(!firstNotch[2], !corners[!in].real())
        if ((!coord[1] eq !firstNotch[0].real()) and (!coord[2] eq !firstNotch[1].real())) then
          !firstCor = !corners[!in]
          !corDefType = 2
          !corners.remove(!corners.findFirst(!firstCor))
          break
        endif
      enddo

    else
      !firstCor = !firstNotchStmt.after('COR=').before(',').before(';')
    endif

    !firstRad = !firstNotchStmtArr[2].replace('R',' ').trim().real()
    if (!secondNotchStmt.matchWild('*LIM*')) then
      !secondLim = !secondNotchStmt.after('LIM=').before(',').before(';')
    elseif (!secondNotchStmt.matchWild('*SEA*')) then
      !secondSeam = !secondNotchStmt.after('SEA=').before(',').before(';').real()
      !secondSeamPan = !secondNotchStmt.after('''').before('''')
      !refPanel = !secondNotch[2]
    elseif (!secondNotchStmt.matchWild('*COR*')) then
      !mUI.messageNoConfirm('Combining two corner notches not allowed!')
      return
    endif
```

```pml
  -- Retrieve data from seam notches
  !seamInfo = !mHullPan.getNearbySeams(!refPanel)
  if (!firstSeam neq 0 or !secondSeam neq 0) then
    do !in indices !seamInfo
      if (!firstSeam eq !seamInfo[!in].seamNo() and !firstSeamPan eq !seamInfo[!in].panelName()) then
        !firstNotch[0] = !seamInfo[!in].uCoord().string()
        !firstNotch[1] = !seamInfo[!in].vCoord().string()
        !firstNotch[4] = !seamInfo[!in].limNo().string()
      endif
      if (!secondSeam eq !seamInfo[!in].seamNo() and !secondSeamPan eq !seamInfo[!in].panelName()) then
        !secondNotch[0] = !seamInfo[!in].uCoord().string()
        !secondNotch[1] = !seamInfo[!in].vCoord().string()
        !secondNotch[4] = !seamInfo[!in].limNo().string()
      endif
    enddo
  endif

  -- Set length of a new notch
  if (DEFINED(!firstRad) and DEFINED(!secondRad)) then
    !newNotchLen = SQRT(POWER((!firstNotch[0].real() - !secondNotch[0].real()), 2) + POWER((!firstNotch[1].real() - !secondNotch[1].real()), 2)) + !firstRad + !secondRad
  else
    !mUI.messageNoConfirm('Error while acquiring notch radii!')
    return
  endif

  !newNotchMidU = (!firstNotch[0].real() + !secondNotch[0].real()) / 2
  !newNotchMidV = (!firstNotch[1].real() + !secondNotch[1].real()) / 2

  if (!firstNotch[1] eq !secondNotch[1]) then
    !newNotchMid = !newNotchMidU
    !coordParam = ', U='
  else
    !newNotchMid = !newNotchMidV
    !coordParam = ', V='
  endif

  -- Setting new notch creation statements
  if (DEFINED(!firstCor) and DEFINED(!secondLim)) then
    if (!firstRad eq !secondRad) then
      !radius = !firstRad
    else
      !radius = !firstRad & '*' & !secondRad
    endif
    !newNotchLim = !secondLim
    !newNotchC = !firstCor
    !newNotchL = !newNotchLen - !firstRad
    !newNotchLenA = !!phullroundnumber(!newNotchL)
    !newNotchStmt = 'NOT, VU' & !newNotchLenA & '*' & !radius & ', COR=' & !newNotchC & ', LIM=' & !newNotchLim & ';'

  elseif (DEFINED(!firstLim) and DEFINED(!secondLim)) then
    !newNotchLim = !firstLim
    !newNotchB = max(!firstRad, !secondRad)
    !newNotchStmt = 'NOT, KU' & !newNotchLen.nint() & '*' & !newNotchB & ', LIM=' & !newNotchLim & !coordParam & !newNotchMid.nint() & ';'
  endif

  -- (其余 4 个镜像分支同构：L114-191，见源文件)

  !notchGroup = 0

  -- Check if statements with multiple corner notch definitions need to be updated
  if (DEFINED(!corDefType)) then
    !partStmt = ''
    do !in indices !corners
      !partStmt = !partStmt & !corners[!in].string()
      if (DEFINED(!corners[!in + 1])) then
        !partStmt = !partStmt & ','
      endif
    enddo
    if(!firstNotchStmt.matchWild('*COR*')) then
      !partFront = !firstNotchStmt.before('COR=')
    else
      !partFront = !secondNotchStmt.before('COR=')
    endif
    !corStmt = !partFront & 'COR= ' & !partStmt & ';'
  endif

  -- Execute creation and removal of notches
  !mHullPan.panActivate(!firstNotch[2])
  !mHullPan.stmtExecSingle(!notchGroup, !newNotchStmt, !firstNotch[2])
  !mHullPan.panGroupDelete(!firstNotch[2], !firstNotchGroup)
  !secondNotchGroup = !mHullPan.groupGet(!secondNotch[2], !secondNotch[3])
  !mHullPan.panGroupDelete(!secondNotch[2], !secondNotchGroup)
  if(DEFINED(!corDefType)) then
    !mHullPan.stmtExecSingle(!notchGroup, !corStmt, !firstNotch[2])
  endif
endfunction
```

**解析要点**：
- **Hull 参数化修改固定五步**：groupGet → stmtGet → 字符串解析 → 模板拼接新语句 → stmtExec/stmtExecSingle——绝不直接改几何属性（面板是语句历史驱动的参数化模型）。
- 语句解析必须按"重复语法 `COR=1(5)` / 逗号列表 / 单值"多分支全覆盖；token 定位用 `match()+substring+after/before`，不用正则。
- 焊缝切口只存 `SEA=` 序号，几何经 `getNearbySeams` 二次解析回写——语句存拓扑、几何实时求。
- 多角 COR 列表消费一部分后，**剩余角重组语句回写**（`!partFront & 'COR= ' & ...`）——保持设计历史合法可回放。
- 新语句两种模板：`NOT, VU<len>*<rad>, COR=.., LIM=..;`（双半径不等写 `R75*R50`）与 `NOT, KU<len>*<rad>, LIM=.. U=/V=..;`——分号收尾（HML-01 规则出处）。
- **本文件零 handle**：前置校验 + messageNoConfirm + return——与 Design 模块 handle 风格对比；且未调 panRecreate/panStore（stmtExecSingle 引擎内部重算）。

## 实例 6：P&ID 导入宏生成（writeRecord 范式）

**来源**：`router\functions\rtrpidprocess.pmlfnc:213-283`（Pass 2 主循环 START PIPE 分支）

```pml
  elseif (!line.match(|START|) gt 0) then

    if (!words[2].match(|PIPE|) gt 0) then

      !string = !!messageFile.messageString(162,65,!words[3] )
      !!rtrWriteLog( !logFile, !string )

      !pipeName = !words[3]
      !pipeBore = !line.after( 'BORE' )
      !pipeBore = !pipeBore.part( 1 )

      !currentBore = !pipeBore.real()

      !pspe = !line.after(|PSPE|).part(1)

      -- If it has been spelt PSPEC (not PSPE), get second part

      if( !pspe eq |C|) then
        !pspe = !line.after(|PSPEC|).part(1)
      endif

      if ( !pspe eq ||) then
        !string = 'WARNING: '
        !string = !string + !!messageFile.messageString(162,66,!pipeName )
        !string = !string + !!messageFile.messageString(162,58,!lineNumber.string() )
        !string = !string + !!messageFile.messageString(162,67 )
        !!rtrWriteLog( !logFile, !string )

        if ( !defaultPspec ne '' ) then
          !line = !line + ' PSPE /' + !defaultPspec
        endif
        !pspe = !defaultPspec
      endif

      !oldSize = !replaced.size()
      if ( not !!rtrPIDreplace( !pipeName, !ask, !replaced ) ) then
        !string = !!messageFile.messageString(162,73 )
        !!rtrWriteLog( !logFile, !string)

        break
      elseif ( !replaced.size() gt !oldSize ) then
        !pipe = !pipeName.dbRef()
        !oldBranches = !pipe.members
        !string = !!messageFile.messageString(162,68,!pipeName )
        !!rtrWriteLog( !logFile, !string)
        !string = !!messageFile.messageString(162,69,!pipeName )
        !newOrOld = 'OLD '
      else
        !oldBranches = ARRAY()
        !string = !!messageFile.messageString(162,70,!pipeName )
        !newOrOld = 'NEW '
      endif

      !details = !line.after(|PIPE|)

      !macroFile.writeRecord( || )
      !macroFile.writeRecord( |    !!rtrWriteLog( !logFile, '' ) | )
      !macroFile.writeRecord( |    !!rtrWriteLog( !logFile, '$!string' ) | )

      !macroFile.writeRecord( |$!newOrOld PIPE $!details| )

      -- ERROR checking after "NEW PIPE /XXX PSPEC /mmm"

      !macroFile.writeRecord( |  handle ANY| )
      !string = 'ERROR: Pipe ' + !pipeName + ' (Line ' + !lineNumber.string() + ') '
      !string = !string + !!messageFile.messageString(162,71)
      !macroFile.writeRecord( |    !!rtrWriteLog( !logFile, '$!string' ) | )
      !macroFile.writeRecord( |    !!rtrWriteLog( !logFile, !!error.text ) | )
      !macroFile.writeRecord( |  endhandle| )

      !branchCount = 0
```

**解析要点**：
- **解析器+生成器双阶段**：PML 函数只解析裁决，pid????.tmp 宏才是执行体——可重放、可审计、`var !unique unique` 多用户隔离。
- **错误处理可以"生成"**：把 `handle ANY / !!rtrWriteLog(!!error.text) / endhandle` 按模板 writeRecord 进宏，批执行时同样有错误捕获。
- 输入容错三件套：拼写兼容（PSPE/PSPEC——`after('PSPE')` 切出 C 判别后改用 `after('PSPEC')`）、默认值回填（修补进 `!line` 本身）、NEW/OLD 幂等裁决（`!!rtrPIDreplace` 探测同名管，拒绝则 break 终止）。
- `$!var` 在 writeRecord 时刻展开固化成宏文本；跨行状态（`!currentBore`）在解析器侧维护，宏里只写结论。
- 日志带行号 `!lineNumber` 一路进错误文本——可追溯性设计。

## 实例 7：Isodraft 后台批处理（完整函数）

**来源**：`pipefabricationmanager\draft\functions\pfPipeMakeIsoView.pmlfnc:29-133`（全文）

```pml
define function !!pfPipeMakeIsoView(!spoolList is ARRAY, !optionFilePath is STRING, !pdmsUserPath is STRING) is BOOLEAN

  var !spooldebug evar 'TRACE_SPOOLDRAWINGS'
  if !spooldebug.neq('') then
    $r101/c:\temp\pfPipeMakeIsoView.pmldat
  endif

  var !projCode proj code
  var !mdb mdb
  var !user user
  var !installenv      evar 'pdms_installed_dir'
  var !installenvaddin evar 'pdms_installed_dir'

  !debugFlag = false

  !userlogin = object PMLUSERLOGIN()
  !userlogin.project(!projCode)
  !userlogin.mdb(!mdb)

  var !path evar pdmswk
  !path = !path.replace(';','')
  !userlogin.saveToFile(!path & '\temp_login_' & !user & '.tmp')

  !macfile = object FILE('$!pdmsUserPath\makeisoview.mac')
  !macfile.open('OVER')

  !macfile.writeRecord('$m "/$!path\temp_login_' & !user & '.tmp"')
  !macfile.writeRecord(!mdb)
  !macfile.writeRecord(|ISODRAFT|)

  !contentsFile = object FILE('$!pdmsUserPath\isospllist.dat')
  !contentsFile.open('OVER')
  handle any
    return false
  endhandle
  do !entry values !spoolList
    !contentsFile.writeRecord(!entry.flnm)
  enddo
  !contentsFile.close()

  !macfile.writeRecord(|!!pfpipemakeoverlyingview('$!optionFilePath', '$!pdmsUserPath')|)

  !macfile.writeRecord(|!donefile = object FILE('$!pdmsUserPath\spooldwgdone.log')|)
  !macfile.writeRecord(|!donefile.open('OVER')|)
  !macfile.writeRecord(|!donefile.writeRecord('DONE')|)
  !macfile.writeRecord(|!donefile.close()|)

  if (!debugFlag.not()) then
    !macfile.writeRecord(|FINISH|)
  endif
  !macfile.close()

  !batchFile = object FILE('$!pdmsUserPath\makespooldrwg.bat')
  !batchFile.open('OVER')
  !batchFile.writeRecord(|setlocal|)
  !batchFile.writeRecord(|set savepath=%path%|)
  !batchFile.writeRecord(|set pdms_installed_dir=$!installenv|)
  !batchFile.writeRecord(|set pdms_installed_addin_dir=$!installenvaddin|)
  !batchFile.writeRecord(|set AVEVA_MARINE=YES|)
  !batchFile.writeRecord(|set MARINE=YES|)
  !batchFile.writeRecord(|call "%pdms_installed_addin_dir%\evars.bat" "%pdms_installed_addin_dir%"|)
  if (!debugFlag) then
    !batchFile.writeRecord(|"%pdms_installed_dir%\MON"  tty  -macro="$!pdmsUserPath/makeisoview.mac"|)
  else
    !batchFile.writeRecord(|"%pdms_installed_dir%\MON"  tty  -noconsole -macro="$!pdmsUserPath/makeisoview.mac"|)
  endif

  !batchFile.writeRecord(|endlocal|)
  !batchFile.writeRecord(|exit|)
  !batchFile.close()

  if (!debugFlag) then
    SYSCOM 'START  cmd.exe /C "$!batchFile" &'
    return
  endif

  !batchFileFullPath = !batchFile.fullname()
  import 'PipeFabricationAddin'
  handle any
  endhandle

  using namespace 'Aveva.Pdms.PipeFabrication.RunBatchProc'
  !runBatchProc = object RUNBATCHPROCESS()
  handle any
    SYSCOM 'START /MIN cmd.exe /C "$!batchFile" &'
  elsehandle none
    !runBatchProc.run(!batchFileFullPath)
  endhandle
endfunction
```

**解析要点**：
- **后台批处理四件套**：登录宏（$M 引用）+ 业务宏 + 数据清单 + .bat 装配；全部 `object FILE` + `writeRecord`，open('OVER')/close 严格成对。
- `$M` 解决后台进程自动登录：`PMLUSERLOGIN` 现场生成 temp_login_*.tmp，宏首行 `$m` 引入——口令不落地业务宏。
- **DONE 标志文件**做完成信号（把写标志的代码生成进宏），避免主会话轮询进程句柄。
- **`handle any / elsehandle none` 双通道**：any=异常路径（降级 SYSCOM 弹窗），none=正常路径（RUNBATCHPROCESS 托管同步等待）——"优先托管、失败退化"写法。
- PML1 遗产（`$r101` 调试记录、`$m`、SYSCOM、`|...|`）与 PML2（object FILE、import、using namespace）同一函数共存——Marine 生产代码混合风格实况。
- 非调试模式补 `FINISH` 干净退出；FILE 打不开直接 `return false` 短路。

## 实例 8：PML1 规格构建宏（mbldspec 全文范式）

**来源**：`PDMSUI\CAT\specs\mbldspec:1-155`（全文 155 行；节选核心段，全文见源文件）

```pml
$(H
-- Macro:   mbldspec
$)
$:debug$:

$* Initialise Variables
 var USER   _CDTBLDSPEC sel 1
 var !SPEC |$_CDTBLDSPEC_USERDATA|
 var !DESC |$_CDTBLDSPEC_CEDESC|

$* Move to Specification
 $!SPEC
 LOCK ALL
 UNLOCK CE

$* Get Spec Information
 var !SPQU |TYPE|      $* Spec Question
 var !SEQ1 |PBOR|      $* Sele Level 1 Question
 var !SCAN1 |answ (PPBORE 1 of CATR)| $* Spec Component Answer
 var !SCAN2 |maxa (PPBORE 1 of CATR)| $* Spec Component Answer

$* Structural Steel Spec
 if(PURP of SPWL eq |STL| and PURP of SPEC eq |STL|) then
   var !SEQ1 |GTYP|      $* Sele Level 1 Question
   var !SCAN1 |answ (gtype of catref)|          $* Spec Component Answer
   var !SCAN2 ||          $* Spec Component Answer
 endif

$* Set Description
 DESC |$!DESC|
 QUES $!SPQU

$* Loop through Generic Types
 do !SELE indices !!CDCADESC

   var !SDESC |$!!CDCADESC[$!SELE]|

   if(|$!SDESC| eq ||) then
     var !DFLG  true
   else
     var !DFLG  false
   endif

   if(undefined(!!CDPASELE[$!SELE])) then
     var !SSELE |New Sele|
     var !NFLG  true
   else
     var !SSELE |$!!CDPASELE[$!SELE]|
     var !NFLG  false
   endif

   var !VNAM  |!!CDSPCO$N$!SELE|

   if(not $!DFLG) then

     if($!NFLG) then
       $!SPEC
       NEW SELE DESC |$!SDESC|
     else
       $!SSELE
       UNLOCK CE
     endif

     QUES $!SEQ1
     var !NSELE REFE

     do !SPCO values $!VNAM

       var !ITEM coll all SPCO with (REFE of CATR eq $!SPCO ) for $!NSELE

       if(arraysize(!ITEM) eq 0) then

         var !NNAM (NAME of $!SPEC  + NAME of $!SPCO )
         var !EXIST exists $!NNAM
         var !FLAG (substr(|$!EXIST|,1,1))

         if($!FLAG) then
           error |$!NNAM is already in Spec.|
           skip
         else
           NEW SPCO $!NNAM
         endif

       else
         $!ITEM[1]
         UNLOCK CE
       endif

       CATR $!SPCO
       $!SCAN1
       $!SCAN2

     enddo

   endif $* End of Modify/Create SELE

 enddo

$* Get all SPCO that are still locked and then delete them
 $!SPEC
 var !DLST coll all SPCO with (lock) for $!SPEC

 UNLOCK ALL
 do !DSPCO values !DLST
   $!DSPCO
   DELETE SPCO
 enddo

 $!SPEC

$* --- also delete sele's with no members PUR 24340
 var !SLST coll all SELE with (mcount eq 0) for $!SPEC
  do !DSELE values !SLST
     $!DSELE
     DELETE SELE
  enddo

$* Reload Form
 CALLCSP IBLDSPEC

return
$.
```

**解析要点**：
- **PML1/PML2 差异全谱**（对照教材）：`$*` 注释 / `$!VAR` 命令行展开 / `var`+`coll`+`exists` / `error`+`skip`（无 handle） / `CALLCSP` 库调用 / `$.` 宏终结符。
- **数据即代码**：问句/答案表达式全部存字符串变量，`$!SCAN1` 展开即执行 `answ (PPBORE 1 of CATR)`——PML1 无对象，表单→宏传值靠 `$` 全局变量与双叹号 PML2 全局数组（!!CDCADESC，PML1 do 可直接索引 PML2 数组）。
- **锁当差异集**：开头 `LOCK ALL + UNLOCK CE`，结尾 `coll all SPCO with (lock)` 收集仍锁者 DELETE——被表单改过的保持锁定，锁状态即脏标记，替代事务日志。全宏最巧妙设计。
- `$N`/`$!SELE` 命名约定模拟二维数组（每 SELE 一套 SPCO 数组）。
- 重名防御：`exists` + `substr(|$!EXIST|,1,1)` 首字符当布尔；`error |...|` + `skip`（= continue）。
- `PUR 24340` 是 AVEVA 内部缺陷单号——官方源码缺陷追溯痕迹。
- 结构钢特判：PURP=STL 整体换 GTYP 问答体系——同一宏按规格用途切换模板。

---

## 横向对照：八实例的工程纪律矩阵

| 纪律 | 实1 EDG | 实2 UNDO | 实3 表单 | 实4 批量 | 实5 Hull | 实6 宏生成 | 实7 批处理 | 实8 PML1 |
|---|---|---|---|---|---|---|---|---|
| 错误处理 | CANCEL 一等路径+判界 | 预检+handle ANY 两级 | confirm+return | unset return | 前置校验+return（零 handle） | 错误宏生成进批文件 | 短路 return+双通道降级 | error+skip |
| 状态管理 | 栈进出配对 | UNDO 三件套 | CE 快照还原 | rText 关联 | 语句历史回写 | 跨行状态解析器持有 | DONE 标志文件 | LOCK 当脏标记 |
| 动态执行 | $!<function> | — | $! 内插两式 | BLOCK !evalIndex | 语句模板拼接 | writeRecord 时展开 | $M 嵌宏 | $!SCAN 展开即执行 |

**使用建议**：写交互工具→套实例 1+3；写写库操作→套实例 2；写报表/批量→套实例 4；写船体工具→套实例 5；写导入/批处理→套实例 6+7；维护 PML1→对照实例 8。
