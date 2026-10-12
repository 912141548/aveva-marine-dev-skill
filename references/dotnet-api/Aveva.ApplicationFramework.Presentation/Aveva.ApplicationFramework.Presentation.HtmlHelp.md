---
title: Aveva.ApplicationFramework.Presentation.HtmlHelp Class
namespace: Aveva.ApplicationFramework.Presentation
assembly: Aveva.ApplicationFramework.Presentation
kind: Class
source: Aveva.ApplicationFramework
---

# Aveva.ApplicationFramework.Presentation.HtmlHelp Class

> A class to control Html Help viewer.

## Syntax

```csharp
public abstract class HtmlHelp
```

## Inheritance

`System.Object` → `Aveva.ApplicationFramework.Presentation.HtmlHelp`

## Thread Safety

Public static ( Shared in Visual Basic) members of this type are
safe for multithreaded operations. Instance members are not guaranteed to be
thread-safe.

## Requirements

Namespace:
Aveva.ApplicationFramework.Presentation
Assembly: Aveva.ApplicationFramework.Presentation (in Aveva.ApplicationFramework.Presentation.dll)

## Properties

#### `ContextHelpIndex` Property

Gets or sets the index file for context lookup

```csharp
public abstract string ContextHelpIndex {get; set;}
```

#### `DefaultContextAlias` Property

The default .chm alias to use for context lookups

```csharp
public abstract string DefaultContextAlias {get; set;}
```

#### `HelpAboutForm` Property

Gets or sets the form to display for help about.

```csharp
public abstract System.Windows.Forms.Form HelpAboutForm {get; set;}
```

#### `HelpFile` Property

Gets or sets the application .chm html help file

```csharp
public abstract string HelpFile {get; set;}
```

#### `HelpOnHelpFile` Property

Gets or sets the help file to use for help on help.

```csharp
public abstract string HelpOnHelpFile {get; set;}
```

#### `Instance` Property

Get instance of HtmlHelp

```csharp
public static HtmlHelp Instance {get; set;}
```

#### `OnTop` Property

Gets or sets whether the help window is owned by the application window an will allways be on top.

```csharp
public abstract bool OnTop {get; set;}
```

## Methods

#### `ShowHelpAbout` Method

Shows the help about form as a modal dialog.

```csharp
public abstract int ShowHelpAbout();
```

#### `ShowHelpALink` Method

Displays the help window at the topic with the given associative link.

```csharp
public abstract int ShowHelpALink( string aLink );
```

**Parameters**

- **aLink** —

#### `ShowHelpContents` Method

Displays the help window with the contents pane active.

```csharp
public abstract int ShowHelpContents();
```

#### `ShowHelpContext` Method (String)

Displays the help window at the topic associated with the given contextId. The help topic is determined via a lookup in the context help index.

```csharp
public abstract int ShowHelpContext( string contextId );
```

**Parameters**

- **contextId** — 

#### `ShowHelpContext` Method (String, String)

Displays the help window at the topic associated with the given contextId in the given chm file. The help topic is determined via a lookup in the context help index.

```csharp
public abstract int ShowHelpContext( string contextId , string chmAlias );
```

**Parameters**

- **contextId** — 
- **chmAlias** —

#### `ShowHelpIndex` Method

Displays the help window with the index pane active.

```csharp
public abstract int ShowHelpIndex();
```

#### `ShowHelpKeyword` Method

Displays the help window at the topic with the given keyword.

```csharp
public abstract int ShowHelpKeyword( string keyword );
```

**Parameters**

- **keyword** —

#### `ShowHelpOnHelp` Method

Show a help window for help on help if a help on help file has been specified.

```csharp
public abstract int ShowHelpOnHelp();
```

#### `ShowHelpSearch` Method

Displays the help window with the search pane active.

```csharp
public abstract int ShowHelpSearch();
```

#### `ShowOnlineLink` Method

Opens a browser window for the given url.

```csharp
public abstract void ShowOnlineLink( string url );
```

**Parameters**

- **url** — The url that will be displayed in the browser.
