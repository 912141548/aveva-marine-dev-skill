---
title: Aveva.Pdms.Utilities.Tracing.PdmsTrace Class
namespace: Aveva.Pdms.Utilities.Tracing
assembly: Aveva.Pdms.Utilities
kind: Class
source: Aveva.Pdms.Utilities
---

# Aveva.Pdms.Utilities.Tracing.PdmsTrace Class

> PDMS application tracing control. This class includes facilities to output trace statements, monitor CPU, and retrieving the current trace entry stack. Trace entry/exit is done via the TraceEntry class.

## Syntax

```csharp
public abstract class PdmsTrace
```

## Inheritance

`System.Object` → `Aveva.Pdms.Utilities.Tracing.PdmsTrace`

## Thread Safety

Public static ( Shared in Visual Basic) members of this type are
safe for multithreaded operations. Instance members are not guaranteed to be
thread-safe.

## Requirements

Namespace:
Aveva.Pdms.Utilities.Tracing
Assembly: Aveva.Pdms.Utilities (in Aveva.Pdms.Utilities.dll)

## Properties

#### `CPUTraceStarted` Property

Indicates if CPU monitoring is on or not

```csharp
public static bool CPUTraceStarted {get;}
```

#### `Enabled` Property

Enable or disable tracing

```csharp
public static bool Enabled {get; set;}
```

#### `TraceLog` Property

Log file for trace.

```csharp
public static string TraceLog {get; set;}
```

## Methods

#### `GetTraceback` Method

Get current stack of trace entries

```csharp
public static string GetTraceback( bool outputToConsole );
```

**Parameters**

- **outputToConsole** — Output or not

#### `GetTraceFlag` Method

Get value of specified trace flag

```csharp
public static int GetTraceFlag( TraceNumber traceNumber );
```

**Parameters**

- **traceNumber** — trace number

#### `SetTraceFlag` Method

Set value of specified trace flag

```csharp
public static void SetTraceFlag( TraceNumber traceNumber , int value );
```

**Parameters**

- **traceNumber** — trace number
- **value** — new value to set trace number to

#### `StartCPUTrace` Method

Turn on CPU recording (suppressing trace output)

```csharp
public static void StartCPUTrace();
```

#### `StopCPUTrace` Method

Turn off CPU recording, outputting results. Standard trace output will be reactivated.

```csharp
public static string StopCPUTrace( bool outputToConsole );
```

**Parameters**

- **outputToConsole** — output or not

#### `TestFlag` Method

Test if trace flag is non zero

```csharp
public static bool TestFlag( TraceNumber traceNumber );
```

**Parameters**

- **traceNumber** — trace number

#### `TestFlagBit` Method

Test if bit value for trace flag is set.

```csharp
public static bool TestFlagBit( TraceNumber traceNumber , int bit );
```

**Parameters**

- **traceNumber** — trace number
- **bit** — bit number

#### `Trace` Method (ArrayList)

Output values as trace converting via 'ToString'. Trace output should always be conditional on a trace flag value.

```csharp
public static void Trace( ArrayList list );
```

**Parameters**

- **list** — 

#### `Trace` Method (Object)

Output value as trace converting via 'ToString'. Trace output should always be conditional on a trace flag value.

```csharp
public static void Trace( object val );
```

**Parameters**

- **val** — 

#### `Trace` Method (String)

Output string as trace. Trace output should always be conditional on a trace flag value.

```csharp
public static void Trace( string val );
```

**Parameters**

- **val** —
