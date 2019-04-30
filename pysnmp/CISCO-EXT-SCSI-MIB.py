#
# PySNMP MIB module CISCO-EXT-SCSI-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/CISCO-EXT-SCSI-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 17:40:29 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
SingleValueConstraint, ConstraintsUnion, ValueRangeConstraint, ConstraintsIntersection, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "SingleValueConstraint", "ConstraintsUnion", "ValueRangeConstraint", "ConstraintsIntersection", "ValueSizeConstraint")
ScsiIndexValue, ciscoScsiInstanceEntry, ciscoScsiDscLunEntry, ciscoScsiDscTgtEntry = mibBuilder.importSymbols("CISCO-SCSI-MIB", "ScsiIndexValue", "ciscoScsiInstanceEntry", "ciscoScsiDscLunEntry", "ciscoScsiDscTgtEntry")
ciscoMgmt, = mibBuilder.importSymbols("CISCO-SMI", "ciscoMgmt")
VsanIndex, FcAddressId, DomainId = mibBuilder.importSymbols("CISCO-ST-TC", "VsanIndex", "FcAddressId", "DomainId")
vsanIndex, = mibBuilder.importSymbols("CISCO-VSAN-MIB", "vsanIndex")
ObjectGroup, ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ObjectGroup", "ModuleCompliance", "NotificationGroup")
Counter32, ModuleIdentity, NotificationType, Integer32, Counter64, MibIdentifier, Unsigned32, ObjectIdentity, Bits, iso, MibScalar, MibTable, MibTableRow, MibTableColumn, Gauge32, IpAddress, TimeTicks = mibBuilder.importSymbols("SNMPv2-SMI", "Counter32", "ModuleIdentity", "NotificationType", "Integer32", "Counter64", "MibIdentifier", "Unsigned32", "ObjectIdentity", "Bits", "iso", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Gauge32", "IpAddress", "TimeTicks")
TruthValue, DisplayString, TimeStamp, TestAndIncr, TextualConvention, RowStatus = mibBuilder.importSymbols("SNMPv2-TC", "TruthValue", "DisplayString", "TimeStamp", "TestAndIncr", "TextualConvention", "RowStatus")
ciscoExtScsiMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 9, 299))
ciscoExtScsiMIB.setRevisions(('2004-03-14 00:00', '2003-11-28 00:00', '2003-01-28 00:00', '2002-10-10 00:00', '2002-10-05 00:00',))
if mibBuilder.loadTexts: ciscoExtScsiMIB.setLastUpdated('200403140000Z')
if mibBuilder.loadTexts: ciscoExtScsiMIB.setOrganization('Cisco Systems Inc.')
ciscoExtScsiMIBObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 299, 1))
ciscoExtScsiMIBConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 299, 2))
ciscoExtScsiConfiguration = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 299, 1, 1))
ciscoExtScsiNotification = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 299, 1, 2))
ciscoExtScsiNotifications = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 299, 1, 2, 0))
ciscoExtScsiStats = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 299, 1, 3))
class LunDiscOS(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6))
    namedValues = NamedValues(("windows", 1), ("aix", 2), ("solaris", 3), ("linux", 4), ("hpux", 5), ("all", 6))

