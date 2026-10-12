---
title: Aveva.PDMS.Database.Filters.CompoundFilter Class
namespace: Aveva.PDMS.Database.Filters
assembly: PDMSFilters
kind: Class
source: Aveva.Pdms.Database.Filters
---

# Aveva.PDMS.Database.Filters.CompoundFilter Class

> Filter designed specifically for use in the explorer. It is composed of the following - list of filters for elements to show - list of filters for elements to skip - list of filters for elements to hide if there are no 'show' or 'showDescendants then ALL elements considered to be shown.

## Syntax

```csharp
public class CompoundFilter : BaseFilter
```

## Inheritance

`System.Object` → `Aveva.PDMS.Database.Filters.BaseFilter` → `Derived types` → `Aveva.PDMS.Database.Filters.CompoundFilter`

## Thread Safety

Public static ( Shared in Visual Basic) members of this type are
safe for multithreaded operations. Instance members are not guaranteed to be
thread-safe.

## Requirements

Namespace:
Aveva.PDMS.Database.Filters
Assembly: PDMSFilters (in PDMSFilters.dll)

## Constructors

#### `CompoundFilter` Constructor

default constructor

```csharp
public CompoundFilter();
```

## Properties

#### `Hides` Property

Add a 'hide' filters

```csharp
public BaseFilter[] Hides {get;}
```

#### `Shows` Property

list of 'show' filters.

```csharp
public BaseFilter[] Shows {get;}
```

#### `Skips` Property

'skip' filters

```csharp
public BaseFilter[] Skips {get;}
```

## Methods

#### `AddHide` Method

Add a 'hide' filter to list

```csharp
public void AddHide( BaseFilter filt );
```

**Parameters**

- **filt** —

#### `AddShow` Method

Add additional 'show' filter.

```csharp
public void AddShow( BaseFilter filt );
```

**Parameters**

- **filt** —

#### `AddSkip` Method

Add additional 'skip' filter.

```csharp
public void AddSkip( BaseFilter filt );
```

**Parameters**

- **filt** —

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

#### `RemoveHide` Method

Remove 'hide' filter from list

```csharp
public void RemoveHide( BaseFilter filt );
```

**Parameters**

- **filt** —

#### `RemoveShow` Method

Remove given 'show' filter.

```csharp
public void RemoveShow( BaseFilter filt );
```

**Parameters**

- **filt** —

#### `RemoveSkip` Method

remove 'skip' filter from list.

```csharp
public void RemoveSkip( BaseFilter filt );
```

**Parameters**

- **filt** —

#### `ScanBelow` Method

Method to test whether we need to scan below given element. Optimised for this class.

```csharp
public override bool ScanBelow( DbElement ele );
```

**Parameters**

- **ele** — current element

**Return Value**

whether to scan below or not

#### `TestSkip` Method

Test 'skip' filters only

```csharp
public bool TestSkip( DbElement ele );
```

**Parameters**

- **ele** —

#### `Valid` Method

method to return whether filter is true or false for a given element.

```csharp
public override bool Valid( DbElement ele );
```

**Parameters**

- **ele** — element to evaluate filter against

**Return Value**

result of avaluating filter
