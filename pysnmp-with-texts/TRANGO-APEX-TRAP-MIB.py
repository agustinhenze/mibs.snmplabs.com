#
# PySNMP MIB module TRANGO-APEX-TRAP-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/TRANGO-APEX-TRAP-MIB
# Produced by pysmi-0.3.4 at Wed May  1 15:26:58 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
ObjectIdentifier, Integer, OctetString = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "Integer", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsUnion, SingleValueConstraint, ValueSizeConstraint, ConstraintsIntersection, ValueRangeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "SingleValueConstraint", "ValueSizeConstraint", "ConstraintsIntersection", "ValueRangeConstraint")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
IpAddress, iso, Bits, Gauge32, MibIdentifier, Unsigned32, Counter32, ObjectIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, NotificationType, TimeTicks, Integer32, Counter64, ModuleIdentity = mibBuilder.importSymbols("SNMPv2-SMI", "IpAddress", "iso", "Bits", "Gauge32", "MibIdentifier", "Unsigned32", "Counter32", "ObjectIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "NotificationType", "TimeTicks", "Integer32", "Counter64", "ModuleIdentity")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
Unsigned32, ObjectIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, ModuleIdentity, NotificationType, apex = mibBuilder.importSymbols("TRANGO-APEX-MIB", "Unsigned32", "ObjectIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "ModuleIdentity", "NotificationType", "apex")
class DisplayString(OctetString):
    pass

trangotrap = MibIdentifier((1, 3, 6, 1, 4, 1, 5454, 1, 60, 6))
trapReboot = NotificationType((1, 3, 6, 1, 4, 1, 5454, 1, 60, 6, 1))
if mibBuilder.loadTexts: trapReboot.setStatus('current')
if mibBuilder.loadTexts: trapReboot.setDescription('send traps when the system reboots')
trapStartUp = NotificationType((1, 3, 6, 1, 4, 1, 5454, 1, 60, 6, 2))
if mibBuilder.loadTexts: trapStartUp.setStatus('current')
if mibBuilder.loadTexts: trapStartUp.setDescription('send traps when the system starts up')
traplock = MibIdentifier((1, 3, 6, 1, 4, 1, 5454, 1, 60, 6, 3))
trapModemLock = NotificationType((1, 3, 6, 1, 4, 1, 5454, 1, 60, 6, 3, 1))
if mibBuilder.loadTexts: trapModemLock.setStatus('current')
if mibBuilder.loadTexts: trapModemLock.setDescription('send traps when the system lose modem lock')
trapTimingLock = NotificationType((1, 3, 6, 1, 4, 1, 5454, 1, 60, 6, 3, 2))
if mibBuilder.loadTexts: trapTimingLock.setStatus('current')
if mibBuilder.loadTexts: trapTimingLock.setDescription('Timing Lock in modem changed')
trapInnerCodeLock = NotificationType((1, 3, 6, 1, 4, 1, 5454, 1, 60, 6, 3, 3))
if mibBuilder.loadTexts: trapInnerCodeLock.setStatus('current')
if mibBuilder.loadTexts: trapInnerCodeLock.setDescription('send traps when the system lose Inner Code lock')
trapEqualizerLock = NotificationType((1, 3, 6, 1, 4, 1, 5454, 1, 60, 6, 3, 4))
if mibBuilder.loadTexts: trapEqualizerLock.setStatus('current')
if mibBuilder.loadTexts: trapEqualizerLock.setDescription('send traps when the system lose Equalizer lock')
trapFrameSyncLock = NotificationType((1, 3, 6, 1, 4, 1, 5454, 1, 60, 6, 3, 5))
if mibBuilder.loadTexts: trapFrameSyncLock.setStatus('current')
if mibBuilder.loadTexts: trapFrameSyncLock.setDescription('send traps when the system lose Frame Sync lock')
trapthreshold = MibIdentifier((1, 3, 6, 1, 4, 1, 5454, 1, 60, 6, 4))
trapmse = MibIdentifier((1, 3, 6, 1, 4, 1, 5454, 1, 60, 6, 4, 1))
trapMSEMinThreshold = NotificationType((1, 3, 6, 1, 4, 1, 5454, 1, 60, 6, 4, 1, 1))
if mibBuilder.loadTexts: trapMSEMinThreshold.setStatus('current')
if mibBuilder.loadTexts: trapMSEMinThreshold.setDescription('send traps when the MSE fall out from the threshold')
trapMSEMaxThreshold = NotificationType((1, 3, 6, 1, 4, 1, 5454, 1, 60, 6, 4, 1, 2))
if mibBuilder.loadTexts: trapMSEMaxThreshold.setStatus('current')
if mibBuilder.loadTexts: trapMSEMaxThreshold.setDescription('send traps when the MSE fall out from the threshold')
trapber = MibIdentifier((1, 3, 6, 1, 4, 1, 5454, 1, 60, 6, 4, 2))
trapBERMinThreshold = NotificationType((1, 3, 6, 1, 4, 1, 5454, 1, 60, 6, 4, 2, 1))
if mibBuilder.loadTexts: trapBERMinThreshold.setStatus('current')
if mibBuilder.loadTexts: trapBERMinThreshold.setDescription('send traps when the BER fall out from the threshold')
trapBERMaxThreshold = NotificationType((1, 3, 6, 1, 4, 1, 5454, 1, 60, 6, 4, 2, 2))
if mibBuilder.loadTexts: trapBERMaxThreshold.setStatus('current')
if mibBuilder.loadTexts: trapBERMaxThreshold.setDescription('send traps when the BER fall out from the threshold')
trapfer = MibIdentifier((1, 3, 6, 1, 4, 1, 5454, 1, 60, 6, 4, 3))
trapFERMinThreshold = NotificationType((1, 3, 6, 1, 4, 1, 5454, 1, 60, 6, 4, 3, 1))
if mibBuilder.loadTexts: trapFERMinThreshold.setStatus('current')
if mibBuilder.loadTexts: trapFERMinThreshold.setDescription('send traps when the FER fall out from the threshold')
trapFERMaxThreshold = NotificationType((1, 3, 6, 1, 4, 1, 5454, 1, 60, 6, 4, 3, 2))
if mibBuilder.loadTexts: trapFERMaxThreshold.setStatus('current')
if mibBuilder.loadTexts: trapFERMaxThreshold.setDescription('send traps when the FER fall out from the threshold')
traprssi = MibIdentifier((1, 3, 6, 1, 4, 1, 5454, 1, 60, 6, 4, 4))
trapRSSIMinThreshold = NotificationType((1, 3, 6, 1, 4, 1, 5454, 1, 60, 6, 4, 4, 1))
if mibBuilder.loadTexts: trapRSSIMinThreshold.setStatus('current')
if mibBuilder.loadTexts: trapRSSIMinThreshold.setDescription('send traps when the RSSI fall out from the threshold')
trapRSSIMaxThreshold = NotificationType((1, 3, 6, 1, 4, 1, 5454, 1, 60, 6, 4, 4, 2))
if mibBuilder.loadTexts: trapRSSIMaxThreshold.setStatus('current')
if mibBuilder.loadTexts: trapRSSIMaxThreshold.setDescription('send traps when the RSSI fall out from the threshold')
trapidutemp = MibIdentifier((1, 3, 6, 1, 4, 1, 5454, 1, 60, 6, 4, 5))
trapIDUTempMinThreshold = NotificationType((1, 3, 6, 1, 4, 1, 5454, 1, 60, 6, 4, 5, 1))
if mibBuilder.loadTexts: trapIDUTempMinThreshold.setStatus('current')
if mibBuilder.loadTexts: trapIDUTempMinThreshold.setDescription('send traps when the ethernet status exceed threshold')
trapIDUTempMaxThreshold = NotificationType((1, 3, 6, 1, 4, 1, 5454, 1, 60, 6, 4, 5, 2))
if mibBuilder.loadTexts: trapIDUTempMaxThreshold.setStatus('current')
if mibBuilder.loadTexts: trapIDUTempMaxThreshold.setDescription('send traps when the ethernet status exceed threshold')
trapodutemp = MibIdentifier((1, 3, 6, 1, 4, 1, 5454, 1, 60, 6, 4, 6))
trapODUTempMinThreshold = NotificationType((1, 3, 6, 1, 4, 1, 5454, 1, 60, 6, 4, 6, 1))
if mibBuilder.loadTexts: trapODUTempMinThreshold.setStatus('current')
if mibBuilder.loadTexts: trapODUTempMinThreshold.setDescription('send traps when the T1 status exceed threshold')
trapODUTempMaxThreshold = NotificationType((1, 3, 6, 1, 4, 1, 5454, 1, 60, 6, 4, 6, 2))
if mibBuilder.loadTexts: trapODUTempMaxThreshold.setStatus('current')
if mibBuilder.loadTexts: trapODUTempMaxThreshold.setDescription('send traps when the T1 status exceed threshold')
trapinport = MibIdentifier((1, 3, 6, 1, 4, 1, 5454, 1, 60, 6, 4, 7))
trapInPortUtilMinThreshold = NotificationType((1, 3, 6, 1, 4, 1, 5454, 1, 60, 6, 4, 7, 1))
if mibBuilder.loadTexts: trapInPortUtilMinThreshold.setStatus('current')
if mibBuilder.loadTexts: trapInPortUtilMinThreshold.setDescription('send traps when the IN port utilization fall below min threshold')
trapInPortUtilMaxThreshold = NotificationType((1, 3, 6, 1, 4, 1, 5454, 1, 60, 6, 4, 7, 2))
if mibBuilder.loadTexts: trapInPortUtilMaxThreshold.setStatus('current')
if mibBuilder.loadTexts: trapInPortUtilMaxThreshold.setDescription('send traps when the IN port utilization exceed max threshold')
trapoutport = MibIdentifier((1, 3, 6, 1, 4, 1, 5454, 1, 60, 6, 4, 8))
trapOutPortUtilMinThreshold = NotificationType((1, 3, 6, 1, 4, 1, 5454, 1, 60, 6, 4, 8, 1))
if mibBuilder.loadTexts: trapOutPortUtilMinThreshold.setStatus('current')
if mibBuilder.loadTexts: trapOutPortUtilMinThreshold.setDescription('send traps when the OUT port utilization fall below min threshold')
trapOutPortUtilMaxThreshold = NotificationType((1, 3, 6, 1, 4, 1, 5454, 1, 60, 6, 4, 8, 2))
if mibBuilder.loadTexts: trapOutPortUtilMaxThreshold.setStatus('current')
if mibBuilder.loadTexts: trapOutPortUtilMaxThreshold.setDescription('send traps when the OUT port utilization exceed max threshold')
trapstandby = MibIdentifier((1, 3, 6, 1, 4, 1, 5454, 1, 60, 6, 5))
trapStandbyLinkDown = NotificationType((1, 3, 6, 1, 4, 1, 5454, 1, 60, 6, 5, 1))
if mibBuilder.loadTexts: trapStandbyLinkDown.setStatus('current')
if mibBuilder.loadTexts: trapStandbyLinkDown.setDescription('send traps when Standby link is down')
trapStandbyLinkUp = NotificationType((1, 3, 6, 1, 4, 1, 5454, 1, 60, 6, 5, 2))
if mibBuilder.loadTexts: trapStandbyLinkUp.setStatus('current')
if mibBuilder.loadTexts: trapStandbyLinkUp.setDescription('send traps when Standby link is up')
trapSwitchover = NotificationType((1, 3, 6, 1, 4, 1, 5454, 1, 60, 6, 5, 3))
if mibBuilder.loadTexts: trapSwitchover.setStatus('current')
if mibBuilder.loadTexts: trapSwitchover.setDescription('send traps when backup unit takes over the link')
trapeth = MibIdentifier((1, 3, 6, 1, 4, 1, 5454, 1, 60, 6, 6))
trapethstatus = MibIdentifier((1, 3, 6, 1, 4, 1, 5454, 1, 60, 6, 6, 1))
trapEth1StatusUpdate = NotificationType((1, 3, 6, 1, 4, 1, 5454, 1, 60, 6, 6, 1, 1))
if mibBuilder.loadTexts: trapEth1StatusUpdate.setStatus('current')
if mibBuilder.loadTexts: trapEth1StatusUpdate.setDescription('send traps when ethernet port 1 status changed')
trapEth2StatusUpdate = NotificationType((1, 3, 6, 1, 4, 1, 5454, 1, 60, 6, 6, 1, 2))
if mibBuilder.loadTexts: trapEth2StatusUpdate.setStatus('current')
if mibBuilder.loadTexts: trapEth2StatusUpdate.setDescription('send traps when ethernet port 2 status changed')
trapEth3StatusUpdate = NotificationType((1, 3, 6, 1, 4, 1, 5454, 1, 60, 6, 6, 1, 3))
if mibBuilder.loadTexts: trapEth3StatusUpdate.setStatus('current')
if mibBuilder.loadTexts: trapEth3StatusUpdate.setDescription('send traps when ethernet port 3 status changed')
trapEth4StatusUpdate = NotificationType((1, 3, 6, 1, 4, 1, 5454, 1, 60, 6, 6, 1, 4))
if mibBuilder.loadTexts: trapEth4StatusUpdate.setStatus('current')
if mibBuilder.loadTexts: trapEth4StatusUpdate.setDescription('send traps when ethernet port 4 status changed')
trapDownShift = NotificationType((1, 3, 6, 1, 4, 1, 5454, 1, 60, 6, 8))
if mibBuilder.loadTexts: trapDownShift.setStatus('current')
if mibBuilder.loadTexts: trapDownShift.setDescription('send traps when the system downshift the modulation')
trapRapidPortShutdown = NotificationType((1, 3, 6, 1, 4, 1, 5454, 1, 60, 6, 9))
if mibBuilder.loadTexts: trapRapidPortShutdown.setStatus('current')
if mibBuilder.loadTexts: trapRapidPortShutdown.setDescription('send traps when the rapid port shutdown occurs')
trapRPSPortUp = NotificationType((1, 3, 6, 1, 4, 1, 5454, 1, 60, 6, 10))
if mibBuilder.loadTexts: trapRPSPortUp.setStatus('current')
if mibBuilder.loadTexts: trapRPSPortUp.setDescription('send traps when the re-enable ports after RPS port down')
mibBuilder.exportSymbols("TRANGO-APEX-TRAP-MIB", trapODUTempMaxThreshold=trapODUTempMaxThreshold, trapIDUTempMinThreshold=trapIDUTempMinThreshold, trapber=trapber, trapethstatus=trapethstatus, trapoutport=trapoutport, trapFrameSyncLock=trapFrameSyncLock, trapStandbyLinkDown=trapStandbyLinkDown, trapSwitchover=trapSwitchover, trapReboot=trapReboot, trapEqualizerLock=trapEqualizerLock, trapBERMaxThreshold=trapBERMaxThreshold, trapODUTempMinThreshold=trapODUTempMinThreshold, trapInPortUtilMinThreshold=trapInPortUtilMinThreshold, trapInPortUtilMaxThreshold=trapInPortUtilMaxThreshold, traprssi=traprssi, trapRSSIMinThreshold=trapRSSIMinThreshold, trapmse=trapmse, DisplayString=DisplayString, trapOutPortUtilMaxThreshold=trapOutPortUtilMaxThreshold, trapEth1StatusUpdate=trapEth1StatusUpdate, trapBERMinThreshold=trapBERMinThreshold, trapidutemp=trapidutemp, traplock=traplock, trapstandby=trapstandby, trapEth2StatusUpdate=trapEth2StatusUpdate, trapRPSPortUp=trapRPSPortUp, trapMSEMaxThreshold=trapMSEMaxThreshold, trapStartUp=trapStartUp, trapeth=trapeth, trapRapidPortShutdown=trapRapidPortShutdown, trangotrap=trangotrap, trapStandbyLinkUp=trapStandbyLinkUp, trapMSEMinThreshold=trapMSEMinThreshold, trapodutemp=trapodutemp, trapTimingLock=trapTimingLock, trapRSSIMaxThreshold=trapRSSIMaxThreshold, trapIDUTempMaxThreshold=trapIDUTempMaxThreshold, trapinport=trapinport, trapfer=trapfer, trapEth3StatusUpdate=trapEth3StatusUpdate, trapInnerCodeLock=trapInnerCodeLock, trapOutPortUtilMinThreshold=trapOutPortUtilMinThreshold, trapEth4StatusUpdate=trapEth4StatusUpdate, trapFERMaxThreshold=trapFERMaxThreshold, trapFERMinThreshold=trapFERMinThreshold, trapthreshold=trapthreshold, trapDownShift=trapDownShift, trapModemLock=trapModemLock)
