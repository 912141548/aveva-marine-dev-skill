---
title: Aveva.ApplicationFramework.Presentation.DragDropDirector Class
namespace: Aveva.ApplicationFramework.Presentation
assembly: Aveva.ApplicationFramework.Presentation
kind: Class
source: Aveva.ApplicationFramework
---

# Aveva.ApplicationFramework.Presentation.DragDropDirector Class

> A class to help direct drag-drop events.

## Syntax

```csharp
public abstract class DragDropDirector
```

## Inheritance

`System.Object` → `Aveva.ApplicationFramework.Presentation.DragDropDirector`

## Thread Safety

Public static ( Shared in Visual Basic) members of this type are
safe for multithreaded operations. Instance members are not guaranteed to be
thread-safe.

## Requirements

Namespace:
Aveva.ApplicationFramework.Presentation
Assembly: Aveva.ApplicationFramework.Presentation (in Aveva.ApplicationFramework.Presentation.dll)

## Methods

#### `RegisterDropTarget` Method

Registers a new DropTarget with the DragDropDirector.

```csharp
public abstract DropTarget RegisterDropTarget( string targetType );
```

**Parameters**

- **targetType** —

#### `UnregisterDropTarget` Method

Unregisters a DropTarget from the DragDropDirector.

```csharp
public abstract void UnregisterDropTarget( DropTarget target );
```

**Parameters**

- **target** —

## Events

#### `DropTargetRegistered` Event

Occurs when a new DropTarget is registered with the DragDropDirector.

```csharp
public event DropTargetEventHandler DropTargetRegistered;
```

#### `DropTargetUnregistered` Event

Occurs when a DropTarget is unregistered from the DragDropDirector.

```csharp
public event DropTargetEventHandler DropTargetUnregistered;
```
