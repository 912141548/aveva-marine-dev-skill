# Marine PDMSUI PML1 树与宏机制速查(实证)

> 来源:逐目录勘察 `E:\AVEVA\Marine\OH12.1.SP4\PDMSUI`(9704 文件)+ 启动宏/addin 文件全文精读(2026-09-25 第 6 轮)。
> 定位:PDMSUI 是 PML1 时代界面宏树,新定制**原则上不碰它**——但看懂它才能:定制启动行为、看懂官方界面实现、排查加载问题。

---

## 1. 树结构(20 个顶层目录)

```
PDMSUI\
  adm\            → Admin 模块界面(内含 admin\)
  cat\            → Paragon 目录库界面(含 addins\dflts\applications)
  clib\           → 公共宏库:dflts/files/geocal/lists/plot/query/rep/setup 七子目录
                    (FILES\ 下放 INIT 等公共宏——CALLIB 的目标)
  data\ des\ diagrams\ DRA\ hdes\ icons\ intf\ iso\ lex\ mdra\ mon\ opsys\
  plots\ reports\ smm\ spl\ tags\
  des\            → Design 界面(最大):access/addins/admin/cabl/civil/clasher/clib/core/
                    data/dflts/dtmp/equi/func/gen/geom/graphics/hvacadv/layout/mds/panel/
                    pens/pipe/plot/PSI/query/router/stlwrk/supp
  DRA\            → 出图界面,Marine 专属库:adpcore adpgdp adpsched adptag(组立出图)
                    + libmaba libmdrl libmgen libmiso libmlab libmrep libmshe libmsty
                    libmsym libmtag(Marine 出图库:ABA/DRL/GEN/ISO/LAB/REP/SHE/STY/SYM/TAG)
```

**文件命名约定**(第 30 轮抽样考证,des\clib、des\civil、DRA\adpcore 等):单字母前缀 = `f*` 表单宏 / `i*` init 初始化 / `m*` 菜单与应用宏 / `u*` 实用工具 / **`r*` 子例程库**(Macro Generic Type: "Local Functions, Subroutines",供 CALLIB 式调用,如 clib\ratpos"按位置找元素"、civil\rwallline"型材共线检查"——**PML1 的函数库等价物**) / **`x*` 执行型入口宏**(Generic Type: "Execution",被菜单/应用切换调用后即跑,如 cabl\xcablapp"检查规格并弹表单") / **`p*` 主要是 addin 定义文件名首字母(panel/penetrations/pipe/PSI)而非宏前缀**(plot\pacfa1 等为 plot 配置);每应用目录常有 `init / isystem / dbar / version` 四件。宏头 `Macro Generic Type:` 字段可机械区分用途(Execution / Results / Local Functions, Subroutines)。

## 2. 启动链(des\admin\ 四件套,全文精读)

| 宏 | 职责 | 关键内容 |
|---|---|---|
| `start` | 模块启动入口 | 读 `$1` 设 `!!modLoadMethod`;`$m "%PDMSUI%/CLIB/FILES/FLOAD"`(载入 F&M) |
| `binload` | 单位精度 | `var !UNIT UNIT / MM DIST / PREC VAR 6DP / FINCH DIST / PREC VAR 1/1024`(英制分数精度 1/1024 英寸!)|
| `macload` | **应用装载主宏** | `!!comDefineGlobal(object COMFORMATS())` → `FMINFO HELP callback` → `!!loadColours(FILE('%PDMSDFLTS%/PDMS-COLOURS'))` → `CALLIB INIT`(公共库)/`CALLIBD INIT`(Design)/`CALLIBL/CALLGPH/CALLGEOM/CALLIBSU INIT` → **`$M "%PDMSDFLTS%/DES-INIT-MAC"`(用户自定义 INIT 挂载点,包 handle ANY)** → DDL 版本检查 → `CALLIB TEAMCHK` 权限检查 |
| `vars` | 全局路径变量 | `$G 名字 =/路径/` + `$U 名字`(定义+导出全局变量,如 `$G PIPE =/%PDMSUI%/DES/PIPE/`)——宏里以 `$:PIPE$:...` 或前缀引用 |

