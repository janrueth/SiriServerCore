from siriObjects.baseObjects import ClientBoundCommand, AceObject, ServerBoundCommand
from siriObjects.systemObjects import DomainObject, Location
from siriObjects.uiObjects import UISnippet

class MapItemSnippet(UISnippet):
    def __init__(self, userCurrentLocation=True, items=None):
        super(MapItemSnippet, self).__init__("MapItemSnippet", "com.apple.ace.localsearch")
        self.userCurrentLocation = userCurrentLocation
        self.items = items
        self.searchRegionCenter = None # systemObjects.Location
        self.regionOfInterestRadiusInMiles = None
        self.providerCommand = None # array
    
    def to_plist(self):
        self.add_property('userCurrentLocation')
        self.add_property('items')
        self.add_property('searchRegionCenter')
        self.add_property('regionOfInterestRadiusInMiles')
        self.add_property('providerCommand')
        return super(MapItemSnippet, self).to_plist()

class MapItem(DomainObject):
    TypeCURRENT_LOCATIONValue = "CURRENT_LOCATION"
    TypeBUSINESS_ITEMValue = "BUSINESS_ITEM"
    TypePERSON_ITEMValue = "PERSON_ITEM"
    TypeADDRESS_ITEMValue = "ADDRESS_ITEM"
    TypeHOME_ITEMValue = "HOME_ITEM"
    
    def __init__(self, label="", street="", city="", stateCode="", countryCode="", postalCode="", latitude=0, longitude=0, detailType="BUSINESS_ITEM", clazz="MapItem"):
        super(MapItem, self).__init__("com.apple.ace.localsearch", clazz="MapItem")
        self.label = label
        self.detailType = detailType
        self.location = Location(label,street,city,stateCode,countryCode,postalCode,latitude,longitude)
        self.placeId = None
        self.distanceInMiles = None
        self.detail = None #AceObject
    
    def to_plist(self):
        self.add_property('label')
        self.add_property('detailType')
        self.add_property('location')
        self.add_property('placeId')
        self.add_property('distanceInMiles')
        self.add_property('detail')
        return super(MapItem, self).to_plist()

class ActionableMapItem(MapItem):
    def __init__(self, label="", street="", city="", stateCode="", countryCode="", postalCode="", latitude=0, longitude=0, detailType=MapItem.TypeCURRENT_LOCATIONValue, commands=None):
        super(ActionableMapItem, self).__init__(self, label, street, city, stateCode, countryCode, postalCode, latitude, longitude, detailType, clazz="ActionableMapItem")
        self.commands = commands if commands != None else []
    
    def to_plist(self):
        self.add_property('commands')
        return super(ActionableMapItem, self).to_plist()


class Rating(AceObject):
    def __init__(self, value=0.0, providerId="", description="", count=0):
        super(Rating, self).__init__("Rating", "com.apple.ace.localsearch")
        self.value = value
        self.providerId = providerId
        self.description = description
        self.count = count

    def to_plist(self):
        self.add_property('value')
        self.add_property('providerId')
        self.add_property('description')
        self.add_property('count')
        return super(Rating, self).to_plist()

class Business(AceObject):
    def __init__(self, totalNumberOfReviews=0, rating=None, photo="", phoneNumbers=None, openingHours="", name="", extSessionGuid="", categories=None, businessUrl="", businessIds=None, businessId=0):
        super(Business, self).__init__("Business", "com.apple.ace.localsearch")
        self.totalNumberOfReviews = totalNumberOfReviews
        self.rating = rating if rating != None else Rating()
        self.photo = photo
        self.phoneNumbers = phoneNumbers if phoneNumbers != None else []
        self.openingHours = openingHours
        self.name = name
        self.extSessionGuid = extSessionGuid
        self.categories = categories if categories != None else []
        self.businessUrl = businessUrl
        self.businessIds = businessIds if businessIds != None else dict()
        self.businessId = businessId

    def to_plist(self):
        self.add_property('totalNumberOfReviews')
        self.add_property('rating')
        self.add_property('photo')
        self.add_property('phoneNumbers')
        self.add_property('openingHours')
        self.add_property('name')
        self.add_property('extSessionGuid')
        self.add_property('categories')
        self.add_property('businessUrl')
        self.add_property('businessIds')
        self.add_property('businessId')
        return super(Business, self).to_plist()

