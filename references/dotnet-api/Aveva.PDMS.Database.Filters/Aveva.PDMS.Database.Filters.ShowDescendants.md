---
title: Aveva.PDMS.Database.Filters.ShowDescendants Class
namespace: Aveva.PDMS.Database.Filters
assembly: PDMSFilters
kind: Class
source: Aveva.Pdms.Database.Filters
---

# Aveva.PDMS.Database.Filters.ShowDescendants Class

> Filter to show elements of given type plus ascendants and descendants. Class is used by the Explorer.

## Syntax

```csharp
public class ShowDescendants : BaseFilter
```

## Inheritance

`System.Object` → `Aveva.PDMS.Database.Filters.BaseFilter` → `Aveva.PDMS.Database.Filters.ShowDescendants`

## Thread Safety

Public static ( Shared in Visual Basic) members of this type are
safe for multithreaded operations. Instance members are not guaranteed to be
thread-safe.

## Requirements

Namespace:
Aveva.PDMS.Database.Filters
Assembly: PDMSFilters (in PDMSFilters.dll)

## Constructors

#### `ShowDescendants` Constructor (Overload 1)

Constructor taking type to show

**Overload List**

Default constructor
public ShowDescendants();
Constructor taking type to show
public ShowDescendants(DbElementType);
Construct filter with list of types to show
public ShowDescendants(DbElementType[]);

#### `ShowDescendants` Constructor (DbElementType)

Constructor taking type to show

```csharp
public ShowDescendants( DbElementType type );
```

**Parameters**

- **type** — 

#### `ShowDescendants` Constructor (DbElementType[])

Construct filter with list of types to show

```csharp
public ShowDescendants( DbElementType[] types );
```

**Parameters**

- **types** — 

#### `ShowDescendants` Constructor ()

Default constructor

```csharp
public ShowDescendants();
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
