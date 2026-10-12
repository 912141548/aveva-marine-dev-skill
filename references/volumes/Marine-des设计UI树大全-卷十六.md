# Marine des 设计UI树大全·卷十六（覆盖分析+四块增量·源码实证）

> 来源：`E:\AVEVA\Marine\OH12.1.SP4\PDMSUI\des\` 28 子目录 6228 文件：分类穷举 + 3 遍全树正则扫描（NEW/handle/动词）+ 与十五卷差集对照 + Top 20 命令密度宏精读。
> 定位：设计模块 UI 宏树（用户在 Design 里点按钮背后下发的命令）。PML1 前缀：f*=Form/i*=Init/m*=Method/x*=eXecute。

## 1. 结构与构成判定

**6228 文件 = 3921 文本宏 + 2307 二进制（全部为 .plt 绘图标准，一行登记）。**

| 子目录 | 文件数 | 性质 |
|---|---|---|
| mds | 2008（4 宏 + 2004 .plt） | **Marine 特有**（MDS 出图标准） |
| hvacadv | 754 | **Marine 特有**（HVAC Designer） |
| supp | 482 | **Marine 特有**（支吊架建模） |
| gen 553 / access 343 / equi 243 / pipe 239 / stlwrk 207 / query 120 / panel 122 / clib 119 / router 153 / dtmp 89 / layout 63 / geom 54 / civil 48 / clasher 36 / graphics 33 / plot 303 | ~2900 | PDMS 通用（与 E3D/PDMS 12 同源） |
| pens | 123 | **Marine 特有**（穿舱件） |
| cabl | 68 | **Marine 特有**（电缆托架） |
| addins 27 / dflts 13 / admin/core/data/func/PSI ~28 | ~68 | 配置 |

**构成比例**：纯 UI 样板 ≈15%（604）、UI+命令混合 ≈6%、**纯命令承载 ≈25%（997）**、逻辑胶水 ≈54%（1889）。命令高度集中：454 文件含全部 5614 条 NEW 行；684 文件含全部 1978 处 handle。命令承载率最高：access 68%、equi 45%、hvacadv 38%。

Marine 特有判别依据 = `des\addins\` 27 个 Add-in 定义（MDS=Multi Discipline Supports、supp=Hangers & Supports、hvacadv=HVAC Designer、cabl=Cable Trays、avevamarine、amutil、mms、roomdesign、holemanagement、VNET、asl/aslswitch）。

## 2. 新元素类型（9 族约 60 种，十五卷均未见）

| 族 | 类型 | 说明 |
|---|---|---|
| **接头族** | SJOI/PJOI/PCOJ/SCOJ/SUBJ/SELJ/PALJ + JLDAT/JLDATUM/PLDAT/PLDATU/DATU | PDMS 12 结构接头 + 接头数据（supp\mtemnew:374-659 实用） |
| **新式基元族** | NBOX/NCYL/NCYLI/NCON/NDIS/NPYRA/NLCY/NSEX/NCTO + NSBO/NSCY/NSLC/NSNO | data\utmpls.upgrade 模板中成对出现（负几何 NS*） |
| **回转/拉伸体** | CTOR(362)/RTOR(242)/CTORU/RTORU/NXTR/NXTRU/NRTO/SOLI/SLCY(109) | 环形/矩形回转体——access 平台柱脚主力（mpostfi:59-95） |
| **型钢细化族** | SCTN/STIF/FRMW/STWALL/PAVE/SBFR/SBFI/SELE/SEVE/SLOO/SDTE/STSE/SDEN/TDEN/SNOD(E)/SNOU/SVER/SCLA/SPLR | 支吊架/型钢细节 |
| **板排族** | PANE/PANEL/PLOO/PCLA/PCOM/PNODE/PNOD | |
| **支吊架族** | HANG/HELE/FLEX/REST/ATTA/FIXING | supp 建模核心 |
| **穿舱件族** | CMPF/CMFI/PFIT/BPFITT/BPFEAT/STCA | `NEW FIXING GTYP PENH`（pens\mfitispec-dp:85）；升级链 PFIT/FITT gtype PENH→CMPF/CMFI（data\upene.upgrade） |
| **多面体族** | POHE(21)/POGO(101)/POINT(524) | access 楼梯宏以 POINT 列表构面（mstairpp:153-195） |
| **管路规格元件** | FLAN(60)/GASK(66)/VALV(24)/FTUB(18) | 配 `CHOOSE DEFAULT|TEXT|ALL` 句式 |

## 3. 新命令句式（十五卷未见）

```pml
NEW SUBS                          $* ★1096 次——PML 事件订阅对象(UI 机制核心)
CONNECT HH TO $!ATTAREF           $* ★吊架头连接(supp\mcrhangstd:521)
CONNECT HT TO $!FITTREF           $* ★吊架尾连接(:525)
NEW FLAN CHOOSE DEFAULT           $* ★规格选件三式：DEFAULT|TEXT|ALL(pipe\mfgvgfc:57-232)
NEW FLAN CHOOSE TEXT / CHOOSE ALL
ROTATE ABOUT PPLINE NA AND PPLINE $!FPLIN IS $!SFIDIR WRT WORLD   $* 双 PPLINE 轴旋转(supp\mcrhangstd:953、xffread:435)
NEW SUBS COPY PREV SUBS ORI Y IS S AND Z IS U BY W460    $* ★单行复合创建(access\mladddse:93)
NEW SUBS POLAR N22.5W DIST(...) / MOVE E DIST ...        $* 极坐标复合(mceigi:53-54)
NEW CYL COPY PREV CYL BY U$!CALC4                        $* 阵列复制(mladddse:119)
NEW BOX ... CONN P5 TO P2 OF PREV RTORU                  $* 创建行内连接(mladddse:154)
HANDLE (41,66) (2,113)            $* 多重错误码连写(全树惯用)
```

## 4. Top 宏命令序列（四块增量的骨架）

### 4.1 支吊架建模（supp，95 命令承载文件）

**标准吊架生成 mcrhangstd**（2507 行，Marine 首位）：14 处 `handle (61,528)` 拾取 → `NEW FITT`(:307) → `NEW SPLO`(:318) → `NEW ATTA`(:354) → `NEW STRU $!RESTNAM/STRU`(:419) → `NEW FRMW`(:424) → `NEW SBFR`(:462) → `NEW HANG`(:516) → **`CONNECT HH TO`(:521) / `CONNECT HT TO`(:525)** → `NEW SCTN` + 双 PPLINE 旋转(:944-953) → `NEW PNOD`/`NEW PJOI`(:966-969)；错误码 (42,94) "P15 doesn't exist"、(62,327)、(61,566)。

**模板修改 mtemnew**（701 行）：`NEW SCTN` → `SPREF $!TSPREF` → `NEW SNOD/SJOI/FITT` → `DESPAR 0 0 0 0` → `NEW SPLO`。
**自由杆件生成 msupcfg**（2042 行）：反向清理 `DELETE PNOD/SNOD/SJOI/SCTN/FITT` → `SPREF` → `NEW SCTN`×2。
**型材端头读取 xhbhele/xffread**（856 行）：`NEW HELE`（handle (61,164) Bad selectors）→ `SPREF /$!SPROF[..]` → 双 PPLINE 旋转 → `DESPAR NUM 2 $!FITANG` → `handle (2,9)(47,15) Too many values and bad data`。

### 4.2 ASL 参数化宏族（access，233 命令承载文件，全树密度最高）

楼梯 5 族（mstairpp/t/tl/b/bl：`NEW POHE OBST 0 LEV 5 7` + 20 组 `NEW POGO`+`NEW POINT AT D150 S20 W(...)`）、直梯 msteplad（`NEW PYRA OBST 0 XBOTT 10 YBOTT 75` + `COPY PREV BY W 460`）、梯平台 mladdfel、柱脚 6 变体 mpostf*（CTOR/RTOR 交替）、平台/栏杆/踢脚板 12 文件 mpltwo*/mprail*、走道 mwwrros（12 组拾取 + `NEW BOX OBST 2 LEV 2 7`）。

### 4.3 穿舱件体系（pens + utmpls.upgrade）

`data\utmpls.upgrade`（446 行）：`NEW STCA /PENH/CMPF/DTSE` → `NEW DTSE` → `NEW DATA DKEY DIAM PPRO...` → `NEW NSCY...PAXI Z` 成套负几何模板；`TRACE OFF` 收尾。

### 4.4 Design 12 新类型（并入卷一增补）

接头族 + 新式基元 + 回转体（见 §2）；通用变换 gen\icopyrot/icopyxyz/imirror（:MDS UDA 引用 + `handle (2,109)`×8）；组操作 gen\igrou：`NEW GPWL`（handle (41,54)(2,20) CANT CHANGE RO DB）→ `NEW GROU`。

## 5. 管路规格选件句式（并入卷四增补）

pipe\mfgvgfc/mfgvgf/mfgvg/mgvgf/mfgf/mfg 六宏：`BRAN`（handle (41,222)(2,111)）→ 按 GTYP 分支 → `NEW FLAN|GASK|VALV CHOOSE DEFAULT|TEXT|ALL`（handle (7,3) 规格无此件）。des 树 (7,3) 达 202 次——规格选件失败是该 UI 的头号业务错误。

## 6. des 特有错误码（全树 1978 处/94 种；Marine 目录独有 25 种）

高频：**(61,528)×446**（拾取失败）、**(2,113)×203**（"Can't get to PJOI"）、**(7,3)×202**（规格选件失败）、(61,123)×137、(2,441)×111（110 在 supp/hvac）、(2,201)×94、(41,66)×80 "No next comp"、(47,15)×67 "Too many values and bad data"、(41,222)×66、(2,109)×54 "no /MDS spec"。
**Marine 目录独有**：(62,327)、(7,35)、(2,427)、(2,433)、(16,206)、(44,7)、(61,620)、(73,211)、(41,224)、(2,29)、(61,40)、(61,163)、(61,303)、(2,106) 等（集中支吊架 D/62 域与 HVAC，约 100 处）。
语义补证：(41,54)(2,20)="CANT CHANGE RO DB"（igrou:37）、(61,164)="Bad selectors"（xhbhele:197）、(42,94)="P15 doesn't exist"（mcrhangstd:1468）。

## 7. 编目结论

1. **值得精读的约 1200 个命令承载宏已按四块抽取骨架**（支吊架建模/ASL 参数化/穿舱件/新类型），其余 2700 UI 样板与胶水 + 2307 二进制资源无需成卷。
2. PDMS 通用部分（gen/equi/pipe/panel/stlwrk/civil/layout/query/clib/geom/graphics/dtmp/clasher/router）与 E3D/PDMS 12 同源，其命令模式已被卷一~卷十五覆盖，不再重复。
3. **des 树按本卷增补后即可宣告覆盖完毕**——PDMSUI 树（des 6228 + DRA 1456 + CAT 294 + ISO 331 + clib 393 定性 + 其余小目录）全部处理完毕。
4. clib 根目录（393 文件）同轮定性：经典 PDMS 通用 UI 库（ffilemotif 文件对话框/fconfirm/fcolsel/flist 等），即卷十一/十五已登记的 `CALLIB XFILEMOTIF/FCONFIRM` 宿主宏，无新增开发知识。