class DisambiguationMap(UISnippet):
    def __init__(self, items=None):
        super(DisambiguationMap, self).__init__("DisambiguationMap", "com.apple.ace.localsearch")
        self.items = items if items != None else []

    def to_plist(self):
        self.add_property('items')
        return super(DisambiguationMap, self).to_plist()

class PhoneNumber(AceObject):
    TypePRIMARYValue = "PRIMARY"
    TypeSECONDARYValue =  "SECONDARY"
    TypeFAXValue = "FAX"
    TTYValue = "TTY"

    def __init__(self, value="", type="PRIMARY"):
        super(PhoneNumber, self).__init__("PhoneNumber", "com.apple.ace.localsearch")
        self.value = value
        self.type = type

    def to_plist(self):
        self.add_property('value')
        self.add_property('type')
        return super(PhoneNumber, self).to_plist()



class Review(AceObject):
    TypePROFESSIONALValue = "PROFESSIONAL"
    TypeCOMMUNITYValue = "COMMUNITY"
    TypePERSONALValue = "PERSONAL"

    def __init__(self, url="", type="PROFESSIONAL", reviewerUrl="", reviewerName="", rating=None, publication="", provider="", fullReview="", excerpt=""):
        super(Review, self).__init__("Review", "com.apple.ace.localsearch")
        self.url = url
        self.type = type
        self.reviewerUrl = reviewerUrl
        self.reviewerName = reviewerName
        self.rating = rating if rating != None else Rating()
        self.publication = publication
        self.provider = provider
        self.fullReview = fullReview
        self.excerpt = excerpt

    def to_plist(self):
        self.add_property('url')
        self.add_property('type')
        self.add_property('reviewerUrl')
        self.add_property('reviewerName')
        self.add_property('rating')
        self.add_property('publication')
        self.add_property('provider')
        self.add_property('fullReview')
        self.add_property('excerpt')
        return super(Review, self).to_plist()

class ShowMapPoints(ClientBoundCommand):
    DirectionsTypeByCarValue = "ByCar"
    DirectionsTypeByPublicTransitValue = "ByPublicTransit"
    DirectionsTypeWalkingValue = "Walking"
    DirectionsTypeBikingValue = "Biking"

    def __init__(self, refId, showTraffic=False, showDirections=False, regionOfInterestRadiusInMiles=0, itemSource=None, itemDestination=None, directionsType="ByCar", targetAppId=""):
        super(ShowMapPoints, self).__init__("ShowMapPoints", "com.apple.ace.localsearch", None, refId)
        self.showTraffic = showTraffic
        self.showDirections = showDirections
        self.regionOfInterestRadiusInMiles = regionOfInterestRadiusInMiles
        self.itemSource = itemSource if itemSource != None else MapItem()
        self.itemDestination = itemDestination if itemDestination != None else MapItem()
        self.directionsType = directionsType
        self.targetAppId = targetAppId

    def to_plist(self):
        self.add_property('showTraffic')
        self.add_property('showDirections')
        self.add_property('regionOfInterestRadiusInMiles')
        self.add_property('itemSource')
        self.add_property('itemDestination')
        self.add_property('directionsType')
        self.add_property('targetAppId')
        return super(ShowMapPoints, self).to_plist()

class ShowMapPointsCompleted(ServerBoundCommand):
    classIdentifier = "ShowMapPointsCompleted"
    groupIdentifier = "com.apple.ace.localsearch"
    
    def __init__(self, plist):
        super(ShowMapPointsCompleted, self).__init__(plist)
        
        
        
##### IOS 6 stuff

