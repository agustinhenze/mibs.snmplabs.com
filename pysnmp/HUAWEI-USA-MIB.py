#
# PySNMP MIB module HUAWEI-USA-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/HUAWEI-USA-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 19:37:35 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsUnion, ConstraintsIntersection, SingleValueConstraint, ValueRangeConstraint, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "ConstraintsIntersection", "SingleValueConstraint", "ValueRangeConstraint", "ValueSizeConstraint")
hwBRASMib, = mibBuilder.importSymbols("HUAWEI-MIB", "hwBRASMib")
EnabledStatus, = mibBuilder.importSymbols("P-BRIDGE-MIB", "EnabledStatus")
NotificationGroup, ModuleCompliance, ObjectGroup = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance", "ObjectGroup")
Counter64, Unsigned32, Bits, iso, ModuleIdentity, ObjectIdentity, NotificationType, Counter32, MibScalar, MibTable, MibTableRow, MibTableColumn, TimeTicks, Gauge32, IpAddress, Integer32, MibIdentifier = mibBuilder.importSymbols("SNMPv2-SMI", "Counter64", "Unsigned32", "Bits", "iso", "ModuleIdentity", "ObjectIdentity", "NotificationType", "Counter32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "TimeTicks", "Gauge32", "IpAddress", "Integer32", "MibIdentifier")
DisplayString, RowStatus, TextualConvention, MacAddress = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "RowStatus", "TextualConvention", "MacAddress")
hwUSA = ModuleIdentity((1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 20))
hwUSA.setRevisions(('2010-08-11 16:00', '2010-09-11 16:00',))
if mibBuilder.loadTexts: hwUSA.setLastUpdated('201008111600Z')
if mibBuilder.loadTexts: hwUSA.setOrganization('Huawei Technologies Co.,Ltd.')
hwUSAObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 20, 1))
hwUSAConfigTable = MibTable((1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 20, 1, 1), )
if mibBuilder.loadTexts: hwUSAConfigTable.setStatus('current')
hwUSAConfigEntry = MibTableRow((1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 20, 1, 1, 1), ).setIndexNames((0, "HUAWEI-USA-MIB", "hwUSAPortIndex"))
if mibBuilder.loadTexts: hwUSAConfigEntry.setStatus('current')
hwUSAPortIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 20, 1, 1, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 32767))).setMaxAccess("readonly")
if mibBuilder.loadTexts: hwUSAPortIndex.setStatus('current')
hwUSAInterfaceName = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 20, 1, 1, 1, 2), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(1, 64))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hwUSAInterfaceName.setStatus('current')
hwAuthenAccessPoint = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 20, 1, 1, 1, 3), EnabledStatus().clone()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hwAuthenAccessPoint.setStatus('current')
hwAssociateUserTable = MibTable((1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 20, 1, 2), )
if mibBuilder.loadTexts: hwAssociateUserTable.setStatus('current')
hwAssociateUserEntry = MibTableRow((1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 20, 1, 2, 1), ).setIndexNames((0, "HUAWEI-USA-MIB", "hwAssociateUserIndex"))
if mibBuilder.loadTexts: hwAssociateUserEntry.setStatus('current')
hwAssociateUserIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 20, 1, 2, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 32767))).setMaxAccess("readonly")
if mibBuilder.loadTexts: hwAssociateUserIndex.setStatus('current')
hwAssociateUserMac = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 20, 1, 2, 1, 2), MacAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hwAssociateUserMac.setStatus('current')
hwAssociateUserIp = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 20, 1, 2, 1, 3), IpAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hwAssociateUserIp.setStatus('current')
hwAssociateUserStates = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 20, 1, 2, 1, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1, 2))).clone(namedValues=NamedValues(("idle", 0), ("associated", 1), ("up", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: hwAssociateUserStates.setStatus('current')
hwAssociateType = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 20, 1, 2, 1, 5), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3))).clone(namedValues=NamedValues(("arp", 0), ("dot1x", 1), ("dhcp", 2), ("http", 3)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: hwAssociateType.setStatus('current')
hwUserDetectInterval = MibScalar((1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 20, 1, 3), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 65535))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hwUserDetectInterval.setStatus('current')
hwUserDetectRetry = MibScalar((1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 20, 1, 4), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 255))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hwUserDetectRetry.setStatus('current')
hwUserSyncInterval = MibScalar((1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 20, 1, 5), Integer32().subtype(subtypeSpec=ValueRangeConstraint(60, 3600))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hwUserSyncInterval.setStatus('current')
hwGlobalLinkDownOffline = MibScalar((1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 20, 1, 6), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 65535))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hwGlobalLinkDownOffline.setStatus('current')
hwGlobalControlDownOffline = MibScalar((1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 20, 1, 7), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 65535))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hwGlobalControlDownOffline.setStatus('current')
hwAuthenSpeedLimitMaxNum = MibScalar((1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 20, 1, 8), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 65535))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hwAuthenSpeedLimitMaxNum.setStatus('current')
hwAuthenSpeedLimitInterval = MibScalar((1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 20, 1, 9), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 65535))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hwAuthenSpeedLimitInterval.setStatus('current')
mibBuilder.exportSymbols("HUAWEI-USA-MIB", hwUserDetectInterval=hwUserDetectInterval, hwGlobalLinkDownOffline=hwGlobalLinkDownOffline, hwAuthenSpeedLimitInterval=hwAuthenSpeedLimitInterval, hwUSAConfigEntry=hwUSAConfigEntry, hwAssociateType=hwAssociateType, hwAuthenAccessPoint=hwAuthenAccessPoint, hwUSA=hwUSA, hwAssociateUserEntry=hwAssociateUserEntry, hwAssociateUserMac=hwAssociateUserMac, hwUSAInterfaceName=hwUSAInterfaceName, hwAuthenSpeedLimitMaxNum=hwAuthenSpeedLimitMaxNum, PYSNMP_MODULE_ID=hwUSA, hwAssociateUserIndex=hwAssociateUserIndex, hwAssociateUserTable=hwAssociateUserTable, hwGlobalControlDownOffline=hwGlobalControlDownOffline, hwUSAPortIndex=hwUSAPortIndex, hwUserSyncInterval=hwUserSyncInterval, hwAssociateUserIp=hwAssociateUserIp, hwAssociateUserStates=hwAssociateUserStates, hwUSAObjects=hwUSAObjects, hwUSAConfigTable=hwUSAConfigTable, hwUserDetectRetry=hwUserDetectRetry)
