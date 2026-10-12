---
title: Aveva.Pdms.Database.DbNounField Enumeration
namespace: Aveva.Pdms.Database
assembly: Aveva.Pdms.Database
kind: Enumeration
source: Aveva.Pdms.Database
---

# Aveva.Pdms.Database.DbNounField Enumeration

> List of Element component field identifiers.

## Syntax

```csharp
public enum DbNounField
```

## Members

Member Name
Description

DEFI Real or pseudo
VISI Visible or not
RPTX REPORTER text.
NAME Element type name
LGSPLN element may be moved within spooler
CHOL gives the complement of a hole
DBTP DB types containing element
CSIG Element is primary in terms of claiming
TOPF Element is a top level element in the 3D graphics
PRMF True if a primitive
POPF True if a point
XTRF true if an extrusion like element
FEWO true if element exists at the world level
PIPC true if a piping component
HOLC true if a hole
CATC true if a catalogue component
HNGC true if a hanger component
PSKC Component can have a PSKEY
GCODE Draft graphical code
PSOWNR True if owner could be different from Dabacon owner
PSNEXT True if next element could be different from Dabacon next element
PSFRST True if first member could be different from Dabacon first member element
PICK True for a pickable element
XPVISI True if element is visible
SECOND true if element has a secondary hierarchy
FOLDER List of types to create folders in the explorer
LNODE Indicates last node in Explorer
VALIDC Used to determine connections- AVEVA USE ONLY
DESTEX Textual description.
CATEG CATEGORY: Category of attribute for organization in documentation
SYNO Pointer to synonym; 0 if not a synonym
QMOD QMOD: True if the user can modify the element
PRTCTN True if design element is protected
COMP DO NOT USE - REDUNDANT
IMAP Significance with respect to the spatial map
CHANGE CHANGE: Control for changing element type. Elements with the same value of CHANGE may have their types changed to one another
CATGLE CATGLE: Catalogue database geometry level
CATDEP CATDEP: Catalogue dependencies
DESDEP DESDEP: Design dependencies
GRAPH GRAPH: Relates to how the 3D Graphics is generated
GORP True for an item in a geomset or negative geomset or plineset or pointset
SIGNIF SIGNIF: True for significant types
ANCES True for an element which is an ancestor of another element
CLWTHN CLWTHN: True for element types that should, by default, be in the NOCHECK WITHIN list for CLASHER
CLRSEC CLRSEC: True for elements that should, by default, be included in the CLASH REPORT list for CLASHER
WLDORI WLDORI: True for element types whose orientation is deemed to be with respect to the world
VOLDEF VOLDEF: True for element types which will, by default, be included in volumetric queries
HULC HULC: Hull component
DTXC Detail text component
COMC ACOM-HCOM component
EQUC Equipment component
FRMC Framework component
PFRC Positioned framework component
FITC Fitting component
GMTC 2D Geomset component
GMSC Geomset component
DTSC Dataset component
NGMC Negative geomset component
JOIC Joint component
PLNC Plineset component
PRFC Profile component
PTSC Pointset component
BUIC Building component
LNGDES Long description of element type for documentation
ATTDES Description following attributes for documentation
DIAGRM Diagram title for documentation
ENDNOT End note for documentation
DTLNAM DTLNAM: Element has NAME derived from specified attribute
DRQFIL DRQFIL: True for Elements which have Drawing files
DROFIL DROFIL: True for Elements which own Drawing-file elements
MANUAL MANUAL: Manual category

## Requirements

Namespace:
Aveva.Pdms.Database
Assembly: Aveva.Pdms.Database (in Aveva.Pdms.Database.dll)
