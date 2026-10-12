---
title: Aveva.Pdms.Database.DbAttributeIntrepidQueryType Enumeration
namespace: Aveva.Pdms.Database
assembly: Aveva.Pdms.Database
kind: Enumeration
source: Aveva.Pdms.Database
---

# Aveva.Pdms.Database.DbAttributeIntrepidQueryType Enumeration

> List of Intrepid Query Types * Enumerates possible values of the ITYP field of attributes

## Syntax

```csharp
public enum DbAttributeIntrepidQueryType
```

## Members

Member Name
Description

INTEGER Integer (and int arrays)
REALS Real (and real arrays)
REFERENCE Reference
MEMBERLIST Member List
LOGICAL Logical (and logical arrays)
REFARRAY Reference array
DATE Date
TEXTorEXPRESSION Text or expression
PSEUDOTEXT Pseudo text (no quotes)
TEXT Text
POSITION Position attribute
DIRECTION Direction attribute in ENU format
ORIENTATION Orientation
PARAMETERS Parameters (hashed word/value mixture)
PPOINT Ppoint info
PTSETPARAMETERS Integer array - ptset parameters (axis)
PTSPOINTS Integer array = PTS points for lines
INTEGERCODE Integer - integer code number - DRAFT only
GAPSATTRIBUTES Real array - gaps attributes - DRAFT only
ENULIMITATTRIBUTES Real array = ENU limit attributes - DRAFT only
REALCODEDATTRIBUTES Real - real coded attributes - DRAFT only
PACKEDINTEGER Integer - packed integer attribute - DRAFT only
VIEWPOSITION Real array -- View position attribute - DRAFT only
SPECIALVALUE integer, real array, real - attribute with a special value - DRAFT only
PLDI PLDI - angle if 1 value, direction if 3
LOGICALONOFF Logical - logical attribute set by ON/OFF
PACKEDRELEASES Packed releases (Strutural attribute)
SELECTIONCRITERIA Selection criteria
RATIOATTRIBUTE Real array - ratio attribute
DIRECTIONXYZ Real array - direction in XYZ format
REFASREF Single ref output as a ref
HASHEDWORDARRAY Hashed word array including UDAs
XYLIMITATTRIBUTES Real array = XY limit attributes - DRAFT only
IDREFPLUSPPOINT Integer arrays as ID refs + ppoint
ITMTBL Int array ITMTBL as bolts or additems for ID name
AWDOWN Integer array AWDOWN as ID name weld int.
PARTNUMBER Partnumber for %SPLTBL attribute
ROUTERRULEEXPRESSION Router rules expressions (integer array)
REALBLEN Real array = BLEN format
HASHEDATTRIBUTESNOUNS Hash word array of attributes and nouns

## Requirements

Namespace:
Aveva.Pdms.Database
Assembly: Aveva.Pdms.Database (in Aveva.Pdms.Database.dll)
