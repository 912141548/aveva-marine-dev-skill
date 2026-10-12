---
title: Aveva.PDMS.Database.Filters.BelowOrAtType Class
namespace: Aveva.PDMS.Database.Filters
assembly: PDMSFilters
kind: Class
source: Aveva.Pdms.Database.Filters
---

# Aveva.PDMS.Database.Filters.BelowOrAtType Class

> Filter to test if element is at or below given element types.

## Syntax

```csharp
public class BelowOrAtType : BaseFilter
```

## Inheritance

`System.Object` → `Aveva.PDMS.Database.Filters.BaseFilter` → `Aveva.PDMS.Database.Filters.BelowOrAtType`

## Thread Safety

Public static ( Shared in Visual Basic) members of this type are
safe for multithreaded operations. Instance members are not guaranteed to be
thread-safe.

## Requirements

Namespace:
Aveva.PDMS.Database.Filters
Assembly: PDMSFilters (in PDMSFilters.dll)

## Constructors

#### `BelowOrAtType` Constructor (Overload 1)

Construct filter for single type

**Overload List**

Empty filter
public BelowOrAtType();
Construct filter for single type
public BelowOrAtType(DbElementType);
Set list of possible types
public BelowOrAtType(DbElementType[]);

#### `BelowOrAtType` Constructor (DbElementType)

Construct filter for single type

```csharp
public BelowOrAtType( DbElementType type );
```

**Parameters**

- **type** — 

#### `BelowOrAtType` Constructor (DbElementType[])

Set list of possible types

```csharp
public BelowOrAtType( DbElementType[] types );
```

**Parameters**

- **types** — 

#### `BelowOrAtType` Constructor ()

Empty filter

```csharp
public BelowOrAtType();
```

## Properties

#### `types` Property

List of element types

```csharp
public Aveva.Pdms.Database.DbElementType[] types {get;}
```

## Methods

#### `Add` Method (DbElementType)

Add element type to list of possibilities

```csharp
public void Add( DbElementType type );
```

**Parameters**

- **type** — 

#### `Add` Method (DbElementType[])

Add list of element types to list of possibilities

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

Remove element type from list of possibilities

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
