# PML 记忆（合一版）：语法硬约束 · 生成规范 · 审核关卡 · 方法论

> 本文件是 `02-记忆维护\PDMS-PML二次开发\` 的**唯一记忆**，由原四件套（生成规范 / 审核规范 / E3D手册规则集 / 范式法）+ 总览合并而成。
> 适用范围：AVEVA PDMS / E3D 的 PML1（宏）与 PML2（函数/表单/对象）开发，也作为 AI 生成与审核 PML 的强制记忆。

**速查导读**：

| 场景 | 看哪章 |
|---|---|
| 写 / 改 PML 代码之前 | 第 2 章 生成规范（写码标准） |
| 代码放行 / 提交之前 | 第 3 章 审核规范（A→B→C→D 流程） |
| 规则有争议、查"为什么/手册原文" | 第 4 章 手册证据库（R 条目，带页码） |
| 搭 AI 工作流、TTY 联调排错 | 第 5 章 方法论 |
| 两个来源说法不一时 | 第 6 章 差异裁决表（勿来回改） |

---

## 1. 来源与证据层级

本记忆依据四个来源，冲突时按此裁决：

1. **官方源码实证**（PDMS12.0.SP6 `PDMSUI`+`PMLLIB` 两棵源码树，9030 份文件：pmlfnc 3030 / pmlfrm 1878 / pmlobj 1591 / 宏 268）——裁决"什么能跑、什么是主流写法"，官方代码即"真跑过、不会错"的标准样本；
2. **E3D 3.1 官方手册**《Software Customization》（`01-原始资料\0102\aveva™_e3d_design_software_customization_2026-06-22-16-51-01.pdf`，722 页，语法核心章 Page 179–368 与 PML1 附录 Page 677–721 已通读）——裁决"语法为什么合法、细节语义"，唯一带页码的证据；
3. **TM-1401《Programmable Macro Language Basic》、TM-1402《PML Form Design》《Advanced PML》官方培训教材**——教学范式；
4. **公众号《AI 与 PDMS 联动探索》一/二**（配管提效实践指南，2026-09-07）——流程设计与实战坑。

裁决原则：**语法合法性以手册为准；风格约定以生成规范（第 2 章）为准（约定可以比手册更严格）；产品差异按语境标注（PDMS ≠ E3D）；已裁决项见第 6 章。**

---

## 2. 生成规范（写码标准）

### 2.1 文件组织与装载机制

#### 2.1.1 两种语言两代结构

| | PML1（遗留） | PML2（现行，**必须用**） |
|---|---|---|
| 存放 | `PDMSUI` 环境变量指向的目录树 | `PMLLIB` 环境变量指向的目录树 |
| 文件类型 | `.mac` 宏、旧式表单 | `.pmlfnc` 函数、`.pmlfrm` 表单、`.pmlobj` 对象 |
| 调用方式 | 同义词（synonym）或 `$m/路径/文件` | 函数 `!!name()`；表单 `show !!name`；对象 `!x = object NAME()` |
| 装载 | 手动/同义词触发 | PDMS 启动时自动建立索引，首次使用时动态加载 |

实证：官方 PML2 文件中 `define method` 出现 4.1 万次、`gosub` 为 0 次——**新代码一律 PML2，禁止写 PML1 式宏逻辑**。

#### 2.1.2 平行目录原则

**禁止修改 AVEVA 标准产品的任何文件**（官方手册原话：改动可能导致 PDMS 行为异常）。定制代码必须放在平行目录树，并把路径前置到环境变量：

```bat
Set PMLLIB=C:\myproject\pmllib %pmllib%
Set PDMSUI=C:\myproject\pdmsui %pdmsui%
```

- 自定义路径放 `%pmllib%` **前面**，先搜到先生效，实现"覆盖式定制"而不动原文件。
- 在 PDMS 内用 `q evar pmllib` / `q evar pdmsui` 验证路径顺序。

#### 2.1.3 装载维护命令

| 场景 | 命令 |
|---|---|
| 新建了 pml 文件 | `pml rehash`（重建第一个搜索路径索引）或 `pml rehash all`（全部路径） |
| 修改了已加载的表单 | `pml reload form !!Name` |
| 修改了已加载的对象 | `pml reload object NAME` |

**运行时铁律**：`PML REHASH ALL` 执行后索引并未瞬时建好。人工敲命令天然有几秒间隔，但脚本/AI 连发命令会拿到旧索引甚至空调用。**重建索引后必须等待约 10 秒再发起下一次函数调用**。

#### 2.1.4 文件即定义

- 一个 `.pmlfnc` 定义一个同名函数；一个 `.pmlfrm` 定义一个同名表单及其方法；一个 `.pmlobj` 定义一个同名对象及其方法。
- 文件名（小写）与内部定义名必须对应（如 `addconnected.pmlfnc` 内 `define function !!addConnected()`），否则动态加载找不到。

### 2.2 命名规范

#### 2.2.1 变量

| 项 | 规则 | 依据 |
|---|---|---|
| 局部变量 | 单叹号前缀：`!name` | TM-1401 §4.2 |
| 全局变量 | 双叹号前缀：`!!name` | 官方源码：全局变量前 25 名全部 `!!` 开头 |
| 当前元素 | **只写 `!!CE`**，不写 `!CE` | 官方源码 `!!CE` 22462 次 vs `!CE` 622 次（36:1） |
| 长度/字符 | ≤64 字符，仅字母数字，**不得以数字开头，不得含 `.`** | TM-1401 §4.2 |
| 大小写 | PML 不区分大小写；按 camelCase 书写提升可读性 | 官方源码风格 |

#### 2.2.2 函数 / 表单 / 对象 / 方法

- 全局函数、全局表单：`!!camelCaseName`（如 `!!addConnected`、`!!aidceArrow`）。
- 自定义对象类型：全大写（如 `MODULEDATACACHE`、`COLLECTION`）。
- 方法与成员：点号前缀 camelCase（如 `.append`、`.moduleData`、`.ceArrowStat`）。
- 构造函数与所属表单/对象同名（`define method .aidceArrow()` 是 `!!aidceArrow` 的构造器）。

#### 2.2.3 表单 gadget 命名前缀（官方约定）

| 前缀 | 控件 | 前缀 | 控件 |
|---|---|---|---|
| `fme` | frame | `tgl` | toggle |
| `txt` | text 输入框 | `opt` | option 下拉 |
| `btn` | button | `lst` | list |
| `para` | paragraph 文本 | `cbo` | combo |

示例（官方 `aidcearrow.pmlfrm`）：`frame .fmeceArrow` → `toggle .tglCeArrow` / `text .txtHeight` / `option .optPosition`。

### 2.3 注释规范

| 场景 | 写法 | 禁止 |
|---|---|---|
| PML2 文件（.pmlfnc/.pmlfrm/.pmlobj） | `-- 注释内容` | ~~`! 注释`~~（`!` 是变量前缀，直接解析异常）、~~`//`~~、~~`#`~~ |
| PML1 宏（.mac/.pmlmac）行内/整行注释 | `$* 注释内容` | 同左 |

实证：官方源码 `--` 注释行共 91.9 万行——**注释密度是官方文化的一部分**，照此标准写。
（手册层面 `$*` 在 PML2 亦合法 [P197]，项目约定从严只用 `--`，见第 6 章#2。）

#### 2.3.1 文件头模板（PML2 文件必须携带）

```
------------------------------------------------------------------------
--
-- File:            myfunc.pmlfnc
--   Type:          Function Definition
--   Module:        myproject
-- Author:          <姓名>
-- Created:         <日期>
--
-- Description:     <一句话说明用途>
--
------------------------------------------------------------------------
```

对象/表单文件追加方法清单块：

```
-- Methods defined:
--  Method call                      Return   Description
--  ===========                      ======   ===========
--  myMethod()                       -        constructor
--  getData(STRING)                  ARRAY    return ...
```

#### 2.3.2 方法头模板（每个 `define method` 前必须携带）

```
------------------------------------------------------------------------
--
-- Method:      !getData()
-- Description: <用途>
-- Method Type: Function            ← 或 Procedure（无返回值）
-- Arguments:
--   [1] [R] [STRING] [说明]        ← R=只读 / RW=读写
-- Return:
--   [ARRAY] [说明]
--
------------------------------------------------------------------------
```

### 2.4 变量与类型系统

#### 2.4.1 四种基本类型

`STRING`、`REAL`、`BOOLEAN`、`ARRAY`；另有 `DBREF`、`POSITION`、`ORIENTATION`、`BLOCK`、`FILE`、`COLLECTION` 等对象类型（官方实例化频次前 12：DBREF 2873 / ARRAY 2443 / BLOCK 1576 / LINE 1319 / COLLECTION 1306 / FILE 874 / ORIENTATION 773 / POSITION 739）。

#### 2.4.2 PML1 与 PML2 赋值的本质区别

```
VAR !x (64)      ← PML1：!x 是 STRING（VAR 语法只存字符串）
!x = 64          ← PML2：!x 是 REAL，类型由内容自动推导
```

**新代码只用 PML2 赋值**。类型由内容推导：`42`→REAL，`|abc|`→STRING，`TRUE`→BOOLEAN，`ARRAY()`→空数组。

#### 2.4.3 BOOLEAN 规则（高频翻车点）

- 合法布尔常量：`TRUE FALSE YES NO T F Y N`（**不带引号**）。
- 非法判断：`if ( 1 )`（REAL 不是布尔）、`if ( |TRUE| )`（STRING 不是布尔）。
- 转换规则（`.boolean()` 方法或 `$` 前缀兼容判断）：REAL 0→FALSE，其余→TRUE；字符串 `'TRUE'/'T'/'YES'/'Y'`（大小写均可）→TRUE，`'FALSE'/'F'/'NO'/'N'`→FALSE。
- PML1 兼容：字符串变量加 `$` 前缀可参与 if 判断：`if ($flag) then`。

