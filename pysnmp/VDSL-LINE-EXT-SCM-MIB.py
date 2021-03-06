#
# PySNMP MIB module VDSL-LINE-EXT-SCM-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/VDSL-LINE-EXT-SCM-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 21:26:32 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsUnion, ConstraintsIntersection, ValueRangeConstraint, SingleValueConstraint, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "ConstraintsIntersection", "ValueRangeConstraint", "SingleValueConstraint", "ValueSizeConstraint")
ifIndex, = mibBuilder.importSymbols("IF-MIB", "ifIndex")
NotificationGroup, ModuleCompliance, ObjectGroup = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance", "ObjectGroup")
ModuleIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter32, Counter64, Integer32, Bits, Unsigned32, NotificationType, Gauge32, transmission, TimeTicks, MibIdentifier, IpAddress, ObjectIdentity, iso = mibBuilder.importSymbols("SNMPv2-SMI", "ModuleIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter32", "Counter64", "Integer32", "Bits", "Unsigned32", "NotificationType", "Gauge32", "transmission", "TimeTicks", "MibIdentifier", "IpAddress", "ObjectIdentity", "iso")
DisplayString, TextualConvention, RowStatus, TruthValue = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention", "RowStatus", "TruthValue")
vdslLineConfProfileName, = mibBuilder.importSymbols("VDSL-LINE-MIB", "vdslLineConfProfileName")
vdslExtSCMMIB = ModuleIdentity((1, 3, 6, 1, 2, 1, 10, 228))
vdslExtSCMMIB.setRevisions(('2005-04-28 00:00',))
if mibBuilder.loadTexts: vdslExtSCMMIB.setLastUpdated('200504280000Z')
if mibBuilder.loadTexts: vdslExtSCMMIB.setOrganization('ADSLMIB Working Group')
vdslLineExtSCMMib = MibIdentifier((1, 3, 6, 1, 2, 1, 10, 228, 1))
vdslLineExtSCMMibObjects = MibIdentifier((1, 3, 6, 1, 2, 1, 10, 228, 1, 1))
class VdslSCMBandId(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7))
    namedValues = NamedValues(("optionalBand", 1), ("firstDownstreamBand", 2), ("firstUpstreamBand", 3), ("secondDownstreamBand", 4), ("secondUpstreamBand", 5), ("thirdDownstreamBand", 6), ("thirdUpstreamBand", 7))

