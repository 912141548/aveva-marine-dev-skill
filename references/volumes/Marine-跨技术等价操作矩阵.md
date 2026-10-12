# Marine 跨技术等价操作矩阵（卷十二·综合索引）

> 综合【卷一至卷十一】全部源码实证，把同一操作在 **PML 命令宏 / PML2 / marAPI(PML互操作) / .NET Addin / Vitesse Python** 五条轨道上的写法并排对照。
> 每格注明出处卷号，写法本身回查对应卷文档；本卷不引入任何未经前十一卷实证的新 API。

---

## 1. 五轨道总览与选型决策

| 轨道 | 入口 | 强项 | 弱项 | 出处 |
|---|---|---|---|---|
| PML 命令宏（PML1 + 命令嵌入） | `$m` / 宏文件 / `$!var` 嵌入 | 零部署、批处理 TTY 友好、官方宏生成器范式（rtrpidprocess） | 无面向对象、字符串拼接易错 | 卷三§4、卷一§14 |
| PML2（.pmlfnc/.pmlfrm/.pmlobj） | `!!func()` / `object X()` / `show !!form` | 面向对象、UNDOABLE、COLLECTION、与全部 PDMS 命令互通 | 无继承/私有 | 卷一~卷十一全部 |
| marAPI（PML 侧 .NET 互操作） | `import 'marAPI' + using namespace + object XXX()` | Hull 语句引擎、Draft 出图、数据抽取（MARDEX） | 需 handle(1000,0)、类型受限（Double 重载） | 卷七§2.10/§5 |
| .NET Addin（C#） | IAddin + ServiceManager + uic | 停靠窗、复杂 UI、事件、PMLNet 双向 | 部署链复杂（uic/ADDIN） | 模板②、Cookbook、uic 手册 |
| Vitesse Python 2.6 | PYTHON 命令 / 菜单 / 触发器 / _TBhook_ | Hull 语句（kcs_hullpan）、Draft 图元（kcs_draft 180 函数）、数据抽取（kcs_dex） | Py2.6、GUI 用 wxPython2、无 PML 对象访问 | 卷八全卷 |

**选型一句话**：船体建模语句走 marAPI/kcs_hullpan；Draft 图元走 kcs_draft 或 marAPI.MARDRAFTING；界面走 PML2 表单（简单）或 .NET 停靠窗（复杂）；批处理走 TTY 宏；数据抽取走 MARDEX/kcs_dex。

---

## 2. 任务 → 技术等价矩阵

### 2.1 元素创建

| 轨道 | 写法 | 出处 |
|---|---|---|
| PML 命令 | `NEW EQUI /NAME`、`NEW $!<type> BEFORE 1`（变量式管件） | 卷一§1、卷三§3.1 |
| PML2 | `!undo = object UNDOABLE(); !undo.description(...); !undo.add(); NEW PIPE; ...; !undo.endUndoable()` | 卷三§7.4 |
| Vitesse | `kcs_modelstruct.block_new(name,min,max)`、`kcs_struct.struct_activate(name)` → 建模 → `struct_save()` | 卷八§6 |
| Hull 语句 | `MARHULLPAN.stmtExec(0, "PAN, 'X', SP, DT=301, Z=...;")` / `kcs_hull.pan_exec_stmt(0, stmt)` | 卷七§2.1/§2.10 |

### 2.2 连接/断开

| 轨道 | 写法 | 出处 |
|---|---|---|
| PML 命令 | 六种标准变体 `CONNECT PH TO PT of HREF` 等；断开 `HREF nulref`；降级 `FCONN` + MOVE 最小管长 | 卷三§2.1-2.3 |
| PML2 对象 | `BRANCHCONNECTION.connect(!element, 'P<n>')`（P 点连接唯一入口） | 卷三§2.4 |
| Vitesse | `kcs_cable`/`!cwayObject.pick('CONNECT')`（电缆域）；`kcs_hullpan.stmt_exec` 内 `CON=15` 端切码（Hull 域） | 卷三§2.5、卷七§2.4 |

### 2.3 属性读写

