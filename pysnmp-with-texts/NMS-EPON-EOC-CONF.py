#
# PySNMP MIB module NMS-EPON-EOC-CONF (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/NMS-EPON-EOC-CONF
# Produced by pysmi-0.3.4 at Wed May  1 14:21:33 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
OctetString, Integer, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "OctetString", "Integer", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ValueRangeConstraint, ValueSizeConstraint, ConstraintsUnion, SingleValueConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ValueRangeConstraint", "ValueSizeConstraint", "ConstraintsUnion", "SingleValueConstraint")
nmsEPONGroup, = mibBuilder.importSymbols("NMS-SMI", "nmsEPONGroup")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
iso, TimeTicks, Counter32, Counter64, MibIdentifier, IpAddress, MibScalar, MibTable, MibTableRow, MibTableColumn, ModuleIdentity, NotificationType, Unsigned32, ObjectIdentity, Bits, Integer32, Gauge32 = mibBuilder.importSymbols("SNMPv2-SMI", "iso", "TimeTicks", "Counter32", "Counter64", "MibIdentifier", "IpAddress", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "ModuleIdentity", "NotificationType", "Unsigned32", "ObjectIdentity", "Bits", "Integer32", "Gauge32")
TextualConvention, RowStatus, TruthValue, PhysAddress, MacAddress, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "RowStatus", "TruthValue", "PhysAddress", "MacAddress", "DisplayString")
nmsEponEocConfig = MibIdentifier((1, 3, 6, 1, 4, 1, 11606, 10, 101, 32))
nmsEponEocTftpOper = MibIdentifier((1, 3, 6, 1, 4, 1, 11606, 10, 101, 32, 1))
tftpServerIpAddr = MibScalar((1, 3, 6, 1, 4, 1, 11606, 10, 101, 32, 1, 1), IpAddress()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: tftpServerIpAddr.setStatus('mandatory')
if mibBuilder.loadTexts: tftpServerIpAddr.setDescription('Remot TFTP server IP address. This value only effects after tftpAction is set.')
tftpServerSourceFileName = MibScalar((1, 3, 6, 1, 4, 1, 11606, 10, 101, 32, 1, 2), OctetString()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: tftpServerSourceFileName.setStatus('mandatory')
if mibBuilder.loadTexts: tftpServerSourceFileName.setDescription('TFTP server source file name. This value only effects after tftpAction is set.')
tftpServerDestFileName = MibScalar((1, 3, 6, 1, 4, 1, 11606, 10, 101, 32, 1, 3), OctetString()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: tftpServerDestFileName.setStatus('mandatory')
if mibBuilder.loadTexts: tftpServerDestFileName.setDescription('TFTP server destination file name. This value only effects after tftpAction is set.')
tftpServerOper = MibScalar((1, 3, 6, 1, 4, 1, 11606, 10, 101, 32, 1, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1, 2))).clone(namedValues=NamedValues(("no_operation", 0), ("upload_to_onu", 1), ("download_from_onu", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: tftpServerOper.setStatus('mandatory')
if mibBuilder.loadTexts: tftpServerOper.setDescription('TFTP server operation. When the value is set, ths tftpServerIpAddr, tftpServerSourceFileName and tftpServerDestFileName effects at ths same time.')
nmsEponEocBlackWhiteListTable = MibTable((1, 3, 6, 1, 4, 1, 11606, 10, 101, 32, 2), )
if mibBuilder.loadTexts: nmsEponEocBlackWhiteListTable.setStatus('mandatory')
if mibBuilder.loadTexts: nmsEponEocBlackWhiteListTable.setDescription('A list of epon EoC Black White List table.')
nmsEponEocBlackWhiteListEntry = MibTableRow((1, 3, 6, 1, 4, 1, 11606, 10, 101, 32, 2, 1), ).setIndexNames((0, "NMS-EPON-EOC-CONF", "authMode"), (0, "NMS-EPON-EOC-CONF", "macAddr"))
if mibBuilder.loadTexts: nmsEponEocBlackWhiteListEntry.setStatus('mandatory')
if mibBuilder.loadTexts: nmsEponEocBlackWhiteListEntry.setDescription('A collection of Eoc Black White List property.')
authMode = MibTableColumn((1, 3, 6, 1, 4, 1, 11606, 10, 101, 32, 2, 1, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("black_list", 1), ("white_list", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: authMode.setStatus('mandatory')
if mibBuilder.loadTexts: authMode.setDescription('EPON EoC authentication mode. black_list(1), white_list(2). ')
macAddr = MibTableColumn((1, 3, 6, 1, 4, 1, 11606, 10, 101, 32, 2, 1, 2), MacAddress()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: macAddr.setStatus('mandatory')
if mibBuilder.loadTexts: macAddr.setDescription('EPON EoC master MAC address.')
listOper = MibScalar((1, 3, 6, 1, 4, 1, 11606, 10, 101, 32, 2, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1, 2))).clone(namedValues=NamedValues(("no_action", 0), ("add_list", 1), ("delete_list", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: listOper.setStatus('mandatory')
if mibBuilder.loadTexts: listOper.setDescription('EPON EoC white and black list operation. no_action(0), add_list(1),delete_list(2). ')
mibBuilder.exportSymbols("NMS-EPON-EOC-CONF", nmsEponEocBlackWhiteListEntry=nmsEponEocBlackWhiteListEntry, nmsEponEocConfig=nmsEponEocConfig, nmsEponEocBlackWhiteListTable=nmsEponEocBlackWhiteListTable, tftpServerOper=tftpServerOper, nmsEponEocTftpOper=nmsEponEocTftpOper, tftpServerDestFileName=tftpServerDestFileName, tftpServerSourceFileName=tftpServerSourceFileName, tftpServerIpAddr=tftpServerIpAddr, authMode=authMode, listOper=listOper, macAddr=macAddr)
