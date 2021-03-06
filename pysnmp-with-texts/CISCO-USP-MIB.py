#
# PySNMP MIB module CISCO-USP-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/CISCO-USP-MIB
# Produced by pysmi-0.3.4 at Wed May  1 12:18:05 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
SingleValueConstraint, ConstraintsIntersection, ValueSizeConstraint, ConstraintsUnion, ValueRangeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "SingleValueConstraint", "ConstraintsIntersection", "ValueSizeConstraint", "ConstraintsUnion", "ValueRangeConstraint")
ciscoMgmt, = mibBuilder.importSymbols("CISCO-SMI", "ciscoMgmt")
ObjectGroup, NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "ObjectGroup", "NotificationGroup", "ModuleCompliance")
ObjectIdentity, iso, Unsigned32, MibIdentifier, ModuleIdentity, TimeTicks, Integer32, Counter64, Bits, MibScalar, MibTable, MibTableRow, MibTableColumn, IpAddress, NotificationType, Gauge32, Counter32 = mibBuilder.importSymbols("SNMPv2-SMI", "ObjectIdentity", "iso", "Unsigned32", "MibIdentifier", "ModuleIdentity", "TimeTicks", "Integer32", "Counter64", "Bits", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "IpAddress", "NotificationType", "Gauge32", "Counter32")
TruthValue, TextualConvention, DateAndTime, TimeStamp, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TruthValue", "TextualConvention", "DateAndTime", "TimeStamp", "DisplayString")
ciscoUspMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 9, 827))
ciscoUspMIB.setRevisions(('2015-07-20 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: ciscoUspMIB.setRevisionsDescriptions(('First version of this MIB module.',))
if mibBuilder.loadTexts: ciscoUspMIB.setLastUpdated('201507200000Z')
if mibBuilder.loadTexts: ciscoUspMIB.setOrganization('Cisco Systems, Inc.')
if mibBuilder.loadTexts: ciscoUspMIB.setContactInfo('Cisco Systems Customer Service Postal: 170 W Tasman Drive San Jose, CA 95134 USA Tel: +1 800 553-NETS E-mail: cs-cusp@cisco.com')
if mibBuilder.loadTexts: ciscoUspMIB.setDescription("The MIB Module for the management of the Cisco Unified SIP Proxy (CUSP) service. CUSP is a Session Initiation Protocol (SIP) proxy server that helps enterprises aggregate their SIP elements into a centralized architecture in order to simplify and improve the flexibility of their network. MIB has OID's to monitor CUSP specific info like Server Group, Calls Per Second (CPS), Total Calls, Failed Calls, Dropped Calls, License, Up time CPU and Memory info and also traps on Server group elements, CPU and Memory threshold exceed, License exceed, Back up , process going down, Extensive logging and connection.")
ciscoUspMIBNotifs = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 827, 0))
cuspSystemStateAlert = NotificationType((1, 3, 6, 1, 4, 1, 9, 9, 827, 0, 1)).setObjects(("CISCO-USP-MIB", "cuspNotifSeverity"), ("CISCO-USP-MIB", "cuspNotifDetail"), ("CISCO-USP-MIB", "cuspSystemState"))
if mibBuilder.loadTexts: cuspSystemStateAlert.setStatus('current')
if mibBuilder.loadTexts: cuspSystemStateAlert.setDescription('This notification is generated when the CUSP system goes up/down. This notification can be enabled/disabled by setting cuspSystemStateAlertEnable.')
cuspServerGroupElementAlert = NotificationType((1, 3, 6, 1, 4, 1, 9, 9, 827, 0, 2)).setObjects(("CISCO-USP-MIB", "cuspNotifSeverity"), ("CISCO-USP-MIB", "cuspElementName"), ("CISCO-USP-MIB", "cuspElementStatus"))
if mibBuilder.loadTexts: cuspServerGroupElementAlert.setStatus('current')
if mibBuilder.loadTexts: cuspServerGroupElementAlert.setDescription('This notification is generated when server group element status changes. This notification can be enabled/disabled by setting cuspServerGroupElementAlertEnable.')
cuspServerGroupAlert = NotificationType((1, 3, 6, 1, 4, 1, 9, 9, 827, 0, 3)).setObjects(("CISCO-USP-MIB", "cuspNotifSeverity"), ("CISCO-USP-MIB", "cuspServerGroupName"), ("CISCO-USP-MIB", "cuspServerGroupStatus"))
if mibBuilder.loadTexts: cuspServerGroupAlert.setStatus('current')
if mibBuilder.loadTexts: cuspServerGroupAlert.setDescription('This notification is generated when all the elements in the server group goes down or when any one element in the server group comes up after all the elements in the group were down. This notification can be enabled/disabled by setting cuspServerGroupAlertEnable.')
cuspMemoryThresholdAlert = NotificationType((1, 3, 6, 1, 4, 1, 9, 9, 827, 0, 4)).setObjects(("CISCO-USP-MIB", "cuspNotifSeverity"), ("CISCO-USP-MIB", "cuspMemoryThresholdValue"), ("CISCO-USP-MIB", "cuspConfiguredMemory"), ("CISCO-USP-MIB", "cuspMemoryUsed"))
if mibBuilder.loadTexts: cuspMemoryThresholdAlert.setStatus('current')
if mibBuilder.loadTexts: cuspMemoryThresholdAlert.setDescription('This notification is generated when CUSP memory usage exceeds the cuspMemoryThresholdValue. This notification can be enabled/disabled by setting cuspMemoryThresholdAlertEnable.')
cuspLicenseExceededAlert = NotificationType((1, 3, 6, 1, 4, 1, 9, 9, 827, 0, 5)).setObjects(("CISCO-USP-MIB", "cuspNotifSeverity"), ("CISCO-USP-MIB", "cuspCPS"), ("CISCO-USP-MIB", "cuspLicenseLimit"))
if mibBuilder.loadTexts: cuspLicenseExceededAlert.setStatus('current')
if mibBuilder.loadTexts: cuspLicenseExceededAlert.setDescription('This notification is generated when average CPS exceeds cuspLicenseLimit. This notification can be enabled/disabled by setting cuspLicenseExceededAlertEnable.')
cuspLicenseStateAlert = NotificationType((1, 3, 6, 1, 4, 1, 9, 9, 827, 0, 6)).setObjects(("CISCO-USP-MIB", "cuspNotifSeverity"), ("CISCO-USP-MIB", "cuspLicenseState"))
if mibBuilder.loadTexts: cuspLicenseStateAlert.setStatus('current')
if mibBuilder.loadTexts: cuspLicenseStateAlert.setDescription('This notification is generated when CUSP license state changes. This notification can be enabled/disabled by setting cuspLicenseStateAlertEnable.')
cuspExtensiveLoggingAlert = NotificationType((1, 3, 6, 1, 4, 1, 9, 9, 827, 0, 7)).setObjects(("CISCO-USP-MIB", "cuspNotifSeverity"), ("CISCO-USP-MIB", "cuspNotifDetail"))
if mibBuilder.loadTexts: cuspExtensiveLoggingAlert.setStatus('current')
if mibBuilder.loadTexts: cuspExtensiveLoggingAlert.setDescription('This notification is generated when extensive debug level logging is enabled in CUSP. Extensive logging might impact the performance and system stability. This notification can be enabled/disabled by setting cuspExtensiveLoggingAlertEnable.')
cuspDiskSpaceThresholdAlert = NotificationType((1, 3, 6, 1, 4, 1, 9, 9, 827, 0, 8)).setObjects(("CISCO-USP-MIB", "cuspNotifSeverity"), ("CISCO-USP-MIB", "cuspDiskSpaceThresholdValue"), ("CISCO-USP-MIB", "cuspDiskSpaceUsed"))
if mibBuilder.loadTexts: cuspDiskSpaceThresholdAlert.setStatus('current')
if mibBuilder.loadTexts: cuspDiskSpaceThresholdAlert.setDescription('This notification is generated when the CUSP Disk usage exceeds the cuspDiskSpaceThresholdValue. This notification can be enabled/disabled by setting cuspDiskSpaceThresholdAlertEnable.')
cuspBackupProcessFailAlert = NotificationType((1, 3, 6, 1, 4, 1, 9, 9, 827, 0, 9)).setObjects(("CISCO-USP-MIB", "cuspNotifSeverity"), ("CISCO-USP-MIB", "cuspNotifDetail"))
if mibBuilder.loadTexts: cuspBackupProcessFailAlert.setStatus('current')
if mibBuilder.loadTexts: cuspBackupProcessFailAlert.setDescription('This notification is generated when back up process fails. This notification can be enabled/disabled by setting cuspBackupProcessFailAlertEnable.')
cuspConnectionExceptionAlert = NotificationType((1, 3, 6, 1, 4, 1, 9, 9, 827, 0, 10)).setObjects(("CISCO-USP-MIB", "cuspNotifSeverity"), ("CISCO-USP-MIB", "cuspNotifDetail"))
if mibBuilder.loadTexts: cuspConnectionExceptionAlert.setStatus('current')
if mibBuilder.loadTexts: cuspConnectionExceptionAlert.setDescription('This notification is generated when a connection exception occurs. This notification can be enabled/disabled by setting cuspConnectionExceptionAlertEnable.')
ciscoUspMIBObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 827, 1))
ciscoUspMIBConform = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 827, 2))
cuspScalar = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 827, 1, 1))
cuspTable = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 827, 1, 2))
ciscoUspMIBCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 827, 2, 1))
ciscoUspMIBGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 827, 2, 2))
ciscoUspMIBModuleCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 9, 9, 827, 2, 1, 1)).setObjects(("CISCO-USP-MIB", "ciscoUspMIBMainObjectGroup"), ("CISCO-USP-MIB", "ciscoUspMIBNotifyGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoUspMIBModuleCompliance = ciscoUspMIBModuleCompliance.setStatus('current')
if mibBuilder.loadTexts: ciscoUspMIBModuleCompliance.setDescription('The compliance statement for entities which implement the Cisco USP MIB.')
ciscoUspMIBMainObjectGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 827, 2, 2, 1)).setObjects(("CISCO-USP-MIB", "cuspLicenseLimit"), ("CISCO-USP-MIB", "cuspLastCounterResetTime"), ("CISCO-USP-MIB", "cuspTotalCalls"), ("CISCO-USP-MIB", "cuspTotalFailedCalls"), ("CISCO-USP-MIB", "cuspCPS"), ("CISCO-USP-MIB", "cuspAvgCPSOneMin"), ("CISCO-USP-MIB", "cuspMaxCPSOneMin"), ("CISCO-USP-MIB", "cuspDroppedCallsOneSec"), ("CISCO-USP-MIB", "cuspAvgDroppedCPSOneMin"), ("CISCO-USP-MIB", "cuspMaxDroppedCPSOneMin"), ("CISCO-USP-MIB", "cuspCallsRoutedOneSec"), ("CISCO-USP-MIB", "cuspAvgCallsRoutedOneMin"), ("CISCO-USP-MIB", "cuspMaxCallsRoutedOneMin"), ("CISCO-USP-MIB", "cuspCallsDroppedExceedingLicense"), ("CISCO-USP-MIB", "cuspSystemState"), ("CISCO-USP-MIB", "cuspSystemUpTime"), ("CISCO-USP-MIB", "cuspNoOfMessagesRecieved"), ("CISCO-USP-MIB", "cuspSmartAgentState"), ("CISCO-USP-MIB", "cuspStrayMessageCount"), ("CISCO-USP-MIB", "cuspConfiguredMemory"), ("CISCO-USP-MIB", "cuspMemoryUsed"), ("CISCO-USP-MIB", "cuspSystemStateAlertEnable"), ("CISCO-USP-MIB", "cuspServerGroupAlertEnable"), ("CISCO-USP-MIB", "cuspDiskSpaceThresholdAlertEnable"), ("CISCO-USP-MIB", "cuspBackupProcessFailAlertEnable"), ("CISCO-USP-MIB", "cuspExtensiveLoggingAlertEnable"), ("CISCO-USP-MIB", "cuspMemoryThresholdValue"), ("CISCO-USP-MIB", "cuspDiskSpaceThresholdValue"), ("CISCO-USP-MIB", "cuspServerGroupName"), ("CISCO-USP-MIB", "cuspServerGroupNetwork"), ("CISCO-USP-MIB", "cuspServerGroupStatus"), ("CISCO-USP-MIB", "cuspElementName"), ("CISCO-USP-MIB", "cuspElementStatus"), ("CISCO-USP-MIB", "cuspElementQValue"), ("CISCO-USP-MIB", "cuspElementWeight"), ("CISCO-USP-MIB", "cuspElementTransport"), ("CISCO-USP-MIB", "cuspElementTotalCalls"), ("CISCO-USP-MIB", "cuspElementFailedCalls"), ("CISCO-USP-MIB", "cuspNotifSeverity"), ("CISCO-USP-MIB", "cuspNotifDetail"), ("CISCO-USP-MIB", "cuspLicenseExceededAlertEnable"), ("CISCO-USP-MIB", "cuspServerGroupPingStatus"), ("CISCO-USP-MIB", "cuspServerGroupLBType"), ("CISCO-USP-MIB", "cuspDiskSpaceUsed"), ("CISCO-USP-MIB", "cuspElementPort"), ("CISCO-USP-MIB", "cuspServerGroupElementAlertEnable"), ("CISCO-USP-MIB", "cuspLicenseStateAlertEnable"), ("CISCO-USP-MIB", "cuspMemoryThresholdAlertEnable"), ("CISCO-USP-MIB", "cuspConnectionExceptionAlertEnable"), ("CISCO-USP-MIB", "cuspLicenseState"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoUspMIBMainObjectGroup = ciscoUspMIBMainObjectGroup.setStatus('current')
if mibBuilder.loadTexts: ciscoUspMIBMainObjectGroup.setDescription('A collection of objects providing information on CUSP system parameters.')
ciscoUspMIBNotifyGroup = NotificationGroup((1, 3, 6, 1, 4, 1, 9, 9, 827, 2, 2, 2)).setObjects(("CISCO-USP-MIB", "cuspSystemStateAlert"), ("CISCO-USP-MIB", "cuspBackupProcessFailAlert"), ("CISCO-USP-MIB", "cuspDiskSpaceThresholdAlert"), ("CISCO-USP-MIB", "cuspConnectionExceptionAlert"), ("CISCO-USP-MIB", "cuspServerGroupElementAlert"), ("CISCO-USP-MIB", "cuspServerGroupAlert"), ("CISCO-USP-MIB", "cuspMemoryThresholdAlert"), ("CISCO-USP-MIB", "cuspLicenseExceededAlert"), ("CISCO-USP-MIB", "cuspExtensiveLoggingAlert"), ("CISCO-USP-MIB", "cuspLicenseStateAlert"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoUspMIBNotifyGroup = ciscoUspMIBNotifyGroup.setStatus('current')
if mibBuilder.loadTexts: ciscoUspMIBNotifyGroup.setDescription('A collection of notifications that are generated by the CUSP.')
cuspNotifControlInfo = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 827, 1, 3))
cuspLastCounterResetTime = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 827, 1, 1, 1), DateAndTime()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cuspLastCounterResetTime.setStatus('current')
if mibBuilder.loadTexts: cuspLastCounterResetTime.setDescription('This object gives the time stamp in date and time when the call counter was last reset. All counters related to calls, CPS and messages would be reset when counter is reset.')
cuspSystemState = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 827, 1, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("up", 1), ("down", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: cuspSystemState.setStatus('current')
if mibBuilder.loadTexts: cuspSystemState.setDescription("This object gives the CUSP system state. 'up' - System is up. 'down' - System is either offline or going down.")
cuspSystemUpTime = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 827, 1, 1, 3), TimeStamp()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cuspSystemUpTime.setStatus('current')
if mibBuilder.loadTexts: cuspSystemUpTime.setDescription('This object gives the CUSP system up time information.')
cuspLicenseLimit = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 827, 1, 1, 4), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(0, 10000))).setUnits('CPS').setMaxAccess("readonly")
if mibBuilder.loadTexts: cuspLicenseLimit.setStatus('current')
if mibBuilder.loadTexts: cuspLicenseLimit.setDescription('This object gives the maximum licensed CPS limit value. Calls will be rejected if the license limit is exceeded.')
cuspLicenseState = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 827, 1, 1, 5), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12))).clone(namedValues=NamedValues(("waiting", 1), ("overage", 2), ("outofcompliance", 3), ("notapplicable", 4), ("invalidtag", 5), ("invalid", 6), ("init", 7), ("incompliance", 8), ("evalexpired", 9), ("eval", 10), ("disabled", 11), ("authorizedperiodexpired", 12)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: cuspLicenseState.setStatus('current')
if mibBuilder.loadTexts: cuspLicenseState.setDescription("This object gives the current license state of the CUSP. 'waiting' - The initial state after an entitlement request while waiting for the authorization request response. 'overage' - The entitlement is in overage. 'outofcompliance' - Requested entitlement is more than the available count. All calls will be rejected. 'notapplicable' - Enforcement mode is not applicable. 'invalidtag' - The entitlement tag is invalid. 'invalid' - Error condition state. 'init' - The initial state after the instance is created but before the entitlement is requested with. 'incompliance' - License registration and entitlement succeeded. 'evalexpired' - Evaluation period has expired. 'eval' - CUSP is using the evaluation period for this entitlement. 'disabled' - Smart Licensing has been deactivated or disabled. 'authorizedperiodexpired' - The authorized period has expired.")
cuspSmartAgentState = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 827, 1, 1, 6), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 8))).clone(namedValues=NamedValues(("unconfigured", 1), ("unidentified", 2), ("evalexpired", 3), ("registered", 4), ("outofcomplaince", 5), ("authorized", 6), ("authorizationexpiry", 7), ("transient", 8)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: cuspSmartAgentState.setStatus('current')
if mibBuilder.loadTexts: cuspSmartAgentState.setDescription("This object gives the current license state of the Smart License Agent. 'unconfigured' - Smart licensing agent is not enabled and and all calls will be rejected in this state. 'unidentified' - Smart licensing is enabled and entitlement information is sent to the agent. Calls will be allowed in this state. 'evalexpired' - Smart agent will move to this state when evaluation period expires. All calls will be rejected in this state. 'transient' - Smart agent is in transient state. 'registered' - CUSP registered with the cloud server but license not yet authorized. 'outofcompliance' - Requested entitlement is more than the available count. All calls will be rejected. 'authorized' - License registration and entitlement succeeded. 'authorizationexpiry' - Renew request failed for more than 90 days. All calls will be rejected.")
cuspConfiguredMemory = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 827, 1, 1, 7), Unsigned32()).setUnits('MegaByte').setMaxAccess("readonly")
if mibBuilder.loadTexts: cuspConfiguredMemory.setStatus('current')
if mibBuilder.loadTexts: cuspConfiguredMemory.setDescription('This object gives the total memory (RAM) in MB(MegaByte) configured on CUSP.')
cuspMemoryUsed = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 827, 1, 1, 8), Unsigned32()).setUnits('MegaByte').setMaxAccess("readonly")
if mibBuilder.loadTexts: cuspMemoryUsed.setStatus('current')
if mibBuilder.loadTexts: cuspMemoryUsed.setDescription('This object gives the CUSP current memory (RAM) usage information in MB (MegaByte).')
cuspDiskSpaceUsed = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 827, 1, 1, 9), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cuspDiskSpaceUsed.setStatus('current')
if mibBuilder.loadTexts: cuspDiskSpaceUsed.setDescription('This object gives the current disk utilization of CUSP in MB (Mega Byte).')
cuspCallStats = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 827, 1, 1, 10))
cuspMessageStats = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 827, 1, 1, 11))
cuspThresholdValues = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 827, 1, 1, 12))
cuspTotalCalls = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 827, 1, 1, 10, 1), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cuspTotalCalls.setStatus('current')
if mibBuilder.loadTexts: cuspTotalCalls.setDescription('This object gives the total number of calls since the last counter reset.')
cuspTotalFailedCalls = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 827, 1, 1, 10, 2), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cuspTotalFailedCalls.setStatus('current')
if mibBuilder.loadTexts: cuspTotalFailedCalls.setDescription('This object gives the total number of failed calls since last counter reset.')
cuspCPS = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 827, 1, 1, 10, 3), Unsigned32()).setUnits('CPS').setMaxAccess("readonly")
if mibBuilder.loadTexts: cuspCPS.setStatus('current')
if mibBuilder.loadTexts: cuspCPS.setDescription('This object gives the current running Calls Per Second (CPS) information.')
cuspAvgCPSOneMin = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 827, 1, 1, 10, 4), Unsigned32()).setUnits('CPS').setMaxAccess("readonly")
if mibBuilder.loadTexts: cuspAvgCPSOneMin.setStatus('current')
if mibBuilder.loadTexts: cuspAvgCPSOneMin.setDescription('This object gives the average CPS (Calls Per Second) in the last one minute.')
cuspMaxCPSOneMin = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 827, 1, 1, 10, 5), Unsigned32()).setUnits('CPS').setMaxAccess("readonly")
if mibBuilder.loadTexts: cuspMaxCPSOneMin.setStatus('current')
if mibBuilder.loadTexts: cuspMaxCPSOneMin.setDescription('This object gives the Maximum value of CPS (Calls Per Second) in the last one minute.')
cuspDroppedCallsOneSec = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 827, 1, 1, 10, 6), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cuspDroppedCallsOneSec.setStatus('current')
if mibBuilder.loadTexts: cuspDroppedCallsOneSec.setDescription('This object gives the count on number of calls dropped in the last one second.')
cuspAvgDroppedCPSOneMin = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 827, 1, 1, 10, 7), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cuspAvgDroppedCPSOneMin.setStatus('current')
if mibBuilder.loadTexts: cuspAvgDroppedCPSOneMin.setDescription("This object gives the average of 'dropped calls per second' in the last one minute.")
cuspMaxDroppedCPSOneMin = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 827, 1, 1, 10, 8), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cuspMaxDroppedCPSOneMin.setStatus('current')
if mibBuilder.loadTexts: cuspMaxDroppedCPSOneMin.setDescription("This object gives the Maximum of 'dropped calls per second' in the last one minute.")
cuspCallsRoutedOneSec = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 827, 1, 1, 10, 9), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cuspCallsRoutedOneSec.setStatus('current')
if mibBuilder.loadTexts: cuspCallsRoutedOneSec.setDescription('This object gives the number of calls routed through CUSP in last one second.')
cuspAvgCallsRoutedOneMin = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 827, 1, 1, 10, 10), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cuspAvgCallsRoutedOneMin.setStatus('current')
if mibBuilder.loadTexts: cuspAvgCallsRoutedOneMin.setDescription("This object gives the average of 'calls routed per second' in last one minute.")
cuspMaxCallsRoutedOneMin = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 827, 1, 1, 10, 11), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cuspMaxCallsRoutedOneMin.setStatus('current')
if mibBuilder.loadTexts: cuspMaxCallsRoutedOneMin.setDescription("This object gives the maximum of 'calls routed per second' in the last one minute.")
cuspCallsDroppedExceedingLicense = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 827, 1, 1, 10, 12), Unsigned32()).setUnits('CPS').setMaxAccess("readonly")
if mibBuilder.loadTexts: cuspCallsDroppedExceedingLicense.setStatus('current')
if mibBuilder.loadTexts: cuspCallsDroppedExceedingLicense.setDescription('This object gives the total calls dropped due to exceeding license limit.')
cuspStrayMessageCount = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 827, 1, 1, 11, 1), Unsigned32()).setUnits('Messages').setMaxAccess("readonly")
if mibBuilder.loadTexts: cuspStrayMessageCount.setStatus('current')
if mibBuilder.loadTexts: cuspStrayMessageCount.setDescription("This object gives the number of stray messages information. Stray messages are messages for which CUSP doesn't have a transaction.")
cuspNoOfMessagesRecieved = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 827, 1, 1, 11, 2), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cuspNoOfMessagesRecieved.setStatus('current')
if mibBuilder.loadTexts: cuspNoOfMessagesRecieved.setDescription('This object gives the total number of messages received.')
cuspDiskSpaceThresholdValue = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 827, 1, 1, 12, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 100))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cuspDiskSpaceThresholdValue.setStatus('current')
if mibBuilder.loadTexts: cuspDiskSpaceThresholdValue.setDescription('The percentage threshold value configured by the user. If the percentage disk space utilization exceeds this limit then cuspDiskSpaceThresholdAlert notification is sent.')
cuspMemoryThresholdValue = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 827, 1, 1, 12, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 100))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cuspMemoryThresholdValue.setStatus('current')
if mibBuilder.loadTexts: cuspMemoryThresholdValue.setDescription('The percentage threshold value configured by the user. If the percentage memory utilization exceeds this limit then cuspMemoryThresholdAlert notification is sent.')
cuspServerGroupTable = MibTable((1, 3, 6, 1, 4, 1, 9, 9, 827, 1, 2, 1), )
if mibBuilder.loadTexts: cuspServerGroupTable.setStatus('current')
if mibBuilder.loadTexts: cuspServerGroupTable.setDescription('A list of Server Groups. Server groups define the elements with which the Cisco Unified SIP Proxy system interacts for each network.')
cuspServerGroupEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9, 9, 827, 1, 2, 1, 1), ).setIndexNames((0, "CISCO-USP-MIB", "cuspServerGroupIndex"))
if mibBuilder.loadTexts: cuspServerGroupEntry.setStatus('current')
if mibBuilder.loadTexts: cuspServerGroupEntry.setDescription('An entry (conceptual row) in the ServerGroup Table.')
cuspServerGroupIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 827, 1, 2, 1, 1, 1), Unsigned32())
if mibBuilder.loadTexts: cuspServerGroupIndex.setStatus('current')
if mibBuilder.loadTexts: cuspServerGroupIndex.setDescription('A unique value, greater than zero, for each server group.')
cuspServerGroupName = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 827, 1, 2, 1, 1, 2), OctetString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cuspServerGroupName.setStatus('current')
if mibBuilder.loadTexts: cuspServerGroupName.setDescription('This object gives the name of the server group.')
cuspServerGroupNetwork = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 827, 1, 2, 1, 1, 3), OctetString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cuspServerGroupNetwork.setStatus('current')
if mibBuilder.loadTexts: cuspServerGroupNetwork.setDescription('This object gives the network name to which the server group belongs.')
cuspServerGroupStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 827, 1, 2, 1, 1, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("up", 1), ("partialdown", 2), ("down", 3)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: cuspServerGroupStatus.setStatus('current')
if mibBuilder.loadTexts: cuspServerGroupStatus.setDescription('This object gives the Server group status as up/partialdown/down. up - All the elements in the server group are up. partialdown - At least one element in the server group is down. down - All the elements in the server group are down.')
cuspServerGroupPingStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 827, 1, 2, 1, 1, 5), TruthValue()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cuspServerGroupPingStatus.setStatus('current')
if mibBuilder.loadTexts: cuspServerGroupPingStatus.setDescription('This object gives server group ping status. true - Ping is enabled. false - Ping is disabled.')
cuspServerGroupLBType = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 827, 1, 2, 1, 1, 6), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6))).clone(namedValues=NamedValues(("global", 1), ("highestq", 2), ("requesturi", 3), ("callid", 4), ("touri", 5), ("weight", 6)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: cuspServerGroupLBType.setStatus('current')
if mibBuilder.loadTexts: cuspServerGroupLBType.setDescription('This object gives the load balancing algorithm for the server group. global - Uses global load balance algorithm. highestq - Uses highestq algorithm where in CUSP picks the first available element with the higest q-value. requesturi - Hash algorithm is on Request-URI. callid - Hash algorithm is on Call-ID. touri - Hash algorithm is on To URI. weight - Uses weight-based scheme.')
cuspElementTable = MibTable((1, 3, 6, 1, 4, 1, 9, 9, 827, 1, 2, 2), )
if mibBuilder.loadTexts: cuspElementTable.setStatus('current')
if mibBuilder.loadTexts: cuspElementTable.setDescription('A list of elements in a server group table. Also gives information on status(up/down) of the element, its Q value, weight and transport type.')
cuspElementEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9, 9, 827, 1, 2, 2, 1), ).setIndexNames((0, "CISCO-USP-MIB", "cuspServerGroupIndex"), (0, "CISCO-USP-MIB", "cuspElementIndex"))
if mibBuilder.loadTexts: cuspElementEntry.setStatus('current')
if mibBuilder.loadTexts: cuspElementEntry.setDescription('An entry (conceptual row) in the cuspElementTable.')
cuspElementIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 827, 1, 2, 2, 1, 1), Unsigned32())
if mibBuilder.loadTexts: cuspElementIndex.setStatus('current')
if mibBuilder.loadTexts: cuspElementIndex.setDescription('A unique value, greater than zero, for each element.')
cuspElementName = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 827, 1, 2, 2, 1, 2), OctetString().subtype(subtypeSpec=ValueSizeConstraint(0, 255))).setMaxAccess("readonly")
if mibBuilder.loadTexts: cuspElementName.setStatus('current')
if mibBuilder.loadTexts: cuspElementName.setDescription('This object gives the Server group element ID.')
cuspElementStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 827, 1, 2, 2, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("up", 1), ("down", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: cuspElementStatus.setStatus('current')
if mibBuilder.loadTexts: cuspElementStatus.setDescription("This object gives the server group element status. 'up' - Server group element is up. 'down' - Server group element is down.")
cuspElementQValue = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 827, 1, 2, 2, 1, 4), OctetString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cuspElementQValue.setStatus('current')
if mibBuilder.loadTexts: cuspElementQValue.setDescription('This object gives the Q value of the server group element. Q value is a real number that specifies the priority of the server group element with respect to others in the server group. Q value range is 0.0 to 1.0.')
cuspElementWeight = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 827, 1, 2, 2, 1, 5), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 100))).setMaxAccess("readonly")
if mibBuilder.loadTexts: cuspElementWeight.setStatus('current')
if mibBuilder.loadTexts: cuspElementWeight.setDescription('This object gives the weight of the server group element. Weight is used for load balancing between server group elements.')
cuspElementPort = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 827, 1, 2, 2, 1, 6), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 65535))).setMaxAccess("readonly")
if mibBuilder.loadTexts: cuspElementPort.setStatus('current')
if mibBuilder.loadTexts: cuspElementPort.setDescription('This object gives the port number of the server group element.')
cuspElementTransport = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 827, 1, 2, 2, 1, 7), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("udp", 1), ("tcp", 2), ("tls", 3)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: cuspElementTransport.setStatus('current')
if mibBuilder.loadTexts: cuspElementTransport.setDescription('This object gives the transport type of the server group element. Transport type can be udp,tcp or tls.')
cuspElementTotalCalls = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 827, 1, 2, 2, 1, 8), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cuspElementTotalCalls.setStatus('current')
if mibBuilder.loadTexts: cuspElementTotalCalls.setDescription('This object gives the total routed calls to the server group element.')
cuspElementFailedCalls = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 827, 1, 2, 2, 1, 9), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cuspElementFailedCalls.setStatus('current')
if mibBuilder.loadTexts: cuspElementFailedCalls.setDescription('This object gives the total failed calls on the server group element.')
cuspNotifSeverity = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 827, 1, 3, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("error", 1), ("warning", 2), ("informational", 3)))).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: cuspNotifSeverity.setStatus('current')
if mibBuilder.loadTexts: cuspNotifSeverity.setDescription("The classification on the event severity. 'error' - Significant problem. 'warning' - Not immediately significant. 'informational' - Information only.")
cuspNotifDetail = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 827, 1, 3, 2), OctetString().subtype(subtypeSpec=ValueSizeConstraint(0, 255))).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: cuspNotifDetail.setStatus('current')
if mibBuilder.loadTexts: cuspNotifDetail.setDescription('This object gives the detailed information on error encountered.')
cuspSystemStateAlertEnable = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 827, 1, 3, 3), TruthValue()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cuspSystemStateAlertEnable.setStatus('current')
if mibBuilder.loadTexts: cuspSystemStateAlertEnable.setDescription("This variable controls generation of cuspSystemStateAlert. When this is 'true', generation of Notification is enabled and when this variable is 'false', generation of Notification is disabled.")
cuspServerGroupAlertEnable = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 827, 1, 3, 4), TruthValue()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cuspServerGroupAlertEnable.setStatus('current')
if mibBuilder.loadTexts: cuspServerGroupAlertEnable.setDescription('This variable controls the generation of cuspServerGroupAlert.')
cuspServerGroupElementAlertEnable = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 827, 1, 3, 5), TruthValue()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cuspServerGroupElementAlertEnable.setStatus('current')
if mibBuilder.loadTexts: cuspServerGroupElementAlertEnable.setDescription('This variable controls the generation of cuspServerGroupElementAlert')
cuspLicenseExceededAlertEnable = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 827, 1, 3, 6), TruthValue()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cuspLicenseExceededAlertEnable.setStatus('current')
if mibBuilder.loadTexts: cuspLicenseExceededAlertEnable.setDescription('This variable controls the generation of cuspLicenseExceededAlert.')
cuspLicenseStateAlertEnable = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 827, 1, 3, 7), TruthValue()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cuspLicenseStateAlertEnable.setStatus('current')
if mibBuilder.loadTexts: cuspLicenseStateAlertEnable.setDescription('This variable controls the generation of cuspLicenseStateAlert.')
cuspExtensiveLoggingAlertEnable = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 827, 1, 3, 8), TruthValue()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cuspExtensiveLoggingAlertEnable.setStatus('current')
if mibBuilder.loadTexts: cuspExtensiveLoggingAlertEnable.setDescription('This variable controls the generation of cuspExtensiveLoggingAlert.')
cuspDiskSpaceThresholdAlertEnable = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 827, 1, 3, 9), TruthValue()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cuspDiskSpaceThresholdAlertEnable.setStatus('current')
if mibBuilder.loadTexts: cuspDiskSpaceThresholdAlertEnable.setDescription('This variable controls the generation of cuspDiskSpaceThresholdAlert.')
cuspMemoryThresholdAlertEnable = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 827, 1, 3, 10), TruthValue()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cuspMemoryThresholdAlertEnable.setStatus('current')
if mibBuilder.loadTexts: cuspMemoryThresholdAlertEnable.setDescription('This variable controls the generation of cuspMemoryThresholdAlert.')
cuspBackupProcessFailAlertEnable = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 827, 1, 3, 11), TruthValue()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cuspBackupProcessFailAlertEnable.setStatus('current')
if mibBuilder.loadTexts: cuspBackupProcessFailAlertEnable.setDescription('This variable controls the generation of cuspBackupProcessFailAlert notification.')
cuspConnectionExceptionAlertEnable = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 827, 1, 3, 12), TruthValue()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cuspConnectionExceptionAlertEnable.setStatus('current')
if mibBuilder.loadTexts: cuspConnectionExceptionAlertEnable.setDescription('This variable controls the generation of cuspConnectionExceptionAlert.')
mibBuilder.exportSymbols("CISCO-USP-MIB", cuspServerGroupEntry=cuspServerGroupEntry, cuspCallStats=cuspCallStats, cuspMemoryThresholdAlert=cuspMemoryThresholdAlert, cuspDiskSpaceUsed=cuspDiskSpaceUsed, cuspMaxDroppedCPSOneMin=cuspMaxDroppedCPSOneMin, cuspTotalCalls=cuspTotalCalls, cuspLastCounterResetTime=cuspLastCounterResetTime, cuspTotalFailedCalls=cuspTotalFailedCalls, cuspElementTable=cuspElementTable, ciscoUspMIBNotifyGroup=ciscoUspMIBNotifyGroup, cuspElementEntry=cuspElementEntry, cuspMemoryUsed=cuspMemoryUsed, cuspServerGroupTable=cuspServerGroupTable, cuspLicenseExceededAlert=cuspLicenseExceededAlert, ciscoUspMIBMainObjectGroup=ciscoUspMIBMainObjectGroup, cuspConnectionExceptionAlert=cuspConnectionExceptionAlert, cuspServerGroupElementAlertEnable=cuspServerGroupElementAlertEnable, cuspMaxCPSOneMin=cuspMaxCPSOneMin, cuspServerGroupAlert=cuspServerGroupAlert, cuspSystemUpTime=cuspSystemUpTime, cuspDiskSpaceThresholdAlertEnable=cuspDiskSpaceThresholdAlertEnable, cuspServerGroupNetwork=cuspServerGroupNetwork, ciscoUspMIBGroups=ciscoUspMIBGroups, cuspDiskSpaceThresholdAlert=cuspDiskSpaceThresholdAlert, cuspLicenseState=cuspLicenseState, cuspServerGroupName=cuspServerGroupName, cuspBackupProcessFailAlertEnable=cuspBackupProcessFailAlertEnable, cuspElementStatus=cuspElementStatus, ciscoUspMIBObjects=ciscoUspMIBObjects, cuspDiskSpaceThresholdValue=cuspDiskSpaceThresholdValue, cuspMessageStats=cuspMessageStats, cuspElementQValue=cuspElementQValue, ciscoUspMIBConform=ciscoUspMIBConform, cuspLicenseStateAlertEnable=cuspLicenseStateAlertEnable, ciscoUspMIBCompliances=ciscoUspMIBCompliances, cuspServerGroupElementAlert=cuspServerGroupElementAlert, cuspLicenseStateAlert=cuspLicenseStateAlert, cuspCallsRoutedOneSec=cuspCallsRoutedOneSec, cuspTable=cuspTable, cuspServerGroupIndex=cuspServerGroupIndex, cuspSystemStateAlertEnable=cuspSystemStateAlertEnable, cuspExtensiveLoggingAlert=cuspExtensiveLoggingAlert, cuspMaxCallsRoutedOneMin=cuspMaxCallsRoutedOneMin, cuspConfiguredMemory=cuspConfiguredMemory, cuspElementTotalCalls=cuspElementTotalCalls, cuspConnectionExceptionAlertEnable=cuspConnectionExceptionAlertEnable, cuspAvgCallsRoutedOneMin=cuspAvgCallsRoutedOneMin, cuspElementPort=cuspElementPort, cuspElementTransport=cuspElementTransport, cuspServerGroupLBType=cuspServerGroupLBType, ciscoUspMIBModuleCompliance=ciscoUspMIBModuleCompliance, cuspStrayMessageCount=cuspStrayMessageCount, cuspServerGroupPingStatus=cuspServerGroupPingStatus, cuspDroppedCallsOneSec=cuspDroppedCallsOneSec, cuspNoOfMessagesRecieved=cuspNoOfMessagesRecieved, ciscoUspMIBNotifs=ciscoUspMIBNotifs, cuspAvgCPSOneMin=cuspAvgCPSOneMin, cuspLicenseExceededAlertEnable=cuspLicenseExceededAlertEnable, cuspServerGroupAlertEnable=cuspServerGroupAlertEnable, cuspNotifSeverity=cuspNotifSeverity, cuspAvgDroppedCPSOneMin=cuspAvgDroppedCPSOneMin, cuspCallsDroppedExceedingLicense=cuspCallsDroppedExceedingLicense, cuspBackupProcessFailAlert=cuspBackupProcessFailAlert, cuspSystemStateAlert=cuspSystemStateAlert, cuspElementName=cuspElementName, cuspNotifDetail=cuspNotifDetail, cuspSmartAgentState=cuspSmartAgentState, PYSNMP_MODULE_ID=ciscoUspMIB, cuspThresholdValues=cuspThresholdValues, cuspElementFailedCalls=cuspElementFailedCalls, cuspSystemState=cuspSystemState, cuspExtensiveLoggingAlertEnable=cuspExtensiveLoggingAlertEnable, cuspScalar=cuspScalar, cuspServerGroupStatus=cuspServerGroupStatus, cuspCPS=cuspCPS, cuspMemoryThresholdAlertEnable=cuspMemoryThresholdAlertEnable, cuspMemoryThresholdValue=cuspMemoryThresholdValue, cuspLicenseLimit=cuspLicenseLimit, cuspElementIndex=cuspElementIndex, cuspElementWeight=cuspElementWeight, cuspNotifControlInfo=cuspNotifControlInfo, ciscoUspMIB=ciscoUspMIB)
