#
# PySNMP MIB module HH3C-LswDHCP-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/HH3C-LswDHCP-MIB
# Produced by pysmi-0.3.4 at Wed May  1 13:28:01 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ValueSizeConstraint, ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ValueSizeConstraint", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion")
hh3clswCommon, = mibBuilder.importSymbols("HH3C-OID-MIB", "hh3clswCommon")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
MibScalar, MibTable, MibTableRow, MibTableColumn, NotificationType, Counter32, Bits, IpAddress, ObjectIdentity, TimeTicks, iso, Gauge32, Unsigned32, ModuleIdentity, Counter64, Integer32, MibIdentifier = mibBuilder.importSymbols("SNMPv2-SMI", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "NotificationType", "Counter32", "Bits", "IpAddress", "ObjectIdentity", "TimeTicks", "iso", "Gauge32", "Unsigned32", "ModuleIdentity", "Counter64", "Integer32", "MibIdentifier")
DisplayString, MacAddress, TextualConvention, RowStatus = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "MacAddress", "TextualConvention", "RowStatus")
hh3cLswDhcpMib = ModuleIdentity((1, 3, 6, 1, 4, 1, 25506, 8, 35, 8))
hh3cLswDhcpMib.setRevisions(('2001-06-29 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: hh3cLswDhcpMib.setRevisionsDescriptions(('',))
if mibBuilder.loadTexts: hh3cLswDhcpMib.setLastUpdated('200106290000Z')
if mibBuilder.loadTexts: hh3cLswDhcpMib.setOrganization('Hangzhou H3C Tech. Co., Ltd.')
if mibBuilder.loadTexts: hh3cLswDhcpMib.setContactInfo('Platform Team Hangzhou H3C Tech. Co., Ltd. Hai-Dian District Beijing P.R. China http://www.h3c.com Zip:100085 ')
if mibBuilder.loadTexts: hh3cLswDhcpMib.setDescription('')
hh3cLswDhcpMibObject = MibIdentifier((1, 3, 6, 1, 4, 1, 25506, 8, 35, 8, 1))
hh3cDhcpGroupTable = MibTable((1, 3, 6, 1, 4, 1, 25506, 8, 35, 8, 1, 1), )
if mibBuilder.loadTexts: hh3cDhcpGroupTable.setStatus('current')
if mibBuilder.loadTexts: hh3cDhcpGroupTable.setDescription('A table containing the information of dhcp group ')
hh3cDhcpGroupEntry = MibTableRow((1, 3, 6, 1, 4, 1, 25506, 8, 35, 8, 1, 1, 1), ).setIndexNames((0, "HH3C-LswDHCP-MIB", "hh3cDhcpGroupID"))
if mibBuilder.loadTexts: hh3cDhcpGroupEntry.setStatus('current')
if mibBuilder.loadTexts: hh3cDhcpGroupEntry.setDescription('A table entry containing the information of dhcp group ')
hh3cDhcpGroupID = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 8, 35, 8, 1, 1, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 19))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hh3cDhcpGroupID.setStatus('current')
if mibBuilder.loadTexts: hh3cDhcpGroupID.setDescription(' DHCP group identifier ')
hh3cIpDhcpServerAddress1 = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 8, 35, 8, 1, 1, 1, 2), IpAddress()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hh3cIpDhcpServerAddress1.setStatus('current')
if mibBuilder.loadTexts: hh3cIpDhcpServerAddress1.setDescription(' The first IP address of DHCP server group ')
hh3cIpDhcpServerAddress2 = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 8, 35, 8, 1, 1, 1, 3), IpAddress()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hh3cIpDhcpServerAddress2.setStatus('current')
if mibBuilder.loadTexts: hh3cIpDhcpServerAddress2.setDescription(' The second IP address of DHCP server group ')
hh3cDhcpRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 8, 35, 8, 1, 1, 1, 4), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hh3cDhcpRowStatus.setStatus('current')
if mibBuilder.loadTexts: hh3cDhcpRowStatus.setDescription(' Operation status of this table entry ')
hh3cDhcpSecurityTable = MibTable((1, 3, 6, 1, 4, 1, 25506, 8, 35, 8, 1, 2), )
if mibBuilder.loadTexts: hh3cDhcpSecurityTable.setStatus('current')
if mibBuilder.loadTexts: hh3cDhcpSecurityTable.setDescription('A table containing the information of dhcp security ')
hh3cDhcpSecurityEntry = MibTableRow((1, 3, 6, 1, 4, 1, 25506, 8, 35, 8, 1, 2, 1), ).setIndexNames((0, "HH3C-LswDHCP-MIB", "hh3cDhcpClientIpAddress"))
if mibBuilder.loadTexts: hh3cDhcpSecurityEntry.setStatus('current')
if mibBuilder.loadTexts: hh3cDhcpSecurityEntry.setDescription('A table containing the information of dhcp security ')
hh3cDhcpClientIpAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 8, 35, 8, 1, 2, 1, 1), IpAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hh3cDhcpClientIpAddress.setStatus('current')
if mibBuilder.loadTexts: hh3cDhcpClientIpAddress.setDescription(" DHCP client's net ip address ")
hh3cDhcpClientMacAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 8, 35, 8, 1, 2, 1, 2), MacAddress()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hh3cDhcpClientMacAddress.setStatus('current')
if mibBuilder.loadTexts: hh3cDhcpClientMacAddress.setDescription(" DHCP client's mac address ")
hh3cDhcpClientProperty = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 8, 35, 8, 1, 2, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("static", 1), ("dynamic", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hh3cDhcpClientProperty.setStatus('current')
if mibBuilder.loadTexts: hh3cDhcpClientProperty.setDescription(' Property of client address ')
hh3cDhcpClientRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 8, 35, 8, 1, 2, 1, 4), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hh3cDhcpClientRowStatus.setStatus('current')
if mibBuilder.loadTexts: hh3cDhcpClientRowStatus.setDescription(" status of this table's entry. ")
hh3cDhcpToL3IfTable = MibTable((1, 3, 6, 1, 4, 1, 25506, 8, 35, 8, 1, 3), )
if mibBuilder.loadTexts: hh3cDhcpToL3IfTable.setStatus('current')
if mibBuilder.loadTexts: hh3cDhcpToL3IfTable.setDescription('A table configuring dhcp for layer 3 interface')
hh3cDhcpToL3IfEntry = MibTableRow((1, 3, 6, 1, 4, 1, 25506, 8, 35, 8, 1, 3, 1), ).setIndexNames((0, "HH3C-LswDHCP-MIB", "hh3cDhcpToL3VlanIfIndex"))
if mibBuilder.loadTexts: hh3cDhcpToL3IfEntry.setStatus('current')
if mibBuilder.loadTexts: hh3cDhcpToL3IfEntry.setDescription('A table configuring dhcp for layer 3 interface ')
hh3cDhcpToL3VlanIfIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 8, 35, 8, 1, 3, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hh3cDhcpToL3VlanIfIndex.setStatus('current')
if mibBuilder.loadTexts: hh3cDhcpToL3VlanIfIndex.setDescription(' vlan virtual interface index ')
hh3cDhcpToL3GroupId = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 8, 35, 8, 1, 3, 1, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 19))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hh3cDhcpToL3GroupId.setStatus('current')
if mibBuilder.loadTexts: hh3cDhcpToL3GroupId.setDescription(' DHCP group id for this vlan virtual interface')
hh3cDhcpToL3AddressCheck = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 8, 35, 8, 1, 3, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enabled", 1), ("disabled", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hh3cDhcpToL3AddressCheck.setStatus('current')
if mibBuilder.loadTexts: hh3cDhcpToL3AddressCheck.setDescription(' If dhcp security check enabled for this vlan virtual interface ')
hh3cDhcpToL3RowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 8, 35, 8, 1, 3, 1, 4), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hh3cDhcpToL3RowStatus.setStatus('current')
if mibBuilder.loadTexts: hh3cDhcpToL3RowStatus.setDescription(" status of this table's entry. ")
mibBuilder.exportSymbols("HH3C-LswDHCP-MIB", hh3cDhcpToL3AddressCheck=hh3cDhcpToL3AddressCheck, hh3cDhcpGroupID=hh3cDhcpGroupID, hh3cLswDhcpMib=hh3cLswDhcpMib, hh3cDhcpSecurityEntry=hh3cDhcpSecurityEntry, hh3cDhcpClientRowStatus=hh3cDhcpClientRowStatus, hh3cDhcpToL3RowStatus=hh3cDhcpToL3RowStatus, hh3cDhcpClientProperty=hh3cDhcpClientProperty, PYSNMP_MODULE_ID=hh3cLswDhcpMib, hh3cDhcpGroupTable=hh3cDhcpGroupTable, hh3cDhcpGroupEntry=hh3cDhcpGroupEntry, hh3cDhcpToL3IfEntry=hh3cDhcpToL3IfEntry, hh3cDhcpClientIpAddress=hh3cDhcpClientIpAddress, hh3cDhcpToL3IfTable=hh3cDhcpToL3IfTable, hh3cDhcpRowStatus=hh3cDhcpRowStatus, hh3cIpDhcpServerAddress1=hh3cIpDhcpServerAddress1, hh3cDhcpSecurityTable=hh3cDhcpSecurityTable, hh3cLswDhcpMibObject=hh3cLswDhcpMibObject, hh3cIpDhcpServerAddress2=hh3cIpDhcpServerAddress2, hh3cDhcpToL3VlanIfIndex=hh3cDhcpToL3VlanIfIndex, hh3cDhcpToL3GroupId=hh3cDhcpToL3GroupId, hh3cDhcpClientMacAddress=hh3cDhcpClientMacAddress)