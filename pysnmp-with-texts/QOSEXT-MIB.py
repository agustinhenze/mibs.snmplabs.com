#
# PySNMP MIB module QOSEXT-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/QOSEXT-MIB
# Produced by pysmi-0.3.4 at Wed May  1 14:44:14 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
qosExt, = mibBuilder.importSymbols("APENT-MIB", "qosExt")
Integer, OctetString, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "Integer", "OctetString", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ValueRangeConstraint, SingleValueConstraint, ConstraintsIntersection, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsIntersection", "ConstraintsUnion")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
ModuleIdentity, iso, IpAddress, Counter32, TimeTicks, NotificationType, Bits, Unsigned32, MibScalar, MibTable, MibTableRow, MibTableColumn, Gauge32, ObjectIdentity, Integer32, Counter64, MibIdentifier = mibBuilder.importSymbols("SNMPv2-SMI", "ModuleIdentity", "iso", "IpAddress", "Counter32", "TimeTicks", "NotificationType", "Bits", "Unsigned32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Gauge32", "ObjectIdentity", "Integer32", "Counter64", "MibIdentifier")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
apQosExtMib = ModuleIdentity((1, 3, 6, 1, 4, 1, 2467, 1, 28, 1))
if mibBuilder.loadTexts: apQosExtMib.setLastUpdated('9710092000Z')
if mibBuilder.loadTexts: apQosExtMib.setOrganization('ArrowPoint Communications Inc.')
if mibBuilder.loadTexts: apQosExtMib.setContactInfo(' Postal: ArrowPoint Communications Inc. 50 Nagog Park Acton, Massachusetts 01720 Tel: +1 978-206-3000 option 1 E-Mail: support@arrowpoint.com')
if mibBuilder.loadTexts: apQosExtMib.setDescription('The MIB module ArrowPoint QOS class definitions')
apQosTable = MibTable((1, 3, 6, 1, 4, 1, 2467, 1, 28, 2), )
if mibBuilder.loadTexts: apQosTable.setStatus('current')
if mibBuilder.loadTexts: apQosTable.setDescription('QOS class attributes')
apQosEntry = MibTableRow((1, 3, 6, 1, 4, 1, 2467, 1, 28, 2, 1), ).setIndexNames((0, "QOSEXT-MIB", "apQosType"), (0, "QOSEXT-MIB", "apQosSubType"))
if mibBuilder.loadTexts: apQosEntry.setStatus('current')
if mibBuilder.loadTexts: apQosEntry.setDescription('Configureable Interface specific characteristic record.')
apQosType = MibTableColumn((1, 3, 6, 1, 4, 1, 2467, 1, 28, 2, 1, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("best-effort", 1), ("streamed", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: apQosType.setStatus('current')
if mibBuilder.loadTexts: apQosType.setDescription('The basic category of QOS to be delivered')
apQosSubType = MibTableColumn((1, 3, 6, 1, 4, 1, 2467, 1, 28, 2, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7))).clone(namedValues=NamedValues(("best-effort", 1), ("realAudio-2-14400", 2), ("realAudio-2-28800", 3), ("realAudio-3-28800", 4), ("realAudio-3-28800-stereo", 5), ("realAudio-3-isdn", 6), ("realAudio-3-dual-isdn", 7)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: apQosSubType.setStatus('current')
if mibBuilder.loadTexts: apQosSubType.setDescription('The more specific QOS categorization')
apQosName = MibTableColumn((1, 3, 6, 1, 4, 1, 2467, 1, 28, 2, 1, 3), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(1, 64))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: apQosName.setStatus('current')
if mibBuilder.loadTexts: apQosName.setDescription('The name used to reference the particular set of QOS settings')
apQosClass = MibTableColumn((1, 3, 6, 1, 4, 1, 2467, 1, 28, 2, 1, 4), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 7))).setMaxAccess("readonly")
if mibBuilder.loadTexts: apQosClass.setStatus('current')
if mibBuilder.loadTexts: apQosClass.setDescription('The QOS switching priority')
apQosHopLatency = MibTableColumn((1, 3, 6, 1, 4, 1, 2467, 1, 28, 2, 1, 5), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: apQosHopLatency.setStatus('current')
if mibBuilder.loadTexts: apQosHopLatency.setDescription('The maximum switch introduced delay which can be tolerated')
apQosSampleRate = MibTableColumn((1, 3, 6, 1, 4, 1, 2467, 1, 28, 2, 1, 6), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: apQosSampleRate.setStatus('current')
if mibBuilder.loadTexts: apQosSampleRate.setDescription('The sampling rate used to produce files that require this QOS')
apQosBitsPerSample = MibTableColumn((1, 3, 6, 1, 4, 1, 2467, 1, 28, 2, 1, 7), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: apQosBitsPerSample.setStatus('current')
if mibBuilder.loadTexts: apQosBitsPerSample.setDescription('The number of bits per sample')
apQosAvgBw = MibTableColumn((1, 3, 6, 1, 4, 1, 2467, 1, 28, 2, 1, 8), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: apQosAvgBw.setStatus('current')
if mibBuilder.loadTexts: apQosAvgBw.setDescription('The average bandwidth requirements for flows of this QOS')
apQosSampleSize = MibTableColumn((1, 3, 6, 1, 4, 1, 2467, 1, 28, 2, 1, 9), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: apQosSampleSize.setStatus('current')
if mibBuilder.loadTexts: apQosSampleSize.setDescription('The sampling size used when creating files for use with this QOS')
apQosSilenceTime = MibTableColumn((1, 3, 6, 1, 4, 1, 2467, 1, 28, 2, 1, 10), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: apQosSilenceTime.setStatus('current')
if mibBuilder.loadTexts: apQosSilenceTime.setDescription('The length of the quiet time between packets transmitted by the server for this QOS')
mibBuilder.exportSymbols("QOSEXT-MIB", apQosAvgBw=apQosAvgBw, apQosSampleRate=apQosSampleRate, apQosSubType=apQosSubType, apQosClass=apQosClass, apQosEntry=apQosEntry, apQosTable=apQosTable, PYSNMP_MODULE_ID=apQosExtMib, apQosBitsPerSample=apQosBitsPerSample, apQosType=apQosType, apQosHopLatency=apQosHopLatency, apQosSilenceTime=apQosSilenceTime, apQosName=apQosName, apQosExtMib=apQosExtMib, apQosSampleSize=apQosSampleSize)