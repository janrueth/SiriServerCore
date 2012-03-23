from siriObjects.baseObjects import ClientBoundCommand, ServerBoundCommand, AceObject
from siriObjects.uiObjects import UISnippet
from siriObjects.systemObjects import DomainObject


class ReminderPayload(AceObject):
    def __init__(self, clazz, group):
        super(ReminderPayload, self).__init__(clazz, group)

class ReminderTrigger(AceObject):
    def __init__(self, clazz="Trigger", group="com.apple.ace.reminder"):
        super(ReminderTrigger, self).__init__(clazz, group)
        
class ReminderAssistantPayload(ReminderPayload):
    def __init__(self):
        super(ReminderAssistantPayload, self).__init__("AssistantPayload", "com.apple.ace.reminder")
        self.utterance = None # string
        
    def to_plist(self):
        self.add_property('utterance')
        return super(ReminderAssistantPayload, self).to_plist()
    
class ReminderCompositeTrigger(ReminderTrigger):
    def __init__(self):
        super(ReminderCompositeTrigger, self).__init__("CompositeTrigger", "com.apple.ace.reminder")
        self.locationTrigger = None # ReminderLocationTrigger 
        self.dateTimeTrigger = None # ReminderDateTimeTrigger
        
    def to_plist(self):
        self.add_property('locationTrigger')
        self.add_property('dateTimeTrigger')
        return super(ReminderCompositeTrigger, self).to_plist()


class ReminderDateTimeTrigger(ReminderTrigger):
    def __init__(self):
        super(ReminderDateTimeTrigger, self).__init__("DateTimeTrigger", "com.apple.ace.reminder")
        self.timeZoneId = None # string
        self.relativeTimeOffset = None # reminderDateTimeTriggerOffset
        self.offset = None # reminderDateTimeTriggerOffset
        self.date = None #date
    
    def to_plist(self):
        self.add_property('timeZoneId')
        self.add_property('relativeTimeOffset')
        self.add_property('offset')
        self.add_property('date')
        return super(ReminderDateTimeTrigger, self).to_plist()


class ReminderDateTimeTriggerOffset(ReminderTrigger):
    TimeUnitDayValue = "Day"
    TimeUnitMonthValue = "Month"
    TimeUnitWeekValue = "Week"
    TimeUnitYearValue = "Year"
    TimeUnitHourValue = "Hour"
    TimeUnitMinuteValue = "Minute"
    TimeUnitSecondValue = "Second"
    
    def __init__(self):
        super(ReminderDateTimeTriggerOffset, self).__init__("DateTimeTriggerOffset", "com.apple.ace.reminder")
        self.offsetValue = None # number
        self.offsetTimeUnit = None # string
    
    def to_plist(self):
        self.add_property('offsetValue')
        self.add_property('offsetTimeUnit')
        return super(ReminderDateTimeTriggerOffset, self).to_plist() 
    
class ReminderEmailPayload(ReminderPayload):
    def __init__(self):
        super(ReminderEmailPayload, self).__init__("EmailPayload", "com.apple.ace.reminder")
        self.subject = None # string
        self.recipientsTo = None # array
        
    def to_plist(self):
        self.add_property('subject')
        self.add_property('recipientsTo')
        return super(ReminderEmailPayload, self).to_plist()
    
class ReminderListObject(DomainObject):
    def __init__(self):
        super(ReminderListObject, self).__init__("com.apple.ace.reminder", clazz="ListObject")
        self.name = None # string
    
    def to_plist(self):
        self.add_property('name')
        return super(ReminderListObject, self).to_plist()
    
class ReminderListSearch(ClientBoundCommand):
    def __init__(self, refId):
        super(ReminderListSearch, self).__init__("ListSearch", "com.apple.ace.reminder", None, refId)
        self.name = None
        self.targetAppId = None

    def to_plist(self):
        self.add_property('name')
        self.add_property('targetAppId')
        return super(ReminderListSearch, self).to_plist()
    
class ReminderListSearchCompleted(ServerBoundCommand):
    classIdentifier = "ListSearchCompleted"
    groupIdentifier = "com.apple.ace.reminder"
    
    def __init__(self, plist):
        self.results = None # array
        super(ReminderListSearchCompleted, self).__init(plist)
        
        
