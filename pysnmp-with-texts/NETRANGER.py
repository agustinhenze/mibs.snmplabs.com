#
# PySNMP MIB module NETRANGER (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/NETRANGER
# Produced by pysmi-0.3.4 at Wed May  1 14:19:58 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
ObjectIdentifier, Integer, OctetString = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "Integer", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
SingleValueConstraint, ConstraintsUnion, ValueSizeConstraint, ConstraintsIntersection, ValueRangeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "SingleValueConstraint", "ConstraintsUnion", "ValueSizeConstraint", "ConstraintsIntersection", "ValueRangeConstraint")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
Unsigned32, Counter32, ModuleIdentity, Gauge32, enterprises, Bits, iso, Counter64, NotificationType, Integer32, ObjectIdentity, TimeTicks, IpAddress, MibScalar, MibTable, MibTableRow, MibTableColumn, MibIdentifier = mibBuilder.importSymbols("SNMPv2-SMI", "Unsigned32", "Counter32", "ModuleIdentity", "Gauge32", "enterprises", "Bits", "iso", "Counter64", "NotificationType", "Integer32", "ObjectIdentity", "TimeTicks", "IpAddress", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "MibIdentifier")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
wheelgroup = MibIdentifier((1, 3, 6, 1, 4, 1, 2252))
securityMgmt = MibIdentifier((1, 3, 6, 1, 4, 1, 2252, 1))
networkMgmt = MibIdentifier((1, 3, 6, 1, 4, 1, 2252, 3))
system = MibIdentifier((1, 3, 6, 1, 4, 1, 2252, 3, 1))
ip = MibIdentifier((1, 3, 6, 1, 4, 1, 2252, 3, 3))
snmp = MibIdentifier((1, 3, 6, 1, 4, 1, 2252, 3, 5))
netranger = MibIdentifier((1, 3, 6, 1, 4, 1, 2252, 1, 1))
autospa = MibIdentifier((1, 3, 6, 1, 4, 1, 2252, 1, 3))
nrTrapVars = MibIdentifier((1, 3, 6, 1, 4, 1, 2252, 1, 1, 1))
services = MibIdentifier((1, 3, 6, 1, 4, 1, 2252, 1, 1, 3))
general = MibIdentifier((1, 3, 6, 1, 4, 1, 2252, 1, 1, 5))
postoffice = MibIdentifier((1, 3, 6, 1, 4, 1, 2252, 1, 1, 3, 0))
sensor = MibIdentifier((1, 3, 6, 1, 4, 1, 2252, 1, 1, 3, 1))
config = MibIdentifier((1, 3, 6, 1, 4, 1, 2252, 1, 1, 3, 2))
manage = MibIdentifier((1, 3, 6, 1, 4, 1, 2252, 1, 1, 3, 3))
event = MibIdentifier((1, 3, 6, 1, 4, 1, 2252, 1, 1, 3, 4))
logger = MibIdentifier((1, 3, 6, 1, 4, 1, 2252, 1, 1, 3, 5))
smi = MibIdentifier((1, 3, 6, 1, 4, 1, 2252, 1, 1, 3, 6))
sap = MibIdentifier((1, 3, 6, 1, 4, 1, 2252, 1, 1, 3, 7))
packet = MibIdentifier((1, 3, 6, 1, 4, 1, 2252, 1, 1, 3, 8))
commonServices = MibIdentifier((1, 3, 6, 1, 4, 1, 2252, 1, 1, 3, 9))
commonVars = MibIdentifier((1, 3, 6, 1, 4, 1, 2252, 1, 1, 1, 0))
command = MibIdentifier((1, 3, 6, 1, 4, 1, 2252, 1, 1, 1, 1))
error = MibIdentifier((1, 3, 6, 1, 4, 1, 2252, 1, 1, 1, 2))
commandLog = MibIdentifier((1, 3, 6, 1, 4, 1, 2252, 1, 1, 1, 3))
alarm = MibIdentifier((1, 3, 6, 1, 4, 1, 2252, 1, 1, 1, 4))
ipLog = MibIdentifier((1, 3, 6, 1, 4, 1, 2252, 1, 1, 1, 5))
redirect = MibIdentifier((1, 3, 6, 1, 4, 1, 2252, 1, 1, 1, 6))
addressing = MibIdentifier((1, 3, 6, 1, 4, 1, 2252, 1, 1, 1, 4, 1))
tcpip = MibIdentifier((1, 3, 6, 1, 4, 1, 2252, 1, 1, 1, 4, 1, 1))
messageType = MibScalar((1, 3, 6, 1, 4, 1, 2252, 1, 1, 1, 0, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: messageType.setStatus('mandatory')
if mibBuilder.loadTexts: messageType.setDescription('Identifies the type of message (trap) being sent. Type types are: 1) command 2) error 3) command log 4) alarm 5) IP log 6) redirect This object cannot be retrieved from the SNMP agent.')
recordId = MibScalar((1, 3, 6, 1, 4, 1, 2252, 1, 1, 1, 0, 2), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: recordId.setStatus('mandatory')
if mibBuilder.loadTexts: recordId.setDescription('An ID that is used along with a timestamp, org, host, and application ID to uniquiely identify a message (trap). This object cannot be retrieved from the SNMP agent.')
globalTime = MibScalar((1, 3, 6, 1, 4, 1, 2252, 1, 1, 1, 0, 3), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: globalTime.setStatus('mandatory')
if mibBuilder.loadTexts: globalTime.setDescription('The time at which the message was generated, expressed in number of seconds since the epoch (Jan 1, 1970), with respect to GMT. This object cannot be retrieved from the SNMP agent.')
localTime = MibScalar((1, 3, 6, 1, 4, 1, 2252, 1, 1, 1, 0, 4), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: localTime.setStatus('mandatory')
if mibBuilder.loadTexts: localTime.setDescription('The time at which the message was generated, expressed in number of seconds since the epoch (Jan 1, 1970), with respect to the timezone local to the machine that generated the message. The combination of the globalTime and the localTime can be used to calculate the timezone of the source machine. This object cannot be retrieved from the SNMP agent.')
dateString = MibScalar((1, 3, 6, 1, 4, 1, 2252, 1, 1, 1, 0, 5), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dateString.setStatus('mandatory')
if mibBuilder.loadTexts: dateString.setDescription('The date at which the message was generated, with respect to the timezone of the source machine, expressed as an ASCII string in the format yyyy/mm/dd. This object cannot be retrieved from the SNMP agent.')
timeString = MibScalar((1, 3, 6, 1, 4, 1, 2252, 1, 1, 1, 0, 6), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: timeString.setStatus('mandatory')
if mibBuilder.loadTexts: timeString.setDescription('The time at which the message was generated, with respect to the timezone of the source machine, expressed as an ASCII string in the format hh:mm:ss. This object cannot be retrieved from the SNMP agent.')
appId = MibScalar((1, 3, 6, 1, 4, 1, 2252, 1, 1, 1, 0, 7), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: appId.setStatus('mandatory')
if mibBuilder.loadTexts: appId.setDescription('The application ID of the NetRanger application that generated the message. This object cannot be retrieved from the SNMP agent.')
hostId = MibScalar((1, 3, 6, 1, 4, 1, 2252, 1, 1, 1, 0, 8), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hostId.setStatus('mandatory')
if mibBuilder.loadTexts: hostId.setDescription('The host ID of the machine running the NetRanger application that generated the message. This object cannot be retrieved from the SNMP agent.')
orgId = MibScalar((1, 3, 6, 1, 4, 1, 2252, 1, 1, 1, 0, 9), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: orgId.setStatus('mandatory')
if mibBuilder.loadTexts: orgId.setDescription('An ID that uniquely identifies the organization responsible for the machine running the NetRanger application that generated the message. This object cannot be retrieved from the SNMP agent.')
errorMessage = MibScalar((1, 3, 6, 1, 4, 1, 2252, 1, 1, 1, 2, 1), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: errorMessage.setStatus('mandatory')
if mibBuilder.loadTexts: errorMessage.setDescription('Describes the error that occurred. This object cannot be retrieved from the SNMP agent.')
sourceAppId = MibScalar((1, 3, 6, 1, 4, 1, 2252, 1, 1, 1, 3, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sourceAppId.setStatus('mandatory')
if mibBuilder.loadTexts: sourceAppId.setDescription('The application ID of the NetRanger application that executed the command. This object cannot be retrieved from the SNMP agent.')
sourceHostId = MibScalar((1, 3, 6, 1, 4, 1, 2252, 1, 1, 1, 3, 2), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sourceHostId.setStatus('mandatory')
if mibBuilder.loadTexts: sourceHostId.setDescription('The host ID of the machine running the NetRanger application that executed the command. This object cannot be retrieved from the SNMP agent.')
sourceOrgId = MibScalar((1, 3, 6, 1, 4, 1, 2252, 1, 1, 1, 3, 3), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sourceOrgId.setStatus('mandatory')
if mibBuilder.loadTexts: sourceOrgId.setDescription('An ID that uniquely identifies the organization responsible for the machine running the NetRanger application that generated the command. This object cannot be retrieved from the SNMP agent.')
commandMessage = MibScalar((1, 3, 6, 1, 4, 1, 2252, 1, 1, 1, 3, 4), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: commandMessage.setStatus('mandatory')
if mibBuilder.loadTexts: commandMessage.setDescription('Describes the command that was executed. This object cannot be retrieved from the SNMP agent.')
srcDirection = MibScalar((1, 3, 6, 1, 4, 1, 2252, 1, 1, 1, 4, 3), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: srcDirection.setStatus('mandatory')
if mibBuilder.loadTexts: srcDirection.setDescription('Describes whether the source of the alarm is inside or outside the protected network. IN means inside, and OUT means outside. This object cannot be retrieved from the SNMP agent.')
dstDirection = MibScalar((1, 3, 6, 1, 4, 1, 2252, 1, 1, 1, 4, 5), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dstDirection.setStatus('mandatory')
if mibBuilder.loadTexts: dstDirection.setDescription('Describes whether the destination of the alarm (the machine being attacked) is inside or outside the protected network. IN means inside, and OUT means outside. This object cannot be retrieved from the SNMP agent.')
eventLevel = MibScalar((1, 3, 6, 1, 4, 1, 2252, 1, 1, 1, 4, 7), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: eventLevel.setStatus('mandatory')
if mibBuilder.loadTexts: eventLevel.setDescription('An integer that reflects the severity level of the alarm. The number can range from 1 to 255, but the current NetRanger system only uses 1 (least severe) to 5 (most severe). This object cannot be retrieved from the SNMP agent.')
sigId = MibScalar((1, 3, 6, 1, 4, 1, 2252, 1, 1, 1, 4, 9), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sigId.setStatus('mandatory')
if mibBuilder.loadTexts: sigId.setDescription('Describes which signature was detected. The full list of signatures can be found on a NetRanger system at /usr/nr/etc/signatures. This object cannot be retrieved from the SNMP agent.')
subSigId = MibScalar((1, 3, 6, 1, 4, 1, 2252, 1, 1, 1, 4, 11), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: subSigId.setStatus('mandatory')
if mibBuilder.loadTexts: subSigId.setDescription('Provides additional information about an alarm signature. This object cannot be retrieved from the SNMP agent.')
protocol = MibScalar((1, 3, 6, 1, 4, 1, 2252, 1, 1, 1, 4, 13), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: protocol.setStatus('mandatory')
if mibBuilder.loadTexts: protocol.setDescription('Describes the protocol of the attack that was detected. Usually, this will be TCP/IP. This object cannot be retrieved from the SNMP agent.')
srcIpAddr = MibScalar((1, 3, 6, 1, 4, 1, 2252, 1, 1, 1, 4, 1, 1, 1), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: srcIpAddr.setStatus('mandatory')
if mibBuilder.loadTexts: srcIpAddr.setDescription('The IP address of the machine from which the attack originated. This object cannot be retrieved from the SNMP agent.')
dstIpAddr = MibScalar((1, 3, 6, 1, 4, 1, 2252, 1, 1, 1, 4, 1, 1, 3), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dstIpAddr.setStatus('mandatory')
if mibBuilder.loadTexts: dstIpAddr.setDescription('The IP address of the machine being attacked. This object cannot be retrieved from the SNMP agent.')
srcIpPort = MibScalar((1, 3, 6, 1, 4, 1, 2252, 1, 1, 1, 4, 1, 1, 5), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: srcIpPort.setStatus('mandatory')
if mibBuilder.loadTexts: srcIpPort.setDescription('The port from which the attack originated. This object cannot be retrieved from the SNMP agent.')
dstIpPort = MibScalar((1, 3, 6, 1, 4, 1, 2252, 1, 1, 1, 4, 1, 1, 7), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dstIpPort.setStatus('mandatory')
if mibBuilder.loadTexts: dstIpPort.setDescription('The port that received the attack on the destination machine. This value may not have significance for signatures that involve multiple ports (for example, a port sweep). This object cannot be retrieved from the SNMP agent.')
rtrIpAddr = MibScalar((1, 3, 6, 1, 4, 1, 2252, 1, 1, 1, 4, 1, 1, 9), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rtrIpAddr.setStatus('mandatory')
if mibBuilder.loadTexts: rtrIpAddr.setDescription('The IP address of the router through which the attack traveled. This object cannot be retrieved from the SNMP agent.')
alarmMessage = MibScalar((1, 3, 6, 1, 4, 1, 2252, 1, 1, 1, 4, 15), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: alarmMessage.setStatus('mandatory')
if mibBuilder.loadTexts: alarmMessage.setDescription('ASCII string that provides additional information about an alarm. For instance, this field gives the exact string that was matched during a string match alarm. This object cannot be retrieved from the SNMP agent.')
mibBuilder.exportSymbols("NETRANGER", alarm=alarm, general=general, sourceAppId=sourceAppId, addressing=addressing, timeString=timeString, srcDirection=srcDirection, dstIpAddr=dstIpAddr, tcpip=tcpip, commonServices=commonServices, nrTrapVars=nrTrapVars, packet=packet, hostId=hostId, sourceHostId=sourceHostId, errorMessage=errorMessage, srcIpAddr=srcIpAddr, redirect=redirect, netranger=netranger, subSigId=subSigId, postoffice=postoffice, alarmMessage=alarmMessage, config=config, commonVars=commonVars, error=error, commandLog=commandLog, localTime=localTime, ipLog=ipLog, commandMessage=commandMessage, srcIpPort=srcIpPort, system=system, sourceOrgId=sourceOrgId, eventLevel=eventLevel, sap=sap, dateString=dateString, autospa=autospa, logger=logger, orgId=orgId, smi=smi, recordId=recordId, messageType=messageType, sigId=sigId, dstIpPort=dstIpPort, rtrIpAddr=rtrIpAddr, wheelgroup=wheelgroup, event=event, sensor=sensor, command=command, globalTime=globalTime, appId=appId, dstDirection=dstDirection, networkMgmt=networkMgmt, ip=ip, services=services, snmp=snmp, manage=manage, securityMgmt=securityMgmt, protocol=protocol)