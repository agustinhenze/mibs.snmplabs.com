#
# PySNMP MIB module HP-ICF-OOBM-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/HP-ICF-OOBM-MIB
# Produced by pysmi-0.3.4 at Wed May  1 13:34:51 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
OctetString, ObjectIdentifier, Integer = mibBuilder.importSymbols("ASN1", "OctetString", "ObjectIdentifier", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
SingleValueConstraint, ValueRangeConstraint, ConstraintsIntersection, ConstraintsUnion, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "SingleValueConstraint", "ValueRangeConstraint", "ConstraintsIntersection", "ConstraintsUnion", "ValueSizeConstraint")
hpSwitch, = mibBuilder.importSymbols("HP-ICF-OID", "hpSwitch")
ifIndex, = mibBuilder.importSymbols("IF-MIB", "ifIndex")
InetAddress, InetAddressType = mibBuilder.importSymbols("INET-ADDRESS-MIB", "InetAddress", "InetAddressType")
snmpTargetAddrEntry, = mibBuilder.importSymbols("SNMP-TARGET-MIB", "snmpTargetAddrEntry")
ObjectGroup, ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ObjectGroup", "ModuleCompliance", "NotificationGroup")
Gauge32, Counter32, Bits, NotificationType, ModuleIdentity, Integer32, TimeTicks, ObjectIdentity, iso, MibIdentifier, MibScalar, MibTable, MibTableRow, MibTableColumn, Unsigned32, IpAddress, Counter64 = mibBuilder.importSymbols("SNMPv2-SMI", "Gauge32", "Counter32", "Bits", "NotificationType", "ModuleIdentity", "Integer32", "TimeTicks", "ObjectIdentity", "iso", "MibIdentifier", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Unsigned32", "IpAddress", "Counter64")
DisplayString, TruthValue, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TruthValue", "TextualConvention")
hpicfOobmMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 58))
hpicfOobmMIB.setRevisions(('2010-03-26 00:00', '2009-02-13 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: hpicfOobmMIB.setRevisionsDescriptions(('Added oobm member tables', 'Initial Revision',))
if mibBuilder.loadTexts: hpicfOobmMIB.setLastUpdated('201003260000Z')
if mibBuilder.loadTexts: hpicfOobmMIB.setOrganization('HP Networking')
if mibBuilder.loadTexts: hpicfOobmMIB.setContactInfo('Hewlett-Packard Company 8000 Foothills Blvd. Roseville, CA 95747')
if mibBuilder.loadTexts: hpicfOobmMIB.setDescription('The MIB module is for representing Oobm entity')
hpicfOobmNotifications = MibIdentifier((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 58, 0))
hpicfOobmObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 58, 1))
hpicfOobmConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 58, 3))
class HpicfOobmServerIndex(TextualConvention, Integer32):
    description = 'An enumerated value that indications the Server application type. Server application type is index for this table.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5))
    namedValues = NamedValues(("telnet", 1), ("ssh", 2), ("tftp", 3), ("http", 4), ("snmp", 5))

class HpicfOobmServerState(TextualConvention, Integer32):
    description = "An enumerated value which provides an indication of the Application server's presence. Default value is oobm only. Application server can be run for oobm only, data only, or for both."
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3))
    namedValues = NamedValues(("oobm", 1), ("data", 2), ("both", 3))

