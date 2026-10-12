---
title: Aveva.Pdms.Maths.Geometry.D2RegularCartesianGrid Class
namespace: Aveva.Pdms.Maths.Geometry
assembly: Aveva.Pdms.Maths.Geometry
kind: Class
source: Aveva.Pdms.Maths.Geometry
---

# Aveva.Pdms.Maths.Geometry.D2RegularCartesianGrid Class

> Class definition of a Regular Cartesian Grid. The x and y spacings must be non-zero and positive for this type of grid to be valid.

## Syntax

```csharp
public abstract class D2RegularCartesianGrid
```

## Inheritance

`System.Object` → `Aveva.Pdms.Maths.Geometry.D2RegularCartesianGrid`

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

Returns a deep copy of the D2RegularCartesianGrid

```csharp
public abstract D2RegularCartesianGrid Clone();
```

#### `Create` Method ()

Default constructor of an empty grid

```csharp
public static D2RegularCartesianGrid Create();
```

#### `Create` Method (D2RegularCartesianGrid)

Copy regular cartesian grid

```csharp
public static D2RegularCartesianGrid Create( D2RegularCartesianGrid g );
```

**Parameters**

- **g** — 

#### `Create` Method (D3OrientedPlane, Double, Double)

Construct an infinite grid from an oriented plane and x,y spacings

```csharp
public static D2RegularCartesianGrid Create( D3OrientedPlane plane , double x_spacing , double y_spacing );
```

**Parameters**

- **plane** — 
- **x_spacing** — 
- **y_spacing** —

#### `Equals` Method (D2RegularCartesianGrid)

check for equality

```csharp
public abstract bool Equals( D2RegularCartesianGrid g );
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

#### `GetXSpacing` Method

Returns the X spacing of the grid

```csharp
public abstract double GetXSpacing();
```

#### `GetYSpacing` Method

Returns the Y spacing of the grid

```csharp
public abstract double GetYSpacing();
```

#### `GridValidity` Method

Return true if grid is valid

```csharp
public abstract bool GridValidity();
```

#### `LocateControlPoint` Method

Locates control point for use in snapping routines

```csharp
public abstract void LocateControlPoint( D2Point p , ref int i , ref int j );
```

**Parameters**

- **p** — 
- **i** — 
- **j** —

#### `SetData` Method

Returns the plane of the grid, and the x/y spacings

```csharp
public abstract void SetData( D3OrientedPlane plane , double xs , double ys );
```

**Parameters**

- **plane** — 
- **xs** — 
- **ys** —

#### `SetXSpacing` Method

Set the X spacing of the grid to given value

```csharp
public abstract void SetXSpacing( double x );
```

**Parameters**

- **x** —

#### `SetYSpacing` Method

Set the y spacing of the grid to given value

```csharp
public abstract void SetYSpacing( double y );
```

**Parameters**

- **y** —

#### `SnapToCentre` Method

Returns centre of grid closest to given point

```csharp
public abstract bool SnapToCentre( D2Point p , D2Point c );
```

**Parameters**

- **p** — 
- **c** —

#### `SnapToPoint` Method

Returns point on grid closest to given point

```csharp
public abstract bool SnapToPoint( D2Point p , D2Point sp );
```

**Parameters**

- **p** — 
- **sp** —

#### `ToString` Method

Returns a string describing the values of the D2RegularCartesianGrid

```csharp
public abstract string ToString();
```

## Operators

#### `Equality` Operator

invoked by left == right

```csharp
public static bool operator ==( D2RegularCartesianGrid left , D2RegularCartesianGrid right );
```

**Parameters**

- **left** — 
- **right** —

#### `Inequality` Operator

invoked by left != right

```csharp
public static bool operator !=( D2RegularCartesianGrid left , D2RegularCartesianGrid right );
```

**Parameters**

- **left** — 
- **right** —
