#
# PySNMP MIB module A3COM-HUAWEI-FCOE-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/A3COM-HUAWEI-FCOE-MIB
# Produced by pysmi-0.3.4 at Wed May  1 11:05:00 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
h3cCommon, = mibBuilder.importSymbols("A3COM-HUAWEI-OID-MIB", "h3cCommon")
OctetString, Integer, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "OctetString", "Integer", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsUnion, ValueSizeConstraint, SingleValueConstraint, ValueRangeConstraint, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "ValueSizeConstraint", "SingleValueConstraint", "ValueRangeConstraint", "ConstraintsIntersection")
fcmInstanceIndex, = mibBuilder.importSymbols("FC-MGMT-MIB", "fcmInstanceIndex")
InterfaceIndexOrZero, InterfaceIndex = mibBuilder.importSymbols("IF-MIB", "InterfaceIndexOrZero", "InterfaceIndex")
VlanIndex, = mibBuilder.importSymbols("Q-BRIDGE-MIB", "VlanIndex")
SnmpAdminString, = mibBuilder.importSymbols("SNMP-FRAMEWORK-MIB", "SnmpAdminString")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
ObjectIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, NotificationType, Integer32, Counter64, Counter32, ModuleIdentity, Unsigned32, iso, MibIdentifier, Gauge32, Bits, IpAddress, TimeTicks = mibBuilder.importSymbols("SNMPv2-SMI", "ObjectIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "NotificationType", "Integer32", "Counter64", "Counter32", "ModuleIdentity", "Unsigned32", "iso", "MibIdentifier", "Gauge32", "Bits", "IpAddress", "TimeTicks")
TruthValue, TimeStamp, DisplayString, MacAddress, RowStatus, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "TruthValue", "TimeStamp", "DisplayString", "MacAddress", "RowStatus", "TextualConvention")
T11FabricIndex, = mibBuilder.importSymbols("T11-TC-MIB", "T11FabricIndex")
h3cFCoE = ModuleIdentity((1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 120))
h3cFCoE.setRevisions(('2012-03-28 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: h3cFCoE.setRevisionsDescriptions(('Initial version of this MIB module.',))
if mibBuilder.loadTexts: h3cFCoE.setLastUpdated('201203280000Z')
if mibBuilder.loadTexts: h3cFCoE.setOrganization('Hangzhou H3C Technologies Co., Ltd.')
if mibBuilder.loadTexts: h3cFCoE.setContactInfo('Platform Team H3C Technologies Co., Ltd. Hai-Dian District Beijing P.R. China http://www.h3c.com Zip: 100085')
if mibBuilder.loadTexts: h3cFCoE.setDescription('This MIB module is for configuring and monitoring Fibre Channel over Ethernet (FCoE) related entities. This MIB defines a Virtual FC (VFC) Interface as an object that represents either a VF_Port or a VE_Port on a FCoE Forwarder (FCF). VFC interfaces can be created either statically (by management request) or dynamically (at the time of FIP based FLOGI or ELP request). Other terminologies used in this MIB are defined by the H3c FCoE standard, as defined in the FC-BB-5 specification. See www.h3c.com for more information. This MIB also supports configuration of the following objects: - Mapping of FCoE VLAN-ID used to carry traffic for a Fabric - FC-MAP value used by the FCF operating in FPMA mode - FIP snooping related objects')
h3cFCoEObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 120, 1))
h3cFCoEConfig = MibIdentifier((1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 120, 1, 1))
h3cFCoEFIPSnoopingObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 120, 1, 2))
class H3cFCoEVfcBindType(TextualConvention, Integer32):
    description = "Defines the different methods to identify (or bind to) - the ENode associated with a particular VF_Port VFC - the remote-FCF associated with a particular VE_Port VFC interfaceIndex(1) - This type is used only when an ENode or remote-FCF is directly connected to the local FCF via one of the local Ethernet interfaces, in which case the value contains the ifIndex of said Ethernet interface. macAddress(2) - This type is used when an ENode or remote-FCF is reachable from the local FCF over a (Layer-2) Ethernet network. A FIP frame from an ENode or remote-FCF is associated to a VFC only if the frame's source MAC address is the same as the MAC Address bound on that VFC."
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2))
    namedValues = NamedValues(("interfaceIndex", 1), ("macAddress", 2))

