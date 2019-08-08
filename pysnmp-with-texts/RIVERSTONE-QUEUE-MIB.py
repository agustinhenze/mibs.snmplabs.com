#
# PySNMP MIB module RIVERSTONE-QUEUE-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/RIVERSTONE-QUEUE-MIB
# Produced by pysmi-0.3.4 at Wed May  1 14:57:36 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
Integer, OctetString, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "Integer", "OctetString", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, ConstraintsIntersection, ValueSizeConstraint, SingleValueConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "ConstraintsIntersection", "ValueSizeConstraint", "SingleValueConstraint", "ConstraintsUnion")
ifIndex, = mibBuilder.importSymbols("IF-MIB", "ifIndex")
riverstoneMibs, = mibBuilder.importSymbols("RIVERSTONE-SMI-MIB", "riverstoneMibs")
RsDiscardPolicy, = mibBuilder.importSymbols("RIVERSTONE-TC-MIB", "RsDiscardPolicy")
SnmpAdminString, = mibBuilder.importSymbols("SNMP-FRAMEWORK-MIB", "SnmpAdminString")
NotificationGroup, ObjectGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ObjectGroup", "ModuleCompliance")
MibIdentifier, Counter32, iso, Counter64, Unsigned32, ModuleIdentity, ObjectIdentity, NotificationType, Gauge32, TimeTicks, Integer32, IpAddress, MibScalar, MibTable, MibTableRow, MibTableColumn, Bits = mibBuilder.importSymbols("SNMPv2-SMI", "MibIdentifier", "Counter32", "iso", "Counter64", "Unsigned32", "ModuleIdentity", "ObjectIdentity", "NotificationType", "Gauge32", "TimeTicks", "Integer32", "IpAddress", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Bits")
TextualConvention, TimeStamp, DisplayString, TruthValue = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "TimeStamp", "DisplayString", "TruthValue")
rsQueueMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 5567, 2, 70))
rsQueueMIB.setRevisions(('2002-06-12 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: rsQueueMIB.setRevisionsDescriptions(('Initial version.',))
if mibBuilder.loadTexts: rsQueueMIB.setLastUpdated('200206120000Z')
if mibBuilder.loadTexts: rsQueueMIB.setOrganization('Riverstone Networks, Inc')
if mibBuilder.loadTexts: rsQueueMIB.setContactInfo('Riverstone Networks Customer Service Postal: Riverstone Networks, Inc 5200 Great America Parkway Santa Clara CA 95054 USA PHONE:+1 408.878.6500 EMAIL: nms-eng@riverstonenet.com WEB: http://www.riverstonenet.com')
if mibBuilder.loadTexts: rsQueueMIB.setDescription('This MIB module represents information on each of the queues for each port.')
class IndexInteger(TextualConvention, Unsigned32):
    description = 'An integer which may be used as a table index.'
    status = 'current'
    displayHint = 'd'
    subtypeSpec = Unsigned32.subtypeSpec + ValueRangeConstraint(1, 4294967295)

rsQueueMIBObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 5567, 2, 70, 1))
rsQueuePropertiesTable = MibTable((1, 3, 6, 1, 4, 1, 5567, 2, 70, 1, 1), )
if mibBuilder.loadTexts: rsQueuePropertiesTable.setStatus('current')
if mibBuilder.loadTexts: rsQueuePropertiesTable.setDescription('This table contains descriptions of different queues. It is used as a reference table by rsQueueStatsTable.')
rsQueuePropertiesEntry = MibTableRow((1, 3, 6, 1, 4, 1, 5567, 2, 70, 1, 1, 1), ).setIndexNames((0, "RIVERSTONE-QUEUE-MIB", "rsQueueId"))
if mibBuilder.loadTexts: rsQueuePropertiesEntry.setStatus('current')
if mibBuilder.loadTexts: rsQueuePropertiesEntry.setDescription('This entry represents a queue and its properties. It is indexed by a natural number.')
rsQueueId = MibTableColumn((1, 3, 6, 1, 4, 1, 5567, 2, 70, 1, 1, 1, 1), IndexInteger())
if mibBuilder.loadTexts: rsQueueId.setStatus('current')
if mibBuilder.loadTexts: rsQueueId.setDescription('An index that enumerates the number of queue entries.')
rsQueueName = MibTableColumn((1, 3, 6, 1, 4, 1, 5567, 2, 70, 1, 1, 1, 2), SnmpAdminString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rsQueueName.setStatus('current')
if mibBuilder.loadTexts: rsQueueName.setDescription('The name of the queue. For example, on the RS platform, the four queue names are control, high, medium, and low.')
rsQueueDescr = MibTableColumn((1, 3, 6, 1, 4, 1, 5567, 2, 70, 1, 1, 1, 3), SnmpAdminString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rsQueueDescr.setStatus('current')
if mibBuilder.loadTexts: rsQueueDescr.setDescription('A more detailed description of the functionality of the queue.')
rsQueueDiscardPolicy = MibTableColumn((1, 3, 6, 1, 4, 1, 5567, 2, 70, 1, 1, 1, 4), RsDiscardPolicy()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rsQueueDiscardPolicy.setStatus('current')
if mibBuilder.loadTexts: rsQueueDiscardPolicy.setDescription('The type of policy used by the queue to drop a frame.')
rsQueueMaxCapacity = MibTableColumn((1, 3, 6, 1, 4, 1, 5567, 2, 70, 1, 1, 1, 6), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rsQueueMaxCapacity.setStatus('current')
if mibBuilder.loadTexts: rsQueueMaxCapacity.setDescription('The max number of frames the queue can contain.')
rsQueueStatsTable = MibTable((1, 3, 6, 1, 4, 1, 5567, 2, 70, 1, 2), )
if mibBuilder.loadTexts: rsQueueStatsTable.setStatus('current')
if mibBuilder.loadTexts: rsQueueStatsTable.setDescription('This table contains stats per queue for each physical interface.')
rsQueueStatsEntry = MibTableRow((1, 3, 6, 1, 4, 1, 5567, 2, 70, 1, 2, 1), ).setIndexNames((0, "IF-MIB", "ifIndex"), (0, "RIVERSTONE-QUEUE-MIB", "rsQueueId"))
if mibBuilder.loadTexts: rsQueueStatsEntry.setStatus('current')
if mibBuilder.loadTexts: rsQueueStatsEntry.setDescription('The stats per queue for each physical interface.')
rsQueueStatsLastCapChange = MibTableColumn((1, 3, 6, 1, 4, 1, 5567, 2, 70, 1, 2, 1, 1), TimeStamp()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rsQueueStatsLastCapChange.setStatus('current')
if mibBuilder.loadTexts: rsQueueStatsLastCapChange.setDescription('The value of sysUpTime at the time when the port capability changed. As a result of this change, the application need to restart its counter collection. For example, the card may have been hotswapped out and replaced by another card.')
rsQueueStatsValid = MibTableColumn((1, 3, 6, 1, 4, 1, 5567, 2, 70, 1, 2, 1, 2), Bits().clone(namedValues=NamedValues(("validBytes", 0), ("validFrames", 1), ("validDiscards", 2), ("validHCBytes", 3), ("validHCFrames", 4)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: rsQueueStatsValid.setStatus('current')
if mibBuilder.loadTexts: rsQueueStatsValid.setDescription('The current state of each counter in this table. Each bit indicate the validity of a counter. Some queues may not support every counter in the table.')
rsQueueBytes = MibTableColumn((1, 3, 6, 1, 4, 1, 5567, 2, 70, 1, 2, 1, 101), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rsQueueBytes.setStatus('current')
if mibBuilder.loadTexts: rsQueueBytes.setDescription('The number of bytes that have passed through this priority queue on this port.')
rsQueueFrames = MibTableColumn((1, 3, 6, 1, 4, 1, 5567, 2, 70, 1, 2, 1, 102), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rsQueueFrames.setStatus('current')
if mibBuilder.loadTexts: rsQueueFrames.setDescription('The number of frames that have passed through this priority queue on this port.')
rsQueueDiscards = MibTableColumn((1, 3, 6, 1, 4, 1, 5567, 2, 70, 1, 2, 1, 103), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rsQueueDiscards.setStatus('current')
if mibBuilder.loadTexts: rsQueueDiscards.setDescription('The number of frames into this queue that were discarded because the queue was full.')
rsQueueHCBytes = MibTableColumn((1, 3, 6, 1, 4, 1, 5567, 2, 70, 1, 2, 1, 201), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rsQueueHCBytes.setStatus('current')
if mibBuilder.loadTexts: rsQueueHCBytes.setDescription('The number of bytes stored in a 64 bit counter that have passed through this priority queue on this port.')
rsQueueHCFrames = MibTableColumn((1, 3, 6, 1, 4, 1, 5567, 2, 70, 1, 2, 1, 202), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rsQueueHCFrames.setStatus('current')
if mibBuilder.loadTexts: rsQueueHCFrames.setDescription('The number of frames stored in a 64 bit counter that have passed through this priority queue on this port.')
rsQueueConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 5567, 2, 70, 2))
rsQueueCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 5567, 2, 70, 2, 1))
rsQueueGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 5567, 2, 70, 2, 2))
rsQueueCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 5567, 2, 70, 2, 1, 1)).setObjects(("RIVERSTONE-QUEUE-MIB", "rsQueuePropertiesGroup"), ("RIVERSTONE-QUEUE-MIB", "rsQueueStatsGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    rsQueueCompliance = rsQueueCompliance.setStatus('current')
if mibBuilder.loadTexts: rsQueueCompliance.setDescription('The compliance statement for RIVERSTONE-STATS-MIB.')
rsQueuePropertiesGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 5567, 2, 70, 2, 2, 1)).setObjects(("RIVERSTONE-QUEUE-MIB", "rsQueueName"), ("RIVERSTONE-QUEUE-MIB", "rsQueueDescr"), ("RIVERSTONE-QUEUE-MIB", "rsQueueDiscardPolicy"), ("RIVERSTONE-QUEUE-MIB", "rsQueueMaxCapacity"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    rsQueuePropertiesGroup = rsQueuePropertiesGroup.setStatus('current')
if mibBuilder.loadTexts: rsQueuePropertiesGroup.setDescription('The collection of objects used to represent properties of a queue.')
rsQueueStatsGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 5567, 2, 70, 2, 2, 2)).setObjects(("RIVERSTONE-QUEUE-MIB", "rsQueueStatsLastCapChange"), ("RIVERSTONE-QUEUE-MIB", "rsQueueStatsValid"), ("RIVERSTONE-QUEUE-MIB", "rsQueueBytes"), ("RIVERSTONE-QUEUE-MIB", "rsQueueFrames"), ("RIVERSTONE-QUEUE-MIB", "rsQueueDiscards"), ("RIVERSTONE-QUEUE-MIB", "rsQueueHCBytes"), ("RIVERSTONE-QUEUE-MIB", "rsQueueHCFrames"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    rsQueueStatsGroup = rsQueueStatsGroup.setStatus('current')
if mibBuilder.loadTexts: rsQueueStatsGroup.setDescription('The collection of objects used to represent the queue stats.')
mibBuilder.exportSymbols("RIVERSTONE-QUEUE-MIB", rsQueueDiscards=rsQueueDiscards, rsQueuePropertiesGroup=rsQueuePropertiesGroup, rsQueueId=rsQueueId, rsQueueDiscardPolicy=rsQueueDiscardPolicy, rsQueueFrames=rsQueueFrames, rsQueueCompliance=rsQueueCompliance, IndexInteger=IndexInteger, rsQueueStatsEntry=rsQueueStatsEntry, rsQueueHCFrames=rsQueueHCFrames, rsQueueMIB=rsQueueMIB, rsQueueStatsGroup=rsQueueStatsGroup, rsQueueCompliances=rsQueueCompliances, rsQueueName=rsQueueName, rsQueuePropertiesTable=rsQueuePropertiesTable, rsQueueGroups=rsQueueGroups, rsQueuePropertiesEntry=rsQueuePropertiesEntry, rsQueueStatsLastCapChange=rsQueueStatsLastCapChange, rsQueueConformance=rsQueueConformance, rsQueueStatsTable=rsQueueStatsTable, rsQueueDescr=rsQueueDescr, rsQueueBytes=rsQueueBytes, rsQueueMIBObjects=rsQueueMIBObjects, rsQueueHCBytes=rsQueueHCBytes, rsQueueStatsValid=rsQueueStatsValid, rsQueueMaxCapacity=rsQueueMaxCapacity, PYSNMP_MODULE_ID=rsQueueMIB)