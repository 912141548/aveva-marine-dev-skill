# AVEVA Marine Draft 出图操作命令大全（穷举版）

> 来源：子 agent 深读 PMLLIB draft/assembly/spooler + PDMSUI DRA 全树，逐文件提取全部出图命令。
> 日期：2026-09-26

---

## 一、图纸创建（DRWG → SHEET → VIEW → LAYER 全属性链）

### 完整模板构建（pipetappingdrwg.pmlobj:1800-2167）

```
-- 定位到 DRW 注册表
/DRA/PRJ/REPR/GEN/PIPE

-- 创建 REGISTRY（全局样式容器）
NEW REGISTRY /TEMP-REGI
  SIZE 1189mm 841mm
  UCOD mm  Distance  mm  Bore Nominal
  FONT 5
  DTER Arrows
  LTER Off
  PCODE mms to 0 dpls  Inches to 1 dpls  Fractions to 32 ths  Angles to 1 dpls
  TXCOLO 1
  NLSTYL Solid
  NLCOLO 1
  LLSTYL Solid
  LLCOLO 1
  LFSTYL Solid
  LFCOLO 1
  DLSTYL Solid
  DLCOLO 1
  PLSTYL Solid
  PLCOLO 1
  FSTYLE Off
  FCOLOUR 1
  POSFOR ENU

-- 创建 DRWG（图纸）
NEW DRWG /DETAIL/TEMP
  DATE '5  Apr 2013'
  SIZE 120mm 60mm
  FONT 1
  UCOD mm  Distance  mm  Bore Nominal
  DTER Arrows
  TITL 'Detail Plot View'
  AUTH 'chris.whiteley'
  TXCOLO 1
  POSFOR ENU

-- 创建 SHEET（图页）
NEW SHEET /DETAIL/TEMP/S1
  SIZE 120mm 60mm
  TITL 'Piping Drawing'
  POSFOR ENU

-- 创建 VIEW（视图）
NEW VIEW /DETAIL/TEMP/S1/V1
  DIR D
  VSCA 0.05
  VTYP Universal HLine
  SIZE 60mm 60mm
  XYPS X 30mm Y 30mm
  LFRA true
  POSFOR ENU

-- 创建 LAYER（尺寸标注层，全属性）
NEW LAYER /DETAIL/TEMP/S1/V1/USER_dims
  PURP DIMA
  UCOD mm  Distance  mm  Bore Nominal
  FONT 11
  DTER Arrows
  TSIZ 3mm
  DOFF 25mm
  CHEI 3mm
  LLEA true
  LFRA true
  TXCOLO 10
  NLSTYL Solid
  NLCOLO 1
  POSFOR ENU
END

-- 创建符号库
NEW LIBY /DETAIL/TEMP/LIBY
  NEW PLLB
  NEW DLLB
    NEW IDLIST
      NEW ADDENTRY
  NEW TRLB
END
END

-- 挂接 IDLN
OLD DRWG /DETAIL/TEMP
  IDLN IDLIST 1 of DLLB 1 of LIBY /DETAIL/TEMP/LIBY
  RRSF RRST /DRA/PRJ/REPR/GEN/PIPE
```

### 带 PML 变量的创建（DEPT→REGI→DRWG）

```pml
new DEPT $!this.deptName
handle ANY ... endhandle
!dept = !!ce

!!ce = !dept
new REGI $!this.regiName
handle ANY ... endhandle

!!ce = !regi
new DRWG $!dwgName
handle any ... endhandle

-- 跨 REGI 移动已有 DRWG
include $!dwg
handle ANY
  !!ce = !regi
  new DRWG
  handle ANY ... endhandle
  !deleteDwg = !dwg
  !dwg = !!ce
  !!ce = !deleteDwg
  delete DRWG
  !dwg.name = !dwgName
endhandle

-- 模板复制
copy $!this.dwgTmplName rename $!this.dwgTmplName $!dwgName
```

### SHEET 模板复制式创建
```pml
NEW SHEE $!sheeName
  handle (41,52)          $* 引用非法类型
  elsehandle (41,12)      $* 名称已占用
    DELETE SHEE
    !!ce = !sheeName.dbref()
    DELETE SHEE MEM
  endhandle
BSRF UNSET
COPY LIKE $!shtmplRefe BSRF UNSET
LINKREF $!shtmplRefe
SPPURP ASYADP
IDLN $!idliRefe
WARNINGS OFF
POSFORMAT NUMBER
FUNC '$!funcString'
```

---

## 二、VIEW 视图操作

