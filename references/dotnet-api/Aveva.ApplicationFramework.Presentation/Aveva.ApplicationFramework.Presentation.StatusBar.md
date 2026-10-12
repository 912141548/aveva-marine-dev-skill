---
title: Aveva.ApplicationFramework.Presentation.StatusBar Class
namespace: Aveva.ApplicationFramework.Presentation
assembly: Aveva.ApplicationFramework.Presentation
kind: Class
source: Aveva.ApplicationFramework
---

# Aveva.ApplicationFramework.Presentation.StatusBar Class

> Represents a Windows style status bar control.

## Syntax

```csharp
public abstract class StatusBar
```

## Inheritance

`System.Object` → `Aveva.ApplicationFramework.Presentation.StatusBar`

## Thread Safety

Public static ( Shared in Visual Basic) members of this type are
safe for multithreaded operations. Instance members are not guaranteed to be
thread-safe.

## Requirements

Namespace:
Aveva.ApplicationFramework.Presentation
Assembly: Aveva.ApplicationFramework.Presentation (in Aveva.ApplicationFramework.Presentation.dll)

## Properties

#### `Panels` Property

Gets the collection of application defined statusbar panels.

```csharp
public abstract StatusBarPanelsCollection Panels {get;}
```

#### `Progress` Property

Gets or sets the progress bar value [0-100].

```csharp
public abstract int Progress {get; set;}
```

#### `ProgressText` Property

Gets or Sets the text that is displayed with the progress bar.

```csharp
public abstract string ProgressText {get; set;}
```

#### `ShowCapsLock` Property

Gets or sets whether the panel showing the CapsLock state is displayed on the statusbar.

```csharp
public abstract bool ShowCapsLock {get; set;}
```

#### `ShowDateTime` Property

Gets or sets whether the Date and Time should be displayed on the statusbar.

```csharp
public abstract bool ShowDateTime {get; set;}
```

#### `ShowInsertMode` Property

Gets or sets whether the panel showing the IntertMode is displayed on the statusbar.

```csharp
public abstract bool ShowInsertMode {get; set;}
```

#### `ShowNumLock` Property

Gets or sets whether the panel showing the NumLock state is displayed on the statusbar.

```csharp
public abstract bool ShowNumLock {get; set;}
```

#### `ShowScrollLock` Property

Gets or sets whether the panel showing the ScrollLock state is displayed on the statusbar.

```csharp
public abstract bool ShowScrollLock {get; set;}
```

#### `Text` Property

Gets or sets the text to display in the statusbar text pane.

```csharp
public abstract string Text {get; set;}
```

#### `Visible` Property

Gets or sets the visibility of the statusbar.

```csharp
public abstract bool Visible {get; set;}
```
