---
title: Aveva.ApplicationFramework.Addin Class
namespace: Aveva.ApplicationFramework
assembly: Aveva.ApplicationFramework
kind: Class
source: Aveva.ApplicationFramework
---

# Aveva.ApplicationFramework.Addin Class

> Class to represent an ApplicationFramework Addin

## Syntax

```csharp
public abstract class Addin
```

## Inheritance

`System.Object` → `Aveva.ApplicationFramework.Addin`

## Thread Safety

Public static ( Shared in Visual Basic) members of this type are
safe for multithreaded operations. Instance members are not guaranteed to be
thread-safe.

## Requirements

Namespace:
Aveva.ApplicationFramework
Assembly: Aveva.ApplicationFramework (in Aveva.ApplicationFramework.dll)

## Properties

#### `Assembly` Property

Assembly containing the Addin

```csharp
public abstract System.Reflection.Assembly Assembly {get;}
```

#### `Description` Property

Addin Description

```csharp
public abstract string Description {get;}
```

#### `IsStarted` Property

Get whether the addins Start method has been called.

```csharp
public abstract bool IsStarted {get;}
```

#### `Name` Property

Addin Name

```csharp
public abstract string Name {get;}
```

## Methods

#### `Start` Method

Calls the Start method on the Addin interface

```csharp
public abstract void Start();
```

#### `Stop` Method

Calls the Stop method on the Addin interface

```csharp
public abstract void Stop();
```
