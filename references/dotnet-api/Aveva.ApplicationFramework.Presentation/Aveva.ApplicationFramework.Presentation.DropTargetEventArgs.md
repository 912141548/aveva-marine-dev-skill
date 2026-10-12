---
title: Aveva.ApplicationFramework.Presentation.DropTargetEventArgs Class
namespace: Aveva.ApplicationFramework.Presentation
assembly: Aveva.ApplicationFramework.Presentation
kind: Class
source: Aveva.ApplicationFramework
---

# Aveva.ApplicationFramework.Presentation.DropTargetEventArgs Class

> A class to provide information to for drop-drop events.

## Syntax

```csharp
public class DropTargetEventArgs : EventArgs
```

## Inheritance

`System.Object` → `System.EventArgs` → `Aveva.ApplicationFramework.Presentation.DropTargetEventArgs`

## Thread Safety

Public static ( Shared in Visual Basic) members of this type are
safe for multithreaded operations. Instance members are not guaranteed to be
thread-safe.

## Requirements

Namespace:
Aveva.ApplicationFramework.Presentation
Assembly: Aveva.ApplicationFramework.Presentation (in Aveva.ApplicationFramework.Presentation.dll)

## Constructors

#### `DropTargetEventArgs` Constructor

Initialize a new instance of a DropTargetEventArgs class

```csharp
public DropTargetEventArgs( DropTarget target );
```

**Parameters**

- **target** — The DropTaget object

## Fields

#### `Data` Field

Data object used to encapslate the object being dropped

```csharp
public IDataObject Data;
```

#### `DragDropEffect` Field

The target drop effect in a drag-and-drop operation.

```csharp
public DragDropEffects DragDropEffect;
```

#### `DragEventArgs` Field

The windows DragEventArgs object

```csharp
public DragEventArgs DragEventArgs;
```

#### `IsValidDropTarget` Field

Boolean used to indicate if drop target is valid for a particular DataObject

```csharp
public bool IsValidDropTarget;
```

#### `Target` Field

The DropTarget object

```csharp
public DropTarget Target;
```
