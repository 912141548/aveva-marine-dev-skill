# Marine 官方手册增补·卷十四（手册 vs 卷本交叉核对）

> 来源：Documentation 目录 118 CHM 全部反编译成功（`C:\Windows\hh.exe -decompile`，此前会话失败系未尝试该工具）+ 9 直提 PDF，共收割约 95 本官方手册；PML语料\pdf_text\ 新增 128 个 .txt（23.5MB），**总计 140 本手册全文入库**。提取脚本：`_extract_doc_pdfs.py`、`_extract_chm_pdfs.py`、`_chm_to_text.py`（pypdf 6.18.0）。
> 本卷登记"手册有、卷本没有"的增补点与两边差异；全部原文可按 `手册名.txt` + PAGE n 回查。

## 1. 新入库重磅手册（节选）

| 手册 | 页数 | 内容 |
|---|---|---|
| **DMRM**（Data Model RM） | 826 | **Ch4 Design 库 491 个元素类型**（Attributes + Legal Owners + Legal Members = 层级规则权威表）、Ch2 目录库、Ch15 伪属性总表、Ch17 DEX 关键词映射 |
| **DBRM**（Database Management RM） | 251 | 导航/属性/单位/COLLECT/OUTPUT/CLEANUP 全语法（12.1.SP3/SP4 更新版） |
| **CSRM/CSUG**（Catalogues & Specifications，Paragon） | 205+226 | SPECONMODE 制表语法全链、Selector 问题清单、PBORE0/PCONN0 特例 |
| **DRUGP**（DRAFT UG） | 371 | VIEW/LAYER/尺寸标注/标签/Autotag 全命令语法 |
| Drafting（Marine Draft UG） | 462 | SDB 体系按菜单（SP3/SP4 新增项标注） |
| **ISORM + ISOUG** | 262+137 | Isodraft 命令总览 7 类约 70 条、DETAIL 全语法 |
| DRMPCM（Design RM: Creating the Model） | 202 | Outfitting 定位/连接语法大全（POSITION AT/BY/INFRONT/BEH/UNDER PIN/镜像） |
| Hull 系列 5 本（HullDab/Init_Hull/Concepts/Nesting 等） | ~550 | 船体库 DESI+MANU 双库、隐式 Claim、套料 |
| Setup_Customisation | 706 | 环境定制 |
| Lines(554p)/Planar_Modelling(530p)/Hydro(320p)/HVACUG(512p)/Diagrams(364p)/SCHMM(252p) 等 | — | 各模块 UG |

---

## 2. 手册有、卷本没有（增补点 42 项，按域分组）

### 2.1 DB/导航（DBRM）

```pml
Q BACKREF (ATTNAME SPCO)          $* ★ SP4 新增：反向查"谁引用我"
SAME                              $* 返回前一个 CE（拆管 splitpipe 同款）
GOTO FRSTW CATA                   $* 到首个 CATA world（规格搜索同款）
!MyEle = ( next box of /VESS1 )   $* ID 表达式赋值不改变 CE
-- 导航伪属性表（PAGE 52）：ALLELE CONNECTIONS(H) DDEP FRSTW MAXD MBACK MCOU MEMB OWNLST PARENT SEQU TYSEQU
-- 属性量纲总表（约 50 项）：DIST=mm ANGL BORE MASS CUDI VFLO...（含哈希码与数据库单位）
-- 属性查询四列表：ATTLIS / ATTOUT / UDALIS / PSATTS
Q PPOS(1) / Q LASTMOD(ATTNAME XLEN) / Q MEMBER(TYPENAME BOX) / Q DESP NUM 3 TO 5
XLEN $!A                          $* 命令式设属性必须 $ 展开；!!CE.XLEN = 99（= 后必须空格）
-- 动态组（SP4 新增）：
SCOSEL ALL EQUI FROM CLAIMLIST
ALL BRAN MEMBERS WHERE (SPREF EQ /MYSPEC)
-- COLLECT 进阶变体：
VAR !a COLLECT ALL WITH (XLEN*YLEN*ZLEN GT 1000)
COLLECT ... WITHIN W800N17000U0 TO W1400N13500U1200
COLLECT ALL PIPE EXCLUSIVE WITHIN VOLUME /PUMP1 1500
COLLECT ... FOR /PIPE1 EXCLUDE BRAN 1 OF /PIPE2
COLLECT ... FROM TABLE SPRE VALUE /RF300/100G / FROM TABLE :MYATT VALUE 100 TO 110
Q VOLUMEOPTION HULL DESIGN        $* ★ Marine 专属：体查询只返回设计或生产数据其一（HULL PRODUCTION ON/OFF）
-- OUTPUT 变更追踪全语法（PAGE 182-184）：
OUTPUT /PIPE-100 CHANGES
OUTPUT ALL PIPE FOR /ZONE CHANGES SINCE 21 JANUARY
OUTPUT ... CHANGES SINCE EXTRACT 44 / SINCE LATEST EXTRACT / SINCE SESSION 77 EXTRACT 44
  （选项：COMMENT TABULATE n INDEX BRIEF NOUDA ONLY (NOUN...) PASS 1|2 OLDFORMAT LOCATE REPLACE）
-- CLEANUP（SP3 新增整章）：
Q NULLRE (ATTNAME att) / Q UNRESO / Q INVREF
CLEANU NULL|INVALID|UNRESOLVED attribute [ON noun] [FOR ele] [SETNULL|DELETE]
  例：CLEANU NULL STLREF ON EQUI DELETE
```

