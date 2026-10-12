# Marine Router 布线命令大全（穷举级·源码实证）

> 来源：逐文件全文读取 Router 模块 21 文件 + pipecreation.pmlfrm(4522行) + componentcreation.pmlfrm(8851行) + design\functions 布线相关 33 文件。
> 所有代码块均带源文件路径与行号，可直接回查。
> 适用：AVEVA Marine (PDMS 系) 12.1 SP4。管道布线、Router 约束、P&ID 导入、管件创建、管段拆分全收录。

---

## 1. 布线引擎核心命令

### 1.1 Router 配置（弯头自动插入等）

`PMLLIB\design\functions\pipeSimpleAutoRoute.pmlfnc:48-53`：
```pml
  ROUTER
    --CONFIGURATION DIRECTION  $!dir
    CONFIGURATION DIRECTION  ELBOW      $* 方向变更用弯头(BEND/ELBOW/RULE 三选)
    CONFIGURATION PRSPACE    $!gap      $* 平行管间距
    CONFIGURATION PRROUNDING $!round    $* 圆角半径
  EXIT
```

关闭错误消息 / 清除全部约束（L60-63、L89-91）：
```pml
  router
    --config error mess
    config error off
  exit
...
  router
  config error off
  clear all
```

分支布线状态复位（L74）：`BSTAT 0`（"not Routed"）。

**方向变更三模式**（`router\forms\rtrdefaults.pmlfrm:76-81` 下拉项）：
```pml
  !changeDir[1] = |Bend|      $* 折弯
  !changeDir[2] = |Elbow|     $* 弯头
  !changeDir[3] = |Rule    |  $* 按规则
```

### 1.2 布线主体：加途经点 + 执行布线

`pipeSimpleAutoRoute.pmlfnc:93-113`（完整官方范式，含错误码）：
```pml
  do !point values !positions
    !pointStr = 'E ' & !point.east.string('D2') & ' N ' & !point.north.string('D2') & ' U ' & !point.up.string('D2')
    skip if (!hposStr eq !pointStr or !tposStr eq !pointStr)
    new point at $!point after $!element     $* ★ NEW POINT AT <pos> AFTER <branch> = 加途经点
  enddo

  route $!element                            $* ★ ROUTE <branch> = 执行布线
  handle none
    EXIT
    BSTAT 1                                  $* 布线成功 → Routed
  elsehandle (61,721)                        $* ★ 布线失败错误码
    EXIT
    BSTAT 2                                  $* 布线失败 → Failed
  elsehandle any
    exit
  endhandle
```

头尾点过滤用 `!element.hpos.wrt( /* )` / `!element.tpos`（L83-87）。

### 1.3 Router 约束查询（ICONS 体系）

逐个枚举分支上的 Router 约束图标（`router\functions\rtrgeticonnum.pmlfnc:47-64`）：
```pml
  do !x
    ROUTER
      var !after ICONS POINT $!x COMPONENT    $* 点约束
      handle any
        var !after ICONS PLANE $!x COMPONENT  $* 平面约束
        handle any
          EXIT
          break                               $* 无更多约束，退出
        endhandle
        EXIT
      elsehandle none
        EXIT
    endhandle
  enddo
```
`HEAD` 判断（L66）：`if ( !after eq |HEAD| )`；排序键 `!element.sequ`（L44）。

**统计约束数**（`rtrnumberofconstraints.pmlfnc:41-44`）：
```pml
  !!ce = !branch
  ROUTER
  var !numberConstraints ICONS NUMB
  EXIT
```

**点约束全字段查询**（`rtrpointdetails.pmlfnc:60-110`，Arrive/Leave/Direction/FIXED）：
```pml
  ROUTER
    var !field3 ICONS POINT $!iconsNum ACTUAL POSITION WRT $_cdPoints_WRT
    var !field4 ICONS POINT $!iconsNum DIR
    var !field5 ICONS POINT $!iconsNum LEAV
    handle(62,707)                          $* LEAV 不存在时的错误码
      EXIT
      var !field5 ||
      ROUTER
    elsehandle none
      exit
    endhandle
    -- Arrive/Direction 文本判定
    if(|$!field5| eq || and |$!field4| neq ||) then
      var !field4 |Direction $!field4|
    elseif(|$!field4| neq ||) then
      var !field4 |Arrive $!field4|
    endif
    ROUTER
      var !unusedFx ICONS POINT $!iconsNum FIXED
    EXIT
```
方向名 ENU↔XYZ 换算（L72、L75）：`!field4.replace('E','X').replace('W','-X')...`。

