#
# PySNMP MIB module HUAWEI-WLAN-QOS-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/HUAWEI-WLAN-QOS-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 19:38:10 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
OctetString, ObjectIdentifier, Integer = mibBuilder.importSymbols("ASN1", "OctetString", "ObjectIdentifier", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, SingleValueConstraint, ValueSizeConstraint, ConstraintsUnion, ValueRangeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "SingleValueConstraint", "ValueSizeConstraint", "ConstraintsUnion", "ValueRangeConstraint")
hwWlan, = mibBuilder.importSymbols("HUAWEI-WLAN-MIB", "hwWlan")
ObjectGroup, ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ObjectGroup", "ModuleCompliance", "NotificationGroup")
Bits, IpAddress, NotificationType, ModuleIdentity, Counter64, ObjectIdentity, MibIdentifier, Unsigned32, iso, MibScalar, MibTable, MibTableRow, MibTableColumn, Integer32, TimeTicks, Counter32, Gauge32 = mibBuilder.importSymbols("SNMPv2-SMI", "Bits", "IpAddress", "NotificationType", "ModuleIdentity", "Counter64", "ObjectIdentity", "MibIdentifier", "Unsigned32", "iso", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Integer32", "TimeTicks", "Counter32", "Gauge32")
TextualConvention, DisplayString, RowStatus = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString", "RowStatus")
hwWlanQosManagement = ModuleIdentity((1, 3, 6, 1, 4, 1, 2011, 6, 139, 5))
hwWlanQosManagement.setRevisions(('2010-10-12 10:00', '2010-06-01 10:00',))
if mibBuilder.loadTexts: hwWlanQosManagement.setLastUpdated('201011100000Z')
if mibBuilder.loadTexts: hwWlanQosManagement.setOrganization('Huawei Technologies Co.,Ltd.')
hwWlanWmmProfileTable = MibTable((1, 3, 6, 1, 4, 1, 2011, 6, 139, 5, 1), )
if mibBuilder.loadTexts: hwWlanWmmProfileTable.setStatus('current')
hwWlanWmmProfileEntry = MibTableRow((1, 3, 6, 1, 4, 1, 2011, 6, 139, 5, 1, 1), ).setIndexNames((0, "HUAWEI-WLAN-QOS-MIB", "hwWlanWmmProfileName"))
if mibBuilder.loadTexts: hwWlanWmmProfileEntry.setStatus('current')
hwWlanWmmProfileName = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 6, 139, 5, 1, 1, 1), OctetString().subtype(subtypeSpec=ValueSizeConstraint(1, 31)))
if mibBuilder.loadTexts: hwWlanWmmProfileName.setStatus('current')
hwWlanWmmSwitch = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 6, 139, 5, 1, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enable", 1), ("disable", 2))).clone(1)).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hwWlanWmmSwitch.setStatus('current')
hwWlanWmmMandatorySwitch = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 6, 139, 5, 1, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enable", 1), ("disable", 2))).clone(2)).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hwWlanWmmMandatorySwitch.setStatus('current')
hwWlanWmmProfileRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 6, 139, 5, 1, 1, 4), RowStatus()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hwWlanWmmProfileRowStatus.setStatus('current')
hwQAPEDCAVoiceECWmax = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 6, 139, 5, 1, 1, 5), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 15)).clone(3)).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hwQAPEDCAVoiceECWmax.setStatus('current')
hwQAPEDCAVoiceECWmin = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 6, 139, 5, 1, 1, 6), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 15)).clone(2)).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hwQAPEDCAVoiceECWmin.setStatus('current')
hwQAPEDCAVoiceAIFSN = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 6, 139, 5, 1, 1, 7), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 15)).clone(1)).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hwQAPEDCAVoiceAIFSN.setStatus('current')
hwQAPEDCAVoiceTXOPLimit = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 6, 139, 5, 1, 1, 8), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 65535)).clone(47)).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hwQAPEDCAVoiceTXOPLimit.setStatus('current')
hwQAPEDCAVoiceACKPolicy = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 6, 139, 5, 1, 1, 9), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("normal", 1), ("noack", 2))).clone(1)).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hwQAPEDCAVoiceACKPolicy.setStatus('current')
hwQAPEDCAVideoECWmax = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 6, 139, 5, 1, 1, 10), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 15)).clone(4)).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hwQAPEDCAVideoECWmax.setStatus('current')
hwQAPEDCAVideoECWmin = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 6, 139, 5, 1, 1, 11), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 15)).clone(3)).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hwQAPEDCAVideoECWmin.setStatus('current')
hwQAPEDCAVideoAIFSN = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 6, 139, 5, 1, 1, 12), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 15)).clone(1)).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hwQAPEDCAVideoAIFSN.setStatus('current')
hwQAPEDCAVideoTXOPLimit = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 6, 139, 5, 1, 1, 13), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 65535)).clone(94)).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hwQAPEDCAVideoTXOPLimit.setStatus('current')
hwQAPEDCAVideoACKPolicy = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 6, 139, 5, 1, 1, 14), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("normal", 1), ("noack", 2))).clone(1)).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hwQAPEDCAVideoACKPolicy.setStatus('current')
hwQAPEDCABEECWmax = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 6, 139, 5, 1, 1, 15), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 15)).clone(6)).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hwQAPEDCABEECWmax.setStatus('current')
hwQAPEDCABEECWmin = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 6, 139, 5, 1, 1, 16), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 15)).clone(4)).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hwQAPEDCABEECWmin.setStatus('current')
hwQAPEDCABEAIFSN = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 6, 139, 5, 1, 1, 17), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 15)).clone(3)).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hwQAPEDCABEAIFSN.setStatus('current')
hwQAPEDCABETXOPLimit = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 6, 139, 5, 1, 1, 18), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 65535))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hwQAPEDCABETXOPLimit.setStatus('current')
hwQAPEDCABEACKPolicy = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 6, 139, 5, 1, 1, 19), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("normal", 1), ("noack", 2))).clone(1)).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hwQAPEDCABEACKPolicy.setStatus('current')
hwQAPEDCABKECWmax = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 6, 139, 5, 1, 1, 20), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 15)).clone(10)).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hwQAPEDCABKECWmax.setStatus('current')
hwQAPEDCABKECWmin = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 6, 139, 5, 1, 1, 21), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 15)).clone(4)).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hwQAPEDCABKECWmin.setStatus('current')
hwQAPEDCABKAIFSN = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 6, 139, 5, 1, 1, 22), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 15)).clone(7)).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hwQAPEDCABKAIFSN.setStatus('current')
hwQAPEDCABKTXOPLimit = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 6, 139, 5, 1, 1, 23), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 65535))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hwQAPEDCABKTXOPLimit.setStatus('current')
hwQAPEDCABKACKPolicy = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 6, 139, 5, 1, 1, 24), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("normal", 1), ("noack", 2))).clone(1)).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hwQAPEDCABKACKPolicy.setStatus('current')
hwQClientEDCAVoiceECWmax = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 6, 139, 5, 1, 1, 25), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 15)).clone(3)).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hwQClientEDCAVoiceECWmax.setStatus('current')
hwQClientEDCAVoiceECWmin = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 6, 139, 5, 1, 1, 26), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 15)).clone(2)).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hwQClientEDCAVoiceECWmin.setStatus('current')
hwQClientEDCAVoiceAIFSN = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 6, 139, 5, 1, 1, 27), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 15)).clone(2)).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hwQClientEDCAVoiceAIFSN.setStatus('current')
hwQClientEDCAVoiceTXOPLimit = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 6, 139, 5, 1, 1, 28), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 65535)).clone(47)).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hwQClientEDCAVoiceTXOPLimit.setStatus('current')
hwQClientEDCAVideoECWmax = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 6, 139, 5, 1, 1, 29), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 15)).clone(4)).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hwQClientEDCAVideoECWmax.setStatus('current')
hwQClientEDCAVideoECWmin = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 6, 139, 5, 1, 1, 30), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 15)).clone(3)).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hwQClientEDCAVideoECWmin.setStatus('current')
hwQClientEDCAVideoAIFSN = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 6, 139, 5, 1, 1, 31), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 15)).clone(2)).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hwQClientEDCAVideoAIFSN.setStatus('current')
hwQClientEDCAVideoTXOPLimit = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 6, 139, 5, 1, 1, 32), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 65535)).clone(94)).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hwQClientEDCAVideoTXOPLimit.setStatus('current')
hwQClientEDCABEECWmax = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 6, 139, 5, 1, 1, 33), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 15)).clone(10)).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hwQClientEDCABEECWmax.setStatus('current')
hwQClientEDCABEECWmin = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 6, 139, 5, 1, 1, 34), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 15)).clone(4)).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hwQClientEDCABEECWmin.setStatus('current')
hwQClientEDCABEAIFSN = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 6, 139, 5, 1, 1, 35), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 15)).clone(3)).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hwQClientEDCABEAIFSN.setStatus('current')
hwQClientEDCABETXOPLimit = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 6, 139, 5, 1, 1, 36), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 65535))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hwQClientEDCABETXOPLimit.setStatus('current')
hwQClientEDCABKECWmax = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 6, 139, 5, 1, 1, 37), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 15)).clone(10)).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hwQClientEDCABKECWmax.setStatus('current')
hwQClientEDCABKECWmin = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 6, 139, 5, 1, 1, 38), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 15)).clone(4)).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hwQClientEDCABKECWmin.setStatus('current')
hwQClientEDCABKAIFSN = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 6, 139, 5, 1, 1, 39), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 15)).clone(7)).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hwQClientEDCABKAIFSN.setStatus('current')
hwQClientEDCABKTXOPLimit = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 6, 139, 5, 1, 1, 40), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 65535))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hwQClientEDCABKTXOPLimit.setStatus('current')
hwWlanTrafficProfileTable = MibTable((1, 3, 6, 1, 4, 1, 2011, 6, 139, 5, 2), )
if mibBuilder.loadTexts: hwWlanTrafficProfileTable.setStatus('current')
hwWlanTrafficProfileEntry = MibTableRow((1, 3, 6, 1, 4, 1, 2011, 6, 139, 5, 2, 1), ).setIndexNames((0, "HUAWEI-WLAN-QOS-MIB", "hwWlanTrafficProfileName"))
if mibBuilder.loadTexts: hwWlanTrafficProfileEntry.setStatus('current')
hwWlanTrafficProfileName = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 6, 139, 5, 2, 1, 1), OctetString().subtype(subtypeSpec=ValueSizeConstraint(1, 31)))
if mibBuilder.loadTexts: hwWlanTrafficProfileName.setStatus('current')
hwWlanTrafficProfileRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 6, 139, 5, 2, 1, 2), RowStatus()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hwWlanTrafficProfileRowStatus.setStatus('current')
hwWlanClientUpLimitRate = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 6, 139, 5, 2, 1, 3), Unsigned32()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hwWlanClientUpLimitRate.setStatus('current')
hwWlanVAPUpLimitRate = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 6, 139, 5, 2, 1, 4), Unsigned32()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hwWlanVAPUpLimitRate.setStatus('current')
hwWlan8021pMapMode = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 6, 139, 5, 2, 1, 5), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("designate", 1), ("mapping", 2)))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hwWlan8021pMapMode.setStatus('current')
hwWlan8021pSpecValue = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 6, 139, 5, 2, 1, 6), Integer32()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hwWlan8021pSpecValue.setStatus('current')
hwWlanUP0Map8021p = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 6, 139, 5, 2, 1, 7), Integer32()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hwWlanUP0Map8021p.setStatus('current')
hwWlanUP1Map8021p = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 6, 139, 5, 2, 1, 8), Integer32().clone(1)).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hwWlanUP1Map8021p.setStatus('current')
hwWlanUP2Map8021p = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 6, 139, 5, 2, 1, 9), Integer32().clone(2)).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hwWlanUP2Map8021p.setStatus('current')
hwWlanUP3Map8021p = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 6, 139, 5, 2, 1, 10), Integer32().clone(3)).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hwWlanUP3Map8021p.setStatus('current')
hwWlanUP4Map8021p = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 6, 139, 5, 2, 1, 11), Integer32().clone(4)).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hwWlanUP4Map8021p.setStatus('current')
hwWlanUP5Map8021p = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 6, 139, 5, 2, 1, 12), Integer32().clone(5)).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hwWlanUP5Map8021p.setStatus('current')
hwWlanUP6Map8021p = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 6, 139, 5, 2, 1, 13), Integer32().clone(6)).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hwWlanUP6Map8021p.setStatus('current')
hwWlanUP7Map8021p = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 6, 139, 5, 2, 1, 14), Integer32().clone(7)).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hwWlanUP7Map8021p.setStatus('current')
hwWlan8021p0MapUPValue = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 6, 139, 5, 2, 1, 15), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 7))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hwWlan8021p0MapUPValue.setStatus('current')
hwWlan8021p1MapUPValue = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 6, 139, 5, 2, 1, 16), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 7)).clone(1)).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hwWlan8021p1MapUPValue.setStatus('current')
hwWlan8021p2MapUPValue = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 6, 139, 5, 2, 1, 17), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 7)).clone(2)).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hwWlan8021p2MapUPValue.setStatus('current')
hwWlan8021p3MapUPValue = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 6, 139, 5, 2, 1, 18), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 7)).clone(3)).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hwWlan8021p3MapUPValue.setStatus('current')
hwWlan8021p4MapUPValue = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 6, 139, 5, 2, 1, 19), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 7)).clone(4)).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hwWlan8021p4MapUPValue.setStatus('current')
hwWlan8021p5MapUPValue = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 6, 139, 5, 2, 1, 20), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 7)).clone(5)).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hwWlan8021p5MapUPValue.setStatus('current')
hwWlan8021p6MapUPValue = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 6, 139, 5, 2, 1, 21), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 7)).clone(6)).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hwWlan8021p6MapUPValue.setStatus('current')
hwWlan8021p7MapUPValue = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 6, 139, 5, 2, 1, 22), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 7)).clone(7)).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hwWlan8021p7MapUPValue.setStatus('current')
hwWlanUpTunnelPriorityMapMode = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 6, 139, 5, 2, 1, 23), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6))).clone(namedValues=NamedValues(("specCOS", 1), ("specDSCP", 2), ("cos2cos", 3), ("cos2dscp", 4), ("dscp2cos", 5), ("dscp2dscp", 6))).clone(6)).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hwWlanUpTunnelPriorityMapMode.setStatus('current')
hwWlanUpTunnelPrioritySpecValue = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 6, 139, 5, 2, 1, 24), Integer32()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hwWlanUpTunnelPrioritySpecValue.setStatus('current')
hwWlanValue0MapUpTunnelPriority = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 6, 139, 5, 2, 1, 25), Integer32()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hwWlanValue0MapUpTunnelPriority.setStatus('current')
hwWlanValue1MapUpTunnelPriority = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 6, 139, 5, 2, 1, 26), Integer32().clone(1)).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hwWlanValue1MapUpTunnelPriority.setStatus('current')
hwWlanValue2MapUpTunnelPriority = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 6, 139, 5, 2, 1, 27), Integer32().clone(2)).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hwWlanValue2MapUpTunnelPriority.setStatus('current')
hwWlanValue3MapUpTunnelPriority = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 6, 139, 5, 2, 1, 28), Integer32().clone(3)).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hwWlanValue3MapUpTunnelPriority.setStatus('current')
hwWlanValue4MapUpTunnelPriority = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 6, 139, 5, 2, 1, 29), Integer32().clone(4)).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hwWlanValue4MapUpTunnelPriority.setStatus('current')
hwWlanValue5MapUpTunnelPriority = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 6, 139, 5, 2, 1, 30), Integer32().clone(5)).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hwWlanValue5MapUpTunnelPriority.setStatus('current')
hwWlanValue6MapUpTunnelPriority = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 6, 139, 5, 2, 1, 31), Integer32().clone(6)).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hwWlanValue6MapUpTunnelPriority.setStatus('current')
hwWlanValue7MapUpTunnelPriority = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 6, 139, 5, 2, 1, 32), Integer32().clone(7)).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hwWlanValue7MapUpTunnelPriority.setStatus('current')
hwWlanDownTunnelPriorityMapMode = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 6, 139, 5, 2, 1, 33), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6))).clone(namedValues=NamedValues(("specCOS", 1), ("specDSCP", 2), ("cos2cos", 3), ("cos2dscp", 4), ("dscp2cos", 5), ("dscp2dscp", 6))).clone(6)).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hwWlanDownTunnelPriorityMapMode.setStatus('current')
hwWlanDownTunnelPrioritySpecValue = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 6, 139, 5, 2, 1, 34), Integer32()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hwWlanDownTunnelPrioritySpecValue.setStatus('current')
hwWlanValue0MapDownTunnelPriority = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 6, 139, 5, 2, 1, 35), Integer32()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hwWlanValue0MapDownTunnelPriority.setStatus('current')
hwWlanValue1MapDownTunnelPriority = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 6, 139, 5, 2, 1, 36), Integer32().clone(1)).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hwWlanValue1MapDownTunnelPriority.setStatus('current')
hwWlanValue2MapDownTunnelPriority = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 6, 139, 5, 2, 1, 37), Integer32().clone(2)).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hwWlanValue2MapDownTunnelPriority.setStatus('current')
hwWlanValue3MapDownTunnelPriority = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 6, 139, 5, 2, 1, 38), Integer32().clone(7)).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hwWlanValue3MapDownTunnelPriority.setStatus('current')
hwWlanValue4MapDownTunnelPriority = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 6, 139, 5, 2, 1, 39), Integer32().clone(4)).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hwWlanValue4MapDownTunnelPriority.setStatus('current')
hwWlanValue5MapDownTunnelPriority = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 6, 139, 5, 2, 1, 40), Integer32().clone(5)).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hwWlanValue5MapDownTunnelPriority.setStatus('current')
hwWlanValue6MapDownTunnelPriority = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 6, 139, 5, 2, 1, 41), Integer32().clone(6)).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hwWlanValue6MapDownTunnelPriority.setStatus('current')
hwWlanValue7MapDownTunnelPriority = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 6, 139, 5, 2, 1, 42), Integer32().clone(7)).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hwWlanValue7MapDownTunnelPriority.setStatus('current')
hwWlanClientDownLimitRate = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 6, 139, 5, 2, 1, 43), Unsigned32()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hwWlanClientDownLimitRate.setStatus('current')
hwWlanVAPDownLimitRate = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 6, 139, 5, 2, 1, 44), Unsigned32()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hwWlanVAPDownLimitRate.setStatus('current')
hwWlanTos0MapUPValue = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 6, 139, 5, 2, 1, 45), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 7))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hwWlanTos0MapUPValue.setStatus('current')
hwWlanTos1MapUPValue = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 6, 139, 5, 2, 1, 46), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 7)).clone(1)).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hwWlanTos1MapUPValue.setStatus('current')
hwWlanTos2MapUPValue = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 6, 139, 5, 2, 1, 47), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 7)).clone(2)).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hwWlanTos2MapUPValue.setStatus('current')
hwWlanTos3MapUPValue = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 6, 139, 5, 2, 1, 48), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 7)).clone(3)).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hwWlanTos3MapUPValue.setStatus('current')
hwWlanTos4MapUPValue = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 6, 139, 5, 2, 1, 49), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 7)).clone(4)).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hwWlanTos4MapUPValue.setStatus('current')
hwWlanTos5MapUPValue = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 6, 139, 5, 2, 1, 50), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 7)).clone(5)).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hwWlanTos5MapUPValue.setStatus('current')
hwWlanTos6MapUPValue = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 6, 139, 5, 2, 1, 51), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 7)).clone(6)).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hwWlanTos6MapUPValue.setStatus('current')
hwWlanTos7MapUPValue = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 6, 139, 5, 2, 1, 52), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 7)).clone(7)).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hwWlanTos7MapUPValue.setStatus('current')
hwWlanBatchWmmProfileStartNumber = MibScalar((1, 3, 6, 1, 4, 1, 2011, 6, 139, 5, 3), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 32))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hwWlanBatchWmmProfileStartNumber.setStatus('current')
hwWlanBatchWmmProfileGetNumber = MibScalar((1, 3, 6, 1, 4, 1, 2011, 6, 139, 5, 4), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 32))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hwWlanBatchWmmProfileGetNumber.setStatus('current')
hwWlanBatchWmmProfileReturnNumber = MibScalar((1, 3, 6, 1, 4, 1, 2011, 6, 139, 5, 5), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hwWlanBatchWmmProfileReturnNumber.setStatus('current')
hwWlanBatchWmmProfileName = MibScalar((1, 3, 6, 1, 4, 1, 2011, 6, 139, 5, 6), OctetString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hwWlanBatchWmmProfileName.setStatus('current')
hwWlanBatchTrafficProfileStartNumber = MibScalar((1, 3, 6, 1, 4, 1, 2011, 6, 139, 5, 7), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 32))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hwWlanBatchTrafficProfileStartNumber.setStatus('current')
hwWlanBatchTrafficProfileGetNumber = MibScalar((1, 3, 6, 1, 4, 1, 2011, 6, 139, 5, 8), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 32))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hwWlanBatchTrafficProfileGetNumber.setStatus('current')
hwWlanBatchTrafficProfileReturnNumber = MibScalar((1, 3, 6, 1, 4, 1, 2011, 6, 139, 5, 9), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hwWlanBatchTrafficProfileReturnNumber.setStatus('current')
hwWlanBatchTrafficProfileName = MibScalar((1, 3, 6, 1, 4, 1, 2011, 6, 139, 5, 10), OctetString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hwWlanBatchTrafficProfileName.setStatus('current')
hwWlanQosManagementObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 6, 139, 5, 11))
hwWlanQosManagementConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 6, 139, 5, 12))
hwWlanQosManagementCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 6, 139, 5, 12, 1))
hwWlanQosManagementCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 2011, 6, 139, 5, 12, 1, 1)).setObjects(("HUAWEI-WLAN-QOS-MIB", "hwWlanWmmProfileGroup"), ("HUAWEI-WLAN-QOS-MIB", "hwWlanTrafficProfileGroup"), ("HUAWEI-WLAN-QOS-MIB", "hwWlanQosManagementGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    hwWlanQosManagementCompliance = hwWlanQosManagementCompliance.setStatus('current')
hwWlanQosManagementObjectGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 6, 139, 5, 12, 2))
hwWlanWmmProfileGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 2011, 6, 139, 5, 12, 2, 1)).setObjects(("HUAWEI-WLAN-QOS-MIB", "hwWlanWmmSwitch"), ("HUAWEI-WLAN-QOS-MIB", "hwWlanWmmMandatorySwitch"), ("HUAWEI-WLAN-QOS-MIB", "hwWlanWmmProfileRowStatus"), ("HUAWEI-WLAN-QOS-MIB", "hwQAPEDCAVoiceECWmax"), ("HUAWEI-WLAN-QOS-MIB", "hwQAPEDCAVoiceECWmin"), ("HUAWEI-WLAN-QOS-MIB", "hwQAPEDCAVoiceAIFSN"), ("HUAWEI-WLAN-QOS-MIB", "hwQAPEDCAVoiceTXOPLimit"), ("HUAWEI-WLAN-QOS-MIB", "hwQAPEDCAVoiceACKPolicy"), ("HUAWEI-WLAN-QOS-MIB", "hwQAPEDCAVideoECWmax"), ("HUAWEI-WLAN-QOS-MIB", "hwQAPEDCAVideoECWmin"), ("HUAWEI-WLAN-QOS-MIB", "hwQAPEDCAVideoAIFSN"), ("HUAWEI-WLAN-QOS-MIB", "hwQAPEDCAVideoTXOPLimit"), ("HUAWEI-WLAN-QOS-MIB", "hwQAPEDCAVideoACKPolicy"), ("HUAWEI-WLAN-QOS-MIB", "hwQAPEDCABEECWmax"), ("HUAWEI-WLAN-QOS-MIB", "hwQAPEDCABEECWmin"), ("HUAWEI-WLAN-QOS-MIB", "hwQAPEDCABEAIFSN"), ("HUAWEI-WLAN-QOS-MIB", "hwQAPEDCABETXOPLimit"), ("HUAWEI-WLAN-QOS-MIB", "hwQAPEDCABEACKPolicy"), ("HUAWEI-WLAN-QOS-MIB", "hwQAPEDCABKECWmax"), ("HUAWEI-WLAN-QOS-MIB", "hwQAPEDCABKECWmin"), ("HUAWEI-WLAN-QOS-MIB", "hwQAPEDCABKAIFSN"), ("HUAWEI-WLAN-QOS-MIB", "hwQAPEDCABKTXOPLimit"), ("HUAWEI-WLAN-QOS-MIB", "hwQAPEDCABKACKPolicy"), ("HUAWEI-WLAN-QOS-MIB", "hwQClientEDCAVoiceECWmax"), ("HUAWEI-WLAN-QOS-MIB", "hwQClientEDCAVoiceECWmin"), ("HUAWEI-WLAN-QOS-MIB", "hwQClientEDCAVoiceAIFSN"), ("HUAWEI-WLAN-QOS-MIB", "hwQClientEDCAVoiceTXOPLimit"), ("HUAWEI-WLAN-QOS-MIB", "hwQClientEDCAVideoECWmax"), ("HUAWEI-WLAN-QOS-MIB", "hwQClientEDCAVideoECWmin"), ("HUAWEI-WLAN-QOS-MIB", "hwQClientEDCAVideoAIFSN"), ("HUAWEI-WLAN-QOS-MIB", "hwQClientEDCAVideoTXOPLimit"), ("HUAWEI-WLAN-QOS-MIB", "hwQClientEDCABEECWmax"), ("HUAWEI-WLAN-QOS-MIB", "hwQClientEDCABEECWmin"), ("HUAWEI-WLAN-QOS-MIB", "hwQClientEDCABEAIFSN"), ("HUAWEI-WLAN-QOS-MIB", "hwQClientEDCABETXOPLimit"), ("HUAWEI-WLAN-QOS-MIB", "hwQClientEDCABKECWmax"), ("HUAWEI-WLAN-QOS-MIB", "hwQClientEDCABKECWmin"), ("HUAWEI-WLAN-QOS-MIB", "hwQClientEDCABKAIFSN"), ("HUAWEI-WLAN-QOS-MIB", "hwQClientEDCABKTXOPLimit"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    hwWlanWmmProfileGroup = hwWlanWmmProfileGroup.setStatus('current')
hwWlanTrafficProfileGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 2011, 6, 139, 5, 12, 2, 2)).setObjects(("HUAWEI-WLAN-QOS-MIB", "hwWlanTrafficProfileRowStatus"), ("HUAWEI-WLAN-QOS-MIB", "hwWlanClientUpLimitRate"), ("HUAWEI-WLAN-QOS-MIB", "hwWlanVAPUpLimitRate"), ("HUAWEI-WLAN-QOS-MIB", "hwWlan8021pMapMode"), ("HUAWEI-WLAN-QOS-MIB", "hwWlan8021pSpecValue"), ("HUAWEI-WLAN-QOS-MIB", "hwWlanUP0Map8021p"), ("HUAWEI-WLAN-QOS-MIB", "hwWlanUP1Map8021p"), ("HUAWEI-WLAN-QOS-MIB", "hwWlanUP2Map8021p"), ("HUAWEI-WLAN-QOS-MIB", "hwWlanUP3Map8021p"), ("HUAWEI-WLAN-QOS-MIB", "hwWlanUP4Map8021p"), ("HUAWEI-WLAN-QOS-MIB", "hwWlanUP5Map8021p"), ("HUAWEI-WLAN-QOS-MIB", "hwWlanUP6Map8021p"), ("HUAWEI-WLAN-QOS-MIB", "hwWlanUP7Map8021p"), ("HUAWEI-WLAN-QOS-MIB", "hwWlan8021p0MapUPValue"), ("HUAWEI-WLAN-QOS-MIB", "hwWlan8021p1MapUPValue"), ("HUAWEI-WLAN-QOS-MIB", "hwWlan8021p2MapUPValue"), ("HUAWEI-WLAN-QOS-MIB", "hwWlan8021p3MapUPValue"), ("HUAWEI-WLAN-QOS-MIB", "hwWlan8021p4MapUPValue"), ("HUAWEI-WLAN-QOS-MIB", "hwWlan8021p5MapUPValue"), ("HUAWEI-WLAN-QOS-MIB", "hwWlan8021p6MapUPValue"), ("HUAWEI-WLAN-QOS-MIB", "hwWlan8021p7MapUPValue"), ("HUAWEI-WLAN-QOS-MIB", "hwWlanUpTunnelPriorityMapMode"), ("HUAWEI-WLAN-QOS-MIB", "hwWlanUpTunnelPrioritySpecValue"), ("HUAWEI-WLAN-QOS-MIB", "hwWlanValue0MapUpTunnelPriority"), ("HUAWEI-WLAN-QOS-MIB", "hwWlanValue1MapUpTunnelPriority"), ("HUAWEI-WLAN-QOS-MIB", "hwWlanValue2MapUpTunnelPriority"), ("HUAWEI-WLAN-QOS-MIB", "hwWlanValue3MapUpTunnelPriority"), ("HUAWEI-WLAN-QOS-MIB", "hwWlanValue4MapUpTunnelPriority"), ("HUAWEI-WLAN-QOS-MIB", "hwWlanValue5MapUpTunnelPriority"), ("HUAWEI-WLAN-QOS-MIB", "hwWlanValue6MapUpTunnelPriority"), ("HUAWEI-WLAN-QOS-MIB", "hwWlanValue7MapUpTunnelPriority"), ("HUAWEI-WLAN-QOS-MIB", "hwWlanDownTunnelPriorityMapMode"), ("HUAWEI-WLAN-QOS-MIB", "hwWlanDownTunnelPrioritySpecValue"), ("HUAWEI-WLAN-QOS-MIB", "hwWlanValue0MapDownTunnelPriority"), ("HUAWEI-WLAN-QOS-MIB", "hwWlanValue1MapDownTunnelPriority"), ("HUAWEI-WLAN-QOS-MIB", "hwWlanValue2MapDownTunnelPriority"), ("HUAWEI-WLAN-QOS-MIB", "hwWlanValue3MapDownTunnelPriority"), ("HUAWEI-WLAN-QOS-MIB", "hwWlanValue4MapDownTunnelPriority"), ("HUAWEI-WLAN-QOS-MIB", "hwWlanValue5MapDownTunnelPriority"), ("HUAWEI-WLAN-QOS-MIB", "hwWlanValue6MapDownTunnelPriority"), ("HUAWEI-WLAN-QOS-MIB", "hwWlanValue7MapDownTunnelPriority"), ("HUAWEI-WLAN-QOS-MIB", "hwWlanClientDownLimitRate"), ("HUAWEI-WLAN-QOS-MIB", "hwWlanVAPDownLimitRate"), ("HUAWEI-WLAN-QOS-MIB", "hwWlanTos0MapUPValue"), ("HUAWEI-WLAN-QOS-MIB", "hwWlanTos1MapUPValue"), ("HUAWEI-WLAN-QOS-MIB", "hwWlanTos2MapUPValue"), ("HUAWEI-WLAN-QOS-MIB", "hwWlanTos3MapUPValue"), ("HUAWEI-WLAN-QOS-MIB", "hwWlanTos4MapUPValue"), ("HUAWEI-WLAN-QOS-MIB", "hwWlanTos5MapUPValue"), ("HUAWEI-WLAN-QOS-MIB", "hwWlanTos6MapUPValue"), ("HUAWEI-WLAN-QOS-MIB", "hwWlanTos7MapUPValue"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    hwWlanTrafficProfileGroup = hwWlanTrafficProfileGroup.setStatus('current')
hwWlanQosManagementGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 2011, 6, 139, 5, 12, 2, 3)).setObjects(("HUAWEI-WLAN-QOS-MIB", "hwWlanBatchWmmProfileStartNumber"), ("HUAWEI-WLAN-QOS-MIB", "hwWlanBatchWmmProfileGetNumber"), ("HUAWEI-WLAN-QOS-MIB", "hwWlanBatchWmmProfileReturnNumber"), ("HUAWEI-WLAN-QOS-MIB", "hwWlanBatchWmmProfileName"), ("HUAWEI-WLAN-QOS-MIB", "hwWlanBatchTrafficProfileStartNumber"), ("HUAWEI-WLAN-QOS-MIB", "hwWlanBatchTrafficProfileGetNumber"), ("HUAWEI-WLAN-QOS-MIB", "hwWlanBatchTrafficProfileReturnNumber"), ("HUAWEI-WLAN-QOS-MIB", "hwWlanBatchTrafficProfileName"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    hwWlanQosManagementGroup = hwWlanQosManagementGroup.setStatus('current')
mibBuilder.exportSymbols("HUAWEI-WLAN-QOS-MIB", hwWlan8021p5MapUPValue=hwWlan8021p5MapUPValue, hwWlanBatchTrafficProfileGetNumber=hwWlanBatchTrafficProfileGetNumber, hwWlanDownTunnelPrioritySpecValue=hwWlanDownTunnelPrioritySpecValue, hwQClientEDCAVideoTXOPLimit=hwQClientEDCAVideoTXOPLimit, hwWlanValue7MapUpTunnelPriority=hwWlanValue7MapUpTunnelPriority, hwWlanBatchWmmProfileReturnNumber=hwWlanBatchWmmProfileReturnNumber, hwQAPEDCAVoiceAIFSN=hwQAPEDCAVoiceAIFSN, hwQClientEDCABEECWmin=hwQClientEDCABEECWmin, hwWlanWmmProfileName=hwWlanWmmProfileName, hwWlanVAPDownLimitRate=hwWlanVAPDownLimitRate, hwQAPEDCAVideoACKPolicy=hwQAPEDCAVideoACKPolicy, hwWlanTos4MapUPValue=hwWlanTos4MapUPValue, hwWlanTos1MapUPValue=hwWlanTos1MapUPValue, hwWlanBatchTrafficProfileName=hwWlanBatchTrafficProfileName, hwWlanQosManagementObjectGroups=hwWlanQosManagementObjectGroups, hwWlanUP1Map8021p=hwWlanUP1Map8021p, hwQClientEDCAVideoECWmin=hwQClientEDCAVideoECWmin, hwWlanUP6Map8021p=hwWlanUP6Map8021p, hwWlanTos6MapUPValue=hwWlanTos6MapUPValue, hwWlanValue4MapDownTunnelPriority=hwWlanValue4MapDownTunnelPriority, hwWlanUP0Map8021p=hwWlanUP0Map8021p, hwWlan8021pMapMode=hwWlan8021pMapMode, hwQClientEDCAVideoECWmax=hwQClientEDCAVideoECWmax, hwWlanValue5MapDownTunnelPriority=hwWlanValue5MapDownTunnelPriority, hwWlanValue0MapDownTunnelPriority=hwWlanValue0MapDownTunnelPriority, hwQAPEDCAVoiceECWmax=hwQAPEDCAVoiceECWmax, hwWlan8021p7MapUPValue=hwWlan8021p7MapUPValue, hwQAPEDCAVideoECWmax=hwQAPEDCAVideoECWmax, hwQAPEDCAVideoECWmin=hwQAPEDCAVideoECWmin, hwWlanQosManagementCompliances=hwWlanQosManagementCompliances, hwWlanTos0MapUPValue=hwWlanTos0MapUPValue, hwWlanVAPUpLimitRate=hwWlanVAPUpLimitRate, hwWlanValue6MapDownTunnelPriority=hwWlanValue6MapDownTunnelPriority, hwWlanTrafficProfileTable=hwWlanTrafficProfileTable, hwQClientEDCABKTXOPLimit=hwQClientEDCABKTXOPLimit, hwQAPEDCAVoiceTXOPLimit=hwQAPEDCAVoiceTXOPLimit, hwWlanTos3MapUPValue=hwWlanTos3MapUPValue, hwWlanUpTunnelPrioritySpecValue=hwWlanUpTunnelPrioritySpecValue, hwQAPEDCAVideoAIFSN=hwQAPEDCAVideoAIFSN, hwQAPEDCABEECWmax=hwQAPEDCABEECWmax, hwWlanValue3MapDownTunnelPriority=hwWlanValue3MapDownTunnelPriority, hwQClientEDCABKECWmax=hwQClientEDCABKECWmax, hwWlanUP2Map8021p=hwWlanUP2Map8021p, hwQClientEDCAVoiceTXOPLimit=hwQClientEDCAVoiceTXOPLimit, hwWlanClientUpLimitRate=hwWlanClientUpLimitRate, hwWlanTos2MapUPValue=hwWlanTos2MapUPValue, hwWlanValue4MapUpTunnelPriority=hwWlanValue4MapUpTunnelPriority, hwWlanWmmSwitch=hwWlanWmmSwitch, hwWlanTos5MapUPValue=hwWlanTos5MapUPValue, hwWlanValue1MapUpTunnelPriority=hwWlanValue1MapUpTunnelPriority, hwQClientEDCAVideoAIFSN=hwQClientEDCAVideoAIFSN, hwWlanBatchWmmProfileGetNumber=hwWlanBatchWmmProfileGetNumber, hwWlanUpTunnelPriorityMapMode=hwWlanUpTunnelPriorityMapMode, hwWlanTrafficProfileGroup=hwWlanTrafficProfileGroup, hwWlan8021p0MapUPValue=hwWlan8021p0MapUPValue, hwWlan8021p6MapUPValue=hwWlan8021p6MapUPValue, hwWlanValue3MapUpTunnelPriority=hwWlanValue3MapUpTunnelPriority, hwQAPEDCABKECWmin=hwQAPEDCABKECWmin, hwQClientEDCABEAIFSN=hwQClientEDCABEAIFSN, hwQAPEDCAVoiceACKPolicy=hwQAPEDCAVoiceACKPolicy, hwWlanValue2MapUpTunnelPriority=hwWlanValue2MapUpTunnelPriority, hwWlanUP3Map8021p=hwWlanUP3Map8021p, hwQAPEDCAVideoTXOPLimit=hwQAPEDCAVideoTXOPLimit, hwQAPEDCABKTXOPLimit=hwQAPEDCABKTXOPLimit, hwWlanQosManagementObjects=hwWlanQosManagementObjects, hwWlanValue0MapUpTunnelPriority=hwWlanValue0MapUpTunnelPriority, hwWlanValue6MapUpTunnelPriority=hwWlanValue6MapUpTunnelPriority, hwWlanQosManagementCompliance=hwWlanQosManagementCompliance, hwQAPEDCABEAIFSN=hwQAPEDCABEAIFSN, hwQClientEDCABKECWmin=hwQClientEDCABKECWmin, PYSNMP_MODULE_ID=hwWlanQosManagement, hwQAPEDCABKECWmax=hwQAPEDCABKECWmax, hwWlanUP4Map8021p=hwWlanUP4Map8021p, hwWlanTrafficProfileRowStatus=hwWlanTrafficProfileRowStatus, hwQAPEDCABKAIFSN=hwQAPEDCABKAIFSN, hwWlanUP5Map8021p=hwWlanUP5Map8021p, hwWlanValue5MapUpTunnelPriority=hwWlanValue5MapUpTunnelPriority, hwWlanQosManagementConformance=hwWlanQosManagementConformance, hwQClientEDCABEECWmax=hwQClientEDCABEECWmax, hwWlanTrafficProfileName=hwWlanTrafficProfileName, hwQClientEDCABETXOPLimit=hwQClientEDCABETXOPLimit, hwWlanDownTunnelPriorityMapMode=hwWlanDownTunnelPriorityMapMode, hwQAPEDCABETXOPLimit=hwQAPEDCABETXOPLimit, hwQAPEDCABEECWmin=hwQAPEDCABEECWmin, hwWlan8021p4MapUPValue=hwWlan8021p4MapUPValue, hwWlanQosManagement=hwWlanQosManagement, hwWlanWmmProfileRowStatus=hwWlanWmmProfileRowStatus, hwWlan8021p3MapUPValue=hwWlan8021p3MapUPValue, hwQAPEDCAVoiceECWmin=hwQAPEDCAVoiceECWmin, hwQAPEDCABKACKPolicy=hwQAPEDCABKACKPolicy, hwQClientEDCAVoiceAIFSN=hwQClientEDCAVoiceAIFSN, hwWlanBatchWmmProfileName=hwWlanBatchWmmProfileName, hwWlanQosManagementGroup=hwWlanQosManagementGroup, hwWlanTos7MapUPValue=hwWlanTos7MapUPValue, hwWlanWmmProfileTable=hwWlanWmmProfileTable, hwQAPEDCABEACKPolicy=hwQAPEDCABEACKPolicy, hwWlanBatchTrafficProfileReturnNumber=hwWlanBatchTrafficProfileReturnNumber, hwWlan8021p1MapUPValue=hwWlan8021p1MapUPValue, hwWlanWmmProfileGroup=hwWlanWmmProfileGroup, hwWlanUP7Map8021p=hwWlanUP7Map8021p, hwWlanTrafficProfileEntry=hwWlanTrafficProfileEntry, hwWlanBatchTrafficProfileStartNumber=hwWlanBatchTrafficProfileStartNumber, hwWlan8021p2MapUPValue=hwWlan8021p2MapUPValue, hwWlanValue2MapDownTunnelPriority=hwWlanValue2MapDownTunnelPriority, hwWlanWmmMandatorySwitch=hwWlanWmmMandatorySwitch, hwWlanWmmProfileEntry=hwWlanWmmProfileEntry, hwWlanClientDownLimitRate=hwWlanClientDownLimitRate, hwWlanBatchWmmProfileStartNumber=hwWlanBatchWmmProfileStartNumber, hwWlan8021pSpecValue=hwWlan8021pSpecValue, hwQClientEDCAVoiceECWmin=hwQClientEDCAVoiceECWmin, hwWlanValue1MapDownTunnelPriority=hwWlanValue1MapDownTunnelPriority, hwWlanValue7MapDownTunnelPriority=hwWlanValue7MapDownTunnelPriority, hwQClientEDCAVoiceECWmax=hwQClientEDCAVoiceECWmax, hwQClientEDCABKAIFSN=hwQClientEDCABKAIFSN)