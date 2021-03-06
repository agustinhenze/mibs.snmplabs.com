#
# PySNMP MIB module HH3C-SNA-DLSW-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/HH3C-SNA-DLSW-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 19:16:54 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
OctetString, ObjectIdentifier, Integer = mibBuilder.importSymbols("ASN1", "OctetString", "ObjectIdentifier", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ValueSizeConstraint, ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ValueSizeConstraint", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion")
hh3cRhw, = mibBuilder.importSymbols("HH3C-OID-MIB", "hh3cRhw")
ifIndex, = mibBuilder.importSymbols("IF-MIB", "ifIndex")
NotificationGroup, ModuleCompliance, ObjectGroup = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance", "ObjectGroup")
Integer32, iso, NotificationType, MibIdentifier, MibScalar, MibTable, MibTableRow, MibTableColumn, ModuleIdentity, Bits, Gauge32, IpAddress, Counter64, TimeTicks, ObjectIdentity, Unsigned32, Counter32 = mibBuilder.importSymbols("SNMPv2-SMI", "Integer32", "iso", "NotificationType", "MibIdentifier", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "ModuleIdentity", "Bits", "Gauge32", "IpAddress", "Counter64", "TimeTicks", "ObjectIdentity", "Unsigned32", "Counter32")
DisplayString, TextualConvention, RowPointer, TruthValue = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention", "RowPointer", "TruthValue")
hh3cdlsw = ModuleIdentity((1, 3, 6, 1, 4, 1, 25506, 8, 37))
if mibBuilder.loadTexts: hh3cdlsw.setLastUpdated('200410301551Z')
if mibBuilder.loadTexts: hh3cdlsw.setOrganization('Hangzhou H3C Tech. Co., Ltd.')
class MacAddressNC(TextualConvention, OctetString):
    status = 'current'
    displayHint = '1x:'
    subtypeSpec = OctetString.subtypeSpec + ConstraintsUnion(ValueSizeConstraint(0, 0), ValueSizeConstraint(6, 6), )
class EndStationLocation(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))
    namedValues = NamedValues(("other", 1), ("internal", 2), ("remote", 3), ("local", 4))

class DlcType(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5))
    namedValues = NamedValues(("other", 1), ("na", 2), ("llc", 3), ("sdlc", 4), ("qllc", 5))

class LFSize(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(516, 1470, 1500, 2052, 4472, 8144, 11407, 11454, 17800, 65535))
    namedValues = NamedValues(("lfs516", 516), ("lfs1470", 1470), ("lfs1500", 1500), ("lfs2052", 2052), ("lfs4472", 4472), ("lfs8144", 8144), ("lfs11407", 11407), ("lfs11454", 11454), ("lfs17800", 17800), ("unknown", 65535))

class CreateLineFlag(Integer32):
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2))
    namedValues = NamedValues(("createLine", 1), ("deleteLine", 2))

class EntryStatus(Integer32):
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))
    namedValues = NamedValues(("valid", 1), ("createRequest", 2), ("underCreation", 3), ("invalid", 4))

