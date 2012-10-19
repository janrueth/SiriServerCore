from siriObjects.baseObjects import ClientBoundCommand, AceObject, \
    ServerBoundCommand
from siriObjects.systemObjects import AceView



class UISnippetInteraction(ServerBoundCommand):
    classIdentifier = "SnippetInteraction"
    groupIdentifier = "com.apple.ace.assistant"
    def __init__(self, plist):
        self.requestId = None # @"NSString"
        self.snippetId = None # @"NSString"
        super(UISnippetInteraction, self).__init__(plist)
        
class UISnippetObjectInteraction(UISnippetInteraction):
    classIdentifier = "SnippetObjectInteraction"
    groupIdentifier = "com.apple.ace.assistant"
    def __init__(self, plist):
        self.object = None # @"SADomainObject"
        super(UISnippetObjectInteraction, self).__init__(plist)
        
class UISnippet(AceView):
    def __init__(self, clazz="Snippet", group="com.apple.ace.assistant"):
        super(UISnippet, self).__init__(clazz, group)
        self.confirmationOptions = None # @"SAUIConfirmationOptions"
        self.otherOptions = None # @"NSArray"

    def to_plist(self):
        self.add_property('confirmationOptions')
        self.add_property('otherOptions')
        return super(UISnippet, self).to_plist()
        

class UIAddViews(ClientBoundCommand):
    DialogPhaseAcknowledgementValue = "Acknowledgement"
    DialogPhaseReflectionValue = "Reflection"
    DialogPhaseStatusValue = "Status"
    DialogPhaseClarificationValue = "Clarification"
    DialogPhaseSummaryValue = "Summary"
    DialogPhaseConfirmationValue = "Confirmation"
    DialogPhaseCompletionValue = "Completion"
    DialogPhaseErrorValue = "Error"
    DialogPhaseConfirmedValue = "Confirmed"
    DialogPhaseCanceledValue = "Canceled"
    
    def __init__(self, refId):
        super(UIAddViews, self).__init__("AddViews", "com.apple.ace.assistant", None, refId)
        self.dialogPhase = None # @"NSString"
        self.scrollToTop = None # BOOL
        self.temporary = None # BOOL
        self.views = None # @"NSArray"


    def to_plist(self):
        self.add_property('dialogPhase')
        self.add_property('scrollToTop')
        self.add_property('temporary')
        self.add_property('views')
        return super(UIAddViews, self).to_plist()

class UIAssistantUtteranceView(AceView):
    def __init__(self):
        super(UIAssistantUtteranceView, self).__init__("AssistantUtteranceView", "com.apple.ace.assistant")
        self.dialogIdentifier = None # @"NSString"
        self.text = None # @"NSString"

    def to_plist(self):
        self.add_property('dialogIdentifier')
        self.add_property('text')
        return super(UIAssistantUtteranceView, self).to_plist()

class UIButton(AceView):
    def __init__(self):
        super(UIButton, self).__init__("Button", "com.apple.ace.assistant")
        self.commands = None # @"NSArray"
        self.text = None # @"NSString"

    def to_plist(self):
        self.add_property('commands')
        self.add_property('text')
        return super(UIButton, self).to_plist()

class UICancelSnippet(UISnippetInteraction):
    classIdentifier = "CancelSnippet"
    groupIdentifier = "com.apple.ace.assistant"
    def __init__(self, plist):
        super(UICancelSnippet, self).__init__(plist)

class UIClearScreen(ClientBoundCommand):
    def __init__(self, refId):
        super(UIClearScreen, self).__init__("ClearScreen", "com.apple.ace.assistant", None, refId)
        self.initialView = None # @"SAAceView"

    def to_plist(self):
        self.add_property('initialView')
        return super(UIClearScreen, self).to_plist()


class UICloseAssistant(ClientBoundCommand):
    def __init__(self, refId):
        super(UICloseAssistant, self).__init__("CloseAssistant", "com.apple.ace.assistant", None, refId)

    def to_plist(self):
        return super(UICloseAssistant, self).to_plist()