#### 2.4.4 数组

- 数组无需预声明，给元素赋值即创建：`!x[1] = |ABCD|`；多维数组 = 元素再赋数组。
- 遍历用 `do !v values !arr`（取值）或 `do !i index !arr`（取下标 1..N）。

#### 2.4.5 `q var` 是查询不是声明

`q var !x` 只是**打印**变量值的调试命令，绝不产生声明或赋值效果。声明/初始化用 `!x = ...` 或 `!x = real()` / `string()` / `ARRAY()`。

### 2.5 运算符与表达式

#### 2.5.1 词运算符（PML 没有符号比较符）

| 类别 | 合法 | 禁止 |
|---|---|---|
| 比较 | `EQ NE GT LT GE LE` | ~~`==` `!=` `>` `<` `>=` `<=`~~ |
| 逻辑 | `AND OR NOT` | ~~`&&` `||` `!`~~ |
| 算术 | `+ - * /` | — |
| 数学函数 | `SIN COS TAN SQR POW NEGATE ASIN ACOS ATAN LOG ALOG ABS INT NINT` | — |

TTY 实测：`>` `<` 直接报语法错误，无任何兼容模式。

#### 2.5.2 优先级（从高到低）

```
()  →  * /  →  + -  →  EQ NE GT LT GE LE  →  NOT  →  AND  →  OR
```

**不要赌优先级，复合条件一律加括号。**

#### 2.5.3 `$` 展开（在 PDMS 命令行/命令嵌入中使用）

| 写法 | 含义 | 实证频次 |
|---|---|---|
| `$!var` | 展开变量值（嵌入命令行） | 24858 次，主流 |
| `$!<表达式>` | 展开表达式（如 `$!<this.ceArrowHeight>`） | 459 次，按需 |
| `$!x` 前缀强制 | 把 REAL 强制为 STRING 参与字符串比较：`IF($!x eq !y)THEN` | 类型桥接手段 |
| `$p 文本` | 打印到命令行 | 调试/日志标准手段 |
| `$m/路径/文件` | 调用宏文件 | 宏入口 |
| `$1..$9`、`$d1` | 宏位置参数/具名参数 | 仅宏内 |

#### 2.5.4 字符串

- 三种定界符均合法：`` `xxx' ``、`|xxx|`、`'xxx'`。官方实证：单引号式 15.4 万次 vs 竖线 2.7 万次——**新代码统一用 `'..'`**，字符串内含单引号时才用 `|..|`（E3D 手册只认 `'` 与 `|`，反引号式见第 6 章#3）。
- 拼接用 `&`（自动把操作数转 STRING）：`!c = !a & !b & |mm|`。
- 字符串是对象，方法可链式调用：`!line.upcase().split().sort()`。

### 2.6 控制流

#### 2.6.1 合法结构速查

```
-- 循环（没有 loop/while/for 关键字）
do !i from 1 to 10 by 2          →  enddo
do !item values !array           →  enddo     ← 遍历集合/数组的首选
do !i index !array               →  enddo
do                               →  break if ( !v gt 1000 )  →  enddo   ← 无条件循环必须配 BREAK，否则死循环
skip if ( !i le 5 )                         ← 跳过本轮（类似 continue）

-- 判断（then 必需；含运算符的条件必须整体加括号——官方 6.3 万处带括号 vs 483 处裸写，
-- 裸写仅限 if !val.unset() then 这类单一方法/布尔值。新代码一律带括号）
if ( !x gt 5 ) then
elseif ( !x eq 0 ) then
else
endif

-- 错误处理
handle (41, 8)          ← 按模块号+错误码捕获
elsehandle ANY          ← 兜底任意其他错误
elsehandle NONE         ← 无错误分支
endhandle
```

#### 2.6.2 控制流禁令

- 禁 `loop ... endloop`、`for`、`while`、`switch`——PML 不存在这些关键字。
- 禁 `gosub`（官方源码 0 次使用）。
- `golabel /label` + `label /label` 官方全套源码仅 174 次且手册明示"应限制使用，降低可读性"——**新代码禁用**，用函数/方法拆分代替。标签名 ≤16 字符（不含 `/`）。
- 一个 IF 结构内只能有一个 `ELSE`。
- 开放 `do ... enddo` 若无可达的 `BREAK IF` 条件 = 死循环，禁止；需要上限时改 `do !i from 1 to N`。

### 2.7 错误处理与用户反馈

#### 2.7.1 handle 块

可能出错的 PDMS 命令（建元素、改属性、导航）一律包 handle 块。官方源码 `endhandle` 出现 16060 次——这是官方标准动作，不是可选装饰。捕获码形如 `(41, 8)`：`模块号, 错误码`，从报错信息 `(41,8) ERROR - ...` 中读取。

#### 2.7.2 Alert 对象（官方实证频次）

| 方法 | 用途 | 次数 |
|---|---|---|
| `!!alert.error( '...' )` | 错误弹窗 | 5073 |
| `!!alert.warning( '...' )` | 警告 | 2022 |
| `!!alert.confirm( '...' )` | 确认，返回 `'YES'/'NO'` | 1066 |
| `!!alert.message( '...' )` | 提示 | 1063 |
| `!!alert.question( '...' )` | 询问，返回 `'YES'/'NO'/'CANCEL'` | 104 |
| `!!alert.input( '提示', '默认值' )` | 输入，返回字符串 | 30 |

可用第 2、3 参数按屏幕比例定位弹窗（0.25, 0.1）。

### 2.8 数据库访问与遍历

#### 2.8.1 当前元素

- `!!CE` 是全局 DBREF 对象，永远指向当前元素，成员=属性：`!!CE.Hbore`、`!!CE.Pos.Up`。
- 可反向写属性：`!p = !!CE.Pos` → `!p.Up = 2000` → `!!CE.Pos = !p`。
- `/ref`、`/name` 等是**导航命令**，不是可赋值表达式，**不能写进变量**。遍历场景在循环体内导航：`do !p values !zone.members` 后用 `$!p` 或 `q ev !p`。

#### 2.8.2 元素收集：优先 PML2 COLLECTION 对象

官方手册原话："**It is recommended that all new PML uses COLLECTION objects**"。COLLECTION 返回 DBREF 对象数组（保留类型），PML1 的 `var !x coll all ...` 只返回字符串数组。

```
!coll = object COLLECTION()
!coll.type(|EQUI BRAN|.split())              ← 类型过滤
!coll.scope(!!ce)                            ← 范围（必须是 DBREF）
!coll.filter(object EXPRESSION(|name of owner eq '/200-B-4-B1'|))   ← 可选
!results = !coll.results()                   ← ARRAY of DBREF
```

批量取属性用 ARRAY.evaluate + BLOCK（内部游标变量固定名 `!evalIndex`）：

```
!names = !results.evaluate(object BLOCK(|!results[!evalIndex].flnn|))
```

#### 2.8.3 遍历子元素

```
do !m values !!ce.members
  ...
enddo
```

禁止凭其他语言经验编造 `.MEMBERS('X', c)` 之类的调用——对象成员/方法名必须在《Software Customisation Reference Manual》或官方源码中查证（见 2.14 防猜协议）。

### 2.9 函数开发规范（.pmlfnc）

标准骨架（官方实证模板）：

```
<文件头，见 §2.3.1>
define function !!myFunc(!param1 is STRING, !param2 is REAL) is ARRAY

  -- 局部变量就近声明并初始化
  !result = ARRAY()

  handle ANY
    !!alert.error('myFunc: 处理失败')
    return !result
  elsehandle NONE
    -- 正常路径
  endhandle

  return !result

endfunction
-- End of function definition
```

规则：
- 顶层**禁止裸语句**——所有逻辑必须包在 `define function ... endfunction` 内，无返回值的函数末尾直接结束，有返回值的以 `return !var` 收尾。
- 参数/返回值在签名处声明类型：`is STRING / REAL / BOOLEAN / ARRAY / DBREF / <自定义对象>`。
- 函数名与文件名对应；调用 `!!myFunc(...)`。

### 2.10 对象开发规范（.pmlobj）

```
<文件头 + Methods defined 清单>
define object MYTYPE

  member .items is ARRAY
  member .name  is STRING

endobject
-- End of object definition for MYTYPE

<方法头，见 §2.3.2>
define method .append(!data is MYTYPE)
  !this.items.append(!data)
endmethod
-- End of method definition for .append(MYTYPE)
```

规则：
- 对象类型名全大写；`member .x is TYPE` 集中声明在 `define object` 块内。
- 方法内用 `!this.member` 访问成员；方法可重载（同名不同签名，官方 `moduleData()` / `moduleData(STRING)` 实证）。
- 实例化：`!x = object MYTYPE()`；禁止假设未查证的构造函数参数。

### 2.11 表单开发规范（.pmlfrm）

#### 2.11.1 标准骨架

```
<文件头 + Methods defined 清单>
setup form !!myForm dialog resizeable        ← 形态修饰见 §2.11.2

  !!myForm.formTitle    = '我的表单'
  !!myForm.iconTitle    = 'MyForm'
  !!myForm.callback     = '!!myForm.init()'   ← 打开回调
  !!myForm.formRevision = ' $Revision: 1.0 $ '

  member .selItem is STRING                   ← 用户自定义成员集中声明

  frame .fmeMain '分组标题' at xMin yMin
    path down
    halign left
    vdist 0
    toggle .tglEnable '启用'
    text   .txtWidth  '宽度' width 14 is REAL format !!distanceFmt
    option .optMode   '模式' width 10
  exit
exit
-- End of form definition for !!myForm

<方法头>
define method .myForm()        ← 构造器，与表单同名
  !this.optMode.dText = |模式A 模式B|.split()
  !this.tglEnable.callback = '!this.apply()'
  ...
endmethod
```

【产品差异】`setup form` 是 PDMS12 官方源码主流范式（TM-1402 同）；E3D 手册推荐 `layout form`（强制 VarChars）——按目标产品选，见第 6 章#1。

