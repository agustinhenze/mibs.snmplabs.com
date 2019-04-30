#
# PySNMP MIB module HP-ICF-PROVIDER-BRIDGE (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/HP-ICF-PROVIDER-BRIDGE
# Produced by pysmi-0.3.4 at Mon Apr 29 19:22:34 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
OctetString, Integer, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "OctetString", "Integer", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
SingleValueConstraint, ValueSizeConstraint, ConstraintsUnion, ValueRangeConstraint, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "SingleValueConstraint", "ValueSizeConstraint", "ConstraintsUnion", "ValueRangeConstraint", "ConstraintsIntersection")
hpSwitch, = mibBuilder.importSymbols("HP-ICF-OID", "hpSwitch")
ifIndex, = mibBuilder.importSymbols("IF-MIB", "ifIndex")
dot1qVlanStaticEntry, = mibBuilder.importSymbols("Q-BRIDGE-MIB", "dot1qVlanStaticEntry")
ModuleCompliance, ObjectGroup, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "ObjectGroup", "NotificationGroup")
MibIdentifier, Unsigned32, Gauge32, iso, Counter32, Counter64, Bits, ModuleIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, Integer32, IpAddress, NotificationType, ObjectIdentity, TimeTicks = mibBuilder.importSymbols("SNMPv2-SMI", "MibIdentifier", "Unsigned32", "Gauge32", "iso", "Counter32", "Counter64", "Bits", "ModuleIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Integer32", "IpAddress", "NotificationType", "ObjectIdentity", "TimeTicks")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
hpicfProviderBridge = ModuleIdentity((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 40))
hpicfProviderBridge.setRevisions(('2008-10-01 00:00', '2006-08-15 00:00',))
if mibBuilder.loadTexts: hpicfProviderBridge.setLastUpdated('200810010000Z')
if mibBuilder.loadTexts: hpicfProviderBridge.setOrganization('HP Networking')
hpicfProviderBridgeObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 40, 1))
hpicfProviderBridgeBase = MibIdentifier((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 40, 1, 1))
hpicfProviderBridgeType = MibScalar((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 40, 1, 1, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))).clone(namedValues=NamedValues(("vlanBridge", 1), ("svlanBridge", 2), ("providerEdgeBridge", 3), ("vlanSvlanBridge", 4))).clone('vlanBridge')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hpicfProviderBridgeType.setStatus('current')
hpicfProviderBridgeEtherType = MibScalar((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 40, 1, 1, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1536, 65535)).clone(34984)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hpicfProviderBridgeEtherType.setStatus('current')
hpicfProviderBridgeVlanTypeTable = MibTable((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 40, 1, 1, 3), )
if mibBuilder.loadTexts: hpicfProviderBridgeVlanTypeTable.setStatus('current')
hpicfProviderBridgeVlanTypeEntry = MibTableRow((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 40, 1, 1, 3, 1), )
dot1qVlanStaticEntry.registerAugmentions(("HP-ICF-PROVIDER-BRIDGE", "hpicfProviderBridgeVlanTypeEntry"))
hpicfProviderBridgeVlanTypeEntry.setIndexNames(*dot1qVlanStaticEntry.getIndexNames())
if mibBuilder.loadTexts: hpicfProviderBridgeVlanTypeEntry.setStatus('current')
hpicfProviderBridgeVlanType = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 40, 1, 1, 3, 1, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("cvlan", 1), ("svlan", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hpicfProviderBridgeVlanType.setStatus('current')
hpicfProviderBridgePortTable = MibTable((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 40, 1, 1, 4), )
if mibBuilder.loadTexts: hpicfProviderBridgePortTable.setStatus('current')
hpicfProviderBridgePortEntry = MibTableRow((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 40, 1, 1, 4, 1), ).setIndexNames((0, "IF-MIB", "ifIndex"))
if mibBuilder.loadTexts: hpicfProviderBridgePortEntry.setStatus('current')
hpicfProviderBridgePortType = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 40, 1, 1, 4, 1, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("customer-edge", 1), ("customer-network", 2), ("provider-network", 3))).clone('customer-edge')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hpicfProviderBridgePortType.setStatus('current')
hpicfProviderBridgeConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 40, 2))
hpicfProviderBridgeGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 40, 2, 1))
hpicfProviderBridgeBaseGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 40, 2, 1, 1)).setObjects(("HP-ICF-PROVIDER-BRIDGE", "hpicfProviderBridgeType"), ("HP-ICF-PROVIDER-BRIDGE", "hpicfProviderBridgeEtherType"), ("HP-ICF-PROVIDER-BRIDGE", "hpicfProviderBridgePortType"), ("HP-ICF-PROVIDER-BRIDGE", "hpicfProviderBridgeVlanType"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    hpicfProviderBridgeBaseGroup = hpicfProviderBridgeBaseGroup.setStatus('current')
hpicfProviderBridgeCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 40, 2, 2))
hpicfProviderBridgeCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 40, 2, 2, 1)).setObjects(("HP-ICF-PROVIDER-BRIDGE", "hpicfProviderBridgeBaseGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    hpicfProviderBridgeCompliance = hpicfProviderBridgeCompliance.setStatus('current')
mibBuilder.exportSymbols("HP-ICF-PROVIDER-BRIDGE", hpicfProviderBridgePortTable=hpicfProviderBridgePortTable, hpicfProviderBridgePortEntry=hpicfProviderBridgePortEntry, PYSNMP_MODULE_ID=hpicfProviderBridge, hpicfProviderBridgeEtherType=hpicfProviderBridgeEtherType, hpicfProviderBridgeCompliance=hpicfProviderBridgeCompliance, hpicfProviderBridgeVlanType=hpicfProviderBridgeVlanType, hpicfProviderBridgePortType=hpicfProviderBridgePortType, hpicfProviderBridgeCompliances=hpicfProviderBridgeCompliances, hpicfProviderBridgeType=hpicfProviderBridgeType, hpicfProviderBridge=hpicfProviderBridge, hpicfProviderBridgeConformance=hpicfProviderBridgeConformance, hpicfProviderBridgeVlanTypeEntry=hpicfProviderBridgeVlanTypeEntry, hpicfProviderBridgeBaseGroup=hpicfProviderBridgeBaseGroup, hpicfProviderBridgeObjects=hpicfProviderBridgeObjects, hpicfProviderBridgeBase=hpicfProviderBridgeBase, hpicfProviderBridgeGroups=hpicfProviderBridgeGroups, hpicfProviderBridgeVlanTypeTable=hpicfProviderBridgeVlanTypeTable)