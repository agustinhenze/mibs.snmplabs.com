#
# PySNMP MIB module NOKIA-AZC-SYSTEM-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/NOKIA-AZC-SYSTEM-MIB
# Produced by pysmi-0.3.4 at Wed May  1 14:23:20 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
OctetString, ObjectIdentifier, Integer = mibBuilder.importSymbols("ASN1", "OctetString", "ObjectIdentifier", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsUnion, SingleValueConstraint, ValueRangeConstraint, ConstraintsIntersection, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "SingleValueConstraint", "ValueRangeConstraint", "ConstraintsIntersection", "ValueSizeConstraint")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
Unsigned32, Integer32, Gauge32, TimeTicks, Counter64, IpAddress, Bits, NotificationType, enterprises, MibIdentifier, MibScalar, MibTable, MibTableRow, MibTableColumn, ObjectIdentity, Counter32, ModuleIdentity, iso = mibBuilder.importSymbols("SNMPv2-SMI", "Unsigned32", "Integer32", "Gauge32", "TimeTicks", "Counter64", "IpAddress", "Bits", "NotificationType", "enterprises", "MibIdentifier", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "ObjectIdentity", "Counter32", "ModuleIdentity", "iso")
DisplayString, TextualConvention, DateAndTime = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention", "DateAndTime")
nokia = MibIdentifier((1, 3, 6, 1, 4, 1, 94))
nokiaProducts = MibIdentifier((1, 3, 6, 1, 4, 1, 94, 1))
azcProducts = MibIdentifier((1, 3, 6, 1, 4, 1, 94, 1, 32))
azcSystem = MibIdentifier((1, 3, 6, 1, 4, 1, 94, 1, 32, 2))
azcStatusGroup = MibIdentifier((1, 3, 6, 1, 4, 1, 94, 1, 32, 2, 1))
azcVersion = MibScalar((1, 3, 6, 1, 4, 1, 94, 1, 32, 2, 1, 1), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: azcVersion.setStatus('mandatory')
if mibBuilder.loadTexts: azcVersion.setDescription('The version tag of AZC software. ')
azcRelease = MibScalar((1, 3, 6, 1, 4, 1, 94, 1, 32, 2, 1, 2), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: azcRelease.setStatus('mandatory')
if mibBuilder.loadTexts: azcRelease.setDescription('The release number of AZC software. ')
azcStarted = MibScalar((1, 3, 6, 1, 4, 1, 94, 1, 32, 2, 1, 3), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: azcStarted.setStatus('mandatory')
if mibBuilder.loadTexts: azcStarted.setDescription('The datestamp when AZC software was started. ')
azcLoginsSuccess = MibScalar((1, 3, 6, 1, 4, 1, 94, 1, 32, 2, 1, 4), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: azcLoginsSuccess.setStatus('mandatory')
if mibBuilder.loadTexts: azcLoginsSuccess.setDescription('The number of successful logins. ')
azcLoginsAuthFailures = MibScalar((1, 3, 6, 1, 4, 1, 94, 1, 32, 2, 1, 5), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: azcLoginsAuthFailures.setStatus('mandatory')
if mibBuilder.loadTexts: azcLoginsAuthFailures.setDescription('The number of logins failed because of authentication failure. ')
azcLoginsACLFailures = MibScalar((1, 3, 6, 1, 4, 1, 94, 1, 32, 2, 1, 6), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: azcLoginsACLFailures.setStatus('mandatory')
if mibBuilder.loadTexts: azcLoginsACLFailures.setDescription('The number of logins failed because of ACL subsystem failure. ')
azcLoginsDuplFailures = MibScalar((1, 3, 6, 1, 4, 1, 94, 1, 32, 2, 1, 7), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: azcLoginsDuplFailures.setStatus('mandatory')
if mibBuilder.loadTexts: azcLoginsDuplFailures.setDescription('The number of logins failed because user had already logged on. ')
azcLoginsSpaceFailures = MibScalar((1, 3, 6, 1, 4, 1, 94, 1, 32, 2, 1, 8), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: azcLoginsSpaceFailures.setStatus('mandatory')
if mibBuilder.loadTexts: azcLoginsSpaceFailures.setDescription('The number of logins failed because maximum number of users already logged on. ')
azcLoginsRADIUSFailures = MibScalar((1, 3, 6, 1, 4, 1, 94, 1, 32, 2, 1, 9), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: azcLoginsRADIUSFailures.setStatus('mandatory')
if mibBuilder.loadTexts: azcLoginsRADIUSFailures.setDescription('The number of logins failed because RADIUS system error. ')
azcLoginsRADIUSACLFailures = MibScalar((1, 3, 6, 1, 4, 1, 94, 1, 32, 2, 1, 10), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: azcLoginsRADIUSACLFailures.setStatus('mandatory')
if mibBuilder.loadTexts: azcLoginsRADIUSACLFailures.setDescription('The number of logins failed because RADIUS ACL error. Currently not used. ')
azcAutologoffsRADIUS = MibScalar((1, 3, 6, 1, 4, 1, 94, 1, 32, 2, 1, 11), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: azcAutologoffsRADIUS.setStatus('mandatory')
if mibBuilder.loadTexts: azcAutologoffsRADIUS.setDescription('The number of autologoffs because RADIUS of negative accounting response. ')
azcAutologoffsPing = MibScalar((1, 3, 6, 1, 4, 1, 94, 1, 32, 2, 1, 12), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: azcAutologoffsPing.setStatus('mandatory')
if mibBuilder.loadTexts: azcAutologoffsPing.setDescription('The number of autologoffs because of no response to pings. ')
azcAutologoffsMAC = MibScalar((1, 3, 6, 1, 4, 1, 94, 1, 32, 2, 1, 13), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: azcAutologoffsMAC.setStatus('mandatory')
if mibBuilder.loadTexts: azcAutologoffsMAC.setDescription('The number of autologoffs because MAC address of an IP address has been changed. ')
azcAutologoffsACL = MibScalar((1, 3, 6, 1, 4, 1, 94, 1, 32, 2, 1, 14), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: azcAutologoffsACL.setStatus('mandatory')
if mibBuilder.loadTexts: azcAutologoffsACL.setDescription('The number of autologoffs because ACL error. ')
azcAutologoffsQuota = MibScalar((1, 3, 6, 1, 4, 1, 94, 1, 32, 2, 1, 15), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: azcAutologoffsQuota.setStatus('mandatory')
if mibBuilder.loadTexts: azcAutologoffsQuota.setDescription('The number of autologoffs because quota has exceeded. ')
azcAutologoffsMaxTime = MibScalar((1, 3, 6, 1, 4, 1, 94, 1, 32, 2, 1, 16), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: azcAutologoffsMaxTime.setStatus('mandatory')
if mibBuilder.loadTexts: azcAutologoffsMaxTime.setDescription('The number of autologoffs because maximum time exceeded. ')
azcAutologoffsIdletimer = MibScalar((1, 3, 6, 1, 4, 1, 94, 1, 32, 2, 1, 17), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: azcAutologoffsIdletimer.setStatus('mandatory')
if mibBuilder.loadTexts: azcAutologoffsIdletimer.setDescription('The number of autologoffs because session has been idle too long time. ')
azcPktsIntIn = MibScalar((1, 3, 6, 1, 4, 1, 94, 1, 32, 2, 1, 18), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: azcPktsIntIn.setStatus('mandatory')
if mibBuilder.loadTexts: azcPktsIntIn.setDescription('The number of packets received from the internal interface. ')
azcPktsIntOut = MibScalar((1, 3, 6, 1, 4, 1, 94, 1, 32, 2, 1, 19), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: azcPktsIntOut.setStatus('mandatory')
if mibBuilder.loadTexts: azcPktsIntOut.setDescription('The number of packets sent to the internal interface. ')
azcBytesIntIn = MibScalar((1, 3, 6, 1, 4, 1, 94, 1, 32, 2, 1, 20), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: azcBytesIntIn.setStatus('mandatory')
if mibBuilder.loadTexts: azcBytesIntIn.setDescription('The number of bytes received from the internal interface. ')
azcBytesIntOut = MibScalar((1, 3, 6, 1, 4, 1, 94, 1, 32, 2, 1, 21), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: azcBytesIntOut.setStatus('mandatory')
if mibBuilder.loadTexts: azcBytesIntOut.setDescription('The number of bytes sent to the internal interface. ')
azcPktsExtIn = MibScalar((1, 3, 6, 1, 4, 1, 94, 1, 32, 2, 1, 22), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: azcPktsExtIn.setStatus('mandatory')
if mibBuilder.loadTexts: azcPktsExtIn.setDescription('The number of packets received from the external interface. ')
azcPktsExtOut = MibScalar((1, 3, 6, 1, 4, 1, 94, 1, 32, 2, 1, 23), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: azcPktsExtOut.setStatus('mandatory')
if mibBuilder.loadTexts: azcPktsExtOut.setDescription('The number of packets sent to the external interface. ')
azcBytesExtIn = MibScalar((1, 3, 6, 1, 4, 1, 94, 1, 32, 2, 1, 24), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: azcBytesExtIn.setStatus('mandatory')
if mibBuilder.loadTexts: azcBytesExtIn.setDescription('The number of bytes received from the external interface. ')
azcBytesExtOut = MibScalar((1, 3, 6, 1, 4, 1, 94, 1, 32, 2, 1, 25), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: azcBytesExtOut.setStatus('mandatory')
if mibBuilder.loadTexts: azcBytesExtOut.setDescription('The number of bytes sent to the external interface. ')
azcPktsNattedIn = MibScalar((1, 3, 6, 1, 4, 1, 94, 1, 32, 2, 1, 26), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: azcPktsNattedIn.setStatus('mandatory')
if mibBuilder.loadTexts: azcPktsNattedIn.setDescription('The number of packets received and NATed. ')
azcPktsNattedOut = MibScalar((1, 3, 6, 1, 4, 1, 94, 1, 32, 2, 1, 27), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: azcPktsNattedOut.setStatus('mandatory')
if mibBuilder.loadTexts: azcPktsNattedOut.setDescription('The number of packets sent and NATed.')
azcBytesNattedIn = MibScalar((1, 3, 6, 1, 4, 1, 94, 1, 32, 2, 1, 28), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: azcBytesNattedIn.setStatus('mandatory')
if mibBuilder.loadTexts: azcBytesNattedIn.setDescription('The number of bytes received and NATed. ')
azcBytesNattedOut = MibScalar((1, 3, 6, 1, 4, 1, 94, 1, 32, 2, 1, 29), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: azcBytesNattedOut.setStatus('mandatory')
if mibBuilder.loadTexts: azcBytesNattedOut.setDescription('The number of bytes sent and NATed.')
azcPktsNattedErrIn = MibScalar((1, 3, 6, 1, 4, 1, 94, 1, 32, 2, 1, 30), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: azcPktsNattedErrIn.setStatus('mandatory')
if mibBuilder.loadTexts: azcPktsNattedErrIn.setDescription('The number of packets received and NAT failed. ')
azcPktsNattedErrOut = MibScalar((1, 3, 6, 1, 4, 1, 94, 1, 32, 2, 1, 31), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: azcPktsNattedErrOut.setStatus('mandatory')
if mibBuilder.loadTexts: azcPktsNattedErrOut.setDescription('The number of packets sent and NAT failed.')
azcBytesNattedErrIn = MibScalar((1, 3, 6, 1, 4, 1, 94, 1, 32, 2, 1, 32), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: azcBytesNattedErrIn.setStatus('mandatory')
if mibBuilder.loadTexts: azcBytesNattedErrIn.setDescription('The number of bytes received and NAT failed. ')
azcBytesNattedErrOut = MibScalar((1, 3, 6, 1, 4, 1, 94, 1, 32, 2, 1, 33), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: azcBytesNattedErrOut.setStatus('mandatory')
if mibBuilder.loadTexts: azcBytesNattedErrOut.setDescription('The number of bytes sent and NAT failed.')
azcPktsRejInt = MibScalar((1, 3, 6, 1, 4, 1, 94, 1, 32, 2, 1, 34), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: azcPktsRejInt.setStatus('mandatory')
if mibBuilder.loadTexts: azcPktsRejInt.setDescription('The number of packets rejected from the internal interface. ')
azcPktsRejExt = MibScalar((1, 3, 6, 1, 4, 1, 94, 1, 32, 2, 1, 35), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: azcPktsRejExt.setStatus('mandatory')
if mibBuilder.loadTexts: azcPktsRejExt.setDescription('The number of packets rejected from the external interface. ')
azcBytesRejInt = MibScalar((1, 3, 6, 1, 4, 1, 94, 1, 32, 2, 1, 36), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: azcBytesRejInt.setStatus('mandatory')
if mibBuilder.loadTexts: azcBytesRejInt.setDescription('The number of bytes rejected from the internal interface. ')
azcBytesRejExt = MibScalar((1, 3, 6, 1, 4, 1, 94, 1, 32, 2, 1, 37), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: azcBytesRejExt.setStatus('mandatory')
if mibBuilder.loadTexts: azcBytesRejExt.setDescription('The number of bytes rejected from the external interface. ')
azcACLSelectErr = MibScalar((1, 3, 6, 1, 4, 1, 94, 1, 32, 2, 1, 38), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: azcACLSelectErr.setStatus('mandatory')
if mibBuilder.loadTexts: azcACLSelectErr.setDescription('The number of select errors in the ACL module. ')
azcACLSendmsgErr = MibScalar((1, 3, 6, 1, 4, 1, 94, 1, 32, 2, 1, 39), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: azcACLSendmsgErr.setStatus('mandatory')
if mibBuilder.loadTexts: azcACLSendmsgErr.setDescription('The number of sendmsg errors in the ACL module. ')
azcACLRevmsgErr = MibScalar((1, 3, 6, 1, 4, 1, 94, 1, 32, 2, 1, 40), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: azcACLRevmsgErr.setStatus('mandatory')
if mibBuilder.loadTexts: azcACLRevmsgErr.setDescription('The number of recvmsg errors in the ACL module. ')
azcACLRevmsgOverflow = MibScalar((1, 3, 6, 1, 4, 1, 94, 1, 32, 2, 1, 41), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: azcACLRevmsgOverflow.setStatus('mandatory')
if mibBuilder.loadTexts: azcACLRevmsgOverflow.setDescription('The number of recvmsg overflows in the ACL module. ')
azcACLSendmsgLocErr = MibScalar((1, 3, 6, 1, 4, 1, 94, 1, 32, 2, 1, 42), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: azcACLSendmsgLocErr.setStatus('mandatory')
if mibBuilder.loadTexts: azcACLSendmsgLocErr.setDescription('The number of sendmsg errors in the ACL module. ')
azcACLRevmsgLocErr = MibScalar((1, 3, 6, 1, 4, 1, 94, 1, 32, 2, 1, 43), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: azcACLRevmsgLocErr.setStatus('mandatory')
if mibBuilder.loadTexts: azcACLRevmsgLocErr.setDescription('The number of recvmsg errors in the ACL module. ')
azcACLRevmsgLocOverflow = MibScalar((1, 3, 6, 1, 4, 1, 94, 1, 32, 2, 1, 44), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: azcACLRevmsgLocOverflow.setStatus('mandatory')
if mibBuilder.loadTexts: azcACLRevmsgLocOverflow.setDescription('The number of recvmsg overflows in the ACL module. ')
azcACLRevmsgCtlErr = MibScalar((1, 3, 6, 1, 4, 1, 94, 1, 32, 2, 1, 45), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: azcACLRevmsgCtlErr.setStatus('mandatory')
if mibBuilder.loadTexts: azcACLRevmsgCtlErr.setDescription('The number of recvmsg control errors in the ACL module. ')
azcACLRevmsgCtlOverflow = MibScalar((1, 3, 6, 1, 4, 1, 94, 1, 32, 2, 1, 46), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: azcACLRevmsgCtlOverflow.setStatus('mandatory')
if mibBuilder.loadTexts: azcACLRevmsgCtlOverflow.setDescription('The number of recvmsg control overflows in the ACL module. ')
azcACLMemAllocs = MibScalar((1, 3, 6, 1, 4, 1, 94, 1, 32, 2, 1, 47), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: azcACLMemAllocs.setStatus('mandatory')
if mibBuilder.loadTexts: azcACLMemAllocs.setDescription('The number of memory allocations in the ACL module. ')
azcACLMemAllocErr = MibScalar((1, 3, 6, 1, 4, 1, 94, 1, 32, 2, 1, 48), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: azcACLMemAllocErr.setStatus('mandatory')
if mibBuilder.loadTexts: azcACLMemAllocErr.setDescription('The number of memory allocation errors in the ACL module. ')
azcActivationKey = MibScalar((1, 3, 6, 1, 4, 1, 94, 1, 32, 2, 1, 49), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: azcActivationKey.setStatus('mandatory')
if mibBuilder.loadTexts: azcActivationKey.setDescription('AZC activation key. ')
azcHostID = MibScalar((1, 3, 6, 1, 4, 1, 94, 1, 32, 2, 1, 50), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: azcHostID.setStatus('mandatory')
if mibBuilder.loadTexts: azcHostID.setDescription('AZC host ID. ')
azcIntIf = MibScalar((1, 3, 6, 1, 4, 1, 94, 1, 32, 2, 1, 51), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: azcIntIf.setStatus('mandatory')
if mibBuilder.loadTexts: azcIntIf.setDescription('AZC internal interface name. ')
azcExtIf = MibScalar((1, 3, 6, 1, 4, 1, 94, 1, 32, 2, 1, 52), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: azcExtIf.setStatus('mandatory')
if mibBuilder.loadTexts: azcExtIf.setDescription('AZC external interface name. ')
azcMaxTimeout = MibScalar((1, 3, 6, 1, 4, 1, 94, 1, 32, 2, 1, 53), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: azcMaxTimeout.setStatus('mandatory')
if mibBuilder.loadTexts: azcMaxTimeout.setDescription('AZC max session duration in seconds. ')
azcMaxIdleTimeout = MibScalar((1, 3, 6, 1, 4, 1, 94, 1, 32, 2, 1, 54), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: azcMaxIdleTimeout.setStatus('mandatory')
if mibBuilder.loadTexts: azcMaxIdleTimeout.setDescription('AZC max session idle time in seconds. ')
azcPingPeriod = MibScalar((1, 3, 6, 1, 4, 1, 94, 1, 32, 2, 1, 55), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: azcPingPeriod.setStatus('mandatory')
if mibBuilder.loadTexts: azcPingPeriod.setDescription('AZC ping period in seconds. ')
azcLoginURL = MibScalar((1, 3, 6, 1, 4, 1, 94, 1, 32, 2, 1, 56), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: azcLoginURL.setStatus('mandatory')
if mibBuilder.loadTexts: azcLoginURL.setDescription('AZC login URL. ')
azcIPAddress = MibScalar((1, 3, 6, 1, 4, 1, 94, 1, 32, 2, 1, 57), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: azcIPAddress.setStatus('mandatory')
if mibBuilder.loadTexts: azcIPAddress.setDescription('AZC internal IP address. ')
azcExtIPAddress = MibScalar((1, 3, 6, 1, 4, 1, 94, 1, 32, 2, 1, 58), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: azcExtIPAddress.setStatus('mandatory')
if mibBuilder.loadTexts: azcExtIPAddress.setDescription('AZC external IP address. ')
azcDNSIPAddress = MibScalar((1, 3, 6, 1, 4, 1, 94, 1, 32, 2, 1, 59), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: azcDNSIPAddress.setStatus('mandatory')
if mibBuilder.loadTexts: azcDNSIPAddress.setDescription('AZC external DNS proxy IP address. Currently not in use. ')
azcDHCPIPAddress = MibScalar((1, 3, 6, 1, 4, 1, 94, 1, 32, 2, 1, 60), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: azcDHCPIPAddress.setStatus('mandatory')
if mibBuilder.loadTexts: azcDHCPIPAddress.setDescription('AZC DHCP IP Address. ')
azcProxyHost = MibScalar((1, 3, 6, 1, 4, 1, 94, 1, 32, 2, 1, 61), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: azcProxyHost.setStatus('mandatory')
if mibBuilder.loadTexts: azcProxyHost.setDescription('AZC HTTP proxy host address. ')
azcProxyPorts = MibScalar((1, 3, 6, 1, 4, 1, 94, 1, 32, 2, 1, 62), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: azcProxyPorts.setStatus('mandatory')
if mibBuilder.loadTexts: azcProxyPorts.setDescription('AZC HTTP proxy ports. ')
azcMailRelayHost = MibScalar((1, 3, 6, 1, 4, 1, 94, 1, 32, 2, 1, 63), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: azcMailRelayHost.setStatus('mandatory')
if mibBuilder.loadTexts: azcMailRelayHost.setDescription('AZC mail relay host address. ')
azcRADIUSAlivePeriod = MibScalar((1, 3, 6, 1, 4, 1, 94, 1, 32, 2, 1, 64), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: azcRADIUSAlivePeriod.setStatus('mandatory')
if mibBuilder.loadTexts: azcRADIUSAlivePeriod.setDescription('RADIUS accounting-alive period in seconds. ')
azcRADIUSAliveTrigger = MibScalar((1, 3, 6, 1, 4, 1, 94, 1, 32, 2, 1, 65), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: azcRADIUSAliveTrigger.setStatus('mandatory')
if mibBuilder.loadTexts: azcRADIUSAliveTrigger.setDescription('RADIUS accounting-alive trigger size in kilobytes. ')
azcWhitelist = MibScalar((1, 3, 6, 1, 4, 1, 94, 1, 32, 2, 1, 66), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: azcWhitelist.setStatus('mandatory')
if mibBuilder.loadTexts: azcWhitelist.setDescription('AZC whitelist host addresses. ')
azcBlackList = MibScalar((1, 3, 6, 1, 4, 1, 94, 1, 32, 2, 1, 67), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: azcBlackList.setStatus('mandatory')
if mibBuilder.loadTexts: azcBlackList.setDescription('AZC blacklist host addresses. ')
azcDemoAccounts = MibScalar((1, 3, 6, 1, 4, 1, 94, 1, 32, 2, 1, 68), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: azcDemoAccounts.setStatus('mandatory')
if mibBuilder.loadTexts: azcDemoAccounts.setDescription('AZC demo accounts. ')
azcUDPFilter = MibScalar((1, 3, 6, 1, 4, 1, 94, 1, 32, 2, 1, 69), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: azcUDPFilter.setStatus('mandatory')
if mibBuilder.loadTexts: azcUDPFilter.setDescription('AZC UDP filter setting. Value 1 means that ports > 1024 are protected; value -1 means, that only DHCP and DNS are open; value 0 means, that UDP is totally open; values > 1 means, that UDP port greater than the value are open. ')
azcCutTime = MibScalar((1, 3, 6, 1, 4, 1, 94, 1, 32, 2, 1, 70), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: azcCutTime.setStatus('mandatory')
if mibBuilder.loadTexts: azcCutTime.setDescription('AZC session cut-time. ')
azcCutSafetyTime = MibScalar((1, 3, 6, 1, 4, 1, 94, 1, 32, 2, 1, 71), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: azcCutSafetyTime.setStatus('mandatory')
if mibBuilder.loadTexts: azcCutSafetyTime.setDescription('AZC session-cut safety time tolerance in minutes. ')
azcRADIUSActivated = MibScalar((1, 3, 6, 1, 4, 1, 94, 1, 32, 2, 1, 72), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1))).clone(namedValues=NamedValues(("disabled", 0), ("enabled", 1)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: azcRADIUSActivated.setStatus('mandatory')
if mibBuilder.loadTexts: azcRADIUSActivated.setDescription('AZC RADIUS activation state. ')
azcMACCheckMode = MibScalar((1, 3, 6, 1, 4, 1, 94, 1, 32, 2, 1, 73), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1))).clone(namedValues=NamedValues(("disabled", 0), ("enabled", 1)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: azcMACCheckMode.setStatus('mandatory')
if mibBuilder.loadTexts: azcMACCheckMode.setDescription('AZC MAC address check mode. ')
azcNATState = MibScalar((1, 3, 6, 1, 4, 1, 94, 1, 32, 2, 1, 74), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1))).clone(namedValues=NamedValues(("disabled", 0), ("enabled", 1)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: azcNATState.setStatus('mandatory')
if mibBuilder.loadTexts: azcNATState.setDescription('AZC NAT activation state. ')
azcDHCPState = MibScalar((1, 3, 6, 1, 4, 1, 94, 1, 32, 2, 1, 75), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1))).clone(namedValues=NamedValues(("disabled", 0), ("enabled", 1)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: azcDHCPState.setStatus('mandatory')
if mibBuilder.loadTexts: azcDHCPState.setDescription('AZC DHCP activation state. ')
azcSSLState = MibScalar((1, 3, 6, 1, 4, 1, 94, 1, 32, 2, 1, 76), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1))).clone(namedValues=NamedValues(("disabled", 0), ("enabled", 1)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: azcSSLState.setStatus('mandatory')
if mibBuilder.loadTexts: azcSSLState.setDescription('AZC SSL activation state. ')
azcSNMPTrapState = MibScalar((1, 3, 6, 1, 4, 1, 94, 1, 32, 2, 1, 77), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1))).clone(namedValues=NamedValues(("disabled", 0), ("enabled", 1)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: azcSNMPTrapState.setStatus('mandatory')
if mibBuilder.loadTexts: azcSNMPTrapState.setDescription('AZC SNMP trap activation state. ')
azcMACAuthState = MibScalar((1, 3, 6, 1, 4, 1, 94, 1, 32, 2, 1, 78), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1))).clone(namedValues=NamedValues(("disabled", 0), ("enabled", 1)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: azcMACAuthState.setStatus('mandatory')
if mibBuilder.loadTexts: azcMACAuthState.setDescription('AZC MAC authentication state. ')
azcMACRealm = MibScalar((1, 3, 6, 1, 4, 1, 94, 1, 32, 2, 1, 79), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: azcMACRealm.setStatus('mandatory')
if mibBuilder.loadTexts: azcMACRealm.setDescription('AZC MAC authentication realm. ')
azcMACPassword = MibScalar((1, 3, 6, 1, 4, 1, 94, 1, 32, 2, 1, 80), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: azcMACPassword.setStatus('mandatory')
if mibBuilder.loadTexts: azcMACPassword.setDescription('AZC MAC authenticatoin password. ')
azcNATDArgs = MibScalar((1, 3, 6, 1, 4, 1, 94, 1, 32, 2, 1, 81), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: azcNATDArgs.setStatus('mandatory')
if mibBuilder.loadTexts: azcNATDArgs.setDescription('AZC NAT daemon arguments. ')
azcSyslogFacility = MibScalar((1, 3, 6, 1, 4, 1, 94, 1, 32, 2, 1, 82), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: azcSyslogFacility.setStatus('mandatory')
if mibBuilder.loadTexts: azcSyslogFacility.setDescription('AZC syslog facility code. ')
azcSyslogLevel = MibScalar((1, 3, 6, 1, 4, 1, 94, 1, 32, 2, 1, 83), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1, 4, 6))).clone(namedValues=NamedValues(("nothing", 0), ("onlyErrors", 1), ("alsoWarnings", 4), ("alsoInfo", 6)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: azcSyslogLevel.setStatus('mandatory')
if mibBuilder.loadTexts: azcSyslogLevel.setDescription('AZC syslogging level. ')
azcQOSClass1 = MibScalar((1, 3, 6, 1, 4, 1, 94, 1, 32, 2, 1, 84), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: azcQOSClass1.setStatus('mandatory')
if mibBuilder.loadTexts: azcQOSClass1.setDescription("AZC QOS Class 1 (formatted as 'name rateKBps'). ")
azcQOSClass2 = MibScalar((1, 3, 6, 1, 4, 1, 94, 1, 32, 2, 1, 85), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: azcQOSClass2.setStatus('mandatory')
if mibBuilder.loadTexts: azcQOSClass2.setDescription("AZC QOS Class 2 (formatted as 'name rateKBps'). ")
azcQOSClass3 = MibScalar((1, 3, 6, 1, 4, 1, 94, 1, 32, 2, 1, 86), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: azcQOSClass3.setStatus('mandatory')
if mibBuilder.loadTexts: azcQOSClass3.setDescription("AZC QOS Class 3 (formatted as 'name rateKBps'). ")
azcQOSClassDefault = MibScalar((1, 3, 6, 1, 4, 1, 94, 1, 32, 2, 1, 87), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: azcQOSClassDefault.setStatus('mandatory')
if mibBuilder.loadTexts: azcQOSClassDefault.setDescription('AZC default QOS Class (rateKBps). ')
azcLocation = MibScalar((1, 3, 6, 1, 4, 1, 94, 1, 32, 2, 1, 88), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: azcLocation.setStatus('mandatory')
if mibBuilder.loadTexts: azcLocation.setDescription('AZC location string. ')
azcUptime = MibScalar((1, 3, 6, 1, 4, 1, 94, 1, 32, 2, 1, 89), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: azcUptime.setStatus('mandatory')
if mibBuilder.loadTexts: azcUptime.setDescription('Number of seconds since AZC startup. ')
azcTrialTime = MibScalar((1, 3, 6, 1, 4, 1, 94, 1, 32, 2, 1, 90), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: azcTrialTime.setStatus('mandatory')
if mibBuilder.loadTexts: azcTrialTime.setDescription('Free trial time in seconds. ')
azcTrialLockime = MibScalar((1, 3, 6, 1, 4, 1, 94, 1, 32, 2, 1, 91), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: azcTrialLockime.setStatus('mandatory')
if mibBuilder.loadTexts: azcTrialLockime.setDescription('Trial lock time in seconds. ')
azcNokiaAuthMode = MibScalar((1, 3, 6, 1, 4, 1, 94, 1, 32, 2, 1, 92), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: azcNokiaAuthMode.setStatus('mandatory')
if mibBuilder.loadTexts: azcNokiaAuthMode.setDescription('Nokia authentication mode. ')
azcActiveLogins = MibScalar((1, 3, 6, 1, 4, 1, 94, 1, 32, 2, 1, 93), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: azcActiveLogins.setStatus('mandatory')
if mibBuilder.loadTexts: azcActiveLogins.setDescription('Number of logged-in users. ')
azcZoneName = MibScalar((1, 3, 6, 1, 4, 1, 94, 1, 32, 2, 1, 94), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: azcZoneName.setStatus('mandatory')
if mibBuilder.loadTexts: azcZoneName.setDescription('AZC Zone Name. ')
azcLoginTime = MibScalar((1, 3, 6, 1, 4, 1, 94, 1, 32, 2, 1, 95), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: azcLoginTime.setStatus('mandatory')
if mibBuilder.loadTexts: azcLoginTime.setDescription('Average login time (response time) in seconds. ')
mibBuilder.exportSymbols("NOKIA-AZC-SYSTEM-MIB", azcLocation=azcLocation, azcDNSIPAddress=azcDNSIPAddress, azcAutologoffsPing=azcAutologoffsPing, azcSyslogLevel=azcSyslogLevel, azcVersion=azcVersion, azcPktsExtIn=azcPktsExtIn, azcHostID=azcHostID, azcExtIPAddress=azcExtIPAddress, azcPktsNattedOut=azcPktsNattedOut, azcQOSClassDefault=azcQOSClassDefault, azcTrialLockime=azcTrialLockime, azcDHCPIPAddress=azcDHCPIPAddress, azcBytesNattedOut=azcBytesNattedOut, azcMaxTimeout=azcMaxTimeout, azcLoginsDuplFailures=azcLoginsDuplFailures, azcQOSClass1=azcQOSClass1, azcAutologoffsMAC=azcAutologoffsMAC, azcLoginsAuthFailures=azcLoginsAuthFailures, azcACLSendmsgErr=azcACLSendmsgErr, azcActivationKey=azcActivationKey, azcMaxIdleTimeout=azcMaxIdleTimeout, azcBytesNattedErrIn=azcBytesNattedErrIn, azcZoneName=azcZoneName, azcBytesRejInt=azcBytesRejInt, azcProducts=azcProducts, azcUDPFilter=azcUDPFilter, azcLoginTime=azcLoginTime, azcExtIf=azcExtIf, azcNATState=azcNATState, azcPktsRejInt=azcPktsRejInt, azcRADIUSAlivePeriod=azcRADIUSAlivePeriod, azcMACAuthState=azcMACAuthState, azcACLSendmsgLocErr=azcACLSendmsgLocErr, azcPktsNattedIn=azcPktsNattedIn, azcACLRevmsgLocOverflow=azcACLRevmsgLocOverflow, azcActiveLogins=azcActiveLogins, azcBytesExtOut=azcBytesExtOut, nokia=nokia, azcAutologoffsRADIUS=azcAutologoffsRADIUS, azcQOSClass2=azcQOSClass2, azcACLMemAllocs=azcACLMemAllocs, azcACLMemAllocErr=azcACLMemAllocErr, azcTrialTime=azcTrialTime, azcNokiaAuthMode=azcNokiaAuthMode, azcDHCPState=azcDHCPState, azcBlackList=azcBlackList, nokiaProducts=nokiaProducts, azcACLRevmsgLocErr=azcACLRevmsgLocErr, azcBytesIntIn=azcBytesIntIn, azcBytesExtIn=azcBytesExtIn, azcUptime=azcUptime, azcACLRevmsgCtlOverflow=azcACLRevmsgCtlOverflow, azcPktsIntIn=azcPktsIntIn, azcBytesNattedIn=azcBytesNattedIn, azcIPAddress=azcIPAddress, azcMACRealm=azcMACRealm, azcQOSClass3=azcQOSClass3, azcPktsIntOut=azcPktsIntOut, azcProxyPorts=azcProxyPorts, azcAutologoffsACL=azcAutologoffsACL, azcRADIUSActivated=azcRADIUSActivated, azcStatusGroup=azcStatusGroup, azcCutTime=azcCutTime, azcPktsExtOut=azcPktsExtOut, azcPktsNattedErrIn=azcPktsNattedErrIn, azcDemoAccounts=azcDemoAccounts, azcMACCheckMode=azcMACCheckMode, azcACLRevmsgOverflow=azcACLRevmsgOverflow, azcMailRelayHost=azcMailRelayHost, azcStarted=azcStarted, azcACLSelectErr=azcACLSelectErr, azcSSLState=azcSSLState, azcWhitelist=azcWhitelist, azcSyslogFacility=azcSyslogFacility, azcNATDArgs=azcNATDArgs, azcCutSafetyTime=azcCutSafetyTime, azcAutologoffsIdletimer=azcAutologoffsIdletimer, azcAutologoffsMaxTime=azcAutologoffsMaxTime, azcLoginsRADIUSFailures=azcLoginsRADIUSFailures, azcMACPassword=azcMACPassword, azcBytesNattedErrOut=azcBytesNattedErrOut, azcPingPeriod=azcPingPeriod, azcBytesIntOut=azcBytesIntOut, azcLoginsACLFailures=azcLoginsACLFailures, azcLoginsRADIUSACLFailures=azcLoginsRADIUSACLFailures, azcACLRevmsgErr=azcACLRevmsgErr, azcProxyHost=azcProxyHost, azcPktsRejExt=azcPktsRejExt, azcLoginsSpaceFailures=azcLoginsSpaceFailures, azcSNMPTrapState=azcSNMPTrapState, azcBytesRejExt=azcBytesRejExt, azcACLRevmsgCtlErr=azcACLRevmsgCtlErr, azcPktsNattedErrOut=azcPktsNattedErrOut, azcRelease=azcRelease, azcRADIUSAliveTrigger=azcRADIUSAliveTrigger, azcAutologoffsQuota=azcAutologoffsQuota, azcLoginsSuccess=azcLoginsSuccess, azcLoginURL=azcLoginURL, azcIntIf=azcIntIf, azcSystem=azcSystem)
