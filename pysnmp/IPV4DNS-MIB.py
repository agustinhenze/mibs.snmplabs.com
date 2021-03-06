#
# PySNMP MIB module IPV4DNS-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/IPV4DNS-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 19:45:33 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
apIpv4Dns, = mibBuilder.importSymbols("APENT-MIB", "apIpv4Dns")
ObjectIdentifier, Integer, OctetString = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "Integer", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ValueSizeConstraint, ConstraintsUnion, SingleValueConstraint, ValueRangeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ValueSizeConstraint", "ConstraintsUnion", "SingleValueConstraint", "ValueRangeConstraint")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
Gauge32, TimeTicks, NotificationType, Bits, ObjectIdentity, ModuleIdentity, Counter64, MibIdentifier, MibScalar, MibTable, MibTableRow, MibTableColumn, Unsigned32, Integer32, iso, Counter32, IpAddress = mibBuilder.importSymbols("SNMPv2-SMI", "Gauge32", "TimeTicks", "NotificationType", "Bits", "ObjectIdentity", "ModuleIdentity", "Counter64", "MibIdentifier", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Unsigned32", "Integer32", "iso", "Counter32", "IpAddress")
RowStatus, TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "RowStatus", "TextualConvention", "DisplayString")
apIpv4DnsMib = ModuleIdentity((1, 3, 6, 1, 4, 1, 2467, 1, 9, 7, 1))
if mibBuilder.loadTexts: apIpv4DnsMib.setLastUpdated('9801282000Z')
if mibBuilder.loadTexts: apIpv4DnsMib.setOrganization('ArrowPoint Communications Inc.')
apIpv4DnsDefaultSuffix = MibScalar((1, 3, 6, 1, 4, 1, 2467, 1, 9, 7, 2), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 64))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: apIpv4DnsDefaultSuffix.setStatus('current')
apIpv4DnsPrimary = MibScalar((1, 3, 6, 1, 4, 1, 2467, 1, 9, 7, 3), IpAddress()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: apIpv4DnsPrimary.setStatus('current')
apIpv4DnsTable = MibTable((1, 3, 6, 1, 4, 1, 2467, 1, 9, 7, 4), )
if mibBuilder.loadTexts: apIpv4DnsTable.setStatus('current')
apIpv4DnsEntry = MibTableRow((1, 3, 6, 1, 4, 1, 2467, 1, 9, 7, 4, 1), ).setIndexNames((0, "IPV4DNS-MIB", "apIpv4DnsSecondaryIP"))
if mibBuilder.loadTexts: apIpv4DnsEntry.setStatus('current')
apIpv4DnsSecondaryIP = MibTableColumn((1, 3, 6, 1, 4, 1, 2467, 1, 9, 7, 4, 1, 1), IpAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: apIpv4DnsSecondaryIP.setStatus('current')
apIpv4DnsStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 2467, 1, 9, 7, 4, 1, 2), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: apIpv4DnsStatus.setStatus('current')
mibBuilder.exportSymbols("IPV4DNS-MIB", apIpv4DnsDefaultSuffix=apIpv4DnsDefaultSuffix, apIpv4DnsTable=apIpv4DnsTable, apIpv4DnsMib=apIpv4DnsMib, apIpv4DnsPrimary=apIpv4DnsPrimary, apIpv4DnsEntry=apIpv4DnsEntry, apIpv4DnsSecondaryIP=apIpv4DnsSecondaryIP, PYSNMP_MODULE_ID=apIpv4DnsMib, apIpv4DnsStatus=apIpv4DnsStatus)
