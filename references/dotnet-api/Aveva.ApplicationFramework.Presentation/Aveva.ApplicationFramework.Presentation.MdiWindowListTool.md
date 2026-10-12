---
title: Aveva.ApplicationFramework.Presentation.MdiWindowListTool Class
namespace: Aveva.ApplicationFramework.Presentation
assembly: Aveva.ApplicationFramework.Presentation
kind: Class
source: Aveva.ApplicationFramework
---

# Aveva.ApplicationFramework.Presentation.MdiWindowListTool Class

> Class to respresent the special tool which displays a list of current MDI Windows.

## Syntax

```csharp
public abstract class MdiWindowListTool : ITool
```

## Inheritance

`System.Object` → `Aveva.ApplicationFramework.Presentation.MdiWindowListTool`

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
