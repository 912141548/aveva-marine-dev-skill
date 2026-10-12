---
title: Aveva.ApplicationFramework.Presentation.WindowManager Class
namespace: Aveva.ApplicationFramework.Presentation
assembly: Aveva.ApplicationFramework.Presentation
kind: Class
source: Aveva.ApplicationFramework
---

# Aveva.ApplicationFramework.Presentation.WindowManager Class

> Provides access to window related facilities.

## Syntax

```csharp
public abstract class WindowManager
```

## Inheritance

`System.Object` → `Aveva.ApplicationFramework.Presentation.WindowManager`

## Thread Safety

Public static ( Shared in Visual Basic) members of this type are
safe for multithreaded operations. Instance members are not guaranteed to be
thread-safe.

## Requirements

Namespace:
Aveva.ApplicationFramework.Presentation
Assembly: Aveva.ApplicationFramework.Presentation (in Aveva.ApplicationFramework.Presentation.dll)

## Properties

#### `Enabled` Property

Get or set a property which controls the enabled state of all docked windows

```csharp
public abstract bool Enabled {get; set;}
```

#### `Instance` Property

Get instance of window manager

```csharp
public static WindowManager Instance {get; set;}
```

#### `MainForm` Property

Gets the main application Form

```csharp
public abstract System.Windows.Forms.Form MainForm {get;}
```

#### `SplashScreen` Property

Gets the splashscreen object.

```csharp
public abstract SplashScreen SplashScreen {get;}
```

#### `StatusBar` Property

Gets the StatusBar object.

```csharp
public abstract StatusBar StatusBar {get;}
```

#### `TabbedMdi` Property

Gets or sets whether MDI windows are displayed as tabbed windows.

```csharp
public abstract bool TabbedMdi {get; set;}
```

#### `Windows` Property

Gets the WindowCollection object.

```csharp
public abstract WindowsCollection Windows {get;}
```

## Methods

#### `CreateDockedWindow` Method

Creates and adds to the WindowsCollection a new DockedWindow.

```csharp
public abstract DockedWindow CreateDockedWindow( string key , string title , Control control , DockedPosition position );
```

**Parameters**

- **key** — Window key in the WindowsCollection.
- **title** — Window title.
- **control** — Control to display in the docked window.
- **position** — Window DockPosition.

**Return Value**

New DockedWindow created.

#### `CreateMdiWindow` Method

Creates and adds to the WindowsCollection a new MdiWindow

```csharp
public abstract MdiWindow CreateMdiWindow( string key , string title , Control control );
```

**Parameters**

- **key** — Window key in the WindowsCollection.
- **title** — Window title.
- **control** — Control to display in the docked window.

**Return Value**

New MdiWindow created

#### `LoadWindowLayout` Method

Loads the docked window layout.

```csharp
public abstract void LoadWindowLayout();
```

#### `SaveWindowLayout` Method

Saves the docked window layout.

```csharp
public abstract void SaveWindowLayout();
```

## Events

#### `WindowAdded` Event

Event Raised when a new window is added.

```csharp
public event WindowEventHandler WindowAdded;
```

**Event Data**

The event handler receives an argument of type WindowEventArgs containing data related to this event. The following WindowEventArgs property provides information specific to this event.
Property
Description

Window

Gets the Window object associated with the event

#### `WindowLayoutLoaded` Event

Event Raised when window layout is loaded

```csharp
public event EventHandler WindowLayoutLoaded;
```
