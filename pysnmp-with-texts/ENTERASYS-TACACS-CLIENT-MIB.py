#
# PySNMP MIB module ENTERASYS-TACACS-CLIENT-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/ENTERASYS-TACACS-CLIENT-MIB
# Produced by pysmi-0.3.4 at Wed May  1 13:04:44 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ConstraintsUnion, ValueSizeConstraint, SingleValueConstraint, ValueRangeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ConstraintsUnion", "ValueSizeConstraint", "SingleValueConstraint", "ValueRangeConstraint")
etsysModules, = mibBuilder.importSymbols("ENTERASYS-MIB-NAMES", "etsysModules")
InetAddressType, InetPortNumber, InetAddress = mibBuilder.importSymbols("INET-ADDRESS-MIB", "InetAddressType", "InetPortNumber", "InetAddress")
EnabledStatus, = mibBuilder.importSymbols("P-BRIDGE-MIB", "EnabledStatus")
SnmpAdminString, = mibBuilder.importSymbols("SNMP-FRAMEWORK-MIB", "SnmpAdminString")
ObjectGroup, NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "ObjectGroup", "NotificationGroup", "ModuleCompliance")
iso, ObjectIdentity, MibIdentifier, Gauge32, MibScalar, MibTable, MibTableRow, MibTableColumn, ModuleIdentity, NotificationType, IpAddress, Integer32, TimeTicks, Unsigned32, Counter64, Bits, Counter32 = mibBuilder.importSymbols("SNMPv2-SMI", "iso", "ObjectIdentity", "MibIdentifier", "Gauge32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "ModuleIdentity", "NotificationType", "IpAddress", "Integer32", "TimeTicks", "Unsigned32", "Counter64", "Bits", "Counter32")
RowStatus, TextualConvention, DisplayString, TruthValue = mibBuilder.importSymbols("SNMPv2-TC", "RowStatus", "TextualConvention", "DisplayString", "TruthValue")
etsysTacacsClientMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 5624, 1, 2, 58))
etsysTacacsClientMIB.setRevisions(('2010-02-01 17:02', '2005-02-10 17:57',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: etsysTacacsClientMIB.setRevisionsDescriptions(('Corrected DESCRIPTION clause for the etsysTacacsClientSesnAuthValue object.', 'The initial version of this MIB module.',))
if mibBuilder.loadTexts: etsysTacacsClientMIB.setLastUpdated('201002011702Z')
if mibBuilder.loadTexts: etsysTacacsClientMIB.setOrganization('Enterasys Networks, Inc')
if mibBuilder.loadTexts: etsysTacacsClientMIB.setContactInfo('Postal: Enterasys Networks 50 Minuteman Rd. Andover, MA 01810-1008 USA Phone: +1 978 684 1000 E-mail: support@enterasys.com WWW: http://www.enterasys.com')
if mibBuilder.loadTexts: etsysTacacsClientMIB.setDescription('This MIB module defines a portion of the SNMP MIB under the Enterasys Networks enterprise OID pertaining to TACACS+ client configuration.')
etsysTacacsClientObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 5624, 1, 2, 58, 1))
etsysTacacsClientControl = MibIdentifier((1, 3, 6, 1, 4, 1, 5624, 1, 2, 58, 1, 1))
etsysTacacsClientSesnAuth = MibIdentifier((1, 3, 6, 1, 4, 1, 5624, 1, 2, 58, 1, 2))
etsysTacacsClientServer = MibIdentifier((1, 3, 6, 1, 4, 1, 5624, 1, 2, 58, 1, 3))
etsysTacacsClientSesnAuthEnabled = MibScalar((1, 3, 6, 1, 4, 1, 5624, 1, 2, 58, 1, 1, 1), EnabledStatus().clone('disabled')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: etsysTacacsClientSesnAuthEnabled.setStatus('current')
if mibBuilder.loadTexts: etsysTacacsClientSesnAuthEnabled.setDescription('Controls the operation of the TACACS+ client for session authentication and authorization.')
etsysTacacsClientSesnAcctEnabled = MibScalar((1, 3, 6, 1, 4, 1, 5624, 1, 2, 58, 1, 1, 2), EnabledStatus().clone('disabled')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: etsysTacacsClientSesnAcctEnabled.setStatus('current')
if mibBuilder.loadTexts: etsysTacacsClientSesnAcctEnabled.setDescription('Controls the operation of the TACACS+ client for session accounting.')
etsysTacacsClientCmdAuthEnabled = MibScalar((1, 3, 6, 1, 4, 1, 5624, 1, 2, 58, 1, 1, 3), EnabledStatus().clone('disabled')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: etsysTacacsClientCmdAuthEnabled.setStatus('current')
if mibBuilder.loadTexts: etsysTacacsClientCmdAuthEnabled.setDescription('Controls the operation of the TACACS+ client for command level authorization.')
etsysTacacsClientCmdAcctEnabled = MibScalar((1, 3, 6, 1, 4, 1, 5624, 1, 2, 58, 1, 1, 4), EnabledStatus().clone('disabled')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: etsysTacacsClientCmdAcctEnabled.setStatus('current')
if mibBuilder.loadTexts: etsysTacacsClientCmdAcctEnabled.setDescription('Controls the operation of the TACACS+ client for command accounting.')
etsysTacacsClientSingleConnection = MibScalar((1, 3, 6, 1, 4, 1, 5624, 1, 2, 58, 1, 1, 5), EnabledStatus().clone('disabled')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: etsysTacacsClientSingleConnection.setStatus('current')
if mibBuilder.loadTexts: etsysTacacsClientSingleConnection.setDescription('Allows the TACACS+ client to send multiple TACACS+ requests on a single TCP connection. All configured TACACS+ servers MUST allow this NAS to use single connection mode.')
etsysTacacsClientSesnAuthService = MibScalar((1, 3, 6, 1, 4, 1, 5624, 1, 2, 58, 1, 2, 1), SnmpAdminString().clone('enable')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: etsysTacacsClientSesnAuthService.setStatus('current')
if mibBuilder.loadTexts: etsysTacacsClientSesnAuthService.setDescription('The service to be requested for management session authorization.')
etsysTacacsClientSesnAuthTable = MibTable((1, 3, 6, 1, 4, 1, 5624, 1, 2, 58, 1, 2, 2), )
if mibBuilder.loadTexts: etsysTacacsClientSesnAuthTable.setStatus('current')
if mibBuilder.loadTexts: etsysTacacsClientSesnAuthTable.setDescription('A list of TACACS+ servers that this client may attempt to use.')
etsysTacacsClientSesnAuthEntry = MibTableRow((1, 3, 6, 1, 4, 1, 5624, 1, 2, 58, 1, 2, 2, 1), ).setIndexNames((0, "ENTERASYS-TACACS-CLIENT-MIB", "etsysTacacsClientSesnAuthLevel"))
if mibBuilder.loadTexts: etsysTacacsClientSesnAuthEntry.setStatus('current')
if mibBuilder.loadTexts: etsysTacacsClientSesnAuthEntry.setDescription('A TACACS+ server that this client may attempt to use.')
etsysTacacsClientSesnAuthLevel = MibTableColumn((1, 3, 6, 1, 4, 1, 5624, 1, 2, 58, 1, 2, 2, 1, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))).clone(namedValues=NamedValues(("readonly", 1), ("readwrite", 2), ("superuser", 3), ("debug", 4))))
if mibBuilder.loadTexts: etsysTacacsClientSesnAuthLevel.setStatus('current')
if mibBuilder.loadTexts: etsysTacacsClientSesnAuthLevel.setDescription('The authorization level for the corresponding attribute value pair. Managed entities are not required to support all authorization levels.')
etsysTacacsClientSesnAuthAttribute = MibTableColumn((1, 3, 6, 1, 4, 1, 5624, 1, 2, 58, 1, 2, 2, 1, 2), SnmpAdminString().clone('priv-lvl')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: etsysTacacsClientSesnAuthAttribute.setStatus('current')
if mibBuilder.loadTexts: etsysTacacsClientSesnAuthAttribute.setDescription("The attribute part of the attribute-value pair for this access level. The default value 'priv-lvl' is normally defined to have a corresponding value part with a value between '0' and '15' inclusive.")
etsysTacacsClientSesnAuthValue = MibTableColumn((1, 3, 6, 1, 4, 1, 5624, 1, 2, 58, 1, 2, 2, 1, 3), SnmpAdminString()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: etsysTacacsClientSesnAuthValue.setStatus('current')
if mibBuilder.loadTexts: etsysTacacsClientSesnAuthValue.setDescription("The value part of the attribute-value pair for this access level. To allow the leveraging of existing Cisco 'enable' mode configurations. When 1.) the etsysTacacsClientSesnAuthService object has the value 'enable', 2.) the attribute part of this attribute-value pair is 'priv-lvl', and 3.) the value part of this attribute-value pair represents a numeric value between 0 and 15, inclusive, then the value part of this attribute-value pair specifies the minimum value required for this access level. If any of the above conditions are not met then this value must be an exact match with the value returned from the TACACS+ server. The default values for this object are '0' for read-only, '1' for read-write, and '15' for superuser authorization.")
etsysTacacsClientServerTable = MibTable((1, 3, 6, 1, 4, 1, 5624, 1, 2, 58, 1, 3, 1), )
if mibBuilder.loadTexts: etsysTacacsClientServerTable.setStatus('current')
if mibBuilder.loadTexts: etsysTacacsClientServerTable.setDescription('A list of TACACS+ servers that this client may attempt to use.')
etsysTacacsClientServerEntry = MibTableRow((1, 3, 6, 1, 4, 1, 5624, 1, 2, 58, 1, 3, 1, 1), ).setIndexNames((0, "ENTERASYS-TACACS-CLIENT-MIB", "etsysTacacsClientServerIndex"))
if mibBuilder.loadTexts: etsysTacacsClientServerEntry.setStatus('current')
if mibBuilder.loadTexts: etsysTacacsClientServerEntry.setDescription('A TACACS+ server that this client may attempt to use.')
etsysTacacsClientServerIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 5624, 1, 2, 58, 1, 3, 1, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 2147483647)))
if mibBuilder.loadTexts: etsysTacacsClientServerIndex.setStatus('current')
if mibBuilder.loadTexts: etsysTacacsClientServerIndex.setDescription('A number uniquely identifying each conceptual row in the etsysTacacsClientServerTable. In the event of an agent restart, the same value of etsysTacacsClientServerIndex must be used to identify each conceptual row in etsysTacacsClientServerTable as prior to the restart.')
etsysTacacsClientServerAddressType = MibTableColumn((1, 3, 6, 1, 4, 1, 5624, 1, 2, 58, 1, 3, 1, 1, 2), InetAddressType().clone('ipv4')).setMaxAccess("readcreate")
if mibBuilder.loadTexts: etsysTacacsClientServerAddressType.setStatus('current')
if mibBuilder.loadTexts: etsysTacacsClientServerAddressType.setDescription('The type of Internet address by which this TACACS+ server is reachable.')
etsysTacacsClientServerAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 5624, 1, 2, 58, 1, 3, 1, 1, 3), InetAddress().subtype(subtypeSpec=ValueSizeConstraint(1, 64))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: etsysTacacsClientServerAddress.setStatus('current')
if mibBuilder.loadTexts: etsysTacacsClientServerAddress.setDescription('The Internet address for the TACACS+ server. The etsysTacacsClientServerAddress may not be empty due to the SIZE restriction. Also the size of a DNS name is limited to 64 characters. If a row is created administratively by an SNMP operation and the address type value is dns(16), then the agent stores the DNS name internally. A DNS name lookup must be performed on the internally stored DNS name whenever it is being used to contact the peer. If a row is created by the managed entity itself and the address type value is dns(16), then the agent stores the IP address internally. A DNS reverse lookup must be performed on the internally stored IP address whenever the value is retrieved via SNMP.')
etsysTacacsClientServerPortNumber = MibTableColumn((1, 3, 6, 1, 4, 1, 5624, 1, 2, 58, 1, 3, 1, 1, 4), InetPortNumber().clone(49)).setMaxAccess("readcreate")
if mibBuilder.loadTexts: etsysTacacsClientServerPortNumber.setStatus('current')
if mibBuilder.loadTexts: etsysTacacsClientServerPortNumber.setDescription('The TCP port number (0-65535) the client is using to send requests to this server.')
etsysTacacsClientServerTimeout = MibTableColumn((1, 3, 6, 1, 4, 1, 5624, 1, 2, 58, 1, 3, 1, 1, 5), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 180)).clone(10)).setUnits('seconds').setMaxAccess("readwrite")
if mibBuilder.loadTexts: etsysTacacsClientServerTimeout.setStatus('current')
if mibBuilder.loadTexts: etsysTacacsClientServerTimeout.setDescription('The number of seconds to wait for a TACACS+ server to respond to a request.')
etsysTacacsClientServerSecret = MibTableColumn((1, 3, 6, 1, 4, 1, 5624, 1, 2, 58, 1, 3, 1, 1, 6), OctetString().subtype(subtypeSpec=ValueSizeConstraint(0, 32))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: etsysTacacsClientServerSecret.setStatus('current')
if mibBuilder.loadTexts: etsysTacacsClientServerSecret.setDescription('This object is the secret shared between the TACACS+ server and TACACS+ client.')
etsysTacacsClientServerSecretEntered = MibTableColumn((1, 3, 6, 1, 4, 1, 5624, 1, 2, 58, 1, 3, 1, 1, 7), TruthValue()).setMaxAccess("readonly")
if mibBuilder.loadTexts: etsysTacacsClientServerSecretEntered.setStatus('current')
if mibBuilder.loadTexts: etsysTacacsClientServerSecretEntered.setDescription('This indicates the existence of a shared secret.')
etsysTacacsClientServerStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 5624, 1, 2, 58, 1, 3, 1, 1, 8), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: etsysTacacsClientServerStatus.setStatus('current')
if mibBuilder.loadTexts: etsysTacacsClientServerStatus.setDescription("Lets users create and delete TACACS+ server entries on systems that support this capability. Rules 1. When creating a TACACS+ client, it is up to the management station to determine a suitable etsysTacacsClientServerIndex. To facilitate interoperability, agents should not put any restrictions on the etsysTacacsClientServerIndex beyond the obvious ones that it be valid and unused. 2. Before a new row can become 'active', values must be supplied for the columnar objects etsysTacacsClientServerAddress and etsysTacacsClientServerSecret. 3. The value of etsysTacacsClientServerStatus MAY need to be set to 'notInService' in order to modify a writable object in the same conceptual row. 4. etsysTacacsClientServer entries whose status is 'notReady' or 'notInService' will not be used for authentication.")
etsysTacacsClientConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 5624, 1, 2, 58, 2))
etsysTacacsClientCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 5624, 1, 2, 58, 2, 1))
etsysTacacsClientGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 5624, 1, 2, 58, 2, 2))
etsysTacacsClientSessionGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 5624, 1, 2, 58, 2, 2, 1)).setObjects(("ENTERASYS-TACACS-CLIENT-MIB", "etsysTacacsClientSesnAuthEnabled"), ("ENTERASYS-TACACS-CLIENT-MIB", "etsysTacacsClientSesnAcctEnabled"), ("ENTERASYS-TACACS-CLIENT-MIB", "etsysTacacsClientSingleConnection"), ("ENTERASYS-TACACS-CLIENT-MIB", "etsysTacacsClientServerAddressType"), ("ENTERASYS-TACACS-CLIENT-MIB", "etsysTacacsClientServerAddress"), ("ENTERASYS-TACACS-CLIENT-MIB", "etsysTacacsClientServerPortNumber"), ("ENTERASYS-TACACS-CLIENT-MIB", "etsysTacacsClientServerTimeout"), ("ENTERASYS-TACACS-CLIENT-MIB", "etsysTacacsClientServerSecret"), ("ENTERASYS-TACACS-CLIENT-MIB", "etsysTacacsClientServerSecretEntered"), ("ENTERASYS-TACACS-CLIENT-MIB", "etsysTacacsClientServerStatus"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    etsysTacacsClientSessionGroup = etsysTacacsClientSessionGroup.setStatus('current')
if mibBuilder.loadTexts: etsysTacacsClientSessionGroup.setDescription('The collection of objects required to do TACACS+ authentication, authorization, and accounting for management sessions.')
etsysTacacsClientCmdAuthGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 5624, 1, 2, 58, 2, 2, 2)).setObjects(("ENTERASYS-TACACS-CLIENT-MIB", "etsysTacacsClientCmdAuthEnabled"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    etsysTacacsClientCmdAuthGroup = etsysTacacsClientCmdAuthGroup.setStatus('current')
if mibBuilder.loadTexts: etsysTacacsClientCmdAuthGroup.setDescription('Additional objects for TACACS+ command authorization.')
etsysTacacsClientCmdAcctGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 5624, 1, 2, 58, 2, 2, 3)).setObjects(("ENTERASYS-TACACS-CLIENT-MIB", "etsysTacacsClientCmdAcctEnabled"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    etsysTacacsClientCmdAcctGroup = etsysTacacsClientCmdAcctGroup.setStatus('current')
if mibBuilder.loadTexts: etsysTacacsClientCmdAcctGroup.setDescription('Additional objects for TACACS+ command accounting.')
etsysTacacsClientSesnAuthGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 5624, 1, 2, 58, 2, 2, 4)).setObjects(("ENTERASYS-TACACS-CLIENT-MIB", "etsysTacacsClientSesnAuthService"), ("ENTERASYS-TACACS-CLIENT-MIB", "etsysTacacsClientSesnAuthAttribute"), ("ENTERASYS-TACACS-CLIENT-MIB", "etsysTacacsClientSesnAuthValue"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    etsysTacacsClientSesnAuthGroup = etsysTacacsClientSesnAuthGroup.setStatus('current')
if mibBuilder.loadTexts: etsysTacacsClientSesnAuthGroup.setDescription('Additional objects to map read-only, read-write, superuser, and debug authorization level into a service level and respective attribute-value pairs.')
etsysTacacsClientCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 5624, 1, 2, 58, 2, 1, 1)).setObjects(("ENTERASYS-TACACS-CLIENT-MIB", "etsysTacacsClientSessionGroup"), ("ENTERASYS-TACACS-CLIENT-MIB", "etsysTacacsClientCmdAuthGroup"), ("ENTERASYS-TACACS-CLIENT-MIB", "etsysTacacsClientCmdAcctGroup"), ("ENTERASYS-TACACS-CLIENT-MIB", "etsysTacacsClientSesnAuthGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    etsysTacacsClientCompliance = etsysTacacsClientCompliance.setStatus('current')
if mibBuilder.loadTexts: etsysTacacsClientCompliance.setDescription('The compliance statement for clients implementing the TACACS+ Client MIB.')
mibBuilder.exportSymbols("ENTERASYS-TACACS-CLIENT-MIB", etsysTacacsClientCmdAcctGroup=etsysTacacsClientCmdAcctGroup, etsysTacacsClientSesnAuth=etsysTacacsClientSesnAuth, etsysTacacsClientSesnAuthTable=etsysTacacsClientSesnAuthTable, etsysTacacsClientServerSecretEntered=etsysTacacsClientServerSecretEntered, etsysTacacsClientCmdAuthGroup=etsysTacacsClientCmdAuthGroup, etsysTacacsClientSesnAcctEnabled=etsysTacacsClientSesnAcctEnabled, etsysTacacsClientCmdAcctEnabled=etsysTacacsClientCmdAcctEnabled, PYSNMP_MODULE_ID=etsysTacacsClientMIB, etsysTacacsClientSesnAuthLevel=etsysTacacsClientSesnAuthLevel, etsysTacacsClientServerIndex=etsysTacacsClientServerIndex, etsysTacacsClientServer=etsysTacacsClientServer, etsysTacacsClientCompliances=etsysTacacsClientCompliances, etsysTacacsClientConformance=etsysTacacsClientConformance, etsysTacacsClientServerEntry=etsysTacacsClientServerEntry, etsysTacacsClientMIB=etsysTacacsClientMIB, etsysTacacsClientCompliance=etsysTacacsClientCompliance, etsysTacacsClientServerTimeout=etsysTacacsClientServerTimeout, etsysTacacsClientServerAddressType=etsysTacacsClientServerAddressType, etsysTacacsClientServerStatus=etsysTacacsClientServerStatus, etsysTacacsClientSesnAuthGroup=etsysTacacsClientSesnAuthGroup, etsysTacacsClientServerPortNumber=etsysTacacsClientServerPortNumber, etsysTacacsClientSesnAuthService=etsysTacacsClientSesnAuthService, etsysTacacsClientSessionGroup=etsysTacacsClientSessionGroup, etsysTacacsClientControl=etsysTacacsClientControl, etsysTacacsClientServerAddress=etsysTacacsClientServerAddress, etsysTacacsClientSesnAuthEnabled=etsysTacacsClientSesnAuthEnabled, etsysTacacsClientSingleConnection=etsysTacacsClientSingleConnection, etsysTacacsClientServerSecret=etsysTacacsClientServerSecret, etsysTacacsClientObjects=etsysTacacsClientObjects, etsysTacacsClientServerTable=etsysTacacsClientServerTable, etsysTacacsClientSesnAuthAttribute=etsysTacacsClientSesnAuthAttribute, etsysTacacsClientGroups=etsysTacacsClientGroups, etsysTacacsClientCmdAuthEnabled=etsysTacacsClientCmdAuthEnabled, etsysTacacsClientSesnAuthEntry=etsysTacacsClientSesnAuthEntry, etsysTacacsClientSesnAuthValue=etsysTacacsClientSesnAuthValue)