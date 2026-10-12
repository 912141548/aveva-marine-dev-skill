# AVEVA Marine 元素操作命令大全（穷举版·第一卷）

> 来源：4 个并行子 agent 深读 PMLLIB 全树全部源文件（6075 文件/206 万行），逐行提取嵌入 PML 代码中的 PDMS 数据库操作命令。
> 日期：2026-09-26
> 用法：写涉及模型/库/图纸/元素实际增删改查操作的 PML 代码时查证命令写法。

---

## 第一部分：元素创建命令（NEW 系列）

### 1.1 层次元素

#### SITE（站点）
```pml
new site /MDS/PARS
  handle NONE
  elsehandle ANY
  endhandle
```
出处：`mds\design\objects\MdsTest.pmlobj:169`

#### ZONE（区域）
```pml
new zone /MDS/PARS/$!Standard
  endhandle
```
```pml
NEW ZONE $!copyFirst COPY $!first RENAME $!first $!copyFirst
handle ANY
  NEW ZONE $!copyFirst COPY $!first
endhandle
```
出处：`design\forms\cblcwaycopy.pmlfrm:572`

#### DEPT（部门，图纸域）
```pml
new DEPT $!this.deptName
handle ANY
endhandle
```
出处：`design\objects\pipespooldwg.pmlobj:275`

#### REGI（注册表，图纸域）
```pml
new REGI $!this.regiName
handle ANY
endhandle
```

#### EQUI（设备）— 4 种变体

**变体 1：裸创建 + CHANGETYPE + 自动命名**
```pml
NEW EQUI
handle any
  !!alert.error(!!error.text)
elsehandle none
  CHANGETYPE TO :$!<userType>
  NAME /$!<autoName>
  POS $!<pickedData.position>
endhandle
```

**变体 2：全套属性命令**
```pml
NEW EQUI
NAME $!<this.name>
DESC |$!<this.description>|
FUNC |$!<this.function>|
DSCO |$!<this.code>|
INSC |$!<this.inSpec>|
PTSP |$!<this.paint>|
```

**变体 3：COPY 复制**
```pml
NEW EQUI COPY $!<source>
NEW EQUI COPY MEMBERS OF $!<source>
```

**变体 4：重名自动编号循环**
```pml
NEW EQUI
do !index from 1 to 1000
  !!ce.name = !fileName + !indexString
  handle none
    break
  elsehandle any
    !indexString = !index.string()
  endhandle
enddo
```

#### PIPE（管路）— 4 种变体

**变体 1：裸创建**
```pml
NEW PIPE
handle ANY
  !error = !!error.text.after(')').trim()
endhandle
!this.pipe = !!ce
```

**变体 2：COPY ATT OF**
```pml
NEW PIPE COPY ATT OF $!pipe
ispec $!insulation
NAME /$!pipeName
handle (41,12)
  !pipeName = !pipeName.before('-Split(')
  !newNumber = !newNumber + 1
  !pipeName = !pipeName + '-Split($!newNumber)'
endhandle
```

**变体 3：copy prev + 搬移成员**
```pml
new pipe copy prev
delete pipe mem
incl $!newBran
```

**变体 4：DAC 错误组**
```pml
NEW PIPE
handle (2,500) (2,501) (2,502) (2,503) (2,504)
  !!alert.error(!!error.text)
  return
elsehandle ANY
  !!messageFile.error(162, 48)
  return
elsehandle none
  DELETE PIPE
endhandle
```

#### BRAN（分支）— 11 种变体

1. 裸创建 + 属性赋值
2. NEW BRANCH + name
3. NEW BRAN + flowdir OFF
4. NEW BRAN + COPY LIKE（两行式）
5. NEW BRANCH COPY ATT OF + 成员搬移 + 连接
6. new bran copy like（条件式）
7. NEW BRAN COPY + DELETE BRAN MEM + 端点重设
8. new bran copy prev + conn
9. NEW BRAN COPY PREV + rename + flowdir
10. new bran + UDA + 连接命令
11. copy 后端点/方向命令

**分支属性命令全集**：`hBore/tBore`、`hpos/tpos`、`hdir/tdir`、`href/tref`、`hcon/tcon`、`hstu/tstu`、`flowdir OFF`、`CONN PH/PT`

