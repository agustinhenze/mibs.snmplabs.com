#
# PySNMP MIB module Wellfleet-TNC-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/Wellfleet-TNC-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 21:35:30 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
Integer, OctetString, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "Integer", "OctetString", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsUnion, ValueRangeConstraint, SingleValueConstraint, ValueSizeConstraint, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "ValueRangeConstraint", "SingleValueConstraint", "ValueSizeConstraint", "ConstraintsIntersection")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
iso, IpAddress, ModuleIdentity, ObjectIdentity, Unsigned32, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter64, Bits, Gauge32, MibIdentifier, Counter32, Integer32, TimeTicks, NotificationType = mibBuilder.importSymbols("SNMPv2-SMI", "iso", "IpAddress", "ModuleIdentity", "ObjectIdentity", "Unsigned32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter64", "Bits", "Gauge32", "MibIdentifier", "Counter32", "Integer32", "TimeTicks", "NotificationType")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
wfTelnetGroup, = mibBuilder.importSymbols("Wellfleet-COMMON-MIB", "wfTelnetGroup")
wfTelnetClient = MibIdentifier((1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 7, 2))
wfTelnetClientDelete = MibScalar((1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 7, 2, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("created", 1), ("deleted", 2))).clone('created')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: wfTelnetClientDelete.setStatus('mandatory')
wfTelnetClientDisable = MibScalar((1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 7, 2, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enabled", 1), ("disabled", 2))).clone('enabled')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: wfTelnetClientDisable.setStatus('mandatory')
wfTelnetClientDebug = MibScalar((1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 7, 2, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("on", 1), ("off", 2))).clone('off')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: wfTelnetClientDebug.setStatus('mandatory')
wfTelnetClientRemotePort = MibScalar((1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 7, 2, 4), Integer32().clone(23)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: wfTelnetClientRemotePort.setStatus('mandatory')
wfTelnetClientPrompt = MibScalar((1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 7, 2, 5), DisplayString()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: wfTelnetClientPrompt.setStatus('mandatory')
wfTelnetClientActiveSessions = MibScalar((1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 7, 2, 6), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: wfTelnetClientActiveSessions.setStatus('mandatory')
wfTelnetClientTotalSessions = MibScalar((1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 7, 2, 7), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: wfTelnetClientTotalSessions.setStatus('mandatory')
mibBuilder.exportSymbols("Wellfleet-TNC-MIB", wfTelnetClientDebug=wfTelnetClientDebug, wfTelnetClientDisable=wfTelnetClientDisable, wfTelnetClientDelete=wfTelnetClientDelete, wfTelnetClient=wfTelnetClient, wfTelnetClientRemotePort=wfTelnetClientRemotePort, wfTelnetClientActiveSessions=wfTelnetClientActiveSessions, wfTelnetClientTotalSessions=wfTelnetClientTotalSessions, wfTelnetClientPrompt=wfTelnetClientPrompt)