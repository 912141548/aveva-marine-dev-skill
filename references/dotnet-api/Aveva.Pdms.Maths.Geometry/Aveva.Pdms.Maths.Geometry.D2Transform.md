---
title: Aveva.Pdms.Maths.Geometry.D2Transform Class
namespace: Aveva.Pdms.Maths.Geometry
assembly: Aveva.Pdms.Maths.Geometry
kind: Class
source: Aveva.Pdms.Maths.Geometry
---

# Aveva.Pdms.Maths.Geometry.D2Transform Class

> D2Transform - solid body transformations

## Syntax

```csharp
public abstract class D2Transform
```

## Inheritance

`System.Object` → `Aveva.Pdms.Maths.Geometry.D2Transform`

## Thread Safety

Public static ( Shared in Visual Basic) members of this type are
safe for multithreaded operations. Instance members are not guaranteed to be
thread-safe.

## Requirements

Namespace:
Aveva.Pdms.Maths.Geometry
Assembly: Aveva.Pdms.Maths.Geometry (in Aveva.Pdms.Maths.Geometry.dll)

## Methods

#### `AsArray6` Method

return transformation as an array of number

```csharp
public abstract double[] AsArray6();
```

#### `BeIdentity` Method

set transform to be a null rotation and null shift

```csharp
public abstract void BeIdentity();
```

#### `Clone` Method

deep copy

```csharp
public abstract D2Transform Clone();
```

#### `Create` Method ()

Default

```csharp
public static D2Transform Create();
```

#### `Create` Method (D2Matrix, D2Vector)

Construct a transform from rotation matrix and shift vector

```csharp
public static D2Transform Create( D2Matrix theRot , D2Vector theShift );
```

**Parameters**

- **theRot** — 
- **theShift** — 

#### `Create` Method (D2Transform)

Copy constructor

```csharp
public static D2Transform Create( D2Transform transform );
```

**Parameters**

- **transform** — 

#### `Create` Method (Double[])

Construct a transfrom from given 6 values (by row)

```csharp
public static D2Transform Create( double[] v );
```

**Parameters**

- **v** —

#### `Determinant` Method

return determinant of rotation matrix

```csharp
public abstract double Determinant();
```

#### `Equals` Method (D2Transform)

Test for equality

```csharp
public abstract bool Equals( D2Transform d2 );
```

**Parameters**

- **d2** — 

#### `Equals` Method (Object)

equals method

```csharp
public override bool Equals( object o );
```

**Parameters**

- **o** —

#### `GetHashCode` Method

gethashcode

```csharp
public override int GetHashCode();
```

#### `GetInverse` Method

finds inverse transformation - returns "true" and sets result if successful; returns false and result remains unaltered for a singular rotation matrix

```csharp
public abstract bool GetInverse( D2Transform result );
```

**Parameters**

- **result** —

#### `GetRot` Method

return rotation matrix

```csharp
public abstract D2Matrix GetRot();
```

#### `GetShift` Method

return shift part of transformation

```csharp
public abstract D2Vector GetShift();
```

#### `Inverse` Method

Return inverse transformation - returns null transformation if the original transformation is singular

```csharp
public abstract D2Transform Inverse();
```

#### `Invert` Method

invert transformation - returns "true" if successful; returns false and remains unaltered in the case of a singular transformation

```csharp
public abstract bool Invert();
```

#### `IsIdentity` Method

true if rotation is Identity matrix (ie no rotation) AND shift is zero

```csharp
public abstract bool IsIdentity();
```

#### `IsOrthogonal` Method

TRUE if rotation matrix is Orthogonal (within tolerance)

```csharp
public abstract bool IsOrthogonal( double tol );
```

**Parameters**

- **tol** —

#### `IsSingular` Method

result predicts failure of getInverse()/inverse()/invert()

```csharp
public abstract bool IsSingular();
```

#### `Map` Method

Sets the transformation to represent a simple rotation and shift (i.e. no scaling, shearing or reflection) such that: - point posFrom is mapped onto posTo, and - vector vecFrom is mapped onto vecTo.

```csharp
public abstract bool Map( D2Point posFrom , D2Point posTo , D2Vector vecFrom , D2Vector vecTo );
```

**Parameters**

- **posFrom** — 
- **posTo** — 
- **vecFrom** — 
- **vecTo** —

#### `MapOriXTo` Method

Sets the transformation to represent a simple rotation and shift (i.e. no scaling, shearing or reflection) such that: - the origin is mapped onto pos, and - the x-axis is mapped onto vec.

```csharp
public abstract bool MapOriXTo( D2Point pos , D2Vector vec );
```

**Parameters**

- **pos** — 
- **vec** —

#### `MoveBy` Method (D2Vector)

add v vector to shift vector of the transform

```csharp
public abstract void MoveBy( D2Vector v );
```

**Parameters**

- **v** — 

#### `MoveBy` Method (Double, Double)

add (x,y) vector to shift vector of the transform

```csharp
public abstract void MoveBy( double x , double y );
```

**Parameters**

- **x** — 
- **y** —

#### `Multiply` Method (D2Limits)

Multiply two transforms

```csharp
public abstract D2Limits Multiply( D2Limits lim2 );
```

**Parameters**

- **lim2** — 

#### `Multiply` Method (D2Point)

Multiply two transforms

```csharp
public abstract D2Point Multiply( D2Point p2 );
```

**Parameters**

- **p2** — 

#### `Multiply` Method (D2Transform)

Multiply two transforms

```csharp
public abstract D2Transform Multiply( D2Transform t2 );
```

**Parameters**

- **t2** — 

#### `Multiply` Method (D2Vector)

Multiply two transforms

```csharp
public abstract D2Vector Multiply( D2Vector v2 );
```

**Parameters**

- **v2** —

#### `RotateByDegrees` Method

rotate transformation (rotation matrix and shift vector) by given number of degrees

```csharp
public abstract void RotateByDegrees( double degrees );
```

**Parameters**

- **degrees** —

#### `RotateByRadians` Method

rotate transformation (rotation matrix and shift vector) by given number of radians

```csharp
public abstract void RotateByRadians( double radians );
```

**Parameters**

- **radians** —

#### `SetValues` Method

set transform from an array of 6 numbers ( rotation(4) followed by shift(2) )

```csharp
public abstract void SetValues( double[] v );
```

**Parameters**

- **v** —

#### `TakeToXAxis` Method

Make the transform take the given vector to the x axis

```csharp
public abstract void TakeToXAxis( D2Vector v );
```

**Parameters**

- **v** —

#### `TakeToYAxis` Method

Make the transform take the given vector to the y axis

```csharp
public abstract void TakeToYAxis( D2Vector v );
```

**Parameters**

- **v** —

#### `ToString` Method

Returns a string describing the contents of the D2Transform

```csharp
public abstract string ToString();
```

## Operators

#### `Equality` Operator

true if transforms match exactly

```csharp
public static bool operator ==( D2Transform left , D2Transform right );
```

**Parameters**

- **left** — 
- **right** —

#### `Inequality` Operator

true if transforms do not match exactly

```csharp
public static bool operator !=( D2Transform left , D2Transform right );
```

**Parameters**

- **left** — 
- **right** —

#### `Multiplication` Operator

resultant transform is equivalent to apply both tranformations.

```csharp
public static D2Transform operator *( D2Transform t1 , D2Transform t );
```

**Parameters**

- **t1** — 
- **t** —
