---
title: Aveva.Pdms.Geometry.Direction Class
namespace: Aveva.Pdms.Geometry
assembly: Aveva.Pdms.Geometry
kind: Class
source: Aveva.Pdms.Geometry
---

# Aveva.Pdms.Geometry.Direction Class

> Summary description for Direction.

## Syntax

```csharp
public abstract class Direction
```

## Inheritance

`System.Object` → `Aveva.Pdms.Geometry.Direction`

## Thread Safety

Public static ( Shared in Visual Basic) members of this type are
safe for multithreaded operations. Instance members are not guaranteed to be
thread-safe.

## Requirements

Namespace:
Aveva.Pdms.Geometry
Assembly: Aveva.Pdms.Geometry (in Aveva.Pdms.Geometry.dll)

## Properties

#### `East` Property

E component

```csharp
public abstract double East {get; set;}
```

#### `North` Property

N component

```csharp
public abstract double North {get; set;}
```

#### `Up` Property

U component

```csharp
public abstract double Up {get; set;}
```

## Methods

#### `Angle` Method

Returns the angle between the two directions

```csharp
public abstract double Angle( Direction d );
```

**Parameters**

- **d** —

#### `Create` Method ()

Default Direction

```csharp
public static Direction Create();
```

#### `Create` Method (Axis)

Create a Direction along the given axis

```csharp
public static Direction Create( Axis axis );
```

**Parameters**

- **axis** — 

#### `Create` Method (Axis, Double, Axis)

Create a Direction rotated angle degrees from a1 towards a2

```csharp
public static Direction Create( Axis axis , double angle , Axis axis2 );
```

**Parameters**

- **axis** — 
- **angle** — 
- **axis2** — 

#### `Create` Method (Axis, Double, Axis, Double, Axis)

Create a Direction rotated angle degrees from a1 towards a2, and then ang2 degrees towards a3

```csharp
public static Direction Create( Axis axis , double ang1 , Axis a2 , double ang2 , Axis a3 );
```

**Parameters**

- **axis** — 
- **ang1** — 
- **a2** — 
- **ang2** — 
- **a3** — 

#### `Create` Method (Position)

Create a direction from the origin to p1

```csharp
public static Direction Create( Position p1 );
```

**Parameters**

- **p1** — 

#### `Create` Method (Position, Position)

Create a Direction from p1 to p2

```csharp
public static Direction Create( Position p1 , Position p2 );
```

**Parameters**

- **p1** — 
- **p2** — 

#### `Create` Method (String)

```csharp
public static Direction Create( string dirstring );
```

#### `Equals` Method (Direction)

Same Direction, within tolerance

```csharp
public abstract bool Equals( Direction dir );
```

**Parameters**

- **dir** — 

#### `Equals` Method (Object)

Same Direction, within tolerance

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

#### `IsAntiParallel` Method

Returns true if the two directions are parallel (in the opposite direction)

```csharp
public abstract bool IsAntiParallel( Direction d );
```

**Parameters**

- **d** —

#### `IsParallel` Method

Returns true if the two directions are parallel (in the same direction)

```csharp
public abstract bool IsParallel( Direction d );
```

**Parameters**

- **d** —

#### `Midway` Method

Returns the direction halfway between the two directions

```csharp
public abstract Direction Midway( Direction d );
```

**Parameters**

- **d** —

#### `NearestAxis` Method

Returns the nearest Axis

```csharp
public abstract Axis NearestAxis();
```

#### `Normal` Method

Returns a plane normal to the Direction through pos

```csharp
public abstract Plane Normal( Position pos );
```

**Parameters**

- **pos** —

#### `Opposite` Method

Returns the opposite direction

```csharp
public abstract Direction Opposite();
```

#### `Orthogonal` Method

Returns Direction that is orthogonal between the two directions

```csharp
public abstract Direction Orthogonal( Direction d );
```

**Parameters**

- **d** —

#### `Parse` Method

Converts a direction in PDMS format into a Direction object

```csharp
public abstract Direction Parse( string str );
```

**Parameters**

- **str** —

#### `Project` Method

Returns the distance which is the projection of this direction onto Direction d

```csharp
public abstract double Project( Direction d );
```

**Parameters**

- **d** —

#### `RotateAbout` Method

Rotate this direction towards direction dir by amount degrees

```csharp
public abstract void RotateAbout( Direction dir , double degrees );
```

**Parameters**

- **dir** — 
- **degrees** —

#### `RotateTowards` Method

Rotate this direction towards direction dir by amount degrees

```csharp
public abstract void RotateTowards( Direction dir , double degrees );
```

**Parameters**

- **dir** — 
- **degrees** —

#### `ToString` Method

Returns Direction in PDMS Format

```csharp
public abstract string ToString();
```

## Operators

#### `Equality` Operator

Exact equality

```csharp
public static bool operator ==( Direction d1 , Direction d2 );
```

**Parameters**

- **d1** — 
- **d2** —

#### `Inequality` Operator

Exact inequality

```csharp
public static bool operator !=( Direction d1 , Direction d2 );
```

**Parameters**

- **d1** — 
- **d2** —
