---
title: Aveva.Pdms.Maths.Geometry.D2Vector Class
namespace: Aveva.Pdms.Maths.Geometry
assembly: Aveva.Pdms.Maths.Geometry
kind: Class
source: Aveva.Pdms.Maths.Geometry
---

# Aveva.Pdms.Maths.Geometry.D2Vector Class

> 2-D vector class

## Syntax

```csharp
public abstract class D2Vector
```

## Inheritance

`System.Object` → `Aveva.Pdms.Maths.Geometry.D2Vector`

## Thread Safety

Public static ( Shared in Visual Basic) members of this type are
safe for multithreaded operations. Instance members are not guaranteed to be
thread-safe.

## Requirements

Namespace:
Aveva.Pdms.Maths.Geometry
Assembly: Aveva.Pdms.Maths.Geometry (in Aveva.Pdms.Maths.Geometry.dll)

## Fields

#### `D2DOWN` Field

static constant - in negative Y direction

```csharp
public static D2Vector D2DOWN;
```

#### `D2LEFT` Field

static constant - in negative X directiov

```csharp
public static D2Vector D2LEFT;
```

#### `D2RIGHT` Field

static constants - in positive X direction

```csharp
public static D2Vector D2RIGHT;
```

#### `D2UP` Field

static constant - in positive Y direction

```csharp
public static D2Vector D2UP;
```

## Properties

#### `X` Property

property to set/get X coordinate of vector

```csharp
public abstract double X {get; set;}
```

#### `Y` Property

property to set/get Y coordinate

```csharp
public abstract double Y {get; set;}
```

## Methods

#### `Add` Method

Add two vectors

```csharp
public abstract D2Vector Add( D2Vector v2 );
```

**Parameters**

- **v2** —

#### `Angle` Method

return angle between vectors in radians; range: -pi to pi

```csharp
public abstract double Angle( D2Vector v );
```

**Parameters**

- **v** —

#### `Antiparallel` Method (D2Vector)

Returns true if vectors are in opposite direction

```csharp
public abstract bool Antiparallel( D2Vector v );
```

**Parameters**

- **v** — 

#### `Antiparallel` Method (D2Vector, Double)

returns true if vectors are in opposite direction, within delta

```csharp
public abstract bool Antiparallel( D2Vector v , double delta );
```

**Parameters**

- **v** — 
- **delta** —

#### `AsPoint` Method

Return vector as a point

```csharp
public abstract D2Point AsPoint();
```

#### `Clone` Method

```csharp
public abstract D2Vector Clone();
```

#### `Create` Method ()

Create a default D2Vector

```csharp
public static D2Vector Create();
```

**Return Value**

D2Vector

#### `Create` Method (D2Point, D2Point)

Create a D2Vector from 2 D2Points

```csharp
public static D2Vector Create( D2Point a , D2Point b );
```

**Parameters**

- **a** — 
- **b** — 

**Return Value**

D2Vector

#### `Create` Method (D2Vector)

Create a vector as a copy of another

```csharp
public static D2Vector Create( D2Vector v );
```

**Parameters**

- **v** — 

#### `Create` Method (Double, Double)

Create a D2Vector from two coordinate values

```csharp
public static D2Vector Create( double x , double y );
```

**Parameters**

- **x** — 
- **y** — 

**Return Value**

D2Vector

#### `Create` Method (Double[])

Create a D2Vector from an array of 2 doubles

```csharp
public static D2Vector Create( double[] v );
```

**Parameters**

- **v** — 

**Return Value**

D2Vector

#### `Cross` Method

Returns cross product

```csharp
public abstract double Cross( D2Vector v );
```

**Parameters**

- **v** —

#### `Divide` Method

Divid vector by given value

```csharp
public abstract D2Vector Divide( double d );
```

**Parameters**

- **d** —

#### `Dot` Method

Returns dot product

```csharp
public abstract double Dot( D2Vector v );
```

**Parameters**

- **v** —

#### `Equals` Method (D2Vector)

Return true if vectors are same

```csharp
public abstract bool Equals( D2Vector v );
```

**Parameters**

- **v** — 

#### `Equals` Method (D2Vector, Double)

Return true if vectors are equal within given delta length

```csharp
public abstract bool Equals( D2Vector v , double deltaMag );
```

**Parameters**

- **v** — 
- **deltaMag** — 

#### `Equals` Method (D2Vector, Double, Double)

Return true if vectors are equla within given delta angle and given delta length of each other

```csharp
public abstract bool Equals( D2Vector v , double deltaMag , double deltaAng );
```

**Parameters**

- **v** — 
- **deltaMag** — 
- **deltaAng** — 

