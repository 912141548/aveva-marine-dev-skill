# Marine 总索引（跨十四卷命令/对象/函数检索）

> **生成说明**：本文件由脚本汇总《Marine-元素操作命令大全》（卷一）至《Marine-官方手册增补-卷十四》共 14 卷穷举/专题文档逐卷扫描生成（2026-09-29）。只收录各卷文档中**真实出现**的命令词 / PML 对象类 / kcs_* Python 函数，未做任何凭记忆补充。
> **使用方式**：查词 → 下表定位"锚" → 回对应卷文档核对参数、示例与 handle 错误码。锚格式 `卷三§2.1` = 该卷文档第 2 节（按文档内章节层级推算）。同一命令多卷出现时锚全部列出；语义取各卷中最完整描述；别名（缩写/同义形）合并展示。
> **卷号对照**：卷一=元素操作、卷二=Draft出图、卷三=Router布线、卷四=规格库(Paragon)、卷五=属性操作、卷六=Isodraft、卷七=Hull船体、卷八=Vitesse Python、卷九=Spooler管件车间、卷十=专业模块、卷十一=横切命令族(AID/GPH/CLAIM/VAR)、卷十二=跨技术等价矩阵、卷十三=.NET程序集反射普查、卷十四=官方手册增补。
> **覆盖范围**：表 A 以 PDMS 命令宏词为主（含 NEW/DELETE/CONNECT/AID/CLAIM/DETAIL 等动词、SIZE/POS/ORI 等选项词、`:UDA`、SELECT/CHOOSE/RESELECT 选件词，以及卷七 HML 船体语句关键字与卷十四手册增补词）；表 B 收 `object XXX()` 构造类、MAR*/KCS* 桥类与 pmlobj 类；表 C 收卷七+卷八全部 kcs_模块.函数。

## 表 A：PDMS 命令词索引（字母序）

| 命令 | 语义 | 锚 | 别名 |
|---|---|---|---|

