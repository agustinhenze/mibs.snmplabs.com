#
# PySNMP MIB module CISCO-MGX82XX-RPM-SUBIF-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/CISCO-MGX82XX-RPM-SUBIF-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 17:50:33 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsUnion, ValueSizeConstraint, ConstraintsIntersection, ValueRangeConstraint, SingleValueConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "ValueSizeConstraint", "ConstraintsIntersection", "ValueRangeConstraint", "SingleValueConstraint")
rpmPort, = mibBuilder.importSymbols("BASIS-MIB", "rpmPort")
ciscoWan, = mibBuilder.importSymbols("CISCOWAN-SMI", "ciscoWan")
NotificationGroup, ObjectGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ObjectGroup", "ModuleCompliance")
Counter32, Gauge32, IpAddress, Bits, NotificationType, Unsigned32, MibIdentifier, Integer32, TimeTicks, iso, MibScalar, MibTable, MibTableRow, MibTableColumn, ObjectIdentity, Counter64, ModuleIdentity = mibBuilder.importSymbols("SNMPv2-SMI", "Counter32", "Gauge32", "IpAddress", "Bits", "NotificationType", "Unsigned32", "MibIdentifier", "Integer32", "TimeTicks", "iso", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "ObjectIdentity", "Counter64", "ModuleIdentity")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
ciscoMgx82xxRpmSubIfMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 351, 150, 60))
ciscoMgx82xxRpmSubIfMIB.setRevisions(('2002-09-08 00:00',))
if mibBuilder.loadTexts: ciscoMgx82xxRpmSubIfMIB.setLastUpdated('200209080000Z')
if mibBuilder.loadTexts: ciscoMgx82xxRpmSubIfMIB.setOrganization('Cisco Systems, Inc.')
rpmPortTable = MibTable((1, 3, 6, 1, 4, 1, 351, 110, 5, 2, 9, 1, 1), )
if mibBuilder.loadTexts: rpmPortTable.setStatus('current')
rpmPortEntry = MibTableRow((1, 3, 6, 1, 4, 1, 351, 110, 5, 2, 9, 1, 1, 1), ).setIndexNames((0, "CISCO-MGX82XX-RPM-SUBIF-MIB", "rpmPortSlotNum"), (0, "CISCO-MGX82XX-RPM-SUBIF-MIB", "rpmPortSubInterface"))
if mibBuilder.loadTexts: rpmPortEntry.setStatus('current')
rpmPortSlotNum = MibTableColumn((1, 3, 6, 1, 4, 1, 351, 110, 5, 2, 9, 1, 1, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 30))).setMaxAccess("readonly")
if mibBuilder.loadTexts: rpmPortSlotNum.setStatus('current')
rpmPortInterface = MibTableColumn((1, 3, 6, 1, 4, 1, 351, 110, 5, 2, 9, 1, 1, 1, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 2147483647))).setMaxAccess("readonly")
if mibBuilder.loadTexts: rpmPortInterface.setStatus('current')
rpmPortSubInterface = MibTableColumn((1, 3, 6, 1, 4, 1, 351, 110, 5, 2, 9, 1, 1, 1, 3), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 2147483647))).setMaxAccess("readonly")
if mibBuilder.loadTexts: rpmPortSubInterface.setStatus('current')
rpmPortRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 351, 110, 5, 2, 9, 1, 1, 1, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("add", 1), ("del", 2), ("mod", 3)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: rpmPortRowStatus.setStatus('current')
rpmPortIpAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 351, 110, 5, 2, 9, 1, 1, 1, 5), IpAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rpmPortIpAddress.setStatus('current')
rpmPortSubNetMask = MibTableColumn((1, 3, 6, 1, 4, 1, 351, 110, 5, 2, 9, 1, 1, 1, 6), IpAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rpmPortSubNetMask.setStatus('current')
rpmPortState = MibTableColumn((1, 3, 6, 1, 4, 1, 351, 110, 5, 2, 9, 1, 1, 1, 7), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("notConfigured", 1), ("active", 2), ("failed", 3)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: rpmPortState.setStatus('current')
cmrSubIfMIBConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 351, 150, 60, 2))
cmrSubIfMIBCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 351, 150, 60, 2, 1))
cmrSubIfMIBGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 351, 150, 60, 2, 2))
cmrSubIfMIBCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 351, 150, 60, 2, 1, 1)).setObjects(("CISCO-MGX82XX-RPM-SUBIF-MIB", "cmrSubIfMIBGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cmrSubIfMIBCompliance = cmrSubIfMIBCompliance.setStatus('current')
cmrSubIfMIBGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 351, 150, 60, 2, 2, 1)).setObjects(("CISCO-MGX82XX-RPM-SUBIF-MIB", "rpmPortSlotNum"), ("CISCO-MGX82XX-RPM-SUBIF-MIB", "rpmPortInterface"), ("CISCO-MGX82XX-RPM-SUBIF-MIB", "rpmPortSubInterface"), ("CISCO-MGX82XX-RPM-SUBIF-MIB", "rpmPortRowStatus"), ("CISCO-MGX82XX-RPM-SUBIF-MIB", "rpmPortIpAddress"), ("CISCO-MGX82XX-RPM-SUBIF-MIB", "rpmPortSubNetMask"), ("CISCO-MGX82XX-RPM-SUBIF-MIB", "rpmPortState"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cmrSubIfMIBGroup = cmrSubIfMIBGroup.setStatus('current')
mibBuilder.exportSymbols("CISCO-MGX82XX-RPM-SUBIF-MIB", rpmPortIpAddress=rpmPortIpAddress, cmrSubIfMIBGroups=cmrSubIfMIBGroups, rpmPortTable=rpmPortTable, rpmPortRowStatus=rpmPortRowStatus, rpmPortState=rpmPortState, PYSNMP_MODULE_ID=ciscoMgx82xxRpmSubIfMIB, rpmPortEntry=rpmPortEntry, ciscoMgx82xxRpmSubIfMIB=ciscoMgx82xxRpmSubIfMIB, cmrSubIfMIBConformance=cmrSubIfMIBConformance, cmrSubIfMIBCompliances=cmrSubIfMIBCompliances, rpmPortSubInterface=rpmPortSubInterface, rpmPortInterface=rpmPortInterface, rpmPortSubNetMask=rpmPortSubNetMask, rpmPortSlotNum=rpmPortSlotNum, cmrSubIfMIBCompliance=cmrSubIfMIBCompliance, cmrSubIfMIBGroup=cmrSubIfMIBGroup)
