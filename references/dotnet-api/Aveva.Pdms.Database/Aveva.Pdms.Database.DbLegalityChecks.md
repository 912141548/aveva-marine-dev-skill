---
title: Aveva.Pdms.Database.DbLegalityChecks Class
namespace: Aveva.Pdms.Database
assembly: Aveva.Pdms.Database
kind: Class
source: Aveva.Pdms.Database
---

# Aveva.Pdms.Database.DbLegalityChecks Class

> Class to registry legality checkers- For AVEVA use only

## Syntax

```csharp
public abstract class DbLegalityChecks
```

## Inheritance

`System.Object` → `Aveva.Pdms.Database.DbLegalityChecks`

## Thread Safety

Public static ( Shared in Visual Basic) members of this type are
safe for multithreaded operations. Instance members are not guaranteed to be
thread-safe.

## Requirements

Namespace:
Aveva.Pdms.Database
Assembly: Aveva.Pdms.Database (in Aveva.Pdms.Database.dll)

## Methods

#### `AddBoolAttributeAllowed` Method

Add Delegate to test if setting of specified boolean attributre is allowed- For AVEVA use only

```csharp
public static void AddBoolAttributeAllowed( DbAttribute att , BoolAttributeDelegate plug );
```

#### `AddCopyElementAllowed` Method

Add Delegate to test if Copy of element of specified type is allowed- For AVEVA use only

```csharp
public static void AddCopyElementAllowed( DbElementType type , CopyDelegate plug );
```

#### `AddCreateElementAllowed` Method

Add Delegate to test if creation of element is allowed- For AVEVA use only

```csharp
public static void AddCreateElementAllowed( DbElementType type , CreateDelegate plug );
```

#### `AddDeleteElementAllowed` Method

Add Delegate to test if deletion of element of specified type is allowed- For AVEVA use only

```csharp
public static void AddDeleteElementAllowed( DbElementType type , DeleteDelegate plug );
```

#### `AddDoubleArrayAttributeAllowed` Method

Add Delegate to test if setting of specified real array attributre is allowed- For AVEVA use only

```csharp
public static void AddDoubleArrayAttributeAllowed( DbAttribute att , DoubleArrayAttributeDelegate plug );
```

#### `AddDoubleAttributeAllowed` Method

Add Delegate to test if setting of specified real attributre is allowed- For AVEVA use only

```csharp
public static void AddDoubleAttributeAllowed( DbAttribute att , DoubleAttributeDelegate plug );
```

#### `AddIntArrayAttributeAllowed` Method

Add Delegate to test if setting of specified int array attributre is allowed- For AVEVA use only

```csharp
public static void AddIntArrayAttributeAllowed( DbAttribute att , IntArrayAttributeDelegate plug );
```

#### `AddIntAttributeAllowed` Method

Add Delegate to test if setting of specified int attributre is allowed- For AVEVA use only

```csharp
public static void AddIntAttributeAllowed( DbAttribute att , IntAttributeDelegate plug );
```

#### `AddMoveElementAllowed` Method

Add Delegate to test if Move(INCLUDE) of element of specified type is allowed- For AVEVA use only

```csharp
public static void AddMoveElementAllowed( DbElementType type , MoveDelegate plug );
```

#### `AddRefArrayAttributeAllowed` Method

Add Delegate to test if setting of specified ref array attributre is allowed- For AVEVA use only

```csharp
public static void AddRefArrayAttributeAllowed( DbAttribute att , RefArrayAttributeDelegate plug );
```

#### `AddRefAttributeAllowed` Method

Add Delegate to test if setting of specified ref attributre is allowed- For AVEVA use only

```csharp
public static void AddRefAttributeAllowed( DbAttribute att , RefAttributeDelegate plug );
```

#### `AddStringAttributeAllowed` Method

Add Delegate to test if setting of specified string attributre is allowed- For AVEVA use only

```csharp
public static void AddStringAttributeAllowed( DbAttribute att , StringAttributeDelegate plug );
```
