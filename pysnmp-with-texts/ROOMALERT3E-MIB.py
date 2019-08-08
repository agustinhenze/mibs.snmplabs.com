#
# PySNMP MIB module ROOMALERT3E-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/ROOMALERT3E-MIB
# Produced by pysmi-0.3.4 at Wed May  1 14:58:19 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
OctetString, ObjectIdentifier, Integer = mibBuilder.importSymbols("ASN1", "OctetString", "ObjectIdentifier", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsIntersection, ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsIntersection", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
NotificationType, Unsigned32, Bits, IpAddress, MibIdentifier, ModuleIdentity, enterprises, Counter64, ObjectIdentity, Integer32, TimeTicks, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter32, iso, Gauge32, NotificationType = mibBuilder.importSymbols("SNMPv2-SMI", "NotificationType", "Unsigned32", "Bits", "IpAddress", "MibIdentifier", "ModuleIdentity", "enterprises", "Counter64", "ObjectIdentity", "Integer32", "TimeTicks", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter32", "iso", "Gauge32", "NotificationType")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
avtech = MibIdentifier((1, 3, 6, 1, 4, 1, 20916))
products = MibIdentifier((1, 3, 6, 1, 4, 1, 20916, 1))
ROOMALERT3E = MibIdentifier((1, 3, 6, 1, 4, 1, 20916, 1, 9))
sensors = MibIdentifier((1, 3, 6, 1, 4, 1, 20916, 1, 9, 1))
signaltower = MibIdentifier((1, 3, 6, 1, 4, 1, 20916, 1, 9, 2))
traps = MibIdentifier((1, 3, 6, 1, 4, 1, 20916, 1, 9, 3))
digital = MibIdentifier((1, 3, 6, 1, 4, 1, 20916, 1, 9, 1, 1))
digital_sen1 = MibIdentifier((1, 3, 6, 1, 4, 1, 20916, 1, 9, 1, 1, 1)).setLabel("digital-sen1")
digital_sen2 = MibIdentifier((1, 3, 6, 1, 4, 1, 20916, 1, 9, 1, 1, 2)).setLabel("digital-sen2")
switch = MibIdentifier((1, 3, 6, 1, 4, 1, 20916, 1, 9, 1, 2))
digital_sen1_1 = MibScalar((1, 3, 6, 1, 4, 1, 20916, 1, 9, 1, 1, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 65535))).setLabel("digital-sen1-1").setMaxAccess("readonly")
if mibBuilder.loadTexts: digital_sen1_1.setStatus('mandatory')
if mibBuilder.loadTexts: digital_sen1_1.setDescription('The current temperature reading in Celsius of the Internal Temperature Sensor.')
digital_sen1_2 = MibScalar((1, 3, 6, 1, 4, 1, 20916, 1, 9, 1, 1, 1, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 65535))).setLabel("digital-sen1-2").setMaxAccess("readonly")
if mibBuilder.loadTexts: digital_sen1_2.setStatus('mandatory')
if mibBuilder.loadTexts: digital_sen1_2.setDescription('The current temperature reading in Fahrenheit of the Internal Temperature Sensor.')
digital_sen1_label = MibScalar((1, 3, 6, 1, 4, 1, 20916, 1, 9, 1, 1, 1, 3), OctetString()).setLabel("digital-sen1-label").setMaxAccess("readonly")
if mibBuilder.loadTexts: digital_sen1_label.setStatus('mandatory')
if mibBuilder.loadTexts: digital_sen1_label.setDescription('The label of this sensor')
digital_sen2_1 = MibScalar((1, 3, 6, 1, 4, 1, 20916, 1, 9, 1, 1, 2, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 65535))).setLabel("digital-sen2-1").setMaxAccess("readonly")
if mibBuilder.loadTexts: digital_sen2_1.setStatus('mandatory')
if mibBuilder.loadTexts: digital_sen2_1.setDescription('If this sensor is a Temperature or Temp/Humidity sensor, this value represents the current temperature in Celsius.')
digital_sen2_2 = MibScalar((1, 3, 6, 1, 4, 1, 20916, 1, 9, 1, 1, 2, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 65535))).setLabel("digital-sen2-2").setMaxAccess("readonly")
if mibBuilder.loadTexts: digital_sen2_2.setStatus('mandatory')
if mibBuilder.loadTexts: digital_sen2_2.setDescription('If this sensor is a Temperature or Temp/Humidity sensor, this value represents the current temperature in Fahrenheit.')
digital_sen2_3 = MibScalar((1, 3, 6, 1, 4, 1, 20916, 1, 9, 1, 1, 2, 3), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 65535))).setLabel("digital-sen2-3").setMaxAccess("readonly")
if mibBuilder.loadTexts: digital_sen2_3.setStatus('mandatory')
if mibBuilder.loadTexts: digital_sen2_3.setDescription('If this sensor is a Temp/Humidity sensor, this value represents the current relative humidity in % Relative Humidity.')
digital_sen2_4 = MibScalar((1, 3, 6, 1, 4, 1, 20916, 1, 9, 1, 1, 2, 4), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 65535))).setLabel("digital-sen2-4").setMaxAccess("readonly")
if mibBuilder.loadTexts: digital_sen2_4.setStatus('mandatory')
if mibBuilder.loadTexts: digital_sen2_4.setDescription('If this sensor is a Temp/Humidity sensor, this value represents the current heat index in Fahrenheit.')
digital_sen2_5 = MibScalar((1, 3, 6, 1, 4, 1, 20916, 1, 9, 1, 1, 2, 5), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 65535))).setLabel("digital-sen2-5").setMaxAccess("readonly")
if mibBuilder.loadTexts: digital_sen2_5.setStatus('mandatory')
if mibBuilder.loadTexts: digital_sen2_5.setDescription('If this sensor is a Temp/Humidity sensor, this value represents the current heat index in Celsius.')
digital_sen2_label = MibScalar((1, 3, 6, 1, 4, 1, 20916, 1, 9, 1, 1, 2, 6), OctetString()).setLabel("digital-sen2-label").setMaxAccess("readonly")
if mibBuilder.loadTexts: digital_sen2_label.setStatus('mandatory')
if mibBuilder.loadTexts: digital_sen2_label.setDescription('The label of this sensor')
switch_sen1 = MibScalar((1, 3, 6, 1, 4, 1, 20916, 1, 9, 1, 2, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 1))).setLabel("switch-sen1").setMaxAccess("readonly")
if mibBuilder.loadTexts: switch_sen1.setStatus('mandatory')
if mibBuilder.loadTexts: switch_sen1.setDescription('The reading for the switch sensor (0 = OPEN, 1 = CLOSED).')
switch_label = MibScalar((1, 3, 6, 1, 4, 1, 20916, 1, 9, 1, 2, 2), OctetString()).setLabel("switch-label").setMaxAccess("readonly")
if mibBuilder.loadTexts: switch_label.setStatus('mandatory')
if mibBuilder.loadTexts: switch_label.setDescription('The label for the switch sensor')
red_led = MibScalar((1, 3, 6, 1, 4, 1, 20916, 1, 9, 2, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 1))).setLabel("red-led").setMaxAccess("readwrite")
if mibBuilder.loadTexts: red_led.setStatus('current')
if mibBuilder.loadTexts: red_led.setDescription('The status of this Signal Tower element (0 = OFF, 1 = ON).')
amber_led = MibScalar((1, 3, 6, 1, 4, 1, 20916, 1, 9, 2, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 1))).setLabel("amber-led").setMaxAccess("readwrite")
if mibBuilder.loadTexts: amber_led.setStatus('current')
if mibBuilder.loadTexts: amber_led.setDescription('The status of this Signal Tower element (0 = OFF, 1 = ON).')
green_led = MibScalar((1, 3, 6, 1, 4, 1, 20916, 1, 9, 2, 3), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 1))).setLabel("green-led").setMaxAccess("readwrite")
if mibBuilder.loadTexts: green_led.setStatus('current')
if mibBuilder.loadTexts: green_led.setDescription('The status of this Signal Tower element (0 = OFF, 1 = ON).')
blue_led = MibScalar((1, 3, 6, 1, 4, 1, 20916, 1, 9, 2, 4), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 1))).setLabel("blue-led").setMaxAccess("readwrite")
if mibBuilder.loadTexts: blue_led.setStatus('current')
if mibBuilder.loadTexts: blue_led.setDescription('The status of this Signal Tower element (0 = OFF, 1 = ON).')
white_led = MibScalar((1, 3, 6, 1, 4, 1, 20916, 1, 9, 2, 5), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 1))).setLabel("white-led").setMaxAccess("readwrite")
if mibBuilder.loadTexts: white_led.setStatus('current')
if mibBuilder.loadTexts: white_led.setDescription('The status of this Signal Tower element (0 = OFF, 1 = ON).')
alarm1 = MibScalar((1, 3, 6, 1, 4, 1, 20916, 1, 9, 2, 6), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 1))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: alarm1.setStatus('current')
if mibBuilder.loadTexts: alarm1.setDescription('The status of this Signal Tower element (0 = OFF, 1 = ON).')
alarm2 = MibScalar((1, 3, 6, 1, 4, 1, 20916, 1, 9, 2, 7), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 1))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: alarm2.setStatus('current')
if mibBuilder.loadTexts: alarm2.setDescription('The status of this Signal Tower element (0 = OFF, 1 = ON).')
alarmmessage = MibScalar((1, 3, 6, 1, 4, 1, 20916, 1, 9, 3, 1), OctetString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: alarmmessage.setStatus('mandatory')
if mibBuilder.loadTexts: alarmmessage.setDescription('Last Alarm Message')
room_alert_3e_snmp_trap = NotificationType((1, 3, 6, 1, 4, 1, 20916, 1, 9) + (0,2)).setLabel("room-alert-3e-snmp-trap").setObjects(("ROOMALERT3E-MIB", "alarmmessage"))
if mibBuilder.loadTexts: room_alert_3e_snmp_trap.setDescription('A room-alert-3e-snmp-trap indicates that an alarm condition has occurred on the sensor indicated by the alarmmessage variable.')
mibBuilder.exportSymbols("ROOMALERT3E-MIB", alarm1=alarm1, signaltower=signaltower, digital=digital, white_led=white_led, digital_sen1_label=digital_sen1_label, alarmmessage=alarmmessage, digital_sen1_1=digital_sen1_1, ROOMALERT3E=ROOMALERT3E, digital_sen2_5=digital_sen2_5, digital_sen2=digital_sen2, room_alert_3e_snmp_trap=room_alert_3e_snmp_trap, digital_sen2_2=digital_sen2_2, switch_label=switch_label, digital_sen1=digital_sen1, red_led=red_led, digital_sen2_1=digital_sen2_1, amber_led=amber_led, sensors=sensors, traps=traps, digital_sen1_2=digital_sen1_2, digital_sen2_3=digital_sen2_3, blue_led=blue_led, switch_sen1=switch_sen1, avtech=avtech, green_led=green_led, products=products, digital_sen2_4=digital_sen2_4, digital_sen2_label=digital_sen2_label, alarm2=alarm2, switch=switch)