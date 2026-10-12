# TTY 环境自检脚本(复制粘贴即可跑,验证知识库关键事实)

> 第 32 轮:把知识库中"需要真实环境确认"的事实,转成 PDMS 命令行(TTY)可执行的验证序列。
> 用法:启动 Outfitting/Design → 显示命令行(Display > Command Line)→ 分段粘贴;每段附"预期结果",不符即记录反馈。

---

## 1. 环境与装载

```pml
q evar pmllib
-- 预期:自定义路径在最前(C:\mydev\pmllib ...)
q var !!PML.getpathname('mycollect.pmlfnc')
-- 预期:返回模板①文件的实际路径
pml rehash all
-- 等 10 秒(自动化场景必须)
q var !!pml
-- 预期:!!PML 全局对象成员清单
```

## 2. 模板①/③ 冒烟

```pml
show !!mycollect
-- 预期:表单弹出,网格已绑定当前 CE 下 EQUI
-- 边界:CE 在 /* 时 Collect;Scope 输入不存在名 → 应弹 'Scope element not found'
!!myBatchDesc(ARRAY(), 'x')
-- 预期:弹 'Nothing to update.'(空集合防护)
```

## 3. 撤销栈验证(MARKDB/UNDOABLE 是否生效)

```pml
MARKDB 'my test mark'
NEW EQUI /MYTESTBOX
-- 命令行执行 UNDODB
-- 预期:MYTESTBOX 消失;REDODB 后恢复
```

## 4. IFTRUE 存在性(已由语料实证,TTY 复核)

```pml
-- 语料实证:IFTRUE 仅用于 Static Rule 表达式(asl\objects\aslstrlngdata.pmlobj
-- 的 'rule set pos Static Rule ( W ( IFTRUE ( ATTRIB INTSEN OF STRTWR, 1, -1 ) ...))')
-- TTY 验证 PML2 表达式中是否可用:
!x = IFTRUE(FALSE, 1, 2)
-- 预期 A:报语法错 → IFTRUE 仅规则语境(与规范分工一致)
-- 预期 B:返回 2 → PML2 亦可用(注意双分支都求值)
q var !!ce
-- 若 CE 是 STRTWR 相关元素,可在命令行直接跑一条 IFTRUE 规则验证求值方向
```

## 5. marAPI / PMLNet 桥

```pml
import 'marapi'
  handle (1000,0)
  endhandle
using namespace 'AVEVA.Marine.UI'
!ui = object MARUI()
q var !ui
-- 预期:<Aveva.Marine.UI.MarUi> 对象存在(桥可用)
q methods !ui
-- 预期:列出 PointPlanarReqPML/DimCreate 等全部方法(防猜终审)
```

## 6. 错误码实测(校准错误码速查)

```pml
!f = object FILE('C:/definitely_not_exists_123.txt')
!f.open('READ')
-- 预期报错头含 (160,9) → 佐证模块 160=FILE
!x = 'abc' + 1
-- 预期:(46,x) 类类型错误 → 佐证 46=PML 解释器
q var !undefinedVariable123
-- 预期:(46,28) Variable not defined
```

## 7. EDG 拾取(模板③ 交互变体前置)

```pml
!packet = object EDGPACKET()
!packet.elementPick('Pick any element <esc> to finish')
!packet.action = '!!mycollect.collect()'
!!edgCntrl.add(!packet)
-- 预期:光标变拾取态;点元素后 collect 触发;ESC 结束
-- 若表单内 VOLUME 视图拾取失败 → 需先 !!edgCntrl.addView(该视图)
```

## 8. 模块号归属考证(第 87 轮大部关闭:17/33/39/62 已确认,见错误码速查 §5;余项仅需 TTY 复核)

```pml
-- 依次触发并记录报错头,复核剩余高号段(41/42/43/44/73/83 的官方模块名):
new EQUI /XNONAME1
new EQUI /XNONAME1
-- 第二次必撞 (41,12)/(2,x) 名称冲突 → 记录实际模块号
$P $!undefined
-- 记录展开类错误的模块号
-- 卷三/六/九已实证域化语义(如 (44,15) PDF 已存在、(83,x) Spooler 编号网、(62,707) Router 约束),
-- TTY 只需确认官方模块名(如 44 是否 OUTPUT/FILE 域),回填《Marine-PML错误码速查.md》§1 即全部关闭
```

## 9. 回归清单(每次 SP 升级后跑一遍)

- [ ] §1 装载三项
- [ ] §2 模板①两例
- [ ] §5 桥两例
- [ ] §6 错误码三例(160/46 模块)
- [ ] addin 三件套(DLL/uic/Addins.xml)加载 + 按钮冒烟(→ uic 手册清单)
