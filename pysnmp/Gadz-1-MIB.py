#
# PySNMP MIB module Gadz-1-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/Gadz-1-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 19:07:35 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsUnion, SingleValueConstraint, ConstraintsIntersection, ValueRangeConstraint, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "SingleValueConstraint", "ConstraintsIntersection", "ValueRangeConstraint", "ValueSizeConstraint")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
ObjectIdentity, IpAddress, Bits, Counter64, Gauge32, MibIdentifier, NotificationType, enterprises, Counter32, iso, Integer32, NotificationType, Unsigned32, ModuleIdentity, TimeTicks, MibScalar, MibTable, MibTableRow, MibTableColumn = mibBuilder.importSymbols("SNMPv2-SMI", "ObjectIdentity", "IpAddress", "Bits", "Counter64", "Gauge32", "MibIdentifier", "NotificationType", "enterprises", "Counter32", "iso", "Integer32", "NotificationType", "Unsigned32", "ModuleIdentity", "TimeTicks", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
gadzoox = MibIdentifier((1, 3, 6, 1, 4, 1, 1754))
netMgmt = MibIdentifier((1, 3, 6, 1, 4, 1, 1754, 1))
common = MibIdentifier((1, 3, 6, 1, 4, 1, 1754, 1, 1))
system = MibIdentifier((1, 3, 6, 1, 4, 1, 1754, 1, 1, 1))
zoning = MibIdentifier((1, 3, 6, 1, 4, 1, 1754, 1, 1, 1, 3))
download = MibIdentifier((1, 3, 6, 1, 4, 1, 1754, 1, 1, 3))
security = MibIdentifier((1, 3, 6, 1, 4, 1, 1754, 1, 1, 4))
discovery = MibIdentifier((1, 3, 6, 1, 4, 1, 1754, 1, 1, 5))
monitor = MibIdentifier((1, 3, 6, 1, 4, 1, 1754, 1, 1, 6))
proxy = MibIdentifier((1, 3, 6, 1, 4, 1, 1754, 1, 1, 7))
policy = MibIdentifier((1, 3, 6, 1, 4, 1, 1754, 1, 1, 7, 11))
gbic = MibIdentifier((1, 3, 6, 1, 4, 1, 1754, 1, 1, 8))
hub = MibIdentifier((1, 3, 6, 1, 4, 1, 1754, 1, 2))
areaSwitch = MibIdentifier((1, 3, 6, 1, 4, 1, 1754, 1, 3))
channelAgent = MibIdentifier((1, 3, 6, 1, 4, 1, 1754, 1, 4))
traps = MibIdentifier((1, 3, 6, 1, 4, 1, 1754, 1, 5))
switch = MibIdentifier((1, 3, 6, 1, 4, 1, 1754, 1, 6))
capChas = MibIdentifier((1, 3, 6, 1, 4, 1, 1754, 1, 6, 1))
capPim = MibIdentifier((1, 3, 6, 1, 4, 1, 1754, 1, 6, 2))
sysReset = MibScalar((1, 3, 6, 1, 4, 1, 1754, 1, 1, 1, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("warm", 1), ("cold", 2)))).setMaxAccess("writeonly")
if mibBuilder.loadTexts: sysReset.setStatus('mandatory')
sysDiagnostic = MibScalar((1, 3, 6, 1, 4, 1, 1754, 1, 1, 1, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 65535))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: sysDiagnostic.setStatus('mandatory')
nlZoningPolicyControlOwner = MibScalar((1, 3, 6, 1, 4, 1, 1754, 1, 1, 1, 3, 1), IpAddress()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: nlZoningPolicyControlOwner.setStatus('mandatory')
nlZoningPolicyTimeout = MibScalar((1, 3, 6, 1, 4, 1, 1754, 1, 1, 1, 3, 2), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: nlZoningPolicyTimeout.setStatus('mandatory')
nlZoningPolicyStatus = MibScalar((1, 3, 6, 1, 4, 1, 1754, 1, 1, 1, 3, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3))).clone(namedValues=NamedValues(("no-current-owner", 0), ("request-valid", 1), ("request-invalid", 2), ("request-in-progress", 3)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: nlZoningPolicyStatus.setStatus('mandatory')
nlZoningPolicyControl = MibScalar((1, 3, 6, 1, 4, 1, 1754, 1, 1, 1, 3, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3))).clone(namedValues=NamedValues(("clear-owner", 0), ("create-table", 1), ("clear-zoning-configuration", 2), ("default-zoning-configuration", 3)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: nlZoningPolicyControl.setStatus('mandatory')
nlZoningPolicyLastError = MibScalar((1, 3, 6, 1, 4, 1, 1754, 1, 1, 1, 3, 5), OctetString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: nlZoningPolicyLastError.setStatus('mandatory')
nlPendingZoneCount = MibScalar((1, 3, 6, 1, 4, 1, 1754, 1, 1, 1, 3, 6), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: nlPendingZoneCount.setStatus('mandatory')
nlPendingZoneTable = MibTable((1, 3, 6, 1, 4, 1, 1754, 1, 1, 1, 3, 7), )
if mibBuilder.loadTexts: nlPendingZoneTable.setStatus('mandatory')
nlPendingZoneEntry = MibTableRow((1, 3, 6, 1, 4, 1, 1754, 1, 1, 1, 3, 7, 1), ).setIndexNames((0, "Gadz-1-MIB", "nlPendingZoneIndex"))
if mibBuilder.loadTexts: nlPendingZoneEntry.setStatus('mandatory')
nlPendingZoneIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 1754, 1, 1, 1, 3, 7, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: nlPendingZoneIndex.setStatus('mandatory')
nlPendingZoneName = MibTableColumn((1, 3, 6, 1, 4, 1, 1754, 1, 1, 1, 3, 7, 1, 2), OctetString()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: nlPendingZoneName.setStatus('mandatory')
nlPendingZoneType = MibTableColumn((1, 3, 6, 1, 4, 1, 1754, 1, 1, 1, 3, 7, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1))).clone(namedValues=NamedValues(("edgeDevice", 1)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: nlPendingZoneType.setStatus('mandatory')
nlPendingZoneMembers = MibTableColumn((1, 3, 6, 1, 4, 1, 1754, 1, 1, 1, 3, 7, 1, 4), OctetString()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: nlPendingZoneMembers.setStatus('mandatory')
nlPendingZoneLipToZonePolicy = MibTableColumn((1, 3, 6, 1, 4, 1, 1754, 1, 1, 1, 3, 7, 1, 5), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: nlPendingZoneLipToZonePolicy.setStatus('mandatory')
nlPendingZoneMemberCount = MibScalar((1, 3, 6, 1, 4, 1, 1754, 1, 1, 1, 3, 8), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: nlPendingZoneMemberCount.setStatus('mandatory')
nlPendingZoneMemberTable = MibTable((1, 3, 6, 1, 4, 1, 1754, 1, 1, 1, 3, 9), )
if mibBuilder.loadTexts: nlPendingZoneMemberTable.setStatus('mandatory')
nlPendingZoneMemberEntry = MibTableRow((1, 3, 6, 1, 4, 1, 1754, 1, 1, 1, 3, 9, 1), ).setIndexNames((0, "Gadz-1-MIB", "nlPendingZoneMemberIndex"))
if mibBuilder.loadTexts: nlPendingZoneMemberEntry.setStatus('mandatory')
nlPendingZoneMemberIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 1754, 1, 1, 1, 3, 9, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: nlPendingZoneMemberIndex.setStatus('mandatory')
nlPendingZoneMemberName = MibTableColumn((1, 3, 6, 1, 4, 1, 1754, 1, 1, 1, 3, 9, 1, 2), OctetString()).setMaxAccess("writeonly")
if mibBuilder.loadTexts: nlPendingZoneMemberName.setStatus('mandatory')
nlPendingZoneMemberType = MibTableColumn((1, 3, 6, 1, 4, 1, 1754, 1, 1, 1, 3, 9, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3))).clone(namedValues=NamedValues(("typeNotYetAssigned", 0), ("portZoneMember", 1), ("hardAssignedALPAZoneMember", 2), ("wwnZoneMember", 3)))).setMaxAccess("writeonly")
if mibBuilder.loadTexts: nlPendingZoneMemberType.setStatus('mandatory')
nlPendingZoneMemberID = MibTableColumn((1, 3, 6, 1, 4, 1, 1754, 1, 1, 1, 3, 9, 1, 4), OctetString()).setMaxAccess("writeonly")
if mibBuilder.loadTexts: nlPendingZoneMemberID.setStatus('mandatory')
nlActiveZoneCount = MibScalar((1, 3, 6, 1, 4, 1, 1754, 1, 1, 1, 3, 10), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: nlActiveZoneCount.setStatus('mandatory')
nlActiveZoneTable = MibTable((1, 3, 6, 1, 4, 1, 1754, 1, 1, 1, 3, 11), )
if mibBuilder.loadTexts: nlActiveZoneTable.setStatus('mandatory')
nlActiveZoneEntry = MibTableRow((1, 3, 6, 1, 4, 1, 1754, 1, 1, 1, 3, 11, 1), ).setIndexNames((0, "Gadz-1-MIB", "nlActiveZoneIndex"))
if mibBuilder.loadTexts: nlActiveZoneEntry.setStatus('mandatory')
nlActiveZoneIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 1754, 1, 1, 1, 3, 11, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: nlActiveZoneIndex.setStatus('mandatory')
nlActiveZoneName = MibTableColumn((1, 3, 6, 1, 4, 1, 1754, 1, 1, 1, 3, 11, 1, 2), OctetString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: nlActiveZoneName.setStatus('mandatory')
nlActiveZoneType = MibTableColumn((1, 3, 6, 1, 4, 1, 1754, 1, 1, 1, 3, 11, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1))).clone(namedValues=NamedValues(("edgeDevice", 1)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: nlActiveZoneType.setStatus('mandatory')
nlActiveZoneAddressSpace = MibTableColumn((1, 3, 6, 1, 4, 1, 1754, 1, 1, 1, 3, 11, 1, 4), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: nlActiveZoneAddressSpace.setStatus('mandatory')
nlActiveZoneMembers = MibTableColumn((1, 3, 6, 1, 4, 1, 1754, 1, 1, 1, 3, 11, 1, 5), OctetString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: nlActiveZoneMembers.setStatus('mandatory')
nlActiveZoneLipToZonePolicy = MibTableColumn((1, 3, 6, 1, 4, 1, 1754, 1, 1, 1, 3, 11, 1, 6), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: nlActiveZoneLipToZonePolicy.setStatus('mandatory')
nlActiveZoneMemberCount = MibScalar((1, 3, 6, 1, 4, 1, 1754, 1, 1, 1, 3, 12), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: nlActiveZoneMemberCount.setStatus('mandatory')
nlActiveZoneMemberTable = MibTable((1, 3, 6, 1, 4, 1, 1754, 1, 1, 1, 3, 13), )
if mibBuilder.loadTexts: nlActiveZoneMemberTable.setStatus('mandatory')
nlActiveZoneMemberEntry = MibTableRow((1, 3, 6, 1, 4, 1, 1754, 1, 1, 1, 3, 13, 1), ).setIndexNames((0, "Gadz-1-MIB", "nlActiveZoneMemberIndex"))
if mibBuilder.loadTexts: nlActiveZoneMemberEntry.setStatus('mandatory')
nlActiveZoneMemberIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 1754, 1, 1, 1, 3, 13, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: nlActiveZoneMemberIndex.setStatus('mandatory')
nlActiveZoneMemberName = MibTableColumn((1, 3, 6, 1, 4, 1, 1754, 1, 1, 1, 3, 13, 1, 2), OctetString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: nlActiveZoneMemberName.setStatus('mandatory')
nlActiveZoneMemberType = MibTableColumn((1, 3, 6, 1, 4, 1, 1754, 1, 1, 1, 3, 13, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("portZoneMember", 1), ("hardAssignedALPAZoneMember", 2), ("wwnZoneMember", 3)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: nlActiveZoneMemberType.setStatus('mandatory')
nlActiveZoneMemberID = MibTableColumn((1, 3, 6, 1, 4, 1, 1754, 1, 1, 1, 3, 13, 1, 4), OctetString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: nlActiveZoneMemberID.setStatus('mandatory')
downloadFile = MibScalar((1, 3, 6, 1, 4, 1, 1754, 1, 1, 3, 1), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 63))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: downloadFile.setStatus('mandatory')
downloadBootFile = MibScalar((1, 3, 6, 1, 4, 1, 1754, 1, 1, 3, 2), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 31))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: downloadBootFile.setStatus('mandatory')
downloadTFTPServer = MibScalar((1, 3, 6, 1, 4, 1, 1754, 1, 1, 3, 3), IpAddress()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: downloadTFTPServer.setStatus('mandatory')
downloadTargetID = MibScalar((1, 3, 6, 1, 4, 1, 1754, 1, 1, 3, 4), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: downloadTargetID.setStatus('mandatory')
downloadAction = MibScalar((1, 3, 6, 1, 4, 1, 1754, 1, 1, 3, 5), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("notDownloading", 1), ("downloadToPROM", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: downloadAction.setStatus('mandatory')
downloadStatus = MibScalar((1, 3, 6, 1, 4, 1, 1754, 1, 1, 3, 6), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 8, 9, 10))).clone(namedValues=NamedValues(("downloadSuccess", 1), ("downloadStatusUnknown", 2), ("downloadGeneralError", 3), ("downloadNoResponseFromServer", 4), ("downloadChecksumError", 5), ("downloadIncompatibleImage", 6), ("downloadTftpFileNotFound", 7), ("downloadTftpAccessViolation", 8), ("downloadAlreadyInProgress", 9), ("downloadCancelled", 10)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: downloadStatus.setStatus('mandatory')
downloadRetry = MibScalar((1, 3, 6, 1, 4, 1, 1754, 1, 1, 3, 7), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: downloadRetry.setStatus('mandatory')
downloadTimeOut = MibScalar((1, 3, 6, 1, 4, 1, 1754, 1, 1, 3, 8), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: downloadTimeOut.setStatus('mandatory')
downloadCfgFileFileName = MibScalar((1, 3, 6, 1, 4, 1, 1754, 1, 1, 3, 9), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 29))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: downloadCfgFileFileName.setStatus('mandatory')
downloadCfgFileServerIp = MibScalar((1, 3, 6, 1, 4, 1, 1754, 1, 1, 3, 10), IpAddress()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: downloadCfgFileServerIp.setStatus('mandatory')
downloadCfgFileAction = MibScalar((1, 3, 6, 1, 4, 1, 1754, 1, 1, 3, 11), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("noAction", 1), ("backupConfig", 2), ("restoreConfig", 3)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: downloadCfgFileAction.setStatus('mandatory')
downloadCfgFileBkupStatus = MibScalar((1, 3, 6, 1, 4, 1, 1754, 1, 1, 3, 12), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 8, 9, 10))).clone(namedValues=NamedValues(("backUpRestoreSuccess", 1), ("backUpRestoreStatusUnknown", 2), ("backUpRestoreIncomplete", 3), ("backUpRestoreGeneralError", 4), ("backUpRestoreNoFileNameSpecified", 5), ("backUpRestoreNoIpAddressSpecified", 6), ("backUpRestoreTftpDriverError", 7), ("backUpRestoreNoResponseFromServer", 8), ("backUpRestoreFileNotFound", 9), ("backUpRestoreCouldNotWriteFile", 10)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: downloadCfgFileBkupStatus.setStatus('mandatory')
proxyMaxMembers = MibScalar((1, 3, 6, 1, 4, 1, 1754, 1, 1, 7, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: proxyMaxMembers.setStatus('mandatory')
proxyCurMembers = MibScalar((1, 3, 6, 1, 4, 1, 1754, 1, 1, 7, 2), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: proxyCurMembers.setStatus('mandatory')
proxyChanges = MibScalar((1, 3, 6, 1, 4, 1, 1754, 1, 1, 7, 3), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: proxyChanges.setStatus('mandatory')
proxyBoardID = MibScalar((1, 3, 6, 1, 4, 1, 1754, 1, 1, 7, 4), OctetString().subtype(subtypeSpec=ValueSizeConstraint(0, 255))).setMaxAccess("readonly")
if mibBuilder.loadTexts: proxyBoardID.setStatus('mandatory')
proxyFirmwareVersion = MibScalar((1, 3, 6, 1, 4, 1, 1754, 1, 1, 7, 5), OctetString().subtype(subtypeSpec=ValueSizeConstraint(0, 15))).setMaxAccess("readonly")
if mibBuilder.loadTexts: proxyFirmwareVersion.setStatus('mandatory')
proxyTopologyCRC = MibScalar((1, 3, 6, 1, 4, 1, 1754, 1, 1, 7, 6), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 65535))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: proxyTopologyCRC.setStatus('mandatory')
proxyEventStatus = MibScalar((1, 3, 6, 1, 4, 1, 1754, 1, 1, 7, 7), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 255))).setMaxAccess("readonly")
if mibBuilder.loadTexts: proxyEventStatus.setStatus('mandatory')
proxyDeviceEventInd = MibScalar((1, 3, 6, 1, 4, 1, 1754, 1, 1, 7, 8), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 255))).setMaxAccess("readonly")
if mibBuilder.loadTexts: proxyDeviceEventInd.setStatus('mandatory')
proxyControl = MibScalar((1, 3, 6, 1, 4, 1, 1754, 1, 1, 7, 10), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 255))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: proxyControl.setStatus('mandatory')
deviceTable = MibTable((1, 3, 6, 1, 4, 1, 1754, 1, 1, 7, 9), )
if mibBuilder.loadTexts: deviceTable.setStatus('mandatory')
deviceEntry = MibTableRow((1, 3, 6, 1, 4, 1, 1754, 1, 1, 7, 9, 1), ).setIndexNames((0, "Gadz-1-MIB", "devDeviceID"))
if mibBuilder.loadTexts: deviceEntry.setStatus('mandatory')
devDeviceID = MibTableColumn((1, 3, 6, 1, 4, 1, 1754, 1, 1, 7, 9, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: devDeviceID.setStatus('mandatory')
devOID = MibTableColumn((1, 3, 6, 1, 4, 1, 1754, 1, 1, 7, 9, 1, 2), ObjectIdentifier()).setMaxAccess("readonly")
if mibBuilder.loadTexts: devOID.setStatus('mandatory')
devProductID = MibTableColumn((1, 3, 6, 1, 4, 1, 1754, 1, 1, 7, 9, 1, 3), OctetString().subtype(subtypeSpec=ValueSizeConstraint(0, 100))).setMaxAccess("readonly")
if mibBuilder.loadTexts: devProductID.setStatus('mandatory')
devBoardID = MibTableColumn((1, 3, 6, 1, 4, 1, 1754, 1, 1, 7, 9, 1, 4), OctetString().subtype(subtypeSpec=ValueSizeConstraint(0, 100))).setMaxAccess("readonly")
if mibBuilder.loadTexts: devBoardID.setStatus('mandatory')
devFirmwareVersion = MibTableColumn((1, 3, 6, 1, 4, 1, 1754, 1, 1, 7, 9, 1, 5), OctetString().subtype(subtypeSpec=ValueSizeConstraint(0, 20))).setMaxAccess("readonly")
if mibBuilder.loadTexts: devFirmwareVersion.setStatus('mandatory')
devEventStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 1754, 1, 1, 7, 9, 1, 6), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 255))).setMaxAccess("readonly")
if mibBuilder.loadTexts: devEventStatus.setStatus('mandatory')
devReset = MibTableColumn((1, 3, 6, 1, 4, 1, 1754, 1, 1, 7, 9, 1, 7), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("warm", 1), ("cold", 2)))).setMaxAccess("writeonly")
if mibBuilder.loadTexts: devReset.setStatus('mandatory')
devDiagnostic = MibTableColumn((1, 3, 6, 1, 4, 1, 1754, 1, 1, 7, 9, 1, 8), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 65535))).setMaxAccess("readonly")
if mibBuilder.loadTexts: devDiagnostic.setStatus('mandatory')
devSysUpTimestamp = MibTableColumn((1, 3, 6, 1, 4, 1, 1754, 1, 1, 7, 9, 1, 9), TimeTicks()).setMaxAccess("readonly")
if mibBuilder.loadTexts: devSysUpTimestamp.setStatus('mandatory')
devCumulativeUpTime = MibTableColumn((1, 3, 6, 1, 4, 1, 1754, 1, 1, 7, 9, 1, 10), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: devCumulativeUpTime.setStatus('mandatory')
devContact = MibTableColumn((1, 3, 6, 1, 4, 1, 1754, 1, 1, 7, 9, 1, 11), OctetString().subtype(subtypeSpec=ValueSizeConstraint(0, 63))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: devContact.setStatus('mandatory')
devLocation = MibTableColumn((1, 3, 6, 1, 4, 1, 1754, 1, 1, 7, 9, 1, 12), OctetString().subtype(subtypeSpec=ValueSizeConstraint(0, 63))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: devLocation.setStatus('mandatory')
devTopologyLink = MibTableColumn((1, 3, 6, 1, 4, 1, 1754, 1, 1, 7, 9, 1, 13), OctetString().subtype(subtypeSpec=ValueSizeConstraint(3, 3)).setFixedLength(3)).setMaxAccess("readonly")
if mibBuilder.loadTexts: devTopologyLink.setStatus('mandatory')
devBeaconOnTime = MibTableColumn((1, 3, 6, 1, 4, 1, 1754, 1, 1, 7, 9, 1, 14), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 25))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: devBeaconOnTime.setStatus('mandatory')
devBeaconOffTime = MibTableColumn((1, 3, 6, 1, 4, 1, 1754, 1, 1, 7, 9, 1, 15), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 25))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: devBeaconOffTime.setStatus('mandatory')
devFaultLedState = MibTableColumn((1, 3, 6, 1, 4, 1, 1754, 1, 1, 7, 9, 1, 16), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 1))).setMaxAccess("readonly")
if mibBuilder.loadTexts: devFaultLedState.setStatus('mandatory')
devNumPorts = MibTableColumn((1, 3, 6, 1, 4, 1, 1754, 1, 1, 7, 9, 1, 17), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 64))).setMaxAccess("readonly")
if mibBuilder.loadTexts: devNumPorts.setStatus('mandatory')
devType = MibTableColumn((1, 3, 6, 1, 4, 1, 1754, 1, 1, 7, 9, 1, 18), OctetString().subtype(subtypeSpec=ValueSizeConstraint(4, 4)).setFixedLength(4)).setMaxAccess("readonly")
if mibBuilder.loadTexts: devType.setStatus('mandatory')
devDescriptor = MibTableColumn((1, 3, 6, 1, 4, 1, 1754, 1, 1, 7, 9, 1, 19), OctetString().subtype(subtypeSpec=ValueSizeConstraint(0, 63))).setMaxAccess("readonly")
if mibBuilder.loadTexts: devDescriptor.setStatus('mandatory')
gbicTable = MibTable((1, 3, 6, 1, 4, 1, 1754, 1, 1, 8, 1), )
if mibBuilder.loadTexts: gbicTable.setStatus('mandatory')
gbicEntry = MibTableRow((1, 3, 6, 1, 4, 1, 1754, 1, 1, 8, 1, 1), ).setIndexNames((0, "Gadz-1-MIB", "gbicDeviceIndex"), (0, "Gadz-1-MIB", "gbicPortIndex"))
if mibBuilder.loadTexts: gbicEntry.setStatus('mandatory')
gbicDeviceIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 1754, 1, 1, 8, 1, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: gbicDeviceIndex.setStatus('mandatory')
gbicPortIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 1754, 1, 1, 8, 1, 1, 2), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: gbicPortIndex.setStatus('mandatory')
gbicEntryValid = MibTableColumn((1, 3, 6, 1, 4, 1, 1754, 1, 1, 8, 1, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1))).clone(namedValues=NamedValues(("invalid", 0), ("valid", 1)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: gbicEntryValid.setStatus('mandatory')
gbicInfo = MibTableColumn((1, 3, 6, 1, 4, 1, 1754, 1, 1, 8, 1, 1, 4), OctetString().subtype(subtypeSpec=ValueSizeConstraint(128, 128)).setFixedLength(128)).setMaxAccess("readonly")
if mibBuilder.loadTexts: gbicInfo.setStatus('mandatory')
capChasTable = MibTable((1, 3, 6, 1, 4, 1, 1754, 1, 6, 1, 1), )
if mibBuilder.loadTexts: capChasTable.setStatus('mandatory')
capChasEntry = MibTableRow((1, 3, 6, 1, 4, 1, 1754, 1, 6, 1, 1, 1), ).setIndexNames((0, "Gadz-1-MIB", "capChasDeviceID"))
if mibBuilder.loadTexts: capChasEntry.setStatus('mandatory')
capChasDeviceID = MibTableColumn((1, 3, 6, 1, 4, 1, 1754, 1, 6, 1, 1, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: capChasDeviceID.setStatus('mandatory')
capChasFeatureMask = MibTableColumn((1, 3, 6, 1, 4, 1, 1754, 1, 6, 1, 1, 1, 2), OctetString().subtype(subtypeSpec=ValueSizeConstraint(1, 1)).setFixedLength(1)).setMaxAccess("readonly")
if mibBuilder.loadTexts: capChasFeatureMask.setStatus('mandatory')
capChasEventStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 1754, 1, 6, 1, 1, 1, 3), OctetString().subtype(subtypeSpec=ValueSizeConstraint(2, 2)).setFixedLength(2)).setMaxAccess("readonly")
if mibBuilder.loadTexts: capChasEventStatus.setStatus('mandatory')
capChasLedStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 1754, 1, 6, 1, 1, 1, 4), OctetString().subtype(subtypeSpec=ValueSizeConstraint(2, 2)).setFixedLength(2)).setMaxAccess("readonly")
if mibBuilder.loadTexts: capChasLedStatus.setStatus('mandatory')
capChasModuleStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 1754, 1, 6, 1, 1, 1, 5), OctetString().subtype(subtypeSpec=ValueSizeConstraint(2, 2)).setFixedLength(2)).setMaxAccess("readonly")
if mibBuilder.loadTexts: capChasModuleStatus.setStatus('mandatory')
capChasWorldWideName = MibTableColumn((1, 3, 6, 1, 4, 1, 1754, 1, 6, 1, 1, 1, 6), OctetString().subtype(subtypeSpec=ValueSizeConstraint(0, 16))).setMaxAccess("readonly")
if mibBuilder.loadTexts: capChasWorldWideName.setStatus('mandatory')
capChasTemperature = MibTableColumn((1, 3, 6, 1, 4, 1, 1754, 1, 6, 1, 1, 1, 7), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: capChasTemperature.setStatus('mandatory')
capChasTempMaxAllowed = MibTableColumn((1, 3, 6, 1, 4, 1, 1754, 1, 6, 1, 1, 1, 8), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: capChasTempMaxAllowed.setStatus('mandatory')
capChasTempMaxThreshold = MibTableColumn((1, 3, 6, 1, 4, 1, 1754, 1, 6, 1, 1, 1, 9), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: capChasTempMaxThreshold.setStatus('mandatory')
capChasSANDoctor = MibTableColumn((1, 3, 6, 1, 4, 1, 1754, 1, 6, 1, 1, 1, 10), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: capChasSANDoctor.setStatus('mandatory')
capChasSlotTable = MibTable((1, 3, 6, 1, 4, 1, 1754, 1, 6, 1, 2), )
if mibBuilder.loadTexts: capChasSlotTable.setStatus('mandatory')
capChasSlotEntry = MibTableRow((1, 3, 6, 1, 4, 1, 1754, 1, 6, 1, 2, 1), ).setIndexNames((0, "Gadz-1-MIB", "capChasDevID"), (0, "Gadz-1-MIB", "capChasSlotNum"))
if mibBuilder.loadTexts: capChasSlotEntry.setStatus('mandatory')
capChasDevID = MibTableColumn((1, 3, 6, 1, 4, 1, 1754, 1, 6, 1, 2, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: capChasDevID.setStatus('mandatory')
capChasSlotNum = MibTableColumn((1, 3, 6, 1, 4, 1, 1754, 1, 6, 1, 2, 1, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 3))).setMaxAccess("readonly")
if mibBuilder.loadTexts: capChasSlotNum.setStatus('mandatory')
capChasPimDevID = MibTableColumn((1, 3, 6, 1, 4, 1, 1754, 1, 6, 1, 2, 1, 3), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: capChasPimDevID.setStatus('mandatory')
capSlotPimType = MibTableColumn((1, 3, 6, 1, 4, 1, 1754, 1, 6, 1, 2, 1, 4), OctetString().subtype(subtypeSpec=ValueSizeConstraint(4, 4)).setFixedLength(4)).setMaxAccess("readonly")
if mibBuilder.loadTexts: capSlotPimType.setStatus('mandatory')
capSlotPimStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 1754, 1, 6, 1, 2, 1, 5), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3))).clone(namedValues=NamedValues(("unknown", 0), ("empty", 1), ("present-and-active", 2), ("present-but-inactive", 3)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: capSlotPimStatus.setStatus('mandatory')
capSlotPimIPaddr = MibTableColumn((1, 3, 6, 1, 4, 1, 1754, 1, 6, 1, 2, 1, 6), IpAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: capSlotPimIPaddr.setStatus('mandatory')
capPimTable = MibTable((1, 3, 6, 1, 4, 1, 1754, 1, 6, 2, 1), )
if mibBuilder.loadTexts: capPimTable.setStatus('mandatory')
capPimEntry = MibTableRow((1, 3, 6, 1, 4, 1, 1754, 1, 6, 2, 1, 1), ).setIndexNames((0, "Gadz-1-MIB", "capPimDeviceID"))
if mibBuilder.loadTexts: capPimEntry.setStatus('mandatory')
capPimDeviceID = MibTableColumn((1, 3, 6, 1, 4, 1, 1754, 1, 6, 2, 1, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: capPimDeviceID.setStatus('mandatory')
capPimFeatureMask = MibTableColumn((1, 3, 6, 1, 4, 1, 1754, 1, 6, 2, 1, 1, 2), OctetString().subtype(subtypeSpec=ValueSizeConstraint(1, 1)).setFixedLength(1)).setMaxAccess("readonly")
if mibBuilder.loadTexts: capPimFeatureMask.setStatus('mandatory')
capPimEventStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 1754, 1, 6, 2, 1, 1, 3), OctetString().subtype(subtypeSpec=ValueSizeConstraint(2, 2)).setFixedLength(2)).setMaxAccess("readonly")
if mibBuilder.loadTexts: capPimEventStatus.setStatus('mandatory')
capPimLedStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 1754, 1, 6, 2, 1, 1, 4), OctetString().subtype(subtypeSpec=ValueSizeConstraint(3, 3)).setFixedLength(3)).setMaxAccess("readonly")
if mibBuilder.loadTexts: capPimLedStatus.setStatus('mandatory')
capPimPortAttributes = MibTableColumn((1, 3, 6, 1, 4, 1, 1754, 1, 6, 2, 1, 1, 5), OctetString().subtype(subtypeSpec=ValueSizeConstraint(16, 16)).setFixedLength(16)).setMaxAccess("readonly")
if mibBuilder.loadTexts: capPimPortAttributes.setStatus('mandatory')
capPimPortStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 1754, 1, 6, 2, 1, 1, 6), OctetString().subtype(subtypeSpec=ValueSizeConstraint(16, 16)).setFixedLength(16)).setMaxAccess("readonly")
if mibBuilder.loadTexts: capPimPortStatus.setStatus('mandatory')
capPortTable = MibTable((1, 3, 6, 1, 4, 1, 1754, 1, 6, 2, 2), )
if mibBuilder.loadTexts: capPortTable.setStatus('mandatory')
capPortEntry = MibTableRow((1, 3, 6, 1, 4, 1, 1754, 1, 6, 2, 2, 1), ).setIndexNames((0, "Gadz-1-MIB", "capPortDeviceID"), (0, "Gadz-1-MIB", "capPortIndex"))
if mibBuilder.loadTexts: capPortEntry.setStatus('mandatory')
capPortDeviceID = MibTableColumn((1, 3, 6, 1, 4, 1, 1754, 1, 6, 2, 2, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: capPortDeviceID.setStatus('mandatory')
capPortIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 1754, 1, 6, 2, 2, 1, 2), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: capPortIndex.setStatus('mandatory')
capPortType = MibTableColumn((1, 3, 6, 1, 4, 1, 1754, 1, 6, 2, 2, 1, 3), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: capPortType.setStatus('mandatory')
capPortForcedBypass = MibTableColumn((1, 3, 6, 1, 4, 1, 1754, 1, 6, 2, 2, 1, 4), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: capPortForcedBypass.setStatus('mandatory')
capPortLipType = MibTableColumn((1, 3, 6, 1, 4, 1, 1754, 1, 6, 2, 2, 1, 5), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: capPortLipType.setStatus('mandatory')
capPortAlpaCount = MibTableColumn((1, 3, 6, 1, 4, 1, 1754, 1, 6, 2, 2, 1, 6), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: capPortAlpaCount.setStatus('mandatory')
capPortAlpaBitmap = MibTableColumn((1, 3, 6, 1, 4, 1, 1754, 1, 6, 2, 2, 1, 7), OctetString().subtype(subtypeSpec=ValueSizeConstraint(16, 16)).setFixedLength(16)).setMaxAccess("readonly")
if mibBuilder.loadTexts: capPortAlpaBitmap.setStatus('mandatory')
capPortLipInitiatorCount = MibTableColumn((1, 3, 6, 1, 4, 1, 1754, 1, 6, 2, 2, 1, 8), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: capPortLipInitiatorCount.setStatus('mandatory')
trapIPaddrTable = MibTable((1, 3, 6, 1, 4, 1, 1754, 1, 5, 1), )
if mibBuilder.loadTexts: trapIPaddrTable.setStatus('mandatory')
trapIPentry = MibTableRow((1, 3, 6, 1, 4, 1, 1754, 1, 5, 1, 1), ).setIndexNames((0, "Gadz-1-MIB", "trapIndex"))
if mibBuilder.loadTexts: trapIPentry.setStatus('mandatory')
trapIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 1754, 1, 5, 1, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 255))).setMaxAccess("readonly")
if mibBuilder.loadTexts: trapIndex.setStatus('mandatory')
trapIPaddr = MibTableColumn((1, 3, 6, 1, 4, 1, 1754, 1, 5, 1, 1, 2), IpAddress()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: trapIPaddr.setStatus('mandatory')
trapDevID = MibScalar((1, 3, 6, 1, 4, 1, 1754, 1, 5, 2), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: trapDevID.setStatus('mandatory')
trapDevType = MibScalar((1, 3, 6, 1, 4, 1, 1754, 1, 5, 3), OctetString().subtype(subtypeSpec=ValueSizeConstraint(4, 4)).setFixedLength(4)).setMaxAccess("readonly")
if mibBuilder.loadTexts: trapDevType.setStatus('mandatory')
trapDevEventStatus = MibScalar((1, 3, 6, 1, 4, 1, 1754, 1, 5, 4), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 255))).setMaxAccess("readonly")
if mibBuilder.loadTexts: trapDevEventStatus.setStatus('mandatory')
trapDevEnvironmentStatus = MibScalar((1, 3, 6, 1, 4, 1, 1754, 1, 5, 5), OctetString().subtype(subtypeSpec=ValueSizeConstraint(4, 4)).setFixedLength(4)).setMaxAccess("readonly")
if mibBuilder.loadTexts: trapDevEnvironmentStatus.setStatus('mandatory')
trapDevPortStatus = MibScalar((1, 3, 6, 1, 4, 1, 1754, 1, 5, 6), OctetString().subtype(subtypeSpec=ValueSizeConstraint(36, 36)).setFixedLength(36)).setMaxAccess("readonly")
if mibBuilder.loadTexts: trapDevPortStatus.setStatus('mandatory')
trapDevPortAttributes = MibScalar((1, 3, 6, 1, 4, 1, 1754, 1, 5, 7), OctetString().subtype(subtypeSpec=ValueSizeConstraint(36, 36)).setFixedLength(36)).setMaxAccess("readonly")
if mibBuilder.loadTexts: trapDevPortAttributes.setStatus('mandatory')
trapDevConfigStatus = MibScalar((1, 3, 6, 1, 4, 1, 1754, 1, 5, 8), OctetString().subtype(subtypeSpec=ValueSizeConstraint(4, 4)).setFixedLength(4)).setMaxAccess("readonly")
if mibBuilder.loadTexts: trapDevConfigStatus.setStatus('mandatory')
trapDevLIPStatus = MibScalar((1, 3, 6, 1, 4, 1, 1754, 1, 5, 9), OctetString().subtype(subtypeSpec=ValueSizeConstraint(7, 7)).setFixedLength(7)).setMaxAccess("readonly")
if mibBuilder.loadTexts: trapDevLIPStatus.setStatus('mandatory')
trapMaxNumberTrapTargets = MibScalar((1, 3, 6, 1, 4, 1, 1754, 1, 5, 10), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: trapMaxNumberTrapTargets.setStatus('mandatory')
trapLIPStatus = NotificationType((1, 3, 6, 1, 4, 1, 1754, 1, 6, 1) + (0,1)).setObjects(("Gadz-1-MIB", "trapDevID"), ("Gadz-1-MIB", "trapDevType"), ("Gadz-1-MIB", "trapDevLIPStatus"))
trapMgmtTopologyChange = NotificationType((1, 3, 6, 1, 4, 1, 1754, 1, 6, 1) + (0,2)).setObjects(("Gadz-1-MIB", "trapDevID"), ("Gadz-1-MIB", "trapDevType"))
trapEnvironment = NotificationType((1, 3, 6, 1, 4, 1, 1754, 1, 6, 1) + (0,3)).setObjects(("Gadz-1-MIB", "trapDevID"), ("Gadz-1-MIB", "trapDevType"), ("Gadz-1-MIB", "trapDevEnvironmentStatus"))
trapPortStatus = NotificationType((1, 3, 6, 1, 4, 1, 1754, 1, 6, 1) + (0,4)).setObjects(("Gadz-1-MIB", "trapDevID"), ("Gadz-1-MIB", "trapDevType"), ("Gadz-1-MIB", "trapDevPortStatus"), ("Gadz-1-MIB", "trapDevPortAttributes"))
trapConfigurationStatus = NotificationType((1, 3, 6, 1, 4, 1, 1754, 1, 6, 1) + (0,5)).setObjects(("Gadz-1-MIB", "trapDevID"), ("Gadz-1-MIB", "trapDevType"), ("Gadz-1-MIB", "trapDevConfigStatus"))
mibBuilder.exportSymbols("Gadz-1-MIB", system=system, proxyCurMembers=proxyCurMembers, gbicDeviceIndex=gbicDeviceIndex, capChasTemperature=capChasTemperature, nlPendingZoneLipToZonePolicy=nlPendingZoneLipToZonePolicy, nlPendingZoneMemberIndex=nlPendingZoneMemberIndex, nlActiveZoneTable=nlActiveZoneTable, trapIndex=trapIndex, proxyFirmwareVersion=proxyFirmwareVersion, capPimPortAttributes=capPimPortAttributes, nlPendingZoneMemberType=nlPendingZoneMemberType, capPortEntry=capPortEntry, nlPendingZoneIndex=nlPendingZoneIndex, devTopologyLink=devTopologyLink, trapPortStatus=trapPortStatus, nlZoningPolicyControlOwner=nlZoningPolicyControlOwner, trapEnvironment=trapEnvironment, nlPendingZoneTable=nlPendingZoneTable, devDescriptor=devDescriptor, downloadFile=downloadFile, trapDevEnvironmentStatus=trapDevEnvironmentStatus, nlPendingZoneName=nlPendingZoneName, capPortTable=capPortTable, nlPendingZoneMemberTable=nlPendingZoneMemberTable, nlPendingZoneMemberName=nlPendingZoneMemberName, nlPendingZoneMemberID=nlPendingZoneMemberID, downloadBootFile=downloadBootFile, capSlotPimType=capSlotPimType, trapConfigurationStatus=trapConfigurationStatus, proxyMaxMembers=proxyMaxMembers, channelAgent=channelAgent, devDiagnostic=devDiagnostic, trapDevID=trapDevID, capPortForcedBypass=capPortForcedBypass, devBeaconOnTime=devBeaconOnTime, trapDevLIPStatus=trapDevLIPStatus, proxy=proxy, trapMgmtTopologyChange=trapMgmtTopologyChange, capChasModuleStatus=capChasModuleStatus, devProductID=devProductID, capSlotPimStatus=capSlotPimStatus, nlActiveZoneMemberType=nlActiveZoneMemberType, capPimPortStatus=capPimPortStatus, hub=hub, capPortLipInitiatorCount=capPortLipInitiatorCount, devBoardID=devBoardID, trapDevEventStatus=trapDevEventStatus, capChasFeatureMask=capChasFeatureMask, devNumPorts=devNumPorts, proxyEventStatus=proxyEventStatus, proxyTopologyCRC=proxyTopologyCRC, capPimDeviceID=capPimDeviceID, trapDevPortStatus=trapDevPortStatus, proxyControl=proxyControl, gbic=gbic, devCumulativeUpTime=devCumulativeUpTime, capChasTable=capChasTable, gadzoox=gadzoox, nlPendingZoneType=nlPendingZoneType, nlPendingZoneMemberEntry=nlPendingZoneMemberEntry, devReset=devReset, capChas=capChas, capChasSlotNum=capChasSlotNum, sysDiagnostic=sysDiagnostic, switch=switch, downloadCfgFileServerIp=downloadCfgFileServerIp, nlActiveZoneMemberTable=nlActiveZoneMemberTable, common=common, capChasTempMaxThreshold=capChasTempMaxThreshold, gbicTable=gbicTable, capPimLedStatus=capPimLedStatus, nlActiveZoneMemberID=nlActiveZoneMemberID, nlPendingZoneCount=nlPendingZoneCount, downloadTFTPServer=downloadTFTPServer, nlActiveZoneMemberName=nlActiveZoneMemberName, capChasTempMaxAllowed=capChasTempMaxAllowed, capPimTable=capPimTable, security=security, zoning=zoning, gbicEntry=gbicEntry, monitor=monitor, capPortAlpaCount=capPortAlpaCount, proxyBoardID=proxyBoardID, devLocation=devLocation, trapIPaddr=trapIPaddr, trapDevConfigStatus=trapDevConfigStatus, capChasLedStatus=capChasLedStatus, nlActiveZoneCount=nlActiveZoneCount, devDeviceID=devDeviceID, nlActiveZoneMemberEntry=nlActiveZoneMemberEntry, devOID=devOID, devFirmwareVersion=devFirmwareVersion, capChasSlotTable=capChasSlotTable, capChasEntry=capChasEntry, capSlotPimIPaddr=capSlotPimIPaddr, nlZoningPolicyTimeout=nlZoningPolicyTimeout, capPim=capPim, nlZoningPolicyLastError=nlZoningPolicyLastError, capChasSANDoctor=capChasSANDoctor, nlZoningPolicyControl=nlZoningPolicyControl, capPimEventStatus=capPimEventStatus, downloadTimeOut=downloadTimeOut, trapIPentry=trapIPentry, downloadTargetID=downloadTargetID, capPortDeviceID=capPortDeviceID, proxyChanges=proxyChanges, gbicInfo=gbicInfo, capChasPimDevID=capChasPimDevID, capPortIndex=capPortIndex, nlPendingZoneMemberCount=nlPendingZoneMemberCount, deviceTable=deviceTable, gbicPortIndex=gbicPortIndex, download=download, discovery=discovery, devBeaconOffTime=devBeaconOffTime, nlActiveZoneIndex=nlActiveZoneIndex, trapLIPStatus=trapLIPStatus, capPortAlpaBitmap=capPortAlpaBitmap, policy=policy, proxyDeviceEventInd=proxyDeviceEventInd, downloadCfgFileFileName=downloadCfgFileFileName, downloadRetry=downloadRetry, devSysUpTimestamp=devSysUpTimestamp, downloadAction=downloadAction, capChasSlotEntry=capChasSlotEntry, capPimFeatureMask=capPimFeatureMask, sysReset=sysReset, nlPendingZoneEntry=nlPendingZoneEntry, nlActiveZoneMemberIndex=nlActiveZoneMemberIndex, nlActiveZoneLipToZonePolicy=nlActiveZoneLipToZonePolicy, devFaultLedState=devFaultLedState, netMgmt=netMgmt, trapDevType=trapDevType, trapIPaddrTable=trapIPaddrTable, nlActiveZoneName=nlActiveZoneName, traps=traps, nlActiveZoneType=nlActiveZoneType, nlPendingZoneMembers=nlPendingZoneMembers, nlActiveZoneEntry=nlActiveZoneEntry, devContact=devContact, capChasDevID=capChasDevID, nlActiveZoneMemberCount=nlActiveZoneMemberCount, gbicEntryValid=gbicEntryValid, nlZoningPolicyStatus=nlZoningPolicyStatus, capChasDeviceID=capChasDeviceID, downloadStatus=downloadStatus, capChasWorldWideName=capChasWorldWideName, nlActiveZoneMembers=nlActiveZoneMembers, trapDevPortAttributes=trapDevPortAttributes, capPortLipType=capPortLipType, devEventStatus=devEventStatus, devType=devType, capChasEventStatus=capChasEventStatus, trapMaxNumberTrapTargets=trapMaxNumberTrapTargets, areaSwitch=areaSwitch, capPortType=capPortType, deviceEntry=deviceEntry, capPimEntry=capPimEntry, nlActiveZoneAddressSpace=nlActiveZoneAddressSpace, downloadCfgFileBkupStatus=downloadCfgFileBkupStatus, downloadCfgFileAction=downloadCfgFileAction)
