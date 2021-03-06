#
# PySNMP MIB module STACK-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/STACK-MIB
# Produced by pysmi-0.3.4 at Wed May  1 15:10:55 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
SingleValueConstraint, ConstraintsIntersection, ValueSizeConstraint, ConstraintsUnion, ValueRangeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "SingleValueConstraint", "ConstraintsIntersection", "ValueSizeConstraint", "ConstraintsUnion", "ValueRangeConstraint")
ModuleCompliance, NotificationGroup, ObjectGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup", "ObjectGroup")
TimeTicks, iso, enterprises, ModuleIdentity, Counter64, MibIdentifier, Counter32, Bits, Gauge32, Integer32, NotificationType, ObjectIdentity, Unsigned32, MibScalar, MibTable, MibTableRow, MibTableColumn, IpAddress = mibBuilder.importSymbols("SNMPv2-SMI", "TimeTicks", "iso", "enterprises", "ModuleIdentity", "Counter64", "MibIdentifier", "Counter32", "Bits", "Gauge32", "Integer32", "NotificationType", "ObjectIdentity", "Unsigned32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "IpAddress")
TextualConvention, MacAddress, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "MacAddress", "DisplayString")
zte = MibIdentifier((1, 3, 6, 1, 4, 1, 3902))
zxr10 = MibIdentifier((1, 3, 6, 1, 4, 1, 3902, 3))
stack = ModuleIdentity((1, 3, 6, 1, 4, 1, 3902, 3, 300))
stack.setRevisions(('2004-05-14 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: stack.setRevisionsDescriptions(('',))
if mibBuilder.loadTexts: stack.setLastUpdated('200705280000Z')
if mibBuilder.loadTexts: stack.setOrganization('ZTE Corp.')
if mibBuilder.loadTexts: stack.setContactInfo('')
if mibBuilder.loadTexts: stack.setDescription('')
class MasterSlaveDataSynStatus(Integer32):
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(11, 12, 13, 20, 40, 50, 60, 70, 80, 90, 100))
    namedValues = NamedValues(("masterinit", 11), ("backinit", 12), ("memberinit", 13), ("masteridle", 20), ("backreg", 40), ("interaction", 50), ("masterbatchsync", 60), ("backbatchsync", 70), ("masterrealsync", 80), ("backrealsync", 90), ("mastergr", 100))

class StkDeviceStatus(Integer32):
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2))
    namedValues = NamedValues(("master", 0), ("slave", 1), ("member", 2))

systemGrp = MibIdentifier((1, 3, 6, 1, 4, 1, 3902, 3, 300, 1))
class VendorIdType(OctetString):
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(3, 3)
    fixedLength = 3

