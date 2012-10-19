from siriObjects.baseObjects import AceObject
from siriObjects.localsearchObjects import LocalSearchBusiness2
from siriObjects.uiObjects import UISirilandSnippet
class RestaurantOpening(AceObject):
    def __init__(self):
        super(RestaurantOpening, self).__init__("Opening", "com.apple.ace.restaurant")
        self.bookingId = None # @"NSURL"
        self.makeReservationPunchOut = None # @"SAUIAppPunchOut"
        self.partySize = None # @"NSNumber"
        self.timeSlot = None # @"SACalendar"

    def to_plist(self):
        self.add_property('bookingId')
        self.add_property('makeReservationPunchOut')
        self.add_property('partySize')
        self.add_property('timeSlot')
        return super(RestaurantOpening, self).to_plist()

class RestaurantRestaurant(LocalSearchBusiness2):
    def __init__(self):
        super(RestaurantRestaurant, self).__init__("Restaurant", "com.apple.ace.restaurant")
        self.attributeSet = None # @"NSArray"
        self.currencySymbol = None # @"NSString"
        self.makeReservationPunchOuts = None # @"NSArray"
        self.menuLink = None # @"NSURL"
        self.openings = None # @"NSArray"
        self.orderDeliveryPunchOuts = None # @"NSArray"
        self.priceRange = None # @"NSString"

    def to_plist(self):
        self.add_property('attributeSet')
        self.add_property('currencySymbol')
        self.add_property('makeReservationPunchOuts')
        self.add_property('menuLink')
        self.add_property('openings')
        self.add_property('orderDeliveryPunchOuts')
        self.add_property('priceRange')
        return super(RestaurantRestaurant, self).to_plist()

class RestaurantRestaurantsSnippet(UISirilandSnippet):
    def __init__(self):
        super(RestaurantRestaurantsSnippet, self).__init__("RestaurantsSnippet", "com.apple.ace.restaurant")
        self.attributionOrder = None # @"NSArray"
        self.contributingProviderIds = None # @"NSArray"
        self.providerPunchOutMap = None # @"NSDictionary"
        self.restaurants = None # @"NSArray"

    def to_plist(self):
        self.add_property('attributionOrder')
        self.add_property('contributingProviderIds')
        self.add_property('providerPunchOutMap')
        self.add_property('restaurants')
        return super(RestaurantRestaurantsSnippet, self).to_plist()