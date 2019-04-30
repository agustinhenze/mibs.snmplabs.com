#
# PySNMP MIB module DELL-NETWORKING-VIRTUAL-LINK-TRUNK-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/DELL-NETWORKING-VIRTUAL-LINK-TRUNK-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 18:22:48 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
OctetString, ObjectIdentifier, Integer = mibBuilder.importSymbols("ASN1", "OctetString", "ObjectIdentifier", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ConstraintsUnion, SingleValueConstraint, ValueSizeConstraint, ValueRangeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ConstraintsUnion", "SingleValueConstraint", "ValueSizeConstraint", "ValueRangeConstraint")
dellNetMgmt, = mibBuilder.importSymbols("DELL-NETWORKING-SMI", "dellNetMgmt")
InterfaceIndex, = mibBuilder.importSymbols("IF-MIB", "InterfaceIndex")
InetAddress, InetAddressType = mibBuilder.importSymbols("INET-ADDRESS-MIB", "InetAddress", "InetAddressType")
ObjectGroup, ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ObjectGroup", "ModuleCompliance", "NotificationGroup")
NotificationType, Counter32, Counter64, MibScalar, MibTable, MibTableRow, MibTableColumn, iso, Bits, TimeTicks, Gauge32, Unsigned32, ObjectIdentity, Integer32, ModuleIdentity, IpAddress, MibIdentifier = mibBuilder.importSymbols("SNMPv2-SMI", "NotificationType", "Counter32", "Counter64", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "iso", "Bits", "TimeTicks", "Gauge32", "Unsigned32", "ObjectIdentity", "Integer32", "ModuleIdentity", "IpAddress", "MibIdentifier")
MacAddress, TextualConvention, DisplayString, TimeInterval = mibBuilder.importSymbols("SNMPv2-TC", "MacAddress", "TextualConvention", "DisplayString", "TimeInterval")
dellNetVirtualLinkTrunkMib = ModuleIdentity((1, 3, 6, 1, 4, 1, 6027, 3, 17))
dellNetVirtualLinkTrunkMib.setRevisions(('2012-11-28 00:00', '2012-05-21 00:00', '2012-05-14 00:00', '2012-04-02 00:00', '2011-05-06 00:00', '2011-03-14 00:00',))
if mibBuilder.loadTexts: dellNetVirtualLinkTrunkMib.setLastUpdated('201211280000Z')
if mibBuilder.loadTexts: dellNetVirtualLinkTrunkMib.setOrganization('Dell Inc')
dellNetVirtualLinkTrunkObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 6027, 3, 17, 1))
dellNetVirtualLinkTrunkNotifObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 6027, 3, 17, 2))
class DellNetVLTMemberLinkStatus(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3))
    namedValues = NamedValues(("linkNotEstablished", 0), ("linkUp", 1), ("linkDown", 2), ("linkError", 3))

