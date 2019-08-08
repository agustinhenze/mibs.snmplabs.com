#
# PySNMP MIB module SONICWALL-FIREWALL-IP-STATISTICS-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/SONICWALL-FIREWALL-IP-STATISTICS-MIB
# Produced by pysmi-0.3.4 at Wed May  1 15:09:07 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
OctetString, ObjectIdentifier, Integer = mibBuilder.importSymbols("ASN1", "OctetString", "ObjectIdentifier", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
SingleValueConstraint, ConstraintsUnion, ValueSizeConstraint, ValueRangeConstraint, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "SingleValueConstraint", "ConstraintsUnion", "ValueSizeConstraint", "ValueRangeConstraint", "ConstraintsIntersection")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
ModuleIdentity, Integer32, Counter32, MibIdentifier, Counter64, MibScalar, MibTable, MibTableRow, MibTableColumn, TimeTicks, NotificationType, ObjectIdentity, iso, IpAddress, Gauge32, Unsigned32, Bits = mibBuilder.importSymbols("SNMPv2-SMI", "ModuleIdentity", "Integer32", "Counter32", "MibIdentifier", "Counter64", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "TimeTicks", "NotificationType", "ObjectIdentity", "iso", "IpAddress", "Gauge32", "Unsigned32", "Bits")
DisplayString, TruthValue, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TruthValue", "TextualConvention")
sonicwallFw, = mibBuilder.importSymbols("SONICWALL-SMI", "sonicwallFw")
sonicwallFwStatsModule = ModuleIdentity((1, 3, 6, 1, 4, 1, 8741, 1, 3))
sonicwallFwStatsModule.setRevisions(('2015-01-08 00:00', '2014-02-28 00:00', '2014-02-18 00:00', '2005-11-09 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: sonicwallFwStatsModule.setRevisionsDescriptions(('Update Postal, Tel, Fax Add DPI-SSL Connection Counts', 'Add Syslog Module for syslog configuration and syslog statistic info exposing', 'Add Sensor Table for hardware health monitoring', 'Initial Version',))
if mibBuilder.loadTexts: sonicwallFwStatsModule.setLastUpdated('201501080000Z')
if mibBuilder.loadTexts: sonicwallFwStatsModule.setOrganization('DELL SonicWall')
if mibBuilder.loadTexts: sonicwallFwStatsModule.setContactInfo(' DELL SonicWall Postal: 5455 Great America Parkway Santa Clara, CA 95054 USA Tel: +1 408 745 9600 Fax: +1 408 745 9300 E-mail: products@sonicwall.com')
if mibBuilder.loadTexts: sonicwallFwStatsModule.setDescription('The Generic MIB Module for SonicWALL Firewall.')
class SyslogFacility(TextualConvention, Integer32):
    reference = 'The Syslog Protocol (RFC 3164): Section 4.'
    description = 'The Syslog standard facilities defined by RFC 3164.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23))
    namedValues = NamedValues(("kern", 0), ("user", 1), ("mail", 2), ("daemon", 3), ("auth", 4), ("syslog", 5), ("lpr", 6), ("news", 7), ("uucp", 8), ("cron", 9), ("authpriv", 10), ("ftp", 11), ("ntp", 12), ("audit", 13), ("alert", 14), ("cron2", 15), ("local0", 16), ("local1", 17), ("local2", 18), ("local3", 19), ("local4", 20), ("local5", 21), ("local6", 22), ("local7", 23))

sonicwallFwStats = MibIdentifier((1, 3, 6, 1, 4, 1, 8741, 1, 3, 1))
sonicMaxConnCacheEntries = MibScalar((1, 3, 6, 1, 4, 1, 8741, 1, 3, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 2147483647))).setMaxAccess("readonly")
if mibBuilder.loadTexts: sonicMaxConnCacheEntries.setStatus('current')
if mibBuilder.loadTexts: sonicMaxConnCacheEntries.setDescription(' Maximum number of connection cache entries allowed through the firewall')
sonicCurrentConnCacheEntries = MibScalar((1, 3, 6, 1, 4, 1, 8741, 1, 3, 1, 2), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sonicCurrentConnCacheEntries.setStatus('current')
if mibBuilder.loadTexts: sonicCurrentConnCacheEntries.setDescription(' Number of active connection cache entries through the firewall')
sonicCurrentCPUUtil = MibScalar((1, 3, 6, 1, 4, 1, 8741, 1, 3, 1, 3), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sonicCurrentCPUUtil.setStatus('current')
if mibBuilder.loadTexts: sonicCurrentCPUUtil.setDescription(' Instantaneous CPU Utilization in percent')
sonicCurrentRAMUtil = MibScalar((1, 3, 6, 1, 4, 1, 8741, 1, 3, 1, 4), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sonicCurrentRAMUtil.setStatus('current')
if mibBuilder.loadTexts: sonicCurrentRAMUtil.setDescription(' Instantaneous RAM Utilization in percent')
sonicNatTranslationCount = MibScalar((1, 3, 6, 1, 4, 1, 8741, 1, 3, 1, 5), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sonicNatTranslationCount.setStatus('current')
if mibBuilder.loadTexts: sonicNatTranslationCount.setDescription(' Current number of dynamic NAT translations being performed.')
sonicCurrentManagementCPUUtil = MibScalar((1, 3, 6, 1, 4, 1, 8741, 1, 3, 1, 6), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sonicCurrentManagementCPUUtil.setStatus('current')
if mibBuilder.loadTexts: sonicCurrentManagementCPUUtil.setDescription(' Instantaneous management CPU Utilization in percent.')
sonicCurrentFwdAndInspectCPUUtil = MibScalar((1, 3, 6, 1, 4, 1, 8741, 1, 3, 1, 7), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sonicCurrentFwdAndInspectCPUUtil.setStatus('current')
if mibBuilder.loadTexts: sonicCurrentFwdAndInspectCPUUtil.setDescription(' Instantaneous Forwarding/Inspection CPU Utilization in percent.')
sonicIfStatTable = MibTable((1, 3, 6, 1, 4, 1, 8741, 1, 3, 1, 8), )
if mibBuilder.loadTexts: sonicIfStatTable.setStatus('current')
if mibBuilder.loadTexts: sonicIfStatTable.setDescription('List of physical interfaces and their current usage in percentage.')
sonicIfStatEntry = MibTableRow((1, 3, 6, 1, 4, 1, 8741, 1, 3, 1, 8, 1), ).setIndexNames((0, "SONICWALL-FIREWALL-IP-STATISTICS-MIB", "sonicIfIndex"))
if mibBuilder.loadTexts: sonicIfStatEntry.setStatus('current')
if mibBuilder.loadTexts: sonicIfStatEntry.setDescription('Interface status entry.')
sonicIfIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 8741, 1, 3, 1, 8, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sonicIfIndex.setStatus('current')
if mibBuilder.loadTexts: sonicIfIndex.setDescription("A unique value for each interface. Its value ranges between 1 and the value of ifNumber. The value for each interface must remain constant at least from one re-initialization of the entity's network management system to the next re- initialization.")
sonicIfUsage = MibTableColumn((1, 3, 6, 1, 4, 1, 8741, 1, 3, 1, 8, 1, 2), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sonicIfUsage.setStatus('current')
if mibBuilder.loadTexts: sonicIfUsage.setDescription('Interface bandwidth usage value in percentage.')
sonicIfThroughput = MibTableColumn((1, 3, 6, 1, 4, 1, 8741, 1, 3, 1, 8, 1, 3), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sonicIfThroughput.setStatus('current')
if mibBuilder.loadTexts: sonicIfThroughput.setDescription('Interface throughput value in bits per second.')
sonicwallFwVPNStats = MibIdentifier((1, 3, 6, 1, 4, 1, 8741, 1, 3, 2))
sonicwallFwVpnIPSecStats = MibIdentifier((1, 3, 6, 1, 4, 1, 8741, 1, 3, 2, 1))
sonicSAStatTable = MibTable((1, 3, 6, 1, 4, 1, 8741, 1, 3, 2, 1, 1), )
if mibBuilder.loadTexts: sonicSAStatTable.setStatus('current')
if mibBuilder.loadTexts: sonicSAStatTable.setDescription('This table provides statistics for each Security Association.')
sonicSAStatEntry = MibTableRow((1, 3, 6, 1, 4, 1, 8741, 1, 3, 2, 1, 1, 1), ).setIndexNames((0, "SONICWALL-FIREWALL-IP-STATISTICS-MIB", "sonicIpsecSaIndex"))
if mibBuilder.loadTexts: sonicSAStatEntry.setStatus('current')
if mibBuilder.loadTexts: sonicSAStatEntry.setDescription('Entries in table cannot be added or deleted. This table is completely controlled by the agent. Each SA statistics will be represented by an entry in this table. ')
sonicIpsecSaIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 8741, 1, 3, 2, 1, 1, 1, 1), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sonicIpsecSaIndex.setStatus('current')
if mibBuilder.loadTexts: sonicIpsecSaIndex.setDescription(' Phase2 SA index.')
sonicSAStatPeerGateway = MibTableColumn((1, 3, 6, 1, 4, 1, 8741, 1, 3, 2, 1, 1, 1, 2), IpAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sonicSAStatPeerGateway.setStatus('current')
if mibBuilder.loadTexts: sonicSAStatPeerGateway.setDescription('Peer gateway address where the tunnel gets terminated .')
sonicSAStatSrcAddrBegin = MibTableColumn((1, 3, 6, 1, 4, 1, 8741, 1, 3, 2, 1, 1, 1, 3), IpAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sonicSAStatSrcAddrBegin.setStatus('current')
if mibBuilder.loadTexts: sonicSAStatSrcAddrBegin.setDescription('First address of the Source network for the phase2 SA .')
sonicSAStatSrcAddrEnd = MibTableColumn((1, 3, 6, 1, 4, 1, 8741, 1, 3, 2, 1, 1, 1, 4), IpAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sonicSAStatSrcAddrEnd.setStatus('current')
if mibBuilder.loadTexts: sonicSAStatSrcAddrEnd.setDescription('Last address of the Source network for the phase2 SA .')
sonicSAStatDstAddrBegin = MibTableColumn((1, 3, 6, 1, 4, 1, 8741, 1, 3, 2, 1, 1, 1, 5), IpAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sonicSAStatDstAddrBegin.setStatus('current')
if mibBuilder.loadTexts: sonicSAStatDstAddrBegin.setDescription('First address of the destination network for the phase2 SA .')
sonicSAStatDstAddrEnd = MibTableColumn((1, 3, 6, 1, 4, 1, 8741, 1, 3, 2, 1, 1, 1, 6), IpAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sonicSAStatDstAddrEnd.setStatus('current')
if mibBuilder.loadTexts: sonicSAStatDstAddrEnd.setDescription('Last address of the destination network for the phase2 SA .')
sonicSAStatCreateTime = MibTableColumn((1, 3, 6, 1, 4, 1, 8741, 1, 3, 2, 1, 1, 1, 7), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sonicSAStatCreateTime.setStatus('current')
if mibBuilder.loadTexts: sonicSAStatCreateTime.setDescription('Time this phase2 SA was actually created in GMT.')
sonicSAStatEncryptPktCount = MibTableColumn((1, 3, 6, 1, 4, 1, 8741, 1, 3, 2, 1, 1, 1, 8), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sonicSAStatEncryptPktCount.setStatus('current')
if mibBuilder.loadTexts: sonicSAStatEncryptPktCount.setDescription('Total encrypted packet count for this phase2 SA.')
sonicSAStatEncryptByteCount = MibTableColumn((1, 3, 6, 1, 4, 1, 8741, 1, 3, 2, 1, 1, 1, 9), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sonicSAStatEncryptByteCount.setStatus('current')
if mibBuilder.loadTexts: sonicSAStatEncryptByteCount.setDescription('Total encrypted byte count for this phase2 SA.')
sonicSAStatDecryptPktCount = MibTableColumn((1, 3, 6, 1, 4, 1, 8741, 1, 3, 2, 1, 1, 1, 10), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sonicSAStatDecryptPktCount.setStatus('current')
if mibBuilder.loadTexts: sonicSAStatDecryptPktCount.setDescription('Total decrypted packet count for this phase2 SA.')
sonicSAStatDecryptByteCount = MibTableColumn((1, 3, 6, 1, 4, 1, 8741, 1, 3, 2, 1, 1, 1, 11), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sonicSAStatDecryptByteCount.setStatus('current')
if mibBuilder.loadTexts: sonicSAStatDecryptByteCount.setDescription('Total decrypted byte count for this phase2 SA.')
sonicSAStatInFragPktCount = MibTableColumn((1, 3, 6, 1, 4, 1, 8741, 1, 3, 2, 1, 1, 1, 12), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sonicSAStatInFragPktCount.setStatus('current')
if mibBuilder.loadTexts: sonicSAStatInFragPktCount.setDescription('Incoming Fragmented packet count for this phase2 SA')
sonicSAStatOutFragPktCount = MibTableColumn((1, 3, 6, 1, 4, 1, 8741, 1, 3, 2, 1, 1, 1, 13), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sonicSAStatOutFragPktCount.setStatus('current')
if mibBuilder.loadTexts: sonicSAStatOutFragPktCount.setDescription('Outgoing Fragmented packet count for this phase2 SA')
sonicSAStatUserName = MibTableColumn((1, 3, 6, 1, 4, 1, 8741, 1, 3, 2, 1, 1, 1, 14), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sonicSAStatUserName.setStatus('current')
if mibBuilder.loadTexts: sonicSAStatUserName.setDescription('Name of the security policy used for creating this phase2 SA.')
sonicwallFwHWStats = MibIdentifier((1, 3, 6, 1, 4, 1, 8741, 1, 3, 3))
sonicwallFwHWSensorStats = MibIdentifier((1, 3, 6, 1, 4, 1, 8741, 1, 3, 3, 3))
sonicwallSensorsTable = MibTable((1, 3, 6, 1, 4, 1, 8741, 1, 3, 3, 3, 1), )
if mibBuilder.loadTexts: sonicwallSensorsTable.setStatus('current')
if mibBuilder.loadTexts: sonicwallSensorsTable.setDescription('This lists all the sensors and their value in SonicWALL firewall device.')
sonicwallSensorsEntry = MibTableRow((1, 3, 6, 1, 4, 1, 8741, 1, 3, 3, 3, 1, 1), ).setIndexNames((0, "SONICWALL-FIREWALL-IP-STATISTICS-MIB", "sonicwallSensorsIndex"))
if mibBuilder.loadTexts: sonicwallSensorsEntry.setStatus('current')
if mibBuilder.loadTexts: sonicwallSensorsEntry.setDescription('SonicWALL sensor entry')
sonicwallSensorsIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 8741, 1, 3, 3, 3, 1, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 65535))).setMaxAccess("readonly")
if mibBuilder.loadTexts: sonicwallSensorsIndex.setStatus('current')
if mibBuilder.loadTexts: sonicwallSensorsIndex.setDescription('Index that identifies the sensor')
sonicwallSensorsId = MibTableColumn((1, 3, 6, 1, 4, 1, 8741, 1, 3, 3, 3, 1, 1, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 65535))).setMaxAccess("readonly")
if mibBuilder.loadTexts: sonicwallSensorsId.setStatus('current')
if mibBuilder.loadTexts: sonicwallSensorsId.setDescription('Index that identifies the sensor ID')
sonicwallSensorsDevice = MibTableColumn((1, 3, 6, 1, 4, 1, 8741, 1, 3, 3, 3, 1, 1, 3), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 255))).setMaxAccess("readonly")
if mibBuilder.loadTexts: sonicwallSensorsDevice.setStatus('current')
if mibBuilder.loadTexts: sonicwallSensorsDevice.setDescription('Sensor descriptive name')
sonicwallSensorsValue = MibTableColumn((1, 3, 6, 1, 4, 1, 8741, 1, 3, 3, 3, 1, 1, 4), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sonicwallSensorsValue.setStatus('current')
if mibBuilder.loadTexts: sonicwallSensorsValue.setDescription('Sensor value')
sonicwallSensorsUnit = MibTableColumn((1, 3, 6, 1, 4, 1, 8741, 1, 3, 3, 3, 1, 1, 5), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 255))).setMaxAccess("readonly")
if mibBuilder.loadTexts: sonicwallSensorsUnit.setStatus('current')
if mibBuilder.loadTexts: sonicwallSensorsUnit.setDescription('Sensor unit')
sonicwallFwSyslogStats = MibIdentifier((1, 3, 6, 1, 4, 1, 8741, 1, 3, 4))
sonicwallFwSyslogSetting = MibIdentifier((1, 3, 6, 1, 4, 1, 8741, 1, 3, 4, 1))
sonicwallFwSyslogServer = MibIdentifier((1, 3, 6, 1, 4, 1, 8741, 1, 3, 4, 2))
sonicwallFwSyslogStatistic = MibIdentifier((1, 3, 6, 1, 4, 1, 8741, 1, 3, 4, 3))
sonicSyslogFacility = MibScalar((1, 3, 6, 1, 4, 1, 8741, 1, 3, 4, 1, 1), SyslogFacility()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sonicSyslogFacility.setStatus('current')
if mibBuilder.loadTexts: sonicSyslogFacility.setDescription('Syslog facility configured on firewall.')
sonicSyslogOverrideSetting = MibScalar((1, 3, 6, 1, 4, 1, 8741, 1, 3, 4, 1, 2), TruthValue()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sonicSyslogOverrideSetting.setStatus('current')
if mibBuilder.loadTexts: sonicSyslogOverrideSetting.setDescription('When using SonicWALL ViewPoint for reporting solution, this object indicates whether the appliance overrides Syslog settings with reporting software settings.')
sonicSyslogFormat = MibScalar((1, 3, 6, 1, 4, 1, 8741, 1, 3, 4, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3))).clone(namedValues=NamedValues(("default", 0), ("webTrends", 1), ("enhSyslog", 2), ("arcSight", 3)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: sonicSyslogFormat.setStatus('current')
if mibBuilder.loadTexts: sonicSyslogFormat.setDescription('Syslog format configured on firewall. The following Syslog formats can be specified: Default - Use the default SonicWALL Syslog format. WebTrends - Use the WebTrends Syslog format. You must have WebTrends software installed on your system. Enhanced Syslog - Use the Enhanced SonicWALL Syslog format. ArcSight - Use the ArcSight Syslog format. A Syslog server must be configured with the ArcSight Logger application to decode the ArcSight messages.')
sonicSyslogID = MibScalar((1, 3, 6, 1, 4, 1, 8741, 1, 3, 4, 1, 4), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 32))).setMaxAccess("readonly")
if mibBuilder.loadTexts: sonicSyslogID.setStatus('current')
if mibBuilder.loadTexts: sonicSyslogID.setDescription('The Syslog ID field is included in all generated syslog messages, prefixed by id=. The Syslog ID field is disabled when the Override Syslog Settings with Reporting Software Settings option is enabled.')
sonicSyslogEventRateLimitEnable = MibScalar((1, 3, 6, 1, 4, 1, 8741, 1, 3, 4, 1, 5), TruthValue()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sonicSyslogEventRateLimitEnable.setStatus('current')
if mibBuilder.loadTexts: sonicSyslogEventRateLimitEnable.setDescription('This object indicates whether the appliance enables rate limiting of events to prevent the internal or external logging mechanism from being overwhelmed by log events.')
sonicSyslogEventRateLimit = MibScalar((1, 3, 6, 1, 4, 1, 8741, 1, 3, 4, 1, 6), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sonicSyslogEventRateLimit.setStatus('current')
if mibBuilder.loadTexts: sonicSyslogEventRateLimit.setDescription('Event rate limiting: Maximum Events Per Second.')
sonicSyslogDataRateLimitEnable = MibScalar((1, 3, 6, 1, 4, 1, 8741, 1, 3, 4, 1, 7), TruthValue()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sonicSyslogDataRateLimitEnable.setStatus('current')
if mibBuilder.loadTexts: sonicSyslogDataRateLimitEnable.setDescription('This object indicates whether the appliance enables rate limiting of data to prevent the internal or external logging mechanism from being overwhelmed by log events.')
sonicSyslogDataRateLimit = MibScalar((1, 3, 6, 1, 4, 1, 8741, 1, 3, 4, 1, 8), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sonicSyslogDataRateLimit.setStatus('current')
if mibBuilder.loadTexts: sonicSyslogDataRateLimit.setDescription('Data rate limiting: Maximum Bytes Per Second.')
sonicSyslogNDPPEnable = MibScalar((1, 3, 6, 1, 4, 1, 8741, 1, 3, 4, 1, 9), TruthValue()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sonicSyslogNDPPEnable.setStatus('current')
if mibBuilder.loadTexts: sonicSyslogNDPPEnable.setDescription('This object indicates whether the appliance enables NDPP Enforcement for Syslog Server.')
sonicSyslogMaxServers = MibScalar((1, 3, 6, 1, 4, 1, 8741, 1, 3, 4, 2, 1), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sonicSyslogMaxServers.setStatus('current')
if mibBuilder.loadTexts: sonicSyslogMaxServers.setDescription('The maximum number of syslog servers that can be configured for the system in sonicSyslogTable.')
sonicSyslogServerTable = MibTable((1, 3, 6, 1, 4, 1, 8741, 1, 3, 4, 2, 2), )
if mibBuilder.loadTexts: sonicSyslogServerTable.setStatus('current')
if mibBuilder.loadTexts: sonicSyslogServerTable.setDescription('This table contains entries of syslog servers for the appliance. The maximum number of entries is indicated by the object sonicwallSyslogMaxServers.')
sonicSyslogServerEntry = MibTableRow((1, 3, 6, 1, 4, 1, 8741, 1, 3, 4, 2, 2, 1), ).setIndexNames((0, "SONICWALL-FIREWALL-IP-STATISTICS-MIB", "sonicSyslogServerIndex"))
if mibBuilder.loadTexts: sonicSyslogServerEntry.setStatus('current')
if mibBuilder.loadTexts: sonicSyslogServerEntry.setDescription('An entry containing info about syslog server configured by SonicWALL firewall appliance')
sonicSyslogServerIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 8741, 1, 3, 4, 2, 2, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sonicSyslogServerIndex.setStatus('current')
if mibBuilder.loadTexts: sonicSyslogServerIndex.setDescription('Index that identifies the syslog server')
sonicSyslogServerAddr = MibTableColumn((1, 3, 6, 1, 4, 1, 8741, 1, 3, 4, 2, 2, 1, 2), IpAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sonicSyslogServerAddr.setStatus('current')
if mibBuilder.loadTexts: sonicSyslogServerAddr.setDescription('Syslog server address.')
sonicSyslogServerPort = MibTableColumn((1, 3, 6, 1, 4, 1, 8741, 1, 3, 4, 2, 2, 1, 3), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 65535))).setMaxAccess("readonly")
if mibBuilder.loadTexts: sonicSyslogServerPort.setStatus('current')
if mibBuilder.loadTexts: sonicSyslogServerPort.setDescription('Syslog server port.')
sonicSyslogMessage = MibScalar((1, 3, 6, 1, 4, 1, 8741, 1, 3, 4, 3, 1), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sonicSyslogMessage.setStatus('current')
if mibBuilder.loadTexts: sonicSyslogMessage.setDescription('Running total of syslog message generated since startup.')
sonicSyslogStreamData = MibScalar((1, 3, 6, 1, 4, 1, 8741, 1, 3, 4, 3, 2), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sonicSyslogStreamData.setStatus('current')
if mibBuilder.loadTexts: sonicSyslogStreamData.setDescription('Running total of syslog stream data generated since startup.')
sonicwallFwDpiSslStats = MibIdentifier((1, 3, 6, 1, 4, 1, 8741, 1, 3, 5))
sonicDpiSslConnCountCur = MibScalar((1, 3, 6, 1, 4, 1, 8741, 1, 3, 5, 1), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sonicDpiSslConnCountCur.setStatus('current')
if mibBuilder.loadTexts: sonicDpiSslConnCountCur.setDescription('Current SSL-inspected connections through the firewall.')
sonicDpiSslConnCountHighWater = MibScalar((1, 3, 6, 1, 4, 1, 8741, 1, 3, 5, 2), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sonicDpiSslConnCountHighWater.setStatus('current')
if mibBuilder.loadTexts: sonicDpiSslConnCountHighWater.setDescription('Highwater SSL-inspected connections through the firewall.')
sonicDpiSslConnCountMax = MibScalar((1, 3, 6, 1, 4, 1, 8741, 1, 3, 5, 3), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sonicDpiSslConnCountMax.setStatus('current')
if mibBuilder.loadTexts: sonicDpiSslConnCountMax.setDescription('Maximum SSL-inspected connections through the firewall.')
mibBuilder.exportSymbols("SONICWALL-FIREWALL-IP-STATISTICS-MIB", SyslogFacility=SyslogFacility, sonicSAStatDstAddrBegin=sonicSAStatDstAddrBegin, sonicwallFwSyslogSetting=sonicwallFwSyslogSetting, sonicwallSensorsDevice=sonicwallSensorsDevice, sonicDpiSslConnCountHighWater=sonicDpiSslConnCountHighWater, sonicCurrentConnCacheEntries=sonicCurrentConnCacheEntries, sonicwallFwHWStats=sonicwallFwHWStats, sonicSAStatTable=sonicSAStatTable, sonicSAStatPeerGateway=sonicSAStatPeerGateway, sonicSAStatOutFragPktCount=sonicSAStatOutFragPktCount, sonicSAStatSrcAddrBegin=sonicSAStatSrcAddrBegin, sonicwallSensorsIndex=sonicwallSensorsIndex, sonicwallSensorsValue=sonicwallSensorsValue, sonicNatTranslationCount=sonicNatTranslationCount, sonicSyslogDataRateLimit=sonicSyslogDataRateLimit, sonicSyslogStreamData=sonicSyslogStreamData, sonicSAStatCreateTime=sonicSAStatCreateTime, sonicwallFwSyslogServer=sonicwallFwSyslogServer, sonicSyslogNDPPEnable=sonicSyslogNDPPEnable, sonicSyslogServerEntry=sonicSyslogServerEntry, sonicSAStatEncryptByteCount=sonicSAStatEncryptByteCount, sonicSAStatEntry=sonicSAStatEntry, sonicCurrentCPUUtil=sonicCurrentCPUUtil, sonicCurrentFwdAndInspectCPUUtil=sonicCurrentFwdAndInspectCPUUtil, sonicwallFwVPNStats=sonicwallFwVPNStats, sonicwallFwStatsModule=sonicwallFwStatsModule, sonicIpsecSaIndex=sonicIpsecSaIndex, sonicwallFwStats=sonicwallFwStats, sonicIfUsage=sonicIfUsage, sonicwallFwSyslogStatistic=sonicwallFwSyslogStatistic, sonicSAStatSrcAddrEnd=sonicSAStatSrcAddrEnd, sonicwallSensorsUnit=sonicwallSensorsUnit, sonicSyslogServerAddr=sonicSyslogServerAddr, sonicwallFwHWSensorStats=sonicwallFwHWSensorStats, sonicMaxConnCacheEntries=sonicMaxConnCacheEntries, sonicSAStatInFragPktCount=sonicSAStatInFragPktCount, sonicSyslogDataRateLimitEnable=sonicSyslogDataRateLimitEnable, sonicwallSensorsTable=sonicwallSensorsTable, sonicSyslogFormat=sonicSyslogFormat, sonicDpiSslConnCountMax=sonicDpiSslConnCountMax, PYSNMP_MODULE_ID=sonicwallFwStatsModule, sonicSyslogOverrideSetting=sonicSyslogOverrideSetting, sonicSyslogID=sonicSyslogID, sonicSyslogServerPort=sonicSyslogServerPort, sonicSAStatDecryptPktCount=sonicSAStatDecryptPktCount, sonicwallSensorsId=sonicwallSensorsId, sonicIfThroughput=sonicIfThroughput, sonicwallSensorsEntry=sonicwallSensorsEntry, sonicIfStatEntry=sonicIfStatEntry, sonicCurrentRAMUtil=sonicCurrentRAMUtil, sonicwallFwVpnIPSecStats=sonicwallFwVpnIPSecStats, sonicSAStatEncryptPktCount=sonicSAStatEncryptPktCount, sonicSAStatUserName=sonicSAStatUserName, sonicSyslogMaxServers=sonicSyslogMaxServers, sonicSyslogEventRateLimitEnable=sonicSyslogEventRateLimitEnable, sonicSAStatDstAddrEnd=sonicSAStatDstAddrEnd, sonicIfIndex=sonicIfIndex, sonicSyslogEventRateLimit=sonicSyslogEventRateLimit, sonicCurrentManagementCPUUtil=sonicCurrentManagementCPUUtil, sonicSyslogServerTable=sonicSyslogServerTable, sonicIfStatTable=sonicIfStatTable, sonicDpiSslConnCountCur=sonicDpiSslConnCountCur, sonicSAStatDecryptByteCount=sonicSAStatDecryptByteCount, sonicwallFwDpiSslStats=sonicwallFwDpiSslStats, sonicSyslogFacility=sonicSyslogFacility, sonicSyslogServerIndex=sonicSyslogServerIndex, sonicSyslogMessage=sonicSyslogMessage, sonicwallFwSyslogStats=sonicwallFwSyslogStats)