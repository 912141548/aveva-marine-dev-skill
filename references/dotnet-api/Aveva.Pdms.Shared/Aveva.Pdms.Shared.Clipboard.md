---
title: Aveva.Pdms.Shared.Clipboard Class
namespace: Aveva.Pdms.Shared
assembly: Aveva.Pdms.Shared
kind: Class
source: Aveva.Pdms.Shared
---

# Aveva.Pdms.Shared.Clipboard Class

> Summary description for Clipboard.

## Syntax

```csharp
public abstract class Clipboard
```

## Inheritance

`System.Object` → `Aveva.Pdms.Shared.Clipboard`

## Thread Safety

Public static ( Shared in Visual Basic) members of this type are
safe for multithreaded operations. Instance members are not guaranteed to be
thread-safe.

## Requirements

Namespace:
Aveva.Pdms.Shared
Assembly: Aveva.Pdms.Shared (in Aveva.Pdms.Shared.dll)

## Fields

#### `CurrentClipboard` Field

```csharp
public static readonly Clipboard CurrentClipboard;
```

## Properties

#### `Members` Property

```csharp
public abstract Aveva.Pdms.Database.DbElement[] Members {get; set;}
```

#### `Mode` Property

```csharp
public abstract EditMode Mode {get; set;}
```
