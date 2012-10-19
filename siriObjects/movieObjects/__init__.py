from siriObjects.uiObjects import UISnippet
from siriObjects.baseObjects import AceObject
from siriObjects.systemObjects import DomainObject


class MovieImage(AceObject):
    def __init__(self):
        super(MovieImage, self).__init__("Image", "com.apple.ace.movie")
        self.resolution = None # @"SAMovieResolution"
        self.uri = None # @"NSURL"

    def to_plist(self):
        self.add_property('resolution')
        self.add_property('uri')
        return super(MovieImage, self).to_plist()

class MovieMovie(DomainObject):
    def __init__(self):
        super(MovieMovie, self).__init__("Movie", "com.apple.ace.movie")
        self.actors = None # @"NSArray"
        self.directors = None # @"NSArray"
        self.genres = None # @"NSArray"
        self.hiResTrailerUri = None # @"NSURL"
        self.iTunesUri = None # @"NSURL"
        self.is3d = None # c
        self.isAvailableOnItunesForPurchase = None # @"NSNumber"
        self.isAvailableOnItunesForRent = None # @"NSNumber"
        self.lowResTrailerUri = None # @"NSURL"
        self.name = None # @"NSString"
        self.posterImages = None # @"NSArray"
        self.posterUri = None # @"NSURL"
        self.qualityRating = None # @"NSNumber"
        self.rating = None # @"NSString"
        self.reviews = None # @"SALocalSearchReviewList"
        self.rottenTomatoesUri = None # @"NSURL"
        self.runtimeInMinutes = None # i
        self.studios = None # @"NSArray"
        self.synopsis = None # @"NSString"
        self.theaterShowtimeSearchRegionDescription = None # @"NSString"
        self.theaterShowtimes = None # @"NSArray"
        self.theatricalReleaseDate = None # @"NSDate"
        self.trailerUri = None # @"NSURL"

    def to_plist(self):
        self.add_property('actors')
        self.add_property('directors')
        self.add_property('genres')
        self.add_property('hiResTrailerUri')
        self.add_property('iTunesUri')
        self.add_property('is3d')
        self.add_property('isAvailableOnItunesForPurchase')
        self.add_property('isAvailableOnItunesForRent')
        self.add_property('lowResTrailerUri')
        self.add_property('name')
        self.add_property('posterImages')
        self.add_property('posterUri')
        self.add_property('qualityRating')
        self.add_property('rating')
        self.add_property('reviews')
        self.add_property('rottenTomatoesUri')
        self.add_property('runtimeInMinutes')
        self.add_property('studios')
        self.add_property('synopsis')
        self.add_property('theaterShowtimeSearchRegionDescription')
        self.add_property('theaterShowtimes')
        self.add_property('theatricalReleaseDate')
        self.add_property('trailerUri')
        return super(MovieMovie, self).to_plist()

class MovieMovieListSnippet(UISnippet):
    def __init__(self):
        super(MovieMovieListSnippet, self).__init__("MovieListSnippet", "com.apple.ace.movie")
        self.movies = None # @"NSArray"
        self.shouldShowRottenTomatoesRating = None # c

    def to_plist(self):
        self.add_property('movies')
        self.add_property('shouldShowRottenTomatoesRating')
        return super(MovieMovieListSnippet, self).to_plist()

class MovieMovieSnippet(UISnippet):
    def __init__(self):
        super(MovieMovieSnippet, self).__init__("MovieSnippet", "com.apple.ace.movie")
        self.movie = None # @"SAMovieMovie"
        self.playTrailer = None # c

    def to_plist(self):
        self.add_property('movie')
        self.add_property('playTrailer')
        return super(MovieMovieSnippet, self).to_plist()

class MovieMovieTheaterShowtimes(AceObject):
    def __init__(self):
        super(MovieMovieTheaterShowtimes, self).__init__("MovieTheaterShowtimes", "com.apple.ace.movie")
        self.movieShowtimes = None # @"NSArray"
        self.showtimes = None # @"NSArray"
        self.theater = None # @"SALocalSearchBusiness2"

    def to_plist(self):
        self.add_property('movieShowtimes')
        self.add_property('showtimes')
        self.add_property('theater')
        return super(MovieMovieTheaterShowtimes, self).to_plist()

class MovieResolution(AceObject):
    def __init__(self):
        super(MovieResolution, self).__init__("Resolution", "com.apple.ace.movie")
        self.height = None # i
        self.width = None # i

    def to_plist(self):
        self.add_property('height')
        self.add_property('width')
        return super(MovieResolution, self).to_plist()

class MovieReviewsSnippet(UISnippet):
    def __init__(self):
        super(MovieReviewsSnippet, self).__init__("ReviewsSnippet", "com.apple.ace.movie")
        self.movie = None # @"SAMovieMovie"

    def to_plist(self):
        self.add_property('movie')
        return super(MovieReviewsSnippet, self).to_plist()

class MovieShowtime(AceObject):
    def __init__(self):
        super(MovieShowtime, self).__init__("Showtime", "com.apple.ace.movie")
        self.buyTicketsPunchout = None # @"SAUIAppPunchOut"
        self.childTicketQuantity = None # @"NSNumber"
        self.is3d = None # c
        self.isImax = None # c
        self.regularTicketQuantity = None # @"NSNumber"
        self.seniorTicketQuantity = None # @"NSNumber"
        self.showtime = None # @"SACalendar"

    def to_plist(self):
        self.add_property('buyTicketsPunchout')
        self.add_property('childTicketQuantity')
        self.add_property('is3d')
        self.add_property('isImax')
        self.add_property('regularTicketQuantity')
        self.add_property('seniorTicketQuantity')
        self.add_property('showtime')
        return super(MovieShowtime, self).to_plist()

class MovieShowtimeListSnippet(MovieMovieListSnippet):
    def __init__(self):
        super(MovieShowtimeListSnippet, self).__init__("ShowtimeListSnippet", "com.apple.ace.movie")

    def to_plist(self):
        return super(MovieShowtimeListSnippet, self).to_plist()

class MovieShowtimeSelectionSnippet(UISnippet):
    def __init__(self):
        super(MovieShowtimeSelectionSnippet, self).__init__("ShowtimeSelectionSnippet", "com.apple.ace.movie")
        self.movie = None # @"SAMovieMovie"

    def to_plist(self):
        self.add_property('movie')
        return super(MovieShowtimeSelectionSnippet, self).to_plist()

class MovieTheaterListSnippet(MovieMovieListSnippet):
    def __init__(self):
        super(MovieTheaterListSnippet, self).__init__("TheaterListSnippet", "com.apple.ace.movie")

    def to_plist(self):
        return super(MovieTheaterListSnippet, self).to_plist()