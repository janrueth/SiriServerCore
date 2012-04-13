from uuid import uuid4
import logging

class AceObject(object):
    def __init__(self, encodedClassName, groupIdentifier):
        self.className = encodedClassName
        self.groupId = groupIdentifier
        self.plist = dict()
        self.properties = dict()
        
    def initializeFromPlist(self, plist):
        if 'properties' in plist:
            for key in plist['properties'].keys():
                if type(plist['properties'][key]) == list:
                    setattr(self, key, AceObject.list_from_plist_list(plist['properties'][key]))
                elif type(plist['properties'][key]) == dict: #unwrap 
                    setattr(self, key, ServerBoundCommand(plist['properties'][key]))
                else:
                    try:
                        setattr(self, key, plist['properties'][key])
                    except:
                        pass
    def add_item(self, name):
        try:
            if getattr(self, name) != None and getattr(self, name) != "":
                self.plist[name] = getattr(self, name) 
        except AttributeError:
            logging.getLogger("logger").exception("You tried to set the item \"{0}\", but this instance of class: \"{1}\" does not have a member variable named like this".format(name, self.__class__))

    def add_property(self, name):
        try:
            if getattr(self,name) != None:
                self.properties[name] = getattr(self, name) 
        except AttributeError:
            logging.getLogger("logger").exception("You tried to set the property \"{0}\", but this instance of class: \"{1}\" does not have a member variable named like this".format(name, self.__class__))

    @staticmethod
    def list_to_plist(newList):
        def parseList(x):
            if type(x) == list:
                new = AceObject.list_to_plist(x)
            elif type(x) == dict:
                new = AceObject.dict_to_plist(x)
            else:
                try:
                    new = x.to_plist()
                except:
                    new = x
            return new

        return map(parseList, newList)

    @staticmethod
    def dict_to_plist(newDict):
        def parseDict((k,v)):
            if type(v) == list:
                new = AceObject.list_to_plist(v)
            elif type(v) == dict:
                new = AceObject.dict_to_plist(v)
            else:
                try:
                    new = v.to_plist()
                except:
                    new = v
            return (k,new)
                
        return dict(map(parseDict, newDict.items()))

    def to_plist(self):
        self.plist['group'] = self.groupId
        self.plist['class'] = self.className
        self.plist['properties'] = self.properties

        for key in self.plist.keys():
            if type(self.plist[key]) == list:
                self.plist[key] = AceObject.list_to_plist(self.plist[key])
            elif type(self.plist[key]) == dict:
                self.plist[key] = AceObject.dict_to_plist(self.plist[key])
            else:
                try:
                    self.plist[key] = self.plist[key].to_plist() 
                except:
                    pass
        return self.plist

    @staticmethod
    def list_from_plist_list(plistList):
        def parseList(x):
            if type(x) == list:
                return AceObject.list_from_plist_list(x)
            elif type(x) == dict:
                return ServerBoundCommand(x)
            else:
                # do nothing.. primitive
                return x
        return map(parseList, plistList)


    def from_plist(self):
        # get basic properties
        self.groupId = self.plist['group'] if 'group' in self.plist else self.groupIdentifier if hasattr(self, 'groupIdentifier') else ""
        self.className = self.plist['class'] if 'class' in self.plist else self.classIdentifier if hasattr(self, 'classIdentifier') else ""
        self.properties = self.plist['properties'] if 'properties' in self.plist else dict()
        
        #expand properties to
        for key in self.properties.keys():
            if type(self.properties[key]) == list:
                self.__setattr__(key, AceObject.list_from_plist_list(self.properties[key]))
            elif type(self.properties[key]) == dict: #unwrap 
                self.__setattr__(key, ServerBoundCommand(self.properties[key]))
            else:
                try:
                    self.__setattr__(key, self.properties[key])
                except:
                    pass

    def initWithPList(self, plist):
        self.plist = plist
        self.from_plist()
        
class ServerBoundCommand(AceObject):
    def __init__(self, plist):
        super(ServerBoundCommand, self).__init__(None, None)
        self.aceId = plist['aceId'] if 'aceId' in plist else None
        self.refId = plist['refId'] if 'refId' in plist else None
        self.plist = plist
        self.from_plist()

class ClientBoundCommand(AceObject):
    def __init__(self, encodedClassName, groupIdentifier, aceId, refId, callbacks=None):
        super(ClientBoundCommand, self).__init__(encodedClassName, groupIdentifier)
        self.aceId= aceId if aceId != None else str.upper(str(uuid4()))
        self.refId = refId if refId != None else str.upper(str(uuid4()))
        self.callbacks = callbacks if callbacks != None else []
    
    def to_plist(self):
        self.add_item('aceId')
        self.add_item('refId')
        self.add_property('callbacks')
        return super(ClientBoundCommand, self).to_plist()


class RequestCompleted(ClientBoundCommand):
    def __init__(self, refId, callbacks = None):
        super(RequestCompleted, self).__init__("RequestCompleted", "com.apple.ace.system", None, refId, callbacks)


def ObjectIsCommand(obj, command):
    try:
        if issubclass(command, AceObject):
            group = obj['group']
            clazz = obj['class']
            if command.classIdentifier == clazz and command.groupIdentifier == group:
                return True
    except:
        pass
    return False
    