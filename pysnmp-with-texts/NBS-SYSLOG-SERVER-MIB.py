#
# PySNMP MIB module NBS-SYSLOG-SERVER-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/NBS-SYSLOG-SERVER-MIB
# Produced by pysmi-0.3.4 at Wed May  1 14:17:44 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
Integer, OctetString, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "Integer", "OctetString", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
SingleValueConstraint, ValueRangeConstraint, ConstraintsUnion, ValueSizeConstraint, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "SingleValueConstraint", "ValueRangeConstraint", "ConstraintsUnion", "ValueSizeConstraint", "ConstraintsIntersection")
nbs, = mibBuilder.importSymbols("NBS-CMMC-MIB", "nbs")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
Gauge32, NotificationType, TimeTicks, MibIdentifier, Bits, Unsigned32, Counter64, ObjectIdentity, iso, Integer32, Counter32, ModuleIdentity, IpAddress, MibScalar, MibTable, MibTableRow, MibTableColumn = mibBuilder.importSymbols("SNMPv2-SMI", "Gauge32", "NotificationType", "TimeTicks", "MibIdentifier", "Bits", "Unsigned32", "Counter64", "ObjectIdentity", "iso", "Integer32", "Counter32", "ModuleIdentity", "IpAddress", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
nbsSyslogServerMib = ModuleIdentity((1, 3, 6, 1, 4, 1, 629, 206))
if mibBuilder.loadTexts: nbsSyslogServerMib.setLastUpdated('200902040000Z')
if mibBuilder.loadTexts: nbsSyslogServerMib.setOrganization('NBS')
if mibBuilder.loadTexts: nbsSyslogServerMib.setContactInfo('For technical support, please contact your service channel')
if mibBuilder.loadTexts: nbsSyslogServerMib.setDescription('MIB for representing NBS remote syslog servers')
class InetAddressType(TextualConvention, Integer32):
    description = 'A value that represents a type of Internet address. unknown(0) An unknown address type. This value MUST be used if the value of the corresponding InetAddress object is a zero-length string. It may also be used to indicate an IP address that is not in one of the formats defined below. ipv4(1) An IPv4 address as defined by the InetAddressIPv4 textual convention. ipv6(2) An IPv6 address as defined by the InetAddressIPv6 textual convention. ipv4z(3) A non-global IPv4 address including a zone index as defined by the InetAddressIPv4z textual convention. ipv6z(4) A non-global IPv6 address including a zone index as defined by the InetAddressIPv6z textual convention. dns(16) A DNS domain name as defined by the InetAddressDNS textual convention. Each definition of a concrete InetAddressType value must be accompanied by a definition of a textual convention for use with that InetAddressType. To support future extensions, the InetAddressType textual convention SHOULD NOT be sub-typed in object type definitions. It MAY be sub-typed in compliance statements in order to require only a subset of these address types for a compliant implementation. Implementations must ensure that InetAddressType objects and any dependent objects (e.g., InetAddress objects) are consistent. An inconsistentValue error must be generated if an attempt to change an InetAddressType object would, for example, lead to an undefined InetAddress value. In particular, InetAddressType/InetAddress pairs must be changed together if the address type changes (e.g., from ipv6(2) to ipv4(1)).'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3, 4, 16))
    namedValues = NamedValues(("unknown", 0), ("ipv4", 1), ("ipv6", 2), ("ipv4z", 3), ("ipv6z", 4), ("dns", 16))

