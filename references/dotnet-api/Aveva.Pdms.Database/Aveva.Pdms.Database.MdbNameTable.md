---
title: Aveva.Pdms.Database.MdbNameTable Class
namespace: Aveva.Pdms.Database
assembly: Aveva.Pdms.Database
kind: Class
source: Aveva.Pdms.Database
---

# Aveva.Pdms.Database.MdbNameTable Class

> Class for scanning a name table representing all dbs of given type within the current MDB. Names are ordered alphabetically. The actual scanning of the name table is performed by getting a MdbNameTableEnumerator and iterating on that.

## Syntax

```csharp
public abstract class MdbNameTable : IEnumerable , IDisposable
```

## Inheritance

`System.Object` → `Aveva.Pdms.Database.MdbNameTable`

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

Get enumerator for this name table. The enumerator can then be used to access values within the table

```csharp
public abstract IEnumerator GetEnumerator();
```

**Implements**

IEnumerable.GetEnumerator

#### `GetMdbNameTable` Method (DbType, DbAttribute)

Get object that represents the entire name table for a MDB

```csharp
public static MdbNameTable GetMdbNameTable( DbType dbtype , DbAttribute att );
```

**Parameters**

- **dbtype** — 
- **att** — identity of name table

#### `GetMdbNameTable` Method (DbType, DbAttribute, String, String)

Get object that represents a range within a name table for a MDB

```csharp
public static MdbNameTable GetMdbNameTable( DbType dbtype , DbAttribute att , string firstName , string lastName );
```

**Parameters**

- **dbtype** — 
- **att** — identity of name table
- **firstName** — Start of range
- **lastName** — End of range
