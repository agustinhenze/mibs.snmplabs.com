#
# PySNMP MIB module Wellfleet-GRE-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/Wellfleet-GRE-MIB
# Produced by pysmi-0.3.4 at Wed May  1 15:40:19 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
OctetString, Integer, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "OctetString", "Integer", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
SingleValueConstraint, ValueRangeConstraint, ConstraintsIntersection, ConstraintsUnion, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "SingleValueConstraint", "ValueRangeConstraint", "ConstraintsIntersection", "ConstraintsUnion", "ValueSizeConstraint")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
TimeTicks, Unsigned32, Bits, IpAddress, ObjectIdentity, Counter32, iso, NotificationType, Gauge32, Counter64, MibIdentifier, ModuleIdentity, Integer32, MibScalar, MibTable, MibTableRow, MibTableColumn = mibBuilder.importSymbols("SNMPv2-SMI", "TimeTicks", "Unsigned32", "Bits", "IpAddress", "ObjectIdentity", "Counter32", "iso", "NotificationType", "Gauge32", "Counter64", "MibIdentifier", "ModuleIdentity", "Integer32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
wfGreGroup, = mibBuilder.importSymbols("Wellfleet-COMMON-MIB", "wfGreGroup")
wfGreInterfaceTable = MibTable((1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 20, 1), )
if mibBuilder.loadTexts: wfGreInterfaceTable.setStatus('mandatory')
if mibBuilder.loadTexts: wfGreInterfaceTable.setDescription('Parameters in wfGreInterfaceTable')
wfGreInterfaceEntry = MibTableRow((1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 20, 1, 1), ).setIndexNames((0, "Wellfleet-GRE-MIB", "wfGreIntfIpAddr"), (0, "Wellfleet-GRE-MIB", "wfGreIntfCct"))
if mibBuilder.loadTexts: wfGreInterfaceEntry.setStatus('mandatory')
if mibBuilder.loadTexts: wfGreInterfaceEntry.setDescription('An entry in wfGreTable.')
wfGreIntfCreate = MibTableColumn((1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 20, 1, 1, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("create", 1), ("delete", 2))).clone('create')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: wfGreIntfCreate.setStatus('mandatory')
if mibBuilder.loadTexts: wfGreIntfCreate.setDescription('Create/Delete parameter. Default is created. Users perform a set operation on this object in order to create/delete an wfGreEntry instance.')
wfGreIntfEnable = MibTableColumn((1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 20, 1, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enabled", 1), ("disabled", 2))).clone('enabled')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: wfGreIntfEnable.setStatus('mandatory')
if mibBuilder.loadTexts: wfGreIntfEnable.setDescription('Enable/Disable parameter. Default is enabled. Users perform a set operation on this object in order to enable/disable GRE .')
wfGreIntfState = MibTableColumn((1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 20, 1, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))).clone(namedValues=NamedValues(("up", 1), ("down", 2), ("init", 3), ("notpres", 4))).clone('notpres')).setMaxAccess("readonly")
if mibBuilder.loadTexts: wfGreIntfState.setStatus('mandatory')
if mibBuilder.loadTexts: wfGreIntfState.setDescription('The current state of GRE interface.')
wfGreIntfIpAddr = MibTableColumn((1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 20, 1, 1, 4), IpAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: wfGreIntfIpAddr.setStatus('mandatory')
if mibBuilder.loadTexts: wfGreIntfIpAddr.setDescription('The IP interface to run GRE on.')
wfGreIntfCct = MibTableColumn((1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 20, 1, 1, 5), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: wfGreIntfCct.setStatus('mandatory')
if mibBuilder.loadTexts: wfGreIntfCct.setDescription('Circuit number of the GRE interface')
wfGreIntfStatsEnable = MibTableColumn((1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 20, 1, 1, 6), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enabled", 1), ("disabled", 2))).clone('enabled')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: wfGreIntfStatsEnable.setStatus('mandatory')
if mibBuilder.loadTexts: wfGreIntfStatsEnable.setDescription('Enable/Disable parameter. Default is enabled. Users perform a set operation on this object in order to enable/disable mib statistics for GRE interface.')
wfGreIntfDebugLevel = MibTableColumn((1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 20, 1, 1, 7), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: wfGreIntfDebugLevel.setStatus('mandatory')
if mibBuilder.loadTexts: wfGreIntfDebugLevel.setDescription('A parameter to specify which messages to be printed in to the log.')
wfGreTunnelTable = MibTable((1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 20, 2), )
if mibBuilder.loadTexts: wfGreTunnelTable.setStatus('mandatory')
if mibBuilder.loadTexts: wfGreTunnelTable.setDescription('Parameters in wfGreTunnelTable')
wfGreTunnelEntry = MibTableRow((1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 20, 2, 1), ).setIndexNames((0, "Wellfleet-GRE-MIB", "wfGreTunnelLocalAddr"), (0, "Wellfleet-GRE-MIB", "wfGreTunnelPeerAddress"), (0, "Wellfleet-GRE-MIB", "wfGreTunnelLocalIndex"))
if mibBuilder.loadTexts: wfGreTunnelEntry.setStatus('mandatory')
if mibBuilder.loadTexts: wfGreTunnelEntry.setDescription('An entry in wfGreTunnelTable.')
wfGreTunnelLocalAddr = MibTableColumn((1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 20, 2, 1, 1), IpAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: wfGreTunnelLocalAddr.setStatus('mandatory')
if mibBuilder.loadTexts: wfGreTunnelLocalAddr.setDescription('IP Address of local interface.')
wfGreTunnelLocalIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 20, 2, 1, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 65535))).setMaxAccess("readonly")
if mibBuilder.loadTexts: wfGreTunnelLocalIndex.setStatus('mandatory')
if mibBuilder.loadTexts: wfGreTunnelLocalIndex.setDescription('This tunnel index is assigned by the GRE process. It is used to index into the GRE mapping table.')
wfGreTunnelType = MibTableColumn((1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 20, 2, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("generic", 1), ("udas", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: wfGreTunnelType.setStatus('mandatory')
if mibBuilder.loadTexts: wfGreTunnelType.setDescription('Indicate whether a tunnel peer has assigned a tunnel ID.')
wfGreTunnelId = MibTableColumn((1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 20, 2, 1, 4), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 65535))).setMaxAccess("readonly")
if mibBuilder.loadTexts: wfGreTunnelId.setStatus('mandatory')
if mibBuilder.loadTexts: wfGreTunnelId.setDescription('This tunnel ID is assigned by the tunnel peer.')
wfGreTunnelPeerAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 20, 2, 1, 5), IpAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: wfGreTunnelPeerAddress.setStatus('mandatory')
if mibBuilder.loadTexts: wfGreTunnelPeerAddress.setDescription('Address of the tunnel peer.')
wfGreRemotePayloadAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 20, 2, 1, 6), OctetString().subtype(subtypeSpec=ValueSizeConstraint(10, 10)).setFixedLength(10)).setMaxAccess("readonly")
if mibBuilder.loadTexts: wfGreRemotePayloadAddress.setStatus('deprecated')
if mibBuilder.loadTexts: wfGreRemotePayloadAddress.setDescription('The address of the remote node.')
wfGreTunnelState = MibTableColumn((1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 20, 2, 1, 7), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("up", 1), ("down", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: wfGreTunnelState.setStatus('mandatory')
if mibBuilder.loadTexts: wfGreTunnelState.setDescription('The state of the GRE tunnel.')
wfGreVersion = MibTableColumn((1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 20, 2, 1, 8), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: wfGreVersion.setStatus('mandatory')
if mibBuilder.loadTexts: wfGreVersion.setDescription('Reserved for future use')
wfGreProtoMap = MibTableColumn((1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 20, 2, 1, 9), OctetString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: wfGreProtoMap.setStatus('mandatory')
if mibBuilder.loadTexts: wfGreProtoMap.setDescription('This will be set to the protocol type of the payload. GRE_PROTO_IP 1 GRE_PROTO_IPX 2')
wfGreTunnelPktsTx = MibTableColumn((1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 20, 2, 1, 10), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: wfGreTunnelPktsTx.setStatus('mandatory')
if mibBuilder.loadTexts: wfGreTunnelPktsTx.setDescription('Number of packets transmitted ')
wfGreTunnelPktsRx = MibTableColumn((1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 20, 2, 1, 11), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: wfGreTunnelPktsRx.setStatus('mandatory')
if mibBuilder.loadTexts: wfGreTunnelPktsRx.setDescription('Number of packets received ')
wfGreTunnelBytesTx = MibTableColumn((1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 20, 2, 1, 12), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: wfGreTunnelBytesTx.setStatus('mandatory')
if mibBuilder.loadTexts: wfGreTunnelBytesTx.setDescription('Number of bytes transmitted ')
wfGreTunnelBytesRx = MibTableColumn((1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 20, 2, 1, 13), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: wfGreTunnelBytesRx.setStatus('mandatory')
if mibBuilder.loadTexts: wfGreTunnelBytesRx.setDescription('Number of bytes received')
wfGreTunnelPktsTxDropped = MibTableColumn((1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 20, 2, 1, 14), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: wfGreTunnelPktsTxDropped.setStatus('mandatory')
if mibBuilder.loadTexts: wfGreTunnelPktsTxDropped.setDescription('Number of outgoing packets dropped')
wfGreTunnelPktsRxDropped = MibTableColumn((1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 20, 2, 1, 15), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: wfGreTunnelPktsRxDropped.setStatus('mandatory')
if mibBuilder.loadTexts: wfGreTunnelPktsRxDropped.setDescription('Number of incoming packets dropped')
wfGreTunnelXsumErr = MibTableColumn((1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 20, 2, 1, 16), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: wfGreTunnelXsumErr.setStatus('mandatory')
if mibBuilder.loadTexts: wfGreTunnelXsumErr.setDescription('Number of inbound checksum errors')
wfGreTunnelSeqNumErr = MibTableColumn((1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 20, 2, 1, 17), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: wfGreTunnelSeqNumErr.setStatus('mandatory')
if mibBuilder.loadTexts: wfGreTunnelSeqNumErr.setDescription('Number of sequence errors')
wfGreTunnelMtu = MibTableColumn((1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 20, 2, 1, 18), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 4500))).setMaxAccess("readonly")
if mibBuilder.loadTexts: wfGreTunnelMtu.setStatus('mandatory')
if mibBuilder.loadTexts: wfGreTunnelMtu.setDescription('The MTU of the GRE tunnel')
mibBuilder.exportSymbols("Wellfleet-GRE-MIB", wfGreTunnelPktsTxDropped=wfGreTunnelPktsTxDropped, wfGreTunnelLocalIndex=wfGreTunnelLocalIndex, wfGreTunnelEntry=wfGreTunnelEntry, wfGreTunnelState=wfGreTunnelState, wfGreTunnelType=wfGreTunnelType, wfGreTunnelBytesRx=wfGreTunnelBytesRx, wfGreTunnelPktsRxDropped=wfGreTunnelPktsRxDropped, wfGreIntfCreate=wfGreIntfCreate, wfGreIntfState=wfGreIntfState, wfGreIntfIpAddr=wfGreIntfIpAddr, wfGreTunnelPeerAddress=wfGreTunnelPeerAddress, wfGreTunnelLocalAddr=wfGreTunnelLocalAddr, wfGreIntfEnable=wfGreIntfEnable, wfGreRemotePayloadAddress=wfGreRemotePayloadAddress, wfGreIntfStatsEnable=wfGreIntfStatsEnable, wfGreTunnelBytesTx=wfGreTunnelBytesTx, wfGreProtoMap=wfGreProtoMap, wfGreTunnelXsumErr=wfGreTunnelXsumErr, wfGreTunnelId=wfGreTunnelId, wfGreTunnelTable=wfGreTunnelTable, wfGreInterfaceTable=wfGreInterfaceTable, wfGreVersion=wfGreVersion, wfGreTunnelPktsTx=wfGreTunnelPktsTx, wfGreInterfaceEntry=wfGreInterfaceEntry, wfGreIntfDebugLevel=wfGreIntfDebugLevel, wfGreTunnelPktsRx=wfGreTunnelPktsRx, wfGreIntfCct=wfGreIntfCct, wfGreTunnelMtu=wfGreTunnelMtu, wfGreTunnelSeqNumErr=wfGreTunnelSeqNumErr)
