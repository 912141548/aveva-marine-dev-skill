---
title: Aveva.ApplicationFramework.Presentation.ResourceSet Class
namespace: Aveva.ApplicationFramework.Presentation
assembly: Aveva.ApplicationFramework.Presentation
kind: Class
source: Aveva.ApplicationFramework
---

# Aveva.ApplicationFramework.Presentation.ResourceSet Class

> Represent a set of culture-specific resource files.

## Syntax

```csharp
public abstract class ResourceSet
```

## Inheritance

`System.Object` → `Aveva.ApplicationFramework.Presentation.ResourceSet`

## Thread Safety

Public static ( Shared in Visual Basic) members of this type are
safe for multithreaded operations. Instance members are not guaranteed to be
thread-safe.

## Requirements

Namespace:
Aveva.ApplicationFramework.Presentation
Assembly: Aveva.ApplicationFramework.Presentation (in Aveva.ApplicationFramework.Presentation.dll)

## Properties

#### `Basename` Property

Basename for ResourceSet

```csharp
public abstract string Basename {get;}
```

#### `Manager` Property

The System.Resources.ResourceManager for the ResourceSet.

```csharp
public abstract System.Resources.ResourceManager Manager {get;}
```

#### `Pathname` Property

Path to resource file

```csharp
public abstract string Pathname {get;}
```

## Methods

#### `ReleaseResources` Method

Release all resources for this ResourceSet

```csharp
public abstract void ReleaseResources();
```
