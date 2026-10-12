---
title: Aveva.PDMS.Database.Filters.DBElementEnumerator Class
namespace: Aveva.PDMS.Database.Filters
assembly: PDMSFilters
kind: Class
source: Aveva.Pdms.Database.Filters
---

# Aveva.PDMS.Database.Filters.DBElementEnumerator Class

> Enumerator to iterate through a scan defined by the DBElementCollection class.

## Syntax

```csharp
public class DBElementEnumerator : IEnumerator
```

## Inheritance

`System.Object` → `Aveva.PDMS.Database.Filters.DBElementEnumerator`

## Thread Safety

Public static ( Shared in Visual Basic) members of this type are
safe for multithreaded operations. Instance members are not guaranteed to be
thread-safe.

## Requirements

Namespace:
Aveva.PDMS.Database.Filters
Assembly: PDMSFilters (in PDMSFilters.dll)

## Properties

#### `CountSoFar` Property

number of elements passing filter so far

```csharp
public int CountSoFar {get;}
```

#### `Current` Property

return element at current position.

```csharp
public object Current {get;}
```

**Implements**

IEnumerator.Current

#### `Scanned` Property

Total number of elements the the enumerator naviagated over, regardless of whether they satisfied the filter.

```csharp
public int Scanned {get;}
```

## Methods

#### `MoveNext` Method

Move to next element that satisfies the filter.

```csharp
public bool MoveNext();
```

**Implements**

IEnumerator.MoveNext

#### `Reset` Method

Reset enumerator to start of scan.

```csharp
public void Reset();
```

**Implements**

IEnumerator.Reset
