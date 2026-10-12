# 00 - START HERE · AVEVA 开发知识库导航

> 本工作区是 AVEVA Marine(12.1 SP4)二次开发知识库,基于官方安装目录全量实证(6075 PML 文件逐文件扫描 + 140 本官方手册全文 + 400 DLL 机器反射 + 33 XLS 属性表),2026-09-25 起 87 轮循环研究积累,十四卷穷举本 + 权威表 + 三件套规范 + 6 模板。
> **先查这里,再进具体文档;查具体命令词用《Marine-总索引.md》。**

---

## 1. 三步上手(新需求/新会话)

0. **先读《AVEVA开发工作流一页纸.md》**——七阶段 SOP 把全部工具与文档串成流水线,以下细节按需展开。
1. **判断轨道**:界面表单/DB 操作 → PML;停靠窗/复杂 UI/命令 → .NET addin;船体专业脚本 → Vitesse Python(Python 2.6)。
2. **按场景取文档**(见 §3 决策表),照端到端模板起骨架。
3. **放行前过审核**:pml_audit / net_consistency 跑一遍 → 规范 A→B→C→D;不确定的 API 走防猜协议(字典 → 语料库 → 手册 → TODO-UNVERIFIED)。

## 2. 文档清单与用途

| 文档 | 一句话用途 | 何时读 |
|---|---|---|
| PML生成规范*.md / PML审核规范.md / PML记忆*.md | **语法与验收三件套**(本体,未动) | 写码前/放行前 |
| AVEVA-Marine-PML开发技能.md | 环境·启动链·源码树·部署·Marine 特有写法 | 搭环境/定部署方案 |
| Marine-PML表单语法精要.md | setup form 体系权威速查(1380 表单所用语法) | 写任何表单 |
| Marine-PML对象API字典精要.md | 高频 46 类全方法 + 75 节目录 | 查对象方法签名(防猜第一步) |
| Marine-PML错误码速查.md | 330 错误码+模块号对照 | 写 handle / 读报错 |
| Marine-PML任务写法速查.md | 34 任务官方写法频次+样例 | 动手前定写法 |
| Marine-PML官方公共库目录.md | common 764 文件清点(先复用再自研) | 动手前查轮子 |
| AVEVA-Marine-NET开发技能.md | .NET addin 技术栈/部署/约束 | .NET 轨道总览 |
| AVEVA-Marine-NET-API用法Cookbook.md | Samples 20 文件逐类 API 范式 | 写 C# 时查用法 |
| AVEVA-Marine-marAPI调用姿势表.md | Marine 专属 API 反射全表+调用姿势 | PML/.NET 调船体/出图功能 |
| AVEVA-Marine-uic定制与部署调试手册.md | uic 全语法+部署调试排错 | 挂按钮/调 addin |
| Marine-PDMSUI-PML1宏机制速查.md | PML1 树/启动链/ADDIN 文件 | 动启动链/找官方界面实现 |
| Marine-设计模型操作命令编目.md | NEW/DELETE/CONNECT/POS/SPREF/UDA 等数据库操作命令全编目 | 写涉及模型/库/图纸/元素操作的代码 |
| Marine-元素操作命令大全.md | **穷举版第一卷**：30+元素类型创建/属性/导航/删除/连接/定位/规格/Rule/船体语句/PML变量嵌入 | 元素操作写法查证 |
| Marine-Draft出图操作命令大全.md | **穷举版第二卷**：DRWG/SHEET/VIEW/LAYER 全属性链 + 7种标注 + 2D图形 + 出图输出 | 出图操作写法查证 |
| Marine-Router布线命令大全.md | **穷举版第三卷**：ROUTE 布线/CONNECT 六变体/FCONN 降级/管件注册表/P&ID 导入宏生成/RPLA 管架/拆管 | 管道布线、Router 约束、P&ID 导入 |
| Marine-规格库操作命令大全.md | **穷举版第四卷**：SPWLD/SPEC/SPCO/SELE/选择表 57 方法/SPREF 全变体/PML1 CAT 宏族/NOMINB | 规格/目录/选择表操作 |
| Marine-属性操作写法全编.md | **穷举版第五卷**：296 属性名/198 UDA 名全频次表、复位四关键字、unset 判定、evaluate 求值、ppBore 数组 | 查属性名/UDA 写法/复位姿势 |
| Marine-Isodraft出图命令大全.md | **穷举版第六卷**：DETAIL/FILE/options 全命令词/材料表列定义/批处理 TTY/PLOT 输出/isometricadp 35 对象 | 轴测图生成与选项 |
| Marine-Hull船体建模语句大全.md | **穷举版第七卷**：PAN/BOU/PLA/STI/NOT/CUT/POI/CUR/SEA/WEL/FLA 全语句 + MARHULLPAN 全方法 + kcs_hull/chm/hullpan API | 船体面板/骨材/开孔 |
| Marine-Vitesse-Python-API全编.md | **穷举版第八卷**：kcs_util/ui/draft/dex/gui/model 全函数 + 四扩展机制 + Lib 102 库 + 错误处理范式 | 船体外全部 Vitesse 脚本 |
| Marine-Spooler管件车间命令大全.md | **穷举版第九卷**：SPOOLING 命令族/六套编号对象/焊接创建全序列/MTO/批处理合并/spool→iso 链 | 管段划分/车间制造 |
| Marine-专业模块命令大全-卷十.md | **穷举版第十卷**：MDS 支吊架/ASL 梯栏杆/舱室/PSI 应力/ABA 模板/装配/VNET/Integrator/关联规则 20 模块 | 支吊架/舱室/模板/应力模块 |
| Marine-横切命令族大全.md | **穷举版第十一卷**：AID/GPH/CLAIM 工作共享/命名服务/会话/$ 命令全集/VAR+CONSTRUCT 全集 | 写 AID 标注/批量收集/工作共享代码 |
| Marine-跨技术等价操作矩阵.md | **卷十二·综合索引**：20 组任务 × PML/PML2/marAPI/.NET/Vitesse 五轨道写法对照 + 选型决策 | 动手前定轨道/查等价写法 |
| AVEVA-Marine-NET程序集反射普查.md | **卷十三·机器验证**：400 DLL 反射总表、PMLNetCallable 184 类全清单（新增 115）、姿势表勘误、Samples 增量 15 文件 | .NET 轨道查类/防幽灵 API |
| Marine-官方手册增补-卷十四.md | **卷十四·手册对照**：140 本手册入库说明、42 项增补命令（CLEANU/Q BACKREF/SCOSEL/SPREAD/AUTOTAG/SPECONMODE 制表/PBORE0...）、6 条写法差异登记 | 查官方语法/批量建规格 |
| Marine-DRA宏树大全-卷十五.md | **卷十五·DRAFT UI 宏**：PDMSUI\DRA 30 子目录 1456 宏、尺寸 15 样式真实实现、GAP 四动词、SKEY→ISOTM 翻译器、PLOT DXF/PDF 直出、ADDINS 注册格式、37 项卷二增补 | 写 Draft UI 级宏/查标注样式实现 |
| Marine-des设计UI树大全-卷十六.md | **卷十六·设计 UI 宏**：des 树覆盖分析、9 族新元素类型（接头/新式基元/回转体/穿舱件）、CONNECT HH/HT、CHOOSE DEFAULT、单行复合创建句式、支吊架/ASL 建模宏骨架 | Design UI 级宏/查支吊架与 ASL 建模命令 |
| Marine-官方代码实例精讲.md | **卷十七·实例精讲**：8 个完整官方实例逐字提取+逐段解析（EDG 拾取/UNDOABLE/表单四件套/批量求值/Hull 语句改写/宏生成/批处理/PML1 规格宏）+ 纪律对照矩阵 | **写码前套骨架的第一站** |
| Marine-元素类型属性权威表.md | **DMRM 权威提取**：27 高频元素类型 × 862 条属性(显示名+DB 名+类型+说明) + Legal Owners/Members 层级规则 + 页码回查 | 查元素合法属性/合法层级(防猜权威) |
| **Marine-总索引.md** | **跨十四卷检索总入口**：674 命令词 + 255 对象/类 + 193 kcs 函数 = 1122 条,字母序,每条带 卷§ 锚与别名 | **查任何命令词/类/函数的第一站** |
| Marine-Vitesse-Python轨道速查.md | Python 2.6 四机制+kcs API | 船体脚本 |
| AVEVA-Marine端到端示例-收集导出工具.md | **模板①**:PML 表单+网格+Excel | 照抄起骨架 |
| AVEVA-Marine端到端示例-NET停靠窗addin.md | **模板②**:C# 停靠窗全流程 | 升级停靠窗 |
| AVEVA-Marine端到端示例-批量改库事务.md | **模板③**:批量改库三层防护(撤销/DAC/错误隔离) | 任何写库批量操作 |
| AVEVA-Marine端到端示例-出图批处理.md | **模板④**:marAPI 图纸批量生成/导出 | 出图自动化 |
| AVEVA-Marine端到端示例-Vitesse船体脚本.md | **模板⑤**:Python 抽取-报告-右键菜单三件套 | 船体脚本 |
| Marine-EDG事件系统精要.md | EDG 全参考:edgCntrl/edgPacket 成员表、11 种拾取序列、pick data 成员 | 写 3D 交互拾取工具 |
| Marine-帮助文档地图.md | Documentation 122 本 CHM 编目(F1 热键数+主题样例) | 遇到不熟悉的模块/对话框,查该开哪本 CHM |
| starter-kit-mycollect\ | **模板①的可部署工程包**(表单+addin 对象+install.cmd,已过审计) | 直接拷贝部署 |
| starter-kit-mybrowser\ | **模板②的可编译工程包**(3 个 .cs + uic + README) | VS 打开编译部署 |
| 规范修订建议-待并入.md | 21 条对三规范的修订建议(待批,含 81-83 轮增补 6 条) | 维护规范时 |
| Marine-PML学习报告-2026-09-25.md | 87 轮研究全记录(知识溯源入口) | 查"为什么/出处" |
| PML语料\(README.md 在内) | 语料库:6075 源码索引 + 140 本手册全文 + 38 XLS TSV + 反射/审计/校验脚本 | grep 查证 |

