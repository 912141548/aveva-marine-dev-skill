---
title: Aveva.Pdms.Maths.Geometry.D3FiniteLine Class
namespace: Aveva.Pdms.Maths.Geometry
assembly: Aveva.Pdms.Maths.Geometry
kind: Class
source: Aveva.Pdms.Maths.Geometry
---

# Aveva.Pdms.Maths.Geometry.D3FiniteLine Class

> Finite line in 3D space

## Syntax

```csharp
public abstract class D3FiniteLine
```

## Inheritance

`System.Object` → `Aveva.Pdms.Maths.Geometry.D3FiniteLine`

## Thread Safety

Public static ( Shared in Visual Basic) members of this type are
safe for multithreaded operations. Instance members are not guaranteed to be
thread-safe.

## Requirements

Namespace:
Aveva.Pdms.Maths.Geometry
Assembly: Aveva.Pdms.Maths.Geometry (in Aveva.Pdms.Maths.Geometry.dll)

## Methods

#### `Antiparallel` Method (D3FiniteLine)

Returns True if lines point in OPPOSITE DIRECTIONS within default tolerance

```csharp
public abstract bool Antiparallel( D3FiniteLine f );
```

**Parameters**

- **f** — 

#### `Antiparallel` Method (D3FiniteLine, Double)

Returns True if lines point in OPPOSITE DIRECTIONS within tolerance tol in Radians

```csharp
public abstract bool Antiparallel( D3FiniteLine f , double tol );
```

**Parameters**

- **f** — 
- **tol** —

#### `AzimuthalAngleInRadians` Method

azimuthal angle of direction vector of line measured wrt z-direction

```csharp
public abstract double AzimuthalAngleInRadians();
```

#### `Box` Method

Return box that encloses line

```csharp
public abstract D3Limits Box();
```

#### `CheckLength` Method ()

Returns true if length is greater than default tolerance

```csharp
public abstract bool CheckLength();
```

#### `CheckLength` Method (Double)

True if length is greater than tol

```csharp
public abstract bool CheckLength( double tol );
```

**Parameters**

- **tol** —

#### `Clone` Method

deep copy

```csharp
public abstract D3FiniteLine Clone();
```

#### `Coplanar` Method (D3FiniteLine)

Returns TRUE if lines lie in the same plane Returns TRUE If lines are PARALLEL or ANTIPARALLEL. N.B. uses parallel(FiniteLine,tol) and antparallel(FiniteLine,tol) functions with given tolerance. For non-parallel lines- this routine works by finding these two vectors- A: the vector connecting the two start points B: the vector product of the two line directions If the angle between these two lines is PI radians (within default tolerance), then TRUE will be returned. If either input line is less than fl_TOLERANCE in length FALSE will be returned

```csharp
public abstract bool Coplanar( D3FiniteLine f );
```

**Parameters**

- **f** — 

#### `Coplanar` Method (D3FiniteLine, Double)

Returns TRUE if lines lie in the same plane Returns TRUE If lines are PARALLEL or ANTIPARALLEL. N.B. uses parallel(FiniteLine,tol) and antparallel(FiniteLine,tol) functions with given tolerance. For non-parallel lines- this routine works by finding these two vectors- A: the vector connecting the two start points B: the vector product of the two line directions If the angle between these two lines is PI radians (within tolerance tol), then TRUE will be returned. If either input line is less than fl_TOLERANCE in length FALSE will be returned

```csharp
public abstract bool Coplanar( D3FiniteLine f , double tol );
```

**Parameters**

- **f** — 
- **tol** —

#### `Create` Method ()

default constructor ( zero length line at origin)

```csharp
public static D3FiniteLine Create();
```

#### `Create` Method (D3Point, D3Point)

construct from start and end points

```csharp
public static D3FiniteLine Create( D3Point start , D3Point end );
```

**Parameters**

- **start** — 
- **end** — 

#### `Create` Method (Double, Double, Double, Double, Double, Double)

construct from start and end coordinates

```csharp
public static D3FiniteLine Create( double x1 , double y1 , double z1 , double x2 , double y2 , double z2 );
```

**Parameters**

- **x1** — 
- **y1** — 
- **z1** — 
- **x2** — 
- **y2** — 
- **z2** —

#### `Direction` Method

return direction vector (end - start)

```csharp
public abstract D3Vector Direction();
```

#### `DistanceFrom` Method

Shortest distance from line to point. Line treated as FINITE Returns distance from point

```csharp
public abstract double DistanceFrom( D3Point pt );
```

**Parameters**

- **pt** —

#### `DistanceFromOrigin` Method

Shortest distance from line to origin. Line treated as FINITE

```csharp
public abstract double DistanceFromOrigin();
```

#### `End` Method ()

Return the end point

```csharp
public abstract D3Point End();
```

#### `End` Method (D3Point)

set end point

```csharp
public abstract void End( D3Point end );
```

**Parameters**

- **end** — 

#### `End` Method (Double, Double, Double)

set coordinate values of end point

```csharp
public abstract void End( double x , double y , double z );
```

**Parameters**

- **x** — 
- **y** — 
- **z** —

#### `Equals` Method (D3FiniteLine)

Test for equality

```csharp
public abstract bool Equals( D3FiniteLine d2 );
```

**Parameters**

- **d2** — 

#### `Equals` Method (Object)

```csharp
public override bool Equals( object obj );
```

**Parameters**

- **obj** —

#### `GetHashCode` Method

```csharp
public override int GetHashCode();
```

#### `InterPoint` Method

