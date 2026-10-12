---
title: Aveva.Pdms.Maths.Geometry.D2Limits Class
namespace: Aveva.Pdms.Maths.Geometry
assembly: Aveva.Pdms.Maths.Geometry
kind: Class
source: Aveva.Pdms.Maths.Geometry
---

# Aveva.Pdms.Maths.Geometry.D2Limits Class

> 2-D Limits Box

## Syntax

```csharp
public abstract class D2Limits
```

## Inheritance

`System.Object` → `Aveva.Pdms.Maths.Geometry.D2Limits`

## Thread Safety

Public static ( Shared in Visual Basic) members of this type are
safe for multithreaded operations. Instance members are not guaranteed to be
thread-safe.

## Requirements

Namespace:
Aveva.Pdms.Maths.Geometry
Assembly: Aveva.Pdms.Maths.Geometry (in Aveva.Pdms.Maths.Geometry.dll)

## Methods

#### `Area` Method

Return area of box

```csharp
public abstract double Area();
```

#### `Clear` Method

Set box to unset

```csharp
public abstract void Clear();
```

#### `Clone` Method

```csharp
public abstract D2Limits Clone();
```

#### `ContainsPoint` Method

Returns true if given point is within the box

```csharp
public abstract bool ContainsPoint( D2Point p );
```

**Parameters**

- **p** —

#### `ContainsPointToTol` Method

Returns true if given point is within the box, within tolerance

```csharp
public abstract bool ContainsPointToTol( D2Point p , double tol );
```

**Parameters**

- **p** — 
- **tol** —

#### `Create` Method ()

Create zero size limits box

```csharp
public static D2Limits Create();
```

#### `Create` Method (D2Limits)

Copy constructor

```csharp
public static D2Limits Create( D2Limits r );
```

**Parameters**

- **r** — 

#### `Create` Method (D2Point)

Create limits box at given point

```csharp
public static D2Limits Create( D2Point p );
```

**Parameters**

- **p** — 

#### `Create` Method (D2Point, D2Point)

Create cube between given points

```csharp
public static D2Limits Create( D2Point min , D2Point max );
```

**Parameters**

- **min** — 
- **max** — 

#### `Create` Method (D2Point, D2Vector)

Create limits cube from given point with given extent

```csharp
public static D2Limits Create( D2Point p , D2Vector extent );
```

**Parameters**

- **p** — 
- **extent** —

#### `Equals` Method (D2Limits)

Returns true if equal within default tolerance

```csharp
public abstract bool Equals( D2Limits limits );
```

**Parameters**

- **limits** — 

#### `Equals` Method (D2Limits, Double)

Returns true if equal within given tolerance

```csharp
public abstract bool Equals( D2Limits limits , double delta );
```

**Parameters**

- **limits** — 
- **delta** — 

#### `Equals` Method (Object)

override system equals method

```csharp
public override bool Equals( object a );
```

**Parameters**

- **a** —

#### `Exits` Method

Point where line exits the box, and which side of box

```csharp
public abstract D2Point Exits( D2Point start , D2Vector direction , ref int SideOfRect );
```

**Parameters**

- **start** — 
- **direction** — 
- **SideOfRect** — Left for 1, top for 2, right for 3, bottom for 4

#### `ExpandBy` Method (D2Vector)

Expand box by vector

```csharp
public abstract void ExpandBy( D2Vector v );
```

**Parameters**

- **v** — 

#### `ExpandBy` Method (Double)

Expand box by given amount in all directions constant margin - may be neg

```csharp
public abstract void ExpandBy( double delta );
```

**Parameters**

- **delta** —

#### `ExpandToInclude` Method (D2Limits)

Expand to include anothe box

```csharp
public abstract void ExpandToInclude( D2Limits limits );
```

**Parameters**

- **limits** — 

#### `ExpandToInclude` Method (D2Point)

Expand box to include point

```csharp
public abstract void ExpandToInclude( D2Point p );
```

**Parameters**

- **p** —

#### `GetBase` Method

Min value of Y

```csharp
public abstract double GetBase();
```

#### `GetBL` Method

Bottom left corner

```csharp
public abstract D2Point GetBL();
```

#### `GetBR` Method

Bottom right corner

```csharp
public abstract D2Point GetBR();
```

#### `GetCentre` Method

Mid point of box

```csharp
public abstract D2Point GetCentre();
```

