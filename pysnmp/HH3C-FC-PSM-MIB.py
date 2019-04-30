#
# PySNMP MIB module HH3C-FC-PSM-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/HH3C-FC-PSM-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 19:14:01 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsUnion, ValueSizeConstraint, ValueRangeConstraint, ConstraintsIntersection, SingleValueConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "ValueSizeConstraint", "ValueRangeConstraint", "ConstraintsIntersection", "SingleValueConstraint")
Hh3cFcNameIdOrZero, = mibBuilder.importSymbols("HH3C-FC-TC-MIB", "Hh3cFcNameIdOrZero")
hh3cSan, = mibBuilder.importSymbols("HH3C-VSAN-MIB", "hh3cSan")
InterfaceIndex, InterfaceIndexOrZero, ifDescr = mibBuilder.importSymbols("IF-MIB", "InterfaceIndex", "InterfaceIndexOrZero", "ifDescr")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
NotificationType, Counter32, MibIdentifier, MibScalar, MibTable, MibTableRow, MibTableColumn, Gauge32, IpAddress, ObjectIdentity, Counter64, Bits, TimeTicks, Unsigned32, Integer32, ModuleIdentity, iso = mibBuilder.importSymbols("SNMPv2-SMI", "NotificationType", "Counter32", "MibIdentifier", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Gauge32", "IpAddress", "ObjectIdentity", "Counter64", "Bits", "TimeTicks", "Unsigned32", "Integer32", "ModuleIdentity", "iso")
TimeStamp, RowStatus, DisplayString, TextualConvention, TruthValue = mibBuilder.importSymbols("SNMPv2-TC", "TimeStamp", "RowStatus", "DisplayString", "TextualConvention", "TruthValue")
hh3cFcPsm = ModuleIdentity((1, 3, 6, 1, 4, 1, 25506, 2, 127, 8))
hh3cFcPsm.setRevisions(('2013-10-17 00:00',))
if mibBuilder.loadTexts: hh3cFcPsm.setLastUpdated('201310170000Z')
if mibBuilder.loadTexts: hh3cFcPsm.setOrganization('Hangzhou H3C Tech. Co., Ltd.')
hh3cFcPsmNotifications = MibIdentifier((1, 3, 6, 1, 4, 1, 25506, 2, 127, 8, 0))
hh3cFcPsmObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 25506, 2, 127, 8, 1))
hh3cFcPsmScalarObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 25506, 2, 127, 8, 1, 1))
hh3cFcPsmConfiguration = MibIdentifier((1, 3, 6, 1, 4, 1, 25506, 2, 127, 8, 1, 2))
hh3cFcPsmStats = MibIdentifier((1, 3, 6, 1, 4, 1, 25506, 2, 127, 8, 1, 3))
class Hh3cFcPsmPortBindDevType(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))
    namedValues = NamedValues(("nWWN", 1), ("pWWN", 2), ("sWWN", 3), ("wildCard", 4))

class Hh3cFcPsmClearEntryType(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))
    namedValues = NamedValues(("clearStatic", 1), ("clearAutoLearn", 2), ("clearAll", 3), ("noop", 4))

