#
# PySNMP MIB module HPN-ICF-LAG-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/HPN-ICF-LAG-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 19:27:21 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsUnion, ValueSizeConstraint, ConstraintsIntersection, SingleValueConstraint, ValueRangeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "ValueSizeConstraint", "ConstraintsIntersection", "SingleValueConstraint", "ValueRangeConstraint")
hpnicfRhw, = mibBuilder.importSymbols("HPN-ICF-OID-MIB", "hpnicfRhw")
PortList, = mibBuilder.importSymbols("Q-BRIDGE-MIB", "PortList")
ObjectGroup, NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "ObjectGroup", "NotificationGroup", "ModuleCompliance")
Gauge32, Unsigned32, Counter64, TimeTicks, Counter32, MibIdentifier, Integer32, iso, NotificationType, ModuleIdentity, IpAddress, MibScalar, MibTable, MibTableRow, MibTableColumn, ObjectIdentity, Bits = mibBuilder.importSymbols("SNMPv2-SMI", "Gauge32", "Unsigned32", "Counter64", "TimeTicks", "Counter32", "MibIdentifier", "Integer32", "iso", "NotificationType", "ModuleIdentity", "IpAddress", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "ObjectIdentity", "Bits")
RowStatus, DisplayString, TextualConvention, TruthValue = mibBuilder.importSymbols("SNMPv2-TC", "RowStatus", "DisplayString", "TextualConvention", "TruthValue")
hpnicfLAG = ModuleIdentity((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 25))
if mibBuilder.loadTexts: hpnicfLAG.setLastUpdated('200310091942Z')
if mibBuilder.loadTexts: hpnicfLAG.setOrganization('')
hpnicfLAGMibObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 25, 1))
hpnicfAggLinkTable = MibTable((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 25, 1, 1), )
if mibBuilder.loadTexts: hpnicfAggLinkTable.setStatus('current')
hpnicfAggLinkEntry = MibTableRow((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 25, 1, 1, 1), ).setIndexNames((0, "HPN-ICF-LAG-MIB", "hpnicfAggLinkNumber"))
if mibBuilder.loadTexts: hpnicfAggLinkEntry.setStatus('current')
hpnicfAggLinkNumber = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 25, 1, 1, 1, 1), Integer32()).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: hpnicfAggLinkNumber.setStatus('current')
hpnicfAggLinkName = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 25, 1, 1, 1, 2), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 32))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hpnicfAggLinkName.setStatus('current')
hpnicfAggLinkMode = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 25, 1, 1, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("manual", 1), ("static", 2), ("dynamic", 3)))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hpnicfAggLinkMode.setStatus('current')
hpnicfAggLinkPortList = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 25, 1, 1, 1, 4), PortList()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hpnicfAggLinkPortList.setStatus('current')
hpnicfAggLinkState = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 25, 1, 1, 1, 5), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hpnicfAggLinkState.setStatus('current')
hpnicfAggPortListSelectedPorts = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 25, 1, 1, 1, 6), PortList()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hpnicfAggPortListSelectedPorts.setStatus('current')
hpnicfAggPortListSamePartnerPorts = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 25, 1, 1, 1, 7), PortList()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hpnicfAggPortListSamePartnerPorts.setStatus('current')
hpnicfAggPortTable = MibTable((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 25, 1, 2), )
if mibBuilder.loadTexts: hpnicfAggPortTable.setStatus('current')
hpnicfAggPortEntry = MibTableRow((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 25, 1, 2, 1), ).setIndexNames((0, "HPN-ICF-LAG-MIB", "hpnicfAggPortIndex"))
if mibBuilder.loadTexts: hpnicfAggPortEntry.setStatus('current')
hpnicfAggPortIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 25, 1, 2, 1, 1), Gauge32()).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: hpnicfAggPortIndex.setStatus('current')
hpnicfAggPortNotAttachedReason = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 25, 1, 2, 1, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 10))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hpnicfAggPortNotAttachedReason.setStatus('current')
hpnicfAggPortLacpState = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 25, 1, 2, 1, 3), TruthValue()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hpnicfAggPortLacpState.setStatus('current')
hpnicfAggPortNotAttachedString = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 25, 1, 2, 1, 4), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 255))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hpnicfAggPortNotAttachedString.setStatus('current')
hpnicfAggResourceAllocationValue = MibScalar((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 25, 1, 3), PortList().clone('0')).setMaxAccess("readonly")
if mibBuilder.loadTexts: hpnicfAggResourceAllocationValue.setStatus('current')
hpnicfLAGMibNotifications = MibIdentifier((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 25, 2))
hpnicfAggSpeedChangedNotification = NotificationType((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 25, 2, 1)).setObjects(("HPN-ICF-LAG-MIB", "hpnicfAggLinkNumber"))
if mibBuilder.loadTexts: hpnicfAggSpeedChangedNotification.setStatus('current')
hpnicfAggPortInactiveNotification = NotificationType((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 25, 2, 2)).setObjects(("HPN-ICF-LAG-MIB", "hpnicfAggLinkNumber"))
if mibBuilder.loadTexts: hpnicfAggPortInactiveNotification.setStatus('current')
hpnicfAggPortInactiveNotification2 = NotificationType((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 25, 2, 3)).setObjects(("HPN-ICF-LAG-MIB", "hpnicfAggLinkNumber"), ("HPN-ICF-LAG-MIB", "hpnicfAggPortIndex"))
if mibBuilder.loadTexts: hpnicfAggPortInactiveNotification2.setStatus('current')
hpnicfAggPortActiveNotification = NotificationType((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 25, 2, 4)).setObjects(("HPN-ICF-LAG-MIB", "hpnicfAggLinkNumber"), ("HPN-ICF-LAG-MIB", "hpnicfAggPortIndex"))
if mibBuilder.loadTexts: hpnicfAggPortActiveNotification.setStatus('current')
hpnicfLAGMibConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 25, 3))
hpnicfLAGMibCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 25, 3, 1))
hpnicfLAGMibCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 25, 3, 1, 1)).setObjects(("HPN-ICF-LAG-MIB", "hpnicfLAGMibObjectGroup"), ("HPN-ICF-LAG-MIB", "hpnicfLAGMibNotificationGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    hpnicfLAGMibCompliance = hpnicfLAGMibCompliance.setStatus('current')
hpnicfLAGMibGroup = MibIdentifier((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 25, 3, 2))
hpnicfLAGMibObjectGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 25, 3, 2, 1)).setObjects(("HPN-ICF-LAG-MIB", "hpnicfAggLinkName"), ("HPN-ICF-LAG-MIB", "hpnicfAggLinkMode"), ("HPN-ICF-LAG-MIB", "hpnicfAggLinkPortList"), ("HPN-ICF-LAG-MIB", "hpnicfAggLinkState"), ("HPN-ICF-LAG-MIB", "hpnicfAggPortListSelectedPorts"), ("HPN-ICF-LAG-MIB", "hpnicfAggPortListSamePartnerPorts"), ("HPN-ICF-LAG-MIB", "hpnicfAggPortNotAttachedReason"), ("HPN-ICF-LAG-MIB", "hpnicfAggPortLacpState"), ("HPN-ICF-LAG-MIB", "hpnicfAggPortNotAttachedString"), ("HPN-ICF-LAG-MIB", "hpnicfAggResourceAllocationValue"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    hpnicfLAGMibObjectGroup = hpnicfLAGMibObjectGroup.setStatus('current')
hpnicfLAGMibNotificationGroup = NotificationGroup((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 25, 3, 2, 2)).setObjects(("HPN-ICF-LAG-MIB", "hpnicfAggSpeedChangedNotification"), ("HPN-ICF-LAG-MIB", "hpnicfAggPortInactiveNotification"), ("HPN-ICF-LAG-MIB", "hpnicfAggPortInactiveNotification2"), ("HPN-ICF-LAG-MIB", "hpnicfAggPortActiveNotification"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    hpnicfLAGMibNotificationGroup = hpnicfLAGMibNotificationGroup.setStatus('current')
mibBuilder.exportSymbols("HPN-ICF-LAG-MIB", hpnicfAggPortIndex=hpnicfAggPortIndex, hpnicfAggLinkPortList=hpnicfAggLinkPortList, hpnicfAggPortInactiveNotification2=hpnicfAggPortInactiveNotification2, hpnicfAggPortActiveNotification=hpnicfAggPortActiveNotification, hpnicfLAG=hpnicfLAG, hpnicfLAGMibNotificationGroup=hpnicfLAGMibNotificationGroup, hpnicfLAGMibObjectGroup=hpnicfLAGMibObjectGroup, hpnicfAggLinkNumber=hpnicfAggLinkNumber, hpnicfAggLinkTable=hpnicfAggLinkTable, hpnicfAggPortTable=hpnicfAggPortTable, hpnicfLAGMibGroup=hpnicfLAGMibGroup, hpnicfAggLinkMode=hpnicfAggLinkMode, hpnicfLAGMibConformance=hpnicfLAGMibConformance, hpnicfLAGMibNotifications=hpnicfLAGMibNotifications, hpnicfAggPortNotAttachedString=hpnicfAggPortNotAttachedString, hpnicfAggLinkEntry=hpnicfAggLinkEntry, hpnicfAggPortEntry=hpnicfAggPortEntry, hpnicfAggPortInactiveNotification=hpnicfAggPortInactiveNotification, PYSNMP_MODULE_ID=hpnicfLAG, hpnicfAggLinkName=hpnicfAggLinkName, hpnicfAggPortLacpState=hpnicfAggPortLacpState, hpnicfLAGMibCompliance=hpnicfLAGMibCompliance, hpnicfLAGMibObjects=hpnicfLAGMibObjects, hpnicfAggPortListSelectedPorts=hpnicfAggPortListSelectedPorts, hpnicfAggSpeedChangedNotification=hpnicfAggSpeedChangedNotification, hpnicfAggPortNotAttachedReason=hpnicfAggPortNotAttachedReason, hpnicfAggPortListSamePartnerPorts=hpnicfAggPortListSamePartnerPorts, hpnicfLAGMibCompliances=hpnicfLAGMibCompliances, hpnicfAggLinkState=hpnicfAggLinkState, hpnicfAggResourceAllocationValue=hpnicfAggResourceAllocationValue)