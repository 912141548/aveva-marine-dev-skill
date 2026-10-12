---
title: Aveva.Pdms.Geometry.PointVector Class
namespace: Aveva.Pdms.Geometry
assembly: Aveva.Pdms.Geometry
kind: Class
source: Aveva.Pdms.Geometry
---

# Aveva.Pdms.Geometry.PointVector Class

> Summary description for PointVector.

## Syntax

```csharp
public abstract class PointVector
```

## Inheritance

`System.Object` → `Aveva.Pdms.Geometry.PointVector`

## Thread Safety

Public static ( Shared in Visual Basic) members of this type are
safe for multithreaded operations. Instance members are not guaranteed to be
thread-safe.

## Requirements

Namespace:
Aveva.Pdms.Geometry
Assembly: Aveva.Pdms.Geometry (in Aveva.Pdms.Geometry.dll)

## Properties

#### `Direction` Property

Direction of PointVector

```csharp
public abstract Direction Direction {get; set;}
```

#### `Position` Property

Origin of PointVector

```csharp
public abstract Position Position {get; set;}
```

## Methods

#### `Create` Method ()

Default PointVector

```csharp
public static PointVector Create();
```

#### `Create` Method (Position, Direction)

Create a pointVector at pos with direction dir

```csharp
public static PointVector Create( Position pos , Direction dir );
```

**Parameters**

- **pos** — 
- **dir** —

#### `Equals` Method (PointVector)

Same PointVector

```csharp
public abstract bool Equals( PointVector pointvector );
```

**Parameters**

- **pointvector** — 

#### `Equals` Method (Object)

Same PointVector

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

#### `Line` Method

Returns an unbounded line from the origin and direction of the PointVector

```csharp
public abstract Line Line();
```

#### `Offset` Method

Offset the PointVector by val in its direction

```csharp
public abstract void Offset( double val );
```

#### `Plane` Method

Returns plane through the origin and with normal in the direction of the PointVector

```csharp
public abstract Plane Plane();
```

#### `ToString` Method

Returns PointVector in PDMS Format

```csharp
public abstract string ToString();
```

#### `Towards` Method

Change the direction of the PointVector to point towards pos

```csharp
public abstract void Towards( Position pos );
```

**Parameters**

- **pos** —

## Operators

#### `Equality` Operator

Same PointVector

```csharp
public static bool operator ==( PointVector p1 , PointVector p2 );
```

**Parameters**

- **p1** — 
- **p2** —

#### `Inequality` Operator

Not same PointVector

```csharp
public static bool operator !=( PointVector p1 , PointVector p2 );
```

**Parameters**

- **p1** — 
- **p2** —