| 轨道 | 写法 | 出处 |
|---|---|---|
| PML2 直写 | `!!ce.spref = !spec`（296 名频次表）；读 `!x = !!ce.hbore` | 卷五§1a |
| UDA 命令式 | `:MDSSuppType 'TT04'`；复位 `:MDSConn default`（四关键字） | 卷五§2a |
| UDA 成员式 | `!o.:PsiSystem[1] = !val`；读 `!x = !o.:mdsguideref` | 卷五§2b |
| UDA 定义 | `NEW UWRLD → NEW UGROUP → NEW UDA + UDNA/UTYP/ULEN/ABLE/ELEL/DFLT` | 卷五§2c |
| 命令读取 | `var !x EVAL attr for all from !arr`、`var !x :uda of $!e`、类型化 `var !d CLOCK DATE` | 卷五§4、卷十一§8.5 |
| .NET | `dbRef.GetAttr/...`（Cookbook §DBRef 族）；PML 属性经 PMLNet 序列化 | Cookbook |
| Vitesse | `kcs_att.attribute_create/string_set/integer_get/real_get` + `kcs_att_<Group>` 组模块 | 卷八§6 |

### 2.4 元素收集/遍历

| 轨道 | 写法 | 出处 |
|---|---|---|
| PML2 COLLECTION（新代码首选） | `!coll = object COLLECTION(); !coll.type(...).scope(!!ce).filter(object EXPRESSION(...)); !r = !coll.results()` | 规范§8.2 |
| VAR COLLECT（文本式，110 处） | `var !x collect all SCTN with (...) for CE / from !arr / from CLAIMLIST EXTRACT / members of` | 卷十一§8.2 |
| 批量求值 | `!arr.evaluate(object BLOCK('...'))`（206 处）+ 预构建 BLOCK 复用 | 卷五§7 |
| Vitesse | `kcs_db.object_list_get(criteria, dbname, list)`（配 ObjectCriteria） | 卷八§6 |

### 2.5 规格选型

| 轨道 | 写法 | 出处 |
|---|---|---|
| 命令 | `var !c CHOICE WITH $!spec` → `SELECT with $!str`；`SELECT WITH SPEC $!spec`；重选 `RESELECT WITH SPEC` | 卷三§3.3 |
| PML2 对象 | `object SPECIFICATION(dbref)` → loadComponents/loadBores/loadTable/subTypes → `components(type,questions,answers)` | 卷四§5.5 |
| 选择表 | `object SELECTIONTABLE(); createTable/newType/newQuestion/newItems; chooseItems(...)` | 卷四§4.1-4.2 |
| 匹配算法 | SPCSPECIFICATION.choose：TEXT findFirst / BOOLEAN / RANGE `between(answer,maxAnswer)` | 卷四§5.4 |
| 设计侧窗体骨架 | SPCLINK + SPCSEARCH + SPECDATA 四成员（21 窗体同构） | 卷四§5.6 |

### 2.6 Draft 图纸

| 轨道 | 写法 | 出处 |
|---|---|---|
| 命令 | `NEW DRWG → NEW SHEE → NEW VIEW → NEW LAYER`（全属性链）；`DRAWING/SHEET/VIEW/LAYER` 导航 | 卷二全卷 |
| isometricadp | `object ISODRWG(!ref,!update).create()`（DRWG→SHEE→VIEW→REVI→NOTE→SYMB 全链） | 卷六§3.4 |
| Vitesse | `kcs_draft.dwg_new/open/save/print/dxf_export` + 图元 `text_new/line_new/dim_linear_new` 等 31 种 | 卷八§3.1/3.8 |
| .NET | WindowManager/marAPI MARDRAFTING（模板④） | 模板④ |

### 2.7 Isodraft 出图

| 轨道 | 写法 | 出处 |
|---|---|---|
| 交互 | `ISODRAFTMODE` → 选项 `$M` → `DETAIL $!type $!name` → `var !s isodraw status` | 卷六§1.2/3.3 |
| 批处理 TTY | 写宏（`ISODRAFT` + `detail` + `FINISH`）→ `"...\MON" tty -noconsole -macro=...` | 卷六§3.2 |
| 输出控制 | `FILE "$!name" SINGLE`、`FILE AND DXF`、`MatlistFile`、`PLOT $!sheet PDF "$!file" ...` | 卷六§3.5 |

### 2.8 Hull 建模

| 轨道 | 写法 | 出处 |
|---|---|---|
| PML + marAPI | `stmtExec/stmtExecSingle/stmtGet/groupGet` + `panModify/panRecreate/panStore`（19 方法） | 卷七§5 |
| Vitesse | `kcs_hullpan.pan_init/stmt_exec/pan_store/pan_activate/split/move/copy`（22 函数）；`kcs_chm` 曲面族 | 卷七§3/§4 |
| DB 级 | `new GBLOCK/BLOCK/OBJHD/GOBELE`（分段）、`new RAWPLA`（原材料板）、`new SOLI/SOLEXT/TDEN/SDEN`（材质） | 卷七§1.2 |

### 2.9 交互拾取

