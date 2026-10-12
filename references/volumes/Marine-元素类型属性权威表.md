# Marine 元素类型属性权威表（DMRM 826p 权威提取）

> **来源**：AVEVA Marine 12.1 SP4《Data Model Reference Manual》（DMRM.pdf，826 页，文本版
> `PML语料/pdf_text/DMRM.txt`，含 `===== PAGE n =====` 分隔符）。
> 30 个高频元素类型中 **27 个在 DMRM 正文找到权威章节**（Ch4 Design 库 19 个 + Ch6 Draft 库 8 个），
> **3 个未收录**（SLAB / SKEY / POSITION，见对应条目与文末说明）。
> 属性**类型**列取自 DMRM 第 16 章《Introduction to Attributes — 16.2 List of All Attributes》
> （约 3000 条属性字典，按"说明文字匹配 + 属性名匹配"对应到 Ch4 显示名；`—` 表示字典未匹配）。
> 页码均可回查：给出 PDF 物理页码与手册印刷页码（如 4:90 = 第 4 章第 90 页）。
> 提取日期：2026-09-29。

**图例**：属性行尾 `◊` = 该行提取自本节 owners/members 区带（PDF 两栏串行所致），
个别行可能实为相邻类型表格的延续，使用前建议按页码回查原书；`[推断]` = 手册未直接使用该 PML 短码，映射关系由其他官方手册佐证。

---

## EQUI（Equipment，设备）— DMRM §4.8.2 ｜ PDF 第194页 ｜ 印刷页 4:90

> 层级标签（原书）：Equipment Element / Primary Element

共 33 条属性。

| 属性（Ch4 显示名） | DB 属性名（Ch16） | 类型 | 说明（原书） |
|---|---|---|---|
| Height | HEIG | real | Height |
| Angle | ANGL | real | Angle |
| Radius | RADI | real | Radius |
| Ispec | ISPE | element | Insulation spec reference |
| Duty | DUTY | string(120) | Duty |
| Desparam | DESP | real(100) | Design parameters |
| Orrf | ORRF | element | Origin reference (for templates) |
| Stmf | STMF | element | Template selection pointer |
| Name | NAME | string(500) | Name of the element |
| Description | DESC | string(120) | Description of the element |
| Function | FUNC | string(120) | Function |
| Purpose | PURP | word | Description code word |
| Number | NUMB | integer | Number |
| Area | AREA | integer | Area |
| Usrweight | USRWEI | integer(500) | User entered weight value |
| Usrwweight | USRWWE | integer(500) | User entered wet weight value |
| Usrcogravity | USRCOG | integer(500) | User centre of gravity position |
| Usrwcogravity | USRWCO | integer(500) | User wet centre of gravity position |
| Position | POS | pos | Position |
| Orientation | ADEG | real | Orientation |
| Built | BUIL | logical | Built/Unbuilt flag |
| Uwmtxt | UWMTXT | string(120) | User weight Manager text |
| Dscode ◊ | DSCO | string(120) | Design code |
| Ptspec ◊ | PTSP | string(120) | Paint specification |
| Inschedule ◊ | INSC | string(120) | Inspection schedule |
| Skey ◊ | SKEY | string(4) | Symbol key |
| StlRef ◊ | STLR | element | Steel Reference |
| Invfarray ◊ | INVF | element(500) | Array of Inventory Items |
| Spref ◊ | SPRE | element | Component spec reference |
| Fstatus ◊ | FSTAT | string(15) | Fstatus |
| Mdsysf ◊ | MDSYSF | element(10) | Reference Array of Model and Design Elements |
| Inprtref ◊ | INPRTR | element | Inside paint reference |
| Ouprtref ◊ | OUPRTR | element | Outside paint reference |

- **Legal Owners（合法父类型）**：ZONE（Zone Element）
- **Legal Members（合法子类型）**：BOX（Box Element）；CONE（Cone Element）；CTORUS（Circular Torus Element）；CYLINDER（Cylinder Element）；DDSE（Design Dataset Element）；DISH（Dish Element）；DPSET（Design Ppoint/Pline Set Element）；DRAWING（Drawn Line Element）；ELCONN（Electrical Connection Element）；EXTRUSION（Extrusion Element）；LOAPOINT（Equipment Load Point Element）；NOZZLE（Nozzle Element）；PANEL（Panel Element）；POHEDRON（Polyhedron Element）；POLYHEDRON（Polyhedron Element）；PVOLUME（Penalty or Preferred Volume Element）；PYRAMID（Pyramid Element）；REVOLUTION（Revolution Element）；RPLANE（Routing Plane Element）；RTORUS（Rectangular Torus Element）；SLCYLINDER（Slope Bottom Cylinder Element）；SNOUT（Snout Element）；SUBEQUIPMENT（Subequipment Element）；TEXT（Text Element）；TMPLATE（Template Element）

---

## BRAN（Branch，支管（管路分支））— DMRM §4.23.1 ｜ PDF 第336页 ｜ 印刷页 4:232

> 注：手册记名 **Branch Element (BRANCH)**（PML 短码 BRAN）。
>
> 层级标签（原书）：Piping Major Items Element / Primary Element

共 74 条属性。

| 属性（Ch4 显示名） | DB 属性名（Ch16） | 类型 | 说明（原书） |
|---|---|---|---|
| Name | NAME | string(500) | Name of the element |
| Description | DESC | string(120) | Description of the element |
| Skey | SKEY | string(4) | Symbol key |
| Function | FUNC | string(120) | Function |
| Purpose | PURP | word | Description code word |
| Built | BUIL | logical | Built/Unbuilt flag |
| Shop | SHOP | logical | Shop/Site flag |
| Isohidden | ISOHIDDEN | logical | Isohidden flag |
| Hposition | HPOS | pos | Head position |
| Tposition | TPOS | pos | Tail position |
| Hdirection | HDIR | dir | Head direction |
| Tdirection | TDIR | dir | Tail direction |
| Href | HREF | element | Head reference |
| Tref | TREF | element | Tail reference |
| Lhead | LHEA | logical | Logical head flag |
| Ltail | LTAI | logical | Logical tail flag |
| Hbore | HBOR | real | Head bore |
| Tbore | TBOR | real | Tail bore |
| Hconnect | HCON | word | Head connection type |
| Tconnect | TCON | word | Tail connection type |
| Detail | DETA | logical | Detail flag |
| Lstressed | LSTR | logical | Stress flag |
| Linetype | LNTP | word | Line type |
| Erection | EREC | integer | Erection class |
| Temperature | TEMP | real | Temperature |
| Pressure | PRES | real | Pressure |
| TPressure | TPRESS | real | TestPressure |
| Flowdirection | FLOW | word | Flow direction |
| Hstube | HSTU | element | Head tube specification |
| Ccentre | CCEN | integer | Cost centre |
| Cclass | CCLA | integer | Cost class |
| Safclass | SAFC | integer | Safety class |
| Matref | MATR | element | Material reference |
| Fluref | FLUR | element | Fluid reference |
| Casref | CASR | element | Case reference |
| Pspec | PSPE | element | Pipe specification |
| Ispec | ISPE | element | Insulation spec reference |
| Tspec | TSPE | element | Tracing spec reference |
| Duty | DUTY | string(120) | Duty |
| Dscode | DSCO | string(120) | Design code |
| Ptspec | PTSP | string(120) | Paint specification |
| Inschedule | INSC | string(120) | Inspection schedule |
| Splh | SPLH | string(120) | Old spooler head tube spool number |
| Hdmtype | HDMT | word(2) | ISODRAFT Reference Dimension attribute |
| Hdmfarray | HDMF | element(2) | ISODRAFT Reference Dimension attribute |
| Tdmtype | TDMT | word(2) | ISODRAFT Reference Dimension attribute |
| Tdmfarray | TDMF | element(2) | ISODRAFT Reference Dimension attribute |
| Lissue | LISS | logical | True if drawing has been issued |
| Wmaximum | WMAX | integer | Maximum weld number in current spool drawing |
| Pmaximum | PMAX | integer | Maximum part number in current spool drawing |
| Ptnhead | PTNH | integer | Old spooler head tube part number |
| Smaximum | SMAX | integer | Maximum spool number in current spool drawing |
| Jmaximum | JMAX | integer | Maximum joint number in current spool drawing |
| Mtohead | MTOH | word | Material list control for head tube |
| Ptnbarray ◊ | PTNB | integer(20) | Old spooler bolt part number |
| Drrf ◊ | DRRF | element | Old spooler drawing reference |
| Spsp ◊ | SPSP | string(2) | Old spooler spool prefix |
| Jnumber ◊ | JNUM | integer(2) | Old spooler joint number |
| Joiprefix ◊ | JOIP | word(2) | Old spooler joint number prefix |
| Orrf ◊ | ORRF | element | Origin reference (for templates) |
| BendMacReference ◊ | BENDMC | element | Bending Machine reference |
| Inco ◊ | — | — | Array of integers for ROUTER internal points |
| PLANU ◊ | PLANU | string(1000) | Planning Unit |
| Bstatus ◊ | BSTA | integer | Branch Status code (Router) |
| Hwrf ◊ | HWRF | element | Head Working Point (Router) |
| Twrf ◊ | TWRF | element | Tail Working Point (Router) |
| Brlock ◊ | BRLO | integer | Branch Positioning Status code (Router) |
| Rlstored ◊ | RLSE | integer(500) | Array of ROUTER saved rules |
| Tsfbreak ◊ | TSFBR | logical | Spooling marker for leave tube |
| Deldsg ◊ | DELDSG | word | Delivery Designation flag |
| Mdsysf ◊ | MDSYSF | element(10) | Reference Array of Model and Design Elements |
| Inprtref ◊ | INPRTR | element | Inside paint reference |
| Ouprtref ◊ | OUPRTR | element | Outside paint reference |
| Sloreference ◊ | SLOREF | element | Pipe slope reference |

- **Legal Owners（合法父类型）**：HVAC（HVAC Element）；PIPE（Pipe Element）
- **Legal Members（合法子类型）**：AHU（Air Handling Unit Element）；ATTACHMENT（Attachment Point Element）；BATTERY（Battery Element）；BEND（Bend Element）；BRCO（Branch Connector Element）；CAP（Cap Element）；CLOSURE（Closure Element）；COUPLING（Coupling Element）；COWL（Cowl Element）；CROSS（Cross Element）；DAMPER（Damper Element）；DUCTING（Ducting Element）；ELBOW（Elbow Element）；FBLIND（Blind Flange Element）；FILTER（Filter Element）；FLANGE（Flange Element）；FLEXIBLE（Flexible Element）；FTUBE（Fixed Length Tube Element）；GASKET（Gasket Element）；GRILLE（Grille Element）；HACC（Access Panel Element）；HFAN（Fan Element）；HSADDLE（Saddle Element）；IDAM（Internal Damper Element）；INSTRUMENT（Instrument Element）；LJSE（Lap-joint Stub End Element）；MESH（Mesh Element）；OFST（Offset Element）；OLET（Olet Element）；PCOMPONENT（Piping Component Element）；PLATE（Plate Element）；PLENUM（Plenum Element）；REDUCER（Reducer Element）；SHU（Standard Hook-up Element）；SILENCER（Silencer Element）；SKIR（Skirt Element）；SPLR（Splitter Element）；STIFFENER（Stiffener Element）；STRT（Straight Element）；TAPER（Taper Element）；TEE（Tee Element）；THREEWAY（Threeway Element）；TP（Test Point Element）；TRAP（Trap Element）；TRNS（Transformation Piece Element）；UNION（Union Element）；VALVE（Valve Element）；VENT（Vent Element）；VFWAY（Four Way Valve Element）；VTWAY（Three Way Valve Element）；WELD（Weld Element）

---

## PIPE（Pipe，管线）— DMRM §4.23.4 ｜ PDF 第342页 ｜ 印刷页 4:238

