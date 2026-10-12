---
title: Aveva.ApplicationFramework.Presentation.ResourceManager Class
namespace: Aveva.ApplicationFramework.Presentation
assembly: Aveva.ApplicationFramework.Presentation
kind: Class
source: Aveva.ApplicationFramework
---

# Aveva.ApplicationFramework.Presentation.ResourceManager Class

> Provides convenient access to culture-specific resources at runtime.

## Syntax

```csharp
public abstract class ResourceManager
```

## Inheritance

`System.Object` → `Aveva.ApplicationFramework.Presentation.ResourceManager`

## Thread Safety

Public static ( Shared in Visual Basic) members of this type are
safe for multithreaded operations. Instance members are not guaranteed to be
thread-safe.

## Requirements

Namespace:
Aveva.ApplicationFramework.Presentation
Assembly: Aveva.ApplicationFramework.Presentation (in Aveva.ApplicationFramework.Presentation.dll)

## Properties

#### `Instance` Property

Get instance of resource manager

```csharp
public static ResourceManager Instance {get; set;}
```

#### `ResourceSets` Property

Return a list of all loaded ResourceSets

```csharp
public abstract System.Collections.Hashtable ResourceSets {get;}
```

## Methods

#### `GetIcon` Method (String)

Gets a resource Icon.

```csharp
public abstract Icon GetIcon( string resourceID );
```

**Parameters**

- **resourceID** — Resource identifier for the required icon.

**Return Value**

A resource Icon

#### `GetIcon` Method (String, String)

Gets a resource Icon from the named resource set.

```csharp
public abstract Icon GetIcon( string resourceID , string resourceSetName );
```

**Parameters**

- **resourceID** — 
- **resourceSetName** —

#### `GetImage` Method (String)

Gets a resource Image.

```csharp
public abstract Image GetImage( string resourceID );
```

**Parameters**

- **resourceID** — Resource identifier for the required Image

**Return Value**

A resource Image

#### `GetImage` Method (String, String)

Gets a resource Image from the named resource set.

```csharp
public abstract Image GetImage( string resourceID , string resourceSetName );
```

**Parameters**

- **resourceID** — 
- **resourceSetName** — 

#### `GetImage` Method (String, String, String)

Gets a resource Image from the named resource set. Uses defaultResourceId if resourceID is not found

```csharp
public abstract Image GetImage( string resourceID , string resourceSetName , string defaultResourceID );
```

**Parameters**

- **resourceID** — 
- **resourceSetName** — 
- **defaultResourceID** —

#### `GetObject` Method (String)

Gets a resource object.

```csharp
public abstract object GetObject( string resourceID );
```

**Parameters**

- **resourceID** — Resource identifier for the required object

**Return Value**

A resource object

#### `GetObject` Method (String, String)

Gets a resource object from the named resource set.

```csharp
public abstract object GetObject( string resourceID , string resourceSetName );
```

**Parameters**

- **resourceID** — 
- **resourceSetName** —

#### `GetStandardImage` Method

Gets a standard image.

```csharp
public abstract Image GetStandardImage( StandardImage imageID );
```

**Parameters**

- **imageID** — The identification of the image to return.

**Return Value**

A standard image

#### `GetString` Method (String)

Gets a resource string.

```csharp
public abstract string GetString( string resourceID );
```

**Parameters**

- **resourceID** — Resource identifier for the required string.

**Return Value**

A resource string

#### `GetString` Method (String, String)

Gets a resource string from the named resource set.

```csharp
public abstract string GetString( string resourceID , string resourceSetName );
```

**Parameters**

- **resourceID** — 
- **resourceSetName** —

#### `LoadResourceFile` Method

Loads the resource file with given base name.

```csharp
public abstract ResourceManager LoadResourceFile( string resourceSetName );
```

**Parameters**

- **resourceSetName** —

#### `ReleaseAllResources` Method

Release all resource unlocking resource files

```csharp
public abstract void ReleaseAllResources();
```
