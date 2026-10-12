---
title: Aveva.Pdms.Database.DbElementType Class
namespace: Aveva.Pdms.Database
assembly: Aveva.Pdms.Database
kind: Class
source: Aveva.Pdms.Database
---

# Aveva.Pdms.Database.DbElementType Class

> The class has two purposes: i) Instances of the class are used to identify and pass around Element types ii) The class can be used to get meta data about an attribute. e.g. type, size, Name, pseudo or not, etc Return meta data about an element type, e,g. allowed members, name, Primary or not, etc. The class is valid for system types and UDETS. Object instances are created for all system element types. These instances are in DbElementTypeInstance class All methods that pass an Element Type should pass a DbElemenType object rather than a string that represents the attribute

## Syntax

```csharp
public abstract class DbElementType : IComparable , IMessage
```

## Inheritance

`System.Object` → `Aveva.Pdms.Database.DbElementType`

## Thread Safety

Public static ( Shared in Visual Basic) members of this type are
safe for multithreaded operations. Instance members are not guaranteed to be
thread-safe.

## Requirements

Namespace:
Aveva.Pdms.Database
Assembly: Aveva.Pdms.Database (in Aveva.Pdms.Database.dll)

## Properties

#### `BaseType` Property

Return Base type. This will be different for UDETs. Otherwise it will return this

```csharp
public abstract DbElementType BaseType {get;}
```

#### `Description` Property

Description for this Element type

```csharp
public abstract string Description {get;}
```

#### `HardType` Property

Return hard type- This will be different if a UDET or if a Dabacon 'softtype' was used in the definition. Otherwise it will return this

```csharp
public abstract DbElementType HardType {get;}
```

#### `IsPrimary` Property

True, if this Element type is primary

```csharp
public abstract bool IsPrimary {get;}
```

#### `IsPrimaryList` Property

True, if this Element type has a primary list

```csharp
public abstract bool IsPrimaryList {get;}
```

#### `IsPseudo` Property

True, if this Element type is pseudo

```csharp
public abstract bool IsPseudo {get;}
```

#### `IsSynonym` Property

```csharp
public bool IsSynonym {get;}
```

#### `IsValid` Property

True, if this Element type is valid

```csharp
public abstract bool IsValid {get;}
```

#### `IsWorld` Property

True, if this Element type is a World type

```csharp
public abstract bool IsWorld {get;}
```

#### `Name` Property

Name of this Element type

```csharp
public abstract string Name {get;}
```

#### `ShortName` Property

Short name of this Element type

```csharp
public abstract string ShortName {get;}
```

#### `ValidConnections` Property

True, if this Element type has valid connections

```csharp
public abstract bool ValidConnections {get;}
```

#### `Visible` Property

True, if this Element type is visible

```csharp
public abstract bool Visible {get;}
```

## Methods

#### `AscendantTypes` Method

Return list of possible ascendant Element types.

```csharp
public abstract DbElementType[] AscendantTypes();
```

**Return Value**

Array of Element types

#### `CompareTo` Method

Compare Element type with a generic object.

```csharp
public abstract int CompareTo( object obj );
```

**Parameters**

- **obj** — Object to compare with

**Return Value**

0, if object is "equal"; -1, if object is "less than"; 1, if object is "greater than"

**Implements**

IComparable.CompareTo

#### `DatabaseTypes` Method

Return list of database types which can contain Elements of this type.

```csharp
public abstract int[] DatabaseTypes();
```

**Return Value**

Array of Database types

**Remarks**

Should this method return DbType[]?

#### `DescendantTypes` Method

Return list of possible descendant types.

```csharp
public abstract DbElementType[] DescendantTypes();
```

**Return Value**

Array of Element types

#### `Equals` Method

Test for equality with a generic object.

```csharp
public abstract bool Equals( object type );
```

**Parameters**

- **type** — Object to test

**Return Value**

True, if object is equal

#### `GetAllElementTypes` Method

List of all element types

```csharp
public static DbElementType[] GetAllElementTypes();
```

**Return Value**

An array of all element types

#### `GetAllUdas` Method

```csharp
public DbAttribute[] GetAllUdas();
```

#### `GetAsString` Method (DbNounField)

```csharp
public string GetAsString( DbNounField field );
```

#### `GetAsString` Method (DbNounField, Int32)

```csharp
public string GetAsString( DbNounField field , int arrayindex );
```

#### `GetAsString` Method (DbNounField, String)

```csharp
public string GetAsString( DbNounField field , string arrayseparator );
```

#### `GetAsString` Method (DbNounSpecialField)

```csharp
public string GetAsString( DbNounSpecialField field );
```

#### `GetAsString` Method (DbNounSpecialField, Int32)

```csharp
public string GetAsString( DbNounSpecialField field , int arrayindex );
```

#### `GetAsString` Method (DbNounSpecialField, Int32, Int32, String)

