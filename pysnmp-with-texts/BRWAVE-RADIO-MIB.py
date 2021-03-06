#
# PySNMP MIB module BRWAVE-RADIO-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/BRWAVE-RADIO-MIB
# Produced by pysmi-0.3.4 at Wed May  1 11:41:28 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, SingleValueConstraint, ConstraintsUnion, ValueRangeConstraint, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "SingleValueConstraint", "ConstraintsUnion", "ValueRangeConstraint", "ConstraintsIntersection")
ifIndex, = mibBuilder.importSymbols("IF-MIB", "ifIndex")
ObjectGroup, ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ObjectGroup", "ModuleCompliance", "NotificationGroup")
Unsigned32, enterprises, iso, TimeTicks, Counter64, ObjectIdentity, Bits, Integer32, Gauge32, IpAddress, Counter32, MibScalar, MibTable, MibTableRow, MibTableColumn, MibIdentifier, NotificationType, ModuleIdentity = mibBuilder.importSymbols("SNMPv2-SMI", "Unsigned32", "enterprises", "iso", "TimeTicks", "Counter64", "ObjectIdentity", "Bits", "Integer32", "Gauge32", "IpAddress", "Counter32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "MibIdentifier", "NotificationType", "ModuleIdentity")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
brwaveRadioMibModule = ModuleIdentity((1, 3, 6, 1, 4, 1, 6080, 1, 1, 3))
brwaveRadioMibModule.setRevisions(('2006-07-06 11:00', '2005-05-26 11:30',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: brwaveRadioMibModule.setRevisionsDescriptions(('Combined ROOT/RADIO mib in one module.', 'Radio MIB module created.',))
if mibBuilder.loadTexts: brwaveRadioMibModule.setLastUpdated('200607061100Z')
if mibBuilder.loadTexts: brwaveRadioMibModule.setOrganization('BridgeWave Communications')
if mibBuilder.loadTexts: brwaveRadioMibModule.setContactInfo(' Postal: BridgeWave Communications 3350 Thomas Road Santa Clara, CA 95054 USA Tel: +1 408 567 6900 Fax: +1 408 567 0775 Web: www.bridgewave.com ')
if mibBuilder.loadTexts: brwaveRadioMibModule.setDescription('Radio MIB module.')
bridgeWave = ObjectIdentity((1, 3, 6, 1, 4, 1, 6080))
if mibBuilder.loadTexts: bridgeWave.setStatus('current')
if mibBuilder.loadTexts: bridgeWave.setDescription('BridgeWave enterprise OID.')
brwaveReg = ObjectIdentity((1, 3, 6, 1, 4, 1, 6080, 1))
if mibBuilder.loadTexts: brwaveReg.setStatus('current')
if mibBuilder.loadTexts: brwaveReg.setDescription('Sub-tree for BridgeWave objects registration.')
brwaveMibs = ObjectIdentity((1, 3, 6, 1, 4, 1, 6080, 1, 1))
if mibBuilder.loadTexts: brwaveMibs.setStatus('current')
if mibBuilder.loadTexts: brwaveMibs.setDescription('Sub-tree to register values assigned to MIB modules with the MODULES-IDENTITY construct.')
brwaveModules = ObjectIdentity((1, 3, 6, 1, 4, 1, 6080, 1, 2))
if mibBuilder.loadTexts: brwaveModules.setStatus('current')
if mibBuilder.loadTexts: brwaveModules.setDescription('Sub-tree to register unique values assigned to identify all BridgeWave hardware and software components of ethernet radio products.')
brwaveRadioFE60 = ObjectIdentity((1, 3, 6, 1, 4, 1, 6080, 1, 2, 1))
if mibBuilder.loadTexts: brwaveRadioFE60.setStatus('current')
if mibBuilder.loadTexts: brwaveRadioFE60.setDescription('Registered System OID for FE60 radio.')
brwaveRadioGE60 = ObjectIdentity((1, 3, 6, 1, 4, 1, 6080, 1, 2, 2))
if mibBuilder.loadTexts: brwaveRadioGE60.setStatus('current')
if mibBuilder.loadTexts: brwaveRadioGE60.setDescription('Registered System OID for GE60 radio.')
brwaveRadioAR60 = ObjectIdentity((1, 3, 6, 1, 4, 1, 6080, 1, 2, 3))
if mibBuilder.loadTexts: brwaveRadioAR60.setStatus('current')
if mibBuilder.loadTexts: brwaveRadioAR60.setDescription('Registered system OID for AdaptiveRate(AR60) radio.')
brwaveCommon = ObjectIdentity((1, 3, 6, 1, 4, 1, 6080, 2))
if mibBuilder.loadTexts: brwaveCommon.setStatus('current')
if mibBuilder.loadTexts: brwaveCommon.setDescription('Sub-tree for BridgeWave objects common across products.')
brwaveRadioSn = MibScalar((1, 3, 6, 1, 4, 1, 6080, 2, 1), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: brwaveRadioSn.setStatus('current')
if mibBuilder.loadTexts: brwaveRadioSn.setDescription('Radio serial number.')
brwaveUnitModel = MibScalar((1, 3, 6, 1, 4, 1, 6080, 2, 2), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: brwaveUnitModel.setStatus('current')
if mibBuilder.loadTexts: brwaveUnitModel.setDescription("Unit's model.")
brwaveBbSn = MibScalar((1, 3, 6, 1, 4, 1, 6080, 2, 3), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: brwaveBbSn.setStatus('current')
if mibBuilder.loadTexts: brwaveBbSn.setDescription('Base Band hardware serial number')
brwaveIfSn = MibScalar((1, 3, 6, 1, 4, 1, 6080, 2, 4), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: brwaveIfSn.setStatus('current')
if mibBuilder.loadTexts: brwaveIfSn.setDescription('IF hardware serial number')
brwaveMmwSn = MibScalar((1, 3, 6, 1, 4, 1, 6080, 2, 5), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: brwaveMmwSn.setStatus('current')
if mibBuilder.loadTexts: brwaveMmwSn.setDescription('MMW Hardware serial number')
brwaveTrapCount = MibScalar((1, 3, 6, 1, 4, 1, 6080, 2, 6), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: brwaveTrapCount.setStatus('current')
if mibBuilder.loadTexts: brwaveTrapCount.setDescription('Number of traps generated by unit since start-up. Rolls back to zero once reached to maximum value.')
brwaveProducts = ObjectIdentity((1, 3, 6, 1, 4, 1, 6080, 3))
if mibBuilder.loadTexts: brwaveProducts.setStatus('current')
if mibBuilder.loadTexts: brwaveProducts.setDescription('Sub-tree for product specific objects & events')
brwaveRadio = ObjectIdentity((1, 3, 6, 1, 4, 1, 6080, 3, 1))
if mibBuilder.loadTexts: brwaveRadio.setStatus('current')
if mibBuilder.loadTexts: brwaveRadio.setDescription('Ethernet Radio (FE60/GE60/AR60) obejcts.')
brwaveRadioFactorySetup = ObjectIdentity((1, 3, 6, 1, 4, 1, 6080, 3, 1, 2))
if mibBuilder.loadTexts: brwaveRadioFactorySetup.setStatus('current')
if mibBuilder.loadTexts: brwaveRadioFactorySetup.setDescription('Group of factory setup objects.')
brwaveRadioTxBand = MibScalar((1, 3, 6, 1, 4, 1, 6080, 3, 1, 2, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("low", 1), ("high", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: brwaveRadioTxBand.setStatus('current')
if mibBuilder.loadTexts: brwaveRadioTxBand.setDescription('Radio Link Transmit frequency.')
brwaveRadioFactoryRate = MibScalar((1, 3, 6, 1, 4, 1, 6080, 3, 1, 2, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("adaptRate", 1), ("mbps1000", 2), ("mbps100", 3)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: brwaveRadioFactoryRate.setStatus('current')
if mibBuilder.loadTexts: brwaveRadioFactoryRate.setDescription('Factory configured radio link rate.')
brwaveRadioClearStats = MibScalar((1, 3, 6, 1, 4, 1, 6080, 3, 1, 2, 4), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: brwaveRadioClearStats.setStatus('current')
if mibBuilder.loadTexts: brwaveRadioClearStats.setDescription('Clear Statistics, Set value of 1 to clear. Returns always 0 when read.')
brwaveRadioStatus = ObjectIdentity((1, 3, 6, 1, 4, 1, 6080, 3, 1, 3))
if mibBuilder.loadTexts: brwaveRadioStatus.setStatus('current')
if mibBuilder.loadTexts: brwaveRadioStatus.setDescription('Group of radio status objects.')
brwaveRadioInVoltage = MibScalar((1, 3, 6, 1, 4, 1, 6080, 3, 1, 3, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: brwaveRadioInVoltage.setStatus('current')
if mibBuilder.loadTexts: brwaveRadioInVoltage.setDescription("Input voltage. The reading of the unit's input voltage level in Volts x100.")
brwaveRadioUnitTemperature = MibScalar((1, 3, 6, 1, 4, 1, 6080, 3, 1, 3, 2), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: brwaveRadioUnitTemperature.setStatus('current')
if mibBuilder.loadTexts: brwaveRadioUnitTemperature.setDescription('Unit Temperature. The reading of the temperature sensor in degrees C x 100.')
brwaveRadioTxTemperature = MibScalar((1, 3, 6, 1, 4, 1, 6080, 3, 1, 3, 3), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: brwaveRadioTxTemperature.setStatus('current')
if mibBuilder.loadTexts: brwaveRadioTxTemperature.setDescription('Radio Transmiter Temperature. The reading of the radio temperature sensor in degrees C x 100.')
brwaveRadioRSL = MibScalar((1, 3, 6, 1, 4, 1, 6080, 3, 1, 3, 4), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: brwaveRadioRSL.setStatus('current')
if mibBuilder.loadTexts: brwaveRadioRSL.setDescription('Received Signal Level. The signal level of the received radio frequency in dBm x 100')
brwaveRadioRSLVoltage = MibScalar((1, 3, 6, 1, 4, 1, 6080, 3, 1, 3, 5), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: brwaveRadioRSLVoltage.setStatus('current')
if mibBuilder.loadTexts: brwaveRadioRSLVoltage.setDescription('Received Signal Level measured as Voltage.')
brwaveRadioAbsRSL = MibScalar((1, 3, 6, 1, 4, 1, 6080, 3, 1, 3, 6), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: brwaveRadioAbsRSL.setStatus('current')
if mibBuilder.loadTexts: brwaveRadioAbsRSL.setDescription('Received Signal Level. The signal level of the received radio frequency in dBm x 100')
brwaveRadioRSLVoltageInt = MibScalar((1, 3, 6, 1, 4, 1, 6080, 3, 1, 3, 7), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: brwaveRadioRSLVoltageInt.setStatus('current')
if mibBuilder.loadTexts: brwaveRadioRSLVoltageInt.setDescription('Received Signal Level measured as Voltage.')
brwaveCopperUtilization = MibScalar((1, 3, 6, 1, 4, 1, 6080, 3, 1, 3, 8), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: brwaveCopperUtilization.setStatus('current')
if mibBuilder.loadTexts: brwaveCopperUtilization.setDescription('Link utilization calculated every polling interval.')
brwaveFiberUtilization = MibScalar((1, 3, 6, 1, 4, 1, 6080, 3, 1, 3, 9), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: brwaveFiberUtilization.setStatus('current')
if mibBuilder.loadTexts: brwaveFiberUtilization.setDescription('Link utilization calculated every polling interval.')
brwaveRadioUtilization = MibScalar((1, 3, 6, 1, 4, 1, 6080, 3, 1, 3, 10), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: brwaveRadioUtilization.setStatus('current')
if mibBuilder.loadTexts: brwaveRadioUtilization.setDescription('Link utilization calculated every polling interval.')
brwaveRadioFecError = MibScalar((1, 3, 6, 1, 4, 1, 6080, 3, 1, 3, 11), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1, 2))).clone(namedValues=NamedValues(("noError", 0), ("preFec", 1), ("postFec", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: brwaveRadioFecError.setStatus('current')
if mibBuilder.loadTexts: brwaveRadioFecError.setDescription('Post and Pre FEC error calculated every polling interval 0 - No Error, 1-Pre FEC Error, 2-Post FEC Error')
brwaveRadioPreFecFlag = MibScalar((1, 3, 6, 1, 4, 1, 6080, 3, 1, 3, 12), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: brwaveRadioPreFecFlag.setStatus('current')
if mibBuilder.loadTexts: brwaveRadioPreFecFlag.setDescription('Pre FEC error flag every polling interval')
brwaveRadioPostFecFlag = MibScalar((1, 3, 6, 1, 4, 1, 6080, 3, 1, 3, 13), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: brwaveRadioPostFecFlag.setStatus('current')
if mibBuilder.loadTexts: brwaveRadioPostFecFlag.setDescription('Post FEC error Flag every polling interval')
brwaveRadioLinkRate = MibScalar((1, 3, 6, 1, 4, 1, 6080, 3, 1, 3, 14), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: brwaveRadioLinkRate.setStatus('current')
if mibBuilder.loadTexts: brwaveRadioLinkRate.setDescription('Radio Link Rate in Mbps.')
brwaveRadioEvents = MibIdentifier((1, 3, 6, 1, 4, 1, 6080, 3, 1, 9))
brwaveRadioEventsV2 = MibIdentifier((1, 3, 6, 1, 4, 1, 6080, 3, 1, 9, 0))
brwaveRadioTrapObjs = MibIdentifier((1, 3, 6, 1, 4, 1, 6080, 3, 1, 9, 1))
managerIP = MibScalar((1, 3, 6, 1, 4, 1, 6080, 3, 1, 9, 1, 1), OctetString().subtype(subtypeSpec=ValueSizeConstraint(0, 32))).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: managerIP.setStatus('current')
if mibBuilder.loadTexts: managerIP.setDescription('IP address of NMS station accessing the unit.')
userName = MibScalar((1, 3, 6, 1, 4, 1, 6080, 3, 1, 9, 1, 2), OctetString().subtype(subtypeSpec=ValueSizeConstraint(0, 32))).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: userName.setStatus('current')
if mibBuilder.loadTexts: userName.setDescription('User accessing the unit.')
brwaveConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 6080, 3, 1, 10))
brwaveRadioGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 6080, 3, 1, 10, 1))
brwaveCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 6080, 3, 1, 10, 2))
brwaveErrorsOverThreshold = NotificationType((1, 3, 6, 1, 4, 1, 6080, 3, 1, 9, 0, 1)).setObjects(("IF-MIB", "ifIndex"), ("BRWAVE-RADIO-MIB", "brwaveRadioUnitTemperature"), ("BRWAVE-RADIO-MIB", "brwaveRadioTxTemperature"), ("BRWAVE-RADIO-MIB", "brwaveRadioRSL"))
if mibBuilder.loadTexts: brwaveErrorsOverThreshold.setStatus('current')
if mibBuilder.loadTexts: brwaveErrorsOverThreshold.setDescription('Link has error rate over threshold.')
brwaveErrorsUnderThreshold = NotificationType((1, 3, 6, 1, 4, 1, 6080, 3, 1, 9, 0, 2)).setObjects(("IF-MIB", "ifIndex"), ("BRWAVE-RADIO-MIB", "brwaveRadioUnitTemperature"), ("BRWAVE-RADIO-MIB", "brwaveRadioTxTemperature"), ("BRWAVE-RADIO-MIB", "brwaveRadioRSL"))
if mibBuilder.loadTexts: brwaveErrorsUnderThreshold.setStatus('current')
if mibBuilder.loadTexts: brwaveErrorsUnderThreshold.setDescription('Link error rate changed from over to under threshold .')
brwaveUnitTemperatureAbnormal = NotificationType((1, 3, 6, 1, 4, 1, 6080, 3, 1, 9, 0, 3)).setObjects(("BRWAVE-RADIO-MIB", "brwaveRadioUnitTemperature"))
if mibBuilder.loadTexts: brwaveUnitTemperatureAbnormal.setStatus('current')
if mibBuilder.loadTexts: brwaveUnitTemperatureAbnormal.setDescription('Radio unit temperature not in normal operating range. Normal range is: -20 to +75 degree Centigrade.')
brwaveUnitTemperatureNormal = NotificationType((1, 3, 6, 1, 4, 1, 6080, 3, 1, 9, 0, 4)).setObjects(("BRWAVE-RADIO-MIB", "brwaveRadioUnitTemperature"))
if mibBuilder.loadTexts: brwaveUnitTemperatureNormal.setStatus('current')
if mibBuilder.loadTexts: brwaveUnitTemperatureNormal.setDescription('Unit temperature restores from abnormal to normal range.')
brwaveTxTemperatureAbnormal = NotificationType((1, 3, 6, 1, 4, 1, 6080, 3, 1, 9, 0, 5)).setObjects(("BRWAVE-RADIO-MIB", "brwaveRadioTxTemperature"))
if mibBuilder.loadTexts: brwaveTxTemperatureAbnormal.setStatus('current')
if mibBuilder.loadTexts: brwaveTxTemperatureAbnormal.setDescription('Transmitter temperature is not in normal operating range. Normal range is: -20 to +75 degree Centigrade.')
brwaveTxTemperatureNormal = NotificationType((1, 3, 6, 1, 4, 1, 6080, 3, 1, 9, 0, 6)).setObjects(("BRWAVE-RADIO-MIB", "brwaveRadioTxTemperature"))
if mibBuilder.loadTexts: brwaveTxTemperatureNormal.setStatus('current')
if mibBuilder.loadTexts: brwaveTxTemperatureNormal.setDescription('Transmitter temperature is restored to normal range.')
brwaveInputVoltageAbnormal = NotificationType((1, 3, 6, 1, 4, 1, 6080, 3, 1, 9, 0, 7)).setObjects(("BRWAVE-RADIO-MIB", "brwaveRadioInVoltage"))
if mibBuilder.loadTexts: brwaveInputVoltageAbnormal.setStatus('current')
if mibBuilder.loadTexts: brwaveInputVoltageAbnormal.setDescription("Unit's input voltage is not in normal range. Normal input voltage > 16 Volts.")
brwaveInputVoltageNormal = NotificationType((1, 3, 6, 1, 4, 1, 6080, 3, 1, 9, 0, 8)).setObjects(("BRWAVE-RADIO-MIB", "brwaveRadioInVoltage"))
if mibBuilder.loadTexts: brwaveInputVoltageNormal.setStatus('current')
if mibBuilder.loadTexts: brwaveInputVoltageNormal.setDescription("Unit's input voltage is restored to normal range.")
brwaveRslNormal = NotificationType((1, 3, 6, 1, 4, 1, 6080, 3, 1, 9, 0, 10)).setObjects(("BRWAVE-RADIO-MIB", "brwaveRadioRSL"))
if mibBuilder.loadTexts: brwaveRslNormal.setStatus('current')
if mibBuilder.loadTexts: brwaveRslNormal.setDescription('Received Signal Level is normal. Normal signal level RSL > -55.00 dBm (Gigabit) and RSL > -59.00 dBm (Fast Ethernet).')
brwaveRslMinor = NotificationType((1, 3, 6, 1, 4, 1, 6080, 3, 1, 9, 0, 11)).setObjects(("BRWAVE-RADIO-MIB", "brwaveRadioRSL"))
if mibBuilder.loadTexts: brwaveRslMinor.setStatus('current')
if mibBuilder.loadTexts: brwaveRslMinor.setDescription('Received Signal Leve droped to the level of minor event. RSL from -55.00 to -59.00 dBm (GE Radio) RSL from -59.00 to -65.00 dBm (FE radio).')
brwaveRslMajor = NotificationType((1, 3, 6, 1, 4, 1, 6080, 3, 1, 9, 0, 13)).setObjects(("BRWAVE-RADIO-MIB", "brwaveRadioRSL"))
if mibBuilder.loadTexts: brwaveRslMajor.setStatus('current')
if mibBuilder.loadTexts: brwaveRslMajor.setDescription('RSL droppped to the level of major event. RSL < -59.00 dBm (GE Radio) or RSL < -65 dBm (FE radio).')
brwaveConfigChange = NotificationType((1, 3, 6, 1, 4, 1, 6080, 3, 1, 9, 0, 26))
if mibBuilder.loadTexts: brwaveConfigChange.setStatus('current')
if mibBuilder.loadTexts: brwaveConfigChange.setDescription('Configuration changes are performed by WEB client.')
brwaveLoginSuccessfull = NotificationType((1, 3, 6, 1, 4, 1, 6080, 3, 1, 9, 0, 27))
if mibBuilder.loadTexts: brwaveLoginSuccessfull.setStatus('current')
if mibBuilder.loadTexts: brwaveLoginSuccessfull.setDescription('NMS Loged in successfully.')
brwaveGeToFeSwitch = NotificationType((1, 3, 6, 1, 4, 1, 6080, 3, 1, 9, 0, 28)).setObjects(("BRWAVE-RADIO-MIB", "brwaveRadioRSL"))
if mibBuilder.loadTexts: brwaveGeToFeSwitch.setStatus('current')
if mibBuilder.loadTexts: brwaveGeToFeSwitch.setDescription('Tx Rate switched from GE to FE.')
brwaveFeToGeSwitch = NotificationType((1, 3, 6, 1, 4, 1, 6080, 3, 1, 9, 0, 29)).setObjects(("BRWAVE-RADIO-MIB", "brwaveRadioRSL"))
if mibBuilder.loadTexts: brwaveFeToGeSwitch.setStatus('current')
if mibBuilder.loadTexts: brwaveFeToGeSwitch.setDescription('Tx Rate switched from FE to GE.')
brwaveCommonGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 6080, 3, 1, 10, 1, 1)).setObjects(("BRWAVE-RADIO-MIB", "brwaveRadioSn"), ("BRWAVE-RADIO-MIB", "brwaveUnitModel"), ("BRWAVE-RADIO-MIB", "brwaveTrapCount"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    brwaveCommonGroup = brwaveCommonGroup.setStatus('current')
if mibBuilder.loadTexts: brwaveCommonGroup.setDescription('Collection of common objects.')
brwaveFactoryGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 6080, 3, 1, 10, 1, 2)).setObjects(("BRWAVE-RADIO-MIB", "brwaveRadioTxBand"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    brwaveFactoryGroup = brwaveFactoryGroup.setStatus('current')
if mibBuilder.loadTexts: brwaveFactoryGroup.setDescription('Collection of factory setup objects.')
brwaveStatusGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 6080, 3, 1, 10, 1, 3)).setObjects(("BRWAVE-RADIO-MIB", "brwaveRadioInVoltage"), ("BRWAVE-RADIO-MIB", "brwaveRadioUnitTemperature"), ("BRWAVE-RADIO-MIB", "brwaveRadioTxTemperature"), ("BRWAVE-RADIO-MIB", "brwaveRadioRSL"), ("BRWAVE-RADIO-MIB", "brwaveRadioRSLVoltage"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    brwaveStatusGroup = brwaveStatusGroup.setStatus('current')
if mibBuilder.loadTexts: brwaveStatusGroup.setDescription('Collection of status objects.')
mibBuilder.exportSymbols("BRWAVE-RADIO-MIB", brwaveErrorsOverThreshold=brwaveErrorsOverThreshold, PYSNMP_MODULE_ID=brwaveRadioMibModule, brwaveCommon=brwaveCommon, brwaveRadioInVoltage=brwaveRadioInVoltage, brwaveRadioLinkRate=brwaveRadioLinkRate, brwaveRadioSn=brwaveRadioSn, brwaveMmwSn=brwaveMmwSn, brwaveGeToFeSwitch=brwaveGeToFeSwitch, brwaveRadioAbsRSL=brwaveRadioAbsRSL, brwaveConfigChange=brwaveConfigChange, brwaveBbSn=brwaveBbSn, brwaveRadioFactorySetup=brwaveRadioFactorySetup, brwaveFeToGeSwitch=brwaveFeToGeSwitch, bridgeWave=bridgeWave, brwaveRslMajor=brwaveRslMajor, brwaveFiberUtilization=brwaveFiberUtilization, brwaveRadioStatus=brwaveRadioStatus, brwaveUnitTemperatureAbnormal=brwaveUnitTemperatureAbnormal, brwaveRadioTxTemperature=brwaveRadioTxTemperature, brwaveCopperUtilization=brwaveCopperUtilization, brwaveRadioFactoryRate=brwaveRadioFactoryRate, managerIP=managerIP, brwaveModules=brwaveModules, brwaveConformance=brwaveConformance, brwaveMibs=brwaveMibs, brwaveRadioAR60=brwaveRadioAR60, brwaveRadioUnitTemperature=brwaveRadioUnitTemperature, brwaveRslNormal=brwaveRslNormal, brwaveStatusGroup=brwaveStatusGroup, brwaveInputVoltageAbnormal=brwaveInputVoltageAbnormal, brwaveRslMinor=brwaveRslMinor, brwaveLoginSuccessfull=brwaveLoginSuccessfull, brwaveRadioRSLVoltageInt=brwaveRadioRSLVoltageInt, brwaveCompliances=brwaveCompliances, brwaveRadioRSLVoltage=brwaveRadioRSLVoltage, userName=userName, brwaveInputVoltageNormal=brwaveInputVoltageNormal, brwaveFactoryGroup=brwaveFactoryGroup, brwaveRadioUtilization=brwaveRadioUtilization, brwaveCommonGroup=brwaveCommonGroup, brwaveRadio=brwaveRadio, brwaveRadioTrapObjs=brwaveRadioTrapObjs, brwaveRadioClearStats=brwaveRadioClearStats, brwaveRadioGroups=brwaveRadioGroups, brwaveTxTemperatureAbnormal=brwaveTxTemperatureAbnormal, brwaveErrorsUnderThreshold=brwaveErrorsUnderThreshold, brwaveUnitTemperatureNormal=brwaveUnitTemperatureNormal, brwaveUnitModel=brwaveUnitModel, brwaveRadioTxBand=brwaveRadioTxBand, brwaveRadioFE60=brwaveRadioFE60, brwaveReg=brwaveReg, brwaveIfSn=brwaveIfSn, brwaveTrapCount=brwaveTrapCount, brwaveProducts=brwaveProducts, brwaveRadioRSL=brwaveRadioRSL, brwaveRadioPostFecFlag=brwaveRadioPostFecFlag, brwaveRadioEvents=brwaveRadioEvents, brwaveRadioGE60=brwaveRadioGE60, brwaveTxTemperatureNormal=brwaveTxTemperatureNormal, brwaveRadioFecError=brwaveRadioFecError, brwaveRadioEventsV2=brwaveRadioEventsV2, brwaveRadioPreFecFlag=brwaveRadioPreFecFlag, brwaveRadioMibModule=brwaveRadioMibModule)
