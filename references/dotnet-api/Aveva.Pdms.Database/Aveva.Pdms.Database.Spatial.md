---
title: Aveva.Pdms.Database.Spatial Class
namespace: Aveva.Pdms.Database
assembly: Aveva.Pdms.Database
kind: Class
source: Aveva.Pdms.Database
---

# Aveva.Pdms.Database.Spatial Class

> Class to do volumetic queries. For exact opertaions on catalogue items, all primities with TUFL set are tested.

## Syntax

```csharp
public abstract class Spatial
```

## Inheritance

`System.Object` → `Aveva.Pdms.Database.Spatial`

## Thread Safety

Public static ( Shared in Visual Basic) members of this type are
safe for multithreaded operations. Instance members are not guaranteed to be
thread-safe.

## Requirements

Namespace:
Aveva.Pdms.Database
Assembly: Aveva.Pdms.Database (in Aveva.Pdms.Database.dll)

## Fields

#### `Instance` Field

Instance of class.

```csharp
public static readonly Spatial Instance;
```

## Methods

#### `ElementInBox` Method

Does the 3D volume for an element overlap the given box

```csharp
public abstract bool ElementInBox( DbElement ele , float[] rbox );
```

**Parameters**

- **ele** — 
- **rbox** —

#### `ElementInElementBox` Method

Does the 3D volume for an element overlap the 3D volume for another element?

```csharp
public abstract bool ElementInElementBox( DbElement ele1 , DbElement ele2 );
```

**Parameters**

- **ele1** — 
- **ele2** —

#### `ElementInElementExact` Method

Does element 2 overlap, or enclose element 1. Exact calculations are used to determine this

```csharp
public abstract bool ElementInElementExact( DbElement ele1 , DbElement ele2 , bool bFully );
```

**Parameters**

- **ele1** — 
- **ele2** — 
- **bFully** —

#### `ElementsInBox` Method (Single[], DbElementType[], Boolean)

Return elements within a 3D box climbing to given type

```csharp
public abstract DbElement[] ElementsInBox( float[] rbox , DbElementType[] types , bool bFully );
```

**Parameters**

- **rbox** — box volume
- **types** — Element type to climb to, e.g. Equipment
- **bFully** — Only return elements taht are fully enclosed by box

#### `ElementsInBox` Method (Single[], Boolean)

Return elements within a 3D box

```csharp
public abstract DbElement[] ElementsInBox( float[] rbox , bool bFully );
```

**Parameters**

- **rbox** — box volume
- **bFully** — Only return elements that are fully enclosed by box

#### `ElementsInElementBox` Method (DbElement, DbElementType[], Boolean)

Return elements within the 3D volume of another element, climbing to element of specified type.

```csharp
public abstract DbElement[] ElementsInElementBox( DbElement ele , DbElementType[] types , bool bFully );
```

**Parameters**

- **ele** — 
- **types** — Element type to climb to, e.g. Equipment
- **bFully** — Only return elements that are fully enclosed by box

#### `ElementsInElementBox` Method (DbElement, Boolean)

Return elements within the 3D volume of another element.

```csharp
public abstract DbElement[] ElementsInElementBox( DbElement ele , bool bFully );
```

**Parameters**

- **ele** — 
- **bFully** — Only return elements that are fully enclosed by box

#### `ElementsInElementExact` Method (DbElement, DbElementType[], Boolean)

Return elements which overlap or are fully enclosed by another element. Exact calculations are used rather than the surrounding 3D box. Only elements at required level are returned.

```csharp
public abstract DbElement[] ElementsInElementExact( DbElement ele , DbElementType[] types , bool bFully );
```

**Parameters**

- **ele** — 
- **types** — Element type to climb to, e.g. Equipment
- **bFully** — Only return elements that are fully enclosed by given element

#### `ElementsInElementExact` Method (DbElement, Boolean)

Return elements which overlap or are fully enclosed by another element. Exact calculations are used rather than the surrounding 3D box.

```csharp
public abstract DbElement[] ElementsInElementExact( DbElement ele , bool bFully );
```

**Parameters**

- **ele** — 
- **bFully** — Only return elements that are fully enclosed by given element

#### `LimitsBox` Method

Limits box for element

```csharp
public abstract bool LimitsBox( DbElement ele , float[] rbox );
```

**Parameters**

- **ele** — 
- **rbox** —
