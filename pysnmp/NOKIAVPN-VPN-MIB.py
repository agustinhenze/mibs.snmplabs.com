#
# PySNMP MIB module NOKIAVPN-VPN-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/NOKIAVPN-VPN-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 20:14:02 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
OctetString, ObjectIdentifier, Integer = mibBuilder.importSymbols("ASN1", "OctetString", "ObjectIdentifier", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsUnion, ConstraintsIntersection, ValueSizeConstraint, ValueRangeConstraint, SingleValueConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "ConstraintsIntersection", "ValueSizeConstraint", "ValueRangeConstraint", "SingleValueConstraint")
nokiaVPNModules, vpn = mibBuilder.importSymbols("NOKIAVPN-MIB", "nokiaVPNModules", "vpn")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
Integer32, iso, Bits, MibIdentifier, ObjectIdentity, TimeTicks, Gauge32, NotificationType, Unsigned32, Counter32, IpAddress, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter64, ModuleIdentity = mibBuilder.importSymbols("SNMPv2-SMI", "Integer32", "iso", "Bits", "MibIdentifier", "ObjectIdentity", "TimeTicks", "Gauge32", "NotificationType", "Unsigned32", "Counter32", "IpAddress", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter64", "ModuleIdentity")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
nokiaVPNMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 94, 1, 41, 5, 5))
nokiaVPNMIB.setRevisions(('2001-01-18 00:00',))
if mibBuilder.loadTexts: nokiaVPNMIB.setLastUpdated('200101180000Z')
if mibBuilder.loadTexts: nokiaVPNMIB.setOrganization('Nokia Internet Communications')
vpnL2TPTunnels = MibScalar((1, 3, 6, 1, 4, 1, 94, 1, 41, 2, 2, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: vpnL2TPTunnels.setStatus('current')
vpnActiveL2TPTunnels = MibScalar((1, 3, 6, 1, 4, 1, 94, 1, 41, 2, 2, 2), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: vpnActiveL2TPTunnels.setStatus('current')
vpnL2TPSessions = MibScalar((1, 3, 6, 1, 4, 1, 94, 1, 41, 2, 2, 3), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: vpnL2TPSessions.setStatus('current')
vpnActiveL2TPSessions = MibScalar((1, 3, 6, 1, 4, 1, 94, 1, 41, 2, 2, 4), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: vpnActiveL2TPSessions.setStatus('current')
vpnPPTPTS = MibScalar((1, 3, 6, 1, 4, 1, 94, 1, 41, 2, 2, 5), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: vpnPPTPTS.setStatus('current')
vpnActivePPTPTS = MibScalar((1, 3, 6, 1, 4, 1, 94, 1, 41, 2, 2, 6), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: vpnActivePPTPTS.setStatus('current')
vpnTunnelTable = MibTable((1, 3, 6, 1, 4, 1, 94, 1, 41, 2, 2, 7), )
if mibBuilder.loadTexts: vpnTunnelTable.setStatus('current')
vpnTunnelEntry = MibTableRow((1, 3, 6, 1, 4, 1, 94, 1, 41, 2, 2, 7, 1), ).setIndexNames((0, "NOKIAVPN-VPN-MIB", "vpnTunnelLocalID"), (0, "NOKIAVPN-VPN-MIB", "vpnTunnelIPAddress"))
if mibBuilder.loadTexts: vpnTunnelEntry.setStatus('current')
vpnTunnelLocalID = MibTableColumn((1, 3, 6, 1, 4, 1, 94, 1, 41, 2, 2, 7, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: vpnTunnelLocalID.setStatus('current')
vpnTunnelIPAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 94, 1, 41, 2, 2, 7, 1, 2), IpAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: vpnTunnelIPAddress.setStatus('current')
vpnTunnelRemoteID = MibTableColumn((1, 3, 6, 1, 4, 1, 94, 1, 41, 2, 2, 7, 1, 3), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: vpnTunnelRemoteID.setStatus('current')
vpnTunnelType = MibTableColumn((1, 3, 6, 1, 4, 1, 94, 1, 41, 2, 2, 7, 1, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1, 2))).clone(namedValues=NamedValues(("any", 0), ("l2tp", 1), ("pptp", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: vpnTunnelType.setStatus('current')
vpnTunnelActive = MibTableColumn((1, 3, 6, 1, 4, 1, 94, 1, 41, 2, 2, 7, 1, 5), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1))).clone(namedValues=NamedValues(("inactive", 0), ("active", 1)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: vpnTunnelActive.setStatus('current')
vpnTunnelState = MibTableColumn((1, 3, 6, 1, 4, 1, 94, 1, 41, 2, 2, 7, 1, 6), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 4))).setMaxAccess("readonly")
if mibBuilder.loadTexts: vpnTunnelState.setStatus('current')
vpnSessionTable = MibTable((1, 3, 6, 1, 4, 1, 94, 1, 41, 2, 2, 8), )
if mibBuilder.loadTexts: vpnSessionTable.setStatus('current')
vpnSessionEntry = MibTableRow((1, 3, 6, 1, 4, 1, 94, 1, 41, 2, 2, 8, 1), ).setIndexNames((0, "NOKIAVPN-VPN-MIB", "vpnTunnelLocalID"), (0, "NOKIAVPN-VPN-MIB", "vpnTunnelIPAddress"), (0, "NOKIAVPN-VPN-MIB", "vpnSessionLocalID"), (0, "NOKIAVPN-VPN-MIB", "vpnSessionIPAddress"))
if mibBuilder.loadTexts: vpnSessionEntry.setStatus('current')
vpnSessionLocalID = MibTableColumn((1, 3, 6, 1, 4, 1, 94, 1, 41, 2, 2, 8, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: vpnSessionLocalID.setStatus('current')
vpnSessionIPAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 94, 1, 41, 2, 2, 8, 1, 2), IpAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: vpnSessionIPAddress.setStatus('current')
vpnSessionRemoteID = MibTableColumn((1, 3, 6, 1, 4, 1, 94, 1, 41, 2, 2, 8, 1, 3), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: vpnSessionRemoteID.setStatus('current')
vpnSessionPacketsIn = MibTableColumn((1, 3, 6, 1, 4, 1, 94, 1, 41, 2, 2, 8, 1, 4), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: vpnSessionPacketsIn.setStatus('current')
vpnSessionPacketsOut = MibTableColumn((1, 3, 6, 1, 4, 1, 94, 1, 41, 2, 2, 8, 1, 5), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: vpnSessionPacketsOut.setStatus('current')
vpnSessionActive = MibTableColumn((1, 3, 6, 1, 4, 1, 94, 1, 41, 2, 2, 8, 1, 6), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1))).clone(namedValues=NamedValues(("inactive", 0), ("active", 1)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: vpnSessionActive.setStatus('current')
vpnSessionState = MibTableColumn((1, 3, 6, 1, 4, 1, 94, 1, 41, 2, 2, 8, 1, 7), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1, 2))).clone(namedValues=NamedValues(("inactive", 0), ("suspended", 1), ("active", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: vpnSessionState.setStatus('current')
vpnSessionAuthType = MibTableColumn((1, 3, 6, 1, 4, 1, 94, 1, 41, 2, 2, 8, 1, 8), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3))).clone(namedValues=NamedValues(("none", 0), ("chap", 1), ("mschap", 2), ("pap", 3)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: vpnSessionAuthType.setStatus('current')
vpnSessionSendFlags = MibTableColumn((1, 3, 6, 1, 4, 1, 94, 1, 41, 2, 2, 8, 1, 9), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: vpnSessionSendFlags.setStatus('current')
vpnSessionRecvFlags = MibTableColumn((1, 3, 6, 1, 4, 1, 94, 1, 41, 2, 2, 8, 1, 10), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: vpnSessionRecvFlags.setStatus('current')
vpnSessionUsername = MibTableColumn((1, 3, 6, 1, 4, 1, 94, 1, 41, 2, 2, 8, 1, 11), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: vpnSessionUsername.setStatus('current')
vpnSessionLifetimeSeconds = MibTableColumn((1, 3, 6, 1, 4, 1, 94, 1, 41, 2, 2, 8, 1, 12), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: vpnSessionLifetimeSeconds.setStatus('current')
mibBuilder.exportSymbols("NOKIAVPN-VPN-MIB", vpnSessionLocalID=vpnSessionLocalID, vpnTunnelLocalID=vpnTunnelLocalID, vpnTunnelType=vpnTunnelType, vpnL2TPTunnels=vpnL2TPTunnels, PYSNMP_MODULE_ID=nokiaVPNMIB, nokiaVPNMIB=nokiaVPNMIB, vpnSessionState=vpnSessionState, vpnActiveL2TPSessions=vpnActiveL2TPSessions, vpnSessionIPAddress=vpnSessionIPAddress, vpnSessionSendFlags=vpnSessionSendFlags, vpnActiveL2TPTunnels=vpnActiveL2TPTunnels, vpnTunnelEntry=vpnTunnelEntry, vpnSessionRecvFlags=vpnSessionRecvFlags, vpnActivePPTPTS=vpnActivePPTPTS, vpnSessionPacketsIn=vpnSessionPacketsIn, vpnSessionEntry=vpnSessionEntry, vpnPPTPTS=vpnPPTPTS, vpnSessionTable=vpnSessionTable, vpnL2TPSessions=vpnL2TPSessions, vpnTunnelActive=vpnTunnelActive, vpnTunnelIPAddress=vpnTunnelIPAddress, vpnSessionLifetimeSeconds=vpnSessionLifetimeSeconds, vpnSessionPacketsOut=vpnSessionPacketsOut, vpnTunnelRemoteID=vpnTunnelRemoteID, vpnSessionRemoteID=vpnSessionRemoteID, vpnTunnelState=vpnTunnelState, vpnTunnelTable=vpnTunnelTable, vpnSessionAuthType=vpnSessionAuthType, vpnSessionUsername=vpnSessionUsername, vpnSessionActive=vpnSessionActive)