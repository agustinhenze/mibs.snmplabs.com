#
# PySNMP MIB module TOS-SYSINFO (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/TOS-SYSINFO
# Produced by pysmi-0.3.4 at Mon Apr 29 21:16:36 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsUnion, SingleValueConstraint, ValueSizeConstraint, ConstraintsIntersection, ValueRangeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "SingleValueConstraint", "ValueSizeConstraint", "ConstraintsIntersection", "ValueRangeConstraint")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
Gauge32, ModuleIdentity, Counter64, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter32, ObjectIdentity, Bits, Integer32, iso, TimeTicks, Opaque, MibIdentifier, IpAddress, Unsigned32, Gauge, NotificationType = mibBuilder.importSymbols("SNMPv2-SMI", "Gauge32", "ModuleIdentity", "Counter64", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter32", "ObjectIdentity", "Bits", "Integer32", "iso", "TimeTicks", "Opaque", "MibIdentifier", "IpAddress", "Unsigned32", "Gauge", "NotificationType")
DateAndTime, DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DateAndTime", "DisplayString", "TextualConvention")
tosMib, = mibBuilder.importSymbols("TOS-SMI", "tosMib")
sysInfo = ModuleIdentity((1, 3, 6, 1, 4, 1, 14331, 5, 5, 1, 3))
sysInfo.setRevisions(('1970-01-01 00:00', '1970-01-01 00:00', '1970-01-01 00:00', '1970-01-01 00:00', '1970-01-01 00:00',))
if mibBuilder.loadTexts: sysInfo.setLastUpdated('08-03-17')
if mibBuilder.loadTexts: sysInfo.setOrganization('TOPSEC')
sysProductSN = MibScalar((1, 3, 6, 1, 4, 1, 14331, 5, 5, 1, 3, 1), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 255))).setMaxAccess("readonly")
if mibBuilder.loadTexts: sysProductSN.setStatus('current')
sysProductType = MibScalar((1, 3, 6, 1, 4, 1, 14331, 5, 5, 1, 3, 2), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 255))).setMaxAccess("readonly")
if mibBuilder.loadTexts: sysProductType.setStatus('current')
sysSoftwareVersion = MibScalar((1, 3, 6, 1, 4, 1, 14331, 5, 5, 1, 3, 3), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 255))).setMaxAccess("readonly")
if mibBuilder.loadTexts: sysSoftwareVersion.setStatus('current')
sysHardwareId = MibScalar((1, 3, 6, 1, 4, 1, 14331, 5, 5, 1, 3, 4), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 255))).setMaxAccess("readonly")
if mibBuilder.loadTexts: sysHardwareId.setStatus('current')
sysSnmpVersion = MibScalar((1, 3, 6, 1, 4, 1, 14331, 5, 5, 1, 3, 5), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sysSnmpVersion.setStatus('current')
sysVpnEngine = MibScalar((1, 3, 6, 1, 4, 1, 14331, 5, 5, 1, 3, 6), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 255))).setMaxAccess("readonly")
if mibBuilder.loadTexts: sysVpnEngine.setStatus('current')
sysAntiVirusEngine = MibScalar((1, 3, 6, 1, 4, 1, 14331, 5, 5, 1, 3, 7), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 255))).setMaxAccess("readonly")
if mibBuilder.loadTexts: sysAntiVirusEngine.setStatus('current')
sysAntiVirusLibrary = MibScalar((1, 3, 6, 1, 4, 1, 14331, 5, 5, 1, 3, 8), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 255))).setMaxAccess("readonly")
if mibBuilder.loadTexts: sysAntiVirusLibrary.setStatus('current')
sysSecurityEngine = MibScalar((1, 3, 6, 1, 4, 1, 14331, 5, 5, 1, 3, 9), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 255))).setMaxAccess("readonly")
if mibBuilder.loadTexts: sysSecurityEngine.setStatus('current')
sysDpiSupport = MibScalar((1, 3, 6, 1, 4, 1, 14331, 5, 5, 1, 3, 10), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 255))).setMaxAccess("readonly")
if mibBuilder.loadTexts: sysDpiSupport.setStatus('current')
sysNatSupport = MibScalar((1, 3, 6, 1, 4, 1, 14331, 5, 5, 1, 3, 11), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 255))).setMaxAccess("readonly")
if mibBuilder.loadTexts: sysNatSupport.setStatus('current')
sysAuthenticationSupport = MibScalar((1, 3, 6, 1, 4, 1, 14331, 5, 5, 1, 3, 12), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 255))).setMaxAccess("readonly")
if mibBuilder.loadTexts: sysAuthenticationSupport.setStatus('current')
sysService = MibScalar((1, 3, 6, 1, 4, 1, 14331, 5, 5, 1, 3, 13), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 255))).setMaxAccess("readonly")
if mibBuilder.loadTexts: sysService.setStatus('current')
sysDynamicRoutingProtocol = MibScalar((1, 3, 6, 1, 4, 1, 14331, 5, 5, 1, 3, 14), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 255))).setMaxAccess("readonly")
if mibBuilder.loadTexts: sysDynamicRoutingProtocol.setStatus('current')
sysMaxSession = MibScalar((1, 3, 6, 1, 4, 1, 14331, 5, 5, 1, 3, 15), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sysMaxSession.setStatus('current')
sysMaxVrcClient = MibScalar((1, 3, 6, 1, 4, 1, 14331, 5, 5, 1, 3, 16), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sysMaxVrcClient.setStatus('current')
mibBuilder.exportSymbols("TOS-SYSINFO", sysVpnEngine=sysVpnEngine, sysMaxSession=sysMaxSession, sysAntiVirusLibrary=sysAntiVirusLibrary, sysInfo=sysInfo, sysDynamicRoutingProtocol=sysDynamicRoutingProtocol, sysSecurityEngine=sysSecurityEngine, sysNatSupport=sysNatSupport, sysProductSN=sysProductSN, sysSnmpVersion=sysSnmpVersion, sysMaxVrcClient=sysMaxVrcClient, sysAuthenticationSupport=sysAuthenticationSupport, sysAntiVirusEngine=sysAntiVirusEngine, PYSNMP_MODULE_ID=sysInfo, sysProductType=sysProductType, sysDpiSupport=sysDpiSupport, sysHardwareId=sysHardwareId, sysSoftwareVersion=sysSoftwareVersion, sysService=sysService)
