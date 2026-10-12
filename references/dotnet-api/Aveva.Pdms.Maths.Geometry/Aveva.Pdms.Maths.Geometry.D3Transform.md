---
title: Aveva.Pdms.Maths.Geometry.D3Transform Class
namespace: Aveva.Pdms.Maths.Geometry
assembly: Aveva.Pdms.Maths.Geometry
kind: Class
source: Aveva.Pdms.Maths.Geometry
---

# Aveva.Pdms.Maths.Geometry.D3Transform Class

> D3Transform - solid body transformations

## Syntax

```csharp
public abstract class D3Transform
```

## Inheritance

`System.Object` → `Aveva.Pdms.Maths.Geometry.D3Transform`

## Thread Safety

Public static ( Shared in Visual Basic) members of this type are
safe for multithreaded operations. Instance members are not guaranteed to be
thread-safe.

## Requirements

Namespace:
Aveva.Pdms.Maths.Geometry
Assembly: Aveva.Pdms.Maths.Geometry (in Aveva.Pdms.Maths.Geometry.dll)

## Methods

#### `AsArray12` Method

Returns array containing rotation matrix (in column order) and shift

```csharp
public abstract double[] AsArray12();
```

#### `BeIdentity` Method

Set the transform to be the identity transform

```csharp
public abstract void BeIdentity();
```

#### `Clone` Method

Deep copy

```csharp
public abstract D3Transform Clone();
```

#### `Create` Method ()

Default constructor

```csharp
public static D3Transform Create();
```

#### `Create` Method (D3Matrix, D3Vector)

Construct a transform from a rotation matrix and a shift vector

```csharp
public static D3Transform Create( D3Matrix theRot , D3Vector theShift );
```

**Parameters**

- **theRot** — 
- **theShift** — 

#### `Create` Method (D3Transform)

Copy constructor

```csharp
public static D3Transform Create( D3Transform transform );
```

**Parameters**

- **transform** — 

#### `Create` Method (Double[])

Construct a transform from an array of 12 values (in column order)

```csharp
public static D3Transform Create( double[] array12 );
```

**Parameters**

- **array12** —

#### `Determinant` Method

Return the determinant of the rotation matrix

```csharp
public abstract double Determinant();
```

#### `Equals` Method (D3Transform)

Test for equality

