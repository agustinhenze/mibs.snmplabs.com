#
# PySNMP MIB module CXFrameRelayATMIWF-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/CXFrameRelayATMIWF-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 18:17:12 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, ConstraintsUnion, ValueSizeConstraint, ConstraintsIntersection, SingleValueConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "ConstraintsUnion", "ValueSizeConstraint", "ConstraintsIntersection", "SingleValueConstraint")
SapIndex, cxFrameRelay = mibBuilder.importSymbols("CXProduct-SMI", "SapIndex", "cxFrameRelay")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
Counter64, ObjectIdentity, ModuleIdentity, NotificationType, Unsigned32, IpAddress, Counter32, Integer32, Gauge32, MibIdentifier, Bits, iso, MibScalar, MibTable, MibTableRow, MibTableColumn, TimeTicks = mibBuilder.importSymbols("SNMPv2-SMI", "Counter64", "ObjectIdentity", "ModuleIdentity", "NotificationType", "Unsigned32", "IpAddress", "Counter32", "Integer32", "Gauge32", "MibIdentifier", "Bits", "iso", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "TimeTicks")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
frpAtmIWFMibLevel = MibScalar((1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 3, 50), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: frpAtmIWFMibLevel.setStatus('mandatory')
frpAtmConnectTimer = MibScalar((1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 3, 51), Integer32().subtype(subtypeSpec=ValueRangeConstraint(3, 600)).clone(10)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: frpAtmConnectTimer.setStatus('mandatory')
frpAtmNISapTable = MibTable((1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 3, 52), )
if mibBuilder.loadTexts: frpAtmNISapTable.setStatus('mandatory')
frpAtmNISapEntry = MibTableRow((1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 3, 52, 1), ).setIndexNames((0, "CXFrameRelayATMIWF-MIB", "frpAtmNISapNumber"))
if mibBuilder.loadTexts: frpAtmNISapEntry.setStatus('mandatory')
frpAtmNISapNumber = MibTableColumn((1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 3, 52, 1, 1), SapIndex()).setMaxAccess("readonly")
if mibBuilder.loadTexts: frpAtmNISapNumber.setStatus('mandatory')
frpAtmNISapState = MibTableColumn((1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 3, 52, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5))).clone(namedValues=NamedValues(("offLine", 1), ("notConnected", 2), ("inProgress", 3), ("connected", 4), ("connectFlowOff", 5)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: frpAtmNISapState.setStatus('mandatory')
frpAtmNIFailureReason = MibTableColumn((1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 3, 52, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 8, 10, 11, 12, 13, 15, 16, 18))).clone(namedValues=NamedValues(("noFailure", 1), ("internalError", 2), ("localAllocFailure", 3), ("remoteAllocFailure", 4), ("localNoAccess", 5), ("remoteNoAccess", 6), ("remotePvcDown", 8), ("remotePvcBusy", 10), ("localFcnFailure", 11), ("remoteFcnFailure", 12), ("localDsnFailure", 13), ("remoteAliasNotFound", 15), ("remoteNoPvcService", 16), ("routeStalled", 18)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: frpAtmNIFailureReason.setStatus('mandatory')
frpAtmNISapDEtoCLPMapping = MibTableColumn((1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 3, 52, 1, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("mode1", 1), ("mode2", 2))).clone('mode1')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: frpAtmNISapDEtoCLPMapping.setStatus('mandatory')
frpAtmNISapCLPtoDEMapping = MibTableColumn((1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 3, 52, 1, 5), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("mode1", 1), ("mode2", 2))).clone('mode1')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: frpAtmNISapCLPtoDEMapping.setStatus('mandatory')
frpAtmNISapCLPBit = MibTableColumn((1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 3, 52, 1, 6), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("zero", 1), ("one", 2))).clone('zero')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: frpAtmNISapCLPBit.setStatus('mandatory')
mibBuilder.exportSymbols("CXFrameRelayATMIWF-MIB", frpAtmNISapDEtoCLPMapping=frpAtmNISapDEtoCLPMapping, frpAtmNISapCLPtoDEMapping=frpAtmNISapCLPtoDEMapping, frpAtmNISapState=frpAtmNISapState, frpAtmNISapCLPBit=frpAtmNISapCLPBit, frpAtmNISapTable=frpAtmNISapTable, frpAtmNISapNumber=frpAtmNISapNumber, frpAtmNISapEntry=frpAtmNISapEntry, frpAtmIWFMibLevel=frpAtmIWFMibLevel, frpAtmNIFailureReason=frpAtmNIFailureReason, frpAtmConnectTimer=frpAtmConnectTimer)
