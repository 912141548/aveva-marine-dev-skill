---
title: Aveva.Pdms.Maths.Geometry.D2IrregularCartesianGrid Class
namespace: Aveva.Pdms.Maths.Geometry
assembly: Aveva.Pdms.Maths.Geometry
kind: Class
source: Aveva.Pdms.Maths.Geometry
---

# Aveva.Pdms.Maths.Geometry.D2IrregularCartesianGrid Class

> Class definition of a an Irregular Cartesian Grid. The members of this class are: 1) a mthOrientedPlane representing the origin and orientation of the grid, 2) a validity flag, 3) an array containing the x spacings for the grid definition, and 4) an array containing the y spacings for the grid definition. The x and y spacings must be non-zero and positive for this type of grid to be valid. Empty vectors will result in an invalid grid.

## Syntax

```csharp
public abstract class D2IrregularCartesianGrid
```

## Inheritance

`System.Object` → `Aveva.Pdms.Maths.Geometry.D2IrregularCartesianGrid`

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

Returns a deep copy of the D2IrregularCartesianGrid

```csharp
public abstract D2IrregularCartesianGrid Clone();
```

#### `Create` Method ()

Default constructor

```csharp
public static D2IrregularCartesianGrid Create();
```

#### `Create` Method (D2IrregularCartesianGrid)

Copy constructor

```csharp
public static D2IrregularCartesianGrid Create( D2IrregularCartesianGrid g );
```

**Parameters**

- **g** — 

#### `Create` Method (D3OrientedPlane, Double[], Double[])

Create from a grid on a D3oriented plane

```csharp
public static D2IrregularCartesianGrid Create( D3OrientedPlane p , double[] xs , double[] ys );
```

**Parameters**

- **p** — 
- **xs** — 
- **ys** —

#### `Equals` Method (D2IrregularCartesianGrid)

test for equality

```csharp
public abstract bool Equals( D2IrregularCartesianGrid g );
```

**Parameters**

- **g** — 

#### `Equals` Method (Object)

```csharp
public override bool Equals( object obj );
```

**Parameters**

- **obj** —

#### `GetGridPoint` Method

Returns point at grid intersection (i,j).

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

#### `GetXLimit` Method

returns the grid limit in x

```csharp
public abstract double GetXLimit();
```

#### `GetXSpacings` Method

Returns the array of x spacings

```csharp
public abstract double[] GetXSpacings();
```

#### `GetYLimit` Method

returns the grid limit in y

```csharp
public abstract double GetYLimit();
```

#### `GetYSpacings` Method

Returns the array of spacings in y

```csharp
public abstract double[] GetYSpacings();
```

#### `GridValidity` Method

Returns fales if if grid has a null or negative spacing value.

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

#### `SetData` Method

Set plane and x/y spacings

```csharp
public abstract void SetData( D3OrientedPlane plane , double[] xs , double[] ys );
```

#### `SetXSpacings` Method

Set an array of spacings in x

```csharp
public abstract void SetXSpacings( double[] x );
```

**Parameters**

- **x** —

#### `SetYSpacings` Method

Set an array of spacings in y

```csharp
public abstract void SetYSpacings( double[] y );
```

**Parameters**

- **y** —

#### `SnapToCentre` Method

Returns nearest grid centre point to given point p

```csharp
public abstract bool SnapToCentre( D2Point p , D2Point c );
```

**Parameters**

- **p** — 
- **c** —

#### `SnapToPoint` Method

Returns nearest grid point to given point p.

```csharp
public abstract bool SnapToPoint( D2Point p , D2Point ps );
```

**Parameters**

- **p** — 
- **ps** —

#### `ToString` Method

Returns a string describing the values of the D2IrregularCartesianGrid

```csharp
public abstract string ToString();
```

## Operators

#### `Equality` Operator

invoked by left == right

```csharp
public static bool operator ==( D2IrregularCartesianGrid left , D2IrregularCartesianGrid right );
```

**Parameters**

- **left** — 
- **right** —

#### `Inequality` Operator

invoked by left != right

```csharp
public static bool operator !=( D2IrregularCartesianGrid left , D2IrregularCartesianGrid right );
```

**Parameters**

- **left** — 
- **right** —