Returns an intermediate point along the line (Note: it'll be off the end if |t| > 1)

```csharp
public abstract D3Point InterPoint( double t );
```

**Parameters**

- **t** —

#### `Length` Method

Return the length of the line

```csharp
public abstract double Length();
```

#### `Middle` Method

Return the mid point of the line

```csharp
public abstract D3Point Middle();
```

#### `MirrorX` Method ()

Mirror X about origin

```csharp
public abstract void MirrorX();
```

#### `MirrorX` Method (D3Point)

Mirror X about pivot

```csharp
public abstract void MirrorX( D3Point pivot );
```

**Parameters**

- **pivot** —

#### `MirrorY` Method ()

Mirror Y about origin

```csharp
public abstract void MirrorY();
```

#### `MirrorY` Method (D3Point)

Mirror Y about pivot

```csharp
public abstract void MirrorY( D3Point pivot );
```

**Parameters**

- **pivot** —

#### `MirrorZ` Method ()

Mirror Z about origin

```csharp
public abstract void MirrorZ();
```

#### `MirrorZ` Method (D3Point)

Mirror Z about pivot

```csharp
public abstract void MirrorZ( D3Point pivot );
```

**Parameters**

- **pivot** —

#### `MoveBy` Method

Move line by given vector

```csharp
public abstract void MoveBy( D3Vector v );
```

**Parameters**

- **v** —

#### `NearestPoint` Method

Returns point ON FINITE line nearest given point pt

```csharp
public abstract D3Point NearestPoint( D3Point pt );
```

**Parameters**

- **pt** —

#### `NearestPointToOrigin` Method

Returns point on line closest to origin

```csharp
public abstract D3Point NearestPointToOrigin();
```

#### `OnLine` Method (D3Point)

True if point lies on the line (within default tolerance )

```csharp
public abstract bool OnLine( D3Point p );
```

**Parameters**

- **p** — 

#### `OnLine` Method (D3Point, Double)

True if point lies on the line (within tolerance tol)

```csharp
public abstract bool OnLine( D3Point p , double tol );
```

**Parameters**

- **p** — 
- **tol** —

#### `Parallel` Method (D3FiniteLine)

true if lines point in the SAME DIRECTION (within default tolerance) Tolerance is max angle between the directions measured in RADIANS N.B. will return FALSE for antiparallel lines.

```csharp
public abstract bool Parallel( D3FiniteLine f );
```

**Parameters**

- **f** — 

#### `Parallel` Method (D3FiniteLine, Double)

true if lines point in the SAME DIRECTION (within tolerance tol) Tolerance is max angle between the directions measured in RADIANS N.B. will return FALSE for antiparallel lines.

```csharp
public abstract bool Parallel( D3FiniteLine f , double tol );
```

**Parameters**

- **f** — 
- **tol** —

#### `PerpendicularDistance` Method

Distance of the given point from the perpendicularPoint() calculated using NearestPoint function.

```csharp
public abstract double PerpendicularDistance( D3Point point );
```

**Parameters**

- **point** —

#### `PerpendicularPoint` Method

Returns the point on the INFINITELY EXTENDED line from which a perpendicular line can be dropped onto the argument point

```csharp
public abstract D3Point PerpendicularPoint( D3Point point );
```

**Parameters**

- **point** —

#### `PolarAngleInRadians` Method

polar angle of direction vector of line

```csharp
public abstract double PolarAngleInRadians();
```

#### `Reverse` Method

swap start and end points

```csharp
public abstract void Reverse();
```

#### `ScaleBy` Method (Double)

scale uniformly by given value

```csharp
public abstract void ScaleBy( double s );
```

**Parameters**

- **s** — 

#### `ScaleBy` Method (Double, D3Point)

Scale by given value about pivot

```csharp
public abstract void ScaleBy( double s , D3Point pivot );
```

**Parameters**

- **s** — 
- **pivot** —

#### `SetValue` Method (D3Point, D3Point)

set start and end points

```csharp
public abstract void SetValue( D3Point start , D3Point end );
```

**Parameters**

- **start** — 
- **end** — 

#### `SetValue` Method (Double, Double, Double, Double, Double, Double)

set start and end points to given coordinate values

```csharp
public abstract void SetValue( double x1 , double y1 , double z1 , double x2 , double y2 , double z2 );
```

**Parameters**

- **x1** — 
- **y1** — 
- **z1** — 
- **x2** — 
- **y2** — 
- **z2** —

#### `Start` Method ()

Return the start point

```csharp
public abstract D3Point Start();
```

#### `Start` Method (D3Point)

set start point

```csharp
public abstract void Start( D3Point start );
```

**Parameters**

- **start** — 

#### `Start` Method (Double, Double, Double)

set coordinate values of start

```csharp
public abstract void Start( double x , double y , double z );
```

**Parameters**

- **x** — 
- **y** — 
- **z** —

#### `ToString` Method

Return string containing description of D3FiniteLine

```csharp
public abstract string ToString();
```

#### `TValue` Method

Distance of point p from start point of line in the direction of the line. The distance is returned in units such that one line length = 1 unit. So tValue > 1 -> point lies beyond end of line tValue < 0 -> point lies before start of line 0 <= tValue <= 1 -> can drop a perpendicular from line to point ie. point lies between ends of line

```csharp
public abstract double TValue( D3Point p );
```

**Parameters**

- **p** —

#### `UnitDirection` Method

Return unit direction vector

```csharp
public abstract D3Vector UnitDirection();
```

## Operators

#### `Equality` Operator

invoked by left == right True if start and end points match exaclty

```csharp
public static bool operator ==( D3FiniteLine left , D3FiniteLine right );
```

**Parameters**

- **left** — 
- **right** —

#### `Inequality` Operator

invoked by left != right True if either start or end point does not match exactly

```csharp
public static bool operator !=( D3FiniteLine left , D3FiniteLine right );
```

**Parameters**

- **left** — 
- **right** —
