---
title: Aveva.Pdms.Database.DbSession Class
namespace: Aveva.Pdms.Database
assembly: Aveva.Pdms.Database
kind: Class
source: Aveva.Pdms.Database
---

# Aveva.Pdms.Database.DbSession Class

> Class to return details about a particular Dabacon session.

## Syntax

```csharp
public abstract class DbSession
```

## Inheritance

`System.Object` → `Aveva.Pdms.Database.DbSession`

## Thread Safety

Public static ( Shared in Visual Basic) members of this type are
safe for multithreaded operations. Instance members are not guaranteed to be
thread-safe.

## Requirements

Namespace:
Aveva.Pdms.Database
Assembly: Aveva.Pdms.Database (in Aveva.Pdms.Database.dll)

## Properties

#### `Date` Property

Date of session

```csharp
public abstract System.DateTime Date {get;}
```

#### `Description` Property

Description of session

```csharp
public abstract string Description {get;}
```

#### `Extract` Property

Extract number

```csharp
public abstract int Extract {get; set;}
```

#### `IsValid` Property

Is this session object valid

```csharp
public abstract bool IsValid {get;}
```

#### `PreviousSession` Property

Previous session

```csharp
public abstract DbSession PreviousSession {get;}
```

#### `Primary` Property

Is the session primary

```csharp
public abstract bool Primary {get;}
```

#### `SessionNumber` Property

Session number

```csharp
public abstract int SessionNumber {get; set;}
```

#### `User` Property

User that created the session

```csharp
public abstract string User {get;}
```

## Methods

#### `ToString` Method

```csharp
public override string ToString();
```
