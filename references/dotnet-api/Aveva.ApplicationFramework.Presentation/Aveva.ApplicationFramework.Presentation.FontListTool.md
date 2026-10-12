---
title: Aveva.ApplicationFramework.Presentation.FontListTool Class
namespace: Aveva.ApplicationFramework.Presentation
assembly: Aveva.ApplicationFramework.Presentation
kind: Class
source: Aveva.ApplicationFramework
---

# Aveva.ApplicationFramework.Presentation.FontListTool Class

> Represents a FontListTool.

## Syntax

```csharp
public abstract class FontListTool : ITool
```

## Inheritance

`System.Object` → `Aveva.ApplicationFramework.Presentation.FontListTool`

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

#### `Command` Property

Gets the command object which was associated with the tool when it was created.

```csharp
public abstract Command Command {get;}
```

#### `Enabled` Property

Gets or sets the enabled state of the tool.

```csharp
public abstract bool Enabled {get; set;}
```

**Implements**

ITool.Enabled

#### `FontName` Property

Gets the FontName selected.

```csharp
public abstract string FontName {get; set;}
```

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

#### `Visible` Property

Gets or sets the visibility of the tool.

```csharp
public abstract bool Visible {get; set;}
```

**Implements**

ITool.Visible

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

Occurs when a font is selected.

```csharp
public event EventHandler ToolClick;
```

#### `ToolValueChanged` Event

Occurs when the value of the tool changes.

```csharp
public event EventHandler ToolValueChanged;
```
