from siriObjects.baseObjects import ClientBoundCommand, AceObject, ServerBoundCommand
from siriObjects.systemObjects import SendCommands, StartRequest, DomainObject
from siriObjects.uiObjects import ConfirmationOptions, UISnippet

class TimerGet(ClientBoundCommand):
    def __init__(self, refId):
        super(TimerGet, self).__init__("Get", "com.apple.ace.timer", None, refId)
    
    def to_plist(self):
        return super(TimerGet, self).to_plist()

class TimerGetCompleted(ServerBoundCommand):
    classIdentifier = "GetCompleted"
    groupIdentifier = "com.apple.ace.timer"
    def __init__(self, plist):
        self.timer = None # TimerObject
        super(TimerGetCompleted, self).__init__(plist)


class TimerSet(ClientBoundCommand):
    def __init__(self, refId, timer = None):
        super(TimerSet, self).__init__("Set", "com.apple.ace.timer", None, refId)
        self.timer = timer
    
    def to_plist(self):
        self.add_property("timer")
        return super(TimerSet, self).to_plist()

class TimerSetCompleted(ServerBoundCommand):
    classIdentifier = "SetCompleted"
    groupIdentifier = "com.apple.ace.timer"
    def __init__(self, plist):
        super(TimerSetCompleted, self).__init__(plist)

class TimerCancel(ClientBoundCommand):
    def __init__(self, refId):
        super(TimerCancel, self).__init__("Cancel", "com.apple.ace.timer", None, refId)
           
    def to_plist(self):
        return super(TimerCancel, self).to_plist()

class TimerCancelCompleted(ServerBoundCommand):
    classIdentifier = "CancelCompleted"
    groupIdentifier = "com.apple.ace.timer"
    def __init__(self, plist):
        self.timer = None # timer object
        super(TimerCancelCompleted, self).__init__(plist)



class TimerPause(ClientBoundCommand):
    def __init__(self, refId):
        super(TimerPause, self).__init__("Pause", "com.apple.ace.timer", None, refId)
           
    def to_plist(self):
        return super(TimerPause, self).to_plist()

class TimerPauseCompleted(ServerBoundCommand):
    classIdentifier = "PauseCompleted"
    groupIdentifier = "com.apple.ace.timer"
    def __init__(self, plist):
        super(TimerPauseCompleted, self).__init__(plist)


class TimerResume(ClientBoundCommand):
    def __init__(self, refId):
        super(TimerResume, self).__init__("Resume", "com.apple.ace.timer", None, refId)
           
    def to_plist(self):
        return super(TimerResume, self).to_plist()

class TimerResumeCompleted(ServerBoundCommand):
    classIdentifier = "ResumeCompleted"
    groupIdentifier = "com.apple.ace.timer"
    def __init__(self, plist):
        super(TimerResumeCompleted, self).__init__(plist)

class TimerSnippet(UISnippet):                
    def __init__(self, timers = None, confirm = False):
        super(TimerSnippet, self).__init__(group="com.apple.ace.timer")
        self.timers = timers if timers != None else []
        if confirm:
            self.confirmationOptions = ConfirmationOptions(
                    submitCommands = [SendCommands([StartRequest(utterance="^timerConfirmation^=^yes^ ^timerVerb^=^set^ ^timerNoun^=^timer^")])],
                    cancelCommands = [SendCommands([StartRequest(utterance="^timerConfirmation^=^no^ ^timerVerb^=^set^ ^timerNoun^=^timer^")])],
                    denyCommands = [SendCommands([StartRequest(utterance="^timerConfirmation^=^no^ ^timerVerb^=^set^ ^timerNoun^=^timer^")])],
                    confirmCommands = [SendCommands([StartRequest(utterance="^timerConfirmation^=^yes^ ^timerVerb^=^set^ ^timerNoun^=^timer^")])],
                    denyText = "Keep it",
                    cancelLabel = "Keep it",
                    submitLabel = "Change it",
                    confirmText = "Change it",
                    cancelTrigger = "Confirm")
        else:
            self.confirmationOptions = None
    
    def to_plist(self):
        self.add_property('timers')
        return super(TimerSnippet, self).to_plist()

class TimerObject(DomainObject):
    def __init__(self, timerValue = None, state = None):
        super(TimerObject, self).__init__("com.apple.ace.timer")
        self.timerValue = timerValue #number 
        self.state = state #string
    
    def to_plist(self):
        self.add_property('timerValue')
        self.add_property('state')
        return super(TimerObject, self).to_plist()
