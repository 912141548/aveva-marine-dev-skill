---
title: Aveva.Pdms.Maths.Geometry.D2Point Class
namespace: Aveva.Pdms.Maths.Geometry
assembly: Aveva.Pdms.Maths.Geometry
kind: Class
source: Aveva.Pdms.Maths.Geometry
---

# Aveva.Pdms.Maths.Geometry.D2Point Class

> D2Point - a 2-D point class

## Syntax

```csharp
public abstract class D2Point
```

## Inheritance

`System.Object` → `Aveva.Pdms.Maths.Geometry.D2Point`

## Thread Safety

Public static ( Shared in Visual Basic) members of this type are
safe for multithreaded operations. Instance members are not guaranteed to be
thread-safe.

## Requirements

Namespace:
Aveva.Pdms.Maths.Geometry
Assembly: Aveva.Pdms.Maths.Geometry (in Aveva.Pdms.Maths.Geometry.dll)

## Properties

#### `X` Property

set/get X coordinate

```csharp
public abstract double X {get; set;}
```

#### `Y` Property

set/get Y coordinate

```csharp
public abstract double Y {get; set;}
```

## Methods

#### `Add` Method

Point = this + vector v2

```csharp
public abstract D2Point Add( D2Vector v2 );
```

**Parameters**

- **v2** —

#### `AsVector` Method

explicit conversion to D2Vector

```csharp
public abstract D2Vector AsVector();
```

#### `BottomPoint` Method

Returns the bottom-most of two points (min Y)

```csharp
public D2Point BottomPoint( D2Point a , D2Point b );
```

**Parameters**

- **a** — 
- **b** — 

**Return Value**

D2Point

#### `Clone` Method

```csharp
public abstract D2Point Clone();
```

#### `Create` Method ()

Create a D2Point from two coordinate values

```csharp
public static D2Point Create();
```

#### `Create` Method (D2Point)

Copy a D2Point

```csharp
public static D2Point Create( D2Point p );
```

**Parameters**

- **p** — 

#### `Create` Method (Double, Double)

Create a D2Point from two coordinate values

```csharp
public static D2Point Create( double x , double y );
```

**Parameters**

- **x** — 
- **y** — 

#### `Create` Method (Double[])

Create a D2Point from an array of 2 doubles

```csharp
public static D2Point Create( double[] v );
```

**Parameters**

- **v** — 2 dimension array of doubles

#### `Ddistance` Method (D2Point)

Return distance from given point

```csharp
public abstract double Ddistance( D2Point b );
```

**Parameters**

- **b** — 

#### `Ddistance` Method (D2Point, D2Point)

Distance between two points

```csharp
public double Ddistance( D2Point a , D2Point b );
```

**Parameters**

- **a** — 
- **b** — 

**Return Value**

double

#### `Equals` Method (D2Point)

Points are within fl_TOLERANCE of each other

```csharp
public abstract bool Equals( D2Point p2 );
```

**Parameters**

- **p2** — 

#### `Equals` Method (D2Point, Double)

Points are within delta of each other

```csharp
public abstract bool Equals( D2Point p2 , double delta );
```

**Parameters**

- **p2** — 
- **delta** — 

#### `Equals` Method (Object)

required override of Equals() when we define operator ==

```csharp
public override bool Equals( object a );
```

**Parameters**

- **a** — 

**Return Value**

true if equal

#### `GetHashCode` Method

required override of GetHashCode() when we define operator ==

```csharp
public override int GetHashCode();
```

#### `LeftPoint` Method

Returns the left-most of two points (min X)

```csharp
public D2Point LeftPoint( D2Point a , D2Point b );
```

**Parameters**

- **a** — 
- **b** — 

**Return Value**

D2Point

#### `MidPoint` Method

Returns the mid point between two points

```csharp
public D2Point MidPoint( D2Point a , D2Point b );
```

**Parameters**

- **a** — 
- **b** — 

**Return Value**

D2Point

#### `MirrorX` Method ()

Mirror X about origin

```csharp
public abstract void MirrorX();
```

#### `MirrorX` Method (D2Point)

Mirror X about pivot

```csharp
public abstract void MirrorX( D2Point pivot );
```

**Parameters**

- **pivot** —

#### `MirrorY` Method ()

Mirror Y about origin

```csharp
public abstract void MirrorY();
```

