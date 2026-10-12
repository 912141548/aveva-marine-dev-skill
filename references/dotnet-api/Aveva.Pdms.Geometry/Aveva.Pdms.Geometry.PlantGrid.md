---
title: Aveva.Pdms.Geometry.PlantGrid Class
namespace: Aveva.Pdms.Geometry
assembly: Aveva.Pdms.Geometry
kind: Class
source: Aveva.Pdms.Geometry
---

# Aveva.Pdms.Geometry.PlantGrid Class

> Summary description for PlantGrid.

## Syntax

```csharp
public abstract class PlantGrid
```

## Inheritance

`System.Object` → `Aveva.Pdms.Geometry.PlantGrid`

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

Spacings between grid lines in X direction

```csharp
public abstract double[] XSpacing {get; set;}
```

#### `YSpacing` Property

Spacings between lines in Y direction

```csharp
public abstract double[] YSpacing {get; set;}
```

## Methods

#### `Create` Method ()

Create PlantGrid

```csharp
public static PlantGrid Create();
```

#### `Create` Method (Position, Orientation, Double[], Double[])

Create PlantGrid

```csharp
public static PlantGrid Create( Position pos , Orientation ori , double[] xspacings , double[] yspacings );
```

**Parameters**

- **pos** — 
- **ori** — 
- **xspacings** — 
- **yspacings** —

#### `Equals` Method (PlantGrid)

same PlantGrid

```csharp
public abstract bool Equals( PlantGrid pg );
```

**Parameters**

- **pg** — 

#### `Equals` Method (Object)

Same PlantGrid

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

Returns the position at the (ix,iy) intersection of the grid. If ix or iy are negative, refers to intersections before the origin..

```csharp
public abstract Position GridPoint( int ix , int iy );
```

**Parameters**

- **ix** — 
- **iy** —

#### `internalCreate` Method ()

create PlantGrid

```csharp
public abstract PlantGrid internalCreate();
```

#### `internalCreate` Method (Position, Orientation, Double[], Double[])

create PlantGrid

```csharp
public abstract PlantGrid internalCreate( Position pos , Orientation ori , double[] xspacings , double[] yspacings );
```

**Parameters**

- **pos** — 
- **ori** — 
- **xspacings** — 
- **yspacings** —

#### `IsInGridBounds` Method

Returns true if pos is within the grid

```csharp
public abstract bool IsInGridBounds( Position pos );
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

Returns PlantGrid property values in a string

```csharp
public abstract string ToString();
```

#### `XSize` Method

Maximum size in the X direction

```csharp
public abstract double XSize();
```

#### `YSize` Method

Maximum size in the Y direction

```csharp
public abstract double YSize();
```

## Operators

#### `Equality` Operator

Same PlantGrid

```csharp
public static bool operator ==( PlantGrid pg1 , PlantGrid pg2 );
```

**Parameters**

- **pg1** — 
- **pg2** —

#### `Inequality` Operator

Not same PlantGrid

```csharp
public static bool operator !=( PlantGrid pg1 , PlantGrid pg2 );
```

**Parameters**

- **pg1** — 
- **pg2** —