class LocalSearchMapItem(DomainObject):
    def __init__(self):
        super(LocalSearchMapItem, self).__init__("MapItem", "com.apple.ace.localsearch")
        self.attributions = None # @"NSArray"
        self.detail = None # @"<SAAceSerializable>"
        self.detailType = None # @"NSString"
        self.directionRole = None # @"NSString"
        self.distance = None # @"SADistance"
        self.distanceInMiles = None # @"NSNumber"
        self.label = None # @"NSString"
        self.location = None # @"SALocation"
        self.placeId = None # @"NSNumber"

    def to_plist(self):
        self.add_property('attributions')
        self.add_property('detail')
        self.add_property('detailType')
        self.add_property('directionRole')
        self.add_property('distance')
        self.add_property('distanceInMiles')
        self.add_property('label')
        self.add_property('location')
        self.add_property('placeId')
        return super(LocalSearchMapItem, self).to_plist()

class LocalSearchAceNavigationEta(AceObject):
    def __init__(self):
        super(LocalSearchAceNavigationEta, self).__init__("AceNavigationEta", "com.apple.ace.localsearch")
        self.distanceEta = None # @"SADistance"
        self.timeEta = None # @"SADuration"

    def to_plist(self):
        self.add_property('distanceEta')
        self.add_property('timeEta')
        return super(LocalSearchAceNavigationEta, self).to_plist()

class LocalSearchActionableMapItem(LocalSearchMapItem):
    def __init__(self):
        super(LocalSearchActionableMapItem, self).__init__("ActionableMapItem", "com.apple.ace.localsearch")
        self.commands = None # @"NSArray"

    def to_plist(self):
        self.add_property('commands')
        return super(LocalSearchActionableMapItem, self).to_plist()

class LocalSearchAttribution(AceObject):
    def __init__(self):
        super(LocalSearchAttribution, self).__init__("Attribution", "com.apple.ace.localsearch")
        self.attributionId = None # @"NSString"
        self.urls = None # @"NSArray"
        self.version = None # i

    def to_plist(self):
        self.add_property('attributionId')
        self.add_property('urls')
        self.add_property('version')
        return super(LocalSearchAttribution, self).to_plist()

class LocalSearchBusiness(AceObject):
    def __init__(self):
        super(LocalSearchBusiness, self).__init__("Business", "com.apple.ace.localsearch")
        self.businessId = None # @"NSNumber"
        self.businessIds = None # @"NSDictionary"
        self.businessUrl = None # @"NSURL"
        self.categories = None # @"NSArray"
        self.extSessionGuid = None # @"NSString"
        self.name = None # @"NSString"
        self.openingHours = None # @"NSString"
        self.phoneNumbers = None # @"NSArray"
        self.photo = None # @"NSURL"
        self.rating = None # @"SALocalSearchRating"
        self.reviews = None # @"NSArray"
        self.totalNumberOfReviews = None # i

    def to_plist(self):
        self.add_property('businessId')
        self.add_property('businessIds')
        self.add_property('businessUrl')
        self.add_property('categories')
        self.add_property('extSessionGuid')
        self.add_property('name')
        self.add_property('openingHours')
        self.add_property('phoneNumbers')
        self.add_property('photo')
        self.add_property('rating')
        self.add_property('reviews')
        self.add_property('totalNumberOfReviews')
        return super(LocalSearchBusiness, self).to_plist()

class LocalSearchBusiness2(DomainObject):
    def __init__(self):
        super(LocalSearchBusiness2, self).__init__("Business2", "com.apple.ace.localsearch")
        self.address = None # @"SALocation"
        self.businessUrl = None # @"NSURL"
        self.categories = None # @"NSArray"
        self.description = None # @"NSString"
        self.extSessionGuid = None # @"NSString"
        self.identifierMap = None # @"NSDictionary"
        self.name = None # @"NSString"
        self.offerLists = None # @"NSArray"
        self.operationHours = None # @"SALocalSearchOperationHours"
        self.phoneNumber = None # @"NSString"
        self.photoFullSize = None # @"NSArray"
        self.photoList = None # @"NSArray"
        self.photoThumbnail = None # @"NSArray"
        self.reviewList = None # @"NSArray"

    def to_plist(self):
        self.add_property('address')
        self.add_property('businessUrl')
        self.add_property('categories')
        self.add_property('description')
        self.add_property('extSessionGuid')
        self.add_property('identifierMap')
        self.add_property('name')
        self.add_property('offerLists')
        self.add_property('operationHours')
        self.add_property('phoneNumber')
        self.add_property('photoFullSize')
        self.add_property('photoList')
        self.add_property('photoThumbnail')
        self.add_property('reviewList')
        return super(LocalSearchBusiness2, self).to_plist()

