from siriObjects.baseObjects import ClientBoundCommand, ServerBoundCommand,\
    AceObject
    
    
class SyncAnchor(AceObject):
    def __init__(self):
        super(SyncAnchor, self).__init__("Anchor", "com.apple.ace.sync")
        self.generation = None # @"NSString"
        self.key = None # @"NSString"
        self.validity = None # @"NSString"
        self.value = None # @"NSString"

    def to_plist(self):
        self.add_property('generation')
        self.add_property('key')
        self.add_property('validity')
        self.add_property('value')
        return super(SyncAnchor, self).to_plist()

class SyncChunk(ServerBoundCommand):
    classIdentifier = "Chunk"
    groupIdentifier = "com.apple.ace.sync"
    def __init__(self, plist):
        self.key = None # @"NSString"
        self.postGen = None # @"NSString"
        self.preGen = None # @"NSString"
        self.toAdd = None # @"NSArray"
        self.toRemove = None # @"NSArray"
        self.validity = None # @"NSString"
        super(SyncChunk, self).__init__(plist)


class SyncChunkAccepted(ClientBoundCommand):
    def __init__(self, refId):
        super(SyncChunkAccepted, self).__init__("ChunkAccepted", "com.apple.ace.sync", None, refId)
        self.current = None # @"SASyncAnchor"


    def to_plist(self):
        self.add_property('current')
        return super(SyncChunkAccepted, self).to_plist()


class SyncChunkDenied(ClientBoundCommand):
    def __init__(self, refId):
        super(SyncChunkDenied, self).__init__("ChunkDenied", "com.apple.ace.sync", None, refId)
        self.callbacks = None # @"NSArray"
        self.current = None # @"SASyncAnchor"
        self.errorCode = None # i

    def to_plist(self):
        self.add_property('callbacks')
        self.add_property('current')
        self.add_property('errorCode')
        return super(SyncChunkDenied, self).to_plist()


class SyncFinished(ServerBoundCommand):
    classIdentifier = "Finished"
    groupIdentifier = "com.apple.ace.sync"
    def __init__(self, plist):
        super(SyncFinished, self).__init__(plist)



class SyncGetAnchors(ServerBoundCommand):
    classIdentifier = "GetAnchors"
    groupIdentifier = "com.apple.ace.sync"
    def __init__(self, plist):
        self.sources = None # @"NSArray"
        super(SyncGetAnchors, self).__init__(plist)


class SyncGetAnchorsResponse(ClientBoundCommand):
    def __init__(self, refId):
        super(SyncGetAnchorsResponse, self).__init__("GetAnchorsResponse", "com.apple.ace.sync", None, refId)
        self.anchors = None # @"NSArray"

    def to_plist(self):
        self.add_property('anchors')
        return super(SyncGetAnchorsResponse, self).to_plist()