hpicfOobmScalars = MibIdentifier((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 58, 1, 1))
hpicfOobmStatus = MibScalar((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 58, 1, 1, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enable", 1), ("disable", 2))).clone('enable')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hpicfOobmStatus.setStatus('current')
if mibBuilder.loadTexts: hpicfOobmStatus.setDescription('Global Oobm (Out Of Band Management) status. By default oobm is globally enabled. On the stackable device, when stacking is enabled, this enables oobm on all the member switches.')
hpicfOobmServers = MibIdentifier((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 58, 1, 2))
hpicfOobmServerTable = MibTable((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 58, 1, 2, 1), )
if mibBuilder.loadTexts: hpicfOobmServerTable.setStatus('current')
if mibBuilder.loadTexts: hpicfOobmServerTable.setDescription('This table contains one row for every server application in the switch entity. On a stackable device, when stacking is enabled, the server entry is created on all the member switches.')
hpicfOobmServerEntry = MibTableRow((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 58, 1, 2, 1, 1), ).setIndexNames((0, "HP-ICF-OOBM-MIB", "hpicfOobmServerType"))
if mibBuilder.loadTexts: hpicfOobmServerEntry.setStatus('current')
if mibBuilder.loadTexts: hpicfOobmServerEntry.setDescription('Information about Server Application table.')
hpicfOobmServerType = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 58, 1, 2, 1, 1, 1), HpicfOobmServerIndex())
if mibBuilder.loadTexts: hpicfOobmServerType.setStatus('current')
if mibBuilder.loadTexts: hpicfOobmServerType.setDescription('The index that is used to access the switch server application table.')
hpicfOobmServerListenMode = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 58, 1, 2, 1, 1, 2), HpicfOobmServerState()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hpicfOobmServerListenMode.setStatus('current')
if mibBuilder.loadTexts: hpicfOobmServerListenMode.setDescription('The current state of the server application. Default value is Oobm. Depending on the interface on which server application is running, incoming queries will be listened by the switch.')
hpicfOobmSnmpTargetAddrIsOobm = MibIdentifier((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 58, 1, 3))
hpicfSnmpTargetAddrIsOobmTable = MibTable((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 58, 1, 3, 1), )
if mibBuilder.loadTexts: hpicfSnmpTargetAddrIsOobmTable.setStatus('current')
if mibBuilder.loadTexts: hpicfSnmpTargetAddrIsOobmTable.setDescription('Adds an HpicfSnmpTargetAddrIsOobmEntry to snmpTargetAddrTable.')
hpicfSnmpTargetAddrIsOobmEntry = MibTableRow((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 58, 1, 3, 1, 1), )
snmpTargetAddrEntry.registerAugmentions(("HP-ICF-OOBM-MIB", "hpicfSnmpTargetAddrIsOobmEntry"))
hpicfSnmpTargetAddrIsOobmEntry.setIndexNames(*snmpTargetAddrEntry.getIndexNames())
if mibBuilder.loadTexts: hpicfSnmpTargetAddrIsOobmEntry.setStatus('current')
if mibBuilder.loadTexts: hpicfSnmpTargetAddrIsOobmEntry.setDescription('Adds an HpicfSnmpTargetAddrIsOobmEntry to snmpTargetAddrTable.')
hpicfSnmpTargetAddrIsOobm = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 58, 1, 3, 1, 1, 1), TruthValue().clone('false')).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hpicfSnmpTargetAddrIsOobm.setStatus('current')
if mibBuilder.loadTexts: hpicfSnmpTargetAddrIsOobm.setDescription('This object indicates if the target is reachable over OOBM (Out OF Band Management) interface or not. This mib object will be applicable only if there is a physical OOBM port on the device.')
hpicfOobmDefGateway = MibIdentifier((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 58, 1, 4))
hpicfOobmDefGatewayTable = MibTable((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 58, 1, 4, 1), )
if mibBuilder.loadTexts: hpicfOobmDefGatewayTable.setStatus('current')
if mibBuilder.loadTexts: hpicfOobmDefGatewayTable.setDescription('This table contains one row for every default gateway configured for OOBM Interface.')
hpicfOobmDefGatewayEntry = MibTableRow((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 58, 1, 4, 1, 1), ).setIndexNames((0, "HP-ICF-OOBM-MIB", "hpicfOobmDefGatewayType"))
if mibBuilder.loadTexts: hpicfOobmDefGatewayEntry.setStatus('current')
if mibBuilder.loadTexts: hpicfOobmDefGatewayEntry.setDescription('Information about Default Gateway table.')
hpicfOobmDefGatewayType = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 58, 1, 4, 1, 1, 1), InetAddressType())
if mibBuilder.loadTexts: hpicfOobmDefGatewayType.setStatus('current')
if mibBuilder.loadTexts: hpicfOobmDefGatewayType.setDescription('Address type of default gateway configured for OOBM Interface.')
hpicfOobmDefGatewayAddr = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 58, 1, 4, 1, 1, 2), InetAddress()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hpicfOobmDefGatewayAddr.setStatus('current')
if mibBuilder.loadTexts: hpicfOobmDefGatewayAddr.setDescription('The IP Address of the default gateway configured for OOBM interface.')
hpicfOobmStackMembers = MibIdentifier((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 58, 1, 5))
hpicfOobmMemberDefGatewayTable = MibTable((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 58, 1, 5, 3), )
if mibBuilder.loadTexts: hpicfOobmMemberDefGatewayTable.setStatus('current')
if mibBuilder.loadTexts: hpicfOobmMemberDefGatewayTable.setDescription('This table contains one row for every default gateway configured for OOBM Interface and for each member of the stack.')
hpicfOobmMemberDefGatewayEntry = MibTableRow((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 58, 1, 5, 3, 1), ).setIndexNames((0, "IF-MIB", "ifIndex"), (0, "HP-ICF-OOBM-MIB", "hpicfOobmMemberDefGatewayType"))
if mibBuilder.loadTexts: hpicfOobmMemberDefGatewayEntry.setStatus('current')
if mibBuilder.loadTexts: hpicfOobmMemberDefGatewayEntry.setDescription('Information about Default Gateway table.')
hpicfOobmMemberDefGatewayType = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 58, 1, 5, 3, 1, 1), InetAddressType())
if mibBuilder.loadTexts: hpicfOobmMemberDefGatewayType.setStatus('current')
if mibBuilder.loadTexts: hpicfOobmMemberDefGatewayType.setDescription('Address type of default gateway configured for OOBM Interface.')
hpicfOobmMemberDefGatewayAddr = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 58, 1, 5, 3, 1, 2), InetAddress()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hpicfOobmMemberDefGatewayAddr.setStatus('current')
if mibBuilder.loadTexts: hpicfOobmMemberDefGatewayAddr.setDescription('The IP Address of the default gateway configured for OOBM interface.')
hpicfOobmCompliance = MibIdentifier((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 58, 3, 1))
hpicfOobmGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 58, 3, 2))
hpicfOobmMibCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 58, 3, 1, 1)).setObjects(("HP-ICF-OOBM-MIB", "hpicfOobmScalarsGroup"), ("HP-ICF-OOBM-MIB", "hpicfOobmServersGroup"), ("HP-ICF-OOBM-MIB", "hpicfSnmpTargetAddrIsOobmGroup"), ("HP-ICF-OOBM-MIB", "hpicfOobmDefGatewayGroup"), ("HP-ICF-OOBM-MIB", "hpicfOobmMemberGroup"), ("HP-ICF-OOBM-MIB", "hpicfOobmGroups"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    hpicfOobmMibCompliance = hpicfOobmMibCompliance.setStatus('current')
if mibBuilder.loadTexts: hpicfOobmMibCompliance.setDescription('The compliance statement for entries which implement the Oobm application servers MIB.')
hpicfOobmScalarsGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 58, 3, 2, 1)).setObjects(("HP-ICF-OOBM-MIB", "hpicfOobmStatus"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    hpicfOobmScalarsGroup = hpicfOobmScalarsGroup.setStatus('current')
if mibBuilder.loadTexts: hpicfOobmScalarsGroup.setDescription('Basic Scalars required in Oobm MIB implementation.')
hpicfOobmServersGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 58, 3, 2, 2)).setObjects(("HP-ICF-OOBM-MIB", "hpicfOobmServerListenMode"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    hpicfOobmServersGroup = hpicfOobmServersGroup.setStatus('current')
if mibBuilder.loadTexts: hpicfOobmServersGroup.setDescription('Oobm Server MIB parameters.')
hpicfSnmpTargetAddrIsOobmGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 58, 3, 2, 3)).setObjects(("HP-ICF-OOBM-MIB", "hpicfSnmpTargetAddrIsOobm"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    hpicfSnmpTargetAddrIsOobmGroup = hpicfSnmpTargetAddrIsOobmGroup.setStatus('current')
if mibBuilder.loadTexts: hpicfSnmpTargetAddrIsOobmGroup.setDescription('A group of objects to add an HpicfSnmpTargetAddrIsOobmEntry to snmpTargetAddrTable.')
hpicfOobmDefGatewayGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 58, 3, 2, 4)).setObjects(("HP-ICF-OOBM-MIB", "hpicfOobmDefGatewayAddr"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    hpicfOobmDefGatewayGroup = hpicfOobmDefGatewayGroup.setStatus('current')
if mibBuilder.loadTexts: hpicfOobmDefGatewayGroup.setDescription('OOBM Default Gateway MIB parameters')
hpicfOobmMemberGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 58, 3, 2, 5)).setObjects(("HP-ICF-OOBM-MIB", "hpicfOobmMemberDefGatewayAddr"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    hpicfOobmMemberGroup = hpicfOobmMemberGroup.setStatus('current')
if mibBuilder.loadTexts: hpicfOobmMemberGroup.setDescription('OOBM stack member parameters')
mibBuilder.exportSymbols("HP-ICF-OOBM-MIB", HpicfOobmServerState=HpicfOobmServerState, hpicfOobmDefGatewayGroup=hpicfOobmDefGatewayGroup, hpicfOobmServerEntry=hpicfOobmServerEntry, hpicfOobmDefGateway=hpicfOobmDefGateway, hpicfOobmStatus=hpicfOobmStatus, hpicfOobmDefGatewayEntry=hpicfOobmDefGatewayEntry, hpicfOobmServerTable=hpicfOobmServerTable, hpicfOobmCompliance=hpicfOobmCompliance, hpicfOobmObjects=hpicfOobmObjects, hpicfOobmDefGatewayType=hpicfOobmDefGatewayType, hpicfOobmMemberDefGatewayAddr=hpicfOobmMemberDefGatewayAddr, hpicfOobmMemberGroup=hpicfOobmMemberGroup, hpicfOobmDefGatewayAddr=hpicfOobmDefGatewayAddr, hpicfOobmSnmpTargetAddrIsOobm=hpicfOobmSnmpTargetAddrIsOobm, hpicfOobmServerType=hpicfOobmServerType, hpicfOobmServers=hpicfOobmServers, hpicfSnmpTargetAddrIsOobmEntry=hpicfSnmpTargetAddrIsOobmEntry, hpicfOobmMemberDefGatewayEntry=hpicfOobmMemberDefGatewayEntry, hpicfSnmpTargetAddrIsOobm=hpicfSnmpTargetAddrIsOobm, hpicfOobmMemberDefGatewayType=hpicfOobmMemberDefGatewayType, hpicfOobmServerListenMode=hpicfOobmServerListenMode, PYSNMP_MODULE_ID=hpicfOobmMIB, hpicfOobmGroups=hpicfOobmGroups, hpicfOobmScalars=hpicfOobmScalars, hpicfOobmConformance=hpicfOobmConformance, HpicfOobmServerIndex=HpicfOobmServerIndex, hpicfSnmpTargetAddrIsOobmTable=hpicfSnmpTargetAddrIsOobmTable, hpicfOobmNotifications=hpicfOobmNotifications, hpicfSnmpTargetAddrIsOobmGroup=hpicfSnmpTargetAddrIsOobmGroup, hpicfOobmScalarsGroup=hpicfOobmScalarsGroup, hpicfOobmMemberDefGatewayTable=hpicfOobmMemberDefGatewayTable, hpicfOobmMIB=hpicfOobmMIB, hpicfOobmMibCompliance=hpicfOobmMibCompliance, hpicfOobmDefGatewayTable=hpicfOobmDefGatewayTable, hpicfOobmServersGroup=hpicfOobmServersGroup, hpicfOobmStackMembers=hpicfOobmStackMembers)