**定制挂载点**:`%PDMSDFLTS%\DES-INIT-MAC`(用户 INIT 宏,macload 自动调用,失败被吞)——这是**不改官方文件往 Design 启动流程插代码的官方入口**。加菜单/工具条则走 `des\ADDINS\`(见 §4)。

## 3. PML1 宏语法要素(官方宏中实证)

| 写法 | 含义 | 出处 |
|---|---|---|
| `$(H ... $)` / `$(D ... $)` | 文件头/说明块注释 | start/binload |
| `$* 行内注释` | 注释到行尾 | 全部 |
| `$:debug$:` | 调试条件插入点 | binload/macload |
| `$1..$9` / `$<表达式$>` | 位置参数 / 带引号参数展开 | start;`CALLIB TEAMCHK $<MASTER DESADMIN$>` |
| `$!var` / `$!!var` / `$:var$:` | 局部/全局/变量展开 | macload |
| `label /名` + `return` + `$.` | 标签/返回/文件尾 | binload |
| `var !x TYPE` / `PREC VAR 6DP` | 变量与精度 | binload |
| `$G 名=值` + `$U 名` | 定义全局变量并向上层导出 | vars |
| `$m "路径"` | 调宏(路径带空格用引号) | start |

## 4. PML ADDIN 文件( des\ADDINS\ ,27 个,实文)

```
# des\ADDINS\avevamarine —— Marine 注入 Design 的方式(修饰型 addin)
name:        AvevaMarine
title:       Aveva Marine
ShowOnMenu:  FALSE        ← 不上 Applications 菜单 = 纯修饰
object:      APPDESAVEVAMARINE   ← 对象在 PMLLIB(PML2)
helpAlias:   DRMPCM

# des\ADDINS\gen —— 完整应用型 addin
Name:          GEN
Directory:     GEN
showOnMenu:    TRUE
Title:         General
Object:        appgeneral
Synonym:       CALLG              ← 该应用的宏调用前缀(CALLG <宏名>)
startUp:       $M "%PDMSUI%\DES\GEN\INIT"
helpAlias:     DRMPCM
```

- **`Synonym: CALLxx` 的机制**:`CALLG <宏>` = 调 %PDMSUI%/DES/GEN/\<宏\>;`CALLIB INIT` = 调 clib\FILES\INIT;`CALLAC`(access)等同理——**CALL 前缀即"CALL + 目录同义词"**。
- **`helpAlias:` 是 Guide ch23/TM-1401 未载的新键**:F1 帮助别名(本机统一指 DRMPCM)。
- 菜单/工具条本体由 addin 对象(`app****.pmlobj`,放 PMLLIB)的 `.modifyMenus()/.modifyForm()` 用 APPMENU/APPTBARCNTRL 定义——PDMSUI 侧只有这份"注册表"。

## 5. DRA Marine 库(libm* / adp*)

- `libmgen\`:`dbar / flibatt ilibatt mlibatt / ftexted mtexted itexted / init isystem mversion uedwin` —— f/i/m/u 前缀 + 每库 dbar/init/isystem 标准件(旧 DBAR 体系的存量)。
- `adpcore\`(ADP 组立出图核心):`dbar init initshow isystem` + 每类 dflts 宏(`fadpdflts/iadpdflts/madpdflts/uadpdflts` 四前缀同功能四模块)+ 规则宏(`rgetrule/rnearside/rinterfront/rviewcorn`)。
- 定位:这些是 Marine 出图的存量 PML1 界面层;新开发对应能力在 PMLLIB 的 assembly/ 与 marinedrafting/ 里。

## 6. 使用守则

1. **新定制三选一**:纯 PML 功能 → PMLLIB;菜单/工具条入口 → `des\ADDINS\` 加定义文件 + PMLLIB 加 app 对象;启动钩子 → `%PDMSDFLTS%\DES-INIT-MAC`。**不直接改 PDMSUI 任何文件**(PKG-05)。
2. 读官方界面实现时,从 `q var !!appdesmain` 出发找 addin 对象,再回到 PDMSUI 找它引用的旧宏。
3. 排查"宏没生效":先 `q evar pdmsui` 看搜索路径,再看 `pml.index`/`CALLIB` 是否指向预期目录。
