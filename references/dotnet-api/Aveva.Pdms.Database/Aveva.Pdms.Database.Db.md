---
title: Aveva.Pdms.Database.Db Class
namespace: Aveva.Pdms.Database
assembly: Aveva.Pdms.Database
kind: Class
source: Aveva.Pdms.Database
---

# Aveva.Pdms.Database.Db Class

> This class provides information on the opened DB Additional information on the DB (e.g foreign, size, extractParent etc) can be obtain from the %DB DbElement object Some of the information avialable on the %DB object is also repeated here for conveniance, e.g. DBnumber, type. If the MDB is closed, the Db and DbSession objects will no longer be valid. Methods relating to savework, claims, extract operations are available via the MDB class

## Syntax

```csharp
public abstract class Db
```

## Inheritance

`System.Object` → `Aveva.Pdms.Database.Db`

## Thread Safety

Public static ( Shared in Visual Basic) members of this type are
safe for multithreaded operations. Instance members are not guaranteed to be
thread-safe.

## Requirements

Namespace:
Aveva.Pdms.Database
Assembly: Aveva.Pdms.Database (in Aveva.Pdms.Database.dll)

## Properties

#### `CurrentSession` Property

Current session on this Database

```csharp
public abstract DbSession CurrentSession {get;}
```

#### `DbItem` Property

System Database Element that represents this Database. Various queries are available from this.

```csharp
public abstract DbElement DbItem {get;}
```

#### `ExtractNumber` Property

Extract number (integer)

```csharp
public abstract int ExtractNumber {get;}
```

#### `HasChangedThisSession` Property

True, if there are changes in this Database in the current session

```csharp
public abstract bool HasChangedThisSession {get;}
```

#### `IsExtract` Property

True, if this Database is an extract database

```csharp
public abstract bool IsExtract {get;}
```

#### `IsReadOnly` Property

True, if this Database is read-only

```csharp
public abstract bool IsReadOnly {get;}
```

#### `LatestSessionOnDb` Property

Most recent session on this Database

```csharp
public abstract DbSession LatestSessionOnDb {get;}
```

#### `Name` Property

Database name

```csharp
public abstract string Name {get;}
```

**Remarks**

(replace by ToString(). Exclude the /* at start - PDC)

#### `Number` Property

Database number (integer)

```csharp
public abstract int Number {get;}
```

#### `Type` Property

Database type

```csharp
public abstract DbType Type {get;}
```

#### `World` Property

Root "world" Element for this Database

```csharp
public abstract DbElement World {get;}
```

## Methods

#### `ElementExists` Method

Query whether the named Element exists in this Database.

```csharp
public abstract bool ElementExists( string name , DbAttribute attributeName );
```

**Parameters**

- **name** — Element name
- **attributeName** — Attribute

**Return Value**

True, if Element exists

**Remarks**

(Not sure why we have this method. It would be better to replace it with FindElement- PDC)

#### `FindElement` Method

Find Element of given name. If it does not exits then returns a null element.

```csharp
public abstract DbElement FindElement( string Name , DbAttribute attributeName );
```

**Parameters**

- **Name** — Element name
- **attributeName** — Attribute

**Return Value**

Element instance

#### `Session` Method (Int32)

Get numbered session from this Database.

```csharp
public abstract DbSession Session( int sessionNumber );
```

**Parameters**

- **sessionNumber** — 

**Remarks**

(PDC-should raise an exception if session is invalid)

#### `Session` Method (Int32, Int32)

Get numbered session on extract, from this Database.

```csharp
public abstract DbSession Session( int extractNumber , int sessionNumber );
```

**Parameters**

- **extractNumber** — Extract number
- **sessionNumber** — Session Number

**Return Value**

Session

**Remarks**

(PDC-should raise an exception if session is invalid)

#### `SessionBeforeDate` Method

Return most recent session before Date-Time, from this Database

```csharp
public abstract DbSession SessionBeforeDate( DateTime date );
```

**Parameters**

- **date** — Date-Time deadline

**Return Value**

Session

#### `WorldMembers` Method

Get child Elements of the World element of this Database. N.B. the normal query for members of a world goes across Databases.

```csharp
public abstract DbElement[] WorldMembers();
```

**Return Value**

Array of Elements
