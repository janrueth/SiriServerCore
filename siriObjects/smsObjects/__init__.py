from siriObjects.baseObjects import ClientBoundCommand, ServerBoundCommand
from siriObjects.systemObjects import DomainObject
from siriObjects.uiObjects import Snippet


class SmsRecipientSearch(ClientBoundCommand):
    def __init__(self, refId):
        super(SmsRecipientSearch, self).__init__("RecipientSearch", "com.apple.ace.sms", None, refId)
        self.targetAppId = None # @"NSURL"
        self.recipient = None # @"Person"
        self.recipients = None # @"NSArray"

    def to_plist(self):
        self.add_property('targetAppId')
        self.add_property('recipient')
        self.add_property('recipients')
        return super(SmsRecipientSearch, self).to_plist()

class SmsRecipientSearchCompleted(ServerBoundCommand):
    classIdentifier = "RecipientSearchCompleted"
    groupIdentifier = "com.apple.ace.sms"
    def __init__(self, plist):
        self.recipient = None # @"PersonAttribute"
        self.recipients = None # @"NSArray"
        super(SmsRecipientSearchCompleted, self).__init__(plist)

class SmsSearch(ClientBoundCommand):
    SearchStatusReadValue = 1
    SearchStatusUnreadValue = 2
    def __init__(self, refId):
        super(SmsSearch, self).__init__("Search", "com.apple.ace.sms", None, refId)
        self.targetAppId = None # @"NSURL"
        self.end = None # @"NSDate"
        self.message = None # @"NSString"
        self.recipient = None # @"NSString"
        self.sender = None # @"NSString"
        self.start = None # @"NSDate"
        self.status = None # i
        self.timeZoneId = None # @"NSString"

    def to_plist(self):
        self.add_property('targetAppId')
        self.add_property('end')
        self.add_property('message')
        self.add_property('recipient')
        self.add_property('sender')
        self.add_property('start')
        self.add_property('status')
        self.add_property('timeZoneId')
        return super(SmsSearch, self).to_plist()

class SmsSearchCompleted(ServerBoundCommand):
    classIdentifier = "SearchCompleted"
    groupIdentifier = "com.apple.ace.sms"
    def __init__(self, plist):
        self.results = None # @"NSArray"
        super(SmsSearchCompleted, self).__init__(plist)

class SmsSms(DomainObject):
    def __init__(self):
        super(SmsSms, self).__init__("com.apple.ace.sms", clazz="Sms")
        self.attachment = None # @"NSURL"
        self.dateSent = None # @"NSDate"
        self.message = None # @"NSString"
        self.msgRecipients = None # @"NSArray"
        self.msgSender = None # @"PersonAttribute"
        self.outgoing = None # @"NSNumber"
        self.recipients = None # @"NSArray"
        self.sender = None # @"NSString"
        self.subject = None # @"NSString"
        self.timezoneId = None # @"NSString"

    def to_plist(self):
        self.add_property('attachment')
        self.add_property('dateSent')
        self.add_property('message')
        self.add_property('msgRecipients')
        self.add_property('msgSender')
        self.add_property('outgoing')
        self.add_property('recipients')
        self.add_property('sender')
        self.add_property('subject')
        self.add_property('timezoneId')
        return super(SmsSms, self).to_plist()

class SmsSnippet(Snippet):
    def __init__(self):
        super(SmsSnippet, self).__init__("com.apple.ace.sms")
        self.smss = None # @"NSArray"

    def to_plist(self):
        self.add_property('smss')
        return super(SmsSnippet, self).to_plist()