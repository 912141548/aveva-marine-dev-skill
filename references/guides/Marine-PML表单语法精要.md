# Marine PML 表单语法精要(setup form 体系,Guide ch13-20 实证)

> 来源:PDMS 12《Software Customisation Guide》第 13-20 章逐节精读(2026-09-25 第 3 轮,全文在 `PML语料\pdf_text\Guide_ch8_14.txt` 与 `Guide_ch15_20.txt`,带 PDF 页码)。
> 定位:Marine 语料 1380 个 .pmlfrm 全部是 `setup form` 体系——本文件是该体系的权威速查(记忆文件的 R17-R19 基于 E3D `layout form`,两套并存时**以本文件为准**用于 Marine)。
> 通用规则:gadget 定义 = `类型 .名字 {通用属性:position/tag/tooltip/callback/anchor/dock,任意序} {专有属性:顺序按语法图}`;**几何属性定义后不可改**(唯一例外:可缩放表单上的 VIEW gadget)。

---

## 1. 表单定义与类型(ch13/15)

```
setup form !!name <类型> <布局> <尺寸> <修饰>     ← 只能设一次的属性必须在 setup 行
   ... gadgets / member 声明 / 子命令 ...
exit
define method .name() ... endmethod              ← 构造器(与表单同名,仅 load 时跑一次)
```

**类型**(setup 行,互斥):`MAIN`(工具条+菜单供给 AppWin,不直接显示)/ `DOCUMENT`(MDI 子窗,可浮离,可拖去另一屏)/ `DIALOG`(缺省:浮动不可缩放;加 `RESIZABLE` 可缩放;加 `dock left|right|top|bottom` 停靠且默认可缩放)/ `BLOCKINGDIALOG`(阻塞一切其他表单)。
其他 setup 行属性:`size w h`(最小尺寸,单位=字符宽/行高)、`RESIZABLE`、`NOQUIT`(禁边框关闭)、`NOALIGN`、`VarChars`/`FixChars`、`Float`(document 浮离)。

```bat
setup form !!f dialog dock left      → 可缩放停靠
setup form !!f dialog resizable      → 可缩放浮动
setup form !!f document Float        → 浮动非 MDI 文档
```

**布局模式**:`setup form` **缺省 FixChars**(旧等宽近似,要频繁 TagWidth/Width 试错);新表单加 `VarChars`(按真实串宽测量,更紧凑)——PDMS12.1 时代 VarChars 是推荐值,`layout form`(未来语法)= 强制 VarChars+NoAlign。`!!FMSYS.SetDefaultFormLayout('VarChars')` 可整体切换测试。
**NOALIGN**:关掉 TEXT/OPTION/COMBO/TOGGLE/单行 paragraph 在横排时的"伪居中对齐"——复杂表单一律加。

## 2. 表单级回调(ch15)

| 成员 | 触发 | 要点 |
|---|---|---|
| `initcall` | 每次显示前 | **不得显示其他表单/请求用户输入**(可 ALERT);`return error 1 '消息'` 可中止显示(已弹过窗用 `return error 1 NOALERT`) |
| `okcall` | OK 按下(含祖先 OK 级联) | 收数据干活;OK 按钮**自身的 callback 会被忽略** |
| `cancelcall` | CANCEL/关闭/祖先 CANCEL | gadget 自动重置到显示时或上次 APPLY 的值 |
| `quitcall` | 标题栏 X | MAIN 表单:确认后执行退出命令不返回 / `return error …noalert` 表示不退;普通表单:无 quitcall=默认 Cancel;要自己 hide(`!this.hide()`);**DOCUMENT 表单 quitcall 里不得弹 ALERT**(会弄坏 gadget) |
| `firstShownCall` | 首次真正显示后 | 窗口管理器可见性/背景色等"必须已显示才能做"的动作 |
| `killingCall` | 表单销毁前 | 清理全局资源(全局对象能活过模块切换);**禁止改表单和 gadget**(只能查询) |

