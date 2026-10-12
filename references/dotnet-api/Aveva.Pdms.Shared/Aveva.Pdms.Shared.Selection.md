---
title: Aveva.Pdms.Shared.Selection Class
namespace: Aveva.Pdms.Shared
assembly: Aveva.Pdms.Shared
kind: Class
source: Aveva.Pdms.Shared
---

# Aveva.Pdms.Shared.Selection Class

> Summary description for Selection.

## Syntax

```csharp
public abstract class Selection
```

## Inheritance

`System.Object` → `Aveva.Pdms.Shared.Selection`

## Thread Safety

Public static ( Shared in Visual Basic) members of this type are
safe for multithreaded operations. Instance members are not guaranteed to be
thread-safe.

## Requirements

Namespace:
Aveva.Pdms.Shared
Assembly: Aveva.Pdms.Shared (in Aveva.Pdms.Shared.dll)

## Fields

#### `CurrentSelection` Field

```csharp
public static readonly Selection CurrentSelection;
```

## Properties

#### `Members` Property

```csharp
public abstract Aveva.Pdms.Database.DbElement[] Members {get; set;}
```

## Methods

#### `RaiseSelectionChanged` Method

Raise the Selection Changed event.

```csharp
public static void RaiseSelectionChanged( object sender , SelectionChangedEventArgs e );
```

**Parameters**

- **sender** — Object raising the event
- **e** — Event arguments

## Events

#### `SelectionChanged` Event

Current Element Changed event.

```csharp
public static event SelectionChangedEventHandler SelectionChanged;
```