> 层级标签（原书）：Piping Major Items Element / Primary Element

共 43 条属性。

| 属性（Ch4 显示名） | DB 属性名（Ch16） | 类型 | 说明（原书） |
|---|---|---|---|
| Name | NAME | string(500) | Name of the element |
| Description | DESC | string(120) | Description of the element |
| Function | FUNC | string(120) | Function |
| Purpose | PURP | word | Description code word |
| Built | BUIL | logical | Built/Unbuilt flag |
| Shop | SHOP | logical | Shop/Site flag |
| Isohidden | ISOHIDDEN | logical | Isohidden flag |
| Bore | BORE | real | Bore |
| Temperature | TEMP | real | Temperature |
| Pressure | PRES | real | Pressure |
| TPressure | TPRESS | real | TestPressure |
| Pspec | PSPE | element | Pipe specification |
| Ispec | ISPE | element | Insulation spec reference |
| Tspec | TSPE | element | Tracing spec reference |
| Matref | MATR | element | Material reference |
| Fluref | FLUR | element | Fluid reference |
| Casref | CASR | element | Case reference |
| Ccentre | CCEN | integer | Cost centre |
| Cclass | CCLA | integer | Cost class |
| Linetype | LNTP | word | Line type |
| Erection | EREC | integer | Erection class |
| Rev | REV | integer | Pipe Revision number |
| Safclass | SAFC | integer | Safety class |
| Duty | DUTY | string(120) | Duty |
| Dscode | DSCO | string(120) | Design code |
| Ptspec | PTSP | string(120) | Paint specification |
| Inschedule | INSC | string(120) | Inspection schedule |
| Skey | SKEY | string(4) | Symbol key |
| Lissue | LISS | logical | True if drawing has been issued |
| Wmaximum | WMAX | integer | Maximum weld number in current spool drawing |
| Pmaximum | PMAX | integer | Maximum part number in current spool drawing |
| Smaximum | SMAX | integer | Maximum spool number in current spool drawing |
| Jmaximum | JMAX | integer | Maximum joint number in current spool drawing |
| Drrf | DRRF | element | Old spooler drawing reference |
| Cdrg ◊ | CDRG | string(24) | Isodraft Compipe: Drawing number |
| Cnumber ◊ | CNUM | string(22) | Isodraft Compipe: Line number |
| Carea ◊ | CARE | string(12) | Isodraft Compipe: Area |
| Splprefix ◊ | SPLP | string(120) | Spool number prefix |
| Orrf ◊ | ORRF | element | Origin reference (for templates) |
| Deldsg ◊ | DELDSG | word | Delivery Designation flag |
| Mdsysf ◊ | MDSYSF | element(10) | Reference Array of Model and Design Elements |
| Inprtref ◊ | INPRTR | element | Inside paint reference |
| Ouprtref ◊ | OUPRTR | element | Outside paint reference |

- **Legal Owners（合法父类型）**：ZONE（Zone Element）
- **Legal Members（合法子类型）**：BRANCH（Branch Element）；PPLIST（Pipe Piece List Element）；PSLIST（Pipe Spool List Element）；RESTRAINT（Restraint Element）；TEXT（Text Element）

---

## STRU（Structure，结构）— DMRM §4.32.37 ｜ PDF 第443页 ｜ 印刷页 4:339

> 层级标签（原书）：Structural Element / Primary Element

共 25 条属性。

| 属性（Ch4 显示名） | DB 属性名（Ch16） | 类型 | 说明（原书） |
|---|---|---|---|
| Name | NAME | string(500) | Name of the element |
| Orrf | ORRF | element | Origin reference (for templates) |
| Drnstart | DRNS | dir | Plane normal at start of SCTN/GENSEC |
| Drnend | DRNE | dir | Plane normal at end of SCTN/GENSEC |
| Ydirection | YDIR | dir | Preferred Y axis direction |
| Description | DESC | string(120) | Description of the element |
| Function | FUNC | string(120) | Function |
| Purpose | PURP | word | Description code word |
| Number | NUMB | integer | Number |
| Area | AREA | integer | Area |
| Position | POS | pos | Position |
| Orientation | ADEG | real | Orientation |
| Usrweight | USRWEI | integer(500) | User entered weight value |
| Usrwweight | USRWWE | integer(500) | User entered wet weight value |
| Usrcogravity | USRCOG | integer(500) | User centre of gravity position |
| Usrwcogravity | USRWCO | integer(500) | User wet centre of gravity position |
| Uwmtxt | UWMTXT | string(120) | User weight Manager text |
| Built | BUIL | logical | Built/Unbuilt flag |
| DUnion ◊ | DUNION | integer | DRAFT element union detail flag |
| Skey ◊ | SKEY | string(4) | Symbol key |
| Stmf ◊ | STMF | element | Template selection pointer |
| Invfarray ◊ | INVF | element(500) | Array of Inventory Items |
| Fstatus ◊ | FSTAT | string(15) | Fstatus |
| Inprtref ◊ | INPRTR | element | Inside paint reference |
| Ouprtref ◊ | OUPRTR | element | Outside paint reference |

- **Legal Owners（合法父类型）**：ZONE（Zone Element）
- **Legal Members（合法子类型）**：BOX（Box Element）；CONE（Cone Element）；CTORUS（Circular Torus Element）；CTWALL（Constant Thickness Wall Element）；CYLINDER（Cylinder Element）；DDSE（Design Dataset Element）；DISH（Dish Element）；DPSET（Design Ppoint/Pline Set Element）；DRAWING（Drawn Line Element）；EXTRUSION（Extrusion Element）；FRMWORK（Framework Element）；HANDRA（Handrail Element）；LADDER（Ladder Element）；LCDESCRIPTOR（Load Case Descriptor Element）；PANEL（Panel Element）；PLTFRM（Platform Element）；POHEDRON（Polyhedron Element）；POLYHEDRON（Polyhedron Element）；PVOLUME（Penalty or Preferred Volume Element）；PYRAMID（Pyramid Element）；REVOLUTION（Revolution Element）；ROOM（Room Element）；RPLANE（Routing Plane Element）；RPLGROUP（Routing Plane Element）；RTORUS（Rectangular Torus Element）；SLCYLINDER（Slope Bottom Cylinder Element）；SNOUT（Snout Element）；STRFLT（Stair Flight Element）；STRTWR（Stair Tower Element）；SUBSTRUCTURE（Substructure Element）；TEXT（Text Element）；TMPLATE（Template Element）

---

## SCTN（Structural Section，结构梁截面（型材构件））— DMRM §4.32.31 ｜ PDF 第438页 ｜ 印刷页 4:334

> 层级标签（原书）：Structural Element / Primary Element

共 29 条属性。

| 属性（Ch4 显示名） | DB 属性名（Ch16） | 类型 | 说明（原书） |
|---|---|---|---|
| Name | NAME | string(500) | Name of the element |
| Description | DESC | string(120) | Description of the element |
| Function | FUNC | string(120) | Function |
| Purpose | PURP | word | Description code word |
| Gtype | GTYP | word | Generic type |
| Number | NUMB | integer | Number |
| Desparam | DESP | real(100) | Design parameters |
| Built | BUIL | logical | Built/Unbuilt flag |
| Shop | SHOP | logical | Shop/Site flag |
| Bangle | BANG | real | Beta angle |
| Drnstart | DRNS | dir | Plane normal at start of SCTN/GENSEC |
| Drnend | DRNE | dir | Plane normal at end of SCTN/GENSEC |
| Posstart | POSS | pos | Start point position |
| Posend | POSE | pos | End point position |
| Joistart | JOIS | element | Start joint |
| Joiend | JOIE | element | End joint |
| Jline | JLIN | word | Joining line |
| Jusline | JUSL | word | Justification Pline |
| Ctystart | CTYS | word | Start connection type |
| Ctyend | CTYE | word | End connection type |
| Srelease | SREL | integer | Start releases (packed) |
| Erelease | EREL | integer | End releases (packed) |
| Grade | GRADE | real | Steel grade |
| Matref | MATR | element | Material reference |
| Ispec | ISPE | element | Insulation spec reference |
| Firesistance | FIRE | real | Fire resistance |
| WeldDp | WELDDP | real | Welding depth |
| PosNo | POSNO | integer | Position number |
| ParNam | PARNAM | string(256) | Part name |

- **Legal Owners（合法父类型）**：CFLOOR（Floor Element）；CWALL（Wall Element）；FRMWORK（Framework Element）；SBFRAMEWORK（Subframework Element）；TMPLATE（Template Element）
- **Legal Members（合法子类型）**：CMFITTING（Compound fitting Element）；DDSE（Design Dataset Element）；DPSET（Design Ppoint/Pline Set Element）；FITTING（Fitting Element）；SDLOAD（Section Distributed Load Element）；SELJOINT（Section Linear Joint Element）；SNODE（Secondary Node Element）；SPLOAD（Section Point Load Element）；TMPLATE（Template Element）

---

## GENSEC（Structural Generic Section，结构通用截面）— DMRM §4.32.13 ｜ PDF 第419页 ｜ 印刷页 4:315

> 层级标签（原书）：Structural Element / Primary Element

共 38 条属性。

| 属性（Ch4 显示名） | DB 属性名（Ch16） | 类型 | 说明（原书） |
|---|---|---|---|
| Name | NAME | string(500) | Name of the element |
| Description | DESC | string(120) | Description of the element |
| Function | FUNC | string(120) | Function |
| Gtype | GTYP | word | Generic type |
| Number | NUMB | integer | Number |
| Desparam | DESP | real(100) | Design parameters |
| Built | BUIL | logical | Built/Unbuilt flag |
| Shop | SHOP | logical | Shop/Site flag |
| Bangle | BANG | real | Beta angle |
| LMirror | LMIRR | logical | True if Mirroring required |
| Joistart | JOIS | element | Start joint |
| Joiend | JOIE | element | End joint |
| Jlnstart | JLNS | word | Joining line start |
| Jlnend | JLNE | word | Joining line end |
| Jusline | JUSL | word | Justification Pline |
| Ctystart | CTYS | word | Start connection type |
| Ctyend | CTYE | word | End connection type |
| Srelease | SREL | integer | Start releases (packed) |
| Erelease ◊ | EREL | integer | End releases (packed) |
| Grade ◊ | GRADE | real | Steel grade |
| Matref ◊ | MATR | element | Material reference |
| Ispec ◊ | ISPE | element | Insulation spec reference |
| Firesistance ◊ | FIRE | real | Fire resistance |
| WeldDp ◊ | WELDDP | real | Welding depth |
| PosNo ◊ | POSNO | integer | Position number |
| ParNam ◊ | PARNAM | string(256) | Part name |
| Inref ◊ | INRE | element | Insulation reference |
| Spref ◊ | SPRE | element | Component spec reference |
| Antype ◊ | ANTY | string(120) | Analysis type |
| Memline ◊ | MEML | word | Member line for SCTNs |
| Orrf ◊ | ORRF | element | Origin reference (for templates) |
| Position ◊ | POS | pos | Position |
| Orientation ◊ | ADEG | real | Orientation |
| Purpose ◊ | PURP | word | Description code word |
| Tmrref ◊ | TMRREF | element | Template Repeat Element Reference |
| RepCount ◊ | REPCOU | integer | Rule Repeat Counter |
| Prodrf ◊ | PRODRF | element | Reference to Production Object |
| Bevcodes ◊ | BEVCOD | real(10) | Bevel codes for edges |

