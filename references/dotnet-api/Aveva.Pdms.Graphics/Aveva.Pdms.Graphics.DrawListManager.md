---
title: Aveva.Pdms.Graphics.DrawListManager Class
namespace: Aveva.Pdms.Graphics
assembly: Aveva.Pdms.Graphics
kind: Class
source: Aveva.Pdms.Graphics
---

# Aveva.Pdms.Graphics.DrawListManager Class

> Summary description for DrawListManager.

## Syntax

```csharp
public abstract class DrawListManager
```

## Inheritance

`System.Object` → `Aveva.Pdms.Graphics.DrawListManager`

## Thread Safety

Public static ( Shared in Visual Basic) members of this type are
safe for multithreaded operations. Instance members are not guaranteed to be
thread-safe.

## Requirements

Namespace:
Aveva.Pdms.Graphics
Assembly: Aveva.Pdms.Graphics (in Aveva.Pdms.Graphics.dll)

## Fields

#### `Instance` Field

```csharp
public static readonly DrawListManager Instance;
```

## Properties

#### `CurrentDrawList` Property

```csharp
public abstract DrawList CurrentDrawList {get;}
```

## Methods

#### `FireChangedEvent` Method

```csharp
public static void FireChangedEvent( DrawListEventArgs e );
```

#### `getDrawList` Method

```csharp
public abstract DrawList getDrawList( int viewWindowId );
```

**Parameters**

- **viewWindowId** —

## Events

#### `Changed` Event

```csharp
public static event DrawListEventHandler Changed;
```

**Event Data**

The event handler receives an argument of type DrawListEventArgs containing data related to this event. The following DrawListEventArgs property provides information specific to this event.
Property
Description

EventType
