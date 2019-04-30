#
# PySNMP MIB module CIENA-CES-TIME-SYNC-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/CIENA-CES-TIME-SYNC-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 17:31:59 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
ObjectIdentifier, Integer, OctetString = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "Integer", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsUnion, SingleValueConstraint, ValueRangeConstraint, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsUnion", "SingleValueConstraint", "ValueRangeConstraint", "ConstraintsIntersection")
cienaGlobalSeverity, cienaGlobalMacAddress = mibBuilder.importSymbols("CIENA-GLOBAL-MIB", "cienaGlobalSeverity", "cienaGlobalMacAddress")
cienaCesConfig, cienaCesNotifications = mibBuilder.importSymbols("CIENA-SMI", "cienaCesConfig", "cienaCesNotifications")
CienaGlobalState, = mibBuilder.importSymbols("CIENA-TC", "CienaGlobalState")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
Unsigned32, Bits, MibScalar, MibTable, MibTableRow, MibTableColumn, Gauge32, ModuleIdentity, Integer32, iso, Counter32, NotificationType, TimeTicks, IpAddress, Counter64, ObjectIdentity, MibIdentifier = mibBuilder.importSymbols("SNMPv2-SMI", "Unsigned32", "Bits", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Gauge32", "ModuleIdentity", "Integer32", "iso", "Counter32", "NotificationType", "TimeTicks", "IpAddress", "Counter64", "ObjectIdentity", "MibIdentifier")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
cienaCesTimeSyncMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 1271, 2, 1, 28))
cienaCesTimeSyncMIB.setRevisions(('2012-06-20 00:00',))
if mibBuilder.loadTexts: cienaCesTimeSyncMIB.setLastUpdated('201206200000Z')
if mibBuilder.loadTexts: cienaCesTimeSyncMIB.setOrganization('Ciena, Inc')
class SsmStratumLevel(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16))
    namedValues = NamedValues(("unknown", 1), ("prc", 2), ("ssua", 3), ("ssub", 4), ("sec", 5), ("dnu", 6), ("prs", 7), ("stu", 8), ("st2", 9), ("tnc", 10), ("st3e", 11), ("st3", 12), ("smc", 13), ("st4", 14), ("dus", 15), ("prov", 16))

class SyncInterfaceProtocol(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3))
    namedValues = NamedValues(("unknown", 1), ("bits", 2), ("synce", 3))

class SyncBITSSignalMode(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7))
    namedValues = NamedValues(("modeunknown", 1), ("modet1", 2), ("modee1", 3), ("modej1", 4), ("mode2048khz", 5), ("mode64kcc", 6), ("mode6312khz", 7))

class SyncBITSSignalFormat(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7))
    namedValues = NamedValues(("unknown", 1), ("cas", 2), ("cascrc", 3), ("esf", 4), ("fas", 5), ("fascrc", 6), ("sf", 7))

class SyncBITSSignalEncoding(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))
    namedValues = NamedValues(("unknown", 1), ("b8zs", 2), ("ami", 3), ("hdb3", 4))

class SyncRefOperationalStatus(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14))
    namedValues = NamedValues(("unknown", 1), ("active", 2), ("selected", 3), ("lossofsignal", 4), ("lossofframe", 5), ("alarmindicationsignal", 6), ("hardwarefault", 7), ("hardwarenotconfigured", 8), ("qlbelowthreshold", 9), ("rxtimeout", 10), ("notauthenticated", 11), ("loopbacktx", 12), ("loopbackrx", 13), ("linkflap", 14))

cienaCesTimeSyncMIBObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 1271, 2, 1, 28, 1))
cienaCesTimeSyncObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 1271, 2, 1, 28, 1, 1))
cienaCesTimeSyncMIBNotificationPrefix = MibIdentifier((1, 3, 6, 1, 4, 1, 1271, 2, 2, 28))
cienaCesTimeSyncMIBNotifications = MibIdentifier((1, 3, 6, 1, 4, 1, 1271, 2, 2, 28, 0))
cienaCesSyncAdminState = MibScalar((1, 3, 6, 1, 4, 1, 1271, 2, 1, 28, 1, 1, 1), CienaGlobalState()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cienaCesSyncAdminState.setStatus('current')
cienaCesSyncOptionType = MibScalar((1, 3, 6, 1, 4, 1, 1271, 2, 1, 28, 1, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("unknown", 1), ("option1", 2), ("option2", 3)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: cienaCesSyncOptionType.setStatus('current')
cienaCesSyncRevertiveMode = MibScalar((1, 3, 6, 1, 4, 1, 1271, 2, 1, 28, 1, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("unknown", 1), ("revertive", 2), ("nonrevertive", 3)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: cienaCesSyncRevertiveMode.setStatus('current')
cienaCesSyncWaitToRestoreTimer = MibScalar((1, 3, 6, 1, 4, 1, 1271, 2, 1, 28, 1, 1, 4), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cienaCesSyncWaitToRestoreTimer.setStatus('current')
cienaCesSyncInputProtectionGroupTable = MibTable((1, 3, 6, 1, 4, 1, 1271, 2, 1, 28, 1, 1, 5), )
if mibBuilder.loadTexts: cienaCesSyncInputProtectionGroupTable.setStatus('current')
cienaCesSyncInputProtectionGroupEntry = MibTableRow((1, 3, 6, 1, 4, 1, 1271, 2, 1, 28, 1, 1, 5, 1), ).setIndexNames((0, "CIENA-CES-TIME-SYNC-MIB", "cienaCesInputPGEntityId"))
if mibBuilder.loadTexts: cienaCesSyncInputProtectionGroupEntry.setStatus('current')
cienaCesInputPGEntityId = MibTableColumn((1, 3, 6, 1, 4, 1, 1271, 2, 1, 28, 1, 1, 5, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 1)))
if mibBuilder.loadTexts: cienaCesInputPGEntityId.setStatus('current')
cienaCesInputPGEntityName = MibTableColumn((1, 3, 6, 1, 4, 1, 1271, 2, 1, 28, 1, 1, 5, 1, 2), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(1, 31))).setMaxAccess("readonly")
if mibBuilder.loadTexts: cienaCesInputPGEntityName.setStatus('current')
cienaCesInputPGPreferredReference = MibTableColumn((1, 3, 6, 1, 4, 1, 1271, 2, 1, 28, 1, 1, 5, 1, 3), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(1, 31))).setMaxAccess("readonly")
if mibBuilder.loadTexts: cienaCesInputPGPreferredReference.setStatus('current')
cienaCesInputPGSelectedReference = MibTableColumn((1, 3, 6, 1, 4, 1, 1271, 2, 1, 28, 1, 1, 5, 1, 4), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(1, 31))).setMaxAccess("readonly")
if mibBuilder.loadTexts: cienaCesInputPGSelectedReference.setStatus('current')
cienaCesInputPGForcedReference = MibTableColumn((1, 3, 6, 1, 4, 1, 1271, 2, 1, 28, 1, 1, 5, 1, 5), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(1, 31))).setMaxAccess("readonly")
if mibBuilder.loadTexts: cienaCesInputPGForcedReference.setStatus('current')
cienaCesInputPGThresholdQualityLevel = MibTableColumn((1, 3, 6, 1, 4, 1, 1271, 2, 1, 28, 1, 1, 5, 1, 6), SsmStratumLevel()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cienaCesInputPGThresholdQualityLevel.setStatus('current')
cienaCesInputPGState = MibTableColumn((1, 3, 6, 1, 4, 1, 1271, 2, 1, 28, 1, 1, 5, 1, 7), CienaGlobalState()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cienaCesInputPGState.setStatus('current')
cienaCesInputPGStateDuration = MibTableColumn((1, 3, 6, 1, 4, 1, 1271, 2, 1, 28, 1, 1, 5, 1, 8), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(1, 31))).setMaxAccess("readonly")
if mibBuilder.loadTexts: cienaCesInputPGStateDuration.setStatus('current')
cienaCesInputPGReferenceSwitchCount = MibTableColumn((1, 3, 6, 1, 4, 1, 1271, 2, 1, 28, 1, 1, 5, 1, 9), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cienaCesInputPGReferenceSwitchCount.setStatus('current')
cienaCesInputPGOperationalStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 1271, 2, 1, 28, 1, 1, 5, 1, 10), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5))).clone(namedValues=NamedValues(("unknown", 1), ("freerun", 2), ("holdover", 3), ("locked", 4), ("acquiringlock", 5)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: cienaCesInputPGOperationalStatus.setStatus('current')
cienaCesSyncInputProtectionUnitTable = MibTable((1, 3, 6, 1, 4, 1, 1271, 2, 1, 28, 1, 1, 6), )
if mibBuilder.loadTexts: cienaCesSyncInputProtectionUnitTable.setStatus('current')
cienaCesSyncInputProtectionUnitEntry = MibTableRow((1, 3, 6, 1, 4, 1, 1271, 2, 1, 28, 1, 1, 6, 1), ).setIndexNames((0, "CIENA-CES-TIME-SYNC-MIB", "cienaCesInputPUEntityId"))
if mibBuilder.loadTexts: cienaCesSyncInputProtectionUnitEntry.setStatus('current')
cienaCesInputPUEntityId = MibTableColumn((1, 3, 6, 1, 4, 1, 1271, 2, 1, 28, 1, 1, 6, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 48)))
if mibBuilder.loadTexts: cienaCesInputPUEntityId.setStatus('current')
cienaCesInputPUEntityName = MibTableColumn((1, 3, 6, 1, 4, 1, 1271, 2, 1, 28, 1, 1, 6, 1, 2), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(1, 31))).setMaxAccess("readonly")
if mibBuilder.loadTexts: cienaCesInputPUEntityName.setStatus('current')
cienaCesInputPUPGEntityName = MibTableColumn((1, 3, 6, 1, 4, 1, 1271, 2, 1, 28, 1, 1, 6, 1, 3), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(1, 31))).setMaxAccess("readonly")
if mibBuilder.loadTexts: cienaCesInputPUPGEntityName.setStatus('current')
cienaCesInputPUTimingInterfaceName = MibTableColumn((1, 3, 6, 1, 4, 1, 1271, 2, 1, 28, 1, 1, 6, 1, 4), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(1, 31))).setMaxAccess("readonly")
if mibBuilder.loadTexts: cienaCesInputPUTimingInterfaceName.setStatus('current')
cienaCesInputPUTimingInterfaceProtocol = MibTableColumn((1, 3, 6, 1, 4, 1, 1271, 2, 1, 28, 1, 1, 6, 1, 5), SyncInterfaceProtocol()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cienaCesInputPUTimingInterfaceProtocol.setStatus('current')
cienaCesInputPUUserPriority = MibTableColumn((1, 3, 6, 1, 4, 1, 1271, 2, 1, 28, 1, 1, 6, 1, 6), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cienaCesInputPUUserPriority.setStatus('current')
cienaCesInputPUOperationalQL = MibTableColumn((1, 3, 6, 1, 4, 1, 1271, 2, 1, 28, 1, 1, 6, 1, 7), SsmStratumLevel()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cienaCesInputPUOperationalQL.setStatus('current')
cienaCesInputPUForcedQL = MibTableColumn((1, 3, 6, 1, 4, 1, 1271, 2, 1, 28, 1, 1, 6, 1, 8), SsmStratumLevel()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cienaCesInputPUForcedQL.setStatus('current')
cienaCesInputPUReceivedQL = MibTableColumn((1, 3, 6, 1, 4, 1, 1271, 2, 1, 28, 1, 1, 6, 1, 9), SsmStratumLevel()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cienaCesInputPUReceivedQL.setStatus('current')
cienaCesInputPUSsmEnabled = MibTableColumn((1, 3, 6, 1, 4, 1, 1271, 2, 1, 28, 1, 1, 6, 1, 10), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("unknown", 1), ("disabled", 2), ("enabled", 3)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: cienaCesInputPUSsmEnabled.setStatus('current')
cienaCesInputPUOperationalStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 1271, 2, 1, 28, 1, 1, 6, 1, 11), SyncRefOperationalStatus()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cienaCesInputPUOperationalStatus.setStatus('current')
cienaCesInputPUBITSSignalMode = MibTableColumn((1, 3, 6, 1, 4, 1, 1271, 2, 1, 28, 1, 1, 6, 1, 12), SyncBITSSignalMode()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cienaCesInputPUBITSSignalMode.setStatus('current')
cienaCesInputPUBITSSignalFormat = MibTableColumn((1, 3, 6, 1, 4, 1, 1271, 2, 1, 28, 1, 1, 6, 1, 13), SyncBITSSignalFormat()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cienaCesInputPUBITSSignalFormat.setStatus('current')
cienaCesInputPUBITSSignalEncoding = MibTableColumn((1, 3, 6, 1, 4, 1, 1271, 2, 1, 28, 1, 1, 6, 1, 14), SyncBITSSignalEncoding()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cienaCesInputPUBITSSignalEncoding.setStatus('current')
cienaCesSyncOutputTable = MibTable((1, 3, 6, 1, 4, 1, 1271, 2, 1, 28, 1, 1, 7), )
if mibBuilder.loadTexts: cienaCesSyncOutputTable.setStatus('current')
cienaCesSyncOutputEntry = MibTableRow((1, 3, 6, 1, 4, 1, 1271, 2, 1, 28, 1, 1, 7, 1), ).setIndexNames((0, "CIENA-CES-TIME-SYNC-MIB", "cienaCesOutputEntityId"))
if mibBuilder.loadTexts: cienaCesSyncOutputEntry.setStatus('current')
cienaCesOutputEntityId = MibTableColumn((1, 3, 6, 1, 4, 1, 1271, 2, 1, 28, 1, 1, 7, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 48)))
if mibBuilder.loadTexts: cienaCesOutputEntityId.setStatus('current')
cienaCesOutputEntityName = MibTableColumn((1, 3, 6, 1, 4, 1, 1271, 2, 1, 28, 1, 1, 7, 1, 2), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(1, 31))).setMaxAccess("readonly")
if mibBuilder.loadTexts: cienaCesOutputEntityName.setStatus('current')
cienaCesOutputTimingInterfaceName = MibTableColumn((1, 3, 6, 1, 4, 1, 1271, 2, 1, 28, 1, 1, 7, 1, 3), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(1, 31))).setMaxAccess("readonly")
if mibBuilder.loadTexts: cienaCesOutputTimingInterfaceName.setStatus('current')
cienaCesOutputTimingInterfaceProtocol = MibTableColumn((1, 3, 6, 1, 4, 1, 1271, 2, 1, 28, 1, 1, 7, 1, 4), SyncInterfaceProtocol()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cienaCesOutputTimingInterfaceProtocol.setStatus('current')
cienaCesOutputOperationalQL = MibTableColumn((1, 3, 6, 1, 4, 1, 1271, 2, 1, 28, 1, 1, 7, 1, 5), SsmStratumLevel()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cienaCesOutputOperationalQL.setStatus('current')
cienaCesOutputOperationalStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 1271, 2, 1, 28, 1, 1, 7, 1, 6), SyncRefOperationalStatus()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cienaCesOutputOperationalStatus.setStatus('current')
cienaCesOutputBITSSignalMode = MibTableColumn((1, 3, 6, 1, 4, 1, 1271, 2, 1, 28, 1, 1, 7, 1, 7), SyncBITSSignalMode()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cienaCesOutputBITSSignalMode.setStatus('current')
cienaCesOutputBITSSignalFormat = MibTableColumn((1, 3, 6, 1, 4, 1, 1271, 2, 1, 28, 1, 1, 7, 1, 8), SyncBITSSignalFormat()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cienaCesOutputBITSSignalFormat.setStatus('current')
cienaCesOutputBITSSignalEncoding = MibTableColumn((1, 3, 6, 1, 4, 1, 1271, 2, 1, 28, 1, 1, 7, 1, 9), SyncBITSSignalEncoding()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cienaCesOutputBITSSignalEncoding.setStatus('current')
cienaCesOutputBITSSignalLineBuildout = MibTableColumn((1, 3, 6, 1, 4, 1, 1271, 2, 1, 28, 1, 1, 7, 1, 10), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6))).clone(namedValues=NamedValues(("unknown", 1), ("lbo133", 2), ("lbo266", 3), ("lbo399", 4), ("lbo533", 5), ("lbo655", 6)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: cienaCesOutputBITSSignalLineBuildout.setStatus('current')
cienaCesOutputBITSSignalSsmLocation = MibTableColumn((1, 3, 6, 1, 4, 1, 1271, 2, 1, 28, 1, 1, 7, 1, 11), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5))).clone(namedValues=NamedValues(("unknown", 1), ("sa4", 2), ("sa5", 3), ("sa6", 4), ("sa7", 5)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: cienaCesOutputBITSSignalSsmLocation.setStatus('current')
cienaCesSyncInputPUStateChangeNotification = NotificationType((1, 3, 6, 1, 4, 1, 1271, 2, 2, 28, 0, 1)).setObjects(("CIENA-GLOBAL-MIB", "cienaGlobalSeverity"), ("CIENA-GLOBAL-MIB", "cienaGlobalMacAddress"), ("CIENA-CES-TIME-SYNC-MIB", "cienaCesInputPUEntityName"), ("CIENA-CES-TIME-SYNC-MIB", "cienaCesInputPUPGEntityName"), ("CIENA-CES-TIME-SYNC-MIB", "cienaCesInputPUTimingInterfaceName"), ("CIENA-CES-TIME-SYNC-MIB", "cienaCesInputPUTimingInterfaceProtocol"), ("CIENA-CES-TIME-SYNC-MIB", "cienaCesInputPUOperationalStatus"))
if mibBuilder.loadTexts: cienaCesSyncInputPUStateChangeNotification.setStatus('current')
cienaCesSyncInputProtectionGroupStateChangeNotification = NotificationType((1, 3, 6, 1, 4, 1, 1271, 2, 2, 28, 0, 2)).setObjects(("CIENA-GLOBAL-MIB", "cienaGlobalSeverity"), ("CIENA-GLOBAL-MIB", "cienaGlobalMacAddress"), ("CIENA-CES-TIME-SYNC-MIB", "cienaCesInputPGEntityName"), ("CIENA-CES-TIME-SYNC-MIB", "cienaCesInputPGOperationalStatus"))
if mibBuilder.loadTexts: cienaCesSyncInputProtectionGroupStateChangeNotification.setStatus('current')
mibBuilder.exportSymbols("CIENA-CES-TIME-SYNC-MIB", cienaCesOutputBITSSignalEncoding=cienaCesOutputBITSSignalEncoding, cienaCesInputPGStateDuration=cienaCesInputPGStateDuration, cienaCesInputPUEntityId=cienaCesInputPUEntityId, cienaCesSyncInputPUStateChangeNotification=cienaCesSyncInputPUStateChangeNotification, cienaCesSyncInputProtectionGroupEntry=cienaCesSyncInputProtectionGroupEntry, cienaCesInputPGThresholdQualityLevel=cienaCesInputPGThresholdQualityLevel, cienaCesTimeSyncMIBNotifications=cienaCesTimeSyncMIBNotifications, cienaCesSyncInputProtectionUnitTable=cienaCesSyncInputProtectionUnitTable, cienaCesOutputTimingInterfaceProtocol=cienaCesOutputTimingInterfaceProtocol, cienaCesSyncWaitToRestoreTimer=cienaCesSyncWaitToRestoreTimer, cienaCesTimeSyncMIBNotificationPrefix=cienaCesTimeSyncMIBNotificationPrefix, cienaCesInputPGOperationalStatus=cienaCesInputPGOperationalStatus, cienaCesInputPUSsmEnabled=cienaCesInputPUSsmEnabled, cienaCesOutputOperationalStatus=cienaCesOutputOperationalStatus, cienaCesInputPGPreferredReference=cienaCesInputPGPreferredReference, cienaCesInputPUPGEntityName=cienaCesInputPUPGEntityName, cienaCesInputPUBITSSignalEncoding=cienaCesInputPUBITSSignalEncoding, SsmStratumLevel=SsmStratumLevel, cienaCesSyncInputProtectionGroupStateChangeNotification=cienaCesSyncInputProtectionGroupStateChangeNotification, SyncBITSSignalEncoding=SyncBITSSignalEncoding, cienaCesInputPUBITSSignalFormat=cienaCesInputPUBITSSignalFormat, SyncInterfaceProtocol=SyncInterfaceProtocol, cienaCesInputPUOperationalQL=cienaCesInputPUOperationalQL, cienaCesSyncOptionType=cienaCesSyncOptionType, cienaCesOutputBITSSignalMode=cienaCesOutputBITSSignalMode, PYSNMP_MODULE_ID=cienaCesTimeSyncMIB, cienaCesOutputBITSSignalSsmLocation=cienaCesOutputBITSSignalSsmLocation, cienaCesInputPUForcedQL=cienaCesInputPUForcedQL, cienaCesSyncRevertiveMode=cienaCesSyncRevertiveMode, cienaCesOutputEntityId=cienaCesOutputEntityId, cienaCesInputPUOperationalStatus=cienaCesInputPUOperationalStatus, SyncBITSSignalMode=SyncBITSSignalMode, SyncRefOperationalStatus=SyncRefOperationalStatus, cienaCesSyncOutputEntry=cienaCesSyncOutputEntry, cienaCesTimeSyncMIB=cienaCesTimeSyncMIB, cienaCesInputPUTimingInterfaceName=cienaCesInputPUTimingInterfaceName, cienaCesInputPGForcedReference=cienaCesInputPGForcedReference, cienaCesOutputBITSSignalLineBuildout=cienaCesOutputBITSSignalLineBuildout, cienaCesInputPGEntityId=cienaCesInputPGEntityId, cienaCesInputPGEntityName=cienaCesInputPGEntityName, cienaCesInputPGReferenceSwitchCount=cienaCesInputPGReferenceSwitchCount, cienaCesSyncInputProtectionUnitEntry=cienaCesSyncInputProtectionUnitEntry, cienaCesInputPUBITSSignalMode=cienaCesInputPUBITSSignalMode, cienaCesOutputTimingInterfaceName=cienaCesOutputTimingInterfaceName, cienaCesTimeSyncMIBObjects=cienaCesTimeSyncMIBObjects, cienaCesSyncOutputTable=cienaCesSyncOutputTable, cienaCesSyncInputProtectionGroupTable=cienaCesSyncInputProtectionGroupTable, cienaCesInputPUUserPriority=cienaCesInputPUUserPriority, cienaCesInputPUReceivedQL=cienaCesInputPUReceivedQL, cienaCesInputPGState=cienaCesInputPGState, cienaCesInputPUTimingInterfaceProtocol=cienaCesInputPUTimingInterfaceProtocol, cienaCesSyncAdminState=cienaCesSyncAdminState, cienaCesInputPUEntityName=cienaCesInputPUEntityName, SyncBITSSignalFormat=SyncBITSSignalFormat, cienaCesOutputBITSSignalFormat=cienaCesOutputBITSSignalFormat, cienaCesOutputOperationalQL=cienaCesOutputOperationalQL, cienaCesInputPGSelectedReference=cienaCesInputPGSelectedReference, cienaCesOutputEntityName=cienaCesOutputEntityName, cienaCesTimeSyncObjects=cienaCesTimeSyncObjects)