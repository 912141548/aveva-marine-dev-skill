---
title: Aveva.Pdms.Database.RefTableEnumerator Class
namespace: Aveva.Pdms.Database
assembly: Aveva.Pdms.Database
kind: Class
source: Aveva.Pdms.Database
---

# Aveva.Pdms.Database.RefTableEnumerator Class

> Ref Table Enumerator. N.B. Enumerator MUST be explicitly disposed to clean up resources

## Syntax

```csharp
public abstract class RefTableEnumerator : IEnumerator , IDisposable
```

## Inheritance

`System.Object` → `Aveva.Pdms.Database.RefTableEnumerator`

## Thread Safety

Public static ( Shared in Visual Basic) members of this type are
safe for multithreaded operations. Instance members are not guaranteed to be
thread-safe.

## Requirements

Namespace:
Aveva.Pdms.Database
Assembly: Aveva.Pdms.Database (in Aveva.Pdms.Database.dll)

## Properties

#### `Current` Property

Get current entry. The object returned will always be a DbElement

```csharp
public abstract object Current {get;}
```

**Implements**

IEnumerator.Current

## Methods

#### `Dispose` Method

```csharp
public abstract void Dispose();
```

**Implements**

IDisposable.Dispose

#### `MoveNext` Method

Move to next entry in ref table

```csharp
public abstract bool MoveNext();
```

**Implements**

IEnumerator.MoveNext

#### `Reset` Method

Reset scan to start of range

```csharp
public abstract void Reset();
```

**Implements**

IEnumerator.Reset
