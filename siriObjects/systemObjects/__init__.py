from siriObjects.baseObjects import ClientBoundCommand, AceObject, \
    ServerBoundCommand
import biplist
import struct
import types

##### IOS 6 DUMP

class BaseCommand(AceObject):
    classIdentifier = "BaseCommand"
    groupIdentifier = "com.apple.ace.system"
    def __init__(self, clazz=classIdentifier, group=groupIdentifier, aceId=None, refId=None, plist=None):
        super(BaseCommand, self).__init__(clazz, group)
        if plist == None: # act as a clientBoundCommand
            self.refId = refId
            self.aceId = aceId
            self.callbacks = None
        else:
            self.refId = plist['refId'] if 'refId' in plist else None
            self.aceId = plist['aceId'] if 'aceId' in plist else None
            self.plist = plist
            self.from_plist()

    def to_plist(self):
        self.add_item('refId')
        self.add_item('aceId')
        self.add_property('callbacks')
        return super(BaseCommand, self).to_plist()


class DomainObject(AceObject):
    def __init__(self, group, identifier=None, clazz="Object"): #"DomainObject"
        super(DomainObject, self).__init__(clazz, group)
        self.identifier = None # @"NSURL"
    
    def to_plist(self):
        self.add_property('identifier')
        return super(DomainObject, self).to_plist()


class AceView(AceObject):
    def __init__(self, clazz="AceView", group="com.apple.ace.system"):
        super(AceView, self).__init__(clazz, group)
        self.listenAfterSpeaking = None # @"NSNumber"
        self.speakableText = None # @"NSString"
        self.viewId = None # @"NSString"
    
    def to_plist(self):
        self.add_property('listenAfterSpeaking')
        self.add_property('speakableText')
        self.add_property('viewId')
        return super(AceView, self).to_plist()


class AcknowledgeAlert(ClientBoundCommand):
	def __init__(self, refId):
		super(AcknowledgeAlert, self).__init__("AcknowledgeAlert", "com.apple.ace.system", None, refId)
		self.object = None # @"SADomainObject"
    
    
	def to_plist(self):
		self.add_property('object')
		return super(AcknowledgeAlert, self).to_plist()


class AndCondition(AceObject):
	def __init__(self):
		super(AndCondition, self).__init__("AndCondition", "com.apple.ace.system")
		self.conditions = None # @"NSArray"
    
	def to_plist(self):
		self.add_property('conditions')
		return super(AndCondition, self).to_plist()


class AppInfo(DomainObject):
	def __init__(self):
		super(AppInfo, self).__init__("AppInfo", "com.apple.ace.system")
		self.appId = None # @"NSString"
		self.appName = None # @"NSString"
		self.appNameMap = None # @"NSDictionary"
		self.appVersion = None # @"NSString"
		self.displayAppName = None # @"NSString"
		self.displayAppNameMap = None # @"NSDictionary"
		self.providerName = None # @"NSString"
		self.spotlightName = None # @"NSString"
		self.spotlightNameMap = None # @"NSDictionary"
		self.supportedCommands = None # @"NSArray"
		self.supportedSchemes = None # @"NSArray"
    
	def to_plist(self):
		self.add_property('appId')
		self.add_property('appName')
		self.add_property('appNameMap')
		self.add_property('appVersion')
		self.add_property('displayAppName')
		self.add_property('displayAppNameMap')
		self.add_property('providerName')
		self.add_property('spotlightName')
		self.add_property('spotlightNameMap')
		self.add_property('supportedCommands')
		self.add_property('supportedSchemes')
		return super(AppInfo, self).to_plist()


class AssistantCreated(ClientBoundCommand):
	def __init__(self, refId):
		super(AssistantCreated, self).__init__("AssistantCreated", "com.apple.ace.system", None, refId)
		self.assistantId = None # @"NSString"
		self.speechId = None # @"NSString"
    
    
	def to_plist(self):
		self.add_property('assistantId')
		self.add_property('speechId')
		return super(AssistantCreated, self).to_plist()


class AssistantDestroyed(ClientBoundCommand):
	def __init__(self, refId):
		super(AssistantDestroyed, self).__init__("AssistantDestroyed", "com.apple.ace.system", None, refId)
		self.assistantId = None # @"NSString"
    
    
	def to_plist(self):
		self.add_property('assistantId')
		return super(AssistantDestroyed, self).to_plist()


class AssistantLoaded(ClientBoundCommand):
	def __init__(self, refId):
		super(AssistantLoaded, self).__init__("AssistantLoaded", "com.apple.ace.system", None, refId)
		self.dataAnchor = None # @"NSString"
		self.requestSync = None # @"NSNumber"
		self.syncAnchors = None # @"NSArray"
		self.version = None # @"NSString"
    
    
	def to_plist(self):
		self.add_property('dataAnchor')
		self.add_property('requestSync')
		self.add_property('syncAnchors')
		self.add_property('version')
		return super(AssistantLoaded, self).to_plist()


