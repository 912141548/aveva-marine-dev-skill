---
title: Aveva.ApplicationFramework.Presentation.UpdateOptions Enumeration
namespace: Aveva.ApplicationFramework.Presentation
assembly: Aveva.ApplicationFramework.Presentation
kind: Enumeration
source: Aveva.ApplicationFramework
---

# Aveva.ApplicationFramework.Presentation.UpdateOptions Enumeration

> Enumerations for the options for automatically updating the state of a MenuTool following state changes to an child StateButtonTool or ButtonTool. This enumeration can be treated as a bit field; that is, a set of flags. Bit fields can be combined using a bitwise OR operation.

## Syntax

```csharp
public enum UpdateOptions
```

## Members

Member Name
Description
Value

None No automatic updating. 0
Image Update image of MenuTool. 1
ToolTip Update tooltip of MenuTool. 2
Command Update associated command of MenuTool. 4
CheckedState Update Checked state of MenuTool. 8
All Update Image, Tooltip, Command and CheckedState. 15
ResetOnUncheck Restore MenuTool state after unchecking a child StateButtonTool. 16

## Requirements

Namespace:
Aveva.ApplicationFramework.Presentation
Assembly: Aveva.ApplicationFramework.Presentation (in Aveva.ApplicationFramework.Presentation.dll)
