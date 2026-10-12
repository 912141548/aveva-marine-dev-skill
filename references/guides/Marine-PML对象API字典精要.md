# Marine PML 对象 API 字典精要(Reference Manual 实证)

> 来源:PDMS 12《Software Customisation Reference Manual》§2.5 共 **75 个对象节**(全文在 `PML语料\pdf_text\Software_Customisation_Reference_Manual.txt`,行号见 §9 目录索引)。第 9 轮精读核心 8 类,其余按同法随用随查。
> 用法:**写 PML 涉及对象方法时,先查本文件(已核实签名);没有再到原文 grep(防猜第二步);两者皆无 → 对象不存在该方法,禁止编造。**

---

## 1. ARRAY(2.5.3,全 29 方法)

创建/追加:`Append(v)` `AppendArray(arr)`;`Clear()` 清空。
**规范未载的常用方法**(全部官方签名):
- 集合运算:`Difference(arr)`(差集,去重)/`Intersect(arr)`(交集)/`Union(arr)`(并集)/`Unique()`(原地去重重排)/`SortUnique()`(排序去重副本)
- 查找:`Find(v)` → 下标数组;`FindFirst(v)` → 首个下标(无则 UNSET);`Indices()` → 有值下标数组;`MaxIndex()/MinIndex()` → 最后/首个非空下标
- 子数组:`From(i[,n])`(复制,不动原数组)vs `RemoveFrom(i[,n])`(删除并返回,重排)/`To(i[,n])` vs `RemoveTo(i[,n])`/`Remove(n)`/`RemoveFirst()/RemoveLast()`
- 删除(置 UNSET **不重排**):`DeleteFrom(i[,n])`/`DeleteTo(i[,n])` → 返回被删元素数组
- 插入:`Insert(i, v)`/`InsertArray(i, arr)`(后者重排)
- 其他:`Compress()`(清除 UNSET 并重排)/`Overlay(i, arr)`(覆盖并返回被覆盖值)/`Empty()`/`First()/Last()`/`Width()`(字符串元素最大宽)/`Evaluate(BLOCK)`/`Sort()/SortedIndices()/ReIndex(indices)`/`Invert()`

## 2. STRING(2.5.64,全方法)

- 转换:`Real()`(含扩展英尺英寸格式与单位限定符)/`Boolean()`/`Bore([FORMAT])`/`DBRef([FORMAT])`/`Direction([FORMAT])`/`Orientation([FORMAT])`/`Position([FORMAT])`/`Digits()`(全 Unicode 数字串→正数,否则 -1)
- 校验:`Empty()`/`isDigits()`/`isLetters()`/`isLettersAndDigits()`(均支持全 Unicode 字符)
- 比较:**`EQNoCase(s)`——官方明示比 `upcase().eq()` 更高效可靠**(特别是失败时)
- 查找/统计:`Match(s)` → 子串起始位置(0=未找到)/`MatchWild(s[,多字通配[,单字通配]])`/`Occurs(s)`/`After(s)/Before(s)`
- 提取/变换:`Part(n[,分隔串])`/`Substring(i[,n])`/`LowCase()/UpCase()`/`LT(s)`(ASCII 序)/`Replace(a,b[,第n处[,次数]])`(n 负=从尾数)/`Split([分隔串])`(空格版压缩连续空白,指定分隔版不压缩)/`Block()`(转 BLOCK 求值)
- `String(x)` 转换重载族:BOOLEAN/BORE/DIRECTION/ORIENTATION/POSITION/REAL(+FORMAT 或 'Dn')/DB/MDB/PROJECT/SESSION/TEAM/USER → STRING

## 3. REAL(2.5.56)——量纲系统的完整方法面

