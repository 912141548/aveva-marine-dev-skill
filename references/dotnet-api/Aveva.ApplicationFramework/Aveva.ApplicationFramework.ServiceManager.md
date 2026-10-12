---
title: Aveva.ApplicationFramework.ServiceManager Class
namespace: Aveva.ApplicationFramework
assembly: Aveva.ApplicationFramework
kind: Class
source: Aveva.ApplicationFramework
---

# Aveva.ApplicationFramework.ServiceManager Class

> Provides a means by which the various components of the ApplicationFramework (e.g. Presentation Component) can publish their services. The ServiceManager also acts as a service provider responding to requests for services.

## Syntax

```csharp
public abstract class ServiceManager : IServiceContainer , IServiceProvider
```

## Inheritance

`System.Object` → `Aveva.ApplicationFramework.ServiceManager`

## Thread Safety

Public static ( Shared in Visual Basic) members of this type are
safe for multithreaded operations. Instance members are not guaranteed to be
thread-safe.

## Requirements

Namespace:
Aveva.ApplicationFramework
Assembly: Aveva.ApplicationFramework (in Aveva.ApplicationFramework.dll)

## Properties

#### `ApplicationName` Property

Gets the name of the application.

```csharp
public abstract string ApplicationName {get;}
```

#### `Instance` Property

Get instance of service manager

```csharp
public static ServiceManager Instance {get; set;}
```

## Methods

#### `AddService` Method (Type, ServiceCreatorCallback)

Adds the specified service to the service container.

```csharp
public abstract void AddService( Type serviceType , ServiceCreatorCallback callback );
```

**Parameters**

- **serviceType** — The type of service to add.
- **callback** — A callback object that is used to create the service. This allows a service to be declared as available, but delays the creation of the object until the service is requested.

**Implements**

IServiceContainer.AddService

#### `AddService` Method (Type, ServiceCreatorCallback, Boolean)

Adds the specified service to the service container, and optionally promotes the service to parent service containers.

```csharp
public abstract void AddService( Type serviceType , ServiceCreatorCallback callback , bool promoteToParent );
```

**Parameters**

- **serviceType** — The type of service to add.
- **callback** — A callback object that is used to create the service. This allows a service to be declared as available, but delays the creation of the object until the service is requested.
- **promoteToParent** — true to promote this request to any parent service containers; otherwise, false.

**Implements**

IServiceContainer.AddService

#### `AddService` Method (Type, Object)

Adds the specified service to the ServiceManager service container.

```csharp
public abstract void AddService( Type serviceType , object service );
```

**Parameters**

- **serviceType** — The type of service to add.
- **service** — An instance of the service type to add. This object must implement or inherit from the type indicated by the serviceType parameter.

**Implements**

IServiceContainer.AddService

#### `AddService` Method (Type, Object, Boolean)

Adds the specified service to the service container, and optionally promotes the service to any parent service containers.

```csharp
public abstract void AddService( Type serviceType , object service , bool promoteToParent );
```

**Parameters**

- **serviceType** — The type of service to add.
- **service** — An instance of the service type to add. This object must implement or inherit from the type indicated by the serviceType parameter.
- **promoteToParent** — true to promote this request to any parent service containers; otherwise, false.

**Implements**

IServiceContainer.AddService

#### `GetService` Method

Gets the service object of the specified type, if it is available.

```csharp
public abstract object GetService( Type serviceType );
```

**Parameters**

- **serviceType** — The Type of the service to retrieve.

**Implements**

IServiceProvider.GetService

#### `RemoveService` Method (Type)

Removes the specified service type from the serviceManager service container.

```csharp
public abstract void RemoveService( Type serviceType );
```

**Parameters**

- **serviceType** — The type of service to remove.

**Implements**

IServiceContainer.RemoveService

#### `RemoveService` Method (Type, Boolean)

Removes the specified service type from the service container, and optionally promotes the service to parent service containers.

```csharp
public abstract void RemoveService( Type serviceType , bool removeFromParent );
```

**Parameters**

- **serviceType** — The type of service to remove.
- **removeFromParent** — true to promote this remove request to any parent service containers; otherwise, false.

**Implements**

IServiceContainer.RemoveService

## Events

#### `ServiceAdded` Event

Event raised when a service is added to the service manager

```csharp
public event ServiceEventHandler ServiceAdded;
```

**Event Data**

The event handler receives an argument of type ServiceEventArgs containing data related to this event. The following ServiceEventArgs property provides information specific to this event.
Property
Description

Service

Gets the service which was added for removed

#### `ServiceRemoved` Event

Event raised when a service is removed from the service manager

```csharp
public event ServiceEventHandler ServiceRemoved;
```

**Event Data**

The event handler receives an argument of type ServiceEventArgs containing data related to this event. The following ServiceEventArgs property provides information specific to this event.
Property
Description

Service

Gets the service which was added for removed
