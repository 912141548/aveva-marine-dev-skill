---
title: Aveva.Pdms.Database Namespace
namespace: Aveva.Pdms.Database
source: Aveva.Pdms.Database
---

# Aveva.Pdms.Database Namespace

## Classes

| 类型 | 描述 |
|------|------|
| [DatabaseService](Aveva.Pdms.Database.DatabaseService.md) | Class to open a project |
| [Db](Aveva.Pdms.Database.Db.md) | This class provides information on the opened DB Additional information on the DB (e.g foreign, size, extractParent etc) can be obtain from the %DB DbElement object Some of the information avialable on the %DB object is also repeated here for conveniance, e.g. DBnumber, type. If the MDB is closed, the Db and DbSession objects will no longer be valid. Methods relating to savework, claims, extract operations are available via the MDB class |
| [DbAttribute](Aveva.Pdms.Database.DbAttribute.md) | The class has two purposes: i) Instances of the class are used to identify and pass around attributes ii) The class can be used to get meta data about an attribute. e.g. type, size, Name, pseudo or not, etc The class is valid for system attributes and UDAS. Object instances are created for all system atttributes. These instances are in DbAttributeInstance class All methods that pass in an attribute should pass a DbAttribute object rather than a string that represents the attribute |
| [DbAttributeComparer](Aveva.Pdms.Database.DbAttributeComparer.md) | Class to define comparers for ordering lists of attributes. These allow lists of attributes to be sorted on the value of any field. At present, only an alphabetic sort on field values expressed as strings is implemented, although it would be possible to extend this to sort on numerical values. However, as most integers actually represent hash values or enumerations, this may be less useful than it at first sounds! |
| [DbAttributeFormat](Aveva.Pdms.Database.DbAttributeFormat.md) | Class to define an object for formatting an attribute definition for output ie what fields are to displayed, what intervening text etc Generally, a DbAttributeFormat will be used by a DbAttributeListFormat, which defines how a whole list of attributes is formatted |
| [DbAttributeInstance](Aveva.Pdms.Database.DbAttributeInstance.md) | List of definitions for predefined Attributes |
| [DbAttributeList](Aveva.Pdms.Database.DbAttributeList.md) | Class to define a list of attributes; usually for documentation purposes |
| [DbAttributeListEnum](Aveva.Pdms.Database.DbAttributeListEnum.md) | Enumerator for the DbAttributeList class |
| [DbAttributeListFormat](Aveva.Pdms.Database.DbAttributeListFormat.md) | Class to define an object to format a list of attributes. Each individual attribute is formatted by the DbAttributeFormat specified, and other aspects of the overall presentation (line breaks etc) are controlled by other properties of the DbAttributeListFormat |
| [DbChangesEventArgs](Aveva.Pdms.Database.DbChangesEventArgs.md) | Deprecated - do not use |
| [DbClaimEventArgs](Aveva.Pdms.Database.DbClaimEventArgs.md) | Deprecated - do not use |
| [DbElement](Aveva.Pdms.Database.DbElement.md) | Methods to read and write to the database. These cover element creation, deletion and copy; getting and querying attributes and rules; scanning the DB; evaluating database expressions. Instances of DbElement should be used to identify an element. i.e. methods that take an element should always pass a DbElement rather than a 2 long reference number or the name of the element. Some methods return a 'null' DbElement to denote failure. A 'null' DbElement can only be tested using the 'IsNull' method. |
| [DbElementType](Aveva.Pdms.Database.DbElementType.md) | The class has two purposes: i) Instances of the class are used to identify and pass around Element types ii) The class can be used to get meta data about an attribute. e.g. type, size, Name, pseudo or not, etc Return meta data about an element type, e,g. allowed members, name, Primary or not, etc. The class is valid for system types and UDETS. Object instances are created for all system element types. These instances are in DbElementTypeInstance class All methods that pass an Element Type should pass a DbElemenType object rather than a string that represents the attribute |
| [DbElementTypeComparer](Aveva.Pdms.Database.DbElementTypeComparer.md) | Class to define comparers for ordering lists of ElementTypes. These allow lists of element types to be sorted on the value of any field. At present, only an alphabetic sort on field values expressed as strings is implemented, although it would be possible to extend this to sort on numerical values. However, as most integers actually represent hash values or enumerations, this may be less useful than it at first sounds! |
| [DbElementTypeFormat](Aveva.Pdms.Database.DbElementTypeFormat.md) | Class to define an object for formatting a DbElementType definition for output ie what fields are to displayed, what intervening text etc Generally, a DbElementTypeFormat will be used by a DbElementTypeListFormat, which defines how a whole list of DbElementTypes is formatted |
| [DbElementTypeInstance](Aveva.Pdms.Database.DbElementTypeInstance.md) | List of definitions for predefined Element Types |
| [DbElementTypeList](Aveva.Pdms.Database.DbElementTypeList.md) | Class to define a list of DbElementTypes; usually for documentation purposes |
| [DbElementTypeListEnum](Aveva.Pdms.Database.DbElementTypeListEnum.md) | Enumerator for the DbElementTypeList class |
| [DbElementTypeListFormat](Aveva.Pdms.Database.DbElementTypeListFormat.md) | Class to define an object to format a list of DbElementTypes. Each individual DbElementType is formatted by the DbElementTypeFormat specified, and other aspects of the overall presentation (line breaks etc) are controlled by other properties of the DbElementTypeListFormat |
| [DbEvents](Aveva.Pdms.Database.DbEvents.md) | This class contains the mechanisms for subscribing to database events: It covers project open, mdb open, mdb close, savework, getwork, undo, redo, flush, refresh, drop plus capturing general database changes. It does not cover legality checkers for operations on elements. The delegates are organised by type of operation rather than specific ones for each operation e.g. there is a single callback to cover all opeartions(undo, redo, getwork, quit) that changes the user's current viewed data |
| [DbExpression](Aveva.Pdms.Database.DbExpression.md) | Representation of an Database (PML1) Expression. Methods to evaluate an expression are on DbElement |
| [DbFieldFormat](Aveva.Pdms.Database.DbFieldFormat.md) | Class to define objects to control the representation of field values |
| [DbGetWorkChangesEventArgs](Aveva.Pdms.Database.DbGetWorkChangesEventArgs.md) | Deprecated - do not use |
| [DbLegalityChecks](Aveva.Pdms.Database.DbLegalityChecks.md) | Class to registry legality checkers- For AVEVA use only |
| [DbNameSequence](Aveva.Pdms.Database.DbNameSequence.md) | Representation of a NameSequence |
| [DbPostElementChange](Aveva.Pdms.Database.DbPostElementChange.md) | Class to add delegates to do follow up data integrity actions. FOR USE BY AVEVA ONLY This class should only be used to ensure the data integrity of the database. To capture general database changes it is much more efficent to use the classes in DbEvents |
| [DbPseudoAttribute](Aveva.Pdms.Database.DbPseudoAttribute.md) | Class allows pseudo attribute code to be plugged in. This includes pseudo code for UDAs. There are different methods to plug in the pseudo attribute code depending on the attribute type. User's may only plug code for UADs. The plugging of pseudo attribute code for system attributes is FOR AVEVA USE ONLY |
| [DbQualifier](Aveva.Pdms.Database.DbQualifier.md) | Summary description for DbQualifier. |
| [DbRawChanges](Aveva.Pdms.Database.DbRawChanges.md) | Representation of Raw Dabacon Changes. An instance of this class is passed back for certain events such as savework. In general it is better to handle changes in the 'post action', other than deletions which are best handled in the 'pre action' |
| [DbRule](Aveva.Pdms.Database.DbRule.md) | Representation of a Rule. |
| [DbSession](Aveva.Pdms.Database.DbSession.md) | Class to return details about a particular Dabacon session. |
| [DbUndoChangesEventArgs](Aveva.Pdms.Database.DbUndoChangesEventArgs.md) | Deprecated - do not use |
| [DbUserChanges](Aveva.Pdms.Database.DbUserChanges.md) | Representation of User Changes list Instances will be passed |
| [IntTable](Aveva.Pdms.Database.IntTable.md) | Class for scanning an integer table for a particular DB. The actual scanning of the name table is performed by getting a IntTableEnumerator and iterating on that |
| [IntTableEnumerator](Aveva.Pdms.Database.IntTableEnumerator.md) | Int Table Enumerator. N.B. Enumerator MUST be explicitly disposed to clean up resources |
| [InvalidSession](Aveva.Pdms.Database.InvalidSession.md) |  |
| [MDB](Aveva.Pdms.Database.MDB.md) | Representation of an MDB The MDB is accessed via the currentMDB N.B. most methods do not return anything useful until the MDB is opened. (class needs to be remnmed Mdb rather than MDB, similarly MDBSetup should be MdbSetup ) |
| [MdbIntTable](Aveva.Pdms.Database.MdbIntTable.md) | Class for scanning an integer table representing all dbs of given type within the current MDB. The actual scanning of the name table is performed by getting a MdbIntTableEnumerator and iterating on that |
| [MdbIntTableEnumerator](Aveva.Pdms.Database.MdbIntTableEnumerator.md) | MDB Int Table Enumerator. N.B. Enumerator MUST be explicitly disposed to clean up resources |
| [MdbNameTable](Aveva.Pdms.Database.MdbNameTable.md) | Class for scanning a name table representing all dbs of given type within the current MDB. Names are ordered alphabetically. The actual scanning of the name table is performed by getting a MdbNameTableEnumerator and iterating on that. |
| [MdbNameTableEnumerator](Aveva.Pdms.Database.MdbNameTableEnumerator.md) | MDB name Table Enumerator. N.B. Enumerator MUST be explicitly disposed to clean up resources |
| [MDBSetup](Aveva.Pdms.Database.MDBSetup.md) | Class to store options when opening an MDB. |
| [NameTable](Aveva.Pdms.Database.NameTable.md) | Class for scanning a name table for a particular DB. Names are ordered alphabetically. The actual scanning of the name table is performed by getting a NameTableEnumerator and iterating on that. |
| [NameTableEnumerator](Aveva.Pdms.Database.NameTableEnumerator.md) | Name Table Enumerator. N.B. Enumerator MUST be explicitly disposed to clean up resources |
| [ParameterList](Aveva.Pdms.Database.ParameterList.md) | Representation of Parameter List. to be used for PARA and DESP attributes NOT YET IMPLEMENTED. |
| [Project](Aveva.Pdms.Database.Project.md) | Representation of a Project. |
| [ProjectError](Aveva.Pdms.Database.ProjectError.md) |  |
| [RefTable](Aveva.Pdms.Database.RefTable.md) | Class for scanning of a ref table for a particular DB. The actual scanning of the ref table is performed by getting a RefTableEnumerator and iterating on that |
| [RefTableEnumerator](Aveva.Pdms.Database.RefTableEnumerator.md) | Ref Table Enumerator. N.B. Enumerator MUST be explicitly disposed to clean up resources |
| [Spatial](Aveva.Pdms.Database.Spatial.md) | Class to do volumetic queries. For exact opertaions on catalogue items, all primities with TUFL set are tested. |

