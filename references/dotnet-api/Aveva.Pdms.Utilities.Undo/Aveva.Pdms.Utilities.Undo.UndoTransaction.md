---
title: Aveva.Pdms.Utilities.Undo.UndoTransaction Class
namespace: Aveva.Pdms.Utilities.Undo
assembly: Aveva.Pdms.Utilities
kind: Class
source: Aveva.Pdms.Utilities
---

# Aveva.Pdms.Utilities.Undo.UndoTransaction Class

> This class is used to: a) Start and end an UndoTransaction transaction b) Static method to Clear all transactions c) Static method to denote that a significant event is about to happen

## Syntax

```csharp
public abstract class UndoTransaction
```

## Inheritance

`System.Object` → `Aveva.Pdms.Utilities.Undo.UndoTransaction`

## Thread Safety

Public static ( Shared in Visual Basic) members of this type are
safe for multithreaded operations. Instance members are not guaranteed to be
thread-safe.

## Requirements

Namespace:
Aveva.Pdms.Utilities.Undo
Assembly: Aveva.Pdms.Utilities (in Aveva.Pdms.Utilities.dll)

## Methods

#### `EndTransaction` Method

End an Undo Transaction

```csharp
public abstract void EndTransaction();
```

#### `GetUndoTransaction` Method

Get Transaction Object

```csharp
public static UndoTransaction GetUndoTransaction();
```

#### `PerformRedo` Method

Do Redo

```csharp
public static void PerformRedo();
```

#### `PerformUndo` Method

Do Undo

```csharp
public static void PerformUndo();
```

#### `StartTransaction` Method

Start an Undo Transaction Any existing transaction will be ended

```csharp
public abstract void StartTransaction( string description );
```
