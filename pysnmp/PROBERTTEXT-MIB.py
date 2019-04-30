#
# PySNMP MIB module PROBERTTEXT-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/PROBERTTEXT-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 20:33:24 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
probeRttExt, = mibBuilder.importSymbols("APENT-MIB", "probeRttExt")
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
SingleValueConstraint, ValueRangeConstraint, ConstraintsUnion, ConstraintsIntersection, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "SingleValueConstraint", "ValueRangeConstraint", "ConstraintsUnion", "ConstraintsIntersection", "ValueSizeConstraint")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
MibScalar, MibTable, MibTableRow, MibTableColumn, Counter64, Bits, ObjectIdentity, Counter32, NotificationType, ModuleIdentity, MibIdentifier, Integer32, Gauge32, iso, Unsigned32, IpAddress, TimeTicks = mibBuilder.importSymbols("SNMPv2-SMI", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter64", "Bits", "ObjectIdentity", "Counter32", "NotificationType", "ModuleIdentity", "MibIdentifier", "Integer32", "Gauge32", "iso", "Unsigned32", "IpAddress", "TimeTicks")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
apProbeRttExtMib = ModuleIdentity((1, 3, 6, 1, 4, 1, 2467, 1, 55, 1))
if mibBuilder.loadTexts: apProbeRttExtMib.setLastUpdated('9707202000Z')
if mibBuilder.loadTexts: apProbeRttExtMib.setOrganization('ArrowPoint Communications Inc.')
apProbeRttEnable = MibScalar((1, 3, 6, 1, 4, 1, 2467, 1, 55, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1))).clone(namedValues=NamedValues(("disable", 0), ("enable", 1)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: apProbeRttEnable.setStatus('current')
apProbeRttMethod0 = MibScalar((1, 3, 6, 1, 4, 1, 2467, 1, 55, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1))).clone(namedValues=NamedValues(("icmp", 0), ("tcp", 1)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: apProbeRttMethod0.setStatus('current')
apProbeRttMethod1 = MibScalar((1, 3, 6, 1, 4, 1, 2467, 1, 55, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1, 2))).clone(namedValues=NamedValues(("icmp", 0), ("tcp", 1), ("none", 2))).clone(1)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: apProbeRttMethod1.setStatus('current')
apProbeRttIcmpSamples = MibScalar((1, 3, 6, 1, 4, 1, 2467, 1, 55, 5), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 30)).clone(2)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: apProbeRttIcmpSamples.setStatus('current')
apProbeRttIcmpInterval = MibScalar((1, 3, 6, 1, 4, 1, 2467, 1, 55, 6), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 10)).clone(1)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: apProbeRttIcmpInterval.setStatus('current')
apProbeRttTcpPort0 = MibScalar((1, 3, 6, 1, 4, 1, 2467, 1, 55, 7), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 65535)).clone(23)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: apProbeRttTcpPort0.setStatus('current')
apProbeRttTcpPort1 = MibScalar((1, 3, 6, 1, 4, 1, 2467, 1, 55, 8), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 65535)).clone(21)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: apProbeRttTcpPort1.setStatus('current')
apProbeRttTcpPort2 = MibScalar((1, 3, 6, 1, 4, 1, 2467, 1, 55, 9), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 65535)).clone(80)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: apProbeRttTcpPort2.setStatus('current')
apProbeRttTcpPort3 = MibScalar((1, 3, 6, 1, 4, 1, 2467, 1, 55, 10), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 65535))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: apProbeRttTcpPort3.setStatus('current')
apProbeRttLastReset = MibScalar((1, 3, 6, 1, 4, 1, 2467, 1, 55, 11), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 19))).setMaxAccess("readonly")
if mibBuilder.loadTexts: apProbeRttLastReset.setStatus('current')
apProbeRttTtlProbes = MibScalar((1, 3, 6, 1, 4, 1, 2467, 1, 55, 12), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: apProbeRttTtlProbes.setStatus('current')
apProbeRttAvgProbes = MibScalar((1, 3, 6, 1, 4, 1, 2467, 1, 55, 13), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: apProbeRttAvgProbes.setStatus('current')
apProbeRttICMPReqSent = MibScalar((1, 3, 6, 1, 4, 1, 2467, 1, 55, 14), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: apProbeRttICMPReqSent.setStatus('current')
apProbeRttICMPResp = MibScalar((1, 3, 6, 1, 4, 1, 2467, 1, 55, 15), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: apProbeRttICMPResp.setStatus('current')
apProbeRttICMPNoResp = MibScalar((1, 3, 6, 1, 4, 1, 2467, 1, 55, 16), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: apProbeRttICMPNoResp.setStatus('current')
apProbeRttICMPAvgReq = MibScalar((1, 3, 6, 1, 4, 1, 2467, 1, 55, 17), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: apProbeRttICMPAvgReq.setStatus('current')
apProbeRttICMPSendFail = MibScalar((1, 3, 6, 1, 4, 1, 2467, 1, 55, 18), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: apProbeRttICMPSendFail.setStatus('current')
apProbeRttTCPReqSent = MibScalar((1, 3, 6, 1, 4, 1, 2467, 1, 55, 19), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: apProbeRttTCPReqSent.setStatus('current')
apProbeRttTCPResp = MibScalar((1, 3, 6, 1, 4, 1, 2467, 1, 55, 20), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: apProbeRttTCPResp.setStatus('current')
apProbeRttTCPNoResp = MibScalar((1, 3, 6, 1, 4, 1, 2467, 1, 55, 21), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: apProbeRttTCPNoResp.setStatus('current')
apProbeRttTCPAvgReq = MibScalar((1, 3, 6, 1, 4, 1, 2467, 1, 55, 22), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: apProbeRttTCPAvgReq.setStatus('current')
apProbeRttTCPSendFail = MibScalar((1, 3, 6, 1, 4, 1, 2467, 1, 55, 23), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: apProbeRttTCPSendFail.setStatus('current')
apProbeRttPortTable = MibTable((1, 3, 6, 1, 4, 1, 2467, 1, 55, 24), )
if mibBuilder.loadTexts: apProbeRttPortTable.setStatus('current')
apProbeRttPortEntry = MibTableRow((1, 3, 6, 1, 4, 1, 2467, 1, 55, 24, 1), ).setIndexNames((0, "PROBERTTEXT-MIB", "apProbeRttPortIndex"))
if mibBuilder.loadTexts: apProbeRttPortEntry.setStatus('current')
apProbeRttPortIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 2467, 1, 55, 24, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 3))).setMaxAccess("readonly")
if mibBuilder.loadTexts: apProbeRttPortIndex.setStatus('current')
apProbeRttPortNumber = MibTableColumn((1, 3, 6, 1, 4, 1, 2467, 1, 55, 24, 1, 2), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: apProbeRttPortNumber.setStatus('current')
apProbeRttPortRequests = MibTableColumn((1, 3, 6, 1, 4, 1, 2467, 1, 55, 24, 1, 3), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: apProbeRttPortRequests.setStatus('current')
apProbeRttPortResponses = MibTableColumn((1, 3, 6, 1, 4, 1, 2467, 1, 55, 24, 1, 4), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: apProbeRttPortResponses.setStatus('current')
apProbeRttPortFailures = MibTableColumn((1, 3, 6, 1, 4, 1, 2467, 1, 55, 24, 1, 5), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: apProbeRttPortFailures.setStatus('current')
mibBuilder.exportSymbols("PROBERTTEXT-MIB", apProbeRttICMPReqSent=apProbeRttICMPReqSent, apProbeRttTCPAvgReq=apProbeRttTCPAvgReq, apProbeRttPortNumber=apProbeRttPortNumber, apProbeRttPortIndex=apProbeRttPortIndex, apProbeRttTCPNoResp=apProbeRttTCPNoResp, apProbeRttPortTable=apProbeRttPortTable, PYSNMP_MODULE_ID=apProbeRttExtMib, apProbeRttTcpPort1=apProbeRttTcpPort1, apProbeRttTCPResp=apProbeRttTCPResp, apProbeRttTcpPort3=apProbeRttTcpPort3, apProbeRttExtMib=apProbeRttExtMib, apProbeRttPortResponses=apProbeRttPortResponses, apProbeRttMethod0=apProbeRttMethod0, apProbeRttIcmpSamples=apProbeRttIcmpSamples, apProbeRttICMPNoResp=apProbeRttICMPNoResp, apProbeRttAvgProbes=apProbeRttAvgProbes, apProbeRttPortEntry=apProbeRttPortEntry, apProbeRttTCPSendFail=apProbeRttTCPSendFail, apProbeRttTcpPort0=apProbeRttTcpPort0, apProbeRttTcpPort2=apProbeRttTcpPort2, apProbeRttICMPAvgReq=apProbeRttICMPAvgReq, apProbeRttEnable=apProbeRttEnable, apProbeRttTtlProbes=apProbeRttTtlProbes, apProbeRttPortFailures=apProbeRttPortFailures, apProbeRttPortRequests=apProbeRttPortRequests, apProbeRttLastReset=apProbeRttLastReset, apProbeRttIcmpInterval=apProbeRttIcmpInterval, apProbeRttICMPSendFail=apProbeRttICMPSendFail, apProbeRttMethod1=apProbeRttMethod1, apProbeRttTCPReqSent=apProbeRttTCPReqSent, apProbeRttICMPResp=apProbeRttICMPResp)