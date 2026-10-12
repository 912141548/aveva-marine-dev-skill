---
title: Aveva.PDMS.Database.Filters.DBElementCollection Class
namespace: Aveva.PDMS.Database.Filters
assembly: PDMSFilters
kind: Class
source: Aveva.Pdms.Database.Filters
---

# Aveva.PDMS.Database.Filters.DBElementCollection Class

> Class to iterate through the database hierarchy returning the elements that match the supplied filter. The scan starts at a given element. If no filter is given, then all elements below the start element are returned. The actual iteration is done via an enumerator.

## Syntax

```csharp
public class DBElementCollection : IEnumerable
```

## Inheritance

`System.Object` → `Aveva.PDMS.Database.Filters.DBElementCollection`

## Thread Safety

Public static ( Shared in Visual Basic) members of this type are
safe for multithreaded operations. Instance members are not guaranteed to be
thread-safe.

## Requirements

Namespace:
Aveva.PDMS.Database.Filters
Assembly: PDMSFilters (in PDMSFilters.dll)

## Constructors

#### `DBElementCollection` Constructor (Overload 1)

Default constructor

**Overload List**

Default constructor
public DBElementCollection();
Constructor taking a root element
public DBElementCollection(DbElement);
Constructor taking root element and a filter
public DBElementCollection(DbElement,BaseFilter);

#### `DBElementCollection` Constructor ()

Default constructor

```csharp
public DBElementCollection();
```

#### `DBElementCollection` Constructor (DbElement)

Constructor taking a root element

```csharp
public DBElementCollection( DbElement root );
```

**Parameters**

- **root** — 

#### `DBElementCollection` Constructor (DbElement, BaseFilter)

Constructor taking root element and a filter

```csharp
public DBElementCollection( DbElement root , BaseFilter filt );
```

**Parameters**

- **root** — 
- **filt** —

## Properties

#### `Filter` Property

filter to be applied

```csharp
public BaseFilter Filter {get; set;}
```

#### `IncludeRoot` Property

Flag to denotr if to return the root element as aprt of the collection

```csharp
public bool IncludeRoot {get; set;}
```

## Methods

#### `GetEnumerator` Method

Return enumerator into the database. This enumerator can then be used to do the actual iteration.

```csharp
public IEnumerator GetEnumerator();
```

**Implements**

IEnumerable.GetEnumerator