- 成员声明:`member .x is TYPE`(寿命=表单,kill 时销毁);`!!form.gadgets()` 返回 GADGET 数组(除 USERDATA);`q var !!formname` 调试全列。
- **Form Family**:button `FORM !!child` 或 callback `show !!child` 产生子表单;父 OK/CANCEL 按"最年轻优先"级联子表单后全隐藏;`show !!form free` 脱离家族。定位:`show !!f Free At xr 0.3 yr 0.5`(原点)、`Free Centred`、`!f.show('At',0.3,0.5)` / `show('Cen',0.5,0.5)`(屏幕比例坐标)。
- **hide 陷阱**:`hide !!f` 会重置 gadget 值(同 CANCEL)但**不执行 cancelcall**——hide 前先取走数据。
- **kill 慎用**:kill 后再 show 走慢速 demand-load;要重复显示用 `loadform !!f` + `!!f.show()`(show() 不动态加载定义)。对已存在表单再执行 `setup form !!同名` = kill+重建(可用来在 AppWare 里动态生成表单,慎用)。
- 表单改名/改标题:`!!f.formTitle = ...` / `!!f.iconTitle = ...`。

## 3. 布局系统(ch17)

**坐标系**:容器(表单/frame)左上原点(0,0);水平格距=标称字符宽,垂直格距=行高(最高单行文本 gadget);每个 gadget 有 box(含 tag),极限记作 `xmin.g1 / ymax.g1`,表单为 `xmin form` 等;加入 gadget 会撑大容器的 xmax/ymax。

**自动放置**:`path right|down|left|up`(缺省 right,持续生效);`hdist`(缺省 0.2)/`vdist`(缺省 1.0)是**相邻 gadget 盒之间的净距**不是原点距;`halign left|centre|right`、`valign top|centre|bottom`(横排用 hdist+valign,竖排用 vdist+halign;横排缺省 halign left+valign top)。frame 内首个 gadget 自动放 `(hdist/2, vdist/2)`。
官方推荐惯用组合:`path down` + `vdist 0.2`;`path right` + `hdist 1.0`。

**AT 相对定位**(推荐,少用绝对坐标):
```pml
toggle .t AT xmin ymax+1                    -- 相对上一个 gadget
button .ok at xmax form - size OK           -- 右对齐不撑宽表单(form-size 技巧)
button .cancel at xmin form ymax form CANCEL
frame .f2 at xmin.f1 width to min.f1 hei to max   -- 尺寸=到参照物极限的距离(width to/height to)
frame .p2 Panel anchor all at xmin.p1 width.p1
```
X 和 Y 可各自独立用自动或相对;可跨不同参照:`AT xmin.g1 ymax.g2+0.25`;表达式算术合法(`width to max.fr1 * 0.5 + hdist`,星号两侧必须有空格)。

**Tag 宽度语义**(决定 width/height 到底量什么):

| 类别 | gadget | width/height 含义 |
|---|---|---|
| 行内 tag | TEXT/OPTION/COMBO/TOGGLE/RTOGGLE | 量 data-box+decoration,**不含 tag**(tag 在左,占宽) |
| 盒上 tag | LIST/SELECTOR/TEXTPANE/ALPHA | width 量盒宽,height 量**可见行数**,tag 占高 |
| 无 tag | SLIDER/paragraph/G2D/G3D | 直接量盒 |
| 整体盒 | BUTTON/FRAME | 直接量盒(BUTTON 的 tag 在按钮内居中,与 width 无关) |

`tagwid n` 只在两处需要:给后设的 tag 预留空间、对齐一组 gadget 的 data-box。

**ANCHOR/DOCK**(定义时设,运行期不可改,互斥):anchor 任选 left/right/top/bottom 组合或 all/none(缺省 top+left);dock left/right/top/bottom/all/none。**ALPHA/VIEW 不支持**——放进独立 frame,给 frame 设 anchor/dock。

