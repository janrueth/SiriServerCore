from siriObjects.baseObjects import AceObject, ClientBoundCommand
from siriObjects.uiObjects import UISnippet
from siriObjects.systemObjects import DomainObject

class AnswerSnippet(UISnippet):
    def __init__(self, answers=None):
        super(AnswerSnippet, self).__init__(group="com.apple.ace.answer")
        self.answers = answers if answers != None else []

    def to_plist(self):
        self.add_property('answers')
        return super(AnswerSnippet, self).to_plist()

class AnswerObject(DomainObject):
    def __init__(self, title=None, lines=None):
        super(AnswerObject, self).__init__("com.apple.ace.answer")
        self.title = title
        self.lines = lines if lines != None else []

    def to_plist(self):
        self.add_property('title')
        self.add_property('lines')
        return super(AnswerObject, self).to_plist()

class AnswerObjectLine(AceObject):
    def __init__(self, text="", image=""):
        super(AnswerObjectLine, self).__init__("ObjectLine", "com.apple.ace.answer")
        self.text = text
        self.image = image

    def to_plist(self):
        self.add_property('text')
        self.add_property('image')
        return super(AnswerObjectLine, self).to_plist()