class AssistantNotFound(ClientBoundCommand):
	def __init__(self, refId):
		super(AssistantNotFound, self).__init__("AssistantNotFound", "com.apple.ace.system", None, refId)
    
    
	def to_plist(self):
		return super(AssistantNotFound, self).to_plist()


class AssistantNotReady(ClientBoundCommand):
	def __init__(self, refId):
		super(AssistantNotReady, self).__init__("AssistantNotReady", "com.apple.ace.system", None, refId)
		self.language = None # @"NSString"
    
    
	def to_plist(self):
		self.add_property('language')
		return super(AssistantNotReady, self).to_plist()


class BackgroundUpdateRequest(ServerBoundCommand):
	classIdentifier = "BackgroundUpdateRequest"
	groupIdentifier = "com.apple.ace.system"
	def __init__(self, plist):
		self.attachment = None # @"<SAAceSerializable>"
		super(BackgroundUpdateRequest, self).__init__(plist)



class BaseClientBoundCommand(ClientBoundCommand):
	def __init__(self, refId):
		super(BaseClientBoundCommand, self).__init__("BaseClientBoundCommand", "com.apple.ace.system", None, refId)
		self.appId = None # @"NSString"
		self.callbacks = None # @"NSArray"
		self.aceId = None # @"NSString"
		self.refId = None # @"NSString"
    
    
	def to_plist(self):
		self.add_property('appId')
		self.add_property('callbacks')
		self.add_property('aceId')
		self.add_property('refId')
		return super(BaseClientBoundCommand, self).to_plist()



class Calendar(AceObject):
	def __init__(self):
		super(Calendar, self).__init__("Calendar", "com.apple.ace.system")
		self.date = None # @"NSDate"
		self.timeZoneId = None # @"NSString"
    
	def to_plist(self):
		self.add_property('date')
		self.add_property('timeZoneId')
		return super(Calendar, self).to_plist()


class CancelRequest(ServerBoundCommand):
	classIdentifier = "CancelRequest"
	groupIdentifier = "com.apple.ace.system"
	def __init__(self, plist):
		self.aceId = None # @"NSString"
		self.refId = None # @"NSString"
		super(CancelRequest, self).__init__(plist)


class CancelSucceeded(ClientBoundCommand):
	def __init__(self, refId):
		super(CancelSucceeded, self).__init__("CancelSucceeded", "com.apple.ace.system", None, refId)
    
    
	def to_plist(self):
		return super(CancelSucceeded, self).to_plist()


class ClearContext(ServerBoundCommand):
	classIdentifier = "ClearContext"
	groupIdentifier = "com.apple.ace.system"
	def __init__(self, plist):
		self.aceId = None # @"NSString"
		self.refId = None # @"NSString"
		super(ClearContext, self).__init__(plist)


class CommandFailed(BaseCommand):
	classIdentifier = "CommandFailed"
	groupIdentifier = "com.apple.ace.system"
	def __init__(self, refId=None, plist=None):
		self.errorCode = None # i
		self.reason = None # @"NSString"
		self.appId = None # @"NSString"
		super(CommandFailed, self).__init__(clazz=CommandFailed.classIdentifier, group=CommandFailed.groupIdentifier, aceId=None, refId=refId, plist=plist)
    
	def to_plist(self):
		self.add_property("errorCode")
		self.add_property("reason")
		self.add_property("appId")
		return super(CommandFailed, self).to_plist()


class CommandIgnored(ServerBoundCommand):
	classIdentifier = "CommandIgnored"
	groupIdentifier = "com.apple.ace.system"
	def __init__(self, plist):
		self.aceId = None # @"NSString"
		self.refId = None # @"NSString"
		super(CommandIgnored, self).__init__(plist)


class CommandSucceeded(ServerBoundCommand):
	classIdentifier = "CommandSucceeded"
	groupIdentifier = "com.apple.ace.system"
	def __init__(self, plist):
		self.aceId = None # @"NSString"
		self.refId = None # @"NSString"
		super(CommandSucceeded, self).__init__(plist)


class CommandSupport(AceObject):
	def __init__(self):
		super(CommandSupport, self).__init__("CommandSupport", "com.apple.ace.system")
		self.aceVersion = None # @"NSString"
		self.commandId = None # @"NSString"
		self.resultSupport = None # @"SAObjectSupport"
		self.serverEndpoint = None # @"NSURL"
		self.supportedConstraints = None # @"NSArray"
		self.weight = None # i
    
	def to_plist(self):
		self.add_property('aceVersion')
		self.add_property('commandId')
		self.add_property('resultSupport')
		self.add_property('serverEndpoint')
		self.add_property('supportedConstraints')
		self.add_property('weight')
		return super(CommandSupport, self).to_plist()


