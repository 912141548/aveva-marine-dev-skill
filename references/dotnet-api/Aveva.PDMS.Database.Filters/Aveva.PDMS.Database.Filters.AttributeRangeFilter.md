---
title: Aveva.PDMS.Database.Filters.AttributeRangeFilter Class
namespace: Aveva.PDMS.Database.Filters
assembly: PDMSFilters
kind: Class
source: Aveva.Pdms.Database.Filters
---

# Aveva.PDMS.Database.Filters.AttributeRangeFilter Class

> Filter to test if attribute is in a given range. CLASS IS UNDER REVIEW- DO NOT USE

## Syntax

```csharp
public class AttributeRangeFilter : BaseAttributeFilter
```

## Inheritance

`System.Object` → `Aveva.PDMS.Database.Filters.BaseFilter` → `Aveva.PDMS.Database.Filters.BaseAttributeFilter` → `Aveva.PDMS.Database.Filters.AttributeRangeFilter`

## Thread Safety

Public static ( Shared in Visual Basic) members of this type are
safe for multithreaded operations. Instance members are not guaranteed to be
thread-safe.

## Requirements

Namespace:
Aveva.PDMS.Database.Filters
Assembly: PDMSFilters (in PDMSFilters.dll)

## Constructors

#### `AttributeRangeFilter` Constructor (Overload 1)

Construct instance of filter from attribute and low/high value

**Overload List**

Construct instance of filter from attribute and low/high value
public AttributeRangeFilter(DbAttribute,object,object);
Constructor, taking the range as a string
public AttributeRangeFilter(string);

#### `AttributeRangeFilter` Constructor (DbAttribute, Object, Object)

Construct instance of filter from attribute and low/high value

```csharp
public AttributeRangeFilter( DbAttribute att , object lowValue , object highValue );
```

**Parameters**

- **att** — 
- **lowValue** — minimum
- **highValue** — maximum

#### `AttributeRangeFilter` Constructor (String)

Constructor, taking the range as a string

```csharp
public AttributeRangeFilter( string attRangeFilter );
```

**Parameters**

- **attRangeFilter** —

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
