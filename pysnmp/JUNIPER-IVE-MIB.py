#
# PySNMP MIB module JUNIPER-IVE-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/JUNIPER-IVE-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 19:48:29 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
OctetString, ObjectIdentifier, Integer = mibBuilder.importSymbols("ASN1", "OctetString", "ObjectIdentifier", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsUnion, ValueRangeConstraint, SingleValueConstraint, ValueSizeConstraint, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "ValueRangeConstraint", "SingleValueConstraint", "ValueSizeConstraint", "ConstraintsIntersection")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
ObjectIdentity, Bits, TimeTicks, Unsigned32, ModuleIdentity, enterprises, MibIdentifier, iso, Counter32, Gauge32, Counter64, Integer32, NotificationType, IpAddress, MibScalar, MibTable, MibTableRow, MibTableColumn = mibBuilder.importSymbols("SNMPv2-SMI", "ObjectIdentity", "Bits", "TimeTicks", "Unsigned32", "ModuleIdentity", "enterprises", "MibIdentifier", "iso", "Counter32", "Gauge32", "Counter64", "Integer32", "NotificationType", "IpAddress", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
juniper_ive = ModuleIdentity((1, 3, 6, 1, 4, 1, 12532)).setLabel("juniper-ive")
juniper_ive.setRevisions(('2010-02-22 10:00',))
if mibBuilder.loadTexts: juniper_ive.setLastUpdated('201005180000Z')
if mibBuilder.loadTexts: juniper_ive.setOrganization('Juniper')
logFullPercent = MibScalar((1, 3, 6, 1, 4, 1, 12532, 1), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: logFullPercent.setStatus('current')
signedInWebUsers = MibScalar((1, 3, 6, 1, 4, 1, 12532, 2), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: signedInWebUsers.setStatus('current')
signedInMailUsers = MibScalar((1, 3, 6, 1, 4, 1, 12532, 3), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: signedInMailUsers.setStatus('current')
blockedIP = MibScalar((1, 3, 6, 1, 4, 1, 12532, 4), IpAddress()).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: blockedIP.setStatus('current')
authServerName = MibScalar((1, 3, 6, 1, 4, 1, 12532, 5), OctetString()).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: authServerName.setStatus('current')
productName = MibScalar((1, 3, 6, 1, 4, 1, 12532, 6), OctetString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: productName.setStatus('current')
productVersion = MibScalar((1, 3, 6, 1, 4, 1, 12532, 7), OctetString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: productVersion.setStatus('current')
fileName = MibScalar((1, 3, 6, 1, 4, 1, 12532, 8), OctetString()).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: fileName.setStatus('current')
meetingUserCount = MibScalar((1, 3, 6, 1, 4, 1, 12532, 9), Gauge32()).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: meetingUserCount.setStatus('current')
iveCpuUtil = MibScalar((1, 3, 6, 1, 4, 1, 12532, 10), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: iveCpuUtil.setStatus('current')
iveMemoryUtil = MibScalar((1, 3, 6, 1, 4, 1, 12532, 11), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: iveMemoryUtil.setStatus('current')
iveConcurrentUsers = MibScalar((1, 3, 6, 1, 4, 1, 12532, 12), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: iveConcurrentUsers.setStatus('current')
clusterConcurrentUsers = MibScalar((1, 3, 6, 1, 4, 1, 12532, 13), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: clusterConcurrentUsers.setStatus('current')
iveTotalHits = MibScalar((1, 3, 6, 1, 4, 1, 12532, 14), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: iveTotalHits.setStatus('current')
iveFileHits = MibScalar((1, 3, 6, 1, 4, 1, 12532, 15), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: iveFileHits.setStatus('current')
iveWebHits = MibScalar((1, 3, 6, 1, 4, 1, 12532, 16), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: iveWebHits.setStatus('current')
iveAppletHits = MibScalar((1, 3, 6, 1, 4, 1, 12532, 17), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: iveAppletHits.setStatus('current')
ivetermHits = MibScalar((1, 3, 6, 1, 4, 1, 12532, 18), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ivetermHits.setStatus('current')
iveSAMHits = MibScalar((1, 3, 6, 1, 4, 1, 12532, 19), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: iveSAMHits.setStatus('current')
iveNCHits = MibScalar((1, 3, 6, 1, 4, 1, 12532, 20), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: iveNCHits.setStatus('current')
meetingHits = MibScalar((1, 3, 6, 1, 4, 1, 12532, 21), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: meetingHits.setStatus('current')
meetingCount = MibScalar((1, 3, 6, 1, 4, 1, 12532, 22), Gauge32()).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: meetingCount.setStatus('current')
logName = MibScalar((1, 3, 6, 1, 4, 1, 12532, 23), OctetString()).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: logName.setStatus('current')
iveSwapUtil = MibScalar((1, 3, 6, 1, 4, 1, 12532, 24), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: iveSwapUtil.setStatus('current')
diskFullPercent = MibScalar((1, 3, 6, 1, 4, 1, 12532, 25), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: diskFullPercent.setStatus('current')
blockedIPList = MibTable((1, 3, 6, 1, 4, 1, 12532, 26), ).setMaxAccess("readonly")
if mibBuilder.loadTexts: blockedIPList.setStatus('current')
ipEntry = MibTableRow((1, 3, 6, 1, 4, 1, 12532, 26, 1), ).setIndexNames((0, "JUNIPER-IVE-MIB", "ipIndex"))
if mibBuilder.loadTexts: ipEntry.setStatus('current')
ipIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 12532, 26, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ipIndex.setStatus('current')
ipValue = MibTableColumn((1, 3, 6, 1, 4, 1, 12532, 26, 1, 2), IpAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ipValue.setStatus('current')
logID = MibScalar((1, 3, 6, 1, 4, 1, 12532, 27), OctetString()).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: logID.setStatus('current')
logType = MibScalar((1, 3, 6, 1, 4, 1, 12532, 28), OctetString()).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: logType.setStatus('current')
logDescription = MibScalar((1, 3, 6, 1, 4, 1, 12532, 29), OctetString()).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: logDescription.setStatus('current')
ivsName = MibScalar((1, 3, 6, 1, 4, 1, 12532, 30), OctetString()).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: ivsName.setStatus('current')
ocspResponderURL = MibScalar((1, 3, 6, 1, 4, 1, 12532, 31), OctetString()).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: ocspResponderURL.setStatus('current')
fanDescription = MibScalar((1, 3, 6, 1, 4, 1, 12532, 32), OctetString()).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: fanDescription.setStatus('current')
psDescription = MibScalar((1, 3, 6, 1, 4, 1, 12532, 33), OctetString()).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: psDescription.setStatus('current')
raidDescription = MibScalar((1, 3, 6, 1, 4, 1, 12532, 34), OctetString()).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: raidDescription.setStatus('current')
clusterName = MibScalar((1, 3, 6, 1, 4, 1, 12532, 35), OctetString()).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: clusterName.setStatus('current')
nodeList = MibScalar((1, 3, 6, 1, 4, 1, 12532, 36), OctetString()).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: nodeList.setStatus('current')
vipType = MibScalar((1, 3, 6, 1, 4, 1, 12532, 37), OctetString()).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: vipType.setStatus('current')
currentVIP = MibScalar((1, 3, 6, 1, 4, 1, 12532, 38), OctetString()).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: currentVIP.setStatus('current')
newVIP = MibScalar((1, 3, 6, 1, 4, 1, 12532, 39), OctetString()).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: newVIP.setStatus('current')
nicEvent = MibScalar((1, 3, 6, 1, 4, 1, 12532, 40), OctetString()).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: nicEvent.setStatus('current')
nodeName = MibScalar((1, 3, 6, 1, 4, 1, 12532, 41), OctetString()).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: nodeName.setStatus('current')
iveTemperature = MibScalar((1, 3, 6, 1, 4, 1, 12532, 42), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: iveTemperature.setStatus('current')
iveTraps = MibIdentifier((1, 3, 6, 1, 4, 1, 12532, 251))
iveLogNearlyFull = NotificationType((1, 3, 6, 1, 4, 1, 12532, 251, 4)).setObjects(("JUNIPER-IVE-MIB", "logFullPercent"), ("JUNIPER-IVE-MIB", "logName"))
if mibBuilder.loadTexts: iveLogNearlyFull.setStatus('current')
iveLogFull = NotificationType((1, 3, 6, 1, 4, 1, 12532, 251, 5)).setObjects(("JUNIPER-IVE-MIB", "logName"))
if mibBuilder.loadTexts: iveLogFull.setStatus('current')
iveMaxConcurrentUsersSignedIn = NotificationType((1, 3, 6, 1, 4, 1, 12532, 251, 6))
if mibBuilder.loadTexts: iveMaxConcurrentUsersSignedIn.setStatus('current')
iveTooManyFailedLoginAttempts = NotificationType((1, 3, 6, 1, 4, 1, 12532, 251, 7)).setObjects(("JUNIPER-IVE-MIB", "blockedIP"))
if mibBuilder.loadTexts: iveTooManyFailedLoginAttempts.setStatus('current')
externalAuthServerUnreachable = NotificationType((1, 3, 6, 1, 4, 1, 12532, 251, 8)).setObjects(("JUNIPER-IVE-MIB", "authServerName"))
if mibBuilder.loadTexts: externalAuthServerUnreachable.setStatus('current')
iveStart = NotificationType((1, 3, 6, 1, 4, 1, 12532, 251, 9))
if mibBuilder.loadTexts: iveStart.setStatus('current')
iveShutdown = NotificationType((1, 3, 6, 1, 4, 1, 12532, 251, 10))
if mibBuilder.loadTexts: iveShutdown.setStatus('current')
iveReboot = NotificationType((1, 3, 6, 1, 4, 1, 12532, 251, 11))
if mibBuilder.loadTexts: iveReboot.setStatus('current')
archiveServerUnreachable = NotificationType((1, 3, 6, 1, 4, 1, 12532, 251, 12))
if mibBuilder.loadTexts: archiveServerUnreachable.setStatus('current')
archiveServerLoginFailed = NotificationType((1, 3, 6, 1, 4, 1, 12532, 251, 13))
if mibBuilder.loadTexts: archiveServerLoginFailed.setStatus('current')
archiveFileTransferFailed = NotificationType((1, 3, 6, 1, 4, 1, 12532, 251, 14)).setObjects(("JUNIPER-IVE-MIB", "fileName"))
if mibBuilder.loadTexts: archiveFileTransferFailed.setStatus('current')
meetingUserLimit = NotificationType((1, 3, 6, 1, 4, 1, 12532, 251, 15)).setObjects(("JUNIPER-IVE-MIB", "meetingUserCount"))
if mibBuilder.loadTexts: meetingUserLimit.setStatus('current')
iveRestart = NotificationType((1, 3, 6, 1, 4, 1, 12532, 251, 16))
if mibBuilder.loadTexts: iveRestart.setStatus('current')
meetingLimit = NotificationType((1, 3, 6, 1, 4, 1, 12532, 251, 17)).setObjects(("JUNIPER-IVE-MIB", "meetingCount"))
if mibBuilder.loadTexts: meetingLimit.setStatus('current')
iveDiskNearlyFull = NotificationType((1, 3, 6, 1, 4, 1, 12532, 251, 18)).setObjects(("JUNIPER-IVE-MIB", "diskFullPercent"))
if mibBuilder.loadTexts: iveDiskNearlyFull.setStatus('current')
iveDiskFull = NotificationType((1, 3, 6, 1, 4, 1, 12532, 251, 19))
if mibBuilder.loadTexts: iveDiskFull.setStatus('current')
logMessageTrap = NotificationType((1, 3, 6, 1, 4, 1, 12532, 251, 20)).setObjects(("JUNIPER-IVE-MIB", "logID"), ("JUNIPER-IVE-MIB", "logType"), ("JUNIPER-IVE-MIB", "logDescription"))
if mibBuilder.loadTexts: logMessageTrap.setStatus('current')
memUtilNotify = NotificationType((1, 3, 6, 1, 4, 1, 12532, 251, 21)).setObjects(("JUNIPER-IVE-MIB", "iveMemoryUtil"))
if mibBuilder.loadTexts: memUtilNotify.setStatus('current')
cpuUtilNotify = NotificationType((1, 3, 6, 1, 4, 1, 12532, 251, 22)).setObjects(("JUNIPER-IVE-MIB", "iveCpuUtil"))
if mibBuilder.loadTexts: cpuUtilNotify.setStatus('current')
swapUtilNotify = NotificationType((1, 3, 6, 1, 4, 1, 12532, 251, 23)).setObjects(("JUNIPER-IVE-MIB", "iveSwapUtil"))
if mibBuilder.loadTexts: swapUtilNotify.setStatus('current')
iveMaxConcurrentUsersVirtualSystem = NotificationType((1, 3, 6, 1, 4, 1, 12532, 251, 24)).setObjects(("JUNIPER-IVE-MIB", "ivsName"))
if mibBuilder.loadTexts: iveMaxConcurrentUsersVirtualSystem.setStatus('current')
ocspResponderConnectionFailed = NotificationType((1, 3, 6, 1, 4, 1, 12532, 251, 25)).setObjects(("JUNIPER-IVE-MIB", "ocspResponderURL"))
if mibBuilder.loadTexts: ocspResponderConnectionFailed.setStatus('current')
iveFanNotify = NotificationType((1, 3, 6, 1, 4, 1, 12532, 251, 26)).setObjects(("JUNIPER-IVE-MIB", "fanDescription"))
if mibBuilder.loadTexts: iveFanNotify.setStatus('current')
ivePowerSupplyNotify = NotificationType((1, 3, 6, 1, 4, 1, 12532, 251, 27)).setObjects(("JUNIPER-IVE-MIB", "psDescription"))
if mibBuilder.loadTexts: ivePowerSupplyNotify.setStatus('current')
iveRaidNotify = NotificationType((1, 3, 6, 1, 4, 1, 12532, 251, 28)).setObjects(("JUNIPER-IVE-MIB", "raidDescription"))
if mibBuilder.loadTexts: iveRaidNotify.setStatus('current')
iveClusterDisableNodeTrap = NotificationType((1, 3, 6, 1, 4, 1, 12532, 251, 29)).setObjects(("JUNIPER-IVE-MIB", "clusterName"), ("JUNIPER-IVE-MIB", "nodeList"))
if mibBuilder.loadTexts: iveClusterDisableNodeTrap.setStatus('current')
iveClusterChangedVIPTrap = NotificationType((1, 3, 6, 1, 4, 1, 12532, 251, 30)).setObjects(("JUNIPER-IVE-MIB", "vipType"), ("JUNIPER-IVE-MIB", "currentVIP"), ("JUNIPER-IVE-MIB", "newVIP"))
if mibBuilder.loadTexts: iveClusterChangedVIPTrap.setStatus('current')
iveNetExternalInterfaceDownTrap = NotificationType((1, 3, 6, 1, 4, 1, 12532, 251, 31)).setObjects(("JUNIPER-IVE-MIB", "nicEvent"))
if mibBuilder.loadTexts: iveNetExternalInterfaceDownTrap.setStatus('current')
iveClusterDeleteTrap = NotificationType((1, 3, 6, 1, 4, 1, 12532, 251, 32)).setObjects(("JUNIPER-IVE-MIB", "nodeName"))
if mibBuilder.loadTexts: iveClusterDeleteTrap.setStatus('current')
iveNetInternalInterfaceDownTrap = NotificationType((1, 3, 6, 1, 4, 1, 12532, 251, 33)).setObjects(("JUNIPER-IVE-MIB", "nicEvent"))
if mibBuilder.loadTexts: iveNetInternalInterfaceDownTrap.setStatus('current')
iveNetManagementInterfaceDownTrap = NotificationType((1, 3, 6, 1, 4, 1, 12532, 251, 34)).setObjects(("JUNIPER-IVE-MIB", "nicEvent"))
if mibBuilder.loadTexts: iveNetManagementInterfaceDownTrap.setStatus('current')
iveTemperatureNotify = NotificationType((1, 3, 6, 1, 4, 1, 12532, 251, 35)).setObjects(("JUNIPER-IVE-MIB", "iveTemperature"))
if mibBuilder.loadTexts: iveTemperatureNotify.setStatus('current')
iveSAProduct = MibIdentifier((1, 3, 6, 1, 4, 1, 12532, 252))
iveICProduct = MibIdentifier((1, 3, 6, 1, 4, 1, 12532, 253))
iveMAGProduct = MibIdentifier((1, 3, 6, 1, 4, 1, 12532, 254))
iveProductSA700 = MibIdentifier((1, 3, 6, 1, 4, 1, 12532, 252, 1))
iveProductSA2000 = MibIdentifier((1, 3, 6, 1, 4, 1, 12532, 252, 2))
iveProductSA2500 = MibIdentifier((1, 3, 6, 1, 4, 1, 12532, 252, 3))
iveProductSA4000 = MibIdentifier((1, 3, 6, 1, 4, 1, 12532, 252, 4))
iveProductSA4500 = MibIdentifier((1, 3, 6, 1, 4, 1, 12532, 252, 5))
iveProductSA6000 = MibIdentifier((1, 3, 6, 1, 4, 1, 12532, 252, 6))
iveProductSA6500 = MibIdentifier((1, 3, 6, 1, 4, 1, 12532, 252, 7))
iveProductIC4000 = MibIdentifier((1, 3, 6, 1, 4, 1, 12532, 253, 1))
iveProductIC4500 = MibIdentifier((1, 3, 6, 1, 4, 1, 12532, 253, 2))
iveProductIC6000 = MibIdentifier((1, 3, 6, 1, 4, 1, 12532, 253, 3))
iveProductIC6500 = MibIdentifier((1, 3, 6, 1, 4, 1, 12532, 253, 4))
iveProductMAG2600 = MibIdentifier((1, 3, 6, 1, 4, 1, 12532, 254, 1))
iveProductMAG4610 = MibIdentifier((1, 3, 6, 1, 4, 1, 12532, 254, 2))
iveProductSM160 = MibIdentifier((1, 3, 6, 1, 4, 1, 12532, 254, 3))
iveProductSM360 = MibIdentifier((1, 3, 6, 1, 4, 1, 12532, 254, 4))
iveSA700 = MibIdentifier((1, 3, 6, 1, 4, 1, 12532, 252, 1, 1))
iveSA2000 = MibIdentifier((1, 3, 6, 1, 4, 1, 12532, 252, 2, 1))
iveSA2500 = MibIdentifier((1, 3, 6, 1, 4, 1, 12532, 252, 3, 1))
iveSA4000 = MibIdentifier((1, 3, 6, 1, 4, 1, 12532, 252, 4, 1))
iveSA4500 = MibIdentifier((1, 3, 6, 1, 4, 1, 12532, 252, 5, 1))
iveSA4000FIPS = MibIdentifier((1, 3, 6, 1, 4, 1, 12532, 252, 4, 2))
iveSA4500FIPS = MibIdentifier((1, 3, 6, 1, 4, 1, 12532, 252, 5, 2))
iveSA6000 = MibIdentifier((1, 3, 6, 1, 4, 1, 12532, 252, 6, 1))
iveSA6500 = MibIdentifier((1, 3, 6, 1, 4, 1, 12532, 252, 7, 1))
iveSA6000FIPS = MibIdentifier((1, 3, 6, 1, 4, 1, 12532, 252, 6, 2))
iveSA6500FIPS = MibIdentifier((1, 3, 6, 1, 4, 1, 12532, 252, 7, 2))
iveIC4000 = MibIdentifier((1, 3, 6, 1, 4, 1, 12532, 253, 1, 1))
iveIC6000 = MibIdentifier((1, 3, 6, 1, 4, 1, 12532, 253, 3, 1))
iveIC4500 = MibIdentifier((1, 3, 6, 1, 4, 1, 12532, 253, 2, 1))
iveIC6500 = MibIdentifier((1, 3, 6, 1, 4, 1, 12532, 253, 4, 1))
iveIC6000FIPS = MibIdentifier((1, 3, 6, 1, 4, 1, 12532, 253, 3, 2))
iveMAG2600 = MibIdentifier((1, 3, 6, 1, 4, 1, 12532, 254, 1, 1))
iveMAG4610 = MibIdentifier((1, 3, 6, 1, 4, 1, 12532, 254, 2, 1))
iveMAGSM160 = MibIdentifier((1, 3, 6, 1, 4, 1, 12532, 254, 3, 1))
iveMAGSM360 = MibIdentifier((1, 3, 6, 1, 4, 1, 12532, 254, 4, 1))
mibBuilder.exportSymbols("JUNIPER-IVE-MIB", iveLogNearlyFull=iveLogNearlyFull, iveSAProduct=iveSAProduct, blockedIP=blockedIP, clusterConcurrentUsers=clusterConcurrentUsers, ivsName=ivsName, nicEvent=nicEvent, iveSA6000=iveSA6000, logFullPercent=logFullPercent, ipEntry=ipEntry, ocspResponderURL=ocspResponderURL, iveIC6000=iveIC6000, ipIndex=ipIndex, signedInMailUsers=signedInMailUsers, iveMAGSM160=iveMAGSM160, iveSA2000=iveSA2000, vipType=vipType, iveFileHits=iveFileHits, iveNetInternalInterfaceDownTrap=iveNetInternalInterfaceDownTrap, iveSA2500=iveSA2500, iveProductSM360=iveProductSM360, logName=logName, iveSA6500=iveSA6500, iveProductSA6000=iveProductSA6000, iveIC4500=iveIC4500, externalAuthServerUnreachable=externalAuthServerUnreachable, iveClusterChangedVIPTrap=iveClusterChangedVIPTrap, meetingUserLimit=meetingUserLimit, meetingLimit=meetingLimit, iveProductSA2500=iveProductSA2500, iveMAG2600=iveMAG2600, raidDescription=raidDescription, iveSA4000FIPS=iveSA4000FIPS, logType=logType, iveProductSA2000=iveProductSA2000, PYSNMP_MODULE_ID=juniper_ive, iveSA4000=iveSA4000, swapUtilNotify=swapUtilNotify, archiveServerLoginFailed=archiveServerLoginFailed, iveClusterDeleteTrap=iveClusterDeleteTrap, fanDescription=fanDescription, iveSwapUtil=iveSwapUtil, archiveFileTransferFailed=archiveFileTransferFailed, iveSA700=iveSA700, currentVIP=currentVIP, iveSA4500=iveSA4500, fileName=fileName, iveTemperatureNotify=iveTemperatureNotify, iveMaxConcurrentUsersSignedIn=iveMaxConcurrentUsersSignedIn, clusterName=clusterName, blockedIPList=blockedIPList, iveIC6500=iveIC6500, ipValue=ipValue, iveProductSA4000=iveProductSA4000, iveCpuUtil=iveCpuUtil, authServerName=authServerName, iveProductSA6500=iveProductSA6500, signedInWebUsers=signedInWebUsers, meetingHits=meetingHits, iveTraps=iveTraps, iveProductMAG2600=iveProductMAG2600, iveProductIC4500=iveProductIC4500, logID=logID, iveNetExternalInterfaceDownTrap=iveNetExternalInterfaceDownTrap, juniper_ive=juniper_ive, iveDiskFull=iveDiskFull, iveSAMHits=iveSAMHits, iveRestart=iveRestart, iveProductSM160=iveProductSM160, iveMAGSM360=iveMAGSM360, iveAppletHits=iveAppletHits, iveReboot=iveReboot, iveFanNotify=iveFanNotify, iveMemoryUtil=iveMemoryUtil, iveProductIC4000=iveProductIC4000, iveMAG4610=iveMAG4610, iveProductIC6000=iveProductIC6000, psDescription=psDescription, nodeName=nodeName, logMessageTrap=logMessageTrap, iveTotalHits=iveTotalHits, iveTooManyFailedLoginAttempts=iveTooManyFailedLoginAttempts, iveIC4000=iveIC4000, iveMAGProduct=iveMAGProduct, iveShutdown=iveShutdown, iveTemperature=iveTemperature, diskFullPercent=diskFullPercent, iveProductIC6500=iveProductIC6500, nodeList=nodeList, meetingUserCount=meetingUserCount, iveMaxConcurrentUsersVirtualSystem=iveMaxConcurrentUsersVirtualSystem, iveSA6500FIPS=iveSA6500FIPS, iveNCHits=iveNCHits, iveNetManagementInterfaceDownTrap=iveNetManagementInterfaceDownTrap, iveRaidNotify=iveRaidNotify, meetingCount=meetingCount, iveSA4500FIPS=iveSA4500FIPS, iveSA6000FIPS=iveSA6000FIPS, iveIC6000FIPS=iveIC6000FIPS, iveStart=iveStart, ivePowerSupplyNotify=ivePowerSupplyNotify, iveDiskNearlyFull=iveDiskNearlyFull, iveClusterDisableNodeTrap=iveClusterDisableNodeTrap, iveProductSA700=iveProductSA700, newVIP=newVIP, memUtilNotify=memUtilNotify, archiveServerUnreachable=archiveServerUnreachable, productVersion=productVersion, ocspResponderConnectionFailed=ocspResponderConnectionFailed, iveWebHits=iveWebHits, iveLogFull=iveLogFull, iveProductSA4500=iveProductSA4500, ivetermHits=ivetermHits, productName=productName, iveConcurrentUsers=iveConcurrentUsers, iveICProduct=iveICProduct, iveProductMAG4610=iveProductMAG4610, cpuUtilNotify=cpuUtilNotify, logDescription=logDescription)