class ReminderLocationTrigger(ReminderTrigger):
    TimingOnArrivalValue = "OnArrival"
    TimingOnDepartureValue = "OnDeparture"
    
    def __init__(self):
        super(ReminderLocationTrigger, self).__init__("LocationTrigger", "com.apple.ace.reminder")
        self.timing = None # string
        self.location = None # systemObjects.Location
        self.contactIdentifier = None # url (string)
        
    def to_plist(self):
        self.add_property('timing')
        self.add_property('location')
        self.add_property('contactIdentifier')
        return super(ReminderLocationTrigger, self).to_plist()
    
class ReminderObject(DomainObject):
    def __init__(self):
        super(ReminderObject, self).__init__("com.apple.ace.reminder")
        self.trigger = None # ReminderTrigger
        self.subject = None # string
        self.recurrence = None # ReminderRecurrence
        self.payload = None # ReminderPayload
        self.lists = None # array
        self.important = None # bool
        self.dueDateTimeZoneId = None# string 
        self.dueDate = None # date
        self.completed = None # bool
        self.alternateSubject = None # string
    
    def to_plist(self):
        self.add_property('trigger')
        self.add_property('subject')
        self.add_property('recurrence')
        self.add_property('payload')
        self.add_property('lists')
        self.add_property('important')
        self.add_property('dueDateTimeZoneId') 
        self.add_property('dueDate')
        self.add_property('completed')
        self.add_property('alternateSubject')
        return super(ReminderObject, self).to_plist()
    

class ReminderPhonePayload(ReminderPayload):
    def __init__(self):
        super(ReminderPhonePayload, self).__init__("PhonePayload", "com.apple.ace.reminder")
        self.recipient = None
        
    def to_plist(self):
        self.add_property('recipient')
        return super(ReminderPhonePayload, self).to_plist()
 

class ReminderRecurrence(AceObject):
    DayOfWeekSundayValue = "Sunday"
    DayOfWeekMondayValue = "Monday"
    DayOfWeekTuesdayValue = "Tuesday"
    DayOfWeekWednesdayValue = "Wednesday"
    DayOfWeekThursdayValue = "Thursday"
    DayOfWeekFridayValue = "Friday"
    DayOfWeekSaturdayValue = "Saturday"
    
    def __init__(self):
        super(ReminderRecurrence, self).__init__("Recurrence", "com.apple.ace.reminder")
        self.weeksOfTheYear = None # array
        self.monthOfTheYear = None # array
        self.interval = None # int
        self.frequencyTimeUnit = None # string
        self.daysOfTheYear = None # array
        self.daysOfTheWeek = None # array
        self.daysOfTheMonth = None # array
        
    def to_plist(self):
        self.add_property("weeksOfTheYear")
        self.add_property("monthOfTheYear")
        self.add_property("interval")
        self.add_property("frequencyTimeUnit")
        self.add_property("daysOfTheYear")
        self.add_property("daysOfTheWeek")
        self.add_property("daysOfTheMonth")
        return super(ReminderRecurrence, self).to_plist()


class ReminderSearch(ClientBoundCommand):
    def __init__(self, refId):
        super(ReminderSearch, self).__init__(self, "Search", "com.apple.ace.reminder", None, refId)
        self.timeZoneId = None # string
        self.subject = None # string
        self.listName = None # string
        self.dueBefore = None # date
        self.dueAfter = None # date
        self.completionStatus = None # number
        self.targetAppId = None # url (string)
        
    def to_plist(self):
        self.add_property('timeZoneId')
        self.add_property('subject')
        self.add_property('listName')
        self.add_property('dueBefore')
        self.add_property('dueAfter')
        self.add_property('completionStatus')
        self.add_property('targetAppId')
        return super(ReminderSearch, self).to_plist()

class ReminderSearchCompleted(ServerBoundCommand):
    classIdentifier = "SearchCompleted"
    groupIdentifier = "com.apple.ace.reminder"   
    
    def __init__(self, plist):
        self.results = None # array
        super(ReminderSearchCompleted, self).__init__(plist)
        

class ReminderSmsPayload(ReminderPayload):
    def __init__(self):
        super(ReminderSmsPayload, self).__init("SmsPayload", "com.apple.ace.reminder")
        self.recipients = None # array
        self.message = None # string
        
    def to_plist(self):
        self.add_property('recipients')
        self.add_property('message')
        return super(ReminderSmsPayload, self).to_plist()
         
class ReminderSnippet(UISnippet):
    def __init__(self):
        super(ReminderSnippet, self).__init__(group="com.apple.ace.reminder")
        self.reminders = None # array
    
    def to_plist(self):
        self.add_property('reminders')
        return super(ReminderSnippet, self).to_plist()
        