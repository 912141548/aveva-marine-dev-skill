---
title: Aveva.Pdms.Database.DbPseudoAttribute Class
namespace: Aveva.Pdms.Database
assembly: Aveva.Pdms.Database
kind: Class
source: Aveva.Pdms.Database
---

# Aveva.Pdms.Database.DbPseudoAttribute Class

> Class allows pseudo attribute code to be plugged in. This includes pseudo code for UDAs. There are different methods to plug in the pseudo attribute code depending on the attribute type. User's may only plug code for UADs. The plugging of pseudo attribute code for system attributes is FOR AVEVA USE ONLY

## Syntax

```csharp
public abstract class DbPseudoAttribute
```

## Inheritance

`System.Object` → `Aveva.Pdms.Database.DbPseudoAttribute`

## Thread Safety

Public static ( Shared in Visual Basic) members of this type are
safe for multithreaded operations. Instance members are not guaranteed to be
thread-safe.

## Requirements

Namespace:
Aveva.Pdms.Database
Assembly: Aveva.Pdms.Database (in Aveva.Pdms.Database.dll)

## Methods

#### `AddGetBoolAttribute` Method (DbAttribute, DbElementType, GetBoolDelegate)

```csharp
public static void AddGetBoolAttribute( DbAttribute att , DbElementType type , GetBoolDelegate plug );
```

#### `AddGetBoolAttribute` Method (DbAttribute, GetBoolDelegate)

```csharp
public static void AddGetBoolAttribute( DbAttribute att , GetBoolDelegate plug );
```

#### `AddGetDoubleArrayAttribute` Method (DbAttribute, DbElementType, GetDoubleArrayDelegate)

```csharp
public static void AddGetDoubleArrayAttribute( DbAttribute att , DbElementType type , GetDoubleArrayDelegate plug );
```

#### `AddGetDoubleArrayAttribute` Method (DbAttribute, GetDoubleArrayDelegate)

```csharp
public static void AddGetDoubleArrayAttribute( DbAttribute att , GetDoubleArrayDelegate plug );
```

#### `AddGetDoubleAttribute` Method (DbAttribute, DbElementType, GetDoubleDelegate)

```csharp
public static void AddGetDoubleAttribute( DbAttribute att , DbElementType type , GetDoubleDelegate plug );
```

#### `AddGetDoubleAttribute` Method (DbAttribute, GetDoubleDelegate)

```csharp
public static void AddGetDoubleAttribute( DbAttribute att , GetDoubleDelegate plug );
```

#### `AddGetIntArrayAttribute` Method (DbAttribute, DbElementType, GetIntArrayDelegate)

```csharp
public static void AddGetIntArrayAttribute( DbAttribute att , DbElementType type , GetIntArrayDelegate plug );
```

#### `AddGetIntArrayAttribute` Method (DbAttribute, GetIntArrayDelegate)

```csharp
public static void AddGetIntArrayAttribute( DbAttribute att , GetIntArrayDelegate plug );
```

#### `AddGetIntAttribute` Method (DbAttribute, DbElementType, GetIntDelegate)

```csharp
public static void AddGetIntAttribute( DbAttribute att , DbElementType type , GetIntDelegate plug );
```

#### `AddGetIntAttribute` Method (DbAttribute, GetIntDelegate)

```csharp
public static void AddGetIntAttribute( DbAttribute att , GetIntDelegate plug );
```

#### `AddGetRefArrayAttribute` Method (DbAttribute, DbElementType, GetRefArrayDelegate)

```csharp
public static void AddGetRefArrayAttribute( DbAttribute att , DbElementType type , GetRefArrayDelegate plug );
```

#### `AddGetRefArrayAttribute` Method (DbAttribute, GetRefArrayDelegate)

```csharp
public static void AddGetRefArrayAttribute( DbAttribute att , GetRefArrayDelegate plug );
```

#### `AddGetRefAttribute` Method (DbAttribute, DbElementType, GetRefDelegate)

```csharp
public static void AddGetRefAttribute( DbAttribute att , DbElementType type , GetRefDelegate plug );
```

#### `AddGetRefAttribute` Method (DbAttribute, GetRefDelegate)

```csharp
public static void AddGetRefAttribute( DbAttribute att , GetRefDelegate plug );
```

#### `AddGetStringAttribute` Method (DbAttribute, DbElementType, GetStringDelegate)

```csharp
public static void AddGetStringAttribute( DbAttribute att , DbElementType type , GetStringDelegate plug );
```

#### `AddGetStringAttribute` Method (DbAttribute, GetStringDelegate)

```csharp
public static void AddGetStringAttribute( DbAttribute att , GetStringDelegate plug );
```

#### `AddSetBoolAttribute` Method

```csharp
public static void AddSetBoolAttribute( DbAttribute att , DbElementType type , SetBoolDelegate plug );
```

#### `AddSetDoubleArrayAttribute` Method

```csharp
public static void AddSetDoubleArrayAttribute( DbAttribute att , DbElementType type , SetDoubleArrayDelegate plug );
```

#### `AddSetDoubleAttribute` Method

```csharp
public static void AddSetDoubleAttribute( DbAttribute att , DbElementType type , SetDoubleDelegate plug );
```

#### `AddSetIntArrayAttribute` Method

```csharp
public static void AddSetIntArrayAttribute( DbAttribute att , DbElementType type , SetIntArrayDelegate plug );
```

#### `AddSetIntAttribute` Method

```csharp
public static void AddSetIntAttribute( DbAttribute att , DbElementType type , SetIntDelegate plug );
```

#### `AddSetRefArrayAttribute` Method

```csharp
public static void AddSetRefArrayAttribute( DbAttribute att , DbElementType type , SetRefArrayDelegate plug );
```

#### `AddSetRefAttribute` Method

```csharp
public static void AddSetRefAttribute( DbAttribute att , DbElementType type , SetRefDelegate plug );
```

#### `AddSetStringAttribute` Method

```csharp
public static void AddSetStringAttribute( DbAttribute att , DbElementType type , SetStringDelegate plug );
```

#### `RemoveGetDelegate` Method (DbAttribute)

```csharp
public static void RemoveGetDelegate( DbAttribute att );
```

#### `RemoveGetDelegate` Method (DbAttribute, DbElementType)

```csharp
public static void RemoveGetDelegate( DbAttribute att , DbElementType type );
```

#### `RemoveSetDelegate` Method

```csharp
public static void RemoveSetDelegate( DbAttribute att , DbElementType type );
```
