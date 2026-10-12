---
title: Aveva.ApplicationFramework.Presentation.WindowEventArgs Class
namespace: Aveva.ApplicationFramework.Presentation
assembly: Aveva.ApplicationFramework.Presentation
kind: Class
source: Aveva.ApplicationFramework
---

# Aveva.ApplicationFramework.Presentation.WindowEventArgs Class

> Provides data for the WindowAdded event.

## Syntax

```csharp
public class WindowEventArgs : EventArgs
```

## Inheritance

`System.Object` → `System.EventArgs` → `Aveva.ApplicationFramework.Presentation.WindowEventArgs`

## Thread Safety

Public static ( Shared in Visual Basic) members of this type are
safe for multithreaded operations. Instance members are not guaranteed to be
thread-safe.

## Requirements

Namespace:
Aveva.ApplicationFramework.Presentation
Assembly: Aveva.ApplicationFramework.Presentation (in Aveva.ApplicationFramework.Presentation.dll)

## Constructors

#### `WindowEventArgs` Constructor

Initialize a new instance of a WindowEventArgs class

```csharp
public WindowEventArgs( IWindow window );
```

**Parameters**

- **window** — The IWindow object

## Properties

#### `Window` Property

Gets the Window object associated with the event

```csharp
public IWindow Window {get;}
```
