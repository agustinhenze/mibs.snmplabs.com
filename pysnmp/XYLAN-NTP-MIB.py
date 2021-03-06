#
# PySNMP MIB module XYLAN-NTP-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/XYLAN-NTP-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 21:38:46 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ConstraintsUnion, SingleValueConstraint, ValueSizeConstraint, ValueRangeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ConstraintsUnion", "SingleValueConstraint", "ValueSizeConstraint", "ValueRangeConstraint")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
Bits, iso, MibScalar, MibTable, MibTableRow, MibTableColumn, Integer32, TimeTicks, MibIdentifier, ObjectIdentity, Counter64, Gauge32, Counter32, Unsigned32, ModuleIdentity, IpAddress, NotificationType = mibBuilder.importSymbols("SNMPv2-SMI", "Bits", "iso", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Integer32", "TimeTicks", "MibIdentifier", "ObjectIdentity", "Counter64", "Gauge32", "Counter32", "Unsigned32", "ModuleIdentity", "IpAddress", "NotificationType")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
xylanNtpArch, = mibBuilder.importSymbols("XYLAN-BASE-MIB", "xylanNtpArch")
xylanNtpConfig = MibIdentifier((1, 3, 6, 1, 4, 1, 800, 2, 27, 1))
xylanNtpInfo = MibIdentifier((1, 3, 6, 1, 4, 1, 800, 2, 27, 2))
xylanNtpStats = MibIdentifier((1, 3, 6, 1, 4, 1, 800, 2, 27, 3))
xylanNtpAdmin = MibIdentifier((1, 3, 6, 1, 4, 1, 800, 2, 27, 4))
xylanNtpAccess = MibIdentifier((1, 3, 6, 1, 4, 1, 800, 2, 27, 5))
xylanNtpEnable = MibScalar((1, 3, 6, 1, 4, 1, 800, 2, 27, 1, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enable", 1), ("disable", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: xylanNtpEnable.setStatus('mandatory')
xylanNtpMonitorEnable = MibScalar((1, 3, 6, 1, 4, 1, 800, 2, 27, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enable", 1), ("disable", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: xylanNtpMonitorEnable.setStatus('mandatory')
xylanNtpPeerTable = MibTable((1, 3, 6, 1, 4, 1, 800, 2, 27, 1, 3), )
if mibBuilder.loadTexts: xylanNtpPeerTable.setStatus('mandatory')
xylanNtpPeerEntry = MibTableRow((1, 3, 6, 1, 4, 1, 800, 2, 27, 1, 3, 1), ).setIndexNames((0, "XYLAN-NTP-MIB", "xylanNtpPeerAddress"))
if mibBuilder.loadTexts: xylanNtpPeerEntry.setStatus('mandatory')
xylanNtpPeerAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 800, 2, 27, 1, 3, 1, 1), IpAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: xylanNtpPeerAddress.setStatus('mandatory')
xylanNtpPeerType = MibTableColumn((1, 3, 6, 1, 4, 1, 800, 2, 27, 1, 3, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 3, 5))).clone(namedValues=NamedValues(("active", 1), ("client", 3), ("broadcast", 5)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: xylanNtpPeerType.setStatus('mandatory')
xylanNtpPeerAuth = MibTableColumn((1, 3, 6, 1, 4, 1, 800, 2, 27, 1, 3, 1, 3), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: xylanNtpPeerAuth.setStatus('mandatory')
xylanNtpPeerVersion = MibTableColumn((1, 3, 6, 1, 4, 1, 800, 2, 27, 1, 3, 1, 4), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: xylanNtpPeerVersion.setStatus('mandatory')
xylanNtpPeerMinpoll = MibTableColumn((1, 3, 6, 1, 4, 1, 800, 2, 27, 1, 3, 1, 5), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: xylanNtpPeerMinpoll.setStatus('mandatory')
xylanNtpPeerPrefer = MibTableColumn((1, 3, 6, 1, 4, 1, 800, 2, 27, 1, 3, 1, 6), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("prefer", 1), ("no-prefer", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: xylanNtpPeerPrefer.setStatus('mandatory')
xylanNtpPeerAdmin = MibTableColumn((1, 3, 6, 1, 4, 1, 800, 2, 27, 1, 3, 1, 7), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("active", 1), ("delete", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: xylanNtpPeerAdmin.setStatus('mandatory')
xylanNtpPeerName = MibTableColumn((1, 3, 6, 1, 4, 1, 800, 2, 27, 1, 3, 1, 8), DisplayString()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: xylanNtpPeerName.setStatus('mandatory')
xylanNtpAuthDelay = MibScalar((1, 3, 6, 1, 4, 1, 800, 2, 27, 1, 4), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: xylanNtpAuthDelay.setStatus('mandatory')
xylanNtpKeysFile = MibScalar((1, 3, 6, 1, 4, 1, 800, 2, 27, 1, 5), DisplayString()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: xylanNtpKeysFile.setStatus('mandatory')
xylanNtpConfigReqKeyId = MibScalar((1, 3, 6, 1, 4, 1, 800, 2, 27, 1, 6), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: xylanNtpConfigReqKeyId.setStatus('mandatory')
xylanNtpConfigCtlKeyId = MibScalar((1, 3, 6, 1, 4, 1, 800, 2, 27, 1, 7), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: xylanNtpConfigCtlKeyId.setStatus('mandatory')
xylanNtpConfigCfgKeyId = MibScalar((1, 3, 6, 1, 4, 1, 800, 2, 27, 1, 8), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: xylanNtpConfigCfgKeyId.setStatus('mandatory')
xylanNtpPrecision = MibScalar((1, 3, 6, 1, 4, 1, 800, 2, 27, 1, 9), Integer32().subtype(subtypeSpec=ValueRangeConstraint(-20, -1))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: xylanNtpPrecision.setStatus('mandatory')
xylanNtpPeerListTable = MibTable((1, 3, 6, 1, 4, 1, 800, 2, 27, 2, 1), )
if mibBuilder.loadTexts: xylanNtpPeerListTable.setStatus('mandatory')
xylanNtpPeerListEntry = MibTableRow((1, 3, 6, 1, 4, 1, 800, 2, 27, 2, 1, 1), ).setIndexNames((0, "XYLAN-NTP-MIB", "xylanNtpPeerListAddress"))
if mibBuilder.loadTexts: xylanNtpPeerListEntry.setStatus('mandatory')
xylanNtpPeerListAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 800, 2, 27, 2, 1, 1, 1), IpAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: xylanNtpPeerListAddress.setStatus('mandatory')
xylanNtpPeerListLocal = MibTableColumn((1, 3, 6, 1, 4, 1, 800, 2, 27, 2, 1, 1, 2), IpAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: xylanNtpPeerListLocal.setStatus('mandatory')
xylanNtpPeerListStratum = MibTableColumn((1, 3, 6, 1, 4, 1, 800, 2, 27, 2, 1, 1, 3), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: xylanNtpPeerListStratum.setStatus('mandatory')
xylanNtpPeerListPoll = MibTableColumn((1, 3, 6, 1, 4, 1, 800, 2, 27, 2, 1, 1, 4), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: xylanNtpPeerListPoll.setStatus('mandatory')
xylanNtpPeerListReach = MibTableColumn((1, 3, 6, 1, 4, 1, 800, 2, 27, 2, 1, 1, 5), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: xylanNtpPeerListReach.setStatus('mandatory')
xylanNtpPeerListDelay = MibTableColumn((1, 3, 6, 1, 4, 1, 800, 2, 27, 2, 1, 1, 6), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: xylanNtpPeerListDelay.setStatus('mandatory')
xylanNtpPeerListOffset = MibTableColumn((1, 3, 6, 1, 4, 1, 800, 2, 27, 2, 1, 1, 7), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: xylanNtpPeerListOffset.setStatus('mandatory')
xylanNtpPeerListDispersion = MibTableColumn((1, 3, 6, 1, 4, 1, 800, 2, 27, 2, 1, 1, 8), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: xylanNtpPeerListDispersion.setStatus('mandatory')
xylanNtpPeerListSynced = MibTableColumn((1, 3, 6, 1, 4, 1, 800, 2, 27, 2, 1, 1, 9), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("synchornized", 1), ("not-synchronized", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: xylanNtpPeerListSynced.setStatus('mandatory')
xylanNtpPeerListName = MibTableColumn((1, 3, 6, 1, 4, 1, 800, 2, 27, 2, 1, 1, 10), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: xylanNtpPeerListName.setStatus('mandatory')
xylanNtpLocalInfo = MibScalar((1, 3, 6, 1, 4, 1, 800, 2, 27, 2, 2), Integer32())
if mibBuilder.loadTexts: xylanNtpLocalInfo.setStatus('mandatory')
xylanNtpInfoPeer = MibScalar((1, 3, 6, 1, 4, 1, 800, 2, 27, 2, 2, 1), IpAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: xylanNtpInfoPeer.setStatus('mandatory')
xylanNtpInfoMode = MibScalar((1, 3, 6, 1, 4, 1, 800, 2, 27, 2, 2, 2), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: xylanNtpInfoMode.setStatus('mandatory')
xylanNtpInfoLeapIndicator = MibScalar((1, 3, 6, 1, 4, 1, 800, 2, 27, 2, 2, 3), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: xylanNtpInfoLeapIndicator.setStatus('mandatory')
xylanNtpInfoStratum = MibScalar((1, 3, 6, 1, 4, 1, 800, 2, 27, 2, 2, 4), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: xylanNtpInfoStratum.setStatus('mandatory')
xylanNtpInfoPrecision = MibScalar((1, 3, 6, 1, 4, 1, 800, 2, 27, 2, 2, 5), Integer32().subtype(subtypeSpec=ValueRangeConstraint(-20, -4))).setMaxAccess("readonly")
if mibBuilder.loadTexts: xylanNtpInfoPrecision.setStatus('mandatory')
xylanNtpInfoDistance = MibScalar((1, 3, 6, 1, 4, 1, 800, 2, 27, 2, 2, 6), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: xylanNtpInfoDistance.setStatus('mandatory')
xylanNtpInfoDispersion = MibScalar((1, 3, 6, 1, 4, 1, 800, 2, 27, 2, 2, 7), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: xylanNtpInfoDispersion.setStatus('mandatory')
xylanNtpInfoReferenceId = MibScalar((1, 3, 6, 1, 4, 1, 800, 2, 27, 2, 2, 8), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: xylanNtpInfoReferenceId.setStatus('mandatory')
xylanNtpInfoReferenceTime = MibScalar((1, 3, 6, 1, 4, 1, 800, 2, 27, 2, 2, 9), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: xylanNtpInfoReferenceTime.setStatus('mandatory')
xylanNtpInfoFrequency = MibScalar((1, 3, 6, 1, 4, 1, 800, 2, 27, 2, 2, 10), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: xylanNtpInfoFrequency.setStatus('mandatory')
xylanNtpInfoStability = MibScalar((1, 3, 6, 1, 4, 1, 800, 2, 27, 2, 2, 11), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: xylanNtpInfoStability.setStatus('mandatory')
xylanNtpInfoBroadcastDelay = MibScalar((1, 3, 6, 1, 4, 1, 800, 2, 27, 2, 2, 12), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: xylanNtpInfoBroadcastDelay.setStatus('mandatory')
xylanNtpInfoAuthDelay = MibScalar((1, 3, 6, 1, 4, 1, 800, 2, 27, 2, 2, 13), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: xylanNtpInfoAuthDelay.setStatus('mandatory')
xylanNtpPeerShowTable = MibTable((1, 3, 6, 1, 4, 1, 800, 2, 27, 2, 3), )
if mibBuilder.loadTexts: xylanNtpPeerShowTable.setStatus('mandatory')
xylanNtpPeerShowEntry = MibTableRow((1, 3, 6, 1, 4, 1, 800, 2, 27, 2, 3, 1), ).setIndexNames((0, "XYLAN-NTP-MIB", "xylanNtpPeerShowRemote"))
if mibBuilder.loadTexts: xylanNtpPeerShowEntry.setStatus('mandatory')
xylanNtpPeerShowRemote = MibTableColumn((1, 3, 6, 1, 4, 1, 800, 2, 27, 2, 3, 1, 1), IpAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: xylanNtpPeerShowRemote.setStatus('mandatory')
xylanNtpPeerShowLocal = MibTableColumn((1, 3, 6, 1, 4, 1, 800, 2, 27, 2, 3, 1, 2), IpAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: xylanNtpPeerShowLocal.setStatus('mandatory')
xylanNtpPeerShowHmode = MibTableColumn((1, 3, 6, 1, 4, 1, 800, 2, 27, 2, 3, 1, 3), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: xylanNtpPeerShowHmode.setStatus('mandatory')
xylanNtpPeerShowPmode = MibTableColumn((1, 3, 6, 1, 4, 1, 800, 2, 27, 2, 3, 1, 4), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: xylanNtpPeerShowPmode.setStatus('mandatory')
xylanNtpPeerShowStratum = MibTableColumn((1, 3, 6, 1, 4, 1, 800, 2, 27, 2, 3, 1, 5), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: xylanNtpPeerShowStratum.setStatus('mandatory')
xylanNtpPeerShowPrecision = MibTableColumn((1, 3, 6, 1, 4, 1, 800, 2, 27, 2, 3, 1, 6), Integer32().subtype(subtypeSpec=ValueRangeConstraint(-20, -4))).setMaxAccess("readonly")
if mibBuilder.loadTexts: xylanNtpPeerShowPrecision.setStatus('mandatory')
xylanNtpPeerShowLeapIndicator = MibTableColumn((1, 3, 6, 1, 4, 1, 800, 2, 27, 2, 3, 1, 7), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: xylanNtpPeerShowLeapIndicator.setStatus('mandatory')
xylanNtpPeerShowReferenceId = MibTableColumn((1, 3, 6, 1, 4, 1, 800, 2, 27, 2, 3, 1, 8), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: xylanNtpPeerShowReferenceId.setStatus('mandatory')
xylanNtpPeerShowRootDistance = MibTableColumn((1, 3, 6, 1, 4, 1, 800, 2, 27, 2, 3, 1, 9), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: xylanNtpPeerShowRootDistance.setStatus('mandatory')
xylanNtpPeerShowRootDispersion = MibTableColumn((1, 3, 6, 1, 4, 1, 800, 2, 27, 2, 3, 1, 10), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: xylanNtpPeerShowRootDispersion.setStatus('mandatory')
xylanNtpPeerShowPpoll = MibTableColumn((1, 3, 6, 1, 4, 1, 800, 2, 27, 2, 3, 1, 11), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: xylanNtpPeerShowPpoll.setStatus('mandatory')
xylanNtpPeerShowHpoll = MibTableColumn((1, 3, 6, 1, 4, 1, 800, 2, 27, 2, 3, 1, 12), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: xylanNtpPeerShowHpoll.setStatus('mandatory')
xylanNtpPeerShowKeyid = MibTableColumn((1, 3, 6, 1, 4, 1, 800, 2, 27, 2, 3, 1, 13), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: xylanNtpPeerShowKeyid.setStatus('mandatory')
xylanNtpPeerShowVersion = MibTableColumn((1, 3, 6, 1, 4, 1, 800, 2, 27, 2, 3, 1, 14), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: xylanNtpPeerShowVersion.setStatus('mandatory')
xylanNtpPeerShowAssociation = MibTableColumn((1, 3, 6, 1, 4, 1, 800, 2, 27, 2, 3, 1, 15), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: xylanNtpPeerShowAssociation.setStatus('mandatory')
xylanNtpPeerShowValid = MibTableColumn((1, 3, 6, 1, 4, 1, 800, 2, 27, 2, 3, 1, 16), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: xylanNtpPeerShowValid.setStatus('mandatory')
xylanNtpPeerShowReach = MibTableColumn((1, 3, 6, 1, 4, 1, 800, 2, 27, 2, 3, 1, 17), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: xylanNtpPeerShowReach.setStatus('mandatory')
xylanNtpPeerShowUnreach = MibTableColumn((1, 3, 6, 1, 4, 1, 800, 2, 27, 2, 3, 1, 18), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: xylanNtpPeerShowUnreach.setStatus('mandatory')
xylanNtpPeerShowFlash = MibTableColumn((1, 3, 6, 1, 4, 1, 800, 2, 27, 2, 3, 1, 19), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: xylanNtpPeerShowFlash.setStatus('mandatory')
xylanNtpPeerShowBroadcastOffset = MibTableColumn((1, 3, 6, 1, 4, 1, 800, 2, 27, 2, 3, 1, 20), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: xylanNtpPeerShowBroadcastOffset.setStatus('mandatory')
xylanNtpPeerShowTTL = MibTableColumn((1, 3, 6, 1, 4, 1, 800, 2, 27, 2, 3, 1, 21), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: xylanNtpPeerShowTTL.setStatus('mandatory')
xylanNtpPeerShowTimer = MibTableColumn((1, 3, 6, 1, 4, 1, 800, 2, 27, 2, 3, 1, 22), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: xylanNtpPeerShowTimer.setStatus('mandatory')
xylanNtpPeerShowFlags = MibTableColumn((1, 3, 6, 1, 4, 1, 800, 2, 27, 2, 3, 1, 23), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: xylanNtpPeerShowFlags.setStatus('mandatory')
xylanNtpPeerShowReferenceTime = MibTableColumn((1, 3, 6, 1, 4, 1, 800, 2, 27, 2, 3, 1, 24), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: xylanNtpPeerShowReferenceTime.setStatus('mandatory')
xylanNtpPeerShowOriginateTime = MibTableColumn((1, 3, 6, 1, 4, 1, 800, 2, 27, 2, 3, 1, 25), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: xylanNtpPeerShowOriginateTime.setStatus('mandatory')
xylanNtpPeerShowReceiveTime = MibTableColumn((1, 3, 6, 1, 4, 1, 800, 2, 27, 2, 3, 1, 26), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: xylanNtpPeerShowReceiveTime.setStatus('mandatory')
xylanNtpPeerShowTransmitTime = MibTableColumn((1, 3, 6, 1, 4, 1, 800, 2, 27, 2, 3, 1, 27), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: xylanNtpPeerShowTransmitTime.setStatus('mandatory')
xylanNtpPeerShowOffset = MibTableColumn((1, 3, 6, 1, 4, 1, 800, 2, 27, 2, 3, 1, 28), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: xylanNtpPeerShowOffset.setStatus('mandatory')
xylanNtpPeerShowDelay = MibTableColumn((1, 3, 6, 1, 4, 1, 800, 2, 27, 2, 3, 1, 29), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: xylanNtpPeerShowDelay.setStatus('mandatory')
xylanNtpPeerShowDispersion = MibTableColumn((1, 3, 6, 1, 4, 1, 800, 2, 27, 2, 3, 1, 30), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: xylanNtpPeerShowDispersion.setStatus('mandatory')
xylanNtpPeerShowName = MibTableColumn((1, 3, 6, 1, 4, 1, 800, 2, 27, 2, 3, 1, 31), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: xylanNtpPeerShowName.setStatus('mandatory')
xylanNtpStatsStat = MibScalar((1, 3, 6, 1, 4, 1, 800, 2, 27, 3, 1), Integer32())
if mibBuilder.loadTexts: xylanNtpStatsStat.setStatus('mandatory')
xylanNtpStatsStatUptime = MibScalar((1, 3, 6, 1, 4, 1, 800, 2, 27, 3, 1, 1), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: xylanNtpStatsStatUptime.setStatus('mandatory')
xylanNtpStatsStatReset = MibScalar((1, 3, 6, 1, 4, 1, 800, 2, 27, 3, 1, 2), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: xylanNtpStatsStatReset.setStatus('mandatory')
xylanNtpStatsStatBadStratum = MibScalar((1, 3, 6, 1, 4, 1, 800, 2, 27, 3, 1, 3), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: xylanNtpStatsStatBadStratum.setStatus('mandatory')
xylanNtpStatsStatOldVersion = MibScalar((1, 3, 6, 1, 4, 1, 800, 2, 27, 3, 1, 4), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: xylanNtpStatsStatOldVersion.setStatus('mandatory')
xylanNtpStatsStatNewVersion = MibScalar((1, 3, 6, 1, 4, 1, 800, 2, 27, 3, 1, 5), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: xylanNtpStatsStatNewVersion.setStatus('mandatory')
xylanNtpStatsStatUnknownVersion = MibScalar((1, 3, 6, 1, 4, 1, 800, 2, 27, 3, 1, 6), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: xylanNtpStatsStatUnknownVersion.setStatus('mandatory')
xylanNtpStatsStatBadLength = MibScalar((1, 3, 6, 1, 4, 1, 800, 2, 27, 3, 1, 7), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: xylanNtpStatsStatBadLength.setStatus('mandatory')
xylanNtpStatsStatProcessed = MibScalar((1, 3, 6, 1, 4, 1, 800, 2, 27, 3, 1, 8), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: xylanNtpStatsStatProcessed.setStatus('mandatory')
xylanNtpStatsStatBadAuth = MibScalar((1, 3, 6, 1, 4, 1, 800, 2, 27, 3, 1, 9), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: xylanNtpStatsStatBadAuth.setStatus('mandatory')
xylanNtpStatsStatLimitRejects = MibScalar((1, 3, 6, 1, 4, 1, 800, 2, 27, 3, 1, 10), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: xylanNtpStatsStatLimitRejects.setStatus('mandatory')
xylanNtpStatsPeerTable = MibTable((1, 3, 6, 1, 4, 1, 800, 2, 27, 3, 2), )
if mibBuilder.loadTexts: xylanNtpStatsPeerTable.setStatus('mandatory')
xylanNtpStatsPeerEntry = MibTableRow((1, 3, 6, 1, 4, 1, 800, 2, 27, 3, 2, 1), ).setIndexNames((0, "XYLAN-NTP-MIB", "xylanNtpStatsPeerAddress"))
if mibBuilder.loadTexts: xylanNtpStatsPeerEntry.setStatus('mandatory')
xylanNtpStatsPeerAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 800, 2, 27, 3, 2, 1, 1), IpAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: xylanNtpStatsPeerAddress.setStatus('mandatory')
xylanNtpStatsPeerLocal = MibTableColumn((1, 3, 6, 1, 4, 1, 800, 2, 27, 3, 2, 1, 2), IpAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: xylanNtpStatsPeerLocal.setStatus('mandatory')
xylanNtpStatsPeerLastRcv = MibTableColumn((1, 3, 6, 1, 4, 1, 800, 2, 27, 3, 2, 1, 3), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: xylanNtpStatsPeerLastRcv.setStatus('mandatory')
xylanNtpStatsPeerNextSend = MibTableColumn((1, 3, 6, 1, 4, 1, 800, 2, 27, 3, 2, 1, 4), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: xylanNtpStatsPeerNextSend.setStatus('mandatory')
xylanNtpStatsPeerReachChange = MibTableColumn((1, 3, 6, 1, 4, 1, 800, 2, 27, 3, 2, 1, 5), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: xylanNtpStatsPeerReachChange.setStatus('mandatory')
xylanNtpStatsPeerPacketsSent = MibTableColumn((1, 3, 6, 1, 4, 1, 800, 2, 27, 3, 2, 1, 6), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: xylanNtpStatsPeerPacketsSent.setStatus('mandatory')
xylanNtpStatsPeerPacketsRcvd = MibTableColumn((1, 3, 6, 1, 4, 1, 800, 2, 27, 3, 2, 1, 7), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: xylanNtpStatsPeerPacketsRcvd.setStatus('mandatory')
xylanNtpStatsPeerBadAuth = MibTableColumn((1, 3, 6, 1, 4, 1, 800, 2, 27, 3, 2, 1, 8), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: xylanNtpStatsPeerBadAuth.setStatus('mandatory')
xylanNtpStatsPeerBogusOrigin = MibTableColumn((1, 3, 6, 1, 4, 1, 800, 2, 27, 3, 2, 1, 9), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: xylanNtpStatsPeerBogusOrigin.setStatus('mandatory')
xylanNtpStatsPeerDuplicate = MibTableColumn((1, 3, 6, 1, 4, 1, 800, 2, 27, 3, 2, 1, 10), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: xylanNtpStatsPeerDuplicate.setStatus('mandatory')
xylanNtpStatsPeerBadDispersion = MibTableColumn((1, 3, 6, 1, 4, 1, 800, 2, 27, 3, 2, 1, 11), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: xylanNtpStatsPeerBadDispersion.setStatus('mandatory')
xylanNtpStatsPeerBadRefTime = MibTableColumn((1, 3, 6, 1, 4, 1, 800, 2, 27, 3, 2, 1, 12), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: xylanNtpStatsPeerBadRefTime.setStatus('mandatory')
xylanNtpStatsPeerCandidateOrder = MibTableColumn((1, 3, 6, 1, 4, 1, 800, 2, 27, 3, 2, 1, 13), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: xylanNtpStatsPeerCandidateOrder.setStatus('mandatory')
xylanNtpStatsPeerReset = MibTableColumn((1, 3, 6, 1, 4, 1, 800, 2, 27, 3, 2, 1, 14), Integer32()).setMaxAccess("writeonly")
if mibBuilder.loadTexts: xylanNtpStatsPeerReset.setStatus('mandatory')
xylanNtpStatsPeerName = MibTableColumn((1, 3, 6, 1, 4, 1, 800, 2, 27, 3, 2, 1, 15), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: xylanNtpStatsPeerName.setStatus('mandatory')
xylanNtpStatsLoop = MibScalar((1, 3, 6, 1, 4, 1, 800, 2, 27, 3, 3), Integer32())
if mibBuilder.loadTexts: xylanNtpStatsLoop.setStatus('mandatory')
xylanNtpStatsLoopOffset = MibScalar((1, 3, 6, 1, 4, 1, 800, 2, 27, 3, 3, 1), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: xylanNtpStatsLoopOffset.setStatus('mandatory')
xylanNtpStatsLoopFrequency = MibScalar((1, 3, 6, 1, 4, 1, 800, 2, 27, 3, 3, 2), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: xylanNtpStatsLoopFrequency.setStatus('mandatory')
xylanNtpStatsLoopPollAdjust = MibScalar((1, 3, 6, 1, 4, 1, 800, 2, 27, 3, 3, 3), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: xylanNtpStatsLoopPollAdjust.setStatus('mandatory')
xylanNtpStatsLoopWatchdog = MibScalar((1, 3, 6, 1, 4, 1, 800, 2, 27, 3, 3, 4), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: xylanNtpStatsLoopWatchdog.setStatus('mandatory')
xylanNtpStatsIo = MibScalar((1, 3, 6, 1, 4, 1, 800, 2, 27, 3, 4), Integer32())
if mibBuilder.loadTexts: xylanNtpStatsIo.setStatus('mandatory')
xylanNtpStatsIoReset = MibScalar((1, 3, 6, 1, 4, 1, 800, 2, 27, 3, 4, 1), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: xylanNtpStatsIoReset.setStatus('mandatory')
xylanNtpStatsIoRcvBuffers = MibScalar((1, 3, 6, 1, 4, 1, 800, 2, 27, 3, 4, 2), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: xylanNtpStatsIoRcvBuffers.setStatus('mandatory')
xylanNtpStatsIoFreeRcvBuffers = MibScalar((1, 3, 6, 1, 4, 1, 800, 2, 27, 3, 4, 3), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: xylanNtpStatsIoFreeRcvBuffers.setStatus('mandatory')
xylanNtpStatsIoUsedRcvBuffers = MibScalar((1, 3, 6, 1, 4, 1, 800, 2, 27, 3, 4, 4), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: xylanNtpStatsIoUsedRcvBuffers.setStatus('mandatory')
xylanNtpStatsIoRefills = MibScalar((1, 3, 6, 1, 4, 1, 800, 2, 27, 3, 4, 5), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: xylanNtpStatsIoRefills.setStatus('mandatory')
xylanNtpStatsIoDroppedPackets = MibScalar((1, 3, 6, 1, 4, 1, 800, 2, 27, 3, 4, 6), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: xylanNtpStatsIoDroppedPackets.setStatus('mandatory')
xylanNtpStatsIoIgnoredPackets = MibScalar((1, 3, 6, 1, 4, 1, 800, 2, 27, 3, 4, 7), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: xylanNtpStatsIoIgnoredPackets.setStatus('mandatory')
xylanNtpStatsIoRcvPackets = MibScalar((1, 3, 6, 1, 4, 1, 800, 2, 27, 3, 4, 8), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: xylanNtpStatsIoRcvPackets.setStatus('mandatory')
xylanNtpStatsIoSentPackets = MibScalar((1, 3, 6, 1, 4, 1, 800, 2, 27, 3, 4, 9), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: xylanNtpStatsIoSentPackets.setStatus('mandatory')
xylanNtpStatsIoNotSentPackets = MibScalar((1, 3, 6, 1, 4, 1, 800, 2, 27, 3, 4, 10), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: xylanNtpStatsIoNotSentPackets.setStatus('mandatory')
xylanNtpStatsIoInterrupts = MibScalar((1, 3, 6, 1, 4, 1, 800, 2, 27, 3, 4, 11), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: xylanNtpStatsIoInterrupts.setStatus('mandatory')
xylanNtpStatsIoInterruptsRcv = MibScalar((1, 3, 6, 1, 4, 1, 800, 2, 27, 3, 4, 12), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: xylanNtpStatsIoInterruptsRcv.setStatus('mandatory')
xylanNtpStatsReset = MibScalar((1, 3, 6, 1, 4, 1, 800, 2, 27, 3, 5), Integer32()).setMaxAccess("writeonly")
if mibBuilder.loadTexts: xylanNtpStatsReset.setStatus('mandatory')
xylanNtpStatsMonitorTable = MibTable((1, 3, 6, 1, 4, 1, 800, 2, 27, 3, 6), )
if mibBuilder.loadTexts: xylanNtpStatsMonitorTable.setStatus('mandatory')
xylanNtpStatsMonitorEntry = MibTableRow((1, 3, 6, 1, 4, 1, 800, 2, 27, 3, 6, 1), ).setIndexNames((0, "XYLAN-NTP-MIB", "xylanNtpStatsMonitorIndex"))
if mibBuilder.loadTexts: xylanNtpStatsMonitorEntry.setStatus('mandatory')
xylanNtpStatsMonitorIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 800, 2, 27, 3, 6, 1, 1), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: xylanNtpStatsMonitorIndex.setStatus('mandatory')
xylanNtpStatsMonitorAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 800, 2, 27, 3, 6, 1, 2), IpAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: xylanNtpStatsMonitorAddress.setStatus('mandatory')
xylanNtpStatsMonitorPort = MibTableColumn((1, 3, 6, 1, 4, 1, 800, 2, 27, 3, 6, 1, 3), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: xylanNtpStatsMonitorPort.setStatus('mandatory')
xylanNtpStatsMonitorLocalAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 800, 2, 27, 3, 6, 1, 4), IpAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: xylanNtpStatsMonitorLocalAddress.setStatus('mandatory')
xylanNtpStatsMonitorCount = MibTableColumn((1, 3, 6, 1, 4, 1, 800, 2, 27, 3, 6, 1, 5), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: xylanNtpStatsMonitorCount.setStatus('mandatory')
xylanNtpStatsMonitorMode = MibTableColumn((1, 3, 6, 1, 4, 1, 800, 2, 27, 3, 6, 1, 6), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: xylanNtpStatsMonitorMode.setStatus('mandatory')
xylanNtpStatsMonitorVersion = MibTableColumn((1, 3, 6, 1, 4, 1, 800, 2, 27, 3, 6, 1, 7), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: xylanNtpStatsMonitorVersion.setStatus('mandatory')
xylanNtpStatsMonitorDrop = MibTableColumn((1, 3, 6, 1, 4, 1, 800, 2, 27, 3, 6, 1, 8), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: xylanNtpStatsMonitorDrop.setStatus('mandatory')
xylanNtpStatsMonitorLast = MibTableColumn((1, 3, 6, 1, 4, 1, 800, 2, 27, 3, 6, 1, 9), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: xylanNtpStatsMonitorLast.setStatus('mandatory')
xylanNtpStatsMonitorFirst = MibTableColumn((1, 3, 6, 1, 4, 1, 800, 2, 27, 3, 6, 1, 10), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: xylanNtpStatsMonitorFirst.setStatus('mandatory')
xylanNtpStatsMonitorName = MibTableColumn((1, 3, 6, 1, 4, 1, 800, 2, 27, 3, 6, 1, 11), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: xylanNtpStatsMonitorName.setStatus('mandatory')
xylanNtpAccessKeyIdTable = MibTable((1, 3, 6, 1, 4, 1, 800, 2, 27, 5, 1), )
if mibBuilder.loadTexts: xylanNtpAccessKeyIdTable.setStatus('mandatory')
xylanNtpAccessKeyIdEntry = MibTableRow((1, 3, 6, 1, 4, 1, 800, 2, 27, 5, 1, 1), ).setIndexNames((0, "XYLAN-NTP-MIB", "xylanNtpAccessKeyIdKeyId"))
if mibBuilder.loadTexts: xylanNtpAccessKeyIdEntry.setStatus('mandatory')
xylanNtpAccessKeyIdKeyId = MibTableColumn((1, 3, 6, 1, 4, 1, 800, 2, 27, 5, 1, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: xylanNtpAccessKeyIdKeyId.setStatus('mandatory')
xylanNtpAccessKeyIdAdmin = MibTableColumn((1, 3, 6, 1, 4, 1, 800, 2, 27, 5, 1, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("active", 1), ("delete", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: xylanNtpAccessKeyIdAdmin.setStatus('mandatory')
xylanNtpAccessRestrictedTable = MibTable((1, 3, 6, 1, 4, 1, 800, 2, 27, 5, 2), )
if mibBuilder.loadTexts: xylanNtpAccessRestrictedTable.setStatus('mandatory')
xylanNtpAccessRestrictedEntry = MibTableRow((1, 3, 6, 1, 4, 1, 800, 2, 27, 5, 2, 1), ).setIndexNames((0, "XYLAN-NTP-MIB", "xylanNtpAccessRestrictedIpAddress"), (0, "XYLAN-NTP-MIB", "xylanNtpAccessRestrictedMask"))
if mibBuilder.loadTexts: xylanNtpAccessRestrictedEntry.setStatus('mandatory')
xylanNtpAccessRestrictedIpAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 800, 2, 27, 5, 2, 1, 1), IpAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: xylanNtpAccessRestrictedIpAddress.setStatus('mandatory')
xylanNtpAccessRestrictedMask = MibTableColumn((1, 3, 6, 1, 4, 1, 800, 2, 27, 5, 2, 1, 2), IpAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: xylanNtpAccessRestrictedMask.setStatus('mandatory')
xylanNtpAccessRestrictedRestrictions = MibTableColumn((1, 3, 6, 1, 4, 1, 800, 2, 27, 5, 2, 1, 3), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: xylanNtpAccessRestrictedRestrictions.setStatus('mandatory')
xylanNtpAccessRestrictedCount = MibTableColumn((1, 3, 6, 1, 4, 1, 800, 2, 27, 5, 2, 1, 4), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: xylanNtpAccessRestrictedCount.setStatus('mandatory')
xylanNtpAccessRestrictedAdmin = MibTableColumn((1, 3, 6, 1, 4, 1, 800, 2, 27, 5, 2, 1, 5), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("active", 1), ("delete", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: xylanNtpAccessRestrictedAdmin.setStatus('mandatory')
xylanNtpAccessRereadKeyFile = MibScalar((1, 3, 6, 1, 4, 1, 800, 2, 27, 5, 3), Integer32()).setMaxAccess("writeonly")
if mibBuilder.loadTexts: xylanNtpAccessRereadKeyFile.setStatus('mandatory')
mibBuilder.exportSymbols("XYLAN-NTP-MIB", xylanNtpStatsIoReset=xylanNtpStatsIoReset, xylanNtpPeerShowRootDistance=xylanNtpPeerShowRootDistance, xylanNtpStatsPeerLastRcv=xylanNtpStatsPeerLastRcv, xylanNtpPeerListStratum=xylanNtpPeerListStratum, xylanNtpPeerTable=xylanNtpPeerTable, xylanNtpPeerAuth=xylanNtpPeerAuth, xylanNtpPeerName=xylanNtpPeerName, xylanNtpPeerShowStratum=xylanNtpPeerShowStratum, xylanNtpStatsIoInterruptsRcv=xylanNtpStatsIoInterruptsRcv, xylanNtpPeerMinpoll=xylanNtpPeerMinpoll, xylanNtpStatsLoopWatchdog=xylanNtpStatsLoopWatchdog, xylanNtpPeerVersion=xylanNtpPeerVersion, xylanNtpPeerShowTimer=xylanNtpPeerShowTimer, xylanNtpStatsMonitorPort=xylanNtpStatsMonitorPort, xylanNtpStatsMonitorDrop=xylanNtpStatsMonitorDrop, xylanNtpInfoDistance=xylanNtpInfoDistance, xylanNtpPeerShowHmode=xylanNtpPeerShowHmode, xylanNtpConfig=xylanNtpConfig, xylanNtpPrecision=xylanNtpPrecision, xylanNtpConfigReqKeyId=xylanNtpConfigReqKeyId, xylanNtpPeerAdmin=xylanNtpPeerAdmin, xylanNtpPeerListAddress=xylanNtpPeerListAddress, xylanNtpStatsPeerBogusOrigin=xylanNtpStatsPeerBogusOrigin, xylanNtpInfoReferenceId=xylanNtpInfoReferenceId, xylanNtpStatsLoopFrequency=xylanNtpStatsLoopFrequency, xylanNtpPeerListOffset=xylanNtpPeerListOffset, xylanNtpPeerEntry=xylanNtpPeerEntry, xylanNtpStatsPeerBadRefTime=xylanNtpStatsPeerBadRefTime, xylanNtpStatsIoRefills=xylanNtpStatsIoRefills, xylanNtpStatsPeerBadDispersion=xylanNtpStatsPeerBadDispersion, xylanNtpStats=xylanNtpStats, xylanNtpPeerShowKeyid=xylanNtpPeerShowKeyid, xylanNtpPeerListEntry=xylanNtpPeerListEntry, xylanNtpMonitorEnable=xylanNtpMonitorEnable, xylanNtpStatsPeerNextSend=xylanNtpStatsPeerNextSend, xylanNtpStatsPeerBadAuth=xylanNtpStatsPeerBadAuth, xylanNtpStatsIoInterrupts=xylanNtpStatsIoInterrupts, xylanNtpConfigCtlKeyId=xylanNtpConfigCtlKeyId, xylanNtpLocalInfo=xylanNtpLocalInfo, xylanNtpStatsPeerLocal=xylanNtpStatsPeerLocal, xylanNtpPeerListDelay=xylanNtpPeerListDelay, xylanNtpAccessRestrictedEntry=xylanNtpAccessRestrictedEntry, xylanNtpStatsMonitorEntry=xylanNtpStatsMonitorEntry, xylanNtpPeerListTable=xylanNtpPeerListTable, xylanNtpPeerShowTransmitTime=xylanNtpPeerShowTransmitTime, xylanNtpInfoDispersion=xylanNtpInfoDispersion, xylanNtpPeerShowReferenceId=xylanNtpPeerShowReferenceId, xylanNtpStatsMonitorVersion=xylanNtpStatsMonitorVersion, xylanNtpStatsMonitorFirst=xylanNtpStatsMonitorFirst, xylanNtpStatsPeerEntry=xylanNtpStatsPeerEntry, xylanNtpInfoPrecision=xylanNtpInfoPrecision, xylanNtpPeerShowTable=xylanNtpPeerShowTable, xylanNtpAccessRestrictedIpAddress=xylanNtpAccessRestrictedIpAddress, xylanNtpStatsMonitorMode=xylanNtpStatsMonitorMode, xylanNtpStatsIoRcvBuffers=xylanNtpStatsIoRcvBuffers, xylanNtpPeerListLocal=xylanNtpPeerListLocal, xylanNtpStatsStatOldVersion=xylanNtpStatsStatOldVersion, xylanNtpStatsLoop=xylanNtpStatsLoop, xylanNtpStatsPeerPacketsSent=xylanNtpStatsPeerPacketsSent, xylanNtpPeerPrefer=xylanNtpPeerPrefer, xylanNtpStatsIoDroppedPackets=xylanNtpStatsIoDroppedPackets, xylanNtpPeerShowRootDispersion=xylanNtpPeerShowRootDispersion, xylanNtpPeerListDispersion=xylanNtpPeerListDispersion, xylanNtpPeerListName=xylanNtpPeerListName, xylanNtpPeerShowEntry=xylanNtpPeerShowEntry, xylanNtpPeerShowRemote=xylanNtpPeerShowRemote, xylanNtpStatsPeerReachChange=xylanNtpStatsPeerReachChange, xylanNtpStatsIoUsedRcvBuffers=xylanNtpStatsIoUsedRcvBuffers, xylanNtpPeerShowLeapIndicator=xylanNtpPeerShowLeapIndicator, xylanNtpPeerShowReferenceTime=xylanNtpPeerShowReferenceTime, xylanNtpPeerShowOffset=xylanNtpPeerShowOffset, xylanNtpStatsPeerReset=xylanNtpStatsPeerReset, xylanNtpStatsIoIgnoredPackets=xylanNtpStatsIoIgnoredPackets, xylanNtpStatsIoNotSentPackets=xylanNtpStatsIoNotSentPackets, xylanNtpStatsIoFreeRcvBuffers=xylanNtpStatsIoFreeRcvBuffers, xylanNtpPeerShowReach=xylanNtpPeerShowReach, xylanNtpPeerShowDispersion=xylanNtpPeerShowDispersion, xylanNtpPeerShowVersion=xylanNtpPeerShowVersion, xylanNtpPeerShowValid=xylanNtpPeerShowValid, xylanNtpAccess=xylanNtpAccess, xylanNtpInfoReferenceTime=xylanNtpInfoReferenceTime, xylanNtpStatsLoopOffset=xylanNtpStatsLoopOffset, xylanNtpStatsMonitorLast=xylanNtpStatsMonitorLast, xylanNtpStatsStatProcessed=xylanNtpStatsStatProcessed, xylanNtpStatsMonitorName=xylanNtpStatsMonitorName, xylanNtpPeerListPoll=xylanNtpPeerListPoll, xylanNtpStatsIoRcvPackets=xylanNtpStatsIoRcvPackets, xylanNtpPeerShowHpoll=xylanNtpPeerShowHpoll, xylanNtpAccessRestrictedCount=xylanNtpAccessRestrictedCount, xylanNtpStatsPeerCandidateOrder=xylanNtpStatsPeerCandidateOrder, xylanNtpStatsStatReset=xylanNtpStatsStatReset, xylanNtpKeysFile=xylanNtpKeysFile, xylanNtpEnable=xylanNtpEnable, xylanNtpInfoFrequency=xylanNtpInfoFrequency, xylanNtpPeerShowBroadcastOffset=xylanNtpPeerShowBroadcastOffset, xylanNtpStatsStatBadStratum=xylanNtpStatsStatBadStratum, xylanNtpStatsPeerDuplicate=xylanNtpStatsPeerDuplicate, xylanNtpPeerShowDelay=xylanNtpPeerShowDelay, xylanNtpStatsMonitorIndex=xylanNtpStatsMonitorIndex, xylanNtpStatsStat=xylanNtpStatsStat, xylanNtpPeerShowReceiveTime=xylanNtpPeerShowReceiveTime, xylanNtpPeerType=xylanNtpPeerType, xylanNtpStatsMonitorAddress=xylanNtpStatsMonitorAddress, xylanNtpAccessKeyIdEntry=xylanNtpAccessKeyIdEntry, xylanNtpAuthDelay=xylanNtpAuthDelay, xylanNtpPeerShowFlags=xylanNtpPeerShowFlags, xylanNtpPeerShowPrecision=xylanNtpPeerShowPrecision, xylanNtpPeerShowPmode=xylanNtpPeerShowPmode, xylanNtpPeerShowUnreach=xylanNtpPeerShowUnreach, xylanNtpAccessKeyIdAdmin=xylanNtpAccessKeyIdAdmin, xylanNtpPeerShowTTL=xylanNtpPeerShowTTL, xylanNtpStatsPeerName=xylanNtpStatsPeerName, xylanNtpAdmin=xylanNtpAdmin, xylanNtpStatsStatLimitRejects=xylanNtpStatsStatLimitRejects, xylanNtpInfoStratum=xylanNtpInfoStratum, xylanNtpPeerShowOriginateTime=xylanNtpPeerShowOriginateTime, xylanNtpStatsIoSentPackets=xylanNtpStatsIoSentPackets, xylanNtpAccessRestrictedTable=xylanNtpAccessRestrictedTable, xylanNtpInfoStability=xylanNtpInfoStability, xylanNtpStatsStatBadLength=xylanNtpStatsStatBadLength, xylanNtpPeerShowName=xylanNtpPeerShowName, xylanNtpPeerShowAssociation=xylanNtpPeerShowAssociation, xylanNtpInfoBroadcastDelay=xylanNtpInfoBroadcastDelay, xylanNtpStatsStatBadAuth=xylanNtpStatsStatBadAuth, xylanNtpAccessRestrictedRestrictions=xylanNtpAccessRestrictedRestrictions, xylanNtpInfoPeer=xylanNtpInfoPeer, xylanNtpInfoMode=xylanNtpInfoMode, xylanNtpAccessRestrictedAdmin=xylanNtpAccessRestrictedAdmin, xylanNtpAccessKeyIdKeyId=xylanNtpAccessKeyIdKeyId, xylanNtpPeerShowPpoll=xylanNtpPeerShowPpoll, xylanNtpInfo=xylanNtpInfo, xylanNtpStatsStatNewVersion=xylanNtpStatsStatNewVersion, xylanNtpStatsMonitorLocalAddress=xylanNtpStatsMonitorLocalAddress, xylanNtpPeerShowFlash=xylanNtpPeerShowFlash, xylanNtpStatsStatUptime=xylanNtpStatsStatUptime, xylanNtpAccessRereadKeyFile=xylanNtpAccessRereadKeyFile, xylanNtpAccessKeyIdTable=xylanNtpAccessKeyIdTable, xylanNtpInfoLeapIndicator=xylanNtpInfoLeapIndicator, xylanNtpAccessRestrictedMask=xylanNtpAccessRestrictedMask, xylanNtpStatsReset=xylanNtpStatsReset, xylanNtpStatsStatUnknownVersion=xylanNtpStatsStatUnknownVersion, xylanNtpPeerListReach=xylanNtpPeerListReach, xylanNtpStatsIo=xylanNtpStatsIo, xylanNtpStatsPeerAddress=xylanNtpStatsPeerAddress, xylanNtpStatsLoopPollAdjust=xylanNtpStatsLoopPollAdjust, xylanNtpInfoAuthDelay=xylanNtpInfoAuthDelay, xylanNtpPeerShowLocal=xylanNtpPeerShowLocal, xylanNtpStatsPeerPacketsRcvd=xylanNtpStatsPeerPacketsRcvd, xylanNtpPeerListSynced=xylanNtpPeerListSynced, xylanNtpStatsPeerTable=xylanNtpStatsPeerTable, xylanNtpConfigCfgKeyId=xylanNtpConfigCfgKeyId, xylanNtpStatsMonitorTable=xylanNtpStatsMonitorTable, xylanNtpStatsMonitorCount=xylanNtpStatsMonitorCount, xylanNtpPeerAddress=xylanNtpPeerAddress)
