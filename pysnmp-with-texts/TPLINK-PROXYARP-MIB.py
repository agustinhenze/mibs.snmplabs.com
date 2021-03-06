#
# PySNMP MIB module TPLINK-PROXYARP-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/TPLINK-PROXYARP-MIB
# Produced by pysmi-0.3.4 at Wed May  1 15:25:41 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
ObjectIdentifier, Integer, OctetString = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "Integer", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, ValueSizeConstraint, ConstraintsUnion, ConstraintsIntersection, SingleValueConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "ValueSizeConstraint", "ConstraintsUnion", "ConstraintsIntersection", "SingleValueConstraint")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
ModuleIdentity, Gauge32, ObjectIdentity, TimeTicks, Counter32, iso, Counter64, Unsigned32, IpAddress, Bits, MibScalar, MibTable, MibTableRow, MibTableColumn, MibIdentifier, NotificationType, Integer32 = mibBuilder.importSymbols("SNMPv2-SMI", "ModuleIdentity", "Gauge32", "ObjectIdentity", "TimeTicks", "Counter32", "iso", "Counter64", "Unsigned32", "IpAddress", "Bits", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "MibIdentifier", "NotificationType", "Integer32")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
tplinkMgmt, = mibBuilder.importSymbols("TPLINK-MIB", "tplinkMgmt")
tplinkProxyArpMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 11863, 6, 37))
tplinkProxyArpMIB.setRevisions(('2012-12-13 09:30',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: tplinkProxyArpMIB.setRevisionsDescriptions(('Initial version of this MIB module.',))
if mibBuilder.loadTexts: tplinkProxyArpMIB.setLastUpdated('201212130930Z')
if mibBuilder.loadTexts: tplinkProxyArpMIB.setOrganization('TPLINK')
if mibBuilder.loadTexts: tplinkProxyArpMIB.setContactInfo('www.tplink.com.cn')
if mibBuilder.loadTexts: tplinkProxyArpMIB.setDescription('Private MIB for proxy arp configuration.')
tplinkProxyArpMIBObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 11863, 6, 37, 1))
tplinkProxyArpNotifications = MibIdentifier((1, 3, 6, 1, 4, 1, 11863, 6, 37, 2))
tpProxyArpConfig = MibIdentifier((1, 3, 6, 1, 4, 1, 11863, 6, 37, 1))
tpProxyArpTable = MibTable((1, 3, 6, 1, 4, 1, 11863, 6, 37, 1, 1), )
if mibBuilder.loadTexts: tpProxyArpTable.setStatus('current')
if mibBuilder.loadTexts: tpProxyArpTable.setDescription('Proxy Arp.')
tpProxyArpEntry = MibTableRow((1, 3, 6, 1, 4, 1, 11863, 6, 37, 1, 1, 1), ).setIndexNames((0, "TPLINK-PROXYARP-MIB", "tpProxyArpVlanId"))
if mibBuilder.loadTexts: tpProxyArpEntry.setStatus('current')
if mibBuilder.loadTexts: tpProxyArpEntry.setDescription('An entry contains of the information of port configure.')
tpProxyArpVlanId = MibTableColumn((1, 3, 6, 1, 4, 1, 11863, 6, 37, 1, 1, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 4094))).setMaxAccess("readonly")
if mibBuilder.loadTexts: tpProxyArpVlanId.setStatus('current')
if mibBuilder.loadTexts: tpProxyArpVlanId.setDescription('The vlan id of the proxy arp ip address')
tpProxyArpIpAddr = MibTableColumn((1, 3, 6, 1, 4, 1, 11863, 6, 37, 1, 1, 1, 2), IpAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: tpProxyArpIpAddr.setStatus('current')
if mibBuilder.loadTexts: tpProxyArpIpAddr.setDescription('Displays the proxy arp ip address.')
tpProxyArpIpMask = MibTableColumn((1, 3, 6, 1, 4, 1, 11863, 6, 37, 1, 1, 1, 3), IpAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: tpProxyArpIpMask.setStatus('current')
if mibBuilder.loadTexts: tpProxyArpIpMask.setDescription('Displays the proxy arp ip address mask')
tpProxyArpInterfaceName = MibTableColumn((1, 3, 6, 1, 4, 1, 11863, 6, 37, 1, 1, 1, 4), OctetString().subtype(subtypeSpec=ValueSizeConstraint(0, 20))).setMaxAccess("readonly")
if mibBuilder.loadTexts: tpProxyArpInterfaceName.setStatus('current')
if mibBuilder.loadTexts: tpProxyArpInterfaceName.setDescription('Displays the interface name.')
tpProxyArpEnable = MibTableColumn((1, 3, 6, 1, 4, 1, 11863, 6, 37, 1, 1, 1, 5), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1))).clone(namedValues=NamedValues(("disable", 0), ("enable", 1)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: tpProxyArpEnable.setStatus('current')
if mibBuilder.loadTexts: tpProxyArpEnable.setDescription('Select Enable/Disable Fast Leave feature for the IP address. 0. Disable 1. Enable')
mibBuilder.exportSymbols("TPLINK-PROXYARP-MIB", tplinkProxyArpMIBObjects=tplinkProxyArpMIBObjects, tplinkProxyArpNotifications=tplinkProxyArpNotifications, tpProxyArpVlanId=tpProxyArpVlanId, tpProxyArpEntry=tpProxyArpEntry, PYSNMP_MODULE_ID=tplinkProxyArpMIB, tplinkProxyArpMIB=tplinkProxyArpMIB, tpProxyArpConfig=tpProxyArpConfig, tpProxyArpIpAddr=tpProxyArpIpAddr, tpProxyArpTable=tpProxyArpTable, tpProxyArpInterfaceName=tpProxyArpInterfaceName, tpProxyArpEnable=tpProxyArpEnable, tpProxyArpIpMask=tpProxyArpIpMask)