## 3. 场景 → 文档路径(决策表)

| 你要做的事 | 路径 |
|---|---|
| 写一个数据收集表单 | 任务写法速查(收集/遍历) → 表单语法精要 → 模板① → 审核规范 |
| 表单里嵌表格导 Excel | 模板①(现成);变体见其 §变体表 |
| 查某对象有没有某方法 | 对象字典 → 语料库 grep → pdf_text 手册 → TODO-UNVERIFIED |
| 报错 (2,109) 是什么 | 错误码速查(含模块号对照) |
| 给 Outfitting 加菜单/按钮 | PML 技能 §3.4(PML 路线)或 uic 手册(.NET 路线) |
| 写停靠窗 C# addin | 模板② → Cookbook → uic 手册排错表 |
| 调 marAPI 点图元/出图 | marAPI 姿势表(§3.5 点取/§3.2 图纸) |
| 批量改库要可撤销 | 模板③(三层防护) → PML 技能 §3.5 修订批 |
| 部署后按钮没反应 | uic 手册 §3.4 排错树 |
| 改了 PML 不生效 | PML 技能 §5.2(rehash/reload/pml index)+ 检查 DES-INIT-MAC |
| 船体批量脚本 | Vitesse 速查(四机制+Examples 索引) |
| 查官方怎么写某任务 | 任务写法速查 → task_idioms.tsv 样例 |
| 查某个错误码的官方处理姿势 | errorcode_semantics.tsv |
| 查官方手册语法原文 | pdf_text\140 本全文 findstr + 官方手册增补-卷十四（42 增补点） |
| 管道布线/Router 约束/P&ID 导入 | Router布线命令大全(§1 布线/§2 连接/§4 宏生成) |
| 规格库/目录/选择表操作 | 规格库操作命令大全(§2 SPEC/§3 SPCO/§4 选择表/§5 SPREF) |
| 查某属性名怎么写/UDA 复位 | 属性操作写法全编(§1 直写/§2 UDA/§5 复位/§8 数组) |
| 查某元素类型有哪些合法属性/能挂哪里 | 元素类型属性权威表(DMRM 27 类 862 属性 + Legal Owners/Members) |

