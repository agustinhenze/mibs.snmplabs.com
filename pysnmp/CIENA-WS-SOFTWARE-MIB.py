#
# PySNMP MIB module CIENA-WS-SOFTWARE-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/CIENA-WS-SOFTWARE-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 17:32:05 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
ObjectIdentifier, Integer, OctetString = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "Integer", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsUnion, SingleValueConstraint, ValueRangeConstraint, ValueSizeConstraint, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "SingleValueConstraint", "ValueRangeConstraint", "ValueSizeConstraint", "ConstraintsIntersection")
cienaWsConfig, = mibBuilder.importSymbols("CIENA-WS-MIB", "cienaWsConfig")
StringMaxl128, StringMaxl64, StringMaxl256, StringMaxl32 = mibBuilder.importSymbols("CIENA-WS-TYPEDEFS-MIB", "StringMaxl128", "StringMaxl64", "StringMaxl256", "StringMaxl32")
ObjectGroup, NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "ObjectGroup", "NotificationGroup", "ModuleCompliance")
MibScalar, MibTable, MibTableRow, MibTableColumn, Unsigned32, iso, ObjectIdentity, Bits, Counter32, Gauge32, NotificationType, TimeTicks, Counter64, IpAddress, ModuleIdentity, MibIdentifier, Integer32 = mibBuilder.importSymbols("SNMPv2-SMI", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Unsigned32", "iso", "ObjectIdentity", "Bits", "Counter32", "Gauge32", "NotificationType", "TimeTicks", "Counter64", "IpAddress", "ModuleIdentity", "MibIdentifier", "Integer32")
DisplayString, TruthValue, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TruthValue", "TextualConvention")
cienaWsSoftwareMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 1271, 3, 4, 14))
cienaWsSoftwareMIB.setRevisions(('2016-11-03 00:00', '2016-06-14 00:00', '2015-09-29 00:00',))
if mibBuilder.loadTexts: cienaWsSoftwareMIB.setLastUpdated('201611030000Z')
if mibBuilder.loadTexts: cienaWsSoftwareMIB.setOrganization('Ciena Corporation')
class SoftwareOpState(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3, 4, 5))
    namedValues = NamedValues(("unknown", 0), ("normal", 1), ("upgradeinprogress", 2), ("restartinprogress", 3), ("subsystemfailed", 4), ("systemloaderror", 5))

class SoftwareRtncode(TextualConvention, Unsigned32):
    status = 'current'

class UpgradeOpState(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18))
    namedValues = NamedValues(("unknown", 0), ("idle", 1), ("downloadinprogress", 2), ("downloadcomplete", 3), ("downloadfailed", 4), ("installationinprogress", 5), ("installationcomplete", 6), ("installationfailed", 7), ("activationinprogress", 8), ("activationcomplete", 9), ("activationfailed", 10), ("commitinprogress", 11), ("commitcomplete", 12), ("commitfailed", 13), ("cancelinprogress", 14), ("cancelcomplete", 15), ("cancelfailed", 16), ("manualcommit", 17), ("manualcancel", 18))

