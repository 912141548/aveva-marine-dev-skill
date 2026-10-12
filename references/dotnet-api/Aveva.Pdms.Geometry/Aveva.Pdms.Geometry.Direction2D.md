---
title: Aveva.Pdms.Geometry.Direction2D Class
namespace: Aveva.Pdms.Geometry
assembly: Aveva.Pdms.Geometry
kind: Class
source: Aveva.Pdms.Geometry
---

# Aveva.Pdms.Geometry.Direction2D Class

> Summary description for Direction2D.

## Syntax

```csharp
public abstract class Direction2D
```

## Inheritance

`System.Object` → `Aveva.Pdms.Geometry.Direction2D`

## Thread Safety

Public static ( Shared in Visual Basic) members of this type are
safe for multithreaded operations. Instance members are not guaranteed to be
thread-safe.

## Requirements

Namespace:
Aveva.Pdms.Geometry
Assembly: Aveva.Pdms.Geometry (in Aveva.Pdms.Geometry.dll)

## Properties

#### `Right` Property

X Component

```csharp
public abstract double Right {get; set;}
```

#### `Up` Property

Y Component

```csharp
public abstract double Up {get; set;}
```

## Methods

#### `Angle` Method

Returns the angle between the two Direction2Ds

```csharp
public abstract double Angle( Direction2D d );
```

**Parameters**

- **d** —

#### `Create` Method ()

Create a Direction2D ( unset )

```csharp
public static Direction2D Create();
```

#### `Create` Method (Axis2D)

Create a Direction2D along the given axis

```csharp
public static Direction2D Create( Axis2D axis );
```

**Parameters**

- **axis** — 

#### `Create` Method (Position2D)

Create a Direction2D from the origin to p1

```csharp
public static Direction2D Create( Position2D p1 );
```

**Parameters**

- **p1** — 

#### `Create` Method (Position2D, Position2D)

Create a Direction2D from p1 to p2

```csharp
public static Direction2D Create( Position2D p1 , Position2D p2 );
```

**Parameters**

- **p1** — 
- **p2** — 

#### `Create` Method (Double)

Create a Direction2D rotated angle degrees from X axis

```csharp
public static Direction2D Create( double angle );
```

**Parameters**

- **angle** —

#### `Equals` Method (Direction2D)

Same Direction2D, within tolerance

```csharp
public abstract bool Equals( Direction2D dir );
```

**Parameters**

- **dir** — 

#### `Equals` Method (Object)

Same Direction2D, within tolerance

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
public abstract bool IsAntiParallel( Direction2D d );
```

**Parameters**

- **d** —

#### `IsParallel` Method

Returns true if the two directions are parallel (in the same direction)

```csharp
public abstract bool IsParallel( Direction2D d );
```

**Parameters**

- **d** —

#### `Midway` Method

Returns the direction halfway between the two directions

```csharp
public abstract Direction2D Midway( Direction2D d );
```

**Parameters**

- **d** —

#### `NearestAxis` Method

Returns the nearest Axis

```csharp
public abstract Axis2D NearestAxis();
```

#### `Opposite` Method

Returns the opposite direction

```csharp
public abstract Direction2D Opposite();
```

#### `Parse` Method

Return Direction2D object derived from a string in PDMS format

```csharp
public abstract Direction2D Parse( string str );
```

**Parameters**

- **str** —

#### `Rotate` Method

Rotate this Direction2D by amount degrees

```csharp
public abstract void Rotate( double degrees );
```

**Parameters**

- **degrees** —

#### `ToString` Method

Returns Direction2D property values in a string

```csharp
public abstract string ToString();
```

## Operators

#### `Equality` Operator

Same Direction2D within tolerance

```csharp
public static bool operator ==( Direction2D d1 , Direction2D d2 );
```

**Parameters**

- **d1** — 
- **d2** —

#### `Inequality` Operator

Not same Direction2D

```csharp
public static bool operator !=( Direction2D d1 , Direction2D d2 );
```

**Parameters**

- **d1** — 
- **d2** —
