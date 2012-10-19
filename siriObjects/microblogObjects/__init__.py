from siriObjects.uiObjects import UISnippet
from siriObjects.systemObjects import DomainObject


class MicroblogObject(DomainObject):
    def __init__(self):
        super(MicroblogObject, self).__init__("Object", "com.apple.ace.microblog")
        self.attachment = None # @"NSURL"
        self.content = None # @"NSString"
        self.dateSent = None # @"NSDate"
        self.hashtagAlternatives = None # @"NSDictionary"
        self.location = None # @"SALocation"
        self.outgoing = None # @"NSNumber"
        self.providerId = None # @"NSNumber"
        self.recipients = None # @"NSArray"
        self.refereceId = None # @"NSURL"
        self.sender = None # @"SAPersonAttribute"
        self.serviceType = None # @"NSString"
        self.socialProfileReferences = None # @"NSDictionary"
        self.useLocation = None # @"NSNumber"

    def to_plist(self):
        self.add_property('attachment')
        self.add_property('content')
        self.add_property('dateSent')
        self.add_property('hashtagAlternatives')
        self.add_property('location')
        self.add_property('outgoing')
        self.add_property('providerId')
        self.add_property('recipients')
        self.add_property('refereceId')
        self.add_property('sender')
        self.add_property('serviceType')
        self.add_property('socialProfileReferences')
        self.add_property('useLocation')
        return super(MicroblogObject, self).to_plist()
    
class MicroblogFacebookPost(MicroblogObject):
    def __init__(self):
        super(MicroblogFacebookPost, self).__init__("FacebookPost", "com.apple.ace.microblog")

    def to_plist(self):
        return super(MicroblogFacebookPost, self).to_plist()

class MicroblogSnippet(UISnippet):
    def __init__(self):
        super(MicroblogSnippet, self).__init__("Snippet", "com.apple.ace.microblog")
        self.microblogs = None # @"NSArray"

    def to_plist(self):
        self.add_property('microblogs')
        return super(MicroblogSnippet, self).to_plist()

class MicroblogTwitterPost(MicroblogObject):
    def __init__(self):
        super(MicroblogTwitterPost, self).__init__("TwitterPost", "com.apple.ace.microblog")

    def to_plist(self):
        return super(MicroblogTwitterPost, self).to_plist()