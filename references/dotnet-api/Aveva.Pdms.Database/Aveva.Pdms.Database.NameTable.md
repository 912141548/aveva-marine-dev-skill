---
title: Aveva.Pdms.Database.NameTable Class
namespace: Aveva.Pdms.Database
assembly: Aveva.Pdms.Database
kind: Class
source: Aveva.Pdms.Database
---

# Aveva.Pdms.Database.NameTable Class

> Class for scanning a name table for a particular DB. Names are ordered alphabetically. The actual scanning of the name table is performed by getting a NameTableEnumerator and iterating on that.

## Syntax

```csharp
public abstract class NameTable : IEnumerable , IDisposable
```

## Inheritance

`System.Object` → `Aveva.Pdms.Database.NameTable`

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

#### `GetNameTable` Method (Db, DbAttribute)

Get object that represents entire name table for a DB

```csharp
public static NameTable GetNameTable( Db db , DbAttribute att );
```

**Parameters**

- **db** — Db for table
- **att** — identity of name table

#### `GetNameTable` Method (Db, DbAttribute, String, String)

Get object that represents a range within a name table for a DB

```csharp
public static NameTable GetNameTable( Db db , DbAttribute att , string firstName , string lastName );
```

**Parameters**

- **db** — Db for table
- **att** — identity of name table
- **firstName** — Start of range
- **lastName** — End of range
