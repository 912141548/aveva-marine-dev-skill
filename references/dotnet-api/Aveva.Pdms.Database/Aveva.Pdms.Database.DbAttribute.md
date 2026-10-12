---
title: Aveva.Pdms.Database.DbAttribute Class
namespace: Aveva.Pdms.Database
assembly: Aveva.Pdms.Database
kind: Class
source: Aveva.Pdms.Database
---

# Aveva.Pdms.Database.DbAttribute Class

> The class has two purposes: i) Instances of the class are used to identify and pass around attributes ii) The class can be used to get meta data about an attribute. e.g. type, size, Name, pseudo or not, etc The class is valid for system attributes and UDAS. Object instances are created for all system atttributes. These instances are in DbAttributeInstance class All methods that pass in an attribute should pass a DbAttribute object rather than a string that represents the attribute

## Syntax

```csharp
public abstract class DbAttribute : IComparable , IMessage
```

## Inheritance

`System.Object` → `Aveva.Pdms.Database.DbAttribute`

## Thread Safety

Public static ( Shared in Visual Basic) members of this type are
safe for multithreaded operations. Instance members are not guaranteed to be
thread-safe.

## Requirements

Namespace:
Aveva.Pdms.Database
Assembly: Aveva.Pdms.Database (in Aveva.Pdms.Database.dll)

## Properties

#### `Category` Property

Attribute category used for display

```csharp
public abstract string Category {get;}
```

#### `Description` Property

Description of this Attribute

```csharp
public abstract string Description {get;}
```

#### `HashValue` Property

Hash value for this Attribute

```csharp
public abstract int HashValue {get;}
```

#### `Hyperlink` Property

True if attribute represents a hyperlink

```csharp
public abstract bool Hyperlink {get;}
```

#### `IsArray` Property

True, if this Attribute is an array

```csharp
public abstract bool IsArray {get;}
```

#### `IsPseudo` Property

True, if this Attribute is a pseudo-attribute

```csharp
public abstract bool IsPseudo {get;}
```

#### `IsSynonym` Property

```csharp
public bool IsSynonym {get;}
```

#### `IsUDA` Property

True, if this Attribute is a User-Defined Attribute

```csharp
public abstract bool IsUDA {get;}
```

#### `MaximumSize` Property

Maximum size of this Attribute

```csharp
public abstract int MaximumSize {get;}
```

#### `Name` Property

Name of this Attribute. This is always reinputable as valid syntax to PML

```csharp
public abstract string Name {get;}
```

#### `QueryText` Property

Query text associated with this Attribute

```csharp
public abstract string QueryText {get;}
```

#### `ShortName` Property

Short name for this Attribute

```csharp
public abstract string ShortName {get;}
```

#### `Type` Property

Type of this Attribute

```csharp
public abstract DbAttributeType Type {get;}
```

#### `Units` Property

Units of this Attribute

```csharp
public abstract DbAttributeUnit Units {get;}
```

## Methods

#### `AllowedIntRanges` Method

Allowed range(s) for an integer UDA

```csharp
public abstract int[] AllowedIntRanges( DbElementType type );
```

**Parameters**

- **type** — Applicable Element type

**Return Value**

List of ranges

#### `AllowedRanges` Method

Allowed range(s) for a real UDA

```csharp
public abstract double[] AllowedRanges( DbElementType type );
```

**Parameters**

- **type** — Applicable Element type

**Return Value**

List of ranges

#### `AllowedValues` Method

Allowed values for a text UDA

```csharp
public abstract string[] AllowedValues( DbElementType type );
```

**Parameters**

- **type** — Applicable Element type

**Return Value**

List of allowed values

#### `AttributeFieldType` Method

The type of an attribute field

```csharp
public static DbFieldType AttributeFieldType( DbAttributeField field );
```

**Parameters**

- **field** — An attribute field

**Return Value**

The type of the attribute field

#### `CompareTo` Method

Compare Attribute with generic object.

```csharp
public abstract int CompareTo( object obj );
```

**Parameters**

- **obj** — Object to compare with

**Implements**

IComparable.CompareTo

#### `Equals` Method

Test equality to Attribute.

```csharp
public abstract bool Equals( object type );
```

**Parameters**

- **type** — Object to test for equality

**Return Value**

True if object is equal to Attribute; otherwise False

#### `GetAllAttributes` Method

List of all attributes

```csharp
public static DbAttribute[] GetAllAttributes();
```

**Return Value**

An array of all attributes

#### `GetAsString` Method (DbAttributeField)

Get the value of any attribute field as a string; array valued fields will be returned as the elements concatenated together separated by commas

```csharp
public string GetAsString( DbAttributeField field );
```

**Parameters**

- **field** — Any atribute field

**Return Value**

Field value as a string

#### `GetAsString` Method (DbAttributeField, Int32)

Gets the value of any element of an attribute field as a string; for an array valued field the (zero based) array index is specified; this must be '0' for a scalar field

```csharp
public string GetAsString( DbAttributeField field , int arrayindex );
```

**Parameters**

