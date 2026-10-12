---
title: Aveva.Pdms.Maths.Geometry.D3Vector Class
namespace: Aveva.Pdms.Maths.Geometry
assembly: Aveva.Pdms.Maths.Geometry
kind: Class
source: Aveva.Pdms.Maths.Geometry
---

# Aveva.Pdms.Maths.Geometry.D3Vector Class

> 3D Vector class

## Syntax

```csharp
public abstract class D3Vector
```

## Inheritance

`System.Object` → `Aveva.Pdms.Maths.Geometry.D3Vector`

## Thread Safety

Public static ( Shared in Visual Basic) members of this type are
safe for multithreaded operations. Instance members are not guaranteed to be
thread-safe.

## Requirements

Namespace:
Aveva.Pdms.Maths.Geometry
Assembly: Aveva.Pdms.Maths.Geometry (in Aveva.Pdms.Maths.Geometry.dll)

## Fields

#### `D3DOWN` Field

static constant - down

```csharp
public static D3Vector D3DOWN;
```

#### `D3EAST` Field

static constant - east

```csharp
public static D3Vector D3EAST;
```

#### `D3NORTH` Field

static constant - north

```csharp
public static D3Vector D3NORTH;
```

#### `D3SOUTH` Field

static constant - south

```csharp
public static D3Vector D3SOUTH;
```

#### `D3UP` Field

static constant - up

```csharp
public static D3Vector D3UP;
```

#### `D3WEST` Field

static constant - west

