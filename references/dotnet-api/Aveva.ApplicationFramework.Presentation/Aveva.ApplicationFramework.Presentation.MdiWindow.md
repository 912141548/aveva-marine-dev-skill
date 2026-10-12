---
title: Aveva.ApplicationFramework.Presentation.MdiWindow Class
namespace: Aveva.ApplicationFramework.Presentation
assembly: Aveva.ApplicationFramework.Presentation
kind: Class
source: Aveva.ApplicationFramework
---

# Aveva.ApplicationFramework.Presentation.MdiWindow Class

> Represents an MDI style window or dialog box.

## Syntax

```csharp
public abstract class MdiWindow : IWindow
```

## Inheritance

`System.Object` → `Aveva.ApplicationFramework.Presentation.MdiWindow`

## Thread Safety

Public static ( Shared in Visual Basic) members of this type are
safe for multithreaded operations. Instance members are not guaranteed to be
thread-safe.

## Requirements

Namespace:
Aveva.ApplicationFramework.Presentation
Assembly: Aveva.ApplicationFramework.Presentation (in Aveva.ApplicationFramework.Presentation.dll)

## Properties

#### `CommandBarManager` Property

Gets the CommandBarManager for this Mdi window.

```csharp
public abstract CommandBarManager CommandBarManager {get;}
```

#### `Control` Property

Gets the control displayed in the window.

```csharp
public abstract System.Windows.Forms.Control Control {get;}
```

**Implements**

IWindow.Control

#### `DestroyOnClose` Property

Controls the default behaviour of destorying the window on close. If this is set to false then the default behaviour will be to hide the window.

```csharp
public abstract bool DestroyOnClose {get; set;}
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

#### `Form` Property

Returns the underlying Form for the MdiWindow

```csharp
public abstract System.Windows.Forms.Form Form {get;}
```

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

#### `Maximized` Property

Gets or sets the maximized state of the window.

```csharp
public abstract bool Maximized {get; set;}
```

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

#### `Resizeable` Property

Gets or sets whether the window is resizeable.

```csharp
public abstract bool Resizeable {get; set;}
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

Occurs when the window is activated.

```csharp
public event EventHandler Activated;
```

#### `Closed` Event

Event which occurs when window is closed.

```csharp
public event EventHandler Closed;
```

#### `Closing` Event

Occurs when this window is closing.

```csharp
public event CancelEventHandler Closing;
```

#### `Deactivated` Event

Occurs then the window is deactivated.

```csharp
public event EventHandler Deactivated;
```

#### `Reparented` Event

Occurs when the window is reparented.

```csharp
public event EventHandler Reparented;
```

#### `Resized` Event

Occurs when the window is resized.

```csharp
public event EventHandler Resized;
```
