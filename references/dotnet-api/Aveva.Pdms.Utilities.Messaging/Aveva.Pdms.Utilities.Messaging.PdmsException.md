---
title: Aveva.Pdms.Utilities.Messaging.PdmsException Class
namespace: Aveva.Pdms.Utilities.Messaging
assembly: Aveva.Pdms.Utilities
kind: Class
source: Aveva.Pdms.Utilities
---

# Aveva.Pdms.Utilities.Messaging.PdmsException Class

> Exception handling class. All PDMS exceptions should throw a PdmsException object.

## Syntax

```csharp
public abstract class PdmsException : ApplicationException
```

## Inheritance

`System.Object` → `System.Exception` → `System.ApplicationException` → `Aveva.Pdms.Utilities.Messaging.PdmsException`

## Thread Safety

Public static ( Shared in Visual Basic) members of this type are
safe for multithreaded operations. Instance members are not guaranteed to be
thread-safe.

## Requirements

Namespace:
Aveva.Pdms.Utilities.Messaging
Assembly: Aveva.Pdms.Utilities (in Aveva.Pdms.Utilities.dll)

## Properties

#### `Error` Property

error associated with exception

```csharp
public abstract PdmsMessage Error {get;}
```

## Methods

#### `Output` Method

Output Error associated with exception

```csharp
public abstract void Output();
```

#### `ToString` Method

Convert to string

```csharp
public abstract string ToString();
```
