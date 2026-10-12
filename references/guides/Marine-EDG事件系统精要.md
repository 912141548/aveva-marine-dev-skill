# Marine EDG 事件系统精要(edgCntrl / edgPacket / Pick 全参考)

> 来源:RefMan §3(Event Driven Graphics,L10053-12600)逐节精读,2026-09-26 第 43 轮。
> 定位:3D 交互拾取工具的完整参考——表单按钮 → 建事件包 → 用户拾取 → 回调处理 → 清理,全生命周期。
> 基础用法见《AVEVA-Marine-PML开发技能.md》§3.7;本文件是深水区。
> **实战模板**:见《PML语料/audit_test/mypicker.pmlfrm》(第 50 轮,通过 16 规则审计 0 违规)。

---

## 1. 体系四组件

| 组件 | 全局实例 | 职责 |
|---|---|---|
| **edgCntrl** | `!!edgCntrl`(系统唯一) | 事件栈管理:当前激活事件 + 堆栈事件 + 已注册图形视图 |
| **edgPacket** | 用户创建 | 事件完整定义(管理数据+动作+拾取序列+输入输出) |
| **edgPickPacket** | packet 内 | 拾取序列定义(picks 数组,每项一个 pick 类型) |
| **edgPickData / edgPositionData** | 系统返回 | 拾取结果(只读对象,成员有名) |

**堆栈语义**:add 时激活事件压栈、等价包(同 description 同 priority)被替换提示;remove 时执行 .close、弹栈恢复上一事件。表单随包自动显隐(栈顶激活、栈底灰显)。

## 2. edgCntrl 公开接口

| 方法 | 用途 |
|---|---|
| `.add(!packet)` | 入栈激活;失败回 FALSE,原因在 `!!error.text`(**必须检查**) |
| `.remove('描述')` | 按 description 移除;不存在不报错 |
| `.setPrompt('主提示')` / `.setPrompt('主','次')` | 改当前激活事件提示(递归拾取换提示) |
| `.setStackPrompt('描述','主提示')` | 改栈内事件的提示 |
| `.viewStack()` / `.viewStack(n)` | 命令行查看栈(仅调试用) |

**add 流程**:移除等价包 → 上一包表单灰显 → 激活包压栈 → 应用拾取过滤器 → 注册视图挂事件处理器。
**remove 流程**:执行 .close → 移除关联表单 → 恢复栈顶事件。
**铁律**:`.add()` 之后的代码**不得再改包定义**(改的是本地副本,不生效)。

## 3. edgPacket 全成员表

### 管理成员
| 成员 | 类型 | 说明 |
|---|---|---|
| `.description` | STRING | **同工具多包共用同一描述**(remove 按它删) |
| `.priority` | REAL | 0=最高;同描述同级包入栈时提示替换;**入栈只移除同级,不动低级** |
| `.remove` | BOOLEAN | TRUE=拾取序列完成后自动出栈;FALSE=重装(不跑 .initialisation) |
| `.form` | FORM | 关联表单(必须先 loadform 再赋);系统自动显隐 |

### 动作成员(全部是回调字符串;**禁用旧式宏**)
| 成员 | 触发时机 | !this 指向 | 典型写法 |
|---|---|---|---|
| `.initialisation` | 包初次入栈(重装不跑) | packet | `'!!form.init(!this.input[1])'` |
| `.action` | 拾取序列全部完成 | packet | `'!!form.process(!this.return[1])'` |
| `.close` | 出栈前(成功/被替换/ESC) | packet | `'!!form.cleanup()'`(有 .form 时**不要**自己 hide) |
| `.continue` | 出栈后(**ESC 时不跑**) | 外部 | `'!!form.afterEvent()'` |
| `.escape` | 仅 ESC 出栈时 | 外部 | `'!!form.onEsc()'` |

### 数据成员
| 成员 | 类型 | 说明 |
|---|---|---|
| `.input` | ARRAY | 包内局部数据(按引用传递;动作内用 `!this.input[n]`) |
| `.return` | ARRAY | 拾取结果(动作内用 `!this.return[1]`;也按引用) |
| `.pickPacket` | EDGPICKPACKET | 拾取序列定义 |

## 4. 拾取序列方法(11 种)

| 方法 | 返回 | .remove 缺省 | priority |
|---|---|---|---|
| `.navigate()` | 无 | TRUE | 10 |
| `.elementPick(prompt)` | return[1] = edgPickData | FALSE | 0 |
| `.plinePick(prompt)` | edgPickData | FALSE | 0 |
| `.anyPick(prompt)` | edgPickData(元素/pline/ppoint/aid) | FALSE | 0 |
| `.aidPick(prompt)` | edgPickData(图形辅助元素) | FALSE | 0 |
| `.definePosition(prompt)` | return[1] = edgPositionData | FALSE | 0 |
| `.defineCircle(option)` | return[1] = ARC 对象 | TRUE | 0 |
| `.definePoint(option)` | — | — | — |
| `.defineLine(option)` | — | — | — |
| `.definePlane(option)` | — | — | — |
| `.defineMeasure(option)` | — | — | — |

