---
title: Aveva.Pdms.Database.DbElement Class
namespace: Aveva.Pdms.Database
assembly: Aveva.Pdms.Database
kind: Class
source: Aveva.Pdms.Database
---

# Aveva.Pdms.Database.DbElement Class

> Methods to read and write to the database. These cover element creation, deletion and copy; getting and querying attributes and rules; scanning the DB; evaluating database expressions. Instances of DbElement should be used to identify an element. i.e. methods that take an element should always pass a DbElement rather than a 2 long reference number or the name of the element. Some methods return a 'null' DbElement to denote failure. A 'null' DbElement can only be tested using the 'IsNull' method.

## Syntax

```csharp
public abstract class DbElement : IComparable , IMessage
```

## Inheritance

`System.Object` → `Aveva.Pdms.Database.DbElement`

## Thread Safety

Public static ( Shared in Visual Basic) members of this type are
safe for multithreaded operations. Instance members are not guaranteed to be
thread-safe.

## Requirements

Namespace:
Aveva.Pdms.Database
Assembly: Aveva.Pdms.Database (in Aveva.Pdms.Database.dll)

## Properties

#### `DbType` Property

Get the Database Type associated with the Element.

```csharp
public abstract DbType DbType {get;}
```

#### `IsDeleteable` Property

True if this Element can be deleted.

```csharp
public abstract bool IsDeleteable {get;}
```

#### `IsDeleted` Property

True if the Element has been deleted.

```csharp
public abstract bool IsDeleted {get;}
```

#### `IsHierarchyDeleteable` Property

True if the Element and all its descendants can be deleted together.

```csharp
public abstract bool IsHierarchyDeleteable {get;}
```

#### `IsNull` Property

True if this Element is null.

```csharp
public abstract bool IsNull {get;}
```

#### `IsValid` Property

True if this Element is valid.

```csharp
public abstract bool IsValid {get;}
```

#### `Owner` Property

Owner Element of this Element. If none, returns a null DbElement.

```csharp
public abstract DbElement Owner {get;}
```

#### `Previous` Property

Previous Element in order from this Element. If none, returns a null DbElement.

```csharp
public abstract DbElement Previous {get;}
```

## Methods

#### `AtDefault` Method

Query whether the named Attribute of this Element has default value. If attribute is invalid, method returns false.

```csharp
public abstract bool AtDefault( DbAttribute attributeName );
```

**Parameters**

- **attributeName** — Name of Attribute

**Return Value**

True, if the Element's Attribute is at the default value

#### `ChangeType` Method

Change the type of this Element. Method throws an exception if not allowed.

```csharp
public abstract void ChangeType( DbElementType elementType );
```

**Parameters**

- **elementType** — New Element type

#### `Claim` Method

Claim this Element. Throws an exception if element cannot be claimed

```csharp
public abstract void Claim();
```

#### `ClaimHierarchy` Method

Claim this Element and all its descendants. Throws an exception if all elements cannot be claimed. Even if some elements cannot be claimed, the method will claim what it can.

```csharp
public abstract void ClaimHierarchy();
```

#### `Clone` Method

Return a new instance representing this Element.

```csharp
public abstract DbElement Clone();
```

**Return Value**

Element clone

#### `CompareTo` Method

Compare this Element with general object.

```csharp
public abstract int CompareTo( object obj );
```

**Parameters**

- **obj** — Object to compare

**Return Value**

0, if object is equal; -1 if object is "less than"; 1 if object is "greater than"

**Implements**

IComparable.CompareTo

#### `Copy` Method

Copy attributes from another Element. This method throws an exception if operation fails.

```csharp
public abstract void Copy( DbElement element );
```

**Parameters**

- **element** — Existing Element to copy from

#### `CopyHierarchy` Method

Copy attributes from another Element, and create a copy of Element's descendants. This method throws an exception if operation fails.

```csharp
public abstract void CopyHierarchy( DbElement element , DbCopyOption option );
```

**Parameters**

- **element** — Existing Element to copy from
- **option** — Copy options

#### `CopyLike` Method

Copy only a subset of attributes from another Element, as determined by attribute definitions. Examples of attributes NOT copied are POS/ORI. The list is documented in the 'COPY LIKE' section of the database reference manual. This method throws an exception if operation fails.

```csharp
public abstract void CopyLike( DbElement element );
```

**Parameters**

- **element** — Existing Element to copy from

#### `Create` Method

Create a new Element at given position in this Element's child list. This method throws an exception if operation fails.

```csharp
public abstract DbElement Create( int PositionInList , DbElementType elementType );
```

**Parameters**

- **PositionInList** — Insert position index
- **elementType** — New Element type

**Return Value**

New Element

#### `CreateAfter` Method

Create a new Element after this Element in owner's child list. This method throws an exception if operation fails.

```csharp
public abstract DbElement CreateAfter( DbElementType elementType );
```

**Parameters**

- **elementType** — New Element type

**Return Value**

New Element

#### `CreateBefore` Method

Create a new Element before this Element in owner's child list. This method throws an exception if operation fails.

```csharp
public abstract DbElement CreateBefore( DbElementType elementType );
```

**Parameters**

- **elementType** — New Element type

**Return Value**

New Element

#### `CreateCopyHierarchyAfter` Method

Create copy of an Element hierarchy after this Element in owner's child list. This method throws an exception if operation fails.

```csharp
public abstract DbElement CreateCopyHierarchyAfter( DbElement elementToCopy , DbCopyOption option );
```

**Parameters**

- **elementToCopy** — Existing Element to copy from
- **option** — Copy options

**Return Value**

New Element (root)

#### `CreateCopyHierarchyAfterLast` Method

Create copy of an Element hierarchy at the end of this Element's owner's child list. This method throws an exception if operation fails.

```csharp
public abstract DbElement CreateCopyHierarchyAfterLast( DbElement elementToCopy , DbCopyOption option );
```

**Parameters**

- **elementToCopy** — Existing Element to copy from
- **option** — Copy options

**Return Value**

New Element (root)

#### `CreateCopyHierarchyBefore` Method

Create copy of an Element hierarchy before this Element in owner's child list. This method throws an exception if operation fails.

