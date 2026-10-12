---
title: Aveva.ApplicationFramework.SettingsGroup Class
namespace: Aveva.ApplicationFramework
assembly: Aveva.ApplicationFramework
kind: Class
source: Aveva.ApplicationFramework
---

# Aveva.ApplicationFramework.SettingsGroup Class

> Class that represents a named colletion of keyed objects which represent application settings

## Syntax

```csharp
public abstract class SettingsGroup : ICollection , IEnumerable
```

## Inheritance

`System.Object` → `Aveva.ApplicationFramework.SettingsGroup`

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

#### `Directory` Property

The name of the directory into which the settings for this group will be persisted

```csharp
public abstract string Directory {get;}
```

#### `IsSynchronized` Property

Gets a value indicating whether access to the collection is synchronized (thread-safe).

```csharp
public abstract bool IsSynchronized {get;}
```

**Implements**

ICollection.IsSynchronized

#### `Item` Property

Indexer to return the object associated with the given key

```csharp
public abstract object this[ string key ] {get; set;}
```

#### `Name` Property

Name of settings group

```csharp
public abstract string Name {get;}
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

Returns an enumerator that can iterate through the SettingsGroup.

```csharp
public abstract IEnumerator GetEnumerator();
```

**Return Value**

An IEnumerator for the entire SettingsGroup.

**Implements**

IEnumerable.GetEnumerator