- **Legal Owners（合法父类型）**：CAGSEG（Cage Segment Element）；CFLOOR（Floor Element）；CLNLATTICE（Ceiling Lattice Element）；CTFEAT（Cable Tray Feature Element）；CWALL（Wall Element）；EXTFRM（External Framework Element）；FRMWORK（Framework Element）；HRGATE（Handrail Gate Element）；HRPANE（Handrail Panel Element）；HRPOST（Handrail Post Element）；HRTERM（Handrail Termination Element）；INTFRM（Platform Internal Framework Element）；INTLNG（Intermediate Landing Element）；LDRRUN（Ladder Rung Element）；LDRSTR（Ladder Stringer Element）；PLTGRD（Plating Grid Element）；SBFRAMEWORK（Subframework Element）；STRLNG（Stair Landing Element）；STRSTR（Stair String Element）；TMPLATE（Template Element）；TREAD（Tread Element）；TWRSTL（Tower Steel Element）
- **Legal Members（合法子类型）**：COMFIXING（Complementary Fitting Element）；DDSE（Design Dataset Element）；DPSET（Design Ppoint/Pline Set Element）；JLDATUM（Justification Line Datum Element）；SPINE（Spine (of Gensec) Element）；TMPLATE（Template Element）

---

## BOX（Box，长方体基元）— DMRM §4.25.1 ｜ PDF 第349页 ｜ 印刷页 4:245

> 层级标签（原书）：Primitive Element

共 21 条属性。

| 属性（Ch4 显示名） | DB 属性名（Ch16） | 类型 | 说明（原书） |
|---|---|---|---|
| Name | NAME | string(500) | Name of the element |
| Description | DESC | string(120) | Description of the element |
| Function | FUNC | string(120) | Function |
| Purpose | PURP | word | Description code word |
| Number | NUMB | integer | Number |
| Dconnect | DCON | word | Design PPoint connection type |
| Bore | BORE | real | Bore |
| Position | POS | pos | Position |
| Orientation | ADEG | real | Orientation |
| Ddirection | DDIR | dir | Design PPoint spherical direction |
| Radius | RADI | real | Radius |
| Pvifilter | PVIF | integer | PPoint/Pline visibility filter |
| Pskey | PSKE | word | Key for ISODRAFT |
| Orrf | ORRF | element | Origin reference (for templates) |
| Level ◊ | LEVE | integer(2) | Drawing level |
| Obstruction ◊ | OBST | integer | Obstruction level |
| Xlength ◊ | XLEN | real | X length |
| Ylength ◊ | YLEN | real | Y length |
| Zlength ◊ | ZLEN | real | Z length |
| Tmrref ◊ | TMRREF | element | Template Repeat Element Reference |
| RepCount ◊ | REPCOU | integer | Rule Repeat Counter |

- **Legal Owners（合法父类型）**：EQUIPMENT（Equipment Element）；PTRACK（Pipe Track Element）；STRUCTURE（Structure Element）；SUBEQUIPMENT（Subequipment Element）；SUBSTRUCTURE（Substructure Element）；SVOLMODEL（Sub Volume Model Element）；TMPLATE（Template Element）；SVOLMODEL（Sub Volume Model Element）
- **Legal Members（合法子类型）**：NBOX（Negative Box Element）；NCONE（Negative Cone Element）；NCTORUS（Negative Circular Torus Element）；NCYLINDER（Negative Cylinder Element）；NDISH（Negative Dish Element）；NPOLYHEDRON（Negative Polyhedron Element）；NPYRAMID（Negative Pyramid Element）；NREVOLUTION（Negative Revolution Element）；NRTORUS（Negative Rectangular Torus Element）；NSLCYLINDER（Negative Slope Bottom Cylinder Element）；NSNOUT（Negative Snout Element）；NXTRUSION（Negative Rectangular Extrusion Element）

---

## CYLI（Cylinder，圆柱基元）— DMRM §4.25.4 ｜ PDF 第354页 ｜ 印刷页 4:250

> 层级标签（原书）：Primitive Element

共 11 条属性。

| 属性（Ch4 显示名） | DB 属性名（Ch16） | 类型 | 说明（原书） |
|---|---|---|---|
| Name ◊ | NAME | string(500) | Name of the element |
| Purpose ◊ | PURP | word | Description code word |
| Position ◊ | POS | pos | Position |
| Orientation ◊ | ADEG | real | Orientation |
| Level ◊ | LEVE | integer(2) | Drawing level |
| Obstruction ◊ | OBST | integer | Obstruction level |
| Diameter ◊ | DIAM | real | Diameter |
| Height ◊ | HEIG | real | Height |
| Orrf ◊ | ORRF | element | Origin reference (for templates) |
| Tmrref ◊ | TMRREF | element | Template Repeat Element Reference |
| RepCount ◊ | REPCOU | integer | Rule Repeat Counter |

- **Legal Owners（合法父类型）**：EQUIPMENT（Equipment Element）；PTRACK（Pipe Track Element）；STRUCTURE（Structure Element）；SUBEQUIPMENT（Subequipment Element）；SUBSTRUCTURE（Substructure Element）；SVOLMODEL（Sub Volume Model Element）；TMPLATE（Template Element）；VOLMODEL（Volume Model Element）
- **Legal Members（合法子类型）**：NBOX（Negative Box Element）；NCONE（Negative Cone Element）；NCTORUS（Negative Circular Torus Element）；NCYLINDER（Negative Cylinder Element）；NDISH（Negative Dish Element）；NPOLYHEDRON（Negative Polyhedron Element）；NPYRAMID（Negative Pyramid Element）；NREVOLUTION（Negative Revolution Element）；NRTORUS（Negative Rectangular Torus Element）；NSLCYLINDER（Negative Slope Bottom Cylinder Element）；NSNOUT（Negative Snout Element）；NXTRUSION（Negative Rectangular Extrusion Element）

---

## NOZZ（Nozzle，接管嘴）— DMRM §4.8.3 ｜ PDF 第196页 ｜ 印刷页 4:92

> 层级标签（原书）：Equipment Element

共 23 条属性。

| 属性（Ch4 显示名） | DB 属性名（Ch16） | 类型 | 说明（原书） |
|---|---|---|---|
| Name | NAME | string(500) | Name of the element |
| Description | DESC | string(120) | Description of the element |
| Function | FUNC | string(120) | Function |
| Purpose | PURP | word | Description code word |
| Position | POS | pos | Position |
| Orientation | ADEG | real | Orientation |
| Temperature | TEMP | real | Temperature |
| Pressure | PRES | real | Pressure |
| TPressure | TPRESS | real | TestPressure |
| Cref | CREF | element | Connection reference |
| Catref | CATR | element | Catalogue reference |
| Height | HEIG | real | Height |
| Angle | ANGL | real | Angle |
| Radius | RADI | real | Radius |
| Ispec | ISPE | element | Insulation spec reference |
| Duty | DUTY | string(120) | Duty |
| Desparam | DESP | real(100) | Design parameters |
| Orrf | ORRF | element | Origin reference (for templates) |
| Stmf | STMF | element | Template selection pointer |
| Invfarray | INVF | element(500) | Array of Inventory Items |
| Bselector | BSEL | string(3) | Bolt Selector |
| Inprtref | INPRTR | element | Inside paint reference |
| Ouprtref | OUPRTR | element | Outside paint reference |

- **Legal Owners（合法父类型）**：EQUIPMENT（Equipment Element）；SUBEQUIPMENT（Subequipment Element）；TMPLATE（Template Element）
- **Legal Members（合法子类型）**：DDSE（Design Dataset Element）；DPSET（Design Ppoint/Pline Set Element）；TMPLATE（Template Element）

---

## FLAN（Flange，法兰）— DMRM §4.21.12 ｜ PDF 第310页 ｜ 印刷页 4:206

> 层级标签（原书）：Piping Component Element

共 41 条属性。

| 属性（Ch4 显示名） | DB 属性名（Ch16） | 类型 | 说明（原书） |
|---|---|---|---|
| Name | NAME | string(500) | Name of the element |
| Position | POS | pos | Position |
| Orientation | ADEG | real | Orientation |
| Desparam | DESP | real(100) | Design parameters |
| Built | BUIL | logical | Built/Unbuilt flag |
| Shop | SHOP | logical | Shop/Site flag |
| Isohidden | ISOHIDDEN | logical | Isohidden flag |
| Spref | SPRE | element | Component spec reference |
| Lstube | LSTU | element | Leave tube reference |
| Arrive | ARRI | integer | Arrive Ppoint |
| Leave | LEAV | integer | Leave Ppoint |
| Oriflag | ORIF | logical | Orientation flag |
| Posflag | POSF | logical | Positioning flag |
| Ispec | ISPE | element | Insulation spec reference |
| Tspec | TSPE | element | Tracing spec reference |
| Loose | LOOS | logical | Loose |
| Height | HEIG | real | Height |
| Cref | CREF | element | Connection reference |
| Csfbreak | CSFBR | logical | Spooling marker for components |
| Tsfbreak | TSFBR | logical | Spooling marker for leave tube |
| Spln | SPLN | string(120) | Old spooler component spool number |
| Splt | SPLT | string(120) | Old spooler tube spool number |
| Mtoref | MTOR | element(20) | Extra material list spec references |
| Cmpx | — | — | Comparator/Design-Manager exclusion text attribute |
| Ptno | PTNO | integer | Old spooler component part number |
| Ptntube | PTNT | integer | Old spooler tube part number |
| Ptnbarray | PTNB | integer(20) | Old spooler bolt part number |
| Jnumber | JNUM | integer(2) | Old spooler joint number |
| Joiprefix | JOIP | word(2) | Old spooler joint number prefix |
| Mtocomponent | MTOC | word | Material list control for components |
| Mtotube | MTOT | word | Material list control for components leave tube |
| Mtoxarray | MTOX | integer(20) | Old spooler addition items |
| Spsp | SPSP | string(2) | Old spooler spool prefix |
| Dpfname | DPFN | string(1024) | ISODRAFT dynamic detail plotfile name |
| Dpgridref | DPGRID | integer | ISODRAFT dynamic detail grid reference attribute |
| Nwelds | NWELDS | integer | Number of attached welds on a piping component |
| Allowance | ALLO | real | Allowance |
| Orrf | ORRF | element | Origin reference (for templates) |
| Invfarray | INVF | element(500) | Array of Inventory Items |
| Bselector | BSEL | string(3) | Bolt Selector |
| MATN | MATN | string(1000) | Material Note |

- **Legal Owners（合法父类型）**：BRANCH（Branch Element）
- **Legal Members（合法子类型）**：NONE（None）

---

## VALV（Valve，阀门）— DMRM §4.21.25 ｜ PDF 第326页 ｜ 印刷页 4:222

> 层级标签（原书）：Piping Component Element

共 49 条属性。

