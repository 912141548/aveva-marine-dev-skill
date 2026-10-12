# Marine PML 错误码速查(官方源码 330 码实证 + 第 81-86 轮九卷域化增补)

> 来源(第 18 轮):官方 PMLLIB 全库 **330 种 handle 码**的块内 alert 文本自动配对(`PML语料\_extract_errorcodes.py` → `errorcode_semantics.tsv`,每条语义都可在该文件回查出处);模块号表来自官方 `common\objects\msgmodules.pmlobj` + `commonmsgfiles.pmlfnc` 实文。
> 增补(第 87 轮):第 81-86 轮九卷穷举新实证的 **60+ 码**按域分组入 §5(Router/Isodraft/Spooler/规格/工作共享/船体),模块号新确认 17/33/39/62 四个归属——原 TODO-UNVERIFIED"高号段模块归属"部分关闭。
> 用法:写 `handle (m,c)` 前先查本表——**码值必须与运行时报错一致**(报错头 `(模块,码) ERROR - ...`),拿不准就先触发一次真实错误读码。

---

## 1. 模块号(第一段)对照

| 模块号 | 含义 | 证据 |
|---|---|---|
| 1 | General 通用(gen01) | commonmsgfiles.pmlfnc |
| **2** | **Database 数据库/导航**(db02) | 同上 + (2,109) 全是元素缺失类 |
| 3 | Admin(adm03) | 同上 |
| 4 | List 维护(lst04) | 同上 |
| 5 | EDG(edg05) | 同上 |
| 7 | Positioning & Orientation(posori07) | (7,3)=连接类型不兼容,吻合 |
| 8 | Graphical views(gph08) | 同上 |
| 10 | Checker(chk10) | 同上 |
| 11 | Spec(spec11) | 同上 |
| 12 | Rule(rule12) | 同上 |
| 46 | PML 解释器 | (46,28) Variable not defined(记忆 R9) |
| 17 | 规格复制(speconmode 域) | (17,19) new spec COPY RENAME 失败(catupgradespec.pmlobj:492)——卷四 |
| **33** | **Isodraw 出图引擎** | (33,157) DETAIL 出图失败(pfIsoDrawingManager:171)——卷六/卷九 |
| **39** | **MDB 会话** | (39,15) 无 MDB(moduleswitch)——卷十一 |
| **62** | **Router 约束查询** | (62,707) ICONS POINT LEAV 不存在(rtrpointdetails:60)——卷三 |
| 61 | F&M/图形视图 | (61,528)/(61,115) 官方文本 |
| 160 | FILE 对象 | Guide ch11 错误码表 |
| 1000 | PMLNet 桥 | TM-1402 PMLNetException(1000,1,…) |
| 41/42/43/44/47/64/73/83/99… | F&M/应用层(域化语义见 §5 实证表) | 高频但官方文档未载模块表 |

## 2. 高频码语义表(按语料使用频次;语义取自官方块内 alert 原文)

| 码 | 块数 | 语义(官方 alert 原文归纳) | 常见场景 |
|---|---|---|---|
| **(2,109)** | 803 | 元素/引用不存在类:"Support Datum does not exist" | `new` 元素、引用属性取值前 |
| **(61,528)** | 505 | **用户从子模式退出(ESC)**——光标函数/点取被取消 | 交互点取循环的标准退出捕获(id @ + ESC) |
| (2,752) | 421 | 关联成员丢失/无法定位("Unable to locate the broken association member") | 修关联 |
| **(7,3)** | 272 | 连接类型不兼容("Component has incompatible connection types") | 组件连接前 |
| (61,567) | 264 | F&M/图形操作上下文不满足 | 提取/修改前的环境检查 |
| (2,113) | 180 | 元素内容不符("does not contain a VIEW") | 出图元素操作 |
| (41,66) | 162 | (无统一文本,多为通用失败) | — |
| **(2,201)** | 155 | **引用元素无位置**("Ref element does not have a position") | 取 POS 前 |
| **(41,12)** | 116 | **元素名已存在**("An element of this name already exists. Please rename") | `new` 命名元素 |
| **(1000,0)** | 116 | PMLNet 桥通用错误(Excel 写失败等) | 所有 .NET 调用的兜底 |
| (2,751) | 109 | 应用未装载("Cabling System Application not loaded") | 应用前置检查 |
| (2,107) | 101 | 引用失效("Recent element no longer available") | 引用回取 |
| (2,754) | 92 | 连接引用缺失/数据元素不存在 | 支吊架/修改 |
| (2,822) | 91 | 无可删对象/引用 unset | 删除操作 |
| (2,111) | 82 | 需位于 DRWG/SHEE/VIEW | 出图上下文检查 |
| (47,15) | 77 | **属性值非法**("Value entered is not valid for this attribute") | 文本字段校验 |
| (2,441) | 67 | **字符串转 REAL 失败**("Cannot convert string to REAL") | 数值输入解析 |
| (2,759) | 63 | 尾端已连接等状态冲突 | 布管 |
| (42,64) | 59 | — | — |

