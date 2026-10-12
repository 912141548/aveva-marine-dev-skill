---
title: Aveva.Pdms.Utilities.Messaging.PdmsMessage Class
namespace: Aveva.Pdms.Utilities.Messaging
assembly: Aveva.Pdms.Utilities
kind: Class
source: Aveva.Pdms.Utilities
---

# Aveva.Pdms.Utilities.Messaging.PdmsMessage Class

> PDMS application message. Every message is identified by a module number and message number. The messages are defined in separate message files. Each nessage may have a nimber of substitutions denoted by '$x' in the message. These substitutions are filled at run time.

## Syntax

```csharp
public abstract class PdmsMessage
```

## Inheritance

`System.Object` → `Aveva.Pdms.Utilities.Messaging.PdmsMessage`

## Thread Safety

Public static ( Shared in Visual Basic) members of this type are
safe for multithreaded operations. Instance members are not guaranteed to be
thread-safe.

## Requirements

Namespace:
Aveva.Pdms.Utilities.Messaging
Assembly: Aveva.Pdms.Utilities (in Aveva.Pdms.Utilities.dll)

## Properties

#### `MessageNumber` Property

message number.

```csharp
public abstract int MessageNumber {get;}
```

#### `ModuleNumber` Property

module number for message.

```csharp
public abstract int ModuleNumber {get;}
```

## Methods

#### `AddElementDelegate` Method

Add in delegate to cope with Elements- AVEVA USE ONLY.

```csharp
public static void AddElementDelegate( MessageConvert dele );
```

**Parameters**

- **dele** —

#### `AddHashDelegate` Method

Add in delegate to cope with attributes, nouns- AVEVA USE ONLY.

```csharp
public static void AddHashDelegate( MessageConvert dele );
```

**Parameters**

- **dele** —

#### `CreateMessage` Method

Creates a PDMS message.

```csharp
public static PdmsMessage CreateMessage( int module , int messagenum );
```

**Parameters**

- **module** — 
- **messagenum** —

#### `EmbedMessage` Method

Embed a message within this message.

```csharp
public abstract void EmbedMessage( PdmsMessage message );
```

**Parameters**

- **message** —

#### `EmbedMessages` Method

Embed a list of messages within this message.

```csharp
public abstract void EmbedMessages( PdmsMessage[] messages );
```

**Parameters**

- **messages** —

#### `FlushPmlErrors` Method

AVEVA USE ONLY

```csharp
public static void FlushPmlErrors();
```

#### `GetDouble` Method

Get real substitution.

```csharp
public abstract double GetDouble( int pos );
```

**Parameters**

- **pos** — substitution number

**Return Value**

double value

#### `GetElement` Method

Get Element substitution.

```csharp
public abstract IMessage GetElement( int pos );
```

**Parameters**

- **pos** — substitution number

**Return Value**

element

#### `GetHash` Method

Get attribute or element type substitution.

```csharp
public abstract IMessage GetHash( int pos );
```

**Parameters**

- **pos** — substitution number

**Return Value**

attribute / element type

#### `GetInt` Method

Get integer substitution.

```csharp
public abstract int GetInt( int pos );
```

**Parameters**

- **pos** — substitution number

**Return Value**

integer value

#### `GetLastError` Method

AVEVA USE ONLY

```csharp
public static PdmsMessage GetLastError();
```

#### `GetName` Method

Get text substitution.

```csharp
public abstract string GetName( int pos );
```

**Parameters**

- **pos** — substitution number

**Return Value**

text value

#### `MessageText` Method

Obtains message text, filling in any substitutions.

```csharp
public abstract string MessageText();
```

**Return Value**

message text

#### `Output` Method

Output a list of messages, filling in any substitutions

```csharp
public static void Output( PdmsMessage[] messages );
```

**Parameters**

- **messages** —

#### `OutputError` Method

Output message as an error, filling in any substitutions.

```csharp
public abstract void OutputError();
```

#### `Reset` Method

Unset all substitutions and remove embedded messages.

```csharp
public abstract void Reset();
```

#### `ResetErrorOccurred` Method

AVEVA USE ONLY

```csharp
public static void ResetErrorOccurred();
```

#### `RetrieveEmbeddedMessages` Method

Retrieve embedded messages.

```csharp
public abstract PdmsMessage[] RetrieveEmbeddedMessages();
```

#### `SaveLastError` Method

AVEVA USE ONLY

```csharp
public static void SaveLastError( bool save );
```

**Parameters**

- **save** —

#### `SetDouble` Method

Set real substitutions.

```csharp
public abstract void SetDouble( int pos , double val );
```

**Parameters**

- **pos** — substitution number
- **val** — double value

#### `SetElement` Method

Set Element substitutions.

```csharp
public abstract void SetElement( int pos , IMessage ele );
```

**Parameters**

- **pos** — substitution number
- **ele** — element

#### `SetHash` Method

Set attribute or element type substitutions.

```csharp
public abstract void SetHash( int pos , IMessage att );
```

**Parameters**

- **pos** — substitution number
- **att** — attribute or element type

#### `SetInt` Method

Set integer substitutions.

```csharp
public abstract void SetInt( int pos , int val );
```

**Parameters**

- **pos** — substitution number
- **val** — integer value

#### `SetName` Method

Set text substitutions.

```csharp
public abstract void SetName( int pos , object val );
```

**Parameters**

- **pos** — substitution number
- **val** — object, yielding text
