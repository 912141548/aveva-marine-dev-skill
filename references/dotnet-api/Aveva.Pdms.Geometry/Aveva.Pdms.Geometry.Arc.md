---
title: Aveva.Pdms.Geometry.Arc Class
namespace: Aveva.Pdms.Geometry
assembly: Aveva.Pdms.Geometry
kind: Class
source: Aveva.Pdms.Geometry
---

# Aveva.Pdms.Geometry.Arc Class

> An arc in 3d space. This is represented as a 2D arc and a given Oriented Plane. It is defined by the Oriented Plane origin as centre, a radius, start angle defined as an angular offset from the X direction of the orientation, and an end angle similarly defined.

## Syntax

```csharp
public abstract class Arc
```

## Inheritance

`System.Object` → `Aveva.Pdms.Geometry.Arc`

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

Centre

```csharp
public abstract Position Centre {get;}
```

#### `EndAngle` Property

End angle from X axis of Orientation

```csharp
public abstract double EndAngle {get; set;}
```

#### `Plane` Property

OrientedPlane of arc – the arc is in the XY plane – centred on the origin of the plane

```csharp
public abstract Plane Plane {get; set;}
```

#### `Radius` Property

Radius

```csharp
public abstract double Radius {get;}
```

#### `Sense` Property

Sense: 1 = anticlockwise, 0 = clockwise

```csharp
public abstract bool Sense {get; set;}
```

#### `StartAngle` Property

Start angle from X axis of Orientation

```csharp
public abstract double StartAngle {get; set;}
```

## Methods

#### `Angle` Method

Return the subtended angle of arc

```csharp
public abstract double Angle();
```

#### `AngleDirection` Method

Return the direction from the centre of the arc through a point at angle degrees from the X axis

```csharp
public abstract Direction AngleDirection( double degrees );
```

**Parameters**

- **degrees** —

#### `AngleTangent` Method

Return the direction of a tangent to the arc at the angle ang from the X axis, in the sense of the arc

```csharp
public abstract Direction AngleTangent( double ang );
```

**Parameters**

- **ang** —

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

Return Arc which is the full circle from the arc

```csharp
public abstract Arc Circle();
```

#### `Complement` Method

Return the complementary Arc – the remainder of the circle

```csharp
public abstract Arc Complement();
```

#### `Create` Method ()

Default Arc

```csharp
public static Arc Create();
```

#### `Create` Method (Plane, Double, Double, Double, Boolean)

Construct an Arc from an Oriented Plane, start and end angles and radius. The Boolean antiClock is used to decide whether clockwise or anticlockwise arc is required

```csharp
public static Arc Create( Plane plane , double radius , double startAngle , double endAngle , bool antiClock );
```

**Parameters**

- **plane** — 
- **radius** — 
- **startAngle** — 
- **endAngle** — 
- **antiClock** — 

#### `Create` Method (Position, Position, Position)

Construct an Arc passing through Positions p1 p2 and p3. The arc will have invalid state if the points are collinear.

```csharp
public static Arc Create( Position p1 , Position p2 , Position p3 );
```

**Parameters**

- **p1** — 
- **p2** — 
- **p3** — 

#### `Create` Method (Position, Position, Position, Double)

Construct an Arc from two tangents (from apex to posA and apex to PosB) , centre and radius The arc will have invalid state if the points are collinear.

```csharp
public static Arc Create( Position posA , Position posB , Position apex , double radius );
```

**Parameters**

- **posA** — 
- **posB** — 
- **apex** — 
- **radius** — 

#### `Create` Method (Position, Double, Position, Position, Boolean)

Construct an Arc from start and end positions, centre, and radius. The oriented plane will be determined by the centre, start and end positions. The start and end positions are used to determine the start and end angles for the arc. The Boolean antiClock is used to decide whether clockwise or anticlockwise arc is required.

```csharp
public static Arc Create( Position centre , double radius , Position start , Position end , bool antiClock );
```

**Parameters**

- **centre** — 
- **radius** — 
- **start** — 
- **end** — 
- **antiClock** —

#### `EndPosition` Method

Position of end of arc

