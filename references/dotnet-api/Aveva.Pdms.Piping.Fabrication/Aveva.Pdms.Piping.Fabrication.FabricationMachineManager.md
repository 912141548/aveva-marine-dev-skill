---
title: Aveva.Pdms.Piping.Fabrication.FabricationMachineManager Class
namespace: Aveva.Pdms.Piping.Fabrication
assembly: Aveva.Pdms.Piping
kind: Class
source: Aveva.Pdms.Piping
---

# Aveva.Pdms.Piping.Fabrication.FabricationMachineManager Class

> Summary description for FabricationMachineManager.

## Syntax

```csharp
public abstract class FabricationMachineManager
```

## Inheritance

`System.Object` → `Aveva.Pdms.Piping.Fabrication.FabricationMachineManager`

## Thread Safety

Public static ( Shared in Visual Basic) members of this type are
safe for multithreaded operations. Instance members are not guaranteed to be
thread-safe.

## Requirements

Namespace:
Aveva.Pdms.Piping.Fabrication
Assembly: Aveva.Pdms.Piping (in Aveva.Pdms.Piping.dll)

## Properties

#### `AddEndExcess` Property

```csharp
public static bool AddEndExcess {get; set;}
```

#### `AddExcessBetweenBends` Property

```csharp
public static bool AddExcessBetweenBends {get; set;}
```

#### `ChangeFlangeToManual` Property

```csharp
public static bool ChangeFlangeToManual {get; set;}
```

#### `CheckStockLength` Property

```csharp
public static bool CheckStockLength {get; set;}
```

#### `ClutchEndPriority` Property

```csharp
public static FabricationMachineManager.ClutchEndPriorityType ClutchEndPriority {get; set;}
```

#### `DisplaySimulation` Property

```csharp
public static bool DisplaySimulation {get; set;}
```

#### `FirstFeedNegative` Property

```csharp
public static bool FirstFeedNegative {get; set;}
```

#### `MaximumMaterialLength` Property

```csharp
public static double MaximumMaterialLength {get; set;}
```

## Methods

#### `BendingMachineAcceptsPipePiece` Method

```csharp
public static bool BendingMachineAcceptsPipePiece( DbElement pipePiece );
```

**Parameters**

- **pipePiece** —

#### `CanFabricatePipePiece` Method

```csharp
public static bool CanFabricatePipePiece( DbElement pipePiece );
```

**Parameters**

- **pipePiece** —

#### `GetBendingMachineResult` Method ()

```csharp
public static BendingMachineResult GetBendingMachineResult();
```

#### `GetBendingMachineResult` Method (DbElement)

```csharp
public static BendingMachineResult GetBendingMachineResult( DbElement pipePiece );
```

**Parameters**

- **pipePiece** —

#### `GetWeldingMachineResult` Method ()

```csharp
public static WeldingMachineResult GetWeldingMachineResult();
```

#### `GetWeldingMachineResult` Method (DbElement)

```csharp
public static WeldingMachineResult GetWeldingMachineResult( DbElement pipePiece );
```

**Parameters**

- **pipePiece** —

#### `RevalidatePipePiece` Method

```csharp
public static bool RevalidatePipePiece( DbElement pipePiece );
```

**Parameters**

- **pipePiece** —

#### `ScanElements` Method

```csharp
public static DbElement[] ScanElements( DbElement ce , DbElementType type );
```

**Parameters**

- **ce** — 
- **type** —

#### `SetBendingMachine` Method

```csharp
public static void SetBendingMachine( DbElement machine );
```

**Parameters**

- **machine** —

#### `SetWeldingMachine` Method

```csharp
public static void SetWeldingMachine( DbElement machine );
```

**Parameters**

- **machine** —

#### `WeldingMachineAcceptsPipePiece` Method

```csharp
public static bool WeldingMachineAcceptsPipePiece( DbElement pipePiece );
```

**Parameters**

- **pipePiece** —
