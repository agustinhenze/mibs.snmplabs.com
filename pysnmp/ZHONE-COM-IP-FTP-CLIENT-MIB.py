#
# PySNMP MIB module ZHONE-COM-IP-FTP-CLIENT-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/ZHONE-COM-IP-FTP-CLIENT-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 21:40:46 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
OctetString, ObjectIdentifier, Integer = mibBuilder.importSymbols("ASN1", "OctetString", "ObjectIdentifier", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
SingleValueConstraint, ValueSizeConstraint, ConstraintsIntersection, ConstraintsUnion, ValueRangeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "SingleValueConstraint", "ValueSizeConstraint", "ConstraintsIntersection", "ConstraintsUnion", "ValueRangeConstraint")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
TimeTicks, NotificationType, Integer32, MibScalar, MibTable, MibTableRow, MibTableColumn, ModuleIdentity, ObjectIdentity, Bits, Gauge32, Counter32, Counter64, IpAddress, Unsigned32, MibIdentifier, iso = mibBuilder.importSymbols("SNMPv2-SMI", "TimeTicks", "NotificationType", "Integer32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "ModuleIdentity", "ObjectIdentity", "Bits", "Gauge32", "Counter32", "Counter64", "IpAddress", "Unsigned32", "MibIdentifier", "iso")
TextualConvention, DisplayString, TimeStamp = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString", "TimeStamp")
zhoneModules, zhoneIp = mibBuilder.importSymbols("Zhone", "zhoneModules", "zhoneIp")
ZhoneFileName, ZhoneAdminString, ZhoneRowStatus = mibBuilder.importSymbols("Zhone-TC", "ZhoneFileName", "ZhoneAdminString", "ZhoneRowStatus")
comIpFtpClient = ModuleIdentity((1, 3, 6, 1, 4, 1, 5504, 6, 68))
comIpFtpClient.setRevisions(('2001-01-11 15:59', '2000-09-18 11:13',))
if mibBuilder.loadTexts: comIpFtpClient.setLastUpdated('200101081559Z')
if mibBuilder.loadTexts: comIpFtpClient.setOrganization('Zhone Technologies, Inc.')
ftpClient = ObjectIdentity((1, 3, 6, 1, 4, 1, 5504, 4, 1, 18))
if mibBuilder.loadTexts: ftpClient.setStatus('current')
ftpClientNextIndex = MibScalar((1, 3, 6, 1, 4, 1, 5504, 4, 1, 18, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 20))).setMaxAccess("readonly")
if mibBuilder.loadTexts: ftpClientNextIndex.setStatus('current')
ftpClientHighRequests = MibScalar((1, 3, 6, 1, 4, 1, 5504, 4, 1, 18, 2), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ftpClientHighRequests.setStatus('current')
ftpClientAutoRemovals = MibScalar((1, 3, 6, 1, 4, 1, 5504, 4, 1, 18, 3), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ftpClientAutoRemovals.setStatus('current')
ftpClientIndexFailures = MibScalar((1, 3, 6, 1, 4, 1, 5504, 4, 1, 18, 4), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ftpClientIndexFailures.setStatus('current')
ftpClientRequestTable = MibTable((1, 3, 6, 1, 4, 1, 5504, 4, 1, 18, 5), )
if mibBuilder.loadTexts: ftpClientRequestTable.setStatus('current')
ftpClientRequestEntry = MibTableRow((1, 3, 6, 1, 4, 1, 5504, 4, 1, 18, 5, 1), ).setIndexNames((0, "ZHONE-COM-IP-FTP-CLIENT-MIB", "ftpClientRequestIndex"))
if mibBuilder.loadTexts: ftpClientRequestEntry.setStatus('current')
ftpClientRequestIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 5504, 4, 1, 18, 5, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 20)))
if mibBuilder.loadTexts: ftpClientRequestIndex.setStatus('current')
ftpClientRequestCode = MibTableColumn((1, 3, 6, 1, 4, 1, 5504, 4, 1, 18, 5, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))).clone(namedValues=NamedValues(("putBinary", 1), ("putAscii", 2), ("getBinary", 3), ("getAscii", 4))).clone('putBinary')).setMaxAccess("readcreate")
if mibBuilder.loadTexts: ftpClientRequestCode.setStatus('current')
ftpClientRequestLocalFileName = MibTableColumn((1, 3, 6, 1, 4, 1, 5504, 4, 1, 18, 5, 1, 3), ZhoneFileName()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: ftpClientRequestLocalFileName.setStatus('current')
ftpClientRequestRemoteFileName = MibTableColumn((1, 3, 6, 1, 4, 1, 5504, 4, 1, 18, 5, 1, 4), ZhoneFileName()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: ftpClientRequestRemoteFileName.setStatus('current')
ftpClientRequestServerAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 5504, 4, 1, 18, 5, 1, 5), ZhoneAdminString()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: ftpClientRequestServerAddress.setStatus('current')
ftpClientRequestUserName = MibTableColumn((1, 3, 6, 1, 4, 1, 5504, 4, 1, 18, 5, 1, 6), ZhoneAdminString()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: ftpClientRequestUserName.setStatus('current')
ftpClientRequestPassword = MibTableColumn((1, 3, 6, 1, 4, 1, 5504, 4, 1, 18, 5, 1, 7), ZhoneAdminString()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: ftpClientRequestPassword.setStatus('current')
ftpClientRequestResult = MibTableColumn((1, 3, 6, 1, 4, 1, 5504, 4, 1, 18, 5, 1, 8), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 8, 9, 10))).clone(namedValues=NamedValues(("inProgress", 1), ("success", 2), ("stoppedByUser", 3), ("localFileNameError", 4), ("remoteFileNameError", 5), ("unreachableDestination", 6), ("invalidUserNamePassword", 7), ("tooManyOpenFiles", 8), ("readError", 9), ("writeError", 10)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: ftpClientRequestResult.setStatus('current')
ftpClientRequestAction = MibTableColumn((1, 3, 6, 1, 4, 1, 5504, 4, 1, 18, 5, 1, 9), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("start", 1), ("stop", 2))).clone('start')).setMaxAccess("readcreate")
if mibBuilder.loadTexts: ftpClientRequestAction.setStatus('current')
ftpClientRequestCompletionTime = MibTableColumn((1, 3, 6, 1, 4, 1, 5504, 4, 1, 18, 5, 1, 10), TimeStamp()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ftpClientRequestCompletionTime.setStatus('current')
ftpClientRequestRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 5504, 4, 1, 18, 5, 1, 11), ZhoneRowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: ftpClientRequestRowStatus.setStatus('current')
mibBuilder.exportSymbols("ZHONE-COM-IP-FTP-CLIENT-MIB", ftpClientRequestEntry=ftpClientRequestEntry, ftpClientNextIndex=ftpClientNextIndex, ftpClientRequestCode=ftpClientRequestCode, ftpClientRequestAction=ftpClientRequestAction, ftpClientRequestLocalFileName=ftpClientRequestLocalFileName, ftpClientAutoRemovals=ftpClientAutoRemovals, ftpClientRequestServerAddress=ftpClientRequestServerAddress, ftpClientRequestTable=ftpClientRequestTable, ftpClient=ftpClient, ftpClientIndexFailures=ftpClientIndexFailures, PYSNMP_MODULE_ID=comIpFtpClient, ftpClientRequestResult=ftpClientRequestResult, ftpClientRequestRemoteFileName=ftpClientRequestRemoteFileName, ftpClientRequestRowStatus=ftpClientRequestRowStatus, comIpFtpClient=comIpFtpClient, ftpClientHighRequests=ftpClientHighRequests, ftpClientRequestUserName=ftpClientRequestUserName, ftpClientRequestIndex=ftpClientRequestIndex, ftpClientRequestPassword=ftpClientRequestPassword, ftpClientRequestCompletionTime=ftpClientRequestCompletionTime)