**布局清单(ch17.12 官方)**:①很少需要显式设表单宽高 ②用 VarChars ③`path down vdist 0.2` 免掉 `at ymax+0.2` ④`path right hdist 1.0` 免掉 `at xmax+1.0` ⑤anchor 只需 top+left 时不用写 ⑥少用字面坐标,多相对 ⑦frame 尺寸一般不用设 ⑧`form-size`/`.gad-size` 右对齐技巧(如 `button .nextPage linklabel 'Next' anchor bottom+right at xmax form-size ymin`)。

## 4. Frame(ch18/20.2)

五类型:`NORMAL`(有边框,任意嵌套)/`TABSET`(页签容器,无边框无 tag)/`TOOLBAR`(**只能出现在 MAIN 表单**,只准 BUTTON/TOGGLE/OPTION/TEXT/COMBOBOX/SLIDER/NUMERICINPUT,gadget 按定义顺序单行排;MAIN 上 toolbar 外的 gadget 归入名为 'Default' 的工具条)/`PANEL`(无边框,可 INDENT 做 3D 凹陷)/`FOLDUPPANEL`(带标题栏可折叠,`EXPANDED` 属性定初态;折叠时下方 gadget 上移,配合表单 AutoScroll 出滚动条)。

- **单选组**:frame 直接包含的 RTOGGLE 组成 radio group(仅 NORMAL/PANEL/FOLDUPPANEL 有效);`!frame.val`=选中序号(**0=全不选**);`!frame.rtoggle(!idx)` 取对象、`.onValue` 取该钮值;取消选中选择=置 `!frame.val = 0`;frame callback 仅 SELECT(简单回调即可);或给每个 rtoggle 挂 open callback(UNSELECT/SELECT)。事件顺序:**UNSELECT(旧钮)→ SELECT(新钮)→ SELECT(FRAME)**。
  - 防焦点陷阱:构造器里 `!this.keyboardFocus = !this.ok`,避免 Windows 把焦点给第一个 rtoggle。
- **TABSET**:直接子 frame 即页签页;页 SHOWN/HIDDEN 事件**只在页定义了 open callback 时触发**;程序切页必须设**新页** `visible=true`(设旧页 invisible 无效);TABSET 不可嵌套;页内可再嵌普通 frame。
- frame 的 visible/active 施加于所有子 gadget 但**不覆盖子自身的属性值**(frame 隐藏时子 .visible 查询仍 true)。

## 5. gadget 通用操作(ch19)

- 通用成员 `type`/`name`(只读);方法 `subtype()`(frame 的 NORMAL/TABSET/FOLDUPPANEL…)、`container()`(上层 FMO)。
- **Pixmap**:`pixmap /路径 [宽 高]`(缺省 32×32);BUTTON/TOGGLE 可给两图(未选/选中):`button .B1 pixmap /a.png /b.png width 26 height 26`;改图用 `.addPixmap('未选.png','选中.png')`(第一参空串=保持选中图);取标准图标路径 `!!PML.getPathname('x.png')`;定义时尺寸要≥最大图;灰显自动,无需第三张图。paragraph 的 pixmap 走 `.val`。
- 置灰:`.active = FALSE`;整表单:`!f.setActive(false)`(只灰显,恢复时精确还原原状态)vs `!f.setGadgetsActive(false)`(强制全 inactive,原状态丢失)。
- 可见性:`.visible = FALSE`;焦点:`!!f.keyboardFocus = !!f.g` 或 `!g.setfocus()`(限 TEXT/TEXTPANE/BUTTON/TOGGLE/RTOGGLE/SLIDER/LIST/SELECTOR/OPTION/ALPHA)。
- **刷新**:**回调内对 gadget 的修改延迟到回调结束才上屏**;要立即生效 `!g.refresh()`;`REFRESH` 命令刷全部表单;**交互 do 循环中删除元素后必须 REFRESH**(否则宏失败,官方示例用 `id slab@` + `handle (61,528)` 捕 ESC + `delete` + `refresh`);刷新省着用(尤其视图)。
- 背景:`.background('colourname')` / `.Background = 色号`(0=恢复缺省);部分 gadget(如带 pixmap)不支持。

