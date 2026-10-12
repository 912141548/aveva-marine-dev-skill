---
title: Aveva.Pdms.Database.MDB Class
namespace: Aveva.Pdms.Database
assembly: Aveva.Pdms.Database
kind: Class
source: Aveva.Pdms.Database
---

# Aveva.Pdms.Database.MDB Class

> Representation of an MDB The MDB is accessed via the currentMDB N.B. most methods do not return anything useful until the MDB is opened. (class needs to be remnmed Mdb rather than MDB, similarly MDBSetup should be MdbSetup )

## Syntax

```csharp
public abstract class MDB
```

## Inheritance

`System.Object` → `Aveva.Pdms.Database.MDB`

## Thread Safety

Public static ( Shared in Visual Basic) members of this type are
safe for multithreaded operations. Instance members are not guaranteed to be
thread-safe.

## Requirements

Namespace:
Aveva.Pdms.Database
Assembly: Aveva.Pdms.Database (in Aveva.Pdms.Database.dll)

## Fields

#### `CurrentMDB` Field

Get hold of the current MDB. This is the only way to get at an MDB object.

```csharp
public static readonly MDB CurrentMDB;
```

## Properties

#### `MdbElement` Property

DbElement corresponding to %MDB element in system DB. Various attributes can be queried off this.

```csharp
public abstract DbElement MdbElement {get;}
```

#### `Name` Property

Return MDB name.

```csharp
public abstract string Name {get;}
```

#### `SetUp` Property

MDdbSetup object used to open the MDB.

```csharp
public abstract MDBSetup SetUp {get;}
```

## Methods

#### `Claim` Method

Claim elements. If claim fails, the method will still claim what it can.

```csharp
public abstract bool Claim( DbElement[] elements );
```

**Parameters**

- **elements** —

#### `Close` Method

Close MDB.

```csharp
public abstract void Close();
```

#### `DefaultType` Method

Retrieve the default DB type. e.g. DESI, CATA etc

```csharp
public abstract DbType DefaultType();
```

#### `Drop` Method

Drop changes from extract. Drop is actually done on a DB by DB basis. If a drop of a DB fails no changes will be droped for that DB. If a Drop of one DB fails, the others will still be done.

```csharp
public abstract bool Drop( DbElement[] elements , string comment );
```

**Parameters**

- **elements** — 
- **comment** —

#### `ExtractClaim` Method

Extract Claim elements. If claim fails, the method will still claim what it can

```csharp
public abstract bool ExtractClaim( DbElement[] elements );
```

**Parameters**

- **elements** —

#### `ExtractRelease` Method

Extract Release elements. If release fails, the method will still release what it can.

```csharp
public abstract bool ExtractRelease( DbElement[] elements );
```

**Parameters**

- **elements** —

#### `FindElements` Method (DbType, DbAttribute, Int32[])

Return all elements where name matches given int key.

```csharp
public abstract DbElement[] FindElements( DbType type , DbAttribute att , int[] key );
```

**Parameters**

- **type** — 
- **att** — 
- **key** — 

#### `FindElements` Method (DbType, DbAttribute, String)

Return all elements where given attribute matches given string key.

```csharp
public abstract DbElement[] FindElements( DbType type , DbAttribute att , string key );
```

**Parameters**

- **type** — 
- **att** — 
- **key** — 

#### `FindElements` Method (DbType, String)

Return all elements where name matches given string key.

```csharp
public abstract DbElement[] FindElements( DbType type , string Name );
```

**Parameters**

- **type** — 
- **Name** —

#### `Flush` Method

Flush changes from extract. Flush is actually done on a DB by DB basis. If a flush of a DB fails no changes will be flushed for that DB. If a flush of one DB fails, the others will still be done.

```csharp
public abstract bool Flush( DbElement[] elements , string comment );
```

**Parameters**

- **elements** — 
- **comment** —

#### `GetDB` Method

Find the DB of a given number.

```csharp
public abstract Db GetDB( int dbNumber );
```

**Parameters**

- **dbNumber** —

#### `GetDBArray` Method ()

List of DBs in MDB.

```csharp
public abstract Db[] GetDBArray();
```

#### `GetDBArray` Method (DbType)

List of DBs in MDB of given type.

