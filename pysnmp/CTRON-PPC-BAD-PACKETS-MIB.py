#
# PySNMP MIB module CTRON-PPC-BAD-PACKETS-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/CTRON-PPC-BAD-PACKETS-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 18:14:50 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ValueRangeConstraint, ConstraintsIntersection, ConstraintsUnion, SingleValueConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ValueRangeConstraint", "ConstraintsIntersection", "ConstraintsUnion", "SingleValueConstraint")
ctFWDebug, = mibBuilder.importSymbols("CTRON-MIB-NAMES", "ctFWDebug")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
Gauge32, ObjectIdentity, TimeTicks, Counter32, Unsigned32, Integer32, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter64, MibIdentifier, NotificationType, ModuleIdentity, IpAddress, iso, Bits = mibBuilder.importSymbols("SNMPv2-SMI", "Gauge32", "ObjectIdentity", "TimeTicks", "Counter32", "Unsigned32", "Integer32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter64", "MibIdentifier", "NotificationType", "ModuleIdentity", "IpAddress", "iso", "Bits")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
ctPPCBadPkts = MibIdentifier((1, 3, 6, 1, 4, 1, 52, 4, 2, 29, 1))
ctPPCBadPktsTotalTx = MibScalar((1, 3, 6, 1, 4, 1, 52, 4, 2, 29, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ctPPCBadPktsTotalTx.setStatus('mandatory')
ctPPCBadPktsTotalRx = MibScalar((1, 3, 6, 1, 4, 1, 52, 4, 2, 29, 1, 2), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ctPPCBadPktsTotalRx.setStatus('mandatory')
ctPPCBadPktsTxTable = MibTable((1, 3, 6, 1, 4, 1, 52, 4, 2, 29, 1, 3), )
if mibBuilder.loadTexts: ctPPCBadPktsTxTable.setStatus('mandatory')
ctPPCBadPktsTxEntry = MibTableRow((1, 3, 6, 1, 4, 1, 52, 4, 2, 29, 1, 3, 1), ).setIndexNames((0, "CTRON-PPC-BAD-PACKETS-MIB", "ctPPCBadPktsTxIndex"))
if mibBuilder.loadTexts: ctPPCBadPktsTxEntry.setStatus('mandatory')
ctPPCBadPktsTxIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 2, 29, 1, 3, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ctPPCBadPktsTxIndex.setStatus('mandatory')
ctPPCBadPktsTxQueues = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 2, 29, 1, 3, 1, 2), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ctPPCBadPktsTxQueues.setStatus('mandatory')
ctPPCBadPktsTxFulls = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 2, 29, 1, 3, 1, 3), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ctPPCBadPktsTxFulls.setStatus('mandatory')
ctPPCBadPktsTxQDepthTable = MibTable((1, 3, 6, 1, 4, 1, 52, 4, 2, 29, 1, 4), )
if mibBuilder.loadTexts: ctPPCBadPktsTxQDepthTable.setStatus('mandatory')
ctPPCBadPktsTxQDepthEntry = MibTableRow((1, 3, 6, 1, 4, 1, 52, 4, 2, 29, 1, 4, 1), ).setIndexNames((0, "CTRON-PPC-BAD-PACKETS-MIB", "ctPPCBadPktsTxQIndex"), (0, "CTRON-PPC-BAD-PACKETS-MIB", "ctPPCBadPktsQ"))
if mibBuilder.loadTexts: ctPPCBadPktsTxQDepthEntry.setStatus('mandatory')
ctPPCBadPktsTxQIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 2, 29, 1, 4, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ctPPCBadPktsTxQIndex.setStatus('mandatory')
ctPPCBadPktsQ = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 2, 29, 1, 4, 1, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 3))).setMaxAccess("readonly")
if mibBuilder.loadTexts: ctPPCBadPktsQ.setStatus('mandatory')
ctPPCBadPktsTxQDepth = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 2, 29, 1, 4, 1, 3), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ctPPCBadPktsTxQDepth.setStatus('mandatory')
ctPPCBadPktsRxTable = MibTable((1, 3, 6, 1, 4, 1, 52, 4, 2, 29, 1, 5), )
if mibBuilder.loadTexts: ctPPCBadPktsRxTable.setStatus('mandatory')
ctPPCBadPktsRxEntry = MibTableRow((1, 3, 6, 1, 4, 1, 52, 4, 2, 29, 1, 5, 1), ).setIndexNames((0, "CTRON-PPC-BAD-PACKETS-MIB", "ctPPCBadPktsRxIndex"))
if mibBuilder.loadTexts: ctPPCBadPktsRxEntry.setStatus('mandatory')
ctPPCBadPktsRxIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 2, 29, 1, 5, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ctPPCBadPktsRxIndex.setStatus('mandatory')
ctPPCBadPktsRxTotalErrors = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 2, 29, 1, 5, 1, 2), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ctPPCBadPktsRxTotalErrors.setStatus('mandatory')
ctPPCBadPktsRxDescHigh = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 2, 29, 1, 5, 1, 3), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ctPPCBadPktsRxDescHigh.setStatus('mandatory')
ctPPCBadPktsRxDescLow = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 2, 29, 1, 5, 1, 4), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ctPPCBadPktsRxDescLow.setStatus('mandatory')
ctPPCBadPktsRxDaSa0 = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 2, 29, 1, 5, 1, 5), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ctPPCBadPktsRxDaSa0.setStatus('mandatory')
ctPPCBadPktsRxDaSa1 = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 2, 29, 1, 5, 1, 6), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ctPPCBadPktsRxDaSa1.setStatus('mandatory')
ctPPCBadPktsRxDaSa2 = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 2, 29, 1, 5, 1, 7), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ctPPCBadPktsRxDaSa2.setStatus('mandatory')
ctPPCBadPktsRxData = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 2, 29, 1, 5, 1, 8), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ctPPCBadPktsRxData.setStatus('mandatory')
mibBuilder.exportSymbols("CTRON-PPC-BAD-PACKETS-MIB", ctPPCBadPktsQ=ctPPCBadPktsQ, ctPPCBadPktsRxDaSa1=ctPPCBadPktsRxDaSa1, ctPPCBadPktsTxTable=ctPPCBadPktsTxTable, ctPPCBadPktsTxQDepthTable=ctPPCBadPktsTxQDepthTable, ctPPCBadPktsTotalTx=ctPPCBadPktsTotalTx, ctPPCBadPktsTxQDepth=ctPPCBadPktsTxQDepth, ctPPCBadPktsRxDaSa2=ctPPCBadPktsRxDaSa2, ctPPCBadPktsRxData=ctPPCBadPktsRxData, ctPPCBadPkts=ctPPCBadPkts, ctPPCBadPktsRxDescLow=ctPPCBadPktsRxDescLow, ctPPCBadPktsRxDaSa0=ctPPCBadPktsRxDaSa0, ctPPCBadPktsTxEntry=ctPPCBadPktsTxEntry, ctPPCBadPktsTxQueues=ctPPCBadPktsTxQueues, ctPPCBadPktsTxIndex=ctPPCBadPktsTxIndex, ctPPCBadPktsRxEntry=ctPPCBadPktsRxEntry, ctPPCBadPktsTxFulls=ctPPCBadPktsTxFulls, ctPPCBadPktsRxTable=ctPPCBadPktsRxTable, ctPPCBadPktsTxQIndex=ctPPCBadPktsTxQIndex, ctPPCBadPktsRxTotalErrors=ctPPCBadPktsRxTotalErrors, ctPPCBadPktsTotalRx=ctPPCBadPktsTotalRx, ctPPCBadPktsRxDescHigh=ctPPCBadPktsRxDescHigh, ctPPCBadPktsTxQDepthEntry=ctPPCBadPktsTxQDepthEntry, ctPPCBadPktsRxIndex=ctPPCBadPktsRxIndex)