| $ (行尾) | 续行符 | 卷十一§6 | - |
| $(…$) | 宏注释块定界（$(H …$)） | 卷一§15、卷十一§6 | - |
| $<…$> | 命令串内联 PML 求值（$<$!action$>） | 卷一§15、卷十一§6 | - |
| $D | 宏形参默认值（$d2=FALSE/$d3=TRUE/$d4=UNSET） | 卷一§15、卷十一§6 | - |
| $M | 调用执行宏文件（P&ID 导入宏生成后 $M 运行） | 卷一§15、卷三§4 | $M-/宏路径 |
| $N | COMPOSE 串内换行 | 卷十一§6 | - |
| $P | 命令行输出提示文本 | 卷一§15、卷十一§6 | - |
| $S | 定义同义词（$s name=…；$S1.. 为同义词形参） | 卷一§15、卷十一§6 | - |
| :UDA | 命令式设置自定义属性（!!ce.:UDA 为 PML2 形式） | 卷一§2、卷一§12 | !$<name> default|unset |
| ABLE | UDA 定义参数（长度类） | 卷五§2c | 见锚处 |
| ADD | 将元素加入显示列表（ADD CE COLOUR n TRANSL n EDGES ON） | 卷一§7、卷三§6、卷六§2.1、卷六§3.4 | - |
| ADEFRF | 关联规则定义引用（ADEFRF /av-exists2） | 卷十§7 | - |
| ADEG | 旋转角度（视图/文本） | 卷一§10、卷二§2 | - |
| AID | 三维可视化标注（AID TEXT/SPHERE/ARROW/LINE/BOX/CYLINDER NUMBER …；AID CLEAR 清除） | 卷三§1、卷三§6、卷五§5d | - |
| AID ARC | 弧标注（AID ARC NUMBER n arcStart TO arcEnd THRU mid） | 卷十一§1.1 | - |
| AID ARROW | 箭头标注（AID ARROW NUM n AT pos DIR dir HEI h [PROP r]，方向可 N/E/U） | 卷十一§1.1 | - |
| AID BOX | 盒标注（AID BOX NUMB n XLEN/YLEN/ZLEN … POSITION pos ORIENTATION ori [FILLED ON]） | 卷十一§1.1 | - |
| AID CIRCLE | 圆标注（无文本调用，仅经 GPHCIRCLE 封装） | 卷十一§1.1 | - |
| AID CLEAR | 清除标注（AID CLEAR ALL [n]；AID CLEAR LINE/TEXT/SPHERE/CYLI/BOX/ARROW/ARC n） | 卷五§5d、卷十一§1.1 | - |
| AID CYLINDER | 圆柱标注（AID CYLI NUMBER n DIAMETER d HEIGHT h [FILLED ON|OFF]） | 卷十一§1.1 | CYLI |
| AID LINE | 线标注（AID LINE NUMBER n pos1 TO pos2 [linestyle dashed]） | 卷十一§1.1 | - |
| AID SPHERE | 球标注（AID SPHERE NUMBER n pos DIAMETER d [MM]） | 卷十一§1.1 | NUM/NUMB |
| AID TEXT | 文本标注（AID TEXT NUMB n |txt| AT pos） | 卷三§1、卷十一§1.1 | - |
| AKEY | 直径标注键（AKEY word，默认 DIAM） | 卷十四§2.2 | - |
| ALIGN | 文本垂直对齐（TBODY/Base/BB/TB） | 卷二§4 | - |
| ALLOW | 余量设置（ALLOW $!allowance） | 卷九§6 | - |
| AMAPNME | 映射成员名（AMAPNME /av-exists2-ref1） | 卷五§3、卷十§7 | - |
| AMEMRF | 附件成员引用属性 | 卷五§3 | - |
| ANGLEACCURACY | 角度精度选项 | 卷六§2.4 | - |
| ANSTYPE | 答案类型（TEXT/REAL/WORD） | 卷四§4、卷四§4.3 | - |
| ARCTOL | 视图弧容差（HVAC=1 其余=5） | 卷六§3.4 | - |
| ASFBREAK | Arrive 端车间断点（asfbreak true|false） | 卷九§2 | LSFBREAK |
| ASSTMP | 装配模板引用属性（asstmp $!ref） | 卷五§3、卷十§2.1 | - |
| ATEXT | 替代文本定义（ATEXT n |text|；缺省库 .defaultAtexts[201..483]） | 卷六§2.7、卷六§7 | - |
| ATOL | 视图弧容差（Draft） | 卷十四§2.2 | ARCTOL |
| ATTABREAK | 加附加断点（ATTABREAK ON/SPKBRK branch） | 卷三§1 | - |
| ATTLIS | 属性查询列表（ATTLIS/ATTOUT/UDALIS/PSATTS 四列表） | 卷十四§2.1 | ATTOUT、UDALIS、PSATTS |
| ATTSET | 绑定属性集（ATTSET NONE，错误码 47,15） | 卷四§4 | - |
| ATTY | 附件/注记类型（atty CCNN） | 卷五§3 | - |
| AUTH | 图纸作者 | 卷二§1 | - |
| AUTO | 视图自动比例 | 卷一§10、卷二§2 | - |
| AUTOBLANKING | 自动消隐开关（作用于 LDIM/ADIM/RDIM/PDIM/GLAB/SLAB/VNOT/NOTE） | 卷十四§2.2 | - |
| AUTOSCALE | 自动比例（设 IDLN/THPO/VSCA，二次执行不重设 IDLN） | 卷十四§2.2 | AUTO |
| AUTOSIZE | 视图自动尺寸 | 卷十四§2.2 | - |
| AXES | 轴线标注（axes world|<axname>） | 卷六§2.4 | - |
| BACKREF | 反向引用查询（Q BACKREF (ATTNAME SPCO)，SP4 新增） | 卷十四§2.1 | - |
| BANN | Banner 查询（var !data BANN NAME/STATUS/COPYRIGHT/COMPANY/SHORT） | 卷十一§5.2 | - |
| BEND | 管件类型字：弯头（半径=N*OD 或弯管机自动） | 卷三§3 | - |
| BENDRADIUS | 弯头半径标注（distance/standard/diameters/outdiam） | 卷六§2.4 | - |
| BLNK | 文本/标注消隐开关（配 BMAR） | 卷二§4、卷十四§2.2 | BMAR |
| BOLT | 螺栓数查询（PA|PL BOLT TOTAL OF / BOLT JOINT OF） | 卷九§5 | - |
| BOLT LENGTH | 螺栓长度文本（bolt length description/itemcode append|insert at） | 卷六§2.2 | - |
| BOLTING | 螺栓选项（bolting off；bolting units metimp|metric|imperial） | 卷六§2.2 | - |
| BOLTREPORT | 螺栓报告（boltreport all [with position]） | 卷六§2.1 | - |
| BOU | HML 边界语句（'panel'/LIM=/SUR=/ZMIN=/ZMAX=/YMI=/REF/'__HULLFORM__'） | 卷七§2.2 | - |
| BPOF | 标签笔点偏移（BPOF 0 29.99） | 卷五§3 | CPOF、CPOFFSET |
| BSRF | 背景参照（BSRF UNSET 清除） | 卷二§1 | - |
| BSTAT | 分支布线状态（0 未布线~共 11 态） | 卷三§1、卷三§5 | - |
| BTEX | 文本内容参数 | 卷一§10、卷二§4 | - |
| BY | 相对偏移（by x 60mm/BY U zValue） | 卷二§2、卷三§1、卷三§6 | - |
| CALL | 调用 PML 函数（CALL !!autonamece(false)） | 卷七§1.2 | - |
| CALLCAPS | 调用 CAPS 系数宏（COFORMAT/WELDCOEFF/SLIPWELDCOEFF/… 系数记录关键字） | 卷六§2.6 | - |
| CALLDRE | AutoDRAFT 调用（CALLDRE MACAD-LINK <dir> <dxffn> <pipe> CREATE） | 卷六§4 | - |
| CALLIB | 调用名字校验例程（CALLIB UNAMECHK _CDTCRTSPWL_NAME） | 卷四§1 | - |
| CALLIG | 调用 PML1 宏（CALLIG RPREDET/RDISPLAY/RLIST） | 卷六§3.1 | CALLIB |
| CALLR | 调用外部宏例程（CALLR MADDCE 等） | 卷三§4 | callr |
| CATR | 设规格元件目录引用（CATR $!SPCO） | 卷四§3 | - |
| CHANGE | 改库属性 DDL（CHANGE <db> CLAIM <mode>） | 卷十一§3.2 | - |
| CHANGETYPE | 将当前元素改为指定用户类型 | 卷一§1 | - |
| CHARGE | 原材料炉批号 | 卷七§1.2 | - |
| CHARHEIGHT | 字符高度选项（charheight；weldnumbers charheight） | 卷六§2.2、卷六§2.4 | CHEI |
| CHECKRULES | 校验当前元素规则（CHECKRULES CE） | 卷一§13 | - |
| CHEI | 字符高度 | 卷一§10、卷二§1、卷二§4 | - |
| CHOICE | 声明规格选件选择集（CHOICE WITH，配 question/answer/maxans） | 卷一§1、卷三§3 | - |
| CHOOSE | 规格选件匹配（CHOOSE WITH SHOP；NEW WELD … CHOOSE SPEC …） | 卷九§6 | - |
| CLAIM | 认领元素（CLAIM CE[/MEM][/HIERARCHY]；错误码 2,603/2,614/2,616） | 卷五§5c、卷十一§3 | EXTRACT CLAIM |
| CLEANUP | 数据清理（CLEANU NULL|INVALID|UNRESOLVED attribute [ON noun][FOR ele][SETNULL|DELETE]，SP3） | 卷十四§2.1 | CLEANU |
| CLEAR | 清除 Router 全部约束（clear all） | 卷三§1 | CLEAR ALL |
| CLLLENGTHFILE | 切割长度输出文件（可带 insulation） | 卷六§2.3 | - |
| CLOCK | 日期时间查询（var !x CLOCK DATE/TIME/MDB） | 卷十一§8.5 | - |
| COLLECT | 收集元素集（COLLECT ALL <type> WITH … FOR …） | 卷四§1、卷四§5.3、卷四§7 | coll all |
| COLOUR | 设置元素/视图颜色（COLOUR CE n） | 卷一§7 | - |
| COMMENT | SPECONMODE 注释行；OUTPUT 选项 COMMENT | 卷十四§2.4 | - |
| COMPIPE | Compipe 输出（compipefile "<f>"；compipe mto/itemcodes/descriptions/supports） | 卷六§2.6 | COMPIPEFILE |
| COMPOSE | 字符串合成（COMPOSE |PT| WIDTH n SPACE 2） | 卷九§5 | - |
| CONFIGURATION | Router 配置（DIRECTION ELBOW/BEND/RULE、PRSPACE、PRROUNDING） | 卷三§1 | CONFIG |
| CONN | CONNECT 简写（CONN PH TO FIRST MEM 等） | 卷三§2、卷三§7 | CONNECT |
| CONNECT | 连接两端（PH/PT TO HREF/TREF/PH/PT of …/P1..Pn/next） | 卷一§5、卷三§2 | CONN |
| CONNECT TO NEXT | 顺序连接（CONNECT TO PREVIOUS/NEXT 变体） | 卷三§2、卷九§6 | CONNECT |
| CONSTRUCT | 几何构造族（ANGLE/DIRECTION/LINE/PLANE/POSITION/DISTANCE；INTERSECT LINE/PLANE、NEAREST … ON、… THROUGH … [DISTANCE d]） | 卷三§1、卷十一§8.6 | CONST |
| CONTNOTES | 续接注记（contnotes/contsheets/contudeftext） | 卷六§2.4 | CONT SHEETS |
| COORDINATES | 坐标标注位置（… at pipe/nozzle/open/close/vent/dran/shee/misc） | 卷六§2.4 | - |
| COPY | 复制元素（copy <src> rename <old> <new>；COPY PREV/LIKE/ATT OF/ATTRIB OF 变体） | 卷二§1、卷十§5.4、卷十四§2.4 | COPY PREV |
| COPY ATT OF | 按属性复制新建元素 | 卷一§1、卷三§7 | COPY ATTRIBUTES OF |
| COPY LIKE | 按参照复制（NEW 之后跟） | 卷一§1、卷二§1 | - |
| COPY MEM | 复制成员并改名（COPY MEM OF $!x RENAME a b） | 卷十§1.1、卷十§1.2 | - |
| COPY PREV | 复制前一同类元素 | 卷一§1、卷十§1.2、卷十§3.3 | COPY PRE |
| COPYCONSTRAINT | 复制分支 Router 约束（错误码 2,583） | 卷三§1 | - |
| COUP | 管件类型字：管箍（bore=checkBore(P2)） | 卷三§3 | - |
| CREATE | 通用创建（CREATE TEAM … DESC，安装用） | 卷六§1 | - |
| CREATE DB | 建库 DDL（CREATE DB <name> <type> … ACCESS/CLAIM 模式） | 卷十一§3.2 | - |
| CREATE VARIANT | 建变体/抽取库（CREATE VARIANT/EXTRACT <db> FROM <from>；CREATE WORK VARIANT FROM <db> FOR user） | 卷十一§3.2 | CREATE EXTRACT |
| CREF | 设置依附参照 | 卷三§3 | - |
| CRITERIA | 选择表准则属性（CRITERIA FOR $!itemRefe） | 卷五§4a | - |
| CSFBREAK | 组件断点 | 卷九§2 | - |
| CUR | HML 曲线/轮廓语句（X=/Y=/U=/V=/T=/R=/CLO/DIR=/M1=） | 卷七§2.8 | - |
| CUT | HML 开孔语句（tag 前缀 S/ST/SL/L/T/TR，C=偏移,R1=,SHP= 自由名） | 卷一§14、卷七§2.6 | - |
| CUTBACK | 截面定位（CUTBACK THROUGH p VIA SPINE BOUNDED；WALL THROUGH 同族） | 卷五§4b | - |
| CUTMARKS | 切断/续接符号（cutmarks/continuationsymbols） | 卷六§2.4 | CONTINUATIONSYMBOLS |
| CUTPIPELISTFILE | 切管清单输出文件（可带 formatfile） | 卷六§2.3 | - |
| CUTTINGLIST | 切割清单选项（off/itemcodes/endpreparations） | 卷六§2.2 | - |
| DACERR | DAC 错误查询（var !x DACERR $!i of dbref） | 卷十一§8.5 | - |
| DATE | 图纸日期属性 | 卷一§10、卷二§1 | - |
| DDNM | 尺寸名称引用（REFE OF DDNM） | 卷五§4a | - |
| DEFAULT | 缺省答案（DEFAULT 0） | 卷四§4 | TDEFAULT |
| DEFAULTS | SPECONMODE 默认行（'-' 无默认/'=' 取首项；*=当前 SPEC 名） | 卷十四§2.4 | - |
| DELETE | 删除当前元素/成员（DELETE <type>、DELETE <type> MEM、范围 TO） | 卷一§4、卷三§6、卷十四§2.2 | DELETE NULL IDLI |
| DELIMITER | 分隔符选项 | 卷六§2.2 | - |
| DENSITY | 密度值（Density $!Dens） | 卷七§1.2 | - |
| DEPR | UDA 偏置查询（DEPR ATTR/RULE/WRTO OF OWNER；RDEP NOFF） | 卷十一§8.5 | RDEP |
| DESADD | 设计元素加入视图/ID 列表（DESADD|DESREMOVE id） | 卷一§10、卷二§2、卷十四§2.2 | DESREMOVE |
| DESC | 元素描述文本 | 卷一§2 | - |
| DESP | 偏移参数（DESP 0 0…；DESP NUM 1 $!weldGap） | 卷五§3、卷九§6 | - |
| DESPAR | 尺寸参数写回（DESPAR d1 d2 d3 d4 d5，错误码 2,752 越界） | 卷五§3、卷十§1.1 | - |
| DETAIL | 出图核心（DETAIL <item>/isodrawing/all [as]/PIPE/SPOOL；类型 PIPE BRAN PSLIST PSPOOL ZONE GROU DRAWI ISODEP ISOREG SPLDRG SPOOL FIELD） | 卷六§2.1、卷九§10、卷十四§2.3、卷六§3 | SHEETN |
| DFLAG | 半径/直径标注标志（DIAM/RAD） | 卷二§3 | - |
| DFLT | UDA 默认值（FALSE/TRUE） | 卷五§2c | DEFAULT |
| DIAMETER | 圆柱/球标直径参数 | 卷一§1、卷三§1 | DIAM |
| DIM | 标注命令（DIM OFFS/DIM ABS/DIM @；DPBA FR BEFORE/TO AFTER 前后建点） | 卷十四§2.2 | DIM OFFS |
| DIMALL | 全尺寸开关 | 卷六§2.4 | - |
| DIMDIST | 尺寸间距（dimdist overall/support） | 卷六§2.4 | - |
| DIMENSIONS | 尺寸选项（off/composite/overall/centreline/critical/support/hangers） | 卷六§2.4、卷六§3.2 | Dimension |
| DIMLABELS | 尺寸标签位置（in/above） | 卷六§2.4 | - |
| DIR | 设方向（视图 DIR D/标注方向） | 卷一§10、卷二§2、卷二§3 | - |
| DIRECTORY | 目录查询（var !file DIRECTORY "$!name" DIR/FILE/FULLNAME） | 卷十一§8.5 | - |
| DKEY | 数据元素键 | 卷五§3、卷五§4a | - |
| DLFG | 尺寸线标志（DLFG PROJ|DIM|ALL；OSHT/PLCL 同族开关） | 卷十四§2.2 | OSHT、PLCL |
| DLSTYLE | 尺寸线/线样式颜色族（DLSTYLE/PLSTYLE/DLCOLOUR/PLCOLOUR/DTCOLOUR/PTCOLOUR） | 卷五§3 | - |
| DMSP | 标注文本间距（DMSP value|@） | 卷十四§2.2 | 见锚处 |
| DMTX | 改标注文本内容 | 卷二§3 | - |
| DOFF | 图层尺寸偏移距离 | 卷二§6 | - |
| DPOS | 标注文本定位（DPOS X.. Y..） | 卷二§3 | - |
| DRAWING | 出图张数参数（drawing $!COUNT） | 卷六§2.1 | 见锚处 |
| DRWG | 裸名访问图纸（DRWG /name 存在则访问） | 卷六§3.4 | - |
| DSCO | 设备代码属性（EQUI 全套属性之一） | 卷一§2 | 见锚处 |
| DSLAYE | 设计符号层（每 VIEW 仅一个） | 卷十四§2.2 | - |
| DSTYLE | 半径标注样式（DIMLINE/LEAD） | 卷二§3 | - |
| DTAN | 标注方向参数（DTAN PARA） | 卷二§3、卷五§3 | DTANG |
| DTANG | 标注方向角/文本角参数（配 PTANG） | 卷一§10、卷二§3 | PTANG |
| DTCH | 尺寸终端选择参数 | 卷五§3 | - |
| DTER | 尺寸终端样式（Arrows） | 卷二§1 | - |
| DTEXT | 直接文本选项（dtext $_DTEX；mtext 多行） | 卷六§2.2 | MTEXT |
| DTIT | 数据元素标题（DTIT '?'） | 卷五§3 | - |
| DTOFF | 标注文本偏移 | 卷二§3 | - |
| ELBO | 管件类型字：弯头（角度 min/angle/max） | 卷三§3 | - |
| ELEL | UDA 适用元素类型（ELEL ADD CYMLNK GPITEM GPSET） | 卷五§2c | - |
| ELEVATION | 高程标注选项 | 卷六§2.4 | - |
| END | 结束 NEW 创建块（含 CYLI/LAYER/TABHEA/UDA 等） | 卷一§1、卷二§1、卷四§4、卷五§2c | - |
| ENDMARKDB | 结束数据库标记区间 | 卷一§8 | - |
| ENHANCE | 高亮显示元素 | 卷一§7 | - |
| EQUIPMENTNUMBERING | 设备编号选项 | 卷六§2.2 | - |
| EVAL | PML1 属性求值（var !x EVAL <attr> FOR ALL FROM …） | 卷五§4a | EVALUATE |
| EVAR | 环境变量查询（var !data EVAR '$!evar'） | 卷三§4、卷十一§8.5 | - |
| EXC | HML 余量语句（EXC, LIM=, M1=） | 卷七§2.9 | - |
| EXISTS | 重名检查（var !x exists <name>） | 卷四§3 | - |
| EXIT | 退出 Router/命令环境 | 卷三§1 | - |
| EXTEND | 延伸元素端点（extend start/end thro pin n） | 卷十§1.1、卷十§1.2 | - |
| EXTRA | SPECONMODE UDA 列（EXTRA :uda_name value） | 卷十四§2.4 | - |
| FALLINGLINES | 落差线（fallinglines <fall> <limit> accuracylevel） | 卷六§2.4 | - |
| FALLSKEWS | 斜接管落差（fallskews on|off <numb>） | 卷六§2.4 | - |
| FCONN | 软连接（CONNECT 失败降级，配 MOVE 最小管长补偿） | 卷三§2 | FCONNECT |
| FILE | 输出文件（FILE "…" SINGLE；FILE AND DXF … SINGLE） | 卷六§2.1、卷十一§8.5 | - |
| FILL | 填充开关（FILL ON/FILLED ON|OFF） | 卷十一§1.1 | FILLED |
| FILT | 管件类型字：过滤器 | 卷三§3 | - |
| FINCH | 精度码（UCOD FINCH DIST） | 卷十四§2.2 | - |
| FIND | 视内元素查找（Q FIND gid IN view） | 卷十四§2.2 | - |
| FINISH | 退出模块（批处理宏收尾） | 卷六§1 | - |
| FLA | HML 法兰面板语句（PRO=/LIM=/CON=/CUT=） | 卷七§2.9 | - |
| FLAN | 管件类型字：法兰（flallow 松套标志） | 卷三§3 | - |
| FLIP | 翻转组件（REDU 扩径时前缀 FLIP） | 卷三§1、卷三§4 | - |
| FLOWARROWS | 流向箭头（flowarrows inline off|scale [automatic]） | 卷六§2.4 | - |
| FLOWDIR | 设分支流向（FLOWDIR OFF 关闭） | 卷一§1 | - |
| FONT | 字体号 | 卷一§10、卷二§1、卷二§4 | - |
| FORWARD | 流向/模式（FORWARDS 模式；NEW WELD FORWARD） | 卷三§1、卷九§6 | BACKWARDS |
| FPT | 线起点参数（NEW STRA FPT … TPT …） | 卷五§3 | TPT |
| FRPO | 视点起点（LOOK FROM） | 卷十四§2.2 | - |
| FSTYLE | 填充样式（配 FCOLOUR） | 卷二§1 | - |
| FUNC | 功能文本属性 | 卷一§2、卷三§5、卷三§6 | - |
| GAP | 标注间隙（GAP @/GAP AT @ [L v]/GAP DELETE/GAP TIDY/SETDEF GAP value） | 卷十四§2.2 | SETDEF |
| GETWORK | 恢复上次保存的工作区 | 卷一§8 | getwork |
| GLOBAL | 视图全局选项（NEW VIEW … GLOBAL） | 卷六§3.4 | - |
| GOBREF | 挂对象头引用 | 卷七§1.2 | - |
| GOTO | 世界导航（goto frstw CATA 跳转首世界） | 卷四§1、卷四§5.3 | - |
| GRDID | 网格标识 | 卷五§3 | - |
| GRDOFF | 网格偏移参数 | 卷五§3 | - |
| GTYP | 通用截面类型 | 卷一§1、卷三§3 | - |
| HBORE | 设分支头端公称口径 | 卷一§1、卷三§5 | - |
| HCON | 设头端连接特性（CLOS/OPEN 等） | 卷一§1、卷三§5、卷三§7 | - |
| HDIR | 设分支头端方向 | 卷一§1 | - |
| HEADING | SPECONMODE 表头定义（最多 20 列，建后不可改列数） | 卷十四§2.4 | - |
| HEIGHT | 圆柱/锥体高度参数 | 卷一§1 | HEIG |
| HIDE | 隐藏表单（hide !!form） | 卷十一§5.1 | - |
| HPOS | 设分支头端位置 | 卷一§1、卷三§5 | - |
| HREF | 设头端连接引用（NULREF 断开） | 卷一§1、卷三§2、卷三§4 | - |
| HSTU | 选头端离壁短管（select hstu/hstube） | 卷一§1、卷三§3 | - |
| HYPERPLANT | Hyperplant 输出开关（ON/OFF） | 卷六§2.1、卷六§2.4 | - |
| ICONS | Router 约束图标查询（ICONS POINT/PLANE n COMPONENT/DIR/LEAV/FIXED/NUMB/RPLA） | 卷三§1 | - |
| ID | 段标识查询（var !seg ID SEGMENT PPLINE … VIA PLINE BOUND） | 卷十一§8.5 | ID SEGMENT |
| IDLN | 挂接 ID 列表（配 IDLIST） | 卷二§1、卷二§2 | - |
| ILEAVE | 隐含管查询（ILEAVE TUBE OF $!element；710633=TUBI 标志） | 卷九§2、卷九§3、卷九§7 | - |
| IMPORT | 导入 .NET 程序集（import 'marAPI'，错误 1000,0 已导入可忽略） | 卷七§2.10、卷七§5 | - |
| INCBORE | 公称通径英制值 | 卷四§3.5 | - |
| INCLUDE | 将已有元素搬入当前元素成员 | 卷二§1、卷三§7 | incl |
| INSC | 设备保温规格属性 | 卷一§2 | - |
| INST | 管件类型字：仪表（P 点连接白名单成员） | 卷三§2、卷三§3 | - |
| INSULATIONCONTROL | 保温/伴热控制图（insulationcontrol/tracingcontrol） | 卷六§2.4 | TRACINGCONTROL |
| ISODRAFT | 进入 Isodraft 模块（TTY 宏一行进入） | 卷六§1 | - |
| ISODRAFTMODE | Design/Spooler 内进入轴测出图模式 | 卷六§1、卷六§3.3 | - |
| ISODRAW | 轴测状态查询（var !x isodraw status/number/plotfile …） | 卷六§1.2 | - |
| ISOTYPE | 轴测图类型查询/选项（var !x ISOTYPE） | 卷六§1.2 | 见锚处 |
| ISPEC | 保温规格属性 | 卷三§4、卷三§5 | iSpec |
| ITEMCODE | 项目码选项（itemcode from spref|UDA，for supports） | 卷六§2.2 | - |
| JOINTNUMBERS | 焊接头编号（jointnumbers/contjoints） | 卷六§2.4 | CONTJOINTS |
| JUSL | 截面对齐查询/设置（var !ppl JUSL；JUSLINE 同族） | 卷一§11、卷十一§8.5 | JUSLINE |
| JUST | 文本对齐（LEFT/RIGHT/CENTRE） | 卷二§4 | - |
| KEYS | 键图选项（keys <numb> [|value|]） | 卷六§2.4 | - |
| KILL | 关闭表单（kill !!form） | 卷十一§5.1 | - |
| LABEL | 宏内跳转标签（golabel 跳转） | 卷三§7 | golabel |
| LAST | 导航到同类末元素（last member/last stru） | 卷一§3 | - |
| LCHA | 链式/平行标注切换命令（LCHA PARA|CHAI；LCHAIN 为属性） | 卷二§3、卷十四§2.2、卷十四§3 | LCHAIN |
| LCHAIN | 链式标注开关（TRUE/FALSE） | 卷二§3 | - |
| LENGTH | 板长参数 | 卷七§1.2 | - |
| LFRA | 视图/图层框架显隐 | 卷一§10、卷二§2 | - |
| LIEXEC | 调 Draft 接口执行 DXF 导入导出 | 卷一§10、卷二§8 | - |
| LIMITS | 视图限界（LIMITS @ TO @/LIMITS ID @ ID @） | 卷十四§2.2 | - |
| LINETHICKNESS | 线宽选项 | 卷六§2.4 | - |
| LINKREF | 图页链接参照 | 卷二§1 | - |
| LLEA | 引线显示开关 | 卷二§6 | - |
| LNAME | 设置逻辑名（LNAME /av-exists2-rd1） | 卷十§7 | - |
| LOCK | 锁定元素（LOCK ALL/UNLOCK CE/UNLOCK ALL） | 卷四§3 | UNLOCK |
| LOCRF | 位置参照查询（LOCRF OF DBLOC 1） | 卷十一§8.5 | DBLOC |
| LOFF | 离线标志属性（choice loff 查询后 !!ce.loff 赋值） | 卷三§3 | - |
| LOOSEFLANGEALLOWANCE | 松套法兰余量选项 | 卷六§2.2 | - |
| LSFBREAK | Leave 端车间断点 | 卷九§2 | - |
| LSTU | 选离线管短管（select lstube） | 卷三§3 | - |
| LTER | 引线终端样式 | 卷二§1 | - |
| LVIS | 视图设计元素可见性 | 卷二§2 | - |
| LVOL | 体积查询（var !x LVOL OF item WRT wrt；VOL 同族） | 卷十一§8.5 | VOL |
| MARGIN | 页边距（margin left/right/top/bottom R） | 卷六§2.4 | - |
| MARK | 出图标记（mark detail/revision/ignore） | 卷六§2.4 | - |
| MARKDB | 设数据库回退标记（MARKDB CLEAR 清除、!mark=MARKDB 查询） | 卷一§8、卷三§1 | - |
| MARPTYPE | Marine 图纸类型属性（marPtype $!n；!!setmarptype(shee,n)） | 卷九§10 | - |
| MATCONTROL | 材料表控制（MATCONTROL OFF；matcontrol "<f>" [extended]） | 卷六§2.3、卷六§3.1 | - |
| MATERIALLIST | 材料表选项总命令（partnumbers/code/itemcode/bolting/cuttinglist/ppiece/spoolnumbers/tabledefinition…） | 卷六§2.2、卷六§2.5、卷九§10 | - |
| MATLISTFILE | 材料表输出文件（matlistfilename "<f>" PERPLOT with N lines） | 卷六§2.2、卷六§3.2 | MatlistFile |
| MATREF | 材料引用属性 | 卷一§2 | - |
| MCOLOUR | 标记颜色（MCOLOUR default 复位） | 卷二§7、卷五§3 | - |
| MESS | 输出消息文件（mess "<file>" over） | 卷六§3.3 | - |
| MESSAGEACCURACY | 消息精度（radial/iterations） | 卷六§2.4 | - |
| MESSAGEFILENAME | 消息文件选项（messagefilename "<f>"） | 卷六§2.4、卷六§3.2 | MessageFile |
| MIRROR | 镜像（MIRROR PLANE TOWARDS P2 OF CE THRO P2 OF CE） | 卷十§1.2 | - |
| MMBORE | 公称通径公制值 | 卷四§3.5 | - |
| MODERR | 触发属性修改校验错误（MODERR <attr> of <comp>） | 卷一§2 | - |
| MONITOR | 批处理宏收尾监视命令 | 卷六§2.1 | - |
| MOVE | 移动元素（MOVE <dir> distance d / THROUGH <pos>） | 卷三§2、卷七§1.2 | - |
| MSTYLE | 标记样式（MSTYLE Stop/SCALE，MSTYLE default 复位） | 卷二§4、卷二§7、卷五§3 | MCOLOUR |
| MTOH | 头管 MTO 状态（MTOH $!status；同族 MTOT/MTOC） | 卷九§5 | MTOT、MTOC |
| NAME | 命名/重命名元素 | 卷一§2 | - |
| NEW <type> | 按类型变量化创建任意管件（官方唯一推荐写法） | 卷一§1、卷三§3 | NEW $!<componentType> |
| NEW <type> COPY MEMBERS OF | 复制元素及其成员 | 卷一§1 | COPY MEMBERS OF |
| NEW ADDE | 创建 ID 列表项 | 卷一§10、卷十§5.5 | ADDENTRY |
| NEW ADIM | 创建角度标注（SENSE CLOCKWISE/ANTICLOCKWISE） | 卷一§10、卷二§3 | - |
| NEW AEXTR | 创建区域拉伸（obs=0） | 卷十§3.1 | - |
| NEW APPDAR | 创建 ASL 标准数据（DELETE 后 NEW 防重） | 卷十§2.4 | - |
| NEW APPLDA | 创建 ASL 梯数据 | 卷十§2.4 | - |
| NEW APPT | 创建绝对位置点（DDNAME+PPDI） | 卷二§3 | - |
| NEW ARC | 创建弧（DEF 三点/ADEF 圆心半径角，FILLETRADIUS 圆角） | 卷一§10、卷二§5 | - |
| NEW AREADEF | 创建区域定义 | 卷十§3.1 | - |
| NEW ASSMBR | 创建关联成员（AMEMRF $!dbref 配用） | 卷十§7 | - |
| NEW ASSOC | 创建关联规则 | 卷十§7 | - |
| NEW ATTA | 创建附件 | 卷三§3 | - |
| NEW AXESYM | 创建轴线符号（ASMBLR/AXSTYPE/AXSSIZE） | 卷二§5 | - |
| NEW BBLOCK | 创建舱室块 | 卷十§3.4 | - |
| NEW BLEVEL | 创建舱室层高 | 卷十§3.4 | - |
| NEW BLOCK | 创建分段 Block | 卷七§1.2 | - |
| NEW BNDLIN | 创建边界线（舱室轮廓） | 卷十§3.1 | - |
| NEW BOX | 创建长方体（XLENGTH/YLENGTH/ZLENGTH/ORI） | 卷一§1 | - |
| NEW BRAC | 创建肘板 | 卷十§1 | - |
| NEW BRAN | 创建分支（COPY LIKE/COPY ATT OF/copy prev 等 11 变体） | 卷一§1、卷三§7 | NEW BRANCH |
| NEW CABLE | 创建电缆（COPY ATTRIBUTES OF 复制式） | 卷一§1 | - |
| NEW CEILING | 创建天花板（clnHeight/clnVoid/colSchema） | 卷十§3.1 | - |
| NEW CGRDCP | 创建格栅交叉件（COPY LIKE PREV） | 卷十§3.3 | - |
| NEW CGRDLP | 创建格栅纵长件 | 卷十§3.3 | - |
| NEW CIRC | 创建圆（DEF 圆心半径/DIAM 两点直径） | 卷一§10、卷二§5 | - |
| NEW CLNCGR | 创建天花格栅 | 卷十§3.3 | - |
| NEW CLNLAT | 创建天花格栅条（配 GENSEC/SPINE/POINSP） | 卷十§3.3 | - |
| NEW CLNPNG | 创建天花覆层 | 卷十§3.1 | - |
| NEW CLNTIL | 创建天花铺板（COPY LIKE PREV 逐格） | 卷十§3.3 | - |
| NEW CMFI | 创建多管贯穿件（ZDIST THRO p WRT World） | 卷三§3 | - |
| NEW CMPF | 创建贯穿套管（AT p WRT world） | 卷三§3 | - |
| NEW COCO | 创建元件兼容表元素（cType/cKey 属性） | 卷四§3.4 | - |
| NEW CTABLE | 创建选择表（DESC，命名 /CT/规格/标题） | 卷四§1、卷四§4 | - |
| NEW CTRAY | 创建电缆托盘 | 卷一§1 | - |
| NEW CTWALL | 创建曲面板墙 | 卷五§3、卷七§5、卷十§3.4 | - |
| NEW CURVE | 创建曲线元素（舱室布置） | 卷十§3.4 | - |
| NEW CWAY | 创建电缆桥架路径 | 卷一§1 | - |
| NEW CWBRAN | 创建电缆桥架支路 | 卷一§1 | - |
| NEW CYLI | 创建圆柱（DIAMETER/HEIGHT/ORI） | 卷一§1 | - |
| NEW DATA | 创建数据元素（DESC/DKEY/DTIT/PPRO） | 卷五§3 | - |
| NEW DDATA | 创建数据定义元素（PURP EXPR/DKEY/WRTO/PTYP） | 卷五§3、卷十§1 | DDAT |
| NEW DDSE | 创建详图数据集 | 卷十§1.4、卷十§2.4 | - |
| NEW DEPT | 创建 Draft 部门域 | 卷一§1 | DEPT |
| NEW DETGRP | 创建详图组（purpose CLN） | 卷十§3.1 | - |
| NEW DLLB | 创建绘图库（SPPURP CWSUBS） | 卷六§3.4 | - |
| NEW DMND | 创建菱形 | 卷二§5 | - |
| NEW DPOI | 创建位置点（POS） | 卷二§3 | - |
| NEW DPPT | 创建尺寸点（DDNAME+NPPT） | 卷二§3 | - |
| NEW DPSP | 创建 Draft 参数点（PVIF/PURP DIM/FUNC/NUMB） | 卷五§3 | - |
| NEW DRTMLB | 创建图纸模板库 | 卷十§5.1 | - |
| NEW DRTMPL | 创建图纸模板 | 卷五§3 | - |
| NEW DRWG | 创建图纸（DATE/TITL/AUTH 属性链） | 卷一§10、卷二§1 | DRWG |
| NEW ELCONN | 创建元素连接件（Integrator 喷嘴） | 卷十§7 | - |
| NEW ELFITT | 创建电气配件 | 卷十§3.3 | - |
| NEW ELLI | 创建椭圆（三点） | 卷二§5 | - |
| NEW EQUI | 创建设备（裸创建+CHANGETYPE/COPY/自动编号四变体） | 卷一§1 | - |
| NEW EXTR | 创建拉伸负体（LOOP+VERT 后再 EXTR 执行） | 卷一§1 | - |
| NEW FCUTPL | 创建地板切割平面 | 卷十§3.4 | - |
| NEW FITT | 创建配件 | 卷三§3 | - |
| NEW FIXING | 创建固定件（AFTER LAST MEMBER/POS … WRT World） | 卷一§9、卷三§3 | - |
| NEW FLRCOV | 创建地板覆盖 | 卷十§3.1、卷十§3.4 | - |
| NEW FLRLAY | 创建地板铺层 | 卷十§3.1、卷十§3.4 | - |
| NEW FPFITT | 创建防火配件 | 卷十§3.3 | - |
| NEW FRMW | 创建框架元素（开孔虚拟框架） | 卷五§3、卷七§1.2 | - |
| NEW FTUB | 创建电缆托盘槽件（SEL + CONN + WI STYP） | 卷五§3 | - |
| NEW GBLOCK | 创建分段组块（handle 2,109 探测后建） | 卷七§1.2 | - |
| NEW GENSEC | 创建通用截面（SPRE/GTYP/POSS/POSE 属性链） | 卷一§1 | - |
| NEW GLAB | 创建全局标签（ON <ref> BTEX，CPOFFSET 偏移） | 卷一§10、卷二§4 | - |
| NEW GOBELE | 创建块元素 | 卷七§1.2 | - |
| NEW GPART | 创建零件（COPY LIKE $!spco，pritype 赋值） | 卷四§3.6 | - |
| NEW GRIDLN | 创建网格线（GRDOFF/GRDID） | 卷五§3 | - |
| NEW HANDRA | 创建栏杆（railHeight/postSpacing/tangOffset 属性） | 卷十§2.3 | - |
| NEW HANG | 创建吊架 | 卷一§1、卷十§3.3 | - |
| NEW HATTA | 创建舱壁附件 | 卷十§3.4 | - |
| NEW HEXA | 创建六边形 | 卷二§5 | - |
| NEW HRTERM | 创建扶手终端（ref $!ref） | 卷五§3 | - |
| NEW HVAC | 创建风管（分支 COPY LIKE） | 卷一§1 | - |
| NEW HVACFI | 创建舱室 HVAC 风口 | 卷十§3.3 | - |
| NEW IDLI | 创建 ID 列表（错误码 2,618 被占用；SPPURP PARTSL/ADJCNT） | 卷六§3.4 | IDLI |
| NEW INFITT | 创建舱室家具配件 | 卷十§3.3 | - |
| NEW INSURQ | 创建保温需求元素 | 卷十§3.4 | - |
| NEW JLDATUM | 创建甲板标高基准 | 卷三§3 | - |
| NEW LAYER | 创建图层（PURP/FONT/CHEI 等全属性） | 卷一§10、卷二§6 | LAYE |
| NEW LDIM | 创建线性标注（DTANG/PTANG+DIR+FROM/TO，15 种样式） | 卷一§10、卷二§3 | - |
| NEW LNDESC | 创建折线描述（Marine Drafting 唯一 DB 命令） | 卷十§6、卷十§7 | - |
| NEW LOOP | 创建负体轮廓 | 卷一§1、卷一§4 | - |
| NEW MBRMAP | 创建成员映射 | 卷十§7 | - |
| NEW MRKP | 创建标记点（PURP AT @，MCOLOUR/MSTYLE） | 卷二§5、卷二§7 | - |
| NEW NBRWLD | 创建公称通径世界（NEW NBRWLD /NOMINALBOREWORLD PURP BORE） | 卷四§3.5 | - |
| NEW NOMINB | 创建公称通径项（INCBORE/MMBORE） | 卷四§3.5 | - |
| NEW NOTE | 创建注释（copy+ren 复制式） | 卷二§4 | - |
| NEW NOZZ | 创建管嘴（catref/height/pos 由 PML 直赋） | 卷一§1 | - |
| NEW NPYR | 创建负四棱锥（XBOTTOM/YBOTTOM/YTOP/XTOP/XOFF） | 卷一§1 | - |
| NEW NREV | 创建圆锥负体 | 卷一§1 | - |
| NEW NXTR | 创建函数负体 | 卷一§1 | - |
| NEW OBJHD | 创建对象头（配 GOBREF 挂接） | 卷七§1.2 | - |
| NEW OLAY | 创建覆盖层 | 卷十§5.5 | - |
| NEW OPENSP | 创建开敞空间 | 卷十§3.4 | - |
| NEW OUTL | 创建轮廓 | 卷一§10、卷二§5 | - |
| NEW PANE | 创建板件（补偿板 copy $!source 变体） | 卷一§1、卷十§1.4 | - |
| NEW PANEL | 创建板（配 NEW PLOOP 定义轮廓） | 卷一§1 | - |
| NEW PAVE | 创建铺面元素 | 卷一§1 | - |
| NEW PDIM | 创建螺栓圆 PCD 标注（PCEN/PCIRC/DDEG） | 卷二§3 | - |
| NEW PIPE | 创建管路（COPY ATT OF/copy prev/DAC 错误组变体） | 卷一§1、卷三§7 | - |
| NEW PJOI | 创建管接头（jois 属性配用） | 卷十§1.4 | - |
| NEW PLAT | 创建平台（SEL SPREF WITH STYP 选型材规格） | 卷一§1 | - |
| NEW PLDATU | 创建平面基准（POSL） | 卷三§3 | - |
| NEW PLOO | 创建板体（负轮廓体） | 卷一§1 | - |
| NEW PLOOP | 创建板轮廓回路 | 卷一§1 | - |
| NEW PLTFRM | 创建平台（ref 挂接变体，UNNAME 后属性直写） | 卷十§2.1 | - |
| NEW PNODE | 创建管节点 | 卷十§1.4 | - |
| NEW POINSP | 创建样条插值点（POLAR 变体） | 卷一§1 | - |
| NEW POINT | 加布线途经点（NEW POINT AT <pos> AFTER <branch>） | 卷三§1 | - |
| NEW POINTR | 创建参考点（派生体） | 卷一§1 | - |
| NEW PPLA | 创建平行剖切面（FPLA/SPLA 同族；配 WPOS/VSEC 挂 Layer） | 卷十四§2.2 | FPLA、SPLA |
| NEW PRTELE | 创建零件元素（purpose=GTYP） | 卷四§3.6 | - |
| NEW RAWPLA | 创建原材料板（Height/Length/Matref/Width） | 卷七§1.2 | - |
| NEW RDIM | 创建半径/直径标注（DFLAG DIAM|RAD，DSTYLE DIMLINE|LEAD） | 卷二§3 | DDIM |
| NEW RECT | 创建矩形（XYPOS/XLEN/YLEN） | 卷一§10、卷二§5 | - |
| NEW REGI | 创建注册表（图纸域容器） | 卷一§1 | REGI=REGISTRY |
| NEW REGISTRY | 创建 Draft 全局样式注册表（SIZE/UCOD/FONT 等全属性） | 卷二§1、卷一§10 | REGI |
| NEW REST | 创建约束（PSI 节点约束/舱室吊件，handle 2,109 探测） | 卷十§3.3、卷十§4 | - |
| NEW RESTRI | 创建关联约束 | 卷十§7 | - |
| NEW ROOM | 创建房间（COPY 变体） | 卷十§3.4 | - |
| NEW RPATH | 元素路径（电缆路径；ASL 走道边界 ref 变体） | 卷一§1、卷十§2.1、卷十§2.2 | - |
| NEW RPLA | 创建管架平面（XLEN/YLEN/ORI/PURP PRRP|PREX） | 卷三§6 | - |
| NEW RPLG | 创建管架平面组 | 卷三§6 | - |
| NEW RPLTAB | 创建原材料板表 | 卷七§1.2 | - |
| NEW RRUL | 创建出图规则（USE /TT/…/Dashed_Style FOR …） | 卷六§3.4 | - |
| NEW RSTARE | 创建房间楼梯区域 | 卷十§3.4 | 见锚处 |
| NEW SBFI | 创建穿舱密封件（DELP p） | 卷三§3 | - |
| NEW SCLA | 创建天花吊件类元素 | 卷十§3.3 | 见锚处 |
| NEW SCTN | 创建结构型材（copy prev 等 8 种变体） | 卷一§1 | - |
| NEW SDEN | 创建标准密度定义 | 卷七§1.2 | - |
| NEW SELE | 创建旧式规格选择器 | 卷四§3 | SELE |
| NEW SHEET | 创建图页（错误码 41,52/41,12 处理范式） | 卷一§10、卷二§1 | SHEE |
| NEW SHLB | 创建图页库 | 卷十§5.1 | - |
| NEW SHTMPL | 创建图页模板（COPY RENAME 复制式） | 卷五§3 | - |
| NEW SITE | 创建站点元素（handle 错误包裹范式） | 卷一§1 | - |
| NEW SLAB | 创建符号标签（ON <ref> ATEX，TMRF 符号引用） | 卷一§10、卷二§4、卷二§7 | - |
| NEW SOLEXT | 创建材质扩展定义 | 卷七§1.2 | - |
| NEW SOLI | 创建材质等级固体 | 卷七§1.2 | - |
| NEW SPCO | 创建规格元件 | 卷四§3 | - |
| NEW SPEC | 创建规格（NEW SPEC name question TYPE；COPY RENAME 升级复制） | 卷四§2 | NEW SPECIFICATION |
| NEW SPINE | 创建样条线 | 卷一§1 | - |
| NEW SPLA | 创建样条元素（视图 spla1） | 卷十§5.5 | 见锚处 |
| NEW SPLDRG | 创建管段图容器（ISODEP/ISOREG/SPLDRG 经 NEW $!type） | 卷九§1、卷九§2 | ISODEP、ISOREG |
| NEW SPWLD | 创建规格世界（PURP 可一步完成） | 卷四§1 | NEW SPWL |
| NEW STRA | 创建直线（DEF @ 两点交互，TPT 续点） | 卷一§10、卷二§5 | - |
| NEW STRFLT | 创建斜梯段（fThickness/lRise/rise 等属性） | 卷十§2.2 | - |
| NEW STRSTR | 创建梯腹板梁（重建前 delete GENSEC） | 卷十§2.2 | - |
| NEW STRU | 创建结构元素 | 卷一§1、卷一§9 | - |
| NEW STRWELL | 创建围井 | 卷十§3.4 | - |
| NEW SUBS | 创建子组件模板（COPY ATTRIB OF 复制式） | 卷十§1.2 | - |
| NEW SYLB | 创建符号库（BSRF/SIZE） | 卷二§7 | - |
| NEW SYMB | 创建符号 | 卷二§7 | - |
| NEW SYMBOL | 符号库装载宏（NEW SYMBOL / TMRF SYTM …；OLD SYMBOL 改引用） | 卷六§7 | OLD SYMBOL |
| NEW SYTM | 创建符号项（AT X.. Y..） | 卷二§7 | - |
| NEW TABGRO | 创建选择表组（PURP INSU 等） | 卷四§1、卷四§4 | - |
| NEW TABHEA | 创建选择表表头 | 卷四§1、卷四§4 | TABHEADER |
| NEW TABHQU | 创建表头问题（QTYPE/ANSTYPE/PURP） | 卷四§4、卷四§4.3 | - |
| NEW TABITE | 创建选择表表项（PRTREF 挂 GPART） | 卷四§4、卷四§4.4 | TABITEM |
| NEW TABL | 创建表格元素（修订区 REVISI，ncol/nrow/fillDirection） | 卷二§5、卷十§6 | TABLE |
| NEW TABLE | 创建表格 | 卷二§5 | - |
| NEW TABQUE | 创建表项问题/答案（RFLAG/WANSWERS） | 卷四§4、卷四§4.3 | - |
| NEW TAGR | 创建 tag 规则 | 卷十§5.5 | - |
| NEW TASK | 创建绘图任务（COPY 复制式） | 卷五§3、卷十§5.4 | - |
| NEW TASKLB | 创建任务库 | 卷十§5.1 | - |
| NEW TATTA | 创建穿舱附件 | 卷十§3.4 | - |
| NEW TDEN | 创建理论密度定义 | 卷七§1.2 | - |
| NEW TEXP | 创建文本注释（JUST/ALIGN/BTEX/CHEI/ADEG） | 卷一§10、卷二§4 | - |
| NEW TEXT | 创建 DB 文本元素（PSI 应力文本） | 卷十§4 | - |
| NEW TKPARA | 创建绘图任务参数（tpvalue） | 卷五§3、卷十§5.4 | - |
| NEW TMPL | 创建负体模板容器（开孔三件套） | 卷一§1 | - |
| NEW TRLB | 创建标签库（TAGLIB） | 卷一§10、卷十§5.1、卷十§5.3 | - |
| NEW TRST | 创建 tag 规则集 | 卷十§5.3 | - |
| NEW UDA | 定义自定义属性（UDNA/UTYP/ULEN/ABLE/ELEL/DFLT/END） | 卷五§2c | - |
| NEW UGROUP | 创建 UDA 组 | 卷五§2c | - |
| NEW UWRLD | 创建 UDA 世界 | 卷五§2c | - |
| NEW VERT | 创建轮廓顶点（AT X.. Y..，BULGE 鼓度） | 卷一§1、卷二§5 | - |
| NEW VIEW | 创建视图（IDLN/SIZE/XYPO/SPPURP） | 卷一§10、卷二§2 | - |
| NEW VNOTE | 创建竖排注释（MSTYLE Stop 等参数） | 卷二§4 | - |
| NEW VSEC | 创建垂直剖面 | 卷十§5.5 | - |
| NEW VSPR | 创建可变弹簧支吊架 | 卷十§1.4 | - |
| NEW WALL | 创建墙（与 PANEL 同族） | 卷一§1 | - |
| NEW WELD | 创建焊缝（NEW WELD <posKey>/FORWARD/BACKWARD，CHOOSE SPEC 选规格） | 卷九§6 | - |
| NEW WLCOMP | 创建墙板组件组 | 卷十§3.2 | - |
| NEW WLFEAT | 创建墙特征 | 卷十§3.4 | - |
| NEW WLFITT | 创建壁装配件（copy prev） | 卷十§3.4 | - |
| NEW WLJNTS | 创建墙接缝组 | 卷十§3.2 | - |
| NEW WLJOIN | 创建墙接缝 | 卷十§3.2 | - |
| NEW WLOPEN | 创建墙开孔 | 卷十§3.4 | - |
| NEW WLPANE | 创建墙板（zdistance/posRef/wJusLine） | 卷十§3.2 | - |
| NEW WLPROF | 创建墙型材 | 卷十§3.2 | - |
| NEW WLPRSE | 创建墙压条 | 卷十§3.2 | - |
| NEW WPOS | 创建世界位置点（wpos pos e.. n..） | 卷十§5.5 | - |
| NEW ZONE | 创建区域，支持 COPY/RENAME 复制式 | 卷一§1 | - |
| NEX | 导航到后一同类元素 | 卷一§3 | - |
| NLCOLO | 线型颜色族属性（NLCOLO/LLCOLO/LFCOLO/DLCOLO/PLCOLO） | 卷一§10、卷二§1 | - |
| NLSTYL | 线型样式族属性（NLSTYL/LLSTYL/LFSTYL/DLSTYL/PLSTYL） | 卷一§10、卷二§1 | - |
| NORMAL | 法向定位（NORMAL DIST $!zDist FROM START） | 卷五§4b | - |
| NOT | HML 切口/流水孔语句（R 尺寸,COR=/SEA=/LIM=/U=/V=/REF） | 卷一§14、卷七§2.5 | - |
| OBST | 管架平面障碍标志 | 卷三§5、卷三§6 | - |
| OLD | 引用已有元素/定义（OLD UDA 改定义、OLD PIPE 复用前缀） | 卷二§1、卷三§4、卷五§2c | OLD UDA |
| OLET | 管件类型字：支管台（同 TEE 处理） | 卷三§3 | - |
| ONPO | 视点命令（ONPO） | 卷十四§2.2 | 见锚处 |
| OPCLAIM | DAC 权限操作模式 | 卷十一§3.2 | - |
| OPTIONS | 选项复位/选项文件（options default；$M 载入） | 卷六§2.1、卷六§3.3 | - |
| ORI | 设元素方向（ORI Z IS … AND X IS …） | 卷一§6、卷三§6 | ORIENTATION |
| ORIENTATE | 创建后自动定向组件 | 卷三§1 | - |
| ORIF | 三通立管标志（ORIF TRUE，配 POSF） | 卷三§4 | - |
| ORIGIN | 原点定位（ORIGIN CENTRE X50 Y50） | 卷五§3 | - |
| OUTPUT | 输出/变更追踪（OUTPUT <ele> CHANGES SINCE 21 JANUARY|EXTRACT 44|LATEST EXTRACT|SESSION 77 EXTRACT 44；选项 COMMENT/TABULATE/INDEX/BRIEF/ONLY/PASS；OUTPUT FILE|DXF|PDF|IMAGE|EMF） | 卷九§9、卷十§7、卷十四§2.1、卷九§10 | OUT |
| OVERALLSKEWS | 总斜度/零长度斜度选项 | 卷六§2.4 | ZEROLENGTHSKEWS |
| OWN | 层次移动（owner 向上；owner 连用回退两层） | 卷一§3、卷七§1.2 | OWNER |
| PAN | HML 面板定义语句（PAN,'name',<SBP|SP|P|S>[,BRA][,SUB][,BLO=][,DT=],X=|Y=|Z=|ORI=,UAX=,VAX=;） | 卷七§2.1 | - |
| PARAM | 目录元件参数读写（PARAM NUM n value、PARAM NUMB 计数） | 卷四§3.4、卷四§3.6 | PARAM NUM/NUMB |
| PARTNO | 零件号创建（PARTNO CREATE $!pipeRef/<gid> PBEND） | 卷九§7 | partno create ce |
| PARTNU | FTUB 及隐含管零件号计数（PARTNU $!count） | 卷九§7 | - |
| PBENDNUMBERS | 弯头编号选项 | 卷六§2.4 | - |
| PCODE | 单位换算精度组（mms to 0 dpls 等） | 卷二§1 | - |
| PCOM | 管件类型字：工艺仪表（同 INST） | 卷三§2、卷三§3 | - |
| PCON | 设连接点连接类型（PCON <type>） | 卷四§3.4 | - |
| PEN | 符号笔画定义（PEN U5 5/PEN D10 0） | 卷六§2.7 | - |
| PERSPECTIVE | 透视角度（VTYP 配用） | 卷十四§2.2 | - |
| PICTURESCALE | 图片比例选项 | 卷六§2.4 | - |
| PIN | 交点捕捉定位（PIN1 AT p DIR E/BEHIND el/OFF） | 卷三§6、卷五§4b | PIN1/PIN2 |
| PLA | HML 板语句（MAT=厚度,MSI=材料边,QUA=材质,U=/V=轮廓） | 卷七§2.3 | - |
| PLDI | 标注投影方向（PLDI U/-90） | 卷二§3、卷五§3 | PLDIR |
| PLDIR | 线性标注投影方向角 | 卷二§3 | - |
| PLDIST | 平面距离查询（PLDIST PPLINE ppl THROUGH … VIA PLINE BOUND） | 卷十一§8.5 | - |
| PLOT | 出图输出（PLOT CE/PLOT SHEE PDF/SVG/PRINT，OVERWRITE） | 卷一§10、卷二§8 | over |
| PLOTDETAILDATA | 出图明细查询（FILENAMES/NUM/ATTR） | 卷十一§7 | - |
| PLPM | 管架平面安装面（NEAR/WEIG） | 卷三§5、卷三§6 | - |
| PLPP | 管架平面位置（CENT/ABOV/BELO） | 卷三§5、卷三§6 | - |
| PLWW | 管架平面焊缝位置（WW/WF/FF） | 卷三§5、卷三§6 | - |
| POI | HML 定位点语句（NO=/INT/SID=/SI2=/DU=/DV=/XYZ=/X2Y=/F=/CRO） | 卷七§2.7 | - |
| POS | 设元素位置（POS PA AT PT OF BRAN、POS X.. Y.. 变体） | 卷一§6、卷三§6 | POSITION |
| POSF | 三通立管位置标志（POSF TRUE） | 卷三§4 | - |
| POSFOR | 图素位置格式（ENU） | 卷一§10、卷二§1 | - |
| POSFORMAT | 位置输入格式（XYZ/ENU/NUMBER） | 卷一§10、卷二§1、卷二§2 | - |
| PPLINE | 辅助线查询（PPLINE <x> OF <ref> NORMAL START/PROPORTION/DISTANCE … WRT World；VIA PLINE BOUND） | 卷十一§8.5 | - |
| PPPIECE | 管段件选项（ppiece on [CUT|TAG] after x |delim|） | 卷六§2.2 | - |
| PPRO | 数据元素表达式（PPRO (DDESP[4])，可接运算） | 卷五§3 | - |
| PRECISION | 单位精度切换（PRECISION VAR 1/16 | 1DP） | 卷三§1 | - |
| PREPPR | 表面预处理/油漆属性（Preppr） | 卷七§1.2 | - |
| PREV | 导航到前一同类元素 | 卷一§3 | - |
| PREVIOUS | 导航到前一同类元素（配 handle 2,113 列表耗尽） | 卷一§3、卷九§5 | PREV |
| PROJ | 工程属性查询（var !x PROJ MBCHAR/PROJ LOCK AT id） | 卷十一§7 | - |
| PROTECTION | 元素保护开关（PROTECTION OFF/ON） | 卷七§1.2 | - |
| PRTREF | 表项/元件零件引用（指向 GPART） | 卷四§4 | - |
| PSNAME | 管系统名选项（psname off/on [after x]） | 卷六§2.2 | - |
| PSPE | 管路规格属性命令（PSPE $!val；!!cdpipe.pspe 默认联动） | 卷三§4、卷三§5、卷四§5.2 | - |
| PTSP | 设备油漆规格属性 | 卷一§2 | - |
| PTYP | 数据元素类型（STRI 等） | 卷五§3 | - |
| PURCH | 原材料采购信息 | 卷七§1.2 | - |
| PURP | 用途代码（LAYER:PURP DIMA/LABA/NOTA/TAGA；RPLA:PRRP/PREX） | 卷一§2、卷二§6、卷三§5 | - |
| PURPOSE | 规格目的属性命令（配 PURP） | 卷四§2、卷四§4 | PURP |
| PYTHON | 命令行调起 Python 脚本（PYTHON 脚本名，嵌入式 2.6） | 卷八§9、卷十二§2.13 | - |
| Q | 属性/状态查询命令（Q BACKREF/PPOS/LASTMOD/MEMBER/DESP NUM/OPTIONS…） | 卷十四§2.1 | QUERY |
| QTYPE | 问题类型（TEXT/WORD/REAL/EXPR） | 卷四§4、卷四§4.3 | - |
| QUACD | 材质质量码属性（QuaCd） | 卷七§1.2 | - |
| QUALIFIER | 问题限定符（PBOR 端部代码 PBOA..PBOD） | 卷四§4.3 | - |
| QUES | 设选择器/规格问题（PBOR/GTYP/TYPE） | 卷四§3 | - |
| QUIT | 退出（批处理宏） | 卷六§1、卷九§9 | - |
| READONLY | 只读限定词（savework/sessions 命令限定） | 卷十一§5.2 | - |
| RECREATE | 重建保存选项文件（recreate options "<path>" overwrite） | 卷六§2.1 | - |
| REDODB | 数据库操作重做 n 步 | 卷三§1 | - |
| REDU | 管件类型字：异径管（双口径 Arrive/Leave 配置） | 卷三§3、卷三§4 | - |
| REFDIMENSIONS | 参考尺寸选项 | 卷六§2.4 | - |
| REFE | 引用属性（REFE OF CATR 等） | 卷四§3、卷五§4a | - |
| REFRESH | 刷新显示 | 卷二§9 | - |
| REMOVE | 移出显示列表（REMOVE ALL/REM CE） | 卷一§7、卷三§6 | REM |
| REORDER | 重排成员顺序（BEFORE/AFTER） | 卷一§9、卷三§1 | - |
| REPEATABILITY | Isodraft 选项词增补（REPEATABILITY/UNDERLAYPLOTNAME/TUBESPLITS） | 卷十四§2.3 | UNDERLAYPLOTNAME、TUBESPLITS |
| REPR | 更新表示/报表（REPR UPDATE） | 卷十§7 | - |
| RESELECT | 用新规格重选当前组件 | 卷三§3 | SELECT |
| RESERVE | 保留区（reserve/reserve materiallist） | 卷六§2.4 | - |
| REVI | 创建图纸修订（REVD/RVSN/RVAU/APPR/APPD 属性） | 卷六§3.4 | - |
| RFLAG | 答案形态（NONE/SING/RANG/MULT） | 卷四§4、卷四§4.3 | - |
| RLOCK | Router 锁定标志（0 可重排/2 自动件不可移动） | 卷三§4、卷三§5 | RLOC |
| ROTATE | 旋转（ROTATE THROUGH p ABOUT dir BY ang） | 卷三§1 | - |
| ROUTE | 执行分支布线（失败错误码 61,721） | 卷三§1 | - |
| ROUTER | 进入 Router 环境（CONFIGURATION/CLEAR/EXIT） | 卷三§1 | - |
| RRSF | 设置规则/引用集（RRSF RRST /DRA/…；RRSF $!ruleRefe） | 卷二§1、卷六§3.4 | RRST |
| RULE | 规则查询（var !ruleList RLIST；RULE OF <attribute>） | 卷一§13、卷十一§8.5 | RLIST |
| RULE DELETE | 删除规则（RULE DELETE ALL） | 卷一§13 | - |
| RULE EXECUTE | 执行规则（RULE EXECUTE SPRE ON ALL FOR CE） | 卷一§13 | - |
| RULE REXECUTE | 重新执行全部规则 | 卷一§13 | - |
| RULE SET | 定义 Rule 规则（RULE SET POSE (expr)） | 卷一§13 | - |
| RULEERROR | 取规则错误文本（RULEERROR $!j） | 卷一§13 | - |
| SAME | 结束元素级命令块（命令流收尾） | 卷三§2 | - |
| SAVEWORK | 保存当前工作（工具栏 GETWORK/MSAVEW 配对） | 卷一§8、卷二§9、卷九§9、卷九§11 | savework、MSAVEW |
| SCOSEL | 动态组选择（SCOSEL ALL EQUI FROM CLAIMLIST，SP4；ALL <type> MEMBERS WHERE …） | 卷十四§2.1 | ALL |
| SEA | HML 板缝语句（BEV=/EXC=/Y=） | 卷七§2.9 | - |
| SEL | 规格选取简写（SEL wi spec ... stype ...） | 卷一§1、卷三§3 | SELECT |
| SELECT | 按规格选件字符串选取组件（SELECT WITH/SELECT SPEC） | 卷一§1、卷三§3 | - |
| SENSE | 角度标注方向（CLOCKWISE/ANTICLOCKWISE） | 卷二§3 | - |
| SETUP FORM | 表单定义命令（setup form !!name；控件 button/text/frame/toggle/option/list/paragraph/combo/slider） | 卷十一§5.1 | - |
| SFLIMIT | Search Within 约束（SFLimit $!constraint） | 卷九§2 | - |
| SHOP | 现场/车间制造标志（SHOP TRUE → !component.shop） | 卷三§3、卷九§6 | - |
| SHOW | 显示表单（show !!splMtoStatus） | 卷九§8 | - |
| SIZE | 图纸/图页/视图尺寸（SIZE x y） | 卷一§10、卷二§1、卷二§2 | - |
| SKEWBOX | 斜管框（full|triangle standout hatch） | 卷六§2.4 | - |
| SKEY | 支吊架符号键定义（SKEY '10HG'…ENDSKEY，配 PEN 线笔画） | 卷六§2.7 | ENDSKEY |
| SMAXIMUM | 重置管段编号计数器（Smaximum 0；同族 W/J/P/Bmaximum） | 卷九§2 | WMAXIMUM、JMAXIMUM、PMAXIMUM、BMAXIMUM |
| SORT DIM | 尺寸排序整理 | 卷二§3 | - |
| SPAN | 轮廓封闭（SPAN TO CLOSE） | 卷二§5 | - |
| SPECBREAK | 规格断点标注（specbreak dimensiontype specchanges） | 卷六§2.4 | - |
| SPECONMODE | 进入/退出规格写模式（错误码 47,15 防重复） | 卷四§2、卷四§3 | exit |
| SPKBRK | 附加断点标志（SPKBRK TRUE） | 卷三§1、卷五§3 | ATTABREAK |
| SPLIT MEMB | 按成员拆分收集（var !x SPLIT MEMB SPWL） | 卷四§1 | - |
| SPLPREFIX | 管段编号前缀选项 | 卷九§2 | - |
| SPOOLING ADD | 元素加入管段（SPOOLING ADD CE $!element） | 卷九§6、卷九§9 | - |
| SPOOLING OPTIONS | Spooler 选项（SPOOLING OPTIONS INCLUDEFIELDS <flag>） | 卷九§9、卷九§10 | - |
| SPOOLING REMOVE | 移出管段/现场件（SPOOL/FIELD 专用，MEMBERS 变体） | 卷九§2、卷九§9 | - |
| SPOOLING REMOVESPLTMPS | 清除临时管段件 | 卷九§2、卷九§4 | - |
| SPOOLNUMBERS | 管段号选项（off/fromdb/on/perdrawing+prefix） | 卷六§2.2 | - |
| SPPURP | 设计数据用途（SPPURP ABAT 等模块标记；SPPURPOSE 同义） | 卷二§1、卷二§2、卷五§3、卷十§5.2 | SPPURPOSE |
| SPRE | 通用截面的型材参照 | 卷一§1 | - |
| SPREAD | 标签排版（SPREAD LOCAL/REMOTE SELECT OFFSET|MARGIN|GAP|NOROT） | 卷十四§2.2 | - |
| SPREF | 设置规格引用（变量/路径/NULREF/=0/UNSET 清空全变体） | 卷一§11、卷一§1、卷四§5.1 | - |
| SPWL | 导航到规格世界/属性查询（SPWL OF $!spec、PURP OF SPWL） | 卷四§1 | SPWLD |
| STACKINGARRANGEMENT | 叠装图选项 | 卷六§2.4 | - |
| STAR | 星号名解析（var !star STAR，* 展开为 CE 全名） | 卷十一§4.2 | - |
| STEX | 注记文本（stex 'DO NOT CUT HOLE…'） | 卷五§3 | - |
| STI | HML 骨材语句（PRO=/SID=/位置重复/REV/CON=/CUT=） | 卷七§2.4 | - |
| STYP | 选件子类型过滤（SELECT WITH STYP） | 卷一§1、卷三§3、卷三§4 | - |
| SUPPORTFILENAME | 支吊架输出文件 | 卷六§2.3 | - |
| SUR | HML 曲面/基准语句组（stmtGet 组3=SUR） | 卷七§2.10 | - |
| SYMBOLFILENAME | 符号输出文件（write|readonly） | 卷六§2.3 | - |
| SYSCOM | 执行系统命令（SYSCOM 'START /MIN cmd.exe /C …'） | 卷九§9 | syscom |
| TABANSWERS | 属性族答案（TABANSWER/TABANSWERS） | 卷四§4 | - |
| TABLEDEFINITION | 表列定义（… tabledefinition column N <att> [heading] with width W；gridlines） | 卷六§2.5 | - |
| TAG | Autotag 自动标注（TAG selection_option；CRIT ALL BRAN WI (…)） | 卷十四§2.2 | CRIT |
| TAGG | Autotag 消息/更新（TAGG MESS ON [/file]；UPDATE TAGG [IGNORE|OVERWRITE]） | 卷十四§2.2 | - |
| TANSWER | 文本答案属性（TANSWER |…|） | 卷四§4.3 | - |
| TBORE | 设分支尾端公称口径 | 卷一§1、卷三§5 | - |
| TCON | 设尾端连接特性 | 卷一§1、卷三§5、卷三§7 | - |
| TDIR | 设分支尾端方向 | 卷一§1 | - |
| TEE | 管件类型字：三通（bore=P3，宏 TEE /T 50） | 卷三§3、卷三§4 | - |
| TERM | 结束回放宏生成 | 卷九§9 | - |
| TEXT | 创建 DB 文本元素（PSI）；SPECONMODE 制表文本行（≤50 字符） | 卷十§4、卷十四§2.4 | - |
| TEXTPOS | 自定义文本位置（textpos attribute/system/revisiontable/weldtable/bendtable … corner C at x y；TEXTPOSITION 同族） | 卷六§1.2、卷六§2.4、卷六§2.5 | TEXTPOSITION |
| THPO | 视点穿过（THPO E N U = LOOK THROUGH；THPO ID @） | 卷十四§2.2 | - |
| THRU | 穿过点参数（AID ARC … THRU mid） | 卷十§1.1、卷十一§1.1 | THRO |
| TITL | 图纸/图页标题 | 卷一§10、卷二§1 | TITLE |
| TITLEBLOCK | 标题栏选项（titleblock <numb> [text]） | 卷六§2.4 | - |
| TOLERANCE | 公差选项（tolerance offset/angle） | 卷六§2.4 | - |
| TPOS | 设分支尾端位置 | 卷一§1、卷三§5、卷三§7 | - |
| TPT | 线下一点/终点参数 | 卷二§5、卷五§3 | - |
| TRANSFERFILE | IDF 传输文件处理（process transferfile "…"） | 卷六§2.1、卷六§4 | transferfilename |
| TRANSL | 设置半透明度（0-100） | 卷一§7 | - |
| TREF | 设尾端连接引用（NULREF 断开） | 卷一§1、卷三§2、卷三§4、卷三§7 | - |
| TRUN | 尺寸截断（TRUN BY|TO value = TRUNCATE） | 卷二§3、卷十四§2.2 | TRUNCATE |
| TRUNCATE | 英制尺寸截断设置 | 卷二§3 | - |
| TSFBREAK | 隐含管（Ileave tube）断点 | 卷九§2 | - |
| TSIZ | 图层数据文本尺寸 | 卷二§6 | - |
| TSPEC | 伴热/涂层规格属性 | 卷三§4、卷三§5 | tSpec |
| TSTU | 选尾端离壁短管 | 卷一§1 | - |
| TTY | 命令行无头批处理（-macro=… 官方范式） | 卷三§7 | - |
| TURN | 视图旋转（=ADEG） | 卷十四§2.2 | ADEG |
| TXCOLO | 文本颜色 | 卷一§10、卷二§1 | TXCOLOUR |
| UCOD | 单位集定义（UCOD mm Distance mm Bore Nominal） | 卷一§10、卷二§1 | - |
| UDNA | UDA 名称定义参数 | 卷五§2c | - |
| ULEN | UDA 文本长度 | 卷五§2c | - |
| UNCLAIM | 解除认领（UNCLAIM CE[/MEM HIERARCHY]/ALL） | 卷九§9、卷十一§3 | uncl |
| UNDERLAY | 底图（underlay "<file>" $!COUNT；off all） | 卷六§2.4 | - |
| UNDODB | 数据库操作回退 n 步 | 卷一§8、卷三§1、卷三§7 | - |
| UNENHANCE | 取消高亮 | 卷一§7 | - |
| UNITS | 单位选项（UNITS IMPERIAL；var !x output units） | 卷六§2.4、卷六§3.2、卷十一§8.5 | - |
| UNNAME | 去除元素名（三通去名，错误码 41,25） | 卷三§4 | unname |
| UNSET | 属性复位关键字四选一（unset/default/def/nulref，命令式行尾） | 卷五§5a | - |
| UPDATE | 图纸更新族（UPDATE DESIGN/REFRESH/ANNO/BSHEETS/ALL/PICTURE [IGNORE][OVERWRITE][NOWAIT]） | 卷二§9、卷十四§2.2 | - |
| USENAME | 名占用查询（var !x USENAME $!name） | 卷十一§4.2 | - |
| USING NAMESPACE | 声明 .NET 命名空间（Aveva.Marine.Design/DataExtraction/Geometry/UI/Drafting/Utility） | 卷七§2.10、卷七§5 | - |
| UTYP | UDA 类型（LOG/TEXT） | 卷五§2c | - |
| VALV | 管件类型字：阀门 | 卷三§3 | - |
| VAR | PML1 求值命令，结果存变量（var !x <expr>） | 卷四§1 | - |
| VOLUMEOPTION | 体查询选项（Q VOLUMEOPTION HULL DESIGN；HULL PRODUCTION ON/OFF） | 卷十四§2.1 | - |
| VREGION | Draft 视区定义（VREGION @/FROM X.. TO X../TL|TR|BL|BR|C/VERTICAL U|D|L|R） | 卷十四§2.2 | - |
| VSCA | 视图比例 | 卷一§10、卷二§2 | - |
| VSCAN | 视图查询族（Q VSCAN SIGNIF/Q VSIDE [ROT]/Q VLIMITS/Q VIEWDIR） | 卷十四§2.2 | VSIDE、VLIMITS、VIEWDIR |
| VTWA | 管件类型字：闸阀类（P 点连接白名单成员） | 卷三§2、卷三§3 | - |
| VTYP | 视图类型（Universal HLine 等） | 卷一§10、卷二§2、卷六§3.4 | VTYPE |
| WAITON | 等待表单（waiton !!form at xr0.4 yr0.45） | 卷十一§5.1 | - |
| WANSWERS | 文本型答案（WANSWERS UNSET 清除） | 卷四§4、卷四§4.3 | - |
| WARNINGS | 警告开关（WARNINGS OFF） | 卷二§1 | - |
| WASTAGE | 蚀损区标注（wastage area 1..9） | 卷六§2.4 | - |
| WEL | HML 焊接语句（WEL, LIM=, BEV=V22.5T） | 卷七§2.9 | - |
| WELDANGLES | 焊缝角度标注（on weldangmin） | 卷六§2.4 | - |
| WELDNUMBERS | 焊缝编号（off/charheight…；contwelds/weldid/weldtype） | 卷六§2.4 | CONTWELDS |
| WELDTABLEFILENAME | 焊缝表/弯管表输出文件 | 卷六§2.4、卷六§2.5 | BENDTABLEFILENAME |
| WI | WITH 简写（WI STYP VL、COLL ALL … WI <cond>） | 卷五§3 | WITH |
| WIDTH | 板宽参数 | 卷七§1.2 | - |
| WITHIN | 空间范围收集（COLLECT … WITHIN W… TO …；EXCLUSIVE WITHIN VOLUME；EXCLUDE …） | 卷十四§2.1 | EXCLUSIVE、EXCLUDE |
| XBOTTOM | 负四棱锥底 X 向参数 | 卷一§1 | - |
| XLENGTH | 元素 X 向长度 | 卷一§1、卷二§5、卷三§6 | XLEN |
| XOFF | 负四棱锥 X 向偏移 | 卷一§1 | - |
| XTOP | 负四棱锥顶 X 向参数 | 卷一§1 | - |
| XYPO | 图素位置（XYPO x y） | 卷一§10、卷二§2 | XYPS |
| YBOTTOM | 负四棱锥底 Y 向参数 | 卷一§1 | - |
| YLENGTH | 元素 Y 向长度 | 卷一§1、卷二§5、卷三§6 | YLEN |
| YTOP | 负四棱锥顶 Y 向参数 | 卷一§1 | - |
| ZLENGTH | 元素 Z 向长度 | 卷一§1 | - |

