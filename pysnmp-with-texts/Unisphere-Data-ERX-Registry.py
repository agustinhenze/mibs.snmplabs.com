#
# PySNMP MIB module Unisphere-Data-ERX-Registry (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/Unisphere-Data-ERX-Registry
# Produced by pysmi-0.3.4 at Wed May  1 15:31:00 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
ObjectIdentifier, Integer, OctetString = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "Integer", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ValueSizeConstraint, SingleValueConstraint, ConstraintsUnion, ValueRangeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ValueSizeConstraint", "SingleValueConstraint", "ConstraintsUnion", "ValueRangeConstraint")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
MibIdentifier, MibScalar, MibTable, MibTableRow, MibTableColumn, IpAddress, Integer32, Gauge32, ObjectIdentity, iso, ModuleIdentity, NotificationType, Counter64, Bits, Counter32, Unsigned32, TimeTicks = mibBuilder.importSymbols("SNMPv2-SMI", "MibIdentifier", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "IpAddress", "Integer32", "Gauge32", "ObjectIdentity", "iso", "ModuleIdentity", "NotificationType", "Counter64", "Bits", "Counter32", "Unsigned32", "TimeTicks")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
usDataAdmin, = mibBuilder.importSymbols("Unisphere-Data-Registry", "usDataAdmin")
usdErxRegistry = ModuleIdentity((1, 3, 6, 1, 4, 1, 4874, 4, 2, 2))
usdErxRegistry.setRevisions(('2002-10-10 18:51', '2002-05-08 12:34', '2002-05-07 14:05', '2001-08-20 16:08', '2001-06-12 18:27', '2001-06-04 20:11',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: usdErxRegistry.setRevisionsDescriptions(('Added support for the 12-port E3 IO adapter. Added support for the Ut3f12 line card. Added SRP module with 40 gbps plus switch fabric. Added Vitrual Tunneling Server (VTS) module. Added X.21/V.35 Server module and I/O adapter. Added OC12 APS I/O adapters. Added redundant midplane spare I/O adapters.', 'Added GE SFP IOA module.', "Added SRP modules with 5 gbps and 40 gbps 'plus' switch fabrics.", 'Added 12 port channelized T3 modules.', 'Added High Speed Serial Interface (HSSI) modules.', 'Initial version of this SNMP management information module.',))
if mibBuilder.loadTexts: usdErxRegistry.setLastUpdated('200210101851Z')
if mibBuilder.loadTexts: usdErxRegistry.setOrganization('Juniper Networks, Inc.')
if mibBuilder.loadTexts: usdErxRegistry.setContactInfo(' Juniper Networks, Inc. Postal: 10 Technology Park Drive Westford, MA 01886 USA Tel: +1 978 589 5800 Email: mib@Juniper.net')
if mibBuilder.loadTexts: usdErxRegistry.setDescription('Unisphere Edge Routing Switch (ERX) product family system-specific object identification values. This module includes the textual convention definition for the ERX module types. It also defines AutonomousType (OID) values for all the physical entity types (entPhysicalVendorType). This module will be updated whenever a new type of module or other hardware becomes available in ERX systems.')
usdErxEntPhysicalType = MibIdentifier((1, 3, 6, 1, 4, 1, 4874, 4, 2, 2, 1))
erxChassis = ObjectIdentity((1, 3, 6, 1, 4, 1, 4874, 4, 2, 2, 1, 1))
if mibBuilder.loadTexts: erxChassis.setStatus('current')
if mibBuilder.loadTexts: erxChassis.setDescription("The vendor type ID for a generic Edge Routing Switch (ERX) chassis. This identifies an 'overall' physical entity for any ERX system.")
erx700Chassis = ObjectIdentity((1, 3, 6, 1, 4, 1, 4874, 4, 2, 2, 1, 1, 1))
if mibBuilder.loadTexts: erx700Chassis.setStatus('current')
if mibBuilder.loadTexts: erx700Chassis.setDescription("The vendor type ID for an Edge Routing Switch 700 (ERX-700) 7-slot chassis. This is the 'overall' physical entity for an ERX-700 system.")
erx1400Chassis = ObjectIdentity((1, 3, 6, 1, 4, 1, 4874, 4, 2, 2, 1, 1, 2))
if mibBuilder.loadTexts: erx1400Chassis.setStatus('current')
if mibBuilder.loadTexts: erx1400Chassis.setDescription("The vendor type ID for an Edge Routing Switch 1400 (ERX-1400) 14-slot chassis. This is the 'overall' physical entity for an ERX-1400 system.")
erxFanAssembly = ObjectIdentity((1, 3, 6, 1, 4, 1, 4874, 4, 2, 2, 1, 2))
if mibBuilder.loadTexts: erxFanAssembly.setStatus('current')
if mibBuilder.loadTexts: erxFanAssembly.setDescription('The vendor type ID for an ERX fan assembly.')
erx700FanAssembly = ObjectIdentity((1, 3, 6, 1, 4, 1, 4874, 4, 2, 2, 1, 2, 1))
if mibBuilder.loadTexts: erx700FanAssembly.setStatus('current')
if mibBuilder.loadTexts: erx700FanAssembly.setDescription('The vendor type ID for an ERX700 fan assembly with four fans and two -12 volt, 15 watt power converters (Product Code: FAN-7).')
erx1400FanAssembly = ObjectIdentity((1, 3, 6, 1, 4, 1, 4874, 4, 2, 2, 1, 2, 2))
if mibBuilder.loadTexts: erx1400FanAssembly.setStatus('current')
if mibBuilder.loadTexts: erx1400FanAssembly.setDescription('The vendor type ID for an ERX1400 fan assembly with six fans and two -24 volt, 50 watt power converters (Product Code: FAN-14).')
erxPowerInput = ObjectIdentity((1, 3, 6, 1, 4, 1, 4874, 4, 2, 2, 1, 3))
if mibBuilder.loadTexts: erxPowerInput.setStatus('current')
if mibBuilder.loadTexts: erxPowerInput.setDescription('The vendor type ID for an ERX power distribution module (Product Code: PDU).')
erxMidplane = ObjectIdentity((1, 3, 6, 1, 4, 1, 4874, 4, 2, 2, 1, 4))
if mibBuilder.loadTexts: erxMidplane.setStatus('current')
if mibBuilder.loadTexts: erxMidplane.setDescription('The vendor type ID for an ERX midplane.')
erx700Midplane = ObjectIdentity((1, 3, 6, 1, 4, 1, 4874, 4, 2, 2, 1, 4, 1))
if mibBuilder.loadTexts: erx700Midplane.setStatus('current')
if mibBuilder.loadTexts: erx700Midplane.setDescription('The vendor type ID for an ERX700 (7-slot) midplane.')
erx1400Midplane = ObjectIdentity((1, 3, 6, 1, 4, 1, 4874, 4, 2, 2, 1, 4, 2))
if mibBuilder.loadTexts: erx1400Midplane.setStatus('current')
if mibBuilder.loadTexts: erx1400Midplane.setDescription('The vendor type ID for an ERX1400 (14-slot) midplane.')
erx1Plus1RedundantT1E1Midplane = ObjectIdentity((1, 3, 6, 1, 4, 1, 4874, 4, 2, 2, 1, 4, 3))
if mibBuilder.loadTexts: erx1Plus1RedundantT1E1Midplane.setStatus('current')
if mibBuilder.loadTexts: erx1Plus1RedundantT1E1Midplane.setDescription('The vendor type ID for an ERX 1 + 1 redundant T1/E1 midplane (Product Code: REDMID-T1/E1/1/1).')
erx2Plus1RedundantT1E1Midplane = ObjectIdentity((1, 3, 6, 1, 4, 1, 4874, 4, 2, 2, 1, 4, 4))
if mibBuilder.loadTexts: erx2Plus1RedundantT1E1Midplane.setStatus('current')
if mibBuilder.loadTexts: erx2Plus1RedundantT1E1Midplane.setDescription('The vendor type ID for an ERX 2 + 1 redundant T1/E1 midplane (Product Code: REDMID-T1/E1/2/1).')
erx3Plus1RedundantT1E1Midplane = ObjectIdentity((1, 3, 6, 1, 4, 1, 4874, 4, 2, 2, 1, 4, 5))
if mibBuilder.loadTexts: erx3Plus1RedundantT1E1Midplane.setStatus('current')
if mibBuilder.loadTexts: erx3Plus1RedundantT1E1Midplane.setDescription('The vendor type ID for an ERX 3 + 1 redundant T1/E1 midplane (Product Code: REDMID-T1/E1/3/1).')
erx4Plus1RedundantT1E1Midplane = ObjectIdentity((1, 3, 6, 1, 4, 1, 4874, 4, 2, 2, 1, 4, 6))
if mibBuilder.loadTexts: erx4Plus1RedundantT1E1Midplane.setStatus('current')
if mibBuilder.loadTexts: erx4Plus1RedundantT1E1Midplane.setDescription('The vendor type ID for an ERX 4 + 1 redundant T1/E1 midplane (Product Code: REDMID-T1/E1/4/1).')
erx5Plus1RedundantT1E1Midplane = ObjectIdentity((1, 3, 6, 1, 4, 1, 4874, 4, 2, 2, 1, 4, 7))
if mibBuilder.loadTexts: erx5Plus1RedundantT1E1Midplane.setStatus('current')
if mibBuilder.loadTexts: erx5Plus1RedundantT1E1Midplane.setDescription('The vendor type ID for an ERX 5 + 1 redundant T1/E1 midplane (Product Code: REDMID-T1/E1/5/1).')
erx1Plus1RedundantT3E3Midplane = ObjectIdentity((1, 3, 6, 1, 4, 1, 4874, 4, 2, 2, 1, 4, 8))
if mibBuilder.loadTexts: erx1Plus1RedundantT3E3Midplane.setStatus('current')
if mibBuilder.loadTexts: erx1Plus1RedundantT3E3Midplane.setDescription('The vendor type ID for an ERX 1 + 1 redundant CT3/T3/E3 midplane (Product Code: REDMID-T3/E3/1/1).')
erx2Plus1RedundantT3E3Midplane = ObjectIdentity((1, 3, 6, 1, 4, 1, 4874, 4, 2, 2, 1, 4, 9))
if mibBuilder.loadTexts: erx2Plus1RedundantT3E3Midplane.setStatus('current')
if mibBuilder.loadTexts: erx2Plus1RedundantT3E3Midplane.setDescription('The vendor type ID for an ERX 2 + 1 redundant CT3/T3/E3 midplane (Product Code: REDMID-T3/E3/2/1).')
erx3Plus1RedundantT3E3Midplane = ObjectIdentity((1, 3, 6, 1, 4, 1, 4874, 4, 2, 2, 1, 4, 10))
if mibBuilder.loadTexts: erx3Plus1RedundantT3E3Midplane.setStatus('current')
if mibBuilder.loadTexts: erx3Plus1RedundantT3E3Midplane.setDescription('The vendor type ID for an ERX 3 + 1 redundant CT3/T3/E3 midplane (Product Code: REDMID-T3/E3/3/1).')
erx4Plus1RedundantT3E3Midplane = ObjectIdentity((1, 3, 6, 1, 4, 1, 4874, 4, 2, 2, 1, 4, 11))
if mibBuilder.loadTexts: erx4Plus1RedundantT3E3Midplane.setStatus('current')
if mibBuilder.loadTexts: erx4Plus1RedundantT3E3Midplane.setDescription('The vendor type ID for an ERX 4 + 1 redundant CT3/T3/E3 midplane (Product Code: REDMID-T3/E3/4/1).')
erx5Plus1RedundantT3E3Midplane = ObjectIdentity((1, 3, 6, 1, 4, 1, 4874, 4, 2, 2, 1, 4, 12))
if mibBuilder.loadTexts: erx5Plus1RedundantT3E3Midplane.setStatus('current')
if mibBuilder.loadTexts: erx5Plus1RedundantT3E3Midplane.setDescription('The vendor type ID for an ERX 5 + 1 redundant CT3/T3/E3 midplane (Product Code: REDMID-T3/E3/5/1).')
erx1Plus1RedundantOcMidplane = ObjectIdentity((1, 3, 6, 1, 4, 1, 4874, 4, 2, 2, 1, 4, 13))
if mibBuilder.loadTexts: erx1Plus1RedundantOcMidplane.setStatus('current')
if mibBuilder.loadTexts: erx1Plus1RedundantOcMidplane.setDescription('The vendor type ID for an ERX 1 + 1 redundant OC3/OC12 midplane (Product Code: REDMID-OC/1/1).')
erx2Plus1RedundantOcMidplane = ObjectIdentity((1, 3, 6, 1, 4, 1, 4874, 4, 2, 2, 1, 4, 14))
if mibBuilder.loadTexts: erx2Plus1RedundantOcMidplane.setStatus('current')
if mibBuilder.loadTexts: erx2Plus1RedundantOcMidplane.setDescription('The vendor type ID for an ERX 2 + 1 redundant OC3/OC12 midplane (Product Code: REDMID-OC/2/1).')
erx3Plus1RedundantOcMidplane = ObjectIdentity((1, 3, 6, 1, 4, 1, 4874, 4, 2, 2, 1, 4, 15))
if mibBuilder.loadTexts: erx3Plus1RedundantOcMidplane.setStatus('current')
if mibBuilder.loadTexts: erx3Plus1RedundantOcMidplane.setDescription('The vendor type ID for an ERX 3 + 1 redundant OC3/OC12 midplane (Product Code: REDMID-OC/3/1).')
erx4Plus1RedundantOcMidplane = ObjectIdentity((1, 3, 6, 1, 4, 1, 4874, 4, 2, 2, 1, 4, 16))
if mibBuilder.loadTexts: erx4Plus1RedundantOcMidplane.setStatus('current')
if mibBuilder.loadTexts: erx4Plus1RedundantOcMidplane.setDescription('The vendor type ID for an ERX 4 + 1 redundant OC3/OC12 midplane (Product Code: REDMID-OC/4/1).')
erx5Plus1RedundantOcMidplane = ObjectIdentity((1, 3, 6, 1, 4, 1, 4874, 4, 2, 2, 1, 4, 17))
if mibBuilder.loadTexts: erx5Plus1RedundantOcMidplane.setStatus('current')
if mibBuilder.loadTexts: erx5Plus1RedundantOcMidplane.setDescription('The vendor type ID for an ERX 5 + 1 redundant OC3/OC12 midplane (Product Code: REDMID-OC/5/1).')
erxSrpModule = ObjectIdentity((1, 3, 6, 1, 4, 1, 4874, 4, 2, 2, 1, 5))
if mibBuilder.loadTexts: erxSrpModule.setStatus('current')
if mibBuilder.loadTexts: erxSrpModule.setDescription('The vendor type ID for an ERX Switch and Router Processor (SRP) module.')
erxSrp5 = ObjectIdentity((1, 3, 6, 1, 4, 1, 4874, 4, 2, 2, 1, 5, 1))
if mibBuilder.loadTexts: erxSrp5.setStatus('current')
if mibBuilder.loadTexts: erxSrp5.setDescription('The vendor type ID for an ERX Switch and Router Processor (SRP) module with 5 Gbps switch fabric (Product Code: SRP-5).')
erxSrp10 = ObjectIdentity((1, 3, 6, 1, 4, 1, 4874, 4, 2, 2, 1, 5, 2))
if mibBuilder.loadTexts: erxSrp10.setStatus('current')
if mibBuilder.loadTexts: erxSrp10.setDescription('The vendor type ID for an ERX Switch and Router Processor (SRP) module with 10 Gbps switch fabric (Product Code: SRP-10).')
erxSrp10Ecc = ObjectIdentity((1, 3, 6, 1, 4, 1, 4874, 4, 2, 2, 1, 5, 3))
if mibBuilder.loadTexts: erxSrp10Ecc.setStatus('current')
if mibBuilder.loadTexts: erxSrp10Ecc.setDescription('The vendor type ID for an ERX Switch and Router Processor (SRP) module with 10 Gbps switch fabric with ECC (Product Code: SRP-10-ECC).')
erxSrp40 = ObjectIdentity((1, 3, 6, 1, 4, 1, 4874, 4, 2, 2, 1, 5, 4))
if mibBuilder.loadTexts: erxSrp40.setStatus('current')
if mibBuilder.loadTexts: erxSrp40.setDescription('The vendor type ID for an ERX Switch and Router Processor (SRP) module with 40 Gbps switch fabric with ECC (Product Code: SRP-40-ECC).')
erxSrp5Plus = ObjectIdentity((1, 3, 6, 1, 4, 1, 4874, 4, 2, 2, 1, 5, 5))
if mibBuilder.loadTexts: erxSrp5Plus.setStatus('current')
if mibBuilder.loadTexts: erxSrp5Plus.setDescription("The vendor type ID for an ERX Switch and Router Processor (SRP) module with 5 Gbps 'plus' switch fabric (Product Code: SRP-5Plus).")
erxSrp40Plus = ObjectIdentity((1, 3, 6, 1, 4, 1, 4874, 4, 2, 2, 1, 5, 6))
if mibBuilder.loadTexts: erxSrp40Plus.setStatus('current')
if mibBuilder.loadTexts: erxSrp40Plus.setDescription("The vendor type ID for an ERX Switch and Router Processor (SRP) module with 40 Gbps 'plus' switch fabric (Product Code: ERX-40EC2-SRP).")
erxSrpIoAdapter = ObjectIdentity((1, 3, 6, 1, 4, 1, 4874, 4, 2, 2, 1, 6))
if mibBuilder.loadTexts: erxSrpIoAdapter.setStatus('current')
if mibBuilder.loadTexts: erxSrpIoAdapter.setDescription('The vendor type ID for an ERX SRP I/O adapter (Product Code: SRP_I/O).')
erxLineModule = ObjectIdentity((1, 3, 6, 1, 4, 1, 4874, 4, 2, 2, 1, 7))
if mibBuilder.loadTexts: erxLineModule.setStatus('current')
if mibBuilder.loadTexts: erxLineModule.setDescription('The vendor type ID for an ERX line module.')
erxCt1 = ObjectIdentity((1, 3, 6, 1, 4, 1, 4874, 4, 2, 2, 1, 7, 1))
if mibBuilder.loadTexts: erxCt1.setStatus('current')
if mibBuilder.loadTexts: erxCt1.setDescription('The vendor type ID for an ERX 24 port fully channelized T1 line module (Product Code: CT1-FULL).')
erxCe1 = ObjectIdentity((1, 3, 6, 1, 4, 1, 4874, 4, 2, 2, 1, 7, 2))
if mibBuilder.loadTexts: erxCe1.setStatus('current')
if mibBuilder.loadTexts: erxCe1.setDescription('The vendor type ID for an ERX 20 port fully channelized E1 line module (Product Code: CE1-FULL).')
erxCt3 = ObjectIdentity((1, 3, 6, 1, 4, 1, 4874, 4, 2, 2, 1, 7, 4))
if mibBuilder.loadTexts: erxCt3.setStatus('current')
if mibBuilder.loadTexts: erxCt3.setDescription('The vendor type ID for an ERX 3 port channelized T3 line module (Product Code: CT3-3).')
erxT3Atm = ObjectIdentity((1, 3, 6, 1, 4, 1, 4874, 4, 2, 2, 1, 7, 5))
if mibBuilder.loadTexts: erxT3Atm.setStatus('current')
if mibBuilder.loadTexts: erxT3Atm.setDescription('The vendor type ID for an ERX 3 port unchannelized T3 cell service line module (Product Code: T3-3A).')
erxT3Frame = ObjectIdentity((1, 3, 6, 1, 4, 1, 4874, 4, 2, 2, 1, 7, 6))
if mibBuilder.loadTexts: erxT3Frame.setStatus('current')
if mibBuilder.loadTexts: erxT3Frame.setDescription('The vendor type ID for an ERX 3 port unchannelized T3 packet service line module (Product Code: T3-3F).')
erxE3Atm = ObjectIdentity((1, 3, 6, 1, 4, 1, 4874, 4, 2, 2, 1, 7, 7))
if mibBuilder.loadTexts: erxE3Atm.setStatus('current')
if mibBuilder.loadTexts: erxE3Atm.setDescription('The vendor type ID for an ERX 3 port unchannelized E3 cell service line module (Product Code: E3-3A).')
erxE3Frame = ObjectIdentity((1, 3, 6, 1, 4, 1, 4874, 4, 2, 2, 1, 7, 8))
if mibBuilder.loadTexts: erxE3Frame.setStatus('current')
if mibBuilder.loadTexts: erxE3Frame.setDescription('The vendor type ID for an ERX 3 port unchannelized E3 packet service line module (Product Code: E3-3F).')
erxOc3 = ObjectIdentity((1, 3, 6, 1, 4, 1, 4874, 4, 2, 2, 1, 7, 9))
if mibBuilder.loadTexts: erxOc3.setStatus('current')
if mibBuilder.loadTexts: erxOc3.setDescription('The vendor type ID for an ERX dual port Optical Carrier 3 (OC-3/STM-1) SONET/SDH line module (Product Code: OC3-2).')
erxOc3Oc12Atm = ObjectIdentity((1, 3, 6, 1, 4, 1, 4874, 4, 2, 2, 1, 7, 10))
if mibBuilder.loadTexts: erxOc3Oc12Atm.setStatus('current')
if mibBuilder.loadTexts: erxOc3Oc12Atm.setDescription('The vendor type ID for an ERX OC3/OC12 multi-personality cell service line module (Product Code: OC3/OC12-ATM).')
erxOc3Oc12Pos = ObjectIdentity((1, 3, 6, 1, 4, 1, 4874, 4, 2, 2, 1, 7, 11))
if mibBuilder.loadTexts: erxOc3Oc12Pos.setStatus('current')
if mibBuilder.loadTexts: erxOc3Oc12Pos.setDescription('The vendor type ID for an ERX OC3/OC12 multi-personality packet service line module (Product Code: OC3/OC12-POS).')
erxCOcx = ObjectIdentity((1, 3, 6, 1, 4, 1, 4874, 4, 2, 2, 1, 7, 12))
if mibBuilder.loadTexts: erxCOcx.setStatus('current')
if mibBuilder.loadTexts: erxCOcx.setDescription('The vendor type ID for an ERX channelized OC3/STM1 and OC12/STM4 line module (Product Code: COCX/STMX-F0).')
erxFe2 = ObjectIdentity((1, 3, 6, 1, 4, 1, 4874, 4, 2, 2, 1, 7, 13))
if mibBuilder.loadTexts: erxFe2.setStatus('current')
if mibBuilder.loadTexts: erxFe2.setDescription('The vendor type ID for an ERX dual port fast (10/100) Ethernet line module (Product Code: 10/100_FE-2).')
erxGeFe = ObjectIdentity((1, 3, 6, 1, 4, 1, 4874, 4, 2, 2, 1, 7, 14))
if mibBuilder.loadTexts: erxGeFe.setStatus('current')
if mibBuilder.loadTexts: erxGeFe.setDescription('The vendor type ID for an ERX multi-personality gigabit or fast (10/100) Ethernet line module (Product Code: GE/FE-8).')
erxTunnelService = ObjectIdentity((1, 3, 6, 1, 4, 1, 4874, 4, 2, 2, 1, 7, 15))
if mibBuilder.loadTexts: erxTunnelService.setStatus('current')
if mibBuilder.loadTexts: erxTunnelService.setDescription('The vendor type ID for an ERX L2TP LNS and GRE Tunnel Service line module (Product Code: TUNNEL-SERVICE).')
erxHssi = ObjectIdentity((1, 3, 6, 1, 4, 1, 4874, 4, 2, 2, 1, 7, 16))
if mibBuilder.loadTexts: erxHssi.setStatus('current')
if mibBuilder.loadTexts: erxHssi.setDescription('The vendor type ID for an ERX 3 port High Speed Serial Interface (HSSI) line module (Product Code: HSSI-3F).')
erxVts = ObjectIdentity((1, 3, 6, 1, 4, 1, 4874, 4, 2, 2, 1, 7, 17))
if mibBuilder.loadTexts: erxVts.setStatus('current')
if mibBuilder.loadTexts: erxVts.setDescription('The vendor type ID for an ERX Virtual Tunnelling Server (VTS) line module (Product Code: ERX-IPSEC-MOD).')
erxCt3P12 = ObjectIdentity((1, 3, 6, 1, 4, 1, 4874, 4, 2, 2, 1, 7, 18))
if mibBuilder.loadTexts: erxCt3P12.setStatus('current')
if mibBuilder.loadTexts: erxCt3P12.setDescription('The vendor type ID for an ERX 12 port channelized T3 line module (Product Code: CT3-12-F0).')
erxV35 = ObjectIdentity((1, 3, 6, 1, 4, 1, 4874, 4, 2, 2, 1, 7, 19))
if mibBuilder.loadTexts: erxV35.setStatus('current')
if mibBuilder.loadTexts: erxV35.setDescription('The vendor type ID for an ERX X.21/V.35 server line module (Product Code: ERX-X21-V35-MOD).')
erxUt3E3Ocx = ObjectIdentity((1, 3, 6, 1, 4, 1, 4874, 4, 2, 2, 1, 7, 20))
if mibBuilder.loadTexts: erxUt3E3Ocx.setStatus('current')
if mibBuilder.loadTexts: erxUt3E3Ocx.setDescription('The vendor type ID for an ERX OC12, quad OC3 or 12 port T3/E3 server line module (Product Code: ERX-UT3E3OCX-MOD).')
erxLineIoAdapter = ObjectIdentity((1, 3, 6, 1, 4, 1, 4874, 4, 2, 2, 1, 8))
if mibBuilder.loadTexts: erxLineIoAdapter.setStatus('current')
if mibBuilder.loadTexts: erxLineIoAdapter.setDescription('The vendor type ID for an ERX I/O adapter for a line module.')
erxCt1Ioa = ObjectIdentity((1, 3, 6, 1, 4, 1, 4874, 4, 2, 2, 1, 8, 1))
if mibBuilder.loadTexts: erxCt1Ioa.setStatus('current')
if mibBuilder.loadTexts: erxCt1Ioa.setDescription('The vendor type ID for an ERX 24 port channelized T1/J1 I/O adapter (Product Code: CT1-FULL-I/O).')
erxCe1Ioa = ObjectIdentity((1, 3, 6, 1, 4, 1, 4874, 4, 2, 2, 1, 8, 2))
if mibBuilder.loadTexts: erxCe1Ioa.setStatus('current')
if mibBuilder.loadTexts: erxCe1Ioa.setDescription('The vendor type ID for an ERX 20 port channelized E1 I/O adapter (Product Code: CE1-FULL-I/O).')
erxCe1TIoa = ObjectIdentity((1, 3, 6, 1, 4, 1, 4874, 4, 2, 2, 1, 8, 3))
if mibBuilder.loadTexts: erxCe1TIoa.setStatus('current')
if mibBuilder.loadTexts: erxCe1TIoa.setDescription('The vendor type ID for an ERX 20 port channelized E1 Telco I/O adapter (Product Code: CE1-FULL-I/OT).')
erxCt3Ioa = ObjectIdentity((1, 3, 6, 1, 4, 1, 4874, 4, 2, 2, 1, 8, 4))
if mibBuilder.loadTexts: erxCt3Ioa.setStatus('current')
if mibBuilder.loadTexts: erxCt3Ioa.setDescription('The vendor type ID for an ERX 3 port channelized T3/E3 I/O adapter (Product Code: CT3/T3-3_I/O).')
erxE3Ioa = ObjectIdentity((1, 3, 6, 1, 4, 1, 4874, 4, 2, 2, 1, 8, 5))
if mibBuilder.loadTexts: erxE3Ioa.setStatus('current')
if mibBuilder.loadTexts: erxE3Ioa.setDescription('The vendor type ID for an ERX 3 port E3 I/O adapter (Product Code: E3-3_I/O).')
erxOc3Mm2Ioa = ObjectIdentity((1, 3, 6, 1, 4, 1, 4874, 4, 2, 2, 1, 8, 6))
if mibBuilder.loadTexts: erxOc3Mm2Ioa.setStatus('current')
if mibBuilder.loadTexts: erxOc3Mm2Ioa.setDescription('The vendor type ID for an ERX dual port OC3/STM1 multi-mode I/O adapter (Product Code: OC3-2M_I/O).')
erxOc3Sm2Ioa = ObjectIdentity((1, 3, 6, 1, 4, 1, 4874, 4, 2, 2, 1, 8, 7))
if mibBuilder.loadTexts: erxOc3Sm2Ioa.setStatus('current')
if mibBuilder.loadTexts: erxOc3Sm2Ioa.setDescription('The vendor type ID for an ERX dual port OC3/STM1 single-mode I/O adapter (Product Code: OC3-2S_I/O).')
erxOc3Mm4Ioa = ObjectIdentity((1, 3, 6, 1, 4, 1, 4874, 4, 2, 2, 1, 8, 8))
if mibBuilder.loadTexts: erxOc3Mm4Ioa.setStatus('current')
if mibBuilder.loadTexts: erxOc3Mm4Ioa.setDescription('The vendor type ID for an ERX 4 port OC3/STM1 multi-mode I/O adapter (Product Code: OC3-4MM_I/O).')
erxOc3SmIr4Ioa = ObjectIdentity((1, 3, 6, 1, 4, 1, 4874, 4, 2, 2, 1, 8, 9))
if mibBuilder.loadTexts: erxOc3SmIr4Ioa.setStatus('current')
if mibBuilder.loadTexts: erxOc3SmIr4Ioa.setDescription('The vendor type ID for an ERX 4 port OC3/STM single-mode intermediate- reach I/O adapter (Product Code: OC3-4SM_I/O).')
erxOc3SmLr4Ioa = ObjectIdentity((1, 3, 6, 1, 4, 1, 4874, 4, 2, 2, 1, 8, 10))
if mibBuilder.loadTexts: erxOc3SmLr4Ioa.setStatus('current')
if mibBuilder.loadTexts: erxOc3SmLr4Ioa.setDescription('The vendor type ID for an ERX 4 port OC3/STM1 single-mode long-reach I/O adapter (Product Code: OC3-4LH-I/O).')
erxCOc3Mm4Ioa = ObjectIdentity((1, 3, 6, 1, 4, 1, 4874, 4, 2, 2, 1, 8, 11))
if mibBuilder.loadTexts: erxCOc3Mm4Ioa.setStatus('current')
if mibBuilder.loadTexts: erxCOc3Mm4Ioa.setDescription('The vendor type ID for an ERX 4 port channelized OC3/STM multi-mode I/O adapter (Product Code: COC3F0-MM-I/O).')
erxCOc3SmIr4Ioa = ObjectIdentity((1, 3, 6, 1, 4, 1, 4874, 4, 2, 2, 1, 8, 12))
if mibBuilder.loadTexts: erxCOc3SmIr4Ioa.setStatus('current')
if mibBuilder.loadTexts: erxCOc3SmIr4Ioa.setDescription('The vendor type ID for an ERX 4 port channelized OC3/STM1 single-mode intermediate-reach I/O adapter (Product Code: COC3F0-SM-I/O).')
erxCOc3SmLr4Ioa = ObjectIdentity((1, 3, 6, 1, 4, 1, 4874, 4, 2, 2, 1, 8, 13))
if mibBuilder.loadTexts: erxCOc3SmLr4Ioa.setStatus('current')
if mibBuilder.loadTexts: erxCOc3SmLr4Ioa.setDescription('The vendor type ID for an ERX 4 port channelized OC3/STM1 single-mode long-reach I/O adapter (Product Code: ERX-COC3-4LH-IOA).')
erxOc12Mm1Ioa = ObjectIdentity((1, 3, 6, 1, 4, 1, 4874, 4, 2, 2, 1, 8, 14))
if mibBuilder.loadTexts: erxOc12Mm1Ioa.setStatus('current')
if mibBuilder.loadTexts: erxOc12Mm1Ioa.setDescription('The vendor type ID for an ERX single port OC12/STM4 multi-mode I/O adapter (Product Code: OC12-MM_I/O).')
erxOc12SmIr1Ioa = ObjectIdentity((1, 3, 6, 1, 4, 1, 4874, 4, 2, 2, 1, 8, 15))
if mibBuilder.loadTexts: erxOc12SmIr1Ioa.setStatus('current')
if mibBuilder.loadTexts: erxOc12SmIr1Ioa.setDescription('The vendor type ID for an ERX single port OC12/STM4 single-mode intermediate-reach I/O adapter (Product Code: OC12-SM_I/O).')
erxOc12SmLr1Ioa = ObjectIdentity((1, 3, 6, 1, 4, 1, 4874, 4, 2, 2, 1, 8, 16))
if mibBuilder.loadTexts: erxOc12SmLr1Ioa.setStatus('current')
if mibBuilder.loadTexts: erxOc12SmLr1Ioa.setDescription('The vendor type ID for an ERX single port OC12/STM4 single-mode long-reach I/O adapter (Product Code: OC12-LH-I/O).')
erxCOc12Mm1Ioa = ObjectIdentity((1, 3, 6, 1, 4, 1, 4874, 4, 2, 2, 1, 8, 17))
if mibBuilder.loadTexts: erxCOc12Mm1Ioa.setStatus('current')
if mibBuilder.loadTexts: erxCOc12Mm1Ioa.setDescription('The vendor type ID for an ERX single port channelized OC12/STM4 multi-mode I/O adapter (Product Code: COC12F0-MM-I/O).')
erxCOc12SmIr1Ioa = ObjectIdentity((1, 3, 6, 1, 4, 1, 4874, 4, 2, 2, 1, 8, 18))
if mibBuilder.loadTexts: erxCOc12SmIr1Ioa.setStatus('current')
if mibBuilder.loadTexts: erxCOc12SmIr1Ioa.setDescription('The vendor type ID for an ERX single port channelized OC12/STM4 single-mode intermediate-reach I/O adapter (Product Code: COC12F0-SM-I/O).')
erxCOc12SmLr1Ioa = ObjectIdentity((1, 3, 6, 1, 4, 1, 4874, 4, 2, 2, 1, 8, 19))
if mibBuilder.loadTexts: erxCOc12SmLr1Ioa.setStatus('current')
if mibBuilder.loadTexts: erxCOc12SmLr1Ioa.setDescription('The vendor type ID for an ERX single port channelized OC12/STM4 single-mode long-reach I/O adapter (Product Code: ERX-COC12-LH-IOA).')
erxFe2Ioa = ObjectIdentity((1, 3, 6, 1, 4, 1, 4874, 4, 2, 2, 1, 8, 20))
if mibBuilder.loadTexts: erxFe2Ioa.setStatus('current')
if mibBuilder.loadTexts: erxFe2Ioa.setDescription('The vendor type ID for an ERX dual port 10/100 Fast Ethernet I/O adapter (Product Code: 10/100_FE-2_I/O).')
erxFe8Ioa = ObjectIdentity((1, 3, 6, 1, 4, 1, 4874, 4, 2, 2, 1, 8, 21))
if mibBuilder.loadTexts: erxFe8Ioa.setStatus('current')
if mibBuilder.loadTexts: erxFe8Ioa.setDescription('The vendor type ID for an ERX 8 port 10/100 Fast Ethernet I/O adapter (Product Code: FE-8_I/O).')
erxGeMm1Ioa = ObjectIdentity((1, 3, 6, 1, 4, 1, 4874, 4, 2, 2, 1, 8, 22))
if mibBuilder.loadTexts: erxGeMm1Ioa.setStatus('current')
if mibBuilder.loadTexts: erxGeMm1Ioa.setDescription('The vendor type ID for an ERX single port Gigabit Ethernet multi-mode I/O adapter (Product Code: GE_M_I/O).')
erxGeSm1Ioa = ObjectIdentity((1, 3, 6, 1, 4, 1, 4874, 4, 2, 2, 1, 8, 23))
if mibBuilder.loadTexts: erxGeSm1Ioa.setStatus('current')
if mibBuilder.loadTexts: erxGeSm1Ioa.setDescription('The vendor type ID for an ERX single port Gigabit Ethernet single-mode I/O adapter (Product Code: GE_S_I/O).')
erxHssiIoa = ObjectIdentity((1, 3, 6, 1, 4, 1, 4874, 4, 2, 2, 1, 8, 24))
if mibBuilder.loadTexts: erxHssiIoa.setStatus('current')
if mibBuilder.loadTexts: erxHssiIoa.setDescription('The vendor type ID for an ERX 3 port High Speed Serial Interface (HSSI) I/O adapter (Product Code: HSSI-3-I/O).')
erxCt3P12Ioa = ObjectIdentity((1, 3, 6, 1, 4, 1, 4874, 4, 2, 2, 1, 8, 25))
if mibBuilder.loadTexts: erxCt3P12Ioa.setStatus('current')
if mibBuilder.loadTexts: erxCt3P12Ioa.setDescription('The vendor type ID for an ERX 12 port channelized T3 I/O adapter (Product Code: T312-F0-F3-I/O).')
erxV35Ioa = ObjectIdentity((1, 3, 6, 1, 4, 1, 4874, 4, 2, 2, 1, 8, 26))
if mibBuilder.loadTexts: erxV35Ioa.setStatus('current')
if mibBuilder.loadTexts: erxV35Ioa.setDescription('The vendor type ID for an ERX X.21/V.35 I/O adapter (Product Code: ERX-X21-V35-IOA).')
erxGeSfpIoa = ObjectIdentity((1, 3, 6, 1, 4, 1, 4874, 4, 2, 2, 1, 8, 27))
if mibBuilder.loadTexts: erxGeSfpIoa.setStatus('current')
if mibBuilder.loadTexts: erxGeSfpIoa.setDescription('The vendor type ID for an ERX single port Gigabit Ethernet SFP I/O adapter (Product Code: ERX-GIGESFP-IOA).')
erxE3P12Ioa = ObjectIdentity((1, 3, 6, 1, 4, 1, 4874, 4, 2, 2, 1, 8, 28))
if mibBuilder.loadTexts: erxE3P12Ioa.setStatus('current')
if mibBuilder.loadTexts: erxE3P12Ioa.setDescription('The vendor type ID for an ERX 12-port E3 I/O adapter (Product Code: E3-12-F3-I/O).')
erxCOc12Mm2Ioa = ObjectIdentity((1, 3, 6, 1, 4, 1, 4874, 4, 2, 2, 1, 8, 30))
if mibBuilder.loadTexts: erxCOc12Mm2Ioa.setStatus('current')
if mibBuilder.loadTexts: erxCOc12Mm2Ioa.setDescription('The vendor type ID for an ERX dual port OC12/STM4 channelized multi-mode I/O adapter (Product Code: ERX-COC12-MA-IOA).')
erxCOc12SmIr2Ioa = ObjectIdentity((1, 3, 6, 1, 4, 1, 4874, 4, 2, 2, 1, 8, 31))
if mibBuilder.loadTexts: erxCOc12SmIr2Ioa.setStatus('current')
if mibBuilder.loadTexts: erxCOc12SmIr2Ioa.setDescription('The vendor type ID for an ERX dual port OC12/STM4 channelized single-mode intermediate-reach I/O adapter (Product Code: ERX-COC12-SA-IOA).')
erxCOc12SmLr2Ioa = ObjectIdentity((1, 3, 6, 1, 4, 1, 4874, 4, 2, 2, 1, 8, 32))
if mibBuilder.loadTexts: erxCOc12SmLr2Ioa.setStatus('current')
if mibBuilder.loadTexts: erxCOc12SmLr2Ioa.setDescription('The vendor type ID for an ERX dual port OC12/STM4 channelized single-mode long-reach I/O adapter (Product Code: ERX-COC12-LA-IOA).')
erxOc12Mm2ApsIoa = ObjectIdentity((1, 3, 6, 1, 4, 1, 4874, 4, 2, 2, 1, 8, 33))
if mibBuilder.loadTexts: erxOc12Mm2ApsIoa.setStatus('current')
if mibBuilder.loadTexts: erxOc12Mm2ApsIoa.setDescription('The vendor type ID for an ERX dual port OC12/STM4 multi-mode with APS I/O adapter (Product Code: ERX-OC12MM-A-IOA).')
erxOc12SmIr2ApsIoa = ObjectIdentity((1, 3, 6, 1, 4, 1, 4874, 4, 2, 2, 1, 8, 34))
if mibBuilder.loadTexts: erxOc12SmIr2ApsIoa.setStatus('current')
if mibBuilder.loadTexts: erxOc12SmIr2ApsIoa.setDescription('The vendor type ID for an ERX dual port OC12/STM4 single-mode intermediate-reach with APS I/O adapter (Product Code: ERX-OC12SM-A-IOA).')
erxOc12SmLr2ApsIoa = ObjectIdentity((1, 3, 6, 1, 4, 1, 4874, 4, 2, 2, 1, 8, 35))
if mibBuilder.loadTexts: erxOc12SmLr2ApsIoa.setStatus('current')
if mibBuilder.loadTexts: erxOc12SmLr2ApsIoa.setDescription('The vendor type ID for an ERX dual port OC12/STM4 single-mode long-reach with APS I/O adapter (Product Code: ERX-OC12LH-A-IOA).')
erxT1E1RMidSpareIoa = ObjectIdentity((1, 3, 6, 1, 4, 1, 4874, 4, 2, 2, 1, 8, 42))
if mibBuilder.loadTexts: erxT1E1RMidSpareIoa.setStatus('current')
if mibBuilder.loadTexts: erxT1E1RMidSpareIoa.setDescription('The vendor type ID for an ERX T1/E1 redundant midplane spare I/O adapter (Product Code: PNL-RDMD-T1/E1).')
erxT3E3RMidSpareIoa = ObjectIdentity((1, 3, 6, 1, 4, 1, 4874, 4, 2, 2, 1, 8, 43))
if mibBuilder.loadTexts: erxT3E3RMidSpareIoa.setStatus('current')
if mibBuilder.loadTexts: erxT3E3RMidSpareIoa.setDescription('The vendor type ID for an ERX T3/E3 redundant midplane spare I/O adapter (Product Code: PNL-RDMD-T3/E3).')
erxCt3RMidSpareIoa = ObjectIdentity((1, 3, 6, 1, 4, 1, 4874, 4, 2, 2, 1, 8, 44))
if mibBuilder.loadTexts: erxCt3RMidSpareIoa.setStatus('current')
if mibBuilder.loadTexts: erxCt3RMidSpareIoa.setDescription('The vendor type ID for an ERX 12 port channelized T3 redundant midplane spare I/O adapter (Product Code: ERX-12PT3E3-PNL).')
erxOcxRMidSpareIoa = ObjectIdentity((1, 3, 6, 1, 4, 1, 4874, 4, 2, 2, 1, 8, 45))
if mibBuilder.loadTexts: erxOcxRMidSpareIoa.setStatus('current')
if mibBuilder.loadTexts: erxOcxRMidSpareIoa.setDescription('The vendor type ID for an ERX OC3/OC12 redundant midplane spare I/O adapter (Product Code: PNL-RDMD-OCX).')
erxCOcxRMidSpareIoa = ObjectIdentity((1, 3, 6, 1, 4, 1, 4874, 4, 2, 2, 1, 8, 46))
if mibBuilder.loadTexts: erxCOcxRMidSpareIoa.setStatus('current')
if mibBuilder.loadTexts: erxCOcxRMidSpareIoa.setDescription('The vendor type ID for an ERX OC3/OC12 channelized redundant midplane spare I/O adapter (Product Code: ERX-COCXPNL-IOA).')
mibBuilder.exportSymbols("Unisphere-Data-ERX-Registry", erxE3Frame=erxE3Frame, erxGeFe=erxGeFe, erxCOc12SmLr1Ioa=erxCOc12SmLr1Ioa, erxTunnelService=erxTunnelService, erxSrp10=erxSrp10, erx1400Midplane=erx1400Midplane, erxE3P12Ioa=erxE3P12Ioa, erx700Midplane=erx700Midplane, erxLineModule=erxLineModule, erxGeSm1Ioa=erxGeSm1Ioa, erxOc3Mm4Ioa=erxOc3Mm4Ioa, erxSrp5Plus=erxSrp5Plus, erxCOcx=erxCOcx, erxE3Ioa=erxE3Ioa, erxOcxRMidSpareIoa=erxOcxRMidSpareIoa, erxFe2=erxFe2, erxCt3RMidSpareIoa=erxCt3RMidSpareIoa, erxLineIoAdapter=erxLineIoAdapter, erxV35Ioa=erxV35Ioa, erxCOc3SmLr4Ioa=erxCOc3SmLr4Ioa, erxOc3Mm2Ioa=erxOc3Mm2Ioa, usdErxRegistry=usdErxRegistry, erxT3Frame=erxT3Frame, erxT3E3RMidSpareIoa=erxT3E3RMidSpareIoa, erx1400Chassis=erx1400Chassis, erxV35=erxV35, erxCe1TIoa=erxCe1TIoa, erxSrp40=erxSrp40, erx3Plus1RedundantT3E3Midplane=erx3Plus1RedundantT3E3Midplane, erxSrp40Plus=erxSrp40Plus, erx700FanAssembly=erx700FanAssembly, erxOc12SmLr2ApsIoa=erxOc12SmLr2ApsIoa, erxChassis=erxChassis, erxOc3Oc12Pos=erxOc3Oc12Pos, erxSrp5=erxSrp5, erxCe1=erxCe1, erxHssiIoa=erxHssiIoa, erx1Plus1RedundantOcMidplane=erx1Plus1RedundantOcMidplane, erx700Chassis=erx700Chassis, erxUt3E3Ocx=erxUt3E3Ocx, erx2Plus1RedundantOcMidplane=erx2Plus1RedundantOcMidplane, erx5Plus1RedundantT1E1Midplane=erx5Plus1RedundantT1E1Midplane, erxE3Atm=erxE3Atm, erxGeSfpIoa=erxGeSfpIoa, erxCOc12SmLr2Ioa=erxCOc12SmLr2Ioa, erxCOc12SmIr1Ioa=erxCOc12SmIr1Ioa, erxSrp10Ecc=erxSrp10Ecc, erx4Plus1RedundantT1E1Midplane=erx4Plus1RedundantT1E1Midplane, erxOc12SmLr1Ioa=erxOc12SmLr1Ioa, erxT1E1RMidSpareIoa=erxT1E1RMidSpareIoa, erxFe2Ioa=erxFe2Ioa, erxCe1Ioa=erxCe1Ioa, erxCt3=erxCt3, erx4Plus1RedundantT3E3Midplane=erx4Plus1RedundantT3E3Midplane, erxMidplane=erxMidplane, erxOc12SmIr2ApsIoa=erxOc12SmIr2ApsIoa, erxCOcxRMidSpareIoa=erxCOcxRMidSpareIoa, erxOc3SmIr4Ioa=erxOc3SmIr4Ioa, erx2Plus1RedundantT3E3Midplane=erx2Plus1RedundantT3E3Midplane, erxOc12SmIr1Ioa=erxOc12SmIr1Ioa, erxCOc12SmIr2Ioa=erxCOc12SmIr2Ioa, erxOc12Mm2ApsIoa=erxOc12Mm2ApsIoa, erxOc3SmLr4Ioa=erxOc3SmLr4Ioa, erx1400FanAssembly=erx1400FanAssembly, erxT3Atm=erxT3Atm, erxPowerInput=erxPowerInput, erxCt1=erxCt1, erxSrpIoAdapter=erxSrpIoAdapter, erx5Plus1RedundantT3E3Midplane=erx5Plus1RedundantT3E3Midplane, erx5Plus1RedundantOcMidplane=erx5Plus1RedundantOcMidplane, erxOc12Mm1Ioa=erxOc12Mm1Ioa, PYSNMP_MODULE_ID=usdErxRegistry, erxFe8Ioa=erxFe8Ioa, usdErxEntPhysicalType=usdErxEntPhysicalType, erxFanAssembly=erxFanAssembly, erxCt3Ioa=erxCt3Ioa, erx3Plus1RedundantT1E1Midplane=erx3Plus1RedundantT1E1Midplane, erx3Plus1RedundantOcMidplane=erx3Plus1RedundantOcMidplane, erxSrpModule=erxSrpModule, erxOc3Oc12Atm=erxOc3Oc12Atm, erxCt1Ioa=erxCt1Ioa, erx2Plus1RedundantT1E1Midplane=erx2Plus1RedundantT1E1Midplane, erxOc3=erxOc3, erxHssi=erxHssi, erxCt3P12Ioa=erxCt3P12Ioa, erxCOc3SmIr4Ioa=erxCOc3SmIr4Ioa, erx1Plus1RedundantT1E1Midplane=erx1Plus1RedundantT1E1Midplane, erxVts=erxVts, erx1Plus1RedundantT3E3Midplane=erx1Plus1RedundantT3E3Midplane, erx4Plus1RedundantOcMidplane=erx4Plus1RedundantOcMidplane, erxCOc12Mm2Ioa=erxCOc12Mm2Ioa, erxCOc12Mm1Ioa=erxCOc12Mm1Ioa, erxCt3P12=erxCt3P12, erxCOc3Mm4Ioa=erxCOc3Mm4Ioa, erxGeMm1Ioa=erxGeMm1Ioa, erxOc3Sm2Ioa=erxOc3Sm2Ioa)