#### 2.11.2 表单形态（setup 行修饰符）

| 写法 | 效果 |
|---|---|
| `dialog dock left` | 停靠左侧 |
| `dialog resizeable` | 浮动可缩放 |
| `document at xr 0.5 yr 0.5 size 100 100` | 居中定尺寸 |
| （无修饰） | 默认 dialog，按内容自动尺寸 |

选型规则：有 OK/Cancel 的表单不做停靠；**带 menubar 的表单不能停靠**。

#### 2.11.3 回调约定

- 表单级特殊回调成员：`initcall` / `okcall` / `cancelcall` / `quitcall`，赋字符串：`|!this.okCall()|`。
- 控件回调：`.callback = '!this.method()'`，回调体是**字符串**，写错不会报编译错，只在点击时炸——审核必查。
- 控件读写：`.val` 取值/赋值；`.active` 置灰；`.dText` 设下拉/列表内容（赋 ARRAY）；`.select('RTEXT', !val)` 回显选中。

#### 2.11.4 显示/隐藏

`show !!form`（加载并显示）、`loadform !!form`（只加载）、`!!form.show()` / `.hide()` / `.shown()`。

#### 2.11.5 单位处理（官方范式）

涉及长度输入必须区分 mm/inch（官方实证写法）：查当前单位 `var !u split units` → `!u[3].upcase().eq('MM')`；内部存储**统一毫米**，inch 会话在输入时 `* 25.4` 换算、显示时除以 25.4。输入框配 `format !!distanceFmt` 跟随系统精度。

### 2.12 命令嵌入与宏

- 在 PML 代码中直接写 PDMS 命令行（如 `AID CEARROW ON`、`NEW EQUI /ABCD`）是合法且主流的官方做法，变量用 `$!var` / `$!<expr>` 嵌入。
- 宏参数：`$1..$9` 位置参数、`$d1=xxx` 具名参数；调用 `$m/path/file.mac`。
- 宏内注释用 `$*`；PML2 文件内禁止出现 `$*` 注释风格（项目约定，见第 6 章#2）。

### 2.13 运行时与调试铁律

1. `pml rehash all` 后**等待约 10 秒**再调用任何函数/表单（索引异步建立）。
2. `> / < / == / !=` 直接语法错误，没有例外。
3. `q var !x` 只用于调试打印，不是声明。
4. TTY 调试输出统一用 `$p`；弹窗反馈用 `!!alert.*`。
5. 导航命令（`/ref`、`next`、`owner` 等）是命令不是表达式，不得赋给变量。
6. 函数/对象/表单被加载后其定义被 PDMS 持有，改文件必须 `pml reload` 对应实体，否则跑的是旧定义。

### 2.14 防猜协议（对 API 不确定时的强制流程）

实证教训：最危险的不是语法错（当场报错），而是 AI/人**编造一个语法自洽但库里不存在的 API 调用**。因此凡涉及不常用对象方法/成员/命令，必须按顺序执行：

1. **查手册**：《Software Customisation Guide》《Software Customisation Reference Manual》对应对象条目，确认方法名、参数、返回类型、MODIFIES/NO RESULT 语义。
2. **对源码**：在 PMLLIB/PDMSUI 官方源码树中 `grep` 该函数/方法名，抄 AVEVA 自己的真实用法（调用姿势、参数形式、上下文）。
3. **都查不到 → 显式标注不确定**：在代码上方加 `-- TODO-UNVERIFIED: <疑点描述>，需人工确认`，并在提交说明中列出，**禁止假装确定、禁止静默通过**。

### 2.15 附录 A：八大类禁止清单（AI 高频翻车对照表）

| # | 类别 | 错误写法（禁止） | 正确写法 |
|---|---|---|---|
| 1 | 注释 | `! 这是注释` | `-- 这是注释` |
| 2 | 控制流 | `loop !i = 1 to 10 ... endloop` | `do !i from 1 to 10 ... enddo` |
| 3 | 判断 | `if !x > 5 ... endif` | `if ( !x gt 5 ) then ... endif` |
| 4 | 比较 | `==` `!=` `>` `<` | `eq ne gt lt ge le` |
| 5 | 遍历 | `.MEMBERS('X', c)` | `do !m values !!ce.members ... enddo` |
| 6 | 封装 | 顶层裸语句 + return | `define function ... endfunction` |
| 7 | 变量 | `q var !x` 当声明 | `!x = ...` 赋值即声明 |
| 8 | 布尔 | `if ( 1 )`、`if ( |TRUE| )` | `if ( TRUE )`、`if ( !ok )`（BOOLEAN 型变量） |

### 2.16 附录 B：关键实证数据备查

| 指标 | 数据 | 结论 |
|---|---|---|
| `!!CE` vs `!CE` | 22462 vs 622（36:1） | 当前元素只写 `!!CE` |
| `define method` | 41629 次 | PML2 面向对象是绝对主流 |
| `gosub` | 0 次 | 禁用 |
| `golabel` | 174 次/9000+文件 | 实际不用，禁用 |
| `endhandle` | 16060 次 | 错误处理是标准动作 |
| `object COLLECTION()` | 1306 次 | 元素收集用 COLLECTION |
| `$!var` vs `$<expr>` | 24858 vs 459 | 简单展开为主 |
| 单引号串 vs 竖线串 | 154264 vs 27239 | 字符串统一 `'..'` |
| `--` 注释行 | 91.9 万行 | 注释密度对标官方 |

---

## 3. 审核规范（验收关卡）

本部分是第 2 章的验收侧，用于：人工代码评审、AI 生成 PML 的强制放行关卡、提交前自查。

### 3.1 严重度分级

| 级别 | 含义 | 处置 |
|---|---|---|
| **Blocker** | 必炸：语法错误、解析异常、运行时必错、编造 API | 一律打回，修复前禁止放行 |
| **Major** | 能跑但违规：风格背离官方范式、错误处理缺失、隐患（死循环风险、类型混比） | 打回修改，或经负责人书面确认豁免 |
| **Minor** | 可读性/一致性问题 | 建议修改，不阻塞放行 |

放行标准：**Blocker = 0，Major = 0 或全部豁免，Minor 记录留档。**

### 3.2 A 类：机器可查静态规则（附检测正则）

> 正则为 PCRE 写法，适用于 `grep -P`、VS Code 搜索或扫描脚本。对 `.pmlfnc/.pmlfrm/.pmlobj/.pmlmac` 全量扫描。
> **预处理**：扫描前先剔除注释行（`^\s*--`、`^\s*\$\*`）与文档分隔线（`={3,}`、`-{3,}`），否则 `==` 等模式会被官方文件头的 `===========` 淹没。以下规则均已在官方 9000+ 文件语料上回归验证，误报率为零或接近零。

#### A1 注释类

| ID | 级别 | 检测正则 | 说明 |
|---|---|---|---|
| CMT-01 | Blocker | `^\s*!\s*[^=!*/\s].*$` 且同行无赋值特征 | 用 `! 文本` 当注释（`!` 是变量前缀，解析异常）。注释必须 `--`（PML2）或 `$*`（宏） |
| CMT-02 | Blocker | `//|/\*|#` 出现在非字符串上下文 | C/Java 风格注释，PML 不支持 |
| CMT-03 | Minor | 无文件头块（文件前 20 行内无 `File:` 且无 `--`） | 缺官方式文件头 |

#### A2 控制流类

| ID | 级别 | 检测正则 | 说明 |
|---|---|---|---|
| CTL-01 | Blocker | `\bloop\s+!\w+\s*=`、`\bendloop\b` | 伪循环语法（官方语料 0 命中）。注意：绘图命令 `loop 1 of nxtr $!i` 是合法 PDMS 命令，**不要**把裸 `loop` 一词当错误 |
| CTL-02 | Blocker | `^\s*(for|while|switch)\b`（排除字符串与注释） | 不存在的关键字 |
| CTL-03a | Blocker | `^\s*if\b.*$` 行内无 `\bthen\b` | `then` 是语法必需，缺失必炸 |
| CTL-03b | Major | `^\s*if\s+![^(].*(eq|ne|gt|lt|ge|le|and|or)` 且条件未加括号 | 含运算表达式的条件必须整体加括号；官方 63232 次带括号 vs 483 次裸写（裸写仅限 `if !val.unset() then` 这类单一方法/布尔值），新代码一律带括号 |
| CTL-04 | Blocker | `gosub` | PML1 遗留，官方 0 次使用，禁用 |
| CTL-05 | Major | `\bgolabel\b` | 官方手册明示限制使用，新代码禁用，用函数拆分 |
| CTL-06 | Major | `^\s*do\s*$` 且块内无 `break if` | 开放循环无出口 = 死循环 |
| CTL-07 | Major | 同一 if 块内出现 2 个及以上 `^\s*else\s*$` | PML 单 if 结构只允许一个 else |
| CTL-08 | Blocker | `enddo/endif/endhandle/endfunction/endmethod/endobject/endform` 与对应 `do/if/handle/define...` 数量不配 | 块结构失衡，必炸 |

#### A3 运算符与表达式类

| ID | 级别 | 检测正则 | 说明 |
|---|---|---|---|
| OPR-01 | Blocker | `==|!=|>=|<=`（预处理后；官方语料 0 命中） | 符号比较不存在，改 `eq ne ge le` |
| OPR-02 | Blocker | if 条件内裸 `>`、`<`（排除 `$<...>` 展开语法与字符串） | 必须 `gt/lt`；TTY 实测必炸 |
| OPR-03 | Blocker | `&&|\|\|` | 逻辑运算用 `and/or` |
| OPR-04 | Major | 复合条件（含 and/or）未加括号分组 | 优先级 NOT>AND>OR，显式加括号消除歧义 |
| OPR-05 | Major | 混合型比较：`if ( !realVar eq '...' )` 或反向 | REAL 与 STRING 直接比较属无效语法；需 `$!x` 强制或 `.real()/.string()` 转换 |

