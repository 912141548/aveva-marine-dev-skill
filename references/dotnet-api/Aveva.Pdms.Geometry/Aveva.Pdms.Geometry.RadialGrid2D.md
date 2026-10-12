---
title: Aveva.Pdms.Geometry.RadialGrid2D Class
namespace: Aveva.Pdms.Geometry
assembly: Aveva.Pdms.Geometry
kind: Class
source: Aveva.Pdms.Geometry
---

# Aveva.Pdms.Geometry.RadialGrid2D Class

> Summary description for RadialGrid2D.

## Syntax

```csharp
public abstract class RadialGrid2D
```

## Inheritance

`System.Object` → `Aveva.Pdms.Geometry.RadialGrid2D`

## Thread Safety

Public static ( Shared in Visual Basic) members of this type are
safe for multithreaded operations. Instance members are not guaranteed to be
thread-safe.

## Requirements

Namespace:
Aveva.Pdms.Geometry
Assembly: Aveva.Pdms.Geometry (in Aveva.Pdms.Geometry.dll)

## Properties

#### `Angles` Property

Angular spacing from X axis

```csharp
public abstract double[] Angles {get; set;}
```

#### `Position` Property

Origin of the grid

```csharp
public abstract Position2D Position {get; set;}
```

#### `Radii` Property

Radii of the grid

```csharp
public abstract double[] Radii {get; set;}
```

## Methods

#### `Create` Method ()

Create RadialGrid2D

```csharp
public static RadialGrid2D Create();
```

#### `Create` Method (Position2D, Double[], Double[])

Create a RadialGrid2D

```csharp
public static RadialGrid2D Create( Position2D pos , double[] angles , double[] radii );
```

**Parameters**

- **pos** — 
- **angles** — 
- **radii** —

#### `Equals` Method (RadialGrid2D)

Same RadialGrid2D

```csharp
public abstract bool Equals( RadialGrid2D rg );
```

**Parameters**

- **rg** — 

#### `Equals` Method (Object)

Same RadialGrid2D

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

#### `RadialPosition` Method

Return the nearest grid position of the given radius and angle

```csharp
public abstract Position2D RadialPosition( double radius , double angle );
```

**Parameters**

- **radius** — 
- **angle** —

#### `Snap` Method

Returns nearest grid intersection point to pos

```csharp
public abstract Position2D Snap( Position2D pos );
```

**Parameters**

- **pos** —

#### `ToString` Method

Returns RadialGrid2D property values in a string

```csharp
public abstract string ToString();
```

## Operators

#### `Equality` Operator

Same RadialGrid2D within tolerance

```csharp
public static bool operator ==( RadialGrid2D rg1 , RadialGrid2D rg2 );
```

**Parameters**

- **rg1** — 
- **rg2** —

#### `Inequality` Operator

Not same RadialGrid2D

```csharp
public static bool operator !=( RadialGrid2D rg1 , RadialGrid2D rg2 );
```

**Parameters**

- **rg1** — 
- **rg2** —
