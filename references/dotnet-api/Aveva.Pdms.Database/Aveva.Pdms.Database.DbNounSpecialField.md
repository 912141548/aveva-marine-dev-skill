---
title: Aveva.Pdms.Database.DbNounSpecialField Enumeration
namespace: Aveva.Pdms.Database
assembly: Aveva.Pdms.Database
kind: Enumeration
source: Aveva.Pdms.Database
---

# Aveva.Pdms.Database.DbNounSpecialField Enumeration

> Other DbElementType information which may be included in tabular output. The values of special fields may be derived from fields or other information on the output. Special fields must be supported by the GetAsString method, and can thus be used in DbElementTypeFormats. However, they cannot be used in most other pleaces where a field may be.

## Syntax

```csharp
public enum DbNounSpecialField
```

## Members

Member Name
Description

HASHCODE The hash code as an integer
INTERNALNAME The internal name, ie, the hash code unhashed. Note that every DbElementType will have an internal name, but invisible attributes will not have a NAME
HARDTYPE Hard type
BASETYPE Base type
ASCENDANTTYPES List of ascendant types
SYSTEMATTRIBUTES List of visible system attributes
DESCENDANTTYPES List of valid descendant types
MEMBERTYPES List of valid member types
OWNERTYPES List of valid owner types
ISPSEUDO Whether element type is pseuco
SHORTNAME Shortname
ALLSYSTEMATTRIBUTES List of all system attributes, including any that are not visible
CAPITALISEDNAME Name, with first letter in upper case and rest in lower
SYSATTSANDDESC List of visible system attributes together with their descriptions
PRIMARYTYPE String 'Primary Element' if and only if type is primary

## Requirements

Namespace:
Aveva.Pdms.Database
Assembly: Aveva.Pdms.Database (in Aveva.Pdms.Database.dll)
