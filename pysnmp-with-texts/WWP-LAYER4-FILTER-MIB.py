#
# PySNMP MIB module WWP-LAYER4-FILTER-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/WWP-LAYER4-FILTER-MIB
# Produced by pysmi-0.3.4 at Wed May  1 15:37:42 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsUnion, ValueRangeConstraint, ValueSizeConstraint, ConstraintsIntersection, SingleValueConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "ValueRangeConstraint", "ValueSizeConstraint", "ConstraintsIntersection", "SingleValueConstraint")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
Gauge32, IpAddress, Integer32, MibScalar, MibTable, MibTableRow, MibTableColumn, TimeTicks, Unsigned32, ModuleIdentity, iso, Counter32, NotificationType, MibIdentifier, Counter64, ObjectIdentity, Bits = mibBuilder.importSymbols("SNMPv2-SMI", "Gauge32", "IpAddress", "Integer32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "TimeTicks", "Unsigned32", "ModuleIdentity", "iso", "Counter32", "NotificationType", "MibIdentifier", "Counter64", "ObjectIdentity", "Bits")
TextualConvention, DisplayString, RowStatus = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString", "RowStatus")
wwpModules, = mibBuilder.importSymbols("WWP-SMI", "wwpModules")
wwpLayer4FilterMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 6141, 2, 52))
wwpLayer4FilterMIB.setRevisions(('2003-04-11 17:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: wwpLayer4FilterMIB.setRevisionsDescriptions(('Initial creation.',))
if mibBuilder.loadTexts: wwpLayer4FilterMIB.setLastUpdated('200304111700Z')
if mibBuilder.loadTexts: wwpLayer4FilterMIB.setOrganization('World Wide Packets, Inc')
if mibBuilder.loadTexts: wwpLayer4FilterMIB.setContactInfo(' Mib Meister Postal: World Wide Packets P.O. Box 950 Veradale, WA 99037 USA Phone: +1 509 242 9000 Email: mib.meister@worldwidepackets.com')
if mibBuilder.loadTexts: wwpLayer4FilterMIB.setDescription('This MIB module defines the mgmt objects to support the layer 4 filtering on the WWP products.')
class PortList(TextualConvention, OctetString):
    description = "Each octet within this value specifies a set of eight ports, with the first octet specifying ports 1 through 8, the second octet specifying ports 9 through 16, etc. Within each octet, the most significant bit represents the lowest numbered port, and the least significant bit represents the highest numbered port. Thus, each port of the bridge is represented by a single bit within the value of this object. If that bit has a value of '1' then that port is included in the set of ports; the port is not included if its bit has a value of '0'."
    status = 'current'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(0, 255)

wwpLayer4FilterMIBObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 6141, 2, 52, 1))
wwpLayer4Filter = MibIdentifier((1, 3, 6, 1, 4, 1, 6141, 2, 52, 1, 1))
wwpLayer4FilterMIBNotificationPrefix = MibIdentifier((1, 3, 6, 1, 4, 1, 6141, 2, 52, 2))
wwpLayer4FilterMIBNotifications = MibIdentifier((1, 3, 6, 1, 4, 1, 6141, 2, 52, 2, 0))
wwpLayer4FilterMIBConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 6141, 2, 52, 3))
wwpLayer4FilterMIBCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 6141, 2, 52, 3, 1))
wwpLayer4FilterMIBGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 6141, 2, 52, 3, 2))
wwpMaxLayer4Filters = MibScalar((1, 3, 6, 1, 4, 1, 6141, 2, 52, 1, 1, 1), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: wwpMaxLayer4Filters.setStatus('current')
if mibBuilder.loadTexts: wwpMaxLayer4Filters.setDescription('The maximum number of Layer4 Filters that this device supports.')
wwpNumLayer4Filters = MibScalar((1, 3, 6, 1, 4, 1, 6141, 2, 52, 1, 1, 2), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: wwpNumLayer4Filters.setStatus('current')
if mibBuilder.loadTexts: wwpNumLayer4Filters.setDescription('The current number of Layer4 Filters that are configured in this device.')
wwpLayer4FilterTable = MibTable((1, 3, 6, 1, 4, 1, 6141, 2, 52, 1, 1, 3), )
if mibBuilder.loadTexts: wwpLayer4FilterTable.setStatus('current')
if mibBuilder.loadTexts: wwpLayer4FilterTable.setDescription('The (conceptual) table listing the config parameters for the Layer 4 filter.')
wwpLayer4FilterEntry = MibTableRow((1, 3, 6, 1, 4, 1, 6141, 2, 52, 1, 1, 3, 1), ).setIndexNames((0, "WWP-LAYER4-FILTER-MIB", "wwpLayer4FilterName"))
if mibBuilder.loadTexts: wwpLayer4FilterEntry.setStatus('current')
if mibBuilder.loadTexts: wwpLayer4FilterEntry.setDescription('An entry (conceptual row) in the wwpLayer4FilterTable.')
wwpLayer4FilterName = MibTableColumn((1, 3, 6, 1, 4, 1, 6141, 2, 52, 1, 1, 3, 1, 1), OctetString().subtype(subtypeSpec=ValueSizeConstraint(1, 32))).setMaxAccess("readonly")
if mibBuilder.loadTexts: wwpLayer4FilterName.setStatus('current')
if mibBuilder.loadTexts: wwpLayer4FilterName.setDescription('The locally arbitrary, but unique identifier associated with this wwpLayer4FilterEntry.')
wwpLayer4FilterProtocolNumber = MibTableColumn((1, 3, 6, 1, 4, 1, 6141, 2, 52, 1, 1, 3, 1, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 65535))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: wwpLayer4FilterProtocolNumber.setReference('RFC 1700')
if mibBuilder.loadTexts: wwpLayer4FilterProtocolNumber.setStatus('current')
if mibBuilder.loadTexts: wwpLayer4FilterProtocolNumber.setDescription('The protocol number for the Layer 4 Filter. The list of protocol numbers are assigned by IANA.')
wwpLayer4FilterSrcPort = MibTableColumn((1, 3, 6, 1, 4, 1, 6141, 2, 52, 1, 1, 3, 1, 3), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 65535))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: wwpLayer4FilterSrcPort.setStatus('current')
if mibBuilder.loadTexts: wwpLayer4FilterSrcPort.setDescription('The traffic addressed to the transport layer source port specified by this object will be blocked by this filter. A zero value for this object will indicate that this object should be ignored while applying the filter.')
wwpLayer4FilterDstPort = MibTableColumn((1, 3, 6, 1, 4, 1, 6141, 2, 52, 1, 1, 3, 1, 4), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 65535))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: wwpLayer4FilterDstPort.setStatus('current')
if mibBuilder.loadTexts: wwpLayer4FilterDstPort.setDescription('The traffic addressed to the transport layer destination port specified by this object will be blocked by this filter. A zero value for this object will indicate that this object should be ignored while applying the filter.')
wwpLayer4FilterStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 6141, 2, 52, 1, 1, 3, 1, 5), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: wwpLayer4FilterStatus.setStatus('current')
if mibBuilder.loadTexts: wwpLayer4FilterStatus.setDescription("Used to manage the creation and deletion of the conceptual rows in this table. To create a row in this table, a manager must set this object to 'createAndGo'. Until instances of all corresponding columns are appropriately configured, the value of the corresponding instance of the wwpLayer4FilterStatus column can't be set to 'active'. In particular, a newly created row cannot be made active until the corresponding instance of wwpLayer4FilterProtocol has been set. None of the objects can be modified while the value of this object is active(1).")
wwpLayer4FilterAttachTable = MibTable((1, 3, 6, 1, 4, 1, 6141, 2, 52, 1, 1, 4), )
if mibBuilder.loadTexts: wwpLayer4FilterAttachTable.setStatus('current')
if mibBuilder.loadTexts: wwpLayer4FilterAttachTable.setDescription('The (conceptual) table listing the attachment of created filters to the VLANs and ports. If there is no entry atached with the filter, then filter is virtually disabled.')
wwpLayer4FilterAttachEntry = MibTableRow((1, 3, 6, 1, 4, 1, 6141, 2, 52, 1, 1, 4, 1), ).setIndexNames((0, "WWP-LAYER4-FILTER-MIB", "wwpLayer4FilterVid"), (0, "WWP-LAYER4-FILTER-MIB", "wwpLayer4FilterName"), (0, "WWP-LAYER4-FILTER-MIB", "wwpLayer4FilterAttachType"))
if mibBuilder.loadTexts: wwpLayer4FilterAttachEntry.setStatus('current')
if mibBuilder.loadTexts: wwpLayer4FilterAttachEntry.setDescription('An entry (conceptual row) in the wwpLayer4FilterAttachTable.')
wwpLayer4FilterVid = MibTableColumn((1, 3, 6, 1, 4, 1, 6141, 2, 52, 1, 1, 4, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 4094))).setMaxAccess("readonly")
if mibBuilder.loadTexts: wwpLayer4FilterVid.setStatus('current')
if mibBuilder.loadTexts: wwpLayer4FilterVid.setDescription('The vlan id to be associated with this ingress filter.')
wwpLayer4FilterAttachType = MibTableColumn((1, 3, 6, 1, 4, 1, 6141, 2, 52, 1, 1, 4, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("deny", 1), ("allow", 2))).clone('deny')).setMaxAccess("readcreate")
if mibBuilder.loadTexts: wwpLayer4FilterAttachType.setStatus('current')
if mibBuilder.loadTexts: wwpLayer4FilterAttachType.setDescription("The attach type for this filter. Setting this object to 'allow' will allow the traffic specified by the filter name.")
wwpLayer4FilterPortList = MibTableColumn((1, 3, 6, 1, 4, 1, 6141, 2, 52, 1, 1, 4, 1, 3), PortList()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: wwpLayer4FilterPortList.setStatus('current')
if mibBuilder.loadTexts: wwpLayer4FilterPortList.setDescription('The set of ports on which this filter is to be applied.')
wwpLayer4FilterCounterId = MibTableColumn((1, 3, 6, 1, 4, 1, 6141, 2, 52, 1, 1, 4, 1, 4), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 15))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: wwpLayer4FilterCounterId.setStatus('current')
if mibBuilder.loadTexts: wwpLayer4FilterCounterId.setDescription('The stats related to this filter will be stored in the counter specified by this object.')
wwpLayer4FilterCount = MibTableColumn((1, 3, 6, 1, 4, 1, 6141, 2, 52, 1, 1, 4, 1, 5), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: wwpLayer4FilterCount.setStatus('current')
if mibBuilder.loadTexts: wwpLayer4FilterCount.setDescription('The stats value in the counter specified by the wwpLayer4FilterCounterId.')
wwpLayer4FilterAttachStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 6141, 2, 52, 1, 1, 4, 1, 6), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: wwpLayer4FilterAttachStatus.setStatus('current')
if mibBuilder.loadTexts: wwpLayer4FilterAttachStatus.setDescription("Used to manage the creation and deletion of the conceptual rows in this table. To create a row in this table, a manager must set this object to 'createAndGo'. Until instances of all corresponding columns are appropriately configured, the value of the corresponding instance of the wwpLayer4FilterStatus column can't be set to 'active'. In particular, a newly created row cannot be made active until the corresponding instance of wwpLayer4FilterPortList has been set. None of the objects can be modified while the value of this object is active(1).")
mibBuilder.exportSymbols("WWP-LAYER4-FILTER-MIB", wwpLayer4FilterDstPort=wwpLayer4FilterDstPort, wwpLayer4FilterTable=wwpLayer4FilterTable, wwpLayer4FilterVid=wwpLayer4FilterVid, wwpLayer4FilterStatus=wwpLayer4FilterStatus, wwpLayer4FilterAttachType=wwpLayer4FilterAttachType, wwpNumLayer4Filters=wwpNumLayer4Filters, wwpLayer4FilterAttachEntry=wwpLayer4FilterAttachEntry, wwpLayer4FilterCount=wwpLayer4FilterCount, wwpMaxLayer4Filters=wwpMaxLayer4Filters, wwpLayer4FilterProtocolNumber=wwpLayer4FilterProtocolNumber, wwpLayer4FilterMIBObjects=wwpLayer4FilterMIBObjects, wwpLayer4FilterEntry=wwpLayer4FilterEntry, wwpLayer4FilterName=wwpLayer4FilterName, wwpLayer4FilterMIBGroups=wwpLayer4FilterMIBGroups, wwpLayer4FilterMIB=wwpLayer4FilterMIB, wwpLayer4FilterAttachStatus=wwpLayer4FilterAttachStatus, wwpLayer4FilterAttachTable=wwpLayer4FilterAttachTable, wwpLayer4FilterMIBNotificationPrefix=wwpLayer4FilterMIBNotificationPrefix, wwpLayer4FilterSrcPort=wwpLayer4FilterSrcPort, wwpLayer4FilterPortList=wwpLayer4FilterPortList, wwpLayer4FilterCounterId=wwpLayer4FilterCounterId, PortList=PortList, wwpLayer4FilterMIBNotifications=wwpLayer4FilterMIBNotifications, wwpLayer4Filter=wwpLayer4Filter, wwpLayer4FilterMIBConformance=wwpLayer4FilterMIBConformance, wwpLayer4FilterMIBCompliances=wwpLayer4FilterMIBCompliances, PYSNMP_MODULE_ID=wwpLayer4FilterMIB)