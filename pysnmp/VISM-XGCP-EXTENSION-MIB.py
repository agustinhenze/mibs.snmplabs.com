#
# PySNMP MIB module VISM-XGCP-EXTENSION-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/VISM-XGCP-EXTENSION-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 21:27:38 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
OctetString, Integer, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "OctetString", "Integer", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, ValueSizeConstraint, ConstraintsIntersection, ConstraintsUnion, SingleValueConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "ValueSizeConstraint", "ConstraintsIntersection", "ConstraintsUnion", "SingleValueConstraint")
voice, = mibBuilder.importSymbols("BASIS-MIB", "voice")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
TimeTicks, NotificationType, Integer32, ObjectIdentity, Counter64, Bits, iso, MibScalar, MibTable, MibTableRow, MibTableColumn, Unsigned32, IpAddress, ModuleIdentity, MibIdentifier, Gauge32, Counter32 = mibBuilder.importSymbols("SNMPv2-SMI", "TimeTicks", "NotificationType", "Integer32", "ObjectIdentity", "Counter64", "Bits", "iso", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Unsigned32", "IpAddress", "ModuleIdentity", "MibIdentifier", "Gauge32", "Counter32")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
vismXgcpExtensionGrp = MibIdentifier((1, 3, 6, 1, 4, 1, 351, 110, 5, 5, 5))
vismXgcpCoreObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 351, 110, 5, 5, 5, 1))
vismXgcpEnhancementsObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 351, 110, 5, 5, 5, 2))
vismXgcpRequestMaxTimeout = MibScalar((1, 3, 6, 1, 4, 1, 351, 110, 5, 5, 5, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 100000)).clone(500)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: vismXgcpRequestMaxTimeout.setStatus('mandatory')
vismXgcpPort = MibScalar((1, 3, 6, 1, 4, 1, 351, 110, 5, 5, 5, 1, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1025, 65535)).clone(2427)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: vismXgcpPort.setStatus('mandatory')
vismXgcpPeerTable = MibTable((1, 3, 6, 1, 4, 1, 351, 110, 5, 5, 5, 1, 3), )
if mibBuilder.loadTexts: vismXgcpPeerTable.setStatus('mandatory')
vismXgcpPeerEntry = MibTableRow((1, 3, 6, 1, 4, 1, 351, 110, 5, 5, 5, 1, 3, 1), ).setIndexNames((0, "VISM-XGCP-EXTENSION-MIB", "vismXgcpPeerNumber"), (0, "VISM-XGCP-EXTENSION-MIB", "vismXgcpPeerProtocolNumber"))
if mibBuilder.loadTexts: vismXgcpPeerEntry.setStatus('mandatory')
vismXgcpPeerNumber = MibTableColumn((1, 3, 6, 1, 4, 1, 351, 110, 5, 5, 5, 1, 3, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 8))).setMaxAccess("readonly")
if mibBuilder.loadTexts: vismXgcpPeerNumber.setStatus('mandatory')
vismXgcpPeerProtocolNumber = MibTableColumn((1, 3, 6, 1, 4, 1, 351, 110, 5, 5, 5, 1, 3, 1, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 8))).setMaxAccess("readonly")
if mibBuilder.loadTexts: vismXgcpPeerProtocolNumber.setStatus('mandatory')
vismXgcpPeerPort = MibTableColumn((1, 3, 6, 1, 4, 1, 351, 110, 5, 5, 5, 1, 3, 1, 3), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1025, 65535)).clone(2427)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: vismXgcpPeerPort.setStatus('mandatory')
vismXgcpMsgStatTable = MibTable((1, 3, 6, 1, 4, 1, 351, 110, 5, 5, 5, 1, 4), )
if mibBuilder.loadTexts: vismXgcpMsgStatTable.setStatus('mandatory')
vismXgcpMsgStatEntry = MibTableRow((1, 3, 6, 1, 4, 1, 351, 110, 5, 5, 5, 1, 4, 1), ).setIndexNames((0, "VISM-XGCP-EXTENSION-MIB", "vismXgcpIpAddress"))
if mibBuilder.loadTexts: vismXgcpMsgStatEntry.setStatus('mandatory')
vismXgcpIpAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 351, 110, 5, 5, 5, 1, 4, 1, 1), IpAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: vismXgcpIpAddress.setStatus('mandatory')
vismXgcpCrcxCnts = MibTableColumn((1, 3, 6, 1, 4, 1, 351, 110, 5, 5, 5, 1, 4, 1, 2), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: vismXgcpCrcxCnts.setStatus('mandatory')
vismXgcpCrcxFailCnts = MibTableColumn((1, 3, 6, 1, 4, 1, 351, 110, 5, 5, 5, 1, 4, 1, 3), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: vismXgcpCrcxFailCnts.setStatus('mandatory')
vismXgcpMdcxCnts = MibTableColumn((1, 3, 6, 1, 4, 1, 351, 110, 5, 5, 5, 1, 4, 1, 4), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: vismXgcpMdcxCnts.setStatus('mandatory')
vismXgcpMdcxFailCnts = MibTableColumn((1, 3, 6, 1, 4, 1, 351, 110, 5, 5, 5, 1, 4, 1, 5), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: vismXgcpMdcxFailCnts.setStatus('mandatory')
vismXgcpDlcxRcvCnts = MibTableColumn((1, 3, 6, 1, 4, 1, 351, 110, 5, 5, 5, 1, 4, 1, 6), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: vismXgcpDlcxRcvCnts.setStatus('mandatory')
vismXgcpDlcxRcvFailCnts = MibTableColumn((1, 3, 6, 1, 4, 1, 351, 110, 5, 5, 5, 1, 4, 1, 7), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: vismXgcpDlcxRcvFailCnts.setStatus('mandatory')
vismXgcpDlcxSentCnts = MibTableColumn((1, 3, 6, 1, 4, 1, 351, 110, 5, 5, 5, 1, 4, 1, 8), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: vismXgcpDlcxSentCnts.setStatus('mandatory')
vismXgcpDlcxSentFailCnts = MibTableColumn((1, 3, 6, 1, 4, 1, 351, 110, 5, 5, 5, 1, 4, 1, 9), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: vismXgcpDlcxSentFailCnts.setStatus('mandatory')
vismXgcpRqntCnts = MibTableColumn((1, 3, 6, 1, 4, 1, 351, 110, 5, 5, 5, 1, 4, 1, 10), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: vismXgcpRqntCnts.setStatus('mandatory')
vismXgcpRqntFailCnts = MibTableColumn((1, 3, 6, 1, 4, 1, 351, 110, 5, 5, 5, 1, 4, 1, 11), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: vismXgcpRqntFailCnts.setStatus('mandatory')
vismXgcpNtfyCnts = MibTableColumn((1, 3, 6, 1, 4, 1, 351, 110, 5, 5, 5, 1, 4, 1, 12), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: vismXgcpNtfyCnts.setStatus('mandatory')
vismXgcpNtfyFailCnts = MibTableColumn((1, 3, 6, 1, 4, 1, 351, 110, 5, 5, 5, 1, 4, 1, 13), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: vismXgcpNtfyFailCnts.setStatus('mandatory')
vismXgcpAuepCnts = MibTableColumn((1, 3, 6, 1, 4, 1, 351, 110, 5, 5, 5, 1, 4, 1, 14), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: vismXgcpAuepCnts.setStatus('mandatory')
vismXgcpAuepFailCnts = MibTableColumn((1, 3, 6, 1, 4, 1, 351, 110, 5, 5, 5, 1, 4, 1, 15), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: vismXgcpAuepFailCnts.setStatus('mandatory')
vismXgcpAucxCnts = MibTableColumn((1, 3, 6, 1, 4, 1, 351, 110, 5, 5, 5, 1, 4, 1, 16), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: vismXgcpAucxCnts.setStatus('mandatory')
vismXgcpAucxFailCnts = MibTableColumn((1, 3, 6, 1, 4, 1, 351, 110, 5, 5, 5, 1, 4, 1, 17), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: vismXgcpAucxFailCnts.setStatus('mandatory')
vismXgcpRsipCnts = MibTableColumn((1, 3, 6, 1, 4, 1, 351, 110, 5, 5, 5, 1, 4, 1, 18), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: vismXgcpRsipCnts.setStatus('mandatory')
vismXgcpRsipFailCnts = MibTableColumn((1, 3, 6, 1, 4, 1, 351, 110, 5, 5, 5, 1, 4, 1, 19), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: vismXgcpRsipFailCnts.setStatus('mandatory')
vismXgcpRestartInProgressTdinit = MibScalar((1, 3, 6, 1, 4, 1, 351, 110, 5, 5, 5, 2, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 100)).clone(15)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: vismXgcpRestartInProgressTdinit.setStatus('mandatory')
vismXgcpRestartInProgressTdmin = MibScalar((1, 3, 6, 1, 4, 1, 351, 110, 5, 5, 5, 2, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 100)).clone(15)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: vismXgcpRestartInProgressTdmin.setStatus('mandatory')
vismXgcpRestartInProgressTdmax = MibScalar((1, 3, 6, 1, 4, 1, 351, 110, 5, 5, 5, 2, 3), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 5000)).clone(600)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: vismXgcpRestartInProgressTdmax.setStatus('mandatory')
mibBuilder.exportSymbols("VISM-XGCP-EXTENSION-MIB", vismXgcpMdcxFailCnts=vismXgcpMdcxFailCnts, vismXgcpRsipFailCnts=vismXgcpRsipFailCnts, vismXgcpRestartInProgressTdinit=vismXgcpRestartInProgressTdinit, vismXgcpRestartInProgressTdmin=vismXgcpRestartInProgressTdmin, vismXgcpPeerProtocolNumber=vismXgcpPeerProtocolNumber, vismXgcpCrcxCnts=vismXgcpCrcxCnts, vismXgcpPeerPort=vismXgcpPeerPort, vismXgcpRequestMaxTimeout=vismXgcpRequestMaxTimeout, vismXgcpPeerEntry=vismXgcpPeerEntry, vismXgcpAuepCnts=vismXgcpAuepCnts, vismXgcpCrcxFailCnts=vismXgcpCrcxFailCnts, vismXgcpAuepFailCnts=vismXgcpAuepFailCnts, vismXgcpNtfyFailCnts=vismXgcpNtfyFailCnts, vismXgcpExtensionGrp=vismXgcpExtensionGrp, vismXgcpDlcxRcvFailCnts=vismXgcpDlcxRcvFailCnts, vismXgcpPeerTable=vismXgcpPeerTable, vismXgcpMdcxCnts=vismXgcpMdcxCnts, vismXgcpRsipCnts=vismXgcpRsipCnts, vismXgcpPort=vismXgcpPort, vismXgcpPeerNumber=vismXgcpPeerNumber, vismXgcpRqntFailCnts=vismXgcpRqntFailCnts, vismXgcpEnhancementsObjects=vismXgcpEnhancementsObjects, vismXgcpNtfyCnts=vismXgcpNtfyCnts, vismXgcpRestartInProgressTdmax=vismXgcpRestartInProgressTdmax, vismXgcpAucxFailCnts=vismXgcpAucxFailCnts, vismXgcpCoreObjects=vismXgcpCoreObjects, vismXgcpMsgStatTable=vismXgcpMsgStatTable, vismXgcpMsgStatEntry=vismXgcpMsgStatEntry, vismXgcpAucxCnts=vismXgcpAucxCnts, vismXgcpDlcxSentFailCnts=vismXgcpDlcxSentFailCnts, vismXgcpRqntCnts=vismXgcpRqntCnts, vismXgcpDlcxRcvCnts=vismXgcpDlcxRcvCnts, vismXgcpIpAddress=vismXgcpIpAddress, vismXgcpDlcxSentCnts=vismXgcpDlcxSentCnts)