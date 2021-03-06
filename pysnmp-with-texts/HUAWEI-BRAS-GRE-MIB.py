#
# PySNMP MIB module HUAWEI-BRAS-GRE-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/HUAWEI-BRAS-GRE-MIB
# Produced by pysmi-0.3.4 at Wed May  1 13:43:12 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
OctetString, Integer, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "OctetString", "Integer", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion, ValueSizeConstraint, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion", "ValueSizeConstraint", "ConstraintsIntersection")
hwBRASMib, = mibBuilder.importSymbols("HUAWEI-MIB", "hwBRASMib")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
Unsigned32, MibIdentifier, ModuleIdentity, ObjectIdentity, Integer32, Bits, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter64, NotificationType, iso, IpAddress, Gauge32, Counter32, TimeTicks = mibBuilder.importSymbols("SNMPv2-SMI", "Unsigned32", "MibIdentifier", "ModuleIdentity", "ObjectIdentity", "Integer32", "Bits", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter64", "NotificationType", "iso", "IpAddress", "Gauge32", "Counter32", "TimeTicks")
TextualConvention, RowStatus, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "RowStatus", "DisplayString")
hwGRE = ModuleIdentity((1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 13))
if mibBuilder.loadTexts: hwGRE.setLastUpdated('200508101200Z')
if mibBuilder.loadTexts: hwGRE.setOrganization('HAUWEI MIB Standard community. ')
if mibBuilder.loadTexts: hwGRE.setContactInfo('Floor 5, Block 4, R&D Building, Huawei Longgang Production Base, Shenzhen, P.R.C. http://www.huawei.com Zip:518057 ')
if mibBuilder.loadTexts: hwGRE.setDescription('V1.00. The GRE mib is for all datacomm product. ')
hwhwGREMibObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 13, 1))
hwQueryGreGroupTable = MibTable((1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 13, 1, 1), )
if mibBuilder.loadTexts: hwQueryGreGroupTable.setStatus('current')
hwQueryGreGroupEntry = MibTableRow((1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 13, 1, 1, 1), ).setIndexNames((0, "HUAWEI-BRAS-GRE-MIB", "hwQueryGreGroupName"))
if mibBuilder.loadTexts: hwQueryGreGroupEntry.setStatus('current')
if mibBuilder.loadTexts: hwQueryGreGroupEntry.setDescription('An entry of hwQueryGreGroupTable.')
hwQueryGreGroupName = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 13, 1, 1, 1, 1), OctetString().subtype(subtypeSpec=ValueSizeConstraint(1, 32))).setMaxAccess("readonly")
if mibBuilder.loadTexts: hwQueryGreGroupName.setStatus('current')
if mibBuilder.loadTexts: hwQueryGreGroupName.setDescription('The name of the gre-group.')
hwQueryGreGroupCounter = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 13, 1, 1, 1, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 4))).setMaxAccess("readonly")
if mibBuilder.loadTexts: hwQueryGreGroupCounter.setStatus('current')
if mibBuilder.loadTexts: hwQueryGreGroupCounter.setDescription('The number of interfaces that the gre-group bound.')
hwQueryGreGroupActiveTunnel = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 13, 1, 1, 1, 3), OctetString().subtype(subtypeSpec=ValueSizeConstraint(0, 64))).setMaxAccess("readonly")
if mibBuilder.loadTexts: hwQueryGreGroupActiveTunnel.setStatus('current')
if mibBuilder.loadTexts: hwQueryGreGroupActiveTunnel.setDescription('The name of the active tunnel of the gre-group.')
hwQueryGreGroupTunnel1Name = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 13, 1, 1, 1, 4), OctetString().subtype(subtypeSpec=ValueSizeConstraint(0, 64))).setMaxAccess("readonly")
if mibBuilder.loadTexts: hwQueryGreGroupTunnel1Name.setStatus('current')
if mibBuilder.loadTexts: hwQueryGreGroupTunnel1Name.setDescription('The name of the first tunnel of the gre-group.')
hwQueryGreGroupTunnel2Name = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 13, 1, 1, 1, 5), OctetString().subtype(subtypeSpec=ValueSizeConstraint(0, 64))).setMaxAccess("readonly")
if mibBuilder.loadTexts: hwQueryGreGroupTunnel2Name.setStatus('current')
if mibBuilder.loadTexts: hwQueryGreGroupTunnel2Name.setDescription('The name of the second tunnel of the gre-group.')
hwQueryGreGroupTunnel3Name = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 13, 1, 1, 1, 6), OctetString().subtype(subtypeSpec=ValueSizeConstraint(0, 64))).setMaxAccess("readonly")
if mibBuilder.loadTexts: hwQueryGreGroupTunnel3Name.setStatus('current')
if mibBuilder.loadTexts: hwQueryGreGroupTunnel3Name.setDescription('The name of the third tunnel of the gre-group.')
hwQueryGreGroupTunnel4Name = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 13, 1, 1, 1, 7), OctetString().subtype(subtypeSpec=ValueSizeConstraint(0, 64))).setMaxAccess("readonly")
if mibBuilder.loadTexts: hwQueryGreGroupTunnel4Name.setStatus('current')
if mibBuilder.loadTexts: hwQueryGreGroupTunnel4Name.setDescription('The name of the fourth tunnel of the gre-group.')
hwQueryGreGroupTunnel1Preference = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 13, 1, 1, 1, 8), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 4294967295))).setMaxAccess("readonly")
if mibBuilder.loadTexts: hwQueryGreGroupTunnel1Preference.setStatus('current')
if mibBuilder.loadTexts: hwQueryGreGroupTunnel1Preference.setDescription('The preference of the first tunnel.')
hwQueryGreGroupTunnel2Preference = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 13, 1, 1, 1, 9), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 4294967295))).setMaxAccess("readonly")
if mibBuilder.loadTexts: hwQueryGreGroupTunnel2Preference.setStatus('current')
if mibBuilder.loadTexts: hwQueryGreGroupTunnel2Preference.setDescription('The preference of the second tunnel.')
hwQueryGreGroupTunnel3Preference = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 13, 1, 1, 1, 10), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 4294967295))).setMaxAccess("readonly")
if mibBuilder.loadTexts: hwQueryGreGroupTunnel3Preference.setStatus('current')
if mibBuilder.loadTexts: hwQueryGreGroupTunnel3Preference.setDescription('The preference of the third tunnel.')
hwQueryGreGroupTunnel4Preference = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 13, 1, 1, 1, 11), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 4294967295))).setMaxAccess("readonly")
if mibBuilder.loadTexts: hwQueryGreGroupTunnel4Preference.setStatus('current')
if mibBuilder.loadTexts: hwQueryGreGroupTunnel4Preference.setDescription('The preference of the fourth tunnel.')
hwQueryGreConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 13, 2))
hwQueryGreCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 13, 2, 1))
hwQueryGreCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 13, 2, 1, 1)).setObjects(("HUAWEI-BRAS-GRE-MIB", "hwQueryGrePolicyGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    hwQueryGreCompliance = hwQueryGreCompliance.setStatus('current')
if mibBuilder.loadTexts: hwQueryGreCompliance.setDescription('The compliance statement for systems supporting the this module.')
hwQueryGreGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 13, 2, 2))
hwQueryGrePolicyGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 13, 2, 2, 1)).setObjects(("HUAWEI-BRAS-GRE-MIB", "hwQueryGreGroupName"), ("HUAWEI-BRAS-GRE-MIB", "hwQueryGreGroupCounter"), ("HUAWEI-BRAS-GRE-MIB", "hwQueryGreGroupActiveTunnel"), ("HUAWEI-BRAS-GRE-MIB", "hwQueryGreGroupTunnel1Name"), ("HUAWEI-BRAS-GRE-MIB", "hwQueryGreGroupTunnel2Name"), ("HUAWEI-BRAS-GRE-MIB", "hwQueryGreGroupTunnel3Name"), ("HUAWEI-BRAS-GRE-MIB", "hwQueryGreGroupTunnel4Name"), ("HUAWEI-BRAS-GRE-MIB", "hwQueryGreGroupTunnel1Preference"), ("HUAWEI-BRAS-GRE-MIB", "hwQueryGreGroupTunnel2Preference"), ("HUAWEI-BRAS-GRE-MIB", "hwQueryGreGroupTunnel3Preference"), ("HUAWEI-BRAS-GRE-MIB", "hwQueryGreGroupTunnel4Preference"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    hwQueryGrePolicyGroup = hwQueryGrePolicyGroup.setStatus('current')
if mibBuilder.loadTexts: hwQueryGrePolicyGroup.setDescription('The query gre policy group.')
mibBuilder.exportSymbols("HUAWEI-BRAS-GRE-MIB", hwQueryGreGroupTable=hwQueryGreGroupTable, hwQueryGreGroupActiveTunnel=hwQueryGreGroupActiveTunnel, hwQueryGreGroups=hwQueryGreGroups, hwQueryGrePolicyGroup=hwQueryGrePolicyGroup, hwhwGREMibObjects=hwhwGREMibObjects, hwQueryGreGroupTunnel1Name=hwQueryGreGroupTunnel1Name, hwQueryGreGroupTunnel4Preference=hwQueryGreGroupTunnel4Preference, hwQueryGreGroupCounter=hwQueryGreGroupCounter, hwQueryGreGroupTunnel2Name=hwQueryGreGroupTunnel2Name, hwQueryGreGroupName=hwQueryGreGroupName, hwQueryGreGroupTunnel4Name=hwQueryGreGroupTunnel4Name, PYSNMP_MODULE_ID=hwGRE, hwQueryGreCompliance=hwQueryGreCompliance, hwQueryGreGroupTunnel2Preference=hwQueryGreGroupTunnel2Preference, hwQueryGreGroupTunnel3Preference=hwQueryGreGroupTunnel3Preference, hwGRE=hwGRE, hwQueryGreGroupTunnel3Name=hwQueryGreGroupTunnel3Name, hwQueryGreConformance=hwQueryGreConformance, hwQueryGreGroupTunnel1Preference=hwQueryGreGroupTunnel1Preference, hwQueryGreCompliances=hwQueryGreCompliances, hwQueryGreGroupEntry=hwQueryGreGroupEntry)
