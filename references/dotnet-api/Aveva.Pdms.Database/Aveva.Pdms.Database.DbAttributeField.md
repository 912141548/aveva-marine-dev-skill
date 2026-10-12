---
title: Aveva.Pdms.Database.DbAttributeField Enumeration
namespace: Aveva.Pdms.Database
assembly: Aveva.Pdms.Database
kind: Enumeration
source: Aveva.Pdms.Database
---

# Aveva.Pdms.Database.DbAttributeField Enumeration

> List of Attribute component field identifiers.

## Syntax

```csharp
public enum DbAttributeField
```

## Members

Member Name
Description

NAME Attribute name.
DESTEX Textual description.
TYPE Type of attribute. e.g. int
SIZE Maximum Size of attribute
UNIT Units for attribute, i.e. distance or bore or none
VISI Visible or not
ITYP Formatting type
DTLATT attribute to be used in Datal instead of given one. AVEVA USE ONLY
DEFER Datal-type output reference deferral. AVEVA USE ONLY
ITSATT DRAFT Intelligent Text System basic value. AVEVA USE ONLY.
COORD DRAFT Intelligent Text System coordinate. AVEVA USE ONLY.
ITSEL DRAFT Intelligent Text System navigation. AVEVA USE ONLY.
QSET If false then attribute may only be queried
DTYP Underlying dabacon type
CASC True for attributes whose values are cascaded down when an element is created
TUBE Is attribute valid on TUBI
QTXT Query text
RPTX Reporter text
CATPAR Catalogue parameter or not
QSUPPA Suppress output
QUAL Attribute has a qualifier
INVIS Attribute is always invisible
DESRUL True for a ref attribute that allows rules
LGSPLA True if attribute for a design db is writable within spooler
TKEYLN Key length for an integer table
TDATLN Data length for an integer table
CATRUL true if attribute can be used in a catalogue rule
TABLE true if attribute is a table attribute
DEPEND List of real attributes on which a pseudo attribute depends
CHANGE Indicates 'change type' category
CATEG CATEGORY: Category of attribute for organization in documentation
DEFI Definition: DDL or Pseudo.
WDEFI Definition for writing: DDL or Pseudo.
SYNO Synonym mapping.
EQUIVA EQUIVA: Attribute to be used when determining value of associated pseudoattribute
TABATT TABATT: Table attribute that provides permitted values when setting associated attribute
PLCF P-line cache change flag.
DFDP Default precision (D.P.s)
TRUN Truncation possible?
DCHC DESIGN change code.
COPY Copy option.
PNAME P-point or P-line specific.
IDREF ID reference required for pseudo attribute?
EXPSIZ Expected size of Splash element.
TBLTYP Integer table type.
PRTCTA Attribute protected?
AVAIDB AVAIDB: Hash codes of databases in which attribute is defined
DACCHK DACCHK: Data access control checking status
ENUM ENUM: Indicates an integer which is really an enumeration
RULEDP RULDEP: List of other attributes that affect the value of this attribute
CONNEX CONNEX: Whether attribute defines a connection
PSCODE PSCODE:
MANUAL Manual category

## Requirements

Namespace:
Aveva.Pdms.Database
Assembly: Aveva.Pdms.Database (in Aveva.Pdms.Database.dll)
