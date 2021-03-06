#
# PySNMP MIB module CISCO-UNIFIED-COMPUTING-VERSION-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/CISCO-UNIFIED-COMPUTING-VERSION-MIB
# Produced by pysmi-0.3.4 at Wed May  1 12:17:54 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, ValueSizeConstraint, ConstraintsIntersection, SingleValueConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "ValueSizeConstraint", "ConstraintsIntersection", "SingleValueConstraint", "ConstraintsUnion")
ciscoMgmt, = mibBuilder.importSymbols("CISCO-SMI", "ciscoMgmt")
TimeIntervalSec, Unsigned64, CiscoAlarmSeverity, CiscoNetworkAddress, CiscoInetAddressMask = mibBuilder.importSymbols("CISCO-TC", "TimeIntervalSec", "Unsigned64", "CiscoAlarmSeverity", "CiscoNetworkAddress", "CiscoInetAddressMask")
ciscoUnifiedComputingMIBObjects, CucsManagedObjectDn, CucsManagedObjectId = mibBuilder.importSymbols("CISCO-UNIFIED-COMPUTING-MIB", "ciscoUnifiedComputingMIBObjects", "CucsManagedObjectDn", "CucsManagedObjectId")
InetAddressIPv6, InetAddressIPv4 = mibBuilder.importSymbols("INET-ADDRESS-MIB", "InetAddressIPv6", "InetAddressIPv4")
SnmpAdminString, = mibBuilder.importSymbols("SNMP-FRAMEWORK-MIB", "SnmpAdminString")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
Integer32, Unsigned32, Bits, Counter32, Gauge32, TimeTicks, iso, IpAddress, Counter64, ObjectIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, MibIdentifier, ModuleIdentity, NotificationType = mibBuilder.importSymbols("SNMPv2-SMI", "Integer32", "Unsigned32", "Bits", "Counter32", "Gauge32", "TimeTicks", "iso", "IpAddress", "Counter64", "ObjectIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "MibIdentifier", "ModuleIdentity", "NotificationType")
TruthValue, DateAndTime, MacAddress, TextualConvention, TimeInterval, RowPointer, DisplayString, TimeStamp = mibBuilder.importSymbols("SNMPv2-TC", "TruthValue", "DateAndTime", "MacAddress", "TextualConvention", "TimeInterval", "RowPointer", "DisplayString", "TimeStamp")
cucsVersionObjects = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 70))
if mibBuilder.loadTexts: cucsVersionObjects.setLastUpdated('201601180000Z')
if mibBuilder.loadTexts: cucsVersionObjects.setOrganization('Cisco Systems Inc.')
if mibBuilder.loadTexts: cucsVersionObjects.setContactInfo('Cisco Systems Customer Service Postal: 170 W Tasman Drive San Jose, CA 95134 USA Tel: +1 800 553 -NETS E-mail: cs-san@cisco.com, cs-lan-switch-snmp@cisco.com')
if mibBuilder.loadTexts: cucsVersionObjects.setDescription('MIB representation of the Cisco Unified Computing System VERSION management information model package')
cucsVersionApplicationTable = MibTable((1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 70, 1), )
if mibBuilder.loadTexts: cucsVersionApplicationTable.setStatus('current')
if mibBuilder.loadTexts: cucsVersionApplicationTable.setDescription('Cisco UCS version:Application managed object table')
cucsVersionApplicationEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 70, 1, 1), ).setIndexNames((0, "CISCO-UNIFIED-COMPUTING-VERSION-MIB", "cucsVersionApplicationInstanceId"))
if mibBuilder.loadTexts: cucsVersionApplicationEntry.setStatus('current')
if mibBuilder.loadTexts: cucsVersionApplicationEntry.setDescription('Entry for the cucsVersionApplicationTable table.')
cucsVersionApplicationInstanceId = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 70, 1, 1, 1), CucsManagedObjectId())
if mibBuilder.loadTexts: cucsVersionApplicationInstanceId.setStatus('current')
if mibBuilder.loadTexts: cucsVersionApplicationInstanceId.setDescription('Instance identifier of the managed object.')
cucsVersionApplicationDn = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 70, 1, 1, 2), CucsManagedObjectDn()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cucsVersionApplicationDn.setStatus('current')
if mibBuilder.loadTexts: cucsVersionApplicationDn.setDescription('Cisco UCS version:Application:dn managed object property')
cucsVersionApplicationRn = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 70, 1, 1, 3), SnmpAdminString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cucsVersionApplicationRn.setStatus('current')
if mibBuilder.loadTexts: cucsVersionApplicationRn.setDescription('Cisco UCS version:Application:rn managed object property')
cucsVersionApplicationDetail = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 70, 1, 1, 4), SnmpAdminString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cucsVersionApplicationDetail.setStatus('current')
if mibBuilder.loadTexts: cucsVersionApplicationDetail.setDescription('Cisco UCS version:Application:detail managed object property')
cucsVersionApplicationTime = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 70, 1, 1, 5), SnmpAdminString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cucsVersionApplicationTime.setStatus('current')
if mibBuilder.loadTexts: cucsVersionApplicationTime.setDescription('Cisco UCS version:Application:time managed object property')
cucsVersionApplicationVersion = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 70, 1, 1, 6), SnmpAdminString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cucsVersionApplicationVersion.setStatus('current')
if mibBuilder.loadTexts: cucsVersionApplicationVersion.setDescription('Cisco UCS version:Application:version managed object property')
cucsVersionEpTable = MibTable((1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 70, 2), )
if mibBuilder.loadTexts: cucsVersionEpTable.setStatus('current')
if mibBuilder.loadTexts: cucsVersionEpTable.setDescription('Cisco UCS version:Ep managed object table')
cucsVersionEpEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 70, 2, 1), ).setIndexNames((0, "CISCO-UNIFIED-COMPUTING-VERSION-MIB", "cucsVersionEpInstanceId"))
if mibBuilder.loadTexts: cucsVersionEpEntry.setStatus('current')
if mibBuilder.loadTexts: cucsVersionEpEntry.setDescription('Entry for the cucsVersionEpTable table.')
cucsVersionEpInstanceId = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 70, 2, 1, 1), CucsManagedObjectId())
if mibBuilder.loadTexts: cucsVersionEpInstanceId.setStatus('current')
if mibBuilder.loadTexts: cucsVersionEpInstanceId.setDescription('Instance identifier of the managed object.')
cucsVersionEpDn = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 70, 2, 1, 2), CucsManagedObjectDn()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cucsVersionEpDn.setStatus('current')
if mibBuilder.loadTexts: cucsVersionEpDn.setDescription('Cisco UCS version:Ep:dn managed object property')
cucsVersionEpRn = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 70, 2, 1, 3), SnmpAdminString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cucsVersionEpRn.setStatus('current')
if mibBuilder.loadTexts: cucsVersionEpRn.setDescription('Cisco UCS version:Ep:rn managed object property')
mibBuilder.exportSymbols("CISCO-UNIFIED-COMPUTING-VERSION-MIB", cucsVersionEpTable=cucsVersionEpTable, cucsVersionEpEntry=cucsVersionEpEntry, cucsVersionEpDn=cucsVersionEpDn, cucsVersionApplicationDetail=cucsVersionApplicationDetail, PYSNMP_MODULE_ID=cucsVersionObjects, cucsVersionApplicationInstanceId=cucsVersionApplicationInstanceId, cucsVersionApplicationTime=cucsVersionApplicationTime, cucsVersionEpRn=cucsVersionEpRn, cucsVersionApplicationVersion=cucsVersionApplicationVersion, cucsVersionApplicationEntry=cucsVersionApplicationEntry, cucsVersionApplicationDn=cucsVersionApplicationDn, cucsVersionObjects=cucsVersionObjects, cucsVersionApplicationTable=cucsVersionApplicationTable, cucsVersionApplicationRn=cucsVersionApplicationRn, cucsVersionEpInstanceId=cucsVersionEpInstanceId)
