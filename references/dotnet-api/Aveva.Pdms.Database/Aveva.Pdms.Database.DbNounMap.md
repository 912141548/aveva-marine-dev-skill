---
title: Aveva.Pdms.Database.DbNounMap Enumeration
namespace: Aveva.Pdms.Database
assembly: Aveva.Pdms.Database
kind: Enumeration
source: Aveva.Pdms.Database
---

# Aveva.Pdms.Database.DbNounMap Enumeration

> Significance with respect to spatial map * Mirrors the Fortran constants K:MAP.x * Enumerates possible values of the IMAP field for nouns

## Syntax

```csharp
public enum DbNounMap
```

## Members

Member Name
Description

IGNORE IGNORE
MAPPED MAPPED - Mapped items
SUPERMAP SUPERMAP - Above mapped items
SUBMAP SUBMAP - below mapped items, but still having geometry/position
MAPPEDSUPERMAP MAPPEDSUPERMAP - both mapped and above map elements
MAPPEDMEM MAPPEDMEM - Mapped including member submap elements
MAPPEDMEMSUPERMAP MAPPEDMEMSUPERMAP - both mapped includingmembers, and above map elements
POSMAPPED POSMAPPED = possibly mapped
SUBSUPERMAP SUBSUPERMAP = sub and supermap type

## Requirements

Namespace:
Aveva.Pdms.Database
Assembly: Aveva.Pdms.Database (in Aveva.Pdms.Database.dll)
