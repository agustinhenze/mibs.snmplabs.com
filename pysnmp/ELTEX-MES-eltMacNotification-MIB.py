#
# PySNMP MIB module ELTEX-MES-eltMacNotification-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/ELTEX-MES-eltMacNotification-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 18:47:57 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
ObjectIdentifier, Integer, OctetString = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "Integer", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsUnion, SingleValueConstraint, ConstraintsIntersection, ValueRangeConstraint, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "SingleValueConstraint", "ConstraintsIntersection", "ValueRangeConstraint", "ValueSizeConstraint")
VlanIndex, = mibBuilder.importSymbols("CISCO-VTP-MIB", "VlanIndex")
eltMesMng, = mibBuilder.importSymbols("ELTEX-MES", "eltMesMng")
ifIndex, = mibBuilder.importSymbols("IF-MIB", "ifIndex")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
IpAddress, TimeTicks, iso, Counter32, ObjectIdentity, Unsigned32, Integer32, Counter64, MibScalar, MibTable, MibTableRow, MibTableColumn, Gauge32, MibIdentifier, ModuleIdentity, Bits, NotificationType = mibBuilder.importSymbols("SNMPv2-SMI", "IpAddress", "TimeTicks", "iso", "Counter32", "ObjectIdentity", "Unsigned32", "Integer32", "Counter64", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Gauge32", "MibIdentifier", "ModuleIdentity", "Bits", "NotificationType")
TextualConvention, DisplayString, TruthValue, TimeStamp, MacAddress = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString", "TruthValue", "TimeStamp", "MacAddress")
eltMesMacNotificationMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 35265, 1, 23, 1, 7))
eltMesMacNotificationMIB.setRevisions(('2015-11-05 00:00', '2015-11-19 00:00',))
if mibBuilder.loadTexts: eltMesMacNotificationMIB.setLastUpdated('201511190000Z')
if mibBuilder.loadTexts: eltMesMacNotificationMIB.setOrganization('Eltex Enterprise Co, Ltd.')
eltMesMacNotificationObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 35265, 1, 23, 1, 7, 1))
eltMesMnFlappingObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 35265, 1, 23, 1, 7, 1, 1))
eltMnFlappingFeatureEnabled = MibScalar((1, 3, 6, 1, 4, 1, 35265, 1, 23, 1, 7, 1, 1, 1), TruthValue().clone('true')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: eltMnFlappingFeatureEnabled.setStatus('deprecated')
eltMnFlappingNotificationsEnabled = MibScalar((1, 3, 6, 1, 4, 1, 35265, 1, 23, 1, 7, 1, 1, 2), TruthValue().clone('true')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: eltMnFlappingNotificationsEnabled.setStatus('deprecated')
eltMnFlappingAddress = MibScalar((1, 3, 6, 1, 4, 1, 35265, 1, 23, 1, 7, 1, 1, 3), MacAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: eltMnFlappingAddress.setStatus('deprecated')
eltMnFlappingVlanNumber = MibScalar((1, 3, 6, 1, 4, 1, 35265, 1, 23, 1, 7, 1, 1, 4), VlanIndex()).setMaxAccess("readonly")
if mibBuilder.loadTexts: eltMnFlappingVlanNumber.setStatus('deprecated')
eltMnFlappingFirstPortId = MibScalar((1, 3, 6, 1, 4, 1, 35265, 1, 23, 1, 7, 1, 1, 5), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 65535))).setMaxAccess("readonly")
if mibBuilder.loadTexts: eltMnFlappingFirstPortId.setStatus('deprecated')
eltMnFlappingSecondPortId = MibScalar((1, 3, 6, 1, 4, 1, 35265, 1, 23, 1, 7, 1, 1, 6), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 65535))).setMaxAccess("readonly")
if mibBuilder.loadTexts: eltMnFlappingSecondPortId.setStatus('deprecated')
eltMnFlappingTime = MibScalar((1, 3, 6, 1, 4, 1, 35265, 1, 23, 1, 7, 1, 1, 7), TimeStamp()).setMaxAccess("readonly")
if mibBuilder.loadTexts: eltMnFlappingTime.setStatus('deprecated')
eltMesMnNotificationPrefix = MibIdentifier((1, 3, 6, 1, 4, 1, 35265, 1, 23, 1, 7, 2))
eltMesMnNotifications = MibIdentifier((1, 3, 6, 1, 4, 1, 35265, 1, 23, 1, 7, 2, 0))
eltMnFlappingNotification = NotificationType((1, 3, 6, 1, 4, 1, 35265, 1, 23, 1, 7, 2, 0, 1)).setObjects(("ELTEX-MES-eltMacNotification-MIB", "eltMnFlappingAddress"), ("ELTEX-MES-eltMacNotification-MIB", "eltMnFlappingVlanNumber"), ("ELTEX-MES-eltMacNotification-MIB", "eltMnFlappingFirstPortId"), ("ELTEX-MES-eltMacNotification-MIB", "eltMnFlappingSecondPortId"), ("ELTEX-MES-eltMacNotification-MIB", "eltMnFlappingTime"))
if mibBuilder.loadTexts: eltMnFlappingNotification.setStatus('deprecated')
mibBuilder.exportSymbols("ELTEX-MES-eltMacNotification-MIB", eltMesMacNotificationMIB=eltMesMacNotificationMIB, eltMnFlappingVlanNumber=eltMnFlappingVlanNumber, eltMesMnFlappingObjects=eltMesMnFlappingObjects, eltMnFlappingFeatureEnabled=eltMnFlappingFeatureEnabled, PYSNMP_MODULE_ID=eltMesMacNotificationMIB, eltMnFlappingTime=eltMnFlappingTime, eltMnFlappingSecondPortId=eltMnFlappingSecondPortId, eltMnFlappingNotification=eltMnFlappingNotification, eltMesMnNotificationPrefix=eltMesMnNotificationPrefix, eltMesMnNotifications=eltMesMnNotifications, eltMesMacNotificationObjects=eltMesMacNotificationObjects, eltMnFlappingFirstPortId=eltMnFlappingFirstPortId, eltMnFlappingNotificationsEnabled=eltMnFlappingNotificationsEnabled, eltMnFlappingAddress=eltMnFlappingAddress)