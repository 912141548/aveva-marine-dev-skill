---
title: Aveva.ApplicationFramework.Presentation.SplashScreen Class
namespace: Aveva.ApplicationFramework.Presentation
assembly: Aveva.ApplicationFramework.Presentation
kind: Class
source: Aveva.ApplicationFramework
---

# Aveva.ApplicationFramework.Presentation.SplashScreen Class

> Provides an application SplashScreen.

## Syntax

```csharp
public abstract class SplashScreen
```

## Inheritance

`System.Object` → `Aveva.ApplicationFramework.Presentation.SplashScreen`

## Thread Safety

Public static ( Shared in Visual Basic) members of this type are
safe for multithreaded operations. Instance members are not guaranteed to be
thread-safe.

## Requirements

Namespace:
Aveva.ApplicationFramework.Presentation
Assembly: Aveva.ApplicationFramework.Presentation (in Aveva.ApplicationFramework.Presentation.dll)

## Properties

#### `Status` Property

Get or set the splashscreen status prompt.

```csharp
public abstract string Status {get; set;}
```

## Methods

#### `Close` Method

Close the splashscreen

```csharp
public abstract void Close();
```

#### `Show` Method (Image)

Display a splashscreen with the given image.

```csharp
public abstract void Show( Image image );
```

**Parameters**

- **image** — The image to display.

#### `Show` Method (String)

Display a splashscreen with the image defined by the given path or resource id

```csharp
public abstract void Show( string imagePathOrID );
```

**Parameters**

- **imagePathOrID** — The path or resource id of the image to display.

#### `Show` Method (String, IApplicationInfo)

Display a splashscreen with the image defined by the given path or resource id

```csharp
public abstract void Show( string imagePathOrID , IApplicationInfo applicationInfo );
```

**Parameters**

- **imagePathOrID** — The path or resource id of the image to display
- **applicationInfo** — Application information to display on splashscreen