单位精度切换（L48-52）：英制 `PRECISION VAR 1/16`；公制 `PRECISION VAR 1DP`。

**平面约束细节**（`rtrplanedetails.pmlfnc:34-78`）：
```pml
  ROUTER
    var !rplane ICONS PLANE $!iconsNum RPLA
  EXIT
  var !ty TYPE
  RPLA1
  handle any
    !record[1] = |Unpositioned| & '	' & |No Planes|
  endhandle
  var !pos  POS WRT $_cdPoints_WRT
  var !enex PLED
  !planeOri = !!ce.ori
  !xDir = !planeOri.yDir().orthogonal(!planeOri.zDir())
```
可视化标注（L110、L122-144，AID 家族全用法）：
```pml
    AID TEXT NUMBER $!!noOfSp |$!rplane| AT $!pos WRT $_cdPoints_WRT
    AID SPHERE NUMBER $!!noOfSp $!field3  WRT $_cdPoints_WRT DIAMETER 250 MM
    AID ARROW NUMBER $!!noOfSp AT $!field3 WRT $_cdPoints_WRT DIRECTION $!leave[2] HEIGHT 400 MM
    var !plane  CONSTRUCT PLANE $!arrive[2] THROUGH $!field3 DISTANCE 400 MM
    var !aPos   CONSTRUCT POSITION $!plane
    AID LINE NUMBER $!!noOfSp $!aPos WRT $_cdPoints_WRT TO $!field3 WRT $_cdPoints_WRT
```

### 1.4 约束复制 / 撤销重做

复制约束（`router\forms\rtrcopyconstraints.pmlfrm:196-201`）：
```pml
        ROUTER
        COPYCONSTRAINT $!fromBranch
        handle ( 2, 583 )
          !!messageFile.warning(162, 21, !!ce.name)
        endhandle
        EXIT
```

UNDO/REDO（`router\functions\undoroute.pmlfnc:25-48`，数据库级回退标准范式）：
```pml
   REDODB 1
   handle none
      UNDODB 1
   elsehandle any
      MARKDB CLEAR
      !!cdRouter.btnUndo.active = false
      !!cdRouter.btnRedo.active = false
   endhandle
   UNDODB 1
   handle any
      !!cdRouter.btnUndo.active = false
      return
   endhandle
   !!cdRouter.btnRedo.active = true
   !mark = MARKDB
```
`redoroute.pmlfnc:25-41`：`REDODB 1` + 二次探测 endmark（`!mark = MARKDB`，判断 `!mark[!mark.maxIndex()] eq 'endmark'`）+ `UNDODB 1` 回退探测。

### 1.5 建模模式与顺序命令

`componentcreation.pmlfrm`：
- 流向：`.flow()`（L7620-7626）`FORWARDS` / `BACKWARDS`
- 附加断点：`ATTABREAK ON branch` / `ATTABREAK SPKBRK branch`（L6284/L6540）
- 翻转组件组（`.flip()` L1891-1963）：
```pml
    REORDER $!<component> BEFORE $!<item>
    FLIP
    BY $!<offset>
    ROTATE THROUGH $!<sPosition> ABOUT $!<direction> BY $!<angle>
```
- 自动定向：`ORIENTATE`（L5487，create 后自动定向）
- 重排序（含元素锁错误码）：`REORDER $!atta before 1` / `reorder $!atta after $!component`（L8748-8754，`handle (2,18)`）

---

## 2. 连接命令全变体

### 2.1 CONNECT PH/PT 六种标准变体（唯一权威出处）

`pipecreation.pmlfrm` .reconnect（L3045-3099）：
```pml
  if(!end.upcase() eq 'HEAD') then
    if !!ce.hend.set() then
      if !!ce.hend.length().gt(0) then
        !hend = !!ce.hend
        if !hend.eq('TAIL') then
          CONNECT PH TO PT of HREF        $* ① 对端是尾端
        else
          CONNECT PH TO PH of HREF        $* ② 对端是头端
        endif
      else
        CONNECT PH TO HREF                $* ③ 无端名
      endif
    else
      CONNECT PH TO HREF
    endif
  else
    if !!ce.tend.set() then
      if !!ce.tend.length().gt(0) then
        !tend = !!ce.tend
        if !tend.eq('TAIL') then
          CONNECT PT TO PT of TREF        $* ④
        else
          CONNECT PT TO PH of TREF        $* ⑤
        endif
      else
        CONNECT PT TO TREF                $* ⑥
      endif
    else
      CONNECT PT TO TREF
    endif
  endif
```