### 2.2 Draft（DRUGP）

```pml
-- 层级（PAGE 29-31）：NEW DEPT/REGI/SHEET 可省略——仅 NEW DRWG 与 NEW VIEW 必需，中间层自动补建
-- VIEW 视区（3.11.3）：
VREGION @ / FROM X..Y.. TO X..Y.. / TL|TR|BL|BR|C / VERTICAL U|D|L|R
THPO E N U（=LOOK THROUGH）/ THPO ID @ / FRPO（=LOOK FROM）/ ONPO
AUTOSCALE（设 IDLN/THPO/VSCA，二次执行不重设 IDLN）/ AUTOSIZE
TURN value（=ADEG）/ VTYP WIRE|MWIR|LOCAL|GLOB|UNIV / PERSPECTIVE angle / ATOL（弧容差）
Q FIND gid IN view / Q VSCAN SIGNIF IN view / Q VSIDE [ROT] OF 3dpt / Q VLIMITS / Q VIEWDIR
-- Id List（3.11.1）：
ADD ALL id FOR id / REM ALL id WITH (criteria) FOR id / DESADD|DESREMOVE id
LIMITS @ TO @ / LIMITS ID @ ID @ / DELETE ENTRY|ADD|REM number
DELETE NULL IDLI                  $* Anywhere 级清空
-- UPDATE 族（3.11.2）：
UPDATE DESIGN [IGNORE] [SHOW CHANGES|NOCHECK] NOWAIT / UPDATE REFRESH / UPDATE ANNO
UPDATE BSHEETS / UPDATE ALL [IGNORE][OVERWRITE] / UPDATE PICTURE
-- LAYER（11.1）：PURP DIMS 控制可挂元素类型；DSLAYE（设计符号层，每 VIEW 仅一个）；
--   UCOD FINCH DIST 精度码；★ AUTOBLANKING ON/OFF + BLNK/BMAR（作用于 LDIM/ADIM/RDIM/PDIM/GLAB/SLAB/VNOT/NOTE）
-- 尺寸标注（12.11，PAGE 217-224）：
NEW LDIM / FR BEFORE ID @ TO AFTER ID @        $* DPBA 前后建点
DIM OFFS（DPOS→DOFF 换算）/ DIM ABS（DOFF→DPOS）/ SORT DIM
NEW RDIM / ON ID @ / AKEY word（默认 DIAM）/ DIM @ / MODIFY @
PDIM：PCEN IDP@|IDPL@|IDPD@|POS@ / PCIRC ...（自动建 RPPT/RPOI）
ADIM：FROM DIR PA|PL|PH|PT|PPoint|IDP|N|S|D|E|W|X|Y|HH|HT / SENSE REV|STAN / DMTX 'text'
GAP @ / GAP AT @ [L value] / GAP DELETE @|ALL / GAP TIDY / SETDEF GAP value
LCHA PARA|CHAI（平行/链式切换命令）/ DMSP value|@ / TRUN BY|TO value / DTER ARR|OBL|DOT|OFF
TSIZ 4 / OSHT / PLCL / DLFG PROJ|DIM|ALL / Q AKEYLIST / Q DDNM X Y / Q EXTENT DMTX|PLTX
DELETE NULL ANNO
-- GRIDLN 标注特例：ppoint 0=原点、1/2=与 VIEW 边界交点、3=中点（NPPT -1 默认 P3）
-- 标签排版 SPREAD（13.6）：
SPREAD LOCAL SELECT [INSIDE pos] / OFFSET|XOFFSET|YOFFSET|RADIUS distance
SPREAD REMOTE SELECT|REPOSITION|...MARGIN d|OMIT (top/bottom/left/right)|GAP d|NOROT
-- Autotag（SP3 新增，13.6.11）：
TAG selection_option
CRIT ALL BRAN WI (HBOR LE 80 OR TBOR LE 80)
TAGG MESS ON [/file] / UPDATE TAGG [IGNORE|OVERWRITE]
-- 剖切面：NEW PPLA/FPLA/SPLA / NEW WPOS / NEW VSEC（VIEW Section 挂 Layer）
```

### 2.3 Isodraft（ISORM）

