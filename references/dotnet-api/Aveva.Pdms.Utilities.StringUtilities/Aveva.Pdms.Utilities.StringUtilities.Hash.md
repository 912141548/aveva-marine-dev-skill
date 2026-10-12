---
title: Aveva.Pdms.Utilities.StringUtilities.Hash Class
namespace: Aveva.Pdms.Utilities.StringUtilities
assembly: Aveva.Pdms.Utilities
kind: Class
source: Aveva.Pdms.Utilities
---

# Aveva.Pdms.Utilities.StringUtilities.Hash Class

> Provides access to hash and dehash methods

## Syntax

```csharp
public abstract class Hash
```

## Inheritance

`System.Object` → `Aveva.Pdms.Utilities.StringUtilities.Hash`

## Thread Safety

Public static ( Shared in Visual Basic) members of this type are
safe for multithreaded operations. Instance members are not guaranteed to be
thread-safe.

## Requirements

Namespace:
Aveva.Pdms.Utilities.StringUtilities
Assembly: Aveva.Pdms.Utilities (in Aveva.Pdms.Utilities.dll)

## Methods

#### `CreateHash` Method

Create a PDMS Hash command.

```csharp
public static Hash CreateHash();
```

**Return Value**

Hash object

#### `hashValueToString` Method

```csharp
public abstract string hashValueToString( int Number );
```

#### `stringToHashValue` Method

```csharp
public abstract int stringToHashValue( string s );
```
