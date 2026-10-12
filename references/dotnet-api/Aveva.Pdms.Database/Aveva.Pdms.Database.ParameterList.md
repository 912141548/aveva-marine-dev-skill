---
title: Aveva.Pdms.Database.ParameterList Class
namespace: Aveva.Pdms.Database
assembly: Aveva.Pdms.Database
kind: Class
source: Aveva.Pdms.Database
---

# Aveva.Pdms.Database.ParameterList Class

> Representation of Parameter List. to be used for PARA and DESP attributes NOT YET IMPLEMENTED.

## Syntax

```csharp
public class ParameterList
```

## Inheritance

`System.Object` → `Aveva.Pdms.Database.ParameterList`

## Thread Safety

Public static ( Shared in Visual Basic) members of this type are
safe for multithreaded operations. Instance members are not guaranteed to be
thread-safe.

## Requirements

Namespace:
Aveva.Pdms.Database
Assembly: Aveva.Pdms.Database (in Aveva.Pdms.Database.dll)

## Constructors

#### `ParameterList` Constructor

Initializes a new instance of the ParameterList class.

```csharp
public ParameterList();
```

## Methods

#### `AsDouble` Method

Return indexed parameter in list as double

```csharp
public double AsDouble( int index );
```

**Parameters**

- **index** — Index of parameter in list

**Return Value**

Indexed parameter value as double

#### `AsInteger` Method

Return indexed parameter in list as integer.

```csharp
public double AsInteger( int index );
```

**Parameters**

- **index** — Index of parameter in list

**Return Value**

Indexed parameter value as integer

#### `AsString` Method

Return indexed parameter in list as text value.

```csharp
public string AsString( int index );
```

**Parameters**

- **index** — Index of parameter in list

**Return Value**

Indexed parameter value as text.

#### `GetParameterType` Method

Get type of indexed parameter in list.

```csharp
public DbParameterType GetParameterType( int index );
```

**Parameters**

- **index** — Index of parameter in list

#### `SetFromDouble` Method

Set the indexed parameter in the list according to double value.

```csharp
public void SetFromDouble( int index , double d );
```

**Parameters**

- **index** — Index of parameter in list
- **d** — New value as double

#### `SetFromInteger` Method

Set the indexed parameter in the list according to integer value.

```csharp
public void SetFromInteger( int index , int i );
```

**Parameters**

- **index** — Index of parameter in list
- **i** — New value as integer

#### `SetFromString` Method

Set the indexed parameter in the list according to text value.

```csharp
public void SetFromString( int index , string value );
```

**Parameters**

- **index** — Index of parameter in list
- **value** — New value as text
