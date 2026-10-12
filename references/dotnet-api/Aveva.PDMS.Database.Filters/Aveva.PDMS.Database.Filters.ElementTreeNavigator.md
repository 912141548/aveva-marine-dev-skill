---
title: Aveva.PDMS.Database.Filters.ElementTreeNavigator Class
namespace: Aveva.PDMS.Database.Filters
assembly: PDMSFilters
kind: Class
source: Aveva.Pdms.Database.Filters
---

# Aveva.PDMS.Database.Filters.ElementTreeNavigator Class

> Class to navigate a Dabacon tree taking into account the given filters. It allows the scan to continue at any point in the tree. The class is for use by the Explorer. The tree view presented is compressed to remove any 'skipped' elements.

## Syntax

```csharp
public class ElementTreeNavigator
```

## Inheritance

`System.Object` → `Aveva.PDMS.Database.Filters.ElementTreeNavigator`

## Thread Safety

Public static ( Shared in Visual Basic) members of this type are
safe for multithreaded operations. Instance members are not guaranteed to be
thread-safe.

## Requirements

Namespace:
Aveva.PDMS.Database.Filters
Assembly: PDMSFilters (in PDMSFilters.dll)

## Constructors

#### `ElementTreeNavigator` Constructor

Constructor taking root element and filter

```csharp
public ElementTreeNavigator( DbElement ele , CompoundFilter filter );
```

**Parameters**

- **ele** — 
- **filter** —

## Properties

#### `Filter` Property

Filter to use

```csharp
public CompoundFilter Filter {get; set;}
```

#### `TopElement` Property

root element

```csharp
public Aveva.Pdms.Database.DbElement TopElement {get; set;}
```

## Methods

#### `DbWorldMembersInScan` Method

Return members at world level

```csharp
public DbElement[] DbWorldMembersInScan( Db db );
```

**Parameters**

- **db** — 

**Return Value**

list of members satisfying filter

#### `FirstMemberInScan` Method

Get the first member.

```csharp
public DbElement FirstMemberInScan( DbElement startce );
```

**Parameters**

- **startce** —

#### `HasMember` Method

has element any members that satisfy the filter and is of given type.

```csharp
public bool HasMember( DbElement ele , DbElementType eleType );
```

**Parameters**

- **ele** — 
- **eleType** — element type to match

#### `HasMembers` Method

returns true if element has members that satisfy the filter

```csharp
public bool HasMembers( DbElement ele );
```

**Parameters**

- **ele** —

#### `MembersInScan` Method

Return list of members below given element. The method also works for secondary hierarchies.

```csharp
public DbElement[] MembersInScan( DbElement ele );
```

**Parameters**

- **ele** — element

**Return Value**

list of members satisfying filter

#### `NextInScan` Method

Get next element at this level that matches filter

```csharp
public DbElement NextInScan( DbElement startce );
```

**Parameters**

- **startce** —

#### `Parent` Method

First ascendant that satisfies filter

```csharp
public DbElement Parent( DbElement ele );
```

**Parameters**

- **ele** —
