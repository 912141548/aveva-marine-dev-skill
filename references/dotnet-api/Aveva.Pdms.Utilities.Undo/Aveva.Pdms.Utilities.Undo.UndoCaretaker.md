---
title: Aveva.Pdms.Utilities.Undo.UndoCaretaker Class
namespace: Aveva.Pdms.Utilities.Undo
assembly: Aveva.Pdms.Utilities
kind: Class
source: Aveva.Pdms.Utilities
---

# Aveva.Pdms.Utilities.Undo.UndoCaretaker Class

> This class registers any UndoSubscribers

## Syntax

```csharp
public abstract class UndoCaretaker
```

## Inheritance

`System.Object` → `Aveva.Pdms.Utilities.Undo.UndoCaretaker`

## Thread Safety

Public static ( Shared in Visual Basic) members of this type are
safe for multithreaded operations. Instance members are not guaranteed to be
thread-safe.

## Requirements

Namespace:
Aveva.Pdms.Utilities.Undo
Assembly: Aveva.Pdms.Utilities (in Aveva.Pdms.Utilities.dll)

## Methods

#### `ClearAllTransactions` Method

Clear all Undo Transactions as they are no longer valid

```csharp
public static void ClearAllTransactions();
```

#### `RegisterUndoSubscriber` Method

Register a subscriber

```csharp
public static void RegisterUndoSubscriber( UndoSubscriber subscriber );
```

**Parameters**

- **subscriber** — subscriber instance

#### `RemoveUndoSubscriber` Method

Remove a subscriber

```csharp
public static void RemoveUndoSubscriber( UndoSubscriber subscriber );
```

**Parameters**

- **subscriber** — subscriber instance

#### `SignificantEventAboutToHappen` Method

Signal that a Significant Event is about to happen. The consequences of this are: a) Clears the redo stack b) Starts a transaction if not already started.

```csharp
public static void SignificantEventAboutToHappen();
```
