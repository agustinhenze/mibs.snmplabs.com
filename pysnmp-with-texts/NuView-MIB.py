#
# PySNMP MIB module NuView-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/NuView-MIB
# Produced by pysmi-0.3.4 at Wed May  1 14:32:00 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
ObjectIdentifier, Integer, OctetString = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "Integer", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsUnion, SingleValueConstraint, ValueRangeConstraint, ConstraintsIntersection, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "SingleValueConstraint", "ValueRangeConstraint", "ConstraintsIntersection", "ValueSizeConstraint")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
NotificationType, enterprises, Unsigned32, iso, Counter64, ObjectIdentity, IpAddress, Bits, Integer32, TimeTicks, NotificationType, MibScalar, MibTable, MibTableRow, MibTableColumn, Gauge32, MibIdentifier, Counter32, ModuleIdentity = mibBuilder.importSymbols("SNMPv2-SMI", "NotificationType", "enterprises", "Unsigned32", "iso", "Counter64", "ObjectIdentity", "IpAddress", "Bits", "Integer32", "TimeTicks", "NotificationType", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Gauge32", "MibIdentifier", "Counter32", "ModuleIdentity")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
NuView = MibIdentifier((1, 3, 6, 1, 4, 1, 2427))
ClusterX = MibIdentifier((1, 3, 6, 1, 4, 1, 2427, 2))
clxMibStats = MibIdentifier((1, 3, 6, 1, 4, 1, 2427, 2, 1))
clxTrapData = MibIdentifier((1, 3, 6, 1, 4, 1, 2427, 2, 2))
clxMibStatsMajRev = MibScalar((1, 3, 6, 1, 4, 1, 2427, 2, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 65535))).setMaxAccess("readonly")
if mibBuilder.loadTexts: clxMibStatsMajRev.setStatus('mandatory')
if mibBuilder.loadTexts: clxMibStatsMajRev.setDescription('The major revision level of the ClusterX SNMP extension agent MIB.')
clxMibStatsMinRev = MibScalar((1, 3, 6, 1, 4, 1, 2427, 2, 1, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 65535))).setMaxAccess("readonly")
if mibBuilder.loadTexts: clxMibStatsMinRev.setStatus('mandatory')
if mibBuilder.loadTexts: clxMibStatsMinRev.setDescription('The minor revision level of the ClusterX SNMP extension agent MIB.')
clxMibStatsVendorName = MibScalar((1, 3, 6, 1, 4, 1, 2427, 2, 1, 3), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: clxMibStatsVendorName.setStatus('mandatory')
if mibBuilder.loadTexts: clxMibStatsVendorName.setDescription('The name of the vendor supplying the ClusterX SNMP extension agent MIB.')
clxTrapDataString01 = MibScalar((1, 3, 6, 1, 4, 1, 2427, 2, 2, 1), DisplayString())
if mibBuilder.loadTexts: clxTrapDataString01.setStatus('mandatory')
if mibBuilder.loadTexts: clxTrapDataString01.setDescription('Custom string 1 (Varbind #1) for NuView ClusterX trap.')
clxTrapDataNodeName = MibScalar((1, 3, 6, 1, 4, 1, 2427, 2, 2, 2), DisplayString())
if mibBuilder.loadTexts: clxTrapDataNodeName.setStatus('mandatory')
if mibBuilder.loadTexts: clxTrapDataNodeName.setDescription('Name of the MSCS Node. ')
clxTrapDataClusterName = MibScalar((1, 3, 6, 1, 4, 1, 2427, 2, 2, 3), DisplayString())
if mibBuilder.loadTexts: clxTrapDataClusterName.setStatus('mandatory')
if mibBuilder.loadTexts: clxTrapDataClusterName.setDescription('Name of the MSCS Cluster. ')
clxTrapDataResourceName = MibScalar((1, 3, 6, 1, 4, 1, 2427, 2, 2, 4), DisplayString())
if mibBuilder.loadTexts: clxTrapDataResourceName.setStatus('mandatory')
if mibBuilder.loadTexts: clxTrapDataResourceName.setDescription('Name of the MSCS Resource. ')
clxTrapDataResourceType = MibScalar((1, 3, 6, 1, 4, 1, 2427, 2, 2, 5), DisplayString())
if mibBuilder.loadTexts: clxTrapDataResourceType.setStatus('mandatory')
if mibBuilder.loadTexts: clxTrapDataResourceType.setDescription('Type of the MSCS Resource. ')
clxTrapDataSeverityValue = MibScalar((1, 3, 6, 1, 4, 1, 2427, 2, 2, 6), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1, 2))).clone(namedValues=NamedValues(("info", 0), ("warning", 1), ("error", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: clxTrapDataSeverityValue.setStatus('mandatory')
if mibBuilder.loadTexts: clxTrapDataSeverityValue.setDescription('The severity value type.')
clxTrapDataNetwork = MibScalar((1, 3, 6, 1, 4, 1, 2427, 2, 2, 7), DisplayString())
if mibBuilder.loadTexts: clxTrapDataNetwork.setStatus('mandatory')
if mibBuilder.loadTexts: clxTrapDataNetwork.setDescription('Network Info ')
clxTrapEventDate = MibScalar((1, 3, 6, 1, 4, 1, 2427, 2, 2, 8), DisplayString())
if mibBuilder.loadTexts: clxTrapEventDate.setStatus('mandatory')
if mibBuilder.loadTexts: clxTrapEventDate.setDescription('Date of the Event created in NT event log file ')
clxTrapEventTime = MibScalar((1, 3, 6, 1, 4, 1, 2427, 2, 2, 9), DisplayString())
if mibBuilder.loadTexts: clxTrapEventTime.setStatus('mandatory')
if mibBuilder.loadTexts: clxTrapEventTime.setDescription('Time of the Event created in NT event log file ')
clxTrapEventSource = MibScalar((1, 3, 6, 1, 4, 1, 2427, 2, 2, 10), DisplayString())
if mibBuilder.loadTexts: clxTrapEventSource.setStatus('mandatory')
if mibBuilder.loadTexts: clxTrapEventSource.setDescription('Source of the Event created in NT event log file ')
clxTrapEventCategory = MibScalar((1, 3, 6, 1, 4, 1, 2427, 2, 2, 11), DisplayString())
if mibBuilder.loadTexts: clxTrapEventCategory.setStatus('mandatory')
if mibBuilder.loadTexts: clxTrapEventCategory.setDescription('Category of the Event created in NT event log file ')
clxTrapEventID = MibScalar((1, 3, 6, 1, 4, 1, 2427, 2, 2, 12), DisplayString())
if mibBuilder.loadTexts: clxTrapEventID.setStatus('mandatory')
if mibBuilder.loadTexts: clxTrapEventID.setDescription('ID of the Event created in NT event log file')
clxTrapEventUser = MibScalar((1, 3, 6, 1, 4, 1, 2427, 2, 2, 13), DisplayString())
if mibBuilder.loadTexts: clxTrapEventUser.setStatus('mandatory')
if mibBuilder.loadTexts: clxTrapEventUser.setDescription('User which created the event in NT event log file ')
clxTrapEventComputer = MibScalar((1, 3, 6, 1, 4, 1, 2427, 2, 2, 14), DisplayString())
if mibBuilder.loadTexts: clxTrapEventComputer.setStatus('mandatory')
if mibBuilder.loadTexts: clxTrapEventComputer.setDescription('Computer which created Event in NT event log file')
clxTrapDataNetworkName = MibScalar((1, 3, 6, 1, 4, 1, 2427, 2, 2, 15), DisplayString())
if mibBuilder.loadTexts: clxTrapDataNetworkName.setStatus('mandatory')
if mibBuilder.loadTexts: clxTrapDataNetworkName.setDescription('Network Name')
NuViewTrapStr = NotificationType((1, 3, 6, 1, 4, 1, 2427) + (0,1)).setObjects(("NuView-MIB", "clxTrapDataString01"))
if mibBuilder.loadTexts: NuViewTrapStr.setDescription('Generic SNMP trap generated by NuView applications and services. Varbind #1: Custom string.')
ClusterXTrapStr = NotificationType((1, 3, 6, 1, 4, 1, 2427, 2) + (0,1)).setObjects(("NuView-MIB", "clxTrapDataString01"))
if mibBuilder.loadTexts: ClusterXTrapStr.setDescription('Generic SNMP trap generated by NuView ClusterX applications and services. Varbind #1: Custom string.')
ClusterXTrapNodeFail = NotificationType((1, 3, 6, 1, 4, 1, 2427, 2) + (0,2)).setObjects(("NuView-MIB", "clxTrapDataClusterName"), ("NuView-MIB", "clxTrapDataNodeName"))
if mibBuilder.loadTexts: ClusterXTrapNodeFail.setDescription('This trap is sent when ClusterX detects the failure of a node in an MSCS cluster. The trap identifies the cluster,the name of the node that failed ')
ClusterXTrapClusterFail = NotificationType((1, 3, 6, 1, 4, 1, 2427, 2) + (0,3)).setObjects(("NuView-MIB", "clxTrapDataClusterName"))
if mibBuilder.loadTexts: ClusterXTrapClusterFail.setDescription('This trap is sent when ClusterX detects the failure of an MSCS cluster. The trap identifies the name of the failed cluster ')
ClusterXTrapResourceFail = NotificationType((1, 3, 6, 1, 4, 1, 2427, 2) + (0,4)).setObjects(("NuView-MIB", "clxTrapDataClusterName"), ("NuView-MIB", "clxTrapDataNodeName"), ("NuView-MIB", "clxTrapDataResourceName"))
if mibBuilder.loadTexts: ClusterXTrapResourceFail.setDescription('This trap is sent when ClusterX detects the failure of a resource on an MSCS cluster. The trap identifies the names of the cluster, node and resource ')
ClusterXTrapNodeJoins = NotificationType((1, 3, 6, 1, 4, 1, 2427, 2) + (0,5)).setObjects(("NuView-MIB", "clxTrapDataClusterName"), ("NuView-MIB", "clxTrapDataNodeName"))
if mibBuilder.loadTexts: ClusterXTrapNodeJoins.setDescription('This trap is sent when ClusterX detects that node has joined or rejoined an MSCS cluster. The trap identifes the name of the cluster and the name of the node that joined.')
ClusterXTrapNetworkFail = NotificationType((1, 3, 6, 1, 4, 1, 2427, 2) + (0,6)).setObjects(("NuView-MIB", "clxTrapDataClusterName"), ("NuView-MIB", "clxTrapDataNetworkName"))
if mibBuilder.loadTexts: ClusterXTrapNetworkFail.setDescription('This trap is sent when ClusterX detects the failure of the private or public cluster interconnects on an MSCS cluster.')
ClusterXTrapNormalClusterServiceLog = NotificationType((1, 3, 6, 1, 4, 1, 2427, 2) + (0,7)).setObjects(("NuView-MIB", "clxTrapEventDate"), ("NuView-MIB", "clxTrapEventTime"), ("NuView-MIB", "clxTrapEventSource"), ("NuView-MIB", "clxTrapEventCategory"), ("NuView-MIB", "clxTrapEventID"), ("NuView-MIB", "clxTrapEventUser"), ("NuView-MIB", "clxTrapEventComputer"))
if mibBuilder.loadTexts: ClusterXTrapNormalClusterServiceLog.setDescription('This trap is generated when ClusterX detects that the Cluster Service has written a new entry in the Windows NT Event Log on a managed cluster.It contains the information about cluster service log')
ClusterXTrapWarningClusterServiceLog = NotificationType((1, 3, 6, 1, 4, 1, 2427, 2) + (0,8)).setObjects(("NuView-MIB", "clxTrapEventDate"), ("NuView-MIB", "clxTrapEventTime"), ("NuView-MIB", "clxTrapEventSource"), ("NuView-MIB", "clxTrapEventCategory"), ("NuView-MIB", "clxTrapEventID"), ("NuView-MIB", "clxTrapEventUser"), ("NuView-MIB", "clxTrapEventComputer"))
if mibBuilder.loadTexts: ClusterXTrapWarningClusterServiceLog.setDescription('This trap is generated when ClusterX detects that the Cluster Service has written a new entry in the Windows NT Event Log on a managed cluster.It contains the information about cluster service log')
ClusterXTrapCriticalClusterServiceLog = NotificationType((1, 3, 6, 1, 4, 1, 2427, 2) + (0,9)).setObjects(("NuView-MIB", "clxTrapEventDate"), ("NuView-MIB", "clxTrapEventTime"), ("NuView-MIB", "clxTrapEventSource"), ("NuView-MIB", "clxTrapEventCategory"), ("NuView-MIB", "clxTrapEventID"), ("NuView-MIB", "clxTrapEventUser"), ("NuView-MIB", "clxTrapEventComputer"))
if mibBuilder.loadTexts: ClusterXTrapCriticalClusterServiceLog.setDescription('This trap is generated when ClusterX detects that the Cluster Service has written a new entry in the Windows NT Event Log on a managed cluster.It contains the information about cluster service log')
mibBuilder.exportSymbols("NuView-MIB", clxTrapData=clxTrapData, ClusterXTrapClusterFail=ClusterXTrapClusterFail, clxTrapDataResourceType=clxTrapDataResourceType, clxMibStats=clxMibStats, clxTrapDataNetworkName=clxTrapDataNetworkName, clxTrapEventComputer=clxTrapEventComputer, NuView=NuView, clxTrapDataNodeName=clxTrapDataNodeName, clxTrapEventUser=clxTrapEventUser, clxTrapEventCategory=clxTrapEventCategory, clxTrapEventDate=clxTrapEventDate, ClusterXTrapResourceFail=ClusterXTrapResourceFail, clxTrapEventTime=clxTrapEventTime, ClusterXTrapCriticalClusterServiceLog=ClusterXTrapCriticalClusterServiceLog, clxMibStatsVendorName=clxMibStatsVendorName, ClusterXTrapNormalClusterServiceLog=ClusterXTrapNormalClusterServiceLog, clxTrapDataResourceName=clxTrapDataResourceName, ClusterXTrapNodeFail=ClusterXTrapNodeFail, ClusterX=ClusterX, clxTrapEventSource=clxTrapEventSource, clxTrapEventID=clxTrapEventID, ClusterXTrapWarningClusterServiceLog=ClusterXTrapWarningClusterServiceLog, clxTrapDataSeverityValue=clxTrapDataSeverityValue, NuViewTrapStr=NuViewTrapStr, ClusterXTrapStr=ClusterXTrapStr, ClusterXTrapNodeJoins=ClusterXTrapNodeJoins, clxTrapDataClusterName=clxTrapDataClusterName, clxTrapDataString01=clxTrapDataString01, clxTrapDataNetwork=clxTrapDataNetwork, ClusterXTrapNetworkFail=ClusterXTrapNetworkFail, clxMibStatsMajRev=clxMibStatsMajRev, clxMibStatsMinRev=clxMibStatsMinRev)