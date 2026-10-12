---
title: Aveva.Pdms.Geometry.Arc2D Class
namespace: Aveva.Pdms.Geometry
assembly: Aveva.Pdms.Geometry
kind: Class
source: Aveva.Pdms.Geometry
---

# Aveva.Pdms.Geometry.Arc2D Class

> Summary description for Arc2D.

## Syntax

```csharp
public abstract class Arc2D
```

## Inheritance

`System.Object` → `Aveva.Pdms.Geometry.Arc2D`

## Thread Safety

Public static ( Shared in Visual Basic) members of this type are
safe for multithreaded operations. Instance members are not guaranteed to be
thread-safe.

## Requirements

Namespace:
Aveva.Pdms.Geometry
Assembly: Aveva.Pdms.Geometry (in Aveva.Pdms.Geometry.dll)

## Properties

#### `Centre` Property

Centre of the arc

```csharp
public abstract Position2D Centre {get; set;}
```

#### `End` Property

End position of the arc

```csharp
public abstract Position2D End {get; set;}
```

#### `Radius` Property

Redius of the arc

```csharp
public abstract double Radius {get; set;}
```

#### `Sense` Property

Sense of the arc

```csharp
public abstract bool Sense {get; set;}
```

#### `Start` Property

Start position of the arc

```csharp
public abstract Position2D Start {get; set;}
```

## Methods

#### `Angle` Method

Return angle subtended by start and end points at centre of Arc2D

```csharp
public abstract double Angle();
```

#### `AnglePosition` Method

Return Position2D on Arc2D which is at given angle from centre of Arc2D

```csharp
public abstract Position2D AnglePosition( double angle );
```

**Parameters**

- **angle** —

#### `Chord` Method

Return length of chord between start and end points

```csharp
public abstract double Chord();
```

#### `ChordHeight` Method

Return height of chord between start and end points

```csharp
public abstract double ChordHeight();
```

#### `Circle` Method

Return Arc2D which is the full circle from the Arc2D

```csharp
public abstract Arc2D Circle();
```

#### `Complement` Method

Return the complementary Arc2D – the remainder of the circle

```csharp
public abstract Arc2D Complement();
```

#### `Create` Method ()

Create Arc2D (all values zero)

```csharp
public static Arc2D Create();
```

#### `Create` Method (Line2D, Line2D, Position2D, Double, Boolean)

Create an Arc2D from two tangents and radius

```csharp
public static Arc2D Create( Line2D line1 , Line2D line2 , Position2D locator , double radius , bool anticlock );
```

**Parameters**

- **line1** — 
- **line2** — 
- **locator** — 
- **radius** — 
- **anticlock** — 

#### `Create` Method (Position2D, Position2D, Position2D)

Create an Arc2D passing through Position2Ds p1, p2 and p3

```csharp
public static Arc2D Create( Position2D p1 , Position2D p2 , Position2D p3 );
```

**Parameters**

- **p1** — 
- **p2** — 
- **p3** — 

#### `Create` Method (Position2D, Double, Position2D, Position2D, Boolean)

Create an Arc2D from 2 positions, centre, radius and direction

```csharp
public static Arc2D Create( Position2D centre , double radius , Position2D start , Position2D end , bool anticlock );
```

**Parameters**

- **centre** — 
- **radius** — 
- **start** — 
- **end** — 
- **anticlock** — 

#### `Create` Method (Position2D, Double, Double, Double, Boolean)

Create an Arc2D from centre, radius, startangle and endangles and sense

```csharp
public static Arc2D Create( Position2D centre , double radius , double startAngle , double endAngle , bool anticlock );
```

**Parameters**

- **centre** — 
- **radius** — 
- **startAngle** — 
- **endAngle** — 
- **anticlock** —

#### `Equals` Method (Arc2D)

Same Arc2D, within tolerance

```csharp
public abstract bool Equals( Arc2D arc );
```

**Parameters**

- **arc** — 

#### `Equals` Method (Object)

Same Arc2D, within tolerance

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

#### `Intersections` Method (Arc2D, Position2D[])

Returns intersection points of two Arc2Ds. Returns false if they do not intersect

```csharp
public abstract bool Intersections( Arc2D a , ref Position2D[] pa );
```

**Parameters**

- **a** — 
- **pa** — 

#### `Intersections` Method (Line2D, Position2D[])

Returns intersection points of Arc2D with line. Returns false if they do not intersect

```csharp
public abstract bool Intersections( Line2D line , ref Position2D[] pa );
```

**Parameters**

- **line** — 
- **pa** —

#### `IsOnArc` Method

Return true if p is on Arc2D

```csharp
public abstract bool IsOnArc( Position2D p );
```

**Parameters**

- **p** —

#### `Length` Method

Return length of Arc2D

```csharp
public abstract double Length();
```

#### `MoveBy` Method

Move Arc2D by given x,y values

```csharp
public abstract void MoveBy( double x , double y );
```

**Parameters**

- **x** — 
- **y** —

#### `ToString` Method

Returns Arc2D property values in a string

```csharp
public abstract string ToString();
```

## Operators

#### `Equality` Operator

Same Arc2D

```csharp
public static bool operator ==( Arc2D a1 , Arc2D a2 );
```

**Parameters**

- **a1** — 
- **a2** —

#### `Inequality` Operator

Not same Arc2D

```csharp
public static bool operator !=( Arc2D a1 , Arc2D a2 );
```

**Parameters**

- **a1** — 
- **a2** —
