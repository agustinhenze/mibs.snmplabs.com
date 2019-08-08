#
# PySNMP MIB module PDN-CPIWF-IP-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/PDN-CPIWF-IP-MIB
# Produced by pysmi-0.3.4 at Wed May  1 14:38:21 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
ObjectIdentifier, Integer, OctetString = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "Integer", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
SingleValueConstraint, ConstraintsIntersection, ValueSizeConstraint, ValueRangeConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "SingleValueConstraint", "ConstraintsIntersection", "ValueSizeConstraint", "ValueRangeConstraint", "ConstraintsUnion")
pdnCpIwfEntry, pdnCpIwfIndex = mibBuilder.importSymbols("PDN-CP-IWF-MIB", "pdnCpIwfEntry", "pdnCpIwfIndex")
pdn_common, = mibBuilder.importSymbols("PDN-HEADER-MIB", "pdn-common")
SwitchState, = mibBuilder.importSymbols("PDN-TC", "SwitchState")
NotificationGroup, ModuleCompliance, ObjectGroup = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance", "ObjectGroup")
TimeTicks, NotificationType, Counter32, Counter64, Unsigned32, IpAddress, ObjectIdentity, MibIdentifier, Integer32, MibScalar, MibTable, MibTableRow, MibTableColumn, ModuleIdentity, Bits, iso, Gauge32 = mibBuilder.importSymbols("SNMPv2-SMI", "TimeTicks", "NotificationType", "Counter32", "Counter64", "Unsigned32", "IpAddress", "ObjectIdentity", "MibIdentifier", "Integer32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "ModuleIdentity", "Bits", "iso", "Gauge32")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
pdnCpIwfIpMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 53))
pdnCpIwfIpMIB.setRevisions(('2005-03-24 11:00', '2005-01-05 11:00', '2004-12-03 11:00', '2004-10-07 11:00', '2004-09-30 11:00', '2004-08-24 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: pdnCpIwfIpMIB.setRevisionsDescriptions(('Added back pdnCpIwfIpActiveSoftswitch', 'Added pdnCpIwfIpMgcpPriAgentDNSIpAddr and pdnCpIwfIpMgcpSecAgentDNSIpAddr to the CpIwfIp MGCP Table', 'Added pdnCpIwfIpMgcpRSIPKeepAlive to the CpIwfIp MGCP Table', "o Removed pdnCpIwfIpBracketing from CpIwfIpTable is favor of pdnCpIwfIpMgcpEndPtFormat which supports more options. o Added pdnCpIwfIpMgcpEndPtFormat object for domain formatting options o Added pdnCpIwfIpMgcpDomainName object to be used if the formatting option is 'domainname (3)' o Removed the following items from mib as requested by SE: * Removed DtmfSignaling TEXTUAL-CONVENTION * Removed pdnCpIwfIpDtmfSignaling o Removed pdnCpIwfIpActiveSoftswitch in favor of keeping this object on a per Port basis rather than per IAD. o Removed DscpBits TEXTUAL-CONVENTION ", 'Added pdnCpIwfIpBracketing to the CpIwfIp Config Table', 'Initial release.',))
if mibBuilder.loadTexts: pdnCpIwfIpMIB.setLastUpdated('200412031100Z')
if mibBuilder.loadTexts: pdnCpIwfIpMIB.setOrganization('Paradyne Networks MIB Working Group Other information about group editing the MIB')
if mibBuilder.loadTexts: pdnCpIwfIpMIB.setContactInfo('Paradyne Networks, Inc. 8545 126th Avenue North Largo, FL 33773 www.paradyne.com General Comments to: mibwg_team@paradyne.com Editor Jesus Pinto')
if mibBuilder.loadTexts: pdnCpIwfIpMIB.setDescription('This module contains objects that are used for monitoring and controlling CPIWF interfaces when terminating an IP Network. This enterprise mib is meant to be used in connection with RFC 2863 which defines the ifTable and the Paradyne Enterprise PDN-CP-IWF-MIB.mib. ')
pdnCpIwfIpNotifications = MibIdentifier((1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 53, 0))
pdnCpIwfIpMIBObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 53, 1))
pdnCpIwfIpMIBConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 53, 2))
pdnCpIwfIpConfigObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 53, 1, 1))
pdnCpIwfIpTestObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 53, 1, 2))
pdnCpIwfIpStatsObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 53, 1, 3))
pdnCpIwfIpApplObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 53, 1, 4))
class VoiceChannelType(TextualConvention, Integer32):
    description = 'This textual convention defines the possible voice channel types for a CpIWF interface '
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2))
    namedValues = NamedValues(("bearer", 1), ("signaling", 2))

