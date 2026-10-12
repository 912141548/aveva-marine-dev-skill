# 端到端示例:Outfitting 元素收集导出工具(从零到部署)

> 第 22 轮:把前 21 轮知识串成**可复制模板**。需求:在 Outfitting 中收集当前 CE 下全部 EQUI,表格展示,一键导出 Excel,并挂到界面入口。
> 每步标注依据(→ 指向工作区文档);代码符合三份规范全部规则(命名前缀 my、PML2、handle、错误处理)。

---

## Step 1 方案选型(→ NET 技能文档 §1 三轨定位)

需求 = 表格 + 导出 + 收集,无停靠窗/命令状态需求 → **纯 PML 方案最短路径**(PML 表单 + NetGridControl 控件嵌入 + 公共库 exportToExcel),不需要写 C#。
依据:官方同构范式 `aba\forms\abaarea.pmlfrm`(容器嵌网格)/`common\functions\exporttoexcel.pmlfnc`(115 处调用的公共函数)。

## Step 2 目录与文件(→ PML 技能文档 §5.1 平行目录铁律)

```
C:\mydev\pmllib\myco\forms\mycollect.pmlfrm     ← 表单(唯一必需文件)
C:\mydev\pmllib\myco\icons\mycollect16.png      ← 图标(可选)
```
命名:模块 `myco`(自定前缀防冲突,记忆 R15)、表单 `!!mycollect`(小写文件名=定义名)。

## Step 3 表单代码(→ 表单语法精要 §1/§5;PML 技能 §4.3;任务写法速查 §2/§5)

```pml
--========================================================================
-- File:      mycollect.pmlfrm   Type: Form Definition   Module: myco
-- Description: Collect EQUIs under CE, show in grid, export to Excel
--========================================================================
import 'GridControl'
  handle (1000,0)
    -- already imported - ignore
  endhandle

setup form !!mycollect dialog resizeable VarChars NoAlign
  title 'My EQUI Collector'
  !this.formRevision = '1.0'

  member .grid     is NETGRIDCONTROL
  member .rows     is ARRAY

  path down
  text .scope 'Scope(空=当前CE)' width 22 is STRING
  frame .fmeBtns 'Actions'
    path right
    button .btnGo    'Collect'   callback '!this.collect()'   tooltip 'Collect EQUIs'
    button .btnXls   'Export...' callback '!this.export()'    tooltip 'Save grid to Excel'
    button .btnClose 'Close'     CANCEL
  exit
  container .netFrame 'Grid' nobox pmlNetControl width 60 height 16 anchor all
exit

define method .mycollect()
  !this.initcall = '!this.onShow()'
endmethod

define method .onShow()
  -- 构造 .NET 控件并挂入容器(范式:abaarea.pmlfrm)
  !this.grid = object NETGRIDCONTROL()
  !this.netFrame.control = !this.grid.handle()
  -- 表头与数据收集
  !this.collect()
endmethod

define method .collect()
  !this.rows = ARRAY()
  !heads = ARRAY()
  !heads[1] = 'Name'
  !heads[2] = 'Description'
  !heads[3] = 'Type'
  -- 收集:CE 下全部 EQUI(防猜:COLLECTION 三段式,规范 §8.2)
  !coll = object COLLECTION()
  !coll.type(|EQUI|)
  !scope = !this.scope.val
  if (!scope.empty()) then
    !coll.scope(!!ce)
  else
    !target = object DBREF(!scope)
    handle (2,109)                        -- 元素/引用不存在(错误码速查)
      !!alert.error('Scope element not found: ' & !scope)
      return
    elsehandle NONE
    endhandle
    !coll.scope(!target)
  endif
  !results = !coll.results()
  if (!results.size() gt 0) then
    do !e index !results
      !row = ARRAY()
      !row[1] = !results[!e].flnn
      !row[2] = !results[!e].desc
      !row[3] = !results[!e].type.string()
      !this.rows.append(!row)
    enddo
  else
    !!alert.warning('No EQUI found under the scope.')
  endif
  -- 绑定(NetDataSource 行数组构造:不自动取库值)
  !ds = object NETDATASOURCE('MyCollect', !heads, !this.rows)
  handle (1000,0)
    !!alert.error(!!error.text)
    return
  endhandle
  !this.grid.bindToDataSource(!ds)
  !this.grid.setNameColumnImage()
endmethod

define method .export()
  -- 复用官方公共函数(115 处调用):弹保存框+写 Excel
  !!exportToExcel(!this.grid, ||, |Save EQUI List|)
endmethod
-- End of form definition for !!mycollect
```

