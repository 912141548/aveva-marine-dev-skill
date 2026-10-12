
# Aveva.ApplicationFramework.Presentation API 参考(官方 XML 文档)

类型数:107


## Aveva.ApplicationFramework.Presentation.AnimationControl

| 类 | 成员 | 说明 |
|---|---|---|
| F | components | Required designer variable. |
| M | Dispose(System.Boolean) | Clean up any resources being used. |
| M | InitializeComponent | Required method for Designer support - do not modify the contents of this method with the code editor. |

## Aveva.ApplicationFramework.Presentation.ApplicationMenuBar

Class to represent the ApplicationMenu Ribbon element

| 类 | 成员 | 说明 |
|---|---|---|
| P | AreaLeftTools | Gets the ToolsCollection containing the tools to display in the AreaLeftTools |
| P | AreaRightTools | Gets the ToolsCollection containing the tools to display in the AreaRightTools |
| P | FooterToolbarTools | Gets the ToolsCollection containing the tools to display in the FooterToolbar |
| P | NavigationMenuTools | Gets the ToolsCollection containing the tools to display in the Scenic application menu navigation area |
| P | Caption | Get or set the caption for the application tab on the Ribbon. |
| P | Tag | Gets or sets the tag property which can be used to logically attach another object or value to a tool. |

## Aveva.ApplicationFramework.Presentation.ButtonTool

Represents a ButtonToolt.

| 类 | 成员 | 说明 |
|---|---|---|
| E | ToolClick | Occurs when the ButtonTool is clicked. |
| P | Command | Gets the command object which was associated with the tool when it was created. |
| P | MenuToolUpdateOptions | Gets or sets how properties of an owning MenuTool will be automatically updated. |
| P | Key | The Key of the tool in the RootToolsCollection |
| P | Tag | Gets or sets the tag property which can be used to logically attach another object or value to a tool. |
| P | Caption | Gets or sets the tool caption |
| P | Tooltip | Gets or sets the tools tooltip |
| P | TooltipFormattedText | Gets / sets the formatted text to be displayed in the tooltip. |
| P | TooltipTitle | Gets or sets the text displayed for the tooltip title |
| P | KeyTip | Returns or sets a string with a maximum of 3 characters that represents the mnemonic that is displayed when using keytips. |
| P | Image | Gets or sets the image (16x16) displayed on the tool |
| P | LargeImage | Gets or sets the large image (32x32) displayed on the tool |
| P | SmallImage | Gets or sets the image (16x16) displayed on the tool |
| P | IsFirstInGroup | Gets or sets a flag which indicated whether an instance tool is the first in a tool group. A separator will be displayed before a tool if this property is set to true. |
| P | ButtonGroup | Gets or sets the name of the group the instance tool should be contained within when placed on a RibbonGroup. |
| P | DisplayLargeImage | Flag to indicate if a large image should be displayed for an instance of a tool on the ribbon |
| P | ImageOnly | Flag to indicate if the tool should olny display an image and no caption. |
| P | Visible | Gets or sets the visibility of the tool. |
| P | Enabled | Gets or sets the enabled state of the tool. |
| P | DisplayStyle | Gets or sets the display style for a tool. |
| P | Shortcut | Gets or sets the shortcut associated with a tool. |
| P | Category | Gets or sets the tools category |
| P | Value | Gets or sets the value of the tool. |
| P | Arguments | Gets or sets the tools arguments. |

## Aveva.ApplicationFramework.Presentation.CancelClosingEventArgs

Provides data for a cancelable event.

| 类 | 成员 | 说明 |
|---|---|---|
| P | ParentClosing | Indicates if the closing event was raised as a result of closing the main window. |

## Aveva.ApplicationFramework.Presentation.ComboBoxTool

Represents a ComboBoxTool.

| 类 | 成员 | 说明 |
|---|---|---|
| P | Command | Gets the command object which was associated with the tool when it was created. |
| P | ValueList | Gets the ValueList object associated with the ComboBoxTool. |
| P | SelectedIndex | Gets or sets the zero-based index of the selected item in the ValueList. |
| P | SelectedValue | Returns the object behind the selected ValueList item. |
| P | DisplayText | Gets or sets the text displayed in the tool. |
| P | Editable | Gets or sets whether the text portion of the ComboBoxTool is editable. |
| P | MaxLength | Gets or sets the maximum allowable length of the text that can be entered in the ComboBoxTool. |
| P | PasswordChar | Gets or sets a value indicating how the characters typed by a user are displayed. |
| P | AutoComplete | Gets or sets whether the edit portion is automatically updated to match an item in the list as new characters are typed. |
| P | Width | Gets or sets the width of the tool. |
| E | ToolClick | Occurs when Enter key is pressed while display field has focus. |
| E | ToolValueChanged | Occurs when the value of the tool changes. |
| E | BeforePopup | Occurs before the popup part of the tool is displayed. |
| E | AfterCloseup | Occurs after the popup part of the tool is closed. |
| P | Key | The Key of the tool in the RootToolsCollection |
| P | Tag | Gets or sets the tag property which can be used to logically attach another object or value to a tool. |
| P | Caption | Gets or sets the tool caption |
| P | Tooltip | Gets or sets the tools tooltip |
| P | Image | Gets or sets the image (16x16) displayed on the tool |
| P | LargeImage | Gets or sets the large image (32x32) displayed on the tool |
| P | SmallImage | Gets or sets the image (16x16) displayed on the tool |
| P | IsFirstInGroup | Gets or sets a flag which indicated whether an instance tool is the first in a tool group. A separator will be displayed before a tool if this property is set to true. |
| P | ButtonGroup | Gets or sets the name of the group the instance tool should be contained within when placed on a RibbonGroup. |
| P | DisplayLargeImage | Flag to indicate if a large image should be displayed for an instance of a tool on the ribbon |
| P | ImageOnly | Flag to indicate if the tool should olny display an image and no caption. |
| P | Visible | Gets or sets the visibility of the tool. |
| P | Enabled | Gets or sets the enabled state of the tool. |
| P | DisplayStyle | Gets or sets the display style for a tool. |
| P | Shortcut | Gets or sets the shortcut associated with a tool. |
| P | Category | Gets or sets the tools category |
| P | Value | Gets or sets the value of the tool. |
| P | Arguments | Gets or sets the tools arguments. |
| P | TooltipFormattedText | Gets / sets the formatted text to be displayed in the tooltip. |
| P | TooltipTitle | Gets or sets the text displayed for the tooltip title |
| P | KeyTip | Returns or sets a string with a maximum of 3 characters that represents the mnemonic that is displayed when using keytips. |

## Aveva.ApplicationFramework.Presentation.Command

Abstract base class which an application must inherit from to create a Command object

| 类 | 成员 | 说明 |
|---|---|---|
| M | #ctor | Command constructor |
| M | CancelableExecute(System.Collections.ArrayList) | Version of Execute which can be cancelled by an BeforeCommandExecute event handler and which takes arguments |
| M | Execute(System.Collections.ArrayList) | The command Execute method which takes arguments, and calls a matching Execute in a derived class |
| M | FindExecute(System.Collections.ArrayList,System.Reflection.MethodInfo@) | Finds a matching execute overload |
| M | CancelableExecute | Version of Execute which can be cancelled by an BeforeCommandExecute event handler |
| M | Execute | The command Execute method is normally overridden by a derived class |
| M | Refresh(System.String) | Call to allow the command to update its visilility or enabled state following a change to the application context. |
| M | Refresh | Call to allow the command to update its visilility or enabled state following a change to the application context. |
| M | AttachExecutor(Aveva.ApplicationFramework.Presentation.CommandExecutor) | Attaches a CommandExecutor derived class to the command |
| M | DetachExecutor(Aveva.ApplicationFramework.Presentation.CommandExecutor) | Detach a CommandExecutor derived class from the command |
| M | DetachAllExecutors | Detach all CommandExecutor derived classes from the command |
| M | GetState(System.String) | Gets the current state of the command |
| M | SetProperty(System.String,System.Object) |  |
| E | CommandExecuted | Occurs when the command is executed |
| E | BeforeCommandExecute | Occurs before the command is executed |
| P | Key | The commands key in the CommandCollection |
| P | ApplicationContext | Application context for which this command is valid |
| P | ContextObjectKey |  |
| P | ValueChanged | True if the value of the command has been changed |
| P | List | ArrayList which can contain data to be presented in the GUI |
| P | SelectedIndex | Used to communicate to the command which item in the list was selected |
| P | IsValid | Gets the IsValid status of the command. A Command may become invalid in some application contexts |
| P | Checked | Gets or sets if the command is in a checked state. Setting this value will set the CommandExecutor.Checked property on all attached CommandExecutors. |
| P | Enabled | Gets or sets if the command is enabled. Setting this value will set the CommandExecutor.Enabled property on all attached CommandExecutors. |
| P | Visible | Gets or sets if the command is visible. Setting this value will set the CommandExecutor.Visible property on all attached CommandExecutors. |
| P | Value | Setting this value will set the CommandExecutor.Value property on all attached CommandExecutors. |
| P | Description | Description for the command |
| P | Internal | Flag to control the visibility of the command in Customization dialog |
| P | ExecuteOnCheckedChange |  |
| P | Executes | Get all command Execute overloads |

## Aveva.ApplicationFramework.Presentation.CommandBar

Class to represent a CommandBar.

| 类 | 成员 | 说明 |
|---|---|---|
| E | Closed | Event raised when the CommandBar is Closed |
| E | Opened | Event raised when the CommandBar is Opened |
| E | Resized | Event raised when the CommandBar is Resized |
| P | Key | The Key of the CommandBar in the CommandBarCollection |
| P | Tools | Gets the ToolsCollection containing the tools to display in the CommandBar. |
| P | Enabled | Gets or sets the enabled state of the CommandBar. |
| P | DockedColumn | Gets or sets the column (within the dock area) in which the CommandBar is docked. |
| P | DockedRow | Gets or sets the row (within the dock area) in which the CommandBar is docked. |
| P | DockedPosition | Gets or sets the current location of the CommandBar (left, right, top, bottom, floating) |
| P | FloatingLocation | Gets or sets the location of a floating CommandBar |
| P | FloatingSize | Gets or sets the size of a floating CommandBar |
| P | AllowFloating | Gets or sets whether the CommandBar can be dragged out of a dock area and floated. |
| P | AllowHiding | Gets or sets whether the CommandBar can be hidden at run-time by the end user. |
| P | AllowCustomize | Gets or sets whether the CommandBar can be customized at run-time by the end user. |
| P | FillEntireRow | Gets or sets whether the CommandBar will take up the entire dock area row, even if it doesn't have enough tools to fill the area. |
| P | Visible | Gets or sets whether the CommandBar is visible. |
| P | ShowInToolbarList | Gets or sets whether the CommandBar shows up in the customization dialog at runtime. |
| P | IsMainMenuBar | Get whether the CommandBar is the main menubar |
| P | Caption | Gets or sets the description displayed in the customization dialogs and in the caption of the floating CommandBar. |
| P | Command | Gets the command object which was associated with the CommandBar when it was created. |
| P | Tag | Gets or sets the tag property which can be used to logically attach another object or value to a tool. |

## Aveva.ApplicationFramework.Presentation.CommandBarEventArgs

Provides data for the CommandBarAdded and CommandBarRemoved events.

| 类 | 成员 | 说明 |
|---|---|---|
| M | #ctor(Aveva.ApplicationFramework.Presentation.CommandBar) | Initialize a new instance of a CommandBarEventArgs class |
| P | CommandBar | Gets the CommandBar object associated with the event |

## Aveva.ApplicationFramework.Presentation.CommandBarEventHandler

Represents the method that will handle CommandBar related events.


## Aveva.ApplicationFramework.Presentation.CommandBarManager

Class representing a CommandBarManager.

| 类 | 成员 | 说明 |
|---|---|---|
| M | ShowMiniToolbar | Shows the mini toolbar to the user |
| M | ShowMiniToolbar(System.Drawing.Point) | Shows the mini toolbar to the user at the given position |
| M | AddOptionSet(System.Boolean,System.String) | Create a new OptionSet identified by the specified Key An OptionSet is a set of StateButtonTools (a radio group) where at most one of the tools can can be in the Down (pressed) state. |
| M | SaveLayout | Save the current command CommandBars layout to a settings file. |
| M | LoadLayout | Load the saved command CommandBars layout from a settings file. |
| M | AddUICustomizationFile(System.String,System.String) | Adds a new UI Customization file. |
| M | AddUICustomizationSet(System.String,System.String[]) | Adds a set of UI Customization files. |
| M | AddUICustomizationFromStream(System.IO.Stream,System.String) | Adds a new UI Customization from the given stream |
| M | LoadUI | Creates the Menus,CommandBars and ContextMenus defined by the loaded UICustomization files. |
| M | LoadUI(System.String) | Loads the UI from the specified uic file |
| M | LoadUI(System.String,System.Boolean) | Loads the UI from he specified uic file, but only changes the Menu Bar if changeMenuBar is true |
| M | SelectTaskPane(System.String) | Select the task-pane with the given key |
| M | BeginInit | ISupportInitialize allows controls to optimize for multiple sets to properties. As a result, you can initialize co-dependent properties or batch set multiple properties at design time. Signal the object that initializati |
| M | EndInit | ISupportInitialize allows controls to optimize for multiple sets to properties. As a result, you can initialize co-dependent properties or batch set multiple properties at design time. Signal that initialization is compl |
| M | BeginUpdate | Signal the object that updating is starting. |
| M | EndUpdate(System.Boolean) | Signal that updating is complete. |
| M | AddMenuItem(System.String,System.String,System.String) | Add menu item in correct position |
| M | HideApplicationMenu | Hide the application menu (Backstage View) |
| P | Instance | Get instance of command-bar manager |
| P | MenuBar | Gets the CommandBar object that represents the Main Menu Bar. |
| P | CommandBars | Gets the collection of CommandBar objects currently managed by the CommandBarManager. |
| P | Ribbon | Gets the Ribbon object that represents the Office Ribbon. |
| P | Style | Gets or sets a value that specifies the style of all CommandBars, PopupMenuTools, and tools. |
| P | MiniToolbarTools | Gets the MiniToolbar element |
| P | RootTools | Gets the collection of RootTool objects currently managed by the CommandBarManager. |
| P | AllowCustomization | Gets or sets the default Customization status for all CommandBars belonging to the CommandBarManager; |
| P | CustomizationType | Gets or sets the type of customization. |
| P | CustomizationDialog | Gets the non standard customization dialog. |
| E | UILoaded | Event raised when the UI (Menus,CommandBars and ContextMenus) have finished loading after a call to LoadUI(). |
| P | IsUpdating | Gets whether the CommandBarManager is currently in update mode. (i.e. BeginInit() has been called) |
| P | Controls | Gets a Hashtable which contains controls to use for controls containers. |
| P | Enabled | Get or sets a property which controls the enabled state of all CommandBars |
| E | CommandBarLayoutLoaded | Event raised when the commandBar layout is loaded |

## Aveva.ApplicationFramework.Presentation.CommandBarMenuTool

Special tool which displays a menu of current CommandBars.

