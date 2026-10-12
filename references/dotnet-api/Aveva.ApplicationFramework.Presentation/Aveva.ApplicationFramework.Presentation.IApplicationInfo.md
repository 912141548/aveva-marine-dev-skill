---
title: Aveva.ApplicationFramework.Presentation.IApplicationInfo Interface
namespace: Aveva.ApplicationFramework.Presentation
assembly: Aveva.ApplicationFramework.Presentation
kind: Interface
source: Aveva.ApplicationFramework
---

# Aveva.ApplicationFramework.Presentation.IApplicationInfo Interface

> Interface use to supply application information to the framework

## Syntax

```csharp
public interface IApplicationInfo
```

## Requirements

Namespace:
Aveva.ApplicationFramework.Presentation
Assembly: Aveva.ApplicationFramework.Presentation (in Aveva.ApplicationFramework.Presentation.dll)

## Properties

#### `AdditionalInfoDialog` Property

Return a form to display additional application specific information

```csharp
System.Windows.Forms.Form AdditionalInfoDialog {get;}
```

#### `Copyright` Property

Return the application copyright notice

```csharp
string Copyright {get;}
```

#### `License` Property

Return the application license information

```csharp
string License {get;}
```

#### `Name` Property

Return the Application Name

```csharp
string Name {get;}
```

#### `ShortName` Property

Return the Application ShortName;

```csharp
string ShortName {get;}
```

#### `Version` Property

Return the application version number

```csharp
string Version {get;}
```