#### A4 变量类

| ID | 级别 | 检测正则 | 说明 |
|---|---|---|---|
| VAR-01 | Blocker | `^\s*q\s+var\s+!\w+\s*$` 出现在非调试意图的交付代码中 | `q var` 是查询命令不是声明；调试残留应清除 |
| VAR-02 | Blocker | `(?<![!])!CE\b` | 当前元素只用 `!!CE`（官方 pmlfnc 语料本规则 0 命中，全局 36:1 实证） |
| VAR-03 | Major | `var !\w+ \(`（PML1 VAR 赋值） | PML1 式只存字符串；新代码用 PML2 `!x = ...` 获得类型 |
| VAR-04 | Major | 变量名含 `.` 或以数字开头：`!(?:\d\w*|\w*\.\w*)` | 非法变量名 |
| VAR-05 | Major | 全局变量 `!!xxx` 在非全局表单/函数定义处出现且无名下空间 | 全局变量污染；确认是否应局部化 |
| VAR-06 | Minor | 变量名 >64 字符 | 超长非法 |

#### A5 对象与 API 类（防猜重点）

| ID | 级别 | 检测方式 | 说明 |
|---|---|---|---|
| OBJ-01 | Blocker | 抽取全部 `.methodName(...)` 与 `object XXX(...)`，逐一在官方源码树 grep 对名 | **整库搜不到 = 编造 API，直接打回**；这是文章实测抓到的最隐蔽翻车形态 |
| OBJ-02 | Blocker | `.MEMBERS\s*\(` | 凭其他语言编造的成员访问；正确：`!!ce.members` 集合属性 + `do !m values` |
| OBJ-03 | Major | 元素收集用 `var !x coll all ...`（PML1） | 官方推荐新代码用 `object COLLECTION()`（返回 DBREF 数组而非字符串数组） |
| OBJ-04 | Major | 方法调用缺括号：`!x.upcase\b(?!\()` 类形态 | PML2 方法括号必须存在，即使无参 |
| OBJ-05 | Major | `object COLLECTION()` 后缺 `.scope(...)` 或缺 `.results()` | 收集三段式不完整 |

#### A6 封装与文件结构类

| ID | 级别 | 检测正则 | 说明 |
|---|---|---|---|
| PKG-01 | Blocker | `.pmlfnc` 内无 `define function` | 顶层裸语句禁止；一切逻辑入函数 |
| PKG-02 | Blocker | `.pmlobj` 内无 `define object ... endobject` | 对象文件结构缺失 |
| PKG-03 | Blocker | `.pmlfrm` 内无 `setup form ... exit` | 表单文件结构缺失 |
| PKG-04 | Major | 文件名（小写）与内部 `define function !!名`/`setup form !!名`/`define object 名` 不对应 | 破坏动态加载约定，找不到定义 |
| PKG-05 | Blocker | 改动落在 AVEVA 标准安装目录内文件 | 禁止改标准产品；必须平行目录 + 环境变量前置 |

#### A7 字符串与 IO 类

| ID | 级别 | 检测正则 | 说明 |
|---|---|---|---|
| STR-01 | Minor | 同一文件混用 `` ` ``、`'`、`|` 三种定界符且无必要 | 统一 `'..'`，含引号串才用 `|..|` |
| STR-02 | Major | 字符串拼接用 `+` | 拼接用 `&`；`+` 是算术运算，类型错误 |
| IO-01 | Major | 交付代码残留 `$p`/`q var` 调试输出 | 清理或转正式日志 |

#### A8 错误处理类

| ID | 级别 | 检测方式 | 说明 |
|---|---|---|---|
| ERR-01 | Major | 含建/删/改元素命令（`NEW/DELETE/MODIFY` 或属性写）的函数无 `handle ... endhandle` | 官方 1.6 万处 handle 是标准动作 |
| ERR-02 | Minor | `handle ANY` 分支为空或静默吞错 | 至少 `!!alert` 或日志，禁止静默 |
| ERR-03 | Minor | 用户可见错误用 `$p` 而非 `!!alert.error/warning` | 交互反馈走 Alert 对象 |

#### A9 表单类

| ID | 级别 | 检测方式 | 说明 |
|---|---|---|---|
| FRM-01 | Blocker | 回调字符串指向的方法在文件内不存在（抽取 `.callback = '...'`/`initcall` 等，对照 `define method` 清单） | 回调是字符串，写错编译期不报错，点击才炸 |
| FRM-02 | Major | 长度类 `text` 控件无 `is REAL format` 且代码无 mm/inch 换算 | 单位处理缺失；官方范式：内部统一毫米，inch ×25.4 |
| FRM-03 | Major | 带 menubar 的表单声明 `dock` | 手册明确不能停靠 |
| FRM-04 | Minor | gadget 名无前缀约定（fme/txt/tgl/opt/btn/lst/para/cbo） | 官方命名约定 |
| FRM-05 | Major | 构造器方法与表单不同名 | 官方约定同名构造 |

#### A10 运行时类（审核发布/部署动作）

| ID | 级别 | 检查项 | 说明 |
|---|---|---|---|
| RUN-01 | Blocker | 自动化脚本中 `PML REHASH ALL` 之后 10 秒内发函数调用 | 索引异步建立，连发必拿到旧/空索引；强制等待约 10 秒 |
| RUN-02 | Major | 修改已加载实体后只改文件未 `pml reload form/object` | 跑的是旧定义 |
| RUN-03 | Blocker | 把 `/ref`、`next` 等导航命令当表达式赋给变量 | 导航是命令不是值 |
| RUN-04 | Major | 部署清单未验证 `q evar pmllib` 路径顺序 | 自定义路径必须前置 |

### 3.3 B 类：语义审核清单（人工/AI 逐项过）

逻辑层问题机器查不出，逐项确认：

1. **业务上下文**：代码假设的 CE 类型/层级是否正确？（如在 ZONE 下建 EQUI，在 PIPE 上建 BRAN）错误层级是官方培训列出的头号运行错误。
2. **空集合防护**：`!coll.results()` / `!!ce.members` 可能为空数组，后续 `!arr[1]` 访问前是否有 `!arr.size() gt 0` 判断？
3. **单位一致性**：长度/角度/重量在存库、显示、换算三处是否统一（内部毫米制）？
4. **handle 分支语义**：`elsehandle NONE`（无错分支）与 `elsehandle ANY`（兜底）是否写反？`(模块号, 错误码)` 是否对得上目标报错？
5. **回调查通**：每个按钮/控件的 callback 方法存在、签名匹配、副作用（改 CE、改库）符合用户预期。
6. **全局状态**：写入的 `!!xxx` 全局变量是否有初始化路径？多表单/多会话复用时会不会读到脏值？
7. **遍历副作用**：`do !m values` 循环体内是否做了建删元素导致集合失效？需要先收集到 ARRAY 再操作。
8. **返回值契约**：声明 `is ARRAY/BOOLEAN` 的函数/方法，所有退出路径（含 handle 兜底）都有同类型 `return`？
9. **事务边界**：批量改库后是否需要 `SAVEWORK`？失败路径是否需要 `GETWORK`/回滚提示？
10. **不确定项**：代码中是否残留未标注的"猜测 API"？凡未查证处必须有 `-- TODO-UNVERIFIED:` 标记并写入提交说明。

### 3.4 C 类：运行时验证步骤（TTY/PDMS 实测）

静态全绿后在真实环境验证，缺一不可：

1. **装载验证**：`pml rehash all` → 等 10 秒 → 调用入口函数，确认无 `function not found`。
2. **正例路径**：用最小合法输入跑通主流程，核对数据库实际变化（`q att`、层级树）与预期一致。
3. **边界路径**：空输入、空集合、错误 CE 层级、超长/非法字符串各跑一次，确认 handle 分支按设计触发（Alert 弹出而非宏中断）。
4. **表单冒烟**：`show !!form` → 逐控件点一遍（每个 callback 至少触发一次）→ OK/Cancel/关闭三条退出路径。
5. **重复执行**：同一函数连跑两次，确认幂等或符合预期（重复建名冲突是否被 handle 捕获并友好提示）。

### 3.5 D 类：审核工作流

```
生成/提交代码
   │
   ▼
① A 类机器扫描（正则全量过一遍）      → Blocker/Major 打回
   │
   ▼
② 防猜核验（OBJ-01）：所有对象方法/成员/构造
   在官方源码树 grep 对名；查不到 → 查手册；
   手册也没有 → 标 TODO-UNVERIFIED 上报      → 编造 API 打回
   │
   ▼
③ B 类语义清单逐项过                  → 问题打回
   │
   ▼
④ C 类运行时实测                      → 失败打回
   │
   ▼
⑤ 放行：记录 Major 豁免项与 Minor 清单，归档到提交说明
```

**审核员（人或 AI 技能）职责边界**：审核只回答"合不合规、跑不跑得对"，业务逻辑对错由需求方终审——规范把语法层的错清零，就是为了让人只看业务层。

---

## 4. E3D 官方手册证据库（R0–R22）

> 来源：`01-原始资料\0102-PDMS-E3D-.NET二次开发文档\aveva™_e3d_design_software_customization_2026-06-22-16-51-01.pdf`（AVEVA™ E3D Design 3.1，© 2015-2026 AVEVA，722 页）。提取 PDF 文本层后通读 Page 179–368（PML 语法核心章 + 表单/菜单/命令章全部）+ Page 677–721（PML 1 表达式附录全部）；关键关键字做过全文检索核实。Reference 方法总表章（Page 409–677）未逐页精读，方法名以正文出现过的为准。
> 本部分供查证语法"为什么"；所有未标注【推断】的条目均可在尾注页码 [Pxxx] 找到原文依据。审查意见可直接引用编号（如「违反 R3-O1」）。

### R0 总则

