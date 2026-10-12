---
title: Aveva.Pdms.Geometry.LimitsBox Class
namespace: Aveva.Pdms.Geometry
assembly: Aveva.Pdms.Geometry
kind: Class
source: Aveva.Pdms.Geometry
---

# Aveva.Pdms.Geometry.LimitsBox Class

> Summary description for LimitsBox.

## Syntax

```csharp
public abstract class LimitsBox
```

## Inheritance

`System.Object` → `Aveva.Pdms.Geometry.LimitsBox`

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

Maximum corner of the LimitsBox

```csharp
public abstract Position Maximum {get; set;}
```

#### `Minimum` Property

Minimum corner of the LimitsBox

```csharp
public abstract Position Minimum {get; set;}
```

## Methods

#### `Centre` Method

Return centre point of LimitsBox

```csharp
public abstract Position Centre();
```

#### `Contains` Method

Returns true if box is entirely contained within this LimitsBox

```csharp
public abstract bool Contains( LimitsBox box );
```

**Parameters**

- **box** —

#### `ContainsPoint` Method

Returns true if p is inside (not on) LimitsBox

```csharp
public abstract bool ContainsPoint( Position p );
```

**Parameters**

- **p** —

#### `Create` Method ()

Create LimitsBox

```csharp
public static LimitsBox Create();
```

#### `Create` Method (Position, Position)

Createa LimitsBox with min and max corners specified by p1 and p2

```csharp
public static LimitsBox Create( Position p1 , Position p2 );
```

**Parameters**

- **p1** — 
- **p2** —

#### `Equals` Method (LimitsBox)

Same Limitsbox

```csharp
public abstract bool Equals( LimitsBox box );
```

**Parameters**

- **box** — 

#### `Equals` Method (Object)

Same Limitsbox

```csharp
public override bool Equals( object obj );
```

**Parameters**

- **obj** —

#### `ExpandBy` Method

Expand LimitsBox by val in all directions

```csharp
public abstract void ExpandBy( double val );
```

**Parameters**

- **val** —

#### `ExpandToInclude` Method

Expand LimitsBox to include pos

```csharp
public abstract void ExpandToInclude( Position pos );
```

**Parameters**

- **pos** —

#### `GetHashCode` Method

A hash method is used to quickly generate a hash code, which is an int that corresponds to the value of an object. Hash codes allow C# to store objects more efficiently in collections

```csharp
public override int GetHashCode();
```

#### `Intersection` Method

Returns LimitsBox which consists of the overlap of the two LimitsBoxes

```csharp
public abstract LimitsBox Intersection( LimitsBox box );
```

**Parameters**

- **box** —

#### `Intersects` Method

Returns true if LimitsBoxes intersect

```csharp
public abstract bool Intersects( LimitsBox box );
```

**Parameters**

- **box** —

#### `Merge` Method

Return LimitsBox that is the combination of the 2 LimitsBoxes

```csharp
public abstract LimitsBox Merge( LimitsBox box );
```

**Parameters**

- **box** —

#### `ToString` Method

Returns Limits Box property values in a string

```csharp
public abstract string ToString();
```

#### `Volume` Method

Returns the volume inside the LimitsBox

```csharp
public abstract double Volume();
```

## Operators

#### `Equality` Operator

Same LimitsBox

```csharp
public static bool operator ==( LimitsBox t1 , LimitsBox t2 );
```

**Parameters**

- **t1** — 
- **t2** —

#### `Inequality` Operator

Not Same LimitsBox

```csharp
public static bool operator !=( LimitsBox t1 , LimitsBox t2 );
```

**Parameters**

- **t1** — 
- **t2** —
