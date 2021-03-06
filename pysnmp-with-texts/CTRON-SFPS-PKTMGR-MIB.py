#
# PySNMP MIB module CTRON-SFPS-PKTMGR-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/CTRON-SFPS-PKTMGR-MIB
# Produced by pysmi-0.3.4 at Wed May  1 12:31:05 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
Integer, OctetString, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "Integer", "OctetString", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
SingleValueConstraint, ConstraintsIntersection, ValueSizeConstraint, ValueRangeConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "SingleValueConstraint", "ConstraintsIntersection", "ValueSizeConstraint", "ValueRangeConstraint", "ConstraintsUnion")
sfpsPktDispatchStats, sfpsCSPPacket, sfpsSwitchSfpsPacket = mibBuilder.importSymbols("CTRON-SFPS-INCLUDE-MIB", "sfpsPktDispatchStats", "sfpsCSPPacket", "sfpsSwitchSfpsPacket")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
MibIdentifier, Unsigned32, Counter64, Integer32, iso, ObjectIdentity, Bits, IpAddress, ModuleIdentity, NotificationType, Counter32, Gauge32, MibScalar, MibTable, MibTableRow, MibTableColumn, TimeTicks = mibBuilder.importSymbols("SNMPv2-SMI", "MibIdentifier", "Unsigned32", "Counter64", "Integer32", "iso", "ObjectIdentity", "Bits", "IpAddress", "ModuleIdentity", "NotificationType", "Counter32", "Gauge32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "TimeTicks")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
class SfpsSwitchInstance(Integer32):
    pass

class HexInteger(Integer32):
    pass

sfpsPacketMgrTable = MibTable((1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 1, 7, 1), )
if mibBuilder.loadTexts: sfpsPacketMgrTable.setStatus('mandatory')
if mibBuilder.loadTexts: sfpsPacketMgrTable.setDescription('This table keeps the statistics on all packets in the packetmanager')
sfpsPacketMgrEntry = MibTableRow((1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 1, 7, 1, 1), ).setIndexNames((0, "CTRON-SFPS-PKTMGR-MIB", "sfpsPacketMgrSwitchID"), (0, "CTRON-SFPS-PKTMGR-MIB", "sfpsPacketMgrPacketType"))
if mibBuilder.loadTexts: sfpsPacketMgrEntry.setStatus('mandatory')
if mibBuilder.loadTexts: sfpsPacketMgrEntry.setDescription('Each entry describes part of the packetmanager table')
sfpsPacketMgrSwitchID = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 1, 7, 1, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sfpsPacketMgrSwitchID.setStatus('mandatory')
if mibBuilder.loadTexts: sfpsPacketMgrSwitchID.setDescription('The switch instance of the switch')
sfpsPacketMgrPacketType = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 1, 7, 1, 1, 2), HexInteger()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sfpsPacketMgrPacketType.setStatus('mandatory')
if mibBuilder.loadTexts: sfpsPacketMgrPacketType.setDescription('The packet type')
sfpsPacketMgrTotalPackets = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 1, 7, 1, 1, 3), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sfpsPacketMgrTotalPackets.setStatus('mandatory')
if mibBuilder.loadTexts: sfpsPacketMgrTotalPackets.setDescription('The total number of packets created in the packetmanager')
sfpsPacketMgrPktsUsed = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 1, 7, 1, 1, 4), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sfpsPacketMgrPktsUsed.setStatus('mandatory')
if mibBuilder.loadTexts: sfpsPacketMgrPktsUsed.setDescription('The total number of pkts used since beginning of switch uptime')
sfpsPacketMgrPktsAvailable = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 1, 7, 1, 1, 5), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sfpsPacketMgrPktsAvailable.setStatus('mandatory')
if mibBuilder.loadTexts: sfpsPacketMgrPktsAvailable.setDescription('The number of packets left in the packetmanager')
sfpsPacketMgrPktsInUse = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 1, 7, 1, 1, 6), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sfpsPacketMgrPktsInUse.setStatus('mandatory')
if mibBuilder.loadTexts: sfpsPacketMgrPktsInUse.setDescription('The number of packets created minus the number of packets left')
sfpsPacketMgrNotFound = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 1, 7, 1, 1, 8), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sfpsPacketMgrNotFound.setStatus('mandatory')
if mibBuilder.loadTexts: sfpsPacketMgrNotFound.setDescription('The number of times a packet was requested and the packetmanager did not have a packet of its size or larger')
sfpsPacketMgrTooLarge = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 1, 7, 1, 1, 9), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sfpsPacketMgrTooLarge.setStatus('mandatory')
if mibBuilder.loadTexts: sfpsPacketMgrTooLarge.setDescription('')
sfpsPacketMgrToCreate = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 1, 7, 1, 1, 10), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: sfpsPacketMgrToCreate.setStatus('mandatory')
if mibBuilder.loadTexts: sfpsPacketMgrToCreate.setDescription('Changes the number of packets in the PacketManager')
sfpsPacketMgrReInit = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 1, 7, 1, 1, 11), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("other", 1), ("reinit", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: sfpsPacketMgrReInit.setStatus('mandatory')
if mibBuilder.loadTexts: sfpsPacketMgrReInit.setDescription('The lowest number of packets ever in the packetmanager')
sfpsPacketListTable = MibTable((1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 1, 7, 2), )
if mibBuilder.loadTexts: sfpsPacketListTable.setStatus('mandatory')
if mibBuilder.loadTexts: sfpsPacketListTable.setDescription('This table keeps the statistics on all packets in the packetmanager')
sfpsPacketListEntry = MibTableRow((1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 1, 7, 2, 1), ).setIndexNames((0, "CTRON-SFPS-PKTMGR-MIB", "sfpsPacketListPacketType"), (0, "CTRON-SFPS-PKTMGR-MIB", "sfpsPacketListSize"))
if mibBuilder.loadTexts: sfpsPacketListEntry.setStatus('mandatory')
if mibBuilder.loadTexts: sfpsPacketListEntry.setDescription('Each entry describes part of the packetmanager table')
sfpsPacketListPacketType = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 1, 7, 2, 1, 1), HexInteger()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sfpsPacketListPacketType.setStatus('mandatory')
if mibBuilder.loadTexts: sfpsPacketListPacketType.setDescription('The switch instance of the switch')
sfpsPacketListSize = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 1, 7, 2, 1, 2), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sfpsPacketListSize.setStatus('mandatory')
if mibBuilder.loadTexts: sfpsPacketListSize.setDescription('The size of the packets that are located in this particular sfpspacketlist')
sfpsPacketListTotalPackets = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 1, 7, 2, 1, 3), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sfpsPacketListTotalPackets.setStatus('mandatory')
if mibBuilder.loadTexts: sfpsPacketListTotalPackets.setDescription('The total number of packets created in the packetmanager')
sfpsPacketListPktsUsed = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 1, 7, 2, 1, 4), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sfpsPacketListPktsUsed.setStatus('mandatory')
if mibBuilder.loadTexts: sfpsPacketListPktsUsed.setDescription('The total number of pkts used since beginning of switch uptime')
sfpsPacketListPktsLeft = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 1, 7, 2, 1, 5), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sfpsPacketListPktsLeft.setStatus('mandatory')
if mibBuilder.loadTexts: sfpsPacketListPktsLeft.setDescription('The number of packets left in the packetmanager')
sfpsPacketListPktsInUse = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 1, 7, 2, 1, 6), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sfpsPacketListPktsInUse.setStatus('mandatory')
if mibBuilder.loadTexts: sfpsPacketListPktsInUse.setDescription('The number of packets created minus the number of packets left')
sfpsPacketListLowWater = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 1, 7, 2, 1, 7), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sfpsPacketListLowWater.setStatus('mandatory')
if mibBuilder.loadTexts: sfpsPacketListLowWater.setDescription('The lowest number of packets ever in the packetmanager')
sfpsPacketListNotFound = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 1, 7, 2, 1, 8), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sfpsPacketListNotFound.setStatus('mandatory')
if mibBuilder.loadTexts: sfpsPacketListNotFound.setDescription('The number of times a packet was requested and the packetmanager did not have a packet of its size or larger')
sfpsPacketListStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 1, 7, 2, 1, 9), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("other", 1), ("enabled", 2), ("disabled", 3)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: sfpsPacketListStatus.setStatus('mandatory')
if mibBuilder.loadTexts: sfpsPacketListStatus.setDescription('Sets the administrative state of the packet list for which the entry exists.')
sfpsPacketSizeTable = MibTable((1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 1, 7, 3), )
if mibBuilder.loadTexts: sfpsPacketSizeTable.setStatus('mandatory')
if mibBuilder.loadTexts: sfpsPacketSizeTable.setDescription('This table keeps the statistics on all packets in the packetmanager')
sfpsPacketSizeEntry = MibTableRow((1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 1, 7, 3, 1), ).setIndexNames((0, "CTRON-SFPS-PKTMGR-MIB", "sfpsPacketSizeSwitchInstance"), (0, "CTRON-SFPS-PKTMGR-MIB", "sfpsPacketSizeSize"))
if mibBuilder.loadTexts: sfpsPacketSizeEntry.setStatus('mandatory')
if mibBuilder.loadTexts: sfpsPacketSizeEntry.setDescription('Each entry describes part of the packetmanager table')
sfpsPacketSizeSwitchInstance = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 1, 7, 3, 1, 1), SfpsSwitchInstance()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sfpsPacketSizeSwitchInstance.setStatus('mandatory')
if mibBuilder.loadTexts: sfpsPacketSizeSwitchInstance.setDescription('The switch instance of the switch')
sfpsPacketSizeSize = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 1, 7, 3, 1, 2), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sfpsPacketSizeSize.setStatus('mandatory')
if mibBuilder.loadTexts: sfpsPacketSizeSize.setDescription('The size of the packets that are located in this particular sfpspacketSize')
sfpsPacketSizePktsUsed = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 1, 7, 3, 1, 3), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sfpsPacketSizePktsUsed.setStatus('mandatory')
if mibBuilder.loadTexts: sfpsPacketSizePktsUsed.setDescription('The total number of pkts used since beginning of switch uptime')
sfpsPacketSizeNotFound = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 1, 7, 3, 1, 4), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sfpsPacketSizeNotFound.setStatus('mandatory')
if mibBuilder.loadTexts: sfpsPacketSizeNotFound.setDescription('The number of times a packet was requested and the packetmanager did not have a packet of its size or Larger')
sfpsPacketQTable = MibTable((1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 1, 7, 4), )
if mibBuilder.loadTexts: sfpsPacketQTable.setStatus('mandatory')
if mibBuilder.loadTexts: sfpsPacketQTable.setDescription('')
sfpsPacketQEntry = MibTableRow((1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 1, 7, 4, 1), ).setIndexNames((0, "CTRON-SFPS-PKTMGR-MIB", "sfpsPacketQPriorityQ"))
if mibBuilder.loadTexts: sfpsPacketQEntry.setStatus('mandatory')
if mibBuilder.loadTexts: sfpsPacketQEntry.setDescription('')
sfpsPacketQPriorityQ = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 1, 7, 4, 1, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("low", 1), ("medium", 2), ("high", 3)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: sfpsPacketQPriorityQ.setStatus('mandatory')
if mibBuilder.loadTexts: sfpsPacketQPriorityQ.setDescription('')
sfpsPacketQTotalPackets = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 1, 7, 4, 1, 2), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sfpsPacketQTotalPackets.setStatus('mandatory')
if mibBuilder.loadTexts: sfpsPacketQTotalPackets.setDescription('')
sfpsPacketQCurrent = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 1, 7, 4, 1, 3), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sfpsPacketQCurrent.setStatus('mandatory')
if mibBuilder.loadTexts: sfpsPacketQCurrent.setDescription('')
sfpsPacketQHighWater = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 1, 7, 4, 1, 4), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sfpsPacketQHighWater.setStatus('mandatory')
if mibBuilder.loadTexts: sfpsPacketQHighWater.setDescription('')
sfpsCSPPacketStatsPacketsSentBad = MibScalar((1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 1, 10, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sfpsCSPPacketStatsPacketsSentBad.setStatus('mandatory')
if mibBuilder.loadTexts: sfpsCSPPacketStatsPacketsSentBad.setDescription('')
sfpsCSPPacketStatsPacketsSentGood = MibScalar((1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 1, 10, 2), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sfpsCSPPacketStatsPacketsSentGood.setStatus('mandatory')
if mibBuilder.loadTexts: sfpsCSPPacketStatsPacketsSentGood.setDescription('')
sfpsCSPPacketStatsPacketsReceivedBad = MibScalar((1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 1, 10, 3), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sfpsCSPPacketStatsPacketsReceivedBad.setStatus('mandatory')
if mibBuilder.loadTexts: sfpsCSPPacketStatsPacketsReceivedBad.setDescription('')
sfpsCSPPacketStatsPacketsReceivedGood = MibScalar((1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 1, 10, 4), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sfpsCSPPacketStatsPacketsReceivedGood.setStatus('mandatory')
if mibBuilder.loadTexts: sfpsCSPPacketStatsPacketsReceivedGood.setDescription('')
sfpsPktDispatchStatsVerb = MibScalar((1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 1, 7, 5, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("other", 1), ("resetAllStats", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: sfpsPktDispatchStatsVerb.setStatus('mandatory')
if mibBuilder.loadTexts: sfpsPktDispatchStatsVerb.setDescription('')
numHPMInvalidFrameTypeDrops = MibScalar((1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 1, 7, 5, 2), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: numHPMInvalidFrameTypeDrops.setStatus('mandatory')
if mibBuilder.loadTexts: numHPMInvalidFrameTypeDrops.setDescription('')
numHPMFilterMgtPortDrops = MibScalar((1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 1, 7, 5, 3), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: numHPMFilterMgtPortDrops.setStatus('mandatory')
if mibBuilder.loadTexts: numHPMFilterMgtPortDrops.setDescription('')
numHPMPhysToLogPortDrops = MibScalar((1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 1, 7, 5, 4), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: numHPMPhysToLogPortDrops.setStatus('mandatory')
if mibBuilder.loadTexts: numHPMPhysToLogPortDrops.setDescription('')
numHPMNullSFPSPktDrops = MibScalar((1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 1, 7, 5, 5), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: numHPMNullSFPSPktDrops.setStatus('mandatory')
if mibBuilder.loadTexts: numHPMNullSFPSPktDrops.setDescription('')
numHPM81fdThrottleDrops = MibScalar((1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 1, 7, 5, 6), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: numHPM81fdThrottleDrops.setStatus('mandatory')
if mibBuilder.loadTexts: numHPM81fdThrottleDrops.setDescription('')
numHPM81ffThrottleDrops = MibScalar((1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 1, 7, 5, 7), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: numHPM81ffThrottleDrops.setStatus('mandatory')
if mibBuilder.loadTexts: numHPM81ffThrottleDrops.setDescription('')
numHPMPhysStandbyMaskDrops = MibScalar((1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 1, 7, 5, 8), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: numHPMPhysStandbyMaskDrops.setStatus('mandatory')
if mibBuilder.loadTexts: numHPMPhysStandbyMaskDrops.setDescription('')
numBSInvSrcPortDrops = MibScalar((1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 1, 7, 5, 9), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: numBSInvSrcPortDrops.setStatus('mandatory')
if mibBuilder.loadTexts: numBSInvSrcPortDrops.setDescription('')
numBSSourceBlockDrops = MibScalar((1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 1, 7, 5, 10), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: numBSSourceBlockDrops.setStatus('mandatory')
if mibBuilder.loadTexts: numBSSourceBlockDrops.setDescription('')
numBSViolationDrops = MibScalar((1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 1, 7, 5, 11), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: numBSViolationDrops.setStatus('mandatory')
if mibBuilder.loadTexts: numBSViolationDrops.setDescription('')
numBSUnknownPortDrops = MibScalar((1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 1, 7, 5, 12), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: numBSUnknownPortDrops.setStatus('mandatory')
if mibBuilder.loadTexts: numBSUnknownPortDrops.setDescription('')
numBSStandbyPortDrops = MibScalar((1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 1, 7, 5, 13), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: numBSStandbyPortDrops.setStatus('mandatory')
if mibBuilder.loadTexts: numBSStandbyPortDrops.setDescription('')
numBSFabricNghbrPortDrops = MibScalar((1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 1, 7, 5, 14), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: numBSFabricNghbrPortDrops.setStatus('mandatory')
if mibBuilder.loadTexts: numBSFabricNghbrPortDrops.setDescription('')
numBSGoingToAccessPortDrops = MibScalar((1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 1, 7, 5, 15), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: numBSGoingToAccessPortDrops.setStatus('mandatory')
if mibBuilder.loadTexts: numBSGoingToAccessPortDrops.setDescription('')
numBSInvPortTypeDrops = MibScalar((1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 1, 7, 5, 16), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: numBSInvPortTypeDrops.setStatus('mandatory')
if mibBuilder.loadTexts: numBSInvPortTypeDrops.setDescription('')
numBSNullCallDrops = MibScalar((1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 1, 7, 5, 17), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: numBSNullCallDrops.setStatus('mandatory')
if mibBuilder.loadTexts: numBSNullCallDrops.setDescription('')
numBSNullBottomCPDrops = MibScalar((1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 1, 7, 5, 18), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: numBSNullBottomCPDrops.setStatus('mandatory')
if mibBuilder.loadTexts: numBSNullBottomCPDrops.setDescription('')
numBSInvCSPTypeDrops = MibScalar((1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 1, 7, 5, 19), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: numBSInvCSPTypeDrops.setStatus('mandatory')
if mibBuilder.loadTexts: numBSInvCSPTypeDrops.setDescription('')
numBSNonHello81fdDrops = MibScalar((1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 1, 7, 5, 20), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: numBSNonHello81fdDrops.setStatus('mandatory')
if mibBuilder.loadTexts: numBSNonHello81fdDrops.setDescription('')
numBSCSPCtrlDisableDrops = MibScalar((1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 1, 7, 5, 21), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: numBSCSPCtrlDisableDrops.setStatus('mandatory')
if mibBuilder.loadTexts: numBSCSPCtrlDisableDrops.setDescription('')
numBSCSPCtrlIndexDrops = MibScalar((1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 1, 7, 5, 22), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: numBSCSPCtrlIndexDrops.setStatus('mandatory')
if mibBuilder.loadTexts: numBSCSPCtrlIndexDrops.setDescription('')
numBCPNullCallDrops = MibScalar((1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 1, 7, 5, 23), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: numBCPNullCallDrops.setStatus('mandatory')
if mibBuilder.loadTexts: numBCPNullCallDrops.setDescription('')
numBCPCPFaultedDrops = MibScalar((1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 1, 7, 5, 24), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: numBCPCPFaultedDrops.setStatus('mandatory')
if mibBuilder.loadTexts: numBCPCPFaultedDrops.setDescription('')
numBCPGleanFailDrops = MibScalar((1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 1, 7, 5, 25), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: numBCPGleanFailDrops.setStatus('mandatory')
if mibBuilder.loadTexts: numBCPGleanFailDrops.setDescription('')
numBCPCPHaltedDrops = MibScalar((1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 1, 7, 5, 26), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: numBCPCPHaltedDrops.setStatus('mandatory')
if mibBuilder.loadTexts: numBCPCPHaltedDrops.setDescription('')
numBCPSwitchedBCADrops = MibScalar((1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 1, 7, 5, 27), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: numBCPSwitchedBCADrops.setStatus('mandatory')
if mibBuilder.loadTexts: numBCPSwitchedBCADrops.setDescription('')
numBCPCallNotAcceptedDrops = MibScalar((1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 1, 7, 5, 28), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: numBCPCallNotAcceptedDrops.setStatus('mandatory')
if mibBuilder.loadTexts: numBCPCallNotAcceptedDrops.setDescription('')
numHPM81fdNullPktDrops = MibScalar((1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 1, 7, 5, 29), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: numHPM81fdNullPktDrops.setStatus('mandatory')
if mibBuilder.loadTexts: numHPM81fdNullPktDrops.setDescription('')
numHPM81fdHelloNullPktDrops = MibScalar((1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 1, 7, 5, 30), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: numHPM81fdHelloNullPktDrops.setStatus('mandatory')
if mibBuilder.loadTexts: numHPM81fdHelloNullPktDrops.setDescription('')
mibBuilder.exportSymbols("CTRON-SFPS-PKTMGR-MIB", sfpsCSPPacketStatsPacketsReceivedGood=sfpsCSPPacketStatsPacketsReceivedGood, numBSViolationDrops=numBSViolationDrops, sfpsPacketMgrTable=sfpsPacketMgrTable, numBSNullCallDrops=numBSNullCallDrops, numHPM81fdThrottleDrops=numHPM81fdThrottleDrops, numBCPSwitchedBCADrops=numBCPSwitchedBCADrops, sfpsPacketMgrSwitchID=sfpsPacketMgrSwitchID, sfpsPacketMgrPktsAvailable=sfpsPacketMgrPktsAvailable, numBSUnknownPortDrops=numBSUnknownPortDrops, numHPM81fdNullPktDrops=numHPM81fdNullPktDrops, sfpsPacketSizePktsUsed=sfpsPacketSizePktsUsed, sfpsPacketQTable=sfpsPacketQTable, sfpsPacketQCurrent=sfpsPacketQCurrent, sfpsPacketMgrPktsUsed=sfpsPacketMgrPktsUsed, sfpsPacketListPktsInUse=sfpsPacketListPktsInUse, numBSGoingToAccessPortDrops=numBSGoingToAccessPortDrops, numHPMNullSFPSPktDrops=numHPMNullSFPSPktDrops, sfpsPacketMgrTotalPackets=sfpsPacketMgrTotalPackets, sfpsPacketSizeSwitchInstance=sfpsPacketSizeSwitchInstance, sfpsPacketSizeNotFound=sfpsPacketSizeNotFound, numBSInvPortTypeDrops=numBSInvPortTypeDrops, sfpsPacketListSize=sfpsPacketListSize, sfpsPacketListPktsLeft=sfpsPacketListPktsLeft, sfpsPacketSizeTable=sfpsPacketSizeTable, sfpsPacketQEntry=sfpsPacketQEntry, sfpsPacketListNotFound=sfpsPacketListNotFound, sfpsCSPPacketStatsPacketsSentBad=sfpsCSPPacketStatsPacketsSentBad, numBSCSPCtrlDisableDrops=numBSCSPCtrlDisableDrops, numBCPNullCallDrops=numBCPNullCallDrops, numBCPCallNotAcceptedDrops=numBCPCallNotAcceptedDrops, SfpsSwitchInstance=SfpsSwitchInstance, sfpsCSPPacketStatsPacketsSentGood=sfpsCSPPacketStatsPacketsSentGood, numBCPCPFaultedDrops=numBCPCPFaultedDrops, sfpsPacketSizeEntry=sfpsPacketSizeEntry, numHPMInvalidFrameTypeDrops=numHPMInvalidFrameTypeDrops, numBSCSPCtrlIndexDrops=numBSCSPCtrlIndexDrops, sfpsPacketMgrPktsInUse=sfpsPacketMgrPktsInUse, numHPM81fdHelloNullPktDrops=numHPM81fdHelloNullPktDrops, sfpsPacketListLowWater=sfpsPacketListLowWater, numBSSourceBlockDrops=numBSSourceBlockDrops, sfpsPacketListPacketType=sfpsPacketListPacketType, HexInteger=HexInteger, sfpsPacketListStatus=sfpsPacketListStatus, sfpsPacketMgrTooLarge=sfpsPacketMgrTooLarge, sfpsPktDispatchStatsVerb=sfpsPktDispatchStatsVerb, numHPMPhysStandbyMaskDrops=numHPMPhysStandbyMaskDrops, numBSNullBottomCPDrops=numBSNullBottomCPDrops, numBCPGleanFailDrops=numBCPGleanFailDrops, numHPMFilterMgtPortDrops=numHPMFilterMgtPortDrops, numHPMPhysToLogPortDrops=numHPMPhysToLogPortDrops, numBCPCPHaltedDrops=numBCPCPHaltedDrops, sfpsPacketSizeSize=sfpsPacketSizeSize, numBSStandbyPortDrops=numBSStandbyPortDrops, sfpsPacketQPriorityQ=sfpsPacketQPriorityQ, sfpsPacketListEntry=sfpsPacketListEntry, sfpsPacketMgrToCreate=sfpsPacketMgrToCreate, sfpsPacketMgrReInit=sfpsPacketMgrReInit, sfpsPacketQTotalPackets=sfpsPacketQTotalPackets, sfpsPacketListPktsUsed=sfpsPacketListPktsUsed, sfpsCSPPacketStatsPacketsReceivedBad=sfpsCSPPacketStatsPacketsReceivedBad, numBSFabricNghbrPortDrops=numBSFabricNghbrPortDrops, sfpsPacketListTotalPackets=sfpsPacketListTotalPackets, sfpsPacketMgrEntry=sfpsPacketMgrEntry, sfpsPacketMgrNotFound=sfpsPacketMgrNotFound, numBSNonHello81fdDrops=numBSNonHello81fdDrops, numBSInvCSPTypeDrops=numBSInvCSPTypeDrops, sfpsPacketQHighWater=sfpsPacketQHighWater, numBSInvSrcPortDrops=numBSInvSrcPortDrops, sfpsPacketListTable=sfpsPacketListTable, numHPM81ffThrottleDrops=numHPM81ffThrottleDrops, sfpsPacketMgrPacketType=sfpsPacketMgrPacketType)