class ConstraintSupport(AceObject):
	def __init__(self):
		super(ConstraintSupport, self).__init__("ConstraintSupport", "com.apple.ace.system")
		self.condition = None # @"<SASupportCondition>"
		self.property = None # @"NSString"
    
	def to_plist(self):
		self.add_property('condition')
		self.add_property('property')
		return super(ConstraintSupport, self).to_plist()


class CreateAssistant(ServerBoundCommand):
	classIdentifier = "CreateAssistant"
	groupIdentifier = "com.apple.ace.system"
	def __init__(self, plist):
		self.activationToken = None # @"NSData"
		self.connectionType = None # @"NSString"
		self.language = None # @"NSString"
		self.validationData = None # @"NSData"
		super(CreateAssistant, self).__init__(plist)


class CreateSessionInfoRequest(ServerBoundCommand):
	classIdentifier = "CreateSessionInfoRequest"
	groupIdentifier = "com.apple.ace.system"
	def __init__(self, plist):
		self.sessionInfoRequest = None # @"NSData"
		super(CreateSessionInfoRequest, self).__init__(plist)


class CreateSessionInfoResponse(ClientBoundCommand):
	def __init__(self, refId):
		super(CreateSessionInfoResponse, self).__init__("CreateSessionInfoResponse", "com.apple.ace.system", None, refId)
		self.sessionInfo = None # @"NSData"
		self.validityDuration = None # @"NSNumber"
    
    
	def to_plist(self):
		self.add_property('sessionInfo')
		self.add_property('validityDuration')
		return super(CreateSessionInfoResponse, self).to_plist()


class DeferredObject(AceObject):
	def __init__(self):
		super(DeferredObject, self).__init__("DeferredObject", "com.apple.ace.system")
		self.identifier = None # @"NSURL"
    
	def to_plist(self):
		self.add_property('identifier')
		return super(DeferredObject, self).to_plist()


class DestroyAssistant(ServerBoundCommand):
	classIdentifier = "DestroyAssistant"
	groupIdentifier = "com.apple.ace.system"
	def __init__(self, plist):
		self.assistantId = None # @"NSString"
		self.speechId = None # @"NSString"
		super(DestroyAssistant, self).__init__(plist)


class Distance(AceObject):
	def __init__(self):
		super(Distance, self).__init__("Distance", "com.apple.ace.system")
		self.unit = None # @"NSString"
		self.units = None # @"NSString"
		self.value = None # @"NSNumber"
    
	def to_plist(self):
		self.add_property('unit')
		self.add_property('units')
		self.add_property('value')
		return super(Distance, self).to_plist()



class DomainObjectCancel(ClientBoundCommand):
    def __init__(self, refId, identifier=None):
        super(DomainObjectCancel, self).__init__("DomainObjectCancel", "com.apple.ace.system", None, refId)
        self.identifier = identifier # @"SADomainObject"
    
    def to_plist(self):
        self.add_property('identifier')
        return super(DomainObjectCancel, self).to_plist()


class DomainObjectCancelCompleted(ServerBoundCommand):
    classIdentifier = "DomainObjectCancelCompleted"
    groupIdentifier = "com.apple.ace.system"
    def __init__(self, plist):
        super(DomainObjectCancelCompleted, self).__init__(plist)


class DomainObjectCommit(ClientBoundCommand):
    def __init__(self, refId, identifier=None):
        super(DomainObjectCommit, self).__init__("DomainObjectCommit", "com.apple.ace.system", None, refId)
        self.identifier = identifier # @"SADomainObject"
    
    def to_plist(self):
        self.add_property('identifier')
        return super(DomainObjectCommit, self).to_plist()


class DomainObjectCommitCompleted(ServerBoundCommand):
    classIdentifier = "DomainObjectCommitCompleted"
    groupIdentifier = "com.apple.ace.system"
    def __init__(self, plist):
        self.identifier = None # @"NSURL"
        super(DomainObjectCommitCompleted, self).__init__(plist)


class DomainObjectCreate(ClientBoundCommand):
    def __init__(self, refId, obj=None):
        super(DomainObjectCreate, self).__init__("DomainObjectCreate", "com.apple.ace.system", None, refId)
        self.targetAppId = None # @"NSURL"
        self.object = obj # @"SADomainObject"
    
    
    def to_plist(self):
        self.add_property('targetAppId')
        self.add_property('object')
        return super(DomainObjectCreate, self).to_plist()