**defineCircle 13 种 option**(完整清单):3pnt / diameter3D / radius3D / fixedRadius3D / fixedDiameter3D / diameter2D / radius2D / fixedRadius2D / fixedDiameter2D / fillet / tanTan / pntTan / fixedRadiusPntTan / fixedRadiusPntPnt / derive / tan3Lines——每种定义拾取次数与几何推导方式(RefMan p241-243)。

## 5. edgPickData 成员表(动作回调里读这些)

### edgPickPacket 拾取序列方法全表(§3.11.1,50+ 方法)

**基础拾取**(返回 edgPickData):
`.stdGphWindow(prompt)`(框选窗口)/ `.stdScreen(prompt)`(屏幕点,返回 POINTVECTOR)/ `.stdView(prompt)`(视图,返回 GADGET)/ `.stdElement(prompt)` / `.stdAny(prompt)` / `.stdPpoint(prompt)` / `.stdPline(prompt)` / `.stdAid(prompt)` / `.stdGraphic(prompt)`

**定位拾取**(返回 edgPositionData):
`.stdPosition(prompt)` / `.positionLinear(prompt)`(线性元素上取点)/ `.positionArc(prompt)`(弧上取点)/ `.positionPlane(prompt)`(面上取点)

**圆定义 16 种**:circle3pnts / circleDia3d / circleRad3D / circleFixRad3D / circleFixDia3D / circleDia2D / circleRad2D / circleFixRad2D / circleFixDia2D / circleFillet / circleTan3Lines / circleTanTan / circlePntTan / circleFRadPntTan / circleFRadPntPnt / circleDerive

**点/线/面定义**:
`.pointPnt()`(3D 工作点)/ `.linePntPnt()`(两点线)/ `.lineAngle(any)`(角度偏移线)/ `.lineDerive()`(元素派生线)/ `.linePntTan()` / `.lineTanTan()`(双弧公切线)/ `.lineBisect()`(角平分线)/ `.lineTwoPlanes()`(两面交线)/ `.lineShortest()`(最短线段)/ `.plane3pnts()` / `.plane2pnts(pos)` / `.planeDerive()`

**测量**:`.measureDistance()` / `.measureAngle()` / `.measureLineAngle()`

**数据库元素解释**(edgPickType 层,返回 edgPositionData 但 .position 不填充):
`dbLine(STRING)` / `dbCircle(STRING)` / `dbPlane(STRING)`——把拾取的 DB 元素转换为线/弧/面

### edgPick 过滤器(§3.13)

通过 `pick.input[n]` 传过滤规则 + `.modifiable = false`:
```pml
!packet.pickPacket.picks[1].pick.input[3] = 'TYPE eq |TUBING|'    -- 元素类型过滤
!packet.pickPacket.picks[1].pick.input[5] = 'GRADIENT eq 100000'  -- 属性过滤
!packet.pickPacket.picks[1].pick.modifiable = false
```
input 数组各下标含义(各对应一种拾取项类型)——详见 RefMan p282-285。
**限制**:目前只能通过 pick 对象的 input 成员设过滤,无其他入口(§3.13.5)。

### 通用拾取成员
| 成员 | 类型 | 说明 |
|---|---|---|
| `.type` | STRING | 拾取类型:ELEMENT / PLINE / PPOINT / AID 等 |
| `.item` | DBREF | **拾到的 DB 元素**(最常用) |
| `.point` | REAL | Ppoint/辅助元素编号 |
| `.pline` | STRING | 结构 pline 名 |
| `.tubing` | STRING | 管道 HEAD/LEAVE |
| `.aidType` | STRING | 辅助元素类型(LINE/CYLINDER…) |
| `.pickLine` | POINTVECTOR | 拾取视线向量 |

### 图形实体拾取成员(边/面/顶点)
| 成员 | 类型 | 说明 |
|---|---|---|
| `.vertexCount / .vertices` | REAL / ARRAY | 顶点数与位置 |
| `.lineCount / .lines` | REAL / ARRAY | 边数与成对位置 |
| `.facetCount / .facets` | REAL / ARRAY | 面数与角点 |

### 方法
`.positionData()` — 转换为 edgPositionData(含派生位置)。

### 拾取过滤(进阶)

**input 数组 6 个下标的含义**(RefMan §3.13.1):
| 下标 | 过滤对象 | 说明 |
|---|---|---|
| [1] | Pline | 结构元素 pline 过滤 |
| [2] | Ppoint | Ppoint 过滤 |
| [3] | Element | 元素过滤 |
| [4] | Design Aid | 设计辅助元素过滤 |
| [5] | Tubing | 管道过滤 |
| [6] | Graphical Entity | VERTEX/EDGE/FACET 图形实体过滤 |

**规则组合矩阵**(§3.13.2,哪些下标可同时使用):
- Element + Pline/Ppoint/Aid/Tubing/Graphics 可组合
- Graphics 可与全部组合
- Aid 只能独立使用
- 规则在光标经过时实时求值

**关键注意**:
- Element 规则**先于** Pline/Ppoint 规则求值——如果 Element 规则排除了含 pline 的元素,用户将无法选中任何 pline
- **`.modifiable = false` 必须设置**(否则标准过滤器覆盖自定义规则)
- 规则表达式必须是 STRING 类型

