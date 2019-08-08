#
# PySNMP MIB module CISCO-WIRELESS-NOTIFICATION-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/CISCO-WIRELESS-NOTIFICATION-MIB
# Produced by pysmi-0.3.4 at Wed May  1 12:21:19 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, SingleValueConstraint, ValueSizeConstraint, ConstraintsUnion, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "SingleValueConstraint", "ValueSizeConstraint", "ConstraintsUnion", "ConstraintsIntersection")
ciscoMgmt, = mibBuilder.importSymbols("CISCO-SMI", "ciscoMgmt")
CiscoAlarmSeverity, = mibBuilder.importSymbols("CISCO-TC", "CiscoAlarmSeverity")
InetAddress, InetAddressType = mibBuilder.importSymbols("INET-ADDRESS-MIB", "InetAddress", "InetAddressType")
SnmpAdminString, = mibBuilder.importSymbols("SNMP-FRAMEWORK-MIB", "SnmpAdminString")
ModuleCompliance, ObjectGroup, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "ObjectGroup", "NotificationGroup")
ModuleIdentity, TimeTicks, Gauge32, ObjectIdentity, iso, Bits, IpAddress, Counter32, NotificationType, Integer32, MibScalar, MibTable, MibTableRow, MibTableColumn, MibIdentifier, Unsigned32, Counter64 = mibBuilder.importSymbols("SNMPv2-SMI", "ModuleIdentity", "TimeTicks", "Gauge32", "ObjectIdentity", "iso", "Bits", "IpAddress", "Counter32", "NotificationType", "Integer32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "MibIdentifier", "Unsigned32", "Counter64")
TruthValue, DateAndTime, DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "TruthValue", "DateAndTime", "DisplayString", "TextualConvention")
ciscoWirelessNotificationMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 9, 712))
ciscoWirelessNotificationMIB.setRevisions(('2011-06-06 00:00', '2010-09-15 00:00', '2009-10-28 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: ciscoWirelessNotificationMIB.setRevisionsDescriptions(("Adding a new enumeration type 'ncs' to CWirelessNotificationCategory object. Changing 'WCS' to 'NCS'", "Adding a new enumeration type 'switch' to CWirelessNotificationCategory object.", 'Initial version of this MIB module.',))
if mibBuilder.loadTexts: ciscoWirelessNotificationMIB.setLastUpdated('201106060000Z')
if mibBuilder.loadTexts: ciscoWirelessNotificationMIB.setOrganization('Cisco Systems, Inc.')
if mibBuilder.loadTexts: ciscoWirelessNotificationMIB.setContactInfo('Cisco Systems Customer Service Postal: 170 W Tasman Drive San Jose, CA 95134 USA Tel: +1 800 553-NETS E-mail: cs-wnbu-snmp@cisco.com')
if mibBuilder.loadTexts: ciscoWirelessNotificationMIB.setDescription("This MIB is intended to be implemented on those Network Management applications that manage a network of wireless devices through the Controller and send relevant management information to Northbound Operation Support Systems. The Northbound OSS, with the information received shall present a consolidated view of the whole network of wireless devices. The NM learns the status of the managed devices from the Controller through interfaces like the SNMP, and raises events. Depending upon the event severity, alerts are raised for the events. The alert/event information is sent to the Northbound OSS in the form of SNMP Notifications. This MIB defines these Notifications. The MIB objects cWNotificationDescription, cWNotificationSpecialAttributes and cWNotificationVirtualDomains have been defined to have a maximum size of 1024. The bigger size is required for the following reasons. 1. If the size is reduced, the information intended to be sent to the Northbound applications will be truncated / lost. 2. Networks using UDP are better in handling fragmentation than before. 3. In case if the implementation is used in those networks that can't handle Notifications of a larger size, the intent is to suggest the use of the TCP as the transport protocol for SNMP as against the UDP. 4. The respective objects may not have the maximum defined range at all the times. The higher range is just to accommodate those cases where the size can hit the maximum value. The relationships between NCS, CC, AP, MN and Mgmt-Appl can be depicted as follows : +................+ +................+ + + + + + NB OSS 1 + .. + NB OSS n + + + + + +................+ +................+ ^ ^ . . . . Notifications . . . +..........+ + + + NCS + + + +..........+ ^ ^ ^ . . . SNMP . . . . . . . . . +......+ +......+ +......+ + + + + + + + CC + + CC + + CC + + + + + + + +......+ +......+ +......+ .. . . . . . . . . . . . . . . . . . . +......+ +......+ +......+ +......+ + + + + + + + + + AP + + AP + + AP + + AP + + + + + + + + + +......+ +......+ +......+ +......+ . . . . . . . . . . . . . . . . . . . +......+ +......+ +......+ +......+ + + + + + + + + + MN + + MN + + MN + + MN + + + + + + + + + +......+ +......+ +......+ +......+ GLOSSARY Access Point ( AP ) An entity that contains an 802.11 medium access control (MAC) and physical layer (PHY) interface and provides access to the distribution services via the wireless medium for associated clients. LWAPP APs encapsulate all the 802.11 frames in LWAPP frames and sends it to the Controller to which it is logically connected to. Alert An alert is an NM response to one or more related Events from Managed Object. If the Event learnt is severe enough to let the user know about, the NM raises an alert i.e if event has one of the following severity critical, major, minor or warning. One or more Events can result in a single alert being raised. Central Controller ( CC ) The central entity that terminates the LWAPP protocol tunnel from the LWAPP APs. Throughout this MIB, this entity is also referred to as 'Controller'. Event An Event is an occurrence or detection of some condition in and around the network. Event can be generated by the NM corresponding to traps received or through polling the managed object. Light Weight Access Point Protocol ( LWAPP ) This is a generic protocol that defines the communication between the Access Points and the Controllers. Managed Object Managed Objects are used to represent those entities being managed by the NM. It could be an AP, WLAN, Controller or an MN. Mobile Node ( MN ) Mobile Nodes are roaming 802.11 wireless devices that would associate to an AP to get their uplink to the wired network. Mobile Nodes are also known as clients. Network Management Application ( NM ) Application which manages network of managed objects using SNMP. It provides network management functions of FCAPS - Fault, Configuration, Accounting, Performance and Security to manage the network. Notification NM application like NCS sends Notifications defined through this MIB, corresponding to their Alerts and Events to a Northbound OSS to provide a consolidated view. Operations Support Systems ( OSS ) Management applications in the network that receive Notifications from NM (like NCS) and provide consolidated view of the whole network of wireless devices. Received Signal Strength Indicator ( RSSI ) A measure of the strength of the signal as observed by the entity that received it, expressed in 'dbm'. Signal-Noise Ratio ( SNR ) A measure of the quality of the signal relative to the strength of noise expressed in 'dB'. Virtual Domain A NM's Virtual Domain is a logical grouping that consists of a set of managed objects like Controllers, APs, WLANs, maps etc. It restricts a user's view to information relevant to these managed objects. Through a virtual domain, an administrator can ensure that users are only able to view the managed objects and maps for which they are responsible. A managed object can belong to more than one virtual domain. Network Control System ( NCS ) Network Control System (NCS) is a converged platform for wired, wireless, and security policy management in a single solution for faster troubleshooting and more efficient network operations. Wireless LAN ( WLAN ) A WLAN refers to the network of IEEE 802.11 complaint wireless devices within mutual communication range of each other via the wireless medium. REFERENCE [1] Wireless LAN Medium Access Control (MAC) and Physical Layer (PHY) Specifications. [2] IEEE 802.11 - The original 1 Mbit/s and 2 Mbit/s, 2.4 GHz RF and IR standard.")
class CWirelessNotificationType(TextualConvention, Integer32):
    description = 'This textual convention defines the different Notification types. Unknown : This indicates an unknown Notification type. Alert : This indicates that the Notification is generated due to an Alert generated by a set of Events. Event : This indicates that the Notification is generated due to an Event related to a Managed Object. The Event can be raised through polling the Managed Object, receiving SNMP Notifications from the Managed Object etc.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3))
    namedValues = NamedValues(("unknown", 1), ("alert", 2), ("event", 3))

class CWirelessNotificationCategory(TextualConvention, Integer32):
    description = "This textual convention defines the different Notification categories. The semantics are as follows. 'unknown' This indicates an unknown category. 'accessPoints' The Notification is associated with APs. 'adhocRogue' The Notification is associated with adhoc rogue APs. 'clients' The Notification is associated with client/mobile nodes. 'controllers' The Notification is associated with Controllers. 'coverageHole' The Notification is associated with holes in radio coverage. 'contextAwareNotifications' The Notification is associated with Alerts generated by location service for Event definitions configured on the MSE like containment,chokepoint etc. 'interference' The Notification is associated with interference in radio coverage by APs. 'meshLinks' The Notification is associated with mesh wireless networks. 'mobilityService' The Notification is associated with MSE status. 'performance' The Notification is associated with wireless network performance. 'rogueAP' The Notification is associated with rogue APs detected in the network. 'rrm' The Notification is associated to radio resource management. 'security' The Notification is associated with security of wireless networks. 'wcs' The Notification is associated with WCS. 'switch' The Notification is associated with Ethernet switch. 'ncs' The Notification is associated with NCS."
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17))
    namedValues = NamedValues(("unknown", 1), ("accessPoints", 2), ("adhocRogue", 3), ("clients", 4), ("controllers", 5), ("coverageHole", 6), ("interference", 7), ("contextAwareNotifications", 8), ("meshLinks", 9), ("mobilityService", 10), ("performance", 11), ("rogueAP", 12), ("rrm", 13), ("security", 14), ("wcs", 15), ("switch", 16), ("ncs", 17))

