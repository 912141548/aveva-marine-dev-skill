---
title: Aveva.ApplicationFramework.AddinEventArgs Class
namespace: Aveva.ApplicationFramework
assembly: Aveva.ApplicationFramework
kind: Class
source: Aveva.ApplicationFramework
---

# Aveva.ApplicationFramework.AddinEventArgs Class

> Class used to hold the event arguments in Addin related events

## Syntax

```csharp
public class AddinEventArgs : EventArgs
```

## Inheritance

`System.Object` → `System.EventArgs` → `Aveva.ApplicationFramework.AddinEventArgs`

## Thread Safety

Public static ( Shared in Visual Basic) members of this type are
safe for multithreaded operations. Instance members are not guaranteed to be
thread-safe.

## Requirements

Namespace:
Aveva.ApplicationFramework
Assembly: Aveva.ApplicationFramework (in Aveva.ApplicationFramework.dll)

## Constructors

#### `AddinEventArgs` Constructor

Constructor for AddinEventArgs

```csharp
public AddinEventArgs( Addin addin );
```

**Parameters**

- **addin** —

## Properties

#### `Addin` Property

Gets the Addin

```csharp
public Addin Addin {get;}
```
