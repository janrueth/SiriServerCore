#!/usr/bin/python
# -*- coding: utf-8 -*-



from siriObjects.baseObjects import ClientBoundCommand, RequestCompleted
from siriObjects.systemObjects import GetRequestOrigin, SetRequestOrigin
from siriObjects.uiObjects import UIAddViews, UIAssistantUtteranceView, \
    UIOpenLink, UIButton
import PluginManager
import contextlib
import inspect
import logging
import re
import threading
import urllib2



__criteria_key__ = "criterias"


__error_responses__ = {
    "de-DE": "Es ist ein Fehler in der Verarbeitung ihrer Anfrage aufgetreten!",
    "en-US": "There was an error during the processing of your request!",
    "en-GB": "There was an error during the processing of your request!",
    "en-AU": "There was an error during the processing of your request!",
    "fr-FR": "Il y avait une erreur lors du traitement de votre demande!",
    "nl-NL": u"Er is een fout opgetreden tijdens de verwerking van uw aanvraag!",
}

__error_location_help__ = {
    "de-DE": u"Ich weiß nicht wo du bist… Aber du kannst mir helfen es heraus zu finden…",
    "en-US": u"I don’t know where you are… But you can help me find out…",
    "en-GB": u"I don’t know where you are… But you can help me find out…",
    "en-AU": u"I don’t know where you are… But you can help me find out…",
    "fr-FR": u"Je ne sais pas où vous êtes ... Mais vous pouvez m'aider à en savoir plus sur ...",
    "nl-NL": u"Ik weet niet waar je bent… Maar je kunt me helpen erachter te komen…",
}

__error_location_saysettings__ = {
    "de-DE": u"In den Ortungsdienst Einstellungen, schalte Ortungsdienst und Siri ein.",
    "en-US": u"In Location Services Settings, turn on both Location Services and Siri.",
    "en-GB": u"In Location Services Settings, turn on both Location Services and Siri.",
    "en-AU": u"In Location Services Settings, turn on both Location Services and Siri.",
    "fr-FR": u"Dans les paramètres de service de localisation, activez les services de localisation et Siri.",
    "nl-NL": u"In locatievoorzieningen instellingen, zet locatievoorzieningen en Siri aan."
}

__error_location_settings__ = {
    "de-DE": u"Ortungsdienst Einstellungen",
    "en-US": u"Location Services Settings",
    "en-GB": u"Location Services Settings",
    "en-AU": u"Location Services Settings",
    "fr-FR": u"Services de localisation",
    "nl-NL": u"Locatievoorzieningen Instellingen",
}



def register(lang, regex):
    def addInfosTo(func):
        if not __criteria_key__ in func.__dict__:
            func.__dict__[__criteria_key__] = dict()
        crits = func.__dict__[__criteria_key__]
        crits[lang] = re.compile(regex, re.IGNORECASE | re.UNICODE)
        return func
    return addInfosTo

class StopPluginExecution(Exception):
    def __init__(self, reason):
        self.reason = reason
    def __str__(self):
        return repr(self.reason)

class ApiKeyNotFoundException(Exception):
    def __init__(self, reason):
        self.reason = reason
    def __str__(self):
        return repr(self.reason)

class NecessaryModuleNotFound(Exception):
    def __init__(self, reason):
        self.reason = reason
    def __str__(self):
        return repr(self.reason)

def APIKeyForAPI(apiName):
    apiKey = PluginManager.getAPIKeyForAPI(apiName)
    if apiKey == None or apiKey == "":
        raise ApiKeyNotFoundException("Could not find API key for: "+ apiName + ". Please check your " + PluginManager.__apikeys_file__)
    return apiKey


def getWebsite(url, timeout=5):
    '''
        This method retrieved the website at the url encoded url
        if this method fails to retrieve the website with the given timeout
        or anything else, None is returned
    '''
    try:
        with contextlib.closing(urllib2.urlopen(url, timeout=timeout)) as page:
            body = page.read()
            return body
    except:
        pass
    return None