nbsSyslogServerGrp = ObjectIdentity((1, 3, 6, 1, 4, 1, 629, 206, 1))
if mibBuilder.loadTexts: nbsSyslogServerGrp.setStatus('current')
if mibBuilder.loadTexts: nbsSyslogServerGrp.setDescription('Meta MIB')
nbsSyslogServerTableSize = MibScalar((1, 3, 6, 1, 4, 1, 629, 206, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: nbsSyslogServerTableSize.setStatus('current')
if mibBuilder.loadTexts: nbsSyslogServerTableSize.setDescription('The number of entries in nbsSyslogServerTable table.')
nbsSyslogServerTable = MibTable((1, 3, 6, 1, 4, 1, 629, 206, 1, 2), )
if mibBuilder.loadTexts: nbsSyslogServerTable.setStatus('current')
if mibBuilder.loadTexts: nbsSyslogServerTable.setDescription('Syslog messages will be sent to every active server in the table.')
nbsSyslogServerEntry = MibTableRow((1, 3, 6, 1, 4, 1, 629, 206, 1, 2, 1), ).setIndexNames((0, "NBS-SYSLOG-SERVER-MIB", "nbsSyslogServerIndex"))
if mibBuilder.loadTexts: nbsSyslogServerEntry.setStatus('current')
if mibBuilder.loadTexts: nbsSyslogServerEntry.setDescription('A remote syslog server.')
nbsSyslogServerIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 629, 206, 1, 2, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 5)))
if mibBuilder.loadTexts: nbsSyslogServerIndex.setStatus('current')
if mibBuilder.loadTexts: nbsSyslogServerIndex.setDescription('The index of the entry/row in the syslog table.')
nbsSyslogServerStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 629, 206, 1, 2, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("invalid", 1), ("active", 2))).clone('invalid')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: nbsSyslogServerStatus.setStatus('current')
if mibBuilder.loadTexts: nbsSyslogServerStatus.setDescription("This object is used to get/set the validity of the information contained by nbsSyslogServerEntry row. Setting this object to the value invalid(1) has the effect of deleting the corresponding nbsSyslogServerTable entry. Deleting an entry has the effect of initializing it to default values : IpAddr = 0.0.0.0, Port = 0 etc. Setting this object to the value active(2) entry has the effect of creating a new row in the nbsSyslogServerTable object, if an entry with the same nbsSyslogServerIpAddr does not exist. If such an entry exists, then a 'badValue' error will be returned. The GET operations will receive a value of active(2) for existing entries. An invalid(1) value indicates an entry that was deleted by a previous SET operation.")
nbsSyslogServerAddressType = MibTableColumn((1, 3, 6, 1, 4, 1, 629, 206, 1, 2, 1, 3), InetAddressType().clone('ipv4')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: nbsSyslogServerAddressType.setStatus('current')
if mibBuilder.loadTexts: nbsSyslogServerAddressType.setDescription('The address type of nbsSyslogServerAddress. Currently only ipv4 is supported.')
nbsSyslogServerAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 629, 206, 1, 2, 1, 4), IpAddress()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: nbsSyslogServerAddress.setStatus('current')
if mibBuilder.loadTexts: nbsSyslogServerAddress.setDescription('IP address of a remote server that should be sent syslog messages.')
nbsSyslogServerPort = MibTableColumn((1, 3, 6, 1, 4, 1, 629, 206, 1, 2, 1, 5), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(0, 65535)).clone(514)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: nbsSyslogServerPort.setStatus('current')
if mibBuilder.loadTexts: nbsSyslogServerPort.setDescription('UDP port of the remote syslog server. The default port is 514.')
nbsSyslogServerLevel = MibTableColumn((1, 3, 6, 1, 4, 1, 629, 206, 1, 2, 1, 6), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 8, 9))).clone(namedValues=NamedValues(("disabled", 1), ("emerg", 2), ("alert", 3), ("crit", 4), ("error", 5), ("warning", 6), ("notice", 7), ("info", 8), ("debug", 9))).clone('warning')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: nbsSyslogServerLevel.setStatus('current')
if mibBuilder.loadTexts: nbsSyslogServerLevel.setDescription('Indicates the level of messages that are sent to this syslog server.')
mibBuilder.exportSymbols("NBS-SYSLOG-SERVER-MIB", nbsSyslogServerLevel=nbsSyslogServerLevel, nbsSyslogServerTable=nbsSyslogServerTable, nbsSyslogServerAddressType=nbsSyslogServerAddressType, InetAddressType=InetAddressType, nbsSyslogServerPort=nbsSyslogServerPort, nbsSyslogServerStatus=nbsSyslogServerStatus, nbsSyslogServerTableSize=nbsSyslogServerTableSize, nbsSyslogServerEntry=nbsSyslogServerEntry, nbsSyslogServerGrp=nbsSyslogServerGrp, nbsSyslogServerIndex=nbsSyslogServerIndex, nbsSyslogServerAddress=nbsSyslogServerAddress, nbsSyslogServerMib=nbsSyslogServerMib, PYSNMP_MODULE_ID=nbsSyslogServerMib)