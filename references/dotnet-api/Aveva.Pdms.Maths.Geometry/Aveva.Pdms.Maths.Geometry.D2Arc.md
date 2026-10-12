---
title: Aveva.Pdms.Maths.Geometry.D2Arc Class
namespace: Aveva.Pdms.Maths.Geometry
assembly: Aveva.Pdms.Maths.Geometry
kind: Class
source: Aveva.Pdms.Maths.Geometry
---

# Aveva.Pdms.Maths.Geometry.D2Arc Class

> A directed arc class An arc can run either anticlockwise or clockwise from the start to the end angle. The direction is defined by the user. Input angles will be normalized to lie between 0 and 2pi If start and end angles are EXACTLY EQUAL then the arc will be treated as a FULL CIRCLE. All Angles are measured anticlockwise from the x axis.

## Syntax

```csharp
public abstract class D2Arc
```

## Inheritance

`System.Object` → `Aveva.Pdms.Maths.Geometry.D2Arc`

## Thread Safety

Public static ( Shared in Visual Basic) members of this type are
safe for multithreaded operations. Instance members are not guaranteed to be
thread-safe.

## Requirements

Namespace:
Aveva.Pdms.Maths.Geometry
Assembly: Aveva.Pdms.Maths.Geometry (in Aveva.Pdms.Maths.Geometry.dll)

## Properties

#### `Radius` Property

Property to set/get radius of arc

```csharp
public abstract double Radius {get; set;}
```

## Methods

#### `Anticlockwise` Method ()

Return true if sense is clockwise

```csharp
public abstract bool Anticlockwise();
```

#### `Anticlockwise` Method (Boolean)

set the direction the arc takes from start to end ( input "true" implies anticlockwise)

```csharp
public abstract void Anticlockwise( bool anti );
```

**Parameters**

- **anti** — True for anticlockwise

#### `Bulge` Method

returns the bulge factor of the arc. +ve for anticlockwise arc and -ve for clockwise arc (returns DBL_MAX for a full circle.)

```csharp
public abstract double Bulge();
```

#### `Centre` Method ()

returns the centre of the arc circle

```csharp
public abstract D2Point Centre();
```

#### `Centre` Method (D2Point)

set the centre of arc to given point

```csharp
public abstract void Centre( D2Point p );
```

**Parameters**

- **p** — 

#### `Centre` Method (Double, Double)

set centre of arc to given x, y values

```csharp
public abstract void Centre( double x , double y );
```

**Parameters**

- **x** — 
- **y** —

#### `Clockwise` Method ()

Return true if sense of arc is anticlockwise

```csharp
public abstract bool Clockwise();
```

#### `Clockwise` Method (Boolean)

set the direction the arc takes from start to end ( input "true" implies clockwise)

```csharp
public abstract void Clockwise( bool clock );
```

**Parameters**

- **clock** — True for clockwise

#### `Clone` Method

```csharp
public abstract D2Arc Clone();
```

#### `Create` Method ()

Create default arc

```csharp
public static D2Arc Create();
```

#### `Create` Method (D2Arc)

Create copy of arc

```csharp
public static D2Arc Create( D2Arc arc );
```

**Parameters**

- **arc** — 

#### `Create` Method (D2Point, D2Point, D2Point)

construct an arc with start, mid and end point.

```csharp
public static D2Arc Create( D2Point start , D2Point mid , D2Point end );
```

**Parameters**

- **start** — 
- **mid** — 
- **end** — 

#### `Create` Method (D2Point, D2Point, Double)

construct from two points and a bulge factor. The "sense" of the arc is carried by the sign of the bulge factor. +ve bulge => anticlockwise.

```csharp
public static D2Arc Create( D2Point start , D2Point end , double bulge );
```

**Parameters**

- **start** — 
- **end** — 
- **bulge** — 

#### `Create` Method (D2Point, Double, D2Angle, D2Angle, Boolean)

Construct an arc from D2Angles

```csharp
public static D2Arc Create( D2Point centre , double radius , D2Angle startAngle , D2Angle endAngle , bool anticlock );
```

**Parameters**

- **centre** — 
- **radius** — 
- **startAngle** — 
- **endAngle** — 
- **anticlock** — 

#### `Create` Method (D2Point, Double, D2Point, D2Point)