## 表 B：PML 对象/类索引（字母序）

| 类 | 用途 | 锚 |
|---|---|---|

| AIDCONSTRUCTORS | AID 构造管理对象（55 方法：add 12 重载/Packet 族 13 个） | 卷十一§1.4 |
| AIDMODIFY | AID 修改对象（17 方法：rotate/mirror/mirrorPlane/offset） | 卷十一§1.4 |
| AIDNUMBERS | AID 编号管理对象（14 方法：registered/next/draw/hide） | 卷十一§1.4 |
| APPISOADP | 轴测 ADP 辅助对象 | 卷六§6 |
| Arc2D/Arc3D | 弧类（__init__(p1,p2,amp)） | 卷八§8.1 |
| BLOCK | 表达式块对象（evaluate(object BLOCK('…'))，206 处主范式） | 卷一§3、卷五§7 |
| BodyPlanViewOptions/ShellXViewOptions | 横剖/外板展开视图选项类 | 卷八§8.3 |
| BooleanOperations | 布尔运算类（CompositeContour/CommonContour/DifferContour） | 卷八§8.1 |
| BORE | 通径对象（object BORE(real)、object BORE(0)） | 卷四§3.1 |
| Box | 包围盒类（origin+三方向+三长度，SetAxisParallelBox） | 卷八§8.1 |
| BRANCHCONNECTION | 分支连接对象（connect(element,'P<n>')、modifyBranchEnd） | 卷三§2 |
| ButtonState | point2D_req 按钮状态类（EnableLock/GetCheckedLock） | 卷八§8.2 |
| CABLEWAYMANAGER | 电缆路径管理 .NET 对象（disconnecthead/connectbranches） | 卷三§2 |
| CaptureRegion2D | 捕获区域类（SetRectangle/SetContour/SetInside/SetOutside） | 卷八§8.3 |
| CATSELTABVIEWS | 选择表 UI 对象（add/editSelTab/populateTable 等 40+ 方法） | 卷四§0.1、卷四§4.5 |
| CATSPECVIEWS | 规格目录视图对象（万行级：applyCompAdd/applySpecCadAtts） | 卷四§0.1 |
| CATUPGRADESPEC | 规格升级对象（upgrade/copySpec/createGparts/createSelTab） | 卷四§0.1、卷四§7 |
| cCoordRef/CoordRef3D | 坐标参照类 | 卷八§8.3 |
| CHECKNAME | 名字校验对象（!!checkName(name,'NEW')） | 卷四§0.1、卷四§7 |
| Circle2D/Circle3D | 圆类（HasPoint/GetTangentPoints/TangentAtPoint） | 卷八§8.1 |
| COLLECTION | 通用收集对象（scope/type/results 链式收集） | 卷四§7 |
| COMCHECKDBWRITE | 写保护检查对象（checkDBwrite(DBREF)） | 卷十一§3.3 |
| COMMARDRAWINGTYPES | Marine 图类型常量对象 | 卷九§12 |
| COMPONENTBEND | BEND 组件对象（自动半径 testBendRadius） | 卷三§3 |
| COMPONENTDEFAULT | COUP 等默认组件对象 | 卷三§3 |
| COMPONENTELBOW | ELBO 组件对象（角度越界回退 maxValue） | 卷三§3 |
| COMPONENTFILTER | FILT 组件对象 | 卷三§3 |
| COMPONENTFLANGE | FLAN 组件对象（松套 flallow/loose） | 卷三§3 |
| COMPONENTINSTRUMENT | INST/PCOM 组件对象 | 卷三§3 |
| COMPONENTREDUCER | REDU 组件对象（双口径 Arrive/Leave） | 卷三§3 |
| COMPONENTTEE | TEE/OLET 组件对象（bore=P3） | 卷三§3 |
| COMPONENTVALVE | VALV 组件对象 | 卷三§3 |
| COMPONENTVTWA | VTWA 组件对象 | 卷三§3 |
| Conic2D | 二次曲线类 | 卷八§8.1 |
| Contour2D | 2D 轮廓类（AddLine/AddArc/IsInside/Area，运算符 +/*/－ 并交差） | 卷八§8.1 |
| CopyPanOptions | 面板复制选项类（SetNameMapping/SetBlockName） | 卷七§4 |
| cPanel | 面板操作类（GetTransformationMatrix/PanelDataType/FindFreePanelName；限位类 CoordinateLimit/PanelLimit/OuterShellLimit） | 卷七§2.2、卷八§8.3 |
| CursorType | 光标类型类（CrossHair/RubberBand 等 5 种） | 卷八§8.2 |
| CurvedPanelView | 曲面板视图子类（SetSeams/SetStiffeners/SetEndcuts 等） | 卷八§8.3 |
| DEPLOT | 详图列表对象（!!dePlots 表单族配套） | 卷六§5 |
| DimensionSet | 尺寸集合类（AddLinearDim/AddAngleDim/AddRadiusDim/AddCustomDim） | 卷八§8.3 |
| DIRECTION | 方向对象（object DIRECTION(text)，解析失败 handle ANY） | 卷三§5 |
| ElementHandle | kcs_draft 句柄承载类（SetHandle/GetHandle） | 卷八§8.2 |
| Ellipse2D | 椭圆类（外接矩形两角构造） | 卷八§8.1 |
| EXPRESSION | 表达式对象（object EXPRESSION('PURP EQ …')） | 卷四§1 |
| Gencylinder | 广义圆柱类 | 卷八§8.1 |
| GeoContour3D | 3D 轮廓类（AddLine/AddArc） | 卷八§8.1 |
| GPHANGLEDIMENSION | GPH 角度尺寸图形对象（common\objects） | 卷十一§2 |
| GPHASL | GPH ASL 图形对象 | 卷十一§2 |
| GPHAUTOCOLOUR | GPH 自动着色对象 | 卷十一§2 |
| GPHAXES | GPH 轴线对象 | 卷十一§2 |
| GPHBOX | GPH 盒对象 | 卷十一§2 |
| GPHCIRCLE | GPH 圆对象 | 卷十一§2 |
| GPHCLIPBOX | GPH 裁剪盒对象 | 卷十一§2 |
| GPHCLIPPLANE | GPH 裁剪面对象 | 卷十一§2 |
| GPHCOLOPT | GPH 颜色选项对象 | 卷十一§2 |
| GPHDIMENSION | GPH 尺寸对象 | 卷十一§2 |
| GPHDRAWLISTS | GPH 显示列表对象（.add/.remove） | 卷十一§2 |
| GPHLINE | GPH 线对象 | 卷十一§2 |
| GPHLINEARGRID | GPH 线性网格对象 | 卷十一§2 |
| GPHLOCALVOLUME | GPH 局部体积对象 | 卷十一§2 |
| GPHPLANE | GPH 平面对象 | 卷十一§2 |
| GPHPLANTGRID | GPH 厂区网格对象 | 卷十一§2 |
| GPHPOINTVECTOR | GPH 点矢量对象 | 卷十一§2 |
| GPHPOLYGON | GPH 多边形对象 | 卷十一§2 |
| GPHPOSITION | GPH 位置对象 | 卷十一§2 |
| GPHRADIALGRID | GPH 径向网格对象 | 卷十一§2 |
| GPHREPDEFINITION | GPH 表示定义对象 | 卷十一§2 |
| GPHREPLINK | GPH 表示链接对象 | 卷十一§2 |
| GPHREPLST | GPH 表示列表对象 | 卷十一§2 |
| GPHREPOPT | GPH 表示选项对象 | 卷十一§2 |
| GPHSHIPGRID | GPH 船体网格对象 | 卷十一§2 |
| GPHSPHERE | GPH 球对象 | 卷十一§2 |
| GPHSPINE | GPH 骨线对象（draw 落图为 AID 命令序列） | 卷十一§2 |
| GPHVIEWOPT | GPH 视图选项对象 | 卷十一§2 |
| GPHVIEWS | GPH 视图中枢对象（60+ 方法：add/rotate/limits/clipbox/drawlist） | 卷十一§2 |
| GPHVOLUME | GPH 体积对象 | 卷十一§2 |
| GPTHREEDPLANTGRID | GPH 3D 厂区网格对象 | 卷十一§2 |
| GPTHRREDRADIALGRID | GPH 3D 径向网格对象 | 卷十一§2 |
| HighlightSet | 高亮集合类（AddGeometry2D/AddModel/Reset） | 卷八§8.2 |
| HMCONTROL | 开孔管理接口（createFittHole(coll,pos,type)） | 卷七§5 |
| HOLEELEMCOLL | 开孔元素集合对象（panel/holeFixing/fitting 成员） | 卷七§5 |
| HVACDETAILSPEC | HVAC 详图规格对象（宏文本数组建库） | 卷四§0.1 |
| ISDPREVIEWISOCONTROL | Design 内轴测预览控制对象（produceSystemIso/produceStandardIso/prepareToDetail） | 卷六§3.3 |
| ISOADPAPPLICATION | 轴测 ADP 应用对象（makeDrawings/makePartsList/pdf/print/batch/license） | 卷六§3.5、卷六§6 |
| ISOBACK | 背景对象 | 卷六§6 |
| ISOBRCO | 支管连接对象（addBrco/addDimdir/getBrcos） | 卷六§6 |
| ISOCONTENT | 轴测内容表对象 | 卷六§6 |
| ISOCONTTAG | 续接标签对象 | 卷六§6 |
| ISOCUTPIPECOL | 切管集合对象（isodraft 旧式） | 卷六§5 |
| ISOCUTPIPEFMT | 切管格式对象（isodraft 旧式） | 卷六§5 |
| ISODATA | 轴测数据构建对象（buildData/getData/setDrawn/remove） | 卷六§6 |
| ISODEFAULTS | 轴测缺省对象（getDflts/getDrwgNoDflts，读 %PDMSDFLTS%\IsoADP） | 卷六§6 |
| ISODIMENSION | 轴测尺寸对象（getDflts/dimension） | 卷六§6 |
| ISODISPLAYDRWG | 轴测显示图纸对象（isoDisplayDrwg/setSheet/setEntries） | 卷六§6 |
| ISODRWG | 轴测图纸对象（isoDrwg/create→ISODISPLAYDRWG/getNextRev/setSettings） | 卷六§3.4、卷六§6 |
| ISODRWGNODFLTS | 图号缺省对象（readDefaults/saveSettings/saveToFile，method=NSEQ|FILE） | 卷六§6 |
| ISOELEVTAG | 高程标签对象 | 卷六§6 |
| ISOHIGHLIGHT | 高亮对象（.store/.read/.write） | 卷六§5 |
| ISOINSULBRK | 保温断点对象 | 卷六§6 |
| ISOLOG | 轴测日志对象（add/read/write，%PDMSUSER%\LogFiles） | 卷六§6 |
| ISOMDSTAG | MDS 标签对象 | 卷六§6 |
| ISOMODULE | 轴测模块对象（displaySheet/submitToPdf/submitToPrinter） | 卷六§3.5、卷六§6 |
| ISOMTOENTRY | MTO 表项对象（getAtext/getHeaders/setCellAtext/setHeader） | 卷六§6 |
| ISOMTOGEN | MTO 生成对象 | 卷六§6 |
| ISONAMEDTAG | 命名标签对象 | 卷六§6 |
| ISOORIGIN | 指北/原点符号对象 | 卷六§6 |
| ISOPARTSLIST | 零件表对象（build/saveToExcel，配 NETGRIDCONTROL） | 卷六§3.5、卷六§6 |
| ISOPENETAG | 贯穿件标签对象 | 卷六§6 |
| ISORECTANGLE | 轴测矩形对象 | 卷六§6 |
| ISOREVISION | 修订对象（get/set） | 卷六§6 |
| ISORULE | 轴测规则对象（isodraft 旧式） | 卷六§5 |
| ISOSEARCH | 轴测搜索对象 | 卷六§6 |
| ISOSLAB | 轴测板对象 | 卷六§6 |
| ISOSPECBRK | 规格断点对象 | 卷六§6 |
| ISOSPOOL | 单个管段对象（addComponent/addSupport/getMaterial/getVolume） | 卷六§6 |
| ISOSPOOLS | 管段收集/拆分对象（getSpools/splitCway/splitHvac，splitMethod=VOLUME|SPLITPOINT） | 卷六§6 |
| ISOTABLE | 轴测通用表对象（MTO 表等） | 卷六§6 |
| ISOUNITS | 单位对象（getOffsetIncrement/getTextIncrement/getUnits） | 卷六§6 |
| ISOVIEW | 轴测视图对象 | 卷六§6 |
| KcsCPanDist | 曲面板距离表（CPanDist(PanelName,BaseSeam,…,Suffix)） | 卷八§8.3 |
| KcsDrawTable | 图上画表格（AddTable(Data,ViewHandle,Name)） | 卷八§8.3 |
| KcsPanelSchema | HML 语句 Schema 解析类（SetValue/GetStatements/MergeStatement，分隔符 ',' ';' '/'） | 卷七§2.10 |
| KcsPanHoleOptions | 曲面开孔选项类（SetOriginAlongLine/SetBurnOption/SetSymmetry；SYMM_AS_PANEL/SYMM_PS/SYMM_SB） | 卷七§3 |
| KcsProfSymb | 型材符号工具（getSymb(type)） | 卷八§8.3 |
| KcsPythonUtil.PythonUtil | Python 工具（AppendPythonPath） | 卷八§7.2、卷八§8.3 |
| KcsShPlateProp | 曲面板属性类（Thickness/Quality/Posno/GPS_1..4/SurfaceTreatment 等 Set*/Get*，Vitesse Python） | 卷七§3 |
| KcsShStiffProp | 曲面骨材属性类（ProfileType/Connection/EndCut/FilletWeldDepth 等，Vitesse Python） | 卷七§3 |
| KcsTBDVitDef | 默认值持久化（getDefaultdbm → %TEMP%\MenuDef.dbm） | 卷八§8.3 |
| KcsUtilDexPan | DEX 面板工具（getIntegerValue/getCompInd） | 卷八§8.3 |
| KcsUtilPan | 面板工具（getBox/getPlane/getLimitEnds/getUname） | 卷八§8.3 |
| KcsUtilPanSch | 面板语句工具（getGeo/getRef/getDefSurf/getGeoRepSSE） | 卷八§8.3 |
| KcsUtilPos | 位置工具（frp/lyp/lzp/coord_to_pos 封装） | 卷八§8.3 |
| Line3D/Line2D | 线类（ScalarComponentOfVector/Transform） | 卷八§8.1 |
| LineTypeDisplaySettings | 线型显示设置类（SetPattern/SetScaleFactor） | 卷八§8.3 |
| MARCONTOURPLANAR | 平面轮廓对象（getPointOnContour/contourPML） | 卷七§5 |
| MarDex | 数据抽取对象（extractPML/nextResultPML/getIntPML/getReal/getString/getBox/getIndexedReal） | 卷七§6、卷十三§3.1、卷七§5 |
| MARDRADRAFTINGAPI | Marine Drafting API 对象（dwgOpen/dwgSave/dwgClose/dwgRepaint） | 卷九§12 |
| MarDrafting | 出图对象（modelIdentify/DwgCurrent） | 卷七§5、卷十三§3.1 |
| MarElementHandle | Marine 元素句柄桥类 | 卷十三§3.1 |
| MarHoleManager | 开孔管理桥类 | 卷十三§3.1 |
| MARHULLPAN | 船体面板 marAPI 对象（stmtExec/stmtExecSingle/stmtGet/groupGet/panModify/panRecreate/getNearbySeams/getCutoutPoints 等全方法） | 卷一§14、卷七§2.10、卷七§5 |
| MarModel | Marine 模型桥类（partType/name/partId） | 卷七§5、卷十三§3.1 |
| MARPOINTPLANAR | 平面点对象（setCoordinates(u,v)） | 卷七§5 |
| MarPythonObjectPML | PML 侧 Python 桥正主类（21 方法；MarPythonObject 为 .NET 专用不可 new） | 卷十三§3.2 |
| MARTRANSFORMATION | 变换对象（setByRowFromArray/transform） | 卷七§5 |
| MarUi | 交互对象（pointPlanarReqPML/messageNoConfirm/AppWindowRefresh） | 卷十三§3.1、卷七§5 |
| MARUTIL | 工具对象（quitPML/OkPML/TraCoordShip/TBEnvironmentGet） | 卷七§5 |
| MarWorkspace | Marine 工作区桥类（MarWrapper.Workspace） | 卷十二§2.20、卷十三§1 |
| MDB | MDB 会话对象（object MDB(!currentMdb)） | 卷十一§5.2 |
| MDRROUTER | 电缆布线 .NET 对象（与 Pipe Router 无关） | 卷三§2 |
| MDSREST | MDS 约束对象（mode='CREATE'/create） | 卷十§1.4 |
| MDSSUPPORT | MDS 支撑对象（DATUM+ATTA+STRU 模型载体） | 卷十§1.4 |
| MEASURE | 度量对象（Pressure 等，currentUnits/cast 单位换算） | 卷四§2.3 |
| Model | 模型对象类（type/name/partType/partId/reflCode 全 Set/Get） | 卷八§8.3 |
| ModelDrawAssyCriteria | 装配绘制条件类（SetAssemblyName/IsRecursive） | 卷八§8.3 |
| ModelObjectRevision | 模型版本类（配 model_object_revision_*） | 卷八§8.3 |
| MovePanOptions | 面板移动选项类（SetPrincipalPlane/SetThreePoints/SetPlaneObject） | 卷七§4 |
| NAMOPT | 自动命名规则引擎对象（17 方法：load/save/rules/getName/nameString） | 卷四§0.1、卷十一§4.3 |
| NAMOPTRULE | 命名规则对象（6 参构造 + save） | 卷十一§4.3 |
| NetDataSource | NetGrid 数据绑定正主类（19 方法，GridControl） | 卷十三§3.2 |
| Object/ObjectCriteria | 对象与查询条件类（配 kcs_db.object_list_get） | 卷八§8.3 |
| PanelSchema | 语句 Schema Lib 类（KcsPanelSchema 同族） | 卷八§8.3 |
| PARTSFROMSPEC | 从规格生成零件对象（new prtele/new gpart 递归 SELE） | 卷四§0.1、卷四§3.6 |
| PFASSEMBLYACTIVITY | 装配活动对象（findSegments/getElbowActivity 等 26 方法） | 卷九§12 |
| PFBRANCHECK | 分支检查对象 | 卷九§12 |
| PFBRANTEECHECK | 三通检查对象 | 卷九§12 |
| PFEVALUATESPOOLMEMBER | 管段成员求值对象 | 卷九§12 |
| PFFLANGEROTATIONCHECK | 法兰旋转检查对象 | 卷九§12 |
| PFISODRAWINGMANAGER | 轴测图管理对象（createIsometrics，错误码 33,157） | 卷九§10、卷九§12 |
| PFPARTNO | 零件号对象（PARTNO CREATE） | 卷九§7、卷九§12 |
| PFPIPECONSISTENCYCHECK | 管路一致性检查对象 | 卷九§12 |
| PFPIPESPOOLDIMENSION | 管段图尺寸对象（PFM 版，错误码 64,277） | 卷九§12 |
| PFPIPESPOOLDWG | 管段图对象（45 方法） | 卷九§12 |
| PFPIPESPOOLMANAGER | PFM 管段管理对象（getBendingTables/getWeldingTables） | 卷九§12 |
| PFSPECCHECK | 规格检查对象 | 卷九§12 |
| PFSPOOLER | PFM Spooler 对象 | 卷九§12 |
| PFSPOOLVOLUME | 管段体积对象 | 卷九§12 |
| PFVALVEDIRCHECK | 阀门方向检查对象 | 卷九§12 |
| PFWELDCONTROL | PFM 焊接控制对象（33 方法：createWeldOnBranch/renumberAllWelds 等） | 卷九§6 |
| PFWELDDATA | 焊接数据对象 | 卷九§12 |
| PFWELDGAPCHECK | 焊缝间隙检查对象 | 卷九§12 |
| PFWELDINGTABLE | 焊接表对象 | 卷九§12 |
| PIPESPOOLDIMENSION | 管段图尺寸创建对象（createDimension(viewRef)） | 卷三§7 |
| PIPESPOOLMANAGER | 管段拆分/表达式管理对象（getBranchElements） | 卷三§7 |
| Plane3D | 平面类（IntersectLine/Transform） | 卷八§8.1 |
| PMLDataGridLayout | 数据网格布局类（77 方法，Presentation.DataGrid） | 卷十三§3.2 |
| PMLNetAny | PML 数据包装类（PMLNetReal 同族） | 卷十三§2 |
| PMLNetCallable | PMLNet 可调特性类（Aveva.PDMS.PMLNet.PMLNetCallable，无 Attribute 后缀） | 卷十三§2 |
| PMLNetCommandManager | 命令管理桥类（PDMSCommands，PMLNetCommand 20） | 卷十三§3.2 |
| PMLNetDelegate | PML 事件委托桥（嵌套 PMLNetEventHandler） | 卷十二§2.20、卷十三§2 |
| PMLNetEngine | PML/.NET 桥引擎（28 方法 LoadAssembly/ConstructClass/InvokeMethod…，object XXX() 执行通道） | 卷十三§2 |
| PMLNetException | PMLNet 异常桥类 | 卷十三§2 |
| Point2D | 2D 点类（含 Move(xmove,ymove)） | 卷八§8.1 |
| Point3D | 3D 点类（DistanceToPoint/SetFromMidpoint/Transform，X/Y/Z property） | 卷八§8.1 |
| Polygon2D/Polygon3D | 多边形类（AddPoint/GetPoint，2D __add__ 并集） | 卷八§8.1 |
| PrintOptions | 打印选项类（32 方法：PrinterName/ScaleToFit/Paper* 等） | 卷八§8.3 |
| ProfileSketch | 型材草图类（GetProfileType/GetEndcutType/GetBevelGapWeb/Flange） | 卷八§8.3 |
| PSINodeUDAS | PSI 节点 UDA 工具对象（:PsiSystem/:PSISifValue/:PSINodeType 等） | 卷十§4、卷十§7 |
| Rectangle2D | 矩形类（SetCorners/IsEmpty，模块常量 Infinity） | 卷八§8.1 |
| Rline3D/Rline2D | 射线类（__init__(startp,endp)） | 卷八§8.1 |
| RUNBATCHPROCESS | 批处理 .NET 对象（import 'PipeFabricationAddin'） | 卷九§9 |
| RunModeOptions | 运行模式选项类（SetConfirmGeneration/SetTraceOn） | 卷八§8.3 |
| SCTNSPEC | 型材规格对象（design\objects） | 卷四§0.1 |
| SELECTIONTABLE | 选择表操作对象（57 方法：createTable/newType/newQuestion/newItems/choose 等） | 卷四§4 |
| ShPlateProp/ShStiffProp | 板/骨材属性 Lib 类（对应 KcsShPlateProp/KcsShStiffProp） | 卷八§8.3 |
| SPCLINK | 规格选择窗体链接对象（selection/permissible/autoSelect） | 卷四§0.1、卷四§5.6 |
| SPCPCONNLIST | PCONN 列表对象（CKEY 75% 多数判定） | 卷四§3.4 |
| SPCPOINTRULE | 点规则对象（脚本可回放） | 卷四§3.4 |
| SPCPOINTSET | 点集对象（PMLLIB 常用规格对象） | 卷四§0.1 |
| SPCSCOM | SCOM 管理对象（getPSKeys/getPConns/setPconns/pConnsEqualTo） | 卷四§3.4 |
| SPCSEARCH | 规格搜索对象（PURPOSE/MATREF/FLUREF/RATING 准则，search/like） | 卷四§0.1、卷四§5.3 |
| SPCSKEY | SKEY 对象（skeyRef.skey，包 SDTEXT） | 卷四§3.4 |
| SPCSKEYRULE | SKEY 规则对象（includePPRule/getRule/print 可回放脚本） | 卷四§3.4 |
| SPCSPEC | 规格兼容性报表对象（check(ARRAY,STRING) 输出 PPoint 报表） | 卷四§7 |
| SPCSPECIFICATION | SELE/SPCO 匹配对象（defineWith/answerType/valid，bore 区间匹配） | 卷四§0.1、卷四§5.4 |
| SPECCOMPONENT | 规格元件对象（addStringAnswer/addRealAnswer/setRef/addComponent） | 卷四§3 |
| SPECDATA | 规格数据对象（选择窗体骨架成员） | 卷四§0.1、卷四§5.6 |
| SPECDFLTS | 规格缺省对象（选择窗体 .dflts 成员） | 卷四§0.1、卷四§5.6 |
| SPECIFICATION | 设计侧规格对象（bores/loadComponents/components/subTypes/loadTable/availableBores） | 卷四§5.5 |
| SPECIFICATIONS | 规格选件查询对象（loadComponents/components(type,questions,answers)） | 卷一§11、卷三§3、卷四§5.5 |
| SpecSearch | 规格搜索 Lib 类 | 卷八§8.3 |
| SPLBENDN | BEND 编号对象 | 卷九§4 |
| SPLCOMMONN | Spooler 编号基类（start/autoAssign/renumber/merge/undo 等） | 卷九§4 |
| SPLFIELDN | FIELD 编号对象 | 卷九§4 |
| SplitPanOptions | 面板剖分选项类（SetCuttingPlane/AddPanelMapping） | 卷七§4 |
| SPLJOINTN | JOINT 编号对象 | 卷九§4 |
| SPLMTO | MTO 构建引擎对象（buildMto/collectComps/getBolts/totalWeights/print） | 卷九§5 |
| SPLMTOBOLT | MTO 螺栓数据类 | 卷九§5 |
| SPLMTOCOMP | MTO 组件数据类 | 卷九§5 |
| SPLMTOMTOR | MTO 参照数据类 | 卷九§5 |
| SPLMTOOPTIONS | MTO 选项类 | 卷九§5 |
| SPLMTOTUBE | MTO 管数据类 | 卷九§5 |
| SPLPARTN | PART 编号对象 | 卷九§4 |
| SPLSPOOLN | SPOOL 编号对象（align/update/check/renumber/highlight） | 卷九§4 |
| SPLWELDN | WELD 编号对象 | 卷九§4 |
| Stat_point2D_req/Stat_point3D_req | 交互状态类（Locktype/Initial3D/SetCursorType） | 卷八§8.2 |
| STCHOOSEDATA | 选择数据对象（setData 12 重载/getSelTabs/getItemSelectionTable） | 卷四§7 |
| Stringlist/Symbollist | 字符串/符号列表类（AddString/AddSymbol） | 卷八§8.3 |
| stringutils | 字符串工具（TrimNum/IsStringAllowed/ScanFile） | 卷八§8.3 |
| Symbol/Text/Colour/Linetype/Layer | 环境字典类族（Text 36 方法全 Set/Get） | 卷八§8.3 |
| SymbolicView | 符号视图解释类（SetPlaneBy3Points/SetDepth/DrawRSO 等 30+ 开关） | 卷八§8.3 |
| TbBaseException | 扩展异常基类（strFunctionName/strModuleName/strError 属性名不得更改） | 卷八§8.2 |
| Transformation2D | 2D 变换类（IdentityTransf/Rotate/Scale/Reflect + 分解 GetScale/GetRotation） | 卷八§8.1 |
| Transformation3D | 3D 变换类（Combine/Invert/Rotate/Translate/SetByRowFromArray） | 卷八§8.1 |
| TribonDwg2Svg | SVG 转换类（27 def） | 卷八§8.3 |
| UNDOABLE | 可撤销事务对象（description/add/endUndoable、undoaction/redoaction） | 卷三§7、卷十§2.3 |
| USER | 用户对象（object USER(!user)，access 权限判定） | 卷十一§5.2 |
| Vector2D | 2D 矢量类 | 卷八§8.1 |
| Vector3D | 3D 矢量类（AngleToVector/DotProduct/Rotate/ProjectOnPlane 等） | 卷八§8.1 |
| VNETError | VNET 错误对象（Reset） | 卷十§7 |
| VNETWriteASMXML | VNET 装配 XML 导出对象 | 卷十§7 |
| VNETWriteSPLXML | VNET Spooler XML 导出对象 | 卷十§7 |
| VNETWriteXML | VNET Design XML 导出对象 | 卷十§7 |
| Weld/WeldedJoint/WeldTable | 焊接类族（WeldName/BevelCode/SetWeldedJoint 等） | 卷八§8.3 |

