---
title: Aveva.ApplicationFramework.Presentation.ComboBoxTool Class
namespace: Aveva.ApplicationFramework.Presentation
assembly: Aveva.ApplicationFramework.Presentation
kind: Class
source: Aveva.ApplicationFramework
---

# Aveva.ApplicationFramework.Presentation.ComboBoxTool Class

> Represents a ComboBoxTool.

## Syntax

```csharp
public abstract class ComboBoxTool : ITool
```

## Inheritance

`System.Object` → `Aveva.ApplicationFramework.Presentation.ComboBoxTool`

## Thread Safety

Public static ( Shared in Visual Basic) members of this type are
safe for multithreaded operations. Instance members are not guaranteed to be
thread-safe.

## Requirements

Namespace:
Aveva.ApplicationFramework.Presentation
Assembly: Aveva.ApplicationFramework.Presentation (in Aveva.ApplicationFramework.Presentation.dll)

## Properties

#### `AutoComplete` Property

Gets or sets whether the edit portion is automatically updated to match an item in the list as new characters are typed.

```csharp
public abstract bool AutoComplete {get; set;}
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

#### `Command` Property

Gets the command object which was associated with the tool when it was created.

```csharp
public abstract Command Command {get;}
```

#### `DisplayText` Property

Gets or sets the text displayed in the tool.

```csharp
public abstract string DisplayText {get; set;}
```

#### `Editable` Property

Gets or sets whether the text portion of the ComboBoxTool is editable.

```csharp
public abstract bool Editable {get; set;}
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

#### `MaxLength` Property

Gets or sets the maximum allowable length of the text that can be entered in the ComboBoxTool.

```csharp
public abstract int MaxLength {get; set;}
```

#### `PasswordChar` Property

Gets or sets a value indicating how the characters typed by a user are displayed.

```csharp
public abstract string PasswordChar {get; set;}
```

#### `SelectedIndex` Property

Gets or sets the zero-based index of the selected item in the ValueList.

```csharp
public abstract int SelectedIndex {get; set;}
```

#### `SelectedValue` Property

Returns the object behind the selected ValueList item.

```csharp
public abstract object SelectedValue {get;}
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

#### `ValueList` Property

Gets the ValueList object associated with the ComboBoxTool.

```csharp
public abstract ValueList ValueList {get;}
```

#### `Visible` Property

Gets or sets the visibility of the tool.

```csharp
public abstract bool Visible {get; set;}
```

**Implements**

ITool.Visible

#### `Width` Property

Gets or sets the width of the tool.

```csharp
public abstract int Width {get; set;}
```

## Events

#### `AfterCloseup` Event

Occurs after the popup part of the tool is closed.

```csharp
public event EventHandler AfterCloseup;
```

#### `BeforePopup` Event

Occurs before the popup part of the tool is displayed.

```csharp
public event EventHandler BeforePopup;
```

#### `ToolClick` Event

Occurs when Enter key is pressed while display field has focus.

```csharp
public event EventHandler ToolClick;
```

#### `ToolValueChanged` Event

Occurs when the value of the tool changes.

```csharp
public event EventHandler ToolValueChanged;
```