ciscoWirelessNotificationMIBNotifs = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 712, 0))
ciscoWirelessNotificationMIBObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 712, 1))
ciscoWirelessNotificationMIBConform = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 712, 2))
cWNotificationData = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 712, 1, 1))
cwNotificationHistoryTableMaxLength = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 712, 1, 1, 1), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(1, 4294967295)).clone(100)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cwNotificationHistoryTableMaxLength.setStatus('current')
if mibBuilder.loadTexts: cwNotificationHistoryTableMaxLength.setDescription('This object represents the maximum number of entries permissible in cwNotificationHistoryTable. When user sets this to a lower value, for example from 100 to 50, entries corresponding to older Notifications will be deleted to adjust to the new setting.')
cwNotificationHistoryTable = MibTable((1, 3, 6, 1, 4, 1, 9, 9, 712, 1, 1, 2), )
if mibBuilder.loadTexts: cwNotificationHistoryTable.setStatus('current')
if mibBuilder.loadTexts: cwNotificationHistoryTable.setDescription('This table represents the information about the Notifications sent by the NM to Northbound applications. The Notification fields are populated from the corresponding Alert/Event.Whenever the NM sends a Notification to one of the Northbound applications, a row will be added to this table. When the number of maximum allowed of entries is decreased through cwNotificationHistoryTableMaxLength, the least recent entries will be deleted.')
cwNotificationHistoryEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9, 9, 712, 1, 1, 2, 1), ).setIndexNames((0, "CISCO-WIRELESS-NOTIFICATION-MIB", "cWNotificationIndex"))
if mibBuilder.loadTexts: cwNotificationHistoryEntry.setStatus('current')
if mibBuilder.loadTexts: cwNotificationHistoryEntry.setDescription('Each entry represents a conceptual row in cwNotificationHistoryTable and corresponds to the information about a Notification sent by the NM to Northbound applications.')
cWNotificationIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 712, 1, 1, 2, 1, 1), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(1, 4294967295)))
if mibBuilder.loadTexts: cWNotificationIndex.setStatus('current')
if mibBuilder.loadTexts: cWNotificationIndex.setDescription('This object represents a monotonically increasing integer that uniquely identifies the information about the Notification. When the maximum value defined by cwNotificationHistoryTableMaxLength is reached, the value wraps back to 1.')
cWNotificationTimestamp = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 712, 1, 1, 2, 1, 2), DateAndTime()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cWNotificationTimestamp.setStatus('current')
if mibBuilder.loadTexts: cWNotificationTimestamp.setDescription('This object in the Notification represents the time when the corresponding Alert/Event was raised by the NM for a particular condition in the network.')
cWNotificationUpdatedTimestamp = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 712, 1, 1, 2, 1, 3), DateAndTime()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cWNotificationUpdatedTimestamp.setStatus('current')
if mibBuilder.loadTexts: cWNotificationUpdatedTimestamp.setDescription('This object in the Notification represents the time when Alert was last updated. Alerts persist over time and it is possible that their field(s) get changed. For example, when severity changes from a higher level (ex critical to major or major to minor or minor to clear), then the severity field gets updated. This object represents the time when it happened. This object will not be populated for Events.')
cWNotificationKey = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 712, 1, 1, 2, 1, 4), SnmpAdminString().subtype(subtypeSpec=ValueSizeConstraint(1, 255))).setMaxAccess("readonly")
if mibBuilder.loadTexts: cWNotificationKey.setStatus('current')
if mibBuilder.loadTexts: cWNotificationKey.setDescription('This object represents the entity string that describes the network condition identified by cwNotificationType for which this Notification is generated.')
cWNotificationCategory = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 712, 1, 1, 2, 1, 5), CWirelessNotificationCategory()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cWNotificationCategory.setStatus('current')
if mibBuilder.loadTexts: cWNotificationCategory.setDescription('This object represents the category of the network condition represented by cwNotificationType for which this Notification is generated.')
cWNotificationSubCategory = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 712, 1, 1, 2, 1, 6), OctetString().subtype(subtypeSpec=ValueSizeConstraint(1, 256))).setMaxAccess("readonly")
if mibBuilder.loadTexts: cWNotificationSubCategory.setStatus('current')
if mibBuilder.loadTexts: cWNotificationSubCategory.setDescription('This object represents the sub category of the network condition identified by cwNotificationType for which this Notification is generated. This object can be used to further filter down Alert/Event under a particular category.')
cWNotificationManagedObjectAddressType = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 712, 1, 1, 2, 1, 7), InetAddressType()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cWNotificationManagedObjectAddressType.setStatus('current')
if mibBuilder.loadTexts: cWNotificationManagedObjectAddressType.setDescription('This object represents the type of the Internet network address made available through cWNotificationManagedObjectAddress.')
cWNotificationManagedObjectAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 712, 1, 1, 2, 1, 8), InetAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cWNotificationManagedObjectAddress.setStatus('current')
if mibBuilder.loadTexts: cWNotificationManagedObjectAddress.setDescription('This object represents the network address of the Managed Object. The type of the address stored in this object is determined by the cWNotificationManagedObjectAddressType object.')
cWNotificationSourceDisplayName = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 712, 1, 1, 2, 1, 9), OctetString().subtype(subtypeSpec=ValueSizeConstraint(1, 256))).setMaxAccess("readonly")
if mibBuilder.loadTexts: cWNotificationSourceDisplayName.setStatus('current')
if mibBuilder.loadTexts: cWNotificationSourceDisplayName.setDescription('This object represents the display name for the source that triggered the network condition represented by cwNotificationType for which this Notification is generated.')
cWNotificationDescription = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 712, 1, 1, 2, 1, 10), OctetString().subtype(subtypeSpec=ValueSizeConstraint(1, 1024))).setMaxAccess("readonly")
if mibBuilder.loadTexts: cWNotificationDescription.setStatus('current')
if mibBuilder.loadTexts: cWNotificationDescription.setDescription("This object represents a detailed description of the network condition represented by cwNotificationType for which this Notification is generated. For example, rogueAp Alert is described as follows, 'Rogue AP '00:1b:2b:35:6a:f3' is removed; it was detected as Rogue AP by AP 'test_1' Radio Type '802.11b''.")
cWNotificationSeverity = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 712, 1, 1, 2, 1, 11), CiscoAlarmSeverity()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cWNotificationSeverity.setStatus('current')
if mibBuilder.loadTexts: cWNotificationSeverity.setDescription('This object represents the severity of the network condition represented by cwNotificationType for which this Notification is generated.')
cWNotificationSpecialAttributes = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 712, 1, 1, 2, 1, 12), OctetString().subtype(subtypeSpec=ValueSizeConstraint(1, 1024))).setMaxAccess("readonly")
if mibBuilder.loadTexts: cWNotificationSpecialAttributes.setStatus('current')
if mibBuilder.loadTexts: cWNotificationSpecialAttributes.setDescription("This object represents the specialized attributes required to describe the network condition identified by cWNotificationType. These include SNR, RSSI, channel information etc. This value is formatted as 'name=value' pairs in CSV format. For example, rogueAP Alert's special attributes are sent as 'detectingAPRadioType=a0,YCoordinate=0, state=11, rogueApType=0, spt Status=0, ssId=wpspsk, on80211A=0, numOfDetectingAps=0, on80211B=1, XCoordinate=0, classificationType=3, channelNumber=6, containmentLevel=0, rssi=-51, rogueApMacAddr=00:1b:2b:35:6a:f3, onNetwork=0, total RogueClients=0'. This string can be parsed to get different name-value pairs.")
cWNotificationType = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 712, 1, 1, 2, 1, 13), CWirelessNotificationType()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cWNotificationType.setStatus('current')
if mibBuilder.loadTexts: cWNotificationType.setDescription('This object represents the type of this Notification. This basically indicates the trigger that has caused the NM to generate this Notification.')
cWNotificationVirtualDomains = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 712, 1, 1, 2, 1, 14), OctetString().subtype(subtypeSpec=ValueSizeConstraint(1, 1024))).setMaxAccess("readonly")
if mibBuilder.loadTexts: cWNotificationVirtualDomains.setStatus('current')
if mibBuilder.loadTexts: cWNotificationVirtualDomains.setDescription("This object represents the name of one or multiple virtual domains(comma separated) the source of the network condition represented by cWNotificationType is logically assigned to. For example, 'root, California, San Jose' indicates that the source of the network condition is logically assigned to these multiple virtual domains.")
cwNotificationMOStatusEnable = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 712, 1, 1, 3), TruthValue().clone('true')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cwNotificationMOStatusEnable.setStatus('current')
if mibBuilder.loadTexts: cwNotificationMOStatusEnable.setDescription("This object is to control the generation of ciscoWirelessMOStatusNotification. A value of 'true' indicates that the NM generates ciscoWirelessMOStatusNotification Notification. A value of 'false' indicates that the NM does not generate ciscoWirelessMOStatusNotification Notification.")
ciscoWirelessMOStatusNotification = NotificationType((1, 3, 6, 1, 4, 1, 9, 9, 712, 0, 1)).setObjects(("CISCO-WIRELESS-NOTIFICATION-MIB", "cWNotificationTimestamp"), ("CISCO-WIRELESS-NOTIFICATION-MIB", "cWNotificationUpdatedTimestamp"), ("CISCO-WIRELESS-NOTIFICATION-MIB", "cWNotificationKey"), ("CISCO-WIRELESS-NOTIFICATION-MIB", "cWNotificationCategory"), ("CISCO-WIRELESS-NOTIFICATION-MIB", "cWNotificationSubCategory"), ("CISCO-WIRELESS-NOTIFICATION-MIB", "cWNotificationManagedObjectAddressType"), ("CISCO-WIRELESS-NOTIFICATION-MIB", "cWNotificationManagedObjectAddress"), ("CISCO-WIRELESS-NOTIFICATION-MIB", "cWNotificationSourceDisplayName"), ("CISCO-WIRELESS-NOTIFICATION-MIB", "cWNotificationDescription"), ("CISCO-WIRELESS-NOTIFICATION-MIB", "cWNotificationSeverity"), ("CISCO-WIRELESS-NOTIFICATION-MIB", "cWNotificationSpecialAttributes"), ("CISCO-WIRELESS-NOTIFICATION-MIB", "cWNotificationVirtualDomains"))
if mibBuilder.loadTexts: ciscoWirelessMOStatusNotification.setStatus('current')
if mibBuilder.loadTexts: ciscoWirelessMOStatusNotification.setDescription('This Notification is generated by the NM in response to an Alert or Event related to a network device managed by it.')
ciscoWirelessNotificationMIBCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 712, 2, 1))
ciscoWirelessNotificationMIBGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 712, 2, 2))
ciscoWirelessNotificationMIBCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 9, 9, 712, 2, 1, 1)).setObjects(("CISCO-WIRELESS-NOTIFICATION-MIB", "ciscoWirelessNotificationObjectsGroup"), ("CISCO-WIRELESS-NOTIFICATION-MIB", "ciscoWirelessNotificationsGroup"), ("CISCO-WIRELESS-NOTIFICATION-MIB", "ciscoWirelessNotificationConfigGroup"), ("CISCO-WIRELESS-NOTIFICATION-MIB", "ciscoWirelessNotificationEnableGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoWirelessNotificationMIBCompliance = ciscoWirelessNotificationMIBCompliance.setStatus('current')
if mibBuilder.loadTexts: ciscoWirelessNotificationMIBCompliance.setDescription('The compliance statement for the SNMP entities which implement the CISCO-WIRELESS-NOTIFICATION-MIB.')
ciscoWirelessNotificationConfigGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 712, 2, 2, 1)).setObjects(("CISCO-WIRELESS-NOTIFICATION-MIB", "cwNotificationHistoryTableMaxLength"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoWirelessNotificationConfigGroup = ciscoWirelessNotificationConfigGroup.setStatus('current')
if mibBuilder.loadTexts: ciscoWirelessNotificationConfigGroup.setDescription('This collection of objects is used to manage the information about Notifications.')
ciscoWirelessNotificationsGroup = NotificationGroup((1, 3, 6, 1, 4, 1, 9, 9, 712, 2, 2, 2)).setObjects(("CISCO-WIRELESS-NOTIFICATION-MIB", "ciscoWirelessMOStatusNotification"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoWirelessNotificationsGroup = ciscoWirelessNotificationsGroup.setStatus('current')
if mibBuilder.loadTexts: ciscoWirelessNotificationsGroup.setDescription('This collection of objects represent the Notifications generated by the NM.')
ciscoWirelessNotificationObjectsGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 712, 2, 2, 3)).setObjects(("CISCO-WIRELESS-NOTIFICATION-MIB", "cWNotificationTimestamp"), ("CISCO-WIRELESS-NOTIFICATION-MIB", "cWNotificationUpdatedTimestamp"), ("CISCO-WIRELESS-NOTIFICATION-MIB", "cWNotificationKey"), ("CISCO-WIRELESS-NOTIFICATION-MIB", "cWNotificationCategory"), ("CISCO-WIRELESS-NOTIFICATION-MIB", "cWNotificationSubCategory"), ("CISCO-WIRELESS-NOTIFICATION-MIB", "cWNotificationManagedObjectAddressType"), ("CISCO-WIRELESS-NOTIFICATION-MIB", "cWNotificationManagedObjectAddress"), ("CISCO-WIRELESS-NOTIFICATION-MIB", "cWNotificationSourceDisplayName"), ("CISCO-WIRELESS-NOTIFICATION-MIB", "cWNotificationDescription"), ("CISCO-WIRELESS-NOTIFICATION-MIB", "cWNotificationSeverity"), ("CISCO-WIRELESS-NOTIFICATION-MIB", "cWNotificationSpecialAttributes"), ("CISCO-WIRELESS-NOTIFICATION-MIB", "cWNotificationType"), ("CISCO-WIRELESS-NOTIFICATION-MIB", "cWNotificationVirtualDomains"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoWirelessNotificationObjectsGroup = ciscoWirelessNotificationObjectsGroup.setStatus('current')
if mibBuilder.loadTexts: ciscoWirelessNotificationObjectsGroup.setDescription('This collection of objects provide the information about the Notifications generated by the NM.')
ciscoWirelessNotificationEnableGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 712, 2, 2, 4)).setObjects(("CISCO-WIRELESS-NOTIFICATION-MIB", "cwNotificationMOStatusEnable"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoWirelessNotificationEnableGroup = ciscoWirelessNotificationEnableGroup.setStatus('current')
if mibBuilder.loadTexts: ciscoWirelessNotificationEnableGroup.setDescription('This collection of objects is used to control the generation of Notifications.')
mibBuilder.exportSymbols("CISCO-WIRELESS-NOTIFICATION-MIB", cwNotificationHistoryTable=cwNotificationHistoryTable, cwNotificationHistoryTableMaxLength=cwNotificationHistoryTableMaxLength, ciscoWirelessNotificationMIBObjects=ciscoWirelessNotificationMIBObjects, cWNotificationSubCategory=cWNotificationSubCategory, ciscoWirelessNotificationMIB=ciscoWirelessNotificationMIB, ciscoWirelessNotificationMIBGroups=ciscoWirelessNotificationMIBGroups, CWirelessNotificationCategory=CWirelessNotificationCategory, ciscoWirelessNotificationMIBCompliance=ciscoWirelessNotificationMIBCompliance, cWNotificationSourceDisplayName=cWNotificationSourceDisplayName, cWNotificationTimestamp=cWNotificationTimestamp, cWNotificationSpecialAttributes=cWNotificationSpecialAttributes, ciscoWirelessNotificationObjectsGroup=ciscoWirelessNotificationObjectsGroup, cWNotificationData=cWNotificationData, cWNotificationIndex=cWNotificationIndex, cWNotificationSeverity=cWNotificationSeverity, CWirelessNotificationType=CWirelessNotificationType, ciscoWirelessNotificationMIBConform=ciscoWirelessNotificationMIBConform, ciscoWirelessMOStatusNotification=ciscoWirelessMOStatusNotification, cWNotificationCategory=cWNotificationCategory, cWNotificationKey=cWNotificationKey, cwNotificationMOStatusEnable=cwNotificationMOStatusEnable, PYSNMP_MODULE_ID=ciscoWirelessNotificationMIB, ciscoWirelessNotificationsGroup=ciscoWirelessNotificationsGroup, cWNotificationManagedObjectAddress=cWNotificationManagedObjectAddress, cWNotificationUpdatedTimestamp=cWNotificationUpdatedTimestamp, cWNotificationManagedObjectAddressType=cWNotificationManagedObjectAddressType, cwNotificationHistoryEntry=cwNotificationHistoryEntry, cWNotificationDescription=cWNotificationDescription, cWNotificationVirtualDomains=cWNotificationVirtualDomains, ciscoWirelessNotificationMIBNotifs=ciscoWirelessNotificationMIBNotifs, ciscoWirelessNotificationConfigGroup=ciscoWirelessNotificationConfigGroup, ciscoWirelessNotificationEnableGroup=ciscoWirelessNotificationEnableGroup, ciscoWirelessNotificationMIBCompliances=ciscoWirelessNotificationMIBCompliances, cWNotificationType=cWNotificationType)