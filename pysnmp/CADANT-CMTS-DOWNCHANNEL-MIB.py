#
# PySNMP MIB module CADANT-CMTS-DOWNCHANNEL-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/CADANT-CMTS-DOWNCHANNEL-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 17:27:05 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
ObjectIdentifier, Integer, OctetString = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "Integer", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ConstraintsUnion, ValueRangeConstraint, SingleValueConstraint, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ConstraintsUnion", "ValueRangeConstraint", "SingleValueConstraint", "ValueSizeConstraint")
cadSpectrum, = mibBuilder.importSymbols("CADANT-PRODUCTS-MIB", "cadSpectrum")
CardId, = mibBuilder.importSymbols("CADANT-TC", "CardId")
TenthdBmV, = mibBuilder.importSymbols("DOCS-IF-MIB", "TenthdBmV")
InterfaceIndex, = mibBuilder.importSymbols("IF-MIB", "InterfaceIndex")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
MibScalar, MibTable, MibTableRow, MibTableColumn, ModuleIdentity, Unsigned32, Integer32, NotificationType, Bits, iso, ObjectIdentity, MibIdentifier, Counter64, TimeTicks, Counter32, IpAddress, Gauge32 = mibBuilder.importSymbols("SNMPv2-SMI", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "ModuleIdentity", "Unsigned32", "Integer32", "NotificationType", "Bits", "iso", "ObjectIdentity", "MibIdentifier", "Counter64", "TimeTicks", "Counter32", "IpAddress", "Gauge32")
TruthValue, TextualConvention, RowStatus, TimeInterval, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TruthValue", "TextualConvention", "RowStatus", "TimeInterval", "DisplayString")
cadDownchannelMib = ModuleIdentity((1, 3, 6, 1, 4, 1, 4998, 1, 1, 15, 2))
cadDownchannelMib.setRevisions(('2015-10-27 00:00', '2015-10-07 00:00', '2015-09-30 00:00', '2015-09-08 00:00', '2015-08-19 00:00', '2015-08-12 00:00', '2015-06-23 00:00', '2015-05-01 00:00', '2015-04-27 00:00', '2015-03-04 00:00', '2015-02-18 00:00', '2015-02-17 00:00', '2015-02-13 00:00', '2015-02-06 00:00', '2015-01-16 00:00', '2014-11-26 00:00', '2014-11-17 00:00', '2014-05-20 00:00', '2014-04-03 00:00', '2014-01-16 00:00', '2013-10-13 00:00', '2013-03-15 00:00', '2013-02-26 00:00', '2013-01-14 00:00', '2012-10-17 00:00', '2012-10-15 00:00', '2011-09-27 00:00', '2011-08-30 00:00', '2010-06-10 00:00', '2010-05-03 00:00', '2010-04-01 00:00', '2009-12-16 00:00', '2008-04-03 00:00', '2007-10-09 00:00', '2007-09-28 00:00', '2007-02-07 00:00', '2007-01-22 00:00', '2006-11-01 00:00', '2006-08-30 00:00', '2006-08-28 00:00', '2006-02-24 00:00', '2005-06-21 00:00', '2004-12-03 00:00', '2004-03-04 00:00', '2003-07-03 00:00', '2002-12-03 00:00',))
if mibBuilder.loadTexts: cadDownchannelMib.setLastUpdated('201510270000Z')
if mibBuilder.loadTexts: cadDownchannelMib.setOrganization('ARRIS Group, Inc.')
class OfdmProfileId(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(ValueRangeConstraint(1, 3), ValueRangeConstraint(256, 256), )
class CerOfdmModType(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 2, 4, 6, 7, 8, 9, 10, 11, 12, 13, 14))
    namedValues = NamedValues(("qam0", 0), ("qpsk", 2), ("qam16", 4), ("qam64", 6), ("qam128", 7), ("qam256", 8), ("qam512", 9), ("qam1024", 10), ("qam2048", 11), ("qam4096", 12), ("qam8192", 13), ("qam16384", 14))

class CerOfdmModBitsType(TextualConvention, Bits):
    status = 'current'
    namedValues = NamedValues(("qam32768", 0), ("qam16384", 1), ("qam8192", 2), ("qam4096", 3), ("qam2048", 4), ("qam1024", 5), ("qam512", 6), ("qam256", 7), ("qam128", 8), ("qam64", 9), ("qam32", 10), ("qam16", 11), ("qam8", 12), ("qpsk", 13), ("bpsk", 14), ("zeroBitload", 15))