sysNetMask = MibScalar((1, 3, 6, 1, 4, 1, 3902, 3, 300, 1, 1), IpAddress()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: sysNetMask.setStatus('deprecated')
if mibBuilder.loadTexts: sysNetMask.setDescription('System network mask address.')
sysManagIf = MibScalar((1, 3, 6, 1, 4, 1, 3902, 3, 300, 1, 2), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 255))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: sysManagIf.setStatus('current')
if mibBuilder.loadTexts: sysManagIf.setDescription('System management Interface of Stack device.')
sysMacAddr = MibScalar((1, 3, 6, 1, 4, 1, 3902, 3, 300, 1, 3), MacAddress()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: sysMacAddr.setStatus('current')
if mibBuilder.loadTexts: sysMacAddr.setDescription('System mac address.')
sysMacChagAgingTime = MibScalar((1, 3, 6, 1, 4, 1, 3902, 3, 300, 1, 4), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: sysMacChagAgingTime.setStatus('current')
if mibBuilder.loadTexts: sysMacChagAgingTime.setDescription('After the aging time system mac address must be changed.')
sysLastchagConfigTime = MibScalar((1, 3, 6, 1, 4, 1, 3902, 3, 300, 1, 5), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 50))).setMaxAccess("readonly")
if mibBuilder.loadTexts: sysLastchagConfigTime.setStatus('current')
if mibBuilder.loadTexts: sysLastchagConfigTime.setDescription('The lastest time when the stack system changed the configuration.')
sysMasterSlaveDataSynStatus = MibScalar((1, 3, 6, 1, 4, 1, 3902, 3, 300, 1, 6), MasterSlaveDataSynStatus()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sysMasterSlaveDataSynStatus.setStatus('current')
if mibBuilder.loadTexts: sysMasterSlaveDataSynStatus.setDescription('System master and slave device data synchronization status 11: masterinit 12: backinit 13: memberinit 20: masteridle 40: backreg 50: interaction 60: masterbatchsync 70: backbatchsync 90: backrealsync 100:mastergr.')
sysManagIpAddr = MibScalar((1, 3, 6, 1, 4, 1, 3902, 3, 300, 1, 7), IpAddress()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: sysManagIpAddr.setStatus('current')
if mibBuilder.loadTexts: sysManagIpAddr.setDescription('Management IP Address of Stack device.')
sysStkDeviceInfoTable = MibTable((1, 3, 6, 1, 4, 1, 3902, 3, 300, 2), )
if mibBuilder.loadTexts: sysStkDeviceInfoTable.setStatus('current')
if mibBuilder.loadTexts: sysStkDeviceInfoTable.setDescription('A list of system member information.')
sysStkDeviceInfoEntry = MibTableRow((1, 3, 6, 1, 4, 1, 3902, 3, 300, 2, 1), ).setIndexNames((0, "STACK-MIB", "sysStkDeviceID"))
if mibBuilder.loadTexts: sysStkDeviceInfoEntry.setStatus('current')
if mibBuilder.loadTexts: sysStkDeviceInfoEntry.setDescription('An entry to system member information table.')
sysStkDeviceID = MibTableColumn((1, 3, 6, 1, 4, 1, 3902, 3, 300, 2, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sysStkDeviceID.setStatus('current')
if mibBuilder.loadTexts: sysStkDeviceID.setDescription('Stack member device ID.')
sysStkDeviceType = MibTableColumn((1, 3, 6, 1, 4, 1, 3902, 3, 300, 2, 1, 2), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sysStkDeviceType.setStatus('current')
if mibBuilder.loadTexts: sysStkDeviceType.setDescription('Stack member device ID.')
sysMemDeviceMacAddr = MibTableColumn((1, 3, 6, 1, 4, 1, 3902, 3, 300, 2, 1, 3), MacAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sysMemDeviceMacAddr.setStatus('current')
if mibBuilder.loadTexts: sysMemDeviceMacAddr.setDescription('Stack member device mac address.')
sysMemUpTime = MibTableColumn((1, 3, 6, 1, 4, 1, 3902, 3, 300, 2, 1, 4), TimeTicks()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sysMemUpTime.setStatus('current')
if mibBuilder.loadTexts: sysMemUpTime.setDescription('Stack member device running time.')
sysStkDeviceStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 3902, 3, 300, 2, 1, 5), StkDeviceStatus()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sysStkDeviceStatus.setStatus('current')
if mibBuilder.loadTexts: sysStkDeviceStatus.setDescription('System device status, such as: member device, master device and slave device 0: master device 1: slave device 2: member device.')
zxr10StackStatTable = MibTable((1, 3, 6, 1, 4, 1, 3902, 3, 300, 3), )
if mibBuilder.loadTexts: zxr10StackStatTable.setStatus('current')
if mibBuilder.loadTexts: zxr10StackStatTable.setDescription('A list of the stack statistic information,included cpu utility and memory utility.')
zxr10StackStatEntry = MibTableRow((1, 3, 6, 1, 4, 1, 3902, 3, 300, 3, 1), ).setIndexNames((0, "STACK-MIB", "zxr10StkDeviceID"))
if mibBuilder.loadTexts: zxr10StackStatEntry.setStatus('current')
if mibBuilder.loadTexts: zxr10StackStatEntry.setDescription('An entry to the stack statistic information table.')
zxr10StkDeviceID = MibTableColumn((1, 3, 6, 1, 4, 1, 3902, 3, 300, 3, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: zxr10StkDeviceID.setStatus('current')
if mibBuilder.loadTexts: zxr10StkDeviceID.setDescription('Stack system device index.')
zxr10StkDeviceMacAddr = MibTableColumn((1, 3, 6, 1, 4, 1, 3902, 3, 300, 3, 1, 2), MacAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: zxr10StkDeviceMacAddr.setStatus('current')
if mibBuilder.loadTexts: zxr10StkDeviceMacAddr.setDescription('Stack system device mac address.')
zxr10StkDeviceCpuUtility5s = MibTableColumn((1, 3, 6, 1, 4, 1, 3902, 3, 300, 3, 1, 3), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: zxr10StkDeviceCpuUtility5s.setStatus('current')
if mibBuilder.loadTexts: zxr10StkDeviceCpuUtility5s.setDescription('Stack system device cup utility described by percent( 5 seconds).')
zxr10StkDeviceCpuUtility1m = MibTableColumn((1, 3, 6, 1, 4, 1, 3902, 3, 300, 3, 1, 4), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: zxr10StkDeviceCpuUtility1m.setStatus('current')
if mibBuilder.loadTexts: zxr10StkDeviceCpuUtility1m.setDescription('Stack system device cup utility described by percent( 1 minutes).')
zxr10StkDeviceCpuUtility5m = MibTableColumn((1, 3, 6, 1, 4, 1, 3902, 3, 300, 3, 1, 5), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: zxr10StkDeviceCpuUtility5m.setStatus('current')
if mibBuilder.loadTexts: zxr10StkDeviceCpuUtility5m.setDescription('Stack system device cup utility described by percent( 5 minutes).')
zxr10StkDeviceMemUtility = MibTableColumn((1, 3, 6, 1, 4, 1, 3902, 3, 300, 3, 1, 6), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: zxr10StkDeviceMemUtility.setStatus('current')
if mibBuilder.loadTexts: zxr10StkDeviceMemUtility.setDescription('Stack system device memory utility.')
mibBuilder.exportSymbols("STACK-MIB", zxr10StackStatEntry=zxr10StackStatEntry, sysManagIpAddr=sysManagIpAddr, sysStkDeviceStatus=sysStkDeviceStatus, MasterSlaveDataSynStatus=MasterSlaveDataSynStatus, sysMasterSlaveDataSynStatus=sysMasterSlaveDataSynStatus, sysStkDeviceInfoEntry=sysStkDeviceInfoEntry, sysMacChagAgingTime=sysMacChagAgingTime, systemGrp=systemGrp, zxr10StkDeviceCpuUtility5s=zxr10StkDeviceCpuUtility5s, sysStkDeviceInfoTable=sysStkDeviceInfoTable, sysMemDeviceMacAddr=sysMemDeviceMacAddr, StkDeviceStatus=StkDeviceStatus, VendorIdType=VendorIdType, stack=stack, sysStkDeviceID=sysStkDeviceID, zxr10StkDeviceMacAddr=zxr10StkDeviceMacAddr, zxr10StackStatTable=zxr10StackStatTable, sysNetMask=sysNetMask, sysStkDeviceType=sysStkDeviceType, zxr10StkDeviceID=zxr10StkDeviceID, sysMacAddr=sysMacAddr, zte=zte, zxr10=zxr10, sysMemUpTime=sysMemUpTime, zxr10StkDeviceCpuUtility1m=zxr10StkDeviceCpuUtility1m, zxr10StkDeviceMemUtility=zxr10StkDeviceMemUtility, sysManagIf=sysManagIf, zxr10StkDeviceCpuUtility5m=zxr10StkDeviceCpuUtility5m, sysLastchagConfigTime=sysLastchagConfigTime, PYSNMP_MODULE_ID=stack)
