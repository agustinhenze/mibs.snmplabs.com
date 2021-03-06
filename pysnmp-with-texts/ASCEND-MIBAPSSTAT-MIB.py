#
# PySNMP MIB module ASCEND-MIBAPSSTAT-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/ASCEND-MIBAPSSTAT-MIB
# Produced by pysmi-0.3.4 at Wed May  1 11:26:23 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
configuration, = mibBuilder.importSymbols("ASCEND-MIB", "configuration")
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsUnion, ValueRangeConstraint, SingleValueConstraint, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsUnion", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsIntersection")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
NotificationType, Bits, ObjectIdentity, iso, Gauge32, Integer32, Unsigned32, MibIdentifier, Counter64, MibScalar, MibTable, MibTableRow, MibTableColumn, TimeTicks, IpAddress, ModuleIdentity, Counter32 = mibBuilder.importSymbols("SNMPv2-SMI", "NotificationType", "Bits", "ObjectIdentity", "iso", "Gauge32", "Integer32", "Unsigned32", "MibIdentifier", "Counter64", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "TimeTicks", "IpAddress", "ModuleIdentity", "Counter32")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
class DisplayString(OctetString):
    pass

mibapsStat = MibIdentifier((1, 3, 6, 1, 4, 1, 529, 23, 149))
mibapsStatTable = MibTable((1, 3, 6, 1, 4, 1, 529, 23, 149, 1), )
if mibBuilder.loadTexts: mibapsStatTable.setStatus('mandatory')
if mibBuilder.loadTexts: mibapsStatTable.setDescription('A list of mibapsStat profile entries.')
mibapsStatEntry = MibTableRow((1, 3, 6, 1, 4, 1, 529, 23, 149, 1, 1), ).setIndexNames((0, "ASCEND-MIBAPSSTAT-MIB", "apsStat-Name"))
if mibBuilder.loadTexts: mibapsStatEntry.setStatus('mandatory')
if mibBuilder.loadTexts: mibapsStatEntry.setDescription('A mibapsStat entry containing objects that maps to the parameters of mibapsStat profile.')
apsStat_Name = MibScalar((1, 3, 6, 1, 4, 1, 529, 23, 149, 1, 1, 1), DisplayString()).setLabel("apsStat-Name").setMaxAccess("readonly")
if mibBuilder.loadTexts: apsStat_Name.setStatus('mandatory')
if mibBuilder.loadTexts: apsStat_Name.setDescription('Name of APS protection group (aps-config profile).')
apsStat_ProtectionChannel_Shelf = MibScalar((1, 3, 6, 1, 4, 1, 529, 23, 149, 1, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 8, 9, 10))).clone(namedValues=NamedValues(("anyShelf", 1), ("shelf1", 2), ("shelf2", 3), ("shelf3", 4), ("shelf4", 5), ("shelf5", 6), ("shelf6", 7), ("shelf7", 8), ("shelf8", 9), ("shelf9", 10)))).setLabel("apsStat-ProtectionChannel-Shelf").setMaxAccess("readwrite")
if mibBuilder.loadTexts: apsStat_ProtectionChannel_Shelf.setStatus('mandatory')
if mibBuilder.loadTexts: apsStat_ProtectionChannel_Shelf.setDescription('The number of the shelf that the addressed physical device resides on.')
apsStat_ProtectionChannel_Slot = MibScalar((1, 3, 6, 1, 4, 1, 529, 23, 149, 1, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 55, 56, 57, 58, 49, 50, 42, 53, 54, 45, 46, 51, 59))).clone(namedValues=NamedValues(("anySlot", 1), ("slot1", 2), ("slot2", 3), ("slot3", 4), ("slot4", 5), ("slot5", 6), ("slot6", 7), ("slot7", 8), ("slot8", 9), ("slot9", 10), ("slot10", 11), ("slot11", 12), ("slot12", 13), ("slot13", 14), ("slot14", 15), ("slot15", 16), ("slot16", 17), ("slot17", 18), ("slot18", 19), ("slot19", 20), ("slot20", 21), ("slot21", 22), ("slot22", 23), ("slot23", 24), ("slot24", 25), ("slot25", 26), ("slot26", 27), ("slot27", 28), ("slot28", 29), ("slot29", 30), ("slot30", 31), ("slot31", 32), ("slot32", 33), ("slot33", 34), ("slot34", 35), ("slot35", 36), ("slot36", 37), ("slot37", 38), ("slot38", 39), ("slot39", 40), ("slot40", 41), ("aLim", 55), ("bLim", 56), ("cLim", 57), ("dLim", 58), ("leftController", 49), ("rightController", 50), ("controller", 42), ("firstControlModule", 53), ("secondControlModule", 54), ("trunkModule1", 45), ("trunkModule2", 46), ("controlModule", 51), ("slotPrimary", 59)))).setLabel("apsStat-ProtectionChannel-Slot").setMaxAccess("readwrite")
if mibBuilder.loadTexts: apsStat_ProtectionChannel_Slot.setStatus('mandatory')
if mibBuilder.loadTexts: apsStat_ProtectionChannel_Slot.setDescription('The number of the slot that the addressed physical device resides on.')
apsStat_ProtectionChannel_ItemNumber = MibScalar((1, 3, 6, 1, 4, 1, 529, 23, 149, 1, 1, 4), Integer32()).setLabel("apsStat-ProtectionChannel-ItemNumber").setMaxAccess("readwrite")
if mibBuilder.loadTexts: apsStat_ProtectionChannel_ItemNumber.setStatus('mandatory')
if mibBuilder.loadTexts: apsStat_ProtectionChannel_ItemNumber.setDescription('A number that specifies an addressable entity within the context of shelf and slot.')
apsStat_WorkingChannel_Shelf = MibScalar((1, 3, 6, 1, 4, 1, 529, 23, 149, 1, 1, 43), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 8, 9, 10))).clone(namedValues=NamedValues(("anyShelf", 1), ("shelf1", 2), ("shelf2", 3), ("shelf3", 4), ("shelf4", 5), ("shelf5", 6), ("shelf6", 7), ("shelf7", 8), ("shelf8", 9), ("shelf9", 10)))).setLabel("apsStat-WorkingChannel-Shelf").setMaxAccess("readwrite")
if mibBuilder.loadTexts: apsStat_WorkingChannel_Shelf.setStatus('mandatory')
if mibBuilder.loadTexts: apsStat_WorkingChannel_Shelf.setDescription('The number of the shelf that the addressed physical device resides on.')
apsStat_WorkingChannel_Slot = MibScalar((1, 3, 6, 1, 4, 1, 529, 23, 149, 1, 1, 44), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 55, 56, 57, 58, 49, 50, 42, 53, 54, 45, 46, 51, 59))).clone(namedValues=NamedValues(("anySlot", 1), ("slot1", 2), ("slot2", 3), ("slot3", 4), ("slot4", 5), ("slot5", 6), ("slot6", 7), ("slot7", 8), ("slot8", 9), ("slot9", 10), ("slot10", 11), ("slot11", 12), ("slot12", 13), ("slot13", 14), ("slot14", 15), ("slot15", 16), ("slot16", 17), ("slot17", 18), ("slot18", 19), ("slot19", 20), ("slot20", 21), ("slot21", 22), ("slot22", 23), ("slot23", 24), ("slot24", 25), ("slot25", 26), ("slot26", 27), ("slot27", 28), ("slot28", 29), ("slot29", 30), ("slot30", 31), ("slot31", 32), ("slot32", 33), ("slot33", 34), ("slot34", 35), ("slot35", 36), ("slot36", 37), ("slot37", 38), ("slot38", 39), ("slot39", 40), ("slot40", 41), ("aLim", 55), ("bLim", 56), ("cLim", 57), ("dLim", 58), ("leftController", 49), ("rightController", 50), ("controller", 42), ("firstControlModule", 53), ("secondControlModule", 54), ("trunkModule1", 45), ("trunkModule2", 46), ("controlModule", 51), ("slotPrimary", 59)))).setLabel("apsStat-WorkingChannel-Slot").setMaxAccess("readwrite")
if mibBuilder.loadTexts: apsStat_WorkingChannel_Slot.setStatus('mandatory')
if mibBuilder.loadTexts: apsStat_WorkingChannel_Slot.setDescription('The number of the slot that the addressed physical device resides on.')
apsStat_WorkingChannel_ItemNumber = MibScalar((1, 3, 6, 1, 4, 1, 529, 23, 149, 1, 1, 45), Integer32()).setLabel("apsStat-WorkingChannel-ItemNumber").setMaxAccess("readwrite")
if mibBuilder.loadTexts: apsStat_WorkingChannel_ItemNumber.setStatus('mandatory')
if mibBuilder.loadTexts: apsStat_WorkingChannel_ItemNumber.setDescription('A number that specifies an addressable entity within the context of shelf and slot.')
apsStat_ApsState = MibScalar((1, 3, 6, 1, 4, 1, 529, 23, 149, 1, 1, 8), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("unknown", 1), ("onProtection", 2), ("onWorking", 3)))).setLabel("apsStat-ApsState").setMaxAccess("readonly")
if mibBuilder.loadTexts: apsStat_ApsState.setStatus('mandatory')
if mibBuilder.loadTexts: apsStat_ApsState.setDescription('Current status of the protection switching.')
apsStat_BridgeStatus = MibScalar((1, 3, 6, 1, 4, 1, 529, 23, 149, 1, 1, 47), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("false", 1), ("true", 2)))).setLabel("apsStat-BridgeStatus").setMaxAccess("readonly")
if mibBuilder.loadTexts: apsStat_BridgeStatus.setStatus('mandatory')
if mibBuilder.loadTexts: apsStat_BridgeStatus.setDescription('Status of the bridge. True if bridging is on (always on for 1+1).')
apsStat_LastSwitchTime = MibScalar((1, 3, 6, 1, 4, 1, 529, 23, 149, 1, 1, 48), Integer32()).setLabel("apsStat-LastSwitchTime").setMaxAccess("readonly")
if mibBuilder.loadTexts: apsStat_LastSwitchTime.setStatus('mandatory')
if mibBuilder.loadTexts: apsStat_LastSwitchTime.setDescription('Time of last switch.')
apsStat_SwitchCount = MibScalar((1, 3, 6, 1, 4, 1, 529, 23, 149, 1, 1, 49), Integer32()).setLabel("apsStat-SwitchCount").setMaxAccess("readonly")
if mibBuilder.loadTexts: apsStat_SwitchCount.setStatus('mandatory')
if mibBuilder.loadTexts: apsStat_SwitchCount.setDescription('Number of times switch over to protection channel occured.')
apsStat_ApsCfgCreationTime = MibScalar((1, 3, 6, 1, 4, 1, 529, 23, 149, 1, 1, 50), Integer32()).setLabel("apsStat-ApsCfgCreationTime").setMaxAccess("readonly")
if mibBuilder.loadTexts: apsStat_ApsCfgCreationTime.setStatus('mandatory')
if mibBuilder.loadTexts: apsStat_ApsCfgCreationTime.setDescription('Time the protection group was created.')
apsStat_NumberOfChannels = MibScalar((1, 3, 6, 1, 4, 1, 529, 23, 149, 1, 1, 51), Integer32()).setLabel("apsStat-NumberOfChannels").setMaxAccess("readonly")
if mibBuilder.loadTexts: apsStat_NumberOfChannels.setStatus('mandatory')
if mibBuilder.loadTexts: apsStat_NumberOfChannels.setDescription('Number of channels in this protection group.')
apsStat_PsbfFailure = MibScalar((1, 3, 6, 1, 4, 1, 529, 23, 149, 1, 1, 52), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("false", 1), ("true", 2)))).setLabel("apsStat-PsbfFailure").setMaxAccess("readonly")
if mibBuilder.loadTexts: apsStat_PsbfFailure.setStatus('mandatory')
if mibBuilder.loadTexts: apsStat_PsbfFailure.setDescription('PSBF state.')
apsStat_ChannelMismatchFailure = MibScalar((1, 3, 6, 1, 4, 1, 529, 23, 149, 1, 1, 53), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("false", 1), ("true", 2)))).setLabel("apsStat-ChannelMismatchFailure").setMaxAccess("readonly")
if mibBuilder.loadTexts: apsStat_ChannelMismatchFailure.setStatus('mandatory')
if mibBuilder.loadTexts: apsStat_ChannelMismatchFailure.setDescription('Channel mismatch state.')
apsStat_ModeMismatchFailure = MibScalar((1, 3, 6, 1, 4, 1, 529, 23, 149, 1, 1, 54), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("false", 1), ("true", 2)))).setLabel("apsStat-ModeMismatchFailure").setMaxAccess("readonly")
if mibBuilder.loadTexts: apsStat_ModeMismatchFailure.setStatus('mandatory')
if mibBuilder.loadTexts: apsStat_ModeMismatchFailure.setDescription('Mode mismatch state.')
apsStat_FeplFailure = MibScalar((1, 3, 6, 1, 4, 1, 529, 23, 149, 1, 1, 55), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("false", 1), ("true", 2)))).setLabel("apsStat-FeplFailure").setMaxAccess("readonly")
if mibBuilder.loadTexts: apsStat_FeplFailure.setStatus('mandatory')
if mibBuilder.loadTexts: apsStat_FeplFailure.setDescription('FEPL state.')
apsStat_RecvPsbfCount = MibScalar((1, 3, 6, 1, 4, 1, 529, 23, 149, 1, 1, 29), Integer32()).setLabel("apsStat-RecvPsbfCount").setMaxAccess("readonly")
if mibBuilder.loadTexts: apsStat_RecvPsbfCount.setStatus('mandatory')
if mibBuilder.loadTexts: apsStat_RecvPsbfCount.setDescription('Count of PSBF events received.')
apsStat_RecvModeMismatchCount = MibScalar((1, 3, 6, 1, 4, 1, 529, 23, 149, 1, 1, 30), Integer32()).setLabel("apsStat-RecvModeMismatchCount").setMaxAccess("readonly")
if mibBuilder.loadTexts: apsStat_RecvModeMismatchCount.setStatus('mandatory')
if mibBuilder.loadTexts: apsStat_RecvModeMismatchCount.setDescription('Count of mode-mismatch events received.')
apsStat_RecvChannelMismatchCount = MibScalar((1, 3, 6, 1, 4, 1, 529, 23, 149, 1, 1, 31), Integer32()).setLabel("apsStat-RecvChannelMismatchCount").setMaxAccess("readonly")
if mibBuilder.loadTexts: apsStat_RecvChannelMismatchCount.setStatus('mandatory')
if mibBuilder.loadTexts: apsStat_RecvChannelMismatchCount.setDescription('Count of channel-mismatch events received.')
apsStat_RecvFeplCount = MibScalar((1, 3, 6, 1, 4, 1, 529, 23, 149, 1, 1, 32), Integer32()).setLabel("apsStat-RecvFeplCount").setMaxAccess("readonly")
if mibBuilder.loadTexts: apsStat_RecvFeplCount.setStatus('mandatory')
if mibBuilder.loadTexts: apsStat_RecvFeplCount.setDescription('Count of FEPL events received.')
apsStat_ExtraTrafficFlag = MibScalar((1, 3, 6, 1, 4, 1, 529, 23, 149, 1, 1, 33), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("false", 1), ("true", 2)))).setLabel("apsStat-ExtraTrafficFlag").setMaxAccess("readonly")
if mibBuilder.loadTexts: apsStat_ExtraTrafficFlag.setStatus('mandatory')
if mibBuilder.loadTexts: apsStat_ExtraTrafficFlag.setDescription('Indicates whether extra traffic is being carried on protection channel (1:n only).')
apsStat_ProtectionMode = MibScalar((1, 3, 6, 1, 4, 1, 529, 23, 149, 1, 1, 5), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("n-1-plus-1", 1), ("n-1-divide-n", 2)))).setLabel("apsStat-ProtectionMode").setMaxAccess("readonly")
if mibBuilder.loadTexts: apsStat_ProtectionMode.setStatus('mandatory')
if mibBuilder.loadTexts: apsStat_ProtectionMode.setDescription('The linear APS protection mode (1+1, 1:n).')
apsStat_DirectionMode = MibScalar((1, 3, 6, 1, 4, 1, 529, 23, 149, 1, 1, 6), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("unidirectional", 1), ("bidirectional", 2)))).setLabel("apsStat-DirectionMode").setMaxAccess("readonly")
if mibBuilder.loadTexts: apsStat_DirectionMode.setStatus('mandatory')
if mibBuilder.loadTexts: apsStat_DirectionMode.setDescription('The protection group mode (direction) of operation.')
apsStat_RevertiveMode = MibScalar((1, 3, 6, 1, 4, 1, 529, 23, 149, 1, 1, 7), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(2, 1))).clone(namedValues=NamedValues(("nonRevertive", 2), ("revertive", 1)))).setLabel("apsStat-RevertiveMode").setMaxAccess("readonly")
if mibBuilder.loadTexts: apsStat_RevertiveMode.setStatus('mandatory')
if mibBuilder.loadTexts: apsStat_RevertiveMode.setDescription('The protection group revertive mode of operation.')
apsStat_RxK1ByteValue = MibScalar((1, 3, 6, 1, 4, 1, 529, 23, 149, 1, 1, 34), DisplayString()).setLabel("apsStat-RxK1ByteValue").setMaxAccess("readonly")
if mibBuilder.loadTexts: apsStat_RxK1ByteValue.setStatus('mandatory')
if mibBuilder.loadTexts: apsStat_RxK1ByteValue.setDescription('Current value of K1 byte received on protection channel')
apsStat_RxK2ByteValue = MibScalar((1, 3, 6, 1, 4, 1, 529, 23, 149, 1, 1, 35), DisplayString()).setLabel("apsStat-RxK2ByteValue").setMaxAccess("readonly")
if mibBuilder.loadTexts: apsStat_RxK2ByteValue.setStatus('mandatory')
if mibBuilder.loadTexts: apsStat_RxK2ByteValue.setDescription('Current value of K2 byte received on protection channel')
apsStat_TxK1ByteValue = MibScalar((1, 3, 6, 1, 4, 1, 529, 23, 149, 1, 1, 36), DisplayString()).setLabel("apsStat-TxK1ByteValue").setMaxAccess("readonly")
if mibBuilder.loadTexts: apsStat_TxK1ByteValue.setStatus('mandatory')
if mibBuilder.loadTexts: apsStat_TxK1ByteValue.setDescription('Last value of K1 byte transmitted on protection channel')
apsStat_TxK2ByteValue = MibScalar((1, 3, 6, 1, 4, 1, 529, 23, 149, 1, 1, 37), DisplayString()).setLabel("apsStat-TxK2ByteValue").setMaxAccess("readonly")
if mibBuilder.loadTexts: apsStat_TxK2ByteValue.setStatus('mandatory')
if mibBuilder.loadTexts: apsStat_TxK2ByteValue.setDescription('Last value of K2 byte transmitted on protection channel')
apsStat_Action_o = MibScalar((1, 3, 6, 1, 4, 1, 529, 23, 149, 1, 1, 42), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("noAction", 1), ("createProfile", 2), ("deleteProfile", 3)))).setLabel("apsStat-Action-o").setMaxAccess("readwrite")
if mibBuilder.loadTexts: apsStat_Action_o.setStatus('mandatory')
if mibBuilder.loadTexts: apsStat_Action_o.setDescription('')
mibBuilder.exportSymbols("ASCEND-MIBAPSSTAT-MIB", apsStat_ProtectionMode=apsStat_ProtectionMode, apsStat_RecvChannelMismatchCount=apsStat_RecvChannelMismatchCount, apsStat_RxK1ByteValue=apsStat_RxK1ByteValue, apsStat_WorkingChannel_Slot=apsStat_WorkingChannel_Slot, apsStat_ProtectionChannel_Shelf=apsStat_ProtectionChannel_Shelf, apsStat_RecvModeMismatchCount=apsStat_RecvModeMismatchCount, apsStat_Action_o=apsStat_Action_o, apsStat_ExtraTrafficFlag=apsStat_ExtraTrafficFlag, mibapsStat=mibapsStat, apsStat_NumberOfChannels=apsStat_NumberOfChannels, apsStat_ProtectionChannel_ItemNumber=apsStat_ProtectionChannel_ItemNumber, apsStat_RxK2ByteValue=apsStat_RxK2ByteValue, apsStat_WorkingChannel_ItemNumber=apsStat_WorkingChannel_ItemNumber, apsStat_SwitchCount=apsStat_SwitchCount, apsStat_TxK2ByteValue=apsStat_TxK2ByteValue, apsStat_RevertiveMode=apsStat_RevertiveMode, apsStat_RecvFeplCount=apsStat_RecvFeplCount, apsStat_FeplFailure=apsStat_FeplFailure, apsStat_TxK1ByteValue=apsStat_TxK1ByteValue, apsStat_WorkingChannel_Shelf=apsStat_WorkingChannel_Shelf, mibapsStatTable=mibapsStatTable, mibapsStatEntry=mibapsStatEntry, apsStat_RecvPsbfCount=apsStat_RecvPsbfCount, apsStat_PsbfFailure=apsStat_PsbfFailure, apsStat_BridgeStatus=apsStat_BridgeStatus, apsStat_ProtectionChannel_Slot=apsStat_ProtectionChannel_Slot, apsStat_ChannelMismatchFailure=apsStat_ChannelMismatchFailure, apsStat_ApsState=apsStat_ApsState, apsStat_DirectionMode=apsStat_DirectionMode, apsStat_ModeMismatchFailure=apsStat_ModeMismatchFailure, apsStat_ApsCfgCreationTime=apsStat_ApsCfgCreationTime, apsStat_Name=apsStat_Name, DisplayString=DisplayString, apsStat_LastSwitchTime=apsStat_LastSwitchTime)
