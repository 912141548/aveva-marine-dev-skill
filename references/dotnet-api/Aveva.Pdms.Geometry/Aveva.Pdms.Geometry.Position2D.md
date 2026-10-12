---
title: Aveva.Pdms.Geometry.Position2D Class
namespace: Aveva.Pdms.Geometry
assembly: Aveva.Pdms.Geometry
kind: Class
source: Aveva.Pdms.Geometry
---

# Aveva.Pdms.Geometry.Position2D Class

> Summary description for Position2D.

## Syntax

```csharp
public abstract class Position2D
```

## Inheritance

`System.Object` → `Aveva.Pdms.Geometry.Position2D`

## Thread Safety

Public static ( Shared in Visual Basic) members of this type are
safe for multithreaded operations. Instance members are not guaranteed to be
thread-safe.

## Requirements

Namespace:
Aveva.Pdms.Geometry
Assembly: Aveva.Pdms.Geometry (in Aveva.Pdms.Geometry.dll)

## Properties

#### `X` Property

X component of position

```csharp
public abstract double X {get; set;}
```

#### `Y` Property

Y component of position

```csharp
public abstract double Y {get; set;}
```

## Methods

#### `Angle` Method

Return the angle between p1 and p2 about this Position

```csharp
public abstract double Angle( Position2D p1 , Position2D p2 );
```

**Parameters**

- **p1** — 
- **p2** —

#### `Create` Method ()

Create Position2D (all values zero)

```csharp
public static Position2D Create();
```

#### `Create` Method (Double, Double)

Create a Position2D from x, y coordinates

```csharp
public static Position2D Create( double x , double y );
```

**Parameters**

- **x** — 
- **y** —

#### `Distance` Method

Distance from Position2D p

```csharp
public abstract double Distance( Position2D p );
```

**Parameters**

- **p** —

#### `Equals` Method (Position2D)

Same Position2D, within tolerance

```csharp
public abstract bool Equals( Position2D p );
```

**Parameters**

- **p** — 

#### `Equals` Method (Object)

Same Position2D, within tolerance

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

#### `MidPoint` Method

Return Position at midpoint between this Position and p

```csharp
public abstract Position2D MidPoint( Position2D p );
```

**Parameters**

- **p** —

#### `MoveBy` Method (Direction2D, Double)

Move Position2D by offset in direction dir

```csharp
public abstract void MoveBy( Direction2D dir , double offset );
```

**Parameters**

- **dir** — 
- **offset** — 

#### `MoveBy` Method (Double, Double)

Move Position2D by given x,y values

```csharp
public abstract void MoveBy( double X , double Y );
```

**Parameters**

- **X** — 
- **Y** —

#### `Near` Method

Returns true if this position is near p within the given range

```csharp
public abstract bool Near( Position2D p , double range );
```

**Parameters**

- **p** — 
- **range** —

#### `Parse` Method

Return Position2D object derived from a string in PDMS format

```csharp
public abstract Position2D Parse( string str );
```

**Parameters**

- **str** —

#### `Position3D` Method

Return a point in 3D space, using the given Plane

```csharp
public abstract Position Position3D( Plane plane );
```

**Parameters**

- **plane** —

#### `Size` Method

Distance of this position from origin along direction dir

```csharp
public abstract double Size( Direction2D dir );
```

**Parameters**

- **dir** —

#### `ToString` Method

Returns Position2D property values in a string

```csharp
public abstract string ToString();
```

## Operators

#### `Equality` Operator

Same Position2D

```csharp
public static bool operator ==( Position2D t1 , Position2D t2 );
```

**Parameters**

- **t1** — 
- **t2** —

#### `Inequality` Operator

Not Same Position2D

```csharp
public static bool operator !=( Position2D t1 , Position2D t2 );
```

**Parameters**

- **t1** — 
- **t2** —
