---
title: Aveva.Pdms.Database.DbAttributeFormat Class
namespace: Aveva.Pdms.Database
assembly: Aveva.Pdms.Database
kind: Class
source: Aveva.Pdms.Database
---

# Aveva.Pdms.Database.DbAttributeFormat Class

> Class to define an object for formatting an attribute definition for output ie what fields are to displayed, what intervening text etc Generally, a DbAttributeFormat will be used by a DbAttributeListFormat, which defines how a whole list of attributes is formatted

## Syntax

```csharp
public class DbAttributeFormat
```

## Inheritance

`System.Object` → `Aveva.Pdms.Database.DbAttributeFormat`

## Thread Safety

Public static ( Shared in Visual Basic) members of this type are
safe for multithreaded operations. Instance members are not guaranteed to be
thread-safe.

## Requirements

Namespace:
Aveva.Pdms.Database
Assembly: Aveva.Pdms.Database (in Aveva.Pdms.Database.dll)

## Constructors

#### `DbAttributeFormat` Constructor

Initializes a new instance of the DbAttributeFormat class.

```csharp
public DbAttributeFormat();
```

## Methods

#### `AddItem` Method (DbAttributeField)

Add a field to the format

```csharp
public void AddItem( DbAttributeField field );
```

**Parameters**

- **field** — A field

#### `AddItem` Method (DbAttributeField, DbFieldFormat)

Add a field to the format, specifying the field format

```csharp
public void AddItem( DbAttributeField field , DbFieldFormat fieldformat );
```

**Parameters**

- **field** — A field
- **fieldformat** — Format for the field

#### `AddItem` Method (DbAttributeField, DbFieldFormat, Int32)

Add a field to the format, specifying the field format and mimimum width

```csharp
public void AddItem( DbAttributeField field , DbFieldFormat fieldformat , int width );
```

**Parameters**

- **field** — A field
- **fieldformat** — Format for the field
- **width** — The minimum width of the column

#### `AddItem` Method (DbAttributeField, Int32)

Add a field to the format, specifying the mimimum width

```csharp
public void AddItem( DbAttributeField field , int width );
```

**Parameters**

- **field** — A field
- **width** — The minimum width of the column

#### `AddItem` Method (DbAttributeSpecialField)

Add a special field to the format

```csharp
public void AddItem( DbAttributeSpecialField field );
```

**Parameters**

- **field** — A special field

#### `AddItem` Method (DbAttributeSpecialField, DbFieldFormat)

Add a special field to the format, specifying the field format

```csharp
public void AddItem( DbAttributeSpecialField field , DbFieldFormat fieldformat );
```

**Parameters**

- **field** — A special field
- **fieldformat** — Format for the special field

#### `AddItem` Method (DbAttributeSpecialField, DbFieldFormat, Int32)

Add a special field to the format, specifying the field format and mimimum width

```csharp
public void AddItem( DbAttributeSpecialField field , DbFieldFormat fieldformat , int width );
```

**Parameters**

- **field** — A special field
- **fieldformat** — Format for the special field
- **width** — The minimum width of the column

#### `AddItem` Method (DbAttributeSpecialField, Int32)

Add a special field to the format, specifying the minimum width

```csharp
public void AddItem( DbAttributeSpecialField field , int width );
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

Return a string representing the attribute in the defined format

```csharp
public string Format( DbAttribute att );
```

**Parameters**

- **att** — Attribute to be formatted

**Return Value**

Attribute definition formatted in format defined