**断开**（.disconnect，L3126-3131）：`HREF nulref` / `TREF nulref`。

### 2.2 CONN 简写 + 端属性回填（拆管场景）

`design\functions\splitpipe.pmlfnc:111-129`：
```pml
  $!newBranch
  CONN PH TO FIRST MEM                     $* CONN = CONNECT 简写，FIRST/LAST MEM 指向首/末组件
  tref $!tailRef
  tpos $!tailPos
  !hconn = !!ce.hcon
  $!branch
  CONN PT TO LAST MEM
  handle (2,113)
  endhandle
  !tconn = !!ce.tcon
  CONN PT TO PH OF $!newBranch
  tconn $!hconn                            $* 交叉回填连接类型
  $!newBranch
  hconn $!tconn
  same                                     $* SAME = 结束元素级命令块
```

### 2.3 CONNECT 失败降级 FCONNECT（带最小管长补偿）

`componentcreation.pmlfrm` .connect(DBREF)（L6788-6822）——**先试硬连，失败软连+偏移**：
```pml
  CONNECT
  handle ANY
    !minTubeLength  = !this.minTubeLength(!component)
    FCONN                                   $* 软连接（不断自动对齐）
    var !mode MODE
    if(!mode.upCase() eq 'FORWARDS') then
      !direction = !!ce.aDirection.opposite()
      error |Incompatible connection types. Item positioned with a $!minTubeLength spool length from the previous component|
    else
      !direction = !!ce.lDirection.opposite()
    endif
    MOVE $!<direction> distance $!<minTubeLength>
    !connected = false
  endhandle
```

批量连接策略（.connect(ARRAY, BOOLEAN) L6875-6908）：排序后首个 `CONNECT`，其余全部 `FCONNECT`（L6896-6902）。

围绕组件双向连接（.connect(DBREF, ARRAY) L6928-6981、.connectAdjacent L7015-7087）：`CONNECT`→`FCONNECT`→`createFirstConnected`→再 `CONNECT`；对侧镜像组件 `NEW $!<type>` + `CONNECT`，失败 `DELETE $!<type>`（L7168-7192）。

首个连接双向互试（.createFirstConnected L7314-7334）：新连旧 / 旧连新各试一遍。

最小管长补偿主流程（L5870-5880）：
```pml
  do !x from 1 to !sortedEleSeqAr.size()
    !!ce = !elements[!sortedEleSeqAr[!x]]
    if (!x.eq(1)) then
      FCONN
      MOVE $!<direction> distance $!<sMinimumTube>
    else
      CONNECT
    endif
  enddo
```

规格试探连接（.connectionChoices L6729-6754）——**用 CONNECT 成败反推可连接的规格元件**：
```pml
  !selections = SELECT SPEC $!<specification>
  do !selection values !selections
    !component.spref = !selection
    CONNECT
    handle ANY ... elsehandle NONE
      -- CONNECT 成功 = 该规格元件可用
  enddo
```

### 2.4 P 点连接（P1..P6）

无字面 `CONNECT P1 TO` 命令；走 PML 对象 `BRANCHCONNECTION.connect(!element, !connectionPoint)`（pipecreation.pmlfrm L3743）。connectionPoint 取 `HEAD`/`TAIL`/`P1..P6`；`'FIRST'`/`'LAST'` 表示本支管首/末组件（L3323-3335）。

多连接表 rtext 格式（L3659、L3679）：`!element.string() & '\P' & !pPoint.string() & '\' & bore & '\' & connected`。

P 点组件类型白名单（L4473）：`'NOZZ','TEE','OLET','CROS','SHU','PCOM','INST','VTWA','VFWA'`。

**自动连接触发**（.create L5754-5768）：起点/终点位于管段后方时 `!this.connect(!components, !flow)`；snapDist 吸合（L5792-5803）：`atlength leq snapDist` 时自动 `!this.connect(!newComponent)` + `connectAdjacent`。

### 2.5 电缆支路连接（MDR .NET 对象系，非管路）

`cblreversebranch.pmlfnc`：`!cwaymanager.disconnecthead(!bran)` / `disconnecttail` / `connectbranches(!bran, !tail)`；`cblconnectbranches` L37：`!cwayObject.pick('CONNECT')`。

