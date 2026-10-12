---
title: Aveva.Pdms.Geometry.Position Class
namespace: Aveva.Pdms.Geometry
assembly: Aveva.Pdms.Geometry
kind: Class
source: Aveva.Pdms.Geometry
---

# Aveva.Pdms.Geometry.Position Class

> Summary description for D3Point.

## Syntax

```csharp
public abstract class Position
```

## Inheritance

`System.Object` → `Aveva.Pdms.Geometry.Position`

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

X cooridnate

```csharp
public abstract double X {get; set;}
```

#### `Y` Property

Y Coordinate

```csharp
public abstract double Y {get; set;}
```

#### `Z` Property

Z cooridnate

```csharp
public abstract double Z {get; set;}
```

## Methods

#### `Angle` Method

Return the angle between p1 and p2 about this Position

```csharp
public abstract double Angle( Position p1 , Position p2 );
```

**Parameters**

- **p1** — 
- **p2** —

#### `Create` Method ()

Creates a Position at (0,0,0)

```csharp
public static Position Create();
```

#### `Create` Method (Double, Double, Double)

Creates a Position at coordinates (x,y,z)

```csharp
public static Position Create( double x , double y , double z );
```

**Parameters**

- **x** — 
- **y** — 
- **z** — 

#### `Create` Method (String)

```csharp
public static Position Create( string postring );
```

#### `Distance` Method (Line)

Distance to the nearest point on the (infinitely extended) Line line

```csharp
public abstract double Distance( Line line );
```

**Parameters**

- **line** — 

#### `Distance` Method (Plane)

Distance to the nearest point on the Plane plane

```csharp
public abstract double Distance( Plane plane );
```

**Parameters**

- **plane** — 

#### `Distance` Method (Position)

Distance from Position p

```csharp
public abstract double Distance( Position p );
```

**Parameters**

- **p** —

#### `Equals` Method (Position)

Same Position, within tolerance

```csharp
public abstract bool Equals( Position p );
```

**Parameters**

- **p** — 

#### `Equals` Method (Object)

Same Position, within tolerance

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

Return Position at midpoint between this Position and

```csharp
public abstract Position MidPoint( Position p );
```

**Parameters**

- **p** —

#### `MoveBy` Method (Direction, Double)

Offset by val in direction dir

```csharp
public abstract void MoveBy( Direction dir , double val );
```

**Parameters**

- **dir** — 
- **val** — 

#### `MoveBy` Method (Double, Double, Double)

Offset by given amount

```csharp
public abstract void MoveBy( double x , double y , double z );
```

**Parameters**

- **x** — 
- **y** — 
- **z** —

#### `Parse` Method

Return Position object derived from a string in PDMS format

```csharp
public abstract Position Parse( string str );
```

**Parameters**

- **str** —

#### `Position2D` Method ()

Return 2d position calculated from the X,Y values of the Position object

```csharp
public abstract Position2D Position2D();
```

#### `Position2D` Method (Plane)

Return the 2D position which is the position projected onto Plane plane

```csharp
public abstract Position2D Position2D( Plane plane );
```

**Parameters**

- **plane** —

## Operators

#### `Equality` Operator

Same Position, within tolerance

```csharp
public static bool operator ==( Position p1 , Position p2 );
```

**Parameters**

- **p1** — 
- **p2** —

#### `Inequality` Operator

Not same Position

```csharp
public static bool operator !=( Position p1 , Position p2 );
```

**Parameters**

- **p1** — 
- **p2** —
