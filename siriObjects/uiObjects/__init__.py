from siriObjects.baseObjects import ClientBoundCommand, AceObject

class AddViews(ClientBoundCommand):
    def __init__(self, refId, scrollToTop=False, temporary=False, dialogPhase="Completion", views=None, callbacks=None):
        super(AddViews, self).__init__("AddViews", "com.apple.ace.assistant", None, refId, callbacks)
        self.scrollToTop = scrollToTop
        self.temporary = temporary
        self.dialogPhase = dialogPhase
        self.views = views if views != None else []
    
    def to_plist(self):
        self.add_property('scrollToTop')
        self.add_property('temporary')
        self.add_property('dialogPhase')
        self.add_property('views')
        return super(AddViews, self).to_plist()
    
class AceView(AceObject):
    def __init__(self, clazz, group):
        super(AceView, self).__init__(clazz, group)
        self.viewId = None # string
        self.speakableText = None # string
        self.listenAfterSpeaking = None # number

    def to_plist(self):
        self.add_property('viewId')
        self.add_property('speakableText')
        self.add_property('listenAfterSpeaking')
        return super(AceView, self).to_plist()


# Assistant-related objects
class AssistantUtteranceView(AceObject):
    def __init__(self, text="", speakableText="", dialogIdentifier="Misc#ident", listenAfterSpeaking=False):
        super(AssistantUtteranceView, self).__init__("AssistantUtteranceView", "com.apple.ace.assistant")
        self.text = text or speakableText
        self.speakableText = speakableText
        self.dialogIdentifier = dialogIdentifier
        self.listenAfterSpeaking = listenAfterSpeaking
    def to_plist(self):
        self.add_property('text')
        self.add_property('speakableText')
        self.add_property('dialogIdentifier')
        self.add_property('listenAfterSpeaking')
        return super(AssistantUtteranceView, self).to_plist()

class DisambiguationList(AceView):
    def __init__(self, items=None, speakableSelectionResponse="OK!", listenAfterSpeaking=True, speakableText="", speakableFinalDemitter="", speakableDemitter="", selectionResponse="OK!"):
        super(DisambiguationList, self).__init__("DisambiguationList", "com.apple.ace.assistant")
        self.items = items if items != None else []
        self.speakableSelectionResponse = speakableSelectionResponse
        self.listenAfterSpeaking = listenAfterSpeaking
        self.speakableFinalDemitter = speakableFinalDemitter
        self.selectionResponse = selectionResponse
        self.speakableText = speakableText

    def to_plist(self):
        self.add_property('items')
        self.add_property('speakableSelectionResponse')
        self.add_property('speakableFinalDemitter')
        self.add_property('selectionResponse')
        return super(DisambiguationList, self).to_plist()

class Button(AceObject):
    def __init__(self, text="", commands=None):
        super(Button, self).__init__("Button", "com.apple.ace.assistant")
        self.text = text
        self.commands = commands if commands != None else []

    def to_plist(self):
        self.add_property('text')
        self.add_property('commands')
        return super(Button, self).to_plist()

class OpenLink(AceObject):
    def __init__(self, ref=""):
        super(OpenLink, self).__init__("OpenLink", "com.apple.ace.assistant")
        self.ref = ref
    
    def to_plist(self):
        self.add_property('ref')
        return super(OpenLink, self).to_plist()


class HtmlView(AceObject):
    def __init__(self, html=""):
        super(HtmlView, self).__init__("HtmlView", "com.apple.ace.assistant")
        self.html = html
    
    def to_plist(self):
        self.add_property('html')
        return super(HtmlView, self).to_plist()

class MenuItem(AceObject):
    def __init__(self, title="", subtitle="", ref="", icon="", commands=None):
        super(MenuItem, self).__init__("MenuItem", "com.apple.ace.assistant")
        self.title = title
        self.subtitle = subtitle
        self.ref = ref
        self.icon = icon
        self.commands = commands if commands != None else []
    
    def to_plist(self):
        self.add_property('title')
        self.add_property('subtitle')
        self.add_property('ref')
        self.add_property('icon')
        self.add_property('commands')
        return super(MenuItem, self).to_plist()

class ListItem(AceView):
    def __init__(self, title="", selectionText="", commands=None, speakableText="", obj=None):
        super(ListItem, self).__init__("ListItem", "com.apple.ace.assistant")
        self.title= title
        self.selectionText = selectionText
        self.commands = commands if commands != None else []
        self.speakableText = speakableText
        self.object = obj

    def to_plist(self):
        self.add_property('title')
        self.add_property('selectionText')
        self.add_property('commands')
        self.add_property('object')
        return super(ListItem, self).to_plist()

class ConfirmationOptions(AceObject):
    def __init__(self, denyCommands=None, submitCommands=None, confirmText="Confirm", denyText="Cancel", cancelCommands=None, cancelLabel="Cancel", submitLabel="Confirm", confirmCommands=None, cancelTrigger="Deny"):
        super(ConfirmationOptions, self).__init__("ConfirmationOptions", "com.apple.ace.assistant")
        self.denyCommands = denyCommands if denyCommands != None else []
        self.submitCommands = submitCommands if submitCommands != None else []
        self.confirmText = confirmText
        self.denyText = denyText
        self.cancelCommands = cancelCommands if cancelCommands != None else []
        self.cancelLabel = cancelLabel
        self.submitLabel = submitLabel
        self.confirmCommands = confirmCommands if confirmCommands != None else []
        self.cancelTrigger = cancelTrigger
    
    def to_plist(self):
        self.add_property('denyCommands')
        self.add_property('submitCommands')
        self.add_property('confirmText')
        self.add_property('denyText')
        self.add_property('cancelCommands')
        self.add_property('cancelLabel')
        self.add_property('submitLabel')
        self.add_property('confirmCommands')
        self.add_property('cancelTrigger')
        return super(ConfirmationOptions, self).to_plist()

class CancelSnippet(AceObject):
    def __init__(self):
        super(CancelSnippet, self).__init__("CancelSnippet", "com.apple.ace.assistant")
    
class ConfirmSnippet(AceObject):
    def __init__(self):
        super(ConfirmSnippet, self).__init__("ConfirmSnippet", "com.apple.ace.assistant")

class Snippet(AceView):
    def __init__(self, group, clazz="Snippet"):
        super(Snippet, self).__init__(clazz, group)
        self.otherOptions = None # array
        self.confirmationOptions = None # ConfirmationOptions obj
    
    def to_plist(self):
        self.add_property('otherOptions')
        self.add_property('confirmationOptions')
        return super(Snippet, self).to_plist()


    
