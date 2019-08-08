#
# PySNMP MIB module CIENA-WS-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/CIENA-WS-MIB
# Produced by pysmi-0.3.4 at Wed May  1 11:49:30 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
OctetString, ObjectIdentifier, Integer = mibBuilder.importSymbols("ASN1", "OctetString", "ObjectIdentifier", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, ConstraintsUnion, ValueSizeConstraint, SingleValueConstraint, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "ConstraintsUnion", "ValueSizeConstraint", "SingleValueConstraint", "ConstraintsIntersection")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
IpAddress, Gauge32, iso, Bits, NotificationType, Unsigned32, ObjectIdentity, Counter64, MibIdentifier, enterprises, TimeTicks, ModuleIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, Integer32, Counter32 = mibBuilder.importSymbols("SNMPv2-SMI", "IpAddress", "Gauge32", "iso", "Bits", "NotificationType", "Unsigned32", "ObjectIdentity", "Counter64", "MibIdentifier", "enterprises", "TimeTicks", "ModuleIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Integer32", "Counter32")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
ciena = ModuleIdentity((1, 3, 6, 1, 4, 1, 1271))
ciena.setRevisions(('2010-09-27 23:17', '2016-07-07 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: ciena.setRevisionsDescriptions(('Initial creation of MIB file structure for Ciena.', 'String clean-up and addition of version node for release 1.2.',))
if mibBuilder.loadTexts: ciena.setLastUpdated('201009272317Z')
if mibBuilder.loadTexts: ciena.setOrganization('Ciena Corporation')
if mibBuilder.loadTexts: ciena.setContactInfo('Web: http://www.ciena.com Postal: 7035 Ridge Road Hanover, Maryland 21076 U.S.A Phone: +1 800-921-1144 Fax: +1 410-694-5750')
if mibBuilder.loadTexts: ciena.setDescription("Top-level MIB structure for Ciena's Waveserver.")
waveserver = ObjectIdentity((1, 3, 6, 1, 4, 1, 1271, 3))
if mibBuilder.loadTexts: waveserver.setStatus('current')
if mibBuilder.loadTexts: waveserver.setDescription("Root identifier for Ciena's Waveserver product.")
cienaWsStatistics = ObjectIdentity((1, 3, 6, 1, 4, 1, 1271, 3, 3))
if mibBuilder.loadTexts: cienaWsStatistics.setStatus('obsolete')
if mibBuilder.loadTexts: cienaWsStatistics.setDescription('Statistics for Waveserver.')
cienaWsNotifications = ObjectIdentity((1, 3, 6, 1, 4, 1, 1271, 3, 2))
if mibBuilder.loadTexts: cienaWsNotifications.setStatus('current')
if mibBuilder.loadTexts: cienaWsNotifications.setDescription('Waveserver notifications.')
cienaWsNotificationsControlModule = ObjectIdentity((1, 3, 6, 1, 4, 1, 1271, 3, 2, 1))
if mibBuilder.loadTexts: cienaWsNotificationsControlModule.setStatus('current')
if mibBuilder.loadTexts: cienaWsNotificationsControlModule.setDescription('Waveserver control module.')
cienaWsConfigV1 = ObjectIdentity((1, 3, 6, 1, 4, 1, 1271, 3, 1))
if mibBuilder.loadTexts: cienaWsConfigV1.setStatus('current')
if mibBuilder.loadTexts: cienaWsConfigV1.setDescription('Configuration for the Waveserver 1.0 and 1.1 releases.')
cienaWsConfig = ObjectIdentity((1, 3, 6, 1, 4, 1, 1271, 3, 4))
if mibBuilder.loadTexts: cienaWsConfig.setStatus('current')
if mibBuilder.loadTexts: cienaWsConfig.setDescription('Root object for the Waveserver API in 1.2 and beyond.')
mibBuilder.exportSymbols("CIENA-WS-MIB", PYSNMP_MODULE_ID=ciena, cienaWsNotificationsControlModule=cienaWsNotificationsControlModule, waveserver=waveserver, cienaWsNotifications=cienaWsNotifications, ciena=ciena, cienaWsConfigV1=cienaWsConfigV1, cienaWsConfig=cienaWsConfig, cienaWsStatistics=cienaWsStatistics)