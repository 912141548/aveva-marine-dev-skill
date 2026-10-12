---
title: Aveva.Pdms.Geometry.Plane Class
namespace: Aveva.Pdms.Geometry
assembly: Aveva.Pdms.Geometry
kind: Class
source: Aveva.Pdms.Geometry
---

# Aveva.Pdms.Geometry.Plane Class

> Summary description for Plane.

## Syntax

```csharp
public abstract class Plane
```

## Inheritance

`System.Object` → `Aveva.Pdms.Geometry.Plane`

## Thread Safety

Public static ( Shared in Visual Basic) members of this type are
safe for multithreaded operations. Instance members are not guaranteed to be
thread-safe.

## Requirements

Namespace:
Aveva.Pdms.Geometry
Assembly: Aveva.Pdms.Geometry (in Aveva.Pdms.Geometry.dll)

## Properties

#### `Orientation` Property

```csharp
public abstract Orientation Orientation {get; set;}
```

#### `Position` Property

```csharp
public abstract Position Position {get; set;}
```

## Methods

#### `Create` Method ()

Create default plane

```csharp
public static Plane Create();
```

#### `Create` Method (Direction, Position)

Create a plane through pos with normal dir

```csharp
public static Plane Create( Direction d1 , Position pos );
```

**Parameters**

- **d1** — 
- **pos** —

#### `Equals` Method (Plane)

Same Plane

```csharp
public abstract bool Equals( Plane plane );
```

**Parameters**

- **plane** — 

#### `Equals` Method (Object)

Same Plane

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

#### `internalCreate` Method ()

Create default plane

```csharp
public abstract Plane internalCreate();
```

#### `internalCreate` Method (Direction, Position)

Create a plane through pos with normal dir

```csharp
public abstract Plane internalCreate( Direction d1 , Position pos );
```

**Parameters**

- **d1** — 
- **pos** —

#### `Intersection` Method (Line)

Returns the intersection of the plane with the line lin (infinitely extended )

```csharp
public abstract Position Intersection( Line lin );
```

**Parameters**

- **lin** — 

#### `Intersection` Method (Plane)

Returns an unbounded line, which is the intersection line of this plane with pl1. Returns Null if they do not intersect.

```csharp
public abstract Line Intersection( Plane pl1 );
```

**Parameters**

- **pl1** — 

#### `Intersection` Method (Plane, Plane)

Returns the intersection point of this plane with pl1 and pl2. Returns Null if they do not intersect

```csharp
public abstract Position Intersection( Plane pl1 , Plane pl2 );
```

**Parameters**

- **pl1** — 
- **pl2** — 

#### `Intersection` Method (PointVector)

Returns the intersection of the plane with the direction of pv.

```csharp
public abstract Position Intersection( PointVector pv );
```

**Parameters**

- **pv** —

#### `Intersections` Method

Returns the set of intersections with the plane and the Arc arc.

```csharp
public abstract Position[] Intersections( Arc arc );
```

**Parameters**

- **arc** —

#### `Line` Method

Returns a line of length val along the normal of the plane

```csharp
public abstract Line Line( double val );
```

**Parameters**

- **val** —

#### `Near` Method

Returns the nearest Position on the plane to pos

```csharp
public abstract Position Near( Position pos );
```

**Parameters**

- **pos** —

#### `Normal` Method

Return the Z component of the Orientation, uses standard PDMS method of obtaining X and Y components.

```csharp
public abstract Direction Normal();
```

#### `PointVector` Method

Returns a PointVector positioned at the origin of the plane and along the direction of the normal of the plane

```csharp
public abstract PointVector PointVector();
```

#### `Position3D` Method

Returns Position of pos2 offset from the plane origin

```csharp
public abstract Position Position3D( Position2D pos2 );
```

**Parameters**

- **pos2** —

#### `ToString` Method

Return Plane property values as a string

```csharp
public abstract string ToString();
```

#### `Towards` Method

Modifies the orientation so that the normal is directed towards the position pos.

```csharp
public abstract void Towards( Position pos );
```

**Parameters**

- **pos** —

#### `XYOffset` Method

Returns the position mapped onto the plane in terms of an XY offset from the plane origin

```csharp
public abstract Position2D XYOffset( Position pos );
```

**Parameters**

- **pos** —

## Operators

#### `Equality` Operator

Same Plane, within tolerance

```csharp
public static bool operator ==( Plane p1 , Plane p2 );
```

**Parameters**

- **p1** — 
- **p2** —

#### `Inequality` Operator

Not same Plane

```csharp
public static bool operator !=( Plane p1 , Plane p2 );
```

**Parameters**

- **p1** — 
- **p2** —
