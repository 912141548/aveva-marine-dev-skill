---
title: Aveva.ApplicationFramework.Presentation.DockedWindow Class
namespace: Aveva.ApplicationFramework.Presentation
assembly: Aveva.ApplicationFramework.Presentation
kind: Class
source: Aveva.ApplicationFramework
---

# Aveva.ApplicationFramework.Presentation.DockedWindow Class

> Class to represent a DockedWindow.

## Syntax

```csharp
public abstract class DockedWindow : IWindow
```

## Inheritance

`System.Object` → `Aveva.ApplicationFramework.Presentation.DockedWindow`

## Thread Safety

Public static ( Shared in Visual Basic) members of this type are
safe for multithreaded operations. Instance members are not guaranteed to be
thread-safe.

## Requirements

Namespace:
Aveva.ApplicationFramework.Presentation
Assembly: Aveva.ApplicationFramework.Presentation (in Aveva.ApplicationFramework.Presentation.dll)

## Properties

#### `Control` Property

Gets the control displayed in the window.

```csharp
public abstract System.Windows.Forms.Control Control {get;}
```

**Implements**

IWindow.Control

#### `DockedPosition` Property

Gets the current docked position of the window.

```csharp
public abstract DockedPosition DockedPosition {get;}
```

#### `DockGroupStyle` Property

Returns or sets how groups of docked windows should be organised.

```csharp
public abstract DockGroupStyle DockGroupStyle {get; set;}
```

#### `Enabled` Property

Gets or sets whether the window is enabled.

```csharp
public abstract bool Enabled {get; set;}
```

**Implements**

IWindow.Enabled

#### `Floatable` Property

Gets or sets whether the window is floatable.

```csharp
public abstract bool Floatable {get; set;}
```

**Implements**

IWindow.Floatable

#### `Height` Property

Gets or sets the height of the window.

```csharp
public abstract int Height {get; set;}
```

**Implements**

IWindow.Height

#### `HelpALink` Property

Gets or sets a help link associated with the window.

```csharp
public abstract string HelpALink {get; set;}
```

**Implements**

IWindow.HelpALink

#### `HelpContextId` Property

Gets or sets the help context id associated with the window.

```csharp
public abstract string HelpContextId {get; set;}
```

**Implements**

IWindow.HelpContextId

#### `IsFloating` Property

Gets the floating state of a window.

```csharp
public abstract bool IsFloating {get;}
```

**Implements**

IWindow.IsFloating

#### `Key` Property

Gets the Key of the window in the WindowsCollection.

```csharp
public abstract string Key {get;}
```

**Implements**

IWindow.Key

#### `MaximumSize` Property

Get or sets the maximum size of the window.

```csharp
public abstract System.Drawing.Size MaximumSize {get; set;}
```

**Implements**

IWindow.MaximumSize

#### `MinimumSize` Property

Get or sets the minimum size of the window.

```csharp
public abstract System.Drawing.Size MinimumSize {get; set;}
```

**Implements**

IWindow.MinimumSize

#### `SaveLayout` Property

Gets or sets the property which controls if the window should be included in the docked window layout serialization

```csharp
public abstract bool SaveLayout {get; set;}
```

#### `Tag` Property

Gets or sets the tag property which can be used to logically attach another object or value to a window.

```csharp
public abstract object Tag {get; set;}
```

**Implements**

IWindow.Tag

#### `Title` Property

Gets or sets the title of the window.

```csharp
public abstract string Title {get; set;}
```

**Implements**

IWindow.Title

#### `Visible` Property

Gets or sets the visible state of the window.

```csharp
public abstract bool Visible {get; set;}
```

**Implements**

IWindow.Visible

#### `Width` Property

Gets or sets the width of the window.

```csharp
public abstract int Width {get; set;}
```

**Implements**

IWindow.Width

## Methods

#### `Close` Method

Destroys the window.

```csharp
public abstract void Close();
```

**Implements**

IWindow.Close

#### `Dock` Method

Docks the window within the main window.

```csharp
public abstract void Dock();
```

**Implements**

IWindow.Dock

#### `Float` Method

Displays the window as a floating window.

```csharp
public abstract void Float();
```

**Implements**

IWindow.Float

#### `GroupWith` Method

Arrange docked windows together as a group.

```csharp
public abstract void GroupWith( DockedWindow dockedWindow );
```

**Parameters**

- **dockedWindow** —

#### `Hide` Method

Conceals the window from the user.

```csharp
public abstract void Hide();
```

**Implements**

IWindow.Hide

#### `Show` Method

Displays the window to the user.

```csharp
public abstract void Show();
```

**Implements**

IWindow.Show

## Events

#### `Activated` Event

Event which occurs when the window is activated.

```csharp
public event EventHandler Activated;
```

#### `Closed` Event

Event which occurs when window is closed.

```csharp
public event EventHandler Closed;
```

#### `Closing` Event

Event which occurs when window is closing.

```csharp
public event CancelEventHandler Closing;
```

#### `Deactivated` Event

Event which occurs when the window is deactivated.

```csharp
public event EventHandler Deactivated;
```

#### `Reparented` Event

Event which occurs when the window is reparented.

```csharp
public event EventHandler Reparented;
```
