---
title: Aveva.Pdms.Maths.Geometry.D3Matrix Class
namespace: Aveva.Pdms.Maths.Geometry
assembly: Aveva.Pdms.Maths.Geometry
kind: Class
source: Aveva.Pdms.Maths.Geometry
---

# Aveva.Pdms.Maths.Geometry.D3Matrix Class

> 3x3 matrix This matrix class can represent a 3x3 matrix of double recision quantities. The elements are indexed from (zero,zero,zero).

## Syntax

```csharp
public abstract class D3Matrix
```

## Inheritance

`System.Object` → `Aveva.Pdms.Maths.Geometry.D3Matrix`

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

Add given matrix to this

```csharp
public abstract D3Matrix Add( D3Matrix m2 );
```

**Parameters**

- **m2** —

#### `AsArray9` Method

Return the 9 values of the matrix in an array

```csharp
public abstract double[] AsArray9();
```

#### `BeIdentity` Method

Set matrix to identity matrix

```csharp
public abstract void BeIdentity();
```

#### `BeZero` Method

Clear matrix to all zeros

```csharp
public abstract void BeZero();
```

#### `Clone` Method

Return a deep copy

```csharp
public abstract D3Matrix Clone();
```

#### `Create` Method ()

Default constructor

```csharp
public static D3Matrix Create();
```

#### `Create` Method (D3Matrix)

Copy constructor

```csharp
public static D3Matrix Create( D3Matrix matrix );
```

**Parameters**

- **matrix** — 

#### `Create` Method (Double)

Construct a matrix with all zeros, and value diag on the diagonal

```csharp
public static D3Matrix Create( double diag );
```

**Parameters**

- **diag** — 

#### `Create` Method (Double[])

Constrcu matricx from given array of values (by row)

```csharp
public static D3Matrix Create( double[] v );
```

**Parameters**

- **v** —

#### `Determinant` Method

Returns the determinant of the matrix

```csharp
public abstract double Determinant();
```

#### `Divide` Method

Divide matrix values by scalar

```csharp
public abstract D3Matrix Divide( double scalar );
```

**Parameters**

- **scalar** —

#### `Equals` Method (D3Matrix)

Test for equality

```csharp
public abstract bool Equals( D3Matrix d2 );
```

**Parameters**

- **d2** — 

#### `Equals` Method (Object)

```csharp
public override bool Equals( object obj );
```

**Parameters**

- **obj** —

#### `GetHashCode` Method

```csharp
public override int GetHashCode();
```

#### `GetInverse` Method

Returns true if the matrix has an inverse, and the inverse of the matrix as an argument

```csharp
public abstract bool GetInverse( D3Matrix result );
```

**Parameters**

- **result** —

#### `GetValue` Method

Return the value at row i, column j. Args validity checked

```csharp
public abstract double GetValue( int i , int j );
```

**Parameters**

- **i** — 
- **j** —

#### `Inverse` Method

Return the inverse of the matrix

```csharp
public abstract D3Matrix Inverse();
```

#### `Invert` Method

Invert the matrix

```csharp
public abstract bool Invert();
```

#### `IsIdentity` Method

Returns true if the matrix is identity matrix

```csharp
public abstract bool IsIdentity();
```

#### `IsOrthogonal` Method

Returns true if the matrix is orthogonal, within tolerance tol

```csharp
public abstract bool IsOrthogonal( double tol );
```

**Parameters**

- **tol** —

#### `IsSingular` Method

Returns true if the matrix is singular. Result predicts failure of getInverse()/inverse()/invert()

```csharp
public abstract bool IsSingular();
```

#### `Multiply` Method (D3Matrix)

Multuiply matrix by given matrix

```csharp
public abstract D3Matrix Multiply( D3Matrix m2 );
```

**Parameters**

- **m2** — 

#### `Multiply` Method (D3Vector)

Multiply vector by matrix

```csharp
public abstract D3Vector Multiply( D3Vector v2 );
```

**Parameters**

- **v2** — 

#### `Multiply` Method (Double)

Multiply matrix values by scalar value

```csharp
public abstract D3Matrix Multiply( double scalar );
```

**Parameters**

- **scalar** —

#### `RotateBy` Method

Rotate the matrix by degX about X, degY about Y, degZ about Z

```csharp
public abstract void RotateBy( double degX , double degY , double degZ );
```

**Parameters**

- **degX** — 
- **degY** — 
- **degZ** —

#### `RotateX` Method

Rotate the matrix by degrees about X

```csharp
public abstract void RotateX( double degrees );
```

**Parameters**

- **degrees** —

#### `RotateY` Method

Rotate the matrix by degrees about Y

```csharp
public abstract void RotateY( double degrees );
```

**Parameters**

- **degrees** —

#### `RotateZ` Method

Rotate the matrix by degrees about Z

```csharp
public abstract void RotateZ( double degrees );
```

**Parameters**

- **degrees** —

#### `SetValue` Method (Double[])

Set values into matrix (by row)

```csharp
public abstract void SetValue( double[] v );
```

**Parameters**

- **v** — 

#### `SetValue` Method (Int32, Int32, Double)

Set value of element at row i column j to be x

```csharp
public abstract void SetValue( int i , int j , double x );
```

**Parameters**

- **i** — 
- **j** — 
- **x** —

#### `Subtract` Method

Subtract given matrix from this

```csharp
public abstract D3Matrix Subtract( D3Matrix m2 );
```

**Parameters**

- **m2** —

#### `ToOrientationString` Method

```csharp
public abstract string ToOrientationString();
```

#### `ToString` Method

Returns string containing details of the matrix

```csharp
public abstract string ToString();
```

#### `Transpose` Method

Return the transpose of the matrix

```csharp
public abstract D3Matrix Transpose();
```

## Operators

#### `Addition` Operator

invoked by m1+m2

```csharp
public static D3Matrix operator +( D3Matrix m1 , D3Matrix m2 );
```

**Parameters**

- **m1** — 
- **m2** —

#### `Division` Operator

invoked by m1/scalar

```csharp
public static D3Matrix operator /( D3Matrix m1 , double scalar );
```

**Parameters**

- **m1** — 
- **scalar** —

#### `Equality` Operator

invoked by left == right

```csharp
public static bool operator ==( D3Matrix left , D3Matrix right );
```

**Parameters**

- **left** — 
- **right** —

#### `Inequality` Operator

invoked by left != right

```csharp
public static bool operator !=( D3Matrix left , D3Matrix right );
```

**Parameters**

- **left** — 
- **right** —

#### `Multiplication` Operator

invoked by m1 * m2

```csharp
public static D3Matrix operator *( D3Matrix m1 , D3Matrix m2 );
```

**Parameters**

- **m1** — 
- **m2** —

#### `Subtraction` Operator

invoked by m1-m2

```csharp
public static D3Matrix operator -( D3Matrix m1 , D3Matrix m2 );
```

**Parameters**

- **m1** — 
- **m2** —
