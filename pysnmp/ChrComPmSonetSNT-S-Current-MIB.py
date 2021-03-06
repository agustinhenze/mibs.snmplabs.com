#
# PySNMP MIB module ChrComPmSonetSNT-S-Current-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/ChrComPmSonetSNT-S-Current-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 18:20:46 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsUnion, ConstraintsIntersection, SingleValueConstraint, ValueRangeConstraint, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "ConstraintsIntersection", "SingleValueConstraint", "ValueRangeConstraint", "ValueSizeConstraint")
chrComIfifIndex, = mibBuilder.importSymbols("ChrComIfifTable-MIB", "chrComIfifIndex")
TruthValue, = mibBuilder.importSymbols("ChrTyp-MIB", "TruthValue")
chrComPmSonet, = mibBuilder.importSymbols("Chromatis-MIB", "chrComPmSonet")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
Counter64, Bits, ModuleIdentity, ObjectIdentity, IpAddress, iso, Counter32, Integer32, NotificationType, TimeTicks, Gauge32, Unsigned32, MibScalar, MibTable, MibTableRow, MibTableColumn, MibIdentifier = mibBuilder.importSymbols("SNMPv2-SMI", "Counter64", "Bits", "ModuleIdentity", "ObjectIdentity", "IpAddress", "iso", "Counter32", "Integer32", "NotificationType", "TimeTicks", "Gauge32", "Unsigned32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "MibIdentifier")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
chrComPmSonetSNT_S_CurrentTable = MibTable((1, 3, 6, 1, 4, 1, 3695, 1, 10, 2, 1), ).setLabel("chrComPmSonetSNT-S-CurrentTable")
if mibBuilder.loadTexts: chrComPmSonetSNT_S_CurrentTable.setStatus('current')
chrComPmSonetSNT_S_CurrentEntry = MibTableRow((1, 3, 6, 1, 4, 1, 3695, 1, 10, 2, 1, 1), ).setLabel("chrComPmSonetSNT-S-CurrentEntry").setIndexNames((0, "ChrComIfifTable-MIB", "chrComIfifIndex"))
if mibBuilder.loadTexts: chrComPmSonetSNT_S_CurrentEntry.setStatus('current')
chrComPmSonetSuspectedInterval = MibTableColumn((1, 3, 6, 1, 4, 1, 3695, 1, 10, 2, 1, 1, 1), TruthValue()).setMaxAccess("readonly")
if mibBuilder.loadTexts: chrComPmSonetSuspectedInterval.setStatus('current')
chrComPmSonetElapsedTime = MibTableColumn((1, 3, 6, 1, 4, 1, 3695, 1, 10, 2, 1, 1, 2), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(0, 4294967295))).setMaxAccess("readonly")
if mibBuilder.loadTexts: chrComPmSonetElapsedTime.setStatus('current')
chrComPmSonetSuppressedIntrvls = MibTableColumn((1, 3, 6, 1, 4, 1, 3695, 1, 10, 2, 1, 1, 3), Gauge32().subtype(subtypeSpec=ValueRangeConstraint(0, 4294967295))).setMaxAccess("readonly")
if mibBuilder.loadTexts: chrComPmSonetSuppressedIntrvls.setStatus('current')
chrComPmSonetStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 3695, 1, 10, 2, 1, 1, 4), Gauge32().subtype(subtypeSpec=ValueRangeConstraint(0, 4294967295))).setMaxAccess("readonly")
if mibBuilder.loadTexts: chrComPmSonetStatus.setStatus('current')
chrComPmSonetES = MibTableColumn((1, 3, 6, 1, 4, 1, 3695, 1, 10, 2, 1, 1, 5), Gauge32().subtype(subtypeSpec=ValueRangeConstraint(0, 4294967295))).setMaxAccess("readonly")
if mibBuilder.loadTexts: chrComPmSonetES.setStatus('current')
chrComPmSonetSES = MibTableColumn((1, 3, 6, 1, 4, 1, 3695, 1, 10, 2, 1, 1, 6), Gauge32().subtype(subtypeSpec=ValueRangeConstraint(0, 4294967295))).setMaxAccess("readonly")
if mibBuilder.loadTexts: chrComPmSonetSES.setStatus('current')
chrComPmSonetSEFS = MibTableColumn((1, 3, 6, 1, 4, 1, 3695, 1, 10, 2, 1, 1, 7), Gauge32().subtype(subtypeSpec=ValueRangeConstraint(0, 4294967295))).setMaxAccess("readonly")
if mibBuilder.loadTexts: chrComPmSonetSEFS.setStatus('current')
chrComPmSonetCV = MibTableColumn((1, 3, 6, 1, 4, 1, 3695, 1, 10, 2, 1, 1, 8), Gauge32().subtype(subtypeSpec=ValueRangeConstraint(0, 4294967295))).setMaxAccess("readonly")
if mibBuilder.loadTexts: chrComPmSonetCV.setStatus('current')
chrComPmSonetThresholdProfIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 3695, 1, 10, 2, 1, 1, 9), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(0, 4294967295))).setMaxAccess("readonly")
if mibBuilder.loadTexts: chrComPmSonetThresholdProfIndex.setStatus('current')
chrComPmSonetResetPmCountersAction = MibTableColumn((1, 3, 6, 1, 4, 1, 3695, 1, 10, 2, 1, 1, 10), TruthValue()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: chrComPmSonetResetPmCountersAction.setStatus('current')
mibBuilder.exportSymbols("ChrComPmSonetSNT-S-Current-MIB", chrComPmSonetElapsedTime=chrComPmSonetElapsedTime, chrComPmSonetThresholdProfIndex=chrComPmSonetThresholdProfIndex, chrComPmSonetSNT_S_CurrentEntry=chrComPmSonetSNT_S_CurrentEntry, chrComPmSonetResetPmCountersAction=chrComPmSonetResetPmCountersAction, chrComPmSonetCV=chrComPmSonetCV, chrComPmSonetStatus=chrComPmSonetStatus, chrComPmSonetSES=chrComPmSonetSES, chrComPmSonetSuppressedIntrvls=chrComPmSonetSuppressedIntrvls, chrComPmSonetSNT_S_CurrentTable=chrComPmSonetSNT_S_CurrentTable, chrComPmSonetSEFS=chrComPmSonetSEFS, chrComPmSonetSuspectedInterval=chrComPmSonetSuspectedInterval, chrComPmSonetES=chrComPmSonetES)
