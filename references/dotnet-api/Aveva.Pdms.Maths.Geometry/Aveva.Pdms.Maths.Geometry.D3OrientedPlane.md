---
title: Aveva.Pdms.Maths.Geometry.D3OrientedPlane Class
namespace: Aveva.Pdms.Maths.Geometry
assembly: Aveva.Pdms.Maths.Geometry
kind: Class
source: Aveva.Pdms.Maths.Geometry
---

# Aveva.Pdms.Maths.Geometry.D3OrientedPlane Class

> Class definition for an oriented plane This class is intended for use as a local coordinate system so that plane coordinate geometry can be performed. Conceptually it has a one-to-one correspondence with PDMS's orientated plane. Apart from its direct use for the 2-d geometry constructor, it is intended that arcs, planar curves and lines in 3-d are reduced to 2-d via mth2<obj>(const mth3<obj>, const D3OrientedPlane); To create the plane you need to supply an origin (D3Point) and two axes u,v - both D3Vector. The plane normal is then defined by u x v. This class always creates a plane with right-handed orthonormal axes. An internal flag is set if the data is invalid (e.g. the input vectors are null or colinear) and an attempt to use an invalid class will result in an assertion failure. Applications should use the 'inValid()' method to preemptively trap this condition. A cast to a D3Plane exists so that geometric operations on a D3Plane will also work on an D3OrientedPlane; you can also cast to a D3Transform.

## Syntax

```csharp
public abstract class D3OrientedPlane
```

## Inheritance

`System.Object` → `Aveva.Pdms.Maths.Geometry.D3OrientedPlane`

## Thread Safety

Public static ( Shared in Visual Basic) members of this type are
safe for multithreaded operations. Instance members are not guaranteed to be
thread-safe.

## Requirements

Namespace:
Aveva.Pdms.Maths.Geometry
Assembly: Aveva.Pdms.Maths.Geometry (in Aveva.Pdms.Maths.Geometry.dll)

## Methods

#### `AsPlane` Method

Cast a D3OrientedPlane to a D3Plane

```csharp
public abstract D3Plane AsPlane();
```

#### `AsTransform` Method

Cast a D3OrientedPlane to a D3Transform

```csharp
public abstract D3Transform AsTransform();
```

#### `Clone` Method

Returns a deep copy of the D3OrientedPlane

```csharp
public abstract D3OrientedPlane Clone();
```

#### `Create` Method ()

By default construct a natural right-handed plane

```csharp
public static D3OrientedPlane Create();
```

#### `Create` Method (D3OrientedPlane)

Copy a OrientedPlane

```csharp
public static D3OrientedPlane Create( D3OrientedPlane p );
```

**Parameters**

- **p** — 

#### `Create` Method (D3Plane)

Construct from a plane

```csharp
public static D3OrientedPlane Create( D3Plane plane );
```

**Parameters**

- **plane** — 

#### `Create` Method (D3Point, D3Vector, D3Vector)

Construct plane from origin, u axis and v axis

```csharp
public static D3OrientedPlane Create( D3Point origin , D3Vector u , D3Vector v );
```

**Parameters**

- **origin** — 
- **u** — 
- **v** — 

#### `Create` Method (D3Point, Double, Double, Double)

Construct a D3OrientedPlane from a point and three Euler angles

```csharp
public static D3OrientedPlane Create( D3Point origin , double e1 , double e2 , double e3 );
```

**Parameters**

- **origin** — 
- **e1** — 
- **e2** — 
- **e3** —

#### `Equals` Method (D3OrientedPlane)

test for equality

```csharp
public abstract bool Equals( D3OrientedPlane p );
```

**Parameters**

- **p** — 

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

#### `GetNormal` Method

Get the plane normal

```csharp
public abstract D3Vector GetNormal();
```

#### `GetOrigin` Method

Return the plane's origin

```csharp
public abstract D3Point GetOrigin();
```

#### `GetUAxis` Method

Return the U axis

```csharp
public abstract D3Vector GetUAxis();
```

#### `GetVAxis` Method

Return the V axis

```csharp
public abstract D3Vector GetVAxis();
```

#### `InValid` Method

Returns true if the class data if invalid

```csharp
public abstract bool InValid();
```

#### `MapFromPlane` Method

maps point in plane space to user co-ordinates

```csharp
public abstract D3Point MapFromPlane( D3Point pt );
```

**Parameters**

- **pt** —

#### `MapToPlane` Method

maps point in user space to plane co-ordinates

```csharp
public abstract D3Point MapToPlane( D3Point pt );
```

**Parameters**

- **pt** —

#### `OnPlane` Method

Returns true if the given point lies on the plane

```csharp
public abstract bool OnPlane( D3Point pt );
```

**Parameters**

- **pt** —

#### `ProjectOnto` Method

Project a point onto the plane and return the world coord

```csharp
public abstract D3Point ProjectOnto( D3Point p );
```

**Parameters**

- **p** —

#### `SetOrigin` Method

Set the origin (equivalent to moveTo)

```csharp
public abstract void SetOrigin( D3Point ori );
```

**Parameters**

- **ori** —

#### `SetValues` Method

Set the Euler angles (equivalent to rotate to)

```csharp
public abstract void SetValues( double e1 , double e2 , double e3 );
```

**Parameters**

- **e1** — 
- **e2** — 
- **e3** —

#### `ToLocal` Method

Returns the D3point projected onto the 2-d plane

```csharp
public abstract D2Point ToLocal( D3Point p );
```

**Parameters**

- **p** —

#### `ToString` Method

Returns a string describing the values of the D3OrientedPlane

```csharp
public abstract string ToString();
```

#### `ToWorld` Method

Returns the D2_point in 3-d world

```csharp
public abstract D3Point ToWorld( D2Point p );
```

**Parameters**

- **p** —

## Operators

#### `Equality` Operator

invoked by left == right

```csharp
public static bool operator ==( D3OrientedPlane left , D3OrientedPlane right );
```

**Parameters**

- **left** — 
- **right** —

#### `Inequality` Operator

invoked by left != right

```csharp
public static bool operator !=( D3OrientedPlane left , D3OrientedPlane right );
```

**Parameters**

- **left** — 
- **right** —
