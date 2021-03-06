#
# PySNMP MIB module DOT1X-ADVANCED-FEATURES-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/DOT1X-ADVANCED-FEATURES-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 18:39:07 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ValueRangeConstraint, ConstraintsIntersection, ConstraintsUnion, SingleValueConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ValueRangeConstraint", "ConstraintsIntersection", "ConstraintsUnion", "SingleValueConstraint")
dot1xPaePortNumber, = mibBuilder.importSymbols("IEEE8021-PAE-MIB", "dot1xPaePortNumber")
switch, = mibBuilder.importSymbols("QUANTA-SWITCH-MIB", "switch")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
TimeTicks, Bits, ModuleIdentity, ObjectIdentity, Unsigned32, MibScalar, MibTable, MibTableRow, MibTableColumn, MibIdentifier, Integer32, NotificationType, Counter32, Counter64, iso, IpAddress, Gauge32 = mibBuilder.importSymbols("SNMPv2-SMI", "TimeTicks", "Bits", "ModuleIdentity", "ObjectIdentity", "Unsigned32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "MibIdentifier", "Integer32", "NotificationType", "Counter32", "Counter64", "iso", "IpAddress", "Gauge32")
TextualConvention, PhysAddress, DateAndTime, RowStatus, DisplayString, MacAddress = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "PhysAddress", "DateAndTime", "RowStatus", "DisplayString", "MacAddress")
dot1xAdvanced = ModuleIdentity((1, 3, 6, 1, 4, 1, 7244, 2, 36))
if mibBuilder.loadTexts: dot1xAdvanced.setLastUpdated('201108310000Z')
if mibBuilder.loadTexts: dot1xAdvanced.setOrganization('Quanta Computer Inc.')
class Dot1xPortControlMode(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))
    namedValues = NamedValues(("forceUnauthorized", 1), ("auto", 2), ("forceAuthorized", 3), ("macBased", 4))

class Dot1xSessionTerminationAction(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2))
    namedValues = NamedValues(("default", 1), ("reauthenticate", 2))