**官方示例**(§3.13.4):
```pml
-- 只允许 EQUI/SUBE 下的元素被拾取
!rule = 'TYPE of OWNER inset (|EQUI|,|SUBE|)'
!packet.pickPacket.picks[1].pick.input[3] = !rule
!packet.pickPacket.picks[1].pick.modifiable = false

-- 只允许 SCTN/GENSEC 的 BEAM 型材 pline(翼板/腹板)被拾取
!pline = 'PKEY inset (|TO S|,|BOS|,|NAR|,|NAL|)'
!element = 'TYPE of OWNER inset (|SCTN|,|GENSEC|) and GTYPE eq |BEAM|'
!packet.pickPacket.picks[1].pick.input[1] = !pline
!packet.pickPacket.picks[1].pick.input[3] = !element
!packet.pickPacket.picks[1].pick.modifiable = false
```

**限制**(§3.13.5):无其他入口设置过滤规则,必须通过 pick 对象的完整变量链。

## 6. 完整生命周期模板(递归多拾取 + 动态提示)

```pml
define method .startPicks()
  !packet = object EDGPACKET()
  !packet.description = 'My Multi Pick'
  !packet.elementPick('Pick first element <esc> to finish')
  !packet.action = '!!myform.onPick(!this.return[1])'
  !packet.close   = '!!myform.picksDone()'
  !!edgCntrl.add(!packet)
endmethod

define method .onPick(!pickData is ANY)
  !elem = !pickData.item
  -- 处理第一个拾取…
  -- 递归重装(换提示):
  !!edgCntrl.setPrompt('Pick next element <esc> to finish')
  !!edgCntrl.add(!packet)      -- .remove=false 时重装,不跑 initialisation
endmethod
```

## 7. 官方示例模式库(§3.10.2 + §3.11.2/3)

### 模式 A:单次拾取+导航回原(自包含,无表单)
```pml
!packet.elementPick('Pick Element')
!packet.initialisation = '!this.input[1] = !!ce'     -- 记住原 CE
!packet.action = '!!ce = !this.return[1].item'       -- 导航到拾取元素
!packet.close = '!!ce = !this.input[1]'              -- ESC 恢复原 CE
```

### 模式 B:重复拾取+input 收集
```pml
!packet.elementPick('Pick Element <esc> to finish')
!packet.action = '!this.input.append(!this.return[1].item)'   -- input 数组收集
!packet.close = 'q var !this.input'                            -- ESC 时展示
```

### 模式 C:重复拾取+全局存储+高亮切换
```pml
!packet.initialisation = '!!xxxGlobalStore = ARRAY()'
!packet.action = '!!xxxStoreElement(!this.return[1].item)'
!packet.close = '!!xxxTagElements(|NAME|)'
```
StoreElement 函数:findFirst 判重 → 已有则 remove+UNENHANCE / 新则 append+ENHANCE COLOUR RED。

### 模式 D:关联表单(definePosition)
```pml
!packet.definePosition('Pick Position')
!packet.action = '!!xxxForm.position(!this.return[1].position)'
if (undefined(!!xxxForm)) then pml reload form !!xxxForm endif
!packet.form = !!xxxForm          -- 表单按引用传递,必须先 build
!packet.close = '!!xxxForm.tidy()'
```
表单关闭三条路径:①按钮 OK/Cancel/Dismiss → **必须**调 `!!edgCntrl.remove(描述)`;②表单左上角 Close → 同①;③画布 ESC → **只**调 tidy(),**不得**调 remove(会出问题)。

### 模式 E:自定义多拾取序列(EDGPICKPACKET 手动定义)
```pml
define method .elementMove() is EDGPICKPACKET
  !pickPacket = object EDGPICKPACKET()
  !pickPacket.key = 'element-position'
  !pickPacket.prompt = 'Move element'
  !pickPacket.picks[1] = object EDGPICKTYPE()
  !pickPacket.picks[1].stdElement('(Pick element to move)')
  !pickPacket.picks[2] = object EDGPICKTYPE()
  !pickPacket.picks[2].stdPosition('(New position)')
  return !pickPacket
endmethod
-- 使用:
!packet.pickPacket = !this.elementMove()
!!edgCntrl.add(!packet)
```

### 模式 F:等价旧 VAR PICK 命令(PML1 迁移)
| 旧命令 | EDG 等价 |
|---|---|
| `VAR !x PICK` | elementPick + action + add |
| `VAR !x PICK PLINE` | plinePick + action + add |
| `VAR !x PICK PPOINT` | 依此类推(改变拾取方法即可) |

## 8. 规则与禁令

1. 只用公开接口;.add 后不改包定义;动作串禁旧式宏。
2. `.continue` 与 `.escape` 互补(ESC 只触发后者);有 .form 时 close 不 hide。
3. priority 入栈只清同级;不同 description 的包可共存(堆栈)。
4. input/return 按引用——动作里改变量即改包数据。
5. 拾取过滤只能经 pickPacket.picks[n].pick.input 设置(3.13.5:无其他入口)。
