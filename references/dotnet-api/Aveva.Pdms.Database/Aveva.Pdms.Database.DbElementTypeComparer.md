---
title: Aveva.Pdms.Database.DbElementTypeComparer Class
namespace: Aveva.Pdms.Database
assembly: Aveva.Pdms.Database
kind: Class
source: Aveva.Pdms.Database
---

# Aveva.Pdms.Database.DbElementTypeComparer Class

> Class to define comparers for ordering lists of ElementTypes. These allow lists of element types to be sorted on the value of any field. At present, only an alphabetic sort on field values expressed as strings is implemented, although it would be possible to extend this to sort on numerical values. However, as most integers actually represent hash values or enumerations, this may be less useful than it at first sounds!

## Syntax

```csharp
public class DbElementTypeComparer : IComparer
```

## Inheritance

`System.Object` → `Aveva.Pdms.Database.DbElementTypeComparer`

## Thread Safety

Public static ( Shared in Visual Basic) members of this type are
safe for multithreaded operations. Instance members are not guaranteed to be
thread-safe.

## Requirements

Namespace:
Aveva.Pdms.Database
Assembly: Aveva.Pdms.Database (in Aveva.Pdms.Database.dll)

## Constructors

#### `DbElementTypeComparer` Constructor (Overload 1)

Create a new ElementType comparer

**Overload List**

Create a new ElementType comparer
public DbElementTypeComparer(DbNounField);
Create a new ElementType comparer
public DbElementTypeComparer(DbNounField,bool);

#### `DbElementTypeComparer` Constructor (DbNounField, Boolean)

Create a new ElementType comparer

```csharp
public DbElementTypeComparer( DbNounField field , bool reversed );
```

**Parameters**

- **field** — The field to use for comparison
- **reversed** — Whether to reverse comparison. If false (or omitted) comparison is 'less than', so sort order will be ascending. If true, comparison will be 'greater than' and sort order will be descending

#### `DbElementTypeComparer` Constructor (DbNounField)

Create a new ElementType comparer

```csharp
public DbElementTypeComparer( DbNounField field );
```

**Parameters**

- **field** — The field to use for comparison

## Methods

#### `AddSubKey` Method (DbNounField)

Add a further subkey to an existing ElementType comparer The subkey will be used to discriminate ElementTypes if (and only if) all previously defined subkeys have returned identical values for the two ElementTypes being compared

```csharp
public void AddSubKey( DbNounField field );
```

**Parameters**

- **field** — The field to be used for discriminating comparisons

#### `AddSubKey` Method (DbNounField, Boolean)

Add a further subkey to an existing ElementType comparer The subkey will be used to discriminate ElementTypes if (and only if) all previously defined subkeys have returned identical values for the two ElementTypes being compared

```csharp
public void AddSubKey( DbNounField field , bool reversed );
```

**Parameters**

- **field** — The field to be used for discriminating comparisons
- **reversed** — Whether to reverse comparison. If false (or omitted) comparison is 'less than', so sort order will be ascending. If true, comparison will be 'greater than' and sort order will be descending
