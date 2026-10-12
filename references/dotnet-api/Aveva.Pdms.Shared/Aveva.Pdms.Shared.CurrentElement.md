---
title: Aveva.Pdms.Shared.CurrentElement Class
namespace: Aveva.Pdms.Shared
assembly: Aveva.Pdms.Shared
kind: Class
source: Aveva.Pdms.Shared
---

# Aveva.Pdms.Shared.CurrentElement Class

## Syntax

```csharp
public abstract class CurrentElement
```

## Inheritance

`System.Object` → `Aveva.Pdms.Shared.CurrentElement`

## Thread Safety

Public static ( Shared in Visual Basic) members of this type are
safe for multithreaded operations. Instance members are not guaranteed to be
thread-safe.

## Requirements

Namespace:
Aveva.Pdms.Shared
Assembly: Aveva.Pdms.Shared (in Aveva.Pdms.Shared.dll)

## Properties

#### `Element` Property

Current Element (CE).

```csharp
public static Aveva.Pdms.Database.DbElement Element {get; set;}
```

## Methods

#### `RaiseCurrentElementChanged` Method

Raise the Current Element Changed event.

```csharp
public static void RaiseCurrentElementChanged( object sender , CurrentElementChangedEventArgs e );
```

**Parameters**

- **sender** — Object raising the event
- **e** — Event arguments

## Events

#### `CurrentElementChanged` Event

Current Element Changed event.

```csharp
public static event CurrentElementChangedEventHandler CurrentElementChanged;
```

**Event Data**

The event handler receives an argument of type CurrentElementChangedEventArgs containing data related to this event. The following CurrentElementChangedEventArgs property provides information specific to this event.
Property
Description

Element

Element associated with event.
