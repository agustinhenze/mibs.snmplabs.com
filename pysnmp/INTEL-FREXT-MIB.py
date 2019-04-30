#
# PySNMP MIB module INTEL-FREXT-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/INTEL-FREXT-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 19:42:58 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
SingleValueConstraint, ValueSizeConstraint, ConstraintsIntersection, ValueRangeConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "SingleValueConstraint", "ValueSizeConstraint", "ConstraintsIntersection", "ValueRangeConstraint", "ConstraintsUnion")
DLCI, = mibBuilder.importSymbols("FRAME-RELAY-DTE-MIB", "DLCI")
mib2ext, = mibBuilder.importSymbols("INTEL-GEN-MIB", "mib2ext")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
Integer32, Unsigned32, Bits, Gauge32, TimeTicks, ObjectIdentity, NotificationType, iso, Counter32, IpAddress, Counter64, ModuleIdentity, MibIdentifier, MibScalar, MibTable, MibTableRow, MibTableColumn = mibBuilder.importSymbols("SNMPv2-SMI", "Integer32", "Unsigned32", "Bits", "Gauge32", "TimeTicks", "ObjectIdentity", "NotificationType", "iso", "Counter32", "IpAddress", "Counter64", "ModuleIdentity", "MibIdentifier", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
frEx = MibIdentifier((1, 3, 6, 1, 4, 1, 343, 6, 28))
frCircuitExt = MibIdentifier((1, 3, 6, 1, 4, 1, 343, 6, 28, 1))
class InterfaceIndex(Integer32):
    pass

frCirExtEncTable = MibTable((1, 3, 6, 1, 4, 1, 343, 6, 28, 1, 1), )
if mibBuilder.loadTexts: frCirExtEncTable.setStatus('mandatory')
frCirExtEncEntry = MibTableRow((1, 3, 6, 1, 4, 1, 343, 6, 28, 1, 1, 1), ).setIndexNames((0, "INTEL-FREXT-MIB", "frCirExtEncIfIndex"), (0, "INTEL-FREXT-MIB", "frCirExtEncDlci"))
if mibBuilder.loadTexts: frCirExtEncEntry.setStatus('mandatory')
frCirExtEncIfIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 343, 6, 28, 1, 1, 1, 1), InterfaceIndex()).setMaxAccess("readonly")
if mibBuilder.loadTexts: frCirExtEncIfIndex.setStatus('mandatory')
frCirExtEncDlci = MibTableColumn((1, 3, 6, 1, 4, 1, 343, 6, 28, 1, 1, 1, 2), DLCI()).setMaxAccess("readonly")
if mibBuilder.loadTexts: frCirExtEncDlci.setStatus('mandatory')
frCirExtEncLogicalIfIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 343, 6, 28, 1, 1, 1, 3), InterfaceIndex()).setMaxAccess("readonly")
if mibBuilder.loadTexts: frCirExtEncLogicalIfIndex.setStatus('mandatory')
frCirExtEncEnabled = MibTableColumn((1, 3, 6, 1, 4, 1, 343, 6, 28, 1, 1, 1, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("no", 1), ("yes", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: frCirExtEncEnabled.setStatus('mandatory')
frCirExtEncNegotiated = MibTableColumn((1, 3, 6, 1, 4, 1, 343, 6, 28, 1, 1, 1, 5), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("no", 1), ("yes", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: frCirExtEncNegotiated.setStatus('mandatory')
frCirExtEncResetRequestsRx = MibTableColumn((1, 3, 6, 1, 4, 1, 343, 6, 28, 1, 1, 1, 6), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: frCirExtEncResetRequestsRx.setStatus('mandatory')
frCirExtEncResetRequestsTx = MibTableColumn((1, 3, 6, 1, 4, 1, 343, 6, 28, 1, 1, 1, 7), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: frCirExtEncResetRequestsTx.setStatus('mandatory')
frCirExtEncResetAcksRx = MibTableColumn((1, 3, 6, 1, 4, 1, 343, 6, 28, 1, 1, 1, 8), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: frCirExtEncResetAcksRx.setStatus('mandatory')
frCirExtEncResetAcksTx = MibTableColumn((1, 3, 6, 1, 4, 1, 343, 6, 28, 1, 1, 1, 9), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: frCirExtEncResetAcksTx.setStatus('mandatory')
frCirExtEncRxDiscarded = MibTableColumn((1, 3, 6, 1, 4, 1, 343, 6, 28, 1, 1, 1, 10), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: frCirExtEncRxDiscarded.setStatus('mandatory')
frCirExtEncTxDiscarded = MibTableColumn((1, 3, 6, 1, 4, 1, 343, 6, 28, 1, 1, 1, 11), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: frCirExtEncTxDiscarded.setStatus('mandatory')
frCirExtEncReceiverState = MibTableColumn((1, 3, 6, 1, 4, 1, 343, 6, 28, 1, 1, 1, 12), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("ok", 1), ("error", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: frCirExtEncReceiverState.setStatus('mandatory')
frCirExtCompTable = MibTable((1, 3, 6, 1, 4, 1, 343, 6, 28, 1, 2), )
if mibBuilder.loadTexts: frCirExtCompTable.setStatus('mandatory')
frCirExtCompEntry = MibTableRow((1, 3, 6, 1, 4, 1, 343, 6, 28, 1, 2, 1), ).setIndexNames((0, "INTEL-FREXT-MIB", "frCirExtCompIfIndex"), (0, "INTEL-FREXT-MIB", "frCirExtCompDlci"))
if mibBuilder.loadTexts: frCirExtCompEntry.setStatus('mandatory')
frCirExtCompIfIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 343, 6, 28, 1, 2, 1, 1), InterfaceIndex()).setMaxAccess("readonly")
if mibBuilder.loadTexts: frCirExtCompIfIndex.setStatus('mandatory')
frCirExtCompDlci = MibTableColumn((1, 3, 6, 1, 4, 1, 343, 6, 28, 1, 2, 1, 2), DLCI()).setMaxAccess("readonly")
if mibBuilder.loadTexts: frCirExtCompDlci.setStatus('mandatory')
frCirExtCompLogicalIfIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 343, 6, 28, 1, 2, 1, 3), InterfaceIndex()).setMaxAccess("readonly")
if mibBuilder.loadTexts: frCirExtCompLogicalIfIndex.setStatus('mandatory')
frCirExtCompEnabled = MibTableColumn((1, 3, 6, 1, 4, 1, 343, 6, 28, 1, 2, 1, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("no", 1), ("yes", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: frCirExtCompEnabled.setStatus('mandatory')
frCirExtCompNegotiated = MibTableColumn((1, 3, 6, 1, 4, 1, 343, 6, 28, 1, 2, 1, 5), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("no", 1), ("yes", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: frCirExtCompNegotiated.setStatus('mandatory')
frCirExtCompDecoderBytesIn = MibTableColumn((1, 3, 6, 1, 4, 1, 343, 6, 28, 1, 2, 1, 6), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: frCirExtCompDecoderBytesIn.setStatus('mandatory')
frCirExtCompDecoderDecompBytesOut = MibTableColumn((1, 3, 6, 1, 4, 1, 343, 6, 28, 1, 2, 1, 7), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: frCirExtCompDecoderDecompBytesOut.setStatus('mandatory')
frCirExtCompDecoderUncompBytesOut = MibTableColumn((1, 3, 6, 1, 4, 1, 343, 6, 28, 1, 2, 1, 8), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: frCirExtCompDecoderUncompBytesOut.setStatus('mandatory')
frCirExtCompDecoderCompPacketsIn = MibTableColumn((1, 3, 6, 1, 4, 1, 343, 6, 28, 1, 2, 1, 9), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: frCirExtCompDecoderCompPacketsIn.setStatus('mandatory')
frCirExtCompDecoderUncompPacketsIn = MibTableColumn((1, 3, 6, 1, 4, 1, 343, 6, 28, 1, 2, 1, 10), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: frCirExtCompDecoderUncompPacketsIn.setStatus('mandatory')
frCirExtCompDecoderDecompQueueLength = MibTableColumn((1, 3, 6, 1, 4, 1, 343, 6, 28, 1, 2, 1, 11), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: frCirExtCompDecoderDecompQueueLength.setStatus('mandatory')
frCirExtCompDecoderCompressionRatio = MibTableColumn((1, 3, 6, 1, 4, 1, 343, 6, 28, 1, 2, 1, 12), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: frCirExtCompDecoderCompressionRatio.setStatus('mandatory')
frCirExtCompDecoderResetRequestTx = MibTableColumn((1, 3, 6, 1, 4, 1, 343, 6, 28, 1, 2, 1, 13), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: frCirExtCompDecoderResetRequestTx.setStatus('mandatory')
frCirExtCompDecoderResetAcksRx = MibTableColumn((1, 3, 6, 1, 4, 1, 343, 6, 28, 1, 2, 1, 14), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: frCirExtCompDecoderResetAcksRx.setStatus('mandatory')
frCirExtCompDecoderRxDiscarded = MibTableColumn((1, 3, 6, 1, 4, 1, 343, 6, 28, 1, 2, 1, 15), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: frCirExtCompDecoderRxDiscarded.setStatus('mandatory')
frCirExtCompDecoderState = MibTableColumn((1, 3, 6, 1, 4, 1, 343, 6, 28, 1, 2, 1, 16), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("ok", 1), ("error", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: frCirExtCompDecoderState.setStatus('mandatory')
frCirExtCompEncoderBytesIn = MibTableColumn((1, 3, 6, 1, 4, 1, 343, 6, 28, 1, 2, 1, 17), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: frCirExtCompEncoderBytesIn.setStatus('mandatory')
frCirExtCompEncoderCompBytesOut = MibTableColumn((1, 3, 6, 1, 4, 1, 343, 6, 28, 1, 2, 1, 18), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: frCirExtCompEncoderCompBytesOut.setStatus('mandatory')
frCirExtCompEncoderUncompBytesOut = MibTableColumn((1, 3, 6, 1, 4, 1, 343, 6, 28, 1, 2, 1, 19), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: frCirExtCompEncoderUncompBytesOut.setStatus('mandatory')
frCirExtCompEncoderCompPacketsOut = MibTableColumn((1, 3, 6, 1, 4, 1, 343, 6, 28, 1, 2, 1, 20), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: frCirExtCompEncoderCompPacketsOut.setStatus('mandatory')
frCirExtCompEncoderUncompPacketsOut = MibTableColumn((1, 3, 6, 1, 4, 1, 343, 6, 28, 1, 2, 1, 21), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: frCirExtCompEncoderUncompPacketsOut.setStatus('mandatory')
frCirExtCompEncoderCompQueueLength = MibTableColumn((1, 3, 6, 1, 4, 1, 343, 6, 28, 1, 2, 1, 22), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: frCirExtCompEncoderCompQueueLength.setStatus('mandatory')
frCirExtCompEncoderCompressionRation = MibTableColumn((1, 3, 6, 1, 4, 1, 343, 6, 28, 1, 2, 1, 23), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: frCirExtCompEncoderCompressionRation.setStatus('mandatory')
frCirExtCompEncoderResetRequestRx = MibTableColumn((1, 3, 6, 1, 4, 1, 343, 6, 28, 1, 2, 1, 24), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: frCirExtCompEncoderResetRequestRx.setStatus('mandatory')
frCirExtCompEncoderResetAckTx = MibTableColumn((1, 3, 6, 1, 4, 1, 343, 6, 28, 1, 2, 1, 25), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: frCirExtCompEncoderResetAckTx.setStatus('mandatory')
frCirExtCompEncoderTxDiscarded = MibTableColumn((1, 3, 6, 1, 4, 1, 343, 6, 28, 1, 2, 1, 26), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: frCirExtCompEncoderTxDiscarded.setStatus('mandatory')
mibBuilder.exportSymbols("INTEL-FREXT-MIB", frCirExtEncLogicalIfIndex=frCirExtEncLogicalIfIndex, frCirExtEncTable=frCirExtEncTable, frCirExtCompEncoderCompPacketsOut=frCirExtCompEncoderCompPacketsOut, InterfaceIndex=InterfaceIndex, frCirExtCompNegotiated=frCirExtCompNegotiated, frCirExtEncIfIndex=frCirExtEncIfIndex, frCirExtEncResetAcksTx=frCirExtEncResetAcksTx, frCirExtCompEncoderTxDiscarded=frCirExtCompEncoderTxDiscarded, frCirExtCompDecoderState=frCirExtCompDecoderState, frCirExtCompDecoderUncompBytesOut=frCirExtCompDecoderUncompBytesOut, frCirExtCompEncoderResetRequestRx=frCirExtCompEncoderResetRequestRx, frCirExtCompDecoderUncompPacketsIn=frCirExtCompDecoderUncompPacketsIn, frCirExtCompDecoderResetAcksRx=frCirExtCompDecoderResetAcksRx, frCircuitExt=frCircuitExt, frCirExtEncDlci=frCirExtEncDlci, frCirExtCompDecoderCompPacketsIn=frCirExtCompDecoderCompPacketsIn, frCirExtEncEnabled=frCirExtEncEnabled, frCirExtCompEncoderUncompPacketsOut=frCirExtCompEncoderUncompPacketsOut, frCirExtEncResetRequestsRx=frCirExtEncResetRequestsRx, frCirExtCompEncoderBytesIn=frCirExtCompEncoderBytesIn, frCirExtEncResetRequestsTx=frCirExtEncResetRequestsTx, frCirExtCompDecoderCompressionRatio=frCirExtCompDecoderCompressionRatio, frCirExtEncRxDiscarded=frCirExtEncRxDiscarded, frCirExtCompIfIndex=frCirExtCompIfIndex, frCirExtCompEncoderResetAckTx=frCirExtCompEncoderResetAckTx, frCirExtCompDecoderRxDiscarded=frCirExtCompDecoderRxDiscarded, frCirExtCompEncoderCompBytesOut=frCirExtCompEncoderCompBytesOut, frCirExtCompTable=frCirExtCompTable, frCirExtCompDecoderDecompBytesOut=frCirExtCompDecoderDecompBytesOut, frCirExtEncEntry=frCirExtEncEntry, frCirExtEncReceiverState=frCirExtEncReceiverState, frCirExtCompEncoderCompQueueLength=frCirExtCompEncoderCompQueueLength, frCirExtCompLogicalIfIndex=frCirExtCompLogicalIfIndex, frCirExtCompEncoderUncompBytesOut=frCirExtCompEncoderUncompBytesOut, frCirExtCompEncoderCompressionRation=frCirExtCompEncoderCompressionRation, frCirExtCompDlci=frCirExtCompDlci, frEx=frEx, frCirExtCompDecoderDecompQueueLength=frCirExtCompDecoderDecompQueueLength, frCirExtCompDecoderResetRequestTx=frCirExtCompDecoderResetRequestTx, frCirExtEncResetAcksRx=frCirExtEncResetAcksRx, frCirExtEncNegotiated=frCirExtEncNegotiated, frCirExtEncTxDiscarded=frCirExtEncTxDiscarded, frCirExtCompEnabled=frCirExtCompEnabled, frCirExtCompDecoderBytesIn=frCirExtCompDecoderBytesIn, frCirExtCompEntry=frCirExtCompEntry)