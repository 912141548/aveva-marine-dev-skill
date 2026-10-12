---
title: Aveva.Pdms.Database.Project Class
namespace: Aveva.Pdms.Database
assembly: Aveva.Pdms.Database
kind: Class
source: Aveva.Pdms.Database
---

# Aveva.Pdms.Database.Project Class

> Representation of a Project.

## Syntax

```csharp
public abstract class Project
```

## Inheritance

`System.Object` → `Aveva.Pdms.Database.Project`

## Thread Safety

Public static ( Shared in Visual Basic) members of this type are
safe for multithreaded operations. Instance members are not guaranteed to be
thread-safe.

## Requirements

Namespace:
Aveva.Pdms.Database
Assembly: Aveva.Pdms.Database (in Aveva.Pdms.Database.dll)

## Fields

#### `CurrentProject` Field

```csharp
public static readonly Project CurrentProject;
```

## Properties

#### `CommunicationsDB` Property

```csharp
public Db CommunicationsDB {get;}
```

#### `GlobalDB` Property

```csharp
public abstract Db GlobalDB {get;}
```

#### `MiscellaneousDB` Property

```csharp
public Db MiscellaneousDB {get;}
```

#### `Name` Property

```csharp
public abstract string Name {get;}
```

#### `SystemDB` Property

```csharp
public abstract Db SystemDB {get;}
```

#### `Type` Property

Project type: Plant or Marine

```csharp
public abstract DbProjectType Type {get;}
```

#### `UserName` Property

```csharp
public abstract string UserName {get;}
```

## Methods

#### `Close` Method

```csharp
public abstract void Close();
```

#### `IsOpen` Method

```csharp
public abstract bool IsOpen();
```

#### `Open` Method

```csharp
public abstract bool Open( string name , string username , string password );
```

**Parameters**

- **name** — 
- **username** — 
- **password** —

#### `OpenMDB` Method

open project. (should not be static- PDC)

```csharp
public static MDB OpenMDB( MDBSetup setup );
```

**Parameters**

- **setup** —
