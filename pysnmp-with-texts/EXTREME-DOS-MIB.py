#
# PySNMP MIB module EXTREME-DOS-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/EXTREME-BASE-MIB
# Produced by pysmi-0.3.4 at Wed May  1 13:07:14 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
ObjectIdentifier, Integer, OctetString = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "Integer", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, ValueSizeConstraint, ConstraintsUnion, SingleValueConstraint, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "ValueSizeConstraint", "ConstraintsUnion", "SingleValueConstraint", "ConstraintsIntersection")
extremeAgent, extremeV2Traps, extremenetworks = mibBuilder.importSymbols("EXTREME-BASE-MIB", "extremeAgent", "extremeV2Traps", "extremenetworks")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
Counter64, IpAddress, Integer32, Gauge32, Counter32, MibIdentifier, MibScalar, MibTable, MibTableRow, MibTableColumn, iso, NotificationType, ModuleIdentity, ObjectIdentity, TimeTicks, Bits, Unsigned32 = mibBuilder.importSymbols("SNMPv2-SMI", "Counter64", "IpAddress", "Integer32", "Gauge32", "Counter32", "MibIdentifier", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "iso", "NotificationType", "ModuleIdentity", "ObjectIdentity", "TimeTicks", "Bits", "Unsigned32")
TruthValue, DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "TruthValue", "DisplayString", "TextualConvention")
extremeDosMib = ModuleIdentity((1, 3, 6, 1, 4, 1, 1916, 1, 28))
if mibBuilder.loadTexts: extremeDosMib.setLastUpdated('0401020000Z')
if mibBuilder.loadTexts: extremeDosMib.setOrganization('Extreme Networks, Inc.')
if mibBuilder.loadTexts: extremeDosMib.setContactInfo('www.extremenetworks.com')
if mibBuilder.loadTexts: extremeDosMib.setDescription('Extreme Dos protect objects information')
extremeDosProtect = MibIdentifier((1, 3, 6, 1, 4, 1, 1916, 1, 28, 1))
extremeDosEnable = MibScalar((1, 3, 6, 1, 4, 1, 1916, 1, 28, 1, 1), TruthValue().clone('false')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: extremeDosEnable.setStatus('current')
if mibBuilder.loadTexts: extremeDosEnable.setDescription('The Flag indicates whether DOS protection is enabled or disabled.')
extremeDosNoticeLevel = MibScalar((1, 3, 6, 1, 4, 1, 1916, 1, 28, 1, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(150, 100000)).clone(4000)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: extremeDosNoticeLevel.setStatus('current')
if mibBuilder.loadTexts: extremeDosNoticeLevel.setDescription('The number of packets per second to be received for logging.')
extremeDosAlertLevel = MibScalar((1, 3, 6, 1, 4, 1, 1916, 1, 28, 1, 3), Integer32().subtype(subtypeSpec=ValueRangeConstraint(150, 100000)).clone(4000)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: extremeDosAlertLevel.setStatus('current')
if mibBuilder.loadTexts: extremeDosAlertLevel.setDescription('The number of packets per second to be received for ACL creation.')
extremeDosFilterType = MibScalar((1, 3, 6, 1, 4, 1, 1916, 1, 28, 1, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("destination", 1), ("source", 2), ("destinationAndSource", 3))).clone('destination')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: extremeDosFilterType.setStatus('current')
if mibBuilder.loadTexts: extremeDosFilterType.setDescription('The type of access list filter to be set when threshold pakets are received')
extremeDosAclTimeout = MibScalar((1, 3, 6, 1, 4, 1, 1916, 1, 28, 1, 5), Integer32().subtype(subtypeSpec=ValueRangeConstraint(2, 300)).clone(15)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: extremeDosAclTimeout.setStatus('current')
if mibBuilder.loadTexts: extremeDosAclTimeout.setDescription('The timeout interval period over which DOS protect is exercised.')
extremeDosAclRulePrecedence = MibScalar((1, 3, 6, 1, 4, 1, 1916, 1, 28, 1, 6), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 25588)).clone(10)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: extremeDosAclRulePrecedence.setStatus('current')
if mibBuilder.loadTexts: extremeDosAclRulePrecedence.setDescription('The DOS filter Rule Precedence.')
extremeDosMessagesEnable = MibScalar((1, 3, 6, 1, 4, 1, 1916, 1, 28, 1, 7), TruthValue().clone('true')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: extremeDosMessagesEnable.setStatus('current')
if mibBuilder.loadTexts: extremeDosMessagesEnable.setDescription('The Flag indicates whether DOS messages are enabled or disabled.')
extremeDosPortTable = MibTable((1, 3, 6, 1, 4, 1, 1916, 1, 28, 1, 8), )
if mibBuilder.loadTexts: extremeDosPortTable.setStatus('current')
if mibBuilder.loadTexts: extremeDosPortTable.setDescription('This table contains the port wise listing of DOS attributes.')
extremeDosPortEntry = MibTableRow((1, 3, 6, 1, 4, 1, 1916, 1, 28, 1, 8, 1), ).setIndexNames((0, "EXTREME-DOS-MIB", "extremeDosIfIndex"))
if mibBuilder.loadTexts: extremeDosPortEntry.setStatus('current')
if mibBuilder.loadTexts: extremeDosPortEntry.setDescription('Information about the Dos attributes of a particular port.')
extremeDosIfIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 1916, 1, 28, 1, 8, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: extremeDosIfIndex.setStatus('current')
if mibBuilder.loadTexts: extremeDosIfIndex.setDescription('The index for this entry.')
extremeDosPortTrusted = MibTableColumn((1, 3, 6, 1, 4, 1, 1916, 1, 28, 1, 8, 1, 2), TruthValue().clone('false')).setMaxAccess("readcreate")
if mibBuilder.loadTexts: extremeDosPortTrusted.setStatus('current')
if mibBuilder.loadTexts: extremeDosPortTrusted.setDescription('Indicates whether the port is trusted or untrusted.')
extremeDosIsDosActive = MibTableColumn((1, 3, 6, 1, 4, 1, 1916, 1, 28, 1, 8, 1, 3), TruthValue()).setMaxAccess("readonly")
if mibBuilder.loadTexts: extremeDosIsDosActive.setStatus('current')
if mibBuilder.loadTexts: extremeDosIsDosActive.setDescription('Indicates whether DOS is active on this port.')
extremeDosTraps = MibIdentifier((1, 3, 6, 1, 4, 1, 1916, 4, 14))
extremeDosTrapsPrefix = MibIdentifier((1, 3, 6, 1, 4, 1, 1916, 4, 14, 0))
extremeDosThresholdCleared = NotificationType((1, 3, 6, 1, 4, 1, 1916, 4, 14, 0, 1)).setObjects(("EXTREME-DOS-MIB", "extremeDosAlertLevel"))
if mibBuilder.loadTexts: extremeDosThresholdCleared.setStatus('current')
if mibBuilder.loadTexts: extremeDosThresholdCleared.setDescription('The extremeDosThresholdCleared notification is generated when the DOS threshold is cleared .')
extremeDosThresholdReached = NotificationType((1, 3, 6, 1, 4, 1, 1916, 4, 14, 0, 2)).setObjects(("EXTREME-DOS-MIB", "extremeDosAlertLevel"))
if mibBuilder.loadTexts: extremeDosThresholdReached.setStatus('current')
if mibBuilder.loadTexts: extremeDosThresholdReached.setDescription('The extremeDosThresholdReached notification is generated when the DOS threshold is crossed for any of the ports.')
mibBuilder.exportSymbols("EXTREME-DOS-MIB", extremeDosNoticeLevel=extremeDosNoticeLevel, extremeDosPortTrusted=extremeDosPortTrusted, extremeDosEnable=extremeDosEnable, extremeDosAclRulePrecedence=extremeDosAclRulePrecedence, extremeDosProtect=extremeDosProtect, extremeDosFilterType=extremeDosFilterType, extremeDosMessagesEnable=extremeDosMessagesEnable, extremeDosAclTimeout=extremeDosAclTimeout, extremeDosThresholdCleared=extremeDosThresholdCleared, PYSNMP_MODULE_ID=extremeDosMib, extremeDosIsDosActive=extremeDosIsDosActive, extremeDosPortTable=extremeDosPortTable, extremeDosPortEntry=extremeDosPortEntry, extremeDosMib=extremeDosMib, extremeDosAlertLevel=extremeDosAlertLevel, extremeDosThresholdReached=extremeDosThresholdReached, extremeDosIfIndex=extremeDosIfIndex, extremeDosTrapsPrefix=extremeDosTrapsPrefix, extremeDosTraps=extremeDosTraps)