- PML 全部内容（含 if/do 等关键字）大小写不敏感，引号或竖线内文本除外 [P197]。约定：关键字小写、变量驼峰、对象类型全大写 [P186]。
- 关键字没有缩写；命令建议写全称（全称不比缩写低效）[P197]。
- 控制构造只有四种：**if、do、golabel、handle**，手册全文无 switch/case [P203]。

### R1 注释

- 整行注释用 `--` 或 `$*` 开头；行内注释用 `$*`；多行注释块用 `$( ... $)`（也可用于临时注释掉代码）[P197]。
- ❌ 禁止 `!`、`//`、`#` 等其他语言的注释符。`!` 是变量前缀，不是注释 [P186 + 推断综合]。
- 【项目约定，比手册严格】PML2 文件一律只用 `--`，`$*` 仅限宏文件（见第 6 章#2）。

### R2 变量与类型

- `!` 开头 = 局部变量，`!!` 开头 = 全局变量 [P186]。
- 变量名：字母开头，仅字母数字，最长 64 字符；**名字中带点强烈不建议**（点被保留用于对象-方法分隔及表单 gadget 名）[P186]。
- 类型在创建时固定，给已有变量存错误类型直接报错 [P184]。
- 内置类型只有 **STRING、REAL、BOOLEAN、ARRAY**；**没有整型**（循环计数也用 REAL）[P184-185]。
- 系统类型（如 POSITION、ORIENTATION、DBREF）和用户类型经 `object TYPE()` 创建 [P185/188]。
- 类型化声明空值：`!X = REAL()` 等，值为 UNSET [P188]。
- UNSET 判定：`Unset(!X)` / `!X.Unset()`（或 Set 对应）；UNDEFINED（变量不存在）判定：`Undefined()` / `Defined()` **只有函数形式，无方法等价** [P195]。
- 删除变量 `!X.Delete()`；**禁止删除对象或表单的成员** [P196]。
- 全局名以 `CD` 开头为 AVEVA 系统保留；`!!CE`、`!!ERROR`、`!!FMSYS`、`!!CMSYS` 等为系统专用 [P186-187]。
- 自建对象/表单/全局函数名必须加公司前缀防冲突（手册示例 XYZ）[P181]。
- 命名纪律：一变量一用途；少用全局；能用对象/表单方法就不要写全局函数 [P187]。

### R3 表达式与运算符

- 比较/逻辑运算符全集：`EQ NE(NEQ) GT LT GE(GEQ) LE(LEQ) NOT AND OR`；**`==` `!=` `<` `>` 均非法** [P201-202]。
- 运算符前后必须有空格 [P201]。
- 名字后紧跟 `(` 而无空格，括号会被当成名字一部分 [P201]。
- 表达式两边类型必须匹配：REAL 加 STRING 报错；跨类型拼字符串用 `&`（自动转 STRING）[P200/202]。
- 优先级：括号 > 函数 > `* /` > `+ -` > 比较 > NOT > AND > OR [P201]。
- 文本定界符只有 `'` 或 `|`；**不配对的定界符会把后续多行吞成字符串** [P198-199]。【项目约定】统一 `'..'`，串内含引号才用 `|..|`（第 6 章#3）。
- REAL 带单位与量纲参与运算，量纲需兼容（1metre + 10cm 按当前单位出结果）[P203]。
- **PML 2 表达式只能用在 if、do 和 `=` 赋值中；命令参数里必须用 PML 1 表达式（`$!var`）或 VAR 命令** [P203]。
- if 测试必须是 BOOLEAN：`if (1)`、`if ('TRUE')` 非法；`TRUE/FALSE/YES/NO/T/F/Y/N` 不加引号合法；字符串转换用 `.Boolean()` [P205-206]。
- `IFTRUE(cond, a, b)`：a、b **两个都会被求值**（逆波兰求值），不能当惰性三元用 [P206]。

### R4 控制流

- if 完整结构：`if (expr) then` / `elseif (expr) then` / `else` / `endif`；**then 之后不能同行接语句**（`if (...) then !X = TRUE` 错误）[P204]。
- 计数循环：`do !x from 1 to 100 by 1 ... enddo`；`enddo` 必不可少；`from` 缺省 1、`to` 缺省无穷、`by` 缺省 +1；裸 `do ... enddo` 是死循环，需 break/breakif 退出 [P207-208]。
- 循环变量是 REAL，**进入循环会删除同名已有变量**；计数循环结束后变量保留最后值；**do values 循环结束后计数变量被销毁** [P207/221]。
- `break` / `break if (...)` 退出循环；`skip` / `skip if (...)` 跳回循环头；均只作用于**最内层**循环 [P208-209]。
- 嵌套 do 各层计数器必须不同名 [P209]。
- 遍历数组：`do !x values !array`（取元素值）、`do !x index !array`（取下标）[P209/221]。
- `golabel /name` + `label /name`：label 名最长 16 字符（不含 `/`）；**禁止跳入嵌套 do 块内部**，允许向外跳 [P209-210]。手册列为合法构造但明示限制使用；官方语料仅 174 次/9000+ 文件，项目约定**新代码禁用**（第 6 章#4）。
- 【推断】R4-F9：手册未记载 switch/case（全文检索 0 处），不得使用；若旧库代码出现需单独核验。

### R5 函数（.pmlfnc）

- 定义：`define function !!Name( !a is TYPE, ...) is RETTYPE` ... `endfunction`；不返回值就省略 `is RETTYPE`（即 procedure，建议用 `call !!Name(...)` 调用）[P189-190]。
- **一个函数一个文件**：文件名 = 小写函数名 + `.pmlfnc`（`!!` 不进文件名）；`define function` 必须是文件第一行 [P190]。
- 调用括号必须写，无参也要 `()` [P191]。
- **参数按引用传递**：函数内改参数 = 改调用者的变量（手册警告：强力且危险）；输入参数调用前必须有值；**常量不能当会被修改的实参** [P189-190/230]。
- 输出型参数调用前必须已存在：`!Length = REAL()` [P190]。
- `ANY` 类型关闭参数类型检查——是例外不是常规；配合 `.objectType()` 判型 [P191]。
- `return` 设置返回值；函数运行中**不能切换模块**，失败用 EXIT 退出 [P189/190]。
- 有返回值的函数可用于任何表达式位置 [P189-190]。

### R6 对象与方法（.pmlobj）

- `define object NAME` / `member .x is TYPE` / `endobject`；定义存小写同名 `.pmlobj` 于 PMLLIB，自动加载 [P185-186]。
- 方法定义与对象同文件、放在 `endobject` 之后：`define method .Name()` ... `endmethod` [P192]。
- 方法内用 `!This` 引用对象自身：`!This.Answer = 42` [P192-193]。
- **默认构造器** = 与对象同名无参方法，创建时自动调用；带参构造 `object TYPE(args)` [P193-194]。
- 方法重载靠参数列表区分；显式类型优先于 ANY 匹配 [P193-194]。
- 修改对象定义后必须 `pml reload object 名字` [P194]。
- 成员为 PML 对象类型（如 POSITION）的属性修改必须两段式：取出→改成员→整体赋回 [P226]。
- `=` 赋值是深拷贝；但表单/gadget/DB 引用只拷引用不拷对象 [P229]。
- 传参视角：gadget 的 `.val` 作实参是只读的，要改就传 gadget 本身（`is GADGET`）；DB 属性值作实参同样只读 [P230-231]。

### R7 数组

- `!A[1] = v` 自动创建数组；**数组名与 `[` 之间不能有空格**；下标是值为正的表达式 [P210-211]。
- 稀疏数组合法；**负下标已禁用**；下标 0 合法但多数数组功能忽略它，不建议用 [P211]。
- 数组可异构、可多维 `!A[1][2]`、可整体赋给元素 [P211]。
- **有数组方法就禁止手写 do 循环**（手册明言效率高得多）：Size / Append / AppendArray / Clear / Delete / RemoveFrom / Sort / Invert / SortedIndices / ReIndex [P212-214]。
- Append 前数组必须存在，必要时先 `!A = ARRAY()` [P212]。
- 字符串 `.Split()`：缺省按空白分隔（连续空白算一个、首尾忽略）；显式指定分隔符则连续分隔符产生空元素 [P213]。
- 对象数组排序：BLOCK + `.Evaluate()` 提取键 → `.SortedIndices()` → `.ReIndex()` [P220]。
- 多级排序/去重/分组小计用 PML 1 的 `VAR ... SORT`（CIASCII / NUMERIC / UNIQUE / NOUNSET / LASTINGROUP 等）[P215-218]。

### R8 数据库访问（E3D）

- `!!CE` 是系统提供的**当前元素**全局变量，类型 DBREF；对它赋 DBREF 即导航：`!!CE = !!CE.owner` [P225-226]。两套官方语料实证频次：2937 份中 11889:416（≈30:1）、9030 份中 22462:622（36:1）——当前元素只写 `!!CE`。
- 属性点链访问：`!!CE.cref.pspec.rating` [P225]。
- P-point 按下标访问：`!!CE.Pdirection[1]`、`!!CE.Pposition[3]` [P226]。
- 空引用判定：`if (!ref EQ NULREF)` 或 `if (UNSET(!ref))`；无效引用用 `BADREF(!ref)` [P226]。
- 属性名用附录中的**全称**，保未来版本兼容 [P226]。
- 直接给属性赋值允许且类型必须匹配：`!!CE.Built = TRUE`；但把属性值传进函数再改是只读的（见 R6）[P226/231]。
- 遍历数据库元素的官方范式：`!c = object COLLECTION()` → `.type('SITE')` → `.results()` → `do !x values !allSites` [P209]。
- 批量求值：`VAR !Array EVALUATE (expr) FOR select [COUNTVAR !n]`，可 APPEND 或指定起始下标覆盖 [P227]。

### R9 错误处理

