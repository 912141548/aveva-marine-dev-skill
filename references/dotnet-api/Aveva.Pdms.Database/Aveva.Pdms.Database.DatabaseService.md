---
title: Aveva.Pdms.Database.DatabaseService Class
namespace: Aveva.Pdms.Database
assembly: Aveva.Pdms.Database
kind: Class
source: Aveva.Pdms.Database
---

# Aveva.Pdms.Database.DatabaseService Class

> Class to open a project

## Syntax

```csharp
public abstract class DatabaseService
```

## Inheritance

`System.Object` → `Aveva.Pdms.Database.DatabaseService`

## Thread Safety

Public static ( Shared in Visual Basic) members of this type are
safe for multithreaded operations. Instance members are not guaranteed to be
thread-safe.

## Requirements

Namespace:
Aveva.Pdms.Database
Assembly: Aveva.Pdms.Database (in Aveva.Pdms.Database.dll)

## Methods

#### `OpenProject` Method

Open a projects

```csharp
public static Project OpenProject( string name , string username , string password );
```

**Parameters**

- **name** — Project name
- **username** — User name
- **password** — User password

**Return Value**

New Project

#### `RaiseChanges` Method

Deprecated - do not use

```csharp
public static void RaiseChanges( object sender , DbChangesEventArgs e );
```

**Parameters**

- **sender** — Origin object
- **e** — Event arguments

#### `RaiseClaim` Method

Deprecated - do not use

```csharp
public static void RaiseClaim( object sender , DbClaimEventArgs e );
```

**Parameters**

- **sender** — Origin object
- **e** — Event arguments

#### `RaiseMDBClosed` Method

Raise MDB Closed event- This will be replaced by mechanisms in DbEvents

```csharp
public static void RaiseMDBClosed( object sender , EventArgs e );
```

**Parameters**

- **sender** — Origin object
- **e** — Event arguments

#### `RaiseMDBClosing` Method

Deprecated - do not use

```csharp
public static void RaiseMDBClosing( object sender , EventArgs e );
```

**Parameters**

- **sender** — Origin object
- **e** — Event arguments

#### `RaiseMDBOpened` Method

Deprecated - do not use

```csharp
public static void RaiseMDBOpened( object sender , EventArgs e );
```

**Parameters**

- **sender** — Origin object
- **e** — Event arguments

#### `RaisePostGetWork` Method

Deprecated- do not use

```csharp
public static void RaisePostGetWork( object sender , DbGetWorkChangesEventArgs e );
```

**Parameters**

- **sender** — Origin object
- **e** — Event arguments

#### `RaisePostOpenProject` Method

Deprecated- do not use

```csharp
public static void RaisePostOpenProject( object sender , EventArgs e );
```

**Parameters**

- **sender** — Origin object
- **e** — Event arguments

#### `RaisePostRedo` Method

Deprecated- do not use

```csharp
public static void RaisePostRedo( object sender , DbUndoChangesEventArgs e );
```

**Parameters**

- **sender** — Origin object
- **e** — Event arguments

#### `RaisePostUndo` Method

Deprecated- do not use

```csharp
public static void RaisePostUndo( object sender , DbUndoChangesEventArgs e );
```

**Parameters**

- **sender** — Origin object
- **e** — Event arguments

#### `RaisePreGetWork` Method

Deprecated- do not use

```csharp
public static void RaisePreGetWork( object sender , DbGetWorkChangesEventArgs e );
```

**Parameters**

- **sender** — Origin object
- **e** — Event arguments

#### `RaisePreRedo` Method

Deprecated- do not use

```csharp
public static void RaisePreRedo( object sender , DbUndoChangesEventArgs e );
```

**Parameters**

- **sender** — Origin object
- **e** — Event arguments

#### `RaisePreUndo` Method

Deprecated- do not use

```csharp
public static void RaisePreUndo( object sender , DbUndoChangesEventArgs e );
```

**Parameters**

- **sender** — Origin object
- **e** — Event arguments

#### `RaiseRelease` Method

Deprecated- do not use

```csharp
public static void RaiseRelease( object sender , DbClaimEventArgs e );
```

**Parameters**

- **sender** — Origin object
- **e** — Event arguments

## Events