class LocalSearchDisambiguationMap(UISnippet):
    def __init__(self):
        super(LocalSearchDisambiguationMap, self).__init__("DisambiguationMap", "com.apple.ace.localsearch")
        self.items = None # @"NSArray"

    def to_plist(self):
        self.add_property('items')
        return super(LocalSearchDisambiguationMap, self).to_plist()

class LocalSearchGetNavigationStatus(ClientBoundCommand):
    def __init__(self, refId):
        super(LocalSearchGetNavigationStatus, self).__init__("GetNavigationStatus", "com.apple.ace.localsearch", None, refId)
        self.targetAppId = None # @"NSURL"
        self.getRoute = None # @"NSNumber"


    def to_plist(self):
        self.add_property('targetAppId')
        self.add_property('getRoute')
        return super(LocalSearchGetNavigationStatus, self).to_plist()

class LocalSearchGetNavigationStatusCompleted(ServerBoundCommand):
    classIdentifier = "GetNavigationStatusCompleted"
    groupIdentifier = "com.apple.ace.localsearch"
    def __init__(self, plist):
        self.etaInMinutes = None # @"NSNumber"
        self.navigating = None # @"NSNumber"
        self.nextManeuverEta = None # @"SALocalSearchAceNavigationEta"
        self.overallEta = None # @"SALocalSearchAceNavigationEta"
        self.route = None # @"SALocalSearchRoute"
        self.aceId = None # @"NSString"
        self.refId = None # @"NSString"
        super(LocalSearchGetNavigationStatusCompleted, self).__init__(plist)




class LocalSearchMapItemSnippet(UISnippet):
    def __init__(self):
        super(LocalSearchMapItemSnippet, self).__init__("MapItemSnippet", "com.apple.ace.localsearch")
        self.items = None # @"NSArray"
        self.providerCommand = None # @"NSArray"
        self.regionOfInterestRadiusInMiles = None # @"NSNumber"
        self.searchRegionCenter = None # @"SALocation"
        self.userCurrentLocation = None # @"NSNumber"

    def to_plist(self):
        self.add_property('items')
        self.add_property('providerCommand')
        self.add_property('regionOfInterestRadiusInMiles')
        self.add_property('searchRegionCenter')
        self.add_property('userCurrentLocation')
        return super(LocalSearchMapItemSnippet, self).to_plist()

class LocalSearchNamedPeriod(AceObject):
    def __init__(self):
        super(LocalSearchNamedPeriod, self).__init__("NamedPeriod", "com.apple.ace.localsearch")
        self.value = None # @"NSString"

    def to_plist(self):
        self.add_property('value')
        return super(LocalSearchNamedPeriod, self).to_plist()

class LocalSearchNavStatus(AceObject):
    def __init__(self):
        super(LocalSearchNavStatus, self).__init__("NavStatus", "com.apple.ace.localsearch")
        self.statusValue = None # @"NSString"

    def to_plist(self):
        self.add_property('statusValue')
        return super(LocalSearchNavStatus, self).to_plist()

class LocalSearchNavigationPromptManeuver(ClientBoundCommand):
    def __init__(self, refId):
        super(LocalSearchNavigationPromptManeuver, self).__init__("NavigationPromptManeuver", "com.apple.ace.localsearch", None, refId)
        self.targetAppId = None # @"NSURL"
        self.maneuverIndex = None # @"NSNumber"


    def to_plist(self):
        self.add_property('targetAppId')
        self.add_property('maneuverIndex')
        return super(LocalSearchNavigationPromptManeuver, self).to_plist()

class LocalSearchNavigationPromptManeuverCompleted(ServerBoundCommand):
    classIdentifier = "NavigationPromptManeuverCompleted"
    groupIdentifier = "com.apple.ace.localsearch"
    def __init__(self, plist):
        self.aceId = None # @"NSString"
        self.refId = None # @"NSString"
        super(LocalSearchNavigationPromptManeuverCompleted, self).__init__(plist)


