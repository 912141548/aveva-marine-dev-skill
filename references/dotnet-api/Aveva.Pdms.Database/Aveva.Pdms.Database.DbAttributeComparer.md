---
title: Aveva.Pdms.Database.DbAttributeComparer Class
namespace: Aveva.Pdms.Database
assembly: Aveva.Pdms.Database
kind: Class
source: Aveva.Pdms.Database
---

# Aveva.Pdms.Database.DbAttributeComparer Class

> Class to define comparers for ordering lists of attributes. These allow lists of attributes to be sorted on the value of any field. At present, only an alphabetic sort on field values expressed as strings is implemented, although it would be possible to extend this to sort on numerical values. However, as most integers actually represent hash values or enumerations, this may be less useful than it at first sounds!

## Syntax

```csharp
public class DbAttributeComparer : IComparer
```

## Inheritance

`System.Object` → `Aveva.Pdms.Database.DbAttributeComparer`

## Thread Safety

Public static ( Shared in Visual Basic) members of this type are
safe for multithreaded operations. Instance members are not guaranteed to be
thread-safe.

## Requirements

Namespace:
Aveva.Pdms.Database
Assembly: Aveva.Pdms.Database (in Aveva.Pdms.Database.dll)

## Constructors

#### `DbAttributeComparer` Constructor (Overload 1)

Create a new attribute comparer

**Overload List**

Create a new attribute comparer
public DbAttributeComparer(DbAttributeField);
Create a new attribute comparer
public DbAttributeComparer(DbAttributeField,bool);

#### `DbAttributeComparer` Constructor (DbAttributeField, Boolean)

Create a new attribute comparer

```csharp
public DbAttributeComparer( DbAttributeField field , bool reversed );
```

**Parameters**

- **field** — The field to use for comparison
- **reversed** — Whether to reverse comparison. If false (or omitted) comparison is 'less than', so sort order will be ascending. If true, comparison will be 'greater than' and sort order will be descending

#### `DbAttributeComparer` Constructor (DbAttributeField)

Create a new attribute comparer

```csharp
public DbAttributeComparer( DbAttributeField field );
```

**Parameters**

- **field** — The field to use for comparison

## Methods

#### `AddSubKey` Method (DbAttributeField)

Add a further subkey to an existing attribute comparer The subkey will be used to discriminate attributes if (and only if) all previously defined subkeys have returned identical values for the two attributes being compared

```csharp
public void AddSubKey( DbAttributeField field );
```

**Parameters**

- **field** — The field to be used for discriminating comparisons

#### `AddSubKey` Method (DbAttributeField, Boolean)

Add a further subkey to an existing attribute comparer The subkey will be used to discriminate attributes if (and only if) all previously defined subkeys have returned identical values for the two attributes being compared

```csharp
public void AddSubKey( DbAttributeField field , bool reversed );
```

**Parameters**

- **field** — The field to be used for discriminating comparisons
- **reversed** — Whether to reverse comparison. If false (or omitted) comparison is 'less than', so sort order will be ascending. If true, comparison will be 'greater than' and sort order will be descending
