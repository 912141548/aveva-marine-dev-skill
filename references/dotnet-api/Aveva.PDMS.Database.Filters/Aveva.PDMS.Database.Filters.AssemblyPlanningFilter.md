---
title: Aveva.PDMS.Database.Filters.AssemblyPlanningFilter Class
namespace: Aveva.PDMS.Database.Filters
assembly: PDMSFilters
kind: Class
source: Aveva.Pdms.Database.Filters
---

# Aveva.PDMS.Database.Filters.AssemblyPlanningFilter Class

> Summary description for AssemblyPlanningFliter.

## Syntax

```csharp
public class AssemblyPlanningFilter : BaseFilter
```

## Inheritance

`System.Object` → `Aveva.PDMS.Database.Filters.BaseFilter` → `Aveva.PDMS.Database.Filters.AssemblyPlanningFilter`

## Thread Safety

Public static ( Shared in Visual Basic) members of this type are
safe for multithreaded operations. Instance members are not guaranteed to be
thread-safe.

## Requirements

Namespace:
Aveva.PDMS.Database.Filters
Assembly: PDMSFilters (in PDMSFilters.dll)

## Constructors

#### `AssemblyPlanningFilter` Constructor

Initializes a new instance of the AssemblyPlanningFilter class.

```csharp
public AssemblyPlanningFilter();
```

## Methods

#### `Clone` Method

```csharp
public override object Clone();
```

**Implements**

ICloneable.Clone

#### `Equals` Method

```csharp
public override bool Equals( object o );
```

#### `GetHashCode` Method

```csharp
public override int GetHashCode();
```

#### `ScanBelow` Method

```csharp
public override bool ScanBelow( DbElement ele );
```

#### `Valid` Method

```csharp
public override bool Valid( DbElement ele );
```
