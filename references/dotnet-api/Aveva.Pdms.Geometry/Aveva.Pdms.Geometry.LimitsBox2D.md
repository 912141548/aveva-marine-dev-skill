---
title: Aveva.Pdms.Geometry.LimitsBox2D Class
namespace: Aveva.Pdms.Geometry
assembly: Aveva.Pdms.Geometry
kind: Class
source: Aveva.Pdms.Geometry
---

# Aveva.Pdms.Geometry.LimitsBox2D Class

> Summary description for LimitsBox2D.

## Syntax

```csharp
public abstract class LimitsBox2D
```

## Inheritance

`System.Object` → `Aveva.Pdms.Geometry.LimitsBox2D`

## Thread Safety

Public static ( Shared in Visual Basic) members of this type are
safe for multithreaded operations. Instance members are not guaranteed to be
thread-safe.

## Requirements

Namespace:
Aveva.Pdms.Geometry
Assembly: Aveva.Pdms.Geometry (in Aveva.Pdms.Geometry.dll)

## Properties

#### `Maximum` Property

Maximum corner of the LimitsBox2D

```csharp
public abstract Position2D Maximum {get; set;}
```

#### `Minimum` Property

Minimum corner of the LimitsBox2D

```csharp
public abstract Position2D Minimum {get; set;}
```

## Methods

#### `Area` Method

Returns the area inside the LimitsBox2D

```csharp
public abstract double Area();
```

#### `Centre` Method

Return centre point of LimitsBox2D

```csharp
public abstract Position2D Centre();
```

#### `Contains` Method

Returns true if box is entirely contained within this LimitsBox2D

```csharp
public abstract bool Contains( LimitsBox2D box );
```

**Parameters**

- **box** —

#### `ContainsPoint` Method

Returns true if pos is inside (not on) LimitsBox2D

```csharp
public abstract bool ContainsPoint( Position2D pos );
```

**Parameters**

- **pos** —

#### `Create` Method ()

Create LimitsBox2D

```csharp
public static LimitsBox2D Create();
```

#### `Create` Method (Position2D, Position2D)

Create a LimitsBox2D with min and max corners specified by p1 and p2

```csharp
public static LimitsBox2D Create( Position2D p1 , Position2D p2 );
```

**Parameters**

- **p1** — 
- **p2** —

#### `Equals` Method (LimitsBox2D)

Same LimitsBox2D, within tolerance

```csharp
public abstract bool Equals( LimitsBox2D limit );
```

**Parameters**

- **limit** — 

#### `Equals` Method (Object)

Same LimitsBox2D, within tolerance

```csharp
public override bool Equals( object obj );
```

**Parameters**

- **obj** —

#### `ExpandBy` Method

Expand LimitsBox by val in X and Y direction about centre

```csharp
public abstract void ExpandBy( double val );
```

**Parameters**

- **val** —

#### `ExpandToInclude` Method

Expand LimitsBox to include pos

```csharp
public abstract void ExpandToInclude( Position2D pos );
```

**Parameters**

- **pos** —

#### `GetHashCode` Method

A hash method is used to quickly generate a hash code, which is an int that corresponds to the value of an object. Hash codes allow C# to store objects more efficiently in collections

```csharp
public override int GetHashCode();
```

#### `Intersection` Method

Returns LimitsBox2D which consists of the overlap of the two LimitsBoxes

```csharp
public abstract LimitsBox2D Intersection( LimitsBox2D box );
```

**Parameters**

- **box** —

#### `Intersects` Method

Returns true if limits boxes intersect

```csharp
public abstract bool Intersects( LimitsBox2D box );
```

**Parameters**

- **box** —

#### `Merge` Method

Return LimitsBox2D that is the combination ot the 2 LimitsBoxes

```csharp
public abstract LimitsBox2D Merge( LimitsBox2D box );
```

**Parameters**

- **box** —

#### `ToString` Method

Returns LimitsBox2D property values in a string

```csharp
public abstract string ToString();
```

## Operators

#### `Equality` Operator

Same LimitsBox2D within tolerance

```csharp
public static bool operator ==( LimitsBox2D t1 , LimitsBox2D t2 );
```

**Parameters**

- **t1** — 
- **t2** —

#### `Inequality` Operator

Not same LimitsBox2D

```csharp
public static bool operator !=( LimitsBox2D t1 , LimitsBox2D t2 );
```

**Parameters**

- **t1** — 
- **t2** —