```csharp
public abstract DbElement CreateCopyHierarchyBefore( DbElement elementToCopy , DbCopyOption option );
```

**Parameters**

- **elementToCopy** — Existing Element to copy from
- **option** — Copy options

**Return Value**

New Element (root)

#### `CreateCopyHierarchyBeforeFirst` Method

Create copy Element hierarchy at the beginning of this Element's owner's child list. This method throws an exception if operation fails.

```csharp
public abstract DbElement CreateCopyHierarchyBeforeFirst( DbElement elementToCopy , DbCopyOption option );
```

**Parameters**

- **elementToCopy** — Existing Element to copy from
- **option** — Copy options

**Return Value**

New Element (root)

#### `CreateFirst` Method

Create new Element at the beginning of this Element's child list. This method throws an exception if operation fails.

```csharp
public abstract DbElement CreateFirst( DbElementType elementType );
```

**Parameters**

- **elementType** — New Element type

**Return Value**

New Element

#### `CreateLast` Method

Create new Element at the end of this Element's child list. This method throws an exception if operation fails.

```csharp
public abstract DbElement CreateLast( DbElementType elementType );
```

**Parameters**

- **elementType** — New Element type

**Return Value**

New Element

#### `DbNo` Method

Database number for the Database containing this Element

```csharp
public abstract int DbNo();
```

**Return Value**

Integer Database number

#### `Delete` Method

Delete this Element. This method throws an exception if operation fails.

```csharp
public abstract void Delete();
```

#### `DeleteRule` Method

Delete the Rule, attached to the given Attribute, from this Element. This method throws an exception if operation fails.

```csharp
public abstract void DeleteRule( DbAttribute attributeName );
```

**Parameters**

- **attributeName** — Attribute owning the Rule to be deleted

#### `Equals` Method

Compare this Element with general object.

```csharp
public abstract bool Equals( object type );
```

**Parameters**

- **type** — Object to compare against

**Return Value**

True, if object is equal

#### `EvaluateBool` Method

Evaluate boolean valued PML1 Expression against this Element. Example of such an expression is (HBORE GT 100). This method throws an exception if expression can not be evaluated.

```csharp
public abstract bool EvaluateBool( DbExpression expression );
```

**Parameters**

- **expression** — Expression to evaluate

**Return Value**

Boolean value from Expression

#### `EvaluateDouble` Method

Evaluate numerical valued PML1 Expression against this Element. Example of such an expression is (DIAM * 2). This method throws an exception if expression can not be evaluated.

```csharp
public abstract double EvaluateDouble( DbExpression expression , DbAttributeUnit units );
```

**Parameters**

- **expression** — Expression to evaluate
- **units** — Units for attribute concerned, if known. If unknown use NONE.

**Return Value**

Floating-point value from Expression

#### `EvaluateElement` Method

Evaluate reference valued PML1 Expression against this Element. Example of such an expression is (BOX 2 OF /MyEquip ). This method throws an exception if expression can not be evaluated.

```csharp
public abstract DbElement EvaluateElement( DbExpression expression );
```

**Parameters**

- **expression** — Expression to evaluate

**Return Value**

Element identified by Expression

#### `EvaluateString` Method

Evaluate text valued PML1 Expression against this Element. Example of such an expression is (DESC + 'Sometext') This method throws an exception if expression can not be evaluated.

```csharp
public abstract string EvaluateString( DbExpression expression );
```

**Parameters**

- **expression** — Expression to evaluate

**Return Value**

Text value from Expression

#### `ExecuteAllRules` Method

Execute all Rules on this Element. This method throws an exception if rules cannot be executed.

```csharp
public abstract void ExecuteAllRules();
```

#### `ExecuteRule` Method

Execute the Rule, attached to the given Attribute, on this Element. This method throws an exception if rules cannot be executed.

```csharp
public abstract void ExecuteRule( DbAttribute attributeName );
```

**Parameters**

- **attributeName** — Attribute owning the Rule to be deleted

#### `ExistRule` Method

Queries whether a Rule is attached to the given Attribute on this Element.

```csharp
public abstract bool ExistRule( DbAttribute attributeName );
```

**Parameters**

- **attributeName** — Attribute owning the Rule to be deleted

**Return Value**

True only if a Rule exists on the Element's Attribute

#### `FirstMember` Method ()

Navigate to first child Element.

```csharp
public abstract DbElement FirstMember();
```

**Return Value**

Child Element

#### `FirstMember` Method (DbElementType)

Navigate to first child Element that has given type.

```csharp
public abstract DbElement FirstMember( DbElementType elementType );
```

**Parameters**

- **elementType** — Element type

**Return Value**

Child Element

#### `GetActualType` Method

Get the actual type of this Element. Where this is a User-Defined Element Type, that is returned.

```csharp
public abstract DbElementType GetActualType();
```

**Return Value**

Element type

#### `GetAsString` Method (DbAttribute)

Get Attribute value on Element as text. This method works for all attributes that are valid ion this element The string returned will be correctly formated for output taking into account the current units. e.g. if in imperial units a position might be output as 'W 39'4.7/16 N 59'0.85/128 U 4'0.31/128'. This method throws an exception if attribute is invalid.

```csharp
public abstract string GetAsString( DbAttribute attributeName );
```

**Parameters**

- **attributeName** — Attribute to query

**Return Value**

Text value

#### `GetAsString` Method (DbAttribute, DbAttribute)

As for standard GetAsString() but allowing for an attribute qulaifier.

```csharp
public abstract string GetAsString( DbAttribute attributeName , DbAttribute qualifier );
```

**Parameters**

- **attributeName** — Attribute to query
- **qualifier** — Attribute as qualifier

**Return Value**

Text value

#### `GetAsString` Method (DbAttribute, DbElementType)

As for standard GetAsString() but allowing for an element type qulaifier.

```csharp
public abstract string GetAsString( DbAttribute attributeName , DbElementType qualifier );
```

**Parameters**

- **attributeName** — Attribute to query
- **qualifier** — Element type qualifier

**Return Value**

Text value

#### `GetAsString` Method (DbAttribute, Int32)

As for standard GetAsString() but allowing for an int qulaifier.

```csharp
public abstract string GetAsString( DbAttribute attributeName , int qualifier );
```

