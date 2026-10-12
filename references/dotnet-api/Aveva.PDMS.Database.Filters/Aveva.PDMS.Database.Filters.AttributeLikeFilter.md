---
title: Aveva.PDMS.Database.Filters.AttributeLikeFilter Class
namespace: Aveva.PDMS.Database.Filters
assembly: PDMSFilters
kind: Class
source: Aveva.Pdms.Database.Filters
---

# Aveva.PDMS.Database.Filters.AttributeLikeFilter Class

> Returns true if attribute value matches given string, allowing for wild characters. Wild characters are '*' for mutiple wild characters and '?' for a single wild charcter. //These are consistent with PML. CLASS IS UNDER REVIEW- DO NOT USE

## Syntax

```csharp
public class AttributeLikeFilter : BaseAttributeFilter
```

## Inheritance

`System.Object` → `Aveva.PDMS.Database.Filters.BaseFilter` → `Aveva.PDMS.Database.Filters.BaseAttributeFilter` → `Aveva.PDMS.Database.Filters.AttributeLikeFilter`

## Thread Safety

Public static ( Shared in Visual Basic) members of this type are
safe for multithreaded operations. Instance members are not guaranteed to be
thread-safe.

## Requirements

Namespace:
Aveva.PDMS.Database.Filters
Assembly: PDMSFilters (in PDMSFilters.dll)

## Constructors

#### `AttributeLikeFilter` Constructor (Overload 1)

Construct instance of class passing attribute to test and matching string

**Overload List**

Construct instance of class passing attribute to test and matching string
public AttributeLikeFilter(DbAttribute,string);
Parse string.
public AttributeLikeFilter(string);

#### `AttributeLikeFilter` Constructor (DbAttribute, String)

Construct instance of class passing attribute to test and matching string

```csharp
public AttributeLikeFilter( DbAttribute att , string likeString );
```

**Parameters**

- **att** — 
- **likeString** — 

#### `AttributeLikeFilter` Constructor (String)

Parse string.

```csharp
public AttributeLikeFilter( string attLikeFilter );
```

**Parameters**

- **attLikeFilter** —

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
