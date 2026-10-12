---
title: Aveva.ApplicationFramework.Presentation.CommandBarEventArgs Class
namespace: Aveva.ApplicationFramework.Presentation
assembly: Aveva.ApplicationFramework.Presentation
kind: Class
source: Aveva.ApplicationFramework
---

# Aveva.ApplicationFramework.Presentation.CommandBarEventArgs Class

> Provides data for the CommandBarAdded and CommandBarRemoved events.

## Syntax

```csharp
public class CommandBarEventArgs : EventArgs
```

## Inheritance

`System.Object` → `System.EventArgs` → `Aveva.ApplicationFramework.Presentation.CommandBarEventArgs`

## Thread Safety

Public static ( Shared in Visual Basic) members of this type are
safe for multithreaded operations. Instance members are not guaranteed to be
thread-safe.

## Requirements

Namespace:
Aveva.ApplicationFramework.Presentation
Assembly: Aveva.ApplicationFramework.Presentation (in Aveva.ApplicationFramework.Presentation.dll)

## Constructors

#### `CommandBarEventArgs` Constructor

Initialize a new instance of a CommandBarEventArgs class

```csharp
public CommandBarEventArgs( CommandBar cbar );
```

**Parameters**

- **cbar** — The CommandBar object

## Properties

#### `CommandBar` Property

Gets the CommandBar object associated with the event

```csharp
public CommandBar CommandBar {get;}
```
