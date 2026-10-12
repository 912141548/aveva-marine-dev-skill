---
title: Aveva.Pdms.Database.IntTable Class
namespace: Aveva.Pdms.Database
assembly: Aveva.Pdms.Database
kind: Class
source: Aveva.Pdms.Database
---

# Aveva.Pdms.Database.IntTable Class

> Class for scanning an integer table for a particular DB. The actual scanning of the name table is performed by getting a IntTableEnumerator and iterating on that

## Syntax

```csharp
public abstract class IntTable : IEnumerable , IDisposable
```

## Inheritance

`System.Object` → `Aveva.Pdms.Database.IntTable`

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

#### `GetIntTable` Method (Db, DbAttribute)

Get object that represents the entire integer table for a DB

```csharp
public static IntTable GetIntTable( Db db , DbAttribute att );
```

**Parameters**

- **db** — Db for table
- **att** — identity of integer table

#### `GetIntTable` Method (Db, DbAttribute, Int32, Int32)

Get object that represents a range within a integer table for a DB

```csharp
public static IntTable GetIntTable( Db db , DbAttribute att , int firstKey , int lastKey );
```

**Parameters**

- **db** — Db for table
- **att** — identity of integer table
- **firstKey** — Start of range
- **lastKey** — End of range
