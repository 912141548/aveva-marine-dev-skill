---
title: Aveva.Pdms.PdmsVersion Class
namespace: Aveva.Pdms
assembly: Aveva.Pdms
kind: Class
source: Aveva.Pdms
---

# Aveva.Pdms.PdmsVersion Class

> PDMS Version query.

## Syntax

```csharp
public abstract class PdmsVersion
```

## Inheritance

`System.Object` → `Aveva.Pdms.PdmsVersion`

## Thread Safety

Public static ( Shared in Visual Basic) members of this type are
safe for multithreaded operations. Instance members are not guaranteed to be
thread-safe.

## Requirements

Namespace:
Aveva.Pdms
Assembly: Aveva.Pdms (in Aveva.Pdms.dll)

## Methods

#### `GetCompanyName` Method

Retrieve company name PDMS is licensed to

```csharp
public static string GetCompanyName();
```

**Return Value**

Licenced company name

#### `GetCopyright` Method

Retrieve copyright information for PDMS

```csharp
public static string GetCopyright();
```

**Return Value**

Copyright text

#### `GetModuleName` Method

Retrieve the name of a PDMS module

```csharp
public static string GetModuleName( ModuleType module );
```

**Parameters**

- **module** — Module identifier

**Return Value**

Module name

#### `GetModuleVersion` Method

Retrieve the version of a PDMS module

```csharp
public static string GetModuleVersion( ModuleType module );
```

**Parameters**

- **module** — Module identifier

**Return Value**

Module version identifier

#### `GetName` Method

Retrieve name of current module (i.e. VANTAGE PDMS Design)

```csharp
public static string GetName();
```

**Return Value**

Current module name

#### `GetShortBanner` Method

Retrieve short banner string (i.e. qbann)

```csharp
public static string GetShortBanner();
```

**Return Value**

Banner text

#### `GetStatus` Method

Retrieve any special status instructions (i.e. for pre-release builds)

```csharp
public static string GetStatus();
```

**Return Value**

Status text

#### `GetVersion` Method

Retrieve version number of PDMS excluding Mk (i.e. 11.6)

```csharp
public static string GetVersion();
```

**Return Value**

PDMS version identifier
