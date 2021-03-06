#
# PySNMP MIB module DLINK-3100-CDB-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/DLINK-3100-CDB-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 18:33:07 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
OctetString, Integer, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "OctetString", "Integer", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, ConstraintsUnion, ConstraintsIntersection, SingleValueConstraint, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "ConstraintsUnion", "ConstraintsIntersection", "SingleValueConstraint", "ValueSizeConstraint")
rnd, = mibBuilder.importSymbols("DLINK-3100-MIB", "rnd")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
Bits, Unsigned32, Counter32, iso, Gauge32, IpAddress, NotificationType, MibIdentifier, Integer32, Counter64, ObjectIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, TimeTicks, ModuleIdentity = mibBuilder.importSymbols("SNMPv2-SMI", "Bits", "Unsigned32", "Counter32", "iso", "Gauge32", "IpAddress", "NotificationType", "MibIdentifier", "Integer32", "Counter64", "ObjectIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "TimeTicks", "ModuleIdentity")
DisplayString, TextualConvention, TruthValue = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention", "TruthValue")
rlCDB = ModuleIdentity((1, 3, 6, 1, 4, 1, 171, 10, 94, 89, 89, 94))
rlCDB.setRevisions(('2007-01-02 00:00',))
if mibBuilder.loadTexts: rlCDB.setLastUpdated('200701020000Z')
if mibBuilder.loadTexts: rlCDB.setOrganization('Dlink, Inc. Dlink Semiconductor, Inc.')
rlStartupCDBChanged = MibScalar((1, 3, 6, 1, 4, 1, 171, 10, 94, 89, 89, 94, 1), TruthValue()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rlStartupCDBChanged.setStatus('current')
rlManualReboot = MibScalar((1, 3, 6, 1, 4, 1, 171, 10, 94, 89, 89, 94, 2), TruthValue()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rlManualReboot.setStatus('current')
mibBuilder.exportSymbols("DLINK-3100-CDB-MIB", rlCDB=rlCDB, rlManualReboot=rlManualReboot, PYSNMP_MODULE_ID=rlCDB, rlStartupCDBChanged=rlStartupCDBChanged)
