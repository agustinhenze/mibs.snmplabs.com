#
# PySNMP MIB module ASCEND-ADVANCED-AGENT-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/ASCEND-ADVANCED-AGENT-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 17:10:00 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
advancedAgent, DisplayString = mibBuilder.importSymbols("ASCEND-MIB", "advancedAgent", "DisplayString")
ObjectIdentifier, Integer, OctetString = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "Integer", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsUnion, ValueRangeConstraint, SingleValueConstraint, ValueSizeConstraint, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "ValueRangeConstraint", "SingleValueConstraint", "ValueSizeConstraint", "ConstraintsIntersection")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
Bits, NotificationType, Counter64, ObjectIdentity, ModuleIdentity, TimeTicks, Counter32, IpAddress, Unsigned32, MibIdentifier, iso, Integer32, MibScalar, MibTable, MibTableRow, MibTableColumn, Gauge32 = mibBuilder.importSymbols("SNMPv2-SMI", "Bits", "NotificationType", "Counter64", "ObjectIdentity", "ModuleIdentity", "TimeTicks", "Counter32", "IpAddress", "Unsigned32", "MibIdentifier", "iso", "Integer32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Gauge32")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
wanUseTrunkGroups = MibScalar((1, 3, 6, 1, 4, 1, 529, 4, 20), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("do-not-use", 1), ("use", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: wanUseTrunkGroups.setStatus('mandatory')
wanLineTable = MibTable((1, 3, 6, 1, 4, 1, 529, 4, 21), )
if mibBuilder.loadTexts: wanLineTable.setStatus('mandatory')
wanLineEntry = MibTableRow((1, 3, 6, 1, 4, 1, 529, 4, 21, 1), ).setIndexNames((0, "ASCEND-ADVANCED-AGENT-MIB", "wanLineIfIndex"))
if mibBuilder.loadTexts: wanLineEntry.setStatus('mandatory')
wanLineIfIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 529, 4, 21, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: wanLineIfIndex.setStatus('mandatory')
wanLineName = MibTableColumn((1, 3, 6, 1, 4, 1, 529, 4, 21, 1, 2), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: wanLineName.setStatus('mandatory')
wanLineType = MibTableColumn((1, 3, 6, 1, 4, 1, 529, 4, 21, 1, 3), ObjectIdentifier()).setMaxAccess("readonly")
if mibBuilder.loadTexts: wanLineType.setStatus('mandatory')
wanLineChannels = MibTableColumn((1, 3, 6, 1, 4, 1, 529, 4, 21, 1, 4), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: wanLineChannels.setStatus('mandatory')
wanLineState = MibTableColumn((1, 3, 6, 1, 4, 1, 529, 4, 21, 1, 5), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14))).clone(namedValues=NamedValues(("ls-unknown", 1), ("ls-does-not-exist", 2), ("ls-disabled", 3), ("ls-no-physical", 4), ("ls-no-logical", 5), ("ls-point-to-point", 6), ("ls-multipoint-1", 7), ("ls-multipoint-2", 8), ("ls-loss-of-sync", 9), ("ls-yellow-alarm", 10), ("ls-ais-receive", 11), ("ls-no-d-channel", 12), ("ls-active", 13), ("ls-maintenance", 14)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: wanLineState.setStatus('mandatory')
wanLineStateString = MibTableColumn((1, 3, 6, 1, 4, 1, 529, 4, 21, 1, 6), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: wanLineStateString.setStatus('mandatory')
wanLineActiveChannels = MibTableColumn((1, 3, 6, 1, 4, 1, 529, 4, 21, 1, 7), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: wanLineActiveChannels.setStatus('mandatory')
wanLineUsage = MibTableColumn((1, 3, 6, 1, 4, 1, 529, 4, 21, 1, 8), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 8, 9))).clone(namedValues=NamedValues(("lu-unknown", 1), ("lu-unavailable", 2), ("lu-disabled", 3), ("lu-enabled", 4), ("lu-trunk", 5), ("lu-quiesced", 6), ("lu-drop-and-insert", 7), ("lu-t-online-user", 8), ("lu-t-online-zgr", 9)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: wanLineUsage.setStatus('mandatory')
wanLineHuntGrpPhoneNumber1 = MibTableColumn((1, 3, 6, 1, 4, 1, 529, 4, 21, 1, 9), DisplayString()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: wanLineHuntGrpPhoneNumber1.setStatus('mandatory')
wanLineHuntGrpPhoneNumber2 = MibTableColumn((1, 3, 6, 1, 4, 1, 529, 4, 21, 1, 10), DisplayString()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: wanLineHuntGrpPhoneNumber2.setStatus('mandatory')
wanLineHuntGrpPhoneNumber3 = MibTableColumn((1, 3, 6, 1, 4, 1, 529, 4, 21, 1, 11), DisplayString()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: wanLineHuntGrpPhoneNumber3.setStatus('mandatory')
wanLineAvailableChannels = MibTableColumn((1, 3, 6, 1, 4, 1, 529, 4, 21, 1, 12), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: wanLineAvailableChannels.setStatus('mandatory')
wanLineSwitchedChannels = MibTableColumn((1, 3, 6, 1, 4, 1, 529, 4, 21, 1, 13), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: wanLineSwitchedChannels.setStatus('mandatory')
wanLineDisabledChannels = MibTableColumn((1, 3, 6, 1, 4, 1, 529, 4, 21, 1, 14), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: wanLineDisabledChannels.setStatus('mandatory')
wanLineNailedChannels = MibTableColumn((1, 3, 6, 1, 4, 1, 529, 4, 21, 1, 15), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: wanLineNailedChannels.setStatus('mandatory')
wanLineOutOfServiceChannels = MibTableColumn((1, 3, 6, 1, 4, 1, 529, 4, 21, 1, 16), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: wanLineOutOfServiceChannels.setStatus('mandatory')
wanLineNet2NetChannels = MibTableColumn((1, 3, 6, 1, 4, 1, 529, 4, 21, 1, 17), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: wanLineNet2NetChannels.setStatus('mandatory')
wanLineDtptChannels = MibTableColumn((1, 3, 6, 1, 4, 1, 529, 4, 21, 1, 18), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: wanLineDtptChannels.setStatus('mandatory')
wanLineChannelTable = MibTable((1, 3, 6, 1, 4, 1, 529, 4, 22), )
if mibBuilder.loadTexts: wanLineChannelTable.setStatus('mandatory')
wanLineChannelEntry = MibTableRow((1, 3, 6, 1, 4, 1, 529, 4, 22, 1), ).setIndexNames((0, "ASCEND-ADVANCED-AGENT-MIB", "wanLineChannelIfIndex"), (0, "ASCEND-ADVANCED-AGENT-MIB", "wanLineChannelIndex"))
if mibBuilder.loadTexts: wanLineChannelEntry.setStatus('mandatory')
wanLineChannelIfIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 529, 4, 22, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: wanLineChannelIfIndex.setStatus('mandatory')
wanLineChannelIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 529, 4, 22, 1, 2), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: wanLineChannelIndex.setStatus('mandatory')
wanLineChannelState = MibTableColumn((1, 3, 6, 1, 4, 1, 529, 4, 22, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24))).clone(namedValues=NamedValues(("bs-unknown", 1), ("bs-unavailable", 2), ("bs-unused", 3), ("bs-out-of-service", 4), ("bs-nailed-up", 5), ("bs-held", 6), ("bs-idle", 7), ("bs-clear-pending", 8), ("bs-dialing", 9), ("bs-ringing", 10), ("bs-connected", 11), ("bs-signaling", 12), ("bs-cut-through", 13), ("bs-current-d", 14), ("bs-backup-d", 15), ("bs-maintenance", 16), ("bs-spc-up", 17), ("bs-disabled", 18), ("bs-dialing-net2net", 19), ("bs-ringing-net2net", 20), ("bs-connected-net2net", 21), ("bs-dialing-dtpt", 22), ("bs-ringing-dtpt", 23), ("bs-connected-dtpt", 24)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: wanLineChannelState.setStatus('mandatory')
wanLineChannelStateString = MibTableColumn((1, 3, 6, 1, 4, 1, 529, 4, 22, 1, 4), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: wanLineChannelStateString.setStatus('mandatory')
wanLineChannelErrorCount = MibTableColumn((1, 3, 6, 1, 4, 1, 529, 4, 22, 1, 5), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: wanLineChannelErrorCount.setStatus('mandatory')
wanLineChannelUsage = MibTableColumn((1, 3, 6, 1, 4, 1, 529, 4, 22, 1, 6), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 8, 9, 10))).clone(namedValues=NamedValues(("ds0-unknown-channel", 1), ("ds0-unused-channel", 2), ("ds0-switched-channel", 3), ("ds0-cut-through", 4), ("ds0-clear-64", 5), ("ds0-pri-d-channel", 6), ("ds0-nfas-prime-d", 7), ("ds0-nfas-sec-d", 8), ("ds0-cas-channel", 9), ("ds0-spc-channel", 10)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: wanLineChannelUsage.setStatus('mandatory')
wanLineChannelTrunkGroup = MibTableColumn((1, 3, 6, 1, 4, 1, 529, 4, 22, 1, 7), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: wanLineChannelTrunkGroup.setStatus('mandatory')
wanLineChannelPhoneNumber = MibTableColumn((1, 3, 6, 1, 4, 1, 529, 4, 22, 1, 8), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: wanLineChannelPhoneNumber.setStatus('mandatory')
wanLineChannelSlot = MibTableColumn((1, 3, 6, 1, 4, 1, 529, 4, 22, 1, 9), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: wanLineChannelSlot.setStatus('mandatory')
wanLineChannelPort = MibTableColumn((1, 3, 6, 1, 4, 1, 529, 4, 22, 1, 10), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: wanLineChannelPort.setStatus('mandatory')
wanLineChannelNailedState = MibTableColumn((1, 3, 6, 1, 4, 1, 529, 4, 22, 1, 11), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("not-applicable", 1), ("nailed-held", 2), ("nailed-active", 3)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: wanLineChannelNailedState.setStatus('mandatory')
wanAvailableChannels = MibScalar((1, 3, 6, 1, 4, 1, 529, 4, 23), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: wanAvailableChannels.setStatus('mandatory')
wanSwitchedChannels = MibScalar((1, 3, 6, 1, 4, 1, 529, 4, 24), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: wanSwitchedChannels.setStatus('mandatory')
wanDisabledChannels = MibScalar((1, 3, 6, 1, 4, 1, 529, 4, 25), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: wanDisabledChannels.setStatus('mandatory')
wanActiveChannels = MibScalar((1, 3, 6, 1, 4, 1, 529, 4, 26), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: wanActiveChannels.setStatus('mandatory')
wanNailedChannels = MibScalar((1, 3, 6, 1, 4, 1, 529, 4, 27), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: wanNailedChannels.setStatus('mandatory')
wanOutOfServiceChannels = MibScalar((1, 3, 6, 1, 4, 1, 529, 4, 28), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: wanOutOfServiceChannels.setStatus('mandatory')
wanLineChannelUsageTable = MibTable((1, 3, 6, 1, 4, 1, 529, 4, 29), )
if mibBuilder.loadTexts: wanLineChannelUsageTable.setStatus('mandatory')
wanLineChannelUsageEntry = MibTableRow((1, 3, 6, 1, 4, 1, 529, 4, 29, 1), ).setIndexNames((0, "ASCEND-ADVANCED-AGENT-MIB", "wanLineUsage"), (0, "ASCEND-ADVANCED-AGENT-MIB", "wanLineChannelState"))
if mibBuilder.loadTexts: wanLineChannelUsageEntry.setStatus('mandatory')
wanLineChannelUsageCount = MibTableColumn((1, 3, 6, 1, 4, 1, 529, 4, 29, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: wanLineChannelUsageCount.setStatus('mandatory')
mibBuilder.exportSymbols("ASCEND-ADVANCED-AGENT-MIB", wanLineAvailableChannels=wanLineAvailableChannels, wanLineChannelErrorCount=wanLineChannelErrorCount, wanLineChannelEntry=wanLineChannelEntry, wanLineActiveChannels=wanLineActiveChannels, wanLineChannelTrunkGroup=wanLineChannelTrunkGroup, wanActiveChannels=wanActiveChannels, wanLineChannelSlot=wanLineChannelSlot, wanLineEntry=wanLineEntry, wanNailedChannels=wanNailedChannels, wanLineDisabledChannels=wanLineDisabledChannels, wanLineHuntGrpPhoneNumber1=wanLineHuntGrpPhoneNumber1, wanLineHuntGrpPhoneNumber2=wanLineHuntGrpPhoneNumber2, wanLineChannelPort=wanLineChannelPort, wanLineType=wanLineType, wanLineIfIndex=wanLineIfIndex, wanLineState=wanLineState, wanLineUsage=wanLineUsage, wanAvailableChannels=wanAvailableChannels, wanUseTrunkGroups=wanUseTrunkGroups, wanLineChannelIndex=wanLineChannelIndex, wanSwitchedChannels=wanSwitchedChannels, wanLineChannelTable=wanLineChannelTable, wanLineChannelIfIndex=wanLineChannelIfIndex, wanLineChannelUsageEntry=wanLineChannelUsageEntry, wanLineChannelUsageTable=wanLineChannelUsageTable, wanLineChannelUsageCount=wanLineChannelUsageCount, wanLineNailedChannels=wanLineNailedChannels, wanLineSwitchedChannels=wanLineSwitchedChannels, wanLineNet2NetChannels=wanLineNet2NetChannels, wanLineName=wanLineName, wanLineChannelUsage=wanLineChannelUsage, wanLineDtptChannels=wanLineDtptChannels, wanLineChannelNailedState=wanLineChannelNailedState, wanLineStateString=wanLineStateString, wanLineHuntGrpPhoneNumber3=wanLineHuntGrpPhoneNumber3, wanLineChannelState=wanLineChannelState, wanLineChannelStateString=wanLineChannelStateString, wanLineChannelPhoneNumber=wanLineChannelPhoneNumber, wanDisabledChannels=wanDisabledChannels, wanLineOutOfServiceChannels=wanLineOutOfServiceChannels, wanLineChannels=wanLineChannels, wanLineTable=wanLineTable, wanOutOfServiceChannels=wanOutOfServiceChannels)