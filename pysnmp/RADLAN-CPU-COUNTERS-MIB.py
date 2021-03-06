#
# PySNMP MIB module RADLAN-CPU-COUNTERS-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/RADLAN-CPU-COUNTERS-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 20:37:30 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ConstraintsUnion, SingleValueConstraint, ValueRangeConstraint, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ConstraintsUnion", "SingleValueConstraint", "ValueRangeConstraint", "ValueSizeConstraint")
rnd, = mibBuilder.importSymbols("RADLAN-MIB", "rnd")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
MibIdentifier, TimeTicks, MibScalar, MibTable, MibTableRow, MibTableColumn, iso, ObjectIdentity, ModuleIdentity, Integer32, IpAddress, Counter64, NotificationType, Gauge32, Unsigned32, Counter32, Bits = mibBuilder.importSymbols("SNMPv2-SMI", "MibIdentifier", "TimeTicks", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "iso", "ObjectIdentity", "ModuleIdentity", "Integer32", "IpAddress", "Counter64", "NotificationType", "Gauge32", "Unsigned32", "Counter32", "Bits")
TextualConvention, TruthValue, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "TruthValue", "DisplayString")
rlCpuCounters = ModuleIdentity((1, 3, 6, 1, 4, 1, 89, 124))
rlCpuCounters.setRevisions(('2007-05-15 00:00',))
if mibBuilder.loadTexts: rlCpuCounters.setLastUpdated('2007010600Z')
if mibBuilder.loadTexts: rlCpuCounters.setOrganization('Radlan Computer Communications Ltd.')
rlCpuCountersTable = MibTable((1, 3, 6, 1, 4, 1, 89, 124, 1), )
if mibBuilder.loadTexts: rlCpuCountersTable.setStatus('current')
rlCpuCountersEntry = MibTableRow((1, 3, 6, 1, 4, 1, 89, 124, 1, 1), ).setIndexNames((0, "RADLAN-CPU-COUNTERS-MIB", "rlCpuCountersTarget"))
if mibBuilder.loadTexts: rlCpuCountersEntry.setStatus('current')
rlCpuCountersTarget = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 124, 1, 1, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0))).clone(namedValues=NamedValues(("cpuCounters", 0))))
if mibBuilder.loadTexts: rlCpuCountersTarget.setStatus('current')
rlCpuCountersTxBC = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 124, 1, 1, 2), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rlCpuCountersTxBC.setStatus('current')
rlCpuCountersTxMC = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 124, 1, 1, 3), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rlCpuCountersTxMC.setStatus('current')
rlCpuCountersTxUC = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 124, 1, 1, 4), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rlCpuCountersTxUC.setStatus('current')
rlCpuCountersTxOctets = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 124, 1, 1, 5), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rlCpuCountersTxOctets.setStatus('current')
rlCpuCountersRxBC = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 124, 1, 1, 6), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rlCpuCountersRxBC.setStatus('current')
rlCpuCountersRxMC = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 124, 1, 1, 7), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rlCpuCountersRxMC.setStatus('current')
rlCpuCountersRxUC = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 124, 1, 1, 8), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rlCpuCountersRxUC.setStatus('current')
rlCpuCountersRxOctets = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 124, 1, 1, 9), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rlCpuCountersRxOctets.setStatus('current')
rlCpuCountersReset = MibScalar((1, 3, 6, 1, 4, 1, 89, 124, 2), TruthValue().clone('false')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rlCpuCountersReset.setStatus('current')
rlCpuCountersEnabled = MibScalar((1, 3, 6, 1, 4, 1, 89, 124, 3), TruthValue().clone('false')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rlCpuCountersEnabled.setStatus('current')
mibBuilder.exportSymbols("RADLAN-CPU-COUNTERS-MIB", rlCpuCountersTxMC=rlCpuCountersTxMC, rlCpuCountersTable=rlCpuCountersTable, rlCpuCountersEntry=rlCpuCountersEntry, rlCpuCountersTxBC=rlCpuCountersTxBC, rlCpuCountersTxUC=rlCpuCountersTxUC, rlCpuCountersReset=rlCpuCountersReset, rlCpuCountersEnabled=rlCpuCountersEnabled, rlCpuCounters=rlCpuCounters, rlCpuCountersRxBC=rlCpuCountersRxBC, rlCpuCountersRxOctets=rlCpuCountersRxOctets, rlCpuCountersRxMC=rlCpuCountersRxMC, rlCpuCountersRxUC=rlCpuCountersRxUC, PYSNMP_MODULE_ID=rlCpuCounters, rlCpuCountersTarget=rlCpuCountersTarget, rlCpuCountersTxOctets=rlCpuCountersTxOctets)
