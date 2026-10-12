---
title: Aveva.ApplicationFramework.Presentation.ToolEventArgs Class
namespace: Aveva.ApplicationFramework.Presentation
assembly: Aveva.ApplicationFramework.Presentation
kind: Class
source: Aveva.ApplicationFramework
---

# Aveva.ApplicationFramework.Presentation.ToolEventArgs Class

> Provides information for Tool events.

## Syntax

```csharp
public class ToolEventArgs : EventArgs
```

## Inheritance

`System.Object` → `System.EventArgs` → `Aveva.ApplicationFramework.Presentation.ToolEventArgs`

## Thread Safety

Public static ( Shared in Visual Basic) members of this type are
safe for multithreaded operations. Instance members are not guaranteed to be
thread-safe.

## Requirements

Namespace:
Aveva.ApplicationFramework.Presentation
Assembly: Aveva.ApplicationFramework.Presentation (in Aveva.ApplicationFramework.Presentation.dll)

## Constructors

#### `ToolEventArgs` Constructor

```csharp
public ToolEventArgs( string key );
```

**Parameters**

- **key** —

## Properties

#### `Key` Property

The tools key.

```csharp
public string Key {get;}
```
