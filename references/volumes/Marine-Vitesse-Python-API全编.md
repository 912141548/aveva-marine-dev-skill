# Marine Vitesse Python API 全编（穷举级·源码实证）

> 来源：`E:\AVEVA\Marine\OH12.1.SP4\Vitesse\` 全目录 134 个 .py 文件逐个读取（Examples Drafting 42/Misc_Tools 7/Model 6/Util 13/Weld 1、Basic_Design 11、Context_Menu 20、Lib 102、Trigger 8、Model 7）。Hull 系 API（kcs_hull/kcs_hullpan/kcs_chm）已收录于《Marine-Hull船体建模语句大全.md》第三、四节，本编不重复。
> 适用：AVEVA Marine (PDMS 系) 12.1 SP4，Python 2.6。

## 0. 总体事实（先读）

1. **kcs_* 模块不是 .py 文件**——全部是编译进 Marine 主程序（marodes.exe/mardra.exe/marhdes.exe 等）并链接 `python26.dll` 的 C 扩展，无独立签名文件。本编函数签名均从官方示例与 Lib 库的真实调用反演，每条带调用处 文件：行号。
2. 官方 API 文档：`Documentation\Python.chm`、`Vitesse.chm`、`vitesse_access.xls`、`Drafting.chm`、`Data_Extraction.chm`、`marAPI.chm`；TBhook 说明 `Documentation\TBhook_*.txt`。
3. Python 版本：**2.6**（print 语句、`except Exception, e`、wxPython 2.x）。
4. import 统计（穷举）：kcs_util 129、kcs_ui 124、kcs_draft 90、kcs_dex 22、kcs_hull 14、kcs_model 12、kcs_hullpan 11、kcs_chm 11、kcs_assembly 8、kcs_ic 7、kcs_att 6、kcs_struct 4、kcs_pipe 4、kcs_gui 4、kcs_equip 4、kcs_cable 4、kcs_db 2、kcs_weld 1、kcs_tm 1、kcs_spec 1、kcs_placvol 1、kcs_modelstruct 1。
5. `<OH>\auto_clicker.py` 是用户自放工具，与 Vitesse 无关。

---

## 1. kcs_util — 工具/返回码（23 函数）

**返回码函数**（比较用）：
| 函数 | 语义 | 示例 |
|---|---|---|
| `ok()` | 正常确认 | Examples\Util\kcs_ex_ui1.py:95 `if resp == kcs_util.ok():` |
| `cancel()` | 取消 | kcs_ex_util2.py:28 |
| `quit()` / `options()` / `operation_complete()` | EF/OPTIONS/操作完成键 | kcs_ex_ui1.py:99-103 |
| `yes()` / `no()` | answer_req 应答 | kcs_ex_util2.py:43,45 |
| `success()` / `failure()` | 通用布尔状态 | Lib\KcsUtilPos.py:7-8 |
| `u_lock()` / `v_lock()` / `unlock()` | point2D_req 锁定按钮 | Lib\CommonSample.py:379-389 |
| `trigger_ok()` / `trigger_abort()` | 触发器正常/中止 | Trigger\trig_draft_init.py:5 |
| `trigger_override()` | pre 触发器覆盖原函数 | Trigger\kcs_ex_trig01.py:122 |
| `exit_function()` / `exit_program()` | 请求退出 | Lib 内 |
| `drafting()` | 判定当前是否 Drafting 环境 | kcs_ex_util3.py:20 |

**数据函数**：
- `TB_environment_get(name)` / `TB_environment_set(name, value)`：`binDir = kcs_util.TB_environment_get('SB_SYSTEM')`（kcs_ex_trig_ap_parts_list_create.py:17）
- `coord_to_pos(plane, value)` → `(res, posstr)`（1=X/FR, 2=Y/LP, 3=Z）：`frpp = kcs_util.coord_to_pos(1, bigcoord)`（KcsUtilPos.py:17）
- `pos_to_coord(...)`：位置串→坐标（8 处）

---

## 2. kcs_ui — 用户交互（26 函数）

| 函数 | 语法 | 返回 | 示例 |
|---|---|---|---|
| `message_noconfirm(msg)` / `message_confirm(msg)` / `message_debug(msg)` | 字符串 | 无 | kcs_ex_ui1.py:36；17 处 debug |
| `string_req(prompt[, default])` / `req_string(...)` | → `(res, str)` | 元组 | kcs_ex_ui6.py:41；Basic_Design\KcsMenuTBD01Deck.py:35 |
| `real_req(prompt[, default])` | → `(res, real)` | 元组 | kcs_ex_ui6.py:29 |
| `int_req(prompt[, default])` | → `(res, int)` | 元组 | kcs_ex_ui6.py:17 |
| `answer_req(title, question)` / `req_answer(...)` | → yes/no/cancel 码 | 码 | kcs_ex_util2.py:42 |
| `choice_select(title, prompt, actions)` | actions=list → `(res, index)` | 元组 | kcs_ex_util2.py:25 |
| `req_choice(prompt, default)` | → `(res, choice)` | 元组 | KcsMenuTBD01Deck.py:41 |
| `string_select(title, group, prompt, stringlist)` | → `(res, index)` | 元组 | kcs_ex_ui4.py:25 |
| `colour_select(prompt, colour)` | → `(res, Colour)` | 元组 | kcs_ex_ui6.py:77 |
| `point2D_req(prompt, point[, status[, buttons]])` | → `(res, point)` | 元组 | kcs_ex_ui1.py:213,243 |
| `point3D_req(prompt, status, point3d)` | → `(res, point)` | 元组 | kcs_ex_ui6.py:54,68 |
| `req_pick_mod(prompt, x, y)` | → `(res, …, ref)` 拾取模型 | 元组 | KcsMenuTBD01Deck.py:101 |
| `pic_draw_mod(type, name, mode)` | 打开/绘制图 | 码 | KcsMenuTBD01Deck.py:279 |
| `model_info(point)` | 弹出模型信息 | 无 | Context_Menu\ctx_menu2.py:26 |
| `init_highlight(...)` / `terminate_highlight(...)` | 高亮控制 | 无 | 各 2 处 |
| `app_window_minimize()/maximize()/restore()/refresh()` | 主窗口控制 | 无 | kcs_ex_ui7.py:31-35 |

错误属性 `kcs_ui.error`（字符串）。

---

## 3. kcs_draft — Draft 图元/视图/图框（约 180 函数）

### 3.1 图元创建（首个调用位置）

`arc_new`(kcs_ex_draft7.py:132)、`circle_new`(:150)、`cloud_new`(draft40.py:285)、`conic_new`(:179)、`contour_new`(:69)、`cross_new`(:255)、`ellipse_new`(:207)、`line_new`(draft7.py:225)、`point_new`(:239)、`rectangle_new`(draft14.py:34)、`spline_new`(draft7.py:277)、`text_new`(draft11.py:48)、`symbol_new`(draft12.py:33)、`note_new`(draft10.py:63)、`hatch_new`(draft14.py:45)、`hatch_island_new`(draft9.py:68)、`component_new`(draft30.py:364)、`subview_new`(:355)、`view_new`(:347)、`view_symbolic_new`(draft34.py:256)、`ruler_new`(draft40.py:309)、`position_ruler_new`(:332)、`general_restr_symbol_new`(:364)、`pipe_restr_symbol_new`(:380)、`dim_angle_new`(draft8.py:142)、`dim_diameter_new`(:165)、`dim_radius_new`(:192)、`dim_linear_new`(draft29.py:188)、`dim_point_3d`(draft28.py:130)、`dim_shell_new`(Lib\KcsCPanDist.py:179)。

### 3.2 标识/拾取

`view_identify`(draft16.py:32)、`subview_identify`/`component_identify`(draft20.py:28/30)、`model_identify`(draft19.py:43；`model, subview, comp = kcs_draft.model_identify(point, model)` kcs_ex_model03.py:33)、`geometry_identify`/`contour_identify`/`dim_identify`/`note_identify`/`posno_identify`/`text_identify`/`symbol_identify`/`hatch_identify`/`point_identify`(draft21.py:25-41)、`element_identify`(KcsCPanDist.py:134)。

### 3.3 capture 系（draft22.py:33-57）

`view_capture` `subview_capture` `component_capture` `model_capture` `dim_capture` `note_capture` `posno_capture` `hatch_capture` `text_capture` `symbol_capture` `contour_capture` `point_capture` `geometry_capture`。

### 3.4 类型判定（element_is_*，draft30.py:116-141）

`element_is_text/is_contour/is_symbol/is_subpicture/is_view/is_subview/is_component/is_burning_sketch/is_detail_sketch/is_nesting/is_dimension/is_note/is_posno/is_hatch`。

### 3.5 树遍历/操作

`element_child_first_get`(draft30.py:34)、`element_sibling_next_get`(:49)、`element_parent_get`(:381)、`element_extent_get`(:66)、`element_delete`(draft14.py:59)、`element_copy`(draft31.py:113)、`element_highlight`(draft20.py:43)、`element_visibility_get/set`(draft31.py:37/288)、`element_layer_get/set`(draft26.py:272/287)、`element_colour_get/set`(:340/352)、`element_linetype_get/set`(:318/331)、`element_transform`(draft31.py:340)、`element_transformation_get/redefine`(draft34.py:323/draft31.py:347)、`delete_by_area`(draft22.py:302，配 `kcsDEL_INSIDE/kcsDEL_OUTSIDE`)、`highlight_off`/`point_highlight`/`contour_highlight`(draft13.py:78/61/70)。

### 3.6 模态属性

`colour_get/set`(draft2.py:37/45)、`hatch_pattern_set`/`userdef_hatch_pattern_set`/`std_hatch_pattern_set`(draft3.py:53/46/60)、`text_height_set/slant_set/aspect_set`(draft5.py:28/35/42)、text 属性 getter 集（Lib\KcsText.py:61-73：height/rotation/slant/aspect/bold/italic/underline/strikeout/ascii_font）、`symbol_rotation_get/set`(draft6.py:27/33)、`symbol_height_get/set`(:39/45)、`posno_symbol_set`/`posno_height_get/set`(draft4.py:30/35/43)、`default_value_get/set`(draft18.py:28/36)、`linetype_display_settings_get/set`(draft41.py:21/68)。

### 3.7 视图/模型显示

`view_scale`(draft31.py:262)、`view_move`(:272)、`view_restriction_area_get`(:248)、`view_projection_get/set`(draft34.py:292/302)、`view_slicedepth_get`(:310)、`view_slice_planes_get`(:331)、`view_hl_remove`(draft17.py:39)、`zoom_extent_get`/`dwg_zoom`(draft35.py:95/98)、`point_transform`(draft16.py:16,48，3D→2D)、`subpicture_current_get/set`(draft30.py:108/335)、`model_draw`(draft19.py:34)、`model_colour_set`(:47)、`model_layer_set`(draft26.py:307)、`model_properties_get`(:296)、`model_delete`(cPanel.py:475)、`model_object_revision_get/set/save`(draft42.py:50/86/101)。

### 3.8 图页（dwg）生命周期

`dwg_type_list_get`(draft1.py:30)、`dwg_new(name, form, dwgtype)`(:89)、`dwg_open(name, dwgtype, mode, revision)`(:101，mode 用 `kcsOPENMODE_READONLY/READWRITE`)、`dwg_close/save/save_as/exist/delete`(draft1.py:106-141)、`dwg_repaint`(draft10.py:74)、`dwg_name_get`(draft30.py:247)、`dwg_status_set`(kcs_ex_model03.py:117)、`dwg_properties_set/get`(kcs_ex_model04.py:270/kcs_ex_model06.py:202)、`dwg_print`(draft27.py:198，配 `Lib\KcsPrintOptions.PrintOptions`)。

### 3.9 格式交换/图层/子图/版本

`dwg_dxf_export/dwg_dxf_import/dwg_dxf_3d_export`(draft32.py:137/148/113)；`layer_show_all/show/hide`(draft26.py:235/249/257)、`dwg_layers_is_shown/is_hidden/shown_get/hidden_get`(:218-227)；`subpicture_save/insert`(draft37.py:26/37)、`subpicture_name_get/set`(draft30.py:190/374)；`dwg_revision_freeze/unfreeze/new`(draft38.py:20/28/39)；专用：`shd_new/shd_projection_set/shd_zoom_box/shd_autoscale`(kcs_ex_shd01.py:27-46，Shell Difficulty 视图)、`geocontour_function`(KcsContour2D.py:403)、`reference_move`(draft10.py:73)。

常量：`kcsOPENMODE_READONLY/READWRITE`(draft1.py:70/72)、`kcsDEL_INSIDE/OUTSIDE`、`kcsSBD_PICT/kcsSBD_STD`。**`kcs_draft.error` 可读可写**（`kcs_draft.error = 'kcs_HandleInvalid'` CommonSample.py:264）。

---

## 4. kcs_dex — 数据提取（9 函数）

```python
res = kcs_dex.extract(est)          # 执行提取表达式；与 kcs_util.success() 比较
type = kcs_dex.next_result()        # 类型码
v = kcs_dex.get_int()               # type==1
v = kcs_dex.get_real()              # type==2
v = kcs_dex.get_string()            # type==3
v = kcs_dex.get_reavec3d()          # type==4
v = kcs_dex.get_box()               # type==5
v = kcs_dex.get_reavec2d()          # type==6
v = kcs_dex.get_indexedreal(i)      # type>10 列表(元素数=type-10)；type>=25 为 4x4 变换矩阵
```
类型码实证：Lib\KcsUtilDexPan.py:16-79；矩阵读取 `if type >= 25:` 后 `get_indexedreal(0..14)` 读 U/V/W/Origin（KcsUtilPan.py:88）。
调用示例（KcsCPanDist.py:110-116）：
```python
dexString = "HULL.CPANEL('" + PanelName + "').NPPANEL"
kcs_dex.extract(dexString)
type = kcs_dex.next_result()
if type == 1:
    nppanel = kcs_dex.get_int()
