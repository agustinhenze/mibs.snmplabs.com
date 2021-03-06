#
# PySNMP MIB module CADANT-LICENSE-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/CADANT-LICENSE-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 17:28:28 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
OctetString, ObjectIdentifier, Integer = mibBuilder.importSymbols("ASN1", "OctetString", "ObjectIdentifier", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, ConstraintsIntersection, ValueSizeConstraint, ConstraintsUnion, SingleValueConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "ConstraintsIntersection", "ValueSizeConstraint", "ConstraintsUnion", "SingleValueConstraint")
cadLicense, = mibBuilder.importSymbols("CADANT-PRODUCTS-MIB", "cadLicense")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
MibIdentifier, Counter32, MibScalar, MibTable, MibTableRow, MibTableColumn, iso, Bits, ModuleIdentity, Counter64, Gauge32, Integer32, ObjectIdentity, Unsigned32, NotificationType, IpAddress, TimeTicks = mibBuilder.importSymbols("SNMPv2-SMI", "MibIdentifier", "Counter32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "iso", "Bits", "ModuleIdentity", "Counter64", "Gauge32", "Integer32", "ObjectIdentity", "Unsigned32", "NotificationType", "IpAddress", "TimeTicks")
DisplayString, TextualConvention, RowStatus, TruthValue = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention", "RowStatus", "TruthValue")
cadLicenseMib = ModuleIdentity((1, 3, 6, 1, 4, 1, 4998, 1, 1, 135, 1))
cadLicenseMib.setRevisions(('2015-06-17 00:00', '2015-06-09 00:00', '2014-08-20 00:00', '2014-08-14 00:00', '2014-07-17 00:00', '2014-07-10 00:00', '2014-06-25 00:00',))
if mibBuilder.loadTexts: cadLicenseMib.setLastUpdated('201506170000Z')
if mibBuilder.loadTexts: cadLicenseMib.setOrganization('ARRIS Group, Inc.')
class CadChassisLicenseIndexType(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14))
    namedValues = NamedValues(("reserved", 1), ("videoNarrowcastB", 2), ("videoReplicaNarrowcastB", 3), ("videoBroadcastB", 4), ("videoReplicaBroadcastB", 5), ("videoNarrowcastA", 6), ("videoReplicaNarrowcastA", 7), ("videoBroadcastA", 8), ("videoReplicaBroadcastA", 9), ("docsisUpstream30", 10), ("docsisDownstream30B", 11), ("docsisDownstream30A", 12), ("docsisDownstreamOfdm", 13), ("docsisUpstreamOfdma", 14))