REAL 可携带物理量纲,**运算/传参/比较全程保持量纲并自动换算单位**(需量纲兼容)。
- 构造:`Real(STRING)`(带单位限定符即按当前工作单位折算,支持扩展英尺英寸)/`Real(STRING, FORMAT)`(无单位串时 FORMAT 定量纲;**结果恒为当前单位**)/`Real(REAL, UNIT)`(忽略原单位重解读)
- 单位查询:`Value()`(无量纲值)/`Dimension()`(量纲 MEASURE)/`Unit()/Units()`/`AllDimensions()/AllUnits()`
- 单位转换:`Cast(UNIT)`(忽略原单位重解读)vs **`ConvertUnits(UNIT|'单位名')`(物理量不变换单位)**/`DBUnits()`(数据库单位)/`CurrentUnits([UNIT|MEASURE])`(折成当前单位)
- 算术:`ABS/ACos/ASin/ATan/ATanT/ALog/LOG/Cosine/Sine/Tangent/Sqrt/Power(p)`(量纲对象 p 须整数)/`INT()`(向下取整)/`Nint()`(四舍五入)/**`MODULO(p)`**(A−floor(A/p)·p)
- 比较(全部**量纲一致性换算后比较**):`EQ/GT/GEQ/LT/LEQ(REAL|BORE)`;区间:**`Between(a,b)`(含端点)**/`SBetween(a,b)`(不含端点)
- 格式化:`String('D0'..'D6')`/`String(FORMAT)`/**`Distance()`(缺省)**与 `Distance(英尺BOOL, US格式BOOL, 分数BOOL, 精度, 前导零BOOL)`(英尺英寸格式化全家桶)/`Bore()`(精确)vs `NearestBore()`(最近标准通径)

## 4. BOOLEAN / BORE(2.5.7 / 2.5.8)

- BOOLEAN 方法:`AND()/OR(b)/NOT()`/`Real()`(TRUE=1)/`String()`('TRUE'/'FALSE');构造 `BOOLEAN(REAL|STRING)`(字符串 'T/TR/…/YES' 全前缀解析)
- BORE:成员 `Size`(可读写);方法 `EQ/GT/GEQ…`(按当前 BORE 单位比较)/`BORE(REAL|STRING[,FORMAT])`

## 5. COLLECTION(2.5.10,全方法)

`Type(STRING)`(类型过滤)/`Scope(DBREF|COLLECTION|DBREF数组)`(替换作用域)/`AddScope(dbref)`/`AppendScope(数组)`/`ClearScope()`/`Filter(EXPRESSION)`/`ClearFilter()`/`results()`。
**关键语义**:不设 scope 或 `ClearScope()` = **整个 MDB 为作用域**。
(EXPRESSION 见 §6;多类型过滤 `!c.type('EQUI BRAN'.split())` 官方支持——TM-1401 ch7 已证。)

## 6. EXPRESSION(2.5.21)

- `Expression('XLEN + STRING(XLEN)')` 一般表达式;**`Expression('ATTRIBUTE XLEN')` 或快捷 `AttributeExpression('LENGTH')`——属性直取的提速写法**(官方明示速度效率)
- `String()` 回看表达式;`Evaluate(DBREF)` 对指定元素求值
- 表达式例:`('PURP eq |PIPING|')`

## 7. FILE(2.5.22,全方法)

- 读写:`Open('READ'|'WRITE'|'OVERWRITE'|'APPEND')`/`ReadRecord()`(EOF 返回 UNSET STRING)/`ReadFile([行数上限])`/`LineNumber()`/`Close()`/`IsOpen()`/`AccessMode()`
- 文件系统:**`Copy(路径|FILE)`/`Move(路径|FILE)`/`DeleteFile()`**(移动复制删除!)/`Exists()`/`Size()`(字节)/`DTM()`(DATETIME 修改时间)
- 目录导航:**FILE 对象可指目录**——`Directory()`(上级)/`Files()`(子文件 FILE 数组)/`SubDirs()`(子目录)/`Path()`(全上级链)/`FullName()/Name()/PathName()/Entry()`

## 8. BLOCK(2.5.6)

`Block('表达式串')` 延迟求值;`Evaluate()`(可带类型检查参数);`!arr.evaluate(object BLOCK('|!arr[!evalIndex].attr|'))` 中 **`!evalIndex` 是系统游标固定名**。

## 9. FORM(2.5.24,全成员+全方法)

**成员**:FormRevision/FormTitle/IconTitle/Initcall/**Autocall**(指定的应用属性变化时执行的回调——未见于 Guide!)/Okcall/Cancelcall/Quitcall/Killingcall/FirstShownCall/KeyboardFocus/**AutoScroll**(尺寸不足自动出滚动条;MAIN/DOCUMENT 不适用)/**Maximised**/**Active**(只读)/**Popup**(表单当前右键菜单)/**HelpContextID**(F1 上下文 ID)。
**方法**:
- `Name()/FullName()`(含 !!)/`Subtype()`('DIALOG'/'BLOCKINGDIALOG'/'MAIN'/'DOCUMENT')/`Owner()`(**父表单,free 时 UNSET**)
- `NewMenu(名[,'POPUP'|'MAIN'])`
- `SetActive(bool)`(灰显可精确还原)vs `SetGadgetsActive(bool)`(强制改状态,可叠加使用)
- `SetPopup(menu)`/**`RemovePopup(menu)`**/**`GetPickedPopup()`**(最近一次弹出的菜单)
- `Show()` / `Show('FREE')` / `Show('AT',x,y)` / `Show('CEN',x,y)` / `Shown()` / `Hide()`
- **`SetOpacity(10~100)`**——表单透明度(仅非停靠 DIALOG/BLOCKINGDIALOG)
- `SetUndoable(...)`/`Undoable(...)`
**生命周期权威表**:Define→Load(构造器跑一次)→Show(**每次 show 都触发 INIT**/initcall)→Activate(**FIRSTSHOWN 只发生一次**)→Hide(OK/CANCEL 事件)→Kill(KILLING 事件后销毁,不再为 PML 所知);**非 MAIN 表单 quit:隐藏整巢并按显示逆序逐个执行 CANCELCALL**。
**setup form 语法图全参数**:MAIN / DOCUMENT+FLOAT / DIALOG+DOCKING(Left/Right/Top/Bottom)+RESIZEABLE / BLOCKINGDIALOG+RESIZEABLE / VARCHARS / FIXCHARS / AT / SIZE / NOQUIT / NOALIGN / CORE。
**缺省值冲突待裁决**:Reference Manual 本节写 "Defaults: Path right, **Hdist 1.0, Vdist 0.25**, Valign top, Halign left",而 Guide ch17 写 "HDIST 0.2, VDIST 1.0"——两官方书矛盾(TODO-UNVERIFIED,以实测为准,布局不依赖缺省值最稳)。