| 轨道 | 写法 | 出处 |
|---|---|---|
| EDG（PML） | EDGPACKET → edgCntrl.add；pick.input 过滤；`kcs_hullpan` 侧 `MARUI.pointPlanarReqPML` | EDG 精要、卷七§5 |
| Vitesse | `kcs_ui.point3D_req/req_pick_mod/point2D_req`（配 Stat/CursorType/ButtonState） | 卷八§2 |
| .NET | 命令系统 + gphViews 对象（`rotate/limits/clipbox` 全族） | 卷十一§2.4 |

### 2.10 用户反馈

| 场景 | PML | Vitesse | .NET |
|---|---|---|---|
| 错误弹窗 | `!!alert.error(...)`（5073 处） | `kcs_ui.message_confirm` | MessageBox |
| 命令行提示 | `$p 文本` | `kcs_ui.message_noconfirm` / `message_debug` | — |
| 确认 | `!!alert.confirm → 'YES'/'NO'` | `kcs_ui.answer_req` → `kcs_util.yes()/no()` | — |
| 输入 | `!!alert.input('提示','默认')` | `kcs_ui.string_req/real_req/int_req` | — |
| 消息文件 | `!!messageFile.warning(模块号,消息号)`（编译 message.dat） | — | — |

### 2.11 错误处理范式

| 轨道 | 写法 | 出处 |
|---|---|---|
| PML | `handle (61,721) ... elsehandle ANY ... elsehandle NONE ... endhandle`（16060 处 endhandle） | 规范§7.1 |
| Vitesse | `try/except + ReportTribonError(module)`；error 可写注入 `'kcs_<Name>'`；TbBaseException(strFunctionName/strModuleName/strError) | 卷八§10 |
| .NET | try/catch + 日志（模板②自记日志模式） | 模板② |
| Hull 语句 | `handle(1000,0)` 忽略已导入；`(2,441)` 语法错；`(7,3)` connect 失败回退 fconnect | 卷七§8、卷十§1.6 |

### 2.12 事务/撤销

| 层级 | 写法 | 出处 |
|---|---|---|
| 命令级 | `MARKDB` / `MARKDB CLEAR` / `UNDODB 1` / `REDODB 1`（undoroute 范式） | 卷三§1.4/§7.4 |
| 回调级 | UNDOABLE 对象（description/add/endUndoable/undoaction/redoaction） | 卷三§7.4、卷十§2.3 |
| 全局通知 | `!!postEvents` | 规范修订 2.2 |
| Vitesse | `kcs_pipe.pipe_save()/cancel()` 等激活-保存-取消三段 | 卷八§6 |

### 2.13 批处理/无头运行

| 轨道 | 写法 | 出处 |
|---|---|---|
| TTY 宏 | 写登录宏 → `"...\MON" tty -noconsole -macro=...`（PF/pfmergespools 范式） | 卷九§9、卷六§3.2 |
| PML 内生成宏 | FILE.writeRecord 逐行 + `$M "$!macro"` 执行 + deleteFile（rtrpidprocess 范式） | 卷三§4 |
| RUNBATCHPROCESS | `import 'PipeFabricationAddin' + object RUNBATCHPROCESS()`，失败 `SYSCOM 'START /MIN cmd.exe /C ...'` | 卷九§9 |
| Vitesse | `PYTHON 脚本名` 命令行 / 触发器 / _TBhook_ | 卷八§9 |

### 2.14 数据抽取（DEX）

| 轨道 | 写法 | 出处 |
|---|---|---|
| PML | `MARDEX.extractPML/nextResultPML/getIntPML/getReal/getString/getBox/getIndexedReal` | 卷七§6 |
| Vitesse | `kcs_dex.extract/next_result/get_int/get_real/get_string/get_reavec3d/get_box/get_indexedreal`（类型码 1-6/>10/≥25） | 卷八§4 |
| 表达式 | `"HULL.PANEL('N').BOUNDARY(i).COR"` 等全表 | 卷七§6 |

### 2.15 文件/Excel/报告

| 轨道 | 写法 | 出处 |
|---|---|---|
| PML | `FILE.open('OVERWRITE')/writeRecord/close/deleteFile`；宏文本数组执行 | 卷三§4 |
| PML→Excel | NETGRIDCONTROL/NETDATASOURCE（ISOPARTSLIST.saveToExcel 范式） | 卷六§6 |
| Vitesse | Python `open()` + xml.dom（PyXML PrettyPrint） | 卷八§0、kcs_ex_hull_XML |
| 批量打印 | PrintOptions 32 方法 + `dwg_print` | 卷八§8.3 |

