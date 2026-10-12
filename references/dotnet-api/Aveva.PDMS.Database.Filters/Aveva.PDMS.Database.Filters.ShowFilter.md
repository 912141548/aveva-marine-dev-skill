---
title: Aveva.PDMS.Database.Filters.ShowFilter Class
namespace: Aveva.PDMS.Database.Filters
assembly: PDMSFilters
kind: Class
source: Aveva.Pdms.Database.Filters
---

# Aveva.PDMS.Database.Filters.ShowFilter Class

> Filter to show elements of given type plus ancestors. When testing ancestors, the filter checks that valid descendants. actually exist rather than possibly exist. Class is used by the explorer.

## Syntax

```csharp
public class ShowFilter : BaseFilter
```

## Inheritance

`System.Object` → `Aveva.PDMS.Database.Filters.BaseFilter` → `Aveva.PDMS.Database.Filters.ShowFilter`

## Thread Safety

Public static ( Shared in Visual Basic) members of this type are
safe for multithreaded operations. Instance members are not guaranteed to be
thread-safe.

## Requirements

Namespace:
Aveva.PDMS.Database.Filters
Assembly: PDMSFilters (in PDMSFilters.dll)

## Constructors

#### `ShowFilter` Constructor (Overload 1)

Construct filter with single element type to show

**Overload List**

Default constructor
public ShowFilter();
Construct filter with single element type to show
public ShowFilter(DbElementType);
Construct filter with list of types to show
public ShowFilter(DbElementType[]);

#### `ShowFilter` Constructor (DbElementType)

Construct filter with single element type to show

```csharp
public ShowFilter( DbElementType type );
```

**Parameters**

- **type** — 

#### `ShowFilter` Constructor (DbElementType[])

Construct filter with list of types to show

```csharp
public ShowFilter( DbElementType[] types );
```

**Parameters**

- **types** — 

#### `ShowFilter` Constructor ()

Default constructor

```csharp
public ShowFilter();
```

## Properties

#### `types` Property

Return list of types to show

```csharp
public Aveva.Pdms.Database.DbElementType[] types {get;}
```

## Methods

#### `Add` Method (DbElementType)

Add extra type to show

```csharp
public void Add( DbElementType type );
```

**Parameters**

- **type** — 

#### `Add` Method (DbElementType[])

Add list of types to show

```csharp
public void Add( DbElementType[] types );
```

**Parameters**

- **types** —

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

Remove type fom list to show

```csharp
public void Remove( DbElementType type );
```

**Parameters**

- **type** —

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

method to return whether filter is true or false for a given element.

```csharp
public override bool Valid( DbElement ele );
```

**Parameters**

- **ele** — element to evaluate filter against

**Return Value**

result of avaluating filter
