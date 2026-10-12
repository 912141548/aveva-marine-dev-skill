---
title: Aveva.Pdms.Database.DbElementTypeListEnum Class
namespace: Aveva.Pdms.Database
assembly: Aveva.Pdms.Database
kind: Class
source: Aveva.Pdms.Database
---

# Aveva.Pdms.Database.DbElementTypeListEnum Class

> Enumerator for the DbElementTypeList class

## Syntax

```csharp
public class DbElementTypeListEnum : IEnumerator
```

## Inheritance

`System.Object` → `Aveva.Pdms.Database.DbElementTypeListEnum`

## Thread Safety

Public static ( Shared in Visual Basic) members of this type are
safe for multithreaded operations. Instance members are not guaranteed to be
thread-safe.

## Requirements

Namespace:
Aveva.Pdms.Database
Assembly: Aveva.Pdms.Database (in Aveva.Pdms.Database.dll)

## Constructors

#### `DbElementTypeListEnum` Constructor

```csharp
public DbElementTypeListEnum( ArrayList mylist );
```

## Fields

#### `list_` Field

```csharp
public ArrayList list_;
```

## Properties

#### `Current` Property

```csharp
public object Current {get;}
```

**Implements**

IEnumerator.Current

## Methods

#### `MoveNext` Method

```csharp
public bool MoveNext();
```

**Implements**

IEnumerator.MoveNext

#### `Reset` Method

```csharp
public void Reset();
```

**Implements**

IEnumerator.Reset