### 2.16 权限/工作共享

| 轨道 | 写法 | 出处 |
|---|---|---|
| 命令 | `CLAIM CE [MEM [HIERARCHY]]` / `EXTRACT CLAIM` / `UNCLAIM ALL`；DDL `CREATE DB ... CLAIM <mode>` | 卷十一§3 |
| 状态读取 | `!!ce.okClaim/.lclm`、`!db.claim`、ENHANCE 高亮 claim | 卷十一§3.3 |
| 写保护 | `comcheckdbwrite.pmlobj .checkDBwrite(DBREF)`；`dbwrite ne true` 检查 | 卷十一§3.3、卷四§2.1 |

### 2.17 命名服务

| 轨道 | 写法 | 出处 |
|---|---|---|
| 内置 | `!!autoNameCE(TRUE/FALSE)`（CE 本体/含子代） | 卷十一§4.1 |
| 校验 | `!!checkName(!name, 'NEW'\|'OLD')`（*/^/~ 通配、USENAME 占用） | 卷十一§4.2 |
| 规则引擎 | `object NAMOPT(); nameString(element,key,check,wildCard)`；规则文件 `$m` 执行 | 卷十一§4.3 |
| 自定义 | Design Reuse 35 类 build*name 构造器；ABA `NAME $!name/V$!x` 循环命名 | 卷十§9.2/§5.3 |

### 2.18 图形辅助/高亮

| 轨道 | 写法 | 出处 |
|---|---|---|
| AID | `AID ARROW/BOX/SPHERE/... NUMBER n ...`（9 族全变体）+ 预定义号段管理（AIDNUMBERS） | 卷十一§1 |
| Drawlist | `ADD/REM CE [COLOUR x]`、对象化 `!drawlist.add(!element)` | 卷十一§7 |
| ENHANCE | `ENHANCE CE WHERE (...) FROM DRAWLIST COLOUR $!c`（claim 高亮范式） | 卷十一§3.3 |
| Vitesse | `kcs_ui.init_highlight`、HighlightSet（AddGeometry2D/3D/AddModel） | 卷八§2/§8.2 |

### 2.19 批量属性清除

| 轨道 | 写法 | 出处 |
|---|---|---|
| 标准范式 | `EXTRACT CLAIM $!dbRef → CLAIM → !!ce = dbRef → 循环执行 $!属性名 $!复位关键字 → delete` | 卷五§5c |
| PML2 禁忌 | `!!ce.x = unset` **0 处**（审计规则 P2-RESET-01 已拦截） | 卷五§5b |

### 2.20 互操作桥

| 方向 | 机制 | 出处 |
|---|---|---|
| PML → .NET | `import 'marAPI' + handle(1000,0) + using namespace + object CLASS(args)`；PMLNetCallable 类 | 卷七§5 |
| .NET → PML | `PMLNetDelegate.PMLNetEventHandler` 事件、`runPMLFunction` 类 API | Cookbook |
| 宏 → PML | 宏内直接写 `!!func()` / `!x = object X()`（PML1↔PML2 var 桥） | 规范§12 |
| PML → 宏 | `$M "$!file"`、宏文本数组逐行 writeRecord 后执行 | 卷三§4 |
| Vitesse → DB | kcs_* 全族（激活-保存-取消三段事务） | 卷八§6 |
| Marine ↔ Hull | MarWrapper WORKSPACE 同步检查（moduleswitch 内） | 卷十一§5.2 |

---

## 3. 性能与规模要点

1. **收集**：新代码 COLLECTION（返回 DBREF 保类型）；文本 VAR COLLECT 仅作查询拼接；两者都配 `.evaluate(object BLOCK())` 批量取属性，避免循环内逐条 `var ... of`。
2. **Hull 语句**：整段语句拼接后一次 stmtExec，勿逐关键字调用；组号语义（0=追加、2=PAN、3=SUR）勿硬编码——用 `groupGet(name, partId)` 反查。
3. **TTY 批处理**：宏首行 `!oldCe = !!ce` 保存、末行恢复；每步命令带 handle 落日志（rtrWriteLog 范式）。
4. **UNDO 包裹**：交互创建用 UNDOABLE；批处理用 MARKDB + UNDODB n（步数=层次深度）。

## 4. 本矩阵使用方式

- 查到任务类型 → 定位本章 §2.x → 取目标轨道写法 → 回出处卷文档核对参数与 handle 码 → 按 SOP（AVEVA开发工作流一页纸.md）编码与审计。
- 五轨道写法不一致时的裁决：源码实证 > 手册 > 归纳；全部出处见各卷文档头部来源声明。
