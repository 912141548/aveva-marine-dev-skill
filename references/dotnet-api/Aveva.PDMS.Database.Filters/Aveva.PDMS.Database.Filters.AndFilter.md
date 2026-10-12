---
title: Aveva.PDMS.Database.Filters.AndFilter Class
namespace: Aveva.PDMS.Database.Filters
assembly: PDMSFilters
kind: Class
source: Aveva.Pdms.Database.Filters
---

# Aveva.PDMS.Database.Filters.AndFilter Class

> AND two or more filters.

## Syntax

```csharp
public class AndFilter : BaseFilter
```

## Inheritance

`System.Object` → `Aveva.PDMS.Database.Filters.BaseFilter` → `Aveva.PDMS.Database.Filters.AndFilter`

## Thread Safety

Public static ( Shared in Visual Basic) members of this type are
safe for multithreaded operations. Instance members are not guaranteed to be
thread-safe.

## Requirements

Namespace:
Aveva.PDMS.Database.Filters
Assembly: PDMSFilters (in PDMSFilters.dll)

## Constructors

#### `AndFilter` Constructor (Overload 1)

Default constructor

**Overload List**

Default constructor
public AndFilter();
Construct from two existing filters
public AndFilter(BaseFilter,BaseFilter);
Construct from a list of filters
public AndFilter(BaseFilter[]);

#### `AndFilter` Constructor ()

Default constructor

```csharp
public AndFilter();
```

#### `AndFilter` Constructor (BaseFilter, BaseFilter)

Construct from two existing filters

```csharp
public AndFilter( BaseFilter filter1 , BaseFilter filter2 );
```

**Parameters**

- **filter1** — 
- **filter2** — 

#### `AndFilter` Constructor (BaseFilter[])

Construct from a list of filters

```csharp
public AndFilter( BaseFilter[] filts );
```

**Parameters**

- **filts** —

## Properties

#### `filters` Property

list of current filters

```csharp
public BaseFilter[] filters {get;}
```

#### `First` Property

First filter in AND list

```csharp
public BaseFilter First {get;}
```

#### `Second` Property

Second filter in AND list

```csharp
public BaseFilter Second {get;}
```

## Methods

#### `Add` Method

Add another filter to AND list

```csharp
public void Add( BaseFilter filt );
```

**Parameters**

- **filt** —

#### `Clone` Method

Copy filter

```csharp
public override object Clone();
```

**Implements**

ICloneable.Clone

#### `Equals` Method

Equality test

```csharp
public override bool Equals( object o );
```

**Parameters**

- **o** —

#### `GetHashCode` Method

Get hash value

```csharp
public override int GetHashCode();
```

#### `Remove` Method

Remove filter from AND list

```csharp
public void Remove( BaseFilter filt );
```

**Parameters**

- **filt** —

#### `ScanBelow` Method

Return true if we need to scan below this element. This can be returned false to optimise the scan.

```csharp
public override bool ScanBelow( DbElement ele );
```

**Parameters**

- **ele** — Current Element

**Return Value**

Result of whether to scan below or not

#### `Valid` Method

Evaluate filter for given element

```csharp
public override bool Valid( DbElement ele );
```

**Parameters**

- **ele** — Element to test filter on

**Return Value**

Result of evaluating filter against element
