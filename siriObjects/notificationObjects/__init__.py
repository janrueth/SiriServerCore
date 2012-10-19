from siriObjects.systemObjects import DomainObject

class NotificationObject(DomainObject):
    def __init__(self):
        super(NotificationObject, self).__init__("Object", "com.apple.ace.notification")
        self.applicationId = None # @"NSString"
        self.date = None # @"NSDate"
        self.dateIsAllDay = None # @"NSNumber"
        self.endDate = None # @"NSDate"
        self.recencyDate = None # @"NSDate"
        self.timeZoneId = None # @"NSString"
        self.type = None # @"NSString"

    def to_plist(self):
        self.add_property('applicationId')
        self.add_property('date')
        self.add_property('dateIsAllDay')
        self.add_property('endDate')
        self.add_property('recencyDate')
        self.add_property('timeZoneId')
        self.add_property('type')
        return super(NotificationObject, self).to_plist()