#### `MirrorY` Method (D2Point)

Mirror Y about pivot

```csharp
public abstract void MirrorY( D2Point pivot );
```

**Parameters**

- **pivot** —

#### `MoveBy` Method (D2Vector)

Offset by given vector

```csharp
public abstract void MoveBy( D2Vector v );
```

**Parameters**

- **v** — 

#### `MoveBy` Method (Double, Double)

Offset by given x,y values

```csharp
public abstract void MoveBy( double x , double y );
```

**Parameters**

- **x** — 
- **y** —

#### `MoveTo` Method

Move point to given x, y coordinates

```csharp
public abstract void MoveTo( double x , double y );
```

**Parameters**

- **x** — 
- **y** —

#### `NearestPoint` Method

Return whichever of a and b is nearest

```csharp
public abstract D2Point NearestPoint( D2Point a , D2Point b );
```

**Parameters**

- **a** — 
- **b** —

#### `Parse` Method

Creates a D2Point from a string of the format:"xxx,yyy"

```csharp
public abstract D2Point Parse( string str );
```

#### `RightPoint` Method

Returns the right-most of two points (max X)

```csharp
public D2Point RightPoint( D2Point a , D2Point b );
```

**Parameters**

- **a** — 
- **b** — 

**Return Value**

D2Point

#### `RotateByDegrees` Method (Double)

about origin in degrees

```csharp
public abstract void RotateByDegrees( double angle );
```

**Parameters**

- **angle** — 

#### `RotateByDegrees` Method (Double, D2Point)

about pivot

```csharp
public abstract void RotateByDegrees( double angle , D2Point pivot );
```

**Parameters**

- **angle** — 
- **pivot** —

#### `RotateByRadians` Method (Double)

about origin in radians

```csharp
public abstract void RotateByRadians( double angle );
```

**Parameters**

- **angle** — 

#### `RotateByRadians` Method (Double, D2Point)

about pivot

```csharp
public abstract void RotateByRadians( double angle , D2Point pivot );
```

**Parameters**

- **angle** — 
- **pivot** —

#### `ScaleBy` Method (Double)

Scale about origin

```csharp
public abstract void ScaleBy( double s );
```

**Parameters**

- **s** — 

#### `ScaleBy` Method (Double, D2Point)

Scale about pivot

```csharp
public abstract void ScaleBy( double s , D2Point pivot );
```

**Parameters**

- **s** — 
- **pivot** —

#### `SetXY` Method

Set x and y coordinates

```csharp
public abstract void SetXY( double x , double y );
```

**Parameters**

- **x** — 
- **y** —

#### `Subtract` Method (D2Point)

Vector which is the difference between two points

```csharp
public abstract D2Vector Subtract( D2Point p2 );
```

**Parameters**

- **p2** — 

#### `Subtract` Method (D2Vector)

Point = this -vector v2

```csharp
public abstract D2Point Subtract( D2Vector v2 );
```

**Parameters**

- **v2** —

#### `TopPoint` Method

Returns the top-most of two points (max Y)

```csharp
public D2Point TopPoint( D2Point a , D2Point b );
```

**Parameters**

- **a** — 
- **b** — 

**Return Value**

D2Point

#### `ToString` Method

Returns a string describing the contents of the D2Point

```csharp
public abstract string ToString();
```

## Operators

#### `Addition` Operator

Create a point p = p1 + v

```csharp
public static D2Point operator +( D2Point p1 , D2Vector v );
```

**Parameters**

- **p1** — 
- **v** —

#### `Equality` Operator

invoked by left == right

```csharp
public static bool operator ==( D2Point left , D2Point right );
```

**Parameters**

- **left** — 
- **right** —

#### `Inequality` Operator

Invoked by left != right

```csharp
public static bool operator !=( D2Point left , D2Point right );
```

**Parameters**

- **left** — 
- **right** —

#### `Subtraction` Operator (D2Point, D2Point)

Create a vector v = p1 + p2

```csharp
public static D2Vector operator -( D2Point p1 , D2Point p2 );
```

**Parameters**

- **p1** — 
- **p2** — 

#### `Subtraction` Operator (D2Point, D2Vector)

Create a point p = p1 - v

```csharp
public static D2Point operator -( D2Point p1 , D2Vector v );
```

**Parameters**

- **p1** — 
- **v** —
