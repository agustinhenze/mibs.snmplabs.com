#
# PySNMP MIB module Wellfleet-ASYNC-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/Wellfleet-ASYNC-MIB
# Produced by pysmi-0.3.4 at Wed May  1 15:39:26 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
Integer, OctetString, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "Integer", "OctetString", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
SingleValueConstraint, ConstraintsUnion, ConstraintsIntersection, ValueSizeConstraint, ValueRangeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "SingleValueConstraint", "ConstraintsUnion", "ConstraintsIntersection", "ValueSizeConstraint", "ValueRangeConstraint")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
IpAddress, MibIdentifier, ObjectIdentity, Unsigned32, Bits, Counter64, MibScalar, MibTable, MibTableRow, MibTableColumn, Opaque, mgmt, ModuleIdentity, enterprises, Gauge32, TimeTicks, NotificationType, Counter32, iso, Integer32, NotificationType, mib_2 = mibBuilder.importSymbols("SNMPv2-SMI", "IpAddress", "MibIdentifier", "ObjectIdentity", "Unsigned32", "Bits", "Counter64", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Opaque", "mgmt", "ModuleIdentity", "enterprises", "Gauge32", "TimeTicks", "NotificationType", "Counter32", "iso", "Integer32", "NotificationType", "mib-2")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
wfLine, = mibBuilder.importSymbols("Wellfleet-COMMON-MIB", "wfLine")
wfAsyncTable = MibTable((1, 3, 6, 1, 4, 1, 18, 3, 4, 3), )
if mibBuilder.loadTexts: wfAsyncTable.setStatus('mandatory')
if mibBuilder.loadTexts: wfAsyncTable.setDescription('ASYNC line record')
wfAsyncEntry = MibTableRow((1, 3, 6, 1, 4, 1, 18, 3, 4, 3, 1), ).setIndexNames((0, "Wellfleet-ASYNC-MIB", "wfAsyncSlot"), (0, "Wellfleet-ASYNC-MIB", "wfAsyncConnector"))
if mibBuilder.loadTexts: wfAsyncEntry.setStatus('mandatory')
if mibBuilder.loadTexts: wfAsyncEntry.setDescription('An entry in the ASYNC table')
wfAsyncDelete = MibTableColumn((1, 3, 6, 1, 4, 1, 18, 3, 4, 3, 1, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("created", 1), ("deleted", 2))).clone('created')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: wfAsyncDelete.setStatus('mandatory')
if mibBuilder.loadTexts: wfAsyncDelete.setDescription('Create/Delete parameter')
wfAsyncDisable = MibTableColumn((1, 3, 6, 1, 4, 1, 18, 3, 4, 3, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enabled", 1), ("disabled", 2))).clone('enabled')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: wfAsyncDisable.setStatus('mandatory')
if mibBuilder.loadTexts: wfAsyncDisable.setDescription('Enable/Disable parameter')
wfAsyncState = MibTableColumn((1, 3, 6, 1, 4, 1, 18, 3, 4, 3, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5))).clone(namedValues=NamedValues(("up", 1), ("down", 2), ("init", 3), ("notpresent", 4), ("dsrwait", 5))).clone('notpresent')).setMaxAccess("readonly")
if mibBuilder.loadTexts: wfAsyncState.setStatus('mandatory')
if mibBuilder.loadTexts: wfAsyncState.setDescription('Line Driver state variable, Not Present, DSR Wait, Init, Down, Up')
wfAsyncSlot = MibTableColumn((1, 3, 6, 1, 4, 1, 18, 3, 4, 3, 1, 4), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: wfAsyncSlot.setStatus('mandatory')
if mibBuilder.loadTexts: wfAsyncSlot.setDescription('Instance ID Slot, filled in by driver')
wfAsyncConnector = MibTableColumn((1, 3, 6, 1, 4, 1, 18, 3, 4, 3, 1, 5), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))).clone(namedValues=NamedValues(("one", 1), ("two", 2), ("three", 3), ("four", 4)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: wfAsyncConnector.setStatus('mandatory')
if mibBuilder.loadTexts: wfAsyncConnector.setDescription("Instance ID Connector, filled in by driver. For the ASN this attribute is an encoded value and is equal to 'module'*10 + 'connector'. Where 'module' is defined in attribute 86 and 'connector' is defined in attribute 78 of this table. For non-ASN platforms this attribute is the physical connector number on the slot.")
wfAsyncCct = MibTableColumn((1, 3, 6, 1, 4, 1, 18, 3, 4, 3, 1, 6), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 1023))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: wfAsyncCct.setStatus('mandatory')
if mibBuilder.loadTexts: wfAsyncCct.setDescription('CCT number for this line instance')
wfAsyncMtu = MibTableColumn((1, 3, 6, 1, 4, 1, 18, 3, 4, 3, 1, 7), Integer32().subtype(subtypeSpec=ValueRangeConstraint(3, 1580)).clone(1000)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: wfAsyncMtu.setStatus('mandatory')
if mibBuilder.loadTexts: wfAsyncMtu.setDescription('MTU parameter, this is buffer size for ASYNC media, fixed')
wfAsyncMadr = MibTableColumn((1, 3, 6, 1, 4, 1, 18, 3, 4, 3, 1, 8), OctetString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: wfAsyncMadr.setStatus('mandatory')
if mibBuilder.loadTexts: wfAsyncMadr.setDescription('Line MAC address, fixed - line driver fills in from the 48 bit address stored in the serial number prom for this connector.')
wfAsyncStartProtocol = MibTableColumn((1, 3, 6, 1, 4, 1, 18, 3, 4, 3, 1, 9), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("loop", 1), ("originate", 2), ("answer", 3))).clone('answer')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: wfAsyncStartProtocol.setStatus('mandatory')
if mibBuilder.loadTexts: wfAsyncStartProtocol.setDescription('Start protocol selection is provided via this parameter. The supported protocols can be selected per interface.')
wfAsyncRxOctets = MibTableColumn((1, 3, 6, 1, 4, 1, 18, 3, 4, 3, 1, 10), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: wfAsyncRxOctets.setStatus('mandatory')
if mibBuilder.loadTexts: wfAsyncRxOctets.setDescription('Number of octets received without error')
wfAsyncTxOctets = MibTableColumn((1, 3, 6, 1, 4, 1, 18, 3, 4, 3, 1, 11), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: wfAsyncTxOctets.setStatus('mandatory')
if mibBuilder.loadTexts: wfAsyncTxOctets.setDescription('Number of octets transmitted without error')
wfAsyncRxErrors = MibTableColumn((1, 3, 6, 1, 4, 1, 18, 3, 4, 3, 1, 12), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: wfAsyncRxErrors.setStatus('mandatory')
if mibBuilder.loadTexts: wfAsyncRxErrors.setDescription('Number of receive errors')
wfAsyncTxErrors = MibTableColumn((1, 3, 6, 1, 4, 1, 18, 3, 4, 3, 1, 13), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: wfAsyncTxErrors.setStatus('mandatory')
if mibBuilder.loadTexts: wfAsyncTxErrors.setDescription('Number of transmission errors')
wfAsyncRxLackRescs = MibTableColumn((1, 3, 6, 1, 4, 1, 18, 3, 4, 3, 1, 14), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: wfAsyncRxLackRescs.setStatus('mandatory')
if mibBuilder.loadTexts: wfAsyncRxLackRescs.setDescription('Number of Rx frames dropped due to lack of buffer resources')
wfAsyncTxLackRescs = MibTableColumn((1, 3, 6, 1, 4, 1, 18, 3, 4, 3, 1, 15), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: wfAsyncTxLackRescs.setStatus('mandatory')
if mibBuilder.loadTexts: wfAsyncTxLackRescs.setDescription("Number of frames clipped in driver's transmit routine due to transmit congestion.")
wfAsyncTxUnderFlows = MibTableColumn((1, 3, 6, 1, 4, 1, 18, 3, 4, 3, 1, 16), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: wfAsyncTxUnderFlows.setStatus('mandatory')
if mibBuilder.loadTexts: wfAsyncTxUnderFlows.setDescription('Number of transmission underflows, device FIFO went empty before next DMA request was granted.')
wfAsyncTxRejects = MibTableColumn((1, 3, 6, 1, 4, 1, 18, 3, 4, 3, 1, 17), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: wfAsyncTxRejects.setStatus('mandatory')
if mibBuilder.loadTexts: wfAsyncTxRejects.setDescription('Number of reject frames which were transmitted')
wfAsyncRxRejects = MibTableColumn((1, 3, 6, 1, 4, 1, 18, 3, 4, 3, 1, 18), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: wfAsyncRxRejects.setStatus('mandatory')
if mibBuilder.loadTexts: wfAsyncRxRejects.setDescription('Number of reject frames which were received')
wfAsyncRxOverFlows = MibTableColumn((1, 3, 6, 1, 4, 1, 18, 3, 4, 3, 1, 19), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: wfAsyncRxOverFlows.setStatus('mandatory')
if mibBuilder.loadTexts: wfAsyncRxOverFlows.setDescription('Number of receive overflows, device FIFO overflowed before next DMA cycle granted. No buffer resources available.')
wfAsyncRxBadOctets = MibTableColumn((1, 3, 6, 1, 4, 1, 18, 3, 4, 3, 1, 20), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: wfAsyncRxBadOctets.setStatus('mandatory')
if mibBuilder.loadTexts: wfAsyncRxBadOctets.setDescription('Number of bad receive frames, caused by FCS errors or non octet aligned.')
wfAsyncRxRunts = MibTableColumn((1, 3, 6, 1, 4, 1, 18, 3, 4, 3, 1, 21), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: wfAsyncRxRunts.setStatus('mandatory')
if mibBuilder.loadTexts: wfAsyncRxRunts.setDescription('Number of runt frames received')
wfAsyncTxQueueLength = MibTableColumn((1, 3, 6, 1, 4, 1, 18, 3, 4, 3, 1, 22), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: wfAsyncTxQueueLength.setStatus('mandatory')
if mibBuilder.loadTexts: wfAsyncTxQueueLength.setDescription('Current Transmit Queue Length.')
wfAsyncRxQueueLength = MibTableColumn((1, 3, 6, 1, 4, 1, 18, 3, 4, 3, 1, 23), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: wfAsyncRxQueueLength.setStatus('mandatory')
if mibBuilder.loadTexts: wfAsyncRxQueueLength.setDescription('Current Receive Queue Length.')
wfAsyncRxReplenMisses = MibTableColumn((1, 3, 6, 1, 4, 1, 18, 3, 4, 3, 1, 24), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: wfAsyncRxReplenMisses.setStatus('mandatory')
if mibBuilder.loadTexts: wfAsyncRxReplenMisses.setDescription('Number of packet buffer misses while attempting to replenish driver receive ring.')
wfAsyncLineNumber = MibTableColumn((1, 3, 6, 1, 4, 1, 18, 3, 4, 3, 1, 25), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: wfAsyncLineNumber.setStatus('mandatory')
if mibBuilder.loadTexts: wfAsyncLineNumber.setDescription('line number for this line instance')
wfAsyncRemoteAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 18, 3, 4, 3, 1, 26), IpAddress()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: wfAsyncRemoteAddress.setStatus('mandatory')
if mibBuilder.loadTexts: wfAsyncRemoteAddress.setDescription('Remote TCP host IP address')
wfAsyncRemotePort = MibTableColumn((1, 3, 6, 1, 4, 1, 18, 3, 4, 3, 1, 27), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(7))).clone(namedValues=NamedValues(("port", 7))).clone('port')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: wfAsyncRemotePort.setStatus('mandatory')
if mibBuilder.loadTexts: wfAsyncRemotePort.setDescription('Remote port for TCP connection')
wfAsyncLocalPort = MibTableColumn((1, 3, 6, 1, 4, 1, 18, 3, 4, 3, 1, 28), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(2100))).clone(namedValues=NamedValues(("default", 2100))).clone('default')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: wfAsyncLocalPort.setStatus('mandatory')
if mibBuilder.loadTexts: wfAsyncLocalPort.setDescription('Local port for TCP connection')
wfAsyncBaud = MibTableColumn((1, 3, 6, 1, 4, 1, 18, 3, 4, 3, 1, 29), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(300, 1200, 2400, 4800, 9600, 19200))).clone(namedValues=NamedValues(("r300", 300), ("r1200", 1200), ("r2400", 2400), ("r4800", 4800), ("r9600", 9600), ("r19200", 19200))).clone('r9600')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: wfAsyncBaud.setStatus('mandatory')
if mibBuilder.loadTexts: wfAsyncBaud.setDescription('Async line speed')
wfAsyncIdleTimer = MibTableColumn((1, 3, 6, 1, 4, 1, 18, 3, 4, 3, 1, 30), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 300)).clone(20)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: wfAsyncIdleTimer.setStatus('mandatory')
if mibBuilder.loadTexts: wfAsyncIdleTimer.setDescription('Async line Idle timer')
wfAsyncRxWindow = MibTableColumn((1, 3, 6, 1, 4, 1, 18, 3, 4, 3, 1, 31), Integer32().subtype(subtypeSpec=ValueRangeConstraint(512, 65535)).clone(4096)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: wfAsyncRxWindow.setStatus('mandatory')
if mibBuilder.loadTexts: wfAsyncRxWindow.setDescription('Configured TCP receive window')
wfAsyncMinRxWindows = MibTableColumn((1, 3, 6, 1, 4, 1, 18, 3, 4, 3, 1, 32), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: wfAsyncMinRxWindows.setStatus('mandatory')
if mibBuilder.loadTexts: wfAsyncMinRxWindows.setDescription('Low-water mark of receive window (for latest connection)')
wfASyncSecTxQmaxs = MibTableColumn((1, 3, 6, 1, 4, 1, 18, 3, 4, 3, 1, 33), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: wfASyncSecTxQmaxs.setStatus('mandatory')
if mibBuilder.loadTexts: wfASyncSecTxQmaxs.setDescription('secondary TX queue hi-water mark (for this connection)')
wfASyncSecTxQlens = MibTableColumn((1, 3, 6, 1, 4, 1, 18, 3, 4, 3, 1, 34), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: wfASyncSecTxQlens.setStatus('mandatory')
if mibBuilder.loadTexts: wfASyncSecTxQlens.setDescription('secondary TX queue present value')
wfAsyncTCPKeepalive = MibTableColumn((1, 3, 6, 1, 4, 1, 18, 3, 4, 3, 1, 35), Integer32().subtype(subtypeSpec=ValueRangeConstraint(3, 180)).clone(8)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: wfAsyncTCPKeepalive.setStatus('mandatory')
if mibBuilder.loadTexts: wfAsyncTCPKeepalive.setDescription('Keepalive timer. A keepalive (probe) message is sent out if there is no activity in this number of seconds.')
wfAsyncTCPInactivityLimit = MibTableColumn((1, 3, 6, 1, 4, 1, 18, 3, 4, 3, 1, 36), Integer32().subtype(subtypeSpec=ValueRangeConstraint(-65536, 65535)).clone(300)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: wfAsyncTCPInactivityLimit.setStatus('mandatory')
if mibBuilder.loadTexts: wfAsyncTCPInactivityLimit.setDescription('Inactivity limit. Connection (eligable for) reset if no activity in this number of seconds.')
wfAsyncCfgTxQueueLength = MibTableColumn((1, 3, 6, 1, 4, 1, 18, 3, 4, 3, 1, 37), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 255))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: wfAsyncCfgTxQueueLength.setStatus('mandatory')
if mibBuilder.loadTexts: wfAsyncCfgTxQueueLength.setDescription('Configured Transmit Queue Length. Values other than zero over-ride the router selected values. A value of zero has a special meaning. Zero causes router based default values to be used. Values larger than the compiled ring size are truncated to the compiled ring size. ')
wfAsyncCfgRxQueueLength = MibTableColumn((1, 3, 6, 1, 4, 1, 18, 3, 4, 3, 1, 38), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 255))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: wfAsyncCfgRxQueueLength.setStatus('mandatory')
if mibBuilder.loadTexts: wfAsyncCfgRxQueueLength.setDescription('Configured Receive Queue Length. Values other than zero over-ride the router selected values. A value of zero has a special meaning. Zero causes router based default values to be used. Values larger than the compiled ring size are truncated to the compiled ring size. ')
mibBuilder.exportSymbols("Wellfleet-ASYNC-MIB", wfAsyncDisable=wfAsyncDisable, wfAsyncRxOverFlows=wfAsyncRxOverFlows, wfAsyncConnector=wfAsyncConnector, wfAsyncRxReplenMisses=wfAsyncRxReplenMisses, wfAsyncLocalPort=wfAsyncLocalPort, wfAsyncBaud=wfAsyncBaud, wfAsyncMtu=wfAsyncMtu, wfAsyncRxRejects=wfAsyncRxRejects, wfAsyncDelete=wfAsyncDelete, wfAsyncTable=wfAsyncTable, wfAsyncStartProtocol=wfAsyncStartProtocol, wfAsyncRxQueueLength=wfAsyncRxQueueLength, wfAsyncTCPKeepalive=wfAsyncTCPKeepalive, wfAsyncMadr=wfAsyncMadr, wfAsyncTxOctets=wfAsyncTxOctets, wfAsyncLineNumber=wfAsyncLineNumber, wfAsyncRxBadOctets=wfAsyncRxBadOctets, wfAsyncRxWindow=wfAsyncRxWindow, wfAsyncRxLackRescs=wfAsyncRxLackRescs, wfAsyncTxLackRescs=wfAsyncTxLackRescs, wfAsyncState=wfAsyncState, wfAsyncRxRunts=wfAsyncRxRunts, wfASyncSecTxQlens=wfASyncSecTxQlens, wfAsyncEntry=wfAsyncEntry, wfAsyncRxErrors=wfAsyncRxErrors, wfAsyncMinRxWindows=wfAsyncMinRxWindows, wfAsyncRxOctets=wfAsyncRxOctets, wfAsyncRemoteAddress=wfAsyncRemoteAddress, wfAsyncCct=wfAsyncCct, wfAsyncCfgRxQueueLength=wfAsyncCfgRxQueueLength, wfAsyncTxUnderFlows=wfAsyncTxUnderFlows, wfASyncSecTxQmaxs=wfASyncSecTxQmaxs, wfAsyncSlot=wfAsyncSlot, wfAsyncRemotePort=wfAsyncRemotePort, wfAsyncIdleTimer=wfAsyncIdleTimer, wfAsyncTxQueueLength=wfAsyncTxQueueLength, wfAsyncCfgTxQueueLength=wfAsyncCfgTxQueueLength, wfAsyncTxErrors=wfAsyncTxErrors, wfAsyncTxRejects=wfAsyncTxRejects, wfAsyncTCPInactivityLimit=wfAsyncTCPInactivityLimit)
