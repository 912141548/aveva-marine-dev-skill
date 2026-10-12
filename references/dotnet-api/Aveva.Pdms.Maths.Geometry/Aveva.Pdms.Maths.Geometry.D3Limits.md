---
title: Aveva.Pdms.Maths.Geometry.D3Limits Class
namespace: Aveva.Pdms.Maths.Geometry
assembly: Aveva.Pdms.Maths.Geometry
kind: Class
source: Aveva.Pdms.Maths.Geometry
---

# Aveva.Pdms.Maths.Geometry.D3Limits Class

> 3-D limits This object can be in one of 2 states: - unset: origin at ( DBL_MAX, DBL_MAX, DBL_MAX) extent at (-DBL_MAX, -DBL_MAX, -DBL_MAX) - set: xMin <= xMax, yMin <= yMax, zMin <= zMax

## Syntax

```csharp
public abstract class D3Limits
```

## Inheritance

`System.Object` → `Aveva.Pdms.Maths.Geometry.D3Limits`

## Thread Safety

Public static ( Shared in Visual Basic) members of this type are
safe for multithreaded operations. Instance members are not guaranteed to be
thread-safe.

## Requirements

Namespace:
Aveva.Pdms.Maths.Geometry
Assembly: Aveva.Pdms.Maths.Geometry (in Aveva.Pdms.Maths.Geometry.dll)

## Properties

#### `MaxX` Property

Return minimum Y value of the limits

```csharp
public abstract double MaxX {get;}
```

#### `MaxY` Property

Return maximum X value of limits

```csharp
public abstract double MaxY {get;}
```

#### `MaxZ` Property

Return maximum Z value of limits

```csharp
public abstract double MaxZ {get;}
```

#### `MinX` Property

Property to return the minimum X value of the limits box

```csharp
public abstract double MinX {get;}
```

#### `MinY` Property

Return minimum Z value of the limits

```csharp
public abstract double MinY {get;}
```

#### `MinZ` Property

Return maximum Y value of limits

```csharp
public abstract double MinZ {get;}
```

## Methods

#### `Add` Method

Add two limits bboxes

```csharp
public abstract D3Limits Add( D3Limits lim2 );
```

**Parameters**

- **lim2** —

#### `Clear` Method

Set box to unset

```csharp
public abstract void Clear();
```

#### `Clone` Method

deep copy

```csharp
public abstract D3Limits Clone();
```

#### `ContainsPoint` Method

Returns true if given point is within limits

```csharp
public abstract bool ContainsPoint( D3Point p );
```

**Parameters**

- **p** —

#### `ContainsPointToTol` Method

Returns true if point is within the limits box expanded by tolerance tol

```csharp
public abstract bool ContainsPointToTol( D3Point p , double tol );
```

**Parameters**

- **p** — 
- **tol** —

#### `Create` Method ()

Null constructor

```csharp
public static D3Limits Create();
```

#### `Create` Method (D3Limits)

Copy constructor

```csharp
public static D3Limits Create( D3Limits lim );
```

**Parameters**

- **lim** — 

#### `Create` Method (D3Point)

Construct from origin and given point

```csharp
public static D3Limits Create( D3Point p );
```

**Parameters**

- **p** — 

#### `Create` Method (D3Point, D3Point)

Construct from origin and opposite corner

```csharp
public static D3Limits Create( D3Point p1 , D3Point p2 );
```

**Parameters**

- **p1** — 
- **p2** — 

#### `Create` Method (D3Point, D3Point, D3Point)

Construct limits box which contains the 3 specified points

```csharp
public static D3Limits Create( D3Point p1 , D3Point p2 , D3Point p3 );
```

**Parameters**

- **p1** — 
- **p2** — 
- **p3** — 

#### `Create` Method (D3Point, D3Vector)

construct from given origin with given size

```csharp
public static D3Limits Create( D3Point p , D3Vector extent );
```

**Parameters**

- **p** — 
- **extent** —

#### `Equals` Method (D3Limits)

Test for equality

```csharp
public abstract bool Equals( D3Limits d2 );
```

**Parameters**

- **d2** — 

#### `Equals` Method (Object)

test objects for equality

```csharp
public override bool Equals( object obj );
```

**Parameters**

- **obj** —

#### `ExcludesLine` Method

Returns true if limits does not enclose the two given points

```csharp
public abstract bool ExcludesLine( D3Point p , D3Point q );
```

**Parameters**

- **p** — 
- **q** —

#### `ExcludesTriangle` Method

Returns true if limits box does not include the given three points

```csharp
public abstract bool ExcludesTriangle( D3Point p , D3Point q , D3Point limits );
```

**Parameters**

- **p** — 
- **q** — 
- **limits** —

#### `ExpandBy` Method (D3Vector)

Move min and max corners outwards by vector

```csharp
public abstract void ExpandBy( D3Vector dext );
```

**Parameters**

- **dext** — 

#### `ExpandBy` Method (Double)

Move min and max corners outwards by delta

```csharp
public abstract void ExpandBy( double delta );
```

**Parameters**

- **delta** —

#### `ExpandToInclude` Method (D3Limits)

Expand the box to include specified box

```csharp
public abstract void ExpandToInclude( D3Limits limits );
```

**Parameters**

- **limits** — 

#### `ExpandToInclude` Method (D3Point)

Expand the box to include specified point

```csharp
public abstract void ExpandToInclude( D3Point p );
```

**Parameters**

- **p** —

#### `GetCentre` Method

Return point at centre of limits box

```csharp
public abstract D3Point GetCentre();
```

#### `GetExtent` Method

