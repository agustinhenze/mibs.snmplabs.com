#
# PySNMP MIB module BAY-STACK-LINK-STATE-TRACKING-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/BAY-STACK-LINK-STATE-TRACKING-MIB
# Produced by pysmi-0.3.4 at Wed May  1 11:35:36 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, ValueSizeConstraint, ConstraintsUnion, ConstraintsIntersection, SingleValueConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "ValueSizeConstraint", "ConstraintsUnion", "ConstraintsIntersection", "SingleValueConstraint")
ifIndex, = mibBuilder.importSymbols("IF-MIB", "ifIndex")
PortList, = mibBuilder.importSymbols("Q-BRIDGE-MIB", "PortList")
IdList, = mibBuilder.importSymbols("RAPID-CITY", "IdList")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
ObjectIdentity, NotificationType, MibScalar, MibTable, MibTableRow, MibTableColumn, Bits, Unsigned32, iso, Integer32, Counter32, Gauge32, IpAddress, Counter64, MibIdentifier, TimeTicks, ModuleIdentity = mibBuilder.importSymbols("SNMPv2-SMI", "ObjectIdentity", "NotificationType", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Bits", "Unsigned32", "iso", "Integer32", "Counter32", "Gauge32", "IpAddress", "Counter64", "MibIdentifier", "TimeTicks", "ModuleIdentity")
DisplayString, TextualConvention, TruthValue = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention", "TruthValue")
bayStackMibs, = mibBuilder.importSymbols("SYNOPTICS-ROOT-MIB", "bayStackMibs")
bayStackLinkStateTrackingMib = ModuleIdentity((1, 3, 6, 1, 4, 1, 45, 5, 43))
bayStackLinkStateTrackingMib.setRevisions(('2013-10-11 00:00', '2013-02-13 00:00', '2012-11-15 00:00', '2012-10-17 00:00', '2012-09-03 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: bayStackLinkStateTrackingMib.setRevisionsDescriptions(('Ver 5: Changed the MAX-ACCESS of bsLstGroupIndex to read-only.', 'Ver 4: Added a new line at the end of the file', 'Ver 3: Changed bsLstGroupUpstreamMltList and bsLstGroupDownstreamMltList objects description.', 'Ver 2: Added bsLstInterfaceStatusChanged, bsLstGroupOperStateChanged.', 'Ver 1: Initial version.',))
if mibBuilder.loadTexts: bayStackLinkStateTrackingMib.setLastUpdated('201310110000Z')
if mibBuilder.loadTexts: bayStackLinkStateTrackingMib.setOrganization('Avaya')
if mibBuilder.loadTexts: bayStackLinkStateTrackingMib.setContactInfo('avaya.com')
if mibBuilder.loadTexts: bayStackLinkStateTrackingMib.setDescription('This MIB module is used for Link State Tracking configuration. The purpose of Link-state tracking feature is to bind the link state of multiple interfaces, by creating link-state groups with upstream and downstream interfaces.')
bsLstNotifications = MibIdentifier((1, 3, 6, 1, 4, 1, 45, 5, 43, 0))
bsLstObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 45, 5, 43, 1))
bsLstScalars = MibIdentifier((1, 3, 6, 1, 4, 1, 45, 5, 43, 1, 1))
bsLstNotifObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 45, 5, 43, 1, 3))
bsLstInterfaceStatus = MibScalar((1, 3, 6, 1, 4, 1, 45, 5, 43, 1, 3, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("up", 1), ("down", 2)))).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: bsLstInterfaceStatus.setStatus('current')
if mibBuilder.loadTexts: bsLstInterfaceStatus.setDescription('This object specifies the status of a physical or logical interface.')
bsLstGroupTable = MibTable((1, 3, 6, 1, 4, 1, 45, 5, 43, 1, 2), )
if mibBuilder.loadTexts: bsLstGroupTable.setStatus('current')
if mibBuilder.loadTexts: bsLstGroupTable.setDescription('This table is used to configure link-state tracking group settings.')
bsLstGroupEntry = MibTableRow((1, 3, 6, 1, 4, 1, 45, 5, 43, 1, 2, 1), ).setIndexNames((0, "BAY-STACK-LINK-STATE-TRACKING-MIB", "bsLstGroupIndex"))
if mibBuilder.loadTexts: bsLstGroupEntry.setStatus('current')
if mibBuilder.loadTexts: bsLstGroupEntry.setDescription('An entry for this instance of bsLstGroupTable.')
bsLstGroupIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 45, 5, 43, 1, 2, 1, 1), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(1, 2))).setMaxAccess("readonly")
if mibBuilder.loadTexts: bsLstGroupIndex.setStatus('current')
if mibBuilder.loadTexts: bsLstGroupIndex.setDescription('The link-state tracking group id.')
bsLstGroupEnabled = MibTableColumn((1, 3, 6, 1, 4, 1, 45, 5, 43, 1, 2, 1, 2), TruthValue().clone('false')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: bsLstGroupEnabled.setStatus('current')
if mibBuilder.loadTexts: bsLstGroupEnabled.setDescription('This object controls whether this link-state tracking group is enabled.')
bsLstGroupUpstreamPortList = MibTableColumn((1, 3, 6, 1, 4, 1, 45, 5, 43, 1, 2, 1, 3), PortList().clone(hexValue="")).setMaxAccess("readwrite")
if mibBuilder.loadTexts: bsLstGroupUpstreamPortList.setStatus('current')
if mibBuilder.loadTexts: bsLstGroupUpstreamPortList.setDescription('This object specifies the upstream port list for this group instance.')
bsLstGroupDownstreamPortList = MibTableColumn((1, 3, 6, 1, 4, 1, 45, 5, 43, 1, 2, 1, 4), PortList().clone(hexValue="")).setMaxAccess("readwrite")
if mibBuilder.loadTexts: bsLstGroupDownstreamPortList.setStatus('current')
if mibBuilder.loadTexts: bsLstGroupDownstreamPortList.setDescription('This object specifies the downstream port list for this group instance.')
bsLstGroupUpstreamMltList = MibTableColumn((1, 3, 6, 1, 4, 1, 45, 5, 43, 1, 2, 1, 5), IdList().clone(hexValue="")).setMaxAccess("readwrite")
if mibBuilder.loadTexts: bsLstGroupUpstreamMltList.setStatus('current')
if mibBuilder.loadTexts: bsLstGroupUpstreamMltList.setDescription('This object specifies the upstream mlt list for this group instance. Each MLT ID is stored as a two bytes value. The first byte in the pair holds bits 15-8 of the MLT ID, while the second byte holds bits 7-0 of the MLT ID.')
bsLstGroupDownstreamMltList = MibTableColumn((1, 3, 6, 1, 4, 1, 45, 5, 43, 1, 2, 1, 6), IdList().clone(hexValue="")).setMaxAccess("readwrite")
if mibBuilder.loadTexts: bsLstGroupDownstreamMltList.setStatus('current')
if mibBuilder.loadTexts: bsLstGroupDownstreamMltList.setDescription('This object specifies the downstream mlt list for this group instance. Each MLT ID is stored as a two bytes value. The first byte in the pair holds bits 15-8 of the MLT ID, while the second byte holds bits 7-0 of the MLT ID.')
bsLstGroupOperState = MibTableColumn((1, 3, 6, 1, 4, 1, 45, 5, 43, 1, 2, 1, 7), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("up", 1), ("down", 2), ("notConfigured", 3)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: bsLstGroupOperState.setStatus('current')
if mibBuilder.loadTexts: bsLstGroupOperState.setDescription("This object specifies the operational status of this group instance. When this link-state tracking group is disabled, the value of this object must be 'notConfigured(3)'.")
bsLstInterfaceStatusChanged = NotificationType((1, 3, 6, 1, 4, 1, 45, 5, 43, 0, 1)).setObjects(("IF-MIB", "ifIndex"), ("BAY-STACK-LINK-STATE-TRACKING-MIB", "bsLstInterfaceStatus"), ("BAY-STACK-LINK-STATE-TRACKING-MIB", "bsLstGroupIndex"))
if mibBuilder.loadTexts: bsLstInterfaceStatusChanged.setStatus('current')
if mibBuilder.loadTexts: bsLstInterfaceStatusChanged.setDescription('This notification is generated when a physical or logical interface changes its status in a particular link-state tracking group.')
bsLstGroupOperStateChanged = NotificationType((1, 3, 6, 1, 4, 1, 45, 5, 43, 0, 2)).setObjects(("IF-MIB", "ifIndex"), ("BAY-STACK-LINK-STATE-TRACKING-MIB", "bsLstInterfaceStatus"), ("BAY-STACK-LINK-STATE-TRACKING-MIB", "bsLstGroupOperState"))
if mibBuilder.loadTexts: bsLstGroupOperStateChanged.setStatus('current')
if mibBuilder.loadTexts: bsLstGroupOperStateChanged.setDescription('This notification is generated when the operational status of a link-state tracking group changes due to an interface status change. For example, when the last interface of an link-state tracking group becomes down, the operational status of the group changes to down.')
mibBuilder.exportSymbols("BAY-STACK-LINK-STATE-TRACKING-MIB", bsLstGroupUpstreamPortList=bsLstGroupUpstreamPortList, bsLstGroupEntry=bsLstGroupEntry, bsLstInterfaceStatusChanged=bsLstInterfaceStatusChanged, bsLstGroupOperStateChanged=bsLstGroupOperStateChanged, bsLstObjects=bsLstObjects, bsLstGroupOperState=bsLstGroupOperState, PYSNMP_MODULE_ID=bayStackLinkStateTrackingMib, bsLstGroupEnabled=bsLstGroupEnabled, bsLstGroupUpstreamMltList=bsLstGroupUpstreamMltList, bsLstGroupDownstreamMltList=bsLstGroupDownstreamMltList, bsLstScalars=bsLstScalars, bsLstGroupTable=bsLstGroupTable, bsLstGroupIndex=bsLstGroupIndex, bsLstNotifications=bsLstNotifications, bsLstInterfaceStatus=bsLstInterfaceStatus, bayStackLinkStateTrackingMib=bayStackLinkStateTrackingMib, bsLstGroupDownstreamPortList=bsLstGroupDownstreamPortList, bsLstNotifObjects=bsLstNotifObjects)