## 10. FORMAT(2.5.25,13 成员全表)——距离/位置格式化中枢

| 成员 | 缺省 | 说明 |
|---|---|---|
| `Units` | 'MM' | 'MM'/'M'/'FINCH'(英尺英寸)/'INCH'/任意标准或复合单位限定符 |
| `Dimension` | 'NONE' | 'L'/'L2'/'L3'/'NONE'/任意量纲或单位限定符(间接定量纲);**用时才校验** |
| `DP` | 2 | 小数位数 |
| `Fraction` | FALSE | TRUE=分数输出(配 Denominator=32 最大分母、PadFractions、InchSeparator'.') |
| `FtLabel` | `'` | 英尺标签(FT/ft/feet…) |
| `Label` | 无 | 距离标签;**设为 'UNITS' = 输出标准单位限定符**;自定义标签在回读时会被系统反向解析 |
| `ENU` | TRUE | POSITION 输出 ENU 格式;FALSE=XYZ |
| **`OriginExp`** | '\|/\|' | **POSITION 的 WRT 参照(BLOCK)**:'\|CE\|' = 相对当前元素输出! |
| `Zeros` | TRUE | 英制前导零 |
| `TrailZeros` | TRUE | 尾零(含小数点) |
| `CompSeparator` | 空格 | POSITION 多分量分隔符 |

(文本控件 `text ... format !!fmt` 的显示与回读解释都由它控制;单位换算入口见 REAL 的 ConvertUnits 族。)

## 11. MENU(2.5.37,全成员+全方法)

**成员**:`Callback`(菜单级回调,可读写);`PickedField`(**已废弃**)→ **`PickedFieldName`**(最后点选的 TOGGLE/CALLBACK 字段的字段名)。
**Add/InsertAfter/InsertBefore 全类型**:`CALLBACK` / `FORM`(formName 可 NULL 不可空串) / `MENU`(pullright) / `TOGGLE`(**回调必须是 open PML function**——官方明示,用来收 SELECT/UNSELECT) / `SEPARATOR`(可命名字段名);全类型均有 CORE 变体:**CORECALLBACK/COREFORM/COREMENU/CORETOGGLE/CORESEPARATOR**(核心托管,不必给回调——与 Guide 附录 A 互证)。
**已废弃方法族**(新代码禁用,用 `SetFieldProperty/FieldProperty` 替代):`Clear()/Clear(dtext)/Select(Dtext,bool)/Selected(Dtext)/SetActive(Dtext,bool)`。
其他:`FieldProperty(字段,'ACTIVE'|'VISIBLE'|'SELECTED')`(SEPARATOR 影响**隐含字段组**) / `PopupGadget()` / `Refresh()` / `FullName()/Name()/Owner()`。
**菜单规则**(官方重申):Main 体系菜单全局只能出现一次;Popup 体系可在多棵树各出现一次;禁止自引用;未指定类型时由首次使用推断——动态创建必须显式给类型。

## 12. POSITION(2.5.51,全成员+全方法)

