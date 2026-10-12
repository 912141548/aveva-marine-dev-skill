---
title: Aveva.PDMS.Database.Filters.AttributeListFilter Class
namespace: Aveva.PDMS.Database.Filters
assembly: PDMSFilters
kind: Class
source: Aveva.Pdms.Database.Filters
---

# Aveva.PDMS.Database.Filters.AttributeListFilter Class

> Filter to compare an attribute against a list of potential values.

## Syntax

```csharp
public class AttributeListFilter : BaseAttributeFilter
```

## Inheritance

`System.Object` → `Aveva.PDMS.Database.Filters.BaseFilter` → `Aveva.PDMS.Database.Filters.BaseAttributeFilter` → `Aveva.PDMS.Database.Filters.AttributeListFilter`

## Thread Safety

Public static ( Shared in Visual Basic) members of this type are
safe for multithreaded operations. Instance members are not guaranteed to be
thread-safe.

## Requirements

Namespace:
Aveva.PDMS.Database.Filters
Assembly: PDMSFilters (in PDMSFilters.dll)

## Constructors

#### `AttributeListFilter` Constructor (Overload 1)

Construct object from attribute and list of allowed values. CLASS IS UNDER REVIEW- DO NOT USE

**Overload List**

Construct object from attribute and list of allowed values. CLASS IS UNDER REVIEW- DO NOT USE
public AttributeListFilter(DbAttribute,object[]);
Parse string to produce filter
public AttributeListFilter(string);

#### `AttributeListFilter` Constructor (DbAttribute, Object[])

Construct object from attribute and list of allowed values. CLASS IS UNDER REVIEW- DO NOT USE

```csharp
public AttributeListFilter( DbAttribute att , object[] listValues );
```

**Parameters**

- **att** — 
- **listValues** — 

#### `AttributeListFilter` Constructor (String)

Parse string to produce filter

```csharp
public AttributeListFilter( string attributeListFilter );
```

**Parameters**

- **attributeListFilter** —

## Methods

#### `Clone` Method

method to Copy filter

```csharp
public override object Clone();
```

**Return Value**

copy of filter

**Implements**

ICloneable.Clone

#### `Equals` Method

Equal or not

```csharp
public override bool Equals( object o );
```

**Parameters**

- **o** —

#### `GetHashCode` Method

Return hash value

```csharp
public override int GetHashCode();
```

#### `ScanBelow` Method

Method to test whether we need to scan below given element. Always return true.

```csharp
public override bool ScanBelow( DbElement ele );
```

**Parameters**

- **ele** — current element

**Return Value**

whether to scan below or not

#### `ToString` Method

Construct string from filter

```csharp
public override string ToString();
```

#### `Valid` Method

method to return whether filter is true or false for a given element.

```csharp
public override bool Valid( DbElement ele );
```

**Parameters**

- **ele** — element to evaluate filter against

**Return Value**

result of avaluating filter
