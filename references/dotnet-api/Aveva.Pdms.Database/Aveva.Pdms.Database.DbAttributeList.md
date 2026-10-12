---
title: Aveva.Pdms.Database.DbAttributeList Class
namespace: Aveva.Pdms.Database
assembly: Aveva.Pdms.Database
kind: Class
source: Aveva.Pdms.Database
---

# Aveva.Pdms.Database.DbAttributeList Class

> Class to define a list of attributes; usually for documentation purposes

## Syntax

```csharp
public class DbAttributeList : IEnumerable
```

## Inheritance

`System.Object` → `Aveva.Pdms.Database.DbAttributeList`

## Thread Safety

Public static ( Shared in Visual Basic) members of this type are
safe for multithreaded operations. Instance members are not guaranteed to be
thread-safe.

## Requirements

Namespace:
Aveva.Pdms.Database
Assembly: Aveva.Pdms.Database (in Aveva.Pdms.Database.dll)

## Constructors

#### `DbAttributeList` Constructor

Initializes a new instance of the DbAttributeList class.

```csharp
public DbAttributeList();
```

## Properties

#### `Include_Invisible` Property

Whether to include invisible attributes in all AddAll and RemoveAll opeations (default FALSE) NB: The setting does *not* modify the existing list - it is used as a filter on all *subsequent* AddAll and RemoveAll operations. The setting does not apply to Add or Remove operations.

```csharp
public bool Include_Invisible {get; set;}
```

#### `Include_Synonyms` Property

Whether to include synonyms in all AddAll and RemoveAll opeations (default FALSE) NB: The setting does *not* modify the existing list - it is used as a filter on all *subsequent* AddAll and RemoveAll operations. The setting does not apply to Add or Remove operations.

```csharp
public bool Include_Synonyms {get; set;}
```

#### `Include_System` Property

Whether to include system (ie non uda) attributes in all AddAll and RemoveAll opeations (default TRUE) NB: The setting does *not* modify the existing list - it is used as a filter on all *subsequent* AddAll and RemoveAll operations. The setting does not apply to Add or Remove operations.

```csharp
public bool Include_System {get; set;}
```

#### `Include_UDAs` Property

Whether to include udas in all AddAll and RemoveAll operations (default TRUE) NB: The setting does *not* modify the existing list - it is used as a filter on all *subsequent* AddAll and RemoveAll operations. The setting does not apply to Add or Remove operations.

```csharp
public bool Include_UDAs {get; set;}
```

## Methods

#### `Add` Method (DbAttribute)

Add a specific attribute

```csharp
public void Add( DbAttribute att );
```

**Parameters**

- **att** — The attribute to be added

#### `Add` Method (DbAttributeList)

Append an existing AttributeList

```csharp
public void Add( DbAttributeList addlist );
```

**Parameters**

- **addlist** — AttributeList to be appended

#### `AddAll` Method ()

Add all attributes to the AttributeList NB: The Include_UDA and Include_System properties may be used to specify whether or not UDAs/System attributes are included in 'all'

```csharp
public void AddAll();
```

#### `AddAll` Method (DbAttributeField, Boolean)

Add all attributes with a specified value of a given logical field NB: The Include_UDA and Include_System properties may be used to specify whether or not UDAs/System attributes are included in 'all'

```csharp
public void AddAll( DbAttributeField field , bool boolvalue );
```

**Parameters**

- **field** — The logical field
- **boolvalue** — The required value of the logical field

#### `AddAll` Method (DbAttributeField, Boolean, Boolean)

```csharp
public void AddAll( DbAttributeField field , bool boolvalue , bool match );
```

#### `AddAll` Method (DbAttributeField, Int32)

Add all attributes with a specified value of a given integer field NB: Also works for integer array fields; an attribute is added if any array element matches the required value NB: The Include_UDA and Include_System properties may be used to specify whether or not UDAs/System attributes are included in 'all'

```csharp
public void AddAll( DbAttributeField field , int intvalue );
```

**Parameters**

- **field** — The integer field
- **intvalue** — The required value of the integer field

#### `AddAll` Method (DbAttributeField, Int32, Boolean)

```csharp
public void AddAll( DbAttributeField field , int intvalue , bool match );
```

#### `AddAll` Method (DbAttributeField, String)

Add all attributes with a specified value of a given text field NB: This may be used for ANY field; the GetAsString value being used for comparison NB: The Include_UDA and Include_System properties may be used to specify whether or not UDAs/System attributes are included in 'all'

```csharp
public void AddAll( DbAttributeField field , string strvalue );
```

**Parameters**

- **field** — The field
- **strvalue** — The required value of the field

#### `AddAll` Method (DbAttributeField, String, Boolean)

```csharp
public void AddAll( DbAttributeField field , string strvalue , bool match );
```

#### `AddAll` Method (DbAttributeList, DbAttributeField, Boolean)

```csharp
public void AddAll( DbAttributeList domain , DbAttributeField field , bool boolvalue );
```

#### `AddAll` Method (DbAttributeList, DbAttributeField, Boolean, Boolean)

```csharp
public void AddAll( DbAttributeList domain , DbAttributeField field , bool boolvalue , bool match );
```

#### `AddAll` Method (DbAttributeList, DbAttributeField, Int32)

```csharp
public void AddAll( DbAttributeList domain , DbAttributeField field , int intvalue );
```

