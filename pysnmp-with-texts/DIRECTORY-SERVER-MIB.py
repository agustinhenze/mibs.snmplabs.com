#
# PySNMP MIB module DIRECTORY-SERVER-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/DIRECTORY-SERVER-MIB
# Produced by pysmi-0.3.4 at Wed May  1 12:47:11 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
OctetString, Integer, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "OctetString", "Integer", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, ConstraintsIntersection, ConstraintsUnion, ValueSizeConstraint, SingleValueConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "ConstraintsIntersection", "ConstraintsUnion", "ValueSizeConstraint", "SingleValueConstraint")
applIndex, DistinguishedName, URLString = mibBuilder.importSymbols("NETWORK-SERVICES-MIB", "applIndex", "DistinguishedName", "URLString")
ZeroBasedCounter32, = mibBuilder.importSymbols("RMON2-MIB", "ZeroBasedCounter32")
ModuleCompliance, ObjectGroup, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "ObjectGroup", "NotificationGroup")
NotificationType, iso, MibIdentifier, mib_2, MibScalar, MibTable, MibTableRow, MibTableColumn, Integer32, Unsigned32, Gauge32, ModuleIdentity, IpAddress, ObjectIdentity, Bits, Counter32, Counter64, TimeTicks = mibBuilder.importSymbols("SNMPv2-SMI", "NotificationType", "iso", "MibIdentifier", "mib-2", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Integer32", "Unsigned32", "Gauge32", "ModuleIdentity", "IpAddress", "ObjectIdentity", "Bits", "Counter32", "Counter64", "TimeTicks")
TextualConvention, TimeStamp, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "TimeStamp", "DisplayString")
dsMIB = ModuleIdentity((1, 3, 6, 1, 2, 1, 66))
dsMIB.setRevisions(('1999-06-07 00:00', '1993-11-25 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: dsMIB.setRevisionsDescriptions(('This revision of this MIB is published in RFC 2605. This revision obsoletes RFC 1567. It is incompatible with the original MIB and so it has been renamed from dsaMIB to dsMIB.', 'The original version of this MIB was published in RFC 1567.',))
if mibBuilder.loadTexts: dsMIB.setLastUpdated('9906070000Z')
if mibBuilder.loadTexts: dsMIB.setOrganization('IETF Mail and Directory Management Working Group')
if mibBuilder.loadTexts: dsMIB.setContactInfo(' Glenn Mansfield Postal: Cyber Solutions Inc. 6-6-3, Minami Yoshinari Aoba-ku, Sendai, Japan 989-3204. Tel: +81-22-303-4012 Fax: +81-22-303-4015 E-mail: glenn@cysols.com Working Group E-mail: ietf-madman@innosoft.com To subscribe: ietf-madman-request@innosoft.com')
if mibBuilder.loadTexts: dsMIB.setDescription(' The MIB module for monitoring Directory Services.')
dsTable = MibTable((1, 3, 6, 1, 2, 1, 66, 1), )
if mibBuilder.loadTexts: dsTable.setStatus('current')
if mibBuilder.loadTexts: dsTable.setDescription(' The table holding information related to the Directory Servers.')
dsTableEntry = MibTableRow((1, 3, 6, 1, 2, 1, 66, 1, 1), ).setIndexNames((0, "NETWORK-SERVICES-MIB", "applIndex"))
if mibBuilder.loadTexts: dsTableEntry.setStatus('current')
if mibBuilder.loadTexts: dsTableEntry.setDescription(' Entry containing summary description for a Directory Server.')
dsServerType = MibTableColumn((1, 3, 6, 1, 2, 1, 66, 1, 1, 1), Bits().clone(namedValues=NamedValues(("frontEndDirectoryServer", 0), ("backEndDirectoryServer", 1)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: dsServerType.setStatus('current')
if mibBuilder.loadTexts: dsServerType.setDescription('This object indicates whether the server is a frontend or, a backend or, both. If the server is a frontend, then the frontEndDirectoryServer bit will be set. Similarly for the backend.')
dsServerDescription = MibTableColumn((1, 3, 6, 1, 2, 1, 66, 1, 1, 2), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dsServerDescription.setStatus('current')
if mibBuilder.loadTexts: dsServerDescription.setDescription('A text description of the application. This information is intended to identify and briefly describe the application in a status display.')
dsMasterEntries = MibTableColumn((1, 3, 6, 1, 2, 1, 66, 1, 1, 3), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dsMasterEntries.setStatus('current')
if mibBuilder.loadTexts: dsMasterEntries.setDescription(' Number of entries mastered in the Directory Server.')
dsCopyEntries = MibTableColumn((1, 3, 6, 1, 2, 1, 66, 1, 1, 4), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dsCopyEntries.setStatus('current')
if mibBuilder.loadTexts: dsCopyEntries.setDescription(' Number of entries for which systematic (slave) copies are maintained in the Directory Server.')
dsCacheEntries = MibTableColumn((1, 3, 6, 1, 2, 1, 66, 1, 1, 5), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dsCacheEntries.setStatus('current')
if mibBuilder.loadTexts: dsCacheEntries.setDescription(' Number of entries cached (non-systematic copies) in the Directory Server. This will include the entries that are cached partially. The negative cache is not counted.')
dsCacheHits = MibTableColumn((1, 3, 6, 1, 2, 1, 66, 1, 1, 6), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dsCacheHits.setStatus('current')
if mibBuilder.loadTexts: dsCacheHits.setDescription(' Number of operations that were serviced from the locally held cache.')
dsSlaveHits = MibTableColumn((1, 3, 6, 1, 2, 1, 66, 1, 1, 7), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dsSlaveHits.setStatus('current')
if mibBuilder.loadTexts: dsSlaveHits.setDescription(' Number of operations that were serviced from the locally held object replications ( copy- entries).')
dsApplIfOpsTable = MibTable((1, 3, 6, 1, 2, 1, 66, 2), )
if mibBuilder.loadTexts: dsApplIfOpsTable.setStatus('current')
if mibBuilder.loadTexts: dsApplIfOpsTable.setDescription(' The table holding information related to the Directory Server operations.')
dsApplIfOpsEntry = MibTableRow((1, 3, 6, 1, 2, 1, 66, 2, 1), ).setIndexNames((0, "NETWORK-SERVICES-MIB", "applIndex"), (0, "DIRECTORY-SERVER-MIB", "dsApplIfProtocolIndex"))
if mibBuilder.loadTexts: dsApplIfOpsEntry.setStatus('current')
if mibBuilder.loadTexts: dsApplIfOpsEntry.setDescription(' Entry containing operations related statistics for a Directory Server.')
dsApplIfProtocolIndex = MibTableColumn((1, 3, 6, 1, 2, 1, 66, 2, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 2147483647))).setMaxAccess("readonly")
if mibBuilder.loadTexts: dsApplIfProtocolIndex.setStatus('current')
if mibBuilder.loadTexts: dsApplIfProtocolIndex.setDescription('An index to uniquely identify an entry corresponding to a application-layer protocol interface. This index is used for lexicographic ordering of the table.')
dsApplIfProtocol = MibTableColumn((1, 3, 6, 1, 2, 1, 66, 2, 1, 2), ObjectIdentifier()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dsApplIfProtocol.setStatus('current')
if mibBuilder.loadTexts: dsApplIfProtocol.setDescription("An identification of the protocol being used by the application on this interface. For an OSI Application, this will be the Application Context. For Internet applications, the IANA maintains a registry[22] of the OIDs which correspond to well-known applications. If the application protocol is not listed in the registry, an OID value of the form {applTCPProtoID port} or {applUDProtoID port} are used for TCP-based and UDP-based protocols, respectively. In either case 'port' corresponds to the primary port number being used by the protocol. The OIDs applTCPProtoID and applUDPProtoID are defined in NETWORK-SERVICES-MIB")
dsApplIfUnauthBinds = MibTableColumn((1, 3, 6, 1, 2, 1, 66, 2, 1, 3), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dsApplIfUnauthBinds.setStatus('current')
if mibBuilder.loadTexts: dsApplIfUnauthBinds.setDescription(' Number of unauthenticated/anonymous bind requests received.')
dsApplIfSimpleAuthBinds = MibTableColumn((1, 3, 6, 1, 2, 1, 66, 2, 1, 4), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dsApplIfSimpleAuthBinds.setStatus('current')
if mibBuilder.loadTexts: dsApplIfSimpleAuthBinds.setDescription(' Number of bind requests that were authenticated using simple authentication procedures like password checks. This includes the password authentication using SASL mechanisms like CRAM-MD5.')
dsApplIfStrongAuthBinds = MibTableColumn((1, 3, 6, 1, 2, 1, 66, 2, 1, 5), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dsApplIfStrongAuthBinds.setStatus('current')
if mibBuilder.loadTexts: dsApplIfStrongAuthBinds.setDescription(' Number of bind requests that were authenticated using TLS and X.500 strong authentication procedures. This includes the binds that were authenticated using external authentication procedures.')
dsApplIfBindSecurityErrors = MibTableColumn((1, 3, 6, 1, 2, 1, 66, 2, 1, 6), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dsApplIfBindSecurityErrors.setStatus('current')
if mibBuilder.loadTexts: dsApplIfBindSecurityErrors.setDescription(' Number of bind requests that have been rejected due to inappropriate authentication or invalid credentials.')
dsApplIfInOps = MibTableColumn((1, 3, 6, 1, 2, 1, 66, 2, 1, 7), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dsApplIfInOps.setStatus('current')
if mibBuilder.loadTexts: dsApplIfInOps.setDescription(' Number of requests received from DUAs or other Directory Servers.')
dsApplIfReadOps = MibTableColumn((1, 3, 6, 1, 2, 1, 66, 2, 1, 8), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dsApplIfReadOps.setStatus('current')
if mibBuilder.loadTexts: dsApplIfReadOps.setDescription(' Number of read requests received.')
dsApplIfCompareOps = MibTableColumn((1, 3, 6, 1, 2, 1, 66, 2, 1, 9), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dsApplIfCompareOps.setStatus('current')
if mibBuilder.loadTexts: dsApplIfCompareOps.setDescription(' Number of compare requests received.')
dsApplIfAddEntryOps = MibTableColumn((1, 3, 6, 1, 2, 1, 66, 2, 1, 10), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dsApplIfAddEntryOps.setStatus('current')
if mibBuilder.loadTexts: dsApplIfAddEntryOps.setDescription(' Number of addEntry requests received.')
dsApplIfRemoveEntryOps = MibTableColumn((1, 3, 6, 1, 2, 1, 66, 2, 1, 11), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dsApplIfRemoveEntryOps.setStatus('current')
if mibBuilder.loadTexts: dsApplIfRemoveEntryOps.setDescription(' Number of removeEntry requests received.')
dsApplIfModifyEntryOps = MibTableColumn((1, 3, 6, 1, 2, 1, 66, 2, 1, 12), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dsApplIfModifyEntryOps.setStatus('current')
if mibBuilder.loadTexts: dsApplIfModifyEntryOps.setDescription(' Number of modifyEntry requests received.')
dsApplIfModifyRDNOps = MibTableColumn((1, 3, 6, 1, 2, 1, 66, 2, 1, 13), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dsApplIfModifyRDNOps.setStatus('current')
if mibBuilder.loadTexts: dsApplIfModifyRDNOps.setDescription(' Number of modifyRDN requests received.')
dsApplIfListOps = MibTableColumn((1, 3, 6, 1, 2, 1, 66, 2, 1, 14), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dsApplIfListOps.setStatus('current')
if mibBuilder.loadTexts: dsApplIfListOps.setDescription(' Number of list requests received.')
dsApplIfSearchOps = MibTableColumn((1, 3, 6, 1, 2, 1, 66, 2, 1, 15), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dsApplIfSearchOps.setStatus('current')
if mibBuilder.loadTexts: dsApplIfSearchOps.setDescription(' Number of search requests- baseObject searches, oneLevel searches and whole subtree searches, received.')
dsApplIfOneLevelSearchOps = MibTableColumn((1, 3, 6, 1, 2, 1, 66, 2, 1, 16), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dsApplIfOneLevelSearchOps.setStatus('current')
if mibBuilder.loadTexts: dsApplIfOneLevelSearchOps.setDescription(' Number of oneLevel search requests received.')
dsApplIfWholeSubtreeSearchOps = MibTableColumn((1, 3, 6, 1, 2, 1, 66, 2, 1, 17), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dsApplIfWholeSubtreeSearchOps.setStatus('current')
if mibBuilder.loadTexts: dsApplIfWholeSubtreeSearchOps.setDescription(' Number of whole subtree search requests received.')
dsApplIfReferrals = MibTableColumn((1, 3, 6, 1, 2, 1, 66, 2, 1, 18), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dsApplIfReferrals.setStatus('current')
if mibBuilder.loadTexts: dsApplIfReferrals.setDescription(' Number of referrals returned in response to requests for operations.')
dsApplIfChainings = MibTableColumn((1, 3, 6, 1, 2, 1, 66, 2, 1, 19), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dsApplIfChainings.setStatus('current')
if mibBuilder.loadTexts: dsApplIfChainings.setDescription(' Number of operations forwarded by this Directory Server to other Directory Servers.')
dsApplIfSecurityErrors = MibTableColumn((1, 3, 6, 1, 2, 1, 66, 2, 1, 20), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dsApplIfSecurityErrors.setStatus('current')
if mibBuilder.loadTexts: dsApplIfSecurityErrors.setDescription(' Number of requests received which did not meet the security requirements. ')
dsApplIfErrors = MibTableColumn((1, 3, 6, 1, 2, 1, 66, 2, 1, 21), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dsApplIfErrors.setStatus('current')
if mibBuilder.loadTexts: dsApplIfErrors.setDescription(' Number of requests that could not be serviced due to errors other than security errors, and referrals. A partially serviced operation will not be counted as an error. The errors include naming-related, update-related, attribute-related and service-related errors.')
dsApplIfReplicationUpdatesIn = MibTableColumn((1, 3, 6, 1, 2, 1, 66, 2, 1, 22), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dsApplIfReplicationUpdatesIn.setStatus('current')
if mibBuilder.loadTexts: dsApplIfReplicationUpdatesIn.setDescription(' Number of replication updates fetched or received from supplier Directory Servers.')
dsApplIfReplicationUpdatesOut = MibTableColumn((1, 3, 6, 1, 2, 1, 66, 2, 1, 23), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dsApplIfReplicationUpdatesOut.setStatus('current')
if mibBuilder.loadTexts: dsApplIfReplicationUpdatesOut.setDescription(' Number of replication updates sent to or taken by consumer Directory Servers.')
dsApplIfInBytes = MibTableColumn((1, 3, 6, 1, 2, 1, 66, 2, 1, 24), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dsApplIfInBytes.setStatus('current')
if mibBuilder.loadTexts: dsApplIfInBytes.setDescription(' Incoming traffic, in bytes, on the interface. This will include requests from DUAs as well as responses from other Directory Servers.')
dsApplIfOutBytes = MibTableColumn((1, 3, 6, 1, 2, 1, 66, 2, 1, 25), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dsApplIfOutBytes.setStatus('current')
if mibBuilder.loadTexts: dsApplIfOutBytes.setDescription(' Outgoing traffic in bytes on the interface. This will include responses to DUAs and Directory Servers as well as requests to other Directory Servers.')
dsIntTable = MibTable((1, 3, 6, 1, 2, 1, 66, 3), )
if mibBuilder.loadTexts: dsIntTable.setStatus('current')
if mibBuilder.loadTexts: dsIntTable.setDescription(' Each row of this table contains some details related to the history of the interaction of the monitored Directory Server with its peer Directory Servers.')
dsIntEntry = MibTableRow((1, 3, 6, 1, 2, 1, 66, 3, 1), ).setIndexNames((0, "NETWORK-SERVICES-MIB", "applIndex"), (0, "DIRECTORY-SERVER-MIB", "dsIntEntIndex"), (0, "DIRECTORY-SERVER-MIB", "dsApplIfProtocolIndex"))
if mibBuilder.loadTexts: dsIntEntry.setStatus('current')
if mibBuilder.loadTexts: dsIntEntry.setDescription(' Entry containing interaction details of a Directory Server with a peer Directory Server.')
dsIntEntIndex = MibTableColumn((1, 3, 6, 1, 2, 1, 66, 3, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 2147483647)))
if mibBuilder.loadTexts: dsIntEntIndex.setStatus('current')
if mibBuilder.loadTexts: dsIntEntIndex.setDescription(' Together with applIndex and dsApplIfProtocolIndex, this object forms the unique key to identify the conceptual row which contains useful info on the (attempted) interaction between the Directory Server (referred to by applIndex) and a peer Directory Server using a particular protocol.')
dsIntEntDirectoryName = MibTableColumn((1, 3, 6, 1, 2, 1, 66, 3, 1, 2), DistinguishedName()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dsIntEntDirectoryName.setStatus('current')
if mibBuilder.loadTexts: dsIntEntDirectoryName.setDescription(' Distinguished Name of the peer Directory Server to which this entry pertains.')
dsIntEntTimeOfCreation = MibTableColumn((1, 3, 6, 1, 2, 1, 66, 3, 1, 3), TimeStamp()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dsIntEntTimeOfCreation.setStatus('current')
if mibBuilder.loadTexts: dsIntEntTimeOfCreation.setDescription(' The value of sysUpTime when this row was created. If the entry was created before the network management subsystem was initialized, this object will contain a value of zero.')
dsIntEntTimeOfLastAttempt = MibTableColumn((1, 3, 6, 1, 2, 1, 66, 3, 1, 4), TimeStamp()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dsIntEntTimeOfLastAttempt.setStatus('current')
if mibBuilder.loadTexts: dsIntEntTimeOfLastAttempt.setDescription(' The value of sysUpTime when the last attempt was made to contact the peer Directory Server. If the last attempt was made before the network management subsystem was initialized, this object will contain a value of zero.')
dsIntEntTimeOfLastSuccess = MibTableColumn((1, 3, 6, 1, 2, 1, 66, 3, 1, 5), TimeStamp()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dsIntEntTimeOfLastSuccess.setStatus('current')
if mibBuilder.loadTexts: dsIntEntTimeOfLastSuccess.setDescription(' The value of sysUpTime when the last attempt made to contact the peer Directory Server was successful. If there have been no successful attempts this entry will have a value of zero. If the last successful attempt was made before the network management subsystem was initialized, this object will contain a value of zero.')
dsIntEntFailuresSinceLastSuccess = MibTableColumn((1, 3, 6, 1, 2, 1, 66, 3, 1, 6), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dsIntEntFailuresSinceLastSuccess.setStatus('current')
if mibBuilder.loadTexts: dsIntEntFailuresSinceLastSuccess.setDescription(' The number of failures since the last time an attempt to contact the peer Directory Server was successful. If there have been no successful attempts, this counter will contain the number of failures since this entry was created.')
dsIntEntFailures = MibTableColumn((1, 3, 6, 1, 2, 1, 66, 3, 1, 7), ZeroBasedCounter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dsIntEntFailures.setStatus('current')
if mibBuilder.loadTexts: dsIntEntFailures.setDescription(' Cumulative failures in contacting the peer Directory Server since the creation of this entry.')
dsIntEntSuccesses = MibTableColumn((1, 3, 6, 1, 2, 1, 66, 3, 1, 8), ZeroBasedCounter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dsIntEntSuccesses.setStatus('current')
if mibBuilder.loadTexts: dsIntEntSuccesses.setDescription(' Cumulative successes in contacting the peer Directory Server since the creation of this entry.')
dsIntEntURL = MibTableColumn((1, 3, 6, 1, 2, 1, 66, 3, 1, 9), URLString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dsIntEntURL.setStatus('current')
if mibBuilder.loadTexts: dsIntEntURL.setDescription(' URL of the peer Directory Server.')
dsConformance = MibIdentifier((1, 3, 6, 1, 2, 1, 66, 4))
dsGroups = MibIdentifier((1, 3, 6, 1, 2, 1, 66, 4, 1))
dsCompliances = MibIdentifier((1, 3, 6, 1, 2, 1, 66, 4, 2))
dsEntryCompliance = ModuleCompliance((1, 3, 6, 1, 2, 1, 66, 4, 2, 1)).setObjects(("DIRECTORY-SERVER-MIB", "dsEntryGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    dsEntryCompliance = dsEntryCompliance.setStatus('current')
if mibBuilder.loadTexts: dsEntryCompliance.setDescription('The compliance statement for SNMP entities which implement the DIRECTORY-SERVER-MIB for a summary overview of the Directory Servers .')
dsOpsCompliance = ModuleCompliance((1, 3, 6, 1, 2, 1, 66, 4, 2, 2)).setObjects(("DIRECTORY-SERVER-MIB", "dsEntryGroup"), ("DIRECTORY-SERVER-MIB", "dsOpsGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    dsOpsCompliance = dsOpsCompliance.setStatus('current')
if mibBuilder.loadTexts: dsOpsCompliance.setDescription('The compliance statement for SNMP entities which implement the DIRECTORY-SERVER-MIB for monitoring Directory Server operations, entry statistics and cache performance.')
dsIntCompliance = ModuleCompliance((1, 3, 6, 1, 2, 1, 66, 4, 2, 3)).setObjects(("DIRECTORY-SERVER-MIB", "dsEntryGroup"), ("DIRECTORY-SERVER-MIB", "dsIntGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    dsIntCompliance = dsIntCompliance.setStatus('current')
if mibBuilder.loadTexts: dsIntCompliance.setDescription(' The compliance statement for SNMP entities which implement the DIRECTORY-SERVER-MIB for monitoring Directory Server operations and the interaction of the Directory Server with peer Directory Servers.')
dsOpsIntCompliance = ModuleCompliance((1, 3, 6, 1, 2, 1, 66, 4, 2, 4)).setObjects(("DIRECTORY-SERVER-MIB", "dsEntryGroup"), ("DIRECTORY-SERVER-MIB", "dsOpsGroup"), ("DIRECTORY-SERVER-MIB", "dsIntGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    dsOpsIntCompliance = dsOpsIntCompliance.setStatus('current')
if mibBuilder.loadTexts: dsOpsIntCompliance.setDescription(' The compliance statement for SNMP entities which implement the DIRECTORY-SERVER-MIB for monitoring Directory Server operations and the interaction of the Directory Server with peer Directory Servers.')
dsEntryGroup = ObjectGroup((1, 3, 6, 1, 2, 1, 66, 4, 1, 1)).setObjects(("DIRECTORY-SERVER-MIB", "dsServerType"), ("DIRECTORY-SERVER-MIB", "dsServerDescription"), ("DIRECTORY-SERVER-MIB", "dsMasterEntries"), ("DIRECTORY-SERVER-MIB", "dsCopyEntries"), ("DIRECTORY-SERVER-MIB", "dsCacheEntries"), ("DIRECTORY-SERVER-MIB", "dsCacheHits"), ("DIRECTORY-SERVER-MIB", "dsSlaveHits"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    dsEntryGroup = dsEntryGroup.setStatus('current')
if mibBuilder.loadTexts: dsEntryGroup.setDescription(' A collection of objects for a summary overview of the Directory Servers.')
dsOpsGroup = ObjectGroup((1, 3, 6, 1, 2, 1, 66, 4, 1, 2)).setObjects(("DIRECTORY-SERVER-MIB", "dsApplIfProtocolIndex"), ("DIRECTORY-SERVER-MIB", "dsApplIfProtocol"), ("DIRECTORY-SERVER-MIB", "dsApplIfUnauthBinds"), ("DIRECTORY-SERVER-MIB", "dsApplIfSimpleAuthBinds"), ("DIRECTORY-SERVER-MIB", "dsApplIfStrongAuthBinds"), ("DIRECTORY-SERVER-MIB", "dsApplIfBindSecurityErrors"), ("DIRECTORY-SERVER-MIB", "dsApplIfInOps"), ("DIRECTORY-SERVER-MIB", "dsApplIfReadOps"), ("DIRECTORY-SERVER-MIB", "dsApplIfCompareOps"), ("DIRECTORY-SERVER-MIB", "dsApplIfAddEntryOps"), ("DIRECTORY-SERVER-MIB", "dsApplIfRemoveEntryOps"), ("DIRECTORY-SERVER-MIB", "dsApplIfModifyEntryOps"), ("DIRECTORY-SERVER-MIB", "dsApplIfModifyRDNOps"), ("DIRECTORY-SERVER-MIB", "dsApplIfListOps"), ("DIRECTORY-SERVER-MIB", "dsApplIfSearchOps"), ("DIRECTORY-SERVER-MIB", "dsApplIfOneLevelSearchOps"), ("DIRECTORY-SERVER-MIB", "dsApplIfWholeSubtreeSearchOps"), ("DIRECTORY-SERVER-MIB", "dsApplIfReferrals"), ("DIRECTORY-SERVER-MIB", "dsApplIfChainings"), ("DIRECTORY-SERVER-MIB", "dsApplIfSecurityErrors"), ("DIRECTORY-SERVER-MIB", "dsApplIfErrors"), ("DIRECTORY-SERVER-MIB", "dsApplIfReplicationUpdatesIn"), ("DIRECTORY-SERVER-MIB", "dsApplIfReplicationUpdatesOut"), ("DIRECTORY-SERVER-MIB", "dsApplIfInBytes"), ("DIRECTORY-SERVER-MIB", "dsApplIfOutBytes"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    dsOpsGroup = dsOpsGroup.setStatus('current')
if mibBuilder.loadTexts: dsOpsGroup.setDescription(' A collection of objects for monitoring the Directory Server operations.')
dsIntGroup = ObjectGroup((1, 3, 6, 1, 2, 1, 66, 4, 1, 3)).setObjects(("DIRECTORY-SERVER-MIB", "dsIntEntDirectoryName"), ("DIRECTORY-SERVER-MIB", "dsIntEntTimeOfCreation"), ("DIRECTORY-SERVER-MIB", "dsIntEntTimeOfLastAttempt"), ("DIRECTORY-SERVER-MIB", "dsIntEntTimeOfLastSuccess"), ("DIRECTORY-SERVER-MIB", "dsIntEntFailuresSinceLastSuccess"), ("DIRECTORY-SERVER-MIB", "dsIntEntFailures"), ("DIRECTORY-SERVER-MIB", "dsIntEntSuccesses"), ("DIRECTORY-SERVER-MIB", "dsIntEntURL"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    dsIntGroup = dsIntGroup.setStatus('current')
if mibBuilder.loadTexts: dsIntGroup.setDescription(" A collection of objects for monitoring the Directory Server's interaction with peer Directory Servers.")
mibBuilder.exportSymbols("DIRECTORY-SERVER-MIB", dsMIB=dsMIB, dsIntEntFailuresSinceLastSuccess=dsIntEntFailuresSinceLastSuccess, dsIntEntTimeOfCreation=dsIntEntTimeOfCreation, dsApplIfChainings=dsApplIfChainings, dsIntEntTimeOfLastAttempt=dsIntEntTimeOfLastAttempt, dsIntEntSuccesses=dsIntEntSuccesses, dsTable=dsTable, dsApplIfReadOps=dsApplIfReadOps, dsApplIfReferrals=dsApplIfReferrals, dsOpsIntCompliance=dsOpsIntCompliance, dsCopyEntries=dsCopyEntries, dsApplIfSecurityErrors=dsApplIfSecurityErrors, dsApplIfOpsTable=dsApplIfOpsTable, dsApplIfModifyEntryOps=dsApplIfModifyEntryOps, dsServerDescription=dsServerDescription, dsApplIfBindSecurityErrors=dsApplIfBindSecurityErrors, dsApplIfModifyRDNOps=dsApplIfModifyRDNOps, dsApplIfRemoveEntryOps=dsApplIfRemoveEntryOps, dsApplIfOneLevelSearchOps=dsApplIfOneLevelSearchOps, dsIntEntURL=dsIntEntURL, dsIntEntDirectoryName=dsIntEntDirectoryName, dsConformance=dsConformance, dsApplIfSimpleAuthBinds=dsApplIfSimpleAuthBinds, dsApplIfSearchOps=dsApplIfSearchOps, dsIntEntTimeOfLastSuccess=dsIntEntTimeOfLastSuccess, dsMasterEntries=dsMasterEntries, dsApplIfAddEntryOps=dsApplIfAddEntryOps, dsApplIfInOps=dsApplIfInOps, dsSlaveHits=dsSlaveHits, dsEntryCompliance=dsEntryCompliance, dsApplIfWholeSubtreeSearchOps=dsApplIfWholeSubtreeSearchOps, dsApplIfErrors=dsApplIfErrors, dsServerType=dsServerType, dsCacheHits=dsCacheHits, dsIntEntFailures=dsIntEntFailures, dsIntEntIndex=dsIntEntIndex, dsOpsCompliance=dsOpsCompliance, dsApplIfStrongAuthBinds=dsApplIfStrongAuthBinds, dsApplIfProtocol=dsApplIfProtocol, dsOpsGroup=dsOpsGroup, dsApplIfCompareOps=dsApplIfCompareOps, dsEntryGroup=dsEntryGroup, dsApplIfOutBytes=dsApplIfOutBytes, dsIntCompliance=dsIntCompliance, dsApplIfProtocolIndex=dsApplIfProtocolIndex, dsCacheEntries=dsCacheEntries, dsApplIfReplicationUpdatesIn=dsApplIfReplicationUpdatesIn, dsApplIfReplicationUpdatesOut=dsApplIfReplicationUpdatesOut, dsGroups=dsGroups, dsCompliances=dsCompliances, dsTableEntry=dsTableEntry, dsApplIfListOps=dsApplIfListOps, dsIntTable=dsIntTable, dsApplIfUnauthBinds=dsApplIfUnauthBinds, PYSNMP_MODULE_ID=dsMIB, dsIntEntry=dsIntEntry, dsApplIfOpsEntry=dsApplIfOpsEntry, dsIntGroup=dsIntGroup, dsApplIfInBytes=dsApplIfInBytes)