class DomainObjectCreateCompleted(ServerBoundCommand):
    classIdentifier = "DomainObjectCreateCompleted"
    groupIdentifier = "com.apple.ace.system"
    def __init__(self, plist):
        self.identifier = None # @"NSURL"
        super(DomainObjectCreateCompleted, self).__init__(plist)


class DomainObjectDelete(ClientBoundCommand):
    def __init__(self, refId):
        super(DomainObjectDelete, self).__init__("DomainObjectDelete", "com.apple.ace.system", None, refId)
        self.identifier = None # @"SADomainObject"
    
    def to_plist(self):
        self.add_property('identifier')
        return super(DomainObjectDelete, self).to_plist()


class DomainObjectDeleteCompleted(ServerBoundCommand):
    classIdentifier = "DomainObjectDeleteCompleted"
    groupIdentifier = "com.apple.ace.system"
    def __init__(self, plist):
        super(DomainObjectDeleteCompleted, self).__init__(plist)

class DomainObjectRetrieve(ClientBoundCommand):
    def __init__(self, refId, identifiers=None):
        super(DomainObjectRetrieve, self).__init__("DomainObjectRetrieve", "com.apple.ace.system", None, refId)
        self.identifiers = identifiers # @"NSArray"
    
    def to_plist(self):
        self.add_property('identifiers')
        return super(DomainObjectRetrieve, self).to_plist()

class DomainObjectRetrieveCompleted(ServerBoundCommand):
    classIdentifier = "DomainObjectRetrieveCompleted"
    groupIdentifier = "com.apple.ace.system"
    def __init__(self, plist):
        self.objects = None # @"NSArray"
        super(DomainObjectRetrieveCompleted, self).__init__(plist)


class DomainObjectUpdate(ClientBoundCommand):
    def __init__(self, refId, identifier=None, addFields=None, setFields=None, removeFields=None):
        super(DomainObjectUpdate, self).__init__("DomainObjectUpdate", "com.apple.ace.system", None, refId)
        self.addFields = addFields # @"SADomainObject"
        self.identifier = identifier # @"SADomainObject"
        self.removeFields = removeFields # @"SADomainObject"
        self.setFields = setFields # @"SADomainObject"
    
    
    def to_plist(self):
        self.add_property('addFields')
        self.add_property('identifier')
        self.add_property('removeFields')
        self.add_property('setFields')
        return super(DomainObjectUpdate, self).to_plist()


class DomainObjectUpdateCompleted(ServerBoundCommand):
    classIdentifier = "DomainObjectUpdateCompleted"
    groupIdentifier = "com.apple.ace.system"
    def __init__(self, plist):
        self.identifier = None # @"NSURL"
        super(DomainObjectUpdateCompleted, self).__init__(plist)



class Duration(AceObject):
	def __init__(self):
		super(Duration, self).__init__("Duration", "com.apple.ace.system")
		self.unit = None # @"NSString"
		self.units = None # @"NSString"
		self.value = None # @"NSNumber"
    
	def to_plist(self):
		self.add_property('unit')
		self.add_property('units')
		self.add_property('value')
		return super(Duration, self).to_plist()


class Email(AceObject):
    def __init__(self, group="com.apple.ace.system"):
        super(Email, self).__init__("Email", group)
        self.emailAddress = None # @"NSString"
        self.favoriteFacetime = None # @"NSNumber"
        self.label = None # @"NSString"
    
	def to_plist(self):
		self.add_property('emailAddress')
		self.add_property('favoriteFacetime')
		self.add_property('label')
		return super(Email, self).to_plist()

class EntryPoint(AceObject):
	def __init__(self):
		super(EntryPoint, self).__init__("EntryPoint", "com.apple.ace.system")
		self.latitude = None # @"NSNumber"
		self.longitude = None # @"NSNumber"
    
	def to_plist(self):
		self.add_property('latitude')
		self.add_property('longitude')
		return super(EntryPoint, self).to_plist()


class FalseCondition(AceObject):
	def __init__(self):
		super(FalseCondition, self).__init__("FalseCondition", "com.apple.ace.system")
    
	def to_plist(self):
		return super(FalseCondition, self).to_plist()


class GetAssistantData(ClientBoundCommand):
	def __init__(self, refId):
		super(GetAssistantData, self).__init__("GetAssistantData", "com.apple.ace.system", None, refId)
    
    
	def to_plist(self):
		return super(GetAssistantData, self).to_plist()


class GetDeferredObject(ServerBoundCommand):
	classIdentifier = "GetDeferredObject"
	groupIdentifier = "com.apple.ace.system"
	def __init__(self, plist):
		self.identifier = None # @"NSURL"
		self.aceId = None # @"NSString"
		self.refId = None # @"NSString"
		super(GetDeferredObject, self).__init__(plist)