agentGuestVlanConfigGroup = MibIdentifier((1, 3, 6, 1, 4, 1, 7244, 2, 36, 1))
agentGuestVlanSupplMode = MibScalar((1, 3, 6, 1, 4, 1, 7244, 2, 36, 1, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enable", 1), ("disable", 2))).clone('disable')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: agentGuestVlanSupplMode.setStatus('current')
agentDot1xGuestVlanPortConfigTable = MibTable((1, 3, 6, 1, 4, 1, 7244, 2, 36, 1, 2), )
if mibBuilder.loadTexts: agentDot1xGuestVlanPortConfigTable.setStatus('current')
agentDot1xGuestVlanPortConfigEntry = MibTableRow((1, 3, 6, 1, 4, 1, 7244, 2, 36, 1, 2, 1), ).setIndexNames((0, "IEEE8021-PAE-MIB", "dot1xPaePortNumber"))
if mibBuilder.loadTexts: agentDot1xGuestVlanPortConfigEntry.setStatus('current')
agentDot1xGuestVlanId = MibTableColumn((1, 3, 6, 1, 4, 1, 7244, 2, 36, 1, 2, 1, 1), Unsigned32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: agentDot1xGuestVlanId.setStatus('current')
agentDot1xGuestVlanPeriod = MibTableColumn((1, 3, 6, 1, 4, 1, 7244, 2, 36, 1, 2, 1, 2), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(0, 65535)).clone(90)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: agentDot1xGuestVlanPeriod.setStatus('current')
agentDot1xEnhancementConfigGroup = MibIdentifier((1, 3, 6, 1, 4, 1, 7244, 2, 36, 2))
agentDot1xRadiusVlanAssignment = MibScalar((1, 3, 6, 1, 4, 1, 7244, 2, 36, 2, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enable", 1), ("disable", 2))).clone('disable')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: agentDot1xRadiusVlanAssignment.setStatus('current')
agentDot1xDynamicVlanCreationMode = MibScalar((1, 3, 6, 1, 4, 1, 7244, 2, 36, 2, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enable", 1), ("disable", 2))).clone('disable')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: agentDot1xDynamicVlanCreationMode.setStatus('current')
agentDot1xClientGroup = MibIdentifier((1, 3, 6, 1, 4, 1, 7244, 2, 36, 3))
agentDot1xClientTable = MibTable((1, 3, 6, 1, 4, 1, 7244, 2, 36, 3, 1), )
if mibBuilder.loadTexts: agentDot1xClientTable.setStatus('current')
agentDot1xClientEntry = MibTableRow((1, 3, 6, 1, 4, 1, 7244, 2, 36, 3, 1, 1), ).setIndexNames((0, "DOT1X-ADVANCED-FEATURES-MIB", "agentDot1xClientLogicalInterface"))
if mibBuilder.loadTexts: agentDot1xClientEntry.setStatus('current')
agentDot1xClientLogicalInterface = MibTableColumn((1, 3, 6, 1, 4, 1, 7244, 2, 36, 3, 1, 1, 1), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: agentDot1xClientLogicalInterface.setStatus('current')
agentDot1xClientInterface = MibTableColumn((1, 3, 6, 1, 4, 1, 7244, 2, 36, 3, 1, 1, 2), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: agentDot1xClientInterface.setStatus('current')
agentDot1xClientUsername = MibTableColumn((1, 3, 6, 1, 4, 1, 7244, 2, 36, 3, 1, 1, 3), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: agentDot1xClientUsername.setStatus('current')
agentDot1xClientMacAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 7244, 2, 36, 3, 1, 1, 4), PhysAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: agentDot1xClientMacAddress.setStatus('current')
agentDot1xClientSessionTime = MibTableColumn((1, 3, 6, 1, 4, 1, 7244, 2, 36, 3, 1, 1, 5), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: agentDot1xClientSessionTime.setStatus('current')
agentDot1xClientVlanId = MibTableColumn((1, 3, 6, 1, 4, 1, 7244, 2, 36, 3, 1, 1, 6), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: agentDot1xClientVlanId.setStatus('current')
agentDot1xClientVlanAssigned = MibTableColumn((1, 3, 6, 1, 4, 1, 7244, 2, 36, 3, 1, 1, 7), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("default", 1), ("radius", 2), ("unauthenticated", 3)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: agentDot1xClientVlanAssigned.setStatus('current')
agentDot1xClientSessionTimeout = MibTableColumn((1, 3, 6, 1, 4, 1, 7244, 2, 36, 3, 1, 1, 8), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: agentDot1xClientSessionTimeout.setStatus('current')
agentDot1xClientSessionTerminationAction = MibTableColumn((1, 3, 6, 1, 4, 1, 7244, 2, 36, 3, 1, 1, 9), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("default", 1), ("radius", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: agentDot1xClientSessionTerminationAction.setStatus('current')
mibBuilder.exportSymbols("DOT1X-ADVANCED-FEATURES-MIB", agentDot1xGuestVlanPortConfigEntry=agentDot1xGuestVlanPortConfigEntry, agentDot1xClientSessionTime=agentDot1xClientSessionTime, agentDot1xClientVlanAssigned=agentDot1xClientVlanAssigned, agentGuestVlanSupplMode=agentGuestVlanSupplMode, agentDot1xClientSessionTimeout=agentDot1xClientSessionTimeout, agentDot1xGuestVlanId=agentDot1xGuestVlanId, agentDot1xClientUsername=agentDot1xClientUsername, agentDot1xClientGroup=agentDot1xClientGroup, agentDot1xClientMacAddress=agentDot1xClientMacAddress, agentDot1xClientEntry=agentDot1xClientEntry, agentDot1xClientLogicalInterface=agentDot1xClientLogicalInterface, Dot1xSessionTerminationAction=Dot1xSessionTerminationAction, PYSNMP_MODULE_ID=dot1xAdvanced, agentDot1xGuestVlanPortConfigTable=agentDot1xGuestVlanPortConfigTable, agentDot1xClientSessionTerminationAction=agentDot1xClientSessionTerminationAction, agentDot1xEnhancementConfigGroup=agentDot1xEnhancementConfigGroup, agentDot1xDynamicVlanCreationMode=agentDot1xDynamicVlanCreationMode, agentDot1xClientInterface=agentDot1xClientInterface, agentDot1xRadiusVlanAssignment=agentDot1xRadiusVlanAssignment, agentDot1xClientVlanId=agentDot1xClientVlanId, dot1xAdvanced=dot1xAdvanced, Dot1xPortControlMode=Dot1xPortControlMode, agentDot1xGuestVlanPeriod=agentDot1xGuestVlanPeriod, agentGuestVlanConfigGroup=agentGuestVlanConfigGroup, agentDot1xClientTable=agentDot1xClientTable)