## 4. 知识的可信层级

1. **机器验证**(反射/特性级校验,如 184 PMLNetCallable 全清单、862 权威属性表)= 最高;
2. **官方源码/手册原文**(语料库可回查行号/PAGE n);
3. **机器统计**(task_idioms/errorcode/callback_validation)= 频次与规律;
4. **归纳表述**(各速查文档)= 已尽量带出处;
5. **TODO-UNVERIFIED**(仅剩:HDIST/VDIST 三说;高号段模块的"官方模块名"——域化语义已实证,见错误码速查 §5)。

冲突裁决:官方两书矛盾时以"显式设置不依赖缺省值"绕行;源码与手册冲突时源码实证优先;规范本体修改一律走《规范修订建议-待并入.md》待批。

## 5. 维护

- 每轮研究追加学习报告"轮次记录";新体系知识并入对应速查;新修订点追加建议清单节。
- 语料库可重算:`python _scan_pml.py` / `_extract_pdfs.py` / `_extract_chm_pdfs.py` / `_extract_doc_pdfs.py` / `extract_xls.py` / `_validate_callbacks.py` / `_extract_errorcodes.py` / `_task_idioms.py`(Python 3)。
- 知识库自检:`python check_docs.py`(引用完整性;示例路径误报属已知良性)。
- 用户说停止前,每 30 分钟一轮持续迭代。
