#
# PySNMP MIB module CISCO-WAN-VISM-TONE-PLAN-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/CISCO-WAN-VISM-TONE-PLAN-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 18:02:23 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
OctetString, Integer, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "OctetString", "Integer", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ValueSizeConstraint, SingleValueConstraint, ValueRangeConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ValueSizeConstraint", "SingleValueConstraint", "ValueRangeConstraint", "ConstraintsUnion")
ciscoWan, = mibBuilder.importSymbols("CISCOWAN-SMI", "ciscoWan")
ModuleCompliance, NotificationGroup, ObjectGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup", "ObjectGroup")
IpAddress, Counter32, TimeTicks, Gauge32, Unsigned32, MibIdentifier, Bits, iso, ObjectIdentity, Counter64, ModuleIdentity, NotificationType, MibScalar, MibTable, MibTableRow, MibTableColumn, Integer32 = mibBuilder.importSymbols("SNMPv2-SMI", "IpAddress", "Counter32", "TimeTicks", "Gauge32", "Unsigned32", "MibIdentifier", "Bits", "iso", "ObjectIdentity", "Counter64", "ModuleIdentity", "NotificationType", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Integer32")
RowStatus, DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "RowStatus", "DisplayString", "TextualConvention")
vismTonePlanGrpMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 351, 150, 24))
vismTonePlanGrpMIB.setRevisions(('2003-12-17 00:00', '2003-04-23 00:00', '2002-07-19 00:00', '2001-12-26 00:00', '2001-08-05 00:00', '2001-04-03 00:00',))
if mibBuilder.loadTexts: vismTonePlanGrpMIB.setLastUpdated('200312170000Z')
if mibBuilder.loadTexts: vismTonePlanGrpMIB.setOrganization('Cisco Systems, Inc.')
vismTonePlanGrpMIBObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 351, 150, 24, 1))
vismTonePlan = MibIdentifier((1, 3, 6, 1, 4, 1, 351, 150, 24, 1, 1))
vismTonePlanControlGrp = MibIdentifier((1, 3, 6, 1, 4, 1, 351, 150, 24, 1, 1, 1))
vismTonePlanTableGrp = MibIdentifier((1, 3, 6, 1, 4, 1, 351, 150, 24, 1, 1, 2))
vismConfigToneDetectGrp = MibIdentifier((1, 3, 6, 1, 4, 1, 351, 150, 24, 1, 1, 3))
vismSequentialToneDetectGrp = MibIdentifier((1, 3, 6, 1, 4, 1, 351, 150, 24, 1, 1, 4))
tonePlanCurrentSize = MibScalar((1, 3, 6, 1, 4, 1, 351, 150, 24, 1, 1, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: tonePlanCurrentSize.setStatus('current')
vismTonePlanTable = MibTable((1, 3, 6, 1, 4, 1, 351, 150, 24, 1, 1, 2, 1), )
if mibBuilder.loadTexts: vismTonePlanTable.setStatus('current')
vismTonePlanEntry = MibTableRow((1, 3, 6, 1, 4, 1, 351, 150, 24, 1, 1, 2, 1, 1), ).setIndexNames((0, "CISCO-WAN-VISM-TONE-PLAN-MIB", "tonePlanIndex"))
if mibBuilder.loadTexts: vismTonePlanEntry.setStatus('current')
tonePlanIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 351, 150, 24, 1, 1, 2, 1, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 1000)))
if mibBuilder.loadTexts: tonePlanIndex.setStatus('current')
tonePlanEntryStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 351, 150, 24, 1, 1, 2, 1, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))).clone(namedValues=NamedValues(("unused", 1), ("configured", 2), ("reloading", 3), ("lostFile", 4))).clone('unused')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: tonePlanEntryStatus.setStatus('current')
tonePlanProvisionFlag = MibTableColumn((1, 3, 6, 1, 4, 1, 351, 150, 24, 1, 1, 2, 1, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("builtIn", 1), ("provisionable", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: tonePlanProvisionFlag.setStatus('current')
tonePlanRegionName = MibTableColumn((1, 3, 6, 1, 4, 1, 351, 150, 24, 1, 1, 2, 1, 1, 4), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(1, 64))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: tonePlanRegionName.setStatus('current')
tonePlanVersionNumber = MibTableColumn((1, 3, 6, 1, 4, 1, 351, 150, 24, 1, 1, 2, 1, 1, 5), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 65535))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: tonePlanVersionNumber.setStatus('current')
tonePlanFileName = MibTableColumn((1, 3, 6, 1, 4, 1, 351, 150, 24, 1, 1, 2, 1, 1, 6), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(1, 32))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: tonePlanFileName.setStatus('current')
vismConfigToneDetectTable = MibTable((1, 3, 6, 1, 4, 1, 351, 150, 24, 1, 1, 3, 1), )
if mibBuilder.loadTexts: vismConfigToneDetectTable.setStatus('current')
vismConfigToneDetectEntry = MibTableRow((1, 3, 6, 1, 4, 1, 351, 150, 24, 1, 1, 3, 1, 1), ).setIndexNames((0, "CISCO-WAN-VISM-TONE-PLAN-MIB", "vismConfigToneDetectNum"))
if mibBuilder.loadTexts: vismConfigToneDetectEntry.setStatus('current')
vismConfigToneDetectNum = MibTableColumn((1, 3, 6, 1, 4, 1, 351, 150, 24, 1, 1, 3, 1, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 10))).setMaxAccess("readonly")
if mibBuilder.loadTexts: vismConfigToneDetectNum.setStatus('current')
vismEventCode = MibTableColumn((1, 3, 6, 1, 4, 1, 351, 150, 24, 1, 1, 3, 1, 1, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 255))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: vismEventCode.setStatus('current')
vismConfigToneDetectRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 351, 150, 24, 1, 1, 3, 1, 1, 3), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: vismConfigToneDetectRowStatus.setStatus('current')
vismFreqMaxDeviation = MibTableColumn((1, 3, 6, 1, 4, 1, 351, 150, 24, 1, 1, 3, 1, 1, 4), Integer32().subtype(subtypeSpec=ValueRangeConstraint(10, 125)).clone(30)).setUnits('Hz').setMaxAccess("readcreate")
if mibBuilder.loadTexts: vismFreqMaxDeviation.setStatus('current')
vismFreqMaxPower = MibTableColumn((1, 3, 6, 1, 4, 1, 351, 150, 24, 1, 1, 3, 1, 1, 5), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 30))).setUnits('dB').setMaxAccess("readcreate")
if mibBuilder.loadTexts: vismFreqMaxPower.setStatus('current')
vismFreqMinPower = MibTableColumn((1, 3, 6, 1, 4, 1, 351, 150, 24, 1, 1, 3, 1, 1, 6), Integer32().subtype(subtypeSpec=ValueRangeConstraint(10, 35)).clone(35)).setUnits('dB').setMaxAccess("readcreate")
if mibBuilder.loadTexts: vismFreqMinPower.setStatus('current')
vismFreqPowerTwist = MibTableColumn((1, 3, 6, 1, 4, 1, 351, 150, 24, 1, 1, 3, 1, 1, 7), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 15)).clone(10)).setUnits('dB').setMaxAccess("readcreate")
if mibBuilder.loadTexts: vismFreqPowerTwist.setStatus('current')
vismFreqMaxDelay = MibTableColumn((1, 3, 6, 1, 4, 1, 351, 150, 24, 1, 1, 3, 1, 1, 8), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 100)).clone(10)).setUnits('milliseconds').setMaxAccess("readcreate")
if mibBuilder.loadTexts: vismFreqMaxDelay.setStatus('current')
vismMinOnCadence = MibTableColumn((1, 3, 6, 1, 4, 1, 351, 150, 24, 1, 1, 3, 1, 1, 9), Integer32().subtype(subtypeSpec=ValueRangeConstraint(3, 100)).clone(20)).setUnits('milliseconds').setMaxAccess("readcreate")
if mibBuilder.loadTexts: vismMinOnCadence.setStatus('current')
vismMaxOffCadence = MibTableColumn((1, 3, 6, 1, 4, 1, 351, 150, 24, 1, 1, 3, 1, 1, 10), Integer32().subtype(subtypeSpec=ValueRangeConstraint(5, 5000)).clone(450)).setMaxAccess("readcreate")
if mibBuilder.loadTexts: vismMaxOffCadence.setStatus('current')
vismFreqNumOfCadenceMatch = MibTableColumn((1, 3, 6, 1, 4, 1, 351, 150, 24, 1, 1, 3, 1, 1, 11), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 6)).clone(1)).setMaxAccess("readcreate")
if mibBuilder.loadTexts: vismFreqNumOfCadenceMatch.setStatus('current')
vismFrequency1 = MibTableColumn((1, 3, 6, 1, 4, 1, 351, 150, 24, 1, 1, 3, 1, 1, 12), Integer32().subtype(subtypeSpec=ValueRangeConstraint(280, 3800))).setUnits('Hz').setMaxAccess("readcreate")
if mibBuilder.loadTexts: vismFrequency1.setStatus('current')
vismFrequency2 = MibTableColumn((1, 3, 6, 1, 4, 1, 351, 150, 24, 1, 1, 3, 1, 1, 13), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 3800))).setUnits('Hz').setMaxAccess("readcreate")
if mibBuilder.loadTexts: vismFrequency2.setStatus('current')
vismFreqOnCadence = MibTableColumn((1, 3, 6, 1, 4, 1, 351, 150, 24, 1, 1, 3, 1, 1, 14), Integer32().subtype(subtypeSpec=ValueRangeConstraint(3, 5000))).setUnits('milliseconds').setMaxAccess("readcreate")
if mibBuilder.loadTexts: vismFreqOnCadence.setStatus('current')
vismFreqOffCadence = MibTableColumn((1, 3, 6, 1, 4, 1, 351, 150, 24, 1, 1, 3, 1, 1, 15), Integer32().subtype(subtypeSpec=ValueRangeConstraint(5, 5000))).setUnits('milliseconds').setMaxAccess("readcreate")
if mibBuilder.loadTexts: vismFreqOffCadence.setStatus('current')
seqToneNumOfFrequencies = MibScalar((1, 3, 6, 1, 4, 1, 351, 150, 24, 1, 1, 4, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 10)).clone(3)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: seqToneNumOfFrequencies.setStatus('current')
seqToneEventID = MibScalar((1, 3, 6, 1, 4, 1, 351, 150, 24, 1, 1, 4, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 255)).clone(74)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: seqToneEventID.setStatus('current')
seqToneDurationOfEachTone = MibScalar((1, 3, 6, 1, 4, 1, 351, 150, 24, 1, 1, 4, 3), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 65534)).clone(33)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: seqToneDurationOfEachTone.setStatus('current')
seqToneGapBetweenEachTone = MibScalar((1, 3, 6, 1, 4, 1, 351, 150, 24, 1, 1, 4, 4), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 65534)).clone(1)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: seqToneGapBetweenEachTone.setStatus('current')
seqToneDurationDeviation = MibScalar((1, 3, 6, 1, 4, 1, 351, 150, 24, 1, 1, 4, 5), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 4095)).clone(2)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: seqToneDurationDeviation.setStatus('current')
seqToneMaximumGapDuration = MibScalar((1, 3, 6, 1, 4, 1, 351, 150, 24, 1, 1, 4, 6), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 4095)).clone(15)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: seqToneMaximumGapDuration.setStatus('current')
seqToneGapDurationDeviation = MibScalar((1, 3, 6, 1, 4, 1, 351, 150, 24, 1, 1, 4, 7), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 4095)).clone(20)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: seqToneGapDurationDeviation.setStatus('current')
seqToneFreqDeviation = MibScalar((1, 3, 6, 1, 4, 1, 351, 150, 24, 1, 1, 4, 8), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 1000)).clone(40)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: seqToneFreqDeviation.setStatus('current')
seqTonePowerLevelCeiling = MibScalar((1, 3, 6, 1, 4, 1, 351, 150, 24, 1, 1, 4, 9), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 40)).clone(3)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: seqTonePowerLevelCeiling.setStatus('current')
seqTonePowerLevelFloor = MibScalar((1, 3, 6, 1, 4, 1, 351, 150, 24, 1, 1, 4, 10), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 40)).clone(40)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: seqTonePowerLevelFloor.setStatus('current')
seqToneFrequency1 = MibScalar((1, 3, 6, 1, 4, 1, 351, 150, 24, 1, 1, 4, 11), Integer32().subtype(subtypeSpec=ValueRangeConstraint(280, 3800)).clone(950)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: seqToneFrequency1.setStatus('current')
seqToneFrequency2 = MibScalar((1, 3, 6, 1, 4, 1, 351, 150, 24, 1, 1, 4, 12), Integer32().subtype(subtypeSpec=ValueRangeConstraint(280, 3800)).clone(1400)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: seqToneFrequency2.setStatus('current')
seqToneFrequency3 = MibScalar((1, 3, 6, 1, 4, 1, 351, 150, 24, 1, 1, 4, 13), Integer32().subtype(subtypeSpec=ValueRangeConstraint(280, 3800)).clone(1800)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: seqToneFrequency3.setStatus('current')
seqToneFrequency4 = MibScalar((1, 3, 6, 1, 4, 1, 351, 150, 24, 1, 1, 4, 14), Integer32().subtype(subtypeSpec=ValueRangeConstraint(280, 3800)).clone(280)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: seqToneFrequency4.setStatus('current')
seqToneFrequency5 = MibScalar((1, 3, 6, 1, 4, 1, 351, 150, 24, 1, 1, 4, 15), Integer32().subtype(subtypeSpec=ValueRangeConstraint(280, 3800)).clone(280)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: seqToneFrequency5.setStatus('current')
seqToneFrequency6 = MibScalar((1, 3, 6, 1, 4, 1, 351, 150, 24, 1, 1, 4, 16), Integer32().subtype(subtypeSpec=ValueRangeConstraint(280, 3800)).clone(280)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: seqToneFrequency6.setStatus('current')
seqToneFrequency7 = MibScalar((1, 3, 6, 1, 4, 1, 351, 150, 24, 1, 1, 4, 17), Integer32().subtype(subtypeSpec=ValueRangeConstraint(280, 3800)).clone(280)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: seqToneFrequency7.setStatus('current')
seqToneFrequency8 = MibScalar((1, 3, 6, 1, 4, 1, 351, 150, 24, 1, 1, 4, 18), Integer32().subtype(subtypeSpec=ValueRangeConstraint(280, 3800)).clone(280)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: seqToneFrequency8.setStatus('current')
seqToneFrequency9 = MibScalar((1, 3, 6, 1, 4, 1, 351, 150, 24, 1, 1, 4, 19), Integer32().subtype(subtypeSpec=ValueRangeConstraint(280, 3800)).clone(280)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: seqToneFrequency9.setStatus('current')
seqToneFrequency10 = MibScalar((1, 3, 6, 1, 4, 1, 351, 150, 24, 1, 1, 4, 20), Integer32().subtype(subtypeSpec=ValueRangeConstraint(280, 3800)).clone(280)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: seqToneFrequency10.setStatus('current')
vismToneNotificationPrefix = MibIdentifier((1, 3, 6, 1, 4, 1, 351, 150, 24, 2))
vismToneNotifications = MibIdentifier((1, 3, 6, 1, 4, 1, 351, 150, 24, 2, 0))
vismTonePlanMIBConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 351, 150, 24, 3))
vismTonePlanMIBCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 351, 150, 24, 3, 1))
vismTonePlanMIBGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 351, 150, 24, 3, 2))
vismTonePlanMIBCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 351, 150, 24, 3, 1, 1)).setObjects(("CISCO-WAN-VISM-TONE-PLAN-MIB", "vismTonePlanControlGroup"), ("CISCO-WAN-VISM-TONE-PLAN-MIB", "vismTonePlanTableGroup"), ("CISCO-WAN-VISM-TONE-PLAN-MIB", "vismConfigToneDetectTableGroup"), ("CISCO-WAN-VISM-TONE-PLAN-MIB", "vismSequentialToneDetectGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    vismTonePlanMIBCompliance = vismTonePlanMIBCompliance.setStatus('current')
vismTonePlanControlGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 351, 150, 24, 3, 2, 1)).setObjects(("CISCO-WAN-VISM-TONE-PLAN-MIB", "tonePlanCurrentSize"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    vismTonePlanControlGroup = vismTonePlanControlGroup.setStatus('current')
vismTonePlanTableGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 351, 150, 24, 3, 2, 2)).setObjects(("CISCO-WAN-VISM-TONE-PLAN-MIB", "tonePlanEntryStatus"), ("CISCO-WAN-VISM-TONE-PLAN-MIB", "tonePlanProvisionFlag"), ("CISCO-WAN-VISM-TONE-PLAN-MIB", "tonePlanRegionName"), ("CISCO-WAN-VISM-TONE-PLAN-MIB", "tonePlanVersionNumber"), ("CISCO-WAN-VISM-TONE-PLAN-MIB", "tonePlanFileName"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    vismTonePlanTableGroup = vismTonePlanTableGroup.setStatus('current')
vismConfigToneDetectTableGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 351, 150, 24, 3, 2, 3)).setObjects(("CISCO-WAN-VISM-TONE-PLAN-MIB", "vismConfigToneDetectNum"), ("CISCO-WAN-VISM-TONE-PLAN-MIB", "vismEventCode"), ("CISCO-WAN-VISM-TONE-PLAN-MIB", "vismConfigToneDetectRowStatus"), ("CISCO-WAN-VISM-TONE-PLAN-MIB", "vismFreqMaxDeviation"), ("CISCO-WAN-VISM-TONE-PLAN-MIB", "vismFreqMaxPower"), ("CISCO-WAN-VISM-TONE-PLAN-MIB", "vismFreqMinPower"), ("CISCO-WAN-VISM-TONE-PLAN-MIB", "vismFreqPowerTwist"), ("CISCO-WAN-VISM-TONE-PLAN-MIB", "vismFreqMaxDelay"), ("CISCO-WAN-VISM-TONE-PLAN-MIB", "vismMinOnCadence"), ("CISCO-WAN-VISM-TONE-PLAN-MIB", "vismMaxOffCadence"), ("CISCO-WAN-VISM-TONE-PLAN-MIB", "vismFreqNumOfCadenceMatch"), ("CISCO-WAN-VISM-TONE-PLAN-MIB", "vismFrequency1"), ("CISCO-WAN-VISM-TONE-PLAN-MIB", "vismFrequency2"), ("CISCO-WAN-VISM-TONE-PLAN-MIB", "vismFreqOnCadence"), ("CISCO-WAN-VISM-TONE-PLAN-MIB", "vismFreqOffCadence"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    vismConfigToneDetectTableGroup = vismConfigToneDetectTableGroup.setStatus('current')
vismSequentialToneDetectGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 351, 150, 24, 3, 2, 4)).setObjects(("CISCO-WAN-VISM-TONE-PLAN-MIB", "seqToneNumOfFrequencies"), ("CISCO-WAN-VISM-TONE-PLAN-MIB", "seqToneEventID"), ("CISCO-WAN-VISM-TONE-PLAN-MIB", "seqToneDurationOfEachTone"), ("CISCO-WAN-VISM-TONE-PLAN-MIB", "seqToneGapBetweenEachTone"), ("CISCO-WAN-VISM-TONE-PLAN-MIB", "seqToneDurationDeviation"), ("CISCO-WAN-VISM-TONE-PLAN-MIB", "seqToneMaximumGapDuration"), ("CISCO-WAN-VISM-TONE-PLAN-MIB", "seqToneGapDurationDeviation"), ("CISCO-WAN-VISM-TONE-PLAN-MIB", "seqToneFreqDeviation"), ("CISCO-WAN-VISM-TONE-PLAN-MIB", "seqTonePowerLevelCeiling"), ("CISCO-WAN-VISM-TONE-PLAN-MIB", "seqTonePowerLevelFloor"), ("CISCO-WAN-VISM-TONE-PLAN-MIB", "seqToneFrequency1"), ("CISCO-WAN-VISM-TONE-PLAN-MIB", "seqToneFrequency2"), ("CISCO-WAN-VISM-TONE-PLAN-MIB", "seqToneFrequency3"), ("CISCO-WAN-VISM-TONE-PLAN-MIB", "seqToneFrequency4"), ("CISCO-WAN-VISM-TONE-PLAN-MIB", "seqToneFrequency5"), ("CISCO-WAN-VISM-TONE-PLAN-MIB", "seqToneFrequency6"), ("CISCO-WAN-VISM-TONE-PLAN-MIB", "seqToneFrequency7"), ("CISCO-WAN-VISM-TONE-PLAN-MIB", "seqToneFrequency8"), ("CISCO-WAN-VISM-TONE-PLAN-MIB", "seqToneFrequency9"), ("CISCO-WAN-VISM-TONE-PLAN-MIB", "seqToneFrequency10"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    vismSequentialToneDetectGroup = vismSequentialToneDetectGroup.setStatus('current')
mibBuilder.exportSymbols("CISCO-WAN-VISM-TONE-PLAN-MIB", vismFreqPowerTwist=vismFreqPowerTwist, seqTonePowerLevelFloor=seqTonePowerLevelFloor, vismTonePlanGrpMIB=vismTonePlanGrpMIB, tonePlanRegionName=tonePlanRegionName, vismFrequency1=vismFrequency1, vismConfigToneDetectTable=vismConfigToneDetectTable, seqToneFrequency7=seqToneFrequency7, seqToneMaximumGapDuration=seqToneMaximumGapDuration, vismMinOnCadence=vismMinOnCadence, seqTonePowerLevelCeiling=seqTonePowerLevelCeiling, seqToneNumOfFrequencies=seqToneNumOfFrequencies, tonePlanEntryStatus=tonePlanEntryStatus, seqToneDurationDeviation=seqToneDurationDeviation, vismConfigToneDetectEntry=vismConfigToneDetectEntry, vismTonePlanControlGroup=vismTonePlanControlGroup, vismTonePlanMIBCompliance=vismTonePlanMIBCompliance, vismFreqMaxPower=vismFreqMaxPower, vismFrequency2=vismFrequency2, seqToneFrequency4=seqToneFrequency4, seqToneFrequency9=seqToneFrequency9, seqToneFreqDeviation=seqToneFreqDeviation, seqToneFrequency1=seqToneFrequency1, vismTonePlanMIBCompliances=vismTonePlanMIBCompliances, vismSequentialToneDetectGrp=vismSequentialToneDetectGrp, tonePlanVersionNumber=tonePlanVersionNumber, vismFreqOnCadence=vismFreqOnCadence, vismToneNotifications=vismToneNotifications, vismFreqNumOfCadenceMatch=vismFreqNumOfCadenceMatch, vismConfigToneDetectGrp=vismConfigToneDetectGrp, vismConfigToneDetectRowStatus=vismConfigToneDetectRowStatus, seqToneFrequency2=seqToneFrequency2, tonePlanCurrentSize=tonePlanCurrentSize, vismFreqMinPower=vismFreqMinPower, seqToneEventID=seqToneEventID, vismSequentialToneDetectGroup=vismSequentialToneDetectGroup, vismMaxOffCadence=vismMaxOffCadence, vismTonePlanControlGrp=vismTonePlanControlGrp, PYSNMP_MODULE_ID=vismTonePlanGrpMIB, seqToneGapBetweenEachTone=seqToneGapBetweenEachTone, vismConfigToneDetectNum=vismConfigToneDetectNum, vismEventCode=vismEventCode, seqToneFrequency8=seqToneFrequency8, seqToneGapDurationDeviation=seqToneGapDurationDeviation, seqToneFrequency6=seqToneFrequency6, tonePlanFileName=tonePlanFileName, vismTonePlan=vismTonePlan, vismTonePlanMIBConformance=vismTonePlanMIBConformance, seqToneFrequency3=seqToneFrequency3, vismTonePlanEntry=vismTonePlanEntry, vismTonePlanGrpMIBObjects=vismTonePlanGrpMIBObjects, tonePlanIndex=tonePlanIndex, seqToneFrequency5=seqToneFrequency5, vismTonePlanTableGroup=vismTonePlanTableGroup, vismTonePlanTableGrp=vismTonePlanTableGrp, vismToneNotificationPrefix=vismToneNotificationPrefix, vismTonePlanTable=vismTonePlanTable, vismTonePlanMIBGroups=vismTonePlanMIBGroups, vismFreqOffCadence=vismFreqOffCadence, vismFreqMaxDelay=vismFreqMaxDelay, seqToneDurationOfEachTone=seqToneDurationOfEachTone, seqToneFrequency10=seqToneFrequency10, tonePlanProvisionFlag=tonePlanProvisionFlag, vismFreqMaxDeviation=vismFreqMaxDeviation, vismConfigToneDetectTableGroup=vismConfigToneDetectTableGroup)