```csharp
public static D3Vector D3WEST;
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

#### `Z` Property

property to set/get Z coordinate of vector

```csharp
public abstract double Z {get; set;}
```

## Methods

#### `Add` Method

Add two vectors

```csharp
public abstract D3Vector Add( D3Vector v2 );
```

**Parameters**

- **v2** —

#### `Angle` Method

Return the angle of the vector (in degrees)

```csharp
public abstract double Angle( D3Vector v );
```

**Parameters**

- **v** —

#### `Antiparallel` Method (D3Vector)

Returns true if vectors are parallel (within default tolerance) and in the opposite direction

```csharp
public abstract bool Antiparallel( D3Vector v );
```

**Parameters**

- **v** — 

#### `Antiparallel` Method (D3Vector, Double)

Returns true if vectors are parallel (within given tolerance) and in the opposite direction

```csharp
public abstract bool Antiparallel( D3Vector v , double tol );
```

**Parameters**

- **v** — 
- **tol** —

#### `ApproxProject` Method

Return an approximate projection onto z =0 plane

```csharp
public abstract void ApproxProject( ref int ix , ref int iy );
```

**Parameters**

- **ix** — 
- **iy** —

#### `AsPoint` Method

Explicit conversion of vector to D3Point

```csharp
public abstract D3Point AsPoint();
```

#### `Clone` Method

Returns a deep copy of the vector

```csharp
public abstract D3Vector Clone();
```

#### `Create` Method ()

Default constructor - Creates a D3Vector with default values (0.0,0.0,0.0)

```csharp
public static D3Vector Create();
```

#### `Create` Method (D3Point, D3Point)

Creates a 3d vector from point pa to point pb

```csharp
public static D3Vector Create( D3Point pa , D3Point pb );
```

**Parameters**

- **pa** — 
- **pb** — 

#### `Create` Method (D3Vector)

Copies a D3Vector

```csharp
public static D3Vector Create( D3Vector v );
```

**Parameters**

- **v** — 

#### `Create` Method (Double, Double, Double)

Creates a 3d vector with coordinates x,y,z

```csharp
public static D3Vector Create( double x , double y , double z );
```

**Parameters**

- **x** — 
- **y** — 
- **z** — 

#### `Create` Method (Double[])

Creates a 3d vector with coordinates from array v

```csharp
public static D3Vector Create( double[] v );
```

**Parameters**

- **v** —

#### `Cross` Method

Return the cross product

```csharp
public abstract D3Vector Cross( D3Vector v );
```

**Parameters**

- **v** —

#### `Divide` Method

Divide vector by a scalar value

```csharp
public abstract D3Vector Divide( double d );
```

**Parameters**

- **d** —

#### `Dot` Method

Return the dot product

```csharp
public abstract double Dot( D3Vector v );
```

**Parameters**

- **v** —

#### `Equals` Method (D3Vector)

Returns true if vectors are equal within default tolerance of size and angle

```csharp
public abstract bool Equals( D3Vector v );
```

**Parameters**

- **v** — 

#### `Equals` Method (D3Vector, Double)

Returns true if vectors are equal within given tolerance of size and default angle tolerance

```csharp
public abstract bool Equals( D3Vector v , double deltaMag );
```

**Parameters**

- **v** — 
- **deltaMag** — 

#### `Equals` Method (D3Vector, Double, Double)

Returns true if vectors are equal within given tolerance of size and angle

```csharp
public abstract bool Equals( D3Vector v , double deltaMag , double deltaAng );
```

**Parameters**

- **v** — 
- **deltaMag** — 
- **deltaAng** — 

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

#### `GetUnit` Method

Returns unit magnitude equivalent vector; returns (0,0,0) if original is (0,0,0)

```csharp
public abstract D3Vector GetUnit();
```

#### `IsZero` Method

Returns true if x=y=z=0

```csharp
public abstract bool IsZero();
```

#### `Magnitude` Method

Return the length of the vector

```csharp
public abstract double Magnitude();
```

#### `Multiply` Method

Multiply vector by a scalar value

```csharp
public abstract D3Vector Multiply( double d );
```

**Parameters**

- **d** —

#### `NearestAxis` Method

Get unit vector of axis which is closest

```csharp
public abstract D3Vector NearestAxis();
```

#### `Negate` Method

Negate the vector

```csharp
public abstract D3Vector Negate();
```

#### `Parallel` Method (D3Vector)

Returns true if vectors are parallel (within default tolerance) and in the same direction

```csharp
public abstract bool Parallel( D3Vector v );
```

**Parameters**

- **v** — 

#### `Parallel` Method (D3Vector, Double)

Returns true if vectors are parallel (within given tolerance) and in the same direction

```csharp
public abstract bool Parallel( D3Vector v , double tol );
```

**Parameters**

- **v** — 
- **tol** —

#### `Parse` Method

Returns a D3Vector constructed from a string of form "xxx,yyy,zzz" (opposite of ToString)

```csharp
public abstract D3Vector Parse( string str );
```

**Parameters**

- **str** —

#### `Perpendicular` Method (D3Vector)

Returns true if vectors are perpendicular (within default tolerance)

```csharp
public abstract bool Perpendicular( D3Vector v );
```

**Parameters**

- **v** — 

#### `Perpendicular` Method (D3Vector, Double)

Returns true if vectors are perpendicular (within given tolerance)

```csharp
public abstract bool Perpendicular( D3Vector v , double delta );
```

**Parameters**

- **v** — 
- **delta** —

#### `ProjectOntoLine` Method

Returns vector which is a projection of this vector onto given line

```csharp
public abstract D3Vector ProjectOntoLine( D3Vector line );
```

**Parameters**

- **line** —

#### `ProjectOntoPlane` Method

Returns vector which is projection of this vector onto given plane

```csharp
public abstract D3Vector ProjectOntoPlane( D3Vector normal );
```

**Parameters**

- **normal** —

#### `ScaleBy` Method

Scale x,y,z uniformly by scalar value

```csharp
public abstract void ScaleBy( double s );
```

**Parameters**

- **s** —

#### `SetXYZ` Method

set x,y,z coordinates

```csharp
public abstract void SetXYZ( double x , double y , double z );
```

**Parameters**

- **x** — 
- **y** — 
- **z** —

#### `Subtract` Method

Subtract two vectors

```csharp
public abstract D3Vector Subtract( D3Vector v2 );
```

**Parameters**

- **v2** —

#### `ToString` Method

Returns a string describing the values of the D3Vector

```csharp
public abstract string ToString();
```

## Operators

#### `Addition` Operator

invoked by v1 + v2

```csharp
public static D3Vector operator +( D3Vector v1 , D3Vector v2 );
```

**Parameters**

- **v1** — 
- **v2** —

#### `Division` Operator

Invoked by v1 / v2

```csharp
public static D3Vector operator /( D3Vector v1 , double d );
```

**Parameters**

- **v1** — 
- **d** —

#### `Equality` Operator

invoked by left == right (exact equality)

```csharp
public static bool operator ==( D3Vector left , D3Vector right );
```

**Parameters**

- **left** — 
- **right** —

#### `Inequality` Operator

invoked by left != right

```csharp
public static bool operator !=( D3Vector left , D3Vector right );
```

**Parameters**

- **left** — 
- **right** —

#### `Multiplication` Operator

Invoked by v1*v2

```csharp
public static D3Vector operator *( D3Vector v1 , double d );
```

**Parameters**

- **v1** — 
- **d** —

#### `Subtraction` Operator

Invoked by v1 - v2

```csharp
public static D3Vector operator -( D3Vector v1 , D3Vector v2 );
```

**Parameters**

- **v1** — 
- **v2** —

#### `Unary Negation` Operator

Invoked by -v

```csharp
public static D3Vector operator -( D3Vector v );
```

**Parameters**

- **v** —
