---
title: Aveva.ApplicationFramework.Presentation.DropTarget Class
namespace: Aveva.ApplicationFramework.Presentation
assembly: Aveva.ApplicationFramework.Presentation
kind: Class
source: Aveva.ApplicationFramework
---

# Aveva.ApplicationFramework.Presentation.DropTarget Class

> A class to represent a DragDropTarget.

## Syntax

```csharp
public abstract class DropTarget
```

## Inheritance

`System.Object` → `Aveva.ApplicationFramework.Presentation.DropTarget`

## Thread Safety

Public static ( Shared in Visual Basic) members of this type are
safe for multithreaded operations. Instance members are not guaranteed to be
thread-safe.

## Requirements

Namespace:
Aveva.ApplicationFramework.Presentation
Assembly: Aveva.ApplicationFramework.Presentation (in Aveva.ApplicationFramework.Presentation.dll)

## Properties

#### `DropTargetType` Property

Gets the DropTarget type.

```csharp
public abstract string DropTargetType {get;}
```

## Methods

#### `RaiseDragDrop` Method

Raise a DragDrop event for this DropTarget.

```csharp
public abstract void RaiseDragDrop( DropTargetEventArgs args );
```

**Parameters**

- **args** — Event arguments

#### `RaiseDragEnter` Method

Raise a DragEnter event for this DropTarget.

```csharp
public abstract void RaiseDragEnter( DropTargetEventArgs args );
```

**Parameters**

- **args** — Event arguments

## Events

#### `DragDrop` Event

Occurs when an object is droopped onto the DropTargets.

```csharp
public event DropTargetEventHandler DragDrop;
```

#### `DragEnter` Event

Occurs when an object is dragged into the DropTargets bounds.

```csharp
public event DropTargetEventHandler DragEnter;
```