#### STRU（结构元素）
```pml
NEW STRU /$!StruName
!Support.Stru = !!CE
:MDSSuppType |$!Support.Type|
```

#### GENSEC（通用截面）— 完整属性链
```pml
NEW GENSEC $!startPos
SPRE $!selection
GTYP $!genericType
NEW SPINE
NEW POINSP $!startPos
NEW POINSP POLAR $!railDir DIST $!newLeng
GENSEC
POSS $!pose
POSE $!poss
```

#### SCTN（结构型材）— 8 种变体

1. 裸创建 + 全套线型属性
2. 裸创建 + PML 属性直赋
3. copy prev（28 处）
4. copy 指定源 + RENAME
5. copy 绝对路径源
6. copy attrib of prev
7. copy prev 链式阵列
8. 复制改名换属主

#### PANEL / WALL / PLAT
```pml
NEW PANEL
NEW PLOOP
!!ce.height = !thickness
!!ce.sJustification = 'UBOT'
```
```pml
NEW PLAT SEL SPREF WITH STYP '$!selection' SPEC /MDS
```

#### 管件（通过规格选取）
```pml
NEW $!<componentType> $!<createPosition>
handle ANY
endhandle
!newComponent.spref = !specReference
var !choice CHOICE WITH $!<specReference>
SELECT WITH $!<selectString>
```

#### 基本体

**BOX — 4 种参数写法**
```pml
NEW BOX
POSITION $!box.position
XLENGTH $!x
YLENGTH $!y
ZLENGTH $!z
ORI $!orientation
```

**CYLI（圆柱）**
```pml
NEW CYLI
POSITION $!pos
DIAMETER $!dia
HEIGHT $!h
ORI $!ori
END
```

**NOZZ（管嘴）**
```pml
NEW NOZZ
!!ce.catref = !specRef
!!ce.height = !height
!!ce.pos = !position
```

**EXTR/LOOP/VERT（负体开孔三件套）**
```pml
NEW TMPL
NEW EXTR
NEW LOOP
NEW VERT AT X -100mm Y 100mm
NEW VERT AT X 100mm Y 100mm
NEW VERT AT X 100mm Y -100mm
NEW VERT AT X -100mm Y -100mm
EXTR
```

**NPYR（负四棱锥）— 完整参数**
```pml
NEW NPYR
POS $!posString
HEIGHT $!height
ORI P0 IS $!oriString AND X IS D
XBOTTOM $!depth
YBOTTOM $!width
YTOP 0
XTOP 0
XOFF $!value
```

**其他派生体**：NREV（圆锥负体）/ NXTR（函数负体）/ PLOO（板体）/ SPINE / POINSP / POINTR / PAVE

#### 电缆类
```pml
NEW CABLE /name COPY ATTRIBUTES OF $!src
NEW CWAY
NEW CWBRAN
NEW CTRAY
NEW RPATH
```

#### HVAC
```pml
NEW HVAC $!name
NEW BRAN $!name/B1
COPY LIKE $!fromBranch
```

---

## 第二部分：属性操作

### 属性写入

**命令式属性字**
```pml
NAME $!name
DESC |$!desc|
FUNC |$!func|
PURP $!purpose
MATREF /material/path
```

**PML2 直写**
```pml
!!ce.desc = !value
!!ce.hbore = 200
!!ce.spref = !spco
!entry.$!attrName = !result
!db.attribute(!attName) = !attVal
```

**UDA 冒号语法**
```pml
:MDSMatRef /CARBON/STEEL
!!ce.:MDSMatRef = !value
!this.component.$!<name> = value
!$!<name> default
!$!<name> unset
```

### 属性读取

```pml
!bore = !spref.ppbore[n]
!value = !component.$!<udaName>
!val = !element.attribute(!attName)[!index]
!designItem.evaluate(object BLOCK(!expression))
```

### 属性校验

```pml
!!dbRefUpdate(!element)
!element.attributes().findFirst('Spref')
!element.pspec.unset()
MODERR $!<attribute> of $!<component>
```

---

## 第三部分：元素导航