| 属性（Ch4 显示名） | DB 属性名（Ch16） | 类型 | 说明（原书） |
|---|---|---|---|
| Name | NAME | string(500) | Name of the element |
| Position | POS | pos | Position |
| Orientation | ADEG | real | Orientation |
| Desparam | DESP | real(100) | Design parameters |
| Built | BUIL | logical | Built/Unbuilt flag |
| Shop | SHOP | logical | Shop/Site flag |
| Isohidden | ISOHIDDEN | logical | Isohidden flag |
| Spref | SPRE | element | Component spec reference |
| Lstube | LSTU | element | Leave tube reference |
| Arrive | ARRI | integer | Arrive Ppoint |
| Leave | LEAV | integer | Leave Ppoint |
| Oriflag | ORIF | logical | Orientation flag |
| Posflag | POSF | logical | Positioning flag |
| Ispec | ISPE | element | Insulation spec reference |
| Tspec | TSPE | element | Tracing spec reference |
| Angle | ANGL | real | Angle |
| Height | HEIG | real | Height |
| Radius | RADI | real | Radius |
| Cref | CREF | element | Connection reference |
| Csfbreak | CSFBR | logical | Spooling marker for components |
| Tsfbreak | TSFBR | logical | Spooling marker for leave tube |
| Spln | SPLN | string(120) | Old spooler component spool number |
| Splt | SPLT | string(120) | Old spooler tube spool number |
| Mtoref | MTOR | element(20) | Extra material list spec references |
| Cmpx | — | — | Comparator/Design-Manager exclusion text attribute |
| Ptno | PTNO | integer | Old spooler component part number |
| Ptntube | PTNT | integer | Old spooler tube part number |
| Ptnbarray | PTNB | integer(20) | Old spooler bolt part number |
| Jnumber | JNUM | integer(2) | Old spooler joint number |
| Joiprefix | JOIP | word(2) | Old spooler joint number prefix |
| Mtocomponent | MTOC | word | Material list control for components |
| Mtotube | MTOT | word | Material list control for components leave tube |
| Mtoxarray | MTOX | integer(20) | Old spooler addition items |
| Spsp | SPSP | string(2) | Old spooler spool prefix |
| Dpfname | DPFN | string(1024) | ISODRAFT dynamic detail plotfile name |
| Dpgridref | DPGRID | integer | ISODRAFT dynamic detail grid reference attribute |
| Nwelds | NWELDS | integer | Number of attached welds on a piping component |
| Orrf | ORRF | element | Origin reference (for templates) |
| Invfarray | INVF | element(500) | Array of Inventory Items |
| Bselector | BSEL | string(3) | Bolt Selector |
| MATN | MATN | string(1000) | Material Note |
| Rlock | RLOC | integer | Branch Member Creation Status code (Router) |
| Rlinclude | RLIN | element(20) | Array of references of special rules to include |
| Rlexclude | RLEX | element(20) | Array of references of special rules to exclude |
| Hrelative | HREL | logical | Branch Member Head relative flag (Router) |
| Spkchg ◊ | SPKCHG | element | flag to show where a spec change occurs in a branch |
| Deldsg ◊ | DELDSG | word | Delivery Designation flag |
| Inprtref ◊ | INPRTR | element | Inside paint reference |
| Ouprtref ◊ | OUPRTR | element | Outside paint reference |

- **Legal Owners（合法父类型）**：BRANCH（Branch Element）
- **Legal Members（合法子类型）**：NONE（None）

---

## TEE（Tee，三通）— DMRM §4.21.22 ｜ PDF 第323页 ｜ 印刷页 4:219

> 层级标签（原书）：Piping Component Element

共 41 条属性。

| 属性（Ch4 显示名） | DB 属性名（Ch16） | 类型 | 说明（原书） |
|---|---|---|---|
| Name | NAME | string(500) | Name of the element |
| Position | POS | pos | Position |
| Orientation | ADEG | real | Orientation |
| Desparam | DESP | real(100) | Design parameters |
| Built | BUIL | logical | Built/Unbuilt flag |
| Shop | SHOP | logical | Shop/Site flag |
| Isohidden | ISOHIDDEN | logical | Isohidden flag |
| Spref | SPRE | element | Component spec reference |
| Lstube | LSTU | element | Leave tube reference |
| Arrive | ARRI | integer | Arrive Ppoint |
| Leave | LEAV | integer | Leave Ppoint |
| Oriflag | ORIF | logical | Orientation flag |
| Posflag | POSF | logical | Positioning flag |
| Ispec | ISPE | element | Insulation spec reference |
| Tspec | TSPE | element | Tracing spec reference |
| Angle | ANGL | real | Angle |
| Height | HEIG | real | Height |
| Radius | RADI | real | Radius |
| Loffline | LOFF | logical | Offline flag |
| Cref | CREF | element | Connection reference |
| Csfbreak | CSFBR | logical | Spooling marker for components |
| Tsfbreak | TSFBR | logical | Spooling marker for leave tube |
| Spln | SPLN | string(120) | Old spooler component spool number |
| Splt | SPLT | string(120) | Old spooler tube spool number |
| Mtoref | MTOR | element(20) | Extra material list spec references |
| Cmpx | — | — | Comparator/Design-Manager exclusion text attribute |
| Ptno | PTNO | integer | Old spooler component part number |
| Ptntube | PTNT | integer | Old spooler tube part number |
| Ptnbarray | PTNB | integer(20) | Old spooler bolt part number |
| Jnumber | JNUM | integer(2) | Old spooler joint number |
| Joiprefix | JOIP | word(2) | Old spooler joint number prefix |
| Mtocomponent | MTOC | word | Material list control for components |
| Mtotube | MTOT | word | Material list control for components leave tube |
| Mtoxarray | MTOX | integer(20) | Old spooler addition items |
| Spsp | SPSP | string(2) | Old spooler spool prefix |
| Dpfname | DPFN | string(1024) | ISODRAFT dynamic detail plotfile name |
| Dpgridref | DPGRID | integer | ISODRAFT dynamic detail grid reference attribute |
| Nwelds | NWELDS | integer | Number of attached welds on a piping component |
| Dmtype | DMTY | word(2) | ISODRAFT Reference Dimension attribute |
| Dmfarray | DMFA | element(2) | ISODRAFT Reference Dimension attribute |
| Orrf | ORRF | element | Origin reference (for templates) |

- **Legal Owners（合法父类型）**：BRANCH（Branch Element）
- **Legal Members（合法子类型）**：NONE（None）

---

## REDU（Reducer，异径管）— DMRM §4.21.19 ｜ PDF 第319页 ｜ 印刷页 4:215

> 层级标签（原书）：Piping Component Element

共 35 条属性。

| 属性（Ch4 显示名） | DB 属性名（Ch16） | 类型 | 说明（原书） |
|---|---|---|---|
| Name | NAME | string(500) | Name of the element |
| Position | POS | pos | Position |
| Orientation | ADEG | real | Orientation |
| Desparam | DESP | real(100) | Design parameters |
| Built | BUIL | logical | Built/Unbuilt flag |
| Shop | SHOP | logical | Shop/Site flag |
| Isohidden | ISOHIDDEN | logical | Isohidden flag |
| Spref | SPRE | element | Component spec reference |
| Lstube | LSTU | element | Leave tube reference |
| Arrive | ARRI | integer | Arrive Ppoint |
| Leave | LEAV | integer | Leave Ppoint |
| Oriflag | ORIF | logical | Orientation flag |
| Posflag | POSF | logical | Positioning flag |
| Ispec | ISPE | element | Insulation spec reference |
| Tspec | TSPE | element | Tracing spec reference |
| Cref | CREF | element | Connection reference |
| Csfbreak | CSFBR | logical | Spooling marker for components |
| Tsfbreak | TSFBR | logical | Spooling marker for leave tube |
| Spln | SPLN | string(120) | Old spooler component spool number |
| Splt | SPLT | string(120) | Old spooler tube spool number |
| Mtoref | MTOR | element(20) | Extra material list spec references |
| Cmpx | — | — | Comparator/Design-Manager exclusion text attribute |
| Ptno | PTNO | integer | Old spooler component part number |
| Ptntube | PTNT | integer | Old spooler tube part number |
| Ptnbarray | PTNB | integer(20) | Old spooler bolt part number |
| Jnumber | JNUM | integer(2) | Old spooler joint number |
| Joiprefix | JOIP | word(2) | Old spooler joint number prefix |
| Mtocomponent | MTOC | word | Material list control for components |
| Mtotube | MTOT | word | Material list control for components leave tube |
| Mtoxarray | MTOX | integer(20) | Old spooler addition items |
| Spsp | SPSP | string(2) | Old spooler spool prefix |
| Dpfname | DPFN | string(1024) | ISODRAFT dynamic detail plotfile name |
| Dpgridref | DPGRID | integer | ISODRAFT dynamic detail grid reference attribute |
| Nwelds | NWELDS | integer | Number of attached welds on a piping component |
| Orrf | ORRF | element | Origin reference (for templates) |

- **Legal Owners（合法父类型）**：BRANCH（Branch Element）
- **Legal Members（合法子类型）**：NONE（None）

---

## ELBO（Elbow，弯头）— DMRM §4.21.9 ｜ PDF 第306页 ｜ 印刷页 4:202

> 层级标签（原书）：Piping Component Element

共 35 条属性。

| 属性（Ch4 显示名） | DB 属性名（Ch16） | 类型 | 说明（原书） |
|---|---|---|---|
| Name | NAME | string(500) | Name of the element |
| Position | POS | pos | Position |
| Orientation | ADEG | real | Orientation |
| Desparam | DESP | real(100) | Design parameters |
| Built | BUIL | logical | Built/Unbuilt flag |
| Shop | SHOP | logical | Shop/Site flag |
| Isohidden | ISOHIDDEN | logical | Isohidden flag |
| Spref | SPRE | element | Component spec reference |
| Lstube | LSTU | element | Leave tube reference |
| Arrive | ARRI | integer | Arrive Ppoint |
| Leave | LEAV | integer | Leave Ppoint |
| Oriflag | ORIF | logical | Orientation flag |
| Posflag | POSF | logical | Positioning flag |
| Ispec | ISPE | element | Insulation spec reference |
| Tspec | TSPE | element | Tracing spec reference |
| Angle | ANGL | real | Angle |
| Radius | RADI | real | Radius |
| Cref | CREF | element | Connection reference |
| Csfbreak | CSFBR | logical | Spooling marker for components |
| Tsfbreak | TSFBR | logical | Spooling marker for leave tube |
| Spln | SPLN | string(120) | Old spooler component spool number |
| Splt | SPLT | string(120) | Old spooler tube spool number |
| Mtoref | MTOR | element(20) | Extra material list spec references |
| Cmpx | — | — | Comparator/Design-Manager exclusion text attribute |
| Ptno | PTNO | integer | Old spooler component part number |
| Ptntube | PTNT | integer | Old spooler tube part number |
| Ptnbarray | PTNB | integer(20) | Old spooler bolt part number |
| Jnumber | JNUM | integer(2) | Old spooler joint number |
| Joiprefix | JOIP | word(2) | Old spooler joint number prefix |
| Mtocomponent | MTOC | word | Material list control for components |
| Mtotube | MTOT | word | Material list control for components leave tube |
| Mtoxarray | MTOX | integer(20) | Old spooler addition items |
| Spsp | SPSP | string(2) | Old spooler spool prefix |
| Dpfname | DPFN | string(1024) | ISODRAFT dynamic detail plotfile name |
| Dpgridref | DPGRID | integer | ISODRAFT dynamic detail grid reference attribute |

- **Legal Owners（合法父类型）**：BRANCH（Branch Element）
- **Legal Members（合法子类型）**：NONE（None）

---

## ATTA（Attachment Point，附件点（支吊架附着点））— DMRM §4.21.1 ｜ PDF 第295页 ｜ 印刷页 4:191

> 层级标签（原书）：Piping Component Element / Primary Element

共 59 条属性。

