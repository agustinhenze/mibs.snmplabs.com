#
# PySNMP MIB module A3COM-HUAWEI-MPLS-BGP-VPN-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/A3COM-HUAWEI-MPLS-BGP-VPN-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 16:51:26 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
huaweiMgmt, hwMpls = mibBuilder.importSymbols("A3COM-HUAWEI-OID-MIB", "huaweiMgmt", "hwMpls")
Integer, OctetString, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "Integer", "OctetString", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, SingleValueConstraint, ConstraintsUnion, ValueRangeConstraint, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "SingleValueConstraint", "ConstraintsUnion", "ValueRangeConstraint", "ValueSizeConstraint")
InterfaceIndex, = mibBuilder.importSymbols("IF-MIB", "InterfaceIndex")
InetAddress, InetAddressType = mibBuilder.importSymbols("INET-ADDRESS-MIB", "InetAddress", "InetAddressType")
SnmpAdminString, = mibBuilder.importSymbols("SNMP-FRAMEWORK-MIB", "SnmpAdminString")
ModuleCompliance, NotificationGroup, ObjectGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup", "ObjectGroup")
ObjectIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter32, Unsigned32, TimeTicks, experimental, iso, MibIdentifier, ModuleIdentity, Gauge32, NotificationType, Bits, IpAddress, Integer32, Counter64 = mibBuilder.importSymbols("SNMPv2-SMI", "ObjectIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter32", "Unsigned32", "TimeTicks", "experimental", "iso", "MibIdentifier", "ModuleIdentity", "Gauge32", "NotificationType", "Bits", "IpAddress", "Integer32", "Counter64")
DisplayString, StorageType, RowStatus, TruthValue, TextualConvention, TimeStamp = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "StorageType", "RowStatus", "TruthValue", "TextualConvention", "TimeStamp")
hwMplsVpn = ModuleIdentity((1, 3, 6, 1, 4, 1, 43, 45, 1, 5, 12, 3))
hwMplsVpn.setRevisions(('2001-07-20 12:00', '2001-07-17 12:00', '2001-07-10 12:00', '2001-06-19 12:00', '2001-05-30 12:00', '2000-09-30 12:00',))
if mibBuilder.loadTexts: hwMplsVpn.setLastUpdated('200107201200Z')
if mibBuilder.loadTexts: hwMplsVpn.setOrganization('IETF Layer-3 Virtual Private Networks Working Group.')
class MplsVpnId(TextualConvention, OctetString):
    reference = "RFC 2685 [VPN-RFC2685] Fox B., et al, 'Virtual Private Networks Identifier', September 1999."
    status = 'current'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(0, 31)

class MplsVpnRouteDistinguisher(TextualConvention, OctetString):
    status = 'current'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(0, 256)

mplsVpnObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 43, 45, 1, 5, 12, 3, 1))
mplsVpnScalars = MibIdentifier((1, 3, 6, 1, 4, 1, 43, 45, 1, 5, 12, 3, 1, 1))
mplsVpnConf = MibIdentifier((1, 3, 6, 1, 4, 1, 43, 45, 1, 5, 12, 3, 1, 2))
mplsVpnRoute = MibIdentifier((1, 3, 6, 1, 4, 1, 43, 45, 1, 5, 12, 3, 1, 3))
mplsVpnConfiguredVrfs = MibScalar((1, 3, 6, 1, 4, 1, 43, 45, 1, 5, 12, 3, 1, 1, 1), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mplsVpnConfiguredVrfs.setStatus('current')
mplsVpnActiveVrfs = MibScalar((1, 3, 6, 1, 4, 1, 43, 45, 1, 5, 12, 3, 1, 1, 2), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mplsVpnActiveVrfs.setStatus('current')
mplsVpnInterfaceConfTable = MibTable((1, 3, 6, 1, 4, 1, 43, 45, 1, 5, 12, 3, 1, 2, 1), )
if mibBuilder.loadTexts: mplsVpnInterfaceConfTable.setStatus('current')
mplsVpnInterfaceConfEntry = MibTableRow((1, 3, 6, 1, 4, 1, 43, 45, 1, 5, 12, 3, 1, 2, 1, 1), ).setIndexNames((0, "A3COM-HUAWEI-MPLS-BGP-VPN-MIB", "mplsVpnVrfName"), (0, "A3COM-HUAWEI-MPLS-BGP-VPN-MIB", "mplsVpnInterfaceConfIndex"))
if mibBuilder.loadTexts: mplsVpnInterfaceConfEntry.setStatus('current')
mplsVpnInterfaceConfIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 45, 1, 5, 12, 3, 1, 2, 1, 1, 1), InterfaceIndex()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mplsVpnInterfaceConfIndex.setStatus('current')
mplsVpnInterfaceLabelEdgeType = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 45, 1, 5, 12, 3, 1, 2, 1, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("providerEdge", 1), ("customerEdge", 2))).clone('providerEdge')).setMaxAccess("readonly")
if mibBuilder.loadTexts: mplsVpnInterfaceLabelEdgeType.setStatus('current')
mplsVpnInterfaceVpnClassification = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 45, 1, 5, 12, 3, 1, 2, 1, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("carrierOfCarrier", 1), ("enterprise", 2), ("interProvider", 3)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: mplsVpnInterfaceVpnClassification.setStatus('current')
mplsVpnInterfaceIpAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 45, 1, 5, 12, 3, 1, 2, 1, 1, 4), InetAddress()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: mplsVpnInterfaceIpAddress.setStatus('current')
mplsVpnInterfaceIpAddressMask = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 45, 1, 5, 12, 3, 1, 2, 1, 1, 5), InetAddress()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: mplsVpnInterfaceIpAddressMask.setStatus('current')
mplsVpnInterfaceConfRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 45, 1, 5, 12, 3, 1, 2, 1, 1, 6), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: mplsVpnInterfaceConfRowStatus.setStatus('current')
mplsVpnVrfConfTable = MibTable((1, 3, 6, 1, 4, 1, 43, 45, 1, 5, 12, 3, 1, 2, 2), )
if mibBuilder.loadTexts: mplsVpnVrfConfTable.setStatus('current')
mplsVpnVrfConfEntry = MibTableRow((1, 3, 6, 1, 4, 1, 43, 45, 1, 5, 12, 3, 1, 2, 2, 1), ).setIndexNames((0, "A3COM-HUAWEI-MPLS-BGP-VPN-MIB", "mplsVpnVrfName"))
if mibBuilder.loadTexts: mplsVpnVrfConfEntry.setStatus('current')
mplsVpnVrfName = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 45, 1, 5, 12, 3, 1, 2, 2, 1, 1), MplsVpnId()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mplsVpnVrfName.setStatus('current')
mplsVpnVrfRouteDistinguisher = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 45, 1, 5, 12, 3, 1, 2, 2, 1, 2), MplsVpnRouteDistinguisher()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: mplsVpnVrfRouteDistinguisher.setStatus('current')
mplsVpnVrfNetPrefixType = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 45, 1, 5, 12, 3, 1, 2, 2, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6))).clone(namedValues=NamedValues(("other", 1), ("rip", 2), ("ospf", 3), ("isis", 4), ("bgp", 5), ("static", 6)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: mplsVpnVrfNetPrefixType.setStatus('current')
mplsVpnVrfNetPrefix = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 45, 1, 5, 12, 3, 1, 2, 2, 1, 4), InetAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mplsVpnVrfNetPrefix.setStatus('current')
mplsVpnVrfIpRouteRedistributeConn = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 45, 1, 5, 12, 3, 1, 2, 2, 1, 5), TruthValue()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: mplsVpnVrfIpRouteRedistributeConn.setStatus('current')
mplsVpnVrfIpRouteRedistributeStatic = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 45, 1, 5, 12, 3, 1, 2, 2, 1, 6), TruthValue()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: mplsVpnVrfIpRouteRedistributeStatic.setStatus('current')
mplsVpnVrfIpRouteRedistributeRip = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 45, 1, 5, 12, 3, 1, 2, 2, 1, 7), TruthValue()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: mplsVpnVrfIpRouteRedistributeRip.setStatus('current')
mplsVpnVrfConfHighRouteThreshold = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 45, 1, 5, 12, 3, 1, 2, 2, 1, 8), Unsigned32()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: mplsVpnVrfConfHighRouteThreshold.setStatus('current')
mplsVpnVrfConfIsWarnOnly = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 45, 1, 5, 12, 3, 1, 2, 2, 1, 9), TruthValue()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: mplsVpnVrfConfIsWarnOnly.setStatus('current')
mplsVpnVrfConfMaxRoutes = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 45, 1, 5, 12, 3, 1, 2, 2, 1, 10), Unsigned32()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: mplsVpnVrfConfMaxRoutes.setStatus('current')
mplsVpnVrfConfRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 45, 1, 5, 12, 3, 1, 2, 2, 1, 11), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: mplsVpnVrfConfRowStatus.setStatus('current')
mplsVpnVrfRouteTargetTable = MibTable((1, 3, 6, 1, 4, 1, 43, 45, 1, 5, 12, 3, 1, 2, 3), )
if mibBuilder.loadTexts: mplsVpnVrfRouteTargetTable.setStatus('current')
mplsVpnVrfRouteTargetEntry = MibTableRow((1, 3, 6, 1, 4, 1, 43, 45, 1, 5, 12, 3, 1, 2, 3, 1), ).setIndexNames((0, "A3COM-HUAWEI-MPLS-BGP-VPN-MIB", "mplsVpnVrfName"), (0, "A3COM-HUAWEI-MPLS-BGP-VPN-MIB", "mplsVpnVrfRouteTarget"), (0, "A3COM-HUAWEI-MPLS-BGP-VPN-MIB", "mplsVpnVrfRouteTargetType"))
if mibBuilder.loadTexts: mplsVpnVrfRouteTargetEntry.setStatus('current')
mplsVpnVrfRouteTarget = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 45, 1, 5, 12, 3, 1, 2, 3, 1, 1), MplsVpnRouteDistinguisher()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mplsVpnVrfRouteTarget.setStatus('current')
mplsVpnVrfRouteTargetType = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 45, 1, 5, 12, 3, 1, 2, 3, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("import", 1), ("export", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: mplsVpnVrfRouteTargetType.setStatus('current')
mplsVpnVrfRouteTargetRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 45, 1, 5, 12, 3, 1, 2, 3, 1, 3), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: mplsVpnVrfRouteTargetRowStatus.setStatus('current')
mplsVpnVrfBgpNbrAddrTable = MibTable((1, 3, 6, 1, 4, 1, 43, 45, 1, 5, 12, 3, 1, 2, 4), )
if mibBuilder.loadTexts: mplsVpnVrfBgpNbrAddrTable.setStatus('current')
mplsVpnVrfBgpNbrAddrEntry = MibTableRow((1, 3, 6, 1, 4, 1, 43, 45, 1, 5, 12, 3, 1, 2, 4, 1), ).setIndexNames((0, "A3COM-HUAWEI-MPLS-BGP-VPN-MIB", "mplsVpnVrfName"), (0, "A3COM-HUAWEI-MPLS-BGP-VPN-MIB", "mplsVpnVrfBgpNbrAddr"))
if mibBuilder.loadTexts: mplsVpnVrfBgpNbrAddrEntry.setStatus('current')
mplsVpnVrfBgpNbrAddr = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 45, 1, 5, 12, 3, 1, 2, 4, 1, 1), InetAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mplsVpnVrfBgpNbrAddr.setStatus('current')
mplsVpnVrfBgpNbrRole = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 45, 1, 5, 12, 3, 1, 2, 4, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("ce", 1), ("pe", 2)))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: mplsVpnVrfBgpNbrRole.setStatus('current')
mplsVpnVrfBgpNbrType = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 45, 1, 5, 12, 3, 1, 2, 4, 1, 3), InetAddressType()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: mplsVpnVrfBgpNbrType.setStatus('current')
mplsVpnVrfBgpNbrAsNumber = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 45, 1, 5, 12, 3, 1, 2, 4, 1, 4), Unsigned32()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: mplsVpnVrfBgpNbrAsNumber.setStatus('current')
mplsVpnVrfBgpNbrAdminStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 45, 1, 5, 12, 3, 1, 2, 4, 1, 5), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("mplsVpnVrfBgpNbrSetUp", 1), ("mplsVpnVrfBgpNbrSetDown", 2)))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: mplsVpnVrfBgpNbrAdminStatus.setStatus('current')
mplsVpnVrfBgpNbrRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 45, 1, 5, 12, 3, 1, 2, 4, 1, 6), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: mplsVpnVrfBgpNbrRowStatus.setStatus('current')
mplsVpnVrfRouteTable = MibTable((1, 3, 6, 1, 4, 1, 43, 45, 1, 5, 12, 3, 1, 3, 1), )
if mibBuilder.loadTexts: mplsVpnVrfRouteTable.setStatus('current')
mplsVpnVrfRouteEntry = MibTableRow((1, 3, 6, 1, 4, 1, 43, 45, 1, 5, 12, 3, 1, 3, 1, 1), ).setIndexNames((0, "A3COM-HUAWEI-MPLS-BGP-VPN-MIB", "mplsVpnVrfName"), (0, "A3COM-HUAWEI-MPLS-BGP-VPN-MIB", "mplsVpnVrfRouteDest"), (0, "A3COM-HUAWEI-MPLS-BGP-VPN-MIB", "mplsVpnVrfRouteMask"), (0, "A3COM-HUAWEI-MPLS-BGP-VPN-MIB", "mplsVpnVrfRouteNextHop"))
if mibBuilder.loadTexts: mplsVpnVrfRouteEntry.setStatus('current')
mplsVpnVrfRouteDest = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 45, 1, 5, 12, 3, 1, 3, 1, 1, 1), InetAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mplsVpnVrfRouteDest.setStatus('current')
mplsVpnVrfRouteMask = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 45, 1, 5, 12, 3, 1, 3, 1, 1, 2), InetAddress()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: mplsVpnVrfRouteMask.setStatus('current')
mplsVpnVrfRouteNextHop = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 45, 1, 5, 12, 3, 1, 3, 1, 1, 3), InetAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mplsVpnVrfRouteNextHop.setStatus('current')
mplsVpnVrfRouteIfIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 45, 1, 5, 12, 3, 1, 3, 1, 1, 4), InterfaceIndex()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: mplsVpnVrfRouteIfIndex.setStatus('current')
mplsVpnVrfRouteProto = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 45, 1, 5, 12, 3, 1, 3, 1, 1, 5), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16))).clone(namedValues=NamedValues(("other", 1), ("local", 2), ("netmgmt", 3), ("icmp", 4), ("egp", 5), ("ggp", 6), ("hello", 7), ("rip", 8), ("isIs", 9), ("esIs", 10), ("ciscoIgrp", 11), ("bbnSpfIgp", 12), ("ospf", 13), ("bgp", 14), ("idpr", 15), ("ciscoEigrp", 16)))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: mplsVpnVrfRouteProto.setStatus('current')
mplsVpnVrfRouteRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 45, 1, 5, 12, 3, 1, 3, 1, 1, 6), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: mplsVpnVrfRouteRowStatus.setStatus('current')
mibBuilder.exportSymbols("A3COM-HUAWEI-MPLS-BGP-VPN-MIB", mplsVpnVrfConfIsWarnOnly=mplsVpnVrfConfIsWarnOnly, hwMplsVpn=hwMplsVpn, mplsVpnInterfaceConfTable=mplsVpnInterfaceConfTable, mplsVpnVrfConfTable=mplsVpnVrfConfTable, mplsVpnVrfConfMaxRoutes=mplsVpnVrfConfMaxRoutes, mplsVpnConfiguredVrfs=mplsVpnConfiguredVrfs, mplsVpnVrfName=mplsVpnVrfName, mplsVpnVrfBgpNbrAddrEntry=mplsVpnVrfBgpNbrAddrEntry, mplsVpnVrfNetPrefix=mplsVpnVrfNetPrefix, mplsVpnVrfBgpNbrAsNumber=mplsVpnVrfBgpNbrAsNumber, mplsVpnVrfRouteProto=mplsVpnVrfRouteProto, mplsVpnConf=mplsVpnConf, mplsVpnVrfRouteTargetEntry=mplsVpnVrfRouteTargetEntry, mplsVpnVrfRouteNextHop=mplsVpnVrfRouteNextHop, mplsVpnActiveVrfs=mplsVpnActiveVrfs, mplsVpnVrfConfHighRouteThreshold=mplsVpnVrfConfHighRouteThreshold, mplsVpnVrfNetPrefixType=mplsVpnVrfNetPrefixType, mplsVpnInterfaceConfEntry=mplsVpnInterfaceConfEntry, mplsVpnVrfRouteEntry=mplsVpnVrfRouteEntry, mplsVpnVrfRouteTargetRowStatus=mplsVpnVrfRouteTargetRowStatus, mplsVpnInterfaceConfRowStatus=mplsVpnInterfaceConfRowStatus, mplsVpnVrfConfEntry=mplsVpnVrfConfEntry, PYSNMP_MODULE_ID=hwMplsVpn, mplsVpnInterfaceIpAddressMask=mplsVpnInterfaceIpAddressMask, mplsVpnVrfBgpNbrAddrTable=mplsVpnVrfBgpNbrAddrTable, mplsVpnVrfBgpNbrType=mplsVpnVrfBgpNbrType, mplsVpnVrfBgpNbrRole=mplsVpnVrfBgpNbrRole, mplsVpnVrfRouteRowStatus=mplsVpnVrfRouteRowStatus, mplsVpnVrfBgpNbrRowStatus=mplsVpnVrfBgpNbrRowStatus, mplsVpnVrfRouteTargetTable=mplsVpnVrfRouteTargetTable, mplsVpnVrfRouteTargetType=mplsVpnVrfRouteTargetType, mplsVpnVrfRouteIfIndex=mplsVpnVrfRouteIfIndex, mplsVpnInterfaceLabelEdgeType=mplsVpnInterfaceLabelEdgeType, mplsVpnInterfaceVpnClassification=mplsVpnInterfaceVpnClassification, mplsVpnVrfIpRouteRedistributeStatic=mplsVpnVrfIpRouteRedistributeStatic, mplsVpnVrfIpRouteRedistributeRip=mplsVpnVrfIpRouteRedistributeRip, mplsVpnVrfConfRowStatus=mplsVpnVrfConfRowStatus, mplsVpnVrfBgpNbrAddr=mplsVpnVrfBgpNbrAddr, mplsVpnInterfaceIpAddress=mplsVpnInterfaceIpAddress, mplsVpnInterfaceConfIndex=mplsVpnInterfaceConfIndex, mplsVpnVrfIpRouteRedistributeConn=mplsVpnVrfIpRouteRedistributeConn, mplsVpnVrfRouteDest=mplsVpnVrfRouteDest, MplsVpnRouteDistinguisher=MplsVpnRouteDistinguisher, mplsVpnObjects=mplsVpnObjects, mplsVpnVrfRouteTarget=mplsVpnVrfRouteTarget, mplsVpnVrfBgpNbrAdminStatus=mplsVpnVrfBgpNbrAdminStatus, mplsVpnVrfRouteTable=mplsVpnVrfRouteTable, MplsVpnId=MplsVpnId, mplsVpnVrfRouteMask=mplsVpnVrfRouteMask, mplsVpnRoute=mplsVpnRoute, mplsVpnVrfRouteDistinguisher=mplsVpnVrfRouteDistinguisher, mplsVpnScalars=mplsVpnScalars)