| 类 | 成员 | 说明 |
|---|---|---|
| P | Key | The Key of the tool in the RootToolsCollection |
| P | Tag | Gets or sets the tag property which can be used to logically attach another object or value to a tool. |
| P | Caption | Gets or sets the tool caption |
| P | Tooltip | Gets or sets the tools tooltip |
| P | Image | Gets or sets the image (16x16) displayed on the tool |
| P | LargeImage | Gets or sets the large image (32x32) displayed on the tool |
| P | SmallImage | Gets or sets the image (16x16) displayed on the tool |
| P | IsFirstInGroup | Gets or sets a flag which indicated whether an instance tool is the first in a tool group. A separator will be displayed before a tool if this property is set to true. |
| P | ButtonGroup | Gets or sets the name of the group the instance tool should be contained within when placed on a RibbonGroup. |
| P | DisplayLargeImage | Flag to indicate if a large image should be displayed for an instance of a tool on the ribbon |
| P | ImageOnly | Flag to indicate if the tool should olny display an image and no caption. |
| P | Visible | Gets or sets the visibility of the tool. |
| P | Enabled | Gets or sets the enabled state of the tool. |
| P | DisplayStyle | Gets or sets the display style for a tool. |
| P | Shortcut | Gets or sets the shortcut associated with a tool. |
| P | Category | Gets or sets the tools category |
| P | Value | Gets or sets the value of the tool. |
| P | Arguments | Gets or sets the tools arguments. |
| P | TooltipFormattedText | Gets / sets the formatted text to be displayed in the tooltip. |
| P | TooltipTitle | Gets or sets the text displayed for the tooltip title |
| P | KeyTip | Returns or sets a string with a maximum of 3 characters that represents the mnemonic that is displayed when using keytips. |

## Aveva.ApplicationFramework.Presentation.CommandBarStyle

Enumerator used to specify the look and feel of the toolbar

| 类 | 成员 | 说明 |
|---|---|---|
| F | Default | The toolbars will be displayed in their default style of OfficeXP. |
| F | Office2003 | Visual elements will emulate the Office 2003 look and feel. |
| F | ScenicRibbon | Visual elements will emulate the Scenic Ribbon look and feel. |
| F | Office2007 | Visual elements will emulate the Office 2007 look and feel. |
| F | Office2010 | Visual elements will emulate the Office 2010 look and feel. |

## Aveva.ApplicationFramework.Presentation.CommandBarsCollection

Class to represent a CommandBarCollection.

| 类 | 成员 | 说明 |
|---|---|---|
| M | AddCommandBar(System.String) | Create and add to the CommandBarCollection a new CommandBar with given Key. |
| M | AddCommandBar(System.String,Aveva.ApplicationFramework.Presentation.Command) | Create and add to the CommandBarCollection a new CommandBar with given Key and associated Command. |
| M | AddCommandBar(System.String,System.String) | Create and add to the CommandBarCollection a new CommandBar with given Key and associated CommandId. |
| M | AddTaskBar(System.String) | Create and add a new TaskBar with given Key to the CommandBarCollection. |
| M | RemoveCommandBar(System.String) | Remove the CommandBar with given Key from the CommandBarCollection. |
| M | RemoveCommandBar(Aveva.ApplicationFramework.Presentation.CommandBar) | Remove the specified CommandBar from the CommandBarCollection. |
| M | Clear | Remove all CommandBars from the CommandBarCollection. |
| M | Contains(System.String) | Determine if the CommandBar with the specified Key exists in the CommandBarCollection. |
| M | GetEnumerator | Returns an enumerator that can iterate through the CommandBarCollection. |
| M | CopyTo(System.Array,System.Int32) | Copies the elements of the collection to an Array, starting at a particular Array index. |
| P | Item(System.String) | Indexer to get the CommandBar with given Key from the CommandBarCollection. |
| E | CommandBarAdded | Occurs after a CommandBar has been added to the CommandBarCollection. |
| E | CommandBarRemoved | Occurs after a CommandBar has been removed from the CommandBarCollection. |
| P | IsSynchronized | Gets a value indicating whether access to the collection is synchronized (thread-safe). |
| P | Count | Gets the number of elements contained in the collection. |
| P | SyncRoot | Gets an object that can be used to synchronize access to the collection. |

## Aveva.ApplicationFramework.Presentation.CommandContextCollection

| 类 | 成员 | 说明 |
|---|---|---|
| M | Add(System.String,System.Object) | Add or replace existing keyed context object |
| E | CommandContextAdded |  |
| E | CommandContextChanged |  |
| P | Item(System.String) |  |

## Aveva.ApplicationFramework.Presentation.CommandContextEventArgs

Store arguments for Command Context

| 类 | 成员 | 说明 |
|---|---|---|
| M | #ctor(System.String) | Constructor |
| P | Key | Key |

## Aveva.ApplicationFramework.Presentation.CommandContextEventHandler

Represents the method that will handle command context related events.


## Aveva.ApplicationFramework.Presentation.CommandEventArgs

Provides data for the CommandAdded and CommandRemoved events.

| 类 | 成员 | 说明 |
|---|---|---|
| M | #ctor(Aveva.ApplicationFramework.Presentation.Command) | Initialize a new instance of a CommandEventArgs class |
| P | Command | Gets the Command object associated with the event |

## Aveva.ApplicationFramework.Presentation.CommandEventHandler

Represents the method that will handle command related events.


## Aveva.ApplicationFramework.Presentation.CommandExecutor

Abstract base class which an application must inherit from to create a CommandExecutor object.

| 类 | 成员 | 说明 |
|---|---|---|
| M | SetProperty(System.String,System.Object) | Sets the given property to the given value. |
| P | Enabled | Gets or sets the Enabled state of the CommandExecutor. |
| P | Visible | Gets or sets the Visible state of the CommandExecutor. |
| P | Checked | Gets or sets the Checked state of the CommandExecutor. |
| P | Value | Gets or sets the value of the CommandExecutor. |
| P | SelectedIndex | Set the SelectedIndex of the CommandExecutor. |

## Aveva.ApplicationFramework.Presentation.CommandList

An ArrayList use for the list property of Command objects which supports an IsModified property.

| 类 | 成员 | 说明 |
|---|---|---|
| M | #ctor | Default constructor for CommandList. |
| M | Add(System.Object) | Adds an object to the end of the CommandList. |
| M | AddRange(System.Collections.ICollection) | Adds the elements of an ICollection to the end of the CommandList. |
| M | Clear | Removes all elements from the CommandList. |
| M | Insert(System.Int32,System.Object) | Inserts an element into the CommandList at the specified index. |
| M | InsertRange(System.Int32,System.Collections.ICollection) | Inserts the elements of a collection into the CommandList at the specified index. |
| M | Remove(System.Object) | Removes the first occurrence of a specific object from the CommandList. |
| M | RemoveAt(System.Int32) | Removes the element at the specified index of the CommandList. |
| M | RemoveRange(System.Int32,System.Int32) | Removes a range of elements from the CommandList. |
| M | Reverse | Reverses the order of the elements in the CommandList or a portion of it. |
| M | Reverse(System.Int32,System.Int32) | Reverses the order of the elements in the CommandList or a portion of it. |
| M | SetRange(System.Int32,System.Collections.ICollection) | Copies the elements of a collection over a range of elements in the CommandList. |
| M | Sort | Sorts the elements in the CommandList or a portion of it. |
| M | Sort(System.Int32,System.Int32,System.Collections.IComparer) | Sorts the elements in the CommandList or a portion of it. |
| M | Sort(System.Collections.IComparer) | Sorts the elements in the CommandList or a portion of it. |
| P | IsModified | Flag which is set to true whenever the list is modified. |
| P | Item(System.Int32) | Gets or sets the element at the specified index. |

## Aveva.ApplicationFramework.Presentation.CommandManager

Class representing a CommandManager.

| 类 | 成员 | 说明 |
|---|---|---|
| M | AddAllCommands | Add to the CommandCollection an instance of each class in the calling assembly which has a base class of type Aveva.ApplicationFramework.Presentation.Command |
| P | Instance | Get instance of command manager |
| P | Commands | Gets the collection of Command objects currently managed by the CommandManager. |
| P | ApplicationContext | Property which holds the current application context, which is used to manage the state of all commands. |
| P | MacroCommand | Property which holds the type of a class which implements a command to execute a macro in the context of the host application. (e.g. A PML command) |
| P | CommandTypes | Property which returns a collection of Command Types |
| P | CommandContext | Property which returns a collection of Command Contexts |

## Aveva.ApplicationFramework.Presentation.CommandState

Enumeration for various states of a command. This enumeration can be treated as a bit field; that is, a set of flags. Bit fields can be combined using a bitwise OR operation.

| 类 | 成员 | 说明 |
|---|---|---|
| F | Enabled | Command is enabled. |
| F | Disabled | Command is disabled. |
| F | Hidden | Command is hidden. |
| F | Checked | Command is in checked state. |
| F | Unchecked | Command is in unchecked state. |

## Aveva.ApplicationFramework.Presentation.CommandTypesCollection

Class that represents a CommandCollection.

| 类 | 成员 | 说明 |
|---|---|---|
| M | Add(System.Type) | Add the given Command Type to the CommandCollection. |
| M | ContainsKey(System.String) | Determine if the Command with the specified Key exists in the CommandCollection. |
| M | Remove(System.String) | Remove the Command with given Key from the CommandCollection. |
| M | GetEnumerator | Returns an enumerator that can iterate through the CommandBarCollection. |
| M | CopyTo(System.Array,System.Int32) | Copies the elements of the collection to an Array, starting at a particular Array index. |
| P | Item(System.String) | Indexer to get the Command with given Key from the CommandCollection. |
| P | IsSynchronized | Gets a value indicating whether access to the collection is synchronized (thread-safe). |
| P | Count | Gets the number of elements contained in the collection. |
| P | SyncRoot | Gets an object that can be used to synchronize access to the collection. |

## Aveva.ApplicationFramework.Presentation.CommandsCollection

Class that represents a CommandCollection.

| 类 | 成员 | 说明 |
|---|---|---|
| M | Add(Aveva.ApplicationFramework.Presentation.Command) | Add the given Command to the CommandCollection. |
| M | ContainsKey(System.String) | Determine if the Command with the specified Key exists in the CommandCollection. |
| M | Remove(System.String) | Remove the Command with given Key from the CommandCollection. |
| M | GetEnumerator | Returns an enumerator that can iterate through the CommandBarCollection. |
| M | CopyTo(System.Array,System.Int32) | Copies the elements of the collection to an Array, starting at a particular Array index. |
| P | Item(System.String) | Indexer to get the Command with given Key from the CommandCollection. |
| E | CommandAdded | Occurs after a Command has been added to the CommandCollection. |
| E | CommandRemoved | Occurs after a Command has been removed from the CommandCollection. |
| P | IsSynchronized | Gets a value indicating whether access to the collection is synchronized (thread-safe). |
| P | Count | Gets the number of elements contained in the collection. |
| P | SyncRoot | Gets an object that can be used to synchronize access to the collection. |

## Aveva.ApplicationFramework.Presentation.ContainerTool

A tool that contains a Control.

| 类 | 成员 | 说明 |
|---|---|---|
| P | Control | Gets or sets the control displayed in the ContainerTool |
| P | Width | Gets or sets the width of the tool. |
| P | Key | The Key of the tool in the RootToolsCollection |
| P | Tag | Gets or sets the tag property which can be used to logically attach another object or value to a tool. |
| P | Caption | Gets or sets the tool caption |
| P | Tooltip | Gets or sets the tools tooltip |
| P | Image | Gets or sets the image (16x16) displayed on the tool |
| P | LargeImage | Gets or sets the large image (32x32) displayed on the tool |
| P | SmallImage | Gets or sets the image (16x16) displayed on the tool |
| P | IsFirstInGroup | Gets or sets a flag which indicated whether an instance tool is the first in a tool group. A separator will be displayed before a tool if this property is set to true. |
| P | ButtonGroup | Gets or sets the name of the group the instance tool should be contained within when placed on a RibbonGroup. |
| P | DisplayLargeImage | Flag to indicate if a large image should be displayed for an instance of a tool on the ribbon |
| P | ImageOnly | Flag to indicate if the tool should olny display an image and no caption. |
| P | Visible | Gets or sets the visibility of the tool. |
| P | Enabled | Gets or sets the enabled state of the tool. |
| P | DisplayStyle | Gets or sets the display style for a tool. |
| P | Shortcut | Gets or sets the shortcut associated with a tool. |
| P | Category | Gets or sets the tools category |
| P | Value | Gets or sets the value of the tool. |
| P | Arguments | Gets or sets the tools arguments. |
| P | TooltipFormattedText | Gets / sets the formatted text to be displayed in the tooltip. |
| P | TooltipTitle | Gets or sets the text displayed for the tooltip title |
| P | KeyTip | Returns or sets a string with a maximum of 3 characters that represents the mnemonic that is displayed when using keytips. |

## Aveva.ApplicationFramework.Presentation.CustomizationType

Enumeration of menu and commandbar customisation options

| 类 | 成员 | 说明 |
|---|---|---|
| F | Standard | Use standard Office 2003 style customisation |
| F | Custom | Use advanced customisation |

## Aveva.ApplicationFramework.Presentation.DockGroupStyle

Enumeration of styles for group docked windows.

| 类 | 成员 | 说明 |
|---|---|---|
| F | HorizontalSplit | The child panes are split horizontally. |
| F | SlidingGroup | The panes appear as headers in an outlook group bar style interface. |
| F | TabGroup | The panes are displayed as tabs items in a tab group. |
| F | VerticalSplit | The child panes are split vertically. |

## Aveva.ApplicationFramework.Presentation.DockedPosition

Enumerator used to specify the location of a toolbar or window docking area.

| 类 | 成员 | 说明 |
|---|---|---|
| F | Top | The docking area is located at the top of the container. |
| F | Bottom | The docking area is located at the bottom of the container. |
| F | Left | The docking area is located at the left edge of the container. |
| F | Right | The docking area is located at the right edge of the container. |
| F | Floating | The commandbar or window is floating. |

## Aveva.ApplicationFramework.Presentation.DockedWindow

Class to represent a DockedWindow.

| 类 | 成员 | 说明 |
|---|---|---|
| M | GroupWith(Aveva.ApplicationFramework.Presentation.DockedWindow) | Arrange docked windows together as a group. |
| M | Hide | Conceals the window from the user. |
| M | Show | Displays the window to the user. |
| M | Float | Displays the window as a floating window. |
| M | Dock | Docks the window within the main window. |
| M | Close | Destroys the window. |
| P | DockGroupStyle | How groups of docked windows should be organised. |
| E | Closing | Event which occurs when window is closing. |
| E | Closed | Event which occurs when window is closed. |
| E | Shown | Event which occurs when the window is shown. |
| E | Activated | Event which occurs when the window is activated. |
| E | Deactivated | Event which occurs when the window is deactivated. |
| E | Reparented | Event which occurs when the window is reparented. |
| P | DockedPosition | Current docked position of the window. |
| P | SaveLayout | Property which controls if the window should be included in the docked window layout serialization |
| P | Control | Control displayed in the window. |
| P | Enabled | Gets or sets whether the window is enabled. |
| P | Floatable | Whether the window is floatable. |
| P | Height | Height of the window. |
| P | HelpALink | Help link associated with the window. |
| P | HelpContextId | Help context id associated with the window. |
| P | IsFloating | Floating state of a window. |
| P | Key | Key of the window in the WindowsCollection. |
| P | Tag | Tag property which can be used to logically attach another object or value to a window. |
| P | Title | Title of the window. |
| P | Visible | State of the window. |
| P | Width | Width of the window. |
| P | MinimumSize | Minimum size of the window. |
| P | MaximumSize | Maximum size of the window. |
| P | Tooltip | Windows tooltip. |

