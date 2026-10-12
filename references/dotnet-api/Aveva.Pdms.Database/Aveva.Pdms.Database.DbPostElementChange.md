---
title: Aveva.Pdms.Database.DbPostElementChange Class
namespace: Aveva.Pdms.Database
assembly: Aveva.Pdms.Database
kind: Class
source: Aveva.Pdms.Database
---

# Aveva.Pdms.Database.DbPostElementChange Class

> Class to add delegates to do follow up data integrity actions. FOR USE BY AVEVA ONLY This class should only be used to ensure the data integrity of the database. To capture general database changes it is much more efficent to use the classes in DbEvents

## Syntax

```csharp
public abstract class DbPostElementChange
```

## Inheritance

`System.Object` → `Aveva.Pdms.Database.DbPostElementChange`

## Thread Safety

Public static ( Shared in Visual Basic) members of this type are
safe for multithreaded operations. Instance members are not guaranteed to be
thread-safe.

## Requirements

Namespace:
Aveva.Pdms.Database
Assembly: Aveva.Pdms.Database (in Aveva.Pdms.Database.dll)

## Methods

#### `AddPostAttributeChange` Method

Add Delegate to do post action on setting specified attribute - For AVEVA use only

```csharp
public static void AddPostAttributeChange( DbAttribute att , PostAttributeChangeDelegate plug );
```

#### `AddPostCopyElement` Method

Add Delegate to do follow up action on copying element of specific type - For AVEVA use only

```csharp
public static void AddPostCopyElement( DbElementType type , PostCopyDelegate plug );
```

#### `AddPostCreateElement` Method

Add Delegate to do follow up action on creating element of specific type- For AVEVA use only

```csharp
public static void AddPostCreateElement( DbElementType type , PostCreateDelegate plug );
```

#### `AddPostMoveElement` Method

Add Delegate to do post action on moving element(i.e. INCLUDE) of given type - For AVEVA use only

```csharp
public static void AddPostMoveElement( DbElementType type , PostMoveDelegate plug );
```

#### `AddPostRefAttributeChange` Method

Add Delegate to do post action on setting specified ref attribute - For AVEVA use only

```csharp
public static void AddPostRefAttributeChange( DbAttribute att , PostRefAttributeChangeDelegate plug );
```

#### `AddPostRefListAttributeChange` Method

Add Delegate to do post action on setting specified ref array attribute - For AVEVA use only

```csharp
public static void AddPostRefListAttributeChange( DbAttribute att , PostRefListAttributeChangeDelegate plug );
```

#### `AddPreDeleteElement` Method (DbElementType, PreDeleteDelegate)

Add Delegate to do pre action on deleting element of specific type- For AVEVA use only

```csharp
public static void AddPreDeleteElement( DbElementType type , PreDeleteDelegate plug );
```

#### `AddPreDeleteElement` Method (PreDeleteDelegate)

Add Delegate to do pre action on any element deletion- For AVEVA use only

```csharp
public static void AddPreDeleteElement( PreDeleteDelegate plug );
```