## 表 C：kcs_* Python 函数索引（按模块）

> 来源：卷七《Hull船体建模语句大全》§2.10/§3/§4/§6/§8 + 卷八《Vitesse-Python-API全编》全卷。kcs_* 为编译进 Marine 主程序的 C 扩展模块，签名从官方示例与 Lib 库真实调用反演；每个模块带 `.error` 字符串属性（可写注入）。


### kcs_assembly（1 项）

| 函数 | 签名摘要 | 锚 |
|---|---|---|
| assembly_activate/save/cancel、assembly_exist | assembly_activate/save/cancel、assembly_exist(name)、assembly_properties_get 装配体族 | 卷八§6 |

### kcs_att（3 项）

| 函数 | 签名摘要 | 锚 |
|---|---|---|
| attribute_first_get | attribute_first_get(model,1)/attribute_next_get(1) 属性遍历 | 卷八§6 |
| attribute_is | attribute_is(att, <type码>)/attribute_create(model,"General","ModelUnit") 属性判定/创建 | 卷八§6 |
| string_set/integer_get/real_get/string_get、model_save | string_set/integer_get/real_get/string_get、model_save(model) 属性值读写 | 卷八§6 |

### kcs_cable（1 项）

| 函数 | 签名摘要 | 锚 |
|---|---|---|
| cable_activate/save/cancel、cway_activate/save/cancel | cable_activate/save/cancel、cway_activate/save/cancel 电缆/路径激活族 | 卷八§6 |

