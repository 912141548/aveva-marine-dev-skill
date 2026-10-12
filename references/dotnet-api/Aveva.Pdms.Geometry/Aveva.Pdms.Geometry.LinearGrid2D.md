---
title: Aveva.Pdms.Geometry.LinearGrid2D Class
namespace: Aveva.Pdms.Geometry
assembly: Aveva.Pdms.Geometry
kind: Class
source: Aveva.Pdms.Geometry
---

# Aveva.Pdms.Geometry.LinearGrid2D Class

> Summary description for LinearGrid2D.

## Syntax

```csharp
public abstract class LinearGrid2D
```

## Inheritance

`System.Object` → `Aveva.Pdms.Geometry.LinearGrid2D`

## Thread Safety

Public static ( Shared in Visual Basic) members of this type are
safe for multithreaded operations. Instance members are not guaranteed to be
thread-safe.

## Requirements

Namespace:
Aveva.Pdms.Geometry
Assembly: Aveva.Pdms.Geometry (in Aveva.Pdms.Geometry.dll)

## Properties

#### `Position` Property

Origin of the grid

```csharp
public abstract Position2D Position {get; set;}
```

#### `XSpacing` Property

Spacing between grid lines in X direction

```csharp
public abstract double XSpacing {get; set;}
```

#### `YSpacing` Property

Spacing between grid lines in Y direction

```csharp
public abstract double YSpacing {get; set;}
```

## Methods

#### `Create` Method ()

Create LinearGrid2D

```csharp
public static LinearGrid2D Create();
```

#### `Create` Method (Position2D, Double, Double)

Create a LinearGrid2D

```csharp
public static LinearGrid2D Create( Position2D pos , double xspacing , double yspacing );
```

**Parameters**

- **pos** — 
- **xspacing** — 
- **yspacing** —

#### `Equals` Method (LinearGrid2D)

Same LinearGrid2D

```csharp
public abstract bool Equals( LinearGrid2D lg );
```

**Parameters**

- **lg** — 

#### `Equals` Method (Object)

Same LinearGrid2D

```csharp
public override bool Equals( object obj );
```

**Parameters**

- **obj** —

#### `GetHashCode` Method

A hash method is used to quickly generate a hash code, which is an int that corresponds to the value of an object. Hash codes allow C# to store objects more efficiently in collections

```csharp
public override int GetHashCode();
```

#### `GridPoint` Method

Returns the position at the (ix,iy) intersection of the grid. If ix or iy are negative, refers to intersections before the origin.

```csharp
public abstract Position2D GridPoint( int ix , int iy );
```

**Parameters**

- **ix** — 
- **iy** —

#### `Snap` Method

Returns nearest grid intersection point to pos

```csharp
public abstract Position2D Snap( Position2D pos );
```

**Parameters**

- **pos** —

#### `SnapToCentre` Method

Return the nearest mesh cell centre point to pos in the grid plane

```csharp
public abstract Position2D SnapToCentre( Position2D pos );
```

**Parameters**

- **pos** —

#### `ToString` Method

Returns LinearGrid2D property values in a string

```csharp
public abstract string ToString();
```

## Operators

#### `Equality` Operator

Same LinearGrid2D within tolerance

```csharp
public static bool operator ==( LinearGrid2D lg1 , LinearGrid2D lg2 );
```

**Parameters**

- **lg1** — 
- **lg2** —

#### `Inequality` Operator

Not same LinearGrid2D

```csharp
public static bool operator !=( LinearGrid2D lg1 , LinearGrid2D lg2 );
```

**Parameters**

- **lg1** — 
- **lg2** —
