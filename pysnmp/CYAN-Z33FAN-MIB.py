#
# PySNMP MIB module CYAN-Z33FAN-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/CYAN-Z33FAN-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 18:18:41 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
OctetString, ObjectIdentifier, Integer = mibBuilder.importSymbols("ASN1", "OctetString", "ObjectIdentifier", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, ConstraintsIntersection, ConstraintsUnion, SingleValueConstraint, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "ConstraintsIntersection", "ConstraintsUnion", "SingleValueConstraint", "ValueSizeConstraint")
CyanTypeTc, cyanEntityModules = mibBuilder.importSymbols("CYAN-MIB", "CyanTypeTc", "cyanEntityModules")
CyanLEDTc, CyanSecServiceStateTc, CyanOpStateTc, CyanAdminStateTc, CyanOpStateQualTc = mibBuilder.importSymbols("CYAN-TC-MIB", "CyanLEDTc", "CyanSecServiceStateTc", "CyanOpStateTc", "CyanAdminStateTc", "CyanOpStateQualTc")
NotificationGroup, ModuleCompliance, ObjectGroup = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance", "ObjectGroup")
IpAddress, Gauge32, Integer32, Unsigned32, ObjectIdentity, Bits, iso, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter32, NotificationType, ModuleIdentity, MibIdentifier, TimeTicks, Counter64 = mibBuilder.importSymbols("SNMPv2-SMI", "IpAddress", "Gauge32", "Integer32", "Unsigned32", "ObjectIdentity", "Bits", "iso", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter32", "NotificationType", "ModuleIdentity", "MibIdentifier", "TimeTicks", "Counter64")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
cyanZ33FanModule = ModuleIdentity((1, 3, 6, 1, 4, 1, 28533, 5, 30, 80))
cyanZ33FanModule.setRevisions(('2014-12-07 05:45',))
if mibBuilder.loadTexts: cyanZ33FanModule.setLastUpdated('201412070545Z')
if mibBuilder.loadTexts: cyanZ33FanModule.setOrganization('Cyan, Inc.')
cyanZ33FanMibObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 28533, 5, 30, 80, 1))
cyanZ33FanTable = MibTable((1, 3, 6, 1, 4, 1, 28533, 5, 30, 80, 1, 1), )
if mibBuilder.loadTexts: cyanZ33FanTable.setStatus('current')
cyanZ33FanEntry = MibTableRow((1, 3, 6, 1, 4, 1, 28533, 5, 30, 80, 1, 1, 1), ).setIndexNames((0, "CYAN-Z33FAN-MIB", "cyanZ33FanShelfId"), (0, "CYAN-Z33FAN-MIB", "cyanZ33FanZ33FanId"))
if mibBuilder.loadTexts: cyanZ33FanEntry.setStatus('current')
cyanZ33FanShelfId = MibTableColumn((1, 3, 6, 1, 4, 1, 28533, 5, 30, 80, 1, 1, 1, 1), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(0, 255)))
if mibBuilder.loadTexts: cyanZ33FanShelfId.setStatus('current')
cyanZ33FanZ33FanId = MibTableColumn((1, 3, 6, 1, 4, 1, 28533, 5, 30, 80, 1, 1, 1, 2), Unsigned32())
if mibBuilder.loadTexts: cyanZ33FanZ33FanId.setStatus('current')
cyanZ33FanAcoLed = MibTableColumn((1, 3, 6, 1, 4, 1, 28533, 5, 30, 80, 1, 1, 1, 3), CyanLEDTc()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cyanZ33FanAcoLed.setStatus('current')
cyanZ33FanAdminState = MibTableColumn((1, 3, 6, 1, 4, 1, 28533, 5, 30, 80, 1, 1, 1, 4), CyanAdminStateTc()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cyanZ33FanAdminState.setStatus('current')
cyanZ33FanAssetTag = MibTableColumn((1, 3, 6, 1, 4, 1, 28533, 5, 30, 80, 1, 1, 1, 5), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 124))).setMaxAccess("readonly")
if mibBuilder.loadTexts: cyanZ33FanAssetTag.setStatus('current')
cyanZ33FanAutoinserviceSoakTimeSec = MibTableColumn((1, 3, 6, 1, 4, 1, 28533, 5, 30, 80, 1, 1, 1, 6), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cyanZ33FanAutoinserviceSoakTimeSec.setStatus('current')
cyanZ33FanBaseMacAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 28533, 5, 30, 80, 1, 1, 1, 7), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cyanZ33FanBaseMacAddress.setStatus('current')
cyanZ33FanCriticalLed = MibTableColumn((1, 3, 6, 1, 4, 1, 28533, 5, 30, 80, 1, 1, 1, 8), CyanLEDTc()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cyanZ33FanCriticalLed.setStatus('current')
cyanZ33FanDescription = MibTableColumn((1, 3, 6, 1, 4, 1, 28533, 5, 30, 80, 1, 1, 1, 9), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 255))).setMaxAccess("readonly")
if mibBuilder.loadTexts: cyanZ33FanDescription.setStatus('current')
cyanZ33FanFanLed = MibTableColumn((1, 3, 6, 1, 4, 1, 28533, 5, 30, 80, 1, 1, 1, 10), CyanLEDTc()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cyanZ33FanFanLed.setStatus('current')
cyanZ33FanFilterLed = MibTableColumn((1, 3, 6, 1, 4, 1, 28533, 5, 30, 80, 1, 1, 1, 11), CyanLEDTc()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cyanZ33FanFilterLed.setStatus('current')
cyanZ33FanIdentifier = MibTableColumn((1, 3, 6, 1, 4, 1, 28533, 5, 30, 80, 1, 1, 1, 12), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cyanZ33FanIdentifier.setStatus('current')
cyanZ33FanMacBlockSize = MibTableColumn((1, 3, 6, 1, 4, 1, 28533, 5, 30, 80, 1, 1, 1, 13), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(0, 255))).setMaxAccess("readonly")
if mibBuilder.loadTexts: cyanZ33FanMacBlockSize.setStatus('current')
cyanZ33FanMajorLed = MibTableColumn((1, 3, 6, 1, 4, 1, 28533, 5, 30, 80, 1, 1, 1, 14), CyanLEDTc()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cyanZ33FanMajorLed.setStatus('current')
cyanZ33FanMfgCleiCode = MibTableColumn((1, 3, 6, 1, 4, 1, 28533, 5, 30, 80, 1, 1, 1, 15), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 10))).setMaxAccess("readonly")
if mibBuilder.loadTexts: cyanZ33FanMfgCleiCode.setStatus('current')
cyanZ33FanMfgEciCode = MibTableColumn((1, 3, 6, 1, 4, 1, 28533, 5, 30, 80, 1, 1, 1, 16), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 6))).setMaxAccess("readonly")
if mibBuilder.loadTexts: cyanZ33FanMfgEciCode.setStatus('current')
cyanZ33FanMfgModuleId = MibTableColumn((1, 3, 6, 1, 4, 1, 28533, 5, 30, 80, 1, 1, 1, 17), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cyanZ33FanMfgModuleId.setStatus('current')
cyanZ33FanMfgPartNumber = MibTableColumn((1, 3, 6, 1, 4, 1, 28533, 5, 30, 80, 1, 1, 1, 18), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 16))).setMaxAccess("readonly")
if mibBuilder.loadTexts: cyanZ33FanMfgPartNumber.setStatus('current')
cyanZ33FanMfgRevision = MibTableColumn((1, 3, 6, 1, 4, 1, 28533, 5, 30, 80, 1, 1, 1, 19), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 4))).setMaxAccess("readonly")
if mibBuilder.loadTexts: cyanZ33FanMfgRevision.setStatus('current')
cyanZ33FanMfgSerialNumber = MibTableColumn((1, 3, 6, 1, 4, 1, 28533, 5, 30, 80, 1, 1, 1, 20), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 16))).setMaxAccess("readonly")
if mibBuilder.loadTexts: cyanZ33FanMfgSerialNumber.setStatus('current')
cyanZ33FanMinorLed = MibTableColumn((1, 3, 6, 1, 4, 1, 28533, 5, 30, 80, 1, 1, 1, 21), CyanLEDTc()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cyanZ33FanMinorLed.setStatus('current')
cyanZ33FanName = MibTableColumn((1, 3, 6, 1, 4, 1, 28533, 5, 30, 80, 1, 1, 1, 22), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cyanZ33FanName.setStatus('current')
cyanZ33FanOidClass = MibTableColumn((1, 3, 6, 1, 4, 1, 28533, 5, 30, 80, 1, 1, 1, 23), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cyanZ33FanOidClass.setStatus('current')
cyanZ33FanOperState = MibTableColumn((1, 3, 6, 1, 4, 1, 28533, 5, 30, 80, 1, 1, 1, 24), CyanOpStateTc()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cyanZ33FanOperState.setStatus('current')
cyanZ33FanOperStateQual = MibTableColumn((1, 3, 6, 1, 4, 1, 28533, 5, 30, 80, 1, 1, 1, 25), CyanOpStateQualTc()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cyanZ33FanOperStateQual.setStatus('current')
cyanZ33FanOssLabel = MibTableColumn((1, 3, 6, 1, 4, 1, 28533, 5, 30, 80, 1, 1, 1, 26), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 80))).setMaxAccess("readonly")
if mibBuilder.loadTexts: cyanZ33FanOssLabel.setStatus('current')
cyanZ33FanOwner = MibTableColumn((1, 3, 6, 1, 4, 1, 28533, 5, 30, 80, 1, 1, 1, 27), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 80))).setMaxAccess("readonly")
if mibBuilder.loadTexts: cyanZ33FanOwner.setStatus('current')
cyanZ33FanPartNumber = MibTableColumn((1, 3, 6, 1, 4, 1, 28533, 5, 30, 80, 1, 1, 1, 28), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 11))).setMaxAccess("readonly")
if mibBuilder.loadTexts: cyanZ33FanPartNumber.setStatus('current')
cyanZ33FanSecServState = MibTableColumn((1, 3, 6, 1, 4, 1, 28533, 5, 30, 80, 1, 1, 1, 29), CyanSecServiceStateTc()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cyanZ33FanSecServState.setStatus('current')
cyanZ33FanType = MibTableColumn((1, 3, 6, 1, 4, 1, 28533, 5, 30, 80, 1, 1, 1, 30), CyanTypeTc()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cyanZ33FanType.setStatus('current')
cyanZ33FanObjectGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 28533, 5, 30, 80, 20)).setObjects(("CYAN-Z33FAN-MIB", "cyanZ33FanAcoLed"), ("CYAN-Z33FAN-MIB", "cyanZ33FanAdminState"), ("CYAN-Z33FAN-MIB", "cyanZ33FanAssetTag"), ("CYAN-Z33FAN-MIB", "cyanZ33FanAutoinserviceSoakTimeSec"), ("CYAN-Z33FAN-MIB", "cyanZ33FanBaseMacAddress"), ("CYAN-Z33FAN-MIB", "cyanZ33FanCriticalLed"), ("CYAN-Z33FAN-MIB", "cyanZ33FanDescription"), ("CYAN-Z33FAN-MIB", "cyanZ33FanFanLed"), ("CYAN-Z33FAN-MIB", "cyanZ33FanFilterLed"), ("CYAN-Z33FAN-MIB", "cyanZ33FanIdentifier"), ("CYAN-Z33FAN-MIB", "cyanZ33FanMacBlockSize"), ("CYAN-Z33FAN-MIB", "cyanZ33FanMajorLed"), ("CYAN-Z33FAN-MIB", "cyanZ33FanMfgCleiCode"), ("CYAN-Z33FAN-MIB", "cyanZ33FanMfgEciCode"), ("CYAN-Z33FAN-MIB", "cyanZ33FanMfgModuleId"), ("CYAN-Z33FAN-MIB", "cyanZ33FanMfgPartNumber"), ("CYAN-Z33FAN-MIB", "cyanZ33FanMfgRevision"), ("CYAN-Z33FAN-MIB", "cyanZ33FanMfgSerialNumber"), ("CYAN-Z33FAN-MIB", "cyanZ33FanMinorLed"), ("CYAN-Z33FAN-MIB", "cyanZ33FanName"), ("CYAN-Z33FAN-MIB", "cyanZ33FanOidClass"), ("CYAN-Z33FAN-MIB", "cyanZ33FanOperState"), ("CYAN-Z33FAN-MIB", "cyanZ33FanOperStateQual"), ("CYAN-Z33FAN-MIB", "cyanZ33FanOssLabel"), ("CYAN-Z33FAN-MIB", "cyanZ33FanOwner"), ("CYAN-Z33FAN-MIB", "cyanZ33FanPartNumber"), ("CYAN-Z33FAN-MIB", "cyanZ33FanSecServState"), ("CYAN-Z33FAN-MIB", "cyanZ33FanType"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cyanZ33FanObjectGroup = cyanZ33FanObjectGroup.setStatus('current')
cyanZ33FanCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 28533, 5, 30, 80, 30)).setObjects(("CYAN-Z33FAN-MIB", "cyanZ33FanObjectGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cyanZ33FanCompliance = cyanZ33FanCompliance.setStatus('current')
mibBuilder.exportSymbols("CYAN-Z33FAN-MIB", cyanZ33FanModule=cyanZ33FanModule, cyanZ33FanDescription=cyanZ33FanDescription, cyanZ33FanName=cyanZ33FanName, cyanZ33FanMfgPartNumber=cyanZ33FanMfgPartNumber, cyanZ33FanShelfId=cyanZ33FanShelfId, cyanZ33FanMibObjects=cyanZ33FanMibObjects, cyanZ33FanCompliance=cyanZ33FanCompliance, cyanZ33FanObjectGroup=cyanZ33FanObjectGroup, cyanZ33FanCriticalLed=cyanZ33FanCriticalLed, cyanZ33FanMfgModuleId=cyanZ33FanMfgModuleId, PYSNMP_MODULE_ID=cyanZ33FanModule, cyanZ33FanOperStateQual=cyanZ33FanOperStateQual, cyanZ33FanAutoinserviceSoakTimeSec=cyanZ33FanAutoinserviceSoakTimeSec, cyanZ33FanMajorLed=cyanZ33FanMajorLed, cyanZ33FanSecServState=cyanZ33FanSecServState, cyanZ33FanOidClass=cyanZ33FanOidClass, cyanZ33FanIdentifier=cyanZ33FanIdentifier, cyanZ33FanOperState=cyanZ33FanOperState, cyanZ33FanPartNumber=cyanZ33FanPartNumber, cyanZ33FanZ33FanId=cyanZ33FanZ33FanId, cyanZ33FanAdminState=cyanZ33FanAdminState, cyanZ33FanOssLabel=cyanZ33FanOssLabel, cyanZ33FanType=cyanZ33FanType, cyanZ33FanAcoLed=cyanZ33FanAcoLed, cyanZ33FanOwner=cyanZ33FanOwner, cyanZ33FanMfgCleiCode=cyanZ33FanMfgCleiCode, cyanZ33FanMacBlockSize=cyanZ33FanMacBlockSize, cyanZ33FanFilterLed=cyanZ33FanFilterLed, cyanZ33FanMfgEciCode=cyanZ33FanMfgEciCode, cyanZ33FanMfgSerialNumber=cyanZ33FanMfgSerialNumber, cyanZ33FanFanLed=cyanZ33FanFanLed, cyanZ33FanMfgRevision=cyanZ33FanMfgRevision, cyanZ33FanMinorLed=cyanZ33FanMinorLed, cyanZ33FanTable=cyanZ33FanTable, cyanZ33FanBaseMacAddress=cyanZ33FanBaseMacAddress, cyanZ33FanEntry=cyanZ33FanEntry, cyanZ33FanAssetTag=cyanZ33FanAssetTag)