---
title: Aveva.PDMS.Database.Filters.AttributeValueFilter Class
namespace: Aveva.PDMS.Database.Filters
assembly: PDMSFilters
kind: Class
source: Aveva.Pdms.Database.Filters
---

# Aveva.PDMS.Database.Filters.AttributeValueFilter Class

> General filter to test whether the value of any type of attribute matches a given value CLASS IS UNDER REVIEW- DO NOT USE

## Syntax

```csharp
public class AttributeValueFilter : BaseAttributeFilter
```

## Inheritance

`System.Object` → `Aveva.PDMS.Database.Filters.BaseFilter` → `Aveva.PDMS.Database.Filters.BaseAttributeFilter` → `Aveva.PDMS.Database.Filters.AttributeValueFilter`

## Thread Safety

Public static ( Shared in Visual Basic) members of this type are
safe for multithreaded operations. Instance members are not guaranteed to be
thread-safe.

## Requirements

Namespace:
Aveva.PDMS.Database.Filters
Assembly: PDMSFilters (in PDMSFilters.dll)

## Constructors

#### `AttributeValueFilter` Constructor (Overload 1)

**Overload List**

public AttributeValueFilter(DbAttribute,TestOperator,object);
public AttributeValueFilter(string);

#### `AttributeValueFilter` Constructor (DbAttribute, TestOperator, Object)

```csharp
public AttributeValueFilter( DbAttribute att , TestOperator testOp , object testVal );
```

#### `AttributeValueFilter` Constructor (String)

```csharp
public AttributeValueFilter( string attValueFilter );
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
