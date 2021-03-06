#
# PySNMP MIB module CISCOSB-SYSMNG-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/CISCOSB-SYSMNG-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 18:07:40 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
Integer, OctetString, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "Integer", "OctetString", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsUnion, SingleValueConstraint, ValueRangeConstraint, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsUnion", "SingleValueConstraint", "ValueRangeConstraint", "ConstraintsIntersection")
Percents, switch001 = mibBuilder.importSymbols("CISCOSB-MIB", "Percents", "switch001")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
Unsigned32, Counter64, NotificationType, MibIdentifier, TimeTicks, IpAddress, ObjectIdentity, Counter32, iso, MibScalar, MibTable, MibTableRow, MibTableColumn, ModuleIdentity, Integer32, Gauge32, Bits = mibBuilder.importSymbols("SNMPv2-SMI", "Unsigned32", "Counter64", "NotificationType", "MibIdentifier", "TimeTicks", "IpAddress", "ObjectIdentity", "Counter32", "iso", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "ModuleIdentity", "Integer32", "Gauge32", "Bits")
DisplayString, TextualConvention, RowPointer, RowStatus, TruthValue = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention", "RowPointer", "RowStatus", "TruthValue")
rlSysmngMib = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 204))
rlSysmngMib.setRevisions(('2010-10-31 00:00',))
if mibBuilder.loadTexts: rlSysmngMib.setLastUpdated('201010310000Z')
if mibBuilder.loadTexts: rlSysmngMib.setOrganization('Cisco Systems, Inc.')
class SysmngResourceRouteType(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5))
    namedValues = NamedValues(("ipv4", 1), ("ipv6", 2), ("ipmv4", 3), ("ipmv6", 4), ("nonIp", 5))

class SysmngResourceRouteUsageType(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11))
    namedValues = NamedValues(("ipv4Neighbor", 1), ("ipv4Address", 2), ("ipv4Route", 3), ("ipv6Neighbor", 4), ("ipv6Address", 5), ("ipv6OnlinkPrefix", 6), ("ipv6Route", 7), ("ipmv4Route", 8), ("ipmv4RouteStarG", 9), ("ipmv6Route", 10), ("ipmv6RouteStarG", 11))

class SysmngPoolType(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))
    namedValues = NamedValues(("router", 1), ("iscsi", 2), ("voip", 3), ("misc", 4))

