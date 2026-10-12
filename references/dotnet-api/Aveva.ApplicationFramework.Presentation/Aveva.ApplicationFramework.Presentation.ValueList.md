---
title: Aveva.ApplicationFramework.Presentation.ValueList Class
namespace: Aveva.ApplicationFramework.Presentation
assembly: Aveva.ApplicationFramework.Presentation
kind: Class
source: Aveva.ApplicationFramework
---

# Aveva.ApplicationFramework.Presentation.ValueList Class

> Class representing a ValueList, which is a collection of ValueListItem objects. It is typicall assigned to a ComboBoxTool as the list of options displayed as the dropdown list.

## Syntax

```csharp
public abstract class ValueList : ICollection , IEnumerable
```

## Inheritance

`System.Object` → `Aveva.ApplicationFramework.Presentation.ValueList`

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

#### `DisplayStyle` Property

Set the DisplayStyle for the ValueList. ValueListDisplayStyle enumeration specifies what properties of ValueListItems will be displayed.

```csharp
public abstract ValueListDisplayStyle DisplayStyle {get; set;}
```

#### `IsSynchronized` Property

Gets a value indicating whether access to the collection is synchronized (thread-safe).

```csharp
public abstract bool IsSynchronized {get;}
```

**Implements**

ICollection.IsSynchronized

#### `Item` Property (Overload 1)

Class representing a ValueListItem, which can be a member of ValueList.

```csharp
public abstract class ValueListItem
```

**Thread Safety**

Public static ( Shared in Visual Basic) members of this type are
safe for multithreaded operations. Instance members are not guaranteed to be
thread-safe.

**Requirements**

Namespace:
Aveva.ApplicationFramework.Presentation
Assembly: Aveva.ApplicationFramework.Presentation (in Aveva.ApplicationFramework.Presentation.dll)

#### `Item` Property (Int32)

Indexer to get the ValuListItem at the given postion index from the ValueList.

```csharp
public abstract ValueListItem this[ int index ] {get;}
```

#### `Item` Property (String)

Indexer to get the ValuListItem with given DisplayText from the ValueList.

```csharp
public abstract ValueListItem this[ string DisplayText ] {get;}
```

#### `SortStyle` Property

Set the SortStyle for the ValueList. ValueListSortStyle enumeration specifies how the ValueListItems will be sorted for display.

```csharp
public abstract ValueListSortStyle SortStyle {get; set;}
```

#### `SyncRoot` Property

Gets an object that can be used to synchronize access to the collection.

```csharp
public abstract object SyncRoot {get;}
```

**Implements**

ICollection.SyncRoot

## Methods

#### `Add` Method (String)

Create and add a new ValueListItem object to the ValueList. Note that the ValueListItem created will contain the given DisplayText and a default DataValue with value (object)DislayText.

```csharp
public abstract ValueListItem Add( string DisplayText );
```

**Parameters**

- **DisplayText** — ValueListItem display text.

#### `Add` Method (String, Object)

Create and add a new ValueListItem object to the ValueList.

```csharp
public abstract ValueListItem Add( string DisplayText , object DataValue );
```

**Parameters**

- **DisplayText** — ValueListItem display text.
- **DataValue** — ValueListItem DataValue object.

#### `Add` Method (String, Object, Image)

Create and add a new ValueListItem object to the ValueList.

```csharp
public abstract ValueListItem Add( string DisplayText , object DataValue , Image image );
```

**Parameters**

- **DisplayText** — ValueListItem display text.
- **DataValue** — ValueListItem DataValue object.
- **image** — ValueListItem display icon.

#### `Clear` Method

Remove all ValueListItems from the ValueList.

```csharp
public abstract void Clear();
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

#### `Insert` Method (String, Int32)

Create and insert a new ValueListItem object into the ValueList. Note that the ValueListItem created will contain the given DisplayText and a default DataValue with value (object)DislayText.

```csharp
public abstract ValueListItem Insert( string DisplayText , int index );
```

**Parameters**

- **DisplayText** — ValueListItem display text.
- **index** — Index position of new ValueListItem in the ValueList

#### `Insert` Method (String, Object, Image, Int32)

Create and insert a new ValueListItem object into the ValueList.

```csharp
public abstract ValueListItem Insert( string DisplayText , object DataValue , Image image , int index );
```

**Parameters**

- **DisplayText** — ValueListItem display text.
- **DataValue** — ValueListItem DataValue object.
- **image** — ValueListItem display icon.
- **index** — Index position of new ValueListItem in the ValueList

#### `Insert` Method (String, Object, Int32)

Create and insert a new ValueListItem object into the ValueList.

```csharp
public abstract ValueListItem Insert( string DisplayText , object DataValue , int index );
```

**Parameters**

- **DisplayText** — ValueListItem display text.
- **DataValue** — ValueListItem DataValue object.
- **index** — Index position of new ValueListItem in the ValueList

#### `Remove` Method (ValueListItem)

Remove the specified ValueListItem object from the ValueList.

```csharp
public abstract void Remove( ValueListItem valueListItem );
```

#### `Remove` Method (Int32)

Remove the ValueListItem at the specified index position from the ValueList.

```csharp
public abstract void Remove( int index );
```

#### `Remove` Method (String)

Remove the ValueListItem with the specified DisplayText from the ValueList.

```csharp
public abstract void Remove( string DisplayText );
```
