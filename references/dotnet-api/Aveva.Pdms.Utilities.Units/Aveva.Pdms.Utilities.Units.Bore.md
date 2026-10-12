---
title: Aveva.Pdms.Utilities.Units.Bore Class
namespace: Aveva.Pdms.Utilities.Units
assembly: Aveva.Pdms.Utilities
kind: Class
source: Aveva.Pdms.Utilities
---

# Aveva.Pdms.Utilities.Units.Bore Class

> Provides access to Nominal Bore methods.

## Syntax

```csharp
public abstract class Bore
```

## Inheritance

`System.Object` → `Aveva.Pdms.Utilities.Units.Bore`

## Thread Safety

Public static ( Shared in Visual Basic) members of this type are
safe for multithreaded operations. Instance members are not guaranteed to be
thread-safe.

## Requirements

Namespace:
Aveva.Pdms.Utilities.Units
Assembly: Aveva.Pdms.Utilities (in Aveva.Pdms.Utilities.dll)

## Methods

#### `CreateBore` Method

Create a PDMS Bore command.

```csharp
public static Bore CreateBore();
```

**Return Value**

Bore object

#### `NominalBoreValue` Method

```csharp
public abstract double NominalBoreValue( double bore , int hashDimension );
```
