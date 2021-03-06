#
# PySNMP MIB module NMS-FLASH (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/NMS-FLASH
# Produced by pysmi-0.3.4 at Mon Apr 29 20:12:19 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
OctetString, ObjectIdentifier, Integer = mibBuilder.importSymbols("ASN1", "OctetString", "ObjectIdentifier", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, SingleValueConstraint, ConstraintsUnion, ValueRangeConstraint, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "SingleValueConstraint", "ConstraintsUnion", "ValueRangeConstraint", "ValueSizeConstraint")
nmslocal, = mibBuilder.importSymbols("NMS-SMI", "nmslocal")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
TimeTicks, NotificationType, iso, Unsigned32, Bits, Gauge32, MibIdentifier, ObjectIdentity, Counter32, ModuleIdentity, IpAddress, Integer32, Counter64, MibScalar, MibTable, MibTableRow, MibTableColumn = mibBuilder.importSymbols("SNMPv2-SMI", "TimeTicks", "NotificationType", "iso", "Unsigned32", "Bits", "Gauge32", "MibIdentifier", "ObjectIdentity", "Counter32", "ModuleIdentity", "IpAddress", "Integer32", "Counter64", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
nmslflash = MibIdentifier((1, 3, 6, 1, 4, 1, 11606, 10, 2, 10))
nmsflashSize = MibScalar((1, 3, 6, 1, 4, 1, 11606, 10, 2, 10, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: nmsflashSize.setStatus('mandatory')
nmsflashFree = MibScalar((1, 3, 6, 1, 4, 1, 11606, 10, 2, 10, 2), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: nmsflashFree.setStatus('mandatory')
nmsflashController = MibScalar((1, 3, 6, 1, 4, 1, 11606, 10, 2, 10, 3), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: nmsflashController.setStatus('mandatory')
nmsflashCard = MibScalar((1, 3, 6, 1, 4, 1, 11606, 10, 2, 10, 4), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: nmsflashCard.setStatus('mandatory')
nmsflashVPP = MibScalar((1, 3, 6, 1, 4, 1, 11606, 10, 2, 10, 5), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("installed", 1), ("missing", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: nmsflashVPP.setStatus('mandatory')
nmsflashErase = MibScalar((1, 3, 6, 1, 4, 1, 11606, 10, 2, 10, 6), Integer32()).setMaxAccess("writeonly")
if mibBuilder.loadTexts: nmsflashErase.setStatus('mandatory')
nmsflashEraseTime = MibScalar((1, 3, 6, 1, 4, 1, 11606, 10, 2, 10, 7), TimeTicks()).setMaxAccess("readonly")
if mibBuilder.loadTexts: nmsflashEraseTime.setStatus('mandatory')
nmsflashEraseStatus = MibScalar((1, 3, 6, 1, 4, 1, 11606, 10, 2, 10, 8), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7))).clone(namedValues=NamedValues(("flashOpInProgress", 1), ("flashOpSuccess", 2), ("flashOpFailure", 3), ("flashReadOnly", 4), ("flashOpenFailure", 5), ("bufferAllocationFailure", 6), ("noOpAfterPowerOn", 7)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: nmsflashEraseStatus.setStatus('mandatory')
nmsflashToNet = MibScalar((1, 3, 6, 1, 4, 1, 11606, 10, 2, 10, 9), DisplayString()).setMaxAccess("writeonly")
if mibBuilder.loadTexts: nmsflashToNet.setStatus('mandatory')
nmsflashToNetTime = MibScalar((1, 3, 6, 1, 4, 1, 11606, 10, 2, 10, 10), TimeTicks()).setMaxAccess("readonly")
if mibBuilder.loadTexts: nmsflashToNetTime.setStatus('mandatory')
nmsflashToNetStatus = MibScalar((1, 3, 6, 1, 4, 1, 11606, 10, 2, 10, 11), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7))).clone(namedValues=NamedValues(("flashOpInProgress", 1), ("flashOpSuccess", 2), ("flashOpFailure", 3), ("flashReadOnly", 4), ("flashOpenFailure", 5), ("bufferAllocationFailure", 6), ("noOpAfterPowerOn", 7)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: nmsflashToNetStatus.setStatus('mandatory')
nmsnetToFlash = MibScalar((1, 3, 6, 1, 4, 1, 11606, 10, 2, 10, 12), DisplayString()).setMaxAccess("writeonly")
if mibBuilder.loadTexts: nmsnetToFlash.setStatus('mandatory')
nmsnetToFlashTime = MibScalar((1, 3, 6, 1, 4, 1, 11606, 10, 2, 10, 13), TimeTicks()).setMaxAccess("readonly")
if mibBuilder.loadTexts: nmsnetToFlashTime.setStatus('mandatory')
nmsnetToFlashStatus = MibScalar((1, 3, 6, 1, 4, 1, 11606, 10, 2, 10, 14), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7))).clone(namedValues=NamedValues(("flashOpInProgress", 1), ("flashOpSuccess", 2), ("flashOpFailure", 3), ("flashReadOnly", 4), ("flashOpenFailure", 5), ("bufferAllocationFailure", 6), ("noOpAfterPowerOn", 7)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: nmsnetToFlashStatus.setStatus('mandatory')
nmsflashStatus = MibScalar((1, 3, 6, 1, 4, 1, 11606, 10, 2, 10, 15), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("busy", 1), ("available", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: nmsflashStatus.setStatus('mandatory')
nmsflashEntries = MibScalar((1, 3, 6, 1, 4, 1, 11606, 10, 2, 10, 16), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: nmsflashEntries.setStatus('mandatory')
nmslflashFileDirTable = MibTable((1, 3, 6, 1, 4, 1, 11606, 10, 2, 10, 17), )
if mibBuilder.loadTexts: nmslflashFileDirTable.setStatus('mandatory')
nmslflashFileDirEntry = MibTableRow((1, 3, 6, 1, 4, 1, 11606, 10, 2, 10, 17, 1), ).setIndexNames((0, "NMS-FLASH", "flashEntries"))
if mibBuilder.loadTexts: nmslflashFileDirEntry.setStatus('mandatory')
nmsflashDirName = MibTableColumn((1, 3, 6, 1, 4, 1, 11606, 10, 2, 10, 17, 1, 1), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: nmsflashDirName.setStatus('mandatory')
nmsflashDirSize = MibTableColumn((1, 3, 6, 1, 4, 1, 11606, 10, 2, 10, 17, 1, 2), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: nmsflashDirSize.setStatus('mandatory')
nmsflashDirStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 11606, 10, 2, 10, 17, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("valid", 1), ("deleted", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: nmsflashDirStatus.setStatus('mandatory')
mibBuilder.exportSymbols("NMS-FLASH", nmsflashSize=nmsflashSize, nmsflashToNetStatus=nmsflashToNetStatus, nmslflash=nmslflash, nmsflashDirStatus=nmsflashDirStatus, nmsflashCard=nmsflashCard, nmsnetToFlashTime=nmsnetToFlashTime, nmsflashController=nmsflashController, nmsflashErase=nmsflashErase, nmslflashFileDirEntry=nmslflashFileDirEntry, nmsflashEraseStatus=nmsflashEraseStatus, nmsflashVPP=nmsflashVPP, nmsflashToNetTime=nmsflashToNetTime, nmsflashDirSize=nmsflashDirSize, nmsflashEraseTime=nmsflashEraseTime, nmsflashDirName=nmsflashDirName, nmsnetToFlashStatus=nmsnetToFlashStatus, nmsflashToNet=nmsflashToNet, nmsflashFree=nmsflashFree, nmsflashStatus=nmsflashStatus, nmslflashFileDirTable=nmslflashFileDirTable, nmsnetToFlash=nmsnetToFlash, nmsflashEntries=nmsflashEntries)