- 错误发生后**下一条命令是 handle 才能拦截**：`handle (46,27)` / `elsehandle (46,28)` / `elsehandle ANY` / `elsehandle NONE` / `endhandle`；处理完从 `endhandle` 后继续 [P231-232]。
- 默认 `onerror RETURN`（当前宏/函数放弃，交调用者处理）；`onerror GOLABEL /label` 的标签后第一条必须是 handle；`onerror CONTINUE` 压制错误但**效果不可预测，慎用**；`onerror PAUSE` 仅调试 [P232]。
- handle 块内查详情：`q var !!error` [P233]。
- 上抛/自造错误：`return error [n ['消息']] [NOALERT]` [P233]。

### R10 文件 IO

- `!f = object FILE('路径')` 创建不打开；`.Open('READ'|'WRITE'|'OVERWRITE'|'APPEND')`；用完 `.Close()` [P233-234]。
- `.ReadRecord()` 逐行返回 STRING，**文件尾返回 UNSET STRING**，用 `.Set()` 判定 [P234]。
- 首选整文件读写：`.ReadFile()` 返回字符串数组（**默认上限 10000 行**，可指定）、`.WriteFile('WRITE', !array)` [P234]。
- 常见文件错误码：(160,9) 文件不存在、(160,36/37) 未打开就读/写、(41,319) 权限不足 [P235]。

### R11 表单与回调（.pmlfrm）

- PML 2 用 `layout form !!name ... exit`；`setup form` 是旧 FixChars 排版模式（向后兼容），E3D 新表单用 layout form [P255/258]。【产品差异】PDMS 12.x 项目按官方源码范式沿用 `setup form`，按目标产品选——见第 6 章#1。
- 一表单一文件，小写名 `.pmlfrm`；方法写在 `exit` 之后；**文件中不得出现表单定义与方法之外的可执行语句**（后果不确定）[P242-243]。
- 表单即全局对象变量：名字不得与其他全局变量、对象类型、表单冲突 [P196/240]。
- gadget 是表单成员：`!This.gadget.val`；gadget **不支持**用户自定义成员与方法 [P240-241]。
- 默认构造器 `.formname()` 只在**加载时**执行一次，重新 show 不会再跑；每次显示都要初始化的用 `initcall` [P245-246/260]。
- initcall 不得显示其他表单、不得请求用户输入（可用 ALERT）；可 `return error 1 '消息'` 中止显示 [P260]。
- 回调是字符串：`callback |!this.method()|`；复杂回调整体用表单方法；open callback 形如 `'!this.Method('`（只写左括号，F&M 自动补参）[P242/247-248]。
- 表单级回调成员：Okcall / Cancelcall / Quitcall / FirstShownCall / KillingCall / initcall，语义见 [P260-262]；KILLING 回调里禁止改表单和 gadget [P262]。
- 显示控制：`show !!form` / `hide !!form` / `kill !!form` / `loadform !!form`；hide 再 show 不会重新加载定义 [P243]。

### R12 宏与 $ 转义序列

- 常用：`$P` 输出、行尾 `$` 续行、`$$` 字面 $、`$newline`、`$M 文件` 执行宏、`$!var` 展开为字符串（PML 2 尽量用 String() 方法替代，便于调试）[P198]。
- 宏参数 `$1`–`$9`；缺省值 `$Dn = ...`（写在开头）；含空格参数用 `$<...$>` 包裹；分隔符可改 `$,`（列表以 `$.` 结束）[P222-223]。
- 宏参数只能是 STRING：`$M file $!X $!Y`；手册明言**不要大量混用宏与函数** [P223]。
- 同义词（synonyms）可用在宏中，**PML 函数中禁用**（全局副作用 + 全局性能惩罚）[P224]。
- PML 指令（`pml rehash` 等）是命令行用的，**不应写进回调** [P244]。

### R13 索引、加载与编码

- `pml rehash` **只扫描 PMLLIB 第一个目录**；`pml rehash all` 扫全部目录、耗时长、避免多用户同时执行 [P199-200]。
- Administration 1.9.4+ 起索引改内存管理，`pml rehash` 即更新内存 [P200]。
- 查 PML 文件位置：`q var !!PML.getpathname('x.pmlfnc')` [P200]。
- 扩展名全部小写：`.pmlcmd` `.pmlfnc` `.pmlobj` `.pmlfrm` [P199]。
- 源文件编码：UTF8 带 BOM（首选）或 ASCII 7-bit；**禁用 8-bit 单字节扩展字符**（° € 等在 CJK 环境会出问题）[P235]。

### R14 调试命令不得留在成品

- `PML TRACE ON/OFF`、`$R`、`$M-`/`$M+`、`onerror PAUSE`、`$Q`、`$QM` 仅限调试，**不得留在交付代码里** [P238-239]。

### R15 升级兼容（手册"严重警告"）

- 只在 User 区用标准宏的**副本**做修改，**永不修改原始文件** [P181]。
- 跟随 AVEVA 标准 AppWare 的风格与约定 [P181]。
- 新对象/表单/全局函数名必须加公司前缀防冲突 [P181]。

### R16 与公众号文章规则的对照（交叉验证）

| 文章规则 | 手册验证结果 |
|---|---|
| 注释必须 `--` | ✅ [P197] |
| 循环必须 `do ... enddo` | ✅ [P207]，且手册无 loop 关键字 |
| `if (!x gt 5) then ... endif` | ✅ [P201/204]，并补充：then 后不能同行接语句 |
| 比较必须 eq/ne/gt/lt | ✅ [P201-202]，`<` `>` `==` `!=` 全部非法 |
| 遍历用 `.members` + `do ... values` | ⚠️ `do ... values` ✅ [P209]；`.members` 是 DB 元素伪属性写法，本手册未记载（PDMS 语境），E3D 官方范式是 COLLECTION → results() → do values |
| `!!CE` 引用当前元素 | ✅ [P225]，官方明确"special Global variable"，类型 DBREF |
| 封装用 `define function ... endfunction` | ✅ [P189]，且一文件一函数、首行定义 |
| `PML REHASH ALL` 后等索引建完再调用 | ✅ [P199-200]，补充细节：`pml rehash` 只扫第一目录，`rehash all` 扫全部；新版索引在内存 |
| `/ref` 是命令不能赋值 | 手册未记载 `/ref`（PDMS 命令）；E3D 中切换当前元素的官方写法是 `!!CE = !dbref` [P226] |

### R17 菜单（bar / menu）

- 表单菜单分 MAIN 与 POPUP 两体系：一个菜单只能属一个体系；MAIN 体系菜单全局只能出现一次；POPUP 菜单可用于多棵弹出树但每棵树内只能出现一次；**菜单不得自引用** [P291]。
- 混合表单定义顺序：先 bar → 再 MAIN 菜单 → 最后 POPUP 菜单（显式标 popup）；动态 NewMenu() 创建时必须始终指定类型 [P291]。
- 一个表单只有一个 bar 菜单（名字固定为 bar）[P292]。
- 加字段：`!menu.Add('<CALLBACK|TOGGLE|MENU|FORM>', <Dtext>, <Rtext>, {<FieldName>})`；Dtext 不可空；Rtext 含义——CALLBACK/TOGGLE=回调串、MENU=菜单名（不带点）、FORM=表单名（不带!!）；SEPARATOR 可命名，用于字段组管理 [P293]。
- 指向表单的菜单项文本按惯例以 `...` 结尾（必须写进 Dtext）；子菜单的拉出箭头 `>` 由系统自动加 [P293]。
- 系统 Window/Help 菜单：`add('<dtext>','window')` / `add('<dtext>','help')`；Help 按惯例放最右 [P293-294]。
- 弹出菜单必须先存在才能 SetPopup()；`!menu.popupGadget()` 返回 gadget 或 UNSET [P294-295]。
- 字段状态：`SetFieldProperty(名,'ACTIVE'|'VISIBLE'|'SELECTED',布尔)` 与 `FieldProperty(名,属性)` 读取（属性可缩写 ACT/VIS/SEL；SEL 不能用于 bar）；命名 SEPARATOR 隐含其后到下一分隔符的字段组 [P297-299]。

### R18 表单布局与加载