### 创建
```pml
NEW VIEW $!viewName IDLN =0
SIZE $!size
XYPO $!position
SPPURP PARTVW
```

### 属性设置
```pml
DIR $!direction                      $* 方向
VSCA $!scale                          $* 比例
VTYP $!viewType                       $* 类型(Universal HLine等)
SIZE $!xSize $!ySize                 $* 尺寸
XYPO $!xPos $!yPos                   $* 位置
LFRA $!frame                          $* 框架显隐
LVIS $!visible                        $* 可见性
ADEG $!angle                          $* 旋转角度
TITLE |$!title|                      $* 标题
POSFORMAT XYZ|ENU                    $* 坐标格式
SPPURP $!purpose                     $* 用途
IDLN $!idliRefe                      $* ID 列表
AUTO                                  $* 自动比例
NOCLIPVIEW = TRUE                    $* (PML直赋) 不裁剪
```

### 复制视图
```pml
new view $!v2Name copy prev rename $!v1Name $!v2Name
adeg 0
by x 60mm
```

### 元素添加到视图
```pml
DESADD $!element
DESADD CE
DESADD CE COLOUR RED
```

---

## 三、尺寸标注命令

### LDIM（线性标注）— 15 种样式

```pml
$* 基础模板
NEW LDIM DTANG $!!CDLDTANG PTANG $!!CDLPTANG

$* 样式 1: DIR + LCHAIN TRUE
NEW LDIM DTANG ... PTANG ...
DIR $!dirVal
LCHAIN TRUE

$* 样式 3: DIR + PLDIR -90 + LCHAIN FALSE
DIR $!dirVal
PLDIR -90
LCHAIN FALSE

$* 样式 4: 英制截断
DIR $!dirVal
LCHAIN FALSE
TRUNCATE $!!CDDIMTRUNC.IMP

$* PML2 程序内创建（管段图）
NEW LDIM DTAN PARA
DIR $!currDir
handle any
  DELETE LDIM
elsehandle none
  FROM P$!first OF $!firstElement
  TO P$!second OF $!secondElement
endhandle

$* Ppoint 定位式
new ldim from pa of $!component to $!connectedBy of $!branchElement
direction $!componentArriveDirection
handle any
  ldim
  delete ldim
elsehandle none
  dpos X$!maxX Y$!maxY
  sort dim
endhandle
```

### ADIM（角度标注）
```pml
NEW ADIM DTANG $!!CDADTANG PTANG $!!CDAPTANG
SENSE CLOCKWISE|ANTICLOCKWISE
```

### RDIM/DDIM（半径/直径标注）— 6 种样式
```pml
$* DDIM（直径）样式1: DIMLINE
NEW RDIM DFLAG DIAM DDEG 45 ON $!from @ DTANG $!tang
DSTYLE DIMLINE
DTFLAG MID
DTUL OFF
DTRAD 0
DTOF 0 0

$* RDIM（半径）样式2: LEAD 引出线
NEW RDIM DFLAG RAD DDEG 45 ON $!from @
DSTYLE LEAD
DTFLAG CIRC
DTUL ON
DTRAD $!RAD
DTOF 0 0
```

### PDIM（螺栓圆 PCD）
```pml
NEW PDIM DFLAG DIAM PCEN $!from @ PCIRC $!to @
DDEG TRUE
```

### DPPT / APPT / DPOI（尺寸点定义）
```pml
NEW DPPT
DDNAME $!component
NPPT $!pPointNumber

NEW APPT
DDNAME $!component
PPDI $!position

NEW DPOI
POS $!point
```

### 标注修改
```pml
DPOS $!x $!y                          $* 标注位置
DTOFF $!x $!y                         $* 标注偏移
DMTX |$!text|                         $* 标注文本
DIR $!dir                             $* 标注方向
length $!newLength                    $* 长度
```

---

## 四、文本/标签命令

### TEXP（文本）
```pml
NEW TEXP at @                         $* 交互定位
JUST $!just                           $* LEFT|RIGHT|CENTRE
ALIGN $!align                         $* TBODY|Base|BB|TB
BTEX '$!text'                         $* 文本内容
CHEI $!height                         $* 字符高度
TXCOLOUR $!colour                     $* 颜色
ADEG $!angle                          $* 旋转角
FONT $!font
```

### VNOTE（竖排注释）
```pml
NEW VNOTE
XYPS X 30mm Y 30mm
JUST Left
ALIGN Bbody
FONT 1
BLNK false
CHEI 3mm
TXCOLO 1
MSTYLE Stop Scale 1
```

