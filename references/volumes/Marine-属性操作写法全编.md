# Marine 元素属性操作写法全编（穷举级·6075 文件全树统计）

> 来源：PMLLIB 全树 6075 文件（.pmlfnc 3703 / .pmlfrm 1380 / .pmlobj 988 / 其他 4）并行扫描统计 + 关键文件精读。
> 每类给出全量属性名/写法清单与真实示例（带路径行号）。
> 检索基址：`E:\AVEVA\Marine\OH12.1.SP4\PMLLIB\`。

---

## 总览：四层写法体系

| 层级 | 写 | 读 | 复位 | 判定 |
|---|---|---|---|---|
| PML2 属性 | `!!ce.attr = v` / `!o.attr = v` | `!!ce.attr`、`attr of $!x` | **无 `= unset`**；仅命令式/哨兵 `'unset'` | `.unset()` `.objectType()` |
| PML2 UDA | `!o.:UDA = v` | `!o.:UDA` | 走命令式 | `.:UDA.unset()` |
| 命令宏 | `:UDA v` / `ATTR v` / `NEW T attr...` | `q :uda`、`var !x EVAL attr`、`:uda of $!e` | `:UDA unset/default/def/nulref`、`ATTR unset` | `if :UDA then`、`WI :uda eq ...` |
| UDA 定义 | `NEW UDA`+`UDNA/UTYP/ULEN/ABLE/ELEL/DFLT` | — | `OLD UDA`+`ULEN` | `handle (2,109)` |

---

## 1. PML2 属性直写

### 1a. `!!ce.属性 = 值`（当前元素直写）——1751 处，296 个不同属性名

**频次全表（≥10 次的 29 个）**：
`name(179) position(124) description(91) spref(84) desc(64) pos(52) height(46) drne(39) drns(39) pose(38) purpose(38) poss(36) tdir(29) tpos(26) number(21) orientation(19) function(19) purp(17) lstu(17) posref(15) hdir(14) desp(14) zdistance(13) frad(13) ori(13) func(12) lsrod(12) bang(12) spre(10)`

**中频（2-9 次，全量）**：
- 9 次：`cposition rflag zdist ddnm hpos amemrf grdoff grdid`
- 8 次：`hbor obs grdaxe`
- 7 次：`tmrf posline ppro tbor cutb btext`
- 6 次：`grdlbl nppt cpos radi title date catref asstar ddproperty cutplane angle tconn author`
- 5 次：`firerating gtyp href attyp sjustification vsca size tbore dpro wthickness lstube jusl`
- 4 次：`atext validvalue matref radius od radsetf linkref cref idna stext staref`
- 3 次：`bore llea loff bangle endelevation tdefault adeg dkey bradius diameter dtitl stfconstant awdfln valrule stfproportional heig ddname stoucd hbore atex endref xoffset stincd despara`
- 2 次（63 个）：`rinside routside ispe excess ydirection oset spkbrk yoffset tref dbottom hpref sppurp heigh intsen pspe gtype stourf paspec tposition stinrf btex cutp fllthk hconn llead jusline posl gangle fradius sjus tmpref asstmpreference twidth rise staelevation cttype uextns gxyoffset curtyp grdxspacing grdyspacing bulgef pritype szdis numb fltdirection fthickness angspb skey tanswer lactive maxlp mtoref dtop matn headroom area mliflange grip mleflange fcmeasure prtref angspa lrise`
- 1 次（126 个）：`descr rtext fstatus fissue xlen ylen anstype lhide dtitle dddfault attset question tquestion zlen stex default insuref ckey pltx prtreference maxslope minslope cthick lfpn ddnam dtit idln ptyp tpen pkey pkdi defslope cmpref hcon tcon lock finputby sptype bltref rtex nlpn bmar minvert sectype posli matxt detref olength asstmp temperature zoffset xoff angl zdis bndoff thickness duty maxod minod xlength minlp bmcloc dconnect pressure compensate pskey instoptions aslsta asstmpref elevation aslsbs ezdis tangoffset postspacing epostoffset closeflag extref lextnsion uextnsion lcutdirection ucutdirection ogoing cagoff cagsiz orise sigref ylength endpoint stapoint delp rntype tierheight lgap igap trayh trayw nappflag lmerex dir hstu spkchg vscale width depth ydir wjusline fgap ytshear xtshear ybshear xbshear ybottom xtop zlength xbottom ytop tolerance colschema pkdis ctspe markrf railheight nolnkpropagation thickn cellid joie`

**高频属性真实示例**：
```pml
!!ce.name = !name                        -- accommodation\forms\accceilinggriddefinition.pmlfrm:4014
!!ce.position = !edges[!i].startposition -- :3745
!!ce.description = !description          -- accommodation\forms\accdetail.pmlfrm:937
!!ce.spref = !this.profileSPREF.val.dbRef()  -- accceilinggriddefinition.pmlfrm:3744
!!ce.pos = !this.plane.plane.position    -- accflrcoverdefinition.pmlfrm:3371
!!ce.height = !this.clnThk               -- accommodation\objects\accceilingbasics.pmlobj:232
!!ce.height = 10mm                       -- asl\objects\aslstrfltdata.pmlobj:244（字面量带单位）
!!ce.drne = !endDir / !!ce.drns = !endDir.opposite()  -- design\forms\splitgensectpane.pmlfrm:1311/1303
!!ce.pose = !intrsctn1 / !!ce.poss = ... -- splitgensectpane.pmlfrm:1309
!!ce.purpose = !purpose                  -- accdetail.pmlfrm:938
!!ce.purp = 'FABR'                       -- asl\forms\aslfabricatorstandards.pmlfrm:140
!!ce.tdir = !direction                   -- design\forms\hvacposition.pmlfrm:450
!!ce.tpos = !newBranch.hpos              -- design\forms\pipesplitting.pmlfrm:3187
!!ce.tbor = !!ce.hbor                    -- design\forms\specborechange.pmlfrm:990
!!ce.hBore = !this.bore                  -- design\objects\branchconnection.pmlobj:317（大小写混用合法）
!!ce.catref = !this.nozzSpecRef          -- design\forms\equmeicreatenozzle.pmlfrm:643
!!ce.matRef = !this.matRefSST.val.dbref()-- design\forms\fabmachinedat.pmlfrm:324
!!ce.intsen = TRUE                       -- asl\forms\aslmain.pmlfrm:8024
!!ce.xoff = !!ce.xoff * !this.xoffset    -- 表达式右值
!!ce.gtyp = !!ce.catr.gtyp               -- 链式右值
!!ce.matn = |$!insertNote|               -- 竖线嵌变量
!!ce.delp = !fixing.pos.wrt(worl)        -- WRT 位置
```

**流水线标准写法**（以对象中转再写 CE）：`!hpos = !currentBranch.tpos` → `!!ce.hpos = !currentBranch`（hvacassembly.pmlobj:1492-1500）。

**重要语法变体**：属性名可混用大小写（`!!ce.hBore`/`!!ce.hbore`）；4 字缩写型（`pkdi、lfpn、tpen、dtit`）与全拼型并存；UDA 成员可直写后接链 `!!ce.:PsiSystem[1].hconn`。

### 1b. `!对象.成员 = !值`（对象成员/属性赋值）——26472 处，4980 个不同成员名

前 120 高频（名称：次数）：
`position(1201) direction(675) support(629) description(475) val(460) name(424) endposition(373) startposition(354) type(350) up(332) directionb(323) directiona(321) north(231) east(226) datum(226) alias(219) replace(208) form(205) stru(200) backup(188) rotated(184) orientation(171) dtext(167) element(160) formtitle(156) spref(151) rtext(144) aidnumber(137) preliminarystore(114) material(105) bedplate1(105) current(105) plane(104) mode(100) radius(100) origin(97) number(94) currentancil(92) pos(82) size(76) currentpane(76) height(74) action(73) ce(71) dbref(68) supporterrors(68) joints(67) steelmem(67) bedplate2(64) profile(62) selectedbore(60) owner(59) function(59) purpose(56) drns(55) aidaxes(55) drne(53) file(51) offset(49) result(48) posref(47) refe(47) endangle(46) dbelement(46) currentelement(45) flangethk(44) pickpacket(43) wrt(41) callback(40) width(40) tpos(39) reference(39) from(38) prompt(38) mdsassoc(38) pose(38) mdsform(38) poss(37) to(36) pick1(36) sortval(36) zdistance(36) tdir(36) filterval(35) text(35) config(35) jusline(35) desc(34) units(34) arc(33) area(33) matref(33) datumorthdirs(33) ref(32) pipe(32) ancilerrors(32) component(32) main(31) angle(31) startangle(31) indiceofselectedbore(31) title(30) task(30) packs(29) flangewidth(29) currentsession(28) sctn(28) penetrated(27) active(27) bang(27) amemrf(27) tuberef(27) nangle(27) colour(26) sense(26) constantdirectionone(26) constantdirectiontwo(26) vendorform(26) view(26) purp(25) aidnumberouter(25) drawlist(25) currentnumber(25) dir(25) filename(24) gapvalue(24) gpartdata(24) rest(24) barlen(24)`

**判定要点**：DB 真属性（position/direction/description/spref/...）与 PML 对象成员（val/form/dtext/callback/...）混在同一模式；区分靠对象类型。

---

## 2. UDA 冒号语法

### 2a. 命令式 `:UDA 值`——4441 处，198 个不同 UDA 名

**写入形式全集（9 类）**：
```pml
:MDSCp1 '$!Support.Config;$!RCur;$!HCur;$!Support.Rotated;$!Mirror'   -- ① 字符串
:MDSXConn $!pick2                                                      -- ② 变量
:hxysize $!ductA $!ductB                                               -- ③ 带单位数值(可多值)
:MdsScale '$!SelectedScale'
:MDSRotated true                                                       -- ④ 布尔
if :MDSRotated then                                                    --   （可作条件）
:MDSAdp default                                                        -- ⑤ 复位 default
:MDSPackRef unset                                                      -- ⑥ 复位 unset
:Mdsbpref1 def                                                         -- ⑦ 复位缩写 def
:mdsbpref1 nulref                                                      -- ⑧ 置空引用
!maxBore = :MDSMaxBore of $!template                                   -- ⑨ of 读取
!supportype = :MDSSuppType                                             --    （当前元素读取）
```
VAR/COLLECT 内嵌：
```pml
var !bpref1 :BPREF1                                                    -- mdsigt20.pmlfnc:123
var !spools eval :mdsspool for all from !Sctns                         -- Mdsspool.pmlfrm:103
var !mdshanggroup :MDSHangGroup of /MDS/$!template                     -- Mdsfh01.pmlfrm:484
COLL ALL RECT WI SPPURP OF OWNE EQ 'RESERV' AND :FUNC EQ 'Revision'    -- assyreviblock.pmlobj:240
```
NEW 语句内联：`NEW SLAB ... ATEX |$!atex| :IdpBtex |$!angle|`（isocont.pmlfnc:227）。

**UDA 名频次 Top60**：
`MDSCP1(380) MDSSUPPTYPE(348) MDSATTAREF(343) MDSCONN(226) MDSANCREF(209) MDSGUIDEREF(171) MDSPACKREF(156) MDSONUM(140) MDSBPREF1(137) MDSBARS(128) MDSCHECK(112) MDSSUPPFUNC(104) MDSTRUN(96) MDSOLAP(96) MDSMATREF(96) ISOSHIPCOORD(81) MDSBPREF2(72) MDSSREF(66) MDSFRAMIRROR(63) USTHCFGKEY(57) MDSBUILDSTYL(55) MDSTMPLORI(55) MDSDYNOFFSET(49) MDSORIGIN(38) MDSADP(37) MDSCIVREF(34) MDSMINBORE(33) MDSMAXBORE(33) MDSHV(33) MDSWELDDATA(29) MDSPCONN(29) MDSPAD(29) MDSNUDGEDIST(27) MDSCOMMENT(27) USTMOVEMENT(26) MDSACTIVE(26) USTTESTLOAD(26) MDSHCONFIG(24) MDSPIPEMAT(23) MDSFRAMEDIR(22) PFILOOSE(20) MDSRANGE(20) USTNUTREF(17) MDSPOSNUM(17) IDPDESC(16) PFILEXCESS(16) MDSXCONN(15) MDSCPLWEIGHT(14) MDSCONNECT(14) USTSPRRATE(14) MDSWELDSIZE(14) MDSMOVEX(13) MDSHLOAD(13) USTFORCES(13) MDSLOAD(13) USTDISTROD(13) MDSMOVEZ(13) MDSMOVEY(13) MDSSIZETAG(12) MDSPLATE(11)`

**命名规律**：MDS 前缀（ Marine 支吊架）、UST 前缀（支承弹簧）、IDP 前缀（出图）、PFI（松套法兰）、UST/PSI（应力）、AVINT（集成器）。

### 2b. PML2 成员式 `!引用.:UDA`——4539 处

```pml
!this.value.val = !this.viewname.:cdlimits.real()      -- 读  aba\Forms\abaextendarea.pmlfrm:31
!this.viewname.:cdlimits = !this.value.val.string()    -- 写  :40
!testForUpdate = !!ce.:ABAUpdate                       -- aba\Objects\abaview.pmlobj:166
!spool.:HSVLD = !approve                               -- design\forms\hvacspool.pmlfrm:1595
!xslap = !prev.:hxysize[1]                             -- chkhvaccompsizs.pmlfnc:129（取下标）
!result = !entry.:TREAT.part(2,',')                    -- pipespoolcalcexpr.pmlfnc:82（字符串方法链）
!number = (!sytmRefe.:End - !prevRefe.:End) / 2        -- assyreviblock.pmlobj:131（参与运算）
!!ce.hconn = !!ce.:PsiSystem[1].hconn                  -- psi\design\objects\stressgroup.pmlobj:2870（链式）
```
Top：`.:mdsguideref(361) .:mdssupptype(290) .:mdsconn(278) .:mdscp1(207) .:mdshconfig(199) .:mdscivref(165) .:mdsolap(164) .:mdsbpref1(159) .:mdsancref(145) .:mdspackref(141) .:mdstrun(130) .:mdsattaref(115) .:mdscheck(115) .:usthcfgkey(108) .:mdsframirror(105) .:mdsonum(95) .:ustforces(82) .:mdsbpref2(81) .:mdsrotdir(76) .:mdssref(71) .:mdsmatref(70) .:mdspipemat(70) .:mdstmplori(70) .:mdsposnum(64) .:psisystem(19) .:paint(12)`

### 2c. UDA 定义命令（integrator\functions\integratorUDAs.pmlfnc 全文）

```pml
NEW UWRLD /AVEVA/INTEGRATOR/UWRL
NEW UGROUP ...
NEW UDA /ACCEPT2D3DDIFFERENCE
  UDNA 'ACCEPT2D3DDIFFERENCE'    -- 名称
  ABLE 20                        -- 长度
  UTYP LOG|TEXT                  -- 类型
  ULEN 16|120                    -- 文本长
  ELEL ADD CYMLNK GPITEM GPSET   -- 适用元素
  DFLT FALSE|TRUE                -- 默认值
  END
