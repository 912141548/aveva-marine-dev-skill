---
title: Aveva.ApplicationFramework.Presentation.ToolsCollection Class
namespace: Aveva.ApplicationFramework.Presentation
assembly: Aveva.ApplicationFramework.Presentation
kind: Class
source: Aveva.ApplicationFramework
---

# Aveva.ApplicationFramework.Presentation.ToolsCollection Class

> Class representing a ToolsCollection.

## Syntax

```csharp
public abstract class ToolsCollection : ICollection , IEnumerable
```

## Inheritance

`System.Object` → `Aveva.ApplicationFramework.Presentation.ToolsCollection`

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

#### `Item` Property (Overload 1)

Indexer to get the instance of the tool at the specified index of the ToolsCollection as an ITool object.

**Overload List**

Indexer to get the instance of the tool at the specified index of the ToolsCollection as an ITool object.
public abstract ITool this[int] {get;}
Indexer to get the instance of the tool with given Key from the ToolsCollection as an ITool object.
public abstract ITool this[string] {get;}

#### `Item` Property (Int32)

Indexer to get the instance of the tool at the specified index of the ToolsCollection as an ITool object.

```csharp
public abstract ITool this[ int index ] {get;}
```

#### `Item` Property (String)

Indexer to get the instance of the tool with given Key from the ToolsCollection as an ITool object.

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

#### `AddTool` Method

Create an instance of a root tool and add it to the ToolsCollection, with the same Key.

```csharp
public abstract ITool AddTool( string key );
```

**Parameters**

- **key** — Key of the root tool in the RootToolsCollection.

#### `Clear` Method

Remove all tool instances from the ToolsCollection.

```csharp
public abstract void Clear();
```

#### `Contains` Method

Determine if the tool instance with the specified Key exists in the ToolsCollection.

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

#### `IndexOf` Method

Get the index of the tool with given Key from the ToolsCollection. Returns -1 if tool is not in the collection.

```csharp
public abstract int IndexOf( string key );
```

#### `InsertTool` Method

Create an instance of a root tool and insert it into the ToolsCollection at the given index, with the same Key.

```csharp
public abstract ITool InsertTool( string key , int index );
```

**Parameters**

- **key** — Key of the root tool in the RootToolsCollection.
- **index** — Position which tool instance will have in ToolsCollection.

#### `Remove` Method

Remove the tool instance with the specified Key from the ToolsCollection.

```csharp
public abstract void Remove( string key );
```

#### `RemoveAt` Method

Remove the tool instance at the specified index position from the ToolsCollection.

```csharp
public abstract void RemoveAt( int index );
```
