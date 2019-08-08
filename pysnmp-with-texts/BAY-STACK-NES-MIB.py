#
# PySNMP MIB module BAY-STACK-NES-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/BAY-STACK-NES-MIB
# Produced by pysmi-0.3.4 at Wed May  1 11:35:52 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
OctetString, Integer, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "OctetString", "Integer", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsIntersection, SingleValueConstraint, ValueRangeConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsIntersection", "SingleValueConstraint", "ValueRangeConstraint", "ConstraintsUnion")
InterfaceIndex, = mibBuilder.importSymbols("IF-MIB", "InterfaceIndex")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
Gauge32, iso, ModuleIdentity, Bits, Integer32, Counter32, ObjectIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, IpAddress, Unsigned32, TimeTicks, Counter64, MibIdentifier, NotificationType = mibBuilder.importSymbols("SNMPv2-SMI", "Gauge32", "iso", "ModuleIdentity", "Bits", "Integer32", "Counter32", "ObjectIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "IpAddress", "Unsigned32", "TimeTicks", "Counter64", "MibIdentifier", "NotificationType")
DisplayString, RowStatus, TruthValue, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "RowStatus", "TruthValue", "TextualConvention")
bayStackMibs, = mibBuilder.importSymbols("SYNOPTICS-ROOT-MIB", "bayStackMibs")
bayStackNesMib = ModuleIdentity((1, 3, 6, 1, 4, 1, 45, 5, 34))
bayStackNesMib.setRevisions(('2014-08-22 00:00', '2009-05-19 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: bayStackNesMib.setRevisionsDescriptions(('v2: Changed organization to Avaya.', 'v1: Initial version.',))
if mibBuilder.loadTexts: bayStackNesMib.setLastUpdated('201408220000Z')
if mibBuilder.loadTexts: bayStackNesMib.setOrganization('Avaya')
if mibBuilder.loadTexts: bayStackNesMib.setContactInfo('Avaya')
if mibBuilder.loadTexts: bayStackNesMib.setDescription("Avaya Energy Saver (AES, formerly known as NES) MIB Copyright 2014 Avaya, Inc. All rights reserved. This Avaya SNMP Management Information Base Specification embodies Avaya' confidential and proprietary intellectual property. Avaya retains all title and ownership in the Specification, including any revisions. This Specification is supplied 'AS IS,' and Avaya makes no warranty, either express or implied, as to the use, operation, condition, or performance of the Specification.")
bayStackNesNotifications = MibIdentifier((1, 3, 6, 1, 4, 1, 45, 5, 34, 0))
bayStackNesObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 45, 5, 34, 1))
bayStackNesNotificationObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 45, 5, 34, 2))
bsnesScalars = MibIdentifier((1, 3, 6, 1, 4, 1, 45, 5, 34, 1, 1))
bsnesEnergySaverEnabled = MibScalar((1, 3, 6, 1, 4, 1, 45, 5, 34, 1, 1, 1), TruthValue()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: bsnesEnergySaverEnabled.setStatus('current')
if mibBuilder.loadTexts: bsnesEnergySaverEnabled.setDescription('This object controls whether the Avaya Energy Saver feature is enabled.')
bsnesPoePowerSavingEnabled = MibScalar((1, 3, 6, 1, 4, 1, 45, 5, 34, 1, 1, 2), TruthValue()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: bsnesPoePowerSavingEnabled.setStatus('current')
if mibBuilder.loadTexts: bsnesPoePowerSavingEnabled.setDescription('This object controls whether Avaya Energy Saver POE power saving is enabled.')
bsnesEfficiencyModeEnabled = MibScalar((1, 3, 6, 1, 4, 1, 45, 5, 34, 1, 1, 3), TruthValue()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: bsnesEfficiencyModeEnabled.setStatus('current')
if mibBuilder.loadTexts: bsnesEfficiencyModeEnabled.setDescription('This object controls whether Avaya Energy Saver Efficiency-Mode is enabled.')
bsnesEnergySaverActive = MibScalar((1, 3, 6, 1, 4, 1, 45, 5, 34, 1, 1, 4), TruthValue()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: bsnesEnergySaverActive.setStatus('current')
if mibBuilder.loadTexts: bsnesEnergySaverActive.setDescription('This object controls whether Avaya Energy Saver is currently active. A value of true(1) indicates energy saving is active. A value of false(2) indicates energy saving is currently inactive. The value of this object will change over time as specified by the energy saving schedule. Setting this object allows energy saving to be manually activated or deactivated.')
bsnesScheduleTable = MibTable((1, 3, 6, 1, 4, 1, 45, 5, 34, 1, 2), )
if mibBuilder.loadTexts: bsnesScheduleTable.setStatus('current')
if mibBuilder.loadTexts: bsnesScheduleTable.setDescription('This table contains the schedule for activation and deactivation of the Avaya Energy Saver feature.')
bsnesScheduleEntry = MibTableRow((1, 3, 6, 1, 4, 1, 45, 5, 34, 1, 2, 1), ).setIndexNames((0, "BAY-STACK-NES-MIB", "bsnesScheduleDay"), (0, "BAY-STACK-NES-MIB", "bsnesScheduleHour"), (0, "BAY-STACK-NES-MIB", "bsnesScheduleMinute"))
if mibBuilder.loadTexts: bsnesScheduleEntry.setStatus('current')
if mibBuilder.loadTexts: bsnesScheduleEntry.setDescription('An energy saver schedule entry, indicates a time to activate or deactivate energy savings.')
bsnesScheduleDay = MibTableColumn((1, 3, 6, 1, 4, 1, 45, 5, 34, 1, 2, 1, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7))).clone(namedValues=NamedValues(("monday", 1), ("tuesday", 2), ("wednesday", 3), ("thursday", 4), ("friday", 5), ("saturday", 6), ("sunday", 7))))
if mibBuilder.loadTexts: bsnesScheduleDay.setStatus('current')
if mibBuilder.loadTexts: bsnesScheduleDay.setDescription('Day on which this schedule entry takes effect.')
bsnesScheduleHour = MibTableColumn((1, 3, 6, 1, 4, 1, 45, 5, 34, 1, 2, 1, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 23)))
if mibBuilder.loadTexts: bsnesScheduleHour.setStatus('current')
if mibBuilder.loadTexts: bsnesScheduleHour.setDescription('Hour on which this schedule entry takes effect. A value of 0 means 12am midnight. A value of 12 means 12pm noon.')
bsnesScheduleMinute = MibTableColumn((1, 3, 6, 1, 4, 1, 45, 5, 34, 1, 2, 1, 3), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 59)))
if mibBuilder.loadTexts: bsnesScheduleMinute.setStatus('current')
if mibBuilder.loadTexts: bsnesScheduleMinute.setDescription('Minute on which this schedule entry takes effect.')
bsnesScheduleAction = MibTableColumn((1, 3, 6, 1, 4, 1, 45, 5, 34, 1, 2, 1, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("activate", 1), ("deactivate", 2)))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: bsnesScheduleAction.setStatus('current')
if mibBuilder.loadTexts: bsnesScheduleAction.setDescription('The action taken when this schedule entry takes effect. Indicates whether energy savings will be activated or deactivated.')
bsnesScheduleRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 45, 5, 34, 1, 2, 1, 5), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: bsnesScheduleRowStatus.setStatus('current')
if mibBuilder.loadTexts: bsnesScheduleRowStatus.setDescription('Used to create/delete schedule entries.')
bsnesInterfaceTable = MibTable((1, 3, 6, 1, 4, 1, 45, 5, 34, 1, 3), )
if mibBuilder.loadTexts: bsnesInterfaceTable.setStatus('current')
if mibBuilder.loadTexts: bsnesInterfaceTable.setDescription('This table contains per-port NES settings.')
bsnesInterfaceEntry = MibTableRow((1, 3, 6, 1, 4, 1, 45, 5, 34, 1, 3, 1), ).setIndexNames((0, "BAY-STACK-NES-MIB", "bsnesInterfaceIndex"))
if mibBuilder.loadTexts: bsnesInterfaceEntry.setStatus('current')
if mibBuilder.loadTexts: bsnesInterfaceEntry.setDescription('NES settings for a port.')
bsnesInterfaceIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 45, 5, 34, 1, 3, 1, 1), InterfaceIndex())
if mibBuilder.loadTexts: bsnesInterfaceIndex.setStatus('current')
if mibBuilder.loadTexts: bsnesInterfaceIndex.setDescription('The ifIndex value of an interface.')
bsnesInterfaceEnergySaverEnabled = MibTableColumn((1, 3, 6, 1, 4, 1, 45, 5, 34, 1, 3, 1, 2), TruthValue()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: bsnesInterfaceEnergySaverEnabled.setStatus('current')
if mibBuilder.loadTexts: bsnesInterfaceEnergySaverEnabled.setDescription('Indicates whether the Avaya Energy Saver feature is enabled for this interface.')
bsnesInterfaceEnergySaverPoeStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 45, 5, 34, 1, 3, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("enabled", 1), ("disabled", 2), ("notApplicable", 3)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: bsnesInterfaceEnergySaverPoeStatus.setStatus('current')
if mibBuilder.loadTexts: bsnesInterfaceEnergySaverPoeStatus.setDescription('Indicates the Avaya Energy Saver PoE status for this interface.')
bsnesSavingsTable = MibTable((1, 3, 6, 1, 4, 1, 45, 5, 34, 1, 4), )
if mibBuilder.loadTexts: bsnesSavingsTable.setStatus('current')
if mibBuilder.loadTexts: bsnesSavingsTable.setDescription('This table contains per-unit information about the amount of power being saved by NES.')
bsnesSavingsEntry = MibTableRow((1, 3, 6, 1, 4, 1, 45, 5, 34, 1, 4, 1), ).setIndexNames((0, "BAY-STACK-NES-MIB", "bsnesSavingsUnitIndex"))
if mibBuilder.loadTexts: bsnesSavingsEntry.setStatus('current')
if mibBuilder.loadTexts: bsnesSavingsEntry.setDescription('Information about the amount of power being saved for a unit.')
bsnesSavingsUnitIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 45, 5, 34, 1, 4, 1, 1), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(1, 8)))
if mibBuilder.loadTexts: bsnesSavingsUnitIndex.setStatus('current')
if mibBuilder.loadTexts: bsnesSavingsUnitIndex.setDescription('The unit number.')
bsnesSavingsUnitSavings = MibTableColumn((1, 3, 6, 1, 4, 1, 45, 5, 34, 1, 4, 1, 2), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: bsnesSavingsUnitSavings.setStatus('current')
if mibBuilder.loadTexts: bsnesSavingsUnitSavings.setDescription('Indicates the amount of switch capacity power being saved on this unit. The value of this object is 1/10 watts.')
bsnesSavingsPoeSavings = MibTableColumn((1, 3, 6, 1, 4, 1, 45, 5, 34, 1, 4, 1, 3), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: bsnesSavingsPoeSavings.setStatus('current')
if mibBuilder.loadTexts: bsnesSavingsPoeSavings.setDescription('Indicates the amount of PoE power being saved on this unit. The value of this object is 1/10 watts.')
bsnesGloballyEnabled = NotificationType((1, 3, 6, 1, 4, 1, 45, 5, 34, 0, 1))
if mibBuilder.loadTexts: bsnesGloballyEnabled.setStatus('current')
if mibBuilder.loadTexts: bsnesGloballyEnabled.setDescription('Indicates that NES was globally enabled.')
bsnesGloballyDisabled = NotificationType((1, 3, 6, 1, 4, 1, 45, 5, 34, 0, 2))
if mibBuilder.loadTexts: bsnesGloballyDisabled.setStatus('current')
if mibBuilder.loadTexts: bsnesGloballyDisabled.setDescription('Indicates that NES was globally disabled.')
bsnesManuallyActivated = NotificationType((1, 3, 6, 1, 4, 1, 45, 5, 34, 0, 3))
if mibBuilder.loadTexts: bsnesManuallyActivated.setStatus('current')
if mibBuilder.loadTexts: bsnesManuallyActivated.setDescription('Indicates that NES was manually activated.')
bsnesManuallyDeactivated = NotificationType((1, 3, 6, 1, 4, 1, 45, 5, 34, 0, 4))
if mibBuilder.loadTexts: bsnesManuallyDeactivated.setStatus('current')
if mibBuilder.loadTexts: bsnesManuallyDeactivated.setDescription('Indicates that NES was manually deactived.')
bsnesScheduleNotApplied = NotificationType((1, 3, 6, 1, 4, 1, 45, 5, 34, 0, 5))
if mibBuilder.loadTexts: bsnesScheduleNotApplied.setStatus('current')
if mibBuilder.loadTexts: bsnesScheduleNotApplied.setDescription('Indicates that a schedule was not applied because SNTP in not synchronized.')
bsnesScheduleApplied = NotificationType((1, 3, 6, 1, 4, 1, 45, 5, 34, 0, 6))
if mibBuilder.loadTexts: bsnesScheduleApplied.setStatus('current')
if mibBuilder.loadTexts: bsnesScheduleApplied.setDescription('Indicates that SNTP is synchronized and that the schedule is being applied.')
bsnesActivated = NotificationType((1, 3, 6, 1, 4, 1, 45, 5, 34, 0, 7))
if mibBuilder.loadTexts: bsnesActivated.setStatus('current')
if mibBuilder.loadTexts: bsnesActivated.setDescription('Indicates that NES was activated by schedule.')
bsnesDeactivated = NotificationType((1, 3, 6, 1, 4, 1, 45, 5, 34, 0, 8))
if mibBuilder.loadTexts: bsnesDeactivated.setStatus('current')
if mibBuilder.loadTexts: bsnesDeactivated.setDescription('Indicates that NES was deactivated by schedule.')
mibBuilder.exportSymbols("BAY-STACK-NES-MIB", bsnesSavingsUnitSavings=bsnesSavingsUnitSavings, bsnesInterfaceIndex=bsnesInterfaceIndex, bsnesSavingsTable=bsnesSavingsTable, bsnesScheduleHour=bsnesScheduleHour, bayStackNesObjects=bayStackNesObjects, bsnesManuallyDeactivated=bsnesManuallyDeactivated, bayStackNesMib=bayStackNesMib, bsnesScheduleNotApplied=bsnesScheduleNotApplied, bsnesScheduleMinute=bsnesScheduleMinute, bsnesGloballyDisabled=bsnesGloballyDisabled, bsnesScalars=bsnesScalars, bsnesInterfaceEnergySaverEnabled=bsnesInterfaceEnergySaverEnabled, bsnesScheduleRowStatus=bsnesScheduleRowStatus, bsnesGloballyEnabled=bsnesGloballyEnabled, bsnesEnergySaverEnabled=bsnesEnergySaverEnabled, bsnesDeactivated=bsnesDeactivated, bsnesPoePowerSavingEnabled=bsnesPoePowerSavingEnabled, PYSNMP_MODULE_ID=bayStackNesMib, bayStackNesNotificationObjects=bayStackNesNotificationObjects, bsnesSavingsUnitIndex=bsnesSavingsUnitIndex, bsnesInterfaceEnergySaverPoeStatus=bsnesInterfaceEnergySaverPoeStatus, bsnesSavingsEntry=bsnesSavingsEntry, bsnesScheduleAction=bsnesScheduleAction, bsnesSavingsPoeSavings=bsnesSavingsPoeSavings, bayStackNesNotifications=bayStackNesNotifications, bsnesManuallyActivated=bsnesManuallyActivated, bsnesInterfaceEntry=bsnesInterfaceEntry, bsnesInterfaceTable=bsnesInterfaceTable, bsnesEnergySaverActive=bsnesEnergySaverActive, bsnesEfficiencyModeEnabled=bsnesEfficiencyModeEnabled, bsnesActivated=bsnesActivated, bsnesScheduleEntry=bsnesScheduleEntry, bsnesScheduleDay=bsnesScheduleDay, bsnesScheduleApplied=bsnesScheduleApplied, bsnesScheduleTable=bsnesScheduleTable)