---
title: Aveva.Pdms.Database.DbUndoChangesEventArgs Class
namespace: Aveva.Pdms.Database
assembly: Aveva.Pdms.Database
kind: Class
source: Aveva.Pdms.Database
---

# Aveva.Pdms.Database.DbUndoChangesEventArgs Class

> Deprecated - do not use

## Syntax

```csharp
public class DbUndoChangesEventArgs : EventArgs
```

## Inheritance

`System.Object` → `System.EventArgs` → `Aveva.Pdms.Database.DbUndoChangesEventArgs`

## Thread Safety

Public static ( Shared in Visual Basic) members of this type are
safe for multithreaded operations. Instance members are not guaranteed to be
thread-safe.

## Requirements

Namespace:
Aveva.Pdms.Database
Assembly: Aveva.Pdms.Database (in Aveva.Pdms.Database.dll)

## Constructors

#### `DbUndoChangesEventArgs` Constructor

```csharp
public DbUndoChangesEventArgs( DbRawChanges changeList , int markNumer );
```

**Parameters**

- **changeList** — 
- **markNumer** —

## Properties

#### `ChangeList` Property

```csharp
public DbRawChanges ChangeList {get;}
```

#### `MarkNumber` Property

```csharp
public int MarkNumber {get;}
```