---

## 3. 管件类型创建命令

### 3.1 通用创建模板（官方唯一写法：类型变量化）

`componentcreation.pmlfrm` .create（L5383-5392）：
```pml
  NEW $!<componentType> $!<createPosition>     $* createPosition 仅一种：分支首组件前 'BEFORE 1'
  handle ANY
    !!alert.warning('Error')
    return !created
  endhandle
  !this.newComponent = !!ce
  !newComponent       = !!ce
  !newComponent.spref = !specReference
```
相邻件创建：`NEW $!<adjacentType>`（L7267）、一律 `!newComponent.rlock = 2`（rlock=2 = Router 不可移动的自动件）。

### 3.2 组件类型注册表（构造器 L720-801，穷举）

| 类型字 | 组件对象 | 特殊属性 |
|---|---|---|
| BEND | COMPONENTBEND | 半径 = N*OD 或 Spec/Machine 自动（见下） |
| ELBO | COMPONENTELBOW | 角度 min/angle/max（越界回退 maxValue，L4988-5008） |
| REDU | COMPONENTREDUCER | 双口径；Arrive/Leave 配置 (1,2) 大进小出 / (2,1) 小进大出（L749-757） |
| COUP | COMPONENTDEFAULT | bore 齿轮 = checkBore(P2) |
| FLAN | COMPONENTFLANGE | 松套标志 flallow/loose（L8486-8505，compType match 'ALL'） |
| TEE | COMPONENTTEE | bore = P3；配置 (1,2) 直通、(1,3)、(3,2)（L775-777） |
| OLET | COMPONENTTEE | 同 TEE |
| VALV | COMPONENTVALVE | — |
| VTWA | COMPONENTVTWA | — |
| FILT | COMPONENTFILTER | — |
| INST | COMPONENTINSTRUMENT | — |
| PCOM | COMPONENTINSTRUMENT | — |

BEND 自动半径（.testBendRadius L8284-8325）：问题名含 `RAD` → Spec 半径；`catref.compType eq 'VAR'` → 弯管机 `.machineTest`，`collect all FMBDIM for $!macList`（L8444），匹配 `!a.dbref().od`/`wThickness`，半径 = `bradius * tubeOD`。

ELBO 角度反查（L4623-4635）：`owner.question.match('ANG')` → `maxans/answer`。

### 3.3 规格选取（SELECT / CHOICE 全变体）

创建后强制选择（L5423-5440）：
```pml
  var !choice CHOICE WITH $!<specReference>
  !selectString = !choice
  !selectString = !selectString.replace('PBOR 0','PBOR 0 ')   $* (PBOR 0..3 同)
  SELECT with $!<selectString>
```
相邻件选择：`SELECT WITH SPEC $!<specification>`（L7270、L7396，错误码 `handle (42,55)(42,501)`）；降级 `!selection = SELECT SPEC $!<specification>`（L7399）。

重选：`RESELECT WITH SPEC $!<component.spow>`（L7847）。

**口径问题构造**（.choices L4471-4490）：问题 = `'PBOR' & boreIndices[1]`（进料口径）、`'STYP'`、`'PBOR' & boreIndices[3]`（检查口径，三通 = PBOR3，判定 `!arrive + !leave + !check eq 6`，L5148-5160）；答案 = arriveBore/checkBore/sType；调用 `specifications.components(!type, !questions, !answers)`。

boreIndices 由组件对象 `.arriveLeave()` 返回（L4796-4816）；多口径判定（.checkComponents L8794-8817）：`!items[!n].ppbor[1].neq(!items[!n].ppbor[2])`，`gtype` 属 'TEE,OLET' 亦置 multiBore。

LOFF 离线标志：`var !s choice loff` → `!!ce.loff = !loff`（L8838-8848）。

规格属性套用（.setSpecAttributes L7786-7857）：
```pml
  var !choices choice number
  do !a indices !choices
    var !question Choice question $!a
    var !answer   Choice answer   $!a
    var !maxans   Choice maxans   $!a
    -- 匹配 ANGL/RADI/HEIG/SHOP 四种问题
    -- SHOP TRUE|SHOP → !component.shop = TRUE
    -- 数值取 maxans
  enddo
  RESELECT WITH SPEC ...
```
离线管：`!!ce.lstu = !this.lstu.selection().dbref()` 或 `select lstube`（L5448-5461、L7178-7184）；头管 `select hstu` / `select hstube`。