## Aveva.ApplicationFramework.Presentation.DragDropDirector

A class to help direct drag-drop events.

| 类 | 成员 | 说明 |
|---|---|---|
| M | RegisterDropTarget(System.String) | Registers a new DropTarget with the DragDropDirector. |
| M | UnregisterDropTarget(Aveva.ApplicationFramework.Presentation.DropTarget) | Unregisters a DropTarget from the DragDropDirector. |
| E | DropTargetRegistered | Occurs when a new DropTarget is registered with the DragDropDirector. |
| E | DropTargetUnregistered | Occurs when a DropTarget is unregistered from the DragDropDirector. |

## Aveva.ApplicationFramework.Presentation.DropDownArrowStyle

Enumerator used to specify the style used to draw a popup tool's dropdown arrow. Also determines which part of the tool should be clicked to drop down the tool.

| 类 | 成员 | 说明 |
|---|---|---|
| F | Default | The tool is displayed in its default style. |
| F | None | No dropdown arrow is displayed. |
| F | Segmented | A standard downward-pointing dropdown arrow is displayed to the right of the tool's image and/or text in a separate boxed-off area when on a toolbar and a standard right-pointing arrow with a dividing line to the left of |
| F | SegmentedStateButton | A standard downward-pointing dropdown arrow is displayed to the right of the tool's image and/or text in a separate boxed-off area when on a toolbar and a standard right-pointing arrow with a dividing line to the left of |
| F | Standard | A standard downward-pointing dropdown arrow is displayed to the right of the tool's image and/or text when on a toolbar, and a standard right-pointing arrow is displayed when on a menu. |

## Aveva.ApplicationFramework.Presentation.DropTarget

A class to represent a DragDropTarget.

| 类 | 成员 | 说明 |
|---|---|---|
| M | RaiseDragEnter(Aveva.ApplicationFramework.Presentation.DropTargetEventArgs) | Raise a DragEnter event for this DropTarget. |
| M | RaiseDragOver(Aveva.ApplicationFramework.Presentation.DropTargetEventArgs) | Raise a DragOver event for this DropTarget. |
| M | RaiseDragDrop(Aveva.ApplicationFramework.Presentation.DropTargetEventArgs) | Raise a DragDrop event for this DropTarget. |
| P | DropTargetType | Gets the DropTarget type. |
| E | DragEnter | Occurs when an object is dragged into the DropTargets bounds. |
| E | DragOver | Occurs when an object is dragged over the DropTargets. |
| E | DragDrop | Occurs when an object is dropped onto the DropTargets. |

## Aveva.ApplicationFramework.Presentation.DropTargetEventArgs

A class to provide information to for drop-drop events.

| 类 | 成员 | 说明 |
|---|---|---|
| F | IsValidDropTarget | Boolean used to indicate if drop target is valid for a particular DataObject |
| F | DragDropEffect | The target drop effect in a drag-and-drop operation. |
| F | Target | The DropTarget object |
| F | Data | Data object used to encapsulate the object being dropped |
| F | DragEventArgs | The windows DragEventArgs object |
| M | #ctor(Aveva.ApplicationFramework.Presentation.DropTarget) | Initialize a new instance of a DropTargetEventArgs class |

## Aveva.ApplicationFramework.Presentation.DropTargetEventHandler

Represents the method that will handle DropTarget related events.


## Aveva.ApplicationFramework.Presentation.FontListTool

Represents a FontListTool.

| 类 | 成员 | 说明 |
|---|---|---|
| E | ToolClick | Occurs when a font is selected. |
| E | ToolValueChanged | Occurs when the value of the tool changes. |
| E | BeforePopup | Occurs before the popup part of the tool is displayed. |
| E | AfterCloseup | Occurs after the popup part of the tool is closed. |
| P | Command | Gets the command object which was associated with the tool when it was created. |
| P | FontName | Gets the FontName selected. |
| P | Width | Gets or sets the width of the tool. |
| P | Key | The Key of the tool in the RootToolsCollection |
| P | Tag | Gets or sets the tag property which can be used to logically attach another object or value to a tool. |
| P | Caption | Gets or sets the tool caption |
| P | Tooltip | Gets or sets the tools tooltip |
| P | Image | Gets or sets the image (16x16) displayed on the tool |
| P | LargeImage | Gets or sets the large image (32x32) displayed on the tool |
| P | SmallImage | Gets or sets the image (16x16) displayed on the tool |
| P | IsFirstInGroup | Gets or sets a flag which indicated whether an instance tool is the first in a tool group. A separator will be displayed before a tool if this property is set to true. |
| P | ButtonGroup | Gets or sets the name of the group the instance tool should be contained within when placed on a RibbonGroup. |
| P | DisplayLargeImage | Flag to indicate if a large image should be displayed for an instance of a tool on the ribbon |
| P | ImageOnly | Flag to indicate if the tool should olny display an image and no caption. |
| P | Visible | Gets or sets the visibility of the tool. |
| P | Enabled | Gets or sets the enabled state of the tool. |
| P | DisplayStyle | Gets or sets the display style for a tool. |
| P | Shortcut | Gets or sets the shortcut associated with a tool. |
| P | Category | Gets or sets the tools category |
| P | Value | Gets or sets the value of the tool. |
| P | Arguments | Gets or sets the tools arguments. |
| P | TooltipFormattedText | Gets / sets the formatted text to be displayed in the tooltip. |
| P | TooltipTitle | Gets or sets the text displayed for the tooltip title |
| P | KeyTip | Returns or sets a string with a maximum of 3 characters that represents the mnemonic that is displayed when using keytips. |

## Aveva.ApplicationFramework.Presentation.GalleryToolItem

Class to represent a GalleryToolItem.

| 类 | 成员 | 说明 |
|---|---|---|
| P | Title | Gets or sets the title to display for the item in the gallery drop down and preview and in the tool tips. |
| P | Description | Gets or sets addition information to display for the item in the gallery drop down. This can be formatted text. |
| P | Key | The Key of the item in its collection. |
| P | Image | Gets or sets the image displayed on the tool |
| P | Tooltip | Gets or sets the tools tooltip |
| P | TooltipFormattedText |  |
| P | TooltipTitle |  |
| P | Group |  |
| P | TextPlacement |  |

## Aveva.ApplicationFramework.Presentation.GalleryToolItemCollection

A collection of gallery tool items.

| 类 | 成员 | 说明 |
|---|---|---|
| M | Add(System.String) | Create and add to the GalleryToolItemCollection a new GalleryToolItem with given Name. |
| M | Remove(System.String) | Remove the GalleryToolItem with given Key from the GalleryToolItemCollection. |
| M | Clear | Remove all GalleryToolItems from the GalleryToolItemCollection. |
| M | Contains(System.String) | Determine if the GalleryToolItem with the specified Key exists in the CommandBarCollection. |
| M | GetEnumerator | Returns an enumerator that can iterate through the GalleryToolItemCollection. |
| M | CopyTo(System.Array,System.Int32) | Copies the elements of the collection to an Array, starting at a particular Array index. |
| P | Item(System.String) | Indexer to get the CommandBar with given Key from the CommandBarCollection. |
| P | IsSynchronized | Gets a value indicating whether access to the collection is synchronized (thread-safe). |
| P | Count | Gets the number of elements contained in the collection. |
| P | SyncRoot | Gets an object that can be used to synchronize access to the collection. |

## Aveva.ApplicationFramework.Presentation.GalleryToolItemEventArgs

Provides data for events on GalleryTool items

| 类 | 成员 | 说明 |
|---|---|---|
| M | #ctor(Aveva.ApplicationFramework.Presentation.GalleryToolItem) | Initialize a new instance of a GalleryToolItemEventArgs class |
| P | Item | The Gallery Tool Item associated with the event. |

## Aveva.ApplicationFramework.Presentation.GalleryToolItemEventHandler

Represents the method that will handle CommandBar related events.


## Aveva.ApplicationFramework.Presentation.HtmlHelp

A class to control Html Help viewer.

| 类 | 成员 | 说明 |
|---|---|---|
| M | ShowHelpIndex | Displays the help window with the index pane active. |
| M | ShowHelpContents | Displays the help window with the contents pane active. |
| M | ShowHelpSearch | Displays the help window with the search pane active. |
| M | ShowHelpContext(System.String) | Displays the help window at the topic associated with the given contextId. The help topic is determined via a lookup in the context help index. |
| M | ShowHelpContext(System.String,System.String) | Displays the help window at the topic associated with the given contextId in the given chm file. The help topic is determined via a lookup in the context help index. |
| M | ShowHelpALink(System.String) | Displays the help window at the topic with the given associative link. |
| M | ShowHelpKeyword(System.String) | Displays the help window at the topic with the given keyword. |
| M | ShowHelpAbout | Shows the help about form as a modal dialog. |
| M | ShowHelpOnHelp | Show a help window for help on help if a help on help file has been specified. |
| M | ShowOnlineLink(System.String) | Opens a browser window for the given URL. |
| P | Instance | Get instance of HtmlHelp |
| P | HelpFile | Gets or sets the application .chm html help file |
| P | DefaultContextAlias | The default .chm alias to use for context lookups |
| P | ContextHelpIndex | Gets or sets the index file for context lookup |
| P | HelpOnHelpFile | Gets or sets the help file to use for help on help. |
| P | HelpAboutForm | Gets or sets the form to display for help about. |
| P | OnTop | Gets or sets whether the help window is owned by the application window an will always be on top. |

## Aveva.ApplicationFramework.Presentation.IApplicationInfo

Interface use to supply application information to the framework

| 类 | 成员 | 说明 |
|---|---|---|
| P | ProductFamilyName | Return the Product Family name |
| P | ProductName | Return the Product Name |
| P | ModuleName | Return the Module Name |
| P | Name | Return the Application Name |
| P | ShortName | Return the Application ShortName; |
| P | Version | Return the application version number |
| P | License | Return the application license information |
| P | Copyright | Return the application copyright notice |
| P | AdditionalInfoDialog | Return a form to display additional application specific information |
| P | HelpAlias | Default Help File Book Alias set this if you want your application to jump to a specific help book by default (from Help About) |

## Aveva.ApplicationFramework.Presentation.ICancelIndicator

Interface for elements with cancel functionality

| 类 | 成员 | 说明 |
|---|---|---|
| P | CancelVisible | If cancel indicator is visible |
| P | CancelEnabled | If cancel indicator is enabled |
| P | CancelText | Text to display on cancel indicator |
| P | Cancelled | Cancellation state |
| P | Block | Dialog will also block |
| P | TopMostFlag | Flag to override topmost setting |
| E | CancelRequest | Cancel Request |
| P | FilterMessages | If blocked then filter window messages to prevent background UI changing |

## Aveva.ApplicationFramework.Presentation.IPopupGalleryToolCommand

| 类 | 成员 | 说明 |
|---|---|---|
| M | ExecuteToolItemPreview(System.String) |  |
| M | ExecuteToolItemClick(System.String) |  |

## Aveva.ApplicationFramework.Presentation.IProgressIndicator

Progress Indication API

| 类 | 成员 | 说明 |
|---|---|---|
| M | FinishProgressDisplay | Signal that progress display has ended |
| M | StartProgressDisplay | Signal that progress display to begin |
| P | Progress | Gets or sets the progress bar value. |
| P | ProgressText | Gets or Sets the text that is displayed with the progress bar (left). |
| P | ProgressTextAdditional | Gets or Sets the text that is displayed with the progress bar (right). |
| P | ProgressTitle | Gets or Sets the text that is displayed as a title of the progress bar. |
| P | ProgressShowLabel | Flag for progress label overlaying the statusbar |
| P | ProgressMinimum | Minimum for progress range |
| P | ProgressMaximum | Maximum for progress range |
| P | UseMarqueeStyle | When true then acts and an activity indicator |
| P | MarqueeBounce | When set activity indicator will bounce from side to side |
| P | MarqueeColor | Activity indicator color |
| P | MarqueeSpeed | Activity indicator speed |
| E | OnStart | called when display ready |

## Aveva.ApplicationFramework.Presentation.IStatusBarPanel

Interface supported by Statusbar panels.

| 类 | 成员 | 说明 |
|---|---|---|
| E | PanelClick | Occurs when the panel is clicked |
| E | PanelDoubleClick | Occurs when the panel is double clicked |
| P | Key | Key for the panel. |
| P | Enabled | Returns or sets if the panel is enabled. |
| P | Text | Returns or sets the text associated with the panel. |
| P | Tooltip | Returns or sets the tooltip for the panel. |
| P | Image | Returns or sets the image associated with the panel. |
| P | SizingMode | Returns or sets how the panel can be sized. Fixed - The panel's size is controlled by the width. Automatic - The panel's size is based on its contents. Adjustable - The panel's base size is controlled by the width but th |
| P | Visible | Returns or sets if the panel is visible. |
| P | Width | Returns or sets the width of the panel (pixels). |

## Aveva.ApplicationFramework.Presentation.ITool

Interface supported by all Tool clases.

| 类 | 成员 | 说明 |
|---|---|---|
| P | Key | The Key of the tool in the RootToolsCollection |
| P | Tag | Gets or sets the tag property which can be used to logically attach another object or value to a tool. |
| P | Caption | Gets or sets the tool caption |
| P | Tooltip | Gets or sets the tools tooltip |
| P | Image | Gets or sets the small image (16x16) displayed on the tool |
| P | LargeImage | Gets or sets the large (32x32) image displayed on the tool |
| P | SmallImage | Gets or sets the small image (16x16) displayed on the tool |
| P | IsFirstInGroup | Gets or sets a flag which indicated whether an instance tool is the first in a tool group. A separator will be displayed before a tool if this property is set to true. |
| P | ButtonGroup | Gets or sets the name of the group the instance tool should be contained within when placed on a RibbonGroup. |
| P | DisplayLargeImage | Flag to indicate if a large image should be displayed for an instance of a tool on the ribbon |
| P | ImageOnly | Flag to indicate if the tool should olny display an image and no caption. |
| P | Visible | Gets or sets the visibility of the tool. |
| P | Enabled | Gets or sets the enabled state of the tool. |
| P | DisplayStyle | Gets or sets the display style for a tool. |
| P | Shortcut | Gets or sets the shortcut associated with a tool. |
| P | Category | Gets or sets the tools category |
| P | Value | Gets or sets the value of the tool. |
| P | Arguments | Gets or sets the Attributes of the tool. |
| P | TooltipFormattedText | Gets / sets the formatted text to be displayed in the tooltip. |
| P | TooltipTitle | Gets or sets the text displayed for the tooltip title . |
| P | KeyTip | Returns or sets a string with a maximum of 3 characters that represents the mnemonic that is displayed when using keytips. |

## Aveva.ApplicationFramework.Presentation.ITools

Interface for tools which have a tools collection.

| 类 | 成员 | 说明 |
|---|---|---|
| P | Tools | The ToolsCollection |

## Aveva.ApplicationFramework.Presentation.IWindow

Interface supported by supported window types(MDI, Docked).

