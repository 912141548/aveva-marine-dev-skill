---
title: Aveva.PDMS.Database.Filters.BaseFilter Class
namespace: Aveva.PDMS.Database.Filters
assembly: PDMSFilters
kind: Class
source: Aveva.Pdms.Database.Filters
---

# Aveva.PDMS.Database.Filters.BaseFilter Class

> This is the base class for element filters. Derived classes must implement new versions of Valid(), ScanBelow() and Clone(). The main use of filters is when scanning the database hierarchy looking for elements of a particular criteria. e.g. all Branches.

## Syntax

```csharp
public abstract class BaseFilter : ICloneable
```

## Inheritance

`System.Object` → `Derived types` → `Aveva.PDMS.Database.Filters.BaseFilter`

## Thread Safety

Public static ( Shared in Visual Basic) members of this type are
safe for multithreaded operations. Instance members are not guaranteed to be
thread-safe.

## Requirements

Namespace:
Aveva.PDMS.Database.Filters
Assembly: PDMSFilters (in PDMSFilters.dll)

## Constructors

#### `BaseFilter` Constructor

Default constructor

```csharp
public BaseFilter();
```

## Methods

#### `Clone` Method

Abstract method to Copy filter

```csharp
public abstract object Clone();
```

**Return Value**

copy of filter

**Implements**

ICloneable.Clone

#### `FirstMember` Method

Get first member for which filter is true.

```csharp
public DbElement FirstMember( DbElement element );
```

**Parameters**

- **element** — current element

**Return Value**

first member for which filter is true

#### `Members` Method

Return all members for which filter is true.

```csharp
public DbElement[] Members( DbElement ele );
```

**Parameters**

- **ele** — current element

**Return Value**

members for which filter is true

#### `Next` Method

Get next element in current list for which filter is true.

```csharp
public DbElement Next( DbElement element );
```

**Parameters**

- **element** — current element

**Return Value**

next element for which filter is true

#### `Parent` Method

Climb up to element for which filter is true

```csharp
public DbElement Parent( DbElement element );
```

**Parameters**

- **element** — current element

**Return Value**

first ancestor that matches filter

#### `ScanBelow` Method

abtract method to test whether we need to scan below given element. i.e. could there be elements below this one taht matches the filter. This can be used to optimise a scan. e.g. if we are looking for boxes, there is no point scanning below a branch.

```csharp
public abstract bool ScanBelow( DbElement element );
```

**Parameters**

- **element** — current element

**Return Value**

whether to scan below or not

#### `Valid` Method

abstract method to return whether filter is true or false for a given element.

```csharp
public abstract bool Valid( DbElement element );
```

**Parameters**

- **element** — element to evaluate filter against

**Return Value**

result of avaluating filter

## Operators

#### `Equality` Operator

Compare filters.

```csharp
public static bool operator ==( BaseFilter f1 , BaseFilter f2 );
```

**Parameters**

- **f1** — 
- **f2** —

#### `Inequality` Operator

Compare filters for inequality

```csharp
public static bool operator !=( BaseFilter f1 , BaseFilter f2 );
```

**Parameters**

- **f1** — 
- **f2** —