## 6. 各 gadget 要义(ch20)

**paragraph**:无 tag 无 callback(被动);文本/像素图**定义后不可互换**;**尺寸定义后不可变**;无初始文本就必须给初始尺寸(width+height 或 lines);多行自动换行。

**button**:
```pml
button .SubForm 'More...' FORM !!ChildForm        -- 弹子表单(Dtext 惯例以 ... 结尾)
button .calc 'Calculate' CALLBACK '!this.calc()'
button .B1 TOGGLE pixmap /off.png /on.png width 16 height 16   -- toggle 模式按钮,.val 为 BOOLEAN
button .Dismiss 'Dismiss' CANCEL                  -- DISMISS = 无回调的 CANCEL
```
控制属性:`OK / APPLY / CANCEL / RESET / HELP`——每类每表单**只能一个(APPLY 可多个)**;有 APPLY 就应配 DISMISS;**OK 按钮自身的 callback 被忽略**;RESET 把 gadget 恢复到显示时/上次 APPLY 的值**然后执行回调**(供你撤销副作用)。LINKLABEL 子类型:无边框链接样式,无控制属性、不支持改背景、无按压态,按下会触发表单文本校验。

**toggle / rtoggle**:toggle 的 tag 显示在按钮**右侧**,`.val` BOOLEAN 缺省 FALSE;rtoggle 只准在 frame 内,`States '' '值'` 定义 onValue。

**option / combo**:文本型 **width 必给**;选项=赋 Dtext 数组(Rtext 可选,缺省=Dtext);`!opt.dtext = !arr`、`select('Dtext', 'Orange')`、`selection()`(回 Rtext)/`selection('dtext')`、`.val`=索引、`clear()` 清双列表、`Add(dtext[,rtext])` 追加单项;显示框可用左右键滚动(可窄于下拉项)。像素图型必须 `WIDTH` + `HEIGHT` 或 `ASPECT`,Dtext 填 png 路径。combo 显示框**缺省可编辑**,输入+回车触发 VALIDATE 事件(**须 open callback 才能与 SELECT/UNSELECT 区分**,用 `.displayText` 取输入);combo 不支持 pixmap。

**slider**:`slider .s vertical range -50 +50 step 5 val -2 height 5`;事件 START/MOVE/STOP(建议 open callback);**MOVE 后系统不自动刷新**,联动显示要 `!g.refresh()`。

**line**:`line .h 'H' Horiz width.f3 height.t1` 分隔线;tag 永不显示、不进 toolbar、无值。

**numericinput**:`val` REAL / `range` REAL 数组[start,end,step] / `ndp`(只读小数位) / `editable` / `modified`(MODIFIED 事件开关,缺省关) / `setRange(!range,!ndp)`;SELECT=回车确认;MODIFIED=每次上下箭头步进(须 open callback 区分)。

**list**(最复杂的交互件):
```pml
list .l '标题' MULTIPLE width 15 height 8        -- SINGLE/MULTIPLE 和 width+height(length) 必给
!this.l.dtext = !arr                             -- Dtext 必给;Rtext 可选(缺省=Dtext,常放回调串)
```
- 单选:`.val`=索引;`select('Dtext',v)` / `select('Rtext',v)`;`selection()` 回 Rtext、`selection('Dtext')` 回显示文本;`zerosel`(允许全不选,可点空行取消)、`noReselect`(重击已选项不发事件)。
- 多选:`selection()` 回选中 Rtext 数组、`.val` 回索引数组;**扩展选择模式(CTRL/SHIFT)下一次操作会产生整批 UNSELECT 再整批 SELECT**,START/STOP 批事件只有 open callback 才收到——**列表内容/选择的程序性修改只能放在 STOP 分支**(回调中改列表有崩溃风险,官方明言);新代码多选一律 open callback。
- 重赋 `.dtext` 会**连 Rtext 带选择一起清掉**;只换 Rtext(同长)不影响 Dtext 与选择。
- 多列:`SetHeadings(!heads)` / `SetRows(!rows)`(行数组的数组)/`SetColumns(!cols)`;每行 Dtext 是**制表符分隔串**;`select(!col, dtext)` 按列选行;多列上右键会先选中该行再弹菜单。

