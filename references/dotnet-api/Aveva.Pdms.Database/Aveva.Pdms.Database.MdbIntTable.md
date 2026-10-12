---
title: Aveva.Pdms.Database.MdbIntTable Class
namespace: Aveva.Pdms.Database
assembly: Aveva.Pdms.Database
kind: Class
source: Aveva.Pdms.Database
---

# Aveva.Pdms.Database.MdbIntTable Class

> Class for scanning an integer table representing all dbs of given type within the current MDB. The actual scanning of the name table is performed by getting a MdbIntTableEnumerator and iterating on that

## Syntax

```csharp
public abstract class MdbIntTable : IEnumerable , IDisposable
```

## Inheritance

`System.Object` → `Aveva.Pdms.Database.MdbIntTable`

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

Get enumerator for this integer table. The enumerator can then be used to access values within the table

```csharp
public abstract IEnumerator GetEnumerator();
```

**Implements**

IEnumerable.GetEnumerator

#### `GetMdbIntTable` Method (DbType, DbAttribute)

Get object that represents the entire integer table for entire MDB

```csharp
public static MdbIntTable GetMdbIntTable( DbType dbtype , DbAttribute att );
```

**Parameters**

- **dbtype** — 
- **att** — identity of integer table

#### `GetMdbIntTable` Method (DbType, DbAttribute, Int32, Int32)

Get object that represents a range within a integer table for entire MDB

```csharp
public static MdbIntTable GetMdbIntTable( DbType dbtype , DbAttribute att , int firstKey , int lastKey );
```

**Parameters**

- **dbtype** — Db type
- **att** — identity of integer table
- **firstKey** — Start of range
- **lastKey** — End of range
