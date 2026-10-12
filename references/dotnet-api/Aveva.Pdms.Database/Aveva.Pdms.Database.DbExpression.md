---
title: Aveva.Pdms.Database.DbExpression Class
namespace: Aveva.Pdms.Database
assembly: Aveva.Pdms.Database
kind: Class
source: Aveva.Pdms.Database
---

# Aveva.Pdms.Database.DbExpression Class

> Representation of an Database (PML1) Expression. Methods to evaluate an expression are on DbElement

## Syntax

```csharp
public abstract class DbExpression
```

## Inheritance

`System.Object` → `Aveva.Pdms.Database.DbExpression`

## Thread Safety

Public static ( Shared in Visual Basic) members of this type are
safe for multithreaded operations. Instance members are not guaranteed to be
thread-safe.

## Requirements

Namespace:
Aveva.Pdms.Database
Assembly: Aveva.Pdms.Database (in Aveva.Pdms.Database.dll)

## Properties

#### `Type` Property

Get Expression Type.

```csharp
public abstract DbExpressionType Type {get;}
```

## Methods

#### `Clone` Method

Create and returns a copy of the Expression.

```csharp
public abstract DbExpression Clone();
```

**Return Value**

Expression copy

#### `CreateExpression` Method

Create expression from internal integer array format

```csharp
public static DbExpression CreateExpression( int[] listNet );
```

**Parameters**

- **listNet** —

#### `Equals` Method

Compare two expressions

```csharp
public abstract bool Equals( object obj );
```

**Parameters**

- **obj** —

#### `GetHashCode` Method

Returns hash code for Expression.

```csharp
public abstract int GetHashCode();
```

**Return Value**

Hash code

#### `GetStack` Method

Get internal integer array format from the Expression.

```csharp
public abstract int[] GetStack();
```

**Return Value**

Internal stack as array of integer

#### `Parse` Method

Create Expression by parsing expression text. The text may be any PML1 expression. e.g. (XLEN + 10)

```csharp
public static DbExpression Parse( string name );
```

**Parameters**

- **name** — Expression text

**Return Value**

Expression

#### `ToString` Method

Gets textual representation of Expression.

```csharp
public abstract string ToString();
```

**Return Value**

Text