```csharp
public string GetAsString( DbNounSpecialField field , int arrayindex , int dbrestriction , string itemseparator );
```

#### `GetAsString` Method (DbNounSpecialField, String)

```csharp
public string GetAsString( DbNounSpecialField field , string arrayseparator );
```

#### `GetAsString` Method (DbNounSpecialField, String, Int32, String)

```csharp
public string GetAsString( DbNounSpecialField field , string arrayseparator , int dbrestriction , string itemseparator );
```

#### `GetAsStringArray` Method (DbNounField)

Gets the value of any field as an array of strings; note this may be of length 0

```csharp
public string[] GetAsStringArray( DbNounField field );
```

**Parameters**

- **field** — Noun field

#### `GetAsStringArray` Method (DbNounSpecialField, Int32, String)

```csharp
public string[] GetAsStringArray( DbNounSpecialField field , int dbrestriction , string itemseparator );
```

#### `GetBool` Method

Get boolean metadata for Element type.

```csharp
public abstract bool GetBool( DbNounField field );
```

**Parameters**

- **field** — Field

**Return Value**

Boolean value

#### `GetElementType` Method (Int32)

Creates and returns a new Element Type

```csharp
public static DbElementType GetElementType( int hash );
```

**Parameters**

- **hash** — Hash code for new Element Type

**Return Value**

Element Type

#### `GetElementType` Method (String)

Creates and returns a new Element Type

```csharp
public static DbElementType GetElementType( string name );
```

**Parameters**

- **name** — Name for new Element Type

**Return Value**

Element Type

#### `GetElementTypeArray` Method

Get array of Element types metadata for Element type.

```csharp
public abstract DbElementType[] GetElementTypeArray( DbNounField field );
```

**Parameters**

- **field** — Field

**Return Value**

Array of Element types

#### `GetHashCode` Method

Get unique integer identifier for Element type.

```csharp
public abstract int GetHashCode();
```

**Return Value**

Hash code

#### `GetInteger` Method

Get integer metadata for Element type

```csharp
public abstract int GetInteger( DbNounField field );
```

**Parameters**

- **field** — Field

**Return Value**

Integer value

#### `GetIntegerArray` Method

Get integer array metadata for the given noun field.

```csharp
public abstract int[] GetIntegerArray( DbNounField field );
```

**Parameters**

- **field** — Noun field

**Return Value**

Integer array value

#### `GetString` Method

Get string metadata for Element type.

```csharp
public abstract string GetString( DbNounField field );
```

**Parameters**

- **field** — Field

**Return Value**

Text value

#### `getUDAs` Method

```csharp
public abstract DbAttribute[] getUDAs();
```

#### `IsAttributeValid` Method

Check whether a given attribute is valid for this Element type.

```csharp
public abstract bool IsAttributeValid( DbAttribute attname );
```

**Parameters**

- **attname** — Attribute to check

**Return Value**

True, if the Attribute is valid

#### `MemberTypes` Method

Return list of allowed member types for Elements of this type.

```csharp
public abstract DbElementType[] MemberTypes();
```

**Return Value**

Array of Element types

#### `NounFieldType` Method

The type of a noun field

```csharp
public static DbFieldType NounFieldType( DbNounField field );
```

**Parameters**

- **field** — A noun field

**Return Value**

The type of the noun field

#### `OwnerTypes` Method

Return list of allowed owner types for Elements of this type.

```csharp
public abstract DbElementType[] OwnerTypes();
```

**Return Value**

Array of Element types

#### `PassObjectToCPP` Method

Pass object through to unmanaged C++. AVEVA USE ONLY.

```csharp
public abstract void PassObjectToCPP( int pos , PdmsMessage message );
```

**Parameters**

- **pos** — Position index
- **message** — Associated message

**Implements**

IMessage.PassObjectToCPP

#### `ReferenceTypes` Method

Return list of allowed reference types for Attribute, given this Element type.

```csharp
public abstract DbElementType[] ReferenceTypes( DbAttribute attname );
```

**Parameters**

- **attname** — Attribute to query

**Return Value**

Array of Element types

#### `SystemAttributes` Method

Return system attributes and UDAs on this Element type.

```csharp
public abstract DbAttribute[] SystemAttributes();
```

**Return Value**

Array of Attributes

#### `VisibleSystemAttributes` Method

```csharp
public DbAttribute[] VisibleSystemAttributes();
```

## Operators

#### `Equality` Operator

Element type equality operator.

```csharp
public static bool operator ==( DbElementType left , DbElementType right );
```

**Parameters**

- **left** — Left-hand Element type
- **right** — Right-hand Element type

**Return Value**

True, if Element types are equal

#### `Inequality` Operator

Element type inequality operator.

```csharp
public static bool operator !=( DbElementType left , DbElementType right );
```

**Parameters**

- **left** — Left-hand Element type
- **right** — Right-hand Element type

**Return Value**

True, if Element types are not equal