#### `Changes` Event

Changes event- Deprecated, use DbEvents.AddHandleUserChanges to add a delegate

```csharp
public static event DbChangesEventHandler Changes;
```

**Event Data**

The event handler receives an argument of type DbChangesEventArgs containing data related to this event. The following DbChangesEventArgs property provides information specific to this event.
Property
Description

ChangeList

User change list.

#### `Claim` Event

Deprecated - use DbEvents.AddClaimedEventHandler to add a delegate

```csharp
public static event DbClaimEventHandler Claim;
```

**Event Data**

The event handler receives an argument of type DbClaimEventArgs containing data related to this event. The following DbClaimEventArgs property provides information specific to this event.
Property
Description

Element

Element relating to claim event.

#### `MDBClosed` Event

MDB Closed event- This will be replaced by mechanisms in DbEvents

```csharp
public static event EventHandler MDBClosed;
```

#### `MDBClosing` Event

MDB Closing event- This will be replaced by mechanisms in DbEvents

```csharp
public static event EventHandler MDBClosing;
```

#### `MDBOpened` Event

MDB Opened event- This will be replaced by mechanisms in DbEvents

```csharp
public static event EventHandler MDBOpened;
```

#### `PostGetWork` Event

Deprecated - use DbEvents.AddLocalChangedEventHandler

```csharp
public static event DbGetWorkEventHandler PostGetWork;
```

**Event Data**

The event handler receives an argument of type DbGetWorkChangesEventArgs containing data related to this event. The following DbGetWorkChangesEventArgs properties provide information specific to this event.
Property
Description

ChangeList

Raw change list

DB

Database

NewSessionNumber

New session number

PreviousSessionNumber

Previous session number

#### `PostOpenProject` Event

Project opened event- This will be replaced by a mechanism in the DbEvents class

```csharp
public static event EventHandler PostOpenProject;
```

#### `PostRedo` Event

Deprecated - use DbEvents.AddLocalChangingEventHandler

```csharp
public static event DbUndoEventHandler PostRedo;
```

**Event Data**

The event handler receives an argument of type DbUndoChangesEventArgs containing data related to this event. The following DbUndoChangesEventArgs properties provide information specific to this event.
Property
Description

ChangeList

MarkNumber

#### `PostUndo` Event

Deprecated - use DbEvents.AddLocalChangedEventHandler

```csharp
public static event DbUndoEventHandler PostUndo;
```

**Event Data**

The event handler receives an argument of type DbUndoChangesEventArgs containing data related to this event. The following DbUndoChangesEventArgs properties provide information specific to this event.
Property
Description

ChangeList

MarkNumber

#### `PreGetWork` Event

Deprecated - use DbEvents.AddLocalChangingEventHandler

```csharp
public static event DbGetWorkEventHandler PreGetWork;
```

**Event Data**

The event handler receives an argument of type DbGetWorkChangesEventArgs containing data related to this event. The following DbGetWorkChangesEventArgs properties provide information specific to this event.
Property
Description

ChangeList

Raw change list

DB

Database

NewSessionNumber

New session number

PreviousSessionNumber

Previous session number

#### `PreRedo` Event

Deprecated - use DbEvents.AddLocalChangingEventHandler

```csharp
public static event DbUndoEventHandler PreRedo;
```

**Event Data**

The event handler receives an argument of type DbUndoChangesEventArgs containing data related to this event. The following DbUndoChangesEventArgs properties provide information specific to this event.
Property
Description

ChangeList

MarkNumber

#### `PreUndo` Event

Deprecated - use DbEvents.AddLocalChangingEventHandler

```csharp
public static event DbUndoEventHandler PreUndo;
```

**Event Data**

The event handler receives an argument of type DbUndoChangesEventArgs containing data related to this event. The following DbUndoChangesEventArgs properties provide information specific to this event.
Property
Description

ChangeList

MarkNumber

#### `Release` Event

Deprecated - use DbEvents.AddClaimedEventHandler

```csharp
public static event DbClaimEventHandler Release;
```

**Event Data**

The event handler receives an argument of type DbClaimEventArgs containing data related to this event. The following DbClaimEventArgs property provides information specific to this event.
Property
Description

Element

Element relating to claim event.
