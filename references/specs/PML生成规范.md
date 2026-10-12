# PML 生成规范

> 适用范围：AVEVA PDMS / E3D 12.x 的 PML1（宏）与 PML2（函数/表单/对象）开发。
> 本规范蒸馏自三个来源，每条规则均有出处：
> 1. AVEVA 官方源码实证统计：PDMS12.0.SP6 的 `PDMSUI` + `PMLLIB` 两棵源码树（9030 份文件，其中 pmlfnc 3030 / pmlfrm 1878 / pmlobj 1591 / 宏 268），官方代码即"真跑过、不会错"的标准样本；
> 2. 官方培训文档：TM-1401《Programmable Macro Language Basic》、TM-1402《PML Form Design》《Advanced PML》；
> 3. 实战经验（《AI 与 PDMS 联动探索》一/二）：AI 写 PML 的高频翻车点与 TTY 联调运行时坑。
>
> 配套文件：《PML审核规范.md》是本规范的检查清单形式，用于代码评审与 AI 生成代码的验收。

---

## 1. 文件组织与装载机制

### 1.1 两种语言两代结构

| | PML1（遗留） | PML2（现行，**必须用**） |
|---|---|---|
| 存放 | `PDMSUI` 环境变量指向的目录树 | `PMLLIB` 环境变量指向的目录树 |
| 文件类型 | `.mac` 宏、旧式表单 | `.pmlfnc` 函数、`.pmlfrm` 表单、`.pmlobj` 对象 |
| 调用方式 | 同义词（synonym）或 `$m/路径/文件` | 函数 `!!name()`；表单 `show !!name`；对象 `!x = object NAME()` |
| 装载 | 手动/同义词触发 | PDMS 启动时自动建立索引，首次使用时动态加载 |

实证：官方 PML2 文件中 `define method` 出现 4.1 万次、`gosub` 为 0 次——**新代码一律 PML2，禁止写 PML1 式宏逻辑**。

### 1.2 平行目录原则

**禁止修改 AVEVA 标准产品的任何文件**（官方手册原话：改动可能导致 PDMS 行为异常）。定制代码必须放在平行目录树，并把路径前置到环境变量：

```bat
Set PMLLIB=C:\myproject\pmllib %pmllib%
Set PDMSUI=C:\myproject\pdmsui %pdmsui%
```

- 自定义路径放 `%pmllib%` **前面**，先搜到先生效，实现"覆盖式定制"而不动原文件。
- 在 PDMS 内用 `q evar pmllib` / `q evar pdmsui` 验证路径顺序。

### 1.3 装载维护命令

| 场景 | 命令 |
|---|---|
| 新建了 pml 文件 | `pml rehash`（重建第一个搜索路径索引）或 `pml rehash all`（全部路径） |
| 修改了已加载的表单 | `pml reload form !!Name` |
| 修改了已加载的对象 | `pml reload object NAME` |

**运行时铁律**：`PML REHASH ALL` 执行后索引并未瞬时建好。人工敲命令天然有几秒间隔，但脚本/AI 连发命令会拿到旧索引甚至空调用。**重建索引后必须等待约 10 秒再发起下一次函数调用**。

### 1.4 文件即定义

- 一个 `.pmlfnc` 定义一个同名函数；一个 `.pmlfrm` 定义一个同名表单及其方法；一个 `.pmlobj` 定义一个同名对象及其方法。
- 文件名（小写）与内部定义名必须对应（如 `addconnected.pmlfnc` 内 `define function !!addConnected()`），否则动态加载找不到。

---

## 2. 命名规范

### 2.1 变量

| 项 | 规则 | 依据 |
|---|---|---|
| 局部变量 | 单叹号前缀：`!name` | TM-1401 §4.2 |
| 全局变量 | 双叹号前缀：`!!name` | 官方源码：全局变量前 25 名全部 `!!` 开头 |
| 当前元素 | **只写 `!!CE`**，不写 `!CE` | 官方源码 `!!CE` 22462 次 vs `!CE` 622 次（36:1） |
| 长度/字符 | ≤64 字符，仅字母数字，**不得以数字开头，不得含 `.`** | TM-1401 §4.2 |
| 大小写 | PML 不区分大小写；按 camelCase 书写提升可读性 | 官方源码风格 |

### 2.2 函数 / 表单 / 对象 / 方法

