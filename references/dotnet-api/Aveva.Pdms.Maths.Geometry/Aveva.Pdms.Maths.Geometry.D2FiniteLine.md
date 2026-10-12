---
title: Aveva.Pdms.Maths.Geometry.D2FiniteLine Class
namespace: Aveva.Pdms.Maths.Geometry
assembly: Aveva.Pdms.Maths.Geometry
kind: Class
source: Aveva.Pdms.Maths.Geometry
---

# Aveva.Pdms.Maths.Geometry.D2FiniteLine Class

> Finite line

## Syntax

```csharp
public abstract class D2FiniteLine
```

## Inheritance

`System.Object` → `Aveva.Pdms.Maths.Geometry.D2FiniteLine`

## Thread Safety

Public static ( Shared in Visual Basic) members of this type are
safe for multithreaded operations. Instance members are not guaranteed to be
thread-safe.

## Requirements

Namespace:
Aveva.Pdms.Maths.Geometry
Assembly: Aveva.Pdms.Maths.Geometry (in Aveva.Pdms.Maths.Geometry.dll)

## Methods

#### `Antiparallel` Method (D2FiniteLine)

Returns true if lines point in OPPOSITE DIRECTIONS (to default tolerance)

```csharp
public abstract bool Antiparallel( D2FiniteLine fline );
```

**Parameters**

- **fline** — 

#### `Antiparallel` Method (D2FiniteLine, Double)

Returns true if lines point in OPPOSITE DIRECTIONS (to given tolerance)

```csharp
public abstract bool Antiparallel( D2FiniteLine fline , double tolerance );
```

**Parameters**

- **fline** — 
- **tolerance** —

#### `Box` Method

Return 2-D limits box that encloses line

```csharp
public abstract D2Limits Box();
```

#### `CheckLength` Method ()

Returns true if length is greater than default tolerance

```csharp
public abstract bool CheckLength();
```

#### `CheckLength` Method (Double)

Returns true if length is greater than given tolerance

```csharp
public abstract bool CheckLength( double tolerance );
```

**Parameters**

- **tolerance** —

#### `Clone` Method

```csharp
public abstract D2FiniteLine Clone();
```

#### `Create` Method ()

Default constructor

```csharp
public static D2FiniteLine Create();
```

#### `Create` Method (D2FiniteLine)

Copy finiteline

```csharp
public static D2FiniteLine Create( D2FiniteLine fline );
```

**Parameters**

- **fline** — 

#### `Create` Method (D2Point, D2Point)

construct from start and end points

```csharp
public static D2FiniteLine Create( D2Point start , D2Point end );
```

**Parameters**

- **start** — 
- **end** — 

#### `Create` Method (Double, Double, Double, Double)

construct from start and end coordinates

```csharp
public static D2FiniteLine Create( double x1 , double y1 , double x2 , double y2 );
```

**Parameters**

- **x1** — 
- **y1** — 
- **x2** — 
- **y2** —

#### `Direction` Method

Return direction vector of line (end - start)

```csharp
public abstract D2Vector Direction();
```

#### `DistanceFrom` Method (D2FiniteLine)

Returns shortest distance from finite line to finite line Returns 0 if lines cross

```csharp
public abstract double DistanceFrom( D2FiniteLine fline );
```

**Parameters**

- **fline** — Finite line

#### `DistanceFrom` Method (D2Point)

Returns the shortest distance from finit line to given point.

```csharp
public abstract double DistanceFrom( D2Point p );
```

**Parameters**

- **p** —

#### `DistanceFromOrigin` Method

Returns the shortest distance from finite line to origin

```csharp
public abstract double DistanceFromOrigin();
```

#### `End` Method ()

Return end point of the finite line

```csharp
public abstract D2Point End();
```

#### `End` Method (D2Point)

Set end point

```csharp
public abstract void End( D2Point beta );
```

**Parameters**

- **beta** — 

