---
title: Aveva.Pdms.Shared.DatalListingEventArgs Class
namespace: Aveva.Pdms.Shared
assembly: Aveva.Pdms.Shared
kind: Class
source: Aveva.Pdms.Shared
---

# Aveva.Pdms.Shared.DatalListingEventArgs Class

> Event arguments for Selection Changed event.

## Syntax

```csharp
public class DatalListingEventArgs : EventArgs
```

## Inheritance

`System.Object` → `System.EventArgs` → `Aveva.Pdms.Shared.DatalListingEventArgs`

## Thread Safety

Public static ( Shared in Visual Basic) members of this type are
safe for multithreaded operations. Instance members are not guaranteed to be
thread-safe.

## Requirements

Namespace:
Aveva.Pdms.Shared
Assembly: Aveva.Pdms.Shared (in Aveva.Pdms.Shared.dll)

## Constructors

#### `DatalListingEventArgs` Constructor (Overload 1)

Constructor.

**Overload List**

Constructor.
public DatalListingEventArgs();
Constructor.
public DatalListingEventArgs(DbElement[]);

#### `DatalListingEventArgs` Constructor ()

Constructor.

```csharp
public DatalListingEventArgs();
```

#### `DatalListingEventArgs` Constructor (DbElement[])

Constructor.

```csharp
public DatalListingEventArgs( DbElement[] elements );
```

## Properties

#### `Elements` Property

```csharp
public Aveva.Pdms.Database.DbElement[] Elements {get;}
```
