#
# PySNMP MIB module CISCO-UNIFIED-COMPUTING-SECURITY-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/CISCO-UNIFIED-COMPUTING-SECURITY-MIB
# Produced by pysmi-0.3.4 at Wed May  1 12:17:30 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
OctetString, ObjectIdentifier, Integer = mibBuilder.importSymbols("ASN1", "OctetString", "ObjectIdentifier", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ConstraintsUnion, SingleValueConstraint, ValueSizeConstraint, ValueRangeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ConstraintsUnion", "SingleValueConstraint", "ValueSizeConstraint", "ValueRangeConstraint")
ciscoMgmt, = mibBuilder.importSymbols("CISCO-SMI", "ciscoMgmt")
CiscoAlarmSeverity, TimeIntervalSec, CiscoInetAddressMask, CiscoNetworkAddress, Unsigned64 = mibBuilder.importSymbols("CISCO-TC", "CiscoAlarmSeverity", "TimeIntervalSec", "CiscoInetAddressMask", "CiscoNetworkAddress", "Unsigned64")
ciscoUnifiedComputingMIBObjects, CucsManagedObjectId, CucsManagedObjectDn = mibBuilder.importSymbols("CISCO-UNIFIED-COMPUTING-MIB", "ciscoUnifiedComputingMIBObjects", "CucsManagedObjectId", "CucsManagedObjectDn")
CucsSecurityUnitId, CucsEquipmentSensorThresholdStatus, CucsEquipmentPresence, CucsEquipmentOperability, CucsEquipmentPowerState = mibBuilder.importSymbols("CISCO-UNIFIED-COMPUTING-TC-MIB", "CucsSecurityUnitId", "CucsEquipmentSensorThresholdStatus", "CucsEquipmentPresence", "CucsEquipmentOperability", "CucsEquipmentPowerState")
InetAddressIPv4, InetAddressIPv6 = mibBuilder.importSymbols("INET-ADDRESS-MIB", "InetAddressIPv4", "InetAddressIPv6")
SnmpAdminString, = mibBuilder.importSymbols("SNMP-FRAMEWORK-MIB", "SnmpAdminString")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
ModuleIdentity, Unsigned32, Bits, Integer32, Counter32, MibScalar, MibTable, MibTableRow, MibTableColumn, iso, IpAddress, MibIdentifier, Gauge32, NotificationType, TimeTicks, Counter64, ObjectIdentity = mibBuilder.importSymbols("SNMPv2-SMI", "ModuleIdentity", "Unsigned32", "Bits", "Integer32", "Counter32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "iso", "IpAddress", "MibIdentifier", "Gauge32", "NotificationType", "TimeTicks", "Counter64", "ObjectIdentity")
RowPointer, DateAndTime, TimeInterval, DisplayString, TruthValue, MacAddress, TimeStamp, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "RowPointer", "DateAndTime", "TimeInterval", "DisplayString", "TruthValue", "MacAddress", "TimeStamp", "TextualConvention")
cucsSecurityObjects = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 88))
if mibBuilder.loadTexts: cucsSecurityObjects.setLastUpdated('201601180000Z')
if mibBuilder.loadTexts: cucsSecurityObjects.setOrganization('Cisco Systems Inc.')
if mibBuilder.loadTexts: cucsSecurityObjects.setContactInfo('Cisco Systems Customer Service Postal: 170 W Tasman Drive San Jose, CA 95134 USA Tel: +1 800 553 -NETS E-mail: cs-san@cisco.com, cs-lan-switch-snmp@cisco.com')
if mibBuilder.loadTexts: cucsSecurityObjects.setDescription('MIB representation of the Cisco Unified Computing System SECURITY management information model package')
cucsSecurityUnitTable = MibTable((1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 88, 1), )
if mibBuilder.loadTexts: cucsSecurityUnitTable.setStatus('current')
if mibBuilder.loadTexts: cucsSecurityUnitTable.setDescription('Cisco UCS security:Unit managed object table')
cucsSecurityUnitEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 88, 1, 1), ).setIndexNames((0, "CISCO-UNIFIED-COMPUTING-SECURITY-MIB", "cucsSecurityUnitInstanceId"))
if mibBuilder.loadTexts: cucsSecurityUnitEntry.setStatus('current')
if mibBuilder.loadTexts: cucsSecurityUnitEntry.setDescription('Entry for the cucsSecurityUnitTable table.')
cucsSecurityUnitInstanceId = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 88, 1, 1, 1), CucsManagedObjectId())
if mibBuilder.loadTexts: cucsSecurityUnitInstanceId.setStatus('current')
if mibBuilder.loadTexts: cucsSecurityUnitInstanceId.setDescription('Instance identifier of the managed object.')
cucsSecurityUnitDn = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 88, 1, 1, 2), CucsManagedObjectDn()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cucsSecurityUnitDn.setStatus('current')
if mibBuilder.loadTexts: cucsSecurityUnitDn.setDescription('Cisco UCS security:Unit:dn managed object property')
cucsSecurityUnitRn = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 88, 1, 1, 3), SnmpAdminString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cucsSecurityUnitRn.setStatus('current')
if mibBuilder.loadTexts: cucsSecurityUnitRn.setDescription('Cisco UCS security:Unit:rn managed object property')
cucsSecurityUnitId = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 88, 1, 1, 4), CucsSecurityUnitId()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cucsSecurityUnitId.setStatus('current')
if mibBuilder.loadTexts: cucsSecurityUnitId.setDescription('Cisco UCS security:Unit:id managed object property')
cucsSecurityUnitLocationDn = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 88, 1, 1, 5), SnmpAdminString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cucsSecurityUnitLocationDn.setStatus('current')
if mibBuilder.loadTexts: cucsSecurityUnitLocationDn.setDescription('Cisco UCS security:Unit:locationDn managed object property')
cucsSecurityUnitModel = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 88, 1, 1, 6), SnmpAdminString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cucsSecurityUnitModel.setStatus('current')
if mibBuilder.loadTexts: cucsSecurityUnitModel.setDescription('Cisco UCS security:Unit:model managed object property')
cucsSecurityUnitOperQualifierReason = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 88, 1, 1, 7), SnmpAdminString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cucsSecurityUnitOperQualifierReason.setStatus('current')
if mibBuilder.loadTexts: cucsSecurityUnitOperQualifierReason.setDescription('Cisco UCS security:Unit:operQualifierReason managed object property')
cucsSecurityUnitOperState = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 88, 1, 1, 8), CucsEquipmentOperability()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cucsSecurityUnitOperState.setStatus('current')
if mibBuilder.loadTexts: cucsSecurityUnitOperState.setDescription('Cisco UCS security:Unit:operState managed object property')
cucsSecurityUnitOperability = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 88, 1, 1, 9), CucsEquipmentOperability()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cucsSecurityUnitOperability.setStatus('current')
if mibBuilder.loadTexts: cucsSecurityUnitOperability.setDescription('Cisco UCS security:Unit:operability managed object property')
cucsSecurityUnitPartNumber = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 88, 1, 1, 10), SnmpAdminString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cucsSecurityUnitPartNumber.setStatus('current')
if mibBuilder.loadTexts: cucsSecurityUnitPartNumber.setDescription('Cisco UCS security:Unit:partNumber managed object property')
cucsSecurityUnitPciAddr = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 88, 1, 1, 11), SnmpAdminString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cucsSecurityUnitPciAddr.setStatus('current')
if mibBuilder.loadTexts: cucsSecurityUnitPciAddr.setDescription('Cisco UCS security:Unit:pciAddr managed object property')
cucsSecurityUnitPciSlot = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 88, 1, 1, 12), SnmpAdminString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cucsSecurityUnitPciSlot.setStatus('current')
if mibBuilder.loadTexts: cucsSecurityUnitPciSlot.setDescription('Cisco UCS security:Unit:pciSlot managed object property')
cucsSecurityUnitPerf = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 88, 1, 1, 13), CucsEquipmentSensorThresholdStatus()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cucsSecurityUnitPerf.setStatus('current')
if mibBuilder.loadTexts: cucsSecurityUnitPerf.setDescription('Cisco UCS security:Unit:perf managed object property')
cucsSecurityUnitPower = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 88, 1, 1, 14), CucsEquipmentPowerState()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cucsSecurityUnitPower.setStatus('current')
if mibBuilder.loadTexts: cucsSecurityUnitPower.setDescription('Cisco UCS security:Unit:power managed object property')
cucsSecurityUnitPresence = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 88, 1, 1, 15), CucsEquipmentPresence()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cucsSecurityUnitPresence.setStatus('current')
if mibBuilder.loadTexts: cucsSecurityUnitPresence.setDescription('Cisco UCS security:Unit:presence managed object property')
cucsSecurityUnitRevision = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 88, 1, 1, 16), SnmpAdminString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cucsSecurityUnitRevision.setStatus('current')
if mibBuilder.loadTexts: cucsSecurityUnitRevision.setDescription('Cisco UCS security:Unit:revision managed object property')
cucsSecurityUnitSerial = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 88, 1, 1, 17), SnmpAdminString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cucsSecurityUnitSerial.setStatus('current')
if mibBuilder.loadTexts: cucsSecurityUnitSerial.setDescription('Cisco UCS security:Unit:serial managed object property')
cucsSecurityUnitThermal = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 88, 1, 1, 18), CucsEquipmentSensorThresholdStatus()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cucsSecurityUnitThermal.setStatus('current')
if mibBuilder.loadTexts: cucsSecurityUnitThermal.setDescription('Cisco UCS security:Unit:thermal managed object property')
cucsSecurityUnitVendor = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 88, 1, 1, 19), SnmpAdminString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cucsSecurityUnitVendor.setStatus('current')
if mibBuilder.loadTexts: cucsSecurityUnitVendor.setDescription('Cisco UCS security:Unit:vendor managed object property')
cucsSecurityUnitVid = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 88, 1, 1, 20), SnmpAdminString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cucsSecurityUnitVid.setStatus('current')
if mibBuilder.loadTexts: cucsSecurityUnitVid.setDescription('Cisco UCS security:Unit:vid managed object property')
cucsSecurityUnitVoltage = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 88, 1, 1, 21), CucsEquipmentSensorThresholdStatus()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cucsSecurityUnitVoltage.setStatus('current')
if mibBuilder.loadTexts: cucsSecurityUnitVoltage.setDescription('Cisco UCS security:Unit:voltage managed object property')
mibBuilder.exportSymbols("CISCO-UNIFIED-COMPUTING-SECURITY-MIB", cucsSecurityUnitOperQualifierReason=cucsSecurityUnitOperQualifierReason, cucsSecurityUnitRn=cucsSecurityUnitRn, cucsSecurityUnitPartNumber=cucsSecurityUnitPartNumber, cucsSecurityUnitVoltage=cucsSecurityUnitVoltage, cucsSecurityUnitPerf=cucsSecurityUnitPerf, cucsSecurityUnitPresence=cucsSecurityUnitPresence, cucsSecurityUnitModel=cucsSecurityUnitModel, cucsSecurityUnitInstanceId=cucsSecurityUnitInstanceId, cucsSecurityUnitRevision=cucsSecurityUnitRevision, cucsSecurityUnitSerial=cucsSecurityUnitSerial, cucsSecurityUnitPciSlot=cucsSecurityUnitPciSlot, cucsSecurityUnitId=cucsSecurityUnitId, cucsSecurityUnitEntry=cucsSecurityUnitEntry, cucsSecurityUnitLocationDn=cucsSecurityUnitLocationDn, cucsSecurityUnitPciAddr=cucsSecurityUnitPciAddr, cucsSecurityUnitTable=cucsSecurityUnitTable, cucsSecurityUnitOperability=cucsSecurityUnitOperability, PYSNMP_MODULE_ID=cucsSecurityObjects, cucsSecurityUnitVendor=cucsSecurityUnitVendor, cucsSecurityUnitDn=cucsSecurityUnitDn, cucsSecurityUnitThermal=cucsSecurityUnitThermal, cucsSecurityUnitOperState=cucsSecurityUnitOperState, cucsSecurityUnitPower=cucsSecurityUnitPower, cucsSecurityObjects=cucsSecurityObjects, cucsSecurityUnitVid=cucsSecurityUnitVid)
