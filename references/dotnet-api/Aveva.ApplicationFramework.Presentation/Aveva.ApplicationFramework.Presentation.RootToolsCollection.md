---
title: Aveva.ApplicationFramework.Presentation.RootToolsCollection Class
namespace: Aveva.ApplicationFramework.Presentation
assembly: Aveva.ApplicationFramework.Presentation
kind: Class
source: Aveva.ApplicationFramework
---

# Aveva.ApplicationFramework.Presentation.RootToolsCollection Class

> Class representing a RootToolsCollection.

## Syntax

```csharp
public abstract class RootToolsCollection : ICollection , IEnumerable
```

## Inheritance

`System.Object` → `Aveva.ApplicationFramework.Presentation.RootToolsCollection`

## Thread Safety

Public static ( Shared in Visual Basic) members of this type are
safe for multithreaded operations. Instance members are not guaranteed to be
thread-safe.

## Requirements

Namespace:
Aveva.ApplicationFramework.Presentation
Assembly: Aveva.ApplicationFramework.Presentation (in Aveva.ApplicationFramework.Presentation.dll)

## Properties

#### `Count` Property

Gets the number of elements contained in the collection.

```csharp
public abstract int Count {get;}
```

**Implements**

ICollection.Count

#### `IsSynchronized` Property

Gets a value indicating whether access to the collection is synchronized (thread-safe).

```csharp
public abstract bool IsSynchronized {get;}
```

**Implements**

ICollection.IsSynchronized

#### `Item` Property

Indexer to get the root tool with given Key from the RootToolsCollection as an ITool object.

```csharp
public abstract ITool this[ string key ] {get;}
```

#### `SyncRoot` Property

Gets an object that can be used to synchronize access to the collection.

```csharp
public abstract object SyncRoot {get;}
```

**Implements**

ICollection.SyncRoot

## Methods

#### `AddButtonTool` Method (String, String, Image)

Create and add a new ButtonTool object to the RootToolsCollection.

```csharp
public abstract ButtonTool AddButtonTool( string key , string text , Image image );
```

**Parameters**

- **key** — Unique key in the RootToolsCollection.
- **text** — Caption for the tool.
- **image** — Icon for the tool.

#### `AddButtonTool` Method (String, String, Image, Command)

Create and add a new ButtonTool object to the RootToolsCollection.

```csharp
public abstract ButtonTool AddButtonTool( string key , string text , Image image , Command command );
```

**Parameters**

- **key** — Unique key in the RootToolsCollection.
- **text** — Caption for the tool.
- **image** — Icon for the tool.
- **command** — Command which the tool is associated with.

#### `AddButtonTool` Method (String, String, Image, String)

Create and add a new ButtonTool object to the RootToolsCollection.

```csharp
public abstract ButtonTool AddButtonTool( string key , string text , Image image , string commandId );
```

**Parameters**

- **key** — Unique key in the RootToolsCollection.
- **text** — Caption for the tool.
- **image** — Icon for the tool.
- **commandId** — Identifier of command which the tool is associated with.

#### `AddComboBoxTool` Method (String, String, Image)

Create and add a new ComboBoxTool object to the RootToolsCollection.

```csharp
public abstract ComboBoxTool AddComboBoxTool( string key , string text , Image image );
```

**Parameters**

- **key** — Unique key in the RootToolsCollection.
- **text** — Caption for the tool.
- **image** — Icon for the tool.

#### `AddComboBoxTool` Method (String, String, Image, Command)

Create and add a new ComboBoxTool object to the RootToolsCollection.

```csharp
public abstract ComboBoxTool AddComboBoxTool( string key , string text , Image image , Command command );
```

**Parameters**

- **key** — Unique key in the RootToolsCollection.
- **text** — Caption for the tool.
- **image** — Icon for the tool.
- **command** — Command which the tool is associated with.

#### `AddComboBoxTool` Method (String, String, Image, String)

