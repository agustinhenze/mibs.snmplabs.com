#
# PySNMP MIB module AMIMEGARAIDMIF-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/AMIMEGARAIDMIF-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 17:06:43 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
ObjectIdentifier, Integer, OctetString = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "Integer", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, SingleValueConstraint, ConstraintsUnion, ValueRangeConstraint, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "SingleValueConstraint", "ConstraintsUnion", "ValueRangeConstraint", "ConstraintsIntersection")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
ModuleIdentity, Gauge32, Integer32, Bits, ObjectIdentity, iso, Unsigned32, MibIdentifier, enterprises, TimeTicks, IpAddress, Counter32, MibScalar, MibTable, MibTableRow, MibTableColumn, NotificationType, Counter64 = mibBuilder.importSymbols("SNMPv2-SMI", "ModuleIdentity", "Gauge32", "Integer32", "Bits", "ObjectIdentity", "iso", "Unsigned32", "MibIdentifier", "enterprises", "TimeTicks", "IpAddress", "Counter32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "NotificationType", "Counter64")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
class DmiInteger(Integer32):
    pass

class DmiOctetstring(OctetString):
    pass

class DmiDisplaystring(DisplayString):
    pass

class DmiDateX(OctetString):
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(28, 28)
    fixedLength = 28

class DmiComponentIndex(Integer32):
    pass

ami = MibIdentifier((1, 3, 6, 1, 4, 1, 16))
megaraid = MibIdentifier((1, 3, 6, 1, 4, 1, 16, 1))
mifmib = MibIdentifier((1, 3, 6, 1, 4, 1, 16, 1, 2))
dmtfGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 16, 1, 2, 1))
tComponentid = MibTable((1, 3, 6, 1, 4, 1, 16, 1, 2, 1, 1), )
if mibBuilder.loadTexts: tComponentid.setStatus('mandatory')
eComponentid = MibTableRow((1, 3, 6, 1, 4, 1, 16, 1, 2, 1, 1, 1), ).setIndexNames((0, "AMIMEGARAIDMIF-MIB", "DmiComponentIndex"))
if mibBuilder.loadTexts: eComponentid.setStatus('mandatory')
a1Manufacturer = MibTableColumn((1, 3, 6, 1, 4, 1, 16, 1, 2, 1, 1, 1, 1), DmiDisplaystring()).setMaxAccess("readonly")
if mibBuilder.loadTexts: a1Manufacturer.setStatus('mandatory')
a1Product = MibTableColumn((1, 3, 6, 1, 4, 1, 16, 1, 2, 1, 1, 1, 2), DmiDisplaystring()).setMaxAccess("readonly")
if mibBuilder.loadTexts: a1Product.setStatus('mandatory')
a1Version = MibTableColumn((1, 3, 6, 1, 4, 1, 16, 1, 2, 1, 1, 1, 3), DmiDisplaystring()).setMaxAccess("readonly")
if mibBuilder.loadTexts: a1Version.setStatus('mandatory')
a1SerialNumber = MibTableColumn((1, 3, 6, 1, 4, 1, 16, 1, 2, 1, 1, 1, 4), DmiDisplaystring()).setMaxAccess("readonly")
if mibBuilder.loadTexts: a1SerialNumber.setStatus('mandatory')
a1Installation = MibTableColumn((1, 3, 6, 1, 4, 1, 16, 1, 2, 1, 1, 1, 5), DmiDateX()).setMaxAccess("readonly")
if mibBuilder.loadTexts: a1Installation.setStatus('mandatory')
a1Verify = MibTableColumn((1, 3, 6, 1, 4, 1, 16, 1, 2, 1, 1, 1, 6), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3, 4, 5, 6, 7))).clone(namedValues=NamedValues(("vAnErrorOccurredCheckStatusCode", 0), ("vThisComponentDoesNotExist", 1), ("vTheVerifyIsNotSupported", 2), ("vReserved", 3), ("vThisComponentExistsButTheFunctionalityI", 4), ("vThisComponentExistsButTheFunctionality1", 5), ("vThisComponentExistsAndIsNotFunctioningC", 6), ("vThisComponentExistsAndIsFunctioningCorr", 7)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: a1Verify.setStatus('mandatory')
tControllerInformation = MibTable((1, 3, 6, 1, 4, 1, 16, 1, 2, 1, 2), )
if mibBuilder.loadTexts: tControllerInformation.setStatus('mandatory')
eControllerInformation = MibTableRow((1, 3, 6, 1, 4, 1, 16, 1, 2, 1, 2, 1), ).setIndexNames((0, "AMIMEGARAIDMIF-MIB", "DmiComponentIndex"), (0, "AMIMEGARAIDMIF-MIB", "a2Adpadapternumber"))
if mibBuilder.loadTexts: eControllerInformation.setStatus('mandatory')
a2Adpadapternumber = MibTableColumn((1, 3, 6, 1, 4, 1, 16, 1, 2, 1, 2, 1, 1), DmiInteger()).setMaxAccess("readonly")
if mibBuilder.loadTexts: a2Adpadapternumber.setStatus('mandatory')
a2Firmwareversion = MibTableColumn((1, 3, 6, 1, 4, 1, 16, 1, 2, 1, 2, 1, 2), DmiDisplaystring()).setMaxAccess("readonly")
if mibBuilder.loadTexts: a2Firmwareversion.setStatus('mandatory')
a2Biosversion = MibTableColumn((1, 3, 6, 1, 4, 1, 16, 1, 2, 1, 2, 1, 3), DmiDisplaystring()).setMaxAccess("readonly")
if mibBuilder.loadTexts: a2Biosversion.setStatus('mandatory')
a2Numlogicaldrives = MibTableColumn((1, 3, 6, 1, 4, 1, 16, 1, 2, 1, 2, 1, 4), DmiInteger()).setMaxAccess("readonly")
if mibBuilder.loadTexts: a2Numlogicaldrives.setStatus('mandatory')
a2Dramsizeinmb = MibTableColumn((1, 3, 6, 1, 4, 1, 16, 1, 2, 1, 2, 1, 5), DmiInteger()).setMaxAccess("readonly")
if mibBuilder.loadTexts: a2Dramsizeinmb.setStatus('mandatory')
a2Chipsettype = MibTableColumn((1, 3, 6, 1, 4, 1, 16, 1, 2, 1, 2, 1, 6), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(225, 226, 97))).clone(namedValues=NamedValues(("vIntelneptuneormercury", 225), ("vTriton", 226), ("vOthers", 97)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: a2Chipsettype.setStatus('mandatory')
a2Rebuildrateinpercent = MibTableColumn((1, 3, 6, 1, 4, 1, 16, 1, 2, 1, 2, 1, 7), DmiInteger()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: a2Rebuildrateinpercent.setStatus('mandatory')
a2Flushinterval = MibTableColumn((1, 3, 6, 1, 4, 1, 16, 1, 2, 1, 2, 1, 8), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(2, 4, 6, 8, 10))).clone(namedValues=NamedValues(("vTwosec", 2), ("vFoursec", 4), ("vSixsec", 6), ("vEightsec", 8), ("vTensec", 10)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: a2Flushinterval.setStatus('mandatory')
a2Maxconcurrentcmds = MibTableColumn((1, 3, 6, 1, 4, 1, 16, 1, 2, 1, 2, 1, 9), DmiInteger()).setMaxAccess("readonly")
if mibBuilder.loadTexts: a2Maxconcurrentcmds.setStatus('mandatory')
a2Spinupdelay = MibTableColumn((1, 3, 6, 1, 4, 1, 16, 1, 2, 1, 2, 1, 10), DmiInteger()).setMaxAccess("readonly")
if mibBuilder.loadTexts: a2Spinupdelay.setStatus('mandatory')
a2Spinupcount = MibTableColumn((1, 3, 6, 1, 4, 1, 16, 1, 2, 1, 2, 1, 11), DmiInteger()).setMaxAccess("readonly")
if mibBuilder.loadTexts: a2Spinupcount.setStatus('mandatory')
a2Adpioreadspersec = MibTableColumn((1, 3, 6, 1, 4, 1, 16, 1, 2, 1, 2, 1, 12), DmiInteger()).setMaxAccess("readonly")
if mibBuilder.loadTexts: a2Adpioreadspersec.setStatus('mandatory')
a2Adpiowritespersec = MibTableColumn((1, 3, 6, 1, 4, 1, 16, 1, 2, 1, 2, 1, 13), DmiInteger()).setMaxAccess("readonly")
if mibBuilder.loadTexts: a2Adpiowritespersec.setStatus('mandatory')
a2Adpreadkbspersec = MibTableColumn((1, 3, 6, 1, 4, 1, 16, 1, 2, 1, 2, 1, 14), DmiInteger()).setMaxAccess("readonly")
if mibBuilder.loadTexts: a2Adpreadkbspersec.setStatus('mandatory')
a2Adpwritekbspersec = MibTableColumn((1, 3, 6, 1, 4, 1, 16, 1, 2, 1, 2, 1, 15), DmiInteger()).setMaxAccess("readonly")
if mibBuilder.loadTexts: a2Adpwritekbspersec.setStatus('mandatory')
a2Adpreadfailurespersec = MibTableColumn((1, 3, 6, 1, 4, 1, 16, 1, 2, 1, 2, 1, 16), DmiInteger()).setMaxAccess("readonly")
if mibBuilder.loadTexts: a2Adpreadfailurespersec.setStatus('mandatory')
a2Adpwritefailurespersec = MibTableColumn((1, 3, 6, 1, 4, 1, 16, 1, 2, 1, 2, 1, 17), DmiInteger()).setMaxAccess("readonly")
if mibBuilder.loadTexts: a2Adpwritefailurespersec.setStatus('mandatory')
a2Scanchannels = MibTableColumn((1, 3, 6, 1, 4, 1, 16, 1, 2, 1, 2, 1, 18), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("vScanover", 1), ("vStartscan", 2), ("vScaninprog", 3)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: a2Scanchannels.setStatus('mandatory')
a2Logicalview = MibTableColumn((1, 3, 6, 1, 4, 1, 16, 1, 2, 1, 2, 1, 19), DmiOctetstring()).setMaxAccess("readonly")
if mibBuilder.loadTexts: a2Logicalview.setStatus('mandatory')
a2Physicalview = MibTableColumn((1, 3, 6, 1, 4, 1, 16, 1, 2, 1, 2, 1, 20), DmiOctetstring()).setMaxAccess("readonly")
if mibBuilder.loadTexts: a2Physicalview.setStatus('mandatory')
tLogicalDriveInformation = MibTable((1, 3, 6, 1, 4, 1, 16, 1, 2, 1, 3), )
if mibBuilder.loadTexts: tLogicalDriveInformation.setStatus('mandatory')
eLogicalDriveInformation = MibTableRow((1, 3, 6, 1, 4, 1, 16, 1, 2, 1, 3, 1), ).setIndexNames((0, "AMIMEGARAIDMIF-MIB", "DmiComponentIndex"), (0, "AMIMEGARAIDMIF-MIB", "a3Ldadapternumber"), (0, "AMIMEGARAIDMIF-MIB", "a3Logicaldrivenumber"))
if mibBuilder.loadTexts: eLogicalDriveInformation.setStatus('mandatory')
a3Ldadapternumber = MibTableColumn((1, 3, 6, 1, 4, 1, 16, 1, 2, 1, 3, 1, 1), DmiInteger()).setMaxAccess("readonly")
if mibBuilder.loadTexts: a3Ldadapternumber.setStatus('mandatory')
a3Logicaldrivenumber = MibTableColumn((1, 3, 6, 1, 4, 1, 16, 1, 2, 1, 3, 1, 2), DmiInteger()).setMaxAccess("readonly")
if mibBuilder.loadTexts: a3Logicaldrivenumber.setStatus('mandatory')
a3Raidlevel = MibTableColumn((1, 3, 6, 1, 4, 1, 16, 1, 2, 1, 3, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1, 3, 5))).clone(namedValues=NamedValues(("vRaid0", 0), ("vRaid1", 1), ("vRaid3", 3), ("vRaid5", 5)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: a3Raidlevel.setStatus('mandatory')
a3Status = MibTableColumn((1, 3, 6, 1, 4, 1, 16, 1, 2, 1, 3, 1, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3, 4))).clone(namedValues=NamedValues(("vOffline", 0), ("vDegraded", 1), ("vOptimal", 2), ("vInitialize", 3), ("vCheckconsistency", 4)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: a3Status.setStatus('mandatory')
a3Sizeinmb = MibTableColumn((1, 3, 6, 1, 4, 1, 16, 1, 2, 1, 3, 1, 5), DmiInteger()).setMaxAccess("readonly")
if mibBuilder.loadTexts: a3Sizeinmb.setStatus('mandatory')
a3Stripesize = MibTableColumn((1, 3, 6, 1, 4, 1, 16, 1, 2, 1, 3, 1, 6), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(2, 4, 8, 16, 32, 64, 128, 256))).clone(namedValues=NamedValues(("vOnekb", 2), ("vTwokb", 4), ("vFourkb", 8), ("vEightkb", 16), ("vSixteenkb", 32), ("vThirtytwokb", 64), ("vSixtyfourkb", 128), ("vOnetwentyeightkb", 256)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: a3Stripesize.setStatus('mandatory')
a3Readpolicy = MibTableColumn((1, 3, 6, 1, 4, 1, 16, 1, 2, 1, 3, 1, 7), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1, 2))).clone(namedValues=NamedValues(("vNormal", 0), ("vReadahead", 1), ("vAdaptive", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: a3Readpolicy.setStatus('mandatory')
a3Writepolicy = MibTableColumn((1, 3, 6, 1, 4, 1, 16, 1, 2, 1, 3, 1, 8), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1))).clone(namedValues=NamedValues(("vWritethru", 0), ("vWriteback", 1)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: a3Writepolicy.setStatus('mandatory')
a3Cachepolicy = MibTableColumn((1, 3, 6, 1, 4, 1, 16, 1, 2, 1, 3, 1, 9), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1))).clone(namedValues=NamedValues(("vCachedio", 0), ("vDirectio", 1)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: a3Cachepolicy.setStatus('mandatory')
a3Numberofspans = MibTableColumn((1, 3, 6, 1, 4, 1, 16, 1, 2, 1, 3, 1, 10), DmiInteger()).setMaxAccess("readonly")
if mibBuilder.loadTexts: a3Numberofspans.setStatus('mandatory')
a3Numberofstripes = MibTableColumn((1, 3, 6, 1, 4, 1, 16, 1, 2, 1, 3, 1, 11), DmiInteger()).setMaxAccess("readonly")
if mibBuilder.loadTexts: a3Numberofstripes.setStatus('mandatory')
a3Ldioreadspersec = MibTableColumn((1, 3, 6, 1, 4, 1, 16, 1, 2, 1, 3, 1, 12), DmiInteger()).setMaxAccess("readonly")
if mibBuilder.loadTexts: a3Ldioreadspersec.setStatus('mandatory')
a3Ldiowritespersec = MibTableColumn((1, 3, 6, 1, 4, 1, 16, 1, 2, 1, 3, 1, 13), DmiInteger()).setMaxAccess("readonly")
if mibBuilder.loadTexts: a3Ldiowritespersec.setStatus('mandatory')
a3Ldreadskbspersec = MibTableColumn((1, 3, 6, 1, 4, 1, 16, 1, 2, 1, 3, 1, 14), DmiInteger()).setMaxAccess("readonly")
if mibBuilder.loadTexts: a3Ldreadskbspersec.setStatus('mandatory')
a3Ldwritekbspersec = MibTableColumn((1, 3, 6, 1, 4, 1, 16, 1, 2, 1, 3, 1, 15), DmiInteger()).setMaxAccess("readonly")
if mibBuilder.loadTexts: a3Ldwritekbspersec.setStatus('mandatory')
a3Ldioreadfailurespersec = MibTableColumn((1, 3, 6, 1, 4, 1, 16, 1, 2, 1, 3, 1, 16), DmiInteger()).setMaxAccess("readonly")
if mibBuilder.loadTexts: a3Ldioreadfailurespersec.setStatus('mandatory')
a3Ldwritefailurespersec = MibTableColumn((1, 3, 6, 1, 4, 1, 16, 1, 2, 1, 3, 1, 17), DmiInteger()).setMaxAccess("readonly")
if mibBuilder.loadTexts: a3Ldwritefailurespersec.setStatus('mandatory')
a3Progress = MibTableColumn((1, 3, 6, 1, 4, 1, 16, 1, 2, 1, 3, 1, 18), DmiInteger()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: a3Progress.setStatus('mandatory')
a3Allattributes = MibTableColumn((1, 3, 6, 1, 4, 1, 16, 1, 2, 1, 3, 1, 19), DmiOctetstring()).setMaxAccess("readonly")
if mibBuilder.loadTexts: a3Allattributes.setStatus('mandatory')
tPhysicalDeviceInformation = MibTable((1, 3, 6, 1, 4, 1, 16, 1, 2, 1, 4), )
if mibBuilder.loadTexts: tPhysicalDeviceInformation.setStatus('mandatory')
ePhysicalDeviceInformation = MibTableRow((1, 3, 6, 1, 4, 1, 16, 1, 2, 1, 4, 1), ).setIndexNames((0, "AMIMEGARAIDMIF-MIB", "DmiComponentIndex"), (0, "AMIMEGARAIDMIF-MIB", "a4Physadapternumber"), (0, "AMIMEGARAIDMIF-MIB", "a4Physchannel"), (0, "AMIMEGARAIDMIF-MIB", "a4Targetid"))
if mibBuilder.loadTexts: ePhysicalDeviceInformation.setStatus('mandatory')
a4Physadapternumber = MibTableColumn((1, 3, 6, 1, 4, 1, 16, 1, 2, 1, 4, 1, 1), DmiInteger()).setMaxAccess("readonly")
if mibBuilder.loadTexts: a4Physadapternumber.setStatus('mandatory')
a4Physchannel = MibTableColumn((1, 3, 6, 1, 4, 1, 16, 1, 2, 1, 4, 1, 2), DmiInteger()).setMaxAccess("readonly")
if mibBuilder.loadTexts: a4Physchannel.setStatus('mandatory')
a4Targetid = MibTableColumn((1, 3, 6, 1, 4, 1, 16, 1, 2, 1, 4, 1, 3), DmiInteger()).setMaxAccess("readonly")
if mibBuilder.loadTexts: a4Targetid.setStatus('mandatory')
a4State = MibTableColumn((1, 3, 6, 1, 4, 1, 16, 1, 2, 1, 4, 1, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 3, 4, 5, 6, 7))).clone(namedValues=NamedValues(("vReady", 1), ("vOnline", 3), ("vFailed", 4), ("vRebuild", 5), ("vHotspare", 6), ("vNotResponding", 7)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: a4State.setStatus('mandatory')
a4Arrayposition = MibTableColumn((1, 3, 6, 1, 4, 1, 16, 1, 2, 1, 4, 1, 5), DmiDisplaystring()).setMaxAccess("readonly")
if mibBuilder.loadTexts: a4Arrayposition.setStatus('mandatory')
a4Sizemb = MibTableColumn((1, 3, 6, 1, 4, 1, 16, 1, 2, 1, 4, 1, 6), DmiInteger()).setMaxAccess("readonly")
if mibBuilder.loadTexts: a4Sizemb.setStatus('mandatory')
a4Devicetype = MibTableColumn((1, 3, 6, 1, 4, 1, 16, 1, 2, 1, 4, 1, 7), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3, 4, 6, 7, 8, 9, 10, 11, 12, 13))).clone(namedValues=NamedValues(("vDisk", 0), ("vTape", 1), ("vPrinter", 2), ("vProcessor", 3), ("vWorm", 4), ("vScanner", 6), ("vOptical", 7), ("vChanger", 8), ("vCommunication", 9), ("vAsynchronouslow", 10), ("vAsynchronoushigh", 11), ("vReservedlow", 12), ("vNotResponding", 13)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: a4Devicetype.setStatus('mandatory')
a4Inquirystring = MibTableColumn((1, 3, 6, 1, 4, 1, 16, 1, 2, 1, 4, 1, 8), DmiDisplaystring()).setMaxAccess("readonly")
if mibBuilder.loadTexts: a4Inquirystring.setStatus('mandatory')
a4Scsilevel = MibTableColumn((1, 3, 6, 1, 4, 1, 16, 1, 2, 1, 4, 1, 9), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("vScsi1", 1), ("vScsi2", 2), ("vUnknown", 3)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: a4Scsilevel.setStatus('mandatory')
a4Syncnegotiation = MibTableColumn((1, 3, 6, 1, 4, 1, 16, 1, 2, 1, 4, 1, 10), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("vEnable", 1), ("vDisable", 2), ("vUnknown", 3)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: a4Syncnegotiation.setStatus('mandatory')
a4Qtags = MibTableColumn((1, 3, 6, 1, 4, 1, 16, 1, 2, 1, 4, 1, 11), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6))).clone(namedValues=NamedValues(("vOne", 1), ("vTwo", 2), ("vThree", 3), ("vFour", 4), ("vEnhancedqtagscheduling", 5), ("vUnknown", 6)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: a4Qtags.setStatus('mandatory')
a4Rebuildprogress = MibTableColumn((1, 3, 6, 1, 4, 1, 16, 1, 2, 1, 4, 1, 12), DmiInteger()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: a4Rebuildprogress.setStatus('mandatory')
a4Mediumerrors = MibTableColumn((1, 3, 6, 1, 4, 1, 16, 1, 2, 1, 4, 1, 13), DmiInteger()).setMaxAccess("readonly")
if mibBuilder.loadTexts: a4Mediumerrors.setStatus('mandatory')
a4Othererrors = MibTableColumn((1, 3, 6, 1, 4, 1, 16, 1, 2, 1, 4, 1, 14), DmiInteger()).setMaxAccess("readonly")
if mibBuilder.loadTexts: a4Othererrors.setStatus('mandatory')
a4Allattributes = MibTableColumn((1, 3, 6, 1, 4, 1, 16, 1, 2, 1, 4, 1, 15), DmiOctetstring()).setMaxAccess("readonly")
if mibBuilder.loadTexts: a4Allattributes.setStatus('mandatory')
tChannels = MibTable((1, 3, 6, 1, 4, 1, 16, 1, 2, 1, 5), )
if mibBuilder.loadTexts: tChannels.setStatus('mandatory')
eChannels = MibTableRow((1, 3, 6, 1, 4, 1, 16, 1, 2, 1, 5, 1), ).setIndexNames((0, "AMIMEGARAIDMIF-MIB", "DmiComponentIndex"), (0, "AMIMEGARAIDMIF-MIB", "a5Chanadapternumber"), (0, "AMIMEGARAIDMIF-MIB", "a5Channel"))
if mibBuilder.loadTexts: eChannels.setStatus('mandatory')
a5Chanadapternumber = MibTableColumn((1, 3, 6, 1, 4, 1, 16, 1, 2, 1, 5, 1, 1), DmiInteger()).setMaxAccess("readonly")
if mibBuilder.loadTexts: a5Chanadapternumber.setStatus('mandatory')
a5Channel = MibTableColumn((1, 3, 6, 1, 4, 1, 16, 1, 2, 1, 5, 1, 2), DmiInteger()).setMaxAccess("readonly")
if mibBuilder.loadTexts: a5Channel.setStatus('mandatory')
a5Terminations = MibTableColumn((1, 3, 6, 1, 4, 1, 16, 1, 2, 1, 5, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1, 2))).clone(namedValues=NamedValues(("vDisabled", 0), ("vHigher8bits", 1), ("vWideterminations", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: a5Terminations.setStatus('mandatory')
a5Channelstatus = MibTableColumn((1, 3, 6, 1, 4, 1, 16, 1, 2, 1, 5, 1, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1))).clone(namedValues=NamedValues(("vQuit", 0), ("vActive", 1)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: a5Channelstatus.setStatus('mandatory')
tAlertManagementInformation = MibTable((1, 3, 6, 1, 4, 1, 16, 1, 2, 1, 6), )
if mibBuilder.loadTexts: tAlertManagementInformation.setStatus('mandatory')
eAlertManagementInformation = MibTableRow((1, 3, 6, 1, 4, 1, 16, 1, 2, 1, 6, 1), ).setIndexNames((0, "AMIMEGARAIDMIF-MIB", "DmiComponentIndex"))
if mibBuilder.loadTexts: eAlertManagementInformation.setStatus('mandatory')
a6Dmiindication = MibTableColumn((1, 3, 6, 1, 4, 1, 16, 1, 2, 1, 6, 1, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1))).clone(namedValues=NamedValues(("vDisabled", 0), ("vEnabled", 1)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: a6Dmiindication.setStatus('mandatory')
a6Ams2alerts = MibTableColumn((1, 3, 6, 1, 4, 1, 16, 1, 2, 1, 6, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1))).clone(namedValues=NamedValues(("vDisabled", 0), ("vEnabled", 1)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: a6Ams2alerts.setStatus('mandatory')
a6Eventlog = MibTableColumn((1, 3, 6, 1, 4, 1, 16, 1, 2, 1, 6, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1))).clone(namedValues=NamedValues(("vDisabled", 0), ("vEnabled", 1)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: a6Eventlog.setStatus('mandatory')
tGlobalinfo = MibTable((1, 3, 6, 1, 4, 1, 16, 1, 2, 1, 7), )
if mibBuilder.loadTexts: tGlobalinfo.setStatus('mandatory')
eGlobalinfo = MibTableRow((1, 3, 6, 1, 4, 1, 16, 1, 2, 1, 7, 1), ).setIndexNames((0, "AMIMEGARAIDMIF-MIB", "DmiComponentIndex"))
if mibBuilder.loadTexts: eGlobalinfo.setStatus('mandatory')
a7Globalcltrinfo = MibTableColumn((1, 3, 6, 1, 4, 1, 16, 1, 2, 1, 7, 1, 1), DmiOctetstring()).setMaxAccess("readonly")
if mibBuilder.loadTexts: a7Globalcltrinfo.setStatus('mandatory')
tMiftomib = MibTable((1, 3, 6, 1, 4, 1, 16, 1, 2, 1, 99), )
if mibBuilder.loadTexts: tMiftomib.setStatus('mandatory')
eMiftomib = MibTableRow((1, 3, 6, 1, 4, 1, 16, 1, 2, 1, 99, 1), ).setIndexNames((0, "AMIMEGARAIDMIF-MIB", "DmiComponentIndex"))
if mibBuilder.loadTexts: eMiftomib.setStatus('mandatory')
a99AmiMegaraidMib = MibTableColumn((1, 3, 6, 1, 4, 1, 16, 1, 2, 1, 99, 1, 1), DmiDisplaystring()).setMaxAccess("readonly")
if mibBuilder.loadTexts: a99AmiMegaraidMib.setStatus('mandatory')
a99MibOid = MibTableColumn((1, 3, 6, 1, 4, 1, 16, 1, 2, 1, 99, 1, 2), DmiDisplaystring()).setMaxAccess("readonly")
if mibBuilder.loadTexts: a99MibOid.setStatus('mandatory')
a99DisableTraps = MibTableColumn((1, 3, 6, 1, 4, 1, 16, 1, 2, 1, 99, 1, 3), DmiInteger()).setMaxAccess("readonly")
if mibBuilder.loadTexts: a99DisableTraps.setStatus('mandatory')
tCompositeDriveAlerts = MibTable((1, 3, 6, 1, 4, 1, 16, 1, 2, 1, 103), )
if mibBuilder.loadTexts: tCompositeDriveAlerts.setStatus('mandatory')
eCompositeDriveAlerts = MibTableRow((1, 3, 6, 1, 4, 1, 16, 1, 2, 1, 103, 1), ).setIndexNames((0, "AMIMEGARAIDMIF-MIB", "DmiComponentIndex"), (0, "AMIMEGARAIDMIF-MIB", "a103AssociatedGroup"))
if mibBuilder.loadTexts: eCompositeDriveAlerts.setStatus('mandatory')
a103EventType = MibTableColumn((1, 3, 6, 1, 4, 1, 16, 1, 2, 1, 103, 1, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("vCompositeDriveStatusChange", 1), ("vCompositeDriveRecoveryStarted", 2), ("vCompositeDriveRecoveryCompleted", 3)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: a103EventType.setStatus('mandatory')
a103EventSeverity = MibTableColumn((1, 3, 6, 1, 4, 1, 16, 1, 2, 1, 103, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 4, 8, 10, 12))).clone(namedValues=NamedValues(("vMonitor", 1), ("vInformation", 2), ("vOk", 4), ("vNon-critical", 8), ("vCritical", 10), ("vNon-recoverable", 12)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: a103EventSeverity.setStatus('mandatory')
a103IsEventStateBased = MibTableColumn((1, 3, 6, 1, 4, 1, 16, 1, 2, 1, 103, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1))).clone(namedValues=NamedValues(("vFalse", 0), ("vTrue", 1)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: a103IsEventStateBased.setStatus('mandatory')
a103EventStateKey = MibTableColumn((1, 3, 6, 1, 4, 1, 16, 1, 2, 1, 103, 1, 4), DmiInteger()).setMaxAccess("readonly")
if mibBuilder.loadTexts: a103EventStateKey.setStatus('mandatory')
a103AssociatedGroup = MibTableColumn((1, 3, 6, 1, 4, 1, 16, 1, 2, 1, 103, 1, 5), DmiDisplaystring()).setMaxAccess("readonly")
if mibBuilder.loadTexts: a103AssociatedGroup.setStatus('mandatory')
a103EventSystem = MibTableColumn((1, 3, 6, 1, 4, 1, 16, 1, 2, 1, 103, 1, 6), DmiInteger()).setMaxAccess("readonly")
if mibBuilder.loadTexts: a103EventSystem.setStatus('mandatory')
a103EventSubsystem = MibTableColumn((1, 3, 6, 1, 4, 1, 16, 1, 2, 1, 103, 1, 7), DmiInteger()).setMaxAccess("readonly")
if mibBuilder.loadTexts: a103EventSubsystem.setStatus('mandatory')
a103EventSolution = MibTableColumn((1, 3, 6, 1, 4, 1, 16, 1, 2, 1, 103, 1, 8), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("vOther", 1), ("vUnknown", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: a103EventSolution.setStatus('mandatory')
a103InstanceDataPresent = MibTableColumn((1, 3, 6, 1, 4, 1, 16, 1, 2, 1, 103, 1, 9), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1))).clone(namedValues=NamedValues(("vFalse", 0), ("vTrue", 1)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: a103InstanceDataPresent.setStatus('mandatory')
a103VendorSpecificMessage = MibTableColumn((1, 3, 6, 1, 4, 1, 16, 1, 2, 1, 103, 1, 10), DmiOctetstring()).setMaxAccess("readonly")
if mibBuilder.loadTexts: a103VendorSpecificMessage.setStatus('mandatory')
a103VendorSpecificData = MibTableColumn((1, 3, 6, 1, 4, 1, 16, 1, 2, 1, 103, 1, 11), DmiOctetstring()).setMaxAccess("readonly")
if mibBuilder.loadTexts: a103VendorSpecificData.setStatus('mandatory')
a103VendorTrapNumber = MibTableColumn((1, 3, 6, 1, 4, 1, 16, 1, 2, 1, 103, 1, 12), DmiInteger()).setMaxAccess("readonly")
if mibBuilder.loadTexts: a103VendorTrapNumber.setStatus('mandatory')
tPhysicalDriveAlerts = MibTable((1, 3, 6, 1, 4, 1, 16, 1, 2, 1, 104), )
if mibBuilder.loadTexts: tPhysicalDriveAlerts.setStatus('mandatory')
ePhysicalDriveAlerts = MibTableRow((1, 3, 6, 1, 4, 1, 16, 1, 2, 1, 104, 1), ).setIndexNames((0, "AMIMEGARAIDMIF-MIB", "DmiComponentIndex"), (0, "AMIMEGARAIDMIF-MIB", "a104AssociatedGroup"))
if mibBuilder.loadTexts: ePhysicalDriveAlerts.setStatus('mandatory')
a104EventType = MibTableColumn((1, 3, 6, 1, 4, 1, 16, 1, 2, 1, 104, 1, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))).clone(namedValues=NamedValues(("vPhysicalDriveStatusChange", 1), ("vPhysicalDriveRemoved", 2), ("vPhysicalDriveAppeared", 3), ("vHotSpareCreated", 4)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: a104EventType.setStatus('mandatory')
a104EventSeverity = MibTableColumn((1, 3, 6, 1, 4, 1, 16, 1, 2, 1, 104, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 4, 8, 10, 12))).clone(namedValues=NamedValues(("vMonitor", 1), ("vInformation", 2), ("vOk", 4), ("vNon-critical", 8), ("vCritical", 10), ("vNon-recoverable", 12)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: a104EventSeverity.setStatus('mandatory')
a104IsEventStateBased = MibTableColumn((1, 3, 6, 1, 4, 1, 16, 1, 2, 1, 104, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1))).clone(namedValues=NamedValues(("vFalse", 0), ("vTrue", 1)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: a104IsEventStateBased.setStatus('mandatory')
a104EventStateKey = MibTableColumn((1, 3, 6, 1, 4, 1, 16, 1, 2, 1, 104, 1, 4), DmiInteger()).setMaxAccess("readonly")
if mibBuilder.loadTexts: a104EventStateKey.setStatus('mandatory')
a104AssociatedGroup = MibTableColumn((1, 3, 6, 1, 4, 1, 16, 1, 2, 1, 104, 1, 5), DmiDisplaystring()).setMaxAccess("readonly")
if mibBuilder.loadTexts: a104AssociatedGroup.setStatus('mandatory')
a104EventSystem = MibTableColumn((1, 3, 6, 1, 4, 1, 16, 1, 2, 1, 104, 1, 6), DmiInteger()).setMaxAccess("readonly")
if mibBuilder.loadTexts: a104EventSystem.setStatus('mandatory')
a104EventSubsystem = MibTableColumn((1, 3, 6, 1, 4, 1, 16, 1, 2, 1, 104, 1, 7), DmiInteger()).setMaxAccess("readonly")
if mibBuilder.loadTexts: a104EventSubsystem.setStatus('mandatory')
a104EventSolution = MibTableColumn((1, 3, 6, 1, 4, 1, 16, 1, 2, 1, 104, 1, 8), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("vOther", 1), ("vUnknown", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: a104EventSolution.setStatus('mandatory')
a104InstanceDataPresent = MibTableColumn((1, 3, 6, 1, 4, 1, 16, 1, 2, 1, 104, 1, 9), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1))).clone(namedValues=NamedValues(("vFalse", 0), ("vTrue", 1)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: a104InstanceDataPresent.setStatus('mandatory')
a104VendorSpecificMessage = MibTableColumn((1, 3, 6, 1, 4, 1, 16, 1, 2, 1, 104, 1, 10), DmiOctetstring()).setMaxAccess("readonly")
if mibBuilder.loadTexts: a104VendorSpecificMessage.setStatus('mandatory')
a104VendorSpecificData = MibTableColumn((1, 3, 6, 1, 4, 1, 16, 1, 2, 1, 104, 1, 11), DmiOctetstring()).setMaxAccess("readonly")
if mibBuilder.loadTexts: a104VendorSpecificData.setStatus('mandatory')
a104VendorTrapNumber = MibTableColumn((1, 3, 6, 1, 4, 1, 16, 1, 2, 1, 104, 1, 12), DmiInteger()).setMaxAccess("readonly")
if mibBuilder.loadTexts: a104VendorTrapNumber.setStatus('mandatory')
mibBuilder.exportSymbols("AMIMEGARAIDMIF-MIB", eChannels=eChannels, a5Channelstatus=a5Channelstatus, a103AssociatedGroup=a103AssociatedGroup, a103IsEventStateBased=a103IsEventStateBased, eComponentid=eComponentid, a1SerialNumber=a1SerialNumber, a4Physadapternumber=a4Physadapternumber, a3Numberofspans=a3Numberofspans, a103VendorSpecificMessage=a103VendorSpecificMessage, a103EventSolution=a103EventSolution, megaraid=megaraid, a1Version=a1Version, a1Manufacturer=a1Manufacturer, a1Installation=a1Installation, DmiOctetstring=DmiOctetstring, tAlertManagementInformation=tAlertManagementInformation, a2Flushinterval=a2Flushinterval, a4Physchannel=a4Physchannel, a7Globalcltrinfo=a7Globalcltrinfo, DmiDateX=DmiDateX, tPhysicalDeviceInformation=tPhysicalDeviceInformation, a3Ldioreadfailurespersec=a3Ldioreadfailurespersec, a103InstanceDataPresent=a103InstanceDataPresent, a99DisableTraps=a99DisableTraps, a2Adpwritekbspersec=a2Adpwritekbspersec, a3Writepolicy=a3Writepolicy, a4Targetid=a4Targetid, eMiftomib=eMiftomib, DmiComponentIndex=DmiComponentIndex, DmiInteger=DmiInteger, eCompositeDriveAlerts=eCompositeDriveAlerts, a2Adpreadkbspersec=a2Adpreadkbspersec, a4Syncnegotiation=a4Syncnegotiation, a2Rebuildrateinpercent=a2Rebuildrateinpercent, a4Scsilevel=a4Scsilevel, a4Rebuildprogress=a4Rebuildprogress, tGlobalinfo=tGlobalinfo, a104EventSolution=a104EventSolution, a4Mediumerrors=a4Mediumerrors, a103EventSeverity=a103EventSeverity, a6Dmiindication=a6Dmiindication, a2Maxconcurrentcmds=a2Maxconcurrentcmds, a2Numlogicaldrives=a2Numlogicaldrives, eLogicalDriveInformation=eLogicalDriveInformation, a2Chipsettype=a2Chipsettype, tPhysicalDriveAlerts=tPhysicalDriveAlerts, a104AssociatedGroup=a104AssociatedGroup, a2Biosversion=a2Biosversion, tControllerInformation=tControllerInformation, tCompositeDriveAlerts=tCompositeDriveAlerts, a3Readpolicy=a3Readpolicy, a104EventSystem=a104EventSystem, a1Verify=a1Verify, a3Logicaldrivenumber=a3Logicaldrivenumber, tLogicalDriveInformation=tLogicalDriveInformation, a2Spinupdelay=a2Spinupdelay, a104VendorSpecificMessage=a104VendorSpecificMessage, a104VendorSpecificData=a104VendorSpecificData, a104EventSubsystem=a104EventSubsystem, a3Ldreadskbspersec=a3Ldreadskbspersec, a103VendorSpecificData=a103VendorSpecificData, dmtfGroups=dmtfGroups, a4Sizemb=a4Sizemb, a3Progress=a3Progress, eControllerInformation=eControllerInformation, tChannels=tChannels, a3Ldadapternumber=a3Ldadapternumber, a104InstanceDataPresent=a104InstanceDataPresent, a4Qtags=a4Qtags, tComponentid=tComponentid, a2Adpadapternumber=a2Adpadapternumber, a4Arrayposition=a4Arrayposition, eGlobalinfo=eGlobalinfo, a4State=a4State, a2Adpwritefailurespersec=a2Adpwritefailurespersec, a1Product=a1Product, a2Firmwareversion=a2Firmwareversion, a2Physicalview=a2Physicalview, a2Scanchannels=a2Scanchannels, a3Numberofstripes=a3Numberofstripes, a2Adpiowritespersec=a2Adpiowritespersec, a5Channel=a5Channel, a3Allattributes=a3Allattributes, a2Logicalview=a2Logicalview, a4Inquirystring=a4Inquirystring, a3Raidlevel=a3Raidlevel, DmiDisplaystring=DmiDisplaystring, a104EventStateKey=a104EventStateKey, a2Spinupcount=a2Spinupcount, a3Ldwritekbspersec=a3Ldwritekbspersec, a104VendorTrapNumber=a104VendorTrapNumber, a4Othererrors=a4Othererrors, a99MibOid=a99MibOid, a5Chanadapternumber=a5Chanadapternumber, a3Cachepolicy=a3Cachepolicy, mifmib=mifmib, eAlertManagementInformation=eAlertManagementInformation, a3Ldioreadspersec=a3Ldioreadspersec, ePhysicalDeviceInformation=ePhysicalDeviceInformation, a4Allattributes=a4Allattributes, tMiftomib=tMiftomib, a3Sizeinmb=a3Sizeinmb, a104EventType=a104EventType, a4Devicetype=a4Devicetype, a5Terminations=a5Terminations, a103EventType=a103EventType, a103VendorTrapNumber=a103VendorTrapNumber, a103EventSystem=a103EventSystem, ami=ami, ePhysicalDriveAlerts=ePhysicalDriveAlerts, a6Ams2alerts=a6Ams2alerts, a103EventSubsystem=a103EventSubsystem, a104IsEventStateBased=a104IsEventStateBased, a103EventStateKey=a103EventStateKey, a3Stripesize=a3Stripesize, a99AmiMegaraidMib=a99AmiMegaraidMib, a3Status=a3Status, a104EventSeverity=a104EventSeverity, a2Dramsizeinmb=a2Dramsizeinmb, a2Adpreadfailurespersec=a2Adpreadfailurespersec, a2Adpioreadspersec=a2Adpioreadspersec, a6Eventlog=a6Eventlog, a3Ldwritefailurespersec=a3Ldwritefailurespersec, a3Ldiowritespersec=a3Ldiowritespersec)
