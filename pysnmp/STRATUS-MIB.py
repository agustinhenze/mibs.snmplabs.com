#
# PySNMP MIB module STRATUS-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/STRATUS-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 21:04:08 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsUnion, ConstraintsIntersection, SingleValueConstraint, ValueSizeConstraint, ValueRangeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "ConstraintsIntersection", "SingleValueConstraint", "ValueSizeConstraint", "ValueRangeConstraint")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
Counter32, ModuleIdentity, Gauge32, TimeTicks, ObjectIdentity, Unsigned32, MibIdentifier, Bits, MibScalar, MibTable, MibTableRow, MibTableColumn, IpAddress, NotificationType, Integer32, Counter64, enterprises, iso, NotificationType = mibBuilder.importSymbols("SNMPv2-SMI", "Counter32", "ModuleIdentity", "Gauge32", "TimeTicks", "ObjectIdentity", "Unsigned32", "MibIdentifier", "Bits", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "IpAddress", "NotificationType", "Integer32", "Counter64", "enterprises", "iso", "NotificationType")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
stratus = MibIdentifier((1, 3, 6, 1, 4, 1, 458))
experimental = MibIdentifier((1, 3, 6, 1, 4, 1, 458, 101))
agentInfo = MibIdentifier((1, 3, 6, 1, 4, 1, 458, 102))
systemInfo = MibIdentifier((1, 3, 6, 1, 4, 1, 458, 103))
productIdent = MibIdentifier((1, 3, 6, 1, 4, 1, 458, 104))
ftServerOid = MibIdentifier((1, 3, 6, 1, 4, 1, 458, 105))
stcpOid = MibIdentifier((1, 3, 6, 1, 4, 1, 458, 106))
sraAgentMibFamily = MibScalar((1, 3, 6, 1, 4, 1, 458, 102, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("stcp", 1), ("ftServer", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: sraAgentMibFamily.setStatus('mandatory')
sraAgentMibRevision = MibScalar((1, 3, 6, 1, 4, 1, 458, 102, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1))).clone(namedValues=NamedValues(("rev01", 1)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: sraAgentMibRevision.setStatus('mandatory')
sraSiSystemType = MibScalar((1, 3, 6, 1, 4, 1, 458, 103, 1), ObjectIdentifier()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sraSiSystemType.setStatus('mandatory')
sraSiManufacturer = MibScalar((1, 3, 6, 1, 4, 1, 458, 103, 2), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sraSiManufacturer.setStatus('mandatory')
sraSiModel = MibScalar((1, 3, 6, 1, 4, 1, 458, 103, 3), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sraSiModel.setStatus('mandatory')
sraSiOverallSystemStatus = MibScalar((1, 3, 6, 1, 4, 1, 458, 103, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))).clone(namedValues=NamedValues(("unsupported", 1), ("noFaults", 2), ("systemFault", 3), ("systemDown", 4)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: sraSiOverallSystemStatus.setStatus('mandatory')
sraSiSystemName = MibScalar((1, 3, 6, 1, 4, 1, 458, 103, 5), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sraSiSystemName.setStatus('mandatory')
sraSiSystemSerialNumber = MibScalar((1, 3, 6, 1, 4, 1, 458, 103, 6), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sraSiSystemSerialNumber.setStatus('mandatory')
sraSiSiteID = MibScalar((1, 3, 6, 1, 4, 1, 458, 103, 7), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sraSiSiteID.setStatus('mandatory')
sraSiCpuFamily = MibScalar((1, 3, 6, 1, 4, 1, 458, 103, 8), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6))).clone(namedValues=NamedValues(("unsupported", 1), ("m68k", 2), ("i860", 3), ("hppa", 4), ("ia32", 5), ("ia64", 6)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: sraSiCpuFamily.setStatus('mandatory')
sraSiOsType = MibScalar((1, 3, 6, 1, 4, 1, 458, 103, 9), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6))).clone(namedValues=NamedValues(("unsupported", 1), ("ftx", 2), ("hpux", 3), ("linux", 4), ("vos", 5), ("windows", 6)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: sraSiOsType.setStatus('mandatory')
osFTX = MibIdentifier((1, 3, 6, 1, 4, 1, 458, 104, 1))
sraProductIdFtxJetta = MibIdentifier((1, 3, 6, 1, 4, 1, 458, 104, 1, 1))
sraProductIdFtxPolo = MibIdentifier((1, 3, 6, 1, 4, 1, 458, 104, 1, 2))
osHPUX = MibIdentifier((1, 3, 6, 1, 4, 1, 458, 104, 2))
sraProductIdHpuxPolo = MibIdentifier((1, 3, 6, 1, 4, 1, 458, 104, 2, 1))
osLinux = MibIdentifier((1, 3, 6, 1, 4, 1, 458, 104, 3))
sraProductIdLnxFtsIa32 = MibIdentifier((1, 3, 6, 1, 4, 1, 458, 104, 3, 1))
osVOS = MibIdentifier((1, 3, 6, 1, 4, 1, 458, 104, 4))
sraProductIdVos68k = MibIdentifier((1, 3, 6, 1, 4, 1, 458, 104, 4, 1))
sraProductIdVosI860 = MibIdentifier((1, 3, 6, 1, 4, 1, 458, 104, 4, 2))
sraProductIdVosJetta = MibIdentifier((1, 3, 6, 1, 4, 1, 458, 104, 4, 3))
sraProductIdVosIa32 = MibIdentifier((1, 3, 6, 1, 4, 1, 458, 104, 4, 4))
osWindowsFt = MibIdentifier((1, 3, 6, 1, 4, 1, 458, 104, 5))
sraProductIdWinFtsIa32 = MibIdentifier((1, 3, 6, 1, 4, 1, 458, 104, 5, 1))
sraProductIdWinFtsIa64 = MibIdentifier((1, 3, 6, 1, 4, 1, 458, 104, 5, 2))
osRadio = MibIdentifier((1, 3, 6, 1, 4, 1, 458, 104, 6))
sraProductIdWinRadIa32 = MibIdentifier((1, 3, 6, 1, 4, 1, 458, 104, 6, 1))
ftsmVar = MibIdentifier((1, 3, 6, 1, 4, 1, 458, 105, 1))
ftsmTrapId = MibIdentifier((1, 3, 6, 1, 4, 1, 458, 105, 2))
ftsmTrapData = MibIdentifier((1, 3, 6, 1, 4, 1, 458, 105, 3))
ftsmVarHostModelName = MibScalar((1, 3, 6, 1, 4, 1, 458, 105, 1, 1), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ftsmVarHostModelName.setStatus('mandatory')
ftsmTrapDataDevicePathId = MibScalar((1, 3, 6, 1, 4, 1, 458, 105, 3, 1), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 31))).setMaxAccess("readonly")
if mibBuilder.loadTexts: ftsmTrapDataDevicePathId.setStatus('mandatory')
ftsmTrapDataDeviceClassname = MibScalar((1, 3, 6, 1, 4, 1, 458, 105, 3, 2), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ftsmTrapDataDeviceClassname.setStatus('mandatory')
ftsmTrapDataNewState = MibScalar((1, 3, 6, 1, 4, 1, 458, 105, 3, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(65536, 65560, 131073, 131076, 131078, 131079, 131080, 131081, 131082, 131083, 131084, 131085, 131086, 131087, 131088, 262149, 524308, 524309, 1572886, 1572887, 2097154, 2097155))).clone(namedValues=NamedValues(("sraFtsm-state-empty", 65536), ("sraFtsm-state-not-present", 65560), ("sraFtsm-state-removed", 131073), ("sraFtsm-state-dumping", 131076), ("sraFtsm-state-diagnostics-passed", 131078), ("sraFtsm-state-initializing", 131079), ("sraFtsm-state-syncing", 131080), ("sraFtsm-state-firmware-update", 131081), ("sraFtsm-state-offline", 131082), ("sraFtsm-state-device-ready", 131083), ("sraFtsm-state-stopped", 131084), ("sraFtsm-state-stop-pending", 131085), ("sraFtsm-state-remove-pending", 131086), ("sraFtsm-state-surprise-removal", 131087), ("sraFtsm-state-firmware-update-complete", 131088), ("sraFtsm-state-diagnostics", 262149), ("sraFtsm-state-online", 524308), ("sraFtsm-state-simplex", 524309), ("sraFtsm-state-duplex", 1572886), ("sraFtsm-state-triplex", 1572887), ("sraFtsm-state-shot", 2097154), ("sraFtsm-state-broken", 2097155)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: ftsmTrapDataNewState.setStatus('mandatory')
ftsmTrapDataNewReason = MibScalar((1, 3, 6, 1, 4, 1, 458, 105, 3, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17))).clone(namedValues=NamedValues(("sraFtsm-reason-none", 0), ("sraFtsm-reason-below-mtbf", 1), ("sraFtsm-reason-diagnostics-failed", 2), ("sraFtsm-reason-hardware-incompatible", 3), ("sraFtsm-reason-holding-dump", 4), ("sraFtsm-reason-bringup-failed", 5), ("sraFtsm-reason-parent-broken", 6), ("sraFtsm-reason-media-disconnect", 7), ("sraFtsm-reason-firmware-burn-fail", 8), ("sraFtsm-reason-firmware-file-not-found", 9), ("sraFtsm-reason-firmware-file-error", 10), ("sraFtsm-reason-firmware-prom-error", 11), ("sraFtsm-reason-autoburn-disabled", 12), ("sraFtsm-reason-idprom-read-error", 13), ("sraFtsm-reason-primary", 14), ("sraFtsm-reason-secondary", 15), ("sraFtsm-reason-parent-empty", 16), ("sraFtsm-reason-deferred-bringup", 17)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: ftsmTrapDataNewReason.setStatus('mandatory')
ftsmTrapDataNewThreshold = MibScalar((1, 3, 6, 1, 4, 1, 458, 105, 3, 5), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3, 4, 5, 6, 7))).clone(namedValues=NamedValues(("sraFtsm-sensor-status-unavailable", 0), ("sraFtsm-sensor-status-normal", 1), ("sraFtsm-sensor-status-below-warning", 2), ("sraFtsm-sensor-status-below-critical", 3), ("sraFtsm-sensor-status-above-warning", 4), ("sraFtsm-sensor-status-above-critical", 5), ("sraFtsm-sensor-status-below-fatal", 6), ("sraFtsm-sensor-status-above-fatal", 7)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: ftsmTrapDataNewThreshold.setStatus('mandatory')
ftsmTrapDataEventId = MibScalar((1, 3, 6, 1, 4, 1, 458, 105, 3, 6), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ftsmTrapDataEventId.setStatus('mandatory')
ftsmTrapDataAlarmId = MibScalar((1, 3, 6, 1, 4, 1, 458, 105, 3, 7), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ftsmTrapDataAlarmId.setStatus('mandatory')
ftsmTrapDataEventDescription = MibScalar((1, 3, 6, 1, 4, 1, 458, 105, 3, 8), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ftsmTrapDataEventDescription.setStatus('mandatory')
ftsmTrapDataEventParameterStrings = MibIdentifier((1, 3, 6, 1, 4, 1, 458, 105, 3, 9))
ftsmTrapDataEventP1 = MibScalar((1, 3, 6, 1, 4, 1, 458, 105, 3, 9, 1), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ftsmTrapDataEventP1.setStatus('mandatory')
ftsmTrapDataEventP2 = MibScalar((1, 3, 6, 1, 4, 1, 458, 105, 3, 9, 2), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ftsmTrapDataEventP2.setStatus('mandatory')
ftsmTrapDataEventP3 = MibScalar((1, 3, 6, 1, 4, 1, 458, 105, 3, 9, 3), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ftsmTrapDataEventP3.setStatus('mandatory')
ftsmTrapDataEventP4 = MibScalar((1, 3, 6, 1, 4, 1, 458, 105, 3, 9, 4), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ftsmTrapDataEventP4.setStatus('mandatory')
ftsmTrapDataEventP5 = MibScalar((1, 3, 6, 1, 4, 1, 458, 105, 3, 9, 5), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ftsmTrapDataEventP5.setStatus('mandatory')
ftsmTrapDataEventP6 = MibScalar((1, 3, 6, 1, 4, 1, 458, 105, 3, 9, 6), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ftsmTrapDataEventP6.setStatus('mandatory')
ftsmTrapDataEventP7 = MibScalar((1, 3, 6, 1, 4, 1, 458, 105, 3, 9, 7), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ftsmTrapDataEventP7.setStatus('mandatory')
ftsmTrapDataEventP8 = MibScalar((1, 3, 6, 1, 4, 1, 458, 105, 3, 9, 8), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ftsmTrapDataEventP8.setStatus('mandatory')
ftsmTrapDataEventP9 = MibScalar((1, 3, 6, 1, 4, 1, 458, 105, 3, 9, 9), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ftsmTrapDataEventP9.setStatus('mandatory')
ftsmTrapEnterBrokenState = NotificationType((1, 3, 6, 1, 4, 1, 458, 105, 2) + (0,101)).setObjects(("STRATUS-MIB", "ftsmTrapDataDevicePathId"), ("STRATUS-MIB", "ftsmTrapDataDeviceClassname"), ("STRATUS-MIB", "ftsmTrapDataNewState"), ("STRATUS-MIB", "ftsmTrapDataNewReason"))
ftsmTrapLeaveBrokenState = NotificationType((1, 3, 6, 1, 4, 1, 458, 105, 2) + (0,102)).setObjects(("STRATUS-MIB", "ftsmTrapDataDevicePathId"), ("STRATUS-MIB", "ftsmTrapDataDeviceClassname"), ("STRATUS-MIB", "ftsmTrapDataNewState"), ("STRATUS-MIB", "ftsmTrapDataNewReason"))
ftsmTrapEnterOnlineState = NotificationType((1, 3, 6, 1, 4, 1, 458, 105, 2) + (0,103)).setObjects(("STRATUS-MIB", "ftsmTrapDataDevicePathId"), ("STRATUS-MIB", "ftsmTrapDataDeviceClassname"), ("STRATUS-MIB", "ftsmTrapDataNewState"), ("STRATUS-MIB", "ftsmTrapDataNewReason"))
ftsmTrapLeaveOnlineState = NotificationType((1, 3, 6, 1, 4, 1, 458, 105, 2) + (0,104)).setObjects(("STRATUS-MIB", "ftsmTrapDataDevicePathId"), ("STRATUS-MIB", "ftsmTrapDataDeviceClassname"), ("STRATUS-MIB", "ftsmTrapDataNewState"), ("STRATUS-MIB", "ftsmTrapDataNewReason"))
ftsmTrapEnterOutOfServiceState = NotificationType((1, 3, 6, 1, 4, 1, 458, 105, 2) + (0,105)).setObjects(("STRATUS-MIB", "ftsmTrapDataDevicePathId"), ("STRATUS-MIB", "ftsmTrapDataDeviceClassname"), ("STRATUS-MIB", "ftsmTrapDataNewState"), ("STRATUS-MIB", "ftsmTrapDataNewReason"))
ftsmTrapLeaveOutOfServiceState = NotificationType((1, 3, 6, 1, 4, 1, 458, 105, 2) + (0,106)).setObjects(("STRATUS-MIB", "ftsmTrapDataDevicePathId"), ("STRATUS-MIB", "ftsmTrapDataDeviceClassname"), ("STRATUS-MIB", "ftsmTrapDataNewState"), ("STRATUS-MIB", "ftsmTrapDataNewReason"))
ftsmTrapImprove2Normal = NotificationType((1, 3, 6, 1, 4, 1, 458, 105, 2) + (0,201)).setObjects(("STRATUS-MIB", "ftsmTrapDataDevicePathId"), ("STRATUS-MIB", "ftsmTrapDataDeviceClassname"), ("STRATUS-MIB", "ftsmTrapDataNewState"), ("STRATUS-MIB", "ftsmTrapDataNewReason"), ("STRATUS-MIB", "ftsmTrapDataNewThreshold"))
ftsmTrapImprove2Warning = NotificationType((1, 3, 6, 1, 4, 1, 458, 105, 2) + (0,202)).setObjects(("STRATUS-MIB", "ftsmTrapDataDevicePathId"), ("STRATUS-MIB", "ftsmTrapDataDeviceClassname"), ("STRATUS-MIB", "ftsmTrapDataNewState"), ("STRATUS-MIB", "ftsmTrapDataNewReason"), ("STRATUS-MIB", "ftsmTrapDataNewThreshold"))
ftsmTrapImprove2Critical = NotificationType((1, 3, 6, 1, 4, 1, 458, 105, 2) + (0,203)).setObjects(("STRATUS-MIB", "ftsmTrapDataDevicePathId"), ("STRATUS-MIB", "ftsmTrapDataDeviceClassname"), ("STRATUS-MIB", "ftsmTrapDataNewState"), ("STRATUS-MIB", "ftsmTrapDataNewReason"), ("STRATUS-MIB", "ftsmTrapDataNewThreshold"))
ftsmTrapUnavailable = NotificationType((1, 3, 6, 1, 4, 1, 458, 105, 2) + (0,204)).setObjects(("STRATUS-MIB", "ftsmTrapDataDevicePathId"), ("STRATUS-MIB", "ftsmTrapDataDeviceClassname"), ("STRATUS-MIB", "ftsmTrapDataNewState"), ("STRATUS-MIB", "ftsmTrapDataNewReason"), ("STRATUS-MIB", "ftsmTrapDataNewThreshold"))
ftsmTrapWorse2Fatal = NotificationType((1, 3, 6, 1, 4, 1, 458, 105, 2) + (0,205)).setObjects(("STRATUS-MIB", "ftsmTrapDataDevicePathId"), ("STRATUS-MIB", "ftsmTrapDataDeviceClassname"), ("STRATUS-MIB", "ftsmTrapDataNewState"), ("STRATUS-MIB", "ftsmTrapDataNewReason"), ("STRATUS-MIB", "ftsmTrapDataNewThreshold"))
ftsmTrapWorse2Critical = NotificationType((1, 3, 6, 1, 4, 1, 458, 105, 2) + (0,206)).setObjects(("STRATUS-MIB", "ftsmTrapDataDevicePathId"), ("STRATUS-MIB", "ftsmTrapDataDeviceClassname"), ("STRATUS-MIB", "ftsmTrapDataNewState"), ("STRATUS-MIB", "ftsmTrapDataNewReason"), ("STRATUS-MIB", "ftsmTrapDataNewThreshold"))
ftsmTrapWorse2Warning = NotificationType((1, 3, 6, 1, 4, 1, 458, 105, 2) + (0,207)).setObjects(("STRATUS-MIB", "ftsmTrapDataDevicePathId"), ("STRATUS-MIB", "ftsmTrapDataDeviceClassname"), ("STRATUS-MIB", "ftsmTrapDataNewState"), ("STRATUS-MIB", "ftsmTrapDataNewReason"), ("STRATUS-MIB", "ftsmTrapDataNewThreshold"))
ftsmTrapMgmtServiceFailure = NotificationType((1, 3, 6, 1, 4, 1, 458, 105, 2) + (0,301)).setObjects(("STRATUS-MIB", "ftsmTrapDataEventId"), ("STRATUS-MIB", "ftsmTrapDataAlarmId"), ("STRATUS-MIB", "ftsmTrapDataEventDescription"))
ftsmTrapUnsentAlarm = NotificationType((1, 3, 6, 1, 4, 1, 458, 105, 2) + (0,302)).setObjects(("STRATUS-MIB", "ftsmTrapDataEventId"), ("STRATUS-MIB", "ftsmTrapDataAlarmId"), ("STRATUS-MIB", "ftsmTrapDataEventDescription"))
mibBuilder.exportSymbols("STRATUS-MIB", systemInfo=systemInfo, stratus=stratus, ftsmTrapDataEventP7=ftsmTrapDataEventP7, ftsmTrapEnterOnlineState=ftsmTrapEnterOnlineState, sraProductIdVosI860=sraProductIdVosI860, sraProductIdWinRadIa32=sraProductIdWinRadIa32, ftsmTrapWorse2Fatal=ftsmTrapWorse2Fatal, ftsmTrapDataEventP8=ftsmTrapDataEventP8, sraSiOsType=sraSiOsType, sraSiSystemName=sraSiSystemName, ftsmVarHostModelName=ftsmVarHostModelName, ftsmTrapDataDevicePathId=ftsmTrapDataDevicePathId, sraProductIdVosJetta=sraProductIdVosJetta, ftsmTrapDataEventDescription=ftsmTrapDataEventDescription, ftsmTrapDataEventParameterStrings=ftsmTrapDataEventParameterStrings, ftsmTrapDataEventP9=ftsmTrapDataEventP9, ftsmTrapUnavailable=ftsmTrapUnavailable, agentInfo=agentInfo, sraProductIdLnxFtsIa32=sraProductIdLnxFtsIa32, ftsmTrapDataNewState=ftsmTrapDataNewState, ftsmTrapEnterBrokenState=ftsmTrapEnterBrokenState, ftsmTrapWorse2Warning=ftsmTrapWorse2Warning, ftsmTrapData=ftsmTrapData, ftsmTrapDataAlarmId=ftsmTrapDataAlarmId, experimental=experimental, osRadio=osRadio, sraSiManufacturer=sraSiManufacturer, sraSiOverallSystemStatus=sraSiOverallSystemStatus, ftsmTrapDataEventP5=ftsmTrapDataEventP5, stcpOid=stcpOid, sraProductIdVos68k=sraProductIdVos68k, osVOS=osVOS, ftsmTrapDataDeviceClassname=ftsmTrapDataDeviceClassname, sraSiSystemSerialNumber=sraSiSystemSerialNumber, ftsmTrapDataEventId=ftsmTrapDataEventId, ftsmTrapDataEventP1=ftsmTrapDataEventP1, ftsmTrapDataEventP3=ftsmTrapDataEventP3, osLinux=osLinux, sraSiCpuFamily=sraSiCpuFamily, osHPUX=osHPUX, sraSiModel=sraSiModel, ftsmTrapDataEventP6=ftsmTrapDataEventP6, productIdent=productIdent, ftsmTrapMgmtServiceFailure=ftsmTrapMgmtServiceFailure, sraProductIdWinFtsIa64=sraProductIdWinFtsIa64, osFTX=osFTX, ftsmTrapLeaveOnlineState=ftsmTrapLeaveOnlineState, ftsmTrapLeaveOutOfServiceState=ftsmTrapLeaveOutOfServiceState, ftsmTrapWorse2Critical=ftsmTrapWorse2Critical, ftsmTrapDataNewReason=ftsmTrapDataNewReason, ftsmTrapDataEventP2=ftsmTrapDataEventP2, sraProductIdFtxJetta=sraProductIdFtxJetta, osWindowsFt=osWindowsFt, sraProductIdVosIa32=sraProductIdVosIa32, ftsmTrapLeaveBrokenState=ftsmTrapLeaveBrokenState, sraAgentMibRevision=sraAgentMibRevision, ftServerOid=ftServerOid, ftsmTrapDataEventP4=ftsmTrapDataEventP4, ftsmVar=ftsmVar, ftsmTrapDataNewThreshold=ftsmTrapDataNewThreshold, sraSiSiteID=sraSiSiteID, ftsmTrapImprove2Critical=ftsmTrapImprove2Critical, sraProductIdFtxPolo=sraProductIdFtxPolo, ftsmTrapId=ftsmTrapId, ftsmTrapEnterOutOfServiceState=ftsmTrapEnterOutOfServiceState, ftsmTrapImprove2Warning=ftsmTrapImprove2Warning, ftsmTrapUnsentAlarm=ftsmTrapUnsentAlarm, sraSiSystemType=sraSiSystemType, sraAgentMibFamily=sraAgentMibFamily, sraProductIdWinFtsIa32=sraProductIdWinFtsIa32, sraProductIdHpuxPolo=sraProductIdHpuxPolo, ftsmTrapImprove2Normal=ftsmTrapImprove2Normal)