hh3cFcPsmNotifyEnable = MibScalar((1, 3, 6, 1, 4, 1, 25506, 2, 127, 8, 1, 1, 1), TruthValue().clone('false')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hh3cFcPsmNotifyEnable.setStatus('current')
hh3cFcPsmEnableTable = MibTable((1, 3, 6, 1, 4, 1, 25506, 2, 127, 8, 1, 2, 1), )
if mibBuilder.loadTexts: hh3cFcPsmEnableTable.setStatus('current')
hh3cFcPsmEnableEntry = MibTableRow((1, 3, 6, 1, 4, 1, 25506, 2, 127, 8, 1, 2, 1, 1), ).setIndexNames((0, "HH3C-FC-PSM-MIB", "hh3cFcPsmEnableVsanIndex"))
if mibBuilder.loadTexts: hh3cFcPsmEnableEntry.setStatus('current')
hh3cFcPsmEnableVsanIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 2, 127, 8, 1, 2, 1, 1, 1), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(1, 4095)))
if mibBuilder.loadTexts: hh3cFcPsmEnableVsanIndex.setStatus('current')
hh3cFcPsmEnable = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 2, 127, 8, 1, 2, 1, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))).clone(namedValues=NamedValues(("enable", 1), ("enableWithAutoLearn", 2), ("disable", 3), ("noop", 4))).clone('noop')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hh3cFcPsmEnable.setStatus('current')
hh3cFcPsmEnableState = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 2, 127, 8, 1, 2, 1, 1, 3), TruthValue().clone('false')).setMaxAccess("readonly")
if mibBuilder.loadTexts: hh3cFcPsmEnableState.setStatus('current')
hh3cFcPsmConfigTable = MibTable((1, 3, 6, 1, 4, 1, 25506, 2, 127, 8, 1, 2, 2), )
if mibBuilder.loadTexts: hh3cFcPsmConfigTable.setStatus('current')
hh3cFcPsmConfigEntry = MibTableRow((1, 3, 6, 1, 4, 1, 25506, 2, 127, 8, 1, 2, 2, 1), ).setIndexNames((0, "HH3C-FC-PSM-MIB", "hh3cFcPsmEnableVsanIndex"), (0, "HH3C-FC-PSM-MIB", "hh3cFcPsmIndex"))
if mibBuilder.loadTexts: hh3cFcPsmConfigEntry.setStatus('current')
hh3cFcPsmIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 2, 127, 8, 1, 2, 2, 1, 1), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(1, 32768)))
if mibBuilder.loadTexts: hh3cFcPsmIndex.setStatus('current')
hh3cFcPsmLoginDevType = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 2, 127, 8, 1, 2, 2, 1, 2), Hh3cFcPsmPortBindDevType()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hh3cFcPsmLoginDevType.setStatus('current')
hh3cFcPsmLoginDev = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 2, 127, 8, 1, 2, 2, 1, 3), Hh3cFcNameIdOrZero()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hh3cFcPsmLoginDev.setStatus('current')
hh3cFcPsmLoginPoint = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 2, 127, 8, 1, 2, 2, 1, 4), InterfaceIndexOrZero()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hh3cFcPsmLoginPoint.setStatus('current')
hh3cFcPsmRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 2, 127, 8, 1, 2, 2, 1, 5), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hh3cFcPsmRowStatus.setStatus('current')
hh3cFcPsmEnfTable = MibTable((1, 3, 6, 1, 4, 1, 25506, 2, 127, 8, 1, 2, 3), )
if mibBuilder.loadTexts: hh3cFcPsmEnfTable.setStatus('current')
hh3cFcPsmEnfEntry = MibTableRow((1, 3, 6, 1, 4, 1, 25506, 2, 127, 8, 1, 2, 3, 1), ).setIndexNames((0, "HH3C-FC-PSM-MIB", "hh3cFcPsmEnableVsanIndex"), (0, "HH3C-FC-PSM-MIB", "hh3cFcPsmEnfIndex"))
if mibBuilder.loadTexts: hh3cFcPsmEnfEntry.setStatus('current')
hh3cFcPsmEnfIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 2, 127, 8, 1, 2, 3, 1, 1), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(1, 32768)))
if mibBuilder.loadTexts: hh3cFcPsmEnfIndex.setStatus('current')
hh3cFcPsmEnfLoginDevType = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 2, 127, 8, 1, 2, 3, 1, 2), Hh3cFcPsmPortBindDevType()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hh3cFcPsmEnfLoginDevType.setStatus('current')
hh3cFcPsmEnfLoginDev = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 2, 127, 8, 1, 2, 3, 1, 3), Hh3cFcNameIdOrZero()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hh3cFcPsmEnfLoginDev.setStatus('current')
hh3cFcPsmEnfLoginPoint = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 2, 127, 8, 1, 2, 3, 1, 4), InterfaceIndexOrZero()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hh3cFcPsmEnfLoginPoint.setStatus('current')
hh3cFcPsmEnfEntryType = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 2, 127, 8, 1, 2, 3, 1, 5), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("learning", 1), ("learnt", 2), ("static", 3)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: hh3cFcPsmEnfEntryType.setStatus('current')
hh3cFcPsmCopyToConfigTable = MibTable((1, 3, 6, 1, 4, 1, 25506, 2, 127, 8, 1, 2, 4), )
if mibBuilder.loadTexts: hh3cFcPsmCopyToConfigTable.setStatus('current')
hh3cFcPsmCopyToConfigEntry = MibTableRow((1, 3, 6, 1, 4, 1, 25506, 2, 127, 8, 1, 2, 4, 1), ).setIndexNames((0, "HH3C-FC-PSM-MIB", "hh3cFcPsmEnableVsanIndex"))
if mibBuilder.loadTexts: hh3cFcPsmCopyToConfigEntry.setStatus('current')
hh3cFcPsmCopyToConfig = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 2, 127, 8, 1, 2, 4, 1, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("copy", 1), ("noop", 2))).clone('noop')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hh3cFcPsmCopyToConfig.setStatus('current')
hh3cFcPsmAutoLearnTable = MibTable((1, 3, 6, 1, 4, 1, 25506, 2, 127, 8, 1, 2, 5), )
if mibBuilder.loadTexts: hh3cFcPsmAutoLearnTable.setStatus('current')
hh3cFcPsmAutoLearnEntry = MibTableRow((1, 3, 6, 1, 4, 1, 25506, 2, 127, 8, 1, 2, 5, 1), ).setIndexNames((0, "HH3C-FC-PSM-MIB", "hh3cFcPsmEnableVsanIndex"))
if mibBuilder.loadTexts: hh3cFcPsmAutoLearnEntry.setStatus('current')
hh3cFcPsmAutoLearnEnable = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 2, 127, 8, 1, 2, 5, 1, 1), TruthValue().clone('false')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hh3cFcPsmAutoLearnEnable.setStatus('current')
hh3cFcPsmClearTable = MibTable((1, 3, 6, 1, 4, 1, 25506, 2, 127, 8, 1, 2, 6), )
if mibBuilder.loadTexts: hh3cFcPsmClearTable.setStatus('current')
hh3cFcPsmClearEntry = MibTableRow((1, 3, 6, 1, 4, 1, 25506, 2, 127, 8, 1, 2, 6, 1), ).setIndexNames((0, "HH3C-FC-PSM-MIB", "hh3cFcPsmEnableVsanIndex"))
if mibBuilder.loadTexts: hh3cFcPsmClearEntry.setStatus('current')
hh3cFcPsmClearType = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 2, 127, 8, 1, 2, 6, 1, 1), Hh3cFcPsmClearEntryType().clone('noop')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hh3cFcPsmClearType.setStatus('current')
hh3cFcPsmClearIntf = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 2, 127, 8, 1, 2, 6, 1, 2), InterfaceIndexOrZero()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hh3cFcPsmClearIntf.setStatus('current')
hh3cFcPsmStatsTable = MibTable((1, 3, 6, 1, 4, 1, 25506, 2, 127, 8, 1, 3, 1), )
if mibBuilder.loadTexts: hh3cFcPsmStatsTable.setStatus('current')
hh3cFcPsmStatsEntry = MibTableRow((1, 3, 6, 1, 4, 1, 25506, 2, 127, 8, 1, 3, 1, 1), ).setIndexNames((0, "HH3C-FC-PSM-MIB", "hh3cFcPsmEnableVsanIndex"))
if mibBuilder.loadTexts: hh3cFcPsmStatsEntry.setStatus('current')
hh3cFcPsmAllowedLogins = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 2, 127, 8, 1, 3, 1, 1, 1), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hh3cFcPsmAllowedLogins.setStatus('current')
hh3cFcPsmDeniedLogins = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 2, 127, 8, 1, 3, 1, 1, 2), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hh3cFcPsmDeniedLogins.setStatus('current')
hh3cFcPsmStatsClear = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 2, 127, 8, 1, 3, 1, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("clear", 1), ("noop", 2))).clone('noop')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hh3cFcPsmStatsClear.setStatus('current')
hh3cFcPsmViolationTable = MibTable((1, 3, 6, 1, 4, 1, 25506, 2, 127, 8, 1, 3, 2), )
if mibBuilder.loadTexts: hh3cFcPsmViolationTable.setStatus('current')
hh3cFcPsmViolationEntry = MibTableRow((1, 3, 6, 1, 4, 1, 25506, 2, 127, 8, 1, 3, 2, 1), ).setIndexNames((0, "HH3C-FC-PSM-MIB", "hh3cFcPsmEnableVsanIndex"), (0, "HH3C-FC-PSM-MIB", "hh3cFcPsmViolationIndex"))
if mibBuilder.loadTexts: hh3cFcPsmViolationEntry.setStatus('current')
hh3cFcPsmViolationIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 2, 127, 8, 1, 3, 2, 1, 1), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(1, 1024)))
if mibBuilder.loadTexts: hh3cFcPsmViolationIndex.setStatus('current')
hh3cFcPsmLoginPWWN = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 2, 127, 8, 1, 3, 2, 1, 2), Hh3cFcNameIdOrZero()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hh3cFcPsmLoginPWWN.setStatus('current')
hh3cFcPsmLoginNWWN = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 2, 127, 8, 1, 3, 2, 1, 3), Hh3cFcNameIdOrZero()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hh3cFcPsmLoginNWWN.setStatus('current')
hh3cFcPsmLoginSWWN = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 2, 127, 8, 1, 3, 2, 1, 4), Hh3cFcNameIdOrZero()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hh3cFcPsmLoginSWWN.setStatus('current')
hh3cFcPsmLoginIntf = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 2, 127, 8, 1, 3, 2, 1, 5), InterfaceIndex()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hh3cFcPsmLoginIntf.setStatus('current')
hh3cFcPsmLoginTime = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 2, 127, 8, 1, 3, 2, 1, 6), TimeStamp()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hh3cFcPsmLoginTime.setStatus('current')
hh3cFcPsmLoginCount = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 2, 127, 8, 1, 3, 2, 1, 7), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hh3cFcPsmLoginCount.setStatus('current')
hh3cFcPsmFPortDenyNotify = NotificationType((1, 3, 6, 1, 4, 1, 25506, 2, 127, 8, 0, 1)).setObjects(("IF-MIB", "ifDescr"), ("HH3C-FC-PSM-MIB", "hh3cFcPsmLoginPWWN"), ("HH3C-FC-PSM-MIB", "hh3cFcPsmLoginIntf"), ("HH3C-FC-PSM-MIB", "hh3cFcPsmLoginTime"))
if mibBuilder.loadTexts: hh3cFcPsmFPortDenyNotify.setStatus('current')
hh3cFcPsmEPortDenyNotify = NotificationType((1, 3, 6, 1, 4, 1, 25506, 2, 127, 8, 0, 2)).setObjects(("IF-MIB", "ifDescr"), ("HH3C-FC-PSM-MIB", "hh3cFcPsmLoginSWWN"), ("HH3C-FC-PSM-MIB", "hh3cFcPsmLoginIntf"), ("HH3C-FC-PSM-MIB", "hh3cFcPsmLoginTime"))
if mibBuilder.loadTexts: hh3cFcPsmEPortDenyNotify.setStatus('current')
mibBuilder.exportSymbols("HH3C-FC-PSM-MIB", hh3cFcPsmEnableEntry=hh3cFcPsmEnableEntry, hh3cFcPsmConfigTable=hh3cFcPsmConfigTable, hh3cFcPsmLoginTime=hh3cFcPsmLoginTime, hh3cFcPsmFPortDenyNotify=hh3cFcPsmFPortDenyNotify, hh3cFcPsmIndex=hh3cFcPsmIndex, hh3cFcPsmStatsClear=hh3cFcPsmStatsClear, hh3cFcPsmStatsEntry=hh3cFcPsmStatsEntry, hh3cFcPsmAutoLearnTable=hh3cFcPsmAutoLearnTable, hh3cFcPsmLoginNWWN=hh3cFcPsmLoginNWWN, hh3cFcPsmConfigEntry=hh3cFcPsmConfigEntry, hh3cFcPsmNotifyEnable=hh3cFcPsmNotifyEnable, hh3cFcPsmEnable=hh3cFcPsmEnable, hh3cFcPsmEnableVsanIndex=hh3cFcPsmEnableVsanIndex, hh3cFcPsmScalarObjects=hh3cFcPsmScalarObjects, hh3cFcPsmCopyToConfig=hh3cFcPsmCopyToConfig, hh3cFcPsmLoginCount=hh3cFcPsmLoginCount, hh3cFcPsmCopyToConfigEntry=hh3cFcPsmCopyToConfigEntry, hh3cFcPsmConfiguration=hh3cFcPsmConfiguration, hh3cFcPsmLoginPoint=hh3cFcPsmLoginPoint, Hh3cFcPsmClearEntryType=Hh3cFcPsmClearEntryType, hh3cFcPsmClearIntf=hh3cFcPsmClearIntf, hh3cFcPsmViolationIndex=hh3cFcPsmViolationIndex, hh3cFcPsmEnfLoginPoint=hh3cFcPsmEnfLoginPoint, hh3cFcPsmEnfLoginDevType=hh3cFcPsmEnfLoginDevType, hh3cFcPsmEnfEntry=hh3cFcPsmEnfEntry, hh3cFcPsmEnfTable=hh3cFcPsmEnfTable, hh3cFcPsmClearTable=hh3cFcPsmClearTable, hh3cFcPsmLoginDev=hh3cFcPsmLoginDev, PYSNMP_MODULE_ID=hh3cFcPsm, hh3cFcPsmDeniedLogins=hh3cFcPsmDeniedLogins, hh3cFcPsmRowStatus=hh3cFcPsmRowStatus, hh3cFcPsmLoginPWWN=hh3cFcPsmLoginPWWN, hh3cFcPsmAutoLearnEnable=hh3cFcPsmAutoLearnEnable, hh3cFcPsmLoginSWWN=hh3cFcPsmLoginSWWN, hh3cFcPsmEnfEntryType=hh3cFcPsmEnfEntryType, hh3cFcPsmAllowedLogins=hh3cFcPsmAllowedLogins, hh3cFcPsmAutoLearnEntry=hh3cFcPsmAutoLearnEntry, hh3cFcPsmEnfIndex=hh3cFcPsmEnfIndex, hh3cFcPsmEPortDenyNotify=hh3cFcPsmEPortDenyNotify, hh3cFcPsmClearType=hh3cFcPsmClearType, hh3cFcPsmCopyToConfigTable=hh3cFcPsmCopyToConfigTable, hh3cFcPsmViolationTable=hh3cFcPsmViolationTable, hh3cFcPsmObjects=hh3cFcPsmObjects, hh3cFcPsmClearEntry=hh3cFcPsmClearEntry, hh3cFcPsmViolationEntry=hh3cFcPsmViolationEntry, hh3cFcPsmStats=hh3cFcPsmStats, hh3cFcPsmLoginDevType=hh3cFcPsmLoginDevType, hh3cFcPsm=hh3cFcPsm, hh3cFcPsmEnableTable=hh3cFcPsmEnableTable, hh3cFcPsmLoginIntf=hh3cFcPsmLoginIntf, hh3cFcPsmNotifications=hh3cFcPsmNotifications, Hh3cFcPsmPortBindDevType=Hh3cFcPsmPortBindDevType, hh3cFcPsmStatsTable=hh3cFcPsmStatsTable, hh3cFcPsmEnfLoginDev=hh3cFcPsmEnfLoginDev, hh3cFcPsmEnableState=hh3cFcPsmEnableState)