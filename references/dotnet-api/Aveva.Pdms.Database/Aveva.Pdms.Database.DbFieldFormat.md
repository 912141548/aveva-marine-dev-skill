---
title: Aveva.Pdms.Database.DbFieldFormat Class
namespace: Aveva.Pdms.Database
assembly: Aveva.Pdms.Database
kind: Class
source: Aveva.Pdms.Database
---

# Aveva.Pdms.Database.DbFieldFormat Class

> Class to define objects to control the representation of field values

## Syntax

```csharp
public class DbFieldFormat
```

## Inheritance

`System.Object` → `Aveva.Pdms.Database.DbFieldFormat`

## Thread Safety

Public static ( Shared in Visual Basic) members of this type are
safe for multithreaded operations. Instance members are not guaranteed to be
thread-safe.

## Requirements

Namespace:
Aveva.Pdms.Database
Assembly: Aveva.Pdms.Database (in Aveva.Pdms.Database.dll)

## Constructors

#### `DbFieldFormat` Constructor

Initializes a new instance of the DbFieldFormat class.

```csharp
public DbFieldFormat();
```

## Properties

#### `ArraySeparator` Property

String to use to separate individual array elements. Typically ', ' for a list

```csharp
public string ArraySeparator {get; set;}
```

#### `DbRestriction` Property

INTEGER database number to restrict elements to those from a certain database for certain special fields (e.g. owner and member types). 0 for no restriction.

```csharp
public int DbRestriction {get; set;}
```

#### `DefaultAction` Property

Action to take if a value is found which does not match a specified mapping By default, this is GET_AS_STRING which will leave the value unchanged It may be set to FIXED_STRING so that any such (unmapped) string will be replaced by the DefaultString

```csharp
public DbFieldFormatDefaultAction DefaultAction {get; set;}
```

#### `DefaultString` Property

String with which to replace any string for which no individual mapping has been defined (with AddMapping) Only used if the DefaultAction is FIXED_STRING

```csharp
public string DefaultString {get; set;}
```

#### `ItemSeparator` Property

String to use to separate items within compound fields. Only used for special fields such as attributes and descriptions. Typically a tab or a colon

```csharp
public string ItemSeparator {get; set;}
```

#### `NonEmptyPrefix` Property

String to prepend to the result if and only if it is not the empty string

```csharp
public string NonEmptyPrefix {get; set;}
```

#### `NonEmptySuffix` Property

String to append to the result if and only if it is not the empty string

```csharp
public string NonEmptySuffix {get; set;}
```

#### `RemoveDuplicates` Property

Whether or not duplicate array items are to be removed NB: Equality is checked AFTER any replacements and mappings

```csharp
public bool RemoveDuplicates {get; set;}
```

#### `SortValues` Property

Whether or not array items are to be sorted into alphabetic order NB: Sorting is applied AFTER any replacements and mappings

```csharp
public bool SortValues {get; set;}
```

#### `UndefinedString` Property

String to substitute if no value is defined

```csharp
public string UndefinedString {get; set;}
```

## Methods

#### `AddMapping` Method

Add a mapping; ie, a specification of a value which is to be replaced by another value

```csharp
public void AddMapping( string invalue , string svalue );
```

**Parameters**

- **invalue** — Value to be replaced
- **svalue** — Value with which it is to be replaced

#### `AddReplace` Method

Add a replacement specification. Replacements are applied first, and will replace any and all occurences of the invalue in values returned with the rvalue

```csharp
public void AddReplace( string invalue , string rvalue );
```

**Parameters**

- **invalue** — String to be replaced
- **rvalue** — String with which it is to be replaced

#### `Format` Method (DbAttribute, DbAttributeField)

Return the formatted value of a field for a given attribute

```csharp
public string Format( DbAttribute att , DbAttributeField field );
```

**Parameters**

- **att** — An attribute
- **field** — A field of the attribute

**Return Value**

The formatted value of the field of the attribute

#### `Format` Method (DbAttribute, DbAttributeSpecialField)

Return the formatted value of a special field for a given attribute

```csharp
public string Format( DbAttribute att , DbAttributeSpecialField field );
```

**Parameters**

- **att** — An attribute
- **field** — A special field of the attribute

**Return Value**

The formatted value of the field of the attribute

#### `Format` Method (DbElementType, DbNounField)

Return the formatted value of a field for a given ElementType

```csharp
public string Format( DbElementType noun , DbNounField field );
```

**Parameters**

- **noun** — 
- **field** — A field of the ElementType

**Return Value**

The formatted value of the field of the ElementType

#### `Format` Method (DbElementType, DbNounSpecialField)

Return the formatted value of a special field for a given ElementType

```csharp
public string Format( DbElementType noun , DbNounSpecialField field );
```

**Parameters**

- **noun** — 
- **field** — A special field of the ElementType

**Return Value**

The formatted value of the specual field of the ElementType
