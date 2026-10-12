---
title: Aveva.Pdms.Geometry.Line Class
namespace: Aveva.Pdms.Geometry
assembly: Aveva.Pdms.Geometry
kind: Class
source: Aveva.Pdms.Geometry
---

# Aveva.Pdms.Geometry.Line Class

> Summary description for Line.

## Syntax

```csharp
public abstract class Line
```

## Inheritance

`System.Object` → `Aveva.Pdms.Geometry.Line`

## Thread Safety

Public static ( Shared in Visual Basic) members of this type are
safe for multithreaded operations. Instance members are not guaranteed to be
thread-safe.

## Requirements

Namespace:
Aveva.Pdms.Geometry
Assembly: Aveva.Pdms.Geometry (in Aveva.Pdms.Geometry.dll)

## Properties

#### `End` Property

[get] Returns Null if this is an infinite line [set] Setting the end position turns an unbounded line into a semi-bounded line, and a semi-bounded-with-start line into a bounded line

```csharp
public abstract Position End {get; set;}
```

#### `Start` Property

[get] Returns Null if this is an infinite line [set] Setting the start position turns an unbounded line into a semi-bounded line, and a semi-bounded-with-end line into a bounded line.

```csharp
public abstract Position Start {get; set;}
```

## Methods

#### `Create` Method ()

Null Constructor

```csharp
public static Line Create();
```

#### `Create` Method (Direction, Position)

Create an unbounded Line through p in given direction. Note that Position p is not defined as either the start or end.

```csharp
public static Line Create( Direction dir , Position p );
```

**Parameters**

- **dir** — 
- **p** — 

#### `Create` Method (Position, Position)

Create a bounded Line from start to end.

```csharp
public static Line Create( Position start , Position end );
```

**Parameters**

- **start** — 
- **end** — 

#### `Create` Method (Double, Double, Double, Double, Double, Double)

Create a bounded Line between two coordinates

```csharp
public static Line Create( double x1 , double y1 , double z1 , double x2 , double y2 , double z2 );
```

**Parameters**

- **x1** — 
- **y1** — 
- **z1** — 
- **x2** — 
- **y2** — 
- **z2** —

#### `Direction` Method

Returns the direction of the line

```csharp
public abstract Direction Direction();
```

#### `Distance` Method (Line)

Returns the minimum distance from line

```csharp
public abstract double Distance( Line line );
```

**Parameters**

- **line** — 

#### `Distance` Method (Position)

Returns the minimum distance from pos

```csharp
public abstract double Distance( Position pos );
```

**Parameters**

- **pos** —

#### `DoesOverlap` Method

Returns true if lines overlap

```csharp
public abstract bool DoesOverlap( Line l1 );
```

**Parameters**

- **l1** —

#### `DoesUnion` Method

Returns true if lines can be unioned

```csharp
public abstract bool DoesUnion( Line l1 );
```

#### `Equals` Method (Line)

Same line

```csharp
public abstract bool Equals( Line line );
```

**Parameters**

- **line** — 

#### `Equals` Method (Object)

Same line

```csharp
public override bool Equals( object obj );
```

**Parameters**

- **obj** —

#### `GetHashCode` Method

A hash method is used to quickly generate a hash code, which is an int that corresponds to the value of an object. Hash codes allow C# to store objects more efficiently in collections

```csharp
public override int GetHashCode();
```

#### `Intersection` Method (Line)

Return intersection point of two lines. Returns Null if they do not intersect.

```csharp
public abstract Position Intersection( Line line );
```

**Parameters**

- **line** — 

#### `Intersection` Method (Plane)

Return intersection point of the line with Pplane plane. Returns Null if they do not intersect.

```csharp
public abstract Position Intersection( Plane plane );
```

**Parameters**

- **plane** —

#### `Intersections` Method

Return intersection points of the line with Arc arc..

```csharp
public abstract Position[] Intersections( Arc arc );
```

**Parameters**

- **arc** —

#### `Intersects` Method

Return true if lines intersect.

```csharp
public abstract bool Intersects( Line line );
```

**Parameters**

- **line** —

#### `IsBounded` Method

Return true if both start and end Positions are set.

```csharp
public abstract bool IsBounded();
```

#### `IsOnLine` Method

Returns true if p is on the line (and within the bounds if it is bounded )

```csharp
public abstract bool IsOnLine( Position p );
```

**Parameters**

- **p** —

#### `IsParallel` Method

Returns true if two lines are parallel

```csharp
public abstract bool IsParallel( Line line );
```

**Parameters**

- **line** —

#### `IsSemiBoundedAtEnd` Method

Return true if end position is set, but start position is not.

```csharp
public abstract bool IsSemiBoundedAtEnd();
```

#### `IsSemiBoundedAtStart` Method

Return true if start position is set, but end position is not.

```csharp
public abstract bool IsSemiBoundedAtStart();
```

#### `Length` Method

Returns the length of the line if it is bounded, otherwise -1

```csharp
public abstract double Length();
```

#### `NearestPoint` Method

Return Position on a line which is the projection of pos onto line. If the line is bounded, the nearest point may be either the start or end point if the projection is beyond the bounds.

```csharp
public abstract Position NearestPoint( Position pos );
```

**Parameters**

- **pos** —

#### `Overlap` Method

Returns the overlapping line of two parallel bounded lines, all position projected onto original line. If the lines are not parallel, returns Null. For unbounded lines returns the first Line.

```csharp
public abstract Line Overlap( Line line );
```

**Parameters**

- **line** —

#### `Parallel` Method (Direction, Double)

Return line which is parallel to this line and offset from it in Direction dir by amount offset

```csharp
public abstract Line Parallel( Direction dir , double offset );
```

**Parameters**

- **dir** — 
- **offset** — 

#### `Parallel` Method (Position)

Return line which is parallel to this line and passes through point p

```csharp
public abstract Line Parallel( Position p );
```

**Parameters**

- **p** —

#### `Perpendicular` Method

Return line which is perpendicular to this line and passes through point p

```csharp
public abstract Line Perpendicular( Position p );
```

**Parameters**

- **p** —

#### `Proportion` Method

Return the Position at ratio along the line from the Start Position. ratio > 0 returns value off end of line, ratio less than zero value before start of line.Unbounded lines return Null

```csharp
public abstract Position Proportion( double ratio );
```

**Parameters**

- **ratio** —

#### `Reverse` Method

Reverse the start and end positions and/or direction of the line

```csharp
public abstract void Reverse();
```

#### `ToString` Method

Returns Line property values as a string

```csharp
public abstract string ToString();
```

#### `Union` Method

Returns the union of two parallel bounded Lines, all positions are projected onto original Line. If the lines are not parallel, returns Null. For unbounded lines returns the first Line

```csharp
public abstract Line Union( Line line );
```

**Parameters**

- **line** —

## Operators

#### `Equality` Operator

Same Line

```csharp
public static bool operator ==( Line t1 , Line t2 );
```

**Parameters**

- **t1** — 
- **t2** —

#### `Inequality` Operator

Not Same Line

```csharp
public static bool operator !=( Line t1 , Line t2 );
```

**Parameters**

- **t1** — 
- **t2** —
