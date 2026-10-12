---
title: Aveva.ApplicationFramework.Presentation.PopupColorPickerTool Class
namespace: Aveva.ApplicationFramework.Presentation
assembly: Aveva.ApplicationFramework.Presentation
kind: Class
source: Aveva.ApplicationFramework
---

# Aveva.ApplicationFramework.Presentation.PopupColorPickerTool Class

> Represents a PopupColorPicker.

## Syntax

```csharp
public abstract class PopupColorPickerTool : ITool
```

## Inheritance

`System.Object` → `Aveva.ApplicationFramework.Presentation.PopupColorPickerTool`

## Thread Safety

Public static ( Shared in Visual Basic) members of this type are
safe for multithreaded operations. Instance members are not guaranteed to be
thread-safe.

## Requirements

Namespace:
Aveva.ApplicationFramework.Presentation
Assembly: Aveva.ApplicationFramework.Presentation (in Aveva.ApplicationFramework.Presentation.dll)

## Properties

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

#### `ReplaceableColor` Property

Returns or sets the color in the PopupColorPickerTool's image that will be replaced with the SelectedColor value. Default is Magenta.

```csharp
public abstract System.Drawing.Color ReplaceableColor {get; set;}
```

#### `SelectedColor` Property

Returns/sets the selected color in the PopupColorPickerTool.

```csharp
public abstract System.Drawing.Color SelectedColor {get; set;}
```

#### `Shortcut` Property

Gets or sets the shortcut associated with a tool.

```csharp
public abstract System.Windows.Forms.Shortcut Shortcut {get; set;}
```

**Implements**

ITool.Shortcut

#### `ShowAutomaticColor` Property

Returns or sets whether a button representing the color Color.WindowText is displayed in the dropdown.

```csharp
public abstract bool ShowAutomaticColor {get; set;}
```

#### `ShowTransparentColor` Property

Returns or sets whether a button representing the color Color.Transparent is displayed in the dropdown.

```csharp
public abstract bool ShowTransparentColor {get; set;}
```

#### `Tag` Property

Gets or sets the tag property which can be used to logically attach another object or value to a tool.

```csharp
public abstract object Tag {get; set;}
```

**Implements**

ITool.Tag

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

## Events

#### `ToolClick` Event

Occurs when the PopupColorPickerTool is clicked.

```csharp
public event EventHandler ToolClick;
```

#### `ToolValueChanged` Event

Occurs when the value of the tool changes.

```csharp
public event EventHandler ToolValueChanged;
```
