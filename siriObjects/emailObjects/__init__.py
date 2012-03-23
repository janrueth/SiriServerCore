from siriObjects.baseObjects import ClientBoundCommand, ServerBoundCommand
from siriObjects.systemObjects import DomainObject
from siriObjects.uiObjects import UISnippet


class EmailEmail(DomainObject):
    def __init__(self):
        super(EmailEmail, self).__init__("com.apple.ace.email", clazz="Email")
        self.type = None # string
        self.timeZoneId = None # string
        self.subject = None # string
        self.referenceId = None # url
        self.recipientsTo = None # array
        self.recipientsCc = None # array
        self.recipientsBcc = None # array
        self.receivingAddresses = None #array
        self.outgoing = None # number
        self.message = None # string
        self.fromEmail = None # PersonAttribute Object
        self.dateSent = None # date

    def to_plist(self):
        self.add_property('type')
        self.add_property('timeZoneId')
        self.add_property('subject')
        self.add_property('referenceId')
        self.add_property('recipientsTo')
        self.add_property('recipientsCc')
        self.add_property('recipientsBcc')
        self.add_property('receivingAddresses')
        self.add_property('outgoing')
        self.add_property('message')
        self.add_property('fromEmail')
        self.add_property('dateSent')
        return super(EmailEmail, self).to_plist()

class EmailRetrieve(ClientBoundCommand):
    def __init__(self, refId):
        super(EmailRetrieve, self).__init__("Retrieve", "com.apple.ace.email", None, refId)
        self.requestedHeaders = None # array
        self.identifiers = None # array
        self.targetAppId = None # url

    def to_plist(self):
        self.add_property('requestedHeaders')
        self.add_property('identifiers')
        self.add_property('targetAppId')
        return super(EmailRetrieve, self).to_plist()

class EmailRetrieveCompleted(ServerBoundCommand):
    classIdentifier = "RetrieveCompleted"
    groupIdentifier = "com.apple.ace.email"
    def __init__(self, plist):
        self.results = None # array
        super(EmailRetrieveCompleted, self).__init__(plist)

class EmailSearch(ClientBoundCommand):
    def __init__(self, refId):
        super(EmailSearch, self).__init__("Search", "com.apple.ace.email", None, refId)
        self.toEmail = None # string
        self.timeZoneId = None #string
        self.subject = None # string
        self.status = None # int
        self.startDate = None # date
        self.fromEmail = None # string
        self.endDate = None # date
        self.targetAppId = None # url

    def to_plist(self):
        self.add_property('toEmail')
        self.add_property('timeZoneId')
        self.add_property('subject')
        self.add_property('status')
        self.add_property('startDate')
        self.add_property('fromEmail')
        self.add_property('endDate')
        self.add_property('targetAppId')
        return super(EmailSearch, self).to_plist()

class EmailSearchCompleted(ServerBoundCommand):
    classIdentifier = "SearchCompleted"
    groupIdentifier = "com.apple.ace.email"
    def __init__(self, plist):
        self.results = None #array
        self.emailResults = None #array
        super(EmailSearchCompleted, self).__init__(plist)

class EmailSnippet(UISnippet):
    def __init__(self):
        super(EmailSnippet, self).__init__(group="com.apple.ace.email")
        self.emails = None # array

    def to_plist(self):
        self.add_property('emails')
        return super(EmailSnippet, self).to_plist()
        
    