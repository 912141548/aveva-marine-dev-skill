---
title: Aveva.ApplicationFramework.Presentation.IWindow Interface
namespace: Aveva.ApplicationFramework.Presentation
assembly: Aveva.ApplicationFramework.Presentation
kind: Interface
source: Aveva.ApplicationFramework
---

# Aveva.ApplicationFramework.Presentation.IWindow Interface

> Interface supported by supported window types(MDI, Docked).

## Syntax

```csharp
public interface IWindow
```

## Types that implement IWindow

Type
Description

DockedWindow

Class to represent a DockedWindow.

MdiWindow

Represents an MDI style window or dialog box.

## Requirements

Namespace:
Aveva.ApplicationFramework.Presentation
Assembly: Aveva.ApplicationFramework.Presentation (in Aveva.ApplicationFramework.Presentation.dll)

## Properties

#### `Control` Property

Gets the control displayed in the window.

```csharp
System.Windows.Forms.Control Control {get;}
```

#### `Enabled` Property

Gets or sets whether the window is enabled.

```csharp
bool Enabled {get; set;}
```

#### `Floatable` Property

Gets or sets whether the window is floatable.

```csharp
bool Floatable {get; set;}
```

#### `Height` Property

Gets or sets the height of the window.

```csharp
int Height {get; set;}
```

#### `HelpALink` Property

Gets or sets a help link associated with the window.

```csharp
string HelpALink {get; set;}
```

#### `HelpContextId` Property

Gets or sets the help context id associated with the window.

```csharp
string HelpContextId {get; set;}
```

#### `IsFloating` Property

Gets the floating state of a window.

```csharp
bool IsFloating {get;}
```

#### `Key` Property

Gets the Key of the window in the WindowsCollection.

```csharp
string Key {get;}
```

#### `MaximumSize` Property

Get or sets the maximum size of the window.

```csharp
System.Drawing.Size MaximumSize {get; set;}
```

#### `MinimumSize` Property

Get or sets the minimum size of the window.

```csharp
System.Drawing.Size MinimumSize {get; set;}
```

#### `Tag` Property

Gets or sets the tag property which can be used to logically attach another object or value to a window.

```csharp
object Tag {get; set;}
```

#### `Title` Property

Gets or sets the title of the window.

```csharp
string Title {get; set;}
```

#### `Visible` Property

Gets or sets the visible state of the window.

```csharp
bool Visible {get; set;}
```

#### `Width` Property

Gets or sets the width of the window.

```csharp
int Width {get; set;}
```

## Methods

#### `Close` Method

Destroys the window.

```csharp
void Close();
```

#### `Dock` Method

Docks the window within the main window.

```csharp
void Dock();
```

#### `Float` Method

Displays the window as a floating window.

```csharp
void Float();
```

#### `Hide` Method

Conceals the window from the user.

```csharp
void Hide();
```

#### `Show` Method

Displays the window to the user.

```csharp
void Show();
```
