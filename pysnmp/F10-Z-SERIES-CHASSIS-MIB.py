#
# PySNMP MIB module F10-Z-SERIES-CHASSIS-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/F10-Z-SERIES-CHASSIS-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 18:57:32 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
Integer, OctetString, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "Integer", "OctetString", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
SingleValueConstraint, ValueRangeConstraint, ConstraintsIntersection, ConstraintsUnion, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "SingleValueConstraint", "ValueRangeConstraint", "ConstraintsIntersection", "ConstraintsUnion", "ValueSizeConstraint")
f10Mgmt, = mibBuilder.importSymbols("FORCE10-SMI", "f10Mgmt")
F10HundredthdB, F10SSeriesPortType, F10SwDate, F10MfgDate, F10ProcessorModuleType, F10CardOperStatus, F10ChassisType = mibBuilder.importSymbols("FORCE10-TC", "F10HundredthdB", "F10SSeriesPortType", "F10SwDate", "F10MfgDate", "F10ProcessorModuleType", "F10CardOperStatus", "F10ChassisType")
ModuleCompliance, ObjectGroup, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "ObjectGroup", "NotificationGroup")
Bits, ModuleIdentity, iso, ObjectIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, Gauge32, Unsigned32, Counter32, Counter64, MibIdentifier, TimeTicks, IpAddress, NotificationType, Integer32 = mibBuilder.importSymbols("SNMPv2-SMI", "Bits", "ModuleIdentity", "iso", "ObjectIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Gauge32", "Unsigned32", "Counter32", "Counter64", "MibIdentifier", "TimeTicks", "IpAddress", "NotificationType", "Integer32")
DisplayString, MacAddress, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "MacAddress", "TextualConvention")
f10ZSerChassisMib = ModuleIdentity((1, 3, 6, 1, 4, 1, 6027, 3, 25))
f10ZSerChassisMib.setRevisions(('2014-04-16 12:00', '2013-10-10 12:00',))
if mibBuilder.loadTexts: f10ZSerChassisMib.setLastUpdated('201404161200Z')
if mibBuilder.loadTexts: f10ZSerChassisMib.setOrganization('Dell Inc.')
f10ZSerChassisObject = MibIdentifier((1, 3, 6, 1, 4, 1, 6027, 3, 25, 1))
chObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 6027, 3, 25, 1, 1))
chSysObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 6027, 3, 25, 1, 2))
chType = MibScalar((1, 3, 6, 1, 4, 1, 6027, 3, 25, 1, 1, 1), F10ChassisType()).setMaxAccess("readonly")
if mibBuilder.loadTexts: chType.setStatus('current')
chSwVersion = MibScalar((1, 3, 6, 1, 4, 1, 6027, 3, 25, 1, 1, 2), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 16))).setMaxAccess("readonly")
if mibBuilder.loadTexts: chSwVersion.setStatus('current')
chMacAddr = MibScalar((1, 3, 6, 1, 4, 1, 6027, 3, 25, 1, 1, 3), MacAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: chMacAddr.setStatus('current')
chSerialNumber = MibScalar((1, 3, 6, 1, 4, 1, 6027, 3, 25, 1, 1, 4), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 14))).setMaxAccess("readonly")
if mibBuilder.loadTexts: chSerialNumber.setStatus('current')
chPartNum = MibScalar((1, 3, 6, 1, 4, 1, 6027, 3, 25, 1, 1, 5), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 11))).setMaxAccess("readonly")
if mibBuilder.loadTexts: chPartNum.setStatus('current')
chProductRev = MibScalar((1, 3, 6, 1, 4, 1, 6027, 3, 25, 1, 1, 6), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 3))).setMaxAccess("readonly")
if mibBuilder.loadTexts: chProductRev.setStatus('current')
chVendorId = MibScalar((1, 3, 6, 1, 4, 1, 6027, 3, 25, 1, 1, 7), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 3))).setMaxAccess("readonly")
if mibBuilder.loadTexts: chVendorId.setStatus('current')
chMfgDate = MibScalar((1, 3, 6, 1, 4, 1, 6027, 3, 25, 1, 1, 8), F10MfgDate()).setMaxAccess("readonly")
if mibBuilder.loadTexts: chMfgDate.setStatus('current')
chCountryCode = MibScalar((1, 3, 6, 1, 4, 1, 6027, 3, 25, 1, 1, 9), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 2))).setMaxAccess("readonly")
if mibBuilder.loadTexts: chCountryCode.setStatus('current')
chPiecePartID = MibScalar((1, 3, 6, 1, 4, 1, 6027, 3, 25, 1, 1, 10), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 24))).setMaxAccess("readonly")
if mibBuilder.loadTexts: chPiecePartID.setStatus('current')
chPPIDRevision = MibScalar((1, 3, 6, 1, 4, 1, 6027, 3, 25, 1, 1, 11), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 3))).setMaxAccess("readonly")
if mibBuilder.loadTexts: chPPIDRevision.setStatus('current')
chServiceTag = MibScalar((1, 3, 6, 1, 4, 1, 6027, 3, 25, 1, 1, 12), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 7))).setMaxAccess("readonly")
if mibBuilder.loadTexts: chServiceTag.setStatus('current')
chExpressServiceCode = MibScalar((1, 3, 6, 1, 4, 1, 6027, 3, 25, 1, 1, 13), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 14))).setMaxAccess("readonly")
if mibBuilder.loadTexts: chExpressServiceCode.setStatus('current')
chNum10GigEtherPorts = MibScalar((1, 3, 6, 1, 4, 1, 6027, 3, 25, 1, 1, 14), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: chNum10GigEtherPorts.setStatus('current')
chNum40GigEtherPorts = MibScalar((1, 3, 6, 1, 4, 1, 6027, 3, 25, 1, 1, 15), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: chNum40GigEtherPorts.setStatus('current')
chNumLineCards = MibScalar((1, 3, 6, 1, 4, 1, 6027, 3, 25, 1, 1, 16), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: chNumLineCards.setStatus('current')
chNumFanTrays = MibScalar((1, 3, 6, 1, 4, 1, 6027, 3, 25, 1, 1, 17), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: chNumFanTrays.setStatus('current')
chNumPowerSupplies = MibScalar((1, 3, 6, 1, 4, 1, 6027, 3, 25, 1, 1, 18), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: chNumPowerSupplies.setStatus('current')
chSysProcessorTable = MibTable((1, 3, 6, 1, 4, 1, 6027, 3, 25, 1, 2, 1), )
if mibBuilder.loadTexts: chSysProcessorTable.setStatus('current')
chSysProcessorEntry = MibTableRow((1, 3, 6, 1, 4, 1, 6027, 3, 25, 1, 2, 1, 1), ).setIndexNames((0, "F10-Z-SERIES-CHASSIS-MIB", "chSysProcessorIndex"))
if mibBuilder.loadTexts: chSysProcessorEntry.setStatus('current')
chSysProcessorIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 6027, 3, 25, 1, 2, 1, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 5)))
if mibBuilder.loadTexts: chSysProcessorIndex.setStatus('current')
chSysProcessorType = MibTableColumn((1, 3, 6, 1, 4, 1, 6027, 3, 25, 1, 2, 1, 1, 2), F10ProcessorModuleType()).setMaxAccess("readonly")
if mibBuilder.loadTexts: chSysProcessorType.setStatus('current')
chSysProcessorUpTime = MibTableColumn((1, 3, 6, 1, 4, 1, 6027, 3, 25, 1, 2, 1, 1, 3), TimeTicks()).setMaxAccess("readonly")
if mibBuilder.loadTexts: chSysProcessorUpTime.setStatus('current')
chSysProcessorMemSize = MibTableColumn((1, 3, 6, 1, 4, 1, 6027, 3, 25, 1, 2, 1, 1, 4), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: chSysProcessorMemSize.setStatus('current')
chSysSwModuleTable = MibTable((1, 3, 6, 1, 4, 1, 6027, 3, 25, 1, 2, 2), )
if mibBuilder.loadTexts: chSysSwModuleTable.setStatus('current')
chSysSwModuleEntry = MibTableRow((1, 3, 6, 1, 4, 1, 6027, 3, 25, 1, 2, 2, 1), ).setIndexNames((0, "F10-Z-SERIES-CHASSIS-MIB", "chSysProcessorIndex"))
if mibBuilder.loadTexts: chSysSwModuleEntry.setStatus('current')
chSysSwModuleRuntimeImgVersion = MibTableColumn((1, 3, 6, 1, 4, 1, 6027, 3, 25, 1, 2, 2, 1, 1), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 16))).setMaxAccess("readonly")
if mibBuilder.loadTexts: chSysSwModuleRuntimeImgVersion.setStatus('current')
chSysSwModuleRuntimeImgDate = MibTableColumn((1, 3, 6, 1, 4, 1, 6027, 3, 25, 1, 2, 2, 1, 2), F10SwDate().subtype(subtypeSpec=ValueSizeConstraint(0, 10))).setMaxAccess("readonly")
if mibBuilder.loadTexts: chSysSwModuleRuntimeImgDate.setStatus('current')
chSysSwModuleBootFlashImgVersion = MibTableColumn((1, 3, 6, 1, 4, 1, 6027, 3, 25, 1, 2, 2, 1, 3), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 16))).setMaxAccess("readonly")
if mibBuilder.loadTexts: chSysSwModuleBootFlashImgVersion.setStatus('current')
chSysSwModuleBootSelectorImgVersion = MibTableColumn((1, 3, 6, 1, 4, 1, 6027, 3, 25, 1, 2, 2, 1, 4), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 16))).setMaxAccess("readonly")
if mibBuilder.loadTexts: chSysSwModuleBootSelectorImgVersion.setStatus('current')
chSysSwModuleNextRebootImage = MibTableColumn((1, 3, 6, 1, 4, 1, 6027, 3, 25, 1, 2, 2, 1, 5), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("partitionA", 1), ("partitionB", 2), ("networkBoot", 3)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: chSysSwModuleNextRebootImage.setStatus('current')
chSysSwModuleCurrentBootImage = MibTableColumn((1, 3, 6, 1, 4, 1, 6027, 3, 25, 1, 2, 2, 1, 6), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("partitionA", 1), ("partitionB", 2), ("networkBoot", 3)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: chSysSwModuleCurrentBootImage.setStatus('current')
chSysSwModuleInPartitionAImgVers = MibTableColumn((1, 3, 6, 1, 4, 1, 6027, 3, 25, 1, 2, 2, 1, 7), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 16))).setMaxAccess("readonly")
if mibBuilder.loadTexts: chSysSwModuleInPartitionAImgVers.setStatus('current')
chSysSwModuleInPartitionBImgVers = MibTableColumn((1, 3, 6, 1, 4, 1, 6027, 3, 25, 1, 2, 2, 1, 8), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 16))).setMaxAccess("readonly")
if mibBuilder.loadTexts: chSysSwModuleInPartitionBImgVers.setStatus('current')
chSysCpuUtilTable = MibTable((1, 3, 6, 1, 4, 1, 6027, 3, 25, 1, 2, 3), )
if mibBuilder.loadTexts: chSysCpuUtilTable.setStatus('current')
chSysCpuUtilEntry = MibTableRow((1, 3, 6, 1, 4, 1, 6027, 3, 25, 1, 2, 3, 1), ).setIndexNames((0, "F10-Z-SERIES-CHASSIS-MIB", "chSysProcessorIndex"))
if mibBuilder.loadTexts: chSysCpuUtilEntry.setStatus('current')
chSysCpuUtil5Sec = MibTableColumn((1, 3, 6, 1, 4, 1, 6027, 3, 25, 1, 2, 3, 1, 1), Gauge32().subtype(subtypeSpec=ValueRangeConstraint(0, 100))).setMaxAccess("readonly")
if mibBuilder.loadTexts: chSysCpuUtil5Sec.setStatus('current')
chSysCpuUtil1Min = MibTableColumn((1, 3, 6, 1, 4, 1, 6027, 3, 25, 1, 2, 3, 1, 2), Gauge32().subtype(subtypeSpec=ValueRangeConstraint(0, 100))).setMaxAccess("readonly")
if mibBuilder.loadTexts: chSysCpuUtil1Min.setStatus('current')
chSysCpuUtil5Min = MibTableColumn((1, 3, 6, 1, 4, 1, 6027, 3, 25, 1, 2, 3, 1, 3), Gauge32().subtype(subtypeSpec=ValueRangeConstraint(0, 100))).setMaxAccess("readonly")
if mibBuilder.loadTexts: chSysCpuUtil5Min.setStatus('current')
chSysCpuUtilMemUsage = MibTableColumn((1, 3, 6, 1, 4, 1, 6027, 3, 25, 1, 2, 3, 1, 4), Gauge32().subtype(subtypeSpec=ValueRangeConstraint(0, 100))).setMaxAccess("readonly")
if mibBuilder.loadTexts: chSysCpuUtilMemUsage.setStatus('current')
chSysCpuUtilFlashUsage = MibTableColumn((1, 3, 6, 1, 4, 1, 6027, 3, 25, 1, 2, 3, 1, 5), Gauge32().subtype(subtypeSpec=ValueRangeConstraint(0, 100))).setMaxAccess("readonly")
if mibBuilder.loadTexts: chSysCpuUtilFlashUsage.setStatus('current')
chSysLineCardTable = MibTable((1, 3, 6, 1, 4, 1, 6027, 3, 25, 1, 2, 4), )
if mibBuilder.loadTexts: chSysLineCardTable.setStatus('current')
chSysLineCardEntry = MibTableRow((1, 3, 6, 1, 4, 1, 6027, 3, 25, 1, 2, 4, 1), ).setIndexNames((0, "F10-Z-SERIES-CHASSIS-MIB", "chSysLineCardIndex"))
if mibBuilder.loadTexts: chSysLineCardEntry.setStatus('current')
chSysLineCardIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 6027, 3, 25, 1, 2, 4, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 3)))
if mibBuilder.loadTexts: chSysLineCardIndex.setStatus('current')
chSysLineCardType = MibTableColumn((1, 3, 6, 1, 4, 1, 6027, 3, 25, 1, 2, 4, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("z9500LC36", 1), ("z9500LC48", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: chSysLineCardType.setStatus('current')
chSysLineCardDescription = MibTableColumn((1, 3, 6, 1, 4, 1, 6027, 3, 25, 1, 2, 4, 1, 3), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 40))).setMaxAccess("readonly")
if mibBuilder.loadTexts: chSysLineCardDescription.setStatus('current')
chSysLineCardStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 6027, 3, 25, 1, 2, 4, 1, 4), F10CardOperStatus()).setMaxAccess("readonly")
if mibBuilder.loadTexts: chSysLineCardStatus.setStatus('current')
chSysLineCardTemp = MibTableColumn((1, 3, 6, 1, 4, 1, 6027, 3, 25, 1, 2, 4, 1, 5), Integer32()).setUnits('degrees Centigrade').setMaxAccess("readonly")
if mibBuilder.loadTexts: chSysLineCardTemp.setStatus('current')
chSysLineCardNum10GigEtherPorts = MibTableColumn((1, 3, 6, 1, 4, 1, 6027, 3, 25, 1, 2, 4, 1, 6), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: chSysLineCardNum10GigEtherPorts.setStatus('current')
chSysLineCardNum40GigEtherPorts = MibTableColumn((1, 3, 6, 1, 4, 1, 6027, 3, 25, 1, 2, 4, 1, 7), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: chSysLineCardNum40GigEtherPorts.setStatus('current')
chSysPortTable = MibTable((1, 3, 6, 1, 4, 1, 6027, 3, 25, 1, 2, 5), )
if mibBuilder.loadTexts: chSysPortTable.setStatus('current')
chSysPortEntry = MibTableRow((1, 3, 6, 1, 4, 1, 6027, 3, 25, 1, 2, 5, 1), ).setIndexNames((0, "F10-Z-SERIES-CHASSIS-MIB", "chSysLineCardIndex"), (0, "F10-Z-SERIES-CHASSIS-MIB", "chSysPortIndex"))
if mibBuilder.loadTexts: chSysPortEntry.setStatus('current')
chSysPortIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 6027, 3, 25, 1, 2, 5, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 192)))
if mibBuilder.loadTexts: chSysPortIndex.setStatus('current')
chSysPortType = MibTableColumn((1, 3, 6, 1, 4, 1, 6027, 3, 25, 1, 2, 5, 1, 2), F10SSeriesPortType()).setMaxAccess("readonly")
if mibBuilder.loadTexts: chSysPortType.setStatus('current')
chSysPortAdminStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 6027, 3, 25, 1, 2, 5, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("up", 1), ("down", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: chSysPortAdminStatus.setStatus('current')
chSysPortOperStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 6027, 3, 25, 1, 2, 5, 1, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6))).clone(namedValues=NamedValues(("ready", 1), ("portDown", 2), ("portProblem", 3), ("cardProblem", 4), ("cardDown", 5), ("notPresent", 6)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: chSysPortOperStatus.setStatus('current')
chSysPortIfIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 6027, 3, 25, 1, 2, 5, 1, 5), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: chSysPortIfIndex.setStatus('current')
chSysPortXfpRxPower = MibTableColumn((1, 3, 6, 1, 4, 1, 6027, 3, 25, 1, 2, 5, 1, 6), F10HundredthdB()).setUnits('dB').setMaxAccess("readonly")
if mibBuilder.loadTexts: chSysPortXfpRxPower.setStatus('current')
chSysPortXfpRxTemp = MibTableColumn((1, 3, 6, 1, 4, 1, 6027, 3, 25, 1, 2, 5, 1, 7), Integer32()).setUnits('degrees Centigrade').setMaxAccess("readonly")
if mibBuilder.loadTexts: chSysPortXfpRxTemp.setStatus('current')
chSysPortXfpTxPower = MibTableColumn((1, 3, 6, 1, 4, 1, 6027, 3, 25, 1, 2, 5, 1, 8), F10HundredthdB()).setUnits('dB').setMaxAccess("readonly")
if mibBuilder.loadTexts: chSysPortXfpTxPower.setStatus('current')
chSysPowerSupplyTable = MibTable((1, 3, 6, 1, 4, 1, 6027, 3, 25, 1, 2, 6), )
if mibBuilder.loadTexts: chSysPowerSupplyTable.setStatus('current')
chSysPowerSupplyEntry = MibTableRow((1, 3, 6, 1, 4, 1, 6027, 3, 25, 1, 2, 6, 1), ).setIndexNames((0, "F10-Z-SERIES-CHASSIS-MIB", "chSysPowerSupplyIndex"))
if mibBuilder.loadTexts: chSysPowerSupplyEntry.setStatus('current')
chSysPowerSupplyIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 6027, 3, 25, 1, 2, 6, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 4)))
if mibBuilder.loadTexts: chSysPowerSupplyIndex.setStatus('current')
chSysPowerSupplyOperStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 6027, 3, 25, 1, 2, 6, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("up", 1), ("down", 2), ("absent", 3)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: chSysPowerSupplyOperStatus.setStatus('current')
chSysPowerSupplyType = MibTableColumn((1, 3, 6, 1, 4, 1, 6027, 3, 25, 1, 2, 6, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("ac", 1), ("dc", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: chSysPowerSupplyType.setStatus('current')
chSysPowerSupplyPiecePartID = MibTableColumn((1, 3, 6, 1, 4, 1, 6027, 3, 25, 1, 2, 6, 1, 4), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 24))).setMaxAccess("readonly")
if mibBuilder.loadTexts: chSysPowerSupplyPiecePartID.setStatus('current')
chSysPowerSupplyPPIDRevision = MibTableColumn((1, 3, 6, 1, 4, 1, 6027, 3, 25, 1, 2, 6, 1, 5), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 3))).setMaxAccess("readonly")
if mibBuilder.loadTexts: chSysPowerSupplyPPIDRevision.setStatus('current')
chSysPowerSupplyServiceTag = MibTableColumn((1, 3, 6, 1, 4, 1, 6027, 3, 25, 1, 2, 6, 1, 6), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 7))).setMaxAccess("readonly")
if mibBuilder.loadTexts: chSysPowerSupplyServiceTag.setStatus('current')
chSysPowerSupplyExpressServiceCode = MibTableColumn((1, 3, 6, 1, 4, 1, 6027, 3, 25, 1, 2, 6, 1, 7), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 14))).setMaxAccess("readonly")
if mibBuilder.loadTexts: chSysPowerSupplyExpressServiceCode.setStatus('current')
chSysPowerSupplyUsage = MibTableColumn((1, 3, 6, 1, 4, 1, 6027, 3, 25, 1, 2, 6, 1, 8), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: chSysPowerSupplyUsage.setStatus('current')
chSysFanTrayTable = MibTable((1, 3, 6, 1, 4, 1, 6027, 3, 25, 1, 2, 7), )
if mibBuilder.loadTexts: chSysFanTrayTable.setStatus('current')
chSysFanTrayEntry = MibTableRow((1, 3, 6, 1, 4, 1, 6027, 3, 25, 1, 2, 7, 1), ).setIndexNames((0, "F10-Z-SERIES-CHASSIS-MIB", "chSysFanTrayIndex"))
if mibBuilder.loadTexts: chSysFanTrayEntry.setStatus('current')
chSysFanTrayIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 6027, 3, 25, 1, 2, 7, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 5)))
if mibBuilder.loadTexts: chSysFanTrayIndex.setStatus('current')
chSysFanTrayOperStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 6027, 3, 25, 1, 2, 7, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("up", 1), ("down", 2), ("absent", 3)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: chSysFanTrayOperStatus.setStatus('current')
chSysFanTrayPiecePartID = MibTableColumn((1, 3, 6, 1, 4, 1, 6027, 3, 25, 1, 2, 7, 1, 3), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 24))).setMaxAccess("readonly")
if mibBuilder.loadTexts: chSysFanTrayPiecePartID.setStatus('current')
chSysFanTrayPPIDRevision = MibTableColumn((1, 3, 6, 1, 4, 1, 6027, 3, 25, 1, 2, 7, 1, 4), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 3))).setMaxAccess("readonly")
if mibBuilder.loadTexts: chSysFanTrayPPIDRevision.setStatus('current')
chSysFanTrayServiceTag = MibTableColumn((1, 3, 6, 1, 4, 1, 6027, 3, 25, 1, 2, 7, 1, 5), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 7))).setMaxAccess("readonly")
if mibBuilder.loadTexts: chSysFanTrayServiceTag.setStatus('current')
chSysFanTrayExpressServiceCode = MibTableColumn((1, 3, 6, 1, 4, 1, 6027, 3, 25, 1, 2, 7, 1, 6), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 14))).setMaxAccess("readonly")
if mibBuilder.loadTexts: chSysFanTrayExpressServiceCode.setStatus('current')
chSysSwCoresTable = MibTable((1, 3, 6, 1, 4, 1, 6027, 3, 25, 1, 2, 8), )
if mibBuilder.loadTexts: chSysSwCoresTable.setStatus('current')
chSysCoresEntry = MibTableRow((1, 3, 6, 1, 4, 1, 6027, 3, 25, 1, 2, 8, 1), ).setIndexNames((0, "F10-Z-SERIES-CHASSIS-MIB", "chSysProcessorIndex"), (0, "F10-Z-SERIES-CHASSIS-MIB", "chSysCoresInstance"))
if mibBuilder.loadTexts: chSysCoresEntry.setStatus('current')
chSysCoresInstance = MibTableColumn((1, 3, 6, 1, 4, 1, 6027, 3, 25, 1, 2, 8, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: chSysCoresInstance.setStatus('current')
chSysCoresFileName = MibTableColumn((1, 3, 6, 1, 4, 1, 6027, 3, 25, 1, 2, 8, 1, 2), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: chSysCoresFileName.setStatus('current')
chSysCoresTimeCreated = MibTableColumn((1, 3, 6, 1, 4, 1, 6027, 3, 25, 1, 2, 8, 1, 3), F10SwDate()).setMaxAccess("readonly")
if mibBuilder.loadTexts: chSysCoresTimeCreated.setStatus('current')
chSysCoresProcessorName = MibTableColumn((1, 3, 6, 1, 4, 1, 6027, 3, 25, 1, 2, 8, 1, 4), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: chSysCoresProcessorName.setStatus('current')
chSysCoresProcess = MibTableColumn((1, 3, 6, 1, 4, 1, 6027, 3, 25, 1, 2, 8, 1, 5), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: chSysCoresProcess.setStatus('current')
f10ZSeriesChassisMibConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 6027, 3, 25, 2))
f10ZSeriesChassisMibCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 6027, 3, 25, 2, 1))
f10ZSeriesChassisMibGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 6027, 3, 25, 2, 2))
f10ZSeriesChassisMibCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 6027, 3, 25, 2, 1, 1)).setObjects(("F10-Z-SERIES-CHASSIS-MIB", "f10ZSeriesComponentGroup"), ("F10-Z-SERIES-CHASSIS-MIB", "f10ZSeriesSystemGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    f10ZSeriesChassisMibCompliance = f10ZSeriesChassisMibCompliance.setStatus('current')
f10ZSeriesComponentGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 6027, 3, 25, 2, 2, 1)).setObjects(("F10-Z-SERIES-CHASSIS-MIB", "chType"), ("F10-Z-SERIES-CHASSIS-MIB", "chSwVersion"), ("F10-Z-SERIES-CHASSIS-MIB", "chMacAddr"), ("F10-Z-SERIES-CHASSIS-MIB", "chSerialNumber"), ("F10-Z-SERIES-CHASSIS-MIB", "chPartNum"), ("F10-Z-SERIES-CHASSIS-MIB", "chProductRev"), ("F10-Z-SERIES-CHASSIS-MIB", "chVendorId"), ("F10-Z-SERIES-CHASSIS-MIB", "chMfgDate"), ("F10-Z-SERIES-CHASSIS-MIB", "chCountryCode"), ("F10-Z-SERIES-CHASSIS-MIB", "chPiecePartID"), ("F10-Z-SERIES-CHASSIS-MIB", "chPPIDRevision"), ("F10-Z-SERIES-CHASSIS-MIB", "chServiceTag"), ("F10-Z-SERIES-CHASSIS-MIB", "chExpressServiceCode"), ("F10-Z-SERIES-CHASSIS-MIB", "chNum10GigEtherPorts"), ("F10-Z-SERIES-CHASSIS-MIB", "chNum40GigEtherPorts"), ("F10-Z-SERIES-CHASSIS-MIB", "chNumLineCards"), ("F10-Z-SERIES-CHASSIS-MIB", "chNumFanTrays"), ("F10-Z-SERIES-CHASSIS-MIB", "chNumPowerSupplies"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    f10ZSeriesComponentGroup = f10ZSeriesComponentGroup.setStatus('current')
f10ZSeriesSystemGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 6027, 3, 25, 2, 2, 2)).setObjects(("F10-Z-SERIES-CHASSIS-MIB", "chSysProcessorType"), ("F10-Z-SERIES-CHASSIS-MIB", "chSysProcessorUpTime"), ("F10-Z-SERIES-CHASSIS-MIB", "chSysProcessorMemSize"), ("F10-Z-SERIES-CHASSIS-MIB", "chSysSwModuleRuntimeImgVersion"), ("F10-Z-SERIES-CHASSIS-MIB", "chSysSwModuleRuntimeImgDate"), ("F10-Z-SERIES-CHASSIS-MIB", "chSysSwModuleBootFlashImgVersion"), ("F10-Z-SERIES-CHASSIS-MIB", "chSysSwModuleBootSelectorImgVersion"), ("F10-Z-SERIES-CHASSIS-MIB", "chSysSwModuleNextRebootImage"), ("F10-Z-SERIES-CHASSIS-MIB", "chSysSwModuleCurrentBootImage"), ("F10-Z-SERIES-CHASSIS-MIB", "chSysSwModuleInPartitionAImgVers"), ("F10-Z-SERIES-CHASSIS-MIB", "chSysSwModuleInPartitionBImgVers"), ("F10-Z-SERIES-CHASSIS-MIB", "chSysCpuUtil5Sec"), ("F10-Z-SERIES-CHASSIS-MIB", "chSysCpuUtil1Min"), ("F10-Z-SERIES-CHASSIS-MIB", "chSysCpuUtil5Min"), ("F10-Z-SERIES-CHASSIS-MIB", "chSysCpuUtilMemUsage"), ("F10-Z-SERIES-CHASSIS-MIB", "chSysCpuUtilFlashUsage"), ("F10-Z-SERIES-CHASSIS-MIB", "chSysLineCardType"), ("F10-Z-SERIES-CHASSIS-MIB", "chSysLineCardDescription"), ("F10-Z-SERIES-CHASSIS-MIB", "chSysLineCardStatus"), ("F10-Z-SERIES-CHASSIS-MIB", "chSysLineCardTemp"), ("F10-Z-SERIES-CHASSIS-MIB", "chSysLineCardNum10GigEtherPorts"), ("F10-Z-SERIES-CHASSIS-MIB", "chSysLineCardNum40GigEtherPorts"), ("F10-Z-SERIES-CHASSIS-MIB", "chSysPortType"), ("F10-Z-SERIES-CHASSIS-MIB", "chSysPortAdminStatus"), ("F10-Z-SERIES-CHASSIS-MIB", "chSysPortOperStatus"), ("F10-Z-SERIES-CHASSIS-MIB", "chSysPortIfIndex"), ("F10-Z-SERIES-CHASSIS-MIB", "chSysPortXfpRxPower"), ("F10-Z-SERIES-CHASSIS-MIB", "chSysPortXfpRxTemp"), ("F10-Z-SERIES-CHASSIS-MIB", "chSysPortXfpTxPower"), ("F10-Z-SERIES-CHASSIS-MIB", "chSysPowerSupplyOperStatus"), ("F10-Z-SERIES-CHASSIS-MIB", "chSysPowerSupplyType"), ("F10-Z-SERIES-CHASSIS-MIB", "chSysPowerSupplyPiecePartID"), ("F10-Z-SERIES-CHASSIS-MIB", "chSysPowerSupplyPPIDRevision"), ("F10-Z-SERIES-CHASSIS-MIB", "chSysPowerSupplyServiceTag"), ("F10-Z-SERIES-CHASSIS-MIB", "chSysPowerSupplyExpressServiceCode"), ("F10-Z-SERIES-CHASSIS-MIB", "chSysPowerSupplyUsage"), ("F10-Z-SERIES-CHASSIS-MIB", "chSysFanTrayOperStatus"), ("F10-Z-SERIES-CHASSIS-MIB", "chSysFanTrayPiecePartID"), ("F10-Z-SERIES-CHASSIS-MIB", "chSysFanTrayPPIDRevision"), ("F10-Z-SERIES-CHASSIS-MIB", "chSysFanTrayServiceTag"), ("F10-Z-SERIES-CHASSIS-MIB", "chSysFanTrayExpressServiceCode"), ("F10-Z-SERIES-CHASSIS-MIB", "chSysCoresInstance"), ("F10-Z-SERIES-CHASSIS-MIB", "chSysCoresFileName"), ("F10-Z-SERIES-CHASSIS-MIB", "chSysCoresTimeCreated"), ("F10-Z-SERIES-CHASSIS-MIB", "chSysCoresProcessorName"), ("F10-Z-SERIES-CHASSIS-MIB", "chSysCoresProcess"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    f10ZSeriesSystemGroup = f10ZSeriesSystemGroup.setStatus('current')
mibBuilder.exportSymbols("F10-Z-SERIES-CHASSIS-MIB", f10ZSerChassisObject=f10ZSerChassisObject, chSysFanTrayIndex=chSysFanTrayIndex, chSysFanTrayPiecePartID=chSysFanTrayPiecePartID, chSysLineCardNum40GigEtherPorts=chSysLineCardNum40GigEtherPorts, chSysFanTrayEntry=chSysFanTrayEntry, f10ZSerChassisMib=f10ZSerChassisMib, chSysSwModuleNextRebootImage=chSysSwModuleNextRebootImage, chSysLineCardDescription=chSysLineCardDescription, chMacAddr=chMacAddr, chSysLineCardType=chSysLineCardType, chSysObjects=chSysObjects, chSysLineCardTable=chSysLineCardTable, chSysPortType=chSysPortType, chSysProcessorUpTime=chSysProcessorUpTime, chSysPortAdminStatus=chSysPortAdminStatus, chSysPowerSupplyPiecePartID=chSysPowerSupplyPiecePartID, chSysCoresFileName=chSysCoresFileName, chSysSwModuleBootSelectorImgVersion=chSysSwModuleBootSelectorImgVersion, chSysCpuUtilFlashUsage=chSysCpuUtilFlashUsage, chSysCoresProcess=chSysCoresProcess, chServiceTag=chServiceTag, chExpressServiceCode=chExpressServiceCode, chSwVersion=chSwVersion, chSysCoresInstance=chSysCoresInstance, chSysCpuUtil5Sec=chSysCpuUtil5Sec, chNumLineCards=chNumLineCards, chSysCpuUtilMemUsage=chSysCpuUtilMemUsage, chNumFanTrays=chNumFanTrays, chPiecePartID=chPiecePartID, chSysPowerSupplyType=chSysPowerSupplyType, chSysFanTrayServiceTag=chSysFanTrayServiceTag, chSysProcessorEntry=chSysProcessorEntry, chSysProcessorType=chSysProcessorType, chSysSwModuleInPartitionBImgVers=chSysSwModuleInPartitionBImgVers, f10ZSeriesComponentGroup=f10ZSeriesComponentGroup, chSysLineCardEntry=chSysLineCardEntry, chSysProcessorIndex=chSysProcessorIndex, chSysPortXfpRxPower=chSysPortXfpRxPower, chSysPortTable=chSysPortTable, chSysPowerSupplyUsage=chSysPowerSupplyUsage, f10ZSeriesChassisMibConformance=f10ZSeriesChassisMibConformance, chSysLineCardStatus=chSysLineCardStatus, chSerialNumber=chSerialNumber, chSysFanTrayTable=chSysFanTrayTable, chSysCpuUtilTable=chSysCpuUtilTable, chPPIDRevision=chPPIDRevision, chSysSwModuleEntry=chSysSwModuleEntry, chNumPowerSupplies=chNumPowerSupplies, chSysPowerSupplyExpressServiceCode=chSysPowerSupplyExpressServiceCode, chSysCoresEntry=chSysCoresEntry, chMfgDate=chMfgDate, chSysPowerSupplyTable=chSysPowerSupplyTable, f10ZSeriesChassisMibCompliances=f10ZSeriesChassisMibCompliances, chSysPowerSupplyServiceTag=chSysPowerSupplyServiceTag, chSysPowerSupplyEntry=chSysPowerSupplyEntry, chSysSwModuleInPartitionAImgVers=chSysSwModuleInPartitionAImgVers, chVendorId=chVendorId, chType=chType, chSysSwModuleRuntimeImgVersion=chSysSwModuleRuntimeImgVersion, chSysPowerSupplyIndex=chSysPowerSupplyIndex, chSysLineCardNum10GigEtherPorts=chSysLineCardNum10GigEtherPorts, chSysPortOperStatus=chSysPortOperStatus, chSysProcessorTable=chSysProcessorTable, chSysPortIndex=chSysPortIndex, chSysCpuUtil5Min=chSysCpuUtil5Min, chSysCoresTimeCreated=chSysCoresTimeCreated, chSysSwModuleRuntimeImgDate=chSysSwModuleRuntimeImgDate, chSysPowerSupplyPPIDRevision=chSysPowerSupplyPPIDRevision, f10ZSeriesSystemGroup=f10ZSeriesSystemGroup, chSysLineCardIndex=chSysLineCardIndex, chSysLineCardTemp=chSysLineCardTemp, f10ZSeriesChassisMibCompliance=f10ZSeriesChassisMibCompliance, chSysFanTrayExpressServiceCode=chSysFanTrayExpressServiceCode, chObjects=chObjects, chSysSwModuleBootFlashImgVersion=chSysSwModuleBootFlashImgVersion, PYSNMP_MODULE_ID=f10ZSerChassisMib, chNum10GigEtherPorts=chNum10GigEtherPorts, chSysFanTrayOperStatus=chSysFanTrayOperStatus, chSysProcessorMemSize=chSysProcessorMemSize, f10ZSeriesChassisMibGroups=f10ZSeriesChassisMibGroups, chSysCpuUtil1Min=chSysCpuUtil1Min, chSysPortXfpRxTemp=chSysPortXfpRxTemp, chProductRev=chProductRev, chSysPowerSupplyOperStatus=chSysPowerSupplyOperStatus, chCountryCode=chCountryCode, chSysCoresProcessorName=chSysCoresProcessorName, chSysSwCoresTable=chSysSwCoresTable, chSysPortXfpTxPower=chSysPortXfpTxPower, chSysCpuUtilEntry=chSysCpuUtilEntry, chSysSwModuleTable=chSysSwModuleTable, chSysPortIfIndex=chSysPortIfIndex, chSysFanTrayPPIDRevision=chSysFanTrayPPIDRevision, chPartNum=chPartNum, chSysSwModuleCurrentBootImage=chSysSwModuleCurrentBootImage, chNum40GigEtherPorts=chNum40GigEtherPorts, chSysPortEntry=chSysPortEntry)