#
# PySNMP MIB module PDN-INET-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/PDN-INET-MIB
# Produced by pysmi-0.3.4 at Wed May  1 14:39:04 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
Integer, OctetString, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "Integer", "OctetString", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsUnion, ValueRangeConstraint, ConstraintsIntersection, SingleValueConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsUnion", "ValueRangeConstraint", "ConstraintsIntersection", "SingleValueConstraint")
ifIndex, = mibBuilder.importSymbols("IF-MIB", "ifIndex")
pdn_inet, = mibBuilder.importSymbols("PDN-HEADER-MIB", "pdn-inet")
InetAddressType, = mibBuilder.importSymbols("PDN-TC", "InetAddressType")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
NotificationType, Unsigned32, Counter64, ObjectIdentity, MibIdentifier, iso, TimeTicks, ModuleIdentity, Gauge32, MibScalar, MibTable, MibTableRow, MibTableColumn, IpAddress, Integer32, NotificationType, Counter32, Bits = mibBuilder.importSymbols("SNMPv2-SMI", "NotificationType", "Unsigned32", "Counter64", "ObjectIdentity", "MibIdentifier", "iso", "TimeTicks", "ModuleIdentity", "Gauge32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "IpAddress", "Integer32", "NotificationType", "Counter32", "Bits")
TextualConvention, DisplayString, RowStatus = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString", "RowStatus")
pdnInetMIBObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 26, 1))
pdnInetMIBTraps = MibIdentifier((1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 26, 2))
pdnInetTelnetServerPort = MibScalar((1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 26, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 65535)).clone(23)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: pdnInetTelnetServerPort.setStatus('mandatory')
if mibBuilder.loadTexts: pdnInetTelnetServerPort.setDescription('This object contains the telnet server (daemon) tcp port number.')
pdnInetFtpServerControlPort = MibScalar((1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 26, 1, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 65535)).clone(21)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: pdnInetFtpServerControlPort.setStatus('mandatory')
if mibBuilder.loadTexts: pdnInetFtpServerControlPort.setDescription('This object contains the ftp server control (daemon) tcp port number.')
pdnInetFtpServerDataPort = MibScalar((1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 26, 1, 3), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 65535)).clone(20)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: pdnInetFtpServerDataPort.setStatus('mandatory')
if mibBuilder.loadTexts: pdnInetFtpServerDataPort.setDescription('This object contains the ftp server data connection tcp port number.')
pdnInetIpAddressTableMaxIpSubnets = MibScalar((1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 26, 1, 4), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: pdnInetIpAddressTableMaxIpSubnets.setStatus('mandatory')
if mibBuilder.loadTexts: pdnInetIpAddressTableMaxIpSubnets.setDescription('This object indicates the maximum number of entries in the pdnInetAddressTable')
pdnInetIpAddressTableCurrentIpSubnets = MibScalar((1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 26, 1, 5), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: pdnInetIpAddressTableCurrentIpSubnets.setStatus('mandatory')
if mibBuilder.loadTexts: pdnInetIpAddressTableCurrentIpSubnets.setDescription('This object indicates the number of entries configured in the pdnInetAddressTable')
pdnInetIpAddressTable = MibTable((1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 26, 1, 6), )
if mibBuilder.loadTexts: pdnInetIpAddressTable.setStatus('mandatory')
if mibBuilder.loadTexts: pdnInetIpAddressTable.setDescription('This table used to configure ipaddresses for an interface which support the internet (IP) protocol')
pdnInetIpAddressTableEntry = MibTableRow((1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 26, 1, 6, 1), ).setIndexNames((0, "IF-MIB", "ifIndex"), (0, "PDN-INET-MIB", "pdnInetIpAddress"))
if mibBuilder.loadTexts: pdnInetIpAddressTableEntry.setStatus('mandatory')
if mibBuilder.loadTexts: pdnInetIpAddressTableEntry.setDescription('This object corresponds to an entry in the IP address table.')
pdnInetIpAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 26, 1, 6, 1, 1), IpAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: pdnInetIpAddress.setStatus('mandatory')
if mibBuilder.loadTexts: pdnInetIpAddress.setDescription('This object is used to configure an IP address for an interface')
pdnInetIpSubnetMask = MibTableColumn((1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 26, 1, 6, 1, 2), IpAddress()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: pdnInetIpSubnetMask.setStatus('mandatory')
if mibBuilder.loadTexts: pdnInetIpSubnetMask.setDescription('This object is used to configure an IP subnet mask for an interface. subnet mask should result in contiguous subnets')
pdnInetIpAddressType = MibTableColumn((1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 26, 1, 6, 1, 3), InetAddressType()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: pdnInetIpAddressType.setStatus('mandatory')
if mibBuilder.loadTexts: pdnInetIpAddressType.setDescription('This object is used to configure the address type for an interface an interface can have only one primary ip address and more than one secondary ip address. the primary ip address is essentially the router ID. The secondary ip address would result in the interface being multi-homed.')
pdnInetIpRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 26, 1, 6, 1, 4), RowStatus()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: pdnInetIpRowStatus.setStatus('mandatory')
if mibBuilder.loadTexts: pdnInetIpRowStatus.setDescription('This object is used to manage rows (add/delete/modify) in this table')
mibBuilder.exportSymbols("PDN-INET-MIB", pdnInetIpRowStatus=pdnInetIpRowStatus, pdnInetMIBObjects=pdnInetMIBObjects, pdnInetTelnetServerPort=pdnInetTelnetServerPort, pdnInetIpAddressTableMaxIpSubnets=pdnInetIpAddressTableMaxIpSubnets, pdnInetIpAddressTableCurrentIpSubnets=pdnInetIpAddressTableCurrentIpSubnets, pdnInetIpAddressTable=pdnInetIpAddressTable, pdnInetIpAddressTableEntry=pdnInetIpAddressTableEntry, pdnInetIpAddress=pdnInetIpAddress, pdnInetIpAddressType=pdnInetIpAddressType, pdnInetMIBTraps=pdnInetMIBTraps, pdnInetFtpServerDataPort=pdnInetFtpServerDataPort, pdnInetFtpServerControlPort=pdnInetFtpServerControlPort, pdnInetIpSubnetMask=pdnInetIpSubnetMask)