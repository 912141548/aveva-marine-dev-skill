---
title: Aveva.Pdms.Geometry.Line2D Class
namespace: Aveva.Pdms.Geometry
assembly: Aveva.Pdms.Geometry
kind: Class
source: Aveva.Pdms.Geometry
---

# Aveva.Pdms.Geometry.Line2D Class

> Summary description for Line2D.

## Syntax

```csharp
public abstract class Line2D
```

## Inheritance

`System.Object` → `Aveva.Pdms.Geometry.Line2D`

## Thread Safety

Public static ( Shared in Visual Basic) members of this type are
safe for multithreaded operations. Instance members are not guaranteed to be
thread-safe.

## Requirements

Namespace:
Aveva.Pdms.Geometry
Assembly: Aveva.Pdms.Geometry (in Aveva.Pdms.Geometry.dll)

## Properties

#### `Direction` Property

Direction of line

```csharp
public abstract Direction2D Direction {get; set;}
```

#### `End` Property

[get] Returns Unset Position if this is an infinite line

```csharp
public abstract Position2D End {get; set;}
```

#### `Start` Property

[get] Returns Unset Position if this is an infinite line

```csharp
public abstract Position2D Start {get; set;}
```

## Methods

#### `Create` Method ()

Create Line2D (unset value)

```csharp
public static Line2D Create();
```

#### `Create` Method (Direction2D, Position2D)

Create an unbounded Line2D through p in given direction

```csharp
public static Line2D Create( Direction2D dir , Position2D p );
```

**Parameters**

- **dir** — 
- **p** — 

#### `Create` Method (Position2D, Position2D)

Create a bounded Line2D from start to end.

```csharp
public static Line2D Create( Position2D start , Position2D end );
```

**Parameters**

- **start** — 
- **end** — 

#### `Create` Method (Double, Double, Double, Double)

Create a Line2D between two coordinates

```csharp
public static Line2D Create( double x1 , double y1 , double x2 , double y2 );
```

**Parameters**

- **x1** — 
- **y1** — 
- **x2** — 
- **y2** —

#### `Distance` Method (Line2D)

Returns the minimum distance from line

```csharp
public abstract double Distance( Line2D line );
```

**Parameters**

- **line** — 

#### `Distance` Method (Position2D)

Returns the minimum distance from pos

```csharp
public abstract double Distance( Position2D pos );
```

**Parameters**

- **pos** —

#### `Equals` Method (Line2D)

Same Line2D

```csharp
public abstract bool Equals( Line2D line );
```

**Parameters**

- **line** — 

#### `Equals` Method (Object)

Same Line2D

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

#### `Intersects` Method

Return true if lines intersect.

```csharp
public abstract bool Intersects( Line2D line );
```

**Parameters**

- **line** —

#### `IsBounded` Method

Return true if start or end Positions are set

```csharp
public abstract bool IsBounded();
```

#### `IsOnLine` Method

Returns true if p is on the line (and within the bounds if it is bounded )

```csharp
public abstract bool IsOnLine( Position2D p );
```

**Parameters**

- **p** —

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

Returns the length of the Line2D if it is bounded, otherwise -1

```csharp
public abstract double Length();
```

#### `NearestPoint` Method

Return Position2D on a line which is the projection of p onto line. Note that if the line is bounded, the nearest point may be either the start or end point if the projection is beyond the bounds.

```csharp
public abstract Position2D NearestPoint( Position2D p );
```

**Parameters**

- **p** —

#### `Proportion` Method

Return the Position2D at ratio along the line from the Start Position2D. ratio > 0 returns value off end of line, ratio less than 0 return value before start of line. Unbounded lines return Unset Position2D

```csharp
public abstract Position2D Proportion( double ratio );
```

**Parameters**

- **ratio** —

#### `ToString` Method

Returns Line2D property values in a string

```csharp
public abstract string ToString();
```

## Operators

#### `Equality` Operator

/// Same Line2D

```csharp
public static bool operator ==( Line2D t1 , Line2D t2 );
```

**Parameters**

- **t1** — 
- **t2** —

#### `Inequality` Operator

Not same Line2D

```csharp
public static bool operator !=( Line2D t1 , Line2D t2 );
```

**Parameters**

- **t1** — 
- **t2** —