- gadget 只能定义在 `layout form ... exit` / `setup form ... exit` 序列内；定义格式 `类型 名字 {通用属性} {专有属性}`；通用属性（位置/tag/tooltip/callback/anchor/dock）任意顺序，**专有属性顺序必须按语法图** [P302-303]。
- **layout form 强制 VarChars**（FixChars 非法）；setup form 缺省 FixChars（旧模式）；新表单一律 layout form（E3D 语境）[P276-277]。
- 自动布局：`path right/down`（缺省 right），HDIST 缺省 0.5、VDIST 缺省 0.2；手册强烈建议自动布局+相对定位，**避免绝对坐标**（at x 12 y 5）[P275/280]。
- 相对定位 AT：`at xmin.g1 ymax.g1+1`、`at xmax form-size`（右对齐不撑宽表单）、`width to max.g1`（按位置范围定尺寸）；可省略 x 或 y 让该轴自动放置 [P282-283]。
- **ANCHOR 与 DOCK 互斥，且只能在定义时设置，运行期不可改**；VIEW/ALPHA/paragraph/textpane/container 只支持 DOCK FILL；VIEW、ALPHA 必须独占一个 frame [P287]。
- 表单原点在左上角，只能向 +x/+y 扩展——**同一容器内 DOCK LEFT / DOCK TOP 不得使用两次** [P287-288]。
- **gadget 定义顺序 = TAB 键导航顺序** [P275]。
- 布局建议（手册）：定义区只写布局命令；tooltip/取值/回调设置放构造器方法 [P275]。
- TABSET 不可嵌套；tabbed page frame 的 DOCK/ANCHOR 被忽略（恒 DOCK FILL）；程序切页必须设**新页** visible=true（设旧页 invisible 无效）；HIDDEN/SHOWN 事件只在页 frame 定义了 open callback 时才触发 [P278/300/309/319]。
- TOOLBAR frame 只能出现在 MAIN 表单上，且只能含 BUTTON/TOGGLE/OPTION/TEXT/COMBOBOX/SLIDER/NUMERICINPUT；MAIN 表单上 toolbar 之外的 gadget 归入名为 'Default' 的工具条 [P300-301]。
- FRAME 单选组：直接包含的 RTOGGLE 组成单选组（仅 NORMAL/PANEL/FOLDUPPANEL 有效），`FRAME.val`=选中序号（0=全不选）；事件顺序 UNSELECT(旧)→SELECT(新)→SELECT(FRAME) [P317-319]。
- `hide !!form`：gadget 值被重置（同 CANCEL）但 **CANCELCALL 不执行**——hide 前先取走数据 [P269]。
- `kill` 一般不要写进 AppWare；kill 后再 show 触发慢速重新加载——改用 `loadform !!form` + `!!form.show()` [P269]。
- 对已存在表单再执行 `layout form !!同名` 会 kill 并重建定义（慎用）[P269]。
- show 缺省产生**子表单**（Form Family），OK/CANCEL 按最年轻优先级联逐个执行；独立显示用 `show !!form free`，定位 `At xr a yr b` / `Cen`（屏幕比例坐标）；`!!form.show()` 不会动态加载定义 [P267-268]。
- 回调内对 gadget 的修改延迟到回调结束才上屏；要立即生效用 `!gadget.Refresh()`；REFRESH 命令刷新所有表单；**交互 do 循环中删除数据库元素后必须 REFRESH**；刷新要省着用（尤其视图）[P306]。
- 进度条/中断：`!!FMSYS.setProgress(百分比)`、`setProgressText`、`setInterrupt(按钮)`、`Interrupt()`；**setProgress 会处理 UI 事件，要丢弃事件就在 setProgress 前先调 Interrupt()** [P359-360]。
- `!!FMSYS.loadForm('名')` 强制加载并返回 FORM 引用（失败返回 UNSET FORM）；`currentDocument()` 取当前文档表单；`SetStatusText()` 写状态栏（内容是临时的）[P363-364]。
- 运行光标函数前先查 `!!FMSYS.OKCurfnView('g2d'|'g3d'|'ANY'[,'subtype'])` [P364]。

### R19 常用 gadget 硬性语法

- paragraph：无 tag、无 callback（被动不可点）；文本/像素图二选一，**定义后不可互换**；**定义后尺寸不可变**；不给初始文本就必须给初始尺寸 [P324]。
- button：`button .名 '标签' CALLBACK '串' | FORM !!子表单 | 控制属性`；控制属性 OK/APPLY/CANCEL/RESET/HELP——**每类每表单只能一个（APPLY 例外可多个）**；有 APPLY 就应配 DISMISS（无回调的 CANCEL 按钮）；**OK 按钮自身的 callback 会被忽略** [P326-327]。
- LINKLABEL 子类型：无边框、无按压态、无控制属性、不支持改背景色 [P326]。
- toggle：tag 显示在右侧；.val 为 BOOLEAN，缺省 FALSE [P328]。
- rtoggle：**只允许出现在 frame 内**；要区分 SELECT/UNSELECT 必须 open callback；`States '' '值'` 定义 onValue [P328-329]。
- option：文本型**必须给 width**；选项数组赋给 Dtext（Rtext 可选）；`select('Dtext',v)` / `selection()` / `.val`=索引；像素图型必须给 WIDTH + HEIGHT 或 ASPECT [P330-331]。
- combobox：显示框缺省可编辑，VALIDATE 事件需 open callback 才能与 SELECT/UNSELECT 区分；定义命令为 combo [P330]。
- slider：`range -50 +50 step 5 val -2`；事件 START/MOVE/STOP（建议 open callback）；MOVE 后系统不自动刷新 [P331-332]。
- numericinput：range/ndp/val；SELECT 与 MODIFIED 事件（MODIFIED 需 open callback 且使能，缺省关闭）[P333]。
- list：**必须给 SINGLE/MULTIPLE 和 width+height（length）**；Dtext 必给、Rtext 可选（缺省同 Dtext）；单选可加 zerosel / noReselect；多列用 SetHeadings/SetRows/SetColumns（多列 Dtext 是制表符分隔串）；**多选列表的事件序列（UNSELECT 批 + SELECT 批）中不得程序性改列表内容——有崩溃风险，改动只在 STOP 事件做**；手册强烈建议多选列表用 open callback [P333-337]。
- selector（数据库选择器）：**DATABASE 关键字必须**；可选 OWNERS/MEMBERS/AUTO；auto 与 multiple 不可同用 [P338]。
- text：**WIDTH 必须给、IS 类型必须给**；SCROLL 缺省 132、最大 256；NOECHO 显示星号（密码）；FORMAT 对象控制显示与输入格式（值恒按数据库单位存储，如距离 mm）[P338/341-342]。
- text 的 ValidateCall **只能检测并报错，不得修改该字段值** [P343]。
- text 字段 unset 判定 `!text.val.Unset()`；`clear()` 置 unset；老式 untyped PML1 字段用空串表示 unset——**避免使用旧式字段** [P342]。
- textpane：值 = 字符串数组（一行一元素）；setline/line/count/setcurpos/curpos；FixChars 强制等宽字体（对齐报表）[P345-346]。
- 快速遍历选中项/行：`do !x list !!form.list` / `do !x selector !!form.sel` / `do !x pane !!form.pane`（退出后 do 变量被销毁）[P347]。
- Alert 对象：`!!Alert.Error/Message/Warning/Confirm/Question/Input(...)`；**全部阻塞**；Confirm 返回 YES/NO，Question 返回 YES/NO/CANCEL；Input 等价 tty 的 VAR READ，宜少用 [P357-358]。

### R20 PML 命令对象（.pmlcmd）

- 定义：`setup command !!名 ... exit` + 构造器中设 `!this.key` 与回调；存小写同名 `.pmlcmd` 于 PMLLIB [P270-271]。
- 属性：Enabled / Checked / ExecuteOnChecked / SelectedIndex / Select；回调：EXECUTE / LIST / REFRESH / STATE，均收 `!args` 数组；STATE 回调返回 'Enabled'|'Disabled'|'Hidden'|'Checked'|'Unchecked'（可组合 'Enabled|Checked'）[P271-274]。
- 装载注册：`PML LOAD COMMAND !!名` → `!!名.register()`；**注册后 key 与回调不可再改**；命令不跨模块切换持久化 [P271/274]。
- **REFRESH 回调必须设 refreshFilters**（如 INITIALISED/CONTEXT），否则每次 CE 变化、每个表单激活/关闭都会执行——性能与调试灾难 [P273-274]。
- 带页签的界面里按钮**不要直接调 PML 宏**——无法控制状态/可见性，必须用命令对象；状态按钮/组合框必须用命令对象 [P270]。
- 用户命令在 `!!loadUserCommands()`（模块启动时调用）或 PML add-in 初始化回调中装载注册 [P274/366]。

### R21 PML 1 表达式（命令参数 / 报表模板 / 规则专用）

- 分工：PML 2 表达式只用于 if、do、`=` 赋值；**命令参数、报表模板、规则中用 PML 1 表达式**（`$!var`、VAR 命令）[P203/224]。
- 拼接：PML 1 用 `+`；PML 2 赋值表达式用 `&`（自动转 STRING）[P707/202]。
- 逻辑常量：TRUE/ON/YES、FALSE/OFF/NO [P679]。
- GT/GE/LE/LT 只用于数字和位置；EQ/NE 可用于任意同类型对（含 ID、位置、方向、方位、ppoint）[P679]。
- 函数名大小写不敏感、可缩写（MATCHWILD 写 MATCHW/ILD、NEGATE 写 NEG）[P684/696]。
- **三角函数以度为单位**；ATANT(y,x) 可安全处理分母为零 [P691-694]。
- 数值函数清单：ABS ACOS ASIN ATAN ATANT ALOG ARRAY(pos/dir/ori→3数) ARRAYSIZE ARRAYWIDTH COMPONENT..OF INT(截断) LOG MATCH MAX MIN NEGATE NINT(四舍五入) OCCUR REAL POWER SQRT VVALUE [P691-698]。
- 文本函数清单：AFTER BEFORE DISTANCE(英尺英寸格式化) LOWCASE UPCASE PART REPLACE STRING SUBSTRING TRIM VTEXT [P707-717]。
- STRING(数值)：最多 6 位有效数字、去尾零；STRING(n,'D0'~'D6') 定小数位；**数值一律输出为毫米**，要单位转换用 DISTANCE() [P714-715]。
- REAL(text) 读字符串开头数字并忽略单位限定符（限定符须合法）；VVALUE/VTEXT/VLOGICAL 用于**迟到求值**（报表模板里的变量必须包一层，否则定义表单时就被求值）[P698/717-718]。
- **比较容差**：数字相对容差 0.000001（`1.000001 GT 1` 为 FALSE）；位置 0.5mm；方向/方位 0.005——精确比较前先想清楚容差 [P719-720]。
- UNSET 跨比较规则：EQ/GT/GE/LT/LE → FALSE，NE → TRUE，AND/OR 中按 FALSE；整个表达式 UNDEFINED 时直接报错 [P720-721]。
- **MODIFIED/DELETED/CREATED 函数不能用在 PML 2 表达式里**（只能 PML 1）[P687]。
- MATCHWILD 通配 `*` `?`（可用第 3/4 参重定义）；EMPTY(text) 判零长串 [P684]。
- PART(text,n[,sep])：负 n 从右数；SUBSTRING 支持负位置/负长度；TRIM(text,'LRM'[,字符]) [P711/716]。
- REPLACE 支持第 4/5 参控制起始与替换次数，负值反向 [P712-713]。
- 位置表达式：`POS OF /el WRT /*`；`N 1000 FROM /el`；WRT 在"绝对→相对"与"相对→绝对"间切换（缺省 owner 轴系）；POLAR dir DIST d FROM pos [P700-705]。
- 位置比较只比较双方**都定义了**的坐标轴；GE 不是 LT 的反面 [P704]。
- 单位：内部一律数据库单位（距离 mm）；一方单位未知时按已知侧折算 [P689/718-719]。
- ID 表达式可 OF 无限嵌套：`SPEC OF SPREF OF FLAN 1 OF NEXT BRAN`；与数字等语法冲突时加 ID 前缀消歧 [P699-700]。

