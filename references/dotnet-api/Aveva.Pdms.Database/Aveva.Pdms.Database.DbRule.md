---
title: Aveva.Pdms.Database.DbRule Class
namespace: Aveva.Pdms.Database
assembly: Aveva.Pdms.Database
kind: Class
source: Aveva.Pdms.Database
---

# Aveva.Pdms.Database.DbRule Class

> Representation of a Rule.

## Syntax

```csharp
public abstract class DbRule
```

## Inheritance

`System.Object` → `Aveva.Pdms.Database.DbRule`

## Thread Safety

Public static ( Shared in Visual Basic) members of this type are
safe for multithreaded operations. Instance members are not guaranteed to be
thread-safe.

## Requirements

Namespace:
Aveva.Pdms.Database
Assembly: Aveva.Pdms.Database (in Aveva.Pdms.Database.dll)

## Properties

#### `RuleExpression` Property

Expression associated with Rule

```csharp
public abstract DbExpression RuleExpression {get; set;}
```

#### `Status` Property

Status of Rule

```csharp
public abstract DbRuleStatus Status {get; set;}
```

#### `Type` Property

Expression Type of Rule

```csharp
public abstract DbExpressionType Type {get; set;}
```

## Methods

#### `Clone` Method

Creates and returns a copy of the Rule.

```csharp
public abstract DbRule Clone();
```

**Return Value**

Rule copy

#### `CreateDbRule` Method

Create rule

```csharp
public static DbRule CreateDbRule( DbExpression expression , DbRuleStatus status , DbExpressionType type );
```

**Parameters**

- **expression** — 
- **status** — 
- **type** —

#### `Equals` Method

Test for equality of two rules

```csharp
public abstract bool Equals( object obj );
```

**Parameters**

- **obj** —

#### `GetHashCode` Method

Get hash code for Rule, overriding Object.GetHashCode.

```csharp
public abstract int GetHashCode();
```

**Return Value**

Hash code

#### `ToString` Method

Gets textual representation of Rule.

```csharp
public abstract string ToString();
```

**Return Value**

Text