rlSysmngTcamAllocations = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 204, 1))
rlSysmngTcamAllocationsTable = MibTable((1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 204, 1, 1), )
if mibBuilder.loadTexts: rlSysmngTcamAllocationsTable.setStatus('current')
rlSysmngTcamAllocationsEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 204, 1, 1, 1), ).setIndexNames((0, "CISCOSB-SYSMNG-MIB", "rlSysmngTcamAllocProfileName"), (0, "CISCOSB-SYSMNG-MIB", "rlSysmngTcamAllocPoolType"))
if mibBuilder.loadTexts: rlSysmngTcamAllocationsEntry.setStatus('current')
rlSysmngTcamAllocProfileName = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 204, 1, 1, 1, 1), DisplayString())
if mibBuilder.loadTexts: rlSysmngTcamAllocProfileName.setStatus('current')
rlSysmngTcamAllocPoolType = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 204, 1, 1, 1, 2), SysmngPoolType())
if mibBuilder.loadTexts: rlSysmngTcamAllocPoolType.setStatus('current')
rlSysmngTcamAllocMinRequiredEntries = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 204, 1, 1, 1, 3), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rlSysmngTcamAllocMinRequiredEntries.setStatus('current')
rlSysmngTcamAllocStaticConfigEntries = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 204, 1, 1, 1, 4), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rlSysmngTcamAllocStaticConfigEntries.setStatus('current')
rlSysmngTcamAllocInUseEntries = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 204, 1, 1, 1, 5), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rlSysmngTcamAllocInUseEntries.setStatus('current')
rlSysmngTcamAllocPoolSize = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 204, 1, 1, 1, 6), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rlSysmngTcamAllocPoolSize.setStatus('current')
rlSysmngResource = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 204, 2))
rlSysmngResourceTable = MibTable((1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 204, 2, 1), )
if mibBuilder.loadTexts: rlSysmngResourceTable.setStatus('current')
rlSysmngResourceEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 204, 2, 1, 1), ).setIndexNames((0, "CISCOSB-SYSMNG-MIB", "rlSysmngResourceRouteType"))
if mibBuilder.loadTexts: rlSysmngResourceEntry.setStatus('current')
rlSysmngResourceRouteType = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 204, 2, 1, 1, 1), SysmngResourceRouteType())
if mibBuilder.loadTexts: rlSysmngResourceRouteType.setStatus('current')
rlSysmngResourceCurrentUse = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 204, 2, 1, 1, 2), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rlSysmngResourceCurrentUse.setStatus('current')
rlSysmngResourceCurrentUseHw = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 204, 2, 1, 1, 3), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rlSysmngResourceCurrentUseHw.setStatus('current')
rlSysmngResourceCurrentMax = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 204, 2, 1, 1, 4), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rlSysmngResourceCurrentMax.setStatus('current')
rlSysmngResourceCurrentMaxHw = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 204, 2, 1, 1, 5), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rlSysmngResourceCurrentMaxHw.setStatus('current')
rlSysmngResourceTemporaryMax = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 204, 2, 1, 1, 6), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rlSysmngResourceTemporaryMax.setStatus('current')
rlSysmngResourceTemporaryMaxHw = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 204, 2, 1, 1, 7), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rlSysmngResourceTemporaryMaxHw.setStatus('current')
rlSysmngResourceCurrentNexthopMax = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 204, 2, 1, 1, 8), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rlSysmngResourceCurrentNexthopMax.setStatus('current')
rlSysmngResourceCurrentNexthopMaxHw = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 204, 2, 1, 1, 9), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rlSysmngResourceCurrentNexthopMaxHw.setStatus('current')
rlSysmngResourceCurrentNexthopUse = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 204, 2, 1, 1, 10), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rlSysmngResourceCurrentNexthopUse.setStatus('current')
rlSysmngResourceCurrentNexthopUseHw = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 204, 2, 1, 1, 11), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rlSysmngResourceCurrentNexthopUseHw.setStatus('current')
rlSysmngRouterResourceAction = MibScalar((1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 204, 3), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rlSysmngRouterResourceAction.setStatus('current')
rlSysmngResourceUsage = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 204, 4))
rlSysmngResourceUsageTable = MibTable((1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 204, 4, 1), )
if mibBuilder.loadTexts: rlSysmngResourceUsageTable.setStatus('current')
rlSysmngResourceUsageEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 204, 4, 1, 1), ).setIndexNames((0, "CISCOSB-SYSMNG-MIB", "rlSysmngResourceUsageType"))
if mibBuilder.loadTexts: rlSysmngResourceUsageEntry.setStatus('current')
rlSysmngResourceUsageType = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 204, 4, 1, 1, 1), SysmngResourceRouteUsageType())
if mibBuilder.loadTexts: rlSysmngResourceUsageType.setStatus('current')
rlSysmngResourceUsageNum = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 204, 4, 1, 1, 2), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rlSysmngResourceUsageNum.setStatus('current')
rlSysmngResourcePerUnit = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 204, 5))
rlSysmngResourcePerUnitTable = MibTable((1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 204, 5, 1), )
if mibBuilder.loadTexts: rlSysmngResourcePerUnitTable.setStatus('current')
rlSysmngResourcePerUnitEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 204, 5, 1, 1), ).setIndexNames((0, "CISCOSB-SYSMNG-MIB", "rlSysmngResourcePerUnitRouteType"), (0, "CISCOSB-SYSMNG-MIB", "rlSysmngResourcePerUnitUnitId"))
if mibBuilder.loadTexts: rlSysmngResourcePerUnitEntry.setStatus('current')
rlSysmngResourcePerUnitRouteType = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 204, 5, 1, 1, 1), SysmngResourceRouteType())
if mibBuilder.loadTexts: rlSysmngResourcePerUnitRouteType.setStatus('current')
rlSysmngResourcePerUnitUnitId = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 204, 5, 1, 1, 2), Unsigned32())
if mibBuilder.loadTexts: rlSysmngResourcePerUnitUnitId.setStatus('current')
rlSysmngResourcePerUnitCurrentUse = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 204, 5, 1, 1, 3), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rlSysmngResourcePerUnitCurrentUse.setStatus('current')
rlSysmngResourcePerUnitCurrentUseHw = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 204, 5, 1, 1, 4), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rlSysmngResourcePerUnitCurrentUseHw.setStatus('current')
rlSysmngResourcePerUnitCurrentMax = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 204, 5, 1, 1, 5), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rlSysmngResourcePerUnitCurrentMax.setStatus('current')
rlSysmngResourcePerUnitCurrentMaxHw = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 204, 5, 1, 1, 6), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rlSysmngResourcePerUnitCurrentMaxHw.setStatus('current')
rlSysmngResourcePerUnitTemporaryMax = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 204, 5, 1, 1, 7), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rlSysmngResourcePerUnitTemporaryMax.setStatus('current')
rlSysmngResourcePerUnitTemporaryMaxHw = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 204, 5, 1, 1, 8), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rlSysmngResourcePerUnitTemporaryMaxHw.setStatus('current')
rlSysmngResourcePerUnitCurrentNexthopMax = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 204, 5, 1, 1, 9), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rlSysmngResourcePerUnitCurrentNexthopMax.setStatus('current')
rlSysmngResourcePerUnitCurrentNexthopMaxHw = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 204, 5, 1, 1, 10), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rlSysmngResourcePerUnitCurrentNexthopMaxHw.setStatus('current')
rlSysmngResourcePerUnitCurrentNexthopUse = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 204, 5, 1, 1, 11), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rlSysmngResourcePerUnitCurrentNexthopUse.setStatus('current')
rlSysmngResourcePerUnitCurrentNexthopUseHw = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 204, 5, 1, 1, 12), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rlSysmngResourcePerUnitCurrentNexthopUseHw.setStatus('current')
mibBuilder.exportSymbols("CISCOSB-SYSMNG-MIB", rlSysmngTcamAllocProfileName=rlSysmngTcamAllocProfileName, rlSysmngTcamAllocStaticConfigEntries=rlSysmngTcamAllocStaticConfigEntries, rlSysmngResourceCurrentUseHw=rlSysmngResourceCurrentUseHw, rlSysmngTcamAllocations=rlSysmngTcamAllocations, rlSysmngTcamAllocPoolType=rlSysmngTcamAllocPoolType, rlSysmngResourcePerUnitTable=rlSysmngResourcePerUnitTable, rlSysmngResourcePerUnit=rlSysmngResourcePerUnit, rlSysmngResourcePerUnitCurrentMaxHw=rlSysmngResourcePerUnitCurrentMaxHw, rlSysmngResourcePerUnitTemporaryMaxHw=rlSysmngResourcePerUnitTemporaryMaxHw, rlSysmngResourcePerUnitCurrentNexthopMax=rlSysmngResourcePerUnitCurrentNexthopMax, rlSysmngResourceTemporaryMax=rlSysmngResourceTemporaryMax, rlSysmngTcamAllocPoolSize=rlSysmngTcamAllocPoolSize, rlSysmngResourceCurrentMax=rlSysmngResourceCurrentMax, rlSysmngResourceEntry=rlSysmngResourceEntry, SysmngResourceRouteUsageType=SysmngResourceRouteUsageType, rlSysmngResourcePerUnitCurrentNexthopUseHw=rlSysmngResourcePerUnitCurrentNexthopUseHw, PYSNMP_MODULE_ID=rlSysmngMib, rlSysmngResourcePerUnitCurrentNexthopUse=rlSysmngResourcePerUnitCurrentNexthopUse, SysmngPoolType=SysmngPoolType, rlSysmngResourcePerUnitCurrentUseHw=rlSysmngResourcePerUnitCurrentUseHw, rlSysmngResourcePerUnitCurrentNexthopMaxHw=rlSysmngResourcePerUnitCurrentNexthopMaxHw, rlSysmngTcamAllocationsTable=rlSysmngTcamAllocationsTable, rlSysmngMib=rlSysmngMib, rlSysmngResourceTable=rlSysmngResourceTable, rlSysmngResourcePerUnitRouteType=rlSysmngResourcePerUnitRouteType, rlSysmngResourceCurrentNexthopUse=rlSysmngResourceCurrentNexthopUse, rlSysmngResourceCurrentNexthopMax=rlSysmngResourceCurrentNexthopMax, rlSysmngResourcePerUnitUnitId=rlSysmngResourcePerUnitUnitId, rlSysmngResource=rlSysmngResource, rlSysmngResourceUsageType=rlSysmngResourceUsageType, rlSysmngResourceUsage=rlSysmngResourceUsage, rlSysmngResourcePerUnitTemporaryMax=rlSysmngResourcePerUnitTemporaryMax, rlSysmngResourceUsageNum=rlSysmngResourceUsageNum, rlSysmngResourceCurrentUse=rlSysmngResourceCurrentUse, rlSysmngTcamAllocMinRequiredEntries=rlSysmngTcamAllocMinRequiredEntries, rlSysmngResourceCurrentNexthopUseHw=rlSysmngResourceCurrentNexthopUseHw, rlSysmngResourceUsageEntry=rlSysmngResourceUsageEntry, SysmngResourceRouteType=SysmngResourceRouteType, rlSysmngRouterResourceAction=rlSysmngRouterResourceAction, rlSysmngTcamAllocInUseEntries=rlSysmngTcamAllocInUseEntries, rlSysmngResourceCurrentNexthopMaxHw=rlSysmngResourceCurrentNexthopMaxHw, rlSysmngResourcePerUnitEntry=rlSysmngResourcePerUnitEntry, rlSysmngResourcePerUnitCurrentUse=rlSysmngResourcePerUnitCurrentUse, rlSysmngResourceCurrentMaxHw=rlSysmngResourceCurrentMaxHw, rlSysmngTcamAllocationsEntry=rlSysmngTcamAllocationsEntry, rlSysmngResourceUsageTable=rlSysmngResourceUsageTable, rlSysmngResourceRouteType=rlSysmngResourceRouteType, rlSysmngResourcePerUnitCurrentMax=rlSysmngResourcePerUnitCurrentMax, rlSysmngResourceTemporaryMaxHw=rlSysmngResourceTemporaryMaxHw)
