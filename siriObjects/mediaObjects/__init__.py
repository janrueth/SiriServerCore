from siriObjects.baseObjects import ClientBoundCommand, ServerBoundCommand, \
AceObject
from siriObjects.systemObjects import DomainObject
from siriObjects.uiObjects import Snippet


class MPMediaEntity(DomainObject):
    def __init__(self, clazz="MediaEntity", group="com.apple.ace.media"):
        super(MPMediaEntity, self).__init__(group, clazz=clazz)
        self.sortTitle = None # @"NSString"
        self.title = None # @"NSString"

    def to_plist(self):
        self.add_property('sortTitle')
        self.add_property('title')
        return super(MPMediaEntity, self).to_plist()

class MPCollection(MPMediaEntity):
    def __init__(self, clazz="Collection", group="com.apple.ace.media"):
        super(MPCollection, self).__init__(clazz, group)
        self.items = None # @"NSArray"

    def to_plist(self):
        self.add_property('items')
        return super(MPCollection, self).to_plist()
    
class MPAlbumCollection(MPCollection):
    def __init__(self):
        super(MPAlbumCollection, self).__init__("AlbumCollection", "com.apple.ace.media")
        self.rating = None # i

    def to_plist(self):
        self.add_property('rating')
        return super(MPAlbumCollection, self).to_plist()

class MPArtistCollection(MPCollection):
    def __init__(self):
        super(MPArtistCollection, self).__init__("ArtistCollection", "com.apple.ace.media")

    def to_plist(self):
        return super(MPArtistCollection, self).to_plist()


class MPEnableShuffle(ClientBoundCommand):
    def __init__(self, refId):
        super(MPEnableShuffle, self).__init__("EnableShuffle", "com.apple.ace.media", None, refId)
        self.targetAppId = None # @"NSURL"
        self.enable = None # c


    def to_plist(self):
        self.add_property('targetAppId')
        self.add_property('enable')
        return super(MPEnableShuffle, self).to_plist()

class MPGeniusMix(MPCollection):
    def __init__(self):
        super(MPGeniusMix, self).__init__("GeniusMix", "com.apple.ace.media")

    def to_plist(self):
        return super(MPGeniusMix, self).to_plist()

class MPGeniusSummon(ClientBoundCommand):
    def __init__(self, refId):
        super(MPGeniusSummon, self).__init__("GeniusSummon", "com.apple.ace.media", None, refId)
        self.targetAppId = None # @"NSURL"
        self.mediaItem = None # @"SAMPMediaItem"
   
    def to_plist(self):
        self.add_property('targetAppId')
        self.add_property('mediaItem')
        return super(MPGeniusSummon, self).to_plist()

class MPGeniusSummonFailed(ServerBoundCommand):
    classIdentifier = "GeniusSummonFailed"
    groupIdentifier = "com.apple.ace.media"
    def __init__(self, plist):
        self.errorCode = None # i
        self.reason = None # @"NSString"
        super(MPGeniusSummonFailed, self).__init__(plist)

class MPGeniusSummonSucceded(ServerBoundCommand):
    classIdentifier = "GeniusSummonSucceded"
    groupIdentifier = "com.apple.ace.media"
    def __init__(self, plist):
        super(MPGeniusSummonSucceded, self).__init__(plist)

class MPGenreCollection(MPCollection):
    def __init__(self):
        super(MPGenreCollection, self).__init__("GenreCollection", "com.apple.ace.media")

    def to_plist(self):
        return super(MPGenreCollection, self).to_plist()

class MPGetState(ClientBoundCommand):
    def __init__(self, refId):
        super(MPGetState, self).__init__("GetState", "com.apple.ace.media", None, refId)
        self.targetAppId = None # @"NSURL"

    def to_plist(self):
        self.add_property('targetAppId')
        return super(MPGetState, self).to_plist()

class MPGetStateResponse(ServerBoundCommand):
    classIdentifier = "GetStateResponse"
    groupIdentifier = "com.apple.ace.media"
    def __init__(self, plist):
        self.listeningToItem = None # @"MediaItem"
        self.listeningToMusicApplication = None # @"NSNumber"
        self.state = None # i
        super(MPGetStateResponse, self).__init__(plist)

class MPLoadPredefinedQueue(ClientBoundCommand):
    MPTypePlaylistValue = 1
    MPTypePodcastValue = 2
    MPTypeSongValue = 3
    MPTypeGeniusMixValue = 4
    MPTypeVideoValue = 5
    MPTypeITunesUValue = 6
    MPTypeAudioBookValue = 7
    MPTypeTVShowValue = 8
    def __init__(self, refId):
        super(MPLoadPredefinedQueue, self).__init__("LoadPredefinedQueue", "com.apple.ace.media", None, refId)
        self.targetAppId = None # @"NSURL"
        self.mediaItemType = None # i

    def to_plist(self):
        self.add_property('targetAppId')
        self.add_property('mediaItemType')
        return super(MPLoadPredefinedQueue, self).to_plist()


