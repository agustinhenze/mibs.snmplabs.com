#
# PySNMP MIB module Wellfleet-MPLS-LDP-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/Wellfleet-MPLS-LDP-MIB
# Produced by pysmi-0.3.4 at Wed May  1 15:40:58 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
Integer, OctetString, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "Integer", "OctetString", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ConstraintsUnion, ValueSizeConstraint, ValueRangeConstraint, SingleValueConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ConstraintsUnion", "ValueSizeConstraint", "ValueRangeConstraint", "SingleValueConstraint")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
TimeTicks, ObjectIdentity, Counter64, Gauge32, iso, NotificationType, Bits, Unsigned32, MibScalar, MibTable, MibTableRow, MibTableColumn, Integer32, ModuleIdentity, Counter32, MibIdentifier, IpAddress = mibBuilder.importSymbols("SNMPv2-SMI", "TimeTicks", "ObjectIdentity", "Counter64", "Gauge32", "iso", "NotificationType", "Bits", "Unsigned32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Integer32", "ModuleIdentity", "Counter32", "MibIdentifier", "IpAddress")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
wfMplsLdpGroup, = mibBuilder.importSymbols("Wellfleet-COMMON-MIB", "wfMplsLdpGroup")
wfMplsLdpSessCfgTable = MibTable((1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 15, 1), )
if mibBuilder.loadTexts: wfMplsLdpSessCfgTable.setStatus('mandatory')
if mibBuilder.loadTexts: wfMplsLdpSessCfgTable.setDescription('MPLS LDP session table - This tabulates the LDP session within an mpls protocol group. All sessions are indexed according to the physical slot and the associated interface circuit number and session index. There can be more LDP sessions per L2 MPLS interface.')
wfMplsLdpSessCfgEntry = MibTableRow((1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 15, 1, 1), ).setIndexNames((0, "Wellfleet-MPLS-LDP-MIB", "wfMplsLdpSessCfgSlot"), (0, "Wellfleet-MPLS-LDP-MIB", "wfMplsLdpSessCfgCircuit"), (0, "Wellfleet-MPLS-LDP-MIB", "wfMplsLdpSessCfgIndex"))
if mibBuilder.loadTexts: wfMplsLdpSessCfgEntry.setStatus('mandatory')
if mibBuilder.loadTexts: wfMplsLdpSessCfgEntry.setDescription('MPLS LDP session entries.')
wfMplsLdpSessCfgCreate = MibTableColumn((1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 15, 1, 1, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("created", 1), ("deleted", 2))).clone('created')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: wfMplsLdpSessCfgCreate.setStatus('mandatory')
if mibBuilder.loadTexts: wfMplsLdpSessCfgCreate.setDescription('Create/Delete parameter. Default is created. Users modify this object in order to create/delete MPLS LDP sessions')
wfMplsLdpSessCfgEnable = MibTableColumn((1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 15, 1, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enabled", 1), ("disabled", 2))).clone('enabled')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: wfMplsLdpSessCfgEnable.setStatus('mandatory')
if mibBuilder.loadTexts: wfMplsLdpSessCfgEnable.setDescription('Enable/Disable parameter. Default is enabled.')
wfMplsLdpSessCfgSlot = MibTableColumn((1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 15, 1, 1, 3), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: wfMplsLdpSessCfgSlot.setStatus('mandatory')
if mibBuilder.loadTexts: wfMplsLdpSessCfgSlot.setDescription('The slot number this LDP session is configured on.')
wfMplsLdpSessCfgIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 15, 1, 1, 4), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: wfMplsLdpSessCfgIndex.setStatus('mandatory')
if mibBuilder.loadTexts: wfMplsLdpSessCfgIndex.setDescription('The Session index identifies this particular LDP session on an interface.')
wfMplsLdpSessCfgCircuit = MibTableColumn((1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 15, 1, 1, 5), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 1023))).setMaxAccess("readonly")
if mibBuilder.loadTexts: wfMplsLdpSessCfgCircuit.setStatus('mandatory')
if mibBuilder.loadTexts: wfMplsLdpSessCfgCircuit.setDescription('The circuit number of the circuit to which the session belongs.')
wfMplsLdpSessCfgLocalIpAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 15, 1, 1, 6), IpAddress()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: wfMplsLdpSessCfgLocalIpAddress.setStatus('mandatory')
if mibBuilder.loadTexts: wfMplsLdpSessCfgLocalIpAddress.setDescription('The IP address of this MPLS device for the purpose of establishing the LDP peer to peer session.')
wfMplsLdpSessCfgLocalTcpPort = MibTableColumn((1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 15, 1, 1, 7), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 65535)).clone(8192)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: wfMplsLdpSessCfgLocalTcpPort.setStatus('mandatory')
if mibBuilder.loadTexts: wfMplsLdpSessCfgLocalTcpPort.setDescription('The TCP port address of this MPLS device for the purpose of establishing the LDP peer to peer session.')
wfMplsLdpSessCfgRemoteIpAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 15, 1, 1, 8), IpAddress()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: wfMplsLdpSessCfgRemoteIpAddress.setStatus('mandatory')
if mibBuilder.loadTexts: wfMplsLdpSessCfgRemoteIpAddress.setDescription('The IP address of the remote MPLS device for the purpose of establishing the LDP peer to peer session.')
wfMplsLdpSessCfgRemoteTcpPort = MibTableColumn((1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 15, 1, 1, 9), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 65535)).clone(8192)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: wfMplsLdpSessCfgRemoteTcpPort.setStatus('mandatory')
if mibBuilder.loadTexts: wfMplsLdpSessCfgRemoteTcpPort.setDescription('The TCP port of the remote MPLS device for the purpose of establishing the LDP peer to peer session.')
wfMplsLdpSessCfgRoutesConfigMode = MibTableColumn((1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 15, 1, 1, 10), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("auto", 1), ("manual", 2))).clone('auto')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: wfMplsLdpSessCfgRoutesConfigMode.setStatus('mandatory')
if mibBuilder.loadTexts: wfMplsLdpSessCfgRoutesConfigMode.setDescription('Indicates whether network routes should be discovered by a routing protocol(auto) or should be Manually configured(manual), see wfMplsLdpCfgRouteTable.')
wfMplsLdpSessCfgHoldTime = MibTableColumn((1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 15, 1, 1, 11), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 240)).clone(40)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: wfMplsLdpSessCfgHoldTime.setStatus('mandatory')
if mibBuilder.loadTexts: wfMplsLdpSessCfgHoldTime.setDescription('the Hold Time indicates the maximum time in seconds that may elapse between the receipt of successive PDUs from the LSR peer.')
wfMplsLdpSessCfgProto = MibTableColumn((1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 15, 1, 1, 12), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))).clone(namedValues=NamedValues(("ospf", 1), ("rip", 2), ("hybridospf", 3), ("hybridrip", 4))).clone('ospf')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: wfMplsLdpSessCfgProto.setStatus('mandatory')
if mibBuilder.loadTexts: wfMplsLdpSessCfgProto.setDescription('The routing protocols used by MPLS.')
wfMplsLdpSessCfgAggregation = MibTableColumn((1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 15, 1, 1, 13), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enabled", 1), ("disabled", 2))).clone('disabled')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: wfMplsLdpSessCfgAggregation.setStatus('mandatory')
if mibBuilder.loadTexts: wfMplsLdpSessCfgAggregation.setDescription('Enable/Disable aggregation. Default is disabled.')
wfMplsLdpSessCfgDebugLevel = MibTableColumn((1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 15, 1, 1, 14), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))).clone(namedValues=NamedValues(("one", 1), ("two", 2), ("three", 3), ("debug", 4))).clone('two')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: wfMplsLdpSessCfgDebugLevel.setStatus('mandatory')
if mibBuilder.loadTexts: wfMplsLdpSessCfgDebugLevel.setDescription('Debug Levels - This attribute is used to assign the level of DEBUG message to be logged for each LDP session.')
wfMplsLdpSessCfgReqBindRetryTime = MibTableColumn((1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 15, 1, 1, 15), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 240)).clone(40)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: wfMplsLdpSessCfgReqBindRetryTime.setStatus('mandatory')
if mibBuilder.loadTexts: wfMplsLdpSessCfgReqBindRetryTime.setDescription('It indicates the maximum time in seconds that may elapse between two consecutive request bind in case of no reply.')
wfMplsLdpSessCfgReqBindRetries = MibTableColumn((1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 15, 1, 1, 16), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 240)).clone(240)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: wfMplsLdpSessCfgReqBindRetries.setStatus('mandatory')
if mibBuilder.loadTexts: wfMplsLdpSessCfgReqBindRetries.setDescription('It indicates the number of retry times.')
wfMplsLdpSessActualTable = MibTable((1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 15, 2), )
if mibBuilder.loadTexts: wfMplsLdpSessActualTable.setStatus('mandatory')
if mibBuilder.loadTexts: wfMplsLdpSessActualTable.setDescription('MPLS LDP interface actual table - read-only table containing LDP peer status, and actual LDP information.')
wfMplsLdpSessActualEntry = MibTableRow((1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 15, 2, 1), ).setIndexNames((0, "Wellfleet-MPLS-LDP-MIB", "wfMplsLdpSessActualCircuit"), (0, "Wellfleet-MPLS-LDP-MIB", "wfMplsLdpSessActualIndex"))
if mibBuilder.loadTexts: wfMplsLdpSessActualEntry.setStatus('mandatory')
if mibBuilder.loadTexts: wfMplsLdpSessActualEntry.setDescription('MPLS LDP interface entries.')
wfMplsLdpSessActualIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 15, 2, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: wfMplsLdpSessActualIndex.setStatus('mandatory')
if mibBuilder.loadTexts: wfMplsLdpSessActualIndex.setDescription('The Session index identifies this particular LDP session on the interface.')
wfMplsLdpSessActualCircuit = MibTableColumn((1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 15, 2, 1, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 1023))).setMaxAccess("readonly")
if mibBuilder.loadTexts: wfMplsLdpSessActualCircuit.setStatus('mandatory')
if mibBuilder.loadTexts: wfMplsLdpSessActualCircuit.setDescription('The circuit number of the circuit to which the session belongs.')
wfMplsLdpSessActualState = MibTableColumn((1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 15, 2, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))).clone(namedValues=NamedValues(("up", 1), ("down", 2), ("init", 3), ("notpresent", 4)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: wfMplsLdpSessActualState.setStatus('mandatory')
if mibBuilder.loadTexts: wfMplsLdpSessActualState.setDescription('The current state of the MPLS LDP session')
wfMplsLdpSessActualPeerState = MibTableColumn((1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 15, 2, 1, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))).clone(namedValues=NamedValues(("initialized", 1), ("opensend", 2), ("openrec", 3), ("operational", 4))).clone('initialized')).setMaxAccess("readonly")
if mibBuilder.loadTexts: wfMplsLdpSessActualPeerState.setStatus('mandatory')
if mibBuilder.loadTexts: wfMplsLdpSessActualPeerState.setDescription('The current state of MPLS LDP session with the remote MPLS device')
wfMplsLdpSessActualLocalIpAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 15, 2, 1, 5), IpAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: wfMplsLdpSessActualLocalIpAddress.setStatus('mandatory')
if mibBuilder.loadTexts: wfMplsLdpSessActualLocalIpAddress.setDescription('The actual IP address that LDP used to establish the LDP peer to peer session.')
wfMplsLdpSessActualLocalTcpPort = MibTableColumn((1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 15, 2, 1, 6), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 65535))).setMaxAccess("readonly")
if mibBuilder.loadTexts: wfMplsLdpSessActualLocalTcpPort.setStatus('mandatory')
if mibBuilder.loadTexts: wfMplsLdpSessActualLocalTcpPort.setDescription('The actual local TCP port address that this LDP used to establish the LDP peer to peer session.')
wfMplsLdpSessActualRemoteIpAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 15, 2, 1, 7), IpAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: wfMplsLdpSessActualRemoteIpAddress.setStatus('mandatory')
if mibBuilder.loadTexts: wfMplsLdpSessActualRemoteIpAddress.setDescription('The actual remote IP address that LDP used to establish the LDP peer to peer session.')
wfMplsLdpSessActualRemoteTcpPort = MibTableColumn((1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 15, 2, 1, 8), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 65535))).setMaxAccess("readonly")
if mibBuilder.loadTexts: wfMplsLdpSessActualRemoteTcpPort.setStatus('mandatory')
if mibBuilder.loadTexts: wfMplsLdpSessActualRemoteTcpPort.setDescription('The actual TCP port that LDP used to establish the LDP peer to peer session.')
wfMplsLdpSessActualHoldTime = MibTableColumn((1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 15, 2, 1, 9), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 240))).setMaxAccess("readonly")
if mibBuilder.loadTexts: wfMplsLdpSessActualHoldTime.setStatus('mandatory')
if mibBuilder.loadTexts: wfMplsLdpSessActualHoldTime.setDescription('the actual Hold Time that LDP used to indicate the maximum time in seconds that may elapse between the receipt of successive PDUs from the LSR peer.')
wfMplsLdpSessActualRoutesConfigMode = MibTableColumn((1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 15, 2, 1, 10), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("auto", 1), ("manual", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: wfMplsLdpSessActualRoutesConfigMode.setStatus('mandatory')
if mibBuilder.loadTexts: wfMplsLdpSessActualRoutesConfigMode.setDescription('Indicates whether network routes are discovered by a routing protocol(auto) or are Manually configured(manual), see wfMplsLdpCfgRouteTable.')
wfMplsLdpSessActualTCPConnectionRole = MibTableColumn((1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 15, 2, 1, 11), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("active", 1), ("passive", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: wfMplsLdpSessActualTCPConnectionRole.setStatus('mandatory')
if mibBuilder.loadTexts: wfMplsLdpSessActualTCPConnectionRole.setDescription('Indicates the TCP connection roles between the peers.')
wfMplsLdpSessActualSlot = MibTableColumn((1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 15, 2, 1, 12), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: wfMplsLdpSessActualSlot.setStatus('mandatory')
if mibBuilder.loadTexts: wfMplsLdpSessActualSlot.setDescription('Indicates the slot on which the LDP session is running.')
wfMplsLdpCfgRouteTable = MibTable((1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 15, 3), )
if mibBuilder.loadTexts: wfMplsLdpCfgRouteTable.setStatus('mandatory')
if mibBuilder.loadTexts: wfMplsLdpCfgRouteTable.setDescription('MPLS LDP configured route table -')
wfMplsLdpCfgRouteEntry = MibTableRow((1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 15, 3, 1), ).setIndexNames((0, "Wellfleet-MPLS-LDP-MIB", "wfMplsLdpCfgRouteCct"), (0, "Wellfleet-MPLS-LDP-MIB", "wfMplsLdpCfgRouteSessId"), (0, "Wellfleet-MPLS-LDP-MIB", "wfMplsLdpCfgRouteIndex"))
if mibBuilder.loadTexts: wfMplsLdpCfgRouteEntry.setStatus('mandatory')
if mibBuilder.loadTexts: wfMplsLdpCfgRouteEntry.setDescription('MPLS LDP configured route entries.')
wfMplsLdpCfgRouteCreate = MibTableColumn((1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 15, 3, 1, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("created", 1), ("deleted", 2))).clone('created')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: wfMplsLdpCfgRouteCreate.setStatus('mandatory')
if mibBuilder.loadTexts: wfMplsLdpCfgRouteCreate.setDescription('Create/Delete parameter. Default is created. Users modify this object in order to create/delete MPLS LSP')
wfMplsLdpCfgRouteEnable = MibTableColumn((1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 15, 3, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enabled", 1), ("disabled", 2))).clone('enabled')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: wfMplsLdpCfgRouteEnable.setStatus('mandatory')
if mibBuilder.loadTexts: wfMplsLdpCfgRouteEnable.setDescription('Enable/Disable parameter. Default is enabled.')
wfMplsLdpCfgRouteCct = MibTableColumn((1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 15, 3, 1, 3), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 1023))).setMaxAccess("readonly")
if mibBuilder.loadTexts: wfMplsLdpCfgRouteCct.setStatus('mandatory')
if mibBuilder.loadTexts: wfMplsLdpCfgRouteCct.setDescription('The circuit munber to which the route associates with.')
wfMplsLdpCfgRouteSessId = MibTableColumn((1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 15, 3, 1, 4), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 1023))).setMaxAccess("readonly")
if mibBuilder.loadTexts: wfMplsLdpCfgRouteSessId.setStatus('mandatory')
if mibBuilder.loadTexts: wfMplsLdpCfgRouteSessId.setDescription('The session identification munber to which the route associates with.')
wfMplsLdpCfgRouteIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 15, 3, 1, 5), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: wfMplsLdpCfgRouteIndex.setStatus('mandatory')
if mibBuilder.loadTexts: wfMplsLdpCfgRouteIndex.setDescription('The index number of this route.')
wfMplsLdpCfgRouteDestination = MibTableColumn((1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 15, 3, 1, 6), IpAddress()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: wfMplsLdpCfgRouteDestination.setStatus('mandatory')
if mibBuilder.loadTexts: wfMplsLdpCfgRouteDestination.setDescription('The netwrok prefix of this route.')
wfMplsLdpCfgRouteMask = MibTableColumn((1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 15, 3, 1, 7), IpAddress()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: wfMplsLdpCfgRouteMask.setStatus('mandatory')
if mibBuilder.loadTexts: wfMplsLdpCfgRouteMask.setDescription('The mask of this route.')
wfMplsLdpCfgRouteState = MibTableColumn((1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 15, 3, 1, 8), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("up", 1), ("down", 2))).clone('down')).setMaxAccess("readonly")
if mibBuilder.loadTexts: wfMplsLdpCfgRouteState.setStatus('mandatory')
if mibBuilder.loadTexts: wfMplsLdpCfgRouteState.setDescription('The current state of the MPLS LDP session.')
wfMplsLdpLibTable = MibTable((1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 15, 4), )
if mibBuilder.loadTexts: wfMplsLdpLibTable.setStatus('mandatory')
if mibBuilder.loadTexts: wfMplsLdpLibTable.setDescription('MPLS LDP Label Information Base table which contains LSPs that have been set up.')
wfMplsLdpLibEntry = MibTableRow((1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 15, 4, 1), ).setIndexNames((0, "Wellfleet-MPLS-LDP-MIB", "wfMplsLdpLibCct"), (0, "Wellfleet-MPLS-LDP-MIB", "wfMplsLdpLibSessId"), (0, "Wellfleet-MPLS-LDP-MIB", "wfMplsLdpLibDest"), (0, "Wellfleet-MPLS-LDP-MIB", "wfMplsLdpLibMid"), (0, "Wellfleet-MPLS-LDP-MIB", "wfMplsLdpLibIndex"))
if mibBuilder.loadTexts: wfMplsLdpLibEntry.setStatus('mandatory')
if mibBuilder.loadTexts: wfMplsLdpLibEntry.setDescription('MPLS LDP Label Information Base.')
wfMplsLdpLibCct = MibTableColumn((1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 15, 4, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 1023))).setMaxAccess("readonly")
if mibBuilder.loadTexts: wfMplsLdpLibCct.setStatus('mandatory')
if mibBuilder.loadTexts: wfMplsLdpLibCct.setDescription('The circuit munber to which the route associates with.')
wfMplsLdpLibSessId = MibTableColumn((1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 15, 4, 1, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 1023))).setMaxAccess("readonly")
if mibBuilder.loadTexts: wfMplsLdpLibSessId.setStatus('mandatory')
if mibBuilder.loadTexts: wfMplsLdpLibSessId.setDescription('The session identification munber to which the LIB entry associates with.')
wfMplsLdpLibDest = MibTableColumn((1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 15, 4, 1, 3), IpAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: wfMplsLdpLibDest.setStatus('mandatory')
if mibBuilder.loadTexts: wfMplsLdpLibDest.setDescription('The destnation network prefix.')
wfMplsLdpLibMid = MibTableColumn((1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 15, 4, 1, 4), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: wfMplsLdpLibMid.setStatus('mandatory')
if mibBuilder.loadTexts: wfMplsLdpLibMid.setDescription('The merge id.')
wfMplsLdpLibLabel = MibTableColumn((1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 15, 4, 1, 5), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: wfMplsLdpLibLabel.setStatus('mandatory')
if mibBuilder.loadTexts: wfMplsLdpLibLabel.setDescription('The label of the lsp that this LIB entry identifies.')
wfMplsLdpLibEncaps = MibTableColumn((1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 15, 4, 1, 6), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("llcsnap", 1), ("null", 2))).clone('llcsnap')).setMaxAccess("readonly")
if mibBuilder.loadTexts: wfMplsLdpLibEncaps.setStatus('mandatory')
if mibBuilder.loadTexts: wfMplsLdpLibEncaps.setDescription('The lsp encapsulation type.')
wfMplsLdpLibDirection = MibTableColumn((1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 15, 4, 1, 7), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("inbound", 1), ("outbound", 2), ("bidirectional", 3)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: wfMplsLdpLibDirection.setStatus('mandatory')
if mibBuilder.loadTexts: wfMplsLdpLibDirection.setDescription('MPLS VC direction.')
wfMplsLdpLibSlot = MibTableColumn((1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 15, 4, 1, 8), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: wfMplsLdpLibSlot.setStatus('mandatory')
if mibBuilder.loadTexts: wfMplsLdpLibSlot.setDescription('Slot on which this LSP got created')
wfMplsLdpLibIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 15, 4, 1, 9), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: wfMplsLdpLibIndex.setStatus('mandatory')
if mibBuilder.loadTexts: wfMplsLdpLibIndex.setDescription('Index part of instance id')
mibBuilder.exportSymbols("Wellfleet-MPLS-LDP-MIB", wfMplsLdpSessActualTable=wfMplsLdpSessActualTable, wfMplsLdpSessActualLocalTcpPort=wfMplsLdpSessActualLocalTcpPort, wfMplsLdpSessActualLocalIpAddress=wfMplsLdpSessActualLocalIpAddress, wfMplsLdpSessCfgCircuit=wfMplsLdpSessCfgCircuit, wfMplsLdpSessCfgDebugLevel=wfMplsLdpSessCfgDebugLevel, wfMplsLdpSessActualTCPConnectionRole=wfMplsLdpSessActualTCPConnectionRole, wfMplsLdpCfgRouteIndex=wfMplsLdpCfgRouteIndex, wfMplsLdpSessActualCircuit=wfMplsLdpSessActualCircuit, wfMplsLdpLibTable=wfMplsLdpLibTable, wfMplsLdpLibMid=wfMplsLdpLibMid, wfMplsLdpLibCct=wfMplsLdpLibCct, wfMplsLdpSessActualHoldTime=wfMplsLdpSessActualHoldTime, wfMplsLdpSessActualRoutesConfigMode=wfMplsLdpSessActualRoutesConfigMode, wfMplsLdpLibEncaps=wfMplsLdpLibEncaps, wfMplsLdpSessCfgEnable=wfMplsLdpSessCfgEnable, wfMplsLdpCfgRouteCct=wfMplsLdpCfgRouteCct, wfMplsLdpSessActualSlot=wfMplsLdpSessActualSlot, wfMplsLdpSessCfgSlot=wfMplsLdpSessCfgSlot, wfMplsLdpSessCfgRemoteIpAddress=wfMplsLdpSessCfgRemoteIpAddress, wfMplsLdpSessCfgHoldTime=wfMplsLdpSessCfgHoldTime, wfMplsLdpCfgRouteState=wfMplsLdpCfgRouteState, wfMplsLdpSessCfgCreate=wfMplsLdpSessCfgCreate, wfMplsLdpLibLabel=wfMplsLdpLibLabel, wfMplsLdpCfgRouteCreate=wfMplsLdpCfgRouteCreate, wfMplsLdpSessCfgLocalTcpPort=wfMplsLdpSessCfgLocalTcpPort, wfMplsLdpSessCfgAggregation=wfMplsLdpSessCfgAggregation, wfMplsLdpSessActualRemoteTcpPort=wfMplsLdpSessActualRemoteTcpPort, wfMplsLdpSessCfgLocalIpAddress=wfMplsLdpSessCfgLocalIpAddress, wfMplsLdpCfgRouteDestination=wfMplsLdpCfgRouteDestination, wfMplsLdpLibSlot=wfMplsLdpLibSlot, wfMplsLdpSessCfgIndex=wfMplsLdpSessCfgIndex, wfMplsLdpCfgRouteSessId=wfMplsLdpCfgRouteSessId, wfMplsLdpSessCfgTable=wfMplsLdpSessCfgTable, wfMplsLdpSessActualIndex=wfMplsLdpSessActualIndex, wfMplsLdpCfgRouteMask=wfMplsLdpCfgRouteMask, wfMplsLdpLibSessId=wfMplsLdpLibSessId, wfMplsLdpLibDest=wfMplsLdpLibDest, wfMplsLdpCfgRouteTable=wfMplsLdpCfgRouteTable, wfMplsLdpCfgRouteEntry=wfMplsLdpCfgRouteEntry, wfMplsLdpLibDirection=wfMplsLdpLibDirection, wfMplsLdpSessCfgRemoteTcpPort=wfMplsLdpSessCfgRemoteTcpPort, wfMplsLdpSessCfgProto=wfMplsLdpSessCfgProto, wfMplsLdpSessActualRemoteIpAddress=wfMplsLdpSessActualRemoteIpAddress, wfMplsLdpLibIndex=wfMplsLdpLibIndex, wfMplsLdpSessCfgRoutesConfigMode=wfMplsLdpSessCfgRoutesConfigMode, wfMplsLdpSessCfgReqBindRetries=wfMplsLdpSessCfgReqBindRetries, wfMplsLdpCfgRouteEnable=wfMplsLdpCfgRouteEnable, wfMplsLdpSessCfgReqBindRetryTime=wfMplsLdpSessCfgReqBindRetryTime, wfMplsLdpSessCfgEntry=wfMplsLdpSessCfgEntry, wfMplsLdpSessActualEntry=wfMplsLdpSessActualEntry, wfMplsLdpSessActualPeerState=wfMplsLdpSessActualPeerState, wfMplsLdpSessActualState=wfMplsLdpSessActualState, wfMplsLdpLibEntry=wfMplsLdpLibEntry)