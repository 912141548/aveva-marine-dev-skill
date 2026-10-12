---
title: Aveva.Pdms.Maths.Geometry.D2Circle Class
namespace: Aveva.Pdms.Maths.Geometry
assembly: Aveva.Pdms.Maths.Geometry
kind: Class
source: Aveva.Pdms.Maths.Geometry
---

# Aveva.Pdms.Maths.Geometry.D2Circle Class

> A 2-D Circle N.B. all ANGLES measured ANTI-CLOCKWISE from X-AXIS

## Syntax

```csharp
public abstract class D2Circle
```

## Inheritance

`System.Object` → `Aveva.Pdms.Maths.Geometry.D2Circle`

## Thread Safety

Public static ( Shared in Visual Basic) members of this type are
safe for multithreaded operations. Instance members are not guaranteed to be
thread-safe.

## Requirements

Namespace:
Aveva.Pdms.Maths.Geometry
Assembly: Aveva.Pdms.Maths.Geometry (in Aveva.Pdms.Maths.Geometry.dll)

## Properties

#### `Area` Property

Property - area (read only)

```csharp
public abstract double Area {get;}
```

#### `Circumference` Property

Circumference - read only

```csharp
public abstract double Circumference {get;}
```

#### `Diameter` Property

Property - diameter

```csharp
public abstract double Diameter {get; set;}
```

#### `Radius` Property

Property - radius

```csharp
public abstract double Radius {get; set;}
```

## Methods

#### `box` Method

return limits box that just encloses the circle

```csharp
public abstract D2Limits box();
```

#### `Centre` Method ()

Return centre point

```csharp
public abstract D2Point Centre();
```

#### `Centre` Method (D2Point)

set the centre point

```csharp
public abstract void Centre( D2Point p );
```

**Parameters**

- **p** — 

#### `Centre` Method (Double, Double)

set the centre point

```csharp
public abstract void Centre( double x , double y );
```

**Parameters**

- **x** — 
- **y** —

#### `Clone` Method

deep copy

```csharp
public abstract D2Circle Clone();
```

#### `Create` Method ()

Default circle - centre [0,0] radius = 1.

```csharp
public static D2Circle Create();
```

#### `Create` Method (D2Circle)

Copy constructor

```csharp
public static D2Circle Create( D2Circle circ );
```

**Parameters**

- **circ** — 

#### `Create` Method (D2Point, D2Point)

construct from centre point and a point on the circumference

```csharp
public static D2Circle Create( D2Point centre , D2Point p );
```

**Parameters**

- **centre** — 
- **p** — 

#### `Create` Method (D2Point, D2Point, Double)

Construct from two points on circumference and a bulge factor N.B. IF bulgeFactor is ZERO a value of 1 will be used instead SO CHECK YOUR BULGE FACTOR BEFOREHAND!!

```csharp
public static D2Circle Create( D2Point p , D2Point q , double bulgeFactor );
```

**Parameters**

- **p** — 
- **q** — 
- **bulgeFactor** — 

#### `Create` Method (D2Point, Double)

Create circle from centre and radius N.B. negative radii will be made positive

```csharp
public static D2Circle Create( D2Point centre , double radius );
```

**Parameters**

- **centre** — 
- **radius** —

#### `Degrees` Method (D2Point)

return angle (in degs) of point p wrt centre of circle

```csharp
public abstract double Degrees( D2Point p );
```

**Parameters**

- **p** — 

#### `Degrees` Method (Double)

return point on circumference at angle given in degrees

```csharp
public abstract D2Point Degrees( double degs );
```

**Parameters**

- **degs** —

#### `DistanceFromCentre` Method

return distance of point p from centre of circle

```csharp
public abstract double DistanceFromCentre( D2Point p );
```

**Parameters**

- **p** —

#### `DistanceFromEdge` Method

return distance of point p from perimeter of circle returns -ve if point is inside circle, +ve otherwise.

```csharp
public abstract double DistanceFromEdge( D2Point p );
```

**Parameters**

- **p** —

#### `Encloses` Method (D2Circle)

true if given circle c lies inside object circle

```csharp
public abstract bool Encloses( D2Circle c );
```

**Parameters**

- **c** — 

#### `Encloses` Method (D2Point)

true if point lies ON or IN circle

```csharp
public abstract bool Encloses( D2Point p );
```

**Parameters**

- **p** — Reference point

#### `Equals` Method (D2Circle)

test for equality

```csharp
public abstract bool Equals( D2Circle c );
```

**Parameters**

- **c** — 

#### `Equals` Method (Object)

override equals

```csharp
public override bool Equals( object o );
```

**Parameters**

- **o** —

#### `From3Points` Method

reset the circle centre and radius to pass through the three given points. returns TRUE if successful returns FALSE if unsuccessful i.e. 2 points too close together or all points on same line Circle will remain unchanged if FALSE is returned.

```csharp
public abstract bool From3Points( D2Point p1 , D2Point p2 , D2Point p3 );
```

**Parameters**

- **p1** — 
- **p2** — 
- **p3** —

#### `GetHashCode` Method

override gethashcode

```csharp
public override int GetHashCode();
```

#### `Intersects` Method (D2Circle, D2Point, D2Point)

Returns intersection points if result is true TRUE if circle circ intersects the circle. FALSE if point of closest approach of line to the centre point is > radius. No tolerance used.

```csharp
public abstract bool Intersects( D2Circle circ , D2Point p1 , D2Point p2 );
```

**Parameters**

- **circ** — 
- **p1** — 
- **p2** — 

#### `Intersects` Method (D2FiniteLine, D2Point, D2Point)