vdslLineSCMConfProfileBandTable = MibTable((1, 3, 6, 1, 2, 1, 10, 228, 1, 1, 1), )
if mibBuilder.loadTexts: vdslLineSCMConfProfileBandTable.setStatus('current')
vdslLineSCMConfProfileBandEntry = MibTableRow((1, 3, 6, 1, 2, 1, 10, 228, 1, 1, 1, 1), ).setIndexNames((0, "VDSL-LINE-MIB", "vdslLineConfProfileName"), (0, "VDSL-LINE-EXT-SCM-MIB", "vdslLineSCMConfProfileBandId"))
if mibBuilder.loadTexts: vdslLineSCMConfProfileBandEntry.setStatus('current')
vdslLineSCMConfProfileBandId = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 228, 1, 1, 1, 1, 1), VdslSCMBandId())
if mibBuilder.loadTexts: vdslLineSCMConfProfileBandId.setStatus('current')
vdslLineSCMConfProfileBandInUse = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 228, 1, 1, 1, 1, 2), TruthValue()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: vdslLineSCMConfProfileBandInUse.setStatus('current')
vdslLineSCMConfProfileBandCenterFrequency = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 228, 1, 1, 1, 1, 3), Unsigned32()).setUnits('Hz').setMaxAccess("readcreate")
if mibBuilder.loadTexts: vdslLineSCMConfProfileBandCenterFrequency.setStatus('current')
vdslLineSCMConfProfileBandSymbolRate = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 228, 1, 1, 1, 1, 4), Unsigned32()).setUnits('baud').setMaxAccess("readcreate")
if mibBuilder.loadTexts: vdslLineSCMConfProfileBandSymbolRate.setStatus('current')
vdslLineSCMConfProfileBandConstellationSize = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 228, 1, 1, 1, 1, 5), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(0, 16))).setUnits('log2').setMaxAccess("readcreate")
if mibBuilder.loadTexts: vdslLineSCMConfProfileBandConstellationSize.setStatus('current')
vdslLineSCMConfProfileBandTransmitPSDLevel = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 228, 1, 1, 1, 1, 6), Unsigned32()).setUnits('-0.25 dBm/Hz').setMaxAccess("readcreate")
if mibBuilder.loadTexts: vdslLineSCMConfProfileBandTransmitPSDLevel.setStatus('current')
vdslLineSCMConfProfileBandRowStatus = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 228, 1, 1, 1, 1, 7), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: vdslLineSCMConfProfileBandRowStatus.setStatus('current')
vdslLineSCMPhysBandTable = MibTable((1, 3, 6, 1, 2, 1, 10, 228, 1, 1, 2), )
if mibBuilder.loadTexts: vdslLineSCMPhysBandTable.setStatus('current')
vdslLineSCMPhysBandEntry = MibTableRow((1, 3, 6, 1, 2, 1, 10, 228, 1, 1, 2, 1), ).setIndexNames((0, "IF-MIB", "ifIndex"), (0, "VDSL-LINE-EXT-SCM-MIB", "vdslLineSCMPhysBandId"))
if mibBuilder.loadTexts: vdslLineSCMPhysBandEntry.setStatus('current')
vdslLineSCMPhysBandId = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 228, 1, 1, 2, 1, 1), VdslSCMBandId())
if mibBuilder.loadTexts: vdslLineSCMPhysBandId.setStatus('current')
vdslLineSCMPhysBandInUse = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 228, 1, 1, 2, 1, 2), TruthValue()).setMaxAccess("readonly")
if mibBuilder.loadTexts: vdslLineSCMPhysBandInUse.setStatus('current')
vdslLineSCMPhysBandCurrCenterFrequency = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 228, 1, 1, 2, 1, 3), Unsigned32()).setUnits('Hz').setMaxAccess("readonly")
if mibBuilder.loadTexts: vdslLineSCMPhysBandCurrCenterFrequency.setStatus('current')
vdslLineSCMPhysBandCurrSymbolRate = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 228, 1, 1, 2, 1, 4), Unsigned32()).setUnits('baud').setMaxAccess("readonly")
if mibBuilder.loadTexts: vdslLineSCMPhysBandCurrSymbolRate.setStatus('current')
vdslLineSCMPhysBandCurrConstellationSize = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 228, 1, 1, 2, 1, 5), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(0, 16))).setUnits('log2').setMaxAccess("readonly")
if mibBuilder.loadTexts: vdslLineSCMPhysBandCurrConstellationSize.setStatus('current')
vdslLineSCMPhysBandCurrPSDLevel = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 228, 1, 1, 2, 1, 6), Unsigned32()).setUnits('- 0.25 dBm/Hz').setMaxAccess("readonly")
if mibBuilder.loadTexts: vdslLineSCMPhysBandCurrPSDLevel.setStatus('current')
vdslLineSCMPhysBandCurrSnrMgn = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 228, 1, 1, 2, 1, 7), Integer32()).setUnits('0.25 dB').setMaxAccess("readonly")
if mibBuilder.loadTexts: vdslLineSCMPhysBandCurrSnrMgn.setStatus('current')
vdslLineSCMPhysBandCurrAtn = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 228, 1, 1, 2, 1, 8), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(0, 255))).setUnits('0.25 dB').setMaxAccess("readonly")
if mibBuilder.loadTexts: vdslLineSCMPhysBandCurrAtn.setStatus('current')
vdslLineExtSCMConformance = MibIdentifier((1, 3, 6, 1, 2, 1, 10, 228, 1, 2))
vdslLineExtSCMGroups = MibIdentifier((1, 3, 6, 1, 2, 1, 10, 228, 1, 2, 1))
vdslLineExtSCMCompliances = MibIdentifier((1, 3, 6, 1, 2, 1, 10, 228, 1, 2, 2))
vdslLineExtSCMMibCompliance = ModuleCompliance((1, 3, 6, 1, 2, 1, 10, 228, 1, 2, 2, 1)).setObjects(("VDSL-LINE-EXT-SCM-MIB", "vdslLineExtSCMGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    vdslLineExtSCMMibCompliance = vdslLineExtSCMMibCompliance.setStatus('current')
vdslLineExtSCMGroup = ObjectGroup((1, 3, 6, 1, 2, 1, 10, 228, 1, 2, 1, 1)).setObjects(("VDSL-LINE-EXT-SCM-MIB", "vdslLineSCMConfProfileBandInUse"), ("VDSL-LINE-EXT-SCM-MIB", "vdslLineSCMConfProfileBandTransmitPSDLevel"), ("VDSL-LINE-EXT-SCM-MIB", "vdslLineSCMConfProfileBandSymbolRate"), ("VDSL-LINE-EXT-SCM-MIB", "vdslLineSCMConfProfileBandConstellationSize"), ("VDSL-LINE-EXT-SCM-MIB", "vdslLineSCMConfProfileBandCenterFrequency"), ("VDSL-LINE-EXT-SCM-MIB", "vdslLineSCMConfProfileBandRowStatus"), ("VDSL-LINE-EXT-SCM-MIB", "vdslLineSCMPhysBandInUse"), ("VDSL-LINE-EXT-SCM-MIB", "vdslLineSCMPhysBandCurrPSDLevel"), ("VDSL-LINE-EXT-SCM-MIB", "vdslLineSCMPhysBandCurrSymbolRate"), ("VDSL-LINE-EXT-SCM-MIB", "vdslLineSCMPhysBandCurrConstellationSize"), ("VDSL-LINE-EXT-SCM-MIB", "vdslLineSCMPhysBandCurrCenterFrequency"), ("VDSL-LINE-EXT-SCM-MIB", "vdslLineSCMPhysBandCurrSnrMgn"), ("VDSL-LINE-EXT-SCM-MIB", "vdslLineSCMPhysBandCurrAtn"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    vdslLineExtSCMGroup = vdslLineExtSCMGroup.setStatus('current')
mibBuilder.exportSymbols("VDSL-LINE-EXT-SCM-MIB", vdslLineExtSCMMibCompliance=vdslLineExtSCMMibCompliance, vdslLineExtSCMMib=vdslLineExtSCMMib, vdslLineSCMPhysBandCurrSymbolRate=vdslLineSCMPhysBandCurrSymbolRate, vdslLineSCMConfProfileBandTable=vdslLineSCMConfProfileBandTable, vdslLineSCMPhysBandCurrCenterFrequency=vdslLineSCMPhysBandCurrCenterFrequency, vdslLineSCMConfProfileBandEntry=vdslLineSCMConfProfileBandEntry, vdslLineExtSCMMibObjects=vdslLineExtSCMMibObjects, vdslLineSCMPhysBandCurrAtn=vdslLineSCMPhysBandCurrAtn, vdslLineExtSCMCompliances=vdslLineExtSCMCompliances, vdslLineSCMPhysBandId=vdslLineSCMPhysBandId, vdslLineSCMConfProfileBandTransmitPSDLevel=vdslLineSCMConfProfileBandTransmitPSDLevel, vdslLineSCMConfProfileBandConstellationSize=vdslLineSCMConfProfileBandConstellationSize, vdslLineExtSCMConformance=vdslLineExtSCMConformance, vdslLineSCMConfProfileBandSymbolRate=vdslLineSCMConfProfileBandSymbolRate, vdslLineSCMPhysBandTable=vdslLineSCMPhysBandTable, VdslSCMBandId=VdslSCMBandId, vdslLineExtSCMGroup=vdslLineExtSCMGroup, vdslLineSCMPhysBandEntry=vdslLineSCMPhysBandEntry, vdslLineExtSCMGroups=vdslLineExtSCMGroups, vdslLineSCMPhysBandCurrConstellationSize=vdslLineSCMPhysBandCurrConstellationSize, vdslExtSCMMIB=vdslExtSCMMIB, PYSNMP_MODULE_ID=vdslExtSCMMIB, vdslLineSCMConfProfileBandRowStatus=vdslLineSCMConfProfileBandRowStatus, vdslLineSCMConfProfileBandCenterFrequency=vdslLineSCMConfProfileBandCenterFrequency, vdslLineSCMConfProfileBandId=vdslLineSCMConfProfileBandId, vdslLineSCMPhysBandInUse=vdslLineSCMPhysBandInUse, vdslLineSCMPhysBandCurrPSDLevel=vdslLineSCMPhysBandCurrPSDLevel, vdslLineSCMPhysBandCurrSnrMgn=vdslLineSCMPhysBandCurrSnrMgn, vdslLineSCMConfProfileBandInUse=vdslLineSCMConfProfileBandInUse)
