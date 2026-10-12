---
title: Aveva.Pdms.Geometry.Orientation Class
namespace: Aveva.Pdms.Geometry
assembly: Aveva.Pdms.Geometry
kind: Class
source: Aveva.Pdms.Geometry
---

# Aveva.Pdms.Geometry.Orientation Class

> Summary description for Orientation.

## Syntax

```csharp
public abstract class Orientation
```

## Inheritance

`System.Object` → `Aveva.Pdms.Geometry.Orientation`

## Thread Safety

Public static ( Shared in Visual Basic) members of this type are
safe for multithreaded operations. Instance members are not guaranteed to be
thread-safe.

## Requirements

Namespace:
Aveva.Pdms.Geometry
Assembly: Aveva.Pdms.Geometry (in Aveva.Pdms.Geometry.dll)

## Properties

#### `AboutX` Property

Rotation angle about X

```csharp
public abstract double AboutX {get;}
```

#### `AboutY` Property

Rotation angle about Y

```csharp
public abstract double AboutY {get;}
```

#### `AboutZ` Property

Rotation angle about Z

```csharp
public abstract double AboutZ {get;}
```

## Methods

#### `Absolute` Method

Return absolute orientation from local Orientation ori.

```csharp
public abstract Orientation Absolute( Orientation ori );
```

**Parameters**

- **ori** —

#### `AbsoluteDirection` Method

Return absolute Direction from local Direction dir.

```csharp
public abstract Direction AbsoluteDirection( Direction dir );
```

**Parameters**

- **dir** —

#### `AbsolutePosition` Method

Return absolute Position from local Position pos

```csharp
public abstract Position AbsolutePosition( Position pos );
```

**Parameters**

- **pos** —

#### `Create` Method ()

Create a default Orientation

```csharp
public static Orientation Create();
```

#### `Create` Method (Direction, Direction)

Create an Orientation

```csharp
public static Orientation Create( Direction xDir , Direction yDir );
```

**Parameters**

- **xDir** — 
- **yDir** — 

#### `Create` Method (String)

```csharp
public static Orientation Create( string oristring );
```

#### `Equals` Method (Orientation)

Same Orientation

```csharp
public abstract bool Equals( Orientation orientation );
```

**Parameters**

- **orientation** — 

#### `Equals` Method (Object)

Same Orientation

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

#### `Local` Method

Return local Orientation from absolute Orientation ori

```csharp
public abstract Orientation Local( Orientation ori );
```

**Parameters**

- **ori** —

#### `LocalDirection` Method

Return local Direction from absolute Direction dir

```csharp
public abstract Direction LocalDirection( Direction dir );
```

**Parameters**

- **dir** —

#### `LocalPosition` Method

Return local Position from absolute Position pos

```csharp
public abstract Position LocalPosition( Position pos );
```

**Parameters**

- **pos** —

#### `Rotate` Method (Axis, Double)

Rotate the orientation by degrees about global Axis axis

```csharp
public abstract void Rotate( Axis axis , double degrees );
```

**Parameters**

- **axis** — 
- **degrees** — 

#### `Rotate` Method (Direction, Double)

Rotate the orientation by degrees about global Direction dir

```csharp
public abstract void Rotate( Direction dir , double degrees );
```

**Parameters**

- **dir** — 
- **degrees** —

#### `RotateLocal` Method (Axis, Double)

Rotate the orientation by degrees about local Axis axis

```csharp
public abstract void RotateLocal( Axis axis , double degrees );
```

**Parameters**

- **axis** — 
- **degrees** — 

#### `RotateLocal` Method (Direction, Direction, Direction)

Rotate around local Direction ldir1 so that local Direction ldir2 is as close as possible to absolute Direction adir. Return the angle of rotation

```csharp
public abstract double RotateLocal( Direction ldir1 , Direction ldir2 , Direction adir );
```

**Parameters**

- **ldir1** — 
- **ldir2** — 
- **adir** — 

#### `RotateLocal` Method (Direction, Double)

Rotate the orientation by degrees about local Direction dir

```csharp
public abstract void RotateLocal( Direction dir , double degrees );
```

**Parameters**

- **dir** — 
- **degrees** —

#### `RotateTo` Method

Rotate about axis1 so that axis2 points in given direction, and return the angle of rotation

```csharp
public abstract double RotateTo( Axis axis1 , Axis axis2 , Direction dir );
```

**Parameters**

- **axis1** — 
- **axis2** — 
- **dir** —

#### `ToString` Method

Returns Orientation in PDMS Format

```csharp
public abstract string ToString();
```

#### `XDir` Method

Returns the X component as a Direction

```csharp
public abstract Direction XDir();
```

#### `YDir` Method

Returns the Y component as a Direction

```csharp
public abstract Direction YDir();
```

#### `ZDir` Method

Returns the Z component as a Direction

```csharp
public abstract Direction ZDir();
```

## Operators

#### `Equality` Operator

Same Orientation

```csharp
public static bool operator ==( Orientation p1 , Orientation p2 );
```

**Parameters**

- **p1** — 
- **p2** —

#### `Inequality` Operator

Not Same Orientation

```csharp
public static bool operator !=( Orientation p1 , Orientation p2 );
```

**Parameters**

- **p1** — 
- **p2** —