cwsSoftwareStatusTable = MibTable((1, 3, 6, 1, 4, 1, 1271, 3, 4, 14, 3), )
if mibBuilder.loadTexts: cwsSoftwareStatusTable.setStatus('current')
cwsSoftwareStatusEntry = MibTableRow((1, 3, 6, 1, 4, 1, 1271, 3, 4, 14, 3, 1), ).setIndexNames((0, "CIENA-WS-SOFTWARE-MIB", "cwsSoftwareStatusTableSnmpKey"))
if mibBuilder.loadTexts: cwsSoftwareStatusEntry.setStatus('current')
cwsSoftwareStatusTableSnmpKey = MibTableColumn((1, 3, 6, 1, 4, 1, 1271, 3, 4, 14, 3, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 2147483647)))
if mibBuilder.loadTexts: cwsSoftwareStatusTableSnmpKey.setStatus('current')
cwsSoftwareStatusSoftwareOperationalState = MibTableColumn((1, 3, 6, 1, 4, 1, 1271, 3, 4, 14, 3, 1, 2), SoftwareOpState()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cwsSoftwareStatusSoftwareOperationalState.setStatus('current')
cwsSoftwareStatusUpgradeOperationalState = MibTableColumn((1, 3, 6, 1, 4, 1, 1271, 3, 4, 14, 3, 1, 3), UpgradeOpState()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cwsSoftwareStatusUpgradeOperationalState.setStatus('current')
cwsSoftwareStatusCommittedVersion = MibTableColumn((1, 3, 6, 1, 4, 1, 1271, 3, 4, 14, 3, 1, 4), StringMaxl32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cwsSoftwareStatusCommittedVersion.setStatus('current')
cwsSoftwareStatusActiveVersion = MibTableColumn((1, 3, 6, 1, 4, 1, 1271, 3, 4, 14, 3, 1, 5), StringMaxl32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cwsSoftwareStatusActiveVersion.setStatus('current')
cwsSoftwareStatusUpgradeToVersion = MibTableColumn((1, 3, 6, 1, 4, 1, 1271, 3, 4, 14, 3, 1, 6), StringMaxl32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cwsSoftwareStatusUpgradeToVersion.setStatus('current')
cwsSoftwareStatusLastOperation = MibTableColumn((1, 3, 6, 1, 4, 1, 1271, 3, 4, 14, 3, 1, 7), StringMaxl128()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cwsSoftwareStatusLastOperation.setStatus('current')
cwsSoftwareCheckStatusReportTable = MibTable((1, 3, 6, 1, 4, 1, 1271, 3, 4, 14, 4), )
if mibBuilder.loadTexts: cwsSoftwareCheckStatusReportTable.setStatus('current')
cwsSoftwareCheckStatusReportEntry = MibTableRow((1, 3, 6, 1, 4, 1, 1271, 3, 4, 14, 4, 1), ).setIndexNames((0, "CIENA-WS-SOFTWARE-MIB", "cwsSoftwareCheckStatusReportTableSnmpKey"))
if mibBuilder.loadTexts: cwsSoftwareCheckStatusReportEntry.setStatus('current')
cwsSoftwareCheckStatusReportTableSnmpKey = MibTableColumn((1, 3, 6, 1, 4, 1, 1271, 3, 4, 14, 4, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 2147483647)))
if mibBuilder.loadTexts: cwsSoftwareCheckStatusReportTableSnmpKey.setStatus('current')
cwsSoftwareCheckStatusReportActiveReleaseVersion = MibTableColumn((1, 3, 6, 1, 4, 1, 1271, 3, 4, 14, 4, 1, 2), StringMaxl32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cwsSoftwareCheckStatusReportActiveReleaseVersion.setStatus('current')
cwsSoftwareCheckStatusReportServerReleaseVersion = MibTableColumn((1, 3, 6, 1, 4, 1, 1271, 3, 4, 14, 4, 1, 3), StringMaxl32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cwsSoftwareCheckStatusReportServerReleaseVersion.setStatus('current')
cwsSoftwareCheckStatusReportLocalReleaseVersion = MibTableColumn((1, 3, 6, 1, 4, 1, 1271, 3, 4, 14, 4, 1, 4), StringMaxl32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cwsSoftwareCheckStatusReportLocalReleaseVersion.setStatus('current')
cwsSoftwareCheckStatusReportServerHostname = MibTableColumn((1, 3, 6, 1, 4, 1, 1271, 3, 4, 14, 4, 1, 5), StringMaxl32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cwsSoftwareCheckStatusReportServerHostname.setStatus('current')
cwsSoftwareCheckStatusReportServerPath = MibTableColumn((1, 3, 6, 1, 4, 1, 1271, 3, 4, 14, 4, 1, 6), StringMaxl256()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cwsSoftwareCheckStatusReportServerPath.setStatus('current')
cwsSoftwareCheckStatusReportTimestamp = MibTableColumn((1, 3, 6, 1, 4, 1, 1271, 3, 4, 14, 4, 1, 7), StringMaxl128()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cwsSoftwareCheckStatusReportTimestamp.setStatus('current')
cwsSoftwareCheckStatusReportCheckOperationalState = MibTableColumn((1, 3, 6, 1, 4, 1, 1271, 3, 4, 14, 4, 1, 8), SoftwareOpState()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cwsSoftwareCheckStatusReportCheckOperationalState.setStatus('current')
cwsSoftwareCheckStatusReportCheckUpgradeState = MibTableColumn((1, 3, 6, 1, 4, 1, 1271, 3, 4, 14, 4, 1, 9), UpgradeOpState()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cwsSoftwareCheckStatusReportCheckUpgradeState.setStatus('current')
cwsSoftwareCheckStatusReportRequiredActivationType = MibTableColumn((1, 3, 6, 1, 4, 1, 1271, 3, 4, 14, 4, 1, 10), StringMaxl32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cwsSoftwareCheckStatusReportRequiredActivationType.setStatus('current')
cwsSoftwareCheckStatusReportServiceInterruptionActivation = MibTableColumn((1, 3, 6, 1, 4, 1, 1271, 3, 4, 14, 4, 1, 11), TruthValue()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cwsSoftwareCheckStatusReportServiceInterruptionActivation.setStatus('current')
cwsSoftwareUpgradeServerTable = MibTable((1, 3, 6, 1, 4, 1, 1271, 3, 4, 14, 5), )
if mibBuilder.loadTexts: cwsSoftwareUpgradeServerTable.setStatus('current')
cwsSoftwareUpgradeServerEntry = MibTableRow((1, 3, 6, 1, 4, 1, 1271, 3, 4, 14, 5, 1), ).setIndexNames((0, "CIENA-WS-SOFTWARE-MIB", "cwsSoftwareUpgradeServerTableSnmpKey"))
if mibBuilder.loadTexts: cwsSoftwareUpgradeServerEntry.setStatus('current')
cwsSoftwareUpgradeServerTableSnmpKey = MibTableColumn((1, 3, 6, 1, 4, 1, 1271, 3, 4, 14, 5, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 2147483647)))
if mibBuilder.loadTexts: cwsSoftwareUpgradeServerTableSnmpKey.setStatus('current')
cwsSoftwareUpgradeServerIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 1271, 3, 4, 14, 5, 1, 2), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cwsSoftwareUpgradeServerIndex.setStatus('current')
cwsSoftwareUpgradeServerServer = MibTableColumn((1, 3, 6, 1, 4, 1, 1271, 3, 4, 14, 5, 1, 3), StringMaxl64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cwsSoftwareUpgradeServerServer.setStatus('current')
cwsSoftwareUpgradeServerMode = MibTableColumn((1, 3, 6, 1, 4, 1, 1271, 3, 4, 14, 5, 1, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3))).clone(namedValues=NamedValues(("tftp", 0), ("ftp", 1), ("sftp", 2), ("scp", 3)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: cwsSoftwareUpgradeServerMode.setStatus('current')
cwsSoftwareUpgradeServerRemotePath = MibTableColumn((1, 3, 6, 1, 4, 1, 1271, 3, 4, 14, 5, 1, 5), OctetString().subtype(subtypeSpec=ValueSizeConstraint(0, 256))).setMaxAccess("readonly")
if mibBuilder.loadTexts: cwsSoftwareUpgradeServerRemotePath.setStatus('current')
cwsSoftwareUpgradeServerLoginId = MibTableColumn((1, 3, 6, 1, 4, 1, 1271, 3, 4, 14, 5, 1, 6), StringMaxl32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cwsSoftwareUpgradeServerLoginId.setStatus('current')
cwsSoftwareUpgradeServerPassword = MibTableColumn((1, 3, 6, 1, 4, 1, 1271, 3, 4, 14, 5, 1, 7), StringMaxl32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cwsSoftwareUpgradeServerPassword.setStatus('current')
cwsSoftwareUpgradeLogListTable = MibTable((1, 3, 6, 1, 4, 1, 1271, 3, 4, 14, 6), )
if mibBuilder.loadTexts: cwsSoftwareUpgradeLogListTable.setStatus('current')
cwsSoftwareUpgradeLogListEntry = MibTableRow((1, 3, 6, 1, 4, 1, 1271, 3, 4, 14, 6, 1), ).setIndexNames((0, "CIENA-WS-SOFTWARE-MIB", "cwsSoftwareUpgradeLogListLogIndex"))
if mibBuilder.loadTexts: cwsSoftwareUpgradeLogListEntry.setStatus('current')
cwsSoftwareUpgradeLogListLogIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 1271, 3, 4, 14, 6, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 2147483647)))
if mibBuilder.loadTexts: cwsSoftwareUpgradeLogListLogIndex.setStatus('current')
cwsSoftwareUpgradeLogListDateAndTime = MibTableColumn((1, 3, 6, 1, 4, 1, 1271, 3, 4, 14, 6, 1, 2), StringMaxl64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cwsSoftwareUpgradeLogListDateAndTime.setStatus('current')
cwsSoftwareUpgradeLogListText = MibTableColumn((1, 3, 6, 1, 4, 1, 1271, 3, 4, 14, 6, 1, 3), StringMaxl256()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cwsSoftwareUpgradeLogListText.setStatus('current')
cwsSoftwareActiveSoftwareTable = MibTable((1, 3, 6, 1, 4, 1, 1271, 3, 4, 14, 7), )
if mibBuilder.loadTexts: cwsSoftwareActiveSoftwareTable.setStatus('current')
cwsSoftwareActiveSoftwareEntry = MibTableRow((1, 3, 6, 1, 4, 1, 1271, 3, 4, 14, 7, 1), ).setIndexNames((0, "CIENA-WS-SOFTWARE-MIB", "cwsSoftwareActiveSoftwareTableSnmpKey"))
if mibBuilder.loadTexts: cwsSoftwareActiveSoftwareEntry.setStatus('current')
cwsSoftwareActiveSoftwareTableSnmpKey = MibTableColumn((1, 3, 6, 1, 4, 1, 1271, 3, 4, 14, 7, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 2147483647)))
if mibBuilder.loadTexts: cwsSoftwareActiveSoftwareTableSnmpKey.setStatus('current')
cwsSoftwareActiveSoftwareVersion = MibTableColumn((1, 3, 6, 1, 4, 1, 1271, 3, 4, 14, 7, 1, 2), StringMaxl32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cwsSoftwareActiveSoftwareVersion.setStatus('current')
cwsSoftwareActiveSoftwareBuildNumber = MibTableColumn((1, 3, 6, 1, 4, 1, 1271, 3, 4, 14, 7, 1, 3), StringMaxl32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cwsSoftwareActiveSoftwareBuildNumber.setStatus('current')
cwsSoftwareActiveSoftwareBuildDate = MibTableColumn((1, 3, 6, 1, 4, 1, 1271, 3, 4, 14, 7, 1, 4), StringMaxl32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cwsSoftwareActiveSoftwareBuildDate.setStatus('current')
cwsSoftwareActiveSoftwareCatalogName = MibTableColumn((1, 3, 6, 1, 4, 1, 1271, 3, 4, 14, 7, 1, 5), StringMaxl64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cwsSoftwareActiveSoftwareCatalogName.setStatus('current')
cwsSoftwareActiveSoftwareNumberOfComponents = MibTableColumn((1, 3, 6, 1, 4, 1, 1271, 3, 4, 14, 7, 1, 6), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cwsSoftwareActiveSoftwareNumberOfComponents.setStatus('current')
cwsSoftwareActivecomponentsTable = MibTable((1, 3, 6, 1, 4, 1, 1271, 3, 4, 14, 8), )
if mibBuilder.loadTexts: cwsSoftwareActivecomponentsTable.setStatus('current')
cwsSoftwareActivecomponentsEntry = MibTableRow((1, 3, 6, 1, 4, 1, 1271, 3, 4, 14, 8, 1), ).setIndexNames((0, "CIENA-WS-SOFTWARE-MIB", "cwsSoftwareActivecomponentsComponentIndex"))
if mibBuilder.loadTexts: cwsSoftwareActivecomponentsEntry.setStatus('current')
cwsSoftwareActivecomponentsComponentIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 1271, 3, 4, 14, 8, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 2147483647)))
if mibBuilder.loadTexts: cwsSoftwareActivecomponentsComponentIndex.setStatus('current')
cwsSoftwareActivecomponentsName = MibTableColumn((1, 3, 6, 1, 4, 1, 1271, 3, 4, 14, 8, 1, 2), StringMaxl32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cwsSoftwareActivecomponentsName.setStatus('current')
cwsSoftwareActivecomponentsVersion = MibTableColumn((1, 3, 6, 1, 4, 1, 1271, 3, 4, 14, 8, 1, 3), StringMaxl32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cwsSoftwareActivecomponentsVersion.setStatus('current')
cwsSoftwareActivecomponentsBuildNumber = MibTableColumn((1, 3, 6, 1, 4, 1, 1271, 3, 4, 14, 8, 1, 4), StringMaxl32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cwsSoftwareActivecomponentsBuildNumber.setStatus('current')
cwsSoftwareActivecomponentsStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 1271, 3, 4, 14, 8, 1, 5), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3, 4))).clone(namedValues=NamedValues(("unknown", 0), ("active", 1), ("failed", 2), ("pending", 3), ("restarting", 4)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: cwsSoftwareActivecomponentsStatus.setStatus('current')
cwsSoftwareBootPartitionListTable = MibTable((1, 3, 6, 1, 4, 1, 1271, 3, 4, 14, 9), )
if mibBuilder.loadTexts: cwsSoftwareBootPartitionListTable.setStatus('current')
cwsSoftwareBootPartitionListEntry = MibTableRow((1, 3, 6, 1, 4, 1, 1271, 3, 4, 14, 9, 1), ).setIndexNames((0, "CIENA-WS-SOFTWARE-MIB", "cwsSoftwareBootPartitionListIndex"))
if mibBuilder.loadTexts: cwsSoftwareBootPartitionListEntry.setStatus('current')
cwsSoftwareBootPartitionListIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 1271, 3, 4, 14, 9, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 2147483647)))
if mibBuilder.loadTexts: cwsSoftwareBootPartitionListIndex.setStatus('current')
cwsSoftwareBootPartitionListName = MibTableColumn((1, 3, 6, 1, 4, 1, 1271, 3, 4, 14, 9, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3, 4, 5, 6, 7))).clone(namedValues=NamedValues(("unknown", 0), ("kernel0", 1), ("bootloader0", 2), ("kernel1", 3), ("bootloader1", 4), ("firmware0", 5), ("firmware1", 6), ("backupbl", 7)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: cwsSoftwareBootPartitionListName.setStatus('current')
cwsSoftwareBootPartitionListVersion = MibTableColumn((1, 3, 6, 1, 4, 1, 1271, 3, 4, 14, 9, 1, 3), StringMaxl32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cwsSoftwareBootPartitionListVersion.setStatus('current')
cwsSoftwareBootPartitionListDate = MibTableColumn((1, 3, 6, 1, 4, 1, 1271, 3, 4, 14, 9, 1, 4), StringMaxl32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cwsSoftwareBootPartitionListDate.setStatus('current')
cwsSoftwareBootPartitionListState = MibTableColumn((1, 3, 6, 1, 4, 1, 1271, 3, 4, 14, 9, 1, 5), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3))).clone(namedValues=NamedValues(("unknown", 0), ("active", 1), ("standby", 2), ("notapplicable", 3)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: cwsSoftwareBootPartitionListState.setStatus('current')
cwsSoftwareBootPartitionListIntegrityCheck = MibTableColumn((1, 3, 6, 1, 4, 1, 1271, 3, 4, 14, 9, 1, 6), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1, 2))).clone(namedValues=NamedValues(("unknown", 0), ("pass", 1), ("invalid", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: cwsSoftwareBootPartitionListIntegrityCheck.setStatus('current')
cwsSoftwareVersionsTable = MibTable((1, 3, 6, 1, 4, 1, 1271, 3, 4, 14, 10), )
if mibBuilder.loadTexts: cwsSoftwareVersionsTable.setStatus('current')
cwsSoftwareVersionsEntry = MibTableRow((1, 3, 6, 1, 4, 1, 1271, 3, 4, 14, 10, 1), ).setIndexNames((0, "CIENA-WS-SOFTWARE-MIB", "cwsSoftwareVersionsIndex"))
if mibBuilder.loadTexts: cwsSoftwareVersionsEntry.setStatus('current')
cwsSoftwareVersionsIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 1271, 3, 4, 14, 10, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 2147483647)))
if mibBuilder.loadTexts: cwsSoftwareVersionsIndex.setStatus('current')
cwsSoftwareVersionsVersion = MibTableColumn((1, 3, 6, 1, 4, 1, 1271, 3, 4, 14, 10, 1, 2), StringMaxl32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cwsSoftwareVersionsVersion.setStatus('current')
cwsSoftwareVersionsBuildNumber = MibTableColumn((1, 3, 6, 1, 4, 1, 1271, 3, 4, 14, 10, 1, 3), StringMaxl32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cwsSoftwareVersionsBuildNumber.setStatus('current')
cwsSoftwareVersionsBuildTag = MibTableColumn((1, 3, 6, 1, 4, 1, 1271, 3, 4, 14, 10, 1, 4), StringMaxl32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cwsSoftwareVersionsBuildTag.setStatus('current')
cwsSoftwareVersionsBuildDate = MibTableColumn((1, 3, 6, 1, 4, 1, 1271, 3, 4, 14, 10, 1, 5), StringMaxl32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cwsSoftwareVersionsBuildDate.setStatus('current')
cwsSoftwareVersionsSize = MibTableColumn((1, 3, 6, 1, 4, 1, 1271, 3, 4, 14, 10, 1, 6), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cwsSoftwareVersionsSize.setStatus('current')
cwsSoftwareVersionsNumberOfComponents = MibTableColumn((1, 3, 6, 1, 4, 1, 1271, 3, 4, 14, 10, 1, 7), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cwsSoftwareVersionsNumberOfComponents.setStatus('current')
cwsSoftwareInstalledcomponentsTable = MibTable((1, 3, 6, 1, 4, 1, 1271, 3, 4, 14, 11), )
if mibBuilder.loadTexts: cwsSoftwareInstalledcomponentsTable.setStatus('current')
cwsSoftwareInstalledcomponentsEntry = MibTableRow((1, 3, 6, 1, 4, 1, 1271, 3, 4, 14, 11, 1), ).setIndexNames((0, "CIENA-WS-SOFTWARE-MIB", "cwsSoftwareVersionsIndex"), (0, "CIENA-WS-SOFTWARE-MIB", "cwsSoftwareInstalledcomponentsComponentIndex"))
if mibBuilder.loadTexts: cwsSoftwareInstalledcomponentsEntry.setStatus('current')
cwsSoftwareInstalledcomponentsComponentIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 1271, 3, 4, 14, 11, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 2147483647)))
if mibBuilder.loadTexts: cwsSoftwareInstalledcomponentsComponentIndex.setStatus('current')
cwsSoftwareInstalledcomponentsName = MibTableColumn((1, 3, 6, 1, 4, 1, 1271, 3, 4, 14, 11, 1, 2), StringMaxl32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cwsSoftwareInstalledcomponentsName.setStatus('current')
cwsSoftwareInstalledcomponentsVersion = MibTableColumn((1, 3, 6, 1, 4, 1, 1271, 3, 4, 14, 11, 1, 3), StringMaxl32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cwsSoftwareInstalledcomponentsVersion.setStatus('current')
cwsSoftwareInstalledcomponentsBuildNumber = MibTableColumn((1, 3, 6, 1, 4, 1, 1271, 3, 4, 14, 11, 1, 4), StringMaxl32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cwsSoftwareInstalledcomponentsBuildNumber.setStatus('current')
cwsSoftwareInstalledcomponentsBuildTag = MibTableColumn((1, 3, 6, 1, 4, 1, 1271, 3, 4, 14, 11, 1, 5), StringMaxl32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cwsSoftwareInstalledcomponentsBuildTag.setStatus('current')
cwsSoftwareInstalledcomponentsBuildTimestamp = MibTableColumn((1, 3, 6, 1, 4, 1, 1271, 3, 4, 14, 11, 1, 6), StringMaxl32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cwsSoftwareInstalledcomponentsBuildTimestamp.setStatus('current')
cwsSoftwareInstalledcomponentsBuildSize = MibTableColumn((1, 3, 6, 1, 4, 1, 1271, 3, 4, 14, 11, 1, 7), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cwsSoftwareInstalledcomponentsBuildSize.setStatus('current')
cienaWsSoftwareObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 1271, 3, 4, 14, 1))
cienaWsSoftwareConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 1271, 3, 4, 14, 2))
cienaWsSoftwareGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 1271, 3, 4, 14, 2, 1))
cienaWsSoftwareGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 1271, 3, 4, 14, 2, 1, 1)).setObjects(("CIENA-WS-SOFTWARE-MIB", "cwsSoftwareStatusSoftwareOperationalState"), ("CIENA-WS-SOFTWARE-MIB", "cwsSoftwareStatusUpgradeOperationalState"), ("CIENA-WS-SOFTWARE-MIB", "cwsSoftwareStatusCommittedVersion"), ("CIENA-WS-SOFTWARE-MIB", "cwsSoftwareStatusActiveVersion"), ("CIENA-WS-SOFTWARE-MIB", "cwsSoftwareStatusUpgradeToVersion"), ("CIENA-WS-SOFTWARE-MIB", "cwsSoftwareStatusLastOperation"), ("CIENA-WS-SOFTWARE-MIB", "cwsSoftwareCheckStatusReportActiveReleaseVersion"), ("CIENA-WS-SOFTWARE-MIB", "cwsSoftwareCheckStatusReportServerReleaseVersion"), ("CIENA-WS-SOFTWARE-MIB", "cwsSoftwareCheckStatusReportLocalReleaseVersion"), ("CIENA-WS-SOFTWARE-MIB", "cwsSoftwareCheckStatusReportServerHostname"), ("CIENA-WS-SOFTWARE-MIB", "cwsSoftwareCheckStatusReportServerPath"), ("CIENA-WS-SOFTWARE-MIB", "cwsSoftwareCheckStatusReportTimestamp"), ("CIENA-WS-SOFTWARE-MIB", "cwsSoftwareCheckStatusReportCheckOperationalState"), ("CIENA-WS-SOFTWARE-MIB", "cwsSoftwareCheckStatusReportCheckUpgradeState"), ("CIENA-WS-SOFTWARE-MIB", "cwsSoftwareCheckStatusReportRequiredActivationType"), ("CIENA-WS-SOFTWARE-MIB", "cwsSoftwareCheckStatusReportServiceInterruptionActivation"), ("CIENA-WS-SOFTWARE-MIB", "cwsSoftwareUpgradeServerIndex"), ("CIENA-WS-SOFTWARE-MIB", "cwsSoftwareUpgradeServerServer"), ("CIENA-WS-SOFTWARE-MIB", "cwsSoftwareUpgradeServerMode"), ("CIENA-WS-SOFTWARE-MIB", "cwsSoftwareUpgradeServerRemotePath"), ("CIENA-WS-SOFTWARE-MIB", "cwsSoftwareUpgradeServerLoginId"), ("CIENA-WS-SOFTWARE-MIB", "cwsSoftwareUpgradeServerPassword"), ("CIENA-WS-SOFTWARE-MIB", "cwsSoftwareUpgradeLogListDateAndTime"), ("CIENA-WS-SOFTWARE-MIB", "cwsSoftwareUpgradeLogListText"), ("CIENA-WS-SOFTWARE-MIB", "cwsSoftwareActiveSoftwareVersion"), ("CIENA-WS-SOFTWARE-MIB", "cwsSoftwareActiveSoftwareBuildNumber"), ("CIENA-WS-SOFTWARE-MIB", "cwsSoftwareActiveSoftwareBuildDate"), ("CIENA-WS-SOFTWARE-MIB", "cwsSoftwareActiveSoftwareCatalogName"), ("CIENA-WS-SOFTWARE-MIB", "cwsSoftwareActiveSoftwareNumberOfComponents"), ("CIENA-WS-SOFTWARE-MIB", "cwsSoftwareActivecomponentsName"), ("CIENA-WS-SOFTWARE-MIB", "cwsSoftwareActivecomponentsVersion"), ("CIENA-WS-SOFTWARE-MIB", "cwsSoftwareActivecomponentsBuildNumber"), ("CIENA-WS-SOFTWARE-MIB", "cwsSoftwareActivecomponentsStatus"), ("CIENA-WS-SOFTWARE-MIB", "cwsSoftwareBootPartitionListName"), ("CIENA-WS-SOFTWARE-MIB", "cwsSoftwareBootPartitionListVersion"), ("CIENA-WS-SOFTWARE-MIB", "cwsSoftwareBootPartitionListDate"), ("CIENA-WS-SOFTWARE-MIB", "cwsSoftwareBootPartitionListState"), ("CIENA-WS-SOFTWARE-MIB", "cwsSoftwareBootPartitionListIntegrityCheck"), ("CIENA-WS-SOFTWARE-MIB", "cwsSoftwareVersionsVersion"), ("CIENA-WS-SOFTWARE-MIB", "cwsSoftwareVersionsBuildNumber"), ("CIENA-WS-SOFTWARE-MIB", "cwsSoftwareVersionsBuildTag"), ("CIENA-WS-SOFTWARE-MIB", "cwsSoftwareVersionsBuildDate"), ("CIENA-WS-SOFTWARE-MIB", "cwsSoftwareVersionsSize"), ("CIENA-WS-SOFTWARE-MIB", "cwsSoftwareVersionsNumberOfComponents"), ("CIENA-WS-SOFTWARE-MIB", "cwsSoftwareInstalledcomponentsName"), ("CIENA-WS-SOFTWARE-MIB", "cwsSoftwareInstalledcomponentsVersion"), ("CIENA-WS-SOFTWARE-MIB", "cwsSoftwareInstalledcomponentsBuildNumber"), ("CIENA-WS-SOFTWARE-MIB", "cwsSoftwareInstalledcomponentsBuildTag"), ("CIENA-WS-SOFTWARE-MIB", "cwsSoftwareInstalledcomponentsBuildTimestamp"), ("CIENA-WS-SOFTWARE-MIB", "cwsSoftwareInstalledcomponentsBuildSize"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cienaWsSoftwareGroup = cienaWsSoftwareGroup.setStatus('current')
cienaWsSoftwareCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 1271, 3, 4, 14, 2, 2))
cienaWsSoftwareCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 1271, 3, 4, 14, 2, 2, 1)).setObjects(("CIENA-WS-SOFTWARE-MIB", "cienaWsSoftwareGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cienaWsSoftwareCompliance = cienaWsSoftwareCompliance.setStatus('current')
mibBuilder.exportSymbols("CIENA-WS-SOFTWARE-MIB", cwsSoftwareStatusUpgradeOperationalState=cwsSoftwareStatusUpgradeOperationalState, cienaWsSoftwareObjects=cienaWsSoftwareObjects, cwsSoftwareUpgradeLogListTable=cwsSoftwareUpgradeLogListTable, cwsSoftwareUpgradeServerTableSnmpKey=cwsSoftwareUpgradeServerTableSnmpKey, cwsSoftwareUpgradeServerPassword=cwsSoftwareUpgradeServerPassword, cwsSoftwareActivecomponentsName=cwsSoftwareActivecomponentsName, cwsSoftwareCheckStatusReportEntry=cwsSoftwareCheckStatusReportEntry, cwsSoftwareCheckStatusReportServerHostname=cwsSoftwareCheckStatusReportServerHostname, cwsSoftwareActiveSoftwareVersion=cwsSoftwareActiveSoftwareVersion, cwsSoftwareUpgradeServerTable=cwsSoftwareUpgradeServerTable, cwsSoftwareInstalledcomponentsBuildSize=cwsSoftwareInstalledcomponentsBuildSize, cwsSoftwareActivecomponentsEntry=cwsSoftwareActivecomponentsEntry, cwsSoftwareCheckStatusReportTable=cwsSoftwareCheckStatusReportTable, cwsSoftwareActiveSoftwareEntry=cwsSoftwareActiveSoftwareEntry, cwsSoftwareActiveSoftwareNumberOfComponents=cwsSoftwareActiveSoftwareNumberOfComponents, cwsSoftwareVersionsVersion=cwsSoftwareVersionsVersion, cwsSoftwareVersionsBuildNumber=cwsSoftwareVersionsBuildNumber, cwsSoftwareStatusEntry=cwsSoftwareStatusEntry, cienaWsSoftwareGroup=cienaWsSoftwareGroup, cwsSoftwareBootPartitionListName=cwsSoftwareBootPartitionListName, cienaWsSoftwareConformance=cienaWsSoftwareConformance, cwsSoftwareActiveSoftwareTableSnmpKey=cwsSoftwareActiveSoftwareTableSnmpKey, cwsSoftwareVersionsNumberOfComponents=cwsSoftwareVersionsNumberOfComponents, cwsSoftwareStatusLastOperation=cwsSoftwareStatusLastOperation, cwsSoftwareActiveSoftwareTable=cwsSoftwareActiveSoftwareTable, cienaWsSoftwareCompliances=cienaWsSoftwareCompliances, cwsSoftwareVersionsSize=cwsSoftwareVersionsSize, cwsSoftwareStatusActiveVersion=cwsSoftwareStatusActiveVersion, PYSNMP_MODULE_ID=cienaWsSoftwareMIB, cwsSoftwareUpgradeLogListEntry=cwsSoftwareUpgradeLogListEntry, cwsSoftwareStatusCommittedVersion=cwsSoftwareStatusCommittedVersion, cwsSoftwareBootPartitionListIndex=cwsSoftwareBootPartitionListIndex, SoftwareRtncode=SoftwareRtncode, cwsSoftwareActivecomponentsVersion=cwsSoftwareActivecomponentsVersion, cwsSoftwareCheckStatusReportServiceInterruptionActivation=cwsSoftwareCheckStatusReportServiceInterruptionActivation, cwsSoftwareActivecomponentsComponentIndex=cwsSoftwareActivecomponentsComponentIndex, cwsSoftwareStatusTable=cwsSoftwareStatusTable, cwsSoftwareStatusTableSnmpKey=cwsSoftwareStatusTableSnmpKey, cwsSoftwareCheckStatusReportCheckOperationalState=cwsSoftwareCheckStatusReportCheckOperationalState, cwsSoftwareCheckStatusReportRequiredActivationType=cwsSoftwareCheckStatusReportRequiredActivationType, cwsSoftwareCheckStatusReportServerPath=cwsSoftwareCheckStatusReportServerPath, cwsSoftwareUpgradeServerRemotePath=cwsSoftwareUpgradeServerRemotePath, cwsSoftwareCheckStatusReportTimestamp=cwsSoftwareCheckStatusReportTimestamp, cwsSoftwareBootPartitionListDate=cwsSoftwareBootPartitionListDate, UpgradeOpState=UpgradeOpState, cwsSoftwareBootPartitionListEntry=cwsSoftwareBootPartitionListEntry, cwsSoftwareActiveSoftwareBuildNumber=cwsSoftwareActiveSoftwareBuildNumber, cwsSoftwareActivecomponentsBuildNumber=cwsSoftwareActivecomponentsBuildNumber, cwsSoftwareBootPartitionListState=cwsSoftwareBootPartitionListState, cwsSoftwareVersionsIndex=cwsSoftwareVersionsIndex, cwsSoftwareCheckStatusReportActiveReleaseVersion=cwsSoftwareCheckStatusReportActiveReleaseVersion, cwsSoftwareVersionsBuildDate=cwsSoftwareVersionsBuildDate, cwsSoftwareInstalledcomponentsBuildTimestamp=cwsSoftwareInstalledcomponentsBuildTimestamp, cwsSoftwareInstalledcomponentsName=cwsSoftwareInstalledcomponentsName, cwsSoftwareCheckStatusReportServerReleaseVersion=cwsSoftwareCheckStatusReportServerReleaseVersion, cwsSoftwareInstalledcomponentsTable=cwsSoftwareInstalledcomponentsTable, SoftwareOpState=SoftwareOpState, cwsSoftwareActivecomponentsStatus=cwsSoftwareActivecomponentsStatus, cwsSoftwareInstalledcomponentsComponentIndex=cwsSoftwareInstalledcomponentsComponentIndex, cwsSoftwareUpgradeLogListLogIndex=cwsSoftwareUpgradeLogListLogIndex, cwsSoftwareVersionsBuildTag=cwsSoftwareVersionsBuildTag, cienaWsSoftwareGroups=cienaWsSoftwareGroups, cwsSoftwareUpgradeLogListDateAndTime=cwsSoftwareUpgradeLogListDateAndTime, cwsSoftwareBootPartitionListIntegrityCheck=cwsSoftwareBootPartitionListIntegrityCheck, cwsSoftwareBootPartitionListTable=cwsSoftwareBootPartitionListTable, cienaWsSoftwareMIB=cienaWsSoftwareMIB, cwsSoftwareInstalledcomponentsBuildTag=cwsSoftwareInstalledcomponentsBuildTag, cwsSoftwareUpgradeServerIndex=cwsSoftwareUpgradeServerIndex, cwsSoftwareInstalledcomponentsVersion=cwsSoftwareInstalledcomponentsVersion, cwsSoftwareInstalledcomponentsBuildNumber=cwsSoftwareInstalledcomponentsBuildNumber, cwsSoftwareActiveSoftwareCatalogName=cwsSoftwareActiveSoftwareCatalogName, cwsSoftwareUpgradeServerEntry=cwsSoftwareUpgradeServerEntry, cwsSoftwareInstalledcomponentsEntry=cwsSoftwareInstalledcomponentsEntry, cwsSoftwareCheckStatusReportLocalReleaseVersion=cwsSoftwareCheckStatusReportLocalReleaseVersion, cwsSoftwareUpgradeServerLoginId=cwsSoftwareUpgradeServerLoginId, cwsSoftwareUpgradeServerServer=cwsSoftwareUpgradeServerServer, cwsSoftwareUpgradeServerMode=cwsSoftwareUpgradeServerMode, cwsSoftwareVersionsEntry=cwsSoftwareVersionsEntry, cwsSoftwareCheckStatusReportTableSnmpKey=cwsSoftwareCheckStatusReportTableSnmpKey, cwsSoftwareActivecomponentsTable=cwsSoftwareActivecomponentsTable, cwsSoftwareStatusSoftwareOperationalState=cwsSoftwareStatusSoftwareOperationalState, cwsSoftwareStatusUpgradeToVersion=cwsSoftwareStatusUpgradeToVersion, cwsSoftwareVersionsTable=cwsSoftwareVersionsTable, cwsSoftwareCheckStatusReportCheckUpgradeState=cwsSoftwareCheckStatusReportCheckUpgradeState, cienaWsSoftwareCompliance=cienaWsSoftwareCompliance, cwsSoftwareUpgradeLogListText=cwsSoftwareUpgradeLogListText, cwsSoftwareActiveSoftwareBuildDate=cwsSoftwareActiveSoftwareBuildDate, cwsSoftwareBootPartitionListVersion=cwsSoftwareBootPartitionListVersion)