ciscoExtScsiGenInstanceTable = MibTable((1, 3, 6, 1, 4, 1, 9, 9, 299, 1, 1, 1), )
if mibBuilder.loadTexts: ciscoExtScsiGenInstanceTable.setStatus('current')
ciscoExtScsiGenInstanceEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9, 9, 299, 1, 1, 1, 1), )
ciscoScsiInstanceEntry.registerAugmentions(("CISCO-EXT-SCSI-MIB", "ciscoExtScsiGenInstanceEntry"))
ciscoExtScsiGenInstanceEntry.setIndexNames(*ciscoScsiInstanceEntry.getIndexNames())
if mibBuilder.loadTexts: ciscoExtScsiGenInstanceEntry.setStatus('current')
ciscoExtScsiDiskGrpId = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 299, 1, 1, 1, 1, 1), OctetString().subtype(subtypeSpec=ConstraintsUnion(ValueSizeConstraint(0, 0), ValueSizeConstraint(64, 64), ))).setMaxAccess("readonly")
if mibBuilder.loadTexts: ciscoExtScsiDiskGrpId.setStatus('current')
ciscoExtScsiLineCardOrSup = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 299, 1, 1, 1, 1, 2), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(1, 2147483647))).setMaxAccess("readonly")
if mibBuilder.loadTexts: ciscoExtScsiLineCardOrSup.setStatus('current')
ciscoExtScsiLunDiscSpinLock = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 299, 1, 1, 2), TestAndIncr()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ciscoExtScsiLunDiscSpinLock.setStatus('current')
ciscoExtScsiStartLunDisc = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 299, 1, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6))).clone(namedValues=NamedValues(("startDiscovery", 1), ("startLocalDiscovery", 2), ("startRemoteDiscovery", 3), ("noop", 4), ("startPartialDiscovery", 5), ("startPortBasedDiscovery", 6)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ciscoExtScsiStartLunDisc.setStatus('current')
ciscoExtScsiLunDiscStatus = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 299, 1, 1, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("inProgress", 1), ("completed", 2), ("failure", 3)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: ciscoExtScsiLunDiscStatus.setStatus('current')
ciscoExtScsiLunDiscCompleteTime = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 299, 1, 1, 5), TimeStamp()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ciscoExtScsiLunDiscCompleteTime.setStatus('current')
ciscoExtScsiIntrDiscTgtTable = MibTable((1, 3, 6, 1, 4, 1, 9, 9, 299, 1, 1, 6), )
if mibBuilder.loadTexts: ciscoExtScsiIntrDiscTgtTable.setStatus('current')
ciscoExtScsiIntrDiscTgtEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9, 9, 299, 1, 1, 6, 1), )
ciscoScsiDscTgtEntry.registerAugmentions(("CISCO-EXT-SCSI-MIB", "ciscoExtScsiIntrDiscTgtEntry"))
ciscoExtScsiIntrDiscTgtEntry.setIndexNames(*ciscoScsiDscTgtEntry.getIndexNames())
if mibBuilder.loadTexts: ciscoExtScsiIntrDiscTgtEntry.setStatus('current')
ciscoExtScsiIntrDiscTgtVsanId = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 299, 1, 1, 6, 1, 1), VsanIndex()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ciscoExtScsiIntrDiscTgtVsanId.setStatus('current')
ciscoExtScsiIntrDiscTgtDevType = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 299, 1, 1, 6, 1, 2), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ciscoExtScsiIntrDiscTgtDevType.setStatus('current')
ciscoExtScsiIntrDiscTgtVendorId = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 299, 1, 1, 6, 1, 3), OctetString().subtype(subtypeSpec=ValueSizeConstraint(8, 8)).setFixedLength(8)).setMaxAccess("readonly")
if mibBuilder.loadTexts: ciscoExtScsiIntrDiscTgtVendorId.setStatus('current')
ciscoExtScsiIntrDiscTgtProductId = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 299, 1, 1, 6, 1, 4), OctetString().subtype(subtypeSpec=ValueSizeConstraint(16, 16)).setFixedLength(16)).setMaxAccess("readonly")
if mibBuilder.loadTexts: ciscoExtScsiIntrDiscTgtProductId.setStatus('current')
ciscoExtScsiIntrDiscTgtRevLevel = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 299, 1, 1, 6, 1, 5), OctetString().subtype(subtypeSpec=ValueSizeConstraint(4, 4)).setFixedLength(4)).setMaxAccess("readonly")
if mibBuilder.loadTexts: ciscoExtScsiIntrDiscTgtRevLevel.setStatus('current')
ciscoExtScsiIntrDiscTgtOtherInfo = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 299, 1, 1, 6, 1, 6), OctetString().subtype(subtypeSpec=ValueSizeConstraint(8, 8)).setFixedLength(8)).setMaxAccess("readonly")
if mibBuilder.loadTexts: ciscoExtScsiIntrDiscTgtOtherInfo.setStatus('current')
ciscoExtScsiIntrDiscLunsTable = MibTable((1, 3, 6, 1, 4, 1, 9, 9, 299, 1, 1, 7), )
if mibBuilder.loadTexts: ciscoExtScsiIntrDiscLunsTable.setStatus('current')
ciscoExtScsiIntrDiscLunsEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9, 9, 299, 1, 1, 7, 1), )
ciscoScsiDscLunEntry.registerAugmentions(("CISCO-EXT-SCSI-MIB", "ciscoExtScsiIntrDiscLunsEntry"))
ciscoExtScsiIntrDiscLunsEntry.setIndexNames(*ciscoScsiDscLunEntry.getIndexNames())
if mibBuilder.loadTexts: ciscoExtScsiIntrDiscLunsEntry.setStatus('current')
ciscoExtScsiIntrDiscLunCapacity = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 299, 1, 1, 7, 1, 1), Unsigned32()).setUnits('MBytes').setMaxAccess("readonly")
if mibBuilder.loadTexts: ciscoExtScsiIntrDiscLunCapacity.setStatus('current')
ciscoExtScsiIntrDiscLunNumber = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 299, 1, 1, 7, 1, 2), OctetString().subtype(subtypeSpec=ValueSizeConstraint(8, 8)).setFixedLength(8)).setMaxAccess("readonly")
if mibBuilder.loadTexts: ciscoExtScsiIntrDiscLunNumber.setStatus('current')
ciscoExtScsiIntrDiscLunSerialNum = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 299, 1, 1, 7, 1, 3), OctetString().subtype(subtypeSpec=ValueSizeConstraint(0, 32))).setMaxAccess("readonly")
if mibBuilder.loadTexts: ciscoExtScsiIntrDiscLunSerialNum.setStatus('current')
ciscoExtScsiIntrDiscLunOs = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 299, 1, 1, 7, 1, 4), LunDiscOS()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ciscoExtScsiIntrDiscLunOs.setStatus('current')
ciscoExtScsiIntrDiscLunPortId = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 299, 1, 1, 7, 1, 5), FcAddressId()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ciscoExtScsiIntrDiscLunPortId.setStatus('current')
ciscoExtScsiNotificationCntl = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 299, 1, 1, 8), TruthValue().clone('false')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ciscoExtScsiNotificationCntl.setStatus('current')
ciscoExtScsiPartialLunDiscTable = MibTable((1, 3, 6, 1, 4, 1, 9, 9, 299, 1, 1, 9), )
if mibBuilder.loadTexts: ciscoExtScsiPartialLunDiscTable.setStatus('current')
ciscoExtScsiPartialLunDiscEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9, 9, 299, 1, 1, 9, 1), ).setIndexNames((0, "CISCO-VSAN-MIB", "vsanIndex"), (0, "CISCO-EXT-SCSI-MIB", "ciscoExtScsiPartialLunDomId"))
if mibBuilder.loadTexts: ciscoExtScsiPartialLunDiscEntry.setStatus('current')
ciscoExtScsiPartialLunDomId = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 299, 1, 1, 9, 1, 1), DomainId())
if mibBuilder.loadTexts: ciscoExtScsiPartialLunDomId.setStatus('current')
ciscoExtScsiPartialLunRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 299, 1, 1, 9, 1, 2), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: ciscoExtScsiPartialLunRowStatus.setStatus('current')
ciscoExtScsiLunDiscOs = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 299, 1, 1, 10), LunDiscOS().clone('windows')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ciscoExtScsiLunDiscOs.setStatus('current')
ciscoExtScsiLunDiscVsanId = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 299, 1, 1, 11), VsanIndex().clone(1)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ciscoExtScsiLunDiscVsanId.setStatus('current')
ciscoExtScsiLunDiscPortId = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 299, 1, 1, 12), FcAddressId().clone(hexValue="000000")).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ciscoExtScsiLunDiscPortId.setStatus('current')
ciscoExtScsiLunCacheScsiIndex = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 299, 1, 1, 13), ScsiIndexValue()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ciscoExtScsiLunCacheScsiIndex.setStatus('current')
ciscoExtScsiLunCacheDevIndex = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 299, 1, 1, 14), ScsiIndexValue()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ciscoExtScsiLunCacheDevIndex.setStatus('current')
ciscoExtScsiLunCachePortIndex = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 299, 1, 1, 15), ScsiIndexValue()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ciscoExtScsiLunCachePortIndex.setStatus('current')
ciscoExtScsiLunCacheTgtIndex = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 299, 1, 1, 16), ScsiIndexValue()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ciscoExtScsiLunCacheTgtIndex.setStatus('current')
ciscoExtScsiDiscType = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 299, 1, 1, 17), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("targets", 1), ("luns", 2))).clone('luns')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ciscoExtScsiDiscType.setStatus('current')
ciscoExtScsiLunDiscDoneNotify = NotificationType((1, 3, 6, 1, 4, 1, 9, 9, 299, 1, 2, 0, 1)).setObjects(("CISCO-EXT-SCSI-MIB", "ciscoExtScsiLunDiscStatus"))
if mibBuilder.loadTexts: ciscoExtScsiLunDiscDoneNotify.setStatus('current')
ciscoExtScsiMIBCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 299, 2, 1))
ciscoExtScsiMIBGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 299, 2, 2))
ciscoExtScsiMIBCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 9, 9, 299, 2, 1, 1)).setObjects(("CISCO-EXT-SCSI-MIB", "ciscoExtScsiConfigGroup"), ("CISCO-EXT-SCSI-MIB", "ciscoExtScsiNotifyControlGroup"), ("CISCO-EXT-SCSI-MIB", "ciscoExtScsiNotifyGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoExtScsiMIBCompliance = ciscoExtScsiMIBCompliance.setStatus('deprecated')
ciscoExtScsiMIBCompliance2 = ModuleCompliance((1, 3, 6, 1, 4, 1, 9, 9, 299, 2, 1, 2)).setObjects(("CISCO-EXT-SCSI-MIB", "ciscoExtScsiConfigGroup"), ("CISCO-EXT-SCSI-MIB", "ciscoExtScsiPartialDiscGroup"), ("CISCO-EXT-SCSI-MIB", "ciscoExtScsiNotifyControlGroup"), ("CISCO-EXT-SCSI-MIB", "ciscoExtScsiNotifyGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoExtScsiMIBCompliance2 = ciscoExtScsiMIBCompliance2.setStatus('deprecated')
ciscoExtScsiMIBComplianceRev3 = ModuleCompliance((1, 3, 6, 1, 4, 1, 9, 9, 299, 2, 1, 3)).setObjects(("CISCO-EXT-SCSI-MIB", "ciscoExtScsiConfigGroup1"), ("CISCO-EXT-SCSI-MIB", "ciscoExtScsiPartialDiscGroup"), ("CISCO-EXT-SCSI-MIB", "ciscoExtScsiNotifyControlGroup"), ("CISCO-EXT-SCSI-MIB", "ciscoExtScsiNotifyGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoExtScsiMIBComplianceRev3 = ciscoExtScsiMIBComplianceRev3.setStatus('deprecated')
ciscoExtScsiMIBComplianceRev4 = ModuleCompliance((1, 3, 6, 1, 4, 1, 9, 9, 299, 2, 1, 4)).setObjects(("CISCO-EXT-SCSI-MIB", "ciscoExtScsiConfigGroup2"), ("CISCO-EXT-SCSI-MIB", "ciscoExtScsiPartialDiscGroup"), ("CISCO-EXT-SCSI-MIB", "ciscoExtScsiNotifyControlGroup"), ("CISCO-EXT-SCSI-MIB", "ciscoExtScsiNotifyGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoExtScsiMIBComplianceRev4 = ciscoExtScsiMIBComplianceRev4.setStatus('current')
ciscoExtScsiConfigGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 299, 2, 2, 1)).setObjects(("CISCO-EXT-SCSI-MIB", "ciscoExtScsiDiskGrpId"), ("CISCO-EXT-SCSI-MIB", "ciscoExtScsiLineCardOrSup"), ("CISCO-EXT-SCSI-MIB", "ciscoExtScsiLunDiscSpinLock"), ("CISCO-EXT-SCSI-MIB", "ciscoExtScsiStartLunDisc"), ("CISCO-EXT-SCSI-MIB", "ciscoExtScsiLunDiscStatus"), ("CISCO-EXT-SCSI-MIB", "ciscoExtScsiLunDiscCompleteTime"), ("CISCO-EXT-SCSI-MIB", "ciscoExtScsiIntrDiscTgtVsanId"), ("CISCO-EXT-SCSI-MIB", "ciscoExtScsiIntrDiscTgtDevType"), ("CISCO-EXT-SCSI-MIB", "ciscoExtScsiIntrDiscTgtVendorId"), ("CISCO-EXT-SCSI-MIB", "ciscoExtScsiIntrDiscTgtProductId"), ("CISCO-EXT-SCSI-MIB", "ciscoExtScsiIntrDiscTgtRevLevel"), ("CISCO-EXT-SCSI-MIB", "ciscoExtScsiIntrDiscTgtOtherInfo"), ("CISCO-EXT-SCSI-MIB", "ciscoExtScsiIntrDiscLunCapacity"), ("CISCO-EXT-SCSI-MIB", "ciscoExtScsiIntrDiscLunNumber"), ("CISCO-EXT-SCSI-MIB", "ciscoExtScsiIntrDiscLunSerialNum"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoExtScsiConfigGroup = ciscoExtScsiConfigGroup.setStatus('deprecated')
ciscoExtScsiNotifyControlGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 299, 2, 2, 2)).setObjects(("CISCO-EXT-SCSI-MIB", "ciscoExtScsiNotificationCntl"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoExtScsiNotifyControlGroup = ciscoExtScsiNotifyControlGroup.setStatus('current')
ciscoExtScsiNotifyGroup = NotificationGroup((1, 3, 6, 1, 4, 1, 9, 9, 299, 2, 2, 3)).setObjects(("CISCO-EXT-SCSI-MIB", "ciscoExtScsiLunDiscDoneNotify"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoExtScsiNotifyGroup = ciscoExtScsiNotifyGroup.setStatus('current')
ciscoExtScsiPartialDiscGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 299, 2, 2, 4)).setObjects(("CISCO-EXT-SCSI-MIB", "ciscoExtScsiPartialLunRowStatus"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoExtScsiPartialDiscGroup = ciscoExtScsiPartialDiscGroup.setStatus('current')
ciscoExtScsiConfigGroup1 = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 299, 2, 2, 5)).setObjects(("CISCO-EXT-SCSI-MIB", "ciscoExtScsiDiskGrpId"), ("CISCO-EXT-SCSI-MIB", "ciscoExtScsiLineCardOrSup"), ("CISCO-EXT-SCSI-MIB", "ciscoExtScsiLunDiscSpinLock"), ("CISCO-EXT-SCSI-MIB", "ciscoExtScsiLunDiscOs"), ("CISCO-EXT-SCSI-MIB", "ciscoExtScsiStartLunDisc"), ("CISCO-EXT-SCSI-MIB", "ciscoExtScsiLunDiscStatus"), ("CISCO-EXT-SCSI-MIB", "ciscoExtScsiLunDiscCompleteTime"), ("CISCO-EXT-SCSI-MIB", "ciscoExtScsiIntrDiscTgtVsanId"), ("CISCO-EXT-SCSI-MIB", "ciscoExtScsiIntrDiscTgtDevType"), ("CISCO-EXT-SCSI-MIB", "ciscoExtScsiIntrDiscTgtVendorId"), ("CISCO-EXT-SCSI-MIB", "ciscoExtScsiIntrDiscTgtProductId"), ("CISCO-EXT-SCSI-MIB", "ciscoExtScsiIntrDiscTgtRevLevel"), ("CISCO-EXT-SCSI-MIB", "ciscoExtScsiIntrDiscTgtOtherInfo"), ("CISCO-EXT-SCSI-MIB", "ciscoExtScsiIntrDiscLunCapacity"), ("CISCO-EXT-SCSI-MIB", "ciscoExtScsiIntrDiscLunNumber"), ("CISCO-EXT-SCSI-MIB", "ciscoExtScsiIntrDiscLunSerialNum"), ("CISCO-EXT-SCSI-MIB", "ciscoExtScsiIntrDiscLunOs"), ("CISCO-EXT-SCSI-MIB", "ciscoExtScsiLunDiscVsanId"), ("CISCO-EXT-SCSI-MIB", "ciscoExtScsiLunDiscPortId"), ("CISCO-EXT-SCSI-MIB", "ciscoExtScsiLunCacheScsiIndex"), ("CISCO-EXT-SCSI-MIB", "ciscoExtScsiLunCacheDevIndex"), ("CISCO-EXT-SCSI-MIB", "ciscoExtScsiLunCachePortIndex"), ("CISCO-EXT-SCSI-MIB", "ciscoExtScsiLunCacheTgtIndex"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoExtScsiConfigGroup1 = ciscoExtScsiConfigGroup1.setStatus('deprecated')
ciscoExtScsiConfigGroup2 = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 299, 2, 2, 6)).setObjects(("CISCO-EXT-SCSI-MIB", "ciscoExtScsiDiskGrpId"), ("CISCO-EXT-SCSI-MIB", "ciscoExtScsiLineCardOrSup"), ("CISCO-EXT-SCSI-MIB", "ciscoExtScsiLunDiscSpinLock"), ("CISCO-EXT-SCSI-MIB", "ciscoExtScsiLunDiscOs"), ("CISCO-EXT-SCSI-MIB", "ciscoExtScsiStartLunDisc"), ("CISCO-EXT-SCSI-MIB", "ciscoExtScsiLunDiscStatus"), ("CISCO-EXT-SCSI-MIB", "ciscoExtScsiLunDiscCompleteTime"), ("CISCO-EXT-SCSI-MIB", "ciscoExtScsiIntrDiscTgtVsanId"), ("CISCO-EXT-SCSI-MIB", "ciscoExtScsiIntrDiscTgtDevType"), ("CISCO-EXT-SCSI-MIB", "ciscoExtScsiIntrDiscTgtVendorId"), ("CISCO-EXT-SCSI-MIB", "ciscoExtScsiIntrDiscTgtProductId"), ("CISCO-EXT-SCSI-MIB", "ciscoExtScsiIntrDiscTgtRevLevel"), ("CISCO-EXT-SCSI-MIB", "ciscoExtScsiIntrDiscTgtOtherInfo"), ("CISCO-EXT-SCSI-MIB", "ciscoExtScsiIntrDiscLunCapacity"), ("CISCO-EXT-SCSI-MIB", "ciscoExtScsiIntrDiscLunNumber"), ("CISCO-EXT-SCSI-MIB", "ciscoExtScsiIntrDiscLunSerialNum"), ("CISCO-EXT-SCSI-MIB", "ciscoExtScsiIntrDiscLunOs"), ("CISCO-EXT-SCSI-MIB", "ciscoExtScsiIntrDiscLunPortId"), ("CISCO-EXT-SCSI-MIB", "ciscoExtScsiLunDiscVsanId"), ("CISCO-EXT-SCSI-MIB", "ciscoExtScsiLunDiscPortId"), ("CISCO-EXT-SCSI-MIB", "ciscoExtScsiLunCacheScsiIndex"), ("CISCO-EXT-SCSI-MIB", "ciscoExtScsiLunCacheDevIndex"), ("CISCO-EXT-SCSI-MIB", "ciscoExtScsiLunCachePortIndex"), ("CISCO-EXT-SCSI-MIB", "ciscoExtScsiLunCacheTgtIndex"), ("CISCO-EXT-SCSI-MIB", "ciscoExtScsiDiscType"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoExtScsiConfigGroup2 = ciscoExtScsiConfigGroup2.setStatus('current')
mibBuilder.exportSymbols("CISCO-EXT-SCSI-MIB", ciscoExtScsiLunCacheDevIndex=ciscoExtScsiLunCacheDevIndex, ciscoExtScsiMIBCompliances=ciscoExtScsiMIBCompliances, ciscoExtScsiIntrDiscLunNumber=ciscoExtScsiIntrDiscLunNumber, ciscoExtScsiIntrDiscTgtVsanId=ciscoExtScsiIntrDiscTgtVsanId, ciscoExtScsiLunDiscOs=ciscoExtScsiLunDiscOs, ciscoExtScsiLunCacheScsiIndex=ciscoExtScsiLunCacheScsiIndex, ciscoExtScsiMIB=ciscoExtScsiMIB, ciscoExtScsiConfigGroup1=ciscoExtScsiConfigGroup1, ciscoExtScsiIntrDiscTgtTable=ciscoExtScsiIntrDiscTgtTable, ciscoExtScsiMIBCompliance=ciscoExtScsiMIBCompliance, ciscoExtScsiPartialDiscGroup=ciscoExtScsiPartialDiscGroup, ciscoExtScsiIntrDiscTgtDevType=ciscoExtScsiIntrDiscTgtDevType, ciscoExtScsiPartialLunRowStatus=ciscoExtScsiPartialLunRowStatus, ciscoExtScsiNotifications=ciscoExtScsiNotifications, ciscoExtScsiNotification=ciscoExtScsiNotification, ciscoExtScsiDiscType=ciscoExtScsiDiscType, ciscoExtScsiIntrDiscLunCapacity=ciscoExtScsiIntrDiscLunCapacity, ciscoExtScsiLunDiscCompleteTime=ciscoExtScsiLunDiscCompleteTime, ciscoExtScsiLunCacheTgtIndex=ciscoExtScsiLunCacheTgtIndex, ciscoExtScsiIntrDiscLunSerialNum=ciscoExtScsiIntrDiscLunSerialNum, ciscoExtScsiIntrDiscTgtOtherInfo=ciscoExtScsiIntrDiscTgtOtherInfo, ciscoExtScsiIntrDiscLunsEntry=ciscoExtScsiIntrDiscLunsEntry, ciscoExtScsiConfigGroup=ciscoExtScsiConfigGroup, ciscoExtScsiNotificationCntl=ciscoExtScsiNotificationCntl, ciscoExtScsiIntrDiscLunOs=ciscoExtScsiIntrDiscLunOs, ciscoExtScsiMIBCompliance2=ciscoExtScsiMIBCompliance2, ciscoExtScsiIntrDiscTgtProductId=ciscoExtScsiIntrDiscTgtProductId, ciscoExtScsiLunDiscSpinLock=ciscoExtScsiLunDiscSpinLock, ciscoExtScsiLunDiscDoneNotify=ciscoExtScsiLunDiscDoneNotify, ciscoExtScsiMIBConformance=ciscoExtScsiMIBConformance, ciscoExtScsiDiskGrpId=ciscoExtScsiDiskGrpId, ciscoExtScsiLunDiscStatus=ciscoExtScsiLunDiscStatus, ciscoExtScsiPartialLunDiscTable=ciscoExtScsiPartialLunDiscTable, ciscoExtScsiIntrDiscTgtRevLevel=ciscoExtScsiIntrDiscTgtRevLevel, ciscoExtScsiMIBComplianceRev4=ciscoExtScsiMIBComplianceRev4, ciscoExtScsiIntrDiscLunPortId=ciscoExtScsiIntrDiscLunPortId, ciscoExtScsiNotifyGroup=ciscoExtScsiNotifyGroup, ciscoExtScsiPartialLunDomId=ciscoExtScsiPartialLunDomId, ciscoExtScsiGenInstanceEntry=ciscoExtScsiGenInstanceEntry, ciscoExtScsiIntrDiscTgtVendorId=ciscoExtScsiIntrDiscTgtVendorId, ciscoExtScsiConfiguration=ciscoExtScsiConfiguration, ciscoExtScsiLunDiscVsanId=ciscoExtScsiLunDiscVsanId, ciscoExtScsiStats=ciscoExtScsiStats, ciscoExtScsiNotifyControlGroup=ciscoExtScsiNotifyControlGroup, ciscoExtScsiConfigGroup2=ciscoExtScsiConfigGroup2, ciscoExtScsiLineCardOrSup=ciscoExtScsiLineCardOrSup, ciscoExtScsiStartLunDisc=ciscoExtScsiStartLunDisc, ciscoExtScsiPartialLunDiscEntry=ciscoExtScsiPartialLunDiscEntry, ciscoExtScsiMIBComplianceRev3=ciscoExtScsiMIBComplianceRev3, PYSNMP_MODULE_ID=ciscoExtScsiMIB, ciscoExtScsiLunCachePortIndex=ciscoExtScsiLunCachePortIndex, LunDiscOS=LunDiscOS, ciscoExtScsiIntrDiscTgtEntry=ciscoExtScsiIntrDiscTgtEntry, ciscoExtScsiMIBGroups=ciscoExtScsiMIBGroups, ciscoExtScsiMIBObjects=ciscoExtScsiMIBObjects, ciscoExtScsiIntrDiscLunsTable=ciscoExtScsiIntrDiscLunsTable, ciscoExtScsiLunDiscPortId=ciscoExtScsiLunDiscPortId, ciscoExtScsiGenInstanceTable=ciscoExtScsiGenInstanceTable)