### kcs_chm（21 项）

| 函数 | 签名摘要 | 锚 |
|---|---|---|
| cpan_hole_create | cpan_hole_create(panelName, HoleOptions) 曲面板开孔（KcsPanHoleOptions） | 卷七§3 |
| curve_planar_create | curve_planar_create(CurveName, Plane, MinPt, MaxPt, SurfaceName) 平面曲线 | 卷七§3 |
| curve_principal_create | curve_principal_create(CurveName, "X=40000", MinPt, MaxPt, SurfaceName) 主平面曲线 | 卷七§3 |
| output_XML | output_XML(ModelList, file) 输出 XML | 卷七§3 |
| plate_prop_get | plate_prop_get(model)/plate_prop_set(model, prop) 板属性读写（KcsShPlateProp） | 卷七§3 |
| recreate | recreate(Long) 重建模型 | 卷七§3 |
| remarking_length | remarking_length(from, along, to) 余量链标注（act 位标志见锚处） | 卷七§3 |
| remarking_length_ext | remarking_length_ext(act, hullpanname, from, along, to) 扩展余量标注 | 卷七§3 |
| run_XML | run_XML(xml, log) XML 建模执行 | 卷七§3 |
| stiffener_combine | stiffener_combine(Stiff1, Stiff2) 骨材合并 | 卷七§3 |
| stiffener_prop_get | stiffener_prop_get(model)/stiffener_prop_set(model, prop) 骨材属性读写（KcsShStiffProp） | 卷七§3 |
| stiffener_split | stiffener_split(ObjToSplit, SplittingObj) 骨材拆分 | 卷七§3 |
| stiffener_to_profdb | stiffener_to_profdb(Stiff1) 骨材转 PROFL DB | 卷七§3 |
| store | store(Model)/skip(Model)/delete(Model) 存储/跳过/删除 | 卷七§3 |
| view_bodyplan_new | view_bodyplan_new(body) 横剖视图 | 卷七§3 |
| view_curvedpanel_new | view_curvedpanel_new(object, options) 曲面板视图 | 卷七§3 |
| view_devpla_new | view_devpla_new(object) 展开板视图 | 卷七§3 |
| view_modify | view_modify(view) → view_options 修改视图 | 卷七§3 |
| view_recreate | view_recreate(view) 重建视图 | 卷七§3 |
| view_shellexp_new | view_shellexp_new(shellx) 外板展开视图 | 卷七§3 |
| view_shprof_new | view_shprof_new(model) 曲面骨材视图 | 卷七§3 |