```pml
!!ce = !siteName.dbref()         -- DBREF 转 CE
!!ce = !!ce.owner                 -- 上级
!!ce = !!ce.members[1]            -- 第一个成员
!!ce = !!ce.members.last()        -- 最后成员
!next = !!ce.owner.members[!!ce.sequence + 1]
!!ce = !!ce.href                  -- 引用属性跳转
!!ce = !!ce.dtRef                 -- 跨引用跳转
/FRA/TEMPLATES                    -- 裸名路径命令
last member / last stru           -- 类型名导航
prev / nex                        -- 前后移动
!x = !!dtbGetOwnerType(!!ce, 'TMAR')   -- 向上找类型
```

---

## 第四部分：删除操作

```pml
DELETE STRU                       -- 删除当前 STRU
DELETE BOX                        -- 删除当前 BOX
DELETE $!!ce.type                 -- 按 CE 类型拼命令
DELETE LOOP MEM                   -- 删除轮廓成员
DELETE SPINE MEMBERS 4 TO $!max   -- 范围删除
DELETE SHEE MEM                   -- 删除图纸及成员
DELETE LAYE MEM                   -- 删除层及成员
```

---

## 第五部分：连接操作

```pml
CONNECT PH TO HREF
CONNECT PT TO TREF
CONNECT P1 OF $!nozzle
CONNECT P$!a OF $!x TO P$!b OF $!y
CONNECT to next
CONNECT
```

---

## 第六部分：定位操作

```pml
POS $!pos
POS PA AT PT OF BRAN
POS X $!x Y $!y
ORI Z IS $!zDir AND X IS $!xDir
ORIENTATION $!ori
!pos = E $!x N $!y U $!z wrt world
```

---

## 第七部分：颜色/图层/显示

```pml
ADD $!elem COLOUR $!col TRANSL 50 EDGES OFF
REMOVE ALL
COLOUR CE $!col
ENHANCE $!item COLOUR $!col
UNENHANCE $!item
```

---

## 第八部分：工作区操作

```pml
savework
getwork
undodb 1
MARKDB 'description'
ENDMARKDB
```

---

## 第九部分：成员/层次操作

```pml
NEW FIXING AFTER LAST MEMBER
reorder $!a before $!b
reorder $!a after $!b
new stru $!name copy $!src rename $!src $!name
```

---

## 第十部分：Draft 出图操作

### 图纸创建（REGISTRY→DRWG→SHEET→VIEW→LAYER 全属性链）
```pml
NEW REGISTRY /TEMP-REGI
  SIZE 1189mm 841mm
  UCOD mm Distance mm Bore Nominal
  FONT 5
  POSFOR ENU

NEW DRWG /DETAIL/TEMP
  DATE '5 Apr 2013'
  TITL 'Detail Plot View'
  AUTH 'chris.whiteley'
  POSFORMAT ENU

NEW SHEET /DETAIL/TEMP/S1
  SIZE 120mm 60mm
  POSFOR ENU

NEW VIEW /DETAIL/TEMP/S1/V1
  DIR D
  VSCA 0.05
  VTYP Universal HLine
  SIZE 60mm 60mm
  XYPS X 30mm Y 30mm
  LFRA true

NEW LAYER /DETAIL/TEMP/S1/V1/USER_dims
  PURP DIMA
  FONT 11
  CHEI 3mm
  POSFOR ENU
END

NEW LIBY /DETAIL/TEMP/LIBY
  NEW PLLB
  NEW DLLB
    NEW IDLIST
      NEW ADDENTRY
  NEW TRLB
```

### 视图操作
```pml
DIR $!dir
VSCA $!scale
VTYP $!viewType
AUTO
adeg $!angle
DESADD CE COLOUR RED
```

### 标注创建
```pml
-- 线性标注
NEW LDIM DTANG $!dtang PTANG $!ptang
DIR $!dir
FROM PA OF $!comp
TO PL OF $!comp

-- 角度标注
NEW ADIM
SENSE CLOCKWISE

-- 文本注释
NEW TEXP CHEI $!h BTEX '$!text' ADEG $!angle JUST C ALIG TB

-- 标签
NEW GLAB ON $!ref BTEX |$!text|
NEW SLAB ON $!ref ATEX |$!tag| TMRF $!symbol
```

### 图形元素
```pml
NEW STRA DEF @
NEW ARC DEF @
NEW CIRC DEF @
NEW OUTL
NEW VRTX BULGE 0.85
NEW RECT
```

