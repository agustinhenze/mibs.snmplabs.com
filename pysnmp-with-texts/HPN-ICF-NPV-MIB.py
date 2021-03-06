#
# PySNMP MIB module HPN-ICF-NPV-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/HPN-ICF-NPV-MIB
# Produced by pysmi-0.3.4 at Wed May  1 13:40:34 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
SingleValueConstraint, ConstraintsIntersection, ValueSizeConstraint, ConstraintsUnion, ValueRangeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "SingleValueConstraint", "ConstraintsIntersection", "ValueSizeConstraint", "ConstraintsUnion", "ValueRangeConstraint")
HpnicfFcVsanIndex, = mibBuilder.importSymbols("HPN-ICF-FC-TC-MIB", "HpnicfFcVsanIndex")
hpnicfSan, hpnicfVsanIndex = mibBuilder.importSymbols("HPN-ICF-VSAN-MIB", "hpnicfSan", "hpnicfVsanIndex")
InterfaceIndex, ifIndex = mibBuilder.importSymbols("IF-MIB", "InterfaceIndex", "ifIndex")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
ModuleIdentity, Counter32, ObjectIdentity, Bits, TimeTicks, Counter64, Unsigned32, MibScalar, MibTable, MibTableRow, MibTableColumn, MibIdentifier, Gauge32, IpAddress, NotificationType, iso, Integer32 = mibBuilder.importSymbols("SNMPv2-SMI", "ModuleIdentity", "Counter32", "ObjectIdentity", "Bits", "TimeTicks", "Counter64", "Unsigned32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "MibIdentifier", "Gauge32", "IpAddress", "NotificationType", "iso", "Integer32")
TextualConvention, DisplayString, TimeStamp, RowStatus = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString", "TimeStamp", "RowStatus")
hpnicfNpv = ModuleIdentity((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 127, 6))
hpnicfNpv.setRevisions(('2013-04-02 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: hpnicfNpv.setRevisionsDescriptions(('Initial version of this MIB module.',))
if mibBuilder.loadTexts: hpnicfNpv.setLastUpdated('201304020000Z')
if mibBuilder.loadTexts: hpnicfNpv.setOrganization('')
if mibBuilder.loadTexts: hpnicfNpv.setContactInfo('')
if mibBuilder.loadTexts: hpnicfNpv.setDescription('This MIB module is for the management of N_Port Virtualization or NPV within the framework of N_Port virtualization(NPV) architecture. N_Port virtualization reduces the number of Fibre Channel domain IDs in SANs(Storage Aera Network). Switches operating in the NPV mode do not join a fabric; rather, they pass traffic between NPV core switch links and end-devices, which eliminates the domain IDs for these edge switches. NPV core switch is a fibre channel edge switch connected to one or more NPV devices.')
class HpnicfNpvIfIndexList(TextualConvention, OctetString):
    description = "This textual convention defines a list of 'ifIndex'. Each 4 octets within this value are combined together to represent the 'ifIndex' of a particular port in the module. For example, the first 4 octets (byte 1, byte 2, byte 3 and byte 4) represent the 'ifIndex' of one interface, while the second 4 octets (byte 5, byte 6, byte 7 and byte 8) represent the 'ifIndex' for another interface in the module, and so on."
    status = 'current'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(4, 65535)

hpnicfNpvMibObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 127, 6, 1))
hpnicfNpvConfiguration = MibIdentifier((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 127, 6, 1, 1))
hpnicfNpvGlobalObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 127, 6, 1, 1, 1))
hpnicfNpvLoadbalanceVsan = MibScalar((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 127, 6, 1, 1, 1, 1), HpnicfFcVsanIndex()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hpnicfNpvLoadbalanceVsan.setStatus('current')
if mibBuilder.loadTexts: hpnicfNpvLoadbalanceVsan.setDescription('Used to trigger a load-banlancing in the specified VSAN (Virtual Storage Area Network). When the hpnicfNpvLoadbalanceVsan is set to a specific VSAN, a disruptive load-balancing process will be initiated in the VSAN so that all nodes in the VSAN will re-login to the core switch. This load-balancing process redistributes downlink traffic across all uplink interfaces for better load balancing, but it causes traffic interruption.')
hpnicfNpvTrafficMapConfigTable = MibTable((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 127, 6, 1, 1, 2), )
if mibBuilder.loadTexts: hpnicfNpvTrafficMapConfigTable.setStatus('current')
if mibBuilder.loadTexts: hpnicfNpvTrafficMapConfigTable.setDescription('A table containing information on the assignment of traffic map interfaces to an interface.')
hpnicfNpvTrafficMapConfigEntry = MibTableRow((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 127, 6, 1, 1, 2, 1), ).setIndexNames((0, "IF-MIB", "ifIndex"), (0, "HPN-ICF-VSAN-MIB", "hpnicfVsanIndex"))
if mibBuilder.loadTexts: hpnicfNpvTrafficMapConfigEntry.setStatus('current')
if mibBuilder.loadTexts: hpnicfNpvTrafficMapConfigEntry.setDescription("An entry in the hpnicfNpvTrafficMapConfigTable. This table contains entries for each of the interfaces which has been assigned a set of interfaces for traffic mapping in the VSAN. Traffic mapping is a technique used in NPV device to restrict the usage of external interface(s) for forwarding the traffic from server interface to the fibre channel fabric. If an interface comes up as a server interface and finds a corresponding entry in this table, then the switch software will assign a valid external interface from this list, if any. Once assigned, that assigned external interface will be used for forwarding the traffic from the server interface to the fibre channel fabric. If an interface comes up as a server interface and finds an entry in this table, but with no valid list of external interfaces, then the switch software keeps the server interface in operationally down state until at least one of the interface in the list becomes a valid external interface. If an interface comes up as a server interface and it can not find an entry in this table, then any of the available external interfaces can be assigned to that server interface. Entries in this table can be created or destroyed via hpnicfNpvTrafficMapRowStatus object. Columnar objects can be modified when the corresponding hpnicfNpvTrafficMapRowStatus is 'active'.")
hpnicfNpvTrafficMapExternalIfIndexList = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 127, 6, 1, 1, 2, 1, 1), HpnicfNpvIfIndexList()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hpnicfNpvTrafficMapExternalIfIndexList.setStatus('current')
if mibBuilder.loadTexts: hpnicfNpvTrafficMapExternalIfIndexList.setDescription('The list of external interfaces which the traffic needs to be mapped to. This object is a list of interfaces presented as an octet string of interface indices or ifindex-es. The list should contain at least one interface and at most all the interfaces in the switch up to 16384 interfaces. The 16384 interfaces max-limit is due to the size of this object. Specifying this object is mandatory for the creation of a row in hpnicfNpvTrafficMapConfigTable.')
hpnicfNpvTrafficMapLastChange = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 127, 6, 1, 1, 2, 1, 2), TimeStamp()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hpnicfNpvTrafficMapLastChange.setStatus('current')
if mibBuilder.loadTexts: hpnicfNpvTrafficMapLastChange.setDescription('The value of sysUpTime at the time of the latest change to this traffic map entry. When there has not been any change to the traffic map entry, the value of this field will be that of the entry creation time.')
hpnicfNpvTrafficMapRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 127, 6, 1, 1, 2, 1, 3), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hpnicfNpvTrafficMapRowStatus.setStatus('current')
if mibBuilder.loadTexts: hpnicfNpvTrafficMapRowStatus.setDescription("The status of this conceptual row. The row can be made 'active' only if value of corresponding instance of hpnicfNpvTrafficMapExternalIfIndexList is provided.")
hpnicfNpvServerIfTable = MibTable((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 127, 6, 1, 1, 3), )
if mibBuilder.loadTexts: hpnicfNpvServerIfTable.setStatus('current')
if mibBuilder.loadTexts: hpnicfNpvServerIfTable.setDescription('This table contains, one entry for each server interface(FC-port configured in F-port mode) in this VSAN in the Fabric element. Each entry contains NPV related information like external interface assigned for the server interface in the VSAN.')
hpnicfNpvServerIfEntry = MibTableRow((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 127, 6, 1, 1, 3, 1), ).setIndexNames((0, "IF-MIB", "ifIndex"), (0, "HPN-ICF-VSAN-MIB", "hpnicfVsanIndex"))
if mibBuilder.loadTexts: hpnicfNpvServerIfEntry.setStatus('current')
if mibBuilder.loadTexts: hpnicfNpvServerIfEntry.setDescription('An entry in the hpnicfNpvServerIfTable, containing NPV related parameters established by a server interface indicated by ifIndex.')
hpnicfNpvExternalIfIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 127, 6, 1, 1, 3, 1, 1), InterfaceIndex()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hpnicfNpvExternalIfIndex.setStatus('current')
if mibBuilder.loadTexts: hpnicfNpvExternalIfIndex.setDescription('This value of this object is the external interface assigned for the server interface associated with the server interface.')
mibBuilder.exportSymbols("HPN-ICF-NPV-MIB", hpnicfNpvTrafficMapConfigEntry=hpnicfNpvTrafficMapConfigEntry, hpnicfNpvTrafficMapRowStatus=hpnicfNpvTrafficMapRowStatus, hpnicfNpvServerIfEntry=hpnicfNpvServerIfEntry, hpnicfNpvGlobalObjects=hpnicfNpvGlobalObjects, hpnicfNpvExternalIfIndex=hpnicfNpvExternalIfIndex, hpnicfNpvTrafficMapExternalIfIndexList=hpnicfNpvTrafficMapExternalIfIndexList, hpnicfNpv=hpnicfNpv, HpnicfNpvIfIndexList=HpnicfNpvIfIndexList, hpnicfNpvServerIfTable=hpnicfNpvServerIfTable, hpnicfNpvTrafficMapLastChange=hpnicfNpvTrafficMapLastChange, hpnicfNpvLoadbalanceVsan=hpnicfNpvLoadbalanceVsan, hpnicfNpvConfiguration=hpnicfNpvConfiguration, hpnicfNpvTrafficMapConfigTable=hpnicfNpvTrafficMapConfigTable, PYSNMP_MODULE_ID=hpnicfNpv, hpnicfNpvMibObjects=hpnicfNpvMibObjects)