class UIConfirmationOptions(AceObject):
    CancelTriggerConfirmValue = "Confirm"
    CancelTriggerDenyValue = "Deny"
    CancelTriggerNoneValue = "None"
    
    def __init__(self):
        super(UIConfirmationOptions, self).__init__("ConfirmationOptions", "com.apple.ace.assistant")
        self.cancelCommands = None # @"NSArray"
        self.cancelLabel = None # @"NSString"
        self.cancelTrigger = None # @"NSString"
        self.confirmCommands = None # @"NSArray"
        self.confirmText = None # @"NSString"
        self.denyCommands = None # @"NSArray"
        self.denyText = None # @"NSString"
        self.submitCommands = None # @"NSArray"
        self.submitLabel = None # @"NSString"

    def to_plist(self):
        self.add_property('cancelCommands')
        self.add_property('cancelLabel')
        self.add_property('cancelTrigger')
        self.add_property('confirmCommands')
        self.add_property('confirmText')
        self.add_property('denyCommands')
        self.add_property('denyText')
        self.add_property('submitCommands')
        self.add_property('submitLabel')
        return super(UIConfirmationOptions, self).to_plist()


class UIConfirmationView(AceView):
    CancelTriggerConfirmValue = "Confirm"
    CancelTriggerDenyValue = "Deny"
    CancelTriggerNoneValue = "None"
    
    def __init__(self):
        super(UIConfirmationView, self).__init__("ConfirmationView", "com.apple.ace.assistant")
        self.cancelTrigger = None # @"NSString"
        self.confirmCommands = None # @"NSArray"
        self.confirmText = None # @"NSString"
        self.denyCommands = None # @"NSArray"
        self.denyText = None # @"NSString"

    def to_plist(self):
        self.add_property('cancelTrigger')
        self.add_property('confirmCommands')
        self.add_property('confirmText')
        self.add_property('denyCommands')
        self.add_property('denyText')
        return super(UIConfirmationView, self).to_plist()


class UIConfirmSnippet(UISnippetInteraction):
    classIdentifier = "ConfirmSnippet"
    groupIdentifier = "com.apple.ace.assistant"
    def __init__(self, plist):
        super(UIConfirmSnippet, self).__init__(plist)


class UIDisambiguationList(AceView):
    def __init__(self):
        super(UIDisambiguationList, self).__init__("DisambiguationList", "com.apple.ace.assistant")
        self.disambiguationKey = None # @"NSString"
        self.items = None # @"NSArray"
        self.selectionResponse = None # @"NSString"
        self.speakableDelimiter = None # @"NSString"
        self.speakableFinalDelimiter = None # @"NSString"
        self.speakableSelectionResponse = None # @"NSString"
        self.speakableSuffix = None # @"NSString"

    def to_plist(self):
        self.add_property('disambiguationKey')
        self.add_property('items')
        self.add_property('selectionResponse')
        self.add_property('speakableDelimiter')
        self.add_property('speakableFinalDelimiter')
        self.add_property('speakableSelectionResponse')
        self.add_property('speakableSuffix')
        return super(UIDisambiguationList, self).to_plist()

class UIErrorSnippet(UISnippet):
    def __init__(self):
        super(UIErrorSnippet, self).__init__("ErrorSnippet", "com.apple.ace.assistant")
        self.message = None # @"NSString"

    def to_plist(self):
        self.add_property('message')
        return super(UIErrorSnippet, self).to_plist()

class UIHtmlView(AceView):
    def __init__(self):
        super(UIHtmlView, self).__init__("HtmlView", "com.apple.ace.assistant")
        self.html = None # @"NSString"

    def to_plist(self):
        self.add_property('html')
        return super(UIHtmlView, self).to_plist()

class UIListItem(AceView):
    def __init__(self):
        super(UIListItem, self).__init__("ListItem", "com.apple.ace.assistant")
        self.commands = None # @"NSArray"
        self.object = None # 
        self.selectionResponse = None # @"NSString"
        self.selectionText = None # @"NSString"
        self.speakableSelectionResponse = None # @"NSString"
        self.title = None # @"NSString"

    def to_plist(self):
        self.add_property('commands')
        self.add_property('object')
        self.add_property('selectionResponse')
        self.add_property('selectionText')
        self.add_property('speakableSelectionResponse')
        self.add_property('title')
        return super(UIListItem, self).to_plist()
    

