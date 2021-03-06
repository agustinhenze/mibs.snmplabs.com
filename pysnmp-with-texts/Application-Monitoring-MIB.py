#
# PySNMP MIB module Application-Monitoring-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/Application-Monitoring-MIB
# Produced by pysmi-0.3.4 at Wed May  1 11:33:17 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, SingleValueConstraint, ConstraintsIntersection, ConstraintsUnion, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsIntersection", "ConstraintsUnion", "ValueSizeConstraint")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
Counter64, MibScalar, MibTable, MibTableRow, MibTableColumn, ModuleIdentity, Gauge32, Counter32, NotificationType, MibIdentifier, IpAddress, Unsigned32, NotificationType, ObjectIdentity, Bits, TimeTicks, enterprises, iso, Integer32 = mibBuilder.importSymbols("SNMPv2-SMI", "Counter64", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "ModuleIdentity", "Gauge32", "Counter32", "NotificationType", "MibIdentifier", "IpAddress", "Unsigned32", "NotificationType", "ObjectIdentity", "Bits", "TimeTicks", "enterprises", "iso", "Integer32")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
sni = MibIdentifier((1, 3, 6, 1, 4, 1, 231))
sniProductMibs = MibIdentifier((1, 3, 6, 1, 4, 1, 231, 2))
sniAppMon = MibIdentifier((1, 3, 6, 1, 4, 1, 231, 2, 23))
sniAppMonSubSystems = MibIdentifier((1, 3, 6, 1, 4, 1, 231, 2, 23, 1))
sniAppMonBcamAppl = MibIdentifier((1, 3, 6, 1, 4, 1, 231, 2, 23, 2))
sniAppMonUserAppl = MibIdentifier((1, 3, 6, 1, 4, 1, 231, 2, 23, 3))
sniAppMonGlobalData = MibIdentifier((1, 3, 6, 1, 4, 1, 231, 2, 23, 5))
sniAppMonDcamAppl = MibIdentifier((1, 3, 6, 1, 4, 1, 231, 2, 23, 6))
appMonLogfiles = MibIdentifier((1, 3, 6, 1, 4, 1, 231, 2, 23, 7))
sniAppMonJVs = MibIdentifier((1, 3, 6, 1, 4, 1, 231, 2, 23, 8))
sniAppMonObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 231, 2, 23, 9))
appMonTraps = MibIdentifier((1, 3, 6, 1, 4, 1, 231, 2, 23, 20))
appMonSubsysTabNum = MibScalar((1, 3, 6, 1, 4, 1, 231, 2, 23, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: appMonSubsysTabNum.setStatus('mandatory')
if mibBuilder.loadTexts: appMonSubsysTabNum.setDescription('The number of entries in the table appMonSubsysTable')
appMonSubsysTable = MibTable((1, 3, 6, 1, 4, 1, 231, 2, 23, 1, 2), )
if mibBuilder.loadTexts: appMonSubsysTable.setStatus('mandatory')
if mibBuilder.loadTexts: appMonSubsysTable.setDescription('The Subsystem information table')
appMonSubsysEntry = MibTableRow((1, 3, 6, 1, 4, 1, 231, 2, 23, 1, 2, 1), ).setIndexNames((0, "Application-Monitoring-MIB", "appMonSubsysIndex"))
if mibBuilder.loadTexts: appMonSubsysEntry.setStatus('mandatory')
if mibBuilder.loadTexts: appMonSubsysEntry.setDescription('An entry in the table')
appMonSubsysIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 231, 2, 23, 1, 2, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: appMonSubsysIndex.setStatus('mandatory')
if mibBuilder.loadTexts: appMonSubsysIndex.setDescription('A unique value for each entry, its value ranges between 1 and the value of appMonSubsysTabNum')
appMonSubsysName = MibTableColumn((1, 3, 6, 1, 4, 1, 231, 2, 23, 1, 2, 1, 2), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: appMonSubsysName.setStatus('mandatory')
if mibBuilder.loadTexts: appMonSubsysName.setDescription('The name of the subsystem')
appMonSubsysVersion = MibTableColumn((1, 3, 6, 1, 4, 1, 231, 2, 23, 1, 2, 1, 3), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: appMonSubsysVersion.setStatus('mandatory')
if mibBuilder.loadTexts: appMonSubsysVersion.setDescription('The current version of the subsystem')
appMonSubsysState = MibTableColumn((1, 3, 6, 1, 4, 1, 231, 2, 23, 1, 2, 1, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 8, 255))).clone(namedValues=NamedValues(("created", 1), ("not-created", 2), ("in-delete", 3), ("in-create", 4), ("in-resume", 5), ("in-hold", 6), ("not-resumed", 7), ("locked", 8), ("unknown", 255)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: appMonSubsysState.setStatus('mandatory')
if mibBuilder.loadTexts: appMonSubsysState.setDescription('The current state of the subsystem')
appMonSubsysTasks = MibTableColumn((1, 3, 6, 1, 4, 1, 231, 2, 23, 1, 2, 1, 5), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: appMonSubsysTasks.setStatus('mandatory')
if mibBuilder.loadTexts: appMonSubsysTasks.setDescription('Number of tasks connected to the subsystem')
appMonBcamApplTabNum = MibScalar((1, 3, 6, 1, 4, 1, 231, 2, 23, 2, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: appMonBcamApplTabNum.setStatus('mandatory')
if mibBuilder.loadTexts: appMonBcamApplTabNum.setDescription('The number of entries in the table appMonTable')
appMonBcamApplTable = MibTable((1, 3, 6, 1, 4, 1, 231, 2, 23, 2, 2), )
if mibBuilder.loadTexts: appMonBcamApplTable.setStatus('mandatory')
if mibBuilder.loadTexts: appMonBcamApplTable.setDescription('The BCAM Application information table')
appMonBcamApplEntry = MibTableRow((1, 3, 6, 1, 4, 1, 231, 2, 23, 2, 2, 1), ).setIndexNames((0, "Application-Monitoring-MIB", "appMonBcamApplIndex"))
if mibBuilder.loadTexts: appMonBcamApplEntry.setStatus('mandatory')
if mibBuilder.loadTexts: appMonBcamApplEntry.setDescription('An entry in the table')
appMonBcamApplIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 231, 2, 23, 2, 2, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: appMonBcamApplIndex.setStatus('mandatory')
if mibBuilder.loadTexts: appMonBcamApplIndex.setDescription('A unique value for each entry, its value ranges between 1 and the value of appMonBcamApplTabNum')
appMonBcamApplName = MibTableColumn((1, 3, 6, 1, 4, 1, 231, 2, 23, 2, 2, 1, 2), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: appMonBcamApplName.setStatus('mandatory')
if mibBuilder.loadTexts: appMonBcamApplName.setDescription('The name of the BCAM application')
appMonBcamApplVersion = MibTableColumn((1, 3, 6, 1, 4, 1, 231, 2, 23, 2, 2, 1, 3), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: appMonBcamApplVersion.setStatus('mandatory')
if mibBuilder.loadTexts: appMonBcamApplVersion.setDescription('The current version of the BCAM application')
appMonBcamApplState = MibTableColumn((1, 3, 6, 1, 4, 1, 231, 2, 23, 2, 2, 1, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 255))).clone(namedValues=NamedValues(("running", 1), ("terminated", 2), ("aborted", 3), ("loaded", 4), ("in-hold", 5), ("scheduled", 6), ("unknown", 255)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: appMonBcamApplState.setStatus('mandatory')
if mibBuilder.loadTexts: appMonBcamApplState.setDescription('The current state of the BCAM application')
appMonBcamApplMonJV = MibTableColumn((1, 3, 6, 1, 4, 1, 231, 2, 23, 2, 2, 1, 5), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: appMonBcamApplMonJV.setStatus('mandatory')
if mibBuilder.loadTexts: appMonBcamApplMonJV.setDescription('Name of the MONJV monitoring the application')
appMonUserApplTabNum = MibScalar((1, 3, 6, 1, 4, 1, 231, 2, 23, 3, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: appMonUserApplTabNum.setStatus('mandatory')
if mibBuilder.loadTexts: appMonUserApplTabNum.setDescription('The number of entries in the table appMonTable')
appMonUserApplTable = MibTable((1, 3, 6, 1, 4, 1, 231, 2, 23, 3, 2), )
if mibBuilder.loadTexts: appMonUserApplTable.setStatus('mandatory')
if mibBuilder.loadTexts: appMonUserApplTable.setDescription('The User Application information table')
appMonUserApplEntry = MibTableRow((1, 3, 6, 1, 4, 1, 231, 2, 23, 3, 2, 1), ).setIndexNames((0, "Application-Monitoring-MIB", "appMonUserApplIndex"))
if mibBuilder.loadTexts: appMonUserApplEntry.setStatus('mandatory')
if mibBuilder.loadTexts: appMonUserApplEntry.setDescription('An entry in the table')
appMonUserApplIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 231, 2, 23, 3, 2, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: appMonUserApplIndex.setStatus('mandatory')
if mibBuilder.loadTexts: appMonUserApplIndex.setDescription('A unique value for each entry, its value ranges between 1 and the value of appMonUserApplTabNum')
appMonUserApplName = MibTableColumn((1, 3, 6, 1, 4, 1, 231, 2, 23, 3, 2, 1, 2), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: appMonUserApplName.setStatus('mandatory')
if mibBuilder.loadTexts: appMonUserApplName.setDescription('The name of the User application')
appMonUserApplVersion = MibTableColumn((1, 3, 6, 1, 4, 1, 231, 2, 23, 3, 2, 1, 3), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: appMonUserApplVersion.setStatus('mandatory')
if mibBuilder.loadTexts: appMonUserApplVersion.setDescription('The current version of the User application')
appMonUserApplState = MibTableColumn((1, 3, 6, 1, 4, 1, 231, 2, 23, 3, 2, 1, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 255))).clone(namedValues=NamedValues(("running", 1), ("terminated", 2), ("aborted", 3), ("loaded", 4), ("in-hold", 5), ("scheduled", 6), ("unknown", 255)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: appMonUserApplState.setStatus('mandatory')
if mibBuilder.loadTexts: appMonUserApplState.setDescription('The current state of the User application')
appMonUserApplMonJV = MibTableColumn((1, 3, 6, 1, 4, 1, 231, 2, 23, 3, 2, 1, 5), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: appMonUserApplMonJV.setStatus('mandatory')
if mibBuilder.loadTexts: appMonUserApplMonJV.setDescription('Name of the MONJV monitoring the application')
appMonVersion = MibScalar((1, 3, 6, 1, 4, 1, 231, 2, 23, 5, 1), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: appMonVersion.setStatus('mandatory')
if mibBuilder.loadTexts: appMonVersion.setDescription('Version of application monitor')
appMonConfFile = MibScalar((1, 3, 6, 1, 4, 1, 231, 2, 23, 5, 2), DisplayString()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: appMonConfFile.setStatus('mandatory')
if mibBuilder.loadTexts: appMonConfFile.setDescription('Pathname of the configuration file')
appMonTrapFormat = MibScalar((1, 3, 6, 1, 4, 1, 231, 2, 23, 5, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("generic", 1), ("tv-cc", 2), ("all", 3)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: appMonTrapFormat.setStatus('mandatory')
if mibBuilder.loadTexts: appMonTrapFormat.setDescription('Format of trap')
appMonDcamApplTabNum = MibScalar((1, 3, 6, 1, 4, 1, 231, 2, 23, 6, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: appMonDcamApplTabNum.setStatus('mandatory')
if mibBuilder.loadTexts: appMonDcamApplTabNum.setDescription('The number of entries in the table appMonDcamApplTable')
appMonDcamApplTable = MibTable((1, 3, 6, 1, 4, 1, 231, 2, 23, 6, 2), )
if mibBuilder.loadTexts: appMonDcamApplTable.setStatus('mandatory')
if mibBuilder.loadTexts: appMonDcamApplTable.setDescription('The DCAM Application information table')
appMonDcamApplEntry = MibTableRow((1, 3, 6, 1, 4, 1, 231, 2, 23, 6, 2, 1), ).setIndexNames((0, "Application-Monitoring-MIB", "appMonDcamApplIndex"))
if mibBuilder.loadTexts: appMonDcamApplEntry.setStatus('mandatory')
if mibBuilder.loadTexts: appMonDcamApplEntry.setDescription('An entry in the table')
appMonDcamApplIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 231, 2, 23, 6, 2, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: appMonDcamApplIndex.setStatus('mandatory')
if mibBuilder.loadTexts: appMonDcamApplIndex.setDescription('A unique value for each entry, its value ranges between 1 and the value of appMonDcamApplTabNum')
appMonDcamApplName = MibTableColumn((1, 3, 6, 1, 4, 1, 231, 2, 23, 6, 2, 1, 2), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: appMonDcamApplName.setStatus('mandatory')
if mibBuilder.loadTexts: appMonDcamApplName.setDescription('The name of the DCAM application')
appMonDcamApplHost = MibTableColumn((1, 3, 6, 1, 4, 1, 231, 2, 23, 6, 2, 1, 3), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: appMonDcamApplHost.setStatus('mandatory')
if mibBuilder.loadTexts: appMonDcamApplHost.setDescription('The host on which the DCAM application is running')
appMonDcamApplState = MibTableColumn((1, 3, 6, 1, 4, 1, 231, 2, 23, 6, 2, 1, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 255))).clone(namedValues=NamedValues(("running", 1), ("terminated", 2), ("unknown", 255)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: appMonDcamApplState.setStatus('mandatory')
if mibBuilder.loadTexts: appMonDcamApplState.setDescription('The current state of the DCAM application')
appMonLogfTabNum = MibScalar((1, 3, 6, 1, 4, 1, 231, 2, 23, 7, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: appMonLogfTabNum.setStatus('mandatory')
if mibBuilder.loadTexts: appMonLogfTabNum.setDescription('The number of entries in the table appMonLogfTable')
appMonLogfTable = MibTable((1, 3, 6, 1, 4, 1, 231, 2, 23, 7, 2), )
if mibBuilder.loadTexts: appMonLogfTable.setStatus('mandatory')
if mibBuilder.loadTexts: appMonLogfTable.setDescription('The Logfile table')
appMonLogfEntry = MibTableRow((1, 3, 6, 1, 4, 1, 231, 2, 23, 7, 2, 1), ).setIndexNames((0, "Application-Monitoring-MIB", "appMonLogfName"))
if mibBuilder.loadTexts: appMonLogfEntry.setStatus('mandatory')
if mibBuilder.loadTexts: appMonLogfEntry.setDescription('An entry in the table')
appMonLogfName = MibTableColumn((1, 3, 6, 1, 4, 1, 231, 2, 23, 7, 2, 1, 1), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: appMonLogfName.setStatus('mandatory')
if mibBuilder.loadTexts: appMonLogfName.setDescription('Pathname of the logfile')
appMonLogfAppl = MibTableColumn((1, 3, 6, 1, 4, 1, 231, 2, 23, 7, 2, 1, 2), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: appMonLogfAppl.setStatus('mandatory')
if mibBuilder.loadTexts: appMonLogfAppl.setDescription('The application name')
appMonLogfState = MibTableColumn((1, 3, 6, 1, 4, 1, 231, 2, 23, 7, 2, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5))).clone(namedValues=NamedValues(("deactive", 1), ("active", 2), ("start-begin", 3), ("start-new", 4), ("start-end", 5)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: appMonLogfState.setStatus('mandatory')
if mibBuilder.loadTexts: appMonLogfState.setDescription('The current monitoring state of the logfile is either active or deactive. For write operation either start-begin, start-new, start-end or deactive has to be specified')
appMonLogfPattern = MibTableColumn((1, 3, 6, 1, 4, 1, 231, 2, 23, 7, 2, 1, 4), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: appMonLogfPattern.setStatus('mandatory')
if mibBuilder.loadTexts: appMonLogfPattern.setDescription('Pattern for which a trap is generated ')
appMonJVTabNum = MibScalar((1, 3, 6, 1, 4, 1, 231, 2, 23, 8, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: appMonJVTabNum.setStatus('mandatory')
if mibBuilder.loadTexts: appMonJVTabNum.setDescription('The number of entries in the table appMonJVTable')
appMonJVTable = MibTable((1, 3, 6, 1, 4, 1, 231, 2, 23, 8, 2), )
if mibBuilder.loadTexts: appMonJVTable.setStatus('mandatory')
if mibBuilder.loadTexts: appMonJVTable.setDescription('The BCAM Application information table')
appMonJVEntry = MibTableRow((1, 3, 6, 1, 4, 1, 231, 2, 23, 8, 2, 1), ).setIndexNames((0, "Application-Monitoring-MIB", "appMonJVName"))
if mibBuilder.loadTexts: appMonJVEntry.setStatus('mandatory')
if mibBuilder.loadTexts: appMonJVEntry.setDescription('An entry in the table')
appMonJVName = MibTableColumn((1, 3, 6, 1, 4, 1, 231, 2, 23, 8, 2, 1, 1), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: appMonJVName.setStatus('mandatory')
if mibBuilder.loadTexts: appMonJVName.setDescription('Name of the JV')
appMonJVAppl = MibTableColumn((1, 3, 6, 1, 4, 1, 231, 2, 23, 8, 2, 1, 2), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: appMonJVAppl.setStatus('mandatory')
if mibBuilder.loadTexts: appMonJVAppl.setDescription('The application name')
appMonJVValue = MibTableColumn((1, 3, 6, 1, 4, 1, 231, 2, 23, 8, 2, 1, 3), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: appMonJVValue.setStatus('mandatory')
if mibBuilder.loadTexts: appMonJVValue.setDescription('The current value of the JV')
appMonJVPattern = MibTableColumn((1, 3, 6, 1, 4, 1, 231, 2, 23, 8, 2, 1, 4), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: appMonJVPattern.setStatus('mandatory')
if mibBuilder.loadTexts: appMonJVPattern.setDescription('Value pattern for which a trap will be sent')
appMonObjectsTabNum = MibScalar((1, 3, 6, 1, 4, 1, 231, 2, 23, 9, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: appMonObjectsTabNum.setStatus('mandatory')
if mibBuilder.loadTexts: appMonObjectsTabNum.setDescription('The number of entries in the table appMonObjectTable')
appMonObjectTable = MibTable((1, 3, 6, 1, 4, 1, 231, 2, 23, 9, 2), )
if mibBuilder.loadTexts: appMonObjectTable.setStatus('mandatory')
if mibBuilder.loadTexts: appMonObjectTable.setDescription('The Object table')
appMonObjectEntry = MibTableRow((1, 3, 6, 1, 4, 1, 231, 2, 23, 9, 2, 1), ).setIndexNames((0, "Application-Monitoring-MIB", "appMonObjectIndex"))
if mibBuilder.loadTexts: appMonObjectEntry.setStatus('mandatory')
if mibBuilder.loadTexts: appMonObjectEntry.setDescription('An entry in the table')
appMonObjectIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 231, 2, 23, 9, 2, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: appMonObjectIndex.setStatus('mandatory')
if mibBuilder.loadTexts: appMonObjectIndex.setDescription('A unique value for each entry, its value ranges between 1 and the value of appMonObjectTabNum')
appMonObjectName = MibTableColumn((1, 3, 6, 1, 4, 1, 231, 2, 23, 9, 2, 1, 2), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: appMonObjectName.setStatus('mandatory')
if mibBuilder.loadTexts: appMonObjectName.setDescription('The name of the object')
appMonObjectBcamAppl = MibTableColumn((1, 3, 6, 1, 4, 1, 231, 2, 23, 9, 2, 1, 3), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: appMonObjectBcamAppl.setStatus('mandatory')
if mibBuilder.loadTexts: appMonObjectBcamAppl.setDescription('Name of the BCAM applications belonging to the object')
appMonObjectUserAppl = MibTableColumn((1, 3, 6, 1, 4, 1, 231, 2, 23, 9, 2, 1, 4), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: appMonObjectUserAppl.setStatus('mandatory')
if mibBuilder.loadTexts: appMonObjectUserAppl.setDescription('Name of the user applications belonging to the object')
appMonObjectDcamAppl = MibTableColumn((1, 3, 6, 1, 4, 1, 231, 2, 23, 9, 2, 1, 5), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: appMonObjectDcamAppl.setStatus('mandatory')
if mibBuilder.loadTexts: appMonObjectDcamAppl.setDescription('Name of the DCAM applications belonging to the object')
appMonObjectSub = MibTableColumn((1, 3, 6, 1, 4, 1, 231, 2, 23, 9, 2, 1, 6), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: appMonObjectSub.setStatus('mandatory')
if mibBuilder.loadTexts: appMonObjectSub.setDescription('Name of the subsystems belonging to the object')
appMonObjectLogfile = MibTableColumn((1, 3, 6, 1, 4, 1, 231, 2, 23, 9, 2, 1, 7), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: appMonObjectLogfile.setStatus('mandatory')
if mibBuilder.loadTexts: appMonObjectLogfile.setDescription('Name of the logfiles belonging to the object')
appMonObjectJV = MibTableColumn((1, 3, 6, 1, 4, 1, 231, 2, 23, 9, 2, 1, 8), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: appMonObjectJV.setStatus('mandatory')
if mibBuilder.loadTexts: appMonObjectJV.setDescription('Name of the JVs belonging to the object')
appMonTrapData = MibIdentifier((1, 3, 6, 1, 4, 1, 231, 2, 23, 20, 1))
appMonSource = MibScalar((1, 3, 6, 1, 4, 1, 231, 2, 23, 20, 1, 1), DisplayString())
if mibBuilder.loadTexts: appMonSource.setStatus('mandatory')
if mibBuilder.loadTexts: appMonSource.setDescription(' ')
appMonDevice = MibScalar((1, 3, 6, 1, 4, 1, 231, 2, 23, 20, 1, 2), DisplayString())
if mibBuilder.loadTexts: appMonDevice.setStatus('mandatory')
if mibBuilder.loadTexts: appMonDevice.setDescription(' ')
appMonMsg = MibScalar((1, 3, 6, 1, 4, 1, 231, 2, 23, 20, 1, 3), DisplayString())
if mibBuilder.loadTexts: appMonMsg.setStatus('mandatory')
if mibBuilder.loadTexts: appMonMsg.setDescription(' ')
appMonWeight = MibScalar((1, 3, 6, 1, 4, 1, 231, 2, 23, 20, 1, 4), Integer32())
if mibBuilder.loadTexts: appMonWeight.setStatus('mandatory')
if mibBuilder.loadTexts: appMonWeight.setDescription(' ')
appMonAckOID = MibScalar((1, 3, 6, 1, 4, 1, 231, 2, 23, 20, 1, 6), ObjectIdentifier())
if mibBuilder.loadTexts: appMonAckOID.setStatus('mandatory')
if mibBuilder.loadTexts: appMonAckOID.setDescription(' ')
appMonGeneric = MibIdentifier((1, 3, 6, 1, 4, 1, 231, 2, 23, 20, 2))
appMonConfirm = MibIdentifier((1, 3, 6, 1, 4, 1, 231, 2, 23, 20, 3))
appMonGenTrap = NotificationType((1, 3, 6, 1, 4, 1, 231, 2, 23, 20, 2) + (0,999)).setObjects(("Application-Monitoring-MIB", "appMonSource"), ("Application-Monitoring-MIB", "appMonDevice"), ("Application-Monitoring-MIB", "appMonMsg"), ("Application-Monitoring-MIB", "appMonWeight"))
if mibBuilder.loadTexts: appMonGenTrap.setDescription('General application trap')
appMonConfirmTrap = NotificationType((1, 3, 6, 1, 4, 1, 231, 2, 23, 20, 3) + (0,999)).setObjects(("Application-Monitoring-MIB", "appMonSource"), ("Application-Monitoring-MIB", "appMonDevice"), ("Application-Monitoring-MIB", "appMonMsg"), ("Application-Monitoring-MIB", "appMonWeight"))
if mibBuilder.loadTexts: appMonConfirmTrap.setDescription('General application trap, the trap must be confirmed')
mibBuilder.exportSymbols("Application-Monitoring-MIB", appMonBcamApplTabNum=appMonBcamApplTabNum, appMonSubsysTabNum=appMonSubsysTabNum, appMonBcamApplMonJV=appMonBcamApplMonJV, appMonConfFile=appMonConfFile, appMonVersion=appMonVersion, appMonSource=appMonSource, appMonJVValue=appMonJVValue, appMonBcamApplState=appMonBcamApplState, appMonLogfPattern=appMonLogfPattern, appMonDevice=appMonDevice, appMonDcamApplHost=appMonDcamApplHost, appMonTraps=appMonTraps, appMonSubsysVersion=appMonSubsysVersion, appMonLogfTabNum=appMonLogfTabNum, appMonGeneric=appMonGeneric, sniAppMonObjects=sniAppMonObjects, appMonObjectUserAppl=appMonObjectUserAppl, appMonLogfTable=appMonLogfTable, appMonSubsysIndex=appMonSubsysIndex, appMonJVEntry=appMonJVEntry, appMonAckOID=appMonAckOID, appMonSubsysTable=appMonSubsysTable, appMonObjectDcamAppl=appMonObjectDcamAppl, appMonTrapData=appMonTrapData, sniAppMon=sniAppMon, appMonBcamApplTable=appMonBcamApplTable, appMonDcamApplIndex=appMonDcamApplIndex, appMonObjectIndex=appMonObjectIndex, appMonGenTrap=appMonGenTrap, appMonDcamApplEntry=appMonDcamApplEntry, appMonObjectsTabNum=appMonObjectsTabNum, appMonDcamApplState=appMonDcamApplState, appMonSubsysEntry=appMonSubsysEntry, appMonJVTabNum=appMonJVTabNum, appMonWeight=appMonWeight, appMonUserApplEntry=appMonUserApplEntry, sniAppMonSubSystems=sniAppMonSubSystems, appMonObjectLogfile=appMonObjectLogfile, appMonLogfState=appMonLogfState, sniAppMonDcamAppl=sniAppMonDcamAppl, appMonMsg=appMonMsg, appMonLogfEntry=appMonLogfEntry, appMonUserApplState=appMonUserApplState, appMonSubsysTasks=appMonSubsysTasks, appMonLogfName=appMonLogfName, sniProductMibs=sniProductMibs, sniAppMonJVs=sniAppMonJVs, appMonSubsysName=appMonSubsysName, appMonConfirm=appMonConfirm, appMonDcamApplTabNum=appMonDcamApplTabNum, appMonConfirmTrap=appMonConfirmTrap, appMonUserApplTabNum=appMonUserApplTabNum, appMonObjectName=appMonObjectName, appMonDcamApplName=appMonDcamApplName, appMonBcamApplIndex=appMonBcamApplIndex, appMonJVTable=appMonJVTable, appMonLogfiles=appMonLogfiles, appMonLogfAppl=appMonLogfAppl, appMonSubsysState=appMonSubsysState, appMonDcamApplTable=appMonDcamApplTable, appMonJVPattern=appMonJVPattern, sniAppMonGlobalData=sniAppMonGlobalData, appMonBcamApplEntry=appMonBcamApplEntry, appMonBcamApplVersion=appMonBcamApplVersion, sniAppMonUserAppl=sniAppMonUserAppl, appMonJVAppl=appMonJVAppl, appMonObjectJV=appMonObjectJV, appMonUserApplIndex=appMonUserApplIndex, appMonBcamApplName=appMonBcamApplName, appMonObjectEntry=appMonObjectEntry, appMonUserApplTable=appMonUserApplTable, appMonObjectSub=appMonObjectSub, appMonUserApplMonJV=appMonUserApplMonJV, appMonJVName=appMonJVName, appMonObjectBcamAppl=appMonObjectBcamAppl, appMonTrapFormat=appMonTrapFormat, appMonObjectTable=appMonObjectTable, sniAppMonBcamAppl=sniAppMonBcamAppl, appMonUserApplName=appMonUserApplName, sni=sni, appMonUserApplVersion=appMonUserApplVersion)
