---
title: Aveva.Pdms.Database.RefTable Class
namespace: Aveva.Pdms.Database
assembly: Aveva.Pdms.Database
kind: Class
source: Aveva.Pdms.Database
---

# Aveva.Pdms.Database.RefTable Class

> Class for scanning of a ref table for a particular DB. The actual scanning of the ref table is performed by getting a RefTableEnumerator and iterating on that

## Syntax

```csharp
public abstract class RefTable : IEnumerable , IDisposable
```

## Inheritance

`System.Object` → `Aveva.Pdms.Database.RefTable`

## Thread Safety

Public static ( Shared in Visual Basic) members of this type are
safe for multithreaded operations. Instance members are not guaranteed to be
thread-safe.

## Requirements

Namespace:
Aveva.Pdms.Database
Assembly: Aveva.Pdms.Database (in Aveva.Pdms.Database.dll)

## Methods

#### `Dispose` Method

```csharp
public abstract void Dispose();
```

**Implements**

IDisposable.Dispose

#### `GetEnumerator` Method

```csharp
public abstract IEnumerator GetEnumerator();
```

**Implements**

IEnumerable.GetEnumerator

#### `GetRefTable` Method (Db, DbAttribute)

Get object that represents the entire ref table for a DB

```csharp
public static RefTable GetRefTable( Db db , DbAttribute att );
```

**Parameters**

- **db** — Db for table
- **att** — identity of ref table

#### `GetRefTable` Method (Db, DbAttribute, DbElement, DbElement)

Get object that represents a range within a ref table for a DB

```csharp
public static RefTable GetRefTable( Db db , DbAttribute att , DbElement firstKey , DbElement lastKey );
```

**Parameters**

- **db** — Db for table
- **att** — identity of ref table
- **firstKey** — Start of range
- **lastKey** — End of range
