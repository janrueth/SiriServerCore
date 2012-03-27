from siriObjects.baseObjects import ClientBoundCommand, AceObject, ServerBoundCommand
from siriObjects.systemObjects import DomainObject, Location, Person as SuperPerson, RelatedName as SuperRelatedName, Phone as SuperPhone, Email as SuperEmail
from siriObjects.uiObjects import UISnippet
import logging

class ABAddress(Location):
    def __init__(self):
        super(ABAddress, self).__init__(clazz="Address", group="com.apple.ace.contact")

    def to_plist(self):
        return super(ABAddress, self).to_plist()

class ABContactGroup(DomainObject):
    def __init__(self):
        super(ABContactGroup, self).__init__("com.apple.ace.contact", clazz="ContactGroup")
        self.groupName = None # @"NSString"
        self.groupSource = None # @"Source"

    def to_plist(self):
        self.add_property('groupName')
        self.add_property('groupSource')
        return super(ABContactGroup, self).to_plist()

class ABEmail(SuperEmail):
    def __init__(self):
        super(ABEmail, self).__init__("Email", "com.apple.ace.contact")

    def to_plist(self):
        return super(ABEmail, self).to_plist()

class ABPerson(SuperPerson):
    def __init__(self):
        super(ABPerson, self).__init__("com.apple.ace.contact")

    def to_plist(self):
        return super(ABPerson, self).to_plist()

class ABPersonSearch(ClientBoundCommand):
    ScopeLocalValue = "Local"
    ScopeRemoteValue = "Remote"

    def __init__(self, refId):
        super(ABPersonSearch, self).__init__("PersonSearch", "com.apple.ace.contact", None, refId)
        self.targetAppId = None # @"NSURL"
        self.accountIdentifier = None # @"NSURL"
        self.address = None # @"Location"
        self.birthday = None # @"NSDate"
        self.company = None # @"NSString"
        self.email = None # @"Email"
        self.me = None # @"NSNumber"
        self.name = None # @"NSString"
        self.phone = None # @"Phone"
        self.relationship = None # @"NSString"
        self.scope = None # @"NSString"


    def to_plist(self):
        self.add_property('targetAppId')
        self.add_property('accountIdentifier')
        self.add_property('address')
        self.add_property('birthday')
        self.add_property('company')
        self.add_property('email')
        self.add_property('me')
        self.add_property('name')
        self.add_property('phone')
        self.add_property('relationship')
        self.add_property('scope')
        return super(ABPersonSearch, self).to_plist()

class ABPersonSearchCompleted(ServerBoundCommand):
    classIdentifier = "PersonSearchCompleted"
    groupIdentifier = "com.apple.ace.contact"
    def __init__(self, plist):
        self.results = None # @"NSArray"
        super(ABPersonSearchCompleted, self).__init__(plist)

class ABPersonSnippet(UISnippet):
    def __init__(self):
        super(ABPersonSnippet, self).__init__("PersonSnippet", "com.apple.ace.contact")
        self.displayProperties = None # @"NSArray"
        self.persons = None # @"NSArray"

    def to_plist(self):
        self.add_property('displayProperties')
        self.add_property('persons')
        return super(ABPersonSnippet, self).to_plist()

class ABPhone(SuperPhone):
    def __init__(self):
        super(ABPhone, self).__init__(group="com.apple.ace.contact")

    def to_plist(self):
        return super(ABPhone, self).to_plist()

class ABRelatedName(SuperRelatedName):
    def __init__(self):
        super(ABRelatedName, self).__init__(group="com.apple.ace.contact")

    def to_plist(self):
        return super(ABRelatedName, self).to_plist()

class ABSource(DomainObject):
    def __init__(self):
        super(ABSource, self).__init__("com.apple.ace.contact", clazz="Source")
        self.accountIdentifier = None # @"NSString"
        self.accountName = None # @"NSString"
        self.remote = None # @"NSNumber"

    def to_plist(self):
        self.add_property('accountIdentifier')
        self.add_property('accountName')
        self.add_property('remote')
        return super(ABSource, self).to_plist()





################### OLD CLASSES BELOW, WILL BE REMOVED IN THE FUTURE ######################
################### OLD CLASSES BELOW, WILL BE REMOVED IN THE FUTURE ######################
################### OLD CLASSES BELOW, WILL BE REMOVED IN THE FUTURE ######################
################### OLD CLASSES BELOW, WILL BE REMOVED IN THE FUTURE ######################


