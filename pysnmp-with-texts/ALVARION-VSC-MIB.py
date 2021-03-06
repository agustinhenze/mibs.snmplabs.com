#
# PySNMP MIB module ALVARION-VSC-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/ALVARION-VSC-MIB
# Produced by pysmi-0.3.4 at Wed May  1 11:22:30 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
alvarionMgmtV2, = mibBuilder.importSymbols("ALVARION-SMI", "alvarionMgmtV2")
AlvarionSSID, = mibBuilder.importSymbols("ALVARION-TC", "AlvarionSSID")
OctetString, ObjectIdentifier, Integer = mibBuilder.importSymbols("ASN1", "OctetString", "ObjectIdentifier", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsIntersection, ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsIntersection", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion")
ObjectGroup, ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ObjectGroup", "ModuleCompliance", "NotificationGroup")
Bits, iso, Counter64, TimeTicks, MibScalar, MibTable, MibTableRow, MibTableColumn, Integer32, ObjectIdentity, NotificationType, Gauge32, IpAddress, MibIdentifier, ModuleIdentity, Unsigned32, Counter32 = mibBuilder.importSymbols("SNMPv2-SMI", "Bits", "iso", "Counter64", "TimeTicks", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Integer32", "ObjectIdentity", "NotificationType", "Gauge32", "IpAddress", "MibIdentifier", "ModuleIdentity", "Unsigned32", "Counter32")
TextualConvention, DisplayString, TruthValue = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString", "TruthValue")
alvarionVscMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 12394, 1, 10, 5, 22))
if mibBuilder.loadTexts: alvarionVscMIB.setLastUpdated('200710310000Z')
if mibBuilder.loadTexts: alvarionVscMIB.setOrganization('Alvarion Ltd.')
if mibBuilder.loadTexts: alvarionVscMIB.setContactInfo('Alvarion Ltd. Postal: 21a HaBarzel St. P.O. Box 13139 Tel-Aviv 69710 Israel Phone: +972 3 645 6262')
if mibBuilder.loadTexts: alvarionVscMIB.setDescription('Alvarion Virtual Service Communities MIB.')
alvarionVscMIBObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 12394, 1, 10, 5, 22, 1))
coVscConfigGroup = MibIdentifier((1, 3, 6, 1, 4, 1, 12394, 1, 10, 5, 22, 1, 1))
coVscConfigTable = MibTable((1, 3, 6, 1, 4, 1, 12394, 1, 10, 5, 22, 1, 1, 1), )
if mibBuilder.loadTexts: coVscConfigTable.setStatus('current')
if mibBuilder.loadTexts: coVscConfigTable.setDescription('Virtual Service Communities configuration attributes.')
coVscConfigEntry = MibTableRow((1, 3, 6, 1, 4, 1, 12394, 1, 10, 5, 22, 1, 1, 1, 1), ).setIndexNames((0, "ALVARION-VSC-MIB", "coVscCfgIndex"))
if mibBuilder.loadTexts: coVscConfigEntry.setStatus('current')
if mibBuilder.loadTexts: coVscConfigEntry.setDescription('An entry in the coVscConfigTable. coVscCfgIndex - Uniquely identify a Virtual Service Community on an Alvarion device.')
coVscCfgIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 12394, 1, 10, 5, 22, 1, 1, 1, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 2147483647)))
if mibBuilder.loadTexts: coVscCfgIndex.setStatus('current')
if mibBuilder.loadTexts: coVscCfgIndex.setDescription('Specifies the index of a Virtual Service Community (VSC) in the configuration file.')
coVscCfgFriendlyVscName = MibTableColumn((1, 3, 6, 1, 4, 1, 12394, 1, 10, 5, 22, 1, 1, 1, 1, 2), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: coVscCfgFriendlyVscName.setStatus('current')
if mibBuilder.loadTexts: coVscCfgFriendlyVscName.setDescription('The friendly name associated with the VSC.')
coVscCfgSSID = MibTableColumn((1, 3, 6, 1, 4, 1, 12394, 1, 10, 5, 22, 1, 1, 1, 1, 3), AlvarionSSID()).setMaxAccess("readonly")
if mibBuilder.loadTexts: coVscCfgSSID.setStatus('current')
if mibBuilder.loadTexts: coVscCfgSSID.setDescription('Service Set ID assigned to the VSC.')
coVscCfgAccessControlled = MibTableColumn((1, 3, 6, 1, 4, 1, 12394, 1, 10, 5, 22, 1, 1, 1, 1, 4), TruthValue()).setMaxAccess("readonly")
if mibBuilder.loadTexts: coVscCfgAccessControlled.setStatus('current')
if mibBuilder.loadTexts: coVscCfgAccessControlled.setDescription('Indicates if the VSC is access controlled.')
coVscCfgSecurity = MibTableColumn((1, 3, 6, 1, 4, 1, 12394, 1, 10, 5, 22, 1, 1, 1, 1, 5), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5))).clone(namedValues=NamedValues(("open", 1), ("ieee802dot1x", 2), ("wpa", 3), ("wpa2", 4), ("wpaAndWpa2", 5)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: coVscCfgSecurity.setStatus('current')
if mibBuilder.loadTexts: coVscCfgSecurity.setDescription('Indicates the type of security used by the VSC.')
coVscCfgEncryption = MibTableColumn((1, 3, 6, 1, 4, 1, 12394, 1, 10, 5, 22, 1, 1, 1, 1, 6), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5))).clone(namedValues=NamedValues(("none", 1), ("wep", 2), ("tkip", 3), ("aes", 4), ("tkipAndAes", 5)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: coVscCfgEncryption.setStatus('current')
if mibBuilder.loadTexts: coVscCfgEncryption.setDescription('Indicates the encryption type supported by the VSC.')
coVscCfg8021xAuthentication = MibTableColumn((1, 3, 6, 1, 4, 1, 12394, 1, 10, 5, 22, 1, 1, 1, 1, 7), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("none", 1), ("radius", 2), ("psk", 3)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: coVscCfg8021xAuthentication.setStatus('current')
if mibBuilder.loadTexts: coVscCfg8021xAuthentication.setDescription('Indicates the 802.1x authentication type supported by the VSC.')
coVscCfgMACAuthentication = MibTableColumn((1, 3, 6, 1, 4, 1, 12394, 1, 10, 5, 22, 1, 1, 1, 1, 8), TruthValue()).setMaxAccess("readonly")
if mibBuilder.loadTexts: coVscCfgMACAuthentication.setStatus('current')
if mibBuilder.loadTexts: coVscCfgMACAuthentication.setDescription('Indicates if MAC authentication is enabled on the VSC.')
coVscCfgHTMLAuthentication = MibTableColumn((1, 3, 6, 1, 4, 1, 12394, 1, 10, 5, 22, 1, 1, 1, 1, 9), TruthValue()).setMaxAccess("readonly")
if mibBuilder.loadTexts: coVscCfgHTMLAuthentication.setStatus('current')
if mibBuilder.loadTexts: coVscCfgHTMLAuthentication.setDescription('Indicates if HTML authentication is enabled on the VSC. Always false on a satellite.')
alvarionVscMIBConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 12394, 1, 10, 5, 22, 2))
alvarionVscMIBCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 12394, 1, 10, 5, 22, 2, 1))
alvarionVscMIBGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 12394, 1, 10, 5, 22, 2, 2))
alvarionVscMIBCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 12394, 1, 10, 5, 22, 2, 1, 1)).setObjects(("ALVARION-VSC-MIB", "alvarionVscMIBGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    alvarionVscMIBCompliance = alvarionVscMIBCompliance.setStatus('current')
if mibBuilder.loadTexts: alvarionVscMIBCompliance.setDescription('The compliance statement for the Virtual Service Communities MIB.')
alvarionVscMIBGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 12394, 1, 10, 5, 22, 2, 2, 1)).setObjects(("ALVARION-VSC-MIB", "coVscCfgFriendlyVscName"), ("ALVARION-VSC-MIB", "coVscCfgSSID"), ("ALVARION-VSC-MIB", "coVscCfgAccessControlled"), ("ALVARION-VSC-MIB", "coVscCfgSecurity"), ("ALVARION-VSC-MIB", "coVscCfgEncryption"), ("ALVARION-VSC-MIB", "coVscCfg8021xAuthentication"), ("ALVARION-VSC-MIB", "coVscCfgMACAuthentication"), ("ALVARION-VSC-MIB", "coVscCfgHTMLAuthentication"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    alvarionVscMIBGroup = alvarionVscMIBGroup.setStatus('current')
if mibBuilder.loadTexts: alvarionVscMIBGroup.setDescription('A collection of objects for the wireless interface status.')
mibBuilder.exportSymbols("ALVARION-VSC-MIB", coVscCfgSecurity=coVscCfgSecurity, alvarionVscMIBGroup=alvarionVscMIBGroup, coVscCfgSSID=coVscCfgSSID, coVscCfg8021xAuthentication=coVscCfg8021xAuthentication, alvarionVscMIBCompliance=alvarionVscMIBCompliance, coVscCfgAccessControlled=coVscCfgAccessControlled, coVscCfgMACAuthentication=coVscCfgMACAuthentication, PYSNMP_MODULE_ID=alvarionVscMIB, coVscCfgIndex=coVscCfgIndex, alvarionVscMIBGroups=alvarionVscMIBGroups, coVscCfgFriendlyVscName=coVscCfgFriendlyVscName, alvarionVscMIBConformance=alvarionVscMIBConformance, coVscCfgEncryption=coVscCfgEncryption, coVscCfgHTMLAuthentication=coVscCfgHTMLAuthentication, coVscConfigTable=coVscConfigTable, alvarionVscMIBObjects=alvarionVscMIBObjects, coVscConfigGroup=coVscConfigGroup, alvarionVscMIB=alvarionVscMIB, alvarionVscMIBCompliances=alvarionVscMIBCompliances, coVscConfigEntry=coVscConfigEntry)