**成员**:`East/North/Up`(REAL 读写)/**`Origin`(DBREF 读写——位置可带参照元素!)**。
**方法**:
- 构造:`Position(STRING[,FORMAT])`
- 变换/查询:`WRT(DBREF)`(**转换到指定元素的参照系**)/`Component(DIRECTION)`(方向分量)/`EQ/LT(POSITION)`/`String(FORMAT)`(配 FORMAT.OriginExp 可输出相对 CE)/`Distance(POSITION|LINE|ARC|PLANE)`(四重载,到线/弧/面的最近距离)
- 几何构造(`this`=X 点):**圆弧六法** `ArcCentre(A,B,方向,半径)`/`ArcFillet(A,B,方向,半径)`/`ArcRadius(A,B,方向,半径,major布尔)`/`ArcThru(A,B,方向)`/`ArcThru(A,B,方向,半径)`/`Arc3Lines(线,线,线,方向)`——全部返回 ARC;另有 `Angle(A,B)`(本点为顶点的夹角)/`MidPoint(pos)`/`Near(pos,距离)`/`Offset(方向,长度)`/`Plane(p1,p2)`(三点定面)/`Line(pos)`(两点连线)/`Direction(pos)`(手册标注返回 BOOLEAN,疑为 DIRECTION——TODO-UNVERIFIED)

## 13. POSTEVENTS / UNDOABLE(2.5.52 / 2.5.71)

- **POSTEVENTS**:约定必须建全局对象**名为 `!!postEvents`**,实现五方法:`postMark(str)/postUndo(str)/postRedo(str)/postClearMark()/postClearAll()`——所有撤销栈动作(含 MARKDB、核心操作)都会回调,参数=关联描述文本。
- **UNDOABLE**:`description(str)` → `add()`(MarkDB+入栈)→ 改库 → `endundoable()`(再 MarkDB 收尾);`undoAction(str)/redoAction(str)/clearAction(str)` 定执行串;表单/gadget 回调级用 `setUndoable()`(第 5 轮 ch14 已证)。

## 14. LIST Gadget(2.5.32,成员+方法)

**成员**:`Val`——单选=REAL(**0=无选择;必选列表置 0 报错**),多选=REAL 数组;`DText/DText[n]`(整表/单行显示文本);`RText/RText[n]`;`PickedField`(最后点选行号,只读);`Count`(行数,只读)。
**方法**:`Add(dtext[,rtext])` 追加单行;`Select('Rtext'|'Dtext', 值|值数组)`;`Selection()` 回选中 Rtext(数组),`Selection('Dtext')` 回显示文本;**`Clear()` 清全表 vs `ClearSelection()` 只清选择 vs `Clear(dtext|行号)` 删单行**;多列 `SetHeadings(串|数组)`/`SetRows(行数组的数组)`/`SetColumns(...)`;通用 gadget 方法族 `SetPopup/RemovePopup/GetPickedPopup/Refresh/Shown/Type/SetToolTip/SetFocus/FullName/Name/Owner`。

## 16. TEXT / SELECTOR Gadget(2.5.68 / 2.5.61)

**TEXT 成员**:`Val`(STRING/REAL/BOOLEAN/用户类型四形态读写)/`DataType`/`Echo`(NOECHO 状态,只读)/`Format`(关联 FORMAT 对象名,只读)/`Scroll`(只读)/`ValidateCall`(校验回调,读写)/**`Editable`(读写)**。
**TEXT 方法**:`Clear()`/`SetEditable(bool)`/`SetFocus()/SetToolTip/Refresh/Shown/Type`/**`SetValue(value, validate布尔)`——程序赋值并可触发校验回调**/**`SetEditable('HANDLEMODIFY', n)`——MODIFIED 事件三档:0=关(缺省)/1=仅首次修改/2=每次修改**。
**TEXT 定义语法**:WIDTH/SCROLL(≤256)/NOECHO/`IS STRING|REAL|BOOLEAN|word FORMAT !!gvar`——**用户自定义类型必须配 FORMAT 对象才可用**;CORE 限定符可选。
**SELECTOR**:成员/方法与 LIST 同族(Val/DText/PickedField/Add/Select/Selection/Clr 系列);**定义语法图确认缺省**:SINGLE 选择、DATABASE 无限定词时 = MEMBERS+OWNERS 双向、**AUTO 缺省关**;`Background()` 色名查询(部分 gadget 不支持)。

## 17. 系统对象 MDB / DB / SESSION(2.5.35 / 2.5.17 / 2.5.62)+ 系统数组

