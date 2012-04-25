from plugin import Plugin, __criteria_key__, NecessaryModuleNotFound, \
    ApiKeyNotFoundException
from types import FunctionType
import logging
import os
import re



logger = logging.getLogger("logger")
pluginPath = "plugins"

__config_file__ = "plugins.conf"
__apikeys_file__ = "apiKeys.conf"



plugins = dict()
prioritizedPlugins = dict()
apiKeys = dict()

def load_plugins():
    with open(__config_file__, "r") as fh:
        for line in fh:
            line = line.strip()
            if line.startswith("#") or line == "":
                continue
            # just load the whole shit...
            try:
                __import__(pluginPath+"."+line,  globals(), locals(), [], -1)
            except NecessaryModuleNotFound as e:
                logger.critical("Failed loading plugin due to missing module: "+str(e))
            except ApiKeyNotFoundException as e:
                logger.critical("Failed loading plugin due to missing API key: "+str(e))
            except:
                logger.exception("Plugin loading failed")
            
    # as they are loaded in the order in the file we will have the same order in __subclasses__()... I hope

    for clazz in Plugin.__subclasses__():
        # look at all functions of a class lets filter them first
        methods = filter(lambda x: type(x) == FunctionType, clazz.__dict__.values())
        # now we check if the method is decorated by register
        for method in methods:
            if __criteria_key__ in method.__dict__:
                criterias = method.__dict__[__criteria_key__]
                for lang, regex in criterias.items():
                    if not lang in plugins:
                        plugins[lang] = []
                    # yeah... save the regex, the clazz and the method, shit just got loaded...
                    plugins[lang].append((regex, clazz, method))


def reload_api_keys():
    global apiKeys
    apiKeys = dict()
    load_api_keys()

def load_api_keys():
    with open(__apikeys_file__, "r") as fh:
        for line in fh:
            line = line.strip()
            if line.startswith("#") or line == "":
                continue
            kv = line.split("=", 1)
            try:
                apiName = str.lower(kv[0]).strip()
                kv[1] = kv[1].strip()
                apiKey = kv[1][1:-1] #stip the ""
                apiKeys[apiName] = apiKey
            except:
                logger.critical("There was an error parsing an API in the line: "+ line)

def getAPIKeyForAPI(APIname):
    apiName = str.lower(APIname) 
    if apiName in apiKeys:
        return apiKeys[apiName]
    return None

def getPlugin(speech, language):
    if language in plugins:
        for (regex, clazz, method) in plugins[language]:
            if regex.match(speech) != None:
                return (clazz, method)
    return (None, None)

def clearPriorityFor(assistantId):
    if assistantId in prioritizedPlugins:
        del prioritizedPlugins[assistantId]

def prioritizePluginObject(pluginObj, assistantId):
    prioritizedPlugins[assistantId] = dict()
    for lang in plugins.keys():
        for (regex, clazz, method) in plugins[lang]:
            if pluginObj.__class__ == clazz:
                if not lang in prioritizedPlugins[assistantId]:
                    prioritizedPlugins[assistantId][lang] = []
                prioritizedPlugins[assistantId][lang].append((regex, pluginObj, method))

def searchPrioritizedPlugin(assistantId, speech, language):
    if assistantId in prioritizedPlugins:
        if language in prioritizedPlugins[assistantId]:
            for (regex, pluginObj, method) in prioritizedPlugins[assistantId][language]:
                if regex.match(speech) != None:
                    return (pluginObj, method)
    return (None, None)

def getPluginForImmediateExecution(assistantId, speech, language, otherPluginParams):
    (sendObj, sendPlist, assistant, location) = otherPluginParams

    (pluginObj, method) = searchPrioritizedPlugin(assistantId, speech, language)
    if pluginObj == None and method == None:
        (clazz, method) = getPlugin(speech, language)
        if clazz != None and method != None:
            logger.debug("Instantiating plugin and method: {0}.{1}".format(clazz.__name__, method.__name__))
            pluginObj = clazz()
            pluginObj.initialize(method, speech, language, sendObj, sendPlist, assistant, location)
            #prioritizePluginObject(pluginObj, assistantId)
    else:
        #reinitialize it
        logger.info("Found a matching prioritized plugin")
        pluginObj.initialize(method, speech, language, sendObj, sendPlist, assistant, location)
    
    return pluginObj
        