| 类 | 成员 | 说明 |
|---|---|---|
| M | Hide | Conceals the window from the user. |
| M | Show | Displays the window to the user. |
| M | Float | Displays the window as a floating window. |
| M | Dock | Docks the window within the main window. |
| M | Close | Destroys the window. |
| P | Control | Gets the control displayed in the window. |
| P | Enabled | Gets or sets whether the window is enabled. |
| P | Floatable | Gets or sets whether the window is floatable. |
| P | Height | Gets or sets the height of the window. |
| P | HelpALink | Gets or sets a help link associated with the window. |
| P | HelpContextId | Gets or sets the help context id associated with the window. |
| P | IsFloating | Gets the floating state of a window. |
| P | Key | Gets the Key of the window in the WindowsCollection. |
| P | Tag | Gets or sets the tag property which can be used to logically attach another object or value to a window. |
| P | Title | Gets or sets the title of the window. |
| P | Visible | Gets or sets the visible state of the window. |
| P | Width | Gets or sets the width of the window. |
| P | MaximumSize | Get or sets the maximum size of the window. |
| P | MinimumSize | Get or sets the minimum size of the window. |
| P | Tooltip | Gets or sets the window tooltip |

## Aveva.ApplicationFramework.Presentation.IZoom

A control that implements zooming

| 类 | 成员 | 说明 |
|---|---|---|
| P | ZoomLargeChange | Large Change |
| P | ZoomSmallChange | Small Change |
| P | ZoomMinValue | Minimum Value |
| P | ZoomMaxValue | Maximum Value |
| P | ZoomMidpointValue | Midpoint Value |
| P | ZoomValue | Current Value |
| E | ZoomValueChanged | On Value changed |

## Aveva.ApplicationFramework.Presentation.InsertPosition

Position to insert new element


## Aveva.ApplicationFramework.Presentation.LabelTool

Class to represent a static Label.

| 类 | 成员 | 说明 |
|---|---|---|
| P | Width | Gets or sets the width of the tool. |
| P | Command | Gets the command object which was associated with the tool when it was created. |
| P | Key | The Key of the tool in the RootToolsCollection |
| P | Tag | Gets or sets the tag property which can be used to logically attach another object or value to a tool. |
| P | Caption | Gets or sets the tool caption |
| P | Tooltip | Gets or sets the tools tooltip |
| P | IsFirstInGroup | Gets or sets a flag which indicated whether an instance tool is the first in a tool group. A separator will be displayed before a tool if this property is set to true. |
| P | ButtonGroup | Gets or sets the name of the group the instance tool should be contained within when placed on a RibbonGroup. |
| P | DisplayLargeImage | Flag to indicate if a large image should be displayed for an instance of a tool on the ribbon |
| P | Image | Gets or sets the image (16x16) displayed on the tool |
| P | LargeImage | Gets or sets the large image (32x32) displayed on the tool |
| P | SmallImage | Gets or sets the image (16x16) displayed on the tool |
| P | ImageOnly | Flag to indicate if the tool should olny display an image and no caption. |
| P | Visible | Gets or sets the visibility of the tool. |
| P | Enabled | Gets or sets the enabled state of the tool. |
| P | DisplayStyle | Gets or sets the display style for a tool. |
| P | Shortcut | Gets or sets the shortcut associated with a tool. |
| P | Category | Gets or sets the tools category |
| P | Value | Gets or sets the value of the tool. |
| P | Arguments | Gets or sets the tools arguments. |
| P | TooltipFormattedText | Gets / sets the formatted text to be displayed in the tooltip. |
| P | TooltipTitle | Gets or sets the text displayed for the tooltip title |
| P | KeyTip | Returns or sets a string with a maximum of 3 characters that represents the mnemonic that is displayed when using keytips. |

## Aveva.ApplicationFramework.Presentation.LayoutDirection

Enumeration used to define how the tools within the group are arranged.

| 类 | 成员 | 说明 |
|---|---|---|
| F | Vertical | The tools are arranged in columns. |
| F | Horizontal | The tools are arranged into a series of rows of tools. |

## Aveva.ApplicationFramework.Presentation.ListTool

Represents a ListTool.

| 类 | 成员 | 说明 |
|---|---|---|
| E | ToolClick | Occurs when the ButtonTool is clicked. |
| E | BeforePopup | Occurs before the menu containing the ListTool is displayed |
| P | DisplayCheckmark | Returns or sets whether a checkmark should be displayed next to the selected ListToolItem. |
| P | Command | Gets the command object which was associated with the tool when it was created. |
| P | ValueList | Gets the ValueList object associated with the ComboBoxTool. |
| P | SelectedItemIndex | Returns the index of the currently selected ListToolItem. |
| P | Key | The Key of the tool in the RootToolsCollection |
| P | Tag | Gets or sets the tag property which can be used to logically attach another object or value to a tool. |
| P | Caption | Gets or sets the tool caption |
| P | Tooltip | Gets or sets the tools tooltip |
| P | Image | Gets or sets the image (16x16) displayed on the tool |
| P | LargeImage | Gets or sets the large image (32x32) displayed on the tool |
| P | SmallImage | Gets or sets the image (16x16) displayed on the tool |
| P | IsFirstInGroup | Gets or sets a flag which indicated whether an instance tool is the first in a tool group. A separator will be displayed before a tool if this property is set to true. |
| P | ButtonGroup | Gets or sets the name of the group the instance tool should be contained within when placed on a RibbonGroup. |
| P | DisplayLargeImage | Flag to indicate if a large image should be displayed for an instance of a tool on the ribbon |
| P | ImageOnly | Flag to indicate if the tool should olny display an image and no caption. |
| P | Visible | Gets or sets the visibility of the tool. |
| P | Enabled | Gets or sets the enabled state of the tool. |
| P | DisplayStyle | Gets or sets the display style for a tool. |
| P | Shortcut | Gets or sets the shortcut associated with a tool. |
| P | Category | Gets or sets the tools category |
| P | Value | Gets or sets the value of the tool. |
| P | Arguments | Gets or sets the tools arguments. |
| P | TooltipFormattedText | Gets / sets the formatted text to be displayed in the tooltip. |
| P | TooltipTitle | Gets or sets the text displayed for the tooltip title |
| P | KeyTip | Returns or sets a string with a maximum of 3 characters that represents the mnemonic that is displayed when using keytips. |

## Aveva.ApplicationFramework.Presentation.MdiWindow

Represents an MDI style window or dialog box.

| 类 | 成员 | 说明 |
|---|---|---|
| M | Hide | Conceals the window from the user. |
| M | Show | Displays the window to the user. |
| M | Float | Displays the window as a floating window. |
| M | Dock | Docks the window within the main window. |
| M | Close | Destroys the window. |
| P | CommandBarManager | Gets the CommandBarManager for this MDI window. |
| E | Closing | Occurs when this window is closing. |
| E | Closed | Event which occurs when window is closed. |
| E | Activated | Occurs when the window is activated. |
| E | Deactivated | Occurs when the window is deactivated. |
| E | Resized | Occurs when the window is resized. |
| E | Reparented | Occurs when the window is reparented. |
| P | Form | Returns the underlying Form for the MdiWindow |
| P | Resizeable | Gets or sets whether the window is resizeable. |
| P | Maximized | Gets or sets the maximized state of the window. |
| P | DestroyOnClose | Controls the default behaviour of destroying the window on close. If this is set to false then the default behaviour will be to hide the window. |
| P | Tooltip | Tooltip to display when MDI window is displayed as a tab |
| P | DisplayFormIcon | Controls if MDI form icon is displayed on a tab |
| P | IsActive | Get if the MdiWindow is currently active |
| P | Control | Gets the control displayed in the window. |
| P | Enabled | Gets or sets whether the window is enabled. |
| P | Floatable | Gets or sets whether the window is floatable. |
| P | Height | Gets or sets the height of the window. |
| P | HelpALink | Gets or sets a help link associated with the window. |
| P | HelpContextId | Gets or sets the help context id associated with the window. |
| P | IsFloating | Gets the floating state of a window. |
| P | Key | Gets the Key of the window in the WindowsCollection. |
| P | Tag | Gets or sets the tag property which can be used to logically attach another object or value to a window. |
| P | Title | Gets or sets the title of the window. |
| P | Visible | Gets or sets the visible state of the window. |
| P | Width | Gets or sets the width of the window. |
| P | MinimumSize | Get or sets the minimum size of the window. |
| P | MaximumSize | Get or sets the maximum size of the window. |

## Aveva.ApplicationFramework.Presentation.MdiWindowListTool

Special tool which displays a list of current MDI Windows.

| 类 | 成员 | 说明 |
|---|---|---|
| P | Key | The Key of the tool in the RootToolsCollection |
| P | Tag | Gets or sets the tag property which can be used to logically attach another object or value to a tool. |
| P | Caption | Gets or sets the tool caption |
| P | Tooltip | Gets or sets the tools tooltip |
| P | Image | Gets or sets the image (16x16) displayed on the tool |
| P | LargeImage | Gets or sets the large image (32x32) displayed on the tool |
| P | SmallImage | Gets or sets the image (16x16) displayed on the tool |
| P | IsFirstInGroup | Gets or sets a flag which indicated whether an instance tool is the first in a tool group. A separator will be displayed before a tool if this property is set to true. |
| P | ButtonGroup | Gets or sets the name of the group the instance tool should be contained within when placed on a RibbonGroup. |
| P | DisplayLargeImage | Flag to indicate if a large image should be displayed for an instance of a tool on the ribbon |
| P | ImageOnly | Flag to indicate if the tool should olny display an image and no caption. |
| P | Visible | Gets or sets the visibility of the tool. |
| P | Enabled | Gets or sets the enabled state of the tool. |
| P | DisplayStyle | Gets or sets the display style for a tool. |
| P | Shortcut | Gets or sets the shortcut associated with a tool. |
| P | Category | Gets or sets the tools category |
| P | Value | Gets or sets the value of the tool. |
| P | Arguments | Gets or sets the tools arguments. |
| P | TooltipFormattedText | Gets / sets the formatted text to be displayed in the tooltip. |
| P | TooltipTitle | Gets or sets the text displayed for the tooltip title |
| P | KeyTip | Returns or sets a string with a maximum of 3 characters that represents the mnemonic that is displayed when using keytips. |

## Aveva.ApplicationFramework.Presentation.MenuTool

Represents a MenuTool.

| 类 | 成员 | 说明 |
|---|---|---|
| M | ShowPopup | Displays the MenuTool as a context popup at the current mouse position. |
| M | ShowPopup(System.String) | Displays the MenuTool as a context popup with given context at the current mouse position. |
| M | ShowPopup(System.Drawing.Point) | Displays the MenuTool as a context popup at the given screen position. |
| M | ShowPopup(System.String,System.Drawing.Point) | Displays the MenuTool as a context popup with given context at the given screen position. |
| E | ToolClick | Occurs when the tool is clicked |
| E | BeforePopup | Occurs before the menu is displayed |
| E | AfterCloseup | Occurs after the menu is displayed |
| P | Tools | Gets the ToolsCollection containing the tools to display in the popup menu. |
| P | Checked | Gets or sets whether the tool is in the checked state. |
| P | DropDownArrowStyle | Returns or sets the style of the dropdown arrow for the popup menu. |
| P | Command | Gets the command object which was associated with the tool when it was created. |
| P | IsContextMenu | Gets or sets whether the menu is a context menu |
| P | AutoUpdate | Gets or sets whether the Image, Tooltip and Command are automatically updated. |
| P | PopupStyle | Gets or sets the popup style of the menu (Menu or CommandBar) |
| P | AllowTearaway | Gets or sets whether the menu can be torn off |
| P | OptionSetKey | Gets or sets the OptionSet key for the tool. Setting the key assigns the tool to the CommandBarManagers OptionSet which has this key. |
| P | Key | The Key of the tool in the RootToolsCollection |
| P | Tag | Gets or sets the tag property which can be used to logically attach another object or value to a tool. |
| P | Caption | Gets or sets the tool caption |
| P | Tooltip | Gets or sets the tools tooltip |
| P | Image | Gets or sets the image (16x16) displayed on the tool |
| P | LargeImage | Gets or sets the large image (32x32) displayed on the tool |
| P | SmallImage | Gets or sets the image (16x16) displayed on the tool |
| P | IsFirstInGroup | Gets or sets a flag which indicated whether an instance tool is the first in a tool group. A separator will be displayed before a tool if this property is set to true. |
| P | ButtonGroup | Gets or sets the name of the group the instance tool should be contained within when placed on a RibbonGroup. |
| P | DisplayLargeImage | Flag to indicate if a large image should be displayed for an instance of a tool on the ribbon |
| P | ImageOnly | Flag to indicate if the tool should olny display an image and no caption. |
| P | Visible | Gets or sets the visibility of the tool. |
| P | Enabled | Gets or sets the enabled state of the tool. |
| P | DisplayStyle | Gets or sets the display style for a tool. |
| P | Shortcut | Gets or sets the shortcut associated with a tool. |
| P | Category | Gets or sets the tools category |
| P | Value | Gets or sets the value of the tool. |
| P | Arguments | Gets or sets the tools arguments. |
| P | TooltipFormattedText | Gets / sets the formatted text to be displayed in the tooltip. |
| P | TooltipTitle | Gets or sets the text displayed for the tooltip title |
| P | KeyTip | Returns or sets a string with a maximum of 3 characters that represents the mnemonic that is displayed when using keytips. |

## Aveva.ApplicationFramework.Presentation.NavigationButtonStyle

Enumeration used to indicate how the navigation buttons are used to navigate the items in a TaskBar

| 类 | 成员 | 说明 |
|---|---|---|
| F | Default |  |
| F | History | The Back and Forward buttons will be used to navigate through the items based on the order in which the items have been selected. |
| F | Linear | The Back and Forward buttons will be used to navigate through the items based on their order in the Tools collection. |
| F | None | The Back and Forward buttons will not be displayed. |

## Aveva.ApplicationFramework.Presentation.PanelSizingMode

Enumeration of the statusbar panel sizing options.

| 类 | 成员 | 说明 |
|---|---|---|
| F | Adjustable | The panel's base size is controlled by the width but the panel may be resized. |
| F | Automatic | The panel's size is based on its contents. |
| F | Fixed | The panel's size is controlled by the width. |
| F | Spring | The panel size is based on the remaining size remaining after the other visible panes have been sized. |

## Aveva.ApplicationFramework.Presentation.PanelStyle

Panel appearance

| 类 | 成员 | 说明 |
|---|---|---|
| F | Text | Text style |
| F | Button | Button style |
| F | StateButton | State Button Style |

## Aveva.ApplicationFramework.Presentation.PopupColorPickerTool

Represents a PopupColorPicker.

