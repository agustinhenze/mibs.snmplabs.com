#
# PySNMP MIB module HPN-ICF-VMAP-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/HPN-ICF-VMAP-MIB
# Produced by pysmi-0.3.4 at Wed May  1 13:41:50 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
SingleValueConstraint, ConstraintsUnion, ValueSizeConstraint, ValueRangeConstraint, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "SingleValueConstraint", "ConstraintsUnion", "ValueSizeConstraint", "ValueRangeConstraint", "ConstraintsIntersection")
hpnicfCommon, = mibBuilder.importSymbols("HPN-ICF-OID-MIB", "hpnicfCommon")
ifIndex, = mibBuilder.importSymbols("IF-MIB", "ifIndex")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
Counter32, ObjectIdentity, MibIdentifier, iso, Integer32, Unsigned32, IpAddress, Counter64, TimeTicks, NotificationType, ModuleIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, Bits, Gauge32 = mibBuilder.importSymbols("SNMPv2-SMI", "Counter32", "ObjectIdentity", "MibIdentifier", "iso", "Integer32", "Unsigned32", "IpAddress", "Counter64", "TimeTicks", "NotificationType", "ModuleIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Bits", "Gauge32")
TextualConvention, DisplayString, TruthValue, RowStatus = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString", "TruthValue", "RowStatus")
hpnicfVmap = ModuleIdentity((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 138))
hpnicfVmap.setRevisions(('2013-03-08 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: hpnicfVmap.setRevisionsDescriptions(('The initial version of this MIB.',))
if mibBuilder.loadTexts: hpnicfVmap.setLastUpdated('201303080000Z')
if mibBuilder.loadTexts: hpnicfVmap.setOrganization('')
if mibBuilder.loadTexts: hpnicfVmap.setContactInfo('')
if mibBuilder.loadTexts: hpnicfVmap.setDescription('H3C 802.1 VLAN Mapping MIB Version')
hpnicfVMAPNNITable = MibTable((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 138, 1), )
if mibBuilder.loadTexts: hpnicfVMAPNNITable.setStatus('current')
if mibBuilder.loadTexts: hpnicfVMAPNNITable.setDescription('VLAN mapping NNI table.')
hpnicfVMAPNNIEntry = MibTableRow((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 138, 1, 1), ).setIndexNames((0, "IF-MIB", "ifIndex"))
if mibBuilder.loadTexts: hpnicfVMAPNNIEntry.setStatus('current')
if mibBuilder.loadTexts: hpnicfVMAPNNIEntry.setDescription('VLAN mapping NNI table entries.')
hpnicfVMAPNNIState = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 138, 1, 1, 1), TruthValue()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hpnicfVMAPNNIState.setStatus('current')
if mibBuilder.loadTexts: hpnicfVMAPNNIState.setDescription('Set the network-side interface for a many-to-one VLAN mapping.')
hpnicfVMAP1to1Table = MibTable((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 138, 2), )
if mibBuilder.loadTexts: hpnicfVMAP1to1Table.setStatus('current')
if mibBuilder.loadTexts: hpnicfVMAP1to1Table.setDescription('One-to-one VLAN mapping table.')
hpnicfVMAP1to1Entry = MibTableRow((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 138, 2, 1), ).setIndexNames((0, "IF-MIB", "ifIndex"), (0, "HPN-ICF-VMAP-MIB", "hpnicfVMAP1to1Vlan"))
if mibBuilder.loadTexts: hpnicfVMAP1to1Entry.setStatus('current')
if mibBuilder.loadTexts: hpnicfVMAP1to1Entry.setDescription('One-to-one VLAN mapping table entries.')
hpnicfVMAP1to1Vlan = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 138, 2, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 65535)))
if mibBuilder.loadTexts: hpnicfVMAP1to1Vlan.setStatus('current')
if mibBuilder.loadTexts: hpnicfVMAP1to1Vlan.setDescription('The original VLAN for a one-to-one VLAN mapping on the port.')
hpnicfVMAP1to1TranslatedVlan = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 138, 2, 1, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 65535))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hpnicfVMAP1to1TranslatedVlan.setStatus('current')
if mibBuilder.loadTexts: hpnicfVMAP1to1TranslatedVlan.setDescription('The translated VLAN for a one-to-one VLAN mapping on the port.')
hpnicfVMAP1to1RowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 138, 2, 1, 3), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hpnicfVMAP1to1RowStatus.setStatus('current')
if mibBuilder.loadTexts: hpnicfVMAP1to1RowStatus.setDescription('Operation status of this table entry.')
hpnicfVMAPNto1RangeTable = MibTable((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 138, 3), )
if mibBuilder.loadTexts: hpnicfVMAPNto1RangeTable.setStatus('current')
if mibBuilder.loadTexts: hpnicfVMAPNto1RangeTable.setDescription('Many-to-one VLAN mapping table. The original VLANs of each entry should be a range of VLANs (for example, VLAN 20 to 30).')
hpnicfVMAPNto1RangeEntry = MibTableRow((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 138, 3, 1), ).setIndexNames((0, "IF-MIB", "ifIndex"), (0, "HPN-ICF-VMAP-MIB", "hpnicfVMAPNto1StartVlan"))
if mibBuilder.loadTexts: hpnicfVMAPNto1RangeEntry.setStatus('current')
if mibBuilder.loadTexts: hpnicfVMAPNto1RangeEntry.setDescription('Many-to-one VLAN mapping table entries. The original VLANs of each entry should be a range of VLANs (for example, VLAN 20 to 30).')
hpnicfVMAPNto1StartVlan = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 138, 3, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 65535)))
if mibBuilder.loadTexts: hpnicfVMAPNto1StartVlan.setStatus('current')
if mibBuilder.loadTexts: hpnicfVMAPNto1StartVlan.setDescription('The original start VLAN for a many-to-one VLAN mapping on the port.')
hpnicfVMAPNto1EndVlan = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 138, 3, 1, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 65535))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hpnicfVMAPNto1EndVlan.setStatus('current')
if mibBuilder.loadTexts: hpnicfVMAPNto1EndVlan.setDescription('The original end VLAN for a many-to-one VLAN mapping on the port.')
hpnicfVMAPNto1RangeTranslatedVlan = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 138, 3, 1, 3), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 65535))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hpnicfVMAPNto1RangeTranslatedVlan.setStatus('current')
if mibBuilder.loadTexts: hpnicfVMAPNto1RangeTranslatedVlan.setDescription('The translated VLAN for a many-to-one VLAN mapping on the port.')
hpnicfVMAPNto1RangeRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 138, 3, 1, 4), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hpnicfVMAPNto1RangeRowStatus.setStatus('current')
if mibBuilder.loadTexts: hpnicfVMAPNto1RangeRowStatus.setDescription('Operation status of this table entry.')
hpnicfVMAPNto1SingleTable = MibTable((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 138, 4), )
if mibBuilder.loadTexts: hpnicfVMAPNto1SingleTable.setStatus('current')
if mibBuilder.loadTexts: hpnicfVMAPNto1SingleTable.setDescription('Many-to-one VLAN mapping table. The original VLANs of each entry should be a group of VLANs listed one by one (for example, VLAN 30, 31, 32).')
hpnicfVMAPNto1SingleEntry = MibTableRow((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 138, 4, 1), ).setIndexNames((0, "IF-MIB", "ifIndex"), (0, "HPN-ICF-VMAP-MIB", "hpnicfVMAPNto1Vlan"))
if mibBuilder.loadTexts: hpnicfVMAPNto1SingleEntry.setStatus('current')
if mibBuilder.loadTexts: hpnicfVMAPNto1SingleEntry.setDescription('Many-to-one VLAN mapping table entries. The original VLANs of each entry should be a group of VLANs listed one by one (for example, VLAN 30, 31, 32).')
hpnicfVMAPNto1Vlan = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 138, 4, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 65535)))
if mibBuilder.loadTexts: hpnicfVMAPNto1Vlan.setStatus('current')
if mibBuilder.loadTexts: hpnicfVMAPNto1Vlan.setDescription('The original VLANs for a many-to-one VLAN mapping on the port.')
hpnicfVMAPNto1SingleTranslatedVlan = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 138, 4, 1, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 65535))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hpnicfVMAPNto1SingleTranslatedVlan.setStatus('current')
if mibBuilder.loadTexts: hpnicfVMAPNto1SingleTranslatedVlan.setDescription('The translated VLAN for a many-to-one VLAN mapping on the port.')
hpnicfVMAPNto1SingleRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 138, 4, 1, 3), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hpnicfVMAPNto1SingleRowStatus.setStatus('current')
if mibBuilder.loadTexts: hpnicfVMAPNto1SingleRowStatus.setDescription('Operation status of this table entry.')
hpnicfVMAP1to2RangeTable = MibTable((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 138, 5), )
if mibBuilder.loadTexts: hpnicfVMAP1to2RangeTable.setStatus('current')
if mibBuilder.loadTexts: hpnicfVMAP1to2RangeTable.setDescription('One-to-two VLAN mapping table. The original VLANs of each entry should be a range of VLANs (for example, VLAN 20 to 30).')
hpnicfVMAP1to2RangeEntry = MibTableRow((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 138, 5, 1), ).setIndexNames((0, "IF-MIB", "ifIndex"), (0, "HPN-ICF-VMAP-MIB", "hpnicfVMAP1to2StartVlan"))
if mibBuilder.loadTexts: hpnicfVMAP1to2RangeEntry.setStatus('current')
if mibBuilder.loadTexts: hpnicfVMAP1to2RangeEntry.setDescription('One-to-two VLAN mapping table entries. The original VLANs of each entry should be a range of VLANs (for example, VLAN 20 to 30).')
hpnicfVMAP1to2StartVlan = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 138, 5, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 65535)))
if mibBuilder.loadTexts: hpnicfVMAP1to2StartVlan.setStatus('current')
if mibBuilder.loadTexts: hpnicfVMAP1to2StartVlan.setDescription('The original start VLAN for a one-to-two VLAN mapping on the port.')
hpnicfVMAP1to2EndVlan = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 138, 5, 1, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 65535))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hpnicfVMAP1to2EndVlan.setStatus('current')
if mibBuilder.loadTexts: hpnicfVMAP1to2EndVlan.setDescription('The original end VLAN for a one-to-two VLAN mapping on the port.')
hpnicfVMAP1to2RangeNestedVlan = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 138, 5, 1, 3), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 65535))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hpnicfVMAP1to2RangeNestedVlan.setStatus('current')
if mibBuilder.loadTexts: hpnicfVMAP1to2RangeNestedVlan.setDescription('The outer VLAN for a one-to-two VLAN mapping on the port.')
hpnicfVMAP1to2RangeRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 138, 5, 1, 4), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hpnicfVMAP1to2RangeRowStatus.setStatus('current')
if mibBuilder.loadTexts: hpnicfVMAP1to2RangeRowStatus.setDescription('Operation status of this table entry.')
hpnicfVMAP1to2SingleTable = MibTable((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 138, 6), )
if mibBuilder.loadTexts: hpnicfVMAP1to2SingleTable.setStatus('current')
if mibBuilder.loadTexts: hpnicfVMAP1to2SingleTable.setDescription('One-to-two VLAN mapping table. The original VLANs of each entry should be a group of VLANs listed one by one (for example, VLAN 30, 31, 32).')
hpnicfVMAP1to2SingleEntry = MibTableRow((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 138, 6, 1), ).setIndexNames((0, "IF-MIB", "ifIndex"), (0, "HPN-ICF-VMAP-MIB", "hpnicfVMAP1to2Vlan"))
if mibBuilder.loadTexts: hpnicfVMAP1to2SingleEntry.setStatus('current')
if mibBuilder.loadTexts: hpnicfVMAP1to2SingleEntry.setDescription('One-to-two VLAN mapping table entries. The original VLANs of each entry should be a group of VLANs listed one by one (for example, VLAN 30, 31, 32).')
hpnicfVMAP1to2Vlan = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 138, 6, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 65535)))
if mibBuilder.loadTexts: hpnicfVMAP1to2Vlan.setStatus('current')
if mibBuilder.loadTexts: hpnicfVMAP1to2Vlan.setDescription('The original VLANs for a one-to-two VLAN mapping on the port.')
hpnicfVMAP1to2SingleNestedVlan = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 138, 6, 1, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 65535))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hpnicfVMAP1to2SingleNestedVlan.setStatus('current')
if mibBuilder.loadTexts: hpnicfVMAP1to2SingleNestedVlan.setDescription('The outer VLAN for a one-to-two VLAN mapping on the port.')
hpnicfVMAP1to2SingleRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 138, 6, 1, 3), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hpnicfVMAP1to2SingleRowStatus.setStatus('current')
if mibBuilder.loadTexts: hpnicfVMAP1to2SingleRowStatus.setDescription('Operation status of this table entry.')
hpnicfVMAP2to2Table = MibTable((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 138, 7), )
if mibBuilder.loadTexts: hpnicfVMAP2to2Table.setStatus('current')
if mibBuilder.loadTexts: hpnicfVMAP2to2Table.setDescription('Two-to-two VLAN mapping table.')
hpnicfVMAP2to2Entry = MibTableRow((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 138, 7, 1), ).setIndexNames((0, "IF-MIB", "ifIndex"), (0, "HPN-ICF-VMAP-MIB", "hpnicfVMAP2to2OuterVlan"), (0, "HPN-ICF-VMAP-MIB", "hpnicfVMAP2to2InnerVlan"))
if mibBuilder.loadTexts: hpnicfVMAP2to2Entry.setStatus('current')
if mibBuilder.loadTexts: hpnicfVMAP2to2Entry.setDescription('Two-to-two VLAN mapping table entries.')
hpnicfVMAP2to2OuterVlan = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 138, 7, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 65535)))
if mibBuilder.loadTexts: hpnicfVMAP2to2OuterVlan.setStatus('current')
if mibBuilder.loadTexts: hpnicfVMAP2to2OuterVlan.setDescription('The original outer VLAN for a two-to-two VLAN mapping on the port.')
hpnicfVMAP2to2InnerVlan = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 138, 7, 1, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 65535)))
if mibBuilder.loadTexts: hpnicfVMAP2to2InnerVlan.setStatus('current')
if mibBuilder.loadTexts: hpnicfVMAP2to2InnerVlan.setDescription('The original inner VLAN for a two-to-two VLAN mapping on the port.')
hpnicfVMAP2to2TranslatedOuterVlan = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 138, 7, 1, 3), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 65535))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hpnicfVMAP2to2TranslatedOuterVlan.setStatus('current')
if mibBuilder.loadTexts: hpnicfVMAP2to2TranslatedOuterVlan.setDescription('The translated outer VLAN for a two-to-two VLAN mapping on the port.')
hpnicfVMAP2to2TranslatedInnerVlan = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 138, 7, 1, 4), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 65535))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hpnicfVMAP2to2TranslatedInnerVlan.setStatus('current')
if mibBuilder.loadTexts: hpnicfVMAP2to2TranslatedInnerVlan.setDescription('The translated inner VLAN for a two-to-two VLAN mapping on the port.')
hpnicfVMAP2to2RowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 138, 7, 1, 5), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hpnicfVMAP2to2RowStatus.setStatus('current')
if mibBuilder.loadTexts: hpnicfVMAP2to2RowStatus.setDescription('Operation status of this table entry.')
mibBuilder.exportSymbols("HPN-ICF-VMAP-MIB", hpnicfVMAP1to1TranslatedVlan=hpnicfVMAP1to1TranslatedVlan, hpnicfVMAP1to1Vlan=hpnicfVMAP1to1Vlan, hpnicfVMAP1to2SingleRowStatus=hpnicfVMAP1to2SingleRowStatus, hpnicfVMAP1to2EndVlan=hpnicfVMAP1to2EndVlan, hpnicfVMAP2to2InnerVlan=hpnicfVMAP2to2InnerVlan, hpnicfVMAPNNIState=hpnicfVMAPNNIState, hpnicfVMAPNto1RangeRowStatus=hpnicfVMAPNto1RangeRowStatus, hpnicfVMAP2to2Entry=hpnicfVMAP2to2Entry, hpnicfVMAPNto1RangeTable=hpnicfVMAPNto1RangeTable, hpnicfVMAPNNITable=hpnicfVMAPNNITable, hpnicfVMAPNto1RangeEntry=hpnicfVMAPNto1RangeEntry, hpnicfVMAPNto1EndVlan=hpnicfVMAPNto1EndVlan, hpnicfVMAPNto1SingleRowStatus=hpnicfVMAPNto1SingleRowStatus, hpnicfVMAP1to2RangeEntry=hpnicfVMAP1to2RangeEntry, hpnicfVMAP1to2SingleEntry=hpnicfVMAP1to2SingleEntry, hpnicfVMAP2to2Table=hpnicfVMAP2to2Table, hpnicfVMAP1to1Table=hpnicfVMAP1to1Table, hpnicfVMAP1to1RowStatus=hpnicfVMAP1to1RowStatus, hpnicfVMAP1to2Vlan=hpnicfVMAP1to2Vlan, hpnicfVMAP1to2RangeRowStatus=hpnicfVMAP1to2RangeRowStatus, hpnicfVMAP1to2SingleNestedVlan=hpnicfVMAP1to2SingleNestedVlan, hpnicfVMAP1to2StartVlan=hpnicfVMAP1to2StartVlan, hpnicfVMAP2to2OuterVlan=hpnicfVMAP2to2OuterVlan, hpnicfVMAP1to2RangeNestedVlan=hpnicfVMAP1to2RangeNestedVlan, hpnicfVMAP1to2SingleTable=hpnicfVMAP1to2SingleTable, hpnicfVMAP1to2RangeTable=hpnicfVMAP1to2RangeTable, hpnicfVMAPNto1SingleTable=hpnicfVMAPNto1SingleTable, hpnicfVMAPNto1RangeTranslatedVlan=hpnicfVMAPNto1RangeTranslatedVlan, hpnicfVMAP2to2RowStatus=hpnicfVMAP2to2RowStatus, hpnicfVMAPNto1Vlan=hpnicfVMAPNto1Vlan, hpnicfVMAP2to2TranslatedOuterVlan=hpnicfVMAP2to2TranslatedOuterVlan, hpnicfVMAPNto1StartVlan=hpnicfVMAPNto1StartVlan, hpnicfVmap=hpnicfVmap, hpnicfVMAPNto1SingleTranslatedVlan=hpnicfVMAPNto1SingleTranslatedVlan, hpnicfVMAPNNIEntry=hpnicfVMAPNNIEntry, hpnicfVMAPNto1SingleEntry=hpnicfVMAPNto1SingleEntry, hpnicfVMAP1to1Entry=hpnicfVMAP1to1Entry, PYSNMP_MODULE_ID=hpnicfVmap, hpnicfVMAP2to2TranslatedInnerVlan=hpnicfVMAP2to2TranslatedInnerVlan)