| 属性（Ch4 显示名） | DB 属性名（Ch16） | 类型 | 说明（原书） |
|---|---|---|---|
| Name | NAME | string(500) | Name of the element |
| Description | DESC | string(120) | Description of the element |
| PLANU | PLANU | string(1000) | Planning Unit |
| PSTYP | PSTYP | word | Spool Type |
| PSARFA | PSARFA | element(500) | Pipespool arrive references |
| PSLRFA | PSLRFA | element(500) | Pipespool leave references |
| Position | POS | pos | Position |
| Orientation | ADEG | real | Orientation |
| Desparam | DESP | real(100) | Design parameters |
| Built | BUIL | logical | Built/Unbuilt flag |
| Shop | SHOP | logical | Shop/Site flag |
| Isohidden | ISOHIDDEN | logical | Isohidden flag |
| Spref | SPRE | element | Component spec reference |
| Lstube | LSTU | element | Leave tube reference |
| Arrive | ARRI | integer | Arrive Ppoint |
| Leave | LEAV | integer | Leave Ppoint |
| Oriflag | ORIF | logical | Orientation flag |
| Posflag | POSF | logical | Positioning flag |
| Ispec | ISPE | element | Insulation spec reference |
| Tspec | TSPE | element | Tracing spec reference |
| Cstref | CSTR | element | Constraint reference |
| Laxes | — | — | Local axes |
| Attype | ATTY | word | Attachment type |
| Lend | LEND | logical | Line end |
| Cref | CREF | element | Connection reference |
| Stext | STEX | string(2000) | S Text string |
| Csfbreak | CSFBR | logical | Spooling marker for components |
| Tsfbreak | TSFBR | logical | Spooling marker for leave tube |
| Spln | SPLN | string(120) | Old spooler component spool number |
| Splt | SPLT | string(120) | Old spooler tube spool number |
| Dmtype | DMTY | word(2) | ISODRAFT Reference Dimension attribute |
| Dmfarray | DMFA | element(2) | ISODRAFT Reference Dimension attribute |
| Ptno | PTNO | integer | Old spooler component part number |
| Ptntube | PTNT | integer | Old spooler tube part number |
| Ptnbarray | PTNB | integer(20) | Old spooler bolt part number |
| Mtocomponent | MTOC | word | Material list control for components |
| Mtotube | MTOT | word | Material list control for components leave tube |
| Mtoref | MTOR | element(20) | Extra material list spec references |
| Mtoxarray | MTOX | integer(20) | Old spooler addition items |
| Spsp | SPSP | string(2) | Old spooler spool prefix |
| Dpfname | DPFN | string(1024) | ISODRAFT dynamic detail plotfile name |
| Dpgridref | DPGRID | integer | ISODRAFT dynamic detail grid reference attribute |
| Nwelds | NWELDS | integer | Number of attached welds on a piping component |
| Orrf | ORRF | element | Origin reference (for templates) |
| Invfarray | INVF | element(500) | Array of Inventory Items |
| Bselector | BSEL | string(3) | Bolt Selector |
| MATN | MATN | string(1000) | Material Note |
| Rlock | RLOC | integer | Branch Member Creation Status code (Router) |
| Rlinclude | RLIN | element(20) | Array of references of special rules to include |
| Rlexclude | RLEX | element(20) | Array of references of special rules to exclude |
| Hrelative | HREL | logical | Branch Member Head relative flag (Router) |
| Spkbrk | SPKBRK | logical | ATTA flag to treat as a real element |
| Spkchg | SPKCHG | element | flag to show where a spec change occurs in a branch |
| Deldsg | DELDSG | word | Delivery Designation flag |
| Fstatus | FSTAT | string(15) | Fstatus |
| Angle | ANGL | real | Angle |
| Matref | MATR | element | Material reference |
| Inprtref | INPRTR | element | Inside paint reference |
| Ouprtref | OUPRTR | element | Outside paint reference |

- **Legal Owners（合法父类型）**：BRANCH（Branch Element）
- **Legal Members（合法子类型）**：NONE（None）

---

## SLAB — DMRM 未收录（无独立章节）

- DMRM 826 页中不存在 `(SLAB)` 元素类型章节（全文件检索 0 命中）。
- **推断映射 [推断]**：`SLAB` 为 **Draft 库 Special Label（特殊标注）** 的 PML 短码。
  依据：DRAFT User Guide（DRUGP）明确写有 "create new General Label (or **NEW SLAB** to create a Special Label)"、
  "DESSYM is a soft-type variant of the Special Label (SLAB) element"。
  DMRM 中该类型记名为 **Special Label Instance Element (SLABEL)**，§6.1.89，PDF 第539页（印刷页 6:59）。
- 若 PML 语料中的 `NEW SLAB` 属于 Marine 船体模块的"板架 Slab"，则该类型属于 Marine Hull 专用数据模型，不在本 DMRM 通用数据模型内。
- **SLABEL（Special Label）属性参考表**（供 Draft 用法参考，共 64 条）：

| 属性 | DB 属性名 | 类型 | 说明 |
|---|---|---|---|
| Name | NAME | string(500) | Name of the element |
| Spsf | SPSF | element | Sheet pointset reference |
| Exfile | EXFI | integer | Extract file number |
| Arno | ARNO | integer | Picture directory area number |
| Pvno | PVNO | integer | Picture version number |
| Size | SIZE | real(2) | Sheet/region size |
| Bsrf | BSRF | element | Backing sheet reference |
| Idlname | IDLN | element | Drawlist name reference |
| TTFenabled | TTFENA | logical | TrueType fonts enabled flag |
| Layarf | LAYARF | element | Annotation Layer ruleset reference |
| Laydrf | LAYDRF | element | Design Layer ruleset reference |
| Bsfname | BSFN | string(1024) | Backing sheet filename |
| BSDWG | BSDWG | string(120) | AutoCAD backing sheet name |
| BSLayer | BSLAYE | string(120) | AutoCAD backing sheet layer |
| ACDWT | ACDWT | string(120) | AutoCAD drawing template name |
| Title | TITL | string(1000) | Title |
| Idlx | IDLX | string(120) | Drawlist name (as text) |
| Posformat | POSFOR | string | Intelligent Text positional code word expansion style |
| Grsystem | GRSYS | element | Grid system reference |
| SpPurpose | SPPURP | word | Special purpose table attribute |
| Function | FUNC | string(120) | Function |
| PlinOn | PLINON | logical | Pline-required flag |
| Ddname | DDNM | element | Design element reference |
| Nppt | NPPT | integer | Ppoint number |
| Pkey | PKEY | word | Pline identifier key |
| Pkdistance | PKDI | real | Proportional distance along Pline |
| Tmrf | TMRF | element | Template reference |
| Sorf | SORF | element | Source reference (for automatic application) |
| Xyposition | XYPS | pos | 2D Position |
| Oset | OSET | logical | Offset/VIEW position flag |
| Adegrees | ADEG | real | Orientation |
| Ppdirection | PPDI | integer | Ppoint number for direction |
| Llclearance | LLCL | real | Leader line clearance |
| Tsize | TSIZ | real | Terminator size |
| Lterminator | LTER | string | Label terminator code |
| Lleader | LLEA | logical | Leader line flag |
| Apoffset | APOF | real(2) | Leaderline attachment point |
| Cpoffset | CPOF | real(2) | Leaderline connection point wrt. text origin |
| Bpoffset | BPOF | real(4) | Leader bend point offset |
| Lshape | LSHA | string | Leader shape code |
| Font | FONT | integer | Text font |
| Tpen | TPEN | integer | Text pen |
| Llpen | LLPN | integer | Label leader pen |
| Lfpen | LFPN | integer | Label frame pen |
| Blnk | BLNK | logical | Auto-blanking flag |
| Bmargin | BMAR | real | Auto-blanking margin |
| Xyscale | XYSC | real(2) | Label XY size |
| Cheight | CHEI | real | Character height |
| Lvisibility | LVIS | logical | Visibility flag |
| Ddnx | DDNX | string(120) | Design element as text |
| Atext | ATEX | string(1000) | Unintelligent text string |
| Gaps | GAPS | real(30) | Projection line gap array |
| Position | POS | pos | Position |
| Txcolour | TXCOLO | integer | Text colour |
| LLStyle | LLSTYL | integer | Label leader linestyle |
| LLColour | LLCOLO | integer | Label leader colour |
| LFStyle | LFSTYL | integer | Label frame linestyle |
| LFColour | LFCOLO | integer | Label frame colour |
| ACDATE | ACDATE | string(50) | Date last modified in AutoCAD |
| ACLock | ACLOCK | string | AutoCAD picture lock |
| TMDWG | TMDWG | string(120) | AutoCAD template name |
| ACDSTY | ACDSTY | string(120) | AutoCAD Dimension style |
| Justification | JUST | string | Justification |
| Alignment | ALIGN | string | Vertical alignment |

- Legal Owners: LAYER（View Annotation Layer Element）
- Legal Members: NONE（None）

---

## PLAT（Plate，板（暖通/管件板件））— DMRM §4.16.13 ｜ PDF 第271页 ｜ 印刷页 4:167

> 注：此 PLATE 为 **暖通/管系板件**（层级标签 HVAC Component Element，父类型 BRANCH），
> 非船体结构板（船体板另见 HPLATE/HIPLA/CPLATE 等 Marine Hull 类型）。
>
> 层级标签（原书）：HVAC Component Element

共 38 条属性。

| 属性（Ch4 显示名） | DB 属性名（Ch16） | 类型 | 说明（原书） |
|---|---|---|---|
| Name | NAME | string(500) | Name of the element |
| Position | POS | pos | Position |
| Orientation | ADEG | real | Orientation |
| Desparam | DESP | real(100) | Design parameters |
| Built | BUIL | logical | Built/Unbuilt flag |
| Shop | SHOP | logical | Shop/Site flag |
| Isohidden | ISOHIDDEN | logical | Isohidden flag |
| Spref | SPRE | element | Component spec reference |
| Lstube | LSTU | element | Leave tube reference |
| Arrive | ARRI | integer | Arrive Ppoint |
| Leave | LEAV | integer | Leave Ppoint |
| Oriflag | ORIF | logical | Orientation flag |
| Posflag | POSF | logical | Positioning flag |
| Ispec | ISPE | element | Insulation spec reference |
| Tspec | TSPE | element | Tracing spec reference |
| Cref | CREF | element | Connection reference |
| Csfbreak | CSFBR | logical | Spooling marker for components |
| Tsfbreak | TSFBR | logical | Spooling marker for leave tube |
| Spln | SPLN | string(120) | Old spooler component spool number |
| Splt | SPLT | string(120) | Old spooler tube spool number |
| Mtoref | MTOR | element(20) | Extra material list spec references |
| Cmpx | — | — | Comparator/Design-Manager exclusion text attribute |
| Ptno | PTNO | integer | Old spooler component part number |
| Ptntube | PTNT | integer | Old spooler tube part number |
| Ptnbarray | PTNB | integer(20) | Old spooler bolt part number |
| Jnumber | JNUM | integer(2) | Old spooler joint number |
| Joiprefix | JOIP | word(2) | Old spooler joint number prefix |
| Mtocomponent | MTOC | word | Material list control for components |
| Mtotube | MTOT | word | Material list control for components leave tube |
| Mtoxarray | MTOX | integer(20) | Old spooler addition items |
| Spsp | SPSP | string(2) | Old spooler spool prefix |
| Dpfname | DPFN | string(1024) | ISODRAFT dynamic detail plotfile name |
| Dpgridref | DPGRID | integer | ISODRAFT dynamic detail grid reference attribute |
| Nwelds | NWELDS | integer | Number of attached welds on a piping component |
| Orrf | ORRF | element | Origin reference (for templates) |
| Invfarray | INVF | element(500) | Array of Inventory Items |
| Bselector | BSEL | string(3) | Bolt Selector |
| MATN | MATN | string(1000) | Material Note |

- **Legal Owners（合法父类型）**：BRANCH（Branch Element）
- **Legal Members（合法子类型）**：NONE（None）

---

## EXTR（Extrusion，挤出体基元）— DMRM §4.25.7 ｜ PDF 第358页 ｜ 印刷页 4:254

> 层级标签（原书）：Primitive Element

共 10 条属性。

| 属性（Ch4 显示名） | DB 属性名（Ch16） | 类型 | 说明（原书） |
|---|---|---|---|
| Name ◊ | NAME | string(500) | Name of the element |
| Purpose ◊ | PURP | word | Description code word |
| Position ◊ | POS | pos | Position |
| Orientation ◊ | ADEG | real | Orientation |
| Level ◊ | LEVE | integer(2) | Drawing level |
| Obstruction ◊ | OBST | integer | Obstruction level |
| Height ◊ | HEIG | real | Height |
| Orrf ◊ | ORRF | element | Origin reference (for templates) |
| Tmrref ◊ | TMRREF | element | Template Repeat Element Reference |
| RepCount ◊ | REPCOU | integer | Rule Repeat Counter |

