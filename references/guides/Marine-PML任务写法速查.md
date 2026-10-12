# Marine PML 任务写法速查(官方 6075 文件频次实证)

> 来源(第 19 轮):按"任务"维度对 PMLLIB 全库统计(`PML语料\_task_idioms.py` → `task_idioms.tsv`,每条含行数/文件数/代表样例)。
> 用法:做某任务前查本表——**首选=官方用得最多的写法**,照抄样例的调用姿势。

---

## 1. 用户反馈

| 任务 | 首选写法 | 频次 | 备选 |
|---|---|---|---|
| 错误/提示/确认 | `!!alert.error/warning/message/confirm('文本')` | **14320 行 / 2496 文件** | `!!messageFile.warning(模块号,消息号)`(1092 行/273 文件,文本在编译的 message.dat,自研勿用) |
| 确认对话取回值 | `!ans = !!alert.confirm('...')` → 'YES'/'NO' | confirm 1085 次 | `!!alert.question`(三键) |

## 2. 收集与遍历

| 任务 | 首选写法 | 频次 | 样例 |
|---|---|---|---|
| 串转 DBREF | `!x = !str.dbref()` | **10000 行 / 1762 文件** | `abaarea.pmlfrm:291` |
| 收集(PML1) | `VAR !x COLL ALL 类型 WITH 条件 FOR 范围` | **2119 行 / 768 文件** | `abaarea.pmlfrm:297`(含 `FOR $!list` 动态范围) |
| 遍历成员 | `do !m values !!ce.members` | ~1986 行(含少量 gadget 同名误计)/475 文件 | 记忆 R16:官方在用 |
| 批量取属性 | `!arr.evaluate(object BLOCK('\|!arr[!evalIndex].attr\|'))` | evaluate 969 行/388 文件 | `abaolddrwgs.pmlfrm:401` |
| 求值命令式 | `VAR !x EVAL NAME FOR ALL FROM !liby` | 713 行/259 文件 | `abaarea.pmlfrm:303-304` |
| 收集(PML2) | `object COLLECTION()` → type/scope/filter/results | 710 行/190 文件 | `accceilingfittings.pmlfrm:815` |
| 收集(MDS 包装) | `!!kcollectallfor(类型, 条件, 范围)` | 457 行/282 文件 | `kclosestpline.pmlfnc:60` |
| 构造空引用 | `object DBREF()` | 2856 行/964 文件 | `abauserview.pmlfrm:1181` |

> **结论**:PML1 `VAR COLL` 行数仍是 PML2 COLLECTION 的 3 倍(2119 vs 710)——官方存量代码偏 PML1 收集;新代码按规范仍用 COLLECTION,但 **`VAR COLL WITH 条件 FOR 动态范围` 表达力更强时可用**(官方大量在用,不算违规)。

## 3. 写库与事务

| 任务 | 首选写法 | 频次 | 样例 |
|---|---|---|---|
| 写 CE 属性 | `!!ce.attr = !val` | **1720 行 / 319 文件** | `abaarea.pmlfrm:534` |
| 提交 | `savework` | 76 行/58 文件(**集中在表单 OK 路径,批量写后一次**) | `abaarea.pmlfrm:364` |
| 回滚 | `GETWORK` / `!!comGetWork()` | 21 行/18 文件 | `adminapplic.pmlfrm:970` |
| 撤销标记 | `MARKDB` / `setUndoable` | 7 / 62 行 | `pos3dexplicit.pmlfrm:187` |
| 申明所有权 | DAC 系列(`!!mdsDacControl`,3573 次,见公共库目录) | — | mds 模块惯例 |

## 4. 交互拾取(EDG)

| 任务 | 首选写法 | 频次 |
|---|---|---|
| 建 EDG 事件 | `object EDGPACKET()` → `!!edgCntrl.add(!packet)` | 656+1342 行 / 285+345 文件 |
| 高亮 | `!!gphDrawlists.createDrawList()` / `.drawlist(n)` | 252 行/45 文件;COMENHANCE 17 文件 |

> **EDG 规模证明**:EDGCntrl.add 1342 行/345 文件——3D 拾取的绝对主流(远超旧 ID@)。

## 5. 文件与 Excel

| 任务 | 首选写法 | 频次 |
|---|---|---|
| 文件操作 | `object FILE(路径)` | 1183 行/353 文件 |
| 整文件读 | `.readFile()` | 223 行/164 文件 |
| 网格导出 | `!!exportToExcel(!grid, 名, 标题)` | 92 行/45 文件 |
| 网格直存 | `!grid.saveGridToExcel(路径)` | 38 行/31 文件 |

## 6. 表单与单位

| 任务 | 首选写法 | 频次 | 备注 |
|---|---|---|---|
| 显示表单 | `show !!form`(636 行/408 文件)vs `.show()`(379/236)vs `loadform`(51/39) | — | show 为主;**reload 前先 loadform** |
| 热更新 | `pml reload form !!x` | 229 行/123 文件(**官方 AppWare 内也写 reload!**) | `abacrhierarchy.pmlfrm:204` |
| 单位判断 | `!!isImperialLength('DIST')` | 175 行/105 文件 | 英制分支的标准开关 |
| 单位换算 | `!!comUnitsConvert(v,'MM','INCH')` | 6 行(封装层,被 comvalueconvert 等转发) | 经由包装使用 |
| 通配过滤 | `!name.matchwild(!filter)` | 994 行/333 文件 | 列表过滤标配;常配 `.not()` 取反 |
| 字符串切分 | `.split(';')[n]` / `.split()` | 1963 行/633 文件 | 指定分隔符不压缩连续分隔 |

## 7. 样例索引

全部 34 个任务的逐条代表样例(文件:行号)在 `PML语料\task_idioms.tsv`——写码前 grep 任务名即可取官方姿势。
