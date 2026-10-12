---
title: Aveva.Pdms.Utilities.Tracing.TraceEntry Class
namespace: Aveva.Pdms.Utilities.Tracing
assembly: Aveva.Pdms.Utilities
kind: Class
source: Aveva.Pdms.Utilities
---

# Aveva.Pdms.Utilities.Tracing.TraceEntry Class

> Class to do subroutine entry and exit trace. The object should be created on the first line off a method. The Dispose method must be called(implicitly or explicitly) on method exit.

## Syntax

```csharp
public abstract class TraceEntry : IDisposable
```

## Inheritance

`System.Object` → `Aveva.Pdms.Utilities.Tracing.TraceEntry`

## Thread Safety

Public static ( Shared in Visual Basic) members of this type are
safe for multithreaded operations. Instance members are not guaranteed to be
thread-safe.

## Requirements

Namespace:
Aveva.Pdms.Utilities.Tracing
Assembly: Aveva.Pdms.Utilities (in Aveva.Pdms.Utilities.dll)

## Methods

#### `Dispose` Method

```csharp
public abstract void Dispose();
```

**Implements**

IDisposable.Dispose

#### `Enter` Method

Create trace entry object.

```csharp
public static TraceEntry Enter( string routineName , TraceNumber traceNumber );
```

**Parameters**

- **routineName** — name to be output
- **traceNumber** — trace number to test against before outputting entry trace
