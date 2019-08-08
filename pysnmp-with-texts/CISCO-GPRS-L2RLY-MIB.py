#
# PySNMP MIB module CISCO-GPRS-L2RLY-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/CISCO-GPRS-L2RLY-MIB
# Produced by pysmi-0.3.4 at Wed May  1 11:59:20 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
Integer, OctetString, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "Integer", "OctetString", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
SingleValueConstraint, ConstraintsUnion, ValueSizeConstraint, ValueRangeConstraint, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "SingleValueConstraint", "ConstraintsUnion", "ValueSizeConstraint", "ValueRangeConstraint", "ConstraintsIntersection")
ciscoMgmt, = mibBuilder.importSymbols("CISCO-SMI", "ciscoMgmt")
InterfaceIndex, = mibBuilder.importSymbols("IF-MIB", "InterfaceIndex")
ObjectGroup, NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "ObjectGroup", "NotificationGroup", "ModuleCompliance")
Integer32, Unsigned32, ObjectIdentity, IpAddress, Counter64, MibScalar, MibTable, MibTableRow, MibTableColumn, NotificationType, TimeTicks, Bits, Gauge32, MibIdentifier, ModuleIdentity, iso, Counter32 = mibBuilder.importSymbols("SNMPv2-SMI", "Integer32", "Unsigned32", "ObjectIdentity", "IpAddress", "Counter64", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "NotificationType", "TimeTicks", "Bits", "Gauge32", "MibIdentifier", "ModuleIdentity", "iso", "Counter32")
DisplayString, TruthValue, RowStatus, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TruthValue", "RowStatus", "TextualConvention")
ciscoGprsL2rlyMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 9, 9993))
if mibBuilder.loadTexts: ciscoGprsL2rlyMIB.setLastUpdated('9812150000Z')
if mibBuilder.loadTexts: ciscoGprsL2rlyMIB.setOrganization('Cisco Systems, Inc.')
if mibBuilder.loadTexts: ciscoGprsL2rlyMIB.setContactInfo(' Cisco Systems Customer Service Postal: 170 W Tasman Drive San Jose, CA 95134 USA Tel: +1 800 553-NETS E-mail: cs-gprs@cisco.com')
if mibBuilder.loadTexts: ciscoGprsL2rlyMIB.setDescription("The MIB Module for managing the General Packet Radio Service(GPRS) L2RLY related information on Servicing GPRS Support Node(SGSN). In GPRS network, a SGSN is typically implemented as a single node; in cisco-Alcatel joint development, it's split into Telecom part (T-node) and Datacom part (D-node). T-nodes and D-nodes are connected by two fast ethernets. A simple connectionless protocol called L2RLY is used to provide service of forwarding packet between T-unit and D-unit, flow control and defending against the failure of a FE subnet. ")
ciscoGprsL2rlyObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 9993, 1))
ciscoGprsL2rlyConfig = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 9993, 1, 1))
ciscoGprsL2rlyStats = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 9993, 1, 2))
cgprsL2rlyUid = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 9993, 1, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 64)).clone(32)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cgprsL2rlyUid.setStatus('current')
if mibBuilder.loadTexts: cgprsL2rlyUid.setDescription('L2 Relay unit identification. ')
cgprsL2rlyUnitType = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 9993, 1, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("datacomUnit", 1), ("telecomUnit", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cgprsL2rlyUnitType.setStatus('current')
if mibBuilder.loadTexts: cgprsL2rlyUnitType.setDescription(' The type can be either a datacom unit, or a telecom unit. ')
cgprsL2rlyEchoTimer = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 9993, 1, 1, 3), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 1000))).setUnits('seconds').setMaxAccess("readwrite")
if mibBuilder.loadTexts: cgprsL2rlyEchoTimer.setStatus('current')
if mibBuilder.loadTexts: cgprsL2rlyEchoTimer.setDescription('The frequency of transmission of self_id packet. This packet is transmitted periodically, for keep-alive and auto discovery purposes. ')
cgprsL2rlyFlowControlFlag = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 9993, 1, 1, 4), TruthValue()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cgprsL2rlyFlowControlFlag.setStatus('current')
if mibBuilder.loadTexts: cgprsL2rlyFlowControlFlag.setDescription("L2 Relay flow control function flag. 'on' means that the flow control has been enabled, and 'off' means the converse. ")
cgprsL2rlyDroppedPktsMonTime = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 9993, 1, 1, 5), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 65535)).clone(300)).setUnits('seconds').setMaxAccess("readwrite")
if mibBuilder.loadTexts: cgprsL2rlyDroppedPktsMonTime.setStatus('current')
if mibBuilder.loadTexts: cgprsL2rlyDroppedPktsMonTime.setDescription('The configurable time duration for monitoring the excessive rate at which packets are dropped by the L2 Relay on SGSN due to traffic congestion problem. ')
cgprsL2rlyNoRespToKeepAliveMsgNotificationEnable = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 9993, 1, 1, 6), TruthValue().clone('true')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cgprsL2rlyNoRespToKeepAliveMsgNotificationEnable.setStatus('current')
if mibBuilder.loadTexts: cgprsL2rlyNoRespToKeepAliveMsgNotificationEnable.setDescription('The object indicates whether the system produces the cgprsL2rlyNoRespToKeepAliveMsgNotification. A false value will prevent the cgprsL2rlyNoRespToKeepAliveMsgNotification from being generated by this system. ')
cgprsL2rlyUnitJoinNotificationEnable = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 9993, 1, 1, 7), TruthValue().clone('true')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cgprsL2rlyUnitJoinNotificationEnable.setStatus('current')
if mibBuilder.loadTexts: cgprsL2rlyUnitJoinNotificationEnable.setDescription('The object indicates whether the system produces the cgprsL2rlyUnitJoinNotification. A false value will prevent the cgprsL2rlyUnitJoinNotificationcgprs from being generated by this system. ')
cgprsL2rlyInterfaceTable = MibTable((1, 3, 6, 1, 4, 1, 9, 9, 9993, 1, 1, 8), )
if mibBuilder.loadTexts: cgprsL2rlyInterfaceTable.setStatus('current')
if mibBuilder.loadTexts: cgprsL2rlyInterfaceTable.setDescription('The table that lists the interfaces which l2rly is using. Currently the table has just two and always two entries. There is only one l2rly T or D unit on each router. To ensure reliability and do load sharing, there could be two fast ethernets among the l2rly units. Thus each l2rly unit could interface with two fast ethernets. At least one interface should be configured and working in order for l2rly to work. ')
cgprsL2rlyInterfaceEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9, 9, 9993, 1, 1, 8, 1), ).setIndexNames((0, "CISCO-GPRS-L2RLY-MIB", "cgprsL2rlyInterfaceId"))
if mibBuilder.loadTexts: cgprsL2rlyInterfaceEntry.setStatus('current')
if mibBuilder.loadTexts: cgprsL2rlyInterfaceEntry.setDescription(' The l2rly interface table entry. ')
cgprsL2rlyInterfaceId = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 9993, 1, 1, 8, 1, 1), InterfaceIndex())
if mibBuilder.loadTexts: cgprsL2rlyInterfaceId.setStatus('current')
if mibBuilder.loadTexts: cgprsL2rlyInterfaceId.setDescription(' The ifIndex for the corresponding interface which l2rly is using. ')
cgprsL2rlyInterfaceRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 9993, 1, 1, 8, 1, 2), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: cgprsL2rlyInterfaceRowStatus.setStatus('current')
if mibBuilder.loadTexts: cgprsL2rlyInterfaceRowStatus.setDescription(' The status for row creation and deletion. ')
cgprsL2rlyFlowControlTriggerCount = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 9993, 1, 2, 1), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cgprsL2rlyFlowControlTriggerCount.setStatus('current')
if mibBuilder.loadTexts: cgprsL2rlyFlowControlTriggerCount.setDescription('A running count indicating how many times L2 Relay flow control has been trigerred. ')
cgprsL2rlyInputQLen = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 9993, 1, 2, 2), Counter32()).setUnits('packets').setMaxAccess("readonly")
if mibBuilder.loadTexts: cgprsL2rlyInputQLen.setStatus('current')
if mibBuilder.loadTexts: cgprsL2rlyInputQLen.setDescription('The L2 Relay input queue length. ')
cgprsL2rlyTotalPacketsDropped = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 9993, 1, 2, 3), Counter32()).setUnits('packets').setMaxAccess("readonly")
if mibBuilder.loadTexts: cgprsL2rlyTotalPacketsDropped.setStatus('current')
if mibBuilder.loadTexts: cgprsL2rlyTotalPacketsDropped.setDescription('Total number of packets dropped by L2 Relay due to unknown headers since system startup. ')
cgprsL2rlyDroppedPktsTimeFrame = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 9993, 1, 2, 4), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 65535))).setUnits('seconds').setMaxAccess("readonly")
if mibBuilder.loadTexts: cgprsL2rlyDroppedPktsTimeFrame.setStatus('current')
if mibBuilder.loadTexts: cgprsL2rlyDroppedPktsTimeFrame.setDescription('The time frame within which the number of L2 Relay packets, defined by cgprsL2rlyDroppedPktsCount, are dropped. ')
cgprsL2rlyDroppedPktsCount = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 9993, 1, 2, 5), Counter32()).setUnits('packets').setMaxAccess("readonly")
if mibBuilder.loadTexts: cgprsL2rlyDroppedPktsCount.setStatus('current')
if mibBuilder.loadTexts: cgprsL2rlyDroppedPktsCount.setDescription('The number of packets dropped by L2 Relay on the SGSN within cgprsL2rlyDroppedPktsTimeFrame. ')
cgprsL2rlyPeerTable = MibTable((1, 3, 6, 1, 4, 1, 9, 9, 9993, 1, 2, 6), )
if mibBuilder.loadTexts: cgprsL2rlyPeerTable.setStatus('current')
if mibBuilder.loadTexts: cgprsL2rlyPeerTable.setDescription(' The table lists all the l2rly units on the peer nodes that directly connect with this l2rly units through two fast ethernets. ')
cgprsL2rlyPeerEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9, 9, 9993, 1, 2, 6, 1), ).setIndexNames((0, "CISCO-GPRS-L2RLY-MIB", "cgprsL2rlyPeerUid"), (0, "CISCO-GPRS-L2RLY-MIB", "cgprsL2rlyInterfaceId"))
if mibBuilder.loadTexts: cgprsL2rlyPeerEntry.setStatus('current')
if mibBuilder.loadTexts: cgprsL2rlyPeerEntry.setDescription(' L2rly unit peer entries. ')
cgprsL2rlyPeerUid = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 9993, 1, 2, 6, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 64)))
if mibBuilder.loadTexts: cgprsL2rlyPeerUid.setStatus('current')
if mibBuilder.loadTexts: cgprsL2rlyPeerUid.setDescription(' The Uid that uniquely identify the peer l2rly unit that connects to the same fast ethernets as this l2rly unit. ')
cgprsL2rlyPeerUnitType = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 9993, 1, 2, 6, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("datacomUnit", 1), ("telecomUnit", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: cgprsL2rlyPeerUnitType.setStatus('current')
if mibBuilder.loadTexts: cgprsL2rlyPeerUnitType.setDescription(' The type of the peer l2rly on other devices which connects to the same fast ethernets as this one. ')
ciscoGprsL2rlyNotificationPrefix = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 9993, 2))
ciscoGprsL2rlyNotifications = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 9993, 2, 0))
cgprsL2rlyUnitJoinNotification = NotificationType((1, 3, 6, 1, 4, 1, 9, 9, 9993, 2, 0, 1)).setObjects(("CISCO-GPRS-L2RLY-MIB", "cgprsL2rlyUid"))
if mibBuilder.loadTexts: cgprsL2rlyUnitJoinNotification.setStatus('current')
if mibBuilder.loadTexts: cgprsL2rlyUnitJoinNotification.setDescription("This trap indicates that a new 'SGSN T-node' joins the service. This happens when a new SGSN node restarts or the network problem (fast ethernets among the units) recovers. ")
cgprsL2rlyNoRespToKeepAliveMsgNotification = NotificationType((1, 3, 6, 1, 4, 1, 9, 9, 9993, 2, 0, 2)).setObjects(("CISCO-GPRS-L2RLY-MIB", "cgprsL2rlyUid"))
if mibBuilder.loadTexts: cgprsL2rlyNoRespToKeepAliveMsgNotification.setStatus('current')
if mibBuilder.loadTexts: cgprsL2rlyNoRespToKeepAliveMsgNotification.setDescription("This trap indicates that the 'SGSN T-node' failed to respond to the L2 Relay 'Keep Alive' message. The cgprsL2rlyUid variable identifies the 'SGSN T-node' that failed to respond. ")
ciscoGprsL2rlyConformances = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 9993, 3))
cgprsL2rlyCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 9993, 3, 1))
cgprsL2rlyGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 9993, 3, 2))
cgprsL2rlyCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 9, 9, 9993, 3, 1, 1)).setObjects(("CISCO-GPRS-L2RLY-MIB", "cgprsL2rlyConfigGroup"), ("CISCO-GPRS-L2RLY-MIB", "cgprsL2rlyStatsGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cgprsL2rlyCompliance = cgprsL2rlyCompliance.setStatus('current')
if mibBuilder.loadTexts: cgprsL2rlyCompliance.setDescription(' The compliance statement for entities which implement the CISCO GPRS L2RLY MIB. ')
cgprsL2rlyConfigGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 9993, 3, 2, 1)).setObjects(("CISCO-GPRS-L2RLY-MIB", "cgprsL2rlyUid"), ("CISCO-GPRS-L2RLY-MIB", "cgprsL2rlyUnitType"), ("CISCO-GPRS-L2RLY-MIB", "cgprsL2rlyEchoTimer"), ("CISCO-GPRS-L2RLY-MIB", "cgprsL2rlyFlowControlFlag"), ("CISCO-GPRS-L2RLY-MIB", "cgprsL2rlyDroppedPktsMonTime"), ("CISCO-GPRS-L2RLY-MIB", "cgprsL2rlyNoRespToKeepAliveMsgNotificationEnable"), ("CISCO-GPRS-L2RLY-MIB", "cgprsL2rlyUnitJoinNotificationEnable"), ("CISCO-GPRS-L2RLY-MIB", "cgprsL2rlyInterfaceRowStatus"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cgprsL2rlyConfigGroup = cgprsL2rlyConfigGroup.setStatus('current')
if mibBuilder.loadTexts: cgprsL2rlyConfigGroup.setDescription(' A collection of configurable parameters for L2RLY. ')
cgprsL2rlyStatsGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 9993, 3, 2, 2)).setObjects(("CISCO-GPRS-L2RLY-MIB", "cgprsL2rlyFlowControlTriggerCount"), ("CISCO-GPRS-L2RLY-MIB", "cgprsL2rlyInputQLen"), ("CISCO-GPRS-L2RLY-MIB", "cgprsL2rlyTotalPacketsDropped"), ("CISCO-GPRS-L2RLY-MIB", "cgprsL2rlyDroppedPktsTimeFrame"), ("CISCO-GPRS-L2RLY-MIB", "cgprsL2rlyDroppedPktsCount"), ("CISCO-GPRS-L2RLY-MIB", "cgprsL2rlyPeerUnitType"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cgprsL2rlyStatsGroup = cgprsL2rlyStatsGroup.setStatus('current')
if mibBuilder.loadTexts: cgprsL2rlyStatsGroup.setDescription(' A collection of stats for L2RLY.')
mibBuilder.exportSymbols("CISCO-GPRS-L2RLY-MIB", cgprsL2rlyInputQLen=cgprsL2rlyInputQLen, ciscoGprsL2rlyNotifications=ciscoGprsL2rlyNotifications, cgprsL2rlyPeerTable=cgprsL2rlyPeerTable, ciscoGprsL2rlyStats=ciscoGprsL2rlyStats, cgprsL2rlyNoRespToKeepAliveMsgNotificationEnable=cgprsL2rlyNoRespToKeepAliveMsgNotificationEnable, ciscoGprsL2rlyMIB=ciscoGprsL2rlyMIB, cgprsL2rlyCompliance=cgprsL2rlyCompliance, cgprsL2rlyCompliances=cgprsL2rlyCompliances, cgprsL2rlyUnitJoinNotification=cgprsL2rlyUnitJoinNotification, cgprsL2rlyInterfaceId=cgprsL2rlyInterfaceId, cgprsL2rlyPeerEntry=cgprsL2rlyPeerEntry, cgprsL2rlyDroppedPktsCount=cgprsL2rlyDroppedPktsCount, ciscoGprsL2rlyConformances=ciscoGprsL2rlyConformances, cgprsL2rlyStatsGroup=cgprsL2rlyStatsGroup, cgprsL2rlyPeerUid=cgprsL2rlyPeerUid, cgprsL2rlyInterfaceRowStatus=cgprsL2rlyInterfaceRowStatus, cgprsL2rlyInterfaceEntry=cgprsL2rlyInterfaceEntry, cgprsL2rlyInterfaceTable=cgprsL2rlyInterfaceTable, ciscoGprsL2rlyObjects=ciscoGprsL2rlyObjects, cgprsL2rlyTotalPacketsDropped=cgprsL2rlyTotalPacketsDropped, cgprsL2rlyDroppedPktsMonTime=cgprsL2rlyDroppedPktsMonTime, cgprsL2rlyDroppedPktsTimeFrame=cgprsL2rlyDroppedPktsTimeFrame, cgprsL2rlyFlowControlTriggerCount=cgprsL2rlyFlowControlTriggerCount, cgprsL2rlyConfigGroup=cgprsL2rlyConfigGroup, cgprsL2rlyUnitJoinNotificationEnable=cgprsL2rlyUnitJoinNotificationEnable, cgprsL2rlyPeerUnitType=cgprsL2rlyPeerUnitType, cgprsL2rlyUnitType=cgprsL2rlyUnitType, cgprsL2rlyUid=cgprsL2rlyUid, ciscoGprsL2rlyConfig=ciscoGprsL2rlyConfig, cgprsL2rlyGroups=cgprsL2rlyGroups, cgprsL2rlyEchoTimer=cgprsL2rlyEchoTimer, cgprsL2rlyNoRespToKeepAliveMsgNotification=cgprsL2rlyNoRespToKeepAliveMsgNotification, cgprsL2rlyFlowControlFlag=cgprsL2rlyFlowControlFlag, PYSNMP_MODULE_ID=ciscoGprsL2rlyMIB, ciscoGprsL2rlyNotificationPrefix=ciscoGprsL2rlyNotificationPrefix)