pdnCpIwfIpTable = MibTable((1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 53, 1, 1, 1), )
if mibBuilder.loadTexts: pdnCpIwfIpTable.setStatus('current')
if mibBuilder.loadTexts: pdnCpIwfIpTable.setDescription('The Cp-Iwf IP Configuration table.')
pdnCpIwfIpEntry = MibTableRow((1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 53, 1, 1, 1, 1), )
pdnCpIwfEntry.registerAugmentions(("PDN-CPIWF-IP-MIB", "pdnCpIwfIpEntry"))
pdnCpIwfIpEntry.setIndexNames(*pdnCpIwfEntry.getIndexNames())
if mibBuilder.loadTexts: pdnCpIwfIpEntry.setStatus('current')
if mibBuilder.loadTexts: pdnCpIwfIpEntry.setDescription('An entry in the Cp-Iwf IP configuration table. There would be one entry in this table for each entry in the pdnCpIwfTable if this CPIWF interface terminates an IP network. ')
pdnCpIwfIpAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 53, 1, 1, 1, 1, 1), IpAddress()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: pdnCpIwfIpAddress.setStatus('current')
if mibBuilder.loadTexts: pdnCpIwfIpAddress.setDescription('The IP address configured in this CpIwf A 0.0.0.0 for this object indicates that no IP address is assigned to the CpIwf Changes to this object could disrupt data flow through this CpIwf ')
pdnCpIwfIpNetMask = MibTableColumn((1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 53, 1, 1, 1, 1, 2), IpAddress()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: pdnCpIwfIpNetMask.setStatus('current')
if mibBuilder.loadTexts: pdnCpIwfIpNetMask.setDescription('The IP subnet mask configured in this CpIwf. A 0.0.0.0 for the this object indicates that no IP subnet mask is assigned to the CpIwf. Changes to this object could disrupt data flow through the CpIwf ')
pdnCpIwfIpDefGateway = MibTableColumn((1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 53, 1, 1, 1, 1, 3), IpAddress()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: pdnCpIwfIpDefGateway.setStatus('current')
if mibBuilder.loadTexts: pdnCpIwfIpDefGateway.setDescription('The IP next hop address (gateway) for this CpIwf. A 0.0.0.0 for this object indicates that no IP Gateway is assigned to the CpIwf.')
pdnCpIwfIpActiveSoftswitch = MibTableColumn((1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 53, 1, 1, 1, 1, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("primary", 1), ("secondary", 2), ("none", 3)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: pdnCpIwfIpActiveSoftswitch.setStatus('current')
if mibBuilder.loadTexts: pdnCpIwfIpActiveSoftswitch.setDescription("This object displays the active selection for the Softswitch (Call Agent, Proxy Agent, etc.) for this IAD entry. If the SNMP agent can not determine an active softswitch for this IAD entry, the value of this object will be set to 'none (3)'. This object is related to the pdnPotsPortActiveSoftswitch object for those pots port's instances terminating in this IAD. That is, if at least one pots port terminating in this IAD losses communication with its Softswitch (call agent, proxy server, etc.), the value of the current object is also set to 'none (3)'. ")
pdnCpIwfIpChanTable = MibTable((1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 53, 1, 1, 2), )
if mibBuilder.loadTexts: pdnCpIwfIpChanTable.setStatus('current')
if mibBuilder.loadTexts: pdnCpIwfIpChanTable.setDescription('The Cp-Iwf IP channel voice table.')
pdnCpIwfIpChanEntry = MibTableRow((1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 53, 1, 1, 2, 1), ).setIndexNames((0, "PDN-CP-IWF-MIB", "pdnCpIwfIndex"), (0, "PDN-CPIWF-IP-MIB", "pdnCpIwfIpChanType"))
if mibBuilder.loadTexts: pdnCpIwfIpChanEntry.setStatus('current')
if mibBuilder.loadTexts: pdnCpIwfIpChanEntry.setDescription('An entry in this table identifies a voice channel defined over a CPIWF in which an IP network terminates. Various channels may be used to carry different type of traffics (e.g, signalling, bearer). The agent is responsible for automatically populating this table with all the channels defined for each CPIWF interface. ')
pdnCpIwfIpChanType = MibTableColumn((1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 53, 1, 1, 2, 1, 1), VoiceChannelType())
if mibBuilder.loadTexts: pdnCpIwfIpChanType.setStatus('current')
if mibBuilder.loadTexts: pdnCpIwfIpChanType.setDescription('This object indicates the voice channel type which is used as the second key to identify an entry in the table')
pdnCpIwfIpChandot1dBasePort = MibTableColumn((1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 53, 1, 1, 2, 1, 2), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(1, 65535))).setMaxAccess("readonly")
if mibBuilder.loadTexts: pdnCpIwfIpChandot1dBasePort.setStatus('current')
if mibBuilder.loadTexts: pdnCpIwfIpChandot1dBasePort.setDescription('This object specifies the bridge port assigned to this channel on this CPIWF interface. These assignments are done automatically.')
pdnCpIwfIpChanTosDSCP = MibTableColumn((1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 53, 1, 1, 2, 1, 3), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 63))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: pdnCpIwfIpChanTosDSCP.setStatus('current')
if mibBuilder.loadTexts: pdnCpIwfIpChanTosDSCP.setDescription('This object is used to configure the 6 bits corresponding to the Differentiated Services Code Point as specified in RFC2474. There are 64 entries represented by this object, each bit corresponds to a code points 0 thru 63 (bits 000000 thru 111111), for each device. If additional functionallity regarding Differentiated Services is required this object could be deprecated and the standard DIFFSERV-MIB should be used instead. ')
pdnCpIwfIpRtpTable = MibTable((1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 53, 1, 4, 1), )
if mibBuilder.loadTexts: pdnCpIwfIpRtpTable.setStatus('current')
if mibBuilder.loadTexts: pdnCpIwfIpRtpTable.setDescription('The Real-Time Protocol config table for CPIWF terminating the IP network.')
pdnCpIwfIpRtpEntry = MibTableRow((1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 53, 1, 4, 1, 1), )
pdnCpIwfEntry.registerAugmentions(("PDN-CPIWF-IP-MIB", "pdnCpIwfIpRtpEntry"))
pdnCpIwfIpRtpEntry.setIndexNames(*pdnCpIwfEntry.getIndexNames())
if mibBuilder.loadTexts: pdnCpIwfIpRtpEntry.setStatus('current')
if mibBuilder.loadTexts: pdnCpIwfIpRtpEntry.setDescription('An entry in the Rtp configuration table. There would be one entry in this table for each entry in the pdnCpIwfTable if this CPIWF interface terminates an IP network. ')
pdnCpIwfIpRtpLocalPortBase = MibTableColumn((1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 53, 1, 4, 1, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 2147483647))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: pdnCpIwfIpRtpLocalPortBase.setStatus('current')
if mibBuilder.loadTexts: pdnCpIwfIpRtpLocalPortBase.setDescription('This object contains the base port range to be used for incoming RTP streams. ')
pdnCpIwfIpMgcpTable = MibTable((1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 53, 1, 4, 2), )
if mibBuilder.loadTexts: pdnCpIwfIpMgcpTable.setStatus('current')
if mibBuilder.loadTexts: pdnCpIwfIpMgcpTable.setDescription('The Media Gateway Control Protocol (MGCP) configuration parameters applicable to a CPIWF terminating the IP network.')
pdnCpIwfIpMgcpEntry = MibTableRow((1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 53, 1, 4, 2, 1), )
pdnCpIwfEntry.registerAugmentions(("PDN-CPIWF-IP-MIB", "pdnCpIwfIpMgcpEntry"))
pdnCpIwfIpMgcpEntry.setIndexNames(*pdnCpIwfEntry.getIndexNames())
if mibBuilder.loadTexts: pdnCpIwfIpMgcpEntry.setStatus('current')
if mibBuilder.loadTexts: pdnCpIwfIpMgcpEntry.setDescription('An entry in the Mgcp configuration table. There would be one entry in this table for each entry in the pdnCpIwfTable if this CPIWF interface terminates an IP network. ')
pdnCpIwfIpMgcpPortNumber = MibTableColumn((1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 53, 1, 4, 2, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 2147483647))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: pdnCpIwfIpMgcpPortNumber.setStatus('current')
if mibBuilder.loadTexts: pdnCpIwfIpMgcpPortNumber.setDescription('This object contains the local port number. ')
pdnCpIwfIpMgcpPriAgentName = MibTableColumn((1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 53, 1, 4, 2, 1, 2), DisplayString()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: pdnCpIwfIpMgcpPriAgentName.setStatus('current')
if mibBuilder.loadTexts: pdnCpIwfIpMgcpPriAgentName.setDescription('This object contains a text with the primary agent name. ')
pdnCpIwfIpMgcpPriAgentIpAddr = MibTableColumn((1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 53, 1, 4, 2, 1, 3), IpAddress()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: pdnCpIwfIpMgcpPriAgentIpAddr.setStatus('current')
if mibBuilder.loadTexts: pdnCpIwfIpMgcpPriAgentIpAddr.setDescription("This object contains the primary agent's IP Address. ")
pdnCpIwfIpMgcpPriAgentPortNum = MibTableColumn((1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 53, 1, 4, 2, 1, 4), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 2147483647))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: pdnCpIwfIpMgcpPriAgentPortNum.setStatus('current')
if mibBuilder.loadTexts: pdnCpIwfIpMgcpPriAgentPortNum.setDescription("This object contains the primary agent's port number. ")
pdnCpIwfIpMgcpPriAgentDNSIpAddr = MibTableColumn((1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 53, 1, 4, 2, 1, 5), IpAddress()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: pdnCpIwfIpMgcpPriAgentDNSIpAddr.setStatus('current')
if mibBuilder.loadTexts: pdnCpIwfIpMgcpPriAgentDNSIpAddr.setDescription("This object contains the primary agent's Domain Name Server's IP Address. ")
pdnCpIwfIpMgcpSecAgentName = MibTableColumn((1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 53, 1, 4, 2, 1, 6), DisplayString()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: pdnCpIwfIpMgcpSecAgentName.setStatus('current')
if mibBuilder.loadTexts: pdnCpIwfIpMgcpSecAgentName.setDescription('This object contains a text with the secondary agent name. ')
pdnCpIwfIpMgcpSecAgentIpAddr = MibTableColumn((1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 53, 1, 4, 2, 1, 7), IpAddress()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: pdnCpIwfIpMgcpSecAgentIpAddr.setStatus('current')
if mibBuilder.loadTexts: pdnCpIwfIpMgcpSecAgentIpAddr.setDescription("This object contains the secondary agent's IP Address. ")
pdnCpIwfIpMgcpSecAgentPortNum = MibTableColumn((1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 53, 1, 4, 2, 1, 8), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 2147483647))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: pdnCpIwfIpMgcpSecAgentPortNum.setStatus('current')
if mibBuilder.loadTexts: pdnCpIwfIpMgcpSecAgentPortNum.setDescription("This object contains the secondary agent's port number. ")
pdnCpIwfIpMgcpSecAgentDNSIpAddr = MibTableColumn((1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 53, 1, 4, 2, 1, 9), IpAddress()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: pdnCpIwfIpMgcpSecAgentDNSIpAddr.setStatus('current')
if mibBuilder.loadTexts: pdnCpIwfIpMgcpSecAgentDNSIpAddr.setDescription("This object contains the secondary agent's Domain Name Server's IP Address. ")
pdnCpIwfIpMgcpRFC2833LoopSignal = MibTableColumn((1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 53, 1, 4, 2, 1, 10), SwitchState()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: pdnCpIwfIpMgcpRFC2833LoopSignal.setStatus('current')
if mibBuilder.loadTexts: pdnCpIwfIpMgcpRFC2833LoopSignal.setDescription('This object contains the MGCP loop signaling. ')
pdnCpIwfIpMgcpIADomainName = MibTableColumn((1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 53, 1, 4, 2, 1, 11), DisplayString()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: pdnCpIwfIpMgcpIADomainName.setStatus('current')
if mibBuilder.loadTexts: pdnCpIwfIpMgcpIADomainName.setDescription("This object contains a text description that lets the user provide a Fully Qualified Domain Name as the domain name portion of the endpoint identifier, as an alternative to using the IP Address of the IAD. This object will be used as the domain name of endpoint identifier if the pdnCpIwfIpMgcpEndPtFormat is set to: 'domainname (3)'; otherwise the value of this object is ignored. ")
pdnCpIwfIpMgcpEndPtFormat = MibTableColumn((1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 53, 1, 4, 2, 1, 12), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("ipaddr", 1), ("bracketandipaddr", 2), ("domainname", 3)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: pdnCpIwfIpMgcpEndPtFormat.setStatus('current')
if mibBuilder.loadTexts: pdnCpIwfIpMgcpEndPtFormat.setDescription('This object specifies the format option to use for the domain portion of the MGCP endpoint identifier. The following options are available: domainipaddr (1): ========== Indicates that IP Address for the IAD shall be used for the domain portion of the endpoint identifier. (e.g., aaln/1@1.2.3.4 - where 1.2.3.4 is the IPAddress) domainbracketipaddr (2): ==================== Indicates that IP Address for the IAD shall be used for the domain portion of of the endpoint identifier enclosed in brackets. (e.g., aaln/1@[1.2.3.4] - where 1.2.3.4 is the IPAddress) domainname (3): ==================== Indicates that the domain name specified in object pdnCpIwfIpMgcpIADomainName shall be used for the domain portion of the endpoint identifier. (e.g., aaln/1@bac1.mytelco.net - where bac1.mytelco.net is the domain name set in the pdnCpIwfIpMgcpIADomainName object) ')
pdnCpIwfIpMgcpRSIPKeepAlive = MibTableColumn((1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 53, 1, 4, 2, 1, 13), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 600))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: pdnCpIwfIpMgcpRSIPKeepAlive.setStatus('current')
if mibBuilder.loadTexts: pdnCpIwfIpMgcpRSIPKeepAlive.setDescription('This object contains the MGCP restart in progress (RSIP) keep alive value. A value of 0 implies the RSIP keep alive timer is disabled. ')
pdnCpIwfIpActiveSoftSwitchChanged = NotificationType((1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 53, 0, 1))
if mibBuilder.loadTexts: pdnCpIwfIpActiveSoftSwitchChanged.setStatus('current')
if mibBuilder.loadTexts: pdnCpIwfIpActiveSoftSwitchChanged.setDescription('This trap/notification will be issued whenever there is a transition in the Active Softswitch. The trap carries the current value of the active softswitch at the time the event was generated. ')
pdnCpIwfIpMIBCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 53, 2, 1))
pdnCpIwfIpMIBGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 53, 2, 2))
pdnCpIwfIpNtfyGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 53, 2, 3))
pdnCpIwfIpMIBCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 53, 2, 1, 1)).setObjects(("PDN-CPIWF-IP-MIB", "pdnCpIwfIpConfigGroup"), ("PDN-CPIWF-IP-MIB", "pdnCpIwfIpApplConfigGroup"), ("PDN-CPIWF-IP-MIB", "pdnCpIwfIpNtfyGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    pdnCpIwfIpMIBCompliance = pdnCpIwfIpMIBCompliance.setStatus('current')
if mibBuilder.loadTexts: pdnCpIwfIpMIBCompliance.setDescription('The compliance statement for SNMP entities that support Customer Premises Interworking Function (CP-IWF) as specified in af-vmoa-0145.000 of the ATM Forum and also these CP-IWFs are used to terminate an IP network. ')
pdnCpIwfIpConfigGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 53, 2, 2, 1)).setObjects(("PDN-CPIWF-IP-MIB", "pdnCpIwfIpChandot1dBasePort"), ("PDN-CPIWF-IP-MIB", "pdnCpIwfIpChanTosDSCP"), ("PDN-CPIWF-IP-MIB", "pdnCpIwfIpAddress"), ("PDN-CPIWF-IP-MIB", "pdnCpIwfIpNetMask"), ("PDN-CPIWF-IP-MIB", "pdnCpIwfIpDefGateway"), ("PDN-CPIWF-IP-MIB", "pdnCpIwfIpActiveSoftswitch"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    pdnCpIwfIpConfigGroup = pdnCpIwfIpConfigGroup.setStatus('current')
if mibBuilder.loadTexts: pdnCpIwfIpConfigGroup.setDescription('Configuration of CpIwf interfaces being used to terminate an IP network.')
pdnCpIwfIpApplConfigGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 53, 2, 2, 2)).setObjects(("PDN-CPIWF-IP-MIB", "pdnCpIwfIpRtpLocalPortBase"), ("PDN-CPIWF-IP-MIB", "pdnCpIwfIpMgcpPortNumber"), ("PDN-CPIWF-IP-MIB", "pdnCpIwfIpMgcpPriAgentName"), ("PDN-CPIWF-IP-MIB", "pdnCpIwfIpMgcpPriAgentIpAddr"), ("PDN-CPIWF-IP-MIB", "pdnCpIwfIpMgcpPriAgentPortNum"), ("PDN-CPIWF-IP-MIB", "pdnCpIwfIpMgcpPriAgentDNSIpAddr"), ("PDN-CPIWF-IP-MIB", "pdnCpIwfIpMgcpSecAgentName"), ("PDN-CPIWF-IP-MIB", "pdnCpIwfIpMgcpSecAgentIpAddr"), ("PDN-CPIWF-IP-MIB", "pdnCpIwfIpMgcpSecAgentPortNum"), ("PDN-CPIWF-IP-MIB", "pdnCpIwfIpMgcpSecAgentDNSIpAddr"), ("PDN-CPIWF-IP-MIB", "pdnCpIwfIpMgcpRFC2833LoopSignal"), ("PDN-CPIWF-IP-MIB", "pdnCpIwfIpMgcpIADomainName"), ("PDN-CPIWF-IP-MIB", "pdnCpIwfIpMgcpEndPtFormat"), ("PDN-CPIWF-IP-MIB", "pdnCpIwfIpMgcpRSIPKeepAlive"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    pdnCpIwfIpApplConfigGroup = pdnCpIwfIpApplConfigGroup.setStatus('current')
if mibBuilder.loadTexts: pdnCpIwfIpApplConfigGroup.setDescription('Configuration of IP Application Voice Call processing protocols that apply to the CPIWFs that terminate an IP network.')
pdnCpIwfIpNtfyGroup = NotificationGroup((1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 53, 2, 3, 1)).setObjects(("PDN-CPIWF-IP-MIB", "pdnCpIwfIpActiveSoftSwitchChanged"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    pdnCpIwfIpNtfyGroup = pdnCpIwfIpNtfyGroup.setStatus('current')
if mibBuilder.loadTexts: pdnCpIwfIpNtfyGroup.setDescription('Notifications related to a CpIwf that terminates an IP Network. ')
mibBuilder.exportSymbols("PDN-CPIWF-IP-MIB", pdnCpIwfIpChanType=pdnCpIwfIpChanType, pdnCpIwfIpChanTable=pdnCpIwfIpChanTable, pdnCpIwfIpEntry=pdnCpIwfIpEntry, VoiceChannelType=VoiceChannelType, pdnCpIwfIpMgcpSecAgentDNSIpAddr=pdnCpIwfIpMgcpSecAgentDNSIpAddr, pdnCpIwfIpNtfyGroups=pdnCpIwfIpNtfyGroups, pdnCpIwfIpDefGateway=pdnCpIwfIpDefGateway, pdnCpIwfIpConfigGroup=pdnCpIwfIpConfigGroup, pdnCpIwfIpMgcpEndPtFormat=pdnCpIwfIpMgcpEndPtFormat, pdnCpIwfIpMgcpPriAgentName=pdnCpIwfIpMgcpPriAgentName, pdnCpIwfIpMIB=pdnCpIwfIpMIB, pdnCpIwfIpRtpLocalPortBase=pdnCpIwfIpRtpLocalPortBase, pdnCpIwfIpChanTosDSCP=pdnCpIwfIpChanTosDSCP, pdnCpIwfIpMgcpIADomainName=pdnCpIwfIpMgcpIADomainName, pdnCpIwfIpApplConfigGroup=pdnCpIwfIpApplConfigGroup, pdnCpIwfIpMgcpRSIPKeepAlive=pdnCpIwfIpMgcpRSIPKeepAlive, pdnCpIwfIpRtpEntry=pdnCpIwfIpRtpEntry, pdnCpIwfIpMIBGroups=pdnCpIwfIpMIBGroups, pdnCpIwfIpMgcpSecAgentName=pdnCpIwfIpMgcpSecAgentName, pdnCpIwfIpRtpTable=pdnCpIwfIpRtpTable, pdnCpIwfIpApplObjects=pdnCpIwfIpApplObjects, pdnCpIwfIpMgcpPriAgentPortNum=pdnCpIwfIpMgcpPriAgentPortNum, pdnCpIwfIpMgcpSecAgentPortNum=pdnCpIwfIpMgcpSecAgentPortNum, pdnCpIwfIpMgcpRFC2833LoopSignal=pdnCpIwfIpMgcpRFC2833LoopSignal, pdnCpIwfIpTable=pdnCpIwfIpTable, pdnCpIwfIpNotifications=pdnCpIwfIpNotifications, pdnCpIwfIpActiveSoftswitch=pdnCpIwfIpActiveSoftswitch, pdnCpIwfIpNetMask=pdnCpIwfIpNetMask, pdnCpIwfIpMIBObjects=pdnCpIwfIpMIBObjects, pdnCpIwfIpTestObjects=pdnCpIwfIpTestObjects, pdnCpIwfIpActiveSoftSwitchChanged=pdnCpIwfIpActiveSoftSwitchChanged, pdnCpIwfIpMgcpTable=pdnCpIwfIpMgcpTable, pdnCpIwfIpChanEntry=pdnCpIwfIpChanEntry, pdnCpIwfIpMgcpPriAgentIpAddr=pdnCpIwfIpMgcpPriAgentIpAddr, pdnCpIwfIpMgcpEntry=pdnCpIwfIpMgcpEntry, pdnCpIwfIpMgcpSecAgentIpAddr=pdnCpIwfIpMgcpSecAgentIpAddr, pdnCpIwfIpMIBCompliance=pdnCpIwfIpMIBCompliance, pdnCpIwfIpChandot1dBasePort=pdnCpIwfIpChandot1dBasePort, pdnCpIwfIpMgcpPriAgentDNSIpAddr=pdnCpIwfIpMgcpPriAgentDNSIpAddr, PYSNMP_MODULE_ID=pdnCpIwfIpMIB, pdnCpIwfIpMIBConformance=pdnCpIwfIpMIBConformance, pdnCpIwfIpConfigObjects=pdnCpIwfIpConfigObjects, pdnCpIwfIpStatsObjects=pdnCpIwfIpStatsObjects, pdnCpIwfIpNtfyGroup=pdnCpIwfIpNtfyGroup, pdnCpIwfIpAddress=pdnCpIwfIpAddress, pdnCpIwfIpMgcpPortNumber=pdnCpIwfIpMgcpPortNumber, pdnCpIwfIpMIBCompliances=pdnCpIwfIpMIBCompliances)