**Parameters**

- **attributeName** — Attribute to query
- **qualifier** — Integer value qualifier

**Return Value**

Text value

#### `GetAsString` Method (DbAttribute, String)

As for standard GetAsString() but allowing for an string qulaifier.

```csharp
public abstract string GetAsString( DbAttribute attributeName , string qualifier );
```

**Parameters**

- **attributeName** — Attribute to query
- **qualifier** — Text value qualifier

**Return Value**

Text value

#### `GetAsStringArray` Method (DbAttribute)

Get word array attribute as an array of strings.

```csharp
public abstract string[] GetAsStringArray( DbAttribute attributeName );
```

**Parameters**

- **attributeName** — Attribute to query

**Return Value**

array of values

#### `GetAsStringArray` Method (DbAttribute, DbQualifier)

Get word array attribute as an array of strings, allowing for qualifier.

```csharp
public abstract string[] GetAsStringArray( DbAttribute attributeName , DbQualifier qualifier );
```

**Parameters**

- **attributeName** — Attribute to query
- **qualifier** — Integer value qualifier

**Return Value**

array of values

#### `GetAsStringArray` Method (DbAttribute, Int32)

Deprecated- do not use. Use method with DbQualifier instead.

```csharp
public abstract string[] GetAsStringArray( DbAttribute attributeName , int qualifier );
```

#### `GetAttribute` Method (DbAttribute)

Get an instance of the Attribute identified by Attribute on Element. This method throws an exception if attribute is invalid.

```csharp
public abstract DbAttribute GetAttribute( DbAttribute attributeName );
```

**Parameters**

- **attributeName** — Attribute to query

**Return Value**

Attribute instance

#### `GetAttribute` Method (DbAttribute, DbQualifier)

Get an instance of the Attribute identified by Attribute on Element. This method throws an exception if attribute is invalid.

```csharp
public abstract DbAttribute GetAttribute( DbAttribute attributeName , DbQualifier qualifier );
```

**Parameters**

- **attributeName** — Attribute to query
- **qualifier** — 

**Return Value**

Attribute instance

#### `GetAttribute` Method (DbAttribute, Int32)

Deprecated- do not use. Use method with DbQualifier instead.

```csharp
public abstract DbAttribute GetAttribute( DbAttribute attributeName , int qualifier );
```

#### `GetAttributeArray` Method (DbAttribute)

Get array of Attribute instances identified by Attribute on Element. This method throws an exception if attribute is invalid.

```csharp
public abstract DbAttribute[] GetAttributeArray( DbAttribute attributeName );
```

**Parameters**

- **attributeName** — Attribute to query

**Return Value**

Array of Attribute instances

#### `GetAttributeArray` Method (DbAttribute, DbQualifier)

Get array of Attribute instances identified by Attribute on Element. This method throws an exception if attribute is invalid.

```csharp
public abstract DbAttribute[] GetAttributeArray( DbAttribute attributeName , DbQualifier qualifier );
```

**Parameters**

- **attributeName** — Attribute to query
- **qualifier** — 

**Return Value**

Array of Attribute instances

#### `GetAttributeArray` Method (DbAttribute, Int32)

Deprecated- do not use. Use method with DbQualifier instead.

```csharp
public abstract DbAttribute[] GetAttributeArray( DbAttribute attributeName , int qualifier );
```

#### `GetAttributes` Method

Get all the Attributes on this Element.

```csharp
public abstract DbAttribute[] GetAttributes();
```

**Return Value**

Array of Attributes

#### `GetAttributesWithRules` Method

Get all Attributes on this Element that have Rules.

```csharp
public abstract DbAttribute[] GetAttributesWithRules();
```

**Return Value**

Array of Attributes

#### `GetBool` Method (DbAttribute)

Get Boolean Attribute value on Element. This method throws an exception if attribute is invalid.

```csharp
public abstract bool GetBool( DbAttribute attributeName );
```

**Parameters**

- **attributeName** — Attribute to query

**Return Value**

Boolean value

#### `GetBool` Method (DbAttribute, DbAttribute)

Get Boolean Attribute value on Element, allowing for qualifier. This method throws an exception if attribute is invalid.

```csharp
public abstract bool GetBool( DbAttribute attributeName , DbAttribute qualifier );
```

**Parameters**

- **attributeName** — Attribute to query
- **qualifier** — Attribute as qualifier

**Return Value**

Boolean value

#### `GetBool` Method (DbAttribute, DbQualifier)

Get Boolean Attribute value on Element, allowing for qualifier. This method throws an exception if attribute is invalid.

```csharp
public abstract bool GetBool( DbAttribute attributeName , DbQualifier qualifier );
```

**Parameters**

- **attributeName** — Attribute to query
- **qualifier** — Integer value qualifier

**Return Value**

Boolean value

#### `GetBool` Method (DbAttribute, Int32)

Deprecated- do not use. Use method with DbQualifier instead.

```csharp
public abstract bool GetBool( DbAttribute attributeName , int qualifier );
```

#### `GetBoolArray` Method (DbAttribute)

Get Boolean array Attribute on Element. This method throws an exception if attribute is invalid.

```csharp
public abstract bool[] GetBoolArray( DbAttribute attributeName );
```

**Parameters**

- **attributeName** — Attribute to query

**Return Value**

Array of Boolean values

#### `GetBoolArray` Method (DbAttribute, DbQualifier)

Get Boolean array Attribute on Element. This method throws an exception if attribute is invalid.

```csharp
public abstract bool[] GetBoolArray( DbAttribute attributeName , DbQualifier qualifier );
```

**Parameters**

- **attributeName** — Attribute to query
- **qualifier** — Integer value qualifier

**Return Value**

Array of Boolean values

#### `GetBoolArray` Method (DbAttribute, Int32)

Deprecated- do not use. Use method with DbQualifier instead.

```csharp
public abstract bool[] GetBoolArray( DbAttribute attributeName , int qualifier );
```

#### `GetDate` Method

Get Date-Time Attribute value on Element. This method throws an exception if attribute is invalid.

```csharp
public abstract DateTime GetDate( DbAttribute attributeName );
```

**Parameters**

- **attributeName** — Attribute to query

**Return Value**

Date-Time value

