#
# PySNMP MIB module Juniper-TACACS-Plus-Client-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/Juniper-TACACS-Plus-Client-MIB
# Produced by pysmi-0.3.4 at Wed May  1 14:04:32 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
OctetString, ObjectIdentifier, Integer = mibBuilder.importSymbols("ASN1", "OctetString", "ObjectIdentifier", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, ConstraintsIntersection, SingleValueConstraint, ConstraintsUnion, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "ConstraintsIntersection", "SingleValueConstraint", "ConstraintsUnion", "ValueSizeConstraint")
juniMibs, = mibBuilder.importSymbols("Juniper-MIBs", "juniMibs")
ModuleCompliance, ObjectGroup, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "ObjectGroup", "NotificationGroup")
Bits, TimeTicks, ObjectIdentity, NotificationType, Unsigned32, MibIdentifier, IpAddress, Counter64, iso, Counter32, Gauge32, Integer32, ModuleIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn = mibBuilder.importSymbols("SNMPv2-SMI", "Bits", "TimeTicks", "ObjectIdentity", "NotificationType", "Unsigned32", "MibIdentifier", "IpAddress", "Counter64", "iso", "Counter32", "Gauge32", "Integer32", "ModuleIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn")
TruthValue, TimeStamp, DisplayString, TextualConvention, RowStatus = mibBuilder.importSymbols("SNMPv2-TC", "TruthValue", "TimeStamp", "DisplayString", "TextualConvention", "RowStatus")
juniTacacsPlusClientMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 4874, 2, 2, 60))
juniTacacsPlusClientMIB.setRevisions(('2004-03-02 17:31', '2002-09-16 21:44', '2002-07-12 13:49',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: juniTacacsPlusClientMIB.setRevisionsDescriptions(('Added juniTacacsPlusClientHostOrder to juniTacacsPlusClientHostConfigTable.', 'Replaced Unisphere names with Juniper names.', 'Initial version of this MIB module.',))
if mibBuilder.loadTexts: juniTacacsPlusClientMIB.setLastUpdated('200403021731Z')
if mibBuilder.loadTexts: juniTacacsPlusClientMIB.setOrganization('Juniper Networks, Inc.')
if mibBuilder.loadTexts: juniTacacsPlusClientMIB.setContactInfo(' Juniper Networks, Inc. Postal: 10 Technology Park Drive Westford, MA 01886-3146 USA Tel: +1 978 589 5800 Email: mib@Juniper.net')
if mibBuilder.loadTexts: juniTacacsPlusClientMIB.setDescription('The Terminal Access Controller Access Control System Plus (TACACS+) Client MIB for the Juniper Networks enterprise.')
class JuniKeyString(TextualConvention, OctetString):
    description = 'A string to keep a TACACS+ key. It may contain TAB character and/or any character from 0x20 to 0x7e inclusive. Its lenght is limited to 100. For security reasons it always reads as an empty string.'
    status = 'current'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(0, 100)

juniTacacsPlusClientObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 4874, 2, 2, 60, 1))
juniTacacsPlusClientCommonConfig = MibIdentifier((1, 3, 6, 1, 4, 1, 4874, 2, 2, 60, 1, 1))
juniTacacsPlusClientHostConfig = MibIdentifier((1, 3, 6, 1, 4, 1, 4874, 2, 2, 60, 1, 2))
juniTacacsPlusClientHostStats = MibIdentifier((1, 3, 6, 1, 4, 1, 4874, 2, 2, 60, 1, 3))
juniTacacsPlusClientDirectedRequest = MibScalar((1, 3, 6, 1, 4, 1, 4874, 2, 2, 60, 1, 1, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5))).clone(namedValues=NamedValues(("notRestrictedAndTruncated", 1), ("disabled", 2), ("notRestrictedAndNotTruncated", 3), ("restrictedAndTruncated", 4), ("restrictedAndNotTruncated", 5)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: juniTacacsPlusClientDirectedRequest.setStatus('current')
if mibBuilder.loadTexts: juniTacacsPlusClientDirectedRequest.setDescription("This object represents directed-request option setting. In any of the enabled enabled states user name entered as `user@host' will be sent to specified host fot authentication. If `restricted' is in effect and the specified host is not available client would not try to use other hosts, if `truncated' is in effect, then `@host' part will be stripped before submission for authentication.")
juniTacacsPlusClientTimeout = MibScalar((1, 3, 6, 1, 4, 1, 4874, 2, 2, 60, 1, 1, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 255))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: juniTacacsPlusClientTimeout.setStatus('current')
if mibBuilder.loadTexts: juniTacacsPlusClientTimeout.setDescription("TACACS+ host response timeout in seconds. Value 0 means 'not configured, it this case built-in internal timeout value will be used.")
juniTacacsPlusClientKey = MibScalar((1, 3, 6, 1, 4, 1, 4874, 2, 2, 60, 1, 1, 3), JuniKeyString()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: juniTacacsPlusClientKey.setStatus('current')
if mibBuilder.loadTexts: juniTacacsPlusClientKey.setDescription('If the size is non-zero, packets passed between host and client will be encrypted.')
juniTacacsPlusClientSourceIp = MibScalar((1, 3, 6, 1, 4, 1, 4874, 2, 2, 60, 1, 1, 4), IpAddress()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: juniTacacsPlusClientSourceIp.setStatus('current')
if mibBuilder.loadTexts: juniTacacsPlusClientSourceIp.setDescription('If the value is is not 0.0.0.0 client will use this address as a source IP address for communication with servers. Changing this value would not affect existing connections.')
juniTacacsPlusClientHostConfigTable = MibTable((1, 3, 6, 1, 4, 1, 4874, 2, 2, 60, 1, 2, 1), )
if mibBuilder.loadTexts: juniTacacsPlusClientHostConfigTable.setStatus('current')
if mibBuilder.loadTexts: juniTacacsPlusClientHostConfigTable.setDescription('This table contains per host configuration parameters.')
juniTacacsPlusClientHostConfigEntry = MibTableRow((1, 3, 6, 1, 4, 1, 4874, 2, 2, 60, 1, 2, 1, 1), ).setIndexNames((0, "Juniper-TACACS-Plus-Client-MIB", "juniTacacsPlusClientHostAddr"))
if mibBuilder.loadTexts: juniTacacsPlusClientHostConfigEntry.setStatus('current')
if mibBuilder.loadTexts: juniTacacsPlusClientHostConfigEntry.setDescription('A TACACS+ host statistics table entry.')
juniTacacsPlusClientHostAddr = MibTableColumn((1, 3, 6, 1, 4, 1, 4874, 2, 2, 60, 1, 2, 1, 1, 1), IpAddress())
if mibBuilder.loadTexts: juniTacacsPlusClientHostAddr.setStatus('current')
if mibBuilder.loadTexts: juniTacacsPlusClientHostAddr.setDescription('The IP address of the host.')
juniTacacsPlusClientHostPort = MibTableColumn((1, 3, 6, 1, 4, 1, 4874, 2, 2, 60, 1, 2, 1, 1, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 65535)).clone(49)).setMaxAccess("readcreate")
if mibBuilder.loadTexts: juniTacacsPlusClientHostPort.setStatus('current')
if mibBuilder.loadTexts: juniTacacsPlusClientHostPort.setDescription('The TCP port of the host.')
juniTacacsPlusClientHostPrimary = MibTableColumn((1, 3, 6, 1, 4, 1, 4874, 2, 2, 60, 1, 2, 1, 1, 3), TruthValue().clone('false')).setMaxAccess("readcreate")
if mibBuilder.loadTexts: juniTacacsPlusClientHostPrimary.setStatus('current')
if mibBuilder.loadTexts: juniTacacsPlusClientHostPrimary.setDescription('Non-directed requests are submitted to the primary host first. There is only one primary host in the table. So, setting this object to true, will also change the value of this object in the current primary host. If primary host is deleted or reset, system will assing new primary host. When the first entry is created it becomes primary regardless of the value of this object.')
juniTacacsPlusClientHostSingleConnection = MibTableColumn((1, 3, 6, 1, 4, 1, 4874, 2, 2, 60, 1, 2, 1, 1, 4), TruthValue().clone('false')).setMaxAccess("readcreate")
if mibBuilder.loadTexts: juniTacacsPlusClientHostSingleConnection.setStatus('current')
if mibBuilder.loadTexts: juniTacacsPlusClientHostSingleConnection.setDescription('Traditionally TACACS+ client creates a new TCP connection for every session. If this value is true then TACACS+ client will try to use single connection if supported both by client implementation and by the host.')
juniTacacsPlusClientHostTimeout = MibTableColumn((1, 3, 6, 1, 4, 1, 4874, 2, 2, 60, 1, 2, 1, 1, 5), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 255))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: juniTacacsPlusClientHostTimeout.setStatus('current')
if mibBuilder.loadTexts: juniTacacsPlusClientHostTimeout.setDescription('TACACS+ host response timeout in seconds. If the value is 0 then the value of juniTacacsPlusClientTimeout will be used instead.')
juniTacacsPlusClientHostKey = MibTableColumn((1, 3, 6, 1, 4, 1, 4874, 2, 2, 60, 1, 2, 1, 1, 6), JuniKeyString()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: juniTacacsPlusClientHostKey.setStatus('current')
if mibBuilder.loadTexts: juniTacacsPlusClientHostKey.setDescription('If size is non-zero, packets passed between host and client will be encrypted with the key, otherwise the value of juniTacacsPlusClientKey will be used for the purpose.')
juniTacacsPlusClientHostStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 4874, 2, 2, 60, 1, 2, 1, 1, 7), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: juniTacacsPlusClientHostStatus.setStatus('current')
if mibBuilder.loadTexts: juniTacacsPlusClientHostStatus.setDescription("Status object, only `createAndGo' and 'destroy' are supported.")
juniTacacsPlusClientHostOrder = MibTableColumn((1, 3, 6, 1, 4, 1, 4874, 2, 2, 60, 1, 2, 1, 1, 8), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: juniTacacsPlusClientHostOrder.setStatus('current')
if mibBuilder.loadTexts: juniTacacsPlusClientHostOrder.setDescription('The search order of this TACACS+ host within all configured TACACS+ hosts. This MIB object indicates the order in which a TACACS+ request will be sent to the TACACS+ hosts until a response is received. The primary host is always the first host to be contacted. The remaining hosts will be contacted in the order that they were created. Should the primary host be deleted, the next host in the search order will become the primary host.')
juniTacacsPlusClientHostStatsTable = MibTable((1, 3, 6, 1, 4, 1, 4874, 2, 2, 60, 1, 3, 1), )
if mibBuilder.loadTexts: juniTacacsPlusClientHostStatsTable.setStatus('current')
if mibBuilder.loadTexts: juniTacacsPlusClientHostStatsTable.setDescription('This table contains per host statistics.')
juniTacacsPlusClientHostStatsEntry = MibTableRow((1, 3, 6, 1, 4, 1, 4874, 2, 2, 60, 1, 3, 1, 1), )
juniTacacsPlusClientHostConfigEntry.registerAugmentions(("Juniper-TACACS-Plus-Client-MIB", "juniTacacsPlusClientHostStatsEntry"))
juniTacacsPlusClientHostStatsEntry.setIndexNames(*juniTacacsPlusClientHostConfigEntry.getIndexNames())
if mibBuilder.loadTexts: juniTacacsPlusClientHostStatsEntry.setStatus('current')
if mibBuilder.loadTexts: juniTacacsPlusClientHostStatsEntry.setDescription('A TACACS+ host statistics table entry.')
juniTacacsPlusClientHostAuthRequests = MibTableColumn((1, 3, 6, 1, 4, 1, 4874, 2, 2, 60, 1, 3, 1, 1, 1), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: juniTacacsPlusClientHostAuthRequests.setStatus('current')
if mibBuilder.loadTexts: juniTacacsPlusClientHostAuthRequests.setDescription('Number of authentication requests sent to the host.')
juniTacacsPlusClientHostAuthReplies = MibTableColumn((1, 3, 6, 1, 4, 1, 4874, 2, 2, 60, 1, 3, 1, 1, 2), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: juniTacacsPlusClientHostAuthReplies.setStatus('current')
if mibBuilder.loadTexts: juniTacacsPlusClientHostAuthReplies.setDescription('Number of authentication replies received from the host.')
juniTacacsPlusClientHostAuthPending = MibTableColumn((1, 3, 6, 1, 4, 1, 4874, 2, 2, 60, 1, 3, 1, 1, 3), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: juniTacacsPlusClientHostAuthPending.setStatus('current')
if mibBuilder.loadTexts: juniTacacsPlusClientHostAuthPending.setDescription('Number of expected but not received authentication replies from the host.')
juniTacacsPlusClientHostAuthTimeouts = MibTableColumn((1, 3, 6, 1, 4, 1, 4874, 2, 2, 60, 1, 3, 1, 1, 4), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: juniTacacsPlusClientHostAuthTimeouts.setStatus('current')
if mibBuilder.loadTexts: juniTacacsPlusClientHostAuthTimeouts.setDescription('Number of authentication timeouts for the host.')
juniTacacsPlusClientHostAuthorRequests = MibTableColumn((1, 3, 6, 1, 4, 1, 4874, 2, 2, 60, 1, 3, 1, 1, 5), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: juniTacacsPlusClientHostAuthorRequests.setStatus('current')
if mibBuilder.loadTexts: juniTacacsPlusClientHostAuthorRequests.setDescription('Number of authorization requests sent to the host.')
juniTacacsPlusClientHostAuthorReplies = MibTableColumn((1, 3, 6, 1, 4, 1, 4874, 2, 2, 60, 1, 3, 1, 1, 6), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: juniTacacsPlusClientHostAuthorReplies.setStatus('current')
if mibBuilder.loadTexts: juniTacacsPlusClientHostAuthorReplies.setDescription('Number of authorization replies received from the host.')
juniTacacsPlusClientHostAuthorPending = MibTableColumn((1, 3, 6, 1, 4, 1, 4874, 2, 2, 60, 1, 3, 1, 1, 7), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: juniTacacsPlusClientHostAuthorPending.setStatus('current')
if mibBuilder.loadTexts: juniTacacsPlusClientHostAuthorPending.setDescription('Number of expected but not received authorization replies from the host.')
juniTacacsPlusClientHostAuthorTimeouts = MibTableColumn((1, 3, 6, 1, 4, 1, 4874, 2, 2, 60, 1, 3, 1, 1, 8), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: juniTacacsPlusClientHostAuthorTimeouts.setStatus('current')
if mibBuilder.loadTexts: juniTacacsPlusClientHostAuthorTimeouts.setDescription('Number of authorization timeouts for the host.')
juniTacacsPlusClientHostAcctRequests = MibTableColumn((1, 3, 6, 1, 4, 1, 4874, 2, 2, 60, 1, 3, 1, 1, 9), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: juniTacacsPlusClientHostAcctRequests.setStatus('current')
if mibBuilder.loadTexts: juniTacacsPlusClientHostAcctRequests.setDescription('Number of accounting requests sent to the host.')
juniTacacsPlusClientHostAcctReplies = MibTableColumn((1, 3, 6, 1, 4, 1, 4874, 2, 2, 60, 1, 3, 1, 1, 10), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: juniTacacsPlusClientHostAcctReplies.setStatus('current')
if mibBuilder.loadTexts: juniTacacsPlusClientHostAcctReplies.setDescription('Number of accounting replies received from the host.')
juniTacacsPlusClientHostAcctPending = MibTableColumn((1, 3, 6, 1, 4, 1, 4874, 2, 2, 60, 1, 3, 1, 1, 11), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: juniTacacsPlusClientHostAcctPending.setStatus('current')
if mibBuilder.loadTexts: juniTacacsPlusClientHostAcctPending.setDescription('Number of expected but not received accounting replies from the host.')
juniTacacsPlusClientHostAcctTimeouts = MibTableColumn((1, 3, 6, 1, 4, 1, 4874, 2, 2, 60, 1, 3, 1, 1, 12), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: juniTacacsPlusClientHostAcctTimeouts.setStatus('current')
if mibBuilder.loadTexts: juniTacacsPlusClientHostAcctTimeouts.setDescription('Number of accounting timeouts for the host.')
juniTacacsPlusClientHostDiscontinuityTime = MibTableColumn((1, 3, 6, 1, 4, 1, 4874, 2, 2, 60, 1, 3, 1, 1, 13), TimeStamp()).setMaxAccess("readonly")
if mibBuilder.loadTexts: juniTacacsPlusClientHostDiscontinuityTime.setStatus('current')
if mibBuilder.loadTexts: juniTacacsPlusClientHostDiscontinuityTime.setDescription('The value of sysUpTime when corresponding juniTacacsPlusHostConfigEntry was created, this object containg zero if host entry was created during system initializatin.')
juniTacacsPlusClientConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 4874, 2, 2, 60, 2))
juniTacacsPlusClientCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 4874, 2, 2, 60, 2, 1))
juniTacacsPlusClientGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 4874, 2, 2, 60, 2, 2))
juniTacacsPlusCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 4874, 2, 2, 60, 2, 1, 1)).setObjects(("Juniper-TACACS-Plus-Client-MIB", "juniTacacsPlusClientCommonGroup"), ("Juniper-TACACS-Plus-Client-MIB", "juniTacacsPlusClientHostConfigGroup"), ("Juniper-TACACS-Plus-Client-MIB", "juniTacacsPlusClientHostStatsGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    juniTacacsPlusCompliance = juniTacacsPlusCompliance.setStatus('obsolete')
if mibBuilder.loadTexts: juniTacacsPlusCompliance.setDescription('Obsolete compliance statement for entities which implement the Juniper TACACS+ Client MIB.')
juniTacacsPlusCompliance2 = ModuleCompliance((1, 3, 6, 1, 4, 1, 4874, 2, 2, 60, 2, 1, 2)).setObjects(("Juniper-TACACS-Plus-Client-MIB", "juniTacacsPlusClientCommonGroup"), ("Juniper-TACACS-Plus-Client-MIB", "juniTacacsPlusClientHostConfigGroup2"), ("Juniper-TACACS-Plus-Client-MIB", "juniTacacsPlusClientHostStatsGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    juniTacacsPlusCompliance2 = juniTacacsPlusCompliance2.setStatus('current')
if mibBuilder.loadTexts: juniTacacsPlusCompliance2.setDescription('The compliance statement for entities which implement the Juniper TACACS+ Client MIB.')
juniTacacsPlusClientCommonGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 4874, 2, 2, 60, 2, 2, 1)).setObjects(("Juniper-TACACS-Plus-Client-MIB", "juniTacacsPlusClientDirectedRequest"), ("Juniper-TACACS-Plus-Client-MIB", "juniTacacsPlusClientTimeout"), ("Juniper-TACACS-Plus-Client-MIB", "juniTacacsPlusClientKey"), ("Juniper-TACACS-Plus-Client-MIB", "juniTacacsPlusClientSourceIp"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    juniTacacsPlusClientCommonGroup = juniTacacsPlusClientCommonGroup.setStatus('current')
if mibBuilder.loadTexts: juniTacacsPlusClientCommonGroup.setDescription('This group defines common configuration parameters for all hosts.')
juniTacacsPlusClientHostConfigGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 4874, 2, 2, 60, 2, 2, 2)).setObjects(("Juniper-TACACS-Plus-Client-MIB", "juniTacacsPlusClientHostPort"), ("Juniper-TACACS-Plus-Client-MIB", "juniTacacsPlusClientHostPrimary"), ("Juniper-TACACS-Plus-Client-MIB", "juniTacacsPlusClientHostSingleConnection"), ("Juniper-TACACS-Plus-Client-MIB", "juniTacacsPlusClientHostTimeout"), ("Juniper-TACACS-Plus-Client-MIB", "juniTacacsPlusClientHostKey"), ("Juniper-TACACS-Plus-Client-MIB", "juniTacacsPlusClientHostStatus"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    juniTacacsPlusClientHostConfigGroup = juniTacacsPlusClientHostConfigGroup.setStatus('obsolete')
if mibBuilder.loadTexts: juniTacacsPlusClientHostConfigGroup.setDescription('Obsolete group for defining per host configuration parameters.')
juniTacacsPlusClientHostStatsGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 4874, 2, 2, 60, 2, 2, 3)).setObjects(("Juniper-TACACS-Plus-Client-MIB", "juniTacacsPlusClientHostAuthRequests"), ("Juniper-TACACS-Plus-Client-MIB", "juniTacacsPlusClientHostAuthReplies"), ("Juniper-TACACS-Plus-Client-MIB", "juniTacacsPlusClientHostAuthPending"), ("Juniper-TACACS-Plus-Client-MIB", "juniTacacsPlusClientHostAuthTimeouts"), ("Juniper-TACACS-Plus-Client-MIB", "juniTacacsPlusClientHostAuthorRequests"), ("Juniper-TACACS-Plus-Client-MIB", "juniTacacsPlusClientHostAuthorReplies"), ("Juniper-TACACS-Plus-Client-MIB", "juniTacacsPlusClientHostAuthorPending"), ("Juniper-TACACS-Plus-Client-MIB", "juniTacacsPlusClientHostAuthorTimeouts"), ("Juniper-TACACS-Plus-Client-MIB", "juniTacacsPlusClientHostAcctRequests"), ("Juniper-TACACS-Plus-Client-MIB", "juniTacacsPlusClientHostAcctReplies"), ("Juniper-TACACS-Plus-Client-MIB", "juniTacacsPlusClientHostAcctPending"), ("Juniper-TACACS-Plus-Client-MIB", "juniTacacsPlusClientHostAcctTimeouts"), ("Juniper-TACACS-Plus-Client-MIB", "juniTacacsPlusClientHostDiscontinuityTime"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    juniTacacsPlusClientHostStatsGroup = juniTacacsPlusClientHostStatsGroup.setStatus('current')
if mibBuilder.loadTexts: juniTacacsPlusClientHostStatsGroup.setDescription('This group defines statistics collected on per host basis.')
juniTacacsPlusClientHostConfigGroup2 = ObjectGroup((1, 3, 6, 1, 4, 1, 4874, 2, 2, 60, 2, 2, 4)).setObjects(("Juniper-TACACS-Plus-Client-MIB", "juniTacacsPlusClientHostPort"), ("Juniper-TACACS-Plus-Client-MIB", "juniTacacsPlusClientHostPrimary"), ("Juniper-TACACS-Plus-Client-MIB", "juniTacacsPlusClientHostSingleConnection"), ("Juniper-TACACS-Plus-Client-MIB", "juniTacacsPlusClientHostTimeout"), ("Juniper-TACACS-Plus-Client-MIB", "juniTacacsPlusClientHostKey"), ("Juniper-TACACS-Plus-Client-MIB", "juniTacacsPlusClientHostStatus"), ("Juniper-TACACS-Plus-Client-MIB", "juniTacacsPlusClientHostOrder"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    juniTacacsPlusClientHostConfigGroup2 = juniTacacsPlusClientHostConfigGroup2.setStatus('current')
if mibBuilder.loadTexts: juniTacacsPlusClientHostConfigGroup2.setDescription('This group defines per host configuration parameters.')
mibBuilder.exportSymbols("Juniper-TACACS-Plus-Client-MIB", juniTacacsPlusClientHostAuthRequests=juniTacacsPlusClientHostAuthRequests, juniTacacsPlusClientHostStatsTable=juniTacacsPlusClientHostStatsTable, juniTacacsPlusClientHostAuthorReplies=juniTacacsPlusClientHostAuthorReplies, juniTacacsPlusClientHostAuthorTimeouts=juniTacacsPlusClientHostAuthorTimeouts, juniTacacsPlusClientHostDiscontinuityTime=juniTacacsPlusClientHostDiscontinuityTime, juniTacacsPlusClientTimeout=juniTacacsPlusClientTimeout, juniTacacsPlusClientHostAddr=juniTacacsPlusClientHostAddr, juniTacacsPlusClientMIB=juniTacacsPlusClientMIB, juniTacacsPlusClientHostPrimary=juniTacacsPlusClientHostPrimary, JuniKeyString=JuniKeyString, juniTacacsPlusClientCompliances=juniTacacsPlusClientCompliances, juniTacacsPlusClientHostAuthPending=juniTacacsPlusClientHostAuthPending, juniTacacsPlusClientHostAcctPending=juniTacacsPlusClientHostAcctPending, juniTacacsPlusClientHostConfig=juniTacacsPlusClientHostConfig, juniTacacsPlusClientSourceIp=juniTacacsPlusClientSourceIp, juniTacacsPlusClientHostAuthTimeouts=juniTacacsPlusClientHostAuthTimeouts, juniTacacsPlusClientHostOrder=juniTacacsPlusClientHostOrder, juniTacacsPlusClientObjects=juniTacacsPlusClientObjects, juniTacacsPlusClientHostConfigEntry=juniTacacsPlusClientHostConfigEntry, juniTacacsPlusClientHostKey=juniTacacsPlusClientHostKey, juniTacacsPlusClientHostAcctRequests=juniTacacsPlusClientHostAcctRequests, juniTacacsPlusClientConformance=juniTacacsPlusClientConformance, juniTacacsPlusClientHostConfigGroup2=juniTacacsPlusClientHostConfigGroup2, juniTacacsPlusClientHostStatsEntry=juniTacacsPlusClientHostStatsEntry, juniTacacsPlusClientHostAuthReplies=juniTacacsPlusClientHostAuthReplies, juniTacacsPlusClientDirectedRequest=juniTacacsPlusClientDirectedRequest, juniTacacsPlusClientHostStats=juniTacacsPlusClientHostStats, juniTacacsPlusCompliance2=juniTacacsPlusCompliance2, juniTacacsPlusClientCommonGroup=juniTacacsPlusClientCommonGroup, juniTacacsPlusClientGroups=juniTacacsPlusClientGroups, juniTacacsPlusClientHostAcctReplies=juniTacacsPlusClientHostAcctReplies, juniTacacsPlusClientHostStatsGroup=juniTacacsPlusClientHostStatsGroup, juniTacacsPlusClientHostAuthorPending=juniTacacsPlusClientHostAuthorPending, juniTacacsPlusClientHostAcctTimeouts=juniTacacsPlusClientHostAcctTimeouts, juniTacacsPlusClientHostTimeout=juniTacacsPlusClientHostTimeout, juniTacacsPlusClientHostConfigTable=juniTacacsPlusClientHostConfigTable, juniTacacsPlusClientHostStatus=juniTacacsPlusClientHostStatus, juniTacacsPlusClientHostSingleConnection=juniTacacsPlusClientHostSingleConnection, juniTacacsPlusClientCommonConfig=juniTacacsPlusClientCommonConfig, PYSNMP_MODULE_ID=juniTacacsPlusClientMIB, juniTacacsPlusClientHostConfigGroup=juniTacacsPlusClientHostConfigGroup, juniTacacsPlusCompliance=juniTacacsPlusCompliance, juniTacacsPlusClientHostAuthorRequests=juniTacacsPlusClientHostAuthorRequests, juniTacacsPlusClientHostPort=juniTacacsPlusClientHostPort, juniTacacsPlusClientKey=juniTacacsPlusClientKey)