dellNetVirtualLinkTrunkTable = MibTable((1, 3, 6, 1, 4, 1, 6027, 3, 17, 1, 1), )
if mibBuilder.loadTexts: dellNetVirtualLinkTrunkTable.setStatus('current')
dellNetVirtualLinkTrunkTableEntry = MibTableRow((1, 3, 6, 1, 4, 1, 6027, 3, 17, 1, 1, 1), ).setIndexNames((0, "DELL-NETWORKING-VIRTUAL-LINK-TRUNK-MIB", "dellNetVLTDomainId"))
if mibBuilder.loadTexts: dellNetVirtualLinkTrunkTableEntry.setStatus('current')
dellNetVLTDomainId = MibTableColumn((1, 3, 6, 1, 4, 1, 6027, 3, 17, 1, 1, 1, 1), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dellNetVLTDomainId.setStatus('current')
dellNetVLTMacAddr = MibTableColumn((1, 3, 6, 1, 4, 1, 6027, 3, 17, 1, 1, 1, 2), MacAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dellNetVLTMacAddr.setStatus('current')
dellNetVLTPriority = MibTableColumn((1, 3, 6, 1, 4, 1, 6027, 3, 17, 1, 1, 1, 3), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(1, 65535)).clone(32768)).setMaxAccess("readonly")
if mibBuilder.loadTexts: dellNetVLTPriority.setStatus('current')
dellNetVLTIclIfIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 6027, 3, 17, 1, 1, 1, 4), InterfaceIndex()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dellNetVLTIclIfIndex.setStatus('current')
dellNetVLTRole = MibTableColumn((1, 3, 6, 1, 4, 1, 6027, 3, 17, 1, 1, 1, 5), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1, 2))).clone(namedValues=NamedValues(("standAlone", 0), ("primary", 1), ("secondary", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: dellNetVLTRole.setStatus('current')
dellNetVLTPeerStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 6027, 3, 17, 1, 1, 1, 6), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3))).clone(namedValues=NamedValues(("notEstablished", 0), ("peerUp", 1), ("peerDown", 2), ("linkDown", 3)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: dellNetVLTPeerStatus.setStatus('current')
dellNetVLTIclStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 6027, 3, 17, 1, 1, 1, 7), DellNetVLTMemberLinkStatus()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dellNetVLTIclStatus.setStatus('current')
dellNetVLTHBeatStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 6027, 3, 17, 1, 1, 1, 8), DellNetVLTMemberLinkStatus()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dellNetVLTHBeatStatus.setStatus('current')
dellNetVLTBkUpIpAddrType = MibTableColumn((1, 3, 6, 1, 4, 1, 6027, 3, 17, 1, 1, 1, 9), InetAddressType()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dellNetVLTBkUpIpAddrType.setStatus('current')
dellNetVLTBkUpIpAddr = MibTableColumn((1, 3, 6, 1, 4, 1, 6027, 3, 17, 1, 1, 1, 10), InetAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dellNetVLTBkUpIpAddr.setStatus('current')
dellNetVLTBkUpInterval = MibTableColumn((1, 3, 6, 1, 4, 1, 6027, 3, 17, 1, 1, 1, 11), TimeInterval().subtype(subtypeSpec=ValueRangeConstraint(100, 500)).clone(100)).setMaxAccess("readonly")
if mibBuilder.loadTexts: dellNetVLTBkUpInterval.setStatus('current')
dellNetVLTRemoteMacAddr = MibTableColumn((1, 3, 6, 1, 4, 1, 6027, 3, 17, 1, 1, 1, 12), MacAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dellNetVLTRemoteMacAddr.setStatus('current')
dellNetVLTRemoteRolePriority = MibTableColumn((1, 3, 6, 1, 4, 1, 6027, 3, 17, 1, 1, 1, 13), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(1, 65535)).clone(32768)).setMaxAccess("readonly")
if mibBuilder.loadTexts: dellNetVLTRemoteRolePriority.setStatus('current')
dellNetVLTUnitId = MibTableColumn((1, 3, 6, 1, 4, 1, 6027, 3, 17, 1, 1, 1, 14), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dellNetVLTUnitId.setStatus('current')
dellNetVLTVersionMajor = MibTableColumn((1, 3, 6, 1, 4, 1, 6027, 3, 17, 1, 1, 1, 15), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dellNetVLTVersionMajor.setStatus('current')
dellNetVLTVersionMinor = MibTableColumn((1, 3, 6, 1, 4, 1, 6027, 3, 17, 1, 1, 1, 16), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dellNetVLTVersionMinor.setStatus('current')
dellNetVLTRemoteUnitId = MibTableColumn((1, 3, 6, 1, 4, 1, 6027, 3, 17, 1, 1, 1, 17), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dellNetVLTRemoteUnitId.setStatus('current')
dellNetVLTRemoteVersionMajor = MibTableColumn((1, 3, 6, 1, 4, 1, 6027, 3, 17, 1, 1, 1, 18), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dellNetVLTRemoteVersionMajor.setStatus('current')
dellNetVLTRemoteVersionMinor = MibTableColumn((1, 3, 6, 1, 4, 1, 6027, 3, 17, 1, 1, 1, 19), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dellNetVLTRemoteVersionMinor.setStatus('current')
dellNetVLTIclBwStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 6027, 3, 17, 1, 1, 1, 20), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1))).clone(namedValues=NamedValues(("belowthreshold", 0), ("abovethreshold", 1)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: dellNetVLTIclBwStatus.setStatus('current')
dellNetVLTCfgSysMacAddr = MibTableColumn((1, 3, 6, 1, 4, 1, 6027, 3, 17, 1, 1, 1, 21), MacAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dellNetVLTCfgSysMacAddr.setStatus('current')
dellNetVLTPeerRouting = MibTableColumn((1, 3, 6, 1, 4, 1, 6027, 3, 17, 1, 1, 1, 22), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1))).clone(namedValues=NamedValues(("disabled", 0), ("enabled", 1)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: dellNetVLTPeerRouting.setStatus('current')
dellNetVLTPeerRoutingTimeout = MibTableColumn((1, 3, 6, 1, 4, 1, 6027, 3, 17, 1, 1, 1, 23), TimeInterval().subtype(subtypeSpec=ValueRangeConstraint(0, 65535))).setMaxAccess("readonly")
if mibBuilder.loadTexts: dellNetVLTPeerRoutingTimeout.setStatus('current')
dellNetVLTRemotePeerRouting = MibTableColumn((1, 3, 6, 1, 4, 1, 6027, 3, 17, 1, 1, 1, 24), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1))).clone(namedValues=NamedValues(("disabled", 0), ("enabled", 1)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: dellNetVLTRemotePeerRouting.setStatus('current')
dellNetVirtualLinkStatsTable = MibTable((1, 3, 6, 1, 4, 1, 6027, 3, 17, 1, 2), )
if mibBuilder.loadTexts: dellNetVirtualLinkStatsTable.setStatus('current')
dellNetVirtualLinkStatsTableEntry = MibTableRow((1, 3, 6, 1, 4, 1, 6027, 3, 17, 1, 2, 1), )
dellNetVirtualLinkTrunkTableEntry.registerAugmentions(("DELL-NETWORKING-VIRTUAL-LINK-TRUNK-MIB", "dellNetVirtualLinkStatsTableEntry"))
dellNetVirtualLinkStatsTableEntry.setIndexNames(*dellNetVirtualLinkTrunkTableEntry.getIndexNames())
if mibBuilder.loadTexts: dellNetVirtualLinkStatsTableEntry.setStatus('current')
dellNetVLTStatNumHelloSent = MibTableColumn((1, 3, 6, 1, 4, 1, 6027, 3, 17, 1, 2, 1, 1), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dellNetVLTStatNumHelloSent.setStatus('current')
dellNetVLTStatNumHelloRcvd = MibTableColumn((1, 3, 6, 1, 4, 1, 6027, 3, 17, 1, 2, 1, 2), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dellNetVLTStatNumHelloRcvd.setStatus('current')
dellNetVLTStatNumHbeatSent = MibTableColumn((1, 3, 6, 1, 4, 1, 6027, 3, 17, 1, 2, 1, 3), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dellNetVLTStatNumHbeatSent.setStatus('current')
dellNetVLTStatNumHbeatRcvd = MibTableColumn((1, 3, 6, 1, 4, 1, 6027, 3, 17, 1, 2, 1, 4), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dellNetVLTStatNumHbeatRcvd.setStatus('current')
dellNetVLTStatNumDomainErrors = MibTableColumn((1, 3, 6, 1, 4, 1, 6027, 3, 17, 1, 2, 1, 5), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dellNetVLTStatNumDomainErrors.setStatus('current')
dellNetVLTStatNumVersionErrors = MibTableColumn((1, 3, 6, 1, 4, 1, 6027, 3, 17, 1, 2, 1, 6), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dellNetVLTStatNumVersionErrors.setStatus('current')
dellNetVirtualLinkDetailsTable = MibTable((1, 3, 6, 1, 4, 1, 6027, 3, 17, 1, 3), )
if mibBuilder.loadTexts: dellNetVirtualLinkDetailsTable.setStatus('current')
dellNetVirtualLinkDetailsTableEntry = MibTableRow((1, 3, 6, 1, 4, 1, 6027, 3, 17, 1, 3, 1), ).setIndexNames((0, "DELL-NETWORKING-VIRTUAL-LINK-TRUNK-MIB", "dellNetVLTDetailLocalLagID"))
if mibBuilder.loadTexts: dellNetVirtualLinkDetailsTableEntry.setStatus('current')
dellNetVLTDetailLocalLagID = MibTableColumn((1, 3, 6, 1, 4, 1, 6027, 3, 17, 1, 3, 1, 1), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(1, 65535))).setMaxAccess("readonly")
if mibBuilder.loadTexts: dellNetVLTDetailLocalLagID.setStatus('current')
dellNetVLTDetailPeerLagID = MibTableColumn((1, 3, 6, 1, 4, 1, 6027, 3, 17, 1, 3, 1, 2), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(1, 65535))).setMaxAccess("readonly")
if mibBuilder.loadTexts: dellNetVLTDetailPeerLagID.setStatus('current')
dellNetVLTDetailLocalStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 6027, 3, 17, 1, 3, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1))).clone(namedValues=NamedValues(("down", 0), ("up", 1)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: dellNetVLTDetailLocalStatus.setStatus('current')
dellNetVLTDetailPeerStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 6027, 3, 17, 1, 3, 1, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1))).clone(namedValues=NamedValues(("down", 0), ("up", 1)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: dellNetVLTDetailPeerStatus.setStatus('current')
dellNetVLTErrorReason = MibScalar((1, 3, 6, 1, 4, 1, 6027, 3, 17, 1, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6))).clone(namedValues=NamedValues(("noError", 1), ("domainIdMismatch", 2), ("unitIdMismatch", 3), ("versionMismatch", 4), ("sysMacMismatch", 5), ("peerRoutingMismatch", 6)))).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: dellNetVLTErrorReason.setStatus('current')
dellNetVirtualLinkTrunkNotifications = MibIdentifier((1, 3, 6, 1, 4, 1, 6027, 3, 17, 2, 0))
dellNetVLTRoleChange = NotificationType((1, 3, 6, 1, 4, 1, 6027, 3, 17, 2, 0, 1)).setObjects(("DELL-NETWORKING-VIRTUAL-LINK-TRUNK-MIB", "dellNetVLTRole"))
if mibBuilder.loadTexts: dellNetVLTRoleChange.setStatus('current')
dellNetVLTIclStatusChange = NotificationType((1, 3, 6, 1, 4, 1, 6027, 3, 17, 2, 0, 2)).setObjects(("DELL-NETWORKING-VIRTUAL-LINK-TRUNK-MIB", "dellNetVLTIclStatus"))
if mibBuilder.loadTexts: dellNetVLTIclStatusChange.setStatus('current')
dellNetVLTPeerStatusChange = NotificationType((1, 3, 6, 1, 4, 1, 6027, 3, 17, 2, 0, 3)).setObjects(("DELL-NETWORKING-VIRTUAL-LINK-TRUNK-MIB", "dellNetVLTPeerStatus"))
if mibBuilder.loadTexts: dellNetVLTPeerStatusChange.setStatus('current')
dellNetVLTHBeatStatusChange = NotificationType((1, 3, 6, 1, 4, 1, 6027, 3, 17, 2, 0, 4)).setObjects(("DELL-NETWORKING-VIRTUAL-LINK-TRUNK-MIB", "dellNetVLTHBeatStatus"))
if mibBuilder.loadTexts: dellNetVLTHBeatStatusChange.setStatus('current')
dellNetVLTIclBwUsageExceed = NotificationType((1, 3, 6, 1, 4, 1, 6027, 3, 17, 2, 0, 5)).setObjects(("DELL-NETWORKING-VIRTUAL-LINK-TRUNK-MIB", "dellNetVLTIclIfIndex"), ("DELL-NETWORKING-VIRTUAL-LINK-TRUNK-MIB", "dellNetVLTIclBwStatus"))
if mibBuilder.loadTexts: dellNetVLTIclBwUsageExceed.setStatus('current')
dellNetVLTDomainConfigError = NotificationType((1, 3, 6, 1, 4, 1, 6027, 3, 17, 2, 0, 6)).setObjects(("DELL-NETWORKING-VIRTUAL-LINK-TRUNK-MIB", "dellNetVLTErrorReason"))
if mibBuilder.loadTexts: dellNetVLTDomainConfigError.setStatus('current')
dellNetVirtualLinkTrunkConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 6027, 3, 17, 3))
dellNetVirtualLinkTrunkCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 6027, 3, 17, 3, 1))
dellNetVirtualLinkTrunkGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 6027, 3, 17, 3, 2))
dellNetVirtualLinkTrunkCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 6027, 3, 17, 3, 1, 1)).setObjects(("DELL-NETWORKING-VIRTUAL-LINK-TRUNK-MIB", "dellNetVirtualLinkTrunkGroup"), ("DELL-NETWORKING-VIRTUAL-LINK-TRUNK-MIB", "dellNetVirtualLinkStatisticsGroup"), ("DELL-NETWORKING-VIRTUAL-LINK-TRUNK-MIB", "dellNetVirtualLinkNotificationGroup"), ("DELL-NETWORKING-VIRTUAL-LINK-TRUNK-MIB", "dellNetVirtualLinkDetailsTableGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    dellNetVirtualLinkTrunkCompliance = dellNetVirtualLinkTrunkCompliance.setStatus('current')
dellNetVirtualLinkTrunkGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 6027, 3, 17, 3, 2, 1)).setObjects(("DELL-NETWORKING-VIRTUAL-LINK-TRUNK-MIB", "dellNetVLTDomainId"), ("DELL-NETWORKING-VIRTUAL-LINK-TRUNK-MIB", "dellNetVLTMacAddr"), ("DELL-NETWORKING-VIRTUAL-LINK-TRUNK-MIB", "dellNetVLTPriority"), ("DELL-NETWORKING-VIRTUAL-LINK-TRUNK-MIB", "dellNetVLTIclIfIndex"), ("DELL-NETWORKING-VIRTUAL-LINK-TRUNK-MIB", "dellNetVLTRole"), ("DELL-NETWORKING-VIRTUAL-LINK-TRUNK-MIB", "dellNetVLTPeerStatus"), ("DELL-NETWORKING-VIRTUAL-LINK-TRUNK-MIB", "dellNetVLTIclStatus"), ("DELL-NETWORKING-VIRTUAL-LINK-TRUNK-MIB", "dellNetVLTHBeatStatus"), ("DELL-NETWORKING-VIRTUAL-LINK-TRUNK-MIB", "dellNetVLTBkUpIpAddrType"), ("DELL-NETWORKING-VIRTUAL-LINK-TRUNK-MIB", "dellNetVLTBkUpIpAddr"), ("DELL-NETWORKING-VIRTUAL-LINK-TRUNK-MIB", "dellNetVLTBkUpInterval"), ("DELL-NETWORKING-VIRTUAL-LINK-TRUNK-MIB", "dellNetVLTRemoteMacAddr"), ("DELL-NETWORKING-VIRTUAL-LINK-TRUNK-MIB", "dellNetVLTRemoteRolePriority"), ("DELL-NETWORKING-VIRTUAL-LINK-TRUNK-MIB", "dellNetVLTUnitId"), ("DELL-NETWORKING-VIRTUAL-LINK-TRUNK-MIB", "dellNetVLTVersionMajor"), ("DELL-NETWORKING-VIRTUAL-LINK-TRUNK-MIB", "dellNetVLTVersionMinor"), ("DELL-NETWORKING-VIRTUAL-LINK-TRUNK-MIB", "dellNetVLTRemoteUnitId"), ("DELL-NETWORKING-VIRTUAL-LINK-TRUNK-MIB", "dellNetVLTRemoteVersionMajor"), ("DELL-NETWORKING-VIRTUAL-LINK-TRUNK-MIB", "dellNetVLTRemoteVersionMinor"), ("DELL-NETWORKING-VIRTUAL-LINK-TRUNK-MIB", "dellNetVLTIclBwStatus"), ("DELL-NETWORKING-VIRTUAL-LINK-TRUNK-MIB", "dellNetVLTCfgSysMacAddr"), ("DELL-NETWORKING-VIRTUAL-LINK-TRUNK-MIB", "dellNetVLTPeerRouting"), ("DELL-NETWORKING-VIRTUAL-LINK-TRUNK-MIB", "dellNetVLTPeerRoutingTimeout"), ("DELL-NETWORKING-VIRTUAL-LINK-TRUNK-MIB", "dellNetVLTRemotePeerRouting"), ("DELL-NETWORKING-VIRTUAL-LINK-TRUNK-MIB", "dellNetVLTErrorReason"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    dellNetVirtualLinkTrunkGroup = dellNetVirtualLinkTrunkGroup.setStatus('current')
dellNetVirtualLinkStatisticsGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 6027, 3, 17, 3, 2, 2)).setObjects(("DELL-NETWORKING-VIRTUAL-LINK-TRUNK-MIB", "dellNetVLTStatNumHelloSent"), ("DELL-NETWORKING-VIRTUAL-LINK-TRUNK-MIB", "dellNetVLTStatNumHelloRcvd"), ("DELL-NETWORKING-VIRTUAL-LINK-TRUNK-MIB", "dellNetVLTStatNumHbeatSent"), ("DELL-NETWORKING-VIRTUAL-LINK-TRUNK-MIB", "dellNetVLTStatNumHbeatRcvd"), ("DELL-NETWORKING-VIRTUAL-LINK-TRUNK-MIB", "dellNetVLTStatNumDomainErrors"), ("DELL-NETWORKING-VIRTUAL-LINK-TRUNK-MIB", "dellNetVLTStatNumVersionErrors"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    dellNetVirtualLinkStatisticsGroup = dellNetVirtualLinkStatisticsGroup.setStatus('current')
dellNetVirtualLinkNotificationGroup = NotificationGroup((1, 3, 6, 1, 4, 1, 6027, 3, 17, 3, 2, 3)).setObjects(("DELL-NETWORKING-VIRTUAL-LINK-TRUNK-MIB", "dellNetVLTRoleChange"), ("DELL-NETWORKING-VIRTUAL-LINK-TRUNK-MIB", "dellNetVLTIclStatusChange"), ("DELL-NETWORKING-VIRTUAL-LINK-TRUNK-MIB", "dellNetVLTPeerStatusChange"), ("DELL-NETWORKING-VIRTUAL-LINK-TRUNK-MIB", "dellNetVLTHBeatStatusChange"), ("DELL-NETWORKING-VIRTUAL-LINK-TRUNK-MIB", "dellNetVLTIclBwUsageExceed"), ("DELL-NETWORKING-VIRTUAL-LINK-TRUNK-MIB", "dellNetVLTDomainConfigError"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    dellNetVirtualLinkNotificationGroup = dellNetVirtualLinkNotificationGroup.setStatus('current')
dellNetVirtualLinkDetailsTableGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 6027, 3, 17, 3, 2, 4)).setObjects(("DELL-NETWORKING-VIRTUAL-LINK-TRUNK-MIB", "dellNetVLTDetailLocalLagID"), ("DELL-NETWORKING-VIRTUAL-LINK-TRUNK-MIB", "dellNetVLTDetailPeerLagID"), ("DELL-NETWORKING-VIRTUAL-LINK-TRUNK-MIB", "dellNetVLTDetailLocalStatus"), ("DELL-NETWORKING-VIRTUAL-LINK-TRUNK-MIB", "dellNetVLTDetailPeerStatus"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    dellNetVirtualLinkDetailsTableGroup = dellNetVirtualLinkDetailsTableGroup.setStatus('current')
mibBuilder.exportSymbols("DELL-NETWORKING-VIRTUAL-LINK-TRUNK-MIB", dellNetVirtualLinkTrunkMib=dellNetVirtualLinkTrunkMib, dellNetVLTStatNumHbeatSent=dellNetVLTStatNumHbeatSent, dellNetVirtualLinkTrunkTableEntry=dellNetVirtualLinkTrunkTableEntry, dellNetVirtualLinkDetailsTableGroup=dellNetVirtualLinkDetailsTableGroup, dellNetVLTRemoteVersionMajor=dellNetVLTRemoteVersionMajor, dellNetVLTHBeatStatusChange=dellNetVLTHBeatStatusChange, dellNetVirtualLinkTrunkCompliance=dellNetVirtualLinkTrunkCompliance, dellNetVirtualLinkNotificationGroup=dellNetVirtualLinkNotificationGroup, dellNetVirtualLinkStatsTable=dellNetVirtualLinkStatsTable, dellNetVirtualLinkTrunkNotifObjects=dellNetVirtualLinkTrunkNotifObjects, dellNetVirtualLinkTrunkGroup=dellNetVirtualLinkTrunkGroup, dellNetVirtualLinkTrunkTable=dellNetVirtualLinkTrunkTable, dellNetVirtualLinkTrunkConformance=dellNetVirtualLinkTrunkConformance, dellNetVLTRemotePeerRouting=dellNetVLTRemotePeerRouting, dellNetVLTRole=dellNetVLTRole, dellNetVLTBkUpInterval=dellNetVLTBkUpInterval, dellNetVLTDomainId=dellNetVLTDomainId, dellNetVirtualLinkStatsTableEntry=dellNetVirtualLinkStatsTableEntry, dellNetVLTStatNumVersionErrors=dellNetVLTStatNumVersionErrors, PYSNMP_MODULE_ID=dellNetVirtualLinkTrunkMib, dellNetVLTPeerStatusChange=dellNetVLTPeerStatusChange, dellNetVLTIclBwStatus=dellNetVLTIclBwStatus, dellNetVLTDetailPeerLagID=dellNetVLTDetailPeerLagID, dellNetVLTPeerStatus=dellNetVLTPeerStatus, dellNetVLTRemoteUnitId=dellNetVLTRemoteUnitId, dellNetVLTDetailPeerStatus=dellNetVLTDetailPeerStatus, DellNetVLTMemberLinkStatus=DellNetVLTMemberLinkStatus, dellNetVLTRemoteRolePriority=dellNetVLTRemoteRolePriority, dellNetVirtualLinkDetailsTable=dellNetVirtualLinkDetailsTable, dellNetVirtualLinkTrunkCompliances=dellNetVirtualLinkTrunkCompliances, dellNetVLTRoleChange=dellNetVLTRoleChange, dellNetVLTBkUpIpAddr=dellNetVLTBkUpIpAddr, dellNetVLTDomainConfigError=dellNetVLTDomainConfigError, dellNetVLTStatNumDomainErrors=dellNetVLTStatNumDomainErrors, dellNetVLTBkUpIpAddrType=dellNetVLTBkUpIpAddrType, dellNetVLTErrorReason=dellNetVLTErrorReason, dellNetVLTStatNumHbeatRcvd=dellNetVLTStatNumHbeatRcvd, dellNetVirtualLinkDetailsTableEntry=dellNetVirtualLinkDetailsTableEntry, dellNetVirtualLinkTrunkNotifications=dellNetVirtualLinkTrunkNotifications, dellNetVLTRemoteVersionMinor=dellNetVLTRemoteVersionMinor, dellNetVLTIclBwUsageExceed=dellNetVLTIclBwUsageExceed, dellNetVLTRemoteMacAddr=dellNetVLTRemoteMacAddr, dellNetVLTDetailLocalLagID=dellNetVLTDetailLocalLagID, dellNetVLTHBeatStatus=dellNetVLTHBeatStatus, dellNetVirtualLinkTrunkObjects=dellNetVirtualLinkTrunkObjects, dellNetVLTVersionMinor=dellNetVLTVersionMinor, dellNetVirtualLinkTrunkGroups=dellNetVirtualLinkTrunkGroups, dellNetVLTMacAddr=dellNetVLTMacAddr, dellNetVLTIclStatusChange=dellNetVLTIclStatusChange, dellNetVLTIclStatus=dellNetVLTIclStatus, dellNetVirtualLinkStatisticsGroup=dellNetVirtualLinkStatisticsGroup, dellNetVLTCfgSysMacAddr=dellNetVLTCfgSysMacAddr, dellNetVLTStatNumHelloRcvd=dellNetVLTStatNumHelloRcvd, dellNetVLTDetailLocalStatus=dellNetVLTDetailLocalStatus, dellNetVLTStatNumHelloSent=dellNetVLTStatNumHelloSent, dellNetVLTPeerRouting=dellNetVLTPeerRouting, dellNetVLTVersionMajor=dellNetVLTVersionMajor, dellNetVLTPriority=dellNetVLTPriority, dellNetVLTPeerRoutingTimeout=dellNetVLTPeerRoutingTimeout, dellNetVLTUnitId=dellNetVLTUnitId, dellNetVLTIclIfIndex=dellNetVLTIclIfIndex)