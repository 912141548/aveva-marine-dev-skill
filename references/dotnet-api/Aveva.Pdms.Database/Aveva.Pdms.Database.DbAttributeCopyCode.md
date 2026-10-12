---
title: Aveva.Pdms.Database.DbAttributeCopyCode Enumeration
namespace: Aveva.Pdms.Database
assembly: Aveva.Pdms.Database
kind: Enumeration
source: Aveva.Pdms.Database
---

# Aveva.Pdms.Database.DbAttributeCopyCode Enumeration

> List of copy codes * Mirrors the Fortran constants K:ATTR.COPY.x * Enumerates possible values of the COPY field of attributes

## Syntax

```csharp
public enum DbAttributeCopyCode
```

## Members

Member Name
Description

ALWAYS Always copy (K:ATTR.COPY)
NOLIKE NOLIKE - do not copy in COPY LIKE
NO NO - Never copy
CONNECTION CONNECTION - go via DT table
SPECIAL Specials
ATTS ATTS - do not copy in COPY ATT
LNAM LNAM - refs for local names (templates) - go via DT table

## Requirements

Namespace:
Aveva.Pdms.Database
Assembly: Aveva.Pdms.Database (in Aveva.Pdms.Database.dll)
