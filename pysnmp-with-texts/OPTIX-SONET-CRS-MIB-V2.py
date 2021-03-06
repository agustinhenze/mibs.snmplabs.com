#
# PySNMP MIB module OPTIX-SONET-CRS-MIB-V2 (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/OPTIX-SONET-CRS-MIB-V2
# Produced by pysmi-0.3.4 at Wed May  1 14:35:16 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
Integer, OctetString, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "Integer", "OctetString", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsUnion, SingleValueConstraint, ValueRangeConstraint, ValueSizeConstraint, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "SingleValueConstraint", "ValueRangeConstraint", "ValueSizeConstraint", "ConstraintsIntersection")
optixProvisionSonet, = mibBuilder.importSymbols("OPTIX-OID-MIB", "optixProvisionSonet")
NotificationGroup, ModuleCompliance, ObjectGroup = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance", "ObjectGroup")
MibScalar, MibTable, MibTableRow, MibTableColumn, IpAddress, ModuleIdentity, TimeTicks, Counter64, Unsigned32, MibIdentifier, ObjectIdentity, Counter32, Bits, iso, NotificationType, Integer32, Gauge32 = mibBuilder.importSymbols("SNMPv2-SMI", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "IpAddress", "ModuleIdentity", "TimeTicks", "Counter64", "Unsigned32", "MibIdentifier", "ObjectIdentity", "Counter32", "Bits", "iso", "NotificationType", "Integer32", "Gauge32")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
optixsonetCRS = ModuleIdentity((1, 3, 6, 1, 4, 1, 2011, 2, 25, 4, 20, 1))
if mibBuilder.loadTexts: optixsonetCRS.setLastUpdated('200605232001Z')
if mibBuilder.loadTexts: optixsonetCRS.setOrganization('Your organization')
if mibBuilder.loadTexts: optixsonetCRS.setContactInfo('Your contact info')
if mibBuilder.loadTexts: optixsonetCRS.setDescription('Enter the description for this MIB module.')
class RowStatus(TextualConvention, Integer32):
    description = 'Enter the description for the RowStatus TEXTUAL-CONVENTION converted from type assignment.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6))
    namedValues = NamedValues(("active", 1), ("notInService", 2), ("notReady", 3), ("createAndGo", 4), ("createAndWait", 5), ("destroy", 6))

