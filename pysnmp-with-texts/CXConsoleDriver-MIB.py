#
# PySNMP MIB module CXConsoleDriver-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/CXConsoleDriver-MIB
# Produced by pysmi-0.3.4 at Wed May  1 12:32:28 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
Integer, OctetString, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "Integer", "OctetString", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ValueRangeConstraint, SingleValueConstraint, ConstraintsIntersection, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsIntersection", "ConstraintsUnion")
cxConsoleDriver, = mibBuilder.importSymbols("CXProduct-SMI", "cxConsoleDriver")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
Counter64, Gauge32, TimeTicks, MibScalar, MibTable, MibTableRow, MibTableColumn, IpAddress, Unsigned32, Integer32, ModuleIdentity, NotificationType, ObjectIdentity, MibIdentifier, Counter32, iso, Bits = mibBuilder.importSymbols("SNMPv2-SMI", "Counter64", "Gauge32", "TimeTicks", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "IpAddress", "Unsigned32", "Integer32", "ModuleIdentity", "NotificationType", "ObjectIdentity", "MibIdentifier", "Counter32", "iso", "Bits")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
cxCdBaudRate = MibScalar((1, 3, 6, 1, 4, 1, 495, 2, 1, 5, 6, 1), Integer32().clone(9600)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cxCdBaudRate.setStatus('mandatory')
if mibBuilder.loadTexts: cxCdBaudRate.setDescription('Determines the baud rate of the console port. The setting of this object is dynamic. The console port immediately implements the option you enter. Options: 9600 19200 38400 115200 Default Value: 9600 Configuration Changed: operative')
cxCdCharSize = MibScalar((1, 3, 6, 1, 4, 1, 495, 2, 1, 5, 6, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(7, 8)).clone(8)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cxCdCharSize.setStatus('mandatory')
if mibBuilder.loadTexts: cxCdCharSize.setDescription('Determines how many bits constitute a character for the console port. Options: none - the value is fixed at 8 Default Value: 8 Configuration Changed: none ')
cxCdParity = MibScalar((1, 3, 6, 1, 4, 1, 495, 2, 1, 5, 6, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("noParity", 1), ("evenParity", 2), ("oddParity", 3))).clone('noParity')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cxCdParity.setStatus('mandatory')
if mibBuilder.loadTexts: cxCdParity.setDescription('Determines the parity scheme the CPU uses to validate the characters it receives through the console port. Options: none - the value is fixed at noParity Default Value: noParity Configuration Changed: none ')
cxCdStopBit = MibScalar((1, 3, 6, 1, 4, 1, 495, 2, 1, 5, 6, 4), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 2)).clone(1)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cxCdStopBit.setStatus('mandatory')
if mibBuilder.loadTexts: cxCdStopBit.setDescription('Determines how many stop bits are at the end of each character the console port receives. Options: none - the value is fixed at 1 Default Value: 1 Configuration Changed: none ')
cxCdProtocol = MibScalar((1, 3, 6, 1, 4, 1, 495, 2, 1, 5, 6, 5), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("localConsole", 1), ("ppp", 2))).clone('localConsole')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cxCdProtocol.setStatus('mandatory')
if mibBuilder.loadTexts: cxCdProtocol.setDescription('Determines the protocol (configuration method) for the console port. The setting of this object is dynamic. The console port immediately implements the option you enter. However, if you change the protocol you are currently using to configure the port your connection will be lost. Options: localConsole (1): you use this protocol when you attach a TTY terminal directly to the console port. This protocol requires you to use command line configuration. You also must enter a password to gain access to the configuration tables. You can define the password using the object uiPassword of the CXUserInterface Table. ppp (2): you use this protocol when you are configuring via a windows-based application such as HP/OV (Hewlett Packard-OpenView). Default Value: ppp (2) Configuration Changed: operative')
mibBuilder.exportSymbols("CXConsoleDriver-MIB", cxCdParity=cxCdParity, cxCdProtocol=cxCdProtocol, cxCdBaudRate=cxCdBaudRate, cxCdStopBit=cxCdStopBit, cxCdCharSize=cxCdCharSize)
