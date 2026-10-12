---
title: Aveva.Pdms.Standalone.PdmsStandalone Class
namespace: Aveva.Pdms.Standalone
assembly: Aveva.Pdms.Standalone
kind: Class
source: Aveva.Pdms.Standalone
---

# Aveva.Pdms.Standalone.PdmsStandalone Class

> Static support class for standalone Plant/Marine applications.

## Syntax

```csharp
public class PdmsStandalone
```

## Inheritance

`System.Object` → `Aveva.Pdms.Standalone.PdmsStandalone`

## Thread Safety

Public static ( Shared in Visual Basic) members of this type are
safe for multithreaded operations. Instance members are not guaranteed to be
thread-safe.

## Requirements

Namespace:
Aveva.Pdms.Standalone
Assembly: Aveva.Pdms.Standalone (in Aveva.Pdms.Standalone.dll)

## Constructors

#### `PdmsStandalone` Constructor

Initializes a new instance of the PdmsStandalone class.

```csharp
public PdmsStandalone();
```

## Properties

#### `MDB` Property

Currently open MDB

```csharp
public static Aveva.Pdms.Database.MDB MDB {get;}
```

#### `Project` Property

Currently open Project

```csharp
public static Aveva.Pdms.Database.Project Project {get;}
```

## Methods

#### `Close` Method

Close the project and MDB

```csharp
public static void Close();
```

#### `ExitError` Method (Exception)

Exit with an error, displaying details on exception

```csharp
public static void ExitError( Exception ex );
```

**Parameters**

- **ex** — Error Exception

#### `ExitError` Method (String)

Exit with an error, displaying message

```csharp
public static void ExitError( string sMessage );
```

**Parameters**

- **sMessage** — Error message

#### `Finish` Method

Finalise standalone application.

```csharp
public static void Finish();
```

#### `Open` Method

Open a project and MDB with given user credentials

```csharp
public static bool Open( string sProject , string sUser , string sPass , string sMdbName );
```

**Parameters**

- **sProject** — Project name
- **sUser** — User name
- **sPass** — Password
- **sMdbName** — MDB name (no leading '/')

**Return Value**

True, if open was successful

#### `Start` Method

Initialise standalone application.

```csharp
public static bool Start();
```

**Return Value**

True, if initialisation is successful
