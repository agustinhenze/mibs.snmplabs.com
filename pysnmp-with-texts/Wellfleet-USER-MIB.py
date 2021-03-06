#
# PySNMP MIB module Wellfleet-USER-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/Wellfleet-USER-MIB
# Produced by pysmi-0.3.4 at Wed May  1 15:42:05 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
OctetString, ObjectIdentifier, Integer = mibBuilder.importSymbols("ASN1", "OctetString", "ObjectIdentifier", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ConstraintsUnion, ValueRangeConstraint, ValueSizeConstraint, SingleValueConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ConstraintsUnion", "ValueRangeConstraint", "ValueSizeConstraint", "SingleValueConstraint")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
iso, NotificationType, Integer32, Gauge32, MibIdentifier, MibScalar, MibTable, MibTableRow, MibTableColumn, IpAddress, Counter32, TimeTicks, ObjectIdentity, Counter64, Bits, ModuleIdentity, Unsigned32 = mibBuilder.importSymbols("SNMPv2-SMI", "iso", "NotificationType", "Integer32", "Gauge32", "MibIdentifier", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "IpAddress", "Counter32", "TimeTicks", "ObjectIdentity", "Counter64", "Bits", "ModuleIdentity", "Unsigned32")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
wfUserServicesGroup, = mibBuilder.importSymbols("Wellfleet-COMMON-MIB", "wfUserServicesGroup")
wfUserAccess = MibIdentifier((1, 3, 6, 1, 4, 1, 18, 3, 3, 2, 22, 1))
wfUserAccessDelete = MibScalar((1, 3, 6, 1, 4, 1, 18, 3, 3, 2, 22, 1, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("created", 1), ("deleted", 2))).clone('created')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: wfUserAccessDelete.setStatus('mandatory')
if mibBuilder.loadTexts: wfUserAccessDelete.setDescription('Indication to create or delete User Access record.')
wfUserAccessConfig = MibScalar((1, 3, 6, 1, 4, 1, 18, 3, 3, 2, 22, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enabled", 1), ("disabled", 2))).clone('enabled')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: wfUserAccessConfig.setStatus('mandatory')
if mibBuilder.loadTexts: wfUserAccessConfig.setDescription('Indicates local password (configuration file ) information is to be used')
wfUserAccessRadius = MibScalar((1, 3, 6, 1, 4, 1, 18, 3, 3, 2, 22, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enabled", 1), ("disabled", 2))).clone('disabled')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: wfUserAccessRadius.setStatus('mandatory')
if mibBuilder.loadTexts: wfUserAccessRadius.setDescription('Indicates radius authentication server is to be used')
wfUserAccessMaxLogin = MibScalar((1, 3, 6, 1, 4, 1, 18, 3, 3, 2, 22, 1, 4), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 16)).clone(16)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: wfUserAccessMaxLogin.setStatus('mandatory')
if mibBuilder.loadTexts: wfUserAccessMaxLogin.setDescription('This the maximum allowed login name, in the range 1 to 16')
wfUserAccessMinLogin = MibScalar((1, 3, 6, 1, 4, 1, 18, 3, 3, 2, 22, 1, 5), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 16)).clone(4)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: wfUserAccessMinLogin.setStatus('mandatory')
if mibBuilder.loadTexts: wfUserAccessMinLogin.setDescription('This the minimum allowed login name, in the range 1 to 16')
wfUserAccessMaxGroup = MibScalar((1, 3, 6, 1, 4, 1, 18, 3, 3, 2, 22, 1, 6), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 16)).clone(16)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: wfUserAccessMaxGroup.setStatus('mandatory')
if mibBuilder.loadTexts: wfUserAccessMaxGroup.setDescription('This the maximum allowed Group name, in the range 1 to 16')
wfUserAccessMinGroup = MibScalar((1, 3, 6, 1, 4, 1, 18, 3, 3, 2, 22, 1, 7), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 16)).clone(4)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: wfUserAccessMinGroup.setStatus('mandatory')
if mibBuilder.loadTexts: wfUserAccessMinGroup.setDescription('This the minimum allowed Group name, in the range 1 to 16')
wfUserAccessMaxPassword = MibScalar((1, 3, 6, 1, 4, 1, 18, 3, 3, 2, 22, 1, 8), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 16)).clone(16)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: wfUserAccessMaxPassword.setStatus('mandatory')
if mibBuilder.loadTexts: wfUserAccessMaxPassword.setDescription('This the maximum allowed Password , in the range 1 to 16')
wfUserAccessMinPassword = MibScalar((1, 3, 6, 1, 4, 1, 18, 3, 3, 2, 22, 1, 9), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 16))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: wfUserAccessMinPassword.setStatus('mandatory')
if mibBuilder.loadTexts: wfUserAccessMinPassword.setDescription('This the minimum allowed Password, in the range 0 to 16')
wfUserManagerLock = MibScalar((1, 3, 6, 1, 4, 1, 18, 3, 3, 2, 22, 1, 10), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("enabled", 1), ("disabled", 2), ("serverwait", 3))).clone('disabled')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: wfUserManagerLock.setStatus('mandatory')
if mibBuilder.loadTexts: wfUserManagerLock.setDescription('When enabled Manager and user are not usable')
wfUserAccessRadiusAcctEnable = MibScalar((1, 3, 6, 1, 4, 1, 18, 3, 3, 2, 22, 1, 11), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enabled", 1), ("disabled", 2))).clone('disabled')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: wfUserAccessRadiusAcctEnable.setStatus('mandatory')
if mibBuilder.loadTexts: wfUserAccessRadiusAcctEnable.setDescription('When enabled Radius Accouting is performed for Login Access')
wfUserAccessNameTable = MibTable((1, 3, 6, 1, 4, 1, 18, 3, 3, 2, 22, 2), )
if mibBuilder.loadTexts: wfUserAccessNameTable.setStatus('mandatory')
if mibBuilder.loadTexts: wfUserAccessNameTable.setDescription('A table to contain user information to be searched on the router')
wfUserAccessNameEntry = MibTableRow((1, 3, 6, 1, 4, 1, 18, 3, 3, 2, 22, 2, 1), ).setIndexNames((0, "Wellfleet-USER-MIB", "wfUserAccessNameId"))
if mibBuilder.loadTexts: wfUserAccessNameEntry.setStatus('mandatory')
if mibBuilder.loadTexts: wfUserAccessNameEntry.setDescription('The attributes for individual User account')
wfUserAccessNameDelete = MibTableColumn((1, 3, 6, 1, 4, 1, 18, 3, 3, 2, 22, 2, 1, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("created", 1), ("deleted", 2))).clone('created')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: wfUserAccessNameDelete.setStatus('mandatory')
if mibBuilder.loadTexts: wfUserAccessNameDelete.setDescription('Indication to create or delete a user record')
wfUserAccessNameDisable = MibTableColumn((1, 3, 6, 1, 4, 1, 18, 3, 3, 2, 22, 2, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enabled", 1), ("disabled", 2))).clone('enabled')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: wfUserAccessNameDisable.setStatus('mandatory')
if mibBuilder.loadTexts: wfUserAccessNameDisable.setDescription('enable/disable this user login')
wfUserAccessNameId = MibTableColumn((1, 3, 6, 1, 4, 1, 18, 3, 3, 2, 22, 2, 1, 3), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: wfUserAccessNameId.setStatus('mandatory')
if mibBuilder.loadTexts: wfUserAccessNameId.setDescription('Login name of the user ')
wfUserAccessNameName = MibTableColumn((1, 3, 6, 1, 4, 1, 18, 3, 3, 2, 22, 2, 1, 4), DisplayString()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: wfUserAccessNameName.setStatus('mandatory')
if mibBuilder.loadTexts: wfUserAccessNameName.setDescription('True name of the user')
wfUserAccessNamePasswd = MibTableColumn((1, 3, 6, 1, 4, 1, 18, 3, 3, 2, 22, 2, 1, 5), DisplayString()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: wfUserAccessNamePasswd.setStatus('mandatory')
if mibBuilder.loadTexts: wfUserAccessNamePasswd.setDescription('Encripted user password')
wfUserAccessNameGroups = MibTableColumn((1, 3, 6, 1, 4, 1, 18, 3, 3, 2, 22, 2, 1, 6), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: wfUserAccessNameGroups.setStatus('mandatory')
if mibBuilder.loadTexts: wfUserAccessNameGroups.setDescription('Bit Field of the groups the user belongs to')
wfUserAccessNameAudit = MibTableColumn((1, 3, 6, 1, 4, 1, 18, 3, 3, 2, 22, 2, 1, 7), Integer32().clone(1)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: wfUserAccessNameAudit.setStatus('mandatory')
if mibBuilder.loadTexts: wfUserAccessNameAudit.setDescription('Audit level for this user 0 No Audit Bit 1 Manager Bit 2 User Bit 3 Operator All Bits Anything user typed All others RFU ')
wfUserAccessNameScript = MibTableColumn((1, 3, 6, 1, 4, 1, 18, 3, 3, 2, 22, 2, 1, 8), DisplayString()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: wfUserAccessNameScript.setStatus('mandatory')
if mibBuilder.loadTexts: wfUserAccessNameScript.setDescription('User specified BCC startup script')
wfUserAccessActiveTable = MibTable((1, 3, 6, 1, 4, 1, 18, 3, 3, 2, 22, 3), )
if mibBuilder.loadTexts: wfUserAccessActiveTable.setStatus('mandatory')
if mibBuilder.loadTexts: wfUserAccessActiveTable.setDescription(' Group access table definition')
wfUserAccessActiveEntry = MibTableRow((1, 3, 6, 1, 4, 1, 18, 3, 3, 2, 22, 3, 1), ).setIndexNames((0, "Wellfleet-USER-MIB", "wfUserAccessActiveLoginAddress"), (0, "Wellfleet-USER-MIB", "wfUserAccessActivePort"))
if mibBuilder.loadTexts: wfUserAccessActiveEntry.setStatus('mandatory')
if mibBuilder.loadTexts: wfUserAccessActiveEntry.setDescription('records indicating active users')
wfUserAccessActiveDelete = MibTableColumn((1, 3, 6, 1, 4, 1, 18, 3, 3, 2, 22, 3, 1, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("created", 1), ("deleted", 2))).clone('created')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: wfUserAccessActiveDelete.setStatus('mandatory')
if mibBuilder.loadTexts: wfUserAccessActiveDelete.setDescription('Indication ot create/delete a active user record')
wfUserAccessActiveDisable = MibTableColumn((1, 3, 6, 1, 4, 1, 18, 3, 3, 2, 22, 3, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enabled", 1), ("disabled", 2))).clone('enabled')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: wfUserAccessActiveDisable.setStatus('mandatory')
if mibBuilder.loadTexts: wfUserAccessActiveDisable.setDescription('Enable/disable this record')
wfUserAccessActiveId = MibTableColumn((1, 3, 6, 1, 4, 1, 18, 3, 3, 2, 22, 3, 1, 3), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: wfUserAccessActiveId.setStatus('mandatory')
if mibBuilder.loadTexts: wfUserAccessActiveId.setDescription('Login name of the login ')
wfUserAccessActiveLoginAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 18, 3, 3, 2, 22, 3, 1, 4), IpAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: wfUserAccessActiveLoginAddress.setStatus('mandatory')
if mibBuilder.loadTexts: wfUserAccessActiveLoginAddress.setDescription('Indicated the IP address this user is logged in from. zero indidates the console. This is undefined when the users state is logout')
wfUserAccessActivePort = MibTableColumn((1, 3, 6, 1, 4, 1, 18, 3, 3, 2, 22, 3, 1, 5), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: wfUserAccessActivePort.setStatus('mandatory')
if mibBuilder.loadTexts: wfUserAccessActivePort.setDescription('Port number this user is logged in on ( identifies multiple logins from the same ip address')
wfUserAccessActiveState = MibTableColumn((1, 3, 6, 1, 4, 1, 18, 3, 3, 2, 22, 3, 1, 6), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("active", 1), ("config", 2), ("ftp", 3))).clone('active')).setMaxAccess("readonly")
if mibBuilder.loadTexts: wfUserAccessActiveState.setStatus('mandatory')
if mibBuilder.loadTexts: wfUserAccessActiveState.setDescription('Current State ofthis login ')
wfUserAccessActiveCmd = MibTableColumn((1, 3, 6, 1, 4, 1, 18, 3, 3, 2, 22, 3, 1, 7), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: wfUserAccessActiveCmd.setStatus('mandatory')
if mibBuilder.loadTexts: wfUserAccessActiveCmd.setDescription('Last Command Issued by the user')
wfUserAccessActiveLastCmdTime = MibTableColumn((1, 3, 6, 1, 4, 1, 18, 3, 3, 2, 22, 3, 1, 8), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: wfUserAccessActiveLastCmdTime.setStatus('mandatory')
if mibBuilder.loadTexts: wfUserAccessActiveLastCmdTime.setDescription('Time last command issued ')
wfUserAccessActiveLoginTime = MibTableColumn((1, 3, 6, 1, 4, 1, 18, 3, 3, 2, 22, 3, 1, 9), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: wfUserAccessActiveLoginTime.setStatus('mandatory')
if mibBuilder.loadTexts: wfUserAccessActiveLoginTime.setDescription('Time user logged in ')
wfUserAccessActiveAcctInOctets = MibTableColumn((1, 3, 6, 1, 4, 1, 18, 3, 3, 2, 22, 3, 1, 10), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: wfUserAccessActiveAcctInOctets.setStatus('mandatory')
if mibBuilder.loadTexts: wfUserAccessActiveAcctInOctets.setDescription('Number of Octets Received ')
wfUserAccessActiveAcctOutOctets = MibTableColumn((1, 3, 6, 1, 4, 1, 18, 3, 3, 2, 22, 3, 1, 11), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: wfUserAccessActiveAcctOutOctets.setStatus('mandatory')
if mibBuilder.loadTexts: wfUserAccessActiveAcctOutOctets.setDescription('Number of Octets Sent ')
wfUserAccessActiveAcctAccessType = MibTableColumn((1, 3, 6, 1, 4, 1, 18, 3, 3, 2, 22, 3, 1, 12), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("console", 1), ("telnet", 2), ("ftp", 3))).clone('console')).setMaxAccess("readonly")
if mibBuilder.loadTexts: wfUserAccessActiveAcctAccessType.setStatus('mandatory')
if mibBuilder.loadTexts: wfUserAccessActiveAcctAccessType.setDescription('Type of login access ')
wfUserAccessActiveAcctTermCause = MibTableColumn((1, 3, 6, 1, 4, 1, 18, 3, 3, 2, 22, 3, 1, 13), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: wfUserAccessActiveAcctTermCause.setStatus('mandatory')
if mibBuilder.loadTexts: wfUserAccessActiveAcctTermCause.setDescription('Reason for ACCT session termination ')
wfUserAccessActiveAcctServiceType = MibTableColumn((1, 3, 6, 1, 4, 1, 18, 3, 3, 2, 22, 3, 1, 14), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: wfUserAccessActiveAcctServiceType.setStatus('mandatory')
if mibBuilder.loadTexts: wfUserAccessActiveAcctServiceType.setDescription('Accounting Service Type ')
wfUserAccessActiveAcctNasPortType = MibTableColumn((1, 3, 6, 1, 4, 1, 18, 3, 3, 2, 22, 3, 1, 15), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: wfUserAccessActiveAcctNasPortType.setStatus('mandatory')
if mibBuilder.loadTexts: wfUserAccessActiveAcctNasPortType.setDescription('NAS Port type ')
wfUserAccessActiveAcctPriv = MibTableColumn((1, 3, 6, 1, 4, 1, 18, 3, 3, 2, 22, 3, 1, 16), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: wfUserAccessActiveAcctPriv.setStatus('mandatory')
if mibBuilder.loadTexts: wfUserAccessActiveAcctPriv.setDescription('Access Privilege for account ')
wfUserAccessGroupTable = MibTable((1, 3, 6, 1, 4, 1, 18, 3, 3, 2, 22, 4), )
if mibBuilder.loadTexts: wfUserAccessGroupTable.setStatus('mandatory')
if mibBuilder.loadTexts: wfUserAccessGroupTable.setDescription(' Group access table definition')
wfUserAccessGroupEntry = MibTableRow((1, 3, 6, 1, 4, 1, 18, 3, 3, 2, 22, 4, 1), ).setIndexNames((0, "Wellfleet-USER-MIB", "wfUserAccessGroupNumber"))
if mibBuilder.loadTexts: wfUserAccessGroupEntry.setStatus('mandatory')
if mibBuilder.loadTexts: wfUserAccessGroupEntry.setDescription('Group Names')
wfUserAccessGroupDelete = MibTableColumn((1, 3, 6, 1, 4, 1, 18, 3, 3, 2, 22, 4, 1, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("created", 1), ("deleted", 2))).clone('created')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: wfUserAccessGroupDelete.setStatus('mandatory')
if mibBuilder.loadTexts: wfUserAccessGroupDelete.setDescription('Indication of create/delete a group record')
wfUserAccessGroupDisable = MibTableColumn((1, 3, 6, 1, 4, 1, 18, 3, 3, 2, 22, 4, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enabled", 1), ("disabled", 2))).clone('enabled')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: wfUserAccessGroupDisable.setStatus('mandatory')
if mibBuilder.loadTexts: wfUserAccessGroupDisable.setDescription('Enable/disable this group')
wfUserAccessGroupNumber = MibTableColumn((1, 3, 6, 1, 4, 1, 18, 3, 3, 2, 22, 4, 1, 3), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: wfUserAccessGroupNumber.setStatus('mandatory')
if mibBuilder.loadTexts: wfUserAccessGroupNumber.setDescription('Number of this group')
wfUserAccessGroupName = MibTableColumn((1, 3, 6, 1, 4, 1, 18, 3, 3, 2, 22, 4, 1, 4), DisplayString()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: wfUserAccessGroupName.setStatus('mandatory')
if mibBuilder.loadTexts: wfUserAccessGroupName.setDescription('Name of this group')
wfUserAccessGroupPriv = MibTableColumn((1, 3, 6, 1, 4, 1, 18, 3, 3, 2, 22, 4, 1, 5), Integer32().clone(2)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: wfUserAccessGroupPriv.setStatus('mandatory')
if mibBuilder.loadTexts: wfUserAccessGroupPriv.setDescription('Bit field of priveledge classes for this group Bit 1 Manager Bit 2 User Bit 3 Operator All others RFU ')
wfUserAccessGroupAudit = MibTableColumn((1, 3, 6, 1, 4, 1, 18, 3, 3, 2, 22, 4, 1, 6), Integer32().clone(2)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: wfUserAccessGroupAudit.setStatus('mandatory')
if mibBuilder.loadTexts: wfUserAccessGroupAudit.setDescription('Bit field matching the group priveledge levels indicating what should or should not be logged 0 No audit Bit 1 Manager Bit 2 User Bit 3 Operator All bits Anything user typed All others RFU ')
wfUserAudit = MibIdentifier((1, 3, 6, 1, 4, 1, 18, 3, 3, 2, 22, 5))
wfUserAuditDelete = MibScalar((1, 3, 6, 1, 4, 1, 18, 3, 3, 2, 22, 5, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("created", 1), ("deleted", 2))).clone('created')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: wfUserAuditDelete.setStatus('mandatory')
if mibBuilder.loadTexts: wfUserAuditDelete.setDescription('Indication to create or delete Audit record.')
wfUserAuditDisable = MibScalar((1, 3, 6, 1, 4, 1, 18, 3, 3, 2, 22, 5, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enabled", 1), ("disabled", 2))).clone('enabled')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: wfUserAuditDisable.setStatus('mandatory')
if mibBuilder.loadTexts: wfUserAuditDisable.setDescription('Indication to enable/disable Audit subsystem.')
wfUserAuditlevel = MibScalar((1, 3, 6, 1, 4, 1, 18, 3, 3, 2, 22, 5, 3), Integer32().clone(1)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: wfUserAuditlevel.setStatus('mandatory')
if mibBuilder.loadTexts: wfUserAuditlevel.setDescription(' A bit field priveledge levels to audit log. This field is global, groups may override this system default 0 No audit Bit 1 Manager Bit 2 User Bit 3 Operator All bits Anything user typed All others RFU ')
wfUserBccLock = MibIdentifier((1, 3, 6, 1, 4, 1, 18, 3, 3, 2, 22, 6))
wfUserBccLockDelete = MibScalar((1, 3, 6, 1, 4, 1, 18, 3, 3, 2, 22, 6, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("created", 1), ("deleted", 2))).clone('created')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: wfUserBccLockDelete.setStatus('mandatory')
if mibBuilder.loadTexts: wfUserBccLockDelete.setDescription('Indication to create or delete BCC lock record.')
wfUserBccLockId = MibScalar((1, 3, 6, 1, 4, 1, 18, 3, 3, 2, 22, 6, 2), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: wfUserBccLockId.setStatus('mandatory')
if mibBuilder.loadTexts: wfUserBccLockId.setDescription('Indicates which BCC/TI user has a configuration mode lock')
wfUserBccLockTimer = MibScalar((1, 3, 6, 1, 4, 1, 18, 3, 3, 2, 22, 6, 3), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: wfUserBccLockTimer.setStatus('mandatory')
if mibBuilder.loadTexts: wfUserBccLockTimer.setDescription('Indicated last time config changed ')
wfUserBccLockAddress = MibScalar((1, 3, 6, 1, 4, 1, 18, 3, 3, 2, 22, 6, 4), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: wfUserBccLockAddress.setStatus('mandatory')
if mibBuilder.loadTexts: wfUserBccLockAddress.setDescription(' IP address of the User holding the lock, used to access wfUserAccessActiveTable see below')
wfUserBccLockPort = MibScalar((1, 3, 6, 1, 4, 1, 18, 3, 3, 2, 22, 6, 5), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: wfUserBccLockPort.setStatus('mandatory')
if mibBuilder.loadTexts: wfUserBccLockPort.setDescription(' IP port of the User holding the lock, used to access wfUserAccessActiveTable ')
wfUserBccConfig = MibIdentifier((1, 3, 6, 1, 4, 1, 18, 3, 3, 2, 22, 7))
wfUserBccConfigDelete = MibScalar((1, 3, 6, 1, 4, 1, 18, 3, 3, 2, 22, 7, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("created", 1), ("deleted", 2))).clone('created')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: wfUserBccConfigDelete.setStatus('mandatory')
if mibBuilder.loadTexts: wfUserBccConfigDelete.setDescription('Indication to create or delete BCC configuration record.')
wfUserBccConfigDefaultShell = MibScalar((1, 3, 6, 1, 4, 1, 18, 3, 3, 2, 22, 7, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enabled", 1), ("disabled", 2))).clone('disabled')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: wfUserBccConfigDefaultShell.setStatus('mandatory')
if mibBuilder.loadTexts: wfUserBccConfigDefaultShell.setDescription('Should BCC be started as the default shell, if resources are avaliable. if disabled, TI is the default shell')
mibBuilder.exportSymbols("Wellfleet-USER-MIB", wfUserAccessNameGroups=wfUserAccessNameGroups, wfUserAccessConfig=wfUserAccessConfig, wfUserAccessNameEntry=wfUserAccessNameEntry, wfUserAccessGroupNumber=wfUserAccessGroupNumber, wfUserAccessMinPassword=wfUserAccessMinPassword, wfUserAccessActiveAcctInOctets=wfUserAccessActiveAcctInOctets, wfUserAccessMaxPassword=wfUserAccessMaxPassword, wfUserAccessNameAudit=wfUserAccessNameAudit, wfUserAccessActiveTable=wfUserAccessActiveTable, wfUserBccLock=wfUserBccLock, wfUserAccessGroupEntry=wfUserAccessGroupEntry, wfUserBccLockPort=wfUserBccLockPort, wfUserAccessMaxLogin=wfUserAccessMaxLogin, wfUserAccessMinLogin=wfUserAccessMinLogin, wfUserAccessActiveCmd=wfUserAccessActiveCmd, wfUserBccLockId=wfUserBccLockId, wfUserAccessGroupName=wfUserAccessGroupName, wfUserAccessActiveLoginAddress=wfUserAccessActiveLoginAddress, wfUserAccessActiveId=wfUserAccessActiveId, wfUserAccessNameId=wfUserAccessNameId, wfUserAuditDelete=wfUserAuditDelete, wfUserAccessActiveAcctOutOctets=wfUserAccessActiveAcctOutOctets, wfUserAccessActiveLastCmdTime=wfUserAccessActiveLastCmdTime, wfUserAccessNameTable=wfUserAccessNameTable, wfUserAccessActiveAcctAccessType=wfUserAccessActiveAcctAccessType, wfUserAccessMinGroup=wfUserAccessMinGroup, wfUserBccConfig=wfUserBccConfig, wfUserBccLockDelete=wfUserBccLockDelete, wfUserAccessRadius=wfUserAccessRadius, wfUserAccessGroupPriv=wfUserAccessGroupPriv, wfUserAccessActiveDisable=wfUserAccessActiveDisable, wfUserAccessActiveState=wfUserAccessActiveState, wfUserAudit=wfUserAudit, wfUserAccessActiveEntry=wfUserAccessActiveEntry, wfUserManagerLock=wfUserManagerLock, wfUserBccLockTimer=wfUserBccLockTimer, wfUserAccessNameDelete=wfUserAccessNameDelete, wfUserAccessGroupDisable=wfUserAccessGroupDisable, wfUserAccessNameDisable=wfUserAccessNameDisable, wfUserBccConfigDelete=wfUserBccConfigDelete, wfUserAccessDelete=wfUserAccessDelete, wfUserAccessActiveAcctPriv=wfUserAccessActiveAcctPriv, wfUserAccess=wfUserAccess, wfUserAccessActiveAcctNasPortType=wfUserAccessActiveAcctNasPortType, wfUserAccessActivePort=wfUserAccessActivePort, wfUserAccessNamePasswd=wfUserAccessNamePasswd, wfUserAccessMaxGroup=wfUserAccessMaxGroup, wfUserAccessActiveDelete=wfUserAccessActiveDelete, wfUserAccessGroupTable=wfUserAccessGroupTable, wfUserAccessGroupAudit=wfUserAccessGroupAudit, wfUserAccessGroupDelete=wfUserAccessGroupDelete, wfUserBccLockAddress=wfUserBccLockAddress, wfUserAccessNameScript=wfUserAccessNameScript, wfUserAuditDisable=wfUserAuditDisable, wfUserAccessActiveLoginTime=wfUserAccessActiveLoginTime, wfUserBccConfigDefaultShell=wfUserBccConfigDefaultShell, wfUserAuditlevel=wfUserAuditlevel, wfUserAccessActiveAcctTermCause=wfUserAccessActiveAcctTermCause, wfUserAccessActiveAcctServiceType=wfUserAccessActiveAcctServiceType, wfUserAccessNameName=wfUserAccessNameName, wfUserAccessRadiusAcctEnable=wfUserAccessRadiusAcctEnable)
