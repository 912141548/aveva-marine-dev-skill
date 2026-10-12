---
title: Aveva.PDMS.Database.Filters.TypeFilter Class
namespace: Aveva.PDMS.Database.Filters
assembly: PDMSFilters
kind: Class
source: Aveva.Pdms.Database.Filters
---

# Aveva.PDMS.Database.Filters.TypeFilter Class

> Tests whether an element is of a given type. The class makes ensures that only valid parts of the database are returned in the ScanBelow() method. This is important for performance.

## Syntax

```csharp
public class TypeFilter : BaseFilter
```

## Inheritance

`System.Object` → `Aveva.PDMS.Database.Filters.BaseFilter` → `Aveva.PDMS.Database.Filters.HideBelowFilter` → `Aveva.PDMS.Database.Filters.HideFilter` → `Aveva.PDMS.Database.Filters.SkipFilter` → `Aveva.PDMS.Database.Filters.TypeFilter`

## Thread Safety

Public static ( Shared in Visual Basic) members of this type are
safe for multithreaded operations. Instance members are not guaranteed to be
thread-safe.

## Requirements

Namespace:
Aveva.PDMS.Database.Filters
Assembly: PDMSFilters (in PDMSFilters.dll)

## Constructors

#### `TypeFilter` Constructor (Overload 1)

Basic constructor

**Overload List**

Basic constructor
public TypeFilter();
Constructor taking single element type
public TypeFilter(DbElementType);
Constructor taking a list of element types
public TypeFilter(DbElementType[]);

#### `TypeFilter` Constructor ()

Basic constructor

```csharp
public TypeFilter();
```

#### `TypeFilter` Constructor (DbElementType)

Constructor taking single element type

```csharp
public TypeFilter( DbElementType type );
```

**Parameters**

- **type** — element type to filter on

#### `TypeFilter` Constructor (DbElementType[])

Constructor taking a list of element types

```csharp
public TypeFilter( DbElementType[] types );
```

**Parameters**

- **types** — element types to filter on

## Properties

#### `types` Property

Remove element types from list for filter

```csharp
public Aveva.Pdms.Database.DbElementType[] types {get;}
```

## Methods

#### `Add` Method (DbElementType)

Additional element type to filter on

```csharp
public void Add( DbElementType actualType );
```

**Parameters**

- **actualType** — 

#### `Add` Method (DbElementType[])

Additional element types to filter on

```csharp
public void Add( DbElementType[] types );
```

**Parameters**

- **types** — list of types

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

#### `Remove` Method

Remove element type from list for filter

```csharp
public void Remove( DbElementType type );
```

**Parameters**

- **type** — Element type

#### `ScanBelow` Method

Method to test whether we need to scan below given element. Optimised for this class.

```csharp
public override bool ScanBelow( DbElement ele );
```

**Parameters**

- **ele** — current element

**Return Value**

whether to scan below or not

#### `Valid` Method

returns true if elements matches valid types.

```csharp
public override bool Valid( DbElement ele );
```

**Parameters**

- **ele** — element to evaluate filter against

**Return Value**

result of avaluating filter
