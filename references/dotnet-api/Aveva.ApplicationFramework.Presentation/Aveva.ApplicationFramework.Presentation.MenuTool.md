---
title: Aveva.ApplicationFramework.Presentation.MenuTool Class
namespace: Aveva.ApplicationFramework.Presentation
assembly: Aveva.ApplicationFramework.Presentation
kind: Class
source: Aveva.ApplicationFramework
---

# Aveva.ApplicationFramework.Presentation.MenuTool Class

> Represents a MenuTool.

## Syntax

```csharp
public abstract class MenuTool : ITool
```

## Inheritance

`System.Object` → `Aveva.ApplicationFramework.Presentation.MenuTool`

## Thread Safety

Public static ( Shared in Visual Basic) members of this type are
safe for multithreaded operations. Instance members are not guaranteed to be
thread-safe.

## Requirements

Namespace:
Aveva.ApplicationFramework.Presentation
Assembly: Aveva.ApplicationFramework.Presentation (in Aveva.ApplicationFramework.Presentation.dll)

## Properties

#### `AllowTearaway` Property

Gets or sets whether the menu can be torn off

```csharp
public abstract bool AllowTearaway {get; set;}
```

#### `AutoUpdate` Property

Gets or sets whether the Image, Tooltip and Command are automaticaly updated.

```csharp
public abstract bool AutoUpdate {get; set;}
```

#### `Caption` Property

Gets or sets the tool caption

```csharp
public abstract string Caption {get; set;}
```

**Implements**

ITool.Caption

#### `Category` Property

Gets or sets the tools category

```csharp
public abstract string Category {get; set;}
```

**Implements**

ITool.Category

#### `Checked` Property

Gets or sets whether the tool is in the checked state.

```csharp
public abstract bool Checked {get; set;}
```

#### `Command` Property

Gets the command object which was associated with the tool when it was created.

```csharp
public abstract Command Command {get;}
```

#### `DropDownArrowStyle` Property

Returns or sets the style of the dropdown arrow for the popup menu.

```csharp
public abstract DropDownArrowStyle DropDownArrowStyle {get; set;}
```

#### `Enabled` Property

Gets or sets the enabled state of the tool.

```csharp
public abstract bool Enabled {get; set;}
```

**Implements**

ITool.Enabled

#### `Image` Property

Gets or sets the image displayed on the tool

```csharp
public abstract System.Drawing.Image Image {get; set;}
```

**Implements**

ITool.Image

#### `IsContextMenu` Property

Gets or sets whether the menu is a context menu

```csharp
public abstract bool IsContextMenu {get; set;}
```

#### `IsFirstInGroup` Property

Gets or sets a flag which indicated whether an instance tool is the first in a tool group. A separator will be displayed before a tool if this property is set to true.

```csharp
public abstract bool IsFirstInGroup {get; set;}
```

**Implements**

ITool.IsFirstInGroup

#### `Key` Property

The Key of the tool in the RootToolsCollection

```csharp
public abstract string Key {get;}
```

**Implements**

ITool.Key

#### `OptionSetKey` Property

Gets or sets the OptionSet key for the tool. Setting the key assigns the tool to the CommandBarManagers OptionSet which has this key.

```csharp
public abstract string OptionSetKey {get; set;}
```

#### `PopupStyle` Property

Gets or sets the popup style of the menu (Menu or CommandBar)

```csharp
public abstract PopupStyle PopupStyle {get; set;}
```

#### `Shortcut` Property

Gets or sets the shortcut associated with a tool.

```csharp
public abstract System.Windows.Forms.Shortcut Shortcut {get; set;}
```

**Implements**

ITool.Shortcut

#### `Tag` Property

Gets or sets the tag property which can be used to logically attach another object or value to a tool.

```csharp
public abstract object Tag {get; set;}
```

**Implements**

ITool.Tag

#### `Tools` Property

Gets the ToolsCollection containing the tools to display in the popup menu.

```csharp
public abstract ToolsCollection Tools {get;}
```

#### `Tooltip` Property

Gets or sets the tools tooltip

```csharp
public abstract string Tooltip {get; set;}
```

**Implements**

ITool.Tooltip

#### `Value` Property

Gets or sets the value of the tool.

```csharp
public abstract object Value {get; set;}
```

**Implements**

ITool.Value

#### `Visible` Property

Gets or sets the visibility of the tool.

```csharp
public abstract bool Visible {get; set;}
```

**Implements**

ITool.Visible

## Methods

#### `ShowPopup` Method ()

Displays the MenuTool as a context popup at the current mouse position.

```csharp
public abstract void ShowPopup();
```

#### `ShowPopup` Method (String)

Displays the MenuTool as a context popup with given context at the current mouse position.

```csharp
public abstract void ShowPopup( string context );
```

**Parameters**

- **context** —

## Events

#### `AfterCloseup` Event

Occurs after the menu is displayed

```csharp
public event EventHandler AfterCloseup;
```

#### `BeforePopup` Event

Occurs before the menu is displayed

```csharp
public event EventHandler BeforePopup;
```

#### `ToolClick` Event

Occurs when the tool is clicked

```csharp
public event EventHandler ToolClick;
```
