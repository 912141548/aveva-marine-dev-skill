---
title: Aveva.Pdms.Maths.Geometry.D3Line Class
namespace: Aveva.Pdms.Maths.Geometry
assembly: Aveva.Pdms.Maths.Geometry
kind: Class
source: Aveva.Pdms.Maths.Geometry
---

# Aveva.Pdms.Maths.Geometry.D3Line Class

> Finite, Semi-infinite or infinite line in 3D space

## Syntax

```csharp
public abstract class D3Line
```

## Inheritance

`System.Object` → `Aveva.Pdms.Maths.Geometry.D3Line`

## Thread Safety

Public static ( Shared in Visual Basic) members of this type are
safe for multithreaded operations. Instance members are not guaranteed to be
thread-safe.

## Requirements

Namespace:
Aveva.Pdms.Maths.Geometry
Assembly: Aveva.Pdms.Maths.Geometry (in Aveva.Pdms.Maths.Geometry.dll)

## Methods

#### `Antiparallel` Method (D3Line)

Returns True if lines point in OPPOSITE DIRECTIONS (within tolerance Default tolerance=1.E-6 rads)

```csharp
public abstract bool Antiparallel( D3Line line );
```

**Parameters**

- **line** — 

#### `Antiparallel` Method (D3Line, Double)

Returns True if lines point in OPPOSITE DIRECTIONS (within tolerance in RADIANS)

```csharp
public abstract bool Antiparallel( D3Line line , double tolerance );
```

**Parameters**

- **line** — 
- **tolerance** —

#### `AzimuthalAngleInRadians` Method

Returns azimuthal angle of direction of line

```csharp
public abstract double AzimuthalAngleInRadians();
```

#### `CheckLength` Method ()

Return true if distance between start and end points is greater than fl_TOLERANCE

```csharp
public abstract bool CheckLength();
```

#### `CheckLength` Method (Double)

Return true if distance between start and end points is greater than minLength

```csharp
public abstract bool CheckLength( double minLength );
```

**Parameters**

- **minLength** —

#### `Clone` Method

deep copy

```csharp
public abstract D3Line Clone();
```

#### `Coplanar` Method (D3Line)

Returns TRUE if lines lie in the same plane Returns TRUE If lines are PARALLEL or ANTIPARALLEL. N.B. uses parallel(FiniteLine,tol) and antparallel(FiniteLine,tol) functions with given tolerance. For non-parallel lines- this routine works by finding these two vectors- A: the vector connecting the two start points B: the vector product of the two line directions If the angle between these two lines is PI radians (within default tolerance), then TRUE will be returned. If either input line is less than fl_TOLERANCE in length FALSE will be returned

```csharp
public abstract bool Coplanar( D3Line line );
```

**Parameters**

- **line** — 

#### `Coplanar` Method (D3Line, Double)

Returns TRUE if lines lie in the same plane Returns TRUE If lines are PARALLEL or ANTIPARALLEL. N.B. uses parallel(FiniteLine,tol) and antparallel(FiniteLine,tol) functions with given tolerance. For non-parallel lines- this routine works by finding these two vectors- A: the vector connecting the two start points B: the vector product of the two line directions If the angle between these two lines is PI radians (within tolerance tol), then TRUE will be returned. If either input line is less than fl_TOLERANCE in length FALSE will be returned

```csharp
public abstract bool Coplanar( D3Line line , double tol );
```

**Parameters**

- **line** — 
- **tol** —

#### `Create` Method ()

Null constructor

```csharp
public static D3Line Create();
```

#### `Create` Method (D3FiniteLine)

Construct a finite line from a D3FiniteLine

```csharp
public static D3Line Create( D3FiniteLine fLine );
```

**Parameters**

- **fLine** — 

#### `Create` Method (D3FiniteLine, LTYPE)

Construct from a finite line D3FiniteLine and type

```csharp
public static D3Line Create( D3FiniteLine fLine , LTYPE type );
```

**Parameters**

- **fLine** — 
- **type** — 

#### `Create` Method (D3Line)

Copy constructor

```csharp
public static D3Line Create( D3Line orig );
```

**Parameters**

- **orig** — 

