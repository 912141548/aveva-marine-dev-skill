---
title: Aveva.Pdms.Database.DbNameSequence Class
namespace: Aveva.Pdms.Database
assembly: Aveva.Pdms.Database
kind: Class
source: Aveva.Pdms.Database
---

# Aveva.Pdms.Database.DbNameSequence Class

> Representation of a NameSequence

## Syntax

```csharp
public abstract class DbNameSequence
```

## Inheritance

`System.Object` → `Aveva.Pdms.Database.DbNameSequence`

## Thread Safety

Public static ( Shared in Visual Basic) members of this type are
safe for multithreaded operations. Instance members are not guaranteed to be
thread-safe.

## Requirements

Namespace:
Aveva.Pdms.Database
Assembly: Aveva.Pdms.Database (in Aveva.Pdms.Database.dll)

## Methods

#### `Create` Method

Creat sequence

```csharp
public abstract bool Create();
```

**Return Value**

true or false

#### `Exist` Method

Check existance

```csharp
public abstract bool Exist();
```

**Return Value**

true or false

#### `GetCurrent` Method

Get current running number

```csharp
public abstract int GetCurrent();
```

**Return Value**

int

#### `GetDbNameSequence` Method

Create and return a new NameSequence instance.

```csharp
public static DbNameSequence GetDbNameSequence( string sequence );
```

**Parameters**

- **sequence** — Name for new NameSequence

#### `GetMax` Method

Get last running number

```csharp
public abstract int GetMax();
```

**Return Value**

int

#### `GetName` Method

Get name of sequence

```csharp
public abstract string GetName();
```

**Return Value**

string

#### `GetStep` Method

Get running number increment

```csharp
public abstract int GetStep();
```

**Return Value**

int

#### `IsWraparound` Method

Is wraparound at overflow allowed

```csharp
public abstract bool IsWraparound();
```

**Return Value**

true or false

#### `Next` Method

Next value in sequence

```csharp
public abstract string Next();
```

**Return Value**

string

#### `Remove` Method

Remove sequence

```csharp
public abstract bool Remove();
```

**Return Value**

true or false

#### `SetMax` Method

Set last running number

```csharp
public abstract bool SetMax( int max );
```

**Parameters**

- **max** — 

**Return Value**

true or false

#### `SetNoWraparound` Method

Disallow wraparound at overflow

```csharp
public abstract bool SetNoWraparound();
```

#### `SetStart` Method

Set starting point of running number

```csharp
public abstract bool SetStart( int start );
```

**Parameters**

- **start** — 

**Return Value**

true or false

#### `SetStep` Method

Set running number increment

```csharp
public abstract bool SetStep( int step );
```

**Parameters**

- **step** — 

**Return Value**

true or false

#### `SetWraparound` Method

Allow wraparound at overflow

```csharp
public abstract bool SetWraparound();
```
