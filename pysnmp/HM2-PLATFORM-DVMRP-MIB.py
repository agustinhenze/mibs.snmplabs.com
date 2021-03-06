#
# PySNMP MIB module HM2-PLATFORM-DVMRP-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/HM2-PLATFORM-DVMRP-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 19:19:07 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ValueSizeConstraint, SingleValueConstraint, ConstraintsUnion, ValueRangeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ValueSizeConstraint", "SingleValueConstraint", "ConstraintsUnion", "ValueRangeConstraint")
hm2PlatformMulticast, = mibBuilder.importSymbols("HM2-PLATFORM-MULTICAST-MIB", "hm2PlatformMulticast")
InterfaceIndex, InterfaceIndexOrZero = mibBuilder.importSymbols("IF-MIB", "InterfaceIndex", "InterfaceIndexOrZero")
SnmpAdminString, = mibBuilder.importSymbols("SNMP-FRAMEWORK-MIB", "SnmpAdminString")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
TimeTicks, Gauge32, MibScalar, MibTable, MibTableRow, MibTableColumn, NotificationType, ModuleIdentity, IpAddress, iso, Bits, Counter64, Unsigned32, MibIdentifier, Integer32, ObjectIdentity, Counter32 = mibBuilder.importSymbols("SNMPv2-SMI", "TimeTicks", "Gauge32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "NotificationType", "ModuleIdentity", "IpAddress", "iso", "Bits", "Counter64", "Unsigned32", "MibIdentifier", "Integer32", "ObjectIdentity", "Counter32")
DisplayString, RowStatus, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "RowStatus", "TextualConvention")
hm2AgentDvmrp = ModuleIdentity((1, 3, 6, 1, 4, 1, 248, 12, 4, 249))
hm2AgentDvmrp.setRevisions(('2013-07-26 00:00',))
if mibBuilder.loadTexts: hm2AgentDvmrp.setLastUpdated('201307260000Z')
if mibBuilder.loadTexts: hm2AgentDvmrp.setOrganization('Hirschmann Automation and Control GmbH')
hm2AgentDvmrpMIBNotifications = MibIdentifier((1, 3, 6, 1, 4, 1, 248, 12, 4, 249, 0))
hm2AgentDvmrpMIBObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 248, 12, 4, 249, 1))
hm2AgentDvmrpGroup = MibIdentifier((1, 3, 6, 1, 4, 1, 248, 12, 4, 249, 1, 1))
hm2AgentDvmrpScalar = MibIdentifier((1, 3, 6, 1, 4, 1, 248, 12, 4, 249, 1, 1, 1))
hm2AgentDvmrpVersionString = MibScalar((1, 3, 6, 1, 4, 1, 248, 12, 4, 249, 1, 1, 1, 1), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hm2AgentDvmrpVersionString.setStatus('current')
hm2AgentDvmrpGenerationId = MibScalar((1, 3, 6, 1, 4, 1, 248, 12, 4, 249, 1, 1, 1, 2), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hm2AgentDvmrpGenerationId.setStatus('current')
hm2AgentDvmrpNumRoutes = MibScalar((1, 3, 6, 1, 4, 1, 248, 12, 4, 249, 1, 1, 1, 3), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hm2AgentDvmrpNumRoutes.setStatus('current')
hm2AgentDvmrpReachableRoutes = MibScalar((1, 3, 6, 1, 4, 1, 248, 12, 4, 249, 1, 1, 1, 4), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hm2AgentDvmrpReachableRoutes.setStatus('current')
hm2AgentDvmrpInterfaceTable = MibTable((1, 3, 6, 1, 4, 1, 248, 12, 4, 249, 1, 1, 2), )
if mibBuilder.loadTexts: hm2AgentDvmrpInterfaceTable.setStatus('current')
hm2AgentDvmrpInterfaceEntry = MibTableRow((1, 3, 6, 1, 4, 1, 248, 12, 4, 249, 1, 1, 2, 1), ).setIndexNames((0, "HM2-PLATFORM-DVMRP-MIB", "hm2AgentDvmrpInterfaceIfIndex"))
if mibBuilder.loadTexts: hm2AgentDvmrpInterfaceEntry.setStatus('current')
hm2AgentDvmrpInterfaceIfIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 248, 12, 4, 249, 1, 1, 2, 1, 1), InterfaceIndex())
if mibBuilder.loadTexts: hm2AgentDvmrpInterfaceIfIndex.setStatus('current')
hm2AgentDvmrpInterfaceLocalAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 248, 12, 4, 249, 1, 1, 2, 1, 2), IpAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hm2AgentDvmrpInterfaceLocalAddress.setStatus('current')
hm2AgentDvmrpInterfaceMetric = MibTableColumn((1, 3, 6, 1, 4, 1, 248, 12, 4, 249, 1, 1, 2, 1, 3), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 31)).clone(1)).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hm2AgentDvmrpInterfaceMetric.setStatus('current')
hm2AgentDvmrpInterfaceStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 248, 12, 4, 249, 1, 1, 2, 1, 4), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hm2AgentDvmrpInterfaceStatus.setStatus('current')
hm2AgentDvmrpInterfaceRcvBadPkts = MibTableColumn((1, 3, 6, 1, 4, 1, 248, 12, 4, 249, 1, 1, 2, 1, 5), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hm2AgentDvmrpInterfaceRcvBadPkts.setStatus('current')
hm2AgentDvmrpInterfaceRcvBadRoutes = MibTableColumn((1, 3, 6, 1, 4, 1, 248, 12, 4, 249, 1, 1, 2, 1, 6), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hm2AgentDvmrpInterfaceRcvBadRoutes.setStatus('current')
hm2AgentDvmrpInterfaceSentRoutes = MibTableColumn((1, 3, 6, 1, 4, 1, 248, 12, 4, 249, 1, 1, 2, 1, 7), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hm2AgentDvmrpInterfaceSentRoutes.setStatus('current')
hm2AgentDvmrpInterfaceInterfaceKey = MibTableColumn((1, 3, 6, 1, 4, 1, 248, 12, 4, 249, 1, 1, 2, 1, 8), SnmpAdminString()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hm2AgentDvmrpInterfaceInterfaceKey.setStatus('current')
hm2AgentDvmrpInterfaceInterfaceKeyVersion = MibTableColumn((1, 3, 6, 1, 4, 1, 248, 12, 4, 249, 1, 1, 2, 1, 9), Integer32()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hm2AgentDvmrpInterfaceInterfaceKeyVersion.setStatus('current')
hm2AgentDvmrpInterfaceGenerationId = MibTableColumn((1, 3, 6, 1, 4, 1, 248, 12, 4, 249, 1, 1, 2, 1, 248), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hm2AgentDvmrpInterfaceGenerationId.setStatus('current')
hm2AgentDvmrpNeighborTable = MibTable((1, 3, 6, 1, 4, 1, 248, 12, 4, 249, 1, 1, 3), )
if mibBuilder.loadTexts: hm2AgentDvmrpNeighborTable.setStatus('current')
hm2AgentDvmrpNeighborEntry = MibTableRow((1, 3, 6, 1, 4, 1, 248, 12, 4, 249, 1, 1, 3, 1), ).setIndexNames((0, "HM2-PLATFORM-DVMRP-MIB", "hm2AgentDvmrpNeighborIfIndex"), (0, "HM2-PLATFORM-DVMRP-MIB", "hm2AgentDvmrpNeighborAddress"))
if mibBuilder.loadTexts: hm2AgentDvmrpNeighborEntry.setStatus('current')
hm2AgentDvmrpNeighborIfIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 248, 12, 4, 249, 1, 1, 3, 1, 1), InterfaceIndex())
if mibBuilder.loadTexts: hm2AgentDvmrpNeighborIfIndex.setStatus('current')
hm2AgentDvmrpNeighborAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 248, 12, 4, 249, 1, 1, 3, 1, 2), IpAddress())
if mibBuilder.loadTexts: hm2AgentDvmrpNeighborAddress.setStatus('current')
hm2AgentDvmrpNeighborUpTime = MibTableColumn((1, 3, 6, 1, 4, 1, 248, 12, 4, 249, 1, 1, 3, 1, 3), TimeTicks()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hm2AgentDvmrpNeighborUpTime.setStatus('current')
hm2AgentDvmrpNeighborExpiryTime = MibTableColumn((1, 3, 6, 1, 4, 1, 248, 12, 4, 249, 1, 1, 3, 1, 4), TimeTicks()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hm2AgentDvmrpNeighborExpiryTime.setStatus('current')
hm2AgentDvmrpNeighborGenerationId = MibTableColumn((1, 3, 6, 1, 4, 1, 248, 12, 4, 249, 1, 1, 3, 1, 5), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hm2AgentDvmrpNeighborGenerationId.setStatus('current')
hm2AgentDvmrpNeighborMajorVersion = MibTableColumn((1, 3, 6, 1, 4, 1, 248, 12, 4, 249, 1, 1, 3, 1, 6), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 255))).setMaxAccess("readonly")
if mibBuilder.loadTexts: hm2AgentDvmrpNeighborMajorVersion.setStatus('current')
hm2AgentDvmrpNeighborMinorVersion = MibTableColumn((1, 3, 6, 1, 4, 1, 248, 12, 4, 249, 1, 1, 3, 1, 7), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 255))).setMaxAccess("readonly")
if mibBuilder.loadTexts: hm2AgentDvmrpNeighborMinorVersion.setStatus('current')
hm2AgentDvmrpNeighborCapabilities = MibTableColumn((1, 3, 6, 1, 4, 1, 248, 12, 4, 249, 1, 1, 3, 1, 8), Bits().clone(namedValues=NamedValues(("leaf", 0), ("prune", 1), ("generationID", 2), ("mtrace", 3)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: hm2AgentDvmrpNeighborCapabilities.setStatus('current')
hm2AgentDvmrpNeighborRcvRoutes = MibTableColumn((1, 3, 6, 1, 4, 1, 248, 12, 4, 249, 1, 1, 3, 1, 9), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hm2AgentDvmrpNeighborRcvRoutes.setStatus('current')
hm2AgentDvmrpNeighborRcvBadPkts = MibTableColumn((1, 3, 6, 1, 4, 1, 248, 12, 4, 249, 1, 1, 3, 1, 10), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hm2AgentDvmrpNeighborRcvBadPkts.setStatus('current')
hm2AgentDvmrpNeighborRcvBadRoutes = MibTableColumn((1, 3, 6, 1, 4, 1, 248, 12, 4, 249, 1, 1, 3, 1, 11), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hm2AgentDvmrpNeighborRcvBadRoutes.setStatus('current')
hm2AgentDvmrpNeighborState = MibTableColumn((1, 3, 6, 1, 4, 1, 248, 12, 4, 249, 1, 1, 3, 1, 12), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))).clone(namedValues=NamedValues(("oneway", 1), ("active", 2), ("ignoring", 3), ("down", 4)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: hm2AgentDvmrpNeighborState.setStatus('current')
hm2AgentDvmrpRouteTable = MibTable((1, 3, 6, 1, 4, 1, 248, 12, 4, 249, 1, 1, 4), )
if mibBuilder.loadTexts: hm2AgentDvmrpRouteTable.setStatus('current')
hm2AgentDvmrpRouteEntry = MibTableRow((1, 3, 6, 1, 4, 1, 248, 12, 4, 249, 1, 1, 4, 1), ).setIndexNames((0, "HM2-PLATFORM-DVMRP-MIB", "hm2AgentDvmrpRouteSource"), (0, "HM2-PLATFORM-DVMRP-MIB", "hm2AgentDvmrpRouteSourceMask"))
if mibBuilder.loadTexts: hm2AgentDvmrpRouteEntry.setStatus('current')
hm2AgentDvmrpRouteSource = MibTableColumn((1, 3, 6, 1, 4, 1, 248, 12, 4, 249, 1, 1, 4, 1, 1), IpAddress())
if mibBuilder.loadTexts: hm2AgentDvmrpRouteSource.setStatus('current')
hm2AgentDvmrpRouteSourceMask = MibTableColumn((1, 3, 6, 1, 4, 1, 248, 12, 4, 249, 1, 1, 4, 1, 2), IpAddress())
if mibBuilder.loadTexts: hm2AgentDvmrpRouteSourceMask.setStatus('current')
hm2AgentDvmrpRouteUpstreamNeighbor = MibTableColumn((1, 3, 6, 1, 4, 1, 248, 12, 4, 249, 1, 1, 4, 1, 3), IpAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hm2AgentDvmrpRouteUpstreamNeighbor.setStatus('current')
hm2AgentDvmrpRouteIfIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 248, 12, 4, 249, 1, 1, 4, 1, 4), InterfaceIndexOrZero()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hm2AgentDvmrpRouteIfIndex.setStatus('current')
hm2AgentDvmrpRouteMetric = MibTableColumn((1, 3, 6, 1, 4, 1, 248, 12, 4, 249, 1, 1, 4, 1, 5), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 32))).setMaxAccess("readonly")
if mibBuilder.loadTexts: hm2AgentDvmrpRouteMetric.setStatus('current')
hm2AgentDvmrpRouteExpiryTime = MibTableColumn((1, 3, 6, 1, 4, 1, 248, 12, 4, 249, 1, 1, 4, 1, 6), TimeTicks()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hm2AgentDvmrpRouteExpiryTime.setStatus('current')
hm2AgentDvmrpRouteUpTime = MibTableColumn((1, 3, 6, 1, 4, 1, 248, 12, 4, 249, 1, 1, 4, 1, 7), TimeTicks()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hm2AgentDvmrpRouteUpTime.setStatus('current')
hm2AgentDvmrpRouteNextHopTable = MibTable((1, 3, 6, 1, 4, 1, 248, 12, 4, 249, 1, 1, 5), )
if mibBuilder.loadTexts: hm2AgentDvmrpRouteNextHopTable.setStatus('current')
hm2AgentDvmrpRouteNextHopEntry = MibTableRow((1, 3, 6, 1, 4, 1, 248, 12, 4, 249, 1, 1, 5, 1), ).setIndexNames((0, "HM2-PLATFORM-DVMRP-MIB", "hm2AgentDvmrpRouteNextHopSource"), (0, "HM2-PLATFORM-DVMRP-MIB", "hm2AgentDvmrpRouteNextHopSourceMask"), (0, "HM2-PLATFORM-DVMRP-MIB", "hm2AgentDvmrpRouteNextHopIfIndex"))
if mibBuilder.loadTexts: hm2AgentDvmrpRouteNextHopEntry.setStatus('current')
hm2AgentDvmrpRouteNextHopSource = MibTableColumn((1, 3, 6, 1, 4, 1, 248, 12, 4, 249, 1, 1, 5, 1, 1), IpAddress())
if mibBuilder.loadTexts: hm2AgentDvmrpRouteNextHopSource.setStatus('current')
hm2AgentDvmrpRouteNextHopSourceMask = MibTableColumn((1, 3, 6, 1, 4, 1, 248, 12, 4, 249, 1, 1, 5, 1, 2), IpAddress())
if mibBuilder.loadTexts: hm2AgentDvmrpRouteNextHopSourceMask.setStatus('current')
hm2AgentDvmrpRouteNextHopIfIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 248, 12, 4, 249, 1, 1, 5, 1, 3), InterfaceIndex())
if mibBuilder.loadTexts: hm2AgentDvmrpRouteNextHopIfIndex.setStatus('current')
hm2AgentDvmrpRouteNextHopType = MibTableColumn((1, 3, 6, 1, 4, 1, 248, 12, 4, 249, 1, 1, 5, 1, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("leaf", 1), ("branch", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: hm2AgentDvmrpRouteNextHopType.setStatus('current')
hm2AgentDvmrpPruneTable = MibTable((1, 3, 6, 1, 4, 1, 248, 12, 4, 249, 1, 1, 6), )
if mibBuilder.loadTexts: hm2AgentDvmrpPruneTable.setStatus('current')
hm2AgentDvmrpPruneEntry = MibTableRow((1, 3, 6, 1, 4, 1, 248, 12, 4, 249, 1, 1, 6, 1), ).setIndexNames((0, "HM2-PLATFORM-DVMRP-MIB", "hm2AgentDvmrpPruneGroup"), (0, "HM2-PLATFORM-DVMRP-MIB", "hm2AgentDvmrpPruneSource"), (0, "HM2-PLATFORM-DVMRP-MIB", "hm2AgentDvmrpPruneSourceMask"))
if mibBuilder.loadTexts: hm2AgentDvmrpPruneEntry.setStatus('current')
hm2AgentDvmrpPruneGroup = MibTableColumn((1, 3, 6, 1, 4, 1, 248, 12, 4, 249, 1, 1, 6, 1, 1), IpAddress())
if mibBuilder.loadTexts: hm2AgentDvmrpPruneGroup.setStatus('current')
hm2AgentDvmrpPruneSource = MibTableColumn((1, 3, 6, 1, 4, 1, 248, 12, 4, 249, 1, 1, 6, 1, 2), IpAddress())
if mibBuilder.loadTexts: hm2AgentDvmrpPruneSource.setStatus('current')
hm2AgentDvmrpPruneSourceMask = MibTableColumn((1, 3, 6, 1, 4, 1, 248, 12, 4, 249, 1, 1, 6, 1, 3), IpAddress())
if mibBuilder.loadTexts: hm2AgentDvmrpPruneSourceMask.setStatus('current')
hm2AgentDvmrpPruneExpiryTime = MibTableColumn((1, 3, 6, 1, 4, 1, 248, 12, 4, 249, 1, 1, 6, 1, 4), TimeTicks()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hm2AgentDvmrpPruneExpiryTime.setStatus('current')
hm2AgentDvmrpNeighborLoss = NotificationType((1, 3, 6, 1, 4, 1, 248, 12, 4, 249, 0, 1)).setObjects(("HM2-PLATFORM-DVMRP-MIB", "hm2AgentDvmrpInterfaceLocalAddress"), ("HM2-PLATFORM-DVMRP-MIB", "hm2AgentDvmrpNeighborState"))
if mibBuilder.loadTexts: hm2AgentDvmrpNeighborLoss.setStatus('current')
hm2AgentDvmrpNeighborNotPruning = NotificationType((1, 3, 6, 1, 4, 1, 248, 12, 4, 249, 0, 2)).setObjects(("HM2-PLATFORM-DVMRP-MIB", "hm2AgentDvmrpInterfaceLocalAddress"), ("HM2-PLATFORM-DVMRP-MIB", "hm2AgentDvmrpNeighborCapabilities"))
if mibBuilder.loadTexts: hm2AgentDvmrpNeighborNotPruning.setStatus('current')
mibBuilder.exportSymbols("HM2-PLATFORM-DVMRP-MIB", hm2AgentDvmrpInterfaceEntry=hm2AgentDvmrpInterfaceEntry, hm2AgentDvmrpInterfaceIfIndex=hm2AgentDvmrpInterfaceIfIndex, hm2AgentDvmrpGroup=hm2AgentDvmrpGroup, hm2AgentDvmrpNeighborNotPruning=hm2AgentDvmrpNeighborNotPruning, hm2AgentDvmrpInterfaceLocalAddress=hm2AgentDvmrpInterfaceLocalAddress, hm2AgentDvmrpInterfaceMetric=hm2AgentDvmrpInterfaceMetric, hm2AgentDvmrpInterfaceRcvBadRoutes=hm2AgentDvmrpInterfaceRcvBadRoutes, hm2AgentDvmrpNeighborState=hm2AgentDvmrpNeighborState, hm2AgentDvmrpRouteExpiryTime=hm2AgentDvmrpRouteExpiryTime, hm2AgentDvmrpRouteSource=hm2AgentDvmrpRouteSource, hm2AgentDvmrpPruneExpiryTime=hm2AgentDvmrpPruneExpiryTime, hm2AgentDvmrpReachableRoutes=hm2AgentDvmrpReachableRoutes, hm2AgentDvmrpNeighborEntry=hm2AgentDvmrpNeighborEntry, hm2AgentDvmrpRouteUpstreamNeighbor=hm2AgentDvmrpRouteUpstreamNeighbor, hm2AgentDvmrpPruneTable=hm2AgentDvmrpPruneTable, hm2AgentDvmrpScalar=hm2AgentDvmrpScalar, hm2AgentDvmrpNeighborAddress=hm2AgentDvmrpNeighborAddress, hm2AgentDvmrpRouteNextHopSourceMask=hm2AgentDvmrpRouteNextHopSourceMask, hm2AgentDvmrpNeighborCapabilities=hm2AgentDvmrpNeighborCapabilities, hm2AgentDvmrpInterfaceSentRoutes=hm2AgentDvmrpInterfaceSentRoutes, hm2AgentDvmrpInterfaceGenerationId=hm2AgentDvmrpInterfaceGenerationId, hm2AgentDvmrpMIBObjects=hm2AgentDvmrpMIBObjects, hm2AgentDvmrpRouteNextHopTable=hm2AgentDvmrpRouteNextHopTable, hm2AgentDvmrpRouteEntry=hm2AgentDvmrpRouteEntry, hm2AgentDvmrpNeighborTable=hm2AgentDvmrpNeighborTable, hm2AgentDvmrpNeighborExpiryTime=hm2AgentDvmrpNeighborExpiryTime, hm2AgentDvmrpNeighborRcvBadPkts=hm2AgentDvmrpNeighborRcvBadPkts, hm2AgentDvmrpPruneSourceMask=hm2AgentDvmrpPruneSourceMask, hm2AgentDvmrpMIBNotifications=hm2AgentDvmrpMIBNotifications, hm2AgentDvmrpRouteMetric=hm2AgentDvmrpRouteMetric, hm2AgentDvmrpRouteIfIndex=hm2AgentDvmrpRouteIfIndex, hm2AgentDvmrpPruneSource=hm2AgentDvmrpPruneSource, hm2AgentDvmrpRouteSourceMask=hm2AgentDvmrpRouteSourceMask, hm2AgentDvmrpPruneEntry=hm2AgentDvmrpPruneEntry, hm2AgentDvmrp=hm2AgentDvmrp, hm2AgentDvmrpInterfaceStatus=hm2AgentDvmrpInterfaceStatus, hm2AgentDvmrpRouteNextHopEntry=hm2AgentDvmrpRouteNextHopEntry, PYSNMP_MODULE_ID=hm2AgentDvmrp, hm2AgentDvmrpRouteUpTime=hm2AgentDvmrpRouteUpTime, hm2AgentDvmrpGenerationId=hm2AgentDvmrpGenerationId, hm2AgentDvmrpRouteNextHopIfIndex=hm2AgentDvmrpRouteNextHopIfIndex, hm2AgentDvmrpNeighborRcvRoutes=hm2AgentDvmrpNeighborRcvRoutes, hm2AgentDvmrpRouteTable=hm2AgentDvmrpRouteTable, hm2AgentDvmrpNeighborLoss=hm2AgentDvmrpNeighborLoss, hm2AgentDvmrpNeighborMinorVersion=hm2AgentDvmrpNeighborMinorVersion, hm2AgentDvmrpInterfaceInterfaceKey=hm2AgentDvmrpInterfaceInterfaceKey, hm2AgentDvmrpInterfaceInterfaceKeyVersion=hm2AgentDvmrpInterfaceInterfaceKeyVersion, hm2AgentDvmrpNeighborUpTime=hm2AgentDvmrpNeighborUpTime, hm2AgentDvmrpVersionString=hm2AgentDvmrpVersionString, hm2AgentDvmrpNeighborRcvBadRoutes=hm2AgentDvmrpNeighborRcvBadRoutes, hm2AgentDvmrpNeighborIfIndex=hm2AgentDvmrpNeighborIfIndex, hm2AgentDvmrpNumRoutes=hm2AgentDvmrpNumRoutes, hm2AgentDvmrpNeighborMajorVersion=hm2AgentDvmrpNeighborMajorVersion, hm2AgentDvmrpInterfaceRcvBadPkts=hm2AgentDvmrpInterfaceRcvBadPkts, hm2AgentDvmrpRouteNextHopType=hm2AgentDvmrpRouteNextHopType, hm2AgentDvmrpNeighborGenerationId=hm2AgentDvmrpNeighborGenerationId, hm2AgentDvmrpPruneGroup=hm2AgentDvmrpPruneGroup, hm2AgentDvmrpInterfaceTable=hm2AgentDvmrpInterfaceTable, hm2AgentDvmrpRouteNextHopSource=hm2AgentDvmrpRouteNextHopSource)
