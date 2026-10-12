---
title: Aveva.ApplicationFramework.Presentation.CommandBarsCollection Class
namespace: Aveva.ApplicationFramework.Presentation
assembly: Aveva.ApplicationFramework.Presentation
kind: Class
source: Aveva.ApplicationFramework
---

# Aveva.ApplicationFramework.Presentation.CommandBarsCollection Class

> Class to represent a CommandBarCollection.

## Syntax

```csharp
public abstract class CommandBarsCollection : ICollection , IEnumerable
```

## Inheritance

`System.Object` → `Aveva.ApplicationFramework.Presentation.CommandBarsCollection`

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

Indexer to get the CommandBar with given Key from the CommandBarCollection.

```csharp
public abstract CommandBar this[ string key ] {get;}
```

#### `SyncRoot` Property

Gets an object that can be used to synchronize access to the collection.

```csharp
public abstract object SyncRoot {get;}
```

**Implements**

ICollection.SyncRoot

## Methods

#### `AddCommandBar` Method (String)

Create and add to the CommandBarCollection a new CommandBar with given Key.

```csharp
public abstract CommandBar AddCommandBar( string key );
```

#### `AddCommandBar` Method (String, Command)

Create and add to the CommandBarCollection a new CommandBar with given Key and associated Command.

```csharp
public abstract CommandBar AddCommandBar( string key , Command command );
```

**Parameters**

- **key** — CommandBar key
- **command** — Command associated with the CommandBar

#### `AddCommandBar` Method (String, String)

Create and add to the CommandBarCollection a new CommandBar with given Key and associated CommandId.

```csharp
public abstract CommandBar AddCommandBar( string key , string commandId );
```

**Parameters**

- **key** — CommandBar key
- **commandId** — Id of the command associated with the CommandBar

#### `AddTaskBar` Method

Create and add a new TaskBar with given Key to the CommandBarCollection.

```csharp
public abstract TaskBar AddTaskBar( string key );
```

#### `Clear` Method

Remove all CommandBars from the CommandBarCollection.

```csharp
public abstract void Clear();
```

#### `Contains` Method

Determine if the CommandBar with the specified Key exists in the CommandBarCollection.

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

Returns an enumerator that can iterate through the CommandBarCollection.

```csharp
public abstract IEnumerator GetEnumerator();
```

**Implements**

IEnumerable.GetEnumerator

#### `RemoveCommandBar` Method (CommandBar)

Remove the specified CommandBar from the CommandBarCollection.

```csharp
public abstract void RemoveCommandBar( CommandBar commandBar );
```

#### `RemoveCommandBar` Method (String)

Remove the CommandBar with given Key from the CommandBarCollection.

```csharp
public abstract void RemoveCommandBar( string key );
```

## Events

#### `CommandBarAdded` Event

Occurs after a CommandBar has been added to the CommandBarCollection.

```csharp
public event CommandBarEventHandler CommandBarAdded;
```

**Event Data**

The event handler receives an argument of type CommandBarEventArgs containing data related to this event. The following CommandBarEventArgs property provides information specific to this event.
Property
Description

CommandBar

Gets the CommandBar object associated with the event

#### `CommandBarRemoved` Event

Occurs after a CommandBar has been removed from the CommandBarCollection.

```csharp
public event CommandBarEventHandler CommandBarRemoved;
```

**Event Data**

The event handler receives an argument of type CommandBarEventArgs containing data related to this event. The following CommandBarEventArgs property provides information specific to this event.
Property
Description

CommandBar

Gets the CommandBar object associated with the event