| 类 | 成员 | 说明 |
|---|---|---|
| E | ToolClick | Occurs when the PopupColorPickerTool is clicked. |
| E | ToolValueChanged | Occurs when the value of the tool changes. |
| P | Command | Gets the command object which was associated with the tool when it was created. |
| P | ReplaceableColor | Returns or sets the color in the PopupColorPickerTool's image that will be replaced with the SelectedColor value. Default is Magenta. |
| P | SelectedColor | Returns/sets the selected color in the PopupColorPickerTool. |
| P | ShowAutomaticColor | Returns or sets whether a button representing the color Color.WindowText is displayed in the dropdown. |
| P | ShowTransparentColor | Returns or sets whether a button representing the color Color.Transparent is displayed in the dropdown. |
| P | Checked | Gets or sets whether the tool is in the checked state. |
| P | DropDownArrowStyle | Returns or sets the style of the dropdown arrow for the popup menu. |
| P | Key | The Key of the tool in the RootToolsCollection |
| P | Tag | Gets or sets the tag property which can be used to logically attach another object or value to a tool. |
| P | Caption | Gets or sets the tool caption |
| P | Tooltip | Gets or sets the tools tooltip |
| P | Image | Gets or sets the image (16x16) displayed on the tool |
| P | LargeImage | Gets or sets the large image (32x32) displayed on the tool |
| P | SmallImage | Gets or sets the image (16x16) displayed on the tool |
| P | IsFirstInGroup | Gets or sets a flag which indicated whether an instance tool is the first in a tool group. A separator will be displayed before a tool if this property is set to true. |
| P | ButtonGroup | Gets or sets the name of the group the instance tool should be contained within when placed on a RibbonGroup. |
| P | DisplayLargeImage | Flag to indicate if a large image should be displayed for an instance of a tool on the ribbon |
| P | ImageOnly | Flag to indicate if the tool should olny display an image and no caption. |
| P | Visible | Gets or sets the visibility of the tool. |
| P | Enabled | Gets or sets the enabled state of the tool. |
| P | DisplayStyle | Gets or sets the display style for a tool. |
| P | Shortcut | Gets or sets the shortcut associated with a tool. |
| P | Category | Gets or sets the tools category |
| P | Value | Gets or sets the value of the tool. |
| P | Arguments | Gets or sets the tools arguments. |
| P | TooltipFormattedText | Gets / sets the formatted text to be displayed in the tooltip. |
| P | TooltipTitle | Gets or sets the text displayed for the tooltip title |
| P | KeyTip | Returns or sets a string with a maximum of 3 characters that represents the mnemonic that is displayed when using keytips. |

## Aveva.ApplicationFramework.Presentation.PopupContainerTool

Represents a Popup Container Tool.

| 类 | 成员 | 说明 |
|---|---|---|
| M | ShowPopup | Shows the PopupContainer |
| M | ClosePopup | Closes the PopupContainer |
| E | BeforePopup | Occurs before the Popup Container is displayed |
| E | AfterCloseup | Occurs after the PopupContainer is displayed |
| E | ToolClick | Occurs when the tool is clicked |
| P | Command | Gets the command object which was associated with the tool when it was created. |
| P | Control | Gets or sets the control to display in the PopupContainer |
| P | Key | The Key of the tool in the RootToolsCollection |
| P | Tag | Gets or sets the tag property which can be used to logically attach another object or value to a tool. |
| P | Caption | Gets or sets the tool caption |
| P | Tooltip | Gets or sets the tools tooltip |
| P | Image | Gets or sets the image (16x16) displayed on the tool |
| P | LargeImage | Gets or sets the large image (32x32) displayed on the tool |
| P | SmallImage | Gets or sets the image (16x16) displayed on the tool |
| P | IsFirstInGroup | Gets or sets a flag which indicated whether an instance tool is the first in a tool group. A separator will be displayed before a tool if this property is set to true. |
| P | ButtonGroup | Gets or sets the name of the group the instance tool should be contained within when placed on a RibbonGroup. |
| P | DisplayLargeImage | Flag to indicate if a large image should be displayed for an instance of a tool on the ribbon |
| P | ImageOnly | Flag to indicate if the tool should olny display an image and no caption. |
| P | Visible | Gets or sets the visibility of the tool. |
| P | Enabled | Gets or sets the enabled state of the tool. |
| P | DisplayStyle | Gets or sets the display style for a tool. |
| P | Shortcut | Gets or sets the shortcut associated with a tool. |
| P | Category | Gets or sets the tools category |
| P | Value | Gets or sets the value of the tool. |
| P | Arguments | Gets or sets the tools arguments. |
| P | TooltipFormattedText | Gets / sets the formatted text to be displayed in the tooltip. |
| P | TooltipTitle | Gets or sets the text displayed for the tooltip title |
| P | KeyTip | Returns or sets a string with a maximum of 3 characters that represents the mnemonic that is displayed when using keytips. |

## Aveva.ApplicationFramework.Presentation.PopupGalleryTool

Represents a MenuTool.

| 类 | 成员 | 说明 |
|---|---|---|
| E | ToolClick | Occurs when the tool is clicked |
| E | BeforePopup | Occurs before the menu is displayed |
| E | AfterCloseup | Occurs after the menu is displayed |
| E | ToolItemPreview | Occurs when cursor hovers over a GalleryTool item |
| E | ToolItemClick | Occurs when a GalleryTool item is clicked |
| P | Items | Collection of GalleryToolItems contained by this PopupGalleryTool |
| P | Tools | Gets the ToolsCollection containing the tools to display in the popup menu. |
| P | Checked | Gets or sets whether the tool is in the checked state. |
| P | DropDownArrowStyle | Returns or sets the style of the dropdown arrow for the popup menu. |
| P | Command | Gets the command object which was associated with the tool when it was created. |
| P | OptionSetKey | Gets or sets the OptionSet key for the tool. Setting the key assigns the tool to the CommandBarManagers OptionSet which has this key. |
| P | MinPreviewColumns | Gets or sets the minimum number of columns that can be displayed in the gallery preview. |
| P | MaxPreviewColumns | Gets or sets the maximum number of columns that can be displayed in the gallery preview. |
| P | MinDropDownColumns | Gets or sets the minimum number of columns that can be displayed in the gallery drop down. |
| P | MaxDropDownColumns | Gets or sets the maximum number of columns that can be displayed in the gallery drop down. 0 means there is no limit to the number of columns in the gallery. |
| P | ShowPreviewInRibbon | Gets or sets the value indicating whether the gallery preview should be displayed if this tool is on the ribbon. |
| P | Key | The Key of the tool in the RootToolsCollection |
| P | Tag | Gets or sets the tag property which can be used to logically attach another object or value to a tool. |
| P | Caption | Gets or sets the tool caption |
| P | Tooltip | Gets or sets the tools tooltip |
| P | Image | Gets or sets the image (16x16) displayed on the tool |
| P | LargeImage | Gets or sets the large image (32x32) displayed on the tool |
| P | SmallImage | Gets or sets the image (16x16) displayed on the tool |
| P | IsFirstInGroup | Gets or sets a flag which indicated whether an instance tool is the first in a tool group. A separator will be displayed before a tool if this property is set to true. |
| P | ButtonGroup | Gets or sets the name of the group the instance tool should be contained within when placed on a RibbonGroup. |
| P | DisplayLargeImage | Flag to indicate if a large image should be displayed for an instance of a tool on the ribbon |
| P | ImageOnly | Flag to indicate if the tool should olny display an image and no caption. |
| P | Visible | Gets or sets the visibility of the tool. |
| P | Enabled | Gets or sets the enabled state of the tool. |
| P | DisplayStyle | Gets or sets the display style for a tool. |
| P | Shortcut | Gets or sets the shortcut associated with a tool. |
| P | Category | Gets or sets the tools category |
| P | Value | Gets or sets the value of the tool. |
| P | Arguments | Gets or sets the tools arguments. |
| P | TooltipFormattedText | Gets / sets the formatted text to be displayed in the tooltip. |
| P | TooltipTitle | Gets or sets the text displayed for the tooltip title |
| P | KeyTip | Returns or sets a string with a maximum of 3 characters that represents the mnemonic that is displayed when using keytips. |

## Aveva.ApplicationFramework.Presentation.PopupStyle

Enumerator used to specify the style of popup menus.

| 类 | 成员 | 说明 |
|---|---|---|
| F | Menu | The menu will popup showing menu items as a standard menu would show them. |
| F | CommandBar | The menu will popup showing the menu items as images only, arranged as they would be in a floating commandbar. |

## Aveva.ApplicationFramework.Presentation.ProgressBar

Class representing a ProgressBar.

| 类 | 成员 | 说明 |
|---|---|---|
| M | Close | Closes the progress bar. |
| M | Show(System.String,System.String,System.Boolean) | Displays the progress bar. |
| M | Show(System.String,System.String,System.Boolean,System.Boolean) | Displays the progress bar. |
| M | Show(Aveva.ApplicationFramework.Presentation.ProgressBarOptions) | Displays the progress bar. |
| P | Title | Gets or sets the title of the window. |
| P | ProgressText | Gets or sets the progress text (left) |
| P | ProgressTextAdditional | Gets or sets the progress text (right) |
| P | ShowCancel | Gets if the Cancel button is shown |
| P | CancelEnabled | Cancel button enable state |
| P | Cancelled | Returns true if Cancel has been requested. |
| P | Progress | Gets or sets the progress value as an integer (0-100) |
| P | Minimum | Minimum for progress range |
| P | Maximum | Maximum for progress range |
| P | UseMarqueeStyle | Gets or set if the progress is Marquee Style. |

## Aveva.ApplicationFramework.Presentation.ProgressBarOptions

Options for controlling progress bar behaviour and appearance

| 类 | 成员 | 说明 |
|---|---|---|
| F | CancelRequest | Called when cancel requested |
| F | OnStart | Called when progressbar ready |
| M | #ctor | Constructor |
| P | CancelEnabled | Cancel button enabled |
| P | CancelVisible | Cancel button visible |
| P | CancelText | Cancel button text |
| P | ShowDialog | When true uses modal dialog, otherwise use status bar progress |
| P | Block | Dialog will also block |
| P | FilterMessages | If blocking then dialog will also filter windows messages |
| P | ProgressText | Text to show indicating current progress (left) |
| P | ProgressTextAdditional | Text to show indicating current progress (right) |
| P | Title | Title for progress bar |
| P | ShowLabel | Show percentage text as label over progress bar |
| P | Minimum | Lower limit for progress range |
| P | Maximum | Upper limit for progress range |
| P | UseMarqueeStyle | When set will act as activity indicator |
| P | MarqueeBounce | When set activity indicator will bounce from side to side |
| P | MarqueeColor | Activity indicator color |
| P | MarqueeSpeed | Activity indicator speed |
| P | TopMost | When set dialog will be forced as topmost window set to null for default behaviour (only true when blocking) |

## Aveva.ApplicationFramework.Presentation.ResourceManager

Provides convenient access to culture-specific resources at runtime.

| 类 | 成员 | 说明 |
|---|---|---|
| M | GetStandardImage(Aveva.ApplicationFramework.Presentation.StandardImage) | Gets a standard image. |
| M | GetString(System.String) | Gets a resource string. |
| M | GetString(System.String,System.String) | Gets a resource string from the named resource set. |
| M | GetIcon(System.String) | Gets a resource Icon. |
| M | GetIcon(System.String,System.String) | Gets a resource Icon from the named resource set. |
| M | GetImage(System.String) | Gets a resource Image. |
| M | GetImage(System.String,System.Int32) | Gets a resource Image. |
| M | GetImage(System.String,System.String) | Gets a resource Image from the named resource set. |
| M | GetImage(System.String,System.String,System.Int32) | Gets a resource Image from the named resource set. |
| M | GetImage(System.String,System.String,System.String) | Gets a resource Image from the named resource set. Uses defaultResourceId if resourceID is not found |
| M | GetImage(System.String,System.String,System.String,System.Int32) | Gets a resource Image from the named resource set. Uses defaultResourceId if resourceID is not found |
| M | GetObject(System.String) | Gets a resource object. |
| M | GetObject(System.String,System.String) | Gets a resource object from the named resource set. |
| M | LoadResourceFile(System.String) | Loads the resource file with given base name. |
| M | ReleaseAllResources | Release all resource unlocking resource files |
| P | Instance | Get instance of resource manager |
| P | ResourceSets | Return a list of all loaded ResourceSets |

## Aveva.ApplicationFramework.Presentation.ResourceSet

Represent a set of culture-specific resource files.

| 类 | 成员 | 说明 |
|---|---|---|
| M | ReleaseResources | Release all resources for this ResourceSet |
| P | Manager | The System.Resources.ResourceManager for the ResourceSet. |
| P | Pathname | Path to resource file |
| P | Basename | Basename for ResourceSet |

## Aveva.ApplicationFramework.Presentation.RibbonBar

Class to represent the RibbonBar

| 类 | 成员 | 说明 |
|---|---|---|
| M | Contains(System.String) | Checks if the provided key is a valid Ribbon element |
| M | GetToolsOf(System.String) | Gets the tools collection of the Ribbon element specified by key |
| P | ApplicationMenu | Gets the ApplicationMenu element |
| P | QuickAccessToolbarTools | Gets the QuickAccessToolbar element |
| P | QATContextMenuTools | Gets the QuickAccessToolbar.ContextMenuTools element |
| P | TabToolbarTools | Gets the TabToolbarTools element |
| P | RibbonContextualTabGroups | Gets the collection of ContextualTabGroup objects currently managed by the Ribbon. |
| P | RibbonTabs | Gets the collection of RibbonTab objects currently managed by the Ribbon. |
| P | Enabled | Gets or sets the enabled state of the RibbonBar. |
| P | Visible | Gets or sets whether the Ribbon is visible. |
| P | Caption | Gets or sets the description displayed in the caption of the Ribbon. |
| P | Tag | Gets or sets the tag property which can be used to logically attach another object or value to a tool. |
| P | RibbonSelectedTabKey | Gets or sets the selected Ribbon Tab by key |
| P | RibbonSelectedTab | Gets or sets the selected Ribbon Tab |

## Aveva.ApplicationFramework.Presentation.RibbonContextualTabGroup

Class to represent a Ribbon RibbonContextualTabGroup contextual tab set.

| 类 | 成员 | 说明 |
|---|---|---|
| P | Key | The Key of the RibbonContextualTabGroup in the RibbonContextualTabGroupsCollection. |
| P | Caption | Gets or sets the description displayed in the Contextual Tab. |
| P | Command | Gets the command object which was associated with the context tab group. |
| P | Colour | Gets or sets the colour of the tabs in this context tab group. |
| P | Enabled | Gets or sets the enabled state of the RibbonContextualTabGroup. |
| P | Visible | Gets or sets whether the RibbonContextualTabGroup is visible. |
| P | Tag | Gets or sets the tag property which can be used to logically attach another object or value to a tool. |

## Aveva.ApplicationFramework.Presentation.RibbonContextualTabGroupEventArgs

Provides data for the RibbonTabGroupAdded and RibbonContextualTabGroupRemoved events.

| 类 | 成员 | 说明 |
|---|---|---|
| M | #ctor(Aveva.ApplicationFramework.Presentation.RibbonContextualTabGroup) | Initialize a new instance of a RibbonContextualTabGroupEventArgs class |
| P | RibbonContextualTabGroup | Gets the RibbonContextTabGroup object associated with the event |

## Aveva.ApplicationFramework.Presentation.RibbonContextualTabGroupEventHandler

Represents the method that will handle RibbonContextualTabGroup related events.


## Aveva.ApplicationFramework.Presentation.RibbonContextualTabGroupsCollection

Class to represent a RibbonContextualTabGroupsCollection.

