---
title: Aveva.Pdms.Maths.Geometry.D3Point Class
namespace: Aveva.Pdms.Maths.Geometry
assembly: Aveva.Pdms.Maths.Geometry
kind: Class
source: Aveva.Pdms.Maths.Geometry
---

# Aveva.Pdms.Maths.Geometry.D3Point Class

> 3D Point class

## Syntax

```csharp
public abstract class D3Point
```

## Inheritance

`System.Object` → `Aveva.Pdms.Maths.Geometry.D3Point`

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

#### `Z` Property

set/get Z coordinate

```csharp
public abstract double Z {get; set;}
```

## Methods

#### `Add` Method

Add a point to a vector to create new point

```csharp
public abstract D3Point Add( D3Vector v1 );
```

**Parameters**

- **v1** —

#### `AsD2Point` Method

Convert to 2D point

```csharp
public abstract D2Point AsD2Point();
```

#### `AsVector` Method

explicit conversion to D3Vector

```csharp
public abstract D3Vector AsVector();
```

#### `Clone` Method

Deep copy

```csharp
public abstract D3Point Clone();
```

#### `Create` Method ()

Default constructor

```csharp
public static D3Point Create();
```

#### `Create` Method (D3Point)

Copy a D3Point

```csharp
public static D3Point Create( D3Point p );
```

**Parameters**

- **p** — 

#### `Create` Method (Double, Double, Double)

Construct a D3Point from 3 coordinates

```csharp
public static D3Point Create( double x , double y , double z );
```

**Parameters**

- **x** — 
- **y** — 
- **z** — 

#### `Create` Method (Double[])

Construct a D3Point from an array of 3 coordinates

```csharp
public static D3Point Create( double[] v );
```

**Parameters**

- **v** —

#### `Ddistance` Method

Returns the distance from the given point

```csharp
public abstract double Ddistance( D3Point b );
```

**Parameters**

- **b** —

#### `Equals` Method (D3Point)

Returns TRUE if p is within default distance of object point

```csharp
public abstract bool Equals( D3Point p );
```

**Parameters**

- **p** — 

#### `Equals` Method (D3Point, Double)

Returns TRUE if p is within distance delta of object point

```csharp
public abstract bool Equals( D3Point p , double delta );
```

**Parameters**

- **p** — 
- **delta** — 

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

#### `MirrorX` Method ()

Set to position mirror X about origin

```csharp
public abstract void MirrorX();
```

#### `MirrorX` Method (D3Point)

Set to position mirror X about pivot

```csharp
public abstract void MirrorX( D3Point pivot );
```

**Parameters**

- **pivot** —

#### `MirrorY` Method ()

Set to position mirror Y about origin

```csharp
public abstract void MirrorY();
```

#### `MirrorY` Method (D3Point)

Set to position mirror Y about pivot

```csharp
public abstract void MirrorY( D3Point pivot );
```

**Parameters**

- **pivot** —

#### `MirrorZ` Method ()

Set to position with mirror Z about origin

```csharp
public abstract void MirrorZ();
```

#### `MirrorZ` Method (D3Point)

Set to position mirror Z about pivot

```csharp
public abstract void MirrorZ( D3Point pivot );
```

**Parameters**

- **pivot** —

#### `MoveBy` Method (D3Vector)

Move along the specified vector

```csharp
public abstract void MoveBy( D3Vector v );
```

**Parameters**

- **v** — 

#### `MoveBy` Method (Double, Double, Double)

Move point by given delata values

```csharp
public abstract void MoveBy( double x , double y , double z );
```

**Parameters**

- **x** — 
- **y** — 
- **z** —

#### `MoveTo` Method

Move point to absolute position x,y,z

```csharp
public abstract void MoveTo( double x , double y , double z );
```

**Parameters**

- **x** — 
- **y** — 
- **z** —

#### `Parse` Method

Creates a D3Point from a string of the format:"xxx,yyy,zzz" (opposite of ToString)

```csharp
public abstract D3Point Parse( string str );
```

**Parameters**

- **str** —

#### `ScaleBy` Method (Double)

Scale uniformly about origin

```csharp
public abstract void ScaleBy( double s );
```

**Parameters**

- **s** — 

#### `ScaleBy` Method (Double, D3Point)

Scale about pivot

```csharp
public abstract void ScaleBy( double s , D3Point pivot );
```

**Parameters**

- **s** — 
- **pivot** —

#### `SetXYZ` Method

Set x,y,z coordinate values

```csharp
public abstract void SetXYZ( double x , double y , double z );
```

**Parameters**

- **x** — 
- **y** — 
- **z** —

#### `Subtract` Method (D3Point)

Subtract two points to get a vector

```csharp
public abstract D3Vector Subtract( D3Point p1 );
```

**Parameters**

- **p1** — 

#### `Subtract` Method (D3Vector)

Subtract a vector from apoint to create new point

```csharp
public abstract D3Point Subtract( D3Vector v1 );
```

**Parameters**

- **v1** —

#### `ToString` Method

Returns a string describing the contents of the D3Point

```csharp
public abstract string ToString();
```

#### `WithinTolerance` Method

Returns true if point p is within Tolerance tol of this point

```csharp
public abstract bool WithinTolerance( D3Point p , double tol );
```

**Parameters**

- **p** — 
- **tol** —

## Operators

#### `Addition` Operator

invoked by p1 + v1

```csharp
public static D3Point operator +( D3Point p1 , D3Vector v1 );
```

**Parameters**

- **p1** — 
- **v1** —

#### `Equality` Operator

invoked by left == right

```csharp
public static bool operator ==( D3Point left , D3Point right );
```

**Parameters**

- **left** — 
- **right** —

#### `Inequality` Operator

invoked by left != right

```csharp
public static bool operator !=( D3Point left , D3Point right );
```

**Parameters**

- **left** — 
- **right** —

#### `Subtraction` Operator (D3Point, D3Point)

invoked by p1-p2

```csharp
public static D3Vector operator -( D3Point p1 , D3Point p2 );
```

**Parameters**

- **p1** — 
- **p2** — 

#### `Subtraction` Operator (D3Point, D3Vector)

invoked by p1-v1

```csharp
public static D3Point operator -( D3Point p1 , D3Vector v1 );
```

**Parameters**

- **p1** — 
- **v1** —
