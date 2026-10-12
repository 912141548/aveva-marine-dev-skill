---
title: Aveva.Pdms.Maths.Geometry.D3Arc Class
namespace: Aveva.Pdms.Maths.Geometry
assembly: Aveva.Pdms.Maths.Geometry
kind: Class
source: Aveva.Pdms.Maths.Geometry
---

# Aveva.Pdms.Maths.Geometry.D3Arc Class

> A directed 3-D arc

## Syntax

```csharp
public abstract class D3Arc
```

## Inheritance

`System.Object` → `Aveva.Pdms.Maths.Geometry.D3Arc`

## Thread Safety

Public static ( Shared in Visual Basic) members of this type are
safe for multithreaded operations. Instance members are not guaranteed to be
thread-safe.

## Requirements

Namespace:
Aveva.Pdms.Maths.Geometry
Assembly: Aveva.Pdms.Maths.Geometry (in Aveva.Pdms.Maths.Geometry.dll)

## Methods

#### `Centre` Method

Get the centre

```csharp
public abstract D3Point Centre();
```

#### `Clone` Method

Create a copy of a D3Arc

```csharp
public abstract D3Arc Clone();
```

#### `Create` Method ()

Create default arc start(0,0,0),end(0,0,0),centre(0,0,0),radius(0),

```csharp
public static D3Arc Create();
```

#### `Create` Method (D3Arc)

Create copy of arc

```csharp
public static D3Arc Create( D3Arc arc );
```

**Parameters**

- **arc** — 

#### `Create` Method (D3OrientedPlane, Double)

Create a circle from plane and radius

```csharp
public static D3Arc Create( D3OrientedPlane plane , double radius );
```

**Parameters**

- **plane** — 
- **radius** — 

#### `Create` Method (D3Point, D3Point, D3Point)

Create arc through 3 points

```csharp
public static D3Arc Create( D3Point start , D3Point mid , D3Point end );
```

**Parameters**

- **start** — 
- **mid** — 
- **end** — 

#### `Create` Method (D3Point, D3Point, D3Point, Double)

Create an arc from a pole point, 2 points and a radius

```csharp
public static D3Arc Create( D3Point pole , D3Point start , D3Point end , double radius );
```

**Parameters**

- **pole** — 
- **start** — 
- **end** — 
- **radius** —

#### `End` Method

Return the end point of the arc

```csharp
public abstract D3Point End();
```

#### `EndAngle` Method ()

Return the end angle

```csharp
public abstract double EndAngle();
```

#### `EndAngle` Method (Double)

Set the end angle

```csharp
public abstract void EndAngle( double angle );
```

**Parameters**

- **angle** —

#### `EndTangent` Method

Get the tangent at the end of the arc

```csharp
public abstract D3Vector EndTangent();
```

#### `Equals` Method (D3Arc)

Returns true if arcs are equal

```csharp
public abstract bool Equals( D3Arc a );
```

**Parameters**

- **a** — 

#### `Equals` Method (D3Arc, Double)

Returns TRUE if start points, end points, and centre points all match to within distance "tol". The "senses" of the arcs must also be the same.

```csharp
public abstract bool Equals( D3Arc a , double tol );
```

**Parameters**

- **a** — 
- **tol** — 

#### `Equals` Method (Object)

override system default equals method

```csharp
public override bool Equals( object a );
```

**Parameters**

- **a** —

#### `GetHashCode` Method

Override system default gethashcode method

```csharp
public override int GetHashCode();
```

#### `Intersections` Method (D3Arc, D3Point, D3Point)

Return true if arcs intersect Intersection points are returned in pa and pb

```csharp
public abstract bool Intersections( D3Arc a , D3Point pa , D3Point pb );
```

#### `Intersections` Method (D3FiniteLine, D3Point, D3Point)

Return true if arc intersects the (finite) line (The line is projected onto the plane of the arc) Intersection points are returned in pa and pb

```csharp
public abstract bool Intersections( D3FiniteLine lin , D3Point pa , D3Point pb );
```

#### `Intersections` Method (D3OrientedPlane, D3Point, D3Point)

Return true if arc intersects the given plane Intersection points are returned in pa and pb

```csharp
public abstract bool Intersections( D3OrientedPlane plan , D3Point pa , D3Point pb );
```

#### `InValid` Method

Return true if arc is invalid

```csharp
public abstract bool InValid();
```

#### `IsAnticlockwise` Method

Return the sense of the arc

```csharp
public abstract bool IsAnticlockwise();
```

#### `IsCircle` Method

Returns true if the arc is a full circle

```csharp
public abstract bool IsCircle();
```

#### `IsOnArc` Method

Return true if point lies on arc

```csharp
public abstract bool IsOnArc( D3Point p );
```

#### `Mid` Method

Return the mid point of the arc between the start and end points

```csharp
public abstract D3Point Mid();
```

#### `OrientedPlane` Method ()

return the oriented plane

```csharp
public abstract D3OrientedPlane OrientedPlane();
```

#### `OrientedPlane` Method (D3OrientedPlane)

set the oriented plane

```csharp
public abstract void OrientedPlane( D3OrientedPlane plane );
```

**Parameters**

- **plane** —

#### `Position` Method

Return the position at given angle on arc

```csharp
public abstract D3Point Position( double angle );
```

**Parameters**

- **angle** —

#### `Radius` Method ()

Return the radius

```csharp
public abstract double Radius();
```

#### `Radius` Method (Double)

Set the radius

```csharp
public abstract void Radius( double rad );
```

**Parameters**

- **rad** —

#### `SetAnticlockwise` Method

Set the sense of the arc

```csharp
public abstract void SetAnticlockwise( bool isAnticlock );
```

**Parameters**

- **isAnticlock** —

#### `Start` Method

Return the first point of the arc

```csharp
public abstract D3Point Start();
```

#### `StartAngle` Method ()

Return the start angle

```csharp
public abstract double StartAngle();
```

#### `StartAngle` Method (Double)

Set the start angle

```csharp
public abstract void StartAngle( double angle );
```

**Parameters**

- **angle** —

#### `StartTangent` Method

Get the tangent at the start of the arc

```csharp
public abstract D3Vector StartTangent();
```

#### `Tangent` Method

Get the tangent at given angle on arc

```csharp
public abstract D3Vector Tangent( double angle );
```

**Parameters**

- **angle** —

#### `TangentPoints` Method

Return true if tangents drawn from the given point to the arc exist (The given point is projected onto the plane of the arc) The points of contact are returned in pa and pb

```csharp
public abstract bool TangentPoints( D3Point pIn , D3Point pa , D3Point pb );
```

#### `ToString` Method

Returns a string describing the contents of the D3Arc

```csharp
public abstract string ToString();
```

## Operators

#### `Equality` Operator

equality operator

```csharp
public static bool operator ==( D3Arc left , D3Arc right );
```

**Parameters**

- **left** — 
- **right** —

#### `Inequality` Operator

inequality operator

```csharp
public static bool operator !=( D3Arc left , D3Arc right );
```

**Parameters**

- **left** — 
- **right** —
