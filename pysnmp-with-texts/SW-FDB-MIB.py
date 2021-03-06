#
# PySNMP MIB module SW-FDB-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/SW-FDB-MIB
# Produced by pysmi-0.3.4 at Wed May  1 15:12:32 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
OctetString, ObjectIdentifier, Integer = mibBuilder.importSymbols("ASN1", "OctetString", "ObjectIdentifier", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsUnion, ValueRangeConstraint, ValueSizeConstraint, ConstraintsIntersection, SingleValueConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "ValueRangeConstraint", "ValueSizeConstraint", "ConstraintsIntersection", "SingleValueConstraint")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
ObjectIdentity, IpAddress, Bits, iso, MibIdentifier, enterprises, Counter64, NotificationType, Gauge32, Counter32, MibScalar, MibTable, MibTableRow, MibTableColumn, ModuleIdentity, TimeTicks, Integer32, Unsigned32 = mibBuilder.importSymbols("SNMPv2-SMI", "ObjectIdentity", "IpAddress", "Bits", "iso", "MibIdentifier", "enterprises", "Counter64", "NotificationType", "Gauge32", "Counter32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "ModuleIdentity", "TimeTicks", "Integer32", "Unsigned32")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
class MacAddress(OctetString):
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(6, 6)
    fixedLength = 6

class PortList(OctetString):
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(4, 4)
    fixedLength = 4

marconi = MibIdentifier((1, 3, 6, 1, 4, 1, 326))
systems = MibIdentifier((1, 3, 6, 1, 4, 1, 326, 2))
external = MibIdentifier((1, 3, 6, 1, 4, 1, 326, 2, 20))
dlink = MibIdentifier((1, 3, 6, 1, 4, 1, 326, 2, 20, 1))
dlinkcommon = MibIdentifier((1, 3, 6, 1, 4, 1, 326, 2, 20, 1, 1))
golf = MibIdentifier((1, 3, 6, 1, 4, 1, 326, 2, 20, 1, 2))
golfproducts = MibIdentifier((1, 3, 6, 1, 4, 1, 326, 2, 20, 1, 2, 1))
es2000 = MibIdentifier((1, 3, 6, 1, 4, 1, 326, 2, 20, 1, 2, 1, 3))
golfcommon = MibIdentifier((1, 3, 6, 1, 4, 1, 326, 2, 20, 1, 2, 2))
marconi_mgmt = MibIdentifier((1, 3, 6, 1, 4, 1, 326, 2, 20, 1, 2, 2, 2)).setLabel("marconi-mgmt")
es2000Mgmt = MibIdentifier((1, 3, 6, 1, 4, 1, 326, 2, 20, 1, 2, 2, 2, 28))
swL2Mgmt = MibIdentifier((1, 3, 6, 1, 4, 1, 326, 2, 20, 1, 2, 2, 2, 28, 2))
swFDB = MibIdentifier((1, 3, 6, 1, 4, 1, 326, 2, 20, 1, 2, 2, 2, 28, 2, 9))
endOfMIB = MibScalar((1, 3, 6, 1, 4, 1, 326, 2, 20, 1, 2, 2, 2, 28, 9999), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: endOfMIB.setStatus('optional')
swFdbStaticTable = MibTable((1, 3, 6, 1, 4, 1, 326, 2, 20, 1, 2, 2, 2, 28, 2, 9, 1), )
if mibBuilder.loadTexts: swFdbStaticTable.setStatus('mandatory')
if mibBuilder.loadTexts: swFdbStaticTable.setDescription('This table defines for frames with specific destincation MAC address, the set of ports that the frame will be forwarded to. Note that if a MAC address appears in this table also appears in the filter table, the filter table has higher priority over than this table. See swFdbFilterTable description.')
swFdbStaticEntry = MibTableRow((1, 3, 6, 1, 4, 1, 326, 2, 20, 1, 2, 2, 2, 28, 2, 9, 1, 1), ).setIndexNames((0, "SW-FDB-MIB", "swFdbStaticVid"), (0, "SW-FDB-MIB", "swFdbStaticAddress"))
if mibBuilder.loadTexts: swFdbStaticEntry.setStatus('mandatory')
if mibBuilder.loadTexts: swFdbStaticEntry.setDescription('A list of information specifies which ports the frames with specific destination MAC address to go.')
swFdbStaticVid = MibTableColumn((1, 3, 6, 1, 4, 1, 326, 2, 20, 1, 2, 2, 2, 28, 2, 9, 1, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: swFdbStaticVid.setStatus('mandatory')
if mibBuilder.loadTexts: swFdbStaticVid.setDescription('This object indicates the VLAN-ID. If the swVlanInfoStatus is port-base mode, the object ranges from 1 to 12. If VLAN is in mac-based mode or disabled, the object indicates the default VLAN-ID(0).')
swFdbStaticAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 326, 2, 20, 1, 2, 2, 2, 28, 2, 9, 1, 1, 2), MacAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: swFdbStaticAddress.setStatus('mandatory')
if mibBuilder.loadTexts: swFdbStaticAddress.setDescription('The MAC address which this forwarding entry applied. It can be an unicast address or a multicast address.')
swFdbStaticPortMap = MibTableColumn((1, 3, 6, 1, 4, 1, 326, 2, 20, 1, 2, 2, 2, 28, 2, 9, 1, 1, 3), PortList()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: swFdbStaticPortMap.setStatus('mandatory')
if mibBuilder.loadTexts: swFdbStaticPortMap.setDescription("The set of ports to which frames received containing the value of swFdbStaticAddress as the DA, are allowed to be forwarded. Each octet within the value of this object specifies a set of eight ports, with the first octet specifying ports 1 through 8, the second octet specifying ports 9 through 16, etc. Within each octet, the most significant bit represents the lowest numbered port, and the least significant bit represents the highest numbered port. Thus, each port of the bridge is represented by a single bit within the value of this object. If that bit has a value of '1' then that port is included in the set of ports; the port is not included if its bit has a value of '0'.(Note that the setting of the bit corresponding to the port from which a frame is received is irrelevant.)")
swFdbStaticState = MibTableColumn((1, 3, 6, 1, 4, 1, 326, 2, 20, 1, 2, 2, 2, 28, 2, 9, 1, 1, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("other", 1), ("invalid", 2), ("valid", 3)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: swFdbStaticState.setStatus('mandatory')
if mibBuilder.loadTexts: swFdbStaticState.setDescription('This object indicates the status of this entry. other(1) - This entry is currently in use but the conditions under which it will remain so are different from each of the following values. invalid(2) - Writing this value to the object, and then the corresponding entry will be removed from the table. valid(3) - This entry is reside in the table.')
swFdbStaticStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 326, 2, 20, 1, 2, 2, 2, 28, 2, 9, 1, 1, 5), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("other", 1), ("apply", 2), ("not-apply", 3)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: swFdbStaticStatus.setStatus('mandatory')
if mibBuilder.loadTexts: swFdbStaticStatus.setDescription('This object indicates the status of this entry. other(1) - This entry is currently in use but the conditions under which it will remain so are different from each of the following values. apply(2) - This entry is currently in use and reside in the table. not-apply(3) - This entry is reside in the table but currently not in use due to conflict with filter table.')
swFdbStaticMemberTable = MibTable((1, 3, 6, 1, 4, 1, 326, 2, 20, 1, 2, 2, 2, 28, 2, 9, 2), )
if mibBuilder.loadTexts: swFdbStaticMemberTable.setStatus('mandatory')
if mibBuilder.loadTexts: swFdbStaticMemberTable.setDescription('A list of information provide a different view for those ports where packets from the given Vlan need to be forwarded to.')
swFdbStaticMemberEntry = MibTableRow((1, 3, 6, 1, 4, 1, 326, 2, 20, 1, 2, 2, 2, 28, 2, 9, 2, 1), ).setIndexNames((0, "SW-FDB-MIB", "swFdbStaticMemberVid"), (0, "SW-FDB-MIB", "swFdbStaticMemberAddress"), (0, "SW-FDB-MIB", "swFdbStaticMemberUnitIndex"), (0, "SW-FDB-MIB", "swFdbStaticMemberModuleIndex"), (0, "SW-FDB-MIB", "swFdbStaticMemberPortIndex"))
if mibBuilder.loadTexts: swFdbStaticMemberEntry.setStatus('mandatory')
if mibBuilder.loadTexts: swFdbStaticMemberEntry.setDescription('A list of MIB capability entries supported by this forwarding static table.')
swFdbStaticMemberVid = MibTableColumn((1, 3, 6, 1, 4, 1, 326, 2, 20, 1, 2, 2, 2, 28, 2, 9, 2, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: swFdbStaticMemberVid.setStatus('mandatory')
if mibBuilder.loadTexts: swFdbStaticMemberVid.setDescription('This object indicates the VLAN-ID. If the swVlanInfoStatus is port-base mode, the object ranges from 1 to 12. If VLAN is in mac-based mode or disabled, the object indicates the default VLAN-ID(0).')
swFdbStaticMemberAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 326, 2, 20, 1, 2, 2, 2, 28, 2, 9, 2, 1, 2), MacAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: swFdbStaticMemberAddress.setStatus('mandatory')
if mibBuilder.loadTexts: swFdbStaticMemberAddress.setDescription('The MAC address which this forwarding entry applied. It can be an unicast address or a multicast address.')
swFdbStaticMemberUnitIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 326, 2, 20, 1, 2, 2, 2, 28, 2, 9, 2, 1, 3), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: swFdbStaticMemberUnitIndex.setStatus('mandatory')
if mibBuilder.loadTexts: swFdbStaticMemberUnitIndex.setDescription('Specifies the unit ID where the port is located.')
swFdbStaticMemberModuleIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 326, 2, 20, 1, 2, 2, 2, 28, 2, 9, 2, 1, 4), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: swFdbStaticMemberModuleIndex.setStatus('mandatory')
if mibBuilder.loadTexts: swFdbStaticMemberModuleIndex.setDescription('Specifies the module ID where the port is located.')
swFdbStaticMemberPortIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 326, 2, 20, 1, 2, 2, 2, 28, 2, 9, 2, 1, 5), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: swFdbStaticMemberPortIndex.setStatus('mandatory')
if mibBuilder.loadTexts: swFdbStaticMemberPortIndex.setDescription('Specifies the port index relative to the module.')
swFdbFilterTable = MibTable((1, 3, 6, 1, 4, 1, 326, 2, 20, 1, 2, 2, 2, 28, 2, 9, 3), )
if mibBuilder.loadTexts: swFdbFilterTable.setStatus('mandatory')
if mibBuilder.loadTexts: swFdbFilterTable.setDescription('This table defines information for the device to filter packets with specific MAC address (either as the DA or as the SA). The MAC address can be a unicast address or a multicast address. This table has higher priority than both static FDB table and IGMP table. It means that if a MAC address appears on this table also appears on the static FDB table, the device will use the information provide by this table to process the packet.')
swFdbFilterEntry = MibTableRow((1, 3, 6, 1, 4, 1, 326, 2, 20, 1, 2, 2, 2, 28, 2, 9, 3, 1), ).setIndexNames((0, "SW-FDB-MIB", "swFdbFilterVid"), (0, "SW-FDB-MIB", "swFdbFilterAddress"))
if mibBuilder.loadTexts: swFdbFilterEntry.setStatus('mandatory')
if mibBuilder.loadTexts: swFdbFilterEntry.setDescription('A list of information about a specific unicast/multicast MAC address for which the switch has filtering information.')
swFdbFilterVid = MibTableColumn((1, 3, 6, 1, 4, 1, 326, 2, 20, 1, 2, 2, 2, 28, 2, 9, 3, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: swFdbFilterVid.setStatus('mandatory')
if mibBuilder.loadTexts: swFdbFilterVid.setDescription('This object indicates the VLAN-ID. If the swVlanInfoStatus is port-base mode, the object ranges from 1 to 12. If VLAN is in mac-based mode or disabled, the object indicates the default VLAN-ID(0).')
swFdbFilterAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 326, 2, 20, 1, 2, 2, 2, 28, 2, 9, 3, 1, 2), MacAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: swFdbFilterAddress.setStatus('mandatory')
if mibBuilder.loadTexts: swFdbFilterAddress.setDescription('This object indicates a unicast/multicast MAC address for which the bridge has filtering information.')
swFdbFilterState = MibTableColumn((1, 3, 6, 1, 4, 1, 326, 2, 20, 1, 2, 2, 2, 28, 2, 9, 3, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))).clone(namedValues=NamedValues(("other", 1), ("invalid", 2), ("valid", 3), ("dst-src-addr", 4)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: swFdbFilterState.setStatus('mandatory')
if mibBuilder.loadTexts: swFdbFilterState.setDescription("This object indicates the status of this entry. other(1) - This entry is currently in use but the conditions under which it will remain so are different from each of the following values. invalid(2) - Writing this value to the object, and then the corresponding entry will be removed from the table. valid(3) - Writing this value to the object, and then the corresponding entry will be added into the table. dst-src-addr(4) - Recieved frames's destination address or source address are currently used to be filtered as it meets with the MAC address entry of the table.")
mibBuilder.exportSymbols("SW-FDB-MIB", swL2Mgmt=swL2Mgmt, golf=golf, swFdbStaticMemberVid=swFdbStaticMemberVid, dlink=dlink, systems=systems, golfproducts=golfproducts, es2000Mgmt=es2000Mgmt, PortList=PortList, swFdbStaticMemberAddress=swFdbStaticMemberAddress, swFdbStaticVid=swFdbStaticVid, marconi_mgmt=marconi_mgmt, swFdbFilterVid=swFdbFilterVid, swFdbFilterAddress=swFdbFilterAddress, swFdbStaticMemberTable=swFdbStaticMemberTable, swFDB=swFDB, swFdbStaticMemberEntry=swFdbStaticMemberEntry, swFdbFilterTable=swFdbFilterTable, external=external, endOfMIB=endOfMIB, dlinkcommon=dlinkcommon, swFdbStaticState=swFdbStaticState, swFdbStaticMemberPortIndex=swFdbStaticMemberPortIndex, MacAddress=MacAddress, swFdbStaticAddress=swFdbStaticAddress, swFdbStaticEntry=swFdbStaticEntry, swFdbStaticStatus=swFdbStaticStatus, swFdbStaticPortMap=swFdbStaticPortMap, swFdbStaticMemberModuleIndex=swFdbStaticMemberModuleIndex, swFdbFilterState=swFdbFilterState, swFdbStaticMemberUnitIndex=swFdbStaticMemberUnitIndex, swFdbFilterEntry=swFdbFilterEntry, swFdbStaticTable=swFdbStaticTable, marconi=marconi, es2000=es2000, golfcommon=golfcommon)