#### `AddAll` Method (DbAttributeList, DbAttributeField, Int32, Boolean)

```csharp
public void AddAll( DbAttributeList domain , DbAttributeField field , int intvalue , bool match );
```

#### `AddAll` Method (DbAttributeList, DbAttributeField, String)

```csharp
public void AddAll( DbAttributeList domain , DbAttributeField field , string strvalue );
```

#### `AddAll` Method (DbAttributeList, DbAttributeField, String, Boolean)

```csharp
public void AddAll( DbAttributeList domain , DbAttributeField field , string strvalue , bool match );
```

#### `Count` Method

Returns the number of attributes currently in the DbAttributeList

```csharp
public int Count();
```

#### `GetEnumerator` Method

```csharp
public IEnumerator GetEnumerator();
```

**Implements**

IEnumerable.GetEnumerator

#### `MaximumFieldWidth` Method (DbAttributeField)

Returns the maximum width of a field over a DbAttributeList (useful when setting column widths)

```csharp
public int MaximumFieldWidth( DbAttributeField field );
```

**Parameters**

- **field** — A field

#### `MaximumFieldWidth` Method (DbAttributeField, DbFieldFormat)

Returns the maximum width of a formatted field over a DbAttributeList (useful when setting column widths)

```csharp
public int MaximumFieldWidth( DbAttributeField field , DbFieldFormat format );
```

**Parameters**

- **field** — A field
- **format** — A field format

#### `MaximumFieldWidth` Method (DbAttributeSpecialField)

Returns the maximum width of a special field over a DbAttributeList (useful when setting column widths)

```csharp
public int MaximumFieldWidth( DbAttributeSpecialField field );
```

**Parameters**

- **field** — A special field

#### `Remove` Method (DbAttribute)

Remove all instances of a specific attribute from the AttributeList

```csharp
public void Remove( DbAttribute att );
```

**Parameters**

- **att** — The attribute to be removed

#### `Remove` Method (DbAttributeList)

Remove all instances of attributes in an existing AttributeList

```csharp
public void Remove( DbAttributeList remlist );
```

**Parameters**

- **remlist** — AttributeList to be removed

#### `RemoveAll` Method ()

Remove all attributes from the AttributeList NB: The Include_UDA and Include_System properties may be used to specify whether or not UDAs/System attributes are included in 'all'

```csharp
public void RemoveAll();
```

#### `RemoveAll` Method (DbAttributeField, Boolean)

Remove all attributes with a specified value of a given logical field NB: The Include_UDA and Include_System properties may be used to specify whether or not UDAs/System attributes are included in 'all'

```csharp
public void RemoveAll( DbAttributeField field , bool boolvalue );
```

**Parameters**

- **field** — The logical field
- **boolvalue** — The required value of the logical field

#### `RemoveAll` Method (DbAttributeField, Int32)

Remove all attributes with a specified value of a given integer field NB: Also works for integer array fields; an attribute is removed if any array element matches the required value NB: The Include_UDA and Include_System properties may be used to specify whether or not UDAs/System attributes are included in 'all'

```csharp
public void RemoveAll( DbAttributeField field , int intvalue );
```

**Parameters**

- **field** — The integer field
- **intvalue** — The required value of the integer field

#### `RemoveAll` Method (DbAttributeField, String)

Remove all attributes with a specified value of a given text field NB: This may be used for ANY field; the GetAsString value being used for comparison NB: The Include_UDA and Include_System properties may be used to specify whether or not UDAs/System attributes are included in 'all'

```csharp
public void RemoveAll( DbAttributeField field , string strvalue );
```

**Parameters**

- **field** — The field
- **strvalue** — The required value of the field

#### `SortList` Method (DbAttributeComparer)

Sort AttributeList on a predefined DbAttributeComparer: this allows for more complex sorts with subkeys

```csharp
public void SortList( DbAttributeComparer sorter );
```

**Parameters**

- **sorter** — 

#### `SortList` Method (DbAttributeField)

Sort AttributeList on a single field

```csharp
public void SortList( DbAttributeField field );
```

**Parameters**

- **field** — Field to use as sort key

#### `SortList` Method (DbAttributeField, DbAttributeField)

Sort AttributeList on a field, using a second field to determine order when values of first are equal

```csharp
public void SortList( DbAttributeField field , DbAttributeField second_field );
```

**Parameters**

- **field** — Field to use as primary sort key
- **second_field** — Field to use as secondary sort key

#### `SortList` Method (DbAttributeField, Boolean)

Sort AttributeList on a single field

```csharp
public void SortList( DbAttributeField field , bool reversed );
```

**Parameters**

- **field** — Field to use as sort key
- **reversed** — Reverse sort order; ie false for ascending, true for descending

#### `SortList` Method (DbAttributeField, Boolean, DbAttributeField, Boolean)

Sort AttributeList on a field, using a second field to determine order when values of first are equal

```csharp
public void SortList( DbAttributeField field , bool reversed , DbAttributeField second_field , bool second_reversed );
```

**Parameters**

- **field** — Field to use as primary sort key
- **reversed** — Reverse sort order on primary key; ie false for ascending, true for descending
- **second_field** — Field to use as secondary sort key
- **second_reversed** — Reverse sort order on secondary key; ie false for ascending, true for descending
