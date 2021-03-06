#
# PySNMP MIB module Fore-FAST-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/Fore-FAST-MIB
# Produced by pysmi-0.3.4 at Wed May  1 13:17:02 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
OctetString, ObjectIdentifier, Integer = mibBuilder.importSymbols("ASN1", "OctetString", "ObjectIdentifier", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, ConstraintsUnion, SingleValueConstraint, ValueSizeConstraint, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "ConstraintsUnion", "SingleValueConstraint", "ValueSizeConstraint", "ConstraintsIntersection")
asx, = mibBuilder.importSymbols("Fore-Common-MIB", "asx")
ifIndex, = mibBuilder.importSymbols("IF-MIB", "ifIndex")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
ObjectIdentity, IpAddress, NotificationType, MibScalar, MibTable, MibTableRow, MibTableColumn, TimeTicks, Unsigned32, Integer32, MibIdentifier, Counter64, Counter32, Gauge32, ModuleIdentity, iso, Bits = mibBuilder.importSymbols("SNMPv2-SMI", "ObjectIdentity", "IpAddress", "NotificationType", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "TimeTicks", "Unsigned32", "Integer32", "MibIdentifier", "Counter64", "Counter32", "Gauge32", "ModuleIdentity", "iso", "Bits")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
foreFastGroup = MibIdentifier((1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 1, 21))
foreFastIfTable = MibTable((1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 1, 21, 1), )
if mibBuilder.loadTexts: foreFastIfTable.setStatus('current')
if mibBuilder.loadTexts: foreFastIfTable.setDescription('A table containing FAST interface configuration and status.')
foreFastIfEntry = MibTableRow((1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 1, 21, 1, 1), ).setIndexNames((0, "IF-MIB", "ifIndex"))
if mibBuilder.loadTexts: foreFastIfEntry.setStatus('current')
if mibBuilder.loadTexts: foreFastIfEntry.setDescription('A table entry containing the FAST interface information.')
foreFastIfFramingMode = MibTableColumn((1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 1, 21, 1, 1, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1))).clone(namedValues=NamedValues(("mode0", 1)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: foreFastIfFramingMode.setStatus('current')
if mibBuilder.loadTexts: foreFastIfFramingMode.setDescription('Indicates the operational Framing mode on this interface.')
foreFastIfAdminStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 1, 21, 1, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("up", 1), ("down", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: foreFastIfAdminStatus.setStatus('current')
if mibBuilder.loadTexts: foreFastIfAdminStatus.setDescription('Indicates the admin status of this interface.')
foreFastIwfStatsTable = MibTable((1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 1, 21, 2), )
if mibBuilder.loadTexts: foreFastIwfStatsTable.setStatus('current')
if mibBuilder.loadTexts: foreFastIwfStatsTable.setDescription('A table containing Fast IWF interface Statistics')
foreFastIwfStatsEntry = MibTableRow((1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 1, 21, 2, 1), ).setIndexNames((0, "IF-MIB", "ifIndex"))
if mibBuilder.loadTexts: foreFastIwfStatsEntry.setStatus('current')
if mibBuilder.loadTexts: foreFastIwfStatsEntry.setDescription('A table entry containing the FastIwf statistics.')
foreFastIwfTxCells = MibTableColumn((1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 1, 21, 2, 1, 1), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: foreFastIwfTxCells.setStatus('current')
if mibBuilder.loadTexts: foreFastIwfTxCells.setDescription('The number of cells that have arrived at the ATM SAP from the upper layer.')
foreFastIwfTxOctets = MibTableColumn((1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 1, 21, 2, 1, 2), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: foreFastIwfTxOctets.setStatus('current')
if mibBuilder.loadTexts: foreFastIwfTxOctets.setDescription('The number of octets that the FAST Packet to ATM cells layer has passed to the lower layer.')
foreFastIwfTxPackets = MibTableColumn((1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 1, 21, 2, 1, 3), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: foreFastIwfTxPackets.setStatus('current')
if mibBuilder.loadTexts: foreFastIwfTxPackets.setDescription('The number of pkts that the FAST Packet to ATM cells layer has passed to the lower layer.')
foreFastIwfTxHdrLookupErr = MibTableColumn((1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 1, 21, 2, 1, 4), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: foreFastIwfTxHdrLookupErr.setStatus('current')
if mibBuilder.loadTexts: foreFastIwfTxHdrLookupErr.setDescription('The number of cells that the FAST Packet to ATM Cells layer has discarded due to addressing errors.')
foreFastIwfTxResourceFail = MibTableColumn((1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 1, 21, 2, 1, 5), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: foreFastIwfTxResourceFail.setStatus('current')
if mibBuilder.loadTexts: foreFastIwfTxResourceFail.setDescription('The number of cells that the FAST Packet To ATM Cells layer has discarded due to resource limitations.')
foreFastIwfRxCells = MibTableColumn((1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 1, 21, 2, 1, 6), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: foreFastIwfRxCells.setStatus('current')
if mibBuilder.loadTexts: foreFastIwfRxCells.setDescription('The number of cells that the ATM SAP has passed to the upper layer.')
foreFastIwfRxOctets = MibTableColumn((1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 1, 21, 2, 1, 7), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: foreFastIwfRxOctets.setStatus('current')
if mibBuilder.loadTexts: foreFastIwfRxOctets.setDescription('The number of octets that the FAST Packet to ATM Cells layer has received from the lower layer.')
foreFastIwfRxPackets = MibTableColumn((1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 1, 21, 2, 1, 8), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: foreFastIwfRxPackets.setStatus('current')
if mibBuilder.loadTexts: foreFastIwfRxPackets.setDescription('The number of FAST Packet to ATM Cells layer has received from the lower layer.')
foreFastIwfRxHdrLookupErr = MibTableColumn((1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 1, 21, 2, 1, 9), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: foreFastIwfRxHdrLookupErr.setStatus('current')
if mibBuilder.loadTexts: foreFastIwfRxHdrLookupErr.setDescription('The number of packets that the FAST Packet to ATM Cells layer has discarded due to addressing errors.')
foreFastIwfRxResourceFail = MibTableColumn((1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 1, 21, 2, 1, 10), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: foreFastIwfRxResourceFail.setStatus('current')
if mibBuilder.loadTexts: foreFastIwfRxResourceFail.setDescription('The number of packets that the FAST Packet to ATM Cells layer has discarded due to resource limitations.')
mibBuilder.exportSymbols("Fore-FAST-MIB", foreFastIwfRxPackets=foreFastIwfRxPackets, foreFastIwfRxCells=foreFastIwfRxCells, foreFastIwfRxOctets=foreFastIwfRxOctets, foreFastIfAdminStatus=foreFastIfAdminStatus, foreFastIwfRxResourceFail=foreFastIwfRxResourceFail, foreFastIfEntry=foreFastIfEntry, foreFastGroup=foreFastGroup, foreFastIwfTxHdrLookupErr=foreFastIwfTxHdrLookupErr, foreFastIwfRxHdrLookupErr=foreFastIwfRxHdrLookupErr, foreFastIwfStatsEntry=foreFastIwfStatsEntry, foreFastIwfTxOctets=foreFastIwfTxOctets, foreFastIwfTxResourceFail=foreFastIwfTxResourceFail, foreFastIwfStatsTable=foreFastIwfStatsTable, foreFastIfFramingMode=foreFastIfFramingMode, foreFastIwfTxPackets=foreFastIwfTxPackets, foreFastIfTable=foreFastIfTable, foreFastIwfTxCells=foreFastIwfTxCells)
