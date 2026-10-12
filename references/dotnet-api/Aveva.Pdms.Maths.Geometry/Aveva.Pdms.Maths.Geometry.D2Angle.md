---
title: Aveva.Pdms.Maths.Geometry.D2Angle Class
namespace: Aveva.Pdms.Maths.Geometry
assembly: Aveva.Pdms.Maths.Geometry
kind: Class
source: Aveva.Pdms.Maths.Geometry
---

# Aveva.Pdms.Maths.Geometry.D2Angle Class

> Class definition for an angle An object of this class represents an angle. The angle can be specified either in radians or degrees, and it can be queried in either units (irrespective of the units that were used to specify it). The functions sin() cos() belonging to this class have the property that when the angle is close to some integer multiple of PI/2 radians (90 degrees), the result is EXACTLY 0.0 , 1.0 or -1.0 as appropriate. The tolerance used for the test can be specified, but otherwise defaults to 1.0e-6 radians. Some operators are also defined.

## Syntax

```csharp
public abstract class D2Angle
```

## Inheritance

`System.Object` → `Aveva.Pdms.Maths.Geometry.D2Angle`

## Thread Safety

Public static ( Shared in Visual Basic) members of this type are
safe for multithreaded operations. Instance members are not guaranteed to be
thread-safe.

## Requirements

Namespace:
Aveva.Pdms.Maths.Geometry
Assembly: Aveva.Pdms.Maths.Geometry (in Aveva.Pdms.Maths.Geometry.dll)

## Methods

#### `Add` Method

Add two angles

```csharp
public abstract D2Angle Add( D2Angle a2 );
```

#### `Clone` Method

Deep copy

```csharp
public abstract D2Angle Clone();
```

#### `Cos` Method ()

Return cosine of angle

```csharp
public abstract double Cos();
```

#### `Cos` Method (Double)

return cosine of angle. angles within delta of 0, PI/2, PI 3PI/2 2PI (or multiples thereof) will return exactly 1, 0, -1 0 1 respectively

```csharp
public abstract double Cos( double delta );
```

**Parameters**

- **delta** —

#### `Cosec` Method

Gets the tangent of the angle through the argument. If false is returned then the argument will contain DBL_MAX (defined in float.h); if true is returned the argument contains the cosecant of the angle.

```csharp
public abstract bool Cosec( ref double d );
```

**Parameters**

- **d** —

#### `Cotan` Method

Gets the cotangent of the angle through the argument. If false is returned then the argument will contain DBL_MAX (defined in float.h); if true is returned the argument contains the cotangent of the angle.

```csharp
public abstract bool Cotan( ref double d );
```

**Parameters**

- **d** —

#### `Create` Method ()

default angle

```csharp
public static D2Angle Create();
```

#### `Create` Method (D2Angle)

copy constructor

```csharp
public static D2Angle Create( D2Angle ang );
```

**Parameters**

- **ang** — 

#### `Create` Method (D2Angle, D2Angle, Double)

Construct an angle as a proportion: a = (1-prop)*a1 + prop*a2

```csharp
public static D2Angle Create( D2Angle a1 , D2Angle a2 , double prop );
```

**Parameters**

- **a1** — 
- **a2** — 
- **prop** — 

#### `Create` Method (D2Vector)

Construct an angle from a 2-d vector

```csharp
public static D2Angle Create( D2Vector vec );
```

**Parameters**

- **vec** — 

#### `Create` Method (Double)

Create from angle (in radians)

```csharp
public static D2Angle Create( double ang );
```

**Parameters**

- **ang** — 

#### `Create` Method (Double, angleUnits)

input D2Angle::rads if ang is in degrees input D2Angle::degs if ang is in degrees

```csharp
public static D2Angle Create( double ang , angleUnits units );
```

**Parameters**

- **ang** — 
- **units** —

#### `Degrees` Method ()

returns angle in degrees

```csharp
public abstract double Degrees();
```

#### `Degrees` Method (Double)

set angle given in degrees

```csharp
public abstract void Degrees( double ang );
```

#### `Equals` Method (D2Angle)

override system equals method

```csharp
public abstract bool Equals( D2Angle a );
```

**Parameters**

- **a** — 

#### `Equals` Method (D2Angle, Double)

true if angles same within tolerance delta, where delta is measured in RADIANS

```csharp
public abstract bool Equals( D2Angle a , double delta );
```

**Parameters**

- **a** — 
- **delta** — 

#### `Equals` Method (Object)

override system equals method

```csharp
public override bool Equals( object a );
```

**Parameters**

- **a** —

#### `GetHashCode` Method

override system gethashcode method

```csharp
public override int GetHashCode();
```

#### `Multiply` Method

Multiply angle by given value

```csharp
public abstract D2Angle Multiply( double s );
```

**Parameters**

- **s** —

#### `Normalize` Method

reset angle_ to be in range 0 - 2Pi

```csharp
public abstract void Normalize();
```

#### `NormDegrees` Method

return angle in the range [0,360]

```csharp
public abstract double NormDegrees();
```

#### `NormRadians` Method

return angle in the range [0,2Pi]

```csharp
public abstract double NormRadians();
```

#### `Radians` Method ()

returns angle in radians

```csharp
public abstract double Radians();
```

#### `Radians` Method (Double)

set angle given in radians

```csharp
public abstract void Radians( double ang );
```

#### `Sec` Method

Gets the secant of the angle through the argument. If false is returned then the argument will contain DBL_MAX (defined in float.h); if true is returned the argument contains the secant of the angle.

```csharp
public abstract bool Sec( ref double d );
```

**Parameters**

- **d** —

#### `Sin` Method ()

Return sine of angle

```csharp
public abstract double Sin();
```

#### `Sin` Method (Double)

return sine of angle. angles within delta of 0, PI/2, PI 3PI/2 2PI (or multiples thereof) will return exactly 0, 1, 0 -1 0 respectively

```csharp
public abstract double Sin( double delta );
```

**Parameters**

- **delta** —

#### `Subtract` Method

Subtract two angle

```csharp
public abstract D2Angle Subtract( D2Angle a2 );
```

**Parameters**

- **a2** —

#### `Tan` Method

Gets the tangent of the angle through the argument. If false is returned then the argument will contain DBL_MAX (defined in float.h); if true is returned the argument contains the tangent of the angle.

```csharp
public abstract bool Tan( ref double d );
```

**Parameters**

- **d** —

#### `ToString` Method

Returns a string describing the contents of the D2Angle

```csharp
public abstract string ToString();
```

## Operators

#### `Addition` Operator

invoked by a1 + a2

```csharp
public static D2Angle operator +( D2Angle a1 , D2Angle a2 );
```

**Parameters**

- **a1** — 
- **a2** —

#### `Equality` Operator

invoked by left == right - true if angles are exactly the same

```csharp
public static bool operator ==( D2Angle left , D2Angle right );
```

**Parameters**

- **left** — 
- **right** —

#### `Inequality` Operator

invoked by left != right - true if angles not exactly the same

```csharp
public static bool operator !=( D2Angle left , D2Angle right );
```

**Parameters**

- **left** — 
- **right** —

#### `Multiplication` Operator

invoked by s * a1

```csharp
public static D2Angle operator *( D2Angle a1 , double s );
```

**Parameters**

- **a1** — 
- **s** —

#### `Subtraction` Operator

invoked by a1 - a2

```csharp
public static D2Angle operator -( D2Angle a1 , D2Angle a2 );
```

**Parameters**

- **a1** — 
- **a2** —
