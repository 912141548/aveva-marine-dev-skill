---
title: Aveva.Pdms.Database.DbElementTypeListFormat Class
namespace: Aveva.Pdms.Database
assembly: Aveva.Pdms.Database
kind: Class
source: Aveva.Pdms.Database
---

# Aveva.Pdms.Database.DbElementTypeListFormat Class

> Class to define an object to format a list of DbElementTypes. Each individual DbElementType is formatted by the DbElementTypeFormat specified, and other aspects of the overall presentation (line breaks etc) are controlled by other properties of the DbElementTypeListFormat

## Syntax

```csharp
public class DbElementTypeListFormat
```

## Inheritance

`System.Object` → `Aveva.Pdms.Database.DbElementTypeListFormat`

## Thread Safety

Public static ( Shared in Visual Basic) members of this type are
safe for multithreaded operations. Instance members are not guaranteed to be
thread-safe.

## Requirements

Namespace:
Aveva.Pdms.Database
Assembly: Aveva.Pdms.Database (in Aveva.Pdms.Database.dll)

## Constructors

#### `DbElementTypeListFormat` Constructor (Overload 1)

Create a new DbElementTypeListFormat. Each individual DbElementType is formatted by the specified DbElementTypeFormat, and a new line is added after each

**Overload List**

Create a new DbElementTypeListFormat. Each individual DbElementType is formatted by the specified DbElementTypeFormat, and a new line is added after each
public DbElementTypeListFormat(DbElementTypeFormat);
Create a new DbElementTypeListFormat. Each individual DbElementType is formatted by the specified DbElementTypeFormat, and the specified text is added after each
public DbElementTypeListFormat(DbElementTypeFormat,string);

#### `DbElementTypeListFormat` Constructor (DbElementTypeFormat)

Create a new DbElementTypeListFormat. Each individual DbElementType is formatted by the specified DbElementTypeFormat, and a new line is added after each

```csharp
public DbElementTypeListFormat( DbElementTypeFormat nounformat );
```

**Parameters**

- **nounformat** — 

#### `DbElementTypeListFormat` Constructor (DbElementTypeFormat, String)

Create a new DbElementTypeListFormat. Each individual DbElementType is formatted by the specified DbElementTypeFormat, and the specified text is added after each

```csharp
public DbElementTypeListFormat( DbElementTypeFormat nounformat , string text_after_noun );
```

**Parameters**

- **nounformat** — 
- **text_after_noun** —

## Properties

#### `BreakCount` Property

Gets or sets the number of DbElementTypes to be output before the BreakText is inserted. This allows, for example, a number of DbElementTypes to be output on the same line, or a blank line to be inserted after every 'n' DbElementTypes to aid readability. Note that the counter is reset by a SplitField. A value of 0 indicates that no such breaks are required.

```csharp
public int BreakCount {get; set;}
```

#### `BreakText` Property

Gets or sets the text to be output after ever BreakCount lines within a section, e.g. a new line (if putting several DbElementTypes on the same line) or an additional new line (if adding a blank line after every 'n' attributes). This is not used if BreakCount is set to 0 (the default).

```csharp
public string BreakText {get; set;}
```

#### `ElementTypeFormat` Property

Gets or sets the DbElementTypeFormat to be used for each individual DbElementType

```csharp
public DbElementTypeFormat ElementTypeFormat {get; set;}
```

#### `IncludeSplitFieldName` Property

Gets or sets whether or not the new value of the SplitField will be output whenever this changes between one DbElementType and the next. This is not used if the SplitField has not been set. If true, the new value of the field is output between the 'TextBeforeSplitFieldName' and 'TextAfterSplitFieldName'

```csharp
public bool IncludeSplitFieldName {get; set;}
```

#### `SplitField` Property

Gets or sets a field to use as the split value; whenever the value of this field changes between one DbElementType and the next, the 'TextBeforeSplitFieldName', the new value of the field (optional), and the 'TextAfterSplitFieldName' are inserted into the output

```csharp
public DbNounField SplitField {get; set;}
```

#### `TextAfterElementType` Property

Gets or sets the text to be inserted after each individual DbElementType (e.g. a new line character)

```csharp
public string TextAfterElementType {get; set;}
```

#### `TextAfterSplitFieldName` Property

Gets or sets the text to be inserted after the field value whenever the value of the specified field changes between one DbElementType and the next. This is not used if the SplitField has not been set. Note that this text is still output even if 'IncludeSplitFieldName' is false so that the actual split field value itself is not.

```csharp
public string TextAfterSplitFieldName {get; set;}
```

#### `TextAtEnd` Property

Gets or sets the text to be output after the final DbElementType in the list

```csharp
public string TextAtEnd {get; set;}
```

#### `TextAtStart` Property

Gets or sets the text to be inserted at the start of the formatted output (e.g. a header)

```csharp
public string TextAtStart {get; set;}
```

#### `TextBeforeElementType` Property

Gets or sets the text to be inserted before each individual DbElementType

```csharp
public string TextBeforeElementType {get; set;}
```

#### `TextBeforeSplitFieldName` Property

Gets or sets the text to be inserted before the field value whenever the value of the specified field changes between one DbElementType and the next. This is not used if the SplitField has not been set. Note that this text is still output even if 'IncludeSplitFieldName' is false so that the actual split field value itself is not.

```csharp
public string TextBeforeSplitFieldName {get; set;}
```

## Methods

#### `Format` Method

Formats a DbElementTypeList in the style specified

```csharp
public string Format( DbElementTypeList mylist );
```

**Parameters**

- **mylist** — The DbElementTypeList to be formatted

**Return Value**

A string representing the DbElementTypeList in the required format
