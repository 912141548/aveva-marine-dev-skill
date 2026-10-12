---
title: Aveva.PDMS.Database.Filters.BelowType Class
namespace: Aveva.PDMS.Database.Filters
assembly: PDMSFilters
kind: Class
source: Aveva.Pdms.Database.Filters
---

# Aveva.PDMS.Database.Filters.BelowType Class

> As for the Below filter, but more efficient in the case where we want to test on type only

## Syntax

```csharp
public class BelowType : BaseFilter
```

## Inheritance

`System.Object` → `Aveva.PDMS.Database.Filters.BaseFilter` → `Aveva.PDMS.Database.Filters.BelowType`

## Thread Safety

Public static ( Shared in Visual Basic) members of this type are
safe for multithreaded operations. Instance members are not guaranteed to be
thread-safe.

## Requirements

Namespace:
Aveva.PDMS.Database.Filters
Assembly: PDMSFilters (in PDMSFilters.dll)

## Constructors

#### `BelowType` Constructor (Overload 1)

Constructor taking single element type

**Overload List**

Default Constructor
public BelowType();
Constructor taking single element type
public BelowType(DbElementType);
Constructor taking list of types
public BelowType(DbElementType[]);

#### `BelowType` Constructor (DbElementType)

Constructor taking single element type

```csharp
public BelowType( DbElementType type );
```

**Parameters**

- **type** — 

#### `BelowType` Constructor (DbElementType[])

Constructor taking list of types

```csharp
public BelowType( DbElementType[] types );
```

**Parameters**

- **types** — 

#### `BelowType` Constructor ()

Default Constructor

```csharp
public BelowType();
```

## Properties

#### `types` Property

list of types

```csharp
public Aveva.Pdms.Database.DbElementType[] types {get;}
```

## Methods

#### `Add` Method (DbElementType)

Add type to list

```csharp
public void Add( DbElementType type );
```

**Parameters**

- **type** — 

#### `Add` Method (DbElementType[])

Add list of types to list

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

Remove type from list

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
