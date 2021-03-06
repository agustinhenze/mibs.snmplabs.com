#
# PySNMP MIB module TPDIN2-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/TPDIN2-MIB
# Produced by pysmi-0.3.4 at Wed May  1 15:24:06 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
Integer, OctetString, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "Integer", "OctetString", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsUnion, SingleValueConstraint, ConstraintsIntersection, ValueSizeConstraint, ValueRangeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "SingleValueConstraint", "ConstraintsIntersection", "ValueSizeConstraint", "ValueRangeConstraint")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
enterprises, NotificationType, iso, MibScalar, MibTable, MibTableRow, MibTableColumn, Gauge32, ModuleIdentity, Bits, IpAddress, Counter64, Unsigned32, Integer32, ObjectIdentity, MibIdentifier, Counter32, TimeTicks = mibBuilder.importSymbols("SNMPv2-SMI", "enterprises", "NotificationType", "iso", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Gauge32", "ModuleIdentity", "Bits", "IpAddress", "Counter64", "Unsigned32", "Integer32", "ObjectIdentity", "MibIdentifier", "Counter32", "TimeTicks")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
tpdin2 = ModuleIdentity((1, 3, 6, 1, 4, 1, 45621, 2))
if mibBuilder.loadTexts: tpdin2.setLastUpdated('201703031251Z')
if mibBuilder.loadTexts: tpdin2.setOrganization('Tycon Systems')
if mibBuilder.loadTexts: tpdin2.setContactInfo('http://www.tyconsystems.com/')
if mibBuilder.loadTexts: tpdin2.setDescription('TPDIN Monitor Web V2 custom MIB')
tycon = MibIdentifier((1, 3, 6, 1, 4, 1, 45621))
product = MibIdentifier((1, 3, 6, 1, 4, 1, 45621, 2, 1))
monitor = MibIdentifier((1, 3, 6, 1, 4, 1, 45621, 2, 2))
class Tenths(TextualConvention, Integer32):
    description = 'tenths'
    status = 'current'
    displayHint = 'd-1'
    subtypeSpec = Integer32.subtypeSpec + ValueRangeConstraint(0, 10000)

name = MibScalar((1, 3, 6, 1, 4, 1, 45621, 2, 1, 1), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: name.setStatus('current')
if mibBuilder.loadTexts: name.setDescription('Product name.')
version = MibScalar((1, 3, 6, 1, 4, 1, 45621, 2, 1, 2), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: version.setStatus('current')
if mibBuilder.loadTexts: version.setDescription('Product version.')
builddate = MibScalar((1, 3, 6, 1, 4, 1, 45621, 2, 1, 3), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: builddate.setStatus('current')
if mibBuilder.loadTexts: builddate.setDescription('Build date.')
relay1 = MibScalar((1, 3, 6, 1, 4, 1, 45621, 2, 2, 1), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: relay1.setStatus('current')
if mibBuilder.loadTexts: relay1.setDescription('Relay 1')
relay2 = MibScalar((1, 3, 6, 1, 4, 1, 45621, 2, 2, 2), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: relay2.setStatus('current')
if mibBuilder.loadTexts: relay2.setDescription('Relay 2')
relay3 = MibScalar((1, 3, 6, 1, 4, 1, 45621, 2, 2, 3), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: relay3.setStatus('current')
if mibBuilder.loadTexts: relay3.setDescription('Relay 3')
relay4 = MibScalar((1, 3, 6, 1, 4, 1, 45621, 2, 2, 4), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: relay4.setStatus('current')
if mibBuilder.loadTexts: relay4.setDescription('Relay 4')
voltage1 = MibScalar((1, 3, 6, 1, 4, 1, 45621, 2, 2, 5), Tenths()).setMaxAccess("readonly")
if mibBuilder.loadTexts: voltage1.setStatus('current')
if mibBuilder.loadTexts: voltage1.setDescription('Voltage 1')
voltage2 = MibScalar((1, 3, 6, 1, 4, 1, 45621, 2, 2, 6), Tenths()).setMaxAccess("readonly")
if mibBuilder.loadTexts: voltage2.setStatus('current')
if mibBuilder.loadTexts: voltage2.setDescription('Voltage 2')
voltage3 = MibScalar((1, 3, 6, 1, 4, 1, 45621, 2, 2, 7), Tenths()).setMaxAccess("readonly")
if mibBuilder.loadTexts: voltage3.setStatus('current')
if mibBuilder.loadTexts: voltage3.setDescription('Voltage 3')
voltage4 = MibScalar((1, 3, 6, 1, 4, 1, 45621, 2, 2, 8), Tenths()).setMaxAccess("readonly")
if mibBuilder.loadTexts: voltage4.setStatus('current')
if mibBuilder.loadTexts: voltage4.setDescription('Voltage 4')
current1 = MibScalar((1, 3, 6, 1, 4, 1, 45621, 2, 2, 9), Tenths()).setMaxAccess("readonly")
if mibBuilder.loadTexts: current1.setStatus('current')
if mibBuilder.loadTexts: current1.setDescription('Current 1')
current2 = MibScalar((1, 3, 6, 1, 4, 1, 45621, 2, 2, 10), Tenths()).setMaxAccess("readonly")
if mibBuilder.loadTexts: current2.setStatus('current')
if mibBuilder.loadTexts: current2.setDescription('Current 2')
current3 = MibScalar((1, 3, 6, 1, 4, 1, 45621, 2, 2, 11), Tenths()).setMaxAccess("readonly")
if mibBuilder.loadTexts: current3.setStatus('current')
if mibBuilder.loadTexts: current3.setDescription('Current 3')
current4 = MibScalar((1, 3, 6, 1, 4, 1, 45621, 2, 2, 12), Tenths()).setMaxAccess("readonly")
if mibBuilder.loadTexts: current4.setStatus('current')
if mibBuilder.loadTexts: current4.setDescription('Current 4')
temperature1 = MibScalar((1, 3, 6, 1, 4, 1, 45621, 2, 2, 13), Tenths()).setMaxAccess("readonly")
if mibBuilder.loadTexts: temperature1.setStatus('current')
if mibBuilder.loadTexts: temperature1.setDescription('External Temp')
temperature2 = MibScalar((1, 3, 6, 1, 4, 1, 45621, 2, 2, 14), Tenths()).setMaxAccess("readonly")
if mibBuilder.loadTexts: temperature2.setStatus('current')
if mibBuilder.loadTexts: temperature2.setDescription('Internal Temp')
mibBuilder.exportSymbols("TPDIN2-MIB", relay1=relay1, name=name, current3=current3, temperature1=temperature1, tpdin2=tpdin2, voltage4=voltage4, current2=current2, Tenths=Tenths, version=version, builddate=builddate, product=product, voltage2=voltage2, relay3=relay3, monitor=monitor, voltage3=voltage3, PYSNMP_MODULE_ID=tpdin2, tycon=tycon, temperature2=temperature2, current4=current4, relay2=relay2, voltage1=voltage1, current1=current1, relay4=relay4)