- 全局函数、全局表单：`!!camelCaseName`（如 `!!addConnected`、`!!aidceArrow`）。
- 自定义对象类型：全大写（如 `MODULEDATACACHE`、`COLLECTION`）。
- 方法与成员：点号前缀 camelCase（如 `.append`、`.moduleData`、`.ceArrowStat`）。
- 构造函数与所属表单/对象同名（`define method .aidceArrow()` 是 `!!aidceArrow` 的构造器）。

### 2.3 表单 gadget 命名前缀（官方约定）

| 前缀 | 控件 | 前缀 | 控件 |
|---|---|---|---|
| `fme` | frame | `tgl` | toggle |
| `txt` | text 输入框 | `opt` | option 下拉 |
| `btn` | button | `lst` | list |
| `para` | paragraph 文本 | `cbo` | combo |

示例（官方 `aidcearrow.pmlfrm`）：`frame .fmeceArrow` → `toggle .tglCeArrow` / `text .txtHeight` / `option .optPosition`。

---

## 3. 注释规范

| 场景 | 写法 | 禁止 |
|---|---|---|
| PML2 文件（.pmlfnc/.pmlfrm/.pmlobj） | `-- 注释内容` | ~~`! 注释`~~（`!` 是变量前缀，直接解析异常）、~~`//`~~、~~`#`~~ |
| PML1 宏（.mac/.pmlmac）行内/整行注释 | `$* 注释内容` | 同左 |

实证：官方源码 `--` 注释行共 91.9 万行——**注释密度是官方文化的一部分**，照此标准写。

### 3.1 文件头模板（PML2 文件必须携带）

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

### 3.2 方法头模板（每个 `define method` 前必须携带）

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

---

## 4. 变量与类型系统

### 4.1 四种基本类型

`STRING`、`REAL`、`BOOLEAN`、`ARRAY`；另有 `DBREF`、`POSITION`、`ORIENTATION`、`BLOCK`、`FILE`、`COLLECTION` 等对象类型（官方实例化频次前 12：DBREF 2873 / ARRAY 2443 / BLOCK 1576 / LINE 1319 / COLLECTION 1306 / FILE 874 / ORIENTATION 773 / POSITION 739）。

### 4.2 PML1 与 PML2 赋值的本质区别

```
VAR !x (64)      ← PML1：!x 是 STRING（VAR 语法只存字符串）
!x = 64          ← PML2：!x 是 REAL，类型由内容自动推导
```

**新代码只用 PML2 赋值**。类型由内容推导：`42`→REAL，`|abc|`→STRING，`TRUE`→BOOLEAN，`ARRAY()`→空数组。

### 4.3 BOOLEAN 规则（高频翻车点）

- 合法布尔常量：`TRUE FALSE YES NO T F Y N`（**不带引号**）。
- 非法判断：`if ( 1 )`（REAL 不是布尔）、`if ( |TRUE| )`（STRING 不是布尔）。
- 转换规则（`.boolean()` 方法或 `$` 前缀兼容判断）：REAL 0→FALSE，其余→TRUE；字符串 `'TRUE'/'T'/'YES'/'Y'`（大小写均可）→TRUE，`'FALSE'/'F'/'NO'/'N'`→FALSE。
- PML1 兼容：字符串变量加 `$` 前缀可参与 if 判断：`if ($flag) then`。

### 4.4 数组

- 数组无需预声明，给元素赋值即创建：`!x[1] = |ABCD|`；多维数组 = 元素再赋数组。
- 遍历用 `do !v values !arr`（取值）或 `do !i index !arr`（取下标 1..N）。

### 4.5 `q var` 是查询不是声明

`q var !x` 只是**打印**变量值的调试命令，绝不产生声明或赋值效果。声明/初始化用 `!x = ...` 或 `!x = real()` / `string()` / `ARRAY()`。

---

## 5. 运算符与表达式

### 5.1 词运算符（PML 没有符号比较符）

| 类别 | 合法 | 禁止 |
|---|---|---|
| 比较 | `EQ NE GT LT GE LE` | ~~`==` `!=` `>` `<` `>=` `<=`~~ |
| 逻辑 | `AND OR NOT` | ~~`&&` `||` `!`~~ |
| 算术 | `+ - * /` | — |
| 数学函数 | `SIN COS TAN SQR POW NEGATE ASIN ACOS ATAN LOG ALOG ABS INT NINT` | — |

TTY 实测：`>` `<` 直接报语法错误，无任何兼容模式。

### 5.2 优先级（从高到低）

