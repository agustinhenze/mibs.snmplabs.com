#
# PySNMP MIB module ZHONE-RADIUS-CLIENT (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/ZHONE-RADIUS-CLIENT
# Produced by pysmi-0.3.4 at Mon Apr 29 21:41:43 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
OctetString, ObjectIdentifier, Integer = mibBuilder.importSymbols("ASN1", "OctetString", "ObjectIdentifier", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, SingleValueConstraint, ConstraintsIntersection, ValueSizeConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsIntersection", "ValueSizeConstraint", "ConstraintsUnion")
ifIndex, = mibBuilder.importSymbols("IF-MIB", "ifIndex")
ModuleCompliance, ObjectGroup, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "ObjectGroup", "NotificationGroup")
Bits, TimeTicks, Counter64, IpAddress, ObjectIdentity, Unsigned32, iso, Counter32, Gauge32, NotificationType, MibScalar, MibTable, MibTableRow, MibTableColumn, ModuleIdentity, MibIdentifier, Integer32 = mibBuilder.importSymbols("SNMPv2-SMI", "Bits", "TimeTicks", "Counter64", "IpAddress", "ObjectIdentity", "Unsigned32", "iso", "Counter32", "Gauge32", "NotificationType", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "ModuleIdentity", "MibIdentifier", "Integer32")
DisplayString, RowStatus, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "RowStatus", "TextualConvention")
zhoneRadius, zhoneModules = mibBuilder.importSymbols("Zhone", "zhoneRadius", "zhoneModules")
comRadiusClient = ModuleIdentity((1, 3, 6, 1, 4, 1, 5504, 6, 112))
comRadiusClient.setRevisions(('2006-11-15 14:07',))
if mibBuilder.loadTexts: comRadiusClient.setLastUpdated('200611151230Z')
if mibBuilder.loadTexts: comRadiusClient.setOrganization('Zhone Technologies, Inc.')
zhoneRadiusClient = ObjectIdentity((1, 3, 6, 1, 4, 1, 5504, 4, 14, 1))
if mibBuilder.loadTexts: zhoneRadiusClient.setStatus('current')
zhoneRadiusClientTable = MibTable((1, 3, 6, 1, 4, 1, 5504, 4, 14, 1, 1), )
if mibBuilder.loadTexts: zhoneRadiusClientTable.setStatus('current')
zhoneRadiusClientEntry = MibTableRow((1, 3, 6, 1, 4, 1, 5504, 4, 14, 1, 1, 1), ).setIndexNames((0, "ZHONE-RADIUS-CLIENT", "zhoneRadiusClientIndex"), (0, "ZHONE-RADIUS-CLIENT", "zhoneRadiusClientId"))
if mibBuilder.loadTexts: zhoneRadiusClientEntry.setStatus('current')
zhoneRadiusClientIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 5504, 4, 14, 1, 1, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 2137483647)))
if mibBuilder.loadTexts: zhoneRadiusClientIndex.setStatus('current')
zhoneRadiusClientId = MibTableColumn((1, 3, 6, 1, 4, 1, 5504, 4, 14, 1, 1, 1, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 2137483647)))
if mibBuilder.loadTexts: zhoneRadiusClientId.setStatus('current')
zhoneRadiusClientRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 5504, 4, 14, 1, 1, 1, 3), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: zhoneRadiusClientRowStatus.setStatus('current')
zhoneRadiusClientServerName = MibTableColumn((1, 3, 6, 1, 4, 1, 5504, 4, 14, 1, 1, 1, 4), DisplayString()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: zhoneRadiusClientServerName.setStatus('current')
zhoneRadiusClientUdpPortNumber = MibTableColumn((1, 3, 6, 1, 4, 1, 5504, 4, 14, 1, 1, 1, 5), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 65535)).clone(1812)).setMaxAccess("readcreate")
if mibBuilder.loadTexts: zhoneRadiusClientUdpPortNumber.setStatus('current')
zhoneRadiusClientSharedSecret = MibTableColumn((1, 3, 6, 1, 4, 1, 5504, 4, 14, 1, 1, 1, 6), DisplayString()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: zhoneRadiusClientSharedSecret.setStatus('current')
zhoneRadiusClientRetryCount = MibTableColumn((1, 3, 6, 1, 4, 1, 5504, 4, 14, 1, 1, 1, 7), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 255)).clone(5)).setMaxAccess("readcreate")
if mibBuilder.loadTexts: zhoneRadiusClientRetryCount.setStatus('current')
zhoneRadiusClientRetryInterval = MibTableColumn((1, 3, 6, 1, 4, 1, 5504, 4, 14, 1, 1, 1, 8), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 60)).clone(1)).setMaxAccess("readcreate")
if mibBuilder.loadTexts: zhoneRadiusClientRetryInterval.setStatus('current')
zhoneRadiusObjectGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 5504, 4, 14, 2)).setObjects(("ZHONE-RADIUS-CLIENT", "zhoneRadiusClientServerName"), ("ZHONE-RADIUS-CLIENT", "zhoneRadiusClientUdpPortNumber"), ("ZHONE-RADIUS-CLIENT", "zhoneRadiusClientSharedSecret"), ("ZHONE-RADIUS-CLIENT", "zhoneRadiusClientRetryCount"), ("ZHONE-RADIUS-CLIENT", "zhoneRadiusClientRetryInterval"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    zhoneRadiusObjectGroup = zhoneRadiusObjectGroup.setStatus('current')
mibBuilder.exportSymbols("ZHONE-RADIUS-CLIENT", zhoneRadiusClientUdpPortNumber=zhoneRadiusClientUdpPortNumber, zhoneRadiusClientSharedSecret=zhoneRadiusClientSharedSecret, zhoneRadiusClientId=zhoneRadiusClientId, zhoneRadiusClientServerName=zhoneRadiusClientServerName, zhoneRadiusClientRetryInterval=zhoneRadiusClientRetryInterval, zhoneRadiusObjectGroup=zhoneRadiusObjectGroup, zhoneRadiusClientIndex=zhoneRadiusClientIndex, zhoneRadiusClientRowStatus=zhoneRadiusClientRowStatus, zhoneRadiusClientTable=zhoneRadiusClientTable, comRadiusClient=comRadiusClient, zhoneRadiusClientRetryCount=zhoneRadiusClientRetryCount, zhoneRadiusClient=zhoneRadiusClient, zhoneRadiusClientEntry=zhoneRadiusClientEntry, PYSNMP_MODULE_ID=comRadiusClient)
