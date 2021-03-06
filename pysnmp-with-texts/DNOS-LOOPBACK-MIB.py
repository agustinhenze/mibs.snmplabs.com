#
# PySNMP MIB module DNOS-LOOPBACK-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/DNOS-LOOPBACK-MIB
# Produced by pysmi-0.3.4 at Wed May  1 12:51:35 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
SingleValueConstraint, ConstraintsIntersection, ValueRangeConstraint, ValueSizeConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "SingleValueConstraint", "ConstraintsIntersection", "ValueRangeConstraint", "ValueSizeConstraint", "ConstraintsUnion")
dnOS, = mibBuilder.importSymbols("DELL-REF-MIB", "dnOS")
InetAddressIPv4, = mibBuilder.importSymbols("INET-ADDRESS-MIB", "InetAddressIPv4")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
Gauge32, Integer32, ObjectIdentity, Counter64, NotificationType, MibScalar, MibTable, MibTableRow, MibTableColumn, IpAddress, ModuleIdentity, Counter32, TimeTicks, Unsigned32, MibIdentifier, Bits, mib_2, iso = mibBuilder.importSymbols("SNMPv2-SMI", "Gauge32", "Integer32", "ObjectIdentity", "Counter64", "NotificationType", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "IpAddress", "ModuleIdentity", "Counter32", "TimeTicks", "Unsigned32", "MibIdentifier", "Bits", "mib-2", "iso")
DisplayString, RowStatus, TextualConvention, TruthValue, PhysAddress = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "RowStatus", "TextualConvention", "TruthValue", "PhysAddress")
fastPathLoopback = ModuleIdentity((1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 22))
fastPathLoopback.setRevisions(('2011-01-26 00:00', '2007-05-23 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: fastPathLoopback.setRevisionsDescriptions(('Postal address updated.', 'Dell branding related changes.',))
if mibBuilder.loadTexts: fastPathLoopback.setLastUpdated('201101260000Z')
if mibBuilder.loadTexts: fastPathLoopback.setOrganization('Dell, Inc.')
if mibBuilder.loadTexts: fastPathLoopback.setContactInfo('')
if mibBuilder.loadTexts: fastPathLoopback.setDescription('The Dell Networking Private MIB for Loopback')
agentLoopbackGroup = MibIdentifier((1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 22, 1))
agentLoopbackTable = MibTable((1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 22, 1, 1), )
if mibBuilder.loadTexts: agentLoopbackTable.setStatus('current')
if mibBuilder.loadTexts: agentLoopbackTable.setDescription('A summary table of the Loopback instances')
agentLoopbackEntry = MibTableRow((1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 22, 1, 1, 1), ).setIndexNames((0, "DNOS-LOOPBACK-MIB", "agentLoopbackID"))
if mibBuilder.loadTexts: agentLoopbackEntry.setStatus('current')
if mibBuilder.loadTexts: agentLoopbackEntry.setDescription('')
agentLoopbackID = MibTableColumn((1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 22, 1, 1, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 2147483647)))
if mibBuilder.loadTexts: agentLoopbackID.setStatus('current')
if mibBuilder.loadTexts: agentLoopbackID.setDescription('The Loopback ID is associated with Internal Interface number which will be generated when we create a loopback.')
agentLoopbackIfIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 22, 1, 1, 1, 2), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: agentLoopbackIfIndex.setStatus('current')
if mibBuilder.loadTexts: agentLoopbackIfIndex.setDescription('This is external interface associated with inetrnal interface of loopback. The Loopback ID is associated with Internal Interface number which will be generated when we create a loopback.')
agentLoopbackIPAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 22, 1, 1, 1, 3), InetAddressIPv4()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: agentLoopbackIPAddress.setStatus('current')
if mibBuilder.loadTexts: agentLoopbackIPAddress.setDescription('The IP Address configured for the respective loopback')
agentLoopbackIPSubnet = MibTableColumn((1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 22, 1, 1, 1, 4), InetAddressIPv4()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: agentLoopbackIPSubnet.setStatus('current')
if mibBuilder.loadTexts: agentLoopbackIPSubnet.setDescription('The Subnet mask configured for the respective loopback')
agentLoopbackStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 22, 1, 1, 1, 5), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: agentLoopbackStatus.setStatus('current')
if mibBuilder.loadTexts: agentLoopbackStatus.setDescription('Status of this instance. The rows can be added/deleted in the table by setting createAndGo/destroy respectively active(1) - this loopback instance is active createAndGo(4) - set to this value to create an instance destroy(6) - set to this value to delete an instance')
mibBuilder.exportSymbols("DNOS-LOOPBACK-MIB", agentLoopbackIPAddress=agentLoopbackIPAddress, agentLoopbackIfIndex=agentLoopbackIfIndex, agentLoopbackIPSubnet=agentLoopbackIPSubnet, PYSNMP_MODULE_ID=fastPathLoopback, agentLoopbackStatus=agentLoopbackStatus, agentLoopbackEntry=agentLoopbackEntry, agentLoopbackGroup=agentLoopbackGroup, fastPathLoopback=fastPathLoopback, agentLoopbackTable=agentLoopbackTable, agentLoopbackID=agentLoopbackID)
