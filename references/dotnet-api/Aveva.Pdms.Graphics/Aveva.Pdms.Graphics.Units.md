---
title: Aveva.Pdms.Graphics.Units Class
namespace: Aveva.Pdms.Graphics
assembly: Aveva.Pdms.Graphics
kind: Class
source: Aveva.Pdms.Graphics
---

# Aveva.Pdms.Graphics.Units Class

> Units formatting.

## Syntax

```csharp
public abstract class Units
```

## Inheritance

`System.Object` → `Aveva.Pdms.Graphics.Units`

## Thread Safety

Public static ( Shared in Visual Basic) members of this type are
safe for multithreaded operations. Instance members are not guaranteed to be
thread-safe.

## Requirements

Namespace:
Aveva.Pdms.Graphics
Assembly: Aveva.Pdms.Graphics (in Aveva.Pdms.Graphics.dll)

## Methods

#### `CreateUnits` Method

```csharp
public static Units CreateUnits();
```

#### `Format` Method

```csharp
public abstract string Format( double value );
```

**Parameters**

- **value** —

#### `GetValue` Method

```csharp
public abstract double GetValue( string input );
```

**Parameters**

- **input** —
