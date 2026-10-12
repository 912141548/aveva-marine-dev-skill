# Marine 设计模型操作命令编目(官方源码实证)

> 来源:4 个并行子 agent 深读 PMLLIB/PDMSUI 全树,提取全部嵌入 PML 代码中的 PDMS 命令行语句(非 PML2 表达式),2026-09-26 第 79 轮。
> 用途:编写涉及**模型/库/图纸/元素**实际操作的 PML 代码时查证命令写法——这是知识库此前最大的空白。

---

## 1. 创建元素(NEW <层级元素类型> [/name])

| 命令 | 频次 | 说明 |
|---|---|---|
| `NEW BRAN /name` | 211 | 创建支管 |
| `NEW STRU /name` | 108 | 创建结构元素 |
| `NEW PIPE /name` | 20 | 创建管路 |
| `NEW ZONE /name` | 9 | 创建区域 |
| `NEW EQUI /name` | 9 | 创建设备 |
| `NEW SITE /name` | 2 | 创建站点 |
| `NEW CABLE /name` | — | 创建电缆 |
| `NEW CWAY /name` | — | 创建电缆走线 |
| `NEW WELD /name` | — | 创建焊缝 |

### 官方范式:创建 → UNDOABLE → handle
```pml
!undoCreate = object UNDOABLE()
!undoCreate.description('Create Equipment')
!undoCreate.add()
NEW EQUI
handle any
  !!alert.error(!!error.text)
elsehandle none
  CHANGETYPE TO :$!<userType>
  NAME /$!<autoName>
  POS $!<pickedData.position>
!undoCreate.endUndoable()
```
出处:`design\forms\equcreatestd.pmlfrm:956-991`

### 复制式创建
```pml
NEW EQUI COPY $!<source>                        -- 复制设备
NEW EQUI COPY MEMBERS OF $!<source>              -- 复制含成员
NEW PIPE COPY ATT OF $!pipe                      -- 复制附带属性
NEW CABLE $!name COPY ATTRIBUTES OF $!src        -- 复制属性
NEW ZONE $!name COPY $!src RENAME $!src $!name   -- 复制+改名
```

## 2. 创建基本体

```pml
NEW BOX
   POSITION    $!box.position
   XLENGTH     $!xLen
   YLENGTH     $!yLen
   ZLENGTH     $!zLen
   ORI         $!orientation
END

NEW CYLI
   DIAMETER    $!dia
   HEIGHT      $!height
END

NEW NOZZ
NEW LOOP          (旋转体/拉伸体轮廓)
```
多行参数块以 `END` 终止。临时建模:创建→读取→删除(`DELETE BOX`)。

## 3. 修改属性(三种写法)

### A. 命令式属性字(NEW 后接)
```pml
NEW EQUI
NAME $!<name>
DESC |$!<desc>|
FUNC |$!<func>|
INSC |$!<spec>|
```

### B. 材料引用命令
```pml
matref /S235JRG2
matref /CARBON/STEEL
:MDSMatRef /CARBON/STEEL    (UDA 冒号语法)
```

### C. PML2 属性赋值(最常见)
```pml
!!ce.hBore = !this.bore
!!ce.spref = !tabItem
!!ce.desc = !this.desc.val
!entry.$!attrName = !result              (动态属性名)
!db.attribute(!attName) = !attVal        (反射式)
```

### D. 管道专用命令(由 rtrpidprocess 生成)
```pml
NEW PIPE /XXX PSPE /SPEC
HBORE $!bore
ISPEC $!iSpec / TSPEC $!tSpec
HREF $!hRef / TREF $!tRef
RLOCK $!rlock
```

## 4. 元素导航

```pml
!!ce = !siteName.dbref()          -- PML2 导航(最常见)
/FRA/TEMPLATES                     -- 裸名路径命令
last member                        -- 跳到最后成员
last stru                          -- 跳到最后 STRU
FORWARDS                           -- 正向模式
!!ce = !!ce.owner                  -- 上级
!!ce = !!ce.members.last()         -- 最后成员
prev / nex                         -- 前后移动命令
```

## 5. 删除

```pml
DELETE STRU                        -- 删除当前 STRU
delete bran                        -- 删除当前 BRAN
DELETE BOX                         -- 删除当前 BOX(临时建模清理)
DELETE $!!ce.type                  -- 按 CE 类型拼命令
DELETE LOOP MEM                    -- 删除轮廓成员
DELETE SPINE MEMBERS 4 TO $!max    -- 删除指定范围成员
```

## 6. 连接操作

```pml
CONNECT PH TO HREF                 -- 头端连接
CONNECT PT TO TREF                 -- 尾端连接
CONNECT P1 OF $!nozzle             -- 连接 Ppoint
CONNECT P$!from OF $!a TO P$!to OF $!b    -- 两元件 Ppoint 互连
CONNECT to next                    -- 连接到下一元件
CONNECT                            -- 自动连接(创建后)
```

## 7. 定位操作

```pml
POS $!pos                           -- 设位置
POS PA AT PT OF BRAN                -- Ppoint A 定位到支管 Ppoint T
POS X $!x Y $!y                     -- 单轴偏移
ORI Z IS $!zDir AND X IS $!xDir     -- 轴向定向
ORIENTATION $!ori                   -- 方位对象赋值
!pos = E $!x N $!y U $!z wrt world  -- ENU 坐标读入
```