### R22 内置对象方法速查（已核实子集）

- 全量方法表在手册 Reference 章（Page 409–677，按对象类型分列）——待后续按需精读补全，下列仅为正文出现过的方法。
- 所有对象：`.objectType()`、`.String()`、`.Unset()` / `.Set()`、`.Delete()`（**对象/表单成员禁止删除**）[P191/195/196]。
- STRING：`.Length()`、`.trim()`、`.Split([分隔符])`、`.Boolean()`、`.Real()`、`.String()` [P188/191/206/213]。
- REAL：`.UNITS()`、`.DIMENSION()`、`.String()`、`.Between(a,b)`、`.Cosine()` 等 [P188/192]。
- ARRAY：`.Size()`、`.Append()`、`.AppendArray()`、`.Clear()`、`.Delete()`、`.RemoveFrom(起,数)`、`.Sort().Invert()`、`.SortedIndices()`、`.ReIndex()`、`.Width()`、`.Evaluate(BLOCK)` [P212-214/220]。
- FILE：`.Open('READ'|'WRITE'|'OVERWRITE'|'APPEND')`、`.ReadRecord()`、`.WriteRecord()`、`.ReadFile()`、`.WriteFile('WRITE', !array)`、`.Close()` [P233-234]。
- COLLECTION：`.type('类型')`、`.results()` [P209]。
- FORM：`.show()` / `.show('free')` / `.show('At',x,y)` / `.show('Cen',x,y)`、`.hide()`、`.setactive(bool)`、`.setGadgetsActive(bool)`、`.gadgets()`、`.newmenu(名,类型)`、`.setPopup()`、`.LoadForm()` [P268/305/263/292/294/363]。
- GADGET：`.type()`、`.name()`、`.subtype()`、`.container()`、`.setfocus()`、`.refresh()`、`.addPixmap()`、`.setpopup()`、`.setTooltip()`、`.seteditable()`、`.select()`、`.selection()` [P303-306/294/318/334]。
- FMSYS：`.setProgress()`、`.setProgressText()`、`.setInterrupt()`、`.Interrupt()`、`.loadForm()`、`.currentDocument()`、`.SetStatusText()`、`.OKCurfnView()`、`.SetDefaultFormLayout()` [P358-364]。
- Alert（!!Alert 全局对象）：`.Error()`、`.Message()`、`.Warning()`、`.Confirm()`、`.Question()`、`.Input()` [P357-358]。

### 待核验（均为推断，未经原文证实）

- `.members` 伪属性、`/ref`、`q ev` 属 PDMS 命令体系，E3D 手册不含，需以 PDMS 文档或官方源码核验。
- switch/case 在 PDMS 旧 PML 中是否存在：E3D 手册 0 处出现，E3D 3.1 下不使用。

---

## 5. 方法论：官方源码漏斗与 AI 工作流（源自公众号《AI 与 PDMS 联动探索》一/二）

> 来源文件：`01-原始资料\0105-AI辅助PML开发\2026-09-07-公众号配管提效实践指南-AI与PDMS联动探索二-PML审核员硬约束.pdf`（原稿：桌面同名 PDF，图片型 5 页）
> 来源日期：2026-09-07（公众号「配管提效实践指南」，作者：日思夜进，河北）
> 原文能支持什么结论：本节全部条目；哪些是推断：均已标注；下次可以用在哪里：AI 写 PML 前置检查、建语料漏斗、TTY 联调

### 5.1 官方源码漏斗（2937 → 18 → 273KB）

- 源头：PDMSUI 和 PMLLIB 两棵树的 2937 份 PML 官方源码，约 66MB ≈ 1500 万 token，不可能整体塞进 AI 上下文。
- 三层漏斗：
  1. 构建脚本 `_build_index.py` 按 13 类 idiom（使用用法）正则抽取；
  2. 反复验证过的范式提炼成 18 段，写入 `idioms.md`，每段带出处——AVEVA 自己人写 PML 的肌肉记忆；
  3. 索引压成 273KB 的 `corpus_index.tsv`，grep 定位、零 token 加载。
- 使用流程：AI 要写一个对象方法 → 先 grep `corpus_index.tsv` 按关键词定位到 PDMSUI 下某个 pmlmac 文件 → 回到原始源码树 grep 那个函数名 → 照 AVEVA 自己的写法对着写。整库 1500 万 token 零进入上下文。

### 5.2 防猜（与 2.14 同源，补充案例）

AI 会假装懂：遇到不熟悉的 API 会照其他语言的习惯编一个调用，语法挑不出毛病、逻辑也自洽。作者的真实案例：AI 编造的函数在 corpus_index.tsv 和整库源码里都 grep 不到。三步规程见 2.14；审核侧对应 OBJ-01（整库 grep 对名）。

### 5.3 TTY 联调运行时坑（作者实测，已并入 2.13 铁律）

1. `/ref` 是切换当前元素的命令，不是可赋值表达式，不能写进变量。
2. `>` 和 `<` 比较运算符不合法，必须写 `gt` 和 `lt`。
3. 改完 PML 函数后要跑 `PML REHASH ALL` 重建索引，且不能马上接着调用：实测输完命令起码五六秒；AI 两连发会拿到旧/空函数，作者让 AI 等 10 秒左右再测下一个调用。

### 5.4 效果与系列脉络

- 硬约束前置后：以前 30 行函数来回改五六轮不一定过；现在首轮跑通概率大增，剩下的错误是业务逻辑（本就该人来审）。
- 手册不适合直接当 AI 准绳：又大又散、像字典，只列举"有什么、语法怎么写"，不点破具体情境用方法调用还是属性调用。
- 系列：上一篇《联动探索（一）→ 接管 TTY 控制台，AI 写的 PML 全翻车》；本篇立规矩；下一篇预告：让 AI 自己出题、自己判卷、自己优化 skill 的闭环。
- 【推断】`!!CE` 是 PML 内置的当前元素全局对象、`!CE` 只是同名普通用户变量——原文只给频次差，机制未解释（E3D 手册 [P225] 已证实为 DBREF 类型全局变量）。
- 【推断】`q ev !p` 应为 query evaluated 缩写，具体输出形式未展示。

---

## 6. 差异裁决表（已裁决，勿来回改）

| # | 差异点 | 手册事实（第 4 章） | 项目约定（第 2 章） | 裁决 |
|---|---|---|---|---|
| 1 | 表单骨架 | E3D 手册推荐 `layout form`（强制 VarChars），`setup form` 是旧模式 [P276-277] | 骨架模板用 `setup form`（PDMS12 官方源码主流、TM-1402 范式） | **按目标产品定**：PDMS 12.x 项目沿用 `setup form`；E3D 新开发用 `layout form`。审核 FRM 类规则两者通用 |
| 2 | `$*` 注释 | 手册明确 `--` 与 `$*` 均合法、`$*` 可行内 [P197] | PML2 文件禁用 `$*`，`$*` 仅限宏 | **手册层面都对；项目约定从严**：PML2 一律 `--`。审核按第 2 章执行 |
| 3 | 字符串定界符 | E3D 手册只认 `'` 与 `\|` [P198] | PDMS 语料存在反引号式；约定统一 `'..'`（含引号才用 `\|..\|`） | 统一 `'..'`，反引号式不写进新代码 |
| 4 | golabel | 手册记载为合法控制构造（标签≤16字符）[P209] | 官方语料仅 174 次/9000+ 文件，手册明示限制使用 → 约定**新代码禁用** | 合法但禁用；审核 CTL-05 按 Major 打回 |
| 5 | 字符串拼接 | PML2 赋值表达式用 `&` [P202]；PML1 文本表达式用 `+` [P707] | 新代码拼接一律 `&`，`+` 按算术处理（STR-02 Major） | PML2 代码只用 `&`；`+` 仅在 PML1 表达式（报表/规则）语境合法 |
| 6 | `!!CE` 频次数据 | 2937 份语料 11889:416（≈30:1） | 9030 份语料 22462:622（36:1） | 结论一致，引用任一均须注明语料来源 |
| 7 | 条件加括号 | 手册 if 结构示例均带括号 [P204] | 官方 63232 带括号 vs 483 裸写，裸写仅限 `if !val.unset() then` 类单一布尔 | 新代码含运算符一律整体加括号（CTL-03b） |

---

## 7. 下次可以用在哪里 + 维护约定

**用在哪里**：

- AI（包括我）生成或修改任何 `.pmlfnc/.pmlobj/.pmlfrm/.pmlcmd` 前后：第 2 章写码、第 3 章验收，审查意见引用规则编号（R 条目或 CMT/CTL/OPR/VAR/OBJ/PKG/STR/IO/ERR/FRM/RUN 编号）。
- TTY 联调报错：先查 2.13 铁律与 R9/R13；"调用到旧函数/空函数"先怀疑 REHASH 时序。
- 对象方法不确定：2.14 防猜协议 + 3.2-OBJ-01。
- 若用户搭建语料漏斗：5.1 三层结构复刻。

**维护约定**：

- 语法新知（带手册页码）→ 并入第 4 章对应 R 条目；风格/骨架/流程 → 第 2 章；检测手段（配正则与严重度）→ 第 3 章；两来源说法不一 → 第 6 章增补裁决行。
- 《00-学习导航-按需精读.md》与工作区 AGENTS.md 指向本文件，改名/移动需同步。
