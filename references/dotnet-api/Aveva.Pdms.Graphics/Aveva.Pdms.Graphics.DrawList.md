---
title: Aveva.Pdms.Graphics.DrawList Class
namespace: Aveva.Pdms.Graphics
assembly: Aveva.Pdms.Graphics
kind: Class
source: Aveva.Pdms.Graphics
---

# Aveva.Pdms.Graphics.DrawList Class

> Summary description for DrawList.

## Syntax

```csharp
public abstract class DrawList
```

## Inheritance

`System.Object` → `Aveva.Pdms.Graphics.DrawList`

## Thread Safety

Public static ( Shared in Visual Basic) members of this type are
safe for multithreaded operations. Instance members are not guaranteed to be
thread-safe.

## Requirements

Namespace:
Aveva.Pdms.Graphics
Assembly: Aveva.Pdms.Graphics (in Aveva.Pdms.Graphics.dll)

## Methods

#### `Add` Method (DbElement)

```csharp
public abstract void Add( DbElement element );
```

**Parameters**

- **element** — 

#### `Add` Method (DbElement[])

```csharp
public abstract void Add( DbElement[] elements );
```

**Parameters**

- **elements** —

#### `AddOnly` Method (DbElement)

```csharp
public abstract void AddOnly( DbElement element );
```

**Parameters**

- **element** — 

#### `AddOnly` Method (DbElement[])

```csharp
public abstract void AddOnly( DbElement[] elements );
```

**Parameters**

- **elements** —

#### `AddReferences` Method

```csharp
public abstract void AddReferences( DbElement element );
```

**Parameters**

- **element** —

#### `AddWithinVolume` Method

```csharp
public abstract void AddWithinVolume( DbElement element );
```

**Parameters**

- **element** —

#### `Exists` Method

```csharp
public abstract bool Exists( DbElement element );
```

**Parameters**

- **element** —

#### `GetDrawListMember` Method

```csharp
public abstract DrawListMember GetDrawListMember( DbElement element );
```

**Parameters**

- **element** —

#### `GetVisualProperties` Method

```csharp
public abstract void GetVisualProperties( ref bool autoColour , ref double autoColorRed , ref double autoColorGreen , ref double autoColorBlue , ref int transparency , ref bool edges );
```

**Parameters**

- **autoColour** — 
- **autoColorRed** — 
- **autoColorGreen** — 
- **autoColorBlue** — 
- **transparency** — 
- **edges** —

#### `GetWithinVolume` Method

```csharp
public abstract DbElement[] GetWithinVolume( DbElement element );
```

**Parameters**

- **element** —

#### `Highlight` Method (DbElement)

```csharp
public abstract void Highlight( DbElement element );
```

**Parameters**

- **element** — 

#### `Highlight` Method (DbElement[])

```csharp
public abstract void Highlight( DbElement[] elements );
```

**Parameters**

- **elements** —

#### `Members` Method

```csharp
public abstract DrawListMember[] Members();
```

#### `Remove` Method (DbElement)

```csharp
public abstract void Remove( DbElement element );
```

**Parameters**

- **element** — 

#### `Remove` Method (DbElement[])

```csharp
public abstract void Remove( DbElement[] elements );
```

**Parameters**

- **elements** — 

#### `Remove` Method (DrawListMember)

```csharp
public abstract void Remove( DrawListMember member );
```

**Parameters**

- **member** — 

#### `Remove` Method (DrawListMember[])

```csharp
public abstract void Remove( DrawListMember[] members );
```

**Parameters**

- **members** —

#### `RemoveAll` Method

```csharp
public abstract void RemoveAll();
```

#### `RemoveOnly` Method (DbElement)

```csharp
public abstract void RemoveOnly( DbElement element );
```

**Parameters**

- **element** — 

#### `RemoveOnly` Method (DbElement[])

```csharp
public abstract void RemoveOnly( DbElement[] elements );
```

**Parameters**

- **elements** — 

#### `RemoveOnly` Method (DrawListMember)

```csharp
public abstract void RemoveOnly( DrawListMember member );
```

**Parameters**

- **member** — 

#### `RemoveOnly` Method (DrawListMember[])

```csharp
public abstract void RemoveOnly( DrawListMember[] members );
```

**Parameters**

- **members** —

#### `SetColour` Method

```csharp
public abstract void SetColour( DrawListMember[] members , int colour );
```

**Parameters**

- **members** — 
- **colour** —

#### `SetEdges` Method

```csharp
public abstract void SetEdges( DrawListMember[] members , bool edges );
```

**Parameters**

- **members** — 
- **edges** —

#### `SetTransparency` Method

```csharp
public abstract void SetTransparency( DrawListMember[] members , int transparency );
```

**Parameters**

- **members** — 
- **transparency** —

#### `SetVisibility` Method

```csharp
public abstract void SetVisibility( DrawListMember[] members , bool visibility );
```

**Parameters**

- **members** — 
- **visibility** —

#### `SetVisualProperties` Method (DrawListMember[], Boolean, Int32, Int32, Boolean)

```csharp
public abstract void SetVisualProperties( DrawListMember[] members , bool visibility , int colour , int transparency , bool edges );
```

**Parameters**

- **members** — 
- **visibility** — 
- **colour** — 
- **transparency** — 
- **edges** — 

#### `SetVisualProperties` Method (Boolean, Int32, Int32, Boolean)

```csharp
public abstract void SetVisualProperties( bool autoColour , int colour , int transparency , bool edges );
```

**Parameters**

- **autoColour** — 
- **colour** — 
- **transparency** — 
- **edges** —

#### `Unhighlight` Method (DbElement)

```csharp
public abstract void Unhighlight( DbElement element );
```

**Parameters**

- **element** — 

#### `Unhighlight` Method (DbElement[])

```csharp
public abstract void Unhighlight( DbElement[] elements );
```

**Parameters**

- **elements** —

#### `VisibleAll` Method

```csharp
public abstract void VisibleAll();
```