### 出图输出
```pml
PLOT SHEET FILE PDF "$!file" 'COLOUR STANDARD' OVERWRITE
PLOT SHEET FILE SVG "$!file" '$!opts'
LIEXEC /Draft_DXF_LI 'DXFOUT' CONFIGDATA '$!config' OUTPUTFILENAME '$!file'
```

---

## 第十一部分：规格库操作

```pml
SPREF $!<spec>                    -- 设置规格
SPREF NULREF                      -- 清空
!!ce.spref = !spco                -- PML2 直写

-- 规格选件
!specs = object SPECIFICATIONS(!spec.dbref())
!specs.loadComponents()
!components = !specs.components(!type, !questions, !answers)

-- 型材
NEW SCTN
SPREF $!spec
JUSLINE $!jusl
POSS $!from
POSE $!to
```

---

## 第十二部分：UDA 操作

```pml
:UDAname value                     -- 命令式设值
!!ce.:UDAname = value              -- PML2 设值
!this.component.udalis             -- 枚举
!this.component.$!<name>           -- 动态读
!destination.$!<name> = value      -- 动态写
!$!<name> default                  -- 复位
!$!<name> unset                    -- 清除
```

---

## 第十三部分：Rule 操作

```pml
RULE SET POSE (expr)
RULE EXECUTE SPRE ON ALL FOR CE
RULE REXECUTE
CHECKRULES CE
RULE DELETE ALL
!errors = !element.nruleerrors
!errorText = RULEERROR $!j
```

---

## 第十四部分：船体建模语句（stmtExec）

```pml
!obj = object MARHULLPAN()
!obj.stmtExec(0, 'NOT,R100, COR=1;')
!obj.stmtExec(0, 'CUT, AB,''P123B-SBP01'',S12,C=-85,R1=50;')
!obj.stmtExec(!groupNr, !statement)
!seams = !obj.getNearbySeams(!panelName)
```

**船体语句语法**：
| 语句 | 语法 |
|---|---|
| 角缝切口 | `NOT,R100, COR=1,2;` |
| 缝切口 | `NOT,R75,'P123B-SBP01', SEA=5;` |
| 限界切口 | `NOT,R100, LIM=2, V=2500;` |
| 组合切口 | `NOT, VU350*25*50, COR=3, LIM=2;` |
| 切口 | `CUT, AB,'PANEL01',S12,C=-85,R1=50;` |

---

## 第十五部分：PML 变量嵌入写法

| 形态 | 示例 | 说明 |
|---|---|---|
| `$!var` | `NAME /$!pipeName` | 直接内插 |
| `$!arr[i]` | `NEW BRAN $!name$n/$!i` | 数组元素 |
| `$!!ce.attr` | `name $!!ce.flnn` | 全局对象属性 |
| `$!<expr>` | `POS $!<pickedData.position>` | 表达式展开 |
| `|$!var|` | `DESC |$!text|` | 竖线保护文本 |
| `'$!var'` | `DATE '$!date'` | 引号字符串 |
| `$$` | `callback \|var _x '$$_PICK'\|` | 延后展开 |
| `$:` | `$:var$:` | 全局宏变量引用 |
| `$<cmd$>` | `$<CALLIB ...$>` | 命令回调嵌入 |
| `$D1=default` | `$D1=_APPMARMAIN` | 宏形参缺省值 |
| `$1`~`$9` | `!mainform = \|$1\|` | 位置参数 |
| `$.` | `$.` | 文件结束 |
| `$m/path` | `$m "%PDMSUI%/CLIB/FILES/FLOAD"` | 宏文件调用 |
| `$p text` | `$p !Total is: $!Total` | 输出 |
| `$*comment` | `$* comment` | 行内注释 |
| `$(...$)` | `$(H ... $)` | 块注释 |
| `$:debug$:` | 调试条件插入点 | binload/macload |
| `$G name=value` | `$G PIPE =/path/` | 定义全局变量 |
| `$U name` | `$U PIPE` | 导出全局变量 |
| `$S CALLxx` | `$S CALLG = $M ...` | 同义词定义 |
| `$R100/$R0` | PML 跟踪开关 | ch12 |
| `$r109 /file` | 全量动作落文件 | ch12 |
| `$M-` / `$M+` | 挂起/恢复（仅宏） | ch12 |
| `$Q` | 查下一合法命令 | ch12 |
| `$QM` | 查文件调用栈 | ch12 |
| `$H` | 帮助 | ch12 |