#### `End` Method (Double, Double)

Set coordinates of end point

```csharp
public abstract void End( double x , double y );
```

**Parameters**

- **x** — 
- **y** —

#### `Equals` Method (D2FiniteLine)

Test for equality

```csharp
public abstract bool Equals( D2FiniteLine d2 );
```

**Parameters**

- **d2** — 

#### `Equals` Method (Object)

required override of Equals() when we define operator ==

```csharp
public override bool Equals( object a );
```

**Parameters**

- **a** — 

**Return Value**

bool

#### `GetHashCode` Method

required override of GetHashCode() when we define operator ==

```csharp
public override int GetHashCode();
```

**Return Value**

int

#### `InterPoint` Method

Returns an intermediate point along the line proportion t from start (note - it'll be off the end if |t| > 1)

```csharp
public abstract D2Point InterPoint( double t );
```

**Parameters**

- **t** —

#### `Intersects` Method

Returns TRUE if lines are not parallel or anti parallel and both lines are of meaningful length (>1.E-6). Intersection point is returned through argument but is unchanged for non-intersecting lines. The Intersection point returned is the point the lines would cross if they were BOTH INFINITE. use the onLine(D2Point, double tol) method to determine if this intersection lies on one or both lines (within tolerance) N.B. use return value to check for intersection otherwise you'll get confused when lines really do cross at input value of "intersection" point

```csharp
public abstract bool Intersects( D2FiniteLine line , D2Point intersection );
```

**Parameters**

- **line** — 
- **intersection** —

#### `Length` Method

Return length of line

```csharp
public abstract double Length();
```

#### `Middle` Method

Return mid point of the finite line

```csharp
public abstract D2Point Middle();
```

#### `MirrorX` Method ()

Reflect line about origin in X

```csharp
public abstract void MirrorX();
```

#### `MirrorX` Method (D2Point)

Reflect line about Y using pivot point

```csharp
public abstract void MirrorX( D2Point pivot );
```

**Parameters**

- **pivot** —

#### `MirrorY` Method ()

Reflect line about origin in Y

```csharp
public abstract void MirrorY();
```

#### `MirrorY` Method (D2Point)

Reflect line about Y using pivot point

```csharp
public abstract void MirrorY( D2Point pivot );
```

**Parameters**

- **pivot** —

#### `MoveBy` Method

Move line by vector

```csharp
public abstract void MoveBy( D2Vector v );
```

**Parameters**

- **v** —

#### `NearestPoint` Method

Return point on finite line closes to the given point

```csharp
public abstract D2Point NearestPoint( D2Point point );
```

**Parameters**

- **point** —

#### `NearestPointToOrigin` Method

Returns point on finite line closest to origin

```csharp
public abstract D2Point NearestPointToOrigin();
```

#### `OnLine` Method (D2Point)

Returns true if point is on line (within default tolerance)

```csharp
public abstract bool OnLine( D2Point p );
```

**Parameters**

- **p** — 

#### `OnLine` Method (D2Point, Double)

Returns true if point is on line (within given tolerance)

```csharp
public abstract bool OnLine( D2Point p , double tolp );
```

**Parameters**

- **p** — 
- **tolp** —

#### `Parallel` Method (D2FiniteLine)

Returns true if lines point in the SAME DIRECTION (to default tolerance)

```csharp
public abstract bool Parallel( D2FiniteLine fline );
```

**Parameters**

- **fline** — 

#### `Parallel` Method (D2FiniteLine, Double)

Returns true if lines point in the SAME DIRECTION (to given tolerance)

```csharp
public abstract bool Parallel( D2FiniteLine fline , double tolerance );
```

**Parameters**

- **fline** — 
- **tolerance** —

#### `PerpendicularDistance` Method

Returns the Distance of the given point from the perpendicularPoint() calculated using NearestPoint function .

```csharp
public abstract double PerpendicularDistance( D2Point point );
```

**Parameters**

- **point** —

#### `PerpendicularPoint` Method

Returns the point on the INFINITELY EXTENDED line from which a perpendicular line can be dropped onto the given point

```csharp
public abstract D2Point PerpendicularPoint( D2Point point );
```

**Parameters**

- **point** —

#### `PolarAngleInRadians` Method

Returns the polar angle of direction of line (in radians)

```csharp
public abstract double PolarAngleInRadians();
```

#### `Reverse` Method

Swap start and end points

```csharp
public abstract void Reverse();
```

#### `RotateByDegrees` Method (Double)

Rotate line about origin by given angle (in degrees)

```csharp
public abstract void RotateByDegrees( double ang );
```

**Parameters**

- **ang** — 

#### `RotateByDegrees` Method (Double, D2Point)

Rotate line about pivot point by given amount (in degrees)

```csharp
public abstract void RotateByDegrees( double ang , D2Point pivot );
```

**Parameters**

- **ang** — 
- **pivot** —

#### `RotateByRadians` Method (Double)

Rotate line about origin by given angle in radians

```csharp
public abstract void RotateByRadians( double ang );
```

**Parameters**

- **ang** — 

#### `RotateByRadians` Method (Double, D2Point)

Rotate line about pivot point by given angle (in radians)

```csharp
public abstract void RotateByRadians( double ang , D2Point pivot );
```

**Parameters**

- **ang** — 
- **pivot** —

#### `ScaleBy` Method (Double)

Scale uniformly by given amount

```csharp
public abstract void ScaleBy( double s );
```

**Parameters**

- **s** — 

#### `ScaleBy` Method (Double, D2Point)

Scale by given amount about pivot point

```csharp
public abstract void ScaleBy( double s , D2Point pivot );
```

**Parameters**

- **s** — 
- **pivot** —

#### `SetValues` Method (D2Point, D2Point)

Set start and end points

```csharp
public abstract void SetValues( D2Point alpha , D2Point beta );
```

**Parameters**

- **alpha** — 
- **beta** — 

#### `SetValues` Method (Double, Double, Double, Double)

Set corrdinates of start and end points

```csharp
public abstract void SetValues( double x1 , double y1 , double x2 , double y2 );
```

**Parameters**

- **x1** — 
- **y1** — 
- **x2** — 
- **y2** —

#### `Start` Method ()

return start point of the finite line

```csharp
public abstract D2Point Start();
```

#### `Start` Method (D2Point)

Set start point

```csharp
public abstract void Start( D2Point alpha );
```

**Parameters**

- **alpha** — 

#### `Start` Method (Double, Double)

Set coordinates of start point

```csharp
public abstract void Start( double x , double y );
```

**Parameters**

- **x** — 
- **y** —

#### `ToString` Method

Returns a string describing the contents of the D2FiniteLine

```csharp
public abstract string ToString();
```

#### `TValue` Method

Distance of point p from start point of line in the direction of the line. The distance is returned in units such that one line length = 1 unit.

```csharp
public abstract double TValue( D2Point p );
```

**Parameters**

- **p** — Reference point

#### `UnitDirection` Method

Return unit vector of direction of line

```csharp
public abstract D2Vector UnitDirection();
```

#### `UValue` Method

Distance of point p from start point of line in the direction normal to the line. The distance is returned in units such that one line length = 1 unit. +ve value => point p lies to left of line -ve value => point p lies to right of line

```csharp
public abstract double UValue( D2Point p );
```

**Parameters**

- **p** —

## Operators

#### `Equality` Operator

test for equality

```csharp
public static bool operator ==( D2FiniteLine left , D2FiniteLine right );
```

**Parameters**

- **left** — 
- **right** —

#### `Inequality` Operator

test for inequality

```csharp
public static bool operator !=( D2FiniteLine left , D2FiniteLine right );
```

**Parameters**

- **left** — 
- **right** —