class LocalSearchOffer(AceObject):
    def __init__(self):
        super(LocalSearchOffer, self).__init__("Offer", "com.apple.ace.localsearch")
        self.identifier = None # @"NSString"
        self.offerPunchOut = None # @"SAUIAppPunchOut"
        self.title = None # @"NSString"

    def to_plist(self):
        self.add_property('identifier')
        self.add_property('offerPunchOut')
        self.add_property('title')
        return super(LocalSearchOffer, self).to_plist()

class LocalSearchOfferList(AceObject):
    def __init__(self):
        super(LocalSearchOfferList, self).__init__("OfferList", "com.apple.ace.localsearch")
        self.offers = None # @"NSArray"
        self.providerId = None # @"NSString"

    def to_plist(self):
        self.add_property('offers')
        self.add_property('providerId')
        return super(LocalSearchOfferList, self).to_plist()

class LocalSearchOperationHours(AceObject):
    def __init__(self):
        super(LocalSearchOperationHours, self).__init__("OperationHours", "com.apple.ace.localsearch")
        self.operationPeriods = None # @"NSDictionary"

    def to_plist(self):
        self.add_property('operationPeriods')
        return super(LocalSearchOperationHours, self).to_plist()

class LocalSearchPhoneNumber(AceObject):
    def __init__(self):
        super(LocalSearchPhoneNumber, self).__init__("PhoneNumber", "com.apple.ace.localsearch")
        self.type = None # @"NSString"
        self.value = None # @"NSString"

    def to_plist(self):
        self.add_property('type')
        self.add_property('value')
        return super(LocalSearchPhoneNumber, self).to_plist()

class LocalSearchPhoto(AceObject):
    def __init__(self):
        super(LocalSearchPhoto, self).__init__("Photo", "com.apple.ace.localsearch")
        self.fullsize = None # @"NSURL"
        self.identifier = None # @"NSString"
        self.photoPunchOut = None # @"SAUIAppPunchOut"
        self.thumbnail = None # @"NSURL"

    def to_plist(self):
        self.add_property('fullsize')
        self.add_property('identifier')
        self.add_property('photoPunchOut')
        self.add_property('thumbnail')
        return super(LocalSearchPhoto, self).to_plist()

class LocalSearchPhotoList(AceObject):
    def __init__(self):
        super(LocalSearchPhotoList, self).__init__("PhotoList", "com.apple.ace.localsearch")
        self.photos = None # @"NSArray"
        self.providerId = None # @"NSString"

    def to_plist(self):
        self.add_property('photos')
        self.add_property('providerId')
        return super(LocalSearchPhotoList, self).to_plist()

class LocalSearchProtobufAttribute(AceObject):
    def __init__(self):
        super(LocalSearchProtobufAttribute, self).__init__("ProtobufAttribute", "com.apple.ace.localsearch")
        self.name = None # @"NSString"
        self.value = None # @"NSString"

    def to_plist(self):
        self.add_property('name')
        self.add_property('value')
        return super(LocalSearchProtobufAttribute, self).to_plist()

class LocalSearchRangePeriod(AceObject):
    def __init__(self):
        super(LocalSearchRangePeriod, self).__init__("RangePeriod", "com.apple.ace.localsearch")
        self.endSecondsSinceMidnight = None # i
        self.startSecondsSinceMidnight = None # i

    def to_plist(self):
        self.add_property('endSecondsSinceMidnight')
        self.add_property('startSecondsSinceMidnight')
        return super(LocalSearchRangePeriod, self).to_plist()

class LocalSearchRating(AceObject):
    def __init__(self):
        super(LocalSearchRating, self).__init__("Rating", "com.apple.ace.localsearch")
        self.count = None # i
        self.description = None # @"NSString"
        self.maxValue = None # d
        self.providerId = None # @"NSString"
        self.value = None # d

    def to_plist(self):
        self.add_property('count')
        self.add_property('description')
        self.add_property('maxValue')
        self.add_property('providerId')
        self.add_property('value')
        return super(LocalSearchRating, self).to_plist()

