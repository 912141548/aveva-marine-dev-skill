---
title: Aveva.Pdms.Database.DbElementTypeFormat Class
namespace: Aveva.Pdms.Database
assembly: Aveva.Pdms.Database
kind: Class
source: Aveva.Pdms.Database
---

# Aveva.Pdms.Database.DbElementTypeFormat Class

> Class to define an object for formatting a DbElementType definition for output ie what fields are to displayed, what intervening text etc Generally, a DbElementTypeFormat will be used by a DbElementTypeListFormat, which defines how a whole list of DbElementTypes is formatted

## Syntax

```csharp
public class DbElementTypeFormat
```

## Inheritance

`System.Object` → `Aveva.Pdms.Database.DbElementTypeFormat`

## Thread Safety

Public static ( Shared in Visual Basic) members of this type are
safe for multithreaded operations. Instance members are not guaranteed to be
thread-safe.

## Requirements

Namespace:
Aveva.Pdms.Database
Assembly: Aveva.Pdms.Database (in Aveva.Pdms.Database.dll)

## Constructors

#### `DbElementTypeFormat` Constructor

Initializes a new instance of the DbElementTypeFormat class.

```csharp
public DbElementTypeFormat();
```

## Properties

#### `DbRestriction` Property

Gets or sets the db type; if set will restrict owners/members etc to that db (0 for no restriction)

```csharp
public int DbRestriction {get; set;}
```

#### `DefaultArraySeparator` Property

```csharp
public string DefaultArraySeparator {get; set;}
```

#### `DefaultItemSeparator` Property

```csharp
public string DefaultItemSeparator {get; set;}
```

## Methods

#### `AddItem` Method (DbNounField)

Add a field to the format

```csharp
public void AddItem( DbNounField field );
```

**Parameters**

- **field** — A field

#### `AddItem` Method (DbNounField, DbFieldFormat)

Add a field to the format, specifying the field format

```csharp
public void AddItem( DbNounField field , DbFieldFormat fieldformat );
```

**Parameters**

- **field** — A field
- **fieldformat** — Format for the field

#### `AddItem` Method (DbNounField, DbFieldFormat, Int32)

Add a field to the format, specifying the field format and mimimum width

```csharp
public void AddItem( DbNounField field , DbFieldFormat fieldformat , int width );
```

**Parameters**

- **field** — A field
- **fieldformat** — Format for the field
- **width** — The minimum width of the column

#### `AddItem` Method (DbNounField, Int32)

Add a field to the format, specifying the mimimum width

```csharp
public void AddItem( DbNounField field , int width );
```

**Parameters**

- **field** — A field
- **width** — The minimum width of the column

#### `AddItem` Method (DbNounSpecialField)

Add a special field to the format

```csharp
public void AddItem( DbNounSpecialField field );
```

**Parameters**

- **field** — A special field

#### `AddItem` Method (DbNounSpecialField, DbFieldFormat)

Add a special field to the format, specifying the field format

```csharp
public void AddItem( DbNounSpecialField field , DbFieldFormat fieldformat );
```

**Parameters**

- **field** — A special field
- **fieldformat** — Format for the field

#### `AddItem` Method (DbNounSpecialField, DbFieldFormat, Int32)

Add a special field to the format, specifying the field format and mimimum width

```csharp
public void AddItem( DbNounSpecialField field , DbFieldFormat fieldformat , int width );
```

**Parameters**

- **field** — A special field
- **fieldformat** — Format for the field
- **width** — The minimum width of the column

#### `AddItem` Method (DbNounSpecialField, Int32)

Add a special field to the format, specifying the minimum width

```csharp
public void AddItem( DbNounSpecialField field , int width );
```

**Parameters**

- **field** — A special field
- **width** — The minimum width of the column

#### `AddItem` Method (Int32)

Add sufficient spaces to bring the result string up to the specified number of characters NB: It is inadvisable to mix using this feature with adding special characters such as newline or tab, since these will count as one character

```csharp
public void AddItem( int tab );
```

**Parameters**

- **tab** — The number of characters

#### `AddItem` Method (String)

Add literal text to the format; this may include special characters such as tab or newline

```csharp
public void AddItem( string mystring );
```

**Parameters**

- **mystring** — Text to be added to format

#### `AddItem` Method (String, Int32)

Add literal text to the format, specifying the minimum width

```csharp
public void AddItem( string mystring , int width );
```

**Parameters**

- **mystring** — Text to be added to format
- **width** — The minimum width of the column

#### `Format` Method

Return a string representing the DbElementType in the defined format

```csharp
public string Format( DbElementType noun );
```

**Parameters**

- **noun** — 

**Return Value**

DbElementType definition formatted in format defined
