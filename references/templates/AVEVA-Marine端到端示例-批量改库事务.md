# 端到端示例:批量改库 + 撤销事务(官方三层防护范式)

> 第 24-25 轮:第三个可复制模板——**安全地批量修改数据库元素**(场景:批量改 N 个元素的属性,如隔离等级/描述/保温规格),带用户可撤销、进度条、逐项错误隔离。
> 依据:官方原文实证——`design\forms\selectSpecification.pmlfrm:821-839`(MARKDB 批量范式)、`common\forms\pos3dexplicit.pmlfrm:183-188`(UNDOABLE 全套)、`mds` DAC 体系(3573 次调用)、Guide ch22(FMSYS 进度)、错误码速查。

---

## 1. 官方三层防护模型(先懂再抄)

| 层 | 机制 | 出处 |
|---|---|---|
| **撤销层** | `MARKDB`(命令级,回到标记)或 `UNDOABLE` 对象(回调级,可挂按钮) | selectSpecification / pos3dexplicit / TM-1401 ch10 |
| **权限层** | 写前申请所有权:轻量场景 `!!ce.claim()`,mds 体系 `!!mdsDacControl(TRUE→FALSE)` | hullNewBlock / MdsComClaimDac(3573 次) |
| **错误隔离层** | 每项 DB 命令包 `handle (精确码) / elsehandle ANY` + 逐项计数,**单项失败不中断批次** | selectSpecification 循环内 `handle any` |

官方纪律:**整批只 `savework` 一次**(成功后);官方**不用 abortwork**(全库 0 次);失败项收集起来最后统一报告。

## 2. 完整模板代码(myco 批量改描述)

```pml
--========================================================================
-- File:      mybatchdesc.pmlfnc   Module: myco
-- Description: Batch update DESC on collected elements, undoable
--========================================================================
define function !!myBatchDesc(!elems is ARRAY, !newDesc is STRING) is ARRAY

  !failed = ARRAY()
  if (!elems.size() eq 0) then
    !!alert.warning('Nothing to update.')
    return !failed
  endif

  -- 撤销层:命令级标记(用户可 Ctrl+Z 回到标记点)
  MARKDB 'MyCo batch description update'

  -- 进度层:长批次防卡死(Guide ch22 范式)
  !!FMSYS.setInterrupt(!!fmstop.stopButton)     -- 停止按钮小表单,见 PML 技能 §3.7
  !increment = 100 / !elems.size()

  do !i index !elems
    !!ce = !elems[!i]                           -- 导航(实证范式:selectSpecification)
    handle (2,109)                              -- 元素已不存在(被他人删除)
      !failed.append(!elems[!i].ref.noquote())
      !!FMSYS.setProgress(!i * !increment)
      skip
    elsehandle (41,319)                         -- 权限不足
      !failed.append(!elems[!i].ref.noquote() & ' (no write access)')
      !!FMSYS.setProgress(!i * !increment)
      skip
    elsehandle NONE
      -- 逐项修改;对象成员两段式(POSITION 类属性必须取出改回,规范 R6)
      !!ce.desc = !newDesc
    elsehandle ANY
      !failed.append(!elems[!i].ref.noquote() & ' (error ' & !!error.text & ')')
    endhandle
    !!FMSYS.setProgress(!i * !increment)
  enddo
  !!FMSYS.setProgress(0)

  -- 结果反馈
  if (!failed.size() eq 0) then
    savework                                    -- 整批一次提交(官方纪律)
    !!alert.message(!elems.size().string() & ' elements updated.')
  else
    !!alert.warning(!failed.size().string() & ' of ' & !elems.size().string() &
                    ' failed. Changes to successful items are NOT saved yet.' )
    -- 官方语义:savework 前的修改都在工作区;让用户检查后手动 savework
    -- 或提供第二个函数执行 comSaveWork()(带确认,见公共库目录)
  endif
  return !failed

endfunction
-- End of function !!myBatchDesc
```

## 3. 回调级撤销(表单 Apply 按钮,官方原文范式)

```pml
-- 表单成员:member .undoApply is UNDOABLE
-- 构造器里(common\forms\pos3dexplicit.pmlfrm:183-188 原文范式):
  !this.undoApply.description('Apply Position Change')
  !this.undoApply.undoAction(|!!myBatch.undoEvent()|)
  !this.undoApply.redoAction(|!!myBatch.undoEvent()|)
  !this.apply.setUndoable(!this.undoApply)
```

要点:undo/redo 执行串是**字符串**(回调,写错点击时才炸——FRM-01 同源风险);官方常用**同一个恢复函数**做 undo/redo(执行时重读当前状态再恢复);全局通知可挂 `!!postEvents.postUndo(str)`(RefMan 2.5.52,对象字典 §13)。

## 4. 错误码速配(本场景,→ 错误码速查)

| 码 | 场景 | 处理建议 |
|---|---|---|
| (2,109) | 元素/引用不存在(中途被删) | skip + 记失败 |
| (41,319) | 无写权限(DAC/团队) | skip + 标注 |
| (41,12) | 建名冲突(若涉及 new) | skip + 标注 |
| (2,201) | 引用元素无位置(几何类修改) | skip |
| (61,528) | 用户按了停止按钮的交互退出 | 整批中止 |
| (1000,0) | 桥层错误(.NET 混合时) | 兜底 alert |

## 5. 变体

| 场景 | 改动点 |
|---|---|
| 涉及建名 | `new` 命令包 `handle (41,12)`;名字先 `!x.checkName()` 思路(公共库 namegadget) |
| 几何位置类修改 | 属性对象两段式:`!p = !!ce.pos` → `!p.up = v` → `!!ce.pos = !p`(规范 R6) |
| mds 体系元素 | 循环外包 `!!mdsDacControl(TRUE)` … 成功 savework 后 `(FALSE)` |
| marAPI 改图 | `stmtExec` 循环 + `dwgRepaint()` + 一次 `savework`(mardradrawviewframe 范式) |
| .NET addin 里批量 | 同逻辑走 `DbElement.SetAttribute` 循环;**注意 DbPostElementChange 每次改动都会回调**(防重入:Collections 改动时先解除订阅或加标志位) |
| 要让用户能撤销到项级 | 每项一个 UNDOABLE 对象(开销大,官方实践是**整批一个标记**) |

## 6. 审核自查

- 每项 DB 命令都有 handle(ERR-01 ✅);失败项有记录(ERR-02 静默 ✅)
- 开放循环无(用 index 循环,天然有上界;CTL-06 ✅)
- 单位无关(描述文本);若改尺寸类属性,套 `!!isImperialLength` 分支(任务写法速查 §6)
- 放行前跑 `_validate_callbacks.py` 思路核对表单回调