class GetDeferredObjectResponse(ClientBoundCommand):
	def __init__(self, refId):
		super(GetDeferredObjectResponse, self).__init__("GetDeferredObjectResponse", "com.apple.ace.system", None, refId)
		self.object = None # @"<SAAceSerializable>"
    
    
	def to_plist(self):
		self.add_property('object')
		return super(GetDeferredObjectResponse, self).to_plist()

class GetRequestOrigin(ClientBoundCommand):
    desiredAccuracyThreeKilometers = "ThreeKilometers"
    desiredAccuracyKilometer = "Kilometer"
    desiredAccuracyHundredMeters = "HundredMeters"
    desiredAccuracyNearestTenMeters = "NearestTenMeters"
    desiredAccuracyBest = "Best"
    
    def __init__(self, refId, desiredAccuracy=desiredAccuracyHundredMeters, maxAge=None, searchTimeout=8.0):
        super(GetRequestOrigin, self).__init__("GetRequestOrigin", "com.apple.ace.system", None, refId)
        self.desiredAccuracy = desiredAccuracy # @"NSString"
        self.maxAge = maxAge # @"NSNumber"
        self.searchTimeout = searchTimeout # @"NSNumber"
    
    
    def to_plist(self):
        self.add_property('desiredAccuracy')
        self.add_property('maxAge')
        self.add_property('searchTimeout')
        return super(GetRequestOrigin, self).to_plist()


class GetSessionCertificate(ServerBoundCommand):
	classIdentifier = "GetSessionCertificate"
	groupIdentifier = "com.apple.ace.system"
	def __init__(self, plist):
		self.aceId = None # @"NSString"
		self.refId = None # @"NSString"
		super(GetSessionCertificate, self).__init__(plist)


class GetSessionCertificateResponse(ClientBoundCommand):
    def __init__(self, refId, caCert, sessionCert):
        super(GetSessionCertificateResponse, self).__init__("GetSessionCertificateResponse", "com.apple.ace.system", None, refId)
        self.certificate = None # NSData
        self.caCert = caCert
        self.sessionCert = sessionCert
    
    def to_plist(self):
        self.certificate = biplist.Data("\x01\x02"+struct.pack(">I", len(self.caCert))+self.caCert + struct.pack(">I", len(self.sessionCert))+self.sessionCert)
        self.add_property('certificate')
        return super(GetSessionCertificateResponse, self).to_plist()



class GetSupportedLocales(ServerBoundCommand):
	classIdentifier = "GetSupportedLocales"
	groupIdentifier = "com.apple.ace.system"
	def __init__(self, plist):
		super(GetSupportedLocales, self).__init__(plist)


class LoadAssistant(ServerBoundCommand):
	classIdentifier = "LoadAssistant"
	groupIdentifier = "com.apple.ace.system"
	def __init__(self, plist):
		self.activationToken = None # @"NSData"
		self.assistantId = None # @"NSString"
		self.connectionType = None # @"NSString"
		self.language = None # @"NSString"
		self.sessionValidationData = None # @"NSData"
		self.speechId = None # @"NSString"
		super(LoadAssistant, self).__init__(plist)


class Location(DomainObject):
    AccuracyBestValue = "Best"
    AccuracyNearestTenMetersValue = "NearestTenMeters"
    AccuracyHundredMetersValue = "HundredMeters"
    AccuracyKilometerValue = "Kilometer"
    AccuracyThreeKilometersValue = "ThreeKilometers"
    
    def __init__(self, label=None, street=None, city=None, stateCode=None, countryCode=None, postalCode=None, latitude=None, longitude=None, accuracy=None, group="com.apple.ace.system", clazz="Location"):
        super(Location, self).__init__(group, None, clazz)
        self.accuracy = None # @"NSNumber"
        self.city = None # @"NSString"
        self.countryCode = None # @"NSString"
        self.entryPoints = None # @"NSArray"
        self.label = None # @"NSString"
        self.latitude = None # @"NSNumber"
        self.longitude = None # @"NSNumber"
        self.postalCode = None # @"NSString"
        self.regionType = None # @"NSString"
        self.relativeDistance = None # @"SADistance"
        self.stateCode = None # @"NSString"
        self.street = None # @"NSString"
        self.subThoroughfare = None # @"NSString"
        self.thoroughfare = None # @"NSString"
        self.timezoneId = None # @"NSString"
    
    def to_plist(self):
		self.add_property('accuracy')
		self.add_property('city')
		self.add_property('countryCode')
		self.add_property('entryPoints')
		self.add_property('label')
		self.add_property('latitude')
		self.add_property('longitude')
		self.add_property('postalCode')
		self.add_property('regionType')
		self.add_property('relativeDistance')
		self.add_property('stateCode')
		self.add_property('street')
		self.add_property('subThoroughfare')
		self.add_property('thoroughfare')
		self.add_property('timezoneId')
		return super(Location, self).to_plist()



