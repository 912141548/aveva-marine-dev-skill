---
title: Aveva.Pdms.Maths.Geometry.D2IrregularPolarGrid Class
namespace: Aveva.Pdms.Maths.Geometry
assembly: Aveva.Pdms.Maths.Geometry
kind: Class
source: Aveva.Pdms.Maths.Geometry
---

# Aveva.Pdms.Maths.Geometry.D2IrregularPolarGrid Class

> Class definition of a an Irregular Polar Grid. An invalid grid will occur if any radii value is negative. If either the angular or radial vectors are empty a valid grid is defined, however, if both the angular and radial vectors are empty an invalid grid is defined.

## Syntax

```csharp
public abstract class D2IrregularPolarGrid
```

## Inheritance

`System.Object` → `Aveva.Pdms.Maths.Geometry.D2IrregularPolarGrid`

## Thread Safety

Public static ( Shared in Visual Basic) members of this type are
safe for multithreaded operations. Instance members are not guaranteed to be
thread-safe.

## Requirements

Namespace:
Aveva.Pdms.Maths.Geometry
Assembly: Aveva.Pdms.Maths.Geometry (in Aveva.Pdms.Maths.Geometry.dll)

## Methods

#### `Clone` Method

Returns a deep copy of the D2IrregularPolarGrid

```csharp
public abstract D2IrregularPolarGrid Clone();
```

#### `Create` Method ()

default constructor with empty grid

```csharp
public static D2IrregularPolarGrid Create();
```

#### `Create` Method (D2IrregularPolarGrid)

Copy grid

```csharp
public static D2IrregularPolarGrid Create( D2IrregularPolarGrid g );
```

**Parameters**

- **g** — 

#### `Create` Method (D3OrientedPlane, Double[], Double[])

Create a grid from given angles/spacings on given plane

```csharp
public static D2IrregularPolarGrid Create( D3OrientedPlane p , double[] radius , double[] angles );
```

**Parameters**

- **p** — 
- **radius** — 
- **angles** —

#### `Equals` Method (D2IrregularPolarGrid)

Test for equality

```csharp
public abstract bool Equals( D2IrregularPolarGrid g );
```

**Parameters**

- **g** — 

#### `Equals` Method (Object)

```csharp
public override bool Equals( object obj );
```

**Parameters**

- **obj** —

#### `GetAngles` Method

Returns an array of angular spacings of the grid

```csharp
public abstract double[] GetAngles();
```

#### `GetGridPoint` Method

Returns point at grid with angle index =i,radius index = j

```csharp
public abstract bool GetGridPoint( int i , int j , D2Point p );
```

**Parameters**

- **i** — 
- **j** — 
- **p** —

#### `GetHashCode` Method

```csharp
public override int GetHashCode();
```

#### `GetPlane` Method

Returns the plane of the grid

```csharp
public abstract D3OrientedPlane GetPlane();
```

#### `GetRadii` Method

Returns an array of radial spacings of the grid

```csharp
public abstract double[] GetRadii();
```

#### `GridValidity` Method

Returns false if grid has a negative or null spacing value

```csharp
public abstract bool GridValidity();
```

#### `LocateControlPoint` Method

Locates control point for use in snapping routines.

```csharp
public abstract void LocateControlPoint( D2Point p , ref int i , ref int j );
```

**Parameters**

- **p** — 
- **i** — 
- **j** —

#### `SetAngles` Method

Sets the angular spacings to values in given array

```csharp
public abstract void SetAngles( double[] angles );
```

**Parameters**

- **angles** —

#### `SetData` Method

Set the plans, radial and angular spacings of the grid

```csharp
public abstract void SetData( D3OrientedPlane plane , double[] radius , double[] angles );
```

**Parameters**

- **plane** — 
- **radius** — 
- **angles** —

#### `SetRadii` Method

Sets the radial spacings to values in given array

```csharp
public abstract void SetRadii( double[] radius );
```

**Parameters**

- **radius** —

#### `SnapToCentre` Method

Returns nearest centre point in grid to given point

```csharp
public abstract bool SnapToCentre( D2Point p , D2Point c );
```

**Parameters**

- **p** — 
- **c** —

#### `SnapToPoint` Method

Returns point on grid nearest to given point p

```csharp
public abstract bool SnapToPoint( D2Point p , D2Point ps );
```

**Parameters**

- **p** — 
- **ps** —

#### `ToString` Method

Returns a string describing the values of the D2IrregularPolarGrid

```csharp
public abstract string ToString();
```

## Operators

#### `Equality` Operator

invoked by left == right

```csharp
public static bool operator ==( D2IrregularPolarGrid left , D2IrregularPolarGrid right );
```

**Parameters**

- **left** — 
- **right** —

#### `Inequality` Operator

invoked by left != right

```csharp
public static bool operator !=( D2IrregularPolarGrid left , D2IrregularPolarGrid right );
```

**Parameters**

- **left** — 
- **right** —