#### `Create` Method (D3Point, D3Point)

Construct from start and end point (finite line)

```csharp
public static D3Line Create( D3Point start , D3Point end );
```

**Parameters**

- **start** — 
- **end** — 

#### `Create` Method (D3Point, D3Point, LTYPE)

Construct from start and end points and type

```csharp
public static D3Line Create( D3Point start , D3Point end , LTYPE type );
```

**Parameters**

- **start** — 
- **end** — 
- **type** — 

#### `Create` Method (D3Point, D3Vector)

Construct from start point and direction (semi-infinite line)

```csharp
public static D3Line Create( D3Point start , D3Vector dir );
```

**Parameters**

- **start** — 
- **dir** — 

#### `Create` Method (D3Point, D3Vector, LTYPE)

Construct from start point and direction

```csharp
public static D3Line Create( D3Point start , D3Vector dir , LTYPE type );
```

**Parameters**

- **start** — 
- **dir** — 
- **type** — 

#### `Create` Method (Double, Double, Double, Double, Double, Double)

Construct from 2 sets of coordinates (finite line)

```csharp
public static D3Line Create( double x1 , double y1 , double z1 , double x2 , double y2 , double z2 );
```

**Parameters**

- **x1** — 
- **y1** — 
- **z1** — 
- **x2** — 
- **y2** — 
- **z2** — 

#### `Create` Method (Double, Double, Double, Double, Double, Double, LTYPE)

Construct from 2 sets of coordinates and line type

```csharp
public static D3Line Create( double x1 , double y1 , double z1 , double x2 , double y2 , double z2 , LTYPE type );
```

**Parameters**

- **x1** — 
- **y1** — 
- **z1** — 
- **x2** — 
- **y2** — 
- **z2** — 
- **type** —

#### `Direction` Method

Returns the direction vector of the line

```csharp
public abstract D3Vector Direction();
```

#### `DistanceFrom` Method

returns shortest straight line distance between line and point

```csharp
public abstract double DistanceFrom( D3Point point );
```

**Parameters**

- **point** —

#### `DistanceFromOrigin` Method

returns shortest straight line distance between line and origin

```csharp
public abstract double DistanceFromOrigin();
```

#### `End` Method ()

Returns position at end of line

```csharp
public abstract D3Point End();
```

#### `End` Method (D3Point)

set end point of line

```csharp
public abstract void End( D3Point p );
```

**Parameters**

- **p** — 

#### `End` Method (Double, Double, Double)

set end coordinates of line

```csharp
public abstract void End( double x , double y , double z );
```

**Parameters**

- **x** — 
- **y** — 
- **z** —

#### `Equals` Method (D3Line)

Test for exact equality

