---
title: Aveva.ApplicationFramework.Presentation Namespace
namespace: Aveva.ApplicationFramework.Presentation
source: Aveva.ApplicationFramework
---

# Aveva.ApplicationFramework.Presentation Namespace

## Classes

| 类型 | 描述 |
|------|------|
| [ButtonTool](Aveva.ApplicationFramework.Presentation.ButtonTool.md) | Represents a ButtonToolt. |
| [CancelClosingEventArgs](Aveva.ApplicationFramework.Presentation.CancelClosingEventArgs.md) | Provides data for a cancelable event. |
| [ComboBoxTool](Aveva.ApplicationFramework.Presentation.ComboBoxTool.md) | Represents a ComboBoxTool. |
| [Command](Aveva.ApplicationFramework.Presentation.Command.md) | Abstract base class which an application must inherit from to create a Command object |
| [CommandBar](Aveva.ApplicationFramework.Presentation.CommandBar.md) | Class to represent a CommandBar. |
| [CommandBarEventArgs](Aveva.ApplicationFramework.Presentation.CommandBarEventArgs.md) | Provides data for the CommandBarAdded and CommandBarRemoved events. |
| [CommandBarManager](Aveva.ApplicationFramework.Presentation.CommandBarManager.md) | Class representing a CommandBarManager. |
| [CommandBarsCollection](Aveva.ApplicationFramework.Presentation.CommandBarsCollection.md) | Class to represent a CommandBarCollection. |
| [CommandEventArgs](Aveva.ApplicationFramework.Presentation.CommandEventArgs.md) | Provides data for the CommandAdded and CommandRemoved events. |
| [CommandExecutor](Aveva.ApplicationFramework.Presentation.CommandExecutor.md) | Abstract base class which an application must inherit from to create a CommandExecutor object. |
| [CommandList](Aveva.ApplicationFramework.Presentation.CommandList.md) | An ArrayList use for the list property of Command objects which supports an IsModified property. |
| [CommandManager](Aveva.ApplicationFramework.Presentation.CommandManager.md) | Class representing a CommandManager. |
| [CommandsCollection](Aveva.ApplicationFramework.Presentation.CommandsCollection.md) | Class that represents a CommandCollection. |
| [CommandTypesCollection](Aveva.ApplicationFramework.Presentation.CommandTypesCollection.md) | Class that represents a CommandCollection. |
| [ContainerTool](Aveva.ApplicationFramework.Presentation.ContainerTool.md) | A tool that contains a Control. |
| [DockedWindow](Aveva.ApplicationFramework.Presentation.DockedWindow.md) | Class to represent a DockedWindow. |
| [DragDropDirector](Aveva.ApplicationFramework.Presentation.DragDropDirector.md) | A class to help direct drag-drop events. |
| [DropTarget](Aveva.ApplicationFramework.Presentation.DropTarget.md) | A class to represent a DragDropTarget. |
| [DropTargetEventArgs](Aveva.ApplicationFramework.Presentation.DropTargetEventArgs.md) | A class to provide information to for drop-drop events. |
| [FontListTool](Aveva.ApplicationFramework.Presentation.FontListTool.md) | Represents a FontListTool. |
| [HtmlHelp](Aveva.ApplicationFramework.Presentation.HtmlHelp.md) | A class to control Html Help viewer. |
| [LabelTool](Aveva.ApplicationFramework.Presentation.LabelTool.md) | Class to represent a static Label. |
| [ListTool](Aveva.ApplicationFramework.Presentation.ListTool.md) | Represents a ListTool. |
| [MdiWindow](Aveva.ApplicationFramework.Presentation.MdiWindow.md) | Represents an MDI style window or dialog box. |
| [MdiWindowListTool](Aveva.ApplicationFramework.Presentation.MdiWindowListTool.md) | Class to respresent the special tool which displays a list of current MDI Windows. |
| [MenuTool](Aveva.ApplicationFramework.Presentation.MenuTool.md) | Represents a MenuTool. |
| [PopupColorPickerTool](Aveva.ApplicationFramework.Presentation.PopupColorPickerTool.md) | Represents a PopupColorPicker. |
| [PopupContainerTool](Aveva.ApplicationFramework.Presentation.PopupContainerTool.md) | Represents a PopuplContainerTool. |
| [ResourceManager](Aveva.ApplicationFramework.Presentation.ResourceManager.md) | Provides convenient access to culture-specific resources at runtime. |
| [ResourceSet](Aveva.ApplicationFramework.Presentation.ResourceSet.md) | Represent a set of culture-specific resource files. |
| [RootToolsCollection](Aveva.ApplicationFramework.Presentation.RootToolsCollection.md) | Class representing a RootToolsCollection. |
| [SplashScreen](Aveva.ApplicationFramework.Presentation.SplashScreen.md) | Provides an application SplashScreen. |
| [StateButtonTool](Aveva.ApplicationFramework.Presentation.StateButtonTool.md) | Represents a StateButtonTool. |
| [StatusBar](Aveva.ApplicationFramework.Presentation.StatusBar.md) | Represents a Windows style status bar control. |
| [StatusBarPanelsCollection](Aveva.ApplicationFramework.Presentation.StatusBarPanelsCollection.md) | Represents a collection of status bar panels. |
| [StatusBarTextPanel](Aveva.ApplicationFramework.Presentation.StatusBarTextPanel.md) | Represents a StatusBarTextPanel. |
| [TaskBar](Aveva.ApplicationFramework.Presentation.TaskBar.md) | Class representing a Microsoft Office style "TaskPane" type toolbar. |
| [TaskPaneTool](Aveva.ApplicationFramework.Presentation.TaskPaneTool.md) | Class used to represent a single item in a TaskPane. |
| [TextBoxTool](Aveva.ApplicationFramework.Presentation.TextBoxTool.md) | Represents a TextBoxTool. |
| [ThemeColours](Aveva.ApplicationFramework.Presentation.ThemeColours.md) | Class which provides a number of Theme colours |
| [ToolEventArgs](Aveva.ApplicationFramework.Presentation.ToolEventArgs.md) | Provides information for Tool events. |
| [ToolsCollection](Aveva.ApplicationFramework.Presentation.ToolsCollection.md) | Class representing a ToolsCollection. |
| [ValueList](Aveva.ApplicationFramework.Presentation.ValueList.md) | Class representing a ValueList, which is a collection of ValueListItem objects. It is typicall assigned to a ComboBoxTool as the list of options displayed as the dropdown list. |
| [ValueListItem](Aveva.ApplicationFramework.Presentation.ValueListItem.md) | Class representing a ValueListItem, which can be a member of ValueList. |
| [WindowEventArgs](Aveva.ApplicationFramework.Presentation.WindowEventArgs.md) | Provides data for the WindowAdded event. |
| [WindowManager](Aveva.ApplicationFramework.Presentation.WindowManager.md) | Provides access to window related facilities. |
| [WindowsCollection](Aveva.ApplicationFramework.Presentation.WindowsCollection.md) | Provides access to a collection of application windows. |

