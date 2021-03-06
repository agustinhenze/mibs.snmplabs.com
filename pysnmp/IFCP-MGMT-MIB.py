#
# PySNMP MIB module IFCP-MGMT-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/IFCP-MGMT-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 19:41:46 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
Integer, OctetString, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "Integer", "OctetString", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, ValueSizeConstraint, ConstraintsIntersection, SingleValueConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "ValueSizeConstraint", "ConstraintsIntersection", "SingleValueConstraint", "ConstraintsUnion")
PhysicalIndexOrZero, = mibBuilder.importSymbols("ENTITY-MIB", "PhysicalIndexOrZero")
FcNameIdOrZero, FcAddressIdOrZero = mibBuilder.importSymbols("FC-MGMT-MIB", "FcNameIdOrZero", "FcAddressIdOrZero")
ZeroBasedCounter64, = mibBuilder.importSymbols("HCNUM-TC", "ZeroBasedCounter64")
InterfaceIndexOrZero, = mibBuilder.importSymbols("IF-MIB", "InterfaceIndexOrZero")
InetAddressType, InetAddress, InetPortNumber = mibBuilder.importSymbols("INET-ADDRESS-MIB", "InetAddressType", "InetAddress", "InetPortNumber")
ZeroBasedCounter32, = mibBuilder.importSymbols("RMON2-MIB", "ZeroBasedCounter32")
SnmpAdminString, = mibBuilder.importSymbols("SNMP-FRAMEWORK-MIB", "SnmpAdminString")
ObjectGroup, ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ObjectGroup", "ModuleCompliance", "NotificationGroup")
iso, MibIdentifier, Gauge32, MibScalar, MibTable, MibTableRow, MibTableColumn, TimeTicks, NotificationType, IpAddress, ModuleIdentity, Counter64, ObjectIdentity, Integer32, Bits, transmission, Counter32, Unsigned32 = mibBuilder.importSymbols("SNMPv2-SMI", "iso", "MibIdentifier", "Gauge32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "TimeTicks", "NotificationType", "IpAddress", "ModuleIdentity", "Counter64", "ObjectIdentity", "Integer32", "Bits", "transmission", "Counter32", "Unsigned32")
TextualConvention, StorageType, DisplayString, TimeStamp, TruthValue = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "StorageType", "DisplayString", "TimeStamp", "TruthValue")
ifcpMgmtMIB = ModuleIdentity((1, 3, 6, 1, 2, 1, 10, 230))
ifcpMgmtMIB.setRevisions(('2011-03-09 00:00', '2006-01-17 00:00',))
if mibBuilder.loadTexts: ifcpMgmtMIB.setLastUpdated('201103090000Z')
if mibBuilder.loadTexts: ifcpMgmtMIB.setOrganization('IETF STORage Maintenance (STORM) Working Group')
class IfcpIpTOVorZero(TextualConvention, Unsigned32):
    reference = 'RFC 4172, iFCP Protocol Specification'
    status = 'current'
    displayHint = 'd'
    subtypeSpec = Unsigned32.subtypeSpec + ValueRangeConstraint(0, 3600)

class IfcpLTIorZero(TextualConvention, Unsigned32):
    reference = 'RFC 4172, iFCP Protocol Specification'
    status = 'current'
    displayHint = 'd'
    subtypeSpec = Unsigned32.subtypeSpec + ValueRangeConstraint(0, 65535)

class IfcpSessionStates(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3))
    namedValues = NamedValues(("down", 1), ("openPending", 2), ("open", 3))

class IfcpAddressMode(TextualConvention, Integer32):
    reference = 'RFC 6172, Deprecation of iFCP Address Translation Mode'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2))
    namedValues = NamedValues(("addressTransparent", 1), ("addressTranslation", 2))