hh3cdlswNode = MibIdentifier((1, 3, 6, 1, 4, 1, 25506, 8, 37, 1))
hh3cdlswTConn = MibIdentifier((1, 3, 6, 1, 4, 1, 25506, 8, 37, 2))
hh3cdlswBridgeGroup = MibIdentifier((1, 3, 6, 1, 4, 1, 25506, 8, 37, 3))
hh3cdlswLocDirectory = MibIdentifier((1, 3, 6, 1, 4, 1, 25506, 8, 37, 4))
hh3cdlswCircuit = MibIdentifier((1, 3, 6, 1, 4, 1, 25506, 8, 37, 5))
hh3cdlswSdlc = MibIdentifier((1, 3, 6, 1, 4, 1, 25506, 8, 37, 6))
hh3cdlswLlc2 = MibIdentifier((1, 3, 6, 1, 4, 1, 25506, 8, 37, 7))
hh3cdlswNodeVersion = MibScalar((1, 3, 6, 1, 4, 1, 25506, 8, 37, 1, 1), OctetString().subtype(subtypeSpec=ValueSizeConstraint(2, 2)).setFixedLength(2)).setMaxAccess("readonly")
if mibBuilder.loadTexts: hh3cdlswNodeVersion.setStatus('current')
hh3cdlswNodeVendorID = MibScalar((1, 3, 6, 1, 4, 1, 25506, 8, 37, 1, 2), OctetString().subtype(subtypeSpec=ValueSizeConstraint(3, 3)).setFixedLength(3)).setMaxAccess("readonly")
if mibBuilder.loadTexts: hh3cdlswNodeVendorID.setStatus('current')
hh3cdlswNodeVersionString = MibScalar((1, 3, 6, 1, 4, 1, 25506, 8, 37, 1, 3), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hh3cdlswNodeVersionString.setStatus('current')
hh3cdlswNodeStdPacingSupport = MibScalar((1, 3, 6, 1, 4, 1, 25506, 8, 37, 1, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 65535))).clone(namedValues=NamedValues(("none", 1), ("adaptiveRcvWindow", 2), ("fixedRcvWindow", 3), ("unknown", 65535)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: hh3cdlswNodeStdPacingSupport.setStatus('current')
hh3cdlswNodeStatus = MibScalar((1, 3, 6, 1, 4, 1, 25506, 8, 37, 1, 5), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("active", 1), ("inactive", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hh3cdlswNodeStatus.setStatus('current')
hh3cdlswNodeVirtualSegmentLFSize = MibScalar((1, 3, 6, 1, 4, 1, 25506, 8, 37, 1, 6), LFSize().clone('lfs1500')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hh3cdlswNodeVirtualSegmentLFSize.setStatus('current')
hh3cdlswNodeLocalAddr = MibScalar((1, 3, 6, 1, 4, 1, 25506, 8, 37, 1, 7), IpAddress()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hh3cdlswNodeLocalAddr.setStatus('current')
hh3cdlswNodePriority = MibScalar((1, 3, 6, 1, 4, 1, 25506, 8, 37, 1, 8), Integer32().subtype(subtypeSpec=ConstraintsUnion(ValueRangeConstraint(1, 5), ValueRangeConstraint(65535, 65535), )).clone(5)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hh3cdlswNodePriority.setStatus('current')
hh3cdlswNodeInitWindow = MibScalar((1, 3, 6, 1, 4, 1, 25506, 8, 37, 1, 9), Integer32().subtype(subtypeSpec=ConstraintsUnion(ValueRangeConstraint(1, 2000), ValueRangeConstraint(65535, 65535), )).clone(40)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hh3cdlswNodeInitWindow.setStatus('current')
hh3cdlswNodeKeepAlive = MibScalar((1, 3, 6, 1, 4, 1, 25506, 8, 37, 1, 10), Integer32().subtype(subtypeSpec=ConstraintsUnion(ValueRangeConstraint(1, 2000), ValueRangeConstraint(65535, 65535), )).clone(30)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hh3cdlswNodeKeepAlive.setStatus('current')
hh3cdlswNodeMaxWindow = MibScalar((1, 3, 6, 1, 4, 1, 25506, 8, 37, 1, 11), Integer32().subtype(subtypeSpec=ConstraintsUnion(ValueRangeConstraint(1, 2000), ValueRangeConstraint(65535, 65535), )).clone(255)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hh3cdlswNodeMaxWindow.setStatus('current')
hh3cdlswNodePermitDynamic = MibScalar((1, 3, 6, 1, 4, 1, 25506, 8, 37, 1, 12), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 65535))).clone(namedValues=NamedValues(("permit-dynamic", 1), ("forbid-dynamic", 2), ("unknown", 65535))).clone('forbid-dynamic')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hh3cdlswNodePermitDynamic.setStatus('current')
hh3cdlswNodeConnTimeout = MibScalar((1, 3, 6, 1, 4, 1, 25506, 8, 37, 1, 13), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 65535)).clone(300)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hh3cdlswNodeConnTimeout.setStatus('current')
hh3cdlswNodeLocalPendTimeout = MibScalar((1, 3, 6, 1, 4, 1, 25506, 8, 37, 1, 14), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 65535)).clone(30)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hh3cdlswNodeLocalPendTimeout.setStatus('current')
hh3cdlswNodeRemotePendTimeout = MibScalar((1, 3, 6, 1, 4, 1, 25506, 8, 37, 1, 15), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 65535)).clone(30)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hh3cdlswNodeRemotePendTimeout.setStatus('current')
hh3cdlswNodeSnaCacheTimeout = MibScalar((1, 3, 6, 1, 4, 1, 25506, 8, 37, 1, 16), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 65535)).clone(120)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hh3cdlswNodeSnaCacheTimeout.setStatus('current')
hh3cdlswRemotePeerTable = MibTable((1, 3, 6, 1, 4, 1, 25506, 8, 37, 2, 1), )
if mibBuilder.loadTexts: hh3cdlswRemotePeerTable.setStatus('current')
hh3cdlswRemotePeerEntry = MibTableRow((1, 3, 6, 1, 4, 1, 25506, 8, 37, 2, 1, 1), ).setIndexNames((0, "HH3C-SNA-DLSW-MIB", "hh3cdlswRemotePeerAddr"))
if mibBuilder.loadTexts: hh3cdlswRemotePeerEntry.setStatus('current')
hh3cdlswRemotePeerAddr = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 8, 37, 2, 1, 1, 1), IpAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hh3cdlswRemotePeerAddr.setStatus('current')
hh3cdlswRemotePeerVersion = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 8, 37, 2, 1, 1, 2), OctetString().subtype(subtypeSpec=ValueSizeConstraint(2, 2)).setFixedLength(2)).setMaxAccess("readonly")
if mibBuilder.loadTexts: hh3cdlswRemotePeerVersion.setStatus('current')
hh3cdlswRemotePeerVendorID = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 8, 37, 2, 1, 1, 3), OctetString().subtype(subtypeSpec=ValueSizeConstraint(3, 3)).setFixedLength(3)).setMaxAccess("readonly")
if mibBuilder.loadTexts: hh3cdlswRemotePeerVendorID.setStatus('current')
hh3cdlswRemotePeerPaceWindInit = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 8, 37, 2, 1, 1, 4), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hh3cdlswRemotePeerPaceWindInit.setStatus('current')
hh3cdlswRemotePeerVersionString = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 8, 37, 2, 1, 1, 5), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hh3cdlswRemotePeerVersionString.setStatus('current')
hh3cdlswRemotePeerIsConfig = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 8, 37, 2, 1, 1, 6), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("yes", 1), ("no", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: hh3cdlswRemotePeerIsConfig.setStatus('current')
hh3cdlswRemotePeerCost = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 8, 37, 2, 1, 1, 7), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 5))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hh3cdlswRemotePeerCost.setStatus('current')
hh3cdlswRemotePeerKeepAlive = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 8, 37, 2, 1, 1, 8), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 60000))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hh3cdlswRemotePeerKeepAlive.setStatus('current')
hh3cdlswRemotePeerLf = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 8, 37, 2, 1, 1, 9), LFSize()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hh3cdlswRemotePeerLf.setStatus('current')
hh3cdlswRemotePeerTcpQueneMax = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 8, 37, 2, 1, 1, 10), Integer32().subtype(subtypeSpec=ValueRangeConstraint(50, 2000))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hh3cdlswRemotePeerTcpQueneMax.setStatus('current')
hh3cdlswRemotePeerHaveBackup = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 8, 37, 2, 1, 1, 11), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("yes", 1), ("no", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: hh3cdlswRemotePeerHaveBackup.setStatus('current')
hh3cdlswRemotePeerIsBackup = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 8, 37, 2, 1, 1, 12), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("yes", 1), ("no", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: hh3cdlswRemotePeerIsBackup.setStatus('current')
hh3cdlswRemotePeerBackupAddr = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 8, 37, 2, 1, 1, 13), IpAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hh3cdlswRemotePeerBackupAddr.setStatus('current')
hh3cdlswRemotePeerLinger = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 8, 37, 2, 1, 1, 14), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 1440)).clone(5)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hh3cdlswRemotePeerLinger.setStatus('current')
hh3cdlswRemotePeerLinkState = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 8, 37, 2, 1, 1, 15), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6))).clone(namedValues=NamedValues(("connecting", 1), ("initCapExchange", 2), ("connected", 3), ("quiescing", 4), ("disconnecting", 5), ("disconnected", 6)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: hh3cdlswRemotePeerLinkState.setStatus('current')
hh3cdlswRemotePeerRecvPacks = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 8, 37, 2, 1, 1, 16), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hh3cdlswRemotePeerRecvPacks.setStatus('current')
hh3cdlswRemotePeerSendPacks = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 8, 37, 2, 1, 1, 17), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hh3cdlswRemotePeerSendPacks.setStatus('current')
hh3cdlswRemotePeerDrops = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 8, 37, 2, 1, 1, 18), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hh3cdlswRemotePeerDrops.setStatus('current')
hh3cdlswRemotePeerUptime = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 8, 37, 2, 1, 1, 19), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hh3cdlswRemotePeerUptime.setStatus('current')
hh3cdlswRemotePeerEntryStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 8, 37, 2, 1, 1, 20), EntryStatus()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hh3cdlswRemotePeerEntryStatus.setStatus('current')
hh3cdlswBridgeTable = MibTable((1, 3, 6, 1, 4, 1, 25506, 8, 37, 3, 1), )
if mibBuilder.loadTexts: hh3cdlswBridgeTable.setStatus('current')
hh3cdlswBridgeEntry = MibTableRow((1, 3, 6, 1, 4, 1, 25506, 8, 37, 3, 1, 1), ).setIndexNames((0, "HH3C-SNA-DLSW-MIB", "hh3cdlswBridgeNum"))
if mibBuilder.loadTexts: hh3cdlswBridgeEntry.setStatus('current')
hh3cdlswBridgeNum = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 8, 37, 3, 1, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 63))).setMaxAccess("readonly")
if mibBuilder.loadTexts: hh3cdlswBridgeNum.setStatus('current')
hh3cdlswBridgeStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 8, 37, 3, 1, 1, 2), CreateLineFlag()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hh3cdlswBridgeStatus.setStatus('current')
hh3cdlswBridgeIfTable = MibTable((1, 3, 6, 1, 4, 1, 25506, 8, 37, 3, 2), )
if mibBuilder.loadTexts: hh3cdlswBridgeIfTable.setStatus('current')
hh3cdlswBridgeIfEntry = MibTableRow((1, 3, 6, 1, 4, 1, 25506, 8, 37, 3, 2, 1), ).setIndexNames((0, "IF-MIB", "ifIndex"))
if mibBuilder.loadTexts: hh3cdlswBridgeIfEntry.setStatus('current')
hh3cdlswBridgeIfBriGru = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 8, 37, 3, 2, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 63))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hh3cdlswBridgeIfBriGru.setStatus('current')
hh3cdlswBridgeIfName = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 8, 37, 3, 2, 1, 2), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hh3cdlswBridgeIfName.setStatus('current')
hh3cdlswBridgeIfStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 8, 37, 3, 2, 1, 3), EntryStatus()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hh3cdlswBridgeIfStatus.setStatus('current')
hh3cdlswLocMacTable = MibTable((1, 3, 6, 1, 4, 1, 25506, 8, 37, 4, 1), )
if mibBuilder.loadTexts: hh3cdlswLocMacTable.setStatus('current')
hh3cdlswLocMacEntry = MibTableRow((1, 3, 6, 1, 4, 1, 25506, 8, 37, 4, 1, 1), ).setIndexNames((0, "HH3C-SNA-DLSW-MIB", "hh3cdlswLocMacHashIndex"), (0, "HH3C-SNA-DLSW-MIB", "hh3cdlswLocMacHashIndexSeqNum"))
if mibBuilder.loadTexts: hh3cdlswLocMacEntry.setStatus('current')
hh3cdlswLocMacHashIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 8, 37, 4, 1, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hh3cdlswLocMacHashIndex.setStatus('current')
hh3cdlswLocMacHashIndexSeqNum = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 8, 37, 4, 1, 1, 2), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hh3cdlswLocMacHashIndexSeqNum.setStatus('current')
hh3cdlswLocMacMac = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 8, 37, 4, 1, 1, 3), MacAddressNC()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hh3cdlswLocMacMac.setStatus('current')
hh3cdlswLocMacLocalInterfaceName = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 8, 37, 4, 1, 1, 4), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hh3cdlswLocMacLocalInterfaceName.setStatus('current')
hh3cdlswCircuitTable = MibTable((1, 3, 6, 1, 4, 1, 25506, 8, 37, 5, 1), )
if mibBuilder.loadTexts: hh3cdlswCircuitTable.setStatus('current')
hh3cdlswCircuitEntry = MibTableRow((1, 3, 6, 1, 4, 1, 25506, 8, 37, 5, 1, 1), ).setIndexNames((0, "HH3C-SNA-DLSW-MIB", "hh3cdlswCircuitS1CircuitId"))
if mibBuilder.loadTexts: hh3cdlswCircuitEntry.setStatus('current')
hh3cdlswCircuitS1CircuitId = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 8, 37, 5, 1, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hh3cdlswCircuitS1CircuitId.setStatus('current')
hh3cdlswCircuitS1Mac = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 8, 37, 5, 1, 1, 2), MacAddressNC()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hh3cdlswCircuitS1Mac.setStatus('current')
hh3cdlswCircuitS1Sap = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 8, 37, 5, 1, 1, 3), OctetString().subtype(subtypeSpec=ValueSizeConstraint(1, 1)).setFixedLength(1)).setMaxAccess("readonly")
if mibBuilder.loadTexts: hh3cdlswCircuitS1Sap.setStatus('current')
hh3cdlswCircuitS2Mac = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 8, 37, 5, 1, 1, 4), MacAddressNC()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hh3cdlswCircuitS2Mac.setStatus('current')
hh3cdlswCircuitS2Sap = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 8, 37, 5, 1, 1, 5), OctetString().subtype(subtypeSpec=ValueSizeConstraint(1, 1)).setFixedLength(1)).setMaxAccess("readonly")
if mibBuilder.loadTexts: hh3cdlswCircuitS2Sap.setStatus('current')
hh3cdlswCircuitS1IfIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 8, 37, 5, 1, 1, 6), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 2147483647))).setMaxAccess("readonly")
if mibBuilder.loadTexts: hh3cdlswCircuitS1IfIndex.setStatus('current')
hh3cdlswCircuitS1Ifname = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 8, 37, 5, 1, 1, 7), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hh3cdlswCircuitS1Ifname.setStatus('current')
hh3cdlswCircuitS1DlcType = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 8, 37, 5, 1, 1, 8), DlcType()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hh3cdlswCircuitS1DlcType.setStatus('current')
hh3cdlswCircuitS2TAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 8, 37, 5, 1, 1, 9), IpAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hh3cdlswCircuitS2TAddress.setStatus('current')
hh3cdlswCircuitS2CircuitId = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 8, 37, 5, 1, 1, 10), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hh3cdlswCircuitS2CircuitId.setStatus('current')
hh3cdlswCircuitOrigin = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 8, 37, 5, 1, 1, 11), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("s1", 1), ("s2", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: hh3cdlswCircuitOrigin.setStatus('current')
hh3cdlswCircuitEntryTime = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 8, 37, 5, 1, 1, 12), TimeTicks()).setUnits('hundredths of a second').setMaxAccess("readonly")
if mibBuilder.loadTexts: hh3cdlswCircuitEntryTime.setStatus('current')
hh3cdlswCircuitStateTime = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 8, 37, 5, 1, 1, 13), TimeTicks()).setUnits('hundredths of a second').setMaxAccess("readonly")
if mibBuilder.loadTexts: hh3cdlswCircuitStateTime.setStatus('current')
hh3cdlswCircuitState = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 8, 37, 5, 1, 1, 14), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13))).clone(namedValues=NamedValues(("disconnected", 1), ("circuitStart", 2), ("resolvePending", 3), ("circuitPending", 4), ("circuitEstablished", 5), ("connectPending", 6), ("contactPending", 7), ("connected", 8), ("disconnectPending", 9), ("haltPending", 10), ("haltPendingNoack", 11), ("circuitRestart", 12), ("restartPending", 13)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: hh3cdlswCircuitState.setStatus('current')
hh3cdlswCircuitFCSendGrantedUnits = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 8, 37, 5, 1, 1, 15), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 65535))).setMaxAccess("readonly")
if mibBuilder.loadTexts: hh3cdlswCircuitFCSendGrantedUnits.setStatus('current')
hh3cdlswCircuitFCSendCurrentWndw = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 8, 37, 5, 1, 1, 16), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 65535))).setMaxAccess("readonly")
if mibBuilder.loadTexts: hh3cdlswCircuitFCSendCurrentWndw.setStatus('current')
hh3cdlswCircuitFCRecvGrantedUnits = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 8, 37, 5, 1, 1, 17), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 65535))).setMaxAccess("readonly")
if mibBuilder.loadTexts: hh3cdlswCircuitFCRecvGrantedUnits.setStatus('current')
hh3cdlswCircuitFCRecvCurrentWndw = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 8, 37, 5, 1, 1, 18), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 65535))).setMaxAccess("readonly")
if mibBuilder.loadTexts: hh3cdlswCircuitFCRecvCurrentWndw.setStatus('current')
hh3cdlswSdlcPortTable = MibTable((1, 3, 6, 1, 4, 1, 25506, 8, 37, 6, 1), )
if mibBuilder.loadTexts: hh3cdlswSdlcPortTable.setStatus('current')
hh3cdlswSdlcPortEntry = MibTableRow((1, 3, 6, 1, 4, 1, 25506, 8, 37, 6, 1, 1), ).setIndexNames((0, "IF-MIB", "ifIndex"))
if mibBuilder.loadTexts: hh3cdlswSdlcPortEntry.setStatus('current')
hh3cdlswSdlcPortSerialName = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 8, 37, 6, 1, 1, 1), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hh3cdlswSdlcPortSerialName.setStatus('current')
hh3cdlswSdlcPortEncap = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 8, 37, 6, 1, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("sdlc", 1), ("ppp", 2), ("other", 3)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: hh3cdlswSdlcPortEncap.setStatus('current')
hh3cdlswSdlcPortRole = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 8, 37, 6, 1, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("primary", 1), ("seconday", 2), ("norole", 3))).clone('norole')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hh3cdlswSdlcPortRole.setStatus('current')
hh3cdlswSdlcPortVmac = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 8, 37, 6, 1, 1, 4), MacAddressNC()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hh3cdlswSdlcPortVmac.setStatus('current')
hh3cdlswSdlcPortHoldq = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 8, 37, 6, 1, 1, 5), Integer32().subtype(subtypeSpec=ValueRangeConstraint(20, 255)).clone(50)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hh3cdlswSdlcPortHoldq.setStatus('current')
hh3cdlswSdlcPortK = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 8, 37, 6, 1, 1, 6), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 7)).clone(7)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hh3cdlswSdlcPortK.setStatus('current')
hh3cdlswSdlcPortModule = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 8, 37, 6, 1, 1, 7), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(8, 128))).clone(namedValues=NamedValues(("m8", 8), ("m128", 128))).clone('m8')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hh3cdlswSdlcPortModule.setStatus('current')
hh3cdlswSdlcPortN1 = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 8, 37, 6, 1, 1, 8), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 17680)).clone(265)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hh3cdlswSdlcPortN1.setStatus('current')
hh3cdlswSdlcPortN2 = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 8, 37, 6, 1, 1, 9), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 255)).clone(20)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hh3cdlswSdlcPortN2.setStatus('current')
hh3cdlswSdlcPortPollPauseTimer = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 8, 37, 6, 1, 1, 10), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 10000)).clone(100)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hh3cdlswSdlcPortPollPauseTimer.setStatus('current')
hh3cdlswSdlcPortSimultaneousEnable = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 8, 37, 6, 1, 1, 11), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enable", 1), ("disenable", 2))).clone(1)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hh3cdlswSdlcPortSimultaneousEnable.setStatus('current')
hh3cdlswSdlcPortT1 = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 8, 37, 6, 1, 1, 12), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 60000)).clone(3000)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hh3cdlswSdlcPortT1.setStatus('current')
hh3cdlswSdlcPortT2 = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 8, 37, 6, 1, 1, 13), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 60000)).clone(500)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hh3cdlswSdlcPortT2.setStatus('current')
hh3cdlswSdlcLsTable = MibTable((1, 3, 6, 1, 4, 1, 25506, 8, 37, 6, 2), )
if mibBuilder.loadTexts: hh3cdlswSdlcLsTable.setStatus('current')
hh3cdlswSdlcLsEntry = MibTableRow((1, 3, 6, 1, 4, 1, 25506, 8, 37, 6, 2, 1), ).setIndexNames((0, "IF-MIB", "ifIndex"), (0, "HH3C-SNA-DLSW-MIB", "hh3cdlswSdlcLsAddress"))
if mibBuilder.loadTexts: hh3cdlswSdlcLsEntry.setStatus('current')
hh3cdlswSdlcLsAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 8, 37, 6, 2, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 254))).setMaxAccess("readonly")
if mibBuilder.loadTexts: hh3cdlswSdlcLsAddress.setStatus('current')
hh3cdlswSdlcLsLocalId = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 8, 37, 6, 2, 1, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 2147483647))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hh3cdlswSdlcLsLocalId.setStatus('current')
hh3cdlswSdlcLsRemoteMac = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 8, 37, 6, 2, 1, 3), MacAddressNC()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hh3cdlswSdlcLsRemoteMac.setStatus('current')
hh3cdlswSdlcLsSsap = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 8, 37, 6, 2, 1, 4), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 254))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hh3cdlswSdlcLsSsap.setStatus('current')
hh3cdlswSdlcLsDsap = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 8, 37, 6, 2, 1, 5), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 254))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hh3cdlswSdlcLsDsap.setStatus('current')
hh3cdlswSdlcLsStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 8, 37, 6, 2, 1, 6), EntryStatus()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hh3cdlswSdlcLsStatus.setStatus('current')
hh3cdlswLlc2PortTable = MibTable((1, 3, 6, 1, 4, 1, 25506, 8, 37, 7, 1), )
if mibBuilder.loadTexts: hh3cdlswLlc2PortTable.setStatus('current')
hh3cdlswLlc2PortEntry = MibTableRow((1, 3, 6, 1, 4, 1, 25506, 8, 37, 7, 1, 1), ).setIndexNames((0, "IF-MIB", "ifIndex"), (0, "HH3C-SNA-DLSW-MIB", "hh3cdlswBridgeIfBriGru"))
if mibBuilder.loadTexts: hh3cdlswLlc2PortEntry.setStatus('current')
hh3cdlswLLC2PortAckDelayTime = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 8, 37, 7, 1, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 60000)).clone(100)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hh3cdlswLLC2PortAckDelayTime.setStatus('current')
hh3cdlswLLC2PortAckMax = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 8, 37, 7, 1, 1, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 127)).clone(3)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hh3cdlswLLC2PortAckMax.setStatus('current')
hh3cdlswLLC2PortLocalWnd = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 8, 37, 7, 1, 1, 3), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 127)).clone(7)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hh3cdlswLLC2PortLocalWnd.setStatus('current')
hh3cdlswLLC2PortModulus = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 8, 37, 7, 1, 1, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(8, 128))).clone(namedValues=NamedValues(("m8", 8), ("m128", 128))).clone('m128')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hh3cdlswLLC2PortModulus.setStatus('current')
hh3cdlswLLC2PortN2 = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 8, 37, 7, 1, 1, 5), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 255)).clone(20)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hh3cdlswLLC2PortN2.setStatus('current')
hh3cdlswLLC2PortT1 = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 8, 37, 7, 1, 1, 6), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 60000)).clone(200)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hh3cdlswLLC2PortT1.setStatus('current')
hh3cdlswLLC2PortTbusyTime = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 8, 37, 7, 1, 1, 7), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 60000)).clone(300)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hh3cdlswLLC2PortTbusyTime.setStatus('current')
hh3cdlswLLC2PortTpfTime = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 8, 37, 7, 1, 1, 8), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 60000)).clone(500)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hh3cdlswLLC2PortTpfTime.setStatus('current')
hh3cdlswLLC2PortTrejTime = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 8, 37, 7, 1, 1, 9), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 60000)).clone(500)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hh3cdlswLLC2PortTrejTime.setStatus('current')
hh3cdlswLLC2PortTxqMax = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 8, 37, 7, 1, 1, 10), Integer32().subtype(subtypeSpec=ValueRangeConstraint(20, 200)).clone(50)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hh3cdlswLLC2PortTxqMax.setStatus('current')
hh3cdlswTrapControl = MibIdentifier((1, 3, 6, 1, 4, 1, 25506, 8, 37, 1, 20))
hh3cdlswTrapCntlState = MibScalar((1, 3, 6, 1, 4, 1, 25506, 8, 37, 1, 20, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enabled", 1), ("disabled", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hh3cdlswTrapCntlState.setStatus('current')
hh3cdlswTraps = MibIdentifier((1, 3, 6, 1, 4, 1, 25506, 8, 37, 8))
hh3cdlswTrapsV2 = MibIdentifier((1, 3, 6, 1, 4, 1, 25506, 8, 37, 8, 0))
hh3cdlswTrapTConnPartnerReject = NotificationType((1, 3, 6, 1, 4, 1, 25506, 8, 37, 8, 0, 1)).setObjects(("HH3C-SNA-DLSW-MIB", "hh3cdlswRemotePeerAddr"))
if mibBuilder.loadTexts: hh3cdlswTrapTConnPartnerReject.setStatus('current')
hh3cdlswTrapTConnChangeState = NotificationType((1, 3, 6, 1, 4, 1, 25506, 8, 37, 8, 0, 2)).setObjects(("HH3C-SNA-DLSW-MIB", "hh3cdlswRemotePeerAddr"), ("HH3C-SNA-DLSW-MIB", "hh3cdlswRemotePeerLinkState"))
if mibBuilder.loadTexts: hh3cdlswTrapTConnChangeState.setStatus('current')
hh3cdlswTrapCircuitChangeState = NotificationType((1, 3, 6, 1, 4, 1, 25506, 8, 37, 8, 0, 3)).setObjects(("HH3C-SNA-DLSW-MIB", "hh3cdlswCircuitS1CircuitId"), ("HH3C-SNA-DLSW-MIB", "hh3cdlswCircuitState"), ("HH3C-SNA-DLSW-MIB", "hh3cdlswCircuitS1Mac"), ("HH3C-SNA-DLSW-MIB", "hh3cdlswCircuitS1Sap"), ("HH3C-SNA-DLSW-MIB", "hh3cdlswCircuitS2Mac"), ("HH3C-SNA-DLSW-MIB", "hh3cdlswCircuitS2Sap"))
if mibBuilder.loadTexts: hh3cdlswTrapCircuitChangeState.setStatus('current')
mibBuilder.exportSymbols("HH3C-SNA-DLSW-MIB", hh3cdlswBridgeIfTable=hh3cdlswBridgeIfTable, hh3cdlswSdlcLsEntry=hh3cdlswSdlcLsEntry, hh3cdlswNodeLocalPendTimeout=hh3cdlswNodeLocalPendTimeout, hh3cdlswRemotePeerEntry=hh3cdlswRemotePeerEntry, hh3cdlswBridgeIfEntry=hh3cdlswBridgeIfEntry, hh3cdlswBridgeStatus=hh3cdlswBridgeStatus, hh3cdlswLLC2PortAckDelayTime=hh3cdlswLLC2PortAckDelayTime, hh3cdlswRemotePeerSendPacks=hh3cdlswRemotePeerSendPacks, hh3cdlswNodeVersionString=hh3cdlswNodeVersionString, hh3cdlswBridgeEntry=hh3cdlswBridgeEntry, hh3cdlswLLC2PortTpfTime=hh3cdlswLLC2PortTpfTime, hh3cdlswRemotePeerKeepAlive=hh3cdlswRemotePeerKeepAlive, hh3cdlswCircuitS1Sap=hh3cdlswCircuitS1Sap, hh3cdlswTraps=hh3cdlswTraps, hh3cdlswNodeInitWindow=hh3cdlswNodeInitWindow, hh3cdlswSdlcPortT1=hh3cdlswSdlcPortT1, hh3cdlswTrapControl=hh3cdlswTrapControl, hh3cdlswSdlcLsStatus=hh3cdlswSdlcLsStatus, hh3cdlswCircuitS2TAddress=hh3cdlswCircuitS2TAddress, hh3cdlswLLC2PortTbusyTime=hh3cdlswLLC2PortTbusyTime, hh3cdlswNodeLocalAddr=hh3cdlswNodeLocalAddr, hh3cdlswLocMacTable=hh3cdlswLocMacTable, hh3cdlswTrapCntlState=hh3cdlswTrapCntlState, hh3cdlswCircuitS1Ifname=hh3cdlswCircuitS1Ifname, hh3cdlswSdlcLsRemoteMac=hh3cdlswSdlcLsRemoteMac, hh3cdlswSdlcPortSerialName=hh3cdlswSdlcPortSerialName, hh3cdlswSdlcPortT2=hh3cdlswSdlcPortT2, LFSize=LFSize, hh3cdlswNodePriority=hh3cdlswNodePriority, hh3cdlswLLC2PortTxqMax=hh3cdlswLLC2PortTxqMax, hh3cdlswRemotePeerHaveBackup=hh3cdlswRemotePeerHaveBackup, hh3cdlswNodeMaxWindow=hh3cdlswNodeMaxWindow, hh3cdlswSdlcPortModule=hh3cdlswSdlcPortModule, hh3cdlswLlc2PortEntry=hh3cdlswLlc2PortEntry, hh3cdlswLLC2PortLocalWnd=hh3cdlswLLC2PortLocalWnd, hh3cdlswNodePermitDynamic=hh3cdlswNodePermitDynamic, hh3cdlswBridgeGroup=hh3cdlswBridgeGroup, hh3cdlswRemotePeerUptime=hh3cdlswRemotePeerUptime, hh3cdlswLLC2PortTrejTime=hh3cdlswLLC2PortTrejTime, hh3cdlswNodeSnaCacheTimeout=hh3cdlswNodeSnaCacheTimeout, PYSNMP_MODULE_ID=hh3cdlsw, hh3cdlswRemotePeerTcpQueneMax=hh3cdlswRemotePeerTcpQueneMax, hh3cdlswCircuitS2Mac=hh3cdlswCircuitS2Mac, hh3cdlswNodeRemotePendTimeout=hh3cdlswNodeRemotePendTimeout, hh3cdlswBridgeNum=hh3cdlswBridgeNum, hh3cdlswBridgeIfBriGru=hh3cdlswBridgeIfBriGru, hh3cdlswCircuitS2CircuitId=hh3cdlswCircuitS2CircuitId, hh3cdlswCircuitStateTime=hh3cdlswCircuitStateTime, hh3cdlswLlc2=hh3cdlswLlc2, hh3cdlswLocMacMac=hh3cdlswLocMacMac, hh3cdlswRemotePeerVersion=hh3cdlswRemotePeerVersion, hh3cdlswSdlcPortPollPauseTimer=hh3cdlswSdlcPortPollPauseTimer, hh3cdlswCircuitFCSendCurrentWndw=hh3cdlswCircuitFCSendCurrentWndw, EntryStatus=EntryStatus, hh3cdlswNode=hh3cdlswNode, hh3cdlswTrapTConnPartnerReject=hh3cdlswTrapTConnPartnerReject, hh3cdlswSdlcPortTable=hh3cdlswSdlcPortTable, hh3cdlswCircuitS2Sap=hh3cdlswCircuitS2Sap, hh3cdlswCircuit=hh3cdlswCircuit, hh3cdlswSdlcLsTable=hh3cdlswSdlcLsTable, hh3cdlswSdlcPortN2=hh3cdlswSdlcPortN2, hh3cdlswNodeKeepAlive=hh3cdlswNodeKeepAlive, hh3cdlswTrapsV2=hh3cdlswTrapsV2, hh3cdlswSdlcPortN1=hh3cdlswSdlcPortN1, hh3cdlswLocMacEntry=hh3cdlswLocMacEntry, hh3cdlswSdlcPortEncap=hh3cdlswSdlcPortEncap, hh3cdlswRemotePeerCost=hh3cdlswRemotePeerCost, hh3cdlswSdlcLsAddress=hh3cdlswSdlcLsAddress, hh3cdlswLLC2PortAckMax=hh3cdlswLLC2PortAckMax, hh3cdlswBridgeIfName=hh3cdlswBridgeIfName, EndStationLocation=EndStationLocation, DlcType=DlcType, hh3cdlswRemotePeerVendorID=hh3cdlswRemotePeerVendorID, MacAddressNC=MacAddressNC, hh3cdlswLLC2PortN2=hh3cdlswLLC2PortN2, hh3cdlswTrapTConnChangeState=hh3cdlswTrapTConnChangeState, hh3cdlswCircuitS1DlcType=hh3cdlswCircuitS1DlcType, hh3cdlswSdlcPortHoldq=hh3cdlswSdlcPortHoldq, hh3cdlswCircuitFCRecvGrantedUnits=hh3cdlswCircuitFCRecvGrantedUnits, hh3cdlswRemotePeerIsConfig=hh3cdlswRemotePeerIsConfig, hh3cdlswSdlcPortSimultaneousEnable=hh3cdlswSdlcPortSimultaneousEnable, hh3cdlswSdlc=hh3cdlswSdlc, hh3cdlswLocMacHashIndexSeqNum=hh3cdlswLocMacHashIndexSeqNum, hh3cdlswSdlcLsLocalId=hh3cdlswSdlcLsLocalId, hh3cdlswSdlcLsSsap=hh3cdlswSdlcLsSsap, hh3cdlswCircuitEntryTime=hh3cdlswCircuitEntryTime, hh3cdlswCircuitS1Mac=hh3cdlswCircuitS1Mac, hh3cdlswLocDirectory=hh3cdlswLocDirectory, hh3cdlswCircuitFCRecvCurrentWndw=hh3cdlswCircuitFCRecvCurrentWndw, hh3cdlswTConn=hh3cdlswTConn, hh3cdlswRemotePeerIsBackup=hh3cdlswRemotePeerIsBackup, hh3cdlswNodeVirtualSegmentLFSize=hh3cdlswNodeVirtualSegmentLFSize, hh3cdlswLocMacHashIndex=hh3cdlswLocMacHashIndex, hh3cdlswRemotePeerAddr=hh3cdlswRemotePeerAddr, hh3cdlswSdlcPortK=hh3cdlswSdlcPortK, hh3cdlswRemotePeerLinkState=hh3cdlswRemotePeerLinkState, hh3cdlswRemotePeerRecvPacks=hh3cdlswRemotePeerRecvPacks, hh3cdlswNodeStatus=hh3cdlswNodeStatus, hh3cdlswLLC2PortT1=hh3cdlswLLC2PortT1, hh3cdlswCircuitEntry=hh3cdlswCircuitEntry, hh3cdlswRemotePeerLf=hh3cdlswRemotePeerLf, hh3cdlsw=hh3cdlsw, hh3cdlswCircuitOrigin=hh3cdlswCircuitOrigin, hh3cdlswNodeVersion=hh3cdlswNodeVersion, hh3cdlswRemotePeerVersionString=hh3cdlswRemotePeerVersionString, hh3cdlswBridgeTable=hh3cdlswBridgeTable, hh3cdlswLocMacLocalInterfaceName=hh3cdlswLocMacLocalInterfaceName, hh3cdlswSdlcPortRole=hh3cdlswSdlcPortRole, hh3cdlswRemotePeerPaceWindInit=hh3cdlswRemotePeerPaceWindInit, hh3cdlswBridgeIfStatus=hh3cdlswBridgeIfStatus, hh3cdlswCircuitS1IfIndex=hh3cdlswCircuitS1IfIndex, hh3cdlswRemotePeerEntryStatus=hh3cdlswRemotePeerEntryStatus, hh3cdlswSdlcPortVmac=hh3cdlswSdlcPortVmac, CreateLineFlag=CreateLineFlag, hh3cdlswLlc2PortTable=hh3cdlswLlc2PortTable, hh3cdlswRemotePeerDrops=hh3cdlswRemotePeerDrops, hh3cdlswCircuitS1CircuitId=hh3cdlswCircuitS1CircuitId, hh3cdlswLLC2PortModulus=hh3cdlswLLC2PortModulus, hh3cdlswRemotePeerTable=hh3cdlswRemotePeerTable, hh3cdlswSdlcPortEntry=hh3cdlswSdlcPortEntry, hh3cdlswCircuitFCSendGrantedUnits=hh3cdlswCircuitFCSendGrantedUnits, hh3cdlswSdlcLsDsap=hh3cdlswSdlcLsDsap, hh3cdlswCircuitTable=hh3cdlswCircuitTable, hh3cdlswTrapCircuitChangeState=hh3cdlswTrapCircuitChangeState, hh3cdlswNodeConnTimeout=hh3cdlswNodeConnTimeout, hh3cdlswNodeVendorID=hh3cdlswNodeVendorID, hh3cdlswRemotePeerBackupAddr=hh3cdlswRemotePeerBackupAddr, hh3cdlswNodeStdPacingSupport=hh3cdlswNodeStdPacingSupport, hh3cdlswRemotePeerLinger=hh3cdlswRemotePeerLinger, hh3cdlswCircuitState=hh3cdlswCircuitState)