- **构造捷径**(性能利器):`object DB(!!CE)` / `object DB(!!CE.Name)` / `!!CE.DB()` / `!!CE.Name.DB()`——**DB 元素到对象四条路**;MDB/SESSION 同款。系统数组:**`DBS`/`MDBS`/`MACROS`/`TEAMS`** 直接给全工程对象数组。
- **DB 成员**:Name/Description/**Access(UPDATE|MULTIWRITE|CONTROLLED)**/**Claim(EXPLICIT|IMPLICIT)**/File(≤17 字符)/Foreign(FOREIGN|LOCAL)/Number/Team/Type(如 DESI)/Refno/**Primary(PRIMARY|SECONDARY,Global 工程位置相关)**。
- **DB 方法**:`MDBList()`(包含此库的 MDB 列表)/**`Size()`(页数,非字节)**/`Sessions()`(DBSESS 数组)/`Lastsession()`。
- **MDB 成员**:Name(≤32)/Description(≤120)/Refno + MACRO 记录成员(Filename/From/To/Number——库间宏);**方法**:`Current()/Deferred()`(当前/延迟库数组)、**`Mode()`(每库 'NR'|'RW')**。
- **SESSION 成员**:UniqueID/Name/Login/Host/Entered/LocationName/IsRemote/IsCurrent;**方法**:`SESSION(UniqueID)`/**`ConfirmID('/密码')`(校验当前用户密码!)**/`Current()/Deferred()/Mode()/Status()`(库访问态 'R'|'RW'|'N')/`Location()/MDB()/User()/Module()/Modified()`;**远端会话限制**:Modified/Current/Deferred/Mode/Status 仅限本机当前会话,Location/MDB/User/Module 可用于远端(会触发 Daemon 活动,先开对应位置的 system DB)。

## 18. gadget 族成员方法(2.5.9/13/14/39/41/70 实证)

**OPTION / COMBOBOX**(同族,方法几乎一致):
- 成员:`DText/RText`(整表/`[n]` 单项)、`Count`、`Val`(**0=无选择,未设 ZeroSel 时置 0 报错**);COMBOBOX 另有 **`Editable`/`Scroll`(可读写)**
- 方法:`Add(dtext[,rtext])` / `Clear()` / **`ClearSelection()`(回到列表第一项=缺省选择)** / **`Clear(dtext)` / `Clear(行号)`(删单项)** / `Select('Rtext'|'Dtext', 值)` / `Selection([type])` / **`DisplayText()`(读显示框当前文本,VALIDATE 事件配套)** / COMBOBOX 独有 **`SetDisplayText(text)`** / `SetPopup/RemovePopup/GetPickedPopup/Refresh/SetFocus/Background()`
- 定义限定符:**`NORESELECT`(重击已选项不发事件)/ `ZEROSELECTION`(允许无选择)/ `PIXMAP` / `CORE`**
- 事件:UNSELECT 仅 open callback 才通知;**官方建议不要在 UNSELECT 里程序性改选择**;COMBO 可编辑框回车触发 VALIDATE(须 open callback 区分),用 DisplayText() 取输入

**NUMERICINPUT**:成员 `val` / **`range`(REAL 数组 [Start,End,Step],可读写)** / `ndp`(只读)/ `modifiedEvents` / `editable`;方法 `setRange(!range, !ndp)`(**ndp<0 = 保持现值**);行为:缺省初值=range 最小值、**range 上限自动调整为整步数**、键入值吸附到最近合法值、不支持用户格式化;SELECT(回车)/MODIFIED(步进,须 open callback 且缺省关)。

**BUTTON**:成员 `Val`(BOOLEAN 按压态——toggle 型)/ **`Background`(色号 REAL 读写;色名 STRING 只写)**;方法 **`AddPixmap(file1[,file2[,file3]])`(未选/选中/禁用三态;禁用图已可省——自动灰显)**/`Subtype()`(Normal/Toggle/Linklabel)/通用族;**Linklabel 六限制**:不可配图、不可改背景色、无按压值、无边框、可挂右键菜单(不建议)、**无 OK/CANCEL 等控制属性**;**Linklabel 按下会触发表单所有已修改文本字段校验**。

**TOGGLE**:成员 `Val`(BOOLEAN);方法 `AddPixmap(file1[,file2])`(未选/选中;尺寸定义时要预留最大图);定义 `STATES text1 text2` 定 OFF/ON 文本(rtoggle 的 onValue 同源);显示后仍可换图。

