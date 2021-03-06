#
# PySNMP MIB module SONUS-COMMON-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/SONUS-COMMON-MIB
# Produced by pysmi-0.3.4 at Wed May  1 15:09:32 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, SingleValueConstraint, ValueSizeConstraint, ValueRangeConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "SingleValueConstraint", "ValueSizeConstraint", "ValueRangeConstraint", "ConstraintsUnion")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
iso, TimeTicks, Counter32, Bits, MibScalar, MibTable, MibTableRow, MibTableColumn, ObjectIdentity, Integer32, ModuleIdentity, NotificationType, IpAddress, Gauge32, Counter64, Unsigned32, MibIdentifier = mibBuilder.importSymbols("SNMPv2-SMI", "iso", "TimeTicks", "Counter32", "Bits", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "ObjectIdentity", "Integer32", "ModuleIdentity", "NotificationType", "IpAddress", "Gauge32", "Counter64", "Unsigned32", "MibIdentifier")
DateAndTime, DisplayString, TextualConvention, RowStatus = mibBuilder.importSymbols("SNMPv2-TC", "DateAndTime", "DisplayString", "TextualConvention", "RowStatus")
sonusSystemMIBs, = mibBuilder.importSymbols("SONUS-SMI", "sonusSystemMIBs")
SonusEventClass, SonusName, SonusAdminState, SonusAccessLevel, SonusEventLevel, SonusNameReference, SonusTrapType, SonusEventString = mibBuilder.importSymbols("SONUS-TC", "SonusEventClass", "SonusName", "SonusAdminState", "SonusAccessLevel", "SonusEventLevel", "SonusNameReference", "SonusTrapType", "SonusEventString")
sonusCommonMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 2879, 2, 1, 5))
if mibBuilder.loadTexts: sonusCommonMIB.setLastUpdated('200102030000Z')
if mibBuilder.loadTexts: sonusCommonMIB.setOrganization('Sonus Networks, Inc.')
if mibBuilder.loadTexts: sonusCommonMIB.setContactInfo(' Customer Support Sonus Networks, Inc, 5 carlisle Road Westford, MA 01886 USA Tel: 978-692-8999 Fax: 978-392-9118 E-mail: cs.snmp@sonusnet.com')
if mibBuilder.loadTexts: sonusCommonMIB.setDescription('The MIB Module for common management of all Sonus devices.')
sonusCommonMIBObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 2879, 2, 1, 5, 1))
sonusNetMgmt = MibIdentifier((1, 3, 6, 1, 4, 1, 2879, 2, 1, 5, 1, 1))
sonusNetMgmtClient = MibIdentifier((1, 3, 6, 1, 4, 1, 2879, 2, 1, 5, 1, 1, 1))
sonusNetMgmtClientNextIndex = MibScalar((1, 3, 6, 1, 4, 1, 2879, 2, 1, 5, 1, 1, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 65535))).setMaxAccess("readonly")
if mibBuilder.loadTexts: sonusNetMgmtClientNextIndex.setStatus('current')
if mibBuilder.loadTexts: sonusNetMgmtClientNextIndex.setDescription('The next valid index to use when creating an entry in the sonusNetMgmtClientTable.')
sonusNetMgmtClientTable = MibTable((1, 3, 6, 1, 4, 1, 2879, 2, 1, 5, 1, 1, 1, 2), )
if mibBuilder.loadTexts: sonusNetMgmtClientTable.setStatus('current')
if mibBuilder.loadTexts: sonusNetMgmtClientTable.setDescription('The sonusNetMgmtClientTable specifies the management entities (i.e. clients) that are capable of configurating the node. Each management client is identified by its IP address.')
sonusNetMgmtClientEntry = MibTableRow((1, 3, 6, 1, 4, 1, 2879, 2, 1, 5, 1, 1, 1, 2, 1), ).setIndexNames((0, "SONUS-COMMON-MIB", "sonusNetMgmtClientIndex"))
if mibBuilder.loadTexts: sonusNetMgmtClientEntry.setStatus('current')
if mibBuilder.loadTexts: sonusNetMgmtClientEntry.setDescription('An entry in the sonusNetMgmtClientTable.')
sonusNetMgmtClientIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 2879, 2, 1, 5, 1, 1, 1, 2, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 8)).clone(1)).setMaxAccess("readonly")
if mibBuilder.loadTexts: sonusNetMgmtClientIndex.setStatus('current')
if mibBuilder.loadTexts: sonusNetMgmtClientIndex.setDescription('The tabular index of this administrative management client.')
sonusNetMgmtClientName = MibTableColumn((1, 3, 6, 1, 4, 1, 2879, 2, 1, 5, 1, 1, 1, 2, 1, 2), SonusName()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: sonusNetMgmtClientName.setStatus('current')
if mibBuilder.loadTexts: sonusNetMgmtClientName.setDescription('The name of this administrative management client.')
sonusNetMgmtClientState = MibTableColumn((1, 3, 6, 1, 4, 1, 2879, 2, 1, 5, 1, 1, 1, 2, 1, 3), SonusAdminState().clone('disabled')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: sonusNetMgmtClientState.setStatus('current')
if mibBuilder.loadTexts: sonusNetMgmtClientState.setDescription('The administrative state of this management client.')
sonusNetMgmtClientIpAddr = MibTableColumn((1, 3, 6, 1, 4, 1, 2879, 2, 1, 5, 1, 1, 1, 2, 1, 4), IpAddress().clone(hexValue="01010101")).setMaxAccess("readwrite")
if mibBuilder.loadTexts: sonusNetMgmtClientIpAddr.setStatus('current')
if mibBuilder.loadTexts: sonusNetMgmtClientIpAddr.setDescription('The IP address of this management client.')
sonusNetMgmtClientAccess = MibTableColumn((1, 3, 6, 1, 4, 1, 2879, 2, 1, 5, 1, 1, 1, 2, 1, 5), SonusAccessLevel().clone('readOnly')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: sonusNetMgmtClientAccess.setStatus('current')
if mibBuilder.loadTexts: sonusNetMgmtClientAccess.setDescription('The level of management that is granted to this management client.')
sonusNetMgmtClientSnmpCommunityGet = MibTableColumn((1, 3, 6, 1, 4, 1, 2879, 2, 1, 5, 1, 1, 1, 2, 1, 6), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 23)).clone('public')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: sonusNetMgmtClientSnmpCommunityGet.setStatus('current')
if mibBuilder.loadTexts: sonusNetMgmtClientSnmpCommunityGet.setDescription('The SNMP read-only community string.')
sonusNetMgmtClientSnmpCommunitySet = MibTableColumn((1, 3, 6, 1, 4, 1, 2879, 2, 1, 5, 1, 1, 1, 2, 1, 7), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 23)).clone('private')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: sonusNetMgmtClientSnmpCommunitySet.setStatus('current')
if mibBuilder.loadTexts: sonusNetMgmtClientSnmpCommunitySet.setDescription('The SNMP read-write community string.')
sonusNetMgmtClientSnmpCommunityTrap = MibTableColumn((1, 3, 6, 1, 4, 1, 2879, 2, 1, 5, 1, 1, 1, 2, 1, 8), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 23)).clone('public')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: sonusNetMgmtClientSnmpCommunityTrap.setStatus('current')
if mibBuilder.loadTexts: sonusNetMgmtClientSnmpCommunityTrap.setDescription('The SNMP trap community string.')
sonusNetMgmtClientTrapState = MibTableColumn((1, 3, 6, 1, 4, 1, 2879, 2, 1, 5, 1, 1, 1, 2, 1, 9), SonusAdminState().clone('enabled')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: sonusNetMgmtClientTrapState.setStatus('current')
if mibBuilder.loadTexts: sonusNetMgmtClientTrapState.setDescription('Determines whether SNMP traps are transmitted to this management client.')
sonusNetMgmtClientRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 2879, 2, 1, 5, 1, 1, 1, 2, 1, 10), RowStatus()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: sonusNetMgmtClientRowStatus.setStatus('current')
if mibBuilder.loadTexts: sonusNetMgmtClientRowStatus.setDescription('This object is used to create and delete rows in the sonusNetMgmtClientTable.')
sonusNetMgmtClientTrapPort = MibTableColumn((1, 3, 6, 1, 4, 1, 2879, 2, 1, 5, 1, 1, 1, 2, 1, 11), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 65535)).clone(162)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: sonusNetMgmtClientTrapPort.setStatus('current')
if mibBuilder.loadTexts: sonusNetMgmtClientTrapPort.setDescription('The port number of the management client where trap/notification PDUs are to be sent to.')
sonusNetMgmtClientAllTraps = MibTableColumn((1, 3, 6, 1, 4, 1, 2879, 2, 1, 5, 1, 1, 1, 2, 1, 12), SonusTrapType().clone('trapv2')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: sonusNetMgmtClientAllTraps.setStatus('current')
if mibBuilder.loadTexts: sonusNetMgmtClientAllTraps.setDescription('Indicates if all traps are to be sent to this management client, and defines their trap type.')
sonusNetMgmtClientInformReqTimeout = MibTableColumn((1, 3, 6, 1, 4, 1, 2879, 2, 1, 5, 1, 1, 1, 2, 1, 13), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 120)).clone(5)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: sonusNetMgmtClientInformReqTimeout.setStatus('current')
if mibBuilder.loadTexts: sonusNetMgmtClientInformReqTimeout.setDescription('The time in seconds that an InformRequest PDU that is sent to this Management Client will timeout if no Response PDU is received. This MIB object does not apply to SNMPv1 or SNMPv2 Trap PDUs. Refer to sonusNetMgmtClientInformRequestRetries for related information.')
sonusNetMgmtClientInformReqRetries = MibTableColumn((1, 3, 6, 1, 4, 1, 2879, 2, 1, 5, 1, 1, 1, 2, 1, 14), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 10)).clone(3)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: sonusNetMgmtClientInformReqRetries.setStatus('current')
if mibBuilder.loadTexts: sonusNetMgmtClientInformReqRetries.setDescription('The number of retries that are to be made when sending an InformRequest PDU to this Management Client. The maximum number of attempts to send an InformRequest PDU to a Management Client will be one, for the initial attempt, plus the number of retries. This MIB object does not apply to SNMPv1 or SNMPv2 Trap PDUs. Refer to sonusNetMgmtClientInformRequestTimeout for related information.')
sonusNetMgmtClientInformReqMaxQueue = MibTableColumn((1, 3, 6, 1, 4, 1, 2879, 2, 1, 5, 1, 1, 1, 2, 1, 15), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 100)).clone(50)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: sonusNetMgmtClientInformReqMaxQueue.setStatus('current')
if mibBuilder.loadTexts: sonusNetMgmtClientInformReqMaxQueue.setDescription('The maximum of InformRequest PDUs that will be outstanding, awaiting for Response PDUs from this Management Client. When the maximum number has been reached, consectutive InformRequest PDUs will be discarded (i.e. not sent.) Increasing this number will increase the memory consumed by the GSX software and the CPU time required to process the InformRequest PDUs. This MIB object does not apply to SNMPv1 or SNMPv2 Trap PDUs.')
sonusNetMgmtClientStatusTable = MibTable((1, 3, 6, 1, 4, 1, 2879, 2, 1, 5, 1, 1, 1, 3), )
if mibBuilder.loadTexts: sonusNetMgmtClientStatusTable.setStatus('current')
if mibBuilder.loadTexts: sonusNetMgmtClientStatusTable.setDescription('The sonusNetMgmtClientStatusTable specifies the status of the management entities (i.e. clients). Each management client is identified by its IP address.')
sonusNetMgmtClientStatusEntry = MibTableRow((1, 3, 6, 1, 4, 1, 2879, 2, 1, 5, 1, 1, 1, 3, 1), ).setIndexNames((0, "SONUS-COMMON-MIB", "sonusNetMgmtClientStatusIndex"))
if mibBuilder.loadTexts: sonusNetMgmtClientStatusEntry.setStatus('current')
if mibBuilder.loadTexts: sonusNetMgmtClientStatusEntry.setDescription('An entry in the sonusNetMgmtClientStatusTable.')
sonusNetMgmtClientStatusIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 2879, 2, 1, 5, 1, 1, 1, 3, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 8)))
if mibBuilder.loadTexts: sonusNetMgmtClientStatusIndex.setStatus('current')
if mibBuilder.loadTexts: sonusNetMgmtClientStatusIndex.setDescription('The tabular index of this status management client.')
sonusNetMgmtClientStatusLastConfigChange = MibTableColumn((1, 3, 6, 1, 4, 1, 2879, 2, 1, 5, 1, 1, 1, 3, 1, 2), DateAndTime()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sonusNetMgmtClientStatusLastConfigChange.setStatus('current')
if mibBuilder.loadTexts: sonusNetMgmtClientStatusLastConfigChange.setDescription('Octet string that identifies the GMT timestamp of last successful SET PDU from this management client. field octects contents range ----- ------- -------- ----- 1 1-2 year 0..65536 2 3 month 1..12 3 4 day 1..31 4 5 hour 0..23 5 6 minutes 0..59 6 7 seconds 0..59 7 8 deci-sec 0..9 * Notes: - the value of year is in network-byte order ')
sonusNetMgmtTrap = MibIdentifier((1, 3, 6, 1, 4, 1, 2879, 2, 1, 5, 1, 1, 2))
sonusNetMgmtTrapNextIndex = MibIdentifier((1, 3, 6, 1, 4, 1, 2879, 2, 1, 5, 1, 1, 2, 1))
sonusNetMgmtTrapTable = MibTable((1, 3, 6, 1, 4, 1, 2879, 2, 1, 5, 1, 1, 2, 2), )
if mibBuilder.loadTexts: sonusNetMgmtTrapTable.setStatus('current')
if mibBuilder.loadTexts: sonusNetMgmtTrapTable.setDescription('The sonusNetMgmtTrapTable identifies the SNMP Traps that this node supports.')
sonusNetMgmtTrapEntry = MibTableRow((1, 3, 6, 1, 4, 1, 2879, 2, 1, 5, 1, 1, 2, 2, 1), ).setIndexNames((0, "SONUS-COMMON-MIB", "sonusNetMgmtTrapIndex"))
if mibBuilder.loadTexts: sonusNetMgmtTrapEntry.setStatus('current')
if mibBuilder.loadTexts: sonusNetMgmtTrapEntry.setDescription('An entry in the sonusNetMgmtTrapTable.')
sonusNetMgmtTrapIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 2879, 2, 1, 5, 1, 1, 2, 2, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 65535)).clone(1))
if mibBuilder.loadTexts: sonusNetMgmtTrapIndex.setStatus('current')
if mibBuilder.loadTexts: sonusNetMgmtTrapIndex.setDescription('The tabular index of this trap.')
sonusNetMgmtTrapName = MibTableColumn((1, 3, 6, 1, 4, 1, 2879, 2, 1, 5, 1, 1, 2, 2, 1, 2), SonusName()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sonusNetMgmtTrapName.setStatus('current')
if mibBuilder.loadTexts: sonusNetMgmtTrapName.setDescription('The name of this trap.')
sonusNetMgmtTrapMIBName = MibTableColumn((1, 3, 6, 1, 4, 1, 2879, 2, 1, 5, 1, 1, 2, 2, 1, 3), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 63))).setMaxAccess("readonly")
if mibBuilder.loadTexts: sonusNetMgmtTrapMIBName.setStatus('obsolete')
if mibBuilder.loadTexts: sonusNetMgmtTrapMIBName.setDescription('The full MIB name of this trap.')
sonusNetMgmtTrapOID = MibTableColumn((1, 3, 6, 1, 4, 1, 2879, 2, 1, 5, 1, 1, 2, 2, 1, 4), ObjectIdentifier()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sonusNetMgmtTrapOID.setStatus('current')
if mibBuilder.loadTexts: sonusNetMgmtTrapOID.setDescription('The MIB OID of this trap.')
sonusNetMgmtTrapClass = MibTableColumn((1, 3, 6, 1, 4, 1, 2879, 2, 1, 5, 1, 1, 2, 2, 1, 5), SonusEventClass().clone('sysmgmt')).setMaxAccess("readonly")
if mibBuilder.loadTexts: sonusNetMgmtTrapClass.setStatus('current')
if mibBuilder.loadTexts: sonusNetMgmtTrapClass.setDescription('The classification of the event that corresponds to this trap.')
sonusNetMgmtTrapLevel = MibTableColumn((1, 3, 6, 1, 4, 1, 2879, 2, 1, 5, 1, 1, 2, 2, 1, 6), SonusEventLevel().clone('info')).setMaxAccess("readonly")
if mibBuilder.loadTexts: sonusNetMgmtTrapLevel.setStatus('current')
if mibBuilder.loadTexts: sonusNetMgmtTrapLevel.setDescription('The severity level of the event that corresponds to this trap.')
sonusNetMgmtTrapState = MibTableColumn((1, 3, 6, 1, 4, 1, 2879, 2, 1, 5, 1, 1, 2, 2, 1, 7), SonusAdminState().clone('enabled')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: sonusNetMgmtTrapState.setStatus('current')
if mibBuilder.loadTexts: sonusNetMgmtTrapState.setDescription('Determines if this SNMP trap is transmitted to any management client.')
sonusNetMgmtNotify = MibIdentifier((1, 3, 6, 1, 4, 1, 2879, 2, 1, 5, 1, 1, 3))
sonusNetMgmtNotifyNextIndex = MibScalar((1, 3, 6, 1, 4, 1, 2879, 2, 1, 5, 1, 1, 3, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 65535))).setMaxAccess("readonly")
if mibBuilder.loadTexts: sonusNetMgmtNotifyNextIndex.setStatus('current')
if mibBuilder.loadTexts: sonusNetMgmtNotifyNextIndex.setDescription('The next valid index to use when creating an entry in the sonusNetMgmtNotifyTable.')
sonusNetMgmtNotifyTable = MibTable((1, 3, 6, 1, 4, 1, 2879, 2, 1, 5, 1, 1, 3, 2), )
if mibBuilder.loadTexts: sonusNetMgmtNotifyTable.setStatus('current')
if mibBuilder.loadTexts: sonusNetMgmtNotifyTable.setDescription('The sonusNetMgmtNotifyTable identifies which management clients are to be notified by which SNMP Traps.')
sonusNetMgmtNotifyEntry = MibTableRow((1, 3, 6, 1, 4, 1, 2879, 2, 1, 5, 1, 1, 3, 2, 1), ).setIndexNames((0, "SONUS-COMMON-MIB", "sonusNetMgmtNotifyIndex"))
if mibBuilder.loadTexts: sonusNetMgmtNotifyEntry.setStatus('current')
if mibBuilder.loadTexts: sonusNetMgmtNotifyEntry.setDescription('An entry in the sonusNetMgmtNotifyTable.')
sonusNetMgmtNotifyIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 2879, 2, 1, 5, 1, 1, 3, 2, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 65535)).clone(1))
if mibBuilder.loadTexts: sonusNetMgmtNotifyIndex.setStatus('current')
if mibBuilder.loadTexts: sonusNetMgmtNotifyIndex.setDescription('The table index of notify entries.')
sonusNetMgmtNotifyName = MibTableColumn((1, 3, 6, 1, 4, 1, 2879, 2, 1, 5, 1, 1, 3, 2, 1, 2), SonusName()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: sonusNetMgmtNotifyName.setStatus('current')
if mibBuilder.loadTexts: sonusNetMgmtNotifyName.setDescription('The name of the notification entry.')
sonusNetMgmtNotifyMgmtName = MibTableColumn((1, 3, 6, 1, 4, 1, 2879, 2, 1, 5, 1, 1, 3, 2, 1, 3), SonusNameReference()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: sonusNetMgmtNotifyMgmtName.setStatus('current')
if mibBuilder.loadTexts: sonusNetMgmtNotifyMgmtName.setDescription('The name of the management client that is to be notified of the trap identified by this entry. The value must match an existing sonusNetMgmtClientName in the sonusNetMgmtClientTable.')
sonusNetMgmtNotifyTrapName = MibTableColumn((1, 3, 6, 1, 4, 1, 2879, 2, 1, 5, 1, 1, 3, 2, 1, 4), SonusNameReference()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: sonusNetMgmtNotifyTrapName.setStatus('current')
if mibBuilder.loadTexts: sonusNetMgmtNotifyTrapName.setDescription('The name of the trap that is to be sent to the management client identified by this entry. The value must match an existing sonusNetMgmtTrapName in the sonusNetMgmtTrapTable.')
sonusNetMgmtNotifyTrapType = MibTableColumn((1, 3, 6, 1, 4, 1, 2879, 2, 1, 5, 1, 1, 3, 2, 1, 5), SonusTrapType().clone('trapv2')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: sonusNetMgmtNotifyTrapType.setStatus('current')
if mibBuilder.loadTexts: sonusNetMgmtNotifyTrapType.setDescription('Identify whether no PDU, a SNMPv1 Trap PDU, SNMPv2 Trap PDU, or SNMPv2 Inform PDU is to be transmitted to this management client.')
sonusNetMgmtNotifyRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 2879, 2, 1, 5, 1, 1, 3, 2, 1, 6), RowStatus()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: sonusNetMgmtNotifyRowStatus.setStatus('current')
if mibBuilder.loadTexts: sonusNetMgmtNotifyRowStatus.setDescription('This object is used to create and delete rows in the sonusNetMgmtNotifyTable.')
sonusCommonMIBNotifications = MibIdentifier((1, 3, 6, 1, 4, 1, 2879, 2, 1, 5, 2))
sonusCommonMIBNotificationsPrefix = MibIdentifier((1, 3, 6, 1, 4, 1, 2879, 2, 1, 5, 2, 0))
sonusCommonMIBNotificationsObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 2879, 2, 1, 5, 2, 1))
sonusShelfIndex = MibScalar((1, 3, 6, 1, 4, 1, 2879, 2, 1, 5, 2, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 6))).setMaxAccess("readonly")
if mibBuilder.loadTexts: sonusShelfIndex.setStatus('current')
if mibBuilder.loadTexts: sonusShelfIndex.setDescription('The shelf index of the event that generated the trap.')
sonusSlotIndex = MibScalar((1, 3, 6, 1, 4, 1, 2879, 2, 1, 5, 2, 1, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 16))).setMaxAccess("readonly")
if mibBuilder.loadTexts: sonusSlotIndex.setStatus('current')
if mibBuilder.loadTexts: sonusSlotIndex.setDescription('The slot index of the event that generated the trap.')
sonusPortIndex = MibScalar((1, 3, 6, 1, 4, 1, 2879, 2, 1, 5, 2, 1, 3), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 65535))).setMaxAccess("readonly")
if mibBuilder.loadTexts: sonusPortIndex.setStatus('current')
if mibBuilder.loadTexts: sonusPortIndex.setDescription('The port index of the event that generated the trap.')
sonusDs3Index = MibScalar((1, 3, 6, 1, 4, 1, 2879, 2, 1, 5, 2, 1, 4), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 65535))).setMaxAccess("readonly")
if mibBuilder.loadTexts: sonusDs3Index.setStatus('current')
if mibBuilder.loadTexts: sonusDs3Index.setDescription('The DS3 index of the event that generated the trap.')
sonusDs1Index = MibScalar((1, 3, 6, 1, 4, 1, 2879, 2, 1, 5, 2, 1, 5), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 65535))).setMaxAccess("readonly")
if mibBuilder.loadTexts: sonusDs1Index.setStatus('current')
if mibBuilder.loadTexts: sonusDs1Index.setDescription('The DS1 index of the event that generated the trap.')
sonusEventDescription = MibScalar((1, 3, 6, 1, 4, 1, 2879, 2, 1, 5, 2, 1, 6), SonusEventString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sonusEventDescription.setStatus('current')
if mibBuilder.loadTexts: sonusEventDescription.setDescription('A description of the event that generated the trap.')
sonusEventClass = MibScalar((1, 3, 6, 1, 4, 1, 2879, 2, 1, 5, 2, 1, 7), SonusEventClass()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sonusEventClass.setStatus('current')
if mibBuilder.loadTexts: sonusEventClass.setDescription('The category of the event that generated the trap.')
sonusEventLevel = MibScalar((1, 3, 6, 1, 4, 1, 2879, 2, 1, 5, 2, 1, 8), SonusEventLevel()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sonusEventLevel.setStatus('current')
if mibBuilder.loadTexts: sonusEventLevel.setDescription('The severity level of the event that generated the trap.')
sonusSequenceId = MibScalar((1, 3, 6, 1, 4, 1, 2879, 2, 1, 5, 2, 1, 9), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sonusSequenceId.setStatus('current')
if mibBuilder.loadTexts: sonusSequenceId.setDescription('A consecutive number assigned to each trap in a sequence of traps that are sent to one management client. Each management client has its own set of sequence IDs.')
sonusEventTime = MibScalar((1, 3, 6, 1, 4, 1, 2879, 2, 1, 5, 2, 1, 10), DateAndTime()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sonusEventTime.setStatus('current')
if mibBuilder.loadTexts: sonusEventTime.setDescription('The date and time of the event that generated the trap.')
sonusNetMgmtInformReqDiscards = MibScalar((1, 3, 6, 1, 4, 1, 2879, 2, 1, 5, 2, 1, 11), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 100))).setMaxAccess("readonly")
if mibBuilder.loadTexts: sonusNetMgmtInformReqDiscards.setStatus('current')
if mibBuilder.loadTexts: sonusNetMgmtInformReqDiscards.setDescription('The number of InformRequest PDUs that were discarded for a Management Client.')
sonusNetMgmtClientInformReqQueueFlushedNotification = NotificationType((1, 3, 6, 1, 4, 1, 2879, 2, 1, 5, 2, 0, 1)).setObjects(("SONUS-COMMON-MIB", "sonusNetMgmtClientName"), ("SONUS-COMMON-MIB", "sonusNetMgmtInformReqDiscards"), ("SONUS-COMMON-MIB", "sonusEventDescription"), ("SONUS-COMMON-MIB", "sonusEventClass"), ("SONUS-COMMON-MIB", "sonusEventLevel"))
if mibBuilder.loadTexts: sonusNetMgmtClientInformReqQueueFlushedNotification.setStatus('current')
if mibBuilder.loadTexts: sonusNetMgmtClientInformReqQueueFlushedNotification.setDescription('The specified number of InformRequest PDUs destined to the specified Management Client were flushed from the InformRequest PDU queue because no Response PDUs were were received from the Management Client. This situtation could occur if the Management Client cannot quickly process and respond to InformRequest PDUs that it receives, or if communications is lost with the Management Client. If this situation occurs occasionally, it is recommended to increase the InformRequest PDU timeout and/or retry values (see sonusNetMgmtClientInformReqTimeout and sonusNetMgmtClientInformReqRetries.) If this situation occurs repeatedly, it is an indication that communications is lost with the Management Client, either because of network problems, or because the Management Client is no longer operational. It is recommended that this device be configured to send a Trap PDU, not an InformRequest PDU, for this Notification to all Management Clients, thus bypassing a problematic InformRequest PDU queue and allowing the situation to be quickly identified and resolved.')
sonusNetMgmtClientInformReqQueueFullNotification = NotificationType((1, 3, 6, 1, 4, 1, 2879, 2, 1, 5, 2, 0, 2)).setObjects(("SONUS-COMMON-MIB", "sonusNetMgmtClientName"), ("SONUS-COMMON-MIB", "sonusNetMgmtInformReqDiscards"), ("SONUS-COMMON-MIB", "sonusEventDescription"), ("SONUS-COMMON-MIB", "sonusEventClass"), ("SONUS-COMMON-MIB", "sonusEventLevel"))
if mibBuilder.loadTexts: sonusNetMgmtClientInformReqQueueFullNotification.setStatus('current')
if mibBuilder.loadTexts: sonusNetMgmtClientInformReqQueueFullNotification.setDescription('The specified number of InformRequest PDUs destined to the specified Management Client were discard because its InformRequest PDU queue was full. This situtation could occur if the Management Client cannot quickly process and respond to InformRequest PDUs that it receives, or if communications is lost with the Management Client. If this situation occurs occasionally, it is recommended to increase the InformRequest PDU queue size (see sonusNetMgmtClientInformReqMaxQueue.) If this situation occurs repeatedly, it is an indication that communications is lost with the Management Client, either because of network problems, or because the Management Client is no longer operational. It is recommended that this device be configured to send a Trap PDU, not an InformRequest PDU, for this Notification to all Management Clients, thus bypassing a problematic InformRequest PDU queue and allowing the situation to be quickly identified and resolved.')
mibBuilder.exportSymbols("SONUS-COMMON-MIB", sonusNetMgmtTrapIndex=sonusNetMgmtTrapIndex, sonusNetMgmtClientStatusTable=sonusNetMgmtClientStatusTable, sonusNetMgmtClientAllTraps=sonusNetMgmtClientAllTraps, sonusNetMgmtTrapClass=sonusNetMgmtTrapClass, sonusNetMgmtTrapTable=sonusNetMgmtTrapTable, sonusEventTime=sonusEventTime, sonusNetMgmtClientEntry=sonusNetMgmtClientEntry, sonusEventDescription=sonusEventDescription, sonusNetMgmtTrap=sonusNetMgmtTrap, sonusSequenceId=sonusSequenceId, sonusNetMgmtTrapMIBName=sonusNetMgmtTrapMIBName, sonusNetMgmtNotifyIndex=sonusNetMgmtNotifyIndex, sonusNetMgmtNotifyMgmtName=sonusNetMgmtNotifyMgmtName, sonusDs3Index=sonusDs3Index, PYSNMP_MODULE_ID=sonusCommonMIB, sonusNetMgmtClientNextIndex=sonusNetMgmtClientNextIndex, sonusEventLevel=sonusEventLevel, sonusNetMgmtTrapName=sonusNetMgmtTrapName, sonusNetMgmtClientName=sonusNetMgmtClientName, sonusCommonMIBNotificationsPrefix=sonusCommonMIBNotificationsPrefix, sonusCommonMIBObjects=sonusCommonMIBObjects, sonusNetMgmtClientTrapState=sonusNetMgmtClientTrapState, sonusNetMgmtNotifyTrapType=sonusNetMgmtNotifyTrapType, sonusNetMgmtClientInformReqTimeout=sonusNetMgmtClientInformReqTimeout, sonusNetMgmtTrapEntry=sonusNetMgmtTrapEntry, sonusCommonMIBNotifications=sonusCommonMIBNotifications, sonusShelfIndex=sonusShelfIndex, sonusNetMgmtClientState=sonusNetMgmtClientState, sonusCommonMIBNotificationsObjects=sonusCommonMIBNotificationsObjects, sonusCommonMIB=sonusCommonMIB, sonusNetMgmtTrapLevel=sonusNetMgmtTrapLevel, sonusNetMgmtNotifyEntry=sonusNetMgmtNotifyEntry, sonusNetMgmtNotifyNextIndex=sonusNetMgmtNotifyNextIndex, sonusNetMgmtClientInformReqQueueFlushedNotification=sonusNetMgmtClientInformReqQueueFlushedNotification, sonusEventClass=sonusEventClass, sonusNetMgmt=sonusNetMgmt, sonusSlotIndex=sonusSlotIndex, sonusNetMgmtNotifyName=sonusNetMgmtNotifyName, sonusDs1Index=sonusDs1Index, sonusNetMgmtClientSnmpCommunitySet=sonusNetMgmtClientSnmpCommunitySet, sonusNetMgmtClientTable=sonusNetMgmtClientTable, sonusNetMgmtTrapState=sonusNetMgmtTrapState, sonusNetMgmtClientInformReqMaxQueue=sonusNetMgmtClientInformReqMaxQueue, sonusNetMgmtTrapOID=sonusNetMgmtTrapOID, sonusNetMgmtClientSnmpCommunityGet=sonusNetMgmtClientSnmpCommunityGet, sonusNetMgmtNotifyTable=sonusNetMgmtNotifyTable, sonusNetMgmtClientInformReqQueueFullNotification=sonusNetMgmtClientInformReqQueueFullNotification, sonusNetMgmtClientInformReqRetries=sonusNetMgmtClientInformReqRetries, sonusNetMgmtTrapNextIndex=sonusNetMgmtTrapNextIndex, sonusNetMgmtNotifyTrapName=sonusNetMgmtNotifyTrapName, sonusNetMgmtClientStatusEntry=sonusNetMgmtClientStatusEntry, sonusNetMgmtClientTrapPort=sonusNetMgmtClientTrapPort, sonusNetMgmtNotifyRowStatus=sonusNetMgmtNotifyRowStatus, sonusNetMgmtClient=sonusNetMgmtClient, sonusPortIndex=sonusPortIndex, sonusNetMgmtClientStatusLastConfigChange=sonusNetMgmtClientStatusLastConfigChange, sonusNetMgmtNotify=sonusNetMgmtNotify, sonusNetMgmtClientAccess=sonusNetMgmtClientAccess, sonusNetMgmtClientSnmpCommunityTrap=sonusNetMgmtClientSnmpCommunityTrap, sonusNetMgmtClientIpAddr=sonusNetMgmtClientIpAddr, sonusNetMgmtClientRowStatus=sonusNetMgmtClientRowStatus, sonusNetMgmtInformReqDiscards=sonusNetMgmtInformReqDiscards, sonusNetMgmtClientIndex=sonusNetMgmtClientIndex, sonusNetMgmtClientStatusIndex=sonusNetMgmtClientStatusIndex)