**selector(数据库选择器)**:`DATABASE` 关键字**必须**;可选 `OWNERS`(只显示上方)/`MEMBERS`(只显示下方)/`AUTO`(随 CE 变化自动刷新;**AUTO 与 MULTIPLE 不可同用**);`selection()` 直接得元素;selector 的 Dtext 与 Rtext 恒相同。

**text**:**WIDTH 必给、IS 类型必给**;`scroll n`(可容纳字符数,缺省 132,最大 256);`NOECHO` 显示星号(密码);`is BORE format !!fmt` 等带 FORMAT 对象控制显示与解释;回调在 Enter 时触发;长度类配合 FORMAT 对象与 mm/inch 换算(官方范式见生成规范 §11.5)。

**textpane**:值=字符串数组(一行一元素):`.val = !lines` / `.count` / `.setline(21,'txt')` / `.line(21)` / `.setcurpos(行,列)` / `.curpos()` / `.seteditable(false)` / `.clear()`;`FixChars` 关键字强制等宽字体(Courier New)——空格对齐报表的唯一正确姿势。

**快速遍历**(选择项/行多时比 selection() 快):
```pml
do !f list !!form.l          -- 逐个选中项(取 Rtext)
do !s selector !!form.sel    -- 逐个选中行(显示值)
do !t pane !!form.pane       -- 逐行
enddo                        -- 退出后 do 变量被销毁
```

**view**(图形/文本视图):`view .v AT ... ALPHA|PLOT|AREA|VOLUME height 20 width 40 ... exit`(或单行无 exit);属性建议在构造器里设而不是定义里;不支持 anchor/dock——放独立 frame。
- ALPHA(文本/命令窗):`channel COMMANDS` / `channel REQUESTS`;`.clear()` 清输出;`.removeRequests()` 移除请求通道(**表单已显示后才可调,定义期报 (61,605)**;恢复:`.channel = 'Requests'`);支持双击复制行、粘贴为宏执行、拖入 .pml 文件直接执行。
- PLOT(非交互 2D 图):`.add('plot文件')` / `.clear()`;`borders=false` 后固定不可缩放(当装饰用)。
- AREA(2D 图页):`put /SITE1/SHEET` 定内容、`limits x1 y1 x2 y2` 定窗口;**没有 .put() 方法**——换内容用旧命令 `edit view !!form.gadget AREA put /site/sheet2`。
- VOLUME(3D):`limits auto|local [brick]`(brick=REAL 数组 [E1,E2,N1,N2,U1,U2]);`.direction` 三元方向数组 / `.through` 三元穿视点 / `.radius(r)` / `.range(r)` / `.projection('PERSPECTIVE')`(缺省 PARALLEL)/ `.shaded(true)` / `.walkthrough(true)+.step(s)` / `.mousemode` / `.bearing/.elevation` / `.labelStyle('ENU'|'XYZ')` / `.saveview(n)/.restoreview(n)`(n=1..4);旧语法 `edit view !!form.g VOLUME` + `LOOK/PLAN/ISOMETRIC/ELEVATION` 修饰符表。
- 光标:2D 视图可 `Cursor POINTER|PICK|CROSSHAIR...`(PLOT/CURSOR 缺省 CROSSHAIR;COMPARATOR POINTER;VOLUME 恒 POINTER 不可改)。

## 7. 与记忆文件 R17-R19 的差异提示

- R17/R18/R19 来自 E3D `layout form` 语境;本文件全部来自 PDMS 12 `setup form` 语境(Marine 实际所用)。冲突点示例:`layout form` 强制 VarChars,`setup form` **缺省 FixChars**(所以 Marine 旧表单要显式加 VarChars 或靠 FMSYS 全局切换);gadget 语法细节以本文件为准,拿不准时查 `Guide_ch15_20.txt` 原文页码。
