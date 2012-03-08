#!/usr/bin/python
# -*- coding: utf-8 -*-


from plugin import *
from siriObjects.systemObjects import ResultCallback
import uuid

class examplePlugin(Plugin):
    
    @register("de-DE", ".*Sinn.*Leben.*")
    @register("en-US", ".*Meaning.*Life.*")
    def meaningOfLife(self, speech, language, matchedRegex):
        if language == 'de-DE':
            answer = self.ask(u"Willst du das wirklich wissen?")
            self.say(u"Du hast \"{0}\" gesagt!".format(answer))
        else:
            self.say("I shouldn't tell you!")
        self.complete_request()

    @register("de-DE", "(.*Hallo.*)|(.*Hi.*Siri.*)|(Hi)|(Hey)")
    @register("en-US", "(.*Hello.*)|(.*Hi.*Siri.*)|(Hi)|(Hey)")
    @register("fr-FR", ".*(Bonjour|Coucou|Salut)( Siri)?.*")
    def st_hello(self, speech, language):
        if language == 'de-DE':
            self.say(u"Hallo {0}!".format(self.user_name()))
        elif language == 'fr-FR':
            self.say(u"Bonjour {0}!".format(self.user_name()));
        else:
            self.say(u"Greetings, {0}!".format(self.user_name()))
        self.complete_request()
    
    @register("de-DE", ".*standort.*test.*")
    @register("en-US", ".*location.*test.*")
    def locationTest(self, speech, language):
        location = self.getCurrentLocation(force_reload=True)
        self.say(u"lat: {0}, long: {1}".format(location.latitude, location.longitude))
        self.complete_request()
          