class UIMenuItem(AceView):
    def __init__(self):
        super(UIMenuItem, self).__init__("MenuItem", "com.apple.ace.assistant")
        self.commands = None # @"NSArray"
        self.icon = None # @"NSURL"
        self.ref = None # @"NSURL"
        self.subtitle = None # @"NSString"
        self.title = None # @"NSString"

    def to_plist(self):
        self.add_property('commands')
        self.add_property('icon')
        self.add_property('ref')
        self.add_property('subtitle')
        self.add_property('title')
        return super(UIMenuItem, self).to_plist()

class UIOpenLink(ClientBoundCommand):
    def __init__(self, refId):
        super(UIOpenLink, self).__init__("OpenLink", "com.apple.ace.assistant", None, refId)
        self.ref = None # @"NSURL"   

    def to_plist(self):
        self.add_property('ref')
        return super(UIOpenLink, self).to_plist()

class UIRepeatIt(ClientBoundCommand):
    def __init__(self, refId):
        super(UIRepeatIt, self).__init__("RepeatIt", "com.apple.ace.assistant", None, refId)
        self.contingency = None # @"NSString"
   
    def to_plist(self):
        self.add_property('contingency')
        return super(UIRepeatIt, self).to_plist()

class UISayIt(ClientBoundCommand):
    def __init__(self, refId):
        super(UISayIt, self).__init__("SayIt", "com.apple.ace.assistant", None, refId)
        self.context = None # 
        self.message = None # @"NSString"  

    def to_plist(self):
        self.add_property('context')
        self.add_property('message')
        return super(UISayIt, self).to_plist()

class UIShowHelp(ClientBoundCommand):
    def __init__(self, refId):
        super(UIShowHelp, self).__init__("ShowHelp", "com.apple.ace.assistant", None, refId)
        self.speakableText = None # @"NSString"
        self.text = None # @"NSString"

    def to_plist(self):
        self.add_property('speakableText')
        self.add_property('text')
        return super(UIShowHelp, self).to_plist()

class UISnippetAttributeOpened(UISnippetInteraction):
    classIdentifier = "SnippetAttributeOpened"
    groupIdentifier = "com.apple.ace.assistant"
    def __init__(self, plist):
        self.attributeName = None # @"NSString"
        self.attributeValue = None # @"NSString"
        super(UISnippetAttributeOpened, self).__init__(plist)

class UISnippetEdited(UISnippetObjectInteraction):
    classIdentifier = "SnippetEdited"
    groupIdentifier = "com.apple.ace.assistant"
    def __init__(self, plist):
        super(UISnippetEdited, self).__init__(plist)

class UISnippetExpanded(UISnippetObjectInteraction):
    classIdentifier = "SnippetExpanded"
    groupIdentifier = "com.apple.ace.assistant"
    def __init__(self, plist):
        super(UISnippetExpanded, self).__init__(plist)

class UISnippetList(AceView):
    def __init__(self):
        super(UISnippetList, self).__init__("SnippetList", "com.apple.ace.assistant")
        self.headerView = None # @"SAAceView"
        self.items = None # @"NSArray"

    def to_plist(self):
        self.add_property('headerView')
        self.add_property('items')
        return super(UISnippetList, self).to_plist()

class UISnippetOpened(UISnippetObjectInteraction):
    classIdentifier = "SnippetOpened"
    groupIdentifier = "com.apple.ace.assistant"
    def __init__(self, plist):
        super(UISnippetOpened, self).__init__(plist)

class UIUnlockDevice(ClientBoundCommand):
    def __init__(self, refId):
        super(UIUnlockDevice, self).__init__("UnlockDevice", "com.apple.ace.assistant", None, refId)
        self.cancellationCommands = None # @"NSArray"
        self.failureCommands = None # @"NSArray"
        self.successCommands = None # @"NSArray"  

    def to_plist(self):
        self.add_property('cancellationCommands')
        self.add_property('failureCommands')
        self.add_property('successCommands')
        return super(UIUnlockDevice, self).to_plist()

