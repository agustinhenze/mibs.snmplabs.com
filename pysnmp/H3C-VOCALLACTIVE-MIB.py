#
# PySNMP MIB module H3C-VOCALLACTIVE-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/H3C-VOCALLACTIVE-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 19:11:12 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
SingleValueConstraint, ConstraintsUnion, ValueRangeConstraint, ConstraintsIntersection, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "SingleValueConstraint", "ConstraintsUnion", "ValueRangeConstraint", "ConstraintsIntersection", "ValueSizeConstraint")
CodecType, = mibBuilder.importSymbols("H3C-VO-TYPE-MIB", "CodecType")
h3cVoice, = mibBuilder.importSymbols("HUAWEI-3COM-OID-MIB", "h3cVoice")
InetAddressType, InetAddress = mibBuilder.importSymbols("INET-ADDRESS-MIB", "InetAddressType", "InetAddress")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
Unsigned32, MibIdentifier, ModuleIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, Gauge32, ObjectIdentity, NotificationType, IpAddress, Counter64, Integer32, TimeTicks, Counter32, iso, Bits = mibBuilder.importSymbols("SNMPv2-SMI", "Unsigned32", "MibIdentifier", "ModuleIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Gauge32", "ObjectIdentity", "NotificationType", "IpAddress", "Counter64", "Integer32", "TimeTicks", "Counter32", "iso", "Bits")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
h3cVoiceCallActive = ModuleIdentity((1, 3, 6, 1, 4, 1, 2011, 10, 2, 39, 6))
h3cVoiceCallActive.setRevisions(('2005-03-15 00:00',))
if mibBuilder.loadTexts: h3cVoiceCallActive.setLastUpdated('200503150000Z')
if mibBuilder.loadTexts: h3cVoiceCallActive.setOrganization('Huawei-3COM Technologies Co., Ltd.')
h3cVoCallActiveObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 10, 2, 39, 6, 1))
h3cVoCallActiveTable = MibTable((1, 3, 6, 1, 4, 1, 2011, 10, 2, 39, 6, 1, 1), )
if mibBuilder.loadTexts: h3cVoCallActiveTable.setStatus('current')
h3cVoCallActiveEntry = MibTableRow((1, 3, 6, 1, 4, 1, 2011, 10, 2, 39, 6, 1, 1, 1), ).setIndexNames((0, "H3C-VOCALLACTIVE-MIB", "h3cVoCallActiveChannel"))
if mibBuilder.loadTexts: h3cVoCallActiveEntry.setStatus('current')
h3cVoCallActiveChannel = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 10, 2, 39, 6, 1, 1, 1, 1), Integer32())
if mibBuilder.loadTexts: h3cVoCallActiveChannel.setStatus('current')
h3cVoCallActiveCallerNumber = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 10, 2, 39, 6, 1, 1, 1, 2), OctetString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: h3cVoCallActiveCallerNumber.setStatus('current')
h3cVoCallActiveCalledNumber = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 10, 2, 39, 6, 1, 1, 1, 3), OctetString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: h3cVoCallActiveCalledNumber.setStatus('current')
h3cVoCallActiveEncodeType = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 10, 2, 39, 6, 1, 1, 1, 4), CodecType()).setMaxAccess("readonly")
if mibBuilder.loadTexts: h3cVoCallActiveEncodeType.setStatus('current')
h3cVoCallActiveLocalAddressType = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 10, 2, 39, 6, 1, 1, 1, 5), InetAddressType()).setMaxAccess("readonly")
if mibBuilder.loadTexts: h3cVoCallActiveLocalAddressType.setStatus('current')
h3cVoCallActiveLocalAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 10, 2, 39, 6, 1, 1, 1, 6), InetAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: h3cVoCallActiveLocalAddress.setStatus('current')
h3cVoCallActivePeerAddressType = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 10, 2, 39, 6, 1, 1, 1, 7), InetAddressType()).setMaxAccess("readonly")
if mibBuilder.loadTexts: h3cVoCallActivePeerAddressType.setStatus('current')
h3cVoCallActivePeerAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 10, 2, 39, 6, 1, 1, 1, 8), InetAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: h3cVoCallActivePeerAddress.setStatus('current')
h3cVoCallActiveCallOrigin = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 10, 2, 39, 6, 1, 1, 1, 9), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("caller", 1), ("called", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: h3cVoCallActiveCallOrigin.setStatus('current')
h3cVoCallActiveIPSigType = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 10, 2, 39, 6, 1, 1, 1, 10), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("unknown", 1), ("h323", 2), ("sip", 3)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: h3cVoCallActiveIPSigType.setStatus('current')
h3cVoCallActivePSTNSigType = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 10, 2, 39, 6, 1, 1, 1, 11), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7))).clone(namedValues=NamedValues(("unknown", 1), ("fxs", 2), ("fxo", 3), ("em", 4), ("r2", 5), ("dss1", 6), ("dem", 7)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: h3cVoCallActivePSTNSigType.setStatus('current')
h3cVoCallActiveStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 10, 2, 39, 6, 1, 1, 1, 12), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5))).clone(namedValues=NamedValues(("idle", 1), ("calling", 2), ("alerting", 3), ("talking", 4), ("release", 5)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: h3cVoCallActiveStatus.setStatus('current')
mibBuilder.exportSymbols("H3C-VOCALLACTIVE-MIB", h3cVoCallActiveEncodeType=h3cVoCallActiveEncodeType, h3cVoCallActivePeerAddressType=h3cVoCallActivePeerAddressType, h3cVoCallActiveIPSigType=h3cVoCallActiveIPSigType, h3cVoCallActiveEntry=h3cVoCallActiveEntry, h3cVoCallActiveCallerNumber=h3cVoCallActiveCallerNumber, h3cVoCallActiveLocalAddress=h3cVoCallActiveLocalAddress, h3cVoCallActivePeerAddress=h3cVoCallActivePeerAddress, h3cVoCallActiveStatus=h3cVoCallActiveStatus, PYSNMP_MODULE_ID=h3cVoiceCallActive, h3cVoCallActiveTable=h3cVoCallActiveTable, h3cVoCallActiveCalledNumber=h3cVoCallActiveCalledNumber, h3cVoCallActiveCallOrigin=h3cVoCallActiveCallOrigin, h3cVoCallActivePSTNSigType=h3cVoCallActivePSTNSigType, h3cVoCallActiveLocalAddressType=h3cVoCallActiveLocalAddressType, h3cVoiceCallActive=h3cVoiceCallActive, h3cVoCallActiveObjects=h3cVoCallActiveObjects, h3cVoCallActiveChannel=h3cVoCallActiveChannel)
