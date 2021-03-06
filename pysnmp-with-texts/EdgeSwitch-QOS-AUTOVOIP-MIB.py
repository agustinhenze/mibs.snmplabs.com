#
# PySNMP MIB module EdgeSwitch-QOS-AUTOVOIP-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/EdgeSwitch-QOS-AUTOVOIP-MIB
# Produced by pysmi-0.3.4 at Wed May  1 13:10:44 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
OctetString, Integer, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "OctetString", "Integer", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, ConstraintsIntersection, ConstraintsUnion, ValueSizeConstraint, SingleValueConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "ConstraintsIntersection", "ConstraintsUnion", "ValueSizeConstraint", "SingleValueConstraint")
fastPathQOS, = mibBuilder.importSymbols("EdgeSwitch-QOS-MIB", "fastPathQOS")
InterfaceIndex, InterfaceIndexOrZero = mibBuilder.importSymbols("IF-MIB", "InterfaceIndex", "InterfaceIndexOrZero")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
NotificationType, TimeTicks, Counter32, ModuleIdentity, iso, Bits, Unsigned32, MibIdentifier, Counter64, ObjectIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, IpAddress, Gauge32, Integer32 = mibBuilder.importSymbols("SNMPv2-SMI", "NotificationType", "TimeTicks", "Counter32", "ModuleIdentity", "iso", "Bits", "Unsigned32", "MibIdentifier", "Counter64", "ObjectIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "IpAddress", "Gauge32", "Integer32")
DisplayString, RowStatus, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "RowStatus", "TextualConvention")
fastPathQOSAUTOVOIP = ModuleIdentity((1, 3, 6, 1, 4, 1, 4413, 1, 1, 3, 4))
fastPathQOSAUTOVOIP.setRevisions(('2012-02-18 00:00', '2011-01-26 00:00', '2007-11-23 00:00', '2007-11-23 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: fastPathQOSAUTOVOIP.setRevisionsDescriptions(('Added OUI based auto VoIP support.', 'Postal address updated.', 'Ubiquiti branding related changes.', 'Initial revision.',))
if mibBuilder.loadTexts: fastPathQOSAUTOVOIP.setLastUpdated('201101260000Z')
if mibBuilder.loadTexts: fastPathQOSAUTOVOIP.setOrganization('Broadcom Inc')
if mibBuilder.loadTexts: fastPathQOSAUTOVOIP.setContactInfo('')
if mibBuilder.loadTexts: fastPathQOSAUTOVOIP.setDescription('The MIB definitions for Quality of Service - VoIP Flex package.')
agentAutoVoIPCfgGroup = MibIdentifier((1, 3, 6, 1, 4, 1, 4413, 1, 1, 3, 4, 1))
agentAutoVoIPVLAN = MibScalar((1, 3, 6, 1, 4, 1, 4413, 1, 1, 3, 4, 1, 1), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: agentAutoVoIPVLAN.setStatus('current')
if mibBuilder.loadTexts: agentAutoVoIPVLAN.setDescription('The VLAN to which all VoIP traffic is mapped to.')
agentAutoVoIPOUIPriority = MibScalar((1, 3, 6, 1, 4, 1, 4413, 1, 1, 3, 4, 1, 2), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: agentAutoVoIPOUIPriority.setStatus('current')
if mibBuilder.loadTexts: agentAutoVoIPOUIPriority.setDescription('The priority to which all VoIP traffic with known OUI is mapped to.')
agentAutoVoIPProtocolPriScheme = MibScalar((1, 3, 6, 1, 4, 1, 4413, 1, 1, 3, 4, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("trafficClass", 1), ("remark", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: agentAutoVoIPProtocolPriScheme.setStatus('current')
if mibBuilder.loadTexts: agentAutoVoIPProtocolPriScheme.setDescription('The priotization scheme which is used to priritize the voice data. ')
agentAutoVoIPProtocolTcOrRemarkValue = MibScalar((1, 3, 6, 1, 4, 1, 4413, 1, 1, 3, 4, 1, 4), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(0, 7))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: agentAutoVoIPProtocolTcOrRemarkValue.setStatus('current')
if mibBuilder.loadTexts: agentAutoVoIPProtocolTcOrRemarkValue.setDescription("If 'agentAutoVoIPProtocolPriScheme' is traffic class, then the object 'agentAutoVoIPProtocolTcOrRemarkValue' is CoS Queue value to which all VoIP traffic is mapped to. if 'agentAutoVoIPProtocolPriScheme' is remark, then the object 'agentAutoVoIPProtocolTcOrRemarkValue' is 802.1p priority to which all VoIP traffic is remarked at the ingress port. This is used by Protocol based Auto VoIP")
agentAutoVoIPTable = MibTable((1, 3, 6, 1, 4, 1, 4413, 1, 1, 3, 4, 1, 5), )
if mibBuilder.loadTexts: agentAutoVoIPTable.setStatus('current')
if mibBuilder.loadTexts: agentAutoVoIPTable.setDescription('A table providing configuration of Auto VoIP Profile.')
agentAutoVoIPEntry = MibTableRow((1, 3, 6, 1, 4, 1, 4413, 1, 1, 3, 4, 1, 5, 1), ).setIndexNames((0, "EdgeSwitch-QOS-AUTOVOIP-MIB", "agentAutoVoIPIntfIndex"))
if mibBuilder.loadTexts: agentAutoVoIPEntry.setStatus('current')
if mibBuilder.loadTexts: agentAutoVoIPEntry.setDescription('Auto VoIP Profile configuration for a port.')
agentAutoVoIPIntfIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 4413, 1, 1, 3, 4, 1, 5, 1, 1), InterfaceIndex())
if mibBuilder.loadTexts: agentAutoVoIPIntfIndex.setStatus('current')
if mibBuilder.loadTexts: agentAutoVoIPIntfIndex.setDescription('This is a unique index for an entry in the agentAutoVoIPTable. A non-zero value indicates the ifIndex for the corresponding interface entry in the ifTable. A value of zero represents global configuration, which in turn causes all interface entries to be updated for a set operation, or reflects the most recent global setting for a get operation.')
agentAutoVoIPProtocolMode = MibTableColumn((1, 3, 6, 1, 4, 1, 4413, 1, 1, 3, 4, 1, 5, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enable", 1), ("disable", 2))).clone(2)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: agentAutoVoIPProtocolMode.setStatus('current')
if mibBuilder.loadTexts: agentAutoVoIPProtocolMode.setDescription('Enables / disables AutoVoIP Protocol profile on an interface.')
agentAutoVoIPOUIMode = MibTableColumn((1, 3, 6, 1, 4, 1, 4413, 1, 1, 3, 4, 1, 5, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enable", 1), ("disable", 2))).clone(2)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: agentAutoVoIPOUIMode.setStatus('current')
if mibBuilder.loadTexts: agentAutoVoIPOUIMode.setDescription('Enables / disables AutoVoIP OUI profile on an interface.')
agentAutoVoIPProtocolPortStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 4413, 1, 1, 3, 4, 1, 5, 1, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("up", 1), ("down", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: agentAutoVoIPProtocolPortStatus.setStatus('current')
if mibBuilder.loadTexts: agentAutoVoIPProtocolPortStatus.setDescription('AutoVoIP protocol profile operational status of an interface.')
agentAutoVoIPOUIPortStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 4413, 1, 1, 3, 4, 1, 5, 1, 5), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("up", 1), ("down", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: agentAutoVoIPOUIPortStatus.setStatus('current')
if mibBuilder.loadTexts: agentAutoVoIPOUIPortStatus.setDescription('AutoVoIP OUI profile operational status of an interface.')
agentAutoVoIPOUITable = MibTable((1, 3, 6, 1, 4, 1, 4413, 1, 1, 3, 4, 1, 6), )
if mibBuilder.loadTexts: agentAutoVoIPOUITable.setStatus('current')
if mibBuilder.loadTexts: agentAutoVoIPOUITable.setDescription('A table providing configuration of Auto VoIP Profile.')
agentAutoVoIPOUIEntry = MibTableRow((1, 3, 6, 1, 4, 1, 4413, 1, 1, 3, 4, 1, 6, 1), ).setIndexNames((0, "EdgeSwitch-QOS-AUTOVOIP-MIB", "agentAutoVoIPOUIIndex"))
if mibBuilder.loadTexts: agentAutoVoIPOUIEntry.setStatus('current')
if mibBuilder.loadTexts: agentAutoVoIPOUIEntry.setDescription('Auto VoIP Profile OUI configuration.')
agentAutoVoIPOUIIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 4413, 1, 1, 3, 4, 1, 6, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 128))).setMaxAccess("readonly")
if mibBuilder.loadTexts: agentAutoVoIPOUIIndex.setStatus('current')
if mibBuilder.loadTexts: agentAutoVoIPOUIIndex.setDescription('The Auto VoIP OUI table index.')
agentAutoVoIPOUI = MibTableColumn((1, 3, 6, 1, 4, 1, 4413, 1, 1, 3, 4, 1, 6, 1, 2), OctetString().subtype(subtypeSpec=ValueSizeConstraint(3, 3)).setFixedLength(3)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: agentAutoVoIPOUI.setStatus('current')
if mibBuilder.loadTexts: agentAutoVoIPOUI.setDescription('The Organizationally Unique Identifier (OUI), as defined in IEEE std 802-2001, is a 24 bit (three octets) globally unique assigned number referenced by various standards, of the information received from the remote system.')
agentAutoVoIPOUIDesc = MibTableColumn((1, 3, 6, 1, 4, 1, 4413, 1, 1, 3, 4, 1, 6, 1, 3), OctetString().subtype(subtypeSpec=ValueSizeConstraint(1, 32))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: agentAutoVoIPOUIDesc.setStatus('current')
if mibBuilder.loadTexts: agentAutoVoIPOUIDesc.setDescription('The Description of the Organizationally Unique Identifier (OUI), as defined in IEEE std 802-2001(up to 32 characters)')
agentAutoVoIPOUIRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 4413, 1, 1, 3, 4, 1, 6, 1, 4), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: agentAutoVoIPOUIRowStatus.setStatus('current')
if mibBuilder.loadTexts: agentAutoVoIPOUIRowStatus.setDescription('The row status variable is used according to installation and removal conventions for conceptual rows.')
agentAutoVoIPSessionTable = MibTable((1, 3, 6, 1, 4, 1, 4413, 1, 1, 3, 4, 1, 7), )
if mibBuilder.loadTexts: agentAutoVoIPSessionTable.setStatus('current')
if mibBuilder.loadTexts: agentAutoVoIPSessionTable.setDescription('A table providing configuration of Auto VoIP Profile.')
agentAutoVoIPSessionEntry = MibTableRow((1, 3, 6, 1, 4, 1, 4413, 1, 1, 3, 4, 1, 7, 1), ).setIndexNames((0, "EdgeSwitch-QOS-AUTOVOIP-MIB", "agentAutoVoIPSessionIndex"))
if mibBuilder.loadTexts: agentAutoVoIPSessionEntry.setStatus('current')
if mibBuilder.loadTexts: agentAutoVoIPSessionEntry.setDescription('Auto VoIP Session Table.')
agentAutoVoIPSessionIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 4413, 1, 1, 3, 4, 1, 7, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 127))).setMaxAccess("readonly")
if mibBuilder.loadTexts: agentAutoVoIPSessionIndex.setStatus('current')
if mibBuilder.loadTexts: agentAutoVoIPSessionIndex.setDescription('The Auto VoIP session index.')
agentAutoVoIPSourceIP = MibTableColumn((1, 3, 6, 1, 4, 1, 4413, 1, 1, 3, 4, 1, 7, 1, 2), IpAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: agentAutoVoIPSourceIP.setStatus('current')
if mibBuilder.loadTexts: agentAutoVoIPSourceIP.setDescription('The source IP address of the VoIP session.')
agentAutoVoIPDestinationIP = MibTableColumn((1, 3, 6, 1, 4, 1, 4413, 1, 1, 3, 4, 1, 7, 1, 3), IpAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: agentAutoVoIPDestinationIP.setStatus('current')
if mibBuilder.loadTexts: agentAutoVoIPDestinationIP.setDescription('The destination IP address of the VoIP session.')
agentAutoVoIPSourceL4Port = MibTableColumn((1, 3, 6, 1, 4, 1, 4413, 1, 1, 3, 4, 1, 7, 1, 4), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: agentAutoVoIPSourceL4Port.setStatus('current')
if mibBuilder.loadTexts: agentAutoVoIPSourceL4Port.setDescription('The source L4 Port of the VoIP session.')
agentAutoVoIPDestinationL4Port = MibTableColumn((1, 3, 6, 1, 4, 1, 4413, 1, 1, 3, 4, 1, 7, 1, 5), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: agentAutoVoIPDestinationL4Port.setStatus('current')
if mibBuilder.loadTexts: agentAutoVoIPDestinationL4Port.setDescription('The destination L4 Port of the VoIP session.')
agentAutoVoIPProtocol = MibTableColumn((1, 3, 6, 1, 4, 1, 4413, 1, 1, 3, 4, 1, 7, 1, 6), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: agentAutoVoIPProtocol.setStatus('current')
if mibBuilder.loadTexts: agentAutoVoIPProtocol.setDescription('The Protocol of the VoIP session.')
mibBuilder.exportSymbols("EdgeSwitch-QOS-AUTOVOIP-MIB", agentAutoVoIPProtocolMode=agentAutoVoIPProtocolMode, agentAutoVoIPOUIMode=agentAutoVoIPOUIMode, agentAutoVoIPProtocol=agentAutoVoIPProtocol, agentAutoVoIPOUIDesc=agentAutoVoIPOUIDesc, agentAutoVoIPDestinationIP=agentAutoVoIPDestinationIP, agentAutoVoIPOUIEntry=agentAutoVoIPOUIEntry, agentAutoVoIPCfgGroup=agentAutoVoIPCfgGroup, agentAutoVoIPEntry=agentAutoVoIPEntry, fastPathQOSAUTOVOIP=fastPathQOSAUTOVOIP, agentAutoVoIPSessionIndex=agentAutoVoIPSessionIndex, agentAutoVoIPSourceL4Port=agentAutoVoIPSourceL4Port, agentAutoVoIPOUIPriority=agentAutoVoIPOUIPriority, agentAutoVoIPOUIIndex=agentAutoVoIPOUIIndex, agentAutoVoIPDestinationL4Port=agentAutoVoIPDestinationL4Port, agentAutoVoIPOUI=agentAutoVoIPOUI, agentAutoVoIPOUIRowStatus=agentAutoVoIPOUIRowStatus, PYSNMP_MODULE_ID=fastPathQOSAUTOVOIP, agentAutoVoIPSessionEntry=agentAutoVoIPSessionEntry, agentAutoVoIPProtocolTcOrRemarkValue=agentAutoVoIPProtocolTcOrRemarkValue, agentAutoVoIPSourceIP=agentAutoVoIPSourceIP, agentAutoVoIPTable=agentAutoVoIPTable, agentAutoVoIPProtocolPriScheme=agentAutoVoIPProtocolPriScheme, agentAutoVoIPSessionTable=agentAutoVoIPSessionTable, agentAutoVoIPOUIPortStatus=agentAutoVoIPOUIPortStatus, agentAutoVoIPOUITable=agentAutoVoIPOUITable, agentAutoVoIPProtocolPortStatus=agentAutoVoIPProtocolPortStatus, agentAutoVoIPIntfIndex=agentAutoVoIPIntfIndex, agentAutoVoIPVLAN=agentAutoVoIPVLAN)
