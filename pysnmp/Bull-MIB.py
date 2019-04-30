#
# PySNMP MIB module Bull-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/Bull-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 17:25:40 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ConstraintsUnion, ValueRangeConstraint, ValueSizeConstraint, SingleValueConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ConstraintsUnion", "ValueRangeConstraint", "ValueSizeConstraint", "SingleValueConstraint")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
IpAddress, NotificationType, ModuleIdentity, Counter32, Counter64, Unsigned32, MibIdentifier, TimeTicks, MibScalar, MibTable, MibTableRow, MibTableColumn, Integer32, Gauge32, ObjectIdentity, Bits, enterprises, iso = mibBuilder.importSymbols("SNMPv2-SMI", "IpAddress", "NotificationType", "ModuleIdentity", "Counter32", "Counter64", "Unsigned32", "MibIdentifier", "TimeTicks", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Integer32", "Gauge32", "ObjectIdentity", "Bits", "enterprises", "iso")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
bull = MibIdentifier((1, 3, 6, 1, 4, 1, 107))
bull_products = MibIdentifier((1, 3, 6, 1, 4, 1, 107, 1)).setLabel("bull-products")
bull_DPX2 = MibIdentifier((1, 3, 6, 1, 4, 1, 107, 1, 1)).setLabel("bull-DPX2")
bull_mibs = MibIdentifier((1, 3, 6, 1, 4, 1, 107, 2)).setLabel("bull-mibs")
bull_mibs_mib1 = MibIdentifier((1, 3, 6, 1, 4, 1, 107, 2, 1)).setLabel("bull-mibs-mib1")
bull_System = MibIdentifier((1, 3, 6, 1, 4, 1, 107, 2, 1, 1)).setLabel("bull-System")
bull_Streams = MibIdentifier((1, 3, 6, 1, 4, 1, 107, 2, 1, 2)).setLabel("bull-Streams")
bull_Ether = MibIdentifier((1, 3, 6, 1, 4, 1, 107, 2, 1, 3)).setLabel("bull-Ether")
bull_Serial = MibIdentifier((1, 3, 6, 1, 4, 1, 107, 2, 1, 4)).setLabel("bull-Serial")
bull_X25 = MibIdentifier((1, 3, 6, 1, 4, 1, 107, 2, 1, 5)).setLabel("bull-X25")
bull_NMFX = MibIdentifier((1, 3, 6, 1, 4, 1, 107, 2, 1, 6)).setLabel("bull-NMFX")
bull_DPX2_100 = MibScalar((1, 3, 6, 1, 4, 1, 107, 1, 1, 1), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 255))).setLabel("bull-DPX2-100").setMaxAccess("readonly")
if mibBuilder.loadTexts: bull_DPX2_100.setStatus('optional')
bull_DPX2_200 = MibScalar((1, 3, 6, 1, 4, 1, 107, 1, 1, 2), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 255))).setLabel("bull-DPX2-200").setMaxAccess("readonly")
if mibBuilder.loadTexts: bull_DPX2_200.setStatus('optional')
bull_DPX2_300 = MibScalar((1, 3, 6, 1, 4, 1, 107, 1, 1, 3), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 255))).setLabel("bull-DPX2-300").setMaxAccess("readonly")
if mibBuilder.loadTexts: bull_DPX2_300.setStatus('optional')
bullStrTable = MibTable((1, 3, 6, 1, 4, 1, 107, 2, 1, 2, 1), )
if mibBuilder.loadTexts: bullStrTable.setStatus('mandatory')
bullStrEntry = MibTableRow((1, 3, 6, 1, 4, 1, 107, 2, 1, 2, 1, 1), ).setIndexNames((0, "Bull-MIB", "bullStrType"))
if mibBuilder.loadTexts: bullStrEntry.setStatus('mandatory')
bullStrType = MibTableColumn((1, 3, 6, 1, 4, 1, 107, 2, 1, 2, 1, 1, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))).clone(namedValues=NamedValues(("streams", 1), ("queues", 2), ("messages", 3), ("blocks", 4)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: bullStrType.setStatus('mandatory')
bullStrAlloc = MibTableColumn((1, 3, 6, 1, 4, 1, 107, 2, 1, 2, 1, 1, 2), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: bullStrAlloc.setStatus('mandatory')
bullStrInuse = MibTableColumn((1, 3, 6, 1, 4, 1, 107, 2, 1, 2, 1, 1, 3), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: bullStrInuse.setStatus('mandatory')
bullStrMaxs = MibTableColumn((1, 3, 6, 1, 4, 1, 107, 2, 1, 2, 1, 1, 4), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: bullStrMaxs.setStatus('mandatory')
bullStrTotals = MibTableColumn((1, 3, 6, 1, 4, 1, 107, 2, 1, 2, 1, 1, 5), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: bullStrTotals.setStatus('mandatory')
bullStrFails = MibTableColumn((1, 3, 6, 1, 4, 1, 107, 2, 1, 2, 1, 1, 6), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: bullStrFails.setStatus('mandatory')
bullBlkTable = MibTable((1, 3, 6, 1, 4, 1, 107, 2, 1, 2, 2), )
if mibBuilder.loadTexts: bullBlkTable.setStatus('mandatory')
bullBlkEntry = MibTableRow((1, 3, 6, 1, 4, 1, 107, 2, 1, 2, 2, 1), ).setIndexNames((0, "Bull-MIB", "bullBlkclass"))
if mibBuilder.loadTexts: bullBlkEntry.setStatus('mandatory')
bullBlkClass = MibTableColumn((1, 3, 6, 1, 4, 1, 107, 2, 1, 2, 2, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 10))).setMaxAccess("readonly")
if mibBuilder.loadTexts: bullBlkClass.setStatus('mandatory')
bullBlkAlloc = MibTableColumn((1, 3, 6, 1, 4, 1, 107, 2, 1, 2, 2, 1, 2), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: bullBlkAlloc.setStatus('mandatory')
bullBlkInuse = MibTableColumn((1, 3, 6, 1, 4, 1, 107, 2, 1, 2, 2, 1, 3), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: bullBlkInuse.setStatus('mandatory')
bullBlkLowpris = MibTableColumn((1, 3, 6, 1, 4, 1, 107, 2, 1, 2, 2, 1, 5), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: bullBlkLowpris.setStatus('mandatory')
bullBlkMedpris = MibTableColumn((1, 3, 6, 1, 4, 1, 107, 2, 1, 2, 2, 1, 6), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: bullBlkMedpris.setStatus('mandatory')
bullBlkMaxs = MibTableColumn((1, 3, 6, 1, 4, 1, 107, 2, 1, 2, 2, 1, 7), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: bullBlkMaxs.setStatus('mandatory')
bullBlkTotals = MibTableColumn((1, 3, 6, 1, 4, 1, 107, 2, 1, 2, 2, 1, 8), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: bullBlkTotals.setStatus('mandatory')
bullBlkFails = MibTableColumn((1, 3, 6, 1, 4, 1, 107, 2, 1, 2, 2, 1, 9), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: bullBlkFails.setStatus('mandatory')
mibBuilder.exportSymbols("Bull-MIB", bullBlkAlloc=bullBlkAlloc, bull_Serial=bull_Serial, bullStrEntry=bullStrEntry, bull=bull, bull_Ether=bull_Ether, bullStrType=bullStrType, bullBlkFails=bullBlkFails, bullStrTotals=bullStrTotals, bullStrInuse=bullStrInuse, bullStrAlloc=bullStrAlloc, bullBlkClass=bullBlkClass, bullBlkTable=bullBlkTable, bull_NMFX=bull_NMFX, bull_DPX2_200=bull_DPX2_200, bull_products=bull_products, bull_mibs_mib1=bull_mibs_mib1, bullBlkMedpris=bullBlkMedpris, bull_Streams=bull_Streams, bull_X25=bull_X25, bull_DPX2=bull_DPX2, bullBlkInuse=bullBlkInuse, bullStrTable=bullStrTable, bull_DPX2_300=bull_DPX2_300, bullStrFails=bullStrFails, bull_System=bull_System, bullStrMaxs=bullStrMaxs, bullBlkEntry=bullBlkEntry, bullBlkLowpris=bullBlkLowpris, bullBlkMaxs=bullBlkMaxs, bull_mibs=bull_mibs, bull_DPX2_100=bull_DPX2_100, bullBlkTotals=bullBlkTotals)