| 类 | 成员 | 说明 |
|---|---|---|
| M | AddRibbonContextualTabGroup(System.String) | Create and add to the RibbonContextualTabGroupsCollection a new RibbonContextualTabGroup with given Key. |
| M | AddRibbonContextualTabGroup(System.String,Aveva.ApplicationFramework.Presentation.Command) | Create and add to the RibbonContextualTabGroupsCollection a new RibbonContextualTabGroup with given Key and associated Command. |
| M | RemoveRibbonContextualTabGroup(System.String) | Remove the RibbonContextualTabGroup with given Key from the RibbonContextualTabGroupsCollection. |
| M | RemoveRibbonContextualTabGroup(Aveva.ApplicationFramework.Presentation.RibbonContextualTabGroup) | Remove the specified RibbonContextualTabGroup from the RibbonContextualTabGroupsCollection. |
| M | Clear | Remove all RibbonContextualTabGroups from the RibbonContextualTabGroupsCollection. |
| M | Contains(System.String) | Determine if the RibbonContextualTabGroup with the specified Key exists in the RibbonContextualTabGroupsCollection. |
| M | GetEnumerator | Returns an enumerator that can iterate through the RibbonContextualTabGroupCollection. |
| M | CopyTo(System.Array,System.Int32) | Copies the elements of the collection to an Array, starting at a particular Array index. |
| P | Item(System.String) | Indexer to get the RibbonContextualTabGroup with given Key from the RibbonContextualTabGroupsCollection. |
| E | RibbonContextualTabGroupAdded | Occurs after a RibbonContextualTabGroup has been added to the RibbonContextualTabGroupsCollection. |
| E | RibbonContextualTabGroupRemoved | Occurs after a RibbonContextualTabGroup has been removed from the RibbonContextualTabGroupsCollection. |
| P | IsSynchronized | Gets a value indicating whether access to the collection is synchronized (thread-safe). |
| P | Count | Gets the number of elements contained in the collection. |
| P | SyncRoot | Gets an object that can be used to synchronize access to the collection. |

## Aveva.ApplicationFramework.Presentation.RibbonTab

Class to represent a RibbonTab.

| 类 | 成员 | 说明 |
|---|---|---|
| P | Key | The Key of the RibbonTab in the RibbonTabsCollection. |
| P | Caption | Gets or sets the description displayed in the Tab. |
| P | RibbonContextualTabGroup | Gets the RibbonContextualTabGroup containing the RibbonTab. |
| P | Groups | Gets the RibbonTabGroupsCollection containing the groups to display in the RibbonTab. |
| P | Enabled | Gets or sets the enabled state of the RibbonTab. |
| P | Visible | Gets or sets whether the RibbonTab is visible. |
| P | Tag | Gets or sets the tag property which can be used to logically attach another object or value to a tool. |
| P | KeyTip | Returns or sets a string with a maximum of 3 characters that represents the mnemonic that is displayed when using keytips. |

## Aveva.ApplicationFramework.Presentation.RibbonTabEventArgs

Provides data for the RibbonTabAdded and RibbonTabRemoved events.

| 类 | 成员 | 说明 |
|---|---|---|
| M | #ctor(Aveva.ApplicationFramework.Presentation.RibbonTab) | Initialize a new instance of a RibbonTabEventArgs class |
| P | RibbonTab | Gets the RibbonTab object associated with the event This will be null for the home tab |

## Aveva.ApplicationFramework.Presentation.RibbonTabEventHandler

Represents the method that will handle RibbonTab related events.


## Aveva.ApplicationFramework.Presentation.RibbonTabGroup

Class to represent a Ribbon RibbonTab Group.

| 类 | 成员 | 说明 |
|---|---|---|
| P | Key | The Key of the RibbonTabGroup in the RibbonTabGroupsCollection. |
| P | Caption | Gets or sets the description displayed in the Group. |
| P | Tools | Gets the ToolsCollection containing the tools to display in the RibbonTabGroup. |
| P | Enabled | Gets or sets the enabled state of the RibbonTabGroup. |
| P | Visible | Gets or sets whether the RibbonTabGroup is visible. |
| P | DialogBoxLauncherKey | Gets or sets the DialogBoxLauncherKey associated with a group |
| P | Tag | Gets or sets the tag property which can be used to logically attach another object or value to a tool. |
| P | LayoutDirection | Gets or sets the layout direction for the tools in the TabGroup. Default is vertical. |
| P | KeyTip | Returns or sets a string with a maximum of 3 characters that represents the mnemonic that is displayed when using keytips. |

## Aveva.ApplicationFramework.Presentation.RibbonTabGroupEventArgs

Provides data for the RibbonTabGroupAdded and RibbonTabGroupRemoved events.

| 类 | 成员 | 说明 |
|---|---|---|
| M | #ctor(Aveva.ApplicationFramework.Presentation.RibbonTabGroup) | Initialize a new instance of a RibbonTabGroupEventArgs class |
| P | RibbonTabGroup | Gets the RibbonTabGroup object associated with the event |

## Aveva.ApplicationFramework.Presentation.RibbonTabGroupEventHandler

Represents the method that will handle RibbonTabGroup related events.


## Aveva.ApplicationFramework.Presentation.RibbonTabGroupsCollection

Class to represent a RibbonTabGroupCollection.

| 类 | 成员 | 说明 |
|---|---|---|
| M | AddRibbonTabGroup(System.String) | Create and add to the RibbonTabGroupCollection a new RibbonTabGroup with given Key. |
| M | RemoveRibbonTabGroup(System.String) | Remove the RibbonTabGroup with given Key from the RibbonTabGroupCollection. |
| M | RemoveRibbonTabGroup(Aveva.ApplicationFramework.Presentation.RibbonTabGroup) | Remove the specified RibbonTabGroup from the RibbonTabGroupCollection. |
| M | Clear | Remove all RibbonTabGroups from the RibbonTabGroupCollection. |
| M | Contains(System.String) | Determine if the RibbonTabGroup with the specified Key exists in the RibbonTabGroupCollection. |
| M | GetEnumerator | Returns an enumerator that can iterate through the RibbonTabGroupCollection. |
| M | CopyTo(System.Array,System.Int32) | Copies the elements of the collection to an Array, starting at a particular Array index. |
| P | Item(System.String) | Indexer to get the RibbonTabGroup with given Key from the RibbonTabGroupCollection. |
| E | RibbonTabGroupAdded | Occurs after a RibbonTabGroup has been added to the RibbonTabGroupCollection. |
| E | RibbonTabGroupRemoved | Occurs after a RibbonTabGroup has been removed from the RibbonTabGroupCollection. |
| P | IsSynchronized | Gets a value indicating whether access to the collection is synchronized (thread-safe). |
| P | Count | Gets the number of elements contained in the collection. |
| P | SyncRoot | Gets an object that can be used to synchronize access to the collection. |

## Aveva.ApplicationFramework.Presentation.RibbonTabsCollection

Class to represent a RibbonTabCollection.

| 类 | 成员 | 说明 |
|---|---|---|
| M | AddRibbonTab(System.String) | Create and add to the RibbonTabCollection a new RibbonTab with given Key. |
| M | RemoveRibbonTab(System.String) | Remove the RibbonTab with given Key from the RibbonTabCollection. |
| M | RemoveRibbonTab(Aveva.ApplicationFramework.Presentation.RibbonTab) | Remove the specified RibbonTab from the RibbonTabCollection. |
| M | Clear | Remove all RibbonTabs from the RibbonTabCollection. |
| M | Contains(System.String) | Determine if the RibbonTab with the specified Key exists in the RibbonTabCollection. |
| M | GetEnumerator | Returns an enumerator that can iterate through the RibbonTabCollection. |
| M | CopyTo(System.Array,System.Int32) | Copies the elements of the collection to an Array, starting at a particular Array index. |
| P | Item(System.String) | Indexer to get the RibbonTab with given Key from the RibbonTabCollection. |
| P | Tabs | return list of ribbon tabs |
| E | RibbonTabAdded | Occurs after a RibbonTab has been added to the RibbonTabCollection. |
| E | RibbonTabRemoved | Occurs after a RibbonTab has been removed from the RibbonTabCollection. |
| P | IsSynchronized | Gets a value indicating whether access to the collection is synchronized (thread-safe). |
| P | Count | Gets the number of elements contained in the collection. |
| P | SyncRoot | Gets an object that can be used to synchronize access to the collection. |

## Aveva.ApplicationFramework.Presentation.RootToolsCollection

Class representing a RootToolsCollection.

