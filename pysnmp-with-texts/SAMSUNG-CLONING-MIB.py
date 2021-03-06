#
# PySNMP MIB module SAMSUNG-CLONING-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/SAMSUNG-CLONING-MIB
# Produced by pysmi-0.3.4 at Wed May  1 15:00:33 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ValueRangeConstraint, ConstraintsIntersection, ConstraintsUnion, SingleValueConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ValueRangeConstraint", "ConstraintsIntersection", "ConstraintsUnion", "SingleValueConstraint")
hrDeviceIndex, = mibBuilder.importSymbols("HOST-RESOURCES-MIB", "hrDeviceIndex")
samsungCommonMIB, = mibBuilder.importSymbols("SAMSUNG-COMMON-MIB", "samsungCommonMIB")
ModuleCompliance, ObjectGroup, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "ObjectGroup", "NotificationGroup")
MibScalar, MibTable, MibTableRow, MibTableColumn, iso, Gauge32, MibIdentifier, ObjectIdentity, Integer32, NotificationType, Bits, Counter64, Unsigned32, ModuleIdentity, Counter32, TimeTicks, IpAddress = mibBuilder.importSymbols("SNMPv2-SMI", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "iso", "Gauge32", "MibIdentifier", "ObjectIdentity", "Integer32", "NotificationType", "Bits", "Counter64", "Unsigned32", "ModuleIdentity", "Counter32", "TimeTicks", "IpAddress")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
scmCloningMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 236, 11, 5, 11, 82))
if mibBuilder.loadTexts: scmCloningMIB.setLastUpdated('200511090000Z')
if mibBuilder.loadTexts: scmCloningMIB.setOrganization('Samsung Common Management Interface Working Group')
if mibBuilder.loadTexts: scmCloningMIB.setContactInfo(' SCMI Editors E-Mail: wani.kang@samsung.com -- -- ')
if mibBuilder.loadTexts: scmCloningMIB.setDescription(' Version: 1.00 Samsung SCMI Extension to IETF Printer MIB Module. This Module provides extension to the IETF Printer MIB. Copyright (C) 2003-2004 Samsung Corporation. All Rights Reserved.')
scmCloning = MibIdentifier((1, 3, 6, 1, 4, 1, 236, 11, 5, 11, 82, 1))
scmCloningTable = MibTable((1, 3, 6, 1, 4, 1, 236, 11, 5, 11, 82, 1, 1), )
if mibBuilder.loadTexts: scmCloningTable.setStatus('current')
if mibBuilder.loadTexts: scmCloningTable.setDescription(' ')
scmCloningEntry = MibTableRow((1, 3, 6, 1, 4, 1, 236, 11, 5, 11, 82, 1, 1, 1), ).setIndexNames((0, "SAMSUNG-CLONING-MIB", "scmCloningIndex"))
if mibBuilder.loadTexts: scmCloningEntry.setStatus('current')
if mibBuilder.loadTexts: scmCloningEntry.setDescription('A set of result for clonning on this device. If the device has no cloning result, this table is empty. ')
scmCloningIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 236, 11, 5, 11, 82, 1, 1, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: scmCloningIndex.setStatus('current')
if mibBuilder.loadTexts: scmCloningIndex.setDescription(' ')
scmCloningIPAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 236, 11, 5, 11, 82, 1, 1, 1, 2), IpAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: scmCloningIPAddress.setStatus('current')
if mibBuilder.loadTexts: scmCloningIPAddress.setDescription('This object indicates IPAdderss of device executing cloning ')
scmCloningResult = MibTableColumn((1, 3, 6, 1, 4, 1, 236, 11, 5, 11, 82, 1, 1, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6))).clone(namedValues=NamedValues(("completed", 1), ("processing", 2), ("invalidFile", 3), ("versionMismatch", 4), ("notSupportedCloning", 5), ("busy", 6)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: scmCloningResult.setStatus('current')
if mibBuilder.loadTexts: scmCloningResult.setDescription('This object indicates result of the cloning')
scmCloningDate = MibTableColumn((1, 3, 6, 1, 4, 1, 236, 11, 5, 11, 82, 1, 1, 1, 4), OctetString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: scmCloningDate.setStatus('current')
if mibBuilder.loadTexts: scmCloningDate.setDescription('This date represents when cloning is executed. Format of date is yyyy/mm/dd/hh/mm/ss')
scmCloningSimple = MibIdentifier((1, 3, 6, 1, 4, 1, 236, 11, 5, 11, 82, 1, 2))
scmCloningLastIPAddress = MibScalar((1, 3, 6, 1, 4, 1, 236, 11, 5, 11, 82, 1, 2, 1), IpAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: scmCloningLastIPAddress.setStatus('current')
if mibBuilder.loadTexts: scmCloningLastIPAddress.setDescription('This object indicates IPAdderss of device executing cloning lately')
scmCloningLastResult = MibScalar((1, 3, 6, 1, 4, 1, 236, 11, 5, 11, 82, 1, 2, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6))).clone(namedValues=NamedValues(("completed", 1), ("processing", 2), ("invalidFile", 3), ("versionMismatch", 4), ("notSupportedCloning", 5), ("busy", 6)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: scmCloningLastResult.setStatus('current')
if mibBuilder.loadTexts: scmCloningLastResult.setDescription('This object indicates result of the latest cloning')
scmCloningLastDate = MibScalar((1, 3, 6, 1, 4, 1, 236, 11, 5, 11, 82, 1, 2, 3), OctetString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: scmCloningLastDate.setStatus('current')
if mibBuilder.loadTexts: scmCloningLastDate.setDescription('This object indicates date of the latest cloning. Format of date is yyyy/mm/dd/hh/mm/ss')
scmCloningSupported = MibScalar((1, 3, 6, 1, 4, 1, 236, 11, 5, 11, 82, 1, 2, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("supported", 1), ("notSupported", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: scmCloningSupported.setStatus('current')
if mibBuilder.loadTexts: scmCloningSupported.setDescription('This object indicates whethere device supports cloning or not')
scmCloningTrap = ObjectIdentity((1, 3, 6, 1, 4, 1, 236, 11, 5, 11, 82, 1, 3))
if mibBuilder.loadTexts: scmCloningTrap.setStatus('current')
if mibBuilder.loadTexts: scmCloningTrap.setDescription('The value of the enterprise-specific oid in a SNMPv1 trap sent signalling a critical event in the JobAccounting')
scmCloningTrapSimple = MibIdentifier((1, 3, 6, 1, 4, 1, 236, 11, 5, 11, 82, 1, 3, 1))
scmCloningTrapResult = NotificationType((1, 3, 6, 1, 4, 1, 236, 11, 5, 11, 82, 1, 3, 1, 1)).setObjects(("SAMSUNG-CLONING-MIB", "scmCloningLastIPAddress"), ("SAMSUNG-CLONING-MIB", "scmCloningLastResult"))
if mibBuilder.loadTexts: scmCloningTrapResult.setStatus('current')
if mibBuilder.loadTexts: scmCloningTrapResult.setDescription('This trap is sent whenever clone is completed')
mibBuilder.exportSymbols("SAMSUNG-CLONING-MIB", scmCloningMIB=scmCloningMIB, scmCloningEntry=scmCloningEntry, scmCloningResult=scmCloningResult, scmCloningTrap=scmCloningTrap, scmCloning=scmCloning, scmCloningIndex=scmCloningIndex, scmCloningLastResult=scmCloningLastResult, scmCloningTrapResult=scmCloningTrapResult, scmCloningSimple=scmCloningSimple, scmCloningDate=scmCloningDate, scmCloningLastDate=scmCloningLastDate, scmCloningSupported=scmCloningSupported, scmCloningLastIPAddress=scmCloningLastIPAddress, scmCloningTable=scmCloningTable, scmCloningIPAddress=scmCloningIPAddress, PYSNMP_MODULE_ID=scmCloningMIB, scmCloningTrapSimple=scmCloningTrapSimple)
