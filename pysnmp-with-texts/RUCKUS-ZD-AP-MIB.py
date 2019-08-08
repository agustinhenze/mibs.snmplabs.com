#
# PySNMP MIB module RUCKUS-ZD-AP-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/RUCKUS-ZD-AP-MIB
# Produced by pysmi-0.3.4 at Wed May  1 14:59:12 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
OctetString, ObjectIdentifier, Integer = mibBuilder.importSymbols("ASN1", "OctetString", "ObjectIdentifier", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, SingleValueConstraint, ConstraintsIntersection, ConstraintsUnion, ValueRangeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "SingleValueConstraint", "ConstraintsIntersection", "ConstraintsUnion", "ValueRangeConstraint")
InterfaceIndex, ifIndex = mibBuilder.importSymbols("IF-MIB", "InterfaceIndex", "ifIndex")
ruckusZDWLANModule, = mibBuilder.importSymbols("RUCKUS-ROOT-MIB", "ruckusZDWLANModule")
NotificationGroup, ModuleCompliance, ObjectGroup = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance", "ObjectGroup")
MibIdentifier, ObjectIdentity, IpAddress, TimeTicks, Unsigned32, NotificationType, Bits, Gauge32, Counter32, iso, Counter64, ModuleIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, Integer32 = mibBuilder.importSymbols("SNMPv2-SMI", "MibIdentifier", "ObjectIdentity", "IpAddress", "TimeTicks", "Unsigned32", "NotificationType", "Bits", "Gauge32", "Counter32", "iso", "Counter64", "ModuleIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Integer32")
DisplayString, TruthValue, TextualConvention, MacAddress, RowStatus = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TruthValue", "TextualConvention", "MacAddress", "RowStatus")
ruckusZDAPMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 25053, 1, 2, 2, 4))
if mibBuilder.loadTexts: ruckusZDAPMIB.setLastUpdated('201010150800Z')
if mibBuilder.loadTexts: ruckusZDAPMIB.setOrganization('Ruckus Wireless, Inc.')
if mibBuilder.loadTexts: ruckusZDAPMIB.setContactInfo('Ruckus Wireless, Inc. Postal: 880 W Maude Ave Sunnyvale, CA 94085 USA EMail: support@ruckuswireless.com Phone: +1-650-265-4200')
if mibBuilder.loadTexts: ruckusZDAPMIB.setDescription('Ruckus ZD WLAN Configuration mib')
ruckusZDAPObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 25053, 1, 2, 2, 4, 1))
ruckusZDAPConfig = MibIdentifier((1, 3, 6, 1, 4, 1, 25053, 1, 2, 2, 4, 1, 1))
ruckusZDAPConfigTable = MibTable((1, 3, 6, 1, 4, 1, 25053, 1, 2, 2, 4, 1, 1, 1), )
if mibBuilder.loadTexts: ruckusZDAPConfigTable.setStatus('current')
if mibBuilder.loadTexts: ruckusZDAPConfigTable.setDescription('ZD AP table.')
ruckusZDAPConfigEntry = MibTableRow((1, 3, 6, 1, 4, 1, 25053, 1, 2, 2, 4, 1, 1, 1, 1), ).setIndexNames((0, "RUCKUS-ZD-AP-MIB", "ruckusZDAPConfigID"))
if mibBuilder.loadTexts: ruckusZDAPConfigEntry.setStatus('current')
if mibBuilder.loadTexts: ruckusZDAPConfigEntry.setDescription('Specifies a ZoneDirector AP configuration per entry.')
ruckusZDAPConfigID = MibTableColumn((1, 3, 6, 1, 4, 1, 25053, 1, 2, 2, 4, 1, 1, 1, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 5000)))
if mibBuilder.loadTexts: ruckusZDAPConfigID.setStatus('current')
if mibBuilder.loadTexts: ruckusZDAPConfigID.setDescription('AP ID.Max value:for zd1000,50;for zd1100,100;for zd3000,500;zd5000,1000')
ruckusZDAPConfigMacAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 25053, 1, 2, 2, 4, 1, 1, 1, 1, 2), MacAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ruckusZDAPConfigMacAddress.setStatus('current')
if mibBuilder.loadTexts: ruckusZDAPConfigMacAddress.setDescription('AP MAC Address.')
ruckusZDAPConfigAPModel = MibTableColumn((1, 3, 6, 1, 4, 1, 25053, 1, 2, 2, 4, 1, 1, 1, 1, 4), OctetString().subtype(subtypeSpec=ValueSizeConstraint(1, 64))).setMaxAccess("readonly")
if mibBuilder.loadTexts: ruckusZDAPConfigAPModel.setStatus('current')
if mibBuilder.loadTexts: ruckusZDAPConfigAPModel.setDescription('AP Model.')
ruckusZDAPConfigDeviceName = MibTableColumn((1, 3, 6, 1, 4, 1, 25053, 1, 2, 2, 4, 1, 1, 1, 1, 5), OctetString().subtype(subtypeSpec=ValueSizeConstraint(1, 64))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ruckusZDAPConfigDeviceName.setStatus('current')
if mibBuilder.loadTexts: ruckusZDAPConfigDeviceName.setDescription('AP Name.')
ruckusZDAPConfigDescription = MibTableColumn((1, 3, 6, 1, 4, 1, 25053, 1, 2, 2, 4, 1, 1, 1, 1, 6), OctetString().subtype(subtypeSpec=ValueSizeConstraint(1, 64))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ruckusZDAPConfigDescription.setStatus('current')
if mibBuilder.loadTexts: ruckusZDAPConfigDescription.setDescription('AP Description.')
ruckusZDAPConfigLocation = MibTableColumn((1, 3, 6, 1, 4, 1, 25053, 1, 2, 2, 4, 1, 1, 1, 1, 7), OctetString().subtype(subtypeSpec=ValueSizeConstraint(1, 64))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ruckusZDAPConfigLocation.setStatus('current')
if mibBuilder.loadTexts: ruckusZDAPConfigLocation.setDescription('AP Location.')
ruckusZDAPConfigGpsLatitude = MibTableColumn((1, 3, 6, 1, 4, 1, 25053, 1, 2, 2, 4, 1, 1, 1, 1, 10), OctetString().subtype(subtypeSpec=ValueSizeConstraint(1, 16))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ruckusZDAPConfigGpsLatitude.setStatus('current')
if mibBuilder.loadTexts: ruckusZDAPConfigGpsLatitude.setDescription("The AP GPS location measured. the range is '-90,90'.")
ruckusZDAPConfigGpsLongitude = MibTableColumn((1, 3, 6, 1, 4, 1, 25053, 1, 2, 2, 4, 1, 1, 1, 1, 11), OctetString().subtype(subtypeSpec=ValueSizeConstraint(1, 16))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ruckusZDAPConfigGpsLongitude.setStatus('current')
if mibBuilder.loadTexts: ruckusZDAPConfigGpsLongitude.setDescription("The AP GPS location measured. the range is '-180,180'.")
ruckusZDAPConfigIPVersion = MibTableColumn((1, 3, 6, 1, 4, 1, 25053, 1, 2, 2, 4, 1, 1, 1, 1, 14), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("ipv4", 1), ("ipv6", 2), ("dualstack", 3)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ruckusZDAPConfigIPVersion.setStatus('current')
if mibBuilder.loadTexts: ruckusZDAPConfigIPVersion.setDescription('The AP IP version ')
ruckusZDAPConfigIpAddressSettingMode = MibTableColumn((1, 3, 6, 1, 4, 1, 25053, 1, 2, 2, 4, 1, 1, 1, 1, 15), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("admin-by-zd", 1), ("admin-by-dhcp", 2), ("admin-by-ap", 3)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ruckusZDAPConfigIpAddressSettingMode.setStatus('current')
if mibBuilder.loadTexts: ruckusZDAPConfigIpAddressSettingMode.setDescription('The AP IP address configuration setting control. admin-by-zd: ap ipv4 address is set in static model by zd; admin-by-dhcp: ap ipv4 address is set in dhcp model by zd; admin-by-ap: ap ipv4 address is gotten by itself in ap.')
ruckusZDAPConfigIpAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 25053, 1, 2, 2, 4, 1, 1, 1, 1, 16), IpAddress()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ruckusZDAPConfigIpAddress.setStatus('current')
if mibBuilder.loadTexts: ruckusZDAPConfigIpAddress.setDescription('The AP IP address.')
ruckusZDAPConfigIpAddressMask = MibTableColumn((1, 3, 6, 1, 4, 1, 25053, 1, 2, 2, 4, 1, 1, 1, 1, 17), IpAddress()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ruckusZDAPConfigIpAddressMask.setStatus('current')
if mibBuilder.loadTexts: ruckusZDAPConfigIpAddressMask.setDescription('The AP IP address mask.')
ruckusZDAPConfigGatewayIpAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 25053, 1, 2, 2, 4, 1, 1, 1, 1, 20), IpAddress()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ruckusZDAPConfigGatewayIpAddress.setStatus('current')
if mibBuilder.loadTexts: ruckusZDAPConfigGatewayIpAddress.setDescription('The AP Gateway IP Address.')
ruckusZDAPConfigIpV6AddressSettingMode = MibTableColumn((1, 3, 6, 1, 4, 1, 25053, 1, 2, 2, 4, 1, 1, 1, 1, 21), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("admin-by-zd", 1), ("admin-by-autoconfig", 2), ("admin-by-ap", 3)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ruckusZDAPConfigIpV6AddressSettingMode.setStatus('current')
if mibBuilder.loadTexts: ruckusZDAPConfigIpV6AddressSettingMode.setDescription('The AP IPV6 address configuration setting control. admin-by-zd: ap ipv6 address is set in manual model by zd; admin-by-autoconfig: ap ipv6 address is set in autoconfig(from route server or dhcpv6 server) model by zd; admin-by-ap: ap ipv6 address is gotten by itself in ap.')
ruckusZDAPConfigIpV6Address = MibTableColumn((1, 3, 6, 1, 4, 1, 25053, 1, 2, 2, 4, 1, 1, 1, 1, 22), OctetString().subtype(subtypeSpec=ValueSizeConstraint(2, 40))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ruckusZDAPConfigIpV6Address.setStatus('current')
if mibBuilder.loadTexts: ruckusZDAPConfigIpV6Address.setDescription('The AP IPV6 address.')
ruckusZDAPConfigIpV6PrefixLen = MibTableColumn((1, 3, 6, 1, 4, 1, 25053, 1, 2, 2, 4, 1, 1, 1, 1, 23), Integer32().subtype(subtypeSpec=ValueRangeConstraint(3, 128))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ruckusZDAPConfigIpV6PrefixLen.setStatus('current')
if mibBuilder.loadTexts: ruckusZDAPConfigIpV6PrefixLen.setDescription('The AP IPV6 prefix length.')
ruckusZDAPConfigGatewayIpV6Address = MibTableColumn((1, 3, 6, 1, 4, 1, 25053, 1, 2, 2, 4, 1, 1, 1, 1, 24), OctetString().subtype(subtypeSpec=ValueSizeConstraint(2, 40))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ruckusZDAPConfigGatewayIpV6Address.setStatus('current')
if mibBuilder.loadTexts: ruckusZDAPConfigGatewayIpV6Address.setDescription('The AP Gateway IPV6 Address.')
ruckusZDAPConfigPrimaryDnsIpAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 25053, 1, 2, 2, 4, 1, 1, 1, 1, 25), IpAddress()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ruckusZDAPConfigPrimaryDnsIpAddress.setStatus('current')
if mibBuilder.loadTexts: ruckusZDAPConfigPrimaryDnsIpAddress.setDescription('The AP Primary DNS IP Address.')
ruckusZDAPConfigSecondaryDnsIpAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 25053, 1, 2, 2, 4, 1, 1, 1, 1, 26), IpAddress()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ruckusZDAPConfigSecondaryDnsIpAddress.setStatus('current')
if mibBuilder.loadTexts: ruckusZDAPConfigSecondaryDnsIpAddress.setDescription('The AP Secondary DNS IP Address.')
ruckusZDAPConfigPrimaryDnsIpV6Address = MibTableColumn((1, 3, 6, 1, 4, 1, 25053, 1, 2, 2, 4, 1, 1, 1, 1, 27), OctetString().subtype(subtypeSpec=ValueSizeConstraint(2, 40))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ruckusZDAPConfigPrimaryDnsIpV6Address.setStatus('current')
if mibBuilder.loadTexts: ruckusZDAPConfigPrimaryDnsIpV6Address.setDescription('The AP Primary DNS IPV6 Address.')
ruckusZDAPConfigSecondaryDnsV6IpAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 25053, 1, 2, 2, 4, 1, 1, 1, 1, 28), OctetString().subtype(subtypeSpec=ValueSizeConstraint(2, 40))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ruckusZDAPConfigSecondaryDnsV6IpAddress.setStatus('current')
if mibBuilder.loadTexts: ruckusZDAPConfigSecondaryDnsV6IpAddress.setDescription('The AP Secondary DNS IPV6 Address.')
ruckusZDAPConfigRadioType = MibTableColumn((1, 3, 6, 1, 4, 1, 25053, 1, 2, 2, 4, 1, 1, 1, 1, 30), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5))).clone(namedValues=NamedValues(("ieee80211bg", 1), ("ieee80211na", 2), ("ieee80211a", 3), ("ieee80211n", 4), ("ieee80211ng", 5)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: ruckusZDAPConfigRadioType.setStatus('current')
if mibBuilder.loadTexts: ruckusZDAPConfigRadioType.setDescription('The AP Wireless type.')
ruckusZDAPConfigRadioChannel24 = MibTableColumn((1, 3, 6, 1, 4, 1, 25053, 1, 2, 2, 4, 1, 1, 1, 1, 31), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 11))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ruckusZDAPConfigRadioChannel24.setStatus('current')
if mibBuilder.loadTexts: ruckusZDAPConfigRadioChannel24.setDescription('The AP Channel selection on the 2.4 GHz radio. The AP radio channel, selectable 0, 1-11, 0 : auto channel selection, 1-11 : specific channel selection.')
ruckusZDAPConfigRadioTxPowerLevel24 = MibTableColumn((1, 3, 6, 1, 4, 1, 25053, 1, 2, 2, 4, 1, 1, 1, 1, 32), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 25))).setUnits('dB').setMaxAccess("readwrite")
if mibBuilder.loadTexts: ruckusZDAPConfigRadioTxPowerLevel24.setStatus('current')
if mibBuilder.loadTexts: ruckusZDAPConfigRadioTxPowerLevel24.setDescription('The AP Tx Power level selection on the 2.4 GHz radio, auto(25) | 0 to 24 corresponding to 0 to -24dB from max power. Now to be compatible with web, if txpower is more than 10, txpower will be set to 24(Min).')
ruckusZDAPConfigRadioWlanGroup24 = MibTableColumn((1, 3, 6, 1, 4, 1, 25053, 1, 2, 2, 4, 1, 1, 1, 1, 33), OctetString().subtype(subtypeSpec=ValueSizeConstraint(1, 63))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ruckusZDAPConfigRadioWlanGroup24.setStatus('current')
if mibBuilder.loadTexts: ruckusZDAPConfigRadioWlanGroup24.setDescription('The AP WLAN group (name) selection on the 2.4 GHz radio.')
ruckusZDAPConfigRadioEnableWlanService24 = MibTableColumn((1, 3, 6, 1, 4, 1, 25053, 1, 2, 2, 4, 1, 1, 1, 1, 34), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enable", 1), ("disable", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ruckusZDAPConfigRadioEnableWlanService24.setStatus('current')
if mibBuilder.loadTexts: ruckusZDAPConfigRadioEnableWlanService24.setDescription('The AP enable wlan service flag on the 2.4 GHz radio.')
ruckusZDAPConfigRadioChannel5 = MibTableColumn((1, 3, 6, 1, 4, 1, 25053, 1, 2, 2, 4, 1, 1, 1, 1, 40), Integer32().subtype(subtypeSpec=ConstraintsUnion(ValueRangeConstraint(0, 0), ValueRangeConstraint(36, 165), ))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ruckusZDAPConfigRadioChannel5.setStatus('current')
if mibBuilder.loadTexts: ruckusZDAPConfigRadioChannel5.setDescription('The AP Channel selection on the 5 GHz radio. The AP radio channel, selectable 0, 36-165, 0 : auto channel selection, 36-165 : specific channel selection. It is ruled by country code.Please consult the MAP of channel for each country.')
ruckusZDAPConfigRadioTxPowerLevel5 = MibTableColumn((1, 3, 6, 1, 4, 1, 25053, 1, 2, 2, 4, 1, 1, 1, 1, 41), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 25))).setUnits('dB').setMaxAccess("readwrite")
if mibBuilder.loadTexts: ruckusZDAPConfigRadioTxPowerLevel5.setStatus('current')
if mibBuilder.loadTexts: ruckusZDAPConfigRadioTxPowerLevel5.setDescription('The AP Tx Power level selection on the 5 GHz radio, auto(25) | 0 to 24 corresponding to 0 to -24dB from max power. Now to be compatible with web, if txpower is more than 10, txpower will be set to 24(Min).')
ruckusZDAPConfigRadioWlanGroup5 = MibTableColumn((1, 3, 6, 1, 4, 1, 25053, 1, 2, 2, 4, 1, 1, 1, 1, 42), OctetString().subtype(subtypeSpec=ValueSizeConstraint(1, 63))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ruckusZDAPConfigRadioWlanGroup5.setStatus('current')
if mibBuilder.loadTexts: ruckusZDAPConfigRadioWlanGroup5.setDescription('The AP WLAN group (name) selection on the 5 GHz radio.')
ruckusZDAPConfigRadioEnableWlanService5 = MibTableColumn((1, 3, 6, 1, 4, 1, 25053, 1, 2, 2, 4, 1, 1, 1, 1, 43), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enable", 1), ("disable", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ruckusZDAPConfigRadioEnableWlanService5.setStatus('current')
if mibBuilder.loadTexts: ruckusZDAPConfigRadioEnableWlanService5.setDescription('The AP enable wlan service flag on the 5 GHz radio.')
ruckusZDAPConfigMeshConfigurationMode = MibTableColumn((1, 3, 6, 1, 4, 1, 25053, 1, 2, 2, 4, 1, 1, 1, 1, 50), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))).clone(namedValues=NamedValues(("auto", 1), ("root-ap", 2), ("mesh-ap", 3), ("disabled", 4)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ruckusZDAPConfigMeshConfigurationMode.setStatus('current')
if mibBuilder.loadTexts: ruckusZDAPConfigMeshConfigurationMode.setDescription('The AP Mesh network configuration mode.')
ruckusZDAPConfigUplinkSelectionMode = MibTableColumn((1, 3, 6, 1, 4, 1, 25053, 1, 2, 2, 4, 1, 1, 1, 1, 51), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("smart", 1), ("manual", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ruckusZDAPConfigUplinkSelectionMode.setStatus('current')
if mibBuilder.loadTexts: ruckusZDAPConfigUplinkSelectionMode.setDescription("The AP network uplink selection mode. For manual,now 'set' is not supported")
ruckusZDAPConfigApproveMode = MibTableColumn((1, 3, 6, 1, 4, 1, 25053, 1, 2, 2, 4, 1, 1, 1, 1, 52), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("approved", 1), ("not-approved", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ruckusZDAPConfigApproveMode.setStatus('current')
if mibBuilder.loadTexts: ruckusZDAPConfigApproveMode.setDescription("AP approval state. For not-approved,'set' is not supported.")
ruckusZDAPConfigManagementAdmin = MibTableColumn((1, 3, 6, 1, 4, 1, 25053, 1, 2, 2, 4, 1, 1, 1, 1, 60), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("delete", 1), ("associated", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ruckusZDAPConfigManagementAdmin.setStatus('current')
if mibBuilder.loadTexts: ruckusZDAPConfigManagementAdmin.setDescription('Admin action to remove this AP from the ZD management.')
ruckusZDAPConfigRebootNow = MibTableColumn((1, 3, 6, 1, 4, 1, 25053, 1, 2, 2, 4, 1, 1, 1, 1, 64), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1))).clone(namedValues=NamedValues(("reboot", 1)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ruckusZDAPConfigRebootNow.setStatus('current')
if mibBuilder.loadTexts: ruckusZDAPConfigRebootNow.setDescription('AP reboot right now.')
mibBuilder.exportSymbols("RUCKUS-ZD-AP-MIB", ruckusZDAPConfigGatewayIpAddress=ruckusZDAPConfigGatewayIpAddress, PYSNMP_MODULE_ID=ruckusZDAPMIB, ruckusZDAPConfigLocation=ruckusZDAPConfigLocation, ruckusZDAPConfigIpAddress=ruckusZDAPConfigIpAddress, ruckusZDAPConfigApproveMode=ruckusZDAPConfigApproveMode, ruckusZDAPConfigRadioType=ruckusZDAPConfigRadioType, ruckusZDAPConfigDeviceName=ruckusZDAPConfigDeviceName, ruckusZDAPMIB=ruckusZDAPMIB, ruckusZDAPConfigSecondaryDnsIpAddress=ruckusZDAPConfigSecondaryDnsIpAddress, ruckusZDAPConfigID=ruckusZDAPConfigID, ruckusZDAPConfigPrimaryDnsIpAddress=ruckusZDAPConfigPrimaryDnsIpAddress, ruckusZDAPConfigRadioWlanGroup5=ruckusZDAPConfigRadioWlanGroup5, ruckusZDAPConfigIpV6Address=ruckusZDAPConfigIpV6Address, ruckusZDAPConfigPrimaryDnsIpV6Address=ruckusZDAPConfigPrimaryDnsIpV6Address, ruckusZDAPConfigRebootNow=ruckusZDAPConfigRebootNow, ruckusZDAPConfigIpV6AddressSettingMode=ruckusZDAPConfigIpV6AddressSettingMode, ruckusZDAPConfigGatewayIpV6Address=ruckusZDAPConfigGatewayIpV6Address, ruckusZDAPConfigEntry=ruckusZDAPConfigEntry, ruckusZDAPConfigRadioEnableWlanService24=ruckusZDAPConfigRadioEnableWlanService24, ruckusZDAPConfigAPModel=ruckusZDAPConfigAPModel, ruckusZDAPConfigDescription=ruckusZDAPConfigDescription, ruckusZDAPConfigRadioEnableWlanService5=ruckusZDAPConfigRadioEnableWlanService5, ruckusZDAPConfigMeshConfigurationMode=ruckusZDAPConfigMeshConfigurationMode, ruckusZDAPConfigIPVersion=ruckusZDAPConfigIPVersion, ruckusZDAPConfigManagementAdmin=ruckusZDAPConfigManagementAdmin, ruckusZDAPConfigRadioTxPowerLevel24=ruckusZDAPConfigRadioTxPowerLevel24, ruckusZDAPConfigTable=ruckusZDAPConfigTable, ruckusZDAPConfigGpsLongitude=ruckusZDAPConfigGpsLongitude, ruckusZDAPObjects=ruckusZDAPObjects, ruckusZDAPConfigSecondaryDnsV6IpAddress=ruckusZDAPConfigSecondaryDnsV6IpAddress, ruckusZDAPConfigGpsLatitude=ruckusZDAPConfigGpsLatitude, ruckusZDAPConfigRadioChannel24=ruckusZDAPConfigRadioChannel24, ruckusZDAPConfigRadioTxPowerLevel5=ruckusZDAPConfigRadioTxPowerLevel5, ruckusZDAPConfigRadioChannel5=ruckusZDAPConfigRadioChannel5, ruckusZDAPConfigIpAddressMask=ruckusZDAPConfigIpAddressMask, ruckusZDAPConfigIpAddressSettingMode=ruckusZDAPConfigIpAddressSettingMode, ruckusZDAPConfigUplinkSelectionMode=ruckusZDAPConfigUplinkSelectionMode, ruckusZDAPConfigRadioWlanGroup24=ruckusZDAPConfigRadioWlanGroup24, ruckusZDAPConfigMacAddress=ruckusZDAPConfigMacAddress, ruckusZDAPConfigIpV6PrefixLen=ruckusZDAPConfigIpV6PrefixLen, ruckusZDAPConfig=ruckusZDAPConfig)