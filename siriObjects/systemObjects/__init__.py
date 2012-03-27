from siriObjects.baseObjects import ClientBoundCommand, AceObject, ServerBoundCommand

import biplist, struct

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

class GetRequestOrigin(ClientBoundCommand):
    desiredAccuracyThreeKilometers = "ThreeKilometers"
    desiredAccuracyKilometer = "Kilometer"
    desiredAccuracyHundredMeters = "HundredMeters"
    desiredAccuracyNearestTenMeters = "NearestTenMeters"
    desiredAccuracyBest = "Best"
    
    def __init__(self, refId, desiredAccuracy=desiredAccuracyHundredMeters, maxAge=None, searchTimeout=8.0):
        super(GetRequestOrigin, self).__init__("GetRequestOrigin", "com.apple.ace.system", None, refId)
        self.desiredAccuracy = desiredAccuracy
        self.searchTimeout = searchTimeout
        self.maxAge = maxAge
    
    def to_plist(self):
        self.add_property('desiredAccuracy')
        self.add_property('searchTimeout')
        self.add_property('maxAge')
        return super(GetRequestOrigin, self).to_plist()

class SetRequestOrigin(ServerBoundCommand):
    statusValid = "Valid"
    statusTimeout = "Timeout"
    statusUnknown = "Unknown"
    statusDenied = "Denied"
    statusDisabled = "Disabled"
    def __init__(self, plist):
        self.aceId = None
        self.refId = None
        self.timestamp = None
        self.status = None
        self.speed = None
        self.direction = None
        self.desiredAccuracy = None
        self.altitude = None
        self.age = None
        self.horizontalAccuracy = None
        self.verticalAccuracy = None
        self.longitude = None
        self.latitude = None
        super(SetRequestOrigin, self).__init__(plist)


class DomainObject(AceObject):
    def __init__(self, group, identifier=None, clazz="Object"):
        super(DomainObject, self).__init__(clazz, group)
        self.identifier = identifier
    
    def to_plist(self):
        self.add_property('identifier')
        return super(DomainObject, self).to_plist()

class DomainObjectCreate(ClientBoundCommand):
    def __init__(self, refId, obj=None):
        super(DomainObjectCreate, self).__init__("DomainObjectCreate", "com.apple.ace.system", None, refId)
        self.object = obj
    
    def to_plist(self):
        self.add_property('object')
        return super(DomainObjectCreate, self).to_plist()

class DomainObjectCreateCompleted(ServerBoundCommand):
    classIdentifier = "DomainObjectCreateCompleted"
    groupIdentifier = "com.apple.ace.system"

    def __init__(self, plist):
        self.identifier = None #string
        super(DomainObjectCreateCompleted, self).__init__(plist)
        
class DomainObjectRetrieve(ClientBoundCommand):
    def __init__(self, refId, identifiers=None):
        super(DomainObjectRetrieve, self).__init__("DomainObjectRetrieve", "com.apple.ace.system", None, refId)
        self.identifiers = identifiers if identifiers != None else []
    
    def to_plist(self):
        self.add_property('identifiers')
        return super(DomainObjectRetrieve, self).to_plist()

class DomainObjectRetrieveCompleted(ServerBoundCommand):
    classIdentifier = "DomainObjectRetrieveCompleted"
    groupIdentifier = "com.apple.ace.system"

    def __init__(self, plist):
        self.objects = [] #array
        super(DomainObjectRetrieveCompleted, self).__init__(plist)
        
        
class DomainObjectUpdate(ClientBoundCommand):
    def __init__(self, refId, identifier=None, addFields=None, setFields=None, removeFields=None):
        super(DomainObjectUpdate, self).__init__("DomainObjectUpdate", "com.apple.ace.system", None, refId)
        self.identifier = identifier
        self.addFields = addFields
        self.setFields = setFields
        self.removeFields = removeFields
        
    def to_plist(self):
        self.add_property('identifier')
        self.add_property('addFields')
        self.add_property('setFields')
        self.add_property('removeFields')
        return super(DomainObjectUpdate, self).to_plist()

class DomainObjectUpdateCompleted(ServerBoundCommand):
    classIdentifier = "DomainObjectUpdateCompleted"
    groupIdentifier = "com.apple.ace.system"

    def __init__(self, plist):
        self.identifier = None #string
        super(DomainObjectUpdateCompleted, self).__init__(plist)

class DomainObjectCommit(ClientBoundCommand):
    def __init__(self, refId, identifier=None):
        super(DomainObjectCommit, self).__init__("DomainObjectCommit", "com.apple.ace.system", None, refId)
        self.identifier = identifier
    
    def to_plist(self):
        self.add_property('identifier')
        return super(DomainObjectCommit, self).to_plist()
    