要点核对(全部有据):`handle (1000,0)` 吞重复 import 与桥错(mDraPickElement 范式);`VarChars NoAlign`(表单语法精要 §1);`anchor all` 让容器随窗缩放;`do !e index`(带下标);`.size() gt 0` 空集合防护(审核 B2);DBREF 构造包 handle (2,109)(错误码速查)。

## Step 4 部署(→ PML 技能 §5.2)

```bat
rem 用户 evars 前置(方式 A)
Set PMLLIB=C:\mydev\pmllib %pmllib%
```
验证链:`q evar pmllib`(顺序)→ `pml rehash all` → **等 10 秒** → `show !!mycollect` → 逐按钮冒烟。

## Step 5 界面入口(两条路线,→ PML 技能 §3.4 / NET 技能 §4)

**路线 A(纯 PML,推荐本例)**:ADDIN 文件 + addin 对象
```
%PDMSUI%\DES\DFLTS\ADDINS\MYCOLLECT :
Name: MYCOLLECT
Object: APPMYCOLLECT
```
PMLLIB 里 `define object APPMYCOLLECT` + `.modifyMenus()`:
```pml
define method .modifyMenus()
  !menu = object APPMENU('sysUtil')             -- 挂到 Utilities 菜单
  !menu.add('CALLBACK', 'My EQUI Collector...', 'show !!mycollect', 'myCollect')
  !!appMenuCntrl.addMenu(!menu, 'ALL')
endmethod
```
(同名字段自动去重→多 addin 幂等;Dtext 以 ... 结尾=弹表单惯例。)

**路线 B(uic Macro 按钮)**:自研 C# addin 或直接在 uic 里加 `<Type>Macro</Type><Macro>show !!mycollect</Macro>` 的 ButtonTool(uic 手册 §1.3 形态④)——**不写 C# 也能挂按钮**。

## Step 6 升级到 .NET addin(需要停靠窗/状态时,→ Cookbook §10/§12)

停靠窗版 = AttributeBrowserAddin 范式:`CreateDockedWindow(key, title, control, DockedPosition.Right)` + `SaveLayout=true` + StateButtonTool↔Checked 同步;部署三步(DLL→exe 目录、Addins.xml 登记、重启);uic 的 `CommandId` 必须等于 Command `Key`。

## Step 7 审核自查(→ 审核规范 A→B→C→D)

- A 类机器扫:预处理三步后过正则(第 14 轮修订 A1-A2 已知豁免)
- 防猜:本例用到的 NETGRIDCONTROL/NETDATASOURCE/exportToExcel/COLLECTION 全部在语料库有官方出处(OBJ-01 ✅)
- C 类实测:空 CE、错误 scope、重复 collect、Export 取消四条边界
- 回调核对:`collect/export/onShow` 三个方法都在(可用 `_validate_callbacks.py` 思路)

> **第 35 轮实测**:本表单全文已落盘为 `PML语料\audit_test\mycollect.pmlfrm` 并通过 `pml_audit.py` 审计——**0 违规**(A 类 16 规则含 FRM-01 回调核对)。模板即合规,可放心抄。

## 变体速查

| 需求变化 | 改哪里 |
|---|---|
| 收集其他类型 | `.type(\|BRAN SCTN\|.split())` |
| 跨 World 收集 | `!coll.scope(object DBREF('\|/\|'))`(不设 scope=全 MDB,慎用) |
| 批量改属性 | 收集后循环 `!e.attr = v` + `MARKDB` 包裹(撤销) |
| 要停靠窗 | 升级 .NET addin(Step 6) |
| 要参数化报表 | PMLReport 通道(对象字典 §23) |
