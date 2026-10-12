---
title: Aveva.ApplicationFramework.ServiceEventArgs Class
namespace: Aveva.ApplicationFramework
assembly: Aveva.ApplicationFramework
kind: Class
source: Aveva.ApplicationFramework
---

# Aveva.ApplicationFramework.ServiceEventArgs Class

> Class used to hold the event arguments in SeviceManager related events

## Syntax

```csharp
public class ServiceEventArgs : EventArgs
```

## Inheritance

`System.Object` → `System.EventArgs` → `Aveva.ApplicationFramework.ServiceEventArgs`

## Thread Safety

Public static ( Shared in Visual Basic) members of this type are
safe for multithreaded operations. Instance members are not guaranteed to be
thread-safe.

## Requirements

Namespace:
Aveva.ApplicationFramework
Assembly: Aveva.ApplicationFramework (in Aveva.ApplicationFramework.dll)

## Constructors

#### `ServiceEventArgs` Constructor

Initializes a new instance of the ServiceEventArgs class.

```csharp
public ServiceEventArgs( Type serviceType );
```

**Parameters**

- **serviceType** —

## Properties

#### `Service` Property

Gets the service which was added for removed

```csharp
public System.Type Service {get;}
```
