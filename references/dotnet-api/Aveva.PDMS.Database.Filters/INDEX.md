---
title: Aveva.PDMS.Database.Filters Namespace
namespace: Aveva.PDMS.Database.Filters
source: Aveva.Pdms.Database.Filters
---

# Aveva.PDMS.Database.Filters Namespace

## Classes

| 类型 | 描述 |
|------|------|
| [AndFilter](Aveva.PDMS.Database.Filters.AndFilter.md) | AND two or more filters. |
| [AssemblyPlanningFilter](Aveva.PDMS.Database.Filters.AssemblyPlanningFilter.md) | Summary description for AssemblyPlanningFliter. |
| [AttributeCompoundFilter](Aveva.PDMS.Database.Filters.AttributeCompoundFilter.md) | This class does any of AND, OR, NOT AND, NOT ALL. CLASS IS UNDER REVIEW- DO NOT USE |
| [AttributeFalseFilter](Aveva.PDMS.Database.Filters.AttributeFalseFilter.md) | Tests if a boolean attribute value is valid and false |
| [AttributeLikeFilter](Aveva.PDMS.Database.Filters.AttributeLikeFilter.md) | Returns true if attribute value matches given string, allowing for wild characters. Wild characters are '*' for mutiple wild characters and '?' for a single wild charcter. //These are consistent with PML. CLASS IS UNDER REVIEW- DO NOT USE |
| [AttributeListFilter](Aveva.PDMS.Database.Filters.AttributeListFilter.md) | Filter to compare an attribute against a list of potential values. |
| [AttributeRangeFilter](Aveva.PDMS.Database.Filters.AttributeRangeFilter.md) | Filter to test if attribute is in a given range. CLASS IS UNDER REVIEW- DO NOT USE |
| [AttributeRefFilter](Aveva.PDMS.Database.Filters.AttributeRefFilter.md) | Filter to test if a ref attribute value matches a given value |
| [AttributeTrueFilter](Aveva.PDMS.Database.Filters.AttributeTrueFilter.md) | Returns true if boolean attribute is valid and true |
| [AttributeValueFilter](Aveva.PDMS.Database.Filters.AttributeValueFilter.md) | General filter to test whether the value of any type of attribute matches a given value CLASS IS UNDER REVIEW- DO NOT USE |
| [BaseAttributeFilter](Aveva.PDMS.Database.Filters.BaseAttributeFilter.md) | Abstract Base Class for attribute filters CLASS IS UNDER REVIEW- DO NOT USE |
| [BaseFilter](Aveva.PDMS.Database.Filters.BaseFilter.md) | This is the base class for element filters. Derived classes must implement new versions of Valid(), ScanBelow() and Clone(). The main use of filters is when scanning the database hierarchy looking for elements of a particular criteria. e.g. all Branches. |
| [BelowFilter](Aveva.PDMS.Database.Filters.BelowFilter.md) | Filter to test if element is below an element for which the given filter is true. |
| [BelowOrAtFilter](Aveva.PDMS.Database.Filters.BelowOrAtFilter.md) | Filter to test if element is below or at an element for which the given filter is true. |
| [BelowOrAtType](Aveva.PDMS.Database.Filters.BelowOrAtType.md) | Filter to test if element is at or below given element types. |
| [BelowType](Aveva.PDMS.Database.Filters.BelowType.md) | As for the Below filter, but more efficient in the case where we want to test on type only |
| [CompoundFilter](Aveva.PDMS.Database.Filters.CompoundFilter.md) | Filter designed specifically for use in the explorer. It is composed of the following - list of filters for elements to show - list of filters for elements to skip - list of filters for elements to hide if there are no 'show' or 'showDescendants then ALL elements considered to be shown. |
| [DBElementCollection](Aveva.PDMS.Database.Filters.DBElementCollection.md) | Class to iterate through the database hierarchy returning the elements that match the supplied filter. The scan starts at a given element. If no filter is given, then all elements below the start element are returned. The actual iteration is done via an enumerator. |
| [DBElementEnumerator](Aveva.PDMS.Database.Filters.DBElementEnumerator.md) | Enumerator to iterate through a scan defined by the DBElementCollection class. |
| [DBTypeFilter](Aveva.PDMS.Database.Filters.DBTypeFilter.md) | Returns true if DB is of a given type |
| [DraftAdminFilter](Aveva.PDMS.Database.Filters.DraftAdminFilter.md) | Specific Filter to be used by the explorer for Draft Admin users. |
| [DraftFilter](Aveva.PDMS.Database.Filters.DraftFilter.md) | Specific Filter to be used by the explorer for Draft DBs. |
| [ElementTreeNavigator](Aveva.PDMS.Database.Filters.ElementTreeNavigator.md) | Class to navigate a Dabacon tree taking into account the given filters. It allows the scan to continue at any point in the tree. The class is for use by the Explorer. The tree view presented is compressed to remove any 'skipped' elements. |
| [EquipmentFilter](Aveva.PDMS.Database.Filters.EquipmentFilter.md) | Specific Filter to be used by the explorer when designing equipment. |
| [FalseFilter](Aveva.PDMS.Database.Filters.FalseFilter.md) | Filter that always returns false. |
| [FieldIntFilter](Aveva.PDMS.Database.Filters.FieldIntFilter.md) | Returns true if DbElementType integer field is valid and equal to val |
| [FieldTrueFilter](Aveva.PDMS.Database.Filters.FieldTrueFilter.md) | Filter to return true if Element type field is valid and true |
| [HangerFilter](Aveva.PDMS.Database.Filters.HangerFilter.md) | Specific Filter to be used by the explorer when designing hangers. |
| [HideBelowFilter](Aveva.PDMS.Database.Filters.HideBelowFilter.md) | Filter to hide all elements below an element of a given type. e.g. hide all elements below a group. It returns true if not an element to hide. Used by the explorer. |
| [HideFilter](Aveva.PDMS.Database.Filters.HideFilter.md) | Filter to hide elements of given type. i.e. returns true if not an element to hide. Used by the explorer. If an element is hidden, its descendents will also be hidden. |
| [InvisibleFilter](Aveva.PDMS.Database.Filters.InvisibleFilter.md) | Filter for determining visibility in explorer. |
| [OrFilter](Aveva.PDMS.Database.Filters.OrFilter.md) | Class to 'OR' together two or more existing filters. |
| [PipingFilter](Aveva.PDMS.Database.Filters.PipingFilter.md) | Specific Filter to be used by the explorer for elements relevant to a piping Engineer. |
| [SchematicElectricalFilter](Aveva.PDMS.Database.Filters.SchematicElectricalFilter.md) | Specific Filter to be used by the explorer for doing electricals. |
| [SchematicHVACFilter](Aveva.PDMS.Database.Filters.SchematicHVACFilter.md) | Specific Filter to be used by the explorer for doing schematic hvac. |
| [SchematicPipingFilter](Aveva.PDMS.Database.Filters.SchematicPipingFilter.md) | Specific Filter to be used by the explorer for doing schematic pipes. |
| [ShowDescendants](Aveva.PDMS.Database.Filters.ShowDescendants.md) | Filter to show elements of given type plus ascendants and descendants. Class is used by the Explorer. |
| [ShowFilter](Aveva.PDMS.Database.Filters.ShowFilter.md) | Filter to show elements of given type plus ancestors. When testing ancestors, the filter checks that valid descendants. actually exist rather than possibly exist. Class is used by the explorer. |
| [SkipFilter](Aveva.PDMS.Database.Filters.SkipFilter.md) | Filter to skip elements of given type. i.e. returns true if not an element to skip. Class is used by the explorer to flatten the tree view. If an element is skipped, its descendents will NOT be skipped. |
| [StructuralFilter](Aveva.PDMS.Database.Filters.StructuralFilter.md) | Specific Filter to be used by the explorer for elements relevant to a structural Engineer. |
| [SystemFilter](Aveva.PDMS.Database.Filters.SystemFilter.md) | Specific Filter to be used by the explorer on the system DB. |
| [TrueFilter](Aveva.PDMS.Database.Filters.TrueFilter.md) | Filter that always returns true. |
| [TypeFilter](Aveva.PDMS.Database.Filters.TypeFilter.md) | Tests whether an element is of a given type. The class makes ensures that only valid parts of the database are returned in the ScanBelow() method. This is important for performance. |

## Enumerations

| 类型 | 描述 |
|------|------|
| [BooleanOperator](Aveva.PDMS.Database.Filters.BooleanOperator.md) |  |
| [TestOperator](Aveva.PDMS.Database.Filters.TestOperator.md) |  |
