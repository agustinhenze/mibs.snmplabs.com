#
# PySNMP MIB module WaveLAN-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/WaveLAN-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 21:32:12 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsIntersection, SingleValueConstraint, ConstraintsUnion, ValueRangeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsIntersection", "SingleValueConstraint", "ConstraintsUnion", "ValueRangeConstraint")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
Counter64, MibIdentifier, Counter32, enterprises, Bits, ModuleIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, TimeTicks, ObjectIdentity, Unsigned32, IpAddress, NotificationType, Gauge32, iso, Integer32 = mibBuilder.importSymbols("SNMPv2-SMI", "Counter64", "MibIdentifier", "Counter32", "enterprises", "Bits", "ModuleIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "TimeTicks", "ObjectIdentity", "Unsigned32", "IpAddress", "NotificationType", "Gauge32", "iso", "Integer32")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
att_2 = MibIdentifier((1, 3, 6, 1, 4, 1, 74)).setLabel("att-2")
att_mgmt = MibIdentifier((1, 3, 6, 1, 4, 1, 74, 2)).setLabel("att-mgmt")
wavelan = MibIdentifier((1, 3, 6, 1, 4, 1, 74, 2, 21))
wavelanInterface = MibIdentifier((1, 3, 6, 1, 4, 1, 74, 2, 21, 1))
wliNicTable = MibTable((1, 3, 6, 1, 4, 1, 74, 2, 21, 1, 1), )
if mibBuilder.loadTexts: wliNicTable.setStatus('mandatory')
wliNicEntry = MibTableRow((1, 3, 6, 1, 4, 1, 74, 2, 21, 1, 1, 1), ).setIndexNames((0, "WaveLAN-MIB", "wliNicIndex"))
if mibBuilder.loadTexts: wliNicEntry.setStatus('mandatory')
wliNicIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 74, 2, 21, 1, 1, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: wliNicIndex.setStatus('mandatory')
wliNicBusType = MibTableColumn((1, 3, 6, 1, 4, 1, 74, 2, 21, 1, 1, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5))).clone(namedValues=NamedValues(("xtBus", 1), ("isaBus", 2), ("mcBus", 3), ("pcmcia2Bus", 4), ("wavepointBus", 5)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: wliNicBusType.setStatus('mandatory')
wliNicSlot = MibTableColumn((1, 3, 6, 1, 4, 1, 74, 2, 21, 1, 1, 1, 3), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 8))).setMaxAccess("readonly")
if mibBuilder.loadTexts: wliNicSlot.setStatus('mandatory')
wliNicIrq = MibTableColumn((1, 3, 6, 1, 4, 1, 74, 2, 21, 1, 1, 1, 4), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 15))).setMaxAccess("readonly")
if mibBuilder.loadTexts: wliNicIrq.setStatus('mandatory')
wliNicError = MibTableColumn((1, 3, 6, 1, 4, 1, 74, 2, 21, 1, 1, 1, 5), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: wliNicError.setStatus('mandatory')
wliNicOutOfRxResource = MibTableColumn((1, 3, 6, 1, 4, 1, 74, 2, 21, 1, 1, 1, 6), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: wliNicOutOfRxResource.setStatus('mandatory')
wliPhyTable = MibTable((1, 3, 6, 1, 4, 1, 74, 2, 21, 1, 2), )
if mibBuilder.loadTexts: wliPhyTable.setStatus('mandatory')
wliPhyEntry = MibTableRow((1, 3, 6, 1, 4, 1, 74, 2, 21, 1, 2, 1), ).setIndexNames((0, "WaveLAN-MIB", "wliPhyIndex"))
if mibBuilder.loadTexts: wliPhyEntry.setStatus('mandatory')
wliPhyIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 74, 2, 21, 1, 2, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: wliPhyIndex.setStatus('mandatory')
wliPhyDsp = MibTableColumn((1, 3, 6, 1, 4, 1, 74, 2, 21, 1, 2, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("icarus", 1), ("daedalus", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: wliPhyDsp.setStatus('mandatory')
wliPhyFrequency = MibTableColumn((1, 3, 6, 1, 4, 1, 74, 2, 21, 1, 2, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11))).clone(namedValues=NamedValues(("f915Mhz", 1), ("f2425Mhz", 2), ("f2460Mhz", 3), ("f2484Mhz", 4), ("f2430Mhz", 5), ("f2412Mhz", 6), ("f2422Mhz", 7), ("f2432Mhz", 8), ("f2442Mhz", 9), ("f2452Mhz", 10), ("f2462Mhz", 11)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: wliPhyFrequency.setStatus('mandatory')
wliPhyNwid = MibTableColumn((1, 3, 6, 1, 4, 1, 74, 2, 21, 1, 2, 1, 4), OctetString().subtype(subtypeSpec=ValueSizeConstraint(2, 2)).setFixedLength(2)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: wliPhyNwid.setStatus('mandatory')
wliPhyRfSilenceLevel = MibTableColumn((1, 3, 6, 1, 4, 1, 74, 2, 21, 1, 2, 1, 5), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 36))).setMaxAccess("readonly")
if mibBuilder.loadTexts: wliPhyRfSilenceLevel.setStatus('mandatory')
wliPhyOwnNwid = MibTableColumn((1, 3, 6, 1, 4, 1, 74, 2, 21, 1, 2, 1, 6), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: wliPhyOwnNwid.setStatus('mandatory')
wliPhyOtherNwid = MibTableColumn((1, 3, 6, 1, 4, 1, 74, 2, 21, 1, 2, 1, 7), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: wliPhyOtherNwid.setStatus('mandatory')
wliPhyLowSnr = MibTableColumn((1, 3, 6, 1, 4, 1, 74, 2, 21, 1, 2, 1, 8), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: wliPhyLowSnr.setStatus('mandatory')
wliPhyGoodSnr = MibTableColumn((1, 3, 6, 1, 4, 1, 74, 2, 21, 1, 2, 1, 9), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: wliPhyGoodSnr.setStatus('mandatory')
wliPhyExcellentSnr = MibTableColumn((1, 3, 6, 1, 4, 1, 74, 2, 21, 1, 2, 1, 10), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: wliPhyExcellentSnr.setStatus('mandatory')
wliMacTable = MibTable((1, 3, 6, 1, 4, 1, 74, 2, 21, 1, 3), )
if mibBuilder.loadTexts: wliMacTable.setStatus('mandatory')
wliMacEntry = MibTableRow((1, 3, 6, 1, 4, 1, 74, 2, 21, 1, 3, 1), ).setIndexNames((0, "WaveLAN-MIB", "wliMacIndex"))
if mibBuilder.loadTexts: wliMacEntry.setStatus('mandatory')
wliMacIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 74, 2, 21, 1, 3, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: wliMacIndex.setStatus('mandatory')
wliMacAddressSelect = MibTableColumn((1, 3, 6, 1, 4, 1, 74, 2, 21, 1, 3, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("universal", 1), ("local", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: wliMacAddressSelect.setStatus('mandatory')
wliMacCaDefers = MibTableColumn((1, 3, 6, 1, 4, 1, 74, 2, 21, 1, 3, 1, 3), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: wliMacCaDefers.setStatus('mandatory')
wliMacDeferredTransmissions = MibTableColumn((1, 3, 6, 1, 4, 1, 74, 2, 21, 1, 3, 1, 4), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: wliMacDeferredTransmissions.setStatus('mandatory')
wliMacFCSErrors = MibTableColumn((1, 3, 6, 1, 4, 1, 74, 2, 21, 1, 3, 1, 5), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: wliMacFCSErrors.setStatus('mandatory')
wliMacFrameTooLongs = MibTableColumn((1, 3, 6, 1, 4, 1, 74, 2, 21, 1, 3, 1, 6), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: wliMacFrameTooLongs.setStatus('mandatory')
wliMacFrameTooShorts = MibTableColumn((1, 3, 6, 1, 4, 1, 74, 2, 21, 1, 3, 1, 7), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: wliMacFrameTooShorts.setStatus('mandatory')
wliMacDeferLimits = MibTableColumn((1, 3, 6, 1, 4, 1, 74, 2, 21, 1, 3, 1, 8), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: wliMacDeferLimits.setStatus('mandatory')
wliDriverTable = MibTable((1, 3, 6, 1, 4, 1, 74, 2, 21, 1, 4), )
if mibBuilder.loadTexts: wliDriverTable.setStatus('mandatory')
wliDriverEntry = MibTableRow((1, 3, 6, 1, 4, 1, 74, 2, 21, 1, 4, 1), ).setIndexNames((0, "WaveLAN-MIB", "wliDriverIndex"))
if mibBuilder.loadTexts: wliDriverEntry.setStatus('mandatory')
wliDriverIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 74, 2, 21, 1, 4, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: wliDriverIndex.setStatus('mandatory')
wliDriverName = MibTableColumn((1, 3, 6, 1, 4, 1, 74, 2, 21, 1, 4, 1, 2), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(7, 7)).setFixedLength(7)).setMaxAccess("readonly")
if mibBuilder.loadTexts: wliDriverName.setStatus('mandatory')
wliDriverVersion = MibTableColumn((1, 3, 6, 1, 4, 1, 74, 2, 21, 1, 4, 1, 3), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 8))).setMaxAccess("readonly")
if mibBuilder.loadTexts: wliDriverVersion.setStatus('mandatory')
wliEncTable = MibTable((1, 3, 6, 1, 4, 1, 74, 2, 21, 1, 5), )
if mibBuilder.loadTexts: wliEncTable.setStatus('mandatory')
wliEncEntry = MibTableRow((1, 3, 6, 1, 4, 1, 74, 2, 21, 1, 5, 1), ).setIndexNames((0, "WaveLAN-MIB", "wliEncIndex"))
if mibBuilder.loadTexts: wliEncEntry.setStatus('mandatory')
wliEncIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 74, 2, 21, 1, 5, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: wliEncIndex.setStatus('mandatory')
wliEncInstalled = MibTableColumn((1, 3, 6, 1, 4, 1, 74, 2, 21, 1, 5, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("none", 1), ("des", 2), ("aes", 3)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: wliEncInstalled.setStatus('mandatory')
wliEncSelect = MibTableColumn((1, 3, 6, 1, 4, 1, 74, 2, 21, 1, 5, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("disabled", 1), ("enabled", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: wliEncSelect.setStatus('mandatory')
wliEncKey = MibTableColumn((1, 3, 6, 1, 4, 1, 74, 2, 21, 1, 5, 1, 4), OctetString().subtype(subtypeSpec=ValueSizeConstraint(8, 8)).setFixedLength(8)).setMaxAccess("writeonly")
if mibBuilder.loadTexts: wliEncKey.setStatus('mandatory')
wliMcastDelayTable = MibTable((1, 3, 6, 1, 4, 1, 74, 2, 21, 1, 6), )
if mibBuilder.loadTexts: wliMcastDelayTable.setStatus('mandatory')
wliMcastDelayEntry = MibTableRow((1, 3, 6, 1, 4, 1, 74, 2, 21, 1, 6, 1), ).setIndexNames((0, "WaveLAN-MIB", "wliMcastDelayIndex"))
if mibBuilder.loadTexts: wliMcastDelayEntry.setStatus('mandatory')
wliMcastDelayIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 74, 2, 21, 1, 6, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: wliMcastDelayIndex.setStatus('mandatory')
wliMcastNumberOfAps = MibTableColumn((1, 3, 6, 1, 4, 1, 74, 2, 21, 1, 6, 1, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 10))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: wliMcastNumberOfAps.setStatus('mandatory')
wliMcastApSequenceNumber = MibTableColumn((1, 3, 6, 1, 4, 1, 74, 2, 21, 1, 6, 1, 3), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 10))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: wliMcastApSequenceNumber.setStatus('mandatory')
wliMcastRepeatCount = MibTableColumn((1, 3, 6, 1, 4, 1, 74, 2, 21, 1, 6, 1, 4), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 10))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: wliMcastRepeatCount.setStatus('mandatory')
mibBuilder.exportSymbols("WaveLAN-MIB", wliMacDeferredTransmissions=wliMacDeferredTransmissions, wliPhyIndex=wliPhyIndex, wliPhyNwid=wliPhyNwid, wliNicOutOfRxResource=wliNicOutOfRxResource, wliNicSlot=wliNicSlot, wliPhyGoodSnr=wliPhyGoodSnr, wliEncTable=wliEncTable, wliEncSelect=wliEncSelect, wliNicEntry=wliNicEntry, wliPhyLowSnr=wliPhyLowSnr, wliPhyRfSilenceLevel=wliPhyRfSilenceLevel, wliPhyOwnNwid=wliPhyOwnNwid, wliDriverVersion=wliDriverVersion, wliEncInstalled=wliEncInstalled, wliEncIndex=wliEncIndex, wliPhyDsp=wliPhyDsp, wliMacFCSErrors=wliMacFCSErrors, wliDriverTable=wliDriverTable, wliEncKey=wliEncKey, wliNicIndex=wliNicIndex, wliMacIndex=wliMacIndex, wliMcastDelayEntry=wliMcastDelayEntry, wliNicIrq=wliNicIrq, wliDriverIndex=wliDriverIndex, wavelanInterface=wavelanInterface, att_2=att_2, wliMacFrameTooLongs=wliMacFrameTooLongs, wliPhyEntry=wliPhyEntry, wliMcastDelayTable=wliMcastDelayTable, wliPhyFrequency=wliPhyFrequency, wliMcastApSequenceNumber=wliMcastApSequenceNumber, wliEncEntry=wliEncEntry, wliNicError=wliNicError, wliMcastDelayIndex=wliMcastDelayIndex, wliNicTable=wliNicTable, wliDriverEntry=wliDriverEntry, wliPhyExcellentSnr=wliPhyExcellentSnr, wliMacTable=wliMacTable, wliNicBusType=wliNicBusType, wavelan=wavelan, wliPhyTable=wliPhyTable, wliPhyOtherNwid=wliPhyOtherNwid, wliMacEntry=wliMacEntry, wliMacFrameTooShorts=wliMacFrameTooShorts, wliMacCaDefers=wliMacCaDefers, wliMacAddressSelect=wliMacAddressSelect, att_mgmt=att_mgmt, wliMacDeferLimits=wliMacDeferLimits, wliMcastNumberOfAps=wliMcastNumberOfAps, wliMcastRepeatCount=wliMcastRepeatCount, wliDriverName=wliDriverName)