-- 改定义：OLD UDA /xxx + ULEN 16 + END
-- 存在性探测：handle (2,109) 捕获"名称未定义"
```

---

## 3. NEW 语句后的属性命令词

NEW 共 21785 处。元素类型 Top（共约 400 种）：`TEXTPRIMITIVE(1904) STRAIGHT(1373) DATA(1271) TKPARA(1030) TEXP(959) ATTA(461) SYTM(420) POSITION(265) VRTX(240) LAYER(230) SVERTEX(216) SUPPORTS(203) TASK(199) SCTN(156) ELEMENT(151) DTSE(144) NAME(138) FRMW(122) NOTE(118) SLAB(118) VIEW(108) STRU(106) BRAN(103) LDIM(101) BRANCH(96) LAYE(83) DDAT(79) SUBS(78) REDU(64) PLAT(66) VNOTE(60) TXTM(58) TRUNNION(58) POINSP(54) TEE(53) GLAB(51) FITT(47) GRIDLN(47) DRAWING(45) SPINE(44) LALB(44) RRUL(43) FIXING(42) DPOI(42) SBFI(42) GENSEC(41) UDA(41) CIRCLE(40) RECTANGLE(40) TMPL(40) HANGER(37) RPATH(33) DATUM(33) WELD(30) OLET(22) VESSEL(20) ROOM(20) PIPE(20) LIBY(20) SHTMPL(20) DRTMPL(20) BEND(18) IDLI(18) SPRING(18) ...`

**属性命令词全表（≥5 次）**：
`ORIGIN(3658) NLSTYL(3453) NLCOLO(3295) BTEX(2871) CHEI(2871) JUST(2790) ALIGN(2769) CSPA(2713) FUNC(2633) LSPA(2567) TXCOLO(2561) SpPurp(2549) FPT(2117) TPT(2101) TPVAL(2040) ACDSTY(2006) DESC(1303) DTIT(1194) PPRO(1193) DKEY(1039) PTYP(1027) XYPS(735) FStyle(588) COPY(586) PX(449) NAME(449) PY(441) SPREF(435) ETEX(430) PURP(373) STYP(362) SEL(361) PMLFUN(326) SIZE(309) DTER(273) UCOD(245) AT(243) LTER(237) MSTYLE(234) MCOLOUR(234) ADEG(218) LENG(214) Mpt(214) STR(208) TSIZ(192) ASUB(192) CHOS(192) PJUS(192) DIR(177) POS(159) despar(151) PREV(151) PIN(147) SPKBRK(144) FColour(138) BLNK(136) BMAR(125) LFRA(115) GBOX(106) TMRF(104) DESP(98) VTYP(94) XLEN(92) LNAME(87) LVIS(75) POSFOR(74) YLEN(74) atty(74) attrib(70) SHOP(67) stex(77) ORI(76) RENAME(76) FUNCTION(59) ddprop(58) UDNA(56) BSDWG(54) HEIGHT(54) UTYP(54) BSLAYE(54) DIAM(54) AMEMRF(54) DPOS(52) BFCOLO(50) CLCOLO(50) CLSTYL(50) FFSTYL(50) DTCH(50) FFCOLO(50) BFSTYL(50) OBSTYL(48) DOFF(48) stext(48) ELEL(46) PLFG(46) TXCOLOUR(43) validvalue(43) NUMB(43) NTEXT(43) GTYP(43) PCODE(43) OBCOLO(42) ATEX(41) DDNM(39) XYSC(36) BTEXT(35) DLSTYLE(35) CONN(34) ULEN(34) XYPO(33) PLDI(32) NROW(30) PRFG(30) RPTX(30) COLCOL(30) ROWSTY(30) COLSTY(30) TUFG(30) ROWCOL(30) STORE(28) BUIL(27) DATE(27) GRDOFF(26) GRDID(26) TARF(25) DRNE(17) OSET(17) GRADE(17) FIRE(17) DFLT(16) POSE(14) TPVALUE(14) POSS(14) PAXI(13) MEM(13) DRTMPL(13) SJOI(13) NPPT(13) PHEAD(12) TITL(20) FCONN(20) PLNSTY(20) IDLN(9) ATT(9) ENHANCE(9) EXTR(9) DIST(9) CATA(9) CREF(20) AMAPNME(20) ...`

**一词一例真实用法**：
```pml
NEW STRA FPT $!lineStart TPT POS $!lineEnd            -- aba\Forms\ababuildkeyplan.pmlfrm:369
NEW LAYER NAME $!name/Tasks SpPURP ABAT               -- abauserview.pmlfrm:1071
NEW DDATA PURP EXPR DKEY WRTO PTYP STRI DTIT 'With Respect To'  -- makerepeatddat.pmlfnc:48
NEW DATA /CADCHVACMTO/CANGBRCO_XSECLAINP DESC '...' DKEY a DTIT '?' PPRO (DDESP[4])  -- Hvac_Paragon.dat:43
NEW DATA ... PPRO (WDESP[60] + (STR(DESP[70])))       -- :51（PPRO 接表达式）
NEW DPSP PVIF 3 PURP DIM FUNC '$!number[$!i]' NUMB $!number[$!i]01 DESC '...'  -- tmpdptscrt.pmlfrm:417
NEW LDIM DIR $!currDir DTCH $!dtch DTAN PARA DTER $!dter DOFF $!doff PLDI U  -- isocwdimnfull.pmlfnc:194
DLSTYLE $!dStyle PLSTYLE $!dStyle DLCOLOUR $!dFColour PLCOLOUR $!dFColour DTCOLOUR $!dTColour PTCOLOUR $!dTColour  -- isocwaysupports.pmlfnc:162
NEW SHTMPL $!newName COPY $!oldName RENAME $!oldName $!newName  -- abatemplatesht.pmlfrm:281
NEW GLAB COPY PREV BY X17 BPOF 0 29.99                -- abaarrange.pmlfrm:157
NEW SHEET $!newName COPY like $!template              -- abadrawing.pmlobj:723
ORIGIN CENTRE X50 Y50                                  -- abaequicldimn.pmlfrm:127
SIZE 100 100 / XLEN 50 YLEN 50 NLPN 31                 -- :126
DPOS X75 Y80 DIR E                                     -- :138
NEW DPOI POS W25 N26 U0                                -- :152
NEW GRIDLN /IsometricADP_GridX1 GRDOFF 0 GRDID '1'     -- Hvac_Design.dat:39
SPKBRK TRUE / DESP 0 0 0 0 0 0 0 0 0 0 $               -- hvacsplitatta.pmlfnc:40/42
stex 'DO NOT CUT HOLE IN PIPE' + atty CCNN             -- Mdscrdatft61.pmlfnc:83/85
new sctn copy attrib of prev                           -- Mdschecklen.pmlfnc:546
new bran flowdir OFF                                   -- Mdsdummy.pmlfrm:296
new HRTERM ref $!ref                                   -- aslhandrail.pmlobj:862
NEW FTUB SEL + CONN + WI STYP VL                       -- cblCableTrayVolumes.pmlfrm:1777-1785
PIN 1 DIR P30                                          -- :1814
```

---

## 4. VAR EVAL / OF 属性读取

### 4a. `var !x EVAL ...`——603 处，371 个不同表达式

Top 表达式：
`num for all from !prop(21) drns for all from !bars(16) (position[3]) for all from !bars(16) num for all from !mem(16) num for all from !ccprop(14) name for all from !a(9) name for all from !strucoll(9) desc for all from !a(8) REFE OF DDNM FOR ALL FROM !existTags(8) DESCRIPTION FOR ALL FROM !stringRefs(7) TPVALUE FOR ALL FROM !allTaskParameters(6) (replace(NAME,'/',!displayText,1,1)) FOR ALL FROM !stringRefs(6) :mdsspool for all from !Sctns(4) CRITERIA FOR $!itemRefe(4) :mdspipemat for all from !pipecoll(4) ...`

表达式成分全集：
- 纯属性：`num/name/desc/dkey/func/ppro/catref/pheight/number/styp/leng/lvis/btex/param 1/prop thlb/prop rinb/heig/p1 bore`
- UDA 冒号：`:mdsspool :mdspipemat :mdsmaxbore :mdsminbore :mdsattaref :purp :func :description :MDSActive :PsiSystem[1] :STATUS :MMSSTATUS :FRA.ROOM_KKS`
- 括号表达式：`( position[3] ) ( substring(name,7,7)) (substring(NAME,2)) (poss wrt world) (drns in world) (up in world) (DACDEL) for ALL for $!<element> IGNORE ANY |true|`
- 函数嵌套：`refe of linkref / name of ddna / compType of catref / FULLNAME FOR ALL LAYER WITH (NOT(UNSET(PURP))) AND MATCH(...) NEQ 0`
- 带过滤：`name for all view with func ne 'ISO_VIEW' for $!sheetRef`、`Description for all with :MDSActive eq TRUE from !sectcolltemp`、`name for all REGI with (SPPURPOSE eq 'PSPOOL')`
- 参数化：`$!property FOR $!compRef`
- 大写全拼：`VAR !rad EVALUATE (FRAD WRT WORLD ) FOR ALL FROM !!cdpaRtn`（design\forms\dbeextrusion.pmlfrm:758）

### 4b. `var !x ... OF ...`——2293 处，598 个不同尾部表达式

Top：`$!datum(189) PREV(107) $!attaName wrt /*(72) cref(70) $!datum TO PIN 4(40) branch(35) $!!ce(34) $!datum to Pin 1(33) CE(33) owner(28) $!owner wrt /*(26) $!ce/FITT/H1 wrt /*(26) ...`

OF 后成分全集：DB 属性（`cref/href/tref/spref/detref/spldrg/ddnm/sctn dir/bran/hang/next/VIEW/DBLOC 1`）、WRT 变换（`wrt /* / wrt world / IN WORLD / z dir wrt /*`）、PIN 对位（`TO PIN 4 / to pin 5 / to $!ptpoint1`）、距离方位（`NORMAL DIST $!zDist FROM START`、`dist $!<zdist> wrt world`）、截面指令（`$!<section> CUTBACK THROUGH $!<position> VIA SPINE BOUNDED`、`WALL THROUGH $!<fixing.pos> VIA SPINE BOUNDED`）、集合条件（`for all from ...`、`WITH (...)`、`IGNORE ANY`）。

---

## 5. 属性删除/复位

### 5a. 命令式复位（行尾）——4520 处

配对频次全表（≥2 次）：
`ACDSTY unset(2734) MSTYLE default(202) MCOLOUR default(202) FTER default(192) NLCOLO default(164) NLSTYL default(164) :MDSCONN default(80) :MDSSUPPFUNC default(74) :MDSSUPPTYPE default(74) BSDWG unset(54) :MDSPACKREF unset(49) BSLAYE unset(48) COLSTY default(30) NTEXT unset(29) SPREF nulref(29) DESP unset(13) SPPURPOSE unset(11) JOIE nulref(11) JOIS nulref(11) SPREF unset(9) :MDSBPREF1 default(9) TANSWER unset(8) JOIS def(8) JOIE def(8) BSFN unset(8) INSC unset(8) RETURN nulref(8) PTSP unset(8) WANSWERS unset(8) :MDSSREF unset(7) LNTP unset(6) TABANSWER unset(6) DUTY unset(6) :MDSXCONN default(5) STAREF unset(5) :MDSANCREF def(5) ENDREF unset(5) MATREF nulref(5) MDSYSF unset(5) GTYPE unset(5) OPTIONS default(4) :MDSBPREF1 nulref(4) :MDSATTAREF def(4) :MDSGUIDEREF unset(4) DESPAR unset(4) :MDSPCONN default(4) :MDSATTAREF default(4) SETCOMPDATE unset(4) ROUTND unset(4) ...`

复位关键字四选一：`unset`（值复位）、`default`（回默认）、`def`（缩写）、`nulref`（引用置空）。
示例：`PURP unset`（ababuildkeyplan.pmlfrm:311）、`BSRF nulref`（abatemplatesht.pmlfrm:964）、`spref nulref`（aslstrlngdata.pmlobj 全篇 20+ 处）、`STLSF UNSET`（admstamp.pmlobj:393）。

### 5b. 关键结论：PML2 中 `!!ce.x = unset` 与 `!!ce.x = default` 命中 **0 处**

PML2 侧复位不使用关键字赋值，只有两种手段：
1. 命令式（经 `$!...` 宏展开或 add 命令串，见 5a）
2. 字符串哨兵值 `!func = 'unset'` / `!this.desc.val = 'unset'`（abaarea.pmlfrm:314/760、abadefaults.pmlfrm:145-147 等，全库 `'unset'` 哨兵极多）

### 5c. 专用批量清除范式（mmsclearattributes.pmlfnc / mmsclearall.pmlfnc）

```pml
EXTRACT CLAIM $!dbRef        -- 认领
CLAIM $!dbRef
!!ce = !dbRef
-- 循环执行配置的属性复位宏（"属性名+复位关键字"两数组拼接成命令行执行）：
$!!mmsConFig.conAttributes[1][$!i] $!!mmsConFig.conAttributes[2][$!i]
!!mmsAccess.delete()
```

### 5d. CLEAR 族（3118 处）

绝大多数为 UI 清屏（`AID CLEAR ARC/ARROW/BOX/CYLINDER/CYLI $!number`，aidnumbers.pmlobj:511/520）与 gadget 清空；属性级清除以 5a/5c 为准。

---

## 6. 属性类型判定

### 6a. `.unset()` 判空（Top 属性）

`val(304) joints(203) index(194) name(105) element(103) connections(81) pos(63) dbref(55) cref(53) plane(51) line(50) inter(49) spref(46) stru(41) value(41) description(39) tref(39) beamrefarray(37) datum(37) store(33) loop(31) position(31) data(30) east(26) file(25) mdshconfig(25) ref(24) find(23) wrtitem(23) dbelement(22) ...`

六式变体：`!x.unset()`、`!x.unset().not()`、`!x.unset().eq(FALSE)`、`!x.unset().and(!y.unset())`、`!x.unset().or(...)`、`skip if (!x.unset())`。
DB 属性判空例：`!dbRef.acrf.unset()`（admacr.pmlobj:250）、`!this.arriveBore.unset().and(!this.leaveBore.unset())`（componentselection.pmlfrm:1378）、子成员链 `!orientation.alpha.unset()`（orielement.pmlfrm:719）。

### 6b. `.objectType()`（39+ 种比较类型）

比较值全集：`'DBREF'|'REAL'|'STRING'|'ARRAY'|'BOOLEAN'|'POSITION'|'ORIENTATION'|'DIRECTION'|'LINE'|'ARC'|'PLANE'|'COLOUR'|'CRITERION'|'EXPRESSION'|'FORM'|'GADGET'|'GPHLINE'|'GPHPLANE'|'GPHAXES'|'GPHPOINTVECTOR'|'CATSPECIFICATION'|'MDSINTERFACEVIRTUALFITTING'|'MDSPIPEREPORT'|'DBEASLSTRFLT'|'ASLRPATH'|'CRITERIASET'|'SPLATTRIBUTES'`
运算：`eq(...)`、`ne/neq(...)`、`inset('GPHAXES','GPHPOINTVECTOR')`、`inset('ARRAY','BOOLEAN','REAL')`、`inset('REAL','BORE')`、`inset('DBREF','POSITION')`。
示例：`!aidColour.objectType().eq('REAL')`（aslhandrail.pmlobj:4386）、`!specOrComp.objectType() eq |CATSPECIFICATION|`（catspecviews.pmlobj:2814）、`!tempValue.objectType() inset('REAL','BORE')`（compropdata.pmlobj:4596）。

### 6c. `.valid()` / `.defined()`

多为自定义方法（`define method .valid() ...`），如 common\objects\lststore.pmlobj 的 `.defined()` 方法族（:107/141/372）。

### 6d. PML1 函数式

`undefined(...)` 1254 处（`if (undefined(!layers[1]))`）；`defined(...)` 2472 处（`if defined(!!abadefaults)`、`not defined(!!abaWhat)`）；混用例 `if(!!view3DCntrl.allViews.unset() or undefined(!!view3DCntrl.allViews[!i]))`（view3daddview.pmlfnc:38）。

---

## 7. 属性表达式求值 `.evaluate(...)`

### 7a. `.evaluate(object BLOCK('...'))`——206 处（数组逐元素属性求值主范式）

BLOCK 字符串内属性目标全集：
`.dbref() .dbref().position.wrt(world) .dbref().ownls[5] .refno.dbref() .name .desc .spref .purpose .posref .owner .owner.zdist .type .objectType() .string() .flnn .flnm .etex .cref .refNo .seq .sequence .number.string() .wldNumber .real() .rpro.thkn .zoffset .endposition.up.string('D2').real() .pos.wrt(world) .pos.wrt(world).distance(!pickPosition) .pos.wrt(world).up .invert() .attribute(!this.numAtt) .partNumber .fullName .fullName.before(| of |) .boolean() .description.trim().upcase() .description .ref.string() .usrli .cmpref`

命令式求值：`'PLOOP 1'`、`'STRU'`、`'MEM CTABLE'`、`'TABHEA 1'`、`'MEM TABITE'`、`'STEXT OF TEXT 1'`、`'MCOUNT TEXT'`、`|$!type|`（`!!ce = !!ce.evaluate(object BLOCK(|$!type|))`，catspecviews.pmlobj:1431）。
表达式对象直传：`!element.evaluate(object BLOCK(!expression))`（attributeRule.pmlobj:502、tmplexpression.pmlfrm:165）。

### 7b. 预构建 BLOCK 复用求值（PML1 风格）

```pml
!lsrods = !springs.evaluate(!oEvalLsrod)     -- mds\design\forms\Mdsfh01.pmlfrm:2721
!stringRefs = !dbRefArray.evaluate(!block)   -- admtextlist.pmlobj:102
!pkeys = !plines.evaluate(!block)            -- kclosestpline.pmlfnc:65
!wildString = !element.evaluate(!nameData.format.block())  -- namopt.pmlobj:782
```

### 7c. 其他形态

无参 `.evaluate()`（任务/引擎对象，`!this.currentTask.evaluate()` 94 次）；带参 `.evaluate('STRAIGHT')`（aslstrtwrdata.pmlobj:1876）；`!relation = !expression.evaluate()`（aslstrfltengine.pmlobj:371）。

---

## 8. 数组属性访问

### 8a. `ppBore[n]`（多孔属性，105 处）

```pml
!radius = !this.element.ppBore[!this.number].real()      -- common\objects\dbeppoint.pmlobj:65
if !!ce.ppbore[1].real().eq(50) or ... .eq(40) then      -- Mdssetdattt06.pmlfnc:814
!width = !ctray.ppbore[1].real() / [2] / [3]             -- cblmtrl.pmlfrm:5129-5134（托盘三宽）
!boreString = !component.ppBore[!boreIndices[3]].string(!!boreFmt)  -- componentselection.pmlfrm:2158
!attributeList.append('PPBore[' & !i.string() & ']')     -- queryattributes.pmlfrm:377（属性名拼装）
var !!xSECLAINP (PPBORE1 OF HREF) / (PPBORE2 OF HREF)    -- hvacControl.pmlobj:739/754（命令行查询）
```

### 8b. `purpose[]` 族（1460 处 purpose token）

下标读写：`!this.purpose[!number] = !purp`（abatask.pmlobj:206）、`!purpose = !this.task.purpose[!this.paramlist.val]`（abatasks.pmlfrm:684）、`SpPURP $!taskobj.purpose[$!count]`（abatasklist.pmlobj:265）。
派生名：`purposes(93) purposelist(51) purposetype(17) purposertype(16) purposedtype(13) purposecallback(13)` 等。
（注：`pdes/purpos[` 未发现数组下标用法；`pdesc/pdescription` 为 gadget 名非 DB 属性。）

### 8c. 数组属性通用三式

读 `!arr[i].attr`、写 `!obj.arr[i] = v`、集合收集 `EVAL (position[3]) FOR ALL FROM !bars`。
