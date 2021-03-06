#
# PySNMP MIB module CENTILLION-LECS-MPOA-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/CENTILLION-LECS-MPOA-MIB
# Produced by pysmi-0.3.4 at Wed May  1 11:47:51 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
ObjectIdentifier, Integer, OctetString = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "Integer", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsUnion, ValueRangeConstraint, SingleValueConstraint, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsUnion", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsIntersection")
atmLane, = mibBuilder.importSymbols("CENTILLION-ROOT-MIB", "atmLane")
lecsConfIndex, = mibBuilder.importSymbols("LAN-EMULATION-ELAN-MIB", "lecsConfIndex")
AtmConfigAddr, MpsIndex, MpcIndex, InternetworkAddrType = mibBuilder.importSymbols("MPOA-MIB", "AtmConfigAddr", "MpsIndex", "MpcIndex", "InternetworkAddrType")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
Bits, Gauge32, ObjectIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, ModuleIdentity, MibIdentifier, Counter64, iso, Integer32, IpAddress, Unsigned32, NotificationType, Counter32, TimeTicks = mibBuilder.importSymbols("SNMPv2-SMI", "Bits", "Gauge32", "ObjectIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "ModuleIdentity", "MibIdentifier", "Counter64", "iso", "Integer32", "IpAddress", "Unsigned32", "NotificationType", "Counter32", "TimeTicks")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
RowStatus, TruthValue = mibBuilder.importSymbols("SNMPv2-TC-v1", "RowStatus", "TruthValue")
cnLecsMpoaGroup = MibIdentifier((1, 3, 6, 1, 4, 1, 930, 2, 2, 3, 6))
cnLecsMpoaMpcTable = MibTable((1, 3, 6, 1, 4, 1, 930, 2, 2, 3, 6, 1), )
if mibBuilder.loadTexts: cnLecsMpoaMpcTable.setStatus('mandatory')
if mibBuilder.loadTexts: cnLecsMpoaMpcTable.setDescription('The Bay Networks proprietary LECS MPC Table. This table contains configuration information for all LECS Mpoa Mpcs this agent manages.')
cnLecsMpoaMpcEntry = MibTableRow((1, 3, 6, 1, 4, 1, 930, 2, 2, 3, 6, 1, 1), ).setIndexNames((0, "LAN-EMULATION-ELAN-MIB", "lecsConfIndex"), (0, "CENTILLION-LECS-MPOA-MIB", "cnLecsMpoaMpcIndex"))
if mibBuilder.loadTexts: cnLecsMpoaMpcEntry.setStatus('mandatory')
if mibBuilder.loadTexts: cnLecsMpoaMpcEntry.setDescription('Each entry contains LECS MPC information for all LECS this agent manages.')
cnLecsMpoaMpcIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 930, 2, 2, 3, 6, 1, 1, 1), MpcIndex()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cnLecsMpoaMpcIndex.setStatus('mandatory')
if mibBuilder.loadTexts: cnLecsMpoaMpcIndex.setDescription('A value which uniquely identifies this conceptual row in the cnLecsMpoaMpcTable.')
cnLecsMpoaMpcRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 930, 2, 2, 3, 6, 1, 1, 2), RowStatus()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cnLecsMpoaMpcRowStatus.setStatus('mandatory')
if mibBuilder.loadTexts: cnLecsMpoaMpcRowStatus.setDescription('This object allows creation and deletion of Lecs MPOA Clients. Within each conceptual cnLecsMpoaMpcTable row, writable objects may be modified, regardless of the value of cnLecsMpoaMpcRowStatus.')
cnLecsMpoaMpcCtrlAtmAddr = MibTableColumn((1, 3, 6, 1, 4, 1, 930, 2, 2, 3, 6, 1, 1, 3), AtmConfigAddr()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cnLecsMpoaMpcCtrlAtmAddr.setStatus('mandatory')
if mibBuilder.loadTexts: cnLecsMpoaMpcCtrlAtmAddr.setDescription("The MPC's Control ATM Address. There exists one Control ATM Address per MPC, therefore, the value of this entry is unique within the table. The control ATM Address is the address which is used by the MPC in its requests to the MPS. The value of this object should not change, once created.")
cnLecsMpoaMpcSCSetupFrameCount = MibTableColumn((1, 3, 6, 1, 4, 1, 930, 2, 2, 3, 6, 1, 1, 4), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 65535)).clone(10)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cnLecsMpoaMpcSCSetupFrameCount.setStatus('mandatory')
if mibBuilder.loadTexts: cnLecsMpoaMpcSCSetupFrameCount.setDescription('This represents the Short-cut setup frame count parameter. This value is frames measured over mpcSCFrameTime seconds. Flow detection is protocol independent. i.e. all network layers lecsMpcProtocolEntries for this MPC share the flow rate specification. A value of 1 causes all flows to initiate resolution/shortcut. process.')
cnLecsMpoaMpcSCSetupFrameTime = MibTableColumn((1, 3, 6, 1, 4, 1, 930, 2, 2, 3, 6, 1, 1, 5), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 60)).clone(1)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cnLecsMpoaMpcSCSetupFrameTime.setStatus('mandatory')
if mibBuilder.loadTexts: cnLecsMpoaMpcSCSetupFrameTime.setDescription('Short-cut setup frame time, in seconds.')
cnLecsMpoaMpcInitialRetryTime = MibTableColumn((1, 3, 6, 1, 4, 1, 930, 2, 2, 3, 6, 1, 1, 6), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 300)).clone(5)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cnLecsMpoaMpcInitialRetryTime.setStatus('mandatory')
if mibBuilder.loadTexts: cnLecsMpoaMpcInitialRetryTime.setDescription('This is the initial value for the retry time out period used for timing out MPOA Resolution Requests in seconds. Retry time consists of this initial time-out and a retry muliplier. If a response is not received, then another request is sent with a timeout of retry time * retry time maximum seconds, or until cnLecsMpoaMpcRetryTimeMaximum.')
cnLecsMpoaMpcRetryTimeMaximum = MibTableColumn((1, 3, 6, 1, 4, 1, 930, 2, 2, 3, 6, 1, 1, 7), Integer32().subtype(subtypeSpec=ValueRangeConstraint(10, 300)).clone(40)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cnLecsMpoaMpcRetryTimeMaximum.setReference('Multiprotocol Over ATM. AF-MPOA-0087.000. Section 4.3 MPOA Retry Mechanism')
if mibBuilder.loadTexts: cnLecsMpoaMpcRetryTimeMaximum.setStatus('mandatory')
if mibBuilder.loadTexts: cnLecsMpoaMpcRetryTimeMaximum.setDescription('Cumulative max value for Retry Time. Retries are attempted at intervals determined by the algorithm descrived in the definition of cnLecsMpoaMpcInitalRetryTime.')
cnLecsMpoaMpcHoldDownTime = MibTableColumn((1, 3, 6, 1, 4, 1, 930, 2, 2, 3, 6, 1, 1, 8), Integer32().subtype(subtypeSpec=ValueRangeConstraint(30, 1200)).clone(160)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cnLecsMpoaMpcHoldDownTime.setReference('Multiprotocol Over ATM. AF-MPOA-0087.000. Section 4.1.2.1 MPC Parameters')
if mibBuilder.loadTexts: cnLecsMpoaMpcHoldDownTime.setStatus('mandatory')
if mibBuilder.loadTexts: cnLecsMpoaMpcHoldDownTime.setDescription('Hold Down Time Minimum time to wait before reinitiating a failed resolution attempt. Default is cnLecsMpoaMpcRetryTimeMaximum * 4.')
cnLecsMpoaMpcDefaultTLV = MibTableColumn((1, 3, 6, 1, 4, 1, 930, 2, 2, 3, 6, 1, 1, 9), TruthValue().clone('false')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cnLecsMpoaMpcDefaultTLV.setStatus('mandatory')
if mibBuilder.loadTexts: cnLecsMpoaMpcDefaultTLV.setDescription('Indicates whether this CnLecsMpoaMpcEntry contains the default TLV settings. Only one entry in the table can have the default setttings.')
cnLecsMpoaMpsTable = MibTable((1, 3, 6, 1, 4, 1, 930, 2, 2, 3, 6, 2), )
if mibBuilder.loadTexts: cnLecsMpoaMpsTable.setStatus('mandatory')
if mibBuilder.loadTexts: cnLecsMpoaMpsTable.setDescription('The Bay Networks proprietary LECS MPS Table. This table contains configuration information for all LECS Mpoa Mpss this agent manages.')
cnLecsMpoaMpsEntry = MibTableRow((1, 3, 6, 1, 4, 1, 930, 2, 2, 3, 6, 2, 1), ).setIndexNames((0, "LAN-EMULATION-ELAN-MIB", "lecsConfIndex"), (0, "CENTILLION-LECS-MPOA-MIB", "cnLecsMpoaMpsIndex"))
if mibBuilder.loadTexts: cnLecsMpoaMpsEntry.setStatus('mandatory')
if mibBuilder.loadTexts: cnLecsMpoaMpsEntry.setDescription('Each entry contains LECS MPS information for all LECS this agent manages.')
cnLecsMpoaMpsIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 930, 2, 2, 3, 6, 2, 1, 1), MpsIndex()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cnLecsMpoaMpsIndex.setStatus('mandatory')
if mibBuilder.loadTexts: cnLecsMpoaMpsIndex.setDescription('A value which uniquely identifies this conceptual row in the cnLecsMpoaMpsTable.')
cnLecsMpoaMpsRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 930, 2, 2, 3, 6, 2, 1, 2), RowStatus()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cnLecsMpoaMpsRowStatus.setStatus('mandatory')
if mibBuilder.loadTexts: cnLecsMpoaMpsRowStatus.setDescription('This object allows creation and deletion of Lecs MPOA Clients. Within each conceptual cnLecsMpoaMpsTable row, writable objects may be modified, regardless of the value of cnLecsMpoaMpsRowStatus.')
cnLecsMpoaMpsCtrlAtmAddr = MibTableColumn((1, 3, 6, 1, 4, 1, 930, 2, 2, 3, 6, 2, 1, 3), AtmConfigAddr()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cnLecsMpoaMpsCtrlAtmAddr.setStatus('mandatory')
if mibBuilder.loadTexts: cnLecsMpoaMpsCtrlAtmAddr.setDescription("The MPS's Control ATM Address. There exists one Control ATM Address per MPS, therefore, the value of this entry is unique within the table.")
cnLecsMpoaMpsKeepAliveTime = MibTableColumn((1, 3, 6, 1, 4, 1, 930, 2, 2, 3, 6, 2, 1, 4), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 300)).clone(10)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cnLecsMpoaMpsKeepAliveTime.setStatus('mandatory')
if mibBuilder.loadTexts: cnLecsMpoaMpsKeepAliveTime.setDescription('Keep-alive time is max interval between the MPS sending MPOA Keep-Alives in seconds.')
cnLecsMpoaMpsKeepAliveLifeTime = MibTableColumn((1, 3, 6, 1, 4, 1, 930, 2, 2, 3, 6, 2, 1, 5), Integer32().subtype(subtypeSpec=ValueRangeConstraint(3, 1000)).clone(35)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cnLecsMpoaMpsKeepAliveLifeTime.setStatus('mandatory')
if mibBuilder.loadTexts: cnLecsMpoaMpsKeepAliveLifeTime.setDescription('Keep-Alive Lifetime The length of time an MPC may consider a Keep-Alive valid in seconds. This value must be at least three times the cnLecsMpoaMpsKeepAliveTime.')
cnLecsMpoaMpsInitialRetryTime = MibTableColumn((1, 3, 6, 1, 4, 1, 930, 2, 2, 3, 6, 2, 1, 6), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 300)).clone(5)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cnLecsMpoaMpsInitialRetryTime.setStatus('mandatory')
if mibBuilder.loadTexts: cnLecsMpoaMpsInitialRetryTime.setDescription('Initial value in seconds for the MPOA retry mechanism.')
cnLecsMpoaMpsRetryTimeMaximum = MibTableColumn((1, 3, 6, 1, 4, 1, 930, 2, 2, 3, 6, 2, 1, 7), Integer32().subtype(subtypeSpec=ValueRangeConstraint(10, 300)).clone(40)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cnLecsMpoaMpsRetryTimeMaximum.setReference('Multiprotocol Over ATM. AF-MPOA-0087.000. Section 4.3 MPOA Retry Mechanism')
if mibBuilder.loadTexts: cnLecsMpoaMpsRetryTimeMaximum.setStatus('mandatory')
if mibBuilder.loadTexts: cnLecsMpoaMpsRetryTimeMaximum.setDescription('Cumulative max value in seconds for Retry Time.')
cnLecsMpoaMpsGiveupTime = MibTableColumn((1, 3, 6, 1, 4, 1, 930, 2, 2, 3, 6, 2, 1, 8), Integer32().subtype(subtypeSpec=ValueRangeConstraint(5, 300)).clone(40)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cnLecsMpoaMpsGiveupTime.setStatus('mandatory')
if mibBuilder.loadTexts: cnLecsMpoaMpsGiveupTime.setDescription('Give Up Time. Minimum time in seconds to wait before giving up on a pending resolution request.')
cnLecsMpoaMpsDefaultHoldingTime = MibTableColumn((1, 3, 6, 1, 4, 1, 930, 2, 2, 3, 6, 2, 1, 9), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 120)).clone(20)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cnLecsMpoaMpsDefaultHoldingTime.setStatus('mandatory')
if mibBuilder.loadTexts: cnLecsMpoaMpsDefaultHoldingTime.setDescription('Default Holding Time in minutes. The default Holding Time used in NHRP Resolution Replies. An egress MPS may use local information to determine a more appropriate Holding Time.')
cnLecsMpoaMpsDefaultTLV = MibTableColumn((1, 3, 6, 1, 4, 1, 930, 2, 2, 3, 6, 2, 1, 10), TruthValue().clone('false')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cnLecsMpoaMpsDefaultTLV.setStatus('mandatory')
if mibBuilder.loadTexts: cnLecsMpoaMpsDefaultTLV.setDescription('Indicates whether this CnLecsMpoaMpsEntry contains the default TLV settings. Only one entry in the table can have the default settings.')
cnLecsMpoaMpcProtocolTable = MibTable((1, 3, 6, 1, 4, 1, 930, 2, 2, 3, 6, 3), )
if mibBuilder.loadTexts: cnLecsMpoaMpcProtocolTable.setStatus('mandatory')
if mibBuilder.loadTexts: cnLecsMpoaMpcProtocolTable.setDescription('The Bay Networks proprietary Protocol LECS MPS Table. This table contains the protocal configuration information for all LECS this agent manages.')
cnLecsMpoaMpcProtocolEntry = MibTableRow((1, 3, 6, 1, 4, 1, 930, 2, 2, 3, 6, 3, 1), ).setIndexNames((0, "LAN-EMULATION-ELAN-MIB", "lecsConfIndex"), (0, "CENTILLION-LECS-MPOA-MIB", "cnLecsMpoaMpcProtocolIndex"), (0, "CENTILLION-LECS-MPOA-MIB", "cnLecsMpoaMpcFlowDetectProtocol"))
if mibBuilder.loadTexts: cnLecsMpoaMpcProtocolEntry.setStatus('mandatory')
if mibBuilder.loadTexts: cnLecsMpoaMpcProtocolEntry.setDescription('Each entry contains Protocol LECS MPC information for all LECS this agent manages.')
cnLecsMpoaMpcProtocolIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 930, 2, 2, 3, 6, 3, 1, 1), MpcIndex()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cnLecsMpoaMpcProtocolIndex.setStatus('mandatory')
if mibBuilder.loadTexts: cnLecsMpoaMpcProtocolIndex.setDescription('A value which uniquely identifies this conceptual row in the cnLecsMpoaMpcProtocolTable.')
cnLecsMpoaMpcFlowDetectProtocol = MibTableColumn((1, 3, 6, 1, 4, 1, 930, 2, 2, 3, 6, 3, 1, 2), InternetworkAddrType()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cnLecsMpoaMpcFlowDetectProtocol.setStatus('mandatory')
if mibBuilder.loadTexts: cnLecsMpoaMpcFlowDetectProtocol.setDescription('The protocol on which flow detection is performed. This value is an index into the Protocol Table.')
cnLecsMpoaMpcProtocolRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 930, 2, 2, 3, 6, 3, 1, 3), RowStatus()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cnLecsMpoaMpcProtocolRowStatus.setStatus('mandatory')
if mibBuilder.loadTexts: cnLecsMpoaMpcProtocolRowStatus.setDescription('This object allows creation and deletion of Lecs MPOA Protocol.')
cnLecsMpoaMpcProtocolEnable = MibTableColumn((1, 3, 6, 1, 4, 1, 930, 2, 2, 3, 6, 3, 1, 4), TruthValue()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cnLecsMpoaMpcProtocolEnable.setStatus('mandatory')
if mibBuilder.loadTexts: cnLecsMpoaMpcProtocolEnable.setDescription('This object enables or disables mpoa for a particular protocol for this entry in the table.')
cnLecsMpoaMpsProtocolTable = MibTable((1, 3, 6, 1, 4, 1, 930, 2, 2, 3, 6, 4), )
if mibBuilder.loadTexts: cnLecsMpoaMpsProtocolTable.setStatus('mandatory')
if mibBuilder.loadTexts: cnLecsMpoaMpsProtocolTable.setDescription('The Bay Networks proprietary Protocol LECS MPS Table. This table contains the protocal configuration information for all LECS this agent manages.')
cnLecsMpoaMpsProtocolEntry = MibTableRow((1, 3, 6, 1, 4, 1, 930, 2, 2, 3, 6, 4, 1), ).setIndexNames((0, "LAN-EMULATION-ELAN-MIB", "lecsConfIndex"), (0, "CENTILLION-LECS-MPOA-MIB", "cnLecsMpoaMpsProtocolIndex"), (0, "CENTILLION-LECS-MPOA-MIB", "cnLecsMpoaMpsInternetworkLayerProtocol"))
if mibBuilder.loadTexts: cnLecsMpoaMpsProtocolEntry.setStatus('mandatory')
if mibBuilder.loadTexts: cnLecsMpoaMpsProtocolEntry.setDescription('Each entry contains Protocol LECS MPs information for all LECS this agent manages.')
cnLecsMpoaMpsProtocolIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 930, 2, 2, 3, 6, 4, 1, 1), MpsIndex()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cnLecsMpoaMpsProtocolIndex.setStatus('mandatory')
if mibBuilder.loadTexts: cnLecsMpoaMpsProtocolIndex.setDescription('A value which uniquely identifies this conceptual row in the cnLecsMpoaMpsProtocolTable.')
cnLecsMpoaMpsInternetworkLayerProtocol = MibTableColumn((1, 3, 6, 1, 4, 1, 930, 2, 2, 3, 6, 4, 1, 2), InternetworkAddrType()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cnLecsMpoaMpsInternetworkLayerProtocol.setStatus('mandatory')
if mibBuilder.loadTexts: cnLecsMpoaMpsInternetworkLayerProtocol.setDescription('The protocol on which flow detection is performed. This value is an index into the Protocol Table.')
cnLecsMpoaMpsProtocolRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 930, 2, 2, 3, 6, 4, 1, 3), RowStatus()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cnLecsMpoaMpsProtocolRowStatus.setStatus('mandatory')
if mibBuilder.loadTexts: cnLecsMpoaMpsProtocolRowStatus.setDescription('This object allows creation and deletion of Lecs MPOA Protocol.')
cnLecsMpoaMpsProtocolEnable = MibTableColumn((1, 3, 6, 1, 4, 1, 930, 2, 2, 3, 6, 4, 1, 4), TruthValue()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cnLecsMpoaMpsProtocolEnable.setStatus('mandatory')
if mibBuilder.loadTexts: cnLecsMpoaMpsProtocolEnable.setDescription('This object enables or disables mpoa for a particular protocol for this entry in the table.')
mibBuilder.exportSymbols("CENTILLION-LECS-MPOA-MIB", cnLecsMpoaMpsDefaultHoldingTime=cnLecsMpoaMpsDefaultHoldingTime, cnLecsMpoaMpsProtocolEnable=cnLecsMpoaMpsProtocolEnable, cnLecsMpoaMpcHoldDownTime=cnLecsMpoaMpcHoldDownTime, cnLecsMpoaMpcFlowDetectProtocol=cnLecsMpoaMpcFlowDetectProtocol, cnLecsMpoaMpcRowStatus=cnLecsMpoaMpcRowStatus, cnLecsMpoaMpcSCSetupFrameCount=cnLecsMpoaMpcSCSetupFrameCount, cnLecsMpoaMpsDefaultTLV=cnLecsMpoaMpsDefaultTLV, cnLecsMpoaMpcProtocolIndex=cnLecsMpoaMpcProtocolIndex, cnLecsMpoaMpsTable=cnLecsMpoaMpsTable, cnLecsMpoaMpsInternetworkLayerProtocol=cnLecsMpoaMpsInternetworkLayerProtocol, cnLecsMpoaMpcIndex=cnLecsMpoaMpcIndex, cnLecsMpoaMpcEntry=cnLecsMpoaMpcEntry, cnLecsMpoaMpsEntry=cnLecsMpoaMpsEntry, cnLecsMpoaMpsProtocolTable=cnLecsMpoaMpsProtocolTable, cnLecsMpoaMpsInitialRetryTime=cnLecsMpoaMpsInitialRetryTime, cnLecsMpoaMpsProtocolRowStatus=cnLecsMpoaMpsProtocolRowStatus, cnLecsMpoaMpcDefaultTLV=cnLecsMpoaMpcDefaultTLV, cnLecsMpoaMpsProtocolEntry=cnLecsMpoaMpsProtocolEntry, cnLecsMpoaMpsCtrlAtmAddr=cnLecsMpoaMpsCtrlAtmAddr, cnLecsMpoaGroup=cnLecsMpoaGroup, cnLecsMpoaMpsKeepAliveTime=cnLecsMpoaMpsKeepAliveTime, cnLecsMpoaMpcSCSetupFrameTime=cnLecsMpoaMpcSCSetupFrameTime, cnLecsMpoaMpcInitialRetryTime=cnLecsMpoaMpcInitialRetryTime, cnLecsMpoaMpcProtocolEntry=cnLecsMpoaMpcProtocolEntry, cnLecsMpoaMpsKeepAliveLifeTime=cnLecsMpoaMpsKeepAliveLifeTime, cnLecsMpoaMpsIndex=cnLecsMpoaMpsIndex, cnLecsMpoaMpsGiveupTime=cnLecsMpoaMpsGiveupTime, cnLecsMpoaMpcCtrlAtmAddr=cnLecsMpoaMpcCtrlAtmAddr, cnLecsMpoaMpsProtocolIndex=cnLecsMpoaMpsProtocolIndex, cnLecsMpoaMpcProtocolRowStatus=cnLecsMpoaMpcProtocolRowStatus, cnLecsMpoaMpsRetryTimeMaximum=cnLecsMpoaMpsRetryTimeMaximum, cnLecsMpoaMpcProtocolEnable=cnLecsMpoaMpcProtocolEnable, cnLecsMpoaMpcTable=cnLecsMpoaMpcTable, cnLecsMpoaMpcProtocolTable=cnLecsMpoaMpcProtocolTable, cnLecsMpoaMpsRowStatus=cnLecsMpoaMpsRowStatus, cnLecsMpoaMpcRetryTimeMaximum=cnLecsMpoaMpcRetryTimeMaximum)
