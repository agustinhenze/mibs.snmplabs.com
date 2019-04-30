#
# PySNMP MIB module ICF-VG-RPTR (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/ICF-VG-RPTR
# Produced by pysmi-0.3.4 at Mon Apr 29 19:23:21 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
OctetString, ObjectIdentifier, Integer = mibBuilder.importSymbols("ASN1", "OctetString", "ObjectIdentifier", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
SingleValueConstraint, ConstraintsUnion, ValueRangeConstraint, ConstraintsIntersection, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "SingleValueConstraint", "ConstraintsUnion", "ValueRangeConstraint", "ConstraintsIntersection", "ValueSizeConstraint")
icfVgRepeater, hpicfObjectModules = mibBuilder.importSymbols("HP-ICF-OID", "icfVgRepeater", "hpicfObjectModules")
ModuleCompliance, ObjectGroup, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "ObjectGroup", "NotificationGroup")
iso, MibScalar, MibTable, MibTableRow, MibTableColumn, ModuleIdentity, Counter32, NotificationType, MibIdentifier, ObjectIdentity, Bits, TimeTicks, Integer32, Counter64, Unsigned32, Gauge32, IpAddress = mibBuilder.importSymbols("SNMPv2-SMI", "iso", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "ModuleIdentity", "Counter32", "NotificationType", "MibIdentifier", "ObjectIdentity", "Bits", "TimeTicks", "Integer32", "Counter64", "Unsigned32", "Gauge32", "IpAddress")
TimeStamp, MacAddress, DisplayString, TextualConvention, TruthValue = mibBuilder.importSymbols("SNMPv2-TC", "TimeStamp", "MacAddress", "DisplayString", "TextualConvention", "TruthValue")
icfVgRepeaterMib = ModuleIdentity((1, 3, 6, 1, 4, 1, 11, 2, 14, 10, 2, 10))
icfVgRepeaterMib.setRevisions(('2000-11-03 22:25', '1997-03-06 03:47', '1996-09-10 02:03', '1996-01-25 03:56', '1995-01-18 00:00',))
if mibBuilder.loadTexts: icfVgRepeaterMib.setLastUpdated('200011032225Z')
if mibBuilder.loadTexts: icfVgRepeaterMib.setOrganization('Hewlett Packard Company, Network Infrastructure Solutions')
icfVgBasic = MibIdentifier((1, 3, 6, 1, 4, 1, 11, 2, 14, 8, 1, 1))
icfVgBasicRptr = MibIdentifier((1, 3, 6, 1, 4, 1, 11, 2, 14, 8, 1, 1, 1))
icfVgMACAddress = MibScalar((1, 3, 6, 1, 4, 1, 11, 2, 14, 8, 1, 1, 1, 1), MacAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: icfVgMACAddress.setStatus('current')
icfVgCurrentFramingType = MibScalar((1, 3, 6, 1, 4, 1, 11, 2, 14, 8, 1, 1, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("frameType88023", 1), ("frameType88025", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: icfVgCurrentFramingType.setStatus('current')
icfVgDesiredFramingType = MibScalar((1, 3, 6, 1, 4, 1, 11, 2, 14, 8, 1, 1, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("frameType88023", 1), ("frameType88025", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: icfVgDesiredFramingType.setStatus('current')
icfVgFramingCapability = MibScalar((1, 3, 6, 1, 4, 1, 11, 2, 14, 8, 1, 1, 1, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("frameType88023", 1), ("frameType88025", 2), ("frameTypeEither", 3)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: icfVgFramingCapability.setStatus('current')
icfVgTrainingVersion = MibScalar((1, 3, 6, 1, 4, 1, 11, 2, 14, 8, 1, 1, 1, 5), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 7))).setMaxAccess("readonly")
if mibBuilder.loadTexts: icfVgTrainingVersion.setStatus('current')
icfVgRepeaterGroupCapacity = MibScalar((1, 3, 6, 1, 4, 1, 11, 2, 14, 8, 1, 1, 1, 6), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 1024))).setMaxAccess("readonly")
if mibBuilder.loadTexts: icfVgRepeaterGroupCapacity.setStatus('current')
icfVgRepeaterHealthState = MibScalar((1, 3, 6, 1, 4, 1, 11, 2, 14, 8, 1, 1, 1, 7), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6))).clone(namedValues=NamedValues(("other", 1), ("ok", 2), ("rptrFailure", 3), ("groupFailure", 4), ("portFailure", 5), ("generalFailure", 6)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: icfVgRepeaterHealthState.setStatus('current')
icfVgRepeaterHealthText = MibScalar((1, 3, 6, 1, 4, 1, 11, 2, 14, 8, 1, 1, 1, 8), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 255))).setMaxAccess("readonly")
if mibBuilder.loadTexts: icfVgRepeaterHealthText.setStatus('current')
icfVgRepeaterReset = MibScalar((1, 3, 6, 1, 4, 1, 11, 2, 14, 8, 1, 1, 1, 9), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("noReset", 1), ("reset", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: icfVgRepeaterReset.setStatus('current')
icfVgRepeaterNonDisruptTest = MibScalar((1, 3, 6, 1, 4, 1, 11, 2, 14, 8, 1, 1, 1, 10), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("noSelfTest", 1), ("selfTest", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: icfVgRepeaterNonDisruptTest.setStatus('current')
icfVgBasicGroup = MibIdentifier((1, 3, 6, 1, 4, 1, 11, 2, 14, 8, 1, 1, 2))
icfVgBasicGroupTable = MibTable((1, 3, 6, 1, 4, 1, 11, 2, 14, 8, 1, 1, 2, 1), )
if mibBuilder.loadTexts: icfVgBasicGroupTable.setStatus('current')
icfVgBasicGroupEntry = MibTableRow((1, 3, 6, 1, 4, 1, 11, 2, 14, 8, 1, 1, 2, 1, 1), ).setIndexNames((0, "ICF-VG-RPTR", "icfVgGroupIndex"))
if mibBuilder.loadTexts: icfVgBasicGroupEntry.setStatus('current')
icfVgGroupIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 8, 1, 1, 2, 1, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 1024)))
if mibBuilder.loadTexts: icfVgGroupIndex.setStatus('current')
icfVgGroupDescr = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 8, 1, 1, 2, 1, 1, 2), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 255))).setMaxAccess("readonly")
if mibBuilder.loadTexts: icfVgGroupDescr.setStatus('current')
icfVgGroupObjectID = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 8, 1, 1, 2, 1, 1, 3), ObjectIdentifier()).setMaxAccess("readonly")
if mibBuilder.loadTexts: icfVgGroupObjectID.setStatus('current')
icfVgGroupOperStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 8, 1, 1, 2, 1, 1, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6))).clone(namedValues=NamedValues(("other", 1), ("operational", 2), ("malfunctioning", 3), ("notPresent", 4), ("underTest", 5), ("resetInProgress", 6)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: icfVgGroupOperStatus.setStatus('current')
icfVgGroupLastOperStatusChange = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 8, 1, 1, 2, 1, 1, 5), TimeStamp()).setMaxAccess("readonly")
if mibBuilder.loadTexts: icfVgGroupLastOperStatusChange.setStatus('current')
icfVgGroupPortCapacity = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 8, 1, 1, 2, 1, 1, 6), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 1024))).setMaxAccess("readonly")
if mibBuilder.loadTexts: icfVgGroupPortCapacity.setStatus('current')
icfVgGroupCablesBundled = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 8, 1, 1, 2, 1, 1, 7), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("someCablesBundled", 1), ("noCablesBundled", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: icfVgGroupCablesBundled.setStatus('current')
icfVgBasicPort = MibIdentifier((1, 3, 6, 1, 4, 1, 11, 2, 14, 8, 1, 1, 3))
icfVgBasicPortTable = MibTable((1, 3, 6, 1, 4, 1, 11, 2, 14, 8, 1, 1, 3, 1), )
if mibBuilder.loadTexts: icfVgBasicPortTable.setStatus('current')
icfVgBasicPortEntry = MibTableRow((1, 3, 6, 1, 4, 1, 11, 2, 14, 8, 1, 1, 3, 1, 1), ).setIndexNames((0, "ICF-VG-RPTR", "icfVgPortGroupIndex"), (0, "ICF-VG-RPTR", "icfVgPortIndex"))
if mibBuilder.loadTexts: icfVgBasicPortEntry.setStatus('current')
icfVgPortGroupIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 8, 1, 1, 3, 1, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 1024)))
if mibBuilder.loadTexts: icfVgPortGroupIndex.setStatus('current')
icfVgPortIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 8, 1, 1, 3, 1, 1, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 1024)))
if mibBuilder.loadTexts: icfVgPortIndex.setStatus('current')
icfVgPortType = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 8, 1, 1, 3, 1, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))).clone(namedValues=NamedValues(("cascadeExternal", 1), ("cascadeInternal", 2), ("localExternal", 3), ("localInternal", 4)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: icfVgPortType.setStatus('current')
icfVgPortAdminStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 8, 1, 1, 3, 1, 1, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enabled", 1), ("disabled", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: icfVgPortAdminStatus.setStatus('current')
icfVgPortStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 8, 1, 1, 3, 1, 1, 5), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("active", 1), ("inactive", 2), ("training", 3)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: icfVgPortStatus.setStatus('current')
icfVgPortSupportedPromiscMode = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 8, 1, 1, 3, 1, 1, 6), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("singleModeOnly", 1), ("singleOrPromiscMode", 2), ("promiscModeOnly", 3)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: icfVgPortSupportedPromiscMode.setStatus('current')
icfVgPortSupportedCascadeMode = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 8, 1, 1, 3, 1, 1, 7), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("endNodesOnly", 1), ("endNodesOrRepeaters", 2), ("cascadePort", 3)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: icfVgPortSupportedCascadeMode.setStatus('current')
icfVgPortAllowedTrainType = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 8, 1, 1, 3, 1, 1, 8), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))).clone(namedValues=NamedValues(("allowEndNodesOnly", 1), ("allowPromiscuousEndNodes", 2), ("allowEndNodesOrRepeaters", 3), ("allowAnything", 4)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: icfVgPortAllowedTrainType.setStatus('current')
icfVgPortLastTrainConfig = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 8, 1, 1, 3, 1, 1, 9), OctetString().subtype(subtypeSpec=ValueSizeConstraint(2, 2)).setFixedLength(2)).setMaxAccess("readonly")
if mibBuilder.loadTexts: icfVgPortLastTrainConfig.setStatus('current')
icfVgPortTrainingResult = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 8, 1, 1, 3, 1, 1, 10), OctetString().subtype(subtypeSpec=ValueSizeConstraint(3, 3)).setFixedLength(3)).setMaxAccess("readonly")
if mibBuilder.loadTexts: icfVgPortTrainingResult.setStatus('current')
icfVgPortPriorityEnable = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 8, 1, 1, 3, 1, 1, 11), TruthValue()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: icfVgPortPriorityEnable.setStatus('current')
icfVgPortMediaType = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 8, 1, 1, 3, 1, 1, 12), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6))).clone(namedValues=NamedValues(("other", 1), ("unknown", 2), ("pmdMissing", 3), ("utp4", 4), ("stp2", 5), ("fibre", 6)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: icfVgPortMediaType.setStatus('current')
icfVgMonitor = MibIdentifier((1, 3, 6, 1, 4, 1, 11, 2, 14, 8, 1, 2))
icfVgMonRptr = MibIdentifier((1, 3, 6, 1, 4, 1, 11, 2, 14, 8, 1, 2, 1))
icfVgMonGroup = MibIdentifier((1, 3, 6, 1, 4, 1, 11, 2, 14, 8, 1, 2, 2))
icfVgMonPort = MibIdentifier((1, 3, 6, 1, 4, 1, 11, 2, 14, 8, 1, 2, 3))
icfVgMonPortTable = MibTable((1, 3, 6, 1, 4, 1, 11, 2, 14, 8, 1, 2, 3, 1), )
if mibBuilder.loadTexts: icfVgMonPortTable.setStatus('current')
icfVgMonPortEntry = MibTableRow((1, 3, 6, 1, 4, 1, 11, 2, 14, 8, 1, 2, 3, 1, 1), ).setIndexNames((0, "ICF-VG-RPTR", "icfVgPortGroupIndex"), (0, "ICF-VG-RPTR", "icfVgPortIndex"))
if mibBuilder.loadTexts: icfVgMonPortEntry.setStatus('current')
icfVgPortReadableFrames = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 8, 1, 2, 3, 1, 1, 1), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: icfVgPortReadableFrames.setStatus('current')
icfVgPortReadableOctets = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 8, 1, 2, 3, 1, 1, 2), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: icfVgPortReadableOctets.setStatus('current')
icfVgPortUnreadableOctets = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 8, 1, 2, 3, 1, 1, 3), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: icfVgPortUnreadableOctets.setStatus('current')
icfVgPortHighPriorityFrames = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 8, 1, 2, 3, 1, 1, 4), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: icfVgPortHighPriorityFrames.setStatus('current')
icfVgPortHighPriorityOctets = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 8, 1, 2, 3, 1, 1, 5), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: icfVgPortHighPriorityOctets.setStatus('current')
icfVgPortBroadcastFrames = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 8, 1, 2, 3, 1, 1, 6), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: icfVgPortBroadcastFrames.setStatus('current')
icfVgPortMulticastFrames = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 8, 1, 2, 3, 1, 1, 7), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: icfVgPortMulticastFrames.setStatus('current')
icfVgPortIPMFrames = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 8, 1, 2, 3, 1, 1, 8), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: icfVgPortIPMFrames.setStatus('current')
icfVgPortDataErrorFrames = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 8, 1, 2, 3, 1, 1, 9), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: icfVgPortDataErrorFrames.setStatus('current')
icfVgPortPriorityPromotions = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 8, 1, 2, 3, 1, 1, 10), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: icfVgPortPriorityPromotions.setStatus('current')
icfVgPortHCReadableOctets = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 8, 1, 2, 3, 1, 1, 11), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: icfVgPortHCReadableOctets.setStatus('current')
icfVgPortHCUnreadableOctets = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 8, 1, 2, 3, 1, 1, 12), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: icfVgPortHCUnreadableOctets.setStatus('current')
icfVgPortHCHighPriorityOctets = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 8, 1, 2, 3, 1, 1, 13), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: icfVgPortHCHighPriorityOctets.setStatus('current')
icfVgPortHCNormPriorityOctets = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 8, 1, 2, 3, 1, 1, 14), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: icfVgPortHCNormPriorityOctets.setStatus('current')
icfVgPortNormPriorityFrames = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 8, 1, 2, 3, 1, 1, 15), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: icfVgPortNormPriorityFrames.setStatus('current')
icfVgPortNormPriorityOctets = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 8, 1, 2, 3, 1, 1, 16), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: icfVgPortNormPriorityOctets.setStatus('current')
icfVgPortNullAddressedFrames = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 8, 1, 2, 3, 1, 1, 17), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: icfVgPortNullAddressedFrames.setStatus('current')
icfVgPortOversizeFrames = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 8, 1, 2, 3, 1, 1, 18), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: icfVgPortOversizeFrames.setStatus('current')
icfVgPortTransitionToTrainings = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 8, 1, 2, 3, 1, 1, 19), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: icfVgPortTransitionToTrainings.setStatus('current')
icfVgAddrTrack = MibIdentifier((1, 3, 6, 1, 4, 1, 11, 2, 14, 8, 1, 3))
icfVgAddrTrackRptr = MibIdentifier((1, 3, 6, 1, 4, 1, 11, 2, 14, 8, 1, 3, 1))
icfVgAddrTrackGroup = MibIdentifier((1, 3, 6, 1, 4, 1, 11, 2, 14, 8, 1, 3, 2))
icfVgAddrTrackPort = MibIdentifier((1, 3, 6, 1, 4, 1, 11, 2, 14, 8, 1, 3, 3))
icfVgAddrTrackTable = MibTable((1, 3, 6, 1, 4, 1, 11, 2, 14, 8, 1, 3, 3, 1), )
if mibBuilder.loadTexts: icfVgAddrTrackTable.setStatus('current')
icfVgAddrTrackEntry = MibTableRow((1, 3, 6, 1, 4, 1, 11, 2, 14, 8, 1, 3, 3, 1, 1), ).setIndexNames((0, "ICF-VG-RPTR", "icfVgPortGroupIndex"), (0, "ICF-VG-RPTR", "icfVgPortIndex"))
if mibBuilder.loadTexts: icfVgAddrTrackEntry.setStatus('current')
icfVgAddrLastTrainedAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 8, 1, 3, 3, 1, 1, 1), OctetString().subtype(subtypeSpec=ConstraintsUnion(ValueSizeConstraint(0, 0), ValueSizeConstraint(6, 6), ))).setMaxAccess("readonly")
if mibBuilder.loadTexts: icfVgAddrLastTrainedAddress.setStatus('current')
icfVgAddrTrainedAddrChanges = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 8, 1, 3, 3, 1, 1, 2), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: icfVgAddrTrainedAddrChanges.setStatus('current')
icfVgRptrDetectedDupAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 8, 1, 3, 3, 1, 1, 3), TruthValue()).setMaxAccess("readonly")
if mibBuilder.loadTexts: icfVgRptrDetectedDupAddress.setStatus('current')
icfVgMgrDetectedDupAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 8, 1, 3, 3, 1, 1, 4), TruthValue()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: icfVgMgrDetectedDupAddress.setStatus('current')
icfVgRptrTraps = MibIdentifier((1, 3, 6, 1, 4, 1, 11, 2, 14, 8, 1, 4))
icfVgRptrTrapsPrefix = MibIdentifier((1, 3, 6, 1, 4, 1, 11, 2, 14, 8, 1, 4, 0))
icfVgRptrHealth = NotificationType((1, 3, 6, 1, 4, 1, 11, 2, 14, 8, 1, 4, 0, 1)).setObjects(("ICF-VG-RPTR", "icfVgRepeaterHealthState"))
if mibBuilder.loadTexts: icfVgRptrHealth.setStatus('current')
icfVgRptrResetEvent = NotificationType((1, 3, 6, 1, 4, 1, 11, 2, 14, 8, 1, 4, 0, 3)).setObjects(("ICF-VG-RPTR", "icfVgRepeaterHealthState"))
if mibBuilder.loadTexts: icfVgRptrResetEvent.setStatus('current')
icfVgRepeaterConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 11, 2, 14, 10, 2, 10, 1))
icfVgRepeaterCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 11, 2, 14, 10, 2, 10, 1, 1))
icfVgRepeaterGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 11, 2, 14, 10, 2, 10, 1, 2))
icfVgRptrPreStdCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 11, 2, 14, 10, 2, 10, 1, 1, 1)).setObjects(("ICF-VG-RPTR", "icfVgRptrBasicGroup"), ("ICF-VG-RPTR", "icfVgRptrPreStdMonitorGroup"), ("ICF-VG-RPTR", "icfVgRptrPreStdAddrTrackGroup"), ("ICF-VG-RPTR", "icfVgRptrNotificationsGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    icfVgRptrPreStdCompliance = icfVgRptrPreStdCompliance.setStatus('obsolete')
icfVgRptrCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 11, 2, 14, 10, 2, 10, 1, 1, 2)).setObjects(("ICF-VG-RPTR", "icfVgRptrBasicGroup"), ("ICF-VG-RPTR", "icfVgRptrMonitorGroup"), ("ICF-VG-RPTR", "icfVgRptrAddrTrackGroup"), ("ICF-VG-RPTR", "icfVgRptrNotificationsGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    icfVgRptrCompliance = icfVgRptrCompliance.setStatus('current')
icfVgRptrBasicGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 11, 2, 14, 10, 2, 10, 1, 2, 1)).setObjects(("ICF-VG-RPTR", "icfVgMACAddress"), ("ICF-VG-RPTR", "icfVgCurrentFramingType"), ("ICF-VG-RPTR", "icfVgDesiredFramingType"), ("ICF-VG-RPTR", "icfVgFramingCapability"), ("ICF-VG-RPTR", "icfVgTrainingVersion"), ("ICF-VG-RPTR", "icfVgRepeaterGroupCapacity"), ("ICF-VG-RPTR", "icfVgRepeaterHealthState"), ("ICF-VG-RPTR", "icfVgRepeaterHealthText"), ("ICF-VG-RPTR", "icfVgRepeaterReset"), ("ICF-VG-RPTR", "icfVgRepeaterNonDisruptTest"), ("ICF-VG-RPTR", "icfVgGroupDescr"), ("ICF-VG-RPTR", "icfVgGroupObjectID"), ("ICF-VG-RPTR", "icfVgGroupOperStatus"), ("ICF-VG-RPTR", "icfVgGroupLastOperStatusChange"), ("ICF-VG-RPTR", "icfVgGroupPortCapacity"), ("ICF-VG-RPTR", "icfVgGroupCablesBundled"), ("ICF-VG-RPTR", "icfVgPortType"), ("ICF-VG-RPTR", "icfVgPortAdminStatus"), ("ICF-VG-RPTR", "icfVgPortStatus"), ("ICF-VG-RPTR", "icfVgPortSupportedPromiscMode"), ("ICF-VG-RPTR", "icfVgPortSupportedCascadeMode"), ("ICF-VG-RPTR", "icfVgPortAllowedTrainType"), ("ICF-VG-RPTR", "icfVgPortLastTrainConfig"), ("ICF-VG-RPTR", "icfVgPortTrainingResult"), ("ICF-VG-RPTR", "icfVgPortPriorityEnable"), ("ICF-VG-RPTR", "icfVgPortMediaType"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    icfVgRptrBasicGroup = icfVgRptrBasicGroup.setStatus('current')
icfVgRptrPreStdMonitorGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 11, 2, 14, 10, 2, 10, 1, 2, 2)).setObjects(("ICF-VG-RPTR", "icfVgPortReadableFrames"), ("ICF-VG-RPTR", "icfVgPortReadableOctets"), ("ICF-VG-RPTR", "icfVgPortUnreadableOctets"), ("ICF-VG-RPTR", "icfVgPortHighPriorityFrames"), ("ICF-VG-RPTR", "icfVgPortHighPriorityOctets"), ("ICF-VG-RPTR", "icfVgPortBroadcastFrames"), ("ICF-VG-RPTR", "icfVgPortMulticastFrames"), ("ICF-VG-RPTR", "icfVgPortIPMFrames"), ("ICF-VG-RPTR", "icfVgPortDataErrorFrames"), ("ICF-VG-RPTR", "icfVgPortPriorityPromotions"), ("ICF-VG-RPTR", "icfVgPortHCReadableOctets"), ("ICF-VG-RPTR", "icfVgPortHCUnreadableOctets"), ("ICF-VG-RPTR", "icfVgPortHCHighPriorityOctets"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    icfVgRptrPreStdMonitorGroup = icfVgRptrPreStdMonitorGroup.setStatus('obsolete')
icfVgRptrPreStdAddrTrackGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 11, 2, 14, 10, 2, 10, 1, 2, 3)).setObjects(("ICF-VG-RPTR", "icfVgAddrLastTrainedAddress"), ("ICF-VG-RPTR", "icfVgAddrTrainedAddrChanges"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    icfVgRptrPreStdAddrTrackGroup = icfVgRptrPreStdAddrTrackGroup.setStatus('obsolete')
icfVgRptrMonitorGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 11, 2, 14, 10, 2, 10, 1, 2, 4)).setObjects(("ICF-VG-RPTR", "icfVgPortReadableFrames"), ("ICF-VG-RPTR", "icfVgPortReadableOctets"), ("ICF-VG-RPTR", "icfVgPortUnreadableOctets"), ("ICF-VG-RPTR", "icfVgPortHighPriorityFrames"), ("ICF-VG-RPTR", "icfVgPortHighPriorityOctets"), ("ICF-VG-RPTR", "icfVgPortBroadcastFrames"), ("ICF-VG-RPTR", "icfVgPortMulticastFrames"), ("ICF-VG-RPTR", "icfVgPortIPMFrames"), ("ICF-VG-RPTR", "icfVgPortDataErrorFrames"), ("ICF-VG-RPTR", "icfVgPortPriorityPromotions"), ("ICF-VG-RPTR", "icfVgPortHCReadableOctets"), ("ICF-VG-RPTR", "icfVgPortHCUnreadableOctets"), ("ICF-VG-RPTR", "icfVgPortHCHighPriorityOctets"), ("ICF-VG-RPTR", "icfVgPortHCNormPriorityOctets"), ("ICF-VG-RPTR", "icfVgPortNormPriorityFrames"), ("ICF-VG-RPTR", "icfVgPortNormPriorityOctets"), ("ICF-VG-RPTR", "icfVgPortNullAddressedFrames"), ("ICF-VG-RPTR", "icfVgPortOversizeFrames"), ("ICF-VG-RPTR", "icfVgPortTransitionToTrainings"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    icfVgRptrMonitorGroup = icfVgRptrMonitorGroup.setStatus('current')
icfVgRptrAddrTrackGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 11, 2, 14, 10, 2, 10, 1, 2, 5)).setObjects(("ICF-VG-RPTR", "icfVgAddrLastTrainedAddress"), ("ICF-VG-RPTR", "icfVgAddrTrainedAddrChanges"), ("ICF-VG-RPTR", "icfVgRptrDetectedDupAddress"), ("ICF-VG-RPTR", "icfVgMgrDetectedDupAddress"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    icfVgRptrAddrTrackGroup = icfVgRptrAddrTrackGroup.setStatus('current')
icfVgRptrNotificationsGroup = NotificationGroup((1, 3, 6, 1, 4, 1, 11, 2, 14, 10, 2, 10, 1, 2, 6)).setObjects(("ICF-VG-RPTR", "icfVgRptrHealth"), ("ICF-VG-RPTR", "icfVgRptrResetEvent"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    icfVgRptrNotificationsGroup = icfVgRptrNotificationsGroup.setStatus('current')
mibBuilder.exportSymbols("ICF-VG-RPTR", icfVgGroupLastOperStatusChange=icfVgGroupLastOperStatusChange, icfVgPortBroadcastFrames=icfVgPortBroadcastFrames, icfVgRptrTrapsPrefix=icfVgRptrTrapsPrefix, icfVgBasicPort=icfVgBasicPort, icfVgPortPriorityPromotions=icfVgPortPriorityPromotions, icfVgRptrPreStdAddrTrackGroup=icfVgRptrPreStdAddrTrackGroup, icfVgMACAddress=icfVgMACAddress, icfVgRepeaterConformance=icfVgRepeaterConformance, icfVgRptrHealth=icfVgRptrHealth, icfVgCurrentFramingType=icfVgCurrentFramingType, icfVgFramingCapability=icfVgFramingCapability, icfVgPortIPMFrames=icfVgPortIPMFrames, icfVgPortHCReadableOctets=icfVgPortHCReadableOctets, icfVgPortSupportedCascadeMode=icfVgPortSupportedCascadeMode, icfVgPortTransitionToTrainings=icfVgPortTransitionToTrainings, icfVgRepeaterReset=icfVgRepeaterReset, icfVgRptrAddrTrackGroup=icfVgRptrAddrTrackGroup, icfVgAddrTrainedAddrChanges=icfVgAddrTrainedAddrChanges, icfVgBasic=icfVgBasic, icfVgPortReadableOctets=icfVgPortReadableOctets, icfVgMonPortTable=icfVgMonPortTable, icfVgAddrTrackTable=icfVgAddrTrackTable, icfVgPortAdminStatus=icfVgPortAdminStatus, icfVgRptrCompliance=icfVgRptrCompliance, icfVgMonPort=icfVgMonPort, icfVgAddrTrackPort=icfVgAddrTrackPort, icfVgRptrResetEvent=icfVgRptrResetEvent, icfVgPortLastTrainConfig=icfVgPortLastTrainConfig, icfVgPortNormPriorityFrames=icfVgPortNormPriorityFrames, icfVgRepeaterNonDisruptTest=icfVgRepeaterNonDisruptTest, icfVgBasicGroupTable=icfVgBasicGroupTable, icfVgAddrTrackRptr=icfVgAddrTrackRptr, icfVgPortNormPriorityOctets=icfVgPortNormPriorityOctets, icfVgAddrTrackGroup=icfVgAddrTrackGroup, icfVgRptrTraps=icfVgRptrTraps, icfVgPortIndex=icfVgPortIndex, icfVgBasicGroupEntry=icfVgBasicGroupEntry, PYSNMP_MODULE_ID=icfVgRepeaterMib, icfVgMgrDetectedDupAddress=icfVgMgrDetectedDupAddress, icfVgRepeaterHealthState=icfVgRepeaterHealthState, icfVgPortSupportedPromiscMode=icfVgPortSupportedPromiscMode, icfVgRptrPreStdMonitorGroup=icfVgRptrPreStdMonitorGroup, icfVgRepeaterGroups=icfVgRepeaterGroups, icfVgRepeaterHealthText=icfVgRepeaterHealthText, icfVgPortOversizeFrames=icfVgPortOversizeFrames, icfVgAddrTrackEntry=icfVgAddrTrackEntry, icfVgPortHCHighPriorityOctets=icfVgPortHCHighPriorityOctets, icfVgPortAllowedTrainType=icfVgPortAllowedTrainType, icfVgPortReadableFrames=icfVgPortReadableFrames, icfVgBasicPortEntry=icfVgBasicPortEntry, icfVgRptrPreStdCompliance=icfVgRptrPreStdCompliance, icfVgPortHCUnreadableOctets=icfVgPortHCUnreadableOctets, icfVgAddrTrack=icfVgAddrTrack, icfVgGroupIndex=icfVgGroupIndex, icfVgPortHighPriorityFrames=icfVgPortHighPriorityFrames, icfVgMonGroup=icfVgMonGroup, icfVgGroupOperStatus=icfVgGroupOperStatus, icfVgBasicGroup=icfVgBasicGroup, icfVgRptrMonitorGroup=icfVgRptrMonitorGroup, icfVgGroupCablesBundled=icfVgGroupCablesBundled, icfVgTrainingVersion=icfVgTrainingVersion, icfVgPortHCNormPriorityOctets=icfVgPortHCNormPriorityOctets, icfVgPortMulticastFrames=icfVgPortMulticastFrames, icfVgRptrNotificationsGroup=icfVgRptrNotificationsGroup, icfVgPortStatus=icfVgPortStatus, icfVgMonitor=icfVgMonitor, icfVgRepeaterGroupCapacity=icfVgRepeaterGroupCapacity, icfVgBasicRptr=icfVgBasicRptr, icfVgPortTrainingResult=icfVgPortTrainingResult, icfVgRepeaterMib=icfVgRepeaterMib, icfVgDesiredFramingType=icfVgDesiredFramingType, icfVgRepeaterCompliances=icfVgRepeaterCompliances, icfVgPortGroupIndex=icfVgPortGroupIndex, icfVgAddrLastTrainedAddress=icfVgAddrLastTrainedAddress, icfVgPortType=icfVgPortType, icfVgPortNullAddressedFrames=icfVgPortNullAddressedFrames, icfVgGroupObjectID=icfVgGroupObjectID, icfVgPortMediaType=icfVgPortMediaType, icfVgGroupDescr=icfVgGroupDescr, icfVgGroupPortCapacity=icfVgGroupPortCapacity, icfVgPortPriorityEnable=icfVgPortPriorityEnable, icfVgRptrDetectedDupAddress=icfVgRptrDetectedDupAddress, icfVgPortDataErrorFrames=icfVgPortDataErrorFrames, icfVgPortUnreadableOctets=icfVgPortUnreadableOctets, icfVgRptrBasicGroup=icfVgRptrBasicGroup, icfVgPortHighPriorityOctets=icfVgPortHighPriorityOctets, icfVgBasicPortTable=icfVgBasicPortTable, icfVgMonRptr=icfVgMonRptr, icfVgMonPortEntry=icfVgMonPortEntry)