```

---

## 5. kcs_gui — 菜单（4 函数）

```python
main_menu = kcs_gui.menu_get(None, 0)                        # basic_design_menu.py:13
my_menu   = kcs_gui.menu_add(main_menu, num, "Quick Panel")  # :22
kcs_gui.menu_item_usr_add(long_menu, 0, "&Deck", "KcsMenuTBD01Deck")  # :37（第4参=脚本名不含.py）
print kcs_gui.error                                          # :15
```

---

## 6. kcs_model 与舾装激活/保存族

- `model_hull_contact(model)` → 模型列表（kcs_ex_model01.py:37）
- `model_interference_check(model, outfittype)` → 模型列表（kcs_ex_model05.py:45；outfittype ∈ 'equipment','struct','pipe','ventilation','cable'）
- `status_values_get(type)`（kcs_ex_model03.py:55）、`model_status_set(model, type, value)`(:115)
- `model_properties_get/set(model[, tdm])`（kcs_ex_model06.py:191 / kcs_ex_model04.py:258）
- 常量：`kcsSTATTYPE_DESIGN / ASSEMBLY / MANUFACTURING / MATERIAL_CONTROL`

| 模块 | 激活/保存/取消 | 示例（kcs_ex_model04.py） |
|---|---|---|
| kcs_pipe | `pipe_activate(name)` / `pipe_save()` / `pipe_cancel()` | :133/:179/:203 |
| kcs_equip | `equip_activate/save/cancel` | :143/:181/:205 |
| kcs_cable | `cable_activate/save/cancel` + `cway_activate/save/cancel` | :150-209 |
| kcs_struct | `struct_activate/save/cancel` | :158/:187/:211 |
| kcs_assembly | `assembly_activate/save/cancel` + `assembly_exist(name)` + `assembly_properties_get` | :169/:191/:164；Weld\kcs_ex_weldcalc1.py:33 |
| kcs_modelstruct | `block_new(name,min,max)/block_delete`、`system_new(name,descr[,code])/system_delete`、`module_new/module_delete` | Vitesse\Model\kcs_ex_modelstruct01.py:62-93 |
| kcs_weld | `weld_calculation(assembly, flag)`、`weld_properties_get/set(assembly, WeldTable)`、`weld_delete` | kcs_ex_weldcalc1.py:36-68 |
| kcs_db | `object_list_get(criteria, dbname, list)`（配 ObjectCriteria） | kcs_ex_draft1.py:48 |
| kcs_tm | `getTMListMin/Average/Max(model, tmList)` | Trigger\trig_tm_prediction.py:44-48 |
| kcs_att | `attribute_first_get(model,1)`、`attribute_is(att, kcs_att_General.kcs_General_ModelUnit())`、`attribute_next_get(1)`、`attribute_create(model,"General","ModelUnit")`、`string_set/integer_get/real_get/string_get`、`model_save(model)` | munDefineModelUnit.py:53-112、trig_hull_nest_structlabel.py:28-92 |
| kcs_ic | `colour_names_get()`、`linetypes_get()`、`layer_desc_get(id)`、`font_name_get`、`intersection_points_get`、`contour_split`、`transf_combine_2d` 等 2D 变换族 | KcsColour.py:18、KcsLayer.py:112 等 17 处 |

---

## 7. 四扩展机制

### 7.1 Trigger（触发器）

**约定**：脚本名 `trig_<应用>_<事件>.py` 放 PYTHONPATH；必须定义 `pre(*args)` 和/或 `post(*args)`。空模板（Trigger\trig_draft_init.py:4-8）：
```python
import kcs_util
def post(*args):
   return kcs_util.trigger_ok()