- **Legal Owners（合法父类型）**：EQUIPMENT（Equipment Element）；PTRACK（Pipe Track Element）；STRUCTURE（Structure Element）；SUBEQUIPMENT（Subequipment Element）；SUBSTRUCTURE（Substructure Element）；SVOLMODEL（Sub Volume Model Element）；TMPLATE（Template Element）；VOLMODEL（Volume Model Element）
- **Legal Members（合法子类型）**：LOOP（Loop Element）；NBOX（Negative Box Element）；NCONE（Negative Cone Element）；NCTORUS（Negative Circular Torus Element）；NCYLINDER（Negative Cylinder Element）；NDISH（Negative Dish Element）；NPOLYHEDRON（Negative Polyhedron Element）；NPYRAMID（Negative Pyramid Element）；NREVOLUTION（Negative Revolution Element）；NRTORUS（Negative Rectangular Torus Element）；NSLCYLINDER（Negative Slope Bottom Cylinder Element）；NSNOUT（Negative Snout Element）；NXTRUSION（Negative Rectangular Extrusion Element）

---

## LOOP（Loop，环（轮廓环））— DMRM §4.25.9 ｜ PDF 第359页 ｜ 印刷页 4:255

> 层级标签（原书）：Primitive Element

共 4 条属性。

| 属性（Ch4 显示名） | DB 属性名（Ch16） | 类型 | 说明（原书） |
|---|---|---|---|
| Name | NAME | string(500) | Name of the element |
| Position | POS | pos | Position |
| Orrf | ORRF | element | Origin reference (for templates) |
| Purpose | PURP | word | Description code word |

- **Legal Owners（合法父类型）**：AEXTRUSION（Area Extrusion Element）；AREVOLUTION（Area Revolution Element）；BNDLIN（Boundary Line Element）；EXTRUSION（Extrusion Element）；FLRCOV（Floor Covering Element）；INSURQ（Insulation Requirements Element）；NREVOLUTION（Negative Revolution Element）；NXTRUSION（Negative Rectangular Extrusion Element）；REVOLUTION（Revolution Element）
- **Legal Members（合法子类型）**：VERTEX（Vertex Element）

---

## VRTX（Vertex，顶点（Draft））— DMRM §6.1.112 ｜ PDF 第554页 ｜ 印刷页 6:74

> 层级标签（原书）：Draft 2D Drafting Element

共 17 条属性。

| 属性（Ch4 显示名） | DB 属性名（Ch16） | 类型 | 说明（原书） |
|---|---|---|---|
| NLStyle | NLSTYL | integer | Note linestyle |
| NLColour | NLCOLO | integer | Note colour |
| FStyle | FSTYLE | integer | Fill style |
| FColour | FCOLOUR | integer | Fill colour |
| MStyle | MSTYLE | integer | Marker style |
| MColour | MCOLOUR | integer | Marker colour |
| Vwrefarray | VWREFA | element(20) | View reference array - special attribute for use by ADP |
| ACDSTY | ACDSTY | string(120) | AutoCAD Dimension style |
| SpPurpose | SPPURP | word | Special purpose table attribute |
| Function | FUNC | string(120) | Function |
| Name | NAME | string(500) | Name of the element |
| Ptrf | PTRF | element | Point reference |
| Bulgefactor | BULG | real | Bulge factor |
| Fradius | FRAD | real | Fillet radius |
| Chamfers | CHAM | real(2) | Chamfer lengths |
| Nlpen | NLPN | integer | Note/framing pen |
| Mpen | MPEN | integer | Marker pen |

- **Legal Owners（合法父类型）**：OUTLINE（Outline Element）
- **Legal Members（合法子类型）**：NONE（None）

---

## NOTE（Sheet Note，图面注记）— DMRM §6.1.62 ｜ PDF 第522页 ｜ 印刷页 6:42

> 层级标签（原书）：Draft Drawing Layer or Note Element

共 19 条属性。

| 属性（Ch4 显示名） | DB 属性名（Ch16） | 类型 | 说明（原书） |
|---|---|---|---|
| Name | NAME | string(500) | Name of the element |
| Function | FUNC | string(120) | Function |
| Pstf | PSTF | element | Pointset reference |
| Xyposition | XYPS | pos | 2D Position |
| Adegrees | ADEG | real | Orientation |
| Lvisibility | LVIS | logical | Visibility flag |
| Justification | JUST | string | Justification |
| Alignment | ALIGN | string | Vertical alignment |
| Nlpen | NLPN | integer | Note/framing pen |
| Fpen | FPEN | integer | Fill pen |
| Font | FONT | integer | Text font |
| Tpen | TPEN | integer | Text pen |
| Cheight | CHEI | real | Character height |
| Cspacing | CSPA | real | Character spacing factor |
| Lspacing | LSPA | real | Text line spacing factor |
| Blnk | BLNK | logical | Auto-blanking flag |
| Bmargin | BMAR | real | Auto-blanking margin |
| Txcolour | TXCOLO | integer | Text colour |
| NLStyle | NLSTYL | integer | Note linestyle |

- **Legal Owners（合法父类型）**：BACKINGSHEET（Backing Sheet Element）；OVERLAY（Overlay Sheet Element）；SHEET（Sheet Element）；SHTMPL（Sheet Template Element）
- **Legal Members（合法子类型）**：ARC（Arc Element）；CIRCLE（Circle Element）；DIAMOND（Diamond Element）；ELLIPSE（Ellipse Element）；ETRIANGLE（Equilateral Triangle Element）；HEXAGON（Hexagon Element）；MARKPRIMITIVE（Marker Element）；OUTLINE（Outline Element）；PRIM（Primitive Element）；RECTANGLE（Rectangle Element）；STRAIGHT（Straight Line Element）；SYMBOL（Symbol Instance Element）；TABLE（Table Element）；TEXTPRIMITIVE（Multi-line Text Element）

---

## TEXP（Multi-line Text，多行文本（Text Primitive））— DMRM §6.1.103 ｜ PDF 第548页 ｜ 印刷页 6:68

> [推断] 手册章节名为 **Multi-line Text Element (TEXTPRIMITIVE)**；PML 短码 TEXP 由 DRAFT User Guide 佐证
>
> 层级标签（原书）：Draft 2D Drafting Element

共 6 条属性。

| 属性（Ch4 显示名） | DB 属性名（Ch16） | 类型 | 说明（原书） |
|---|---|---|---|
| Name ◊ | NAME | string(500) | Name of the element |
| SpPurpose ◊ | SPPURP | word | Special purpose table attribute |
| Function ◊ | FUNC | string(120) | Function |
| Purpose ◊ | PURP | word | Description code word |
| Stext ◊ | STEX | string(2000) | S Text string |
| Orrf ◊ | ORRF | element | Origin reference (for templates) |

- **Legal Owners（合法父类型）**：NOTE（Sheet Note Element）；SYTM（Symbol Template Element）；VNOTE（View Note Element）
- **Legal Members（合法子类型）**：NONE（None）

---

## LDIM（Linear Dimension，线性标注）— DMRM §6.1.55 ｜ PDF 第517页 ｜ 印刷页 6:37

> [推断] 手册章节名为 **Linear Dimension Element (LDIMENSION)**；PML 短码 LDIM 由 DRAFT User Guide 佐证
>
> 层级标签（原书）：Draft Dimensioning Element

共 18 条属性。

| 属性（Ch4 显示名） | DB 属性名（Ch16） | 类型 | 说明（原书） |
|---|---|---|---|
| Name | NAME | string(500) | Name of the element |
| ACLayer | ACLAYE | string(120) | AutoCAD layer name |
| Criteria | CRIT | integer(250) | Selection criteria (used to define tag & rep. rules) |
| SpPurpose | SPPURP | word | Special purpose table attribute |
| Function | FUNC | string(120) | Function |
| Tlindicator | TLIN | logical | True length indicator |
| Direction | DIR | dir | Direction |
| Ddname | DDNM | element | Design element reference |
| Ppdirection | PPDI | integer | Ppoint number for direction |
| Pkey | PKEY | word | Pline identifier key |
| Doffset | DOFF | real | Dimension line offset |
| Dposition | DPOS | pos | Dimension line/arc position |
| Pldirection | PLDI | real(3) | Projection line direction |
| Lchain | LCHA | logical | Chain flag |
| Dmspacing | DMSP | real | Lower limit to spacing between parallel dimensions |
| Truncate | TRUN | real | Truncation value (+ve) or percentage (-ve) |
| Tsize | TSIZ | real | Terminator size |
| Dterminator | DTER | string | Dimension terminator code |

- **Legal Owners（合法父类型）**：LAYER（View Annotation Layer Element）
- **Legal Members（合法子类型）**：DPBA（Dimension Point - Before/After Command Element）；DPOINT（Dimension Point - Position Element）；DPPT（Dimension Point - Ppoint Element）

---

## VIEW（View，视图）— DMRM §6.1.108 ｜ PDF 第551页 ｜ 印刷页 6:71

> 层级标签（原书）：Draft View Element

共 34 条属性。

| 属性（Ch4 显示名） | DB 属性名（Ch16） | 类型 | 说明（原书） |
|---|---|---|---|
| NLColour | NLCOLO | integer | Note colour |
| Ppdirection | PPDI | integer | Ppoint number for direction |
| Name | NAME | string(500) | Name of the element |
| Direction | DIR | dir | Direction |
| Thposition | THPO | pos | Point through which viewing |
| Frposition | FRPO | pos | Eye point |
| Onposition | ONPO | real(2) | ONTO Point, position of view in the region |
| Vscale | VSCA | real | Viewing scale - scales projected view |
| Vratio | VRAT | real(2) | View ratio |
| Adegrees | ADEG | real | Orientation |
| Perspective | PERS | real | Perspective angle |
| Arctolerance | ATOL | integer | Arc tolerance |
| Vtype | VTYP | string | Type of design view |
| Idlname | IDLN | element | Drawlist name reference |
| Rrsf | RRSF | element | Rep ruleset reference |
| Hrsf | HRSF | element | Hatch ruleset reference |
| Crsf | CRSF | element | Change ruleset reference |
| Size | SIZE | real(2) | Sheet/region size |
| Xyposition | XYPS | pos | 2D Position |
| Rcode | RCOD | string | Direction of region vertical on sheet |
| Nlpen | NLPN | integer | Note/framing pen |
| Lframe | LFRA | logical | Frame flag |
| NLStyle | NLSTYL | integer | Note linestyle |
| Lvisibility | LVIS | logical | Visibility flag |
| Vgaplength | VGAP | real | View gap length |
| Smode | SMOD | string | Sectioning mode |
| Title | TITL | string(1000) | Title |
| Function | FUNC | string(120) | Function |
| Idlx | IDLX | string(120) | Drawlist name (as text) |
| Noclipview | NOCLIP | logical | View no clipping flag |
| PlinOn | PLINON | logical | Pline-required flag |
| Vwlimits | VWLIMI | real(6) | View Limits - special attribute for use by ADP |
| Dflta | DFLTA | string(1000) | Defaults for Type 1 annotation - special attribute for use by ADP |
| Dfltb | DFLTB | string(1000) | Defaults for Type 2 annotation - special attribute for use by ADP |

- **Legal Owners（合法父类型）**：OVERLAY（Overlay Sheet Element）；SHEET（Sheet Element）；SHTMPL（Sheet Template Element）
- **Legal Members（合法子类型）**：DSLAYER（View Symbology Layer Element）；HRULE（Hatch Rule Element）；HSVDEF（Hull Symbolic View Element）；LAYER（View Annotation Layer Element）；RRULE（Representation Rule Element）；TASK（Task Element）；VMSUBV（VM Subview Element）；VSECTION（View Section Element）

---

## SHEE（Sheet，图页）— DMRM §6.1.86 ｜ PDF 第537页 ｜ 印刷页 6:57

