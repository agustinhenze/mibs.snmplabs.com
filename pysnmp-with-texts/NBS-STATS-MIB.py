#
# PySNMP MIB module NBS-STATS-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/NBS-STATS-MIB
# Produced by pysmi-0.3.4 at Wed May  1 14:17:42 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsIntersection, SingleValueConstraint, ConstraintsUnion, ValueRangeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsIntersection", "SingleValueConstraint", "ConstraintsUnion", "ValueRangeConstraint")
InterfaceIndex, = mibBuilder.importSymbols("IF-MIB", "InterfaceIndex")
nbs, = mibBuilder.importSymbols("NBS-MIB", "nbs")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
Counter64, IpAddress, NotificationType, Integer32, ModuleIdentity, Bits, MibScalar, MibTable, MibTableRow, MibTableColumn, ObjectIdentity, TimeTicks, Counter32, iso, Unsigned32, Gauge32, MibIdentifier = mibBuilder.importSymbols("SNMPv2-SMI", "Counter64", "IpAddress", "NotificationType", "Integer32", "ModuleIdentity", "Bits", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "ObjectIdentity", "TimeTicks", "Counter32", "iso", "Unsigned32", "Gauge32", "MibIdentifier")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
nbsStatsMib = ModuleIdentity((1, 3, 6, 1, 4, 1, 629, 233))
if mibBuilder.loadTexts: nbsStatsMib.setLastUpdated('201303130000Z')
if mibBuilder.loadTexts: nbsStatsMib.setOrganization('NBS')
if mibBuilder.loadTexts: nbsStatsMib.setContactInfo('For technical support, please contact your service channel')
if mibBuilder.loadTexts: nbsStatsMib.setDescription('For managing statistics')
nbsStatInfoGrp = ObjectIdentity((1, 3, 6, 1, 4, 1, 629, 233, 1))
if mibBuilder.loadTexts: nbsStatInfoGrp.setStatus('current')
if mibBuilder.loadTexts: nbsStatInfoGrp.setDescription('')
nbsStatInfoTable = MibTable((1, 3, 6, 1, 4, 1, 629, 233, 1, 10), )
if mibBuilder.loadTexts: nbsStatInfoTable.setStatus('current')
if mibBuilder.loadTexts: nbsStatInfoTable.setDescription('A table that provides basic control information for entity (typically ports) statistics.')
nbsStatInfoEntry = MibTableRow((1, 3, 6, 1, 4, 1, 629, 233, 1, 10, 1), ).setIndexNames((0, "NBS-STATS-MIB", "nbsStatInfoIndex"))
if mibBuilder.loadTexts: nbsStatInfoEntry.setStatus('current')
if mibBuilder.loadTexts: nbsStatInfoEntry.setDescription('Contains a description of a particular statistics entity')
nbsStatInfoIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 629, 233, 1, 10, 1, 1), InterfaceIndex()).setMaxAccess("readonly")
if mibBuilder.loadTexts: nbsStatInfoIndex.setStatus('current')
if mibBuilder.loadTexts: nbsStatInfoIndex.setDescription('ifIndex-like identifier of a component that has statistics.')
nbsStatInfoCounters = MibTableColumn((1, 3, 6, 1, 4, 1, 629, 233, 1, 10, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("notSupported", 1), ("counting", 2), ("clearing", 3)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: nbsStatInfoCounters.setStatus('current')
if mibBuilder.loadTexts: nbsStatInfoCounters.setDescription('Used to clear all entity-specific counters to zero. Aliased/Equivalent to NBS-CMMC-MIB CountersState objects.')
nbsStatInfoPmData = MibTableColumn((1, 3, 6, 1, 4, 1, 629, 233, 1, 10, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("notSupported", 1), ("counting", 2), ("clearing", 3)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: nbsStatInfoPmData.setStatus('current')
if mibBuilder.loadTexts: nbsStatInfoPmData.setDescription('Used to clear all entity-specific performance monitoring (PM) data to zero. Examples include: nbsFecpmCurrentTable, nbsFecpmHistoricTable, nbsFecpmRunningTable, nbsOtnpmCurrentTable, nbsOtnpmHistoricTable, and nbsOtnpmRunningTable.')
mibBuilder.exportSymbols("NBS-STATS-MIB", nbsStatInfoCounters=nbsStatInfoCounters, nbsStatInfoTable=nbsStatInfoTable, nbsStatsMib=nbsStatsMib, nbsStatInfoIndex=nbsStatInfoIndex, PYSNMP_MODULE_ID=nbsStatsMib, nbsStatInfoGrp=nbsStatInfoGrp, nbsStatInfoPmData=nbsStatInfoPmData, nbsStatInfoEntry=nbsStatInfoEntry)
