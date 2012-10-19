from siriObjects.systemObjects import AceView, Location, DomainObject
from siriObjects.baseObjects import ClientBoundCommand, ServerBoundCommand
from siriObjects.uiObjects import UISnippet


class FmfGeoFence(DomainObject):
    def __init__(self):
        super(FmfGeoFence, self).__init__("GeoFence", "com.apple.ace.fmf")
        self.friend = None # @"SAPersonAttribute"
        self.geoFenceTrigger = None # @"NSString"
        self.location = None # @"SALocation"

    def to_plist(self):
        self.add_property('friend')
        self.add_property('geoFenceTrigger')
        self.add_property('location')
        return super(FmfGeoFence, self).to_plist()

class FmfGeoFenceSet(ClientBoundCommand):
    def __init__(self, refId):
        super(FmfGeoFenceSet, self).__init__("GeoFenceSet", "com.apple.ace.fmf", None, refId)
        self.targetAppId = None # @"NSURL"
        self.enable = None # @"NSNumber"
        self.fenceType = None # @"NSString"
        self.friend = None # @"SAPerson"
        self.geoFenceTrigger = None # @"NSString"
        self.oneTimeOnly = None # @"NSNumber"
        self.requestedLocation = None # @"SALocation"


    def to_plist(self):
        self.add_property('targetAppId')
        self.add_property('enable')
        self.add_property('fenceType')
        self.add_property('friend')
        self.add_property('geoFenceTrigger')
        self.add_property('oneTimeOnly')
        self.add_property('requestedLocation')
        return super(FmfGeoFenceSet, self).to_plist()

class FmfGeoFenceSetCompleted(ServerBoundCommand):
    classIdentifier = "GeoFenceSetCompleted"
    groupIdentifier = "com.apple.ace.fmf"
    def __init__(self, plist):
        self.targetAppId = None # @"NSURL"
        self.geoFence = None # @"SAFmfGeoFence"
        self.searchContext = None # @"NSURL"
        self.aceId = None # @"NSString"
        self.refId = None # @"NSString"
        super(FmfGeoFenceSetCompleted, self).__init__(plist)


class FmfGeoFenceSnippet(UISnippet):
    def __init__(self):
        super(FmfGeoFenceSnippet, self).__init__("GeoFenceSnippet", "com.apple.ace.fmf")
        self.aceFmfGeoFence = None # @"SAFmfGeoFence"
        self.enable = None # @"NSNumber"
        self.fenceType = None # @"NSString"
        self.oneTimeOnly = None # @"NSNumber"
        self.searchContext = None # @"NSURL"

    def to_plist(self):
        self.add_property('aceFmfGeoFence')
        self.add_property('enable')
        self.add_property('fenceType')
        self.add_property('oneTimeOnly')
        self.add_property('searchContext')
        return super(FmfGeoFenceSnippet, self).to_plist()

class FmfLocation(Location):
    def __init__(self):
        super(FmfLocation, self).__init__("Location", "com.apple.ace.fmf")
        self.distance = None # @"NSNumber"
        self.emailAddress = None # @"NSString"
        self.friend = None # @"SAPersonAttribute"
        self.locationDate = None # @"NSNumber"

    def to_plist(self):
        self.add_property('distance')
        self.add_property('emailAddress')
        self.add_property('friend')
        self.add_property('locationDate')
        return super(FmfLocation, self).to_plist()

class FmfLocationSnippet(UISnippet):
    def __init__(self):
        super(FmfLocationSnippet, self).__init__("LocationSnippet", "com.apple.ace.fmf")
        self.atRequestedLocation = None # @"NSNumber"
        self.locations = None # @"NSArray"
        self.proximity = None # @"NSString"
        self.searchContext = None # @"NSURL"

    def to_plist(self):
        self.add_property('atRequestedLocation')
        self.add_property('locations')
        self.add_property('proximity')
        self.add_property('searchContext')
        return super(FmfLocationSnippet, self).to_plist()

class FmfSearch(ClientBoundCommand):
    def __init__(self, refId):
        super(FmfSearch, self).__init__("Search", "com.apple.ace.fmf", None, refId)
        self.targetAppId = None # @"NSURL"
        self.currentLocation = None # @"SALocation"
        self.emailAddresses = None # @"NSArray"
        self.friends = None # @"NSArray"
        self.proximity = None # @"NSString"
        self.requestedLocation = None # @"SALocation"


    def to_plist(self):
        self.add_property('targetAppId')
        self.add_property('currentLocation')
        self.add_property('emailAddresses')
        self.add_property('friends')
        self.add_property('proximity')
        self.add_property('requestedLocation')
        return super(FmfSearch, self).to_plist()

class FmfSearchCompleted(ServerBoundCommand):
    classIdentifier = "SearchCompleted"
    groupIdentifier = "com.apple.ace.fmf"
    def __init__(self, plist):
        self.atRequestedLocation = None # @"NSNumber"
        self.fmfLocations = None # @"NSArray"
        self.searchContext = None # @"NSURL"
        self.aceId = None # @"NSString"
        self.refId = None # @"NSString"
        super(FmfSearchCompleted, self).__init__(plist)


class FmfVisibilitySetCompleted(ServerBoundCommand):
    classIdentifier = "VisibilitySetCompleted"
    groupIdentifier = "com.apple.ace.fmf"
    def __init__(self, plist):
        self.targetAppId = None # @"NSURL"
        self.searchContext = None # @"NSURL"
        self.aceId = None # @"NSString"
        self.refId = None # @"NSString"
        super(FmfVisibilitySetCompleted, self).__init__(plist)


class FmfVisibilityStateSet(ClientBoundCommand):
    def __init__(self, refId):
        super(FmfVisibilityStateSet, self).__init__("VisibilityStateSet", "com.apple.ace.fmf", None, refId)
        self.targetAppId = None # @"NSURL"
        self.visible = None # c


    def to_plist(self):
        self.add_property('targetAppId')
        self.add_property('visible')
        return super(FmfVisibilityStateSet, self).to_plist()

class FmfVisibilityView(AceView):
    def __init__(self):
        super(FmfVisibilityView, self).__init__("VisibilityView", "com.apple.ace.fmf")
        self.searchContext = None # @"NSURL"
        self.visible = None # c

    def to_plist(self):
        self.add_property('searchContext')
        self.add_property('visible')
        return super(FmfVisibilityView, self).to_plist()