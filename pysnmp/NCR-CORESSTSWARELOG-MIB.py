#
# PySNMP MIB module NCR-CORESSTSWARELOG-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/NCR-CORESSTCOMMSLOG-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 20:07:59 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
OctetString, Integer, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "OctetString", "Integer", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, SingleValueConstraint, ConstraintsUnion, ValueRangeConstraint, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "SingleValueConstraint", "ConstraintsUnion", "ValueRangeConstraint", "ConstraintsIntersection")
TruthValue, = mibBuilder.importSymbols("RFC1253-MIB", "TruthValue")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
ModuleIdentity, Unsigned32, MibIdentifier, Counter64, enterprises, IpAddress, Gauge32, Bits, Integer32, MibScalar, MibTable, MibTableRow, MibTableColumn, TimeTicks, iso, NotificationType, ObjectIdentity, Counter32 = mibBuilder.importSymbols("SNMPv2-SMI", "ModuleIdentity", "Unsigned32", "MibIdentifier", "Counter64", "enterprises", "IpAddress", "Gauge32", "Bits", "Integer32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "TimeTicks", "iso", "NotificationType", "ObjectIdentity", "Counter32")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
ncr = MibIdentifier((1, 3, 6, 1, 4, 1, 191))
sst = MibIdentifier((1, 3, 6, 1, 4, 1, 191, 39))
sstCore = MibIdentifier((1, 3, 6, 1, 4, 1, 191, 39, 1))
sstProduct = MibIdentifier((1, 3, 6, 1, 4, 1, 191, 39, 13))
sstObjs = MibIdentifier((1, 3, 6, 1, 4, 1, 191, 39, 13, 2))
sstGeneral = MibIdentifier((1, 3, 6, 1, 4, 1, 191, 39, 13, 2, 1))
sstDevice = MibIdentifier((1, 3, 6, 1, 4, 1, 191, 39, 13, 2, 2))
sstApplic = MibIdentifier((1, 3, 6, 1, 4, 1, 191, 39, 13, 2, 3))
sstLogs = MibIdentifier((1, 3, 6, 1, 4, 1, 191, 39, 13, 2, 4))
sstSWareLogTable = MibTable((1, 3, 6, 1, 4, 1, 191, 39, 13, 2, 4, 9), )
if mibBuilder.loadTexts: sstSWareLogTable.setStatus('mandatory')
sstSWareLogEntry = MibTableRow((1, 3, 6, 1, 4, 1, 191, 39, 13, 2, 4, 9, 1), ).setIndexNames((0, "NCR-CORESSTSWARELOG-MIB", "sstSWareLogIndex"))
if mibBuilder.loadTexts: sstSWareLogEntry.setStatus('mandatory')
sstSWareLogIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 191, 39, 13, 2, 4, 9, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sstSWareLogIndex.setStatus('mandatory')
sstSWareLogLineNumber = MibTableColumn((1, 3, 6, 1, 4, 1, 191, 39, 13, 2, 4, 9, 1, 2), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sstSWareLogLineNumber.setStatus('mandatory')
sstSWareLogSourceName = MibTableColumn((1, 3, 6, 1, 4, 1, 191, 39, 13, 2, 4, 9, 1, 3), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sstSWareLogSourceName.setStatus('mandatory')
sstSWareLogProcName = MibTableColumn((1, 3, 6, 1, 4, 1, 191, 39, 13, 2, 4, 9, 1, 4), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sstSWareLogProcName.setStatus('mandatory')
sstSWareLogThrdName = MibTableColumn((1, 3, 6, 1, 4, 1, 191, 39, 13, 2, 4, 9, 1, 5), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sstSWareLogThrdName.setStatus('mandatory')
sstSWareLogDLLName = MibTableColumn((1, 3, 6, 1, 4, 1, 191, 39, 13, 2, 4, 9, 1, 6), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sstSWareLogDLLName.setStatus('mandatory')
sstSWareLogEventId = MibTableColumn((1, 3, 6, 1, 4, 1, 191, 39, 13, 2, 4, 9, 1, 7), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sstSWareLogEventId.setStatus('mandatory')
sstSWareLogLevel = MibTableColumn((1, 3, 6, 1, 4, 1, 191, 39, 13, 2, 4, 9, 1, 8), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sstSWareLogLevel.setStatus('mandatory')
sstSWareLogReason = MibTableColumn((1, 3, 6, 1, 4, 1, 191, 39, 13, 2, 4, 9, 1, 9), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sstSWareLogReason.setStatus('mandatory')
sstSWareLogBinaryType = MibTableColumn((1, 3, 6, 1, 4, 1, 191, 39, 13, 2, 4, 9, 1, 10), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sstSWareLogBinaryType.setStatus('mandatory')
sstSWareLogBinaryData = MibTableColumn((1, 3, 6, 1, 4, 1, 191, 39, 13, 2, 4, 9, 1, 11), OctetString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sstSWareLogBinaryData.setStatus('mandatory')
sstSWareLogStrData = MibTableColumn((1, 3, 6, 1, 4, 1, 191, 39, 13, 2, 4, 9, 1, 12), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sstSWareLogStrData.setStatus('mandatory')
mibBuilder.exportSymbols("NCR-CORESSTSWARELOG-MIB", sstApplic=sstApplic, sstSWareLogEventId=sstSWareLogEventId, ncr=ncr, sstDevice=sstDevice, sstSWareLogEntry=sstSWareLogEntry, sstLogs=sstLogs, sstCore=sstCore, sstSWareLogStrData=sstSWareLogStrData, sstSWareLogProcName=sstSWareLogProcName, sstGeneral=sstGeneral, sstProduct=sstProduct, sstObjs=sstObjs, sstSWareLogBinaryType=sstSWareLogBinaryType, sstSWareLogTable=sstSWareLogTable, sstSWareLogLineNumber=sstSWareLogLineNumber, sst=sst, sstSWareLogBinaryData=sstSWareLogBinaryData, sstSWareLogSourceName=sstSWareLogSourceName, sstSWareLogDLLName=sstSWareLogDLLName, sstSWareLogThrdName=sstSWareLogThrdName, sstSWareLogReason=sstSWareLogReason, sstSWareLogIndex=sstSWareLogIndex, sstSWareLogLevel=sstSWareLogLevel)
