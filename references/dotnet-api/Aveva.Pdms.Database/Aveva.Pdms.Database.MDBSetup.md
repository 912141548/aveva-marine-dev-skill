---
title: Aveva.Pdms.Database.MDBSetup Class
namespace: Aveva.Pdms.Database
assembly: Aveva.Pdms.Database
kind: Class
source: Aveva.Pdms.Database
---

# Aveva.Pdms.Database.MDBSetup Class

> Class to store options when opening an MDB.

## Syntax

```csharp
public abstract class MDBSetup
```

## Inheritance

`System.Object` → `Aveva.Pdms.Database.MDBSetup`

## Thread Safety

Public static ( Shared in Visual Basic) members of this type are
safe for multithreaded operations. Instance members are not guaranteed to be
thread-safe.

## Requirements

Namespace:
Aveva.Pdms.Database
Assembly: Aveva.Pdms.Database (in Aveva.Pdms.Database.dll)

## Properties

#### `DefaultType` Property

Default database type. e.g. Design. This affects the initial position in the database.

```csharp
public abstract DbType DefaultType {get; set;}
```

#### `Name` Property

MDB name

```csharp
public abstract string Name {get; set;}
```

#### `ReadOnly` Property

ReadOnly or not. If set then all DBs will be opened in read.

```csharp
public abstract bool ReadOnly {get; set;}
```

#### `ReadTypes` Property

DbTypes to open in read

```csharp
public abstract DbType[] ReadTypes {get; set;}
```

#### `Stamp` Property

Stamp at which to open the MDB

```csharp
public abstract string Stamp {get; set;}
```

#### `Subtype` Property

Subtype, i.e. marine or not.

```csharp
public abstract int Subtype {get; set;}
```

#### `WriteTypes` Property

DbTypes to open in write.

```csharp
public abstract DbType[] WriteTypes {get; set;}
```

## Methods

#### `CreateMDBSetup` Method

Create instance of an MDBSetup passing in MDB name

```csharp
public static MDBSetup CreateMDBSetup( string name );
```

**Parameters**

- **name** —
