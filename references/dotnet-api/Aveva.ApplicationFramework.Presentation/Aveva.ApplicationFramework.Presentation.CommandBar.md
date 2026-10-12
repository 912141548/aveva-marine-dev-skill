---
title: Aveva.ApplicationFramework.Presentation.CommandBar Class
namespace: Aveva.ApplicationFramework.Presentation
assembly: Aveva.ApplicationFramework.Presentation
kind: Class
source: Aveva.ApplicationFramework
---

# Aveva.ApplicationFramework.Presentation.CommandBar Class

> Class to represent a CommandBar.

## Syntax

```csharp
public abstract class CommandBar
```

## Inheritance

`System.Object` → `Aveva.ApplicationFramework.Presentation.TaskBar` → `Aveva.ApplicationFramework.Presentation.CommandBar`

## Thread Safety

Public static ( Shared in Visual Basic) members of this type are
safe for multithreaded operations. Instance members are not guaranteed to be
thread-safe.

## Requirements

Namespace:
Aveva.ApplicationFramework.Presentation
Assembly: Aveva.ApplicationFramework.Presentation (in Aveva.ApplicationFramework.Presentation.dll)

## Properties

#### `AllowCustomize` Property

Gets or sets whether the CommandBar can be customized at run-time by the end user.

```csharp
public abstract bool AllowCustomize {get; set;}
```

#### `AllowFloating` Property

Gets or sets whether the CommandBar can be dragged out of a dock area and floated.

```csharp
public abstract bool AllowFloating {get; set;}
```

#### `AllowHiding` Property

Gets or sets whether the CommandBar can be hidden at run-time by the end user.

```csharp
public abstract bool AllowHiding {get; set;}
```

#### `Caption` Property

Gets or sets the description displayed in the customization dialogs and in the caption of the floating CommandBar.

```csharp
public abstract string Caption {get; set;}
```

#### `Command` Property

Gets the command object which was associated with the CommandBar when it was created.

```csharp
public abstract Command Command {get;}
```

#### `DockedColumn` Property

Gets or sets the column (within the dock area) in which the CommandBar is docked.

```csharp
public abstract int DockedColumn {get; set;}
```

#### `DockedPosition` Property

Gets or sets the current location of the CommandBar (left, right, top, bottom, floating)

```csharp
public abstract DockedPosition DockedPosition {get; set;}
```

#### `DockedRow` Property

Gets or sets the row (within the dock area) in which the CommandBar is docked.

```csharp
public abstract int DockedRow {get; set;}
```

#### `Enabled` Property

Gets or sets the enabled state of the CommandBar.

```csharp
public abstract bool Enabled {get; set;}
```

#### `FillEntireRow` Property

Gets or sets whether the CommandBar will take up the entire dock area row, even if it doesn't have enough tools to fill the area.

```csharp
public abstract bool FillEntireRow {get; set;}
```

#### `Key` Property

The Key of the CommandBar in the CommandBarCollection

```csharp
public abstract string Key {get;}
```

#### `ShowInToolbarList` Property

Gets or sets whether the CommandBar shows up in the customization dialog at runtime.

```csharp
public abstract bool ShowInToolbarList {get; set;}
```

#### `Tag` Property

Gets or sets the tag property which can be used to logically attach another object or value to a tool.

```csharp
public abstract object Tag {get; set;}
```

#### `Tools` Property

Gets the ToolsCollection containing the tools to display in the CommandBar.

```csharp
public abstract ToolsCollection Tools {get;}
```

#### `Visible` Property

Gets or sets whether the CommandBar is visible.

```csharp
public abstract bool Visible {get; set;}
```

## Events

#### `Closed` Event

Event raised when the CommandBar is Closed

```csharp
public event EventHandler Closed;
```

#### `Opened` Event

Event raised when the CommandBar is Opened

```csharp
public event EventHandler Opened;
```
