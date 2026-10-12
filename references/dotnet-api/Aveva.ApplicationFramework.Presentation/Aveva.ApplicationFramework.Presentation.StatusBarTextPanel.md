---
title: Aveva.ApplicationFramework.Presentation.StatusBarTextPanel Class
namespace: Aveva.ApplicationFramework.Presentation
assembly: Aveva.ApplicationFramework.Presentation
kind: Class
source: Aveva.ApplicationFramework
---

# Aveva.ApplicationFramework.Presentation.StatusBarTextPanel Class

> Represents a StatusBarTextPanel.

## Syntax

```csharp
public abstract class StatusBarTextPanel : IStatusBarPanel
```

## Inheritance

`System.Object` → `Aveva.ApplicationFramework.Presentation.StatusBarTextPanel`

## Thread Safety

Public static ( Shared in Visual Basic) members of this type are
safe for multithreaded operations. Instance members are not guaranteed to be
thread-safe.

## Requirements

Namespace:
Aveva.ApplicationFramework.Presentation
Assembly: Aveva.ApplicationFramework.Presentation (in Aveva.ApplicationFramework.Presentation.dll)

## Properties

#### `AlertTextChange` Property

Controls if a change in the value of the text panel cause it to start flashing to alert the user. Flashing will stop when the cursor enters the panel.

```csharp
public abstract bool AlertTextChange {get; set;}
```

#### `Enabled` Property

Returns or sets if the panel is enabled.

```csharp
public abstract bool Enabled {get; set;}
```

**Implements**

IStatusBarPanel.Enabled

#### `HotTrack` Property

Determines whether the a panel's appearance changes when the mouse passes over it. This is only valid for panels which have a PanelClick event handler

```csharp
public abstract bool HotTrack {get; set;}
```

#### `Image` Property

Returns or sets the image associated with the panel.

```csharp
public abstract System.Drawing.Image Image {get; set;}
```

**Implements**

IStatusBarPanel.Image

#### `Key` Property

Key for the panel.

```csharp
public abstract string Key {get;}
```

**Implements**

IStatusBarPanel.Key

#### `SizingMode` Property

Returns or sets how the panel can be sized.

```csharp
public abstract PanelSizingMode SizingMode {get; set;}
```

**Implements**

IStatusBarPanel.SizingMode

#### `Text` Property

Returns or sets the text associated with the panel.

```csharp
public abstract string Text {get; set;}
```

**Implements**

IStatusBarPanel.Text

#### `Tooltip` Property

Returns or sets the tooltip for the panel.

```csharp
public abstract string Tooltip {get; set;}
```

**Implements**

IStatusBarPanel.Tooltip

#### `Visible` Property

Returns or sets if the panel is visible.

```csharp
public abstract bool Visible {get; set;}
```

**Implements**

IStatusBarPanel.Visible

#### `Width` Property

Returns or sets the width of the panel.

```csharp
public abstract int Width {get; set;}
```

**Implements**

IStatusBarPanel.Width

## Methods

#### `StopAlert` Method

Stop text panel flashing following a text change when AlertTextChange is turned on.

```csharp
public abstract void StopAlert();
```

## Events

#### `PanelClick` Event

Occurs when the panel is clicked

```csharp
public event EventHandler PanelClick;
```

**Implements**

IStatusBarPanel.PanelClick

#### `PanelDoubleClick` Event

Occurs when the panel is double clicked

```csharp
public event EventHandler PanelDoubleClick;
```

**Implements**

IStatusBarPanel.PanelDoubleClick
