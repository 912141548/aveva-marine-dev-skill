---
title: Aveva.PDMS.Database.Filters.OrFilter Class
namespace: Aveva.PDMS.Database.Filters
assembly: PDMSFilters
kind: Class
source: Aveva.Pdms.Database.Filters
---

# Aveva.PDMS.Database.Filters.OrFilter Class

> Class to 'OR' together two or more existing filters.

## Syntax

```csharp
public class OrFilter : BaseFilter
```

## Inheritance

`System.Object` → `Aveva.PDMS.Database.Filters.BaseFilter` → `Aveva.PDMS.Database.Filters.OrFilter`

## Thread Safety

Public static ( Shared in Visual Basic) members of this type are
safe for multithreaded operations. Instance members are not guaranteed to be
thread-safe.

## Requirements

Namespace:
Aveva.PDMS.Database.Filters
Assembly: PDMSFilters (in PDMSFilters.dll)

## Constructors

#### `OrFilter` Constructor (Overload 1)

Default constructor

**Overload List**

Default constructor
public OrFilter();
constructor taking two existing filters
public OrFilter(BaseFilter,BaseFilter);
constructor taking a list of filters
public OrFilter(BaseFilter[]);

#### `OrFilter` Constructor ()

Default constructor

```csharp
public OrFilter();
```

#### `OrFilter` Constructor (BaseFilter, BaseFilter)

constructor taking two existing filters

```csharp
public OrFilter( BaseFilter filt1 , BaseFilter filt2 );
```

**Parameters**

- **filt1** — 
- **filt2** — 

#### `OrFilter` Constructor (BaseFilter[])

constructor taking a list of filters

```csharp
public OrFilter( BaseFilter[] filts );
```

**Parameters**

- **filts** —

## Properties

#### `filters` Property

Return list of filters in OR list

```csharp
public BaseFilter[] filters {get;}
```

#### `First` Property

1st filter to OR

```csharp
public BaseFilter First {get; set;}
```

#### `Second` Property

2nd filter to OR

```csharp
public BaseFilter Second {get; set;}
```

## Methods

#### `Add` Method

Add filter to list of ORs

```csharp
public void Add( BaseFilter filt );
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

#### `Remove` Method

Remove filter to list of ORs

```csharp
public void Remove( BaseFilter filt );
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

#### `Valid` Method

method to return whether filter is true or false for a given element.

```csharp
public override bool Valid( DbElement ele );
```

**Parameters**

- **ele** — element to evaluate filter against

**Return Value**

result of avaluating filter
