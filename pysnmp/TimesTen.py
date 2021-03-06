#
# PySNMP MIB module TimesTen (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/TimesTen
# Produced by pysmi-0.3.4 at Mon Apr 29 21:20:54 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
ObjectIdentifier, Integer, OctetString = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "Integer", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsIntersection, ConstraintsUnion, SingleValueConstraint, ValueRangeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsIntersection", "ConstraintsUnion", "SingleValueConstraint", "ValueRangeConstraint")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
Integer32, ModuleIdentity, Gauge32, Bits, iso, Unsigned32, TimeTicks, MibScalar, MibTable, MibTableRow, MibTableColumn, NotificationType, Counter64, IpAddress, MibIdentifier, Counter32, enterprises, ObjectIdentity, NotificationType = mibBuilder.importSymbols("SNMPv2-SMI", "Integer32", "ModuleIdentity", "Gauge32", "Bits", "iso", "Unsigned32", "TimeTicks", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "NotificationType", "Counter64", "IpAddress", "MibIdentifier", "Counter32", "enterprises", "ObjectIdentity", "NotificationType")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
timesten = MibIdentifier((1, 3, 6, 1, 4, 1, 5549))
ttSystem = MibIdentifier((1, 3, 6, 1, 4, 1, 5549, 1))
ttTimeStamp = MibScalar((1, 3, 6, 1, 4, 1, 5549, 1, 1), OctetString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ttTimeStamp.setStatus('mandatory')
ttVersion = MibScalar((1, 3, 6, 1, 4, 1, 5549, 1, 2), OctetString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ttVersion.setStatus('mandatory')
ttPid = MibScalar((1, 3, 6, 1, 4, 1, 5549, 1, 3), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ttPid.setStatus('mandatory')
ttProcessName = MibScalar((1, 3, 6, 1, 4, 1, 5549, 1, 4), OctetString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ttProcessName.setStatus('obsolete')
ttUid = MibScalar((1, 3, 6, 1, 4, 1, 5549, 1, 5), OctetString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ttUid.setStatus('mandatory')
ttUserName = MibScalar((1, 3, 6, 1, 4, 1, 5549, 1, 6), OctetString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ttUserName.setStatus('obsolete')
ttMsg = MibIdentifier((1, 3, 6, 1, 4, 1, 5549, 2))
ttMesg = MibScalar((1, 3, 6, 1, 4, 1, 5549, 2, 1), OctetString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ttMesg.setStatus('mandatory')
ttTraps = MibIdentifier((1, 3, 6, 1, 4, 1, 5549, 5))
ttAssertTraps = MibIdentifier((1, 3, 6, 1, 4, 1, 5549, 5, 1))
ttDSTraps = MibIdentifier((1, 3, 6, 1, 4, 1, 5549, 5, 10))
ttFileTraps = MibIdentifier((1, 3, 6, 1, 4, 1, 5549, 5, 20))
ttDaemonTraps = MibIdentifier((1, 3, 6, 1, 4, 1, 5549, 5, 40))
ttRepTraps = MibIdentifier((1, 3, 6, 1, 4, 1, 5549, 5, 50))
ttOraTraps = MibIdentifier((1, 3, 6, 1, 4, 1, 5549, 5, 60))
ttRecoveryTraps = MibIdentifier((1, 3, 6, 1, 4, 1, 5549, 5, 70))
ttTrapTruncated = MibScalar((1, 3, 6, 1, 4, 1, 5549, 5, 100), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ttTrapTruncated.setStatus('mandatory')
ttDataStore = MibIdentifier((1, 3, 6, 1, 4, 1, 5549, 10))
ttDSName = MibScalar((1, 3, 6, 1, 4, 1, 5549, 10, 2), OctetString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ttDSName.setStatus('mandatory')
ttDSPath = MibScalar((1, 3, 6, 1, 4, 1, 5549, 10, 3), OctetString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ttDSPath.setStatus('mandatory')
ttDSShmKey = MibScalar((1, 3, 6, 1, 4, 1, 5549, 10, 4), OctetString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ttDSShmKey.setStatus('mandatory')
ttDSNConn = MibScalar((1, 3, 6, 1, 4, 1, 5549, 10, 7), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ttDSNConn.setStatus('mandatory')
ttDSMaxSize = MibScalar((1, 3, 6, 1, 4, 1, 5549, 10, 8), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ttDSMaxSize.setStatus('mandatory')
ttDSCurSize = MibScalar((1, 3, 6, 1, 4, 1, 5549, 10, 9), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ttDSCurSize.setStatus('mandatory')
ttDSReqSize = MibScalar((1, 3, 6, 1, 4, 1, 5549, 10, 10), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ttDSReqSize.setStatus('mandatory')
ttDSPartition = MibScalar((1, 3, 6, 1, 4, 1, 5549, 10, 11), OctetString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ttDSPartition.setStatus('mandatory')
ttFile = MibIdentifier((1, 3, 6, 1, 4, 1, 5549, 20))
ttFilePath = MibScalar((1, 3, 6, 1, 4, 1, 5549, 20, 3), OctetString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ttFilePath.setStatus('mandatory')
ttReadSize = MibScalar((1, 3, 6, 1, 4, 1, 5549, 20, 6), OctetString()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ttReadSize.setStatus('mandatory')
ttReadReq = MibScalar((1, 3, 6, 1, 4, 1, 5549, 20, 7), OctetString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ttReadReq.setStatus('mandatory')
ttWriteSize = MibScalar((1, 3, 6, 1, 4, 1, 5549, 20, 8), OctetString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ttWriteSize.setStatus('mandatory')
ttWriteReq = MibScalar((1, 3, 6, 1, 4, 1, 5549, 20, 9), OctetString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ttWriteReq.setStatus('mandatory')
ttDaemon = MibIdentifier((1, 3, 6, 1, 4, 1, 5549, 40))
ttDaeName = MibScalar((1, 3, 6, 1, 4, 1, 5549, 40, 2), OctetString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ttDaeName.setStatus('mandatory')
ttDaePid = MibScalar((1, 3, 6, 1, 4, 1, 5549, 40, 4), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ttDaePid.setStatus('mandatory')
ttDaeInst = MibScalar((1, 3, 6, 1, 4, 1, 5549, 40, 6), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ttDaeInst.setStatus('mandatory')
ttReplication = MibIdentifier((1, 3, 6, 1, 4, 1, 5549, 50))
ttRepPid = MibScalar((1, 3, 6, 1, 4, 1, 5549, 50, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ttRepPid.setStatus('mandatory')
ttRepName = MibScalar((1, 3, 6, 1, 4, 1, 5549, 50, 2), OctetString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ttRepName.setStatus('mandatory')
ttRepPeerStoreID = MibScalar((1, 3, 6, 1, 4, 1, 5549, 50, 3), OctetString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ttRepPeerStoreID.setStatus('mandatory')
ttRepPeerName = MibScalar((1, 3, 6, 1, 4, 1, 5549, 50, 4), OctetString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ttRepPeerName.setStatus('mandatory')
ttRepMasterHost = MibScalar((1, 3, 6, 1, 4, 1, 5549, 50, 5), OctetString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ttRepMasterHost.setStatus('mandatory')
ttRepMasterPort = MibScalar((1, 3, 6, 1, 4, 1, 5549, 50, 6), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ttRepMasterPort.setStatus('mandatory')
ttRepSubscriberHost = MibScalar((1, 3, 6, 1, 4, 1, 5549, 50, 7), OctetString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ttRepSubscriberHost.setStatus('mandatory')
ttRepSubscriberPort = MibScalar((1, 3, 6, 1, 4, 1, 5549, 50, 8), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ttRepSubscriberPort.setStatus('mandatory')
ttRepTable = MibScalar((1, 3, 6, 1, 4, 1, 5549, 50, 9), OctetString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ttRepTable.setStatus('mandatory')
ttRepAction = MibScalar((1, 3, 6, 1, 4, 1, 5549, 50, 10), OctetString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ttRepAction.setStatus('mandatory')
ttRepReason = MibScalar((1, 3, 6, 1, 4, 1, 5549, 50, 11), OctetString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ttRepReason.setStatus('mandatory')
ttRepConflictKey = MibScalar((1, 3, 6, 1, 4, 1, 5549, 50, 12), OctetString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ttRepConflictKey.setStatus('mandatory')
ttOraCache = MibIdentifier((1, 3, 6, 1, 4, 1, 5549, 60))
ttOraAgentName = MibScalar((1, 3, 6, 1, 4, 1, 5549, 60, 2), OctetString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ttOraAgentName.setStatus('mandatory')
ttOraAgentPid = MibScalar((1, 3, 6, 1, 4, 1, 5549, 60, 3), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ttOraAgentPid.setStatus('mandatory')
ttOraDSName = MibScalar((1, 3, 6, 1, 4, 1, 5549, 60, 4), OctetString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ttOraDSName.setStatus('mandatory')
ttOraCacheGroupName = MibScalar((1, 3, 6, 1, 4, 1, 5549, 60, 5), OctetString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ttOraCacheGroupName.setStatus('mandatory')
ttRecovery = MibIdentifier((1, 3, 6, 1, 4, 1, 5549, 70))
endLFN = MibScalar((1, 3, 6, 1, 4, 1, 5549, 70, 1), OctetString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: endLFN.setStatus('mandatory')
endLFO = MibScalar((1, 3, 6, 1, 4, 1, 5549, 70, 2), OctetString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: endLFO.setStatus('mandatory')
maxLFN = MibScalar((1, 3, 6, 1, 4, 1, 5549, 70, 3), OctetString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: maxLFN.setStatus('mandatory')
ttAssertFailTrap = NotificationType((1, 3, 6, 1, 4, 1, 5549, 5, 1) + (0,1)).setObjects(("TimesTen", "ttTimeStamp"), ("TimesTen", "ttPid"), ("TimesTen", "ttUid"), ("TimesTen", "ttVersion"), ("TimesTen", "ttMesg"))
ttMainDaemonReadyTrap = NotificationType((1, 3, 6, 1, 4, 1, 5549, 5, 40) + (0,2)).setObjects(("TimesTen", "ttTimeStamp"), ("TimesTen", "ttPid"), ("TimesTen", "ttUid"), ("TimesTen", "ttVersion"), ("TimesTen", "ttMesg"), ("TimesTen", "ttDaeName"), ("TimesTen", "ttDaeInst"), ("TimesTen", "ttDaePid"))
ttMainDaemonExitingTrap = NotificationType((1, 3, 6, 1, 4, 1, 5549, 5, 40) + (0,3)).setObjects(("TimesTen", "ttTimeStamp"), ("TimesTen", "ttPid"), ("TimesTen", "ttUid"), ("TimesTen", "ttVersion"), ("TimesTen", "ttMesg"), ("TimesTen", "ttDaeName"), ("TimesTen", "ttDaeInst"), ("TimesTen", "ttDaePid"))
ttMainDaemonDiedTrap = NotificationType((1, 3, 6, 1, 4, 1, 5549, 5, 40) + (0,4)).setObjects(("TimesTen", "ttTimeStamp"), ("TimesTen", "ttPid"), ("TimesTen", "ttUid"), ("TimesTen", "ttVersion"), ("TimesTen", "ttMesg"), ("TimesTen", "ttDaeName"), ("TimesTen", "ttDaeInst"), ("TimesTen", "ttDaePid"))
ttDSGoingInvalidTrap = NotificationType((1, 3, 6, 1, 4, 1, 5549, 5, 10) + (0,5)).setObjects(("TimesTen", "ttTimeStamp"), ("TimesTen", "ttPid"), ("TimesTen", "ttUid"), ("TimesTen", "ttVersion"), ("TimesTen", "ttMesg"), ("TimesTen", "ttDSName"), ("TimesTen", "ttDSShmKey"), ("TimesTen", "ttDSNConn"))
ttRepAgentStartingTrap = NotificationType((1, 3, 6, 1, 4, 1, 5549, 5, 50) + (0,6)).setObjects(("TimesTen", "ttTimeStamp"), ("TimesTen", "ttPid"), ("TimesTen", "ttUid"), ("TimesTen", "ttVersion"), ("TimesTen", "ttMesg"), ("TimesTen", "ttDSName"))
ttRepAgentExitingTrap = NotificationType((1, 3, 6, 1, 4, 1, 5549, 5, 50) + (0,7)).setObjects(("TimesTen", "ttTimeStamp"), ("TimesTen", "ttPid"), ("TimesTen", "ttUid"), ("TimesTen", "ttVersion"), ("TimesTen", "ttMesg"), ("TimesTen", "ttDSName"))
ttRepAgentDiedTrap = NotificationType((1, 3, 6, 1, 4, 1, 5549, 5, 50) + (0,8)).setObjects(("TimesTen", "ttTimeStamp"), ("TimesTen", "ttPid"), ("TimesTen", "ttUid"), ("TimesTen", "ttVersion"), ("TimesTen", "ttMesg"), ("TimesTen", "ttDSName"), ("TimesTen", "ttRepPid"))
ttRepUpdateFailedTrap = NotificationType((1, 3, 6, 1, 4, 1, 5549, 5, 50) + (0,9)).setObjects(("TimesTen", "ttTimeStamp"), ("TimesTen", "ttPid"), ("TimesTen", "ttUid"), ("TimesTen", "ttVersion"), ("TimesTen", "ttMesg"), ("TimesTen", "ttRepPeerStoreID"), ("TimesTen", "ttRepName"), ("TimesTen", "ttDSName"), ("TimesTen", "ttRepReason"), ("TimesTen", "ttRepTable"), ("TimesTen", "ttRepAction"), ("TimesTen", "ttRepPeerName"), ("TimesTen", "ttRepConflictKey"))
ttRepSubscriberFailedTrap = NotificationType((1, 3, 6, 1, 4, 1, 5549, 5, 50) + (0,10)).setObjects(("TimesTen", "ttTimeStamp"), ("TimesTen", "ttPid"), ("TimesTen", "ttUid"), ("TimesTen", "ttVersion"), ("TimesTen", "ttMesg"), ("TimesTen", "ttRepPeerStoreID"), ("TimesTen", "ttRepName"), ("TimesTen", "ttDSName"), ("TimesTen", "ttRepReason"), ("TimesTen", "ttRepSubscriberHost"), ("TimesTen", "ttRepSubscriberPort"))
ttPartitionSpaceStateTrap = NotificationType((1, 3, 6, 1, 4, 1, 5549, 5, 10) + (0,11)).setObjects(("TimesTen", "ttTimeStamp"), ("TimesTen", "ttPid"), ("TimesTen", "ttUid"), ("TimesTen", "ttVersion"), ("TimesTen", "ttMesg"), ("TimesTen", "ttDSName"), ("TimesTen", "ttDSMaxSize"), ("TimesTen", "ttDSCurSize"), ("TimesTen", "ttDSReqSize"), ("TimesTen", "ttDSPartition"))
ttPartitionSpaceExhaustedTrap = NotificationType((1, 3, 6, 1, 4, 1, 5549, 5, 10) + (0,12)).setObjects(("TimesTen", "ttTimeStamp"), ("TimesTen", "ttPid"), ("TimesTen", "ttUid"), ("TimesTen", "ttVersion"), ("TimesTen", "ttMesg"), ("TimesTen", "ttDSName"), ("TimesTen", "ttDSMaxSize"), ("TimesTen", "ttDSCurSize"), ("TimesTen", "ttDSReqSize"), ("TimesTen", "ttDSPartition"))
ttDaemonOutOfMemoryTrap = NotificationType((1, 3, 6, 1, 4, 1, 5549, 5, 40) + (0,13)).setObjects(("TimesTen", "ttTimeStamp"), ("TimesTen", "ttPid"), ("TimesTen", "ttUid"), ("TimesTen", "ttVersion"), ("TimesTen", "ttMesg"), ("TimesTen", "ttDaeName"), ("TimesTen", "ttDaeInst"))
ttOraAutoRefQueFullTrap = NotificationType((1, 3, 6, 1, 4, 1, 5549, 5, 60) + (0,14)).setObjects(("TimesTen", "ttTimeStamp"), ("TimesTen", "ttPid"), ("TimesTen", "ttUid"), ("TimesTen", "ttVersion"), ("TimesTen", "ttMesg"), ("TimesTen", "ttOraAgentPid"), ("TimesTen", "ttOraAgentName"))
ttOraIncAutoRefFailedTrap = NotificationType((1, 3, 6, 1, 4, 1, 5549, 5, 60) + (0,15)).setObjects(("TimesTen", "ttTimeStamp"), ("TimesTen", "ttPid"), ("TimesTen", "ttUid"), ("TimesTen", "ttVersion"), ("TimesTen", "ttMesg"), ("TimesTen", "ttOraAgentPid"), ("TimesTen", "ttOraAgentName"), ("TimesTen", "ttOraDSName"))
ttOraAgentDiedTrap = NotificationType((1, 3, 6, 1, 4, 1, 5549, 5, 60) + (0,17)).setObjects(("TimesTen", "ttTimeStamp"), ("TimesTen", "ttPid"), ("TimesTen", "ttUid"), ("TimesTen", "ttVersion"), ("TimesTen", "ttMesg"), ("TimesTen", "ttOraAgentPid"), ("TimesTen", "ttOraDSName"))
ttRepReturnReceiptTransitionTrap = NotificationType((1, 3, 6, 1, 4, 1, 5549, 5, 50) + (0,19)).setObjects(("TimesTen", "ttTimeStamp"), ("TimesTen", "ttPid"), ("TimesTen", "ttUid"), ("TimesTen", "ttVersion"), ("TimesTen", "ttMesg"), ("TimesTen", "ttRepPeerStoreID"), ("TimesTen", "ttRepName"), ("TimesTen", "ttDSName"), ("TimesTen", "ttRepReason"), ("TimesTen", "ttRepSubscriberHost"))
ttFileWriteErrorTrap = NotificationType((1, 3, 6, 1, 4, 1, 5549, 5, 20) + (0,20)).setObjects(("TimesTen", "ttTimeStamp"), ("TimesTen", "ttPid"), ("TimesTen", "ttUid"), ("TimesTen", "ttVersion"), ("TimesTen", "ttMesg"), ("TimesTen", "ttDSName"), ("TimesTen", "ttFilePath"), ("TimesTen", "ttWriteSize"), ("TimesTen", "ttWriteReq"))
ttDSDataCorruptionTrap = NotificationType((1, 3, 6, 1, 4, 1, 5549, 5, 10) + (0,21)).setObjects(("TimesTen", "ttTimeStamp"), ("TimesTen", "ttPid"), ("TimesTen", "ttUid"), ("TimesTen", "ttVersion"), ("TimesTen", "ttMesg"), ("TimesTen", "ttDSName"))
ttUnexpectedEndOfLogTrap = NotificationType((1, 3, 6, 1, 4, 1, 5549, 5, 70) + (0,22)).setObjects(("TimesTen", "ttTimeStamp"), ("TimesTen", "ttPid"), ("TimesTen", "ttUid"), ("TimesTen", "ttVersion"), ("TimesTen", "ttMesg"), ("TimesTen", "ttDSName"), ("TimesTen", "endLFN"), ("TimesTen", "endLFO"), ("TimesTen", "maxLFN"))
ttRepCatchupStartTrap = NotificationType((1, 3, 6, 1, 4, 1, 5549, 5, 50) + (0,23)).setObjects(("TimesTen", "ttTimeStamp"), ("TimesTen", "ttPid"), ("TimesTen", "ttUid"), ("TimesTen", "ttVersion"), ("TimesTen", "ttMesg"), ("TimesTen", "ttDSName"))
ttRepCatchupStopTrap = NotificationType((1, 3, 6, 1, 4, 1, 5549, 5, 50) + (0,24)).setObjects(("TimesTen", "ttTimeStamp"), ("TimesTen", "ttPid"), ("TimesTen", "ttUid"), ("TimesTen", "ttVersion"), ("TimesTen", "ttMesg"), ("TimesTen", "ttDSName"))
ttOraValidationErrorTrap = NotificationType((1, 3, 6, 1, 4, 1, 5549, 5, 60) + (0,25)).setObjects(("TimesTen", "ttTimeStamp"), ("TimesTen", "ttPid"), ("TimesTen", "ttUid"), ("TimesTen", "ttVersion"), ("TimesTen", "ttMesg"), ("TimesTen", "ttOraAgentPid"), ("TimesTen", "ttOraAgentName"), ("TimesTen", "ttOraDSName"))
ttOraValidationWarningTrap = NotificationType((1, 3, 6, 1, 4, 1, 5549, 5, 60) + (0,26)).setObjects(("TimesTen", "ttTimeStamp"), ("TimesTen", "ttPid"), ("TimesTen", "ttUid"), ("TimesTen", "ttVersion"), ("TimesTen", "ttMesg"), ("TimesTen", "ttOraAgentPid"), ("TimesTen", "ttOraAgentName"), ("TimesTen", "ttOraDSName"))
ttOraValidationAbortedTrap = NotificationType((1, 3, 6, 1, 4, 1, 5549, 5, 60) + (0,27)).setObjects(("TimesTen", "ttTimeStamp"), ("TimesTen", "ttPid"), ("TimesTen", "ttUid"), ("TimesTen", "ttVersion"), ("TimesTen", "ttMesg"), ("TimesTen", "ttOraAgentPid"), ("TimesTen", "ttOraAgentName"), ("TimesTen", "ttOraDSName"))
mibBuilder.exportSymbols("TimesTen", ttDSShmKey=ttDSShmKey, ttRepAgentDiedTrap=ttRepAgentDiedTrap, ttOraAgentPid=ttOraAgentPid, ttOraDSName=ttOraDSName, ttMesg=ttMesg, ttRepAgentExitingTrap=ttRepAgentExitingTrap, ttOraAutoRefQueFullTrap=ttOraAutoRefQueFullTrap, ttOraValidationAbortedTrap=ttOraValidationAbortedTrap, ttTrapTruncated=ttTrapTruncated, ttAssertFailTrap=ttAssertFailTrap, ttProcessName=ttProcessName, ttTimeStamp=ttTimeStamp, ttDSName=ttDSName, ttRepTraps=ttRepTraps, ttDSTraps=ttDSTraps, ttOraValidationErrorTrap=ttOraValidationErrorTrap, ttRepAgentStartingTrap=ttRepAgentStartingTrap, ttRepSubscriberHost=ttRepSubscriberHost, ttVersion=ttVersion, ttDataStore=ttDataStore, ttOraAgentName=ttOraAgentName, ttDaemonOutOfMemoryTrap=ttDaemonOutOfMemoryTrap, ttOraIncAutoRefFailedTrap=ttOraIncAutoRefFailedTrap, ttFileWriteErrorTrap=ttFileWriteErrorTrap, ttDSNConn=ttDSNConn, ttAssertTraps=ttAssertTraps, ttDSGoingInvalidTrap=ttDSGoingInvalidTrap, ttUserName=ttUserName, ttRepPeerStoreID=ttRepPeerStoreID, endLFN=endLFN, ttReadReq=ttReadReq, ttPartitionSpaceExhaustedTrap=ttPartitionSpaceExhaustedTrap, ttTraps=ttTraps, ttFile=ttFile, ttDaeName=ttDaeName, ttRepName=ttRepName, timesten=timesten, ttMsg=ttMsg, ttUnexpectedEndOfLogTrap=ttUnexpectedEndOfLogTrap, ttRepPid=ttRepPid, ttReadSize=ttReadSize, ttRepSubscriberFailedTrap=ttRepSubscriberFailedTrap, endLFO=endLFO, ttDaePid=ttDaePid, ttDSMaxSize=ttDSMaxSize, ttRepMasterPort=ttRepMasterPort, ttRepTable=ttRepTable, ttRecovery=ttRecovery, ttMainDaemonReadyTrap=ttMainDaemonReadyTrap, ttFileTraps=ttFileTraps, ttFilePath=ttFilePath, ttRecoveryTraps=ttRecoveryTraps, ttRepUpdateFailedTrap=ttRepUpdateFailedTrap, ttMainDaemonDiedTrap=ttMainDaemonDiedTrap, ttWriteSize=ttWriteSize, ttDSPath=ttDSPath, maxLFN=maxLFN, ttDSReqSize=ttDSReqSize, ttRepSubscriberPort=ttRepSubscriberPort, ttMainDaemonExitingTrap=ttMainDaemonExitingTrap, ttOraTraps=ttOraTraps, ttRepCatchupStopTrap=ttRepCatchupStopTrap, ttSystem=ttSystem, ttDaemonTraps=ttDaemonTraps, ttRepConflictKey=ttRepConflictKey, ttRepPeerName=ttRepPeerName, ttOraCacheGroupName=ttOraCacheGroupName, ttReplication=ttReplication, ttRepAction=ttRepAction, ttUid=ttUid, ttOraAgentDiedTrap=ttOraAgentDiedTrap, ttDSCurSize=ttDSCurSize, ttPartitionSpaceStateTrap=ttPartitionSpaceStateTrap, ttDSDataCorruptionTrap=ttDSDataCorruptionTrap, ttRepReturnReceiptTransitionTrap=ttRepReturnReceiptTransitionTrap, ttOraCache=ttOraCache, ttDaeInst=ttDaeInst, ttRepReason=ttRepReason, ttWriteReq=ttWriteReq, ttDaemon=ttDaemon, ttDSPartition=ttDSPartition, ttPid=ttPid, ttRepMasterHost=ttRepMasterHost, ttOraValidationWarningTrap=ttOraValidationWarningTrap, ttRepCatchupStartTrap=ttRepCatchupStartTrap)