class LocalSearchReview(AceObject):
    def __init__(self):
        super(LocalSearchReview, self).__init__("Review", "com.apple.ace.localsearch")
        self.author = None # @"NSString"
        self.comment = None # @"NSString"
        self.lastUpdated = None # @"SACalendar"
        self.publication = None # @"NSString"
        self.reviewPunchOut = None # @"SAUIAppPunchOut"
        self.reviewRating = None # @"SALocalSearchRating"

    def to_plist(self):
        self.add_property('author')
        self.add_property('comment')
        self.add_property('lastUpdated')
        self.add_property('publication')
        self.add_property('reviewPunchOut')
        self.add_property('reviewRating')
        return super(LocalSearchReview, self).to_plist()

class LocalSearchReviewList(AceObject):
    def __init__(self):
        super(LocalSearchReviewList, self).__init__("ReviewList", "com.apple.ace.localsearch")
        self.providerId = None # @"NSURL"
        self.providerId2 = None # @"NSString"
        self.rating = None # @"SALocalSearchRating"
        self.selectReviews = None # @"NSArray"
        self.totalReviewCount = None # @"NSNumber"

    def to_plist(self):
        self.add_property('providerId')
        self.add_property('providerId2')
        self.add_property('rating')
        self.add_property('selectReviews')
        self.add_property('totalReviewCount')
        return super(LocalSearchReviewList, self).to_plist()

class LocalSearchRoute(AceObject):
    def __init__(self):
        super(LocalSearchRoute, self).__init__("Route", "com.apple.ace.localsearch")
        self.routeAsZilchBinary = None # @"NSData"

    def to_plist(self):
        self.add_property('routeAsZilchBinary')
        return super(LocalSearchRoute, self).to_plist()

class LocalSearchSendToProtobufConduit(ClientBoundCommand):
    def __init__(self, refId):
        super(LocalSearchSendToProtobufConduit, self).__init__("SendToProtobufConduit", "com.apple.ace.localsearch", None, refId)
        self.targetAppId = None # @"NSURL"
        self.attributes = None # @"NSArray"
        self.endpoint = None # @"NSURL"
        self.rawRequest = None # @"NSData"
        self.timeoutInSeconds = None # i


    def to_plist(self):
        self.add_property('targetAppId')
        self.add_property('attributes')
        self.add_property('endpoint')
        self.add_property('rawRequest')
        self.add_property('timeoutInSeconds')
        return super(LocalSearchSendToProtobufConduit, self).to_plist()

class LocalSearchSendToProtobufConduitCompleted(ServerBoundCommand):
    classIdentifier = "SendToProtobufConduitCompleted"
    groupIdentifier = "com.apple.ace.localsearch"
    def __init__(self, plist):
        self.rawResponse = None # @"NSData"
        self.aceId = None # @"NSString"
        self.refId = None # @"NSString"
        super(LocalSearchSendToProtobufConduitCompleted, self).__init__(plist)


class LocalSearchShowMapPoints(ClientBoundCommand):
    def __init__(self, refId):
        super(LocalSearchShowMapPoints, self).__init__("ShowMapPoints", "com.apple.ace.localsearch", None, refId)
        self.targetAppId = None # @"NSURL"
        self.directionsType = None # @"NSString"
        self.itemDestination = None # @"SALocalSearchMapItem"
        self.itemSource = None # @"SALocalSearchMapItem"
        self.regionOfInterestRadiusInMiles = None # @"NSNumber"
        self.showDirections = None # c
        self.showTraffic = None # c


    def to_plist(self):
        self.add_property('targetAppId')
        self.add_property('directionsType')
        self.add_property('itemDestination')
        self.add_property('itemSource')
        self.add_property('regionOfInterestRadiusInMiles')
        self.add_property('showDirections')
        self.add_property('showTraffic')
        return super(LocalSearchShowMapPoints, self).to_plist()

class LocalSearchShowMapPointsCompleted(ServerBoundCommand):
    classIdentifier = "ShowMapPointsCompleted"
    groupIdentifier = "com.apple.ace.localsearch"
    def __init__(self, plist):
        self.aceId = None # @"NSString"
        self.refId = None # @"NSString"
        super(LocalSearchShowMapPointsCompleted, self).__init__(plist)