## 8. 颜色/图层/显示

```pml
ADD $!elem COLOUR $!col TRANSL 50 EDGES OFF    -- 加入 drawlist 带色半透明
REMOVE ALL                                      -- 清空 drawlist
REMOVE CE                                       -- 移除 CE
COLOUR CE $!col                                 -- 着色 CE
ENHANCE $!item COLOUR $!col                    -- 高亮
UNENHANCE $!item                               -- 取消高亮
```

## 9. 工作区操作

```pml
savework                       -- 提交
getwork                        -- 回滚
undodb 1                       -- 撤销最近 DB 提交
```

## 10. 成员/层次操作

```pml
NEW FIXING AFTER LAST MEMBER    -- 追加到末尾
reorder $!a before $!b          -- 重排(前)
reorder $!a after $!b           -- 重排(后)
new stru $!name copy $!src rename $!src $!name   -- 复制+改名
```

---

## Draft 出图命令

### 图纸创建
```pml
NEW DRWG /name                   -- 创建图纸
  DATE '5 Apr 2013'
  TITL 'Detail Plot View'
NEW SHEET /name/S1
  SIZE 120mm 60mm
  TITL 'Piping Drawing'
  POSFOR ENU
NEW LAYER /name/S1/V1/USER_dims
  PURP DIMA
NEW LIBY /name/LIBY
NEW DLLB /name/DLLB
NEW IDLIST /name/IDLI
```

### 视图创建
```pml
NEW VIEW /name/S1/V1
DIR D                             -- 方向
VSCA 0.05                        -- 比例
VTYP Universal HLine             -- 视图类型(隐藏线)
SIZE 60mm 60mm                   -- 尺寸
XYPS X 30mm Y 30mm               -- 位置
LFRA true                         -- 框架
DESADD CE COLOUR RED             -- 添加 3D 设计元素
```

### 标注创建
```pml
NEW LDIM DTANG $!ang PTANG $!pang
  DIR $!dir
  LCHAIN TRUE
  FROM P1 OF $!first
  TO P2 OF $!second

NEW ADIM SENSE CLOCKWISE          -- 角度标注

NEW NOTE                          -- 注释
NEW VNOTE                         -- 竖排注释
  JUST Left
  ALIGN Bbody
  FONT 1
  CHEI 3mm
  TXCOLO 1

NEW GLAB BTEX |text| ON $!ref    -- 全局标签
NEW SLAB ON $!ref ATEX |$!tag|   -- SLAB 标签(带 TMRF 模板引用)
  TMRF $!symbol XYPO $!offset

NEW TEXP CHEI $!h BTEX '$!text' ADEG $!angle JUST C ALIG TB
```

### 图形元素创建
```pml
NEW STRA DEF @                    -- 直线(两点)
NEW ARC DEF @                     -- 弧(三点)
NEW CIRC DEF @                    -- 圆(圆心+半径)
NEW OUTL                          -- 轮廓
NEW VRTX BULGE 0.85               -- 顶点(带鼓度)
SPAN TO CLOSE                     -- 封闭轮廓
NEW RECT                          -- 矩形
```

### 出图输出
```pml
PLOT SHEET FILE PDF "$!file" 'options' $!opts OVERWRITE
PLOT SHEET FILE METAFILE "$!file" '$!opts'
PLOT SHEET FILE SVG "$!file" '$!opts'
PLOT SHEET FILE PRINT '$!opts'
LIEXEC /Draft_DXF_LI 'DXFOUT' CONFIGDATA '$!config' OUTPUTFILENAME '$!file'
```

### 图纸修改
```pml
DELETE SHEE MEM                   -- 删除图纸及成员
by x 60mm                         -- 偏移
ADEG $!angle                      -- 旋转
MIRROR ABOUT X $!x1 Y $!y1 AND X $!x2 Y $!y2    -- 镜像
NEW $!type COPY PREV BY X $!dx Y $!dy    -- 多重复制
REFRESH                           -- 刷新
```

---

## 规格库操作

```pml
SPREF $!<specReference>           -- 设置规格引用(命令式)
SPREF NULREF                      -- 清空
!!ce.spref = !spco                -- PML2 直写
GTYPE $!<gType>                   -- 设置元素类型

-- 规格选件
!specifications = object SPECIFICATIONS(!spec.dbref())
!specifications.loadComponents()
!specifications.subTypes(!type, 1, !boreObject)
!components = !specifications.components(!type, !questions, !answers)

-- 型材截面
NEW $!type                         -- SCTN/GENSEC
POSSTART $!start POSEND $!end      -- 起终点

-- 规则
RULE SET POSE (expr)               -- 设置动态规则
RULE EXECUTE SPRE ON ALL FOR CE    -- 执行规则
RULE REXECUTE                      -- 重执行
CHECKRULES CE                      -- 检查规则
!errors = !element.nruleerrors     -- 错误计数
```

---

## UDA 操作

```pml
:MDSMatRef /CARBON/STEEL            -- 冒号语法设 UDA
!!ce.:mdsnudgedist = value          -- PML2 直写 UDA
!this.component.udalis              -- UDA 名单
!this.component.$!<name>            -- 动态读
!destination.$!<name> = value       -- 动态写
!$!<name> default                   -- 命令式复位
!$!<name> unset                     -- 命令式清除
```
