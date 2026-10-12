---
title: Aveva.ApplicationFramework.Presentation.CommandBarManager Class
namespace: Aveva.ApplicationFramework.Presentation
assembly: Aveva.ApplicationFramework.Presentation
kind: Class
source: Aveva.ApplicationFramework
---

# Aveva.ApplicationFramework.Presentation.CommandBarManager Class

> Class representing a CommandBarManager.

## Syntax

```csharp
public abstract class CommandBarManager : ISupportInitialize
```

## Inheritance

`System.Object` → `Aveva.ApplicationFramework.Presentation.CommandBarManager`

## Thread Safety

Public static ( Shared in Visual Basic) members of this type are
safe for multithreaded operations. Instance members are not guaranteed to be
thread-safe.

## Requirements

Namespace:
Aveva.ApplicationFramework.Presentation
Assembly: Aveva.ApplicationFramework.Presentation (in Aveva.ApplicationFramework.Presentation.dll)

## Properties

#### `AllowCustomization` Property

Gets or sets the default Customization status for all CommandBars belonging to the CommandBarManager;

```csharp
public abstract bool AllowCustomization {get; set;}
```

#### `CommandBars` Property

Gets the collection of CommandBar objects currently managed by the CommandBarManager.

```csharp
public abstract CommandBarsCollection CommandBars {get;}
```

#### `Controls` Property

Gets a Hashtable which contains controls to use for controls containers.

```csharp
public abstract System.Collections.Hashtable Controls {get;}
```

#### `CustomizationDialog` Property

Gets the non standard customization dialog.

```csharp
public abstract System.Windows.Forms.Form CustomizationDialog {get;}
```

#### `CustomizationType` Property

Gets or sets the type of customization.

```csharp
public abstract CustomizationType CustomizationType {get; set;}
```

#### `Enabled` Property

Get or sets a property which controls the enabled state of all CommandBars

```csharp
public abstract bool Enabled {get; set;}
```

#### `Instance` Property

Get instance of commandbar manager

```csharp
public static CommandBarManager Instance {get; set;}
```

#### `IsUpdating` Property

Gets whether the CommandBarManager is currently in update mode. (i.e. BeginInit() has been called)

```csharp
public abstract bool IsUpdating {get;}
```

#### `MenuBar` Property

Gets the CommandBar object that represents the Main Menu Bar.

```csharp
public abstract CommandBar MenuBar {get;}
```

#### `RootTools` Property

Gets the collection of RootTool objects currently managed by the CommandBarManager.

```csharp
public abstract RootToolsCollection RootTools {get;}
```

## Methods

#### `AddOptionSet` Method

Create a new OptionSet indentified by the specified Key An OptionSet is a set of StateButtonTools (a radio group) where at most one of the tools can can be in the Down (pressed) state.

```csharp
public abstract void AddOptionSet( bool allowAllUp , string key );
```

**Parameters**

- **allowAllUp** — Boolean, controlling whether all buttons can be in the Up (unpressed) state simultaneously.
- **key** — Unique key indentifying the OptionSet.

#### `AddUICustomizationFile` Method

Adds a new UI Customization file.

```csharp
public abstract void AddUICustomizationFile( string pathname , string name );
```

**Parameters**

- **pathname** — 
- **name** —

#### `AddUICustomizationFromStream` Method

Adds a new UI Customization from the given stream

```csharp
public abstract void AddUICustomizationFromStream( Stream stream , string name );
```

**Parameters**

- **stream** — 
- **name** —

#### `AddUICustomizationSet` Method

Adds a set of UI Customization files.

```csharp
public abstract void AddUICustomizationSet( string pathname , string[] args );
```

**Parameters**

- **pathname** — 
- **args** —

#### `BeginInit` Method

ISupportInitialize allows controls to optimize for multiple sets to properties. As a result, you can initialize co-dependent properties or batch set multiple properties at design time. Signal the object that initialization is starting.

```csharp
public abstract void BeginInit();
```

**Implements**

ISupportInitialize.BeginInit

#### `EndInit` Method

ISupportInitialize allows controls to optimize for multiple sets to properties. As a result, you can initialize co-dependent properties or batch set multiple properties at design time. Signal that initialization is complete.

```csharp
public abstract void EndInit();
```

**Implements**

ISupportInitialize.EndInit

#### `LoadLayout` Method

Load the saved command CommandBars layout from a sttings file.

```csharp
public abstract void LoadLayout();
```

#### `LoadUI` Method

Creates the Menus,CommandBars and ContextMenus defined by the loaded UICustomization files.

```csharp
public abstract void LoadUI();
```

#### `SaveLayout` Method

Save the current command CommandBars layout to a sttings file.

```csharp
public abstract void SaveLayout();
```

#### `SelectTaskPane` Method

Select the taskpane with the given key

```csharp
public abstract void SelectTaskPane( string key );
```

**Parameters**

- **key** —

## Events

#### `CommandBarLayoutLoaded` Event

Event raised when the commandBar layout is loaded

```csharp
public event EventHandler CommandBarLayoutLoaded;
```

#### `UILoaded` Event

Event raised when the UI (Menus,CommandBars and ContextMenus) have finished loading after a call to LoadUI().

```csharp
public event EventHandler UILoaded;
```