#### `GetDateTime` Method

Get Date-Time Attribute value on Element. This method throws an exception if attribute is invalid.

```csharp
public abstract DateTime GetDateTime( DbAttribute attributeName );
```

**Parameters**

- **attributeName** — Attribute to query

**Return Value**

Date-time value

#### `GetDirection` Method (DbAttribute)

Get direction value Attribute on Element. This method throws an exception if attribute is invalid.

```csharp
public abstract Direction GetDirection( DbAttribute attributeName );
```

**Parameters**

- **attributeName** — Attribute to query

**Return Value**

Vector instance

#### `GetDirection` Method (DbAttribute, DbQualifier)

Get direction value Attribute on Element. This method throws an exception if attribute is invalid.

```csharp
public abstract Direction GetDirection( DbAttribute attributeName , DbQualifier qualifier );
```

**Parameters**

- **attributeName** — 
- **qualifier** — 

#### `GetDirection` Method (DbAttribute, Int32)

Deprecated- do not use. Use method with DbQualifier instead.

```csharp
public abstract Direction GetDirection( DbAttribute attributeName , int qualifier );
```

#### `GetDirection` Method (DbAttribute, Int32, DbElement)

Get direction value Attribute on Element, relative to another Element. This method throws an exception if attribute is invalid.

```csharp
public abstract Direction GetDirection( DbAttribute attributeName , int qualifier , DbElement wrt );
```

**Parameters**

- **attributeName** — 
- **qualifier** — 
- **wrt** — Element giving origin

#### `GetDouble` Method (DbAttribute)

Get floating-point Attribute value on Element. This method throws an exception if attribute is invalid.

```csharp
public abstract double GetDouble( DbAttribute attributeName );
```

**Parameters**

- **attributeName** — Attribute to query

**Return Value**

Floating-point value

#### `GetDouble` Method (DbAttribute, DbQualifier)

Get floating-point Attribute value on Element. This method throws an exception if attribute is invalid.

```csharp
public abstract double GetDouble( DbAttribute attributeName , DbQualifier qualifier );
```

**Parameters**

- **attributeName** — Attribute to query
- **qualifier** — Integer value qualifier

**Return Value**

Floating-point value

#### `GetDouble` Method (DbAttribute, Int32)

Deprecated- do not use. Use method with DbQualifier instead.

```csharp
public abstract double GetDouble( DbAttribute attributeName , int qualifier );
```

#### `GetDoubleArray` Method (DbAttribute)

Get floating-point array Attribute on Element. This method throws an exception if attribute is invalid.

```csharp
public abstract double[] GetDoubleArray( DbAttribute attributeName );
```

**Parameters**

- **attributeName** — Attribute to query

**Return Value**

Array of floating-point values

#### `GetDoubleArray` Method (DbAttribute, DbQualifier)

Get floating-point array Attribute on Element. This method throws an exception if attribute is invalid.

```csharp
public abstract double[] GetDoubleArray( DbAttribute attributeName , DbQualifier qualifier );
```

**Parameters**

- **attributeName** — Attribute to query
- **qualifier** — Integer value qualifier

**Return Value**

Array of floating-point values

#### `GetDoubleArray` Method (DbAttribute, Int32)

Deprecated- do not use. Use method with DbQualifier instead.

```csharp
public abstract double[] GetDoubleArray( DbAttribute attributeName , int qualifier );
```

#### `GetElement` Method ()

Get a null Element instance.

```csharp
public static DbElement GetElement();
```

**Return Value**

Element instance

#### `GetElement` Method (DbAttribute)

Get Element instance referenced by Attribute on Element. This method throws an exception if attribute is invalid.

```csharp
public abstract DbElement GetElement( DbAttribute attributeName );
```

**Parameters**

- **attributeName** — Attribute to query

**Return Value**

Element instance

#### `GetElement` Method (DbAttribute, DbElementType)

Get Element instance referenced by Attribute on Element. This method throws an exception if attribute is invalid.

```csharp
public abstract DbElement GetElement( DbAttribute attributeName , DbElementType qualifier );
```

**Parameters**

- **attributeName** — Attribute to query
- **qualifier** — Element type qualifier

**Return Value**

Element instance

#### `GetElement` Method (DbAttribute, DbQualifier)

Get Element instance referenced by Attribute on Element. This method throws an exception if attribute is invalid.

```csharp
public abstract DbElement GetElement( DbAttribute attributeName , DbQualifier qualifier );
```

**Parameters**

- **attributeName** — Attribute to query
- **qualifier** — Integer value qualifier

**Return Value**

Element instance

#### `GetElement` Method (DbAttribute, Int32)

Deprecated- do not use. Use method with DbQualifier instead.

```csharp
public abstract DbElement GetElement( DbAttribute attributeName , int qualifier );
```

#### `GetElement` Method (DbAttribute, String)

Get Element instance referenced by Attribute on Element. This method throws an exception if attribute is invalid.

```csharp
public abstract DbElement GetElement( DbAttribute attributeName , string qualifier );
```

**Parameters**

- **attributeName** — 
- **qualifier** — 

#### `GetElement` Method (Int32[])

Get an Element instance using reference number pair. If the reference number is not valid, a null Element is returned. This method throws an exception if attribute is invalid.

```csharp
public static DbElement GetElement( int[] reference );
```

**Parameters**

- **reference** — Element reference number pair

**Return Value**

Element instance

#### `GetElement` Method (Int32[], DbElementType)

Get an Element instance using reference number pair, and element type.

```csharp
public static DbElement GetElement( int[] reference , DbElementType type );
```

**Parameters**

- **reference** — Reference number pair
- **type** — Element type

**Return Value**

Element instance

#### `GetElement` Method (String)

Get an Element instance using element name. If the element name is not known, a null Element is returned.

```csharp
public static DbElement GetElement( string name );
```

**Parameters**

- **name** — Name of element

**Return Value**

Element instance

#### `GetElementArray` Method (DbAttribute)

Get array of Element instances referenced by Attribute on Element. This method throws an exception if attribute is invalid.

```csharp
public abstract DbElement[] GetElementArray( DbAttribute attributeName );
```

**Parameters**

- **attributeName** — Attribute to query

**Return Value**

