#
# PySNMP MIB module CISCO-SIBU-FLASH-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/CISCO-SIBU-FLASH-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 17:55:16 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
OctetString, ObjectIdentifier, Integer = mibBuilder.importSymbols("ASN1", "OctetString", "ObjectIdentifier", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
SingleValueConstraint, ValueSizeConstraint, ConstraintsIntersection, ValueRangeConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "SingleValueConstraint", "ValueSizeConstraint", "ConstraintsIntersection", "ValueRangeConstraint", "ConstraintsUnion")
ciscoExperiment, = mibBuilder.importSymbols("CISCO-SMI", "ciscoExperiment")
ModuleCompliance, NotificationGroup, ObjectGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup", "ObjectGroup")
iso, Bits, IpAddress, NotificationType, ObjectIdentity, Gauge32, Integer32, Counter64, Unsigned32, TimeTicks, MibScalar, MibTable, MibTableRow, MibTableColumn, ModuleIdentity, MibIdentifier, Counter32 = mibBuilder.importSymbols("SNMPv2-SMI", "iso", "Bits", "IpAddress", "NotificationType", "ObjectIdentity", "Gauge32", "Integer32", "Counter64", "Unsigned32", "TimeTicks", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "ModuleIdentity", "MibIdentifier", "Counter32")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
ciscoSibuFlashMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 10, 45))
ciscoSibuFlashMIB.setRevisions(('1998-10-23 00:00',))
if mibBuilder.loadTexts: ciscoSibuFlashMIB.setLastUpdated('9810230000Z')
if mibBuilder.loadTexts: ciscoSibuFlashMIB.setOrganization('Cisco Systems Inc.')
ciscoSibuFlashMIBObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 10, 45, 1))
csfUpgrade = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 10, 45, 1, 1))
csfUpgradeFirmwareVersion = MibScalar((1, 3, 6, 1, 4, 1, 9, 10, 45, 1, 1, 1), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 8))).setMaxAccess("readonly")
if mibBuilder.loadTexts: csfUpgradeFirmwareVersion.setStatus('current')
csfUpgradeFlashSize = MibScalar((1, 3, 6, 1, 4, 1, 9, 10, 45, 1, 1, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 2147483647))).setUnits('kbytes').setMaxAccess("readonly")
if mibBuilder.loadTexts: csfUpgradeFlashSize.setStatus('current')
csfUpgradeTFTPServerAddress = MibScalar((1, 3, 6, 1, 4, 1, 9, 10, 45, 1, 1, 3), IpAddress().clone(hexValue="00000000")).setMaxAccess("readwrite")
if mibBuilder.loadTexts: csfUpgradeTFTPServerAddress.setStatus('current')
csfUpgradeTFTPLoadFilename = MibScalar((1, 3, 6, 1, 4, 1, 9, 10, 45, 1, 1, 4), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 80))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: csfUpgradeTFTPLoadFilename.setStatus('current')
csfUpgradeTFTPInitiate = MibScalar((1, 3, 6, 1, 4, 1, 9, 10, 45, 1, 1, 5), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("upgrade", 1), ("noUpgrade", 2))).clone('noUpgrade')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: csfUpgradeTFTPInitiate.setStatus('current')
csfUpgradeFlashMode = MibScalar((1, 3, 6, 1, 4, 1, 9, 10, 45, 1, 1, 6), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("permanent", 1), ("temporary", 2))).clone('permanent')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: csfUpgradeFlashMode.setStatus('current')
csfUpgradeFirmwareStatus = MibScalar((1, 3, 6, 1, 4, 1, 9, 10, 45, 1, 1, 7), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))).clone(namedValues=NamedValues(("none", 1), ("inProgress", 2), ("succeeded", 3), ("failed", 4))).clone('none')).setMaxAccess("readonly")
if mibBuilder.loadTexts: csfUpgradeFirmwareStatus.setStatus('current')
ciscoSibuFlashMIBNotificationsPrefix = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 10, 45, 2))
ciscoSibuFlashMIBNotifications = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 10, 45, 2, 0))
ciscoSibuFlashMIBComformance = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 10, 45, 3))
ciscoSibuFlashMIBCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 10, 45, 3, 1))
ciscoSibuFlashMIBGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 10, 45, 3, 2))
ciscoSibuFlashCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 9, 10, 45, 3, 1, 1)).setObjects(("CISCO-SIBU-FLASH-MIB", "ciscoSibuFlashMIBGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoSibuFlashCompliance = ciscoSibuFlashCompliance.setStatus('current')
ciscoSibuFlashMIBGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 10, 45, 3, 2, 1)).setObjects(("CISCO-SIBU-FLASH-MIB", "csfUpgradeFirmwareVersion"), ("CISCO-SIBU-FLASH-MIB", "csfUpgradeFlashSize"), ("CISCO-SIBU-FLASH-MIB", "csfUpgradeTFTPServerAddress"), ("CISCO-SIBU-FLASH-MIB", "csfUpgradeTFTPLoadFilename"), ("CISCO-SIBU-FLASH-MIB", "csfUpgradeTFTPInitiate"), ("CISCO-SIBU-FLASH-MIB", "csfUpgradeFlashMode"), ("CISCO-SIBU-FLASH-MIB", "csfUpgradeFirmwareStatus"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoSibuFlashMIBGroup = ciscoSibuFlashMIBGroup.setStatus('current')
mibBuilder.exportSymbols("CISCO-SIBU-FLASH-MIB", csfUpgrade=csfUpgrade, ciscoSibuFlashMIB=ciscoSibuFlashMIB, ciscoSibuFlashMIBObjects=ciscoSibuFlashMIBObjects, ciscoSibuFlashMIBComformance=ciscoSibuFlashMIBComformance, ciscoSibuFlashMIBGroups=ciscoSibuFlashMIBGroups, csfUpgradeFlashMode=csfUpgradeFlashMode, csfUpgradeTFTPServerAddress=csfUpgradeTFTPServerAddress, PYSNMP_MODULE_ID=ciscoSibuFlashMIB, csfUpgradeTFTPInitiate=csfUpgradeTFTPInitiate, ciscoSibuFlashMIBCompliances=ciscoSibuFlashMIBCompliances, ciscoSibuFlashMIBNotificationsPrefix=ciscoSibuFlashMIBNotificationsPrefix, ciscoSibuFlashCompliance=ciscoSibuFlashCompliance, csfUpgradeTFTPLoadFilename=csfUpgradeTFTPLoadFilename, csfUpgradeFirmwareVersion=csfUpgradeFirmwareVersion, csfUpgradeFlashSize=csfUpgradeFlashSize, csfUpgradeFirmwareStatus=csfUpgradeFirmwareStatus, ciscoSibuFlashMIBGroup=ciscoSibuFlashMIBGroup, ciscoSibuFlashMIBNotifications=ciscoSibuFlashMIBNotifications)