from siriObjects.baseObjects import ClientBoundCommand, AceObject, ServerBoundCommand
from siriObjects.systemObjects import DomainObject, PersonAttribute
from siriObjects.uiObjects import UISnippet


class PhoneCall(ClientBoundCommand):
    def __init__(self, refId, recipient="", faceTime=False, callRecipient=None, targetAppId=""):
        super(PhoneCall, self).__init__("Call", "com.apple.ace.phone", None, refId)
        self.recipient = recipient
        self.faceTime = faceTime
        self.callRecipient = callRecipient if callRecipient != None else PersonAttribute()
        self.targetAppId = targetAppId

    def to_plist(self):
        self.add_property('recipient')
        self.add_property('faceTime')
        self.add_property('callRecipient')
        self.add_property('targetAppId')
        return super(PhoneCall, self).to_plist()



class PhoneCallSnippet(UISnippet):
    def __init__(self, calls=None):
        super(PhoneCallSnippet, self).__init__("CallSnippet", "com.apple.ace.phone")
        self.calls = calls if calls != None else []
    
    def to_plist(self):
        self.add_property('calls')
        return super(PhoneCallSnippet, self).to_plist()

class PhoneCallStarted(ServerBoundCommand):
    groupIdentifier = "com.apple.ace.phone"
    classIdentifier = "CallStarted"
    def __init__(self, plist):
        self.phoneLogId=""
        super(PhoneCallSnippet, self).__init__(plist)

class PhoneSearch(ClientBoundCommand):
    def __init__(self, refId, timeZoneId="", start="", outgoingPhoneNumber="", missed=False, limit=5, incomingPhoneNumber="", end="", targetAppId=""):
        super(PhoneSearch, self).__init__("Search", "com.apple.ace.phone", None, refId)
        self.timeZoneId = timeZoneId
        self.start = start
        self.outgoingPhoneNumber = outgoingPhoneNumber
        self.missed = missed
        self.limit = limit
        self.incomingPhoneNumber = incomingPhoneNumber
        self.end = end
        self.targetAppId = targetAppId

    def to_plist(self):
        self.add_property('timeZoneId')
        self.add_property('start')
        self.add_property('outgoingPhoneNumber')
        self.add_property('missed')
        self.add_property('limit')
        self.add_property('incomingPhoneNumber')
        self.add_property('end')
        self.add_property('targetAppId')
        return super(PhoneSearch, self).to_plist()

class PhoneSearchCompleted(ServerBoundCommand):
    groupIdentifier = "com.apple.ace.phone"
    classIdentifier = "SearchCompleted"

    def __init__(self, plist):
        self.phoneLogIds = []
        super(PhoneSearchCompleted, self).__init__(plist)