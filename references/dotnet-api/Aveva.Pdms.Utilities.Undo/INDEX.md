---
title: Aveva.Pdms.Utilities.Undo Namespace
namespace: Aveva.Pdms.Utilities.Undo
source: Aveva.Pdms.Utilities
---

# Aveva.Pdms.Utilities.Undo Namespace

## Classes

| 类型 | 描述 |
|------|------|
| [UndoCaretaker](Aveva.Pdms.Utilities.Undo.UndoCaretaker.md) | This class registers any UndoSubscribers |
| [UndoSubscriber](Aveva.Pdms.Utilities.Undo.UndoSubscriber.md) | The UndoSubscriber class is the base class for components that participate in the undo system. To particpate in the undo system, a new class must be derived from UndoSubscriber. An instance of the class must then be registered in the system via the UndoCaretaker class. For each instance registered, the methods will be invoked as follows: For a start transaction- GetStartState() will be invoked.
For a end transaction- GetEndState() will be invoked.
For a undo- RestoreStartState() will be invoked.
For a redo- RestoreEndState() will be invoked. The states returned by GetStartState, GetEndState will be managed by the undo system |
| [UndoTransaction](Aveva.Pdms.Utilities.Undo.UndoTransaction.md) | This class is used to: a) Start and end an UndoTransaction transaction b) Static method to Clear all transactions c) Static method to denote that a significant event is about to happen |