Construct an arc from centre, radius, start and end points. Default is anticlockwise

```csharp
public static D2Arc Create( D2Point centre , double radius , D2Point start , D2Point end );
```

**Parameters**

- **centre** — 
- **radius** — 
- **start** — 
- **end** — 

#### `Create` Method (D2Point, Double, D2Point, D2Point, Boolean)

Construct an arc from centre, radius, start and end points. Uses angles of points wrt centre to construct start and end angles. if start (end) point == centre point then start (end) angle will be set to 0 The arc will be treated as a FULL CIRCLE if the START and END angles are EXACTLY the same.

```csharp
public static D2Arc Create( D2Point centre , double radius , D2Point start , D2Point end , bool anticlock );
```

**Parameters**

- **centre** — 
- **radius** — 
- **start** — 
- **end** — 
- **anticlock** — 

#### `Create` Method (D2Point, Double, Double, Double)

Construct an arc from centre point,radius, start and end angles. Default is anticlockwise

```csharp
public static D2Arc Create( D2Point centre , double radius , double startRadians , double endRadians );
```

**Parameters**

- **centre** — 
- **radius** — 
- **startRadians** — 
- **endRadians** — 

#### `Create` Method (D2Point, Double, Double, Double, Boolean)

Construct an arc from centre point,radius, start and end angles. By default, the arc will be made in the anticlockwise direction The arc will be treated as a FULL CIRCLE if the START and END angles are exactly the same.

```csharp
public static D2Arc Create( D2Point centre , double radius , double startRadians , double endRadians , bool anticlock );
```

**Parameters**

- **centre** — 
- **radius** — 
- **startRadians** — 
- **endRadians** — 
- **anticlock** —

#### `Degrees` Method (D2Point)

angle of pt wrt centre of arc measured anticlockwise from the x direction

```csharp
public abstract double Degrees( D2Point p );
```

**Parameters**

- **p** — Reference point

#### `Degrees` Method (Double)

Returns a point on the circumference of the arc circle, at the specified angle

```csharp
public abstract D2Point Degrees( double degs );
```

**Parameters**

- **degs** —

#### `End` Method

returns the end of the arc

```csharp
public abstract D2Point End();
```

#### `EndAngle` Method

Returns end angle in D2Angle

```csharp
public abstract D2Angle EndAngle();
```

#### `EndDegrees` Method ()

Returns end angle in degrees

```csharp
public abstract double EndDegrees();
```

#### `EndDegrees` Method (Double)

set end angle

```csharp
public abstract void EndDegrees( double degs );
```

**Parameters**

- **degs** — angle in degrees

#### `EndRadians` Method ()

Returns end angle in radians

```csharp
public abstract double EndRadians();
```

#### `EndRadians` Method (Double)

set end angle

```csharp
public abstract void EndRadians( double rads );
```

**Parameters**

- **rads** — angle in radians

#### `EndTangent` Method

Returns the vector of the end tangent

```csharp
public abstract D2Vector EndTangent();
```

#### `Equals` Method (D2Arc)

Returns true if arcs are equal

```csharp
public abstract bool Equals( D2Arc a );
```

**Parameters**

- **a** — 

#### `Equals` Method (D2Arc, Double)

returns TRUE if start points, end points, and centre points all match to within distance "tol". The "senses" of the arcs must also be the same.

```csharp
public abstract bool Equals( D2Arc a , double tol );
```

#### `Equals` Method (Object)

override system default equals method

```csharp
public override bool Equals( object a );
```

**Parameters**

- **a** —

#### `From3Points` Method

Reconstruct the arc to pass from the start point to the end point and go THROUGH the thru Point. Returns TRUE if succesful. The three Points must NOT be collinear otherwise the function will return FALSE and the arc will remain unchanged.

```csharp
public abstract bool From3Points( D2Point start , D2Point thru , D2Point end );
```

**Parameters**

- **start** — 
- **thru** — 
- **end** —

#### `GetHashCode` Method

override system default gethashcode method

```csharp
public override int GetHashCode();
```

#### `Height` Method

returns chord height

```csharp
public abstract double Height();
```

#### `Intersects` Method (D2Arc, D2Point, D2Point)