ifcpGatewayObjects = MibIdentifier((1, 3, 6, 1, 2, 1, 10, 230, 1))
ifcpGatewayConformance = MibIdentifier((1, 3, 6, 1, 2, 1, 10, 230, 2))
ifcpLclGatewayInfo = MibIdentifier((1, 3, 6, 1, 2, 1, 10, 230, 1, 1))
ifcpLclGtwyInstTable = MibTable((1, 3, 6, 1, 2, 1, 10, 230, 1, 1, 1), )
if mibBuilder.loadTexts: ifcpLclGtwyInstTable.setStatus('current')
ifcpLclGtwyInstEntry = MibTableRow((1, 3, 6, 1, 2, 1, 10, 230, 1, 1, 1, 1), ).setIndexNames((0, "IFCP-MGMT-MIB", "ifcpLclGtwyInstIndex"))
if mibBuilder.loadTexts: ifcpLclGtwyInstEntry.setStatus('current')
ifcpLclGtwyInstIndex = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 230, 1, 1, 1, 1, 1), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(1, 2147483647)))
if mibBuilder.loadTexts: ifcpLclGtwyInstIndex.setStatus('current')
ifcpLclGtwyInstPhyIndex = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 230, 1, 1, 1, 1, 2), PhysicalIndexOrZero()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ifcpLclGtwyInstPhyIndex.setStatus('current')
ifcpLclGtwyInstVersionMin = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 230, 1, 1, 1, 1, 3), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(0, 255))).setMaxAccess("readonly")
if mibBuilder.loadTexts: ifcpLclGtwyInstVersionMin.setStatus('current')
ifcpLclGtwyInstVersionMax = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 230, 1, 1, 1, 1, 4), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(0, 255))).setMaxAccess("readonly")
if mibBuilder.loadTexts: ifcpLclGtwyInstVersionMax.setStatus('current')
ifcpLclGtwyInstAddrTransMode = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 230, 1, 1, 1, 1, 5), IfcpAddressMode().clone('addressTransparent')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ifcpLclGtwyInstAddrTransMode.setStatus('current')
ifcpLclGtwyInstFcBrdcstSupport = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 230, 1, 1, 1, 1, 6), TruthValue().clone('false')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ifcpLclGtwyInstFcBrdcstSupport.setStatus('current')
ifcpLclGtwyInstDefaultIpTOV = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 230, 1, 1, 1, 1, 7), IfcpIpTOVorZero().clone(6)).setUnits('seconds').setMaxAccess("readwrite")
if mibBuilder.loadTexts: ifcpLclGtwyInstDefaultIpTOV.setStatus('current')
ifcpLclGtwyInstDefaultLTInterval = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 230, 1, 1, 1, 1, 8), IfcpLTIorZero().clone(10)).setUnits('seconds').setMaxAccess("readwrite")
if mibBuilder.loadTexts: ifcpLclGtwyInstDefaultLTInterval.setStatus('current')
ifcpLclGtwyInstDescr = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 230, 1, 1, 1, 1, 9), SnmpAdminString().subtype(subtypeSpec=ValueSizeConstraint(0, 64))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ifcpLclGtwyInstDescr.setStatus('current')
ifcpLclGtwyInstNumActiveSessions = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 230, 1, 1, 1, 1, 10), Gauge32().subtype(subtypeSpec=ValueRangeConstraint(0, 4294967295))).setMaxAccess("readonly")
if mibBuilder.loadTexts: ifcpLclGtwyInstNumActiveSessions.setStatus('current')
ifcpLclGtwyInstStorageType = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 230, 1, 1, 1, 1, 11), StorageType().clone('nonVolatile')).setMaxAccess("readonly")
if mibBuilder.loadTexts: ifcpLclGtwyInstStorageType.setStatus('current')
ifcpNportSessionInfo = MibIdentifier((1, 3, 6, 1, 2, 1, 10, 230, 1, 2))
ifcpSessionAttributesTable = MibTable((1, 3, 6, 1, 2, 1, 10, 230, 1, 2, 1), )
if mibBuilder.loadTexts: ifcpSessionAttributesTable.setStatus('current')
ifcpSessionAttributesEntry = MibTableRow((1, 3, 6, 1, 2, 1, 10, 230, 1, 2, 1, 1), ).setIndexNames((0, "IFCP-MGMT-MIB", "ifcpLclGtwyInstIndex"), (0, "IFCP-MGMT-MIB", "ifcpSessionIndex"))
if mibBuilder.loadTexts: ifcpSessionAttributesEntry.setStatus('current')
ifcpSessionIndex = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 230, 1, 2, 1, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 2147483647)))
if mibBuilder.loadTexts: ifcpSessionIndex.setStatus('current')
ifcpSessionLclPrtlIfIndex = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 230, 1, 2, 1, 1, 2), InterfaceIndexOrZero()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ifcpSessionLclPrtlIfIndex.setStatus('current')
ifcpSessionLclPrtlAddrType = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 230, 1, 2, 1, 1, 3), InetAddressType()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ifcpSessionLclPrtlAddrType.setStatus('current')
ifcpSessionLclPrtlAddr = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 230, 1, 2, 1, 1, 4), InetAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ifcpSessionLclPrtlAddr.setStatus('current')
ifcpSessionLclPrtlTcpPort = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 230, 1, 2, 1, 1, 5), InetPortNumber()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ifcpSessionLclPrtlTcpPort.setStatus('current')
ifcpSessionLclNpWwun = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 230, 1, 2, 1, 1, 6), FcNameIdOrZero()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ifcpSessionLclNpWwun.setStatus('current')
ifcpSessionLclNpFcid = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 230, 1, 2, 1, 1, 7), FcAddressIdOrZero()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ifcpSessionLclNpFcid.setStatus('current')
ifcpSessionRmtNpWwun = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 230, 1, 2, 1, 1, 8), FcNameIdOrZero()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ifcpSessionRmtNpWwun.setStatus('current')
ifcpSessionRmtPrtlIfAddrType = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 230, 1, 2, 1, 1, 9), InetAddressType()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ifcpSessionRmtPrtlIfAddrType.setStatus('current')
ifcpSessionRmtPrtlIfAddr = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 230, 1, 2, 1, 1, 10), InetAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ifcpSessionRmtPrtlIfAddr.setStatus('current')
ifcpSessionRmtPrtlTcpPort = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 230, 1, 2, 1, 1, 11), InetPortNumber().clone(3420)).setMaxAccess("readonly")
if mibBuilder.loadTexts: ifcpSessionRmtPrtlTcpPort.setStatus('current')
ifcpSessionRmtNpFcid = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 230, 1, 2, 1, 1, 12), FcAddressIdOrZero()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ifcpSessionRmtNpFcid.setStatus('current')
ifcpSessionRmtNpFcidAlias = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 230, 1, 2, 1, 1, 13), FcAddressIdOrZero()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ifcpSessionRmtNpFcidAlias.setStatus('current')
ifcpSessionIpTOV = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 230, 1, 2, 1, 1, 14), IfcpIpTOVorZero()).setUnits('seconds').setMaxAccess("readwrite")
if mibBuilder.loadTexts: ifcpSessionIpTOV.setStatus('current')
ifcpSessionLclLTIntvl = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 230, 1, 2, 1, 1, 15), IfcpLTIorZero()).setUnits('seconds').setMaxAccess("readonly")
if mibBuilder.loadTexts: ifcpSessionLclLTIntvl.setStatus('current')
ifcpSessionRmtLTIntvl = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 230, 1, 2, 1, 1, 16), IfcpLTIorZero()).setUnits('seconds').setMaxAccess("readonly")
if mibBuilder.loadTexts: ifcpSessionRmtLTIntvl.setStatus('current')
ifcpSessionBound = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 230, 1, 2, 1, 1, 17), TruthValue()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ifcpSessionBound.setStatus('current')
ifcpSessionStorageType = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 230, 1, 2, 1, 1, 18), StorageType().clone('nonVolatile')).setMaxAccess("readonly")
if mibBuilder.loadTexts: ifcpSessionStorageType.setStatus('current')
ifcpSessionStatsTable = MibTable((1, 3, 6, 1, 2, 1, 10, 230, 1, 2, 2), )
if mibBuilder.loadTexts: ifcpSessionStatsTable.setStatus('current')
ifcpSessionStatsEntry = MibTableRow((1, 3, 6, 1, 2, 1, 10, 230, 1, 2, 2, 1), )
ifcpSessionAttributesEntry.registerAugmentions(("IFCP-MGMT-MIB", "ifcpSessionStatsEntry"))
ifcpSessionStatsEntry.setIndexNames(*ifcpSessionAttributesEntry.getIndexNames())
if mibBuilder.loadTexts: ifcpSessionStatsEntry.setStatus('current')
ifcpSessionState = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 230, 1, 2, 2, 1, 1), IfcpSessionStates()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ifcpSessionState.setStatus('current')
ifcpSessionDuration = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 230, 1, 2, 2, 1, 2), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(0, 4294967295))).setMaxAccess("readonly")
if mibBuilder.loadTexts: ifcpSessionDuration.setStatus('current')
ifcpSessionTxOctets = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 230, 1, 2, 2, 1, 3), ZeroBasedCounter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ifcpSessionTxOctets.setStatus('current')
ifcpSessionRxOctets = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 230, 1, 2, 2, 1, 4), ZeroBasedCounter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ifcpSessionRxOctets.setStatus('current')
ifcpSessionTxFrames = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 230, 1, 2, 2, 1, 5), ZeroBasedCounter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ifcpSessionTxFrames.setStatus('current')
ifcpSessionRxFrames = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 230, 1, 2, 2, 1, 6), ZeroBasedCounter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ifcpSessionRxFrames.setStatus('current')
ifcpSessionStaleFrames = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 230, 1, 2, 2, 1, 7), ZeroBasedCounter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ifcpSessionStaleFrames.setStatus('current')
ifcpSessionHeaderCRCErrors = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 230, 1, 2, 2, 1, 8), ZeroBasedCounter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ifcpSessionHeaderCRCErrors.setStatus('current')
ifcpSessionFcPayloadCRCErrors = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 230, 1, 2, 2, 1, 9), ZeroBasedCounter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ifcpSessionFcPayloadCRCErrors.setStatus('current')
ifcpSessionOtherErrors = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 230, 1, 2, 2, 1, 10), ZeroBasedCounter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ifcpSessionOtherErrors.setStatus('current')
ifcpSessionDiscontinuityTime = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 230, 1, 2, 2, 1, 11), TimeStamp()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ifcpSessionDiscontinuityTime.setStatus('current')
ifcpSessionLcStatsTable = MibTable((1, 3, 6, 1, 2, 1, 10, 230, 1, 2, 3), )
if mibBuilder.loadTexts: ifcpSessionLcStatsTable.setStatus('current')
ifcpSessionLcStatsEntry = MibTableRow((1, 3, 6, 1, 2, 1, 10, 230, 1, 2, 3, 1), )
ifcpSessionAttributesEntry.registerAugmentions(("IFCP-MGMT-MIB", "ifcpSessionLcStatsEntry"))
ifcpSessionLcStatsEntry.setIndexNames(*ifcpSessionAttributesEntry.getIndexNames())
if mibBuilder.loadTexts: ifcpSessionLcStatsEntry.setStatus('current')
ifcpSessionLcTxOctets = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 230, 1, 2, 3, 1, 1), ZeroBasedCounter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ifcpSessionLcTxOctets.setStatus('current')
ifcpSessionLcRxOctets = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 230, 1, 2, 3, 1, 2), ZeroBasedCounter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ifcpSessionLcRxOctets.setStatus('current')
ifcpSessionLcTxFrames = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 230, 1, 2, 3, 1, 3), ZeroBasedCounter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ifcpSessionLcTxFrames.setStatus('current')
ifcpSessionLcRxFrames = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 230, 1, 2, 3, 1, 4), ZeroBasedCounter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ifcpSessionLcRxFrames.setStatus('current')
ifcpSessionLcStaleFrames = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 230, 1, 2, 3, 1, 5), ZeroBasedCounter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ifcpSessionLcStaleFrames.setStatus('current')
ifcpSessionLcHeaderCRCErrors = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 230, 1, 2, 3, 1, 6), ZeroBasedCounter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ifcpSessionLcHeaderCRCErrors.setStatus('current')
ifcpSessionLcFcPayloadCRCErrors = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 230, 1, 2, 3, 1, 7), ZeroBasedCounter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ifcpSessionLcFcPayloadCRCErrors.setStatus('current')
ifcpSessionLcOtherErrors = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 230, 1, 2, 3, 1, 8), ZeroBasedCounter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ifcpSessionLcOtherErrors.setStatus('current')
ifcpCompliances = MibIdentifier((1, 3, 6, 1, 2, 1, 10, 230, 2, 1))
ifcpGatewayCompliance = ModuleCompliance((1, 3, 6, 1, 2, 1, 10, 230, 2, 1, 1)).setObjects(("IFCP-MGMT-MIB", "ifcpLclGatewayGroup"), ("IFCP-MGMT-MIB", "ifcpLclGatewaySessionGroup"), ("IFCP-MGMT-MIB", "ifcpLclGatewaySessionStatsGroup"), ("IFCP-MGMT-MIB", "ifcpLclGatewaySessionLcStatsGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ifcpGatewayCompliance = ifcpGatewayCompliance.setStatus('deprecated')
ifcpGatewayComplianceNoTranslation = ModuleCompliance((1, 3, 6, 1, 2, 1, 10, 230, 2, 1, 2)).setObjects(("IFCP-MGMT-MIB", "ifcpLclGatewayGroup"), ("IFCP-MGMT-MIB", "ifcpLclGatewaySessionGroupNoTranslation"), ("IFCP-MGMT-MIB", "ifcpLclGatewaySessionStatsGroup"), ("IFCP-MGMT-MIB", "ifcpLclGatewaySessionLcStatsGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ifcpGatewayComplianceNoTranslation = ifcpGatewayComplianceNoTranslation.setStatus('current')
ifcpGroups = MibIdentifier((1, 3, 6, 1, 2, 1, 10, 230, 2, 2))
ifcpLclGatewayGroup = ObjectGroup((1, 3, 6, 1, 2, 1, 10, 230, 2, 2, 1)).setObjects(("IFCP-MGMT-MIB", "ifcpLclGtwyInstPhyIndex"), ("IFCP-MGMT-MIB", "ifcpLclGtwyInstVersionMin"), ("IFCP-MGMT-MIB", "ifcpLclGtwyInstVersionMax"), ("IFCP-MGMT-MIB", "ifcpLclGtwyInstAddrTransMode"), ("IFCP-MGMT-MIB", "ifcpLclGtwyInstFcBrdcstSupport"), ("IFCP-MGMT-MIB", "ifcpLclGtwyInstDefaultIpTOV"), ("IFCP-MGMT-MIB", "ifcpLclGtwyInstDefaultLTInterval"), ("IFCP-MGMT-MIB", "ifcpLclGtwyInstDescr"), ("IFCP-MGMT-MIB", "ifcpLclGtwyInstNumActiveSessions"), ("IFCP-MGMT-MIB", "ifcpLclGtwyInstStorageType"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ifcpLclGatewayGroup = ifcpLclGatewayGroup.setStatus('current')
ifcpLclGatewaySessionGroup = ObjectGroup((1, 3, 6, 1, 2, 1, 10, 230, 2, 2, 4)).setObjects(("IFCP-MGMT-MIB", "ifcpSessionLclPrtlIfIndex"), ("IFCP-MGMT-MIB", "ifcpSessionLclPrtlAddrType"), ("IFCP-MGMT-MIB", "ifcpSessionLclPrtlAddr"), ("IFCP-MGMT-MIB", "ifcpSessionLclPrtlTcpPort"), ("IFCP-MGMT-MIB", "ifcpSessionLclNpWwun"), ("IFCP-MGMT-MIB", "ifcpSessionLclNpFcid"), ("IFCP-MGMT-MIB", "ifcpSessionRmtNpWwun"), ("IFCP-MGMT-MIB", "ifcpSessionRmtPrtlIfAddrType"), ("IFCP-MGMT-MIB", "ifcpSessionRmtPrtlIfAddr"), ("IFCP-MGMT-MIB", "ifcpSessionRmtPrtlTcpPort"), ("IFCP-MGMT-MIB", "ifcpSessionRmtNpFcid"), ("IFCP-MGMT-MIB", "ifcpSessionRmtNpFcidAlias"), ("IFCP-MGMT-MIB", "ifcpSessionIpTOV"), ("IFCP-MGMT-MIB", "ifcpSessionLclLTIntvl"), ("IFCP-MGMT-MIB", "ifcpSessionRmtLTIntvl"), ("IFCP-MGMT-MIB", "ifcpSessionBound"), ("IFCP-MGMT-MIB", "ifcpSessionStorageType"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ifcpLclGatewaySessionGroup = ifcpLclGatewaySessionGroup.setStatus('deprecated')
ifcpLclGatewaySessionStatsGroup = ObjectGroup((1, 3, 6, 1, 2, 1, 10, 230, 2, 2, 5)).setObjects(("IFCP-MGMT-MIB", "ifcpSessionState"), ("IFCP-MGMT-MIB", "ifcpSessionDuration"), ("IFCP-MGMT-MIB", "ifcpSessionTxOctets"), ("IFCP-MGMT-MIB", "ifcpSessionRxOctets"), ("IFCP-MGMT-MIB", "ifcpSessionTxFrames"), ("IFCP-MGMT-MIB", "ifcpSessionRxFrames"), ("IFCP-MGMT-MIB", "ifcpSessionStaleFrames"), ("IFCP-MGMT-MIB", "ifcpSessionHeaderCRCErrors"), ("IFCP-MGMT-MIB", "ifcpSessionFcPayloadCRCErrors"), ("IFCP-MGMT-MIB", "ifcpSessionOtherErrors"), ("IFCP-MGMT-MIB", "ifcpSessionDiscontinuityTime"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ifcpLclGatewaySessionStatsGroup = ifcpLclGatewaySessionStatsGroup.setStatus('current')
ifcpLclGatewaySessionLcStatsGroup = ObjectGroup((1, 3, 6, 1, 2, 1, 10, 230, 2, 2, 6)).setObjects(("IFCP-MGMT-MIB", "ifcpSessionLcTxOctets"), ("IFCP-MGMT-MIB", "ifcpSessionLcRxOctets"), ("IFCP-MGMT-MIB", "ifcpSessionLcTxFrames"), ("IFCP-MGMT-MIB", "ifcpSessionLcRxFrames"), ("IFCP-MGMT-MIB", "ifcpSessionLcStaleFrames"), ("IFCP-MGMT-MIB", "ifcpSessionLcHeaderCRCErrors"), ("IFCP-MGMT-MIB", "ifcpSessionLcFcPayloadCRCErrors"), ("IFCP-MGMT-MIB", "ifcpSessionLcOtherErrors"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ifcpLclGatewaySessionLcStatsGroup = ifcpLclGatewaySessionLcStatsGroup.setStatus('current')
ifcpLclGatewaySessionGroupNoTranslation = ObjectGroup((1, 3, 6, 1, 2, 1, 10, 230, 2, 2, 7)).setObjects(("IFCP-MGMT-MIB", "ifcpSessionLclPrtlIfIndex"), ("IFCP-MGMT-MIB", "ifcpSessionLclPrtlAddrType"), ("IFCP-MGMT-MIB", "ifcpSessionLclPrtlAddr"), ("IFCP-MGMT-MIB", "ifcpSessionLclPrtlTcpPort"), ("IFCP-MGMT-MIB", "ifcpSessionLclNpWwun"), ("IFCP-MGMT-MIB", "ifcpSessionLclNpFcid"), ("IFCP-MGMT-MIB", "ifcpSessionRmtNpWwun"), ("IFCP-MGMT-MIB", "ifcpSessionRmtPrtlIfAddrType"), ("IFCP-MGMT-MIB", "ifcpSessionRmtPrtlIfAddr"), ("IFCP-MGMT-MIB", "ifcpSessionRmtPrtlTcpPort"), ("IFCP-MGMT-MIB", "ifcpSessionRmtNpFcid"), ("IFCP-MGMT-MIB", "ifcpSessionIpTOV"), ("IFCP-MGMT-MIB", "ifcpSessionLclLTIntvl"), ("IFCP-MGMT-MIB", "ifcpSessionRmtLTIntvl"), ("IFCP-MGMT-MIB", "ifcpSessionBound"), ("IFCP-MGMT-MIB", "ifcpSessionStorageType"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ifcpLclGatewaySessionGroupNoTranslation = ifcpLclGatewaySessionGroupNoTranslation.setStatus('current')
mibBuilder.exportSymbols("IFCP-MGMT-MIB", ifcpSessionRmtLTIntvl=ifcpSessionRmtLTIntvl, ifcpSessionRmtPrtlTcpPort=ifcpSessionRmtPrtlTcpPort, ifcpSessionRxFrames=ifcpSessionRxFrames, ifcpSessionRmtPrtlIfAddr=ifcpSessionRmtPrtlIfAddr, ifcpLclGatewayInfo=ifcpLclGatewayInfo, ifcpSessionHeaderCRCErrors=ifcpSessionHeaderCRCErrors, ifcpLclGtwyInstVersionMin=ifcpLclGtwyInstVersionMin, ifcpGatewayConformance=ifcpGatewayConformance, ifcpSessionTxFrames=ifcpSessionTxFrames, ifcpSessionRxOctets=ifcpSessionRxOctets, ifcpLclGtwyInstFcBrdcstSupport=ifcpLclGtwyInstFcBrdcstSupport, PYSNMP_MODULE_ID=ifcpMgmtMIB, ifcpSessionLclNpWwun=ifcpSessionLclNpWwun, ifcpGatewayObjects=ifcpGatewayObjects, ifcpSessionIndex=ifcpSessionIndex, ifcpLclGtwyInstStorageType=ifcpLclGtwyInstStorageType, ifcpSessionLclPrtlAddrType=ifcpSessionLclPrtlAddrType, ifcpSessionStaleFrames=ifcpSessionStaleFrames, ifcpSessionRmtNpFcid=ifcpSessionRmtNpFcid, ifcpSessionDiscontinuityTime=ifcpSessionDiscontinuityTime, ifcpSessionBound=ifcpSessionBound, ifcpSessionFcPayloadCRCErrors=ifcpSessionFcPayloadCRCErrors, ifcpSessionAttributesTable=ifcpSessionAttributesTable, IfcpSessionStates=IfcpSessionStates, ifcpSessionIpTOV=ifcpSessionIpTOV, ifcpSessionStatsTable=ifcpSessionStatsTable, ifcpSessionDuration=ifcpSessionDuration, ifcpSessionOtherErrors=ifcpSessionOtherErrors, ifcpGatewayComplianceNoTranslation=ifcpGatewayComplianceNoTranslation, ifcpSessionLclPrtlAddr=ifcpSessionLclPrtlAddr, ifcpSessionState=ifcpSessionState, ifcpLclGatewaySessionGroup=ifcpLclGatewaySessionGroup, ifcpSessionLcStatsTable=ifcpSessionLcStatsTable, ifcpLclGtwyInstNumActiveSessions=ifcpLclGtwyInstNumActiveSessions, ifcpLclGtwyInstDefaultLTInterval=ifcpLclGtwyInstDefaultLTInterval, ifcpSessionStatsEntry=ifcpSessionStatsEntry, ifcpLclGtwyInstIndex=ifcpLclGtwyInstIndex, ifcpGatewayCompliance=ifcpGatewayCompliance, IfcpLTIorZero=IfcpLTIorZero, ifcpSessionLclPrtlIfIndex=ifcpSessionLclPrtlIfIndex, ifcpSessionLcTxFrames=ifcpSessionLcTxFrames, ifcpSessionLcRxFrames=ifcpSessionLcRxFrames, IfcpAddressMode=IfcpAddressMode, ifcpLclGtwyInstDefaultIpTOV=ifcpLclGtwyInstDefaultIpTOV, ifcpSessionRmtNpFcidAlias=ifcpSessionRmtNpFcidAlias, ifcpSessionLcTxOctets=ifcpSessionLcTxOctets, ifcpSessionLclLTIntvl=ifcpSessionLclLTIntvl, ifcpLclGtwyInstPhyIndex=ifcpLclGtwyInstPhyIndex, ifcpSessionLcStaleFrames=ifcpSessionLcStaleFrames, ifcpLclGtwyInstVersionMax=ifcpLclGtwyInstVersionMax, ifcpLclGtwyInstEntry=ifcpLclGtwyInstEntry, ifcpLclGtwyInstTable=ifcpLclGtwyInstTable, ifcpSessionLcRxOctets=ifcpSessionLcRxOctets, ifcpSessionStorageType=ifcpSessionStorageType, ifcpSessionLcFcPayloadCRCErrors=ifcpSessionLcFcPayloadCRCErrors, ifcpSessionRmtNpWwun=ifcpSessionRmtNpWwun, ifcpCompliances=ifcpCompliances, ifcpGroups=ifcpGroups, ifcpNportSessionInfo=ifcpNportSessionInfo, ifcpSessionLcOtherErrors=ifcpSessionLcOtherErrors, ifcpSessionAttributesEntry=ifcpSessionAttributesEntry, ifcpLclGatewaySessionGroupNoTranslation=ifcpLclGatewaySessionGroupNoTranslation, ifcpLclGtwyInstDescr=ifcpLclGtwyInstDescr, IfcpIpTOVorZero=IfcpIpTOVorZero, ifcpSessionLclNpFcid=ifcpSessionLclNpFcid, ifcpSessionLclPrtlTcpPort=ifcpSessionLclPrtlTcpPort, ifcpLclGtwyInstAddrTransMode=ifcpLclGtwyInstAddrTransMode, ifcpSessionLcStatsEntry=ifcpSessionLcStatsEntry, ifcpLclGatewaySessionLcStatsGroup=ifcpLclGatewaySessionLcStatsGroup, ifcpSessionTxOctets=ifcpSessionTxOctets, ifcpSessionRmtPrtlIfAddrType=ifcpSessionRmtPrtlIfAddrType, ifcpSessionLcHeaderCRCErrors=ifcpSessionLcHeaderCRCErrors, ifcpMgmtMIB=ifcpMgmtMIB, ifcpLclGatewayGroup=ifcpLclGatewayGroup, ifcpLclGatewaySessionStatsGroup=ifcpLclGatewaySessionStatsGroup)