#### `Equals` Method (Object)

Override equals

```csharp
public override bool Equals( object a );
```

**Parameters**

- **a** —

#### `GetHashCode` Method

override gethashcode

```csharp
public override int GetHashCode();
```

#### `GetUnit` Method

returns unit magnitude equivalent vector; returns (0,0) if original is (0,0)

```csharp
public abstract D2Vector GetUnit();
```

#### `IsZero` Method

Return true if both X and Y are zero

```csharp
public abstract bool IsZero();
```

#### `Magnitude` Method

magnitude of vector

```csharp
public abstract double Magnitude();
```

#### `MirrorX` Method

Mirror in X

```csharp
public abstract void MirrorX();
```

#### `MirrorY` Method

Mirror in Y

```csharp
public abstract void MirrorY();
```

#### `Multiply` Method

Multiply vector by given value

```csharp
public abstract D2Vector Multiply( double d );
```

**Parameters**

- **d** —

#### `NearestAxis` Method

get unit vector of axis which is closest

```csharp
public abstract D2Vector NearestAxis();
```

#### `Negate` Method

Negate a vector

```csharp
public abstract D2Vector Negate();
```

#### `Parallel` Method (D2Vector)

Returns true if vectors are in same direction

```csharp
public abstract bool Parallel( D2Vector v );
```

**Parameters**

- **v** — 

#### `Parallel` Method (D2Vector, Double)

return true if vectors are in same direction, within delta

```csharp
public abstract bool Parallel( D2Vector v , double delta );
```

**Parameters**

- **v** — 
- **delta** —

#### `Parse` Method

Creates a D2Vector from a string of the format:"xxx,yyy"

```csharp
public abstract D2Vector Parse( string str );
```

#### `Perpendicular` Method (D2Vector)

Returns true if vectors are perpendicular

```csharp
public abstract bool Perpendicular( D2Vector v );
```

**Parameters**

- **v** — 

#### `Perpendicular` Method (D2Vector, Double)

Returns true if vectors are perpendicular within delta

```csharp
public abstract bool Perpendicular( D2Vector v , double delta );
```

**Parameters**

- **v** — 
- **delta** —

#### `PolarAngle` Method

Return polarAngle between 0.0 and fl_TWO_PI"

```csharp
public abstract double PolarAngle();
```

#### `Rotate90` Method

rotate 90 degrees

```csharp
public abstract void Rotate90();
```

#### `RotateByDegrees` Method

rotate vector by angle given in degrees

```csharp
public abstract void RotateByDegrees( double degrees );
```

**Parameters**

- **degrees** —

#### `RotateByRadians` Method

rotate vector by angle given in radians

```csharp
public abstract void RotateByRadians( double radians );
```

**Parameters**

- **radians** —

#### `ScaleBy` Method

Scale x and y uniformly

```csharp
public abstract void ScaleBy( double s );
```

**Parameters**

- **s** — scale factor

#### `SetXY` Method

Set X and Y coordinates

```csharp
public abstract void SetXY( double x , double y );
```

**Parameters**

- **x** — 
- **y** —

#### `Subtract` Method

Subtract two vectors

```csharp
public abstract D2Vector Subtract( D2Vector v2 );
```

**Parameters**

- **v2** —

#### `ToString` Method

Returns a string describing the contents of the D2Vector

```csharp
public abstract string ToString();
```

## Operators

#### `Addition` Operator

Invoked by v1+v2

```csharp
public static D2Vector operator +( D2Vector v1 , D2Vector v2 );
```

**Parameters**

- **v1** — 
- **v2** —

#### `Division` Operator

invoked by v1/d

```csharp
public static D2Vector operator /( D2Vector v1 , double d );
```

**Parameters**

- **v1** — 
- **d** —

#### `Equality` Operator

Invoked by left== right (exact equality)

```csharp
public static bool operator ==( D2Vector left , D2Vector right );
```

**Parameters**

- **left** — 
- **right** —

#### `Inequality` Operator

Invoked by left != right (exact inequality)

```csharp
public static bool operator !=( D2Vector left , D2Vector right );
```

**Parameters**

- **left** — 
- **right** —

#### `Multiplication` Operator

invoked by v1d

```csharp
public static D2Vector operator *( D2Vector v1 , double d );
```

**Parameters**

- **v1** — 
- **d** —

#### `Subtraction` Operator

invoked by v1-v2

```csharp
public static D2Vector operator -( D2Vector v1 , D2Vector v2 );
```

**Parameters**

- **v1** — 
- **v2** —

#### `Unary Negation` Operator

invoked by -v

```csharp
public static D2Vector operator -( D2Vector v );
```

**Parameters**

- **v** —