**CONTAINER(.NET 宿主)**:成员 `type`/**`control`(外部控件整数句柄,读写)**/**`popup`(关联右键菜单,读写)**;方法 **`ShowPopup(x,y)`——坐标是控件内部像素位置**;定义 `CONTAINER 名 NOBOX|INDENT PMLNET [+handle]`;**只支持 PMLNet 控件**;定位必须先于尺寸;Dock/Anchor 有效(控件须支持缩放,通常 Dock fill)。

## 19. 几何族:DIRECTION / ORIENTATION / PLANE / LINE / POINTVECTOR(2.5.20/42/44/30/50)

- **DIRECTION**:成员 `East/North/Up`(读写)+ **`Origin`(DBREF,参照系)**;方法 `Direction(串[,FORMAT])`/`EQ/LT`/`String(FORMAT)`/**`WRT(DBREF)`**/`Angle(d)`(两方向夹角)/`Bisect(d)`(角平分)/`Cross(d)`(叉积)/`Dot(d)`(点积)/`IsParallel(d[,容差])`/`Opposite()`/`Orthogonal(d)`(两方向正交向)/`Projected(plane)`(投影到面)。全部方法不改原对象。
- **ORIENTATION**(只定轴向不定位置):成员 `Alpha/Beta/Gamma` + `Origin`;方法 `Orientation(串[,FORMAT])`/`EQ/LT`/`String(FORMAT)`/`WRT(DBREF)`/**`XDir()/YDir()/ZDir()`**(三轴方向,assyhsv.pmlfnc 的 `.ori.zDir()` 即伪属性版)。
- **PLANE**:成员 `Position`(原点)/`Orientation`;定义 `Plane(POSITION, ORIENTATION)`;**Towards(pos)** 改法向指向;求交族:`Intersection(LINE|POINTVECTOR)` → POSITION、`Intersections(ARC)` → 数组、**`Intersection(PLANE, PLANE)` → 三面交点**、`Intersection(PLANE)` → 交线(重合时回 1000mm 线)、`Near(pos)`(面上最近点)、`ThreeDPosition(XYPOSITION)`、**`XYOffset(pos)`(映射到面的 XY 偏移)**、`Line(长度)`(沿法向)、`PointVector()`。
- **LINE**:成员 `StartPosition/EndPosition`;定义 `Line(p1,p2)`/`Direction([d])`;判定 `On(pos[,bounded])/OnProjected(pos)`;求交 `Intersection(LINE|POINT+VECTOR|PLANE)`/`Intersections(ARC)`;`Near(pos)`/**`Proportion(r)`(沿线比例取点,<0/>1 可出界)**;`Length()/Distance(LINE|POSITION)`;派生 **`SetLengthStart/SetLengthEnd/Towards/From/To/ExtendStart/ExtendEnd`**(改头改尾改向改长,全部返回新 LINE)+ `Plane()/Pointvector()`。
- **POINTVECTOR**(点+方向射线):成员 `Position/Direction`;`Pointvector(pos,dir)`;`Offset(距离)`(沿向推移)/`Towards(pos)`/`Through(pos)`(过垂面交点);求交 `Intersection(POINTVECTOR|LINE|PLANE)`/`Intersections(ARC)`;**`Plane()`(以射线为法向的面)**/`Line(长度)`。
- **意外收获 PMLUSERLOGIN(2.5.49)**:`Macro(全路径宏)/MDB(名)/Project(名)` → **`SaveToFile(路径)`(加密保存自动登录宏)**/`VerifyNonInteractive(TRUE)`(校验生成的宏无交互)——独立进程免密启动的官方工具。

## 21. 系统杂项:USER / TEAM / PROJECT / UNIT / DATETIME(2.5.73/67/53/72/16)

