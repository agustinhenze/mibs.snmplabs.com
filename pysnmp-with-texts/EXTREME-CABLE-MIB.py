#
# PySNMP MIB module EXTREME-CABLE-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/EXTREME-BASE-MIB
# Produced by pysmi-0.3.4 at Wed May  1 13:07:14 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
ObjectIdentifier, Integer, OctetString = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "Integer", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, ValueSizeConstraint, ConstraintsUnion, SingleValueConstraint, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "ValueSizeConstraint", "ConstraintsUnion", "SingleValueConstraint", "ConstraintsIntersection")
extremeAgent, extremeV2Traps, extremenetworks = mibBuilder.importSymbols("EXTREME-BASE-MIB", "extremeAgent", "extremeV2Traps", "extremenetworks")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
Counter64, IpAddress, Integer32, Gauge32, Counter32, MibIdentifier, MibScalar, MibTable, MibTableRow, MibTableColumn, NotificationType, iso, ModuleIdentity, ObjectIdentity, TimeTicks, Bits, Unsigned32 = mibBuilder.importSymbols("SNMPv2-SMI", "Counter64", "IpAddress", "Integer32", "Gauge32", "Counter32", "MibIdentifier", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "NotificationType", "iso", "ModuleIdentity", "ObjectIdentity", "TimeTicks", "Bits", "Unsigned32")
TruthValue, DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "TruthValue", "DisplayString", "TextualConvention")
extremeCable = ModuleIdentity((1, 3, 6, 1, 4, 1, 1916, 1, 24))
if mibBuilder.loadTexts: extremeCable.setLastUpdated('0007240000Z')
if mibBuilder.loadTexts: extremeCable.setOrganization('Extreme Networks, Inc.')
if mibBuilder.loadTexts: extremeCable.setContactInfo('www.extremenetworks.com')
if mibBuilder.loadTexts: extremeCable.setDescription('Extreme-specific Cable objects')
extremeDiagConfigGroup = MibIdentifier((1, 3, 6, 1, 4, 1, 1916, 1, 24, 1))
extremeDiagConfigTime = MibScalar((1, 3, 6, 1, 4, 1, 1916, 1, 24, 1, 1), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(16, 16)).setFixedLength(16)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: extremeDiagConfigTime.setStatus('current')
if mibBuilder.loadTexts: extremeDiagConfigTime.setDescription('Indicates the time at which the Diagnostics information will be collected for the ports which have Auto-Diagnostics configured. Time must be given in hh:mm:ss format where hh, mm and ss are in decimals')
extremeDiagConfigRoF = MibScalar((1, 3, 6, 1, 4, 1, 1916, 1, 24, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("true", 1), ("false", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: extremeDiagConfigRoF.setStatus('current')
if mibBuilder.loadTexts: extremeDiagConfigRoF.setDescription('Indicates whether a port should return to INIT state on Diagnostics Failure. If TRUE the port will be restarted even if the Diagnostics indicate a Failure. If FALSE the port will be moved to DIAG_FAIL state')
extremeDiagPortConfigTable = MibTable((1, 3, 6, 1, 4, 1, 1916, 1, 24, 2), )
if mibBuilder.loadTexts: extremeDiagPortConfigTable.setStatus('current')
if mibBuilder.loadTexts: extremeDiagPortConfigTable.setDescription('Table, which contains the diagnostic configuration information for the ports')
extremeDiagPortConfigEntry = MibTableRow((1, 3, 6, 1, 4, 1, 1916, 1, 24, 2, 1), ).setIndexNames((0, "EXTREME-CABLE-MIB", "extremeDiagPortCfgPortIfIndex"), (0, "EXTREME-CABLE-MIB", "extremeDiagPortCfgMode"))
if mibBuilder.loadTexts: extremeDiagPortConfigEntry.setStatus('current')
if mibBuilder.loadTexts: extremeDiagPortConfigEntry.setDescription('Each row represents port related diagnostics configuration')
extremeDiagPortCfgPortIfIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 1916, 1, 24, 2, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: extremeDiagPortCfgPortIfIndex.setStatus('current')
if mibBuilder.loadTexts: extremeDiagPortCfgPortIfIndex.setDescription('IfIndex of the Port for which the information in this row applies')
extremeDiagPortCfgMode = MibTableColumn((1, 3, 6, 1, 4, 1, 1916, 1, 24, 2, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("auto", 1), ("manual", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: extremeDiagPortCfgMode.setStatus('current')
if mibBuilder.loadTexts: extremeDiagPortCfgMode.setDescription('The mode of operation. The port can be configured to have either manual diagnostics or auto-diagnostics collected.')
extremeDiagPortCfgStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 1916, 1, 24, 2, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))).clone(namedValues=NamedValues(("enable", 1), ("disable", 2), ("run", 3), ("diagfail", 4)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: extremeDiagPortCfgStatus.setStatus('current')
if mibBuilder.loadTexts: extremeDiagPortCfgStatus.setDescription('Specifies whether Diagnostics are enabled or disabled for the port. In the manual mode, enable and disable will disable the corresponding bit in the manual Diag portmask. Once the run command is given the Manual Diagnostics starts running. <diagfail> indicates the diagnostics for the port has failed. <diagfail> is a read-only value and cannot be used for setting the status of the port')
extremeDiagPortDiagTable = MibTable((1, 3, 6, 1, 4, 1, 1916, 1, 24, 3), )
if mibBuilder.loadTexts: extremeDiagPortDiagTable.setStatus('current')
if mibBuilder.loadTexts: extremeDiagPortDiagTable.setDescription('Table contains the diagnostic information for the ports')
extremeDiagPortDiagEntry = MibTableRow((1, 3, 6, 1, 4, 1, 1916, 1, 24, 3, 1), ).setIndexNames((0, "EXTREME-CABLE-MIB", "extremeDiagPortDiagPortIfIndex"), (0, "EXTREME-CABLE-MIB", "extremeDiagPortDiagMode"))
if mibBuilder.loadTexts: extremeDiagPortDiagEntry.setStatus('current')
if mibBuilder.loadTexts: extremeDiagPortDiagEntry.setDescription('Each row represents port related diagnostics information')
extremeDiagPortDiagPortIfIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 1916, 1, 24, 3, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: extremeDiagPortDiagPortIfIndex.setStatus('current')
if mibBuilder.loadTexts: extremeDiagPortDiagPortIfIndex.setDescription('IfIndex of the Port for which the information in this row applies')
extremeDiagPortDiagMode = MibTableColumn((1, 3, 6, 1, 4, 1, 1916, 1, 24, 3, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("auto", 1), ("manual", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: extremeDiagPortDiagMode.setStatus('current')
if mibBuilder.loadTexts: extremeDiagPortDiagMode.setDescription('The mode of operation. The port can be configured to have either manual diagnostics or auto-diagnostics collected.')
extremeDiagPortSpeed = MibTableColumn((1, 3, 6, 1, 4, 1, 1916, 1, 24, 3, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))).clone(namedValues=NamedValues(("speed10", 1), ("speed100", 2), ("speed1000", 3), ("unknown", 4)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: extremeDiagPortSpeed.setStatus('current')
if mibBuilder.loadTexts: extremeDiagPortSpeed.setDescription('Specifies the speed of the port')
extremeDiagPortSwapAB = MibTableColumn((1, 3, 6, 1, 4, 1, 1916, 1, 24, 3, 1, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("swap", 1), ("noswap", 2), ("unknown", 3)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: extremeDiagPortSwapAB.setStatus('current')
if mibBuilder.loadTexts: extremeDiagPortSwapAB.setDescription('Specifies whether pairA pairB cables are swapped')
extremeDiagPortSwapCD = MibTableColumn((1, 3, 6, 1, 4, 1, 1916, 1, 24, 3, 1, 5), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("swap", 1), ("noswap", 2), ("unknown", 3)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: extremeDiagPortSwapCD.setStatus('current')
if mibBuilder.loadTexts: extremeDiagPortSwapCD.setDescription('Specifies whether pairC and pairD cables are swapped')
extremeDiagPortPairAPol = MibTableColumn((1, 3, 6, 1, 4, 1, 1916, 1, 24, 3, 1, 6), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("positive", 1), ("negative", 2), ("unknown", 3)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: extremeDiagPortPairAPol.setStatus('current')
if mibBuilder.loadTexts: extremeDiagPortPairAPol.setDescription('Specifies the polarity of pairA cables')
extremeDiagPortPairAFlen = MibTableColumn((1, 3, 6, 1, 4, 1, 1916, 1, 24, 3, 1, 7), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: extremeDiagPortPairAFlen.setStatus('current')
if mibBuilder.loadTexts: extremeDiagPortPairAFlen.setDescription('Specifies the distance of Fault in the pairA cables')
extremeDiagPortPairALen = MibTableColumn((1, 3, 6, 1, 4, 1, 1916, 1, 24, 3, 1, 8), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: extremeDiagPortPairALen.setStatus('current')
if mibBuilder.loadTexts: extremeDiagPortPairALen.setDescription('Specifies the length of the pairA cables')
extremeDiagPortPairASkew = MibTableColumn((1, 3, 6, 1, 4, 1, 1916, 1, 24, 3, 1, 9), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: extremeDiagPortPairASkew.setStatus('current')
if mibBuilder.loadTexts: extremeDiagPortPairASkew.setDescription('Skew of pairA cables with respect to the fastest pair')
extremeDiagPortPairAStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 1916, 1, 24, 3, 1, 10), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5))).clone(namedValues=NamedValues(("open", 1), ("short", 2), ("terminated", 3), ("imperror", 4), ("unknown", 5)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: extremeDiagPortPairAStatus.setStatus('current')
if mibBuilder.loadTexts: extremeDiagPortPairAStatus.setDescription('Indicates whether pairA cables are properly terminated, short or open')
extremeDiagPortPairBPol = MibTableColumn((1, 3, 6, 1, 4, 1, 1916, 1, 24, 3, 1, 11), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("positive", 1), ("negative", 2), ("unknown", 3)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: extremeDiagPortPairBPol.setStatus('current')
if mibBuilder.loadTexts: extremeDiagPortPairBPol.setDescription('Specifies the polarity of pairB cables')
extremeDiagPortPairBFlen = MibTableColumn((1, 3, 6, 1, 4, 1, 1916, 1, 24, 3, 1, 12), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: extremeDiagPortPairBFlen.setStatus('current')
if mibBuilder.loadTexts: extremeDiagPortPairBFlen.setDescription('Specifies the distance of Fault in the pairB cables')
extremeDiagPortPairBLen = MibTableColumn((1, 3, 6, 1, 4, 1, 1916, 1, 24, 3, 1, 13), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: extremeDiagPortPairBLen.setStatus('current')
if mibBuilder.loadTexts: extremeDiagPortPairBLen.setDescription('Specifies the length of the pairB cables')
extremeDiagPortPairBSkew = MibTableColumn((1, 3, 6, 1, 4, 1, 1916, 1, 24, 3, 1, 14), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: extremeDiagPortPairBSkew.setStatus('current')
if mibBuilder.loadTexts: extremeDiagPortPairBSkew.setDescription('Skew of pairB cables with respect to the fastest pair')
extremeDiagPortPairBStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 1916, 1, 24, 3, 1, 15), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5))).clone(namedValues=NamedValues(("open", 1), ("short", 2), ("terminated", 3), ("imperror", 4), ("unknown", 5)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: extremeDiagPortPairBStatus.setStatus('current')
if mibBuilder.loadTexts: extremeDiagPortPairBStatus.setDescription('Indicates whether pairB cables are properly terminated, short or open')
extremeDiagPortPairCPol = MibTableColumn((1, 3, 6, 1, 4, 1, 1916, 1, 24, 3, 1, 16), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("positive", 1), ("negative", 2), ("unknown", 3)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: extremeDiagPortPairCPol.setStatus('current')
if mibBuilder.loadTexts: extremeDiagPortPairCPol.setDescription('Specifies the polarity of pairC cables')
extremeDiagPortPairCFlen = MibTableColumn((1, 3, 6, 1, 4, 1, 1916, 1, 24, 3, 1, 17), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: extremeDiagPortPairCFlen.setStatus('current')
if mibBuilder.loadTexts: extremeDiagPortPairCFlen.setDescription('Specifies the distance of Fault in the pairC cables')
extremeDiagPortPairCLen = MibTableColumn((1, 3, 6, 1, 4, 1, 1916, 1, 24, 3, 1, 18), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: extremeDiagPortPairCLen.setStatus('current')
if mibBuilder.loadTexts: extremeDiagPortPairCLen.setDescription('Specifies the length of the pairC cables')
extremeDiagPortPairCSkew = MibTableColumn((1, 3, 6, 1, 4, 1, 1916, 1, 24, 3, 1, 19), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: extremeDiagPortPairCSkew.setStatus('current')
if mibBuilder.loadTexts: extremeDiagPortPairCSkew.setDescription('Skew of pairC cables with respect to the fastest pair')
extremeDiagPortPairCStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 1916, 1, 24, 3, 1, 20), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5))).clone(namedValues=NamedValues(("open", 1), ("short", 2), ("terminated", 3), ("imperror", 4), ("unknown", 5)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: extremeDiagPortPairCStatus.setStatus('current')
if mibBuilder.loadTexts: extremeDiagPortPairCStatus.setDescription('Indicates whether pairC cables are properly terminated, short or open')
extremeDiagPortPairDPol = MibTableColumn((1, 3, 6, 1, 4, 1, 1916, 1, 24, 3, 1, 21), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("positive", 1), ("negative", 2), ("unknown", 3)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: extremeDiagPortPairDPol.setStatus('current')
if mibBuilder.loadTexts: extremeDiagPortPairDPol.setDescription('Specifies the polarity of pairD cables')
extremeDiagPortPairDFlen = MibTableColumn((1, 3, 6, 1, 4, 1, 1916, 1, 24, 3, 1, 22), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: extremeDiagPortPairDFlen.setStatus('current')
if mibBuilder.loadTexts: extremeDiagPortPairDFlen.setDescription('Specifies the distance of Fault in the pairD cables')
extremeDiagPortPairDLen = MibTableColumn((1, 3, 6, 1, 4, 1, 1916, 1, 24, 3, 1, 23), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: extremeDiagPortPairDLen.setStatus('current')
if mibBuilder.loadTexts: extremeDiagPortPairDLen.setDescription('Specifies the length of the pairD cables')
extremeDiagPortPairDSkew = MibTableColumn((1, 3, 6, 1, 4, 1, 1916, 1, 24, 3, 1, 24), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: extremeDiagPortPairDSkew.setStatus('current')
if mibBuilder.loadTexts: extremeDiagPortPairDSkew.setDescription('Skew of pairD cables with respect to the fastest pair')
extremeDiagPortPairDStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 1916, 1, 24, 3, 1, 25), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5))).clone(namedValues=NamedValues(("open", 1), ("short", 2), ("terminated", 3), ("imperror", 4), ("unknown", 5)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: extremeDiagPortPairDStatus.setStatus('current')
if mibBuilder.loadTexts: extremeDiagPortPairDStatus.setDescription('Indicates whether pairD cables are properly terminated, short or open')
extremeDiagPortDateTime = MibTableColumn((1, 3, 6, 1, 4, 1, 1916, 1, 24, 3, 1, 26), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(64, 64)).setFixedLength(64)).setMaxAccess("readonly")
if mibBuilder.loadTexts: extremeDiagPortDateTime.setStatus('current')
if mibBuilder.loadTexts: extremeDiagPortDateTime.setDescription('Date and time at which the Diagnostic information was collected')
extremeDiagPortStatsTable = MibTable((1, 3, 6, 1, 4, 1, 1916, 1, 24, 4), )
if mibBuilder.loadTexts: extremeDiagPortStatsTable.setStatus('current')
if mibBuilder.loadTexts: extremeDiagPortStatsTable.setDescription('Table, which contains the diagnostic statistic information for the ports')
extremeDiagPortStatsEntry = MibTableRow((1, 3, 6, 1, 4, 1, 1916, 1, 24, 4, 1), ).setIndexNames((0, "EXTREME-CABLE-MIB", "extremeDiagPortStatsPortIfIndex"))
if mibBuilder.loadTexts: extremeDiagPortStatsEntry.setStatus('current')
if mibBuilder.loadTexts: extremeDiagPortStatsEntry.setDescription('Each row represents port related diagnostics statistics information')
extremeDiagPortStatsPortIfIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 1916, 1, 24, 4, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: extremeDiagPortStatsPortIfIndex.setStatus('current')
if mibBuilder.loadTexts: extremeDiagPortStatsPortIfIndex.setDescription('IfIndex of the Port for which the information in this row applies')
extremeDiagPortStatsNumDiag = MibTableColumn((1, 3, 6, 1, 4, 1, 1916, 1, 24, 4, 1, 2), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: extremeDiagPortStatsNumDiag.setStatus('current')
if mibBuilder.loadTexts: extremeDiagPortStatsNumDiag.setDescription('Number of times Diagnostics information collected for this port')
extremeDiagPortStatsNumSuccess = MibTableColumn((1, 3, 6, 1, 4, 1, 1916, 1, 24, 4, 1, 3), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: extremeDiagPortStatsNumSuccess.setStatus('current')
if mibBuilder.loadTexts: extremeDiagPortStatsNumSuccess.setDescription('Number of times Diagnostics for this port completed successfully without any errors')
extremeDiagPortStatsNumFail = MibTableColumn((1, 3, 6, 1, 4, 1, 1916, 1, 24, 4, 1, 4), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: extremeDiagPortStatsNumFail.setStatus('current')
if mibBuilder.loadTexts: extremeDiagPortStatsNumFail.setDescription('Number of times Diagnostics for this port Failed due to errors in the cable pairs')
extremeDiagPortStatsNumChange = MibTableColumn((1, 3, 6, 1, 4, 1, 1916, 1, 24, 4, 1, 5), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: extremeDiagPortStatsNumChange.setStatus('current')
if mibBuilder.loadTexts: extremeDiagPortStatsNumChange.setDescription('Number of times Diagnostics Changed for this port')
extremeDiagPortStatsNumAbort = MibTableColumn((1, 3, 6, 1, 4, 1, 1916, 1, 24, 4, 1, 6), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: extremeDiagPortStatsNumAbort.setStatus('current')
if mibBuilder.loadTexts: extremeDiagPortStatsNumAbort.setDescription('Number of times Diagnostics was aborted by the user for this port')
extremeCableTraps = MibIdentifier((1, 3, 6, 1, 4, 1, 1916, 4, 13))
extremeCableTrapsPrefix = MibIdentifier((1, 3, 6, 1, 4, 1, 1916, 4, 13, 0))
extremeTrapDiagPortDiagnostics = NotificationType((1, 3, 6, 1, 4, 1, 1916, 4, 13, 0, 1)).setObjects(("EXTREME-CABLE-MIB", "extremeDiagPortCfgPortIfIndex"), ("EXTREME-CABLE-MIB", "extremeDiagPortCfgMode"), ("EXTREME-CABLE-MIB", "extremeDiagPortCfgStatus"))
if mibBuilder.loadTexts: extremeTrapDiagPortDiagnostics.setStatus('current')
if mibBuilder.loadTexts: extremeTrapDiagPortDiagnostics.setDescription('Indicates the status of Diagnostics for a port. The status indicates whether Diagnostics for a particular port failed')
mibBuilder.exportSymbols("EXTREME-CABLE-MIB", extremeDiagPortPairAFlen=extremeDiagPortPairAFlen, extremeDiagPortPairALen=extremeDiagPortPairALen, extremeDiagPortDiagPortIfIndex=extremeDiagPortDiagPortIfIndex, extremeDiagPortPairCStatus=extremeDiagPortPairCStatus, extremeDiagPortPairCSkew=extremeDiagPortPairCSkew, extremeDiagPortPairBPol=extremeDiagPortPairBPol, extremeDiagPortSwapAB=extremeDiagPortSwapAB, extremeDiagConfigTime=extremeDiagConfigTime, extremeDiagPortPairAStatus=extremeDiagPortPairAStatus, extremeDiagPortPairAPol=extremeDiagPortPairAPol, extremeDiagPortPairCPol=extremeDiagPortPairCPol, extremeDiagPortCfgStatus=extremeDiagPortCfgStatus, extremeDiagPortConfigEntry=extremeDiagPortConfigEntry, extremeDiagPortStatsNumAbort=extremeDiagPortStatsNumAbort, extremeDiagPortPairDSkew=extremeDiagPortPairDSkew, extremeCable=extremeCable, extremeCableTraps=extremeCableTraps, extremeDiagPortDateTime=extremeDiagPortDateTime, extremeDiagPortPairBSkew=extremeDiagPortPairBSkew, extremeTrapDiagPortDiagnostics=extremeTrapDiagPortDiagnostics, extremeDiagPortStatsTable=extremeDiagPortStatsTable, extremeDiagPortPairBLen=extremeDiagPortPairBLen, extremeDiagConfigRoF=extremeDiagConfigRoF, PYSNMP_MODULE_ID=extremeCable, extremeDiagPortDiagTable=extremeDiagPortDiagTable, extremeDiagPortPairASkew=extremeDiagPortPairASkew, extremeDiagPortStatsNumDiag=extremeDiagPortStatsNumDiag, extremeDiagPortPairCFlen=extremeDiagPortPairCFlen, extremeDiagPortPairBStatus=extremeDiagPortPairBStatus, extremeDiagPortPairDPol=extremeDiagPortPairDPol, extremeDiagPortDiagMode=extremeDiagPortDiagMode, extremeDiagConfigGroup=extremeDiagConfigGroup, extremeDiagPortSpeed=extremeDiagPortSpeed, extremeDiagPortPairDLen=extremeDiagPortPairDLen, extremeDiagPortCfgPortIfIndex=extremeDiagPortCfgPortIfIndex, extremeDiagPortStatsPortIfIndex=extremeDiagPortStatsPortIfIndex, extremeDiagPortPairCLen=extremeDiagPortPairCLen, extremeDiagPortConfigTable=extremeDiagPortConfigTable, extremeDiagPortStatsNumSuccess=extremeDiagPortStatsNumSuccess, extremeDiagPortStatsNumFail=extremeDiagPortStatsNumFail, extremeDiagPortPairBFlen=extremeDiagPortPairBFlen, extremeCableTrapsPrefix=extremeCableTrapsPrefix, extremeDiagPortCfgMode=extremeDiagPortCfgMode, extremeDiagPortSwapCD=extremeDiagPortSwapCD, extremeDiagPortStatsEntry=extremeDiagPortStatsEntry, extremeDiagPortStatsNumChange=extremeDiagPortStatsNumChange, extremeDiagPortPairDFlen=extremeDiagPortPairDFlen, extremeDiagPortDiagEntry=extremeDiagPortDiagEntry, extremeDiagPortPairDStatus=extremeDiagPortPairDStatus)