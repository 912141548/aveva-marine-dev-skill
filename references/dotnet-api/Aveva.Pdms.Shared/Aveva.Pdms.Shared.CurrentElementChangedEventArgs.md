---
title: Aveva.Pdms.Shared.CurrentElementChangedEventArgs Class
namespace: Aveva.Pdms.Shared
assembly: Aveva.Pdms.Shared
kind: Class
source: Aveva.Pdms.Shared
---

# Aveva.Pdms.Shared.CurrentElementChangedEventArgs Class

> Event arguments for Current Element Changed event.

## Syntax

```csharp
public class CurrentElementChangedEventArgs : EventArgs
```

## Inheritance

`System.Object` → `System.EventArgs` → `Aveva.Pdms.Shared.CurrentElementChangedEventArgs`

## Thread Safety

Public static ( Shared in Visual Basic) members of this type are
safe for multithreaded operations. Instance members are not guaranteed to be
thread-safe.

## Requirements

Namespace:
Aveva.Pdms.Shared
Assembly: Aveva.Pdms.Shared (in Aveva.Pdms.Shared.dll)

## Constructors

#### `CurrentElementChangedEventArgs` Constructor

Constructor.

```csharp
public CurrentElementChangedEventArgs( DbElement ele );
```

**Parameters**

- **ele** — Element to associate with event

## Properties

#### `Element` Property

Element associated with event.

```csharp
public Aveva.Pdms.Database.DbElement Element {get; set;}
```