## Structures

| 类型 | 描述 |
|------|------|
| [DbCopyOption](Aveva.Pdms.Database.DbCopyOption.md) | Container for copy options. |

## Delegates

| 类型 | 描述 |
|------|------|
| [DbChangesEventHandler](Aveva.Pdms.Database.DbChangesEventHandler.md) | Deprecated- do not use |
| [DbClaimEventHandler](Aveva.Pdms.Database.DbClaimEventHandler.md) | Deprecated- do not use |
| [DbEventHandler](Aveva.Pdms.Database.DbEventHandler.md) | Deprecated- do not use |
| [DbEvents.BoolChangeEventHandler](Aveva.Pdms.Database.DbEvents.BoolChangeEventHandler.md) | Delegate taking a DbRawChanges object, operation type and returning true if allowed |
| [DbEvents.ChangeEventHandler](Aveva.Pdms.Database.DbEvents.ChangeEventHandler.md) | Delegate taking a DbRawChanges object plus operation type |
| [DbEvents.ClaimEventHandler](Aveva.Pdms.Database.DbEvents.ClaimEventHandler.md) | Delegate taking a list of elements |
| [DbEvents.CommitEventHandler](Aveva.Pdms.Database.DbEvents.CommitEventHandler.md) | Delegate taking operation only |
| [DbEvents.FailureEventHandler](Aveva.Pdms.Database.DbEvents.FailureEventHandler.md) | Delegate taking a DbRawChanges object, a list of errors plus operation attempted |
| [DbEvents.SimpleEventHandler](Aveva.Pdms.Database.DbEvents.SimpleEventHandler.md) | Delegate with no arguments |
| [DbEvents.UserChangesEventHandler](Aveva.Pdms.Database.DbEvents.UserChangesEventHandler.md) | Delegate taking a DbUserChanges object |
| [DbGetWorkEventHandler](Aveva.Pdms.Database.DbGetWorkEventHandler.md) | Deprecated- do not use |
| [DbLegalityChecks.BoolAttributeDelegate](Aveva.Pdms.Database.DbLegalityChecks.BoolAttributeDelegate.md) | Delegate to test if bool attribute may be set- For AVEVA use only |
| [DbLegalityChecks.CopyDelegate](Aveva.Pdms.Database.DbLegalityChecks.CopyDelegate.md) | Delegate to test if creation of element may be copied- For AVEVA use only |
| [DbLegalityChecks.CreateDelegate](Aveva.Pdms.Database.DbLegalityChecks.CreateDelegate.md) | Delegate to test if creation of element is allowed- For AVEVA use only |
| [DbLegalityChecks.DeleteDelegate](Aveva.Pdms.Database.DbLegalityChecks.DeleteDelegate.md) | Delegate to test if deletion of element is allowed- For AVEVA use only |
| [DbLegalityChecks.DoubleArrayAttributeDelegate](Aveva.Pdms.Database.DbLegalityChecks.DoubleArrayAttributeDelegate.md) | Delegate to test if real array attribute may be set- For AVEVA use only |
| [DbLegalityChecks.DoubleAttributeDelegate](Aveva.Pdms.Database.DbLegalityChecks.DoubleAttributeDelegate.md) | Delegate to test if real attribute may be set- For AVEVA use only |
| [DbLegalityChecks.IntArrayAttributeDelegate](Aveva.Pdms.Database.DbLegalityChecks.IntArrayAttributeDelegate.md) | Delegate to test if int array attribute may be set- For AVEVA use only |
| [DbLegalityChecks.IntAttributeDelegate](Aveva.Pdms.Database.DbLegalityChecks.IntAttributeDelegate.md) | Delegate to test if int attribute may be set- For AVEVA use only |
| [DbLegalityChecks.MoveDelegate](Aveva.Pdms.Database.DbLegalityChecks.MoveDelegate.md) | Delegate to test if element may be moved is allowed- For AVEVA use only |
| [DbLegalityChecks.RefArrayAttributeDelegate](Aveva.Pdms.Database.DbLegalityChecks.RefArrayAttributeDelegate.md) | Delegate to test if ref array attribute may be set- For AVEVA use only |
| [DbLegalityChecks.RefAttributeDelegate](Aveva.Pdms.Database.DbLegalityChecks.RefAttributeDelegate.md) | Delegate to test if ref attribute may be set- For AVEVA use only |
| [DbLegalityChecks.StringAttributeDelegate](Aveva.Pdms.Database.DbLegalityChecks.StringAttributeDelegate.md) | Delegate to test if string attribute may be set- For AVEVA use only |
| [DbPostElementChange.PostAttributeChangeDelegate](Aveva.Pdms.Database.DbPostElementChange.PostAttributeChangeDelegate.md) | Delegate to do follow up action on setting attribute - For AVEVA use only |
| [DbPostElementChange.PostCopyDelegate](Aveva.Pdms.Database.DbPostElementChange.PostCopyDelegate.md) | Delegate to do follow up action on element copy - For AVEVA use only |
| [DbPostElementChange.PostCreateDelegate](Aveva.Pdms.Database.DbPostElementChange.PostCreateDelegate.md) | Delegate to do follow up action on element creation - For AVEVA use only |
| [DbPostElementChange.PostMoveDelegate](Aveva.Pdms.Database.DbPostElementChange.PostMoveDelegate.md) | Delegate to do follow up action on element move (i.e. INCLUDE opeartion) - For AVEVA use only |
| [DbPostElementChange.PostRefAttributeChangeDelegate](Aveva.Pdms.Database.DbPostElementChange.PostRefAttributeChangeDelegate.md) | Delegate to do follow up action on setting ref attribute - For AVEVA use only |
| [DbPostElementChange.PostRefListAttributeChangeDelegate](Aveva.Pdms.Database.DbPostElementChange.PostRefListAttributeChangeDelegate.md) | Delegate to do follow up action on setting ref array attribute - For AVEVA use only |
| [DbPostElementChange.PreDeleteDelegate](Aveva.Pdms.Database.DbPostElementChange.PreDeleteDelegate.md) | Delegate to do pre action on element deletion - For AVEVA use only |
| [DbPseudoAttribute.GetBoolDelegate](Aveva.Pdms.Database.DbPseudoAttribute.GetBoolDelegate.md) | Delegate to use for writing boolean pseudo attribute 'get' method. THE QUALIFIER ARGUMENT WILL CHANGE |
| [DbPseudoAttribute.GetDoubleArrayDelegate](Aveva.Pdms.Database.DbPseudoAttribute.GetDoubleArrayDelegate.md) | Delegate to use for writing real array pseudo attribute 'get' method. THE QUALIFIER ARGUMENT WILL CHANGE |
| [DbPseudoAttribute.GetDoubleDelegate](Aveva.Pdms.Database.DbPseudoAttribute.GetDoubleDelegate.md) | Delegate to use for writing real pseudo attribute 'get' method. THE QUALIFIER ARGUMENT WILL CHANGE |
| [DbPseudoAttribute.GetIntArrayDelegate](Aveva.Pdms.Database.DbPseudoAttribute.GetIntArrayDelegate.md) | Delegate to use for writing integer array pseudo attribute 'get' method. THE QUALIFIER ARGUMENT WILL CHANGE |
| [DbPseudoAttribute.GetIntDelegate](Aveva.Pdms.Database.DbPseudoAttribute.GetIntDelegate.md) | Delegate to use for writing integer pseudo attribute 'get' method. THE QUALIFIER ARGUMENT WILL CHANGE |
| [DbPseudoAttribute.GetRefArrayDelegate](Aveva.Pdms.Database.DbPseudoAttribute.GetRefArrayDelegate.md) | Delegate to use for writing ref array pseudo attribute 'get' method. THE QUALIFIER ARGUMENT WILL CHANGE |
| [DbPseudoAttribute.GetRefDelegate](Aveva.Pdms.Database.DbPseudoAttribute.GetRefDelegate.md) | Delegate to use for writing ref pseudo attribute 'get' method. THE QUALIFIER ARGUMENT WILL CHANGE |
| [DbPseudoAttribute.GetStringDelegate](Aveva.Pdms.Database.DbPseudoAttribute.GetStringDelegate.md) | Delegate to use for writing string pseudo attribute 'get' method. THE QUALIFIER ARGUMENT WILL CHANGE |
| [DbPseudoAttribute.SetBoolDelegate](Aveva.Pdms.Database.DbPseudoAttribute.SetBoolDelegate.md) | Delegate to use for writing boolean pseudo attribute 'set' method. |
| [DbPseudoAttribute.SetDoubleArrayDelegate](Aveva.Pdms.Database.DbPseudoAttribute.SetDoubleArrayDelegate.md) | Delegate to use for writing real array pseudo attribute 'set' method. |
| [DbPseudoAttribute.SetDoubleDelegate](Aveva.Pdms.Database.DbPseudoAttribute.SetDoubleDelegate.md) | Delegate to use for writing real pseudo attribute 'set' method. |
| [DbPseudoAttribute.SetIntArrayDelegate](Aveva.Pdms.Database.DbPseudoAttribute.SetIntArrayDelegate.md) | Delegate to use for writing integer array pseudo attribute 'set' method. |
| [DbPseudoAttribute.SetIntDelegate](Aveva.Pdms.Database.DbPseudoAttribute.SetIntDelegate.md) | Delegate to use for writing integer pseudo attribute 'set' method. |
| [DbPseudoAttribute.SetRefArrayDelegate](Aveva.Pdms.Database.DbPseudoAttribute.SetRefArrayDelegate.md) | Delegate to use for writing ref array pseudo attribute 'set' method. |
| [DbPseudoAttribute.SetRefDelegate](Aveva.Pdms.Database.DbPseudoAttribute.SetRefDelegate.md) | Delegate to use for writing ref pseudo attribute 'set' method. |
| [DbPseudoAttribute.SetStringDelegate](Aveva.Pdms.Database.DbPseudoAttribute.SetStringDelegate.md) | Delegate to use for writing string pseudo attribute 'set' method. |
| [DbUndoEventHandler](Aveva.Pdms.Database.DbUndoEventHandler.md) | Deprecated- do not use |

