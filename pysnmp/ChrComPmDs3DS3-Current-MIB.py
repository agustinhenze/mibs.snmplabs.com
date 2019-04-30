#
# PySNMP MIB module ChrComPmDs3DS3-Current-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/ChrComPmDs3DS3-Current-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 18:19:49 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, ValueSizeConstraint, ConstraintsUnion, ConstraintsIntersection, SingleValueConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "ValueSizeConstraint", "ConstraintsUnion", "ConstraintsIntersection", "SingleValueConstraint")
chrComIfifIndex, = mibBuilder.importSymbols("ChrComIfifTable-MIB", "chrComIfifIndex")
TruthValue, = mibBuilder.importSymbols("ChrTyp-MIB", "TruthValue")
chrComPmDs3, = mibBuilder.importSymbols("Chromatis-MIB", "chrComPmDs3")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
Unsigned32, NotificationType, ObjectIdentity, ModuleIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, iso, Gauge32, Integer32, MibIdentifier, Counter64, Bits, IpAddress, Counter32, TimeTicks = mibBuilder.importSymbols("SNMPv2-SMI", "Unsigned32", "NotificationType", "ObjectIdentity", "ModuleIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "iso", "Gauge32", "Integer32", "MibIdentifier", "Counter64", "Bits", "IpAddress", "Counter32", "TimeTicks")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
chrComPmDs3DS3_CurrentTable = MibTable((1, 3, 6, 1, 4, 1, 3695, 1, 10, 3, 10), ).setLabel("chrComPmDs3DS3-CurrentTable")
if mibBuilder.loadTexts: chrComPmDs3DS3_CurrentTable.setStatus('current')
chrComPmDs3DS3_CurrentEntry = MibTableRow((1, 3, 6, 1, 4, 1, 3695, 1, 10, 3, 10, 1), ).setLabel("chrComPmDs3DS3-CurrentEntry").setIndexNames((0, "ChrComIfifTable-MIB", "chrComIfifIndex"))
if mibBuilder.loadTexts: chrComPmDs3DS3_CurrentEntry.setStatus('current')
chrComPmDs3SuspectedInterval = MibTableColumn((1, 3, 6, 1, 4, 1, 3695, 1, 10, 3, 10, 1, 1), TruthValue()).setMaxAccess("readonly")
if mibBuilder.loadTexts: chrComPmDs3SuspectedInterval.setStatus('current')
chrComPmDs3ElapsedTime = MibTableColumn((1, 3, 6, 1, 4, 1, 3695, 1, 10, 3, 10, 1, 2), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(0, 4294967295))).setMaxAccess("readonly")
if mibBuilder.loadTexts: chrComPmDs3ElapsedTime.setStatus('current')
chrComPmDs3SuppressedIntrvls = MibTableColumn((1, 3, 6, 1, 4, 1, 3695, 1, 10, 3, 10, 1, 3), Gauge32().subtype(subtypeSpec=ValueRangeConstraint(0, 4294967295))).setMaxAccess("readonly")
if mibBuilder.loadTexts: chrComPmDs3SuppressedIntrvls.setStatus('current')
chrComPmDs3LCV = MibTableColumn((1, 3, 6, 1, 4, 1, 3695, 1, 10, 3, 10, 1, 4), Gauge32().subtype(subtypeSpec=ValueRangeConstraint(0, 4294967295))).setMaxAccess("readonly")
if mibBuilder.loadTexts: chrComPmDs3LCV.setStatus('current')
chrComPmDs3LES = MibTableColumn((1, 3, 6, 1, 4, 1, 3695, 1, 10, 3, 10, 1, 5), Gauge32().subtype(subtypeSpec=ValueRangeConstraint(0, 4294967295))).setMaxAccess("readonly")
if mibBuilder.loadTexts: chrComPmDs3LES.setStatus('current')
chrComPmDs3LSES = MibTableColumn((1, 3, 6, 1, 4, 1, 3695, 1, 10, 3, 10, 1, 6), Gauge32().subtype(subtypeSpec=ValueRangeConstraint(0, 4294967295))).setMaxAccess("readonly")
if mibBuilder.loadTexts: chrComPmDs3LSES.setStatus('current')
chrComPmDs3LOSS = MibTableColumn((1, 3, 6, 1, 4, 1, 3695, 1, 10, 3, 10, 1, 7), Gauge32().subtype(subtypeSpec=ValueRangeConstraint(0, 4294967295))).setMaxAccess("readonly")
if mibBuilder.loadTexts: chrComPmDs3LOSS.setStatus('current')
chrComPmDs3PCV = MibTableColumn((1, 3, 6, 1, 4, 1, 3695, 1, 10, 3, 10, 1, 8), Gauge32().subtype(subtypeSpec=ValueRangeConstraint(0, 4294967295))).setMaxAccess("readonly")
if mibBuilder.loadTexts: chrComPmDs3PCV.setStatus('current')
chrComPmDs3CCV = MibTableColumn((1, 3, 6, 1, 4, 1, 3695, 1, 10, 3, 10, 1, 9), Gauge32().subtype(subtypeSpec=ValueRangeConstraint(0, 4294967295))).setMaxAccess("readonly")
if mibBuilder.loadTexts: chrComPmDs3CCV.setStatus('current')
chrComPmDs3PES = MibTableColumn((1, 3, 6, 1, 4, 1, 3695, 1, 10, 3, 10, 1, 10), Gauge32().subtype(subtypeSpec=ValueRangeConstraint(0, 4294967295))).setMaxAccess("readonly")
if mibBuilder.loadTexts: chrComPmDs3PES.setStatus('current')
chrComPmDs3CES = MibTableColumn((1, 3, 6, 1, 4, 1, 3695, 1, 10, 3, 10, 1, 11), Gauge32().subtype(subtypeSpec=ValueRangeConstraint(0, 4294967295))).setMaxAccess("readonly")
if mibBuilder.loadTexts: chrComPmDs3CES.setStatus('current')
chrComPmDs3PSES = MibTableColumn((1, 3, 6, 1, 4, 1, 3695, 1, 10, 3, 10, 1, 12), Gauge32().subtype(subtypeSpec=ValueRangeConstraint(0, 4294967295))).setMaxAccess("readonly")
if mibBuilder.loadTexts: chrComPmDs3PSES.setStatus('current')
chrComPmDs3CSES = MibTableColumn((1, 3, 6, 1, 4, 1, 3695, 1, 10, 3, 10, 1, 13), Gauge32().subtype(subtypeSpec=ValueRangeConstraint(0, 4294967295))).setMaxAccess("readonly")
if mibBuilder.loadTexts: chrComPmDs3CSES.setStatus('current')
chrComPmDs3SAS = MibTableColumn((1, 3, 6, 1, 4, 1, 3695, 1, 10, 3, 10, 1, 14), Gauge32().subtype(subtypeSpec=ValueRangeConstraint(0, 4294967295))).setMaxAccess("readonly")
if mibBuilder.loadTexts: chrComPmDs3SAS.setStatus('current')
chrComPmDs3AISS = MibTableColumn((1, 3, 6, 1, 4, 1, 3695, 1, 10, 3, 10, 1, 15), Gauge32().subtype(subtypeSpec=ValueRangeConstraint(0, 4294967295))).setMaxAccess("readonly")
if mibBuilder.loadTexts: chrComPmDs3AISS.setStatus('current')
chrComPmDs3UASP = MibTableColumn((1, 3, 6, 1, 4, 1, 3695, 1, 10, 3, 10, 1, 16), Gauge32().subtype(subtypeSpec=ValueRangeConstraint(0, 4294967295))).setMaxAccess("readonly")
if mibBuilder.loadTexts: chrComPmDs3UASP.setStatus('current')
chrComPmDs3UASCP = MibTableColumn((1, 3, 6, 1, 4, 1, 3695, 1, 10, 3, 10, 1, 17), Gauge32().subtype(subtypeSpec=ValueRangeConstraint(0, 4294967295))).setMaxAccess("readonly")
if mibBuilder.loadTexts: chrComPmDs3UASCP.setStatus('current')
chrComPmDs3PSC = MibTableColumn((1, 3, 6, 1, 4, 1, 3695, 1, 10, 3, 10, 1, 18), Gauge32().subtype(subtypeSpec=ValueRangeConstraint(0, 4294967295))).setMaxAccess("readonly")
if mibBuilder.loadTexts: chrComPmDs3PSC.setStatus('current')
chrComPmDs3ESPLCP = MibTableColumn((1, 3, 6, 1, 4, 1, 3695, 1, 10, 3, 10, 1, 19), Gauge32().subtype(subtypeSpec=ValueRangeConstraint(0, 4294967295))).setMaxAccess("readonly")
if mibBuilder.loadTexts: chrComPmDs3ESPLCP.setStatus('current')
chrComPmDs3ThresholdProfIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 3695, 1, 10, 3, 10, 1, 20), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(0, 4294967295))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: chrComPmDs3ThresholdProfIndex.setStatus('current')
chrComPmDs3ResetPmCountersAction = MibTableColumn((1, 3, 6, 1, 4, 1, 3695, 1, 10, 3, 10, 1, 21), TruthValue()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: chrComPmDs3ResetPmCountersAction.setStatus('current')
mibBuilder.exportSymbols("ChrComPmDs3DS3-Current-MIB", chrComPmDs3ESPLCP=chrComPmDs3ESPLCP, chrComPmDs3CCV=chrComPmDs3CCV, chrComPmDs3DS3_CurrentEntry=chrComPmDs3DS3_CurrentEntry, chrComPmDs3SuppressedIntrvls=chrComPmDs3SuppressedIntrvls, chrComPmDs3SAS=chrComPmDs3SAS, chrComPmDs3UASP=chrComPmDs3UASP, chrComPmDs3ThresholdProfIndex=chrComPmDs3ThresholdProfIndex, chrComPmDs3PES=chrComPmDs3PES, chrComPmDs3LCV=chrComPmDs3LCV, chrComPmDs3LSES=chrComPmDs3LSES, chrComPmDs3SuspectedInterval=chrComPmDs3SuspectedInterval, chrComPmDs3PSES=chrComPmDs3PSES, chrComPmDs3PCV=chrComPmDs3PCV, chrComPmDs3CES=chrComPmDs3CES, chrComPmDs3AISS=chrComPmDs3AISS, chrComPmDs3LES=chrComPmDs3LES, chrComPmDs3DS3_CurrentTable=chrComPmDs3DS3_CurrentTable, chrComPmDs3ElapsedTime=chrComPmDs3ElapsedTime, chrComPmDs3CSES=chrComPmDs3CSES, chrComPmDs3UASCP=chrComPmDs3UASCP, chrComPmDs3LOSS=chrComPmDs3LOSS, chrComPmDs3ResetPmCountersAction=chrComPmDs3ResetPmCountersAction, chrComPmDs3PSC=chrComPmDs3PSC)