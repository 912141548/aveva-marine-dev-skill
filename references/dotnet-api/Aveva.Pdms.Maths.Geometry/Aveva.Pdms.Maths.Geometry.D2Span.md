---
title: Aveva.Pdms.Maths.Geometry.D2Span Class
namespace: Aveva.Pdms.Maths.Geometry
assembly: Aveva.Pdms.Maths.Geometry
kind: Class
source: Aveva.Pdms.Maths.Geometry
---

# Aveva.Pdms.Maths.Geometry.D2Span Class

> Span class - consists of a line or arc, and is used by D2Profile

## Syntax

```csharp
public abstract class D2Span
```

## Inheritance

`System.Object` → `Aveva.Pdms.Maths.Geometry.D2Span`

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

Creates a deep copy of the D2Span

```csharp
public abstract D2Span Clone();
```

#### `Complement` Method

Convert the span into the complementary arc

```csharp
public abstract void Complement();
```

#### `Create` Method ()

default span

```csharp
public static D2Span Create();
```

#### `Create` Method (D2Point, D2Point, D2Point)

Create from 3 points

```csharp
public static D2Span Create( D2Point a , D2Point b , D2Point c );
```

**Parameters**

- **a** — 
- **b** — 
- **c** — 

#### `Create` Method (D2Point, Double, D2Point)

Create from start and end points, and a bulge factor

```csharp
public static D2Span Create( D2Point p , double b , D2Point q );
```

**Parameters**

- **p** — 
- **b** — 
- **q** — 

#### `Create` Method (D2Span)

copy constructor

```csharp
public static D2Span Create( D2Span a );
```

**Parameters**

- **a** —

#### `Equals` Method (D2Span)

test for equality

```csharp
public abstract bool Equals( D2Span d2 );
```

**Parameters**

- **d2** — 

#### `Equals` Method (Object)

```csharp
public override bool Equals( object obj );
```

**Parameters**

- **obj** —

#### `EvaluateDeriv` Method

Return the tangent on span which is at point proportion uarg from start

```csharp
public abstract D2Vector EvaluateDeriv( double uarg );
```

**Parameters**

- **uarg** — Value between 0 1nd 1

#### `EvaluatePoint` Method

Return a point on span which is proportion uarg from start

```csharp
public abstract D2Point EvaluatePoint( double uarg );
```

**Parameters**

- **uarg** — Value between 0 and 1

#### `FacetToTol` Method

approximate polygon

```csharp
public abstract D2PolyLine FacetToTol( double tol );
```

**Parameters**

- **tol** —

#### `GetAlpha0` Method

Return the angular position of the start of the span

```csharp
public abstract double GetAlpha0();
```

#### `GetAlpha1` Method

Return the angular position of the end of the span

```csharp
public abstract double GetAlpha1();
```

#### `GetApproxPolyLine` Method

Convert arc to polylines

```csharp
public abstract D2PolyLine GetApproxPolyLine( double tol );
```

**Parameters**

- **tol** —

#### `GetApproxPolyLineInSteps` Method

Convert arc to polylines

```csharp
public abstract D2PolyLine GetApproxPolyLineInSteps( int nSteps );
```

**Parameters**

- **nSteps** —

#### `GetAreaUnder` Method

Return the area under the span

```csharp
public abstract double GetAreaUnder();
```

#### `GetBulge` Method

Return the bulge factor

```csharp
public abstract double GetBulge();
```

#### `GetCentre` Method

Return the centre point of the span

```csharp
public abstract D2Point GetCentre();
```

#### `GetEndNearest` Method

Return the end of the span which is nearest to the given point

```csharp
public abstract D2Point GetEndNearest( D2Point p );
```

**Parameters**

- **p** — Reference point

#### `GetFirst` Method

Return the first point on the span

```csharp
public abstract D2Point GetFirst();
```

#### `GetFirstX` Method

Return the X coordinate of the start point of the span

```csharp
public abstract double GetFirstX();
```

#### `GetFirstY` Method

Return the Y coordinate of the start point of the span

```csharp
public abstract double GetFirstY();
```

#### `GetHashCode` Method

```csharp
public override int GetHashCode();
```

#### `GetLast` Method

Return the last point of the span

```csharp
public abstract D2Point GetLast();
```

#### `GetLastX` Method

Return the X coordinate of the last point of the span

```csharp
public abstract double GetLastX();
```

#### `GetLastY` Method

Return the Y coordinate of the last point of the span

```csharp
public abstract double GetLastY();
```

#### `GetLength` Method

Return the length of the span

```csharp
public abstract double GetLength();
```

#### `GetMidPoint` Method

Return the mid point of the span

```csharp
public abstract D2Point GetMidPoint();
```

#### `GetRadius` Method

Return the radius of the span

```csharp
public abstract double GetRadius();
```

#### `IsNull` Method

Return true if span is empty

```csharp
public abstract bool IsNull();
```

#### `IsStraight` Method

returns true if the bulge ratio has a magnitude less than 0.0000306 ; i.e. the angle is less than 0.0001224 radians (0.007013 degrees)

```csharp
public abstract bool IsStraight();
```

#### `LeadsSmoothlyTo` Method

returns true if the directions at the end of the local span and at the start of the span named "next" are within 0.001414 radians (0.08103 degrees) of each other

```csharp
public abstract bool LeadsSmoothlyTo( D2Span next );
```

**Parameters**

- **next** —

#### `MinMaxBox` Method

Return containment box

```csharp
public abstract D2Limits MinMaxBox();
```

#### `MoveBy` Method

Move span by given vector

```csharp
public abstract void MoveBy( D2Vector v );
```

**Parameters**

- **v** —

#### `Offset` Method

Incremental move of span

```csharp
public abstract void Offset( double dist );
```

**Parameters**

- **dist** —

#### `Reverse` Method

Reverse direction of span

```csharp
public abstract void Reverse();
```

#### `RotateBy` Method (Double)

Rotate span by given angle about the origin

```csharp
public abstract void RotateBy( double angle );
```

**Parameters**

- **angle** — 

#### `RotateBy` Method (Double, D2Point)

Rotate the span by given angle about pivot

```csharp
public abstract void RotateBy( double angle , D2Point pivot );
```

**Parameters**

- **angle** — 
- **pivot** —

#### `SetBulge` Method

Set the bulge factor of the span

```csharp
public abstract void SetBulge( double b );
```

**Parameters**

- **b** —

#### `SetFirst` Method

Set the position of the start of the arc

```csharp
public abstract void SetFirst( D2Point p );
```

**Parameters**

- **p** —

#### `SetLast` Method

Set the position of the end of the arc

```csharp
public abstract void SetLast( D2Point p );
```

**Parameters**

- **p** —

#### `SetValue` Method

Set start, end positions and bulge factor

```csharp
public abstract void SetValue( D2Point s , double b , D2Point e );
```

**Parameters**

- **s** — 
- **b** — 
- **e** —

#### `ToString` Method

Returns a string describing the contents of the D2Span

```csharp
public abstract string ToString();
```

## Operators

#### `Equality` Operator

invoked by left == right

```csharp
public static bool operator ==( D2Span left , D2Span right );
```

**Parameters**

- **left** — 
- **right** —

#### `Inequality` Operator

invoked by left != right

```csharp
public static bool operator !=( D2Span left , D2Span right );
```

**Parameters**

- **left** — 
- **right** —
