---
title: Aveva.Pdms.Database.DbGetWorkChangesEventArgs Class
namespace: Aveva.Pdms.Database
assembly: Aveva.Pdms.Database
kind: Class
source: Aveva.Pdms.Database
---

# Aveva.Pdms.Database.DbGetWorkChangesEventArgs Class

> Deprecated - do not use

## Syntax

```csharp
public class DbGetWorkChangesEventArgs : EventArgs
```

## Inheritance

`System.Object` → `System.EventArgs` → `Aveva.Pdms.Database.DbGetWorkChangesEventArgs`

## Thread Safety

Public static ( Shared in Visual Basic) members of this type are
safe for multithreaded operations. Instance members are not guaranteed to be
thread-safe.

## Requirements

Namespace:
Aveva.Pdms.Database
Assembly: Aveva.Pdms.Database (in Aveva.Pdms.Database.dll)

## Constructors

#### `DbGetWorkChangesEventArgs` Constructor

Constructor.

```csharp
public DbGetWorkChangesEventArgs( Db db , DbRawChanges changeList , int previousSession , int newSession );
```

**Parameters**

- **db** — Database
- **changeList** — Raw change list
- **previousSession** — Previous session number
- **newSession** — New session number

## Properties

#### `ChangeList` Property

Raw change list

```csharp
public DbRawChanges ChangeList {get;}
```

#### `DB` Property

Database

```csharp
public Db DB {get;}
```

#### `NewSessionNumber` Property

New session number

```csharp
public int NewSessionNumber {get;}
```

#### `PreviousSessionNumber` Property

Previous session number

```csharp
public int PreviousSessionNumber {get;}
```