Returns TRUE if the two arc circles intersect. If they intersect p1 and p2 will be set to the intersection points- otherwisae p1 and p2 will remain unchanged. N.B. Use the "onArc" function to discover if these intersection points lie on your length of arc.

```csharp
public abstract bool Intersects( D2Arc arc , D2Point p1 , D2Point p2 );
```

**Parameters**

- **arc** — 
- **p1** — First intersection point
- **p2** — Second intersection point

#### `Intersects` Method (D2FiniteLine, D2Point, D2Point)

Returns true if the finite line and the arc intersect

```csharp
public abstract bool Intersects( D2FiniteLine line , D2Point p1 , D2Point p2 );
```

**Parameters**

- **line** — 
- **p1** — 
- **p2** — 

#### `Intersects` Method (D2Line, D2Point, D2Point)

Returns TRUE if the INFINITELY EXTENDED line and the arc circle intersect. If they intersect p1 and p2 will be set to the intersection points- otherwisae p1 and p2 will remain unchanged. N.B. Use the "onArc" and "onLine" functions to discover if these intersection point lie on your length of arc, or your bounded line.

```csharp
public abstract bool Intersects( D2Line line , D2Point p1 , D2Point p2 );
```

**Parameters**

- **line** — 
- **p1** — First intersection point
- **p2** — Second intersection point

#### `IsCircle` Method

True if the arc is a circle i.e. EXACT EQUALITY of start and END ANGLES

```csharp
public abstract bool IsCircle();
```

#### `IsConcentric` Method (D2Arc)

True if two arcs have saem centre

```csharp
public abstract bool IsConcentric( D2Arc arc );
```

**Parameters**

- **arc** — 

#### `IsConcentric` Method (D2Arc, Double)

True if the two arcs have the same centre, within tolerance

```csharp
public abstract bool IsConcentric( D2Arc arc , double tol );
```

#### `LeftTangentPoint` Method

return via argument the point on the arc circle that lies on a line that is tangential to the arc circle and passes through point p. LeftTangentPoint lies to the LEFT of the line from p to circle centre. TRUE if p lies more than 1.E-6 outside the circle. FALSE if p lies within the circle or less than 1.E-6 outside.

```csharp
public abstract bool LeftTangentPoint( D2Point p , D2Point tanPoint );
```

**Parameters**

- **p** — Reference point
- **tanPoint** — Returned Point on Tangent

#### `Length` Method

Returns the length of the arc

```csharp
public abstract double Length();
```

#### `MoveBy` Method (D2Vector)

move the arc by the offset specified by given vector

```csharp
public abstract void MoveBy( D2Vector vec );
```

**Parameters**

- **vec** — 

#### `MoveBy` Method (Double, Double)

Move arc by x and y values

```csharp
public abstract void MoveBy( double x , double y );
```

**Parameters**

- **x** — 
- **y** —

#### `NearestPoint` Method

returns the nearest point to "p" on the length of arc.

```csharp
public abstract D2Point NearestPoint( D2Point p );
```

**Parameters**

- **p** —

#### `NearestPointToOrigin` Method

returns the nearest point to origin on the length of arc.

```csharp
public abstract D2Point NearestPointToOrigin();
```

#### `OnArc` Method (D2Point)

Returns true if point is on arc

```csharp
public abstract bool OnArc( D2Point p );
```

**Parameters**

- **p** — 

#### `OnArc` Method (D2Point, Double)

returns true if point lies within tolerance distance of the arc

```csharp
public abstract bool OnArc( D2Point p , double tol );
```

**Parameters**

- **p** — Reference point
- **tol** — Tolerance

#### `Radians` Method (D2Point)

angle of pt wrt centre of arc measured anticlockwise from the x direction

```csharp
public abstract double Radians( D2Point p );
```

**Parameters**

- **p** — Reference point

#### `Radians` Method (Double)

Returns a point on the circumference of the arc circle, at the specified angle

```csharp
public abstract D2Point Radians( double rads );
```

**Parameters**

- **rads** —

#### `RightTangentPoint` Method

return via argument the point on the arc circle that lies on a line that is tangential to the arc circle and passes through point p. RightTangentPoint lies to the RIGHT of the line from p to circle centre. TRUE if p lies more than 1.E-6 outside the circle. FALSE if p lies within the circle or less than 1.E-6 outside.

