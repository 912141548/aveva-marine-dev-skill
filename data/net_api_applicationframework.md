
# Aveva.ApplicationFramework API 参考(官方 XML 文档)

类型数:15


## Aveva.ApplicationFramework.Addin

Class to represent an ApplicationFramework Addin

| 类 | 成员 | 说明 |
|---|---|---|
| M | Start | Calls the Start method on the Addin interface |
| M | Stop | Calls the Stop method on the Addin interface |
| P | Name | Addin Name |
| P | Description | Addin Description |
| P | Assembly | Assembly containing the Addin |
| P | IsStarted | Get whether the addins Start method has been called. |
| P | IAddinInterfaceObject | Gets the objects which implements the addin IAddin interface |

## Aveva.ApplicationFramework.AddinEventArgs

Class used to hold the event arguments in Addin related events

| 类 | 成员 | 说明 |
|---|---|---|
| M | #ctor(Aveva.ApplicationFramework.Addin) | Constructor for AddinEventArgs |
| P | Addin | Gets the Addin |

## Aveva.ApplicationFramework.AddinEventHandler

Represents the method that will handle addin related events.


## Aveva.ApplicationFramework.AddinManager

Provides properties and methods for the management of ApplicationFramework Addins.

| 类 | 成员 | 说明 |
|---|---|---|
| M | Load(System.String) | Loads the Addin defined in the specified assembly |
| M | Unload(Aveva.ApplicationFramework.Addin) | Stop the given Addin and remove it from the Addins collection |
| M | LoadAddins | This method will attempt to load all the addins that are defined in the XML file called 'Application.Name'Addins.xml located in the same directory as the application executable. |
| M | StartAddins | This method iterates through the Addins collection and calls the Start method on each of the addins. |
| M | StopAddins | This method iterates through the Addins collection and calls the Stop method on each of the addins. |
| M | FindAddinFromAssembly(System.Reflection.Assembly) | Return addin defined in assembly |
| M | GetInterfaceAddin(System.String) | Returns an InterfaceAddin give a name |
| P | Instance | Get instance of addin manager |
| P | Addins | Returns an AddinCollection of Addin objects |
| E | AddinLoaded | Event fired when an Addin is loaded |
| E | AddinUnloaded | Event fired when an Addin is unloaded |
| E | AddinStarting | Event fired when an Addin is starting |
| E | AddinStarted | Event fired when an Addin is started |

## Aveva.ApplicationFramework.AddinsCollection

Class to represent the collection of loaded ApplicationFramework Addins

| 类 | 成员 | 说明 |
|---|---|---|
| M | GetEnumerator | Returns an enumerator that can iterate through the Addin collection |
| M | CopyTo(System.Array,System.Int32) | Copies the collection or a portion of it to a one-dimensional array. |
| P | Item(System.Int32) | Indexer which returns the Addin with a given index |
| P | Item(System.String) | Indexer which retunrs the Addin with the given name |
| P | IsSynchronized | Gets a value indicating whether access to the collection is synchronized (thread-safe). |
| P | Count | Gets the number of Addins actually contained in the collection. |
| P | SyncRoot | Gets an object that can be used to synchronize access to the collection. |

## Aveva.ApplicationFramework.Diagnostics

Class with static methods to display process metrics

| 类 | 成员 | 说明 |
|---|---|---|
| M | WriteModules | Write list of loaded modules |
| M | WriteProcessorTime(System.String) | Write processor usage time information |
| M | WriteProcessElapsedTime(System.String) | Write proccess elapsed time information |

## Aveva.ApplicationFramework.ElapseTimer

| 类 | 成员 | 说明 |
|---|---|---|
| M | Start | Start the timer |
| M | Stop | Stop timer |
| M | WriteDuration(System.String) | Write timer duration information |
| M | WriteDuration(System.Boolean,System.String) | Write timer duration information |
| M | MessageBoxDuration(System.String) | Write timer duration information |
| P | Duration | Return the duration of the timer (in seconds) |
| P | Frequency | Frequency of timer (no counts in one second on this machine) |

## Aveva.ApplicationFramework.IAddin

Interface which enables communication between the framework and the addin.

| 类 | 成员 | 说明 |
|---|---|---|
| M | Start(Aveva.ApplicationFramework.ServiceManager) | Start the Addin |
| M | Stop | Stop the Addin |
| P | Name | Name of Addin |
| P | Description | Description of Addin |

## Aveva.ApplicationFramework.LogViewer

Optionally buffered log viewer

