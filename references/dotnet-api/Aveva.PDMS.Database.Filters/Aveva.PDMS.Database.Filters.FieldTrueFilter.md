---
title: Aveva.PDMS.Database.Filters.FieldTrueFilter Class
namespace: Aveva.PDMS.Database.Filters
assembly: PDMSFilters
kind: Class
source: Aveva.Pdms.Database.Filters
---

# Aveva.PDMS.Database.Filters.FieldTrueFilter Class

> Filter to return true if Element type field is valid and true

## Syntax

```csharp
public class FieldTrueFilter : BaseFilter
```

## Inheritance

`System.Object` → `Aveva.PDMS.Database.Filters.BaseFilter` → `Aveva.PDMS.Database.Filters.FieldTrueFilter`

## Thread Safety

Public static ( Shared in Visual Basic) members of this type are
safe for multithreaded operations. Instance members are not guaranteed to be
thread-safe.

## Requirements

Namespace:
Aveva.PDMS.Database.Filters
Assembly: PDMSFilters (in PDMSFilters.dll)

## Constructors

#### `FieldTrueFilter` Constructor

Constructor taking the ElementType boolean field to test

```csharp
public FieldTrueFilter( DbNounField field );
```

**Parameters**

- **field** —

## Properties

#### `Field` Property

Element Type field

```csharp
public Aveva.Pdms.Database.DbNounField Field {get; set;}
```

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

Method to test whether we need to scan below given element. Always returns true.

```csharp
public override bool ScanBelow( DbElement ele );
```

**Parameters**

- **ele** — current element

**Return Value**

whether to scan below or not

#### `Valid` Method

Returns true if field is true for given element.

```csharp
public override bool Valid( DbElement ele );
```

**Parameters**

- **ele** — element to evaluate filter against

**Return Value**

result of avaluating filter