cadIfDownstreamChannelTable = MibTable((1, 3, 6, 1, 4, 1, 4998, 1, 1, 15, 2, 1), )
if mibBuilder.loadTexts: cadIfDownstreamChannelTable.setStatus('current')
cadIfDownstreamChannelEntry = MibTableRow((1, 3, 6, 1, 4, 1, 4998, 1, 1, 15, 2, 1, 1), ).setIndexNames((0, "CADANT-CMTS-DOWNCHANNEL-MIB", "cadIfDownChannelIfIndex"))
if mibBuilder.loadTexts: cadIfDownstreamChannelEntry.setStatus('current')
cadIfDownChannelId = MibTableColumn((1, 3, 6, 1, 4, 1, 4998, 1, 1, 15, 2, 1, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(-1, 255))).setMaxAccess("readonly")
if mibBuilder.loadTexts: cadIfDownChannelId.setStatus('current')
cadIfDownChannelFrequency = MibTableColumn((1, 3, 6, 1, 4, 1, 4998, 1, 1, 15, 2, 1, 1, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 1000000000))).setUnits('hertz').setMaxAccess("readwrite")
if mibBuilder.loadTexts: cadIfDownChannelFrequency.setStatus('current')
cadIfDownChannelWidth = MibTableColumn((1, 3, 6, 1, 4, 1, 4998, 1, 1, 15, 2, 1, 1, 3), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 16000000)).clone(6000000)).setUnits('hertz').setMaxAccess("readwrite")
if mibBuilder.loadTexts: cadIfDownChannelWidth.setStatus('current')
cadIfDownChannelModulation = MibTableColumn((1, 3, 6, 1, 4, 1, 4998, 1, 1, 15, 2, 1, 1, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))).clone(namedValues=NamedValues(("unknown", 1), ("other", 2), ("qam64", 3), ("qam256", 4))).clone('qam256')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cadIfDownChannelModulation.setStatus('current')
cadIfDownChannelInterleave = MibTableColumn((1, 3, 6, 1, 4, 1, 4998, 1, 1, 15, 2, 1, 1, 5), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15))).clone(namedValues=NamedValues(("unknown", 1), ("other", 2), ("taps8Increment16", 3), ("taps16Increment8", 4), ("taps32Increment4", 5), ("taps64Increment2", 6), ("taps128Increment1", 7), ("taps12increment17", 8), ("taps128increment2", 9), ("taps128increment3", 10), ("taps128increment4", 11), ("taps128increment5", 12), ("taps128increment6", 13), ("taps128increment7", 14), ("taps128increment8", 15))).clone('taps32Increment4')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cadIfDownChannelInterleave.setStatus('current')
cadIfDownChannelPower = MibTableColumn((1, 3, 6, 1, 4, 1, 4998, 1, 1, 15, 2, 1, 1, 6), TenthdBmV().subtype(subtypeSpec=ConstraintsUnion(ValueRangeConstraint(0, 0), ValueRangeConstraint(250, 600), )).clone(380)).setUnits('dBmV').setMaxAccess("readwrite")
if mibBuilder.loadTexts: cadIfDownChannelPower.setStatus('current')
cadIfDownChannelPowerFineAdj = MibTableColumn((1, 3, 6, 1, 4, 1, 4998, 1, 1, 15, 2, 1, 1, 7), Integer32().subtype(subtypeSpec=ValueRangeConstraint(-80, 0))).setUnits('Steps').setMaxAccess("readwrite")
if mibBuilder.loadTexts: cadIfDownChannelPowerFineAdj.setStatus('current')
cadIfCmtsCardNumber = MibTableColumn((1, 3, 6, 1, 4, 1, 4998, 1, 1, 15, 2, 1, 1, 19), CardId()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cadIfCmtsCardNumber.setStatus('current')
cadIfDownChannelCACL1Threshold = MibTableColumn((1, 3, 6, 1, 4, 1, 4998, 1, 1, 15, 2, 1, 1, 21), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 1000)).clone(90)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cadIfDownChannelCACL1Threshold.setStatus('current')
cadIfDownChannelCACL2Threshold = MibTableColumn((1, 3, 6, 1, 4, 1, 4998, 1, 1, 15, 2, 1, 1, 22), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 1000)).clone(100)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cadIfDownChannelCACL2Threshold.setStatus('current')
cadIfDownChannelCACL3Threshold = MibTableColumn((1, 3, 6, 1, 4, 1, 4998, 1, 1, 15, 2, 1, 1, 23), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 1000)).clone(500)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cadIfDownChannelCACL3Threshold.setStatus('current')
cadIfDownChannelMaxRoundTripDelay = MibTableColumn((1, 3, 6, 1, 4, 1, 4998, 1, 1, 15, 2, 1, 1, 24), Integer32().subtype(subtypeSpec=ValueRangeConstraint(200, 1600)).clone(1600)).setUnits('Microseconds').setMaxAccess("readwrite")
if mibBuilder.loadTexts: cadIfDownChannelMaxRoundTripDelay.setStatus('current')
cadIfDownChannelAnnex = MibTableColumn((1, 3, 6, 1, 4, 1, 4998, 1, 1, 15, 2, 1, 1, 26), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5))).clone(namedValues=NamedValues(("unknown", 1), ("other", 2), ("annexA", 3), ("annexB", 4), ("annexC", 5))).clone('annexB')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cadIfDownChannelAnnex.setStatus('current')
cadIfDownChannelPCNormAllowedUsage = MibTableColumn((1, 3, 6, 1, 4, 1, 4998, 1, 1, 15, 2, 1, 1, 27), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 100))).setUnits('percent').setMaxAccess("readwrite")
if mibBuilder.loadTexts: cadIfDownChannelPCNormAllowedUsage.setStatus('current')
cadIfDownChannelPCNormResUsage = MibTableColumn((1, 3, 6, 1, 4, 1, 4998, 1, 1, 15, 2, 1, 1, 28), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 100))).setUnits('percent').setMaxAccess("readwrite")
if mibBuilder.loadTexts: cadIfDownChannelPCNormResUsage.setStatus('current')
cadIfDownChannelPCEmerAllowedUsage = MibTableColumn((1, 3, 6, 1, 4, 1, 4998, 1, 1, 15, 2, 1, 1, 29), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 100))).setUnits('percent').setMaxAccess("readwrite")
if mibBuilder.loadTexts: cadIfDownChannelPCEmerAllowedUsage.setStatus('current')
cadIfDownChannelPCEmerResUsage = MibTableColumn((1, 3, 6, 1, 4, 1, 4998, 1, 1, 15, 2, 1, 1, 30), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 100))).setUnits('percent').setMaxAccess("readwrite")
if mibBuilder.loadTexts: cadIfDownChannelPCEmerResUsage.setStatus('current')
cadIfDownChannelPCTotalAllowedUsage = MibTableColumn((1, 3, 6, 1, 4, 1, 4998, 1, 1, 15, 2, 1, 1, 31), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 100))).setUnits('percent').setMaxAccess("readwrite")
if mibBuilder.loadTexts: cadIfDownChannelPCTotalAllowedUsage.setStatus('current')
cadIfDownChannelPCPreemptionAllowed = MibTableColumn((1, 3, 6, 1, 4, 1, 4998, 1, 1, 15, 2, 1, 1, 32), TruthValue()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cadIfDownChannelPCPreemptionAllowed.setStatus('current')
cadIfDownChannelIfIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 4998, 1, 1, 15, 2, 1, 1, 37), InterfaceIndex()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cadIfDownChannelIfIndex.setStatus('current')
cadIfDownChannelPrimaryCapable = MibTableColumn((1, 3, 6, 1, 4, 1, 4998, 1, 1, 15, 2, 1, 1, 38), TruthValue().clone('true')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cadIfDownChannelPrimaryCapable.setStatus('current')
cadIfDownSpectralInversion = MibTableColumn((1, 3, 6, 1, 4, 1, 4998, 1, 1, 15, 2, 1, 1, 39), TruthValue().clone('false')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cadIfDownSpectralInversion.setStatus('current')
cadDownChannelParams = MibIdentifier((1, 3, 6, 1, 4, 1, 4998, 1, 1, 15, 2, 2))
cadDownChannelMaxFrequency = MibScalar((1, 3, 6, 1, 4, 1, 4998, 1, 1, 15, 2, 2, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(ValueRangeConstraint(858000000, 858000000), ValueRangeConstraint(867000000, 867000000), ValueRangeConstraint(999000000, 999000000), )).clone(867000000)).setUnits('hertz').setMaxAccess("readwrite")
if mibBuilder.loadTexts: cadDownChannelMaxFrequency.setStatus('current')
cadDownChannelMinFrequency = MibScalar((1, 3, 6, 1, 4, 1, 4998, 1, 1, 15, 2, 2, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(ValueRangeConstraint(57000000, 57000000), ValueRangeConstraint(85000000, 85000000), ValueRangeConstraint(91000000, 91000000), ValueRangeConstraint(112000000, 112000000), )).clone(91000000)).setUnits('hertz').setMaxAccess("readwrite")
if mibBuilder.loadTexts: cadDownChannelMinFrequency.setStatus('current')
cadDownChannelAgcEnable = MibScalar((1, 3, 6, 1, 4, 1, 4998, 1, 1, 15, 2, 2, 3), TruthValue().clone('true')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cadDownChannelAgcEnable.setStatus('current')
cadDownChannelOorRecoveryEnable = MibScalar((1, 3, 6, 1, 4, 1, 4998, 1, 1, 15, 2, 2, 4), TruthValue().clone('false')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cadDownChannelOorRecoveryEnable.setStatus('current')
cadDsOfdmOcdDpdPlcInterval = MibScalar((1, 3, 6, 1, 4, 1, 4998, 1, 1, 15, 2, 2, 5), Integer32().subtype(subtypeSpec=ValueRangeConstraint(50, 250)).clone(200)).setUnits('milliseconds').setMaxAccess("readwrite")
if mibBuilder.loadTexts: cadDsOfdmOcdDpdPlcInterval.setStatus('current')
cadDsOfdmDpdProfAInterval = MibScalar((1, 3, 6, 1, 4, 1, 4998, 1, 1, 15, 2, 2, 6), Integer32().subtype(subtypeSpec=ValueRangeConstraint(100, 600)).clone(500)).setUnits('milliseconds').setMaxAccess("readwrite")
if mibBuilder.loadTexts: cadDsOfdmDpdProfAInterval.setStatus('current')
cadDownChannelLsredMinThresh = MibScalar((1, 3, 6, 1, 4, 1, 4998, 1, 1, 15, 2, 2, 7), Integer32().subtype(subtypeSpec=ValueRangeConstraint(10, 2000)).clone(2000)).setUnits('milliseconds').setMaxAccess("readwrite")
if mibBuilder.loadTexts: cadDownChannelLsredMinThresh.setStatus('current')
cadDownChannelLsredMaxThresh = MibScalar((1, 3, 6, 1, 4, 1, 4998, 1, 1, 15, 2, 2, 8), Integer32().subtype(subtypeSpec=ValueRangeConstraint(10, 2500)).clone(2500)).setUnits('milliseconds').setMaxAccess("readwrite")
if mibBuilder.loadTexts: cadDownChannelLsredMaxThresh.setStatus('current')
cadDownChannelLsredMaxProb = MibScalar((1, 3, 6, 1, 4, 1, 4998, 1, 1, 15, 2, 2, 9), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 10000)).clone(10000)).setUnits('0.01%').setMaxAccess("readwrite")
if mibBuilder.loadTexts: cadDownChannelLsredMaxProb.setStatus('current')
cadDownChannelVoiceShaping = MibScalar((1, 3, 6, 1, 4, 1, 4998, 1, 1, 15, 2, 2, 10), TruthValue().clone('false')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cadDownChannelVoiceShaping.setStatus('current')
cadIfDsOfdmPowerTable = MibTable((1, 3, 6, 1, 4, 1, 4998, 1, 1, 15, 2, 3), )
if mibBuilder.loadTexts: cadIfDsOfdmPowerTable.setStatus('current')
cadIfDsOfdmPowerEntry = MibTableRow((1, 3, 6, 1, 4, 1, 4998, 1, 1, 15, 2, 3, 1), ).setIndexNames((0, "CADANT-CMTS-DOWNCHANNEL-MIB", "cadIfDsOfdmPowerIfIndex"), (0, "CADANT-CMTS-DOWNCHANNEL-MIB", "cadIfDsOfdmPowerFrequency"))
if mibBuilder.loadTexts: cadIfDsOfdmPowerEntry.setStatus('current')
cadIfDsOfdmPowerIfIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 4998, 1, 1, 15, 2, 3, 1, 1), InterfaceIndex())
if mibBuilder.loadTexts: cadIfDsOfdmPowerIfIndex.setStatus('current')
cadIfDsOfdmPowerFrequency = MibTableColumn((1, 3, 6, 1, 4, 1, 4998, 1, 1, 15, 2, 3, 1, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 192))).setUnits('MHz')
if mibBuilder.loadTexts: cadIfDsOfdmPowerFrequency.setStatus('current')
cadIfDsOfdmPowerFineAdjustment = MibTableColumn((1, 3, 6, 1, 4, 1, 4998, 1, 1, 15, 2, 3, 1, 3), TenthdBmV().subtype(subtypeSpec=ValueRangeConstraint(-80, 0))).setUnits('dBmVtenths').setMaxAccess("readwrite")
if mibBuilder.loadTexts: cadIfDsOfdmPowerFineAdjustment.setStatus('current')
cadIfDsOfdmPowerCurrLevel = MibTableColumn((1, 3, 6, 1, 4, 1, 4998, 1, 1, 15, 2, 3, 1, 4), TenthdBmV()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cadIfDsOfdmPowerCurrLevel.setStatus('current')
cadIfDsOfdmPowerMinLevel = MibTableColumn((1, 3, 6, 1, 4, 1, 4998, 1, 1, 15, 2, 3, 1, 5), TenthdBmV()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cadIfDsOfdmPowerMinLevel.setStatus('current')
cadIfDsOfdmPowerMaxLevel = MibTableColumn((1, 3, 6, 1, 4, 1, 4998, 1, 1, 15, 2, 3, 1, 6), TenthdBmV()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cadIfDsOfdmPowerMaxLevel.setStatus('current')
cadIfDsOfdmChlTable = MibTable((1, 3, 6, 1, 4, 1, 4998, 1, 1, 15, 2, 5), )
if mibBuilder.loadTexts: cadIfDsOfdmChlTable.setStatus('current')
cadIfDsOfdmChlEntry = MibTableRow((1, 3, 6, 1, 4, 1, 4998, 1, 1, 15, 2, 5, 1), ).setIndexNames((0, "CADANT-CMTS-DOWNCHANNEL-MIB", "cadIfDsOfdmChlIfIndex"))
if mibBuilder.loadTexts: cadIfDsOfdmChlEntry.setStatus('current')
cadIfDsOfdmChlIfIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 4998, 1, 1, 15, 2, 5, 1, 1), InterfaceIndex())
if mibBuilder.loadTexts: cadIfDsOfdmChlIfIndex.setStatus('current')
cadIfDsOfdmChlLowFreq = MibTableColumn((1, 3, 6, 1, 4, 1, 4998, 1, 1, 15, 2, 5, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(ValueRangeConstraint(0, 0), ValueRangeConstraint(108000000, 1770000000), ))).setUnits('hertz').setMaxAccess("readwrite")
if mibBuilder.loadTexts: cadIfDsOfdmChlLowFreq.setStatus('current')
cadIfDsOfdmChlHighFreq = MibTableColumn((1, 3, 6, 1, 4, 1, 4998, 1, 1, 15, 2, 5, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(ValueRangeConstraint(0, 0), ValueRangeConstraint(132000000, 1794000000), ))).setUnits('hertz').setMaxAccess("readwrite")
if mibBuilder.loadTexts: cadIfDsOfdmChlHighFreq.setStatus('current')
cadIfDsOfdmChlPlcBlkLowSubcCentFreq = MibTableColumn((1, 3, 6, 1, 4, 1, 4998, 1, 1, 15, 2, 5, 1, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(ValueRangeConstraint(0, 0), ValueRangeConstraint(108000000, 1788000000), ))).setUnits('hertz').setMaxAccess("readwrite")
if mibBuilder.loadTexts: cadIfDsOfdmChlPlcBlkLowSubcCentFreq.setStatus('current')
cadIfDsOfdmChlCyclicPrefix = MibTableColumn((1, 3, 6, 1, 4, 1, 4998, 1, 1, 15, 2, 5, 1, 5), Integer32().subtype(subtypeSpec=ConstraintsUnion(ValueRangeConstraint(192, 192), ValueRangeConstraint(256, 256), ValueRangeConstraint(512, 512), ValueRangeConstraint(768, 768), ValueRangeConstraint(1024, 1024), )).clone(1024)).setUnits('samples').setMaxAccess("readwrite")
if mibBuilder.loadTexts: cadIfDsOfdmChlCyclicPrefix.setStatus('current')
cadIfDsOfdmChlRolloffPeriod = MibTableColumn((1, 3, 6, 1, 4, 1, 4998, 1, 1, 15, 2, 5, 1, 6), Integer32().subtype(subtypeSpec=ConstraintsUnion(ValueRangeConstraint(0, 0), ValueRangeConstraint(64, 64), ValueRangeConstraint(128, 128), ValueRangeConstraint(192, 192), ValueRangeConstraint(256, 256), )).clone(256)).setUnits('samples').setMaxAccess("readwrite")
if mibBuilder.loadTexts: cadIfDsOfdmChlRolloffPeriod.setStatus('current')
cadIfDsOfdmChlTimeIntlvrDepth = MibTableColumn((1, 3, 6, 1, 4, 1, 4998, 1, 1, 15, 2, 5, 1, 7), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 32)).clone(1)).setUnits('symbols').setMaxAccess("readwrite")
if mibBuilder.loadTexts: cadIfDsOfdmChlTimeIntlvrDepth.setStatus('current')
cadIfDsOfdmChlSubcSpacing = MibTableColumn((1, 3, 6, 1, 4, 1, 4998, 1, 1, 15, 2, 5, 1, 8), Integer32().subtype(subtypeSpec=ConstraintsUnion(ValueRangeConstraint(25000, 25000), ValueRangeConstraint(50000, 50000), )).clone(50000)).setUnits('hertz').setMaxAccess("readwrite")
if mibBuilder.loadTexts: cadIfDsOfdmChlSubcSpacing.setStatus('current')
cadIfDsOfdmChlContPilotScaleFactor = MibTableColumn((1, 3, 6, 1, 4, 1, 4998, 1, 1, 15, 2, 5, 1, 9), Integer32().subtype(subtypeSpec=ValueRangeConstraint(48, 120)).clone(48)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cadIfDsOfdmChlContPilotScaleFactor.setStatus('current')
cadIfDsOfdmChlMaxRoundTripDelay = MibTableColumn((1, 3, 6, 1, 4, 1, 4998, 1, 1, 15, 2, 5, 1, 10), Integer32().subtype(subtypeSpec=ValueRangeConstraint(200, 1600)).clone(800)).setUnits('Microseconds').setMaxAccess("readwrite")
if mibBuilder.loadTexts: cadIfDsOfdmChlMaxRoundTripDelay.setStatus('current')
cadIfDsOfdmChlPCNormAllowedUsage = MibTableColumn((1, 3, 6, 1, 4, 1, 4998, 1, 1, 15, 2, 5, 1, 11), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 100)).clone(50)).setUnits('percent').setMaxAccess("readwrite")
if mibBuilder.loadTexts: cadIfDsOfdmChlPCNormAllowedUsage.setStatus('current')
cadIfDsOfdmChlPCNormResUsage = MibTableColumn((1, 3, 6, 1, 4, 1, 4998, 1, 1, 15, 2, 5, 1, 12), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 100))).setUnits('percent').setMaxAccess("readwrite")
if mibBuilder.loadTexts: cadIfDsOfdmChlPCNormResUsage.setStatus('current')
cadIfDsOfdmChlPCEmerAllowedUsage = MibTableColumn((1, 3, 6, 1, 4, 1, 4998, 1, 1, 15, 2, 5, 1, 13), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 100)).clone(70)).setUnits('percent').setMaxAccess("readwrite")
if mibBuilder.loadTexts: cadIfDsOfdmChlPCEmerAllowedUsage.setStatus('current')
cadIfDsOfdmChlPCEmerResUsage = MibTableColumn((1, 3, 6, 1, 4, 1, 4998, 1, 1, 15, 2, 5, 1, 14), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 100))).setUnits('percent').setMaxAccess("readwrite")
if mibBuilder.loadTexts: cadIfDsOfdmChlPCEmerResUsage.setStatus('current')
cadIfDsOfdmChlPCTotalAllowedUsage = MibTableColumn((1, 3, 6, 1, 4, 1, 4998, 1, 1, 15, 2, 5, 1, 15), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 100)).clone(70)).setUnits('percent').setMaxAccess("readwrite")
if mibBuilder.loadTexts: cadIfDsOfdmChlPCTotalAllowedUsage.setStatus('current')
cadIfDsOfdmChlPCPreemptionAllowed = MibTableColumn((1, 3, 6, 1, 4, 1, 4998, 1, 1, 15, 2, 5, 1, 16), TruthValue().clone('true')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cadIfDsOfdmChlPCPreemptionAllowed.setStatus('current')
cadIfDsOfdmChlRfPortBasePower = MibTableColumn((1, 3, 6, 1, 4, 1, 4998, 1, 1, 15, 2, 5, 1, 17), TenthdBmV().subtype(subtypeSpec=ValueRangeConstraint(250, 600)).clone(380)).setUnits('dBmV').setMaxAccess("readwrite")
if mibBuilder.loadTexts: cadIfDsOfdmChlRfPortBasePower.setStatus('current')
cadIfDsOfdmChlSubcZeroCentFreq = MibTableColumn((1, 3, 6, 1, 4, 1, 4998, 1, 1, 15, 2, 5, 1, 18), Integer32()).setUnits('hertz').setMaxAccess("readonly")
if mibBuilder.loadTexts: cadIfDsOfdmChlSubcZeroCentFreq.setStatus('current')
cadIfDsOfdmChlLowActSubcCentFreq = MibTableColumn((1, 3, 6, 1, 4, 1, 4998, 1, 1, 15, 2, 5, 1, 19), Integer32()).setUnits('hertz').setMaxAccess("readonly")
if mibBuilder.loadTexts: cadIfDsOfdmChlLowActSubcCentFreq.setStatus('current')
cadIfDsOfdmChlHighActSubcCentFreq = MibTableColumn((1, 3, 6, 1, 4, 1, 4998, 1, 1, 15, 2, 5, 1, 20), Integer32()).setUnits('hertz').setMaxAccess("readonly")
if mibBuilder.loadTexts: cadIfDsOfdmChlHighActSubcCentFreq.setStatus('current')
cadIfDsOfdmChlPlcLowSubcCentFreq = MibTableColumn((1, 3, 6, 1, 4, 1, 4998, 1, 1, 15, 2, 5, 1, 21), Integer32()).setUnits('hertz').setMaxAccess("readonly")
if mibBuilder.loadTexts: cadIfDsOfdmChlPlcLowSubcCentFreq.setStatus('current')
cadIfDsOfdmChlNumActSubc = MibTableColumn((1, 3, 6, 1, 4, 1, 4998, 1, 1, 15, 2, 5, 1, 22), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cadIfDsOfdmChlNumActSubc.setStatus('current')
cadIfDsOfdmChlDataTable = MibTable((1, 3, 6, 1, 4, 1, 4998, 1, 1, 15, 2, 6), )
if mibBuilder.loadTexts: cadIfDsOfdmChlDataTable.setStatus('current')
cadIfDsOfdmChlDataEntry = MibTableRow((1, 3, 6, 1, 4, 1, 4998, 1, 1, 15, 2, 6, 1), )
cadIfDsOfdmChlEntry.registerAugmentions(("CADANT-CMTS-DOWNCHANNEL-MIB", "cadIfDsOfdmChlDataEntry"))
cadIfDsOfdmChlDataEntry.setIndexNames(*cadIfDsOfdmChlEntry.getIndexNames())
if mibBuilder.loadTexts: cadIfDsOfdmChlDataEntry.setStatus('current')
cadIfDsOfdmChlDataNumActSubcarriers = MibTableColumn((1, 3, 6, 1, 4, 1, 4998, 1, 1, 15, 2, 6, 1, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(ValueRangeConstraint(0, 0), ValueRangeConstraint(200, 7600), ))).setMaxAccess("readonly")
if mibBuilder.loadTexts: cadIfDsOfdmChlDataNumActSubcarriers.setStatus('current')
cadIfDsOfdmChlDataNumContPilots = MibTableColumn((1, 3, 6, 1, 4, 1, 4998, 1, 1, 15, 2, 6, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(ValueRangeConstraint(0, 0), ValueRangeConstraint(16, 128), ))).setMaxAccess("readonly")
if mibBuilder.loadTexts: cadIfDsOfdmChlDataNumContPilots.setStatus('current')
cadDsOfdmProfileTable = MibTable((1, 3, 6, 1, 4, 1, 4998, 1, 1, 15, 2, 8), )
if mibBuilder.loadTexts: cadDsOfdmProfileTable.setStatus('current')
cadDsOfdmProfileEntry = MibTableRow((1, 3, 6, 1, 4, 1, 4998, 1, 1, 15, 2, 8, 1), ).setIndexNames((0, "CADANT-CMTS-DOWNCHANNEL-MIB", "cadDsOfdmProfileIfIndex"), (0, "CADANT-CMTS-DOWNCHANNEL-MIB", "cadDsOfdmProfileId"))
if mibBuilder.loadTexts: cadDsOfdmProfileEntry.setStatus('current')
cadDsOfdmProfileIfIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 4998, 1, 1, 15, 2, 8, 1, 1), InterfaceIndex())
if mibBuilder.loadTexts: cadDsOfdmProfileIfIndex.setStatus('current')
cadDsOfdmProfileId = MibTableColumn((1, 3, 6, 1, 4, 1, 4998, 1, 1, 15, 2, 8, 1, 2), OfdmProfileId())
if mibBuilder.loadTexts: cadDsOfdmProfileId.setStatus('current')
cadDsOfdmProfileDefBitload = MibTableColumn((1, 3, 6, 1, 4, 1, 4998, 1, 1, 15, 2, 8, 1, 3), CerOfdmModType().clone('qam1024')).setMaxAccess("readcreate")
if mibBuilder.loadTexts: cadDsOfdmProfileDefBitload.setStatus('current')
cadDsOfdmProfileRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 4998, 1, 1, 15, 2, 8, 1, 4), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: cadDsOfdmProfileRowStatus.setStatus('current')
cadDsOfdmProfStatTable = MibTable((1, 3, 6, 1, 4, 1, 4998, 1, 1, 15, 2, 9), )
if mibBuilder.loadTexts: cadDsOfdmProfStatTable.setStatus('current')
cadDsOfdmProfStatEntry = MibTableRow((1, 3, 6, 1, 4, 1, 4998, 1, 1, 15, 2, 9, 1), ).setIndexNames((0, "CADANT-CMTS-DOWNCHANNEL-MIB", "cadDsOfdmProfStatIfIndex"), (0, "CADANT-CMTS-DOWNCHANNEL-MIB", "cadDsOfdmProfStatProfId"))
if mibBuilder.loadTexts: cadDsOfdmProfStatEntry.setStatus('current')
cadDsOfdmProfStatIfIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 4998, 1, 1, 15, 2, 9, 1, 1), InterfaceIndex())
if mibBuilder.loadTexts: cadDsOfdmProfStatIfIndex.setStatus('current')
cadDsOfdmProfStatProfId = MibTableColumn((1, 3, 6, 1, 4, 1, 4998, 1, 1, 15, 2, 9, 1, 2), OfdmProfileId())
if mibBuilder.loadTexts: cadDsOfdmProfStatProfId.setStatus('current')
cadDsOfdmProfStatAvgBitsPerSubc = MibTableColumn((1, 3, 6, 1, 4, 1, 4998, 1, 1, 15, 2, 9, 1, 3), Unsigned32()).setUnits('HundredthBit').setMaxAccess("readonly")
if mibBuilder.loadTexts: cadDsOfdmProfStatAvgBitsPerSubc.setStatus('current')
cadDsOfdmProfStatReqMods = MibTableColumn((1, 3, 6, 1, 4, 1, 4998, 1, 1, 15, 2, 9, 1, 4), CerOfdmModBitsType()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cadDsOfdmProfStatReqMods.setStatus('current')
cadDsOfdmProfStatEtherFrameBytes = MibTableColumn((1, 3, 6, 1, 4, 1, 4998, 1, 1, 15, 2, 9, 1, 5), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cadDsOfdmProfStatEtherFrameBytes.setStatus('current')
cadDsOfdmProfStatTotalCodewords = MibTableColumn((1, 3, 6, 1, 4, 1, 4998, 1, 1, 15, 2, 9, 1, 6), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cadDsOfdmProfStatTotalCodewords.setStatus('current')
cadDsOfdmProfStat30SecCwUtil = MibTableColumn((1, 3, 6, 1, 4, 1, 4998, 1, 1, 15, 2, 9, 1, 7), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(0, 100))).setMaxAccess("readonly")
if mibBuilder.loadTexts: cadDsOfdmProfStat30SecCwUtil.setStatus('current')
cadDsOfdmProfStat30SecCwEff = MibTableColumn((1, 3, 6, 1, 4, 1, 4998, 1, 1, 15, 2, 9, 1, 8), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(0, 100))).setMaxAccess("readonly")
if mibBuilder.loadTexts: cadDsOfdmProfStat30SecCwEff.setStatus('current')
cadDsOfdmProfExceptionTable = MibTable((1, 3, 6, 1, 4, 1, 4998, 1, 1, 15, 2, 11), )
if mibBuilder.loadTexts: cadDsOfdmProfExceptionTable.setStatus('current')
cadDsOfdmProfExceptionEntry = MibTableRow((1, 3, 6, 1, 4, 1, 4998, 1, 1, 15, 2, 11, 1), ).setIndexNames((0, "CADANT-CMTS-DOWNCHANNEL-MIB", "cadDsOfdmProfExceptionIfIndex"), (0, "CADANT-CMTS-DOWNCHANNEL-MIB", "cadDsOfdmProfExceptionProfId"), (0, "CADANT-CMTS-DOWNCHANNEL-MIB", "cadDsOfdmProfExceptionLowFreq"))
if mibBuilder.loadTexts: cadDsOfdmProfExceptionEntry.setStatus('current')
cadDsOfdmProfExceptionIfIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 4998, 1, 1, 15, 2, 11, 1, 1), InterfaceIndex())
if mibBuilder.loadTexts: cadDsOfdmProfExceptionIfIndex.setStatus('current')
cadDsOfdmProfExceptionProfId = MibTableColumn((1, 3, 6, 1, 4, 1, 4998, 1, 1, 15, 2, 11, 1, 2), OfdmProfileId())
if mibBuilder.loadTexts: cadDsOfdmProfExceptionProfId.setStatus('current')
cadDsOfdmProfExceptionLowFreq = MibTableColumn((1, 3, 6, 1, 4, 1, 4998, 1, 1, 15, 2, 11, 1, 3), Integer32().subtype(subtypeSpec=ValueRangeConstraint(108000000, 1770000000))).setUnits('hertz')
if mibBuilder.loadTexts: cadDsOfdmProfExceptionLowFreq.setStatus('current')
cadDsOfdmProfExceptionHighFreq = MibTableColumn((1, 3, 6, 1, 4, 1, 4998, 1, 1, 15, 2, 11, 1, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(ValueRangeConstraint(0, 0), ValueRangeConstraint(108000000, 1770000000), ))).setUnits('hertz').setMaxAccess("readcreate")
if mibBuilder.loadTexts: cadDsOfdmProfExceptionHighFreq.setStatus('current')
cadDsOfdmProfExceptionSkip = MibTableColumn((1, 3, 6, 1, 4, 1, 4998, 1, 1, 15, 2, 11, 1, 5), TruthValue().clone('false')).setMaxAccess("readcreate")
if mibBuilder.loadTexts: cadDsOfdmProfExceptionSkip.setStatus('current')
cadDsOfdmProfExceptionMainBitload = MibTableColumn((1, 3, 6, 1, 4, 1, 4998, 1, 1, 15, 2, 11, 1, 6), CerOfdmModType().clone('qam1024')).setMaxAccess("readcreate")
if mibBuilder.loadTexts: cadDsOfdmProfExceptionMainBitload.setStatus('current')
cadDsOfdmProfExceptionOddBitload = MibTableColumn((1, 3, 6, 1, 4, 1, 4998, 1, 1, 15, 2, 11, 1, 7), CerOfdmModType().clone('qam0')).setMaxAccess("readcreate")
if mibBuilder.loadTexts: cadDsOfdmProfExceptionOddBitload.setStatus('current')
cadDsOfdmProfExceptionRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 4998, 1, 1, 15, 2, 11, 1, 8), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: cadDsOfdmProfExceptionRowStatus.setStatus('current')
mibBuilder.exportSymbols("CADANT-CMTS-DOWNCHANNEL-MIB", cadIfDownChannelPower=cadIfDownChannelPower, cadIfDownChannelCACL3Threshold=cadIfDownChannelCACL3Threshold, CerOfdmModBitsType=CerOfdmModBitsType, cadDsOfdmProfStatEtherFrameBytes=cadDsOfdmProfStatEtherFrameBytes, cadDownChannelLsredMaxThresh=cadDownChannelLsredMaxThresh, cadIfDsOfdmChlDataEntry=cadIfDsOfdmChlDataEntry, cadIfDownstreamChannelEntry=cadIfDownstreamChannelEntry, cadDsOfdmProfileTable=cadDsOfdmProfileTable, cadDownChannelOorRecoveryEnable=cadDownChannelOorRecoveryEnable, cadDownChannelAgcEnable=cadDownChannelAgcEnable, cadIfDownSpectralInversion=cadIfDownSpectralInversion, cadIfDsOfdmChlRolloffPeriod=cadIfDsOfdmChlRolloffPeriod, cadIfDownChannelPCNormResUsage=cadIfDownChannelPCNormResUsage, cadIfDownChannelPowerFineAdj=cadIfDownChannelPowerFineAdj, cadIfDsOfdmChlPCEmerResUsage=cadIfDsOfdmChlPCEmerResUsage, OfdmProfileId=OfdmProfileId, cadDownChannelMaxFrequency=cadDownChannelMaxFrequency, cadIfDsOfdmChlTimeIntlvrDepth=cadIfDsOfdmChlTimeIntlvrDepth, cadDsOfdmProfExceptionProfId=cadDsOfdmProfExceptionProfId, cadIfDsOfdmPowerIfIndex=cadIfDsOfdmPowerIfIndex, cadIfDsOfdmChlPCNormResUsage=cadIfDsOfdmChlPCNormResUsage, cadIfDsOfdmChlPCNormAllowedUsage=cadIfDsOfdmChlPCNormAllowedUsage, cadIfDownChannelPCTotalAllowedUsage=cadIfDownChannelPCTotalAllowedUsage, cadIfDownChannelAnnex=cadIfDownChannelAnnex, cadIfDsOfdmChlCyclicPrefix=cadIfDsOfdmChlCyclicPrefix, cadDownChannelLsredMaxProb=cadDownChannelLsredMaxProb, cadIfDsOfdmChlHighActSubcCentFreq=cadIfDsOfdmChlHighActSubcCentFreq, cadIfDownChannelFrequency=cadIfDownChannelFrequency, cadIfDsOfdmChlTable=cadIfDsOfdmChlTable, cadIfDsOfdmPowerFrequency=cadIfDsOfdmPowerFrequency, cadIfDsOfdmPowerTable=cadIfDsOfdmPowerTable, cadIfDsOfdmChlNumActSubc=cadIfDsOfdmChlNumActSubc, cadIfDownChannelMaxRoundTripDelay=cadIfDownChannelMaxRoundTripDelay, cadIfDownChannelPCPreemptionAllowed=cadIfDownChannelPCPreemptionAllowed, cadDownchannelMib=cadDownchannelMib, cadDsOfdmProfExceptionSkip=cadDsOfdmProfExceptionSkip, cadIfDsOfdmPowerEntry=cadIfDsOfdmPowerEntry, cadIfDsOfdmChlDataNumActSubcarriers=cadIfDsOfdmChlDataNumActSubcarriers, cadDsOfdmOcdDpdPlcInterval=cadDsOfdmOcdDpdPlcInterval, cadIfDsOfdmChlMaxRoundTripDelay=cadIfDsOfdmChlMaxRoundTripDelay, cadDsOfdmProfStatEntry=cadDsOfdmProfStatEntry, cadIfDsOfdmChlLowFreq=cadIfDsOfdmChlLowFreq, cadDsOfdmProfExceptionLowFreq=cadDsOfdmProfExceptionLowFreq, cadIfDsOfdmChlSubcSpacing=cadIfDsOfdmChlSubcSpacing, cadDsOfdmProfExceptionEntry=cadDsOfdmProfExceptionEntry, cadIfDsOfdmChlLowActSubcCentFreq=cadIfDsOfdmChlLowActSubcCentFreq, cadIfDownChannelWidth=cadIfDownChannelWidth, cadIfDsOfdmChlHighFreq=cadIfDsOfdmChlHighFreq, cadIfDsOfdmChlSubcZeroCentFreq=cadIfDsOfdmChlSubcZeroCentFreq, cadIfDsOfdmChlPCPreemptionAllowed=cadIfDsOfdmChlPCPreemptionAllowed, cadDsOfdmProfileRowStatus=cadDsOfdmProfileRowStatus, cadDownChannelMinFrequency=cadDownChannelMinFrequency, cadDsOfdmProfStat30SecCwEff=cadDsOfdmProfStat30SecCwEff, cadDownChannelParams=cadDownChannelParams, cadIfDsOfdmPowerCurrLevel=cadIfDsOfdmPowerCurrLevel, cadDsOfdmProfileDefBitload=cadDsOfdmProfileDefBitload, cadDsOfdmProfExceptionIfIndex=cadDsOfdmProfExceptionIfIndex, cadIfDsOfdmChlIfIndex=cadIfDsOfdmChlIfIndex, cadIfDownChannelPCNormAllowedUsage=cadIfDownChannelPCNormAllowedUsage, cadDsOfdmProfExceptionTable=cadDsOfdmProfExceptionTable, cadDsOfdmProfExceptionMainBitload=cadDsOfdmProfExceptionMainBitload, cadIfDsOfdmChlPCEmerAllowedUsage=cadIfDsOfdmChlPCEmerAllowedUsage, cadIfDsOfdmChlPlcLowSubcCentFreq=cadIfDsOfdmChlPlcLowSubcCentFreq, cadDsOfdmProfStatTable=cadDsOfdmProfStatTable, cadDsOfdmProfExceptionOddBitload=cadDsOfdmProfExceptionOddBitload, cadIfDownChannelCACL1Threshold=cadIfDownChannelCACL1Threshold, cadIfDsOfdmChlPlcBlkLowSubcCentFreq=cadIfDsOfdmChlPlcBlkLowSubcCentFreq, cadDsOfdmProfStatReqMods=cadDsOfdmProfStatReqMods, cadDsOfdmProfStatProfId=cadDsOfdmProfStatProfId, cadIfDownChannelCACL2Threshold=cadIfDownChannelCACL2Threshold, cadIfDsOfdmChlPCTotalAllowedUsage=cadIfDsOfdmChlPCTotalAllowedUsage, CerOfdmModType=CerOfdmModType, cadDsOfdmProfStatTotalCodewords=cadDsOfdmProfStatTotalCodewords, cadDsOfdmProfStatIfIndex=cadDsOfdmProfStatIfIndex, PYSNMP_MODULE_ID=cadDownchannelMib, cadIfDsOfdmChlDataTable=cadIfDsOfdmChlDataTable, cadDsOfdmProfileIfIndex=cadDsOfdmProfileIfIndex, cadDsOfdmDpdProfAInterval=cadDsOfdmDpdProfAInterval, cadIfDownChannelId=cadIfDownChannelId, cadDsOfdmProfileId=cadDsOfdmProfileId, cadDsOfdmProfExceptionRowStatus=cadDsOfdmProfExceptionRowStatus, cadDownChannelVoiceShaping=cadDownChannelVoiceShaping, cadIfDownChannelPCEmerResUsage=cadIfDownChannelPCEmerResUsage, cadIfDownChannelInterleave=cadIfDownChannelInterleave, cadIfDownChannelPrimaryCapable=cadIfDownChannelPrimaryCapable, cadIfDownChannelModulation=cadIfDownChannelModulation, cadDsOfdmProfExceptionHighFreq=cadDsOfdmProfExceptionHighFreq, cadIfDsOfdmChlEntry=cadIfDsOfdmChlEntry, cadIfDsOfdmChlContPilotScaleFactor=cadIfDsOfdmChlContPilotScaleFactor, cadIfDsOfdmChlDataNumContPilots=cadIfDsOfdmChlDataNumContPilots, cadIfDsOfdmPowerMaxLevel=cadIfDsOfdmPowerMaxLevel, cadDsOfdmProfStatAvgBitsPerSubc=cadDsOfdmProfStatAvgBitsPerSubc, cadDownChannelLsredMinThresh=cadDownChannelLsredMinThresh, cadIfDownstreamChannelTable=cadIfDownstreamChannelTable, cadIfDsOfdmPowerFineAdjustment=cadIfDsOfdmPowerFineAdjustment, cadDsOfdmProfileEntry=cadDsOfdmProfileEntry, cadIfCmtsCardNumber=cadIfCmtsCardNumber, cadIfDownChannelIfIndex=cadIfDownChannelIfIndex, cadIfDownChannelPCEmerAllowedUsage=cadIfDownChannelPCEmerAllowedUsage, cadIfDsOfdmPowerMinLevel=cadIfDsOfdmPowerMinLevel, cadIfDsOfdmChlRfPortBasePower=cadIfDsOfdmChlRfPortBasePower, cadDsOfdmProfStat30SecCwUtil=cadDsOfdmProfStat30SecCwUtil)