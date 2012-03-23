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

