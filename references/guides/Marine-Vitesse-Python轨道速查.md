# Marine Vitesse Python 轨道速查(实证)

> 来源:勘察 `E:\AVEVA\Marine\OH12.1.SP4\Vitesse\`(Lib 105 py / Basic_Design 11 / Examples 82 / Trigger 9 / Context_Menu 16 / Model 6)+ 机制文件全文精读(2026-09-25 第 7 轮)。
> 定位:**Tribon KCS 血统的 Python 定制轨**,面向船体基本设计(Basic_Design)、出图(Drafting)、船体(Hull)——与 PML/.NET 平行,由 `evars.bat` 挂载:`pythonpath=%pdmsexe%Vitesse;%pdmsexe%Vitesse\Basic_Design;%pdmsexe%Vitesse\Lib;%pdmsexe%python`。

## 1. 运行时硬约束

- **Python 2.6**(`python26.dll` + `python\` 是 2.6 标准库:`ConfigParser.py`/`BaseHTTPServer.py` 等实证;源码用 `except Exception, e` 旧语法)——**新脚本必须兼容 Python 2.6,不能用 Python 3 语法**。
- API 分两层:**`kcs_*` 模块级函数**(C 扩展,无 .py 源):`kcs_util / kcs_ui / kcs_gui / kcs_draft / kcs_dex / kcs_model(?)`;**`Kcs*.py` 数据类**(Lib\ 下 90 个,与 marAPI 的 `Mar*` 类一一对应:Point2D/3D、Contour2D、Transformation3D、Model、ElementHandle、HighlightSet、PanelSchema、Weld…、MarDex↔kcs_dex)。
- 错误约定:`kcs_ui.error` 是**错误码字符串**(不是异常);常量 `kcs_util.ok()/success()/failure()/trigger_ok()`。

## 2. 四类扩展机制(实文范式)

### 2.1 Trigger(事件钩子)`Vitesse\Trigger\trig_*.py`

命名 `trig_<模块>_<事件>.py`(trig_draft_init / trig_draft_popup_menu / trig_hull_endcut_dim / trig_dm_activate_model_filter / trig_tm_prediction…);**约定入口函数**:

```python
import kcs_util
def pre(*args):    # 事件前钩子
   return kcs_util.trigger_ok()
def post(*args):   # 事件后钩子
   return kcs_util.trigger_ok()
```

`trig_draft_popup_menu.py` 展示**右键菜单上下文注入**官方范式:把 `kcs_draft.ContextPoint / ContextElement / ContextModel / ContextSubpictures` 设为模块级全局变量(geometry_identify/element_parent_get/model_properties_get 取得),再把 `Context_Menu` 目录追加进 Python 搜索路径(`KcsPythonUtil.PythonUtil().AppendPythonPath(...)`)——菜单脚本即可读到"右键点在哪、点到什么"。
【TODO-UNVERIFIED】触发器注册表位置(配置文件或环境变量)本机未定位到;已知由系统按 trig_ 文件名约定加载。

### 2.2 Context_Menu(右键菜单)`Vitesse\Context_Menu\ctx_menu*.py`

```python
def run(*args):          # 菜单项入口约定
    if hasattr(kcs_draft, 'ContextElement') and kcs_draft.ContextElement != None:
        dlg = CtxDeleteDlg.CtxDeleteDlg(NULL)   # GUI 用 wxPython(wxPySimpleApp)
