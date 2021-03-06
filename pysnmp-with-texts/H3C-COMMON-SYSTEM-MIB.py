#
# PySNMP MIB module H3C-COMMON-SYSTEM-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/H3C-COMMON-SYSTEM-MIB
# Produced by pysmi-0.3.4 at Wed May  1 13:21:31 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
OctetString, Integer, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "OctetString", "Integer", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ValueSizeConstraint, ConstraintsUnion, SingleValueConstraint, ValueRangeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ValueSizeConstraint", "ConstraintsUnion", "SingleValueConstraint", "ValueRangeConstraint")
hwSystem, = mibBuilder.importSymbols("HUAWEI-3COM-OID-MIB", "hwSystem")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
ModuleIdentity, Integer32, ObjectIdentity, Bits, Unsigned32, Counter32, Counter64, IpAddress, MibIdentifier, iso, MibScalar, MibTable, MibTableRow, MibTableColumn, NotificationType, TimeTicks, Gauge32 = mibBuilder.importSymbols("SNMPv2-SMI", "ModuleIdentity", "Integer32", "ObjectIdentity", "Bits", "Unsigned32", "Counter32", "Counter64", "IpAddress", "MibIdentifier", "iso", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "NotificationType", "TimeTicks", "Gauge32")
DisplayString, TextualConvention, DateAndTime = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention", "DateAndTime")
hwWriteConfig = MibScalar((1, 3, 6, 1, 4, 1, 2011, 10, 6, 5), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1))).clone(namedValues=NamedValues(("save", 1)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hwWriteConfig.setStatus('current')
if mibBuilder.loadTexts: hwWriteConfig.setDescription('Write config to router.')
hwStartFtpServer = MibScalar((1, 3, 6, 1, 4, 1, 2011, 10, 6, 6), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enable", 1), ("disable", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hwStartFtpServer.setStatus('current')
if mibBuilder.loadTexts: hwStartFtpServer.setDescription('Decide whether start ftp-server.enable(1) indicates to start ftp-server; disable(2) indicates to stop ftp-server.')
hwReboot = MibScalar((1, 3, 6, 1, 4, 1, 2011, 10, 6, 7), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1))).clone(namedValues=NamedValues(("reboot", 1)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hwReboot.setStatus('current')
if mibBuilder.loadTexts: hwReboot.setDescription('Reboot router.')
hwSystemNotification = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 10, 6, 8))
hwWriteSuccessTrap = NotificationType((1, 3, 6, 1, 4, 1, 2011, 10, 6, 8, 1))
if mibBuilder.loadTexts: hwWriteSuccessTrap.setStatus('current')
if mibBuilder.loadTexts: hwWriteSuccessTrap.setDescription('send a trap about write success.')
hwWriteFailureTrap = NotificationType((1, 3, 6, 1, 4, 1, 2011, 10, 6, 8, 2))
if mibBuilder.loadTexts: hwWriteFailureTrap.setStatus('current')
if mibBuilder.loadTexts: hwWriteFailureTrap.setDescription('send a trap about write failure.')
hwRebootSendTrap = NotificationType((1, 3, 6, 1, 4, 1, 2011, 10, 6, 8, 3))
if mibBuilder.loadTexts: hwRebootSendTrap.setStatus('current')
if mibBuilder.loadTexts: hwRebootSendTrap.setDescription("When users restart the device with command 'reboot', this trap will be sent two seconds before the device reboots.")
hwSysColdStartTrap = NotificationType((1, 3, 6, 1, 4, 1, 2011, 10, 6, 8, 4)).setObjects(("H3C-COMMON-SYSTEM-MIB", "hwSysFirstTrapTime"))
if mibBuilder.loadTexts: hwSysColdStartTrap.setStatus('current')
if mibBuilder.loadTexts: hwSysColdStartTrap.setDescription('A system cold start trap.')
hwSysWarmStartTrap = NotificationType((1, 3, 6, 1, 4, 1, 2011, 10, 6, 8, 5)).setObjects(("H3C-COMMON-SYSTEM-MIB", "hwSysFirstTrapTime"))
if mibBuilder.loadTexts: hwSysWarmStartTrap.setStatus('current')
if mibBuilder.loadTexts: hwSysWarmStartTrap.setDescription('A system warm start trap.')
hwSoftwareVersion = MibScalar((1, 3, 6, 1, 4, 1, 2011, 10, 6, 9), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hwSoftwareVersion.setStatus('current')
if mibBuilder.loadTexts: hwSoftwareVersion.setDescription('Software version.')
hwSysBootType = MibScalar((1, 3, 6, 1, 4, 1, 2011, 10, 6, 10), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("coldStart", 1), ("warmStart", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: hwSysBootType.setStatus('current')
if mibBuilder.loadTexts: hwSysBootType.setDescription('The boot type of the system whether the last device reboot was by CLI (warm start) or power off (cold start).')
hwSystemInfo = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 10, 6, 11))
hwSysStatisticPeriod = MibScalar((1, 3, 6, 1, 4, 1, 2011, 10, 6, 11, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 900))).setUnits('seconds').setMaxAccess("readwrite")
if mibBuilder.loadTexts: hwSysStatisticPeriod.setStatus('current')
if mibBuilder.loadTexts: hwSysStatisticPeriod.setDescription('The statistic period. The device collects statistics within the period.')
hwSysSamplePeriod = MibScalar((1, 3, 6, 1, 4, 1, 2011, 10, 6, 11, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 300))).setUnits('seconds').setMaxAccess("readwrite")
if mibBuilder.loadTexts: hwSysSamplePeriod.setStatus('current')
if mibBuilder.loadTexts: hwSysSamplePeriod.setDescription('The sampling period. The device takes samples periodically for statistics collection.')
hwSysTrapResendPeriod = MibScalar((1, 3, 6, 1, 4, 1, 2011, 10, 6, 11, 3), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 3600))).setUnits('seconds').setMaxAccess("readwrite")
if mibBuilder.loadTexts: hwSysTrapResendPeriod.setStatus('current')
if mibBuilder.loadTexts: hwSysTrapResendPeriod.setDescription('The trap resending period. If the value is zero, the trap will not be re-sent.')
hwSysTrapCollectionPeriod = MibScalar((1, 3, 6, 1, 4, 1, 2011, 10, 6, 11, 4), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 60))).setUnits('seconds').setMaxAccess("readwrite")
if mibBuilder.loadTexts: hwSysTrapCollectionPeriod.setStatus('current')
if mibBuilder.loadTexts: hwSysTrapCollectionPeriod.setDescription('The trap collecting period. If the value is zero, the trap will not be re-sent.')
hwSysSnmpPort = MibScalar((1, 3, 6, 1, 4, 1, 2011, 10, 6, 11, 5), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hwSysSnmpPort.setStatus('current')
if mibBuilder.loadTexts: hwSysSnmpPort.setDescription('UDP port for SNMP protocol entity to receive messages except Trap-PDU.')
hwSysSnmpTrapPort = MibScalar((1, 3, 6, 1, 4, 1, 2011, 10, 6, 11, 6), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hwSysSnmpTrapPort.setStatus('current')
if mibBuilder.loadTexts: hwSysSnmpTrapPort.setDescription('UDP port for Trap-PDU to receive messages.')
hwSysNetID = MibScalar((1, 3, 6, 1, 4, 1, 2011, 10, 6, 11, 7), OctetString().subtype(subtypeSpec=ValueSizeConstraint(0, 127))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hwSysNetID.setStatus('current')
if mibBuilder.loadTexts: hwSysNetID.setDescription('The system Net ID.')
hwSysLastSampleTime = MibScalar((1, 3, 6, 1, 4, 1, 2011, 10, 6, 11, 8), DateAndTime()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hwSysLastSampleTime.setStatus('current')
if mibBuilder.loadTexts: hwSysLastSampleTime.setDescription('The last sample local time of the system.')
hwSysTrapSendNum = MibScalar((1, 3, 6, 1, 4, 1, 2011, 10, 6, 11, 9), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 24))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hwSysTrapSendNum.setStatus('current')
if mibBuilder.loadTexts: hwSysTrapSendNum.setDescription('The trap send times. If the value is zero, the trap will be sent all the time if it occurs.')
hwSysFirstTrapTime = MibScalar((1, 3, 6, 1, 4, 1, 2011, 10, 6, 11, 10), TimeTicks()).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: hwSysFirstTrapTime.setStatus('current')
if mibBuilder.loadTexts: hwSysFirstTrapTime.setDescription('Represents the first trap time.')
mibBuilder.exportSymbols("H3C-COMMON-SYSTEM-MIB", hwSysColdStartTrap=hwSysColdStartTrap, hwSysStatisticPeriod=hwSysStatisticPeriod, hwSysSnmpPort=hwSysSnmpPort, hwSysNetID=hwSysNetID, hwSysBootType=hwSysBootType, hwSysSnmpTrapPort=hwSysSnmpTrapPort, hwSysSamplePeriod=hwSysSamplePeriod, hwWriteFailureTrap=hwWriteFailureTrap, hwReboot=hwReboot, hwSysTrapResendPeriod=hwSysTrapResendPeriod, hwWriteSuccessTrap=hwWriteSuccessTrap, hwSysLastSampleTime=hwSysLastSampleTime, hwSysTrapCollectionPeriod=hwSysTrapCollectionPeriod, hwSystemInfo=hwSystemInfo, hwSystemNotification=hwSystemNotification, hwRebootSendTrap=hwRebootSendTrap, hwSysFirstTrapTime=hwSysFirstTrapTime, hwSoftwareVersion=hwSoftwareVersion, hwSysTrapSendNum=hwSysTrapSendNum, hwWriteConfig=hwWriteConfig, hwSysWarmStartTrap=hwSysWarmStartTrap, hwStartFtpServer=hwStartFtpServer)
