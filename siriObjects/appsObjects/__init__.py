from siriObjects.baseObjects import ClientBoundCommand, ServerBoundCommand


class AppsCheckRestriction(ClientBoundCommand):
    def __init__(self, refId):
        super(AppsCheckRestriction, self).__init__("CheckRestriction", "com.apple.ace.apps", None, refId)
        self.launchId = None # @"NSString"


    def to_plist(self):
        self.add_property('launchId')
        return super(AppsCheckRestriction, self).to_plist()

class AppsGetRestrictedApps(ClientBoundCommand):
    def __init__(self, refId):
        super(AppsGetRestrictedApps, self).__init__("GetRestrictedApps", "com.apple.ace.apps", None, refId)
        self.appIds = None # @"NSArray"


    def to_plist(self):
        self.add_property('appIds')
        return super(AppsGetRestrictedApps, self).to_plist()

class AppsGetRestrictedAppsResponse(ServerBoundCommand):
    classIdentifier = "GetRestrictedAppsResponse"
    groupIdentifier = "com.apple.ace.apps"
    def __init__(self, plist):
        self.restrictedApps = None # @"NSArray"
        self.aceId = None # @"NSString"
        self.refId = None # @"NSString"
        super(AppsGetRestrictedAppsResponse, self).__init__(plist)


class AppsLaunchApp(ClientBoundCommand):
    def __init__(self, refId):
        super(AppsLaunchApp, self).__init__("LaunchApp", "com.apple.ace.apps", None, refId)
        self.launchId = None # @"NSString"


    def to_plist(self):
        self.add_property('launchId')
        return super(AppsLaunchApp, self).to_plist()