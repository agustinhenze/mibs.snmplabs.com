#
# PySNMP MIB module SHIVA-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/SHIVA-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 20:54:45 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
OctetString, Integer, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "OctetString", "Integer", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
SingleValueConstraint, ConstraintsIntersection, ValueRangeConstraint, ConstraintsUnion, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "SingleValueConstraint", "ConstraintsIntersection", "ValueRangeConstraint", "ConstraintsUnion", "ValueSizeConstraint")
ifIndex, = mibBuilder.importSymbols("RFC1158-MIB", "ifIndex")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
TimeTicks, IpAddress, NotificationType, enterprises, NotificationType, Unsigned32, iso, Bits, ModuleIdentity, Integer32, Gauge32, Counter64, Counter32, MibScalar, MibTable, MibTableRow, MibTableColumn, MibIdentifier, ObjectIdentity = mibBuilder.importSymbols("SNMPv2-SMI", "TimeTicks", "IpAddress", "NotificationType", "enterprises", "NotificationType", "Unsigned32", "iso", "Bits", "ModuleIdentity", "Integer32", "Gauge32", "Counter64", "Counter32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "MibIdentifier", "ObjectIdentity")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
shiva = MibIdentifier((1, 3, 6, 1, 4, 1, 166))
sSystems = MibIdentifier((1, 3, 6, 1, 4, 1, 166, 1))
products = MibIdentifier((1, 3, 6, 1, 4, 1, 166, 2))
protocols = MibIdentifier((1, 3, 6, 1, 4, 1, 166, 3))
temporary = MibIdentifier((1, 3, 6, 1, 4, 1, 166, 4))
messageLog = MibIdentifier((1, 3, 6, 1, 4, 1, 166, 1, 1))
scc = MibIdentifier((1, 3, 6, 1, 4, 1, 166, 1, 2))
fastpath = MibIdentifier((1, 3, 6, 1, 4, 1, 166, 2, 1))
nmV32e = MibIdentifier((1, 3, 6, 1, 4, 1, 166, 2, 2))
fpBuffer = MibIdentifier((1, 3, 6, 1, 4, 1, 166, 2, 1, 1))
fpConf = MibIdentifier((1, 3, 6, 1, 4, 1, 166, 2, 1, 2))
k_star = MibIdentifier((1, 3, 6, 1, 4, 1, 166, 2, 1, 3)).setLabel("k-star")
tBap = MibIdentifier((1, 3, 6, 1, 4, 1, 166, 4, 1))
tATalk = MibIdentifier((1, 3, 6, 1, 4, 1, 166, 4, 2))
tIP = MibIdentifier((1, 3, 6, 1, 4, 1, 166, 4, 3))
tCommunity = MibIdentifier((1, 3, 6, 1, 4, 1, 166, 4, 4))
tEther = MibIdentifier((1, 3, 6, 1, 4, 1, 166, 4, 5))
mLogEntryCount = MibScalar((1, 3, 6, 1, 4, 1, 166, 1, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mLogEntryCount.setStatus('mandatory')
mLogNewMessageTrapEnable = MibScalar((1, 3, 6, 1, 4, 1, 166, 1, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 8, 9))).clone(namedValues=NamedValues(("disabled", 1), ("emerg", 2), ("alert", 3), ("crit", 4), ("err", 5), ("warning", 6), ("notice", 7), ("info", 8), ("debug", 9))).clone('disabled')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: mLogNewMessageTrapEnable.setStatus('mandatory')
mLogBuffer = MibTable((1, 3, 6, 1, 4, 1, 166, 1, 1, 3), )
if mibBuilder.loadTexts: mLogBuffer.setStatus('mandatory')
pysmiFakeCol1000 = MibTableColumn((1, 3, 6, 1, 4, 1, 166, 1, 1, 3, 1) + (1000, ), Integer32())
mLogMessage = MibTableRow((1, 3, 6, 1, 4, 1, 166, 1, 1, 3, 1), ).setIndexNames((0, "SHIVA-MIB", "pysmiFakeCol1000"))
if mibBuilder.loadTexts: mLogMessage.setStatus('mandatory')
mLogTimeStamp = MibTableColumn((1, 3, 6, 1, 4, 1, 166, 1, 1, 3, 1, 1), TimeTicks()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mLogTimeStamp.setStatus('mandatory')
mLogPriority = MibTableColumn((1, 3, 6, 1, 4, 1, 166, 1, 1, 3, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 8, 9))).clone(namedValues=NamedValues(("not-possible", 1), ("emerg", 2), ("alert", 3), ("crit", 4), ("err", 5), ("warning", 6), ("notice", 7), ("info", 8), ("debug", 9)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: mLogPriority.setStatus('mandatory')
mLogMessageText = MibTableColumn((1, 3, 6, 1, 4, 1, 166, 1, 1, 3, 1, 3), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mLogMessageText.setStatus('mandatory')
mLogTimeOfDay = MibTableColumn((1, 3, 6, 1, 4, 1, 166, 1, 1, 3, 1, 4), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mLogTimeOfDay.setStatus('mandatory')
sccTable = MibTable((1, 3, 6, 1, 4, 1, 166, 1, 2, 1), )
if mibBuilder.loadTexts: sccTable.setStatus('mandatory')
sccEntry = MibTableRow((1, 3, 6, 1, 4, 1, 166, 1, 2, 1, 1), ).setIndexNames((0, "RFC1158-MIB", "ifIndex"))
if mibBuilder.loadTexts: sccEntry.setStatus('mandatory')
sccInterrupts = MibTableColumn((1, 3, 6, 1, 4, 1, 166, 1, 2, 1, 1, 1), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sccInterrupts.setStatus('mandatory')
sccAborts = MibTableColumn((1, 3, 6, 1, 4, 1, 166, 1, 2, 1, 1, 2), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sccAborts.setStatus('mandatory')
sccSpuriousInts = MibTableColumn((1, 3, 6, 1, 4, 1, 166, 1, 2, 1, 1, 3), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sccSpuriousInts.setStatus('mandatory')
sccDeferTimeouts = MibTableColumn((1, 3, 6, 1, 4, 1, 166, 1, 2, 1, 1, 4), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sccDeferTimeouts.setStatus('mandatory')
sccOverruns = MibTableColumn((1, 3, 6, 1, 4, 1, 166, 1, 2, 1, 1, 5), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sccOverruns.setStatus('mandatory')
sccUnderruns = MibTableColumn((1, 3, 6, 1, 4, 1, 166, 1, 2, 1, 1, 6), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sccUnderruns.setStatus('mandatory')
bufferSize = MibScalar((1, 3, 6, 1, 4, 1, 166, 2, 1, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: bufferSize.setStatus('mandatory')
bufferAvail = MibScalar((1, 3, 6, 1, 4, 1, 166, 2, 1, 1, 2), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: bufferAvail.setStatus('mandatory')
bufferDrops = MibScalar((1, 3, 6, 1, 4, 1, 166, 2, 1, 1, 3), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: bufferDrops.setStatus('mandatory')
bufferTypeTable = MibTable((1, 3, 6, 1, 4, 1, 166, 2, 1, 1, 4), )
if mibBuilder.loadTexts: bufferTypeTable.setStatus('mandatory')
bufferTypeEntry = MibTableRow((1, 3, 6, 1, 4, 1, 166, 2, 1, 1, 4, 1), ).setIndexNames((0, "SHIVA-MIB", "bufferTypeIndex"))
if mibBuilder.loadTexts: bufferTypeEntry.setStatus('mandatory')
bufferTypeIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 166, 2, 1, 1, 4, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: bufferTypeIndex.setStatus('mandatory')
bufferTypeType = MibTableColumn((1, 3, 6, 1, 4, 1, 166, 2, 1, 1, 4, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 8, 9))).clone(namedValues=NamedValues(("other", 1), ("free", 2), ("localtalk", 3), ("ethernet", 4), ("arp", 5), ("data", 6), ("erbf", 7), ("etbf", 8), ("malloc", 9)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: bufferTypeType.setStatus('mandatory')
bufferTypeDescr = MibTableColumn((1, 3, 6, 1, 4, 1, 166, 2, 1, 1, 4, 1, 3), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: bufferTypeDescr.setStatus('mandatory')
bufferTypeCount = MibTableColumn((1, 3, 6, 1, 4, 1, 166, 2, 1, 1, 4, 1, 4), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: bufferTypeCount.setStatus('mandatory')
bufferTypeDrops = MibTableColumn((1, 3, 6, 1, 4, 1, 166, 2, 1, 1, 4, 1, 5), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: bufferTypeDrops.setStatus('mandatory')
bufferTypeRequests = MibTableColumn((1, 3, 6, 1, 4, 1, 166, 2, 1, 1, 4, 1, 6), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: bufferTypeRequests.setStatus('mandatory')
bufferTypeMaximum = MibTableColumn((1, 3, 6, 1, 4, 1, 166, 2, 1, 1, 4, 1, 7), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: bufferTypeMaximum.setStatus('mandatory')
confReboot = MibScalar((1, 3, 6, 1, 4, 1, 166, 2, 1, 2, 1), TimeTicks()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: confReboot.setStatus('mandatory')
confCheckSum = MibScalar((1, 3, 6, 1, 4, 1, 166, 2, 1, 2, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("valid", 1), ("invalid", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: confCheckSum.setStatus('mandatory')
codeCheckSum = MibScalar((1, 3, 6, 1, 4, 1, 166, 2, 1, 2, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("valid", 1), ("invalid", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: codeCheckSum.setStatus('mandatory')
promVersion = MibScalar((1, 3, 6, 1, 4, 1, 166, 2, 1, 2, 4), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: promVersion.setStatus('mandatory')
hwStatus = MibScalar((1, 3, 6, 1, 4, 1, 166, 2, 1, 2, 5), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hwStatus.setStatus('mandatory')
confWhyReboot = MibScalar((1, 3, 6, 1, 4, 1, 166, 2, 1, 2, 6), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5))).clone(namedValues=NamedValues(("other", 1), ("hardware", 2), ("firmware", 3), ("software", 4), ("config", 5)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: confWhyReboot.setStatus('mandatory')
confWhoReboot = MibScalar((1, 3, 6, 1, 4, 1, 166, 2, 1, 2, 7), DisplayString()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: confWhoReboot.setStatus('mandatory')
confRebootComment = MibScalar((1, 3, 6, 1, 4, 1, 166, 2, 1, 2, 8), DisplayString()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: confRebootComment.setStatus('mandatory')
confHowReboot = MibScalar((1, 3, 6, 1, 4, 1, 166, 2, 1, 2, 9), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5))).clone(namedValues=NamedValues(("restart", 1), ("go", 2), ("pause", 3), ("reset", 4), ("bootprom", 5)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: confHowReboot.setStatus('mandatory')
tRTMPEntryTimeouts = MibScalar((1, 3, 6, 1, 4, 1, 166, 4, 2, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: tRTMPEntryTimeouts.setStatus('mandatory')
tRTMPEntryDeletes = MibScalar((1, 3, 6, 1, 4, 1, 166, 4, 2, 2), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: tRTMPEntryDeletes.setStatus('mandatory')
tRTMPEntryEqualReplaces = MibScalar((1, 3, 6, 1, 4, 1, 166, 4, 2, 3), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: tRTMPEntryEqualReplaces.setStatus('mandatory')
tRTMPEntryBetterReplaces = MibScalar((1, 3, 6, 1, 4, 1, 166, 4, 2, 4), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: tRTMPEntryBetterReplaces.setStatus('mandatory')
tRTMPEntryAdds = MibScalar((1, 3, 6, 1, 4, 1, 166, 4, 2, 5), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: tRTMPEntryAdds.setStatus('mandatory')
tRTMPZeroCounters = MibScalar((1, 3, 6, 1, 4, 1, 166, 4, 2, 6), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1))).clone(namedValues=NamedValues(("zero", 1)))).setMaxAccess("writeonly")
if mibBuilder.loadTexts: tRTMPZeroCounters.setStatus('mandatory')
tZIPDeletes = MibScalar((1, 3, 6, 1, 4, 1, 166, 4, 2, 7), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: tZIPDeletes.setStatus('mandatory')
tZIPAdds = MibScalar((1, 3, 6, 1, 4, 1, 166, 4, 2, 8), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: tZIPAdds.setStatus('mandatory')
tZIPZeroCounters = MibScalar((1, 3, 6, 1, 4, 1, 166, 4, 2, 9), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1))).clone(namedValues=NamedValues(("zero", 1)))).setMaxAccess("writeonly")
if mibBuilder.loadTexts: tZIPZeroCounters.setStatus('mandatory')
tAARPClearCache = MibScalar((1, 3, 6, 1, 4, 1, 166, 4, 2, 10), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1))).clone(namedValues=NamedValues(("clear", 1)))).setMaxAccess("writeonly")
if mibBuilder.loadTexts: tAARPClearCache.setStatus('mandatory')
tKIPRoutesValid = MibScalar((1, 3, 6, 1, 4, 1, 166, 4, 2, 11), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("valid", 1), ("invalid", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: tKIPRoutesValid.setStatus('mandatory')
tARPClearCache = MibScalar((1, 3, 6, 1, 4, 1, 166, 4, 3, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1))).clone(namedValues=NamedValues(("clear", 1)))).setMaxAccess("writeonly")
if mibBuilder.loadTexts: tARPClearCache.setStatus('mandatory')
tIPClearRoutingTable = MibScalar((1, 3, 6, 1, 4, 1, 166, 4, 3, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1))).clone(namedValues=NamedValues(("clear", 1)))).setMaxAccess("writeonly")
if mibBuilder.loadTexts: tIPClearRoutingTable.setStatus('mandatory')
tCommunityTrapHostType = MibScalar((1, 3, 6, 1, 4, 1, 166, 4, 4, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("unconfigured", 1), ("ip", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: tCommunityTrapHostType.setStatus('mandatory')
tCommunityTrapHostAddress = MibScalar((1, 3, 6, 1, 4, 1, 166, 4, 4, 2), OctetString()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: tCommunityTrapHostAddress.setStatus('mandatory')
tCommunitySetHostType = MibScalar((1, 3, 6, 1, 4, 1, 166, 4, 4, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("unconfigured", 1), ("ip", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: tCommunitySetHostType.setStatus('mandatory')
tCommunitySetHostAddress = MibScalar((1, 3, 6, 1, 4, 1, 166, 4, 4, 4), OctetString()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: tCommunitySetHostAddress.setStatus('mandatory')
tCommunityList = MibTable((1, 3, 6, 1, 4, 1, 166, 4, 4, 5), )
if mibBuilder.loadTexts: tCommunityList.setStatus('mandatory')
pysmiFakeCol1001 = MibTableColumn((1, 3, 6, 1, 4, 1, 166, 4, 4, 5, 1) + (1001, ), Integer32())
tCommunityEntry = MibTableRow((1, 3, 6, 1, 4, 1, 166, 4, 4, 5, 1), ).setIndexNames((0, "SHIVA-MIB", "pysmiFakeCol1001"))
if mibBuilder.loadTexts: tCommunityEntry.setStatus('mandatory')
tCommunityName = MibTableColumn((1, 3, 6, 1, 4, 1, 166, 4, 4, 5, 1, 1), DisplayString()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: tCommunityName.setStatus('mandatory')
tCommunityAccess = MibTableColumn((1, 3, 6, 1, 4, 1, 166, 4, 4, 5, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))).clone(namedValues=NamedValues(("no-access", 1), ("read-only-access", 2), ("clear-statistics", 3), ("configure", 4)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: tCommunityAccess.setStatus('mandatory')
tEtherTable = MibTable((1, 3, 6, 1, 4, 1, 166, 4, 5, 1), )
if mibBuilder.loadTexts: tEtherTable.setStatus('mandatory')
tEtherEntry = MibTableRow((1, 3, 6, 1, 4, 1, 166, 4, 5, 1, 1), ).setIndexNames((0, "RFC1158-MIB", "ifIndex"))
if mibBuilder.loadTexts: tEtherEntry.setStatus('mandatory')
etherCRCErrors = MibTableColumn((1, 3, 6, 1, 4, 1, 166, 4, 5, 1, 1, 1), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: etherCRCErrors.setStatus('mandatory')
etherAlignErrors = MibTableColumn((1, 3, 6, 1, 4, 1, 166, 4, 5, 1, 1, 2), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: etherAlignErrors.setStatus('mandatory')
etherResourceErrors = MibTableColumn((1, 3, 6, 1, 4, 1, 166, 4, 5, 1, 1, 3), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: etherResourceErrors.setStatus('mandatory')
etherOverrunErrors = MibTableColumn((1, 3, 6, 1, 4, 1, 166, 4, 5, 1, 1, 4), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: etherOverrunErrors.setStatus('mandatory')
etherInPackets = MibTableColumn((1, 3, 6, 1, 4, 1, 166, 4, 5, 1, 1, 5), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: etherInPackets.setStatus('mandatory')
etherOutPackets = MibTableColumn((1, 3, 6, 1, 4, 1, 166, 4, 5, 1, 1, 6), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: etherOutPackets.setStatus('mandatory')
etherBadTransmits = MibTableColumn((1, 3, 6, 1, 4, 1, 166, 4, 5, 1, 1, 7), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: etherBadTransmits.setStatus('mandatory')
etherOversizeFrames = MibTableColumn((1, 3, 6, 1, 4, 1, 166, 4, 5, 1, 1, 8), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: etherOversizeFrames.setStatus('mandatory')
etherSpurRUReadys = MibTableColumn((1, 3, 6, 1, 4, 1, 166, 4, 5, 1, 1, 9), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: etherSpurRUReadys.setStatus('mandatory')
etherSpurCUActives = MibTableColumn((1, 3, 6, 1, 4, 1, 166, 4, 5, 1, 1, 10), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: etherSpurCUActives.setStatus('mandatory')
etherSpurUnknowns = MibTableColumn((1, 3, 6, 1, 4, 1, 166, 4, 5, 1, 1, 11), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: etherSpurUnknowns.setStatus('mandatory')
etherBcastDrops = MibTableColumn((1, 3, 6, 1, 4, 1, 166, 4, 5, 1, 1, 12), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: etherBcastDrops.setStatus('mandatory')
etherReceiverRestarts = MibTableColumn((1, 3, 6, 1, 4, 1, 166, 4, 5, 1, 1, 13), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: etherReceiverRestarts.setStatus('mandatory')
etherReinterrupts = MibTableColumn((1, 3, 6, 1, 4, 1, 166, 4, 5, 1, 1, 14), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: etherReinterrupts.setStatus('mandatory')
etherBufferReroutes = MibTableColumn((1, 3, 6, 1, 4, 1, 166, 4, 5, 1, 1, 15), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: etherBufferReroutes.setStatus('mandatory')
etherBufferDrops = MibTableColumn((1, 3, 6, 1, 4, 1, 166, 4, 5, 1, 1, 16), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: etherBufferDrops.setStatus('mandatory')
etherCollisions = MibTableColumn((1, 3, 6, 1, 4, 1, 166, 4, 5, 1, 1, 17), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: etherCollisions.setStatus('mandatory')
etherDefers = MibTableColumn((1, 3, 6, 1, 4, 1, 166, 4, 5, 1, 1, 18), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: etherDefers.setStatus('mandatory')
etherDMAUnderruns = MibTableColumn((1, 3, 6, 1, 4, 1, 166, 4, 5, 1, 1, 19), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: etherDMAUnderruns.setStatus('mandatory')
etherMaxCollisions = MibTableColumn((1, 3, 6, 1, 4, 1, 166, 4, 5, 1, 1, 20), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: etherMaxCollisions.setStatus('mandatory')
etherNoCarriers = MibTableColumn((1, 3, 6, 1, 4, 1, 166, 4, 5, 1, 1, 21), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: etherNoCarriers.setStatus('mandatory')
etherNoCTSs = MibTableColumn((1, 3, 6, 1, 4, 1, 166, 4, 5, 1, 1, 22), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: etherNoCTSs.setStatus('mandatory')
etherNoSQEs = MibTableColumn((1, 3, 6, 1, 4, 1, 166, 4, 5, 1, 1, 23), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: etherNoSQEs.setStatus('mandatory')
mibBuilder.exportSymbols("SHIVA-MIB", tCommunityEntry=tCommunityEntry, bufferTypeMaximum=bufferTypeMaximum, sccAborts=sccAborts, bufferTypeCount=bufferTypeCount, fpBuffer=fpBuffer, bufferTypeTable=bufferTypeTable, etherOverrunErrors=etherOverrunErrors, etherBcastDrops=etherBcastDrops, bufferTypeEntry=bufferTypeEntry, mLogBuffer=mLogBuffer, mLogTimeOfDay=mLogTimeOfDay, temporary=temporary, pysmiFakeCol1000=pysmiFakeCol1000, mLogMessageText=mLogMessageText, sccTable=sccTable, sccSpuriousInts=sccSpuriousInts, sccEntry=sccEntry, etherDMAUnderruns=etherDMAUnderruns, tRTMPEntryDeletes=tRTMPEntryDeletes, etherSpurCUActives=etherSpurCUActives, tZIPZeroCounters=tZIPZeroCounters, etherOversizeFrames=etherOversizeFrames, confHowReboot=confHowReboot, bufferDrops=bufferDrops, bufferTypeIndex=bufferTypeIndex, nmV32e=nmV32e, codeCheckSum=codeCheckSum, etherDefers=etherDefers, confCheckSum=confCheckSum, etherBufferReroutes=etherBufferReroutes, tRTMPEntryAdds=tRTMPEntryAdds, bufferSize=bufferSize, tIP=tIP, scc=scc, sccOverruns=sccOverruns, tKIPRoutesValid=tKIPRoutesValid, shiva=shiva, bufferTypeRequests=bufferTypeRequests, mLogEntryCount=mLogEntryCount, etherInPackets=etherInPackets, tRTMPEntryTimeouts=tRTMPEntryTimeouts, mLogMessage=mLogMessage, etherNoSQEs=etherNoSQEs, tAARPClearCache=tAARPClearCache, bufferTypeDescr=bufferTypeDescr, etherBufferDrops=etherBufferDrops, etherAlignErrors=etherAlignErrors, tCommunityList=tCommunityList, hwStatus=hwStatus, tCommunityName=tCommunityName, tATalk=tATalk, bufferAvail=bufferAvail, etherSpurRUReadys=etherSpurRUReadys, products=products, tRTMPEntryBetterReplaces=tRTMPEntryBetterReplaces, etherNoCarriers=etherNoCarriers, tCommunitySetHostType=tCommunitySetHostType, tRTMPEntryEqualReplaces=tRTMPEntryEqualReplaces, etherNoCTSs=etherNoCTSs, mLogPriority=mLogPriority, tCommunity=tCommunity, tZIPDeletes=tZIPDeletes, tEtherEntry=tEtherEntry, etherOutPackets=etherOutPackets, fpConf=fpConf, tCommunitySetHostAddress=tCommunitySetHostAddress, confWhoReboot=confWhoReboot, sccUnderruns=sccUnderruns, pysmiFakeCol1001=pysmiFakeCol1001, etherBadTransmits=etherBadTransmits, promVersion=promVersion, tCommunityTrapHostType=tCommunityTrapHostType, mLogNewMessageTrapEnable=mLogNewMessageTrapEnable, tARPClearCache=tARPClearCache, tIPClearRoutingTable=tIPClearRoutingTable, tZIPAdds=tZIPAdds, tRTMPZeroCounters=tRTMPZeroCounters, etherReinterrupts=etherReinterrupts, protocols=protocols, bufferTypeDrops=bufferTypeDrops, etherMaxCollisions=etherMaxCollisions, tEtherTable=tEtherTable, etherCRCErrors=etherCRCErrors, tBap=tBap, mLogTimeStamp=mLogTimeStamp, etherResourceErrors=etherResourceErrors, tCommunityTrapHostAddress=tCommunityTrapHostAddress, confRebootComment=confRebootComment, tCommunityAccess=tCommunityAccess, tEther=tEther, confWhyReboot=confWhyReboot, sSystems=sSystems, etherReceiverRestarts=etherReceiverRestarts, messageLog=messageLog, fastpath=fastpath, bufferTypeType=bufferTypeType, etherCollisions=etherCollisions, sccDeferTimeouts=sccDeferTimeouts, etherSpurUnknowns=etherSpurUnknowns, k_star=k_star, sccInterrupts=sccInterrupts, confReboot=confReboot)