Array of Element instances

#### `GetElementArray` Method (DbAttribute, DbElementType)

Get array of Element instances referenced by Attribute on Element. This method throws an exception if attribute is invalid.

```csharp
public abstract DbElement[] GetElementArray( DbAttribute attributeName , DbElementType qualifier );
```

**Parameters**

- **attributeName** — 
- **qualifier** — 

#### `GetElementArray` Method (DbAttribute, DbQualifier)

Get array of Element instances referenced by Attribute on Element. This method throws an exception if attribute is invalid.

```csharp
public abstract DbElement[] GetElementArray( DbAttribute attributeName , DbQualifier qualifier );
```

**Parameters**

- **attributeName** — 
- **qualifier** — 

#### `GetElementArray` Method (DbAttribute, Int32)

Deprecated- do not use. Use method with DbQualifier instead.

```csharp
public abstract DbElement[] GetElementArray( DbAttribute attributeName , int qualifier );
```

#### `GetElementType` Method ()

Get the type of this Element. Where this is a User-Defined Element Type, the base type is returned.

```csharp
public abstract DbElementType GetElementType();
```

**Return Value**

Element type, or base type

#### `GetElementType` Method (DbAttribute)

Get the Element type identifed by Attribute on Element. This method throws an exception if attribute is invalid.

```csharp
public abstract DbElementType GetElementType( DbAttribute attributeName );
```

**Parameters**

- **attributeName** — Attribute to query

**Return Value**

Element type

#### `GetElementType` Method (DbAttribute, DbQualifier)

Get the Element type identifed by Attribute on Element. This method throws an exception if attribute is invalid.

```csharp
public abstract DbElementType GetElementType( DbAttribute attributeName , DbQualifier qualifier );
```

**Parameters**

- **attributeName** — 
- **qualifier** — 

#### `GetElementType` Method (DbAttribute, Int32)

Deprecated- do not use. Use method with DbQualifier instead.

```csharp
public abstract DbElementType GetElementType( DbAttribute attributeName , int qualifier );
```

#### `GetElementTypeArray` Method (DbAttribute)

Get array of Element types identified by Attribute on Element. This method throws an exception if attribute is invalid.

```csharp
public abstract DbElementType[] GetElementTypeArray( DbAttribute attributeName );
```

**Parameters**

- **attributeName** — Attribute to query

**Return Value**

Array of Element types

#### `GetElementTypeArray` Method (DbAttribute, DbQualifier)

Get array of Element types identified by Attribute on Element. This method throws an exception if attribute is invalid.

```csharp
public abstract DbElementType[] GetElementTypeArray( DbAttribute attributeName , DbQualifier qualifier );
```

**Parameters**

- **attributeName** — 
- **qualifier** — 

#### `GetElementTypeArray` Method (DbAttribute, Int32)

Deprecated- do not use. Use method with DbQualifier instead.

```csharp
public abstract DbElementType[] GetElementTypeArray( DbAttribute attributeName , int qualifier );
```

#### `GetExpression` Method

Get Expression instance given by Attribute on Element. This method throws an exception if attribute is invalid.

```csharp
public abstract DbExpression GetExpression( DbAttribute attributeName );
```

**Parameters**

- **attributeName** — Attribute to query

**Return Value**

Expression instance

#### `GetHashCode` Method

Get the hash code for this Element, overriding Object.GetHashCode.

```csharp
public abstract int GetHashCode();
```

**Return Value**

Hash code

#### `GetInteger` Method (DbAttribute)

Get integer Attribute value on Element. This method throws an exception if attribute is invalid.

```csharp
public abstract int GetInteger( DbAttribute attributeName );
```

**Parameters**

- **attributeName** — Attribute to query

**Return Value**

Integer value

#### `GetInteger` Method (DbAttribute, DbAttribute)

Get integer Attribute value on Element. This method throws an exception if attribute is invalid.

```csharp
public abstract int GetInteger( DbAttribute attributeName , DbAttribute qualifier );
```

**Parameters**

- **attributeName** — 
- **qualifier** — 

#### `GetInteger` Method (DbAttribute, DbElementType)

Get integer Attribute value on Element. This method throws an exception if attribute is invalid.

```csharp
public abstract int GetInteger( DbAttribute attributeName , DbElementType qualifier );
```

**Parameters**

- **attributeName** — 
- **qualifier** — 

#### `GetInteger` Method (DbAttribute, DbQualifier)

Get integer Attribute value on Element. This method throws an exception if attribute is invalid.

```csharp
public abstract int GetInteger( DbAttribute attributeName , DbQualifier qualifier );
```

**Parameters**

- **attributeName** — 
- **qualifier** — 

#### `GetInteger` Method (DbAttribute, Int32)

Deprecated- do not use. Use method with DbQualifier instead.

```csharp
public abstract int GetInteger( DbAttribute attributeName , int qualifier );
```

#### `GetInteger` Method (DbAttribute, String)

Get integer Attribute value on Element. This method throws an exception if attribute is invalid.

```csharp
public abstract int GetInteger( DbAttribute attributeName , string qualifier );
```

**Parameters**

- **attributeName** — 
- **qualifier** —

#### `GetIntegerArray` Method (DbAttribute)

Get integer array Attribute on Element. This method throws an exception if attribute is invalid.

```csharp
public abstract int[] GetIntegerArray( DbAttribute attributeName );
```

**Parameters**

- **attributeName** — Attribute to query

**Return Value**

Array of integer values

#### `GetIntegerArray` Method (DbAttribute, DbAttribute)

Get integer array Attribute on Element. This method throws an exception if attribute is invalid.

```csharp
public abstract int[] GetIntegerArray( DbAttribute attributeName , DbAttribute qualifier );
```

**Parameters**

- **attributeName** — 
- **qualifier** — 

#### `GetIntegerArray` Method (DbAttribute, DbQualifier)

Get integer array Attribute on Element. This method throws an exception if attribute is invalid.

```csharp
public abstract int[] GetIntegerArray( DbAttribute attributeName , DbQualifier qualifier );
```

**Parameters**

- **attributeName** — 
- **qualifier** — 

#### `GetIntegerArray` Method (DbAttribute, Int32)

