#
# PySNMP MIB module TPLINK-ACL-RULE-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/TPLINK-ACL-RULE-MIB
# Produced by pysmi-0.3.4 at Wed May  1 15:24:11 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ValueRangeConstraint, ConstraintsIntersection, ConstraintsUnion, SingleValueConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ValueRangeConstraint", "ConstraintsIntersection", "ConstraintsUnion", "SingleValueConstraint")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
MibIdentifier, Unsigned32, ObjectIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, iso, NotificationType, ModuleIdentity, Gauge32, Integer32, Counter32, Bits, IpAddress, TimeTicks, Counter64 = mibBuilder.importSymbols("SNMPv2-SMI", "MibIdentifier", "Unsigned32", "ObjectIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "iso", "NotificationType", "ModuleIdentity", "Gauge32", "Integer32", "Counter32", "Bits", "IpAddress", "TimeTicks", "Counter64")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
tplinkAclMIBObjects, = mibBuilder.importSymbols("TPLINK-ACL-MIB", "tplinkAclMIBObjects")
tplinkMgmt, = mibBuilder.importSymbols("TPLINK-MIB", "tplinkMgmt")
TPRowStatus, = mibBuilder.importSymbols("TPLINK-TC-MIB", "TPRowStatus")
tpAclRuleConfigure = MibIdentifier((1, 3, 6, 1, 4, 1, 11863, 6, 26, 1, 1))
tpMacRuleTable = MibTable((1, 3, 6, 1, 4, 1, 11863, 6, 26, 1, 1, 1), )
if mibBuilder.loadTexts: tpMacRuleTable.setStatus('current')
if mibBuilder.loadTexts: tpMacRuleTable.setDescription('A list of L2 MAC ACL rule entries. Here you can add MAC ACL rules for further ACL configuration.')
tpMacRuleEntry = MibTableRow((1, 3, 6, 1, 4, 1, 11863, 6, 26, 1, 1, 1, 1), ).setIndexNames((0, "TPLINK-ACL-RULE-MIB", "tpMacAclId"), (0, "TPLINK-ACL-RULE-MIB", "tpMacRuleId"))
if mibBuilder.loadTexts: tpMacRuleEntry.setStatus('current')
if mibBuilder.loadTexts: tpMacRuleEntry.setDescription('An entry contains of the information of MAC ACL.')
tpMacAclId = MibTableColumn((1, 3, 6, 1, 4, 1, 11863, 6, 26, 1, 1, 1, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: tpMacAclId.setStatus('current')
if mibBuilder.loadTexts: tpMacAclId.setDescription('MAC ACL ID.')
tpMacRuleId = MibTableColumn((1, 3, 6, 1, 4, 1, 11863, 6, 26, 1, 1, 1, 1, 2), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: tpMacRuleId.setStatus('current')
if mibBuilder.loadTexts: tpMacRuleId.setDescription('MAC ACL rule ID.')
tpMacSecOperation = MibTableColumn((1, 3, 6, 1, 4, 1, 11863, 6, 26, 1, 1, 1, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1))).clone(namedValues=NamedValues(("permit", 0), ("deny", 1)))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: tpMacSecOperation.setStatus('current')
if mibBuilder.loadTexts: tpMacSecOperation.setDescription('MAC ACL Security Operation.')
tpMacSmacAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 11863, 6, 26, 1, 1, 1, 1, 4), OctetString()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: tpMacSmacAddress.setStatus('current')
if mibBuilder.loadTexts: tpMacSmacAddress.setDescription('Source MAC address, string length setting to zero means that the source MAC address is disabled.')
tpMacSmacMask = MibTableColumn((1, 3, 6, 1, 4, 1, 11863, 6, 26, 1, 1, 1, 1, 5), OctetString()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: tpMacSmacMask.setStatus('current')
if mibBuilder.loadTexts: tpMacSmacMask.setDescription('Source Mac Mask, string length setting to zero means that every bit of the mask is 1.')
tpMacDmacAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 11863, 6, 26, 1, 1, 1, 1, 6), OctetString()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: tpMacDmacAddress.setStatus('current')
if mibBuilder.loadTexts: tpMacDmacAddress.setDescription('Destination MAC address, string length setting to zero means that the destination MAC address is disabled.')
tpMacDmacMask = MibTableColumn((1, 3, 6, 1, 4, 1, 11863, 6, 26, 1, 1, 1, 1, 7), OctetString()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: tpMacDmacMask.setStatus('current')
if mibBuilder.loadTexts: tpMacDmacMask.setDescription('Destination Mac Mask, string length setting to zero means that every bit of the mask is 1.')
tpMacVlanId = MibTableColumn((1, 3, 6, 1, 4, 1, 11863, 6, 26, 1, 1, 1, 1, 8), Integer32()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: tpMacVlanId.setStatus('current')
if mibBuilder.loadTexts: tpMacVlanId.setDescription("VLAN ID, 0-4094, value '0' means that the vid field is disabled.")
tpMacEtherType = MibTableColumn((1, 3, 6, 1, 4, 1, 11863, 6, 26, 1, 1, 1, 1, 9), Integer32()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: tpMacEtherType.setStatus('current')
if mibBuilder.loadTexts: tpMacEtherType.setDescription("Ethernet protocol type, 0x0-0x10000. Value '65536' or '0x10000' means that the EtherType field is disabled.")
tpMacPri = MibTableColumn((1, 3, 6, 1, 4, 1, 11863, 6, 26, 1, 1, 1, 1, 10), Integer32()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: tpMacPri.setStatus('current')
if mibBuilder.loadTexts: tpMacPri.setDescription("802.1P priority, 0-8, value '8' means that the priority field is disabled.")
tpMacTimeSegment = MibTableColumn((1, 3, 6, 1, 4, 1, 11863, 6, 26, 1, 1, 1, 1, 11), OctetString()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: tpMacTimeSegment.setStatus('current')
if mibBuilder.loadTexts: tpMacTimeSegment.setDescription('MAC ACL time segment name(max length: 16), the time segment name must be configured previously and string length setting to zero means that this field is disabled.')
tpMacRuleStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 11863, 6, 26, 1, 1, 1, 1, 12), TPRowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: tpMacRuleStatus.setStatus('current')
if mibBuilder.loadTexts: tpMacRuleStatus.setDescription('the following two values are states: these values may be read or written active(1), notInService(2), the following value is a state: this value may be read, but not written notReady(3), the following three values are actions: these values may be written, but are never read createAndGo(4), createAndWait(5), destroy(6)')
tpStdipRuleTable = MibTable((1, 3, 6, 1, 4, 1, 11863, 6, 26, 1, 1, 2), )
if mibBuilder.loadTexts: tpStdipRuleTable.setStatus('current')
if mibBuilder.loadTexts: tpStdipRuleTable.setDescription('A list of standard IP rule entries. Here you can add standard IP ACL rules for further ACL configuration.')
tpStdipRuleEntry = MibTableRow((1, 3, 6, 1, 4, 1, 11863, 6, 26, 1, 1, 2, 1), ).setIndexNames((0, "TPLINK-ACL-RULE-MIB", "tpStdipAclId"), (0, "TPLINK-ACL-RULE-MIB", "tpStdipRuleId"))
if mibBuilder.loadTexts: tpStdipRuleEntry.setStatus('current')
if mibBuilder.loadTexts: tpStdipRuleEntry.setDescription('An entry contains of the information of STDIP ACL.')
tpStdipAclId = MibTableColumn((1, 3, 6, 1, 4, 1, 11863, 6, 26, 1, 1, 2, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: tpStdipAclId.setStatus('current')
if mibBuilder.loadTexts: tpStdipAclId.setDescription('Standard IP ACL ID.')
tpStdipRuleId = MibTableColumn((1, 3, 6, 1, 4, 1, 11863, 6, 26, 1, 1, 2, 1, 2), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: tpStdipRuleId.setStatus('current')
if mibBuilder.loadTexts: tpStdipRuleId.setDescription('Standard IP ACL rule ID.')
tpStdipSecOperation = MibTableColumn((1, 3, 6, 1, 4, 1, 11863, 6, 26, 1, 1, 2, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1))).clone(namedValues=NamedValues(("permit", 0), ("deny", 1)))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: tpStdipSecOperation.setStatus('current')
if mibBuilder.loadTexts: tpStdipSecOperation.setDescription('Standard IP ACL Security Operation.')
tpStdipSipAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 11863, 6, 26, 1, 1, 2, 1, 4), IpAddress()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: tpStdipSipAddress.setStatus('current')
if mibBuilder.loadTexts: tpStdipSipAddress.setDescription("Source IP address, value '0.0.0.0' means that the source IP address is disabled.")
tpStdipSipMask = MibTableColumn((1, 3, 6, 1, 4, 1, 11863, 6, 26, 1, 1, 2, 1, 5), IpAddress()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: tpStdipSipMask.setStatus('current')
if mibBuilder.loadTexts: tpStdipSipMask.setDescription("Source IP Mask, value '0.0.0.0' or zero length means that the mask is 255.255.255.255.")
tpStdipDipAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 11863, 6, 26, 1, 1, 2, 1, 6), IpAddress()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: tpStdipDipAddress.setStatus('current')
if mibBuilder.loadTexts: tpStdipDipAddress.setDescription("Destination IP address, value '0.0.0.0' means that the destination IP address is disabled.")
tpStdipDipMask = MibTableColumn((1, 3, 6, 1, 4, 1, 11863, 6, 26, 1, 1, 2, 1, 7), IpAddress()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: tpStdipDipMask.setStatus('current')
if mibBuilder.loadTexts: tpStdipDipMask.setDescription("Destination IP Mask, value '0.0.0.0' or zero length means that the mask is 255.255.255.255.")
tpStdipTimeSegment = MibTableColumn((1, 3, 6, 1, 4, 1, 11863, 6, 26, 1, 1, 2, 1, 8), OctetString()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: tpStdipTimeSegment.setStatus('current')
if mibBuilder.loadTexts: tpStdipTimeSegment.setDescription('STDIP ACL time segment name(max length: 16), the time segment name must be configured previously and string length setting to zero means that this field is disabled.')
tpStdipRuleStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 11863, 6, 26, 1, 1, 2, 1, 9), TPRowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: tpStdipRuleStatus.setStatus('current')
if mibBuilder.loadTexts: tpStdipRuleStatus.setDescription('the following two values are states: these values may be read or written active(1), notInService(2), the following value is a state: this value may be read, but not written notReady(3), the following three values are actions: these values may be written, but are never read createAndGo(4), createAndWait(5), destroy(6)')
tpExtipRuleTable = MibTable((1, 3, 6, 1, 4, 1, 11863, 6, 26, 1, 1, 3), )
if mibBuilder.loadTexts: tpExtipRuleTable.setStatus('current')
if mibBuilder.loadTexts: tpExtipRuleTable.setDescription('A list of extended IP rule entries. Here you can add extended IP ACL rules for further ACL configuration.')
tpExtipRuleEntry = MibTableRow((1, 3, 6, 1, 4, 1, 11863, 6, 26, 1, 1, 3, 1), ).setIndexNames((0, "TPLINK-ACL-RULE-MIB", "tpExtipAclId"), (0, "TPLINK-ACL-RULE-MIB", "tpExtipRuleId"))
if mibBuilder.loadTexts: tpExtipRuleEntry.setStatus('current')
if mibBuilder.loadTexts: tpExtipRuleEntry.setDescription('An entry contains of the information of EXTIP ACL.')
tpExtipAclId = MibTableColumn((1, 3, 6, 1, 4, 1, 11863, 6, 26, 1, 1, 3, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: tpExtipAclId.setStatus('current')
if mibBuilder.loadTexts: tpExtipAclId.setDescription('Extended IP ACL ID.')
tpExtipRuleId = MibTableColumn((1, 3, 6, 1, 4, 1, 11863, 6, 26, 1, 1, 3, 1, 2), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: tpExtipRuleId.setStatus('current')
if mibBuilder.loadTexts: tpExtipRuleId.setDescription('Extended IP ACL rule ID.')
tpExtipSecOperation = MibTableColumn((1, 3, 6, 1, 4, 1, 11863, 6, 26, 1, 1, 3, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1))).clone(namedValues=NamedValues(("permit", 0), ("deny", 1)))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: tpExtipSecOperation.setStatus('current')
if mibBuilder.loadTexts: tpExtipSecOperation.setDescription('Extended IP ACL Security Operation.')
tpExtipFragment = MibTableColumn((1, 3, 6, 1, 4, 1, 11863, 6, 26, 1, 1, 3, 1, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1))).clone(namedValues=NamedValues(("disable", 0), ("enable", 1)))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: tpExtipFragment.setStatus('current')
if mibBuilder.loadTexts: tpExtipFragment.setDescription('Extended IP fragment, conflicts with all the L4 feature.')
tpExtipSipAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 11863, 6, 26, 1, 1, 3, 1, 5), IpAddress()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: tpExtipSipAddress.setStatus('current')
if mibBuilder.loadTexts: tpExtipSipAddress.setDescription("Source IP address, value '0.0.0.0' means that the source IP address is disabled.")
tpExtipSipMask = MibTableColumn((1, 3, 6, 1, 4, 1, 11863, 6, 26, 1, 1, 3, 1, 6), IpAddress()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: tpExtipSipMask.setStatus('current')
if mibBuilder.loadTexts: tpExtipSipMask.setDescription("Source IP Mask, value '0.0.0.0' or zero length means that the mask is 255.255.255.255.")
tpExtipDipAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 11863, 6, 26, 1, 1, 3, 1, 7), IpAddress()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: tpExtipDipAddress.setStatus('current')
if mibBuilder.loadTexts: tpExtipDipAddress.setDescription("Destination IP address, value '0.0.0.0' means that the Destination IP address is disabled.")
tpExtipDipMask = MibTableColumn((1, 3, 6, 1, 4, 1, 11863, 6, 26, 1, 1, 3, 1, 8), IpAddress()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: tpExtipDipMask.setStatus('current')
if mibBuilder.loadTexts: tpExtipDipMask.setDescription("Destination IP Mask, value '0.0.0.0' or zero length means that the mask is 255.255.255.255.")
tpExtipProtocol = MibTableColumn((1, 3, 6, 1, 4, 1, 11863, 6, 26, 1, 1, 3, 1, 9), Integer32()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: tpExtipProtocol.setStatus('current')
if mibBuilder.loadTexts: tpExtipProtocol.setDescription("L4 protocol type, 0-255, value '0' means this field is disabled. This field conflicts with the TCP Flags or the source/destination port numbers when it is not the value '6'(TCP), or '17'(UDP).")
tpExtipTcpFlag = MibTableColumn((1, 3, 6, 1, 4, 1, 11863, 6, 26, 1, 1, 3, 1, 10), Integer32()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: tpExtipTcpFlag.setStatus('current')
if mibBuilder.loadTexts: tpExtipTcpFlag.setDescription("Extended IP TCP flag, this field is described as a bit-map structure: There are 12 bits of this field, the higher 6 bits show us whether these TCP flags are enabled(1) or disabled(0). The lower 6 bits show us the 6 kind of TCP flags' value (0-1). From the highest bit(bit11) to the lowest bit(0), each bit stands for a TCP flag: bit11 & bit5 -- URG flag bit10 & bit4 -- ACK flag bit9 & bit3 -- PSH flag bit8 & bit2 -- RST flag bit7 & bit1 -- SYN flag bit6 & bit0 -- FIN flag")
tpExtipSourcePort = MibTableColumn((1, 3, 6, 1, 4, 1, 11863, 6, 26, 1, 1, 3, 1, 11), Integer32()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: tpExtipSourcePort.setStatus('current')
if mibBuilder.loadTexts: tpExtipSourcePort.setDescription("Extended IP TCP/UDP source port, 0-65536, value '65536' means that this field is disabled.")
tpExtipDestPort = MibTableColumn((1, 3, 6, 1, 4, 1, 11863, 6, 26, 1, 1, 3, 1, 12), Integer32()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: tpExtipDestPort.setStatus('current')
if mibBuilder.loadTexts: tpExtipDestPort.setDescription("Extended IP TCP/UDP destination port, 0-65536, value '65536' means that this field is disabled.")
tpExtipDscp = MibTableColumn((1, 3, 6, 1, 4, 1, 11863, 6, 26, 1, 1, 3, 1, 13), Integer32()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: tpExtipDscp.setStatus('current')
if mibBuilder.loadTexts: tpExtipDscp.setDescription("Extended IP DSCP, 0-64, value '64' means this field is disabled. conflicts with the Tos and Pre.")
tpExtipTos = MibTableColumn((1, 3, 6, 1, 4, 1, 11863, 6, 26, 1, 1, 3, 1, 14), Integer32()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: tpExtipTos.setStatus('current')
if mibBuilder.loadTexts: tpExtipTos.setDescription("Extended IP type of service(ToS), 0-16, value '16' means this field is disabled.")
tpExtipPre = MibTableColumn((1, 3, 6, 1, 4, 1, 11863, 6, 26, 1, 1, 3, 1, 15), Integer32()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: tpExtipPre.setStatus('current')
if mibBuilder.loadTexts: tpExtipPre.setDescription("Extended IP pre, 0-8, value '8' means this field is disabled.")
tpExtipTimeSegment = MibTableColumn((1, 3, 6, 1, 4, 1, 11863, 6, 26, 1, 1, 3, 1, 16), OctetString()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: tpExtipTimeSegment.setStatus('current')
if mibBuilder.loadTexts: tpExtipTimeSegment.setDescription('EXTIP ACL time segment name(max length: 16), the time segment name must be configured previously and string length setting to zero means that this field is disabled.')
tpExtipRuleStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 11863, 6, 26, 1, 1, 3, 1, 17), TPRowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: tpExtipRuleStatus.setStatus('current')
if mibBuilder.loadTexts: tpExtipRuleStatus.setDescription('the following two values are states: these values may be read or written active(1), notInService(2), the following value is a state: this value may be read, but not written notReady(3), the following three values are actions: these values may be written, but are never read createAndGo(4), createAndWait(5), destroy(6)')
tpCombRuleTable = MibTable((1, 3, 6, 1, 4, 1, 11863, 6, 26, 1, 1, 4), )
if mibBuilder.loadTexts: tpCombRuleTable.setStatus('current')
if mibBuilder.loadTexts: tpCombRuleTable.setDescription('A list of combined MAC+IP rule entries. Here you can add combined ACL rules for further ACL configuration.')
tpCombRuleEntry = MibTableRow((1, 3, 6, 1, 4, 1, 11863, 6, 26, 1, 1, 4, 1), ).setIndexNames((0, "TPLINK-ACL-RULE-MIB", "tpCombAclId"), (0, "TPLINK-ACL-RULE-MIB", "tpCombRuleId"))
if mibBuilder.loadTexts: tpCombRuleEntry.setStatus('current')
if mibBuilder.loadTexts: tpCombRuleEntry.setDescription('An entry contains of the information of Combined ACL.')
tpCombAclId = MibTableColumn((1, 3, 6, 1, 4, 1, 11863, 6, 26, 1, 1, 4, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: tpCombAclId.setStatus('current')
if mibBuilder.loadTexts: tpCombAclId.setDescription('Combined MAC+IP ACL ID.')
tpCombRuleId = MibTableColumn((1, 3, 6, 1, 4, 1, 11863, 6, 26, 1, 1, 4, 1, 2), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: tpCombRuleId.setStatus('current')
if mibBuilder.loadTexts: tpCombRuleId.setDescription('Combined ACL rule ID.')
tpCombSecOperation = MibTableColumn((1, 3, 6, 1, 4, 1, 11863, 6, 26, 1, 1, 4, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1))).clone(namedValues=NamedValues(("permit", 0), ("deny", 1)))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: tpCombSecOperation.setStatus('current')
if mibBuilder.loadTexts: tpCombSecOperation.setDescription('Combined ACL Security Operation.')
tpCombSmacAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 11863, 6, 26, 1, 1, 4, 1, 4), OctetString()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: tpCombSmacAddress.setStatus('current')
if mibBuilder.loadTexts: tpCombSmacAddress.setDescription('Source MAC address, string length setting to zero means that the source MAC address is disabled.')
tpCombSmacMask = MibTableColumn((1, 3, 6, 1, 4, 1, 11863, 6, 26, 1, 1, 4, 1, 5), OctetString()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: tpCombSmacMask.setStatus('current')
if mibBuilder.loadTexts: tpCombSmacMask.setDescription('Source MAC Mask, string length setting to zero means that every bit of the mask is 1.')
tpCombDmacAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 11863, 6, 26, 1, 1, 4, 1, 6), OctetString()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: tpCombDmacAddress.setStatus('current')
if mibBuilder.loadTexts: tpCombDmacAddress.setDescription('Destination MAC address, string length setting to zero means that the destination MAC address is disabled.')
tpCombDmacMask = MibTableColumn((1, 3, 6, 1, 4, 1, 11863, 6, 26, 1, 1, 4, 1, 7), OctetString()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: tpCombDmacMask.setStatus('current')
if mibBuilder.loadTexts: tpCombDmacMask.setDescription('Destination MAC Mask, string length setting to zero means that every bit of the mask is 1.')
tpCombVlanId = MibTableColumn((1, 3, 6, 1, 4, 1, 11863, 6, 26, 1, 1, 4, 1, 8), Integer32()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: tpCombVlanId.setStatus('current')
if mibBuilder.loadTexts: tpCombVlanId.setDescription("VLAN ID, 0-4094, value '0' means that the vid field is disabled.")
tpCombEtherType = MibTableColumn((1, 3, 6, 1, 4, 1, 11863, 6, 26, 1, 1, 4, 1, 9), Integer32()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: tpCombEtherType.setStatus('current')
if mibBuilder.loadTexts: tpCombEtherType.setDescription("Ethernet protocol type, 0x0-0x10000. Value '65536' or '0x10000' means that the EtherType field is disabled.")
tpCombPri = MibTableColumn((1, 3, 6, 1, 4, 1, 11863, 6, 26, 1, 1, 4, 1, 10), Integer32()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: tpCombPri.setStatus('current')
if mibBuilder.loadTexts: tpCombPri.setDescription("802.1P priority, 0-8, value '8' means that the priority field is disabled.")
tpCombSipAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 11863, 6, 26, 1, 1, 4, 1, 11), IpAddress()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: tpCombSipAddress.setStatus('current')
if mibBuilder.loadTexts: tpCombSipAddress.setDescription("Source IP address, value '0.0.0.0' means that the source IP address is disabled.")
tpCombSipMask = MibTableColumn((1, 3, 6, 1, 4, 1, 11863, 6, 26, 1, 1, 4, 1, 12), IpAddress()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: tpCombSipMask.setStatus('current')
if mibBuilder.loadTexts: tpCombSipMask.setDescription("Source IP mask, value '0.0.0.0' or zero length means that the mask is 255.255.255.255.")
tpCombDipAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 11863, 6, 26, 1, 1, 4, 1, 13), IpAddress()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: tpCombDipAddress.setStatus('current')
if mibBuilder.loadTexts: tpCombDipAddress.setDescription("Destination IP address, value '0.0.0.0' means that the destination IP address is disabled.")
tpCombDipMask = MibTableColumn((1, 3, 6, 1, 4, 1, 11863, 6, 26, 1, 1, 4, 1, 14), IpAddress()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: tpCombDipMask.setStatus('current')
if mibBuilder.loadTexts: tpCombDipMask.setDescription("Destination IP mask, value '0.0.0.0' or zero length means that the mask is 255.255.255.255.")
tpCombTimeSegment = MibTableColumn((1, 3, 6, 1, 4, 1, 11863, 6, 26, 1, 1, 4, 1, 15), OctetString()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: tpCombTimeSegment.setStatus('current')
if mibBuilder.loadTexts: tpCombTimeSegment.setDescription('Combined ACL time segment name(max length: 16), the time segment name must be configured previously and string length setting to zero means that this field is disabled.')
tpCombRuleStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 11863, 6, 26, 1, 1, 4, 1, 16), TPRowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: tpCombRuleStatus.setStatus('current')
if mibBuilder.loadTexts: tpCombRuleStatus.setDescription('the following two values are states: these values may be read or written active(1), notInService(2), the following value is a state: this value may be read, but not written notReady(3), the following three values are actions: these values may be written, but are never read createAndGo(4), createAndWait(5), destroy(6)')
tpIPv6RuleTable = MibTable((1, 3, 6, 1, 4, 1, 11863, 6, 26, 1, 1, 5), )
if mibBuilder.loadTexts: tpIPv6RuleTable.setStatus('current')
if mibBuilder.loadTexts: tpIPv6RuleTable.setDescription('A list of IPv6 rule entries. Here you can add IPv6 ACL rules for further ACL configuration.')
tpIPv6RuleEntry = MibTableRow((1, 3, 6, 1, 4, 1, 11863, 6, 26, 1, 1, 5, 1), ).setIndexNames((0, "TPLINK-ACL-RULE-MIB", "tpIPv6AclId"), (0, "TPLINK-ACL-RULE-MIB", "tpIPv6RuleId"))
if mibBuilder.loadTexts: tpIPv6RuleEntry.setStatus('current')
if mibBuilder.loadTexts: tpIPv6RuleEntry.setDescription('An entry contains of the information of IPv6 ACL.')
tpIPv6AclId = MibTableColumn((1, 3, 6, 1, 4, 1, 11863, 6, 26, 1, 1, 5, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: tpIPv6AclId.setStatus('current')
if mibBuilder.loadTexts: tpIPv6AclId.setDescription('IPv6 ACL ID.')
tpIPv6RuleId = MibTableColumn((1, 3, 6, 1, 4, 1, 11863, 6, 26, 1, 1, 5, 1, 2), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: tpIPv6RuleId.setStatus('current')
if mibBuilder.loadTexts: tpIPv6RuleId.setDescription('IPv6 ACL rule ID.')
tpIPv6SecOperation = MibTableColumn((1, 3, 6, 1, 4, 1, 11863, 6, 26, 1, 1, 5, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1))).clone(namedValues=NamedValues(("permit", 0), ("deny", 1)))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: tpIPv6SecOperation.setStatus('current')
if mibBuilder.loadTexts: tpIPv6SecOperation.setDescription('IPv6 ACL Security Operation.')
tpIPv6TrafficClass = MibTableColumn((1, 3, 6, 1, 4, 1, 11863, 6, 26, 1, 1, 5, 1, 4), Integer32()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: tpIPv6TrafficClass.setStatus('current')
if mibBuilder.loadTexts: tpIPv6TrafficClass.setDescription("Traffic Class DSCP, 0-64, value '64' means that this field is disabled.")
tpIPv6FlowLabel = MibTableColumn((1, 3, 6, 1, 4, 1, 11863, 6, 26, 1, 1, 5, 1, 5), Integer32()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: tpIPv6FlowLabel.setStatus('current')
if mibBuilder.loadTexts: tpIPv6FlowLabel.setDescription("IPv6 Flow Label, 0x0-0x100000, value '0x100000' or '1048576' means that this field is disabled.")
tpIPv6SipAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 11863, 6, 26, 1, 1, 5, 1, 6), OctetString()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: tpIPv6SipAddress.setStatus('current')
if mibBuilder.loadTexts: tpIPv6SipAddress.setDescription('IPv6 source IP address, only upper 64 bits supported; the all-zero address means that the source IPv6 address is disabled.')
tpIPv6SipMask = MibTableColumn((1, 3, 6, 1, 4, 1, 11863, 6, 26, 1, 1, 5, 1, 7), OctetString()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: tpIPv6SipMask.setStatus('current')
if mibBuilder.loadTexts: tpIPv6SipMask.setDescription('IPv6 source IP mask, 64 bits, format: ffff:ffff:ffff:ffff; zero length means that every bit of the mask is 1.')
tpIPv6DipAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 11863, 6, 26, 1, 1, 5, 1, 8), OctetString()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: tpIPv6DipAddress.setStatus('current')
if mibBuilder.loadTexts: tpIPv6DipAddress.setDescription('IPv6 destination IP address, only upper 64 bits supported; the all-zero address means that the destination IPv6 address is disabled.')
tpIPv6DipMask = MibTableColumn((1, 3, 6, 1, 4, 1, 11863, 6, 26, 1, 1, 5, 1, 9), OctetString()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: tpIPv6DipMask.setStatus('current')
if mibBuilder.loadTexts: tpIPv6DipMask.setDescription('IPv6 destination IP mask, 64 bits, format: ffff:ffff:ffff:ffff; zero length means that every bit of the mask is 1.')
tpIPv6SourcePort = MibTableColumn((1, 3, 6, 1, 4, 1, 11863, 6, 26, 1, 1, 5, 1, 10), Integer32()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: tpIPv6SourcePort.setStatus('current')
if mibBuilder.loadTexts: tpIPv6SourcePort.setDescription("IPv6 L4 source port, 0-65536, value '65536' means that this field is disabled.")
tpIPv6DestPort = MibTableColumn((1, 3, 6, 1, 4, 1, 11863, 6, 26, 1, 1, 5, 1, 11), Integer32()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: tpIPv6DestPort.setStatus('current')
if mibBuilder.loadTexts: tpIPv6DestPort.setDescription("IPv6 L4 destination port, 0-65536, value '65536' means that this field is disabled.")
tpIPv6TimeSegment = MibTableColumn((1, 3, 6, 1, 4, 1, 11863, 6, 26, 1, 1, 5, 1, 12), OctetString()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: tpIPv6TimeSegment.setStatus('current')
if mibBuilder.loadTexts: tpIPv6TimeSegment.setDescription('IPv6 ACL time segment name(max length: 16), the time segment name must be configured previously and string length setting to zero means that this field is disabled.')
tpIPv6RuleStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 11863, 6, 26, 1, 1, 5, 1, 13), TPRowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: tpIPv6RuleStatus.setStatus('current')
if mibBuilder.loadTexts: tpIPv6RuleStatus.setDescription('the following two values are states: these values may be read or written active(1), notInService(2), the following value is a state: this value may be read, but not written notReady(3), the following three values are actions: these values may be written, but are never read createAndGo(4), createAndWait(5), destroy(6)')
mibBuilder.exportSymbols("TPLINK-ACL-RULE-MIB", tpIPv6DipAddress=tpIPv6DipAddress, tpMacRuleStatus=tpMacRuleStatus, tpExtipRuleEntry=tpExtipRuleEntry, tpExtipDscp=tpExtipDscp, tpExtipRuleId=tpExtipRuleId, tpExtipProtocol=tpExtipProtocol, tpExtipTcpFlag=tpExtipTcpFlag, tpIPv6TrafficClass=tpIPv6TrafficClass, tpStdipRuleStatus=tpStdipRuleStatus, tpExtipTimeSegment=tpExtipTimeSegment, tpIPv6TimeSegment=tpIPv6TimeSegment, tpMacVlanId=tpMacVlanId, tpMacRuleEntry=tpMacRuleEntry, tpIPv6RuleEntry=tpIPv6RuleEntry, tpExtipSipMask=tpExtipSipMask, tpAclRuleConfigure=tpAclRuleConfigure, tpStdipSipAddress=tpStdipSipAddress, tpStdipDipAddress=tpStdipDipAddress, tpIPv6AclId=tpIPv6AclId, tpStdipRuleEntry=tpStdipRuleEntry, tpIPv6RuleId=tpIPv6RuleId, tpCombAclId=tpCombAclId, tpExtipRuleTable=tpExtipRuleTable, tpIPv6DipMask=tpIPv6DipMask, tpStdipDipMask=tpStdipDipMask, tpCombDipAddress=tpCombDipAddress, tpMacDmacAddress=tpMacDmacAddress, tpStdipRuleTable=tpStdipRuleTable, tpCombRuleEntry=tpCombRuleEntry, tpMacDmacMask=tpMacDmacMask, tpIPv6DestPort=tpIPv6DestPort, tpCombRuleStatus=tpCombRuleStatus, tpExtipPre=tpExtipPre, tpMacTimeSegment=tpMacTimeSegment, tpMacRuleId=tpMacRuleId, tpCombPri=tpCombPri, tpCombDipMask=tpCombDipMask, tpMacSmacAddress=tpMacSmacAddress, tpIPv6RuleStatus=tpIPv6RuleStatus, tpExtipSecOperation=tpExtipSecOperation, tpMacPri=tpMacPri, tpCombRuleTable=tpCombRuleTable, tpExtipDipMask=tpExtipDipMask, tpMacSecOperation=tpMacSecOperation, tpExtipDestPort=tpExtipDestPort, tpIPv6SipAddress=tpIPv6SipAddress, tpIPv6RuleTable=tpIPv6RuleTable, tpIPv6FlowLabel=tpIPv6FlowLabel, tpExtipRuleStatus=tpExtipRuleStatus, tpCombEtherType=tpCombEtherType, tpExtipDipAddress=tpExtipDipAddress, tpIPv6SecOperation=tpIPv6SecOperation, tpMacRuleTable=tpMacRuleTable, tpCombSipMask=tpCombSipMask, tpMacSmacMask=tpMacSmacMask, tpStdipSipMask=tpStdipSipMask, tpCombDmacAddress=tpCombDmacAddress, tpStdipAclId=tpStdipAclId, tpIPv6SipMask=tpIPv6SipMask, tpStdipRuleId=tpStdipRuleId, tpExtipSourcePort=tpExtipSourcePort, tpExtipSipAddress=tpExtipSipAddress, tpCombVlanId=tpCombVlanId, tpIPv6SourcePort=tpIPv6SourcePort, tpCombSmacAddress=tpCombSmacAddress, tpMacAclId=tpMacAclId, tpExtipTos=tpExtipTos, tpStdipSecOperation=tpStdipSecOperation, tpCombSipAddress=tpCombSipAddress, tpCombSecOperation=tpCombSecOperation, tpCombRuleId=tpCombRuleId, tpStdipTimeSegment=tpStdipTimeSegment, tpExtipFragment=tpExtipFragment, tpCombTimeSegment=tpCombTimeSegment, tpCombDmacMask=tpCombDmacMask, tpMacEtherType=tpMacEtherType, tpCombSmacMask=tpCombSmacMask, tpExtipAclId=tpExtipAclId)