### kcs_db（1 项）

| 函数 | 签名摘要 | 锚 |
|---|---|---|
| object_list_get | object_list_get(criteria, dbname, list) 对象列表收集（配 ObjectCriteria） | 卷八§6 |

### kcs_dex（4 项）

| 函数 | 签名摘要 | 锚 |
|---|---|---|
| extract | extract(est) 执行提取表达式 | 卷七§6、卷八§4 |
| get_indexedreal | get_indexedreal(0..15) 取 4x4 变换矩阵元素 | 卷七§6 |
| get_int | get_int()/get_real()/get_string()/get_reavec3d()/get_box()/get_reavec2d()/get_indexedreal(i) 按类型码取值 | 卷七§6、卷八§4 |
| next_result | next_result() → 类型码（1=int 2=real 3=string 4=vec3d 5=box 6=vec2d >10 列表 ≥25 4x4 矩阵） | 卷七§6、卷八§4 |

### kcs_draft（88 项）

| 函数 | 签名摘要 | 锚 |
|---|---|---|
| arc_new | arc_new 圆弧创建 | 卷八§3.1 |
| circle_new | circle_new 圆创建 | 卷八§3.1 |
| cloud_new | cloud_new 云线创建 | 卷八§3.1 |
| colour_get/set | colour_get/set 当前模态颜色 | 卷八§3.6 |
| component_new | component_new 组件创建 | 卷八§3.1 |
| conic_new | conic_new 圆锥曲线创建 | 卷八§3.1 |
| contour_new | contour_new 轮廓创建 | 卷八§3.1 |
| cross_new | cross_new 十字标记创建 | 卷八§3.1 |
| default_value_get/set | default_value_get/set 缺省值 | 卷八§3.6 |
| delete_by_area | delete_by_area 区域删除（配 kcsDEL_INSIDE/OUTSIDE） | 卷八§3.5 |
| dim_angle_new | dim_angle_new 角度标注创建 | 卷八§3.1 |
| dim_diameter_new | dim_diameter_new 直径标注创建 | 卷八§3.1 |
| dim_linear_new | dim_linear_new 线性标注创建 | 卷八§3.1 |
| dim_point_3d | dim_point_3d 3D 点标注 | 卷八§3.1 |
| dim_radius_new | dim_radius_new 半径标注创建 | 卷八§3.1 |
| dim_shell_new | dim_shell_new 壳体标注 | 卷八§3.1 |
| dwg_close/save/save_as/exist/delete | dwg_close/save/save_as/exist/delete 图纸生命周期族 | 卷八§3.8 |
| dwg_dxf_export/dwg_dxf_import/dwg_dxf_3d_export | dwg_dxf_export/dwg_dxf_import/dwg_dxf_3d_export DXF 交换 | 卷八§3.9 |
| dwg_layers_is_shown/is_hidden/shown_get/hidden_get | dwg_layers_is_shown/is_hidden/shown_get/hidden_get 图层状态查询 | 卷八§3.9 |
| dwg_name_get | dwg_name_get 图纸名 | 卷八§3.8 |
| dwg_new | dwg_new(name, form, dwgtype) 新建图纸 | 卷八§3.8 |
| dwg_open | dwg_open(name, dwgtype, mode, revision) 打开图纸（kcsOPENMODE_READONLY/READWRITE） | 卷八§3.8 |
| dwg_print | dwg_print 打印（配 PrintOptions） | 卷八§3.8 |
| dwg_properties_set/get | dwg_properties_set/get 图纸属性 | 卷八§3.8 |
| dwg_repaint | dwg_repaint 重绘 | 卷八§3.8 |
| dwg_revision_freeze/unfreeze/new | dwg_revision_freeze/unfreeze/new 图纸版本冻结/新建 | 卷八§3.9 |
| dwg_status_set | dwg_status_set 状态设置 | 卷八§3.8 |
| dwg_type_list_get | dwg_type_list_get 图纸类型列表 | 卷八§3.8 |
| element_child_first_get | element_child_first_get 首子元素 | 卷八§3.5 |
| element_colour_get/set | element_colour_get/set 颜色读写 | 卷八§3.5 |
| element_copy | element_copy 复制元素 | 卷八§3.5 |
| element_delete | element_delete 删除元素 | 卷八§3.5 |
| element_extent_get | element_extent_get 范围获取 | 卷八§3.5 |
| element_highlight | element_highlight 高亮元素 | 卷八§3.5 |
| element_identify | element_identify 元素标识 | 卷八§3.2 |
| element_is_text/is_contour/is_symbol/is_subpicture/is_view/is_subview/is_component/is_burning_sketch/is_detail_sketch/is_nesting/is_dimension/is_note/is_posno/is_hatch | element_is_text/is_contour/is_symbol/is_subpicture/is_view/is_subview/is_component/is_burning_sketch/is_detail_sketch/is_nesting/is_dimension/is_note/is_posno/is_hatch 图元类型判定 | 卷八§3.4 |
| element_layer_get/set | element_layer_get/set 图层读写 | 卷八§3.5 |
| element_linetype_get/set | element_linetype_get/set 线型读写 | 卷八§3.5 |
| element_parent_get | element_parent_get 父元素 | 卷八§3.5 |
| element_sibling_next_get | element_sibling_next_get 下一兄弟元素 | 卷八§3.5 |
| element_transform | element_transform 变换元素 | 卷八§3.5 |
| element_transformation_get/redefine | element_transformation_get/redefine 变换矩阵读取/重定义 | 卷八§3.5 |
| element_visibility_get/set | element_visibility_get/set 可见性读写 | 卷八§3.5 |
| ellipse_new | ellipse_new 椭圆创建 | 卷八§3.1 |
| general_restr_symbol_new | general_restr_symbol_new 通用约束符号创建 | 卷八§3.1 |
| geocontour_function | geocontour_function 2D 轮廓函数 | 卷八§3.9 |
| geometry_identify/contour_identify/dim_identify/note_identify/posno_identify/text_identify/symbol_identify/hatch_identify/point_identify | geometry_identify/contour_identify/dim_identify/note_identify/posno_identify/text_identify/symbol_identify/hatch_identify/point_identify 各类图元标识 | 卷八§3.2 |
| hatch_island_new | hatch_island_new 剖面线孤岛创建 | 卷八§3.1 |
| hatch_new | hatch_new 剖面线创建 | 卷八§3.1 |
| hatch_pattern_set/userdef_hatch_pattern_set/std_hatch_pattern_set | hatch_pattern_set/userdef_hatch_pattern_set/std_hatch_pattern_set 剖面线图案设置 | 卷八§3.6 |
| highlight_off/point_highlight/contour_highlight | highlight_off/point_highlight/contour_highlight 高亮开关族 | 卷八§3.5 |
| layer_show_all/show/hide | layer_show_all/show/hide 图层显示控制 | 卷八§3.9 |
| line_new | line_new 直线创建 | 卷八§3.1 |
| linetype_display_settings_get/set | linetype_display_settings_get/set 线型显示设置 | 卷八§3.6 |
| model_draw/model_colour_set/model_layer_set/model_properties_get/model_delete | model_draw/model_colour_set/model_layer_set/model_properties_get/model_delete 模型显示控制族 | 卷八§3.7 |
| model_identify | model_identify(point) → (model, subview, comp) 模型标识 | 卷八§3.2 |
| model_object_revision_get/set/save | model_object_revision_get/set/save 模型版本 | 卷八§3.7 |
| note_new | note_new 注释创建 | 卷八§3.1 |
| pipe_restr_symbol_new | pipe_restr_symbol_new 管路约束符号创建 | 卷八§3.1 |
| point_new | point_new 点创建 | 卷八§3.1 |
| point_transform | point_transform 3D→2D 点变换 | 卷八§3.7 |
| position_ruler_new | position_ruler_new 位置标尺创建 | 卷八§3.1 |
| posno_symbol_set、posno_height_get/set | posno_symbol_set、posno_height_get/set 件号模态属性 | 卷八§3.6 |
| rectangle_new | rectangle_new 矩形创建 | 卷八§3.1 |
| reference_move | reference_move 参照移动 | 卷八§3.9 |
| ruler_new | ruler_new 标尺创建 | 卷八§3.1 |
| shd_new/shd_projection_set/shd_zoom_box/shd_autoscale | shd_new/shd_projection_set/shd_zoom_box/shd_autoscale 外板展开图（Shell Difficulty） | 卷八§3.9 |
| spline_new | spline_new 样条创建 | 卷八§3.1 |
| subpicture_current_get/set | subpicture_current_get/set 当前子图 | 卷八§3.7 |
| subpicture_save/insert、subpicture_name_get/set | subpicture_save/insert、subpicture_name_get/set 子图操作 | 卷八§3.9 |
| subview_new | subview_new 子视图创建 | 卷八§3.1 |
| symbol_new | symbol_new 符号创建 | 卷八§3.1 |
| symbol_rotation_get/set、symbol_height_get/set | symbol_rotation_get/set、symbol_height_get/set 符号模态属性 | 卷八§3.6 |
| text | text 属性 getter 集（height/rotation/slant/aspect/bold/italic/underline/strikeout/ascii_font，Lib\KcsText） | 卷八§3.6 |
| text_height_set/slant_set/aspect_set | text_height_set/slant_set/aspect_set 文本模态属性 | 卷八§3.6 |
| text_new | text_new 文本创建 | 卷八§3.1 |
| view_capture/subview_capture/component_capture/model_capture/dim_capture/note_capture/posno_capture/hatch_capture/text_capture/symbol_capture/contour_capture/point_capture/geometry_capture | view_capture/subview_capture/component_capture/model_capture/dim_capture/note_capture/posno_capture/hatch_capture/text_capture/symbol_capture/contour_capture/point_capture/geometry_capture 图元捕获（capture 系） | 卷八§3.3 |
| view_hl_remove | view_hl_remove 消隐移除 | 卷八§3.7 |
| view_identify/subview_identify/component_identify | view_identify/subview_identify/component_identify 视图/子视图/组件拾取标识 | 卷八§3.2 |
| view_move | view_move 视图移动 | 卷八§3.7 |
| view_new | view_new 视图创建 | 卷八§3.1 |
| view_projection_get/set | view_projection_get/set 投影设置 | 卷八§3.7 |
| view_restriction_area_get | view_restriction_area_get 视图限制区 | 卷八§3.7 |
| view_scale | view_scale 视图比例 | 卷八§3.7 |
| view_slice_planes_get | view_slice_planes_get 切片平面 | 卷八§3.7 |
| view_slicedepth_get | view_slicedepth_get 切片深度 | 卷八§3.7 |
| view_symbolic_new | view_symbolic_new 符号视图创建 | 卷八§3.1 |
| zoom_extent_get/dwg_zoom | zoom_extent_get/dwg_zoom 缩放 | 卷八§3.7 |