### 3.4 贯穿件/支吊架类 NEW（penetration 系）

`pipe1to1pene.pmlfnc`：L160 `NEW CMPF at $!intr wrt world`；L167 `NEW SBFI delp $!intr wrt world`；L183/L389 `NEW ATTA`；L190/L396 `SEL wi spec $_CDPENEDEF_ISPEC stype $!styp`；L594 `NEW FITT`。
`pipemultipene.pmlfnc`：L300 `NEW CMFI ZDIST THRO $!penposi[$!i] wrt World`；L304 `NEW SBFI`；L320-326 `NEW JLDATUM` / `NEW PLDATU POSL $!ppl` / `NEW FIXING POS ... wrt World`；L334/342 `NEW CMPF AT ... wrt /*`；L348 `NEW SBFI DELP $!spos`；L386 `NEW $!etyp`；L443 `CREF $!href`。

---

## 4. P&ID 导入：宏生成全流程（writeRecord 范式权威模板）

`router\functions\rtrpidprocess.pmlfnc`——签名（L48-50）：
```pml
define function !!rtrPIDprocess( !importFile is FILE, !logFile is FILE, !ask is BOOLEAN, !unNameTees is BOOLEAN, !keepFile is BOOLEAN, !replaced is ARRAY)
```

**流程**：
1. 层级检查（L56-68）：`NEW PIPE` 试探，`handle (2,500)(2,501)(2,502)(2,503)(2,504)` DAC 错误 → 失败即返回；成功 `DELETE PIPE` 撤销试探。
2. 宏文件生成（L104-121）：
```pml
  var !unique unique
  !macroFileName = !!evarSplit('PDMSWK')[1] + '/pid' + !unique + '.tmp'
  !macroFile.open('OVERWRITE')
  !macroFile.writeRecord( '!oldCe = !!ce' )     $* 首行固定保存 CE
```
3. Pass 1 多通归属去重：`!!rtrPIDPreprocess(!lines, !logFile)`（rtrpidpreprocess.pmlfnc L50-206）按 TREF 判定组件属主分支，非属主行剔除。
4. Pass 2 逐行解析 → writeRecord 生成宏。**PIPE 行**（L268-281）：
```pml
  !macroFile.writeRecord( |$!newOrOld PIPE $!details| )    $* OLD/NEW 前缀区分复用/新建
  !macroFile.writeRecord( |  handle ANY| )
  !macroFile.writeRecord( |    !!rtrWriteLog( !logFile, '$!string' ) | )
  !macroFile.writeRecord( |    !!rtrWriteLog( !logFile, !!error.text ) | )
  !macroFile.writeRecord( |  endhandle| )
```
   缺 PSPE 补 `' PSPE /' + !defaultPspec`（默认取 `!!cdPIPE.pspe`，L241-244）。
   **BRANCH 行**（L394-429）：剥离 START/HREF/TREF/PSPE 后重建；无 BORE 继承管路口径 `!macroFile.writeRecord( | $!newOrOld $!newLine HBORE $!pipeBore| )`（L405）；HREF 缺省置 `NO_HREF`、TREF 缺省置 `NO_TREF`（L355、L362）。
   **REDU 行**（L613-725）：剔除 PBORE0；`!selectText = ' SELECT WITH '`；扩径时前缀 `' FLIP'`（L721-723）；口径小于 REDU 口径用 `PBORE1` 否则 `PBORE2`。
   **TEE 行**（L731-814）：`TEE /T 50` 或 `TEE /T PBORE3 50`；`!selectText = ' SELECT WITH ' + !bores`。
   **其它组件**（L821-826）：`' SELECT WITH STYP ' + !attributes.part(1)`。