Deprecated- do not use. Use method with DbQualifier instead.

```csharp
public abstract int[] GetIntegerArray( DbAttribute attributeName , int qualifier );
```

#### `GetOrientation` Method (DbAttribute)

Get orientation value Attribute on Element. This method throws an exception if attribute is invalid.

```csharp
public abstract Orientation GetOrientation( DbAttribute attributeName );
```

**Parameters**

- **attributeName** — Attribute to query

**Return Value**

Matrix instance

#### `GetOrientation` Method (DbAttribute, DbQualifier)

Get orientation value Attribute on Element. This method throws an exception if attribute is invalid.

```csharp
public abstract Orientation GetOrientation( DbAttribute attributeName , DbQualifier qualifier );
```

**Parameters**

- **attributeName** — 
- **qualifier** — 

#### `GetOrientation` Method (DbAttribute, Int32)

Deprecated- do not use. Use method with DbQualifier instead.

```csharp
public abstract Orientation GetOrientation( DbAttribute attributeName , int qualifier );
```

#### `GetOrientation` Method (DbAttribute, Int32, DbElement)

Get orientation value Attribute on Element, relative to another Element. This method throws an exception if attribute is invalid.

```csharp
public abstract Orientation GetOrientation( DbAttribute attributeName , int qualifier , DbElement wrt );
```

**Parameters**

- **attributeName** — 
- **qualifier** — 
- **wrt** — Element giving origin

#### `GetParameterList` Method

Get ParameterList Attribute value on Element. This method throws an exception if attribute is invalid.

```csharp
public abstract ParameterList GetParameterList( DbAttribute attributeName );
```

**Parameters**

- **attributeName** — Attribute to query

**Return Value**

ParameterList instance

#### `GetPosition` Method (DbAttribute)

Get position value Attribute on Element. This method throws an exception if attribute is invalid.

```csharp
public abstract Position GetPosition( DbAttribute attributeName );
```

**Parameters**

- **attributeName** — Attribute to query

**Return Value**

Point instance

#### `GetPosition` Method (DbAttribute, DbQualifier)

Get position value Attribute on Element. This method throws an exception if attribute is invalid.

```csharp
public abstract Position GetPosition( DbAttribute attributeName , DbQualifier qualifier );
```

**Parameters**

- **attributeName** — 
- **qualifier** — 

#### `GetPosition` Method (DbAttribute, Int32)

Deprecated- do not use. Use method with DbQualifier instead.

```csharp
public abstract Position GetPosition( DbAttribute attributeName , int qualifier );
```

#### `GetPosition` Method (DbAttribute, Int32, DbElement)

Get position value Attribute on Element, relative to another Element. This method throws an exception if attribute is invalid.

```csharp
public abstract Position GetPosition( DbAttribute attributeName , int qualifier , DbElement wrt );
```

**Parameters**

- **attributeName** — 
- **qualifier** — 
- **wrt** — Element giving origin

**Return Value**

Point instance

#### `GetRule` Method

Get Rule instance for Attribute on Element. This method throws an exception if no rule exists.

```csharp
public abstract DbRule GetRule( DbAttribute attributeName );
```

**Parameters**

- **attributeName** — Attribute

**Return Value**

Rule instance

#### `GetString` Method (DbAttribute)

Get text value Attribute on Element. This method throws an exception if attribute is invalid.

```csharp
public abstract string GetString( DbAttribute attributeName );
```

**Parameters**

- **attributeName** — Attribute to query

**Return Value**

Text value

#### `GetString` Method (DbAttribute, DbAttribute)

Get text value Attribute on Element. This method throws an exception if attribute is invalid.

```csharp
public abstract string GetString( DbAttribute attributeName , DbAttribute qualifier );
```

**Parameters**

- **attributeName** — 
- **qualifier** — 

#### `GetString` Method (DbAttribute, DbQualifier)

Get text value Attribute on Element. This method throws an exception if attribute is invalid.

```csharp
public abstract string GetString( DbAttribute attributeName , DbQualifier qualifier );
```

**Parameters**

- **attributeName** — 
- **qualifier** — 

#### `GetString` Method (DbAttribute, Int32)

Deprecated- do not use. Use method with DbQualifier instead.

```csharp
public abstract string GetString( DbAttribute attributeName , int qualifier );
```

#### `GetString` Method (DbAttribute, String)

Get text value Attribute on Element. This method throws an exception if attribute is invalid.

```csharp
public abstract string GetString( DbAttribute attributeName , string qualifier );
```

**Parameters**

- **attributeName** — 
- **qualifier** —

#### `GetValidAsString` Method

Get Attribute value on Element as text. This method works for all attributes that are valid ion this element The string returned will be correctly formated for output taking into account the current units. e.g. if in imperial units a position might be output as 'W 39'4.7/16 N 59'0.85/128 U 4'0.31/128'.

```csharp
public abstract bool GetValidAsString( DbAttribute attributeName , ref string attributeValue );
```

**Parameters**

- **attributeName** — Attribute to query
- **attributeValue** — Text value, where return value is True

**Return Value**

True, if attribute exists; False, if attribute does not exist

#### `GetValidBool` Method

Get Boolean Attribute value on Element, if available.

```csharp
public abstract bool GetValidBool( DbAttribute attributeName , ref bool attributeValue );
```

**Parameters**

- **attributeName** — Attribute to query
- **attributeValue** — Boolean value, where return value is True

**Return Value**

True, if Attribute exists; False if Attribute does not exist

#### `GetValidDouble` Method

Get floating-point Attribute value on Element, if available.

```csharp
public abstract bool GetValidDouble( DbAttribute attributeName , ref double dval );
```

**Parameters**

- **attributeName** — Attribute to query
- **dval** — Floating-point value, where return value is True

**Return Value**

True, if Attribute is valid; False, if Attribute is not valid

#### `GetValidInteger` Method

Get integer Attribute value on Element, if available.

```csharp
public abstract bool GetValidInteger( DbAttribute attributeName , ref int intVal );
```

**Parameters**

- **attributeName** — Attribute to query
- **intVal** — Integer value, where return value is True

**Return Value**

True, if Attribute is valid; False, if Attribute is not valid

#### `GetValidString` Method

Get text value Attribute on Element, if available.

