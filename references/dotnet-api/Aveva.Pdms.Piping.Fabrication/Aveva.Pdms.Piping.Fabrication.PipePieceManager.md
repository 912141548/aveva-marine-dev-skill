---
title: Aveva.Pdms.Piping.Fabrication.PipePieceManager Class
namespace: Aveva.Pdms.Piping.Fabrication
assembly: Aveva.Pdms.Piping
kind: Class
source: Aveva.Pdms.Piping
---

# Aveva.Pdms.Piping.Fabrication.PipePieceManager Class

> Pipe Piece Manager.

## Syntax

```csharp
public abstract class PipePieceManager
```

## Inheritance

`System.Object` → `Aveva.Pdms.Piping.Fabrication.PipePieceManager`

## Thread Safety

Public static ( Shared in Visual Basic) members of this type are
safe for multithreaded operations. Instance members are not guaranteed to be
thread-safe.

## Requirements

Namespace:
Aveva.Pdms.Piping.Fabrication
Assembly: Aveva.Pdms.Piping (in Aveva.Pdms.Piping.dll)

## Methods

#### `GeneratePipePieces` Method

```csharp
public static bool GeneratePipePieces( DbElement element );
```

**Parameters**

- **element** —

#### `GetLastError` Method

```csharp
public static PdmsMessage GetLastError();
```

#### `GetPipePieces` Method

```csharp
public static DbElement[] GetPipePieces( DbElement element );
```

**Parameters**

- **element** —

#### `RemovePipePieces` Method

```csharp
public static bool RemovePipePieces( DbElement pipe );
```

**Parameters**

- **pipe** —
