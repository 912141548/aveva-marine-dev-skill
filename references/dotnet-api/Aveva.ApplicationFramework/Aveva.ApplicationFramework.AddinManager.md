---
title: Aveva.ApplicationFramework.AddinManager Class
namespace: Aveva.ApplicationFramework
assembly: Aveva.ApplicationFramework
kind: Class
source: Aveva.ApplicationFramework
---

# Aveva.ApplicationFramework.AddinManager Class

> Provides properties and methods for the management of ApplicationFramework Addins.

## Syntax

```csharp
public abstract class AddinManager
```

## Inheritance

`System.Object` → `Aveva.ApplicationFramework.AddinManager`

## Thread Safety

Public static ( Shared in Visual Basic) members of this type are
safe for multithreaded operations. Instance members are not guaranteed to be
thread-safe.

## Requirements

Namespace:
Aveva.ApplicationFramework
Assembly: Aveva.ApplicationFramework (in Aveva.ApplicationFramework.dll)

## Properties

#### `Addins` Property

Returns an AddinCollection of Addin objects

```csharp
public abstract AddinsCollection Addins {get;}
```

#### `Instance` Property

Get instance of addin manager

```csharp
public static AddinManager Instance {get; set;}
```

## Methods

#### `Load` Method

Loads the Addin defined in the specified assembly

```csharp
public abstract Addin Load( string assemblyPath );
```

**Parameters**

- **assemblyPath** — Path to assembly containing the Addin to load

#### `LoadAddins` Method

This method will attempt to load all the addins that are defined in the XML file called 'Application.Name'Addins.xml located in the same directory as the application executable.

```csharp
public abstract void LoadAddins();
```

#### `StartAddins` Method

This method iterates through the Addins collection and calls the Start method on each of the addins.

```csharp
public abstract void StartAddins();
```

#### `StopAddins` Method

This method iterates through the Addins collection and calls the Stop method on each of the addins.

```csharp
public abstract void StopAddins();
```

#### `Unload` Method

Stop the given Addin and remove it from the Addins collection

```csharp
public abstract void Unload( Addin addin );
```

**Parameters**

- **addin** — Addin to be unloaded

## Events

#### `AddinLoaded` Event

Event fired when an Addin is loaded

```csharp
public event AddinEventHandler AddinLoaded;
```

**Event Data**

The event handler receives an argument of type AddinEventArgs containing data related to this event. The following AddinEventArgs property provides information specific to this event.
Property
Description

Addin

Gets the Addin

#### `AddinStarted` Event

Event fired when an Addin is started

```csharp
public event AddinEventHandler AddinStarted;
```

**Event Data**

The event handler receives an argument of type AddinEventArgs containing data related to this event. The following AddinEventArgs property provides information specific to this event.
Property
Description

Addin

Gets the Addin

#### `AddinStarting` Event

Event fired when an Addin is starting

```csharp
public event AddinEventHandler AddinStarting;
```

**Event Data**

The event handler receives an argument of type AddinEventArgs containing data related to this event. The following AddinEventArgs property provides information specific to this event.
Property
Description

Addin

Gets the Addin

#### `AddinUnloaded` Event

Event fired when an Addin is unloaded

```csharp
public event AddinEventHandler AddinUnloaded;
```

**Event Data**

The event handler receives an argument of type AddinEventArgs containing data related to this event. The following AddinEventArgs property provides information specific to this event.
Property
Description

Addin

Gets the Addin
