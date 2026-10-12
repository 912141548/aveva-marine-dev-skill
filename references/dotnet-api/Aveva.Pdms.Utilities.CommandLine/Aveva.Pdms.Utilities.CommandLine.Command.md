---
title: Aveva.Pdms.Utilities.CommandLine.Command Class
namespace: Aveva.Pdms.Utilities.CommandLine
assembly: Aveva.Pdms.Utilities
kind: Class
source: Aveva.Pdms.Utilities
---

# Aveva.Pdms.Utilities.CommandLine.Command Class

> Interface to PDMS command line and PML variables. AVEVA USE ONLY.

## Syntax

```csharp
public abstract class Command
```

## Inheritance

`System.Object` → `Aveva.Pdms.Utilities.CommandLine.Command`

## Thread Safety

Public static ( Shared in Visual Basic) members of this type are
safe for multithreaded operations. Instance members are not guaranteed to be
thread-safe.

## Requirements

Namespace:
Aveva.Pdms.Utilities.CommandLine
Assembly: Aveva.Pdms.Utilities (in Aveva.Pdms.Utilities.dll)

## Properties

#### `CommandString` Property

Command text

```csharp
public abstract string CommandString {get; set;}
```

#### `Error` Property

Error that occurred as a result of invoking command

```csharp
public abstract Aveva.Pdms.Utilities.Messaging.PdmsMessage Error {get;}
```

#### `Result` Property

Result of command, as would be output on the command line.

```csharp
public abstract string Result {get;}
```

## Methods

#### `CreateCommand` Method

Create a PDMS command.

```csharp
public static Command CreateCommand( string commandString );
```

**Parameters**

- **commandString** — Command text

**Return Value**

Command object

#### `FormRefresh` Method

Refresh PML forms

```csharp
public static void FormRefresh();
```

#### `GetPMLVariableBoolean` Method

Get value of PML boolean variable

```csharp
public abstract bool GetPMLVariableBoolean( string name );
```

**Parameters**

- **name** —

#### `GetPMLVariableReal` Method

Get value of PML floating point variable

```csharp
public abstract double GetPMLVariableReal( string name );
```

**Parameters**

- **name** —

#### `GetPMLVariableString` Method

Get value of PML string variable

```csharp
public abstract string GetPMLVariableString( string name );
```

**Parameters**

- **name** —

#### `Queue` Method

```csharp
public abstract void Queue();
```

#### `Run` Method

Invoke Command

```csharp
public abstract bool Run();
```

#### `RunInPdms` Method

Invoke command outputting error in PDMS rather than returning error

```csharp
public abstract bool RunInPdms();
```

#### `Update` Method

Update forms to reflect changes made. The database changes event will be fired at this point.

```csharp
public static void Update();
```
