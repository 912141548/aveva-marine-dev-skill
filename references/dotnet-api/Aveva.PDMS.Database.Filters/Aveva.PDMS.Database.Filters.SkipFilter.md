---
title: Aveva.PDMS.Database.Filters.SkipFilter Class
namespace: Aveva.PDMS.Database.Filters
assembly: PDMSFilters
kind: Class
source: Aveva.Pdms.Database.Filters
---

# Aveva.PDMS.Database.Filters.SkipFilter Class

> Filter to skip elements of given type. i.e. returns true if not an element to skip. Class is used by the explorer to flatten the tree view. If an element is skipped, its descendents will NOT be skipped.

## Syntax

```csharp
public class SkipFilter : TypeFilter
```

## Inheritance

`System.Object` → `Aveva.PDMS.Database.Filters.BaseFilter` → `Aveva.PDMS.Database.Filters.TypeFilter` → `Aveva.PDMS.Database.Filters.SkipFilter`

## Thread Safety

Public static ( Shared in Visual Basic) members of this type are
safe for multithreaded operations. Instance members are not guaranteed to be
thread-safe.

## Requirements

Namespace:
Aveva.PDMS.Database.Filters
Assembly: PDMSFilters (in PDMSFilters.dll)

## Constructors

#### `SkipFilter` Constructor (Overload 1)

Constructor taking an element type to skip over

**Overload List**

Default constructor
public SkipFilter();
Constructor taking an element type to skip over
public SkipFilter(DbElementType);
Constructor taking a list of element types to skip over
public SkipFilter(DbElementType[]);

#### `SkipFilter` Constructor (DbElementType)

Constructor taking an element type to skip over

```csharp
public SkipFilter( DbElementType type );
```

**Parameters**

- **type** — element type

#### `SkipFilter` Constructor (DbElementType[])

Constructor taking a list of element types to skip over

```csharp
public SkipFilter( DbElementType[] types );
```

**Parameters**

- **types** — list of types

#### `SkipFilter` Constructor ()

Default constructor

```csharp
public SkipFilter();
```

## Methods

#### `ScanBelow` Method

Method to test whether we need to scan below given element. Always true for this class.

```csharp
public override bool ScanBelow( DbElement element );
```

**Parameters**

- **element** — current element

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