```

对话框类 Ctx*Dlg.py 同目录;**Python 侧 GUI = wxPython**(与 .NET 侧 WinForms 平行)。

### 2.3 菜单注入(仅 Basic Design)`Vitesse\Basic_Design\*.py`

`basic_design_menu.py` 的 `add(*args)` 入口被系统调用(参数=菜单位置),然后:

```python
main_menu = kcs_gui.menu_get(None, 0)
my_menu  = kcs_gui.menu_add(main_menu, num, 'Quick Panel')
sub      = kcs_gui.menu_add(my_menu, 0, 'Longitudinal')
kcs_gui.menu_item_usr_add(sub, 0, '&Deck', 'KcsMenuTBD01Deck')   # 菜单项 → 同名脚本
```

KcsMenuTBD01Deck…10KBHD 十个脚本 = 船体基本设计快捷建模(甲板/纵舱壁/舷侧纵桁/纵骨…),错误处理惯例:每步 try/except + `print kcs_gui.error`。

### 2.4 Hook(配置钩子)`Vitesse\Lib\_TBhook_*.py`

九个钩子:`_TBhook_AutoPanelName / ConfigNote / CustBracket / CustHole / CustNotch / CustPartName / Formula / PPanScheme`;**固定接口方法,只能改内容不能改签名**(TBhook_ConfigNote.txt 原话 "Interface methods - must not be changed regarding input parameters & returns")。例:`_TBhook_ConfigNote` 提供 `getNoteName/getNoteChar/getNoteFilter/setNoteData`,自定义船体标注(板厚/型材规格/材质符号)。
官方配置说明:`Documentation\TBhook_ConfigNote.txt`、`TBhook_CustPartName_py.txt`、`TBhook_Formula_py.txt`(Documentation 目录)。

## 3. kcs_* 函数 API 实证(来自示例与钩子)

| 模块 | 实证函数 |
|---|---|
| `kcs_ui` | `point2D_req / point3D_req / message_confirm / message_noconfirm / string_req / real_req / int_req / string_select / choice_select` |
| `kcs_gui` | `menu_get / menu_add / menu_item_usr_add`(错误查 `kcs_gui.error`) |
| `kcs_draft` | 图纸:`dwg_new/open/save/save_as/close/delete/exist/dwg_type_list_get` + `kcsOPENMODE_READONLY/READWRITE`;内容:`note_new / contour_new / cross_new / cloud_new / rectangle_new / line_new / symbol_new / text_new`;识别:`view_identify / subview_identify / component_identify / text_identify / symbol_identify / geometry_identify`;编辑:`element_transform / element_highlight / element_delete / reference_move / highlight_off`;属性:`text_height_set / text_slant_set / text_aspect_set / text_properties_get / symbol_properties_get / model_properties_get`;遍历:`element_child_first_get / element_sibling_next_get / element_parent_get`;缩放:`zoom_extent_get / dwg_zoom`;重绘:`dwg_repaint` |
| `kcs_hullpan` | 面板:`pan_activate / pan_store / pan_skip / pan_delete / pan_list_active / pan_recreate / pan_move / pan_copy / pan_split / pan_topology('defining'\|'dependent primary'\|'dependent all') / pan_remove_seam / pan_group_delete / pan_group_divide / pan_sti_split_by_model / pan_sti_split_by_plane` |
| `kcs_chm` | 曲壳:`run_XML(xml路径, log路径) → ModelList` / `output_XML(ModelList, 路径)` / `stiffener_split / stiffener_combine / stiffener_to_profdb / store / skip / delete` |
| `kcs_model` | `model_hull_contact(model)` 船体接触 |
| `kcs_weld` | `weld_calculation / weld_properties_get / weld_properties_set / weld_delete` |
| `kcs_assembly` | `assembly_exist` |
| `kcs_dex` | `extract(est) → next_result() → get_int()/get_real()/get_string()/get_indexedreal(i)`;类型码:1=INT, 2=REAL, 3=STRING, >10=索引实数列表 |
| `kcs_util` | `ok() / success() / failure() / trigger_ok() / TB_environment_get('SB_SYSTEM')` |
| `kcs_gui` | `menu_get / menu_add / menu_item_usr_add` |

数据类构造即关键字参数:`Text(text=txt, v=0.5)`、`Symbol(font=8, number=symbno, height=10, conn=1, v=0.5, mirr=2)`、`.getRecord()` 取记录。
示例库:`Vitesse\Examples\{Drafting(44), Hull(15), Model, Util(含 kcs_ex_ui1-7 全套 UI), Misc_Tools, Weld}` 共 82 个,`kcs_ex_*` 命名,学 API 先看这里。

## 4. 与另外两轨的关系

- **PML → Python**:marAPI 的 `MarPythonEngine.RunPythonScript(路径)` / `MarPythonObjectPML`(CreatePythonObject/InvokeMethod/GetProperty…,见《AVEVA-Marine-marAPI调用姿势表.md》§3.11)——桥存在但官方 PML 未使用(grep PMLLIB 仅注释提及),属备用能力。
- **Python → marAPI 之外的共享对象**:Kcs* 类与 Mar* 类同构(marAPI 反射里 `Aveva.Marine.Vitesse.MarContour2D/MarPoint2D` 就是 Python 侧类的镜像)。
- **文档**:`Documentation\Python.chm`(450KB)、`Documentation\Vitesse.chm`(2.2MB)、`Documentation\vitesse_access.xls`(API 访问面清单)。
- `.pyc` 缓存(trig_draft_init 等)证明运行时实际编译执行;部署新脚本放 `Vitesse\Lib` 或按机制放 Trigger/Context_Menu,注意 Python 2.6 语法与 `pythonpath` 顺序。

## 5. 使用守则

1. 船体基本设计/出图脚本化任务(批量建模、标注、出图后处理)优先考虑本轨——Kcs/kcs_* 是 Tribon 三十年沉淀的领域 API。
2. 与 PML 轨的选择:界面与数据库交互用 PML;船体专业算法/成批出图脚本用 Vitesse;两者经 marAPI 的 Python 桥互通(备用)。
3. 写任何脚本前先 `Examples\` 找同类 `kcs_ex_*.py` 照抄调用姿势(防猜)。
4. 旧语法陷阱:`print` 语句、`except X, e`、`hasattr` 惯用、整除 `divmod`——按 Python 2.6 写,勿用 Python 3。
