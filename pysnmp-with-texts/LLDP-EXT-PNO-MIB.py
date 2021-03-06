#
# PySNMP MIB module LLDP-EXT-PNO-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/LLDP-EXT-PNO-MIB
# Produced by pysmi-0.3.4 at Wed May  1 14:08:33 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ValueSizeConstraint, SingleValueConstraint, ValueRangeConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ValueSizeConstraint", "SingleValueConstraint", "ValueRangeConstraint", "ConstraintsUnion")
lldpRemLocalPortNum, lldpExtensions, lldpLocPortNum, lldpRemIndex, lldpPortConfigEntry, lldpRemTimeMark = mibBuilder.importSymbols("LLDP-MIB", "lldpRemLocalPortNum", "lldpExtensions", "lldpLocPortNum", "lldpRemIndex", "lldpPortConfigEntry", "lldpRemTimeMark")
SnmpAdminString, = mibBuilder.importSymbols("SNMP-FRAMEWORK-MIB", "SnmpAdminString")
ModuleCompliance, ObjectGroup, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "ObjectGroup", "NotificationGroup")
MibScalar, MibTable, MibTableRow, MibTableColumn, TimeTicks, Gauge32, IpAddress, NotificationType, iso, ModuleIdentity, Counter32, MibIdentifier, Integer32, Unsigned32, ObjectIdentity, Bits, Counter64 = mibBuilder.importSymbols("SNMPv2-SMI", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "TimeTicks", "Gauge32", "IpAddress", "NotificationType", "iso", "ModuleIdentity", "Counter32", "MibIdentifier", "Integer32", "Unsigned32", "ObjectIdentity", "Bits", "Counter64")
DisplayString, TextualConvention, TruthValue = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention", "TruthValue")
lldpXPnoMIB = ModuleIdentity((1, 0, 8802, 1, 1, 2, 1, 5, 3791))
lldpXPnoMIB.setRevisions(('2006-03-09 00:00', '2006-02-28 00:00', '2005-08-31 00:00', '2005-05-30 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: lldpXPnoMIB.setRevisionsDescriptions(('MRRT status added', ' added MRP UUID information, port status values and naming of tables changed ', 'added RT port status', 'initial version',))
if mibBuilder.loadTexts: lldpXPnoMIB.setLastUpdated('200603090000Z')
if mibBuilder.loadTexts: lldpXPnoMIB.setOrganization('PROFIBUS International (PNO)')
if mibBuilder.loadTexts: lldpXPnoMIB.setContactInfo(' URL: http://www.profibus.com email: info@profibus.com Postal: Haid-und-Neu-Strasse 7 D-76131 Karlsruhe Tel: ++49 721 9658 - 590 ')
if mibBuilder.loadTexts: lldpXPnoMIB.setDescription(' The LLDP Management Information Base extension module for PROFINET organizationally defined discovery information. Copyright (C) PROFIBUS Nutzerorganisation e.V. (2005). ')
lldpXPnoObjects = MibIdentifier((1, 0, 8802, 1, 1, 2, 1, 5, 3791, 1))
lldpXPnoConfig = MibIdentifier((1, 0, 8802, 1, 1, 2, 1, 5, 3791, 1, 1))
lldpXPnoLocalData = MibIdentifier((1, 0, 8802, 1, 1, 2, 1, 5, 3791, 1, 2))
lldpXPnoRemoteData = MibIdentifier((1, 0, 8802, 1, 1, 2, 1, 5, 3791, 1, 3))
lldpXPnoConfigTable = MibTable((1, 0, 8802, 1, 1, 2, 1, 5, 3791, 1, 1, 1), )
if mibBuilder.loadTexts: lldpXPnoConfigTable.setStatus('current')
if mibBuilder.loadTexts: lldpXPnoConfigTable.setDescription(' A table that controls selection of LLDP TLVs to be transmitted on individual ports. ')
lldpXPnoConfigEntry = MibTableRow((1, 0, 8802, 1, 1, 2, 1, 5, 3791, 1, 1, 1, 1), )
lldpPortConfigEntry.registerAugmentions(("LLDP-EXT-PNO-MIB", "lldpXPnoConfigEntry"))
lldpXPnoConfigEntry.setIndexNames(*lldpPortConfigEntry.getIndexNames())
if mibBuilder.loadTexts: lldpXPnoConfigEntry.setStatus('current')
if mibBuilder.loadTexts: lldpXPnoConfigEntry.setDescription(' LLDP configuration information that controls the transmission of PNO organizationally defined TLVs on LLDP transmission capable ports. This configuration object augments the lldpPortConfigEntry of the LLDP-MIB, therefore it is only present along with the port configuration defined by the associated lldpPortConfigEntry entry. Each active lldpXPnoConfigEntry must be restored from non-volatile storage (along with the corresponding lldpPortConfigEntry) after a re-initialization of the management system. ')
lldpXPnoConfigSPDTxEnable = MibTableColumn((1, 0, 8802, 1, 1, 2, 1, 5, 3791, 1, 1, 1, 1, 1), TruthValue().clone('true')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: lldpXPnoConfigSPDTxEnable.setStatus('current')
if mibBuilder.loadTexts: lldpXPnoConfigSPDTxEnable.setDescription(" The lldpXPnoConfigSPDTxEnable, which is defined as a truth value and configured by the network management, determines whether the PNO organizationally defined signal propagation delay TLV transmission is allowed on a given LLDP transmission capable port. The signal propagation delay is composed of the port transmission delay, the port receiving delay and the line delay. These values can't be transmitted independently of each other. The value of this object must be restored from nonvolatile storage after a re-initialization of the management system. ")
lldpXPnoConfigPortStatusTxEnable = MibTableColumn((1, 0, 8802, 1, 1, 2, 1, 5, 3791, 1, 1, 1, 1, 2), TruthValue().clone('true')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: lldpXPnoConfigPortStatusTxEnable.setStatus('current')
if mibBuilder.loadTexts: lldpXPnoConfigPortStatusTxEnable.setDescription(' The lldpXPnoConfigPortStatusTxEnable, which is defined as a truth value and configured by the network management, determines whether the PNO organizationally defined RT port status TLV transmission is allowed on a given LLDP transmission capable port. The value of this object must be restored from nonvolatile storage after a re-initialization of the management system. ')
lldpXPnoConfigAliasTxEnable = MibTableColumn((1, 0, 8802, 1, 1, 2, 1, 5, 3791, 1, 1, 1, 1, 3), TruthValue().clone('false')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: lldpXPnoConfigAliasTxEnable.setStatus('current')
if mibBuilder.loadTexts: lldpXPnoConfigAliasTxEnable.setDescription(' The lldpXPnoConfigAliasTxEnable, which is defined as a truth value and configured by the network management, determines whether the PNO organizationally defined alias TLV (chassisId) transmission is allowed on a given LLDP transmission capable port. The value of this object must be restored from nonvolatile storage after a re-initialization of the management system. ')
lldpXPnoConfigMrpTxEnable = MibTableColumn((1, 0, 8802, 1, 1, 2, 1, 5, 3791, 1, 1, 1, 1, 4), TruthValue().clone('true')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: lldpXPnoConfigMrpTxEnable.setStatus('current')
if mibBuilder.loadTexts: lldpXPnoConfigMrpTxEnable.setDescription(' The lldpXPnoConfigMrpTxEnable, which is defined as a truth value and configured by the network management, determines whether the PNO organizationally defined MRP TLV transmission is allowed on a given LLDP transmission capable port. The value of this object must be restored from nonvolatile storage after a re-initialization of the management system. ')
lldpXPnoLocTable = MibTable((1, 0, 8802, 1, 1, 2, 1, 5, 3791, 1, 2, 1), )
if mibBuilder.loadTexts: lldpXPnoLocTable.setStatus('current')
if mibBuilder.loadTexts: lldpXPnoLocTable.setDescription(' This table contains one row per port for PNO organizationally defined LLDP extension on the local system known to this agent. ')
lldpXPnoLocEntry = MibTableRow((1, 0, 8802, 1, 1, 2, 1, 5, 3791, 1, 2, 1, 1), ).setIndexNames((0, "LLDP-MIB", "lldpLocPortNum"))
if mibBuilder.loadTexts: lldpXPnoLocEntry.setStatus('current')
if mibBuilder.loadTexts: lldpXPnoLocEntry.setDescription(' Additional information about a particular port component. This object is indexed by the lldpLocPortNum of the LLDP-MIB, therefore it is only present along with the port entry defined by the associated lldpLocPortEntry entry. Each active lldpXPnoLocEntry must be restored from non-volatile storage (along with the corresponding lldpLocPortEntry) after a re-initialization of the management system. ')
lldpXPnoLocLPDValue = MibTableColumn((1, 0, 8802, 1, 1, 2, 1, 5, 3791, 1, 2, 1, 1, 1), Unsigned32()).setUnits('ns').setMaxAccess("readonly")
if mibBuilder.loadTexts: lldpXPnoLocLPDValue.setStatus('current')
if mibBuilder.loadTexts: lldpXPnoLocLPDValue.setDescription(' This integer value represents the line propagation delay in nanoseconds which was measured by the local system on the corresponding port. A value of zero shall be used if the system either could not accomplish the measurement or does not support such a measurement. ')
lldpXPnoLocPortTxDValue = MibTableColumn((1, 0, 8802, 1, 1, 2, 1, 5, 3791, 1, 2, 1, 1, 2), Unsigned32()).setUnits('ns').setMaxAccess("readonly")
if mibBuilder.loadTexts: lldpXPnoLocPortTxDValue.setStatus('current')
if mibBuilder.loadTexts: lldpXPnoLocPortTxDValue.setDescription(' This integer value represents the PortTxDelay in nanoseconds which was measured by the local system on the corresponding port. A value of zero shall be used if the system either could not accomplish the measurement or does not support such a measurement. ')
lldpXPnoLocPortRxDValue = MibTableColumn((1, 0, 8802, 1, 1, 2, 1, 5, 3791, 1, 2, 1, 1, 3), Unsigned32()).setUnits('ns').setMaxAccess("readonly")
if mibBuilder.loadTexts: lldpXPnoLocPortRxDValue.setStatus('current')
if mibBuilder.loadTexts: lldpXPnoLocPortRxDValue.setDescription(' This integer value represents the PortRxDelay in nanoseconds which was measured by the local system on the corresponding port. A value of zero shall be used if the system either could not accomplish the measurement or does not support such a measurement. ')
lldpXPnoLocPortStatusRT2 = MibTableColumn((1, 0, 8802, 1, 1, 2, 1, 5, 3791, 1, 2, 1, 1, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1, 2))).clone(namedValues=NamedValues(("off", 0), ("configured", 1), ("running", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: lldpXPnoLocPortStatusRT2.setStatus('current')
if mibBuilder.loadTexts: lldpXPnoLocPortStatusRT2.setDescription(" This value represents the status of the corresponding port of the local system according to RT class 2. A value of off(0) means that there isn't any RT2 capability available for this port. When the port is configured for RT2 mode, but the mode isn't active yet the value will be configured(1). If the RT2 mode is configured for this port and the mode is active, the value will be running(2). ")
lldpXPnoLocPortStatusRT3 = MibTableColumn((1, 0, 8802, 1, 1, 2, 1, 5, 3791, 1, 2, 1, 1, 5), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3, 4))).clone(namedValues=NamedValues(("off", 0), ("configured", 1), ("up", 2), ("down", 3), ("running", 4)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: lldpXPnoLocPortStatusRT3.setStatus('current')
if mibBuilder.loadTexts: lldpXPnoLocPortStatusRT3.setDescription(" This value represents the status of the corresponding port of the local system according to RT class 3. A value of off(0) means that there isn't any RT3 capability available for this port. When the port is configured for RT3 mode, but the mode isn't active yet the value will be configured(1). When the port is ready for transmission and reception of RT3 traffic, the port status will be running(4). ")
lldpXPnoLocPortNoS = MibTableColumn((1, 0, 8802, 1, 1, 2, 1, 5, 3791, 1, 2, 1, 1, 6), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: lldpXPnoLocPortNoS.setStatus('current')
if mibBuilder.loadTexts: lldpXPnoLocPortNoS.setDescription(" The local PROFINET NameofStation. If the station isn't configured yet, the value of this object will be the MAC address of the device as a string. ")
lldpXPnoLocPortMrpUuId = MibTableColumn((1, 0, 8802, 1, 1, 2, 1, 5, 3791, 1, 2, 1, 1, 7), OctetString().subtype(subtypeSpec=ValueSizeConstraint(16, 16)).setFixedLength(16)).setMaxAccess("readonly")
if mibBuilder.loadTexts: lldpXPnoLocPortMrpUuId.setStatus('current')
if mibBuilder.loadTexts: lldpXPnoLocPortMrpUuId.setDescription(" The UUID of the MRP domain to which this port belongs to. If the port doesn't belong to a MRP domain, the value must be NIL ('0000000000000000'). ")
lldpXPnoLocPortMrrtStatus = MibTableColumn((1, 0, 8802, 1, 1, 2, 1, 5, 3791, 1, 2, 1, 1, 8), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1, 2))).clone(namedValues=NamedValues(("off", 0), ("configured", 1), ("up", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: lldpXPnoLocPortMrrtStatus.setStatus('current')
if mibBuilder.loadTexts: lldpXPnoLocPortMrrtStatus.setDescription(" This object reports the status of the MRRT entity of the corresponding port. A value of off(0) means that there isn't any MRRT capability available for this port or it is switched off. The value configured(1) indicates that MRRT is configured for the port. When MRRT is active on the port, the value will be up(2). ")
lldpXPnoRemTable = MibTable((1, 0, 8802, 1, 1, 2, 1, 5, 3791, 1, 3, 1), )
if mibBuilder.loadTexts: lldpXPnoRemTable.setStatus('current')
if mibBuilder.loadTexts: lldpXPnoRemTable.setDescription(' This table contains one or more rows per physical network connection known to this agent. The agent may wish to ensure that only one lldpXPnoRemEntry is present for each local port, or it may choose to maintain multiple lldpXPnoRemEntries for the same local port. ')
lldpXPnoRemEntry = MibTableRow((1, 0, 8802, 1, 1, 2, 1, 5, 3791, 1, 3, 1, 1), ).setIndexNames((0, "LLDP-MIB", "lldpRemTimeMark"), (0, "LLDP-MIB", "lldpRemLocalPortNum"), (0, "LLDP-MIB", "lldpRemIndex"))
if mibBuilder.loadTexts: lldpXPnoRemEntry.setStatus('current')
if mibBuilder.loadTexts: lldpXPnoRemEntry.setDescription(' Each entry represents the received information of the communication partner on this physical connection. The entries feature multiple indices from the lldpRemEntry of the LLDP-MIB, therefore it is only present along with the description defined by the associated lldpRemEntry entry. ')
lldpXPnoRemLPDValue = MibTableColumn((1, 0, 8802, 1, 1, 2, 1, 5, 3791, 1, 3, 1, 1, 1), Unsigned32()).setUnits('ns').setMaxAccess("readonly")
if mibBuilder.loadTexts: lldpXPnoRemLPDValue.setStatus('current')
if mibBuilder.loadTexts: lldpXPnoRemLPDValue.setDescription(' This integer value represents the line propagation delay in nanoseconds which was measured by the remote system on the corresponding port. A value of zero shall be used if the remote system either could not accomplish the measurement or does not support such a measurement. ')
lldpXPnoRemPortTxDValue = MibTableColumn((1, 0, 8802, 1, 1, 2, 1, 5, 3791, 1, 3, 1, 1, 2), Unsigned32()).setUnits('ns').setMaxAccess("readonly")
if mibBuilder.loadTexts: lldpXPnoRemPortTxDValue.setStatus('current')
if mibBuilder.loadTexts: lldpXPnoRemPortTxDValue.setDescription(' This integer value represents the PortTxDelay in nanoseconds which was measured by the remote system on the corresponding port. A value of zero shall be used if the remote system either could not accomplish the measurement or does not support such a measurement. ')
lldpXPnoRemPortRxDValue = MibTableColumn((1, 0, 8802, 1, 1, 2, 1, 5, 3791, 1, 3, 1, 1, 3), Unsigned32()).setUnits('ns').setMaxAccess("readonly")
if mibBuilder.loadTexts: lldpXPnoRemPortRxDValue.setStatus('current')
if mibBuilder.loadTexts: lldpXPnoRemPortRxDValue.setDescription(' This integer value represents the PortRxDelay in nanoseconds which was measured by the remote system on the corresponding port. A value of zero shall be used if the remote system either could not accomplish the measurement or does not support such a measurement. ')
lldpXPnoRemPortStatusRT2 = MibTableColumn((1, 0, 8802, 1, 1, 2, 1, 5, 3791, 1, 3, 1, 1, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1, 2))).clone(namedValues=NamedValues(("off", 0), ("configured", 1), ("running", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: lldpXPnoRemPortStatusRT2.setStatus('current')
if mibBuilder.loadTexts: lldpXPnoRemPortStatusRT2.setDescription(" This value represents the status of the corresponding port of the remote system according to RT class 2. A value of off(0) means that there isn't any RT2 capability available for this port. When the port is configured for RT2 mode, but the mode isn't active yet the value will be configured(1). If the RT2 mode is configured for this port and the mode is active, the value will be running(2). ")
lldpXPnoRemPortStatusRT3 = MibTableColumn((1, 0, 8802, 1, 1, 2, 1, 5, 3791, 1, 3, 1, 1, 5), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3, 4))).clone(namedValues=NamedValues(("off", 0), ("configured", 1), ("up", 2), ("down", 3), ("running", 4)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: lldpXPnoRemPortStatusRT3.setStatus('current')
if mibBuilder.loadTexts: lldpXPnoRemPortStatusRT3.setDescription(" This value represents the status of the corresponding port of the remote system according to RT class 3. A value of off(0) means that there isn't any RT3 capability available for this port. When the port is configured for RT3 mode, but the mode isn't active yet the value will be configured(1). When the port is ready for transmission and reception of RT3 traffic, the port status will be running(4). ")
lldpXPnoRemPortNoS = MibTableColumn((1, 0, 8802, 1, 1, 2, 1, 5, 3791, 1, 3, 1, 1, 6), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: lldpXPnoRemPortNoS.setStatus('current')
if mibBuilder.loadTexts: lldpXPnoRemPortNoS.setDescription(" The PROFINET NameofStation of the remote partner. If the station isn't configured yet, the value of this object will be the MAC address of the device as a string. ")
lldpXPnoRemPortMrpUuId = MibTableColumn((1, 0, 8802, 1, 1, 2, 1, 5, 3791, 1, 3, 1, 1, 7), OctetString().subtype(subtypeSpec=ValueSizeConstraint(16, 16)).setFixedLength(16)).setMaxAccess("readonly")
if mibBuilder.loadTexts: lldpXPnoRemPortMrpUuId.setStatus('current')
if mibBuilder.loadTexts: lldpXPnoRemPortMrpUuId.setDescription(" The UUID of the MRP domain to which the corresponding port of the remote system belongs to. If the port doesn't belong to a MRP domain, the value must be NIL ('0000000000000000'). ")
lldpXPnoRemPortMrrtStatus = MibTableColumn((1, 0, 8802, 1, 1, 2, 1, 5, 3791, 1, 3, 1, 1, 8), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1, 2))).clone(namedValues=NamedValues(("off", 0), ("configured", 1), ("up", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: lldpXPnoRemPortMrrtStatus.setStatus('current')
if mibBuilder.loadTexts: lldpXPnoRemPortMrrtStatus.setDescription(" This object reports the status of the MRRT entity of the corresponding port. A value of off(0) means that there isn't any MRRT capability available for this port or it is switched off. The value configured(1) indicates that MRRT is configured for the port. When MRRT is active on the port, the value will be up(2). ")
lldpXPnoConformance = MibIdentifier((1, 0, 8802, 1, 1, 2, 1, 5, 3791, 2))
lldpXPnoCompliances = MibIdentifier((1, 0, 8802, 1, 1, 2, 1, 5, 3791, 2, 1))
lldpXPnoGroups = MibIdentifier((1, 0, 8802, 1, 1, 2, 1, 5, 3791, 2, 2))
lldpXPnoCompliance = ModuleCompliance((1, 0, 8802, 1, 1, 2, 1, 5, 3791, 2, 1, 1)).setObjects(("LLDP-EXT-PNO-MIB", "lldpXPnoConfigGroup"), ("LLDP-EXT-PNO-MIB", "lldpXPnoLocGroup"), ("LLDP-EXT-PNO-MIB", "lldpXPnoRemGroup"), ("LLDP-EXT-PNO-MIB", "lldpXPnoMRPGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    lldpXPnoCompliance = lldpXPnoCompliance.setStatus('current')
if mibBuilder.loadTexts: lldpXPnoCompliance.setDescription(' The compliance statement for SNMP entities which implement the PNO organizationally defined LLDP extension MIB. ')
lldpXPnoConfigGroup = ObjectGroup((1, 0, 8802, 1, 1, 2, 1, 5, 3791, 2, 2, 1)).setObjects(("LLDP-EXT-PNO-MIB", "lldpXPnoConfigSPDTxEnable"), ("LLDP-EXT-PNO-MIB", "lldpXPnoConfigPortStatusTxEnable"), ("LLDP-EXT-PNO-MIB", "lldpXPnoConfigAliasTxEnable"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    lldpXPnoConfigGroup = lldpXPnoConfigGroup.setStatus('current')
if mibBuilder.loadTexts: lldpXPnoConfigGroup.setDescription(' The collection of objects which are used to configure the PNO organizationally defined LLDP extension implementation behavior. This group is mandatory for agents which implement the PNO organizationally defined LLDP extension, because the information about the signal propagation delay is necessary to configure PROFINET domains. ')
lldpXPnoLocGroup = ObjectGroup((1, 0, 8802, 1, 1, 2, 1, 5, 3791, 2, 2, 2)).setObjects(("LLDP-EXT-PNO-MIB", "lldpXPnoLocLPDValue"), ("LLDP-EXT-PNO-MIB", "lldpXPnoLocPortTxDValue"), ("LLDP-EXT-PNO-MIB", "lldpXPnoLocPortRxDValue"), ("LLDP-EXT-PNO-MIB", "lldpXPnoLocPortStatusRT2"), ("LLDP-EXT-PNO-MIB", "lldpXPnoLocPortStatusRT3"), ("LLDP-EXT-PNO-MIB", "lldpXPnoLocPortNoS"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    lldpXPnoLocGroup = lldpXPnoLocGroup.setStatus('current')
if mibBuilder.loadTexts: lldpXPnoLocGroup.setDescription(' The collection of objects which are used to configure the PNO organizationally defined LLDP extension implementation behavior. This group is mandatory for agents which implement the PNO organizationally defined LLDP extension, because the information about the signal propagation delay is necessary to configure PROFINET domains. ')
lldpXPnoRemGroup = ObjectGroup((1, 0, 8802, 1, 1, 2, 1, 5, 3791, 2, 2, 3)).setObjects(("LLDP-EXT-PNO-MIB", "lldpXPnoRemLPDValue"), ("LLDP-EXT-PNO-MIB", "lldpXPnoRemPortTxDValue"), ("LLDP-EXT-PNO-MIB", "lldpXPnoRemPortRxDValue"), ("LLDP-EXT-PNO-MIB", "lldpXPnoRemPortStatusRT2"), ("LLDP-EXT-PNO-MIB", "lldpXPnoRemPortStatusRT3"), ("LLDP-EXT-PNO-MIB", "lldpXPnoRemPortNoS"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    lldpXPnoRemGroup = lldpXPnoRemGroup.setStatus('current')
if mibBuilder.loadTexts: lldpXPnoRemGroup.setDescription(' The collection of objects which are used to configure the PNO organizationally defined LLDP extension implementation behavior. This group is mandatory for agents which implement the PNO organizationally defined LLDP extension, because the information about the signal propagation delay is necessary to configure PROFINET domains. ')
lldpXPnoMRPGroup = ObjectGroup((1, 0, 8802, 1, 1, 2, 1, 5, 3791, 2, 2, 4)).setObjects(("LLDP-EXT-PNO-MIB", "lldpXPnoConfigMrpTxEnable"), ("LLDP-EXT-PNO-MIB", "lldpXPnoLocPortMrpUuId"), ("LLDP-EXT-PNO-MIB", "lldpXPnoLocPortMrrtStatus"), ("LLDP-EXT-PNO-MIB", "lldpXPnoRemPortMrpUuId"), ("LLDP-EXT-PNO-MIB", "lldpXPnoRemPortMrrtStatus"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    lldpXPnoMRPGroup = lldpXPnoMRPGroup.setStatus('current')
if mibBuilder.loadTexts: lldpXPnoMRPGroup.setDescription(' The collection of objects which are used to configure the PNO organizationally defined LLDP extension implementation behavior. This group is mandatory for agents which implement the PNO organizationally defined LLDP extension, because the information about the signal propagation delay is necessary to configure PROFINET domains. ')
mibBuilder.exportSymbols("LLDP-EXT-PNO-MIB", lldpXPnoRemPortNoS=lldpXPnoRemPortNoS, lldpXPnoLocPortRxDValue=lldpXPnoLocPortRxDValue, lldpXPnoRemoteData=lldpXPnoRemoteData, lldpXPnoRemPortTxDValue=lldpXPnoRemPortTxDValue, lldpXPnoRemPortMrpUuId=lldpXPnoRemPortMrpUuId, lldpXPnoConfigMrpTxEnable=lldpXPnoConfigMrpTxEnable, lldpXPnoLocEntry=lldpXPnoLocEntry, lldpXPnoRemPortMrrtStatus=lldpXPnoRemPortMrrtStatus, lldpXPnoRemPortStatusRT2=lldpXPnoRemPortStatusRT2, lldpXPnoLocPortMrrtStatus=lldpXPnoLocPortMrrtStatus, lldpXPnoConfigAliasTxEnable=lldpXPnoConfigAliasTxEnable, lldpXPnoLocLPDValue=lldpXPnoLocLPDValue, lldpXPnoMIB=lldpXPnoMIB, lldpXPnoConfigTable=lldpXPnoConfigTable, lldpXPnoRemPortStatusRT3=lldpXPnoRemPortStatusRT3, lldpXPnoGroups=lldpXPnoGroups, lldpXPnoConfigGroup=lldpXPnoConfigGroup, lldpXPnoLocPortNoS=lldpXPnoLocPortNoS, lldpXPnoLocPortStatusRT3=lldpXPnoLocPortStatusRT3, lldpXPnoLocTable=lldpXPnoLocTable, PYSNMP_MODULE_ID=lldpXPnoMIB, lldpXPnoLocPortMrpUuId=lldpXPnoLocPortMrpUuId, lldpXPnoRemGroup=lldpXPnoRemGroup, lldpXPnoConfigSPDTxEnable=lldpXPnoConfigSPDTxEnable, lldpXPnoLocPortStatusRT2=lldpXPnoLocPortStatusRT2, lldpXPnoObjects=lldpXPnoObjects, lldpXPnoRemLPDValue=lldpXPnoRemLPDValue, lldpXPnoConfigPortStatusTxEnable=lldpXPnoConfigPortStatusTxEnable, lldpXPnoRemPortRxDValue=lldpXPnoRemPortRxDValue, lldpXPnoCompliance=lldpXPnoCompliance, lldpXPnoRemTable=lldpXPnoRemTable, lldpXPnoLocPortTxDValue=lldpXPnoLocPortTxDValue, lldpXPnoRemEntry=lldpXPnoRemEntry, lldpXPnoCompliances=lldpXPnoCompliances, lldpXPnoConformance=lldpXPnoConformance, lldpXPnoMRPGroup=lldpXPnoMRPGroup, lldpXPnoConfig=lldpXPnoConfig, lldpXPnoLocGroup=lldpXPnoLocGroup, lldpXPnoLocalData=lldpXPnoLocalData, lldpXPnoConfigEntry=lldpXPnoConfigEntry)