| 类 | 成员 | 说明 |
|---|---|---|
| M | AddButtonTool(System.String,System.String,System.Drawing.Image) | Create and add a new ButtonTool object to the RootToolsCollection. |
| M | AddButtonTool(System.String,System.String,System.Drawing.Image,Aveva.ApplicationFramework.Pre | Create and add a new ButtonTool object to the RootToolsCollection. |
| M | AddButtonTool(System.String,System.String,System.Drawing.Image,System.String) | Create and add a new ButtonTool object to the RootToolsCollection. |
| M | AddButtonTool(System.String,System.String,System.Drawing.Image,System.String,System.Collectio | Create and add a new ButtonTool object to the RootToolsCollection. |
| M | AddComboBoxTool(System.String,System.String,System.Drawing.Image) | Create and add a new ComboBoxTool object to the RootToolsCollection. |
| M | AddComboBoxTool(System.String,System.String,System.Drawing.Image,Aveva.ApplicationFramework.Pre | Create and add a new ComboBoxTool object to the RootToolsCollection. |
| M | AddComboBoxTool(System.String,System.String,System.Drawing.Image,System.String) | Create and add a new ComboBoxTool object to the RootToolsCollection. |
| M | AddComboBoxTool(System.String,System.String,System.Drawing.Image,System.String,System.Collectio | Create and add a new ComboBoxTool object to the RootToolsCollection. |
| M | AddContainerTool(System.String,System.String,System.Windows.Forms.Control) | Create and add a new ContainerTool object to the RootToolsCollection. |
| M | AddContainerTool(System.String,System.String,System.Windows.Forms.Control,Aveva.ApplicationFrame | Create and add a new ContainerTool object to the RootToolsCollection. |
| M | AddContainerTool(System.String,System.String,System.Windows.Forms.Control,System.String) | Create and add a new ContainerTool object to the RootToolsCollection. |
| M | AddContainerTool(System.String,System.String,System.Windows.Forms.Control,System.String,System.C | Create and add a new ContainerTool object to the RootToolsCollection. |
| M | AddMenuTool(System.String,System.String,System.Drawing.Image) | Create and add a new MenuTool object to the RootToolsCollection. |
| M | AddMenuTool(System.String,System.String,System.Drawing.Image,Aveva.ApplicationFramework.Pre | Create and add a new MenuTool object to the RootToolsCollection. |
| M | AddMenuTool(System.String,System.String,System.Drawing.Image,System.String) | Create and add a new MenuTool object to the RootToolsCollection. |
| M | AddMenuTool(System.String,System.String,System.Drawing.Image,System.String,System.Collectio | Create and add a new MenuTool object to the RootToolsCollection. |
| M | AddPopupGalleryTool(System.String,System.String,System.Drawing.Image) | Create and add a new PopupGalleryTool object to the RootToolsCollection. |
| M | AddPopupGalleryTool(System.String,System.String,System.Drawing.Image,Aveva.ApplicationFramework.Pre | Create and add a new PopupGalleryTool object to the RootToolsCollection. |
| M | AddPopupGalleryTool(System.String,System.String,System.Drawing.Image,System.String) | Create and add a new PopupGalleryTool object to the RootToolsCollection. |
| M | AddPopupGalleryTool(System.String,System.String,System.Drawing.Image,System.String,System.Collectio | Create and add a new PopupGalleryTool object to the RootToolsCollection. |
| M | AddLabelTool(System.String,System.String,System.Drawing.Image) | Create and add a new LabelTool object to the RootToolsCollection. |
| M | AddLabelTool(System.String,System.String,System.Drawing.Image,Aveva.ApplicationFramework.Pre | Create and add a new LabelTool object to the RootToolsCollection. |
| M | AddLabelTool(System.String,System.String,System.Drawing.Image,System.String) | Create and add a new LabelTool object to the RootToolsCollection. |
| M | AddLabelTool(System.String,System.String,System.Drawing.Image,System.String,System.Collectio | Create and add a new LabelTool object to the RootToolsCollection. |
| M | AddPopupContainerTool(System.String,System.String,System.Drawing.Image,System.Windows.Forms.Control) | Create and add a new PopupContainerTool object to the RootToolsCollection. |
| M | AddPopupContainerTool(System.String,System.String,System.Drawing.Image,System.Windows.Forms.Control,A | Create and add a new PopupContainerTool object to the RootToolsCollection. |
| M | AddPopupContainerTool(System.String,System.String,System.Drawing.Image,System.Windows.Forms.Control,S | Create and add a new PopupContainerTool object to the RootToolsCollection. |
| M | AddPopupContainerTool(System.String,System.String,System.Drawing.Image,System.Windows.Forms.Control,S | Create and add a new PopupContainerTool object to the RootToolsCollection. |
| M | AddStateButtonTool(System.String,System.String,System.Drawing.Image) | Create and add a new StateButtonTool object to the RootToolsCollection. |
| M | AddStateButtonTool(System.String,System.String,System.Drawing.Image,Aveva.ApplicationFramework.Pre | Create and add a new StateButtonTool object to the RootToolsCollection. |
| M | AddStateButtonTool(System.String,System.String,System.Drawing.Image,System.String) | Create and add a new StateButtonTool object to the RootToolsCollection. |
| M | AddStateButtonTool(System.String,System.String,System.Drawing.Image,System.String,System.Collectio | Create and add a new StateButtonTool object to the RootToolsCollection. |
| M | AddTextBoxTool(System.String,System.String,System.Drawing.Image,System.String) | Create and add a new TextBoxTool object to the RootToolsCollection. |
| M | AddTextBoxTool(System.String,System.String,System.Drawing.Image,System.String,Aveva.Applicatio | Create and add a new TextBoxTool object to the RootToolsCollection. |
| M | AddTextBoxTool(System.String,System.String,System.Drawing.Image,System.String,System.String) | Create and add a new TextBoxTool object to the RootToolsCollection. |
| M | AddTextBoxTool(System.String,System.String,System.Drawing.Image,System.String,System.String,Sy | Create and add a new TextBoxTool object to the RootToolsCollection. |
| M | AddMdiWindowListTool(System.String) | Create and add a new MdiWindowListTool object in the RootToolsCollection. |
| M | AddCommandBarMenuTool(System.String,System.String,System.Drawing.Image) | Create and add a new CommandBarMenuTool object in the RootToolsCollection. |
| M | AddTaskPaneTool(System.String) | Create and add a new TaskPaneTool object in the RootToolsCollection. |
| M | AddPopupColorPickerTool(System.String,System.String,System.Drawing.Image) | Create and add a new PopupColorPickerTool object in the RootToolsCollection |
| M | AddPopupColorPickerTool(System.String,System.String,System.Drawing.Image,Aveva.ApplicationFramework.Pre | Create and add a new PopupColorPickerTool object in the RootToolsCollection |
| M | AddPopupColorPickerTool(System.String,System.String,System.Drawing.Image,System.String) | Create and add a new PopupColorPickerTool object in the RootToolsCollection |
| M | AddPopupColorPickerTool(System.String,System.String,System.Drawing.Image,System.String,System.Collectio | Create and add a new PopupColorPickerTool object in the RootToolsCollection |
| M | AddFontListTool(System.String,System.String,System.Drawing.Image) | Create and add a new FontListTool object in the RootToolsCollection |
| M | AddFontListTool(System.String,System.String,System.Drawing.Image,Aveva.ApplicationFramework.Pre | Create and add a new FontListTool object in the RootToolsCollection |
| M | AddFontListTool(System.String,System.String,System.Drawing.Image,System.String) | Create and add a new FontListTool object in the RootToolsCollection |
| M | AddFontListTool(System.String,System.String,System.Drawing.Image,System.String,System.Collectio | Create and add a new FontListTool object in the RootToolsCollection |
| M | AddListTool(System.String) | Create and add a new ListTool object in the RootToolsCollection |
| M | AddListTool(System.String,Aveva.ApplicationFramework.Presentation.Command) | Create and add a new ListTool object in the RootToolsCollection |
| M | AddListTool(System.String,System.String) | Create and add a new ListTool object in the RootToolsCollection |
| M | AddListTool(System.String,System.String,System.Collections.ArrayList) | Create and add a new ListTool object in the RootToolsCollection |
| M | Clear | Remove all tools from the RootToolsCollection. |
| M | Contains(System.String) | Determine if the tool with the specified Key exists in the RootToolsCollection. |
| M | Remove(System.String) | Remove the tool with the specified Key from the RootToolsCollection. |
| M | GetEnumerator | Returns an enumerator that can iterate through the Collection. |
| M | CopyTo(System.Array,System.Int32) | Copies the elements of the collection to an Array, starting at a particular Array index. |
| P | Item(System.String) | Indexer to get the root tool with given Key from the RootToolsCollection as an ITool object. |
| E | ToolAdded | Occurs after a tool has been added to the RootToolsCollection. |
| E | ToolRemoved | Occurs after a tool has been removed from the RootToolsCollection. |
| P | IsSynchronized | Gets a value indicating whether access to the collection is synchronized (thread-safe). |
| P | Count | Gets the number of elements contained in the collection. |
| P | SyncRoot | Gets an object that can be used to synchronize access to the collection. |

## Aveva.ApplicationFramework.Presentation.SplashScreen

Provides an application SplashScreen.

| 类 | 成员 | 说明 |
|---|---|---|
| M | Show(System.Drawing.Image) | Display a splash screen with the given image. |
| M | Show(System.String) | Display a splash screen with the image defined by the given path or resource id |
| M | Show(System.String,Aveva.ApplicationFramework.Presentation.IApplicationInfo) | Display a splash screen with the image defined by the given path or resource id |
| M | Close | Close the splash screen |
| M | Hide | Hide the splash screen |
| P | Status | Get or set the splash screen status prompt. |
| P | Form | Form used to display the splash screen |

## Aveva.ApplicationFramework.Presentation.StandardImage

Enumeration of standard images

| 类 | 成员 | 说明 |
|---|---|---|
| F | AppWindow |  |
| F | Arrow |  |
| F | Color |  |
| F | Copy |  |
| F | Cut |  |
| F | Delete |  |
| F | DeleteFolder |  |
| F | Document |  |
| F | Filter |  |
| F | Find |  |
| F | FindNext |  |
| F | FullScreen |  |
| F | Help |  |
| F | HTMLPage |  |
| F | Hyperlink |  |
| F | Information |  |
| F | NavBack |  |
| F | NavForward |  |
| F | NewDocument |  |
| F | NewFolder |  |
| F | NewWindow |  |
| F | Open |  |
| F | OpenFolder |  |
| F | Options |  |
| F | Paste |  |
| F | Print |  |
| F | PrintPreview |  |
| F | Properties |  |
| F | Redo |  |
| F | Save |  |
| F | SaveAll |  |
| F | Search |  |
| F | Undo |  |
| F | User |  |
| F | Zoom |  |

## Aveva.ApplicationFramework.Presentation.StateButtonCommandBarDisplayStyle

Enumerator used to specify the display style of a StateButtonTool when it is displayed on a CommandBar or Ribbon.

| 类 | 成员 | 说明 |
|---|---|---|
| F | Button | The StateButtonTool will display like a button. |
| F | Glyph | The StateButtonTool will display with a CheckBox (if it does not belong to an OptionSet) or Radio Button (if it does belong to an OptionSet). |

## Aveva.ApplicationFramework.Presentation.StateButtonMenuDisplayStyle

Enumerator used to specify the display style of a StateButtonTool's image when the tool appears on a menu.

| 类 | 成员 | 说明 |
|---|---|---|
| F | DisplayToolImage | The StateButtonTool's image is displayed with slightly different rendering depending on whether the button is checked or not. |
| F | DisplayCheckmark | A checkmark image is displayed if the tool is checked. No image is displayed if the tool is unchecked. |

## Aveva.ApplicationFramework.Presentation.StateButtonTool

Represents a StateButtonTool.

| 类 | 成员 | 说明 |
|---|---|---|
| E | ToolClick | Occurs when the tool is clicked. |
| P | Command | Gets the command object which was associated with the tool when it was created. |
| P | Checked | Gets or sets whether the tool is in the checked state. |
| P | OptionSetKey | Gets or sets the OptionSet key for the tool. Setting the key assigns the tool to the CommandBarManagers OptionSet which has this key. |
| P | MenuToolUpdateOptions | Gets or sets how properties of an owning MenuTool will be automatically updated |
| P | CommandBarDisplayStyle | Gets or sets the style that determines how the StateButtonTool is displayed on an Toolbar or RibbonGroup. |
| P | MenuDisplayStyle | Gets or sets the style that determines how the image is drawn for the StateButtonTool when the tool is on a PopupMenuTool |
| P | Key | The Key of the tool in the RootToolsCollection |
| P | Tag | Gets or sets the tag property which can be used to logically attach another object or value to a tool. |
| P | Caption | Gets or sets the tool caption |
| P | Tooltip | Gets or sets the tools tooltip |
| P | Image | Gets or sets the image (16x16) displayed on the tool |
| P | LargeImage | Gets or sets the large image (32x32) displayed on the tool |
| P | SmallImage | Gets or sets the image (16x16) displayed on the tool |
| P | IsFirstInGroup | Gets or sets a flag which indicated whether an instance tool is the first in a tool group. A separator will be displayed before a tool if this property is set to true. |
| P | ButtonGroup | Gets or sets the name of the group the instance tool should be contained within when placed on a RibbonGroup. |
| P | DisplayLargeImage | Flag to indicate if a large image should be displayed for an instance of a tool on the ribbon |
| P | ImageOnly | Flag to indicate if the tool should olny display an image and no caption. |
| P | Visible | Gets or sets the visibility of the tool. |
| P | Enabled | Gets or sets the enabled state of the tool. |
| P | DisplayStyle | Gets or sets the display style for a tool. |
| P | Shortcut | Gets or sets the shortcut associated with a tool. |
| P | Category | Gets or sets the tools category |
| P | Value | Gets or sets the value of the tool. |
| P | Arguments | Gets or sets the tools arguments. |
| P | TooltipFormattedText | Gets / sets the formatted text to be displayed in the tooltip. |
| P | TooltipTitle | Gets or sets the text displayed for the tooltip title |
| P | KeyTip | Returns or sets a string with a maximum of 3 characters that represents the mnemonic that is displayed when using keytips. |

## Aveva.ApplicationFramework.Presentation.StatusBar

Represents a Windows style status bar control.

| 类 | 成员 | 说明 |
|---|---|---|
| M | StartProgressDisplay | Signal that progress display to begin |
| M | FinishProgressDisplay | Signal that progress display has ended |
| P | TextMaxSize | Clip text to this size, set to zero for no clipping |
| P | TextTooltipMaxSize | Clip text tooltip to this size, set to zero for no clipping |
| P | ProgressTextMaxSize | Clip progress text to this size, set to zero for no clipping |
| P | Visible | Gets or sets the visibility of the status-bar. |
| P | Text | Gets or sets the text to display in the status-bar text pane. |
| P | Progress | Gets or sets the progress bar value [0-100]. |
| P | ProgressText | Gets or Sets the text that is displayed with the progress bar (left). |
| P | ProgressTextAdditional | Gets or Sets the text that is displayed with the progress bar (right). |
| P | ProgressShowLabel | Flag for progress label overlaying the status-bar |
| P | ProgressMinimum | Lower limit for progress indicator |
| P | ProgressMaximum | Upper limit for progress indicator |
| P | UseMarqueeStyle | Marquee style, not implemented |
| P | MarqueeBounce | Marquee setting, not implemented |
| P | MarqueeColor | Marquee setting, not implemented |
| P | MarqueeSpeed | Marquee setting, not implemented |
| E | OnStart | Called when display ready |
| P | ProgressTitle | Gets or Sets the text that is displayed as a title of the progress bar. |
| P | ShowDateTime | Gets or sets whether the Date and Time should be displayed on the status-bar. |
| P | ShowCapsLock | Gets or sets whether the panel showing the CapsLock state is displayed on the status-bar. |
| P | ShowNumLock | Gets or sets whether the panel showing the NumLock state is displayed on the status-bar. |
| P | ShowScrollLock | Gets or sets whether the panel showing the ScrollLock state is displayed on the status-bar. |
| P | ShowInsertMode | Gets or sets whether the panel showing the InsertMode is displayed on the status-bar. |
| P | Panels | Gets the collection of application defined status-bar panels. |
| P | ShowZoom | Gets or sets whether the ZoomBar is showing |
| P | ZoomLargeChange | Zoom-bar Large Change |
| P | ZoomSmallChange | ZoomBar Small Change |
| P | ZoomMinValue | ZoomBar Minimum Value |
| P | ZoomMaxValue | ZoomBar Maximum Value |
| P | ZoomMidpointValue | ZoomBar Midpoint Value, set to null for automatically determined value |
| P | ZoomValue | ZoomBar current value |
| E | ZoomValueChanged | ZoomBar event fires when zoom value changes |

## Aveva.ApplicationFramework.Presentation.StatusBarPanelsCollection

Represents a collection of status bar panels.

| 类 | 成员 | 说明 |
|---|---|---|
| M | ContainsKey(System.String) | Determines whether the StatusBarPanelsCollection contains a specific key. |
| M | AddTextPanel(System.String,System.String) | Create and add a new StatusBarTextPanel to the collection |
| M | AddTextPanel(System.String,System.String,System.Drawing.Image) | Create and add a new StatusBarTextPanel to the collection |
| M | AddButtonPanel(System.String,System.String) | Create and add a new StatusBarTextPanel to the collection as a button |
| M | AddButtonPanel(System.String,System.String,System.Drawing.Image) | Create and add a new StatusBarTextPanel to the collection as a button |
| M | AddStateButtonPanel(System.String,System.String) | Create and add a new StatusBarTextPanel to the collection as a state button |
| M | AddStateButtonPanel(System.String,System.String,System.Drawing.Image) | Create and add a new StatusBarTextPanel to the collection as a state button |
| M | AddTextPanel(System.String,System.String,Aveva.ApplicationFramework.Presentation.InsertPosit | Create and add a new StatusBarTextPanel to the collection |
| M | AddTextPanel(System.String,System.String,System.Drawing.Image,Aveva.ApplicationFramework.Pre | Create and add a new StatusBarTextPanel to the collection |
| M | AddButtonPanel(System.String,System.String,Aveva.ApplicationFramework.Presentation.InsertPosit | Create and add a new StatusBarTextPanel to the collection as a button |
| M | AddButtonPanel(System.String,System.String,System.Drawing.Image,Aveva.ApplicationFramework.Pre | Create and add a new StatusBarTextPanel to the collection as a button |
| M | AddStateButtonPanel(System.String,System.String,Aveva.ApplicationFramework.Presentation.InsertPosit | Create and add a new StatusBarTextPanel to the collection as a state button |
| M | AddStateButtonPanel(System.String,System.String,System.Drawing.Image,Aveva.ApplicationFramework.Pre | Create and add a new StatusBarTextPanel to the collection as a state button |
| M | GetEnumerator | Returns an enumerator that can iterate through the collection. |
| M | Remove(System.String) | Remove the panel with the given key from the collection. |
| M | CopyTo(System.Array,System.Int32) | Copies the elements of the collection to an Array, starting at a particular Array index. |
| P | Item(System.String) | Indexer which returns an IStatusBarPanel interface for the panel with the given key. |
| P | IsSynchronized | Gets a value indicating whether access to the collection is synchronized (thread-safe). |
| P | Count | Gets the number of elements contained in the collection. |
| P | SyncRoot | Gets an object that can be used to synchronize access to the collection. |

## Aveva.ApplicationFramework.Presentation.StatusBarTextPanel

Represents a StatusBarTextPanel.

| 类 | 成员 | 说明 |
|---|---|---|
| M | StopAlert | Stop text panel flashing following a text change when AlertTextChange is turned on. |
| P | TextMaxSize | Clip text to this size, set to zero for no clipping |
| P | TextTooltipMaxSize | Clip text tooltip to this size, set to zero for no clipping |
| E | PanelClick | Occurs when the panel is clicked |
| E | PanelDoubleClick | Occurs when the panel is double clicked |
| P | Key | Key for the panel. |
| P | Enabled | Returns or sets if the panel is enabled. |
| P | Text | Returns or sets the text associated with the panel. |
| P | Tooltip | Returns or sets the tooltip for the panel. |
| P | Image | Returns or sets the image associated with the panel. |
| P | SizingMode | Returns or sets how the panel can be sized. |
| P | Visible | Returns or sets if the panel is visible. |
| P | Width | Returns or sets the width of the panel. |
| P | Checked | Returns or sets the checked state |
| P | AlertTextChange | Controls if a change in the value of the text panel cause it to start flashing to alert the user. Flashing will stop when the cursor enters the panel. |
| P | AlertFlashCount | The number of times the panel will flash if AlertTextChange in on. Default is 0 which indicates flash will continue until cursor enters the panel. |
| P | HotTrack | Determines whether the a panel's appearance changes when the mouse passes over it. This is only valid for panels which have a PanelClick event handler |

## Aveva.ApplicationFramework.Presentation.TaskBar

Class representing a Microsoft Office style "TaskPane" type toolbar.

| 类 | 成员 | 说明 |
|---|---|---|
| P | HomeTaskPaneToolKey | Returns or sets the key of the tool representing the "home" item. The SelectedTaskPaneToolKey will be set to the HomeTaskPaneToolKey when the home navigation button is pressed. |
| P | SelectedTaskPaneToolKey | Returns or sets the key of the currently selected task pane tool. |
| P | ShowHomeButton | Returns or sets a value indicating whether the home navigation button will be displayed. |
| P | DockedContentExtent | Return or sets the size of the taskbar. Either its width or height depending on where it is docked. |
| P | NavigationButtonStyle | Returns or sets a value indicating how the navigation buttons are used to navigate the items in a TaskPane and can also be used to hide the navigation buttons. |
| E | AfterTaskPaneToolSelected | Event raised after a task pane tool is selected |

## Aveva.ApplicationFramework.Presentation.TaskPaneTool

Class used to represent a single item in a TaskPane.

| 类 | 成员 | 说明 |
|---|---|---|
| P | Control | Gets or sets the control displayed in the TaskPaneTool. NOTE: The Control must also be added to the main windows controls collection. |
| E | ToolClick | Occurs when the TaskPaneTool is selected. |
| P | Key | The Key of the tool in the RootToolsCollection |
| P | Tag | Gets or sets the tag property which can be used to logically attach another object or value to a tool. |
| P | Caption | Gets or sets the tool caption |
| P | Tooltip | Gets or sets the tools tooltip |
| P | Image | Gets or sets the image (16x16) displayed on the tool |
| P | LargeImage | Gets or sets the large image (32x32) displayed on the tool |
| P | SmallImage | Gets or sets the image (16x16) displayed on the tool |
| P | IsFirstInGroup | Gets or sets a flag which indicated whether an instance tool is the first in a tool group. A separator will be displayed before a tool if this property is set to true. |
| P | ButtonGroup | Gets or sets the name of the group the instance tool should be contained within when placed on a RibbonGroup. |
| P | DisplayLargeImage | Flag to indicate if a large image should be displayed for an instance of a tool on the ribbon |
| P | ImageOnly | Flag to indicate if the tool should olny display an image and no caption. |
| P | Visible | Gets or sets the visibility of the tool. |
| P | Enabled | Gets or sets the enabled state of the tool. |
| P | DisplayStyle | Gets or sets the display style for a tool. |
| P | Shortcut | Gets or sets the shortcut associated with a tool. |
| P | Category | Gets or sets the tools category |
| P | Value | Gets or sets the value of the tool. |
| P | Arguments | Gets or sets the tools arguments. |
| P | TooltipFormattedText | Gets / sets the formatted text to be displayed in the tooltip. |
| P | TooltipTitle | Gets or sets the text displayed for the tooltip title |
| P | KeyTip | Returns or sets a string with a maximum of 3 characters that represents the mnemonic that is displayed when using keytips. |

## Aveva.ApplicationFramework.Presentation.TextBoxTool

Represents a TextBoxTool.

| 类 | 成员 | 说明 |
|---|---|---|
| E | ToolClick | Occurs when Enter key is pressed while text field has focus. |
| E | ToolValueChanged | Occurs when the value of the TextBoxTool changes |
| P | Width | Gets or sets the width of the tool. |
| P | DisplayText | Gets or sets the text displayed in the tool. |
| P | Editable | Gets or sets whether the TextBoxTool is editable |
| P | DisplayStyle | Gets or sets the display style for a tool. |
| P | MaxLength | Gets or sets the maximum allowable length of the text that can be entered in the TextBoxTool |
| P | PasswordChar | Gets or sets a value indicating how the characters typed by a user are displayed. |
| P | Command | Gets the command object which was associated with the tool when it was created. |
| P | Key | The Key of the tool in the RootToolsCollection |
| P | Tag | Gets or sets the tag property which can be used to logically attach another object or value to a tool. |
| P | Caption | Gets or sets the tool caption |
| P | Tooltip | Gets or sets the tools tooltip |
| P | Image | Gets or sets the image (16x16) displayed on the tool |
| P | LargeImage | Gets or sets the large image (32x32) displayed on the tool |
| P | SmallImage | Gets or sets the image (16x16) displayed on the tool |
| P | IsFirstInGroup | Gets or sets a flag which indicated whether an instance tool is the first in a tool group. A separator will be displayed before a tool if this property is set to true. |
| P | ButtonGroup | Gets or sets the name of the group the instance tool should be contained within when placed on a RibbonGroup. |
| P | DisplayLargeImage | Flag to indicate if a large image should be displayed for an instance of a tool on the ribbon |
| P | ImageOnly | Flag to indicate if the tool should olny display an image and no caption. |
| P | Visible | Gets or sets the visibility of the tool. |
| P | Enabled | Gets or sets the enabled state of the tool. |
| P | Shortcut | Gets or sets the shortcut associated with a tool. |
| P | Category | Gets or sets the tools category |
| P | Value | Gets or sets the value of the tool. |
| P | Arguments | Gets or sets the tools arguments. |
| P | TooltipFormattedText | Gets / sets the formatted text to be displayed in the tooltip. |
| P | TooltipTitle | Gets or sets the text displayed for the tooltip title |
| P | KeyTip | Returns or sets a string with a maximum of 3 characters that represents the mnemonic that is displayed when using keytips. |

## Aveva.ApplicationFramework.Presentation.TextPlacement

Enumerator used to specify the text placement of a gallery tool item.

| 类 | 成员 | 说明 |
|---|---|---|
| F | Default | The default text placement should be used. |
| F | AboveImage | The text is placed above the image. |
| F | BelowImage | The text is placed below the image. |
| F | LeftOfImage | The text is placed to the left of the image. |
| F | RightOfImage | The text is placed to the right of the image. |

## Aveva.ApplicationFramework.Presentation.ThemeColours

Class which provides a number of Theme colours

| 类 | 成员 | 说明 |
|---|---|---|
| F | HighlightMouseDownGradientDark | Theme Colour |
| F | HighlightMouseDownGradientLight | Theme Colour |
| F | HighlightNotPressedGradientDark | Theme Colour |
| F | HighlightNotPressedGradientLight | Theme Colour |
| F | HighlightPressedGradientDark | Theme Colour |
| F | HighlightPressedGradientLight | Theme Colour |
| F | PressedGradientDark | Theme Colour |
| F | PressedGradientLight | Theme Colour |
| F | ToolbarGradientDark | Theme Colour |
| F | ToolbarGradientLight | Theme Colour |
| F | MainMenuBarGradientDark | Theme Colour |
| F | MainMenuBarGradientLight | Theme Colour |
| F | SplitterBorder | Theme Colour |

## Aveva.ApplicationFramework.Presentation.ToolDisplayStyle

Enumerator used to specify the display style of a tool.

| 类 | 成员 | 说明 |
|---|---|---|
| F | Default | The tool is displayed in a default style. |
| F | DefaultForToolType | The tool is displayed based on the default for the tools type and its location. |
| F | TextOnlyAlways | The tool is always displayed as text only. |
| F | TextOnlyInMenus | The Tool is displayed as a graphic when located on a Toolbar, and displayed as text when located on a Menu. |
| F | ImageAndText | The tool is displayed using its assigned image and text. This setting is ignored when the item is on a top-level menu. |
| F | ImageOnlyOnToolbars | The Tool is displayed as a graphic when located on a Toolbar, and displayed as image and text when located on a Menu. |

## Aveva.ApplicationFramework.Presentation.ToolEventArgs

Provides information for Tool events.

| 类 | 成员 | 说明 |
|---|---|---|
| M | #ctor(System.String) |  |
| P | Key | The tools key. |

## Aveva.ApplicationFramework.Presentation.ToolEventHandler

Represents the method that will handle Tool related events.


## Aveva.ApplicationFramework.Presentation.ToolsCollection

Class representing a ToolsCollection.

| 类 | 成员 | 说明 |
|---|---|---|
| M | IndexOf(System.String) | Get the index of the tool with given Key from the ToolsCollection. Returns -1 if tool is not in the collection. |
| M | AddTool(System.String) | Create an instance of a root tool and add it to the ToolsCollection, with the same Key. |
| M | InsertTool(System.String,System.Int32) | Create an instance of a root tool and insert it into the ToolsCollection at the given index, with the same Key. |
| M | Clear | Remove all tool instances from the ToolsCollection. |
| M | Contains(System.String) | Determine if the tool instance with the specified Key exists in the ToolsCollection. |
| M | Remove(System.String) | Remove the tool instance with the specified Key from the ToolsCollection. |
| M | RemoveAt(System.Int32) | Remove the tool instance at the specified index position from the ToolsCollection. |
| M | GetEnumerator | Returns an enumerator that can iterate through the Collection. |
| M | CopyTo(System.Array,System.Int32) | Copies the elements of the collection to an Array, starting at a particular Array index. |
| P | Item(System.Int32) | Indexer to get the instance of the tool at the specified index of the ToolsCollection as an ITool object. |
| P | Item(System.String) | Indexer to get the instance of the tool with given Key from the ToolsCollection as an ITool object. |
| P | IsSynchronized | Gets a value indicating whether access to the collection is synchronized (thread-safe). |
| P | Count | Gets the number of elements contained in the collection. |
| P | SyncRoot | Gets an object that can be used to synchronize access to the collection. |

## Aveva.ApplicationFramework.Presentation.UpdateOptions

Enumerations for the options for automatically updating the state of a MenuTool following state changes to an child StateButtonTool or ButtonTool. This enumeration can be treated as a bit field; that is, a set of flags. Bit fields can be combined using a bitwise OR operation.

| 类 | 成员 | 说明 |
|---|---|---|
| F | None | No automatic updating. |
| F | Image | Update image of MenuTool. |
| F | ToolTip | Update tooltip of MenuTool. |
| F | Command | Update associated command of MenuTool. |
| F | CheckedState | Update Checked state of MenuTool. |
| F | All | Update Image, Tooltip, Command and CheckedState. |
| F | ResetOnUncheck | Restore MenuTool state after unchecking a child StateButtonTool. |

## Aveva.ApplicationFramework.Presentation.ValueList

Class representing a ValueList, which is a collection of ValueListItem objects. It is typical assigned to a ComboBoxTool as the list of options displayed as the dropdown list.

| 类 | 成员 | 说明 |
|---|---|---|
| M | Add(System.String) | Create and add a new ValueListItem object to the ValueList. Note that the ValueListItem created will contain the given DisplayText and a default DataValue with value (object)DisplayText. |
| M | Add(System.String,System.Object) | Create and add a new ValueListItem object to the ValueList. |
| M | Add(System.String,System.Object,System.Drawing.Image) | Create and add a new ValueListItem object to the ValueList. |
| M | Insert(System.String,System.Int32) | Create and insert a new ValueListItem object into the ValueList. Note that the ValueListItem created will contain the given DisplayText and a default DataValue with value (object)DisplayText. |
| M | Insert(System.String,System.Object,System.Int32) | Create and insert a new ValueListItem object into the ValueList. |
| M | Insert(System.String,System.Object,System.Drawing.Image,System.Int32) | Create and insert a new ValueListItem object into the ValueList. |
| M | Clear | Remove all ValueListItems from the ValueList. |
| M | Remove(System.String) | Remove the ValueListItem with the specified DisplayText from the ValueList. |
| M | Remove(Aveva.ApplicationFramework.Presentation.ValueListItem) | Remove the specified ValueListItem object from the ValueList. |
| M | Remove(System.Int32) | Remove the ValueListItem at the specified index position from the ValueList. |
| M | GetEnumerator | Returns an enumerator that can iterate through the Collection. |
| M | CopyTo(System.Array,System.Int32) | Copies the elements of the collection to an Array, starting at a particular Array index. |
| P | Item(System.Int32) | Indexer to get the ValuListItem at the given position index from the ValueList. |
| P | Item(System.String) | Indexer to get the ValuListItem with given DisplayText from the ValueList. |
| P | SortStyle | Set the SortStyle for the ValueList. ValueListSortStyle enumeration specifies how the ValueListItems will be sorted for display. |
| P | DisplayStyle | Set the DisplayStyle for the ValueList. ValueListDisplayStyle enumeration specifies what properties of ValueListItems will be displayed. |
| P | IsSynchronized | Gets a value indicating whether access to the collection is synchronized (thread-safe). |
| P | Count | Gets the number of elements contained in the collection. |
| P | SyncRoot | Gets an object that can be used to synchronize access to the collection. |

## Aveva.ApplicationFramework.Presentation.ValueListDisplayStyle

Enumeration for specifying what property of a value list item will be displayed in each item of the DropDown list

| 类 | 成员 | 说明 |
|---|---|---|
| F | DataValue | Text associated with the data value is display in the drop down list. |
| F | DataValueAndPicture | Text associated with the data value and also picture that a value list item's appearance object is assigned to will be displayed. |
| F | Default | Default value list display style. |
| F | DisplayText | Display text value assigned to the value list item will be displayed in each item of the drop down list. |
| F | DisplayTextAndPicture | Display text and also picture that a value list item's appearance object is assigned to will be displayed. |
| F | Picture | Only the picture will be displayed in each item of the drop down list. |

## Aveva.ApplicationFramework.Presentation.ValueListItem

Class representing a ValueListItem, which can be a member of ValueList.

| 类 | 成员 | 说明 |
|---|---|---|
| P | DisplayText | Gets or sets the text which will be displayed for this item in the ValueList. |
| P | DataValue | Gets or sets the DataValue Object for this item in the ValueList. |
| P | Image | Gets or sets the Icon which may be displayed for this item in the ValueList. |

## Aveva.ApplicationFramework.Presentation.ValueListSortStyle

Enumeration for specifying how value list items will be sorted when displaying value list items in a drop down list

| 类 | 成员 | 说明 |
|---|---|---|
| F | Ascending | Sort ascending by display text. |
| F | AscendingByValue | Sort ascending by value. |
| F | Descending | Sort descending by display text. |
| F | DescendingByValue | Sort descending by value. |
| F | None | No sorting. |

## Aveva.ApplicationFramework.Presentation.WindowEventArgs

Provides data for the WindowAdded event.

| 类 | 成员 | 说明 |
|---|---|---|
| M | #ctor(Aveva.ApplicationFramework.Presentation.IWindow) | Initialize a new instance of a WindowEventArgs class |
| P | Window | Gets the Window object associated with the event |

## Aveva.ApplicationFramework.Presentation.WindowEventHandler

Represents the method that will handle Window related events.


## Aveva.ApplicationFramework.Presentation.WindowManager

Provides access to window related facilities.

| 类 | 成员 | 说明 |
|---|---|---|
| M | CreateDockedWindow(System.String,System.String,System.Windows.Forms.Control,Aveva.ApplicationFrame | Creates and adds to the WindowsCollection a new DockedWindow. |
| M | CreateMdiWindow(System.String,System.String,System.Windows.Forms.Control) | Creates and adds to the WindowsCollection a new MdiWindow |
| M | LoadWindowLayout | Loads the docked window layout. |
| M | SaveWindowLayout | Saves the docked window layout. |
| M | SaveWindowPlacement(System.Windows.Forms.Form) | Save the current placement information for the given form. |
| M | RestoreWindowPlacement(System.Windows.Forms.Form) | Restore the placement information for the given form. If the saved placement information would result in a window that is completely off the screen, the system will automatically adjust the coordinates so that the window |
| M | FirePreEventLoop | Fires the PreEventLoop event. |
| P | Instance | Get instance of window manager |
| P | MainForm | Gets the main application Form |
| P | SplashScreen | Gets the splashscreen object. |
| P | StatusBar | Gets the StatusBar object. |
| P | Windows | Gets the WindowCollection object. |
| P | TabbedMdi | Gets or sets whether MDI windows are displayed as tabbed windows. |
| P | ProgressBar | Gets ProgressBar object. |
| E | WindowLayoutLoaded | Event Raised when window layout is loaded |
| E | WindowAdded | Event Raised when a new window is added. |
| E | PreEventLoop | Event Raised just before the event loop starts |
| E | ClipboardChanged | Event raised when the value of the system clipboard changes. |
| P | Enabled | Get or set a property which controls the enabled state of all docked windows |
| P | ActiveWindow | Gets the current active window, either a docked one or an MDI one. |

## Aveva.ApplicationFramework.Presentation.WindowsCollection

Provides access to a collection of application windows.

| 类 | 成员 | 说明 |
|---|---|---|
| M | ContainsKey(System.String) | Determines whether the WindowCollection contains a specific key. |
| M | GetEnumerator | Returns an enumerator that can iterate through the collection. |
| M | Remove(System.String) | Remove the window with the given key from the collection. |
| M | CopyTo(System.Array,System.Int32) | Copies the elements of the collection to an Array, starting at a particular Array index. |
| P | Item(System.String) | Indexer which returns an IWindow interface for the window with the given key. |
| P | IsSynchronized | Gets a value indicating whether access to the collection is synchronized (thread-safe). |
| P | Count | Gets the number of elements contained in the collection. |
| P | SyncRoot | Gets an object that can be used to synchronize access to the collection. |