#
# PySNMP MIB module PMCAPS-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/PMCAPS-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 20:32:09 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
Integer, OctetString, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "Integer", "OctetString", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ConstraintsUnion, ValueSizeConstraint, SingleValueConstraint, ValueRangeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ConstraintsUnion", "ValueSizeConstraint", "SingleValueConstraint", "ValueRangeConstraint")
rmon, = mibBuilder.importSymbols("RMON-MIB", "rmon")
protocolDirLocalIndex, protocolDirectoryGroup = mibBuilder.importSymbols("RMON2-MIB", "protocolDirLocalIndex", "protocolDirectoryGroup")
SnmpAdminString, = mibBuilder.importSymbols("SNMP-FRAMEWORK-MIB", "SnmpAdminString")
ModuleCompliance, ObjectGroup, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "ObjectGroup", "NotificationGroup")
MibScalar, MibTable, MibTableRow, MibTableColumn, Bits, Counter64, TimeTicks, ModuleIdentity, Unsigned32, Gauge32, Integer32, NotificationType, IpAddress, MibIdentifier, iso, Counter32, ObjectIdentity = mibBuilder.importSymbols("SNMPv2-SMI", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Bits", "Counter64", "TimeTicks", "ModuleIdentity", "Unsigned32", "Gauge32", "Integer32", "NotificationType", "IpAddress", "MibIdentifier", "iso", "Counter32", "ObjectIdentity")
RowPointer, TruthValue, DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "RowPointer", "TruthValue", "DisplayString", "TextualConvention")
pmCapsMIB = ModuleIdentity((1, 3, 6, 1, 2, 1, 16, 25))
pmCapsMIB.setRevisions(('2000-07-14 00:00',))
if mibBuilder.loadTexts: pmCapsMIB.setLastUpdated('200007140000Z')
if mibBuilder.loadTexts: pmCapsMIB.setOrganization('IETF RMONMIB WG')
pmCapsMIBObjects = MibIdentifier((1, 3, 6, 1, 2, 1, 16, 25, 1))
pmCaps = MibIdentifier((1, 3, 6, 1, 2, 1, 16, 25, 1, 1))
pmMetrics = MibIdentifier((1, 3, 6, 1, 2, 1, 16, 25, 1, 2))
pmMetricTable = MibTable((1, 3, 6, 1, 2, 1, 16, 25, 1, 1, 1), )
if mibBuilder.loadTexts: pmMetricTable.setStatus('current')
pmMetricEntry = MibTableRow((1, 3, 6, 1, 2, 1, 16, 25, 1, 1, 1, 1), ).setIndexNames((0, "PMCAPS-MIB", "pmMetricID"))
if mibBuilder.loadTexts: pmMetricEntry.setStatus('current')
pmMetricID = MibTableColumn((1, 3, 6, 1, 2, 1, 16, 25, 1, 1, 1, 1, 1), ObjectIdentifier())
if mibBuilder.loadTexts: pmMetricID.setStatus('current')
pmMetricType = MibTableColumn((1, 3, 6, 1, 2, 1, 16, 25, 1, 1, 1, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))).clone(namedValues=NamedValues(("other", 1), ("connectMetric", 2), ("delayMetric", 3), ("lossMetric", 4)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: pmMetricType.setStatus('current')
pmMetricDirType = MibTableColumn((1, 3, 6, 1, 2, 1, 16, 25, 1, 1, 1, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("oneWay", 1), ("twoWay", 2), ("multiWay", 3)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: pmMetricDirType.setStatus('current')
pmMetricName = MibTableColumn((1, 3, 6, 1, 2, 1, 16, 25, 1, 1, 1, 1, 4), SnmpAdminString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: pmMetricName.setStatus('current')
pmMetricReference = MibTableColumn((1, 3, 6, 1, 2, 1, 16, 25, 1, 1, 1, 1, 5), SnmpAdminString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: pmMetricReference.setStatus('current')
pmStudyClassTable = MibTable((1, 3, 6, 1, 2, 1, 16, 25, 1, 1, 2), )
if mibBuilder.loadTexts: pmStudyClassTable.setStatus('current')
pmStudyClassEntry = MibTableRow((1, 3, 6, 1, 2, 1, 16, 25, 1, 1, 2, 1), ).setIndexNames((0, "PMCAPS-MIB", "pmStudyClassID"))
if mibBuilder.loadTexts: pmStudyClassEntry.setStatus('current')
pmStudyClassID = MibTableColumn((1, 3, 6, 1, 2, 1, 16, 25, 1, 1, 2, 1, 1), ObjectIdentifier())
if mibBuilder.loadTexts: pmStudyClassID.setStatus('current')
pmStudyClassMeasLoc = MibTableColumn((1, 3, 6, 1, 2, 1, 16, 25, 1, 1, 2, 1, 2), Bits().clone(namedValues=NamedValues(("pmClient", 0), ("pmNetwork", 1), ("pmServer", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: pmStudyClassMeasLoc.setStatus('current')
pmStudyClassMeasType = MibTableColumn((1, 3, 6, 1, 2, 1, 16, 25, 1, 1, 2, 1, 3), Bits().clone(namedValues=NamedValues(("pmPassive", 0), ("pmActive", 1), ("pmBuiltin", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: pmStudyClassMeasType.setStatus('current')
pmStudyClassCollectPts = MibTableColumn((1, 3, 6, 1, 2, 1, 16, 25, 1, 1, 2, 1, 4), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 2147483647))).setMaxAccess("readonly")
if mibBuilder.loadTexts: pmStudyClassCollectPts.setStatus('current')
pmStudyClassCollectCaps = MibTableColumn((1, 3, 6, 1, 2, 1, 16, 25, 1, 1, 2, 1, 5), Bits().clone(namedValues=NamedValues(("pmCollectTrans", 0), ("pmCollectApp", 1), ("pmCollectFlow", 2), ("pmCollectNonNet", 3)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: pmStudyClassCollectCaps.setStatus('current')
pmStudyClassOutputCaps = MibTableColumn((1, 3, 6, 1, 2, 1, 16, 25, 1, 1, 2, 1, 6), Bits().clone(namedValues=NamedValues(("pmOutputOther", 0), ("pmOutputApmDist", 1), ("pmOutputApmStat", 2), ("pmOutputApmHist", 3), ("pmOutputApmFlow", 4), ("pmOutputApmExcept", 5), ("pmOutputApmProp", 6), ("pmOutputTpmDist", 7), ("pmOutputTpmStat", 8), ("pmOutputTpmHist", 9), ("pmOutputTpmExcept", 10), ("pmOutputTpmProp", 11)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: pmStudyClassOutputCaps.setStatus('current')
pmStudyClassCtlTablePtr = MibTableColumn((1, 3, 6, 1, 2, 1, 16, 25, 1, 1, 2, 1, 7), RowPointer()).setMaxAccess("readonly")
if mibBuilder.loadTexts: pmStudyClassCtlTablePtr.setStatus('current')
pmStudyMetricTable = MibTable((1, 3, 6, 1, 2, 1, 16, 25, 1, 1, 3), )
if mibBuilder.loadTexts: pmStudyMetricTable.setStatus('current')
pmStudyMetricEntry = MibTableRow((1, 3, 6, 1, 2, 1, 16, 25, 1, 1, 3, 1), ).setIndexNames((0, "PMCAPS-MIB", "pmStudyClassID"))
if mibBuilder.loadTexts: pmStudyMetricEntry.setStatus('current')
pmStudyMetricID = MibTableColumn((1, 3, 6, 1, 2, 1, 16, 25, 1, 1, 3, 1, 1), ObjectIdentifier()).setMaxAccess("readonly")
if mibBuilder.loadTexts: pmStudyMetricID.setStatus('current')
pmStudyProtocolTable = MibTable((1, 3, 6, 1, 2, 1, 16, 25, 1, 1, 4), )
if mibBuilder.loadTexts: pmStudyProtocolTable.setStatus('current')
pmStudyProtocolEntry = MibTableRow((1, 3, 6, 1, 2, 1, 16, 25, 1, 1, 4, 1), ).setIndexNames((0, "PMCAPS-MIB", "pmStudyClassID"), (0, "RMON2-MIB", "protocolDirLocalIndex"))
if mibBuilder.loadTexts: pmStudyProtocolEntry.setStatus('current')
pmStudyProtocolIsSubtree = MibTableColumn((1, 3, 6, 1, 2, 1, 16, 25, 1, 1, 4, 1, 1), TruthValue()).setMaxAccess("readonly")
if mibBuilder.loadTexts: pmStudyProtocolIsSubtree.setStatus('current')
pmAppAvailMetric = ObjectIdentity((1, 3, 6, 1, 2, 1, 16, 25, 1, 2, 1))
if mibBuilder.loadTexts: pmAppAvailMetric.setStatus('current')
pmAppTransRespMetric = ObjectIdentity((1, 3, 6, 1, 2, 1, 16, 25, 1, 2, 2))
if mibBuilder.loadTexts: pmAppTransRespMetric.setStatus('current')
pmAppTputRespMetric = ObjectIdentity((1, 3, 6, 1, 2, 1, 16, 25, 1, 2, 3))
if mibBuilder.loadTexts: pmAppTputRespMetric.setStatus('current')
pmAppStreamRespMetric = ObjectIdentity((1, 3, 6, 1, 2, 1, 16, 25, 1, 2, 4))
if mibBuilder.loadTexts: pmAppStreamRespMetric.setStatus('current')
pmCapsNotifications = MibIdentifier((1, 3, 6, 1, 2, 1, 16, 25, 2))
pmCapsConformance = MibIdentifier((1, 3, 6, 1, 2, 1, 16, 25, 3))
pmCapsCompliances = MibIdentifier((1, 3, 6, 1, 2, 1, 16, 25, 3, 1))
pmCapsGroups = MibIdentifier((1, 3, 6, 1, 2, 1, 16, 25, 3, 2))
pmCapsCompliance = ModuleCompliance((1, 3, 6, 1, 2, 1, 16, 25, 3, 1, 1)).setObjects(("PMCAPS-MIB", "protocolDirectoryGroup"), ("PMCAPS-MIB", "pmCapsGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    pmCapsCompliance = pmCapsCompliance.setStatus('current')
pmCapsGroup = ObjectGroup((1, 3, 6, 1, 2, 1, 16, 25, 3, 2, 1)).setObjects(("PMCAPS-MIB", "pmMetricType"), ("PMCAPS-MIB", "pmMetricDirType"), ("PMCAPS-MIB", "pmMetricName"), ("PMCAPS-MIB", "pmMetricReference"), ("PMCAPS-MIB", "pmStudyClassMeasLoc"), ("PMCAPS-MIB", "pmStudyClassMeasType"), ("PMCAPS-MIB", "pmStudyClassCollectPts"), ("PMCAPS-MIB", "pmStudyClassCollectCaps"), ("PMCAPS-MIB", "pmStudyClassOutputCaps"), ("PMCAPS-MIB", "pmStudyClassCtlTablePtr"), ("PMCAPS-MIB", "pmStudyMetricID"), ("PMCAPS-MIB", "pmStudyProtocolIsSubtree"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    pmCapsGroup = pmCapsGroup.setStatus('current')
mibBuilder.exportSymbols("PMCAPS-MIB", pmStudyClassTable=pmStudyClassTable, pmStudyClassMeasType=pmStudyClassMeasType, pmStudyClassCollectPts=pmStudyClassCollectPts, pmAppTputRespMetric=pmAppTputRespMetric, pmStudyMetricEntry=pmStudyMetricEntry, pmCapsNotifications=pmCapsNotifications, pmMetricEntry=pmMetricEntry, pmStudyClassEntry=pmStudyClassEntry, pmMetricName=pmMetricName, pmStudyClassMeasLoc=pmStudyClassMeasLoc, pmCapsCompliance=pmCapsCompliance, pmCapsGroup=pmCapsGroup, pmAppStreamRespMetric=pmAppStreamRespMetric, pmStudyClassCollectCaps=pmStudyClassCollectCaps, pmMetricTable=pmMetricTable, pmStudyClassCtlTablePtr=pmStudyClassCtlTablePtr, pmCapsCompliances=pmCapsCompliances, pmCapsMIB=pmCapsMIB, pmCapsGroups=pmCapsGroups, pmCapsMIBObjects=pmCapsMIBObjects, pmStudyProtocolTable=pmStudyProtocolTable, PYSNMP_MODULE_ID=pmCapsMIB, pmAppTransRespMetric=pmAppTransRespMetric, pmStudyMetricID=pmStudyMetricID, pmCapsConformance=pmCapsConformance, pmStudyMetricTable=pmStudyMetricTable, pmStudyClassID=pmStudyClassID, pmStudyProtocolIsSubtree=pmStudyProtocolIsSubtree, pmCaps=pmCaps, pmMetricID=pmMetricID, pmMetricDirType=pmMetricDirType, pmStudyClassOutputCaps=pmStudyClassOutputCaps, pmAppAvailMetric=pmAppAvailMetric, pmMetricType=pmMetricType, pmMetricReference=pmMetricReference, pmStudyProtocolEntry=pmStudyProtocolEntry, pmMetrics=pmMetrics)