## 3. 文档已载码(权威,Guide/RefMan/记忆)

| 码 | 语义 | 出处 |
|---|---|---|
| (46,28) | Variable not defined | 记忆 R9/Guide ch10 |
| (61,528) | User exit from submode | Guide ch22(FMSYS/OKCurfnView) |
| (61,115) | Invalid command when GRAPHICS OFF / no suitable view | 同上 |
| (61,605) | ALPHA removeRequests 在定义期调用 | Guide ch20.17 |
| (41,319) | Cannot access file (privileges) | Guide ch11 |
| (160,7) | 方法参数错误 | Guide ch11 |
| (160,9) | 文件不存在 | Guide ch11 |
| (160,36)/(160,37) | 未打开就读/写 | Guide ch11 |
| (160,44) | 文件存在,用户拒绝覆盖 | Guide ch11 |
| (160,46)/(160,47) | 读失败/超行数上限(ReadFile 缺省 10000 行) | Guide ch11 + TM-1402 示例 |
| (2,201)/(2,109) | 见上表 | 语料实证 |

## 4. 使用守则

1. **本表语义来自官方块内 alert 原文的归纳,不是核心文档权威定义**——精确码值以运行时报错头 `(m,c)` 为准;同一码在不同上下文可能对应不同底层消息(如 (2,109) 覆盖多种"找不到")。
2. **捕获惯例**:(61,528) 捕 ESC 退出;`(1000,0)` 兜 .NET;`(2,109)` 兜"找不到";**每个 DB 写操作配 `handle ANY/elsehandle NONE`**,精确码仅在需要差异化提示时用。
3. 新代码自造错误用 `return error 1 '消息'`(用户错误号段,配 `handle 1`);**不要占用系统模块号**。
4. 完整 330 码的块数/文本/示例文件:`PML语料\errorcode_semantics.tsv`。

## 5. 域化实证增补(第 81-86 轮九卷穷举新码,按域分组;语义=捕获处上下文)

### 5.1 数据库/权限域(模块 2)

| 码 | 语义 | 出处 |
|---|---|---|
| (2,9) | Spool 图纸求值错误 | pfPipeSpoolDwg——卷九 |
| (2,18) | 元素锁(REORDER/被引用锁定) | componentcreation:8748——卷三 |
| (2,357) | **PIN 方向为空**(交互定位未设) | mdscreateft15:886-890 `pin 5 dist -10` 补偿——卷十 |
| (2,502) | DAC 层级试探失败 | rtrpidprocess 新 PIPE 试探——卷三 |
| (2,583) | COPYCONSTRAINT 失败 | rtrcopyconstraints.pmlfrm:196——卷三 |
| (2,603) | **元素已被本人 CLAIM** | lstclaim.pmlfrm:647——卷十一 |
| (2,605) | **属主分支未 CLAIM(不能建焊缝)** | splcreatweld.pmlfrm:297——卷九 |
| (2,614) | ≤5 项被他人 CLAIM | lstclaim:647-663——卷十一 |
| (2,616) | >5 项被他人 CLAIM("Found 5 items claimed by others") | 同上 |
| (2,618) | **元素被他人占用**("Drawings already claimed by another user") | isodrwg.pmlobj:429——卷六 |
| (2,633) | Extract Claim 进行中 | lstclaim——卷十一 |
| (2,793) | 属性值含非法字符(sptype) | catupgradespec:143——卷四 |
| (2,891) | ADEG 角度计算失败 | pfcalculateadeg——卷九 |
| (2,150)/(2,207)/(2,235)/(2,252)/(2,253) | 名称不存在/Spool 查询/集合空族 | 卷六/卷十 |

### 5.2 出图域(模块 33/41/44/61/64)

