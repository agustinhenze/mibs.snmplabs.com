#
# PySNMP MIB module HUAWEI-SEP-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/HUAWEI-SEP-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 19:36:43 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
ObjectIdentifier, Integer, OctetString = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "Integer", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, SingleValueConstraint, ValueRangeConstraint, ConstraintsUnion, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "SingleValueConstraint", "ValueRangeConstraint", "ConstraintsUnion", "ConstraintsIntersection")
hwDatacomm, = mibBuilder.importSymbols("HUAWEI-MIB", "hwDatacomm")
MibScalar, MibTable, MibTableRow, MibTableColumn, ifName, InterfaceIndex, Integer32, ObjectIdentity, ModuleIdentity, Unsigned32 = mibBuilder.importSymbols("IF-MIB", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "ifName", "InterfaceIndex", "Integer32", "ObjectIdentity", "ModuleIdentity", "Unsigned32")
EnabledStatus, = mibBuilder.importSymbols("P-BRIDGE-MIB", "EnabledStatus")
VlanId, = mibBuilder.importSymbols("Q-BRIDGE-MIB", "VlanId")
ObjectGroup, NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "ObjectGroup", "NotificationGroup", "ModuleCompliance")
MibScalar, MibTable, MibTableRow, MibTableColumn, NotificationType, MibIdentifier, iso, Counter64, Counter32, Bits, IpAddress, Integer32, Gauge32, ModuleIdentity, ObjectIdentity, TimeTicks, Unsigned32 = mibBuilder.importSymbols("SNMPv2-SMI", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "NotificationType", "MibIdentifier", "iso", "Counter64", "Counter32", "Bits", "IpAddress", "Integer32", "Gauge32", "ModuleIdentity", "ObjectIdentity", "TimeTicks", "Unsigned32")
RowStatus, TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "RowStatus", "TextualConvention", "DisplayString")
hwSepMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 2011, 5, 25, 223))
if mibBuilder.loadTexts: hwSepMIB.setLastUpdated('200911171530Z')
if mibBuilder.loadTexts: hwSepMIB.setOrganization('Huawei Technologies Co.,Ltd.')
hwSepObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 5, 25, 223, 1))
hwSepResetPktCnt = MibScalar((1, 3, 6, 1, 4, 1, 2011, 5, 25, 223, 1, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 65535))).clone(namedValues=NamedValues(("clear", 1), ("unused", 65535)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hwSepResetPktCnt.setStatus('current')
hwSepSegmentTable = MibTable((1, 3, 6, 1, 4, 1, 2011, 5, 25, 223, 1, 2), )
if mibBuilder.loadTexts: hwSepSegmentTable.setStatus('current')
hwSepSegmentEntry = MibTableRow((1, 3, 6, 1, 4, 1, 2011, 5, 25, 223, 1, 2, 1), ).setIndexNames((0, "HUAWEI-SEP-MIB", "hwSepSegmentId"))
if mibBuilder.loadTexts: hwSepSegmentEntry.setStatus('current')
hwSepSegmentId = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 5, 25, 223, 1, 2, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 1024)))
if mibBuilder.loadTexts: hwSepSegmentId.setStatus('current')
hwSepControlVlanId = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 5, 25, 223, 1, 2, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(ValueRangeConstraint(0, 0), ValueRangeConstraint(1, 4094), ))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hwSepControlVlanId.setStatus('current')
hwSepPreemptManual = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 5, 25, 223, 1, 2, 1, 3), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 1))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hwSepPreemptManual.setStatus('current')
hwSepPreemptDelay = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 5, 25, 223, 1, 2, 1, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(ValueRangeConstraint(0, 0), ValueRangeConstraint(15, 600), ))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hwSepPreemptDelay.setStatus('current')
hwSepBlockPortMode = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 5, 25, 223, 1, 2, 1, 5), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5))).clone(namedValues=NamedValues(("optimal", 1), ("middle", 2), ("hop", 3), ("name", 4), ("null", 5)))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hwSepBlockPortMode.setStatus('current')
hwSepBlockPortHop = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 5, 25, 223, 1, 2, 1, 6), Integer32().subtype(subtypeSpec=ConstraintsUnion(ValueRangeConstraint(0, 0), ValueRangeConstraint(1, 512), ))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hwSepBlockPortHop.setStatus('current')
hwSepBlockPortSysname = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 5, 25, 223, 1, 2, 1, 7), OctetString().subtype(subtypeSpec=ValueSizeConstraint(0, 20))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hwSepBlockPortSysname.setStatus('current')
hwSepBlockPortIfname = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 5, 25, 223, 1, 2, 1, 8), OctetString().subtype(subtypeSpec=ValueSizeConstraint(0, 63))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hwSepBlockPortIfname.setStatus('current')
hwSepTcNotifySep = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 5, 25, 223, 1, 2, 1, 9), OctetString().subtype(subtypeSpec=ValueSizeConstraint(0, 129))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hwSepTcNotifySep.setStatus('current')
hwSepTcNotifyRrpp = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 5, 25, 223, 1, 2, 1, 10), EnabledStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hwSepTcNotifyRrpp.setStatus('current')
hwSepTcNotifyStp = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 5, 25, 223, 1, 2, 1, 11), EnabledStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hwSepTcNotifyStp.setStatus('current')
hwSepTcNotifyVpls = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 5, 25, 223, 1, 2, 1, 12), EnabledStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hwSepTcNotifyVpls.setStatus('current')
hwSepTcNotifyVll = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 5, 25, 223, 1, 2, 1, 13), EnabledStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hwSepTcNotifyVll.setStatus('current')
hwSepTcNotifySmartLinkCtrlVlan = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 5, 25, 223, 1, 2, 1, 14), Integer32().subtype(subtypeSpec=ConstraintsUnion(ValueRangeConstraint(0, 0), ValueRangeConstraint(1, 4094), ))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hwSepTcNotifySmartLinkCtrlVlan.setStatus('current')
hwSepDealSmartLinkFlush = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 5, 25, 223, 1, 2, 1, 15), EnabledStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hwSepDealSmartLinkFlush.setStatus('current')
hwSepProtectedInstanceList = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 5, 25, 223, 1, 2, 1, 16), OctetString().subtype(subtypeSpec=ValueSizeConstraint(0, 512))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hwSepProtectedInstanceList.setStatus('current')
hwSepTcProtectionInterval = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 5, 25, 223, 1, 2, 1, 17), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 10))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hwSepTcProtectionInterval.setStatus('current')
hwSepSegmentRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 5, 25, 223, 1, 2, 1, 128), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hwSepSegmentRowStatus.setStatus('current')
hwSepTopologyTable = MibTable((1, 3, 6, 1, 4, 1, 2011, 5, 25, 223, 1, 3), )
if mibBuilder.loadTexts: hwSepTopologyTable.setStatus('current')
hwSepTopologyEntry = MibTableRow((1, 3, 6, 1, 4, 1, 2011, 5, 25, 223, 1, 3, 1), ).setIndexNames((0, "HUAWEI-SEP-MIB", "hwSepSegmentId"), (0, "HUAWEI-SEP-MIB", "hwSepHop"))
if mibBuilder.loadTexts: hwSepTopologyEntry.setStatus('current')
hwSepHop = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 5, 25, 223, 1, 3, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 512)))
if mibBuilder.loadTexts: hwSepHop.setStatus('current')
hwSepPortId = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 5, 25, 223, 1, 3, 1, 2), OctetString().subtype(subtypeSpec=ValueSizeConstraint(0, 8))).setMaxAccess("readonly")
if mibBuilder.loadTexts: hwSepPortId.setStatus('current')
hwSepTopoSysname = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 5, 25, 223, 1, 3, 1, 3), OctetString().subtype(subtypeSpec=ValueSizeConstraint(0, 20))).setMaxAccess("readonly")
if mibBuilder.loadTexts: hwSepTopoSysname.setStatus('current')
hwSepTopoPortname = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 5, 25, 223, 1, 3, 1, 4), OctetString().subtype(subtypeSpec=ValueSizeConstraint(0, 16))).setMaxAccess("readonly")
if mibBuilder.loadTexts: hwSepTopoPortname.setStatus('current')
hwSepTopoPortConfigPriority = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 5, 25, 223, 1, 3, 1, 5), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 128))).setMaxAccess("readonly")
if mibBuilder.loadTexts: hwSepTopoPortConfigPriority.setStatus('current')
hwSepTopoPortActivePriority = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 5, 25, 223, 1, 3, 1, 6), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hwSepTopoPortActivePriority.setStatus('current')
hwSepTopoConfigPortRole = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 5, 25, 223, 1, 3, 1, 7), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hwSepTopoConfigPortRole.setStatus('current')
hwSepTopoActivePortRole = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 5, 25, 223, 1, 3, 1, 8), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hwSepTopoActivePortRole.setStatus('current')
hwSepTopoPortNbrState = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 5, 25, 223, 1, 3, 1, 9), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5))).clone(namedValues=NamedValues(("down", 1), ("init", 2), ("preup", 3), ("up", 4), ("conflict", 5)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: hwSepTopoPortNbrState.setStatus('current')
hwSepTopoBrotherPortId = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 5, 25, 223, 1, 3, 1, 10), OctetString().subtype(subtypeSpec=ValueSizeConstraint(0, 8))).setMaxAccess("readonly")
if mibBuilder.loadTexts: hwSepTopoBrotherPortId.setStatus('current')
hwSepTopoNbrPortId = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 5, 25, 223, 1, 3, 1, 11), OctetString().subtype(subtypeSpec=ValueSizeConstraint(0, 8))).setMaxAccess("readonly")
if mibBuilder.loadTexts: hwSepTopoNbrPortId.setStatus('current')
hwSepTopoPortLinkState = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 5, 25, 223, 1, 3, 1, 12), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("down", 1), ("up", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: hwSepTopoPortLinkState.setStatus('current')
hwSepTopoPortFwdState = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 5, 25, 223, 1, 3, 1, 13), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("discarding", 1), ("forwarding", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: hwSepTopoPortFwdState.setStatus('current')
hwSepPortTable = MibTable((1, 3, 6, 1, 4, 1, 2011, 5, 25, 223, 1, 4), )
if mibBuilder.loadTexts: hwSepPortTable.setStatus('current')
hwSepPortEntry = MibTableRow((1, 3, 6, 1, 4, 1, 2011, 5, 25, 223, 1, 4, 1), ).setIndexNames((0, "HUAWEI-SEP-MIB", "hwSepSegmentId"), (0, "HUAWEI-SEP-MIB", "hwSepPortType"), (0, "HUAWEI-SEP-MIB", "hwSepPortId1"), (0, "HUAWEI-SEP-MIB", "hwSepPortId2"), (0, "HUAWEI-SEP-MIB", "hwSepPortId3"), (0, "HUAWEI-SEP-MIB", "hwSepPortId4"))
if mibBuilder.loadTexts: hwSepPortEntry.setStatus('current')
hwSepPortType = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 5, 25, 223, 1, 4, 1, 1), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(1, 1)))
if mibBuilder.loadTexts: hwSepPortType.setStatus('current')
hwSepPortId1 = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 5, 25, 223, 1, 4, 1, 2), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(0, 2147483647)))
if mibBuilder.loadTexts: hwSepPortId1.setStatus('current')
hwSepPortId2 = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 5, 25, 223, 1, 4, 1, 3), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(0, 2147483647)))
if mibBuilder.loadTexts: hwSepPortId2.setStatus('current')
hwSepPortId3 = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 5, 25, 223, 1, 4, 1, 4), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(0, 2147483647)))
if mibBuilder.loadTexts: hwSepPortId3.setStatus('current')
hwSepPortId4 = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 5, 25, 223, 1, 4, 1, 5), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(0, 2147483647)))
if mibBuilder.loadTexts: hwSepPortId4.setStatus('current')
hwSepSysname = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 5, 25, 223, 1, 4, 1, 6), OctetString().subtype(subtypeSpec=ValueSizeConstraint(0, 20))).setMaxAccess("readonly")
if mibBuilder.loadTexts: hwSepSysname.setStatus('current')
hwSepPortname = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 5, 25, 223, 1, 4, 1, 7), OctetString().subtype(subtypeSpec=ValueSizeConstraint(0, 16))).setMaxAccess("readonly")
if mibBuilder.loadTexts: hwSepPortname.setStatus('current')
hwSepPortConfigPriority = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 5, 25, 223, 1, 4, 1, 8), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 128))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hwSepPortConfigPriority.setStatus('current')
hwSepPortActivePriority = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 5, 25, 223, 1, 4, 1, 9), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hwSepPortActivePriority.setStatus('current')
hwSepConfigPortRole = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 5, 25, 223, 1, 4, 1, 10), Integer32()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hwSepConfigPortRole.setStatus('current')
hwSepActivePortRole = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 5, 25, 223, 1, 4, 1, 11), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hwSepActivePortRole.setStatus('current')
hwSepPortNbrState = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 5, 25, 223, 1, 4, 1, 12), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5))).clone(namedValues=NamedValues(("down", 1), ("init", 2), ("preup", 3), ("up", 4), ("conflict", 5)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: hwSepPortNbrState.setStatus('current')
hwSepNbrPortId = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 5, 25, 223, 1, 4, 1, 13), OctetString().subtype(subtypeSpec=ValueSizeConstraint(0, 8))).setMaxAccess("readonly")
if mibBuilder.loadTexts: hwSepNbrPortId.setStatus('current')
hwSepPortFwdState = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 5, 25, 223, 1, 4, 1, 14), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("discarding", 1), ("forwarding", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: hwSepPortFwdState.setStatus('current')
hwSepRxNbrPktCnt = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 5, 25, 223, 1, 4, 1, 15), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hwSepRxNbrPktCnt.setStatus('current')
hwSepTxNbrPktCnt = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 5, 25, 223, 1, 4, 1, 16), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hwSepTxNbrPktCnt.setStatus('current')
hwSepRxLsaInfoPktCnt = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 5, 25, 223, 1, 4, 1, 17), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hwSepRxLsaInfoPktCnt.setStatus('current')
hwSepTxLsaInfoPktCnt = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 5, 25, 223, 1, 4, 1, 18), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hwSepTxLsaInfoPktCnt.setStatus('current')
hwSepRxLsaAckPktCnt = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 5, 25, 223, 1, 4, 1, 19), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hwSepRxLsaAckPktCnt.setStatus('current')
hwSepTxLsaAckPktCnt = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 5, 25, 223, 1, 4, 1, 20), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hwSepTxLsaAckPktCnt.setStatus('current')
hwSepRxPreemptReqPktCnt = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 5, 25, 223, 1, 4, 1, 21), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hwSepRxPreemptReqPktCnt.setStatus('current')
hwSepTxPreemptReqPktCnt = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 5, 25, 223, 1, 4, 1, 22), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hwSepTxPreemptReqPktCnt.setStatus('current')
hwSepRxPreemptAckPktCnt = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 5, 25, 223, 1, 4, 1, 23), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hwSepRxPreemptAckPktCnt.setStatus('current')
hwSepTxPreemptAckPktCnt = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 5, 25, 223, 1, 4, 1, 24), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hwSepTxPreemptAckPktCnt.setStatus('current')
hwSepRxTcPktCnt = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 5, 25, 223, 1, 4, 1, 25), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hwSepRxTcPktCnt.setStatus('current')
hwSepTxTcPktCnt = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 5, 25, 223, 1, 4, 1, 26), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hwSepTxTcPktCnt.setStatus('current')
hwSepRxEpaPktCnt = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 5, 25, 223, 1, 4, 1, 27), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hwSepRxEpaPktCnt.setStatus('current')
hwSepTxEpaPktCnt = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 5, 25, 223, 1, 4, 1, 28), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hwSepTxEpaPktCnt.setStatus('current')
hwSepResetPortPktCnt = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 5, 25, 223, 1, 4, 1, 29), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 65535))).clone(namedValues=NamedValues(("clear", 1), ("unused", 65535)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hwSepResetPortPktCnt.setStatus('current')
hwSepPortRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 5, 25, 223, 1, 4, 1, 128), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hwSepPortRowStatus.setStatus('current')
hwSepGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 5, 25, 223, 2))
hwSepGlobalInfoGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 2011, 5, 25, 223, 2, 1)).setObjects(("HUAWEI-SEP-MIB", "hwSepResetPktCnt"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    hwSepGlobalInfoGroup = hwSepGlobalInfoGroup.setStatus('current')
hwSepSegmentInfoGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 2011, 5, 25, 223, 2, 2)).setObjects(("HUAWEI-SEP-MIB", "hwSepSegmentId"), ("HUAWEI-SEP-MIB", "hwSepControlVlanId"), ("HUAWEI-SEP-MIB", "hwSepPreemptManual"), ("HUAWEI-SEP-MIB", "hwSepPreemptDelay"), ("HUAWEI-SEP-MIB", "hwSepBlockPortMode"), ("HUAWEI-SEP-MIB", "hwSepBlockPortHop"), ("HUAWEI-SEP-MIB", "hwSepBlockPortSysname"), ("HUAWEI-SEP-MIB", "hwSepBlockPortIfname"), ("HUAWEI-SEP-MIB", "hwSepTcNotifySep"), ("HUAWEI-SEP-MIB", "hwSepTcNotifyRrpp"), ("HUAWEI-SEP-MIB", "hwSepTcNotifyStp"), ("HUAWEI-SEP-MIB", "hwSepTcNotifyVpls"), ("HUAWEI-SEP-MIB", "hwSepTcNotifyVll"), ("HUAWEI-SEP-MIB", "hwSepTcNotifySmartLinkCtrlVlan"), ("HUAWEI-SEP-MIB", "hwSepDealSmartLinkFlush"), ("HUAWEI-SEP-MIB", "hwSepProtectedInstanceList"), ("HUAWEI-SEP-MIB", "hwSepTcProtectionInterval"), ("HUAWEI-SEP-MIB", "hwSepSegmentRowStatus"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    hwSepSegmentInfoGroup = hwSepSegmentInfoGroup.setStatus('current')
hwSepPortInfoGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 2011, 5, 25, 223, 2, 3)).setObjects(("HUAWEI-SEP-MIB", "hwSepPortType"), ("HUAWEI-SEP-MIB", "hwSepPortId1"), ("HUAWEI-SEP-MIB", "hwSepPortId2"), ("HUAWEI-SEP-MIB", "hwSepPortId3"), ("HUAWEI-SEP-MIB", "hwSepPortId4"), ("HUAWEI-SEP-MIB", "hwSepSysname"), ("HUAWEI-SEP-MIB", "hwSepPortname"), ("HUAWEI-SEP-MIB", "hwSepPortConfigPriority"), ("HUAWEI-SEP-MIB", "hwSepPortActivePriority"), ("HUAWEI-SEP-MIB", "hwSepConfigPortRole"), ("HUAWEI-SEP-MIB", "hwSepActivePortRole"), ("HUAWEI-SEP-MIB", "hwSepPortNbrState"), ("HUAWEI-SEP-MIB", "hwSepNbrPortId"), ("HUAWEI-SEP-MIB", "hwSepPortFwdState"), ("HUAWEI-SEP-MIB", "hwSepRxNbrPktCnt"), ("HUAWEI-SEP-MIB", "hwSepTxNbrPktCnt"), ("HUAWEI-SEP-MIB", "hwSepRxLsaInfoPktCnt"), ("HUAWEI-SEP-MIB", "hwSepTxLsaInfoPktCnt"), ("HUAWEI-SEP-MIB", "hwSepRxLsaAckPktCnt"), ("HUAWEI-SEP-MIB", "hwSepTxLsaAckPktCnt"), ("HUAWEI-SEP-MIB", "hwSepRxPreemptReqPktCnt"), ("HUAWEI-SEP-MIB", "hwSepTxPreemptReqPktCnt"), ("HUAWEI-SEP-MIB", "hwSepRxPreemptAckPktCnt"), ("HUAWEI-SEP-MIB", "hwSepTxPreemptAckPktCnt"), ("HUAWEI-SEP-MIB", "hwSepRxTcPktCnt"), ("HUAWEI-SEP-MIB", "hwSepTxTcPktCnt"), ("HUAWEI-SEP-MIB", "hwSepRxEpaPktCnt"), ("HUAWEI-SEP-MIB", "hwSepTxEpaPktCnt"), ("HUAWEI-SEP-MIB", "hwSepResetPortPktCnt"), ("HUAWEI-SEP-MIB", "hwSepPortRowStatus"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    hwSepPortInfoGroup = hwSepPortInfoGroup.setStatus('current')
hwSepTopologyInfoGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 2011, 5, 25, 223, 2, 4)).setObjects(("HUAWEI-SEP-MIB", "hwSepHop"), ("HUAWEI-SEP-MIB", "hwSepPortId"), ("HUAWEI-SEP-MIB", "hwSepTopoSysname"), ("HUAWEI-SEP-MIB", "hwSepTopoPortname"), ("HUAWEI-SEP-MIB", "hwSepTopoPortConfigPriority"), ("HUAWEI-SEP-MIB", "hwSepTopoPortActivePriority"), ("HUAWEI-SEP-MIB", "hwSepTopoConfigPortRole"), ("HUAWEI-SEP-MIB", "hwSepTopoActivePortRole"), ("HUAWEI-SEP-MIB", "hwSepTopoPortNbrState"), ("HUAWEI-SEP-MIB", "hwSepTopoNbrPortId"), ("HUAWEI-SEP-MIB", "hwSepTopoPortLinkState"), ("HUAWEI-SEP-MIB", "hwSepTopoPortFwdState"), ("HUAWEI-SEP-MIB", "hwSepTopoBrotherPortId"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    hwSepTopologyInfoGroup = hwSepTopologyInfoGroup.setStatus('current')
mibBuilder.exportSymbols("HUAWEI-SEP-MIB", hwSepTcNotifySep=hwSepTcNotifySep, hwSepPortname=hwSepPortname, hwSepSegmentTable=hwSepSegmentTable, hwSepMIB=hwSepMIB, hwSepTopoPortname=hwSepTopoPortname, hwSepTxTcPktCnt=hwSepTxTcPktCnt, hwSepGroups=hwSepGroups, hwSepPortId2=hwSepPortId2, hwSepTopoConfigPortRole=hwSepTopoConfigPortRole, hwSepRxLsaAckPktCnt=hwSepRxLsaAckPktCnt, hwSepActivePortRole=hwSepActivePortRole, hwSepPortRowStatus=hwSepPortRowStatus, hwSepTopoSysname=hwSepTopoSysname, hwSepTopoPortNbrState=hwSepTopoPortNbrState, hwSepPortId3=hwSepPortId3, hwSepPortNbrState=hwSepPortNbrState, hwSepPortType=hwSepPortType, hwSepTopologyTable=hwSepTopologyTable, hwSepSegmentId=hwSepSegmentId, hwSepRxTcPktCnt=hwSepRxTcPktCnt, hwSepBlockPortMode=hwSepBlockPortMode, hwSepBlockPortIfname=hwSepBlockPortIfname, hwSepPortTable=hwSepPortTable, hwSepConfigPortRole=hwSepConfigPortRole, hwSepHop=hwSepHop, hwSepRxPreemptReqPktCnt=hwSepRxPreemptReqPktCnt, hwSepSysname=hwSepSysname, hwSepTxPreemptAckPktCnt=hwSepTxPreemptAckPktCnt, hwSepProtectedInstanceList=hwSepProtectedInstanceList, hwSepTxEpaPktCnt=hwSepTxEpaPktCnt, hwSepTopologyEntry=hwSepTopologyEntry, hwSepTopoPortActivePriority=hwSepTopoPortActivePriority, hwSepTxLsaInfoPktCnt=hwSepTxLsaInfoPktCnt, hwSepGlobalInfoGroup=hwSepGlobalInfoGroup, hwSepRxEpaPktCnt=hwSepRxEpaPktCnt, hwSepPortEntry=hwSepPortEntry, hwSepTopoPortConfigPriority=hwSepTopoPortConfigPriority, hwSepSegmentInfoGroup=hwSepSegmentInfoGroup, hwSepTopoBrotherPortId=hwSepTopoBrotherPortId, hwSepPortFwdState=hwSepPortFwdState, hwSepTxNbrPktCnt=hwSepTxNbrPktCnt, hwSepResetPktCnt=hwSepResetPktCnt, hwSepSegmentEntry=hwSepSegmentEntry, hwSepDealSmartLinkFlush=hwSepDealSmartLinkFlush, hwSepTcProtectionInterval=hwSepTcProtectionInterval, hwSepNbrPortId=hwSepNbrPortId, hwSepRxPreemptAckPktCnt=hwSepRxPreemptAckPktCnt, hwSepResetPortPktCnt=hwSepResetPortPktCnt, hwSepPreemptManual=hwSepPreemptManual, hwSepPortId4=hwSepPortId4, hwSepTcNotifyVll=hwSepTcNotifyVll, hwSepTopoActivePortRole=hwSepTopoActivePortRole, hwSepPreemptDelay=hwSepPreemptDelay, hwSepPortActivePriority=hwSepPortActivePriority, hwSepTcNotifySmartLinkCtrlVlan=hwSepTcNotifySmartLinkCtrlVlan, hwSepTcNotifyVpls=hwSepTcNotifyVpls, hwSepBlockPortSysname=hwSepBlockPortSysname, hwSepPortConfigPriority=hwSepPortConfigPriority, hwSepPortInfoGroup=hwSepPortInfoGroup, hwSepTopologyInfoGroup=hwSepTopologyInfoGroup, hwSepControlVlanId=hwSepControlVlanId, hwSepObjects=hwSepObjects, hwSepTcNotifyStp=hwSepTcNotifyStp, hwSepPortId=hwSepPortId, hwSepTopoNbrPortId=hwSepTopoNbrPortId, hwSepTxLsaAckPktCnt=hwSepTxLsaAckPktCnt, hwSepTopoPortFwdState=hwSepTopoPortFwdState, hwSepRxLsaInfoPktCnt=hwSepRxLsaInfoPktCnt, hwSepPortId1=hwSepPortId1, hwSepRxNbrPktCnt=hwSepRxNbrPktCnt, PYSNMP_MODULE_ID=hwSepMIB, hwSepBlockPortHop=hwSepBlockPortHop, hwSepTcNotifyRrpp=hwSepTcNotifyRrpp, hwSepSegmentRowStatus=hwSepSegmentRowStatus, hwSepTopoPortLinkState=hwSepTopoPortLinkState, hwSepTxPreemptReqPktCnt=hwSepTxPreemptReqPktCnt)