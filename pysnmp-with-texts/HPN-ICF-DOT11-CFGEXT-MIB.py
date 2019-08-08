#
# PySNMP MIB module HPN-ICF-DOT11-CFGEXT-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/HPN-ICF-DOT11-CFGEXT-MIB
# Produced by pysmi-0.3.4 at Wed May  1 13:38:06 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, ConstraintsIntersection, SingleValueConstraint, ConstraintsUnion, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "ConstraintsIntersection", "SingleValueConstraint", "ConstraintsUnion", "ValueSizeConstraint")
hpnicfDot11, = mibBuilder.importSymbols("HPN-ICF-DOT11-REF-MIB", "hpnicfDot11")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
TimeTicks, MibIdentifier, IpAddress, Integer32, Counter64, NotificationType, Counter32, MibScalar, MibTable, MibTableRow, MibTableColumn, ModuleIdentity, Gauge32, ObjectIdentity, iso, Unsigned32, Bits = mibBuilder.importSymbols("SNMPv2-SMI", "TimeTicks", "MibIdentifier", "IpAddress", "Integer32", "Counter64", "NotificationType", "Counter32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "ModuleIdentity", "Gauge32", "ObjectIdentity", "iso", "Unsigned32", "Bits")
DisplayString, RowStatus, TextualConvention, TruthValue = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "RowStatus", "TextualConvention", "TruthValue")
hpnicfDot11CFGEXT = ModuleIdentity((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 6))
hpnicfDot11CFGEXT.setRevisions(('2010-06-02 14:00', '2007-04-25 20:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: hpnicfDot11CFGEXT.setRevisionsDescriptions(('Modified to add new nodes.', 'The initial revision of this MIB module.',))
if mibBuilder.loadTexts: hpnicfDot11CFGEXT.setLastUpdated('201006021400Z')
if mibBuilder.loadTexts: hpnicfDot11CFGEXT.setOrganization('')
if mibBuilder.loadTexts: hpnicfDot11CFGEXT.setContactInfo('')
if mibBuilder.loadTexts: hpnicfDot11CFGEXT.setDescription('This MIB provides information for WLAN configuration extended. The HPN-ICF-DOT11-CFG-MIB define MIB objects for WLAN basic configuration, while this MIB will define MIB objects for load balance these kinds feature. GLOSSARY IEEE 802.11 Standard to encourage interoperability among wireless networking equipment. Access point (AP) Transmitter/receiver (transceiver) device that commonly connects and transports data between a wireless network and a wired network. Access control (AC) To control and manage multi-APs, it will bridge wireless and wired network. Fat AP Applied in the home, SOHO and so on, and it could work independently without help from AC. Fit AP Applied in the enterprise environment, it will work under the control and management from AC. Control And Provisioning of Wireless Access Points Protocol The short name of protocol is CAPWAP. AC will control and manage AP by CAPWAP tunnel protocol defined by IETF. Also, a data tunnel will be set up between AC and AP. BSS IEEE 802.11 Basic Service Set (Radio Cell). The BSS of an AP comprises of the stations directly associating with the AP. Radio The chip set to receive and send wireless signal. Association The service used to establish access point or station mapping and enable station invocation of the distribution system services. (Wireless clients attempt to connect to access points.) Basic Rate A data rate that is mandatory for client devices to support in order for them to achieve successful association. MSDU MAC Service Data Unit, it is frame format defined by 802.11. TU It is 1,024 microseconds (ms), which is about 1 millisecond. AKM The authentication and key management method defined by 802.11i, and which includes 802.1x and pre-shared key.')
hpnicfDot11LoadBalance = MibIdentifier((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 6, 1))
hpnicfDot11LBGlobalGroup = MibIdentifier((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 6, 1, 1))
hpnicfDot11LoadBalanceTrafficEnable = MibScalar((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 6, 1, 1, 1), TruthValue()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hpnicfDot11LoadBalanceTrafficEnable.setStatus('current')
if mibBuilder.loadTexts: hpnicfDot11LoadBalanceTrafficEnable.setDescription('Represents whether enable load balancing according to station traffic.')
hpnicfDot11LoadBalanceTrafficThres = MibScalar((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 6, 1, 1, 2), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hpnicfDot11LoadBalanceTrafficThres.setStatus('current')
if mibBuilder.loadTexts: hpnicfDot11LoadBalanceTrafficThres.setDescription('Represents the threshold value for Traffic based load balancing.')
hpnicfDot11LoadBalanceSessionEnable = MibScalar((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 6, 1, 1, 3), TruthValue()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hpnicfDot11LoadBalanceSessionEnable.setStatus('current')
if mibBuilder.loadTexts: hpnicfDot11LoadBalanceSessionEnable.setDescription('Represents whether enable load balancing according to station session number.')
hpnicfDot11LoadBalanceSessionThres = MibScalar((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 6, 1, 1, 4), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hpnicfDot11LoadBalanceSessionThres.setStatus('current')
if mibBuilder.loadTexts: hpnicfDot11LoadBalanceSessionThres.setDescription('Represents the threshold value for session number based load balancing.')
hpnicfDot11LoadBalanceTrafficGap = MibScalar((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 6, 1, 1, 5), Integer32().subtype(subtypeSpec=ValueRangeConstraint(10, 40)).clone(20)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hpnicfDot11LoadBalanceTrafficGap.setStatus('current')
if mibBuilder.loadTexts: hpnicfDot11LoadBalanceTrafficGap.setDescription('Traffic gap threshold. Load balancing is carried out for a radio when the traffic threshold and session gap are exceeded.')
hpnicfDot11LoadBalanceSessionGap = MibScalar((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 6, 1, 1, 6), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 8)).clone(4)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hpnicfDot11LoadBalanceSessionGap.setStatus('current')
if mibBuilder.loadTexts: hpnicfDot11LoadBalanceSessionGap.setDescription('Session gap threshold. Load balancing is carried out for a radio when the session threshold and session gap are exceeded.')
hpnicfDot11LBTrafficThresKbps = MibScalar((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 6, 1, 1, 7), Integer32()).setUnits('kbps').setMaxAccess("readwrite")
if mibBuilder.loadTexts: hpnicfDot11LBTrafficThresKbps.setStatus('current')
if mibBuilder.loadTexts: hpnicfDot11LBTrafficThresKbps.setDescription('Represents the threshold value for Traffic based load balancing.')
hpnicfDot11LBTrafficGapKbps = MibScalar((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 6, 1, 1, 8), Integer32()).setUnits('kbps').setMaxAccess("readwrite")
if mibBuilder.loadTexts: hpnicfDot11LBTrafficGapKbps.setStatus('current')
if mibBuilder.loadTexts: hpnicfDot11LBTrafficGapKbps.setDescription('Traffic gap threshold. Load balancing is carried out for a radio when the traffic threshold gap are exceeded.')
hpnicfDot11LBRadioGroupTable = MibTable((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 6, 1, 2), )
if mibBuilder.loadTexts: hpnicfDot11LBRadioGroupTable.setStatus('current')
if mibBuilder.loadTexts: hpnicfDot11LBRadioGroupTable.setDescription('This table defines load balance radio group.')
hpnicfDot11LBRadioGroupEntry = MibTableRow((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 6, 1, 2, 1), ).setIndexNames((0, "HPN-ICF-DOT11-CFGEXT-MIB", "hpnicfDot11LBRadioGroupId"))
if mibBuilder.loadTexts: hpnicfDot11LBRadioGroupEntry.setStatus('current')
if mibBuilder.loadTexts: hpnicfDot11LBRadioGroupEntry.setDescription('Each entry contains information of one load balance radio group.')
hpnicfDot11LBRadioGroupId = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 6, 1, 2, 1, 1), Unsigned32())
if mibBuilder.loadTexts: hpnicfDot11LBRadioGroupId.setStatus('current')
if mibBuilder.loadTexts: hpnicfDot11LBRadioGroupId.setDescription('Represents load balance radio group ID.')
hpnicfDot11LBRadioGroupDesc = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 6, 1, 2, 1, 2), OctetString()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hpnicfDot11LBRadioGroupDesc.setStatus('current')
if mibBuilder.loadTexts: hpnicfDot11LBRadioGroupDesc.setDescription('Represents the description of load balance radio group.')
hpnicfDot11LBRadioGroupRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 6, 1, 2, 1, 3), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hpnicfDot11LBRadioGroupRowStatus.setStatus('current')
if mibBuilder.loadTexts: hpnicfDot11LBRadioGroupRowStatus.setDescription('The row status of this table entry.')
mibBuilder.exportSymbols("HPN-ICF-DOT11-CFGEXT-MIB", hpnicfDot11LoadBalance=hpnicfDot11LoadBalance, hpnicfDot11LBGlobalGroup=hpnicfDot11LBGlobalGroup, hpnicfDot11LoadBalanceTrafficThres=hpnicfDot11LoadBalanceTrafficThres, hpnicfDot11LoadBalanceSessionEnable=hpnicfDot11LoadBalanceSessionEnable, hpnicfDot11CFGEXT=hpnicfDot11CFGEXT, hpnicfDot11LoadBalanceSessionThres=hpnicfDot11LoadBalanceSessionThres, PYSNMP_MODULE_ID=hpnicfDot11CFGEXT, hpnicfDot11LBTrafficGapKbps=hpnicfDot11LBTrafficGapKbps, hpnicfDot11LBTrafficThresKbps=hpnicfDot11LBTrafficThresKbps, hpnicfDot11LBRadioGroupEntry=hpnicfDot11LBRadioGroupEntry, hpnicfDot11LoadBalanceTrafficEnable=hpnicfDot11LoadBalanceTrafficEnable, hpnicfDot11LBRadioGroupId=hpnicfDot11LBRadioGroupId, hpnicfDot11LoadBalanceTrafficGap=hpnicfDot11LoadBalanceTrafficGap, hpnicfDot11LBRadioGroupRowStatus=hpnicfDot11LBRadioGroupRowStatus, hpnicfDot11LBRadioGroupTable=hpnicfDot11LBRadioGroupTable, hpnicfDot11LBRadioGroupDesc=hpnicfDot11LBRadioGroupDesc, hpnicfDot11LoadBalanceSessionGap=hpnicfDot11LoadBalanceSessionGap)