> 层级标签（原书）：Draft Drawing and Sheet Element / Primary Element

共 31 条属性。

| 属性（Ch4 显示名） | DB 属性名（Ch16） | 类型 | 说明（原书） |
|---|---|---|---|
| Name ◊ | NAME | string(500) | Name of the element |
| Spsf ◊ | SPSF | element | Sheet pointset reference |
| Exfile ◊ | EXFI | integer | Extract file number |
| Arno ◊ | ARNO | integer | Picture directory area number |
| Pvno ◊ | PVNO | integer | Picture version number |
| Size ◊ | SIZE | real(2) | Sheet/region size |
| Bsrf ◊ | BSRF | element | Backing sheet reference |
| Idlname ◊ | IDLN | element | Drawlist name reference |
| TTFenabled ◊ | TTFENA | logical | TrueType fonts enabled flag |
| Layarf ◊ | LAYARF | element | Annotation Layer ruleset reference |
| Laydrf ◊ | LAYDRF | element | Design Layer ruleset reference |
| Bsfname ◊ | BSFN | string(1024) | Backing sheet filename |
| BSDWG ◊ | BSDWG | string(120) | AutoCAD backing sheet name |
| Title ◊ | TITL | string(1000) | Title |
| Idlx ◊ | IDLX | string(120) | Drawlist name (as text) |
| Acpicture ◊ | ACPICT | string | AutoCAD picture flag |
| ACScale ◊ | ACSCAL | real | AutoCAD picture scale factor |
| BSLayer ◊ | BSLAYE | string(120) | AutoCAD backing sheet layer |
| ACDWT ◊ | ACDWT | string(120) | AutoCAD drawing template name |
| ACDATE ◊ | ACDATE | string(50) | Date last modified in AutoCAD |
| ACLock ◊ | ACLOCK | string | AutoCAD picture lock |
| Adprfarray ◊ | ADPRFA | element(500) | ADP reference array |
| Posformat ◊ | POSFOR | string | Intelligent Text positional code word expansion style |
| Grsystem ◊ | GRSYS | element | Grid system reference |
| SpPurpose ◊ | SPPURP | word | Special purpose table attribute |
| Function ◊ | FUNC | string(120) | Function |
| DArRef ◊ | DARREF | element | Design area reference |
| LinkRef ◊ | LINKRE | element | Link reference |
| PlinOn ◊ | PLINON | logical | Pline-required flag |
| PFReqd ◊ | PFREQ | logical | Picture file required flag |
| Marptype ◊ | MARPTY | integer | Marine picture type |

- **Legal Owners（合法父类型）**：DRWG（Drawing Element）
- **Legal Members（合法子类型）**：IMGELE（IMGELE Element）；NOTE（Sheet Note Element）；OLAYER（Overlay Element）；PLLB（Plane Library Element）；REVISION（Revision Element）；TASK（Task Element）；VIEW（View Element）；VMSUBV（VM Subview Element）

---

## DRWG（Drawing，图纸）— DMRM §6.1.26 ｜ PDF 第499页 ｜ 印刷页 6:19

> 层级标签（原书）：Draft Drawing and Sheet Element / Primary Element

共 32 条属性。

| 属性（Ch4 显示名） | DB 属性名（Ch16） | 类型 | 说明（原书） |
|---|---|---|---|
| FColour | FCOLOUR | integer | Fill colour |
| Posformat | POSFOR | string | Intelligent Text positional code word expansion style |
| Grsystem | GRSYS | element | Grid system reference |
| SpPurpose | SPPURP | word | Special purpose table attribute |
| Function | FUNC | string(120) | Function |
| PlinOn | PLINON | logical | Pline-required flag |
| Name | NAME | string(500) | Name of the element |
| Date | DATE | string(12) | Date |
| Clrf | CLRF | element | Actual circulation list reference |
| Idlname | IDLN | element | Drawlist name reference |
| Rrsf | RRSF | element | Rep ruleset reference |
| Hrsf | HRSF | element | Hatch ruleset reference |
| Crsf | CRSF | element | Change ruleset reference |
| Layarf | LAYARF | element | Annotation Layer ruleset reference |
| Laydrf | LAYDRF | element | Design Layer ruleset reference |
| Size | SIZE | real(2) | Sheet/region size |
| Font | FONT | integer | Text font |
| Tpen | TPEN | integer | Text pen |
| Ucode | UCOD | integer | Units code |
| Llpen | LLPN | integer | Label leader pen |
| Lfpen | LFPN | integer | Label frame pen |
| Plpen | PLPN | integer | Projection line pen |
| Dlpen | DLPN | integer | Dimension line pen |
| Fpen | FPEN | integer | Fill pen |
| Nlpen | NLPN | integer | Note/framing pen |
| Dterminator | DTER | string | Dimension terminator code |
| Lterminator | LTER | string | Label terminator code |
| Bsrf | BSRF | element | Backing sheet reference |
| Bsfname | BSFN | string(1024) | Backing sheet filename |
| BSDWG | BSDWG | string(120) | AutoCAD backing sheet name |
| BSLayer | BSLAYE | string(120) | AutoCAD backing sheet layer |
| ACDWT | ACDWT | string(120) | AutoCAD drawing template name |

- **Legal Owners（合法父类型）**：REGISTRY（Registry Element）
- **Legal Members（合法子类型）**：LIBY（Library Element）；REVISION（Revision Element）；SHEET（Sheet Element）；TASK（Task Element）

---

## LAYER（View Annotation Layer，视图注释层）— DMRM §6.1.51 ｜ PDF 第514页 ｜ 印刷页 6:34

> 层级标签（原书）：Draft Drawing Layer or Note Element

共 69 条属性。

| 属性（Ch4 显示名） | DB 属性名（Ch16） | 类型 | 说明（原书） |
|---|---|---|---|
| FStyle | FSTYLE | integer | Fill style |
| FColour | FCOLOUR | integer | Fill colour |
| SpPurpose | SPPURP | word | Special purpose table attribute |
| Function | FUNC | string(120) | Function |
| Name | NAME | string(500) | Name of the element |
| ACLayer | ACLAYE | string(120) | AutoCAD layer name |
| Lycol | LYCOL | integer | AutoCAD Layer Colour |
| Lypsty | LYPSTY | string(120) | AutoCAD Layer Plotter Style |
| Lyltyp | LYLTYP | string(120) | AutoCAD Layer LineType |
| Lylwt | LYLWT | real | AutoCAD Layer LineWeight |
| Lyfrze | LYFRZE | logical | AutoCAD Layer Freeze flag |
| Lylock | LYLOCK | logical | AutoCAD Layer Lock flag |
| LyVisibility | LYVIS | logical | AutoCAD Layer Visibility Flag |
| Lypfg | LYPFG | logical | AutoCAD Layer Plotting flag |
| Lynvfr | LYNVFR | logical | AutoCAD Layer New Viewport Freeze |
| Lycvfr | LYCVFR | logical | AutoCAD Layer Current Viewport Freeze |
| Lvisibility | LVIS | logical | Visibility flag |
| Purpose | PURP | word | Description code word |
| Nlpen | NLPN | integer | Note/framing pen |
| Ucode | UCOD | integer | Units code |
| Font | FONT | integer | Text font |
| Tpen | TPEN | integer | Text pen |
| Fpen | FPEN | integer | Fill pen |
| Lterminator | LTER | string | Label terminator code |
| Justification | JUST | string | Justification |
| Alignment | ALIGN | string | Vertical alignment |
| Plpen | PLPN | integer | Projection line pen |
| Dlpen | DLPN | integer | Dimension line pen |
| Llpen | LLPN | integer | Label leader pen |
| Lfpen | LFPN | integer | Label frame pen |
| Dterminator | DTER | string | Dimension terminator code |
| Tsize | TSIZ | real | Terminator size |
| Mpen | MPEN | integer | Marker pen |
| Chpen | CHPN | integer | Crosshairs pen |
| Chosht | CHOS | real | Crosshairs overshoot |
| Asubtended | ASUB | real | Angle subtended |
| Pjustification | PJUS | string | Projection line text justification |
| Overshoot | OSHT | real | Overshoot |
| Plclearance | PLCL | real | Projection line clearance |
| Doffset | DOFF | real | Dimension line offset |
| Dmspacing | DMSP | real | Lower limit to spacing between parallel dimensions |
| Direction | DIR | dir | Direction |
| Cheight | CHEI | real | Character height |
| Lleader | LLEA | logical | Leader line flag |
| Lframe | LFRA | logical | Frame flag |
| Lshape | LSHA | string | Leader shape code |
| Gbox | GBOX | real | Box gap |
| Cspacing | CSPA | real | Character spacing factor |
| Lspacing | LSPA | real | Text line spacing factor |
| Llclearance | LLCL | real | Leader line clearance |
| Xyscale | XYSC | real(2) | Label XY size |
| Xyposition | XYPS | pos | 2D Position |
| Bpoffset | BPOF | real(4) | Leader bend point offset |
| Blnk | BLNK | logical | Auto-blanking flag |
| Bmargin | BMAR | real | Auto-blanking margin |
| Trsf | TRSF | element | Tag ruleset reference |
| Fterminator | FTER | string | First dimension terminator code |
| Pcode | PCODE | integer | Precision code |
| Ntext | NTEXT | string(12) | Null text |
| Txcolour | TXCOLO | integer | Text colour |
| NLStyle | NLSTYL | integer | Note linestyle |
| NLColour | NLCOLO | integer | Note colour |
| LLStyle | LLSTYL | integer | Label leader linestyle |
| LLColour | LLCOLO | integer | Label leader colour |
| LFStyle | LFSTYL | integer | Label frame linestyle |
| LFColour | LFCOLO | integer | Label frame colour |
| DLStyle | DLSTYL | integer | Dimension linestyle |
| DLColour | DLCOLO | integer | Dimension line colour |
| PLStyle | PLSTYL | integer | Projection linestyle |

- **Legal Owners（合法父类型）**：VIEW（View Element）
- **Legal Members（合法子类型）**：ADIMENSION（Angular Dimension Element）；ANNRLR（Annotation Ruler Element）；AXESYMBOL（Axes Symbol Instance Element）；GLABEL（General Label Element）；LDIMENSION（Linear Dimension Element）；PDIMENSION（PCD Radial Dimension Element）；POSRLR（Position Ruler Element）；RDIMENSION（Radial Dimension Element）；SLABEL（Special Label Instance Element）；TAGRULE（Tagging Rule Element）；TASK（Task Element）；VNOTE（View Note Element）

---

## SKEY（Symbol Key，符号键）— DMRM 未收录（无元素类型章节）

- DMRM 全文不存在 `(SKEY)` 元素类型章节（0 命中）；`SKEY` 在本手册中**只作为属性出现**：
  `SKEY string(4) "Symbol key"`（第 16 章属性字典，印刷页 16:79 / PDF 第799页），
  即各类目录件/设计元素上的符号键引用（4 字符代码，如管道元件的二维符号键）。
- 相关元素：`FMWSK`（Fabrication Machine Welding Skey Element，§4.22.8，印刷页 4:232）为船厂焊接符号键，
  以及 Draft 侧 `BKEY`（"DRAFT user defined base symbol/skey name"）。
- 若需 SKEY 元素本身的定义（符号库表），需查阅 IMPOST/Draft 符号库相关手册，DMRM 未覆盖。

---

## POSITION（定位）— DMRM 未收录（无元素类型章节）

- DMRM 全文不存在 `(POSITION)` 元素类型章节（0 命中）。Positioning 在数据模型中通过**属性**而非独立元素表达：
  通用属性 `POS`（pos 类型，"Position"，第 16 章属性字典）出现在几乎所有几何/设备类元素上（本表 EQUI/STRU/BOX 等）。
