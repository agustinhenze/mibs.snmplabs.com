#
# PySNMP MIB module DMA200-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/DMA200-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 18:36:13 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
OctetString, ObjectIdentifier, Integer = mibBuilder.importSymbols("ASN1", "OctetString", "ObjectIdentifier", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, SingleValueConstraint, ValueSizeConstraint, ConstraintsIntersection, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "SingleValueConstraint", "ValueSizeConstraint", "ConstraintsIntersection", "ConstraintsUnion")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
MibIdentifier, IpAddress, NotificationType, TimeTicks, Unsigned32, Counter64, iso, Gauge32, ObjectIdentity, Counter32, ModuleIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, NotificationType, Integer32, Bits, enterprises = mibBuilder.importSymbols("SNMPv2-SMI", "MibIdentifier", "IpAddress", "NotificationType", "TimeTicks", "Unsigned32", "Counter64", "iso", "Gauge32", "ObjectIdentity", "Counter32", "ModuleIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "NotificationType", "Integer32", "Bits", "enterprises")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
gdc = MibIdentifier((1, 3, 6, 1, 4, 1, 498))
sc = MibIdentifier((1, 3, 6, 1, 4, 1, 498, 3))
dmaSystem = MibIdentifier((1, 3, 6, 1, 4, 1, 498, 3, 7))
dmaMaster = MibIdentifier((1, 3, 6, 1, 4, 1, 498, 3, 7, 1))
dmaMasterFSterminate = MibScalar((1, 3, 6, 1, 4, 1, 498, 3, 7, 1, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1))).clone(namedValues=NamedValues(("disconnect", 1)))).setMaxAccess("writeonly")
if mibBuilder.loadTexts: dmaMasterFSterminate.setStatus('mandatory')
dmaMasterSupvAccess = MibScalar((1, 3, 6, 1, 4, 1, 498, 3, 7, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("none", 1), ("local", 2), ("global", 3)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: dmaMasterSupvAccess.setStatus('mandatory')
dmaMasterModemCmd = MibScalar((1, 3, 6, 1, 4, 1, 498, 3, 7, 1, 3), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 256))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: dmaMasterModemCmd.setStatus('mandatory')
dmaMasterDialPrefix = MibScalar((1, 3, 6, 1, 4, 1, 498, 3, 7, 1, 4), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 16))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: dmaMasterDialPrefix.setStatus('mandatory')
dmaMasterDialPhoneNumber = MibScalar((1, 3, 6, 1, 4, 1, 498, 3, 7, 1, 5), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 16))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: dmaMasterDialPhoneNumber.setStatus('mandatory')
dmaMasterDialing = MibScalar((1, 3, 6, 1, 4, 1, 498, 3, 7, 1, 6), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("connect", 1), ("disconnect", 2)))).setMaxAccess("writeonly")
if mibBuilder.loadTexts: dmaMasterDialing.setStatus('mandatory')
dmaMasterDialPortStatus = MibScalar((1, 3, 6, 1, 4, 1, 498, 3, 7, 1, 7), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("readyOffline", 1), ("dialing", 2), ("connectedOnline", 3)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: dmaMasterDialPortStatus.setStatus('mandatory')
dmaMasterResumeScan = MibScalar((1, 3, 6, 1, 4, 1, 498, 3, 7, 1, 8), Integer32()).setMaxAccess("writeonly")
if mibBuilder.loadTexts: dmaMasterResumeScan.setStatus('mandatory')
dmaMasterScanCtrl = MibScalar((1, 3, 6, 1, 4, 1, 498, 3, 7, 1, 9), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("dmaScanOff", 1), ("dmaScanOn", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: dmaMasterScanCtrl.setStatus('mandatory')
dmaNode = MibIdentifier((1, 3, 6, 1, 4, 1, 498, 3, 7, 2))
dmaNodeNum = MibScalar((1, 3, 6, 1, 4, 1, 498, 3, 7, 2, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dmaNodeNum.setStatus('mandatory')
dmaNodeTable = MibTable((1, 3, 6, 1, 4, 1, 498, 3, 7, 2, 2), )
if mibBuilder.loadTexts: dmaNodeTable.setStatus('mandatory')
dmaNodeEntry = MibTableRow((1, 3, 6, 1, 4, 1, 498, 3, 7, 2, 2, 1), ).setIndexNames((0, "DMA200-MIB", "dmaNodeIndex"))
if mibBuilder.loadTexts: dmaNodeEntry.setStatus('mandatory')
dmaNodeIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 498, 3, 7, 2, 2, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 20))).setMaxAccess("readonly")
if mibBuilder.loadTexts: dmaNodeIndex.setStatus('mandatory')
dmaNodeValid = MibTableColumn((1, 3, 6, 1, 4, 1, 498, 3, 7, 2, 2, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("valid", 1), ("invalid", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: dmaNodeValid.setStatus('mandatory')
dmaNodePhoneNumber = MibTableColumn((1, 3, 6, 1, 4, 1, 498, 3, 7, 2, 2, 1, 3), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 16))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: dmaNodePhoneNumber.setStatus('mandatory')
dmaNodeName = MibTableColumn((1, 3, 6, 1, 4, 1, 498, 3, 7, 2, 2, 1, 4), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 8))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: dmaNodeName.setStatus('mandatory')
dmaElement = MibIdentifier((1, 3, 6, 1, 4, 1, 498, 3, 7, 3))
dmaElementConfigTable = MibTable((1, 3, 6, 1, 4, 1, 498, 3, 7, 3, 1), )
if mibBuilder.loadTexts: dmaElementConfigTable.setStatus('mandatory')
dmaElementEntry = MibTableRow((1, 3, 6, 1, 4, 1, 498, 3, 7, 3, 1, 1), ).setIndexNames((0, "DMA200-MIB", "dmaElementIndex"))
if mibBuilder.loadTexts: dmaElementEntry.setStatus('mandatory')
dmaElementIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 498, 3, 7, 3, 1, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 255))).setMaxAccess("readonly")
if mibBuilder.loadTexts: dmaElementIndex.setStatus('mandatory')
dmaElementRemoteIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 498, 3, 7, 3, 1, 1, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 255))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: dmaElementRemoteIndex.setStatus('mandatory')
dmaElementValid = MibTableColumn((1, 3, 6, 1, 4, 1, 498, 3, 7, 3, 1, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("valid", 1), ("invalid", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: dmaElementValid.setStatus('mandatory')
dmaElementType = MibTableColumn((1, 3, 6, 1, 4, 1, 498, 3, 7, 3, 1, 1, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6))).clone(namedValues=NamedValues(("other", 1), ("dc551", 2), ("dc552A", 3), ("dc552A-1", 4), ("dc552A-V11", 5), ("dc552A-1-V11", 6)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: dmaElementType.setStatus('mandatory')
dmaElementStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 498, 3, 7, 3, 1, 1, 5), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 8, 9, 10))).clone(namedValues=NamedValues(("statusOK", 1), ("statusMajor", 2), ("statusMinor", 3), ("statusNotResponding", 4), ("statusCommErr", 5), ("statusMismatchDC551", 6), ("statusMismatchDC552A", 7), ("statusMismatchDC552A-1", 8), ("statusMismatchDC552A-V11", 9), ("statusMismatchDC552A-1-V11", 10)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: dmaElementStatus.setStatus('mandatory')
dmaElementNode = MibTableColumn((1, 3, 6, 1, 4, 1, 498, 3, 7, 3, 1, 1, 6), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: dmaElementNode.setStatus('mandatory')
dmaAccess = NotificationType((1, 3, 6, 1, 4, 1, 498, 3, 7) + (0,1)).setObjects(("DMA200-MIB", "dmaMasterSupvAccess"))
dmaElementAlarm = NotificationType((1, 3, 6, 1, 4, 1, 498, 3, 7) + (0,2)).setObjects(("DMA200-MIB", "dmaElementIndex"), ("DMA200-MIB", "dmaElementType"), ("DMA200-MIB", "dmaElementStatus"), ("DMA200-MIB", "dmaNodeName"))
mibBuilder.exportSymbols("DMA200-MIB", dmaMasterFSterminate=dmaMasterFSterminate, dmaElementIndex=dmaElementIndex, dmaMasterModemCmd=dmaMasterModemCmd, dmaSystem=dmaSystem, dmaNodeTable=dmaNodeTable, dmaElementConfigTable=dmaElementConfigTable, dmaElement=dmaElement, dmaElementType=dmaElementType, dmaElementNode=dmaElementNode, dmaMasterDialPhoneNumber=dmaMasterDialPhoneNumber, dmaNode=dmaNode, dmaMaster=dmaMaster, dmaElementRemoteIndex=dmaElementRemoteIndex, gdc=gdc, dmaElementAlarm=dmaElementAlarm, dmaAccess=dmaAccess, dmaNodeEntry=dmaNodeEntry, dmaNodeNum=dmaNodeNum, dmaElementStatus=dmaElementStatus, dmaMasterSupvAccess=dmaMasterSupvAccess, dmaNodePhoneNumber=dmaNodePhoneNumber, dmaElementEntry=dmaElementEntry, dmaNodeValid=dmaNodeValid, dmaMasterDialPortStatus=dmaMasterDialPortStatus, dmaMasterResumeScan=dmaMasterResumeScan, dmaNodeName=dmaNodeName, dmaMasterDialing=dmaMasterDialing, sc=sc, dmaNodeIndex=dmaNodeIndex, dmaMasterScanCtrl=dmaMasterScanCtrl, dmaElementValid=dmaElementValid, dmaMasterDialPrefix=dmaMasterDialPrefix)