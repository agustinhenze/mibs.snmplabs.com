#
# PySNMP MIB module RM-TRAP-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/RM-TRAP-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 20:49:37 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
host, curSize, memUsage, load, cpuUsage, percentage, processID, disk, processName, file, maxSize, status = mibBuilder.importSymbols("AGGREGATED-EXT-MIB", "host", "curSize", "memUsage", "load", "cpuUsage", "percentage", "processID", "disk", "processName", "file", "maxSize", "status")
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
SingleValueConstraint, ValueSizeConstraint, ConstraintsIntersection, ValueRangeConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "SingleValueConstraint", "ValueSizeConstraint", "ConstraintsIntersection", "ValueRangeConstraint", "ConstraintsUnion")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
TimeTicks, Counter64, NotificationType, iso, IpAddress, Counter32, MibScalar, MibTable, MibTableRow, MibTableColumn, snmpModules, Bits, ObjectIdentity, ObjectName, MibIdentifier, enterprises, Gauge32, Integer32, ModuleIdentity, Unsigned32 = mibBuilder.importSymbols("SNMPv2-SMI", "TimeTicks", "Counter64", "NotificationType", "iso", "IpAddress", "Counter32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "snmpModules", "Bits", "ObjectIdentity", "ObjectName", "MibIdentifier", "enterprises", "Gauge32", "Integer32", "ModuleIdentity", "Unsigned32")
TruthValue, TestAndIncr, DisplayString, TextualConvention, RowStatus, TimeStamp = mibBuilder.importSymbols("SNMPv2-TC", "TruthValue", "TestAndIncr", "DisplayString", "TextualConvention", "RowStatus", "TimeStamp")
lucent = MibIdentifier((1, 3, 6, 1, 4, 1, 1751))
products = MibIdentifier((1, 3, 6, 1, 4, 1, 1751, 1))
softSwitch = MibIdentifier((1, 3, 6, 1, 4, 1, 1751, 1, 1198))
resourceMonitor = MibIdentifier((1, 3, 6, 1, 4, 1, 1751, 1, 1198, 4))
rmTraps = ModuleIdentity((1, 3, 6, 1, 4, 1, 1751, 1, 1198, 4, 0))
if mibBuilder.loadTexts: rmTraps.setLastUpdated('240701')
if mibBuilder.loadTexts: rmTraps.setOrganization('Lucent Technologies')
cpuUtilWarning = NotificationType((1, 3, 6, 1, 4, 1, 1751, 1, 1198, 4, 0, 0)).setObjects(("AGGREGATED-EXT-MIB", "host"), ("AGGREGATED-EXT-MIB", "percentage"))
if mibBuilder.loadTexts: cpuUtilWarning.setStatus('current')
cpuUtilAlarm = NotificationType((1, 3, 6, 1, 4, 1, 1751, 1, 1198, 4, 0, 1)).setObjects(("AGGREGATED-EXT-MIB", "host"), ("AGGREGATED-EXT-MIB", "percentage"))
if mibBuilder.loadTexts: cpuUtilAlarm.setStatus('current')
cpuUtilInform = NotificationType((1, 3, 6, 1, 4, 1, 1751, 1, 1198, 4, 0, 2)).setObjects(("AGGREGATED-EXT-MIB", "host"), ("AGGREGATED-EXT-MIB", "percentage"), ("AGGREGATED-EXT-MIB", "status"))
if mibBuilder.loadTexts: cpuUtilInform.setStatus('current')
cpuLoadWarning = NotificationType((1, 3, 6, 1, 4, 1, 1751, 1, 1198, 4, 0, 3)).setObjects(("AGGREGATED-EXT-MIB", "host"), ("AGGREGATED-EXT-MIB", "load"))
if mibBuilder.loadTexts: cpuLoadWarning.setStatus('current')
cpuLoadAlarm = NotificationType((1, 3, 6, 1, 4, 1, 1751, 1, 1198, 4, 0, 4)).setObjects(("AGGREGATED-EXT-MIB", "host"), ("AGGREGATED-EXT-MIB", "load"))
if mibBuilder.loadTexts: cpuLoadAlarm.setStatus('current')
cpuLoadInform = NotificationType((1, 3, 6, 1, 4, 1, 1751, 1, 1198, 4, 0, 5)).setObjects(("AGGREGATED-EXT-MIB", "host"), ("AGGREGATED-EXT-MIB", "load"), ("AGGREGATED-EXT-MIB", "status"))
if mibBuilder.loadTexts: cpuLoadInform.setStatus('current')
diskUsageWarning = NotificationType((1, 3, 6, 1, 4, 1, 1751, 1, 1198, 4, 0, 6)).setObjects(("AGGREGATED-EXT-MIB", "disk"), ("AGGREGATED-EXT-MIB", "percentage"))
if mibBuilder.loadTexts: diskUsageWarning.setStatus('current')
diskUsageAlarm = NotificationType((1, 3, 6, 1, 4, 1, 1751, 1, 1198, 4, 0, 7)).setObjects(("AGGREGATED-EXT-MIB", "disk"), ("AGGREGATED-EXT-MIB", "percentage"))
if mibBuilder.loadTexts: diskUsageAlarm.setStatus('current')
diskUsageInform = NotificationType((1, 3, 6, 1, 4, 1, 1751, 1, 1198, 4, 0, 8)).setObjects(("AGGREGATED-EXT-MIB", "disk"), ("AGGREGATED-EXT-MIB", "percentage"), ("AGGREGATED-EXT-MIB", "status"))
if mibBuilder.loadTexts: diskUsageInform.setStatus('current')
fileSizeEvent = NotificationType((1, 3, 6, 1, 4, 1, 1751, 1, 1198, 4, 0, 9)).setObjects(("AGGREGATED-EXT-MIB", "file"), ("AGGREGATED-EXT-MIB", "curSize"), ("AGGREGATED-EXT-MIB", "maxSize"))
if mibBuilder.loadTexts: fileSizeEvent.setStatus('current')
unixProcessDied = NotificationType((1, 3, 6, 1, 4, 1, 1751, 1, 1198, 4, 0, 10)).setObjects(("AGGREGATED-EXT-MIB", "host"), ("AGGREGATED-EXT-MIB", "processName"), ("AGGREGATED-EXT-MIB", "processID"))
if mibBuilder.loadTexts: unixProcessDied.setStatus('current')
procCpuAlarm = NotificationType((1, 3, 6, 1, 4, 1, 1751, 1, 1198, 4, 0, 11)).setObjects(("AGGREGATED-EXT-MIB", "host"), ("AGGREGATED-EXT-MIB", "processName"), ("AGGREGATED-EXT-MIB", "processID"), ("AGGREGATED-EXT-MIB", "cpuUsage"))
if mibBuilder.loadTexts: procCpuAlarm.setStatus('current')
procCpuWarn = NotificationType((1, 3, 6, 1, 4, 1, 1751, 1, 1198, 4, 0, 12)).setObjects(("AGGREGATED-EXT-MIB", "host"), ("AGGREGATED-EXT-MIB", "processName"), ("AGGREGATED-EXT-MIB", "processID"), ("AGGREGATED-EXT-MIB", "cpuUsage"))
if mibBuilder.loadTexts: procCpuWarn.setStatus('current')
procMemAlarm = NotificationType((1, 3, 6, 1, 4, 1, 1751, 1, 1198, 4, 0, 13)).setObjects(("AGGREGATED-EXT-MIB", "host"), ("AGGREGATED-EXT-MIB", "processName"), ("AGGREGATED-EXT-MIB", "processID"), ("AGGREGATED-EXT-MIB", "memUsage"))
if mibBuilder.loadTexts: procMemAlarm.setStatus('current')
procCpuInform = NotificationType((1, 3, 6, 1, 4, 1, 1751, 1, 1198, 4, 0, 14)).setObjects(("AGGREGATED-EXT-MIB", "host"), ("AGGREGATED-EXT-MIB", "processName"), ("AGGREGATED-EXT-MIB", "processID"))
if mibBuilder.loadTexts: procCpuInform.setStatus('current')
procMemInform = NotificationType((1, 3, 6, 1, 4, 1, 1751, 1, 1198, 4, 0, 15)).setObjects(("AGGREGATED-EXT-MIB", "host"), ("AGGREGATED-EXT-MIB", "processName"), ("AGGREGATED-EXT-MIB", "processID"))
if mibBuilder.loadTexts: procMemInform.setStatus('current')
mibBuilder.exportSymbols("RM-TRAP-MIB", rmTraps=rmTraps, cpuUtilAlarm=cpuUtilAlarm, cpuUtilInform=cpuUtilInform, lucent=lucent, PYSNMP_MODULE_ID=rmTraps, diskUsageInform=diskUsageInform, fileSizeEvent=fileSizeEvent, cpuLoadAlarm=cpuLoadAlarm, cpuLoadWarning=cpuLoadWarning, procMemAlarm=procMemAlarm, procMemInform=procMemInform, procCpuInform=procCpuInform, unixProcessDied=unixProcessDied, diskUsageWarning=diskUsageWarning, cpuUtilWarning=cpuUtilWarning, softSwitch=softSwitch, resourceMonitor=resourceMonitor, cpuLoadInform=cpuLoadInform, diskUsageAlarm=diskUsageAlarm, products=products, procCpuWarn=procCpuWarn, procCpuAlarm=procCpuAlarm)