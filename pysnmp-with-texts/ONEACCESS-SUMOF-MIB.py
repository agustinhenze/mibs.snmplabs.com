#
# PySNMP MIB module ONEACCESS-SUMOF-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/ONEACCESS-SUMOF-MIB
# Produced by pysmi-0.3.4 at Wed May  1 14:34:41 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
OctetString, ObjectIdentifier, Integer = mibBuilder.importSymbols("ASN1", "OctetString", "ObjectIdentifier", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsIntersection, SingleValueConstraint, ValueRangeConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsIntersection", "SingleValueConstraint", "ValueRangeConstraint", "ConstraintsUnion")
ifIndex, = mibBuilder.importSymbols("IF-MIB", "ifIndex")
oacExpIMManagement, = mibBuilder.importSymbols("ONEACCESS-GLOBAL-REG", "oacExpIMManagement")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
ObjectIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, NotificationType, Integer32, Counter64, Counter32, iso, Unsigned32, Gauge32, TimeTicks, MibIdentifier, ModuleIdentity, Bits, IpAddress = mibBuilder.importSymbols("SNMPv2-SMI", "ObjectIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "NotificationType", "Integer32", "Counter64", "Counter32", "iso", "Unsigned32", "Gauge32", "TimeTicks", "MibIdentifier", "ModuleIdentity", "Bits", "IpAddress")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
oacSumOfMIBModule = ModuleIdentity((1, 3, 6, 1, 4, 1, 13191, 10, 3, 4, 7))
oacSumOfMIBModule.setRevisions(('2011-10-27 00:00', '2010-07-08 00:01',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: oacSumOfMIBModule.setRevisionsDescriptions(('Fixed Minor correction added last revision.', 'This MIB module describes ... something.',))
if mibBuilder.loadTexts: oacSumOfMIBModule.setLastUpdated('201110270000Z')
if mibBuilder.loadTexts: oacSumOfMIBModule.setOrganization(' OneAccess ')
if mibBuilder.loadTexts: oacSumOfMIBModule.setContactInfo('Pascal KESTELOOT Postal: ONE ACCESS 381 Avenue du Gnral de Gaulle 92140 Clamart, France FRANCE Tel: (+33) 01 41 87 70 00 Fax: (+33) 01 41 87 74 00 E-mail: pascal.kesteloot@oneaccess-net.com')
if mibBuilder.loadTexts: oacSumOfMIBModule.setDescription('Contact updated')
oacSumOfObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 13191, 10, 3, 4, 7, 1))
oacSumOfIfTable = MibTable((1, 3, 6, 1, 4, 1, 13191, 10, 3, 4, 7, 1, 1), )
if mibBuilder.loadTexts: oacSumOfIfTable.setStatus('current')
if mibBuilder.loadTexts: oacSumOfIfTable.setDescription('The table representing the oacSumOfIfTable')
oacSumOfIfEntry = MibTableRow((1, 3, 6, 1, 4, 1, 13191, 10, 3, 4, 7, 1, 1, 1), ).setIndexNames((0, "IF-MIB", "ifIndex"))
if mibBuilder.loadTexts: oacSumOfIfEntry.setStatus('current')
if mibBuilder.loadTexts: oacSumOfIfEntry.setDescription('Defines an entry in the oacSumOfIfTable.')
sumOfIfInOctets = MibTableColumn((1, 3, 6, 1, 4, 1, 13191, 10, 3, 4, 7, 1, 1, 1, 1), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sumOfIfInOctets.setStatus('current')
if mibBuilder.loadTexts: sumOfIfInOctets.setDescription('The sum of ifInOctets for the subinterfaces of this interface.')
sumOfIfInUcastPkts = MibTableColumn((1, 3, 6, 1, 4, 1, 13191, 10, 3, 4, 7, 1, 1, 1, 2), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sumOfIfInUcastPkts.setStatus('current')
if mibBuilder.loadTexts: sumOfIfInUcastPkts.setDescription('The sum of ifInUcastPkts for the subinterfaces of this interface.')
sumOfIfInNUcastPkts = MibTableColumn((1, 3, 6, 1, 4, 1, 13191, 10, 3, 4, 7, 1, 1, 1, 3), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sumOfIfInNUcastPkts.setStatus('current')
if mibBuilder.loadTexts: sumOfIfInNUcastPkts.setDescription('The sum of ifInNUcastPkts for the subinterfaces of this interface.')
sumOfIfInDiscards = MibTableColumn((1, 3, 6, 1, 4, 1, 13191, 10, 3, 4, 7, 1, 1, 1, 4), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sumOfIfInDiscards.setStatus('current')
if mibBuilder.loadTexts: sumOfIfInDiscards.setDescription('The sum of ifInDiscards for the subinterfaces of this interface.')
sumOfIfInErrors = MibTableColumn((1, 3, 6, 1, 4, 1, 13191, 10, 3, 4, 7, 1, 1, 1, 5), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sumOfIfInErrors.setStatus('current')
if mibBuilder.loadTexts: sumOfIfInErrors.setDescription('The sum of ifInErrors for the subinterfaces of this interface.')
sumOfIfInUnknownProtos = MibTableColumn((1, 3, 6, 1, 4, 1, 13191, 10, 3, 4, 7, 1, 1, 1, 6), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sumOfIfInUnknownProtos.setStatus('current')
if mibBuilder.loadTexts: sumOfIfInUnknownProtos.setDescription('The sum of ifInUnknownProtos for the subinterfaces of this interface.')
sumOfIfOutOctets = MibTableColumn((1, 3, 6, 1, 4, 1, 13191, 10, 3, 4, 7, 1, 1, 1, 7), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sumOfIfOutOctets.setStatus('current')
if mibBuilder.loadTexts: sumOfIfOutOctets.setDescription('The sum of ifOutOctets for the subinterfaces of this interface.')
sumOfIfOutUcastPkts = MibTableColumn((1, 3, 6, 1, 4, 1, 13191, 10, 3, 4, 7, 1, 1, 1, 8), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sumOfIfOutUcastPkts.setStatus('current')
if mibBuilder.loadTexts: sumOfIfOutUcastPkts.setDescription('The sum of ifOutUcastPkts for the subinterfaces of this interface.')
sumOfIfOutNUcastPkts = MibTableColumn((1, 3, 6, 1, 4, 1, 13191, 10, 3, 4, 7, 1, 1, 1, 9), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sumOfIfOutNUcastPkts.setStatus('current')
if mibBuilder.loadTexts: sumOfIfOutNUcastPkts.setDescription('The sum of ifOutNUcastPkts for the subinterfaces of this interface.')
sumOfIfOutDiscards = MibTableColumn((1, 3, 6, 1, 4, 1, 13191, 10, 3, 4, 7, 1, 1, 1, 10), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sumOfIfOutDiscards.setStatus('current')
if mibBuilder.loadTexts: sumOfIfOutDiscards.setDescription('The sum of ifOutDiscards for the subinterfaces of this interface.')
sumOfIfOutErrors = MibTableColumn((1, 3, 6, 1, 4, 1, 13191, 10, 3, 4, 7, 1, 1, 1, 11), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sumOfIfOutErrors.setStatus('current')
if mibBuilder.loadTexts: sumOfIfOutErrors.setDescription('The sum of ifOutErrors for the subinterfaces of this interface.')
oacSumOfIfXTable = MibTable((1, 3, 6, 1, 4, 1, 13191, 10, 3, 4, 7, 1, 2), )
if mibBuilder.loadTexts: oacSumOfIfXTable.setStatus('current')
if mibBuilder.loadTexts: oacSumOfIfXTable.setDescription('The table representing the entriese of oacSumOfIfXTable')
oacSumOfIfXEntry = MibTableRow((1, 3, 6, 1, 4, 1, 13191, 10, 3, 4, 7, 1, 2, 1), ).setIndexNames((0, "IF-MIB", "ifIndex"))
if mibBuilder.loadTexts: oacSumOfIfXEntry.setStatus('current')
if mibBuilder.loadTexts: oacSumOfIfXEntry.setDescription('Defines an entry in the oacSumOfIfXTable.')
sumOfIfInMulticastPkts = MibTableColumn((1, 3, 6, 1, 4, 1, 13191, 10, 3, 4, 7, 1, 2, 1, 1), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sumOfIfInMulticastPkts.setStatus('current')
if mibBuilder.loadTexts: sumOfIfInMulticastPkts.setDescription('The sum of ifInMulticastPkts for the subinterfaces of this interface.')
sumOfIfInBroadcastPkts = MibTableColumn((1, 3, 6, 1, 4, 1, 13191, 10, 3, 4, 7, 1, 2, 1, 2), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sumOfIfInBroadcastPkts.setStatus('current')
if mibBuilder.loadTexts: sumOfIfInBroadcastPkts.setDescription('The sum ifInBroadcastPkts for the subinterfaces of this interface.')
sumOfIfOutMulticastPkts = MibTableColumn((1, 3, 6, 1, 4, 1, 13191, 10, 3, 4, 7, 1, 2, 1, 3), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sumOfIfOutMulticastPkts.setStatus('current')
if mibBuilder.loadTexts: sumOfIfOutMulticastPkts.setDescription('The sum of ifOutMulticastPkts for the subinterfaces of this interface.')
sumOfIfOutBroadcastPkts = MibTableColumn((1, 3, 6, 1, 4, 1, 13191, 10, 3, 4, 7, 1, 2, 1, 4), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sumOfIfOutBroadcastPkts.setStatus('current')
if mibBuilder.loadTexts: sumOfIfOutBroadcastPkts.setDescription('The sum of ifOutBroadcastPkts for the subinterfaces of this interface.')
sumOfIfHCInOctets = MibTableColumn((1, 3, 6, 1, 4, 1, 13191, 10, 3, 4, 7, 1, 2, 1, 5), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sumOfIfHCInOctets.setStatus('current')
if mibBuilder.loadTexts: sumOfIfHCInOctets.setDescription('The sum of ifHCInOctets for the subinterfaces of this interface.')
sumOfIfHCInUcastPkts = MibTableColumn((1, 3, 6, 1, 4, 1, 13191, 10, 3, 4, 7, 1, 2, 1, 6), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sumOfIfHCInUcastPkts.setStatus('current')
if mibBuilder.loadTexts: sumOfIfHCInUcastPkts.setDescription('The sum of ifHCInUcastPkts for the subinterfaces of this interface.')
sumOfIfHCInMulticastPkts = MibTableColumn((1, 3, 6, 1, 4, 1, 13191, 10, 3, 4, 7, 1, 2, 1, 7), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sumOfIfHCInMulticastPkts.setStatus('current')
if mibBuilder.loadTexts: sumOfIfHCInMulticastPkts.setDescription('The sum of ifHCInMulticastPkts for the subinterfaces of this interface.')
sumOfIfHCInBroadcastPkts = MibTableColumn((1, 3, 6, 1, 4, 1, 13191, 10, 3, 4, 7, 1, 2, 1, 8), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sumOfIfHCInBroadcastPkts.setStatus('current')
if mibBuilder.loadTexts: sumOfIfHCInBroadcastPkts.setDescription('The sum of ifHCInBroadcastPkts for the subinterfaces of this interface.')
sumOfIfHCOutOctets = MibTableColumn((1, 3, 6, 1, 4, 1, 13191, 10, 3, 4, 7, 1, 2, 1, 9), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sumOfIfHCOutOctets.setStatus('current')
if mibBuilder.loadTexts: sumOfIfHCOutOctets.setDescription('The sum of ifHCOutOctets for the subinterfaces of this interface.')
sumOfIfHCOutUcastPkts = MibTableColumn((1, 3, 6, 1, 4, 1, 13191, 10, 3, 4, 7, 1, 2, 1, 10), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sumOfIfHCOutUcastPkts.setStatus('current')
if mibBuilder.loadTexts: sumOfIfHCOutUcastPkts.setDescription('The sum of ifHCOutUcastPkts for the subinterfaces of this interface.')
sumOfIfHCOutMulticastPkts = MibTableColumn((1, 3, 6, 1, 4, 1, 13191, 10, 3, 4, 7, 1, 2, 1, 11), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sumOfIfHCOutMulticastPkts.setStatus('current')
if mibBuilder.loadTexts: sumOfIfHCOutMulticastPkts.setDescription('The sum of ifHCOutMulticastPkts for the subinterfaces of this interface.')
sumOfIfHCOutBroadcastPkts = MibTableColumn((1, 3, 6, 1, 4, 1, 13191, 10, 3, 4, 7, 1, 2, 1, 12), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sumOfIfHCOutBroadcastPkts.setStatus('current')
if mibBuilder.loadTexts: sumOfIfHCOutBroadcastPkts.setDescription('The sum of ifHCOutBroadcastPkts for the subinterfaces of this interface.')
mibBuilder.exportSymbols("ONEACCESS-SUMOF-MIB", sumOfIfHCOutOctets=sumOfIfHCOutOctets, PYSNMP_MODULE_ID=oacSumOfMIBModule, oacSumOfIfXTable=oacSumOfIfXTable, sumOfIfHCInUcastPkts=sumOfIfHCInUcastPkts, sumOfIfHCInMulticastPkts=sumOfIfHCInMulticastPkts, sumOfIfHCOutMulticastPkts=sumOfIfHCOutMulticastPkts, oacSumOfIfEntry=oacSumOfIfEntry, sumOfIfInBroadcastPkts=sumOfIfInBroadcastPkts, sumOfIfInNUcastPkts=sumOfIfInNUcastPkts, oacSumOfIfTable=oacSumOfIfTable, sumOfIfHCInBroadcastPkts=sumOfIfHCInBroadcastPkts, sumOfIfHCOutBroadcastPkts=sumOfIfHCOutBroadcastPkts, sumOfIfOutBroadcastPkts=sumOfIfOutBroadcastPkts, sumOfIfHCOutUcastPkts=sumOfIfHCOutUcastPkts, sumOfIfOutDiscards=sumOfIfOutDiscards, sumOfIfHCInOctets=sumOfIfHCInOctets, sumOfIfInErrors=sumOfIfInErrors, sumOfIfOutNUcastPkts=sumOfIfOutNUcastPkts, sumOfIfInUcastPkts=sumOfIfInUcastPkts, sumOfIfInDiscards=sumOfIfInDiscards, sumOfIfOutMulticastPkts=sumOfIfOutMulticastPkts, oacSumOfIfXEntry=oacSumOfIfXEntry, sumOfIfOutUcastPkts=sumOfIfOutUcastPkts, oacSumOfObjects=oacSumOfObjects, sumOfIfOutOctets=sumOfIfOutOctets, oacSumOfMIBModule=oacSumOfMIBModule, sumOfIfInMulticastPkts=sumOfIfInMulticastPkts, sumOfIfOutErrors=sumOfIfOutErrors, sumOfIfInUnknownProtos=sumOfIfInUnknownProtos, sumOfIfInOctets=sumOfIfInOctets)
