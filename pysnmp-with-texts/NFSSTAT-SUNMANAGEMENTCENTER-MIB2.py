#
# PySNMP MIB module NFSSTAT-SUNMANAGEMENTCENTER-MIB2 (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/NFSSTAT-SUNMANAGEMENTCENTER-MIB2
# Produced by pysmi-0.3.4 at Wed May  1 14:21:07 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
OctetString, Integer, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "OctetString", "Integer", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsUnion, ValueRangeConstraint, SingleValueConstraint, ConstraintsIntersection, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsIntersection", "ValueSizeConstraint")
NotificationGroup, ObjectGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ObjectGroup", "ModuleCompliance")
Gauge32, enterprises, NotificationType, MibScalar, MibTable, MibTableRow, MibTableColumn, ModuleIdentity, IpAddress, Counter32, Integer32, Unsigned32, Bits, ObjectIdentity, MibIdentifier, Counter64, iso, TimeTicks = mibBuilder.importSymbols("SNMPv2-SMI", "Gauge32", "enterprises", "NotificationType", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "ModuleIdentity", "IpAddress", "Counter32", "Integer32", "Unsigned32", "Bits", "ObjectIdentity", "MibIdentifier", "Counter64", "iso", "TimeTicks")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
nfsstat = ModuleIdentity((1, 3, 6, 1, 4, 1, 42, 2, 12, 2, 2, 28))
nfsstat.setRevisions(('1999-07-20 15:05',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: nfsstat.setRevisionsDescriptions(('Rev 1.0 20th July 1999 15:05, Initial version Of MIB.',))
if mibBuilder.loadTexts: nfsstat.setLastUpdated('9907201505Z')
if mibBuilder.loadTexts: nfsstat.setOrganization('Sun Microsystems Inc.')
if mibBuilder.loadTexts: nfsstat.setContactInfo(' Sun Microsystems Inc. Customer Support Postal: 901 San Antonio Road Palo Alto, CA-94303-4900 USA Tel: 650-960-1300 E-mail: service@sun.com')
if mibBuilder.loadTexts: nfsstat.setDescription('The NFS statistics mib allows to monitor information regarding client and server call related to both NFS and RPC.')
sun = MibIdentifier((1, 3, 6, 1, 4, 1, 42))
prod = MibIdentifier((1, 3, 6, 1, 4, 1, 42, 2))
sunsymon = MibIdentifier((1, 3, 6, 1, 4, 1, 42, 2, 12))
agent = MibIdentifier((1, 3, 6, 1, 4, 1, 42, 2, 12, 2))
modules = MibIdentifier((1, 3, 6, 1, 4, 1, 42, 2, 12, 2, 2))
nfsStats = MibIdentifier((1, 3, 6, 1, 4, 1, 42, 2, 12, 2, 2, 28, 1))
nfssServerRPCStatGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 42, 2, 12, 2, 2, 28, 1, 1)).setObjects(("NFSSTAT-SUNMANAGEMENTCENTER-MIB2", "nfssTotServRPCCalls"), ("NFSSTAT-SUNMANAGEMENTCENTER-MIB2", "nfssServBadRPCCalls"), ("NFSSTAT-SUNMANAGEMENTCENTER-MIB2", "nfssServPcntBadRPCCalls"), ("NFSSTAT-SUNMANAGEMENTCENTER-MIB2", "nfssServRPCCallRate"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    nfssServerRPCStatGroup = nfssServerRPCStatGroup.setStatus('current')
if mibBuilder.loadTexts: nfssServerRPCStatGroup.setDescription('RPC server calls related statistics.')
nfssServerNFSStatGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 42, 2, 12, 2, 2, 28, 1, 2)).setObjects(("NFSSTAT-SUNMANAGEMENTCENTER-MIB2", "nfssServTotNFSCalls"), ("NFSSTAT-SUNMANAGEMENTCENTER-MIB2", "nfssServBadNFSCalls"), ("NFSSTAT-SUNMANAGEMENTCENTER-MIB2", "nfssServPcntBadNFSCalls"), ("NFSSTAT-SUNMANAGEMENTCENTER-MIB2", "nfssServNFSCallRate"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    nfssServerNFSStatGroup = nfssServerNFSStatGroup.setStatus('current')
if mibBuilder.loadTexts: nfssServerNFSStatGroup.setDescription('NFS server calls related statistics.')
nfssClientRPCStatGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 42, 2, 12, 2, 2, 28, 1, 3)).setObjects(("NFSSTAT-SUNMANAGEMENTCENTER-MIB2", "nfssCliTotRPCCalls"), ("NFSSTAT-SUNMANAGEMENTCENTER-MIB2", "nfssCliBadRPCCalls"), ("NFSSTAT-SUNMANAGEMENTCENTER-MIB2", "nfssCliPcntBadRPCCalls"), ("NFSSTAT-SUNMANAGEMENTCENTER-MIB2", "nfssCliRPCCallRate"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    nfssClientRPCStatGroup = nfssClientRPCStatGroup.setStatus('current')
if mibBuilder.loadTexts: nfssClientRPCStatGroup.setDescription('RPC client calls related statistics.')
nfssClientNFSStatGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 42, 2, 12, 2, 2, 28, 1, 4)).setObjects(("NFSSTAT-SUNMANAGEMENTCENTER-MIB2", "nfssCliTotNFSCalls"), ("NFSSTAT-SUNMANAGEMENTCENTER-MIB2", "nfssCliBadNFSCalls"), ("NFSSTAT-SUNMANAGEMENTCENTER-MIB2", "nfssCliPcntBadNFSCalls"), ("NFSSTAT-SUNMANAGEMENTCENTER-MIB2", "nfssCliNFSCallRate"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    nfssClientNFSStatGroup = nfssClientNFSStatGroup.setStatus('current')
if mibBuilder.loadTexts: nfssClientNFSStatGroup.setDescription('NFS client calls related statistics.')
nfssTotServRPCCalls = MibScalar((1, 3, 6, 1, 4, 1, 42, 2, 12, 2, 2, 28, 1, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: nfssTotServRPCCalls.setStatus('current')
if mibBuilder.loadTexts: nfssTotServRPCCalls.setDescription('Total number of RPC server calls received by the host since last init. This is the total bad or good RPC server calls.')
nfssServBadRPCCalls = MibScalar((1, 3, 6, 1, 4, 1, 42, 2, 12, 2, 2, 28, 1, 1, 2), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: nfssServBadRPCCalls.setStatus('current')
if mibBuilder.loadTexts: nfssServBadRPCCalls.setDescription('Number of bad RPC server calls received since last init. This is the total number of RPC calls rejected by the RPC layer.')
nfssServPcntBadRPCCalls = MibScalar((1, 3, 6, 1, 4, 1, 42, 2, 12, 2, 2, 28, 1, 1, 3), DisplayString()).setUnits('%').setMaxAccess("readonly")
if mibBuilder.loadTexts: nfssServPcntBadRPCCalls.setStatus('current')
if mibBuilder.loadTexts: nfssServPcntBadRPCCalls.setDescription('Bad RPC server calls as a percentage of the total RPC server calls received.')
nfssServRPCCallRate = MibScalar((1, 3, 6, 1, 4, 1, 42, 2, 12, 2, 2, 28, 1, 1, 4), DisplayString()).setUnits('/sec').setMaxAccess("readonly")
if mibBuilder.loadTexts: nfssServRPCCallRate.setStatus('current')
if mibBuilder.loadTexts: nfssServRPCCallRate.setDescription('Rate at which server RPC calls are being received per second.')
nfssServTotNFSCalls = MibScalar((1, 3, 6, 1, 4, 1, 42, 2, 12, 2, 2, 28, 1, 2, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: nfssServTotNFSCalls.setStatus('current')
if mibBuilder.loadTexts: nfssServTotNFSCalls.setDescription('Total number of NFS server calls since last init. This is the total of bad and good NFS calls received by the server host. ')
nfssServBadNFSCalls = MibScalar((1, 3, 6, 1, 4, 1, 42, 2, 12, 2, 2, 28, 1, 2, 2), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: nfssServBadNFSCalls.setStatus('current')
if mibBuilder.loadTexts: nfssServBadNFSCalls.setDescription('Number of bad NFS server calls since last init. This is the total number of NFS calls rejected by the RPC layer.')
nfssServPcntBadNFSCalls = MibScalar((1, 3, 6, 1, 4, 1, 42, 2, 12, 2, 2, 28, 1, 2, 3), DisplayString()).setUnits('%').setMaxAccess("readonly")
if mibBuilder.loadTexts: nfssServPcntBadNFSCalls.setStatus('current')
if mibBuilder.loadTexts: nfssServPcntBadNFSCalls.setDescription('Bad NFS server calls as a percentage of the total server NFS calls received.')
nfssServNFSCallRate = MibScalar((1, 3, 6, 1, 4, 1, 42, 2, 12, 2, 2, 28, 1, 2, 4), DisplayString()).setUnits('/sec').setMaxAccess("readonly")
if mibBuilder.loadTexts: nfssServNFSCallRate.setStatus('current')
if mibBuilder.loadTexts: nfssServNFSCallRate.setDescription('Rate at which NFS server calls are being received per second.')
nfssCliTotRPCCalls = MibScalar((1, 3, 6, 1, 4, 1, 42, 2, 12, 2, 2, 28, 1, 3, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: nfssCliTotRPCCalls.setStatus('current')
if mibBuilder.loadTexts: nfssCliTotRPCCalls.setDescription('Total number of RPC client calls made by the host since last init. This is the total bad or good RPC client calls.')
nfssCliBadRPCCalls = MibScalar((1, 3, 6, 1, 4, 1, 42, 2, 12, 2, 2, 28, 1, 3, 2), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: nfssCliBadRPCCalls.setStatus('current')
if mibBuilder.loadTexts: nfssCliBadRPCCalls.setDescription('Number of bad RPC client calls since last init. This is the total number of RPC calls rejected by the RPC layer.')
nfssCliPcntBadRPCCalls = MibScalar((1, 3, 6, 1, 4, 1, 42, 2, 12, 2, 2, 28, 1, 3, 3), DisplayString()).setUnits('%').setMaxAccess("readonly")
if mibBuilder.loadTexts: nfssCliPcntBadRPCCalls.setStatus('current')
if mibBuilder.loadTexts: nfssCliPcntBadRPCCalls.setDescription('Bad RPC client calls as a percentage of the total RPC client calls made.')
nfssCliRPCCallRate = MibScalar((1, 3, 6, 1, 4, 1, 42, 2, 12, 2, 2, 28, 1, 3, 4), DisplayString()).setUnits('/sec').setMaxAccess("readonly")
if mibBuilder.loadTexts: nfssCliRPCCallRate.setStatus('current')
if mibBuilder.loadTexts: nfssCliRPCCallRate.setDescription('Rate at which RPC client calls are being made per second.')
nfssCliTotNFSCalls = MibScalar((1, 3, 6, 1, 4, 1, 42, 2, 12, 2, 2, 28, 1, 4, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: nfssCliTotNFSCalls.setStatus('current')
if mibBuilder.loadTexts: nfssCliTotNFSCalls.setDescription('Total number of NFS client calls made by the host since last init. This is the total bad or good NFS calls made by host.')
nfssCliBadNFSCalls = MibScalar((1, 3, 6, 1, 4, 1, 42, 2, 12, 2, 2, 28, 1, 4, 2), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: nfssCliBadNFSCalls.setStatus('current')
if mibBuilder.loadTexts: nfssCliBadNFSCalls.setDescription('Number of bad NFS client calls since last init. This is the total number of NFS calls rejected.')
nfssCliPcntBadNFSCalls = MibScalar((1, 3, 6, 1, 4, 1, 42, 2, 12, 2, 2, 28, 1, 4, 3), DisplayString()).setUnits('%').setMaxAccess("readonly")
if mibBuilder.loadTexts: nfssCliPcntBadNFSCalls.setStatus('current')
if mibBuilder.loadTexts: nfssCliPcntBadNFSCalls.setDescription('Bad NFS client calls as a percentage of the total NFS client calls made.')
nfssCliNFSCallRate = MibScalar((1, 3, 6, 1, 4, 1, 42, 2, 12, 2, 2, 28, 1, 4, 4), DisplayString()).setUnits('/sec').setMaxAccess("readonly")
if mibBuilder.loadTexts: nfssCliNFSCallRate.setStatus('current')
if mibBuilder.loadTexts: nfssCliNFSCallRate.setDescription('Rate at which NFS client calls are being made per second.')
mibBuilder.exportSymbols("NFSSTAT-SUNMANAGEMENTCENTER-MIB2", nfssServPcntBadRPCCalls=nfssServPcntBadRPCCalls, nfssCliBadNFSCalls=nfssCliBadNFSCalls, agent=agent, nfssServerNFSStatGroup=nfssServerNFSStatGroup, nfssTotServRPCCalls=nfssTotServRPCCalls, nfssServerRPCStatGroup=nfssServerRPCStatGroup, nfssCliBadRPCCalls=nfssCliBadRPCCalls, nfssCliTotRPCCalls=nfssCliTotRPCCalls, nfssCliPcntBadNFSCalls=nfssCliPcntBadNFSCalls, PYSNMP_MODULE_ID=nfsstat, nfssServNFSCallRate=nfssServNFSCallRate, nfssCliPcntBadRPCCalls=nfssCliPcntBadRPCCalls, nfssCliRPCCallRate=nfssCliRPCCallRate, sun=sun, nfssServRPCCallRate=nfssServRPCCallRate, nfssServBadRPCCalls=nfssServBadRPCCalls, nfssCliNFSCallRate=nfssCliNFSCallRate, nfssServPcntBadNFSCalls=nfssServPcntBadNFSCalls, sunsymon=sunsymon, prod=prod, nfssServTotNFSCalls=nfssServTotNFSCalls, nfsStats=nfsStats, nfssCliTotNFSCalls=nfssCliTotNFSCalls, modules=modules, nfssClientRPCStatGroup=nfssClientRPCStatGroup, nfssServBadNFSCalls=nfssServBadNFSCalls, nfsstat=nfsstat, nfssClientNFSStatGroup=nfssClientNFSStatGroup)