Create and add a new ComboBoxTool object to the RootToolsCollection.

```csharp
public abstract ComboBoxTool AddComboBoxTool( string key , string text , Image image , string commandId );
```

**Parameters**

- **key** — Unique key in the RootToolsCollection.
- **text** — Caption for the tool.
- **image** — Icon for the tool.
- **commandId** — Id of command which the tool is associated with.

#### `AddContainerTool` Method

Create and add a new ContainerTool object to the RootToolsCollection.

```csharp
public abstract ContainerTool AddContainerTool( string key , string text , Control control );
```

**Parameters**

- **key** — Unique key in the RootToolsCollection.
- **text** — Caption for the tool.
- **control** — Control assigned to the tool.

#### `AddFontListTool` Method (String, String, Image)

Create and add a new FontListTool object in the RootToolsCollection

```csharp
public abstract FontListTool AddFontListTool( string key , string text , Image image );
```

**Parameters**

- **key** — Unique key in the RootToolsCollection.
- **text** — Caption for the tool.
- **image** — Icon for the tool.

#### `AddFontListTool` Method (String, String, Image, Command)

Create and add a new FontListTool object in the RootToolsCollection

```csharp
public abstract FontListTool AddFontListTool( string key , string text , Image image , Command command );
```

**Parameters**

- **key** — Unique key in the RootToolsCollection.
- **text** — Caption for the tool.
- **image** — Icon for the tool.
- **command** — Command which the tool is associated with.

#### `AddFontListTool` Method (String, String, Image, String)

Create and add a new FontListTool object in the RootToolsCollection

```csharp
public abstract FontListTool AddFontListTool( string key , string text , Image image , string commandId );
```

**Parameters**

- **key** — Unique key in the RootToolsCollection.
- **text** — Caption for the tool.
- **image** — Icon for the tool.
- **commandId** — Identifier of command which the tool is associated with.

#### `AddLabelTool` Method

Create and add a new LabelTool object to the RootToolsCollection.

```csharp
public abstract LabelTool AddLabelTool( string key , string text , Image image );
```

**Parameters**

- **key** — Unique key in the RootToolsCollection.
- **text** — Caption for the tool.
- **image** — Icon for the tool.

#### `AddListTool` Method (String)

Create and add a new ListTool object in the RootToolsCollection

```csharp
public abstract ListTool AddListTool( string key );
```

**Parameters**

- **key** — Unique key in the RootToolsCollection.

#### `AddListTool` Method (String, Command)

Create and add a new ListTool object in the RootToolsCollection

```csharp
public abstract ListTool AddListTool( string key , Command command );
```

**Parameters**

- **key** — Unique key in the RootToolsCollection.
- **command** — Command which the tool is associated with.

#### `AddListTool` Method (String, String)

Create and add a new ListTool object in the RootToolsCollection

```csharp
public abstract ListTool AddListTool( string key , string commandId );
```

**Parameters**

- **key** — Unique key in the RootToolsCollection.
- **commandId** — Identifier of command which the tool is associated with.

#### `AddMdiWindowListTool` Method

Create and add a new MdiWindowListTool object in the RootToolsCollection.

```csharp
public abstract MdiWindowListTool AddMdiWindowListTool( string key );
```

**Parameters**

- **key** — Unique key in the RootToolsCollection.

#### `AddMenuTool` Method (String, String, Image)

Create and add a new MenuTool object to the RootToolsCollection.

```csharp
public abstract MenuTool AddMenuTool( string key , string text , Image image );
```

**Parameters**

- **key** — Unique key in the RootToolsCollection.
- **text** — Caption for the tool.
- **image** — Icon for the tool.

#### `AddMenuTool` Method (String, String, Image, Command)

Create and add a new MenuTool object to the RootToolsCollection.

```csharp
public abstract MenuTool AddMenuTool( string key , string text , Image image , Command command );
```

**Parameters**

