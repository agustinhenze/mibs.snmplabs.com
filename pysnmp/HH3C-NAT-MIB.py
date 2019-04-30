#
# PySNMP MIB module HH3C-NAT-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/HH3C-NAT-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 19:15:53 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsUnion, ConstraintsIntersection, ValueSizeConstraint, ValueRangeConstraint, SingleValueConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "ConstraintsIntersection", "ValueSizeConstraint", "ValueRangeConstraint", "SingleValueConstraint")
hh3cCommon, = mibBuilder.importSymbols("HH3C-OID-MIB", "hh3cCommon")
ifIndex, = mibBuilder.importSymbols("IF-MIB", "ifIndex")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
MibIdentifier, NotificationType, MibScalar, MibTable, MibTableRow, MibTableColumn, Integer32, IpAddress, Gauge32, Counter64, TimeTicks, Counter32, ModuleIdentity, ObjectIdentity, Unsigned32, iso, Bits = mibBuilder.importSymbols("SNMPv2-SMI", "MibIdentifier", "NotificationType", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Integer32", "IpAddress", "Gauge32", "Counter64", "TimeTicks", "Counter32", "ModuleIdentity", "ObjectIdentity", "Unsigned32", "iso", "Bits")
RowStatus, TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "RowStatus", "TextualConvention", "DisplayString")
hh3cNat = ModuleIdentity((1, 3, 6, 1, 4, 1, 25506, 2, 18))
hh3cNat.setRevisions(('2005-01-20 15:18',))
if mibBuilder.loadTexts: hh3cNat.setLastUpdated('200409170100Z')
if mibBuilder.loadTexts: hh3cNat.setOrganization('Hangzhou H3C Tech. Co., Ltd.')
hh3cNATGlobalVars = MibIdentifier((1, 3, 6, 1, 4, 1, 25506, 2, 18, 1))
hh3cNATClearSession = MibIdentifier((1, 3, 6, 1, 4, 1, 25506, 2, 18, 1, 1))
hh3cNATClearSessionSlotNo = MibScalar((1, 3, 6, 1, 4, 1, 25506, 2, 18, 1, 1, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(ValueRangeConstraint(1, 14), ValueRangeConstraint(255, 255), ))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hh3cNATClearSessionSlotNo.setStatus('current')
hh3cNATBLConnectLimitPara = MibIdentifier((1, 3, 6, 1, 4, 1, 25506, 2, 18, 1, 2))
hh3cNATBLConnectHighValue = MibScalar((1, 3, 6, 1, 4, 1, 25506, 2, 18, 1, 2, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(20, 20000)).clone(500)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hh3cNATBLConnectHighValue.setStatus('current')
hh3cNATBLConnectLowValue = MibScalar((1, 3, 6, 1, 4, 1, 25506, 2, 18, 1, 2, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(20, 20000)).clone(200)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hh3cNATBLConnectLowValue.setStatus('current')
hh3cNATBLConnectHighRate = MibScalar((1, 3, 6, 1, 4, 1, 25506, 2, 18, 1, 2, 3), Integer32().subtype(subtypeSpec=ValueRangeConstraint(20, 21474836)).clone(250)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hh3cNATBLConnectHighRate.setStatus('current')
hh3cNATBLConnectLowRate = MibScalar((1, 3, 6, 1, 4, 1, 25506, 2, 18, 1, 2, 4), Integer32().subtype(subtypeSpec=ValueRangeConstraint(20, 21474836)).clone(100)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hh3cNATBLConnectLowRate.setStatus('current')
hh3cNATBLSpecialConnectHighRate = MibScalar((1, 3, 6, 1, 4, 1, 25506, 2, 18, 1, 2, 5), Integer32().subtype(subtypeSpec=ValueRangeConstraint(20, 21474836)).clone(250)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hh3cNATBLSpecialConnectHighRate.setStatus('current')
hh3cNATBLSpecialConnectLowRate = MibScalar((1, 3, 6, 1, 4, 1, 25506, 2, 18, 1, 2, 6), Integer32().subtype(subtypeSpec=ValueRangeConstraint(20, 21474836)).clone(100)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hh3cNATBLSpecialConnectLowRate.setStatus('current')
hh3cNATBLCtrlEnable = MibIdentifier((1, 3, 6, 1, 4, 1, 25506, 2, 18, 1, 3))
hh3cNATBLConnectSumEnable = MibScalar((1, 3, 6, 1, 4, 1, 25506, 2, 18, 1, 3, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enable", 1), ("disable", 2))).clone('disable')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hh3cNATBLConnectSumEnable.setStatus('current')
hh3cNATBLConnectRateEnable = MibScalar((1, 3, 6, 1, 4, 1, 25506, 2, 18, 1, 3, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enable", 1), ("disable", 2))).clone('disable')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hh3cNATBLConnectRateEnable.setStatus('current')
hh3cNATNPTimer = MibIdentifier((1, 3, 6, 1, 4, 1, 25506, 2, 18, 1, 4))
hh3cNATNPAgingTime = MibScalar((1, 3, 6, 1, 4, 1, 25506, 2, 18, 1, 4, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("fast", 1), ("slow", 2))).clone('fast')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hh3cNATNPAgingTime.setStatus('current')
hh3cNATMibObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 25506, 2, 18, 2))
hh3cNATPoolInfoTable = MibTable((1, 3, 6, 1, 4, 1, 25506, 2, 18, 2, 1), )
if mibBuilder.loadTexts: hh3cNATPoolInfoTable.setStatus('current')
hh3cNATPoolInfoEntry = MibTableRow((1, 3, 6, 1, 4, 1, 25506, 2, 18, 2, 1, 1), ).setIndexNames((0, "HH3C-NAT-MIB", "hh3cNATPoolIdx"))
if mibBuilder.loadTexts: hh3cNATPoolInfoEntry.setStatus('current')
hh3cNATPoolIdx = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 2, 18, 2, 1, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 320)))
if mibBuilder.loadTexts: hh3cNATPoolIdx.setStatus('current')
hh3cNATPoolStartIpAddr = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 2, 18, 2, 1, 1, 2), IpAddress()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hh3cNATPoolStartIpAddr.setStatus('current')
hh3cNATPoolEndIpAddr = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 2, 18, 2, 1, 1, 3), IpAddress()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hh3cNATPoolEndIpAddr.setStatus('current')
hh3cNATPoolSlotNo = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 2, 18, 2, 1, 1, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(ValueRangeConstraint(1, 14), ValueRangeConstraint(255, 255), ))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hh3cNATPoolSlotNo.setStatus('current')
hh3cNATPoolRefCounter = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 2, 18, 2, 1, 1, 5), Integer32()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hh3cNATPoolRefCounter.setStatus('current')
hh3cNATPoolRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 2, 18, 2, 1, 1, 6), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hh3cNATPoolRowStatus.setStatus('current')
hh3cNATOutboundTable = MibTable((1, 3, 6, 1, 4, 1, 25506, 2, 18, 2, 2), )
if mibBuilder.loadTexts: hh3cNATOutboundTable.setStatus('current')
hh3cNATOutboundEntry = MibTableRow((1, 3, 6, 1, 4, 1, 25506, 2, 18, 2, 2, 1), ).setIndexNames((0, "IF-MIB", "ifIndex"), (0, "HH3C-NAT-MIB", "hh3cNATOutboundAclNo"))
if mibBuilder.loadTexts: hh3cNATOutboundEntry.setStatus('current')
hh3cNATOutboundAclNo = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 2, 18, 2, 2, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(2000, 3999)))
if mibBuilder.loadTexts: hh3cNATOutboundAclNo.setStatus('current')
hh3cNATOutboundPoolIdx = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 2, 18, 2, 2, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(ValueRangeConstraint(0, 320), ValueRangeConstraint(2147483647, 2147483647), ))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hh3cNATOutboundPoolIdx.setStatus('current')
hh3cNATOutboundIsNoPat = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 2, 18, 2, 2, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("true", 1), ("false", 2))).clone('false')).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hh3cNATOutboundIsNoPat.setStatus('current')
hh3cNATOutboundSlotNo = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 2, 18, 2, 2, 1, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(ValueRangeConstraint(1, 14), ValueRangeConstraint(255, 255), ))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hh3cNATOutboundSlotNo.setStatus('current')
hh3cNATOutboundRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 2, 18, 2, 2, 1, 5), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hh3cNATOutboundRowStatus.setStatus('current')
hh3cNATServerTable = MibTable((1, 3, 6, 1, 4, 1, 25506, 2, 18, 2, 3), )
if mibBuilder.loadTexts: hh3cNATServerTable.setStatus('current')
hh3cNATServerEntry = MibTableRow((1, 3, 6, 1, 4, 1, 25506, 2, 18, 2, 3, 1), ).setIndexNames((0, "IF-MIB", "ifIndex"), (0, "HH3C-NAT-MIB", "hh3cNATServerProType"), (0, "HH3C-NAT-MIB", "hh3cNATServerGlobalIP"), (0, "HH3C-NAT-MIB", "hh3cNATServerStartGlobalPort"), (0, "HH3C-NAT-MIB", "hh3cNATServerVpnIndex"))
if mibBuilder.loadTexts: hh3cNATServerEntry.setStatus('current')
hh3cNATServerProType = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 2, 18, 2, 3, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 255)))
if mibBuilder.loadTexts: hh3cNATServerProType.setStatus('current')
hh3cNATServerGlobalIP = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 2, 18, 2, 3, 1, 2), IpAddress())
if mibBuilder.loadTexts: hh3cNATServerGlobalIP.setStatus('current')
hh3cNATServerStartGlobalPort = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 2, 18, 2, 3, 1, 3), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 65535)))
if mibBuilder.loadTexts: hh3cNATServerStartGlobalPort.setStatus('current')
hh3cNATServerEndGlobalPort = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 2, 18, 2, 3, 1, 4), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 65535))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hh3cNATServerEndGlobalPort.setStatus('current')
hh3cNATServerStartInsideIP = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 2, 18, 2, 3, 1, 5), IpAddress()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hh3cNATServerStartInsideIP.setStatus('current')
hh3cNATServerEndInsideIP = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 2, 18, 2, 3, 1, 6), IpAddress()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hh3cNATServerEndInsideIP.setStatus('current')
hh3cNATServerInsidePort = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 2, 18, 2, 3, 1, 7), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 65535))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hh3cNATServerInsidePort.setStatus('current')
hh3cNATServerSlotNo = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 2, 18, 2, 3, 1, 8), Integer32().subtype(subtypeSpec=ConstraintsUnion(ValueRangeConstraint(1, 14), ValueRangeConstraint(255, 255), ))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hh3cNATServerSlotNo.setStatus('current')
hh3cNATServerVpnIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 2, 18, 2, 3, 1, 10), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 65535)))
if mibBuilder.loadTexts: hh3cNATServerVpnIndex.setStatus('current')
hh3cNATServerAclNumber = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 2, 18, 2, 3, 1, 11), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 10000))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hh3cNATServerAclNumber.setStatus('current')
hh3cNATServerRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 2, 18, 2, 3, 1, 12), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hh3cNATServerRowStatus.setStatus('current')
hh3cNATTimeOutTable = MibTable((1, 3, 6, 1, 4, 1, 25506, 2, 18, 2, 4), )
if mibBuilder.loadTexts: hh3cNATTimeOutTable.setStatus('current')
hh3cNATTimeOutEntry = MibTableRow((1, 3, 6, 1, 4, 1, 25506, 2, 18, 2, 4, 1), ).setIndexNames((0, "HH3C-NAT-MIB", "hh3cNATTimeOutProtocol"))
if mibBuilder.loadTexts: hh3cNATTimeOutEntry.setStatus('current')
hh3cNATTimeOutProtocol = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 2, 18, 2, 4, 1, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 8, 9))).clone(namedValues=NamedValues(("tcp", 1), ("udp", 2), ("icmp", 3), ("pptp", 4), ("dns", 5), ("tcpFin", 6), ("tcpSyn", 7), ("ftpCtrl", 8), ("ftpData", 9))))
if mibBuilder.loadTexts: hh3cNATTimeOutProtocol.setStatus('current')
hh3cNATTimeOutTimeValue = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 2, 18, 2, 4, 1, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(10, 86400))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hh3cNATTimeOutTimeValue.setStatus('current')
hh3cNATBLEnableTable = MibTable((1, 3, 6, 1, 4, 1, 25506, 2, 18, 2, 5), )
if mibBuilder.loadTexts: hh3cNATBLEnableTable.setStatus('current')
hh3cNATBLEnableEntry = MibTableRow((1, 3, 6, 1, 4, 1, 25506, 2, 18, 2, 5, 1), ).setIndexNames((0, "HH3C-NAT-MIB", "hh3cNATBLEnableSlotNo"))
if mibBuilder.loadTexts: hh3cNATBLEnableEntry.setStatus('current')
hh3cNATBLEnableSlotNo = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 2, 18, 2, 5, 1, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(ValueRangeConstraint(1, 14), ValueRangeConstraint(255, 255), )))
if mibBuilder.loadTexts: hh3cNATBLEnableSlotNo.setStatus('current')
hh3cNATBLEnable = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 2, 18, 2, 5, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enable", 1), ("disable", 2))).clone('disable')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hh3cNATBLEnable.setStatus('current')
hh3cNATBLIPConnectLimitParaTable = MibTable((1, 3, 6, 1, 4, 1, 25506, 2, 18, 2, 6), )
if mibBuilder.loadTexts: hh3cNATBLIPConnectLimitParaTable.setStatus('current')
hh3cNATBLIPConnectLimitParaEntry = MibTableRow((1, 3, 6, 1, 4, 1, 25506, 2, 18, 2, 6, 1), ).setIndexNames((0, "HH3C-NAT-MIB", "hh3cNATBLIPConnectLimitParaIP"))
if mibBuilder.loadTexts: hh3cNATBLIPConnectLimitParaEntry.setStatus('current')
hh3cNATBLIPConnectLimitParaIP = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 2, 18, 2, 6, 1, 1), IpAddress())
if mibBuilder.loadTexts: hh3cNATBLIPConnectLimitParaIP.setStatus('current')
hh3cNATBLIPConnectHighValue = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 2, 18, 2, 6, 1, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(20, 20000)).clone(500)).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hh3cNATBLIPConnectHighValue.setStatus('current')
hh3cNATBLIPConnectLowValue = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 2, 18, 2, 6, 1, 3), Integer32().subtype(subtypeSpec=ValueRangeConstraint(20, 20000)).clone(200)).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hh3cNATBLIPConnectLowValue.setStatus('current')
hh3cNATBLIPUseSpecialConnectRate = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 2, 18, 2, 6, 1, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("true", 1), ("false", 2))).clone('false')).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hh3cNATBLIPUseSpecialConnectRate.setStatus('current')
hh3cNATBLIPConnectLimitRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 2, 18, 2, 6, 1, 5), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hh3cNATBLIPConnectLimitRowStatus.setStatus('current')
hh3cNATBLManagerTable = MibTable((1, 3, 6, 1, 4, 1, 25506, 2, 18, 2, 7), )
if mibBuilder.loadTexts: hh3cNATBLManagerTable.setStatus('current')
hh3cNATBLManagerEntry = MibTableRow((1, 3, 6, 1, 4, 1, 25506, 2, 18, 2, 7, 1), ).setIndexNames((0, "HH3C-NAT-MIB", "hh3cNATBLIpAdress"), (0, "HH3C-NAT-MIB", "hh3cNATBLSlotNo"))
if mibBuilder.loadTexts: hh3cNATBLManagerEntry.setStatus('current')
hh3cNATBLIpAdress = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 2, 18, 2, 7, 1, 1), IpAddress())
if mibBuilder.loadTexts: hh3cNATBLIpAdress.setStatus('current')
hh3cNATBLSlotNo = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 2, 18, 2, 7, 1, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 14)))
if mibBuilder.loadTexts: hh3cNATBLSlotNo.setStatus('current')
hh3cNATBLConSum = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 2, 18, 2, 7, 1, 3), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hh3cNATBLConSum.setStatus('current')
hh3cNATBLConSpd = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 2, 18, 2, 7, 1, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("red", 1), ("yellow", 2), ("green", 3)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: hh3cNATBLConSpd.setStatus('current')
hh3cNATStatTable = MibTable((1, 3, 6, 1, 4, 1, 25506, 2, 18, 2, 8), )
if mibBuilder.loadTexts: hh3cNATStatTable.setStatus('current')
hh3cNATStatEntry = MibTableRow((1, 3, 6, 1, 4, 1, 25506, 2, 18, 2, 8, 1), ).setIndexNames((0, "HH3C-NAT-MIB", "hh3cNATStatNATBoardNo"))
if mibBuilder.loadTexts: hh3cNATStatEntry.setStatus('current')
hh3cNATStatNATBoardNo = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 2, 18, 2, 8, 1, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(ValueRangeConstraint(1, 14), ValueRangeConstraint(255, 255), )))
if mibBuilder.loadTexts: hh3cNATStatNATBoardNo.setStatus('current')
hh3cNATStatActiveTblCount = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 2, 18, 2, 8, 1, 2), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hh3cNATStatActiveTblCount.setStatus('current')
hh3cNATStatActiveTblCountInNP = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 2, 18, 2, 8, 1, 3), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hh3cNATStatActiveTblCountInNP.setStatus('current')
hh3cNATStatActiveNatTblCount = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 2, 18, 2, 8, 1, 4), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hh3cNATStatActiveNatTblCount.setStatus('current')
hh3cNATStatActiveSvrTblCount = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 2, 18, 2, 8, 1, 5), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hh3cNATStatActiveSvrTblCount.setStatus('current')
hh3cNATStatActivePoolTblCount = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 2, 18, 2, 8, 1, 6), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hh3cNATStatActivePoolTblCount.setStatus('current')
hh3cNATStatNumOfUsedPort = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 2, 18, 2, 8, 1, 7), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hh3cNATStatNumOfUsedPort.setStatus('current')
hh3cNATStatNumOfGoodPkt = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 2, 18, 2, 8, 1, 8), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hh3cNATStatNumOfGoodPkt.setStatus('current')
hh3cNATStatNumOfBadPkt = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 2, 18, 2, 8, 1, 9), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hh3cNATStatNumOfBadPkt.setStatus('current')
hh3cNATStaticSessionCount = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 2, 18, 2, 8, 1, 10), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hh3cNATStaticSessionCount.setStatus('current')
hh3cNATFragmentSessionCount = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 2, 18, 2, 8, 1, 11), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hh3cNATFragmentSessionCount.setStatus('current')
hh3cNATSequenceSessionCount = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 2, 18, 2, 8, 1, 12), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hh3cNATSequenceSessionCount.setStatus('current')
hh3cNATLogCount = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 2, 18, 2, 8, 1, 13), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hh3cNATLogCount.setStatus('current')
hh3cNATSessionTable = MibTable((1, 3, 6, 1, 4, 1, 25506, 2, 18, 2, 9), )
if mibBuilder.loadTexts: hh3cNATSessionTable.setStatus('current')
hh3cNATSessionEntry = MibTableRow((1, 3, 6, 1, 4, 1, 25506, 2, 18, 2, 9, 1), ).setIndexNames((0, "HH3C-NAT-MIB", "hh3cNATSessionHashNumber"), (0, "HH3C-NAT-MIB", "hh3cNATSessionProtocol"), (0, "HH3C-NAT-MIB", "hh3cNATSessionInsideIP"), (0, "HH3C-NAT-MIB", "hh3cNATSessionInsidePort"), (0, "HH3C-NAT-MIB", "hh3cNATSessionPeerIP"), (0, "HH3C-NAT-MIB", "hh3cNATSessionPeerPort"), (0, "HH3C-NAT-MIB", "hh3cNATSessionVpnIndex"))
if mibBuilder.loadTexts: hh3cNATSessionEntry.setStatus('current')
hh3cNATSessionHashNumber = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 2, 18, 2, 9, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 300000)))
if mibBuilder.loadTexts: hh3cNATSessionHashNumber.setStatus('current')
hh3cNATSessionProtocol = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 2, 18, 2, 9, 1, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 255)))
if mibBuilder.loadTexts: hh3cNATSessionProtocol.setStatus('current')
hh3cNATSessionGlobalIP = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 2, 18, 2, 9, 1, 3), IpAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hh3cNATSessionGlobalIP.setStatus('current')
hh3cNATSessionGlobalPort = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 2, 18, 2, 9, 1, 4), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 65535))).setMaxAccess("readonly")
if mibBuilder.loadTexts: hh3cNATSessionGlobalPort.setStatus('current')
hh3cNATSessionInsideIP = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 2, 18, 2, 9, 1, 5), IpAddress())
if mibBuilder.loadTexts: hh3cNATSessionInsideIP.setStatus('current')
hh3cNATSessionInsidePort = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 2, 18, 2, 9, 1, 6), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 65535)))
if mibBuilder.loadTexts: hh3cNATSessionInsidePort.setStatus('current')
hh3cNATSessionPeerIP = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 2, 18, 2, 9, 1, 7), IpAddress())
if mibBuilder.loadTexts: hh3cNATSessionPeerIP.setStatus('current')
hh3cNATSessionPeerPort = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 2, 18, 2, 9, 1, 8), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 65535)))
if mibBuilder.loadTexts: hh3cNATSessionPeerPort.setStatus('current')
hh3cNATSessionVpnIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 2, 18, 2, 9, 1, 9), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 255)))
if mibBuilder.loadTexts: hh3cNATSessionVpnIndex.setStatus('current')
hh3cNATSessionTTL = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 2, 18, 2, 9, 1, 10), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hh3cNATSessionTTL.setStatus('current')
hh3cNATSessionStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 2, 18, 2, 9, 1, 11), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hh3cNATSessionStatus.setStatus('current')
hh3cNATSessionLeftTime = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 2, 18, 2, 9, 1, 12), TimeTicks()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hh3cNATSessionLeftTime.setStatus('current')
hh3cNATStaticConfTable = MibTable((1, 3, 6, 1, 4, 1, 25506, 2, 18, 2, 10), )
if mibBuilder.loadTexts: hh3cNATStaticConfTable.setStatus('current')
hh3cNATStaticConfEntry = MibTableRow((1, 3, 6, 1, 4, 1, 25506, 2, 18, 2, 10, 1), ).setIndexNames((0, "HH3C-NAT-MIB", "hh3cNATStaticInsideIp"))
if mibBuilder.loadTexts: hh3cNATStaticConfEntry.setStatus('current')
hh3cNATStaticInsideIp = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 2, 18, 2, 10, 1, 1), IpAddress())
if mibBuilder.loadTexts: hh3cNATStaticInsideIp.setStatus('current')
hh3cNATStaticGlobalIp = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 2, 18, 2, 10, 1, 2), IpAddress()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hh3cNATStaticGlobalIp.setStatus('current')
hh3cNATStaticRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 2, 18, 2, 10, 1, 3), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hh3cNATStaticRowStatus.setStatus('current')
hh3cNATStaticEnableTable = MibTable((1, 3, 6, 1, 4, 1, 25506, 2, 18, 2, 11), )
if mibBuilder.loadTexts: hh3cNATStaticEnableTable.setStatus('current')
hh3cNATStaticEnableEntry = MibTableRow((1, 3, 6, 1, 4, 1, 25506, 2, 18, 2, 11, 1), ).setIndexNames((0, "IF-MIB", "ifIndex"))
if mibBuilder.loadTexts: hh3cNATStaticEnableEntry.setStatus('current')
hh3cNATStaticEnable = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 2, 18, 2, 11, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1))).clone(namedValues=NamedValues(("disable", 0), ("enable", 1)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hh3cNATStaticEnable.setStatus('current')
hh3cNATDnsMapTable = MibTable((1, 3, 6, 1, 4, 1, 25506, 2, 18, 2, 12), )
if mibBuilder.loadTexts: hh3cNATDnsMapTable.setStatus('current')
hh3cNATDnsMapEntry = MibTableRow((1, 3, 6, 1, 4, 1, 25506, 2, 18, 2, 12, 1), ).setIndexNames((0, "HH3C-NAT-MIB", "hh3cNATDnsMapDomainName"))
if mibBuilder.loadTexts: hh3cNATDnsMapEntry.setStatus('current')
hh3cNATDnsMapDomainName = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 2, 18, 2, 12, 1, 1), DisplayString())
if mibBuilder.loadTexts: hh3cNATDnsMapDomainName.setStatus('current')
hh3cNATDnsMapGlobalIp = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 2, 18, 2, 12, 1, 2), IpAddress()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hh3cNATDnsMapGlobalIp.setStatus('current')
hh3cNATDnsMapGlobalPort = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 2, 18, 2, 12, 1, 3), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 65535))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hh3cNATDnsMapGlobalPort.setStatus('current')
hh3cNATDnsMapProtocolType = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 2, 18, 2, 12, 1, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1, 2))).clone(namedValues=NamedValues(("any", 0), ("typeTCP", 1), ("typeUDP", 2)))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hh3cNATDnsMapProtocolType.setStatus('current')
hh3cNATDnsMapLastUseTime = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 2, 18, 2, 12, 1, 5), TimeTicks()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hh3cNATDnsMapLastUseTime.setStatus('current')
hh3cNATDnsMapRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 2, 18, 2, 12, 1, 6), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hh3cNATDnsMapRowStatus.setStatus('current')
mibBuilder.exportSymbols("HH3C-NAT-MIB", hh3cNATSequenceSessionCount=hh3cNATSequenceSessionCount, hh3cNATDnsMapGlobalIp=hh3cNATDnsMapGlobalIp, hh3cNATDnsMapGlobalPort=hh3cNATDnsMapGlobalPort, hh3cNATDnsMapDomainName=hh3cNATDnsMapDomainName, hh3cNATDnsMapRowStatus=hh3cNATDnsMapRowStatus, hh3cNATBLConnectLimitPara=hh3cNATBLConnectLimitPara, hh3cNATBLEnableEntry=hh3cNATBLEnableEntry, hh3cNATBLConSpd=hh3cNATBLConSpd, hh3cNATStatNATBoardNo=hh3cNATStatNATBoardNo, hh3cNATOutboundSlotNo=hh3cNATOutboundSlotNo, hh3cNATOutboundIsNoPat=hh3cNATOutboundIsNoPat, hh3cNATStatActiveTblCount=hh3cNATStatActiveTblCount, hh3cNATStatNumOfGoodPkt=hh3cNATStatNumOfGoodPkt, hh3cNATStaticConfEntry=hh3cNATStaticConfEntry, hh3cNATSessionStatus=hh3cNATSessionStatus, hh3cNat=hh3cNat, hh3cNATStatTable=hh3cNATStatTable, hh3cNATBLConnectHighValue=hh3cNATBLConnectHighValue, hh3cNATServerProType=hh3cNATServerProType, hh3cNATPoolStartIpAddr=hh3cNATPoolStartIpAddr, hh3cNATTimeOutProtocol=hh3cNATTimeOutProtocol, hh3cNATStaticEnable=hh3cNATStaticEnable, hh3cNATNPAgingTime=hh3cNATNPAgingTime, hh3cNATBLSpecialConnectHighRate=hh3cNATBLSpecialConnectHighRate, hh3cNATStatActiveNatTblCount=hh3cNATStatActiveNatTblCount, hh3cNATNPTimer=hh3cNATNPTimer, hh3cNATSessionPeerPort=hh3cNATSessionPeerPort, hh3cNATStaticEnableTable=hh3cNATStaticEnableTable, hh3cNATStatActiveTblCountInNP=hh3cNATStatActiveTblCountInNP, hh3cNATServerGlobalIP=hh3cNATServerGlobalIP, hh3cNATSessionInsideIP=hh3cNATSessionInsideIP, hh3cNATBLManagerTable=hh3cNATBLManagerTable, hh3cNATTimeOutTimeValue=hh3cNATTimeOutTimeValue, hh3cNATServerEndGlobalPort=hh3cNATServerEndGlobalPort, hh3cNATBLIpAdress=hh3cNATBLIpAdress, hh3cNATStatActivePoolTblCount=hh3cNATStatActivePoolTblCount, hh3cNATOutboundEntry=hh3cNATOutboundEntry, hh3cNATPoolInfoEntry=hh3cNATPoolInfoEntry, hh3cNATSessionHashNumber=hh3cNATSessionHashNumber, hh3cNATStaticEnableEntry=hh3cNATStaticEnableEntry, hh3cNATServerEndInsideIP=hh3cNATServerEndInsideIP, hh3cNATTimeOutEntry=hh3cNATTimeOutEntry, hh3cNATBLSpecialConnectLowRate=hh3cNATBLSpecialConnectLowRate, hh3cNATBLIPConnectLimitParaIP=hh3cNATBLIPConnectLimitParaIP, hh3cNATPoolRefCounter=hh3cNATPoolRefCounter, hh3cNATServerInsidePort=hh3cNATServerInsidePort, hh3cNATPoolRowStatus=hh3cNATPoolRowStatus, hh3cNATBLManagerEntry=hh3cNATBLManagerEntry, hh3cNATBLIPConnectLowValue=hh3cNATBLIPConnectLowValue, hh3cNATBLIPConnectLimitParaEntry=hh3cNATBLIPConnectLimitParaEntry, hh3cNATStatNumOfUsedPort=hh3cNATStatNumOfUsedPort, hh3cNATBLEnable=hh3cNATBLEnable, hh3cNATPoolIdx=hh3cNATPoolIdx, hh3cNATBLCtrlEnable=hh3cNATBLCtrlEnable, hh3cNATSessionLeftTime=hh3cNATSessionLeftTime, hh3cNATPoolSlotNo=hh3cNATPoolSlotNo, hh3cNATBLSlotNo=hh3cNATBLSlotNo, hh3cNATOutboundPoolIdx=hh3cNATOutboundPoolIdx, hh3cNATMibObjects=hh3cNATMibObjects, hh3cNATServerTable=hh3cNATServerTable, hh3cNATBLConnectLowValue=hh3cNATBLConnectLowValue, hh3cNATBLEnableTable=hh3cNATBLEnableTable, hh3cNATBLConnectRateEnable=hh3cNATBLConnectRateEnable, hh3cNATBLIPConnectLimitRowStatus=hh3cNATBLIPConnectLimitRowStatus, hh3cNATStaticGlobalIp=hh3cNATStaticGlobalIp, hh3cNATBLEnableSlotNo=hh3cNATBLEnableSlotNo, hh3cNATStatActiveSvrTblCount=hh3cNATStatActiveSvrTblCount, hh3cNATPoolEndIpAddr=hh3cNATPoolEndIpAddr, hh3cNATSessionProtocol=hh3cNATSessionProtocol, hh3cNATStaticRowStatus=hh3cNATStaticRowStatus, hh3cNATDnsMapTable=hh3cNATDnsMapTable, hh3cNATPoolInfoTable=hh3cNATPoolInfoTable, hh3cNATServerSlotNo=hh3cNATServerSlotNo, hh3cNATOutboundTable=hh3cNATOutboundTable, hh3cNATBLIPUseSpecialConnectRate=hh3cNATBLIPUseSpecialConnectRate, hh3cNATStaticSessionCount=hh3cNATStaticSessionCount, hh3cNATDnsMapProtocolType=hh3cNATDnsMapProtocolType, hh3cNATServerVpnIndex=hh3cNATServerVpnIndex, hh3cNATStatEntry=hh3cNATStatEntry, hh3cNATFragmentSessionCount=hh3cNATFragmentSessionCount, hh3cNATServerStartGlobalPort=hh3cNATServerStartGlobalPort, PYSNMP_MODULE_ID=hh3cNat, hh3cNATSessionPeerIP=hh3cNATSessionPeerIP, hh3cNATBLConnectSumEnable=hh3cNATBLConnectSumEnable, hh3cNATStatNumOfBadPkt=hh3cNATStatNumOfBadPkt, hh3cNATSessionGlobalPort=hh3cNATSessionGlobalPort, hh3cNATSessionEntry=hh3cNATSessionEntry, hh3cNATSessionTable=hh3cNATSessionTable, hh3cNATOutboundAclNo=hh3cNATOutboundAclNo, hh3cNATBLIPConnectLimitParaTable=hh3cNATBLIPConnectLimitParaTable, hh3cNATSessionVpnIndex=hh3cNATSessionVpnIndex, hh3cNATServerRowStatus=hh3cNATServerRowStatus, hh3cNATSessionInsidePort=hh3cNATSessionInsidePort, hh3cNATStaticInsideIp=hh3cNATStaticInsideIp, hh3cNATLogCount=hh3cNATLogCount, hh3cNATGlobalVars=hh3cNATGlobalVars, hh3cNATOutboundRowStatus=hh3cNATOutboundRowStatus, hh3cNATClearSessionSlotNo=hh3cNATClearSessionSlotNo, hh3cNATSessionTTL=hh3cNATSessionTTL, hh3cNATServerEntry=hh3cNATServerEntry, hh3cNATDnsMapLastUseTime=hh3cNATDnsMapLastUseTime, hh3cNATBLConSum=hh3cNATBLConSum, hh3cNATBLIPConnectHighValue=hh3cNATBLIPConnectHighValue, hh3cNATClearSession=hh3cNATClearSession, hh3cNATTimeOutTable=hh3cNATTimeOutTable, hh3cNATBLConnectHighRate=hh3cNATBLConnectHighRate, hh3cNATServerStartInsideIP=hh3cNATServerStartInsideIP, hh3cNATServerAclNumber=hh3cNATServerAclNumber, hh3cNATDnsMapEntry=hh3cNATDnsMapEntry, hh3cNATSessionGlobalIP=hh3cNATSessionGlobalIP, hh3cNATStaticConfTable=hh3cNATStaticConfTable, hh3cNATBLConnectLowRate=hh3cNATBLConnectLowRate)