#
# PySNMP MIB module CISCO-APS-EXT-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/CISCO-APS-EXT-MIB
# Produced by pysmi-0.3.4 at Wed May  1 11:50:17 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
Integer, OctetString, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "Integer", "OctetString", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, ValueSizeConstraint, ConstraintsUnion, ConstraintsIntersection, SingleValueConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "ValueSizeConstraint", "ConstraintsUnion", "ConstraintsIntersection", "SingleValueConstraint")
cApsConfigEntry, cApsChanConfigEntry, cApsChanStatusEntry, cApsStatusEntry, CApsK1K2 = mibBuilder.importSymbols("CISCO-APS-MIB", "cApsConfigEntry", "cApsChanConfigEntry", "cApsChanStatusEntry", "cApsStatusEntry", "CApsK1K2")
ciscoExperiment, = mibBuilder.importSymbols("CISCO-SMI", "ciscoExperiment")
InetAddress, InetAddressType = mibBuilder.importSymbols("INET-ADDRESS-MIB", "InetAddress", "InetAddressType")
SnmpAdminString, = mibBuilder.importSymbols("SNMP-FRAMEWORK-MIB", "SnmpAdminString")
ObjectGroup, NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "ObjectGroup", "NotificationGroup", "ModuleCompliance")
NotificationType, Bits, TimeTicks, Counter32, MibScalar, MibTable, MibTableRow, MibTableColumn, ObjectIdentity, Gauge32, Integer32, Counter64, ModuleIdentity, Unsigned32, iso, MibIdentifier, IpAddress = mibBuilder.importSymbols("SNMPv2-SMI", "NotificationType", "Bits", "TimeTicks", "Counter32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "ObjectIdentity", "Gauge32", "Integer32", "Counter64", "ModuleIdentity", "Unsigned32", "iso", "MibIdentifier", "IpAddress")
TextualConvention, TruthValue, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "TruthValue", "DisplayString")
cApsExtMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 10, 72))
cApsExtMIB.setRevisions(('2003-01-31 00:00', '2002-05-31 00:00', '2002-05-20 00:00', '2001-05-21 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: cApsExtMIB.setRevisionsDescriptions(('Updated the default value for the object cApsConfigSwitchoverEnableInterval. ', 'Added table cApsChanConfigExtTable which augments cApsChanConfigTable in CISCO-APS-MIB, and table cApsChanAssociationTable that provides for all protection/working channels, the associated working/protection channel IP address. ', 'Added objects for control of APS message transport and to show additional channel status information. ', 'The initial version of this MIB augments cApsConfigEntry (in the CISCO-APS-MIB) with two new APS configuration parameters, cApsConfigSpan and cApsConfigYcable, and cApsStatusEntry with two new status parameters, cApsStatusCdlApsBytesRcv and cApsStatusCdlApsBytesTrans. ',))
if mibBuilder.loadTexts: cApsExtMIB.setLastUpdated('200301310000Z')
if mibBuilder.loadTexts: cApsExtMIB.setOrganization('Cisco Systems, Inc.')
if mibBuilder.loadTexts: cApsExtMIB.setContactInfo('Cisco Systems, Inc. Customer Service Postal: 170 W. Tasman Drive San Jose, CA 95134-1706 USA Tel: +1 800 553-NETS Email: optmgmt-dev@cisco.com')
if mibBuilder.loadTexts: cApsExtMIB.setDescription("The Cisco APS Extension MIB extends the Cisco APS MIB in order to a) support path APS architectures and b) support interfaces other than SONET (e.g. Cisco CDL). For configuration and monitoring of APS for CDL interfaces, all objects and notifications in the Cisco APS MIB apply, with the exception of the following: - cApsStatusK1K2Rcv and cApsStatusK1K2Trans in cApsStatusEntry, - cApsConfigSdBerThreshold and cApsConfigSfBerThreshold in cApsConfigEntry, - cApsChanStatusSignalDegrades and cApsChanStatusSignalFailures in cApsChanStatusEntry, - cApsStatusFEPLFs in cApsStatusEntry, - cApsEventFEPLF. Whenever the description of an object in the Cisco APS MIB refers to a SONET LTE interface, this applies to CDL terminating interfaces as well. CDL interfaces have ifType values other than 'sonet'. For SONET path APS support, whenever the description of an object in the Cisco APS MIB refers to a SONET LTE interface, this applies to SONET PTE interfaces as well. SONET PTE interfaces have ifType values 'sonetPath'. ")
cApsExtMIBObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 10, 72, 1))
cApsExtMIBConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 10, 72, 2))
class CdlApsBytes(TextualConvention, OctetString):
    description = 'This Textual Convention describes an object that stores the APS protocol field used in CDL. The semantics of the CDL APS protocol field are similar to those of the SONET K1 and K2 byte APS protocol field. '
    status = 'current'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(2, 2)
    fixedLength = 2