```csharp
public abstract bool GetValidString( DbAttribute attributeName , ref string attributeValue );
```

**Parameters**

- **attributeName** — Attribute to query
- **attributeValue** — Text value, where return vaule is True

**Return Value**

True, if Attribute is valid; False, if Attribute is not valid

#### `InsertAfter` Method

Insert Element after the given reference Element. This method throws an exception if insertion fails.

```csharp
public abstract void InsertAfter( DbElement element );
```

**Parameters**

- **element** — Reference Element

#### `InsertAfterLast` Method

Insert Element after the last child of the given parent Element. This method throws an exception if insertion fails.

```csharp
public abstract void InsertAfterLast( DbElement owner );
```

**Parameters**

- **owner** — Parent Element

#### `InsertBefore` Method

Insert Element before the given reference Element. This method throws an exception if insertion fails.

```csharp
public abstract void InsertBefore( DbElement element );
```

**Parameters**

- **element** — Reference Element

#### `InsertBeforeFirst` Method

Insert Element before the first child of the given parent Element. This method throws an exception if insertion fails.

```csharp
public abstract void InsertBeforeFirst( DbElement owner );
```

**Parameters**

- **owner** — Parent Element

#### `InsertIntoSecondaryListAfter` Method

Insert Element into secondary list, after the given reference Element. This method throws an exception if insertion fails.

```csharp
public abstract void InsertIntoSecondaryListAfter( DbElement element , DbElement group );
```

**Parameters**

- **element** — Reference Element
- **group** — Parent Element

#### `InsertIntoSecondaryListAfterLast` Method

Insert Element into secondary list, after the last child of the given parent Element. This method throws an exception if insertion fails.

```csharp
public abstract void InsertIntoSecondaryListAfterLast( DbElement group );
```

**Parameters**

- **group** — Parent Element

#### `InsertIntoSecondaryListBefore` Method

Insert Element into secondary list, before the given reference Element. This method throws an exception if insertion fails.

```csharp
public abstract void InsertIntoSecondaryListBefore( DbElement element , DbElement group );
```

**Parameters**

- **element** — Reference Element
- **group** — Parent Element

#### `InsertIntoSecondaryListBeforeFirst` Method

Insert Element into secondary list, before the first child of the given parent Element. This method throws an exception if insertion fails.

```csharp
public abstract void InsertIntoSecondaryListBeforeFirst( DbElement group );
```

**Parameters**

- **group** — Parent Element

#### `IsAttributeSetable` Method

Queries whether the named Attribute on this Element can be set.

```csharp
public abstract bool IsAttributeSetable( DbAttribute attributeName );
```

**Parameters**

- **attributeName** — Attribute to query

**Return Value**

True, if Element's Attribute can be set

#### `IsAttributeValid` Method

Queries whether the named Attribute value on this Element is valid.

```csharp
public abstract bool IsAttributeValid( DbAttribute attributeName );
```

**Parameters**

- **attributeName** — Name of Attribute

**Return Value**

True, if Element's Attribute is valid

#### `IsCopyable` Method

Queries whether the Attributes of another Element can be copied into this Element.

```csharp
public abstract bool IsCopyable( DbElement elementToCopyFrom );
```

**Parameters**

- **elementToCopyFrom** — Element to copy Attributes from

**Return Value**

True, if Element Attributes can be copied

#### `IsCreatable` Method

Queries whether a child Element of a given type can be created

```csharp
public abstract bool IsCreatable( DbElementType elementType );
```

**Parameters**

- **elementType** — Element Type

**Return Value**

True, if child Element can be created

#### `IsDescendant` Method

Queries whether this Element is a descendant of the given Element.

```csharp
public abstract bool IsDescendant( DbElement element );
```

**Parameters**

- **element** — Possible parent Element

**Return Value**

True, if Element

#### `IsInsertable` Method

Queries whether this Element can be inserted as child to the given Element.

```csharp
public abstract bool IsInsertable( DbElement owner );
```

**Parameters**

- **owner** — Proposed parent Element

**Return Value**

True, if Element can be inserted as child

#### `LastMember` Method

Returns the last child Element of this Element. If none, returns a null DbElement.

```csharp
public abstract DbElement LastMember();
```

**Return Value**

Last child Element

#### `Member` Method

Returns the numbered child Element of this Element. If none, returns a null DbElement.

```csharp
public abstract DbElement Member( int number );
```

**Parameters**

- **number** — Index of child

**Return Value**

Indexed child Element

#### `Members` Method ()

Returns all child Elements of this Element.

```csharp
public abstract DbElement[] Members();
```

**Return Value**

Array containing all child Elements

#### `Members` Method (DbElementType)

Returns all child Elements of this Element that have Element Type.

```csharp
public abstract DbElement[] Members( DbElementType type );
```

**Parameters**

- **type** — Element Type

**Return Value**

Array containing child Elements

#### `Next` Method ()

Returns the next Element in order from this Element. If none, returns a null DbElement.

```csharp
public abstract DbElement Next();
```

**Return Value**

Next Element

#### `Next` Method (DbElementType)

Returns the next Element in order that has the given Element Type, from this Element. If none, returns a null DbElement.

```csharp
public abstract DbElement Next( DbElementType type );
```

**Parameters**

- **type** — Element Type

**Return Value**

Next conforming Element

#### `PassObjectToCPP` Method

Pass object through to unmanaged C++.

```csharp
public abstract void PassObjectToCPP( int pos , PdmsMessage message );
```

**Parameters**

- **pos** — Position index
- **message** — Associated message

**Implements**

IMessage.PassObjectToCPP

#### `PropagateRules` Method

Re-evaluate all rule-dependent attributes, following change to Attribute on this Element

```csharp
public abstract void PropagateRules( DbAttribute attributeName );
```

**Parameters**

- **attributeName** — Attribute that has changed

#### `RefNo` Method

Reference number pair for this Element

```csharp
public abstract int[] RefNo();
```

**Return Value**

Array of two integer values

#### `Release` Method

Release claim on this Element. Method throws an exception if not allowed.

```csharp
public abstract void Release();
```

#### `ReleaseHierarchy` Method

Release claim on this Element and all its descendants. Method throws an exception if not allowed. The method will always release what it can.