```
()  →  * /  →  + -  →  EQ NE GT LT GE LE  →  NOT  →  AND  →  OR
```

**不要赌优先级，复合条件一律加括号。**

### 5.3 `$` 展开（在 PDMS 命令行/命令嵌入中使用）

| 写法 | 含义 | 实证频次 |
|---|---|---|
| `$!var` | 展开变量值（嵌入命令行） | 24858 次，主流 |
| `$!<表达式>` | 展开表达式（如 `$!<this.ceArrowHeight>`） | 459 次，按需 |
| `$!x` 前缀强制 | 把 REAL 强制为 STRING 参与字符串比较：`IF($!x eq !y)THEN` | 类型桥接手段 |
| `$p 文本` | 打印到命令行 | 调试/日志标准手段 |
| `$m/路径/文件` | 调用宏文件 | 宏入口 |
| `$1..$9`、`$d1` | 宏位置参数/具名参数 | 仅宏内 |

### 5.4 字符串

- 三种定界符均合法：`` `xxx' ``、`|xxx|`、`'xxx'`。官方实证：单引号式 15.4 万次 vs 竖线 2.7 万次——**新代码统一用 `'..'`**，字符串内含单引号时才用 `|..|`。
- 拼接用 `&`（自动把操作数转 STRING）：`!c = !a & !b & |mm|`。
- 字符串是对象，方法可链式调用：`!line.upcase().split().sort()`。

---

## 6. 控制流

### 6.1 合法结构速查

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

### 6.2 控制流禁令

- 禁 `loop ... endloop`、`for`、`while`、`switch`——PML 不存在这些关键字。
- 禁 `gosub`（官方源码 0 次使用）。
- `golabel /label` + `label /label` 官方全套源码仅 174 次且手册明示"应限制使用，降低可读性"——**新代码禁用**，用函数/方法拆分代替。标签名 ≤16 字符（不含 `/`）。
- 一个 IF 结构内只能有一个 `ELSE`。
- 开放 `do ... enddo` 若无可达的 `BREAK IF` 条件 = 死循环，禁止；需要上限时改 `do !i from 1 to N`。

---

## 7. 错误处理与用户反馈

### 7.1 handle 块

可能出错的 PDMS 命令（建元素、改属性、导航）一律包 handle 块。官方源码 `endhandle` 出现 16060 次——这是官方标准动作，不是可选装饰。捕获码形如 `(41, 8)`：`模块号, 错误码`，从报错信息 `(41,8) ERROR - ...` 中读取。

### 7.2 Alert 对象（官方实证频次）

| 方法 | 用途 | 次数 |
|---|---|---|
| `!!alert.error( '...' )` | 错误弹窗 | 5073 |
| `!!alert.warning( '...' )` | 警告 | 2022 |
| `!!alert.confirm( '...' )` | 确认，返回 `'YES'/'NO'` | 1066 |
| `!!alert.message( '...' )` | 提示 | 1063 |
| `!!alert.question( '...' )` | 询问，返回 `'YES'/'NO'/'CANCEL'` | 104 |
| `!!alert.input( '提示', '默认值' )` | 输入，返回字符串 | 30 |

可用第 2、3 参数按屏幕比例定位弹窗（0.25, 0.1）。

---

## 8. 数据库访问与遍历

### 8.1 当前元素

- `!!CE` 是全局 DBREF 对象，永远指向当前元素，成员=属性：`!!CE.Hbore`、`!!CE.Pos.Up`。
- 可反向写属性：`!p = !!CE.Pos` → `!p.Up = 2000` → `!!CE.Pos = !p`。
- `/ref`、`/name` 等是**导航命令**，不是可赋值表达式，**不能写进变量**。遍历场景在循环体内导航：`do !p values !zone.members` 后用 `$!p` 或 `q ev !p`。

### 8.2 元素收集：优先 PML2 COLLECTION 对象

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

### 8.3 遍历子元素

```
do !m values !!ce.members
  ...
enddo
```

禁止凭其他语言经验编造 `.MEMBERS('X', c)` 之类的调用——对象成员/方法名必须在《Software Customisation Reference Manual》或官方源码中查证（见第 14 节防猜协议）。

---

## 9. 函数开发规范（.pmlfnc）

标准骨架（官方实证模板）：

```
<文件头，见 §3.1>
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

## 10. 对象开发规范（.pmlobj）

