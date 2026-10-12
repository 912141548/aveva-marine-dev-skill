---
title: Aveva.Pdms.Database.DbCopyOption Structure
namespace: Aveva.Pdms.Database
assembly: Aveva.Pdms.Database
kind: Structure
source: Aveva.Pdms.Database
---

# Aveva.Pdms.Database.DbCopyOption Structure

> Container for copy options.

## Syntax

```csharp
public struct DbCopyOption
```

## Inheritance

`System.Object` → `System.ValueType` → `Aveva.Pdms.Database.DbCopyOption`

## Thread Safety

Public static ( Shared in Visual Basic) members of this type are
safe for multithreaded operations. Instance members are not guaranteed to be
thread-safe.

## Requirements

Namespace:
Aveva.Pdms.Database
Assembly: Aveva.Pdms.Database (in Aveva.Pdms.Database.dll)

## Properties

#### `FromName` Property

Name of copy source

```csharp
public string FromName {get; set;}
```

#### `IncludeRules` Property

True, if Rules included in copy

```csharp
public bool IncludeRules {get; set;}
```

#### `ReExecuteRules` Property

True, if Rules are re-executed on copy

```csharp
public bool ReExecuteRules {get; set;}
```

#### `Rename` Property

True, if rename on copy

```csharp
public bool Rename {get; set;}
```

#### `ToName` Property

Name of copy destination

```csharp
public string ToName {get; set;}
```
