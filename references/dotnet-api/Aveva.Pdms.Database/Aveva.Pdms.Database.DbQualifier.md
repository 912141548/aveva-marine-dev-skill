---
title: Aveva.Pdms.Database.DbQualifier Class
namespace: Aveva.Pdms.Database
assembly: Aveva.Pdms.Database
kind: Class
source: Aveva.Pdms.Database
---

# Aveva.Pdms.Database.DbQualifier Class

> Summary description for DbQualifier.

## Syntax

```csharp
public class DbQualifier
```

## Inheritance

`System.Object` → `Aveva.Pdms.Database.DbQualifier`

## Thread Safety

Public static ( Shared in Visual Basic) members of this type are
safe for multithreaded operations. Instance members are not guaranteed to be
thread-safe.

## Requirements

Namespace:
Aveva.Pdms.Database
Assembly: Aveva.Pdms.Database (in Aveva.Pdms.Database.dll)

## Constructors

#### `DbQualifier` Constructor

Initializes a new instance of the DbQualifier class.

```csharp
public DbQualifier();
```

## Properties

#### `attributeQualifiers` Property

```csharp
public DbAttribute[] attributeQualifiers {get; set;}
```

#### `boolQualifiers` Property

```csharp
public bool[] boolQualifiers {get; set;}
```

#### `directionQualifiers` Property

```csharp
public Aveva.Pdms.Geometry.Direction[] directionQualifiers {get; set;}
```

#### `doubleQualifiers` Property

```csharp
public double[] doubleQualifiers {get; set;}
```

#### `elementQualifiers` Property

```csharp
public DbElement[] elementQualifiers {get; set;}
```

#### `nounQualifiers` Property

```csharp
public DbElementType[] nounQualifiers {get; set;}
```

#### `orientationQualifiers` Property

```csharp
public Aveva.Pdms.Geometry.Orientation[] orientationQualifiers {get; set;}
```

#### `positionQualifiers` Property

```csharp
public Aveva.Pdms.Geometry.Position[] positionQualifiers {get; set;}
```

#### `stringQualifiers` Property

```csharp
public string[] stringQualifiers {get; set;}
```

#### `wrtQualifier` Property

```csharp
public DbElement wrtQualifier {get; set;}
```

## Methods

#### `Add` Method (DbAttribute)

add attribute qualifier.

```csharp
public void Add( DbAttribute val );
```

#### `Add` Method (DbElement)

add element qualifier.

```csharp
public void Add( DbElement val );
```

#### `Add` Method (DbElementType)

add element type qualifier.

```csharp
public void Add( DbElementType val );
```

#### `Add` Method (Direction)

add Directionn qualifier.

```csharp
public void Add( Direction val );
```

#### `Add` Method (Orientation)

add Orientation qualifier.

```csharp
public void Add( Orientation val );
```

#### `Add` Method (Position)

add Position qualifier.

```csharp
public void Add( Position val );
```

#### `Add` Method (Boolean)

add boolean qualifier.

```csharp
public void Add( bool val );
```

#### `Add` Method (Double)

add numeric qualifier.

```csharp
public void Add( double val );
```

#### `Add` Method (String)

add string qualifier.

```csharp
public void Add( string val );
```
