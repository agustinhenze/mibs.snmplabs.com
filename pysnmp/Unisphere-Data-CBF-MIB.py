#
# PySNMP MIB module Unisphere-Data-CBF-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/Unisphere-Data-CBF-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 21:23:22 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ValueRangeConstraint, ConstraintsUnion, ConstraintsIntersection, SingleValueConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ValueRangeConstraint", "ConstraintsUnion", "ConstraintsIntersection", "SingleValueConstraint")
InterfaceIndex, InterfaceIndexOrZero = mibBuilder.importSymbols("IF-MIB", "InterfaceIndex", "InterfaceIndexOrZero")
ModuleCompliance, NotificationGroup, ObjectGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup", "ObjectGroup")
IpAddress, ObjectIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter64, TimeTicks, iso, Bits, NotificationType, Unsigned32, ModuleIdentity, MibIdentifier, Counter32, Gauge32, Integer32 = mibBuilder.importSymbols("SNMPv2-SMI", "IpAddress", "ObjectIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter64", "TimeTicks", "iso", "Bits", "NotificationType", "Unsigned32", "ModuleIdentity", "MibIdentifier", "Counter32", "Gauge32", "Integer32")
TextualConvention, RowStatus, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "RowStatus", "DisplayString")
usDataMibs, = mibBuilder.importSymbols("Unisphere-Data-MIBs", "usDataMibs")
UsdNextIfIndex, = mibBuilder.importSymbols("Unisphere-Data-TC", "UsdNextIfIndex")
usdCbfMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 4874, 2, 2, 52))
usdCbfMIB.setRevisions(('2001-03-30 16:27',))
if mibBuilder.loadTexts: usdCbfMIB.setLastUpdated('200103301627Z')
if mibBuilder.loadTexts: usdCbfMIB.setOrganization('Unisphere Networks, Inc.')
usdCbfObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 4874, 2, 2, 52, 1))
usdCbfInterface = MibIdentifier((1, 3, 6, 1, 4, 1, 4874, 2, 2, 52, 1, 1))
usdCbfNextIfIndex = MibScalar((1, 3, 6, 1, 4, 1, 4874, 2, 2, 52, 1, 1, 1), UsdNextIfIndex()).setMaxAccess("readonly")
if mibBuilder.loadTexts: usdCbfNextIfIndex.setStatus('current')
usdCbfIfTable = MibTable((1, 3, 6, 1, 4, 1, 4874, 2, 2, 52, 1, 1, 2), )
if mibBuilder.loadTexts: usdCbfIfTable.setStatus('current')
usdCbfIfEntry = MibTableRow((1, 3, 6, 1, 4, 1, 4874, 2, 2, 52, 1, 1, 2, 1), ).setIndexNames((0, "Unisphere-Data-CBF-MIB", "usdCbfIfIndex"))
if mibBuilder.loadTexts: usdCbfIfEntry.setStatus('current')
usdCbfIfIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 4874, 2, 2, 52, 1, 1, 2, 1, 1), InterfaceIndex())
if mibBuilder.loadTexts: usdCbfIfIndex.setStatus('current')
usdCbfIfRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 4874, 2, 2, 52, 1, 1, 2, 1, 2), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: usdCbfIfRowStatus.setStatus('current')
usdCbfIfLowerIfIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 4874, 2, 2, 52, 1, 1, 2, 1, 3), InterfaceIndexOrZero()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: usdCbfIfLowerIfIndex.setStatus('current')
usdCbfIfConnTable = MibTable((1, 3, 6, 1, 4, 1, 4874, 2, 2, 52, 1, 1, 4), )
if mibBuilder.loadTexts: usdCbfIfConnTable.setStatus('current')
usdCbfIfConnEntry = MibTableRow((1, 3, 6, 1, 4, 1, 4874, 2, 2, 52, 1, 1, 4, 1), ).setIndexNames((0, "Unisphere-Data-CBF-MIB", "usdCbfIfIngressIfIndex"))
if mibBuilder.loadTexts: usdCbfIfConnEntry.setStatus('current')
usdCbfIfIngressIfIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 4874, 2, 2, 52, 1, 1, 4, 1, 1), InterfaceIndex())
if mibBuilder.loadTexts: usdCbfIfIngressIfIndex.setStatus('current')
usdCbfIfConnRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 4874, 2, 2, 52, 1, 1, 4, 1, 2), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: usdCbfIfConnRowStatus.setStatus('current')
usdCbfIfEgressIfIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 4874, 2, 2, 52, 1, 1, 4, 1, 3), InterfaceIndex()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: usdCbfIfEgressIfIndex.setStatus('current')
usdCbfConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 4874, 2, 2, 52, 4))
usdCbfCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 4874, 2, 2, 52, 4, 1))
usdCbfGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 4874, 2, 2, 52, 4, 2))
usdCbfCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 4874, 2, 2, 52, 4, 1, 1)).setObjects(("Unisphere-Data-CBF-MIB", "usdCbfGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    usdCbfCompliance = usdCbfCompliance.setStatus('current')
usdCbfGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 4874, 2, 2, 52, 4, 2, 1)).setObjects(("Unisphere-Data-CBF-MIB", "usdCbfNextIfIndex"), ("Unisphere-Data-CBF-MIB", "usdCbfIfRowStatus"), ("Unisphere-Data-CBF-MIB", "usdCbfIfLowerIfIndex"), ("Unisphere-Data-CBF-MIB", "usdCbfIfConnRowStatus"), ("Unisphere-Data-CBF-MIB", "usdCbfIfEgressIfIndex"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    usdCbfGroup = usdCbfGroup.setStatus('current')
mibBuilder.exportSymbols("Unisphere-Data-CBF-MIB", usdCbfMIB=usdCbfMIB, usdCbfIfRowStatus=usdCbfIfRowStatus, usdCbfIfConnTable=usdCbfIfConnTable, usdCbfIfEgressIfIndex=usdCbfIfEgressIfIndex, usdCbfIfIndex=usdCbfIfIndex, usdCbfIfEntry=usdCbfIfEntry, usdCbfCompliances=usdCbfCompliances, usdCbfIfLowerIfIndex=usdCbfIfLowerIfIndex, usdCbfIfConnEntry=usdCbfIfConnEntry, usdCbfNextIfIndex=usdCbfNextIfIndex, usdCbfIfConnRowStatus=usdCbfIfConnRowStatus, usdCbfIfIngressIfIndex=usdCbfIfIngressIfIndex, usdCbfGroups=usdCbfGroups, usdCbfConformance=usdCbfConformance, usdCbfCompliance=usdCbfCompliance, usdCbfGroup=usdCbfGroup, usdCbfIfTable=usdCbfIfTable, usdCbfObjects=usdCbfObjects, usdCbfInterface=usdCbfInterface, PYSNMP_MODULE_ID=usdCbfMIB)
