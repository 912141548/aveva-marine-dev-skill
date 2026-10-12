---
title: Aveva.Pdms.Database.DbRawChanges Class
namespace: Aveva.Pdms.Database
assembly: Aveva.Pdms.Database
kind: Class
source: Aveva.Pdms.Database
---

# Aveva.Pdms.Database.DbRawChanges Class

> Representation of Raw Dabacon Changes. An instance of this class is passed back for certain events such as savework. In general it is better to handle changes in the 'post action', other than deletions which are best handled in the 'pre action'

## Syntax

```csharp
public abstract class DbRawChanges
```

## Inheritance

`System.Object` → `Aveva.Pdms.Database.DbRawChanges`

## Thread Safety

Public static ( Shared in Visual Basic) members of this type are
safe for multithreaded operations. Instance members are not guaranteed to be
thread-safe.

## Requirements

Namespace:
Aveva.Pdms.Database
Assembly: Aveva.Pdms.Database (in Aveva.Pdms.Database.dll)

## Methods

#### `isDeleted` Method

Tests if element has been deleted.

```csharp
public abstract bool isDeleted( DbElement element );
```

**Parameters**

- **element** —

#### `isModified` Method

Tests if element has been modified.

```csharp
public abstract bool isModified( DbElement element );
```

**Parameters**

- **element** —

#### `isTopLevelCreate` Method

Tests if element has been created.

```csharp
public abstract bool isTopLevelCreate( DbElement element );
```

**Parameters**

- **element** —

#### `isTopLevelDelete` Method

Tests if a 'top level' deletion. e.g. if you delete an equipment then the equipment is 'top level' but the owned primitives are not.

```csharp
public abstract bool isTopLevelDelete( DbElement element );
```

**Parameters**

- **element** —

#### `NextCreation` Method

Get next element created.

```csharp
public abstract DbElement NextCreation();
```

#### `NextDeletion` Method

get next element deleted.

```csharp
public abstract DbElement NextDeletion();
```

#### `NextModification` Method

get next element modified.

```csharp
public abstract DbElement NextModification();
```

#### `Reset` Method

Reset the methods 'NextCreatio', 'NextDeletion', 'NextNodification'.

```csharp
public abstract void Reset();
```
