---
title: Aveva.Pdms.Graphics.DrawListMember Class
namespace: Aveva.Pdms.Graphics
assembly: Aveva.Pdms.Graphics
kind: Class
source: Aveva.Pdms.Graphics
---

# Aveva.Pdms.Graphics.DrawListMember Class

> Summary description for DrawListMember.

## Syntax

```csharp
public abstract class DrawListMember
```

## Inheritance

`System.Object` → `Aveva.Pdms.Graphics.DrawListMember`

## Thread Safety

Public static ( Shared in Visual Basic) members of this type are
safe for multithreaded operations. Instance members are not guaranteed to be
thread-safe.

## Requirements

Namespace:
Aveva.Pdms.Graphics
Assembly: Aveva.Pdms.Graphics (in Aveva.Pdms.Graphics.dll)

## Properties

#### `Colour` Property

```csharp
public abstract int Colour {get; set;}
```

#### `DbElement` Property

```csharp
public abstract Aveva.Pdms.Database.DbElement DbElement {get;}
```

#### `Edges` Property

```csharp
public abstract bool Edges {get; set;}
```

#### `Transparency` Property

```csharp
public abstract int Transparency {get; set;}
```

#### `Visibility` Property

```csharp
public abstract bool Visibility {get; set;}
```

## Methods

#### `GetVisualProperties` Method

```csharp
public abstract void GetVisualProperties( ref bool visibility , ref int colour , ref int transparency , ref bool edges );
```

**Parameters**

- **visibility** — 
- **colour** — 
- **transparency** — 
- **edges** —

#### `SetVisualProperties` Method

```csharp
public abstract void SetVisualProperties( bool visibility , int colour , int transparency , bool edges );
```

**Parameters**

- **visibility** — 
- **colour** — 
- **transparency** — 
- **edges** —