| 类 | 成员 | 说明 |
|---|---|---|
| M | #ctor | Constructor |
| M | LogMessage(System.String) | Log a text message |
| M | LogMessageFormat(System.String,System.Object[]) | Log a formatted text message |
| F | components | Required designer variable. |
| M | Dispose(System.Boolean) | Clean up any resources being used. |
| M | InitializeComponent | Required method for Designer support - do not modify the contents of this method with the code editor. |
| P | Running | Set the running flag, will flush buffers when true |

## Aveva.ApplicationFramework.ServiceEventArgs

Class used to hold the event arguments in SeviceManager related events

| 类 | 成员 | 说明 |
|---|---|---|
| M | #ctor(System.Type) | Initializes a new instance of the ServiceEventArgs class. |
| P | Service | Gets the service which was added for removed |

## Aveva.ApplicationFramework.ServiceEventHandler

Represents the method that will handle service related events.


## Aveva.ApplicationFramework.ServiceManager

Provides a means by which the various components of the ApplicationFramework (e.g. Presentation Component) can publish their services. The ServiceManager also acts as a service provider responding to requests for services.

| 类 | 成员 | 说明 |
|---|---|---|
| M | GetService(System.Type) | Gets the service object of the specified type, if it is available. |
| M | AddService(System.Type,System.Object) | Adds the specified service to the ServiceManager service container. |
| M | AddService(System.Type,System.ComponentModel.Design.ServiceCreatorCallback) | Adds the specified service to the service container. |
| M | AddService(System.Type,System.Object,System.Boolean) | Adds the specified service to the service container, and optionally promotes the service to any parent service containers. |
| M | AddService(System.Type,System.ComponentModel.Design.ServiceCreatorCallback,System.Boolean) | Adds the specified service to the service container, and optionally promotes the service to parent service containers. |
| M | RemoveService(System.Type) | Removes the specified service type from the serviceManager service container. |
| M | RemoveService(System.Type,System.Boolean) | Removes the specified service type from the service container, and optionally promotes the service to parent service containers. |
| P | Instance | Get instance of service manager |
| E | ServiceAdded | Event raised when a service is added to the service manager |
| E | ServiceRemoved | Event raised when a service is removed from the service manager |
| P | ApplicationName | Gets the name of the application. |

## Aveva.ApplicationFramework.SettingsGroup

Class that represents a named colletion of keyed objects which represent application settings

| 类 | 成员 | 说明 |
|---|---|---|
| M | LoadSettings | Load the saved settings for this group |
| M | LoadSettings(System.Boolean) | Load the settings with option to force reload |
| M | SaveSettings | Save the settings for this group |
| M | Clear | Clear all items from the settings group |
| M | Remove(System.String) | Remove the setting with the given key from the search group |
| M | GetEnumerator | Returns an enumerator that can iterate through the SettingsGroup. |
| M | CopyTo(System.Array,System.Int32) | Copies the collection or a portion of it to a one-dimensional array. |
| M | Remove(System.Object) | Removes the object with the specified key from the SettingsGroup |
| P | Name | Name of settings group |
| P | Directory | The name of the directory into which the settings for this group will be persisted |
| P | ReadOnly | Gets or Sets the Read Only staus of a settings group |
| P | Item(System.String) | Indexer to return the object associated with the given key |
| P | IsSynchronized | Gets a value indicating whether access to the collection is synchronized (thread-safe). |
| P | Count | Gets the number of items actually contained in the collection. |
| P | SyncRoot | Gets an object that can be used to synchronize access to the collection. |

## Aveva.ApplicationFramework.SettingsGroupsCollection

A collection of SettingsGroup objects

| 类 | 成员 | 说明 |
|---|---|---|
| M | GetEnumerator | Returns an enumerator that can iterate through the SettingsGroupCollection. |
| M | CopyTo(System.Array,System.Int32) | Copies the collection or a portion of it to a one-dimensional array. |
| P | Item(System.String) | Indexer to resturn the SettingsGroup with the given name. |
| P | IsSynchronized | Gets a value indicating whether access to the collection is synchronized (thread-safe). |
| P | Count | Gets the number of Addins actually contained in the collection. |
| P | SyncRoot | Gets an object that can be used to synchronize access to the collection. |

## Aveva.ApplicationFramework.SettingsManager

Class to manage an applications settings

| 类 | 成员 | 说明 |
|---|---|---|
| M | AddGroup(System.String,System.String) | Adds a new SettingsGroup with the given name. |
| M | LoadSettings | Loads the settings from serialized data. |
| M | SaveSettings | Saves the settings. |
| P | Instance | Get instance of settings manager |
| P | SettingsGroups | Gets the collection of SettingsGroups |
| P | Directory | Sets the parent directory into which the settings will be serialized. The defaults to C:\Documents and Settings\'User Name'\Local Settings\Application Data\Aveva\'Application Name' |