```csharp
public abstract bool Equals( D3Transform d2 );
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

#### `GetInverse` Method

calculate inverse transformation - returns "true" and sets result if successful; returns false and result remains unaltered in the case of a singular transformation

```csharp
public abstract bool GetInverse( D3Transform result );
```

**Parameters**

- **result** —

#### `GetRot` Method

Return the rotation matrix

```csharp
public abstract D3Matrix GetRot();
```

#### `GetShift` Method

Return the shift vector

```csharp
public abstract D3Vector GetShift();
```

#### `Inverse` Method

Invert the transform

```csharp
public abstract D3Transform Inverse();
```

#### `Invert` Method

invert transformation - returns "true" if successful; returns false and remains unaltered in the case of a singular transformation

```csharp
public abstract bool Invert();
```

#### `IsIdentity` Method

Return true if this is an identity transform

```csharp
public abstract bool IsIdentity();
```

#### `IsOrthogonal` Method

Return true if the rotation matrix is orthogonal

```csharp
public abstract bool IsOrthogonal( double tol );
```

**Parameters**

- **tol** —

#### `IsSingular` Method

Returns true if determinant is zero

```csharp
public abstract bool IsSingular();
```

#### `Map` Method (D3Point, D3Point, D3Vector, D3Vector)

Sets the transformation to represent a simple rotation and shift (i.e. no scaling, shearing or reflection) such that: - point posFrom is mapped onto posTo, and - vector vecFrom is mapped onto vecTo.

```csharp
public abstract bool Map( D3Point posFrom , D3Point posTo , D3Vector vecFrom , D3Vector vecTo );
```

**Parameters**

- **posFrom** — 
- **posTo** — 
- **vecFrom** — 
- **vecTo** — 

#### `Map` Method (D3Point, D3Point, D3Vector, D3Vector, D3Vector, D3Vector)

Sets the transformation to represent a simple rotation and shift (i.e. no scaling, shearing or reflection) such that: - point posFrom is mapped onto posTo, - vector vec1From is mapped onto vec1To, and - vector vec2From is mapped as closely as is possible onto vec2To.

```csharp
public abstract bool Map( D3Point posFrom , D3Point posTo , D3Vector vec1From , D3Vector vec1To , D3Vector vec2From , D3Vector vec2To );
```

**Parameters**

- **posFrom** — 
- **posTo** — 
- **vec1From** — 
- **vec1To** — 
- **vec2From** — 
- **vec2To** —

#### `MapOriXTo` Method

Sets the transformation to represent a simple rotation and shift (i.e. no scaling, shearing or reflection) such that: - the origin is mapped onto pos, and - the x-axis is mapped onto vec.

```csharp
public abstract bool MapOriXTo( D3Point pos , D3Vector vec );
```

**Parameters**

- **pos** — 
- **vec** —

#### `MapOriXYTo` Method

Sets the transformation to represent a simple rotation and shift (i.e. no scaling, shearing or reflection) such that: - the origin is mapped onto pos, - the x-axis is mapped onto vec1, and - the y-axis is mapped as closely as is possible onto vec2

```csharp
public abstract bool MapOriXYTo( D3Point pos , D3Vector vec1 , D3Vector vec2 );
```

**Parameters**

- **pos** — 
- **vec1** — 
- **vec2** —

#### `MoveBy` Method (D3Vector)

Apply relative shift by given vector

```csharp
public abstract void MoveBy( D3Vector v );
```

**Parameters**

- **v** — 

#### `MoveBy` Method (Double, Double, Double)

Apply relative shift by given x,y,z values

```csharp
public abstract void MoveBy( double x , double y , double z );
```

**Parameters**

- **x** — 
- **y** — 
- **z** —

#### `Multiply` Method (D3Limits)

Transform given limits box

```csharp
public abstract D3Limits Multiply( D3Limits lim1 );
```

**Parameters**

- **lim1** — 

#### `Multiply` Method (D3Point)

Transform given point

```csharp
public abstract D3Point Multiply( D3Point p2 );
```

**Parameters**

- **p2** — 

#### `Multiply` Method (D3Transform)

Multiply two transformations

```csharp
public abstract D3Transform Multiply( D3Transform m2 );
```

**Parameters**

- **m2** — 

#### `Multiply` Method (D3Vector)

Transform given vector

```csharp
public abstract D3Vector Multiply( D3Vector v2 );
```

**Parameters**

- **v2** —

#### `RotateBy` Method

Rotate about X,Y,Z

```csharp
public abstract void RotateBy( double degX , double degY , double degZ );
```

**Parameters**

- **degX** — 
- **degY** — 
- **degZ** —

#### `RotateX` Method

apply rotation in X by pre-multiplication

```csharp
public abstract void RotateX( double degrees );
```

**Parameters**

- **degrees** —

#### `RotateY` Method

apply rotation in Y by pre-multiplication

```csharp
public abstract void RotateY( double degrees );
```

**Parameters**

- **degrees** —

#### `RotateZ` Method

apply rotation in Z by pre-multiplication

```csharp
public abstract void RotateZ( double degrees );
```

**Parameters**

- **degrees** —

#### `SetRotation` Method

Set rotation matrix

```csharp
public abstract void SetRotation( D3Matrix m );
```

**Parameters**

- **m** —

#### `SetShift` Method

Set shift vector

```csharp
public abstract void SetShift( D3Vector v );
```

**Parameters**

- **v** —

#### `SetValue` Method

Set matrix and shift from array of 12 values

```csharp
public abstract void SetValue( double[] v );
```

**Parameters**

- **v** —

#### `TakeToZAxis` Method

Make the transformation take the given vector to the z axis

```csharp
public abstract void TakeToZAxis( D3Vector v );
```

**Parameters**

- **v** —

#### `ToString` Method

Return a string containing details of the transform

```csharp
public abstract string ToString();
```

#### `Transform` Method

Apply transformation to a plane. Works for any non-singular transformation, including a non-orthogonal transformation (i.e. with scaling/shearing/reflection).

```csharp
public abstract bool Transform( D3Plane plane );
```

**Parameters**

- **plane** —

## Operators

#### `Equality` Operator

invoked by left==right

```csharp
public static bool operator ==( D3Transform left , D3Transform right );
```

**Parameters**

- **left** — 
- **right** —

#### `Inequality` Operator

invoked by left != right

```csharp
public static bool operator !=( D3Transform left , D3Transform right );
```

**Parameters**

- **left** — 
- **right** —

#### `Multiplication` Operator

invoked by t1*t2

```csharp
public static D3Transform operator *( D3Transform t1 , D3Transform t2 );
```

**Parameters**

- **t1** — 
- **t2** —
