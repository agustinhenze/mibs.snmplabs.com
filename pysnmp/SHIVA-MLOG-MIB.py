#
# PySNMP MIB module SHIVA-MLOG-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/SHIVA-MLOG-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 20:55:26 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
OctetString, Integer, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "OctetString", "Integer", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, ValueSizeConstraint, SingleValueConstraint, ConstraintsUnion, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "ValueSizeConstraint", "SingleValueConstraint", "ConstraintsUnion", "ConstraintsIntersection")
messageLog, = mibBuilder.importSymbols("SHIVA-MIB", "messageLog")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
IpAddress, Unsigned32, iso, ObjectIdentity, Bits, Counter64, Gauge32, NotificationType, ModuleIdentity, Integer32, MibScalar, MibTable, MibTableRow, MibTableColumn, TimeTicks, MibIdentifier, Counter32 = mibBuilder.importSymbols("SNMPv2-SMI", "IpAddress", "Unsigned32", "iso", "ObjectIdentity", "Bits", "Counter64", "Gauge32", "NotificationType", "ModuleIdentity", "Integer32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "TimeTicks", "MibIdentifier", "Counter32")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
mLogEntryCount = MibScalar((1, 3, 6, 1, 4, 1, 166, 1, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mLogEntryCount.setStatus('deprecated')
mLogNewMessageTrapEnable = MibScalar((1, 3, 6, 1, 4, 1, 166, 1, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 8, 9))).clone(namedValues=NamedValues(("disabled", 1), ("emerg", 2), ("alert", 3), ("crit", 4), ("err", 5), ("warning", 6), ("notice", 7), ("info", 8), ("debug", 9))).clone('disabled')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: mLogNewMessageTrapEnable.setStatus('deprecated')
mLogBuffer = MibTable((1, 3, 6, 1, 4, 1, 166, 1, 1, 3), )
if mibBuilder.loadTexts: mLogBuffer.setStatus('deprecated')
pysmiFakeCol1000 = MibTableColumn((1, 3, 6, 1, 4, 1, 166, 1, 1, 3, 1) + (1000, ), Integer32())
mLogMessage = MibTableRow((1, 3, 6, 1, 4, 1, 166, 1, 1, 3, 1), ).setIndexNames((0, "SHIVA-MLOG-MIB", "pysmiFakeCol1000"))
if mibBuilder.loadTexts: mLogMessage.setStatus('deprecated')
mLogTimeStamp = MibTableColumn((1, 3, 6, 1, 4, 1, 166, 1, 1, 3, 1, 1), TimeTicks()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mLogTimeStamp.setStatus('deprecated')
mLogPriority = MibTableColumn((1, 3, 6, 1, 4, 1, 166, 1, 1, 3, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 8, 9))).clone(namedValues=NamedValues(("not-possible", 1), ("emerg", 2), ("alert", 3), ("crit", 4), ("err", 5), ("warning", 6), ("notice", 7), ("info", 8), ("debug", 9)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: mLogPriority.setStatus('deprecated')
mLogMessageText = MibTableColumn((1, 3, 6, 1, 4, 1, 166, 1, 1, 3, 1, 3), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mLogMessageText.setStatus('deprecated')
mLogTimeOfDay = MibTableColumn((1, 3, 6, 1, 4, 1, 166, 1, 1, 3, 1, 4), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mLogTimeOfDay.setStatus('deprecated')
mibBuilder.exportSymbols("SHIVA-MLOG-MIB", mLogMessageText=mLogMessageText, mLogPriority=mLogPriority, mLogBuffer=mLogBuffer, mLogEntryCount=mLogEntryCount, pysmiFakeCol1000=pysmiFakeCol1000, mLogTimeOfDay=mLogTimeOfDay, mLogMessage=mLogMessage, mLogNewMessageTrapEnable=mLogNewMessageTrapEnable, mLogTimeStamp=mLogTimeStamp)