- **key** — Unique key in the RootToolsCollection.
- **text** — Caption for the tool.
- **image** — Icon for the tool.
- **command** — Command which the tool is associated with.

#### `AddMenuTool` Method (String, String, Image, String)

Create and add a new MenuTool object to the RootToolsCollection.

```csharp
public abstract MenuTool AddMenuTool( string key , string text , Image image , string commandId );
```

**Parameters**

- **key** — Unique key in the RootToolsCollection.
- **text** — Caption for the tool.
- **image** — Icon for the tool.
- **commandId** — Identifier of command which the tool is associated with.

#### `AddPopupColorPickerTool` Method (String, String, Image)

Create and add a new PopupColorPickerTool object in the RootToolsCollection

```csharp
public abstract PopupColorPickerTool AddPopupColorPickerTool( string key , string text , Image image );
```

**Parameters**

- **key** — Unique key in the RootToolsCollection.
- **text** — Caption for the tool.
- **image** — Icon for the tool.

#### `AddPopupColorPickerTool` Method (String, String, Image, Command)

Create and add a new PopupColorPickerTool object in the RootToolsCollection

```csharp
public abstract PopupColorPickerTool AddPopupColorPickerTool( string key , string text , Image image , Command command );
```

**Parameters**

- **key** — Unique key in the RootToolsCollection.
- **text** — Caption for the tool.
- **image** — Icon for the tool.
- **command** — Command which the tool is associated with.

#### `AddPopupColorPickerTool` Method (String, String, Image, String)

Create and add a new PopupColorPickerTool object in the RootToolsCollection

```csharp
public abstract PopupColorPickerTool AddPopupColorPickerTool( string key , string text , Image image , string commandId );
```

**Parameters**

- **key** — Unique key in the RootToolsCollection.
- **text** — Caption for the tool.
- **image** — Icon for the tool.
- **commandId** — Identifier of command which the tool is associated with.

#### `AddPopupContainerTool` Method (String, String, Image, Control)

Create and add a new PopupContainerTool object to the RootToolsCollection.

```csharp
public abstract PopupContainerTool AddPopupContainerTool( string key , string text , Image image , Control control );
```

**Parameters**

- **key** — Unique key in the RootToolsCollection.
- **text** — Caption for the tool.
- **image** — Icon for the tool.
- **control** — Control assigned to the tool.

#### `AddPopupContainerTool` Method (String, String, Image, Control, Command)

Create and add a new PopupContainerTool object to the RootToolsCollection.

```csharp
public abstract PopupContainerTool AddPopupContainerTool( string key , string text , Image image , Control control , Command command );
```

**Parameters**

- **key** — Unique key in the RootToolsCollection.
- **text** — Caption for the tool.
- **image** — Icon for the tool.
- **control** — Control assigned to the tool.
- **command** — Command which the tool is associated with.

#### `AddPopupContainerTool` Method (String, String, Image, Control, String)

Create and add a new PopupContainerTool object to the RootToolsCollection.

```csharp
public abstract PopupContainerTool AddPopupContainerTool( string key , string text , Image image , Control control , string commandId );
```

**Parameters**

- **key** — Unique key in the RootToolsCollection.
- **text** — Caption for the tool.
- **image** — Icon for the tool.
- **control** — Control assigned to the tool.
- **commandId** — Identifier of command which the tool is associated with.

#### `AddStateButtonTool` Method (String, String, Image)

Create and add a new StateButtonTool object to the RootToolsCollection.

```csharp
public abstract StateButtonTool AddStateButtonTool( string key , string text , Image image );
```

**Parameters**

- **key** — Unique key in the RootToolsCollection.
- **text** — Caption for the tool.
- **image** — Icon for the tool.

#### `AddStateButtonTool` Method (String, String, Image, Command)

Create and add a new StateButtonTool object to the RootToolsCollection.

```csharp
public abstract StateButtonTool AddStateButtonTool( string key , string text , Image image , Command command );
```

**Parameters**

