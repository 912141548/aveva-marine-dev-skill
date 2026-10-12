---
title: Aveva.ApplicationFramework.Presentation.CommandExecutor Class
namespace: Aveva.ApplicationFramework.Presentation
assembly: Aveva.ApplicationFramework.Presentation
kind: Class
source: Aveva.ApplicationFramework
---

# Aveva.ApplicationFramework.Presentation.CommandExecutor Class

> Abstract base class which an application must inherit from to create a CommandExecutor object.

## Syntax

```csharp
public abstract class CommandExecutor
```

## Inheritance

`System.Object` → `Aveva.ApplicationFramework.Presentation.CommandExecutor`

## Thread Safety

Public static ( Shared in Visual Basic) members of this type are
safe for multithreaded operations. Instance members are not guaranteed to be
thread-safe.

## Requirements

Namespace:
Aveva.ApplicationFramework.Presentation
Assembly: Aveva.ApplicationFramework.Presentation (in Aveva.ApplicationFramework.Presentation.dll)

## Properties

#### `Checked` Property

Gets or sets the Checked state of the CommandExecutor.

```csharp
public abstract bool Checked {get; set;}
```

#### `Enabled` Property

Gets or sets the Enabled state of the CommandExecutor.

```csharp
public abstract bool Enabled {get; set;}
```

#### `Value` Property

Gets or sets the value of the CommandExecutor.

```csharp
public abstract object Value {set;}
```

#### `Visible` Property

Gets or sets the Visible state of the CommandExecutor.

```csharp
public abstract bool Visible {get; set;}
```

## Methods

#### `SetProperty` Method

Sets the given property to the given value.

```csharp
public abstract void SetProperty( string property , object value );
```

**Parameters**

- **property** — 
- **value** —
