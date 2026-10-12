---
title: Aveva.ApplicationFramework.Presentation.CommandList Class
namespace: Aveva.ApplicationFramework.Presentation
assembly: Aveva.ApplicationFramework.Presentation
kind: Class
source: Aveva.ApplicationFramework
---

# Aveva.ApplicationFramework.Presentation.CommandList Class

> An ArrayList use for the list property of Command objects which supports an IsModified property.

## Syntax

```csharp
public class CommandList : ArrayList
```

## Inheritance

`System.Object` → `System.Collections.ArrayList` → `Aveva.ApplicationFramework.Presentation.CommandList`

## Thread Safety

Public static ( Shared in Visual Basic) members of this type are
safe for multithreaded operations. Instance members are not guaranteed to be
thread-safe.

## Requirements

Namespace:
Aveva.ApplicationFramework.Presentation
Assembly: Aveva.ApplicationFramework.Presentation (in Aveva.ApplicationFramework.Presentation.dll)

## Constructors

#### `CommandList` Constructor

Default constructor for CommandList.

```csharp
public CommandList();
```

## Properties

#### `IsModified` Property

Flag which is set to true whenever the list is modified.

```csharp
public bool IsModified {get; set;}
```

#### `Item` Property

Gets or sets the element at the specified index.

```csharp
public override object this[ int index ] {get; set;}
```

**Implements**

IList.Item

## Methods

#### `Add` Method

Adds an object to the end of the CommandList.

```csharp
public override int Add( object value );
```

**Parameters**

- **value** — The Object to be added to the end of the CommandList

**Implements**

IList.Add

#### `AddRange` Method

Adds the elements of an ICollection to the end of the CommandList.

```csharp
public override void AddRange( ICollection c );
```

**Parameters**

- **c** — The ICollection whose elements should be added to the end of the CommandList

#### `Clear` Method

Removes all elements from the CommandList.

```csharp
public override void Clear();
```

**Implements**

IList.Clear

#### `Insert` Method

Inserts an element into the CommandList at the specified index.

```csharp
public override void Insert( int index , object value );
```

**Parameters**

- **index** — The zero-based index at which value should be inserted.
- **value** — The Object to insert.

**Implements**

IList.Insert

#### `InsertRange` Method

Inserts the elements of a collection into the CommandList at the specified index.

```csharp
public override void InsertRange( int index , ICollection c );
```

**Parameters**

- **index** — The zero-based index at which the new elements should be inserted.
- **c** — The ICollection whose elements should be inserted into the ArrayList.

#### `Remove` Method

Removes the first occurrence of a specific object from the CommandList.

```csharp
public override void Remove( object obj );
```

**Parameters**

- **obj** — The Object to remove from the CommandList.

**Implements**

IList.Remove

#### `RemoveAt` Method

Removes the element at the specified index of the CommandList.

```csharp
public override void RemoveAt( int index );
```

**Parameters**

- **index** — The zero-based index of the element to remove.

**Implements**

IList.RemoveAt

#### `RemoveRange` Method

Removes a range of elements from the CommandList.

```csharp
public override void RemoveRange( int index , int count );
```

**Parameters**

- **index** — The zero-based starting index of the range of elements to remove.
- **count** — The number of elements to remove.

#### `Reverse` Method ()

Reverses the order of the elements in the CommandList or a portion of it.

```csharp
public override void Reverse();
```

#### `Reverse` Method (Int32, Int32)

Reverses the order of the elements in the CommandList or a portion of it.

```csharp
public override void Reverse( int index , int count );
```

**Parameters**

- **index** — The zero-based starting index of the range to reverse.
- **count** — The number of elements in the range to reverse.

#### `SetRange` Method

Copies the elements of a collection over a range of elements in the CommandList.

```csharp
public override void SetRange( int index , ICollection c );
```

**Parameters**

- **index** — The zero-based ArrayList index at which to start copying the elements of c.
- **c** — The ICollection whose elements to copy to the CommandList.

#### `Sort` Method ()

Sorts the elements in the CommandList or a portion of it.

```csharp
public override void Sort();
```

#### `Sort` Method (IComparer)

Sorts the elements in the CommandList or a portion of it.

```csharp
public override void Sort( IComparer comparer );
```

**Parameters**

- **comparer** — The IComparer implementation to use when comparing elements.

#### `Sort` Method (Int32, Int32, IComparer)

Sorts the elements in the CommandList or a portion of it.

```csharp
public override void Sort( int index , int count , IComparer comparer );
```

**Parameters**

- **index** — The zero-based starting index of the range to sort.
- **count** — The length of the range to sort.
- **comparer** — The IComparer implementation to use when comparing elements.
