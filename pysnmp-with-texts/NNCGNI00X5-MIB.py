#
# PySNMP MIB module NNCGNI00X5-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/NNCGNI00X5-MIB
# Produced by pysmi-0.3.4 at Wed May  1 14:23:08 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
Integer, OctetString, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "Integer", "OctetString", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ConstraintsUnion, ValueSizeConstraint, SingleValueConstraint, ValueRangeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ConstraintsUnion", "ValueSizeConstraint", "SingleValueConstraint", "ValueRangeConstraint")
nncExtDs1, = mibBuilder.importSymbols("NNCGNI00X1-SMI", "nncExtDs1")
PortIndex, CircuitIndex = mibBuilder.importSymbols("NNCGNI00X7-MIB", "PortIndex", "CircuitIndex")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
iso, NotificationType, Counter32, MibIdentifier, Integer32, IpAddress, MibScalar, MibTable, MibTableRow, MibTableColumn, Bits, ObjectIdentity, TimeTicks, Unsigned32, ModuleIdentity, Gauge32, Counter64 = mibBuilder.importSymbols("SNMPv2-SMI", "iso", "NotificationType", "Counter32", "MibIdentifier", "Integer32", "IpAddress", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Bits", "ObjectIdentity", "TimeTicks", "Unsigned32", "ModuleIdentity", "Gauge32", "Counter64")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
class Ds1LineIndex(Integer32):
    subtypeSpec = Integer32.subtypeSpec + ValueRangeConstraint(1, 2147483647)

class Ds1IntervalIndex(Integer32):
    subtypeSpec = Integer32.subtypeSpec + ValueRangeConstraint(1, 96)

class DebounceInterval(Integer32):
    subtypeSpec = Integer32.subtypeSpec + ValueRangeConstraint(100, 30000)

nncExtDs1ConfigTable = MibTable((1, 3, 6, 1, 4, 1, 123, 3, 10, 1), )
if mibBuilder.loadTexts: nncExtDs1ConfigTable.setStatus('mandatory')
nncExtDs1ConfigEntry = MibTableRow((1, 3, 6, 1, 4, 1, 123, 3, 10, 1, 1), ).setIndexNames((0, "NNCGNI00X5-MIB", "nncExtDs1ConfigIndex"))
if mibBuilder.loadTexts: nncExtDs1ConfigEntry.setStatus('mandatory')
nncExtDs1ConfigIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 123, 3, 10, 1, 1, 1), Ds1LineIndex()).setMaxAccess("readonly")
if mibBuilder.loadTexts: nncExtDs1ConfigIndex.setStatus('mandatory')
nncExtDs1LineLength = MibTableColumn((1, 3, 6, 1, 4, 1, 123, 3, 10, 1, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("short", 1), ("medium", 2), ("long", 3)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: nncExtDs1LineLength.setStatus('mandatory')
nncExtDs1LineStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 123, 3, 10, 1, 1, 3), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 32767))).setMaxAccess("readonly")
if mibBuilder.loadTexts: nncExtDs1LineStatus.setStatus('mandatory')
nncExtDs1TrunkCondEnable = MibTableColumn((1, 3, 6, 1, 4, 1, 123, 3, 10, 1, 1, 4), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 63))).setMaxAccess("readonly")
if mibBuilder.loadTexts: nncExtDs1TrunkCondEnable.setStatus('mandatory')
nncExtDs1LossOfFrameConditioning = MibTableColumn((1, 3, 6, 1, 4, 1, 123, 3, 10, 1, 1, 5), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enable", 1), ("disable", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: nncExtDs1LossOfFrameConditioning.setStatus('mandatory')
nncExtDs1DistantLossOfFrameConditioning = MibTableColumn((1, 3, 6, 1, 4, 1, 123, 3, 10, 1, 1, 6), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enable", 1), ("disable", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: nncExtDs1DistantLossOfFrameConditioning.setStatus('mandatory')
nncExtDs1FailedStateConditioning = MibTableColumn((1, 3, 6, 1, 4, 1, 123, 3, 10, 1, 1, 7), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enable", 1), ("disable", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: nncExtDs1FailedStateConditioning.setStatus('mandatory')
nncExtDs1ErrorRateConditioning = MibTableColumn((1, 3, 6, 1, 4, 1, 123, 3, 10, 1, 1, 8), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enable", 1), ("disable", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: nncExtDs1ErrorRateConditioning.setStatus('mandatory')
nncExtDs1CSULoopbackConditioning = MibTableColumn((1, 3, 6, 1, 4, 1, 123, 3, 10, 1, 1, 9), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enable", 1), ("disable", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: nncExtDs1CSULoopbackConditioning.setStatus('mandatory')
nncExtDs1AlarmDeclareTime = MibTableColumn((1, 3, 6, 1, 4, 1, 123, 3, 10, 1, 1, 10), DebounceInterval()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: nncExtDs1AlarmDeclareTime.setStatus('mandatory')
nncExtDs1AlarmClearTime = MibTableColumn((1, 3, 6, 1, 4, 1, 123, 3, 10, 1, 1, 11), DebounceInterval()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: nncExtDs1AlarmClearTime.setStatus('mandatory')
nncExtDs1UseCRCOnReframe = MibTableColumn((1, 3, 6, 1, 4, 1, 123, 3, 10, 1, 1, 12), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("enabled", 1), ("disabled", 2), ("notApplicable", 3)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: nncExtDs1UseCRCOnReframe.setStatus('mandatory')
nncExtDs1WorstInterval = MibTableColumn((1, 3, 6, 1, 4, 1, 123, 3, 10, 1, 1, 13), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 96))).setMaxAccess("readonly")
if mibBuilder.loadTexts: nncExtDs1WorstInterval.setStatus('mandatory')
nncExtDs1ErrorEvents = MibTableColumn((1, 3, 6, 1, 4, 1, 123, 3, 10, 1, 1, 14), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 65535))).setMaxAccess("readonly")
if mibBuilder.loadTexts: nncExtDs1ErrorEvents.setStatus('mandatory')
nncExtDs181XXCompatibility = MibTableColumn((1, 3, 6, 1, 4, 1, 123, 3, 10, 1, 1, 15), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enabled", 1), ("disabled", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: nncExtDs181XXCompatibility.setStatus('mandatory')
nncExtDs1LoopbackConfig = MibTableColumn((1, 3, 6, 1, 4, 1, 123, 3, 10, 1, 1, 16), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 5))).clone(namedValues=NamedValues(("none", 1), ("equipment", 2), ("line", 5)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: nncExtDs1LoopbackConfig.setStatus('mandatory')
nncExtDs1E1TrunkCondEnable = MibTableColumn((1, 3, 6, 1, 4, 1, 123, 3, 10, 1, 1, 17), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 63))).setMaxAccess("readonly")
if mibBuilder.loadTexts: nncExtDs1E1TrunkCondEnable.setStatus('deprecated')
nncExtDs1E1ConfigTable = MibTable((1, 3, 6, 1, 4, 1, 123, 3, 10, 2), )
if mibBuilder.loadTexts: nncExtDs1E1ConfigTable.setStatus('mandatory')
nncExtDs1E1ConfigEntry = MibTableRow((1, 3, 6, 1, 4, 1, 123, 3, 10, 2, 1), ).setIndexNames((0, "NNCGNI00X5-MIB", "nncExtDs1E1Index"))
if mibBuilder.loadTexts: nncExtDs1E1ConfigEntry.setStatus('mandatory')
nncExtDs1E1Index = MibTableColumn((1, 3, 6, 1, 4, 1, 123, 3, 10, 2, 1, 1), Ds1LineIndex()).setMaxAccess("readonly")
if mibBuilder.loadTexts: nncExtDs1E1Index.setStatus('mandatory')
nncExtDs1E1TransmitShieldStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 123, 3, 10, 2, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("earthed", 1), ("floating", 2), ("notApplicable", 3)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: nncExtDs1E1TransmitShieldStatus.setStatus('mandatory')
nncExtDs1E1ReceivedShieldStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 123, 3, 10, 2, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("earthed", 1), ("floating", 2), ("notApplicable", 3)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: nncExtDs1E1ReceivedShieldStatus.setStatus('mandatory')
nncExtDs1E1StatisticsType = MibTableColumn((1, 3, 6, 1, 4, 1, 123, 3, 10, 2, 1, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("hdb3", 1), ("crc4", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: nncExtDs1E1StatisticsType.setStatus('mandatory')
nncExtDs1G821StatisticsTable = MibTable((1, 3, 6, 1, 4, 1, 123, 3, 10, 3), )
if mibBuilder.loadTexts: nncExtDs1G821StatisticsTable.setStatus('mandatory')
nncExtDs1G821StatisticsEntry = MibTableRow((1, 3, 6, 1, 4, 1, 123, 3, 10, 3, 1), ).setIndexNames((0, "NNCGNI00X5-MIB", "nncG821Index"))
if mibBuilder.loadTexts: nncExtDs1G821StatisticsEntry.setStatus('mandatory')
nncG821Index = MibTableColumn((1, 3, 6, 1, 4, 1, 123, 3, 10, 3, 1, 1), Ds1LineIndex()).setMaxAccess("readonly")
if mibBuilder.loadTexts: nncG821Index.setStatus('mandatory')
nncG821DegradedMinutes = MibTableColumn((1, 3, 6, 1, 4, 1, 123, 3, 10, 3, 1, 2), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: nncG821DegradedMinutes.setStatus('mandatory')
nncG821ErroredSeconds = MibTableColumn((1, 3, 6, 1, 4, 1, 123, 3, 10, 3, 1, 3), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: nncG821ErroredSeconds.setStatus('mandatory')
nncG821SeverelyErroredSeconds = MibTableColumn((1, 3, 6, 1, 4, 1, 123, 3, 10, 3, 1, 4), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: nncG821SeverelyErroredSeconds.setStatus('mandatory')
nncG821UnavailableSeconds = MibTableColumn((1, 3, 6, 1, 4, 1, 123, 3, 10, 3, 1, 5), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: nncG821UnavailableSeconds.setStatus('mandatory')
nncG821TotalSeconds = MibTableColumn((1, 3, 6, 1, 4, 1, 123, 3, 10, 3, 1, 6), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: nncG821TotalSeconds.setStatus('mandatory')
nncExtDs1IntervalTable = MibTable((1, 3, 6, 1, 4, 1, 123, 3, 10, 4), )
if mibBuilder.loadTexts: nncExtDs1IntervalTable.setStatus('mandatory')
nncExtDs1IntervalEntry = MibTableRow((1, 3, 6, 1, 4, 1, 123, 3, 10, 4, 1), ).setIndexNames((0, "NNCGNI00X5-MIB", "nncExtDs1IntervalIndex"), (0, "NNCGNI00X5-MIB", "nncExtDs1IntervalNumber"))
if mibBuilder.loadTexts: nncExtDs1IntervalEntry.setStatus('mandatory')
nncExtDs1IntervalIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 123, 3, 10, 4, 1, 1), Ds1LineIndex()).setMaxAccess("readonly")
if mibBuilder.loadTexts: nncExtDs1IntervalIndex.setStatus('mandatory')
nncExtDs1IntervalNumber = MibTableColumn((1, 3, 6, 1, 4, 1, 123, 3, 10, 4, 1, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 96))).setMaxAccess("readonly")
if mibBuilder.loadTexts: nncExtDs1IntervalNumber.setStatus('mandatory')
nncExtDs1IntervalLOFC = MibTableColumn((1, 3, 6, 1, 4, 1, 123, 3, 10, 4, 1, 3), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: nncExtDs1IntervalLOFC.setStatus('mandatory')
nncExtDs1TotalTable = MibTable((1, 3, 6, 1, 4, 1, 123, 3, 10, 5), )
if mibBuilder.loadTexts: nncExtDs1TotalTable.setStatus('mandatory')
nncExtDs1TotalEntry = MibTableRow((1, 3, 6, 1, 4, 1, 123, 3, 10, 5, 1), ).setIndexNames((0, "NNCGNI00X5-MIB", "nncExtDs1TotalIndex"))
if mibBuilder.loadTexts: nncExtDs1TotalEntry.setStatus('mandatory')
nncExtDs1TotalIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 123, 3, 10, 5, 1, 1), Ds1LineIndex()).setMaxAccess("readonly")
if mibBuilder.loadTexts: nncExtDs1TotalIndex.setStatus('mandatory')
nncExtDs1TotalLOFC = MibTableColumn((1, 3, 6, 1, 4, 1, 123, 3, 10, 5, 1, 2), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: nncExtDs1TotalLOFC.setStatus('mandatory')
nncExtDs1CurrentTable = MibTable((1, 3, 6, 1, 4, 1, 123, 3, 10, 8), )
if mibBuilder.loadTexts: nncExtDs1CurrentTable.setStatus('mandatory')
nncExtDs1CurrentEntry = MibTableRow((1, 3, 6, 1, 4, 1, 123, 3, 10, 8, 1), ).setIndexNames((0, "NNCGNI00X5-MIB", "nncExtDs1CurrentIndex"))
if mibBuilder.loadTexts: nncExtDs1CurrentEntry.setStatus('mandatory')
nncExtDs1CurrentIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 123, 3, 10, 8, 1, 1), Ds1LineIndex()).setMaxAccess("readonly")
if mibBuilder.loadTexts: nncExtDs1CurrentIndex.setStatus('mandatory')
nncExtDs1CurrentLOFC = MibTableColumn((1, 3, 6, 1, 4, 1, 123, 3, 10, 8, 1, 2), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: nncExtDs1CurrentLOFC.setStatus('mandatory')
nncExtDs1WorstIntervalTable = MibTable((1, 3, 6, 1, 4, 1, 123, 3, 10, 6), )
if mibBuilder.loadTexts: nncExtDs1WorstIntervalTable.setStatus('mandatory')
nncExtDs1WorstIntervalEntry = MibTableRow((1, 3, 6, 1, 4, 1, 123, 3, 10, 6, 1), ).setIndexNames((0, "NNCGNI00X5-MIB", "nncExtDs1WorstIntervalIndex"))
if mibBuilder.loadTexts: nncExtDs1WorstIntervalEntry.setStatus('mandatory')
nncExtDs1WorstIntervalIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 123, 3, 10, 6, 1, 1), Ds1LineIndex()).setMaxAccess("readonly")
if mibBuilder.loadTexts: nncExtDs1WorstIntervalIndex.setStatus('mandatory')
nncExtDs1WorstIntervalBESs = MibTableColumn((1, 3, 6, 1, 4, 1, 123, 3, 10, 6, 1, 2), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: nncExtDs1WorstIntervalBESs.setStatus('mandatory')
nncExtDs1WorstIntervalLOFC = MibTableColumn((1, 3, 6, 1, 4, 1, 123, 3, 10, 6, 1, 3), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: nncExtDs1WorstIntervalLOFC.setStatus('mandatory')
nncExtDs1WorstIntervalESs = MibTableColumn((1, 3, 6, 1, 4, 1, 123, 3, 10, 6, 1, 4), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: nncExtDs1WorstIntervalESs.setStatus('mandatory')
nncExtDs1WorstIntervalSESs = MibTableColumn((1, 3, 6, 1, 4, 1, 123, 3, 10, 6, 1, 5), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: nncExtDs1WorstIntervalSESs.setStatus('mandatory')
nncExtDs1WorstIntervalSEFSs = MibTableColumn((1, 3, 6, 1, 4, 1, 123, 3, 10, 6, 1, 6), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: nncExtDs1WorstIntervalSEFSs.setStatus('mandatory')
nncExtDs1WorstIntervalUASs = MibTableColumn((1, 3, 6, 1, 4, 1, 123, 3, 10, 6, 1, 7), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: nncExtDs1WorstIntervalUASs.setStatus('mandatory')
nncExtDs1WorstIntervalCSSs = MibTableColumn((1, 3, 6, 1, 4, 1, 123, 3, 10, 6, 1, 8), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: nncExtDs1WorstIntervalCSSs.setStatus('mandatory')
nncExtDs1WorstIntervalBPVs = MibTableColumn((1, 3, 6, 1, 4, 1, 123, 3, 10, 6, 1, 9), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: nncExtDs1WorstIntervalBPVs.setStatus('mandatory')
nncExtDs1WorstIntervalCVs = MibTableColumn((1, 3, 6, 1, 4, 1, 123, 3, 10, 6, 1, 10), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: nncExtDs1WorstIntervalCVs.setStatus('mandatory')
nncExtDs1WorstIntervalLESs = MibTableColumn((1, 3, 6, 1, 4, 1, 123, 3, 10, 6, 1, 11), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: nncExtDs1WorstIntervalLESs.setStatus('mandatory')
nncExtDs1CircuitTable = MibTable((1, 3, 6, 1, 4, 1, 123, 3, 10, 7), )
if mibBuilder.loadTexts: nncExtDs1CircuitTable.setStatus('mandatory')
nncExtDs1CircuitEntry = MibTableRow((1, 3, 6, 1, 4, 1, 123, 3, 10, 7, 1), ).setIndexNames((0, "NNCGNI00X5-MIB", "nncExtDs1CctIndex"), (0, "NNCGNI00X5-MIB", "nncExtDs1CctPortNumber"), (0, "NNCGNI00X5-MIB", "nncExtDs1CctNumber"))
if mibBuilder.loadTexts: nncExtDs1CircuitEntry.setStatus('mandatory')
nncExtDs1CctIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 123, 3, 10, 7, 1, 1), Ds1LineIndex()).setMaxAccess("readonly")
if mibBuilder.loadTexts: nncExtDs1CctIndex.setStatus('mandatory')
nncExtDs1CctPortNumber = MibTableColumn((1, 3, 6, 1, 4, 1, 123, 3, 10, 7, 1, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 4))).setMaxAccess("readonly")
if mibBuilder.loadTexts: nncExtDs1CctPortNumber.setStatus('mandatory')
nncExtDs1CctNumber = MibTableColumn((1, 3, 6, 1, 4, 1, 123, 3, 10, 7, 1, 3), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 31))).setMaxAccess("readonly")
if mibBuilder.loadTexts: nncExtDs1CctNumber.setStatus('mandatory')
nncExtDs1CctUseRBS = MibTableColumn((1, 3, 6, 1, 4, 1, 123, 3, 10, 7, 1, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("rbsOn", 1), ("rbsOff", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: nncExtDs1CctUseRBS.setStatus('mandatory')
nncExtDs1CctDataInversion = MibTableColumn((1, 3, 6, 1, 4, 1, 123, 3, 10, 7, 1, 5), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("invertOn", 1), ("invertOff", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: nncExtDs1CctDataInversion.setStatus('mandatory')
nncExtDs1CctDefaultData = MibTableColumn((1, 3, 6, 1, 4, 1, 123, 3, 10, 7, 1, 6), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 255))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: nncExtDs1CctDefaultData.setStatus('mandatory')
nncExtDs1CctFirstCode = MibTableColumn((1, 3, 6, 1, 4, 1, 123, 3, 10, 7, 1, 7), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 15))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: nncExtDs1CctFirstCode.setStatus('mandatory')
nncExtDs1CctSecondCode = MibTableColumn((1, 3, 6, 1, 4, 1, 123, 3, 10, 7, 1, 8), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 15))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: nncExtDs1CctSecondCode.setStatus('mandatory')
nncExtDs1CctBitsToUse = MibTableColumn((1, 3, 6, 1, 4, 1, 123, 3, 10, 7, 1, 9), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 255))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: nncExtDs1CctBitsToUse.setStatus('mandatory')
nncExtDs1CctSuperRateMap = MibTableColumn((1, 3, 6, 1, 4, 1, 123, 3, 10, 7, 1, 10), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 2147483647))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: nncExtDs1CctSuperRateMap.setStatus('mandatory')
nncExtDs1CctFaultSignalling = MibTableColumn((1, 3, 6, 1, 4, 1, 123, 3, 10, 7, 1, 11), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("idle", 1), ("seized", 2), ("none", 3)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: nncExtDs1CctFaultSignalling.setStatus('mandatory')
mibBuilder.exportSymbols("NNCGNI00X5-MIB", nncG821SeverelyErroredSeconds=nncG821SeverelyErroredSeconds, nncExtDs1CctNumber=nncExtDs1CctNumber, nncExtDs1WorstIntervalLESs=nncExtDs1WorstIntervalLESs, nncExtDs1AlarmDeclareTime=nncExtDs1AlarmDeclareTime, nncExtDs181XXCompatibility=nncExtDs181XXCompatibility, nncExtDs1E1ConfigTable=nncExtDs1E1ConfigTable, nncExtDs1E1StatisticsType=nncExtDs1E1StatisticsType, nncExtDs1ConfigTable=nncExtDs1ConfigTable, nncExtDs1CctFirstCode=nncExtDs1CctFirstCode, nncExtDs1ConfigEntry=nncExtDs1ConfigEntry, nncExtDs1AlarmClearTime=nncExtDs1AlarmClearTime, nncExtDs1DistantLossOfFrameConditioning=nncExtDs1DistantLossOfFrameConditioning, nncExtDs1CSULoopbackConditioning=nncExtDs1CSULoopbackConditioning, nncExtDs1CctIndex=nncExtDs1CctIndex, nncExtDs1TotalTable=nncExtDs1TotalTable, nncExtDs1G821StatisticsEntry=nncExtDs1G821StatisticsEntry, nncExtDs1WorstIntervalLOFC=nncExtDs1WorstIntervalLOFC, nncG821UnavailableSeconds=nncG821UnavailableSeconds, nncExtDs1WorstIntervalBPVs=nncExtDs1WorstIntervalBPVs, nncExtDs1WorstIntervalCSSs=nncExtDs1WorstIntervalCSSs, nncExtDs1WorstIntervalCVs=nncExtDs1WorstIntervalCVs, nncExtDs1CctBitsToUse=nncExtDs1CctBitsToUse, nncExtDs1CctDefaultData=nncExtDs1CctDefaultData, nncExtDs1IntervalLOFC=nncExtDs1IntervalLOFC, nncExtDs1WorstIntervalBESs=nncExtDs1WorstIntervalBESs, nncExtDs1CctSecondCode=nncExtDs1CctSecondCode, nncExtDs1CctFaultSignalling=nncExtDs1CctFaultSignalling, nncExtDs1UseCRCOnReframe=nncExtDs1UseCRCOnReframe, nncExtDs1TotalLOFC=nncExtDs1TotalLOFC, nncExtDs1CctUseRBS=nncExtDs1CctUseRBS, nncExtDs1WorstIntervalUASs=nncExtDs1WorstIntervalUASs, nncG821ErroredSeconds=nncG821ErroredSeconds, DebounceInterval=DebounceInterval, nncExtDs1ConfigIndex=nncExtDs1ConfigIndex, nncExtDs1FailedStateConditioning=nncExtDs1FailedStateConditioning, nncExtDs1E1Index=nncExtDs1E1Index, nncExtDs1LineLength=nncExtDs1LineLength, nncExtDs1E1ReceivedShieldStatus=nncExtDs1E1ReceivedShieldStatus, nncExtDs1WorstInterval=nncExtDs1WorstInterval, nncG821TotalSeconds=nncG821TotalSeconds, nncExtDs1E1TrunkCondEnable=nncExtDs1E1TrunkCondEnable, nncExtDs1TotalEntry=nncExtDs1TotalEntry, nncExtDs1WorstIntervalESs=nncExtDs1WorstIntervalESs, nncExtDs1ErrorEvents=nncExtDs1ErrorEvents, nncExtDs1IntervalTable=nncExtDs1IntervalTable, nncExtDs1CctDataInversion=nncExtDs1CctDataInversion, nncExtDs1CctSuperRateMap=nncExtDs1CctSuperRateMap, nncExtDs1LossOfFrameConditioning=nncExtDs1LossOfFrameConditioning, nncExtDs1CircuitTable=nncExtDs1CircuitTable, nncG821DegradedMinutes=nncG821DegradedMinutes, nncExtDs1LineStatus=nncExtDs1LineStatus, nncExtDs1TrunkCondEnable=nncExtDs1TrunkCondEnable, nncExtDs1TotalIndex=nncExtDs1TotalIndex, nncExtDs1CurrentTable=nncExtDs1CurrentTable, nncExtDs1G821StatisticsTable=nncExtDs1G821StatisticsTable, nncExtDs1ErrorRateConditioning=nncExtDs1ErrorRateConditioning, nncExtDs1WorstIntervalEntry=nncExtDs1WorstIntervalEntry, nncExtDs1E1ConfigEntry=nncExtDs1E1ConfigEntry, nncExtDs1WorstIntervalSEFSs=nncExtDs1WorstIntervalSEFSs, nncExtDs1CurrentIndex=nncExtDs1CurrentIndex, nncExtDs1CctPortNumber=nncExtDs1CctPortNumber, Ds1LineIndex=Ds1LineIndex, nncExtDs1IntervalEntry=nncExtDs1IntervalEntry, nncExtDs1WorstIntervalIndex=nncExtDs1WorstIntervalIndex, nncExtDs1IntervalIndex=nncExtDs1IntervalIndex, nncExtDs1CircuitEntry=nncExtDs1CircuitEntry, nncExtDs1CurrentEntry=nncExtDs1CurrentEntry, Ds1IntervalIndex=Ds1IntervalIndex, nncExtDs1CurrentLOFC=nncExtDs1CurrentLOFC, nncExtDs1E1TransmitShieldStatus=nncExtDs1E1TransmitShieldStatus, nncG821Index=nncG821Index, nncExtDs1WorstIntervalSESs=nncExtDs1WorstIntervalSESs, nncExtDs1WorstIntervalTable=nncExtDs1WorstIntervalTable, nncExtDs1LoopbackConfig=nncExtDs1LoopbackConfig, nncExtDs1IntervalNumber=nncExtDs1IntervalNumber)