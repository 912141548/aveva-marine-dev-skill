---
title: Aveva.ApplicationFramework.Presentation.Command Class
namespace: Aveva.ApplicationFramework.Presentation
assembly: Aveva.ApplicationFramework.Presentation
kind: Class
source: Aveva.ApplicationFramework
---

# Aveva.ApplicationFramework.Presentation.Command Class

> Abstract base class which an application must inherit from to create a Command object

## Syntax

```csharp
public abstract class Command
```

## Inheritance

`System.Object` → `Aveva.ApplicationFramework.Presentation.Command`

## Thread Safety

Public static ( Shared in Visual Basic) members of this type are
safe for multithreaded operations. Instance members are not guaranteed to be
thread-safe.

## Requirements

Namespace:
Aveva.ApplicationFramework.Presentation
Assembly: Aveva.ApplicationFramework.Presentation (in Aveva.ApplicationFramework.Presentation.dll)

## Constructors

#### `Command` Constructor

Command constructor

```csharp
public Command();
```

## Properties

#### `Checked` Property

Gets or sets if the command is in a checked state. Setting this value will set the CommandExecutor.Checked property on all attached CommandExecutors.

```csharp
public virtual bool Checked {get; set;}
```

#### `Description` Property

Description for the command

```csharp
public string Description {get; set;}
```

#### `Enabled` Property

Gets or sets if the command is enabled. Setting this value will set the CommandExecutor.Enabled property on all attached CommandExecutors.

```csharp
public virtual bool Enabled {get; set;}
```

#### `ExecuteOnCheckedChange` Property

```csharp
public bool ExecuteOnCheckedChange {get; set;}
```

#### `Internal` Property

Flag to control the visibility of the command in Customization dialog

```csharp
public bool Internal {get; set;}
```

#### `IsValid` Property

Gets the IsValid status of the command. A Command may become invalid in some application context. Method can be overriden in a derived class.

```csharp
public virtual bool IsValid {get;}
```

#### `Key` Property

The commands key in the CommandCollection

```csharp
public string Key {get; set;}
```

#### `List` Property

ArrayList which can contain data to be presented in the GUI

```csharp
public virtual System.Collections.ArrayList List {get;}
```

#### `SelectedIndex` Property

Used to comunicate to the command which item in the list was selected

```csharp
public virtual int SelectedIndex {get; set;}
```

#### `Value` Property

Setting this value will set the CommandExecutor.Value property on all attached CommandExecutors.

```csharp
public virtual object Value {get; set;}
```

#### `ValueChanged` Property

True if the value of the command has been changed

```csharp
public virtual bool ValueChanged {get; set;}
```

#### `Visible` Property

Gets or sets if the command is visible. Setting this value will set the CommandExecutor.Visible property on all attached CommandExecutors.

```csharp
public virtual bool Visible {get; set;}
```

## Methods

#### `AttachExecutor` Method

Attaches a CommandExecutor derived class to the command

```csharp
public void AttachExecutor( CommandExecutor executor );
```

**Parameters**

- **executor** — The CommandExecutor derived class to attach.

#### `CancelableExecute` Method

Version of Execute which can be cancelled by an BeforeCommandExecute event handler

```csharp
public void CancelableExecute();
```

#### `DetachAllExecutors` Method

Detach all CommandExecutor derived classes from the command

```csharp
public void DetachAllExecutors();
```

#### `DetachExecutor` Method

Detach a CommandExecutor derived class from the command

```csharp
public void DetachExecutor( CommandExecutor executor );
```

**Parameters**

- **executor** — The CommandExecutor derived class to detach.

#### `Execute` Method

The command Execute method is normally overridden by a derived class

```csharp
public virtual void Execute();
```

#### `GetState` Method

Gets the current state of the command

```csharp
public virtual CommandState GetState( string context );
```

**Parameters**

- **context** —

#### `Refresh` Method ()

Call to allow the command to update its visilility or enabled state following a change to the application context.

```csharp
public virtual void Refresh();
```

#### `Refresh` Method (String)

Call to allow the command to update its visilility or enabled state following a change to the application context.

```csharp
public virtual void Refresh( string Context );
```

**Parameters**

- **Context** — A string representing the new application context

#### `SetProperty` Method

```csharp
public virtual void SetProperty( string property , object value );
```

**Parameters**

- **property** — 
- **value** —

## Events

#### `BeforeCommandExecute` Event

Occurs before the command is executed

```csharp
public event CancelEventHandler BeforeCommandExecute;
```

#### `CommandExecuted` Event

Occurs when the command is executed

```csharp
public event EventHandler CommandExecuted;
```