class DomainObjectCommitCompleted(ServerBoundCommand):
    classIdentifier = "DomainObjectCommitCompleted"
    groupIdentifier = "com.apple.ace.system"

    def __init__(self, plist):
        self.identifier = None #string
        super(DomainObjectCommitCompleted, self).__init__(plist)
        
class DomainObjectCancel(ClientBoundCommand):
    def __init__(self, refId, identifier=None):
        super(DomainObjectCancel, self).__init__("DomainObjectCancel", "com.apple.ace.system", None, refId)
        self.identifier = identifier
    
    def to_plist(self):
        self.add_property('identifier')
        return super(DomainObjectCancel, self).to_plist()
    
class DomainObjectCancelCompleted(ServerBoundCommand):
    classIdentifier = "DomainObjectCancelCompleted"
    groupIdentifier = "com.apple.ace.system"

    def __init__(self, plist):
        self.identifier = None #string
        super(DomainObjectCancelCompleted, self).__init__(plist)
        
        
class DomainObjectDelete(ClientBoundCommand):
    def __init__(self, refId, identifier=None):
        super(DomainObjectDelete, self).__init__("DomainObjectDelete", "com.apple.ace.system", None, refId)
        self.identifier = identifier
    
    def to_plist(self):
        self.add_property('identifier')
        return super(DomainObjectDelete, self).to_plist()
    
class DomainObjectDeleteCompleted(ServerBoundCommand):
    classIdentifier = "DomainObjectDeleteCompleted"
    groupIdentifier = "com.apple.ace.system"

    def __init__(self, plist):
        self.identifier = None #string
        super(DomainObjectDeleteCompleted, self).__init__(plist)

class StartRequest(AceObject):
    def __init__(self, handsFree=False, utterance=""):
        super(StartRequest, self).__init__("StartRequest", "com.apple.ace.system")
        self.handsFree = handsFree
        self.utterance = utterance

    def to_plist(self):
        self.add_property('handsFree')
        self.add_property('utterance')
        return super(StartRequest, self).to_plist()

class ResultCallback(AceObject):
    def __init__(self, commands=None, code=0):
        super(ResultCallback, self).__init__("ResultCallback", "com.apple.ace.system")
        self.commands = commands if commands != None else []
        self.code = code

    def to_plist(self):
        self.add_property('commands')
        self.add_property('code')
        return super(ResultCallback, self).to_plist()


class SendCommands(AceObject):
    def __init__(self, commands=None):
        super(SendCommands, self).__init__("SendCommands", "com.apple.ace.system")
        self.commands = commands if commands != None else []
    
    def to_plist(self):
        self.add_property('commands')
        return super(SendCommands, self).to_plist()

class Person(DomainObject):
    def __init__(self, group="com.apple.ace.system"):
        super(Person, self).__init__(group, clazz="Person")
        self.suffix = None # string
        self.relatedNames = None # array
        self.prefix = None # string
        self.phones = None # array
        self.nickName = None # string
        self.middleName = None # string
        self.me = None # number
        self.lastNamePhonetic = None # string
        self.lastName = None # string
        self.fullName = None # string
        self.firstNamePhonetic = None # string
        self.firstName = None # string
        self.emails = None # array
        self.compary = None # string
        self.birthday = None # date
        self.addresses = None # array

    def to_plist(self):
        self.add_property('suffix')
        self.add_property('relatedNames')
        self.add_property('prefix')
        self.add_property('phones')
        self.add_property('nickName')
        self.add_property('middleName')
        self.add_property('me')
        self.add_property('lastNamePhonetic')
        self.add_property('lastName')
        self.add_property('fullName')
        self.add_property('firstNamePhonetic')
        self.add_property('firstName')
        self.add_property('emails')
        self.add_property('compary')
        self.add_property('birthday')
        self.add_property('addresses')
        return super(Person, self).to_plist()

class PersonAttribute(AceObject):
    def __init__(self, obj=None, displayText="", data=""):
        super(PersonAttribute, self).__init__("PersonAttribute", "com.apple.ace.system")
        self.object = obj if obj != None else Person()
        self.displayText = ""
        self.data = ""
    
    def to_plist(self):
        self.add_property('object')
        self.add_property('displayText')
        self.add_property('data')
        return super(PersonAttribute, self).to_plist()

