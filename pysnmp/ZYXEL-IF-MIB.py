#
# PySNMP MIB module ZYXEL-IF-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/ZYXEL-IF-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 21:44:07 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
SingleValueConstraint, ConstraintsIntersection, ValueRangeConstraint, ConstraintsUnion, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "SingleValueConstraint", "ConstraintsIntersection", "ValueRangeConstraint", "ConstraintsUnion", "ValueSizeConstraint")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
iso, NotificationType, Counter32, IpAddress, Bits, ObjectIdentity, Integer32, ModuleIdentity, Unsigned32, MibIdentifier, Counter64, TimeTicks, Gauge32, MibScalar, MibTable, MibTableRow, MibTableColumn = mibBuilder.importSymbols("SNMPv2-SMI", "iso", "NotificationType", "Counter32", "IpAddress", "Bits", "ObjectIdentity", "Integer32", "ModuleIdentity", "Unsigned32", "MibIdentifier", "Counter64", "TimeTicks", "Gauge32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn")
RowStatus, DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "RowStatus", "DisplayString", "TextualConvention")
esMgmt, = mibBuilder.importSymbols("ZYXEL-ES-SMI", "esMgmt")
zyxelIf = ModuleIdentity((1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 27))
if mibBuilder.loadTexts: zyxelIf.setLastUpdated('201207010000Z')
if mibBuilder.loadTexts: zyxelIf.setOrganization('Enterprise Solution ZyXEL')
zyxelIfSetup = MibIdentifier((1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 27, 1))
zyIfMaxNumberOfVlanIfs = MibScalar((1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 27, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: zyIfMaxNumberOfVlanIfs.setStatus('current')
zyIfMaxNumberOfLoopbackIfs = MibScalar((1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 27, 1, 2), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: zyIfMaxNumberOfLoopbackIfs.setStatus('current')
zyxelIfTable = MibTable((1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 27, 1, 3), )
if mibBuilder.loadTexts: zyxelIfTable.setStatus('current')
zyxelIfEntry = MibTableRow((1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 27, 1, 3, 1), ).setIndexNames((0, "ZYXEL-IF-MIB", "zyIfType"), (0, "ZYXEL-IF-MIB", "zyIfId"))
if mibBuilder.loadTexts: zyxelIfEntry.setStatus('current')
zyIfType = MibTableColumn((1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 27, 1, 3, 1, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("vlan", 1), ("loopback", 2))))
if mibBuilder.loadTexts: zyIfType.setStatus('current')
zyIfId = MibTableColumn((1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 27, 1, 3, 1, 2), Integer32())
if mibBuilder.loadTexts: zyIfId.setStatus('current')
zyIfRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 27, 1, 3, 1, 3), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: zyIfRowStatus.setStatus('current')
mibBuilder.exportSymbols("ZYXEL-IF-MIB", PYSNMP_MODULE_ID=zyxelIf, zyxelIf=zyxelIf, zyxelIfEntry=zyxelIfEntry, zyIfType=zyIfType, zyIfMaxNumberOfVlanIfs=zyIfMaxNumberOfVlanIfs, zyxelIfSetup=zyxelIfSetup, zyIfId=zyIfId, zyxelIfTable=zyxelIfTable, zyIfRowStatus=zyIfRowStatus, zyIfMaxNumberOfLoopbackIfs=zyIfMaxNumberOfLoopbackIfs)