5. 组件通用宏输出（L835-883，错误码全家福）：
```pml
  !record = !newOrOldComponent + !type + ' ' + !componentName + !selectText
  !macroFile.writeRecord( !record )
  !macroFile.writeRecord( |  handle (42,66) (42,64) (42,52) (42,501) (42,502) | )
  !macroFile.writeRecord( |    var !type type| )
  !macroFile.writeRecord( |  elsehandle (42,54) (42,53)| )
  !macroFile.writeRecord( |  elsehandle ANY| )
  !macroFile.writeRecord( |  RLOCK $!rlock| )           $* 已存在组件 rloc eq 0 → rlock=0 允许 Router 重排
  if( !iSpec ne ||) then
    !macroFile.writeRecord( |  ISPEC $!iSpec| )
  endif
  if(!tSpec ne ||) then
    !macroFile.writeRecord( |  TSPEC $!tSpec| )
  endif
  if ( !isTee ) then
    !macroFile.writeRecord( |   ORIF TRUE| )            $* 三通立管标志
    !macroFile.writeRecord( |   POSF TRUE| )
    !isTee = false
  endif
```
6. HREF/TREF 回填宏（L914-960）：
```pml
  !macroFile.writeRecord( |$!branchName| )
  !macroFile.writeRecord( |!flag = 0| )
  if ( !hRef ne |NO_HREF| ) then
    !macroFile.writeRecord( |HREF $!hRef| )
    !macroFile.writeRecord( |handle ANY| )  ...  |  !flag = 1| ... |elsehandle none| ... |endhandle|
  endif
  if ( !tRef ne |NO_TREF|) then
    !macroFile.writeRecord( |TREF $!tRef| )
    !macroFile.writeRecord( |handle (73,3)| )   $* TREF 回填专属错误码
    ...
  endif
```
7. 挂入 Router 主表单（L970-975）：
```pml
  !macroFile.writeRecord( |if ( defined(!!cdRouter) ) then| )
  !macroFile.writeRecord( |  do !c indices !branches| )
  !macroFile.writeRecord( |    !!ce = !branches[!c]| )
  !macroFile.writeRecord( |    callr MADDCE| )          $* 外部宏：加入 Router
  !macroFile.writeRecord( |  enddo| )
  !macroFile.writeRecord( |endif| )
```
8. 三通去名（L983-991）：`unname` + `handle (41, 25)`。
9. 执行与清理（L997-1046）：
```pml
  !!ce = !oldCe
  !logFile.close()
  $M "$!macroFileName"               $* ★ $M 运行生成的宏文件
  !macroFile.deleteFile()            $* !keepFile 为 FALSE 时删除
```

**替换确认**（`rtrpidreplace.pmlfnc:34-76`）：`!branchName.dbRef()` 失败再试 `'/' & !branchName`；类型须 BRAN/PIPE；`!!alert.confirm(...messageString(162,50...)) eq 'NO'` 中止。
**表单入口**（`rtrimportpid.pmlfrm` .runImport L256-279）：4 开关 `_delete`/`_keepFile`/`_showLog`/`_unNameTees` → `!!rtrPIDProcess(...)`。
**日志**（`rtrwritelog.pmlfnc:37-127`）：BANNER 9 行（Import File/Date/User/Project/Database），`'ERROR:'`/`'WARNING:'` 前缀计数。

---

## 5. 属性设置命令

### 5.1 HBORE/TBORE

- 宏生成：`| $!newOrOld $!newLine HBORE $!pipeBore|`（rtrpidprocess L405）。
- 对象赋值（pipecreation .createBranch L1350-1353）：
```pml
  if(!this.pipe.bore.set()) then
    !this.branch.hBore = !this.pipe.bore
    !this.branch.tBore = !this.pipe.bore
  endif
```
- copyEnd（L1131-1141）：`!branch.tPos = !branch.hPos`、`!branch.tBore = !branch.hBore`、`!branch.tcon = !branch.hcon`。
- 端部口径（BRANCHCONNECTION .modifyBranchEnd L1076-1086）：`!this.endConnection.bore = !this.endBore(!end)` → `updateElement()`；bore 取值 `!this.hBore.selection('RTEXT').real().bore()`（L3857）。
- 弯管机口径判定：`.machineTest` L8394 `!this.branch.hbo.neq(!this.branch.tbo)`。

### 5.2 PSPE / ISPEC / TSPEC

- 宏：`PSPE /<spec>`（rtrpidprocess L242）、`ISPEC $!iSpec` / `TSPEC $!tSpec`（L864-870）。
- 工艺数据对象（pipecreation .updatePipeData L1174-1187）：
```pml
  !this.processData.specification(...)  .insulation(...)  .tracing(...)  .bore(...)
  .systemReference(...)  .temperature(...)  .pressure(...)  .sloRef(!dbElement)
  !this.processData.updateElement()
```
- 读取：`!this.pipe.pspec` / `!this.branch.pspec` / `!this.pipe.ispec` / `!this.pipe.tspec`（setupPipeData L1679-1720）。
- 校验：`chkhvacbranspec.pmlfnc`（`!element.pspec.unset()` → 'No Specification defined'；`dscode` → Detailing Spec）；`chkhvacbraninsu.pmlfnc`（`!element.iSpec.unset()` → uninsulated，`!element.inthi lt 1mm`）。

