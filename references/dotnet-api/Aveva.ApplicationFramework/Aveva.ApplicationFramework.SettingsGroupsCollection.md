---
title: Aveva.ApplicationFramework.SettingsGroupsCollection Class
namespace: Aveva.ApplicationFramework
assembly: Aveva.ApplicationFramework
kind: Class
source: Aveva.ApplicationFramework
---

# Aveva.ApplicationFramework.SettingsGroupsCollection Class

> A collection of SettingsGroup objects

## Syntax

```csharp
public abstract class SettingsGroupsCollection : ICollection , IEnumerable
```

## Inheritance

`System.Object` → `Aveva.ApplicationFramework.SettingsGroupsCollection`

## Thread Safety

Public static ( Shared in Visual Basic) members of this type are
safe for multithreaded operations. Instance members are not guaranteed to be
thread-safe.

## Requirements

Namespace:
Aveva.ApplicationFramework
Assembly: Aveva.ApplicationFramework (in Aveva.ApplicationFramework.dll)

## Properties

#### `Count` Property

Gets the number of Addins actually contained in the collection.

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

Indexer to resturn the SettingsGroup with the given name.

```csharp
public abstract SettingsGroup this[ string groupName ] {get;}
```

#### `SyncRoot` Property

Gets an object that can be used to synchronize access to the collection.

```csharp
public abstract object SyncRoot {get;}
```

**Implements**

ICollection.SyncRoot

## Methods

#### `CopyTo` Method

Copies the collection or a portion of it to a one-dimensional array.

```csharp
public abstract void CopyTo( Array array , int index );
```

**Parameters**

- **array** — The one-dimensional Array that is the destination of the elements copied from the collection. The Array must have zero-based indexing.
- **index** — The zero-based index in array at which copying begins.

**Implements**

ICollection.CopyTo

#### `GetEnumerator` Method

Returns an enumerator that can iterate through the SettingsGroupCollection.

```csharp
public abstract IEnumerator GetEnumerator();
```

**Return Value**

An IEnumerator for the entire SettingsGroupCollection.

**Implements**

IEnumerable.GetEnumerator