def pre(*args):
   return kcs_util.trigger_ok()
```
现存：trig_draft_init、trig_draft_popup_menu（右键菜单）、trig_dm_activate/drop_model_filter（pre 返回 `[kcs_util.trigger_ok(), "CURRFILT"]` :22-25）、trig_hull_endcut_dim（1534 行端切标注）、trig_tm_prediction、kcs_ex_trig01、kcs_ex_trig_ap_parts_list_create。
**返回值协议**（kcs_ex_trig01.py:139-148）：`trigger_ok()`；-2 非法；pre 可 `trigger_override()`（跳过原函数）/`trigger_abort()`；带输出参数返回列表 `[result, out1, out2, ...]`（:129-136）。
绑定方式：数据库宏库（etc\d0300023.sbm 等含 `RELOADING_PYTHON` 宏）与模板 SETT 文件——经宏链间接绑定，非注册表。

### 7.2 Context_Menu（右键菜单）

入口 = `trig_draft_popup_menu.py` 的 `pre(*args)`（args=(菜单句柄, 元素句柄|点)）。先挂上下文变量：
```python
kcs_draft.ContextPoint = None; kcs_draft.ContextElement = None
kcs_draft.ContextModel  = None; kcs_draft.ContextSubpictures = []
```
注册菜单项：`kcs_gui.menu_item_usr_add(args[0], index, "&Delete", "ctx_menu1")`（:76）。**菜单项目标脚本必须实现 `run(*args)`**（ctx_menu1.py:25、ctx_menu2.py:19）。路径注入：`KcsPythonUtil.PythonUtil().AppendPythonPath(os.path.dirname(__file__)+'\\..\\Context_Menu')`。
现存菜单脚本：ctx_menu1(删除+wx 对话框)、ctx_menu2(Model Info)、ctx_menu3-8（文本/符号/轮廓/移动/子图/视图属性）、ctx_menu9；对话框支撑 CtxDeleteDlg/CtxTextPropDlg/CtxSymbolPropDlg/CtxContourPropDlg/CtxSubpictPropDlg/CtxViewProjDlg/CtxValidators（wxPyValidator 子类 5 个）。

### 7.3 Basic_Design（应用菜单钩子）

约定：应用初始化时调用脚本顶层 **`add(*args)`**，args[0]=新菜单插入位置号。`basic_design_menu.py:8-68`：`kcs_gui.menu_get(None,0)` → `menu_add` → `menu_item_usr_add` 挂 KcsMenuTBD01Deck~KcsMenuTBD10KBHD 十个功能脚本。
Misc_Tools 变体：初始化触发器内建菜单（muntrig_draft_init.py:25-32 post 中 `munModelUnitMenu.CModelUnitMenu(10,"Model &Unit").CreateMenu()`）。

### 7.4 _TBhook_ 引擎钩子（文件名固定、签名不得更改）

`_TBhook_<HookName>.py` 放 PYTHONPATH 即被引擎自动调用（原话见 _TBhook_AutoPanelName.py:5-6）。现存 8 个：

| 钩子 | 接口函数 |
|---|---|
| _TBhook_AutoPanelName | `InitPanelName():22`、`ExitPanelName():30`、`getPanelName(Block,Valid,Axis,Location,DType,GType,Project,PartList,GPS1..4):39` |
| _TBhook_Formula | `getFormula(ModelType,ModelName,PartType,PartId,...,PI0..9,PR0..9,PS0..9):235` |
| _TBhook_ConfigNote | `getNoteName/getNoteChar/getNoteFilter/getNoteData/setNoteData :69-262` |
| _TBhook_CustBracket | `getBracketName(BracketNo):289`、`setBracketContour:304` |
| _TBhook_CustHole | `getHoleName:39`、`getHoleSegment:45`、`setHoleContour(HoleName,NPar,Par1..8):77` |
| _TBhook_CustNotch | `getNotchName:42`、`getNotchSegment:48`、`setNotchContour:80` |
| _TBhook_CustPartName | `getPartName(Project,Assembly,Block,Module,...,RulePartName):46` |
| _TBhook_PPanScheme | `SplitIntoLines(stmt):15`、`FormatLine(line):34` |

**`_usr` 前缀**：安装内未发现任何 `_usr*.py` 文件；用户脚本只需放 PYTHONPATH 目录并以脚本名被 `menu_item_usr_add` 引用。

---

## 8. Lib 支撑库（102 个 .py）

### 8.1 几何类（全方法）

- **Point3D**（KcsPoint3D.py:20）：`__init__(x=0,y=0,z=0)`、`DistanceToPoint(p)`、`Round(decimals)`、`SetCoordinates`、`SetFromMidpoint(p1,p2)`、`SetFromPoint`、`Transform(tra)`、`Name()`、GetX/SetX/GetY/SetY/GetZ/SetZ；X/Y/Z 经 property（`p.X`）。
- **Point2D**：同构 + `Move(xmove,ymove)`。
- **Vector3D**（KcsVector3D.py:27，默认值 -32000）：`__add__/__sub__/__cmp__/__nonzero__/__getitem__/__setitem__`、`AngleToVector/AngleToVectorWithSign`、`BlankProduct/BoxProduct/DotProduct`、`CompareVector(vec,tol)`、`AbsoluteLargestComponentAxis()`、`Length()`、`ProjectOnLine/OnVector/OnPlane`、`Rotate(angle,rvec)`、`ScalarComponentOnLine`、`SetFromCrossProduct/FromPoints/FromVector/Difference/Sum`、`SetLength/SetToUnitVector/Transform`。
- **Vector2D**：同构子集。
- **Transformation3D**（KcsTransformation3D.py:28）：`Combine/Invert/ReflectX/Y/Z/Rotate(point,axis,angle)/Translate`、`SetByRow/SetByRowFromArray/SetFromPointAndTwoVectors/ThreeVectors/FromTransformation`、`GetByRow`。
- **Transformation2D**：`IdentityTransf/Translate/Rotate(center,angle)/Scale/Reflect(point,vector)/Combine/Invert/GetByRow` + 分解 `GetScale/GetXYShear/GetTranslation/GetRotation/GetReflection/GetType/GetMatrix`。
- **Plane3D**（`__init__(pnt,norm)`、`IntersectLine(line,point)`、`Transform`）、**Line3D/Line2D**（`ScalarComponentOfVector/VectorComponentOfVector/Transform`）、**Rline3D/Rline2D**（`__init__(startp,endp)`）、**Arc2D/Arc3D**（`__init__(p1,p2,amp)`）、**Circle2D/Circle3D**（`HasPoint/IsPointOnCircle/GetTangentPoints/TangentAtPoint`；3D 加 `Normal`）、**Conic2D**、**Ellipse2D**（外接矩形两角）、**Rectangle2D**（`SetCorners(*args)`、`IsEmpty/SetEmpty`、模块常量 `Infinity`）、**Polygon2D/Polygon3D**（`AddPoint/GetNoOfPoints/GetPoint`、2D `__add__` 并集）、**Box**（`__init__(origin,lengthDir,heightDir,widthDir,len,hei,wid)`、`SetAxisParallelBox`）、**Gencylinder**。
- **Contour2D**（KcsContour2D.py:42）：`AddLine/AddArc`、`SetVisible/IsVisible/SetDetectable/IsDetectable/SetColour/GetColour/SetLineType/GetLineType/SetLayer/GetLayer`、`IsPoint/SetPoint/IsClosed/IsInside(extPnt)/Length/Area/Distance(pnt)/IsPointOnContour/GetPointOnContour/Direction/GetCenterPoint`；运算符 `+`(并)/`*`(交)/`-`(差)。
- **BooleanOperations**（KcsContourOperations.py:33）：`CompositeContour/CommonContour/DifferContour`；模块函数 `IsSamePoint/IsPointInPoints`。
- **GeoContour3D**（`AddLine/AddArc/IsPoint/SetPoint`）。

### 8.2 异常/事件类

- **TbBaseException**（KcsTbBaseException.py:22）——属性名**不得更改**：`strFunctionName`、`strModuleName`、`strError`；`__repr__` 返回三行。
- **ButtonState**（`EnableLock/IsLockEnabled/EnableOptions/IsOptionsEnabled/SetCheckedLock/GetCheckedLock`，锁定值 None/'U'/'V'）——用于 `point2D_req` 第 4 参。
- **CursorType**：常量字典 `CursorTypes = {'CrossHair':1,'RubberBand':2,'RubberRectangle':3,'RubberCircle':4,'DragCursor':5}`；`SetCrossHair/SetRubberBand(point)/SetRubberRectangle/SetRubberCircle/SetDragCursor/GetCursorType`。
- **Stat_point2D_req / Stat_point3D_req**：属性 `Helpdef/Helppnt/Locktype/Lockpnt/Lockvec/Initial3D/Initial2D`、`SetDefMode/SetCursorType/SetHelpPoint/GetDefMode`（kcs_ex_ui6.py:60-67、kcs_ex_ui1.py:71-90）。
- **HighlightSet**：`AddGeometry2D(element[,linetype])/AddGeometry3D/AddModel/AddSubpicture/Reset/GetElements`。
- **ElementHandle**：`SetHandle(value)/GetHandle()/__cmp__`——所有 kcs_draft 句柄的承载类。

### 8.3 业务对象类

- **Model**（type/name/partType/partId/subPartType/subPartId/reflCode 全 Set/Get）、**Object/ObjectCriteria**（配 kcs_db.object_list_get）、**ModelObjectRevision**（配 model_object_revision_*）、**ModelDrawAssyCriteria**（`SetAssemblyName/IsRecursive/EnableModelType/GetCriteria`）。
- **SymbolicView**（KcsInterpretationObject.py:23，1109 行）：平面定义 `SetPlaneByX/Y/Z(coord)`、`SetPlaneBy3Points(origin,uaxis,vaxis)`、`SetPlaneByPanel/SetPlaneByCurve/SetPlaneByRSO`；显示开关 `SetLooking/SetDepth(before,behind)/SetLimits/SetViewType/SetShellCurves/SetDrawRSO/GAView/ShellProfiles/ShellSeams/DrawPlaneViews/DrawIntersections/AutomaticSelection/DrawAsPlate/SetPanelsFilter/SetBlocksFilter/SetAssemblies/SetDrawPipes/DrawEquipment/DrawCableways/DrawStructures/DrawVentilation/DrawRoomDesign/SetShThick/SetCrossSectionSymbols`；**CurvedPanelView** 子类（`SetSeams/Plates/Stiffeners/Endcuts/Jigs/Heights/Panels/ShellStiffNames/DirectionMarks/PartNames/HoleCrossMarks/FrameCurves`）——配 `kcs_chm.view_curvedpanel_new`。
- **Weld/WeldedJoint/WeldTable**（全 Set/Get：WeldName/Comment/Length/LegLength/Layers/Position/TestProcedure/Process/Suspension/ConnectionAngle/RotationAngle/InclinationAngle/TorchVector/BevelCode(part)/Thickness(part)/Quality(part)；Weld 另有 `SetPoint/AddArc/AddLine/GetNoSegments`；WeldedJoint `GetNumberWelds/SetWeld/GetWeld/AddWeld`；WeldTable `SetWeldedJoint/GetWeldedJoint/GetNumberWeldedJoints/AddWeldedJoint`）。
- **TMList/TMResult/DiminutionList/GaugedList/PredictList**（trig_tm_prediction 用）。
- **Symbol/Text/Colour/Linetype/Layer/Date/Time/DateTime**（Text 36 方法全 Set/Get；Colour `ColourStrings` 列表 + `SystemColourStrings = kcs_ic.colour_names_get()`）。
- **PrintOptions**（32 方法：PrinterName/Orientation/PrintToFile/NumberOfCopies/EffectivePrintArea/AutoOrient/ScaleToFit/Scale/FileName/CenterOnPage/Point1/2/Paper*/ColourMode）——配 dwg_print。
- **CaptureRegion2D**（`SetRectangle/SetContour/SetInside/SetOutside/SetCut/SetNoCut/SetBoundaryInfinite`）、**RunModeOptions**（`SetConfirmGeneration/SetTraceOn`）、**LineTypeDisplaySettings**（`SetPattern/SetPatternLength/各线型宽度 Set/Get/SetScaleFactor`）、**DimensionSet/ProfileSketch**（`AddLinearDim/AddAngleDim/AddRadiusDim/AddCustomDim/Reset`；ProfileSketch `GetProfileType/GetEndcutType/GetExcess/GetBevelGapWeb/Flange`）、**PictWinExt**、**SpecSearch/DocumentReference/JigPillar/ConfNoteRec/ResultPipeCheck/ResultPipeStructConn/ShPlateProp/ShStiffProp/PanelSchema/BodyPlanViewOptions/ShellXViewOptions/PanHoleOptions/SplitPanOptions/MovePanOptions/CopyPanOptions**。
- **字符串/工具**：`stringutils.TrimNum(num,prec=-1)/IsStringAllowed/ScanFile(fname,verify_function,flags)`；`Stringlist`（`AddString`，属性 `StrList`）；`Symbollist`（`AddSymbol(font,symbol)`）；`KcsProfSymb.getSymb(type)`；`KcsPythonUtil.PythonUtil.AppendPythonPath(path)`；`KcsTBDVitDef`（`getDefaultdbm()`→`%TEMP%\MenuDef.dbm` 默认值持久化）。
- **高层辅助**：`KcsUtilPos.frp()/lyp()/lzp()`（判定 FR/LP/LZ 位置系统存在）；`KcsUtilDexPan.getIntegerValue/.../getCompInd(Model,CompType,Comp,SubCompType,SubComp)`；`KcsUtilPan.getBox(pan_name)/getPlane/getLimitEnds/getUname`；`KcsUtilPanSch.getGeo/getRef/getDefSurf`；`KcsDrawTable.AddTable(Data,ViewHandle,Name)`（图上画表格）；`KcsCPanDist.CPanDist(PanelName,BaseSeam,EndSeam,FramePrefix,StartFrame,EndFrame,Suffix)`（曲面板距离表全流程）；`cPanel`（`GetTransformationMatrix/GetBoundaryCorners/PanelDataType/FindFreePanelName/pan_delete/GetModelItem` + 类 `AnyPanelLimit/CoordinateLimit/PanelLimit/OuterShellLimit/Panel`）；`cCoordRef/CoordRef3D`；`TribonDwg2Svg`（SVG 转换，27 def）。

---

## 9. 运行入口与部署

1. **环境变量注入**（evars.bat:7）：
```bat
set pythonpath=%pdmsexe%Vitesse;%pdmsexe%Vitesse\Basic_Design;%pdmsexe%Vitesse\Lib;%pdmsexe%python
```
4 个 import 搜索目录：Vitesse 根、Basic_Design、Lib、python（2.6 标准库）。无注册表项。
2. **解释器**：嵌入式 Python 2.6（python26.dll；`<OH>\python\` 为标准库）。启动链：marine.bat → 按模块选 mon/adm/lex/des/iss/marhdes/mardra/marodes/marodra.exe（marine.bat:52-99）。
3. **脚本调起**：(a) 触发器经数据库宏库绑定；(b) 菜单 `menu_item_usr_add(menu,pos,caption,"脚本名")` 按名加载并调用约定入口（`run`/`add`/`pre`/`post`）；(c) 命令窗口 `PYTHON 脚本名`；(d) `__file__` 可定位脚本目录。
4. **print 输出**：同时进 console 与命令窗口；官方封装 `CommonSample.ReportTribonError(module, output)`——output=0 双窗口、1 仅 console、2 仅命令窗口。
5. **日志**：Python 侧无文件日志机制；默认值持久化走 `%TEMP%\MenuDef.dbm`。

---

## 10. 错误处理模式（官方穷举）

1. **try/except + 模块 .error 属性**（全部 kcs_* 模块均有 error 字符串属性）：
```python
# Lib\CommonSample.py:48-61 官方标准封装
def ReportTribonError(module, output=0):
   try:
      import kcs_ui
   except:
      print 'Tribon library not found! Probably no licence for that library.'
      return
   try:
      if output == 1 or output == 0:
         print module.error
      if output == 2 or output == 0:
         kcs_ui.message_noconfirm('Error code: ' + module.error)
   except:
      print 'ReportTribonError function failed!'