## Interfaces

| 类型 | 描述 |
|------|------|
| [IApplicationInfo](Aveva.ApplicationFramework.Presentation.IApplicationInfo.md) | Interface use to supply application information to the framework |
| [IStatusBarPanel](Aveva.ApplicationFramework.Presentation.IStatusBarPanel.md) | Interface supported by Statusbar panels. |
| [ITool](Aveva.ApplicationFramework.Presentation.ITool.md) | Interface supported by all Tool clases. |
| [IWindow](Aveva.ApplicationFramework.Presentation.IWindow.md) | Interface supported by supported window types(MDI, Docked). |

## Delegates

| 类型 | 描述 |
|------|------|
| [CommandBarEventHandler](Aveva.ApplicationFramework.Presentation.CommandBarEventHandler.md) | Represents the method that will handle CommandBar related events. |
| [CommandEventHandler](Aveva.ApplicationFramework.Presentation.CommandEventHandler.md) | Represents the method that will handle command related events. |
| [DropTargetEventHandler](Aveva.ApplicationFramework.Presentation.DropTargetEventHandler.md) | Represents the method that will handle DropTarget related events. |
| [ToolEventHandler](Aveva.ApplicationFramework.Presentation.ToolEventHandler.md) | Represents the method that will handle Tool related events. |
| [WindowEventHandler](Aveva.ApplicationFramework.Presentation.WindowEventHandler.md) | Represents the method that will handle Window related events. |

## Enumerations

| 类型 | 描述 |
|------|------|
| [CommandState](Aveva.ApplicationFramework.Presentation.CommandState.md) | Enumeration for various states of a command. This enumeration can be treated as a bit field; that is, a set of flags. Bit fields can be combined using a bitwise OR operation. |
| [CustomizationType](Aveva.ApplicationFramework.Presentation.CustomizationType.md) | Enumeration of menu and commandbar customisation options |
| [DockedPosition](Aveva.ApplicationFramework.Presentation.DockedPosition.md) | Enumerator used to specify the location of a toolbar or window docking area. |
| [DockGroupStyle](Aveva.ApplicationFramework.Presentation.DockGroupStyle.md) | Enumeration of styles for group docked windows. |
| [DropDownArrowStyle](Aveva.ApplicationFramework.Presentation.DropDownArrowStyle.md) | Enumerator used to specify the style used to draw a popup tool's dropdown arrow. Also determines which part of the tool should be clicked to drop down the tool. |
| [NavigationButtonStyle](Aveva.ApplicationFramework.Presentation.NavigationButtonStyle.md) | Enumeration used to indicate how the navigation buttons are used to navigate the items in a TaskBar |
| [PanelSizingMode](Aveva.ApplicationFramework.Presentation.PanelSizingMode.md) | Enumeration of the statusbar panel sizing options. |
| [PopupStyle](Aveva.ApplicationFramework.Presentation.PopupStyle.md) | Enumerator used to specify the style of popup menus. |
| [StandardImage](Aveva.ApplicationFramework.Presentation.StandardImage.md) | Enumeration of standard images |
| [UpdateOptions](Aveva.ApplicationFramework.Presentation.UpdateOptions.md) | Enumerations for the options for automatically updating the state of a MenuTool following state changes to an child StateButtonTool or ButtonTool. This enumeration can be treated as a bit field; that is, a set of flags. Bit fields can be combined using a bitwise OR operation. |
| [ValueListDisplayStyle](Aveva.ApplicationFramework.Presentation.ValueListDisplayStyle.md) | Enumeration for specifying what property of a value list item will be displayed in each item of the DropDown list |
| [ValueListSortStyle](Aveva.ApplicationFramework.Presentation.ValueListSortStyle.md) | Enumeration for specifying how value list items will be sorted when displaying value list items in a drop down list |