### kcs_equip（1 项）

| 函数 | 签名摘要 | 锚 |
|---|---|---|
| equip_activate/save/cancel | equip_activate/save/cancel 设备激活/保存/取消 | 卷八§6 |

### kcs_gui（3 项）

| 函数 | 签名摘要 | 锚 |
|---|---|---|
| menu_add | menu_add(main_menu, num, title) 加菜单 | 卷八§5 |
| menu_get | menu_get(None, 0) 取主菜单 | 卷八§5 |
| menu_item_usr_add | menu_item_usr_add(menu, index, caption, "脚本名") 挂用户菜单项（脚本需实现 run/add/pre/post） | 卷八§5、卷八§7 |

### kcs_hull（6 项）

| 函数 | 签名摘要 | 锚 |
|---|---|---|
| pan_curve_create | pan_curve_create(viewhandle, panel, curvename, plane, contour) 建面板曲线 | 卷七§2.10 |
| pan_curve_store | pan_curve_store(viewhandle, curvename, contour) 存面板曲线 | 卷七§2.10 |
| pan_exec_stmt | pan_exec_stmt(0, stmt) 执行语句 | 卷七§2.10 |
| pan_init | pan_init(name, name) 初始化 | 卷七§2.10 |
| pan_modify | pan_modify(panel, 2) 触发面板修改 | 卷七§2.10 |
| pan_recreate | pan_recreate()/pan_store()/pan_skip() 重建/存储/跳过 | 卷七§2.10 |

