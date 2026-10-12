---
title: Aveva.Pdms.Maths.Geometry.D2DivideLine Class
namespace: Aveva.Pdms.Maths.Geometry
assembly: Aveva.Pdms.Maths.Geometry
kind: Class
source: Aveva.Pdms.Maths.Geometry
---

# Aveva.Pdms.Maths.Geometry.D2DivideLine Class

> A 2-D Line Class, With normal n and dist d, point x is: on the line if: n.x + d = 0 above the line if: n.x + d > 0 Alternative format is (a,b;c) - point (x,y) is above the line if: ax + by + c > 0 The normal (as stored internally) always has magnitude 1.

## Syntax

```csharp
public abstract class D2DivideLine
```

## Inheritance

`System.Object` → `Aveva.Pdms.Maths.Geometry.D2DivideLine`

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

deep copy

```csharp
public abstract D2DivideLine Clone();
```

#### `Create` Method ()

Default divide line

```csharp
public static D2DivideLine Create();
```

#### `Create` Method (D2DivideLine)

Copy constructor

```csharp
public static D2DivideLine Create( D2DivideLine line );
```

**Parameters**

- **line** — 

#### `Create` Method (D2Vector)

Construct from a vector through the origin

```csharp
public static D2DivideLine Create( D2Vector norm );
```

**Parameters**

- **norm** — 

#### `Create` Method (D2Vector, D2Point)

Construct from a vector and a point

```csharp
public static D2DivideLine Create( D2Vector norm , D2Point pt );
```

**Parameters**

- **norm** — 
- **pt** — 

#### `Create` Method (D2Vector, Double)

Construct from a vector and a distance from origin

```csharp
public static D2DivideLine Create( D2Vector norm , double d );
```

**Parameters**

- **norm** — 
- **d** —

#### `Ddistance` Method

Return distance form given point

```csharp
public abstract double Ddistance( D2Point pt );
```

**Parameters**

- **pt** —

#### `Equals` Method (D2DivideLine)

Test for equality

```csharp
public abstract bool Equals( D2DivideLine d2 );
```

**Parameters**

- **d2** — 

#### `Equals` Method (Object)

override equals method

```csharp
public override bool Equals( object o );
```

**Parameters**

- **o** —

#### `GetA` Method

Return x value of line

```csharp
public abstract double GetA();
```

#### `GetB` Method

Return Y value of line

```csharp
public abstract double GetB();
```

#### `GetC` Method

Return distance from the origin

```csharp
public abstract double GetC();
```

#### `GetHashCode` Method

override gethashcode

```csharp
public override int GetHashCode();
```

#### `GetNormal` Method

Return the unit vector normal to the line

```csharp
public abstract D2Vector GetNormal();
```

#### `GetOffset` Method

Return offset of the divided line

```csharp
public abstract double GetOffset();
```

#### `SetValue` Method (D2Vector)

Set the value of the normal to the plane

```csharp
public abstract void SetValue( D2Vector norm );
```

**Parameters**

- **norm** — 

#### `SetValue` Method (D2Vector, D2Point)

Set the normal and point on line

```csharp
public abstract void SetValue( D2Vector norm , D2Point pt );
```

**Parameters**

- **norm** — 
- **pt** — 

#### `SetValue` Method (D2Vector, Double)

Set the normal and the distance values

```csharp
public abstract void SetValue( D2Vector norm , double d );
```

**Parameters**

- **norm** — 
- **d** —

#### `Side` Method

Return which side of the line the point is: 1=above, 0=on, -1=below

```csharp
public abstract int Side( D2Point pt , double tol );
```

**Parameters**

- **pt** — 
- **tol** —

#### `ToString` Method

Returns a string describing the contents of the D2DivideLine

```csharp
public abstract string ToString();
```

## Operators

#### `Equality` Operator

True if left == right

```csharp
public static bool operator ==( D2DivideLine left , D2DivideLine right );
```

**Parameters**

- **left** — 
- **right** —

#### `Inequality` Operator

True if left != right

```csharp
public static bool operator !=( D2DivideLine left , D2DivideLine right );
```

**Parameters**

- **left** — 
- **right** —
