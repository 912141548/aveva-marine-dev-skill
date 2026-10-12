---
title: Aveva.Pdms.Geometry.RadialGrid Class
namespace: Aveva.Pdms.Geometry
assembly: Aveva.Pdms.Geometry
kind: Class
source: Aveva.Pdms.Geometry
---

# Aveva.Pdms.Geometry.RadialGrid Class

> Summary description for RadialGrid.

## Syntax

```csharp
public abstract class RadialGrid
```

## Inheritance

`System.Object` → `Aveva.Pdms.Geometry.RadialGrid`

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

#### `Orientation` Property

Orientation of the grid

```csharp
public abstract Orientation Orientation {get; set;}
```

#### `Position` Property

Origin of the grid

```csharp
public abstract Position Position {get; set;}
```

#### `Radii` Property

Radii of the grid

```csharp
public abstract double[] Radii {get; set;}
```

## Methods

#### `Create` Method ()

Create RadialGrid

```csharp
public static RadialGrid Create();
```

#### `Create` Method (Position, Orientation, Double[], Double[])

Create a RadialGrid

```csharp
public static RadialGrid Create( Position pos , Orientation ori , double[] angles , double[] radii );
```

**Parameters**

- **pos** — 
- **ori** — 
- **angles** — 
- **radii** —

#### `Equals` Method (RadialGrid)

Same RadialGrid

```csharp
public abstract bool Equals( RadialGrid rg );
```

**Parameters**

- **rg** — 

#### `Equals` Method (Object)

Same RadialGrid

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
public abstract Position GridPoint( int ix , int iy );
```

**Parameters**

- **ix** — 
- **iy** —

#### `internalCreate` Method ()

Create a RadialGrid

```csharp
public abstract RadialGrid internalCreate();
```

#### `internalCreate` Method (Position, Orientation, Double[], Double[])

Create a RadialGrid

```csharp
public abstract RadialGrid internalCreate( Position pos , Orientation ori , double[] angles , double[] radii );
```

**Parameters**

- **pos** — 
- **ori** — 
- **angles** — 
- **radii** —

#### `RadialPosition` Method

Return the nearest grid position of the given radius and angle

```csharp
public abstract Position RadialPosition( double radius , double angle );
```

**Parameters**

- **radius** — 
- **angle** —

#### `Snap` Method (Line)

Returns nearest grid intersection point to the intersection of line with the plane of the grid

```csharp
public abstract Position Snap( Line line );
```

**Parameters**

- **line** — 

#### `Snap` Method (Position)

Returns nearest grid intersection point to pos

```csharp
public abstract Position Snap( Position pos );
```

**Parameters**

- **pos** —

#### `ToString` Method

Returns RadialGrid property values in a string

```csharp
public abstract string ToString();
```

## Operators

#### `Equality` Operator

Same RadialGrid

```csharp
public static bool operator ==( RadialGrid rg1 , RadialGrid rg2 );
```

**Parameters**

- **rg1** — 
- **rg2** —

#### `Inequality` Operator

Not same RadialGrid

```csharp
public static bool operator !=( RadialGrid rg1 , RadialGrid rg2 );
```

**Parameters**

- **rg1** — 
- **rg2** —