Return the length of the diagonal

```csharp
public abstract D3Vector GetExtent();
```

#### `GetHashCode` Method

return hashcode

```csharp
public override int GetHashCode();
```

#### `GetMaxSize` Method

Return max of X size, Y size, Z size

```csharp
public abstract double GetMaxSize();
```

#### `GetMaxXYZ` Method

Returns the maximum point

```csharp
public abstract D3Point GetMaxXYZ();
```

#### `GetMinSize` Method

Return min of X size, Ysize and Z size

```csharp
public abstract double GetMinSize();
```

#### `GetMinXYZ` Method

Returns the origin (minimum point)

```csharp
public abstract D3Point GetMinXYZ();
```

#### `GetVertex` Method

Return the corner at index i,j,k

```csharp
public abstract D3Point GetVertex( int i , int j , int k );
```

**Parameters**

- **i** — 
- **j** — 
- **k** —

#### `GetXSize` Method

Return limits size in X direction

```csharp
public abstract double GetXSize();
```

#### `GetXYLimits` Method

Return a D2 Limits from X, Y of D3Limits

```csharp
public abstract D2Limits GetXYLimits();
```

#### `GetYSize` Method

Returns limits size in Y direction

```csharp
public abstract double GetYSize();
```

#### `GetZSize` Method

Returns limits size in Z direction

```csharp
public abstract double GetZSize();
```

#### `InsetBy` Method (D3Vector)

Move min and max corners inwards by extent

```csharp
public abstract void InsetBy( D3Vector extent );
```

**Parameters**

- **extent** — 

#### `InsetBy` Method (Double)

Move min and max corners inwards by delta

```csharp
public abstract void InsetBy( double delta );
```

**Parameters**

- **delta** —

#### `Intersect` Method

Returns limits box which is Boolean intersection of two boxes

```csharp
public abstract D3Limits Intersect( D3Limits limits );
```

**Parameters**

- **limits** —

#### `Intersects` Method

Returns true if the boxes overlap

```csharp
public abstract bool Intersects( D3Limits limits );
```

**Parameters**

- **limits** —

#### `IsUnset` Method

Returns true if limits unset

```csharp
public abstract bool IsUnset();
```

#### `Merge` Method

Returns limits box which contains both boxes

```csharp
public abstract D3Limits Merge( D3Limits limits );
```

**Parameters**

- **limits** —

#### `MirrorX` Method ()

Mirror in X about origin

```csharp
public abstract void MirrorX();
```

#### `MirrorX` Method (D3Point)

Mirror in X about pivot

```csharp
public abstract void MirrorX( D3Point pivot );
```

**Parameters**

- **pivot** —

#### `MirrorY` Method ()

Mirror in Y about origin

```csharp
public abstract void MirrorY();
```

#### `MirrorY` Method (D3Point)

Mirror in Y about pivot

```csharp
public abstract void MirrorY( D3Point pivot );
```

**Parameters**

- **pivot** —

#### `MirrorZ` Method ()

Mirror in Z about origin

```csharp
public abstract void MirrorZ();
```

#### `MirrorZ` Method (D3Point)

Mirror in Z about pivot

```csharp
public abstract void MirrorZ( D3Point pivot );
```

**Parameters**

- **pivot** —

#### `MoveBy` Method

Move by given vector

```csharp
public abstract void MoveBy( D3Vector v );
```

**Parameters**

- **v** —

#### `Multiply` Method

Multipl limits by a scalar value

```csharp
public abstract D3Limits Multiply( double scalar );
```

**Parameters**

- **scalar** —

#### `Obscures` Method

Returns true if this limits box encloses the given box

```csharp
public abstract bool Obscures( D3Limits limits );
```

**Parameters**

- **limits** —

#### `ScaleBy` Method (Double)

Scale uniformly by s

```csharp
public abstract void ScaleBy( double s );
```

**Parameters**

- **s** — 

#### `ScaleBy` Method (Double, D3Point)

Scale by s about pivot

```csharp
public abstract void ScaleBy( double s , D3Point pivot );
```

**Parameters**

- **s** — 
- **pivot** —

#### `SetCornerExtent` Method

Set corner and size

```csharp
public abstract void SetCornerExtent( D3Point p , D3Vector ext );
```

**Parameters**

- **p** — 
- **ext** —

#### `SetCorners` Method

Set origin to p1 and opposite corner to p2

```csharp
public abstract void SetCorners( D3Point p1 , D3Point p2 );
```

**Parameters**

- **p1** — 
- **p2** —

#### `SphericalAdjust` Method

```csharp
public abstract void SphericalAdjust();
```

#### `ToString` Method

Returns a string describing the contents of the limits

```csharp
public abstract string ToString();
```

#### `Volume` Method

Return volume within box

```csharp
public abstract double Volume();
```

## Operators

#### `Addition` Operator

invoked by lim1 + lim2

```csharp
public static D3Limits operator +( D3Limits lim1 , D3Limits lim2 );
```

**Parameters**

- **lim1** — 
- **lim2** —

#### `Equality` Operator

invoked by left == right

```csharp
public static bool operator ==( D3Limits left , D3Limits right );
```

**Parameters**

- **left** — 
- **right** —

#### `Inequality` Operator

invoked by left != right

```csharp
public static bool operator !=( D3Limits left , D3Limits right );
```

**Parameters**

- **left** — 
- **right** —

#### `Multiplication` Operator

invoked by lim1 * scalar

```csharp
public static D3Limits operator *( D3Limits lim1 , double scalar );
```

**Parameters**

- **lim1** — 
- **scalar** —