class Metrics(ServerBoundCommand):
	classIdentifier = "Metrics"
	groupIdentifier = "com.apple.ace.system"
	def __init__(self, plist):
		self.category = None # @"NSString"
		self.timings = None # @"NSDictionary"
		self.aceId = None # @"NSString"
		self.refId = None # @"NSString"
		super(Metrics, self).__init__(plist)

class NavStatus(AceObject):
	def __init__(self):
		super(NavStatus, self).__init__("NavStatus", "com.apple.ace.system")
		self.statusValue = None # @"NSString"
    
	def to_plist(self):
		self.add_property('statusValue')
		return super(NavStatus, self).to_plist()

class OrCondition(AceObject):
	def __init__(self):
		super(OrCondition, self).__init__("OrCondition", "com.apple.ace.system")
		self.conditions = None # @"NSArray"
    
	def to_plist(self):
		self.add_property('conditions')
		return super(OrCondition, self).to_plist()

class Person(DomainObject):
    def __init__(self, group="com.apple.ace.system"):
        super(Person, self).__init__(group, None, "Person")
        self.addresses = None # @"NSArray"
        self.birthday = None # @"NSDate"
        self.company = None # @"NSString"
        self.emails = None # @"NSArray"
        self.firstName = None # @"NSString"
        self.firstNamePhonetic = None # @"NSString"
        self.fullName = None # @"NSString"
        self.lastName = None # @"NSString"
        self.lastNamePhonetic = None # @"NSString"
        self.me = None # @"NSNumber"
        self.middleName = None # @"NSString"
        self.nickName = None # @"NSString"
        self.phones = None # @"NSArray"
        self.prefix = None # @"NSString"
        self.relatedNames = None # @"NSArray"
        self.socialProfiles = None # @"NSArray"
        self.suffix = None # @"NSString"
    
    def to_plist(self):
        self.add_property('addresses')
        self.add_property('birthday')
        self.add_property('company')
        self.add_property('emails')
        self.add_property('firstName')
        self.add_property('firstNamePhonetic')
        self.add_property('fullName')
        self.add_property('lastName')
        self.add_property('lastNamePhonetic')
        self.add_property('me')
        self.add_property('middleName')
        self.add_property('nickName')
        self.add_property('phones')
        self.add_property('prefix')
        self.add_property('relatedNames')
        self.add_property('socialProfiles')
        self.add_property('suffix')
        return super(Person, self).to_plist()


class PersonAttribute(AceObject):
    def __init__(self, obj=None, data=None, displayText=None):
        super(PersonAttribute, self).__init__("PersonAttribute", "com.apple.ace.system")
        self.data = data # @"NSString"
        self.displayText = displayText # @"NSString"
        self.object = obj # @"SAPerson"
    
    def to_plist(self):
        self.add_property('data')
        self.add_property('displayText')
        self.add_property('object')
        return super(PersonAttribute, self).to_plist()


class Phone(AceObject):
    def __init__(self, number=None, label=None, favoriteVoice=None, favoriteFacetime=None, group="com.apple.ace.system"):
        super(Phone, self).__init__("Phone", group)
        self.favoriteFacetime = favoriteFacetime # @"NSNumber"
        self.favoriteVoice = favoriteVoice # @"NSNumber"
        self.label = label # @"NSString"
        self.number = number # @"NSString"
    
    def to_plist(self):
        self.add_property('favoriteFacetime')
        self.add_property('favoriteVoice')
        self.add_property('label')
        self.add_property('number')
        return super(Phone, self).to_plist()




class Ping(ServerBoundCommand):
	classIdentifier = "Ping"
	groupIdentifier = "com.apple.ace.system"
	def __init__(self, plist):
		super(Ping, self).__init__(plist)

class Pong(ServerBoundCommand):
	classIdentifier = "Pong"
	groupIdentifier = "com.apple.ace.system"
	def __init__(self, plist):
		super(Pong, self).__init__(plist)

class RelatedName(AceObject):
    def __init__(self, name=None, label=None, group="com.apple.ace.system"):
        super(RelatedName, self).__init__("RelatedName", group)
        self.label = label # @"NSString"
        self.name = name # @"NSString"
    
    def to_plist(self):
        self.add_property('label')
        self.add_property('name')
        return super(RelatedName, self).to_plist()


class RequestCompleted(ClientBoundCommand):
	def __init__(self, refId):
		super(RequestCompleted, self).__init__("RequestCompleted", "com.apple.ace.system", None, refId)
    
    
	def to_plist(self):
		return super(RequestCompleted, self).to_plist()