- **USER**:成员 Name(≤32)/Description(≤120)/**Access(FREE|GENERAL|RESTRICTED)**/Refno;方法 `TeamList()`(所在团队)/`WorkingList()`(用户的工作提取库)/**`Password()`(无返回值——不可读密码)**/构造四捷径。
- **TEAM**:成员 Name/Description/Refno;方法 `DbList()`(团队拥有的库)/`UserList()`(团队成员)/构造四捷径。
- **PROJECT**:成员 Name/Evar(如 MAR000);方法 `Active()`(活动用户数)/`Code()`(三位码)/`Isglobal()`/**`Locations()/CurrentLocation()`(Global 工程位置)**/`Sessions()/CurrentSession()`/`Dblist()`/`Description/Message/Number/Mbcharset`。
- **UNIT**(量纲枚举的完整接口):构造 `Unit()/Unit(REAL enum)/Unit(STRING)`(串=Description/Name/ComponentName/HashCode——**派生单位哈希 'DRVD'、无量纲 'NUMB'**);名称 `Description()/Name()/ShortName()/Hashcode()/Ptype()`;查询 **`Enum()`/`Factor()`(到数据库单位换算因子)/`UnitQualifier()/Dimension()/IsStandard()/IsNull()/IsImperial()/IsMetric()`/`AllDimensions()/AllUnits()`**。
- **DATETIME/DATEFORMAT**:`DateTime()`(当前时刻)/`DateTime(y,m,d[,h,min])`(月份可传 'Jan' 等串);**DATEFORMAT 格式串 `'T*D*M*Y'`(T时间/D日/M月/Y年,字母顺序即输出顺序)**、`.Month('INTEGER'|'BRIEF'|'FULL')`、`.Year(2|4)`;`String(DATETIME|串)` 双向转换。

## 22. VIEW 族 gadget 成员方法(2.5.76-79)

- **公共**:成员 `Background`(色号读写+色名方法)/`Highlight`/`Borders`/`Width/Height`(只读)/`Subtype`/`Contents`/`Defcall`;方法 `Refresh/SetSize(w,h)/**SaveView(n)/RestoreView(n)**`(n=1..4,Guide 附录 B 已证)。
- **ALPHA**:`.size()`/`.dynamic()`(动态模式判定)/成员 `Channel`/`Clear()`/**`removeRequests()`**(表单显示后才可调,定义期报 (61,605))/`SetFocus()`。
- **AREA**:`Limits`(窗口)/`Contents`(元素号)/**`Defcall`**(定义回调成员)。
- **PLOT**:`Add('plot文件')`(**替换式**)/`Clear()`。
- **VOLUME**:`Direction`/`EyeMode`/`Limits`/**`Mousemode`(串)**/**`Projection`(串)**/`Radius/Range/Step`/`Shaded`——与 Guide ch20 的方法族互为成员/方法两面。

## 23. 容器/表格/报告收尾:FRAME / BAR / TABLE / PMLReport(2.5.26/5/66/47)

