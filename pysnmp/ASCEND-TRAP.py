#
# PySNMP MIB module ASCEND-TRAP (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/ASCEND-TRAP
# Produced by pysmi-0.3.4 at Mon Apr 29 17:13:14 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
wanLineIfIndex, wanLineUsage = mibBuilder.importSymbols("ASCEND-ADVANCED-AGENT-MIB", "wanLineIfIndex", "wanLineUsage")
atmpLastErrorGenerated, atmpAgentSentErrorTo, atmpHNProfileName, atmpLastErrorRecv, atmpAgentRecvErrorFrom = mibBuilder.importSymbols("ASCEND-ATMP-MIB", "atmpLastErrorGenerated", "atmpAgentSentErrorTo", "atmpHNProfileName", "atmpLastErrorRecv", "atmpAgentRecvErrorFrom")
callLoggingServerIndex, callLoggingServerIPAddress, callLoggingDroppedPacketCount = mibBuilder.importSymbols("ASCEND-CALL-LOGGING-MIB", "callLoggingServerIndex", "callLoggingServerIPAddress", "callLoggingDroppedPacketCount")
cntrReduSwitchLastTime, slotIndex, cntrReduAvailLastTime, cntrReduCurrentIndex, cntrReduSwitchIndex, cntrReduSwitchReason, slotStatus, cntrReduAvailSlotIndex, cntrReduAvailPrevState, cntrReduAvailCurrState = mibBuilder.importSymbols("ASCEND-CHASSIS-MIB", "cntrReduSwitchLastTime", "slotIndex", "cntrReduAvailLastTime", "cntrReduCurrentIndex", "cntrReduSwitchIndex", "cntrReduSwitchReason", "slotStatus", "cntrReduAvailSlotIndex", "cntrReduAvailPrevState", "cntrReduAvailCurrState")
suspectLanModemSlotIndex, suspectLanModemLast32, suspectLanModemBadCount, suspectLanModemUsedCount, suspectLanModemPortIndex = mibBuilder.importSymbols("ASCEND-LANMODEM-MIB", "suspectLanModemSlotIndex", "suspectLanModemLast32", "suspectLanModemBadCount", "suspectLanModemUsedCount", "suspectLanModemPortIndex")
heartBeatSlotCount, heartBeatSourceAddress, heartBeatPacketCount, heartBeatSlotTimeInterval, heartBeatMulticastGroupAddress = mibBuilder.importSymbols("ASCEND-MCAST-MIB", "heartBeatSlotCount", "heartBeatSourceAddress", "heartBeatPacketCount", "heartBeatSlotTimeInterval", "heartBeatMulticastGroupAddress")
mgOperStatus, mgLinkName = mibBuilder.importSymbols("ASCEND-MGSTAT-MIB", "mgOperStatus", "mgLinkName")
sysLastRestartReason, ascend, fatalLogIndex, sysAbsoluteCurrentTime, consoleIndex, fatalLogReason, sysConfigChange = mibBuilder.importSymbols("ASCEND-MIB", "sysLastRestartReason", "ascend", "fatalLogIndex", "sysAbsoluteCurrentTime", "consoleIndex", "fatalLogReason", "sysConfigChange")
multiShelfState, = mibBuilder.importSymbols("ASCEND-MULTI-SHELF-MIB", "multiShelfState")
powerSupplyState, powerSupplyOperationalState = mibBuilder.importSymbols("ASCEND-POWER-SUPPLY-MIB", "powerSupplyState", "powerSupplyOperationalState")
radAuthServerIndex, radAuthHostIPAddress = mibBuilder.importSymbols("ASCEND-RADIUS-MIB", "radAuthServerIndex", "radAuthHostIPAddress")
resourceBadCounts, resourceSlotIndex, resourceLast32, resourceUsedCounts, resourcePortIndex = mibBuilder.importSymbols("ASCEND-RESOURCES-MIB", "resourceBadCounts", "resourceSlotIndex", "resourceLast32", "resourceUsedCounts", "resourcePortIndex")
ssnStatusUserIPAddress, = mibBuilder.importSymbols("ASCEND-SESSION-MIB", "ssnStatusUserIPAddress")
sparingSlotLastStatusChange, sparingIfLastStatusChange, sparingSlotStatus, sparingSlotLastChangeReason, sparingSlotSparingIndex, sparingIfPrimaryIndex, sparingIfLastChangeReason, sparingIfStatus, sparingSlotPrimaryIndex, sparingIfSparingIndex = mibBuilder.importSymbols("ASCEND-SPARING-MIB", "sparingSlotLastStatusChange", "sparingIfLastStatusChange", "sparingSlotStatus", "sparingSlotLastChangeReason", "sparingSlotSparingIndex", "sparingIfPrimaryIndex", "sparingIfLastChangeReason", "sparingIfStatus", "sparingSlotPrimaryIndex", "sparingIfSparingIndex")
voipCfgGkIndex, voipCfgGkIpAddress = mibBuilder.importSymbols("ASCEND-VOIP-MIB", "voipCfgGkIndex", "voipCfgGkIpAddress")
watchdogIndex, watchdogState, watchdogName = mibBuilder.importSymbols("ASCEND-WATCHDOG-MIB", "watchdogIndex", "watchdogState", "watchdogName")
ObjectIdentifier, Integer, OctetString = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "Integer", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ConstraintsUnion, ValueRangeConstraint, SingleValueConstraint, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ConstraintsUnion", "ValueRangeConstraint", "SingleValueConstraint", "ValueSizeConstraint")
ifIndex, = mibBuilder.importSymbols("IF-MIB", "ifIndex")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
sysUpTime, sysName = mibBuilder.importSymbols("SNMPv2-MIB", "sysUpTime", "sysName")
TimeTicks, Counter64, NotificationType, Bits, Gauge32, ModuleIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, MibIdentifier, ObjectIdentity, Unsigned32, Integer32, Counter32, NotificationType, IpAddress, iso = mibBuilder.importSymbols("SNMPv2-SMI", "TimeTicks", "Counter64", "NotificationType", "Bits", "Gauge32", "ModuleIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "MibIdentifier", "ObjectIdentity", "Unsigned32", "Integer32", "Counter32", "NotificationType", "IpAddress", "iso")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
portInactive = NotificationType((1, 3, 6, 1, 4, 1, 529) + (0,0)).setObjects(("IF-MIB", "ifIndex"))
portDualDelay = NotificationType((1, 3, 6, 1, 4, 1, 529) + (0,1)).setObjects(("IF-MIB", "ifIndex"))
portWaitSerial = NotificationType((1, 3, 6, 1, 4, 1, 529) + (0,2)).setObjects(("IF-MIB", "ifIndex"))
portHaveSerial = NotificationType((1, 3, 6, 1, 4, 1, 529) + (0,3)).setObjects(("IF-MIB", "ifIndex"))
portRinging = NotificationType((1, 3, 6, 1, 4, 1, 529) + (0,4)).setObjects(("IF-MIB", "ifIndex"))
portCollectDigits = NotificationType((1, 3, 6, 1, 4, 1, 529) + (0,5)).setObjects(("IF-MIB", "ifIndex"))
portWaiting = NotificationType((1, 3, 6, 1, 4, 1, 529) + (0,6)).setObjects(("IF-MIB", "ifIndex"))
portConnected = NotificationType((1, 3, 6, 1, 4, 1, 529) + (0,7)).setObjects(("IF-MIB", "ifIndex"))
portCarrier = NotificationType((1, 3, 6, 1, 4, 1, 529) + (0,8)).setObjects(("IF-MIB", "ifIndex"))
portLoopback = NotificationType((1, 3, 6, 1, 4, 1, 529) + (0,9)).setObjects(("IF-MIB", "ifIndex"))
portAcrPending = NotificationType((1, 3, 6, 1, 4, 1, 529) + (0,10)).setObjects(("IF-MIB", "ifIndex"))
portDteNotReady = NotificationType((1, 3, 6, 1, 4, 1, 529) + (0,11)).setObjects(("IF-MIB", "ifIndex"))
consoleStateChange = NotificationType((1, 3, 6, 1, 4, 1, 529) + (0,12)).setObjects(("ASCEND-MIB", "consoleIndex"), ("ASCEND-SESSION-MIB", "ssnStatusUserIPAddress"))
portUseExceeded = NotificationType((1, 3, 6, 1, 4, 1, 529) + (0,13)).setObjects(("IF-MIB", "ifIndex"))
systemUseExceeded = NotificationType((1, 3, 6, 1, 4, 1, 529) + (0,14))
maxTelnetAttempts = NotificationType((1, 3, 6, 1, 4, 1, 529) + (0,15)).setObjects(("ASCEND-SESSION-MIB", "ssnStatusUserIPAddress"))
eventTableOverwrite = NotificationType((1, 3, 6, 1, 4, 1, 529) + (0,16))
radiusServerChange = NotificationType((1, 3, 6, 1, 4, 1, 529) + (0,18)).setObjects(("ASCEND-RADIUS-MIB", "radAuthServerIndex"), ("ASCEND-RADIUS-MIB", "radAuthHostIPAddress"))
multicastHeartBeatMonitor = NotificationType((1, 3, 6, 1, 4, 1, 529) + (0,19)).setObjects(("ASCEND-MCAST-MIB", "heartBeatMulticastGroupAddress"), ("ASCEND-MCAST-MIB", "heartBeatSourceAddress"), ("ASCEND-MCAST-MIB", "heartBeatSlotTimeInterval"), ("ASCEND-MCAST-MIB", "heartBeatSlotCount"), ("ASCEND-MCAST-MIB", "heartBeatPacketCount"))
lanModemMovedToSuspectList = NotificationType((1, 3, 6, 1, 4, 1, 529) + (0,20)).setObjects(("ASCEND-LANMODEM-MIB", "suspectLanModemSlotIndex"), ("ASCEND-LANMODEM-MIB", "suspectLanModemPortIndex"), ("ASCEND-LANMODEM-MIB", "suspectLanModemUsedCount"), ("ASCEND-LANMODEM-MIB", "suspectLanModemBadCount"), ("ASCEND-LANMODEM-MIB", "suspectLanModemLast32"))
dirdoListFailure = NotificationType((1, 3, 6, 1, 4, 1, 529) + (0,21)).setObjects(("SNMPv2-MIB", "sysName"))
sysSlotStateChange = NotificationType((1, 3, 6, 1, 4, 1, 529) + (0,22)).setObjects(("ASCEND-CHASSIS-MIB", "slotIndex"), ("ASCEND-CHASSIS-MIB", "slotStatus"))
powerSupplyStateChange = NotificationType((1, 3, 6, 1, 4, 1, 529) + (0,23)).setObjects(("ASCEND-POWER-SUPPLY-MIB", "powerSupplyState"))
powerSupplyOperationalStateChange = NotificationType((1, 3, 6, 1, 4, 1, 529) + (0,24)).setObjects(("ASCEND-POWER-SUPPLY-MIB", "powerSupplyOperationalState"))
multiShelfStateChange = NotificationType((1, 3, 6, 1, 4, 1, 529) + (0,25)).setObjects(("ASCEND-MULTI-SHELF-MIB", "multiShelfState"))
sysLastRestartReasonTrap = NotificationType((1, 3, 6, 1, 4, 1, 529) + (0,26)).setObjects(("ASCEND-MIB", "sysLastRestartReason"), ("ASCEND-MIB", "fatalLogIndex"), ("ASCEND-MIB", "sysAbsoluteCurrentTime"))
atmpMaxTunnelExceeded = NotificationType((1, 3, 6, 1, 4, 1, 529) + (0,27)).setObjects(("ASCEND-ATMP-MIB", "atmpHNProfileName"))
atmpAgentErrorSentTrap = NotificationType((1, 3, 6, 1, 4, 1, 529) + (0,28)).setObjects(("ASCEND-ATMP-MIB", "atmpLastErrorGenerated"), ("ASCEND-ATMP-MIB", "atmpAgentSentErrorTo"))
atmpAgentErrorRecvTrap = NotificationType((1, 3, 6, 1, 4, 1, 529) + (0,29)).setObjects(("ASCEND-ATMP-MIB", "atmpLastErrorRecv"), ("ASCEND-ATMP-MIB", "atmpAgentRecvErrorFrom"))
sysConfigChangeTrap = NotificationType((1, 3, 6, 1, 4, 1, 529) + (0,30)).setObjects(("ASCEND-MIB", "sysConfigChange"))
sdtnPrimaryListEmptyTrap = NotificationType((1, 3, 6, 1, 4, 1, 529) + (0,31))
sdtnSecondaryListEmptyTrap = NotificationType((1, 3, 6, 1, 4, 1, 529) + (0,32))
systemClockDrifted = NotificationType((1, 3, 6, 1, 4, 1, 529) + (0,33))
suspectAccessResource = NotificationType((1, 3, 6, 1, 4, 1, 529) + (0,34)).setObjects(("ASCEND-RESOURCES-MIB", "resourceSlotIndex"), ("ASCEND-RESOURCES-MIB", "resourcePortIndex"), ("ASCEND-RESOURCES-MIB", "resourceUsedCounts"), ("ASCEND-RESOURCES-MIB", "resourceBadCounts"), ("ASCEND-RESOURCES-MIB", "resourceLast32"))
watchdogWarningTrap = NotificationType((1, 3, 6, 1, 4, 1, 529) + (0,35)).setObjects(("ASCEND-WATCHDOG-MIB", "watchdogIndex"), ("ASCEND-WATCHDOG-MIB", "watchdogName"), ("ASCEND-WATCHDOG-MIB", "watchdogState"), ("ASCEND-MIB", "sysAbsoluteCurrentTime"))
slotCardResetTrap = NotificationType((1, 3, 6, 1, 4, 1, 529) + (0,36)).setObjects(("ASCEND-MIB", "fatalLogIndex"), ("ASCEND-MIB", "fatalLogReason"), ("ASCEND-MIB", "sysAbsoluteCurrentTime"), ("ASCEND-CHASSIS-MIB", "slotIndex"))
controllerSwitchoverTrap = NotificationType((1, 3, 6, 1, 4, 1, 529) + (0,37)).setObjects(("ASCEND-MIB", "sysAbsoluteCurrentTime"), ("ASCEND-CHASSIS-MIB", "cntrReduSwitchReason"), ("ASCEND-CHASSIS-MIB", "cntrReduSwitchIndex"), ("ASCEND-CHASSIS-MIB", "cntrReduCurrentIndex"))
callLogServChange = NotificationType((1, 3, 6, 1, 4, 1, 529) + (0,38)).setObjects(("ASCEND-CALL-LOGGING-MIB", "callLoggingServerIndex"), ("ASCEND-CALL-LOGGING-MIB", "callLoggingServerIPAddress"), ("ASCEND-MIB", "sysAbsoluteCurrentTime"))
voipGkChange = NotificationType((1, 3, 6, 1, 4, 1, 529) + (0,39)).setObjects(("ASCEND-VOIP-MIB", "voipCfgGkIndex"), ("ASCEND-VOIP-MIB", "voipCfgGkIpAddress"), ("ASCEND-MIB", "sysAbsoluteCurrentTime"))
wanLineStateChange = NotificationType((1, 3, 6, 1, 4, 1, 529) + (0,40)).setObjects(("ASCEND-ADVANCED-AGENT-MIB", "wanLineIfIndex"), ("ASCEND-ADVANCED-AGENT-MIB", "wanLineUsage"), ("ASCEND-MIB", "sysAbsoluteCurrentTime"))
callLogDroppedPkt = NotificationType((1, 3, 6, 1, 4, 1, 529) + (0,41)).setObjects(("ASCEND-CALL-LOGGING-MIB", "callLoggingDroppedPacketCount"))
megacoLinkStatusTrap = NotificationType((1, 3, 6, 1, 4, 1, 529) + (0,42)).setObjects(("ASCEND-MGSTAT-MIB", "mgLinkName"), ("ASCEND-MGSTAT-MIB", "mgOperStatus"))
sparingSlotStatusChange = NotificationType((1, 3, 6, 1, 4, 1, 529) + (0,43)).setObjects(("ASCEND-SPARING-MIB", "sparingSlotPrimaryIndex"), ("ASCEND-SPARING-MIB", "sparingSlotSparingIndex"), ("ASCEND-SPARING-MIB", "sparingSlotStatus"), ("ASCEND-SPARING-MIB", "sparingSlotLastStatusChange"), ("ASCEND-SPARING-MIB", "sparingSlotLastChangeReason"))
sparingIfStatusChange = NotificationType((1, 3, 6, 1, 4, 1, 529) + (0,44)).setObjects(("ASCEND-SPARING-MIB", "sparingIfPrimaryIndex"), ("ASCEND-SPARING-MIB", "sparingIfSparingIndex"), ("ASCEND-SPARING-MIB", "sparingIfStatus"), ("ASCEND-SPARING-MIB", "sparingIfLastStatusChange"), ("ASCEND-SPARING-MIB", "sparingIfLastChangeReason"))
cntrReduAvailTrap = NotificationType((1, 3, 6, 1, 4, 1, 529) + (0,45)).setObjects(("ASCEND-CHASSIS-MIB", "cntrReduAvailLastTime"), ("ASCEND-CHASSIS-MIB", "cntrReduAvailSlotIndex"), ("ASCEND-CHASSIS-MIB", "cntrReduAvailPrevState"), ("ASCEND-CHASSIS-MIB", "cntrReduAvailCurrState"))
mibBuilder.exportSymbols("ASCEND-TRAP", eventTableOverwrite=eventTableOverwrite, multiShelfStateChange=multiShelfStateChange, sparingIfStatusChange=sparingIfStatusChange, systemClockDrifted=systemClockDrifted, sysConfigChangeTrap=sysConfigChangeTrap, callLogServChange=callLogServChange, voipGkChange=voipGkChange, sysSlotStateChange=sysSlotStateChange, sdtnSecondaryListEmptyTrap=sdtnSecondaryListEmptyTrap, watchdogWarningTrap=watchdogWarningTrap, megacoLinkStatusTrap=megacoLinkStatusTrap, consoleStateChange=consoleStateChange, cntrReduAvailTrap=cntrReduAvailTrap, slotCardResetTrap=slotCardResetTrap, sysLastRestartReasonTrap=sysLastRestartReasonTrap, suspectAccessResource=suspectAccessResource, portCarrier=portCarrier, sparingSlotStatusChange=sparingSlotStatusChange, sdtnPrimaryListEmptyTrap=sdtnPrimaryListEmptyTrap, controllerSwitchoverTrap=controllerSwitchoverTrap, lanModemMovedToSuspectList=lanModemMovedToSuspectList, powerSupplyStateChange=powerSupplyStateChange, multicastHeartBeatMonitor=multicastHeartBeatMonitor, portHaveSerial=portHaveSerial, portWaitSerial=portWaitSerial, atmpAgentErrorSentTrap=atmpAgentErrorSentTrap, portUseExceeded=portUseExceeded, portWaiting=portWaiting, powerSupplyOperationalStateChange=powerSupplyOperationalStateChange, portCollectDigits=portCollectDigits, portRinging=portRinging, portAcrPending=portAcrPending, atmpMaxTunnelExceeded=atmpMaxTunnelExceeded, portConnected=portConnected, wanLineStateChange=wanLineStateChange, portDualDelay=portDualDelay, systemUseExceeded=systemUseExceeded, portInactive=portInactive, callLogDroppedPkt=callLogDroppedPkt, atmpAgentErrorRecvTrap=atmpAgentErrorRecvTrap, radiusServerChange=radiusServerChange, portLoopback=portLoopback, portDteNotReady=portDteNotReady, dirdoListFailure=dirdoListFailure, maxTelnetAttempts=maxTelnetAttempts)