class Plugin(threading.Thread):
    def __init__(self):
        super(Plugin, self).__init__()
        self.__method = None
        self.__lang = None
        self.__speech = None
        self.waitForResponse = None
        self.response = None
        self.refId = None
        self.connection = None
        self.__send_plist = None
        self.__send_object = None
        self.assistant = None
        self.location = None
        self.logger = logging.getLogger()
        self.__priority = False
        self.__shouldCancel = False
    
    def initialize(self, method, speech, language, send_object, send_plist, assistant, location):
        super(Plugin, self).__init__()
        self.__method = method
        self.__lang = language
        self.__speech = speech
        self.__send_plist = send_plist
        self.__send_object = send_object
        self.assistant = assistant
        self.location = location
        self.__shouldCancel = False
        self.__priority = False
        
    def _abortPluginRun(self):
        self.__shouldCancel = True
        

    def run(self):
        try:
            try:
                arguments = inspect.getargspec(self.__method).args
                if len(arguments) == 3:
                    self.__method(self, self.__speech, self.__lang)
                elif len(arguments) == 4:
                    self.__method(self, self.__speech, self.__lang, self.__method.__dict__[__criteria_key__][self.__lang].match(self.__speech))
                if self.__priority:
                    PluginManager.prioritizePluginObject(self, self.assistant.assistantId)
                else:
                    PluginManager.clearPriorityFor(self.assistant.assistantId)
            except ApiKeyNotFoundException as e:
                self.logger.warning("Failed executing plugin due to missing API key: "+str(e))
            except StopPluginExecution, instance:
                self.logger.info("Plugin stopped executing with reason: {0}".format(instance))
            except:
                self.logger.exception("Unexpected error during plugin processing")
                self.say(__error_responses__[self.__lang])
                self.complete_request()
        except:
            pass
        self.connection.current_running_plugin = None
        self.connection = None
        self.assistant = None
        self.location = None
        self.__send_object = None
        self.__send_plist = None
        self.__method = None
        self.__lang = None
        self.__speech = None
        self.waitForResponse = None
        self.response = None
        self.refId = None
        
    def _checkForCancelRequest(self):
        if self.__shouldCancel:
            raise StopPluginExecution("Plugin run was aborted")

    def requestPriorityOnNextRequest(self):
        self._checkForCancelRequest()
        self.__priority = True

    def getCurrentLocation(self, force_reload=False, accuracy=GetRequestOrigin.desiredAccuracyBest):
        self._checkForCancelRequest()
        if self.location != None and force_reload == False:
            return self.location
        if self.location == None or (self.location != None and force_reload):
            #do a reload
            response = self.getResponseForRequest(GetRequestOrigin(self.refId, desiredAccuracy=accuracy, searchTimeout=5.0))
            if response['class'] == 'SetRequestOrigin':
                self.location = SetRequestOrigin(response)
                if self.location.status != None and self.location.status != SetRequestOrigin.statusValid:
                    # urgs... we are fucked no location here, there is a status
                    # tell the other end that it fucked up and should enable location service
                    
                    #We need to say something
                    view1 = UIAssistantUtteranceView()
                    view1.text = view1.speakableText = __error_location_help__[self.__lang] if self.__lang in __error_location_help__ else __error_location_help__['en-US']
                    view1.dialogIdentifier="Common#assistantLocationServicesDisabled"
                    
                    #lets create another which has tells him to open settings
                    view2 = UIAssistantUtteranceView()
                    view2.text = view2.speakableText = __error_location_saysettings__[self.__lang] if self.__lang in __error_location_saysettings__ else __error_location_saysettings__['en-US']
                    view2.dialogIdentifier="Common#assistantLocationServicesDisabled"
                    
                    #create a link
                    link = UIOpenLink(self.refId)
                    link.ref="prefs:root=LOCATION_SERVICES"
                    
                    # create a button which opens the location tab in the settings if clicked on it
                    button = UIButton()
                    button.text = __error_location_settings__[self.__lang] if self.__lang in __error_location_settings__ else __error_location_settings__['en-US']
                    button.commands = [link]
                    
                    # wrap it up in a adds view
                    addview = UIAddViews(self.refId)
                    addview.views = [view1, view2, button]
                    addview.dialogPhase = addview.DialogPhaseClarificationValue
                    self.send_object(addview)
                    self.complete_request()
                    # we should definitivly kill the running plugin
                    raise StopPluginExecution("Could not get necessary location information")
                else: 
                    return self.location
            elif response['class'] == 'SetRequestOriginFailed':
                self.logger.warning('THIS IS NOT YET IMPLEMENTED, PLEASE PROVIDE SITUATION WHERE THIS HAPPEND')
                raise Exception()
     
    def send_object(self, obj):
        self._checkForCancelRequest()
        self.connection.plugin_lastAceId = obj.aceId
        self.__send_object(obj)
    
    def send_plist(self, plist):
        self._checkForCancelRequest()
        self.connection.plugin_lastAceId = plist['aceId']
        self.__send_plist(plist)

    def complete_request(self, callbacks=None):
        self._checkForCancelRequest()
        self.connection.current_running_plugin = None
        self.send_object(RequestCompleted(self.refId, callbacks))

    def ask(self, text, speakableText=None):
        self._checkForCancelRequest()
        self.waitForResponse = threading.Event()
        if speakableText == None:
            speakableText = text
        view = UIAddViews(self.refId)
        view1 = UIAssistantUtteranceView()
        view1.text = text
        view1.speakableText = speakableText 
        view1.listenAfterSpeaking = True
        view.views = [view1]
        self.send_object(view)
        self.waitForResponse.wait()
        self._checkForCancelRequest()
        self.waitForResponse = None
        return self.response

    def getResponseForRequest(self, clientBoundCommand):
        self._checkForCancelRequest()
        self.waitForResponse = threading.Event()
        if isinstance(clientBoundCommand, ClientBoundCommand):
            self.send_object(clientBoundCommand)
        else:
            self.send_plist(clientBoundCommand)
        self.waitForResponse.wait()
        self._checkForCancelRequest()
        self.waitForResponse = None
        return self.response
    
    def sendRequestWithoutAnswer(self, clientBoundCommand):
        self._checkForCancelRequest()
        if isinstance(clientBoundCommand, ClientBoundCommand):
            self.send_object(clientBoundCommand)
        else:
            self.send_plist(clientBoundCommand)

    def say(self, text, speakableText=None):
        self._checkForCancelRequest()
        view = UIAddViews(self.refId)
        if speakableText == None:
            speakableText = text
        view1 = UIAssistantUtteranceView()
        view1.text = text
        view1.speakableText = speakableText
        view.views = [view1]
        self.send_object(view)
        
    def user_name(self):
        if self.assistant.nickName!='':
            self.user_name=self.assistant.nickName.decode("utf-8")
        elif self.assistant.firstName!='':
            self.user_name=self.assistant.firstName.decode("utf-8")
        else:
            self.user_name=u''
        return self.user_name