- **FRAME**(成员):`Tag`/`Val`(单选组选中序号)/`Callback`(单选组回调)/**`RGroupCount`**(只读,非单选组回 0)/**`Expanded`(FoldUpPanel 折叠态,读写)**;方法 `Rtoggle(index)`。**官方补强**:TABSET 内的直接子 frame 只能是 NORMAL(不可 TOOLBAR/TABSET 嵌套);TOOLBAR 内容白名单 = BUTTON/TOGGLE/OPTION/TEXT + 表单变量 + VAR 赋值 + 通用 PML;FOLDUPPANEL 不可嵌套 FOLDUPPANEL;HIDDEN/SHOWN 仅 open callback 才触发(单选 SELECT 可用简单回调)。
- **BAR**(全方法):Add(dText,菜单名)/InsertAfter/InsertBefore/Clear(废弃)/SetFieldProperty/FieldProperty(**仅 ACTIVE|VISIBLE,无 SELECT**)/SetActive(废弃)/Shown()/FullName/Name/Owner。
- **TABLE**(电子表格式数据容器):构造 `Table(DBREF数组|COLLECTION, COLUMN数组)`;`PrimaryKey(...)`/`Columns(...)`/`Evaluate()`(全表求值)/`EvaluatePrimaryKey()`/`Cell(列,行)`(数字或 key+DBREF 双形态)/`Row(n)/Column(n)`;另有一个同名内建 `state()/modifyMode()/featureHighlight(bool)` 的 3D 特性高亮控制对象(官方文档同名两物,按语境区分)。
- **PMLReport(.NET 报告批跑)**:`import 'ReportingAddin'` → `object PMLReport()`;`addParameters(名数组,值数组)`(参数化报告)/**`AddScope(祖先元素串, 元素串)`**(覆盖报告范围)/`exportAsCsv(.repv 路径, .csv 路径)`;响应事件收加载错误——**批处理出报表的官方通道**(ReportingAddin 在 DesignAddins 名单内)。

## 26. 低频类概览(第 38 轮,75 类全覆盖)

- **TABLE/COLUMN/REPORT/COLUMNFORMAT 四件套 = PML 报表引擎**:TABLE 持数据(主键=DBREF 数组或 COLLECTION)→ COLUMN 定取数(AddType/Types/Filter/Scope/Results/Next(n)/Index)→ REPORT 定输出(AddColumn(key, COLUMNFORMAT, heading);Results()/NextEntries()/NextLines() 三种取数节奏;MATCH 串过滤;SetCaseMatch)→ COLUMNFORMAT 控列格式。同一 TABLE 可出多份 REPORT。
- **IDList**(2.5.28):drawlist 选择集操作——.selected(dbref)(取显著父)/.isSelectable/.isModifiable/.inSelection/.getSelection()/.ancestors(dbref);只操作 drawlist 层级以上的显著元素。
- **ViewFinder**(2.5.75):Draft 视图在 3D 视图中的取景框——.viewFinder(view 的 dbref) 创建,可移动/旋转(不改大小),出图排版可视化。
- **PMLUSERLOGIN/VERIFY**(2.5.49/74):加密登录宏生成 + 授权锁定——日期窗(After/Before DATETIME)、主机白名单(Hostname 串|数组)、Windows 用户白名单(WinUser 串|数组),与 SaveToFile 组合成"绑定机器/用户/时间窗的免密启动宏"。
- **MDRM**(2.5.38,434 行):多专业路由大型接口(mdrRoutePoint.OwningDbBranch/OwningRoute 等),路由专用,按需精读。

## 24. §2.5 全目录(75 节,原文行号 → 随用随查)

ALERT 821 / ARC 877 / **ARRAY 1202** / BANNER 1413 / BAR 1443 / BLOCK 1535 / **BOOLEAN 1539** / BORE 1582 / **BUTTON 1628(已精读→§18)** / **COLLECTION 1819** / COLUMN 1858 / COLUMNFORMAT 1914 / **COMBOBOX 2003(已精读→§18)** / **CONTAINER 2205(已精读→§18)** / DATEFORMAT 2263 / **DATETIME 2283(已精读→§21)** / **DB 2394(已精读→§17)** / DBREF 2466(MCount/PPosition/PDirection/BadRef/Line,第 1 轮已证)/ DBSESS 2512 / **DIRECTION 2515(已精读→§19)** / **EXPRESSION 2601** / **FILE 2644** / FMSYS 2750 / **FORM 2902(已精读→§9)** / **FORMAT 3338(已精读→§10)** / FRAME 3501(**已精读→§23**) / Graphical Selection 3691 / IDList 3767 / LINE 3859,3904(**Object 已精读→§19**) / LINEARGRID 4243 / **LIST 4281(已精读→§14)** / LOCATION 4527 / MACRO 4601 / **MDB 4605(已精读→§17)** / MEASURE 4670(DBUnits/DBUnit/UnitsOf/AllDimensions/AllUnits/Enum) / **MENU 4767(已精读→§11)** / MDRM 5184 / **NUMERICINPUT 5619(已精读→§18)** / OBJECT 5702 / **OPTION 5716(已精读→§18)** / **ORIENTATION 5888(已精读→§19)** / PARAGRAPH 5948 / **PLANE 6044(已精读→§19)** / PLANTGRID 6192 / PLATFORMGRID 6237 / PMLReport 6379(**已精读→§23**) / PMLSECURELOGIN 6492 / **PMLUSERLOGIN 6540(已精读→§19,加密登录宏生成器)** / **POINTVECTOR 6545(已精读→§19)** / **POSITION 6656(已精读→§12)** / **POSTEVENTS 6851(已精读→§13)** / **PROJECT 6897(已精读→§21)** / PROFILE 6948 / RADIALGRID 7361 / **REAL 7419** / REPORT 7676 / RTOGGLE 7837 / Section Plane 7926,8013 / **SELECTOR 8156(已精读→§16)** / **SESSION 8302(已精读→§17)** / SLIDER 8412 / **STRING 8516** / STATE 8837 / **TABLE 8841(已精读→§23)** / **TEAM 8933(已精读→§21)** / **TEXT 8979(已精读→§16)** / TEXTPANE 9132 / **TOGGLE 9220(已精读→§18)** / **UNDOABLE 9332(已精读→§13)** / **UNIT 9364(已精读→§21)** / **USER 9449(已精读→§21)** / VERIFY 9495 / ViewFinder 9502 / **VIEW ALPHA 9579 / AREA 9628 / PLOT 9733 / VOLUME 9830(已精读→§22)** / XYPosition 10000

## 25. 与记忆文件 R22 的关系

R22"内置对象方法速查"标注"待后续按需精读补全"——**75 类全部概览级覆盖**(高频 46 类方法级,低频 29 类概览级见 §26),R22 正式由本文件替代。
