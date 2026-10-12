---
title: Aveva.Pdms.Database.DbElementTypeList Class
namespace: Aveva.Pdms.Database
assembly: Aveva.Pdms.Database
kind: Class
source: Aveva.Pdms.Database
---

# Aveva.Pdms.Database.DbElementTypeList Class

> Class to define a list of DbElementTypes; usually for documentation purposes

## Syntax

```csharp
public class DbElementTypeList : IEnumerable
```

## Inheritance

`System.Object` → `Aveva.Pdms.Database.DbElementTypeList`

## Thread Safety

Public static ( Shared in Visual Basic) members of this type are
safe for multithreaded operations. Instance members are not guaranteed to be
thread-safe.

## Requirements

Namespace:
Aveva.Pdms.Database
Assembly: Aveva.Pdms.Database (in Aveva.Pdms.Database.dll)

## Constructors

#### `DbElementTypeList` Constructor

Initializes a new instance of the DbElementTypeList class.

```csharp
public DbElementTypeList();
```

## Properties

#### `Include_Invisible` Property

Whether to include invisible DbElementTypes in all AddAll and RemoveAll opeations (default FALSE) NB: The setting does *not* modify the existing list - it is used as a filter on all *subsequent* AddAll and RemoveAll operations. The setting does not apply to Add or Remove operations.

```csharp
public bool Include_Invisible {get; set;}
```

#### `Include_Synonyms` Property

Whether to include synonyms in all AddAll and RemoveAll opeations (default FALSE) NB: The setting does *not* modify the existing list - it is used as a filter on all *subsequent* AddAll and RemoveAll operations. The setting does not apply to Add or Remove operations.

```csharp
public bool Include_Synonyms {get; set;}
```

## Methods

#### `Add` Method (DbElementType)

Add a specific DbElementType

```csharp
public void Add( DbElementType att );
```

**Parameters**

- **att** — The DbElementType to be added

#### `Add` Method (DbElementTypeList)

Append an existing DbElementTypeList

```csharp
public void Add( DbElementTypeList addlist );
```

**Parameters**

- **addlist** — DbElementTypeList to be appended

#### `AddAll` Method ()

Add all DbElementTypes to the DbElementTypeList

```csharp
public void AddAll();
```

#### `AddAll` Method (DbElementTypeList, DbNounField, Boolean)

```csharp
public void AddAll( DbElementTypeList domain , DbNounField field , bool boolvalue );
```

#### `AddAll` Method (DbElementTypeList, DbNounField, Boolean, Boolean)

```csharp
public void AddAll( DbElementTypeList domain , DbNounField field , bool boolvalue , bool match );
```

#### `AddAll` Method (DbElementTypeList, DbNounField, Int32)

```csharp
public void AddAll( DbElementTypeList domain , DbNounField field , int intvalue );
```

#### `AddAll` Method (DbElementTypeList, DbNounField, Int32, Boolean)

```csharp
public void AddAll( DbElementTypeList domain , DbNounField field , int intvalue , bool match );
```

#### `AddAll` Method (DbElementTypeList, DbNounField, String)

```csharp
public void AddAll( DbElementTypeList domain , DbNounField field , string strvalue );
```

#### `AddAll` Method (DbElementTypeList, DbNounField, String, Boolean)

```csharp
public void AddAll( DbElementTypeList domain , DbNounField field , string strvalue , bool match );
```

#### `AddAll` Method (DbNounField, Boolean)

Add all DbElementTypes with a specified value of a given logical field

```csharp
public void AddAll( DbNounField field , bool boolvalue );
```

**Parameters**

- **field** — The logical field
- **boolvalue** — The required value of the logical field

#### `AddAll` Method (DbNounField, Boolean, Boolean)

```csharp
public void AddAll( DbNounField field , bool boolvalue , bool match );
```

#### `AddAll` Method (DbNounField, Int32)

Add all DbElementTypes with a specified value of a given integer field NB: Also works for integer array fields; a DbElementType is added if any array element matches the required value

```csharp
public void AddAll( DbNounField field , int intvalue );
```

**Parameters**

- **field** — The integer field
- **intvalue** — The required value of the integer field

#### `AddAll` Method (DbNounField, Int32, Boolean)

```csharp
public void AddAll( DbNounField field , int intvalue , bool match );
```

#### `AddAll` Method (DbNounField, String)

Add all DbElementTypes with a specified value of a given text field NB: This may be used for ANY field; the GetAsString value being used for comparison

```csharp
public void AddAll( DbNounField field , string strvalue );
```