### NOTE（注释）
```pml
NEW NOTE
$* 复制式
new note $!newNote copy $!sourceNote ren $!sourceNote $!newNote
```

### GLAB（全局标签）
```pml
NEW GLAB ON $!ref BTEX |$!text|
CPOFFSET 0 -1.25
```

### SLAB（符号标签）
```pml
NEW SLAB ON $!component ATEX |$!mtoTag|
POS $!position
TMRF $!symbol
XYPO $!offset
OSET TRUE
TXCOLOUR $!colour
LFCOLOUR $!fColour
LFSTYLE $!fStyle
LLCOLOUR $!penColour
LLSTYLE $!style
BLNK TRUE
CPOF 0 0
LLEA TRUE
```

---

## 五、2D 图形元素

### 直线（STRA）
```pml
NEW STRA DEF @                        $* 两点交互
NEW STRA                              $* 续画
TPT @                                 $* 下一点
PURP $!purpose
CALLEDR XSETATTS                      $* 样式级联
```

### 圆（CIRC）
```pml
NEW CIRC DEF @                        $* 圆心+半径
NEW CIRC DIAM @                       $* 直径两点
```

### 弧（ARC）
```pml
NEW ARC DEF @                         $* 三点弧
NEW ARC ADEF @                        $* 圆心+半径+角度
NEW ARC TCODE CENTRE                  $* 圆角模式
FILLETRADIUS $!radius BETWEEN $!l1 AND $!l2
```

### 轮廓（OUTL）
```pml
NEW OUTL
NEW VRTX BULGE $!bulge DEF @          $* 带鼓度顶点
SPAN TO CLOSE                         $* 封闭
```

### 矩形（RECT）
```pml
NEW RECT
XYPOS x $!x y $!y
XLEN $!xlen
YLEN $!ylen
```

### 其他
```pml
NEW ELLI DEF @                        $* 椭圆(三点)
NEW DMND DEF @                        $* 菱形
NEW HEXA DEF @                        $* 六边形
NEW TABLE DEF @                       $* 表格
NEW MRKP PURP $!purp AT @             $* 标记点
NEW AXESYM                            $* 轴线符号
  ASMBLR $!assembly
  AXSTYPE $!type
  AXSSIZE $!scale
```

---

## 六、图层操作

```pml
NEW LAYER /path/name
  PURP DIMA|LABA|NOTA|TAGA
  ... 全套样式属性
END

DELETE LAYE MEM                       $* 删除层及成员
layer_show / layer_hide               $* (kcs_draft)
dwg_layers_shown_get
```

---

## 七、符号操作

```pml
NEW SYLB /name                        $* 符号库
  BSRF =0
  SIZE 200mm 200mm
NEW SYTM
  AT X 100mm Y 100mm
NEW SYMB /name/PS

NEW SLAB TMRF $!symbol ON $!ref      $* 符号引用
NEW MRKP MCOLOUR 1 MSTYLE STOP SCALE 1
```

---

## 八、出图输出

```pml
$* PLT 文件
plot ce "$!plotFile" over

$* PDF
PLOT SHEE PDF "$!file" 'COLOUR STANDARD,ISOCOL,NOVIEW' A4V over

$* SVG/METAFILE/IMAGE
PLOT SHEET FILE SVG "$!file" '$!opts' OVERWRITE

$* 打印机
PLOT SHEET FILE PRINT '$!opts'

$* DXF 导入导出
LIEXEC /Draft_DXF_LI 'DXFOUT' CONFIGDATA '$!config' OUTPUTFILENAME '$!file'
dwg_dxf_import(file)  -- (Vitesse)
dwg_dxf_export(file)  -- (Vitesse)
```

---

## 九、更新命令

```pml
update all                            $* 更新全部
update anno                           $* 更新标注
update desi                           $* 更新设计元素
REFRESH                               $* 刷新显示
SAVEWORK                              $* 保存
```

---

## 十、Handle 错误码速查（Draft 专用）

| 错误码 | 含义 |
|---|---|
| (61,528) | 用户 ESC 退出（最高频） |
| (41,52) | 引用类型非法 |
| (41,12) | 名称已存在 |
| (43,364) | 复制失败 |
| (64,503) | 图片未加载 |
| (64,377) | 元素不适用 |
| (64,382) | codeword 不可访问 |
| (64,277) | Ppoint 不存在 |
| (64,499) | DB 不支持 |
| (64,285) | PPLINE 不存在 |
| (61,604) | 色典无此色 |
| (46,28) | 变量未定义 |
| (1000,0) | API 未导入 |
