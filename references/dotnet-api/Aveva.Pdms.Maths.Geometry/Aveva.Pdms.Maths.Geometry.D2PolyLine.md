---
title: Aveva.Pdms.Maths.Geometry.D2PolyLine Class
namespace: Aveva.Pdms.Maths.Geometry
assembly: Aveva.Pdms.Maths.Geometry
kind: Class
source: Aveva.Pdms.Maths.Geometry
---

# Aveva.Pdms.Maths.Geometry.D2PolyLine Class

> 2-D polyline sequence of straight line segments connected end to end

## Syntax

```csharp
public abstract class D2PolyLine
```

## Inheritance

`System.Object` → `Aveva.Pdms.Maths.Geometry.D2PolyLine`

## Thread Safety

Public static ( Shared in Visual Basic) members of this type are
safe for multithreaded operations. Instance members are not guaranteed to be
thread-safe.

## Requirements

Namespace:
Aveva.Pdms.Maths.Geometry
Assembly: Aveva.Pdms.Maths.Geometry (in Aveva.Pdms.Maths.Geometry.dll)

## Methods

#### `AddPolyLine` Method

Add a new polyline to the end

```csharp
public abstract D2PolyLine AddPolyLine( D2PolyLine line );
```

**Parameters**

- **line** —

#### `AddVertex` Method

Donate a vertex (heap allocated)

```csharp
public abstract void AddVertex( D2Point vertex );
```

**Parameters**

- **vertex** —

#### `Clone` Method

deep copy

```csharp
public abstract D2PolyLine Clone();
```

#### `Create` Method ()

Null constructor

```csharp
public static D2PolyLine Create();
```

#### `Create` Method (D2PolyLine)

Copy a polyLine

```csharp
public static D2PolyLine Create( D2PolyLine line );
```

**Parameters**

- **line** — 

#### `Create` Method (Int32)

Construct a polyline with size elements

```csharp
public static D2PolyLine Create( int size );
```

**Parameters**

- **size** —

#### `Equals` Method (D2PolyLine)

test for equality

```csharp
public abstract bool Equals( D2PolyLine d2 );
```

**Parameters**

- **d2** — 

#### `Equals` Method (Object)

override equals

```csharp
public override bool Equals( object obj );
```

**Parameters**

- **obj** —

#### `First` Method

Return the start point

```csharp
public abstract D2Point First();
```

#### `GetHashCode` Method

overrides gethashcode

```csharp
public override int GetHashCode();
```

#### `HasNoVertices` Method

Return true if there are no vertices

```csharp
public abstract bool HasNoVertices();
```

#### `InsertVertexAt` Method

Add a new vertex at position i

```csharp
public abstract void InsertVertexAt( int i , D2Point vertex );
```

**Parameters**

- **i** — 
- **vertex** —

#### `Last` Method

Return the end point

```csharp
public abstract D2Point Last();
```

#### `MinMaxBox` Method

Return a bounding box

```csharp
public abstract D2Limits MinMaxBox();
```

#### `MoveBy` Method

Move the whole polyline by given x,y offsets

```csharp
public abstract void MoveBy( double dx , double dy );
```

**Parameters**

- **dx** — 
- **dy** —

#### `NumberOfVertices` Method

Return the number of vertices on the polyline

```csharp
public abstract int NumberOfVertices();
```

#### `RemoveAll` Method

Remove all spans from the polyline

```csharp
public abstract void RemoveAll();
```

#### `RemoveLastVertex` Method

Remove the last vertex

```csharp
public abstract void RemoveLastVertex();
```

#### `Reverse` Method

Reverse the direction of the polyline

```csharp
public abstract void Reverse();
```

#### `RotateBy` Method

Rotate polyline about origin

```csharp
public abstract void RotateBy( double angle );
```

**Parameters**

- **angle** —

#### `SelfIntersecting` Method

Returns true if one span of the polyline intersects another

```csharp
public abstract bool SelfIntersecting();
```

#### `SetVertex` Method

Set the ith vertex to the given point

```csharp
public abstract void SetVertex( int i , D2Point point );
```

**Parameters**

- **i** — 
- **point** —

#### `ToString` Method

Returns a string describing the contents of the polyline

```csharp
public abstract string ToString();
```

#### `Vertex` Method

Return the position of the ith vertex

```csharp
public abstract D2Point Vertex( int i );
```

**Parameters**

- **i** —

## Operators

#### `Equality` Operator

invoked by left == right

```csharp
public static bool operator ==( D2PolyLine left , D2PolyLine right );
```

**Parameters**

- **left** — 
- **right** —

#### `Inequality` Operator

invoked by left != right

```csharp
public static bool operator !=( D2PolyLine left , D2PolyLine right );
```

**Parameters**

- **left** — 
- **right** —
