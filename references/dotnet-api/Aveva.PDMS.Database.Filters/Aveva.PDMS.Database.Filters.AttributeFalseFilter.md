---
title: Aveva.PDMS.Database.Filters.AttributeFalseFilter Class
namespace: Aveva.PDMS.Database.Filters
assembly: PDMSFilters
kind: Class
source: Aveva.Pdms.Database.Filters
---

# Aveva.PDMS.Database.Filters.AttributeFalseFilter Class

> Tests if a boolean attribute value is valid and false

## Syntax

```csharp
public class AttributeFalseFilter : BaseFilter
```

## Inheritance

`System.Object` → `Aveva.PDMS.Database.Filters.BaseFilter` → `Aveva.PDMS.Database.Filters.AttributeFalseFilter`

## Thread Safety

Public static ( Shared in Visual Basic) members of this type are
safe for multithreaded operations. Instance members are not guaranteed to be
thread-safe.

## Requirements

Namespace:
Aveva.PDMS.Database.Filters
Assembly: PDMSFilters (in PDMSFilters.dll)

## Constructors

#### `AttributeFalseFilter` Constructor

Construct instance, passing attribute to test

```csharp
public AttributeFalseFilter( DbAttribute att );
```

**Parameters**

- **att** —

## Properties

#### `Attribute` Property

Attribute to test

```csharp
public Aveva.Pdms.Database.DbAttribute Attribute {get; set;}
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

Method to test whether we need to scan below given element. Always return true.

```csharp
public override bool ScanBelow( DbElement ele );
```

**Parameters**

- **ele** — current element

**Return Value**

whether to scan below or not

#### `Valid` Method

method to return whether filter is true or false for a given element.

```csharp
public override bool Valid( DbElement ele );
```

**Parameters**

- **ele** — element to evaluate filter against

**Return Value**

result of avaluating filter
