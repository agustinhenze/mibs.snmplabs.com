#
# PySNMP MIB module Nortel-MsCarrier-MscPassport-OamEthernetMIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/Nortel-MsCarrier-MscPassport-OamEthernetMIB
# Produced by pysmi-0.3.4 at Mon Apr 29 20:21:38 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
Integer, OctetString, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "Integer", "OctetString", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsUnion, ValueSizeConstraint, SingleValueConstraint, ConstraintsIntersection, ValueRangeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "ValueSizeConstraint", "SingleValueConstraint", "ConstraintsIntersection", "ValueRangeConstraint")
mscLpIndex, mscLp = mibBuilder.importSymbols("Nortel-MsCarrier-MscPassport-LogicalProcessorMIB", "mscLpIndex", "mscLp")
StorageType, MacAddress, Integer32, Counter32, DisplayString, Unsigned32, RowStatus, InterfaceIndex = mibBuilder.importSymbols("Nortel-MsCarrier-MscPassport-StandardTextualConventionsMIB", "StorageType", "MacAddress", "Integer32", "Counter32", "DisplayString", "Unsigned32", "RowStatus", "InterfaceIndex")
NonReplicated, Link, AsciiString = mibBuilder.importSymbols("Nortel-MsCarrier-MscPassport-TextualConventionsMIB", "NonReplicated", "Link", "AsciiString")
mscPassportMIBs, = mibBuilder.importSymbols("Nortel-MsCarrier-MscPassport-UsefulDefinitionsMIB", "mscPassportMIBs")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
ObjectIdentity, NotificationType, ModuleIdentity, Integer32, Counter32, Unsigned32, iso, MibIdentifier, Counter64, MibScalar, MibTable, MibTableRow, MibTableColumn, TimeTicks, IpAddress, Bits, Gauge32 = mibBuilder.importSymbols("SNMPv2-SMI", "ObjectIdentity", "NotificationType", "ModuleIdentity", "Integer32", "Counter32", "Unsigned32", "iso", "MibIdentifier", "Counter64", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "TimeTicks", "IpAddress", "Bits", "Gauge32")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
oamEthernetMIB = MibIdentifier((1, 3, 6, 1, 4, 1, 562, 36, 2, 2, 79))
mscLpOamEnet = MibIdentifier((1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 27))
mscLpOamEnetRowStatusTable = MibTable((1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 27, 1), )
if mibBuilder.loadTexts: mscLpOamEnetRowStatusTable.setStatus('mandatory')
mscLpOamEnetRowStatusEntry = MibTableRow((1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 27, 1, 1), ).setIndexNames((0, "Nortel-MsCarrier-MscPassport-LogicalProcessorMIB", "mscLpIndex"), (0, "Nortel-MsCarrier-MscPassport-OamEthernetMIB", "mscLpOamEnetIndex"))
if mibBuilder.loadTexts: mscLpOamEnetRowStatusEntry.setStatus('mandatory')
mscLpOamEnetRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 27, 1, 1, 1), RowStatus()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: mscLpOamEnetRowStatus.setStatus('mandatory')
mscLpOamEnetComponentName = MibTableColumn((1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 27, 1, 1, 2), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mscLpOamEnetComponentName.setStatus('mandatory')
mscLpOamEnetStorageType = MibTableColumn((1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 27, 1, 1, 4), StorageType()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mscLpOamEnetStorageType.setStatus('mandatory')
mscLpOamEnetIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 27, 1, 1, 10), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 0)))
if mibBuilder.loadTexts: mscLpOamEnetIndex.setStatus('mandatory')
mscLpOamEnetCidDataTable = MibTable((1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 27, 10), )
if mibBuilder.loadTexts: mscLpOamEnetCidDataTable.setStatus('mandatory')
mscLpOamEnetCidDataEntry = MibTableRow((1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 27, 10, 1), ).setIndexNames((0, "Nortel-MsCarrier-MscPassport-LogicalProcessorMIB", "mscLpIndex"), (0, "Nortel-MsCarrier-MscPassport-OamEthernetMIB", "mscLpOamEnetIndex"))
if mibBuilder.loadTexts: mscLpOamEnetCidDataEntry.setStatus('mandatory')
mscLpOamEnetCustomerIdentifier = MibTableColumn((1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 27, 10, 1, 1), Unsigned32().subtype(subtypeSpec=ConstraintsUnion(ValueRangeConstraint(0, 0), ValueRangeConstraint(1, 8191), ))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: mscLpOamEnetCustomerIdentifier.setStatus('mandatory')
mscLpOamEnetIfEntryTable = MibTable((1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 27, 11), )
if mibBuilder.loadTexts: mscLpOamEnetIfEntryTable.setStatus('mandatory')
mscLpOamEnetIfEntryEntry = MibTableRow((1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 27, 11, 1), ).setIndexNames((0, "Nortel-MsCarrier-MscPassport-LogicalProcessorMIB", "mscLpIndex"), (0, "Nortel-MsCarrier-MscPassport-OamEthernetMIB", "mscLpOamEnetIndex"))
if mibBuilder.loadTexts: mscLpOamEnetIfEntryEntry.setStatus('mandatory')
mscLpOamEnetIfAdminStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 27, 11, 1, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("up", 1), ("down", 2), ("testing", 3))).clone('up')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: mscLpOamEnetIfAdminStatus.setStatus('mandatory')
mscLpOamEnetIfIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 27, 11, 1, 2), InterfaceIndex().subtype(subtypeSpec=ValueRangeConstraint(1, 65535))).setMaxAccess("readonly")
if mibBuilder.loadTexts: mscLpOamEnetIfIndex.setStatus('mandatory')
mscLpOamEnetProvTable = MibTable((1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 27, 12), )
if mibBuilder.loadTexts: mscLpOamEnetProvTable.setStatus('mandatory')
mscLpOamEnetProvEntry = MibTableRow((1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 27, 12, 1), ).setIndexNames((0, "Nortel-MsCarrier-MscPassport-LogicalProcessorMIB", "mscLpIndex"), (0, "Nortel-MsCarrier-MscPassport-OamEthernetMIB", "mscLpOamEnetIndex"))
if mibBuilder.loadTexts: mscLpOamEnetProvEntry.setStatus('mandatory')
mscLpOamEnetApplicationFramerName = MibTableColumn((1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 27, 12, 1, 1), Link()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: mscLpOamEnetApplicationFramerName.setStatus('mandatory')
mscLpOamEnetSwitchoverOnFailure = MibTableColumn((1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 27, 12, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enabled", 1), ("disabled", 2))).clone('enabled')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: mscLpOamEnetSwitchoverOnFailure.setStatus('mandatory')
mscLpOamEnetExtendedStatistics = MibTableColumn((1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 27, 12, 1, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enabled", 1), ("disabled", 2))).clone('disabled')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: mscLpOamEnetExtendedStatistics.setStatus('mandatory')
mscLpOamEnetAdminInfoTable = MibTable((1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 27, 13), )
if mibBuilder.loadTexts: mscLpOamEnetAdminInfoTable.setStatus('mandatory')
mscLpOamEnetAdminInfoEntry = MibTableRow((1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 27, 13, 1), ).setIndexNames((0, "Nortel-MsCarrier-MscPassport-LogicalProcessorMIB", "mscLpIndex"), (0, "Nortel-MsCarrier-MscPassport-OamEthernetMIB", "mscLpOamEnetIndex"))
if mibBuilder.loadTexts: mscLpOamEnetAdminInfoEntry.setStatus('mandatory')
mscLpOamEnetVendor = MibTableColumn((1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 27, 13, 1, 1), AsciiString().subtype(subtypeSpec=ValueSizeConstraint(0, 20))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: mscLpOamEnetVendor.setStatus('mandatory')
mscLpOamEnetCommentText = MibTableColumn((1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 27, 13, 1, 2), AsciiString().subtype(subtypeSpec=ValueSizeConstraint(0, 60))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: mscLpOamEnetCommentText.setStatus('mandatory')
mscLpOamEnetStateTable = MibTable((1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 27, 15), )
if mibBuilder.loadTexts: mscLpOamEnetStateTable.setStatus('mandatory')
mscLpOamEnetStateEntry = MibTableRow((1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 27, 15, 1), ).setIndexNames((0, "Nortel-MsCarrier-MscPassport-LogicalProcessorMIB", "mscLpIndex"), (0, "Nortel-MsCarrier-MscPassport-OamEthernetMIB", "mscLpOamEnetIndex"))
if mibBuilder.loadTexts: mscLpOamEnetStateEntry.setStatus('mandatory')
mscLpOamEnetAdminState = MibTableColumn((1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 27, 15, 1, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1, 2))).clone(namedValues=NamedValues(("locked", 0), ("unlocked", 1), ("shuttingDown", 2))).clone('unlocked')).setMaxAccess("readonly")
if mibBuilder.loadTexts: mscLpOamEnetAdminState.setStatus('mandatory')
mscLpOamEnetOperationalState = MibTableColumn((1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 27, 15, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1))).clone(namedValues=NamedValues(("disabled", 0), ("enabled", 1))).clone('disabled')).setMaxAccess("readonly")
if mibBuilder.loadTexts: mscLpOamEnetOperationalState.setStatus('mandatory')
mscLpOamEnetUsageState = MibTableColumn((1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 27, 15, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1, 2))).clone(namedValues=NamedValues(("idle", 0), ("active", 1), ("busy", 2))).clone('idle')).setMaxAccess("readonly")
if mibBuilder.loadTexts: mscLpOamEnetUsageState.setStatus('mandatory')
mscLpOamEnetOperStatusTable = MibTable((1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 27, 16), )
if mibBuilder.loadTexts: mscLpOamEnetOperStatusTable.setStatus('mandatory')
mscLpOamEnetOperStatusEntry = MibTableRow((1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 27, 16, 1), ).setIndexNames((0, "Nortel-MsCarrier-MscPassport-LogicalProcessorMIB", "mscLpIndex"), (0, "Nortel-MsCarrier-MscPassport-OamEthernetMIB", "mscLpOamEnetIndex"))
if mibBuilder.loadTexts: mscLpOamEnetOperStatusEntry.setStatus('mandatory')
mscLpOamEnetSnmpOperStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 27, 16, 1, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("up", 1), ("down", 2), ("testing", 3))).clone('up')).setMaxAccess("readonly")
if mibBuilder.loadTexts: mscLpOamEnetSnmpOperStatus.setStatus('mandatory')
mscLpOamEnetOperTable = MibTable((1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 27, 17), )
if mibBuilder.loadTexts: mscLpOamEnetOperTable.setStatus('mandatory')
mscLpOamEnetOperEntry = MibTableRow((1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 27, 17, 1), ).setIndexNames((0, "Nortel-MsCarrier-MscPassport-LogicalProcessorMIB", "mscLpIndex"), (0, "Nortel-MsCarrier-MscPassport-OamEthernetMIB", "mscLpOamEnetIndex"))
if mibBuilder.loadTexts: mscLpOamEnetOperEntry.setStatus('mandatory')
mscLpOamEnetMacAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 27, 17, 1, 1), MacAddress().subtype(subtypeSpec=ValueSizeConstraint(6, 6)).setFixedLength(6)).setMaxAccess("readonly")
if mibBuilder.loadTexts: mscLpOamEnetMacAddress.setStatus('mandatory')
mscLpOamEnetActiveStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 27, 17, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("available", 1), ("notAvailable", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: mscLpOamEnetActiveStatus.setStatus('mandatory')
mscLpOamEnetStandbyStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 27, 17, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("available", 1), ("notAvailable", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: mscLpOamEnetStandbyStatus.setStatus('mandatory')
mscLpOamEnetOamEnetStatsTable = MibTable((1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 27, 18), )
if mibBuilder.loadTexts: mscLpOamEnetOamEnetStatsTable.setStatus('mandatory')
mscLpOamEnetOamEnetStatsEntry = MibTableRow((1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 27, 18, 1), ).setIndexNames((0, "Nortel-MsCarrier-MscPassport-LogicalProcessorMIB", "mscLpIndex"), (0, "Nortel-MsCarrier-MscPassport-OamEthernetMIB", "mscLpOamEnetIndex"))
if mibBuilder.loadTexts: mscLpOamEnetOamEnetStatsEntry.setStatus('mandatory')
mscLpOamEnetClearToSendSignalLoss = MibTableColumn((1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 27, 18, 1, 14), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mscLpOamEnetClearToSendSignalLoss.setStatus('mandatory')
mscLpOamEnetFrameTooShort = MibTableColumn((1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 27, 18, 1, 15), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mscLpOamEnetFrameTooShort.setStatus('mandatory')
mscLpOamEnetNumberOfRxCollisions = MibTableColumn((1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 27, 18, 1, 17), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mscLpOamEnetNumberOfRxCollisions.setStatus('mandatory')
mscLpOamEnetLackOfResourcesDiscards = MibTableColumn((1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 27, 18, 1, 18), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mscLpOamEnetLackOfResourcesDiscards.setStatus('mandatory')
mscLpOamEnetOverrunErrors = MibTableColumn((1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 27, 18, 1, 19), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mscLpOamEnetOverrunErrors.setStatus('mandatory')
mscLpOamEnetStatsTable = MibTable((1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 27, 19), )
if mibBuilder.loadTexts: mscLpOamEnetStatsTable.setStatus('mandatory')
mscLpOamEnetStatsEntry = MibTableRow((1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 27, 19, 1), ).setIndexNames((0, "Nortel-MsCarrier-MscPassport-LogicalProcessorMIB", "mscLpIndex"), (0, "Nortel-MsCarrier-MscPassport-OamEthernetMIB", "mscLpOamEnetIndex"))
if mibBuilder.loadTexts: mscLpOamEnetStatsEntry.setStatus('mandatory')
mscLpOamEnetAlignmentErrors = MibTableColumn((1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 27, 19, 1, 2), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mscLpOamEnetAlignmentErrors.setStatus('mandatory')
mscLpOamEnetFcsErrors = MibTableColumn((1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 27, 19, 1, 3), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mscLpOamEnetFcsErrors.setStatus('mandatory')
mscLpOamEnetSingleCollisionFrames = MibTableColumn((1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 27, 19, 1, 4), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mscLpOamEnetSingleCollisionFrames.setStatus('mandatory')
mscLpOamEnetMultipleCollisionFrames = MibTableColumn((1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 27, 19, 1, 5), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mscLpOamEnetMultipleCollisionFrames.setStatus('mandatory')
mscLpOamEnetSqeTestErrors = MibTableColumn((1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 27, 19, 1, 6), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mscLpOamEnetSqeTestErrors.setStatus('mandatory')
mscLpOamEnetDeferredTransmissions = MibTableColumn((1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 27, 19, 1, 7), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mscLpOamEnetDeferredTransmissions.setStatus('mandatory')
mscLpOamEnetLateCollisions = MibTableColumn((1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 27, 19, 1, 8), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mscLpOamEnetLateCollisions.setStatus('mandatory')
mscLpOamEnetExcessiveCollisions = MibTableColumn((1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 27, 19, 1, 9), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mscLpOamEnetExcessiveCollisions.setStatus('mandatory')
mscLpOamEnetMacTransmitErrors = MibTableColumn((1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 27, 19, 1, 10), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mscLpOamEnetMacTransmitErrors.setStatus('mandatory')
mscLpOamEnetCarrierSenseErrors = MibTableColumn((1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 27, 19, 1, 11), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mscLpOamEnetCarrierSenseErrors.setStatus('mandatory')
mscLpOamEnetFrameTooLongs = MibTableColumn((1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 27, 19, 1, 12), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mscLpOamEnetFrameTooLongs.setStatus('mandatory')
mscLpOamEnetMacReceiveErrors = MibTableColumn((1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 27, 19, 1, 13), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mscLpOamEnetMacReceiveErrors.setStatus('mandatory')
mscLpOamEnetTest = MibIdentifier((1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 27, 2))
mscLpOamEnetTestRowStatusTable = MibTable((1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 27, 2, 1), )
if mibBuilder.loadTexts: mscLpOamEnetTestRowStatusTable.setStatus('mandatory')
mscLpOamEnetTestRowStatusEntry = MibTableRow((1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 27, 2, 1, 1), ).setIndexNames((0, "Nortel-MsCarrier-MscPassport-LogicalProcessorMIB", "mscLpIndex"), (0, "Nortel-MsCarrier-MscPassport-OamEthernetMIB", "mscLpOamEnetIndex"), (0, "Nortel-MsCarrier-MscPassport-OamEthernetMIB", "mscLpOamEnetTestIndex"))
if mibBuilder.loadTexts: mscLpOamEnetTestRowStatusEntry.setStatus('mandatory')
mscLpOamEnetTestRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 27, 2, 1, 1, 1), RowStatus()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mscLpOamEnetTestRowStatus.setStatus('mandatory')
mscLpOamEnetTestComponentName = MibTableColumn((1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 27, 2, 1, 1, 2), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mscLpOamEnetTestComponentName.setStatus('mandatory')
mscLpOamEnetTestStorageType = MibTableColumn((1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 27, 2, 1, 1, 4), StorageType()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mscLpOamEnetTestStorageType.setStatus('mandatory')
mscLpOamEnetTestIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 27, 2, 1, 1, 10), NonReplicated())
if mibBuilder.loadTexts: mscLpOamEnetTestIndex.setStatus('mandatory')
mscLpOamEnetTestOperTable = MibTable((1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 27, 2, 10), )
if mibBuilder.loadTexts: mscLpOamEnetTestOperTable.setStatus('mandatory')
mscLpOamEnetTestOperEntry = MibTableRow((1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 27, 2, 10, 1), ).setIndexNames((0, "Nortel-MsCarrier-MscPassport-LogicalProcessorMIB", "mscLpIndex"), (0, "Nortel-MsCarrier-MscPassport-OamEthernetMIB", "mscLpOamEnetIndex"), (0, "Nortel-MsCarrier-MscPassport-OamEthernetMIB", "mscLpOamEnetTestIndex"))
if mibBuilder.loadTexts: mscLpOamEnetTestOperEntry.setStatus('mandatory')
mscLpOamEnetTestType = MibTableColumn((1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 27, 2, 10, 1, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3))).clone(namedValues=NamedValues(("hardwareLogic", 0), ("configuration", 1), ("memoryMap", 2), ("tdr", 3)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: mscLpOamEnetTestType.setStatus('mandatory')
mscLpOamEnetTestResultsTable = MibTable((1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 27, 2, 11), )
if mibBuilder.loadTexts: mscLpOamEnetTestResultsTable.setStatus('mandatory')
mscLpOamEnetTestResultsEntry = MibTableRow((1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 27, 2, 11, 1), ).setIndexNames((0, "Nortel-MsCarrier-MscPassport-LogicalProcessorMIB", "mscLpIndex"), (0, "Nortel-MsCarrier-MscPassport-OamEthernetMIB", "mscLpOamEnetIndex"), (0, "Nortel-MsCarrier-MscPassport-OamEthernetMIB", "mscLpOamEnetTestIndex"))
if mibBuilder.loadTexts: mscLpOamEnetTestResultsEntry.setStatus('mandatory')
mscLpOamEnetTestCauseOfTermination = MibTableColumn((1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 27, 2, 11, 1, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3, 4, 5))).clone(namedValues=NamedValues(("testTimeExpired", 0), ("stoppedByOperator", 1), ("unknown", 2), ("neverStarted", 3), ("testRunning", 4), ("testComplete", 5))).clone('neverStarted')).setMaxAccess("readonly")
if mibBuilder.loadTexts: mscLpOamEnetTestCauseOfTermination.setStatus('mandatory')
mscLpOamEnetTestTestResult = MibTableColumn((1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 27, 2, 11, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3))).clone(namedValues=NamedValues(("neverRun", 0), ("fail", 1), ("pass", 2), ("running", 3)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: mscLpOamEnetTestTestResult.setStatus('mandatory')
oamEthernetGroup = MibIdentifier((1, 3, 6, 1, 4, 1, 562, 36, 2, 2, 79, 1))
oamEthernetGroupCA = MibIdentifier((1, 3, 6, 1, 4, 1, 562, 36, 2, 2, 79, 1, 1))
oamEthernetGroupCA02 = MibIdentifier((1, 3, 6, 1, 4, 1, 562, 36, 2, 2, 79, 1, 1, 3))
oamEthernetGroupCA02A = MibIdentifier((1, 3, 6, 1, 4, 1, 562, 36, 2, 2, 79, 1, 1, 3, 2))
oamEthernetCapabilities = MibIdentifier((1, 3, 6, 1, 4, 1, 562, 36, 2, 2, 79, 3))
oamEthernetCapabilitiesCA = MibIdentifier((1, 3, 6, 1, 4, 1, 562, 36, 2, 2, 79, 3, 1))
oamEthernetCapabilitiesCA02 = MibIdentifier((1, 3, 6, 1, 4, 1, 562, 36, 2, 2, 79, 3, 1, 3))
oamEthernetCapabilitiesCA02A = MibIdentifier((1, 3, 6, 1, 4, 1, 562, 36, 2, 2, 79, 3, 1, 3, 2))
mibBuilder.exportSymbols("Nortel-MsCarrier-MscPassport-OamEthernetMIB", mscLpOamEnetFrameTooShort=mscLpOamEnetFrameTooShort, mscLpOamEnetMultipleCollisionFrames=mscLpOamEnetMultipleCollisionFrames, mscLpOamEnetOperEntry=mscLpOamEnetOperEntry, mscLpOamEnetOperationalState=mscLpOamEnetOperationalState, mscLpOamEnetStateTable=mscLpOamEnetStateTable, mscLpOamEnetLackOfResourcesDiscards=mscLpOamEnetLackOfResourcesDiscards, oamEthernetGroupCA02=oamEthernetGroupCA02, mscLpOamEnetStatsEntry=mscLpOamEnetStatsEntry, oamEthernetCapabilitiesCA02A=oamEthernetCapabilitiesCA02A, mscLpOamEnetTestCauseOfTermination=mscLpOamEnetTestCauseOfTermination, mscLpOamEnetRowStatusEntry=mscLpOamEnetRowStatusEntry, mscLpOamEnetTestRowStatusTable=mscLpOamEnetTestRowStatusTable, mscLpOamEnetApplicationFramerName=mscLpOamEnetApplicationFramerName, mscLpOamEnetTestOperTable=mscLpOamEnetTestOperTable, mscLpOamEnetCidDataEntry=mscLpOamEnetCidDataEntry, mscLpOamEnetFrameTooLongs=mscLpOamEnetFrameTooLongs, mscLpOamEnetActiveStatus=mscLpOamEnetActiveStatus, mscLpOamEnetOverrunErrors=mscLpOamEnetOverrunErrors, mscLpOamEnetIfIndex=mscLpOamEnetIfIndex, mscLpOamEnetTestRowStatusEntry=mscLpOamEnetTestRowStatusEntry, mscLpOamEnetUsageState=mscLpOamEnetUsageState, mscLpOamEnetTestStorageType=mscLpOamEnetTestStorageType, mscLpOamEnetAdminInfoEntry=mscLpOamEnetAdminInfoEntry, mscLpOamEnetCarrierSenseErrors=mscLpOamEnetCarrierSenseErrors, mscLpOamEnetVendor=mscLpOamEnetVendor, mscLpOamEnetTestResultsTable=mscLpOamEnetTestResultsTable, mscLpOamEnetAdminInfoTable=mscLpOamEnetAdminInfoTable, mscLpOamEnetOamEnetStatsTable=mscLpOamEnetOamEnetStatsTable, oamEthernetCapabilitiesCA02=oamEthernetCapabilitiesCA02, mscLpOamEnetIfAdminStatus=mscLpOamEnetIfAdminStatus, mscLpOamEnetCidDataTable=mscLpOamEnetCidDataTable, mscLpOamEnetOamEnetStatsEntry=mscLpOamEnetOamEnetStatsEntry, oamEthernetGroupCA02A=oamEthernetGroupCA02A, mscLpOamEnetComponentName=mscLpOamEnetComponentName, mscLpOamEnetMacReceiveErrors=mscLpOamEnetMacReceiveErrors, mscLpOamEnetTestOperEntry=mscLpOamEnetTestOperEntry, mscLpOamEnetSingleCollisionFrames=mscLpOamEnetSingleCollisionFrames, mscLpOamEnetStatsTable=mscLpOamEnetStatsTable, mscLpOamEnetOperStatusEntry=mscLpOamEnetOperStatusEntry, mscLpOamEnetExcessiveCollisions=mscLpOamEnetExcessiveCollisions, mscLpOamEnet=mscLpOamEnet, mscLpOamEnetProvTable=mscLpOamEnetProvTable, mscLpOamEnetSqeTestErrors=mscLpOamEnetSqeTestErrors, mscLpOamEnetIfEntryTable=mscLpOamEnetIfEntryTable, mscLpOamEnetFcsErrors=mscLpOamEnetFcsErrors, mscLpOamEnetCustomerIdentifier=mscLpOamEnetCustomerIdentifier, mscLpOamEnetStorageType=mscLpOamEnetStorageType, mscLpOamEnetNumberOfRxCollisions=mscLpOamEnetNumberOfRxCollisions, mscLpOamEnetAdminState=mscLpOamEnetAdminState, mscLpOamEnetExtendedStatistics=mscLpOamEnetExtendedStatistics, mscLpOamEnetMacTransmitErrors=mscLpOamEnetMacTransmitErrors, mscLpOamEnetProvEntry=mscLpOamEnetProvEntry, mscLpOamEnetStandbyStatus=mscLpOamEnetStandbyStatus, mscLpOamEnetLateCollisions=mscLpOamEnetLateCollisions, mscLpOamEnetTestRowStatus=mscLpOamEnetTestRowStatus, oamEthernetGroupCA=oamEthernetGroupCA, mscLpOamEnetTestTestResult=mscLpOamEnetTestTestResult, mscLpOamEnetTestIndex=mscLpOamEnetTestIndex, mscLpOamEnetStateEntry=mscLpOamEnetStateEntry, oamEthernetGroup=oamEthernetGroup, mscLpOamEnetOperStatusTable=mscLpOamEnetOperStatusTable, mscLpOamEnetTestType=mscLpOamEnetTestType, mscLpOamEnetSwitchoverOnFailure=mscLpOamEnetSwitchoverOnFailure, mscLpOamEnetTestResultsEntry=mscLpOamEnetTestResultsEntry, mscLpOamEnetAlignmentErrors=mscLpOamEnetAlignmentErrors, mscLpOamEnetIfEntryEntry=mscLpOamEnetIfEntryEntry, mscLpOamEnetSnmpOperStatus=mscLpOamEnetSnmpOperStatus, oamEthernetCapabilities=oamEthernetCapabilities, oamEthernetMIB=oamEthernetMIB, oamEthernetCapabilitiesCA=oamEthernetCapabilitiesCA, mscLpOamEnetDeferredTransmissions=mscLpOamEnetDeferredTransmissions, mscLpOamEnetRowStatusTable=mscLpOamEnetRowStatusTable, mscLpOamEnetIndex=mscLpOamEnetIndex, mscLpOamEnetTestComponentName=mscLpOamEnetTestComponentName, mscLpOamEnetClearToSendSignalLoss=mscLpOamEnetClearToSendSignalLoss, mscLpOamEnetTest=mscLpOamEnetTest, mscLpOamEnetCommentText=mscLpOamEnetCommentText, mscLpOamEnetRowStatus=mscLpOamEnetRowStatus, mscLpOamEnetOperTable=mscLpOamEnetOperTable, mscLpOamEnetMacAddress=mscLpOamEnetMacAddress)
