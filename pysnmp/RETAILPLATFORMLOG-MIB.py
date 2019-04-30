#
# PySNMP MIB module RETAILPLATFORMLOG-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/RETAILPLATFORMLOG-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 20:47:41 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, ValueSizeConstraint, ConstraintsIntersection, SingleValueConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "ValueSizeConstraint", "ConstraintsIntersection", "SingleValueConstraint", "ConstraintsUnion")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
Counter64, Unsigned32, Bits, TimeTicks, MibIdentifier, NotificationType, Integer32, ObjectIdentity, IpAddress, enterprises, ModuleIdentity, iso, Counter32, MibScalar, MibTable, MibTableRow, MibTableColumn, Gauge32 = mibBuilder.importSymbols("SNMPv2-SMI", "Counter64", "Unsigned32", "Bits", "TimeTicks", "MibIdentifier", "NotificationType", "Integer32", "ObjectIdentity", "IpAddress", "enterprises", "ModuleIdentity", "iso", "Counter32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Gauge32")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
ncr = MibIdentifier((1, 3, 6, 1, 4, 1, 191))
ncr_products = MibIdentifier((1, 3, 6, 1, 4, 1, 191, 1)).setLabel("ncr-products")
log = MibIdentifier((1, 3, 6, 1, 4, 1, 191, 1, 33))
class NTSeverity(Integer32):
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 4, 8, 16))
    namedValues = NamedValues(("error", 1), ("warning", 2), ("information", 4), ("auditSuccess", 8), ("auditFailure", 16))

