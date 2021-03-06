#
# PySNMP MIB module HPN-ICF-LPBKDT-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/HPN-ICF-LPBKDT-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 19:27:33 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
ObjectIdentifier, Integer, OctetString = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "Integer", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, SingleValueConstraint, ConstraintsIntersection, ValueRangeConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "SingleValueConstraint", "ConstraintsIntersection", "ValueRangeConstraint", "ConstraintsUnion")
hpnicfCommon, = mibBuilder.importSymbols("HPN-ICF-OID-MIB", "hpnicfCommon")
ifDescr, ifIndex = mibBuilder.importSymbols("IF-MIB", "ifDescr", "ifIndex")
VlanId, = mibBuilder.importSymbols("Q-BRIDGE-MIB", "VlanId")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
Integer32, IpAddress, MibScalar, MibTable, MibTableRow, MibTableColumn, Gauge32, ObjectIdentity, Bits, MibIdentifier, Unsigned32, NotificationType, iso, ModuleIdentity, TimeTicks, Counter32, Counter64 = mibBuilder.importSymbols("SNMPv2-SMI", "Integer32", "IpAddress", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Gauge32", "ObjectIdentity", "Bits", "MibIdentifier", "Unsigned32", "NotificationType", "iso", "ModuleIdentity", "TimeTicks", "Counter32", "Counter64")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
hpnicfLpbkdt = ModuleIdentity((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 95))
hpnicfLpbkdt.setRevisions(('2009-03-30 17:41', '2008-09-27 15:04',))
if mibBuilder.loadTexts: hpnicfLpbkdt.setLastUpdated('200903301741Z')
if mibBuilder.loadTexts: hpnicfLpbkdt.setOrganization('')
hpnicfLpbkdtNotifications = MibIdentifier((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 95, 1))
hpnicfLpbkdtObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 95, 2))
hpnicfLpbkdtTrapPrefix = MibIdentifier((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 95, 1, 0))
hpnicfLpbkdtTrapLoopbacked = NotificationType((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 95, 1, 0, 1)).setObjects(("IF-MIB", "ifIndex"), ("IF-MIB", "ifDescr"))
if mibBuilder.loadTexts: hpnicfLpbkdtTrapLoopbacked.setStatus('current')
hpnicfLpbkdtTrapRecovered = NotificationType((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 95, 1, 0, 2)).setObjects(("IF-MIB", "ifIndex"), ("IF-MIB", "ifDescr"))
if mibBuilder.loadTexts: hpnicfLpbkdtTrapRecovered.setStatus('current')
hpnicfLpbkdtTrapPerVlanLoopbacked = NotificationType((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 95, 1, 0, 3)).setObjects(("IF-MIB", "ifIndex"), ("IF-MIB", "ifDescr"), ("HPN-ICF-LPBKDT-MIB", "hpnicfLpbkdtVlanID"))
if mibBuilder.loadTexts: hpnicfLpbkdtTrapPerVlanLoopbacked.setStatus('current')
hpnicfLpbkdtTrapPerVlanRecovered = NotificationType((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 95, 1, 0, 4)).setObjects(("IF-MIB", "ifIndex"), ("IF-MIB", "ifDescr"), ("HPN-ICF-LPBKDT-MIB", "hpnicfLpbkdtVlanID"))
if mibBuilder.loadTexts: hpnicfLpbkdtTrapPerVlanRecovered.setStatus('current')
hpnicfLpbkdtVlanID = MibScalar((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 95, 2, 1), VlanId()).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: hpnicfLpbkdtVlanID.setStatus('current')
mibBuilder.exportSymbols("HPN-ICF-LPBKDT-MIB", hpnicfLpbkdt=hpnicfLpbkdt, hpnicfLpbkdtTrapPrefix=hpnicfLpbkdtTrapPrefix, hpnicfLpbkdtTrapRecovered=hpnicfLpbkdtTrapRecovered, hpnicfLpbkdtTrapLoopbacked=hpnicfLpbkdtTrapLoopbacked, hpnicfLpbkdtTrapPerVlanLoopbacked=hpnicfLpbkdtTrapPerVlanLoopbacked, hpnicfLpbkdtObjects=hpnicfLpbkdtObjects, hpnicfLpbkdtTrapPerVlanRecovered=hpnicfLpbkdtTrapPerVlanRecovered, hpnicfLpbkdtVlanID=hpnicfLpbkdtVlanID, hpnicfLpbkdtNotifications=hpnicfLpbkdtNotifications, PYSNMP_MODULE_ID=hpnicfLpbkdt)