class Phone(AceObject):
    def __init__(self, number=None, label=None, favoriteVoice=None, favoriteFacetime=None, group="com.apple.ace.system"):
        super(Phone, self).__init__("Phone", group)
        self.number = number
        self.label = label
        self.favoriteVoice = favoriteVoice
        self.favoriteFacetime = favoriteFacetime
    
    def to_plist(self):
        self.add_property('number')
        self.add_property('label')
        self.add_property('favoriteVoice')
        self.add_property('favoriteFacetime')
        return super(Phone, self).to_plist()


class RelatedName(AceObject):
    def __init__(self, name=None, label=None, group="com.apple.ace.system"):
        super(RelatedName, self).__init__("RelatedName", group)
        self.name = name
        self.label = label

    def to_plist(self):
        self.add_property('name')
        self.add_property('label')
        return super(RelatedName, self).to_plist()


class CancelRequest(ServerBoundCommand):
    groupIdentifier = "com.apple.ace.system"
    classIdentifier = "CancelRequest"

    def __init__(self, plist):
        super(CancelRequest, self).__init__(plist)

class CancelSucceeded(ClientBoundCommand):
    def __init__(self, refId):
        super(CancelSucceeded, self).__init__("CancelSucceeded", "com.apple.ace.system", None, refId)

class GetSessionCertificate(ServerBoundCommand):
    groupIdentifier = "com.apple.ace.system"
    classIdentifier = "GetSessionCertificate"

    def __init__(self, plist):
        super(GetSessionCertificate, self).__init__(plist)

class GetSessionCertificateResponse(ClientBoundCommand):
    def __init__(self, refId, caCert, sessionCert):
        super(GetSessionCertificateResponse, self).__init__("GetSessionCertificateResponse", "com.apple.ace.system", None, refId)
        self.certificate = None
        self.caCert = caCert
        self.sessionCert = sessionCert

    def to_plist(self):
        self.certificate = biplist.Data("\x01\x02"+struct.pack(">I", len(self.caCert))+self.caCert + struct.pack(">I", len(self.sessionCert))+self.sessionCert)
        self.add_property('certificate')
        return super(GetSessionCertificateResponse, self).to_plist()
        
class CreateSessionInfoRequest(ServerBoundCommand):
    groupIdentifier = "com.apple.ace.system"
    classIdentifier = "CreateSessionInfoRequest"

    def __init__(self, plist):
        self.sessionInfoRequest = None # binary
        super(CreateSessionInfoRequest, self).__init__(plist)

class CreateSessionInfoResponse(ClientBoundCommand):
    def __init__(self, refId):
        super(CreateSessionInfoResponse, self).__init__("CreateSessionInfoResponse", "com.apple.ace.system", None, refId)
        self.validityDuration = None # number
        self.sessionInfo = None # binary

    def to_plist(self):
        self.add_property('validityDuration')
        self.add_property('sessionInfo')
        return super(CreateSessionInfoResponse, self).to_plist()


class CommandFailed(ClientBoundCommand):
    def __init__(self, refId):
        super(CommandFailed, self).__init__("CommandFailed", "com.apple.ace.system", None, refId, callbacks=[])
        self.reason = None #string
        self.errorCode = None  #int
    
    def to_plist(self):
        self.add_property('reason')
        self.add_property('errorCode')
        return super(CommandFailed, self).to_plist()



class Location(DomainObject):
    AccuracyBestValue = "Best"
    AccuracyNearestTenMetersValue = "NearestTenMeters"
    AccuracyHundredMetersValue = "HundredMeters"
    AccuracyKilometerValue = "Kilometer"
    AccuracyThreeKilometersValue = "ThreeKilometers"
    def __init__(self, label=None, street=None, city=None, stateCode=None, countryCode=None, postalCode=None, latitude=None, longitude=None, accuracy=None, group="com.apple.ace.system", clazz="Location"):
        super(Location, self).__init__(group, None, clazz)
        self.label = label
        self.street = street
        self.city = city
        self.stateCode = stateCode
        self.countryCode = countryCode
        self.postalCode = postalCode
        self.latitude = latitude
        self.longitude = longitude
        self.accuracy = accuracy

    def to_plist(self):
        self.add_property('label')
        self.add_property('street')
        self.add_property('city')
        self.add_property('stateCode')
        self.add_property('countryCode')
        self.add_property('postalCode')
        self.add_property('latitude')
        self.add_property('longitude')
        self.add_property('accuracy')
        return super(Location, self).to_plist()
    
    
class Email(AceObject):
    def __init__(self, group="com.apple.ace.system"):
        super(Email, self).__init__("Email", group)
        self.label = None # string
        self.favoriteFacetime = None # number
        self.emailAddress = None # string

    def to_plist(self):
        self.add_property('label')
        self.add_property('favoriteFacetime')
        self.add_property('emailAddress')
        return super(Email, self).to_plist()
    
    
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