Returns intersection points if result is true TRUE if finiteline intersects the circle. FALSE if point of closest approach of line to the centre point is > radius. No tolerance used.

```csharp
public abstract bool Intersects( D2FiniteLine FiniteLine , D2Point p1 , D2Point p2 );
```

**Parameters**

- **FiniteLine** — 
- **p1** — 
- **p2** — 

#### `Intersects` Method (D2Line, D2Point, D2Point)

Returns intersection points if result is true Input line is treated as INFINITELY EXTENDED Use "onLine" methods of line classes to determine if intersection points lie on the finite/seminfinite lines to within your desired tolerance. TRUE if line/circle intersects the circle. FALSE if point of closest approach of line to the centre point is > radius. No tolerance used.

```csharp
public abstract bool Intersects( D2Line line , D2Point p1 , D2Point p2 );
```

**Parameters**

- **line** — 
- **p1** — 
- **p2** —

#### `LeftTangentPoint` Method

return via argument the point on the circle that lies on a line that is tangential to the circle and passes through point p. LeftTangentPoint lies to the LEFT of the line from p to circle centre. TRUE if p lies more than 1.E-6 outside the circle. FALSE if p lies within the circle or less than 1.E-6 outside.

```csharp
public abstract bool LeftTangentPoint( D2Point p , D2Point tanPoint );
```

**Parameters**

- **p** — 
- **tanPoint** —

#### `MirrorX` Method ()

Reflect in X about origin

```csharp
public abstract void MirrorX();
```

#### `MirrorX` Method (D2Point)

Reflect in X about pivot

```csharp
public abstract void MirrorX( D2Point pivot );
```

**Parameters**

- **pivot** —

#### `MirrorY` Method ()

Reflect in Y about origin

```csharp
public abstract void MirrorY();
```

#### `MirrorY` Method (D2Point)

Reflect in Y about pivot

```csharp
public abstract void MirrorY( D2Point pivot );
```

**Parameters**

- **pivot** —

#### `MoveBy` Method

Move the centre point

```csharp
public abstract void MoveBy( D2Vector v );
```

**Parameters**

- **v** —

#### `OnCircle` Method (D2Point)

Return true if point lies on circumference

```csharp
public abstract bool OnCircle( D2Point p );
```

**Parameters**

- **p** — Reference point

#### `OnCircle` Method (D2Point, Double)

Return true if point lies on circumference (within tolerance)

```csharp
public abstract bool OnCircle( D2Point p , double tol );
```

**Parameters**

- **p** — Reference point
- **tol** —

#### `pointNearCentre` Method (D2FiniteLine)

Returns the point on the finiteline that lies closest to the centre of the circle.

```csharp
public abstract D2Point pointNearCentre( D2FiniteLine FiniteLine );
```

**Parameters**

- **FiniteLine** — 

#### `pointNearCentre` Method (D2Line)

Input line is treated as INFINITELY EXTENDED Returns the point on the infinitely extended line that lies closest to the centre of the circle. Use the onLine functions of the line classes to determine if the returned point lies on your line to within your desired tolerance

```csharp
public abstract D2Point pointNearCentre( D2Line line );
```

**Parameters**

- **line** —

#### `Radians` Method (D2Point)

return angle (in rads) of point p wrt centre of circle

```csharp
public abstract double Radians( D2Point p );
```

**Parameters**

- **p** — 

#### `Radians` Method (Double)

return point on circumference at angle given in rads

```csharp
public abstract D2Point Radians( double rads );
```

**Parameters**

- **rads** —

#### `RightTangentPoint` Method

return via argument the point on the circle that lies on a line that is tangential to the circle and passes through point p. RightTangentPoint lies to the RIGHT of the line from p to circle centre. TRUE if p lies more than 1.E-6 outside the circle. FALSE if p lies within the circle or less than 1.E-6 outside.

```csharp
public abstract bool RightTangentPoint( D2Point p , D2Point tanPoint );
```

**Parameters**

- **p** — Reference point
- **tanPoint** — Returned point on tangent

#### `RotateByDegrees` Method (Double)

Rotate the circle about the origin

```csharp
public abstract void RotateByDegrees( double ang );
```

**Parameters**

- **ang** — 

#### `RotateByDegrees` Method (Double, D2Point)

Rotate the circle about a pivot point

```csharp
public abstract void RotateByDegrees( double ang , D2Point pivot );
```

**Parameters**

- **ang** — 
- **pivot** —

#### `RotateByRadians` Method (Double)

Rotate the circle about the origin

```csharp
public abstract void RotateByRadians( double ang );
```

**Parameters**

- **ang** — 

#### `RotateByRadians` Method (Double, D2Point)

Rotate the circle about the pivot point

```csharp
public abstract void RotateByRadians( double ang , D2Point pivot );
```

**Parameters**

- **ang** — 
- **pivot** —

#### `ScaleBy` Method (Double)

scale centre point and radius

```csharp
public abstract void ScaleBy( double s );
```

**Parameters**

- **s** — 

#### `ScaleBy` Method (Double, D2Point)

scale circle about pivot

```csharp
public abstract void ScaleBy( double s , D2Point pivot );
```

**Parameters**

- **s** — 
- **pivot** —

#### `ToString` Method

Returns a string describing the contents of the D2Circle

```csharp
public abstract string ToString();
```

## Operators

#### `Equality` Operator

true if centre and radius values of both circles match EXACTLY

```csharp
public static bool operator ==( D2Circle left , D2Circle right );
```

**Parameters**

- **left** — 
- **right** —

#### `Inequality` Operator

true if centre or radius values of both circles do not match EXACTLY

```csharp
public static bool operator !=( D2Circle left , D2Circle right );
```

**Parameters**

- **left** — 
- **right** —
