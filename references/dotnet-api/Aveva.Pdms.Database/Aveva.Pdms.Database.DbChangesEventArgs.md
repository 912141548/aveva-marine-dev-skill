---
title: Aveva.Pdms.Database.DbChangesEventArgs Class
namespace: Aveva.Pdms.Database
assembly: Aveva.Pdms.Database
kind: Class
source: Aveva.Pdms.Database
---

# Aveva.Pdms.Database.DbChangesEventArgs Class

> Deprecated - do not use

## Syntax

```csharp
public class DbChangesEventArgs : EventArgs
```

## Inheritance

`System.Object` → `System.EventArgs` → `Aveva.Pdms.Database.DbChangesEventArgs`

## Thread Safety

Public static ( Shared in Visual Basic) members of this type are
safe for multithreaded operations. Instance members are not guaranteed to be
thread-safe.

## Requirements

Namespace:
Aveva.Pdms.Database
Assembly: Aveva.Pdms.Database (in Aveva.Pdms.Database.dll)

## Constructors

#### `DbChangesEventArgs` Constructor

Constructor.

```csharp
public DbChangesEventArgs( DbUserChanges changeList );
```

**Parameters**

- **changeList** — User change list

## Properties

#### `ChangeList` Property

User change list.

```csharp
public DbUserChanges ChangeList {get;}
```
