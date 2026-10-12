---
title: Aveva.Pdms.Database.DbFieldFormatDefaultAction Enumeration
namespace: Aveva.Pdms.Database
assembly: Aveva.Pdms.Database
kind: Enumeration
source: Aveva.Pdms.Database
---

# Aveva.Pdms.Database.DbFieldFormatDefaultAction Enumeration

> Actions a field formatter may take when no specific substitute string has been defined for the value found

## Syntax

```csharp
public enum DbFieldFormatDefaultAction
```

## Members

Member Name
Description

FIXED_STRING Always represent by a fixed string (the DefaultString property)
GET_AS_STRING Fall back to the standard representation of the object (as if no field formatter were defined)

## Requirements

Namespace:
Aveva.Pdms.Database
Assembly: Aveva.Pdms.Database (in Aveva.Pdms.Database.dll)
