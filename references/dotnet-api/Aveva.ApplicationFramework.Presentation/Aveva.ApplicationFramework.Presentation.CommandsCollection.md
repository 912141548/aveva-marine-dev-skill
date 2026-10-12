---
title: Aveva.ApplicationFramework.Presentation.CommandsCollection Class
namespace: Aveva.ApplicationFramework.Presentation
assembly: Aveva.ApplicationFramework.Presentation
kind: Class
source: Aveva.ApplicationFramework
---

# Aveva.ApplicationFramework.Presentation.CommandsCollection Class

> Class that represents a CommandCollection.

## Syntax

```csharp
public abstract class CommandsCollection : ICollection , IEnumerable
```

## Inheritance

`System.Object` → `Aveva.ApplicationFramework.Presentation.CommandsCollection`

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

Indexer to get the Command with given Key from the CommandCollection.

```csharp
public abstract Command this[ string key ] {get;}
```

#### `SyncRoot` Property

Gets an object that can be used to synchronize access to the collection.

```csharp
public abstract object SyncRoot {get;}
```

**Implements**

ICollection.SyncRoot

## Methods

#### `Add` Method

Add the given Command to the CommandCollection.

```csharp
public abstract void Add( Command command );
```

#### `ContainsKey` Method

Determine if the Command with the specified Key exists in the CommandCollection.

```csharp
public abstract bool ContainsKey( string key );
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

#### `Remove` Method

Remove the Command with given Key from the CommandCollection.

```csharp
public abstract void Remove( string key );
```

## Events

#### `CommandAdded` Event

Occurs after a Command has been added to the CommandCollection.

```csharp
public event CommandEventHandler CommandAdded;
```

**Event Data**

The event handler receives an argument of type CommandEventArgs containing data related to this event. The following CommandEventArgs property provides information specific to this event.
Property
Description

Command

Gets the Command object associated with the event

#### `CommandRemoved` Event

Occurs after a Command has been removed from the CommandCollection.

```csharp
public event CommandEventHandler CommandRemoved;
```

**Event Data**

The event handler receives an argument of type CommandEventArgs containing data related to this event. The following CommandEventArgs property provides information specific to this event.
Property
Description

Command

Gets the Command object associated with the event
