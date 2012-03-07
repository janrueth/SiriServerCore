from siriObjects.baseObjects import ClientBoundCommand, AceObject, ServerBoundCommand
from siriObjects.systemObjects import DomainObject, Location, Person as SuperPerson, RelatedName as SuperRelatedName, Phone as SuperPhone
from siriObjects.uiObjects import Snippet
from siriObjects.emailObjects import Email as SuperEmail

class Address(Location):
    def __init__(self, label="", street="", city="", stateCode="", countryCode="", postalCode="", latitude=0, longitude=0, accuracy=0):
        super(Address, self).__init__(label, street, city, stateCode, countryCode, postalCode, latitude, longitude, accuracy, group="com.apple.ace.contact", clazz="Address")

    def to_plist(self):
        return super(Address, self).to_plist()

class ContactGroup(DomainObject):
    def __init__(self, groupSource=None, groupName=""):
        super(ContactGroup, self).__init__("com.apple.ace.contact", clazz="ContactGroup")
        self.groupSource = groupSource if groupSource != None else Source()
        self.groupName = groupName

    def to_plist(self):
        self.add_property('groupSource')
        self.add_property('groupName')
        return super(ContactGroup, self).to_plist()


class Email(SuperEmail):
    def __init__(self):
        super(Email, self).__init__(group="com.apple.ace.contact")

    def to_plist(self):
        return super(Email, self).to_plist()

class Person(SuperPerson):
    def __init__(self):
        super(Person, self).__init__(group="com.apple.ace.contact")

    def to_plist(self):
        return super(Person, self).to_plist()

class PersonSearch(ClientBoundCommand):
    ScopeLocalValue = "Local"
    ScopeRemoteValue = "Remote"

    def __init__(self, refId):
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
        self.results = None #array
        super(PersonSearchCompleted, self).__init__(plist)

class PersonSnippet(Snippet):
    def __init__(self, persons=None, displayProperties=None):
        super(PersonSnippet, self).__init__("com.apple.ace.contact", clazz="PersonSnippet")
        self.person=persons if persons != None else []
        self.displayProperties = displayProperties if displayProperties != None else []

    def to_plist(self):
        self.add_property('person')
        self.add_property('displayProperties')
        return super(PersonSnippet, self).to_plist()

class Phone(SuperPhone):
    def __init__(self):
        super(Phone, self).__init__(group="com.apple.ace.contact")
    
    def to_plist(self):
        return super(Phone, self).to_plist()

class RelatedName(SuperRelatedName):
    def __init__(self):
        super(RelatedName, self).__init__(group="com.apple.ace.contact")
    
    def to_plist(self):
        return super(RelatedName, self).to_plist()

class Source(DomainObject):
    def __init__(self, remote=0, accountName="", accountIdentifier=""):
        super(Source, self).__init__("com.apple.ace.contact", clazz="Source")
        self.remote = remote
        self.accountName = accountName
        self.accountIdentifier = accountIdentifier

    def to_plist(self):
        self.add_property('remote')
        self.add_property('accountName')
        self.add_property('accountIdentifier')
        return super(Source, self).to_plist()