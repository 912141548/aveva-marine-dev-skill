---
title: Aveva.Pdms.Shared.DatalListing Class
namespace: Aveva.Pdms.Shared
assembly: Aveva.Pdms.Shared
kind: Class
source: Aveva.Pdms.Shared
---

# Aveva.Pdms.Shared.DatalListing Class

> Summary description for DatalListing.

## Syntax

```csharp
public abstract class DatalListing
```

## Inheritance

`System.Object` → `Aveva.Pdms.Shared.DatalListing`

## Thread Safety

Public static ( Shared in Visual Basic) members of this type are
safe for multithreaded operations. Instance members are not guaranteed to be
thread-safe.

## Requirements

Namespace:
Aveva.Pdms.Shared
Assembly: Aveva.Pdms.Shared (in Aveva.Pdms.Shared.dll)

## Fields

#### `Instance` Field

Instance of Abstract class

```csharp
public static readonly DatalListing Instance;
```

## Properties

#### `changes` Property

True for Output Changes only (default false)

```csharp
public abstract bool changes {get; set;}
```

#### `Elements` Property

Array of DB Elements

```csharp
public abstract Aveva.Pdms.Database.DbElement[] Elements {get; set;}
```

#### `fileName` Property

Optional filename for output

```csharp
public abstract string fileName {get; set;}
```

#### `LocateParentInTarget` Property

If True, Output will create data under same named Parent element in Target db (default false)

```csharp
public abstract bool LocateParentInTarget {get; set;}
```

#### `ReplaceInTarget` Property

If True, Output will Replace element of same name in Target db (default false)

```csharp
public abstract bool ReplaceInTarget {get; set;}
```

#### `screen` Property

True for screen output, default false

```csharp
public abstract bool screen {get; set;}
```

#### `session` Property

Session to compare with

```csharp
public abstract int session {get; set;}
```

## Methods

#### `inputAbort` Method

INPUT ABORT event.

```csharp
public static event InputAbortEventHandler InputAbort;
```

**Event Data**

The event handler receives an argument of type DatalListingEventArgs containing data related to this event. The following DatalListingEventArgs property provides information specific to this event.
Property
Description

Elements

#### `inputBegin` Method

INPUT BEGIN event.

```csharp
public static event InputBeginEventHandler InputBegin;
```

**Event Data**

The event handler receives an argument of type DatalListingEventArgs containing data related to this event. The following DatalListingEventArgs property provides information specific to this event.
Property
Description

Elements

#### `inputEnd` Method

INPUT END event.

```csharp
public static event InputEndEventHandler InputEnd;
```

**Event Data**

The event handler receives an argument of type DatalListingEventArgs containing data related to this event. The following DatalListingEventArgs property provides information specific to this event.
Property
Description

Elements

#### `OutputListing` Method

Output Datal to File and screen

```csharp
public abstract void OutputListing();
```

#### `RaiseInputAbort` Method

Raise the INPUT ABORT event.

```csharp
public static void RaiseInputAbort( object sender , DatalListingEventArgs e );
```

**Parameters**

- **sender** — Object raising the event
- **e** — Event arguments

#### `RaiseInputBegin` Method

Raise the INPUT BEGIN event.

```csharp
public static void RaiseInputBegin( object sender , DatalListingEventArgs e );
```

**Parameters**

- **sender** — Object raising the event
- **e** — Event arguments

#### `RaiseInputEnd` Method

Raise the INPUT BEGIN event.

```csharp
public static void RaiseInputEnd( object sender , DatalListingEventArgs e );
```

**Parameters**

- **sender** — Object raising the event
- **e** — Event arguments

#### `ShowOptionsForm` Method

Show Options Form

```csharp
public abstract void ShowOptionsForm();
```

## Events

#### `InputAbort` Event

INPUT ABORT event.

```csharp
public static event InputAbortEventHandler InputAbort;
```

**Event Data**

The event handler receives an argument of type DatalListingEventArgs containing data related to this event. The following DatalListingEventArgs property provides information specific to this event.
Property
Description

Elements

#### `InputBegin` Event

INPUT BEGIN event.

```csharp
public static event InputBeginEventHandler InputBegin;
```

**Event Data**

The event handler receives an argument of type DatalListingEventArgs containing data related to this event. The following DatalListingEventArgs property provides information specific to this event.
Property
Description

Elements

#### `InputEnd` Event

INPUT END event.

```csharp
public static event InputEndEventHandler InputEnd;
```

**Event Data**

The event handler receives an argument of type DatalListingEventArgs containing data related to this event. The following DatalListingEventArgs property provides information specific to this event.
Property
Description

Elements
