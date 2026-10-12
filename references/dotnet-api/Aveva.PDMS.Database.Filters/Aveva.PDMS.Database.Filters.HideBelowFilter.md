---
title: Aveva.PDMS.Database.Filters.HideBelowFilter Class
namespace: Aveva.PDMS.Database.Filters
assembly: PDMSFilters
kind: Class
source: Aveva.Pdms.Database.Filters
---

# Aveva.PDMS.Database.Filters.HideBelowFilter Class

> Filter to hide all elements below an element of a given type. e.g. hide all elements below a group. It returns true if not an element to hide. Used by the explorer.

## Syntax

```csharp
public class HideBelowFilter : TypeFilter
```

## Inheritance

`System.Object` → `Aveva.PDMS.Database.Filters.BaseFilter` → `Aveva.PDMS.Database.Filters.TypeFilter` → `Aveva.PDMS.Database.Filters.HideBelowFilter`

## Thread Safety

Public static ( Shared in Visual Basic) members of this type are
safe for multithreaded operations. Instance members are not guaranteed to be
thread-safe.

## Requirements

Namespace:
Aveva.PDMS.Database.Filters
Assembly: PDMSFilters (in PDMSFilters.dll)

## Constructors

#### `HideBelowFilter` Constructor (Overload 1)

Constructor taking a single element to hide below.

**Overload List**

Default Constructor
public HideBelowFilter();
Constructor taking a single element to hide below.
public HideBelowFilter(DbElementType);
Constructor taking a list of elements to hide below.
public HideBelowFilter(DbElementType[]);

#### `HideBelowFilter` Constructor (DbElementType)

Constructor taking a single element to hide below.

```csharp
public HideBelowFilter( DbElementType type );
```

**Parameters**

- **type** — 

#### `HideBelowFilter` Constructor (DbElementType[])

Constructor taking a list of elements to hide below.

```csharp
public HideBelowFilter( DbElementType[] types );
```

**Parameters**

- **types** — 

#### `HideBelowFilter` Constructor ()

Default Constructor

```csharp
public HideBelowFilter();
```

## Methods

#### `ScanBelow` Method

Method to test whether we need to scan below given element. Returns false if Valid() is false.

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
