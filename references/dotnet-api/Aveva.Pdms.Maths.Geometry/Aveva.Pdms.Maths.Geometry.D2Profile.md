---
title: Aveva.Pdms.Maths.Geometry.D2Profile Class
namespace: Aveva.Pdms.Maths.Geometry
assembly: Aveva.Pdms.Maths.Geometry
kind: Class
source: Aveva.Pdms.Maths.Geometry
---

# Aveva.Pdms.Maths.Geometry.D2Profile Class

> 2-D profile This class represents a sequence of spans connected end to end. Each span is either a finite straight line or a circular arc. The number of nodes for a profile is always one more than the number of spans. A closed profile is represented by having the last node equal to the first. The constructors (apart from the copy constructor) generate an 'open-ended' profile consisting of a single node and with no spans. (If the first node is not known when the constructor is invoked, it can be set later by calling setNode() .) The function addSpan() should be called succesively to extend an open-ended profile one span at a time. The function close() may be called to add the final span for what is to be a closed profile.

## Syntax

```csharp
public abstract class D2Profile
```

## Inheritance

`System.Object` → `Aveva.Pdms.Maths.Geometry.D2Profile`

## Thread Safety

Public static ( Shared in Visual Basic) members of this type are
safe for multithreaded operations. Instance members are not guaranteed to be
thread-safe.

## Requirements

Namespace:
Aveva.Pdms.Maths.Geometry
Assembly: Aveva.Pdms.Maths.Geometry (in Aveva.Pdms.Maths.Geometry.dll)

## Methods

#### `AddSpan` Method

Add a span to end to given point with given bulge factor

```csharp
public abstract void AddSpan( double bulge , D2Point node );
```

**Parameters**

- **bulge** — 
- **node** —

#### `Area` Method

Return the area enclosed by the profile

```csharp
public abstract double Area();
```

#### `Clone` Method

Creates a deep copy of the D2Profile

```csharp
public abstract D2Profile Clone();
```

#### `Close` Method ()

Close the span with a straight line (bulge = 0)

```csharp
public abstract void Close();
```

#### `Close` Method (Double)

Close the profile with a span with given bulge

```csharp
public abstract void Close( double bulge );
```

**Parameters**

- **bulge** —

#### `Create` Method ()

Default constructor. constructs an 'open-ended' profile consisting of a single node at (0,0) and with no spans

```csharp
public static D2Profile Create();
```

#### `Create` Method (D2Point)

Create an open-ended profile with a single node and no spans

```csharp
public static D2Profile Create( D2Point node );
```

**Parameters**

- **node** — 

#### `Create` Method (D2Point, Int32)

constructs an 'open-ended' profile consisting of a single node and with no spans; for efficiency, the argument 'nspans' can be used to reserve space internally for the appropriate number of spans (it is not an error if the value is not correct)

```csharp
public static D2Profile Create( D2Point node , int nspans );
```

**Parameters**

- **node** — 
- **nspans** — 

#### `Create` Method (D2Profile)

Copy a profile

```csharp
public static D2Profile Create( D2Profile pro );
```

**Parameters**

- **pro** — 

#### `Create` Method (Int32)

Construct a profile with space for nspans spans

```csharp
public static D2Profile Create( int nspans );
```

**Parameters**

- **nspans** —

#### `Equals` Method (D2Profile)

test for equality

```csharp
public abstract bool Equals( D2Profile d2 );
```

**Parameters**

- **d2** — 

#### `Equals` Method (Object)

```csharp
public override bool Equals( object obj );
```

**Parameters**

- **obj** —

#### `GetAllSpans` Method

Return a vector containing all the spans

```csharp
public abstract D2Span[] GetAllSpans();
```

#### `GetApproxPolyLine` Method

Return a polyline which approximates the profile

```csharp
public abstract D2PolyLine GetApproxPolyLine( double tol );
```

**Parameters**

- **tol** —

