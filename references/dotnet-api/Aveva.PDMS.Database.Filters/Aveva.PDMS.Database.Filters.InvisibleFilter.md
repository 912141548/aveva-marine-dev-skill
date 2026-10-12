---
title: Aveva.PDMS.Database.Filters.InvisibleFilter Class
namespace: Aveva.PDMS.Database.Filters
assembly: PDMSFilters
kind: Class
source: Aveva.Pdms.Database.Filters
---

# Aveva.PDMS.Database.Filters.InvisibleFilter Class

> Filter for determining visibility in explorer.

## Syntax

```csharp
public class InvisibleFilter : BaseFilter
```

## Inheritance

`System.Object` → `Aveva.PDMS.Database.Filters.BaseFilter` → `Aveva.PDMS.Database.Filters.InvisibleFilter`

## Thread Safety

Public static ( Shared in Visual Basic) members of this type are
safe for multithreaded operations. Instance members are not guaranteed to be
thread-safe.

## Requirements

Namespace:
Aveva.PDMS.Database.Filters
Assembly: PDMSFilters (in PDMSFilters.dll)

## Constructors

#### `InvisibleFilter` Constructor

Initializes a new instance of the InvisibleFilter class.

```csharp
public InvisibleFilter();
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

Method to test whether we need to scan below given element. always returns true.

```csharp
public override bool ScanBelow( DbElement ele );
```

**Parameters**

- **ele** — current element

**Return Value**

whether to scan below or not

#### `Valid` Method

True if element is visible in explorer.

```csharp
public override bool Valid( DbElement ele );
```

**Parameters**

- **ele** — element to evaluate filter against

**Return Value**

result of avaluating filter
