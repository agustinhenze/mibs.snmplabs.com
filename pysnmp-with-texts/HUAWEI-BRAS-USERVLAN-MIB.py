#
# PySNMP MIB module HUAWEI-BRAS-USERVLAN-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/HUAWEI-BRAS-USERVLAN-MIB
# Produced by pysmi-0.3.4 at Wed May  1 13:43:38 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
ObjectIdentifier, Integer, OctetString = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "Integer", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ValueRangeConstraint, ConstraintsUnion, ConstraintsIntersection, SingleValueConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ValueRangeConstraint", "ConstraintsUnion", "ConstraintsIntersection", "SingleValueConstraint")
hwBRASMib, = mibBuilder.importSymbols("HUAWEI-MIB", "hwBRASMib")
InterfaceIndex, ifIndex = mibBuilder.importSymbols("IF-MIB", "InterfaceIndex", "ifIndex")
VlanIdOrNone, VlanId = mibBuilder.importSymbols("Q-BRIDGE-MIB", "VlanIdOrNone", "VlanId")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
MibIdentifier, TimeTicks, NotificationType, Unsigned32, MibScalar, MibTable, MibTableRow, MibTableColumn, Bits, ObjectIdentity, Counter64, iso, IpAddress, Integer32, Counter32, Gauge32, ModuleIdentity = mibBuilder.importSymbols("SNMPv2-SMI", "MibIdentifier", "TimeTicks", "NotificationType", "Unsigned32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Bits", "ObjectIdentity", "Counter64", "iso", "IpAddress", "Integer32", "Counter32", "Gauge32", "ModuleIdentity")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
hwUSERVLAN = ModuleIdentity((1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 12))
if mibBuilder.loadTexts: hwUSERVLAN.setLastUpdated('200508101200Z')
if mibBuilder.loadTexts: hwUSERVLAN.setOrganization('Huawei Technologies Co., Ltd. ')
if mibBuilder.loadTexts: hwUSERVLAN.setContactInfo(' NanJing Institute,Huawei Technologies Co.,Ltd. HuiHong Mansion,No.91 BaiXia Rd. NanJing, P.R. of China Zipcode:210001 Http://www.huawei.com E-mail:support@huawei.com ')
if mibBuilder.loadTexts: hwUSERVLAN.setDescription(' The USERVLAN mib is for all datacomm product. ')
hwhwUSERVLANMibObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 12, 1))
hwUserVlanTable = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 12, 1, 1))
hwUserVlanIfIndex = MibScalar((1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 12, 1, 1, 1), InterfaceIndex()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hwUserVlanIfIndex.setStatus('current')
if mibBuilder.loadTexts: hwUserVlanIfIndex.setDescription('Interface Index(es).')
hwUserInnerStartVlan = MibScalar((1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 12, 1, 1, 2), VlanId()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hwUserInnerStartVlan.setStatus('current')
if mibBuilder.loadTexts: hwUserInnerStartVlan.setDescription("The start inner-vlan's of uservlan.")
hwUserInnerEndVlan = MibScalar((1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 12, 1, 1, 3), VlanId()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hwUserInnerEndVlan.setStatus('current')
if mibBuilder.loadTexts: hwUserInnerEndVlan.setDescription('The end inner-vlan of uservlan.')
hwUserVlanOuterVlan = MibScalar((1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 12, 1, 1, 4), VlanId()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hwUserVlanOuterVlan.setStatus('current')
if mibBuilder.loadTexts: hwUserVlanOuterVlan.setDescription('The outer-vlan of uservlan.')
hwUserVlanOpType = MibScalar((1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 12, 1, 1, 5), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("set", 1), ("undo", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hwUserVlanOpType.setStatus('current')
if mibBuilder.loadTexts: hwUserVlanOpType.setDescription(' 1 : set uservlan, 2 : undo userlvlan.')
hwQueryUserVlanTable = MibTable((1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 12, 1, 2), )
if mibBuilder.loadTexts: hwQueryUserVlanTable.setStatus('current')
hwQueryUserVlanEntry = MibTableRow((1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 12, 1, 2, 1), ).setIndexNames((0, "HUAWEI-BRAS-USERVLAN-MIB", "hwQueryUserVlanIfIndex"), (0, "HUAWEI-BRAS-USERVLAN-MIB", "hwQueryUserInnerVlan"), (0, "HUAWEI-BRAS-USERVLAN-MIB", "hwQueryUserOuterVlan"))
if mibBuilder.loadTexts: hwQueryUserVlanEntry.setStatus('current')
if mibBuilder.loadTexts: hwQueryUserVlanEntry.setDescription('Entry of hwQueryUserVlanTable.')
hwQueryUserVlanIfIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 12, 1, 2, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hwQueryUserVlanIfIndex.setStatus('current')
if mibBuilder.loadTexts: hwQueryUserVlanIfIndex.setDescription('Interface Index(es).')
hwQueryUserInnerVlan = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 12, 1, 2, 1, 2), VlanIdOrNone()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hwQueryUserInnerVlan.setStatus('current')
if mibBuilder.loadTexts: hwQueryUserInnerVlan.setDescription('The inner-vlan of uservlan.')
hwQueryUserOuterVlan = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 12, 1, 2, 1, 3), VlanIdOrNone()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hwQueryUserOuterVlan.setStatus('current')
if mibBuilder.loadTexts: hwQueryUserOuterVlan.setDescription('The outer-vlan of uservlan.')
hwUserVlanConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 12, 2))
hwUserVlanCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 12, 2, 1))
hwUserVlanCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 12, 2, 1, 1)).setObjects(("HUAWEI-BRAS-USERVLAN-MIB", "hwUserVlanTableGroup"), ("HUAWEI-BRAS-USERVLAN-MIB", "hwQueryUserVlanTableGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    hwUserVlanCompliance = hwUserVlanCompliance.setStatus('current')
if mibBuilder.loadTexts: hwUserVlanCompliance.setDescription('The compliance statement for systems supporting the this module.')
hwUserVlanObjectGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 12, 2, 1, 2))
hwUserVlanTableGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 12, 2, 1, 2, 1)).setObjects(("HUAWEI-BRAS-USERVLAN-MIB", "hwUserVlanIfIndex"), ("HUAWEI-BRAS-USERVLAN-MIB", "hwUserInnerStartVlan"), ("HUAWEI-BRAS-USERVLAN-MIB", "hwUserInnerEndVlan"), ("HUAWEI-BRAS-USERVLAN-MIB", "hwUserVlanOuterVlan"), ("HUAWEI-BRAS-USERVLAN-MIB", "hwUserVlanOpType"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    hwUserVlanTableGroup = hwUserVlanTableGroup.setStatus('current')
if mibBuilder.loadTexts: hwUserVlanTableGroup.setDescription('User vlan table.')
hwQueryUserVlanTableGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 12, 2, 1, 2, 2)).setObjects(("HUAWEI-BRAS-USERVLAN-MIB", "hwQueryUserVlanIfIndex"), ("HUAWEI-BRAS-USERVLAN-MIB", "hwQueryUserInnerVlan"), ("HUAWEI-BRAS-USERVLAN-MIB", "hwQueryUserOuterVlan"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    hwQueryUserVlanTableGroup = hwQueryUserVlanTableGroup.setStatus('current')
if mibBuilder.loadTexts: hwQueryUserVlanTableGroup.setDescription('Query user vlan table.')
mibBuilder.exportSymbols("HUAWEI-BRAS-USERVLAN-MIB", hwQueryUserVlanEntry=hwQueryUserVlanEntry, hwQueryUserVlanIfIndex=hwQueryUserVlanIfIndex, hwUserVlanCompliance=hwUserVlanCompliance, hwUserVlanConformance=hwUserVlanConformance, hwQueryUserVlanTable=hwQueryUserVlanTable, hwhwUSERVLANMibObjects=hwhwUSERVLANMibObjects, hwUserInnerEndVlan=hwUserInnerEndVlan, hwUserVlanIfIndex=hwUserVlanIfIndex, hwUserVlanObjectGroups=hwUserVlanObjectGroups, hwQueryUserInnerVlan=hwQueryUserInnerVlan, hwUserInnerStartVlan=hwUserInnerStartVlan, hwUserVlanTable=hwUserVlanTable, hwUserVlanOuterVlan=hwUserVlanOuterVlan, hwUSERVLAN=hwUSERVLAN, hwQueryUserVlanTableGroup=hwQueryUserVlanTableGroup, hwQueryUserOuterVlan=hwQueryUserOuterVlan, hwUserVlanOpType=hwUserVlanOpType, hwUserVlanTableGroup=hwUserVlanTableGroup, hwUserVlanCompliances=hwUserVlanCompliances, PYSNMP_MODULE_ID=hwUSERVLAN)