```csharp
public abstract Position EndPosition();
```

#### `EndTangent` Method

Return the direction of a tangent to the arc at the end angle, in the sense of the arc

```csharp
public abstract Direction EndTangent();
```

#### `Equals` Method (Arc)

Same Arc, within tolerance

```csharp
public abstract bool Equals( Arc arc );
```

**Parameters**

- **arc** — 

#### `Equals` Method (Object)

Same Arc, within tolerance

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

#### `Intersections` Method (Arc, Position[])

Returns intersection points of two Arcs. Returns false if they do not intersect. Intersections will only be calculated if the arcs are defined in parallel planes. The given arc is projected onto the plane of the first.

```csharp
public abstract bool Intersections( Arc a , ref Position[] pa );
```

**Parameters**

- **a** — 
- **pa** — 

#### `Intersections` Method (Line, Position[])

Returns intersection points of arc with line projected onto the plane of the arc. Returns false if they do not intersect.

```csharp
public abstract bool Intersections( Line line , ref Position[] pa );
```

**Parameters**

- **line** — 
- **pa** — 

#### `Intersections` Method (Plane, Position[])

Returns intersection points of arc with plane. Returns false if they do not intersect.

```csharp
public abstract bool Intersections( Plane plane , ref Position[] pa );
```

**Parameters**

- **plane** — 
- **pa** —

#### `InValid` Method

Return true if arc is invalid

```csharp
public abstract bool InValid();
```

#### `IsCircle` Method

Return true if arc is a full circle

```csharp
public abstract bool IsCircle();
```

#### `IsOnArc` Method

Return true if p is on arc

```csharp
public abstract bool IsOnArc( Position p );
```

**Parameters**

- **p** —

#### `Length` Method

Return length of arc

```csharp
public abstract double Length();
```

#### `MoveBy` Method

Move the centre of the arc.this distance along the Oriented Plane normal.

```csharp
public abstract void MoveBy( double dist );
```

**Parameters**

- **dist** —

#### `MoveTo` Method

Move the centre of the arc to the new position, keeping the same orientation.

```csharp
public abstract void MoveTo( Position centre );
```

**Parameters**

- **centre** —

#### `Position` Method

Return Position on Arc which is at given angle from X axis of the orientation

```csharp
public abstract Position Position( double angle );
```

**Parameters**

- **angle** —

#### `Proportion` Method

Return the position (angle from the X-axis) at ration from the start of the arc: Angle = (endAngle – startAngle) * ratio + StartAngle

```csharp
public abstract double Proportion( double ratio );
```

**Parameters**

- **ratio** —

#### `SetChord` Method

Changes the end angle so that the end position is at val distance from start position, maintaining centre and radius. Does nothing if val greater then 2*radius, or val less than 0

```csharp
public abstract void SetChord( double val );
```

**Parameters**

- **val** —

#### `StartPosition` Method

Position of start of arc

```csharp
public abstract Position StartPosition();
```

#### `StartTangent` Method

Return the direction of a tangent to the arc at the start angle, in the sense of the arc

```csharp
public abstract Direction StartTangent();
```

#### `TangentPoints` Method (Arc)

Returns the tangents between the two arcs (extended to full circles) (Note that there can be up to 4 lines returned.)

```csharp
public abstract Line[] TangentPoints( Arc arc );
```

**Parameters**

- **arc** — 

#### `TangentPoints` Method (Position)

Returns the points of tangency from the Position pos to the arc (extended to a full circle)The supplied pos is projected onto the plane of the arc.

```csharp
public abstract Position[] TangentPoints( Position pos );
```

**Parameters**

- **pos** —

#### `ToString` Method

Returns Arc property values as a string

```csharp
public abstract string ToString();
```

## Operators

#### `Equality` Operator

Same Arc

```csharp
public static bool operator ==( Arc a1 , Arc a2 );
```

**Parameters**

- **a1** — 
- **a2** —

#### `Inequality` Operator

Not Same Arc

```csharp
public static bool operator !=( Arc a1 , Arc a2 );
```

**Parameters**

- **a1** — 
- **a2** —