**Parameters**

- **field** — The field
- **strvalue** — The required value of the field

#### `AddAll` Method (DbNounField, String, Boolean)

```csharp
public void AddAll( DbNounField field , string strvalue , bool match );
```

#### `Count` Method

Returns the number of element types currently in the DbElementTypeList

```csharp
public int Count();
```

#### `GetEnumerator` Method

```csharp
public IEnumerator GetEnumerator();
```

**Implements**

IEnumerable.GetEnumerator

#### `MaximumFieldWidth` Method (DbNounField)

Returns the maximum width of a field over a DbElementTypeList (useful when setting column widths)

```csharp
public int MaximumFieldWidth( DbNounField field );
```

**Parameters**

- **field** — A field

#### `MaximumFieldWidth` Method (DbNounField, DbFieldFormat)

Returns the maximum width of a formatted field over a DbElementTypeList (useful when setting column widths)

```csharp
public int MaximumFieldWidth( DbNounField field , DbFieldFormat format );
```

**Parameters**

- **field** — A field
- **format** — A field format

#### `MaximumFieldWidth` Method (DbNounSpecialField)

Returns the maximum width of a special field over a DbElementTypeList (useful when setting column widths)

```csharp
public int MaximumFieldWidth( DbNounSpecialField field );
```

**Parameters**

- **field** — A special field

#### `Remove` Method (DbElementType)

Remove all instances of a specific DbElementType from the DbElementTypeList

```csharp
public void Remove( DbElementType noun );
```

**Parameters**

- **noun** — 

#### `Remove` Method (DbElementTypeList)

Remove all instances of DbElementTypes in an existing DbElementTypeList

```csharp
public void Remove( DbElementTypeList remlist );
```

**Parameters**

- **remlist** — DbElementTypeList to be removed

#### `RemoveAll` Method ()

Remove all DbElementTypes from the DbElementTypeList

```csharp
public void RemoveAll();
```

#### `RemoveAll` Method (DbNounField, Boolean)

Remove all DbElementTypes with a specified value of a given logical field

```csharp
public void RemoveAll( DbNounField field , bool boolvalue );
```

**Parameters**

- **field** — The logical field
- **boolvalue** — The required value of the logical field

#### `RemoveAll` Method (DbNounField, Int32)

Remove all DbElementTypes with a specified value of a given integer field NB: Also works for integer array fields; an attribute is removed if any array element matches the required value

```csharp
public void RemoveAll( DbNounField field , int intvalue );
```

**Parameters**

- **field** — The integer field
- **intvalue** — The required value of the integer field

#### `RemoveAll` Method (DbNounField, String)

Remove all DbElementTypes with a specified value of a given text field NB: This may be used for ANY field; the GetAsString value being used for comparison

```csharp
public void RemoveAll( DbNounField field , string strvalue );
```

**Parameters**

- **field** — The field
- **strvalue** — The required value of the field

#### `SortList` Method (DbElementTypeComparer)

Sort DbElementTypeList on a predefined DbElementTypeComparer: this allows for more complex sorts with subkeys

```csharp
public void SortList( DbElementTypeComparer sorter );
```

**Parameters**

- **sorter** — 

#### `SortList` Method (DbNounField)

Sort DbElementTypeList on a single field

```csharp
public void SortList( DbNounField field );
```

**Parameters**

- **field** — Field to use as sort key

#### `SortList` Method (DbNounField, DbNounField)

Sort DbElementTypeList on a field, using a second field to determine order when values of first are equal

```csharp
public void SortList( DbNounField field , DbNounField second_field );
```

**Parameters**

- **field** — Field to use as primary sort key
- **second_field** — Field to use as secondary sort key

#### `SortList` Method (DbNounField, Boolean)

Sort DbElementTypeList on a single field

```csharp
public void SortList( DbNounField field , bool reversed );
```

**Parameters**

- **field** — Field to use as sort key
- **reversed** — Reverse sort order; ie false for ascending, true for descending

#### `SortList` Method (DbNounField, Boolean, DbNounField, Boolean)

Sort DbElementTypeList on a field, using a second field to determine order when values of first are equal

```csharp
public void SortList( DbNounField field , bool reversed , DbNounField second_field , bool second_reversed );
```

**Parameters**

- **field** — Field to use as primary sort key
- **reversed** — Reverse sort order on primary key; ie false for ascending, true for descending
- **second_field** — Field to use as secondary sort key
- **second_reversed** — Reverse sort order on secondary key; ie false for ascending, true for descending
