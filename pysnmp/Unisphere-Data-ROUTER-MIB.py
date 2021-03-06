#
# PySNMP MIB module Unisphere-Data-ROUTER-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/Unisphere-Data-ROUTER-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 21:23:06 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
Integer, OctetString, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "Integer", "OctetString", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, SingleValueConstraint, ConstraintsUnion, ValueRangeConstraint, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "SingleValueConstraint", "ConstraintsUnion", "ValueRangeConstraint", "ValueSizeConstraint")
NotificationGroup, ModuleCompliance, ObjectGroup = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance", "ObjectGroup")
Integer32, ModuleIdentity, IpAddress, Counter32, Bits, NotificationType, Counter64, Gauge32, MibScalar, MibTable, MibTableRow, MibTableColumn, ObjectIdentity, Unsigned32, iso, MibIdentifier, TimeTicks = mibBuilder.importSymbols("SNMPv2-SMI", "Integer32", "ModuleIdentity", "IpAddress", "Counter32", "Bits", "NotificationType", "Counter64", "Gauge32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "ObjectIdentity", "Unsigned32", "iso", "MibIdentifier", "TimeTicks")
RowStatus, TruthValue, TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "RowStatus", "TruthValue", "TextualConvention", "DisplayString")
UsdIpPolicyExtendedCommunity, UsdIpPolicyName = mibBuilder.importSymbols("Unisphere-Data-IP-POLICY-MIB", "UsdIpPolicyExtendedCommunity", "UsdIpPolicyName")
usDataMibs, = mibBuilder.importSymbols("Unisphere-Data-MIBs", "usDataMibs")
UsdName, = mibBuilder.importSymbols("Unisphere-Data-TC", "UsdName")
usdRouterMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 4874, 2, 2, 32))
usdRouterMIB.setRevisions(('2002-05-10 18:16', '2001-01-24 18:25', '2000-01-21 00:00',))
if mibBuilder.loadTexts: usdRouterMIB.setLastUpdated('200205101816Z')
if mibBuilder.loadTexts: usdRouterMIB.setOrganization('Unisphere Networks, Inc.')
class UsdNextRouterIndex(TextualConvention, Unsigned32):
    status = 'current'

class UsdRouterProtocolIndex(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28))
    namedValues = NamedValues(("ip", 1), ("osi", 2), ("icmp", 3), ("igmp", 4), ("tcp", 5), ("udp", 6), ("bgp", 7), ("ospf", 8), ("isis", 9), ("rip", 10), ("snmp", 11), ("ntp", 12), ("generator", 13), ("localAddressServer", 14), ("dhcpProxy", 15), ("dhcpRelay", 16), ("nameResolver", 17), ("policyManager", 18), ("sscClient", 19), ("cops", 20), ("mgtm", 21), ("dvmrp", 22), ("pim", 23), ("msdp", 24), ("mpls", 25), ("radius", 26), ("mplsMgr", 27), ("dhcpLocalServer", 28))

usdRouterObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 4874, 2, 2, 32, 1))
usdRouterNextRouterIndex = MibScalar((1, 3, 6, 1, 4, 1, 4874, 2, 2, 32, 1, 1), UsdNextRouterIndex()).setMaxAccess("readonly")
if mibBuilder.loadTexts: usdRouterNextRouterIndex.setStatus('current')
usdRouterTable = MibTable((1, 3, 6, 1, 4, 1, 4874, 2, 2, 32, 1, 2), )
if mibBuilder.loadTexts: usdRouterTable.setStatus('current')
usdRouterEntry = MibTableRow((1, 3, 6, 1, 4, 1, 4874, 2, 2, 32, 1, 2, 1), ).setIndexNames((0, "Unisphere-Data-ROUTER-MIB", "usdRouterIndex"))
if mibBuilder.loadTexts: usdRouterEntry.setStatus('current')
usdRouterIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 4874, 2, 2, 32, 1, 2, 1, 1), Unsigned32())
if mibBuilder.loadTexts: usdRouterIndex.setStatus('current')
usdRouterName = MibTableColumn((1, 3, 6, 1, 4, 1, 4874, 2, 2, 32, 1, 2, 1, 2), UsdName()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: usdRouterName.setStatus('current')
usdRouterRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 4874, 2, 2, 32, 1, 2, 1, 3), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: usdRouterRowStatus.setStatus('current')
usdRouterVrf = MibTableColumn((1, 3, 6, 1, 4, 1, 4874, 2, 2, 32, 1, 2, 1, 4), TruthValue()).setMaxAccess("readonly")
if mibBuilder.loadTexts: usdRouterVrf.setStatus('current')
usdRouterContextName = MibTableColumn((1, 3, 6, 1, 4, 1, 4874, 2, 2, 32, 1, 2, 1, 5), OctetString().subtype(subtypeSpec=ValueSizeConstraint(7, 14))).setMaxAccess("readonly")
if mibBuilder.loadTexts: usdRouterContextName.setStatus('current')
usdRouterProtocolTable = MibTable((1, 3, 6, 1, 4, 1, 4874, 2, 2, 32, 1, 3), )
if mibBuilder.loadTexts: usdRouterProtocolTable.setStatus('current')
usdRouterProtocolEntry = MibTableRow((1, 3, 6, 1, 4, 1, 4874, 2, 2, 32, 1, 3, 1), ).setIndexNames((0, "Unisphere-Data-ROUTER-MIB", "usdRouterProtocolRouterIndex"), (0, "Unisphere-Data-ROUTER-MIB", "usdRouterProtocolProtocolIndex"))
if mibBuilder.loadTexts: usdRouterProtocolEntry.setStatus('current')
usdRouterProtocolRouterIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 4874, 2, 2, 32, 1, 3, 1, 1), Unsigned32())
if mibBuilder.loadTexts: usdRouterProtocolRouterIndex.setStatus('current')
usdRouterProtocolProtocolIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 4874, 2, 2, 32, 1, 3, 1, 2), UsdRouterProtocolIndex())
if mibBuilder.loadTexts: usdRouterProtocolProtocolIndex.setStatus('current')
usdRouterProtocolRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 4874, 2, 2, 32, 1, 3, 1, 3), RowStatus()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: usdRouterProtocolRowStatus.setStatus('current')
usdRouterVrfTable = MibTable((1, 3, 6, 1, 4, 1, 4874, 2, 2, 32, 1, 4), )
if mibBuilder.loadTexts: usdRouterVrfTable.setStatus('current')
usdRouterVrfEntry = MibTableRow((1, 3, 6, 1, 4, 1, 4874, 2, 2, 32, 1, 4, 1), ).setIndexNames((0, "Unisphere-Data-ROUTER-MIB", "usdRouterVrfRouterIndex"), (0, "Unisphere-Data-ROUTER-MIB", "usdRouterVrfRouterVrfIndex"))
if mibBuilder.loadTexts: usdRouterVrfEntry.setStatus('current')
usdRouterVrfRouterIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 4874, 2, 2, 32, 1, 4, 1, 1), Unsigned32())
if mibBuilder.loadTexts: usdRouterVrfRouterIndex.setStatus('current')
usdRouterVrfRouterVrfIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 4874, 2, 2, 32, 1, 4, 1, 2), Unsigned32())
if mibBuilder.loadTexts: usdRouterVrfRouterVrfIndex.setStatus('current')
usdRouterVrfImportRouteMap = MibTableColumn((1, 3, 6, 1, 4, 1, 4874, 2, 2, 32, 1, 4, 1, 3), UsdIpPolicyName()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: usdRouterVrfImportRouteMap.setStatus('current')
usdRouterVrfExportRouteMap = MibTableColumn((1, 3, 6, 1, 4, 1, 4874, 2, 2, 32, 1, 4, 1, 4), UsdIpPolicyName()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: usdRouterVrfExportRouteMap.setStatus('current')
usdRouterVrfRouteDistinguisher = MibTableColumn((1, 3, 6, 1, 4, 1, 4874, 2, 2, 32, 1, 4, 1, 5), UsdIpPolicyExtendedCommunity()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: usdRouterVrfRouteDistinguisher.setStatus('current')
usdRouterVrfRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 4874, 2, 2, 32, 1, 4, 1, 7), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: usdRouterVrfRowStatus.setStatus('current')
usdRouterVrfRouterName = MibTableColumn((1, 3, 6, 1, 4, 1, 4874, 2, 2, 32, 1, 4, 1, 8), UsdName()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: usdRouterVrfRouterName.setStatus('current')
usdRouterVrfRouterDescription = MibTableColumn((1, 3, 6, 1, 4, 1, 4874, 2, 2, 32, 1, 4, 1, 9), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 80))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: usdRouterVrfRouterDescription.setStatus('current')
usdRouterVrfRouteTargetTable = MibTable((1, 3, 6, 1, 4, 1, 4874, 2, 2, 32, 1, 5), )
if mibBuilder.loadTexts: usdRouterVrfRouteTargetTable.setStatus('current')
usdRouterVrfRouteTargetEntry = MibTableRow((1, 3, 6, 1, 4, 1, 4874, 2, 2, 32, 1, 5, 1), ).setIndexNames((0, "Unisphere-Data-ROUTER-MIB", "usdRouterVrfRouteTargetRouterIndex"), (0, "Unisphere-Data-ROUTER-MIB", "usdRouterVrfRouteTargetRouterVrfIndex"), (0, "Unisphere-Data-ROUTER-MIB", "usdRouterVrfRouteTargetAddrFormat"), (0, "Unisphere-Data-ROUTER-MIB", "usdRouterVrfRouteTargetRouteTarget"))
if mibBuilder.loadTexts: usdRouterVrfRouteTargetEntry.setStatus('current')
usdRouterVrfRouteTargetRouterIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 4874, 2, 2, 32, 1, 5, 1, 1), Unsigned32())
if mibBuilder.loadTexts: usdRouterVrfRouteTargetRouterIndex.setStatus('current')
usdRouterVrfRouteTargetRouterVrfIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 4874, 2, 2, 32, 1, 5, 1, 2), Unsigned32())
if mibBuilder.loadTexts: usdRouterVrfRouteTargetRouterVrfIndex.setStatus('current')
usdRouterVrfRouteTargetAddrFormat = MibTableColumn((1, 3, 6, 1, 4, 1, 4874, 2, 2, 32, 1, 5, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1))).clone(namedValues=NamedValues(("routeTargetFormatAsn", 0), ("routeTargetFormateIp", 1))))
if mibBuilder.loadTexts: usdRouterVrfRouteTargetAddrFormat.setStatus('current')
usdRouterVrfRouteTargetRouteTarget = MibTableColumn((1, 3, 6, 1, 4, 1, 4874, 2, 2, 32, 1, 5, 1, 4), UsdIpPolicyExtendedCommunity())
if mibBuilder.loadTexts: usdRouterVrfRouteTargetRouteTarget.setStatus('current')
usdRouterVrfRouteTargetType = MibTableColumn((1, 3, 6, 1, 4, 1, 4874, 2, 2, 32, 1, 5, 1, 5), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3))).clone(namedValues=NamedValues(("routeTargetInvalid", 0), ("routeTargetImport", 1), ("routeTargetExport", 2), ("routeTargetBoth", 3)))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: usdRouterVrfRouteTargetType.setStatus('current')
usdRouterVrfRouteTargetRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 4874, 2, 2, 32, 1, 5, 1, 6), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: usdRouterVrfRouteTargetRowStatus.setStatus('current')
usdRouterConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 4874, 2, 2, 32, 4))
usdRouterCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 4874, 2, 2, 32, 4, 1))
usdRouterGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 4874, 2, 2, 32, 4, 2))
usdRouterCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 4874, 2, 2, 32, 4, 1, 1)).setObjects(("Unisphere-Data-ROUTER-MIB", "usdRouterGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    usdRouterCompliance = usdRouterCompliance.setStatus('obsolete')
usdRouterCompliance2 = ModuleCompliance((1, 3, 6, 1, 4, 1, 4874, 2, 2, 32, 4, 1, 2)).setObjects(("Unisphere-Data-ROUTER-MIB", "usdRouterGroup2"), ("Unisphere-Data-ROUTER-MIB", "usdRouterVrfGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    usdRouterCompliance2 = usdRouterCompliance2.setStatus('obsolete')
usdRouterCompliance3 = ModuleCompliance((1, 3, 6, 1, 4, 1, 4874, 2, 2, 32, 4, 1, 3)).setObjects(("Unisphere-Data-ROUTER-MIB", "usdRouterGroup3"), ("Unisphere-Data-ROUTER-MIB", "usdRouterVrfGroup2"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    usdRouterCompliance3 = usdRouterCompliance3.setStatus('current')
usdRouterGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 4874, 2, 2, 32, 4, 2, 1)).setObjects(("Unisphere-Data-ROUTER-MIB", "usdRouterNextRouterIndex"), ("Unisphere-Data-ROUTER-MIB", "usdRouterName"), ("Unisphere-Data-ROUTER-MIB", "usdRouterRowStatus"), ("Unisphere-Data-ROUTER-MIB", "usdRouterProtocolRowStatus"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    usdRouterGroup = usdRouterGroup.setStatus('obsolete')
usdRouterGroup2 = ObjectGroup((1, 3, 6, 1, 4, 1, 4874, 2, 2, 32, 4, 2, 2)).setObjects(("Unisphere-Data-ROUTER-MIB", "usdRouterNextRouterIndex"), ("Unisphere-Data-ROUTER-MIB", "usdRouterName"), ("Unisphere-Data-ROUTER-MIB", "usdRouterRowStatus"), ("Unisphere-Data-ROUTER-MIB", "usdRouterVrf"), ("Unisphere-Data-ROUTER-MIB", "usdRouterProtocolRowStatus"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    usdRouterGroup2 = usdRouterGroup2.setStatus('obsolete')
usdRouterVrfGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 4874, 2, 2, 32, 4, 2, 3)).setObjects(("Unisphere-Data-ROUTER-MIB", "usdRouterVrfImportRouteMap"), ("Unisphere-Data-ROUTER-MIB", "usdRouterVrfExportRouteMap"), ("Unisphere-Data-ROUTER-MIB", "usdRouterVrfRouteDistinguisher"), ("Unisphere-Data-ROUTER-MIB", "usdRouterVrfRowStatus"), ("Unisphere-Data-ROUTER-MIB", "usdRouterVrfRouterName"), ("Unisphere-Data-ROUTER-MIB", "usdRouterVrfRouteTargetType"), ("Unisphere-Data-ROUTER-MIB", "usdRouterVrfRouteTargetRowStatus"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    usdRouterVrfGroup = usdRouterVrfGroup.setStatus('obsolete')
usdRouterGroup3 = ObjectGroup((1, 3, 6, 1, 4, 1, 4874, 2, 2, 32, 4, 2, 4)).setObjects(("Unisphere-Data-ROUTER-MIB", "usdRouterNextRouterIndex"), ("Unisphere-Data-ROUTER-MIB", "usdRouterName"), ("Unisphere-Data-ROUTER-MIB", "usdRouterRowStatus"), ("Unisphere-Data-ROUTER-MIB", "usdRouterVrf"), ("Unisphere-Data-ROUTER-MIB", "usdRouterProtocolRowStatus"), ("Unisphere-Data-ROUTER-MIB", "usdRouterContextName"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    usdRouterGroup3 = usdRouterGroup3.setStatus('current')
usdRouterVrfGroup2 = ObjectGroup((1, 3, 6, 1, 4, 1, 4874, 2, 2, 32, 4, 2, 5)).setObjects(("Unisphere-Data-ROUTER-MIB", "usdRouterVrfImportRouteMap"), ("Unisphere-Data-ROUTER-MIB", "usdRouterVrfExportRouteMap"), ("Unisphere-Data-ROUTER-MIB", "usdRouterVrfRouteDistinguisher"), ("Unisphere-Data-ROUTER-MIB", "usdRouterVrfRowStatus"), ("Unisphere-Data-ROUTER-MIB", "usdRouterVrfRouterName"), ("Unisphere-Data-ROUTER-MIB", "usdRouterVrfRouterDescription"), ("Unisphere-Data-ROUTER-MIB", "usdRouterVrfRouteTargetType"), ("Unisphere-Data-ROUTER-MIB", "usdRouterVrfRouteTargetRowStatus"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    usdRouterVrfGroup2 = usdRouterVrfGroup2.setStatus('current')
mibBuilder.exportSymbols("Unisphere-Data-ROUTER-MIB", usdRouterGroup=usdRouterGroup, usdRouterVrfRouterIndex=usdRouterVrfRouterIndex, usdRouterCompliances=usdRouterCompliances, usdRouterVrfRouteTargetEntry=usdRouterVrfRouteTargetEntry, usdRouterVrfEntry=usdRouterVrfEntry, usdRouterVrfRouteTargetRouteTarget=usdRouterVrfRouteTargetRouteTarget, usdRouterVrfRouterDescription=usdRouterVrfRouterDescription, usdRouterCompliance2=usdRouterCompliance2, usdRouterVrf=usdRouterVrf, UsdNextRouterIndex=UsdNextRouterIndex, usdRouterVrfImportRouteMap=usdRouterVrfImportRouteMap, usdRouterObjects=usdRouterObjects, UsdRouterProtocolIndex=UsdRouterProtocolIndex, usdRouterVrfRouteTargetTable=usdRouterVrfRouteTargetTable, usdRouterProtocolRowStatus=usdRouterProtocolRowStatus, usdRouterVrfRouteTargetRouterVrfIndex=usdRouterVrfRouteTargetRouterVrfIndex, usdRouterEntry=usdRouterEntry, usdRouterMIB=usdRouterMIB, usdRouterVrfExportRouteMap=usdRouterVrfExportRouteMap, usdRouterGroup2=usdRouterGroup2, usdRouterVrfRowStatus=usdRouterVrfRowStatus, usdRouterTable=usdRouterTable, usdRouterName=usdRouterName, usdRouterVrfRouteTargetAddrFormat=usdRouterVrfRouteTargetAddrFormat, usdRouterConformance=usdRouterConformance, usdRouterRowStatus=usdRouterRowStatus, usdRouterCompliance3=usdRouterCompliance3, usdRouterProtocolEntry=usdRouterProtocolEntry, usdRouterVrfRouteTargetType=usdRouterVrfRouteTargetType, usdRouterGroups=usdRouterGroups, usdRouterVrfRouteTargetRouterIndex=usdRouterVrfRouteTargetRouterIndex, usdRouterNextRouterIndex=usdRouterNextRouterIndex, usdRouterProtocolTable=usdRouterProtocolTable, usdRouterContextName=usdRouterContextName, usdRouterVrfRouteDistinguisher=usdRouterVrfRouteDistinguisher, usdRouterProtocolProtocolIndex=usdRouterProtocolProtocolIndex, usdRouterGroup3=usdRouterGroup3, usdRouterVrfRouteTargetRowStatus=usdRouterVrfRouteTargetRowStatus, usdRouterVrfTable=usdRouterVrfTable, usdRouterVrfRouterVrfIndex=usdRouterVrfRouterVrfIndex, usdRouterVrfRouterName=usdRouterVrfRouterName, PYSNMP_MODULE_ID=usdRouterMIB, usdRouterCompliance=usdRouterCompliance, usdRouterProtocolRouterIndex=usdRouterProtocolRouterIndex, usdRouterVrfGroup2=usdRouterVrfGroup2, usdRouterIndex=usdRouterIndex, usdRouterVrfGroup=usdRouterVrfGroup)