cadChassisLicenseTable = MibTable((1, 3, 6, 1, 4, 1, 4998, 1, 1, 135, 1, 1), )
if mibBuilder.loadTexts: cadChassisLicenseTable.setStatus('current')
cadChassisLicenseEntry = MibTableRow((1, 3, 6, 1, 4, 1, 4998, 1, 1, 135, 1, 1, 1), ).setIndexNames((0, "CADANT-LICENSE-MIB", "cadLicenseIndex"))
if mibBuilder.loadTexts: cadChassisLicenseEntry.setStatus('current')
cadLicenseIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 4998, 1, 1, 135, 1, 1, 1, 1), CadChassisLicenseIndexType())
if mibBuilder.loadTexts: cadLicenseIndex.setStatus('current')
cadLicenseKey = MibTableColumn((1, 3, 6, 1, 4, 1, 4998, 1, 1, 135, 1, 1, 1, 2), OctetString().subtype(subtypeSpec=ValueSizeConstraint(20, 20)).setFixedLength(20)).setMaxAccess("readcreate")
if mibBuilder.loadTexts: cadLicenseKey.setStatus('current')
cadLicenseChannelCount = MibTableColumn((1, 3, 6, 1, 4, 1, 4998, 1, 1, 135, 1, 1, 1, 3), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(1, 500000))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: cadLicenseChannelCount.setStatus('current')
cadLicenseSpareChannelCount = MibTableColumn((1, 3, 6, 1, 4, 1, 4998, 1, 1, 135, 1, 1, 1, 4), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(0, 250000))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: cadLicenseSpareChannelCount.setStatus('current')
cadLicenseRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 4998, 1, 1, 135, 1, 1, 1, 5), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: cadLicenseRowStatus.setStatus('current')
cadChassisLicenseStatusTable = MibTable((1, 3, 6, 1, 4, 1, 4998, 1, 1, 135, 1, 2), )
if mibBuilder.loadTexts: cadChassisLicenseStatusTable.setStatus('current')
cadChassisLicenseStatusEntry = MibTableRow((1, 3, 6, 1, 4, 1, 4998, 1, 1, 135, 1, 2, 1), ).setIndexNames((0, "CADANT-LICENSE-MIB", "cadChassisLicenseStatusType"))
if mibBuilder.loadTexts: cadChassisLicenseStatusEntry.setStatus('current')
cadChassisLicenseStatusType = MibTableColumn((1, 3, 6, 1, 4, 1, 4998, 1, 1, 135, 1, 2, 1, 1), CadChassisLicenseIndexType())
if mibBuilder.loadTexts: cadChassisLicenseStatusType.setStatus('current')
cadChassisLicensesUsed = MibTableColumn((1, 3, 6, 1, 4, 1, 4998, 1, 1, 135, 1, 2, 1, 2), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cadChassisLicensesUsed.setStatus('current')
cadChassisLicensesRequested = MibTableColumn((1, 3, 6, 1, 4, 1, 4998, 1, 1, 135, 1, 2, 1, 3), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cadChassisLicensesRequested.setStatus('current')
cadChassisLicensesApplied = MibTableColumn((1, 3, 6, 1, 4, 1, 4998, 1, 1, 135, 1, 2, 1, 4), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cadChassisLicensesApplied.setStatus('current')
cadChassisLicensesValid = MibTableColumn((1, 3, 6, 1, 4, 1, 4998, 1, 1, 135, 1, 2, 1, 5), TruthValue()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cadChassisLicensesValid.setStatus('current')
cerCardDataLicenseStatusTable = MibTable((1, 3, 6, 1, 4, 1, 4998, 1, 1, 135, 1, 3), )
if mibBuilder.loadTexts: cerCardDataLicenseStatusTable.setStatus('current')
cerCardDataLicenseStatusEntry = MibTableRow((1, 3, 6, 1, 4, 1, 4998, 1, 1, 135, 1, 3, 1), ).setIndexNames((0, "CADANT-LICENSE-MIB", "cerCardDataLicenseSlot"), (0, "CADANT-LICENSE-MIB", "cerCardDataLicenseType"))
if mibBuilder.loadTexts: cerCardDataLicenseStatusEntry.setStatus('current')
cerCardDataLicenseSlot = MibTableColumn((1, 3, 6, 1, 4, 1, 4998, 1, 1, 135, 1, 3, 1, 1), Unsigned32().subtype(subtypeSpec=ConstraintsUnion(ValueRangeConstraint(1, 6), ValueRangeConstraint(9, 14), )))
if mibBuilder.loadTexts: cerCardDataLicenseSlot.setStatus('current')
cerCardDataLicenseType = MibTableColumn((1, 3, 6, 1, 4, 1, 4998, 1, 1, 135, 1, 3, 1, 2), CadChassisLicenseIndexType())
if mibBuilder.loadTexts: cerCardDataLicenseType.setStatus('current')
cerCardDataLicensesUsed = MibTableColumn((1, 3, 6, 1, 4, 1, 4998, 1, 1, 135, 1, 3, 1, 3), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cerCardDataLicensesUsed.setStatus('current')
cerCardDataLicensesRequested = MibTableColumn((1, 3, 6, 1, 4, 1, 4998, 1, 1, 135, 1, 3, 1, 4), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cerCardDataLicensesRequested.setStatus('current')
mibBuilder.exportSymbols("CADANT-LICENSE-MIB", cadLicenseIndex=cadLicenseIndex, cadChassisLicenseStatusEntry=cadChassisLicenseStatusEntry, cadChassisLicensesUsed=cadChassisLicensesUsed, cadChassisLicensesApplied=cadChassisLicensesApplied, cadLicenseChannelCount=cadLicenseChannelCount, cadChassisLicensesValid=cadChassisLicensesValid, CadChassisLicenseIndexType=CadChassisLicenseIndexType, cadLicenseKey=cadLicenseKey, PYSNMP_MODULE_ID=cadLicenseMib, cadLicenseRowStatus=cadLicenseRowStatus, cadLicenseSpareChannelCount=cadLicenseSpareChannelCount, cerCardDataLicensesUsed=cerCardDataLicensesUsed, cerCardDataLicensesRequested=cerCardDataLicensesRequested, cadChassisLicenseTable=cadChassisLicenseTable, cadChassisLicenseStatusType=cadChassisLicenseStatusType, cerCardDataLicenseStatusEntry=cerCardDataLicenseStatusEntry, cerCardDataLicenseStatusTable=cerCardDataLicenseStatusTable, cadLicenseMib=cadLicenseMib, cadChassisLicenseEntry=cadChassisLicenseEntry, cerCardDataLicenseSlot=cerCardDataLicenseSlot, cerCardDataLicenseType=cerCardDataLicenseType, cadChassisLicensesRequested=cadChassisLicensesRequested, cadChassisLicenseStatusTable=cadChassisLicenseStatusTable)
