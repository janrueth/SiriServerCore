#!/usr/bin/python
# -*- coding: utf-8 -*-



import re
import threading
import logging
import PluginManager
import inspect


from siriObjects.baseObjects import ClientBoundCommand, RequestCompleted
from siriObjects.uiObjects import AddViews, AssistantUtteranceView, OpenLink, Button
from siriObjects.systemObjects import GetRequestOrigin, SetRequestOrigin

__criteria_key__ = "criterias"


__error_responses__ = {"de-DE": "Es ist ein Fehler in der Verarbeitung ihrer Anfrage aufgetreten!", "en-US": "There was an error during the processing of your request!", "en-GB": "There was an error during the processing of your request!", "en-AU": "There was an error during the processing of your request!", "fr-FR": "Il y avait une erreur lors du traitement de votre demande!"}

__error_location_help__ = {"de-DE": u"Ich weiß nicht wo du bist… Aber du kannst mir helfen es heraus zu finden…", "en-US": u"I don’t know where you are… But you can help me find out…", "en-GB": u"I don’t know where you are… But you can help me find out…", "en-AU": u"I don’t know where you are… But you can help me find out…", "fr-FR": u"Je ne sais pas où vous êtes ... Mais vous pouvez m'aider à en savoir plus sur ..."}

__error_location_saysettings__ = {"de-DE": u"In den Ortungsdienst Einstellungen, schalte Ortungsdienst und Siri ein.", "en-US": u"In Location Services Settings, turn on both Location Services and Siri.", "en-GB": u"In Location Services Settings, turn on both Location Services and Siri.", "en-AU": u"In Location Services Settings, turn on both Location Services and Siri.", "fr-FR": u"Dans les paramètres de service de localisation, activez les services de localisation et Siri."}

__error_location_settings__ = {"de-DE": u"Ortungsdienst Einstellungen", "en-US": u"Location Services Settings", "en-GB": u"Location Services Settings", "en-AU": u"Location Services Settings", "fr-FR": u"Services de localisation"}



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
        self.logger = logging.getLogger("logger")
        self.__priority = False
    
    def initialize(self, method, speech, language, send_object, send_plist, assistant, location):
        super(Plugin, self).__init__()
        self.__method = method
        self.__lang = language
        self.__speech = speech
        self.__send_plist = send_plist
        self.__send_object = send_object
        self.assistant = assistant
        self.location = location

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
                self.logger.warning("Plugin stopped executing with reason: {0}".format(instance))
            except:
                self.logger.exception("Unexpected during plugin processing")
                self.say(__error_responses__[self.__lang])
                self.complete_request()
        except:
            pass
        self.connection.current_running_plugin = None

    def requestPriorityOnNextRequest(self):
        self.__priority = True

    def getCurrentLocation(self, force_reload=False, accuracy=GetRequestOrigin.desiredAccuracyBest):
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
                    view1 = AssistantUtteranceView(text=__error_location_help__[self.__lang], speakableText=__error_location_help__[self.__lang], dialogIdentifier="Common#assistantLocationServicesDisabled")
                    
                    #lets create another which has tells him to open settings
                    view2 = AssistantUtteranceView(text=__error_location_saysettings__[self.__lang], speakableText=__error_location_saysettings__[self.__lang], dialogIdentifier="Common#assistantLocationServicesDisabled")
                    
                    # create a button which opens the location tab in the settings if clicked on it
                    button = Button(text=__error_location_settings__[self.__lang], commands=[OpenLink(ref="prefs:root=LOCATION_SERVICES")])
                    
                    # wrap it up in a adds view
                    self.send_object(AddViews(self.refId, views=[view1, view2, button]))
                    self.complete_request()
                    # we should definitivly kill the running plugin
                    raise StopPluginExecution("Could not get necessary location information")
                else: 
                    return self.location
            elif response['class'] == 'SetRequestOriginFailed':
                self.logger.warning('THIS IS NOT YET IMPLEMENTED, PLEASE PROVIDE SITUATION WHERE THIS HAPPEND')
                raise Exception()
     
    def send_object(self, obj):
        self.connection.plugin_lastAceId = obj.aceId
        self.__send_object(obj)
    
    def send_plist(self, plist):
        self.connection.plugin_lastAceId = plist['aceId']
        self.__send_plist(plist)

    def complete_request(self, callbacks=None):
        self.connection.current_running_plugin = None
        self.send_object(RequestCompleted(self.refId, callbacks))

    def ask(self, text, speakableText=""):
        self.waitForResponse = threading.Event()
        if speakableText == "":
            speakableText = text
        view = AddViews(self.refId)
        view.views += [AssistantUtteranceView(text, speakableText, listenAfterSpeaking=True)]
        self.send_object(view)
        self.waitForResponse.wait()
        self.waitForResponse = None
        return self.response

    def getResponseForRequest(self, clientBoundCommand):
        self.waitForResponse = threading.Event()
        if isinstance(clientBoundCommand, ClientBoundCommand):
            self.send_object(clientBoundCommand)
        else:
            self.send_plist(clientBoundCommand)
        self.waitForResponse.wait()
        self.waitForResponse = None
        return self.response
    
    def sendRequestWithoutAnswer(self, clientBoundCommand):
        if isinstance(clientBoundCommand, ClientBoundCommand):
            self.send_object(clientBoundCommand)
        else:
            self.send_plist(clientBoundCommand)

    def say(self, text, speakableText=""):
        view = AddViews(self.refId)
        if speakableText == "":
            speakableText = text
        view.views += [AssistantUtteranceView(text, speakableText)]
        self.send_object(view)