| 码 | 语义 | 出处 |
|---|---|---|
| (33,157) | **Isodraw DETAIL 出图失败** | pfIsoDrawingManager:171——卷九 |
| (41,8) | **该层级禁止创建**(VIEW/SHTMPL) | abatemplatesht/abauserview——卷十 |
| (41,232) | (F&M 图形族) | mds——卷十 |
| (41,303) | 文件操作 | isodoclink:82——卷六 |
| (41,321) | 无读权限 | rgetmes:57——卷六 |
| (41,322) | 文件被占用 | mbatch:70——卷六 |
| (41,323) | 找不到文件 | mdelopt:46——卷六 |
| (41,324) | 文件已存在 | mbatch:55——卷六 |
| (41,325) | 文件尾 | initcoeff:76——卷六 |
| (44,15) | **PDF 文件已存在**(PLOT 覆盖确认) | isomodule.pmlobj:188——卷六 |
| (44,33) | 文件未找到 | isdruniso:42——卷六 |
| (44,36) | 权限不足 | mcreopt:36——卷六 |
| (61,122) | 设置表单控件失败 | mcresys:44——卷六 |
| (61,142) | 列表 >500 截断 | isysiso:37——卷六 |
| (61,143) | 无法访问目录 | isysiso:34——卷六 |
| (61,575) | 无列表数据 | ushow:23——卷六 |
| (61,618) | 一致性检查失败 | pfConsistencyCheck——卷九 |
| (61,721) | **ROUTE 布线失败**(BSTAT 2) | pipeSimpleAutoRoute:109——卷三 |
| (64,12)/(64,277)/(64,313)/(64,314)/(64,324)/(64,347)/(64,353)/(64,510)/(64,548) | 尺寸/几何计算族 | 卷六/卷九 |
| handle 6/7/8(mstdiso VPRM) | 6=MTO 线号/区域未设 7=多工艺线 8=多工艺区 | mstdiso:235-249——卷六 |
| handle 1(opt\iadmin) | 选项目录重置为 Local | 卷六 |

### 5.3 规格/选型域(模块 17/42/47/99)

| 码 | 语义 | 出处 |
|---|---|---|
| (17,19) | new spec COPY RENAME 失败 | catupgradespec:492——卷四 |
| (42,52)/(42,53)/(42,54)/(42,66) | 组件创建/规格选择失败族 | rtrpidprocess:835——卷三 |
| (42,94) | (组件族变体) | mds——卷十 |
| (42,501)/(42,502) | SELECT WITH SPEC 无匹配/失败 | componentcreation:7270——卷三 |
| (47,62) | **属性语法错(UDA/表格定义)** | mweldopt:59——卷六 |
| (61,162)/(61,164) | **规格无匹配元素**(CHOOSE WITH SHOP) | splcreatweld:305——卷九 |
| (61,299) | PARTN 零件号属性错误 | splpartn:166——卷九 |
| (99,532) | **UDA 未定义**(属性读失败) | isodrwgnumber:47、pfWeldControl——卷六/九 |

### 5.4 会话/工作共享域(模块 39/41/73/83)

| 码 | 语义 | 出处 |
|---|---|---|
| (39,15) | **无 MDB**(模块切换前) | moduleswitch——卷十一 |
| (41,6) | 通用失败 | pfm——卷九 |
| (41,25) | unname 三通去名失败 | rtrpidprocess:983——卷三 |
| (41,87)/(46,87) | fabexplorer 环境缺失 | pffabexplorer——卷九 |
| (41,243) | make global 后 CE 被删(注释实证) | moduleswitch——卷十一 |
| (73,3) | **TREF 回填失败**(P&ID 导入) | rtrpidprocess:942——卷三 |
| (73,214) | (连接族) | mds——卷十 |
| (83,6)/(83,14)/(83,15) | **SPOOL/FIELD/WELD/JOINT 编号网络错误** | splspooln:243、splweldn:353——卷九 |
| (43,364)/(43,383) | Spool 图纸/连接族 | 卷九/卷十 |
| (2,441) 补充 | **HML 语句/表达式解析失败**(stmtExec 参数) | phullseparate:229——卷七 |
| (1000,0) 补充 | **marAPI 已导入**(import 后固定写法,可忽略) | phullnotchjoinsplit:32——卷七 |
| (7,41) | **ppoint 未选中**(CONNECT TO P<n>) | splcreatweld:321——卷九 |
| (2,707)/(2,765)/(2,795) | accommodation 属性族 | 卷十 |
| (2,761)/(2,827)/(2,856) | iso 保温/重心/文档链接族 | 卷六 |
| (2,756)/(2,775)/(2,779)/(2,805)/(2,813)/(2,870) | PFM 表达式/生产检查族 | 卷九 |
