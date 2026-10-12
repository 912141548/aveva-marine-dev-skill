---
title: Aveva.Pdms.Maths.Geometry.D3Plane Class
namespace: Aveva.Pdms.Maths.Geometry
assembly: Aveva.Pdms.Maths.Geometry
kind: Class
source: Aveva.Pdms.Maths.Geometry
---

# Aveva.Pdms.Maths.Geometry.D3Plane Class

> A 3-D Plane Class (with double values) With normal n and dist d, point x is: on the plane if: n.x + d = 0 above the plane if: n.x + d > 0 Alternative format is (a,b,c;d) - point (x,y,z) is above the plane if: ax + by + cz + d > 0 normal always has magnitude 1.

## Syntax

```csharp
public abstract class D3Plane
```

## Inheritance

`System.Object` → `Aveva.Pdms.Maths.Geometry.D3Plane`

## Thread Safety

Public static ( Shared in Visual Basic) members of this type are
safe for multithreaded operations. Instance members are not guaranteed to be
thread-safe.

## Requirements

Namespace:
Aveva.Pdms.Maths.Geometry
Assembly: Aveva.Pdms.Maths.Geometry (in Aveva.Pdms.Maths.Geometry.dll)

## Methods

#### `Clone` Method

deep copy

```csharp
public abstract D3Plane Clone();
```

#### `Create` Method ()

Default constructor

```csharp
public static D3Plane Create();
```

#### `Create` Method (D3Plane)

Copy constructor

```csharp
public static D3Plane Create( D3Plane plane );
```

**Parameters**

- **plane** — 

#### `Create` Method (D3Vector, D3Point)

Construct a plane from a normal vector and a point

```csharp
public static D3Plane Create( D3Vector norm , D3Point pt );
```

**Parameters**

- **norm** — 
- **pt** — 

#### `Create` Method (D3Vector, Double)

Construct a plane from a normal vector and an offset

```csharp
public static D3Plane Create( D3Vector norm , double d );
```

**Parameters**

- **norm** — 
- **d** —

#### `Ddistance` Method

Return the distance of the given point from the plane

```csharp
public abstract double Ddistance( D3Point pt );
```

**Parameters**

- **pt** —

#### `Equals` Method (D3Plane)

test for equality

```csharp
public abstract bool Equals( D3Plane d2 );
```

**Parameters**

- **d2** — 

#### `Equals` Method (Object)

```csharp
public override bool Equals( object obj );
```

**Parameters**

- **obj** —

#### `GetA` Method

Returns the X direction of the normal to the plane

```csharp
public abstract double GetA();
```

#### `GetB` Method

Return the Y direction of the normal to the plane

```csharp
public abstract double GetB();
```

#### `GetC` Method

Return the Z direction of the normal to the plane

```csharp
public abstract double GetC();
```

#### `GetD` Method

Return the offset of the plane from the origin

```csharp
public abstract double GetD();
```

#### `GetHashCode` Method

```csharp
public override int GetHashCode();
```

#### `GetIntersectionWithLine` Method

Return the point at the intersection of the line and the plane. Returns false if they do not intersect

```csharp
public abstract bool GetIntersectionWithLine( D3Point linePt , D3Vector lineDir , D3Point intersectionPoint );
```

**Parameters**

- **linePt** — 
- **lineDir** — 
- **intersectionPoint** —

#### `GetNormal` Method

Return the vector normal to the plane

```csharp
public abstract D3Vector GetNormal();
```

#### `GetOffset` Method

Return the offset of the plane from the origin

```csharp
public abstract double GetOffset();
```

#### `SetValue` Method (D3Vector, D3Point)

Set the normal and a point on the plane

```csharp
public abstract void SetValue( D3Vector norm , D3Point pt );
```

**Parameters**

- **norm** — 
- **pt** — 

#### `SetValue` Method (D3Vector, Double)

Set normal and offset values

```csharp
public abstract void SetValue( D3Vector norm , double d );
```

**Parameters**

- **norm** — 
- **d** —

#### `Side` Method

Return which side of the line the point lies on

```csharp
public abstract int Side( D3Point pt , double tol );
```

**Parameters**

- **pt** — 
- **tol** — 

**Return Value**

1=above, 0=on, -1=below

#### `ToString` Method

Return a string containing details of the plane

```csharp
public abstract string ToString();
```

## Operators

#### `Equality` Operator

invoked by left == right

```csharp
public static bool operator ==( D3Plane left , D3Plane right );
```

**Parameters**

- **left** — 
- **right** —

#### `Inequality` Operator

invoked by left != right

```csharp
public static bool operator !=( D3Plane left , D3Plane right );
```

**Parameters**

- **left** — 
- **right** —
