---
title: Aveva.ApplicationFramework.Presentation.CommandManager Class
namespace: Aveva.ApplicationFramework.Presentation
assembly: Aveva.ApplicationFramework.Presentation
kind: Class
source: Aveva.ApplicationFramework
---

# Aveva.ApplicationFramework.Presentation.CommandManager Class

> Class representing a CommandManager.

## Syntax

```csharp
public abstract class CommandManager
```

## Inheritance

`System.Object` → `Aveva.ApplicationFramework.Presentation.CommandManager`

## Thread Safety

Public static ( Shared in Visual Basic) members of this type are
safe for multithreaded operations. Instance members are not guaranteed to be
thread-safe.

## Requirements

Namespace:
Aveva.ApplicationFramework.Presentation
Assembly: Aveva.ApplicationFramework.Presentation (in Aveva.ApplicationFramework.Presentation.dll)

## Properties

#### `ApplicationContext` Property

Property which holds the current application context, which is used to manage the state of all commands.

```csharp
public abstract string ApplicationContext {get; set;}
```

#### `Commands` Property

Gets the collection of Command objects currently managed by the CommandManager.

```csharp
public abstract CommandsCollection Commands {get;}
```

#### `CommandTypes` Property

Property which returns a Hashtable of Command Types

```csharp
public abstract CommandTypesCollection CommandTypes {get;}
```

#### `Instance` Property

Get instance of command manager

```csharp
public static CommandManager Instance {get; set;}
```

#### `MacroCommand` Property

Property which holds the type of a class which implements a command to execute a macro in the context of the host application. (Eg. A PML command in PDMS)

```csharp
public abstract System.Type MacroCommand {get; set;}
```

## Methods

#### `AddAllCommands` Method

Add to the CommandCollection an instance of each class in the calling assembly which has a base class of type Aveva.ApplicationFramework.Presentation.Command

```csharp
public abstract void AddAllCommands();
```
