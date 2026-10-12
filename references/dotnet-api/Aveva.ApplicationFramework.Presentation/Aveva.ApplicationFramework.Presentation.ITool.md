---
title: Aveva.ApplicationFramework.Presentation.ITool Interface
namespace: Aveva.ApplicationFramework.Presentation
assembly: Aveva.ApplicationFramework.Presentation
kind: Interface
source: Aveva.ApplicationFramework
---

# Aveva.ApplicationFramework.Presentation.ITool Interface

> Interface supported by all Tool clases.

## Syntax

```csharp
public interface ITool
```

## Types that implement ITool

Type
Description

ButtonTool

Represents a ButtonToolt.

ComboBoxTool

Represents a ComboBoxTool.

ContainerTool

A tool that contains a Control.

FontListTool

Represents a FontListTool.

LabelTool

Class to represent a static Label.

ListTool

Represents a ListTool.

MdiWindowListTool

Class to respresent the special tool which displays a list of current MDI Windows.

MenuTool

Represents a MenuTool.

PopupColorPickerTool

Represents a PopupColorPicker.

PopupContainerTool

Represents a PopuplContainerTool.

StateButtonTool

Represents a StateButtonTool.

TaskPaneTool

Class used to represent a single item in a TaskPane.

TextBoxTool

Represents a TextBoxTool.

## Requirements

Namespace:
Aveva.ApplicationFramework.Presentation
Assembly: Aveva.ApplicationFramework.Presentation (in Aveva.ApplicationFramework.Presentation.dll)

## Properties

#### `Caption` Property

Gets or sets the tool caption

```csharp
string Caption {get; set;}
```

#### `Category` Property

Gets or sets the tools category

```csharp
string Category {get; set;}
```

#### `Enabled` Property

Gets or sets the enabled state of the tool.

```csharp
bool Enabled {get; set;}
```

#### `Image` Property

Gets or sets the image displayed on the tool

```csharp
System.Drawing.Image Image {get; set;}
```

#### `IsFirstInGroup` Property

Gets or sets a flag which indicated whether an instance tool is the first in a tool group. A separator will be displayed before a tool if this property is set to true.

```csharp
bool IsFirstInGroup {get; set;}
```

#### `Key` Property

The Key of the tool in the RootToolsCollection

```csharp
string Key {get;}
```

#### `Shortcut` Property

Gets or sets the shortcut associated with a tool.

```csharp
System.Windows.Forms.Shortcut Shortcut {get; set;}
```

#### `Tag` Property

Gets or sets the tag property which can be used to logically attach another object or value to a tool.

```csharp
object Tag {get; set;}
```

#### `Tooltip` Property

Gets or sets the tools tooltip

```csharp
string Tooltip {get; set;}
```

#### `Value` Property

Gets or sets the value of the tool.

```csharp
object Value {get; set;}
```

#### `Visible` Property

Gets or sets the visibility of the tool.

```csharp
bool Visible {get; set;}
```