class UIUserUtteranceView(AceView):
    def __init__(self):
        super(UIUserUtteranceView, self).__init__("UserUtteranceView", "com.apple.ace.assistant")
        self.text = None # @"NSString"

    def to_plist(self):
        self.add_property('text')
        return super(UIUserUtteranceView, self).to_plist()





########################################################
# The method below are deprecated you should not use them in new code
####

# this is just a shortcut for UIAddViews
class AddViews(UIAddViews):
    def __init__(self, refId, scrollToTop=False, temporary=False, dialogPhase="Completion", views=None, callbacks=None):
        super(AddViews, self).__init__(refId)
        self.scrollToTop = scrollToTop
        self.temporary = temporary
        self.dialogPhase = dialogPhase
        self.views = views if views != None else []
    
    def to_plist(self):
        return super(AddViews, self).to_plist()


# This is just a shortcut for UIAssistantUtteranceView
class AssistantUtteranceView(UIAssistantUtteranceView):
    def __init__(self, text="", speakableText="", dialogIdentifier="Misc#ident", listenAfterSpeaking=False):
        super(AssistantUtteranceView, self).__init__()
        self.text = text or speakableText
        self.speakableText = speakableText
        self.dialogIdentifier = dialogIdentifier
        self.listenAfterSpeaking = listenAfterSpeaking
        
    def to_plist(self):
        return super(AssistantUtteranceView, self).to_plist()

# This is just a shortcut for UI.... if you code something new use the UI version
class DisambiguationList(UIDisambiguationList):
    def __init__(self, items=None, speakableSelectionResponse="OK!", listenAfterSpeaking=True, speakableText="", speakableFinalDemitter="", speakableDemitter="", selectionResponse="OK!"):
        super(DisambiguationList, self).__init__()
        self.items = items if items != None else []
        self.speakableSelectionResponse = speakableSelectionResponse
        self.listenAfterSpeaking = listenAfterSpeaking
        self.speakableFinalDemitter = speakableFinalDemitter
        self.selectionResponse = selectionResponse
        self.speakableText = speakableText

    def to_plist(self):
        return super(DisambiguationList, self).to_plist()

# This is just a shortcut for UI.... if you code something new use the UI version
class Button(UIButton):
    def __init__(self, text="", commands=None):
        super(Button, self).__init__()
        self.text = text
        self.commands = commands if commands != None else []

    def to_plist(self):
        return super(Button, self).to_plist()

# This is just a shortcut for UI.... if you code something new use the UI version
class OpenLink(UIOpenLink):
    def __init__(self, ref=""):
        super(OpenLink, self).__init__()
        self.ref = ref
    
    def to_plist(self):
        return super(OpenLink, self).to_plist()

# This is just a shortcut for UI.... if you code something new use the UI version
class HtmlView(UIHtmlView):
    def __init__(self, html=""):
        super(HtmlView, self).__init__()
        self.html = html
    
    def to_plist(self):
        return super(HtmlView, self).to_plist()

# This is just a shortcut for UI.... if you code something new use the UI version
class MenuItem(UIMenuItem):
    def __init__(self, title="", subtitle="", ref="", icon="", commands=None):
        super(MenuItem, self).__init__()
        self.title = title
        self.subtitle = subtitle
        self.ref = ref
        self.icon = icon
        self.commands = commands if commands != None else []
    
    def to_plist(self):
        return super(MenuItem, self).to_plist()

# This is just a shortcut for UI.... if you code something new use the UI version
class ListItem(UIListItem):
    def __init__(self, title="", selectionText="", commands=None, speakableText="", obj=None):
        super(ListItem, self).__init__()
        self.title = title
        self.selectionText = selectionText
        self.commands = commands if commands != None else []
        self.speakableText = speakableText
        self.object = obj

    def to_plist(self):
        return super(ListItem, self).to_plist()

