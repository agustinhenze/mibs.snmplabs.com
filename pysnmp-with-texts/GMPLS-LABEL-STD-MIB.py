#
# PySNMP MIB module GMPLS-LABEL-STD-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/GMPLS-LABEL-STD-MIB
# Produced by pysmi-0.3.4 at Wed May  1 13:19:37 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
OctetString, ObjectIdentifier, Integer = mibBuilder.importSymbols("ASN1", "OctetString", "ObjectIdentifier", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsUnion, ValueRangeConstraint, ValueSizeConstraint, SingleValueConstraint, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "ValueRangeConstraint", "ValueSizeConstraint", "SingleValueConstraint", "ConstraintsIntersection")
IndexIntegerNextFree, = mibBuilder.importSymbols("DIFFSERV-MIB", "IndexIntegerNextFree")
GmplsLabelTypeTC, GmplsFreeformLabelTC = mibBuilder.importSymbols("GMPLS-TC-STD-MIB", "GmplsLabelTypeTC", "GmplsFreeformLabelTC")
InterfaceIndexOrZero, = mibBuilder.importSymbols("IF-MIB", "InterfaceIndexOrZero")
mplsStdMIB, MplsLabel = mibBuilder.importSymbols("MPLS-TC-STD-MIB", "mplsStdMIB", "MplsLabel")
ModuleCompliance, NotificationGroup, ObjectGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup", "ObjectGroup")
Unsigned32, TimeTicks, Counter32, Integer32, ModuleIdentity, MibIdentifier, Gauge32, ObjectIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, Bits, NotificationType, IpAddress, iso, Counter64 = mibBuilder.importSymbols("SNMPv2-SMI", "Unsigned32", "TimeTicks", "Counter32", "Integer32", "ModuleIdentity", "MibIdentifier", "Gauge32", "ObjectIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Bits", "NotificationType", "IpAddress", "iso", "Counter64")
StorageType, DisplayString, TextualConvention, RowStatus = mibBuilder.importSymbols("SNMPv2-TC", "StorageType", "DisplayString", "TextualConvention", "RowStatus")
gmplsLabelStdMIB = ModuleIdentity((1, 3, 6, 1, 2, 1, 10, 166, 16))
gmplsLabelStdMIB.setRevisions(('2007-02-27 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: gmplsLabelStdMIB.setRevisionsDescriptions(('Initial version issued as part of RFC 4803.',))
if mibBuilder.loadTexts: gmplsLabelStdMIB.setLastUpdated('200702270000Z')
if mibBuilder.loadTexts: gmplsLabelStdMIB.setOrganization('IETF Common Control and Measurement Plane (CCAMP) Working Group')
if mibBuilder.loadTexts: gmplsLabelStdMIB.setContactInfo(' Thomas D. Nadeau Cisco Systems, Inc. Email: tnadeau@cisco.com Adrian Farrel Old Dog Consulting Email: adrian@olddog.co.uk Comments about this document should be emailed directly to the CCAMP working group mailing list at ccamp@ops.ietf.org.')
if mibBuilder.loadTexts: gmplsLabelStdMIB.setDescription('Copyright (C) The IETF Trust (2007). This version of this MIB module is part of RFC 4803; see the RFC itself for full legal notices. This MIB module contains managed object definitions for labels within GMPLS systems as defined in Generalized Multi-Protocol Label Switching (GMPLS) Signaling Functional Description, Berger, L. (Editor), RFC 3471, January 2003.')
gmplsLabelObjects = MibIdentifier((1, 3, 6, 1, 2, 1, 10, 166, 16, 1))
gmplsLabelConformance = MibIdentifier((1, 3, 6, 1, 2, 1, 10, 166, 16, 2))
gmplsLabelIndexNext = MibScalar((1, 3, 6, 1, 2, 1, 10, 166, 16, 1, 1), IndexIntegerNextFree()).setMaxAccess("readonly")
if mibBuilder.loadTexts: gmplsLabelIndexNext.setStatus('current')
if mibBuilder.loadTexts: gmplsLabelIndexNext.setDescription('This object contains an unused value for gmplsLabelIndex, or a zero to indicate that no unused value exists or is available. A management application wishing to create a row in the gmplsLabelTable may read this object and then attempt to create a row in the table. If row creation fails (because another application has already created a row with the supplied index), the management application should read this object again to get a new index value. When a row is created in the gmplsLabelTable with the gmplsLabelIndex value held by this object, an implementation MUST change the value in this object.')
gmplsLabelTable = MibTable((1, 3, 6, 1, 2, 1, 10, 166, 16, 1, 2), )
if mibBuilder.loadTexts: gmplsLabelTable.setReference('1. Generalized Multiprotocol Label Switching (GMPLS) Architecture, RFC 3945, section 7.1.')
if mibBuilder.loadTexts: gmplsLabelTable.setStatus('current')
if mibBuilder.loadTexts: gmplsLabelTable.setDescription('Table of GMPLS Labels. This table allows the representation of the more complex label forms required for GMPLS that cannot be held within the TEXTUAL-CONVENTION MplsLabel; that is, labels that cannot be encoded within 32 bits. It is, nevertheless, also capable of holding 32-bit labels or regular MPLS Labels if desired. Each entry in this table represents an individual GMPLS Label value. The representation of Labels in tables in other MIB modules may be achieved by a referrence to an entry in this table by means of a row pointer into this table. The indexing of this table provides for arbitrary indexing and also for concatenation of labels. For an example of label concatenation, see RFC 3945, section 7.1. In essence, a GMPLS Label may be composite in order to identify a set of resources in the data plane. Practical examples are timeslots and wavelength sets (which are not contiguous like wavebands). The indexing mechanism allows multiple entries in this table to be seen as a sequence of labels that should be concatenated. Ordering is potentially very sensitive for concatenation.')
gmplsLabelEntry = MibTableRow((1, 3, 6, 1, 2, 1, 10, 166, 16, 1, 2, 1), ).setIndexNames((0, "GMPLS-LABEL-STD-MIB", "gmplsLabelInterface"), (0, "GMPLS-LABEL-STD-MIB", "gmplsLabelIndex"), (0, "GMPLS-LABEL-STD-MIB", "gmplsLabelSubindex"))
if mibBuilder.loadTexts: gmplsLabelEntry.setStatus('current')
if mibBuilder.loadTexts: gmplsLabelEntry.setDescription('An entry in this table represents a single label value. There are three indexes into the table. - The interface index may be helpful to distinguish which labels are in use on which interfaces or to handle cases where there are a very large number of labels in use in the system. When label representation is desired to apply to the whole system or when it is not important to distinguish labels by their interfaces, this index MAY be set to zero. - The label index provides a way of identifying the label. - The label sub-index is only used for concatenated labels. It identifies each component label. When non-concatenated labels are used, this index SHOULD be set to zero. A storage type object is supplied to control the storage type for each entry, but implementations should note that the storage type of conceptual rows in other tables that include row pointers to an entry in this table SHOULD dictate the storage type of the rows in this table where the row in the other table is more persistent.')
gmplsLabelInterface = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 166, 16, 1, 2, 1, 1), InterfaceIndexOrZero())
if mibBuilder.loadTexts: gmplsLabelInterface.setStatus('current')
if mibBuilder.loadTexts: gmplsLabelInterface.setDescription('The interface on which this label is used. If this object is set to zero, the label MUST have applicability across the whole system and not be limited to a single interface.')
gmplsLabelIndex = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 166, 16, 1, 2, 1, 2), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(0, 4294967295)))
if mibBuilder.loadTexts: gmplsLabelIndex.setStatus('current')
if mibBuilder.loadTexts: gmplsLabelIndex.setDescription('An arbitrary index into the table to identify a label. Note that implementations that are representing 32-bit labels within this table MAY choose to align this index with the value of the label, and this may result in the use of the value zero since it represents a valid label value. Such implementation should be aware of the implications of sparsely populated tables. A management application may read the gmplsLabelIndexNext object to find a suitable value for this object.')
gmplsLabelSubindex = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 166, 16, 1, 2, 1, 3), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(0, 4294967295)))
if mibBuilder.loadTexts: gmplsLabelSubindex.setStatus('current')
if mibBuilder.loadTexts: gmplsLabelSubindex.setDescription('In conjunction with gmplsLabelInterface and gmplsLabelIndex, this object uniquely identifies this row. This sub-index allows a single GMPLS Label to be defined as a concatenation of labels. This is particularly useful in TDM. The ordering of sub-labels is strict with the sub-label with the lowest gmplsLabelSubindex appearing first. Note that all sub-labels of a single GMPLS Label must share the same gmplsLabelInterface and gmplsLabelIndex values. For labels that are not composed of concatenated sub-labels, this value SHOULD be set to zero.')
gmplsLabelType = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 166, 16, 1, 2, 1, 4), GmplsLabelTypeTC()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: gmplsLabelType.setReference('1. Generalized Multi-Protocol Label Switching (GMPLS) Signaling Functional Description, RFC 3471, section 3.')
if mibBuilder.loadTexts: gmplsLabelType.setStatus('current')
if mibBuilder.loadTexts: gmplsLabelType.setDescription('Identifies the type of this label. Note that this object does not determine whether MPLS or GMPLS signaling is in use: a value of gmplsMplsLabel(1) denotes that an MPLS Packet Label is present in the gmplsLabelMplsLabel object and encoded using the MplsLabel TEXTUAL-CONVENTION (may be a 20-bit MPLS Label, a 10- or 23-bit Frame Relay Label, or an Asynchronous Transfer Mode (ATM) Label), but does not describe whether this is signaled using MPLS or GMPLS. The value of this object helps determine which of the following objects are valid. This object cannot be modified if gmplsLabelRowStatus is active(1).')
gmplsLabelMplsLabel = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 166, 16, 1, 2, 1, 5), MplsLabel()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: gmplsLabelMplsLabel.setReference('1. MPLS Label Stack Encoding, RFC 3032.')
if mibBuilder.loadTexts: gmplsLabelMplsLabel.setStatus('current')
if mibBuilder.loadTexts: gmplsLabelMplsLabel.setDescription('The value of an MPLS Label (that is a Packet Label) if this table is used to store it. This may be used in MPLS systems even though the label values can be adequately stored in the MPLS MIB modules (MPLS-LSR-STD-MIB and MPLS-TE-STD-MIB). Furthermore, in mixed MPLS and GMPLS systems, it may be advantageous to store all labels in a single label table. Lastly, in GMPLS systems where Packet Labels are used (that is in systems that use GMPLS signaling and GMPLS Labels for packet switching), it may be desirable to use this table. This object is only valid if gmplsLabelType is set to gmplsMplsLabel(1). This object cannot be modified if gmplsLabelRowStatus is active(1).')
gmplsLabelPortWavelength = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 166, 16, 1, 2, 1, 6), Unsigned32()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: gmplsLabelPortWavelength.setReference('1. Generalized Multi-Protocol Label Switching (GMPLS) Signaling Functional Description, RFC 3471, section 3.2.1.1.')
if mibBuilder.loadTexts: gmplsLabelPortWavelength.setStatus('current')
if mibBuilder.loadTexts: gmplsLabelPortWavelength.setDescription('The value of a Port or Wavelength Label when carried as a Generalized Label. Only valid if gmplsLabelType is set to gmplsPortWavelengthLabel(2). This object cannot be modified if gmplsLabelRowStatus is active(1).')
gmplsLabelFreeform = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 166, 16, 1, 2, 1, 7), GmplsFreeformLabelTC().clone(hexValue="00")).setMaxAccess("readcreate")
if mibBuilder.loadTexts: gmplsLabelFreeform.setReference('1. Generalized Multi-Protocol Label Switching (GMPLS) Signaling Functional Description, RFC 3471, section 3.2.')
if mibBuilder.loadTexts: gmplsLabelFreeform.setStatus('current')
if mibBuilder.loadTexts: gmplsLabelFreeform.setDescription('The value of a Freeform Generalized Label that does not conform to one of the standardized label encodings or that an implementation chooses to represent as an octet string without further decoding. Only valid if gmplsLabelType is set to gmplsFreeformLabel(3). This object cannot be modified if gmplsLabelRowStatus is active(1).')
gmplsLabelSonetSdhSignalIndex = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 166, 16, 1, 2, 1, 8), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 4095))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: gmplsLabelSonetSdhSignalIndex.setReference('1. Generalized Multi-Protocol Label Switching (GMPLS) Extensions for Synchronous Optical Network (SONET) and Synchronous Digital Hierarchy (SDH) Control, RFC 4606, section 3.')
if mibBuilder.loadTexts: gmplsLabelSonetSdhSignalIndex.setStatus('current')
if mibBuilder.loadTexts: gmplsLabelSonetSdhSignalIndex.setDescription('The Signal Index value (S) of a SONET or SDH Generalized Label. Zero indicates that this field is non-significant. Only valid if gmplsLabelType is set to gmplsSonetLabel(4) or gmplsSdhLabel(5). This object cannot be modified if gmplsLabelRowStatus is active(1).')
gmplsLabelSdhVc = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 166, 16, 1, 2, 1, 9), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 15))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: gmplsLabelSdhVc.setReference('1. Generalized Multi-Protocol Label Switching (GMPLS) Extensions for Synchronous Optical Network (SONET) and Synchronous Digital Hierarchy (SDH) Control, RFC 4606, section 3.')
if mibBuilder.loadTexts: gmplsLabelSdhVc.setStatus('current')
if mibBuilder.loadTexts: gmplsLabelSdhVc.setDescription('The VC Indicator (U) of an SDH Generalized Label. Zero indicates that this field is non-significant. Only valid if gmplsLabelType is set to gmplsSdhLabel(5). This object cannot be modified if gmplsLabelRowStatus is active(1).')
gmplsLabelSdhVcBranch = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 166, 16, 1, 2, 1, 10), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 15))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: gmplsLabelSdhVcBranch.setReference('1. Generalized Multi-Protocol Label Switching (GMPLS) Extensions for Synchronous Optical Network (SONET) and Synchronous Digital Hierarchy (SDH) Control, RFC 4606, section 3.')
if mibBuilder.loadTexts: gmplsLabelSdhVcBranch.setStatus('current')
if mibBuilder.loadTexts: gmplsLabelSdhVcBranch.setDescription('The VC Branch Indicator (K) of an SDH Generalized Label. Zero indicates that this field is non-significant. Only valid if gmplsLabelType is set to gmplsSdhLabel(5). This object cannot be modified if gmplsLabelRowStatus is active(1).')
gmplsLabelSonetSdhBranch = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 166, 16, 1, 2, 1, 11), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 15))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: gmplsLabelSonetSdhBranch.setReference('1. Generalized Multi-Protocol Label Switching (GMPLS) Extensions for Synchronous Optical Network (SONET) and Synchronous Digital Hierarchy (SDH) Control, RFC 4606, section 3.')
if mibBuilder.loadTexts: gmplsLabelSonetSdhBranch.setStatus('current')
if mibBuilder.loadTexts: gmplsLabelSonetSdhBranch.setDescription('The Branch Indicator (L) of a SONET or SDH Generalized Label. Zero indicates that this field is non-significant. Only valid gmplsLabelType is set to gmplsSonetLabel(4) or gmplsSdhLabel(5). This object cannot be modified if gmplsLabelRowStatus is active(1).')
gmplsLabelSonetSdhGroupBranch = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 166, 16, 1, 2, 1, 12), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 15))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: gmplsLabelSonetSdhGroupBranch.setReference('1. Generalized Multi-Protocol Label Switching (GMPLS) Extensions for Synchronous Optical Network (SONET) and Synchronous Digital Hierarchy (SDH) Control, RFC 4606, section 3.')
if mibBuilder.loadTexts: gmplsLabelSonetSdhGroupBranch.setStatus('current')
if mibBuilder.loadTexts: gmplsLabelSonetSdhGroupBranch.setDescription('The Group Branch Indicator (M) of a SONET or SDH Generalized Label. Zero indicates that this field is non-significant. Only valid if gmplsLabelType is set to gmplsSonetLabel(4) or gmplsSdhLabel(5). This object cannot be modified if gmplsLabelRowStatus is active(1).')
gmplsLabelWavebandId = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 166, 16, 1, 2, 1, 13), Unsigned32()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: gmplsLabelWavebandId.setReference('1. Generalized Multi-Protocol Label Switching (GMPLS) Signaling Functional Description, RFC 3471, section 3.3.')
if mibBuilder.loadTexts: gmplsLabelWavebandId.setStatus('current')
if mibBuilder.loadTexts: gmplsLabelWavebandId.setDescription('The waveband identifier component of a Waveband Label. Only valid if gmplsLabelType is set to gmplsWavebandLabel(6). This object cannot be modified if gmplsLabelRowStatus is active(1).')
gmplsLabelWavebandStart = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 166, 16, 1, 2, 1, 14), Unsigned32()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: gmplsLabelWavebandStart.setReference('1. Generalized Multi-Protocol Label Switching (GMPLS) Signaling Functional Description, RFC 3471, section 3.3.')
if mibBuilder.loadTexts: gmplsLabelWavebandStart.setStatus('current')
if mibBuilder.loadTexts: gmplsLabelWavebandStart.setDescription('The starting label component of a Waveband Label. Only valid if gmplsLabelType is set to gmplsWavebandLabel(6). This object cannot be modified if gmplsLabelRowStatus is active(1).')
gmplsLabelWavebandEnd = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 166, 16, 1, 2, 1, 15), Unsigned32()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: gmplsLabelWavebandEnd.setReference('1. Generalized Multi-Protocol Label Switching (GMPLS) Signaling Functional Description, RFC 3471, section 3.3.')
if mibBuilder.loadTexts: gmplsLabelWavebandEnd.setStatus('current')
if mibBuilder.loadTexts: gmplsLabelWavebandEnd.setDescription('The end label component of a Waveband Label. Only valid if gmplsLabelType is set to gmplsWavebandLabel(6). This object cannot be modified if gmplsLabelRowStatus is active(1).')
gmplsLabelStorageType = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 166, 16, 1, 2, 1, 16), StorageType().clone('volatile')).setMaxAccess("readcreate")
if mibBuilder.loadTexts: gmplsLabelStorageType.setReference('1. Textual Conventions for SMIv2, STD 58, RFC 2579, section 2.')
if mibBuilder.loadTexts: gmplsLabelStorageType.setStatus('current')
if mibBuilder.loadTexts: gmplsLabelStorageType.setDescription("This variable indicates the storage type for this row. The agent MUST ensure that this object's value remains consistent with the storage type of any rows in other tables that contain pointers to this row. In particular, the storage type of this row must be at least as permanent as that of any row that points to it. Conceptual rows having the value 'permanent' need not allow write-access to any columnar objects in the row.")
gmplsLabelRowStatus = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 166, 16, 1, 2, 1, 17), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: gmplsLabelRowStatus.setStatus('current')
if mibBuilder.loadTexts: gmplsLabelRowStatus.setDescription('This variable is used to create, modify, and/or delete a row in this table. When a row in this table has a row in the active(1) state, no objects in this row can be modified except the gmplsLabelRowStatus and gmplsLabelStorageType. The gmplsLabelType object does not have a default and must be set before a row can become active. The corresponding label objects (dependent on the value of gmplsLabelType) should also be set unless they happen to need to use the specified default values as follows: gmplsLabelType setting objects to be set -------------------------------------------------------------- gmplsMplsLabel(1) gmplsLabelMplsLabel gmplsPortWavelengthLabel(2) gmplsLabelPortWavelength gmplsFreeformLabel(3) gmplsLabelFreeform gmplsSonetLabel(4) gmplsLabelSonetSdhSignalIndex gmplsLabelSdhVc gmplsLabelSdhVcBranch gmplsLabelSonetSdhBranch gmplsLabelSonetSdhGroupBranch gmplsSdhLabel(5) gmplsLabelSonetSdhSignalIndex gmplsLabelSdhVc gmplsLabelSdhVcBranch gmplsLabelSonetSdhBranch gmplsLabelSonetSdhGroupBranch gmplsWavebandLabel(6) gmplsLabelWavebandId gmplsLabelWavebandStart gmplsLabelWavebandEnd')
gmplsLabelGroups = MibIdentifier((1, 3, 6, 1, 2, 1, 10, 166, 16, 2, 1))
gmplsLabelCompliances = MibIdentifier((1, 3, 6, 1, 2, 1, 10, 166, 16, 2, 2))
gmplsLabelModuleReadOnlyCompliance = ModuleCompliance((1, 3, 6, 1, 2, 1, 10, 166, 16, 2, 2, 1)).setObjects(("GMPLS-LABEL-STD-MIB", "gmplsLabelTableGroup"), ("GMPLS-LABEL-STD-MIB", "gmplsLabelPacketGroup"), ("GMPLS-LABEL-STD-MIB", "gmplsLabelPortWavelengthGroup"), ("GMPLS-LABEL-STD-MIB", "gmplsLabelFreeformGroup"), ("GMPLS-LABEL-STD-MIB", "gmplsLabelSonetSdhGroup"), ("GMPLS-LABEL-STD-MIB", "gmplsLabelWavebandGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    gmplsLabelModuleReadOnlyCompliance = gmplsLabelModuleReadOnlyCompliance.setStatus('current')
if mibBuilder.loadTexts: gmplsLabelModuleReadOnlyCompliance.setDescription('Compliance requirement for implementations that only provide read-only support for GMPLS-LABEL-STD-MIB. Such devices can then be monitored but cannot be configured using this MIB module.')
gmplsLabelModuleFullCompliance = ModuleCompliance((1, 3, 6, 1, 2, 1, 10, 166, 16, 2, 2, 2)).setObjects(("GMPLS-LABEL-STD-MIB", "gmplsLabelTableGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    gmplsLabelModuleFullCompliance = gmplsLabelModuleFullCompliance.setStatus('current')
if mibBuilder.loadTexts: gmplsLabelModuleFullCompliance.setDescription('Compliance statement for agents that support the complete GMPLS-LABEL-STD-MIB module. The mandatory groups have to be implemented by GMPLS LSRs claiming support for this MIB module. This MIB module is, however, not mandatory for a working implementation of a GMPLS LSR with full MIB support if the GMPLS Labels in use can be represented within a 32-bit quantity.')
gmplsLabelTableGroup = ObjectGroup((1, 3, 6, 1, 2, 1, 10, 166, 16, 2, 1, 1)).setObjects(("GMPLS-LABEL-STD-MIB", "gmplsLabelIndexNext"), ("GMPLS-LABEL-STD-MIB", "gmplsLabelType"), ("GMPLS-LABEL-STD-MIB", "gmplsLabelStorageType"), ("GMPLS-LABEL-STD-MIB", "gmplsLabelRowStatus"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    gmplsLabelTableGroup = gmplsLabelTableGroup.setStatus('current')
if mibBuilder.loadTexts: gmplsLabelTableGroup.setDescription('Necessary, but not sufficient, set of objects to implement label table support. In addition, depending on the type of labels supported, the following other groups defined below are mandatory: gmplsLabelWavebandGroup and/or gmplsLabelPacketGroup and/or gmplsLabelPortWavelengthGroup and/or gmplsLabelFreeformGroup and/or gmplsLabelSonetSdhGroup.')
gmplsLabelPacketGroup = ObjectGroup((1, 3, 6, 1, 2, 1, 10, 166, 16, 2, 1, 2)).setObjects(("GMPLS-LABEL-STD-MIB", "gmplsLabelMplsLabel"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    gmplsLabelPacketGroup = gmplsLabelPacketGroup.setStatus('current')
if mibBuilder.loadTexts: gmplsLabelPacketGroup.setDescription('Object needed to implement Packet (MPLS) Labels.')
gmplsLabelPortWavelengthGroup = ObjectGroup((1, 3, 6, 1, 2, 1, 10, 166, 16, 2, 1, 3)).setObjects(("GMPLS-LABEL-STD-MIB", "gmplsLabelPortWavelength"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    gmplsLabelPortWavelengthGroup = gmplsLabelPortWavelengthGroup.setStatus('current')
if mibBuilder.loadTexts: gmplsLabelPortWavelengthGroup.setDescription('Object needed to implement Port and Wavelength Labels.')
gmplsLabelFreeformGroup = ObjectGroup((1, 3, 6, 1, 2, 1, 10, 166, 16, 2, 1, 4)).setObjects(("GMPLS-LABEL-STD-MIB", "gmplsLabelFreeform"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    gmplsLabelFreeformGroup = gmplsLabelFreeformGroup.setStatus('current')
if mibBuilder.loadTexts: gmplsLabelFreeformGroup.setDescription('Object needed to implement Freeform Labels.')
gmplsLabelSonetSdhGroup = ObjectGroup((1, 3, 6, 1, 2, 1, 10, 166, 16, 2, 1, 5)).setObjects(("GMPLS-LABEL-STD-MIB", "gmplsLabelSonetSdhSignalIndex"), ("GMPLS-LABEL-STD-MIB", "gmplsLabelSdhVc"), ("GMPLS-LABEL-STD-MIB", "gmplsLabelSdhVcBranch"), ("GMPLS-LABEL-STD-MIB", "gmplsLabelSonetSdhBranch"), ("GMPLS-LABEL-STD-MIB", "gmplsLabelSonetSdhGroupBranch"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    gmplsLabelSonetSdhGroup = gmplsLabelSonetSdhGroup.setStatus('current')
if mibBuilder.loadTexts: gmplsLabelSonetSdhGroup.setDescription('Objects needed to implement SONET and SDH Labels.')
gmplsLabelWavebandGroup = ObjectGroup((1, 3, 6, 1, 2, 1, 10, 166, 16, 2, 1, 6)).setObjects(("GMPLS-LABEL-STD-MIB", "gmplsLabelWavebandId"), ("GMPLS-LABEL-STD-MIB", "gmplsLabelWavebandStart"), ("GMPLS-LABEL-STD-MIB", "gmplsLabelWavebandEnd"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    gmplsLabelWavebandGroup = gmplsLabelWavebandGroup.setStatus('current')
if mibBuilder.loadTexts: gmplsLabelWavebandGroup.setDescription('Objects needed to implement Waveband Labels.')
mibBuilder.exportSymbols("GMPLS-LABEL-STD-MIB", gmplsLabelEntry=gmplsLabelEntry, gmplsLabelSonetSdhGroup=gmplsLabelSonetSdhGroup, gmplsLabelTable=gmplsLabelTable, gmplsLabelIndexNext=gmplsLabelIndexNext, gmplsLabelSonetSdhSignalIndex=gmplsLabelSonetSdhSignalIndex, gmplsLabelCompliances=gmplsLabelCompliances, gmplsLabelFreeformGroup=gmplsLabelFreeformGroup, gmplsLabelSdhVc=gmplsLabelSdhVc, gmplsLabelSonetSdhBranch=gmplsLabelSonetSdhBranch, gmplsLabelWavebandGroup=gmplsLabelWavebandGroup, gmplsLabelType=gmplsLabelType, gmplsLabelSdhVcBranch=gmplsLabelSdhVcBranch, gmplsLabelSonetSdhGroupBranch=gmplsLabelSonetSdhGroupBranch, gmplsLabelFreeform=gmplsLabelFreeform, gmplsLabelRowStatus=gmplsLabelRowStatus, gmplsLabelWavebandId=gmplsLabelWavebandId, gmplsLabelWavebandEnd=gmplsLabelWavebandEnd, gmplsLabelPortWavelength=gmplsLabelPortWavelength, gmplsLabelSubindex=gmplsLabelSubindex, gmplsLabelMplsLabel=gmplsLabelMplsLabel, gmplsLabelStorageType=gmplsLabelStorageType, gmplsLabelStdMIB=gmplsLabelStdMIB, gmplsLabelIndex=gmplsLabelIndex, gmplsLabelTableGroup=gmplsLabelTableGroup, gmplsLabelPortWavelengthGroup=gmplsLabelPortWavelengthGroup, gmplsLabelWavebandStart=gmplsLabelWavebandStart, gmplsLabelPacketGroup=gmplsLabelPacketGroup, PYSNMP_MODULE_ID=gmplsLabelStdMIB, gmplsLabelObjects=gmplsLabelObjects, gmplsLabelModuleFullCompliance=gmplsLabelModuleFullCompliance, gmplsLabelModuleReadOnlyCompliance=gmplsLabelModuleReadOnlyCompliance, gmplsLabelInterface=gmplsLabelInterface, gmplsLabelConformance=gmplsLabelConformance, gmplsLabelGroups=gmplsLabelGroups)