```
<文件头 + Methods defined 清单>
define object MYTYPE

  member .items is ARRAY
  member .name  is STRING

endobject
-- End of object definition for MYTYPE

<方法头，见 §3.2>
define method .append(!data is MYTYPE)
  !this.items.append(!data)
endmethod
-- End of method definition for .append(MYTYPE)
```

规则：
- 对象类型名全大写；`member .x is TYPE` 集中声明在 `define object` 块内。
- 方法内用 `!this.member` 访问成员；方法可重载（同名不同签名，官方 `moduleData()` / `moduleData(STRING)` 实证）。
- 实例化：`!x = object MYTYPE()`；禁止假设未查证的构造函数参数。

## 11. 表单开发规范（.pmlfrm）

### 11.1 标准骨架

```
<文件头 + Methods defined 清单>
setup form !!myForm dialog resizeable        ← 形态修饰见 §11.2

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

### 11.2 表单形态（setup 行修饰符）

| 写法 | 效果 |
|---|---|
| `dialog dock left` | 停靠左侧 |
| `dialog resizeable` | 浮动可缩放 |
| `document at xr 0.5 yr 0.5 size 100 100` | 居中定尺寸 |
| （无修饰） | 默认 dialog，按内容自动尺寸 |

选型规则：有 OK/Cancel 的表单不做停靠；**带 menubar 的表单不能停靠**。

### 11.3 回调约定

- 表单级特殊回调成员：`initcall` / `okcall` / `cancelcall` / `quitcall`，赋字符串：`|!this.okCall()|`。
- 控件回调：`.callback = '!this.method()'`，回调体是**字符串**，写错不会报编译错，只在点击时炸——审核必查。
- 控件读写：`.val` 取值/赋值；`.active` 置灰；`.dText` 设下拉/列表内容（赋 ARRAY）；`.select('RTEXT', !val)` 回显选中。

### 11.4 显示/隐藏

`show !!form`（加载并显示）、`loadform !!form`（只加载）、`!!form.show()` / `.hide()` / `.shown()`。

### 11.5 单位处理（官方范式）

涉及长度输入必须区分 mm/inch（官方实证写法）：查当前单位 `var !u split units` → `!u[3].upcase().eq('MM')`；内部存储**统一毫米**，inch 会话在输入时 `* 25.4` 换算、显示时除以 25.4。输入框配 `format !!distanceFmt` 跟随系统精度。

## 12. 命令嵌入与宏

- 在 PML 代码中直接写 PDMS 命令行（如 `AID CEARROW ON`、`NEW EQUI /ABCD`）是合法且主流的官方做法，变量用 `$!var` / `$!<expr>` 嵌入。
- 宏参数：`$1..$9` 位置参数、`$d1=xxx` 具名参数；调用 `$m/path/file.mac`。
- 宏内注释用 `$*`；PML2 文件内禁止出现 `$*` 注释风格。

## 13. 运行时与调试铁律

1. `pml rehash all` 后**等待约 10 秒**再调用任何函数/表单（索引异步建立）。
2. `> / < / == / !=` 直接语法错误，没有例外。
3. `q var !x` 只用于调试打印，不是声明。
4. TTY 调试输出统一用 `$p`；弹窗反馈用 `!!alert.*`。
5. 导航命令（`/ref`、`next`、`owner` 等）是命令不是表达式，不得赋给变量。
6. 函数/对象/表单被加载后其定义被 PDMS 持有，改文件必须 `pml reload` 对应实体，否则跑的是旧定义。

## 14. 防猜协议（对 API 不确定时的强制流程）

实证教训：最危险的不是语法错（当场报错），而是 AI/人**编造一个语法自洽但库里不存在的 API 调用**。因此凡涉及不常用对象方法/成员/命令，必须按顺序执行：

1. **查手册**：《Software Customisation Guide》《Software Customisation Reference Manual》对应对象条目，确认方法名、参数、返回类型、MODIFIES/NO RESULT 语义。
2. **对源码**：在 PMLLIB/PDMSUI 官方源码树中 `grep` 该函数/方法名，抄 AVEVA 自己的真实用法（调用姿势、参数形式、上下文）。
3. **都查不到 → 显式标注不确定**：在代码上方加 `-- TODO-UNVERIFIED: <疑点描述>，需人工确认`，并在提交说明中列出，**禁止假装确定、禁止静默通过**。

---

## 附录 A：八大类禁止清单（AI 高频翻车对照表）

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

## 附录 B：关键实证数据备查

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