```csharp
public abstract bool RightTangentPoint( D2Point p , D2Point tanPoint );
```

**Parameters**

- **p** — 
- **tanPoint** —

#### `RotateByDegrees` Method (Double)

Rotate arc around origin by given angle

```csharp
public abstract void RotateByDegrees( double degrees );
```

**Parameters**

- **degrees** — angle in degrees

#### `RotateByDegrees` Method (Double, D2Point)

Rotate arc by given angle around given pivot point

```csharp
public abstract void RotateByDegrees( double degrees , D2Point pivot );
```

**Parameters**

- **degrees** — angle in degrees
- **pivot** —

#### `RotateByRadians` Method (Double)

Rotate arc by given angle around origin

```csharp
public abstract void RotateByRadians( double radians );
```

**Parameters**

- **radians** — angle in radians

#### `RotateByRadians` Method (Double, D2Point)

Rotate arc by given angle around given pivot point

```csharp
public abstract void RotateByRadians( double radians , D2Point pivot );
```

**Parameters**

- **radians** — angle in radians
- **pivot** —

#### `SpanAngle` Method

Return D2Angle of span

```csharp
public abstract D2Angle SpanAngle();
```

#### `SpanDegrees` Method

Return span in degrees -ve for a clockwise arc, +ve otherwise If start and end angles are EXACTLY the same the arc will be treated as a full circle => span = 360

```csharp
public abstract double SpanDegrees();
```

#### `SpanRadians` Method

Return span in radians -ve for a clockwise arc, +ve otherwise If start and end angles are EXACTLY the same the arc will be treated as a full circle => span = 2pi

```csharp
public abstract double SpanRadians();
```

#### `Start` Method

returns the start of the arc

```csharp
public abstract D2Point Start();
```

#### `StartAngle` Method

Returns start angle in D2Angle

```csharp
public abstract D2Angle StartAngle();
```

#### `StartDegrees` Method ()

Returns start angle in degrees

```csharp
public abstract double StartDegrees();
```

#### `StartDegrees` Method (Double)

set start angle

```csharp
public abstract void StartDegrees( double degs );
```

**Parameters**

- **degs** — angle in degrees

#### `StartRadians` Method ()

Returns start angle in radians

```csharp
public abstract double StartRadians();
```

#### `StartRadians` Method (Double)

Set the start angle. Angles are normalized to be in the range 0 to 2Pi The arc will be treated as a FULL CIRCLE if the START and END ANGLES are EXACTLY the SAME.

```csharp
public abstract void StartRadians( double rads );
```

**Parameters**

- **rads** —

#### `StartTangent` Method

Returns the vector of the start tangent

```csharp
public abstract D2Vector StartTangent();
```

#### `TangentDegrees` Method

returns the direction of the tangent to the arc at the point lying at the supplied angle on the arc circle. The vector returned follow the "sense" of the arc.

```csharp
public abstract D2Vector TangentDegrees( double degs );
```

**Parameters**

- **degs** — angle in degrees

#### `TangentRadians` Method

returns the direction of the tangent to the arc at the point lying at the supplied angle on the arc circle. The vector returned follow the "sense" of the arc.

```csharp
public abstract D2Vector TangentRadians( double rads );
```

**Parameters**

- **rads** — Angle in radians

#### `ToString` Method

Returns a string describing the contents of the D2Arc

```csharp
public abstract string ToString();
```

#### `WithinSpan` Method

return true if the point is within the span of the arc

```csharp
public abstract bool WithinSpan( D2Point p );
```

**Parameters**

- **p** —

#### `WithinSpanDegrees` Method

Return true if angle is within span of the arc

```csharp
public abstract bool WithinSpanDegrees( double degs );
```

**Parameters**

- **degs** — angle in degrees

#### `WithinSpanRadians` Method

return TRUE if angle is within the span of the arc

```csharp
public abstract bool WithinSpanRadians( double rads );
```

**Parameters**

- **rads** —

## Operators

#### `Equality` Operator

equality operator

```csharp
public static bool operator ==( D2Arc left , D2Arc right );
```

**Parameters**

- **left** — 
- **right** —

#### `Inequality` Operator

inequality operator

```csharp
public static bool operator !=( D2Arc left , D2Arc right );
```

**Parameters**

- **left** — 
- **right** —
