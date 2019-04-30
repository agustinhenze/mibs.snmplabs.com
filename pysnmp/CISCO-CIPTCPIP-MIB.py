#
# PySNMP MIB module CISCO-CIPTCPIP-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/CISCO-CIPTCPIP-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 17:36:05 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
OctetString, Integer, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "OctetString", "Integer", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ValueRangeConstraint, ValueSizeConstraint, SingleValueConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ValueRangeConstraint", "ValueSizeConstraint", "SingleValueConstraint", "ConstraintsUnion")
ciscoMgmt, = mibBuilder.importSymbols("CISCO-SMI", "ciscoMgmt")
ifIndex, = mibBuilder.importSymbols("IF-MIB", "ifIndex")
ModuleCompliance, NotificationGroup, ObjectGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup", "ObjectGroup")
Integer32, IpAddress, Bits, MibIdentifier, NotificationType, Counter32, Gauge32, Unsigned32, MibScalar, MibTable, MibTableRow, MibTableColumn, ObjectIdentity, Counter64, TimeTicks, ModuleIdentity, iso = mibBuilder.importSymbols("SNMPv2-SMI", "Integer32", "IpAddress", "Bits", "MibIdentifier", "NotificationType", "Counter32", "Gauge32", "Unsigned32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "ObjectIdentity", "Counter64", "TimeTicks", "ModuleIdentity", "iso")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
ciscoCipTcpIpMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 9, 32))
ciscoCipTcpIpMIB.setRevisions(('1998-01-06 00:00', '1995-08-21 00:00', '1995-04-28 00:00',))
if mibBuilder.loadTexts: ciscoCipTcpIpMIB.setLastUpdated('9508210000Z')
if mibBuilder.loadTexts: ciscoCipTcpIpMIB.setOrganization('cisco IBM engineering Working Group')
cipTcpIpObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 32, 1))
cipIpObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 32, 1, 1))
cipTcpObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 32, 1, 2))
cipIcmpObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 32, 1, 3))
cipUdpObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 32, 1, 4))
cipIpTable = MibTable((1, 3, 6, 1, 4, 1, 9, 9, 32, 1, 1, 1), )
if mibBuilder.loadTexts: cipIpTable.setStatus('current')
cipIpEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9, 9, 32, 1, 1, 1, 1), ).setIndexNames((0, "IF-MIB", "ifIndex"), (0, "CISCO-CIPTCPIP-MIB", "cipIpAddress"))
if mibBuilder.loadTexts: cipIpEntry.setStatus('current')
cipIpAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 32, 1, 1, 1, 1, 1), IpAddress())
if mibBuilder.loadTexts: cipIpAddress.setStatus('current')
cipIpForwarding = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 32, 1, 1, 1, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("forwarding", 1), ("notForwarding", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cipIpForwarding.setStatus('current')
cipIpDefaultTTL = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 32, 1, 1, 1, 1, 3), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 255)).clone(64)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cipIpDefaultTTL.setStatus('current')
cipIpInReceives = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 32, 1, 1, 1, 1, 4), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cipIpInReceives.setStatus('current')
cipIpInHdrErrors = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 32, 1, 1, 1, 1, 5), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cipIpInHdrErrors.setStatus('current')
cipIpInAddrErrors = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 32, 1, 1, 1, 1, 6), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cipIpInAddrErrors.setStatus('current')
cipIpForwDatagrams = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 32, 1, 1, 1, 1, 7), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cipIpForwDatagrams.setStatus('current')
cipIpInUnknownProtos = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 32, 1, 1, 1, 1, 8), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cipIpInUnknownProtos.setStatus('current')
cipIpInDiscards = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 32, 1, 1, 1, 1, 9), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cipIpInDiscards.setStatus('current')
cipIpInDelivers = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 32, 1, 1, 1, 1, 10), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cipIpInDelivers.setStatus('current')
cipIpOutRequests = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 32, 1, 1, 1, 1, 11), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cipIpOutRequests.setStatus('current')
cipIpOutDiscards = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 32, 1, 1, 1, 1, 12), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cipIpOutDiscards.setStatus('current')
cipIpOutNoRoutes = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 32, 1, 1, 1, 1, 13), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cipIpOutNoRoutes.setStatus('current')
cipIpReasmTimeout = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 32, 1, 1, 1, 1, 14), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cipIpReasmTimeout.setStatus('current')
cipIpReasmReqds = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 32, 1, 1, 1, 1, 15), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cipIpReasmReqds.setStatus('current')
cipIpReasmOKs = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 32, 1, 1, 1, 1, 16), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cipIpReasmOKs.setStatus('current')
cipIpReasmFails = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 32, 1, 1, 1, 1, 17), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cipIpReasmFails.setStatus('current')
cipIpFragOKs = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 32, 1, 1, 1, 1, 18), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cipIpFragOKs.setStatus('current')
cipIpFragFails = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 32, 1, 1, 1, 1, 19), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cipIpFragFails.setStatus('current')
cipIpFragCreates = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 32, 1, 1, 1, 1, 20), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cipIpFragCreates.setStatus('current')
cipIpRoutingDiscards = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 32, 1, 1, 1, 1, 21), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cipIpRoutingDiscards.setStatus('current')
cipTcpStackTable = MibTable((1, 3, 6, 1, 4, 1, 9, 9, 32, 1, 2, 1), )
if mibBuilder.loadTexts: cipTcpStackTable.setStatus('current')
cipTcpStackEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9, 9, 32, 1, 2, 1, 1), ).setIndexNames((0, "IF-MIB", "ifIndex"), (0, "CISCO-CIPTCPIP-MIB", "cipIpAddress"))
if mibBuilder.loadTexts: cipTcpStackEntry.setStatus('current')
cipTcpRtoAlgorithm = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 32, 1, 2, 1, 1, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))).clone(namedValues=NamedValues(("other", 1), ("constant", 2), ("rsre", 3), ("vanj", 4)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: cipTcpRtoAlgorithm.setStatus('current')
cipTcpRtoMin = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 32, 1, 2, 1, 1, 2), Integer32()).setUnits('milliseconds').setMaxAccess("readonly")
if mibBuilder.loadTexts: cipTcpRtoMin.setStatus('current')
cipTcpRtoMax = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 32, 1, 2, 1, 1, 3), Integer32()).setUnits('milliseconds').setMaxAccess("readonly")
if mibBuilder.loadTexts: cipTcpRtoMax.setStatus('current')
cipTcpMaxConn = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 32, 1, 2, 1, 1, 4), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cipTcpMaxConn.setStatus('current')
cipTcpActiveOpens = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 32, 1, 2, 1, 1, 5), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cipTcpActiveOpens.setStatus('current')
cipTcpPassiveOpens = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 32, 1, 2, 1, 1, 6), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cipTcpPassiveOpens.setStatus('current')
cipTcpAttemptFails = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 32, 1, 2, 1, 1, 7), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cipTcpAttemptFails.setStatus('current')
cipTcpEstabResets = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 32, 1, 2, 1, 1, 8), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cipTcpEstabResets.setStatus('current')
cipTcpCurrEstab = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 32, 1, 2, 1, 1, 9), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cipTcpCurrEstab.setStatus('current')
cipTcpInSegs = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 32, 1, 2, 1, 1, 10), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cipTcpInSegs.setStatus('current')
cipTcpOutSegs = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 32, 1, 2, 1, 1, 11), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cipTcpOutSegs.setStatus('current')
cipTcpRetransSegs = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 32, 1, 2, 1, 1, 12), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cipTcpRetransSegs.setStatus('current')
cipTcpInErrs = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 32, 1, 2, 1, 1, 13), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cipTcpInErrs.setStatus('current')
cipTcpOutRsts = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 32, 1, 2, 1, 1, 14), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cipTcpOutRsts.setStatus('current')
cipTcpConnTable = MibTable((1, 3, 6, 1, 4, 1, 9, 9, 32, 1, 2, 2), )
if mibBuilder.loadTexts: cipTcpConnTable.setStatus('current')
cipTcpConnEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9, 9, 32, 1, 2, 2, 1), ).setIndexNames((0, "IF-MIB", "ifIndex"), (0, "CISCO-CIPTCPIP-MIB", "cipIpAddress"), (0, "CISCO-CIPTCPIP-MIB", "cipTcpConnLocalPort"), (0, "CISCO-CIPTCPIP-MIB", "cipTcpConnRemAddress"), (0, "CISCO-CIPTCPIP-MIB", "cipTcpConnRemPort"))
if mibBuilder.loadTexts: cipTcpConnEntry.setStatus('current')
cipTcpConnLocalPort = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 32, 1, 2, 2, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 65535)))
if mibBuilder.loadTexts: cipTcpConnLocalPort.setStatus('current')
cipTcpConnRemAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 32, 1, 2, 2, 1, 2), IpAddress())
if mibBuilder.loadTexts: cipTcpConnRemAddress.setStatus('current')
cipTcpConnRemPort = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 32, 1, 2, 2, 1, 3), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 65535)))
if mibBuilder.loadTexts: cipTcpConnRemPort.setStatus('current')
cipTcpConnState = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 32, 1, 2, 2, 1, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12))).clone(namedValues=NamedValues(("closed", 1), ("listen", 2), ("synSent", 3), ("synReceived", 4), ("established", 5), ("finWait1", 6), ("finWait2", 7), ("closeWait", 8), ("lastAck", 9), ("closing", 10), ("timeWait", 11), ("deleteTCB", 12)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cipTcpConnState.setStatus('current')
cipTcpConnInHCBytes = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 32, 1, 2, 2, 1, 5), Counter64()).setUnits('octets').setMaxAccess("readonly")
if mibBuilder.loadTexts: cipTcpConnInHCBytes.setStatus('current')
cipTcpConnInBytes = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 32, 1, 2, 2, 1, 6), Counter32()).setUnits('octets').setMaxAccess("readonly")
if mibBuilder.loadTexts: cipTcpConnInBytes.setStatus('current')
cipTcpConnOutHCBytes = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 32, 1, 2, 2, 1, 7), Counter64()).setUnits('octets').setMaxAccess("readonly")
if mibBuilder.loadTexts: cipTcpConnOutHCBytes.setStatus('current')
cipTcpConnOutBytes = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 32, 1, 2, 2, 1, 8), Counter32()).setUnits('octets').setMaxAccess("readonly")
if mibBuilder.loadTexts: cipTcpConnOutBytes.setStatus('current')
cipIcmpTable = MibTable((1, 3, 6, 1, 4, 1, 9, 9, 32, 1, 3, 1), )
if mibBuilder.loadTexts: cipIcmpTable.setStatus('current')
cipIcmpEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9, 9, 32, 1, 3, 1, 1), ).setIndexNames((0, "IF-MIB", "ifIndex"), (0, "CISCO-CIPTCPIP-MIB", "cipIpAddress"))
if mibBuilder.loadTexts: cipIcmpEntry.setStatus('current')
cipIcmpInMsgs = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 32, 1, 3, 1, 1, 1), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cipIcmpInMsgs.setStatus('current')
cipIcmpInErrors = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 32, 1, 3, 1, 1, 2), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cipIcmpInErrors.setStatus('current')
cipIcmpInDestUnreachs = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 32, 1, 3, 1, 1, 3), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cipIcmpInDestUnreachs.setStatus('current')
cipIcmpInTimeExcds = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 32, 1, 3, 1, 1, 4), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cipIcmpInTimeExcds.setStatus('current')
cipIcmpInParmProbs = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 32, 1, 3, 1, 1, 5), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cipIcmpInParmProbs.setStatus('current')
cipIcmpInSrcQuenchs = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 32, 1, 3, 1, 1, 6), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cipIcmpInSrcQuenchs.setStatus('current')
cipIcmpInRedirects = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 32, 1, 3, 1, 1, 7), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cipIcmpInRedirects.setStatus('current')
cipIcmpInEchos = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 32, 1, 3, 1, 1, 8), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cipIcmpInEchos.setStatus('current')
cipIcmpInAddrMaskReps = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 32, 1, 3, 1, 1, 9), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cipIcmpInAddrMaskReps.setStatus('current')
cipIcmpOutMsgs = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 32, 1, 3, 1, 1, 10), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cipIcmpOutMsgs.setStatus('current')
cipIcmpOutErrors = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 32, 1, 3, 1, 1, 11), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cipIcmpOutErrors.setStatus('current')
cipIcmpOutDestUnreachs = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 32, 1, 3, 1, 1, 12), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cipIcmpOutDestUnreachs.setStatus('current')
cipIcmpOutEchos = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 32, 1, 3, 1, 1, 13), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cipIcmpOutEchos.setStatus('current')
cipIcmpOutEchoReps = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 32, 1, 3, 1, 1, 14), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cipIcmpOutEchoReps.setStatus('current')
cipIcmpOutTimestamps = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 32, 1, 3, 1, 1, 15), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cipIcmpOutTimestamps.setStatus('current')
cipIcmpOutTimestampReps = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 32, 1, 3, 1, 1, 16), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cipIcmpOutTimestampReps.setStatus('current')
cipIcmpOutAddrMasks = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 32, 1, 3, 1, 1, 17), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cipIcmpOutAddrMasks.setStatus('current')
cipIcmpOutAddrMaskReps = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 32, 1, 3, 1, 1, 18), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cipIcmpOutAddrMaskReps.setStatus('current')
cipUdpTable = MibTable((1, 3, 6, 1, 4, 1, 9, 9, 32, 1, 4, 1), )
if mibBuilder.loadTexts: cipUdpTable.setStatus('current')
cipUdpEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9, 9, 32, 1, 4, 1, 1), ).setIndexNames((0, "IF-MIB", "ifIndex"), (0, "CISCO-CIPTCPIP-MIB", "cipIpAddress"))
if mibBuilder.loadTexts: cipUdpEntry.setStatus('current')
cipUdpInDatagrams = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 32, 1, 4, 1, 1, 1), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cipUdpInDatagrams.setStatus('current')
cipUdpNoPorts = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 32, 1, 4, 1, 1, 2), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cipUdpNoPorts.setStatus('current')
cipUdpInErrors = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 32, 1, 4, 1, 1, 3), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cipUdpInErrors.setStatus('current')
cipUdpOutDatagrams = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 32, 1, 4, 1, 1, 4), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cipUdpOutDatagrams.setStatus('current')
cipUdpListenersTable = MibTable((1, 3, 6, 1, 4, 1, 9, 9, 32, 1, 4, 2), )
if mibBuilder.loadTexts: cipUdpListenersTable.setStatus('current')
cipUdpListenersEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9, 9, 32, 1, 4, 2, 1), ).setIndexNames((0, "IF-MIB", "ifIndex"), (0, "CISCO-CIPTCPIP-MIB", "cipIpAddress"), (0, "CISCO-CIPTCPIP-MIB", "cipUdpLocalPort"))
if mibBuilder.loadTexts: cipUdpListenersEntry.setStatus('current')
cipUdpLocalPort = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 32, 1, 4, 2, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 65535))).setMaxAccess("readonly")
if mibBuilder.loadTexts: cipUdpLocalPort.setStatus('current')
ciscoCipTcpIpMibConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 32, 2))
ciscoCipTcpIpMibCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 32, 2, 1))
ciscoCipTcpIpMibGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 32, 2, 2))
ciscoCipTcpIpMibCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 9, 9, 32, 2, 1, 1)).setObjects(("CISCO-CIPTCPIP-MIB", "ciscoCipTcpIpGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoCipTcpIpMibCompliance = ciscoCipTcpIpMibCompliance.setStatus('current')
ciscoCipTcpIpGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 32, 2, 2, 1)).setObjects(("CISCO-CIPTCPIP-MIB", "cipIpForwarding"), ("CISCO-CIPTCPIP-MIB", "cipIpDefaultTTL"), ("CISCO-CIPTCPIP-MIB", "cipIpInReceives"), ("CISCO-CIPTCPIP-MIB", "cipIpInHdrErrors"), ("CISCO-CIPTCPIP-MIB", "cipIpInAddrErrors"), ("CISCO-CIPTCPIP-MIB", "cipIpForwDatagrams"), ("CISCO-CIPTCPIP-MIB", "cipIpInUnknownProtos"), ("CISCO-CIPTCPIP-MIB", "cipIpInDiscards"), ("CISCO-CIPTCPIP-MIB", "cipIpInDelivers"), ("CISCO-CIPTCPIP-MIB", "cipIpOutRequests"), ("CISCO-CIPTCPIP-MIB", "cipIpOutDiscards"), ("CISCO-CIPTCPIP-MIB", "cipIpOutNoRoutes"), ("CISCO-CIPTCPIP-MIB", "cipIpReasmTimeout"), ("CISCO-CIPTCPIP-MIB", "cipIpReasmReqds"), ("CISCO-CIPTCPIP-MIB", "cipIpReasmOKs"), ("CISCO-CIPTCPIP-MIB", "cipIpReasmFails"), ("CISCO-CIPTCPIP-MIB", "cipIpFragOKs"), ("CISCO-CIPTCPIP-MIB", "cipIpFragFails"), ("CISCO-CIPTCPIP-MIB", "cipIpFragCreates"), ("CISCO-CIPTCPIP-MIB", "cipIpRoutingDiscards"), ("CISCO-CIPTCPIP-MIB", "cipTcpRtoAlgorithm"), ("CISCO-CIPTCPIP-MIB", "cipTcpRtoMin"), ("CISCO-CIPTCPIP-MIB", "cipTcpRtoMax"), ("CISCO-CIPTCPIP-MIB", "cipTcpMaxConn"), ("CISCO-CIPTCPIP-MIB", "cipTcpActiveOpens"), ("CISCO-CIPTCPIP-MIB", "cipTcpPassiveOpens"), ("CISCO-CIPTCPIP-MIB", "cipTcpAttemptFails"), ("CISCO-CIPTCPIP-MIB", "cipTcpEstabResets"), ("CISCO-CIPTCPIP-MIB", "cipTcpCurrEstab"), ("CISCO-CIPTCPIP-MIB", "cipTcpInSegs"), ("CISCO-CIPTCPIP-MIB", "cipTcpOutSegs"), ("CISCO-CIPTCPIP-MIB", "cipTcpRetransSegs"), ("CISCO-CIPTCPIP-MIB", "cipTcpInErrs"), ("CISCO-CIPTCPIP-MIB", "cipTcpOutRsts"), ("CISCO-CIPTCPIP-MIB", "cipTcpConnState"), ("CISCO-CIPTCPIP-MIB", "cipTcpConnInBytes"), ("CISCO-CIPTCPIP-MIB", "cipTcpConnInHCBytes"), ("CISCO-CIPTCPIP-MIB", "cipTcpConnOutBytes"), ("CISCO-CIPTCPIP-MIB", "cipTcpConnOutHCBytes"), ("CISCO-CIPTCPIP-MIB", "cipIcmpInMsgs"), ("CISCO-CIPTCPIP-MIB", "cipIcmpInErrors"), ("CISCO-CIPTCPIP-MIB", "cipIcmpInDestUnreachs"), ("CISCO-CIPTCPIP-MIB", "cipIcmpInTimeExcds"), ("CISCO-CIPTCPIP-MIB", "cipIcmpInParmProbs"), ("CISCO-CIPTCPIP-MIB", "cipIcmpInSrcQuenchs"), ("CISCO-CIPTCPIP-MIB", "cipIcmpInRedirects"), ("CISCO-CIPTCPIP-MIB", "cipIcmpInEchos"), ("CISCO-CIPTCPIP-MIB", "cipIcmpInAddrMaskReps"), ("CISCO-CIPTCPIP-MIB", "cipIcmpOutMsgs"), ("CISCO-CIPTCPIP-MIB", "cipIcmpOutErrors"), ("CISCO-CIPTCPIP-MIB", "cipIcmpOutDestUnreachs"), ("CISCO-CIPTCPIP-MIB", "cipIcmpOutEchos"), ("CISCO-CIPTCPIP-MIB", "cipIcmpOutEchoReps"), ("CISCO-CIPTCPIP-MIB", "cipIcmpOutTimestamps"), ("CISCO-CIPTCPIP-MIB", "cipIcmpOutTimestampReps"), ("CISCO-CIPTCPIP-MIB", "cipIcmpOutAddrMasks"), ("CISCO-CIPTCPIP-MIB", "cipIcmpOutAddrMaskReps"), ("CISCO-CIPTCPIP-MIB", "cipUdpInDatagrams"), ("CISCO-CIPTCPIP-MIB", "cipUdpNoPorts"), ("CISCO-CIPTCPIP-MIB", "cipUdpInErrors"), ("CISCO-CIPTCPIP-MIB", "cipUdpOutDatagrams"), ("CISCO-CIPTCPIP-MIB", "cipUdpLocalPort"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoCipTcpIpGroup = ciscoCipTcpIpGroup.setStatus('current')
mibBuilder.exportSymbols("CISCO-CIPTCPIP-MIB", cipTcpActiveOpens=cipTcpActiveOpens, cipIpDefaultTTL=cipIpDefaultTTL, cipIcmpOutMsgs=cipIcmpOutMsgs, cipIcmpEntry=cipIcmpEntry, cipIpReasmReqds=cipIpReasmReqds, cipIcmpOutAddrMasks=cipIcmpOutAddrMasks, cipUdpInDatagrams=cipUdpInDatagrams, cipTcpEstabResets=cipTcpEstabResets, cipIcmpInEchos=cipIcmpInEchos, cipTcpAttemptFails=cipTcpAttemptFails, cipIpForwDatagrams=cipIpForwDatagrams, cipUdpListenersEntry=cipUdpListenersEntry, cipIcmpInSrcQuenchs=cipIcmpInSrcQuenchs, cipIcmpOutTimestampReps=cipIcmpOutTimestampReps, cipTcpRtoAlgorithm=cipTcpRtoAlgorithm, cipTcpRetransSegs=cipTcpRetransSegs, cipIpInReceives=cipIpInReceives, cipTcpConnInHCBytes=cipTcpConnInHCBytes, cipIpOutRequests=cipIpOutRequests, cipUdpListenersTable=cipUdpListenersTable, cipTcpConnRemAddress=cipTcpConnRemAddress, cipIcmpInAddrMaskReps=cipIcmpInAddrMaskReps, cipIpFragFails=cipIpFragFails, cipTcpConnState=cipTcpConnState, cipTcpConnLocalPort=cipTcpConnLocalPort, cipTcpConnRemPort=cipTcpConnRemPort, cipUdpObjects=cipUdpObjects, cipIcmpOutTimestamps=cipIcmpOutTimestamps, cipIcmpObjects=cipIcmpObjects, ciscoCipTcpIpMIB=ciscoCipTcpIpMIB, PYSNMP_MODULE_ID=ciscoCipTcpIpMIB, cipTcpInSegs=cipTcpInSegs, cipIpAddress=cipIpAddress, cipTcpOutRsts=cipTcpOutRsts, cipIpInDiscards=cipIpInDiscards, cipTcpInErrs=cipTcpInErrs, cipIpInDelivers=cipIpInDelivers, cipIpForwarding=cipIpForwarding, cipTcpStackTable=cipTcpStackTable, cipIpEntry=cipIpEntry, cipIpRoutingDiscards=cipIpRoutingDiscards, cipTcpStackEntry=cipTcpStackEntry, cipIpTable=cipIpTable, cipTcpIpObjects=cipTcpIpObjects, cipIcmpInTimeExcds=cipIcmpInTimeExcds, cipTcpOutSegs=cipTcpOutSegs, cipIpReasmOKs=cipIpReasmOKs, cipIcmpOutDestUnreachs=cipIcmpOutDestUnreachs, cipIpFragOKs=cipIpFragOKs, cipTcpCurrEstab=cipTcpCurrEstab, cipIpOutDiscards=cipIpOutDiscards, cipIcmpTable=cipIcmpTable, cipUdpEntry=cipUdpEntry, cipTcpMaxConn=cipTcpMaxConn, cipTcpPassiveOpens=cipTcpPassiveOpens, cipTcpConnEntry=cipTcpConnEntry, cipIcmpOutEchoReps=cipIcmpOutEchoReps, cipUdpInErrors=cipUdpInErrors, cipUdpOutDatagrams=cipUdpOutDatagrams, cipUdpNoPorts=cipUdpNoPorts, cipIpInHdrErrors=cipIpInHdrErrors, ciscoCipTcpIpMibGroups=ciscoCipTcpIpMibGroups, cipTcpConnTable=cipTcpConnTable, cipIcmpInRedirects=cipIcmpInRedirects, cipIpInUnknownProtos=cipIpInUnknownProtos, cipIcmpOutEchos=cipIcmpOutEchos, cipTcpConnInBytes=cipTcpConnInBytes, ciscoCipTcpIpGroup=ciscoCipTcpIpGroup, cipIcmpInDestUnreachs=cipIcmpInDestUnreachs, cipIcmpOutErrors=cipIcmpOutErrors, cipIpReasmTimeout=cipIpReasmTimeout, cipIcmpOutAddrMaskReps=cipIcmpOutAddrMaskReps, cipTcpRtoMin=cipTcpRtoMin, ciscoCipTcpIpMibCompliance=ciscoCipTcpIpMibCompliance, cipIcmpInMsgs=cipIcmpInMsgs, cipIpInAddrErrors=cipIpInAddrErrors, cipIcmpInParmProbs=cipIcmpInParmProbs, cipTcpRtoMax=cipTcpRtoMax, cipIcmpInErrors=cipIcmpInErrors, cipIpFragCreates=cipIpFragCreates, cipIpObjects=cipIpObjects, ciscoCipTcpIpMibConformance=ciscoCipTcpIpMibConformance, cipTcpObjects=cipTcpObjects, cipTcpConnOutHCBytes=cipTcpConnOutHCBytes, cipIpOutNoRoutes=cipIpOutNoRoutes, ciscoCipTcpIpMibCompliances=ciscoCipTcpIpMibCompliances, cipIpReasmFails=cipIpReasmFails, cipTcpConnOutBytes=cipTcpConnOutBytes, cipUdpLocalPort=cipUdpLocalPort, cipUdpTable=cipUdpTable)