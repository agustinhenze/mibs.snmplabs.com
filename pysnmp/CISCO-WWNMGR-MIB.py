#
# PySNMP MIB module CISCO-WWNMGR-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/CISCO-WWNMGR-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 18:05:26 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
OctetString, Integer, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "OctetString", "Integer", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
SingleValueConstraint, ConstraintsIntersection, ValueSizeConstraint, ValueRangeConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "SingleValueConstraint", "ConstraintsIntersection", "ValueSizeConstraint", "ValueRangeConstraint", "ConstraintsUnion")
ciscoMgmt, = mibBuilder.importSymbols("CISCO-SMI", "ciscoMgmt")
FcNameId, = mibBuilder.importSymbols("CISCO-ST-TC", "FcNameId")
vsanIndex, = mibBuilder.importSymbols("CISCO-VSAN-MIB", "vsanIndex")
NotificationGroup, ModuleCompliance, ObjectGroup = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance", "ObjectGroup")
ModuleIdentity, Unsigned32, iso, Counter32, Bits, TimeTicks, Counter64, Gauge32, MibIdentifier, Integer32, IpAddress, MibScalar, MibTable, MibTableRow, MibTableColumn, NotificationType, ObjectIdentity = mibBuilder.importSymbols("SNMPv2-SMI", "ModuleIdentity", "Unsigned32", "iso", "Counter32", "Bits", "TimeTicks", "Counter64", "Gauge32", "MibIdentifier", "Integer32", "IpAddress", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "NotificationType", "ObjectIdentity")
RowStatus, TextualConvention, DisplayString, StorageType, MacAddress = mibBuilder.importSymbols("SNMPv2-TC", "RowStatus", "TextualConvention", "DisplayString", "StorageType", "MacAddress")
ciscoWwnmgrMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 9, 286))
ciscoWwnmgrMIB.setRevisions(('2006-02-06 00:00', '2002-10-01 00:00',))
if mibBuilder.loadTexts: ciscoWwnmgrMIB.setLastUpdated('200602060000Z')
if mibBuilder.loadTexts: ciscoWwnmgrMIB.setOrganization('Cisco Systems Inc. ')
ciscoWwnmMIBObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 286, 1))
wwnmConfigurationGroup = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 286, 1, 1))
wwnmNotificationGroup = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 286, 1, 2))
wwnmNotification = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 286, 1, 2, 1))
wwnmNotificationPrefix = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 286, 1, 2, 1, 0))
wwnmSecondaryBaseMacAddress = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 286, 1, 1, 1), MacAddress().clone(hexValue="000000000000")).setMaxAccess("readwrite")
if mibBuilder.loadTexts: wwnmSecondaryBaseMacAddress.setStatus('current')
wwnmSecondaryMacAddressRange = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 286, 1, 1, 2), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(0, 4294967295))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: wwnmSecondaryMacAddressRange.setStatus('current')
wwnmType1MaxWwns = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 286, 1, 1, 3), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(0, 4294967295))).setMaxAccess("readonly")
if mibBuilder.loadTexts: wwnmType1MaxWwns.setStatus('current')
wwnmType1AvailableWwns = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 286, 1, 1, 4), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: wwnmType1AvailableWwns.setStatus('current')
wwnmTypeOtherMaxWwns = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 286, 1, 1, 5), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(0, 4294967295))).setMaxAccess("readonly")
if mibBuilder.loadTexts: wwnmTypeOtherMaxWwns.setStatus('current')
wwnmTypeOtherAvailableWwns = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 286, 1, 1, 6), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: wwnmTypeOtherAvailableWwns.setStatus('current')
wwnmType1ReservedWwns = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 286, 1, 1, 7), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(0, 4294967295))).setMaxAccess("readonly")
if mibBuilder.loadTexts: wwnmType1ReservedWwns.setStatus('current')
wwnmTypeOtherReservedWwns = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 286, 1, 1, 8), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(0, 4294967295))).setMaxAccess("readonly")
if mibBuilder.loadTexts: wwnmTypeOtherReservedWwns.setStatus('current')
wwnmVsanWwnTable = MibTable((1, 3, 6, 1, 4, 1, 9, 9, 286, 1, 1, 9), )
if mibBuilder.loadTexts: wwnmVsanWwnTable.setStatus('current')
wwnmVsanWwnEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9, 9, 286, 1, 1, 9, 1), ).setIndexNames((0, "CISCO-VSAN-MIB", "vsanIndex"))
if mibBuilder.loadTexts: wwnmVsanWwnEntry.setStatus('current')
wwnmVsanWwn = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 286, 1, 1, 9, 1, 1), FcNameId()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: wwnmVsanWwn.setStatus('current')
wwnmVsanWwnStorageType = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 286, 1, 1, 9, 1, 2), StorageType().clone('nonVolatile')).setMaxAccess("readonly")
if mibBuilder.loadTexts: wwnmVsanWwnStorageType.setStatus('current')
wwnmVsanWwnRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 286, 1, 1, 9, 1, 3), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: wwnmVsanWwnRowStatus.setStatus('current')
wwnmType1WwnShortageNotify = NotificationType((1, 3, 6, 1, 4, 1, 9, 9, 286, 1, 2, 1, 0, 1)).setObjects(("CISCO-WWNMGR-MIB", "wwnmType1AvailableWwns"))
if mibBuilder.loadTexts: wwnmType1WwnShortageNotify.setStatus('current')
wwnmType1WwnAvailableNotify = NotificationType((1, 3, 6, 1, 4, 1, 9, 9, 286, 1, 2, 1, 0, 2)).setObjects(("CISCO-WWNMGR-MIB", "wwnmType1AvailableWwns"))
if mibBuilder.loadTexts: wwnmType1WwnAvailableNotify.setStatus('current')
wwnmTypeOtherWwnShortageNotify = NotificationType((1, 3, 6, 1, 4, 1, 9, 9, 286, 1, 2, 1, 0, 3)).setObjects(("CISCO-WWNMGR-MIB", "wwnmTypeOtherAvailableWwns"))
if mibBuilder.loadTexts: wwnmTypeOtherWwnShortageNotify.setStatus('current')
wwnmTypeOtherWwnAvailableNotify = NotificationType((1, 3, 6, 1, 4, 1, 9, 9, 286, 1, 2, 1, 0, 4)).setObjects(("CISCO-WWNMGR-MIB", "wwnmTypeOtherAvailableWwns"))
if mibBuilder.loadTexts: wwnmTypeOtherWwnAvailableNotify.setStatus('current')
ciscoWwnmMIBConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 286, 2))
ciscoWwnmMIBCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 286, 2, 1))
ciscoWwnmMIBGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 286, 2, 2))
ciscoWwnmMIBCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 9, 9, 286, 2, 1, 1)).setObjects(("CISCO-WWNMGR-MIB", "cwmWwnmConfigurationGroup"), ("CISCO-WWNMGR-MIB", "cwmWwnmNotificationGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoWwnmMIBCompliance = ciscoWwnmMIBCompliance.setStatus('deprecated')
ciscoWwnmMIBCompliance1 = ModuleCompliance((1, 3, 6, 1, 4, 1, 9, 9, 286, 2, 1, 2)).setObjects(("CISCO-WWNMGR-MIB", "cwmWwnmConfigurationGroup"), ("CISCO-WWNMGR-MIB", "cwmWwnmVsanWwnGroup"), ("CISCO-WWNMGR-MIB", "cwmWwnmNotificationGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoWwnmMIBCompliance1 = ciscoWwnmMIBCompliance1.setStatus('current')
cwmWwnmConfigurationGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 286, 2, 2, 6)).setObjects(("CISCO-WWNMGR-MIB", "wwnmSecondaryBaseMacAddress"), ("CISCO-WWNMGR-MIB", "wwnmSecondaryMacAddressRange"), ("CISCO-WWNMGR-MIB", "wwnmType1MaxWwns"), ("CISCO-WWNMGR-MIB", "wwnmType1AvailableWwns"), ("CISCO-WWNMGR-MIB", "wwnmTypeOtherMaxWwns"), ("CISCO-WWNMGR-MIB", "wwnmTypeOtherAvailableWwns"), ("CISCO-WWNMGR-MIB", "wwnmType1ReservedWwns"), ("CISCO-WWNMGR-MIB", "wwnmTypeOtherReservedWwns"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cwmWwnmConfigurationGroup = cwmWwnmConfigurationGroup.setStatus('current')
cwmWwnmNotificationGroup = NotificationGroup((1, 3, 6, 1, 4, 1, 9, 9, 286, 2, 2, 8)).setObjects(("CISCO-WWNMGR-MIB", "wwnmType1WwnShortageNotify"), ("CISCO-WWNMGR-MIB", "wwnmType1WwnAvailableNotify"), ("CISCO-WWNMGR-MIB", "wwnmTypeOtherWwnShortageNotify"), ("CISCO-WWNMGR-MIB", "wwnmTypeOtherWwnAvailableNotify"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cwmWwnmNotificationGroup = cwmWwnmNotificationGroup.setStatus('current')
cwmWwnmVsanWwnGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 286, 2, 2, 9)).setObjects(("CISCO-WWNMGR-MIB", "wwnmVsanWwn"), ("CISCO-WWNMGR-MIB", "wwnmVsanWwnStorageType"), ("CISCO-WWNMGR-MIB", "wwnmVsanWwnRowStatus"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cwmWwnmVsanWwnGroup = cwmWwnmVsanWwnGroup.setStatus('current')
mibBuilder.exportSymbols("CISCO-WWNMGR-MIB", wwnmSecondaryBaseMacAddress=wwnmSecondaryBaseMacAddress, wwnmType1ReservedWwns=wwnmType1ReservedWwns, cwmWwnmNotificationGroup=cwmWwnmNotificationGroup, ciscoWwnmMIBCompliance=ciscoWwnmMIBCompliance, wwnmVsanWwnRowStatus=wwnmVsanWwnRowStatus, wwnmType1MaxWwns=wwnmType1MaxWwns, wwnmConfigurationGroup=wwnmConfigurationGroup, wwnmVsanWwnStorageType=wwnmVsanWwnStorageType, wwnmTypeOtherWwnAvailableNotify=wwnmTypeOtherWwnAvailableNotify, wwnmVsanWwnTable=wwnmVsanWwnTable, wwnmNotificationGroup=wwnmNotificationGroup, wwnmTypeOtherWwnShortageNotify=wwnmTypeOtherWwnShortageNotify, wwnmType1AvailableWwns=wwnmType1AvailableWwns, wwnmNotification=wwnmNotification, PYSNMP_MODULE_ID=ciscoWwnmgrMIB, ciscoWwnmMIBCompliances=ciscoWwnmMIBCompliances, ciscoWwnmgrMIB=ciscoWwnmgrMIB, wwnmNotificationPrefix=wwnmNotificationPrefix, cwmWwnmVsanWwnGroup=cwmWwnmVsanWwnGroup, cwmWwnmConfigurationGroup=cwmWwnmConfigurationGroup, wwnmTypeOtherAvailableWwns=wwnmTypeOtherAvailableWwns, ciscoWwnmMIBObjects=ciscoWwnmMIBObjects, ciscoWwnmMIBConformance=ciscoWwnmMIBConformance, wwnmType1WwnShortageNotify=wwnmType1WwnShortageNotify, wwnmTypeOtherReservedWwns=wwnmTypeOtherReservedWwns, ciscoWwnmMIBGroups=ciscoWwnmMIBGroups, wwnmVsanWwn=wwnmVsanWwn, wwnmTypeOtherMaxWwns=wwnmTypeOtherMaxWwns, ciscoWwnmMIBCompliance1=ciscoWwnmMIBCompliance1, wwnmSecondaryMacAddressRange=wwnmSecondaryMacAddressRange, wwnmType1WwnAvailableNotify=wwnmType1WwnAvailableNotify, wwnmVsanWwnEntry=wwnmVsanWwnEntry)