### kcs_hullpan（24 项）

| 函数 | 签名摘要 | 锚 |
|---|---|---|
| group_next | group_next(panel, -2, 0) 组遍历 | 卷七§2.10 |
| pan_activate | pan_activate(hullpanname) 激活面板 | 卷七§4 |
| pan_copy | pan_copy(modelName, opt) 复制面板（CopyPanOptions） | 卷七§4 |
| pan_delete | pan_delete(hullpanname) 删除面板 | 卷七§4 |
| pan_group_delete | pan_group_delete(hullpanname, dict) 删语句组 | 卷七§4 |
| pan_group_divide | pan_group_divide(hullpanname, dict, [model,…]) 组二分 | 卷七§4 |
| pan_init | pan_init(name, scheme) 初始化面板 | 卷七§2.10 |
| pan_list_active | pan_list_active() → list 当前激活面板 | 卷七§4 |
| pan_move | pan_move(modelName, moveOpt) 移动面板（MovePanOptions） | 卷七§4 |
| pan_recreate | pan_recreate(hullpanname) 重建面板 | 卷七§4 |
| pan_remove_seam | pan_remove_seam(hullpanname, seamNo) 去除板缝 | 卷七§4 |
| pan_skip | pan_skip(name)/pan_skip() 跳过面板 | 卷七§4 |
| pan_split | pan_split(panelName, splitOpt) 剖分面板（SplitPanOptions） | 卷七§4 |
| pan_sti_split_by_model | pan_sti_split_by_model(dictgroup, dict) 按模型拆骨材 | 卷七§4 |
| pan_sti_split_by_plane | pan_sti_split_by_plane(dictgroup, dict) 按平面拆骨材 | 卷七§4 |
| pan_store | pan_store()/pan_store(name) 存储面板 | 卷七§4 |
| pan_store_single | pan_store_single(name)/pan_skip_single(name) 单面板存储/跳过 | 卷七§2.10 |
| pan_topology | pan_topology(model, 'defining'|'dependent primary'|'dependent all') 拓扑查询 | 卷七§4 |
| stmt_exec | stmt_exec(组号, 语句) 执行 HML 语句（组0=新组） | 卷七§2.10 |
| stmt_exec_single | stmt_exec_single(组号, 语句, 面板名) 单面板执行 | 卷七§2.10 |
| stmt_get | stmt_get(panel, group) 取语句组文本 | 卷七§2.10 |
| view_detail_new | view_detail_new(2|3|4|5, nElemHandle) 符号详图视图（2=Flange 3=Stiffener 4=Bracket 5=Seam） | 卷七§1.3、卷七§4 |
| view_symbolic_modify | view_symbolic_modify(nViewHandle) 修改符号视图 | 卷七§4 |
| view_symbolic_recreate | view_symbolic_recreate(nViewHandle) 重建符号视图 | 卷七§4 |

### kcs_ic（2 项）

| 函数 | 签名摘要 | 锚 |
|---|---|---|
| colour_names_get | colour_names_get()/linetypes_get()/layer_desc_get(id)/font_name_get 环境字典查询 | 卷八§6 |
| intersection_points_get/contour_split/transf_combine_2d | intersection_points_get/contour_split/transf_combine_2d 等 2D 变换族 | 卷八§6 |

### kcs_model（4 项）

| 函数 | 签名摘要 | 锚 |
|---|---|---|
| model_hull_contact | model_hull_contact(model) → 模型列表 船体接触检查 | 卷八§6 |
| model_interference_check | model_interference_check(model, outfittype) 干涉检查（equipment/struct/pipe/ventilation/cable） | 卷八§6 |
| model_properties_get/set | model_properties_get/set(model[, tdm]) 模型属性 | 卷八§6 |
| status_values_get | status_values_get(type)/model_status_set(model, type, value) 状态值（kcsSTATTYPE_*） | 卷八§6 |

### kcs_modelstruct（1 项）

| 函数 | 签名摘要 | 锚 |
|---|---|---|
| block_new | block_new(name,min,max)/block_delete、system_new(name,descr[,code])/system_delete、module_new/module_delete 块/系统/模块管理 | 卷八§6 |

### kcs_pipe（1 项）

| 函数 | 签名摘要 | 锚 |
|---|---|---|
| pipe_activate | pipe_activate(name)/pipe_save()/pipe_cancel() 管路激活/保存/取消 | 卷八§6 |

### kcs_struct（1 项）

| 函数 | 签名摘要 | 锚 |
|---|---|---|
| struct_activate/save/cancel | struct_activate/save/cancel 结构激活族 | 卷八§6 |

### kcs_tm（1 项）

| 函数 | 签名摘要 | 锚 |
|---|---|---|
| getTMList{Min,Average,Max} | getTMList{Min,Average,Max}(model, tmList) 壳厚预测 | 卷八§6 |

### kcs_ui（16 项）

| 函数 | 签名摘要 | 锚 |
|---|---|---|
| answer_req | answer_req(title, question)/req_answer(...) → yes/no/cancel 码 | 卷八§2 |
| app_window_minimize | app_window_minimize()/maximize()/restore()/refresh() 主窗口控制 | 卷八§2 |
| choice_select | choice_select(title, prompt, actions) → (res, index) 选项列表 | 卷八§2 |
| colour_select | colour_select(prompt, colour) → (res, Colour) 颜色选择 | 卷八§2 |
| init_highlight | init_highlight(...)/terminate_highlight(...) 高亮控制 | 卷八§2 |
| int_req | int_req(prompt[, default]) → (res, int) 整数输入 | 卷八§2 |
| message_noconfirm | message_noconfirm(msg)/message_confirm(msg)/message_debug(msg) 消息框 | 卷八§2 |
| model_info | model_info(point) 弹出模型信息 | 卷八§2 |
| pic_draw_mod | pic_draw_mod(type, name, mode) 打开/绘制模型图 | 卷八§2 |
| point2D_req | point2D_req(prompt, point[, status[, buttons]]) → (res, point) 2D 点交互 | 卷八§2 |
| point3D_req | point3D_req(prompt, status, point3d) → (res, point) 3D 点交互 | 卷八§2 |
| real_req | real_req(prompt[, default]) → (res, real) 实数输入 | 卷八§2 |
| req_choice | req_choice(prompt, default) → (res, choice) 选择请求 | 卷八§2 |
| req_pick_mod | req_pick_mod(prompt, x, y) → (res,…, ref) 模型拾取 | 卷八§2 |
| string_req | string_req(prompt[, default])/req_string(...) → (res, str) 字符串输入 | 卷八§2 |
| string_select | string_select(title, group, prompt, stringlist) → (res, index) 字符串列表选择 | 卷八§2 |

### kcs_util（13 项）

| 函数 | 签名摘要 | 锚 |
|---|---|---|
| cancel | cancel() 取消返回码 | 卷八§1 |
| coord_to_pos | coord_to_pos(plane, value) → (res, posstr) 坐标转位置串（1=X/FR 2=Y/LP 3=Z） | 卷八§1 |
| drafting | drafting() 判定当前是否 Drafting 环境 | 卷八§1 |
| exit_function | exit_function()/exit_program() 请求退出 | 卷八§1 |
| ok | ok() 正常确认返回码 | 卷八§1 |
| pos_to_coord | pos_to_coord(...) 位置串转坐标 | 卷八§1 |
| quit | quit()/options()/operation_complete() EF/OPTIONS/完成键返回码 | 卷八§1 |
| success | success()/failure() 通用布尔状态 | 卷八§1 |
| TB_environment_get | TB_environment_get(name)/TB_environment_set(name, value) TB 环境变量读写 | 卷八§1 |
| trigger_ok | trigger_ok()/trigger_abort() 触发器确认/中止 | 卷七§8、卷八§1、卷八§7.1 |
| trigger_override | trigger_override() pre 触发器覆盖原函数 | 卷八§1、卷八§7.1 |
| u_lock | u_lock()/v_lock()/unlock() point2D_req 锁定按钮码 | 卷八§1 |
| yes | yes()/no() answer_req 应答码 | 卷八§1 |

### kcs_weld（1 项）

| 函数 | 签名摘要 | 锚 |
|---|---|---|
| weld_calculation | weld_calculation(assembly, flag)、weld_properties_get/set(assembly, WeldTable)、weld_delete 焊接计算族 | 卷八§6 |


## 附：错误码/属性表/DEX 关键词的查找路径指引

| 主题 | 去处（本索引不重复其内容） |
|---|---|
| handle 错误码 | 《Marine-PML错误码速查.md》（§1 模块号对照、§2 高频码、§5 九卷域化增补）；卷二§10、卷六§8、卷七§8、卷九§13、卷十§1.6 各卷域化速查表 |
| 元素类型权威属性 | 《Marine-元素类型属性权威表.md》（30 类元素 × DMRM §4/§6 权威属性：EQUI/BRAN/PIPE/STRU/SCTN/GENSEC/BOX/CYLI/NOZZ/FLAN/VALV/TEE/REDU/ELBO/ATTA/SLAB/PLAT/EXTR/LOOP/VRTX/NOTE/TEXP/LDIM/VIEW/SHEE/DRWG/LAYER/SKEY/POSITION/SUBS） |
| DEX 关键词 | 卷七§6（源码 42 例）→ 权威全集在 `PML语料\xls_tables\_ANALYSIS.md` §3b/§4 与 38 份 TSV（1502 条关键词链）；DMRM Ch17 映射；PML 侧走 MARDEX（卷七§5）、Python 侧走 kcs_dex（表 C） |
| PML 内置对象 API（ARRAY/STRING/REAL/COLLECTION/EXPRESSION/FILE/BLOCK/FORM/FORMAT/POSITION/…共 75 类） | 《Marine-PML对象API字典精要.md》（§2.5 全目录随用随查） |
| 表单语法（setup form / gadget 体系） | 《Marine-PML表单语法精要.md》；控件关键字频次见卷十一§5.1 |
| EDG 事件/拾取体系 | 《Marine-EDG事件系统精要.md》（edgCntrl/edgPacket/edgPick 全参考）；托管面 = MarWrapper 的 Aveva.Marine.Events（卷十三§1） |
| marAPI 调用姿势 | 《AVEVA-Marine-marAPI调用姿势表.md》——注意卷十三§3.3 的 15 条勘误（MarEllipse/MarBoxPlanar/MarRectangle 为幽灵类；MarPythonObjectPML 才是 PML 侧 Python 桥） |
| .NET PMLNetCallable 全量 184 类 | 卷十三§3 + `E:\aveva开发文档\_reflect_survey\`（pmlnetcallable.txt 3535 行、pmlnetcallable_index.csv、key_types.csv） |
| 官方手册原文（140 本全文） | 卷十四§5 使用法：`findstr /n /i "命令词" PML语料\pdf_text\<手册名>.txt` 按 `===== PAGE n ====` 回原文；手册与源码冲突时以源码实证优先 |
| 三件套（只登记，不提取） | 《PML生成规范的冲突文件 2026-09-08 20：34：14.859610.md》、《PML审核规范.md》、《PML记忆-语法硬约束与生成审核规范的冲突文件 2026-09-08 20：34：14.855611.md》 |
| 跨技术选型 | 卷十二§1 五轨道对照（同一操作在 PML 宏/PML2/marAPI/.NET/Vitesse Python 的等价写法全部注明出处卷） |
