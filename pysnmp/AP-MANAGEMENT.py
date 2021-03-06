#
# PySNMP MIB module AP-MANAGEMENT (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/AP-MANAGEMENT
# Produced by pysmi-0.3.4 at Mon Apr 29 17:07:04 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
OctetString, ObjectIdentifier, Integer = mibBuilder.importSymbols("ASN1", "OctetString", "ObjectIdentifier", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ConstraintsUnion, SingleValueConstraint, ValueRangeConstraint, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ConstraintsUnion", "SingleValueConstraint", "ValueRangeConstraint", "ValueSizeConstraint")
ModuleCompliance, ObjectGroup, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "ObjectGroup", "NotificationGroup")
MibScalar, MibTable, MibTableRow, MibTableColumn, ModuleIdentity, iso, Integer32, Counter32, ObjectIdentity, NotificationType, Bits, Unsigned32, TimeTicks, MibIdentifier, enterprises, Gauge32, Counter64, IpAddress = mibBuilder.importSymbols("SNMPv2-SMI", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "ModuleIdentity", "iso", "Integer32", "Counter32", "ObjectIdentity", "NotificationType", "Bits", "Unsigned32", "TimeTicks", "MibIdentifier", "enterprises", "Gauge32", "Counter64", "IpAddress")
RowStatus, TextualConvention, TruthValue, DisplayString, MacAddress = mibBuilder.importSymbols("SNMPv2-TC", "RowStatus", "TextualConvention", "TruthValue", "DisplayString", "MacAddress")
pepwave = MibIdentifier((1, 3, 6, 1, 4, 1, 27662))
productID = MibIdentifier((1, 3, 6, 1, 4, 1, 27662, 200))
apMib = MibIdentifier((1, 3, 6, 1, 4, 1, 27662, 200, 1))
apGeneralMib = MibIdentifier((1, 3, 6, 1, 4, 1, 27662, 200, 1, 1))
ap_management_mib = ModuleIdentity((1, 3, 6, 1, 4, 1, 27662, 200, 1, 1, 7)).setLabel("ap-management-mib")
if mibBuilder.loadTexts: ap_management_mib.setLastUpdated('2011102000Z')
if mibBuilder.loadTexts: ap_management_mib.setOrganization('PEPWAVE')
apWeb = MibIdentifier((1, 3, 6, 1, 4, 1, 27662, 200, 1, 1, 7, 1))
apWebAdmin = MibIdentifier((1, 3, 6, 1, 4, 1, 27662, 200, 1, 1, 7, 1, 1))
apWebAccessProtocol = MibScalar((1, 3, 6, 1, 4, 1, 27662, 200, 1, 1, 7, 1, 1, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1))).clone(namedValues=NamedValues(("http", 0), ("https", 1)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: apWebAccessProtocol.setStatus('current')
apWebManagementPort = MibScalar((1, 3, 6, 1, 4, 1, 27662, 200, 1, 1, 7, 1, 1, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 65535))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: apWebManagementPort.setStatus('current')
apWebHttpRedirection = MibScalar((1, 3, 6, 1, 4, 1, 27662, 200, 1, 1, 7, 1, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1))).clone(namedValues=NamedValues(("disable", 0), ("enable", 1)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: apWebHttpRedirection.setStatus('current')
apWebUsername = MibScalar((1, 3, 6, 1, 4, 1, 27662, 200, 1, 1, 7, 1, 1, 4), OctetString().subtype(subtypeSpec=ValueSizeConstraint(0, 32))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: apWebUsername.setStatus('current')
apWebPassword = MibScalar((1, 3, 6, 1, 4, 1, 27662, 200, 1, 1, 7, 1, 1, 5), OctetString().subtype(subtypeSpec=ValueSizeConstraint(0, 32))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: apWebPassword.setStatus('current')
apWebAdministration = MibScalar((1, 3, 6, 1, 4, 1, 27662, 200, 1, 1, 7, 1, 1, 6), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1))).clone(namedValues=NamedValues(("disable", 0), ("enable", 1)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: apWebAdministration.setStatus('current')
apSnmp = MibIdentifier((1, 3, 6, 1, 4, 1, 27662, 200, 1, 1, 7, 2))
apSnmpBasic = MibIdentifier((1, 3, 6, 1, 4, 1, 27662, 200, 1, 1, 7, 2, 1))
apSnmpName = MibScalar((1, 3, 6, 1, 4, 1, 27662, 200, 1, 1, 7, 2, 1, 1), OctetString().subtype(subtypeSpec=ValueSizeConstraint(1, 32))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: apSnmpName.setStatus('current')
apSnmpV1Enable = MibScalar((1, 3, 6, 1, 4, 1, 27662, 200, 1, 1, 7, 2, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1))).clone(namedValues=NamedValues(("disable", 0), ("enable", 1)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: apSnmpV1Enable.setStatus('current')
apSnmpV2Enable = MibScalar((1, 3, 6, 1, 4, 1, 27662, 200, 1, 1, 7, 2, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1))).clone(namedValues=NamedValues(("disable", 0), ("enable", 1)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: apSnmpV2Enable.setStatus('current')
apSnmpV3Enable = MibScalar((1, 3, 6, 1, 4, 1, 27662, 200, 1, 1, 7, 2, 1, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1))).clone(namedValues=NamedValues(("disable", 0), ("enable", 1)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: apSnmpV3Enable.setStatus('current')
apSnmpTrap = MibIdentifier((1, 3, 6, 1, 4, 1, 27662, 200, 1, 1, 7, 2, 2))
apSnmpTrapEnable = MibScalar((1, 3, 6, 1, 4, 1, 27662, 200, 1, 1, 7, 2, 2, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1))).clone(namedValues=NamedValues(("disable", 0), ("enable", 1)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: apSnmpTrapEnable.setStatus('current')
apSnmpTrapName = MibScalar((1, 3, 6, 1, 4, 1, 27662, 200, 1, 1, 7, 2, 2, 2), OctetString().subtype(subtypeSpec=ValueSizeConstraint(1, 16))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: apSnmpTrapName.setStatus('current')
apSnmpTrapIpAddress = MibScalar((1, 3, 6, 1, 4, 1, 27662, 200, 1, 1, 7, 2, 2, 3), IpAddress()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: apSnmpTrapIpAddress.setStatus('current')
apSnmpCommunityTable = MibTable((1, 3, 6, 1, 4, 1, 27662, 200, 1, 1, 7, 2, 3), )
if mibBuilder.loadTexts: apSnmpCommunityTable.setStatus('current')
apSnmpCommunityEntry = MibTableRow((1, 3, 6, 1, 4, 1, 27662, 200, 1, 1, 7, 2, 3, 1), ).setIndexNames((0, "AP-MANAGEMENT", "apSnmpCommunityIndex"))
if mibBuilder.loadTexts: apSnmpCommunityEntry.setStatus('current')
apSnmpCommunityIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 27662, 200, 1, 1, 7, 2, 3, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: apSnmpCommunityIndex.setStatus('current')
apSnmpCommunityRowControl = MibTableColumn((1, 3, 6, 1, 4, 1, 27662, 200, 1, 1, 7, 2, 3, 1, 2), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: apSnmpCommunityRowControl.setStatus('current')
apSnmpCommunityStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 27662, 200, 1, 1, 7, 2, 3, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1))).clone(namedValues=NamedValues(("disable", 0), ("enable", 1)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: apSnmpCommunityStatus.setStatus('current')
apSnmpCommunityName = MibTableColumn((1, 3, 6, 1, 4, 1, 27662, 200, 1, 1, 7, 2, 3, 1, 4), OctetString().subtype(subtypeSpec=ValueSizeConstraint(1, 16))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: apSnmpCommunityName.setStatus('current')
apSnmpCommunityIpAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 27662, 200, 1, 1, 7, 2, 3, 1, 5), IpAddress()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: apSnmpCommunityIpAddress.setStatus('current')
apSnmpCommunityNetmask = MibTableColumn((1, 3, 6, 1, 4, 1, 27662, 200, 1, 1, 7, 2, 3, 1, 6), IpAddress()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: apSnmpCommunityNetmask.setStatus('current')
apSnmpCommunityAccess = MibTableColumn((1, 3, 6, 1, 4, 1, 27662, 200, 1, 1, 7, 2, 3, 1, 7), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1))).clone(namedValues=NamedValues(("readonly", 0), ("readwrite", 1)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: apSnmpCommunityAccess.setStatus('current')
apSnmpUserTable = MibTable((1, 3, 6, 1, 4, 1, 27662, 200, 1, 1, 7, 2, 4), )
if mibBuilder.loadTexts: apSnmpUserTable.setStatus('current')
apSnmpUserEntry = MibTableRow((1, 3, 6, 1, 4, 1, 27662, 200, 1, 1, 7, 2, 4, 1), ).setIndexNames((0, "AP-MANAGEMENT", "apSnmpUserIndex"))
if mibBuilder.loadTexts: apSnmpUserEntry.setStatus('current')
apSnmpUserIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 27662, 200, 1, 1, 7, 2, 4, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: apSnmpUserIndex.setStatus('current')
apSnmpUserRowControl = MibTableColumn((1, 3, 6, 1, 4, 1, 27662, 200, 1, 1, 7, 2, 4, 1, 2), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: apSnmpUserRowControl.setStatus('current')
apSnmpUserStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 27662, 200, 1, 1, 7, 2, 4, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1))).clone(namedValues=NamedValues(("disable", 0), ("enable", 1)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: apSnmpUserStatus.setStatus('current')
apSnmpUserName = MibTableColumn((1, 3, 6, 1, 4, 1, 27662, 200, 1, 1, 7, 2, 4, 1, 4), OctetString().subtype(subtypeSpec=ValueSizeConstraint(1, 16))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: apSnmpUserName.setStatus('current')
apSnmpUserAuthProtocol = MibTableColumn((1, 3, 6, 1, 4, 1, 27662, 200, 1, 1, 7, 2, 4, 1, 5), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1))).clone(namedValues=NamedValues(("md5", 0), ("sha", 1)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: apSnmpUserAuthProtocol.setStatus('current')
apSnmpUserAuthPassword = MibTableColumn((1, 3, 6, 1, 4, 1, 27662, 200, 1, 1, 7, 2, 4, 1, 6), OctetString().subtype(subtypeSpec=ValueSizeConstraint(0, 32))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: apSnmpUserAuthPassword.setStatus('current')
apSnmpUserPrivProtocol = MibTableColumn((1, 3, 6, 1, 4, 1, 27662, 200, 1, 1, 7, 2, 4, 1, 7), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1))).clone(namedValues=NamedValues(("none", 0), ("des", 1)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: apSnmpUserPrivProtocol.setStatus('current')
apSnmpUserPrivPassword = MibTableColumn((1, 3, 6, 1, 4, 1, 27662, 200, 1, 1, 7, 2, 4, 1, 8), OctetString().subtype(subtypeSpec=ValueSizeConstraint(0, 32))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: apSnmpUserPrivPassword.setStatus('current')
apSnmpUserAccess = MibTableColumn((1, 3, 6, 1, 4, 1, 27662, 200, 1, 1, 7, 2, 4, 1, 9), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1))).clone(namedValues=NamedValues(("readonly", 0), ("readwrite", 1)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: apSnmpUserAccess.setStatus('current')
apRemoteAssistance = MibIdentifier((1, 3, 6, 1, 4, 1, 27662, 200, 1, 1, 7, 3))
apRemoteAssistanceBasic = MibIdentifier((1, 3, 6, 1, 4, 1, 27662, 200, 1, 1, 7, 3, 1))
apRemoteAssistanceCurrentStatus = MibScalar((1, 3, 6, 1, 4, 1, 27662, 200, 1, 1, 7, 3, 1, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1, 2))).clone(namedValues=NamedValues(("disable", 0), ("connecting", 1), ("connected", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: apRemoteAssistanceCurrentStatus.setStatus('current')
apRemoteAssistanceStatus = MibScalar((1, 3, 6, 1, 4, 1, 27662, 200, 1, 1, 7, 3, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1))).clone(namedValues=NamedValues(("disable", 0), ("enable", 1)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: apRemoteAssistanceStatus.setStatus('current')
apControl = MibIdentifier((1, 3, 6, 1, 4, 1, 27662, 200, 1, 1, 7, 4))
apCommands = MibIdentifier((1, 3, 6, 1, 4, 1, 27662, 200, 1, 1, 7, 4, 1))
apSaveAndActivate = MibScalar((1, 3, 6, 1, 4, 1, 27662, 200, 1, 1, 7, 4, 1, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1))).clone(namedValues=NamedValues(("disable", 0), ("enable", 1)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: apSaveAndActivate.setStatus('current')
apReboot = MibScalar((1, 3, 6, 1, 4, 1, 27662, 200, 1, 1, 7, 4, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3))).clone(namedValues=NamedValues(("disable", 0), ("rebootFlash1", 1), ("rebootFlash2", 2), ("rebootCurrentFlash", 3)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: apReboot.setStatus('current')
apRestoreDefault = MibScalar((1, 3, 6, 1, 4, 1, 27662, 200, 1, 1, 7, 4, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1, 2))).clone(namedValues=NamedValues(("disable", 0), ("restoreDefault", 1), ("restorePreserveNetwork", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: apRestoreDefault.setStatus('current')
mibBuilder.exportSymbols("AP-MANAGEMENT", apSnmpUserPrivPassword=apSnmpUserPrivPassword, apReboot=apReboot, apSnmpTrapEnable=apSnmpTrapEnable, apSnmp=apSnmp, apCommands=apCommands, apMib=apMib, apSnmpName=apSnmpName, apSnmpCommunityName=apSnmpCommunityName, apSnmpTrapIpAddress=apSnmpTrapIpAddress, apWebPassword=apWebPassword, apSnmpV3Enable=apSnmpV3Enable, apRestoreDefault=apRestoreDefault, apSnmpV2Enable=apSnmpV2Enable, productID=productID, apGeneralMib=apGeneralMib, apWebHttpRedirection=apWebHttpRedirection, apWebAdmin=apWebAdmin, apWebAdministration=apWebAdministration, apSnmpUserRowControl=apSnmpUserRowControl, apSnmpBasic=apSnmpBasic, apSnmpUserAccess=apSnmpUserAccess, apSnmpCommunityEntry=apSnmpCommunityEntry, apSnmpCommunityAccess=apSnmpCommunityAccess, apSnmpUserAuthPassword=apSnmpUserAuthPassword, apWebManagementPort=apWebManagementPort, apSnmpUserEntry=apSnmpUserEntry, pepwave=pepwave, apSnmpCommunityNetmask=apSnmpCommunityNetmask, apWebUsername=apWebUsername, apSnmpTrapName=apSnmpTrapName, apSnmpCommunityRowControl=apSnmpCommunityRowControl, apRemoteAssistanceCurrentStatus=apRemoteAssistanceCurrentStatus, apRemoteAssistanceStatus=apRemoteAssistanceStatus, apControl=apControl, apSnmpUserAuthProtocol=apSnmpUserAuthProtocol, ap_management_mib=ap_management_mib, apSnmpCommunityStatus=apSnmpCommunityStatus, apSnmpCommunityIndex=apSnmpCommunityIndex, PYSNMP_MODULE_ID=ap_management_mib, apSaveAndActivate=apSaveAndActivate, apSnmpUserTable=apSnmpUserTable, apSnmpV1Enable=apSnmpV1Enable, apWebAccessProtocol=apWebAccessProtocol, apWeb=apWeb, apSnmpUserStatus=apSnmpUserStatus, apRemoteAssistanceBasic=apRemoteAssistanceBasic, apSnmpUserName=apSnmpUserName, apSnmpUserIndex=apSnmpUserIndex, apSnmpUserPrivProtocol=apSnmpUserPrivProtocol, apSnmpTrap=apSnmpTrap, apSnmpCommunityTable=apSnmpCommunityTable, apRemoteAssistance=apRemoteAssistance, apSnmpCommunityIpAddress=apSnmpCommunityIpAddress)
