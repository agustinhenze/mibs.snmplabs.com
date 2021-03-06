#
# PySNMP MIB module XYLAN-MGMTSTN-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/XYLAN-MGMTSTN-MIB
# Produced by pysmi-0.3.4 at Wed May  1 15:45:13 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
ObjectIdentifier, Integer, OctetString = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "Integer", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
SingleValueConstraint, ConstraintsIntersection, ConstraintsUnion, ValueSizeConstraint, ValueRangeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "SingleValueConstraint", "ConstraintsIntersection", "ConstraintsUnion", "ValueSizeConstraint", "ValueRangeConstraint")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
ObjectIdentity, IpAddress, Unsigned32, Counter64, MibIdentifier, NotificationType, MibScalar, MibTable, MibTableRow, MibTableColumn, TimeTicks, ModuleIdentity, Counter32, iso, Gauge32, Bits, Integer32 = mibBuilder.importSymbols("SNMPv2-SMI", "ObjectIdentity", "IpAddress", "Unsigned32", "Counter64", "MibIdentifier", "NotificationType", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "TimeTicks", "ModuleIdentity", "Counter32", "iso", "Gauge32", "Bits", "Integer32")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
xylanTrapArch, = mibBuilder.importSymbols("XYLAN-BASE-MIB", "xylanTrapArch")
mgmtControl = MibIdentifier((1, 3, 6, 1, 4, 1, 800, 2, 5, 1))
trapBindings = MibIdentifier((1, 3, 6, 1, 4, 1, 800, 2, 5, 2))
trapTable = MibTable((1, 3, 6, 1, 4, 1, 800, 2, 5, 1, 1), )
if mibBuilder.loadTexts: trapTable.setStatus('mandatory')
if mibBuilder.loadTexts: trapTable.setDescription('A list of management stations.')
trapEntry = MibTableRow((1, 3, 6, 1, 4, 1, 800, 2, 5, 1, 1, 1), ).setIndexNames((0, "XYLAN-MGMTSTN-MIB", "stationIndex"))
if mibBuilder.loadTexts: trapEntry.setStatus('mandatory')
if mibBuilder.loadTexts: trapEntry.setDescription('A management station entry.')
stationIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 800, 2, 5, 1, 1, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 11))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: stationIndex.setStatus('mandatory')
if mibBuilder.loadTexts: stationIndex.setDescription('The entry index for a given row. A row create is done by specifying a row of 0 with the new row values.')
stationIP = MibTableColumn((1, 3, 6, 1, 4, 1, 800, 2, 5, 1, 1, 1, 2), IpAddress()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: stationIP.setStatus('mandatory')
if mibBuilder.loadTexts: stationIP.setDescription('The IP address of this management entity. A delete may be performed by specifying the current row index with the new IP of 0.')
stationPort = MibTableColumn((1, 3, 6, 1, 4, 1, 800, 2, 5, 1, 1, 1, 3), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 65535))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: stationPort.setStatus('mandatory')
if mibBuilder.loadTexts: stationPort.setDescription('The UDP port used by this management entity. This defaults to the SNMP-TRAP port 162')
stationCommunity = MibTableColumn((1, 3, 6, 1, 4, 1, 800, 2, 5, 1, 1, 1, 4), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 31))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: stationCommunity.setStatus('mandatory')
if mibBuilder.loadTexts: stationCommunity.setDescription('The community string used by this entity. Currently NOT implimented on a per NMS basis.')
stationTrapFlags = MibTableColumn((1, 3, 6, 1, 4, 1, 800, 2, 5, 1, 1, 1, 5), OctetString().subtype(subtypeSpec=ValueSizeConstraint(16, 16)).setFixedLength(16)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: stationTrapFlags.setStatus('mandatory')
if mibBuilder.loadTexts: stationTrapFlags.setDescription("The trap mask flags for this entity. Currently this is four unsigned ints. The default value is ALL traps enabled to this entity -> f's. The actual order of flag words sent is 0->3.... In the Xylan agent implimentation, Enable and SA are taken from the first two bits in the string.")
stationEnable = MibTableColumn((1, 3, 6, 1, 4, 1, 800, 2, 5, 1, 1, 1, 6), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: stationEnable.setStatus('mandatory')
if mibBuilder.loadTexts: stationEnable.setDescription('The enable flag for this NMS. if 1 traps are not sent to this station, if 2 trap are sent. 3 indicates that a row deletion is desired.')
stationSAPrivs = MibTableColumn((1, 3, 6, 1, 4, 1, 800, 2, 5, 1, 1, 1, 7), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: stationSAPrivs.setStatus('mandatory')
if mibBuilder.loadTexts: stationSAPrivs.setDescription("The SA priviledge flag for this NMS. If this is 2, this NMS can modify and delete any entry in the NMS table. Otherwise it is 1 and this station can modify/delete only it's own entry. NOTE: a station can't create a new entry for itself with the SA mode set.... (kinda defeats the SA doesn't it?).")
systemEventTrapNumber = MibScalar((1, 3, 6, 1, 4, 1, 800, 2, 5, 2, 1), Integer32())
if mibBuilder.loadTexts: systemEventTrapNumber.setStatus('mandatory')
if mibBuilder.loadTexts: systemEventTrapNumber.setDescription('This variable is bound to the systemEvent trap. It indicates which system resource is in short supply. 10 Unspecified log event 11 Log file full 12 Log file erased 20 Unspecified memory event 21 Memory shortage 30 Unsepcified CPU event 31 Long term CPU overload 32 Short term CPU overload 40 Unspecified ffs event 41 Attempt to write to full ffs 42 System/user directed purge 43 Removed imgs/cfgs 44 Exec file removed 45 Config file removed 46 Exec file updated 47 Config file updated 50 Unspecified chassis event 51 Module failed to init 52 Module failed to load 53 Module startup failed 54 Module failed 55 Driver failed ')
systemEventTrapString = MibScalar((1, 3, 6, 1, 4, 1, 800, 2, 5, 2, 2), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 63)))
if mibBuilder.loadTexts: systemEventTrapString.setStatus('mandatory')
if mibBuilder.loadTexts: systemEventTrapString.setDescription('This variable is bound to the systemEvent trap. If it is present it will furthor clarify the specific system trap.')
mibBuilder.exportSymbols("XYLAN-MGMTSTN-MIB", stationIndex=stationIndex, systemEventTrapNumber=systemEventTrapNumber, stationPort=stationPort, stationCommunity=stationCommunity, stationEnable=stationEnable, stationIP=stationIP, trapBindings=trapBindings, trapEntry=trapEntry, stationSAPrivs=stationSAPrivs, mgmtControl=mgmtControl, stationTrapFlags=stationTrapFlags, trapTable=trapTable, systemEventTrapString=systemEventTrapString)
