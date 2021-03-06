#
# PySNMP MIB module CISCO-UNIFIED-COMPUTING-TOP-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/CISCO-UNIFIED-COMPUTING-TOP-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 18:01:24 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
OctetString, ObjectIdentifier, Integer = mibBuilder.importSymbols("ASN1", "OctetString", "ObjectIdentifier", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion, ConstraintsIntersection, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion", "ConstraintsIntersection", "ValueSizeConstraint")
ciscoMgmt, = mibBuilder.importSymbols("CISCO-SMI", "ciscoMgmt")
CiscoNetworkAddress, TimeIntervalSec, Unsigned64, CiscoInetAddressMask, CiscoAlarmSeverity = mibBuilder.importSymbols("CISCO-TC", "CiscoNetworkAddress", "TimeIntervalSec", "Unsigned64", "CiscoInetAddressMask", "CiscoAlarmSeverity")
CucsManagedObjectId, ciscoUnifiedComputingMIBObjects, CucsManagedObjectDn = mibBuilder.importSymbols("CISCO-UNIFIED-COMPUTING-MIB", "CucsManagedObjectId", "ciscoUnifiedComputingMIBObjects", "CucsManagedObjectDn")
CucsPolicyPolicyOwner, CucsTopInfoSyncPolicyState, CucsTopInfoPolicyState, CucsTopMode = mibBuilder.importSymbols("CISCO-UNIFIED-COMPUTING-TC-MIB", "CucsPolicyPolicyOwner", "CucsTopInfoSyncPolicyState", "CucsTopInfoPolicyState", "CucsTopMode")
InetAddressIPv4, InetAddressIPv6 = mibBuilder.importSymbols("INET-ADDRESS-MIB", "InetAddressIPv4", "InetAddressIPv6")
SnmpAdminString, = mibBuilder.importSymbols("SNMP-FRAMEWORK-MIB", "SnmpAdminString")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
MibIdentifier, Integer32, Unsigned32, iso, ModuleIdentity, Bits, MibScalar, MibTable, MibTableRow, MibTableColumn, NotificationType, TimeTicks, Counter32, Gauge32, Counter64, IpAddress, ObjectIdentity = mibBuilder.importSymbols("SNMPv2-SMI", "MibIdentifier", "Integer32", "Unsigned32", "iso", "ModuleIdentity", "Bits", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "NotificationType", "TimeTicks", "Counter32", "Gauge32", "Counter64", "IpAddress", "ObjectIdentity")
TruthValue, TextualConvention, TimeInterval, MacAddress, DateAndTime, RowPointer, DisplayString, TimeStamp = mibBuilder.importSymbols("SNMPv2-TC", "TruthValue", "TextualConvention", "TimeInterval", "MacAddress", "DateAndTime", "RowPointer", "DisplayString", "TimeStamp")
cucsTopObjects = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 49))
if mibBuilder.loadTexts: cucsTopObjects.setLastUpdated('201601180000Z')
if mibBuilder.loadTexts: cucsTopObjects.setOrganization('Cisco Systems Inc.')
cucsTopInfoPolicyTable = MibTable((1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 49, 5), )
if mibBuilder.loadTexts: cucsTopInfoPolicyTable.setStatus('current')
cucsTopInfoPolicyEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 49, 5, 1), ).setIndexNames((0, "CISCO-UNIFIED-COMPUTING-TOP-MIB", "cucsTopInfoPolicyInstanceId"))
if mibBuilder.loadTexts: cucsTopInfoPolicyEntry.setStatus('current')
cucsTopInfoPolicyInstanceId = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 49, 5, 1, 1), CucsManagedObjectId())
if mibBuilder.loadTexts: cucsTopInfoPolicyInstanceId.setStatus('current')
cucsTopInfoPolicyDn = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 49, 5, 1, 2), CucsManagedObjectDn()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cucsTopInfoPolicyDn.setStatus('current')
cucsTopInfoPolicyRn = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 49, 5, 1, 3), SnmpAdminString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cucsTopInfoPolicyRn.setStatus('current')
cucsTopInfoPolicyState = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 49, 5, 1, 4), CucsTopInfoPolicyState()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cucsTopInfoPolicyState.setStatus('current')
cucsTopInfoSyncPolicyTable = MibTable((1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 49, 6), )
if mibBuilder.loadTexts: cucsTopInfoSyncPolicyTable.setStatus('current')
cucsTopInfoSyncPolicyEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 49, 6, 1), ).setIndexNames((0, "CISCO-UNIFIED-COMPUTING-TOP-MIB", "cucsTopInfoSyncPolicyInstanceId"))
if mibBuilder.loadTexts: cucsTopInfoSyncPolicyEntry.setStatus('current')
cucsTopInfoSyncPolicyInstanceId = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 49, 6, 1, 1), CucsManagedObjectId())
if mibBuilder.loadTexts: cucsTopInfoSyncPolicyInstanceId.setStatus('current')
cucsTopInfoSyncPolicyDn = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 49, 6, 1, 2), CucsManagedObjectDn()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cucsTopInfoSyncPolicyDn.setStatus('current')
cucsTopInfoSyncPolicyRn = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 49, 6, 1, 3), SnmpAdminString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cucsTopInfoSyncPolicyRn.setStatus('current')
cucsTopInfoSyncPolicyDescr = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 49, 6, 1, 4), SnmpAdminString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cucsTopInfoSyncPolicyDescr.setStatus('current')
cucsTopInfoSyncPolicyIntId = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 49, 6, 1, 5), SnmpAdminString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cucsTopInfoSyncPolicyIntId.setStatus('current')
cucsTopInfoSyncPolicyName = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 49, 6, 1, 6), SnmpAdminString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cucsTopInfoSyncPolicyName.setStatus('current')
cucsTopInfoSyncPolicyPolicyLevel = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 49, 6, 1, 7), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cucsTopInfoSyncPolicyPolicyLevel.setStatus('current')
cucsTopInfoSyncPolicyPolicyOwner = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 49, 6, 1, 8), CucsPolicyPolicyOwner()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cucsTopInfoSyncPolicyPolicyOwner.setStatus('current')
cucsTopInfoSyncPolicyState = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 49, 6, 1, 9), CucsTopInfoSyncPolicyState()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cucsTopInfoSyncPolicyState.setStatus('current')
cucsTopMetaInfTable = MibTable((1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 49, 1), )
if mibBuilder.loadTexts: cucsTopMetaInfTable.setStatus('current')
cucsTopMetaInfEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 49, 1, 1), ).setIndexNames((0, "CISCO-UNIFIED-COMPUTING-TOP-MIB", "cucsTopMetaInfInstanceId"))
if mibBuilder.loadTexts: cucsTopMetaInfEntry.setStatus('current')
cucsTopMetaInfInstanceId = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 49, 1, 1, 1), CucsManagedObjectId())
if mibBuilder.loadTexts: cucsTopMetaInfInstanceId.setStatus('current')
cucsTopMetaInfDn = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 49, 1, 1, 2), CucsManagedObjectDn()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cucsTopMetaInfDn.setStatus('current')
cucsTopMetaInfRn = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 49, 1, 1, 3), SnmpAdminString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cucsTopMetaInfRn.setStatus('current')
cucsTopMetaInfEcode = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 49, 1, 1, 4), SnmpAdminString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cucsTopMetaInfEcode.setStatus('current')
cucsTopMetaInfName = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 49, 1, 1, 5), SnmpAdminString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cucsTopMetaInfName.setStatus('current')
cucsTopRootTable = MibTable((1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 49, 2), )
if mibBuilder.loadTexts: cucsTopRootTable.setStatus('current')
cucsTopRootEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 49, 2, 1), ).setIndexNames((0, "CISCO-UNIFIED-COMPUTING-TOP-MIB", "cucsTopRootInstanceId"))
if mibBuilder.loadTexts: cucsTopRootEntry.setStatus('current')
cucsTopRootInstanceId = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 49, 2, 1, 1), CucsManagedObjectId())
if mibBuilder.loadTexts: cucsTopRootInstanceId.setStatus('current')
cucsTopRootDn = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 49, 2, 1, 2), CucsManagedObjectDn()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cucsTopRootDn.setStatus('current')
cucsTopRootRn = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 49, 2, 1, 3), SnmpAdminString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cucsTopRootRn.setStatus('current')
cucsTopSysDefaultsTable = MibTable((1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 49, 4), )
if mibBuilder.loadTexts: cucsTopSysDefaultsTable.setStatus('current')
cucsTopSysDefaultsEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 49, 4, 1), ).setIndexNames((0, "CISCO-UNIFIED-COMPUTING-TOP-MIB", "cucsTopSysDefaultsInstanceId"))
if mibBuilder.loadTexts: cucsTopSysDefaultsEntry.setStatus('current')
cucsTopSysDefaultsInstanceId = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 49, 4, 1, 1), CucsManagedObjectId())
if mibBuilder.loadTexts: cucsTopSysDefaultsInstanceId.setStatus('current')
cucsTopSysDefaultsDn = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 49, 4, 1, 2), CucsManagedObjectDn()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cucsTopSysDefaultsDn.setStatus('current')
cucsTopSysDefaultsRn = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 49, 4, 1, 3), SnmpAdminString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cucsTopSysDefaultsRn.setStatus('current')
cucsTopSystemTable = MibTable((1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 49, 3), )
if mibBuilder.loadTexts: cucsTopSystemTable.setStatus('current')
cucsTopSystemEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 49, 3, 1), ).setIndexNames((0, "CISCO-UNIFIED-COMPUTING-TOP-MIB", "cucsTopSystemInstanceId"))
if mibBuilder.loadTexts: cucsTopSystemEntry.setStatus('current')
cucsTopSystemInstanceId = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 49, 3, 1, 1), CucsManagedObjectId())
if mibBuilder.loadTexts: cucsTopSystemInstanceId.setStatus('current')
cucsTopSystemDn = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 49, 3, 1, 2), CucsManagedObjectDn()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cucsTopSystemDn.setStatus('current')
cucsTopSystemRn = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 49, 3, 1, 3), SnmpAdminString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cucsTopSystemRn.setStatus('current')
cucsTopSystemAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 49, 3, 1, 4), InetAddressIPv4()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cucsTopSystemAddress.setStatus('current')
cucsTopSystemCurrentTime = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 49, 3, 1, 5), DateAndTime()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cucsTopSystemCurrentTime.setStatus('current')
cucsTopSystemMode = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 49, 3, 1, 6), CucsTopMode()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cucsTopSystemMode.setStatus('current')
cucsTopSystemName = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 49, 3, 1, 7), SnmpAdminString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cucsTopSystemName.setStatus('current')
cucsTopSystemSystemUpTime = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 49, 3, 1, 8), TimeIntervalSec()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cucsTopSystemSystemUpTime.setStatus('current')
cucsTopSystemDescr = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 49, 3, 1, 9), SnmpAdminString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cucsTopSystemDescr.setStatus('current')
cucsTopSystemOwner = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 49, 3, 1, 10), SnmpAdminString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cucsTopSystemOwner.setStatus('current')
cucsTopSystemSite = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 49, 3, 1, 11), SnmpAdminString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cucsTopSystemSite.setStatus('current')
cucsTopSystemIpv6Addr = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 49, 3, 1, 12), InetAddressIPv6()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cucsTopSystemIpv6Addr.setStatus('current')
mibBuilder.exportSymbols("CISCO-UNIFIED-COMPUTING-TOP-MIB", cucsTopInfoPolicyInstanceId=cucsTopInfoPolicyInstanceId, cucsTopRootTable=cucsTopRootTable, cucsTopMetaInfRn=cucsTopMetaInfRn, cucsTopSystemIpv6Addr=cucsTopSystemIpv6Addr, cucsTopSysDefaultsTable=cucsTopSysDefaultsTable, cucsTopInfoSyncPolicyState=cucsTopInfoSyncPolicyState, cucsTopSystemDn=cucsTopSystemDn, cucsTopMetaInfDn=cucsTopMetaInfDn, cucsTopInfoSyncPolicyEntry=cucsTopInfoSyncPolicyEntry, cucsTopInfoPolicyDn=cucsTopInfoPolicyDn, cucsTopSystemTable=cucsTopSystemTable, cucsTopSystemDescr=cucsTopSystemDescr, cucsTopObjects=cucsTopObjects, cucsTopSysDefaultsRn=cucsTopSysDefaultsRn, cucsTopInfoPolicyTable=cucsTopInfoPolicyTable, cucsTopSystemInstanceId=cucsTopSystemInstanceId, cucsTopSystemMode=cucsTopSystemMode, cucsTopMetaInfInstanceId=cucsTopMetaInfInstanceId, cucsTopSystemCurrentTime=cucsTopSystemCurrentTime, cucsTopRootEntry=cucsTopRootEntry, cucsTopInfoSyncPolicyName=cucsTopInfoSyncPolicyName, cucsTopRootRn=cucsTopRootRn, cucsTopInfoSyncPolicyIntId=cucsTopInfoSyncPolicyIntId, cucsTopInfoSyncPolicyRn=cucsTopInfoSyncPolicyRn, cucsTopInfoSyncPolicyPolicyOwner=cucsTopInfoSyncPolicyPolicyOwner, cucsTopInfoSyncPolicyDescr=cucsTopInfoSyncPolicyDescr, cucsTopMetaInfEcode=cucsTopMetaInfEcode, cucsTopSystemOwner=cucsTopSystemOwner, cucsTopSysDefaultsDn=cucsTopSysDefaultsDn, cucsTopInfoSyncPolicyDn=cucsTopInfoSyncPolicyDn, cucsTopRootDn=cucsTopRootDn, cucsTopSysDefaultsInstanceId=cucsTopSysDefaultsInstanceId, cucsTopSystemAddress=cucsTopSystemAddress, cucsTopInfoPolicyEntry=cucsTopInfoPolicyEntry, cucsTopRootInstanceId=cucsTopRootInstanceId, cucsTopSystemSite=cucsTopSystemSite, cucsTopSystemName=cucsTopSystemName, cucsTopInfoSyncPolicyPolicyLevel=cucsTopInfoSyncPolicyPolicyLevel, cucsTopMetaInfName=cucsTopMetaInfName, cucsTopInfoSyncPolicyTable=cucsTopInfoSyncPolicyTable, cucsTopMetaInfEntry=cucsTopMetaInfEntry, cucsTopSystemEntry=cucsTopSystemEntry, cucsTopSysDefaultsEntry=cucsTopSysDefaultsEntry, cucsTopSystemRn=cucsTopSystemRn, cucsTopInfoPolicyRn=cucsTopInfoPolicyRn, cucsTopInfoSyncPolicyInstanceId=cucsTopInfoSyncPolicyInstanceId, cucsTopSystemSystemUpTime=cucsTopSystemSystemUpTime, cucsTopMetaInfTable=cucsTopMetaInfTable, cucsTopInfoPolicyState=cucsTopInfoPolicyState, PYSNMP_MODULE_ID=cucsTopObjects)