class ResultCallback(AceObject):
    def __init__(self, commands=None, code=0):
        super(ResultCallback, self).__init__("ResultCallback", "com.apple.ace.system")
        self.code = code # i
        self.commands = commands # @"NSArray"
    
    def to_plist(self):
        self.add_property('code')
        self.add_property('commands')
        return super(ResultCallback, self).to_plist()


class RollbackRequest(ServerBoundCommand):
	classIdentifier = "RollbackRequest"
	groupIdentifier = "com.apple.ace.system"
	def __init__(self, plist):
		self.requestId = None # @"NSString"
		super(RollbackRequest, self).__init__(plist)


class RollbackSucceeded(ClientBoundCommand):
	def __init__(self, refId):
		super(RollbackSucceeded, self).__init__("RollbackSucceeded", "com.apple.ace.system", None, refId)
    
    
	def to_plist(self):
		return super(RollbackSucceeded, self).to_plist()


class SendCommands(ClientBoundCommand):
    def __init__(self, commands=None): # this is backwarts compatibility
        super(SendCommands, self).__init__("SendCommands", "com.apple.ace.system", None, "")
        self.commands = commands # @"NSArray"
    
    def to_plist(self):
        self.add_property('commands')
        return super(SendCommands, self).to_plist()


class SessionValidationFailed(ClientBoundCommand):
	def __init__(self, refId):
		super(SessionValidationFailed, self).__init__("SessionValidationFailed", "com.apple.ace.system", None, refId)
		self.errorCode = None # @"NSString"
    
    
	def to_plist(self):
		self.add_property('errorCode')
		return super(SessionValidationFailed, self).to_plist()


class SetActivationToken(ClientBoundCommand):
	def __init__(self, refId):
		super(SetActivationToken, self).__init__("SetActivationToken", "com.apple.ace.system", None, refId)
		self.activationToken = None # @"NSData"
		self.language = None # @"NSString"
    
    
	def to_plist(self):
		self.add_property('activationToken')
		self.add_property('language')
		return super(SetActivationToken, self).to_plist()


class SetAlertContext(ServerBoundCommand):
	classIdentifier = "SetAlertContext"
	groupIdentifier = "com.apple.ace.system"
	def __init__(self, plist):
		self.context = None # @"NSArray"
		super(SetAlertContext, self).__init__(plist)


class SetApplicationContext(ServerBoundCommand):
	classIdentifier = "SetApplicationContext"
	groupIdentifier = "com.apple.ace.system"
	def __init__(self, plist):
		self.orderedContext = None # @"NSArray"
		super(SetApplicationContext, self).__init__(plist)


class SetAssistantData(ServerBoundCommand):
	classIdentifier = "SetAssistantData"
	groupIdentifier = "com.apple.ace.system"
	def __init__(self, plist):
		self.abSources = None # @"NSArray"
		self.anchor = None # @"NSString"
		self.censorSpeech = None # c
		self.countryCode = None # @"NSString"
		self.debugFlags = None # @"NSNumber"
		self.deviceCapabilities = None # @"NSArray"
		self.deviceVersion = None # @"NSString"
		self.firstName = None # @"NSString"
		self.handsFree = None # c
		self.lastName = None # @"NSString"
		self.meCards = None # @"NSArray"
		self.osVersion = None # @"NSString"
		self.parentalRestrictions = None # @"NSArray"
		self.region = None # @"NSString"
		self.storefront = None # @"NSNumber"
		self.temperatureUnit = None # @"NSString"
		self.timeZoneId = None # @"NSString"
		self.twentyFourHourTimeDisplay = None # @"NSNumber"
		self.uiScale = None # @"NSNumber"
		self.aceId = None # @"NSString"
		self.refId = None # @"NSString"
		super(SetAssistantData, self).__init__(plist)


class SetConnectionHeader(ClientBoundCommand):
	def __init__(self, refId):
		super(SetConnectionHeader, self).__init__("SetConnectionHeader", "com.apple.ace.system", None, refId)
		self.aceHostHeader = None # @"NSString"
		self.reconnectNow = None # c
    
    
	def to_plist(self):
		self.add_property('aceHostHeader')
		self.add_property('reconnectNow')
		return super(SetConnectionHeader, self).to_plist()

class SetRequestOrigin(ServerBoundCommand):
	classIdentifier = "SetRequestOrigin"
	groupIdentifier = "com.apple.ace.system"
    
	statusValid = "Valid"
	statusTimeout = "Timeout"
	statusUnknown = "Unknown"
	statusDenied = "Denied"
	statusDisabled = "Disabled"
        
	def __init__(self, plist):
		self.latitude = None # d
		self.longitude = None # d
		self.verticalAccuracy = None # d
		self.horizontalAccuracy = None # d
		self.age = None # @"NSNumber"
		self.altitude = None # d
		self.desiredAccuracy = None # @"NSString"
		self.direction = None # d
		self.speed = None # d
		self.status = None # @"NSString"
		self.timestamp = None # @"NSDate"
		self.aceId = None # @"NSString"
		self.refId = None # @"NSString"
		super(SetRequestOrigin, self).__init__(plist)


