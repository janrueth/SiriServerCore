#!/usr/bin/python
# -*- coding: utf-8 -*-

from plugin import *
from siriObjects.systemObjects import ResultCallback
from siriObjects.websearchObjects import WebSearch


webSearchAnswerText = {"de": u"Das Web nach {0} durchsuchen …", "en": u"Searching the web for {0} …", "fr": u"Searching the web for {0} …"}
webSearchAnswerFailureText = {"de": u"Entschuldigung, Ich, ich kann jetzt nicht das Web durchsuchen.", "en": u"Sorry but I cannot search the web right now.", "fr": u"Sorry but I cannot search the web right now."}
class startRequestHandler(Plugin):    

    #we should provide a shortcut for this....
    @register("de-DE", u"\^webSearchQuery\^=\^(.+)\^\^webSearchConfirmation\^=\^(.+)\^")     
    @register("en-US", u"\^webSearchQuery\^=\^(.+)\^\^webSearchConfirmation\^=\^(.+)\^")
    @register("en-AU", u"\^webSearchQuery\^=\^(.+)\^\^webSearchConfirmation\^=\^(.+)\^")
    @register("en-GB", u"\^webSearchQuery\^=\^(.+)\^\^webSearchConfirmation\^=\^(.+)\^")
    @register("fr-FR", u"\^webSearchQuery\^=\^(.+)\^\^webSearchConfirmation\^=\^(.+)\^")
    def webSearchConfirmation(self, speech, language, regMatched):
        webSearchQuery = regMatched.group(1)
        #webSearchConfirmation = regMatched.group(2)
        
        lang = language.split("-")[0]

        resultCallback1View = UIAddViews(refId="")
        resultCallback1ViewView = UIAssistantUtteranceView()
        resultCallback1ViewView.dialogIdentifier="WebSearch#initiateWebSearch"
        resultCallback1ViewView.text=webSearchAnswerText[lang].format(u"„{0}“".format(webSearchQuery))
        resultCallback1ViewView.speakableText=webSearchAnswerText[lang].format(webSearchQuery)
        resultCallback1View.views = [resultCallback1ViewView]
        
        search = WebSearch(refId="", aceId="", query=webSearchQuery)
        resultCallback3View = UIAddViews(refId="")
        resultCallback3ViewView = UIAssistantUtteranceView()
        resultCallback3ViewView.dialogIdentifier="WebSearch#fatalResponse"
        resultCallback3ViewView.text=webSearchAnswerFailureText[lang]
        resultCallback3ViewView.speakableText=webSearchAnswerFailureText[lang]
        resultCallback3View.views=[resultCallback3ViewView]
        resultCallback3 = ResultCallback(commands=[resultCallback3View])
        search.callbacks = [resultCallback3]

        resultCallback2 = ResultCallback(commands=[search])
        resultCallback1View.callbacks = [resultCallback2]

        self.complete_request(callbacks=[ResultCallback(commands=[resultCallback1View])])
    