### 5.3 HREF / TREF / HCON / TCON

- 6 种 CONNECT 变体（§2.1）+ `HREF nulref` / `TREF nulref`。
- 读取：`!element.hConnect` / `!element.tConnect`（.connectionData L3542/L3572）；端名 `!element.hend` / `!element.tend`。
- 封口检查 `chkhvacbranconn.pmlfnc:40-52`：`!element.hcon eq 'CLOS' or 'OPEN'`。

### 5.4 HPOS / TPOS / HDIR / TDIR

- 位置输入：POSITIONCONTROL 控件（L4177-4182）：`!headPosition = !selectedBranch.hPos.wrt(world)`。
- EDG 拾取链：`.pickposH/.pickposT`（L4376-4419）→ `.hPos/.tPos`（L4315-4361）→ `.setHeadTailPosition`（L4455-4482）。
- 文本方向解析（.direction L3011-3029）：`object DIRECTION(!gadget.val)`，handle ANY → 'Invalid direction given.'。
- 读取伪属性：`hPosition/tPosition/hDirection/tDirection`（tagBranch L4003-4007）。

### 5.5 RLOCK / rloc

- 宏生成：`!macroFile.writeRecord( |  RLOCK $!rlock| )`（rtrpidprocess L862）；`!rlock = 0` 仅当已存在组件 `rloc eq 0`（L574-576），每组件输出后复位 `!rlock = 1`（L885）。
- 对象侧：`!newComponent.rlock = 2`（componentcreation L7170、L7269、L7392）。
- **未发现 `RUNLOCK` 字面命令**（该范围无）。

### 5.6 其它路由属性

- `ORIF TRUE` / `POSF TRUE`（三通立管标志，rtrpidprocess L873-874）。
- `BSTAT 0..10` 共 11 态（pipeSimpleAutoRoute L74/L106/L109；rtrstatussummary L94 `!br.dbRef().bstat`）。
- 平面属性：`PLPP`（CENT/ABOV/BELO）、`PLPM`（NEAR/WEIG）、`PLWW`（WW/WF/FF）、`PURP`（PRRP Travel / PREX EntryExit）、`FUNC`、`XLEN/YLEN/OBST 0`（rtrplanesofrack L99-128、L618-694）。

---

## 6. 管架平面（RPLA/RPLG）创建

`router\forms\rtrplanesofrack.pmlfrm` .commit（L618-694）：
```pml
      NEW RPLA
      POS $!position
      BY U $!zValue
      XLEN $!xLength
      YLEN $!yLength
      ORI $!ori
      PURP PRRP          $* Travel 平面（Entry/Exit 为 PURP PREX）
      YLEN $!yLengthEntry
      PLPM NEAR          /  PLPM $!plpm
      POS  $!position
      PLPP $!plpp
      PLWW $!plww
      OBST 0
```
加入 drawlist（L693-694）：`REM CE`、`ADD CE TRANSL 87 EDGES ON`。取消删除（L717）：`DELETE RPLG`。

对象版（`rtrrpla.pmlobj` .commit L150-162）：`POS`、`ORI`、`XLEN`、`YLEN`、`PURP`、`FUNC |$!this.function|`、`PLPP`、`PLPM`、`PLWW`。

`rtrcreaterack.pmlfrm`：
- `NEW RPLG` + `NAME $!<this.name.val>`（L1328-1332）
- AID 标注（L598-601）：`AID ARROW NUMBER ... DIRECTION $!xDir HEIGHT $!arrowLength PROPORTION 0.1`；`AID BOX NUMBER ... XLEN $!xLength YLEN $!yLength ZLEN 0 ORIENTATION $!ori`
- 钢结构内缩定位（L1607-1643，PIN 交点法）：
```pml
    PIN1 AT $!minEast DIR E
    PIN2 AT $!maxEast DIR W
    PIN1 BEHIND $!minEastItem
    PIN2 BEHIND $!maxEastItem
    !this.corner1Position.east = !!posOfPin(1).east
  PIN1 OFF
  PIN2 OFF
```
- 新增/删除平面（L2330-2341、L2445）：`1` `LAST` `NEW RPLA` → `!this.rplaData[!num].commit()`；`DELETE RPLA`。

---

## 7. 管段划分（SPOOL / WELD / 拆管）

