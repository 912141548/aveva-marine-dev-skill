---
title: Aveva.ApplicationFramework.Presentation.CancelClosingEventArgs Class
namespace: Aveva.ApplicationFramework.Presentation
assembly: Aveva.ApplicationFramework.Presentation
kind: Class
source: Aveva.ApplicationFramework
---

# Aveva.ApplicationFramework.Presentation.CancelClosingEventArgs Class

> Provides data for a cancelable event.

## Syntax

```csharp
public class CancelClosingEventArgs : CancelEventArgs
```

## Inheritance

`System.Object` → `System.EventArgs` → `System.ComponentModel.CancelEventArgs` → `Aveva.ApplicationFramework.Presentation.CancelClosingEventArgs`

## Thread Safety

Public static ( Shared in Visual Basic) members of this type are
safe for multithreaded operations. Instance members are not guaranteed to be
thread-safe.

## Requirements

Namespace:
Aveva.ApplicationFramework.Presentation
Assembly: Aveva.ApplicationFramework.Presentation (in Aveva.ApplicationFramework.Presentation.dll)

## Constructors

#### `CancelClosingEventArgs` Constructor

```csharp
public CancelClosingEventArgs();
```

## Properties

#### `ParentClosing` Property

Indicates if the closing event was raised as a result of closing the main window.

```csharp
public bool ParentClosing {get; set;}
```