- **field** — Any attribute field
- **arrayindex** — Array index (Zero based)

**Return Value**

Value of the element of the attribute field as a string

#### `GetAsString` Method (DbAttributeField, String)

Get the value of any attribute field as a string; array valued fields will be returned as the elements concatenated together separated by the specified array separator string

```csharp
public string GetAsString( DbAttributeField field , string arrayseparator );
```

**Parameters**

- **field** — Any attribute field
- **arrayseparator** — String to use to separate array elements

**Return Value**

Field value as a string

#### `GetAsString` Method (DbAttributeSpecialField)

Get the value of any attribute special field as a string; array valued fields will be returned as the elements concatenated together separated by commas

```csharp
public string GetAsString( DbAttributeSpecialField field );
```

**Parameters**

- **field** — Any atribute special field

**Return Value**

Special Field value as a string

#### `GetAsString` Method (DbAttributeSpecialField, Int32)

Gets the value of any element of an attribute special field as a string; for an array valued field the (zero based) array index is specified; this must be '0' for a scalar field

```csharp
public string GetAsString( DbAttributeSpecialField field , int arrayindex );
```

**Parameters**

- **field** — Any attribute special field
- **arrayindex** — Array index (Zero based)

**Return Value**

Value of the element of the attribute special field as a string

#### `GetAsString` Method (DbAttributeSpecialField, String)

Get the value of any attribute special field as a string; array valued fields will be returned as the elements concatenated together separated by the specified array separator string

```csharp
public string GetAsString( DbAttributeSpecialField field , string arrayseparator );
```

**Parameters**

- **field** — Any attribute special field
- **arrayseparator** — String to use to separate array elements

**Return Value**

Special Field value as a string

#### `GetAsStringArray` Method (DbAttributeField)

Get the value of any attribute field as an array of strings

```csharp
public string[] GetAsStringArray( DbAttributeField field );
```

**Parameters**

- **field** — Any attribute field

**Return Value**

Array of attribute field values as strings

#### `GetAsStringArray` Method (DbAttributeSpecialField)

Get the value of any attribute special field as an array of strings

```csharp
public string[] GetAsStringArray( DbAttributeSpecialField field );
```

**Parameters**

- **field** — Any attribute special field

**Return Value**

Array of attribute field values as strings

#### `GetBool` Method

Get boolean value for the given Attribute field.

```csharp
public abstract bool GetBool( DbAttributeField field );
```

**Parameters**

- **field** — Attribute field

**Return Value**

Boolean value

#### `GetDbAttribute` Method (Int32)

Create and return a new Attribute instance.

```csharp
public static DbAttribute GetDbAttribute( int hashValue );
```

**Parameters**

- **hashValue** — Hash value of new Attribute

**Return Value**

New Attribute

#### `GetDbAttribute` Method (String)

Create and return a new Attribute instance.

```csharp
public static DbAttribute GetDbAttribute( string name );
```

**Parameters**

- **name** — Name of new Attribute

**Return Value**

New Attribute

#### `GetHashCode` Method

Return hash code for mapping Attributes, overriding Object.GetHashCode.

```csharp
public abstract int GetHashCode();
```

**Return Value**

Hash code

#### `GetInteger` Method

Get integer value for the given Attribute field.

```csharp
public abstract int GetInteger( DbAttributeField field );
```

**Parameters**

- **field** — Attribute field

**Return Value**

Integer value

#### `GetIntegerArray` Method

Get integer array value for the given Attribute field.

```csharp
public abstract int[] GetIntegerArray( DbAttributeField field );
```

**Parameters**

- **field** — Attribute field

**Return Value**

Integer array value

#### `GetString` Method

Get text value from given field of Attribute.

```csharp
public abstract string GetString( DbAttributeField field );
```

**Parameters**

- **field** — Field of Attribute to query

**Return Value**

Text value

#### `HashValueToString` Method

Convert a hash value to a string

```csharp
public static string HashValueToString( int hashvalue );
```

**Parameters**

- **hashvalue** — Hash value

**Return Value**

string

#### `NoClaim` Method

Query whether it is necessary to claim elements of the given type, in order to change this Attribute.

```csharp
public abstract bool NoClaim( DbElementType elementType );
```

**Parameters**

- **elementType** — Element type

**Return Value**

True, if Attribute change requires claim

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

#### `ToString` Method

Gets the textual representation of this Attribute.

```csharp
public abstract string ToString();
```

**Return Value**

Text

## Operators

#### `Equality` Operator

Test for equality between a pair of Attributes.

```csharp
public static bool operator ==( DbAttribute left , DbAttribute right );
```

**Parameters**

- **left** — First Attribute to test
- **right** — Second Attribute to test

**Return Value**

True, if Attributes are equal

#### `Inequality` Operator

Test for inequality between a pair of Attributes.

```csharp
public static bool operator !=( DbAttribute left , DbAttribute right );
```

**Parameters**

- **left** — First Attribute to test
- **right** — Second Attribute to test

**Return Value**

True, if Attributes are not equal
