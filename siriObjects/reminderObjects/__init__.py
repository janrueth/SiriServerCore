from siriObjects.baseObjects import ClientBoundCommand, AceObject

class ReminderSnippet(AceObject):
    def __init__(self, reminders=None, temporary=False, dialogPhase="Confirmation"):
        super(ReminderSnippet, self).__init__("Snippet", "com.apple.ace.reminder")
        self.reminders = reminders if reminders != None else []
        self.temporary = temporary
        self.dialogPhase = dialogPhase
    
    def to_plist(self):
        self.add_property('reminders')
        self.add_property('temporary')
        self.add_property('dialogPhase')
        return super(ReminderSnippet, self).to_plist()


class ReminderObject(AceObject):
    def __init__(self, dueDateTimeZoneId="America/Chicago", dueDate=None, completed=False, lists=None, trigger=None, subject="", important=False, identifier=""):
        super(ReminderObject, self).__init__("Object", "com.apple.ace.reminder")
        self.dueDateTimeZoneId = dueDateTimeZoneId
        self.dueDate = dueDate
        self.completed = completed
        self.lists = lists if lists != None else []
        self.trigger = trigger if trigger != None else []
        self.subject = subject
        self.important = important
        self.identifier = identifier
    
    def to_plist(self):
        self.add_property('dueDateTimeZoneId')
        self.add_property('dueDate')
        self.add_property('completed')
        self.add_property('lists')
        self.add_property('trigger')
        self.add_property('subject')
        self.add_property('important')
        self.add_property('identifier')
        return super(ReminderObject, self).to_plist()


class ListObject(AceObject):
    def __init__(self, name = "Tasks"):
        super(ListObject, self).__init__("ListObject", "com.apple.ace.reminder")
        self.name = name
    
    def to_plist(self):
        self.add_property('name')
        return super(ListObject, self).to_plist()


class DateTimeTrigger(AceObject):
    def __init__(self, date=None):
        super(DateTimeTrigger, self).__init__("DateTimeTrigger", "com.apple.ace.reminder")
        self.date = date
    
    def to_plist(self):
        self.add_property('date')
        return super(DateTimeTrigger, self).to_plist()

