#
# PySNMP MIB module HUAWEI-POE-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/HUAWEI-POE-MIB
# Produced by pysmi-0.3.4 at Wed May  1 13:47:48 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
SingleValueConstraint, ConstraintsIntersection, ConstraintsUnion, ValueRangeConstraint, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "SingleValueConstraint", "ConstraintsIntersection", "ConstraintsUnion", "ValueRangeConstraint", "ValueSizeConstraint")
hwDatacomm, = mibBuilder.importSymbols("HUAWEI-MIB", "hwDatacomm")
InterfaceIndex, = mibBuilder.importSymbols("IF-MIB", "InterfaceIndex")
EnabledStatus, = mibBuilder.importSymbols("P-BRIDGE-MIB", "EnabledStatus")
NotificationGroup, ModuleCompliance, ObjectGroup = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance", "ObjectGroup")
NotificationType, Bits, MibIdentifier, IpAddress, TimeTicks, iso, Unsigned32, Integer32, Gauge32, ModuleIdentity, Counter32, MibScalar, MibTable, MibTableRow, MibTableColumn, ObjectIdentity, Counter64 = mibBuilder.importSymbols("SNMPv2-SMI", "NotificationType", "Bits", "MibIdentifier", "IpAddress", "TimeTicks", "iso", "Unsigned32", "Integer32", "Gauge32", "ModuleIdentity", "Counter32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "ObjectIdentity", "Counter64")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
hwPoeMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 2011, 5, 25, 195))
if mibBuilder.loadTexts: hwPoeMIB.setLastUpdated('200908241133Z')
if mibBuilder.loadTexts: hwPoeMIB.setOrganization('Huawei Technologies co.,Ltd.')
if mibBuilder.loadTexts: hwPoeMIB.setContactInfo('R&D BeiJing, Huawei Technologies co.,Ltd. Huawei Bld.,NO.3 Xinxi Rd., Shang-Di Information Industry Base, Hai-Dian District Beijing P.R. China Zip:100085 Http://www.huawei.com E-mail:support@huawei.com')
if mibBuilder.loadTexts: hwPoeMIB.setDescription('The HUAWEI-POE-MIB contains objects to manage POE.')
hwPoeGlobalObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 5, 25, 195, 1))
hwPoePower = MibScalar((1, 3, 6, 1, 4, 1, 2011, 5, 25, 195, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hwPoePower.setStatus('current')
if mibBuilder.loadTexts: hwPoePower.setDescription('This object identifies the maximum POE power of the system.')
hwPoePowerRsvPercent = MibScalar((1, 3, 6, 1, 4, 1, 2011, 5, 25, 195, 1, 4), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hwPoePowerRsvPercent.setStatus('current')
if mibBuilder.loadTexts: hwPoePowerRsvPercent.setDescription('This object identifies the reserved percent of total POE power.')
hwPoePowerUtilizationThreshold = MibScalar((1, 3, 6, 1, 4, 1, 2011, 5, 25, 195, 1, 5), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hwPoePowerUtilizationThreshold.setStatus('current')
if mibBuilder.loadTexts: hwPoePowerUtilizationThreshold.setDescription('This object identifies the utilization threshold of total POE power.')
hwPoeSlotTable = MibTable((1, 3, 6, 1, 4, 1, 2011, 5, 25, 195, 2), )
if mibBuilder.loadTexts: hwPoeSlotTable.setStatus('current')
if mibBuilder.loadTexts: hwPoeSlotTable.setDescription('This object indicates the slot configuration table of POE.')
hwPoeSlotEntry = MibTableRow((1, 3, 6, 1, 4, 1, 2011, 5, 25, 195, 2, 1), ).setIndexNames((0, "HUAWEI-POE-MIB", "hwPoeSlotId"))
if mibBuilder.loadTexts: hwPoeSlotEntry.setStatus('current')
if mibBuilder.loadTexts: hwPoeSlotEntry.setDescription('This object indicates the entry of the slot configuration table of POE.')
hwPoeSlotId = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 5, 25, 195, 2, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 8)))
if mibBuilder.loadTexts: hwPoeSlotId.setStatus('current')
if mibBuilder.loadTexts: hwPoeSlotId.setDescription('This object identifies the slot ID.')
hwPoeSlotMaximumPower = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 5, 25, 195, 2, 1, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 1600000)).clone(1776000)).setUnits('mW').setMaxAccess("readwrite")
if mibBuilder.loadTexts: hwPoeSlotMaximumPower.setStatus('current')
if mibBuilder.loadTexts: hwPoeSlotMaximumPower.setDescription('This object identifies the maximum power set by users. The value is expressed in mW.')
hwPoeSlotAvailablePower = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 5, 25, 195, 2, 1, 3), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hwPoeSlotAvailablePower.setStatus('current')
if mibBuilder.loadTexts: hwPoeSlotAvailablePower.setDescription('This object idenfies the available Power. The value is expressed in mW.')
hwPoeSlotReferencePower = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 5, 25, 195, 2, 1, 4), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hwPoeSlotReferencePower.setStatus('current')
if mibBuilder.loadTexts: hwPoeSlotReferencePower.setDescription('This object identifies the total reference power of a slot. The value is expressed in mW.')
hwPoeSlotConsumingPower = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 5, 25, 195, 2, 1, 5), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hwPoeSlotConsumingPower.setStatus('current')
if mibBuilder.loadTexts: hwPoeSlotConsumingPower.setDescription('This object identifies the total consuming power of a slot. The value is expressed in mW.')
hwPoeSlotPeakPower = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 5, 25, 195, 2, 1, 6), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hwPoeSlotPeakPower.setStatus('current')
if mibBuilder.loadTexts: hwPoeSlotPeakPower.setDescription('This object identifies the total peak power of a slot. The value is expressed in mW.')
hwPoeSlotLegacyDetect = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 5, 25, 195, 2, 1, 7), EnabledStatus().clone('disabled')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hwPoeSlotLegacyDetect.setStatus('current')
if mibBuilder.loadTexts: hwPoeSlotLegacyDetect.setDescription('This object indicates the compatibility detection of a non-standard device. (1:enable; 2:disable(default))')
hwPoeSlotPowerManagementManner = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 5, 25, 195, 2, 1, 8), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("manual", 1), ("auto", 2))).clone('auto')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hwPoeSlotPowerManagementManner.setStatus('current')
if mibBuilder.loadTexts: hwPoeSlotPowerManagementManner.setDescription('This object identifies the power management manner. (1:manual, 2:auto(default)).')
hwPoeSlotIsPoeDevice = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 5, 25, 195, 2, 1, 9), OctetString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hwPoeSlotIsPoeDevice.setStatus('current')
if mibBuilder.loadTexts: hwPoeSlotIsPoeDevice.setDescription('This object indicates whether the device supports PoE.')
hwPoeDimmId = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 5, 25, 195, 2, 1, 10), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 1))).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: hwPoeDimmId.setStatus('current')
if mibBuilder.loadTexts: hwPoeDimmId.setDescription('This object identifies the DIMM ID.')
hwPoeSlotPowerRsvPercent = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 5, 25, 195, 2, 1, 11), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hwPoeSlotPowerRsvPercent.setStatus('current')
if mibBuilder.loadTexts: hwPoeSlotPowerRsvPercent.setDescription('This object identifies the reserved percent of POE power in slot.')
hwPoeSlotPowerUtilizationThreshold = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 5, 25, 195, 2, 1, 12), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hwPoeSlotPowerUtilizationThreshold.setStatus('current')
if mibBuilder.loadTexts: hwPoeSlotPowerUtilizationThreshold.setDescription('This object identifies the utilization threshold of total POE power in slot.')
hwPoePortTable = MibTable((1, 3, 6, 1, 4, 1, 2011, 5, 25, 195, 3), )
if mibBuilder.loadTexts: hwPoePortTable.setStatus('current')
if mibBuilder.loadTexts: hwPoePortTable.setDescription('This object indicates the table that contains the configuration parameters of a POE interface. One entry corresponds to a POE interface.')
hwPoePortEntry = MibTableRow((1, 3, 6, 1, 4, 1, 2011, 5, 25, 195, 3, 1), ).setIndexNames((0, "HUAWEI-POE-MIB", "hwPoePortIfIndex"))
if mibBuilder.loadTexts: hwPoePortEntry.setStatus('current')
if mibBuilder.loadTexts: hwPoePortEntry.setDescription('This object indicates the entry of POE Port Table.')
hwPoePortIfIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 5, 25, 195, 3, 1, 1), InterfaceIndex())
if mibBuilder.loadTexts: hwPoePortIfIndex.setStatus('current')
if mibBuilder.loadTexts: hwPoePortIfIndex.setDescription('This object indicates the interface index.')
hwPoePortName = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 5, 25, 195, 3, 1, 2), OctetString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hwPoePortName.setStatus('current')
if mibBuilder.loadTexts: hwPoePortName.setDescription('This object indicates the interface name.')
hwPoePortEnable = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 5, 25, 195, 3, 1, 3), EnabledStatus().clone()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hwPoePortEnable.setStatus('current')
if mibBuilder.loadTexts: hwPoePortEnable.setDescription('This object indicates the enabling status of an interface. (1:enable(default); 2:disable)')
hwPoePortPriority = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 5, 25, 195, 3, 1, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("critical", 1), ("high", 2), ("low", 3))).clone('low')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hwPoePortPriority.setStatus('current')
if mibBuilder.loadTexts: hwPoePortPriority.setDescription('This object identifies the priority of an interface. (1:critical, 2:high, 3:low(default))')
hwPoePortMaximumPower = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 5, 25, 195, 3, 1, 5), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 30000)).clone(37000)).setUnits('mW').setMaxAccess("readwrite")
if mibBuilder.loadTexts: hwPoePortMaximumPower.setStatus('current')
if mibBuilder.loadTexts: hwPoePortMaximumPower.setDescription('This object identifies the maximum power of an interface.The value is expressed in mW.')
hwPoePortPowerOnStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 5, 25, 195, 3, 1, 6), OctetString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hwPoePortPowerOnStatus.setStatus('current')
if mibBuilder.loadTexts: hwPoePortPowerOnStatus.setDescription('This object indicates the powering status of an interface.')
hwPoePortPowerStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 5, 25, 195, 3, 1, 7), OctetString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hwPoePortPowerStatus.setStatus('current')
if mibBuilder.loadTexts: hwPoePortPowerStatus.setDescription('This object indicates the status of an interface.')
hwPoePortPdClass = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 5, 25, 195, 3, 1, 8), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 7))).setMaxAccess("readonly")
if mibBuilder.loadTexts: hwPoePortPdClass.setStatus('current')
if mibBuilder.loadTexts: hwPoePortPdClass.setDescription('This object identifies the class of a PD.')
hwPoePortReferencePower = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 5, 25, 195, 3, 1, 9), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 30000))).setMaxAccess("readonly")
if mibBuilder.loadTexts: hwPoePortReferencePower.setStatus('current')
if mibBuilder.loadTexts: hwPoePortReferencePower.setDescription('This object identifies the guaranteed power of an interface. The value is expressed in mW.')
hwPoePortConsumingPower = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 5, 25, 195, 3, 1, 10), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 30000))).setMaxAccess("readonly")
if mibBuilder.loadTexts: hwPoePortConsumingPower.setStatus('current')
if mibBuilder.loadTexts: hwPoePortConsumingPower.setDescription('This object identifies the consuming power of an interface. The value is expressed in mW.')
hwPoePortPeakPower = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 5, 25, 195, 3, 1, 11), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 30000))).setMaxAccess("readonly")
if mibBuilder.loadTexts: hwPoePortPeakPower.setStatus('current')
if mibBuilder.loadTexts: hwPoePortPeakPower.setDescription('This object identifies the peak power of an interface. The value is expressed in mW.')
hwPoePortAveragePower = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 5, 25, 195, 3, 1, 12), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 30000))).setMaxAccess("readonly")
if mibBuilder.loadTexts: hwPoePortAveragePower.setStatus('current')
if mibBuilder.loadTexts: hwPoePortAveragePower.setDescription('This object identifies the average power of an interface. The value is expressed in mW.')
hwPoePortCurrent = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 5, 25, 195, 3, 1, 13), OctetString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hwPoePortCurrent.setStatus('current')
if mibBuilder.loadTexts: hwPoePortCurrent.setDescription('This object indicates the current of an interface. The value is expressed in mA.')
hwPoePortVoltage = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 5, 25, 195, 3, 1, 14), OctetString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hwPoePortVoltage.setStatus('current')
if mibBuilder.loadTexts: hwPoePortVoltage.setDescription('This object indicates the voltage of an interface. The value is expressed in V.')
hwPoePortManualOperation = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 5, 25, 195, 3, 1, 15), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("powerOff", 1), ("powerOn", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hwPoePortManualOperation.setStatus('current')
if mibBuilder.loadTexts: hwPoePortManualOperation.setDescription('This object indicates that a PD connected to an interface is powered on or powered off manually.')
hwPoeTrapObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 5, 25, 195, 39))
hwPoePdPriority = MibScalar((1, 3, 6, 1, 4, 1, 2011, 5, 25, 195, 39, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("critical", 1), ("high", 2), ("low", 3)))).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: hwPoePdPriority.setStatus('current')
if mibBuilder.loadTexts: hwPoePdPriority.setDescription('This object identifies the PD priority.(1:critical, 2:high, 3:low(default))')
hwPoeSlotNum = MibScalar((1, 3, 6, 1, 4, 1, 2011, 5, 25, 195, 39, 2), Integer32()).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: hwPoeSlotNum.setStatus('current')
if mibBuilder.loadTexts: hwPoeSlotNum.setDescription('This object identifies the slot ID.')
hwPoeCurConsumPower = MibScalar((1, 3, 6, 1, 4, 1, 2011, 5, 25, 195, 39, 3), Integer32()).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: hwPoeCurConsumPower.setStatus('current')
if mibBuilder.loadTexts: hwPoeCurConsumPower.setDescription('This object identifies the current consuming power.')
hwPoeConsumPowerThreshold = MibScalar((1, 3, 6, 1, 4, 1, 2011, 5, 25, 195, 39, 4), Integer32()).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: hwPoeConsumPowerThreshold.setStatus('current')
if mibBuilder.loadTexts: hwPoeConsumPowerThreshold.setDescription('This object identifies the threshold of consuming power.')
hwPoeDeviceID = MibScalar((1, 3, 6, 1, 4, 1, 2011, 5, 25, 195, 39, 5), Integer32()).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: hwPoeDeviceID.setStatus('current')
if mibBuilder.loadTexts: hwPoeDeviceID.setDescription('This object identifies the device ID.')
hwFrameID = MibScalar((1, 3, 6, 1, 4, 1, 2011, 5, 25, 195, 39, 6), Integer32()).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: hwFrameID.setStatus('current')
if mibBuilder.loadTexts: hwFrameID.setDescription('This object identifies the CSS Frame ID.')
hwPoeNotification = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 5, 25, 195, 40))
hwPoeDimmError = NotificationType((1, 3, 6, 1, 4, 1, 2011, 5, 25, 195, 40, 1)).setObjects(("HUAWEI-POE-MIB", "hwPoeSlotNum"), ("HUAWEI-POE-MIB", "hwPoeDimmId"))
if mibBuilder.loadTexts: hwPoeDimmError.setStatus('current')
if mibBuilder.loadTexts: hwPoeDimmError.setDescription('This object indicates the Dimm chip error.')
hwPoePowerOff = NotificationType((1, 3, 6, 1, 4, 1, 2011, 5, 25, 195, 40, 2)).setObjects(("HUAWEI-POE-MIB", "hwPoePortName"))
if mibBuilder.loadTexts: hwPoePowerOff.setStatus('current')
if mibBuilder.loadTexts: hwPoePowerOff.setDescription('This object indicates a PD connected to an interface is powered off.')
hwPoePowerOn = NotificationType((1, 3, 6, 1, 4, 1, 2011, 5, 25, 195, 40, 3)).setObjects(("HUAWEI-POE-MIB", "hwPoePortName"))
if mibBuilder.loadTexts: hwPoePowerOn.setStatus('current')
if mibBuilder.loadTexts: hwPoePowerOn.setDescription('This object indicates that a PD connected to an interface is powered on.')
hwPoeSlotPowerOverload = NotificationType((1, 3, 6, 1, 4, 1, 2011, 5, 25, 195, 40, 4)).setObjects(("HUAWEI-POE-MIB", "hwPoeSlotNum"), ("HUAWEI-POE-MIB", "hwPoeSlotConsumingPower"))
if mibBuilder.loadTexts: hwPoeSlotPowerOverload.setStatus('current')
if mibBuilder.loadTexts: hwPoeSlotPowerOverload.setDescription('This object indicates that the power consumed by a slot exceeds the threshold.')
hwPoeSlotPowerOverloadResume = NotificationType((1, 3, 6, 1, 4, 1, 2011, 5, 25, 195, 40, 5)).setObjects(("HUAWEI-POE-MIB", "hwPoeSlotNum"), ("HUAWEI-POE-MIB", "hwPoeSlotConsumingPower"))
if mibBuilder.loadTexts: hwPoeSlotPowerOverloadResume.setStatus('current')
if mibBuilder.loadTexts: hwPoeSlotPowerOverloadResume.setDescription('This object indicates that the power consumed by a slot does not exceed the threshold.')
hwPoePdPowerOverload = NotificationType((1, 3, 6, 1, 4, 1, 2011, 5, 25, 195, 40, 6)).setObjects(("HUAWEI-POE-MIB", "hwPoePortName"), ("HUAWEI-POE-MIB", "hwPoePortConsumingPower"), ("HUAWEI-POE-MIB", "hwPoePortMaximumPower"))
if mibBuilder.loadTexts: hwPoePdPowerOverload.setStatus('current')
if mibBuilder.loadTexts: hwPoePdPowerOverload.setDescription('This object indicates the power consumed by a PD connected to an interface exceeds the threshold.')
hwPoePdPowerOverloadResume = NotificationType((1, 3, 6, 1, 4, 1, 2011, 5, 25, 195, 40, 7)).setObjects(("HUAWEI-POE-MIB", "hwPoePortName"), ("HUAWEI-POE-MIB", "hwPoePortConsumingPower"), ("HUAWEI-POE-MIB", "hwPoePortMaximumPower"))
if mibBuilder.loadTexts: hwPoePdPowerOverloadResume.setStatus('current')
if mibBuilder.loadTexts: hwPoePdPowerOverloadResume.setDescription('This object indicates that the power consumed by a PD connected to an interface does not exceed the threshold.')
hwPoePdConnected = NotificationType((1, 3, 6, 1, 4, 1, 2011, 5, 25, 195, 40, 8)).setObjects(("HUAWEI-POE-MIB", "hwPoePortName"))
if mibBuilder.loadTexts: hwPoePdConnected.setStatus('current')
if mibBuilder.loadTexts: hwPoePdConnected.setDescription('This object indicates that a PD is connected to an interface.')
hwPoePdDisconnected = NotificationType((1, 3, 6, 1, 4, 1, 2011, 5, 25, 195, 40, 9)).setObjects(("HUAWEI-POE-MIB", "hwPoePortName"))
if mibBuilder.loadTexts: hwPoePdDisconnected.setStatus('current')
if mibBuilder.loadTexts: hwPoePdDisconnected.setDescription('This object indicates that a PD is disconnected from an interface.')
hwPoePdClassInvalid = NotificationType((1, 3, 6, 1, 4, 1, 2011, 5, 25, 195, 40, 10)).setObjects(("HUAWEI-POE-MIB", "hwPoePortName"))
if mibBuilder.loadTexts: hwPoePdClassInvalid.setStatus('current')
if mibBuilder.loadTexts: hwPoePdClassInvalid.setDescription('This object indicates that a PD of an invalid class is detected.')
hwPoePdClassOvercurrent = NotificationType((1, 3, 6, 1, 4, 1, 2011, 5, 25, 195, 40, 11)).setObjects(("HUAWEI-POE-MIB", "hwPoePortName"))
if mibBuilder.loadTexts: hwPoePdClassOvercurrent.setStatus('current')
if mibBuilder.loadTexts: hwPoePdClassOvercurrent.setDescription('This object indicates that overcurrent occurs during the classification of a PD.')
hwPoePdPowerOvercurrent = NotificationType((1, 3, 6, 1, 4, 1, 2011, 5, 25, 195, 40, 12)).setObjects(("HUAWEI-POE-MIB", "hwPoePortName"))
if mibBuilder.loadTexts: hwPoePdPowerOvercurrent.setStatus('current')
if mibBuilder.loadTexts: hwPoePdPowerOvercurrent.setDescription('This object indicates that overcurrent occurs during the powering of a PD.')
hwPoePdPowerOvercurrentResume = NotificationType((1, 3, 6, 1, 4, 1, 2011, 5, 25, 195, 40, 13)).setObjects(("HUAWEI-POE-MIB", "hwPoePortName"))
if mibBuilder.loadTexts: hwPoePdPowerOvercurrentResume.setStatus('current')
if mibBuilder.loadTexts: hwPoePdPowerOvercurrentResume.setDescription('This object indicates that overcurrent is rectified.')
hwPoePowerOnFail = NotificationType((1, 3, 6, 1, 4, 1, 2011, 5, 25, 195, 40, 14)).setObjects(("HUAWEI-POE-MIB", "hwPoePortName"))
if mibBuilder.loadTexts: hwPoePowerOnFail.setStatus('current')
if mibBuilder.loadTexts: hwPoePowerOnFail.setDescription('This object indicates that a PD fails to be powered on.')
hwPoePowerOffCurrentLimits = NotificationType((1, 3, 6, 1, 4, 1, 2011, 5, 25, 195, 40, 15)).setObjects(("HUAWEI-POE-MIB", "hwPoePortName"))
if mibBuilder.loadTexts: hwPoePowerOffCurrentLimits.setStatus('current')
if mibBuilder.loadTexts: hwPoePowerOffCurrentLimits.setDescription('This object indicates that a PD is powered off because its current meets or exceeds the limit of current.')
hwPoePdPriorityDifferent = NotificationType((1, 3, 6, 1, 4, 1, 2011, 5, 25, 195, 40, 16)).setObjects(("HUAWEI-POE-MIB", "hwPoePortName"), ("HUAWEI-POE-MIB", "hwPoePortPriority"), ("HUAWEI-POE-MIB", "hwPoePdPriority"))
if mibBuilder.loadTexts: hwPoePdPriorityDifferent.setStatus('current')
if mibBuilder.loadTexts: hwPoePdPriorityDifferent.setDescription('This object indicates that the priority of PD is different from the port.')
hwPoePowerOverUtilizationThreshold = NotificationType((1, 3, 6, 1, 4, 1, 2011, 5, 25, 195, 40, 17)).setObjects(("HUAWEI-POE-MIB", "hwPoeDeviceID"), ("HUAWEI-POE-MIB", "hwPoeCurConsumPower"), ("HUAWEI-POE-MIB", "hwPoeConsumPowerThreshold"))
if mibBuilder.loadTexts: hwPoePowerOverUtilizationThreshold.setStatus('current')
if mibBuilder.loadTexts: hwPoePowerOverUtilizationThreshold.setDescription('This object indicates that the PSE is overdrawing power.')
hwPoePowerOverUtilizationThresholdResume = NotificationType((1, 3, 6, 1, 4, 1, 2011, 5, 25, 195, 40, 18)).setObjects(("HUAWEI-POE-MIB", "hwPoeDeviceID"), ("HUAWEI-POE-MIB", "hwPoeCurConsumPower"), ("HUAWEI-POE-MIB", "hwPoeConsumPowerThreshold"))
if mibBuilder.loadTexts: hwPoePowerOverUtilizationThresholdResume.setStatus('current')
if mibBuilder.loadTexts: hwPoePowerOverUtilizationThresholdResume.setDescription('This object indicates that the PSE is not overdrawing power.')
hwPoeBoardInsertedWrongFrame = NotificationType((1, 3, 6, 1, 4, 1, 2011, 5, 25, 195, 40, 19)).setObjects(("HUAWEI-POE-MIB", "hwFrameID"), ("HUAWEI-POE-MIB", "hwPoeSlotNum"))
if mibBuilder.loadTexts: hwPoeBoardInsertedWrongFrame.setStatus('current')
if mibBuilder.loadTexts: hwPoeBoardInsertedWrongFrame.setDescription('This object indicates that the poe board is inserted in the frame does not support poe.')
hwPoePowerAbsent = NotificationType((1, 3, 6, 1, 4, 1, 2011, 5, 25, 195, 40, 20)).setObjects(("HUAWEI-POE-MIB", "hwFrameID"), ("HUAWEI-POE-MIB", "hwPoeSlotNum"))
if mibBuilder.loadTexts: hwPoePowerAbsent.setStatus('current')
if mibBuilder.loadTexts: hwPoePowerAbsent.setDescription('This object indicates that the poe power is absent.')
hwPoePowerAbsentResume = NotificationType((1, 3, 6, 1, 4, 1, 2011, 5, 25, 195, 40, 21)).setObjects(("HUAWEI-POE-MIB", "hwFrameID"), ("HUAWEI-POE-MIB", "hwPoeSlotNum"))
if mibBuilder.loadTexts: hwPoePowerAbsentResume.setStatus('current')
if mibBuilder.loadTexts: hwPoePowerAbsentResume.setDescription('This object indicates that the poe power is present.')
hwPoeRpsPowerOutputAlarm = NotificationType((1, 3, 6, 1, 4, 1, 2011, 5, 25, 195, 40, 22)).setObjects(("HUAWEI-POE-MIB", "hwPoeSlotNum"))
if mibBuilder.loadTexts: hwPoeRpsPowerOutputAlarm.setStatus('current')
if mibBuilder.loadTexts: hwPoeRpsPowerOutputAlarm.setDescription('This object indicates that the RPS power can not provide POE power for this device.')
hwPoeRpsPowerOutputAlarmResume = NotificationType((1, 3, 6, 1, 4, 1, 2011, 5, 25, 195, 40, 23)).setObjects(("HUAWEI-POE-MIB", "hwPoeSlotNum"))
if mibBuilder.loadTexts: hwPoeRpsPowerOutputAlarmResume.setStatus('current')
if mibBuilder.loadTexts: hwPoeRpsPowerOutputAlarmResume.setDescription('This object indicates that the RPS power can provide POE power for this device.')
hwPoeConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 5, 25, 195, 100))
hwPoeGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 5, 25, 195, 100, 1))
hwPoeSlotGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 2011, 5, 25, 195, 100, 1, 1)).setObjects(("HUAWEI-POE-MIB", "hwPoeSlotMaximumPower"), ("HUAWEI-POE-MIB", "hwPoeSlotReferencePower"), ("HUAWEI-POE-MIB", "hwPoeSlotConsumingPower"), ("HUAWEI-POE-MIB", "hwPoeSlotPeakPower"), ("HUAWEI-POE-MIB", "hwPoeSlotPowerManagementManner"), ("HUAWEI-POE-MIB", "hwPoeSlotIsPoeDevice"), ("HUAWEI-POE-MIB", "hwPoeSlotLegacyDetect"), ("HUAWEI-POE-MIB", "hwPoeSlotPowerRsvPercent"), ("HUAWEI-POE-MIB", "hwPoeSlotPowerUtilizationThreshold"), ("HUAWEI-POE-MIB", "hwPoeDimmId"), ("HUAWEI-POE-MIB", "hwPoeSlotAvailablePower"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    hwPoeSlotGroup = hwPoeSlotGroup.setStatus('current')
if mibBuilder.loadTexts: hwPoeSlotGroup.setDescription("This object indicates the POE's slot table group.")
hwPoePortGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 2011, 5, 25, 195, 100, 1, 2)).setObjects(("HUAWEI-POE-MIB", "hwPoePortEnable"), ("HUAWEI-POE-MIB", "hwPoePortPriority"), ("HUAWEI-POE-MIB", "hwPoePortMaximumPower"), ("HUAWEI-POE-MIB", "hwPoePortPowerOnStatus"), ("HUAWEI-POE-MIB", "hwPoePortPowerStatus"), ("HUAWEI-POE-MIB", "hwPoePortReferencePower"), ("HUAWEI-POE-MIB", "hwPoePortName"), ("HUAWEI-POE-MIB", "hwPoePortConsumingPower"), ("HUAWEI-POE-MIB", "hwPoePortPeakPower"), ("HUAWEI-POE-MIB", "hwPoePortAveragePower"), ("HUAWEI-POE-MIB", "hwPoePortCurrent"), ("HUAWEI-POE-MIB", "hwPoePortVoltage"), ("HUAWEI-POE-MIB", "hwPoePortManualOperation"), ("HUAWEI-POE-MIB", "hwPoePortPdClass"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    hwPoePortGroup = hwPoePortGroup.setStatus('current')
if mibBuilder.loadTexts: hwPoePortGroup.setDescription("This object indicates the POE's port table group.")
hwPoeGlobalGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 2011, 5, 25, 195, 100, 1, 3)).setObjects(("HUAWEI-POE-MIB", "hwPoePowerUtilizationThreshold"), ("HUAWEI-POE-MIB", "hwPoePowerRsvPercent"), ("HUAWEI-POE-MIB", "hwPoePower"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    hwPoeGlobalGroup = hwPoeGlobalGroup.setStatus('current')
if mibBuilder.loadTexts: hwPoeGlobalGroup.setDescription("This object indicates the POE's global table group.")
hwPoeNotificationGroup = NotificationGroup((1, 3, 6, 1, 4, 1, 2011, 5, 25, 195, 100, 1, 4)).setObjects(("HUAWEI-POE-MIB", "hwPoeDimmError"), ("HUAWEI-POE-MIB", "hwPoePowerOff"), ("HUAWEI-POE-MIB", "hwPoePowerOn"), ("HUAWEI-POE-MIB", "hwPoePdPowerOverload"), ("HUAWEI-POE-MIB", "hwPoePdPowerOverloadResume"), ("HUAWEI-POE-MIB", "hwPoePdConnected"), ("HUAWEI-POE-MIB", "hwPoePdDisconnected"), ("HUAWEI-POE-MIB", "hwPoePdClassInvalid"), ("HUAWEI-POE-MIB", "hwPoePdClassOvercurrent"), ("HUAWEI-POE-MIB", "hwPoePdPowerOvercurrent"), ("HUAWEI-POE-MIB", "hwPoePdPowerOvercurrentResume"), ("HUAWEI-POE-MIB", "hwPoePowerOnFail"), ("HUAWEI-POE-MIB", "hwPoePowerOffCurrentLimits"), ("HUAWEI-POE-MIB", "hwPoePowerOverUtilizationThresholdResume"), ("HUAWEI-POE-MIB", "hwPoePowerOverUtilizationThreshold"), ("HUAWEI-POE-MIB", "hwPoePdPriorityDifferent"), ("HUAWEI-POE-MIB", "hwPoeSlotPowerOverload"), ("HUAWEI-POE-MIB", "hwPoeSlotPowerOverloadResume"), ("HUAWEI-POE-MIB", "hwPoeBoardInsertedWrongFrame"), ("HUAWEI-POE-MIB", "hwPoePowerAbsent"), ("HUAWEI-POE-MIB", "hwPoePowerAbsentResume"), ("HUAWEI-POE-MIB", "hwPoeRpsPowerOutputAlarm"), ("HUAWEI-POE-MIB", "hwPoeRpsPowerOutputAlarmResume"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    hwPoeNotificationGroup = hwPoeNotificationGroup.setStatus('current')
if mibBuilder.loadTexts: hwPoeNotificationGroup.setDescription("This object indicates the POE's notification table group.")
hwPoeTrapObjectsGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 2011, 5, 25, 195, 100, 1, 5)).setObjects(("HUAWEI-POE-MIB", "hwPoePdPriority"), ("HUAWEI-POE-MIB", "hwPoeSlotNum"), ("HUAWEI-POE-MIB", "hwPoeCurConsumPower"), ("HUAWEI-POE-MIB", "hwPoeConsumPowerThreshold"), ("HUAWEI-POE-MIB", "hwPoeDeviceID"), ("HUAWEI-POE-MIB", "hwFrameID"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    hwPoeTrapObjectsGroup = hwPoeTrapObjectsGroup.setStatus('current')
if mibBuilder.loadTexts: hwPoeTrapObjectsGroup.setDescription('Description.')
mibBuilder.exportSymbols("HUAWEI-POE-MIB", hwPoePowerUtilizationThreshold=hwPoePowerUtilizationThreshold, hwPoePowerOnFail=hwPoePowerOnFail, hwPoeCurConsumPower=hwPoeCurConsumPower, hwPoeSlotReferencePower=hwPoeSlotReferencePower, PYSNMP_MODULE_ID=hwPoeMIB, hwPoePortConsumingPower=hwPoePortConsumingPower, hwPoeSlotPowerOverloadResume=hwPoeSlotPowerOverloadResume, hwPoePortVoltage=hwPoePortVoltage, hwPoeNotificationGroup=hwPoeNotificationGroup, hwPoeGlobalGroup=hwPoeGlobalGroup, hwPoeConformance=hwPoeConformance, hwPoePortPriority=hwPoePortPriority, hwPoePdConnected=hwPoePdConnected, hwPoePdPowerOverloadResume=hwPoePdPowerOverloadResume, hwPoePortName=hwPoePortName, hwPoeSlotLegacyDetect=hwPoeSlotLegacyDetect, hwPoePdDisconnected=hwPoePdDisconnected, hwPoePortIfIndex=hwPoePortIfIndex, hwPoeBoardInsertedWrongFrame=hwPoeBoardInsertedWrongFrame, hwPoeMIB=hwPoeMIB, hwPoePdClassOvercurrent=hwPoePdClassOvercurrent, hwPoeNotification=hwPoeNotification, hwPoeSlotGroup=hwPoeSlotGroup, hwPoeSlotPowerRsvPercent=hwPoeSlotPowerRsvPercent, hwPoeSlotMaximumPower=hwPoeSlotMaximumPower, hwPoePdPowerOvercurrent=hwPoePdPowerOvercurrent, hwPoePortPowerOnStatus=hwPoePortPowerOnStatus, hwPoeSlotNum=hwPoeSlotNum, hwPoeDeviceID=hwPoeDeviceID, hwPoeRpsPowerOutputAlarm=hwPoeRpsPowerOutputAlarm, hwPoeSlotEntry=hwPoeSlotEntry, hwPoePowerAbsent=hwPoePowerAbsent, hwPoePdPowerOverload=hwPoePdPowerOverload, hwPoePortGroup=hwPoePortGroup, hwPoePortManualOperation=hwPoePortManualOperation, hwPoePowerOn=hwPoePowerOn, hwPoeSlotTable=hwPoeSlotTable, hwPoePortPowerStatus=hwPoePortPowerStatus, hwPoePortPeakPower=hwPoePortPeakPower, hwPoePdClassInvalid=hwPoePdClassInvalid, hwPoePower=hwPoePower, hwPoePortReferencePower=hwPoePortReferencePower, hwPoeSlotIsPoeDevice=hwPoeSlotIsPoeDevice, hwPoePowerAbsentResume=hwPoePowerAbsentResume, hwPoePowerOffCurrentLimits=hwPoePowerOffCurrentLimits, hwPoePortMaximumPower=hwPoePortMaximumPower, hwFrameID=hwFrameID, hwPoeSlotAvailablePower=hwPoeSlotAvailablePower, hwPoePortEntry=hwPoePortEntry, hwPoeTrapObjects=hwPoeTrapObjects, hwPoePowerOff=hwPoePowerOff, hwPoeSlotPowerOverload=hwPoeSlotPowerOverload, hwPoePdPriority=hwPoePdPriority, hwPoeSlotConsumingPower=hwPoeSlotConsumingPower, hwPoeConsumPowerThreshold=hwPoeConsumPowerThreshold, hwPoePortTable=hwPoePortTable, hwPoePdPowerOvercurrentResume=hwPoePdPowerOvercurrentResume, hwPoeSlotPeakPower=hwPoeSlotPeakPower, hwPoeDimmError=hwPoeDimmError, hwPoePortEnable=hwPoePortEnable, hwPoeSlotId=hwPoeSlotId, hwPoePortCurrent=hwPoePortCurrent, hwPoePortPdClass=hwPoePortPdClass, hwPoeRpsPowerOutputAlarmResume=hwPoeRpsPowerOutputAlarmResume, hwPoeSlotPowerManagementManner=hwPoeSlotPowerManagementManner, hwPoePowerOverUtilizationThreshold=hwPoePowerOverUtilizationThreshold, hwPoePowerOverUtilizationThresholdResume=hwPoePowerOverUtilizationThresholdResume, hwPoePdPriorityDifferent=hwPoePdPriorityDifferent, hwPoePortAveragePower=hwPoePortAveragePower, hwPoeGroups=hwPoeGroups, hwPoeDimmId=hwPoeDimmId, hwPoeGlobalObjects=hwPoeGlobalObjects, hwPoeSlotPowerUtilizationThreshold=hwPoeSlotPowerUtilizationThreshold, hwPoePowerRsvPercent=hwPoePowerRsvPercent, hwPoeTrapObjectsGroup=hwPoeTrapObjectsGroup)