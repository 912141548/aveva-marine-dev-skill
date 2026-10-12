---
title: Aveva.ApplicationFramework.SettingsManager Class
namespace: Aveva.ApplicationFramework
assembly: Aveva.ApplicationFramework
kind: Class
source: Aveva.ApplicationFramework
---

# Aveva.ApplicationFramework.SettingsManager Class

> Class to manage an applications settings

## Syntax

```csharp
public abstract class SettingsManager
```

## Inheritance

`System.Object` → `Aveva.ApplicationFramework.SettingsManager`

## Thread Safety

Public static ( Shared in Visual Basic) members of this type are
safe for multithreaded operations. Instance members are not guaranteed to be
thread-safe.

## Requirements

Namespace:
Aveva.ApplicationFramework
Assembly: Aveva.ApplicationFramework (in Aveva.ApplicationFramework.dll)

## Properties

#### `Directory` Property

Sets the parent directory into which the settings will be serialized. The defaults to C:\Documents and Settings\'User Name'\Local Settings\Application Data\Aveva\'Application Name'

```csharp
public abstract string Directory {get; set;}
```

#### `Instance` Property

Get instance of settings manager

```csharp
public static SettingsManager Instance {get; set;}
```

#### `SettingsGroups` Property

Gets the collection of SettingsGroups

```csharp
public abstract SettingsGroupsCollection SettingsGroups {get;}
```

## Methods

#### `AddGroup` Method

Adds a new SettingsGroup with the given name.

```csharp
public abstract SettingsGroup AddGroup( string groupName , string directory );
```

**Parameters**

- **groupName** — Name of SettingsGroup
- **directory** — The name of the directory where this settings group is saved

#### `LoadSettings` Method

Loads the settings from serialized data.

```csharp
public abstract void LoadSettings();
```

#### `SaveSettings` Method

Saves the settings.

```csharp
public abstract void SaveSettings();
```
