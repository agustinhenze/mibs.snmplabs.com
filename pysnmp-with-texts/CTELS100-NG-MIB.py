#
# PySNMP MIB module CTELS100-NG-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/CTELS100-NG-MIB
# Produced by pysmi-0.3.4 at Wed May  1 12:29:12 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsUnion, SingleValueConstraint, ValueRangeConstraint, ValueSizeConstraint, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "SingleValueConstraint", "ValueRangeConstraint", "ValueSizeConstraint", "ConstraintsIntersection")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
ModuleIdentity, iso, mgmt, Counter64, Unsigned32, Integer32, Counter32, Gauge32, MibIdentifier, enterprises, TimeTicks, NotificationType, IpAddress, Bits, MibScalar, MibTable, MibTableRow, MibTableColumn, ObjectIdentity = mibBuilder.importSymbols("SNMPv2-SMI", "ModuleIdentity", "iso", "mgmt", "Counter64", "Unsigned32", "Integer32", "Counter32", "Gauge32", "MibIdentifier", "enterprises", "TimeTicks", "NotificationType", "IpAddress", "Bits", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "ObjectIdentity")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
mib_2 = MibIdentifier((1, 3, 6, 1, 2, 1)).setLabel("mib-2")
cabletron = MibIdentifier((1, 3, 6, 1, 4, 1, 52))
els100 = MibIdentifier((1, 3, 6, 1, 4, 1, 52, 1011))
els100SystemConfig = MibIdentifier((1, 3, 6, 1, 4, 1, 52, 1011, 1))
els100Switch = MibIdentifier((1, 3, 6, 1, 4, 1, 52, 1011, 3))
els100SysSerialno = MibScalar((1, 3, 6, 1, 4, 1, 52, 1011, 1, 1), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 255))).setMaxAccess("readonly")
if mibBuilder.loadTexts: els100SysSerialno.setStatus('mandatory')
if mibBuilder.loadTexts: els100SysSerialno.setDescription('The serial number of the system.')
els100SysTftpIPAddress = MibScalar((1, 3, 6, 1, 4, 1, 52, 1011, 1, 2), IpAddress()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: els100SysTftpIPAddress.setStatus('mandatory')
if mibBuilder.loadTexts: els100SysTftpIPAddress.setDescription('The IP address of the TFTP server from which a software download is to be initiated. This variable must be set before a TFTP download can be started with the els100SysTftpStartDownload variable.')
els100SysTftpFilename = MibScalar((1, 3, 6, 1, 4, 1, 52, 1011, 1, 3), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 255))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: els100SysTftpFilename.setStatus('mandatory')
if mibBuilder.loadTexts: els100SysTftpFilename.setDescription('The name of the software upgrade file residing on the TFTP server. Path information must be included in the file name. This variable must be set before a TFTP download can be started with the els100SysTftpStartDownload variable.')
els100SysPowerupCount = MibScalar((1, 3, 6, 1, 4, 1, 52, 1011, 1, 4), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: els100SysPowerupCount.setStatus('mandatory')
if mibBuilder.loadTexts: els100SysPowerupCount.setDescription('The total number of times the system has powered up since it was shipped from the factory.')
els100SysBrcastCutoffRate = MibScalar((1, 3, 6, 1, 4, 1, 52, 1011, 1, 5), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: els100SysBrcastCutoffRate.setStatus('mandatory')
if mibBuilder.loadTexts: els100SysBrcastCutoffRate.setDescription('The Broadcast Cutoff Rate of the switch allowing for the control of broadcast storms. The value of this variable sets a per second rate. If the broadcast and unknown destination address frames being forwarded through the system surpass this rate, they are dropped. Valid values for this parameter are in the range (100..500000).')
els100SysGatewayIPAddress = MibScalar((1, 3, 6, 1, 4, 1, 52, 1011, 1, 6), IpAddress()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: els100SysGatewayIPAddress.setStatus('mandatory')
if mibBuilder.loadTexts: els100SysGatewayIPAddress.setDescription('The IP address of the next hop router (gateway) to which frames destined for an IP subnet different than what the system resides are sent.')
els100SysTftpStartDownload = MibScalar((1, 3, 6, 1, 4, 1, 52, 1011, 1, 7), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("download", 1), ("noDownload", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: els100SysTftpStartDownload.setStatus('mandatory')
if mibBuilder.loadTexts: els100SysTftpStartDownload.setDescription('Start a TFTP download. A SET of this variable with the value download (1) initiates a TFTP download to upgrade the system software. The variables els100SysTftpIPAddress and els100SysTftpFilename must be configured before a download can begin. A GET of this variable will always return the value noDownload (2).')
els100SysBootPDhcpEnable = MibScalar((1, 3, 6, 1, 4, 1, 52, 1011, 1, 8), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("disable", 1), ("enable", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: els100SysBootPDhcpEnable.setStatus('mandatory')
if mibBuilder.loadTexts: els100SysBootPDhcpEnable.setDescription("Enable or disable the operation of the BootP and DHCP protocols on the system. These protocols are used for automatically configuring the system's IP address information if a properly configured BootP and/or DHCP server exists on the network.")
els100SysReset = MibScalar((1, 3, 6, 1, 4, 1, 52, 1011, 1, 10), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("noReset", 1), ("reset", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: els100SysReset.setStatus('mandatory')
if mibBuilder.loadTexts: els100SysReset.setDescription('Initiate a software reset of the system.')
els100SysSyslogServer = MibScalar((1, 3, 6, 1, 4, 1, 52, 1011, 1, 11), IpAddress()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: els100SysSyslogServer.setStatus('mandatory')
if mibBuilder.loadTexts: els100SysSyslogServer.setDescription('The IP address of the Syslog Server.')
els100SysLowestSyslogSeverity = MibScalar((1, 3, 6, 1, 4, 1, 52, 1011, 1, 12), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3, 4, 5, 6, 7))).clone(namedValues=NamedValues(("emergency", 0), ("alert", 1), ("critical", 2), ("error", 3), ("warning", 4), ("notice", 5), ("info", 6), ("debug", 7)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: els100SysLowestSyslogSeverity.setStatus('mandatory')
if mibBuilder.loadTexts: els100SysLowestSyslogSeverity.setDescription('The Lowest Syslog Severity Level. All logs with the same or higher severity will be delivered. Note: higher severity has lower number.')
els100SysComPortEnable = MibScalar((1, 3, 6, 1, 4, 1, 52, 1011, 1, 13), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("disabled", 1), ("enabled", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: els100SysComPortEnable.setStatus('mandatory')
if mibBuilder.loadTexts: els100SysComPortEnable.setDescription('The administrative state of the Com Port.')
els100SysBoardID = MibScalar((1, 3, 6, 1, 4, 1, 52, 1011, 1, 14), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: els100SysBoardID.setStatus('mandatory')
if mibBuilder.loadTexts: els100SysBoardID.setDescription('The system board ID.')
els100PortTable = MibTable((1, 3, 6, 1, 4, 1, 52, 1011, 2), )
if mibBuilder.loadTexts: els100PortTable.setStatus('mandatory')
if mibBuilder.loadTexts: els100PortTable.setDescription('The port table.')
els100PortEntry = MibTableRow((1, 3, 6, 1, 4, 1, 52, 1011, 2, 1), ).setIndexNames((0, "CTELS100-NG-MIB", "els100Port"))
if mibBuilder.loadTexts: els100PortEntry.setStatus('mandatory')
if mibBuilder.loadTexts: els100PortEntry.setDescription('An entry in the port table.')
els100Port = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 1011, 2, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: els100Port.setStatus('mandatory')
if mibBuilder.loadTexts: els100Port.setDescription('The number of the port, from 1 to the number of ports on the system.')
els100PortStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 1011, 2, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("up", 1), ("down", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: els100PortStatus.setStatus('mandatory')
if mibBuilder.loadTexts: els100PortStatus.setDescription('The connection (link) status of the port, either up (linked) or down (not linked).')
els100PortDuplexStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 1011, 2, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("half", 1), ("full", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: els100PortDuplexStatus.setStatus('mandatory')
if mibBuilder.loadTexts: els100PortDuplexStatus.setDescription('The duplex status of the port, either half duplex or full duplex.')
els100PortForwardedFrames = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 1011, 2, 1, 4), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: els100PortForwardedFrames.setStatus('mandatory')
if mibBuilder.loadTexts: els100PortForwardedFrames.setDescription('The number of frames received on the port and forwarded to another port on the system module for processing.')
els100PortRcvdLocalFrames = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 1011, 2, 1, 5), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: els100PortRcvdLocalFrames.setStatus('mandatory')
if mibBuilder.loadTexts: els100PortRcvdLocalFrames.setDescription('The number of frames received where the destination is on the port.')
els100PortName = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 1011, 2, 1, 6), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 60))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: els100PortName.setStatus('mandatory')
if mibBuilder.loadTexts: els100PortName.setDescription('A descriptive string of up to 60 characters used by the network administrator to name the port.')
els100PortEnable = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 1011, 2, 1, 7), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("disable", 1), ("enable", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: els100PortEnable.setStatus('mandatory')
if mibBuilder.loadTexts: els100PortEnable.setDescription('The enable status of the port, either enable or disable.')
els100PortSpeed = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 1011, 2, 1, 8), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("tenMbps", 1), ("oneHundredMbps", 2), ("oneThousandMbps", 3)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: els100PortSpeed.setStatus('mandatory')
if mibBuilder.loadTexts: els100PortSpeed.setDescription('The speed the port is operating at: 10Mbps, or 100Mbps, or 1000Mbps.')
els100PortAutonegEnable = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 1011, 2, 1, 9), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("disable", 1), ("enable", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: els100PortAutonegEnable.setStatus('mandatory')
if mibBuilder.loadTexts: els100PortAutonegEnable.setDescription('The auto-negotiation status of the port, either enable or disable. When in the enable (2) state, the port will automatically configure its duplex and speed operation.')
els100PortFlowControlEnable = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 1011, 2, 1, 10), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("disable", 1), ("enable", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: els100PortFlowControlEnable.setStatus('mandatory')
if mibBuilder.loadTexts: els100PortFlowControlEnable.setDescription('The state of flow control operation of the port, either enable or disable.')
els100PortType = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 1011, 2, 1, 11), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 8, 9, 10))).clone(namedValues=NamedValues(("unknown", 1), ("ieee10BaseT", 2), ("ieee100BaseTx", 3), ("ieee100BaseFx-MM", 4), ("ieee100BaseFx-SM", 5), ("ieee1000BaseCx", 6), ("ieee1000BaseLx", 7), ("ieee1000BaseSx", 8), ("ieee1000BaseT", 9), ("ieee1000BaseX", 10)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: els100PortType.setStatus('mandatory')
if mibBuilder.loadTexts: els100PortType.setDescription('Port physical interface type.')
els100SwitchIPAddress = MibScalar((1, 3, 6, 1, 4, 1, 52, 1011, 3, 1), IpAddress()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: els100SwitchIPAddress.setStatus('mandatory')
if mibBuilder.loadTexts: els100SwitchIPAddress.setDescription('The IP address of the system.')
els100SwitchSubnetMask = MibScalar((1, 3, 6, 1, 4, 1, 52, 1011, 3, 2), IpAddress()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: els100SwitchSubnetMask.setStatus('mandatory')
if mibBuilder.loadTexts: els100SwitchSubnetMask.setDescription('The subnet mask associated with the IP address of the system.')
els100ActiveAgingTime = MibScalar((1, 3, 6, 1, 4, 1, 52, 1011, 3, 3), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: els100ActiveAgingTime.setStatus('mandatory')
if mibBuilder.loadTexts: els100ActiveAgingTime.setDescription('The aging time of entries in the MAC address forwarding table of the system.')
els100SwitchSTPStatus = MibScalar((1, 3, 6, 1, 4, 1, 52, 1011, 3, 5), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("on", 1), ("off", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: els100SwitchSTPStatus.setStatus('mandatory')
if mibBuilder.loadTexts: els100SwitchSTPStatus.setDescription('The Spanning Tree status of the system, enter on or off.')
els100SwitchManager = MibIdentifier((1, 3, 6, 1, 4, 1, 52, 1011, 3, 6))
els100SwitchTrapRcvr1 = MibScalar((1, 3, 6, 1, 4, 1, 52, 1011, 3, 6, 1), IpAddress()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: els100SwitchTrapRcvr1.setStatus('mandatory')
if mibBuilder.loadTexts: els100SwitchTrapRcvr1.setDescription('The IP address of the first SNMP manager to which traps from the system are directed.')
els100SwitchTrapCommunity1 = MibScalar((1, 3, 6, 1, 4, 1, 52, 1011, 3, 6, 2), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 60))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: els100SwitchTrapCommunity1.setStatus('mandatory')
if mibBuilder.loadTexts: els100SwitchTrapCommunity1.setDescription('The community name of the first SNMP manager to which traps from the system are directed.')
els100SwitchTrapRcvr2 = MibScalar((1, 3, 6, 1, 4, 1, 52, 1011, 3, 6, 3), IpAddress()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: els100SwitchTrapRcvr2.setStatus('mandatory')
if mibBuilder.loadTexts: els100SwitchTrapRcvr2.setDescription('The IP address of the second SNMP manager to which traps from the system are directed.')
els100SwitchTrapCommunity2 = MibScalar((1, 3, 6, 1, 4, 1, 52, 1011, 3, 6, 4), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 60))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: els100SwitchTrapCommunity2.setStatus('mandatory')
if mibBuilder.loadTexts: els100SwitchTrapCommunity2.setDescription('The community name of the second SNMP manager to which traps from the system are directed.')
els100SwitchTrapRcvr3 = MibScalar((1, 3, 6, 1, 4, 1, 52, 1011, 3, 6, 5), IpAddress()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: els100SwitchTrapRcvr3.setStatus('mandatory')
if mibBuilder.loadTexts: els100SwitchTrapRcvr3.setDescription('The IP address of the third SNMP manager to which traps from the system are directed.')
els100SwitchTrapCommunity3 = MibScalar((1, 3, 6, 1, 4, 1, 52, 1011, 3, 6, 6), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 60))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: els100SwitchTrapCommunity3.setStatus('mandatory')
if mibBuilder.loadTexts: els100SwitchTrapCommunity3.setDescription('The community name of the third SNMP manager to which traps from the system are directed.')
els100SwitchTrapRcvr4 = MibScalar((1, 3, 6, 1, 4, 1, 52, 1011, 3, 6, 7), IpAddress()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: els100SwitchTrapRcvr4.setStatus('mandatory')
if mibBuilder.loadTexts: els100SwitchTrapRcvr4.setDescription('The IP address of the fourth SNMP manager to which traps from the system are directed.')
els100SwitchTrapCommunity4 = MibScalar((1, 3, 6, 1, 4, 1, 52, 1011, 3, 6, 8), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 60))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: els100SwitchTrapCommunity4.setStatus('mandatory')
if mibBuilder.loadTexts: els100SwitchTrapCommunity4.setDescription('The community name of the fourth SNMP manager to which traps from the system are directed.')
els100SwitchPortMirroringStatus = MibScalar((1, 3, 6, 1, 4, 1, 52, 1011, 3, 7), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("disable", 1), ("enable", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: els100SwitchPortMirroringStatus.setStatus('mandatory')
if mibBuilder.loadTexts: els100SwitchPortMirroringStatus.setDescription('The Port Mirroring status of the system, either disable or enable.')
els100SwitchMirroredPort = MibScalar((1, 3, 6, 1, 4, 1, 52, 1011, 3, 8), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: els100SwitchMirroredPort.setStatus('mandatory')
if mibBuilder.loadTexts: els100SwitchMirroredPort.setDescription('The port that is being mirrored - the source.')
els100SwitchMirroringPort = MibScalar((1, 3, 6, 1, 4, 1, 52, 1011, 3, 9), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: els100SwitchMirroringPort.setStatus('mandatory')
if mibBuilder.loadTexts: els100SwitchMirroringPort.setDescription('The port that is mirroring - the destination.')
els100SwitchXmitMirrorEnable = MibScalar((1, 3, 6, 1, 4, 1, 52, 1011, 3, 10), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("disable", 1), ("enable", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: els100SwitchXmitMirrorEnable.setStatus('mandatory')
if mibBuilder.loadTexts: els100SwitchXmitMirrorEnable.setDescription('Enable or disable the mirroring of transmitted traffic out the mirrored port to the mirroring port.')
els100SwitchRcvMirrorEnable = MibScalar((1, 3, 6, 1, 4, 1, 52, 1011, 3, 11), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("disable", 1), ("enable", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: els100SwitchRcvMirrorEnable.setStatus('mandatory')
if mibBuilder.loadTexts: els100SwitchRcvMirrorEnable.setDescription('Enable or disable the mirroring of received traffic into the mirrored port to the mirroring port.')
els100SwitchVlanEnable = MibScalar((1, 3, 6, 1, 4, 1, 52, 1011, 3, 12), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("disable", 1), ("enable", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: els100SwitchVlanEnable.setStatus('mandatory')
if mibBuilder.loadTexts: els100SwitchVlanEnable.setDescription('Globally enable or disable the VLAN operation of the system.')
els100SwitchVlanConfigTable = MibTable((1, 3, 6, 1, 4, 1, 52, 1011, 3, 13), )
if mibBuilder.loadTexts: els100SwitchVlanConfigTable.setStatus('mandatory')
if mibBuilder.loadTexts: els100SwitchVlanConfigTable.setDescription('The VLAN configuration table.')
els100SwitchVlanEntry = MibTableRow((1, 3, 6, 1, 4, 1, 52, 1011, 3, 13, 1), ).setIndexNames((0, "CTELS100-NG-MIB", "els100SwitchVlanId"))
if mibBuilder.loadTexts: els100SwitchVlanEntry.setStatus('mandatory')
if mibBuilder.loadTexts: els100SwitchVlanEntry.setDescription('An entry in the VLAN configuration table.')
els100SwitchVlanId = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 1011, 3, 13, 1, 1), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: els100SwitchVlanId.setStatus('mandatory')
if mibBuilder.loadTexts: els100SwitchVlanId.setDescription("The number of the VLAN, from 1 to the number of VLAN's supported on the system.")
els100SwitchVlanName = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 1011, 3, 13, 1, 2), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 60))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: els100SwitchVlanName.setStatus('mandatory')
if mibBuilder.loadTexts: els100SwitchVlanName.setDescription('A descriptive string of up to 60 characters used by the network administrator to name the VLAN.')
els100SwitchVlanPorts = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 1011, 3, 13, 1, 3), OctetString()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: els100SwitchVlanPorts.setStatus('mandatory')
if mibBuilder.loadTexts: els100SwitchVlanPorts.setDescription("The set of ports in the VLAN. For systems supporting tagged VLAN's, these are the ports to which packets on the VLAN are sent untagged. Each octet within the value of this object specifies a set of eight ports, with the first octet specifying ports 1 through 8, the second octet specifying ports 9 through 16, etc. Within each octet, the most significant bit represents the lowest numbered port, and the least significant bit represents the highest numbered port. Thus each port of the system is represented by a single bit within the value of this object. If that bit has a value of '1' then that port is included in the VLAN; the port is not included if its bit has a value of '0'.")
els100SwitchVlanEgressPorts = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 1011, 3, 13, 1, 4), OctetString()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: els100SwitchVlanEgressPorts.setStatus('mandatory')
if mibBuilder.loadTexts: els100SwitchVlanEgressPorts.setDescription("The set of ports defined to be on other VLAN's to which tagged packets destined for this specific VLAN should also be sent. Thus, this variable defines ports on the system that reach stations downstream which are on this VLAN and to which traffic may be forwarded. Each octet within the value of this object specifies a set of eight ports, with the first octet specifying ports 1 through 8, the second octet specifying ports 9 through 16, etc. Within each octet, the most significant bit represents the lowest numbered port, and the least significant bit represents the highest numbered port. Thus each port of the system is represented by a single bit within the value of this object. If that bit has a value of '1' then that port is included in the VLAN; the port is not included if its bit has a value of '0'.")
els100SwitchVlanStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 1011, 3, 13, 1, 5), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enable", 1), ("disable", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: els100SwitchVlanStatus.setStatus('mandatory')
if mibBuilder.loadTexts: els100SwitchVlanStatus.setDescription('Control variable used to enable or disable the operation of the associated VLAN in the system.')
els100SwitchVlanPortTable = MibTable((1, 3, 6, 1, 4, 1, 52, 1011, 3, 14), )
if mibBuilder.loadTexts: els100SwitchVlanPortTable.setStatus('mandatory')
if mibBuilder.loadTexts: els100SwitchVlanPortTable.setDescription('The VLAN port configuration table.')
els100SwitchVlanPortEntry = MibTableRow((1, 3, 6, 1, 4, 1, 52, 1011, 3, 14, 1), ).setIndexNames((0, "CTELS100-NG-MIB", "els100SwitchVlanPortId"))
if mibBuilder.loadTexts: els100SwitchVlanPortEntry.setStatus('mandatory')
if mibBuilder.loadTexts: els100SwitchVlanPortEntry.setDescription('An entry in the VLAN port configuration table.')
els100SwitchVlanPortId = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 1011, 3, 14, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 63))).setMaxAccess("readonly")
if mibBuilder.loadTexts: els100SwitchVlanPortId.setStatus('mandatory')
if mibBuilder.loadTexts: els100SwitchVlanPortId.setDescription('The number of the port, from 1 to number of ports in the system.')
els100SwitchVlanPvid = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 1011, 3, 14, 1, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 4095))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: els100SwitchVlanPvid.setStatus('mandatory')
if mibBuilder.loadTexts: els100SwitchVlanPvid.setDescription("The port's VLAN ID. For tagged VLAN's, this variable defines a 12 bit port VLAN ID (PVID) used as the identifier of the VLAN in the packet tag.")
els100SwitchVlanPortType = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 1011, 3, 14, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("hybrid", 1), ("access", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: els100SwitchVlanPortType.setStatus('mandatory')
if mibBuilder.loadTexts: els100SwitchVlanPortType.setDescription("For tagged VLAN's, the VLAN port type, either hybrid or access. Hybrid ports allow both tagged and untagged packets to enter the switch. Access ports only accept untagged packets.")
els100SwitchPriorityEnable = MibScalar((1, 3, 6, 1, 4, 1, 52, 1011, 3, 15), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("disable", 1), ("enable", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: els100SwitchPriorityEnable.setStatus('mandatory')
if mibBuilder.loadTexts: els100SwitchPriorityEnable.setDescription('Globally enable or disable the Class of Service traffic priority mechanism for the system.')
els100SwitchPriorityThreshold = MibScalar((1, 3, 6, 1, 4, 1, 52, 1011, 3, 16), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: els100SwitchPriorityThreshold.setStatus('mandatory')
if mibBuilder.loadTexts: els100SwitchPriorityThreshold.setDescription('The global priority threshold level for the system at which VLAN tagged frames entering the associated port are assigned a high priority. This variable can have a value from (0...7). Traffic with a priority level equal to or above this value are high priority. Traffic with a priority level below this value are normal priority.')
els100SwitchPriorityPortTable = MibTable((1, 3, 6, 1, 4, 1, 52, 1011, 3, 17), )
if mibBuilder.loadTexts: els100SwitchPriorityPortTable.setStatus('mandatory')
if mibBuilder.loadTexts: els100SwitchPriorityPortTable.setDescription('The priority port table.')
els100SwitchPriorityPortEntry = MibTableRow((1, 3, 6, 1, 4, 1, 52, 1011, 3, 17, 1), ).setIndexNames((0, "CTELS100-NG-MIB", "els100SwitchPriorityPortId"))
if mibBuilder.loadTexts: els100SwitchPriorityPortEntry.setStatus('mandatory')
if mibBuilder.loadTexts: els100SwitchPriorityPortEntry.setDescription('An entry in the port priority table.')
els100SwitchPriorityPortId = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 1011, 3, 17, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: els100SwitchPriorityPortId.setStatus('mandatory')
if mibBuilder.loadTexts: els100SwitchPriorityPortId.setDescription('The port number, from 1 to number of ports in the system.')
els100SwitchPriorityDefault = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 1011, 3, 17, 1, 2), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: els100SwitchPriorityDefault.setStatus('mandatory')
if mibBuilder.loadTexts: els100SwitchPriorityDefault.setDescription('The port priority level assigned to untagged traffic entering the associated port. This variable can have a value in the range (0...7). This value is compared to the value of the els100SwitchPriorityThreshold variable to determine if the traffic on the port is high or normal.')
els100SwitchSpanningTreeStandby = MibScalar((1, 3, 6, 1, 4, 1, 52, 1011, 3, 18), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("disable", 1), ("enable", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: els100SwitchSpanningTreeStandby.setStatus('mandatory')
if mibBuilder.loadTexts: els100SwitchSpanningTreeStandby.setDescription('Globally enable or disable Spanning Tree Standby. If set to disable, every port will instanly enter forwarding mode after link up')
mibBuilder.exportSymbols("CTELS100-NG-MIB", els100PortName=els100PortName, els100SwitchMirroringPort=els100SwitchMirroringPort, els100SwitchVlanPvid=els100SwitchVlanPvid, els100=els100, els100SysGatewayIPAddress=els100SysGatewayIPAddress, els100SysLowestSyslogSeverity=els100SysLowestSyslogSeverity, els100PortType=els100PortType, els100SwitchMirroredPort=els100SwitchMirroredPort, els100SwitchSubnetMask=els100SwitchSubnetMask, els100SysReset=els100SysReset, els100SwitchPriorityPortId=els100SwitchPriorityPortId, els100SysTftpStartDownload=els100SysTftpStartDownload, els100PortEnable=els100PortEnable, els100SwitchPriorityThreshold=els100SwitchPriorityThreshold, els100SwitchSTPStatus=els100SwitchSTPStatus, els100SysTftpFilename=els100SysTftpFilename, els100SwitchPortMirroringStatus=els100SwitchPortMirroringStatus, els100SwitchTrapRcvr3=els100SwitchTrapRcvr3, els100SwitchPriorityEnable=els100SwitchPriorityEnable, els100SwitchTrapRcvr1=els100SwitchTrapRcvr1, els100SwitchVlanEntry=els100SwitchVlanEntry, els100SwitchTrapRcvr4=els100SwitchTrapRcvr4, els100PortEntry=els100PortEntry, els100SwitchVlanId=els100SwitchVlanId, els100PortStatus=els100PortStatus, els100SysBrcastCutoffRate=els100SysBrcastCutoffRate, els100PortFlowControlEnable=els100PortFlowControlEnable, els100SystemConfig=els100SystemConfig, els100SwitchXmitMirrorEnable=els100SwitchXmitMirrorEnable, els100SwitchRcvMirrorEnable=els100SwitchRcvMirrorEnable, mib_2=mib_2, els100SwitchVlanPortType=els100SwitchVlanPortType, els100SwitchVlanPortTable=els100SwitchVlanPortTable, els100PortSpeed=els100PortSpeed, els100SwitchSpanningTreeStandby=els100SwitchSpanningTreeStandby, els100SwitchVlanPortEntry=els100SwitchVlanPortEntry, els100PortDuplexStatus=els100PortDuplexStatus, els100PortAutonegEnable=els100PortAutonegEnable, els100SwitchTrapCommunity3=els100SwitchTrapCommunity3, els100SysPowerupCount=els100SysPowerupCount, els100SwitchVlanConfigTable=els100SwitchVlanConfigTable, els100SwitchVlanStatus=els100SwitchVlanStatus, els100PortRcvdLocalFrames=els100PortRcvdLocalFrames, cabletron=cabletron, els100SwitchVlanPorts=els100SwitchVlanPorts, els100SysSyslogServer=els100SysSyslogServer, els100Port=els100Port, els100SwitchTrapCommunity4=els100SwitchTrapCommunity4, els100SysBootPDhcpEnable=els100SysBootPDhcpEnable, els100SysBoardID=els100SysBoardID, els100SwitchManager=els100SwitchManager, els100PortTable=els100PortTable, els100SwitchPriorityPortTable=els100SwitchPriorityPortTable, els100SwitchTrapCommunity1=els100SwitchTrapCommunity1, els100SwitchTrapCommunity2=els100SwitchTrapCommunity2, els100SwitchPriorityPortEntry=els100SwitchPriorityPortEntry, els100SwitchVlanEnable=els100SwitchVlanEnable, els100SwitchTrapRcvr2=els100SwitchTrapRcvr2, els100SysTftpIPAddress=els100SysTftpIPAddress, els100SwitchPriorityDefault=els100SwitchPriorityDefault, els100Switch=els100Switch, els100PortForwardedFrames=els100PortForwardedFrames, els100SysComPortEnable=els100SysComPortEnable, els100SwitchIPAddress=els100SwitchIPAddress, els100ActiveAgingTime=els100ActiveAgingTime, els100SwitchVlanName=els100SwitchVlanName, els100SwitchVlanEgressPorts=els100SwitchVlanEgressPorts, els100SysSerialno=els100SysSerialno, els100SwitchVlanPortId=els100SwitchVlanPortId)