```pml
-- DETAIL 全语法（2.3.32，PAGE 57-60）：
DETAIL SHEETN 2 /PIPE-2                    $* 重出第 2 页
DETAIL SHEETN SING /PIPE2                  $* 并单页
DETAIL PSPOOL2 OF PSLIST1 OF PIPE /013-0001-A150-100
DETAIL ... AS EQUIPMENT                    $* 设备管件 trim 图
MARK DETAIL ON/IGNORE（联动 DETA/REV）
-- 选项族新增词：REPEATABILITY / UNDERLAYPLOTNAME / RESERVE / FALLSKEWS / OVERALLSKEWS / TUBESPLITS / TRUNCATE
OPTions DEFault                            $* 复位全部选项；Q OPTions 列出全部当前设置
```

### 2.4 Paragon（CSRM）

```pml
-- SPECONMODE 制表语法全链（12 章，批量建规格的官方正道）：
SPECONMODE
NEW SPECification specname
TEXT '...'                                 $* ≤50 字符
HEADING                                    $* 换行后定义表头（最多 20 列，建后不可改列数）
  TYpe NAme PBOR0 STYP ANGL SHOP CATREF DETAIL MATXT CMPREF BLTREF    $* 管道示例表头
DEFAULTS                                   $* 默认行：'-' 无默认 / '=' 默认取列表第一个
  * + - =                                  $* 特殊字符：*=当前 SPEC 名
EXTRA :uda_name value                      $* UDA 列
COMMENT 'text'
COPY specname REName name1 name2
OUTput specname... / OUTput NEW|OLD gtype... specname... / SPEC ON（宏重载）
EXIT
-- Selector 问题清单（13 章）：PBore n / PConn n / SType / ANgle（可区间 45.0,90.0）/ RADius /
--   TEMperature / PRessure / RATing / SHOP（TRUE|SHOP vs FALSE|SITE）
-- ★ PBORE0/PCONN0 特例：翻转法兰 P1/P2 依序试探
-- 自定义 4 字母问题 + SELECT NEW REDU ... WITH COL1 RED WITH COL2 BLUE
-- STYP 可为带引号任意长字符串（禁 _ " ! $ | '）；答案不得用单位词（FT 会被吃掉）
```

### 2.5 Hull（HullDab 等概念性结论）

- 船体库双类型：**DESI**（Initial/Structural/Detail Design）+ **MANU**（制造）；二进制 blob + 显式数据双存储，Apply 时同步。
- **隐式 Claim**：下层元素不可单独 claim（需显式 unclaim 才可）——解释了 HPLATE/HPANEL 写权限的特殊性。
- 仅 UDA/文档链接/Associations 可用通用命令修改船体元素；DEXTR 关键词仍支持但不再扩展。

---

## 3. 两边都有的写法差异（登记，互补而非冲突）

| 写法 | 卷本（PML 源码实证） | 手册（官方语法） | 结论 |
|---|---|---|---|
| 链式标注 | `LCHAIN TRUE/FALSE`（属性） | `LCHA PARA\|CHAI`（命令） | LCHAIN 是属性、LCHA 是设它的命令；两种写法并存 |
| 文本角 | `DTANG PARA` | `DTANG HORIZ\|VERT\|EXTERN\|PARA` / `DTANGLE STAN` | 同一命令不同缩写深度 |
| 半径样式 | `DSTYLE DIMLINE\|LEAD` + `DTFLAG MID\|CIRC` | `DSTY DIMLINE\|LEADERLINE\|EXTERNAL` + `DTFL CENTRE\|MIDPOINT\|CIRCUMFERENCE` | DSTYLE/DTFLAG=全名，DSTY/DTFL=缩写 |
| AUTOSCALE | `AUTO` | `AUTOSCALE`（AUTO 可缩写，手册建议全拼防歧义） | 一致 |
| SPEC 层级 | SPWE 层不存在，SPEC 直挂 SPWLD | 手册同样只画 SPWLD→SPEC→SELEC/SPCOM | **手册佐证卷四勘误** |
| DETAIL 系统 iso | `detail all as /$!sysName` | `DETAIL CE AS 'System Name'` | /name 与 'name' 文本形式均可 |

---

## 4. 遗留项

1. **XLS 资产未提取**（25 份）：All_logical_names.xls、Attributes_func.xls、Data_Extraction_to_Attributes.xls、DatExt_* 30 份——二进制 Excel，是属性/DEX 关键词的又一手册级来源，后续可用 xlsx 工具入库。
2. **乱码目录** `E:\aveva寮…`（早期 .ps1 编码问题产物）已定位——**待用户确认后手动删除**（不自动删）。
3. CHM 反编译方法已打通，后续任何 CHM 资产可按 `_chm_to_text.py` 流程入库。

## 5. 使用方式

- 查手册语法：`findstr /n /i "命令词" E:\aveva开发文档\PML语料\pdf_text\<手册名>.txt` → 按 `===== PAGE n ====` 定位原文。
- 防猜协议更新：字典 → **语料库 grep（源码）** → **手册 grep（140 本全文）** → TODO-UNVERIFIED。手册与源码冲突时仍以源码实证优先（手册描述的缺省值有时滞后于补丁）。
