---
title: Aveva.ApplicationFramework.Presentation.CommandEventArgs Class
namespace: Aveva.ApplicationFramework.Presentation
assembly: Aveva.ApplicationFramework.Presentation
kind: Class
source: Aveva.ApplicationFramework
---

# Aveva.ApplicationFramework.Presentation.CommandEventArgs Class

> Provides data for the CommandAdded and CommandRemoved events.

## Syntax

```csharp
public class CommandEventArgs : EventArgs
```

## Inheritance

`System.Object` → `System.EventArgs` → `Aveva.ApplicationFramework.Presentation.CommandEventArgs`

## Thread Safety

Public static ( Shared in Visual Basic) members of this type are
safe for multithreaded operations. Instance members are not guaranteed to be
thread-safe.

## Requirements

Namespace:
Aveva.ApplicationFramework.Presentation
Assembly: Aveva.ApplicationFramework.Presentation (in Aveva.ApplicationFramework.Presentation.dll)

## Constructors

#### `CommandEventArgs` Constructor

Initialize a new instance of a CommandEventArgs class

```csharp
public CommandEventArgs( Command command );
```

**Parameters**

- **command** — The Command object

## Properties

#### `Command` Property

Gets the Command object associated with the event

```csharp
public Command Command {get;}
```