#### `GetExtent` Method

Extent of box

```csharp
public abstract D2Vector GetExtent();
```

#### `GetHashCode` Method

override system gethashcode method

```csharp
public override int GetHashCode();
```

#### `GetHeight` Method

size in Y direction

```csharp
public abstract double GetHeight();
```

#### `GetLeft` Method

Min value of X

```csharp
public abstract double GetLeft();
```

#### `GetMaxSize` Method

Max of height and width

```csharp
public abstract double GetMaxSize();
```

#### `GetMaxX` Method

Max value of X

```csharp
public abstract double GetMaxX();
```

#### `GetMaxY` Method

Max value of Y

```csharp
public abstract double GetMaxY();
```

#### `GetMinSize` Method

Min of width and height

```csharp
public abstract double GetMinSize();
```

#### `GetMinX` Method

Min value of X

```csharp
public abstract double GetMinX();
```

#### `GetMinY` Method

Min value of Y

```csharp
public abstract double GetMinY();
```

#### `GetRight` Method

Max value of X

```csharp
public abstract double GetRight();
```

#### `GetTL` Method

Top left corner

```csharp
public abstract D2Point GetTL();
```

#### `GetTop` Method

max value of Y

```csharp
public abstract double GetTop();
```

#### `GetTR` Method

Top right corner

```csharp
public abstract D2Point GetTR();
```

#### `GetWidth` Method

size in X direction

```csharp
public abstract double GetWidth();
```

#### `InsetBy` Method (D2Vector)

Inset box by vector (opposite to expand)

```csharp
public abstract void InsetBy( D2Vector dext );
```

**Parameters**

- **dext** — 

#### `InsetBy` Method (Double)

Inset box by given amount(opposite to expand)

```csharp
public abstract void InsetBy( double delta );
```

**Parameters**

- **delta** —

#### `Intersect` Method

boolean set-op

```csharp
public abstract D2Limits Intersect( D2Limits limits );
```

**Parameters**

- **limits** —

#### `Intersects` Method

True if boxes overlap

```csharp
public abstract bool Intersects( D2Limits limits );
```

**Parameters**

- **limits** —

#### `IsUnset` Method

Test for unset

```csharp
public abstract bool IsUnset();
```

#### `Merge` Method

Returns box which enclose both

```csharp
public abstract D2Limits Merge( D2Limits limits );
```

**Parameters**

- **limits** —

#### `MirrorX` Method ()

Reflect in X about origin

```csharp
public abstract void MirrorX();
```

#### `MirrorX` Method (D2Point)

Reflect in X about pivot

```csharp
public abstract void MirrorX( D2Point pivot );
```

**Parameters**

- **pivot** —

#### `MirrorY` Method ()

Reflect in Y about origin

```csharp
public abstract void MirrorY();
```

#### `MirrorY` Method (D2Point)

Reflect in Y about pivot

```csharp
public abstract void MirrorY( D2Point pivot );
```

**Parameters**

- **pivot** —

#### `MoveBy` Method

Move box by given vector

```csharp
public abstract void MoveBy( D2Vector v );
```

**Parameters**

- **v** —

#### `ScaleBy` Method (Double)

Uniform scaling about centre

```csharp
public abstract void ScaleBy( double s );
```

**Parameters**

- **s** — 

#### `ScaleBy` Method (Double, D2Point)

Scale about pivot point

```csharp
public abstract void ScaleBy( double s , D2Point pivot );
```

**Parameters**

- **s** — 
- **pivot** —

#### `SetCornerExtent` Method

Set corner and direction of box

```csharp
public abstract void SetCornerExtent( D2Point p , D2Vector ext );
```

**Parameters**

- **p** — 
- **ext** —

#### `SetCorners` Method

Set two opposite corners

```csharp
public abstract void SetCorners( D2Point p1 , D2Point p2 );
```

**Parameters**

- **p1** — 
- **p2** —

#### `ToString` Method

Returns a string describing the contents of the D2Line

```csharp
public abstract string ToString();
```

## Operators

#### `Equality` Operator

test for equality

```csharp
public static bool operator ==( D2Limits left , D2Limits right );
```

**Parameters**

- **left** — 
- **right** —

#### `Inequality` Operator

test for inequality

```csharp
public static bool operator !=( D2Limits left , D2Limits right );
```

**Parameters**

- **left** — 
- **right** —
