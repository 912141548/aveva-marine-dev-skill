---
title: Aveva.Pdms.Maths.Geometry.D2Line Class
namespace: Aveva.Pdms.Maths.Geometry
assembly: Aveva.Pdms.Maths.Geometry
kind: Class
source: Aveva.Pdms.Maths.Geometry
---

# Aveva.Pdms.Maths.Geometry.D2Line Class

> 2 D Line class

## Syntax

```csharp
public abstract class D2Line
```

## Inheritance

`System.Object` → `Aveva.Pdms.Maths.Geometry.D2Line`

## Thread Safety

Public static ( Shared in Visual Basic) members of this type are
safe for multithreaded operations. Instance members are not guaranteed to be
thread-safe.

## Requirements

Namespace:
Aveva.Pdms.Maths.Geometry
Assembly: Aveva.Pdms.Maths.Geometry (in Aveva.Pdms.Maths.Geometry.dll)

## Methods

#### `Antiparallel` Method (D2Line)

true if lines are anti parallel

```csharp
public abstract bool Antiparallel( D2Line line );
```

**Parameters**

- **line** — 

#### `Antiparallel` Method (D2Line, Double)

true if lines are anti parallel to within given angular tolerance (radians)

```csharp
public abstract bool Antiparallel( D2Line line , double tol );
```

**Parameters**

- **line** — 
- **tol** —

#### `CheckLength` Method ()

Returns true if distance between start and end points is greater than default tolerance

```csharp
public abstract bool CheckLength();
```

#### `CheckLength` Method (Double)

Returns true if distance between start and end points is greater than minLength

```csharp
public abstract bool CheckLength( double minLength );
```

**Parameters**

- **minLength** —

#### `Clone` Method

Create clone

```csharp
public abstract D2Line Clone();
```

#### `Create` Method ()

default constructor

```csharp
public static D2Line Create();
```

#### `Create` Method (D2FiniteLine, LTYPE)

Construct a line from given FiniteLine

```csharp
public static D2Line Create( D2FiniteLine fLine , LTYPE type );
```

**Parameters**

- **fLine** — 
- **type** — 

#### `Create` Method (D2Point, D2Point)

Construct a finite line through given points

```csharp
public static D2Line Create( D2Point start , D2Point end );
```

**Parameters**

- **start** — 
- **end** — 

#### `Create` Method (D2Point, D2Point, LTYPE)

Construct line of given type passing through given points

```csharp
public static D2Line Create( D2Point start , D2Point end , LTYPE type );
```

**Parameters**

- **start** — 
- **end** — 
- **type** — infinite, semiWithStart, semiWithEnd, finite

#### `Create` Method (D2Point, D2Vector)

Construct a line from given position and in given direction

```csharp
public static D2Line Create( D2Point start , D2Vector dir );
```

**Parameters**

- **start** — 
- **dir** — 

#### `Create` Method (D2Point, D2Vector, LTYPE)

Construct line of given type trhough given point in given direction

```csharp
public static D2Line Create( D2Point start , D2Vector dir , LTYPE type );
```

**Parameters**

- **start** — 
- **dir** — 
- **type** — infinite, semiWithStart, semiWithEnd, finite

#### `Create` Method (Double, Double, Double, Double)

Construct a finite line through given x,y coordinates

```csharp
public static D2Line Create( double x1 , double y1 , double x2 , double y2 );
```

**Parameters**

- **x1** — 
- **y1** — 
- **x2** — 
- **y2** — 

#### `Create` Method (Double, Double, Double, Double, LTYPE)

Construct line of given type through given x, y coordinates

```csharp
public static D2Line Create( double x1 , double y1 , double x2 , double y2 , LTYPE type );
```

**Parameters**

- **x1** — 
- **y1** — 
- **x2** — 
- **y2** — 
- **type** — infinite, semiWithStart, semiWithEnd, finite

#### `Direction` Method

Returns direction vector of line

```csharp
public abstract D2Vector Direction();
```

#### `DistanceFrom` Method (D2FiniteLine)