# This is just a shortcut for UI.... if you code something new use the UI version
class ConfirmationOptions(UIConfirmationOptions):
    def __init__(self, denyCommands=None, submitCommands=None, confirmText="Confirm", denyText="Cancel", cancelCommands=None, cancelLabel="Cancel", submitLabel="Confirm", confirmCommands=None, cancelTrigger="Deny"):
        super(ConfirmationOptions, self).__init__()
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
        return super(ConfirmationOptions, self).to_plist()

# This is just a shortcut for UI.... if you code something new use the UI version
class CancelSnippet(UICancelSnippet):
    def __init__(self):
        super(CancelSnippet, self).__init__()
        
# This is just a shortcut for UI.... if you code something new use the UI version    
class ConfirmSnippet(UIConfirmSnippet):
    def __init__(self):
        super(ConfirmSnippet, self).__init__()

# This is just a shortcut for UI.... if you code something new use the UI version
class Snippet(UISnippet):
    def __init__(self, group, clazz="Snippet"):
        super(Snippet, self).__init__(clazz, group)
        self.otherOptions = None # array
        self.confirmationOptions = None # ConfirmationOptions obj
    
    def to_plist(self):
        return super(Snippet, self).to_plist()
    
    
    
## IOS 6 stuff

class UIAppPunchOut(ClientBoundCommand):
    def __init__(self, refId):
        super(UIAppPunchOut, self).__init__("AppPunchOut", "com.apple.ace.assistant", None, refId)
        self.alternativePunchOut = None # @"SAUIAddViews"
        self.appDisplayName = None # @"NSString"
        self.appIcon = None # @"SAUIImageResource"
        self.appIconMap = None # @"NSDictionary"
        self.appInstalled = None # c
        self.appStoreUri = None # @"NSURL"
        self.bundleId = None # @"NSString"
        self.providerId = None # @"NSString"
        self.punchOutName = None # @"NSString"
        self.punchOutUri = None # @"NSURL"


    def to_plist(self):
        self.add_property('alternativePunchOut')
        self.add_property('appDisplayName')
        self.add_property('appIcon')
        self.add_property('appIconMap')
        self.add_property('appInstalled')
        self.add_property('appStoreUri')
        self.add_property('bundleId')
        self.add_property('providerId')
        self.add_property('punchOutName')
        self.add_property('punchOutUri')
        return super(UIAppPunchOut, self).to_plist()


class UIImageResource(AceObject):
    def __init__(self):
        super(UIImageResource, self).__init__("ImageResource", "com.apple.ace.assistant")
        self.pointHeight = None # d
        self.pointWidth = None # d
        self.resourceUrl = None # @"NSURL"
        self.scaleFactor = None # d

    def to_plist(self):
        self.add_property('pointHeight')
        self.add_property('pointWidth')
        self.add_property('resourceUrl')
        self.add_property('scaleFactor')
        return super(UIImageResource, self).to_plist()


class UIRequestUpdateViews(ClientBoundCommand):
    def __init__(self, refId):
        super(UIRequestUpdateViews, self).__init__("RequestUpdateViews", "com.apple.ace.assistant", None, refId)
        self.commands = None # @"NSArray"
        self.timeInSeconds = None # @"NSNumber"
        self.viewIds = None # @"NSArray"


    def to_plist(self):
        self.add_property('commands')
        self.add_property('timeInSeconds')
        self.add_property('viewIds')
        return super(UIRequestUpdateViews, self).to_plist()


class UISirilandSnippet(UISnippet):
    def __init__(self):
        super(UISirilandSnippet, self).__init__("SirilandSnippet", "com.apple.ace.assistant")
        self.navigationPath = None # @"NSString"

    def to_plist(self):
        self.add_property('navigationPath')
        return super(UISirilandSnippet, self).to_plist()



class UIUpdateViews(ClientBoundCommand):
    def __init__(self, refId):
        super(UIUpdateViews, self).__init__("UpdateViews", "com.apple.ace.assistant", None, refId)
        self.views = None # @"NSArray"


    def to_plist(self):
        self.add_property('views')
        return super(UIUpdateViews, self).to_plist()

