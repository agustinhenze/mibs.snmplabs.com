#
# PySNMP MIB module WRED-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/WRED-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 21:30:17 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
OctetString, Integer, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "OctetString", "Integer", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ValueRangeConstraint, ConstraintsIntersection, ConstraintsUnion, SingleValueConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ValueRangeConstraint", "ConstraintsIntersection", "ConstraintsUnion", "SingleValueConstraint")
dlink_common_mgmt, = mibBuilder.importSymbols("DLINK-ID-REC-MIB", "dlink-common-mgmt")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
Gauge32, Counter64, Counter32, iso, MibScalar, MibTable, MibTableRow, MibTableColumn, Unsigned32, IpAddress, TimeTicks, NotificationType, MibIdentifier, ObjectIdentity, Integer32, Bits, ModuleIdentity = mibBuilder.importSymbols("SNMPv2-SMI", "Gauge32", "Counter64", "Counter32", "iso", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Unsigned32", "IpAddress", "TimeTicks", "NotificationType", "MibIdentifier", "ObjectIdentity", "Integer32", "Bits", "ModuleIdentity")
DisplayString, TextualConvention, RowStatus = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention", "RowStatus")
swWredMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 171, 12, 31))
if mibBuilder.loadTexts: swWredMIB.setLastUpdated('1109300000Z')
if mibBuilder.loadTexts: swWredMIB.setOrganization('D-Link Corp.')
swWredCtrl = MibIdentifier((1, 3, 6, 1, 4, 1, 171, 12, 31, 1))
swWredInfo = MibIdentifier((1, 3, 6, 1, 4, 1, 171, 12, 31, 2))
swWredMgmt = MibIdentifier((1, 3, 6, 1, 4, 1, 171, 12, 31, 3))
swWredGlobalState = MibScalar((1, 3, 6, 1, 4, 1, 171, 12, 31, 1, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("other", 1), ("disabled", 2), ("enabled", 3)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: swWredGlobalState.setStatus('current')
swWredAverageTimeTable = MibTable((1, 3, 6, 1, 4, 1, 171, 12, 31, 3, 1), )
if mibBuilder.loadTexts: swWredAverageTimeTable.setStatus('current')
swWredAverageTimeEntry = MibTableRow((1, 3, 6, 1, 4, 1, 171, 12, 31, 3, 1, 1), ).setIndexNames((0, "WRED-MIB", "swWredPortIndex"))
if mibBuilder.loadTexts: swWredAverageTimeEntry.setStatus('current')
swWredPortIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 12, 31, 3, 1, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 65535))).setMaxAccess("readonly")
if mibBuilder.loadTexts: swWredPortIndex.setStatus('current')
swWredAverageTime = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 12, 31, 3, 1, 1, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 32768))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: swWredAverageTime.setStatus('current')
swWredCtrlTable = MibTable((1, 3, 6, 1, 4, 1, 171, 12, 31, 3, 2), )
if mibBuilder.loadTexts: swWredCtrlTable.setStatus('current')
swWredCtrlEntry = MibTableRow((1, 3, 6, 1, 4, 1, 171, 12, 31, 3, 2, 1), ).setIndexNames((0, "WRED-MIB", "swWredCtrlPortIndex"), (0, "WRED-MIB", "swWredCtrlClassIndex"))
if mibBuilder.loadTexts: swWredCtrlEntry.setStatus('current')
swWredCtrlPortIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 12, 31, 3, 2, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 65535))).setMaxAccess("readonly")
if mibBuilder.loadTexts: swWredCtrlPortIndex.setStatus('current')
swWredCtrlClassIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 12, 31, 3, 2, 1, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 7))).setMaxAccess("readonly")
if mibBuilder.loadTexts: swWredCtrlClassIndex.setStatus('current')
swWredCtrlDropStart = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 12, 31, 3, 2, 1, 3), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 100))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: swWredCtrlDropStart.setStatus('current')
swWredCtrlDropSlope = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 12, 31, 3, 2, 1, 4), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 90))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: swWredCtrlDropSlope.setStatus('current')
swWredProfileTable = MibTable((1, 3, 6, 1, 4, 1, 171, 12, 31, 3, 4), )
if mibBuilder.loadTexts: swWredProfileTable.setStatus('current')
swWredProfileEntry = MibTableRow((1, 3, 6, 1, 4, 1, 171, 12, 31, 3, 4, 1), ).setIndexNames((0, "WRED-MIB", "swWredProfileIndex"))
if mibBuilder.loadTexts: swWredProfileEntry.setStatus('current')
swWredProfileIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 12, 31, 3, 4, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: swWredProfileIndex.setStatus('current')
swWredProfileName = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 12, 31, 3, 4, 1, 2), DisplayString()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: swWredProfileName.setStatus('current')
swWredProfileRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 12, 31, 3, 4, 1, 3), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: swWredProfileRowStatus.setStatus('current')
swWredProfileCfgTable = MibTable((1, 3, 6, 1, 4, 1, 171, 12, 31, 3, 5), )
if mibBuilder.loadTexts: swWredProfileCfgTable.setStatus('current')
swWredProfileCfgEntry = MibTableRow((1, 3, 6, 1, 4, 1, 171, 12, 31, 3, 5, 1), ).setIndexNames((0, "WRED-MIB", "swWredProfileCfgIndex"), (0, "WRED-MIB", "swWredProfileCfgPacketType"), (0, "WRED-MIB", "swWredProfileCfgPacketColor"))
if mibBuilder.loadTexts: swWredProfileCfgEntry.setStatus('current')
swWredProfileCfgIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 12, 31, 3, 5, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 128))).setMaxAccess("readonly")
if mibBuilder.loadTexts: swWredProfileCfgIndex.setStatus('current')
swWredProfileCfgPacketType = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 12, 31, 3, 5, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("tcp", 1), ("nonTcp", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: swWredProfileCfgPacketType.setStatus('current')
swWredProfileCfgPacketColor = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 12, 31, 3, 5, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("green", 1), ("yellow", 2), ("red", 3)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: swWredProfileCfgPacketColor.setStatus('current')
swWredProfileCfgMinThreshold = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 12, 31, 3, 5, 1, 4), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 100))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: swWredProfileCfgMinThreshold.setStatus('current')
swWredProfileCfgMaxThreshold = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 12, 31, 3, 5, 1, 5), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 100))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: swWredProfileCfgMaxThreshold.setStatus('current')
swWredProfileCfgMaxDropRate = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 12, 31, 3, 5, 1, 6), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 100))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: swWredProfileCfgMaxDropRate.setStatus('current')
swWredPortProfileTable = MibTable((1, 3, 6, 1, 4, 1, 171, 12, 31, 3, 6), )
if mibBuilder.loadTexts: swWredPortProfileTable.setStatus('current')
swWredPortProfileEntry = MibTableRow((1, 3, 6, 1, 4, 1, 171, 12, 31, 3, 6, 1), ).setIndexNames((0, "WRED-MIB", "swWredPortProfilePortIndex"), (0, "WRED-MIB", "swWredPortProfileClassIndex"))
if mibBuilder.loadTexts: swWredPortProfileEntry.setStatus('current')
swWredPortProfilePortIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 12, 31, 3, 6, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 65535))).setMaxAccess("readonly")
if mibBuilder.loadTexts: swWredPortProfilePortIndex.setStatus('current')
swWredPortProfileClassIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 12, 31, 3, 6, 1, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 7))).setMaxAccess("readonly")
if mibBuilder.loadTexts: swWredPortProfileClassIndex.setStatus('current')
swWredPortProfileId = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 12, 31, 3, 6, 1, 3), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: swWredPortProfileId.setStatus('current')
swWredPortWeightNum = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 12, 31, 3, 6, 1, 4), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: swWredPortWeightNum.setStatus('current')
swWredAllPortAverageTime = MibScalar((1, 3, 6, 1, 4, 1, 171, 12, 31, 3, 3), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 32768))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: swWredAllPortAverageTime.setStatus('current')
mibBuilder.exportSymbols("WRED-MIB", swWredPortProfileEntry=swWredPortProfileEntry, swWredCtrlEntry=swWredCtrlEntry, swWredProfileEntry=swWredProfileEntry, swWredProfileCfgPacketColor=swWredProfileCfgPacketColor, swWredCtrlPortIndex=swWredCtrlPortIndex, swWredProfileName=swWredProfileName, swWredProfileRowStatus=swWredProfileRowStatus, swWredPortIndex=swWredPortIndex, swWredCtrlTable=swWredCtrlTable, swWredCtrlDropSlope=swWredCtrlDropSlope, swWredAverageTimeTable=swWredAverageTimeTable, swWredGlobalState=swWredGlobalState, PYSNMP_MODULE_ID=swWredMIB, swWredAverageTime=swWredAverageTime, swWredProfileCfgPacketType=swWredProfileCfgPacketType, swWredPortProfilePortIndex=swWredPortProfilePortIndex, swWredCtrlDropStart=swWredCtrlDropStart, swWredAllPortAverageTime=swWredAllPortAverageTime, swWredProfileCfgMaxDropRate=swWredProfileCfgMaxDropRate, swWredInfo=swWredInfo, swWredCtrl=swWredCtrl, swWredProfileTable=swWredProfileTable, swWredProfileCfgMaxThreshold=swWredProfileCfgMaxThreshold, swWredPortProfileId=swWredPortProfileId, swWredProfileCfgMinThreshold=swWredProfileCfgMinThreshold, swWredPortWeightNum=swWredPortWeightNum, swWredMgmt=swWredMgmt, swWredCtrlClassIndex=swWredCtrlClassIndex, swWredPortProfileClassIndex=swWredPortProfileClassIndex, swWredProfileCfgIndex=swWredProfileCfgIndex, swWredAverageTimeEntry=swWredAverageTimeEntry, swWredProfileCfgEntry=swWredProfileCfgEntry, swWredProfileIndex=swWredProfileIndex, swWredProfileCfgTable=swWredProfileCfgTable, swWredPortProfileTable=swWredPortProfileTable, swWredMIB=swWredMIB)