```csharp
public abstract void ReleaseHierarchy();
```

#### `RemoveFromSecondaryList` Method

Remove this Element from the secondary list of another Element Method throws an exception if not allowed.

```csharp
public abstract void RemoveFromSecondaryList( DbElement group );
```

**Parameters**

- **group** — Element with secondary list

#### `SetAttribute` Method (DbAttribute, DbElement)

Set Attribute on Element to reference another Element. Method throws an exception if not allowed.

```csharp
public abstract void SetAttribute( DbAttribute attributeName , DbElement val );
```

**Parameters**

- **attributeName** — Attribute to set
- **val** — Value as Element

#### `SetAttribute` Method (DbAttribute, DbElement[])

Set Attribute on Element as an array of Elements. Method throws an exception if not allowed.

```csharp
public abstract void SetAttribute( DbAttribute attributeName , DbElement[] value );
```

**Parameters**

- **attributeName** — Attribute to set
- **value** — Value as array of Elements

#### `SetAttribute` Method (DbAttribute, ParameterList)

Set Attribute on Element as a ParameterList. Method throws an exception if not allowed.

```csharp
public abstract void SetAttribute( DbAttribute attributeName , ParameterList p );
```

**Parameters**

- **attributeName** — Attribute to set
- **p** — Values as ParameterList

#### `SetAttribute` Method (DbAttribute, Direction)

Set Attribute on Element as a vector. Method throws an exception if not allowed.

```csharp
public abstract void SetAttribute( DbAttribute attributeName , Direction dir );
```

**Parameters**

- **attributeName** — Attribute to set
- **dir** — Value as vector

#### `SetAttribute` Method (DbAttribute, Orientation)

Set Attribute on Element as a matrix. Method throws an exception if not allowed.

```csharp
public abstract void SetAttribute( DbAttribute attributeName , Orientation ori );
```

**Parameters**

- **attributeName** — Attribute to set
- **ori** — Value as matrix

#### `SetAttribute` Method (DbAttribute, Position)

Set Attribute on Element as a point. Method throws an exception if not allowed.

```csharp
public abstract void SetAttribute( DbAttribute attributeName , Position pos );
```

**Parameters**

- **attributeName** — Attribute to set
- **pos** — Value as a point

#### `SetAttribute` Method (DbAttribute, Boolean)

Set Attribute on Element as a boolean. Method throws an exception if not allowed.

```csharp
public abstract void SetAttribute( DbAttribute attributeName , bool value );
```

**Parameters**

- **attributeName** — Attribute to set
- **value** — Value as boolean

#### `SetAttribute` Method (DbAttribute, Boolean[])

Set Attribute on Element as an array of boolean. Method throws an exception if not allowed.

```csharp
public abstract void SetAttribute( DbAttribute attributeName , bool[] val );
```

**Parameters**

- **attributeName** — Attribute to set
- **val** — Value as array of boolean

#### `SetAttribute` Method (DbAttribute, DateTime)

Set Attribute on Element as a date-time. Method throws an exception if not allowed.

```csharp
public abstract void SetAttribute( DbAttribute attributeName , DateTime val );
```

**Parameters**

- **attributeName** — Attribute to set
- **val** — Value as date-time

#### `SetAttribute` Method (DbAttribute, Double)

Set Attribute on Element as a double. Method throws an exception if not allowed.

```csharp
public abstract void SetAttribute( DbAttribute attributeName , double value );
```

**Parameters**

- **attributeName** — Attribute to set
- **value** — Value as double

#### `SetAttribute` Method (DbAttribute, Double[])

Set Attribute on Element as an array of double. Method throws an exception if not allowed.

```csharp
public abstract void SetAttribute( DbAttribute attributeName , double[] val );
```

**Parameters**

- **attributeName** — Attribute to set
- **val** — Value as array of double

#### `SetAttribute` Method (DbAttribute, Int32)

Set Attribute on Element as an integer. Method throws an exception if not allowed.

```csharp
public abstract void SetAttribute( DbAttribute attributeName , int value );
```

**Parameters**

- **attributeName** — Attribute to set
- **value** — Value as integer

#### `SetAttribute` Method (DbAttribute, Int32[])

Set Attribute on Element as an array of integer. Method throws an exception if not allowed.

```csharp
public abstract void SetAttribute( DbAttribute attributeName , int[] val );
```

**Parameters**

- **attributeName** — Attribute to set
- **val** — Value as array of integer

#### `SetAttribute` Method (DbAttribute, String)

Set Attribute on Element as text. Method throws an exception if not allowed.

```csharp
public abstract void SetAttribute( DbAttribute attributeName , string val );
```

**Parameters**

- **attributeName** — Attribute to set
- **val** — Value as text

#### `SetAttributeDefault` Method

Reset Attribute on Element to its default value. Method throws an exception if not allowed.

```csharp
public abstract void SetAttributeDefault( DbAttribute attributeName );
```

**Parameters**

- **attributeName** — Attribute to reset

#### `SetRule` Method

Attach the Rule to the given Attribute of this Element. Method throws an exception if not allowed.

```csharp
public abstract void SetRule( DbAttribute attributeName , DbRule rule );
```

**Parameters**

- **attributeName** — Attribute
- **rule** — Rule to attach

#### `ToString` Method

Get textual representation of this Element.

```csharp
public abstract string ToString();
```

**Return Value**

Text

#### `VerifyRule` Method

Verify that the value and the Rule attached to an Attribute of this Element, are consistent.

```csharp
public abstract bool VerifyRule( DbAttribute attributeName );
```

**Parameters**

- **attributeName** — Attribute with Rule

**Return Value**

True, if the Attribute value and Rule are consistent

## Operators

#### `Equality` Operator

Element equality operator

```csharp
public static bool operator ==( DbElement left , DbElement right );
```

**Parameters**

- **left** — Left-hand Element
- **right** — Right-hand Element

**Return Value**

True, if the Elements are equal

#### `Inequality` Operator

Element inqeuality operator

```csharp
public static bool operator !=( DbElement left , DbElement right );
```

**Parameters**

- **left** — Left-hand Element
- **right** — Right-hand Element

**Return Value**

True, if the Elements are not equal
