---
title: Aveva.Pdms.Database.DbUserChanges Class
namespace: Aveva.Pdms.Database
assembly: Aveva.Pdms.Database
kind: Class
source: Aveva.Pdms.Database
---

# Aveva.Pdms.Database.DbUserChanges Class

> Representation of User Changes list Instances will be passed

## Syntax

```csharp
public abstract class DbUserChanges
```

## Inheritance

`System.Object` → `Aveva.Pdms.Database.DbUserChanges`

## Thread Safety

Public static ( Shared in Visual Basic) members of this type are
safe for multithreaded operations. Instance members are not guaranteed to be
thread-safe.

## Requirements

Namespace:
Aveva.Pdms.Database
Assembly: Aveva.Pdms.Database (in Aveva.Pdms.Database.dll)

## Methods

#### `GetCreations` Method

Get list of elements created. This only includes 'top level' creations. e.g. if you create a site and everything below it, just the site will be returned.

```csharp
public abstract DbElement[] GetCreations();
```

#### `GetDeletions` Method

Get list of elements deleted. This only includes 'top level' creations. e.g. if you delete a site and everything below it, just the site will be returned.

```csharp
public abstract DbElement[] GetDeletions();
```

#### `GetMemberChanges` Method

Return the list of elements whose member list has changed

```csharp
public abstract DbElement[] GetMemberChanges();
```

#### `GetModified` Method

Return the list of elements which have been modified

```csharp
public abstract DbElement[] GetModified();
```

#### `GetMoved` Method

Return the list of elements which have been moved (INCLUDE comman) in the database hierarchy

```csharp
public abstract DbElement[] GetMoved();
```

#### `IsAttributeModified` Method

Test if a specific attribute was modified on an element

```csharp
public abstract bool IsAttributeModified( DbElement element , DbAttribute attributeName );
```

**Parameters**

- **element** — 
- **attributeName** —