optixsonetCrsTable = MibTable((1, 3, 6, 1, 4, 1, 2011, 2, 25, 4, 20, 1, 3), )
if mibBuilder.loadTexts: optixsonetCrsTable.setStatus('current')
if mibBuilder.loadTexts: optixsonetCrsTable.setDescription('Description.')
optixsonetCrsEntry = MibTableRow((1, 3, 6, 1, 4, 1, 2011, 2, 25, 4, 20, 1, 3, 1), ).setIndexNames((0, "OPTIX-SONET-CRS-MIB-V2", "optixsonetCrsMod2"), (0, "OPTIX-SONET-CRS-MIB-V2", "optixsonetCrsFrom"), (0, "OPTIX-SONET-CRS-MIB-V2", "optixsonetCrsTo"), (0, "OPTIX-SONET-CRS-MIB-V2", "optixsonetCrsCct"))
if mibBuilder.loadTexts: optixsonetCrsEntry.setStatus('current')
if mibBuilder.loadTexts: optixsonetCrsEntry.setDescription('Description.')
optixsonetCrsMod2 = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 2, 25, 4, 20, 1, 3, 1, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(9, 10, 11, 12, 13, 15, 16, 17, 21, 22))).clone(namedValues=NamedValues(("crsSTS1", 9), ("crsSTS3C", 10), ("crsSTS6C", 11), ("crsSTS9C", 12), ("crsSTS12C", 13), ("crsSTS24C", 15), ("crsSTS48C", 16), ("crsSTS192C", 17), ("crsVT1", 21), ("crsVT2", 22)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: optixsonetCrsMod2.setStatus('current')
if mibBuilder.loadTexts: optixsonetCrsMod2.setDescription('The modifier that identifies the type of STS and VT path')
optixsonetCrsFrom = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 2, 25, 4, 20, 1, 3, 1, 2), OctetString().subtype(subtypeSpec=ValueSizeConstraint(0, 32))).setMaxAccess("readonly")
if mibBuilder.loadTexts: optixsonetCrsFrom.setStatus('current')
if mibBuilder.loadTexts: optixsonetCrsFrom.setDescription("Access identifier. It can be source or destination of cross connection, or any one path of source or destination. It can be null, that means retrieve all cross connection with entered rate level. '&' is allowed. ")
optixsonetCrsTo = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 2, 25, 4, 20, 1, 3, 1, 3), OctetString().subtype(subtypeSpec=ValueSizeConstraint(0, 32))).setMaxAccess("readonly")
if mibBuilder.loadTexts: optixsonetCrsTo.setStatus('current')
if mibBuilder.loadTexts: optixsonetCrsTo.setDescription("Access identifier identifies the other end of the cross connection. If creating 1-to-N one-way cross-connection, multiple '&' and '&&'are allowed. Else only one '&' is allowed. <TO> cannot be null.")
optixsonetCrsCct = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 2, 25, 4, 20, 1, 3, 1, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("twoWay", 1), ("oneWay", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: optixsonetCrsCct.setStatus('current')
if mibBuilder.loadTexts: optixsonetCrsCct.setDescription('Cross connect type.')
optixsonetCrsCktId = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 2, 25, 4, 20, 1, 3, 1, 5), OctetString().subtype(subtypeSpec=ValueSizeConstraint(0, 32))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: optixsonetCrsCktId.setStatus('current')
if mibBuilder.loadTexts: optixsonetCrsCktId.setDescription('The circuit identification. It is a string of max length 32 ASCII characters. The circuit identification parameter contains the common language circuit ID or other alias of the circuit being provisioned.')
optixsonetCrsPreferredPath = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 2, 25, 4, 20, 1, 3, 1, 6), OctetString().subtype(subtypeSpec=ValueSizeConstraint(0, 32))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: optixsonetCrsPreferredPath.setStatus('current')
if mibBuilder.loadTexts: optixsonetCrsPreferredPath.setDescription("Preferred path. It is only supplied for UPSR. Two values separated by '&' are applicable to only UPSR with 2 sources and 2 destinations.")
optixsonetCrsRDLD = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 2, 25, 4, 20, 1, 3, 1, 7), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("rdld", 1), ("rdldDEA", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: optixsonetCrsRDLD.setStatus('current')
if mibBuilder.loadTexts: optixsonetCrsRDLD.setDescription('Redline state.Vaild values are RDLD and RDLDDEA. RDLD This value indicates that the entity is a special (red-lined) circuit. RDLDDEA Deactive RDLD state.')
optixsonetCrsActivePath = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 2, 25, 4, 20, 1, 3, 1, 8), OctetString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: optixsonetCrsActivePath.setStatus('current')
if mibBuilder.loadTexts: optixsonetCrsActivePath.setDescription("Active path. It is only supplied for UPSR. Two values separated by '&' are applicable to only UPSR with 2 sources and 2 destinations. ")
optixsonetCrsRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 2, 25, 4, 20, 1, 3, 1, 10), RowStatus()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: optixsonetCrsRowStatus.setStatus('current')
if mibBuilder.loadTexts: optixsonetCrsRowStatus.setDescription("The RowStatus textual convention is used to manage the creation and deletion of conceptual rows, and is used as the value of the SYNTAX clause for the status column of a conceptual row. The status column has six defined values: - `active', which indicates that the conceptual row is available for use by the managed device; - `notInService', which indicates that the conceptual row exists in the agent, but is unavailable for use by the managed device (see NOTE below); - `notReady', which indicates that the conceptual row exists in the agent, but is missing information necessary in order to be available for use by the managed device; - `createAndGo', which is supplied by a management station wishing to create a new instance of a conceptual row and to have its status automatically set to active, making it available for use by the managed device; - `createAndWait', which is supplied by a management station wishing to create a new instance of a conceptual row (but not make it available for use by the managed device); and, - `destroy', which is supplied by a management station wishing to delete all of the instances associated with an existing conceptual row. Whereas five of the six values (all except `notReady') may be specified in a management protocol set operation, only three values will be returned in response to a management protocol retrieval operation: `notReady', `notInService' or `active'. That is, when queried, an existing conceptual row has only three states: it is either available for use by the managed device (the status column has value `active'); it is not available for use by the managed device, though the agent has sufficient information to make it so (the status column has value `notInService'); or, it is not available for use by the managed device, and an attempt to make it so would fail because the agent has insufficient information (the state column has value `notReady').")
optixsonetCRSConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 2, 25, 4, 20, 1, 4))
optixsonetCRSGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 2, 25, 4, 20, 1, 4, 1))
currentObjectGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 2011, 2, 25, 4, 20, 1, 4, 1, 1)).setObjects(("OPTIX-SONET-CRS-MIB-V2", "optixsonetCrsMod2"), ("OPTIX-SONET-CRS-MIB-V2", "optixsonetCrsFrom"), ("OPTIX-SONET-CRS-MIB-V2", "optixsonetCrsTo"), ("OPTIX-SONET-CRS-MIB-V2", "optixsonetCrsCct"), ("OPTIX-SONET-CRS-MIB-V2", "optixsonetCrsCktId"), ("OPTIX-SONET-CRS-MIB-V2", "optixsonetCrsPreferredPath"), ("OPTIX-SONET-CRS-MIB-V2", "optixsonetCrsRDLD"), ("OPTIX-SONET-CRS-MIB-V2", "optixsonetCrsActivePath"), ("OPTIX-SONET-CRS-MIB-V2", "optixsonetCrsRowStatus"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    currentObjectGroup = currentObjectGroup.setStatus('current')
if mibBuilder.loadTexts: currentObjectGroup.setDescription('Enter the description of the created OBJECT-GROUP.')
optixsonetCRSCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 2, 25, 4, 20, 1, 4, 2))
basicCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 2011, 2, 25, 4, 20, 1, 4, 2, 1)).setObjects(("OPTIX-SONET-CRS-MIB-V2", "currentObjectGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    basicCompliance = basicCompliance.setStatus('current')
if mibBuilder.loadTexts: basicCompliance.setDescription('Enter the description of the created MODULE-COMPLIANCE.')
mibBuilder.exportSymbols("OPTIX-SONET-CRS-MIB-V2", currentObjectGroup=currentObjectGroup, optixsonetCrsTo=optixsonetCrsTo, optixsonetCrsActivePath=optixsonetCrsActivePath, optixsonetCrsEntry=optixsonetCrsEntry, basicCompliance=basicCompliance, optixsonetCrsPreferredPath=optixsonetCrsPreferredPath, optixsonetCrsFrom=optixsonetCrsFrom, RowStatus=RowStatus, optixsonetCRSConformance=optixsonetCRSConformance, optixsonetCrsRDLD=optixsonetCrsRDLD, PYSNMP_MODULE_ID=optixsonetCRS, optixsonetCrsCct=optixsonetCrsCct, optixsonetCRSCompliances=optixsonetCRSCompliances, optixsonetCrsRowStatus=optixsonetCrsRowStatus, optixsonetCRS=optixsonetCRS, optixsonetCrsTable=optixsonetCrsTable, optixsonetCrsMod2=optixsonetCrsMod2, optixsonetCRSGroups=optixsonetCRSGroups, optixsonetCrsCktId=optixsonetCrsCktId)
