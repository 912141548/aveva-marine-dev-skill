---
title: Aveva.ApplicationFramework.Presentation.DropDownArrowStyle Enumeration
namespace: Aveva.ApplicationFramework.Presentation
assembly: Aveva.ApplicationFramework.Presentation
kind: Enumeration
source: Aveva.ApplicationFramework
---

# Aveva.ApplicationFramework.Presentation.DropDownArrowStyle Enumeration

> Enumerator used to specify the style used to draw a popup tool's dropdown arrow. Also determines which part of the tool should be clicked to drop down the tool.

## Syntax

```csharp
public enum DropDownArrowStyle
```

## Members

Member Name
Description

Default The tool is displayed in its default style.
None No dropdown arrow is displayed.
Segmented A standard downward-pointing dropdown arrow is displayed to the right of the tool's image and/or text in a separate boxed-off area when on a toolbar and a standard right-pointing arrow with a dividing line to the left of it is displayed when on a menu. Clicking on the arrow drops down the tool. Clicking on the image and/or text area fires the ToolClick event.
SegmentedStateButton A standard downward-pointing dropdown arrow is displayed to the right of the tool's image and/or text in a separate boxed-off area when on a toolbar and a standard right-pointing arrow with a dividing line to the left of it is displayed when on a menu. Clicking on the arrow drops down the tool. Clicking on the image and/or text area fires the ToolClick event and toggles the Checked state.
Standard A standard downward-pointing dropdown arrow is displayed to the right of the tool's image and/or text when on a toolbar, and a standard right-pointing arrow is displayed when on a menu.

## Requirements

Namespace:
Aveva.ApplicationFramework.Presentation
Assembly: Aveva.ApplicationFramework.Presentation (in Aveva.ApplicationFramework.Presentation.dll)