```csharp
public abstract bool Equals( D3Line d2 );
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

Return point on line ratio t (0<= t <= 1.0) from start

```csharp
public abstract D3Point InterPoint( double t );
```

**Parameters**

- **t** —

#### `IsFinite` Method

Returns true for line with a start and an end

```csharp
public abstract bool IsFinite();
```

#### `IsInfinite` Method

Return true for bi-directionally infinite lines only

```csharp
public abstract bool IsInfinite();
```

#### `IsSemiInfinite` Method

Return true for semi-infinite lines (one end only)

```csharp
public abstract bool IsSemiInfinite();
```

#### `IsSemiWithEnd` Method

Return true for semi-infinite line with an end point

```csharp
public abstract bool IsSemiWithEnd();
```

#### `IsSemiWithStart` Method

Return true for semi-infinite line with a start point

```csharp
public abstract bool IsSemiWithStart();
```

#### `Length` Method

Returns non-negative distance between start and end points. Always finite since the start and end points are used to define the direction of the line for (semi) infinite lines and not the extent.

```csharp
public abstract double Length();
```

#### `LineType` Method ()

Return line type {infinite,semiWithStart,semiWithEnd,finite}

```csharp
public abstract LTYPE LineType();
```

#### `LineType` Method (LTYPE)

set line type possibilities are - D3Line.finite D3Line.infinite D3Line.semiWithStart D3Line.semiWithEnd

```csharp
public abstract void LineType( LTYPE type );
```

**Parameters**

- **type** —

#### `LTypeToString` Method

Convert line type to string

```csharp
public abstract string LTypeToString( LTYPE lt );
```

**Parameters**

- **lt** —

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

Mirroy Y about origin

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

shift the start and end points by vector v

```csharp
public abstract void MoveBy( D3Vector v );
```

**Parameters**

- **v** —

#### `NearestPoint` Method

Return point on line nearest given point

```csharp
public abstract D3Point NearestPoint( D3Point pt );
```

**Parameters**

- **pt** —

#### `NearestPointToOrigin` Method

Return point on line closest to origin

```csharp
public abstract D3Point NearestPointToOrigin();
```

#### `OnLine` Method (D3Point)

true if given point is within distance fl_TOLERANCE of line

```csharp
public abstract bool OnLine( D3Point p );
```

**Parameters**

- **p** — 

#### `OnLine` Method (D3Point, Double)

true if given point is within distance "tol" of line

```csharp
public abstract bool OnLine( D3Point p , double tol );
```

**Parameters**

- **p** — 
- **tol** —

#### `Parallel` Method (D3Line)

Returns true if lines point in the SAME DIRECTION Tolerance is max angle between the directions measured in RADIANS (Default tolerance=1.E-6 rads) N.B. will return FALSE for antiparallel lines.

```csharp
public abstract bool Parallel( D3Line line );
```

**Parameters**

- **line** — 

#### `Parallel` Method (D3Line, Double)

Returns true if lines point in the SAME DIRECTION Tolerance is max angle between the directions measured in RADIANS N.B. will return FALSE for antiparallel lines.

```csharp
public abstract bool Parallel( D3Line line , double tolerance );
```

**Parameters**

- **line** — 
- **tolerance** —

#### `PerpendicularDistance` Method

Returns the distance of the arg point from the perpendicularPoint() calculated using previous function above.

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

Returns polar angle of direction of line

```csharp
public abstract double PolarAngleInRadians();
```

#### `Reverse` Method

swap start and end points (reverses direction of line) N.B. semiWithEnd becomes a semiWithStart and vice versa

```csharp
public abstract void Reverse();
```

#### `ScaleBy` Method (Double)

Scale uniformly by value s

```csharp
public abstract void ScaleBy( double s );
```

**Parameters**

- **s** — 

#### `ScaleBy` Method (Double, D3Point)

Scale coordinates by s about pivot

```csharp
public abstract void ScaleBy( double s , D3Point pivot );
```

**Parameters**

- **s** — 
- **pivot** —

#### `SetValue` Method (D3Point, D3Point)

set start and end points of line

```csharp
public abstract void SetValue( D3Point start , D3Point end );
```

**Parameters**

- **start** — 
- **end** — 

#### `SetValue` Method (Double, Double, Double, Double, Double, Double)

set start and end coordinate points of line

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

Returns position at start of line

```csharp
public abstract D3Point Start();
```

#### `Start` Method (D3Point)

set start point of line

```csharp
public abstract void Start( D3Point p );
```

**Parameters**

- **p** — 

#### `Start` Method (Double, Double, Double)

set start coordinates of line

```csharp
public abstract void Start( double x , double y , double z );
```

**Parameters**

- **x** — 
- **y** — 
- **z** —

#### `ToString` Method

Returns string describing the D3Line

```csharp
public abstract string ToString();
```

#### `TValue` Method

Distance of point p from start point of line in the direction of the line. The distance is returned in units such that one line length = 1 unit.

```csharp
public abstract double TValue( D3Point p );
```

**Parameters**

- **p** —

#### `UnitDirection` Method

Returns the unit vector of the line

```csharp
public abstract D3Vector UnitDirection();
```

## Operators

#### `Equality` Operator

invoked by left == right. True if start,end and linetype match exactly

```csharp
public static bool operator ==( D3Line left , D3Line right );
```

**Parameters**

- **left** — 
- **right** —

#### `Inequality` Operator

invoked by left != right. True if any of start, end or lineType does not match excalty

```csharp
public static bool operator !=( D3Line left , D3Line right );
```

**Parameters**

- **left** — 
- **right** —