```
调用范式（kcs_ex_draft1.py:88-91）：
```python
try:
   kcs_draft.dwg_new(name, form, dwgtype)
except:
   CommonSample.ReportTribonError(kcs_draft)
```
2. **error 可写**（自定义错误码注入）：`kcs_draft.error = 'kcs_HandleInvalid'`，后续比较 `if kcs_draft.error != 'kcs_SubpictureNotValid'`——错误码为 `'kcs_<Name>'` 风格字符串。
3. **TbBaseException**：`except Exception, e: print e`（ctx_menu2.py:28、trig_draft_popup_menu.py:45）。
4. **通用兜底**：`except: print sys.exc_info()[1]; PrintUIError()`（kcs_ex_ui1.py:265-267）。
5. **触发器错误**：`trigger_abort()` 中止；pre 返回 -2 探测法（kcs_ex_trig01.py:116）；`trigger_override()` 覆盖。
6. **licence 缺失探测**：`import kcs_...` 失败即打印 'Tribon library not found! Probably no licence...'.

## 11. 实测备注（坑）

- `kcs_ex_model04.py:133` 引用 `KcsPipeName.PipeName(name)`，但 `KcsPipeName.py` **不在安装内**——该示例在此路径有缺陷，勿照抄。
- `Examples\Drafting\` 编号 1-42 缺 15。
- `Examples\Model\` 与 `Vitesse\Model\` 前 6 文件为部署副本；`kcs_ex_modelstruct01.py` 仅存在于部署目录。
