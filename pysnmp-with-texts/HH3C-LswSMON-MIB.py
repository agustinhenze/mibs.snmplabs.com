#
# PySNMP MIB module HH3C-LswSMON-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/HH3C-LswSMON-MIB
# Produced by pysmi-0.3.4 at Wed May  1 13:28:13 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion", "ValueSizeConstraint")
hh3cRhw, = mibBuilder.importSymbols("HH3C-OID-MIB", "hh3cRhw")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
Unsigned32, Integer32, Counter64, TimeTicks, NotificationType, MibIdentifier, Counter32, iso, Gauge32, ModuleIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, Bits, IpAddress, ObjectIdentity = mibBuilder.importSymbols("SNMPv2-SMI", "Unsigned32", "Integer32", "Counter64", "TimeTicks", "NotificationType", "MibIdentifier", "Counter32", "iso", "Gauge32", "ModuleIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Bits", "IpAddress", "ObjectIdentity")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
hh3cSmonExtend = MibIdentifier((1, 3, 6, 1, 4, 1, 25506, 8, 26))
hh3csmonExtendObject = MibIdentifier((1, 3, 6, 1, 4, 1, 25506, 8, 26, 1))
hh3cdot1qVlanStatNumber = MibScalar((1, 3, 6, 1, 4, 1, 25506, 8, 26, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hh3cdot1qVlanStatNumber.setStatus('mandatory')
if mibBuilder.loadTexts: hh3cdot1qVlanStatNumber.setDescription('The number of vlans that can collect statistics of packets.')
hh3cdot1qVlanStatStatusTable = MibTable((1, 3, 6, 1, 4, 1, 25506, 8, 26, 1, 2), )
if mibBuilder.loadTexts: hh3cdot1qVlanStatStatusTable.setStatus('mandatory')
if mibBuilder.loadTexts: hh3cdot1qVlanStatStatusTable.setDescription('VLAN statistics status table.')
hh3cdot1qVlanStatStatusEntry = MibTableRow((1, 3, 6, 1, 4, 1, 25506, 8, 26, 1, 2, 1), ).setIndexNames((0, "HH3C-LswSMON-MIB", "hh3cdot1qVlanStatEnableIndex"))
if mibBuilder.loadTexts: hh3cdot1qVlanStatStatusEntry.setStatus('mandatory')
if mibBuilder.loadTexts: hh3cdot1qVlanStatStatusEntry.setDescription(' VLAN statistics status table entry.')
hh3cdot1qVlanStatEnableIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 8, 26, 1, 2, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hh3cdot1qVlanStatEnableIndex.setStatus('mandatory')
if mibBuilder.loadTexts: hh3cdot1qVlanStatEnableIndex.setDescription('Vlan index .')
hh3cdot1qVlanStatEnableStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 8, 26, 1, 2, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enabled", 1), ("disabled", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hh3cdot1qVlanStatEnableStatus.setStatus('mandatory')
if mibBuilder.loadTexts: hh3cdot1qVlanStatEnableStatus.setDescription('VLAN Statistics Status.It represent the current VLAN supports statistic or not.')
mibBuilder.exportSymbols("HH3C-LswSMON-MIB", hh3cdot1qVlanStatStatusTable=hh3cdot1qVlanStatStatusTable, hh3cdot1qVlanStatStatusEntry=hh3cdot1qVlanStatStatusEntry, hh3cdot1qVlanStatEnableStatus=hh3cdot1qVlanStatEnableStatus, hh3csmonExtendObject=hh3csmonExtendObject, hh3cdot1qVlanStatEnableIndex=hh3cdot1qVlanStatEnableIndex, hh3cdot1qVlanStatNumber=hh3cdot1qVlanStatNumber, hh3cSmonExtend=hh3cSmonExtend)
