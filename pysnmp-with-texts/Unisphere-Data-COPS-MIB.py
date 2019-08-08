#
# PySNMP MIB module Unisphere-Data-COPS-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/Unisphere-Data-COPS-MIB
# Produced by pysmi-0.3.4 at Wed May  1 15:30:43 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
ObjectIdentifier, Integer, OctetString = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "Integer", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, ConstraintsUnion, SingleValueConstraint, ValueSizeConstraint, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "ConstraintsUnion", "SingleValueConstraint", "ValueSizeConstraint", "ConstraintsIntersection")
ObjectGroup, NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "ObjectGroup", "NotificationGroup", "ModuleCompliance")
Bits, Counter32, iso, MibScalar, MibTable, MibTableRow, MibTableColumn, ModuleIdentity, NotificationType, Gauge32, Counter64, MibIdentifier, TimeTicks, IpAddress, Unsigned32, ObjectIdentity, Integer32 = mibBuilder.importSymbols("SNMPv2-SMI", "Bits", "Counter32", "iso", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "ModuleIdentity", "NotificationType", "Gauge32", "Counter64", "MibIdentifier", "TimeTicks", "IpAddress", "Unsigned32", "ObjectIdentity", "Integer32")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
usDataMibs, = mibBuilder.importSymbols("Unisphere-Data-MIBs", "usDataMibs")
UsdName, = mibBuilder.importSymbols("Unisphere-Data-TC", "UsdName")
usdCopsProtocolMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 4874, 2, 2, 37))
usdCopsProtocolMIB.setRevisions(('2002-01-14 19:01', '2000-02-22 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: usdCopsProtocolMIB.setRevisionsDescriptions(('Expanded MIB to include following objects: usdCopsProtocolSessionLocalAddress, usdCopsProtocolSessionTransportRouterName ', 'Initial version of this MIB module.',))
if mibBuilder.loadTexts: usdCopsProtocolMIB.setLastUpdated('200201141901Z')
if mibBuilder.loadTexts: usdCopsProtocolMIB.setOrganization('Unisphere Networks, Inc.')
if mibBuilder.loadTexts: usdCopsProtocolMIB.setContactInfo(' Unisphere Networks, Inc. Postal: 10 Technology Park Drive Westford, MA 01886 USA Tel: +1 978 589 5800 Email: mib@UnisphereNetworks.com')
if mibBuilder.loadTexts: usdCopsProtocolMIB.setDescription('The Common Open Policy Service (COPS) Protocol MIB for the Unisphere Networks enterprise.')
usdCopsProtocolObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 4874, 2, 2, 37, 1))
usdCopsProtocolCfg = MibIdentifier((1, 3, 6, 1, 4, 1, 4874, 2, 2, 37, 1, 1))
usdCopsProtocolStatus = MibIdentifier((1, 3, 6, 1, 4, 1, 4874, 2, 2, 37, 1, 2))
usdCopsProtocolStatistics = MibIdentifier((1, 3, 6, 1, 4, 1, 4874, 2, 2, 37, 1, 3))
usdCopsProtocolSession = MibIdentifier((1, 3, 6, 1, 4, 1, 4874, 2, 2, 37, 1, 4))
usdCopsProtocolStatisticsScalars = MibIdentifier((1, 3, 6, 1, 4, 1, 4874, 2, 2, 37, 1, 3, 1))
usdCopsProtocolSessionsCreated = MibScalar((1, 3, 6, 1, 4, 1, 4874, 2, 2, 37, 1, 3, 1, 1), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: usdCopsProtocolSessionsCreated.setStatus('current')
if mibBuilder.loadTexts: usdCopsProtocolSessionsCreated.setDescription('Total number of COPS protocol sessions created.')
usdCopsProtocolSessionsDeleted = MibScalar((1, 3, 6, 1, 4, 1, 4874, 2, 2, 37, 1, 3, 1, 2), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: usdCopsProtocolSessionsDeleted.setStatus('current')
if mibBuilder.loadTexts: usdCopsProtocolSessionsDeleted.setDescription('The number of COPS protocol sessions deleted.')
usdCopsProtocolCurrentSessions = MibScalar((1, 3, 6, 1, 4, 1, 4874, 2, 2, 37, 1, 3, 1, 3), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: usdCopsProtocolCurrentSessions.setStatus('current')
if mibBuilder.loadTexts: usdCopsProtocolCurrentSessions.setDescription('The number of current COPS protocol sessions.')
usdCopsProtocolBytesReceived = MibScalar((1, 3, 6, 1, 4, 1, 4874, 2, 2, 37, 1, 3, 1, 4), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: usdCopsProtocolBytesReceived.setStatus('current')
if mibBuilder.loadTexts: usdCopsProtocolBytesReceived.setDescription('The number of bytes received by the COPS protocol layer.')
usdCopsProtocolPacketsReceived = MibScalar((1, 3, 6, 1, 4, 1, 4874, 2, 2, 37, 1, 3, 1, 5), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: usdCopsProtocolPacketsReceived.setStatus('current')
if mibBuilder.loadTexts: usdCopsProtocolPacketsReceived.setDescription('The number of packets received by the COPS protocol layer.')
usdCopsProtocolBytesSent = MibScalar((1, 3, 6, 1, 4, 1, 4874, 2, 2, 37, 1, 3, 1, 6), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: usdCopsProtocolBytesSent.setStatus('current')
if mibBuilder.loadTexts: usdCopsProtocolBytesSent.setDescription('The number of bytes sent by the COPS protocol layer.')
usdCopsProtocolPacketsSent = MibScalar((1, 3, 6, 1, 4, 1, 4874, 2, 2, 37, 1, 3, 1, 7), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: usdCopsProtocolPacketsSent.setStatus('current')
if mibBuilder.loadTexts: usdCopsProtocolPacketsSent.setDescription('The number of packets sent by the COPS protocol layer.')
usdCopsProtocolKeepAlivesReceived = MibScalar((1, 3, 6, 1, 4, 1, 4874, 2, 2, 37, 1, 3, 1, 8), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: usdCopsProtocolKeepAlivesReceived.setStatus('current')
if mibBuilder.loadTexts: usdCopsProtocolKeepAlivesReceived.setDescription('The number keep alive packets received by the COPS protocol layer.')
usdCopsProtocolKeepAlivesSent = MibScalar((1, 3, 6, 1, 4, 1, 4874, 2, 2, 37, 1, 3, 1, 9), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: usdCopsProtocolKeepAlivesSent.setStatus('current')
if mibBuilder.loadTexts: usdCopsProtocolKeepAlivesSent.setDescription('The number of keep alive packets sent by the COPS protocol layer.')
usdCopsProtocolSessionTable = MibTable((1, 3, 6, 1, 4, 1, 4874, 2, 2, 37, 1, 4, 1), )
if mibBuilder.loadTexts: usdCopsProtocolSessionTable.setStatus('current')
if mibBuilder.loadTexts: usdCopsProtocolSessionTable.setDescription('The COPS protocol session information table.')
usdCopsProtocolSessionEntry = MibTableRow((1, 3, 6, 1, 4, 1, 4874, 2, 2, 37, 1, 4, 1, 1), ).setIndexNames((0, "Unisphere-Data-COPS-MIB", "usdCopsProtocolSessionClientType"))
if mibBuilder.loadTexts: usdCopsProtocolSessionEntry.setStatus('current')
if mibBuilder.loadTexts: usdCopsProtocolSessionEntry.setDescription('An entry in the COPS protocol session information table.')
usdCopsProtocolSessionClientType = MibTableColumn((1, 3, 6, 1, 4, 1, 4874, 2, 2, 37, 1, 4, 1, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 65535)))
if mibBuilder.loadTexts: usdCopsProtocolSessionClientType.setStatus('current')
if mibBuilder.loadTexts: usdCopsProtocolSessionClientType.setDescription('The COPS client-type for which this entry information is valid.')
usdCopsProtocolSessionRemoteAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 4874, 2, 2, 37, 1, 4, 1, 1, 2), IpAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: usdCopsProtocolSessionRemoteAddress.setStatus('current')
if mibBuilder.loadTexts: usdCopsProtocolSessionRemoteAddress.setDescription('The IP address of the remote end of this session.')
usdCopsProtocolSessionRemotePort = MibTableColumn((1, 3, 6, 1, 4, 1, 4874, 2, 2, 37, 1, 4, 1, 1, 3), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: usdCopsProtocolSessionRemotePort.setStatus('current')
if mibBuilder.loadTexts: usdCopsProtocolSessionRemotePort.setDescription('The remote port for this session.')
usdCopsProtocolSessionBytesReceived = MibTableColumn((1, 3, 6, 1, 4, 1, 4874, 2, 2, 37, 1, 4, 1, 1, 4), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: usdCopsProtocolSessionBytesReceived.setStatus('current')
if mibBuilder.loadTexts: usdCopsProtocolSessionBytesReceived.setDescription('The number of bytes received by this session.')
usdCopsProtocolSessionPacketsReceived = MibTableColumn((1, 3, 6, 1, 4, 1, 4874, 2, 2, 37, 1, 4, 1, 1, 5), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: usdCopsProtocolSessionPacketsReceived.setStatus('current')
if mibBuilder.loadTexts: usdCopsProtocolSessionPacketsReceived.setDescription('The number of packets received by this session.')
usdCopsProtocolSessionBytesSent = MibTableColumn((1, 3, 6, 1, 4, 1, 4874, 2, 2, 37, 1, 4, 1, 1, 6), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: usdCopsProtocolSessionBytesSent.setStatus('current')
if mibBuilder.loadTexts: usdCopsProtocolSessionBytesSent.setDescription('The number of bytes sent on this session.')
usdCopsProtocolSessionPacketsSent = MibTableColumn((1, 3, 6, 1, 4, 1, 4874, 2, 2, 37, 1, 4, 1, 1, 7), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: usdCopsProtocolSessionPacketsSent.setStatus('current')
if mibBuilder.loadTexts: usdCopsProtocolSessionPacketsSent.setDescription('The number of packets sent on this session.')
usdCopsProtocolSessionREQSent = MibTableColumn((1, 3, 6, 1, 4, 1, 4874, 2, 2, 37, 1, 4, 1, 1, 8), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: usdCopsProtocolSessionREQSent.setStatus('current')
if mibBuilder.loadTexts: usdCopsProtocolSessionREQSent.setDescription('The number of REQ packets sent on this session.')
usdCopsProtocolSessionDECReceived = MibTableColumn((1, 3, 6, 1, 4, 1, 4874, 2, 2, 37, 1, 4, 1, 1, 9), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: usdCopsProtocolSessionDECReceived.setStatus('current')
if mibBuilder.loadTexts: usdCopsProtocolSessionDECReceived.setDescription('The number of DEC packets received on this session.')
usdCopsProtocolSessionRPTSent = MibTableColumn((1, 3, 6, 1, 4, 1, 4874, 2, 2, 37, 1, 4, 1, 1, 10), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: usdCopsProtocolSessionRPTSent.setStatus('current')
if mibBuilder.loadTexts: usdCopsProtocolSessionRPTSent.setDescription('The number of RPT packets sent on this session.')
usdCopsProtocolSessionDRQSent = MibTableColumn((1, 3, 6, 1, 4, 1, 4874, 2, 2, 37, 1, 4, 1, 1, 11), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: usdCopsProtocolSessionDRQSent.setStatus('current')
if mibBuilder.loadTexts: usdCopsProtocolSessionDRQSent.setDescription('The number of DRQ packets sent on this session.')
usdCopsProtocolSessionSSQSent = MibTableColumn((1, 3, 6, 1, 4, 1, 4874, 2, 2, 37, 1, 4, 1, 1, 12), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: usdCopsProtocolSessionSSQSent.setStatus('current')
if mibBuilder.loadTexts: usdCopsProtocolSessionSSQSent.setDescription('The number of SSQ packets sent on this session.')
usdCopsProtocolSessionOPNSent = MibTableColumn((1, 3, 6, 1, 4, 1, 4874, 2, 2, 37, 1, 4, 1, 1, 13), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: usdCopsProtocolSessionOPNSent.setStatus('current')
if mibBuilder.loadTexts: usdCopsProtocolSessionOPNSent.setDescription('The number of OPN packets sent on this session.')
usdCopsProtocolSessionCATReceived = MibTableColumn((1, 3, 6, 1, 4, 1, 4874, 2, 2, 37, 1, 4, 1, 1, 14), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: usdCopsProtocolSessionCATReceived.setStatus('current')
if mibBuilder.loadTexts: usdCopsProtocolSessionCATReceived.setDescription('The number of CAT packets received on this session.')
usdCopsProtocolSessionCCSent = MibTableColumn((1, 3, 6, 1, 4, 1, 4874, 2, 2, 37, 1, 4, 1, 1, 15), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: usdCopsProtocolSessionCCSent.setStatus('current')
if mibBuilder.loadTexts: usdCopsProtocolSessionCCSent.setDescription('The number of CC packets sent on this session.')
usdCopsProtocolSessionCCReceived = MibTableColumn((1, 3, 6, 1, 4, 1, 4874, 2, 2, 37, 1, 4, 1, 1, 16), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: usdCopsProtocolSessionCCReceived.setStatus('current')
if mibBuilder.loadTexts: usdCopsProtocolSessionCCReceived.setDescription('The number of CC packets received on this session.')
usdCopsProtocolSessionSSCSent = MibTableColumn((1, 3, 6, 1, 4, 1, 4874, 2, 2, 37, 1, 4, 1, 1, 17), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: usdCopsProtocolSessionSSCSent.setStatus('current')
if mibBuilder.loadTexts: usdCopsProtocolSessionSSCSent.setDescription('The number of SSC packets sent on this session.')
usdCopsProtocolSessionLocalAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 4874, 2, 2, 37, 1, 4, 1, 1, 18), IpAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: usdCopsProtocolSessionLocalAddress.setStatus('current')
if mibBuilder.loadTexts: usdCopsProtocolSessionLocalAddress.setDescription('The IP address of the local end of this session.')
usdCopsProtocolSessionTransportRouterName = MibTableColumn((1, 3, 6, 1, 4, 1, 4874, 2, 2, 37, 1, 4, 1, 1, 19), UsdName()).setMaxAccess("readonly")
if mibBuilder.loadTexts: usdCopsProtocolSessionTransportRouterName.setStatus('current')
if mibBuilder.loadTexts: usdCopsProtocolSessionTransportRouterName.setDescription('The administratively assigned name of the transport router for this session.')
usdCopsProtocolMIBConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 4874, 2, 2, 37, 4))
usdCopsProtocolMIBCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 4874, 2, 2, 37, 4, 1))
usdCopsProtocolMIBGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 4874, 2, 2, 37, 4, 2))
usdCopsProtocolAuthCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 4874, 2, 2, 37, 4, 1, 1)).setObjects(("Unisphere-Data-COPS-MIB", "usdCopsProtocolGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    usdCopsProtocolAuthCompliance = usdCopsProtocolAuthCompliance.setStatus('obsolete')
if mibBuilder.loadTexts: usdCopsProtocolAuthCompliance.setDescription('Current compliance statement for authentication clients implementing the Unisphere COPS Protocol MIB authentication functionality. This statement became obsolete when the local address and transport router name objects were add.')
usdCopsProtocolAuthCompliance2 = ModuleCompliance((1, 3, 6, 1, 4, 1, 4874, 2, 2, 37, 4, 1, 2)).setObjects(("Unisphere-Data-COPS-MIB", "usdCopsProtocolGroup2"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    usdCopsProtocolAuthCompliance2 = usdCopsProtocolAuthCompliance2.setStatus('current')
if mibBuilder.loadTexts: usdCopsProtocolAuthCompliance2.setDescription('The compliance statement for authentication clients implementing the Unisphere COPS Protocol MIB authentication functionality.')
usdCopsProtocolGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 4874, 2, 2, 37, 4, 2, 1)).setObjects(("Unisphere-Data-COPS-MIB", "usdCopsProtocolSessionsCreated"), ("Unisphere-Data-COPS-MIB", "usdCopsProtocolSessionsDeleted"), ("Unisphere-Data-COPS-MIB", "usdCopsProtocolCurrentSessions"), ("Unisphere-Data-COPS-MIB", "usdCopsProtocolBytesReceived"), ("Unisphere-Data-COPS-MIB", "usdCopsProtocolPacketsReceived"), ("Unisphere-Data-COPS-MIB", "usdCopsProtocolBytesSent"), ("Unisphere-Data-COPS-MIB", "usdCopsProtocolPacketsSent"), ("Unisphere-Data-COPS-MIB", "usdCopsProtocolKeepAlivesReceived"), ("Unisphere-Data-COPS-MIB", "usdCopsProtocolKeepAlivesSent"), ("Unisphere-Data-COPS-MIB", "usdCopsProtocolSessionRemoteAddress"), ("Unisphere-Data-COPS-MIB", "usdCopsProtocolSessionRemotePort"), ("Unisphere-Data-COPS-MIB", "usdCopsProtocolSessionBytesReceived"), ("Unisphere-Data-COPS-MIB", "usdCopsProtocolSessionPacketsReceived"), ("Unisphere-Data-COPS-MIB", "usdCopsProtocolSessionBytesSent"), ("Unisphere-Data-COPS-MIB", "usdCopsProtocolSessionPacketsSent"), ("Unisphere-Data-COPS-MIB", "usdCopsProtocolSessionREQSent"), ("Unisphere-Data-COPS-MIB", "usdCopsProtocolSessionDECReceived"), ("Unisphere-Data-COPS-MIB", "usdCopsProtocolSessionRPTSent"), ("Unisphere-Data-COPS-MIB", "usdCopsProtocolSessionDRQSent"), ("Unisphere-Data-COPS-MIB", "usdCopsProtocolSessionSSQSent"), ("Unisphere-Data-COPS-MIB", "usdCopsProtocolSessionOPNSent"), ("Unisphere-Data-COPS-MIB", "usdCopsProtocolSessionCATReceived"), ("Unisphere-Data-COPS-MIB", "usdCopsProtocolSessionCCSent"), ("Unisphere-Data-COPS-MIB", "usdCopsProtocolSessionCCReceived"), ("Unisphere-Data-COPS-MIB", "usdCopsProtocolSessionSSCSent"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    usdCopsProtocolGroup = usdCopsProtocolGroup.setStatus('obsolete')
if mibBuilder.loadTexts: usdCopsProtocolGroup.setDescription('Obsolete basic collection of objects providing management of the COPS Protocol. This group became obsolete when the local address and transport router name objects were add.')
usdCopsProtocolGroup2 = ObjectGroup((1, 3, 6, 1, 4, 1, 4874, 2, 2, 37, 4, 2, 2)).setObjects(("Unisphere-Data-COPS-MIB", "usdCopsProtocolSessionsCreated"), ("Unisphere-Data-COPS-MIB", "usdCopsProtocolSessionsDeleted"), ("Unisphere-Data-COPS-MIB", "usdCopsProtocolCurrentSessions"), ("Unisphere-Data-COPS-MIB", "usdCopsProtocolBytesReceived"), ("Unisphere-Data-COPS-MIB", "usdCopsProtocolPacketsReceived"), ("Unisphere-Data-COPS-MIB", "usdCopsProtocolBytesSent"), ("Unisphere-Data-COPS-MIB", "usdCopsProtocolPacketsSent"), ("Unisphere-Data-COPS-MIB", "usdCopsProtocolKeepAlivesReceived"), ("Unisphere-Data-COPS-MIB", "usdCopsProtocolKeepAlivesSent"), ("Unisphere-Data-COPS-MIB", "usdCopsProtocolSessionRemoteAddress"), ("Unisphere-Data-COPS-MIB", "usdCopsProtocolSessionRemotePort"), ("Unisphere-Data-COPS-MIB", "usdCopsProtocolSessionBytesReceived"), ("Unisphere-Data-COPS-MIB", "usdCopsProtocolSessionPacketsReceived"), ("Unisphere-Data-COPS-MIB", "usdCopsProtocolSessionBytesSent"), ("Unisphere-Data-COPS-MIB", "usdCopsProtocolSessionPacketsSent"), ("Unisphere-Data-COPS-MIB", "usdCopsProtocolSessionREQSent"), ("Unisphere-Data-COPS-MIB", "usdCopsProtocolSessionDECReceived"), ("Unisphere-Data-COPS-MIB", "usdCopsProtocolSessionRPTSent"), ("Unisphere-Data-COPS-MIB", "usdCopsProtocolSessionDRQSent"), ("Unisphere-Data-COPS-MIB", "usdCopsProtocolSessionSSQSent"), ("Unisphere-Data-COPS-MIB", "usdCopsProtocolSessionOPNSent"), ("Unisphere-Data-COPS-MIB", "usdCopsProtocolSessionCATReceived"), ("Unisphere-Data-COPS-MIB", "usdCopsProtocolSessionCCSent"), ("Unisphere-Data-COPS-MIB", "usdCopsProtocolSessionCCReceived"), ("Unisphere-Data-COPS-MIB", "usdCopsProtocolSessionSSCSent"), ("Unisphere-Data-COPS-MIB", "usdCopsProtocolSessionLocalAddress"), ("Unisphere-Data-COPS-MIB", "usdCopsProtocolSessionTransportRouterName"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    usdCopsProtocolGroup2 = usdCopsProtocolGroup2.setStatus('current')
if mibBuilder.loadTexts: usdCopsProtocolGroup2.setDescription('The basic collection of objects providing management of the COPS Protocol.')
mibBuilder.exportSymbols("Unisphere-Data-COPS-MIB", usdCopsProtocolMIB=usdCopsProtocolMIB, usdCopsProtocolPacketsSent=usdCopsProtocolPacketsSent, usdCopsProtocolSessionsCreated=usdCopsProtocolSessionsCreated, usdCopsProtocolSessionTransportRouterName=usdCopsProtocolSessionTransportRouterName, usdCopsProtocolStatus=usdCopsProtocolStatus, usdCopsProtocolBytesReceived=usdCopsProtocolBytesReceived, usdCopsProtocolStatistics=usdCopsProtocolStatistics, usdCopsProtocolSessionClientType=usdCopsProtocolSessionClientType, usdCopsProtocolSessionCCSent=usdCopsProtocolSessionCCSent, usdCopsProtocolKeepAlivesSent=usdCopsProtocolKeepAlivesSent, usdCopsProtocolSessionRemotePort=usdCopsProtocolSessionRemotePort, usdCopsProtocolPacketsReceived=usdCopsProtocolPacketsReceived, usdCopsProtocolMIBCompliances=usdCopsProtocolMIBCompliances, usdCopsProtocolSessionREQSent=usdCopsProtocolSessionREQSent, usdCopsProtocolStatisticsScalars=usdCopsProtocolStatisticsScalars, usdCopsProtocolBytesSent=usdCopsProtocolBytesSent, usdCopsProtocolSessionCCReceived=usdCopsProtocolSessionCCReceived, usdCopsProtocolMIBGroups=usdCopsProtocolMIBGroups, usdCopsProtocolAuthCompliance=usdCopsProtocolAuthCompliance, usdCopsProtocolSessionPacketsSent=usdCopsProtocolSessionPacketsSent, usdCopsProtocolSessionDRQSent=usdCopsProtocolSessionDRQSent, usdCopsProtocolCfg=usdCopsProtocolCfg, usdCopsProtocolSessionRemoteAddress=usdCopsProtocolSessionRemoteAddress, usdCopsProtocolSessionsDeleted=usdCopsProtocolSessionsDeleted, usdCopsProtocolGroup2=usdCopsProtocolGroup2, usdCopsProtocolSessionBytesReceived=usdCopsProtocolSessionBytesReceived, usdCopsProtocolSessionSSCSent=usdCopsProtocolSessionSSCSent, usdCopsProtocolKeepAlivesReceived=usdCopsProtocolKeepAlivesReceived, usdCopsProtocolObjects=usdCopsProtocolObjects, usdCopsProtocolSessionDECReceived=usdCopsProtocolSessionDECReceived, usdCopsProtocolSessionRPTSent=usdCopsProtocolSessionRPTSent, usdCopsProtocolSessionLocalAddress=usdCopsProtocolSessionLocalAddress, usdCopsProtocolGroup=usdCopsProtocolGroup, usdCopsProtocolSessionOPNSent=usdCopsProtocolSessionOPNSent, PYSNMP_MODULE_ID=usdCopsProtocolMIB, usdCopsProtocolMIBConformance=usdCopsProtocolMIBConformance, usdCopsProtocolCurrentSessions=usdCopsProtocolCurrentSessions, usdCopsProtocolSessionCATReceived=usdCopsProtocolSessionCATReceived, usdCopsProtocolSessionSSQSent=usdCopsProtocolSessionSSQSent, usdCopsProtocolSessionEntry=usdCopsProtocolSessionEntry, usdCopsProtocolSessionTable=usdCopsProtocolSessionTable, usdCopsProtocolAuthCompliance2=usdCopsProtocolAuthCompliance2, usdCopsProtocolSessionBytesSent=usdCopsProtocolSessionBytesSent, usdCopsProtocolSessionPacketsReceived=usdCopsProtocolSessionPacketsReceived, usdCopsProtocolSession=usdCopsProtocolSession)