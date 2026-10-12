---
title: Aveva.ApplicationFramework.Presentation.IStatusBarPanel Interface
namespace: Aveva.ApplicationFramework.Presentation
assembly: Aveva.ApplicationFramework.Presentation
kind: Interface
source: Aveva.ApplicationFramework
---

# Aveva.ApplicationFramework.Presentation.IStatusBarPanel Interface

> Interface supported by Statusbar panels.

## Syntax

```csharp
public interface IStatusBarPanel
```

## Types that implement IStatusBarPanel

Type
Description

StatusBarTextPanel

Represents a StatusBarTextPanel.

## Requirements

Namespace:
Aveva.ApplicationFramework.Presentation
Assembly: Aveva.ApplicationFramework.Presentation (in Aveva.ApplicationFramework.Presentation.dll)

## Properties

#### `Enabled` Property

Returns or sets if the panel is enabled.

```csharp
bool Enabled {get; set;}
```

#### `Image` Property

Returns or sets the image associated with the panel.

```csharp
System.Drawing.Image Image {get; set;}
```

#### `Key` Property

Key for the panel.

```csharp
string Key {get;}
```

#### `SizingMode` Property

Returns or sets how the panel can be sized. Fixed - The panel's size is controlled by the width. Automatic - The panel's size is based on its contents. Adjustable - The panel's base size is controlled by the width but the panel may be resized. Spring - The panel size is based on the remaining size remaining after the other visible panes have been sized.

```csharp
PanelSizingMode SizingMode {get; set;}
```

#### `Text` Property

Returns or sets the text associated with the panel.

```csharp
string Text {get; set;}
```

#### `Tooltip` Property

Returns or sets the tooltip for the panel.

```csharp
string Tooltip {get; set;}
```

#### `Visible` Property

Returns or sets if the panel is visible.

```csharp
bool Visible {get; set;}
```

#### `Width` Property

Returns or sets the width of the panel.

```csharp
int Width {get; set;}
```

## Events

#### `PanelClick` Event

Occurs when the panel is clicked

```csharp
event EventHandler PanelClick;
```

#### `PanelDoubleClick` Event

Occurs when the panel is double clicked

```csharp
event EventHandler PanelDoubleClick;
```
