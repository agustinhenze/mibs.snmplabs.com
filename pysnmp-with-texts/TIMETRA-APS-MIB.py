#
# PySNMP MIB module TIMETRA-APS-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/TIMETRA-APS-MIB
# Produced by pysmi-0.3.4 at Wed May  1 15:16:51 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
apsCommandSwitch, apsStatusK1K2Trans, apsChanConfigEntry, apsStatusCurrent, apsStatusK1K2Rcv, apsStatusSwitchedChannel, apsCommandEntry, apsConfigEntry = mibBuilder.importSymbols("APS-MIB", "apsCommandSwitch", "apsStatusK1K2Trans", "apsChanConfigEntry", "apsStatusCurrent", "apsStatusK1K2Rcv", "apsStatusSwitchedChannel", "apsCommandEntry", "apsConfigEntry")
OctetString, ObjectIdentifier, Integer = mibBuilder.importSymbols("ASN1", "OctetString", "ObjectIdentifier", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, ConstraintsIntersection, ValueSizeConstraint, SingleValueConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "ConstraintsIntersection", "ValueSizeConstraint", "SingleValueConstraint", "ConstraintsUnion")
InetAddress, InetAddressType = mibBuilder.importSymbols("INET-ADDRESS-MIB", "InetAddress", "InetAddressType")
ModuleCompliance, ObjectGroup, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "ObjectGroup", "NotificationGroup")
Gauge32, Counter32, TimeTicks, IpAddress, iso, ObjectIdentity, MibIdentifier, NotificationType, ModuleIdentity, Counter64, Unsigned32, MibScalar, MibTable, MibTableRow, MibTableColumn, Bits, Integer32 = mibBuilder.importSymbols("SNMPv2-SMI", "Gauge32", "Counter32", "TimeTicks", "IpAddress", "iso", "ObjectIdentity", "MibIdentifier", "NotificationType", "ModuleIdentity", "Counter64", "Unsigned32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Bits", "Integer32")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
timetraSRMIBModules, tmnxSRConfs, tmnxSRNotifyPrefix, tmnxSRObjs = mibBuilder.importSymbols("TIMETRA-GLOBAL-MIB", "timetraSRMIBModules", "tmnxSRConfs", "tmnxSRNotifyPrefix", "tmnxSRObjs")
timetraAPSMIBModule = ModuleIdentity((1, 3, 6, 1, 4, 1, 6527, 1, 1, 3, 29))
timetraAPSMIBModule.setRevisions(('1911-02-01 00:00', '1906-03-23 00:00', '1905-08-31 00:00', '1905-01-24 00:00', '1904-10-28 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: timetraAPSMIBModule.setRevisionsDescriptions(('Rev 9.0 1 Feb 2011 00:00 9.0 release of the TIMETRA-APS-MIB.', 'Rev 4.0 23 Mar 2006 00:00 4.0 release of the TIMETRA-APS-MIB.', 'Rev 3.0 31 Aug 2005 00:00 3.0 release of the TIMETRA-APS-MIB.', 'Rev 2.1 24 Jan 2005 00:00 2.1 release of the TIMETRA-APS-MIB.', 'Rev 1.0 28 Oct 2004 00:00 Initial version of the TIMETRA-APS-MIB.',))
if mibBuilder.loadTexts: timetraAPSMIBModule.setLastUpdated('201102010000Z')
if mibBuilder.loadTexts: timetraAPSMIBModule.setOrganization('Alcatel-Lucent')
if mibBuilder.loadTexts: timetraAPSMIBModule.setContactInfo('Alcatel-Lucent SROS Support Web: http://support.alcatel-lucent.com ')
if mibBuilder.loadTexts: timetraAPSMIBModule.setDescription("This document is the SNMP MIB module to manage and provision APS functionality for the Alcatel-Lucent SROS products. This includes extensions to the APS MIB defined in RFC 3498. Copyright 2004-2011 Alcatel-Lucent. All rights reserved. Reproduction of this document is authorized on the condition that the foregoing copyright notice is included. This SNMP MIB module (Specification) embodies Alcatel-Lucent's proprietary intellectual property. Alcatel-Lucent retains all title and ownership in the Specification, including any revisions. Alcatel-Lucent grants all interested parties a non-exclusive license to use and distribute an unmodified copy of this Specification in connection with management of Alcatel-Lucent products, and without fee, provided this copyright notice and license appear on all copies. This Specification is supplied 'as is', and Alcatel-Lucent makes no warranty, either express or implied, as to the use, operation, condition, or performance of the Specification.")
tApsMIBObjs = MibIdentifier((1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 29))
tApsNotificationsPrefix = MibIdentifier((1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 29))
tApsNotifications = MibIdentifier((1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 29, 0))
tApsMIBConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 29))
tApsCommandTable = MibTable((1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 29, 1), )
if mibBuilder.loadTexts: tApsCommandTable.setStatus('current')
if mibBuilder.loadTexts: tApsCommandTable.setDescription('This table augments the apsCommandTable of the APS-MIB')
tApsCommandEntry = MibTableRow((1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 29, 1, 1), )
apsCommandEntry.registerAugmentions(("TIMETRA-APS-MIB", "tApsCommandEntry"))
tApsCommandEntry.setIndexNames(*apsCommandEntry.getIndexNames())
if mibBuilder.loadTexts: tApsCommandEntry.setStatus('current')
if mibBuilder.loadTexts: tApsCommandEntry.setDescription('A conceptual row in the tApsCommandTable. This row exists only if the associated apsConfigEntry is active.')
tApsExerciseCommandResult = MibTableColumn((1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 29, 1, 1, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))).clone(namedValues=NamedValues(("passed", 1), ("failed", 2), ("preempted", 3), ("unknown", 4)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: tApsExerciseCommandResult.setStatus('current')
if mibBuilder.loadTexts: tApsExerciseCommandResult.setDescription('Stores the result of the last exercise command on the APS group and channel specified by the index values. When read this object returns 4(unknown) if no exercise command has been written to this channel since initialization.')
tApsChanStatusTable = MibTable((1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 29, 2), )
if mibBuilder.loadTexts: tApsChanStatusTable.setStatus('current')
if mibBuilder.loadTexts: tApsChanStatusTable.setDescription('This table augments the apsChanConfigTable of the APS-MIB. It contains status information in addition to those mentioned in apsChanStatusTable of the APS MIB.')
tApsChanStatusEntry = MibTableRow((1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 29, 2, 1), )
apsChanConfigEntry.registerAugmentions(("TIMETRA-APS-MIB", "tApsChanStatusEntry"))
tApsChanStatusEntry.setIndexNames(*apsChanConfigEntry.getIndexNames())
if mibBuilder.loadTexts: tApsChanStatusEntry.setStatus('current')
if mibBuilder.loadTexts: tApsChanStatusEntry.setDescription('A conceptual row in the tApsChanStatusTable. This row exists only if the associated apsChanConfigEntry exists.')
tApsChanTxLaisState = MibTableColumn((1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 29, 2, 1, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1, 2))).clone(namedValues=NamedValues(("clear", 0), ("momentary", 1), ("persistent", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: tApsChanTxLaisState.setStatus('current')
if mibBuilder.loadTexts: tApsChanTxLaisState.setDescription("The current state of the 7x50 APS forced Tx-LAIS on the specified APS channel. Note that the 7x50 products always receive and transmit on the same (active) APS channel. For a Multi-Chassis (MC) APS or a unidirectional APS group, the 7x50 product may transmit (Tx) L-AIS on the inactive APS channel to force the remote end to receive traffic on the 7x50 selected active APS channel. The state clear indicates that the 7x50 product currently doesn't transmit any forced LAIS on the APS channel. The state momentary indicates that the 7x50 product has transmitted forced LAIS on the APS channel for a moment(e.g. 100 msec). The state persistent indicates that the 7x50 product has been persistently transmitting forced LAIS on the APS channel.")
tApsMcConfigTable = MibTable((1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 29, 3), )
if mibBuilder.loadTexts: tApsMcConfigTable.setStatus('current')
if mibBuilder.loadTexts: tApsMcConfigTable.setDescription('This table augments the apsConfigTable of the APS-MIB.')
tApsMcConfigEntry = MibTableRow((1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 29, 3, 1), )
apsConfigEntry.registerAugmentions(("TIMETRA-APS-MIB", "tApsMcConfigEntry"))
tApsMcConfigEntry.setIndexNames(*apsConfigEntry.getIndexNames())
if mibBuilder.loadTexts: tApsMcConfigEntry.setStatus('current')
if mibBuilder.loadTexts: tApsMcConfigEntry.setDescription('A conceptual row in the tApsMcConfigTable. This row exists only if the associated apsConfigEntry is active.')
tApsMcNeighborAddrType = MibTableColumn((1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 29, 3, 1, 1), InetAddressType()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: tApsMcNeighborAddrType.setStatus('current')
if mibBuilder.loadTexts: tApsMcNeighborAddrType.setDescription("The value of object tApsMcNeighborAddrType specifies the address type of the neighbor's ip-address as specified by tApsMcNeighborAddr in the case of Multi-Chassis APS architecture.")
tApsMcNeighborAddr = MibTableColumn((1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 29, 3, 1, 2), InetAddress().subtype(subtypeSpec=ValueSizeConstraint(4, 20)).clone(hexValue="00000000000000000000000000000000")).setMaxAccess("readwrite")
if mibBuilder.loadTexts: tApsMcNeighborAddr.setStatus('current')
if mibBuilder.loadTexts: tApsMcNeighborAddr.setDescription("The value of tApsMcNeighborAddr variable specifies the neighbor's ip-address only on a Multi-Chassis APS where the working and protect circuits are configured on different routers. The value of tApsMcNeighborAddr set to 0.0.0.0, implies that this APS group is configured as a Single-Chassis APS group. The route to the neighbor must not traverse the MC-APS member (working or protect) circuits. It is recommended that the address configured here is on a shared network between the routers that own the working and protect circuits. By default no neighbor address is configured and both the working and protect circuits are to be configured on the same router (i.e. Single-Chassis APS).")
tApsMcAdvertiseInterval = MibTableColumn((1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 29, 3, 1, 3), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(10, 650)).clone(10)).setUnits('100s of milliseconds').setMaxAccess("readwrite")
if mibBuilder.loadTexts: tApsMcAdvertiseInterval.setStatus('current')
if mibBuilder.loadTexts: tApsMcAdvertiseInterval.setDescription("The value of tApsMcAdvertiseInterval specifies the time interval, in 100s of milliseconds, between 'I am operational' messages sent by both protect and working circuits to their neighbor for Multi-Chassis APS. The value of tApsMcAdvertiseInterval is valid only for a Multi-Chassis APS as indicated by the value of tApsMcNeighborAddr not set to 0.0.0.0.")
tApsMcHoldTime = MibTableColumn((1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 29, 3, 1, 4), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(10, 650)).clone(30)).setUnits('100s of milliseconds').setMaxAccess("readwrite")
if mibBuilder.loadTexts: tApsMcHoldTime.setStatus('current')
if mibBuilder.loadTexts: tApsMcHoldTime.setDescription('The value of tApsMcHoldTime specifies how much time can pass, in 100s of milliseconds, without receiving an advertise packet from the neighbor before the Multi-Chassis signaling link is considered not operational. It is usually 3 times the value of tApsMcAdvertiseInterval. The value of tApsMcAdvertiseInterval is valid only for a Multi-Chassis APS as indicated by the value of tApsMcNeighborAddr not set to 0.0.0.0.')
tApsMcStatusTable = MibTable((1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 29, 4), )
if mibBuilder.loadTexts: tApsMcStatusTable.setStatus('current')
if mibBuilder.loadTexts: tApsMcStatusTable.setDescription('tApsMcStatusTable augments the apsConfigTable of the APS-MIB. It contains status information in addition to those mentioned in apsStatusTable of the APS MIB.')
tApsMcStatusEntry = MibTableRow((1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 29, 4, 1), )
apsConfigEntry.registerAugmentions(("TIMETRA-APS-MIB", "tApsMcStatusEntry"))
tApsMcStatusEntry.setIndexNames(*apsConfigEntry.getIndexNames())
if mibBuilder.loadTexts: tApsMcStatusEntry.setStatus('current')
if mibBuilder.loadTexts: tApsMcStatusEntry.setDescription('A conceptual row in the tApsMcStatusTable. This row exists only if the associated apsConfigEntry exists.')
tApsMcApsCtlLinkState = MibTableColumn((1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 29, 4, 1, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1, 2))).clone(namedValues=NamedValues(("up", 0), ("dnSignalingFailure", 1), ("dnIncompatibleNbr", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: tApsMcApsCtlLinkState.setStatus('current')
if mibBuilder.loadTexts: tApsMcApsCtlLinkState.setDescription("The value of tApsMcApsCtlLinkState indicates the current state of the 7x50 Multi-Chassis (MC) APS Group Control Link. Note that for a Single-Chassis APS group the state is always up. The state 'up' indicates that the 7x50 MC-APS controller has received a valid control message from its neighboring router within the last tApsMcHoldTime interval, and the MC-APS control link is considered as operational. The state 'dnSignalingFailure' indicates that the 7x50 MC-APS controller hasn't received any control message from its neighboring router or vice-versa within the last tApsMcHoldTime interval.The MC-APS control link is considered as operationally down. The state 'dnIncompatibleNbr' indicates that the 7x50 MC-APS controller has received a control message from a neighboring router within the last tApsMcHoldTime interval, but the member circuit type (i.e. working/protection) of the neighboring router is not compatible with that of the local router. The MC-APS control link is considered as operationally down.")
tApsConfigTable = MibTable((1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 29, 5), )
if mibBuilder.loadTexts: tApsConfigTable.setStatus('current')
if mibBuilder.loadTexts: tApsConfigTable.setDescription('tApsConfigTable augments the apsConfigTable of the APS-MIB. It contains configuration information in addition to those mentioned in apsConfigTable of the APS MIB.')
tApsConfigEntry = MibTableRow((1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 29, 5, 1), )
apsConfigEntry.registerAugmentions(("TIMETRA-APS-MIB", "tApsConfigEntry"))
tApsConfigEntry.setIndexNames(*apsConfigEntry.getIndexNames())
if mibBuilder.loadTexts: tApsConfigEntry.setStatus('current')
if mibBuilder.loadTexts: tApsConfigEntry.setDescription('A conceptual row in the tApsConfigTable. This row exists only if the associated apsConfigEntry exists.')
tApsProtectionType = MibTableColumn((1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 29, 5, 1, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("onePlusOneSignalling", 1), ("onePlusOne", 2))).clone('onePlusOneSignalling')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: tApsProtectionType.setStatus('current')
if mibBuilder.loadTexts: tApsProtectionType.setDescription('The value of tApsProtectionType specifies the protection type of the APS group. The valid options are: onePlusOneSignalling (1) -- Signalling is 1+1, data is 1:1. onePlusOne (2) -- Both signalling and data is 1+1.')
tApsLineSFHoldTime = MibTableColumn((1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 29, 5, 1, 2), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(0, 100))).setUnits('100s of milliseconds').setMaxAccess("readwrite")
if mibBuilder.loadTexts: tApsLineSFHoldTime.setStatus('current')
if mibBuilder.loadTexts: tApsLineSFHoldTime.setDescription('The value of tApsLineSFHoldTime specifies the time, in 100s of milliseconds, that the APS group will remain operational up before reporting a Line Signal Failure due to lais or b2err-sf.')
tApsLineSDHoldTime = MibTableColumn((1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 29, 5, 1, 3), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(0, 100))).setUnits('100s of milliseconds').setMaxAccess("readwrite")
if mibBuilder.loadTexts: tApsLineSDHoldTime.setStatus('current')
if mibBuilder.loadTexts: tApsLineSDHoldTime.setDescription('The value of tApsLineSDHoldTime specifies the time, in 100s of milliseconds, that the APS group will remain operational up before reporting a Line Signal Degredation due to b2err-sd.')
tApsRdiAlarmGeneration = MibTableColumn((1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 29, 5, 1, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1))).clone(namedValues=NamedValues(("suppress", 0), ("circuit", 1))).clone('circuit')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: tApsRdiAlarmGeneration.setStatus('current')
if mibBuilder.loadTexts: tApsRdiAlarmGeneration.setDescription('The value of tApsRdiAlarmGeneration specifies the method used to generate RDI alarms on all levels (line, path) for the APS physical protecting/working ports referenced by apsChanConfigIfIndex. The modification of the tApsRdiAlarmGeneration value is limited to an APS port with no protecting/working ports, otherwise an INCONSISTENT VALUE error is returned. The available enumerations for tApsRdiAlarmGeneration are: - suppress - RDI alarms are not generated on any level. - circuit - RDI alarms are H/W generated independently on each working and protect circuit on RX failure of that circuit.')
tApsGroupCommandTable = MibTable((1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 29, 6), )
if mibBuilder.loadTexts: tApsGroupCommandTable.setStatus('current')
if mibBuilder.loadTexts: tApsGroupCommandTable.setDescription('tApsGroupCommandTable augments APS-MIB::apsConfigTable. It contains command information in addition to the configuration information in APS-MIB::apsConfigTable.')
tApsGroupCommandEntry = MibTableRow((1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 29, 6, 1), )
apsConfigEntry.registerAugmentions(("TIMETRA-APS-MIB", "tApsGroupCommandEntry"))
tApsGroupCommandEntry.setIndexNames(*apsConfigEntry.getIndexNames())
if mibBuilder.loadTexts: tApsGroupCommandEntry.setStatus('current')
if mibBuilder.loadTexts: tApsGroupCommandEntry.setDescription('A conceptual row in tApsGroupCommandTable. This row exists only if the associated apsConfigEntry exists.')
tApsAnnexBCommandSwitch = MibTableColumn((1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 29, 6, 1, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("noCmd", 1), ("lockout", 2), ("clearLockout", 3)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: tApsAnnexBCommandSwitch.setStatus('current')
if mibBuilder.loadTexts: tApsAnnexBCommandSwitch.setDescription("The value of tApsAnnexBCommandSwitch specifies the Annex B supported APS switch command applied to the APS group. The supported values: 'noCmd(1)' -- no command was applied to the group since system -- initialization. 'lockout(2)' -- lockout the APS group. 'clearLockout(3)' -- clear the lockout. Sets to value 'lockout(2)' or 'clearLockout(3)' will be rejected with error inconsistentValue if APS-MIB::apsConfigMode is not equal to 'onePlusOneOptimized(4)'. If 'noCmd(1)' is used in a write operation a wrongValue error is returned. When read this object returns the last command written or 'noCmd(1)'.")
tApsModeMismatchClear = NotificationType((1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 29, 0, 1)).setObjects(("APS-MIB", "apsStatusCurrent"))
if mibBuilder.loadTexts: tApsModeMismatchClear.setStatus('current')
if mibBuilder.loadTexts: tApsModeMismatchClear.setDescription("The tApsModeMismatchClear notification is generated when a mode mismatch condition, indicated by the 'modeMismatch(0)' bit of APS-MIB::apsStatusCurrent, is cleared.")
tApsChannelMismatchClear = NotificationType((1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 29, 0, 2)).setObjects(("APS-MIB", "apsStatusCurrent"))
if mibBuilder.loadTexts: tApsChannelMismatchClear.setStatus('current')
if mibBuilder.loadTexts: tApsChannelMismatchClear.setDescription("The tApsChannelMismatchClear notification is generated when a channel mismatch condition, indicated by the 'channelMismatch(1)' bit of APS-MIB::apsStatusCurrent, is cleared.")
tApsPSBFClear = NotificationType((1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 29, 0, 3)).setObjects(("APS-MIB", "apsStatusCurrent"))
if mibBuilder.loadTexts: tApsPSBFClear.setStatus('current')
if mibBuilder.loadTexts: tApsPSBFClear.setDescription("The tApsPSBFClear notification is generated when a PSBF (Protection Switch Byte Failure) condition, indicated by the 'psbf(2)' bit of APS-MIB::apsStatusCurrent, is cleared.")
tApsFEPLFClear = NotificationType((1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 29, 0, 4)).setObjects(("APS-MIB", "apsStatusCurrent"))
if mibBuilder.loadTexts: tApsFEPLFClear.setStatus('current')
if mibBuilder.loadTexts: tApsFEPLFClear.setDescription("The tApsFEPLFClear notification is generated when a FEPLF (Far-End Protection-Line Failure) condition, indicated by the 'feplf(3)' bit of APS-MIB::apsStatusCurrent, is cleared.")
tApsLocalSwitchCommandSet = NotificationType((1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 29, 0, 5)).setObjects(("APS-MIB", "apsCommandSwitch"))
if mibBuilder.loadTexts: tApsLocalSwitchCommandSet.setStatus('current')
if mibBuilder.loadTexts: tApsLocalSwitchCommandSet.setDescription("The tApsLocalSwitchCommandSet is generated when any of the following APS switch commands are set on APS-MIB::apsCommandSwitch in the local node. The switch commands are 'lockoutOfProtection', 'forcedSwitchWorkToProtect', 'forcedSwitchProtectToWork', 'manualSwitchWorkToProtect', 'manualSwitchProtectToWork'.")
tApsLocalSwitchCommandClear = NotificationType((1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 29, 0, 6)).setObjects(("APS-MIB", "apsCommandSwitch"))
if mibBuilder.loadTexts: tApsLocalSwitchCommandClear.setStatus('current')
if mibBuilder.loadTexts: tApsLocalSwitchCommandClear.setDescription("The tApsLocalSwitchCommandClear notification is generated when an APS switch command in the local node gets cleared. Note that a switch command in the local node can be cleared either due to set of the 'clear' switch command on APS-MIB::apsCommandSwitch in the local node, or due to presence of a higher priority condition in the local or remote node.")
tApsRemoteSwitchCommandSet = NotificationType((1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 29, 0, 7)).setObjects(("APS-MIB", "apsCommandSwitch"))
if mibBuilder.loadTexts: tApsRemoteSwitchCommandSet.setStatus('current')
if mibBuilder.loadTexts: tApsRemoteSwitchCommandSet.setDescription('The tApsRemoteSwitchCommandSet is generated when the received K1 byte (APS-MIB::apsStatusK1K2Rcv) from a peer indicates that an APS switch command just got set on APS-MIB::apsCommandSwitch in the remote (peer) node.')
tApsRemoteSwitchCommandClear = NotificationType((1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 29, 0, 8)).setObjects(("APS-MIB", "apsCommandSwitch"))
if mibBuilder.loadTexts: tApsRemoteSwitchCommandClear.setStatus('current')
if mibBuilder.loadTexts: tApsRemoteSwitchCommandClear.setDescription('The tApsRemoteSwitchCommandClear is generated when the received K1 byte (APS-MIB::apsStatusK1K2Rcv) from a peer indicates that an APS switch command just got cleared on an APS channel in the remote (peer) node.')
tApsMcApsCtlLinkStateChange = NotificationType((1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 29, 0, 9)).setObjects(("TIMETRA-APS-MIB", "tApsMcApsCtlLinkState"))
if mibBuilder.loadTexts: tApsMcApsCtlLinkStateChange.setStatus('current')
if mibBuilder.loadTexts: tApsMcApsCtlLinkStateChange.setDescription('tApsMcApsCtlLinkStateChange notification is generated when there is a change in the value of tApsMcApsCtlLinkState.')
tApsChanTxLaisStateChange = NotificationType((1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 29, 0, 10)).setObjects(("TIMETRA-APS-MIB", "tApsChanTxLaisState"))
if mibBuilder.loadTexts: tApsChanTxLaisStateChange.setStatus('current')
if mibBuilder.loadTexts: tApsChanTxLaisStateChange.setDescription('tApsChanTxLaisStateChange notification is generated when there is a change in the value of tApsChanTxLaisState.')
tApsPrimaryChannelChange = NotificationType((1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 29, 0, 11)).setObjects(("APS-MIB", "apsStatusSwitchedChannel"), ("APS-MIB", "apsStatusK1K2Trans"), ("APS-MIB", "apsStatusK1K2Rcv"))
if mibBuilder.loadTexts: tApsPrimaryChannelChange.setStatus('current')
if mibBuilder.loadTexts: tApsPrimaryChannelChange.setDescription('tApsPrimaryChannelChange notification is generated when there is a switch of the primary APS channel. Object apsStatusK1K2Trans indicates the new primary APS channel.')
tmnxApsMIBCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 29, 1))
tmnxApsMIBGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 29, 2))
tApsMIBCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 29, 1, 1)).setObjects(("TIMETRA-APS-MIB", "tmnxApsSwitchCommand"), ("TIMETRA-APS-MIB", "tmnxApsChanStatus"), ("TIMETRA-APS-MIB", "tmnxApsNotifications"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    tApsMIBCompliance = tApsMIBCompliance.setStatus('obsolete')
if mibBuilder.loadTexts: tApsMIBCompliance.setDescription('The compliance statement for revision 1.0 of TIMETRA-APS-MIB.')
tApsMIBComplianceV4v0 = ModuleCompliance((1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 29, 1, 2)).setObjects(("TIMETRA-APS-MIB", "tmnxApsSwitchCommand"), ("TIMETRA-APS-MIB", "tmnxApsChanStatus"), ("TIMETRA-APS-MIB", "tmnxApsMcGroup"), ("TIMETRA-APS-MIB", "tmnxApsNotificationsV4v0"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    tApsMIBComplianceV4v0 = tApsMIBComplianceV4v0.setStatus('obsolete')
if mibBuilder.loadTexts: tApsMIBComplianceV4v0.setDescription('The compliance statement for revision 4.0 of the Alcatel-Lucent SROS series systems.')
tApsMIBComplianceV7v0 = ModuleCompliance((1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 29, 1, 3)).setObjects(("TIMETRA-APS-MIB", "tmnxApsSwitchCommand"), ("TIMETRA-APS-MIB", "tmnxApsChanStatus"), ("TIMETRA-APS-MIB", "tmnxApsMcGroup"), ("TIMETRA-APS-MIB", "tmnxApsNotificationsV4v0"), ("TIMETRA-APS-MIB", "tmnxApsConfigGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    tApsMIBComplianceV7v0 = tApsMIBComplianceV7v0.setStatus('obsolete')
if mibBuilder.loadTexts: tApsMIBComplianceV7v0.setDescription('The compliance statement for revision 7.0 of the Alcatel-Lucent SROS series systems.')
tApsMIBComplianceV8v0 = ModuleCompliance((1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 29, 1, 4)).setObjects(("TIMETRA-APS-MIB", "tmnxApsSwitchCommand"), ("TIMETRA-APS-MIB", "tmnxApsChanStatus"), ("TIMETRA-APS-MIB", "tmnxApsMcGroup"), ("TIMETRA-APS-MIB", "tmnxApsNotificationsV4v0"), ("TIMETRA-APS-MIB", "tmnxApsConfigGroup"), ("TIMETRA-APS-MIB", "tmnxApsConfigV8v0Group"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    tApsMIBComplianceV8v0 = tApsMIBComplianceV8v0.setStatus('obsolete')
if mibBuilder.loadTexts: tApsMIBComplianceV8v0.setDescription('The compliance statement for revision 8.0 of the Alcatel-Lucent SROS series systems.')
tApsMIBComplianceV9v0 = ModuleCompliance((1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 29, 1, 5)).setObjects(("TIMETRA-APS-MIB", "tmnxApsSwitchCommand"), ("TIMETRA-APS-MIB", "tmnxApsChanStatus"), ("TIMETRA-APS-MIB", "tmnxApsMcGroup"), ("TIMETRA-APS-MIB", "tmnxApsNotificationsV4v0"), ("TIMETRA-APS-MIB", "tmnxApsConfigGroup"), ("TIMETRA-APS-MIB", "tmnxApsConfigV8v0Group"), ("TIMETRA-APS-MIB", "tmnxApsGroupCommandV9v0Group"), ("TIMETRA-APS-MIB", "tmnxApsNotificationsV9v0Group"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    tApsMIBComplianceV9v0 = tApsMIBComplianceV9v0.setStatus('current')
if mibBuilder.loadTexts: tApsMIBComplianceV9v0.setDescription('The compliance statement for release 9.0 of Alcatel-Lucent SROS series systems.')
tmnxApsSwitchCommand = ObjectGroup((1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 29, 2, 1)).setObjects(("TIMETRA-APS-MIB", "tApsExerciseCommandResult"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    tmnxApsSwitchCommand = tmnxApsSwitchCommand.setStatus('current')
if mibBuilder.loadTexts: tmnxApsSwitchCommand.setDescription('The group of objects for management of aps switch command applicable to the aps groups implementing linear APS 1+1 architecture.')
tmnxApsChanStatus = ObjectGroup((1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 29, 2, 2)).setObjects(("TIMETRA-APS-MIB", "tApsChanTxLaisState"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    tmnxApsChanStatus = tmnxApsChanStatus.setStatus('current')
if mibBuilder.loadTexts: tmnxApsChanStatus.setDescription('The group of objects for management of status information applicable to the APS channels implementing linear APS 1+1 architecture.')
tmnxApsNotifications = NotificationGroup((1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 29, 2, 3)).setObjects(("TIMETRA-APS-MIB", "tApsModeMismatchClear"), ("TIMETRA-APS-MIB", "tApsChannelMismatchClear"), ("TIMETRA-APS-MIB", "tApsPSBFClear"), ("TIMETRA-APS-MIB", "tApsFEPLFClear"), ("TIMETRA-APS-MIB", "tApsLocalSwitchCommandSet"), ("TIMETRA-APS-MIB", "tApsLocalSwitchCommandClear"), ("TIMETRA-APS-MIB", "tApsRemoteSwitchCommandSet"), ("TIMETRA-APS-MIB", "tApsRemoteSwitchCommandClear"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    tmnxApsNotifications = tmnxApsNotifications.setStatus('obsolete')
if mibBuilder.loadTexts: tmnxApsNotifications.setDescription('A collection of SONET liner APS notifications.')
tmnxApsNotificationsV4v0 = NotificationGroup((1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 29, 2, 4)).setObjects(("TIMETRA-APS-MIB", "tApsModeMismatchClear"), ("TIMETRA-APS-MIB", "tApsChannelMismatchClear"), ("TIMETRA-APS-MIB", "tApsPSBFClear"), ("TIMETRA-APS-MIB", "tApsFEPLFClear"), ("TIMETRA-APS-MIB", "tApsLocalSwitchCommandSet"), ("TIMETRA-APS-MIB", "tApsLocalSwitchCommandClear"), ("TIMETRA-APS-MIB", "tApsRemoteSwitchCommandSet"), ("TIMETRA-APS-MIB", "tApsRemoteSwitchCommandClear"), ("TIMETRA-APS-MIB", "tApsMcApsCtlLinkStateChange"), ("TIMETRA-APS-MIB", "tApsChanTxLaisStateChange"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    tmnxApsNotificationsV4v0 = tmnxApsNotificationsV4v0.setStatus('current')
if mibBuilder.loadTexts: tmnxApsNotificationsV4v0.setDescription('A collection of SONET liner APS notifications for revision 4.0 of the Alcatel-Lucent SROS series systems.')
tmnxApsMcGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 29, 2, 5)).setObjects(("TIMETRA-APS-MIB", "tApsMcNeighborAddrType"), ("TIMETRA-APS-MIB", "tApsMcNeighborAddr"), ("TIMETRA-APS-MIB", "tApsMcAdvertiseInterval"), ("TIMETRA-APS-MIB", "tApsMcHoldTime"), ("TIMETRA-APS-MIB", "tApsMcApsCtlLinkState"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    tmnxApsMcGroup = tmnxApsMcGroup.setStatus('current')
if mibBuilder.loadTexts: tmnxApsMcGroup.setDescription('The group of objects for the configuration of a Multi-Chassis APS group.')
tmnxApsConfigGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 29, 2, 6)).setObjects(("TIMETRA-APS-MIB", "tApsProtectionType"), ("TIMETRA-APS-MIB", "tApsLineSFHoldTime"), ("TIMETRA-APS-MIB", "tApsLineSDHoldTime"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    tmnxApsConfigGroup = tmnxApsConfigGroup.setStatus('current')
if mibBuilder.loadTexts: tmnxApsConfigGroup.setDescription('The group of objects for the configuration of APS groups added for revision 7.0 of the Alcatel-Lucent SROS series systems.')
tmnxApsConfigV8v0Group = ObjectGroup((1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 29, 2, 7)).setObjects(("TIMETRA-APS-MIB", "tApsRdiAlarmGeneration"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    tmnxApsConfigV8v0Group = tmnxApsConfigV8v0Group.setStatus('current')
if mibBuilder.loadTexts: tmnxApsConfigV8v0Group.setDescription('The group of objects for the configuration of APS groups added for revision 8.0 of the Alcatel-Lucent SROS series systems.')
tmnxApsGroupCommandV9v0Group = ObjectGroup((1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 29, 2, 8)).setObjects(("TIMETRA-APS-MIB", "tApsAnnexBCommandSwitch"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    tmnxApsGroupCommandV9v0Group = tmnxApsGroupCommandV9v0Group.setStatus('current')
if mibBuilder.loadTexts: tmnxApsGroupCommandV9v0Group.setDescription('The group of APS group command objects for release 9.0 of Alcatel-Lucent SROS series systems.')
tmnxApsNotificationsV9v0Group = NotificationGroup((1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 29, 2, 9)).setObjects(("TIMETRA-APS-MIB", "tApsPrimaryChannelChange"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    tmnxApsNotificationsV9v0Group = tmnxApsNotificationsV9v0Group.setStatus('current')
if mibBuilder.loadTexts: tmnxApsNotificationsV9v0Group.setDescription('The group of APS notifications for release 9.0 of Alcatel-Lucent SROS series systems.')
mibBuilder.exportSymbols("TIMETRA-APS-MIB", tApsMcStatusTable=tApsMcStatusTable, tApsMcNeighborAddrType=tApsMcNeighborAddrType, tmnxApsConfigGroup=tmnxApsConfigGroup, tApsConfigEntry=tApsConfigEntry, tmnxApsGroupCommandV9v0Group=tmnxApsGroupCommandV9v0Group, tApsMIBComplianceV7v0=tApsMIBComplianceV7v0, tApsMIBObjs=tApsMIBObjs, tmnxApsSwitchCommand=tmnxApsSwitchCommand, tApsCommandEntry=tApsCommandEntry, tApsFEPLFClear=tApsFEPLFClear, tmnxApsConfigV8v0Group=tmnxApsConfigV8v0Group, tApsGroupCommandTable=tApsGroupCommandTable, tmnxApsMIBCompliances=tmnxApsMIBCompliances, tApsMcConfigEntry=tApsMcConfigEntry, tmnxApsChanStatus=tmnxApsChanStatus, tApsLocalSwitchCommandSet=tApsLocalSwitchCommandSet, tmnxApsNotifications=tmnxApsNotifications, tApsModeMismatchClear=tApsModeMismatchClear, tApsMIBCompliance=tApsMIBCompliance, tApsMIBConformance=tApsMIBConformance, tApsMcHoldTime=tApsMcHoldTime, tApsExerciseCommandResult=tApsExerciseCommandResult, tApsLocalSwitchCommandClear=tApsLocalSwitchCommandClear, tApsChanTxLaisStateChange=tApsChanTxLaisStateChange, tApsMcStatusEntry=tApsMcStatusEntry, tApsChanStatusTable=tApsChanStatusTable, tApsLineSFHoldTime=tApsLineSFHoldTime, tApsRdiAlarmGeneration=tApsRdiAlarmGeneration, PYSNMP_MODULE_ID=timetraAPSMIBModule, tApsRemoteSwitchCommandClear=tApsRemoteSwitchCommandClear, tApsChannelMismatchClear=tApsChannelMismatchClear, tApsMcApsCtlLinkState=tApsMcApsCtlLinkState, tApsChanTxLaisState=tApsChanTxLaisState, timetraAPSMIBModule=timetraAPSMIBModule, tmnxApsMIBGroups=tmnxApsMIBGroups, tApsConfigTable=tApsConfigTable, tApsMcAdvertiseInterval=tApsMcAdvertiseInterval, tApsRemoteSwitchCommandSet=tApsRemoteSwitchCommandSet, tApsMcNeighborAddr=tApsMcNeighborAddr, tApsMIBComplianceV4v0=tApsMIBComplianceV4v0, tApsLineSDHoldTime=tApsLineSDHoldTime, tApsNotificationsPrefix=tApsNotificationsPrefix, tApsMcConfigTable=tApsMcConfigTable, tApsAnnexBCommandSwitch=tApsAnnexBCommandSwitch, tApsPSBFClear=tApsPSBFClear, tApsGroupCommandEntry=tApsGroupCommandEntry, tApsNotifications=tApsNotifications, tApsMIBComplianceV8v0=tApsMIBComplianceV8v0, tmnxApsNotificationsV4v0=tmnxApsNotificationsV4v0, tApsCommandTable=tApsCommandTable, tApsProtectionType=tApsProtectionType, tApsMcApsCtlLinkStateChange=tApsMcApsCtlLinkStateChange, tApsPrimaryChannelChange=tApsPrimaryChannelChange, tmnxApsNotificationsV9v0Group=tmnxApsNotificationsV9v0Group, tApsChanStatusEntry=tApsChanStatusEntry, tApsMIBComplianceV9v0=tApsMIBComplianceV9v0, tmnxApsMcGroup=tmnxApsMcGroup)