class CApsMessageTransport(TextualConvention, Integer32):
    description = 'The type of transport used to exchange APS protocol messages. none There is no APS message exchange between the endpoints of the associated channels. autoSelect APS automatically selects a transport mechanism to send APS messages. The following transport mechanisms are attempted, in the following order of priority: - apsChannel - dcc - osc dcc APS messages are transmitted over the data communications channels (DCCs) in the overhead of the associated channels. apsChannel APS messages are transmitted in overhead bytes of the associated channels that are defined specifically to carry APS messages. ip APS messages are transmitted over IP. The IP network can consist of any combination of data communication channels (DCCs), optical supervisory channels (OSCs), and out-of-band Data Communication Networks (DCNs). osc APS messages are transmitted over the Optical Supervisory Channel (OSC). '
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6))
    namedValues = NamedValues(("none", 1), ("autoSelect", 2), ("dcc", 3), ("apsChannel", 4), ("ip", 5), ("osc", 6))

class CApsChannelConfigNumber(TextualConvention, Integer32):
    reference = 'Bellcore (Telcordia Technologies) GR-253-CORE, Issue 2,Revision 2 (January 1999), 5.3.2. '
    description = 'This Textual Convention describes an object that is set to a unique channel number within an APS group. The value 0 indicates the null channel. The values 1-14 define a working channel. '
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ValueRangeConstraint(0, 14)

