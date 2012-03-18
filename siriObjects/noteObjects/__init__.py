from siriObjects.baseObjects import ClientBoundCommand, AceObject

class NoteSnippet(AceObject):
    def __init__(self, notes=None, temporary=False, dialogPhase="Summary"):
        super(NoteSnippet, self).__init__("Snippet", "com.apple.ace.note")
        self.notes = notes if notes != None else []
        self.temporary = temporary
        self.dialogPhase = dialogPhase
    
    def to_plist(self):
        self.add_property('notes')
        self.add_property('temporary')
        self.add_property('dialogPhase')
        return super(NoteSnippet, self).to_plist()


class NoteObject(AceObject):
    def __init__(self, contents="", identifier=""):
        super(NoteObject, self).__init__("Object", "com.apple.ace.note")
        self.contents = contents
        self.identifier = identifier
    
    def to_plist(self):
        self.add_property('contents')
        self.add_property('identifier')
        return super(NoteObject, self).to_plist()