### 7.1 拆管全流程（splitpipe.pmlfnc:35-131）

```pml
  !tailRef = !branch.tref
  !tailPos = !branch.tpos
  NEW PIPE COPY ATT OF $!pipe          $* 复制管道
  label /rename
  NAME /$!pipeName                     $* 新名 'name-Split(n)'
  handle (41,12)                       $* 重名 → '-Split(n+1)' golabel /rename
  NEW BRANCH COPY ATT OF $!branch
  NAME /$!branchName                   $* 新名 '/B<mCount+1>'
  handle ANY
  do !i from !newBranchMem.size() to 1 by -1
    INCLUDE $!newBranchMem[$!i]        $* 逆序搬移成员
  enddo
  $!newBranch
  CONN PH TO FIRST MEM
  tref $!tailRef
  tpos $!tailPos
  CONN PT TO LAST MEM
  handle (2,113)
  endhandle
  CONN PT TO PH OF $!newBranch
  tconn $!hconn
  $!newBranch
  hconn $!tconn
  same
```

### 7.2 SPOOL 对象体系

无 `NEW SPOOL` 命令——均为对象操作：
- `pipespoolcalcexpr.pmlfnc:27-112`：`object PIPESPOOLMANAGER()`；类型 `'PPIECE'`/`'PSPOOL'`；`!entry.spln` 名解析；`skip if (!entry.type inset ('WELD','ATTA'))`。
- `pipespoolgetweight.pmlfnc:27-31`：`!pipeSpoolManager.getBranchElements(!spool)`。
- `pipespooldim.pmlfnc:42-46`：`object PIPESPOOLDIMENSION()` → `createDimension(!viewRef)`。
- `pipemakespooldrwg.pmlfnc`：写宏 `%pdmsuser%\makespooldrwg.mac`（L45），批处理 `"...\MON" tty -macro="$!pdmsuser/makespooldrwg.mac"`（L86）——**TTY 无头批处理的官方范式**。
- `pipemakeoverlyingdrwg.pmlfnc:185-187`：`!spool.pstyp.upcase() eq 'SITE'/'FITT'`；iso 输出 `pipespool.met`。
- 数据一致性错误码全集（`pipevaliddatacheck.pmlfnc:72-255`）：24/25 SPREF、30/31 ARRIVE/LEAVE PPOINT、38/50 管长、40/86 BAD ARRIVE BORE、79 HBORE vs HSTUBE、83 HBORE vs TBORE、84 HCONN vs TCONN、163-165 连接兼容性。

### 7.3 焊缝（WELD）

**PMLLIB 范围内不存在 `NEW WELD` 命令**。WELD 仅作为类型被过滤（`skip if (!entry.type inset ('WELD','ATTA'))`，pipespoolcalcexpr L103）。焊缝建模属核心命令/其它模块。

### 7.4 UNDOABLE 事务包裹

- pipecreation：成员 `.undo is UNDOABLE`（L412）；`createPipe` L973-1002：
```pml
  !this.undo.description('Created pipe ...')
  !this.undo.add()
  NEW PIPE
  ...
  !this.undo.endUndoable()
```
- 越界拒绝时 `UNDODB` 回滚（componentcreation L5709、L5882）。
- 数据库级：`UNDODB 1` / `REDODB 1` / `MARKDB` / `MARKDB CLEAR`。

---

## 8. 范围外命令（明确结论，勿猜）

| 命令 | 结论 |
|---|---|
| `ROUTE ... ARRIVE/LEAVE/DIRECTION <dir>` 显式语法 | 未出现；约束以 `ICONS POINT n DIR/LEAV/FIXED` 查询形式存在 |
| `CONNECT P1/P2 TO ...` 字面命令 | 未出现；P 点连接走 `BRANCHCONNECTION.connect(element, 'P<n>')` 或宏 `SELECT WITH PBOREn` |
| `NEW ELBO/TEE/REDU/FLAN/VALV/INST` 字面命令 | 未硬编码；统一 `NEW $!<componentType>` 变量式 |
| `CALLR MADDCE`、`CALLR MRRDEF`、`CALLR MSETRLOC` | 外部宏，定义在 Router 主表单/Defaults 宏，不在 PMLLIB |
| `NEW WELD` | 不在 PMLLIB（属核心命令） |
| 电缆布线 | MDR .NET 对象 API（MDRROUTER/CABLEWAYMANAGER），与 Pipe Router 无关 |
