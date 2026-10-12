---
title: Aveva.ApplicationFramework.Presentation.StatusBarPanelsCollection Class
namespace: Aveva.ApplicationFramework.Presentation
assembly: Aveva.ApplicationFramework.Presentation
kind: Class
source: Aveva.ApplicationFramework
---

# Aveva.ApplicationFramework.Presentation.StatusBarPanelsCollection Class

> Represents a collection of status bar panels.

## Syntax

```csharp
public abstract class StatusBarPanelsCollection : ICollection , IEnumerable
```

## Inheritance

`System.Object` → `Aveva.ApplicationFramework.Presentation.StatusBarPanelsCollection`

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

Indexer which returns an IStatusBarPanel interface for the panel with the given key.

```csharp
public abstract IStatusBarPanel this[ string key ] {get;}
```

#### `SyncRoot` Property

Gets an object that can be used to synchronize access to the collection.

```csharp
public abstract object SyncRoot {get;}
```

**Implements**

ICollection.SyncRoot

## Methods

#### `AddTextPanel` Method (String, String)

Create and add a new StartsBarTextPanel to the collection

```csharp
public abstract StatusBarTextPanel AddTextPanel( string key , string text );
```

**Parameters**

- **key** — Panel Key
- **text** — Panel Text

#### `AddTextPanel` Method (String, String, Image)

Create and add a new StartsBarTextPanel to the collection

```csharp
public abstract StatusBarTextPanel AddTextPanel( string key , string text , Image image );
```

**Parameters**

- **key** — Panel Key
- **text** — Panel Text
- **image** — Panel Image

#### `ContainsKey` Method

Determines whether the StatusBarPanelsCollection contains a specific key.

```csharp
public abstract bool ContainsKey( string key );
```

**Parameters**

- **key** — The key to locate in the StatusBarPanelsCollection.

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

Returns an enumerator that can iterate through the collection.

```csharp
public abstract IEnumerator GetEnumerator();
```

**Implements**

IEnumerable.GetEnumerator

#### `Remove` Method

Remove the panel with the given key from the collection.

```csharp
public abstract void Remove( string key );
```

**Parameters**

- **key** — The key of the window to remove.
