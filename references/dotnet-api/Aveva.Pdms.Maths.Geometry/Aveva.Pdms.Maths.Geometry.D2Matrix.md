---
title: Aveva.Pdms.Maths.Geometry.D2Matrix Class
namespace: Aveva.Pdms.Maths.Geometry
assembly: Aveva.Pdms.Maths.Geometry
kind: Class
source: Aveva.Pdms.Maths.Geometry
---

# Aveva.Pdms.Maths.Geometry.D2Matrix Class

> 2x2 matrix This matrix class can represent a 2x2 matrix of douuble precision quantities. The elements are indexed from (zero,zero).

## Syntax

```csharp
public abstract class D2Matrix
```

## Inheritance

`System.Object` → `Aveva.Pdms.Maths.Geometry.D2Matrix`

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

Add two matrices

```csharp
public abstract D2Matrix Add( D2Matrix m2 );
```

**Parameters**

- **m2** —

#### `AsArray4` Method

return matrix as a vector

```csharp
public abstract double[] AsArray4();
```

#### `BeIdentity` Method

clear matrix to be an identity matrix.

```csharp
public abstract void BeIdentity();
```

#### `BeZero` Method

clear to zeros

```csharp
public abstract void BeZero();
```

#### `Clone` Method

deep copy

```csharp
public abstract D2Matrix Clone();
```

#### `Create` Method ()

Default Constructor

```csharp
public static D2Matrix Create();
```

#### `Create` Method (D2Matrix)

Copy D2Matrix

```csharp
public static D2Matrix Create( D2Matrix matrix );
```

**Parameters**

- **matrix** — 

#### `Create` Method (Double)

Construct a diagonal matrix with value diag along diagonal

```csharp
public static D2Matrix Create( double diag );
```

**Parameters**

- **diag** — 

#### `Create` Method (Double[])

Construct a 4x4 matrix with given values (by row)

```csharp
public static D2Matrix Create( double[] v );
```

**Parameters**

- **v** —

#### `Determinant` Method

Returns the determinate of the matrix

```csharp
public abstract double Determinant();
```

#### `Divide` Method

Divide matrix by scalar value

```csharp
public abstract D2Matrix Divide( double scalar );
```

**Parameters**

- **scalar** —

#### `Equals` Method (D2Matrix)

Returns true if matrix values are within fl_TOLERANCE of each othe

```csharp
public abstract bool Equals( D2Matrix matrix );
```

**Parameters**

- **matrix** — 

#### `Equals` Method (D2Matrix, Double)

Returns true if matrix values are within delta of each other

```csharp
public abstract bool Equals( D2Matrix matrix , double delta );
```

**Parameters**

- **matrix** — 
- **delta** — 

#### `Equals` Method (Object)

override test for equality

```csharp
public override bool Equals( object a );
```

**Parameters**

- **a** —

#### `Get` Method

return matrix element. (N.B i and j are 0 or 1)

```csharp
public abstract double Get( int i , int j );
```

**Parameters**

- **i** — 
- **j** —

#### `GetHashCode` Method

required override of GetHashCode() when we define operator ==

```csharp
public override int GetHashCode();
```

**Return Value**

int

#### `GetInverse` Method

true for non-singular matrices Inverse matrix returned through in result.

```csharp
public abstract bool GetInverse( D2Matrix result );
```

**Parameters**

- **result** —

#### `Inverse` Method

return inverse matrix - returns null matrix if the original matrix is singular

```csharp
public abstract D2Matrix Inverse();
```

#### `Invert` Method

invert matrix if non-singular (return false otherwise)

```csharp
public abstract bool Invert();
```

#### `IsIdentity` Method

True if matrix is identity matrix

```csharp
public abstract bool IsIdentity();
```

#### `IsOrthogonal` Method

True if matrix is orthogonal (within tolerance)

```csharp
public abstract bool IsOrthogonal( double tol );
```

**Parameters**

- **tol** —

#### `IsSingular` Method

True for singular matrices Result predicts failure of getInverse() inverse() and invert()

```csharp
public abstract bool IsSingular();
```

#### `Multiply` Method (D2Matrix)

Multiply matrix by another

```csharp
public abstract D2Matrix Multiply( D2Matrix m2 );
```

**Parameters**

- **m2** — 

#### `Multiply` Method (D2Vector)

Multiply matrix by a vector

```csharp
public abstract D2Vector Multiply( D2Vector v2 );
```

**Parameters**

- **v2** — 

#### `Multiply` Method (Double)

Multiply elements of matrix by scalar value

```csharp
public abstract D2Matrix Multiply( double scalar );
```

**Parameters**

- **scalar** —

#### `RotateByDegrees` Method

rotate matrix by given angle in degrees

```csharp
public abstract void RotateByDegrees( double degrees );
```

**Parameters**

- **degrees** —

#### `RotateByRadians` Method

rotate matrix by given angle in radians

```csharp
public abstract void RotateByRadians( double radians );
```

**Parameters**

- **radians** —

#### `SetValue` Method

Set value of element (i,j)

```csharp
public abstract void SetValue( int i , int j , double x );
```

**Parameters**

- **i** — 
- **j** — 
- **x** —

#### `SetValues` Method

Set value of matrix elements to values in vesctor (row order)

```csharp
public abstract void SetValues( double[] v );
```

**Parameters**

- **v** —

#### `Subtract` Method

Subtract matrix from this one

```csharp
public abstract D2Matrix Subtract( D2Matrix m2 );
```

**Parameters**

- **m2** —

#### `ToString` Method

Returns string containing details of the matrix

```csharp
public abstract string ToString();
```

#### `Transpose` Method

Return transpose of matrix

```csharp
public abstract D2Matrix Transpose();
```

## Operators

#### `Addition` Operator

invoked by m1+m2 - add corresponding elements.

```csharp
public static D2Matrix operator +( D2Matrix m1 , D2Matrix m2 );
```

**Parameters**

- **m1** — 
- **m2** —

#### `Division` Operator

invoked by m1/scalar - divide each element by a scalar

```csharp
public static D2Matrix operator /( D2Matrix m1 , double scalar );
```

**Parameters**

- **m1** — 
- **scalar** —

#### `Equality` Operator

The equality operator. It returns true if all the components are exactly equal (it does not use a tolerance).

```csharp
public static bool operator ==( D2Matrix left , D2Matrix right );
```

**Parameters**

- **left** — 
- **right** —

#### `Inequality` Operator

The inequality operator. It returns true if NOT all the components are exactly equal (it does not use a tolerance).

```csharp
public static bool operator !=( D2Matrix left , D2Matrix right );
```

**Parameters**

- **left** — 
- **right** —

#### `Multiplication` Operator (D2Matrix, D2Matrix)

invoked by m1 * m2 - Matrix multiplication

```csharp
public static D2Matrix operator *( D2Matrix m1 , D2Matrix m2 );
```

**Parameters**

- **m1** — 
- **m2** — 

#### `Multiplication` Operator (D2Matrix, Double)

invoked by scalar * m1 - multiply each element by the scalar

```csharp
public static D2Matrix operator *( D2Matrix m1 , double scalar );
```

**Parameters**

- **m1** — 
- **scalar** —

#### `Subtraction` Operator

invoked by m1-m2 - subtract corresponding element.

```csharp
public static D2Matrix operator -( D2Matrix m1 , D2Matrix m2 );
```

**Parameters**

- **m1** — 
- **m2** —
