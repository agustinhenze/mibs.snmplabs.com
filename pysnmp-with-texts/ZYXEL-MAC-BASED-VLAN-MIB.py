#
# PySNMP MIB module ZYXEL-MAC-BASED-VLAN-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/ZYXEL-MAC-BASED-VLAN-MIB
# Produced by pysmi-0.3.4 at Wed May  1 15:50:45 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
SingleValueConstraint, ValueSizeConstraint, ConstraintsUnion, ValueRangeConstraint, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "SingleValueConstraint", "ValueSizeConstraint", "ConstraintsUnion", "ValueRangeConstraint", "ConstraintsIntersection")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
TimeTicks, Unsigned32, MibScalar, MibTable, MibTableRow, MibTableColumn, ObjectIdentity, ModuleIdentity, Integer32, NotificationType, Counter64, iso, Bits, Counter32, enterprises, IpAddress, Gauge32, MibIdentifier = mibBuilder.importSymbols("SNMPv2-SMI", "TimeTicks", "Unsigned32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "ObjectIdentity", "ModuleIdentity", "Integer32", "NotificationType", "Counter64", "iso", "Bits", "Counter32", "enterprises", "IpAddress", "Gauge32", "MibIdentifier")
MacAddress, DisplayString, TextualConvention, RowStatus = mibBuilder.importSymbols("SNMPv2-TC", "MacAddress", "DisplayString", "TextualConvention", "RowStatus")
esMgmt, = mibBuilder.importSymbols("ZYXEL-ES-SMI", "esMgmt")
zyxelMacBasedVlan = ModuleIdentity((1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 99))
if mibBuilder.loadTexts: zyxelMacBasedVlan.setLastUpdated('201402250000Z')
if mibBuilder.loadTexts: zyxelMacBasedVlan.setOrganization('Enterprise Solution ZyXEL')
if mibBuilder.loadTexts: zyxelMacBasedVlan.setContactInfo('')
if mibBuilder.loadTexts: zyxelMacBasedVlan.setDescription('study')
zyxelMacBasedVlanSetup = MibIdentifier((1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 99, 1))
zyxelMacBasedVlanStatus = MibIdentifier((1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 99, 2))
zyMacBasedVlanMaxNumberOfVlans = MibScalar((1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 99, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: zyMacBasedVlanMaxNumberOfVlans.setStatus('current')
if mibBuilder.loadTexts: zyMacBasedVlanMaxNumberOfVlans.setDescription('Maximum binding number of MAC-based VLAN')
zyxelMacBasedVlanBindingTable = MibTable((1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 99, 1, 2), )
if mibBuilder.loadTexts: zyxelMacBasedVlanBindingTable.setStatus('current')
if mibBuilder.loadTexts: zyxelMacBasedVlanBindingTable.setDescription('The table of MAC-based VLAN configuration.')
zyxelMacBasedVlanBindingEntry = MibTableRow((1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 99, 1, 2, 1), ).setIndexNames((0, "ZYXEL-MAC-BASED-VLAN-MIB", "zyMacBasedVlanBindingSourceMac"))
if mibBuilder.loadTexts: zyxelMacBasedVlanBindingEntry.setStatus('current')
if mibBuilder.loadTexts: zyxelMacBasedVlanBindingEntry.setDescription('An entry contains MAC-based VLAN configuration. ')
zyMacBasedVlanBindingSourceMac = MibTableColumn((1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 99, 1, 2, 1, 1), MacAddress())
if mibBuilder.loadTexts: zyMacBasedVlanBindingSourceMac.setStatus('current')
if mibBuilder.loadTexts: zyMacBasedVlanBindingSourceMac.setDescription('source MAC address of binding')
zyMacBasedVlanBindingName = MibTableColumn((1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 99, 1, 2, 1, 2), OctetString()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: zyMacBasedVlanBindingName.setStatus('current')
if mibBuilder.loadTexts: zyMacBasedVlanBindingName.setDescription('Set a name of the MAC-based VLAN binding')
zyMacBasedVlanBindingVlan = MibTableColumn((1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 99, 1, 2, 1, 3), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 4094))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: zyMacBasedVlanBindingVlan.setStatus('current')
if mibBuilder.loadTexts: zyMacBasedVlanBindingVlan.setDescription('Set a vid for untagged frame forwarding')
zyMacBasedVlanBindingPriority = MibTableColumn((1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 99, 1, 2, 1, 4), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 7))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: zyMacBasedVlanBindingPriority.setStatus('current')
if mibBuilder.loadTexts: zyMacBasedVlanBindingPriority.setDescription('Set a priority to apply to the vlan')
zyMacBasedVlanBindingRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 99, 1, 2, 1, 5), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: zyMacBasedVlanBindingRowStatus.setStatus('current')
if mibBuilder.loadTexts: zyMacBasedVlanBindingRowStatus.setDescription('This object allows entries to be created and deleted from the MAC.')
mibBuilder.exportSymbols("ZYXEL-MAC-BASED-VLAN-MIB", zyMacBasedVlanBindingPriority=zyMacBasedVlanBindingPriority, zyMacBasedVlanBindingRowStatus=zyMacBasedVlanBindingRowStatus, PYSNMP_MODULE_ID=zyxelMacBasedVlan, zyxelMacBasedVlanSetup=zyxelMacBasedVlanSetup, zyxelMacBasedVlan=zyxelMacBasedVlan, zyxelMacBasedVlanStatus=zyxelMacBasedVlanStatus, zyMacBasedVlanMaxNumberOfVlans=zyMacBasedVlanMaxNumberOfVlans, zyMacBasedVlanBindingName=zyMacBasedVlanBindingName, zyMacBasedVlanBindingSourceMac=zyMacBasedVlanBindingSourceMac, zyxelMacBasedVlanBindingTable=zyxelMacBasedVlanBindingTable, zyMacBasedVlanBindingVlan=zyMacBasedVlanBindingVlan, zyxelMacBasedVlanBindingEntry=zyxelMacBasedVlanBindingEntry)
