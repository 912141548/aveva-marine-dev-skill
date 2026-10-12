---
title: Aveva.Pdms.Database.DbEvents Class
namespace: Aveva.Pdms.Database
assembly: Aveva.Pdms.Database
kind: Class
source: Aveva.Pdms.Database
---

# Aveva.Pdms.Database.DbEvents Class

> This class contains the mechanisms for subscribing to database events: It covers project open, mdb open, mdb close, savework, getwork, undo, redo, flush, refresh, drop plus capturing general database changes. It does not cover legality checkers for operations on elements. The delegates are organised by type of operation rather than specific ones for each operation e.g. there is a single callback to cover all opeartions(undo, redo, getwork, quit) that changes the user's current viewed data

## Syntax

```csharp
public class DbEvents
```

## Inheritance

`System.Object` → `Aveva.Pdms.Database.DbEvents`

## Thread Safety

Public static ( Shared in Visual Basic) members of this type are
safe for multithreaded operations. Instance members are not guaranteed to be
thread-safe.

## Requirements

Namespace:
Aveva.Pdms.Database
Assembly: Aveva.Pdms.Database (in Aveva.Pdms.Database.dll)

## Constructors

#### `DbEvents` Constructor

Initializes a new instance of the DbEvents class.

```csharp
public DbEvents();
```

## Methods

#### `AddClaimedEventHandler` Method

Add delegate to capture claim actions

```csharp
public static void AddClaimedEventHandler( ClaimEventHandler h );
```

**Parameters**

- **h** —

#### `AddClearCacheEventHandler` Method

Add delegate to clear any cached data. This will be called after doing a temporary switch to a different session in a DB, or after doing a getwork, undo, redo, quit. N.B. ClearCache may be called 1000s of times within a single operation. Thus any handlers must be fast.

```csharp
public static void AddClearCacheEventHandler( SimpleEventHandler h );
```

**Parameters**

- **h** —

#### `AddCommitPendingEventHandler` Method

Add delegate to commit any pending DB changes prior to savework, setmark, undo, redo, quit, getwork

```csharp
public static void AddCommitPendingEventHandler( CommitEventHandler h );
```

**Parameters**

- **h** —

#### `AddDBFileChangedEventHandler` Method

Add post event delegate to capture changes made to the database file. Operations are Savework, Flush, Refresh, or drop

```csharp
public static void AddDBFileChangedEventHandler( ChangeEventHandler h );
```

**Parameters**

- **h** —

#### `AddDBFileChangesAllowed` Method

Add delegate to check if operation is allowed

```csharp
public static void AddDBFileChangesAllowed( BoolChangeEventHandler h );
```

**Parameters**

- **h** —

#### `AddDBFileChangingEventHandler` Method

Add pre event delegate to capture changes made to the database file. Operations are Savework, Flush, Refresh, or drop

```csharp
public static void AddDBFileChangingEventHandler( ChangeEventHandler h );
```

**Parameters**

- **h** —

#### `AddFailedEventHandler` Method

Add delegate to capture failures at savework

```csharp
public static void AddFailedEventHandler( FailureEventHandler h );
```

**Parameters**

- **h** —

#### `AddHandleUserChanges` Method

Add delegate to capture all database changes made by user. For performance reasons, this event is only raised when focus is returned to the end user. e.g. at the end of running a PML macro, or after hitting the 'Apply' button. Internally a list of changes is built up. This list is then passed to the subscribers.

```csharp
public static void AddHandleUserChanges( UserChangesEventHandler h );
```

**Parameters**

- **h** —

#### `AddLocalChangedEventHandler` Method

Add post event delegate to capture changes made to user's current view. Operations are getwork, undo, redo, quit

```csharp
public static void AddLocalChangedEventHandler( ChangeEventHandler h );
```

**Parameters**

- **h** —

#### `AddLocalChangingEventHandler` Method

Add pre event delegate to capture changes made to user's current view. Operations are getwork, undo, redo, quit

```csharp
public static void AddLocalChangingEventHandler( ChangeEventHandler h );
```

**Parameters**

- **h** —

#### `AddReleasedEventHandler` Method

Add delegate to capture release (unclaim) actions

```csharp
public static void AddReleasedEventHandler( ClaimEventHandler h );
```

**Parameters**

- **h** —