cApsNotifiesEnable = MibScalar((1, 3, 6, 1, 4, 1, 9, 10, 72, 1, 1), TruthValue()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cApsNotifiesEnable.setStatus('current')
if mibBuilder.loadTexts: cApsNotifiesEnable.setDescription("When this object is set to 'true', it allows the generation of the APS-related notifications defined in the CISCO-APS-MIB. When this object is set to 'false', it prevents the generation of the APS-related notifications defined in the CISCO-APS-MIB. By default, this object is set to 'false'.")
cApsConfigExtTable = MibTable((1, 3, 6, 1, 4, 1, 9, 10, 72, 1, 2), )
if mibBuilder.loadTexts: cApsConfigExtTable.setStatus('current')
if mibBuilder.loadTexts: cApsConfigExtTable.setDescription('This table augments the cApsConfigTable.')
cApsConfigExtEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9, 10, 72, 1, 2, 1), )
cApsConfigEntry.registerAugmentions(("CISCO-APS-EXT-MIB", "cApsConfigExtEntry"))
cApsConfigExtEntry.setIndexNames(*cApsConfigEntry.getIndexNames())
if mibBuilder.loadTexts: cApsConfigExtEntry.setStatus('current')
if mibBuilder.loadTexts: cApsConfigExtEntry.setDescription('A conceptual row in the cApsConfigExtTable.')
cApsConfigSpan = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 10, 72, 1, 2, 1, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("hopByHop", 1), ("endToEnd", 2))).clone('hopByHop')).setMaxAccess("readcreate")
if mibBuilder.loadTexts: cApsConfigSpan.setStatus('current')
if mibBuilder.loadTexts: cApsConfigSpan.setDescription("The span (hopByHop or endToEnd) for the APS group. hopByHop This refers to linear APS, e.g. linear SONET APS, or hopByHop CDL APS. In a DWDM system, an APS channel may be associated with either an individual wavelength or an optical fiber. All APS channels within an APS group must be of the same type. Systems that support linear APS on an individual wavelength basis, must assign an ifIndex to each such wavelength. endToEnd This refers to path APS, e.g. endToEnd CDL APS. In this configuration, each APS channel in the APS group is associated with an endToEnd user path. This codepoint does not apply to interfaces with an ifType value of 'sonet'. This object may not be modified if the associated cApsConfigRowStatus object is equal to 'active'. ")
cApsConfigYcable = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 10, 72, 1, 2, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("noYcable", 1), ("ycable", 2), ("ycableXconnectCommon", 3))).clone('noYcable')).setMaxAccess("readcreate")
if mibBuilder.loadTexts: cApsConfigYcable.setStatus('current')
if mibBuilder.loadTexts: cApsConfigYcable.setDescription("The Y-cable configuration for the APS group associated with user channels. noYcable The APS channels in the APS group are not connected to an external Y-cable. ycable Two user-side interfaces (not necessarily SONET or CDL) are connected to an external y-cable and are grouped into an APS group for endToEnd APS. The received user signal is split in the y-cable coupler and is received on both the interfaces. However, only one interface must transmit toward the user at any given time. With cApsConfigYcable set to 'ycable', the cApsConfigSpan must be set to 'endToEnd'. There must be only two APS channels in an APS group with cApsConfigYcable set to 'ycable'. ycableXconnectCommon This refers to a configuration where two user-side interfaces are connected to an external y-cable. The two signals received on these interface are connected to the same cross connect in the switch. The switch fabric selects one of the two received signals, duplicates it, and forwards it to two network side interfaces grouped for 1+1 linear APS. The received signal from the network side is transmitted to only one user-side interface. cApsConfigSpan is ignored if cApsConfigYcable is set to 'ycableXconnectCommon'. There must be only two APS channels in an APS group with cApsConfigYcable set to 'ycableXconnectCommon'. This object may not be modified if the associated cApsConfigRowStatus object is equal to 'active'. If this object is set to 'ycable' or 'ycableXconnectCommon', the user must shut one of the two channels before setting cApsConfigRowStatus to 'notInService'. ")
cApsConfigMinSearchUpInterval = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 10, 72, 1, 2, 1, 3), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 120)).clone(2)).setMaxAccess("readcreate")
if mibBuilder.loadTexts: cApsConfigMinSearchUpInterval.setStatus('current')
if mibBuilder.loadTexts: cApsConfigMinSearchUpInterval.setDescription('This object is instantiated only when the standby interface is not monitored. If both interfaces go down and the standby interface is not monitored, successive switchovers may be used in order to search for an interface that is up. This object specifies the minimum time interval between switchovers when both interfaces go down. A backoff algorithm should be used to increase the time interval between successive switchovers. ')
cApsConfigMaxSearchUpInterval = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 10, 72, 1, 2, 1, 4), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 120)).clone(32)).setUnits('seconds').setMaxAccess("readcreate")
if mibBuilder.loadTexts: cApsConfigMaxSearchUpInterval.setStatus('current')
if mibBuilder.loadTexts: cApsConfigMaxSearchUpInterval.setDescription('This object is instantiated only when the standby interface is not monitored. If both interfaces go down and the standby interface is not monitored, successive switchovers may be used in order to search for an interface that is up. This object specifies the maximum time interval between switchovers when both interfaces go down. ')
cApsConfigSwitchoverEnableInterval = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 10, 72, 1, 2, 1, 5), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 120)).clone(3)).setUnits('seconds').setMaxAccess("readcreate")
if mibBuilder.loadTexts: cApsConfigSwitchoverEnableInterval.setStatus('current')
if mibBuilder.loadTexts: cApsConfigSwitchoverEnableInterval.setDescription('This object specifies the value of the timer to control the minimum interval between switchovers. After a switchover, APS is re-enabled only after this amount of time has elapsed, in order to prevent quick successive switchovers. ')
cApsConfigMessageTransport = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 10, 72, 1, 2, 1, 6), CApsMessageTransport().clone('autoSelect')).setMaxAccess("readcreate")
if mibBuilder.loadTexts: cApsConfigMessageTransport.setStatus('current')
if mibBuilder.loadTexts: cApsConfigMessageTransport.setDescription("This object specifies the type of transport configured for exchange of APS protocol messages. The type of transport currently being used is indicated in the cApsStatusMessageTransport object. When this object is set to 'ip', values must be specified for the cApsConfigFarEndIpAddressType, cApsConfigFarEndIpAddress and cApsConfigFarEndGroupName objects. ")
cApsConfigMessageHolddown = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 10, 72, 1, 2, 1, 7), Integer32().subtype(subtypeSpec=ValueRangeConstraint(100, 10000)).clone(5000)).setUnits('milliseconds').setMaxAccess("readcreate")
if mibBuilder.loadTexts: cApsConfigMessageHolddown.setStatus('current')
if mibBuilder.loadTexts: cApsConfigMessageHolddown.setDescription("The value specified in this object applies when the value of cApsStatusMessageTransport is 'dcc', 'ip', or 'osc'. APS messages are exchanged between systems to support bidirectional or linear operation. To avoid potential system misbehavior in which APS messages would be triggered in an uncontrolled fashion, a hold down timer is introduced that prevents successive event-triggered APS messages from being sent in too short a time interval. This object specifies the minimum time between event driven requests. ")
cApsConfigMessageHolddownCount = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 10, 72, 1, 2, 1, 8), Integer32().subtype(subtypeSpec=ValueRangeConstraint(2, 10)).clone(2)).setMaxAccess("readcreate")
if mibBuilder.loadTexts: cApsConfigMessageHolddownCount.setStatus('current')
if mibBuilder.loadTexts: cApsConfigMessageHolddownCount.setDescription("The value specified in this object applies when the value of cApsStatusMessageTransport is 'dcc', 'ip', or 'osc'. The maximum number of APS messages that can be sent within one cApsConfigMessageHolddown interval. ")
cApsConfigMessageMaxInterval = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 10, 72, 1, 2, 1, 9), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1000, 120000)).clone(15000)).setUnits('milliseconds').setMaxAccess("readcreate")
if mibBuilder.loadTexts: cApsConfigMessageMaxInterval.setStatus('current')
if mibBuilder.loadTexts: cApsConfigMessageMaxInterval.setDescription("The value specified in this object applies when the value of cApsStatusMessageTransport is 'dcc', 'ip', or 'osc'. An APS message is sent unconditionally, whenever the amount of time specified by this object has elapsed since the last transmission of an APS message. ")
cApsConfigFarEndGroupName = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 10, 72, 1, 2, 1, 10), SnmpAdminString().subtype(subtypeSpec=ValueSizeConstraint(0, 32))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: cApsConfigFarEndGroupName.setStatus('current')
if mibBuilder.loadTexts: cApsConfigFarEndGroupName.setDescription("The value specified in this object applies when the value of cApsStatusMessageTransport is 'dcc', 'ip', or 'osc'. APS messages, used to support bidirectional or linear operation, can be sent out-of-band over an IP network. In this case, this object is used to specify the a textual name for the APS group at the far-end to which the message is being sent. ")
cApsConfigFarEndIpAddressType = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 10, 72, 1, 2, 1, 11), InetAddressType().clone('ipv4')).setMaxAccess("readcreate")
if mibBuilder.loadTexts: cApsConfigFarEndIpAddressType.setStatus('current')
if mibBuilder.loadTexts: cApsConfigFarEndIpAddressType.setDescription("This object can be set only when the value of cApsConfigMessageTransport is 'ip'. This object specifies the type of IP address defined in cApsConfigFarEndIpAddress. ")
cApsConfigFarEndIpAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 10, 72, 1, 2, 1, 12), InetAddress()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: cApsConfigFarEndIpAddress.setStatus('current')
if mibBuilder.loadTexts: cApsConfigFarEndIpAddress.setDescription("This object can be set only when the value of cApsConfigMessageTransport is 'ip'. This object specifies the IP address of the far end, which is used as the destination address in APS messages transmitted by this network element. ")
cApsStatusExtTable = MibTable((1, 3, 6, 1, 4, 1, 9, 10, 72, 1, 3), )
if mibBuilder.loadTexts: cApsStatusExtTable.setStatus('current')
if mibBuilder.loadTexts: cApsStatusExtTable.setDescription('This table augments the cApsStatusTable. ')
cApsStatusExtEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9, 10, 72, 1, 3, 1), )
cApsStatusEntry.registerAugmentions(("CISCO-APS-EXT-MIB", "cApsStatusExtEntry"))
cApsStatusExtEntry.setIndexNames(*cApsStatusEntry.getIndexNames())
if mibBuilder.loadTexts: cApsStatusExtEntry.setStatus('current')
if mibBuilder.loadTexts: cApsStatusExtEntry.setDescription('A conceptual row in the cApsStatusExtTable. ')
cApsStatusCdlApsBytesRcv = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 10, 72, 1, 3, 1, 1), CdlApsBytes()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cApsStatusCdlApsBytesRcv.setStatus('current')
if mibBuilder.loadTexts: cApsStatusCdlApsBytesRcv.setDescription('The current value of the APS bytes received on the protection channel. This object applies only to CDL interfaces. This is equivalent to cApsStatusK1K2Rcv for SONET. ')
cApsStatusCdlApsBytesTrans = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 10, 72, 1, 3, 1, 2), CdlApsBytes()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cApsStatusCdlApsBytesTrans.setStatus('current')
if mibBuilder.loadTexts: cApsStatusCdlApsBytesTrans.setDescription('The current value of the APS bytes transmitted on the protection channel. This object applies only to CDL interfaces. This is equivalent to cApsStatusK1K2Trans for SONET. ')
cApsStatusMessageTransport = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 10, 72, 1, 3, 1, 3), CApsMessageTransport()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cApsStatusMessageTransport.setStatus('current')
if mibBuilder.loadTexts: cApsStatusMessageTransport.setDescription("This object specifies the type of transport currently being used for exchange of APS protocol messages. The value of this object is the same as the value specified in the cApsConfigMessageTransport object, except when the value of that object is 'autoSelect'. In that case, the type of transport that has been automatically selected is indicated by this object. ")
cApsChanStatusExtTable = MibTable((1, 3, 6, 1, 4, 1, 9, 10, 72, 1, 4), )
if mibBuilder.loadTexts: cApsChanStatusExtTable.setStatus('current')
if mibBuilder.loadTexts: cApsChanStatusExtTable.setDescription('This table augments the cApsChanStatusTable. ')
cApsChanStatusExtEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9, 10, 72, 1, 4, 1), )
cApsChanStatusEntry.registerAugmentions(("CISCO-APS-EXT-MIB", "cApsChanStatusExtEntry"))
cApsChanStatusExtEntry.setIndexNames(*cApsChanStatusEntry.getIndexNames())
if mibBuilder.loadTexts: cApsChanStatusExtEntry.setStatus('current')
if mibBuilder.loadTexts: cApsChanStatusExtEntry.setDescription('A conceptual row in the cApsChanStatusExtTable. ')
cApsChanStatusExtRequest = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 10, 72, 1, 4, 1, 1), CApsK1K2()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cApsChanStatusExtRequest.setStatus('current')
if mibBuilder.loadTexts: cApsChanStatusExtRequest.setDescription("The highest priority local request for a channel in an APS group. This object uses only the 'Type of Request' part (bits 1-4) of the K1 byte. ")
cApsChanConfigExtTable = MibTable((1, 3, 6, 1, 4, 1, 9, 10, 72, 1, 5), )
if mibBuilder.loadTexts: cApsChanConfigExtTable.setStatus('current')
if mibBuilder.loadTexts: cApsChanConfigExtTable.setDescription('This table augments the cApsChanConfigTable. ')
cApsChanConfigExtEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9, 10, 72, 1, 5, 1), )
cApsChanConfigEntry.registerAugmentions(("CISCO-APS-EXT-MIB", "cApsChanConfigExtEntry"))
cApsChanConfigExtEntry.setIndexNames(*cApsChanConfigEntry.getIndexNames())
if mibBuilder.loadTexts: cApsChanConfigExtEntry.setStatus('current')
if mibBuilder.loadTexts: cApsChanConfigExtEntry.setDescription('A conceptual row in the cApsChanConfigExtTable. ')
cApsChanConfigReflectorMode = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 10, 72, 1, 5, 1, 1), TruthValue()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cApsChanConfigReflectorMode.setStatus('current')
if mibBuilder.loadTexts: cApsChanConfigReflectorMode.setDescription('Indicates whether the channel is in reflector mode or not. Reflector mode establishes a communication channel between the local PTE and the remote PTE at the other end of the SONET path. This object has a value of true(1), if reflector mode is configured and a value of false(2), if the reflector mode is not configured on the channel. ')
cApsChanAssociationTable = MibTable((1, 3, 6, 1, 4, 1, 9, 10, 72, 1, 6), )
if mibBuilder.loadTexts: cApsChanAssociationTable.setStatus('current')
if mibBuilder.loadTexts: cApsChanAssociationTable.setDescription('This table lists the configured IP address of the protect/working interfaces. ')
cApsChanAssociationEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9, 10, 72, 1, 6, 1), ).setIndexNames((0, "CISCO-APS-EXT-MIB", "cApsChanAssociationGroupName"), (0, "CISCO-APS-EXT-MIB", "cApsChanAssociationNumber"), (0, "CISCO-APS-EXT-MIB", "cApsChanAssociationMapNumber"))
if mibBuilder.loadTexts: cApsChanAssociationEntry.setStatus('current')
if mibBuilder.loadTexts: cApsChanAssociationEntry.setDescription('A conceptual row in cApsChanAssociationTable. ')
cApsChanAssociationGroupName = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 10, 72, 1, 6, 1, 1), SnmpAdminString().subtype(subtypeSpec=ValueSizeConstraint(1, 32)))
if mibBuilder.loadTexts: cApsChanAssociationGroupName.setStatus('current')
if mibBuilder.loadTexts: cApsChanAssociationGroupName.setDescription('A textual name for the APS group which this channel is included in. ')
cApsChanAssociationNumber = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 10, 72, 1, 6, 1, 2), CApsChannelConfigNumber())
if mibBuilder.loadTexts: cApsChanAssociationNumber.setStatus('current')
if mibBuilder.loadTexts: cApsChanAssociationNumber.setDescription('This field is set to a unique working/protection channel number within an APS group. The value 0 indicates the null channel. The values 1-14 define a working channel. ')
cApsChanAssociationMapNumber = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 10, 72, 1, 6, 1, 3), CApsChannelConfigNumber())
if mibBuilder.loadTexts: cApsChanAssociationMapNumber.setStatus('current')
if mibBuilder.loadTexts: cApsChanAssociationMapNumber.setDescription('This field is set to the associated working/protection channel number corresponding to the field cApsChanAssociationNumber within an APS group. The value 0 indicates the null channel. The values 1-14 define a working channel. ')
cApsChanAssociationIpAddressType = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 10, 72, 1, 6, 1, 4), InetAddressType()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cApsChanAssociationIpAddressType.setStatus('current')
if mibBuilder.loadTexts: cApsChanAssociationIpAddressType.setDescription(' This object specifies the type of IP address defined in cApsChanAssociationIpAddress. ')
cApsChanAssociationIpAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 10, 72, 1, 6, 1, 5), InetAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cApsChanAssociationIpAddress.setStatus('current')
if mibBuilder.loadTexts: cApsChanAssociationIpAddress.setDescription('IP Address of the working/protection channel. If cApsChanAssociationNumber represents a working channel number, this object indicates the IP Address of the associated protection channel. If cApsChanAssociationNumber represents a protection channel number, this object indicates the IP Address of the associated working channel. ')
cApsExtGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 10, 72, 2, 1))
cApsExtCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 10, 72, 2, 2))
cApsExtCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 9, 10, 72, 2, 2, 1)).setObjects(("CISCO-APS-EXT-MIB", "cApsNotifiesEnableGroup"), ("CISCO-APS-EXT-MIB", "cApsConfigPathExt"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cApsExtCompliance = cApsExtCompliance.setStatus('deprecated')
if mibBuilder.loadTexts: cApsExtCompliance.setDescription('The compliance statement for augmented APS groups.')
cApsExtCompliance2 = ModuleCompliance((1, 3, 6, 1, 4, 1, 9, 10, 72, 2, 2, 2)).setObjects(("CISCO-APS-EXT-MIB", "cApsNotifiesEnableGroup"), ("CISCO-APS-EXT-MIB", "cApsConfigPathExt"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cApsExtCompliance2 = cApsExtCompliance2.setStatus('current')
if mibBuilder.loadTexts: cApsExtCompliance2.setDescription('The compliance statement for augmented APS groups.')
cApsExtComplianceRev1 = ModuleCompliance((1, 3, 6, 1, 4, 1, 9, 10, 72, 2, 2, 3)).setObjects(("CISCO-APS-EXT-MIB", "cApsChanConfigExt"), ("CISCO-APS-EXT-MIB", "cApsChanAssociationGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cApsExtComplianceRev1 = cApsExtComplianceRev1.setStatus('current')
if mibBuilder.loadTexts: cApsExtComplianceRev1.setDescription('The compliance statement for augmented APS groups. ')
cApsNotifiesEnableGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 10, 72, 2, 1, 1)).setObjects(("CISCO-APS-EXT-MIB", "cApsNotifiesEnable"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cApsNotifiesEnableGroup = cApsNotifiesEnableGroup.setStatus('current')
if mibBuilder.loadTexts: cApsNotifiesEnableGroup.setDescription('A managed object that controls the generation of APS-related notifications defined in the CISCO-APS-MIB. ')
cApsConfigPathExt = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 10, 72, 2, 1, 2)).setObjects(("CISCO-APS-EXT-MIB", "cApsConfigSpan"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cApsConfigPathExt = cApsConfigPathExt.setStatus('current')
if mibBuilder.loadTexts: cApsConfigPathExt.setDescription('An augmentation to cApsConfigTable objects providing configuration information applicable to path APS architectures. ')
cApsConfigYcableExt = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 10, 72, 2, 1, 3)).setObjects(("CISCO-APS-EXT-MIB", "cApsConfigYcable"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cApsConfigYcableExt = cApsConfigYcableExt.setStatus('current')
if mibBuilder.loadTexts: cApsConfigYcableExt.setDescription('An augmentation to cApsConfigTable objects providing configuration information applicable to APS groups when Y cable protection is supported. ')
cApsConfigSearchExt = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 10, 72, 2, 1, 4)).setObjects(("CISCO-APS-EXT-MIB", "cApsConfigMinSearchUpInterval"), ("CISCO-APS-EXT-MIB", "cApsConfigMaxSearchUpInterval"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cApsConfigSearchExt = cApsConfigSearchExt.setStatus('current')
if mibBuilder.loadTexts: cApsConfigSearchExt.setDescription('An augmentation to cApsConfigTable objects providing configuration information applicable to APS groups in which the standby interface is not monitored. ')
cApsStatusCdlExt = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 10, 72, 2, 1, 5)).setObjects(("CISCO-APS-EXT-MIB", "cApsStatusCdlApsBytesRcv"), ("CISCO-APS-EXT-MIB", "cApsStatusCdlApsBytesTrans"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cApsStatusCdlExt = cApsStatusCdlExt.setStatus('current')
if mibBuilder.loadTexts: cApsStatusCdlExt.setDescription('An augmentation to cApsStatusTable objects providing status information applicable to APS groups for CDL. ')
cApsConfigSwitchoverTimerExt = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 10, 72, 2, 1, 6)).setObjects(("CISCO-APS-EXT-MIB", "cApsConfigSwitchoverEnableInterval"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cApsConfigSwitchoverTimerExt = cApsConfigSwitchoverTimerExt.setStatus('current')
if mibBuilder.loadTexts: cApsConfigSwitchoverTimerExt.setDescription('An augmentation to cApsConfigTable objects providing configuration information to prevent quick successive switchovers. ')
cApsConfigMessageExt = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 10, 72, 2, 1, 7)).setObjects(("CISCO-APS-EXT-MIB", "cApsConfigMessageTransport"), ("CISCO-APS-EXT-MIB", "cApsConfigMessageHolddown"), ("CISCO-APS-EXT-MIB", "cApsConfigMessageHolddownCount"), ("CISCO-APS-EXT-MIB", "cApsConfigMessageMaxInterval"), ("CISCO-APS-EXT-MIB", "cApsConfigFarEndGroupName"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cApsConfigMessageExt = cApsConfigMessageExt.setStatus('current')
if mibBuilder.loadTexts: cApsConfigMessageExt.setDescription('An augmentation to cApsConfigTable objects providing configuration information applicable to message transport used to exchange APS protocol messages. ')
cApsConfigIPExt = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 10, 72, 2, 1, 8)).setObjects(("CISCO-APS-EXT-MIB", "cApsConfigFarEndIpAddressType"), ("CISCO-APS-EXT-MIB", "cApsConfigFarEndIpAddress"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cApsConfigIPExt = cApsConfigIPExt.setStatus('current')
if mibBuilder.loadTexts: cApsConfigIPExt.setDescription('An augmentation to cApsConfigTable objects providing configuration information applicable to APS groups communicating over IP. ')
cApsStatusMessageExt = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 10, 72, 2, 1, 9)).setObjects(("CISCO-APS-EXT-MIB", "cApsStatusMessageTransport"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cApsStatusMessageExt = cApsStatusMessageExt.setStatus('current')
if mibBuilder.loadTexts: cApsStatusMessageExt.setDescription('An augmentation to cApsStatusTable objects providing status information applicable to message transport used to exchange APS protocol messages. ')
cApsChanStatusRequestExt = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 10, 72, 2, 1, 10)).setObjects(("CISCO-APS-EXT-MIB", "cApsChanStatusExtRequest"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cApsChanStatusRequestExt = cApsChanStatusRequestExt.setStatus('current')
if mibBuilder.loadTexts: cApsChanStatusRequestExt.setDescription('An augmentation to cApsChanStatusTable objects providing additional status information for channels in APS groups. ')
cApsChanConfigExt = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 10, 72, 2, 1, 11)).setObjects(("CISCO-APS-EXT-MIB", "cApsChanConfigReflectorMode"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cApsChanConfigExt = cApsChanConfigExt.setStatus('current')
if mibBuilder.loadTexts: cApsChanConfigExt.setDescription('An augmentation to cApsChanConfigTable objects providing configuration information of channels in APS groups. ')
cApsChanAssociationGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 10, 72, 2, 1, 12)).setObjects(("CISCO-APS-EXT-MIB", "cApsChanAssociationIpAddressType"), ("CISCO-APS-EXT-MIB", "cApsChanAssociationIpAddress"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cApsChanAssociationGroup = cApsChanAssociationGroup.setStatus('current')
if mibBuilder.loadTexts: cApsChanAssociationGroup.setDescription('cApsChanAssociationTable object provides for all protection/working channels, the associated working/protection channel IP address.')
mibBuilder.exportSymbols("CISCO-APS-EXT-MIB", cApsStatusExtTable=cApsStatusExtTable, cApsChanConfigExtTable=cApsChanConfigExtTable, cApsChanAssociationGroupName=cApsChanAssociationGroupName, cApsConfigSpan=cApsConfigSpan, cApsConfigExtEntry=cApsConfigExtEntry, cApsConfigYcableExt=cApsConfigYcableExt, cApsConfigSwitchoverEnableInterval=cApsConfigSwitchoverEnableInterval, cApsConfigFarEndIpAddressType=cApsConfigFarEndIpAddressType, cApsConfigMaxSearchUpInterval=cApsConfigMaxSearchUpInterval, cApsChanStatusRequestExt=cApsChanStatusRequestExt, cApsConfigFarEndIpAddress=cApsConfigFarEndIpAddress, cApsExtCompliances=cApsExtCompliances, cApsNotifiesEnable=cApsNotifiesEnable, cApsStatusCdlExt=cApsStatusCdlExt, cApsChanConfigReflectorMode=cApsChanConfigReflectorMode, cApsChanAssociationTable=cApsChanAssociationTable, cApsChanAssociationEntry=cApsChanAssociationEntry, cApsConfigMinSearchUpInterval=cApsConfigMinSearchUpInterval, cApsConfigMessageMaxInterval=cApsConfigMessageMaxInterval, cApsExtMIBObjects=cApsExtMIBObjects, cApsChanAssociationNumber=cApsChanAssociationNumber, cApsExtMIB=cApsExtMIB, cApsExtComplianceRev1=cApsExtComplianceRev1, cApsChanConfigExt=cApsChanConfigExt, cApsChanStatusExtRequest=cApsChanStatusExtRequest, cApsConfigExtTable=cApsConfigExtTable, cApsChanStatusExtTable=cApsChanStatusExtTable, cApsExtCompliance=cApsExtCompliance, cApsExtCompliance2=cApsExtCompliance2, cApsConfigSwitchoverTimerExt=cApsConfigSwitchoverTimerExt, cApsConfigMessageExt=cApsConfigMessageExt, cApsConfigMessageHolddown=cApsConfigMessageHolddown, cApsChanAssociationMapNumber=cApsChanAssociationMapNumber, cApsConfigFarEndGroupName=cApsConfigFarEndGroupName, cApsChanAssociationIpAddress=cApsChanAssociationIpAddress, cApsConfigIPExt=cApsConfigIPExt, cApsConfigPathExt=cApsConfigPathExt, cApsStatusMessageTransport=cApsStatusMessageTransport, cApsExtMIBConformance=cApsExtMIBConformance, cApsExtGroups=cApsExtGroups, cApsConfigYcable=cApsConfigYcable, cApsChanAssociationIpAddressType=cApsChanAssociationIpAddressType, CApsChannelConfigNumber=CApsChannelConfigNumber, cApsNotifiesEnableGroup=cApsNotifiesEnableGroup, PYSNMP_MODULE_ID=cApsExtMIB, CdlApsBytes=CdlApsBytes, cApsChanAssociationGroup=cApsChanAssociationGroup, cApsChanStatusExtEntry=cApsChanStatusExtEntry, cApsStatusMessageExt=cApsStatusMessageExt, cApsChanConfigExtEntry=cApsChanConfigExtEntry, cApsConfigSearchExt=cApsConfigSearchExt, cApsStatusExtEntry=cApsStatusExtEntry, cApsStatusCdlApsBytesRcv=cApsStatusCdlApsBytesRcv, cApsConfigMessageTransport=cApsConfigMessageTransport, cApsStatusCdlApsBytesTrans=cApsStatusCdlApsBytesTrans, cApsConfigMessageHolddownCount=cApsConfigMessageHolddownCount, CApsMessageTransport=CApsMessageTransport)
