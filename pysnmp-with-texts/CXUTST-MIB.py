#
# PySNMP MIB module CXUTST-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/CXUTST-MIB
# Produced by pysmi-0.3.4 at Wed May  1 12:33:35 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
Integer, OctetString, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "Integer", "OctetString", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, SingleValueConstraint, ConstraintsIntersection, ConstraintsUnion, ValueRangeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "SingleValueConstraint", "ConstraintsIntersection", "ConstraintsUnion", "ValueRangeConstraint")
cxUTst, = mibBuilder.importSymbols("CXProduct-SMI", "cxUTst")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
Integer32, IpAddress, MibScalar, MibTable, MibTableRow, MibTableColumn, TimeTicks, iso, ObjectIdentity, Counter64, NotificationType, MibIdentifier, Unsigned32, Gauge32, ModuleIdentity, Bits, Counter32 = mibBuilder.importSymbols("SNMPv2-SMI", "Integer32", "IpAddress", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "TimeTicks", "iso", "ObjectIdentity", "Counter64", "NotificationType", "MibIdentifier", "Unsigned32", "Gauge32", "ModuleIdentity", "Bits", "Counter32")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
utstTable = MibTable((1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 40, 10), )
if mibBuilder.loadTexts: utstTable.setStatus('mandatory')
if mibBuilder.loadTexts: utstTable.setDescription('A table containing test results of an ISDN U-Interface daughter card.')
utstEntry = MibTableRow((1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 40, 10, 1), ).setIndexNames((0, "CXUTST-MIB", "utstSlotNumberIndex"))
if mibBuilder.loadTexts: utstEntry.setStatus('mandatory')
if mibBuilder.loadTexts: utstEntry.setDescription('The parameters for a specific ISDN U-Interface daughter card.')
utstSlotNumberIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 40, 10, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 6))).setMaxAccess("readonly")
if mibBuilder.loadTexts: utstSlotNumberIndex.setStatus('mandatory')
if mibBuilder.loadTexts: utstSlotNumberIndex.setDescription('Indicates the row containing objects for monitoring an I/O card in the CX 900. Range of Values: 1-6 Default Value: none')
utstIoRegTest = MibTableColumn((1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 40, 10, 1, 20), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("failed", 1), ("passed", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: utstIoRegTest.setStatus('mandatory')
if mibBuilder.loadTexts: utstIoRegTest.setDescription('Indicates the result of the ISDN U-interface I/O register test. Options: failed (1): register test failed passed (2): register test passed Default Value: passed (2)')
utstIoLedsTest = MibTableColumn((1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 40, 10, 1, 21), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("initializationFailed", 1), ("initializationPassed", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: utstIoLedsTest.setStatus('mandatory')
if mibBuilder.loadTexts: utstIoLedsTest.setDescription('Indicates the result of the ISDN U-interface Integrated Multiprotocol Processor (IMP) LEDs test. Options: initializationFailed (1): IMP initialization failed initializationPassed (2): IMP initialization passed Default Value: initializationPassed')
utstImpRegTest = MibTableColumn((1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 40, 10, 1, 22), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("initializationFailed", 1), ("failed", 2), ("passed", 3)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: utstImpRegTest.setStatus('mandatory')
if mibBuilder.loadTexts: utstImpRegTest.setDescription('Indicates the result of the ISDN U-interface Integrated Multiprotocol Processor (IMP) register test. Options: initializationFailed (1): IMP initialization failed failed (2): IMP register test failed passed (3): IMP register test passed Default Value: passed (3)')
utstImpComTestPollResult = MibTableColumn((1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 40, 10, 1, 23), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("initializationFailed", 1), ("failed", 2), ("passed", 3)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: utstImpComTestPollResult.setStatus('mandatory')
if mibBuilder.loadTexts: utstImpComTestPollResult.setDescription('Indicates the result of the ISDN U-interface IMP internal communication test while in polling mode. Options: initializationFailed (1): IMP initialization failed failed (2): IMP communication test failed in polling mode passed (3): IMP communication test passed in polling mode Default Value: passed (3)')
utstUifRegTest = MibTableColumn((1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 40, 10, 1, 24), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("initializationFailed", 1), ("failed", 2), ("passed", 3)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: utstUifRegTest.setStatus('mandatory')
if mibBuilder.loadTexts: utstUifRegTest.setDescription('Indicates the result of the ISDN U-interface transceiver register test. Options: initializationFailed (1): IMP initialization test failed failed (2): transceiver register test failed passed (3): transceiver register test passed Default Value: passed (3)')
utstUifComTestPollResult = MibTableColumn((1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 40, 10, 1, 25), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("initializationFailed", 1), ("failed", 2), ("passed", 3)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: utstUifComTestPollResult.setStatus('mandatory')
if mibBuilder.loadTexts: utstUifComTestPollResult.setDescription('Indicates the result of the ISDN U-interface transceiver internal communication test while in polling mode. Options: initializationFailed (1): IMP initialization failed failed (2): transceiver communication test failed in polling mode passed (3): transceiver communication test passed in polling mode Default Value: passed (3)')
mibBuilder.exportSymbols("CXUTST-MIB", utstEntry=utstEntry, utstIoLedsTest=utstIoLedsTest, utstIoRegTest=utstIoRegTest, utstUifComTestPollResult=utstUifComTestPollResult, utstImpComTestPollResult=utstImpComTestPollResult, utstImpRegTest=utstImpRegTest, utstUifRegTest=utstUifRegTest, utstSlotNumberIndex=utstSlotNumberIndex, utstTable=utstTable)