class SetRestrictions(ServerBoundCommand):
	classIdentifier = "SetRestrictions"
	groupIdentifier = "com.apple.ace.system"
	def __init__(self, plist):
		self.restrictions = None # @"NSArray"
		super(SetRestrictions, self).__init__(plist)


class SetSessionObjects(ServerBoundCommand):
	classIdentifier = "SetSessionObjects"
	groupIdentifier = "com.apple.ace.system"
	def __init__(self, plist):
		self.objects = None # @"NSArray"
		super(SetSessionObjects, self).__init__(plist)


class SetSupportedLocales(ClientBoundCommand):
	def __init__(self, refId):
		super(SetSupportedLocales, self).__init__("SetSupportedLocales", "com.apple.ace.system", None, refId)
		self.locales = None # @"NSArray"
    
    
	def to_plist(self):
		self.add_property('locales')
		return super(SetSupportedLocales, self).to_plist()


class SocialProfile(AceObject):
	def __init__(self):
		super(SocialProfile, self).__init__("SocialProfile", "com.apple.ace.system")
		self.serviceType = None # @"NSString"
		self.url = None # @"NSString"
		self.userName = None # @"NSString"
    
	def to_plist(self):
		self.add_property('serviceType')
		self.add_property('url')
		self.add_property('userName')
		return super(SocialProfile, self).to_plist()


class Source(DomainObject):
	def __init__(self):
		super(Source, self).__init__("Source", "com.apple.ace.system")
		self.accountIdentifier = None # @"NSString"
		self.accountName = None # @"NSString"
		self.domainIdentifier = None # @"NSString"
		self.remote = None # @"NSNumber"
    
	def to_plist(self):
		self.add_property('accountIdentifier')
		self.add_property('accountName')
		self.add_property('domainIdentifier')
		self.add_property('remote')
		return super(Source, self).to_plist()

# this is kind of a special case
class StartRequest(BaseCommand):
    classIdentifier = "StartRequest"
    groupIdentifier = "com.apple.ace.system"
    def __init__(self, *args, **kwargs):
        plist = None
        print "START REQUEST"
        if len(args) == 1:
            # lets test if it is a plist
            if isinstance(args[0], types.DictionaryType):
                plist = args[0]
            elif isinstance(args[0], types.StringType):
                kwargs = dict()
                kwargs['handsFree'] = False
                kwargs['utterance'] = args[0]
        
        if len(args) == 2:
            kwargs = dict()
            kwargs['handsFree'] = args[0]
            kwargs['utterance'] = args[1]
        
        self.eyesFree = kwargs['eyesFree'] if 'eyesFree' in kwargs else None # c
        self.handsFree = kwargs['handsFree'] if 'handsFree' in kwargs else None # bool
        self.motionActivity = kwargs['motionActivity'] if 'motionActivity' in kwargs else None # @"NSString"
        self.motionConfidence = kwargs['motionConfidence'] if 'motionConfidence' in kwargs else None # @"NSNumber"
        self.origin = kwargs['origin'] if 'origin' in kwargs else None # @"NSString"
        self.utterance = kwargs['utterance'] if 'utterance' in kwargs else None # @"NSString"
        super(StartRequest, self).__init__(clazz=StartRequest.classIdentifier, group=StartRequest.groupIdentifier, aceId=None, refId=None, plist=plist)
    
    def to_plist(self):
        self.add_property('eyesFree')
        self.add_property('handsFree')
        self.add_property('motionActivity')
        self.add_property('motionConfidence')
        self.add_property('origin')
        self.add_property('utterance')
        return super(StartRequest, self).to_plist()


class TrueCondition(AceObject):
	def __init__(self):
		super(TrueCondition, self).__init__("TrueCondition", "com.apple.ace.system")
    
	def to_plist(self):
		return super(TrueCondition, self).to_plist()

class ValueCondition(AceObject):
	def __init__(self):
		super(ValueCondition, self).__init__("ValueCondition", "com.apple.ace.system")
		self.legalValues = None # @"NSArray"
    
	def to_plist(self):
		self.add_property('legalValues')
		return super(ValueCondition, self).to_plist()



# this was not included in iOS 6 anymore leave it for backwarts compatibility

class GetRequestOriginFailed(ServerBoundCommand):
    classIdentifier = "GetRequestOriginFailed"
    groupIdentifier = "com.apple.ace.system"
    def __init__(self, plist):
        self.cause = None # @"NSString"
        super(GetRequestOriginFailed, self).__init__(plist)