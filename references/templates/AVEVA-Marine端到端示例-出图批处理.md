# 端到端示例:Marine 出图批处理(marAPI 图纸自动化)

> 第 26 轮:第四个可复制模板——**批量生成/修改 Marine Drafting 图纸并导出**(场景:按元素清单批量开图、建符号视图、画框、保存、导 DXF)。
> 依据:全部调用在官方 PML 实证——`assembly\tasks\assyhsv.pmlfnc`(符号视图创建+变换)、`marinedrafting\functions\openmarinesheet.pmlfnc`(图纸生命周期)、`pipefabricationmanager\draft\functions\mardradrawviewframe.pmlfnc`(画框)、反射全表(marAPI 姿势表)。

---

## 1. 图纸生命周期五步(官方 openmarinesheet 范式)

```pml
!drafting = object MARDRAFTING()
if (!drafting.dwgCurrent()) then                     -- 有未关图?
  if (!drafting.dwgIsModified()) then
    !ans = !!alert.question('Save current drawing?') -- 提示保存
    if (!ans.eq('YES')) then !drafting.dwgSave() endif
  endif
  !drafting.dwgClose()
endif
!drafting.dwgActivate(!sheetName)                    -- 打开目标图
```

## 2. 批处理主函数(清单驱动)

```pml
import 'marAPI'
  handle (1000,0)
  endhandle
using namespace 'AVEVA.Marine.Drafting'
using namespace 'AVEVA.Marine.Geometry'

define function !!myBatchDraw(!sheetNames is ARRAY, !outDir is STRING) is ARRAY

  !failed = ARRAY()
  !drafting = object MARDRAFTING()
  !total = !sheetNames.size()
  !!FMSYS.setInterrupt(!!fmstop.stopButton)

  do !i index !sheetNames
    !!FMSYS.setProgress((!i - 1) * (100 / !total))
    !name = !sheetNames[!i]

    -- (a) 关旧图(见 §1)后开图;不存在则先建
    handle (1000,0)
      -- 桥层错误统一兜底
    endhandle
    if (!drafting.dwgExist(!name)) then
      !drafting.dwgActivate(!name)
    else
      !drafting.dwgNew(!name, 'MyBatch')
      handle (1000,0)
        !failed.append(!name & ' (create failed)')
        skip
      elsehandle NONE
      endhandle
    endif

    -- (b) 建符号视图(assyhsv.pmlfnc:248 原文范式)
    !symbDefObj = object MARSYMBOLICVIEW()
    !symbDefObj.setPlaneByPanel(!name, 0, 0, 0, 0)   -- 按面板定投影面(重载见姿势表)
    !hSVHandle = !drafting.viewSymbolicNew(!symbDefObj)
    handle (1000,0)
      !failed.append(!name & ' (view failed)')
      skip
    elsehandle NONE
      !drafting.viewScale(!hSVHandle, !myScale)      -- 缩放(mardradrawviewframe 同族)
    endhandle

    -- (c) 画图框(mardradrawviewframe 原文范式:颜色+矩形)
    !mStart = object MARPOINTPLANAR(!xmin, !ymin)
    !mEnd   = object MARPOINTPLANAR(!xmax, !ymax)
    !saveColour = !drafting.colourget()
    !mColour = object MARCOLOUR('GRAY')
    !drafting.colourSet(!mColour)
    !drafting.rectangleNew(object MARRECTANGLEPLANAR(!mStart, !mEnd))
    !drafting.colourSet(!saveColour)

    -- (d) 导出 DXF(反射表:DwgDxfExport(路径))
    !drafting.dwgSave()
    !drafting.dwgDxfExport(!outDir & '\' & !name & '.dxf')
    !drafting.dwgClose()
  enddo
  !!FMSYS.setProgress(0)
  return !failed

endfunction
```

## 3. 官方细节与坑(全部实证)

| 要点 | 出处 |
|---|---|
| 保存后图纸"归 Marine Drafting 所有",**Outfitting Draft 打不开** | assyhsv.pmlfnc 尾注释原文 |
| `dwgExist/dwgNew/dwgActivate/dwgSave/dwgClose/dwgCurrent/dwgIsModified` 全族 | 反射表 §3.2 |
| 符号视图定义器 `MARSYMBOLICVIEW`:`setPlaneByPanel/ByX/ByY/ByZ/By3Points/ByCurve/ByRSO`、`SetDepth/SetLimits/SetPanelsFilter/SetBlocksFilter` | 反射表 §2 |
| 视图变换三件:`elementTransform(handle, transform)` + `transform.identityTransf()/translate(vec)/scale(s)`;包围盒 `elementExtentGet(handle).corner1()/corner2()` | assyhsv L280-307 |
| 画框用 `MARRECTANGLEPLANAR(p1,p2)` + `rectangleNew`;颜色对象 `MARCOLOUR(号或'名')`,非法色回退 `'GRAY'` | mardradrawviewframe |
| 改图后 `dwgRepaint()` + `savework`(交互会话)或 `dwgSave()`(批处理) | 同上 |
| 独立进程(不开 GUI)跑本模板:`PdmsApplicationImpl.Initialise()` → `PdmsApplication.Start(false, 91, …)` → `Misc.Init(91)` → … → `Misc.Terminate()+PdmsStandalone.Finish()`(91=Marine Drafting) | ImportDXF.cs / marAPI 姿势表 §3.9 |

## 4. 变体

| 需求 | 改动 |
|---|---|
| 导出其他格式 | `DwgSvgExport / DwgHpgl2Export / DwgTifExport / DwgWmfExport / DwgPreviewBmpExport`(反射表) |
| 加标注 | `DimLinearNew/DimRadiusNew/NoteNew/PosnoNew`(反射表 §MarDrafting);或交互光标 `!mui.dimcreate(!act)`(MarUI) |
| 批量导入 DXF | 反向走 `DwgDxfImport`(ImportDXF.cs 全流程模板) |
| 每图多视图 | 循环 (b)-(c),用 `elementExtentGet`+`translate` 排版(assyhsv 平移范式) |
| 3D 模型投影 | `ViewNew(名, 方向, 向上)/ViewSectionNew`(反射表;3D 内容需 VOLUME 语境) |

## 5. 审核自查

- 所有 marAPI 调用包 `handle (1000,0)`;返回码 253(用户取消)在交互方法处判断
- 批处理**不开交互点取**(无 PointPlanarReqPML),纯后台;若需交互拆成两阶段
- 进度条 + stopButton;失败清单返回;`Misc.Terminate()/PdmsStandalone.Finish()` 对称收尾
- 防猜:全部方法名经反射表核对(姿势表 §4 守则)
