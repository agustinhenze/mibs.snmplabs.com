#
# PySNMP MIB module Wellfleet-LOADER-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/Wellfleet-LOADER-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 21:34:12 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
Integer, OctetString, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "Integer", "OctetString", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
SingleValueConstraint, ConstraintsIntersection, ValueRangeConstraint, ValueSizeConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "SingleValueConstraint", "ConstraintsIntersection", "ValueRangeConstraint", "ValueSizeConstraint", "ConstraintsUnion")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
MibScalar, MibTable, MibTableRow, MibTableColumn, Counter32, ModuleIdentity, NotificationType, Counter64, IpAddress, Gauge32, TimeTicks, Integer32, Bits, Unsigned32, MibIdentifier, ObjectIdentity, iso = mibBuilder.importSymbols("SNMPv2-SMI", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter32", "ModuleIdentity", "NotificationType", "Counter64", "IpAddress", "Gauge32", "TimeTicks", "Integer32", "Bits", "Unsigned32", "MibIdentifier", "ObjectIdentity", "iso")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
wfSoftwareConfig, = mibBuilder.importSymbols("Wellfleet-COMMON-MIB", "wfSoftwareConfig")
wfProtocols = MibIdentifier((1, 3, 6, 1, 4, 1, 18, 3, 2, 1))
wfIPROTOLoad = MibScalar((1, 3, 6, 1, 4, 1, 18, 3, 2, 1, 1), Counter32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: wfIPROTOLoad.setStatus('mandatory')
wfDECNETLoad = MibScalar((1, 3, 6, 1, 4, 1, 18, 3, 2, 1, 2), Counter32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: wfDECNETLoad.setStatus('mandatory')
wfATLoad = MibScalar((1, 3, 6, 1, 4, 1, 18, 3, 2, 1, 3), Counter32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: wfATLoad.setStatus('mandatory')
wfXNSLoad = MibScalar((1, 3, 6, 1, 4, 1, 18, 3, 2, 1, 4), Counter32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: wfXNSLoad.setStatus('mandatory')
wfIPXLoad = MibScalar((1, 3, 6, 1, 4, 1, 18, 3, 2, 1, 5), Counter32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: wfIPXLoad.setStatus('mandatory')
wfOSILoad = MibScalar((1, 3, 6, 1, 4, 1, 18, 3, 2, 1, 6), Counter32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: wfOSILoad.setStatus('mandatory')
wfX25DTELoad = MibScalar((1, 3, 6, 1, 4, 1, 18, 3, 2, 1, 7), Counter32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: wfX25DTELoad.setStatus('mandatory')
wfX25DCELoad = MibScalar((1, 3, 6, 1, 4, 1, 18, 3, 2, 1, 8), Counter32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: wfX25DCELoad.setStatus('mandatory')
wfVINESLoad = MibScalar((1, 3, 6, 1, 4, 1, 18, 3, 2, 1, 9), Counter32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: wfVINESLoad.setStatus('mandatory')
wfFRLoad = MibScalar((1, 3, 6, 1, 4, 1, 18, 3, 2, 1, 10), Counter32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: wfFRLoad.setStatus('mandatory')
wfRARPLoad = MibScalar((1, 3, 6, 1, 4, 1, 18, 3, 2, 1, 11), Counter32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: wfRARPLoad.setStatus('mandatory')
wfATMLoad = MibScalar((1, 3, 6, 1, 4, 1, 18, 3, 2, 1, 12), Counter32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: wfATMLoad.setStatus('mandatory')
wfDLSLoad = MibScalar((1, 3, 6, 1, 4, 1, 18, 3, 2, 1, 13), Counter32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: wfDLSLoad.setStatus('mandatory')
wfLNMLoad = MibScalar((1, 3, 6, 1, 4, 1, 18, 3, 2, 1, 14), Counter32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: wfLNMLoad.setStatus('mandatory')
wfTelnetLoad = MibScalar((1, 3, 6, 1, 4, 1, 18, 3, 2, 1, 15), Counter32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: wfTelnetLoad.setStatus('mandatory')
wfTFTPLoad = MibScalar((1, 3, 6, 1, 4, 1, 18, 3, 2, 1, 16), Counter32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: wfTFTPLoad.setStatus('mandatory')
wfSNMPLoad = MibScalar((1, 3, 6, 1, 4, 1, 18, 3, 2, 1, 17), Counter32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: wfSNMPLoad.setStatus('mandatory')
wfTCPLoad = MibScalar((1, 3, 6, 1, 4, 1, 18, 3, 2, 1, 18), Counter32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: wfTCPLoad.setStatus('mandatory')
wfBGPLoad = MibScalar((1, 3, 6, 1, 4, 1, 18, 3, 2, 1, 19), Counter32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: wfBGPLoad.setStatus('mandatory')
wfEGPLoad = MibScalar((1, 3, 6, 1, 4, 1, 18, 3, 2, 1, 20), Counter32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: wfEGPLoad.setStatus('mandatory')
wfOSPFLoad = MibScalar((1, 3, 6, 1, 4, 1, 18, 3, 2, 1, 21), Counter32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: wfOSPFLoad.setStatus('mandatory')
wfWPROXYLoad = MibScalar((1, 3, 6, 1, 4, 1, 18, 3, 2, 1, 22), Counter32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: wfWPROXYLoad.setStatus('mandatory')
wfLLC2Load = MibScalar((1, 3, 6, 1, 4, 1, 18, 3, 2, 1, 23), Counter32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: wfLLC2Load.setStatus('mandatory')
wfSMDSLoad = MibScalar((1, 3, 6, 1, 4, 1, 18, 3, 2, 1, 24), Counter32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: wfSMDSLoad.setStatus('mandatory')
wfPPPLoad = MibScalar((1, 3, 6, 1, 4, 1, 18, 3, 2, 1, 25), Counter32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: wfPPPLoad.setStatus('mandatory')
wfPktCaptureLoad = MibScalar((1, 3, 6, 1, 4, 1, 18, 3, 2, 1, 26), Counter32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: wfPktCaptureLoad.setStatus('mandatory')
wfFRSWCNGCLoad = MibScalar((1, 3, 6, 1, 4, 1, 18, 3, 2, 1, 27), Counter32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: wfFRSWCNGCLoad.setStatus('mandatory')
wfSWPROXYLoad = MibScalar((1, 3, 6, 1, 4, 1, 18, 3, 2, 1, 28), Counter32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: wfSWPROXYLoad.setStatus('mandatory')
wfFRSWLoad = MibScalar((1, 3, 6, 1, 4, 1, 18, 3, 2, 1, 29), Counter32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: wfFRSWLoad.setStatus('mandatory')
wfSWSMDSLoad = MibScalar((1, 3, 6, 1, 4, 1, 18, 3, 2, 1, 30), Counter32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: wfSWSMDSLoad.setStatus('mandatory')
wfNBASELoad = MibScalar((1, 3, 6, 1, 4, 1, 18, 3, 2, 1, 31), Counter32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: wfNBASELoad.setStatus('mandatory')
wfSDLCLoad = MibScalar((1, 3, 6, 1, 4, 1, 18, 3, 2, 1, 32), Counter32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: wfSDLCLoad.setStatus('mandatory')
wfTNCLoad = MibScalar((1, 3, 6, 1, 4, 1, 18, 3, 2, 1, 33), Counter32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: wfTNCLoad.setStatus('mandatory')
wfLAPBLoad = MibScalar((1, 3, 6, 1, 4, 1, 18, 3, 2, 1, 34), Counter32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: wfLAPBLoad.setStatus('mandatory')
wfDebugLoad = MibScalar((1, 3, 6, 1, 4, 1, 18, 3, 2, 1, 35), Counter32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: wfDebugLoad.setStatus('mandatory')
wfNBIPLoad = MibScalar((1, 3, 6, 1, 4, 1, 18, 3, 2, 1, 36), Counter32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: wfNBIPLoad.setStatus('mandatory')
wfATMCsLoad = MibScalar((1, 3, 6, 1, 4, 1, 18, 3, 2, 1, 37), Counter32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: wfATMCsLoad.setStatus('mandatory')
wfDvmrpLoad = MibScalar((1, 3, 6, 1, 4, 1, 18, 3, 2, 1, 38), Counter32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: wfDvmrpLoad.setStatus('mandatory')
wfIgmpLoad = MibScalar((1, 3, 6, 1, 4, 1, 18, 3, 2, 1, 39), Counter32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: wfIgmpLoad.setStatus('mandatory')
wfISDNLoad = MibScalar((1, 3, 6, 1, 4, 1, 18, 3, 2, 1, 40), Counter32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: wfISDNLoad.setStatus('mandatory')
wfLMLoad = MibScalar((1, 3, 6, 1, 4, 1, 18, 3, 2, 1, 41), Counter32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: wfLMLoad.setStatus('mandatory')
wfPingLoad = MibScalar((1, 3, 6, 1, 4, 1, 18, 3, 2, 1, 42), Counter32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: wfPingLoad.setStatus('mandatory')
wfAPPNCpLoad = MibScalar((1, 3, 6, 1, 4, 1, 18, 3, 2, 1, 43), Counter32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: wfAPPNCpLoad.setStatus('mandatory')
wfAPPNLsLoad = MibScalar((1, 3, 6, 1, 4, 1, 18, 3, 2, 1, 44), Counter32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: wfAPPNLsLoad.setStatus('mandatory')
wfWcpLoad = MibScalar((1, 3, 6, 1, 4, 1, 18, 3, 2, 1, 45), Counter32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: wfWcpLoad.setStatus('mandatory')
wfFTPLoad = MibScalar((1, 3, 6, 1, 4, 1, 18, 3, 2, 1, 46), Counter32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: wfFTPLoad.setStatus('mandatory')
wfARPLoad = MibScalar((1, 3, 6, 1, 4, 1, 18, 3, 2, 1, 47), Counter32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: wfARPLoad.setStatus('mandatory')
wfSYSLLoad = MibScalar((1, 3, 6, 1, 4, 1, 18, 3, 2, 1, 48), Counter32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: wfSYSLLoad.setStatus('mandatory')
wfBGPRSLoad = MibScalar((1, 3, 6, 1, 4, 1, 18, 3, 2, 1, 49), Counter32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: wfBGPRSLoad.setStatus('mandatory')
wfATMLeLoad = MibScalar((1, 3, 6, 1, 4, 1, 18, 3, 2, 1, 50), Counter32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: wfATMLeLoad.setStatus('mandatory')
wfCRMLoad = MibScalar((1, 3, 6, 1, 4, 1, 18, 3, 2, 1, 51), Counter32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: wfCRMLoad.setStatus('mandatory')
wfIPEXLoad = MibScalar((1, 3, 6, 1, 4, 1, 18, 3, 2, 1, 52), Counter32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: wfIPEXLoad.setStatus('mandatory')
wfSt2Load = MibScalar((1, 3, 6, 1, 4, 1, 18, 3, 2, 1, 53), Counter32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: wfSt2Load.setStatus('mandatory')
wfNLSPLoad = MibScalar((1, 3, 6, 1, 4, 1, 18, 3, 2, 1, 54), Counter32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: wfNLSPLoad.setStatus('mandatory')
wfSTATSLoad = MibScalar((1, 3, 6, 1, 4, 1, 18, 3, 2, 1, 55), Counter32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: wfSTATSLoad.setStatus('mandatory')
wfNPTLoad = MibScalar((1, 3, 6, 1, 4, 1, 18, 3, 2, 1, 56), Counter32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: wfNPTLoad.setStatus('mandatory')
wfRREDUNDLoad = MibScalar((1, 3, 6, 1, 4, 1, 18, 3, 2, 1, 57), Counter32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: wfRREDUNDLoad.setStatus('mandatory')
wfATMSigLoad = MibScalar((1, 3, 6, 1, 4, 1, 18, 3, 2, 1, 58), Counter32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: wfATMSigLoad.setStatus('mandatory')
wfIPv6Load = MibScalar((1, 3, 6, 1, 4, 1, 18, 3, 2, 1, 59), Counter32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: wfIPv6Load.setStatus('mandatory')
wfBOTLoad = MibScalar((1, 3, 6, 1, 4, 1, 18, 3, 2, 1, 60), Counter32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: wfBOTLoad.setStatus('mandatory')
wfPimLoad = MibScalar((1, 3, 6, 1, 4, 1, 18, 3, 2, 1, 61), Counter32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: wfPimLoad.setStatus('mandatory')
wfLBCLoad = MibScalar((1, 3, 6, 1, 4, 1, 18, 3, 2, 1, 62), Counter32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: wfLBCLoad.setStatus('mandatory')
wfATMMcsLoad = MibScalar((1, 3, 6, 1, 4, 1, 18, 3, 2, 1, 63), Counter32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: wfATMMcsLoad.setStatus('mandatory')
wfATMAsmLoad = MibScalar((1, 3, 6, 1, 4, 1, 18, 3, 2, 1, 64), Counter32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: wfATMAsmLoad.setStatus('mandatory')
wfCPMLoad = MibScalar((1, 3, 6, 1, 4, 1, 18, 3, 2, 1, 65), Counter32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: wfCPMLoad.setStatus('mandatory')
wfBAYSIGLoad = MibScalar((1, 3, 6, 1, 4, 1, 18, 3, 2, 1, 66), Counter32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: wfBAYSIGLoad.setStatus('mandatory')
wfScmIpcLoad = MibScalar((1, 3, 6, 1, 4, 1, 18, 3, 2, 1, 67), Counter32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: wfScmIpcLoad.setStatus('mandatory')
wfNTPLoad = MibScalar((1, 3, 6, 1, 4, 1, 18, 3, 2, 1, 68), Counter32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: wfNTPLoad.setStatus('mandatory')
wfRADIUSLoad = MibScalar((1, 3, 6, 1, 4, 1, 18, 3, 2, 1, 69), Counter32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: wfRADIUSLoad.setStatus('mandatory')
wfRCMDSLoad = MibScalar((1, 3, 6, 1, 4, 1, 18, 3, 2, 1, 70), Counter32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: wfRCMDSLoad.setStatus('mandatory')
wfDNSLoad = MibScalar((1, 3, 6, 1, 4, 1, 18, 3, 2, 1, 71), Counter32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: wfDNSLoad.setStatus('mandatory')
wfWepLoad = MibScalar((1, 3, 6, 1, 4, 1, 18, 3, 2, 1, 72), Counter32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: wfWepLoad.setStatus('mandatory')
wfRipv6Load = MibScalar((1, 3, 6, 1, 4, 1, 18, 3, 2, 1, 73), Counter32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: wfRipv6Load.setStatus('mandatory')
wfMOSPFLoad = MibScalar((1, 3, 6, 1, 4, 1, 18, 3, 2, 1, 74), Counter32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: wfMOSPFLoad.setStatus('mandatory')
wfRSVPLoad = MibScalar((1, 3, 6, 1, 4, 1, 18, 3, 2, 1, 75), Counter32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: wfRSVPLoad.setStatus('mandatory')
wfIpSwitchLoad = MibScalar((1, 3, 6, 1, 4, 1, 18, 3, 2, 1, 76), Counter32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: wfIpSwitchLoad.setStatus('mandatory')
wfPortMtxLoad = MibScalar((1, 3, 6, 1, 4, 1, 18, 3, 2, 1, 77), Counter32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: wfPortMtxLoad.setStatus('mandatory')
wfConvStrLoad = MibScalar((1, 3, 6, 1, 4, 1, 18, 3, 2, 1, 78), Counter32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: wfConvStrLoad.setStatus('mandatory')
wfS5ChasLoad = MibScalar((1, 3, 6, 1, 4, 1, 18, 3, 2, 1, 79), Counter32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: wfS5ChasLoad.setStatus('mandatory')
wfFRSVCLoad = MibScalar((1, 3, 6, 1, 4, 1, 18, 3, 2, 1, 80), Counter32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: wfFRSVCLoad.setStatus('mandatory')
wfAOTLoad = MibScalar((1, 3, 6, 1, 4, 1, 18, 3, 2, 1, 81), Counter32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: wfAOTLoad.setStatus('mandatory')
wfNATLoad = MibScalar((1, 3, 6, 1, 4, 1, 18, 3, 2, 1, 82), Counter32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: wfNATLoad.setStatus('mandatory')
wfFRPTLoad = MibScalar((1, 3, 6, 1, 4, 1, 18, 3, 2, 1, 83), Counter32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: wfFRPTLoad.setStatus('mandatory')
wfHttpSrvLoad = MibScalar((1, 3, 6, 1, 4, 1, 18, 3, 2, 1, 84), Counter32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: wfHttpSrvLoad.setStatus('mandatory')
wfStacLZSLoad = MibScalar((1, 3, 6, 1, 4, 1, 18, 3, 2, 1, 85), Counter32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: wfStacLZSLoad.setStatus('mandatory')
wfASRLoad = MibScalar((1, 3, 6, 1, 4, 1, 18, 3, 2, 1, 86), Counter32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: wfASRLoad.setStatus('mandatory')
wfNHRPLoad = MibScalar((1, 3, 6, 1, 4, 1, 18, 3, 2, 1, 87), Counter32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: wfNHRPLoad.setStatus('mandatory')
wfAHBLoad = MibScalar((1, 3, 6, 1, 4, 1, 18, 3, 2, 1, 88), Counter32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: wfAHBLoad.setStatus('mandatory')
wfL2TPLoad = MibScalar((1, 3, 6, 1, 4, 1, 18, 3, 2, 1, 89), Counter32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: wfL2TPLoad.setStatus('mandatory')
wfISDBLoad = MibScalar((1, 3, 6, 1, 4, 1, 18, 3, 2, 1, 90), Counter32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: wfISDBLoad.setStatus('mandatory')
wfVCCTLoad = MibScalar((1, 3, 6, 1, 4, 1, 18, 3, 2, 1, 91), Counter32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: wfVCCTLoad.setStatus('mandatory')
wfMpsLoad = MibScalar((1, 3, 6, 1, 4, 1, 18, 3, 2, 1, 92), Counter32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: wfMpsLoad.setStatus('mandatory')
wfTAG1QLoad = MibScalar((1, 3, 6, 1, 4, 1, 18, 3, 2, 1, 93), Counter32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: wfTAG1QLoad.setStatus('mandatory')
wfMpcLoad = MibScalar((1, 3, 6, 1, 4, 1, 18, 3, 2, 1, 94), Counter32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: wfMpcLoad.setStatus('mandatory')
wfDVSLoad = MibScalar((1, 3, 6, 1, 4, 1, 18, 3, 2, 1, 95), Counter32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: wfDVSLoad.setStatus('mandatory')
wfVRRPLoad = MibScalar((1, 3, 6, 1, 4, 1, 18, 3, 2, 1, 96), Counter32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: wfVRRPLoad.setStatus('mandatory')
wfDHCPLoad = MibScalar((1, 3, 6, 1, 4, 1, 18, 3, 2, 1, 97), Counter32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: wfDHCPLoad.setStatus('mandatory')
wfCAPILoad = MibScalar((1, 3, 6, 1, 4, 1, 18, 3, 2, 1, 98), Counter32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: wfCAPILoad.setStatus('mandatory')
wfIPSECLoad = MibScalar((1, 3, 6, 1, 4, 1, 18, 3, 2, 1, 99), Counter32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: wfIPSECLoad.setStatus('mandatory')
wfMplsLdpLoad = MibScalar((1, 3, 6, 1, 4, 1, 18, 3, 2, 1, 100), Counter32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: wfMplsLdpLoad.setStatus('mandatory')
wfMplsMlmLoad = MibScalar((1, 3, 6, 1, 4, 1, 18, 3, 2, 1, 101), Counter32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: wfMplsMlmLoad.setStatus('mandatory')
wfBacPktGenLoad = MibScalar((1, 3, 6, 1, 4, 1, 18, 3, 2, 1, 102), Counter32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: wfBacPktGenLoad.setStatus('mandatory')
wfIISISLoad = MibScalar((1, 3, 6, 1, 4, 1, 18, 3, 2, 1, 103), Counter32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: wfIISISLoad.setStatus('mandatory')
wfCopsCLoad = MibScalar((1, 3, 6, 1, 4, 1, 18, 3, 2, 1, 104), Counter32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: wfCopsCLoad.setStatus('mandatory')
wfDiffServLoad = MibScalar((1, 3, 6, 1, 4, 1, 18, 3, 2, 1, 105), Counter32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: wfDiffServLoad.setStatus('mandatory')
wfIKELoad = MibScalar((1, 3, 6, 1, 4, 1, 18, 3, 2, 1, 106), Counter32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: wfIKELoad.setStatus('mandatory')
wfDsqmsProxyLoad = MibScalar((1, 3, 6, 1, 4, 1, 18, 3, 2, 1, 107), Counter32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: wfDsqmsProxyLoad.setStatus('mandatory')
wfLinkModules = MibIdentifier((1, 3, 6, 1, 4, 1, 18, 3, 2, 2))
wfENETIILoad = MibScalar((1, 3, 6, 1, 4, 1, 18, 3, 2, 2, 1), Counter32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: wfENETIILoad.setStatus('mandatory')
wfQENETLoad = MibScalar((1, 3, 6, 1, 4, 1, 18, 3, 2, 2, 2), Counter32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: wfQENETLoad.setStatus('mandatory')
wfFDDILoad = MibScalar((1, 3, 6, 1, 4, 1, 18, 3, 2, 2, 3), Counter32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: wfFDDILoad.setStatus('mandatory')
wfDSDELoad = MibScalar((1, 3, 6, 1, 4, 1, 18, 3, 2, 2, 4), Counter32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: wfDSDELoad.setStatus('mandatory')
wfDSDEIILoad = MibScalar((1, 3, 6, 1, 4, 1, 18, 3, 2, 2, 5), Counter32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: wfDSDEIILoad.setStatus('mandatory')
wfQSYNCLoad = MibScalar((1, 3, 6, 1, 4, 1, 18, 3, 2, 2, 6), Counter32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: wfQSYNCLoad.setStatus('mandatory')
wfDTLoad = MibScalar((1, 3, 6, 1, 4, 1, 18, 3, 2, 2, 7), Counter32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: wfDTLoad.setStatus('mandatory')
wfDSTLoad = MibScalar((1, 3, 6, 1, 4, 1, 18, 3, 2, 2, 8), Counter32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: wfDSTLoad.setStatus('mandatory')
wfT1IILoad = MibScalar((1, 3, 6, 1, 4, 1, 18, 3, 2, 2, 9), Counter32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: wfT1IILoad.setStatus('mandatory')
wfE1IILoad = MibScalar((1, 3, 6, 1, 4, 1, 18, 3, 2, 2, 10), Counter32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: wfE1IILoad.setStatus('mandatory')
wfHSSILoad = MibScalar((1, 3, 6, 1, 4, 1, 18, 3, 2, 2, 11), Counter32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: wfHSSILoad.setStatus('mandatory')
wfFNSDSELoad = MibScalar((1, 3, 6, 1, 4, 1, 18, 3, 2, 2, 12), Counter32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: wfFNSDSELoad.setStatus('mandatory')
wfFNSDSDTLoad = MibScalar((1, 3, 6, 1, 4, 1, 18, 3, 2, 2, 13), Counter32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: wfFNSDSDTLoad.setStatus('mandatory')
wfMCT1Load = MibScalar((1, 3, 6, 1, 4, 1, 18, 3, 2, 2, 14), Counter32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: wfMCT1Load.setStatus('mandatory')
wfANLoad = MibScalar((1, 3, 6, 1, 4, 1, 18, 3, 2, 2, 15), Counter32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: wfANLoad.setStatus('mandatory')
wfFNSDSETLoad = MibScalar((1, 3, 6, 1, 4, 1, 18, 3, 2, 2, 16), Counter32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: wfFNSDSETLoad.setStatus('mandatory')
wfMCT1E1Load = MibScalar((1, 3, 6, 1, 4, 1, 18, 3, 2, 2, 17), Counter32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: wfMCT1E1Load.setStatus('mandatory')
wfEFDDILoad = MibScalar((1, 3, 6, 1, 4, 1, 18, 3, 2, 2, 18), Counter32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: wfEFDDILoad.setStatus('mandatory')
wfHLSLoad = MibScalar((1, 3, 6, 1, 4, 1, 18, 3, 2, 2, 19), Counter32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: wfHLSLoad.setStatus('mandatory')
wfChipcomLoad = MibScalar((1, 3, 6, 1, 4, 1, 18, 3, 2, 2, 20), Counter32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: wfChipcomLoad.setStatus('mandatory')
wfAtmcLoad = MibScalar((1, 3, 6, 1, 4, 1, 18, 3, 2, 2, 21), Counter32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: wfAtmcLoad.setStatus('mandatory')
wfHDWANLMLoad = MibScalar((1, 3, 6, 1, 4, 1, 18, 3, 2, 2, 22), Counter32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: wfHDWANLMLoad.setStatus('mandatory')
wfDE100Load = MibScalar((1, 3, 6, 1, 4, 1, 18, 3, 2, 2, 23), Counter32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: wfDE100Load.setStatus('mandatory')
wfAtmc5000Load = MibScalar((1, 3, 6, 1, 4, 1, 18, 3, 2, 2, 24), Counter32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: wfAtmc5000Load.setStatus('mandatory')
wfArnLoad = MibScalar((1, 3, 6, 1, 4, 1, 18, 3, 2, 2, 25), Counter32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: wfArnLoad.setStatus('mandatory')
wfFntsLoad = MibScalar((1, 3, 6, 1, 4, 1, 18, 3, 2, 2, 26), Counter32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: wfFntsLoad.setStatus('mandatory')
wfSQE100Load = MibScalar((1, 3, 6, 1, 4, 1, 18, 3, 2, 2, 27), Counter32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: wfSQE100Load.setStatus('mandatory')
wfGigEnetLoad = MibScalar((1, 3, 6, 1, 4, 1, 18, 3, 2, 2, 28), Counter32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: wfGigEnetLoad.setStatus('mandatory')
wfFBRLoad = MibScalar((1, 3, 6, 1, 4, 1, 18, 3, 2, 2, 29), Counter32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: wfFBRLoad.setStatus('mandatory')
wfDrivers = MibIdentifier((1, 3, 6, 1, 4, 1, 18, 3, 2, 3))
wfLANCELoad = MibScalar((1, 3, 6, 1, 4, 1, 18, 3, 2, 3, 1), Counter32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: wfLANCELoad.setStatus('mandatory')
wfILACCLoad = MibScalar((1, 3, 6, 1, 4, 1, 18, 3, 2, 3, 2), Counter32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: wfILACCLoad.setStatus('mandatory')
wfFSILoad = MibScalar((1, 3, 6, 1, 4, 1, 18, 3, 2, 3, 3), Counter32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: wfFSILoad.setStatus('mandatory')
wfTMS380Load = MibScalar((1, 3, 6, 1, 4, 1, 18, 3, 2, 3, 4), Counter32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: wfTMS380Load.setStatus('mandatory')
wfMK5025Load = MibScalar((1, 3, 6, 1, 4, 1, 18, 3, 2, 3, 5), Counter32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: wfMK5025Load.setStatus('mandatory')
wfDS2180Load = MibScalar((1, 3, 6, 1, 4, 1, 18, 3, 2, 3, 6), Counter32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: wfDS2180Load.setStatus('mandatory')
wfDS2181Load = MibScalar((1, 3, 6, 1, 4, 1, 18, 3, 2, 3, 7), Counter32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: wfDS2181Load.setStatus('mandatory')
wfDEFALoad = MibScalar((1, 3, 6, 1, 4, 1, 18, 3, 2, 3, 8), Counter32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: wfDEFALoad.setStatus('mandatory')
wfAMZ8530Load = MibScalar((1, 3, 6, 1, 4, 1, 18, 3, 2, 3, 9), Counter32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: wfAMZ8530Load.setStatus('mandatory')
wfHSSIFSILoad = MibScalar((1, 3, 6, 1, 4, 1, 18, 3, 2, 3, 10), Counter32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: wfHSSIFSILoad.setStatus('mandatory')
wfMUNICHT1Load = MibScalar((1, 3, 6, 1, 4, 1, 18, 3, 2, 3, 11), Counter32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: wfMUNICHT1Load.setStatus('mandatory')
wfQsccSyncLoad = MibScalar((1, 3, 6, 1, 4, 1, 18, 3, 2, 3, 12), Counter32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: wfQsccSyncLoad.setStatus('mandatory')
wfQsccEnetLoad = MibScalar((1, 3, 6, 1, 4, 1, 18, 3, 2, 3, 13), Counter32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: wfQsccEnetLoad.setStatus('mandatory')
wfMunichLoad = MibScalar((1, 3, 6, 1, 4, 1, 18, 3, 2, 3, 14), Counter32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: wfMunichLoad.setStatus('mandatory')
wfHilanceLoad = MibScalar((1, 3, 6, 1, 4, 1, 18, 3, 2, 3, 15), Counter32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: wfHilanceLoad.setStatus('mandatory')
wfAtmAlcLoad = MibScalar((1, 3, 6, 1, 4, 1, 18, 3, 2, 3, 16), Counter32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: wfAtmAlcLoad.setStatus('mandatory')
wfRptrLoad = MibScalar((1, 3, 6, 1, 4, 1, 18, 3, 2, 3, 17), Counter32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: wfRptrLoad.setStatus('mandatory')
wfIsacLoad = MibScalar((1, 3, 6, 1, 4, 1, 18, 3, 2, 3, 18), Counter32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: wfIsacLoad.setStatus('mandatory')
wfAtmizerLoad = MibScalar((1, 3, 6, 1, 4, 1, 18, 3, 2, 3, 19), Counter32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: wfAtmizerLoad.setStatus('mandatory')
wfNSC100MLoad = MibScalar((1, 3, 6, 1, 4, 1, 18, 3, 2, 3, 20), Counter32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: wfNSC100MLoad.setStatus('mandatory')
wfDCMMWLoad = MibScalar((1, 3, 6, 1, 4, 1, 18, 3, 2, 3, 21), Counter32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: wfDCMMWLoad.setStatus('mandatory')
wfHwCompLoad = MibScalar((1, 3, 6, 1, 4, 1, 18, 3, 2, 3, 22), Counter32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: wfHwCompLoad.setStatus('mandatory')
wfRAEsaLoad = MibScalar((1, 3, 6, 1, 4, 1, 18, 3, 2, 3, 23), Counter32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: wfRAEsaLoad.setStatus('mandatory')
wfFntsAtmLoad = MibScalar((1, 3, 6, 1, 4, 1, 18, 3, 2, 3, 24), Counter32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: wfFntsAtmLoad.setStatus('mandatory')
wfRMONStatLoad = MibScalar((1, 3, 6, 1, 4, 1, 18, 3, 2, 3, 25), Counter32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: wfRMONStatLoad.setStatus('mandatory')
wfSEEQ100MLoad = MibScalar((1, 3, 6, 1, 4, 1, 18, 3, 2, 3, 26), Counter32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: wfSEEQ100MLoad.setStatus('mandatory')
wfSeeqGigLoad = MibScalar((1, 3, 6, 1, 4, 1, 18, 3, 2, 3, 27), Counter32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: wfSeeqGigLoad.setStatus('mandatory')
wfPQ2EnetLoad = MibScalar((1, 3, 6, 1, 4, 1, 18, 3, 2, 3, 28), Counter32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: wfPQ2EnetLoad.setStatus('mandatory')
wfTdmManagerLoad = MibScalar((1, 3, 6, 1, 4, 1, 18, 3, 2, 3, 29), Counter32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: wfTdmManagerLoad.setStatus('mandatory')
wfPQ2DsyncLoad = MibScalar((1, 3, 6, 1, 4, 1, 18, 3, 2, 3, 30), Counter32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: wfPQ2DsyncLoad.setStatus('mandatory')
wfVoIPLoad = MibScalar((1, 3, 6, 1, 4, 1, 18, 3, 2, 3, 31), Counter32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: wfVoIPLoad.setStatus('mandatory')
wfQsccVoIPLoad = MibScalar((1, 3, 6, 1, 4, 1, 18, 3, 2, 3, 32), Counter32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: wfQsccVoIPLoad.setStatus('mandatory')
mibBuilder.exportSymbols("Wellfleet-LOADER-MIB", wfSWSMDSLoad=wfSWSMDSLoad, wfNLSPLoad=wfNLSPLoad, wfLLC2Load=wfLLC2Load, wfSMDSLoad=wfSMDSLoad, wfFRSWLoad=wfFRSWLoad, wfILACCLoad=wfILACCLoad, wfMCT1E1Load=wfMCT1E1Load, wfL2TPLoad=wfL2TPLoad, wfPimLoad=wfPimLoad, wfFTPLoad=wfFTPLoad, wfDSTLoad=wfDSTLoad, wfDrivers=wfDrivers, wfDNSLoad=wfDNSLoad, wfHSSIFSILoad=wfHSSIFSILoad, wfCRMLoad=wfCRMLoad, wfPPPLoad=wfPPPLoad, wfNPTLoad=wfNPTLoad, wfFNSDSDTLoad=wfFNSDSDTLoad, wfAOTLoad=wfAOTLoad, wfDsqmsProxyLoad=wfDsqmsProxyLoad, wfPQ2EnetLoad=wfPQ2EnetLoad, wfNBIPLoad=wfNBIPLoad, wfAtmc5000Load=wfAtmc5000Load, wfENETIILoad=wfENETIILoad, wfXNSLoad=wfXNSLoad, wfHttpSrvLoad=wfHttpSrvLoad, wfIPSECLoad=wfIPSECLoad, wfDSDELoad=wfDSDELoad, wfDHCPLoad=wfDHCPLoad, wfVRRPLoad=wfVRRPLoad, wfSQE100Load=wfSQE100Load, wfBGPRSLoad=wfBGPRSLoad, wfTMS380Load=wfTMS380Load, wfFntsLoad=wfFntsLoad, wfFSILoad=wfFSILoad, wfDebugLoad=wfDebugLoad, wfDCMMWLoad=wfDCMMWLoad, wfQsccSyncLoad=wfQsccSyncLoad, wfNSC100MLoad=wfNSC100MLoad, wfIsacLoad=wfIsacLoad, wfFBRLoad=wfFBRLoad, wfMplsMlmLoad=wfMplsMlmLoad, wfIISISLoad=wfIISISLoad, wfDE100Load=wfDE100Load, wfMCT1Load=wfMCT1Load, wfAtmcLoad=wfAtmcLoad, wfBGPLoad=wfBGPLoad, wfLNMLoad=wfLNMLoad, wfRADIUSLoad=wfRADIUSLoad, wfStacLZSLoad=wfStacLZSLoad, wfTAG1QLoad=wfTAG1QLoad, wfX25DTELoad=wfX25DTELoad, wfDVSLoad=wfDVSLoad, wfFDDILoad=wfFDDILoad, wfIPEXLoad=wfIPEXLoad, wfCAPILoad=wfCAPILoad, wfIPv6Load=wfIPv6Load, wfMOSPFLoad=wfMOSPFLoad, wfRSVPLoad=wfRSVPLoad, wfIPROTOLoad=wfIPROTOLoad, wfDSDEIILoad=wfDSDEIILoad, wfRREDUNDLoad=wfRREDUNDLoad, wfWPROXYLoad=wfWPROXYLoad, wfATMMcsLoad=wfATMMcsLoad, wfMpcLoad=wfMpcLoad, wfLinkModules=wfLinkModules, wfPingLoad=wfPingLoad, wfAMZ8530Load=wfAMZ8530Load, wfLAPBLoad=wfLAPBLoad, wfE1IILoad=wfE1IILoad, wfPktCaptureLoad=wfPktCaptureLoad, wfAPPNLsLoad=wfAPPNLsLoad, wfQsccEnetLoad=wfQsccEnetLoad, wfDvmrpLoad=wfDvmrpLoad, wfVINESLoad=wfVINESLoad, wfWcpLoad=wfWcpLoad, wfHLSLoad=wfHLSLoad, wfTCPLoad=wfTCPLoad, wfCPMLoad=wfCPMLoad, wfDECNETLoad=wfDECNETLoad, wfCopsCLoad=wfCopsCLoad, wfSt2Load=wfSt2Load, wfARPLoad=wfARPLoad, wfBOTLoad=wfBOTLoad, wfNATLoad=wfNATLoad, wfTFTPLoad=wfTFTPLoad, wfSeeqGigLoad=wfSeeqGigLoad, wfFRSWCNGCLoad=wfFRSWCNGCLoad, wfFNSDSELoad=wfFNSDSELoad, wfSWPROXYLoad=wfSWPROXYLoad, wfHDWANLMLoad=wfHDWANLMLoad, wfATLoad=wfATLoad, wfISDNLoad=wfISDNLoad, wfArnLoad=wfArnLoad, wfLANCELoad=wfLANCELoad, wfMK5025Load=wfMK5025Load, wfIKELoad=wfIKELoad, wfATMAsmLoad=wfATMAsmLoad, wfBAYSIGLoad=wfBAYSIGLoad, wfWepLoad=wfWepLoad, wfConvStrLoad=wfConvStrLoad, wfEGPLoad=wfEGPLoad, wfMUNICHT1Load=wfMUNICHT1Load, wfATMLoad=wfATMLoad, wfATMCsLoad=wfATMCsLoad, wfAHBLoad=wfAHBLoad, wfRCMDSLoad=wfRCMDSLoad, wfIpSwitchLoad=wfIpSwitchLoad, wfGigEnetLoad=wfGigEnetLoad, wfRARPLoad=wfRARPLoad, wfQsccVoIPLoad=wfQsccVoIPLoad, wfOSPFLoad=wfOSPFLoad, wfSTATSLoad=wfSTATSLoad, wfSEEQ100MLoad=wfSEEQ100MLoad, wfFntsAtmLoad=wfFntsAtmLoad, wfDS2181Load=wfDS2181Load, wfISDBLoad=wfISDBLoad, wfFRLoad=wfFRLoad, wfHwCompLoad=wfHwCompLoad, wfS5ChasLoad=wfS5ChasLoad, wfSDLCLoad=wfSDLCLoad, wfPortMtxLoad=wfPortMtxLoad, wfFRSVCLoad=wfFRSVCLoad, wfEFDDILoad=wfEFDDILoad, wfT1IILoad=wfT1IILoad, wfTdmManagerLoad=wfTdmManagerLoad, wfSNMPLoad=wfSNMPLoad, wfFRPTLoad=wfFRPTLoad, wfLMLoad=wfLMLoad, wfRMONStatLoad=wfRMONStatLoad, wfATMSigLoad=wfATMSigLoad, wfLBCLoad=wfLBCLoad, wfRipv6Load=wfRipv6Load, wfNBASELoad=wfNBASELoad, wfDiffServLoad=wfDiffServLoad, wfDTLoad=wfDTLoad, wfAtmizerLoad=wfAtmizerLoad, wfMunichLoad=wfMunichLoad, wfANLoad=wfANLoad, wfATMLeLoad=wfATMLeLoad, wfQENETLoad=wfQENETLoad, wfIgmpLoad=wfIgmpLoad, wfRAEsaLoad=wfRAEsaLoad, wfHSSILoad=wfHSSILoad, wfDLSLoad=wfDLSLoad, wfTNCLoad=wfTNCLoad, wfPQ2DsyncLoad=wfPQ2DsyncLoad, wfDEFALoad=wfDEFALoad, wfBacPktGenLoad=wfBacPktGenLoad, wfScmIpcLoad=wfScmIpcLoad, wfX25DCELoad=wfX25DCELoad, wfAPPNCpLoad=wfAPPNCpLoad, wfASRLoad=wfASRLoad, wfNHRPLoad=wfNHRPLoad, wfSYSLLoad=wfSYSLLoad, wfFNSDSETLoad=wfFNSDSETLoad, wfProtocols=wfProtocols, wfTelnetLoad=wfTelnetLoad, wfOSILoad=wfOSILoad, wfVoIPLoad=wfVoIPLoad, wfNTPLoad=wfNTPLoad, wfMplsLdpLoad=wfMplsLdpLoad, wfIPXLoad=wfIPXLoad, wfQSYNCLoad=wfQSYNCLoad, wfMpsLoad=wfMpsLoad, wfAtmAlcLoad=wfAtmAlcLoad, wfVCCTLoad=wfVCCTLoad, wfRptrLoad=wfRptrLoad, wfDS2180Load=wfDS2180Load, wfChipcomLoad=wfChipcomLoad, wfHilanceLoad=wfHilanceLoad)