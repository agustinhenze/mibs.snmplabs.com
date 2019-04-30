#
# PySNMP MIB module CISCOSB-LOCALIZATION-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/CISCOSB-LOCALIZATION-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 18:06:55 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
ObjectIdentifier, Integer, OctetString = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "Integer", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ConstraintsUnion, ValueSizeConstraint, SingleValueConstraint, ValueRangeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ConstraintsUnion", "ValueSizeConstraint", "SingleValueConstraint", "ValueRangeConstraint")
switch001, = mibBuilder.importSymbols("CISCOSB-MIB", "switch001")
SnmpAdminString, = mibBuilder.importSymbols("SNMP-FRAMEWORK-MIB", "SnmpAdminString")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
ModuleIdentity, iso, Unsigned32, ObjectIdentity, NotificationType, MibScalar, MibTable, MibTableRow, MibTableColumn, Gauge32, Integer32, Bits, Counter64, TimeTicks, MibIdentifier, IpAddress, Counter32 = mibBuilder.importSymbols("SNMPv2-SMI", "ModuleIdentity", "iso", "Unsigned32", "ObjectIdentity", "NotificationType", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Gauge32", "Integer32", "Bits", "Counter64", "TimeTicks", "MibIdentifier", "IpAddress", "Counter32")
TextualConvention, RowStatus, DisplayString, TruthValue = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "RowStatus", "DisplayString", "TruthValue")
rlLocalization = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 103))
rlLocalization.setRevisions(('2005-03-15 00:00',))
if mibBuilder.loadTexts: rlLocalization.setLastUpdated('200503150000Z')
if mibBuilder.loadTexts: rlLocalization.setOrganization('Cisco Small Business')
rlLocalizationActivelanguage = MibScalar((1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 103, 8), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 50))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rlLocalizationActivelanguage.setStatus('current')
rlLocalizationLoginlanguage = MibScalar((1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 103, 9), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rlLocalizationLoginlanguage.setStatus('current')
rlLocalizationLanguagesTable = MibTable((1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 103, 10), )
if mibBuilder.loadTexts: rlLocalizationLanguagesTable.setStatus('current')
rlLocalizationLanguagesEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 103, 10, 1), ).setIndexNames((1, "CISCOSB-LOCALIZATION-MIB", "rlLocalizationLanguagesName"))
if mibBuilder.loadTexts: rlLocalizationLanguagesEntry.setStatus('current')
rlLocalizationLanguagesName = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 103, 10, 1, 1), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(1, 50)))
if mibBuilder.loadTexts: rlLocalizationLanguagesName.setStatus('current')
rlLocalizationLanguagesUnicodeName = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 103, 10, 1, 2), SnmpAdminString().subtype(subtypeSpec=ValueSizeConstraint(1, 64))).setMaxAccess("readonly")
if mibBuilder.loadTexts: rlLocalizationLanguagesUnicodeName.setStatus('current')
rlLocalizationLanguagesUrlDir = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 103, 10, 1, 3), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rlLocalizationLanguagesUrlDir.setStatus('current')
rlLocalizationLanguagesUrlHelpDir = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 103, 10, 1, 4), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rlLocalizationLanguagesUrlHelpDir.setStatus('current')
rlLocalizationLanguageCode = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 103, 10, 1, 5), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rlLocalizationLanguageCode.setStatus('current')
rlLocalizationNumOfSections = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 103, 10, 1, 6), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 100))).setMaxAccess("readonly")
if mibBuilder.loadTexts: rlLocalizationNumOfSections.setStatus('current')
rlLocalizationNumOfEmbSections = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 103, 10, 1, 7), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 100))).setMaxAccess("readonly")
if mibBuilder.loadTexts: rlLocalizationNumOfEmbSections.setStatus('current')
rlLocalizationVersion = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 103, 10, 1, 8), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 15))).setMaxAccess("readonly")
if mibBuilder.loadTexts: rlLocalizationVersion.setStatus('current')
rlLocalizationMd5ChksumFile = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 103, 10, 1, 9), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rlLocalizationMd5ChksumFile.setStatus('current')
mibBuilder.exportSymbols("CISCOSB-LOCALIZATION-MIB", rlLocalizationLanguageCode=rlLocalizationLanguageCode, rlLocalizationVersion=rlLocalizationVersion, rlLocalization=rlLocalization, rlLocalizationLoginlanguage=rlLocalizationLoginlanguage, rlLocalizationLanguagesEntry=rlLocalizationLanguagesEntry, rlLocalizationMd5ChksumFile=rlLocalizationMd5ChksumFile, PYSNMP_MODULE_ID=rlLocalization, rlLocalizationActivelanguage=rlLocalizationActivelanguage, rlLocalizationLanguagesName=rlLocalizationLanguagesName, rlLocalizationLanguagesUrlDir=rlLocalizationLanguagesUrlDir, rlLocalizationLanguagesUnicodeName=rlLocalizationLanguagesUnicodeName, rlLocalizationLanguagesUrlHelpDir=rlLocalizationLanguagesUrlHelpDir, rlLocalizationNumOfEmbSections=rlLocalizationNumOfEmbSections, rlLocalizationLanguagesTable=rlLocalizationLanguagesTable, rlLocalizationNumOfSections=rlLocalizationNumOfSections)