h3cFCoECfgTable = MibTable((1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 120, 1, 1, 1), )
if mibBuilder.loadTexts: h3cFCoECfgTable.setStatus('current')
if mibBuilder.loadTexts: h3cFCoECfgTable.setDescription('This table facilitates configuration of FCoE parameters on a per Fibre Channel management instance.')
h3cFCoECfgEntry = MibTableRow((1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 120, 1, 1, 1, 1), ).setIndexNames((0, "FC-MGMT-MIB", "fcmInstanceIndex"))
if mibBuilder.loadTexts: h3cFCoECfgEntry.setStatus('current')
if mibBuilder.loadTexts: h3cFCoECfgEntry.setDescription('There is one entry in this table for each Fibre Channel management instance.')
h3cFCoECfgFcmap = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 120, 1, 1, 1, 1, 1), OctetString().subtype(subtypeSpec=ValueSizeConstraint(3, 3)).setFixedLength(3).clone(hexValue="0EFC00")).setMaxAccess("readwrite")
if mibBuilder.loadTexts: h3cFCoECfgFcmap.setReference('Fibre Channel - Backbone - 5 (FC-BB-5), section 7.6 and table 47')
if mibBuilder.loadTexts: h3cFCoECfgFcmap.setStatus('current')
if mibBuilder.loadTexts: h3cFCoECfgFcmap.setDescription('This object configures the FC-MAP value used by the FCF when operating in FPMA mode. The default value is 0EFC00h, as written in the standard.')
h3cFCoECfgDynamicVfcCreation = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 120, 1, 1, 1, 1, 2), TruthValue().clone('false')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: h3cFCoECfgDynamicVfcCreation.setStatus('current')
if mibBuilder.loadTexts: h3cFCoECfgDynamicVfcCreation.setDescription("This object is set to 'true' to enable, or 'false' to disable, the dynamic creation of VFC interfaces on this FCF. When set to 'true', VFC interfaces are dynamically created as and when a FIP-based FLOGI or ELP request is received.")
h3cFCoECfgDefaultFCFPriority = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 120, 1, 1, 1, 1, 3), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(0, 255)).clone(128)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: h3cFCoECfgDefaultFCFPriority.setStatus('current')
if mibBuilder.loadTexts: h3cFCoECfgDefaultFCFPriority.setDescription('The FIP priority value advertised by the FCF to ENodes by default. h3cFCoEStaticVfcFCFPriority configured for a VFC interface overrides this setting for the ENode associated with the VFC.')
h3cFCoECfgDATov = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 120, 1, 1, 1, 1, 4), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(1, 60)).clone(5)).setUnits('seconds').setMaxAccess("readwrite")
if mibBuilder.loadTexts: h3cFCoECfgDATov.setStatus('current')
if mibBuilder.loadTexts: h3cFCoECfgDATov.setDescription('The Discovery_Advertisement_Timeout value configured for the FCF. This is used as the timeout value in seconds by the FCF to send periodic Discovery Advertisements.')
h3cFCoECfgAddressingMode = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 120, 1, 1, 1, 1, 5), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("fpma", 1), ("spma", 2), ("fpmaAndSpma", 3)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: h3cFCoECfgAddressingMode.setStatus('current')
if mibBuilder.loadTexts: h3cFCoECfgAddressingMode.setDescription('Addressing mode(s) supported by the FCF. Implementations should fail SetRequests for unsupported modes.')
h3cFCoEVLANTable = MibTable((1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 120, 1, 1, 2), )
if mibBuilder.loadTexts: h3cFCoEVLANTable.setStatus('current')
if mibBuilder.loadTexts: h3cFCoEVLANTable.setDescription('In fabrics in which VLANs are deployed, this table facilitates configuration of VLAN and Virtual Fabric associations in an FCoE network. In such fabrics, FCoE forwarding for a fabric is over a VLAN in a (Layer-2) Ethernet network. That is, reachability between the ENode/remote-FCF and an FCF for a given fabric is determined by the reachability provided by the Ethernet network on the corresponding VLAN. An active entry in this table indicates which VLAN is used to transport FCoE traffic for a particular Virtual Fabric. If VLANs are not deployed or not enabled, entries in this table are ignored by the bridge. Some implmentations may allow traffic from only one Virtual Fabric to be transported over a given VLAN. Such implementations should prevent multiple entries with the same VLAN-ID from being created in this table. Modifying existing VLAN-Virtual Fabric associations is not possible. The specific row must first be deleted and then a new one created.')
h3cFCoEVLANEntry = MibTableRow((1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 120, 1, 1, 2, 1), ).setIndexNames((0, "FC-MGMT-MIB", "fcmInstanceIndex"), (0, "A3COM-HUAWEI-FCOE-MIB", "h3cFCoEVLANIndex"), (0, "A3COM-HUAWEI-FCOE-MIB", "h3cFCoEFabricIndex"))
if mibBuilder.loadTexts: h3cFCoEVLANEntry.setStatus('current')
if mibBuilder.loadTexts: h3cFCoEVLANEntry.setDescription('There is one entry in this table for each VLAN that is designated to transport FCoE traffic for a given Virtual Fabric.')
h3cFCoEVLANIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 120, 1, 1, 2, 1, 1), VlanIndex())
if mibBuilder.loadTexts: h3cFCoEVLANIndex.setStatus('current')
if mibBuilder.loadTexts: h3cFCoEVLANIndex.setDescription('This object identifies the VLAN-ID that the FCoE FCF function is being enabled for.')
h3cFCoEFabricIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 120, 1, 1, 2, 1, 2), T11FabricIndex())
if mibBuilder.loadTexts: h3cFCoEFabricIndex.setStatus('current')
if mibBuilder.loadTexts: h3cFCoEFabricIndex.setDescription('This object identifies the Fabric Index of the Virtual Fabric traffic which is to be transported over the VLAN identified by h3cFCoEVLANIndex.')
h3cFCoEVLANOperState = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 120, 1, 1, 2, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("up", 1), ("down", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: h3cFCoEVLANOperState.setStatus('current')
if mibBuilder.loadTexts: h3cFCoEVLANOperState.setDescription("Operational state of this VLAN-Virtual Fabric association entry. The 'up' state is achieved when both the Virtual Fabric and VLAN are valid.")
h3cFCoEVLANRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 120, 1, 1, 2, 1, 4), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: h3cFCoEVLANRowStatus.setStatus('current')
if mibBuilder.loadTexts: h3cFCoEVLANRowStatus.setDescription('The status of this conceptual row. The RowStatus becomes active on successful creation of an entry.')
h3cFCoEStaticVfcTable = MibTable((1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 120, 1, 1, 3), )
if mibBuilder.loadTexts: h3cFCoEStaticVfcTable.setStatus('current')
if mibBuilder.loadTexts: h3cFCoEStaticVfcTable.setDescription('This table facilitates the creation and deletion of static VFC interfaces. While VFCs can be dynamically created based on FIP FLOGI/ELP requests, operators may want to associate certain pre-configured policy for a particular ENode or a remote-FCF. In such cases static VFC creation becomes necessary. In addition to being creating, a static VFC also needs to be associated to an ENode or remote-FCF. The VFC binding provides such an associaton. The binding does not need to be specified when the row for a VFC is created, but may be specified later.')
h3cFCoEStaticVfcEntry = MibTableRow((1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 120, 1, 1, 3, 1), ).setIndexNames((0, "FC-MGMT-MIB", "fcmInstanceIndex"), (0, "A3COM-HUAWEI-FCOE-MIB", "h3cFCoEStaticVfcIndex"))
if mibBuilder.loadTexts: h3cFCoEStaticVfcEntry.setStatus('current')
if mibBuilder.loadTexts: h3cFCoEStaticVfcEntry.setDescription('There is one entry in this table for each statically created VFC Interface.')
h3cFCoEStaticVfcIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 120, 1, 1, 3, 1, 1), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(1, 65535)))
if mibBuilder.loadTexts: h3cFCoEStaticVfcIndex.setStatus('current')
if mibBuilder.loadTexts: h3cFCoEStaticVfcIndex.setDescription('This index uniquely identifies a static VFC entry in this table.')
h3cFCoEStaticVfcFCFPriority = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 120, 1, 1, 3, 1, 2), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(0, 255)).clone(128)).setMaxAccess("readcreate")
if mibBuilder.loadTexts: h3cFCoEStaticVfcFCFPriority.setStatus('current')
if mibBuilder.loadTexts: h3cFCoEStaticVfcFCFPriority.setDescription('If this VFC is for a VF_Port this object is used to configure FCF priority to be advertised to the ENode associated with the VFC.')
h3cFCoEStaticVfcBindType = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 120, 1, 1, 3, 1, 3), H3cFCoEVfcBindType()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: h3cFCoEStaticVfcBindType.setStatus('current')
if mibBuilder.loadTexts: h3cFCoEStaticVfcBindType.setDescription('The mechanism to identify the ENode associated with this VFC if it is of type VF_Port or to identify the remote-FCF associated with this VFC if it is of type VE_Port.')
h3cFCoEStaticVfcBindIfIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 120, 1, 1, 3, 1, 4), InterfaceIndexOrZero()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: h3cFCoEStaticVfcBindIfIndex.setStatus('current')
if mibBuilder.loadTexts: h3cFCoEStaticVfcBindIfIndex.setDescription('This object is applicable only when the local FCF is directly connected to an ENode or remote-FCF over a specific Ethernet interface, in which case this object contains the ifIndex of said Ethernet interface. If the ENode or remote-FCF is not directly connected to the FCF, this value of this object is zero.')
h3cFCoEStaticVfcBindMACAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 120, 1, 1, 3, 1, 5), MacAddress()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: h3cFCoEStaticVfcBindMACAddress.setStatus('current')
if mibBuilder.loadTexts: h3cFCoEStaticVfcBindMACAddress.setDescription('This object is applicable when the ENode or remote-FCF to which the local FCF is connected is identified by a MAC address. A FIP frame from a ENode or remote-FCF is associated with this VFC only if the source MAC address in the frame is the same as the value of this object.')
h3cFCoEStaticVfcIfIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 120, 1, 1, 3, 1, 6), InterfaceIndex()).setMaxAccess("readonly")
if mibBuilder.loadTexts: h3cFCoEStaticVfcIfIndex.setStatus('current')
if mibBuilder.loadTexts: h3cFCoEStaticVfcIfIndex.setDescription('The ifIndex of this Virtual FC interface.')
h3cFCoEStaticVfcCreationTime = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 120, 1, 1, 3, 1, 7), TimeStamp()).setMaxAccess("readonly")
if mibBuilder.loadTexts: h3cFCoEStaticVfcCreationTime.setStatus('current')
if mibBuilder.loadTexts: h3cFCoEStaticVfcCreationTime.setDescription("The timestamp of this entry's creation time.")
h3cFCoEStaticVfcFailureCause = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 120, 1, 1, 3, 1, 8), SnmpAdminString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: h3cFCoEStaticVfcFailureCause.setStatus('current')
if mibBuilder.loadTexts: h3cFCoEStaticVfcFailureCause.setDescription('The cause of failure for the last bind operation. This object will be zero length if and only if the bind is successful.')
h3cFCoEStaticVfcRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 120, 1, 1, 3, 1, 9), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: h3cFCoEStaticVfcRowStatus.setStatus('current')
if mibBuilder.loadTexts: h3cFCoEStaticVfcRowStatus.setDescription('The status of this conceptual row. The RowStatus becomes active on successful creation of a VFC. The VFC does not need to be bound for the row to be active, but the VFC must be bound before becoming operational.')
mibBuilder.exportSymbols("A3COM-HUAWEI-FCOE-MIB", h3cFCoEStaticVfcEntry=h3cFCoEStaticVfcEntry, h3cFCoEFabricIndex=h3cFCoEFabricIndex, h3cFCoECfgFcmap=h3cFCoECfgFcmap, h3cFCoE=h3cFCoE, h3cFCoECfgTable=h3cFCoECfgTable, h3cFCoEStaticVfcBindType=h3cFCoEStaticVfcBindType, h3cFCoEConfig=h3cFCoEConfig, h3cFCoECfgDefaultFCFPriority=h3cFCoECfgDefaultFCFPriority, h3cFCoEObjects=h3cFCoEObjects, h3cFCoEStaticVfcFCFPriority=h3cFCoEStaticVfcFCFPriority, h3cFCoECfgAddressingMode=h3cFCoECfgAddressingMode, h3cFCoECfgEntry=h3cFCoECfgEntry, h3cFCoEStaticVfcCreationTime=h3cFCoEStaticVfcCreationTime, h3cFCoEStaticVfcTable=h3cFCoEStaticVfcTable, h3cFCoEFIPSnoopingObjects=h3cFCoEFIPSnoopingObjects, h3cFCoEStaticVfcIfIndex=h3cFCoEStaticVfcIfIndex, h3cFCoEStaticVfcRowStatus=h3cFCoEStaticVfcRowStatus, h3cFCoEVLANRowStatus=h3cFCoEVLANRowStatus, h3cFCoECfgDATov=h3cFCoECfgDATov, h3cFCoEVLANTable=h3cFCoEVLANTable, h3cFCoEVLANOperState=h3cFCoEVLANOperState, h3cFCoEStaticVfcIndex=h3cFCoEStaticVfcIndex, h3cFCoEStaticVfcFailureCause=h3cFCoEStaticVfcFailureCause, h3cFCoEStaticVfcBindMACAddress=h3cFCoEStaticVfcBindMACAddress, H3cFCoEVfcBindType=H3cFCoEVfcBindType, h3cFCoEVLANEntry=h3cFCoEVLANEntry, h3cFCoEStaticVfcBindIfIndex=h3cFCoEStaticVfcBindIfIndex, h3cFCoECfgDynamicVfcCreation=h3cFCoECfgDynamicVfcCreation, h3cFCoEVLANIndex=h3cFCoEVLANIndex, PYSNMP_MODULE_ID=h3cFCoE)