class MPMediaItem(MPMediaEntity):
    def __init__(self, clazz="MediaItem", group="com.apple.ace.media"):
        super(MPMediaItem, self).__init__(clazz, group)
        self.album = None # @"NSString"
        self.artist = None # @"NSString"
        self.genre = None # @"NSString"
        self.playCount = None # i
        self.rating = None # i
        self.sortAlbum = None # @"NSString"
        self.sortArtist = None # @"NSString"
        self.trackNumber = None # i

    def to_plist(self):
        self.add_property('album')
        self.add_property('artist')
        self.add_property('genre')
        self.add_property('playCount')
        self.add_property('rating')
        self.add_property('sortAlbum')
        self.add_property('sortArtist')
        self.add_property('trackNumber')
        return super(MPMediaItem, self).to_plist()

class MPPlaylist(MPCollection):
    def __init__(self):
        super(MPPlaylist, self).__init__("Playlist", "com.apple.ace.media")

    def to_plist(self):
        return super(MPPlaylist, self).to_plist()

class MPPodcast(MPMediaItem):
    def __init__(self):
        super(MPPodcast, self).__init__("Podcast", "com.apple.ace.media")

    def to_plist(self):
        return super(MPPodcast, self).to_plist()

class MPSearch(ClientBoundCommand):
    MPSearchPropertyAlbumValue = 1
    MPSearchPropertyArtistValue = 2
    MPSearchPropertyComposerValue = 3
    MPSearchPropertyGenreValue = 4
    MPSearchPropertyTitleValue = 5
    def __init__(self, refId):
        super(MPSearch, self).__init__("Search", "com.apple.ace.media", None, refId)
        self.targetAppId = None # @"NSURL"
        self.constraints = None # @"NSArray"
        self.maxResults = None # i
        self.searchProperties = None # @"NSArray"
        self.searchTypes = None # @"NSArray"
        self.searchValue = None # @"NSString"
        self.strict = None # c
 
    def to_plist(self):
        self.add_property('targetAppId')
        self.add_property('constraints')
        self.add_property('maxResults')
        self.add_property('searchProperties')
        self.add_property('searchTypes')
        self.add_property('searchValue')
        self.add_property('strict')
        return super(MPSearch, self).to_plist()

class MPSearchCompleted(ServerBoundCommand):
    classIdentifier = "SearchCompleted"
    groupIdentifier = "com.apple.ace.media"
    def __init__(self, plist):
        self.targetAppId = None # @"NSURL"
        self.results = None # @"NSArray"
        super(MPSearchCompleted, self).__init__(plist)

class MPSearchConstraint(AceObject):
    def __init__(self):
        super(MPSearchConstraint, self).__init__("SearchConstraint", "com.apple.ace.media")
        self.query = None # @"NSString"
        self.searchProperties = None # @"NSArray"

    def to_plist(self):
        self.add_property('query')
        self.add_property('searchProperties')
        return super(MPSearchConstraint, self).to_plist()

class MPSetOutputSource(ClientBoundCommand):
    def __init__(self, refId):
        super(MPSetOutputSource, self).__init__("SetOutputSource", "com.apple.ace.media", None, refId)
        self.targetAppId = None # @"NSURL"
        self.outputSourceId = None # @"NSURL"

    def to_plist(self):
        self.add_property('targetAppId')
        self.add_property('outputSourceId')
        return super(MPSetOutputSource, self).to_plist()

class MPSetPlaybackPosition(ClientBoundCommand):
    MPPlaybackPositionNextItemValue = 1
    MPPlaybackPositionPreviousItemValue = 2
    MPPlaybackPositionBeginningValue = 3
    def __init__(self, refId):
        super(MPSetPlaybackPosition, self).__init__("SetPlaybackPosition", "com.apple.ace.media", None, refId)
        self.targetAppId = None # @"NSURL"
        self.position = None # i

    def to_plist(self):
        self.add_property('targetAppId')
        self.add_property('position')
        return super(MPSetPlaybackPosition, self).to_plist()

class MPSetQueue(ClientBoundCommand):
    def __init__(self, refId):
        super(MPSetQueue, self).__init__("SetQueue", "com.apple.ace.media", None, refId)
        self.targetAppId = None # @"NSURL"
        self.mediaItems = None # @"SAMPCollection"

    def to_plist(self):
        self.add_property('targetAppId')
        self.add_property('mediaItems')
        return super(MPSetQueue, self).to_plist()

class MPSetState(ClientBoundCommand):
    MPPlayStatePlayingValue = 1
    MPPlayStatePausedValue = 2
    MPPlayStateStoppedValue = 3
    MPPlayStateInterruptedValue = 4
    def __init__(self, refId):
        super(MPSetState, self).__init__("SetState", "com.apple.ace.media", None, refId)
        self.targetAppId = None # @"NSURL"
        self.state = None # i

    def to_plist(self):
        self.add_property('targetAppId')
        self.add_property('state')
        return super(MPSetState, self).to_plist()

class MPSnippet(Snippet):
    def __init__(self):
        super(MPSnippet, self).__init__("com.apple.ace.media")
        self.items = None # @"NSArray"

    def to_plist(self):
        self.add_property('items')
        return super(MPSnippet, self).to_plist()

class MPSong(MPMediaItem):
    def __init__(self):
        super(MPSong, self).__init__("Song", "com.apple.ace.media")
    
    def to_plist(self):
        return super(MPSong, self).to_plist()

class MPTitleCollection(MPCollection):
    def __init__(self):
        super(MPTitleCollection, self).__init__("TitleCollection", "com.apple.ace.media")

    def to_plist(self):
        return super(MPTitleCollection, self).to_plist()