logSysLog = MibIdentifier((1, 3, 6, 1, 4, 1, 191, 1, 33, 1))
logSysLogTable = MibTable((1, 3, 6, 1, 4, 1, 191, 1, 33, 1, 1), )
if mibBuilder.loadTexts: logSysLogTable.setStatus('mandatory')
logSysLogEntry = MibTableRow((1, 3, 6, 1, 4, 1, 191, 1, 33, 1, 1, 1), ).setIndexNames((0, "RETAILPLATFORMLOG-MIB", "logSysLogIndex"))
if mibBuilder.loadTexts: logSysLogEntry.setStatus('mandatory')
logSysLogIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 191, 1, 33, 1, 1, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: logSysLogIndex.setStatus('mandatory')
logSysLogDate = MibTableColumn((1, 3, 6, 1, 4, 1, 191, 1, 33, 1, 1, 1, 2), OctetString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: logSysLogDate.setStatus('mandatory')
logSysLogTime = MibTableColumn((1, 3, 6, 1, 4, 1, 191, 1, 33, 1, 1, 1, 3), OctetString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: logSysLogTime.setStatus('mandatory')
logSysLogUser = MibTableColumn((1, 3, 6, 1, 4, 1, 191, 1, 33, 1, 1, 1, 4), OctetString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: logSysLogUser.setStatus('mandatory')
logSysLogComputer = MibTableColumn((1, 3, 6, 1, 4, 1, 191, 1, 33, 1, 1, 1, 5), OctetString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: logSysLogComputer.setStatus('mandatory')
logSysLogEventID = MibTableColumn((1, 3, 6, 1, 4, 1, 191, 1, 33, 1, 1, 1, 6), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: logSysLogEventID.setStatus('mandatory')
logSysLogSource = MibTableColumn((1, 3, 6, 1, 4, 1, 191, 1, 33, 1, 1, 1, 7), OctetString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: logSysLogSource.setStatus('mandatory')
logSysLogType = MibTableColumn((1, 3, 6, 1, 4, 1, 191, 1, 33, 1, 1, 1, 8), NTSeverity()).setMaxAccess("readonly")
if mibBuilder.loadTexts: logSysLogType.setStatus('mandatory')
logSysLogCategory = MibTableColumn((1, 3, 6, 1, 4, 1, 191, 1, 33, 1, 1, 1, 9), OctetString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: logSysLogCategory.setStatus('mandatory')
logSysLogDescription = MibTableColumn((1, 3, 6, 1, 4, 1, 191, 1, 33, 1, 1, 1, 10), OctetString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: logSysLogDescription.setStatus('mandatory')
logSysLogData = MibTableColumn((1, 3, 6, 1, 4, 1, 191, 1, 33, 1, 1, 1, 11), OctetString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: logSysLogData.setStatus('mandatory')
logSysLogSize = MibScalar((1, 3, 6, 1, 4, 1, 191, 1, 33, 1, 2), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: logSysLogSize.setStatus('mandatory')
logSysLogReqSize = MibScalar((1, 3, 6, 1, 4, 1, 191, 1, 33, 1, 3), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: logSysLogReqSize.setStatus('mandatory')
logSecLog = MibIdentifier((1, 3, 6, 1, 4, 1, 191, 1, 33, 2))
logSecLogTable = MibTable((1, 3, 6, 1, 4, 1, 191, 1, 33, 2, 1), )
if mibBuilder.loadTexts: logSecLogTable.setStatus('mandatory')
logSecLogEntry = MibTableRow((1, 3, 6, 1, 4, 1, 191, 1, 33, 2, 1, 1), ).setIndexNames((0, "RETAILPLATFORMLOG-MIB", "logSecLogIndex"))
if mibBuilder.loadTexts: logSecLogEntry.setStatus('mandatory')
logSecLogIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 191, 1, 33, 2, 1, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: logSecLogIndex.setStatus('mandatory')
logSecLogDate = MibTableColumn((1, 3, 6, 1, 4, 1, 191, 1, 33, 2, 1, 1, 2), OctetString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: logSecLogDate.setStatus('mandatory')
logSecLogTime = MibTableColumn((1, 3, 6, 1, 4, 1, 191, 1, 33, 2, 1, 1, 3), OctetString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: logSecLogTime.setStatus('mandatory')
logSecLogUser = MibTableColumn((1, 3, 6, 1, 4, 1, 191, 1, 33, 2, 1, 1, 4), OctetString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: logSecLogUser.setStatus('mandatory')
logSecLogComputer = MibTableColumn((1, 3, 6, 1, 4, 1, 191, 1, 33, 2, 1, 1, 5), OctetString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: logSecLogComputer.setStatus('mandatory')
logSecLogEventID = MibTableColumn((1, 3, 6, 1, 4, 1, 191, 1, 33, 2, 1, 1, 6), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: logSecLogEventID.setStatus('mandatory')
logSecLogSource = MibTableColumn((1, 3, 6, 1, 4, 1, 191, 1, 33, 2, 1, 1, 7), OctetString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: logSecLogSource.setStatus('mandatory')
logSecLogType = MibTableColumn((1, 3, 6, 1, 4, 1, 191, 1, 33, 2, 1, 1, 8), NTSeverity()).setMaxAccess("readonly")
if mibBuilder.loadTexts: logSecLogType.setStatus('mandatory')
logSecLogCategory = MibTableColumn((1, 3, 6, 1, 4, 1, 191, 1, 33, 2, 1, 1, 9), OctetString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: logSecLogCategory.setStatus('mandatory')
logSecLogDescription = MibTableColumn((1, 3, 6, 1, 4, 1, 191, 1, 33, 2, 1, 1, 10), OctetString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: logSecLogDescription.setStatus('mandatory')
logSecLogData = MibTableColumn((1, 3, 6, 1, 4, 1, 191, 1, 33, 2, 1, 1, 11), OctetString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: logSecLogData.setStatus('mandatory')
logSecLogSize = MibScalar((1, 3, 6, 1, 4, 1, 191, 1, 33, 2, 2), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: logSecLogSize.setStatus('mandatory')
logSecLogReqSize = MibScalar((1, 3, 6, 1, 4, 1, 191, 1, 33, 2, 3), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: logSecLogReqSize.setStatus('mandatory')
logAppLog = MibIdentifier((1, 3, 6, 1, 4, 1, 191, 1, 33, 3))
logAppLogTable = MibTable((1, 3, 6, 1, 4, 1, 191, 1, 33, 3, 1), )
if mibBuilder.loadTexts: logAppLogTable.setStatus('mandatory')
logAppLogEntry = MibTableRow((1, 3, 6, 1, 4, 1, 191, 1, 33, 3, 1, 1), ).setIndexNames((0, "RETAILPLATFORMLOG-MIB", "logAppLogIndex"))
if mibBuilder.loadTexts: logAppLogEntry.setStatus('mandatory')
logAppLogIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 191, 1, 33, 3, 1, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: logAppLogIndex.setStatus('mandatory')
logAppLogDate = MibTableColumn((1, 3, 6, 1, 4, 1, 191, 1, 33, 3, 1, 1, 2), OctetString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: logAppLogDate.setStatus('mandatory')
logAppLogTime = MibTableColumn((1, 3, 6, 1, 4, 1, 191, 1, 33, 3, 1, 1, 3), OctetString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: logAppLogTime.setStatus('mandatory')
logAppLogUser = MibTableColumn((1, 3, 6, 1, 4, 1, 191, 1, 33, 3, 1, 1, 4), OctetString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: logAppLogUser.setStatus('mandatory')
logAppLogComputer = MibTableColumn((1, 3, 6, 1, 4, 1, 191, 1, 33, 3, 1, 1, 5), OctetString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: logAppLogComputer.setStatus('mandatory')
logAppLogEventID = MibTableColumn((1, 3, 6, 1, 4, 1, 191, 1, 33, 3, 1, 1, 6), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: logAppLogEventID.setStatus('mandatory')
logAppLogSource = MibTableColumn((1, 3, 6, 1, 4, 1, 191, 1, 33, 3, 1, 1, 7), OctetString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: logAppLogSource.setStatus('mandatory')
logAppLogType = MibTableColumn((1, 3, 6, 1, 4, 1, 191, 1, 33, 3, 1, 1, 8), NTSeverity()).setMaxAccess("readonly")
if mibBuilder.loadTexts: logAppLogType.setStatus('mandatory')
logAppLogCategory = MibTableColumn((1, 3, 6, 1, 4, 1, 191, 1, 33, 3, 1, 1, 9), OctetString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: logAppLogCategory.setStatus('mandatory')
logAppLogDescription = MibTableColumn((1, 3, 6, 1, 4, 1, 191, 1, 33, 3, 1, 1, 10), OctetString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: logAppLogDescription.setStatus('mandatory')
logAppLogData = MibTableColumn((1, 3, 6, 1, 4, 1, 191, 1, 33, 3, 1, 1, 11), OctetString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: logAppLogData.setStatus('mandatory')
logAppLogSize = MibScalar((1, 3, 6, 1, 4, 1, 191, 1, 33, 3, 2), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: logAppLogSize.setStatus('mandatory')
logAppLogReqSize = MibScalar((1, 3, 6, 1, 4, 1, 191, 1, 33, 3, 3), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: logAppLogReqSize.setStatus('mandatory')
mibBuilder.exportSymbols("RETAILPLATFORMLOG-MIB", logAppLogReqSize=logAppLogReqSize, logSecLogCategory=logSecLogCategory, logAppLogEventID=logAppLogEventID, logAppLogDate=logAppLogDate, logAppLogCategory=logAppLogCategory, log=log, logAppLogIndex=logAppLogIndex, logSecLogSize=logSecLogSize, logSysLogDate=logSysLogDate, logAppLogTime=logAppLogTime, logSecLogIndex=logSecLogIndex, logSysLogEventID=logSysLogEventID, logSecLogUser=logSecLogUser, logSysLogData=logSysLogData, logSysLogReqSize=logSysLogReqSize, logAppLogSource=logAppLogSource, logSecLogEntry=logSecLogEntry, ncr_products=ncr_products, logSecLogEventID=logSecLogEventID, logAppLogComputer=logAppLogComputer, ncr=ncr, logAppLogSize=logAppLogSize, logSysLogType=logSysLogType, logSysLogCategory=logSysLogCategory, logSecLogComputer=logSecLogComputer, logSecLogDescription=logSecLogDescription, logSecLogData=logSecLogData, logSecLogReqSize=logSecLogReqSize, logSecLog=logSecLog, NTSeverity=NTSeverity, logSysLogTable=logSysLogTable, logSysLogSource=logSysLogSource, logAppLogType=logAppLogType, logAppLogTable=logAppLogTable, logSecLogTable=logSecLogTable, logAppLogDescription=logAppLogDescription, logSecLogTime=logSecLogTime, logSysLog=logSysLog, logAppLogData=logAppLogData, logSysLogIndex=logSysLogIndex, logSysLogComputer=logSysLogComputer, logAppLogEntry=logAppLogEntry, logSysLogSize=logSysLogSize, logAppLogUser=logAppLogUser, logSysLogEntry=logSysLogEntry, logSecLogSource=logSecLogSource, logSecLogType=logSecLogType, logSysLogDescription=logSysLogDescription, logSysLogTime=logSysLogTime, logAppLog=logAppLog, logSysLogUser=logSysLogUser, logSecLogDate=logSecLogDate)