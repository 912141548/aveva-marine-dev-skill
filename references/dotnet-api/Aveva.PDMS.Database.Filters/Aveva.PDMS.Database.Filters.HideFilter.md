---
title: Aveva.PDMS.Database.Filters.HideFilter Class
namespace: Aveva.PDMS.Database.Filters
assembly: PDMSFilters
kind: Class
source: Aveva.Pdms.Database.Filters
---

# Aveva.PDMS.Database.Filters.HideFilter Class

> Filter to hide elements of given type. i.e. returns true if not an element to hide. Used by the explorer. If an element is hidden, its descendents will also be hidden.

## Syntax

```csharp
public class HideFilter : TypeFilter
```

## Inheritance

`System.Object` → `Aveva.PDMS.Database.Filters.BaseFilter` → `Aveva.PDMS.Database.Filters.TypeFilter` → `Aveva.PDMS.Database.Filters.HideFilter`

## Thread Safety

Public static ( Shared in Visual Basic) members of this type are
safe for multithreaded operations. Instance members are not guaranteed to be
thread-safe.

## Requirements

Namespace:
Aveva.PDMS.Database.Filters
Assembly: PDMSFilters (in PDMSFilters.dll)

## Constructors

#### `HideFilter` Constructor (Overload 1)

Constructor taking a type to hide

**Overload List**

Default Constructor
public HideFilter();
Constructor taking a type to hide
public HideFilter(DbElementType);
Constructor taking a list of types to hide
public HideFilter(DbElementType[]);

#### `HideFilter` Constructor (DbElementType)

Constructor taking a type to hide

```csharp
public HideFilter( DbElementType type );
```

**Parameters**

- **type** — 

#### `HideFilter` Constructor (DbElementType[])

Constructor taking a list of types to hide

```csharp
public HideFilter( DbElementType[] types );
```

**Parameters**

- **types** — 

#### `HideFilter` Constructor ()

Default Constructor

```csharp
public HideFilter();
```

## Methods

#### `ScanBelow` Method

Method to test whether we need to scan below given element. Result is as for Valid().

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
