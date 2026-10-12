---
title: Aveva.ApplicationFramework.Presentation.TaskBar Class
namespace: Aveva.ApplicationFramework.Presentation
assembly: Aveva.ApplicationFramework.Presentation
kind: Class
source: Aveva.ApplicationFramework
---

# Aveva.ApplicationFramework.Presentation.TaskBar Class

> Class representing a Microsoft Office style "TaskPane" type toolbar.

## Syntax

```csharp
public abstract class TaskBar : CommandBar
```

## Inheritance

`System.Object` → `Aveva.ApplicationFramework.Presentation.CommandBar` → `Aveva.ApplicationFramework.Presentation.TaskBar`

## Thread Safety

Public static ( Shared in Visual Basic) members of this type are
safe for multithreaded operations. Instance members are not guaranteed to be
thread-safe.

## Requirements

Namespace:
Aveva.ApplicationFramework.Presentation
Assembly: Aveva.ApplicationFramework.Presentation (in Aveva.ApplicationFramework.Presentation.dll)

## Properties

#### `DockedContentExtent` Property

Return or sets the size of the taskbar. Either its width or height depending on where it is docked.

```csharp
public abstract int DockedContentExtent {get; set;}
```

#### `HomeTaskPaneToolKey` Property

Returns or sets the key of the tool representing the "home" item. The SelectedTaskPaneToolKey will be set to the HomeTaskPaneToolKey when the home navigation button is pressed.

```csharp
public abstract string HomeTaskPaneToolKey {get; set;}
```

#### `NavigationButtonStyle` Property

Returns or sets a value indicating how the navigation buttons are used to navigate the items in a TaskPane and can also be used to hide the navigation buttons.

```csharp
public abstract NavigationButtonStyle NavigationButtonStyle {get; set;}
```

#### `SelectedTaskPaneToolKey` Property

Returns or sets the key of the currently selected task pane tool.

```csharp
public abstract string SelectedTaskPaneToolKey {get; set;}
```

#### `ShowHomeButton` Property

Returns or sets a value indicating whether the home navigation button will be displayed.

```csharp
public abstract bool ShowHomeButton {get; set;}
```

## Events

#### `AfterTaskPaneToolSelected` Event

Event raised after a task pane tool is selected

```csharp
public event ToolEventHandler AfterTaskPaneToolSelected;
```

**Event Data**

The event handler receives an argument of type ToolEventArgs containing data related to this event. The following ToolEventArgs property provides information specific to this event.
Property
Description

Key

The tools key.