- **key** — Unique key in the RootToolsCollection.
- **text** — Caption for the tool.
- **image** — Icon for the tool.
- **command** — Command which the tool is associated with.

#### `AddStateButtonTool` Method (String, String, Image, String)

Create and add a new StateButtonTool object to the RootToolsCollection.

```csharp
public abstract StateButtonTool AddStateButtonTool( string key , string text , Image image , string commandId );
```

**Parameters**

- **key** — Unique key in the RootToolsCollection.
- **text** — Caption for the tool.
- **image** — Icon for the tool.
- **commandId** — Identifier of command which the tool is associated with.

#### `AddTaskPaneTool` Method

Create and add a new TaskPaneTool object in the RootToolsCollection.

```csharp
public abstract TaskPaneTool AddTaskPaneTool( string key );
```

**Parameters**

- **key** — Unique key in the RootToolsCollection.

#### `AddTextBoxTool` Method (String, String, Image, String)

Create and add a new TextBoxTool object to the RootToolsCollection.

```csharp
public abstract TextBoxTool AddTextBoxTool( string key , string text , Image image , string val );
```

**Parameters**

- **key** — Unique key in the RootToolsCollection.
- **text** — Caption for the tool.
- **image** — Icon for the tool.
- **val** — Textual value to be displayed in the tool.

#### `AddTextBoxTool` Method (String, String, Image, String, Command)

Create and add a new TextBoxTool object to the RootToolsCollection.

```csharp
public abstract TextBoxTool AddTextBoxTool( string key , string text , Image image , string val , Command command );
```

**Parameters**

- **key** — Unique key in the RootToolsCollection.
- **text** — Caption for the tool.
- **image** — Icon for the tool.
- **val** — Textual value to be displayed in the tool.
- **command** — Command which the tool is associated with.

#### `AddTextBoxTool` Method (String, String, Image, String, String)

Create and add a new TextBoxTool object to the RootToolsCollection.

```csharp
public abstract TextBoxTool AddTextBoxTool( string key , string text , Image image , string val , string commandId );
```

**Parameters**

- **key** — Unique key in the RootToolsCollection.
- **text** — Caption for the tool.
- **image** — Icon for the tool.
- **val** — Textual value to be displayed in the tool.
- **commandId** — Identifier of command which the tool is associated with.

#### `Clear` Method

Remove all tools from the RootToolsCollection.

```csharp
public abstract void Clear();
```

#### `Contains` Method

Determine if the tool with the specified Key exists in the RootToolsCollection.

```csharp
public abstract bool Contains( string key );
```

#### `CopyTo` Method

Copies the elements of the collection to an Array, starting at a particular Array index.

```csharp
public abstract void CopyTo( Array array , int index );
```

**Parameters**

- **array** — The one-dimensional Array that is the destination of the elements copied from collection. The Array must have zero-based indexing.
- **index** — The zero-based index in array at which copying begins.

**Implements**

ICollection.CopyTo

#### `GetEnumerator` Method

Returns an enumerator that can iterate through the Collection.

```csharp
public abstract IEnumerator GetEnumerator();
```

**Implements**

IEnumerable.GetEnumerator

#### `Remove` Method

Remove the tool with the specified Key from the RootToolsCollection.

```csharp
public abstract void Remove( string key );
```

## Events

#### `ToolAdded` Event

Occurs after a tool has been added to the RootToolsCollection.

```csharp
public event ToolEventHandler ToolAdded;
```

**Event Data**

The event handler receives an argument of type ToolEventArgs containing data related to this event. The following ToolEventArgs property provides information specific to this event.
Property
Description

Key

The tools key.

#### `ToolRemoved` Event

Occurs after a tool has been removed from the RootToolsCollection.

```csharp
public event ToolEventHandler ToolRemoved;
```

**Event Data**

The event handler receives an argument of type ToolEventArgs containing data related to this event. The following ToolEventArgs property provides information specific to this event.
Property
Description

Key

The tools key.
