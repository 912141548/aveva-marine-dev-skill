---
title: Aveva.ApplicationFramework.Presentation.WindowsCollection Class
namespace: Aveva.ApplicationFramework.Presentation
assembly: Aveva.ApplicationFramework.Presentation
kind: Class
source: Aveva.ApplicationFramework
---

# Aveva.ApplicationFramework.Presentation.WindowsCollection Class

> Provides access to a collection of application windows.

## Syntax

```csharp
public abstract class WindowsCollection : ICollection , IEnumerable
```

## Inheritance

`System.Object` → `Aveva.ApplicationFramework.Presentation.WindowsCollection`

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

Indexer which returns an IWindow interface for the window with the given key.

```csharp
public abstract IWindow this[ string key ] {get;}
```

#### `SyncRoot` Property

Gets an object that can be used to synchronize access to the collection.

```csharp
public abstract object SyncRoot {get;}
```

**Implements**

ICollection.SyncRoot

## Methods

#### `ContainsKey` Method

Determines whether the WindowCollection contains a specific key.

```csharp
public abstract bool ContainsKey( string key );
```

**Parameters**

- **key** — The key to locate in the WindowCollection.

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

Remove the window with the given key from the collection.

```csharp
public abstract void Remove( string key );
```

**Parameters**

- **key** — The key of the window to remove.
