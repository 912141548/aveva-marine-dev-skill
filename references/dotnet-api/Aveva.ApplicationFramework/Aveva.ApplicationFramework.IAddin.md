---
title: Aveva.ApplicationFramework.IAddin Interface
namespace: Aveva.ApplicationFramework
assembly: Aveva.ApplicationFramework
kind: Interface
source: Aveva.ApplicationFramework
---

# Aveva.ApplicationFramework.IAddin Interface

> Interface which enables communication between the framework and the addin.

## Syntax

```csharp
public interface IAddin
```

## Requirements

Namespace:
Aveva.ApplicationFramework
Assembly: Aveva.ApplicationFramework (in Aveva.ApplicationFramework.dll)

## Properties

#### `Description` Property

Description of Addin

```csharp
string Description {get;}
```

#### `Name` Property

Name of Addin

```csharp
string Name {get;}
```

## Methods

#### `Start` Method

Start the Addin

```csharp
void Start( ServiceManager serviceManager );
```

**Parameters**

- **serviceManager** —

#### `Stop` Method

Stop the Addn

```csharp
void Stop();
```
