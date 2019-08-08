#
# PySNMP MIB module Juniper-Bridging-Manager-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/Juniper-Bridging-Manager-MIB
# Produced by pysmi-0.3.4 at Wed May  1 14:02:01 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
ObjectIdentifier, Integer, OctetString = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "Integer", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, SingleValueConstraint, ConstraintsUnion, ValueSizeConstraint, ValueRangeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "SingleValueConstraint", "ConstraintsUnion", "ValueSizeConstraint", "ValueRangeConstraint")
juniMibs, = mibBuilder.importSymbols("Juniper-MIBs", "juniMibs")
ModuleCompliance, NotificationGroup, ObjectGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup", "ObjectGroup")
ObjectIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, NotificationType, ModuleIdentity, Integer32, TimeTicks, Counter32, Counter64, Gauge32, Unsigned32, IpAddress, Bits, MibIdentifier, iso = mibBuilder.importSymbols("SNMPv2-SMI", "ObjectIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "NotificationType", "ModuleIdentity", "Integer32", "TimeTicks", "Counter32", "Counter64", "Gauge32", "Unsigned32", "IpAddress", "Bits", "MibIdentifier", "iso")
RowStatus, TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "RowStatus", "TextualConvention", "DisplayString")
juniBridgingMgrMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 4874, 2, 2, 64))
juniBridgingMgrMIB.setRevisions(('2002-10-11 20:25',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: juniBridgingMgrMIB.setRevisionsDescriptions(('Initial version of this MIB module.',))
if mibBuilder.loadTexts: juniBridgingMgrMIB.setLastUpdated('200210112025Z')
if mibBuilder.loadTexts: juniBridgingMgrMIB.setOrganization('Juniper Networks, Inc.')
if mibBuilder.loadTexts: juniBridgingMgrMIB.setContactInfo(' Juniper Networks, Inc. Postal: 10 Technology Park Drive Westford, MA 01886-3146 USA Tel: +1 978 589 5800 E-mail: mib@Juniper.net')
if mibBuilder.loadTexts: juniBridgingMgrMIB.setDescription('Initial version of this MIB module to support Bridging.')
class JuniBridgingMgrBridgeRouteMask(TextualConvention, Integer32):
    description = 'This integer is interpreted as a bit mask, in which each bit corresponds to a routed protocol. Bit definitions are as follows: Bit Category ----- ----------------------------------------------- 0 ip 1 pppoe 2 mpls'
    status = 'current'

class JuniBridgingMgrNextIndex(TextualConvention, Unsigned32):
    description = 'Coordinates BridgeGroupIndex value allocation for entries in an associated bridge group table. Clients must first read the BridgeGroupIndex value from this object, then create an entry having the BridgeGroupIndex value in the associated bridge group table. A GET of this object returns the next available BridgeGroupIndex value to be used to create an entry in the associated bridge group table; or zero, if no valid BridgeGroupIndex value is available. This object also returns a value of zero when it is the lexicographic successor of a varbind presented in an SNMP GETNEXT or GETBULK request, for which circumstance it is assumed that routerIndex allocation is unintended. Successive GETs will typically return different values, thus avoiding collisions among cooperating management clients seeking to create table entries simultaneously. Unless specified otherwise by its MAX-ACCESS and DESCRIPTION clauses, an object of this type is read-only, and a SET of such an object returns a notWritable error.'
    status = 'current'

juniBridgingMgrBridgeGroup = MibIdentifier((1, 3, 6, 1, 4, 1, 4874, 2, 2, 64, 1))
juniBridgingMgrBridgeSubscriberPolicy = MibIdentifier((1, 3, 6, 1, 4, 1, 4874, 2, 2, 64, 2))
juniBridgingMgrBridge = MibIdentifier((1, 3, 6, 1, 4, 1, 4874, 2, 2, 64, 3))
juniBridgingMgrNextIndex = MibScalar((1, 3, 6, 1, 4, 1, 4874, 2, 2, 64, 1, 1), JuniBridgingMgrNextIndex()).setMaxAccess("readonly")
if mibBuilder.loadTexts: juniBridgingMgrNextIndex.setStatus('current')
if mibBuilder.loadTexts: juniBridgingMgrNextIndex.setDescription('This scalar object returns the index of the next available row in the juniBridgingMgrBridgeGroupTable. This object returns a value of zero when it is the lexicographic successor of a varbind presented in an SNMP GETNEXT or GETBULK request, for which circumstance it is assumed that index allocation is unintended.')
juniBridgingMgrBridgeGroupTable = MibTable((1, 3, 6, 1, 4, 1, 4874, 2, 2, 64, 1, 3), )
if mibBuilder.loadTexts: juniBridgingMgrBridgeGroupTable.setStatus('current')
if mibBuilder.loadTexts: juniBridgingMgrBridgeGroupTable.setDescription('A list of configuration entries for a bridge group.')
juniBridgingMgrBridgeGroupEntry = MibTableRow((1, 3, 6, 1, 4, 1, 4874, 2, 2, 64, 1, 3, 1), ).setIndexNames((0, "Juniper-Bridging-Manager-MIB", "juniBridgingMgrBridgeGroupIndex"))
if mibBuilder.loadTexts: juniBridgingMgrBridgeGroupEntry.setStatus('current')
if mibBuilder.loadTexts: juniBridgingMgrBridgeGroupEntry.setDescription('Configuration parameters for a bridge group.')
juniBridgingMgrBridgeGroupIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 4874, 2, 2, 64, 1, 3, 1, 1), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(0, 4294967295)))
if mibBuilder.loadTexts: juniBridgingMgrBridgeGroupIndex.setStatus('current')
if mibBuilder.loadTexts: juniBridgingMgrBridgeGroupIndex.setDescription('The number of the bridge group table entry which is defined by this row.')
juniBridgingMgrBridgeRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 4874, 2, 2, 64, 1, 3, 1, 2), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: juniBridgingMgrBridgeRowStatus.setStatus('current')
if mibBuilder.loadTexts: juniBridgingMgrBridgeRowStatus.setDescription('Controls creation/deletion of entries in this table according to the RowStatus textual convention, constrained to support the following values only: createAndGo destroy ')
juniBridgingMgrBridgeGroupLearning = MibTableColumn((1, 3, 6, 1, 4, 1, 4874, 2, 2, 64, 1, 3, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enabled", 1), ("disabled", 2))).clone('enabled')).setMaxAccess("readcreate")
if mibBuilder.loadTexts: juniBridgingMgrBridgeGroupLearning.setStatus('current')
if mibBuilder.loadTexts: juniBridgingMgrBridgeGroupLearning.setDescription('This object indicates if MAC address learning is enabled or disabled for the bridge group.')
juniBridgingMgrBridgeGroupName = MibTableColumn((1, 3, 6, 1, 4, 1, 4874, 2, 2, 64, 1, 3, 1, 4), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 32))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: juniBridgingMgrBridgeGroupName.setStatus('current')
if mibBuilder.loadTexts: juniBridgingMgrBridgeGroupName.setDescription('The name of the bridge group.')
juniBridgingMgrBridgeGroupSPolicyIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 4874, 2, 2, 64, 1, 3, 1, 5), Integer32()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: juniBridgingMgrBridgeGroupSPolicyIndex.setStatus('current')
if mibBuilder.loadTexts: juniBridgingMgrBridgeGroupSPolicyIndex.setDescription('The index of the associated subscriber policy.')
juniBridgingMgrBridgeGroupRouteProtocol = MibTableColumn((1, 3, 6, 1, 4, 1, 4874, 2, 2, 64, 1, 3, 1, 6), JuniBridgingMgrBridgeRouteMask()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: juniBridgingMgrBridgeGroupRouteProtocol.setStatus('current')
if mibBuilder.loadTexts: juniBridgingMgrBridgeGroupRouteProtocol.setDescription('The protocol masks for which protocols to route.')
juniBridgingMgrBridgeGroupLearnCount = MibTableColumn((1, 3, 6, 1, 4, 1, 4874, 2, 2, 64, 1, 3, 1, 7), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 64000))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: juniBridgingMgrBridgeGroupLearnCount.setStatus('current')
if mibBuilder.loadTexts: juniBridgingMgrBridgeGroupLearnCount.setDescription('This object represents the maximum number of mac entries that can be learned from any one bridge interface belonging to this bridge group. The default value of 0 indicates that the maximum number of entries is not restricted.')
juniBridgingMgrSubscriberNextIndex = MibScalar((1, 3, 6, 1, 4, 1, 4874, 2, 2, 64, 2, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 2147483647))).setMaxAccess("readonly")
if mibBuilder.loadTexts: juniBridgingMgrSubscriberNextIndex.setStatus('current')
if mibBuilder.loadTexts: juniBridgingMgrSubscriberNextIndex.setDescription('This scalar object returns the index of the next available row in the juniBridgingMgrBridgeSubscriberPolicyTable. This object returns a value of zero when it is the lexicographic successor of a varbind presented in an SNMP GETNEXT or GETBULK request, for which circumstance it is assumed that index allocation is unintended.')
juniBridgingMgrBridgeSubscriberPolicyTable = MibTable((1, 3, 6, 1, 4, 1, 4874, 2, 2, 64, 2, 2), )
if mibBuilder.loadTexts: juniBridgingMgrBridgeSubscriberPolicyTable.setStatus('current')
if mibBuilder.loadTexts: juniBridgingMgrBridgeSubscriberPolicyTable.setDescription('A list of subscriber policy entries.')
juniBridgingMgrBridgeSubscriberPolicyEntry = MibTableRow((1, 3, 6, 1, 4, 1, 4874, 2, 2, 64, 2, 2, 1), ).setIndexNames((0, "Juniper-Bridging-Manager-MIB", "juniBridgingMgrBridgeSubscriberPolicyIndex"))
if mibBuilder.loadTexts: juniBridgingMgrBridgeSubscriberPolicyEntry.setStatus('current')
if mibBuilder.loadTexts: juniBridgingMgrBridgeSubscriberPolicyEntry.setDescription('Configuration parameters for a subscriber policy.')
juniBridgingMgrBridgeSubscriberPolicyIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 4874, 2, 2, 64, 2, 2, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 2147483647)))
if mibBuilder.loadTexts: juniBridgingMgrBridgeSubscriberPolicyIndex.setStatus('current')
if mibBuilder.loadTexts: juniBridgingMgrBridgeSubscriberPolicyIndex.setDescription('The number of the subscriber policy table entry which is defined by this row.')
juniBridgingMgrBridgeSubscriberPolicyRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 4874, 2, 2, 64, 2, 2, 1, 2), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: juniBridgingMgrBridgeSubscriberPolicyRowStatus.setStatus('current')
if mibBuilder.loadTexts: juniBridgingMgrBridgeSubscriberPolicyRowStatus.setDescription('Controls creation/deletion of entries in this table according to the RowStatus textual convention, constrained to support the following values only: createAndGo destroy ')
juniBridgingMgrBridgeSubscriberPolicyArp = MibTableColumn((1, 3, 6, 1, 4, 1, 4874, 2, 2, 64, 2, 2, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("permit", 1), ("deny", 2)))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: juniBridgingMgrBridgeSubscriberPolicyArp.setStatus('current')
if mibBuilder.loadTexts: juniBridgingMgrBridgeSubscriberPolicyArp.setDescription('This object indicates if ARP is permitted or denied.')
juniBridgingMgrBridgeSubscriberPolicyBroadcast = MibTableColumn((1, 3, 6, 1, 4, 1, 4874, 2, 2, 64, 2, 2, 1, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("permit", 1), ("deny", 2)))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: juniBridgingMgrBridgeSubscriberPolicyBroadcast.setStatus('current')
if mibBuilder.loadTexts: juniBridgingMgrBridgeSubscriberPolicyBroadcast.setDescription('This object indicates if Broadcast packets are permitted or denied.')
juniBridgingMgrBridgeSubscriberPolicyMulticast = MibTableColumn((1, 3, 6, 1, 4, 1, 4874, 2, 2, 64, 2, 2, 1, 5), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("permit", 1), ("deny", 2)))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: juniBridgingMgrBridgeSubscriberPolicyMulticast.setStatus('current')
if mibBuilder.loadTexts: juniBridgingMgrBridgeSubscriberPolicyMulticast.setDescription('This object indicates if Multicast packets are permitted or denied.')
juniBridgingMgrBridgeSubscriberPolicyUnknownUnicast = MibTableColumn((1, 3, 6, 1, 4, 1, 4874, 2, 2, 64, 2, 2, 1, 6), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("permit", 1), ("deny", 2)))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: juniBridgingMgrBridgeSubscriberPolicyUnknownUnicast.setStatus('current')
if mibBuilder.loadTexts: juniBridgingMgrBridgeSubscriberPolicyUnknownUnicast.setDescription('This object indicates if Unknown DA unicast packets are permitted or denied.')
juniBridgingMgrBridgeSubscriberPolicyIp = MibTableColumn((1, 3, 6, 1, 4, 1, 4874, 2, 2, 64, 2, 2, 1, 7), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("permit", 1), ("deny", 2)))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: juniBridgingMgrBridgeSubscriberPolicyIp.setStatus('current')
if mibBuilder.loadTexts: juniBridgingMgrBridgeSubscriberPolicyIp.setDescription('This object indicates if IP is permitted or denied.')
juniBridgingMgrBridgeSubscriberPolicyUnknownProtocol = MibTableColumn((1, 3, 6, 1, 4, 1, 4874, 2, 2, 64, 2, 2, 1, 8), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("permit", 1), ("deny", 2)))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: juniBridgingMgrBridgeSubscriberPolicyUnknownProtocol.setStatus('current')
if mibBuilder.loadTexts: juniBridgingMgrBridgeSubscriberPolicyUnknownProtocol.setDescription('This object indicates if packets with unknown protocols are permitted or denied. Unknown is defined as not IP or PPPoE.')
juniBridgingMgrBridgeSubscriberPolicyUnicast = MibTableColumn((1, 3, 6, 1, 4, 1, 4874, 2, 2, 64, 2, 2, 1, 9), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("permit", 1), ("deny", 2)))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: juniBridgingMgrBridgeSubscriberPolicyUnicast.setStatus('current')
if mibBuilder.loadTexts: juniBridgingMgrBridgeSubscriberPolicyUnicast.setDescription('This object indicates if Unicast packets are permitted or denied.')
juniBridgingMgrBridgeSubscriberPolicyPPPoE = MibTableColumn((1, 3, 6, 1, 4, 1, 4874, 2, 2, 64, 2, 2, 1, 10), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("permit", 1), ("deny", 2)))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: juniBridgingMgrBridgeSubscriberPolicyPPPoE.setStatus('current')
if mibBuilder.loadTexts: juniBridgingMgrBridgeSubscriberPolicyPPPoE.setDescription('This object indicates if PPPoE packets are permitted or denied.')
juniBridgingMgrBridgeSubscriberPolicyRelearn = MibTableColumn((1, 3, 6, 1, 4, 1, 4874, 2, 2, 64, 2, 2, 1, 11), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("permit", 1), ("deny", 2)))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: juniBridgingMgrBridgeSubscriberPolicyRelearn.setStatus('current')
if mibBuilder.loadTexts: juniBridgingMgrBridgeSubscriberPolicyRelearn.setDescription('This object indicates if packets that cause MAC addressing relearning are permitted or denied.')
juniBridgingMgrBridgeSubscriberPolicyMpls = MibTableColumn((1, 3, 6, 1, 4, 1, 4874, 2, 2, 64, 2, 2, 1, 12), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("permit", 1), ("deny", 2)))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: juniBridgingMgrBridgeSubscriberPolicyMpls.setStatus('current')
if mibBuilder.loadTexts: juniBridgingMgrBridgeSubscriberPolicyMpls.setDescription('This object indicates if Mpls packets are permitted or denied.')
juniBridgingMgrBridgeSubscriberPolicyName = MibTableColumn((1, 3, 6, 1, 4, 1, 4874, 2, 2, 64, 2, 2, 1, 13), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 32))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: juniBridgingMgrBridgeSubscriberPolicyName.setStatus('current')
if mibBuilder.loadTexts: juniBridgingMgrBridgeSubscriberPolicyName.setDescription('The name of the subscriber policy.')
juniBridgingMgrBridgeMode = MibScalar((1, 3, 6, 1, 4, 1, 4874, 2, 2, 64, 3, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3))).clone(namedValues=NamedValues(("default", 0), ("crb", 1), ("irb", 2), ("other", 3)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: juniBridgingMgrBridgeMode.setStatus('current')
if mibBuilder.loadTexts: juniBridgingMgrBridgeMode.setDescription('This scalar object represents the mode of the bridge. The legal values are the following: default, CRB, IRB, and other. If the legal value is not supported by a particular implementation an error will occur.')
juniBridgingMgrConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 4874, 2, 2, 64, 4))
juniBridgingMgrCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 4874, 2, 2, 64, 4, 1))
juniBridgingMgrGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 4874, 2, 2, 64, 4, 2))
juniBridgingMgrCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 4874, 2, 2, 64, 4, 1, 1)).setObjects(("Juniper-Bridging-Manager-MIB", "juniBridgingMgrConfGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    juniBridgingMgrCompliance = juniBridgingMgrCompliance.setStatus('current')
if mibBuilder.loadTexts: juniBridgingMgrCompliance.setDescription('The compliance statement for entities which implement the Juniper Bridging Manager MIB.')
juniBridgingMgrConfGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 4874, 2, 2, 64, 4, 2, 1)).setObjects(("Juniper-Bridging-Manager-MIB", "juniBridgingMgrNextIndex"), ("Juniper-Bridging-Manager-MIB", "juniBridgingMgrBridgeRowStatus"), ("Juniper-Bridging-Manager-MIB", "juniBridgingMgrBridgeGroupLearning"), ("Juniper-Bridging-Manager-MIB", "juniBridgingMgrBridgeGroupName"), ("Juniper-Bridging-Manager-MIB", "juniBridgingMgrBridgeGroupSPolicyIndex"), ("Juniper-Bridging-Manager-MIB", "juniBridgingMgrBridgeGroupRouteProtocol"), ("Juniper-Bridging-Manager-MIB", "juniBridgingMgrBridgeGroupLearnCount"), ("Juniper-Bridging-Manager-MIB", "juniBridgingMgrSubscriberNextIndex"), ("Juniper-Bridging-Manager-MIB", "juniBridgingMgrBridgeSubscriberPolicyRowStatus"), ("Juniper-Bridging-Manager-MIB", "juniBridgingMgrBridgeSubscriberPolicyArp"), ("Juniper-Bridging-Manager-MIB", "juniBridgingMgrBridgeSubscriberPolicyBroadcast"), ("Juniper-Bridging-Manager-MIB", "juniBridgingMgrBridgeSubscriberPolicyMulticast"), ("Juniper-Bridging-Manager-MIB", "juniBridgingMgrBridgeSubscriberPolicyUnknownUnicast"), ("Juniper-Bridging-Manager-MIB", "juniBridgingMgrBridgeSubscriberPolicyIp"), ("Juniper-Bridging-Manager-MIB", "juniBridgingMgrBridgeSubscriberPolicyUnknownProtocol"), ("Juniper-Bridging-Manager-MIB", "juniBridgingMgrBridgeSubscriberPolicyUnicast"), ("Juniper-Bridging-Manager-MIB", "juniBridgingMgrBridgeSubscriberPolicyPPPoE"), ("Juniper-Bridging-Manager-MIB", "juniBridgingMgrBridgeSubscriberPolicyRelearn"), ("Juniper-Bridging-Manager-MIB", "juniBridgingMgrBridgeSubscriberPolicyMpls"), ("Juniper-Bridging-Manager-MIB", "juniBridgingMgrBridgeSubscriberPolicyName"), ("Juniper-Bridging-Manager-MIB", "juniBridgingMgrBridgeMode"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    juniBridgingMgrConfGroup = juniBridgingMgrConfGroup.setStatus('current')
if mibBuilder.loadTexts: juniBridgingMgrConfGroup.setDescription('A collection of objects providing basic management of the Bridging Manager in a Juniper product.')
mibBuilder.exportSymbols("Juniper-Bridging-Manager-MIB", juniBridgingMgrBridgeSubscriberPolicyRelearn=juniBridgingMgrBridgeSubscriberPolicyRelearn, juniBridgingMgrConfGroup=juniBridgingMgrConfGroup, juniBridgingMgrBridgeGroupName=juniBridgingMgrBridgeGroupName, juniBridgingMgrBridgeSubscriberPolicyUnknownProtocol=juniBridgingMgrBridgeSubscriberPolicyUnknownProtocol, juniBridgingMgrBridgeSubscriberPolicyBroadcast=juniBridgingMgrBridgeSubscriberPolicyBroadcast, juniBridgingMgrBridgeSubscriberPolicyMpls=juniBridgingMgrBridgeSubscriberPolicyMpls, juniBridgingMgrSubscriberNextIndex=juniBridgingMgrSubscriberNextIndex, juniBridgingMgrBridgeSubscriberPolicyMulticast=juniBridgingMgrBridgeSubscriberPolicyMulticast, juniBridgingMgrMIB=juniBridgingMgrMIB, juniBridgingMgrNextIndex=juniBridgingMgrNextIndex, juniBridgingMgrBridgeGroupEntry=juniBridgingMgrBridgeGroupEntry, juniBridgingMgrBridgeGroupTable=juniBridgingMgrBridgeGroupTable, juniBridgingMgrBridgeSubscriberPolicyUnknownUnicast=juniBridgingMgrBridgeSubscriberPolicyUnknownUnicast, juniBridgingMgrBridgeGroup=juniBridgingMgrBridgeGroup, juniBridgingMgrBridgeMode=juniBridgingMgrBridgeMode, JuniBridgingMgrBridgeRouteMask=JuniBridgingMgrBridgeRouteMask, juniBridgingMgrBridgeSubscriberPolicyIndex=juniBridgingMgrBridgeSubscriberPolicyIndex, juniBridgingMgrBridgeGroupSPolicyIndex=juniBridgingMgrBridgeGroupSPolicyIndex, juniBridgingMgrConformance=juniBridgingMgrConformance, juniBridgingMgrCompliance=juniBridgingMgrCompliance, juniBridgingMgrBridgeSubscriberPolicyRowStatus=juniBridgingMgrBridgeSubscriberPolicyRowStatus, juniBridgingMgrBridgeGroupLearnCount=juniBridgingMgrBridgeGroupLearnCount, juniBridgingMgrBridgeRowStatus=juniBridgingMgrBridgeRowStatus, juniBridgingMgrBridgeSubscriberPolicy=juniBridgingMgrBridgeSubscriberPolicy, juniBridgingMgrBridgeSubscriberPolicyTable=juniBridgingMgrBridgeSubscriberPolicyTable, juniBridgingMgrGroups=juniBridgingMgrGroups, JuniBridgingMgrNextIndex=JuniBridgingMgrNextIndex, juniBridgingMgrBridgeSubscriberPolicyPPPoE=juniBridgingMgrBridgeSubscriberPolicyPPPoE, juniBridgingMgrBridgeSubscriberPolicyUnicast=juniBridgingMgrBridgeSubscriberPolicyUnicast, juniBridgingMgrBridgeSubscriberPolicyArp=juniBridgingMgrBridgeSubscriberPolicyArp, PYSNMP_MODULE_ID=juniBridgingMgrMIB, juniBridgingMgrBridge=juniBridgingMgrBridge, juniBridgingMgrBridgeGroupIndex=juniBridgingMgrBridgeGroupIndex, juniBridgingMgrBridgeSubscriberPolicyName=juniBridgingMgrBridgeSubscriberPolicyName, juniBridgingMgrBridgeSubscriberPolicyEntry=juniBridgingMgrBridgeSubscriberPolicyEntry, juniBridgingMgrBridgeSubscriberPolicyIp=juniBridgingMgrBridgeSubscriberPolicyIp, juniBridgingMgrBridgeGroupLearning=juniBridgingMgrBridgeGroupLearning, juniBridgingMgrBridgeGroupRouteProtocol=juniBridgingMgrBridgeGroupRouteProtocol, juniBridgingMgrCompliances=juniBridgingMgrCompliances)