from siriObjects.baseObjects import ClientBoundCommand, ServerBoundCommand, AceObject
from siriObjects.systemObjects import DomainObject
from siriObjects.uiObjects import UISnippet


class AlarmObject(DomainObject):
    def __init__(self, label = None, minute = None, hour = None, frequency = None, enabled = None):
        super(AlarmObject, self).__init__("com.apple.ace.alarm")
        self.relativeOffsetMinutes = None
        self.label = label
        self.minute = minute
        self.hour = hour
        self.frequency = frequency
        self.enabled = 1
    
    def to_plist(self):
        self.add_property('relativeOffsetMinutes')
        self.add_property('minute')
        self.add_property('label')
        self.add_property('hour')
        self.add_property('frequency')
        self.add_property('enabled')
        return super(AlarmObject, self).to_plist()

class AlarmCreate(ClientBoundCommand):
    def __init__(self, refId, alarm = None):
        super(AlarmCreate, self).__init__("Create", "com.apple.ace.alarm", None, refId)      
        self.alarmToCreate = alarm
    
    def to_plist(self):
        self.add_property('alarmToCreate')
        return super(AlarmCreate, self).to_plist()

class AlarmCreateCompleted(ServerBoundCommand):
    classIdentifier = "CreateCompleted"
    groupIdentifier = "com.apple.ace.alarm"
    def __init__(self, plist):
        self.alarmId
        super(AlarmCreateCompleted, self).__init__(plist)

class AlarmDelete(ClientBoundCommand):
    def __init__(self, refId):
        super(AlarmDelete, self).__init__("Delete", "com.apple.ace.alarm", None, refId)
        self.alarmIds = None #array
        self.targetAppId = None

    def to_plist(self):
        self.add_property('alarmIds')
        self.add_property('targetAppId')
        return super(AlarmDelete, self).to_plist()


class AlarmDeleteCompleted(ServerBoundCommand):
    classIdentifier = "DeleteCompleted"
    groupIdentifier = "com.apple.ace.alarm"
    def __init__(self, plist):
        super(AlarmDeleteCompleted, self).__init__(plist)


class AlarmSearch(ClientBoundCommand):
    def __init__(self, refId):
        super(AlarmSearch, self).__init__("Search", "com.apple.ace.alarm", None, refId)
        self.minute = None # number
        self.label = None # string
        self.identifier = None #url
        self.hour = None #number
        self.frequency = None #array
        self.enabled = None # number
        self.targetAppId = None # url

    def to_plist(self):
        self.add_property('minute')
        self.add_property('label')
        self.add_property('identifier')
        self.add_property('hour')
        self.add_property('frequency')
        self.add_property('enabled')
        self.add_property('targetAppId')
        return super(AlarmSearch, self).to_plist()


class AlarmSearchCompleted(ServerBoundCommand):
    classIdentifier = "SearchCompleted"
    groupIdentifier = "com.apple.ace.alarm"
    def __init__(self, plist):
        self.results = None # array
        super(AlarmSearchCompleted, self).__init__(plist)


class AlarmSnippet(UISnippet):                
    def __init__(self, alarms = None):
        super(AlarmSnippet, self).__init__(group="com.apple.ace.alarm")
        self.alarms = alarms if alarms != None else []
    
    def to_plist(self):
        self.add_property('alarms')
        return super(AlarmSnippet, self).to_plist()
        
class AlarmUpdate(ClientBoundCommand):
    def __init__(self, refId):
        super(AlarmUpdate, self).__init__("Update", "com.apple.ace.alarm", None, refId)
        self.removedFrequency = None # array
        self.minute = None # number
        self.label = None #string
        self.hour = None # number
        self.enabled = None # number
        self.alarmId = None # url
        self.addedFrequency = None # array
        self.targetAppId = None # url

    def to_plist(self):
        self.add_property('removedFrequency')
        self.add_property('minute')
        self.add_property('label')
        self.add_property('hour')
        self.add_property('enabled')
        self.add_property('alarmId')
        self.add_property('addedFrequency')
        self.add_property('targetAppId')
        return super(AlarmUpdate, self).to_plist()

class AlarmUpdateCompleted(ServerBoundCommand):
    groupIdentifier = "com.apple.ace.alarm"
    classIdentifier = "UpdateCompleted"
    def __init__(self, plist):
        self.alarmId = None #url
        super(AlarmUpdateCompleted, self).__init__(plist)