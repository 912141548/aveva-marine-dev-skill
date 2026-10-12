---
title: Aveva.Pdms.Database.DbAttributeSpecialField Enumeration
namespace: Aveva.Pdms.Database
assembly: Aveva.Pdms.Database
kind: Enumeration
source: Aveva.Pdms.Database
---

# Aveva.Pdms.Database.DbAttributeSpecialField Enumeration

> Other attribute information which may be included in tabular output. The values of special fields may be derived from fields or other information on the output. Special fields must be supported by the GetAsString method, and can thus be used in Attribute Formatters. However, they cannot be used in most other pleaces where a field may be.

## Syntax

```csharp
public enum DbAttributeSpecialField
```

## Members

Member Name
Description

TYPESIZE The type followed by the size in parenthesis if this is greater than 1, 'DOUBLE(3)'
HASHCODE The hash code (as an integer)
INTERNALNAME The internal name of the attribute, ie, the hash code unhashed. Note that every attribute will have an internal name, but invisible attributes may not have a NAME
CAPITALISEDNAME The name, with first character upper case and the rest lower case

## Requirements

Namespace:
Aveva.Pdms.Database
Assembly: Aveva.Pdms.Database (in Aveva.Pdms.Database.dll)
