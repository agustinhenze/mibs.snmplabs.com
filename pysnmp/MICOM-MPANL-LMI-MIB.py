#
# PySNMP MIB module MICOM-MPANL-LMI-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/MICOM-MPANL-LMI-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 20:02:06 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
OctetString, Integer, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "OctetString", "Integer", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, ConstraintsIntersection, ConstraintsUnion, ValueSizeConstraint, SingleValueConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "ConstraintsIntersection", "ConstraintsUnion", "ValueSizeConstraint", "SingleValueConstraint")
micom_oscar, = mibBuilder.importSymbols("MICOM-OSCAR-MIB", "micom-oscar")
mcmSysAsciiTimeOfDay, = mibBuilder.importSymbols("MICOM-SYS-MIB", "mcmSysAsciiTimeOfDay")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
MibIdentifier, Counter64, NotificationType, Gauge32, NotificationType, Counter32, TimeTicks, Bits, Unsigned32, IpAddress, Integer32, ModuleIdentity, ObjectIdentity, iso, MibScalar, MibTable, MibTableRow, MibTableColumn = mibBuilder.importSymbols("SNMPv2-SMI", "MibIdentifier", "Counter64", "NotificationType", "Gauge32", "NotificationType", "Counter32", "TimeTicks", "Bits", "Unsigned32", "IpAddress", "Integer32", "ModuleIdentity", "ObjectIdentity", "iso", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
micom_mlmi = MibIdentifier((1, 3, 6, 1, 4, 1, 335, 1, 4, 20)).setLabel("micom-mlmi")
mlmi_configuration = MibIdentifier((1, 3, 6, 1, 4, 1, 335, 1, 4, 20, 1)).setLabel("mlmi-configuration")
mlmi_control = MibIdentifier((1, 3, 6, 1, 4, 1, 335, 1, 4, 20, 2)).setLabel("mlmi-control")
mlmi_statistics = MibIdentifier((1, 3, 6, 1, 4, 1, 335, 1, 4, 20, 3)).setLabel("mlmi-statistics")
mlmi_status = MibIdentifier((1, 3, 6, 1, 4, 1, 335, 1, 4, 20, 4)).setLabel("mlmi-status")
mcmMLMIGenCfg4400Type = MibScalar((1, 3, 6, 1, 4, 1, 335, 1, 4, 20, 1, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("micom-4400", 1), ("nortel-DPN-4400", 2))).clone('nortel-DPN-4400')).setMaxAccess("readonly")
if mibBuilder.loadTexts: mcmMLMIGenCfg4400Type.setStatus('obsolete')
mcmMLMIGenCfgSoftwareRev = MibScalar((1, 3, 6, 1, 4, 1, 335, 1, 4, 20, 1, 2), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 16))).setMaxAccess("readonly")
if mibBuilder.loadTexts: mcmMLMIGenCfgSoftwareRev.setStatus('mandatory')
mcmMLMIServiceTable = MibTable((1, 3, 6, 1, 4, 1, 335, 1, 4, 20, 1, 3), )
if mibBuilder.loadTexts: mcmMLMIServiceTable.setStatus('mandatory')
mcmMLMIServiceEntry = MibTableRow((1, 3, 6, 1, 4, 1, 335, 1, 4, 20, 1, 3, 1), ).setIndexNames((0, "MICOM-MPANL-LMI-MIB", "mcmMLMIServiceIfIndex"))
if mibBuilder.loadTexts: mcmMLMIServiceEntry.setStatus('mandatory')
mcmMLMIServiceIfIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 335, 1, 4, 20, 1, 3, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 255))).setMaxAccess("readonly")
if mibBuilder.loadTexts: mcmMLMIServiceIfIndex.setStatus('mandatory')
mcmMLMIServiceCUGFacility = MibTableColumn((1, 3, 6, 1, 4, 1, 335, 1, 4, 20, 1, 3, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("no-CUG", 1), ("simple-CUG", 2), ("cUG-selection", 3))).clone('no-CUG')).setMaxAccess("readonly")
if mibBuilder.loadTexts: mcmMLMIServiceCUGFacility.setStatus('mandatory')
mcmMLMIServiceCUGAccess = MibTableColumn((1, 3, 6, 1, 4, 1, 335, 1, 4, 20, 1, 3, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))).clone(namedValues=NamedValues(("no-right", 1), ("outgoing-access-right", 2), ("incoming-access-right", 3), ("incoming-outgoing-access-right", 4))).clone('no-right')).setMaxAccess("readonly")
if mibBuilder.loadTexts: mcmMLMIServiceCUGAccess.setStatus('mandatory')
mcmMLMIServiceCUGICType = MibTableColumn((1, 3, 6, 1, 4, 1, 335, 1, 4, 20, 1, 3, 1, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("national-IC", 1), ("international-IC", 2))).clone('national-IC')).setMaxAccess("readonly")
if mibBuilder.loadTexts: mcmMLMIServiceCUGICType.setStatus('mandatory')
mcmMLMIServiceCUGIC = MibTableColumn((1, 3, 6, 1, 4, 1, 335, 1, 4, 20, 1, 3, 1, 5), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(1, 5))).setMaxAccess("readonly")
if mibBuilder.loadTexts: mcmMLMIServiceCUGIC.setStatus('mandatory')
mcmMLMIServiceDNASuffix = MibTableColumn((1, 3, 6, 1, 4, 1, 335, 1, 4, 20, 1, 3, 1, 6), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 3))).setMaxAccess("readonly")
if mibBuilder.loadTexts: mcmMLMIServiceDNASuffix.setStatus('mandatory')
mcmMLMINetlinkTable = MibTable((1, 3, 6, 1, 4, 1, 335, 1, 4, 20, 1, 6), )
if mibBuilder.loadTexts: mcmMLMINetlinkTable.setStatus('mandatory')
mcmMLMINetlinkEntry = MibTableRow((1, 3, 6, 1, 4, 1, 335, 1, 4, 20, 1, 6, 1), ).setIndexNames((0, "MICOM-MPANL-LMI-MIB", "mcmMLMINetlinkIfIndex"))
if mibBuilder.loadTexts: mcmMLMINetlinkEntry.setStatus('mandatory')
mcmMLMINetlinkIfIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 335, 1, 4, 20, 1, 6, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 255))).setMaxAccess("readonly")
if mibBuilder.loadTexts: mcmMLMINetlinkIfIndex.setStatus('mandatory')
mcmMLMINetlinkTunnelingPVCDlci = MibTableColumn((1, 3, 6, 1, 4, 1, 335, 1, 4, 20, 1, 6, 1, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(16, 991))).setMaxAccess("readonly")
if mibBuilder.loadTexts: mcmMLMINetlinkTunnelingPVCDlci.setStatus('mandatory')
mcmMLMINetlinkMpanlMode = MibTableColumn((1, 3, 6, 1, 4, 1, 335, 1, 4, 20, 1, 6, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("dte", 1), ("dce", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: mcmMLMINetlinkMpanlMode.setStatus('mandatory')
mcmMLMINetlinkDLCIAssignMethod = MibTableColumn((1, 3, 6, 1, 4, 1, 335, 1, 4, 20, 1, 6, 1, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("increment", 1), ("decrement", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: mcmMLMINetlinkDLCIAssignMethod.setStatus('mandatory')
mcmMLMINetlinkRstrtT316Timer = MibTableColumn((1, 3, 6, 1, 4, 1, 335, 1, 4, 20, 1, 6, 1, 5), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 16))).setMaxAccess("readonly")
if mibBuilder.loadTexts: mcmMLMINetlinkRstrtT316Timer.setStatus('mandatory')
mcmMLMINetlinkRstrtAckT317Timer = MibTableColumn((1, 3, 6, 1, 4, 1, 335, 1, 4, 20, 1, 6, 1, 6), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 16))).setMaxAccess("readonly")
if mibBuilder.loadTexts: mcmMLMINetlinkRstrtAckT317Timer.setStatus('mandatory')
mcmMLMINetlinkNumUnsuccesRstrtAtmpts = MibTableColumn((1, 3, 6, 1, 4, 1, 335, 1, 4, 20, 1, 6, 1, 7), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 5))).setMaxAccess("readonly")
if mibBuilder.loadTexts: mcmMLMINetlinkNumUnsuccesRstrtAtmpts.setStatus('mandatory')
nvmMLMIGenCfg4400Type = MibScalar((1, 3, 6, 1, 4, 1, 335, 1, 4, 20, 1, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("micom-4400", 1), ("nortel-DPN-4400", 2))).clone('nortel-DPN-4400')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: nvmMLMIGenCfg4400Type.setStatus('obsolete')
nvmMLMIServiceTable = MibTable((1, 3, 6, 1, 4, 1, 335, 1, 4, 20, 1, 5), )
if mibBuilder.loadTexts: nvmMLMIServiceTable.setStatus('mandatory')
nvmMLMIServiceEntry = MibTableRow((1, 3, 6, 1, 4, 1, 335, 1, 4, 20, 1, 5, 1), ).setIndexNames((0, "MICOM-MPANL-LMI-MIB", "nvmMLMIServiceIfIndex"))
if mibBuilder.loadTexts: nvmMLMIServiceEntry.setStatus('mandatory')
nvmMLMIServiceIfIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 335, 1, 4, 20, 1, 5, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 255))).setMaxAccess("readonly")
if mibBuilder.loadTexts: nvmMLMIServiceIfIndex.setStatus('mandatory')
nvmMLMIServiceCUGFacility = MibTableColumn((1, 3, 6, 1, 4, 1, 335, 1, 4, 20, 1, 5, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("no-CUG", 1), ("simple-CUG", 2), ("cUG-selection", 3))).clone('no-CUG')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: nvmMLMIServiceCUGFacility.setStatus('mandatory')
nvmMLMIServiceCUGAccess = MibTableColumn((1, 3, 6, 1, 4, 1, 335, 1, 4, 20, 1, 5, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))).clone(namedValues=NamedValues(("no-right", 1), ("outgoing-access-right", 2), ("incoming-access-right", 3), ("incoming-outgoing-access-right", 4))).clone('no-right')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: nvmMLMIServiceCUGAccess.setStatus('mandatory')
nvmMLMIServiceCUGICType = MibTableColumn((1, 3, 6, 1, 4, 1, 335, 1, 4, 20, 1, 5, 1, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("national-IC", 1), ("international-IC", 2))).clone('national-IC')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: nvmMLMIServiceCUGICType.setStatus('mandatory')
nvmMLMIServiceCUGIC = MibTableColumn((1, 3, 6, 1, 4, 1, 335, 1, 4, 20, 1, 5, 1, 5), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(1, 5))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: nvmMLMIServiceCUGIC.setStatus('mandatory')
nvmMLMIServiceDNASuffix = MibTableColumn((1, 3, 6, 1, 4, 1, 335, 1, 4, 20, 1, 5, 1, 6), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 3))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: nvmMLMIServiceDNASuffix.setStatus('mandatory')
nvmMLMIServiceRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 335, 1, 4, 20, 1, 5, 1, 7), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("add", 1), ("delete", 2), ("active", 3)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: nvmMLMIServiceRowStatus.setStatus('mandatory')
nvmMLMINetlinkTable = MibTable((1, 3, 6, 1, 4, 1, 335, 1, 4, 20, 1, 7), )
if mibBuilder.loadTexts: nvmMLMINetlinkTable.setStatus('mandatory')
nvmMLMINetlinkEntry = MibTableRow((1, 3, 6, 1, 4, 1, 335, 1, 4, 20, 1, 7, 1), ).setIndexNames((0, "MICOM-MPANL-LMI-MIB", "nvmMLMINetlinkIfIndex"))
if mibBuilder.loadTexts: nvmMLMINetlinkEntry.setStatus('mandatory')
nvmMLMINetlinkIfIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 335, 1, 4, 20, 1, 7, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 255))).setMaxAccess("readonly")
if mibBuilder.loadTexts: nvmMLMINetlinkIfIndex.setStatus('mandatory')
nvmMLMINetlinkTunnelingPVCDlci = MibTableColumn((1, 3, 6, 1, 4, 1, 335, 1, 4, 20, 1, 7, 1, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(16, 991))).setMaxAccess("readonly")
if mibBuilder.loadTexts: nvmMLMINetlinkTunnelingPVCDlci.setStatus('mandatory')
nvmMLMINetlinkDLCIAssignMethod = MibTableColumn((1, 3, 6, 1, 4, 1, 335, 1, 4, 20, 1, 7, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("increment", 1), ("decrement", 2))).clone('increment')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: nvmMLMINetlinkDLCIAssignMethod.setStatus('mandatory')
nvmMLMINetlinkRstrtT316Timer = MibTableColumn((1, 3, 6, 1, 4, 1, 335, 1, 4, 20, 1, 7, 1, 4), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 16)).clone(5)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: nvmMLMINetlinkRstrtT316Timer.setStatus('mandatory')
nvmMLMINetlinkRstrtAckT317Timer = MibTableColumn((1, 3, 6, 1, 4, 1, 335, 1, 4, 20, 1, 7, 1, 5), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 16)).clone(5)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: nvmMLMINetlinkRstrtAckT317Timer.setStatus('mandatory')
nvmMLMINetlinkNumUnsuccesRstrtAtmpts = MibTableColumn((1, 3, 6, 1, 4, 1, 335, 1, 4, 20, 1, 7, 1, 6), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 5)).clone(2)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: nvmMLMINetlinkNumUnsuccesRstrtAtmpts.setStatus('mandatory')
mcmMLMIStatsActiveVCs = MibScalar((1, 3, 6, 1, 4, 1, 335, 1, 4, 20, 3, 1), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mcmMLMIStatsActiveVCs.setStatus('mandatory')
mcmMLMIStatsRequestedCalls = MibScalar((1, 3, 6, 1, 4, 1, 335, 1, 4, 20, 3, 2), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mcmMLMIStatsRequestedCalls.setStatus('mandatory')
mcmMLMIStatsInitiatedCalls = MibScalar((1, 3, 6, 1, 4, 1, 335, 1, 4, 20, 3, 3), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mcmMLMIStatsInitiatedCalls.setStatus('mandatory')
mcmMLMIStatsFailedCalls = MibScalar((1, 3, 6, 1, 4, 1, 335, 1, 4, 20, 3, 4), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mcmMLMIStatsFailedCalls.setStatus('mandatory')
mcmMLMIStatsSucceededCalls = MibScalar((1, 3, 6, 1, 4, 1, 335, 1, 4, 20, 3, 5), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mcmMLMIStatsSucceededCalls.setStatus('mandatory')
mcmMLMIStatsReleasedCalls = MibScalar((1, 3, 6, 1, 4, 1, 335, 1, 4, 20, 3, 6), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mcmMLMIStatsReleasedCalls.setStatus('mandatory')
mcmMLMIStatsDisconnectedCalls = MibScalar((1, 3, 6, 1, 4, 1, 335, 1, 4, 20, 3, 7), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mcmMLMIStatsDisconnectedCalls.setStatus('mandatory')
mcmMLMIStatsAdmittedCUGs = MibScalar((1, 3, 6, 1, 4, 1, 335, 1, 4, 20, 3, 8), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mcmMLMIStatsAdmittedCUGs.setStatus('mandatory')
mcmMLMIStatsRejectedCUGs = MibScalar((1, 3, 6, 1, 4, 1, 335, 1, 4, 20, 3, 9), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mcmMLMIStatsRejectedCUGs.setStatus('mandatory')
mcmMLMINetlinkStatTable = MibTable((1, 3, 6, 1, 4, 1, 335, 1, 4, 20, 3, 10), )
if mibBuilder.loadTexts: mcmMLMINetlinkStatTable.setStatus('mandatory')
mcmMLMINetlinkStatEntry = MibTableRow((1, 3, 6, 1, 4, 1, 335, 1, 4, 20, 3, 10, 1), ).setIndexNames((0, "MICOM-MPANL-LMI-MIB", "mcmMLMINetlinkStatIfIndex"))
if mibBuilder.loadTexts: mcmMLMINetlinkStatEntry.setStatus('mandatory')
mcmMLMINetlinkStatIfIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 335, 1, 4, 20, 3, 10, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 255))).setMaxAccess("readonly")
if mibBuilder.loadTexts: mcmMLMINetlinkStatIfIndex.setStatus('mandatory')
mcmMLMINetlinkStatMsgRxSetup = MibTableColumn((1, 3, 6, 1, 4, 1, 335, 1, 4, 20, 3, 10, 1, 2), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mcmMLMINetlinkStatMsgRxSetup.setStatus('mandatory')
mcmMLMINetlinkStatMsgTxSetup = MibTableColumn((1, 3, 6, 1, 4, 1, 335, 1, 4, 20, 3, 10, 1, 3), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mcmMLMINetlinkStatMsgTxSetup.setStatus('mandatory')
mcmMLMINetlinkStatMsgRxCallPrcdngs = MibTableColumn((1, 3, 6, 1, 4, 1, 335, 1, 4, 20, 3, 10, 1, 4), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mcmMLMINetlinkStatMsgRxCallPrcdngs.setStatus('mandatory')
mcmMLMINetlinkStatMsgTxCallPrcdngs = MibTableColumn((1, 3, 6, 1, 4, 1, 335, 1, 4, 20, 3, 10, 1, 5), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mcmMLMINetlinkStatMsgTxCallPrcdngs.setStatus('mandatory')
mcmMLMINetlinkStatMsgRxConn = MibTableColumn((1, 3, 6, 1, 4, 1, 335, 1, 4, 20, 3, 10, 1, 6), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mcmMLMINetlinkStatMsgRxConn.setStatus('mandatory')
mcmMLMINetlinkStatMsgTxConn = MibTableColumn((1, 3, 6, 1, 4, 1, 335, 1, 4, 20, 3, 10, 1, 7), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mcmMLMINetlinkStatMsgTxConn.setStatus('mandatory')
mcmMLMINetlinkStatMsgRxDisConn = MibTableColumn((1, 3, 6, 1, 4, 1, 335, 1, 4, 20, 3, 10, 1, 8), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mcmMLMINetlinkStatMsgRxDisConn.setStatus('mandatory')
mcmMLMINetlinkStatMsgTxDisConn = MibTableColumn((1, 3, 6, 1, 4, 1, 335, 1, 4, 20, 3, 10, 1, 9), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mcmMLMINetlinkStatMsgTxDisConn.setStatus('mandatory')
mcmMLMINetlinkStatMsgRxRls = MibTableColumn((1, 3, 6, 1, 4, 1, 335, 1, 4, 20, 3, 10, 1, 10), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mcmMLMINetlinkStatMsgRxRls.setStatus('mandatory')
mcmMLMINetlinkStatMsgTxRls = MibTableColumn((1, 3, 6, 1, 4, 1, 335, 1, 4, 20, 3, 10, 1, 11), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mcmMLMINetlinkStatMsgTxRls.setStatus('mandatory')
mcmMLMINetlinkStatMsgRxRlseComp = MibTableColumn((1, 3, 6, 1, 4, 1, 335, 1, 4, 20, 3, 10, 1, 12), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mcmMLMINetlinkStatMsgRxRlseComp.setStatus('mandatory')
mcmMLMINetlinkStatMsgTxRlseComp = MibTableColumn((1, 3, 6, 1, 4, 1, 335, 1, 4, 20, 3, 10, 1, 13), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mcmMLMINetlinkStatMsgTxRlseComp.setStatus('mandatory')
mcmMLMINetlinkStatMsgRxStatusInq = MibTableColumn((1, 3, 6, 1, 4, 1, 335, 1, 4, 20, 3, 10, 1, 14), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mcmMLMINetlinkStatMsgRxStatusInq.setStatus('mandatory')
mcmMLMINetlinkStatMsgTxStatusInq = MibTableColumn((1, 3, 6, 1, 4, 1, 335, 1, 4, 20, 3, 10, 1, 15), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mcmMLMINetlinkStatMsgTxStatusInq.setStatus('mandatory')
mcmMLMINetlinkStatMsgRxStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 335, 1, 4, 20, 3, 10, 1, 16), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mcmMLMINetlinkStatMsgRxStatus.setStatus('mandatory')
mcmMLMINetlinkStatMsgTxStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 335, 1, 4, 20, 3, 10, 1, 17), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mcmMLMINetlinkStatMsgTxStatus.setStatus('mandatory')
mcmMLMINetlinkStatLocalSVC = MibTableColumn((1, 3, 6, 1, 4, 1, 335, 1, 4, 20, 3, 10, 1, 18), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mcmMLMINetlinkStatLocalSVC.setStatus('mandatory')
mcmMLMINetlinkStatTransitSVC = MibTableColumn((1, 3, 6, 1, 4, 1, 335, 1, 4, 20, 3, 10, 1, 19), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mcmMLMINetlinkStatTransitSVC.setStatus('mandatory')
mcmMLMINetlinkStatVoiceCalls = MibTableColumn((1, 3, 6, 1, 4, 1, 335, 1, 4, 20, 3, 10, 1, 20), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mcmMLMINetlinkStatVoiceCalls.setStatus('mandatory')
mcmMLMINetlinkStatLanCalls = MibTableColumn((1, 3, 6, 1, 4, 1, 335, 1, 4, 20, 3, 10, 1, 21), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mcmMLMINetlinkStatLanCalls.setStatus('mandatory')
mcmMLMINetlinkStatRsiCalls = MibTableColumn((1, 3, 6, 1, 4, 1, 335, 1, 4, 20, 3, 10, 1, 22), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mcmMLMINetlinkStatRsiCalls.setStatus('mandatory')
mcmMLMINetlinkStatSpvcCalls = MibTableColumn((1, 3, 6, 1, 4, 1, 335, 1, 4, 20, 3, 10, 1, 23), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mcmMLMINetlinkStatSpvcCalls.setStatus('mandatory')
mcmMLMINetlinkStatLnkupCnt = MibTableColumn((1, 3, 6, 1, 4, 1, 335, 1, 4, 20, 3, 10, 1, 24), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mcmMLMINetlinkStatLnkupCnt.setStatus('mandatory')
mcmMLMINetlinkStatLnkDownCnt = MibTableColumn((1, 3, 6, 1, 4, 1, 335, 1, 4, 20, 3, 10, 1, 25), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mcmMLMINetlinkStatLnkDownCnt.setStatus('mandatory')
mcmMLMICircuitStatTable = MibTable((1, 3, 6, 1, 4, 1, 335, 1, 4, 20, 3, 11), )
if mibBuilder.loadTexts: mcmMLMICircuitStatTable.setStatus('mandatory')
mcmMLMICircuitStatEntry = MibTableRow((1, 3, 6, 1, 4, 1, 335, 1, 4, 20, 3, 11, 1), ).setIndexNames((0, "MICOM-MPANL-LMI-MIB", "mcmMLMICircuitStatIfIndex"), (0, "MICOM-MPANL-LMI-MIB", "mcmMLMICircuitStatSVCDLCI"))
if mibBuilder.loadTexts: mcmMLMICircuitStatEntry.setStatus('mandatory')
mcmMLMICircuitStatIfIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 335, 1, 4, 20, 3, 11, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 255))).setMaxAccess("readonly")
if mibBuilder.loadTexts: mcmMLMICircuitStatIfIndex.setStatus('mandatory')
mcmMLMICircuitStatSVCDLCI = MibTableColumn((1, 3, 6, 1, 4, 1, 335, 1, 4, 20, 3, 11, 1, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(17, 991))).setMaxAccess("readonly")
if mibBuilder.loadTexts: mcmMLMICircuitStatSVCDLCI.setStatus('mandatory')
mcmMLMICircuitStatMsgRxStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 335, 1, 4, 20, 3, 11, 1, 3), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mcmMLMICircuitStatMsgRxStatus.setStatus('mandatory')
mcmMLMICircuitStatMsgTxStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 335, 1, 4, 20, 3, 11, 1, 4), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mcmMLMICircuitStatMsgTxStatus.setStatus('mandatory')
mcmMLMICircuitStatMsgRxStatusInq = MibTableColumn((1, 3, 6, 1, 4, 1, 335, 1, 4, 20, 3, 11, 1, 5), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mcmMLMICircuitStatMsgRxStatusInq.setStatus('mandatory')
mcmMLMICircuitStatMsgTxStatusInq = MibTableColumn((1, 3, 6, 1, 4, 1, 335, 1, 4, 20, 3, 11, 1, 6), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mcmMLMICircuitStatMsgTxStatusInq.setStatus('mandatory')
mcmMLMINetlinkStatusTable = MibTable((1, 3, 6, 1, 4, 1, 335, 1, 4, 20, 4, 1), )
if mibBuilder.loadTexts: mcmMLMINetlinkStatusTable.setStatus('mandatory')
mcmMLMINetlinkStatusEntry = MibTableRow((1, 3, 6, 1, 4, 1, 335, 1, 4, 20, 4, 1, 1), ).setIndexNames((0, "MICOM-MPANL-LMI-MIB", "mcmMLMINetlinkStatusIfIndex"))
if mibBuilder.loadTexts: mcmMLMINetlinkStatusEntry.setStatus('mandatory')
mcmMLMINetlinkStatusIfIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 335, 1, 4, 20, 4, 1, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 255))).setMaxAccess("readonly")
if mibBuilder.loadTexts: mcmMLMINetlinkStatusIfIndex.setStatus('mandatory')
mcmMLMINetlinkStatusMPANLStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 335, 1, 4, 20, 4, 1, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("up", 1), ("down", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: mcmMLMINetlinkStatusMPANLStatus.setStatus('mandatory')
mcmMLMINetlinkStatusRestartState = MibTableColumn((1, 3, 6, 1, 4, 1, 335, 1, 4, 20, 4, 1, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("none", 1), ("rstrtRqstSent", 2), ("rstrtRqstReceived", 3)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: mcmMLMINetlinkStatusRestartState.setStatus('mandatory')
mcmMLMINetlinkStatusLAPFState = MibTableColumn((1, 3, 6, 1, 4, 1, 335, 1, 4, 20, 4, 1, 1, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("up", 1), ("down", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: mcmMLMINetlinkStatusLAPFState.setStatus('mandatory')
mcmMLMINetlinkStatusFrCoreState = MibTableColumn((1, 3, 6, 1, 4, 1, 335, 1, 4, 20, 4, 1, 1, 5), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("up", 1), ("down", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: mcmMLMINetlinkStatusFrCoreState.setStatus('mandatory')
mcmMLMINetlinkStatusTxThrput = MibTableColumn((1, 3, 6, 1, 4, 1, 335, 1, 4, 20, 4, 1, 1, 6), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 2560000))).setMaxAccess("readonly")
if mibBuilder.loadTexts: mcmMLMINetlinkStatusTxThrput.setStatus('obsolete')
mcmMLMINetlinkStatusRxThrput = MibTableColumn((1, 3, 6, 1, 4, 1, 335, 1, 4, 20, 4, 1, 1, 7), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 2560000))).setMaxAccess("readonly")
if mibBuilder.loadTexts: mcmMLMINetlinkStatusRxThrput.setStatus('obsolete')
mcmMLMICircuitStatusTable = MibTable((1, 3, 6, 1, 4, 1, 335, 1, 4, 20, 4, 2), )
if mibBuilder.loadTexts: mcmMLMICircuitStatusTable.setStatus('mandatory')
mcmMLMICircuitStatusEntry = MibTableRow((1, 3, 6, 1, 4, 1, 335, 1, 4, 20, 4, 2, 1), ).setIndexNames((0, "MICOM-MPANL-LMI-MIB", "mcmMLMICircuitStatusIfIndex"), (0, "MICOM-MPANL-LMI-MIB", "mcmMLMICircuitStatusSVCDLCI"))
if mibBuilder.loadTexts: mcmMLMICircuitStatusEntry.setStatus('mandatory')
mcmMLMICircuitStatusIfIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 335, 1, 4, 20, 4, 2, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 255))).setMaxAccess("readonly")
if mibBuilder.loadTexts: mcmMLMICircuitStatusIfIndex.setStatus('mandatory')
mcmMLMICircuitStatusSVCDLCI = MibTableColumn((1, 3, 6, 1, 4, 1, 335, 1, 4, 20, 4, 2, 1, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(17, 991))).setMaxAccess("readonly")
if mibBuilder.loadTexts: mcmMLMICircuitStatusSVCDLCI.setStatus('mandatory')
mcmMLMICircStatusRejectCause = MibTableColumn((1, 3, 6, 1, 4, 1, 335, 1, 4, 20, 4, 2, 1, 3), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 512))).setMaxAccess("readonly")
if mibBuilder.loadTexts: mcmMLMICircStatusRejectCause.setStatus('mandatory')
mcmMLMICircStatusSVCType = MibTableColumn((1, 3, 6, 1, 4, 1, 335, 1, 4, 20, 4, 2, 1, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5))).clone(namedValues=NamedValues(("rfc1490", 1), ("voice", 2), ("switched", 3), ("rfc1490switched", 4), ("rsi", 5)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: mcmMLMICircStatusSVCType.setStatus('mandatory')
mcmMLMICircStatusAttriSetupPriority = MibTableColumn((1, 3, 6, 1, 4, 1, 335, 1, 4, 20, 4, 2, 1, 5), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5))).clone(namedValues=NamedValues(("onePriority", 1), ("twoPriority", 2), ("threePriority", 3), ("fourPriority", 4), ("fivePriority", 5)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: mcmMLMICircStatusAttriSetupPriority.setStatus('mandatory')
mcmMLMICircStatusAttriHoldPriority = MibTableColumn((1, 3, 6, 1, 4, 1, 335, 1, 4, 20, 4, 2, 1, 6), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5))).clone(namedValues=NamedValues(("onePriority", 1), ("twoPriority", 2), ("threePriority", 3), ("fourPriority", 4), ("fivePriority", 5)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: mcmMLMICircStatusAttriHoldPriority.setStatus('mandatory')
mcmMLMICircStatusAttriDiscardPriority = MibTableColumn((1, 3, 6, 1, 4, 1, 335, 1, 4, 20, 4, 2, 1, 7), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5))).clone(namedValues=NamedValues(("onePriority", 1), ("twoPriority", 2), ("threePriority", 3), ("fourPriority", 4), ("fivePriority", 5)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: mcmMLMICircStatusAttriDiscardPriority.setStatus('mandatory')
mcmMLMICircStatusClaimedBandWidth = MibTableColumn((1, 3, 6, 1, 4, 1, 335, 1, 4, 20, 4, 2, 1, 8), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 2560000))).setMaxAccess("readonly")
if mibBuilder.loadTexts: mcmMLMICircStatusClaimedBandWidth.setStatus('mandatory')
mcmMLMICircStatusQoSTxThrput = MibTableColumn((1, 3, 6, 1, 4, 1, 335, 1, 4, 20, 4, 2, 1, 9), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 2560000))).setMaxAccess("readonly")
if mibBuilder.loadTexts: mcmMLMICircStatusQoSTxThrput.setStatus('mandatory')
mcmMLMICircStatusQoSRxThrput = MibTableColumn((1, 3, 6, 1, 4, 1, 335, 1, 4, 20, 4, 2, 1, 10), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 2560000))).setMaxAccess("readonly")
if mibBuilder.loadTexts: mcmMLMICircStatusQoSRxThrput.setStatus('mandatory')
mcmMLMICircStatusQoSTxBrstSizGrntd = MibTableColumn((1, 3, 6, 1, 4, 1, 335, 1, 4, 20, 4, 2, 1, 11), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 2560000))).setMaxAccess("readonly")
if mibBuilder.loadTexts: mcmMLMICircStatusQoSTxBrstSizGrntd.setStatus('mandatory')
mcmMLMICircStatusQoSRxBrstSizGrntd = MibTableColumn((1, 3, 6, 1, 4, 1, 335, 1, 4, 20, 4, 2, 1, 12), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 2560000))).setMaxAccess("readonly")
if mibBuilder.loadTexts: mcmMLMICircStatusQoSRxBrstSizGrntd.setStatus('mandatory')
mcmMLMICircStatusQoSTxExRateGrntd = MibTableColumn((1, 3, 6, 1, 4, 1, 335, 1, 4, 20, 4, 2, 1, 13), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 2560000))).setMaxAccess("readonly")
if mibBuilder.loadTexts: mcmMLMICircStatusQoSTxExRateGrntd.setStatus('mandatory')
mcmMLMICircStatusQoSRxExRateGrntd = MibTableColumn((1, 3, 6, 1, 4, 1, 335, 1, 4, 20, 4, 2, 1, 14), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 2560000))).setMaxAccess("readonly")
if mibBuilder.loadTexts: mcmMLMICircStatusQoSRxExRateGrntd.setStatus('mandatory')
mcmMLMICircStatusPeerDLCI = MibTableColumn((1, 3, 6, 1, 4, 1, 335, 1, 4, 20, 4, 2, 1, 15), Integer32().subtype(subtypeSpec=ValueRangeConstraint(16, 991))).setMaxAccess("readonly")
if mibBuilder.loadTexts: mcmMLMICircStatusPeerDLCI.setStatus('mandatory')
mcmMLMICircStatusPeerNetwork = MibTableColumn((1, 3, 6, 1, 4, 1, 335, 1, 4, 20, 4, 2, 1, 16), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 64))).setMaxAccess("readonly")
if mibBuilder.loadTexts: mcmMLMICircStatusPeerNetwork.setStatus('mandatory')
mcmMLMICircStatusCallingDNA = MibTableColumn((1, 3, 6, 1, 4, 1, 335, 1, 4, 20, 4, 2, 1, 17), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(1, 34))).setMaxAccess("readonly")
if mibBuilder.loadTexts: mcmMLMICircStatusCallingDNA.setStatus('mandatory')
mcmMLMICircStatusCalledDNA = MibTableColumn((1, 3, 6, 1, 4, 1, 335, 1, 4, 20, 4, 2, 1, 18), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(1, 34))).setMaxAccess("readonly")
if mibBuilder.loadTexts: mcmMLMICircStatusCalledDNA.setStatus('mandatory')
mcmMLMICntrAction = MibScalar((1, 3, 6, 1, 4, 1, 335, 1, 4, 20, 2, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1))).clone(namedValues=NamedValues(("reset", 1)))).setMaxAccess("writeonly")
if mibBuilder.loadTexts: mcmMLMICntrAction.setStatus('obsolete')
mcmLMISVCCallRejected = NotificationType((1, 3, 6, 1, 4, 1, 335, 1, 4, 20) + (0,1)).setObjects(("MICOM-SYS-MIB", "mcmSysAsciiTimeOfDay"), ("MICOM-MPANL-LMI-MIB", "mcmMLMINetlinkIfIndex"))
mcmLMIIncompatibleType = NotificationType((1, 3, 6, 1, 4, 1, 335, 1, 4, 20) + (0,2)).setObjects(("MICOM-SYS-MIB", "mcmSysAsciiTimeOfDay"), ("MICOM-MPANL-LMI-MIB", "mcmMLMINetlinkIfIndex"))
mcmLMIT317TimerExpired = NotificationType((1, 3, 6, 1, 4, 1, 335, 1, 4, 20) + (0,3)).setObjects(("MICOM-SYS-MIB", "mcmSysAsciiTimeOfDay"), ("MICOM-MPANL-LMI-MIB", "mcmMLMINetlinkIfIndex"))
mcmMLMIReachedMaxUnsucessfulRestartAttemps = NotificationType((1, 3, 6, 1, 4, 1, 335, 1, 4, 20) + (0,4)).setObjects(("MICOM-SYS-MIB", "mcmSysAsciiTimeOfDay"), ("MICOM-MPANL-LMI-MIB", "mcmMLMINetlinkIfIndex"))
mibBuilder.exportSymbols("MICOM-MPANL-LMI-MIB", mcmMLMINetlinkStatMsgRxSetup=mcmMLMINetlinkStatMsgRxSetup, mcmMLMICircStatusQoSTxExRateGrntd=mcmMLMICircStatusQoSTxExRateGrntd, nvmMLMINetlinkRstrtT316Timer=nvmMLMINetlinkRstrtT316Timer, mcmMLMINetlinkStatMsgRxStatusInq=mcmMLMINetlinkStatMsgRxStatusInq, mlmi_status=mlmi_status, mcmMLMICircStatusPeerNetwork=mcmMLMICircStatusPeerNetwork, mcmMLMICircuitStatusIfIndex=mcmMLMICircuitStatusIfIndex, mcmMLMINetlinkStatSpvcCalls=mcmMLMINetlinkStatSpvcCalls, nvmMLMIServiceCUGAccess=nvmMLMIServiceCUGAccess, nvmMLMIServiceCUGIC=nvmMLMIServiceCUGIC, nvmMLMINetlinkDLCIAssignMethod=nvmMLMINetlinkDLCIAssignMethod, mcmMLMIServiceCUGAccess=mcmMLMIServiceCUGAccess, mcmMLMICircuitStatIfIndex=mcmMLMICircuitStatIfIndex, mcmMLMINetlinkStatLnkDownCnt=mcmMLMINetlinkStatLnkDownCnt, nvmMLMINetlinkNumUnsuccesRstrtAtmpts=nvmMLMINetlinkNumUnsuccesRstrtAtmpts, mcmMLMICircStatusCalledDNA=mcmMLMICircStatusCalledDNA, mcmMLMINetlinkStatMsgTxStatusInq=mcmMLMINetlinkStatMsgTxStatusInq, mcmMLMIStatsRejectedCUGs=mcmMLMIStatsRejectedCUGs, micom_mlmi=micom_mlmi, mcmMLMINetlinkTable=mcmMLMINetlinkTable, mlmi_statistics=mlmi_statistics, mcmMLMINetlinkStatMsgTxCallPrcdngs=mcmMLMINetlinkStatMsgTxCallPrcdngs, mcmMLMICircStatusPeerDLCI=mcmMLMICircStatusPeerDLCI, mcmMLMINetlinkEntry=mcmMLMINetlinkEntry, mcmMLMIServiceCUGIC=mcmMLMIServiceCUGIC, nvmMLMIGenCfg4400Type=nvmMLMIGenCfg4400Type, mcmMLMICircStatusRejectCause=mcmMLMICircStatusRejectCause, mcmMLMINetlinkDLCIAssignMethod=mcmMLMINetlinkDLCIAssignMethod, mcmMLMIStatsAdmittedCUGs=mcmMLMIStatsAdmittedCUGs, mcmMLMINetlinkStatMsgRxRlseComp=mcmMLMINetlinkStatMsgRxRlseComp, mcmMLMICircuitStatusTable=mcmMLMICircuitStatusTable, mcmMLMICircuitStatMsgTxStatus=mcmMLMICircuitStatMsgTxStatus, mcmMLMIGenCfgSoftwareRev=mcmMLMIGenCfgSoftwareRev, nvmMLMINetlinkRstrtAckT317Timer=nvmMLMINetlinkRstrtAckT317Timer, mcmMLMINetlinkStatusLAPFState=mcmMLMINetlinkStatusLAPFState, mcmMLMIServiceIfIndex=mcmMLMIServiceIfIndex, mcmMLMICircStatusQoSRxThrput=mcmMLMICircStatusQoSRxThrput, mcmMLMINetlinkStatLocalSVC=mcmMLMINetlinkStatLocalSVC, mcmMLMINetlinkTunnelingPVCDlci=mcmMLMINetlinkTunnelingPVCDlci, mcmMLMINetlinkStatMsgRxDisConn=mcmMLMINetlinkStatMsgRxDisConn, mcmMLMICircStatusQoSTxBrstSizGrntd=mcmMLMICircStatusQoSTxBrstSizGrntd, nvmMLMIServiceCUGICType=nvmMLMIServiceCUGICType, mcmMLMIStatsSucceededCalls=mcmMLMIStatsSucceededCalls, mcmMLMINetlinkStatusFrCoreState=mcmMLMINetlinkStatusFrCoreState, mcmMLMICircStatusQoSRxExRateGrntd=mcmMLMICircStatusQoSRxExRateGrntd, nvmMLMIServiceEntry=nvmMLMIServiceEntry, mcmMLMINetlinkStatusRestartState=mcmMLMINetlinkStatusRestartState, mcmMLMICircStatusClaimedBandWidth=mcmMLMICircStatusClaimedBandWidth, mcmMLMINetlinkStatLnkupCnt=mcmMLMINetlinkStatLnkupCnt, mcmMLMIServiceCUGFacility=mcmMLMIServiceCUGFacility, mcmMLMINetlinkStatRsiCalls=mcmMLMINetlinkStatRsiCalls, mcmMLMINetlinkStatMsgTxConn=mcmMLMINetlinkStatMsgTxConn, mcmMLMINetlinkStatMsgTxRlseComp=mcmMLMINetlinkStatMsgTxRlseComp, mcmMLMINetlinkStatMsgRxStatus=mcmMLMINetlinkStatMsgRxStatus, mcmMLMICircuitStatSVCDLCI=mcmMLMICircuitStatSVCDLCI, mcmMLMINetlinkStatMsgTxDisConn=mcmMLMINetlinkStatMsgTxDisConn, mcmMLMINetlinkStatMsgTxRls=mcmMLMINetlinkStatMsgTxRls, mcmMLMICircStatusQoSTxThrput=mcmMLMICircStatusQoSTxThrput, mcmMLMINetlinkStatMsgRxCallPrcdngs=mcmMLMINetlinkStatMsgRxCallPrcdngs, mcmMLMINetlinkStatMsgRxRls=mcmMLMINetlinkStatMsgRxRls, mcmMLMINetlinkIfIndex=mcmMLMINetlinkIfIndex, mcmMLMINetlinkRstrtT316Timer=mcmMLMINetlinkRstrtT316Timer, mcmMLMIStatsFailedCalls=mcmMLMIStatsFailedCalls, mcmMLMIStatsRequestedCalls=mcmMLMIStatsRequestedCalls, mcmMLMICircuitStatusEntry=mcmMLMICircuitStatusEntry, mcmMLMINetlinkStatEntry=mcmMLMINetlinkStatEntry, mcmMLMIGenCfg4400Type=mcmMLMIGenCfg4400Type, mcmMLMICircuitStatMsgRxStatus=mcmMLMICircuitStatMsgRxStatus, mcmMLMICircStatusSVCType=mcmMLMICircStatusSVCType, mcmMLMICircStatusAttriSetupPriority=mcmMLMICircStatusAttriSetupPriority, nvmMLMINetlinkIfIndex=nvmMLMINetlinkIfIndex, mcmMLMICircStatusAttriHoldPriority=mcmMLMICircStatusAttriHoldPriority, mcmMLMICircStatusQoSRxBrstSizGrntd=mcmMLMICircStatusQoSRxBrstSizGrntd, mcmMLMICircuitStatTable=mcmMLMICircuitStatTable, mcmMLMICircuitStatEntry=mcmMLMICircuitStatEntry, nvmMLMIServiceDNASuffix=nvmMLMIServiceDNASuffix, mcmMLMINetlinkRstrtAckT317Timer=mcmMLMINetlinkRstrtAckT317Timer, mcmMLMINetlinkStatusMPANLStatus=mcmMLMINetlinkStatusMPANLStatus, mcmMLMICircuitStatMsgRxStatusInq=mcmMLMICircuitStatMsgRxStatusInq, mcmMLMIServiceTable=mcmMLMIServiceTable, mcmMLMINetlinkStatusTxThrput=mcmMLMINetlinkStatusTxThrput, nvmMLMIServiceCUGFacility=nvmMLMIServiceCUGFacility, mcmMLMICntrAction=mcmMLMICntrAction, mcmMLMIServiceDNASuffix=mcmMLMIServiceDNASuffix, mcmMLMINetlinkStatusTable=mcmMLMINetlinkStatusTable, mcmMLMINetlinkStatusRxThrput=mcmMLMINetlinkStatusRxThrput, mcmMLMINetlinkStatMsgRxConn=mcmMLMINetlinkStatMsgRxConn, nvmMLMIServiceIfIndex=nvmMLMIServiceIfIndex, mcmLMIIncompatibleType=mcmLMIIncompatibleType, mcmMLMIServiceCUGICType=mcmMLMIServiceCUGICType, mcmMLMINetlinkMpanlMode=mcmMLMINetlinkMpanlMode, mcmMLMINetlinkStatVoiceCalls=mcmMLMINetlinkStatVoiceCalls, nvmMLMINetlinkTable=nvmMLMINetlinkTable, nvmMLMINetlinkTunnelingPVCDlci=nvmMLMINetlinkTunnelingPVCDlci, mcmMLMINetlinkStatIfIndex=mcmMLMINetlinkStatIfIndex, mcmMLMIServiceEntry=mcmMLMIServiceEntry, mcmMLMINetlinkStatMsgTxSetup=mcmMLMINetlinkStatMsgTxSetup, mcmMLMICircuitStatusSVCDLCI=mcmMLMICircuitStatusSVCDLCI, mcmMLMINetlinkStatusEntry=mcmMLMINetlinkStatusEntry, nvmMLMIServiceTable=nvmMLMIServiceTable, mcmMLMIStatsReleasedCalls=mcmMLMIStatsReleasedCalls, mcmMLMIStatsInitiatedCalls=mcmMLMIStatsInitiatedCalls, nvmMLMINetlinkEntry=nvmMLMINetlinkEntry, mcmLMIT317TimerExpired=mcmLMIT317TimerExpired, mcmMLMINetlinkNumUnsuccesRstrtAtmpts=mcmMLMINetlinkNumUnsuccesRstrtAtmpts, mlmi_control=mlmi_control, mcmMLMINetlinkStatMsgTxStatus=mcmMLMINetlinkStatMsgTxStatus, mcmMLMICircStatusCallingDNA=mcmMLMICircStatusCallingDNA, mcmMLMIReachedMaxUnsucessfulRestartAttemps=mcmMLMIReachedMaxUnsucessfulRestartAttemps, mcmMLMINetlinkStatTransitSVC=mcmMLMINetlinkStatTransitSVC, mcmLMISVCCallRejected=mcmLMISVCCallRejected, mcmMLMINetlinkStatTable=mcmMLMINetlinkStatTable, mcmMLMINetlinkStatusIfIndex=mcmMLMINetlinkStatusIfIndex, mcmMLMINetlinkStatLanCalls=mcmMLMINetlinkStatLanCalls, nvmMLMIServiceRowStatus=nvmMLMIServiceRowStatus, mcmMLMICircuitStatMsgTxStatusInq=mcmMLMICircuitStatMsgTxStatusInq, mcmMLMIStatsActiveVCs=mcmMLMIStatsActiveVCs, mcmMLMICircStatusAttriDiscardPriority=mcmMLMICircStatusAttriDiscardPriority, mlmi_configuration=mlmi_configuration, mcmMLMIStatsDisconnectedCalls=mcmMLMIStatsDisconnectedCalls)