## Enumerations

| 类型 | 描述 |
|------|------|
| [DbAttributeChangeCode](Aveva.Pdms.Database.DbAttributeChangeCode.md) | List of Design change codes * Mirrors the Fortran constants K:CHANGE.x * Enumarates possible values of the DCHC field of attributes |
| [DbAttributeCopyCode](Aveva.Pdms.Database.DbAttributeCopyCode.md) | List of copy codes * Mirrors the Fortran constants K:ATTR.COPY.x * Enumerates possible values of the COPY field of attributes |
| [DbAttributeDefinition](Aveva.Pdms.Database.DbAttributeDefinition.md) | Attribute definitions, DDL or Pseudo * Mirrors the Fortran constants K:ATTR.DEF.x * Enumerates possible values of the DEFI and WDEFI fields for attributes |
| [DbAttributeField](Aveva.Pdms.Database.DbAttributeField.md) | List of Attribute component field identifiers. |
| [DbAttributeIntrepidQueryType](Aveva.Pdms.Database.DbAttributeIntrepidQueryType.md) | List of Intrepid Query Types * Enumerates possible values of the ITYP field of attributes |
| [DbAttributeIntTableType](Aveva.Pdms.Database.DbAttributeIntTableType.md) | Integer Table Types * Enumerates possible values of the TBLTYP field of attributes |
| [DbAttributePrecisionCode](Aveva.Pdms.Database.DbAttributePrecisionCode.md) | List of default precision codes * Enumerates possible values of the DFDP field of attributes |
| [DbAttributePseudoCodeLocation](Aveva.Pdms.Database.DbAttributePseudoCodeLocation.md) | Code locations * Mirrors the Fortran constants K:ATTR.PSEUDO.x * Enumerates possible values of the PSCODE field of attributes |
| [DbAttributeQualifier](Aveva.Pdms.Database.DbAttributeQualifier.md) | List of qualifiers * Mirrors the Fortran constants K:ATTR.QUAL.x * Enumerates possible values of the QUAL field of attributes |
| [DbAttributeSpecialField](Aveva.Pdms.Database.DbAttributeSpecialField.md) | Other attribute information which may be included in tabular output. The values of special fields may be derived from fields or other information on the output. Special fields must be supported by the GetAsString method, and can thus be used in Attribute Formatters. However, they cannot be used in most other pleaces where a field may be. |
| [DbAttributeType](Aveva.Pdms.Database.DbAttributeType.md) | List of Attribute Type identifiers. |
| [DbAttributeUnit](Aveva.Pdms.Database.DbAttributeUnit.md) | List of Unit identifiers available for Attribute values. |
| [DbEvents.operation](Aveva.Pdms.Database.DbEvents.operation.md) | List of potential database operations. |
| [DbExpressionType](Aveva.Pdms.Database.DbExpressionType.md) | List of Expression Type identifiers. |
| [DbFieldFormatDefaultAction](Aveva.Pdms.Database.DbFieldFormatDefaultAction.md) | Actions a field formatter may take when no specific substitute string has been defined for the value found |
| [DbFieldType](Aveva.Pdms.Database.DbFieldType.md) | List of attribute and noun field types |
| [DbNounClaimSignificance](Aveva.Pdms.Database.DbNounClaimSignificance.md) | Claim Significance * Mirrors the Fortran constants K:CLAIM.x * Enumerates possible values of the CSIG field for nouns |
| [DbNounComponentFlag](Aveva.Pdms.Database.DbNounComponentFlag.md) | Component flag * Mirrors the Fortran constants K:NOUN.COMP.x * Enumerates possible values of component integer fields for nouns: HULC, PIPC, HOLC, CATC, DTXC, COMC, EQUC, FRMC, PFRC, FITC, GMTC, GMSC, DTSC, NGMC, HNGC, JOIC, PLNC, PRFC, PTSC, PSKC, BUIC |
| [DbNounDefinition](Aveva.Pdms.Database.DbNounDefinition.md) | Noun definitions, DDL or Pseudo * Mirrors the Fortran constants K:NOUN.DEF.x * Enumerates possible values of the DEFI field for nouns |
| [DbNounDraftGraphicalCode](Aveva.Pdms.Database.DbNounDraftGraphicalCode.md) | PSFrst * Mirrors the Fortran constants K:GCODE.x * Enumerates possible values of GCODE field for nouns: |
| [DbNounField](Aveva.Pdms.Database.DbNounField.md) | List of Element component field identifiers. |
| [DbNounGraphics](Aveva.Pdms.Database.DbNounGraphics.md) | Noun graphics * Mirrors the Fortran constants K:GRAPHICS.x * Enumerates possible values of the GRAPH field for nouns |
| [DbNounManual](Aveva.Pdms.Database.DbNounManual.md) | Noun Manual Categories NB: This must mirror the K:NOUN.MANUAL constants in noun_type.mcr Underscores in names will be replaced by space before presentation in the manual |
| [DbNounMap](Aveva.Pdms.Database.DbNounMap.md) | Significance with respect to spatial map * Mirrors the Fortran constants K:MAP.x * Enumerates possible values of the IMAP field for nouns |
| [DbNounPsFrst](Aveva.Pdms.Database.DbNounPsFrst.md) | PSFrst * Mirrors the Fortran constants K:PSFRST.x * Enumerates possible values of PSFRST field for nouns: |
| [DbNounPsNext](Aveva.Pdms.Database.DbNounPsNext.md) | PSNext * Mirrors the Fortran constants K:PSNEXT.x * Enumerates possible values of PSNEXT field for nouns: |
| [DbNounPsOwnr](Aveva.Pdms.Database.DbNounPsOwnr.md) | PSOwnr * Mirrors the Fortran constants K:PSOWNR.x * Enumerates possible values of PSOWNR field for nouns: |
| [DbNounSecondaryHier](Aveva.Pdms.Database.DbNounSecondaryHier.md) | Noun secondary hierarchy * Enumerates possible values of the SECOND field for nouns |
| [DbNounSpecialField](Aveva.Pdms.Database.DbNounSpecialField.md) | Other DbElementType information which may be included in tabular output. The values of special fields may be derived from fields or other information on the output. Special fields must be supported by the GetAsString method, and can thus be used in DbElementTypeFormats. However, they cannot be used in most other pleaces where a field may be. |
| [DbNounValidC](Aveva.Pdms.Database.DbNounValidC.md) | Validity of querying connections * Enumerates possible values of the VALIDC field for nouns |
| [DbParameterType](Aveva.Pdms.Database.DbParameterType.md) | List of Parameter Type identifiers. |
| [DbProjectType](Aveva.Pdms.Database.DbProjectType.md) | List of Project Type identifiers. |
| [DbRuleStatus](Aveva.Pdms.Database.DbRuleStatus.md) | List of Rule Status identifiers. |
| [DbType](Aveva.Pdms.Database.DbType.md) | List of Database Type identifiers. |
| [DbUnits](Aveva.Pdms.Database.DbUnits.md) | List of dimension Unit identifiers. |
| [DbWriteMode](Aveva.Pdms.Database.DbWriteMode.md) | List of Database write-mode identifiers. |
