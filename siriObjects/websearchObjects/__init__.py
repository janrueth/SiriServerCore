from siriObjects.baseObjects import ClientBoundCommand, AceObject

class WebSearch(ClientBoundCommand):
    def __init__(self, refId=None, aceId=None, query="", provider="Default", targetAppId=""):
        super(WebSearch, self).__init__("Search", "com.apple.ace.websearch", aceId, refId)
        self.query = query
        self.provider = provider
        self.targetAppId = targetAppId

    def to_plist(self):
        self.add_property('query')
        self.add_property('provider')
        self.add_property('targetAppId')
        return super(WebSearch, self).to_plist()