returns shortest straight line distance between a line and a FiniteLine

```csharp
public abstract double DistanceFrom( D2FiniteLine FiniteLine );
```

**Parameters**

- **FiniteLine** — 

#### `DistanceFrom` Method (D2Line)

Returns shortest straight line distance between two lines

```csharp
public abstract double DistanceFrom( D2Line line );
```

**Parameters**

- **line** — 

#### `DistanceFrom` Method (D2Point)

returns shortest straight line distance between line and point

```csharp
public abstract double DistanceFrom( D2Point point );
```

**Parameters**

- **point** —

#### `DistanceFromOrigin` Method

Returns shortest straight line distance between line and origin

```csharp
public abstract double DistanceFromOrigin();
```

#### `End` Method ()

Return end point

```csharp
public abstract D2Point End();
```

#### `End` Method (D2Point)

set end point

```csharp
public abstract void End( D2Point p );
```

**Parameters**

- **p** — 

#### `End` Method (Double, Double)

set end coordinates

```csharp
public abstract void End( double x , double y );
```

**Parameters**

- **x** — 
- **y** —

#### `Equals` Method (D2Line)

test for equality

```csharp
public abstract bool Equals( D2Line d2 );
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

Returns point on line, ratio t between start and end

```csharp
public abstract D2Point InterPoint( double t );
```

**Parameters**

- **t** —

#### `Intersects` Method

Returns TRUE if lines are not parallel (or anti parallel) and both lines are of meaningful length (>1.E-6). Intersection point is returned through argument but is unchanged when FALSE is RETURNed. The Intersection point returned is the point the lines would cross if they were BOTH INFINITELY EXTENDED. Use the "onLine(D2Point, double tol=1.E-6)" method to determine if this intersection lies on one or both lines (within tolerance). N.B. use return value to check for intersection otherwise you'll get confused if lines really do cross at input value of "intersection" point

```csharp
public abstract bool Intersects( D2Line line , D2Point intersection );
```

**Parameters**

- **line** — 
- **intersection** —

#### `IsFinite` Method

Returns true for a line with a start and an end

```csharp
public abstract bool IsFinite();
```

#### `IsInfinite` Method

true for bi-directionally infinite lines only

```csharp
public abstract bool IsInfinite();
```

#### `IsSemiInfinite` Method

true for semi-infinite lines (one end only)

```csharp
public abstract bool IsSemiInfinite();
```

#### `IsSemiWithEnd` Method

true for semi-infinite line with an end point

```csharp
public abstract bool IsSemiWithEnd();
```

#### `IsSemiWithStart` Method

true for semi-infinite line with a start point

```csharp
public abstract bool IsSemiWithStart();
```

#### `Length` Method

returns non-negative distance between start_ and end_ points. Always finite since the start and end points are used to define the direction of the line for (semi) infinite lines and not the extent.

```csharp
public abstract double Length();
```

#### `LineType` Method ()

Return line type

```csharp
public abstract LTYPE LineType();
```

**Return Value**

infinite, semiWithStart, semiWithEnd, finite

#### `LineType` Method (LTYPE)

set line type: possibilities are - D2Line::finite D2Line::infinite D2Line::semiWithStart D2Line::semiWithEnd

```csharp
public abstract void LineType( LTYPE type );
```

**Parameters**

- **type** —

#### `LTypeToString` Method

Convert linetype to string

```csharp
public abstract string LTypeToString( LTYPE lt );
```

**Parameters**

- **lt** —

#### `MirrorX` Method ()

Reflect in X about origin

```csharp
public abstract void MirrorX();
```

#### `MirrorX` Method (D2Point)

Reflect in X about y=x coord of pivot

```csharp
public abstract void MirrorX( D2Point pivot );
```

**Parameters**

- **pivot** —

#### `MirrorY` Method ()

Relect in Y about origin

```csharp
public abstract void MirrorY();
```

#### `MirrorY` Method (D2Point)

Reflect about y = x coordinate of pivot

```csharp
public abstract void MirrorY( D2Point pivot );
```

**Parameters**

- **pivot** —

#### `MoveBy` Method

shift the start and end points

```csharp
public abstract void MoveBy( D2Vector v );
```

**Parameters**

- **v** —

#### `NearestPoint` Method

Returns point on line nearest given point "point"

```csharp
public abstract D2Point NearestPoint( D2Point point );
```

**Parameters**

- **point** —

#### `NearestPointToOrigin` Method

Returns point on line closest to origin.

```csharp
public abstract D2Point NearestPointToOrigin();
```

#### `OnLine` Method (D2Point)

trus if point is on line

```csharp
public abstract bool OnLine( D2Point p );
```

**Parameters**

- **p** — 

#### `OnLine` Method (D2Point, Double)

true if given point is within distance "tol" of line

```csharp
public abstract bool OnLine( D2Point p , double tol );
```

**Parameters**

- **p** — 
- **tol** —

#### `Parallel` Method (D2Line)

true if lines are parallel

```csharp
public abstract bool Parallel( D2Line line );
```

**Parameters**

- **line** — 

#### `Parallel` Method (D2Line, Double)

true if lines are parallel to within given angular tolerance (radians)

```csharp
public abstract bool Parallel( D2Line line , double tol );
```

**Parameters**

- **line** — 
- **tol** —

#### `PerpendicularDistance` Method

Returns the Distance of the arg point from the perpendicularPoint calculated using Perpendicluar Point method.

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

Polar angle of direction of line

```csharp
public abstract double PolarAngleInRadians();
```

#### `Reverse` Method

swap start and end points

```csharp
public abstract void Reverse();
```

#### `RotateByDegrees` Method (Double)

Rotate line about origin by angle in degrees

```csharp
public abstract void RotateByDegrees( double ang );
```

**Parameters**

- **ang** — 

#### `RotateByDegrees` Method (Double, D2Point)

Rotate line about pivot by angle in degrees

```csharp
public abstract void RotateByDegrees( double ang , D2Point pivot );
```

**Parameters**

- **ang** — 
- **pivot** —

#### `RotateByRadians` Method (Double)

rotate line about origin by angle in radians

```csharp
public abstract void RotateByRadians( double ang );
```

**Parameters**

- **ang** — 

#### `RotateByRadians` Method (Double, D2Point)

rotate line about pivot by angle in radians

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

Scale by given amount about pivot

```csharp
public abstract void ScaleBy( double s , D2Point pivot );
```

**Parameters**

- **s** — 
- **pivot** —

#### `SetValues` Method (D2Point, D2Point)

set start and end points

```csharp
public abstract void SetValues( D2Point start , D2Point end );
```

**Parameters**

- **start** — 
- **end** — 

#### `SetValues` Method (Double, Double, Double, Double)

set start and end coordinates

```csharp
public abstract void SetValues( double x1 , double y1 , double x2 , double y2 );
```

**Parameters**

- **x1** — 
- **y1** — 
- **x2** — 
- **y2** —

#### `Start` Method ()

Return start point

```csharp
public abstract D2Point Start();
```

#### `Start` Method (D2Point)

set start point

```csharp
public abstract void Start( D2Point p );
```

**Parameters**

- **p** — 

#### `Start` Method (Double, Double)

set start coordinates

```csharp
public abstract void Start( double x , double y );
```

**Parameters**

- **x** — 
- **y** —

#### `ToString` Method

Returns a string describing the contents of the D2Line

```csharp
public abstract string ToString();
```

#### `TValue` Method

Distance of point p from start point of line in the direction of the line. The distance is returned in units such that one line length = 1 unit.

```csharp
public abstract double TValue( D2Point p );
```

**Parameters**

- **p** —

#### `UnitDirection` Method

Returns unit vector of line

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
public static bool operator ==( D2Line left , D2Line right );
```

**Parameters**

- **left** — 
- **right** —

#### `Inequality` Operator

test for inequality

```csharp
public static bool operator !=( D2Line left , D2Line right );
```

**Parameters**

- **left** — 
- **right** —
