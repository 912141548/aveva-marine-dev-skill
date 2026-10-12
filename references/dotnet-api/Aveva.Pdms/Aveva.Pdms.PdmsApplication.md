---
title: Aveva.Pdms.PdmsApplication Class
namespace: Aveva.Pdms
assembly: Aveva.Pdms
kind: Class
source: Aveva.Pdms
---

# Aveva.Pdms.PdmsApplication Class

> Entry point for PDMS application framework

## Syntax

```csharp
public abstract class PdmsApplication
```

## Inheritance

`System.Object` → `Aveva.Pdms.PdmsApplication`

## Thread Safety

Public static ( Shared in Visual Basic) members of this type are
safe for multithreaded operations. Instance members are not guaranteed to be
thread-safe.

## Requirements

Namespace:
Aveva.Pdms
Assembly: Aveva.Pdms (in Aveva.Pdms.dll)

## Properties

#### `GraphicsMode` Property

True if application is in graphics mode

```csharp
public static bool GraphicsMode {get;}
```

## Methods

#### `Exit` Method

Exit application.

```csharp
public static void Exit( string message );
```

**Parameters**

- **message** — Exit message

#### `Finish` Method

Finish application.

```csharp
public static void Finish();
```

#### `getLicenseError` Method

get license error

```csharp
public static string getLicenseError();
```

#### `getLicenseFeature` Method

get license feature

```csharp
public static bool getLicenseFeature( string feature );
```

**Parameters**

- **feature** —

#### `hasLicenseFeature` Method

has license feature

```csharp
public static bool hasLicenseFeature( string feature );
```

**Parameters**

- **feature** —

#### `RaiseBeforeFinished` Method

Raise Finished event.

```csharp
public static void RaiseBeforeFinished( object sender , EventArgs e );
```

**Parameters**

- **sender** — Object raising the event
- **e** — Event arguments

#### `RaiseFinished` Method

Raise Finished event.

```csharp
public static void RaiseFinished( object sender , EventArgs e );
```

**Parameters**

- **sender** — Object raising the event
- **e** — Event arguments

#### `Start` Method

Start the application.

```csharp
public static void Start( bool isGraphics , int moduleNumber , bool isBatch , bool isNoConsole , string logfile );
```

**Parameters**

- **isGraphics** — True if to be started in graphics mode
- **moduleNumber** — 
- **isBatch** — True is to be started in batch mode
- **isNoConsole** — True if to be started with no console
- **logfile** — Filename for application log file

#### `StartEventLoop` Method

Start application activity.

```csharp
public static void StartEventLoop();
```

#### `StartViaCommsFile` Method

Start the application using a Comms file.

```csharp
public static void StartViaCommsFile( bool isGraphics , int moduleNumber , string moduleName );
```

**Parameters**

- **isGraphics** — True if to be started in graphics mode
- **moduleNumber** — Module number
- **moduleName** — Module name

## Events

#### `BeforeFinished` Event

BeforeFinished event handler.

```csharp
public static event BeforeFinishEventHandler BeforeFinished;
```

#### `Finished` Event

Finished event handler.

```csharp
public static event FinishEventHandler Finished;
```
