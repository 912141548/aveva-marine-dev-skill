---
title: Aveva.Pdms.Piping.Fabrication.PipeSpoolManager Class
namespace: Aveva.Pdms.Piping.Fabrication
assembly: Aveva.Pdms.Piping
kind: Class
source: Aveva.Pdms.Piping
---

# Aveva.Pdms.Piping.Fabrication.PipeSpoolManager Class

> Summary description for PipeSpoolManager.

## Syntax

```csharp
public abstract class PipeSpoolManager
```

## Inheritance

`System.Object` → `Aveva.Pdms.Piping.Fabrication.PipeSpoolManager`

## Thread Safety

Public static ( Shared in Visual Basic) members of this type are
safe for multithreaded operations. Instance members are not guaranteed to be
thread-safe.

## Requirements

Namespace:
Aveva.Pdms.Piping.Fabrication
Assembly: Aveva.Pdms.Piping (in Aveva.Pdms.Piping.dll)

## Methods

#### `GeneratePipeSpoolsForPipe` Method

```csharp
public static bool GeneratePipeSpoolsForPipe( DbElement pipe );
```

**Parameters**

- **pipe** —

#### `GetLastError` Method

```csharp
public static PdmsMessage GetLastError();
```

#### `GetPipePiecesForSpool` Method

```csharp
public static DbElement[] GetPipePiecesForSpool( DbElement spool );
```

**Parameters**

- **spool** —

#### `GetPipeSpoolForElement` Method

```csharp
public static DbElement[] GetPipeSpoolForElement( DbElement element );
```

**Parameters**

- **element** —

#### `RemovePipeSpools` Method

```csharp
public static bool RemovePipeSpools( DbElement pipe );
```

**Parameters**

- **pipe** —
