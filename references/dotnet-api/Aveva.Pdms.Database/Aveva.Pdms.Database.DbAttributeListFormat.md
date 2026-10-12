---
title: Aveva.Pdms.Database.DbAttributeListFormat Class
namespace: Aveva.Pdms.Database
assembly: Aveva.Pdms.Database
kind: Class
source: Aveva.Pdms.Database
---

# Aveva.Pdms.Database.DbAttributeListFormat Class

> Class to define an object to format a list of attributes. Each individual attribute is formatted by the DbAttributeFormat specified, and other aspects of the overall presentation (line breaks etc) are controlled by other properties of the DbAttributeListFormat

## Syntax

```csharp
public class DbAttributeListFormat
```

## Inheritance

`System.Object` → `Aveva.Pdms.Database.DbAttributeListFormat`

## Thread Safety

Public static ( Shared in Visual Basic) members of this type are
safe for multithreaded operations. Instance members are not guaranteed to be
thread-safe.

## Requirements

Namespace:
Aveva.Pdms.Database
Assembly: Aveva.Pdms.Database (in Aveva.Pdms.Database.dll)

## Constructors

#### `DbAttributeListFormat` Constructor (Overload 1)

Create a new attribute list format. Each individual attribute is formatted by the specified attribute formatter, and a new line is added after each

**Overload List**

Create a new attribute list format. Each individual attribute is formatted by the specified attribute formatter, and a new line is added after each
public DbAttributeListFormat(DbAttributeFormat);
Create a new attribute list format. Each individual attribute is formatted by the specified attribute formatter, and the specified text is added after each
public DbAttributeListFormat(DbAttributeFormat,string);

#### `DbAttributeListFormat` Constructor (DbAttributeFormat)

Create a new attribute list format. Each individual attribute is formatted by the specified attribute formatter, and a new line is added after each

```csharp
public DbAttributeListFormat( DbAttributeFormat attformat );
```

**Parameters**

- **attformat** — The attribute formatted to use for each individual attribute

#### `DbAttributeListFormat` Constructor (DbAttributeFormat, String)

Create a new attribute list format. Each individual attribute is formatted by the specified attribute formatter, and the specified text is added after each

```csharp
public DbAttributeListFormat( DbAttributeFormat attformat , string text_after_attribute );
```

**Parameters**

- **attformat** — The attribute formatter to use for each individual attribute
- **text_after_attribute** — The text to be added after each individual attribute

## Properties

#### `AttributeFormat` Property

Gets or sets the attribute format to be used for each individual attribute

```csharp
public DbAttributeFormat AttributeFormat {get; set;}
```

#### `BreakCount` Property

Gets or sets the number of attributes to be output before the BreakText is inserted. This allows, for example, a number of attributes to be output on the same line, or a blank line to be inserted after every 'n' attributes to aid readability. Note that the counter is reset by a SplitField. A value of 0 indicates that no such breaks are required.

```csharp
public int BreakCount {get; set;}
```

#### `BreakText` Property

Gets or sets the text to be output after ever BreakCount lines within a section, e.g. a new line (if putting several attributes on the same line) or an additional new line (if adding a blank line after every 'n' attributes). This is not used if BreakCount is set to 0 (the default).

```csharp
public string BreakText {get; set;}
```

#### `IncludeSplitFieldName` Property

Gets or sets whether or not the new value of the SplitField will be output whenever this changes between one attribute and the next. This is not used if the SplitField has not been set. If true, the new value of the field is output between the 'TextBeforeSplitFieldName' and 'TextAfterSplitFieldName'

```csharp
public bool IncludeSplitFieldName {get; set;}
```

#### `SplitField` Property

Gets or sets a field to use as the split value; whenever the value of this field changes between one attribute and the next, the 'TextBeforeSplitFieldName', the new value of the field (optional), and the 'TextAfterSplitFieldName' are inserted into the output

```csharp
public DbAttributeField SplitField {get; set;}
```

#### `TextAfterAttribute` Property

Gets or sets the text to be inserted after each individual attribute (e.g. a new line character)

```csharp
public string TextAfterAttribute {get; set;}
```

#### `TextAfterSplitFieldName` Property

Gets or sets the text to be inserted after the field name whenever the value of the specified field changes between one attribute and the next. This is not used if the SplitField has not been set. Note that this text is still output even if 'IncludeSplitFieldName' is false so that the actual split field value itself is not.

```csharp
public string TextAfterSplitFieldName {get; set;}
```

#### `TextAtEnd` Property

Gets or sets the text to be output after the final attribute in the list

```csharp
public string TextAtEnd {get; set;}
```

#### `TextAtStart` Property

Gets or sets the text to be inserted at the start of the formatted output (e.g. a header)

```csharp
public string TextAtStart {get; set;}
```

#### `TextBeforeAttribute` Property

Gets or sets the text to be inserted before each individual attribute

```csharp
public string TextBeforeAttribute {get; set;}
```

#### `TextBeforeSplitFieldName` Property

Gets or sets the text to be inserted before the field name whenever the value of the specified field changes between one attribute and the next. This is not used if the SplitField has not been set. Note that this text is still output even if 'IncludeSplitFieldName' is false so that the actual split field value itself is not.

```csharp
public string TextBeforeSplitFieldName {get; set;}
```

## Methods

#### `Format` Method

Formats a DbAttributeList in the style specified

```csharp
public string Format( DbAttributeList mylist );
```

**Parameters**

- **mylist** — The DbAttributeList to be formatted

**Return Value**

A string representing the DbAttributeList in the required format