class Address(Location):
    def __init__(self, label="", street="", city="", stateCode="", countryCode="", postalCode="", latitude=0, longitude=0, accuracy=0):
        logging.getLogger().warning("This class is deprecated use the AB version instead")
        super(Address, self).__init__(label, street, city, stateCode, countryCode, postalCode, latitude, longitude, accuracy, group="com.apple.ace.contact", clazz="Address")

    def to_plist(self):
        return super(Address, self).to_plist()

class ContactGroup(DomainObject):
    def __init__(self, groupSource=None, groupName=""):
        logging.getLogger().warning("This class is deprecated use the AB version instead")
        super(ContactGroup, self).__init__("com.apple.ace.contact", clazz="ContactGroup")
        self.groupSource = groupSource if groupSource != None else Source()
        self.groupName = groupName

    def to_plist(self):
        self.add_property('groupSource')
        self.add_property('groupName')
        return super(ContactGroup, self).to_plist()


class Email(SuperEmail):
    def __init__(self):
        logging.getLogger().warning("This class is deprecated use the AB version instead")
        super(Email, self).__init__(group="com.apple.ace.contact")

    def to_plist(self):
        return super(Email, self).to_plist()

class Person(SuperPerson):
    def __init__(self):
        logging.getLogger().warning("This class is deprecated use the AB version instead")
        super(Person, self).__init__(group="com.apple.ace.contact")

    def to_plist(self):
        return super(Person, self).to_plist()

class PersonSearch(ClientBoundCommand):
    ScopeLocalValue = "Local"
    ScopeRemoteValue = "Remote"

    def __init__(self, refId):
        logging.getLogger().warning("This class is deprecated use the AB version instead")
        super(PersonSearch, self).__init__("PersonSearch", "com.apple.ace.contact", None, refId)
        self.scope = None
        self.relationship = None
        self.phone = None
        self.name = None
        self.me = None
        self.email = None
        self.company = None
        self.birthday = None
        self.address = None
        self.accountIdentifier = None
        self.targetAppId = None

    def to_plist(self):
        self.add_property('scope')
        self.add_property('relationship')
        self.add_property('phone')
        self.add_property('name')
        self.add_property('me')
        self.add_property('email')
        self.add_property('company')
        self.add_property('birthday')
        self.add_property('address')
        self.add_property('accountIdentifier')
        self.add_property('targetAppId')
        return super(PersonSearch, self).to_plist()

class PersonSearchCompleted(ServerBoundCommand):
    classIdentifier = "PersonSearchCompleted"
    groupIdentifier = "com.apple.ace.contact"
    
    def __init__(self, plist):
        logging.getLogger().warning("This class is deprecated use the AB version instead")
        self.results = None #array
        super(PersonSearchCompleted, self).__init__(plist)

class PersonSnippet(UISnippet):
    def __init__(self, persons=None, displayProperties=None):
        logging.getLogger().warning("This class is deprecated use the AB version instead")
        super(PersonSnippet, self).__init__("PersonSnippet", "com.apple.ace.contact")
        self.persons=persons if persons != None else []
        self.displayProperties = displayProperties if displayProperties != None else []

    def to_plist(self):
        self.add_property('persons')
        self.add_property('displayProperties')
        return super(PersonSnippet, self).to_plist()

class Phone(SuperPhone):
    def __init__(self):
        logging.getLogger().warning("This class is deprecated use the AB version instead")
        super(Phone, self).__init__(group="com.apple.ace.contact")
    
    def to_plist(self):
        return super(Phone, self).to_plist()

class RelatedName(SuperRelatedName):
    def __init__(self):
        logging.getLogger().warning("This class is deprecated use the AB version instead")
        super(RelatedName, self).__init__(group="com.apple.ace.contact")
    
    def to_plist(self):
        return super(RelatedName, self).to_plist()

class Source(DomainObject):
    def __init__(self, remote=0, accountName="", accountIdentifier=""):
        logging.getLogger().warning("This class is deprecated use the AB version instead")
        super(Source, self).__init__("com.apple.ace.contact", clazz="Source")
        self.remote = remote
        self.accountName = accountName
        self.accountIdentifier = accountIdentifier

    def to_plist(self):
        self.add_property('remote')
        self.add_property('accountName')
        self.add_property('accountIdentifier')
        return super(Source, self).to_plist()