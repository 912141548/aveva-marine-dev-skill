---
title: Aveva.Pdms.Database.DbEvents.operation Enumeration
namespace: Aveva.Pdms.Database
assembly: Aveva.Pdms.Database
kind: Enumeration
source: Aveva.Pdms.Database
---

# Aveva.Pdms.Database.DbEvents.operation Enumeration

> List of potential database operations.

## Syntax

```csharp
public enum DbEvents.operation
```

## Members

Member Name
Description

op_savework Savework to DB
op_flush Flush to parent extract
op_refresh Refresh changes from parent extract
op_drop Drop changes made in extract
op_getwork Getwork changes made on DB
op_undo Undo database changes
op_redo Redo database changes
op_quit Quit database changes
op_setmark Set undo mark

## Requirements

Namespace:
Aveva.Pdms.Database
Assembly: Aveva.Pdms.Database (in Aveva.Pdms.Database.dll)