- DMRM 中的相关"位置类"元素/章节（非 PML 短码 POSITION）：
  - `PTPOS`（Ppoint with Position Element，§2.1.64，目录库，印刷页 2:35）
  - `WPOS`（Point given as 3D Position Element，§6.1.115，Draft 库，印刷页 6:76）
  - `DPOINT`（Dimension Point - Position Element，§6.1.22）/ `RPOINT`（Radial Dimension Point - Position，§6.1.81）
  - 第 15 章属性类别 "Attribute Category: Positional"（印刷页 15:44）
- 若 PML 源码中的 `NEW POSITION` 指向 Marine Hull/其他 Marine 专用库的 POSITION 元素，则不在本 DMRM 范围内。

---

## SUBS（Substructure，子结构）— DMRM §4.32.40 ｜ PDF 第447页 ｜ 印刷页 4:343

> [推断] 手册章节名为 **Substructure Element (SUBSTRUCTURE)**；PML 短码 SUBS 为其 4 字符缩写。
>
> 层级标签（原书）：Structural Element / Primary Element

共 27 条属性。

| 属性（Ch4 显示名） | DB 属性名（Ch16） | 类型 | 说明（原书） |
|---|---|---|---|
| Grade | GRADE | real | Steel grade |
| Ispec | ISPE | element | Insulation spec reference |
| Firesistance | FIRE | real | Fire resistance |
| Inref | INRE | element | Insulation reference |
| Spref | SPRE | element | Component spec reference |
| Jfree | JFRE | logical | True if Section position dominates a connection |
| Matref | MATR | element | Material reference |
| Orrf | ORRF | element | Origin reference (for templates) |
| Bevcodes | BEVCOD | real(10) | Bevel codes for edges |
| Excess | EXCESS | real | Excess |
| Name | NAME | string(500) | Name of the element |
| Description | DESC | string(120) | Description of the element |
| Function | FUNC | string(120) | Function |
| Purpose | PURP | word | Description code word |
| Number | NUMB | integer | Number |
| Area | AREA | integer | Area |
| Usrweight | USRWEI | integer(500) | User entered weight value |
| Usrwweight | USRWWE | integer(500) | User entered wet weight value |
| Usrcogravity | USRCOG | integer(500) | User centre of gravity position |
| Usrwcogravity | USRWCO | integer(500) | User wet centre of gravity position |
| Uwmtxt | UWMTXT | string(120) | User weight Manager text |
| Position | POS | pos | Position |
| Orientation | ADEG | real | Orientation |
| Built | BUIL | logical | Built/Unbuilt flag |
| Shop | SHOP | logical | Shop/Site flag |
| Length | LENG | real | Length |
| DUnion | DUNION | integer | DRAFT element union detail flag |

- **Legal Owners（合法父类型）**：STRUCTURE（Structure Element）
- **Legal Members（合法子类型）**：BOX（Box Element）；CONE（Cone Element）；CTORUS（Circular Torus Element）；DDSE（Cylinder Element (CYLINDER)Design Dataset Element）；DISH（Dish Element）；DPSET（Design Ppoint/Pline Set Element）；DRAWING（Drawn Line Element）；EXTRUSION（Extrusion Element）；PANEL（Panel Element）；POHEDRON（Polyhedron Element）；POLYHEDRON（Polyhedron Element）；PVOLUME（Penalty or Preferred Volume Element）；PYRAMID（Pyramid Element）；REVOLUTION（Revolution Element）；RPLANE（Routing Plane Element）；RTORUS（Rectangular Torus Element）；SLCYLINDER（Slope Bottom Cylinder Element）；SNOUT（Snout Element）；TEXT（Text Element）；TMPLATE（Template Element）

---

# 统计

## 1. 提取完成情况（30 类）

| # | PML 短码 | 手册记名 | 章节 | PDF页 | 印刷页 | 属性数 | 父类型数 | 子类型数 |
|---|---|---|---|---|---|---|---|---|
| 1 | EQUI | Equipment (EQUIPMENT) | 4.8.2 | 194 | 4:90 | 33 | 1 | 25 |
| 2 | BRAN | Branch (BRANCH) | 4.23.1 | 336 | 4:232 | 74 | 2 | 51 |
| 3 | PIPE | Pipe (PIPE) | 4.23.4 | 342 | 4:238 | 43 | 1 | 5 |
| 4 | STRU | Structure (STRUCTURE) | 4.32.37 | 443 | 4:339 | 25 | 1 | 32 |
| 5 | SCTN | Structural Section (SCTN) | 4.32.31 | 438 | 4:334 | 29 | 5 | 9 |
| 6 | GENSEC | Structural Generic Section (GENSEC) | 4.32.13 | 419 | 4:315 | 38 | 22 | 6 |
| 7 | BOX | Box (BOX) | 4.25.1 | 349 | 4:245 | 21 | 8 | 12 |
| 8 | CYLI | Cylinder (CYLINDER) | 4.25.4 | 354 | 4:250 | 11 | 8 | 12 |
| 9 | NOZZ | Nozzle (NOZZLE) | 4.8.3 | 196 | 4:92 | 23 | 3 | 3 |
| 10 | FLAN | Flange (FLANGE) | 4.21.12 | 310 | 4:206 | 41 | 1 | 1 |
| 11 | VALV | Valve (VALVE) | 4.21.25 | 326 | 4:222 | 49 | 1 | 1 |
| 12 | TEE | Tee (TEE) | 4.21.22 | 323 | 4:219 | 41 | 1 | 1 |
| 13 | REDU | Reducer (REDUCER) | 4.21.19 | 319 | 4:215 | 35 | 1 | 1 |
| 14 | ELBO | Elbow (ELBOW) | 4.21.9 | 306 | 4:202 | 35 | 1 | 1 |
| 15 | ATTA | Attachment Point (ATTACHMENT) | 4.21.1 | 295 | 4:191 | 59 | 1 | 1 |
| 16 | SLAB | 未收录 | — | — | — | 0 | — | — |
| 17 | PLAT | Plate (PLATE) | 4.16.13 | 271 | 4:167 | 38 | 1 | 1 |
| 18 | EXTR | Extrusion (EXTRUSION) | 4.25.7 | 358 | 4:254 | 10 | 8 | 13 |
| 19 | LOOP | Loop (LOOP) | 4.25.9 | 359 | 4:255 | 4 | 9 | 1 |
| 20 | VRTX | Vertex (VRTX) | 6.1.112 | 554 | 6:74 | 17 | 1 | 1 |
| 21 | NOTE | Sheet Note (NOTE) | 6.1.62 | 522 | 6:42 | 19 | 4 | 14 |
| 22 | TEXP | Multi-line Text (TEXTPRIMITIVE) | 6.1.103 | 548 | 6:68 | 6 | 3 | 1 |
| 23 | LDIM | Linear Dimension (LDIMENSION) | 6.1.55 | 517 | 6:37 | 18 | 1 | 3 |
| 24 | VIEW | View (VIEW) | 6.1.108 | 551 | 6:71 | 34 | 3 | 8 |
| 25 | SHEE | Sheet (SHEET) | 6.1.86 | 537 | 6:57 | 31 | 1 | 8 |
| 26 | DRWG | Drawing (DRWG) | 6.1.26 | 499 | 6:19 | 32 | 1 | 4 |
| 27 | LAYER | View Annotation Layer (LAYER) | 6.1.51 | 514 | 6:34 | 69 | 1 | 12 |
| 28 | SKEY | 未收录 | — | — | — | 0 | — | — |
| 29 | POSITION | 未收录 | — | — | — | 0 | — | — |
| 30 | SUBS | Substructure (SUBSTRUCTURE) | 4.32.40 | 447 | 4:343 | 27 | 1 | 20 |

- **找到并提取：27 类**（Ch4 Design 库 19 类：EQUI BRAN PIPE STRU SCTN GENSEC BOX CYLI NOZZ FLAN VALV TEE REDU ELBO ATTA PLAT EXTR LOOP SUBS；Ch6 Draft 库 8 类：VRTX NOTE TEXP LDIM VIEW SHEE DRWG LAYER —— 计 19+8=27）
- **未收录：3 类**（SLAB、SKEY、POSITION；SLAB 已附推断映射 SLABEL 的参考表）
- **27 类合计属性行数：862**（每类节内去重后求和；跨类型重复属性分别计入各类）

## 2. 跨类型共用属性 Top 20

按"属性显示名（不区分大小写）在 27 个类型表中出现的类型数"排序：

| 排名 | 属性名 | 出现类型数 |
|---|---|---|
| 1 | name | 27 |
| 2 | orrf | 18 |
| 3 | function | 17 |
| 4 | position | 16 |
| 5 | orientation | 15 |
| 6 | ispec | 14 |
| 7 | purpose | 14 |
| 8 | built | 14 |
| 9 | shop | 12 |
| 10 | desparam | 11 |
| 11 | description | 10 |
| 12 | spref | 10 |
| 13 | isohidden | 9 |
| 14 | tspec | 9 |
| 15 | ptnbarray | 8 |
| 16 | spsp | 8 |
| 17 | tsfbreak | 8 |
| 18 | cref | 8 |
| 19 | height | 7 |
| 20 | invfarray | 7 |

## 3. 解析问题与置信度说明

1. **PDF 两栏串行（最主要问题）**：DMRM 原版为"属性表 + Description + Legal Owners/Members"同页混排，
   PDF 文本提取时常把同一类型属性表的尾部读到 owners/members 区带、或把表头块读到下一页。
   本表采用"节内并集 + 去重 + 按出现区带标注 ◊"的策略：凡带 ◊ 的行来自 owners/members 区带，
   绝大多数为本类型表格的跨页延续（已抽样与原书逐行核对一致），但个别行不排除属于相邻类型（如 EQUI 的
   Invfarray/Inprtref/Ouprtref 同时出现在 NOZZLE 表中），使用前可按页码回查。
2. **PDF 随机空格**：原文存在单词内断字（如 "Structural Generic Section" 提取为两行、"(CYLINDER)Design" 两栏粘连），
   已做拼接与粘连拆分处理；无法复原处已丢弃并记入 WARN（未混入属性表）。
3. **类型列的对应关系**：Ch4 各节使用属性"显示名"（如 Pspec、Smaximum），第 16 章字典使用 DB 属性名（如 PSPE、SMAX）。
   本表通过"说明文字精确匹配（97% 说明文字在字典中唯一）+ 属性名匹配"建立对应，匹配失败者类型列记 `—`
   （如 BRANCH 的 Inco、管件类的 Cmpx、ATTA 的 Laxes 等 3 处）。
4. **手册自身瑕疵**：原书存在重复行（如 BOX 的 Legal Owners 两次列出 SVOLMODEL、EQUI 属性表重复 Orrf/Stmf/Desparam/Ispec），
   以及 POHEDRON/POLYHEDRON 两种拼写并存；本表按原书保留首次出现、合并重复，成员表保留原书两种拼写。
5. **短码映射推断**：DMRM 用全名记类型（EQUIPMENT/BRANCH/CYLINDER/ATTACHMENT/SUBSTRUCTURE/SLABEL/TEXTPRIMITIVE/LDIMENSION），
   与 PML 4 字短码的对应关系除本表标注 [推断] 的 TEXP/LDIM/SLAB/SUBS 外，均为 PDMS 通用常识性对应
   （EQUI/BRAN/STRU/CYLI/NOZZ/FLAN/VALV/REDU/ELBO/ATTA 等，DRAFT User Guide 与 Marine PML 语料可交叉印证）。
6. **未收录类型的去向**：SLAB（Draft 特殊标注→SLABEL §6.1.89；或 Marine 船体板架，不在本手册）、
   SKEY（仅作为 string(4) 属性）、POSITION（以 POS 属性 + WPOS/DPOINT/PTPOS 等元素表达）——
   三者均建议到 Marine Hull/Draft 专门手册进一步查证。