#### `GetBulge` Method

Return the ith bulge factor

```csharp
public abstract double GetBulge( int i );
```

**Parameters**

- **i** —

#### `GetFirstNode` Method

Return the first node

```csharp
public abstract D2Point GetFirstNode();
```

#### `GetHashCode` Method

```csharp
public override int GetHashCode();
```

#### `GetLastNode` Method

Return the last node

```csharp
public abstract D2Point GetLastNode();
```

#### `GetNode` Method

Return the i'th node

```csharp
public abstract D2Point GetNode( int i );
```

**Parameters**

- **i** —

#### `GetSpan` Method

Return the i'th span

```csharp
public abstract D2Span GetSpan( int i );
```

**Parameters**

- **i** —

#### `MinMaxBox` Method

Return limits box of profile

```csharp
public abstract D2Limits MinMaxBox();
```

#### `MirrorX` Method ()

Reflect profile in X about origin

```csharp
public abstract void MirrorX();
```

#### `MirrorX` Method (D2Point)

Reflect profile in X about pivot

```csharp
public abstract void MirrorX( D2Point pivot );
```

**Parameters**

- **pivot** —

#### `MirrorY` Method ()

Reflect profile in Y about origin

```csharp
public abstract void MirrorY();
```

#### `MirrorY` Method (D2Point)

Reflect profile in Y about pivot

```csharp
public abstract void MirrorY( D2Point pivot );
```

**Parameters**

- **pivot** —

#### `MoveBy` Method

Move the profile along the given vector

```csharp
public abstract void MoveBy( D2Vector v );
```

**Parameters**

- **v** —

#### `NumberOfBulges` Method

Return number of bulges in profile

```csharp
public abstract int NumberOfBulges();
```

#### `NumberOfNodes` Method

Return number of nodes in profile

```csharp
public abstract int NumberOfNodes();
```

#### `NumberOfSpans` Method

Return number of spans in profile

```csharp
public abstract int NumberOfSpans();
```

#### `Reverse` Method

Reverse direction of profile

```csharp
public abstract void Reverse();
```

#### `RotateBy` Method (Double)

Rotate profile about the origin by given angle

```csharp
public abstract void RotateBy( double angle );
```

**Parameters**

- **angle** — 

#### `RotateBy` Method (Double, D2Point)

Rotate the profile about the pivot by given angle

```csharp
public abstract void RotateBy( double angle , D2Point pivot );
```

**Parameters**

- **angle** — 
- **pivot** —

#### `ScaleBy` Method (Double)

Scale profile uniformly by given amount

```csharp
public abstract void ScaleBy( double s );
```

**Parameters**

- **s** — 

#### `ScaleBy` Method (Double, D2Point)

Scale profile by given amount about pivot

```csharp
public abstract void ScaleBy( double s , D2Point pivot );
```

**Parameters**

- **s** — 
- **pivot** —

#### `SetBulge` Method

Set the i'th bulge factor to given value

```csharp
public abstract void SetBulge( int i , double bulge );
```

**Parameters**

- **i** — 
- **bulge** —

#### `SetNode` Method

Set the ith node to the given point

```csharp
public abstract void SetNode( int i , D2Point node );
```

**Parameters**

- **i** — 
- **node** —

#### `ToString` Method

Returns a string describing the contents of the D2profile

```csharp
public abstract string ToString();
```

#### `WithoutDuplicatePoints` Method

Return a new profile which is a copy of this profile but without any duplicate points

```csharp
public abstract D2Profile WithoutDuplicatePoints();
```

## Operators

#### `Equality` Operator

left == right

```csharp
public static bool operator ==( D2Profile left , D2Profile right );
```

**Parameters**

- **left** — 
- **right** —

#### `Inequality` Operator

left != right

```csharp
public static bool operator !=( D2Profile left , D2Profile right );
```

**Parameters**

- **left** — 
- **right** —
