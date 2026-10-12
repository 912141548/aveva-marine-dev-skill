---
title: Aveva.ApplicationFramework.Presentation.ValueListItem Class
namespace: Aveva.ApplicationFramework.Presentation
assembly: Aveva.ApplicationFramework.Presentation
kind: Class
source: Aveva.ApplicationFramework
---

# Aveva.ApplicationFramework.Presentation.ValueListItem Class

> Class representing a ValueListItem, which can be a member of ValueList.

## Syntax

```csharp
public abstract class ValueListItem
```

## Inheritance

`System.Object` → `Aveva.ApplicationFramework.Presentation.ValueListItem`

## Thread Safety

Public static ( Shared in Visual Basic) members of this type are
safe for multithreaded operations. Instance members are not guaranteed to be
thread-safe.

## Requirements

Namespace:
Aveva.ApplicationFramework.Presentation
Assembly: Aveva.ApplicationFramework.Presentation (in Aveva.ApplicationFramework.Presentation.dll)

## Properties

#### `DataValue` Property

Gets or sets the DataValue Object for this item in the ValueList.

```csharp
public abstract object DataValue {get; set;}
```

#### `DisplayText` Property

Gets or sets the text which will be displayed for this item in the ValueList.

```csharp
public abstract string DisplayText {get; set;}
```

#### `Image` Property

Gets or sets the Icon which may be displayed for this item in the ValueList.

```csharp
public abstract System.Drawing.Image Image {get; set;}
```
