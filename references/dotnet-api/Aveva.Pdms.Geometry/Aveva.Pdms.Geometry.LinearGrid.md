---
title: Aveva.Pdms.Geometry.LinearGrid Class
namespace: Aveva.Pdms.Geometry
assembly: Aveva.Pdms.Geometry
kind: Class
source: Aveva.Pdms.Geometry
---

# Aveva.Pdms.Geometry.LinearGrid Class

> Summary description for PlantGrid.

## Syntax

```csharp
public abstract class LinearGrid
```

## Inheritance

`System.Object` → `Aveva.Pdms.Geometry.LinearGrid`

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

Orientation of the grid

```csharp
public abstract Orientation Orientation {get; set;}
```

#### `Position` Property

Origin of the grid

```csharp
public abstract Position Position {get; set;}
```

#### `XSpacing` Property

Spacing between grid lines in X direction

```csharp
public abstract double XSpacing {get; set;}
```

#### `YSpacing` Property

Spacing between lines in Y direction

```csharp
public abstract double YSpacing {get; set;}
```

## Methods

#### `Create` Method ()

Create LinearGrid (Unset)

```csharp
public static LinearGrid Create();
```

#### `Create` Method (Position, Orientation, Double, Double)

Create a LinearGrid

```csharp
public static LinearGrid Create( Position pos , Orientation ori , double xspacing , double yspacing );
```

**Parameters**

- **pos** — 
- **ori** — 
- **xspacing** — 
- **yspacing** —

#### `Equals` Method (LinearGrid)

Same LinearGrid

```csharp
public abstract bool Equals( LinearGrid lg );
```

**Parameters**

- **lg** — 

#### `Equals` Method (Object)

Same LinearGrid

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

#### `GridPoint` Method

Returns the position at the (ix,iy) intersection of the grid. If ix or iy are negative, refers to intersections before the origin.

```csharp
public abstract Position GridPoint( int ix , int iy );
```

**Parameters**

- **ix** — 
- **iy** —

#### `internalCreate` Method ()

Create LinearGrid (Unset)

```csharp
public abstract LinearGrid internalCreate();
```

#### `internalCreate` Method (Position, Orientation, Double, Double)

Create a LinearGrid

```csharp
public abstract LinearGrid internalCreate( Position pos , Orientation ori , double xspacing , double yspacing );
```

**Parameters**

- **pos** — 
- **ori** — 
- **xspacing** — 
- **yspacing** —

#### `Offset2D` Method

Return the 2D position mapped onto the grid plane in terms of an XY offset from the grid plane origin

```csharp
public abstract Position2D Offset2D( Position pos );
```

**Parameters**

- **pos** —

#### `Plane` Method

Return Plane of the grid

```csharp
public abstract Plane Plane();
```

#### `Snap` Method (Line)

Returns nearest grid intersection point to the intersection of line with the plane of the grid

```csharp
public abstract Position Snap( Line line );
```

**Parameters**

- **line** — 

#### `Snap` Method (Position)

Returns nearest grid intersection point to pos

```csharp
public abstract Position Snap( Position pos );
```

**Parameters**

- **pos** —

#### `SnapToCentre` Method (Line)

Return the nearest mesh cell centre point to to the intersection of line with the plane of the grid

```csharp
public abstract Position SnapToCentre( Line line );
```

**Parameters**

- **line** — 

#### `SnapToCentre` Method (Position)

Return the nearest mesh cell centre point to pos in the grid plane

```csharp
public abstract Position SnapToCentre( Position pos );
```

**Parameters**

- **pos** —

#### `ToString` Method

Returns LinearGrid property values in a string

```csharp
public abstract string ToString();
```

## Operators

#### `Equality` Operator

Same LinearGrid

```csharp
public static bool operator ==( LinearGrid lg1 , LinearGrid lg2 );
```

**Parameters**

- **lg1** — 
- **lg2** —

#### `Inequality` Operator

Not Same LinearGrid

```csharp
public static bool operator !=( LinearGrid lg1 , LinearGrid lg2 );
```

**Parameters**

- **lg1** — 
- **lg2** —
