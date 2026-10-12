---
title: Aveva.Pdms.Database.DbClaimEventArgs Class
namespace: Aveva.Pdms.Database
assembly: Aveva.Pdms.Database
kind: Class
source: Aveva.Pdms.Database
---

# Aveva.Pdms.Database.DbClaimEventArgs Class

> Deprecated - do not use

## Syntax

```csharp
public class DbClaimEventArgs : EventArgs
```

## Inheritance

`System.Object` → `System.EventArgs` → `Aveva.Pdms.Database.DbClaimEventArgs`

## Thread Safety

Public static ( Shared in Visual Basic) members of this type are
safe for multithreaded operations. Instance members are not guaranteed to be
thread-safe.

## Requirements

Namespace:
Aveva.Pdms.Database
Assembly: Aveva.Pdms.Database (in Aveva.Pdms.Database.dll)

## Constructors

#### `DbClaimEventArgs` Constructor

Claim event argument constructor.

```csharp
public DbClaimEventArgs( DbElement element );
```

**Parameters**

- **element** — Element relating to claim event

## Properties

#### `Element` Property

Element relating to claim event.

```csharp
public DbElement Element {get;}
```
