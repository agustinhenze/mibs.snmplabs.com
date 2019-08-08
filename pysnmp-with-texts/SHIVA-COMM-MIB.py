#
# PySNMP MIB module SHIVA-COMM-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/SHIVA-COMM-MIB
# Produced by pysmi-0.3.4 at Wed May  1 15:02:55 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ValueRangeConstraint, ValueSizeConstraint, SingleValueConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ValueRangeConstraint", "ValueSizeConstraint", "SingleValueConstraint", "ConstraintsUnion")
tCommunity, = mibBuilder.importSymbols("SHIVA-MIB", "tCommunity")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
Counter64, Gauge32, Integer32, Bits, MibIdentifier, ModuleIdentity, NotificationType, MibScalar, MibTable, MibTableRow, MibTableColumn, Unsigned32, TimeTicks, iso, ObjectIdentity, Counter32, IpAddress = mibBuilder.importSymbols("SNMPv2-SMI", "Counter64", "Gauge32", "Integer32", "Bits", "MibIdentifier", "ModuleIdentity", "NotificationType", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Unsigned32", "TimeTicks", "iso", "ObjectIdentity", "Counter32", "IpAddress")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
tCommunityTrapHostType = MibScalar((1, 3, 6, 1, 4, 1, 166, 4, 4, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("unconfigured", 1), ("ip", 2), ("ipx", 3)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: tCommunityTrapHostType.setStatus('mandatory')
if mibBuilder.loadTexts: tCommunityTrapHostType.setDescription('This is the address type of the trap host. The Trap Host is the host to which the device sends all traps.')
tCommunityTrapHostAddress = MibScalar((1, 3, 6, 1, 4, 1, 166, 4, 4, 2), OctetString()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: tCommunityTrapHostAddress.setStatus('mandatory')
if mibBuilder.loadTexts: tCommunityTrapHostAddress.setDescription('This is the Network Address of the host. It is interpreted according to the value of tCommunityTrapHostType.')
tCommunitySetHostType = MibScalar((1, 3, 6, 1, 4, 1, 166, 4, 4, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 6))).clone(namedValues=NamedValues(("unconfigured", 1), ("ip", 2), ("ipx", 3), ("netbios", 4), ("ddprange", 6)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: tCommunitySetHostType.setStatus('mandatory')
if mibBuilder.loadTexts: tCommunitySetHostType.setDescription('This is the address family of the set host. The Set Host is a host which is privileged to change any MIB variable.')
tCommunitySetHostAddress = MibScalar((1, 3, 6, 1, 4, 1, 166, 4, 4, 4), OctetString()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: tCommunitySetHostAddress.setStatus('mandatory')
if mibBuilder.loadTexts: tCommunitySetHostAddress.setDescription('This is the Network Address of the Set Host. It is interpreted according to the value of tCommunityTrapHostType.')
tCommunityTable = MibTable((1, 3, 6, 1, 4, 1, 166, 4, 4, 5), )
if mibBuilder.loadTexts: tCommunityTable.setStatus('mandatory')
if mibBuilder.loadTexts: tCommunityTable.setDescription('The Communities Table describes the various communities known to the the device.')
pysmiFakeCol1000 = MibTableColumn((1, 3, 6, 1, 4, 1, 166, 4, 4, 5, 1) + (1000, ), Integer32())
tCommunityEntry = MibTableRow((1, 3, 6, 1, 4, 1, 166, 4, 4, 5, 1), ).setIndexNames((0, "SHIVA-COMM-MIB", "pysmiFakeCol1000"))
if mibBuilder.loadTexts: tCommunityEntry.setStatus('mandatory')
if mibBuilder.loadTexts: tCommunityEntry.setDescription('The type of a row object in the community table. This represents a single SNMP Community. Community entries are indexed by counting integers starting with 1.')
tCommunityName = MibTableColumn((1, 3, 6, 1, 4, 1, 166, 4, 4, 5, 1, 1), DisplayString()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: tCommunityName.setStatus('mandatory')
if mibBuilder.loadTexts: tCommunityName.setDescription('The name of this community.')
tCommunityAccess = MibTableColumn((1, 3, 6, 1, 4, 1, 166, 4, 4, 5, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))).clone(namedValues=NamedValues(("no-access", 1), ("read-only-access", 2), ("clear-statistics", 3), ("configure", 4)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: tCommunityAccess.setStatus('mandatory')
if mibBuilder.loadTexts: tCommunityAccess.setDescription("This defines the privilege of the community. A 'read-only' community can examine any readable variable. A 'clear-statistics' community can reset non-critical counters. A 'configure' community has complete privileges. By setting the community access to 'no-access', a management station can deny all access by that community.")
tCommunityTrapTable = MibTable((1, 3, 6, 1, 4, 1, 166, 4, 4, 6), )
if mibBuilder.loadTexts: tCommunityTrapTable.setStatus('mandatory')
if mibBuilder.loadTexts: tCommunityTrapTable.setDescription('The Trap Table describes the list of hosts and the assosicated host type to be recepients of traps.')
pysmiFakeCol1001 = MibTableColumn((1, 3, 6, 1, 4, 1, 166, 4, 4, 6, 1) + (1001, ), Integer32())
tCommunityTrapEntry = MibTableRow((1, 3, 6, 1, 4, 1, 166, 4, 4, 6, 1), ).setIndexNames((0, "SHIVA-COMM-MIB", "pysmiFakeCol1001"))
if mibBuilder.loadTexts: tCommunityTrapEntry.setStatus('mandatory')
if mibBuilder.loadTexts: tCommunityTrapEntry.setDescription('The type of a row object in the community trap table. This represents a single trap host type and its address. Community trap entries are indexed by counting integers starting with 1.')
tCommunityTrapEntryHostAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 166, 4, 4, 6, 1, 1), OctetString()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: tCommunityTrapEntryHostAddress.setStatus('mandatory')
if mibBuilder.loadTexts: tCommunityTrapEntryHostAddress.setDescription('Address of the trap host. It is interpreted according to the value of tCommunityTrapEntryHostType')
tCommunityTrapEntryHostType = MibTableColumn((1, 3, 6, 1, 4, 1, 166, 4, 4, 6, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("unconfigured", 1), ("ip", 2), ("ipx", 3)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: tCommunityTrapEntryHostType.setStatus('mandatory')
if mibBuilder.loadTexts: tCommunityTrapEntryHostType.setDescription('Address type of the trap host')
mibBuilder.exportSymbols("SHIVA-COMM-MIB", tCommunitySetHostType=tCommunitySetHostType, tCommunityTrapTable=tCommunityTrapTable, tCommunityTrapEntryHostType=tCommunityTrapEntryHostType, tCommunityTrapHostAddress=tCommunityTrapHostAddress, pysmiFakeCol1000=pysmiFakeCol1000, tCommunityTrapHostType=tCommunityTrapHostType, tCommunityName=tCommunityName, tCommunityTrapEntryHostAddress=tCommunityTrapEntryHostAddress, tCommunityTrapEntry=tCommunityTrapEntry, tCommunityEntry=tCommunityEntry, tCommunitySetHostAddress=tCommunitySetHostAddress, tCommunityAccess=tCommunityAccess, tCommunityTable=tCommunityTable, pysmiFakeCol1001=pysmiFakeCol1001)