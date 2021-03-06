#
# PySNMP MIB module CPQAPPLIANCE-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/CPQAPPLIANCE-MIB
# Produced by pysmi-0.3.4 at Wed May  1 12:27:13 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
SingleValueConstraint, ValueRangeConstraint, ConstraintsUnion, ValueSizeConstraint, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "SingleValueConstraint", "ValueRangeConstraint", "ConstraintsUnion", "ValueSizeConstraint", "ConstraintsIntersection")
compaq, cpqHoTrapFlags = mibBuilder.importSymbols("CPQHOST-MIB", "compaq", "cpqHoTrapFlags")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
sysName, = mibBuilder.importSymbols("SNMPv2-MIB", "sysName")
Integer32, Gauge32, Unsigned32, iso, MibIdentifier, Counter32, ObjectIdentity, TimeTicks, Counter64, IpAddress, ModuleIdentity, enterprises, MibScalar, MibTable, MibTableRow, MibTableColumn, NotificationType, NotificationType, Bits = mibBuilder.importSymbols("SNMPv2-SMI", "Integer32", "Gauge32", "Unsigned32", "iso", "MibIdentifier", "Counter32", "ObjectIdentity", "TimeTicks", "Counter64", "IpAddress", "ModuleIdentity", "enterprises", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "NotificationType", "NotificationType", "Bits")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
cpqApplianceMgmt = MibIdentifier((1, 3, 6, 1, 4, 1, 232, 21))
cpqApMibRev = MibIdentifier((1, 3, 6, 1, 4, 1, 232, 21, 1))
cpqApComponent = MibIdentifier((1, 3, 6, 1, 4, 1, 232, 21, 2))
cpqApInterface = MibIdentifier((1, 3, 6, 1, 4, 1, 232, 21, 2, 1))
cpqApConfig = MibIdentifier((1, 3, 6, 1, 4, 1, 232, 21, 2, 2))
cpqApOsCommon = MibIdentifier((1, 3, 6, 1, 4, 1, 232, 21, 2, 1, 4))
cpqApMibRevMajor = MibScalar((1, 3, 6, 1, 4, 1, 232, 21, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 65535))).setMaxAccess("readonly")
if mibBuilder.loadTexts: cpqApMibRevMajor.setStatus('mandatory')
if mibBuilder.loadTexts: cpqApMibRevMajor.setDescription('The Major Revision level of the MIB. A change in the major revision level represents a major change in the architecture of the MIB. A change in the major revision level may indicate a significant change in the information supported and/or the meaning of the supported information, correct interpretation of data may require a MIB document with the same major revision level.')
cpqApMibRevMinor = MibScalar((1, 3, 6, 1, 4, 1, 232, 21, 1, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 65535))).setMaxAccess("readonly")
if mibBuilder.loadTexts: cpqApMibRevMinor.setStatus('mandatory')
if mibBuilder.loadTexts: cpqApMibRevMinor.setDescription('The Minor Revision level of the MIB. A change in the minor revision level may represent some minor additional support, no changes to any pre-existing information has occurred.')
cpqApMibCondition = MibScalar((1, 3, 6, 1, 4, 1, 232, 21, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))).clone(namedValues=NamedValues(("other", 1), ("ok", 2), ("degraded", 3), ("failed", 4)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: cpqApMibCondition.setStatus('mandatory')
if mibBuilder.loadTexts: cpqApMibCondition.setDescription('The overall condition of the Appliance MIB. This object represents the overall status of the Appliance MIB management system represented by this MIB.')
cpqApOsCommonPollFreq = MibScalar((1, 3, 6, 1, 4, 1, 232, 21, 2, 1, 4, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 2147483647))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cpqApOsCommonPollFreq.setStatus('mandatory')
if mibBuilder.loadTexts: cpqApOsCommonPollFreq.setDescription("The Agent's polling frequency. The frequency, in seconds, at which the Agent requests information from. A frequency of zero indicates that the Agent retrieves the information upon request of a management station, it does not poll at a specific interval. If the poll frequency is zero (0) all attempts to write to this object will fail. If the poll frequency is non-zero, setting this value will change the polling frequency of the Agent. Setting the poll frequency to zero will always fail, an agent may also choose to fail any request to change the poll frequency to a value that would severely impact system performance.")
cpqApApplianceId = MibScalar((1, 3, 6, 1, 4, 1, 232, 21, 2, 2, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cpqApApplianceId.setStatus('mandatory')
if mibBuilder.loadTexts: cpqApApplianceId.setDescription('A unique identifier of the Appliance. This can be used by management consoles to allow specific logic which pertains to the particular appliance. For example, this might be used to provide custom graphics for a particular appliance. Each appliance that needs differentiation will be give a different appliance ID.')
cpqApApplianceDescription = MibScalar((1, 3, 6, 1, 4, 1, 232, 21, 2, 2, 2), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 80))).setMaxAccess("readonly")
if mibBuilder.loadTexts: cpqApApplianceDescription.setStatus('mandatory')
if mibBuilder.loadTexts: cpqApApplianceDescription.setDescription('The text description of this Appliance.')
mibBuilder.exportSymbols("CPQAPPLIANCE-MIB", cpqApOsCommon=cpqApOsCommon, cpqApComponent=cpqApComponent, cpqApInterface=cpqApInterface, cpqApMibRev=cpqApMibRev, cpqApMibRevMinor=cpqApMibRevMinor, cpqApplianceMgmt=cpqApplianceMgmt, cpqApMibRevMajor=cpqApMibRevMajor, cpqApMibCondition=cpqApMibCondition, cpqApOsCommonPollFreq=cpqApOsCommonPollFreq, cpqApApplianceDescription=cpqApApplianceDescription, cpqApConfig=cpqApConfig, cpqApApplianceId=cpqApApplianceId)
