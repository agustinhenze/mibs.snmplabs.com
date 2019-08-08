#
# PySNMP MIB module CISCO-LWAPP-WLAN-SECURITY-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/CISCO-LWAPP-WLAN-SECURITY-MIB
# Produced by pysmi-0.3.4 at Wed May  1 12:06:43 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
SingleValueConstraint, ValueSizeConstraint, ConstraintsUnion, ValueRangeConstraint, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "SingleValueConstraint", "ValueSizeConstraint", "ConstraintsUnion", "ValueRangeConstraint", "ConstraintsIntersection")
CLSecEncryptType, CLSecKeyFormat = mibBuilder.importSymbols("CISCO-LWAPP-TC-MIB", "CLSecEncryptType", "CLSecKeyFormat")
cLWlanIndex, = mibBuilder.importSymbols("CISCO-LWAPP-WLAN-MIB", "cLWlanIndex")
ciscoMgmt, = mibBuilder.importSymbols("CISCO-SMI", "ciscoMgmt")
ObjectGroup, NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "ObjectGroup", "NotificationGroup", "ModuleCompliance")
MibIdentifier, NotificationType, MibScalar, MibTable, MibTableRow, MibTableColumn, ObjectIdentity, Bits, Unsigned32, Integer32, Counter32, Gauge32, TimeTicks, IpAddress, iso, ModuleIdentity, Counter64 = mibBuilder.importSymbols("SNMPv2-SMI", "MibIdentifier", "NotificationType", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "ObjectIdentity", "Bits", "Unsigned32", "Integer32", "Counter32", "Gauge32", "TimeTicks", "IpAddress", "iso", "ModuleIdentity", "Counter64")
TextualConvention, TruthValue, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "TruthValue", "DisplayString")
ciscoLwappWlanSecurityMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 9, 521))
ciscoLwappWlanSecurityMIB.setRevisions(('2015-06-03 00:00', '2008-01-15 00:00', '2007-11-08 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: ciscoLwappWlanSecurityMIB.setRevisionsDescriptions(('Added following OBJECT-GROUP: - ciscoLwappWlanSecurityAaaConfigGroup - ciscoLwappWlanSecurityFtConfigGroup - ciscoLwappWlanSecurityPfmConfigGroup - ciscoLwappWlanSecurityCckmConfigGroup1 Added new compliance - ciscoLwappWlanSecurityMIBComplianceRev2.', 'Added new cLWSecDot11EssWebPolicyTable and ciscoLwappWlanSecurityMIBComplianceRev1', 'Initial version of this MIB module.',))
if mibBuilder.loadTexts: ciscoLwappWlanSecurityMIB.setLastUpdated('201506030000Z')
if mibBuilder.loadTexts: ciscoLwappWlanSecurityMIB.setOrganization('Cisco Systems, Inc.')
if mibBuilder.loadTexts: ciscoLwappWlanSecurityMIB.setContactInfo('Cisco Systems, Customer Service Postal: 170 West Tasman Drive San Jose, CA 95134 USA Tel: +1 800 553-NETS Email: cs-wnbu-snmp@cisco.com')
if mibBuilder.loadTexts: ciscoLwappWlanSecurityMIB.setDescription("This MIB is intended to be implemented on all those devices operating as Central controllers, that terminate the Light Weight Access Point Protocol tunnel from Cisco Light-weight LWAPP Access Points. Information provided by this MIB is for WLAN security related features as specified in the CCKM, CKIP specifications. The relationship between the controller and the LWAPP APs is depicted as follows: +......+ +......+ +......+ + + + + + + + CC + + CC + + CC + + + + + + + +......+ +......+ +......+ .. . . .. . . . . . . . . . . . . . . . . . . +......+ +......+ +......+ +......+ + + + + + + + + + AP + + AP + + AP + + AP + + + + + + + + + +......+ +......+ +......+ +......+ . . . . . . . . . . . . . . . . . . . +......+ +......+ +......+ +......+ + + + + + + + + + MN + + MN + + MN + + MN + + + + + + + + + +......+ +......+ +......+ +......+ The LWAPP tunnel exists between the controller and the APs. The MNs communicate with the APs through the protocol defined by the 802.11 standard. LWAPP APs, upon bootup, discover and join one of the controllers and the controller pushes the configuration, that includes the WLAN parameters, to the LWAPP APs. The APs then encapsulate all the 802.11 frames from wireless clients inside LWAPP frames and forward the LWAPP frames to the controller. GLOSSARY 802.1x The IEEE ratified standard for enforcing port based access control. This was originally intended for use on wired LANs and later extended for use in 802.11 WLAN environments. This defines an architecture with three main parts - a supplicant (Ex. an 802.11 wireless client), an authenticator (the AP) and an authentication server(a Radius server). The authenticator passes messages back and forth between the supplicant and the authentication server to enable the supplicant get authenticated to the network. Access Point ( AP ) An entity that contains an 802.11 medium access control ( MAC ) and physical layer ( PHY ) interface and provides access to the distribution services via the wireless medium for associated clients. LWAPP APs encapsulate all the 802.11 frames in LWAPP frames and sends them to the controller to which it is logically connected. Advanced Encryption Standard ( AES ) In cryptography, the Advanced Encryption Standard (AES), also known as Rijndael, is a block cipher adopted as an encryption standard by the US government. It is expected to be used worldwide and analysed extensively, as was the case with its predecessor, the Data Encryption Standard (DES). AES was adopted by National Institute of Standards and Technology (NIST) as US FIPS PUB 197 in November 2001 after a 5-year standardisation process. Central Controller ( CC ) The central entity that terminates the LWAPP protocol tunnel from the LWAPP APs. Throughout this MIB, this entity also referred to as 'controller'. Cisco Centralized Key Management ( CCKM ) Client and AP exchange several EAPOL packets in the process of EAP authenticaton to determine dynamic session key (NSK), which is used for encrypting packets between them. When client moves to new-AP, it has to mutually authenticate with the new-AP and derive new NSK. This is being done by using complete EAP authentication (which is time consuming and causes noticeable delay in the voice application). Till that time, no data packets are being transmitted between new-AP and client. CCKM implementation in first controller caches client's credentials like session, vlanid, ssid, etc. and propagates the same to other controllers in mobility group. Currently a set of controller can be configured as part of a mobility group. If client roams across access points associated to this set of controllers, then with CCKM implementation in place, the L2 authentication will not happen. To make this happen a CCKM cache is maintained on each controller and the first controller where client gets associated update rest of the controllers in mobility group. On later reassociations, controller validates the CCKM specific IE present and allow associations. Wireless LAN Access Points (APs) manufactured by Cisco Systems have features and capabilities beyond those in related standards (e.g., IEEE 802.11 suite of standards, Wi-Fi recommendations by WECA, 802.1X security suite, etc). A number of features provide higher performance. For example, Cisco AP transmits a specific Information Element, which the clients adapt to for enhanced performance. Similarly, a number of features are implemented by means of proprietary Information Elements, which Cisco clients use in specific ways to carry out tasks above and beyond the standard. Other examples of feature categories are roaming and power saving. Cisco Key Integrity Protocol ( CKIP ) A proprietary implementation similar to TKIP. CKIP implements key permutation for protecting the CKIP key against attacks. Other features of CKIP include expansion of encryption key to 16 bytes of length for key protection and MIC to ensure data integrity. Light Weight Access Point Protocol ( LWAPP ) This is a generic protocol that defines the communication between the Access Points and the Central Controller. Mobile Node ( MN ) A roaming 802.11 wireless device in a wireless network associated with an access point. Mobile Node and client are used interchangeably. Multilinear Modular Hash ( MMH ) This is a message authentication code. The original message is run through the hash (with a secret key), and the code is the result. The code is sent along with the original message. The receiver of the message calculates the hash over the original message (also with the secret key) and compares the final message authentication code with the code sent with the message. If the two codes match, the receiver can be assured that the original message is authentic. Pre-Shared Key ( PSK ) Pre-shared keys are normally used for interoperability purposes. The basic idea is that two parties sharing a common secret can communicate securely. This idea has been used since cryptography first sprung onto the scene. Temporal Key Integrity Protocol ( TKIP ) A security protocol defined to enhance the limitations of WEP. Message Integrity Check and per-packet keying on all WEP-encrypted frames are two significant enhancements provided by TKIP to WEP. Wired Equivalent Privacy ( WEP ) A security method defined by 802.11. WEP uses a symmetric key stream cipher called RC4 to encrypt the data packets. Wi-Fi Protected Access ( WPA ) Wi-Fi Protected Access (WPA and WPA2) are security systems created in response to several serious weaknesses found in Wired Equivalent Privacy (WEP). WPA implements the majority of the IEEE 802.11i standard, and was intended as an intermediate measure to take the place of WEP while 802.11i was prepared. WPA is designed to work with all wireless network interface cards, but not necessarily with first generation wireless access points. Protected Management Frame (PFM) Authentication, Authorization, and Accounting (AAA) Remote Authentication Dial In User Service (RADIUS) REFERENCE [1] Wireless LAN Medium Access Control ( MAC ) and Physical Layer ( PHY ) Specifications, Amendment 6, MAC Security Enhancements. [2] draft-obara-capwap-lwapp-00.txt, IETF Light Weight Access Point Protocol")
ciscoLwappWlanSecurityMIBNotifs = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 521, 0))
ciscoLwappWlanSecurityMIBObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 521, 1))
ciscoLwappWlanSecurityMIBConform = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 521, 2))
clwsCckmConfig = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 521, 1, 1))
clwsCkipConfig = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 521, 1, 2))
clwsWebPolicyConfig = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 521, 1, 3))
clwsAaaConfig = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 521, 1, 4))
cLWSecDot11EssCckmTable = MibTable((1, 3, 6, 1, 4, 1, 9, 9, 521, 1, 1, 1), )
if mibBuilder.loadTexts: cLWSecDot11EssCckmTable.setStatus('current')
if mibBuilder.loadTexts: cLWSecDot11EssCckmTable.setDescription('This table represents the CCKM configuration for the WLANs configured on this controller. There exist a row in this table corresponding to each row representing a WLAN in cLWlanConfigTable. The controller adds or deletes a row to this table whenever a WLAN is added or deleted.')
cLWSecDot11EssCckmEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9, 9, 521, 1, 1, 1, 1), ).setIndexNames((0, "CISCO-LWAPP-WLAN-MIB", "cLWlanIndex"))
if mibBuilder.loadTexts: cLWSecDot11EssCckmEntry.setStatus('current')
if mibBuilder.loadTexts: cLWSecDot11EssCckmEntry.setDescription('Each entry represents a conceptual row in cLWSecDot11EssCckmTable and uniquely identified by cLWlanIndex.')
cLWSecDot11EssCckmWpaSupport = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 521, 1, 1, 1, 1, 1), TruthValue().clone('false')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cLWSecDot11EssCckmWpaSupport.setStatus('current')
if mibBuilder.loadTexts: cLWSecDot11EssCckmWpaSupport.setDescription("This object is used to enable or disable layer-2 security using WPA1 or WPA2. When this object is set to 'true' layer-2 security is enabled. When this object is set to 'false' layer-2 security is disabled. When layer-2 security is enabled, the following objects are only applied to environment and can be set. cLWSecDot11EssCckmWpa1Security cLWSecDot11EssCckmWpa1EncType cLWSecDot11EssCckmWpa2Security cLWSecDot11EssCckmWpa2EncType cLWSecDot11EssCckmKeyMgmtMode cLWSecDot11EssCckmGtkRandomize.")
cLWSecDot11EssCckmWpa1Security = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 521, 1, 1, 1, 1, 2), TruthValue().clone('false')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cLWSecDot11EssCckmWpa1Security.setStatus('current')
if mibBuilder.loadTexts: cLWSecDot11EssCckmWpa1Security.setDescription("This object specifies cckmwpa1 security is enabled or not. A value of 'true' indicates that WPA1 security is enabled on the controller. A value of 'false' disables WPA1 security.")
cLWSecDot11EssCckmWpa1EncType = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 521, 1, 1, 1, 1, 3), CLSecEncryptType()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cLWSecDot11EssCckmWpa1EncType.setStatus('current')
if mibBuilder.loadTexts: cLWSecDot11EssCckmWpa1EncType.setDescription("This object specifies the type of WPA1 encryption configured on this WLAN. The value populated by this object is applicable only when cLWSecDot11EssCckmWpa1Security populates a value of 'true'.")
cLWSecDot11EssCckmWpa2Security = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 521, 1, 1, 1, 1, 4), TruthValue().clone('false')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cLWSecDot11EssCckmWpa2Security.setStatus('current')
if mibBuilder.loadTexts: cLWSecDot11EssCckmWpa2Security.setDescription("This object specifies cckmwpa2 security is enabled or not. A value of 'true' indicates that WPA2 security is enabled on the controller. A value of 'false' disables WPA2 security.")
cLWSecDot11EssCckmWpa2EncType = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 521, 1, 1, 1, 1, 5), CLSecEncryptType()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cLWSecDot11EssCckmWpa2EncType.setStatus('current')
if mibBuilder.loadTexts: cLWSecDot11EssCckmWpa2EncType.setDescription("This object specifies the type of WPA2 encryption configured on this WLAN. The value populated by this object is applicable only when cLWSecDot11EssCckmWpa2Security populates a value of 'true'.")
cLWSecDot11EssCckmKeyMgmtMode = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 521, 1, 1, 1, 1, 6), Bits().clone(namedValues=NamedValues(("dot1x", 0), ("cckm", 1), ("psk", 2), ("ftDot1x", 3), ("ftPsk", 4), ("pfmDot1x", 5), ("pfmPsk", 6))).clone(namedValues=NamedValues(("dot1x", 0)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cLWSecDot11EssCckmKeyMgmtMode.setStatus('current')
if mibBuilder.loadTexts: cLWSecDot11EssCckmKeyMgmtMode.setDescription("This object specifies the type of authentication key management that is applicable only when cLWSecDot11EssCckmWpaSupport is set to a value of 'true'. The following are the possible key management configurations allowed and accepted by the system. dot1x(0) + cckm(1) dot1x(0) only cckm(1) only psk(2) only ftDot1x(3) only ftPsk(4) only psk(2) + ftPsk(4) dot1x(0) + ftDot1x(3) dot1x(0) + cckm(1) + ftDot1x(3) dot1x(0) + cckm(1) + pfmDot1x(5) dot1x(0) + pfmDot1x(5) cckm(1) + pfmDot1x(5) psk(2) + pfmPsk(6)")
cLWSecDot11EssPskFmt = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 521, 1, 1, 1, 1, 7), CLSecKeyFormat().clone('default')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cLWSecDot11EssPskFmt.setStatus('current')
if mibBuilder.loadTexts: cLWSecDot11EssPskFmt.setDescription('This object specifies the type of the authentication preshared key configured through the object cLWSecDot11EssCckmPsk. Note that the key configuration is applicable only when psk is configured as the key management mechanism through the cLWSecDot11EssCckmKeyMgmtMode object.')
cLWSecDot11EssPsk = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 521, 1, 1, 1, 1, 8), OctetString().subtype(subtypeSpec=ValueSizeConstraint(8, 64))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cLWSecDot11EssPsk.setStatus('current')
if mibBuilder.loadTexts: cLWSecDot11EssPsk.setDescription("This object specifies the authentication pre-shared key in the hex format that is applicable only when the 'psk' bit is specified in the cLWSecDot11EssCckmKeyMgmtMode object. The length of the key that can be specified for the cLWSecDot11EssPsk object depends on the value of the cLWSecDot11EssPskFmt object as follows. 'ascii' 8-63 octets 'hex' 32 octets.")
cLWSecDot11EssCckmGtkRandomize = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 521, 1, 1, 1, 1, 9), TruthValue()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cLWSecDot11EssCckmGtkRandomize.setStatus('current')
if mibBuilder.loadTexts: cLWSecDot11EssCckmGtkRandomize.setDescription("This object specifies whether the Group Temporal Key(GTK) randomization is enabled for a WLAN. A value of 'true' indicates that GTK randomization is enabled. A value of 'false' indicates that GTK randomization is disabled.")
cLWSecDot11EssFtEnable = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 521, 1, 1, 1, 1, 10), TruthValue()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cLWSecDot11EssFtEnable.setStatus('current')
if mibBuilder.loadTexts: cLWSecDot11EssFtEnable.setDescription("This object specifies whether fast transition is enabled for particular WLAN. A value of 'true' means that fast transition is enabled and a value of 'false' means that fast transition is disabled.")
cLWSecDot11EssFtReassocTime = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 521, 1, 1, 1, 1, 11), Unsigned32()).setUnits('seconds').setMaxAccess("readwrite")
if mibBuilder.loadTexts: cLWSecDot11EssFtReassocTime.setStatus('current')
if mibBuilder.loadTexts: cLWSecDot11EssFtReassocTime.setDescription('This object specifies the fast transition re-association time.')
cLWSecDot11EssFtOverDs = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 521, 1, 1, 1, 1, 12), TruthValue()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cLWSecDot11EssFtOverDs.setStatus('current')
if mibBuilder.loadTexts: cLWSecDot11EssFtOverDs.setDescription("This object specifies whether fast transition over distributed system is enabled. A value of 'true' means that fast transition over the distributed system is enabled and a value of 'false' means fast transition over the distributed system is disabled.")
cLWSecDot11Ess11wPfm = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 521, 1, 1, 1, 1, 13), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("disabled", 1), ("optional", 2), ("required", 3)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cLWSecDot11Ess11wPfm.setStatus('current')
if mibBuilder.loadTexts: cLWSecDot11Ess11wPfm.setDescription('This object specifies the 802.11w PFM configuration for a particular WLAN.')
cLWSecDot11EssRetryTime = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 521, 1, 1, 1, 1, 14), Unsigned32()).setUnits('milliseconds').setMaxAccess("readwrite")
if mibBuilder.loadTexts: cLWSecDot11EssRetryTime.setStatus('current')
if mibBuilder.loadTexts: cLWSecDot11EssRetryTime.setDescription('This object specifies the 802.11w Security Association(SA) query retry timeout.')
cLWSecDot11EssComebackTime = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 521, 1, 1, 1, 1, 15), Unsigned32()).setUnits('seconds').setMaxAccess("readwrite")
if mibBuilder.loadTexts: cLWSecDot11EssComebackTime.setStatus('current')
if mibBuilder.loadTexts: cLWSecDot11EssComebackTime.setDescription('This object specifies the 802.11w association comeback time.')
cLWSecDot11EssCkipTable = MibTable((1, 3, 6, 1, 4, 1, 9, 9, 521, 1, 1, 2), )
if mibBuilder.loadTexts: cLWSecDot11EssCkipTable.setStatus('current')
if mibBuilder.loadTexts: cLWSecDot11EssCkipTable.setDescription('This table represents the CKIP parameters of a WLAN. This is a new layer-2 security policy similar to static WEP. User can select this policy on a WLAN. This policy will be allowed to be configured only when Aironet Extensions are enabled on the WLAN. Once user has selected CKIP he will be given an option to : 1> configure key 2> select MMH There exist a row in this table corresponding to each row representing a WLAN in cLWlanConfigTable. The controller adds or deletes a row to this table whenever a WLAN is added or deleted.')
cLWSecDot11EssCkipEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9, 9, 521, 1, 1, 2, 1), ).setIndexNames((0, "CISCO-LWAPP-WLAN-MIB", "cLWlanIndex"))
if mibBuilder.loadTexts: cLWSecDot11EssCkipEntry.setStatus('current')
if mibBuilder.loadTexts: cLWSecDot11EssCkipEntry.setDescription('Each entry represents a conceptual row in cLWSecDot11EssCkipTable and uniquely identified by cLWlanIndex.')
cLWSecDot11EssCkipSecurity = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 521, 1, 1, 2, 1, 1), TruthValue().clone('false')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cLWSecDot11EssCkipSecurity.setStatus('current')
if mibBuilder.loadTexts: cLWSecDot11EssCkipSecurity.setDescription("This object is used to enable to disable layer-2 CKIP as security policy for this WLAN. When this object is set to 'true', layer-2 CKIP security is enabled. When this object is set to 'false', layer-2 CKIP security is disabled.")
cLWSecDot11EssCkipKeyIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 521, 1, 1, 2, 1, 2), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(0, 4))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cLWSecDot11EssCkipKeyIndex.setStatus('current')
if mibBuilder.loadTexts: cLWSecDot11EssCkipKeyIndex.setDescription("This object specifies the key index corresponding to the key being configured. A value of 0 indicates that the CKIP key hasn't been configured.")
cLWSecDot11EssCkipKeyLength = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 521, 1, 1, 2, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("none", 1), ("len40", 2), ("len104", 3))).clone('none')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cLWSecDot11EssCkipKeyLength.setStatus('current')
if mibBuilder.loadTexts: cLWSecDot11EssCkipKeyLength.setDescription("This object specifies the length of CKIP key in bits that is applicable only when cLWSecDot11EssCkipSecurity is set as 'true'.")
cLWSecDot11EssCkipKeyFmt = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 521, 1, 1, 2, 1, 4), CLSecKeyFormat().clone('default')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cLWSecDot11EssCkipKeyFmt.setStatus('current')
if mibBuilder.loadTexts: cLWSecDot11EssCkipKeyFmt.setDescription('This object specifies the type of the key configured through the object cLWSecDot11EssCkipKey.')
cLWSecDot11EssCkipKey = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 521, 1, 1, 2, 1, 5), OctetString().subtype(subtypeSpec=ValueSizeConstraint(5, 26))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cLWSecDot11EssCkipKey.setStatus('current')
if mibBuilder.loadTexts: cLWSecDot11EssCkipKey.setDescription("This object specifies the CKIP key that is applicable only when cLWSecDot11EssCkipSecurity is set as 'true'. The number of characters to be configured depends on the key length and the key type configured through the objects cLWSecDot11EssCkipKeyLength and cLWSecDot11EssCkipKeyFmt respectively. The combinations are as follows. Key Type Number of characters hex 10/26 hex characters for 40/104 bits ascii 5/13 ascii characters for 40/104 bits. When cLWSecDot11EssCkipKeyFmt is set to 'hex', cLWSecDot11EssCkipKey can only be set to hexadecimal characters. To ensure consistency the following objects must be set together. cLWSecDot11EssCkipKeyFmt cLWSecDot11EssCkipKeyIndex cLWSecDot11EssCkipKeyLength cLWSecDot11EssCkipKey.")
cLWSecDot11EssCkipMMHMode = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 521, 1, 1, 2, 1, 6), TruthValue().clone('false')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cLWSecDot11EssCkipMMHMode.setStatus('current')
if mibBuilder.loadTexts: cLWSecDot11EssCkipMMHMode.setDescription("This object is used to enable or disable MMH MIC mode for the CKIP for this WLAN. 'true' - MMH MIC mode is enabled 'false' - MMH MIC mode is disabled.")
cLWSecDot11EssCkipKPEnable = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 521, 1, 1, 2, 1, 7), TruthValue().clone('false')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cLWSecDot11EssCkipKPEnable.setStatus('current')
if mibBuilder.loadTexts: cLWSecDot11EssCkipKPEnable.setDescription("This object specifies whether CKIP is enabled. When the value is set to 'true', the encryption keys will be generated by permuting the static CKIP key configured through cLWSecDot11EssCkipKey.")
cLWSecDot11EssWebPolicyTable = MibTable((1, 3, 6, 1, 4, 1, 9, 9, 521, 1, 3, 1), )
if mibBuilder.loadTexts: cLWSecDot11EssWebPolicyTable.setStatus('current')
if mibBuilder.loadTexts: cLWSecDot11EssWebPolicyTable.setDescription('This table represents the conditional web-redirect parameters for the WLANs configured on this controller. There exist a row in this table corresponding to each row representing a WLAN in cLWlanConfigTable. The controller adds or deletes a row to this table whenever a WLAN is added or deleted.')
cLWSecDot11EssWebPolicyEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9, 9, 521, 1, 3, 1, 1), ).setIndexNames((0, "CISCO-LWAPP-WLAN-MIB", "cLWlanIndex"))
if mibBuilder.loadTexts: cLWSecDot11EssWebPolicyEntry.setStatus('current')
if mibBuilder.loadTexts: cLWSecDot11EssWebPolicyEntry.setDescription('Each entry represents a conceptual row in cLWSecDot11EssWebPolicyTable and uniquely identified by cLWlanIndex.')
cLWSecDot11EssWebPolicyCondRedirect = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 521, 1, 3, 1, 1, 1), TruthValue().clone('false')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cLWSecDot11EssWebPolicyCondRedirect.setStatus('current')
if mibBuilder.loadTexts: cLWSecDot11EssWebPolicyCondRedirect.setDescription("This object is used to enable or disable conditional redirect. When this attribute is 'true', it signifies that conditional redirect is enabled and redirection of the client is done based on the url-redirect attribute provided by radius server. When this attribute is 'false', it signifies that conditional redirect is disabled and redirection of the client is not done, even if the url-redirect attribute is provided by the radius server. This attribute can be enabled only when 802.1x has been configured as layer-2 security the wlan and web policy is enabled on the wlan.")
cLWSecDot11EssWebPolicySplashPageWebRedirect = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 521, 1, 3, 1, 1, 2), TruthValue().clone('false')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cLWSecDot11EssWebPolicySplashPageWebRedirect.setStatus('current')
if mibBuilder.loadTexts: cLWSecDot11EssWebPolicySplashPageWebRedirect.setDescription("This object is used to enable or disable splash page web redirect. When this attribute is 'true', it signifies that splash page redirect is enabled and redirection of the client is done based on the url-redirect attribute provided by radius server. The redirect function works only for HTTP traffic. HTTPS redirect is not supported for any of the Web Policies. When this attribute is 'false', it signifies that splash page redirect is disabled and redirection of the client is not done. This attribute can be enabled only when 802.1x or WPA1+WPA2 has been configured as layer-2 security on the wlan.")
cLWSecAaaRadiusAuthCallStationIdType = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 521, 1, 4, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13))).clone(namedValues=NamedValues(("ipAddr", 1), ("macAddr", 2), ("apMacAddress", 3), ("apMacAddressSsid", 4), ("apNameSsid", 5), ("apName", 6), ("apGroupName", 7), ("apLocation", 8), ("apVlanId", 9), ("apMacEthAddress", 10), ("apMacEthAddressSsid", 11), ("apLabelAddress", 12), ("apLabelAddressSsid", 13)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cLWSecAaaRadiusAuthCallStationIdType.setStatus('current')
if mibBuilder.loadTexts: cLWSecAaaRadiusAuthCallStationIdType.setDescription('This object specifies the configured the call station ID information sent in RADIUS authentication messages.')
cLWSecAaaRadiusAccUsernameDelimiter = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 521, 1, 4, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))).clone(namedValues=NamedValues(("noDelimiter", 1), ("hyphen", 2), ("colon", 3), ("singleHyphen", 4)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cLWSecAaaRadiusAccUsernameDelimiter.setStatus('current')
if mibBuilder.loadTexts: cLWSecAaaRadiusAccUsernameDelimiter.setDescription('This object specifies the delimiter to be used when displaying the username for accounting request. For example, if the value of the username for accounting request is 1234567890ab. noDelimiter - display it as 1234567890ab. hyphen - display it as 12-34-56-78-90-ab colon - display it as 12:34:56:78:90:ab singleHyphen - display it as 123456-7890ab')
ciscoLwappWlanSecurityMIBCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 521, 2, 1))
ciscoLwappWlanSecurityMIBGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 521, 2, 2))
ciscoLwappWlanSecurityMIBCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 9, 9, 521, 2, 1, 1)).setObjects(("CISCO-LWAPP-WLAN-SECURITY-MIB", "ciscoLwappWlanSecurityCckmConfigGroup"), ("CISCO-LWAPP-WLAN-SECURITY-MIB", "ciscoLwappWlanSecurityCkipConfigGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoLwappWlanSecurityMIBCompliance = ciscoLwappWlanSecurityMIBCompliance.setStatus('deprecated')
if mibBuilder.loadTexts: ciscoLwappWlanSecurityMIBCompliance.setDescription('The compliance statement for the SNMP entities that implement the ciscoLwappWlanSecurityMIB module.')
ciscoLwappWlanSecurityMIBComplianceRev1 = ModuleCompliance((1, 3, 6, 1, 4, 1, 9, 9, 521, 2, 1, 2)).setObjects(("CISCO-LWAPP-WLAN-SECURITY-MIB", "ciscoLwappWlanSecurityCckmConfigGroup"), ("CISCO-LWAPP-WLAN-SECURITY-MIB", "ciscoLwappWlanSecurityCkipConfigGroup"), ("CISCO-LWAPP-WLAN-SECURITY-MIB", "ciscoLwappWlanSecurityWebPolicyConfigGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoLwappWlanSecurityMIBComplianceRev1 = ciscoLwappWlanSecurityMIBComplianceRev1.setStatus('deprecated')
if mibBuilder.loadTexts: ciscoLwappWlanSecurityMIBComplianceRev1.setDescription('The compliance statement for the SNMP entities that implement the ciscoLwappWlanSecurityMIB module.')
ciscoLwappWlanSecurityMIBComplianceRev2 = ModuleCompliance((1, 3, 6, 1, 4, 1, 9, 9, 521, 2, 1, 3)).setObjects(("CISCO-LWAPP-WLAN-SECURITY-MIB", "ciscoLwappWlanSecurityCckmConfigGroup"), ("CISCO-LWAPP-WLAN-SECURITY-MIB", "ciscoLwappWlanSecurityCkipConfigGroup"), ("CISCO-LWAPP-WLAN-SECURITY-MIB", "ciscoLwappWlanSecurityWebPolicyConfigGroup"), ("CISCO-LWAPP-WLAN-SECURITY-MIB", "ciscoLwappWlanSecurityAaaConfigGroup"), ("CISCO-LWAPP-WLAN-SECURITY-MIB", "ciscoLwappWlanSecurityFtConfigGroup"), ("CISCO-LWAPP-WLAN-SECURITY-MIB", "ciscoLwappWlanSecurityPfmConfigGroup"), ("CISCO-LWAPP-WLAN-SECURITY-MIB", "ciscoLwappWlanSecurityCckmConfigGroup1"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoLwappWlanSecurityMIBComplianceRev2 = ciscoLwappWlanSecurityMIBComplianceRev2.setStatus('current')
if mibBuilder.loadTexts: ciscoLwappWlanSecurityMIBComplianceRev2.setDescription('The compliance statement for the SNMP entities that implement the ciscoLwappWlanSecurityMIB module.')
ciscoLwappWlanSecurityCckmConfigGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 521, 2, 2, 1)).setObjects(("CISCO-LWAPP-WLAN-SECURITY-MIB", "cLWSecDot11EssCckmWpaSupport"), ("CISCO-LWAPP-WLAN-SECURITY-MIB", "cLWSecDot11EssCckmWpa1Security"), ("CISCO-LWAPP-WLAN-SECURITY-MIB", "cLWSecDot11EssCckmWpa1EncType"), ("CISCO-LWAPP-WLAN-SECURITY-MIB", "cLWSecDot11EssCckmWpa2Security"), ("CISCO-LWAPP-WLAN-SECURITY-MIB", "cLWSecDot11EssCckmWpa2EncType"), ("CISCO-LWAPP-WLAN-SECURITY-MIB", "cLWSecDot11EssCckmKeyMgmtMode"), ("CISCO-LWAPP-WLAN-SECURITY-MIB", "cLWSecDot11EssPskFmt"), ("CISCO-LWAPP-WLAN-SECURITY-MIB", "cLWSecDot11EssPsk"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoLwappWlanSecurityCckmConfigGroup = ciscoLwappWlanSecurityCckmConfigGroup.setStatus('current')
if mibBuilder.loadTexts: ciscoLwappWlanSecurityCckmConfigGroup.setDescription('This collection of objects represents CCKM related security parameters on a WLAN. The collection also configures the pre-shared keys when PSK is configured as the key management type.')
ciscoLwappWlanSecurityCkipConfigGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 521, 2, 2, 2)).setObjects(("CISCO-LWAPP-WLAN-SECURITY-MIB", "cLWSecDot11EssCkipSecurity"), ("CISCO-LWAPP-WLAN-SECURITY-MIB", "cLWSecDot11EssCkipKeyIndex"), ("CISCO-LWAPP-WLAN-SECURITY-MIB", "cLWSecDot11EssCkipKeyLength"), ("CISCO-LWAPP-WLAN-SECURITY-MIB", "cLWSecDot11EssCkipKeyFmt"), ("CISCO-LWAPP-WLAN-SECURITY-MIB", "cLWSecDot11EssCkipKey"), ("CISCO-LWAPP-WLAN-SECURITY-MIB", "cLWSecDot11EssCkipMMHMode"), ("CISCO-LWAPP-WLAN-SECURITY-MIB", "cLWSecDot11EssCkipKPEnable"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoLwappWlanSecurityCkipConfigGroup = ciscoLwappWlanSecurityCkipConfigGroup.setStatus('current')
if mibBuilder.loadTexts: ciscoLwappWlanSecurityCkipConfigGroup.setDescription('This collection of objects represents CKIP related security parameters on a WLAN.')
ciscoLwappWlanSecurityWebPolicyConfigGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 521, 2, 2, 3)).setObjects(("CISCO-LWAPP-WLAN-SECURITY-MIB", "cLWSecDot11EssWebPolicyCondRedirect"), ("CISCO-LWAPP-WLAN-SECURITY-MIB", "cLWSecDot11EssWebPolicySplashPageWebRedirect"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoLwappWlanSecurityWebPolicyConfigGroup = ciscoLwappWlanSecurityWebPolicyConfigGroup.setStatus('current')
if mibBuilder.loadTexts: ciscoLwappWlanSecurityWebPolicyConfigGroup.setDescription('This collection of objects represents conditional redirect parameters on a WLAN.')
ciscoLwappWlanSecurityAaaConfigGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 521, 2, 2, 4)).setObjects(("CISCO-LWAPP-WLAN-SECURITY-MIB", "cLWSecAaaRadiusAuthCallStationIdType"), ("CISCO-LWAPP-WLAN-SECURITY-MIB", "cLWSecAaaRadiusAccUsernameDelimiter"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoLwappWlanSecurityAaaConfigGroup = ciscoLwappWlanSecurityAaaConfigGroup.setStatus('current')
if mibBuilder.loadTexts: ciscoLwappWlanSecurityAaaConfigGroup.setDescription('This collection of objects represents AAA related security parameters on a WLAN.')
ciscoLwappWlanSecurityFtConfigGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 521, 2, 2, 5)).setObjects(("CISCO-LWAPP-WLAN-SECURITY-MIB", "cLWSecDot11EssFtEnable"), ("CISCO-LWAPP-WLAN-SECURITY-MIB", "cLWSecDot11EssFtReassocTime"), ("CISCO-LWAPP-WLAN-SECURITY-MIB", "cLWSecDot11EssFtOverDs"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoLwappWlanSecurityFtConfigGroup = ciscoLwappWlanSecurityFtConfigGroup.setStatus('current')
if mibBuilder.loadTexts: ciscoLwappWlanSecurityFtConfigGroup.setDescription('This collection of objects represents fast transition related security parameters on a WLAN.')
ciscoLwappWlanSecurityPfmConfigGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 521, 2, 2, 6)).setObjects(("CISCO-LWAPP-WLAN-SECURITY-MIB", "cLWSecDot11Ess11wPfm"), ("CISCO-LWAPP-WLAN-SECURITY-MIB", "cLWSecDot11EssRetryTime"), ("CISCO-LWAPP-WLAN-SECURITY-MIB", "cLWSecDot11EssComebackTime"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoLwappWlanSecurityPfmConfigGroup = ciscoLwappWlanSecurityPfmConfigGroup.setStatus('current')
if mibBuilder.loadTexts: ciscoLwappWlanSecurityPfmConfigGroup.setDescription('This collection of objects represents PFM related security parameters on a WLAN.')
ciscoLwappWlanSecurityCckmConfigGroup1 = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 521, 2, 2, 7)).setObjects(("CISCO-LWAPP-WLAN-SECURITY-MIB", "cLWSecDot11EssCckmGtkRandomize"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoLwappWlanSecurityCckmConfigGroup1 = ciscoLwappWlanSecurityCckmConfigGroup1.setStatus('current')
if mibBuilder.loadTexts: ciscoLwappWlanSecurityCckmConfigGroup1.setDescription('This collection of objects represents GTK randomization information.')
mibBuilder.exportSymbols("CISCO-LWAPP-WLAN-SECURITY-MIB", cLWSecDot11EssCckmEntry=cLWSecDot11EssCckmEntry, cLWSecDot11EssCkipSecurity=cLWSecDot11EssCkipSecurity, clwsAaaConfig=clwsAaaConfig, cLWSecDot11EssPskFmt=cLWSecDot11EssPskFmt, cLWSecDot11EssCckmWpa2Security=cLWSecDot11EssCckmWpa2Security, cLWSecDot11EssFtEnable=cLWSecDot11EssFtEnable, ciscoLwappWlanSecurityMIBComplianceRev2=ciscoLwappWlanSecurityMIBComplianceRev2, ciscoLwappWlanSecurityMIBCompliance=ciscoLwappWlanSecurityMIBCompliance, cLWSecDot11EssCkipMMHMode=cLWSecDot11EssCkipMMHMode, ciscoLwappWlanSecurityCckmConfigGroup1=ciscoLwappWlanSecurityCckmConfigGroup1, cLWSecDot11EssCkipKPEnable=cLWSecDot11EssCkipKPEnable, ciscoLwappWlanSecurityPfmConfigGroup=ciscoLwappWlanSecurityPfmConfigGroup, cLWSecDot11EssWebPolicyEntry=cLWSecDot11EssWebPolicyEntry, cLWSecDot11EssComebackTime=cLWSecDot11EssComebackTime, ciscoLwappWlanSecurityMIBGroups=ciscoLwappWlanSecurityMIBGroups, cLWSecDot11EssWebPolicySplashPageWebRedirect=cLWSecDot11EssWebPolicySplashPageWebRedirect, cLWSecDot11EssCckmWpa2EncType=cLWSecDot11EssCckmWpa2EncType, cLWSecDot11EssCckmWpa1Security=cLWSecDot11EssCckmWpa1Security, cLWSecDot11EssFtOverDs=cLWSecDot11EssFtOverDs, ciscoLwappWlanSecurityCkipConfigGroup=ciscoLwappWlanSecurityCkipConfigGroup, ciscoLwappWlanSecurityWebPolicyConfigGroup=ciscoLwappWlanSecurityWebPolicyConfigGroup, clwsWebPolicyConfig=clwsWebPolicyConfig, ciscoLwappWlanSecurityMIBConform=ciscoLwappWlanSecurityMIBConform, cLWSecDot11Ess11wPfm=cLWSecDot11Ess11wPfm, cLWSecDot11EssWebPolicyCondRedirect=cLWSecDot11EssWebPolicyCondRedirect, ciscoLwappWlanSecurityMIB=ciscoLwappWlanSecurityMIB, cLWSecDot11EssCckmTable=cLWSecDot11EssCckmTable, ciscoLwappWlanSecurityAaaConfigGroup=ciscoLwappWlanSecurityAaaConfigGroup, cLWSecDot11EssCckmWpa1EncType=cLWSecDot11EssCckmWpa1EncType, ciscoLwappWlanSecurityMIBObjects=ciscoLwappWlanSecurityMIBObjects, cLWSecDot11EssCkipEntry=cLWSecDot11EssCkipEntry, clwsCkipConfig=clwsCkipConfig, cLWSecDot11EssCckmWpaSupport=cLWSecDot11EssCckmWpaSupport, cLWSecDot11EssCckmGtkRandomize=cLWSecDot11EssCckmGtkRandomize, cLWSecDot11EssFtReassocTime=cLWSecDot11EssFtReassocTime, cLWSecDot11EssCckmKeyMgmtMode=cLWSecDot11EssCckmKeyMgmtMode, cLWSecDot11EssPsk=cLWSecDot11EssPsk, cLWSecDot11EssRetryTime=cLWSecDot11EssRetryTime, ciscoLwappWlanSecurityMIBCompliances=ciscoLwappWlanSecurityMIBCompliances, cLWSecDot11EssCkipKeyIndex=cLWSecDot11EssCkipKeyIndex, cLWSecAaaRadiusAuthCallStationIdType=cLWSecAaaRadiusAuthCallStationIdType, cLWSecAaaRadiusAccUsernameDelimiter=cLWSecAaaRadiusAccUsernameDelimiter, cLWSecDot11EssCkipKeyFmt=cLWSecDot11EssCkipKeyFmt, cLWSecDot11EssCkipKey=cLWSecDot11EssCkipKey, cLWSecDot11EssCkipKeyLength=cLWSecDot11EssCkipKeyLength, cLWSecDot11EssWebPolicyTable=cLWSecDot11EssWebPolicyTable, ciscoLwappWlanSecurityMIBNotifs=ciscoLwappWlanSecurityMIBNotifs, ciscoLwappWlanSecurityMIBComplianceRev1=ciscoLwappWlanSecurityMIBComplianceRev1, ciscoLwappWlanSecurityCckmConfigGroup=ciscoLwappWlanSecurityCckmConfigGroup, cLWSecDot11EssCkipTable=cLWSecDot11EssCkipTable, ciscoLwappWlanSecurityFtConfigGroup=ciscoLwappWlanSecurityFtConfigGroup, clwsCckmConfig=clwsCckmConfig, PYSNMP_MODULE_ID=ciscoLwappWlanSecurityMIB)