---
title: Aveva.Pdms.Utilities.Undo.UndoSubscriber Class
namespace: Aveva.Pdms.Utilities.Undo
assembly: Aveva.Pdms.Utilities
kind: Class
source: Aveva.Pdms.Utilities
---

# Aveva.Pdms.Utilities.Undo.UndoSubscriber Class

> For a start transaction- GetStartState() will be invoked.

## Syntax

```csharp
public abstract class UndoSubscriber
```

## Inheritance

`System.Object` → `Aveva.Pdms.Utilities.Undo.UndoSubscriber`

## Thread Safety

Public static ( Shared in Visual Basic) members of this type are
safe for multithreaded operations. Instance members are not guaranteed to be
thread-safe.

## Requirements

Namespace: Aveva.Pdms.Utilities.Undo
Assembly: Aveva.Pdms.Utilities (in Aveva.Pdms.Utilities.dll)

## Constructors

#### `UndoSubscriber` Constructor

Initializes a new instance of the UndoSubscriber class.

```csharp
public UndoSubscriber();
```

## Methods

#### `GetBeginState` Method

GetStartState() will be called on start transaction. It should return the current state.

```csharp
public abstract object GetBeginState();
```

#### `GetEndState` Method

GetStartState() will be called on end transaction. It should return the current state.

```csharp
public abstract object GetEndState();
```

#### `RestoreBeginState` Method

RestoreStartState() will be called on undo of that transaction. It should restore the passed state.

```csharp
public abstract void RestoreBeginState( object obj );
```

#### `RestoreEndState` Method

RestoreEndState() will be called on undo of that transaction. It should restore the passed state.

```csharp
public abstract void RestoreEndState( object obj );
```