```csharp
public abstract Db[] GetDBArray( DbType type );
```

**Parameters**

- **type** —

#### `GetFirstDB` Method

Get First DB of given type.

```csharp
public abstract Db GetFirstDB( DbType type );
```

**Parameters**

- **type** —

#### `GetFirstWorld` Method

Get First world on given type.

```csharp
public abstract DbElement GetFirstWorld( DbType type );
```

**Parameters**

- **type** —

#### `GetLastDB` Method

Get Last DB of given type.

```csharp
public abstract Db GetLastDB( DbType type );
```

**Parameters**

- **type** —

#### `GetNextDB` Method (Db)

Get next DB of the same type.

```csharp
public Db GetNextDB( Db database );
```

**Parameters**

- **database** — 

#### `GetNextDB` Method (Db, DbType)

Get Next DB of given type.

```csharp
public abstract Db GetNextDB( Db database , DbType type );
```

**Parameters**

- **database** — 
- **type** —

#### `GetPreviousDB` Method (Db)

Get previous DB of the same type.

```csharp
public Db GetPreviousDB( Db database );
```

**Parameters**

- **database** — 

#### `GetPreviousDB` Method (Db, DbType)

Get Previous DB of given type.

```csharp
public abstract Db GetPreviousDB( Db database , DbType type );
```

**Parameters**

- **database** — 
- **type** —

#### `GetWork` Method ()

GetWork for all MDB.

```csharp
public abstract bool GetWork();
```

#### `GetWork` Method (Db[])

GetWork for given DBs.

```csharp
public abstract bool GetWork( Db[] dbs );
```

#### `Issue` Method

Issue changes from extract. Issue is actually done on a DB by DB basis. If an issue of a DB fails no changes will be issued for that DB. If an issue of one DB fails, the others will still be done.

```csharp
public abstract bool Issue( DbElement[] elements , string comment );
```

**Parameters**

- **elements** — 
- **comment** —

#### `Open` Method

Open MDB.

```csharp
public abstract void Open( MDBSetup setup );
```

**Parameters**

- **setup** —

#### `QuitWork` Method ()

Quit all changes.

```csharp
public abstract bool QuitWork();
```

#### `QuitWork` Method (Db[])

QuitWork for given DBs

```csharp
public abstract bool QuitWork( Db[] dbs );
```

#### `Refresh` Method (Db[], String)

Extract refresh specific DBs. Refresh is actually done on a DB by DB basis. If a refresh of a DB fails no changes will be refreshed for that DB. If a Refresh of one DB fails, the others will still be done.

```csharp
public abstract bool Refresh( Db[] dbs , string comment );
```

**Parameters**

- **dbs** — 
- **comment** — 

#### `Refresh` Method (String)

Refresh dbs.

```csharp
public abstract bool Refresh( string comment );
```

**Parameters**

- **comment** —

#### `Release` Method

Release elements. If release fails, the method will still release what it can.

```csharp
public abstract bool Release( DbElement[] elements );
```

**Parameters**

- **elements** —

#### `ReleaseAll` Method

Release All elements. If release fails, the method will still release what it can.

```csharp
public abstract bool ReleaseAll();
```

#### `RetrieveErrors` Method

Retrieve errors after a failed operation. i.e. where the method returns false.

```csharp
public abstract PdmsMessage[] RetrieveErrors();
```

#### `SaveWork` Method (Db[], String)

Savework on specific Dbs. If a save of one DB fails, the others will still be done. Returns false if one of DB fails, use RetrieveErrors() in this case.

```csharp
public abstract bool SaveWork( Db[] dbs , string comment );
```

**Parameters**

- **dbs** — 
- **comment** — 

#### `SaveWork` Method (String)

Save all changes. Savework is actually done on a DB by DB basis. If a save of one DB fails, the others will still be done.

```csharp
public abstract bool SaveWork( string comment );
```

**Parameters**

- **comment** —

#### `UpdateClaimsToLatest` Method

Ensure that we are using the latest version of the claimlist Only needed prior to single claim queries

```csharp
public abstract void UpdateClaimsToLatest();
```

#### `WriteMode` Method

Get the write mode for DBs of given type.

```csharp
public abstract DbWriteMode WriteMode( DbType type );
```

**Parameters**

- **type** —
