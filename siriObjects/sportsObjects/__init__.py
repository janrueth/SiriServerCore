from siriObjects.systemObjects import DomainObject
from siriObjects.baseObjects import AceObject
from siriObjects.uiObjects import UISnippet

class SportsSnippet(UISnippet):
    def __init__(self):
        super(SportsSnippet, self).__init__("Snippet", "com.apple.ace.sports")
        self.league = None # @"SASportsLeague"
        self.punchOut = None # @"SAUIAppPunchOut"

    def to_plist(self):
        self.add_property('league')
        self.add_property('punchOut')
        return super(SportsSnippet, self).to_plist()

class SportsScheduleSnippet(SportsSnippet):
    def __init__(self):
        super(SportsScheduleSnippet, self).__init__("ScheduleSnippet", "com.apple.ace.sports")
        self.matchups = None # @"NSArray"

    def to_plist(self):
        self.add_property('matchups')
        return super(SportsScheduleSnippet, self).to_plist()
    
class SportsEntity(DomainObject):
    def __init__(self):
        super(SportsEntity, self).__init__("Entity", "com.apple.ace.sports")
        self.image = None # @"NSURL"
        self.league = None # @"SASportsLeague"
        self.name = None # @"NSString"
        self.punchout = None # @"SAUIAppPunchOut"

    def to_plist(self):
        self.add_property('image')
        self.add_property('league')
        self.add_property('name')
        self.add_property('punchout')
        return super(SportsEntity, self).to_plist()

class SportsMatchup(DomainObject):
    def __init__(self):
        super(SportsMatchup, self).__init__("Matchup", "com.apple.ace.sports")
        self.awayEntity = None # @"SASportsEntity"
        self.awayLineScores = None # @"NSArray"
        self.awayScore = None # @"NSString"
        self.currentPeriod = None # @"NSString"
        self.expectedLineScoreCount = None # @"NSNumber"
        self.favoredEntity = None # @"NSString"
        self.homeEntity = None # @"SASportsEntity"
        self.homeLineScores = None # @"NSArray"
        self.homeScore = None # @"NSString"
        self.line = None # @"NSString"
        self.location = None # @"NSString"
        self.locationName = None # @"NSString"
        self.matchupOrder = None # @"NSString"
        self.overUnder = None # @"NSString"
        self.periodDescription = None # @"NSString"
        self.punchout = None # @"SAUIAppPunchOut"
        self.startTime = None # @"NSDate"
        self.status = None # @"NSString"
        self.timeRemaining = None # @"NSString"
        self.title = None # @"NSString"
        self.tournamentSeriesDescription = None # @"NSString"
        self.tvChannels = None # @"NSArray"
        self.winningEntity = None # @"NSString"

    def to_plist(self):
        self.add_property('awayEntity')
        self.add_property('awayLineScores')
        self.add_property('awayScore')
        self.add_property('currentPeriod')
        self.add_property('expectedLineScoreCount')
        self.add_property('favoredEntity')
        self.add_property('homeEntity')
        self.add_property('homeLineScores')
        self.add_property('homeScore')
        self.add_property('line')
        self.add_property('location')
        self.add_property('locationName')
        self.add_property('matchupOrder')
        self.add_property('overUnder')
        self.add_property('periodDescription')
        self.add_property('punchout')
        self.add_property('startTime')
        self.add_property('status')
        self.add_property('timeRemaining')
        self.add_property('title')
        self.add_property('tournamentSeriesDescription')
        self.add_property('tvChannels')
        self.add_property('winningEntity')
        return super(SportsMatchup, self).to_plist()

class SportsAthlete(SportsEntity):
    def __init__(self):
        super(SportsAthlete, self).__init__("Athlete", "com.apple.ace.sports")
        self.activeTeam = None # @"SASportsTeam"
        self.athleteMetadata = None # @"NSArray"
        self.firstName = None # @"NSString"
        self.formattedMetadata = None # @"NSArray"
        self.gender = None # @"NSString"
        self.injured = None # @"NSNumber"
        self.lastName = None # @"NSString"
        self.position = None # @"NSString"
        self.previousTeams = None # @"NSArray"
        self.statistics = None # @"NSArray"

    def to_plist(self):
        self.add_property('activeTeam')
        self.add_property('athleteMetadata')
        self.add_property('firstName')
        self.add_property('formattedMetadata')
        self.add_property('gender')
        self.add_property('injured')
        self.add_property('lastName')
        self.add_property('position')
        self.add_property('previousTeams')
        self.add_property('statistics')
        return super(SportsAthlete, self).to_plist()

class SportsAthleteSnippet(SportsSnippet):
    def __init__(self):
        super(SportsAthleteSnippet, self).__init__("AthleteSnippet", "com.apple.ace.sports")
        self.athletes = None # @"NSArray"

    def to_plist(self):
        self.add_property('athletes')
        return super(SportsAthleteSnippet, self).to_plist()

class SportsBaseballMatchup(SportsMatchup):
    def __init__(self):
        super(SportsBaseballMatchup, self).__init__("BaseballMatchup", "com.apple.ace.sports")
        self.awayErrors = None # @"NSNumber"
        self.awayHits = None # @"NSNumber"
        self.balls = None # @"NSNumber"
        self.homeErrors = None # @"NSNumber"
        self.homeHits = None # @"NSNumber"
        self.inningStatus = None # @"NSString"
        self.onFirst = None # @"NSNumber"
        self.onSecond = None # @"NSNumber"
        self.onThird = None # @"NSNumber"
        self.outs = None # @"NSNumber"
        self.strikes = None # @"NSNumber"

    def to_plist(self):
        self.add_property('awayErrors')
        self.add_property('awayHits')
        self.add_property('balls')
        self.add_property('homeErrors')
        self.add_property('homeHits')
        self.add_property('inningStatus')
        self.add_property('onFirst')
        self.add_property('onSecond')
        self.add_property('onThird')
        self.add_property('outs')
        self.add_property('strikes')
        return super(SportsBaseballMatchup, self).to_plist()

class SportsEntityGroup(SportsEntity):
    def __init__(self):
        super(SportsEntityGroup, self).__init__("EntityGroup", "com.apple.ace.sports")
        self.entities = None # @"NSArray"
        self.groupType = None # @"NSString"

    def to_plist(self):
        self.add_property('entities')
        self.add_property('groupType')
        return super(SportsEntityGroup, self).to_plist()

class SportsLeague(AceObject):
    def __init__(self):
        super(SportsLeague, self).__init__("League", "com.apple.ace.sports")
        self.diplayedText = None # @"NSString"
        self.displayTeamLocationOverName = None # @"NSNumber"
        self.identifier = None # @"NSString"
        self.season = None # @"SASportsSeason"
        self.sport = None # @"NSString"

    def to_plist(self):
        self.add_property('diplayedText')
        self.add_property('displayTeamLocationOverName')
        self.add_property('identifier')
        self.add_property('season')
        self.add_property('sport')
        return super(SportsLeague, self).to_plist()

class SportsMatchupDetailsSnippet(SportsScheduleSnippet):
    def __init__(self):
        super(SportsMatchupDetailsSnippet, self).__init__("MatchupDetailsSnippet", "com.apple.ace.sports")

    def to_plist(self):
        return super(SportsMatchupDetailsSnippet, self).to_plist()

class SportsMatchupLineScore(AceObject):
    def __init__(self):
        super(SportsMatchupLineScore, self).__init__("MatchupLineScore", "com.apple.ace.sports")
        self.period = None # @"NSString"
        self.score = None # @"NSString"

    def to_plist(self):
        self.add_property('period')
        self.add_property('score')
        return super(SportsMatchupLineScore, self).to_plist()

class SportsMetadata(AceObject):
    def __init__(self):
        super(SportsMetadata, self).__init__("Metadata", "com.apple.ace.sports")
        self.average = None # @"NSNumber"
        self.identifier = None # @"NSString"
        self.name = None # @"NSString"
        self.selected = None # @"NSNumber"
        self.value = None # @"NSString"

    def to_plist(self):
        self.add_property('average')
        self.add_property('identifier')
        self.add_property('name')
        self.add_property('selected')
        self.add_property('value')
        return super(SportsMetadata, self).to_plist()

class SportsMetadataGroup(AceObject):
    def __init__(self):
        super(SportsMetadataGroup, self).__init__("MetadataGroup", "com.apple.ace.sports")
        self.description = None # @"NSString"
        self.metadata = None # @"NSArray"
        self.selected = None # @"NSNumber"

    def to_plist(self):
        self.add_property('description')
        self.add_property('metadata')
        self.add_property('selected')
        return super(SportsMetadataGroup, self).to_plist()

class SportsNewsItem(AceObject):
    def __init__(self):
        super(SportsNewsItem, self).__init__("NewsItem", "com.apple.ace.sports")
        self.link = None # @"NSURL"
        self.summary = None # @"NSString"
        self.title = None # @"NSString"

    def to_plist(self):
        self.add_property('link')
        self.add_property('summary')
        self.add_property('title')
        return super(SportsNewsItem, self).to_plist()


class SportsSeason(AceObject):
    def __init__(self):
        super(SportsSeason, self).__init__("Season", "com.apple.ace.sports")
        self.postSeason = None # @"SASportsSeasonRange"
        self.preSeason = None # @"SASportsSeasonRange"
        self.regularSeason = None # @"SASportsSeasonRange"

    def to_plist(self):
        self.add_property('postSeason')
        self.add_property('preSeason')
        self.add_property('regularSeason')
        return super(SportsSeason, self).to_plist()

class SportsSeasonRange(AceObject):
    def __init__(self):
        super(SportsSeasonRange, self).__init__("SeasonRange", "com.apple.ace.sports")
        self.end = None # @"NSDate"
        self.seasonType = None # @"NSString"
        self.start = None # @"NSDate"

    def to_plist(self):
        self.add_property('end')
        self.add_property('seasonType')
        self.add_property('start')
        return super(SportsSeasonRange, self).to_plist()

class SportsStandingsSnippet(SportsSnippet):
    def __init__(self):
        super(SportsStandingsSnippet, self).__init__("StandingsSnippet", "com.apple.ace.sports")
        self.columns = None # @"NSArray"
        self.entities = None # @"NSArray"
        self.selectedEntities = None # @"NSArray"
        self.showCardinalPositions = None # c

    def to_plist(self):
        self.add_property('columns')
        self.add_property('entities')
        self.add_property('selectedEntities')
        self.add_property('showCardinalPositions')
        return super(SportsStandingsSnippet, self).to_plist()

class SportsTeam(SportsEntity):
    def __init__(self):
        super(SportsTeam, self).__init__("Team", "com.apple.ace.sports")
        self.abbreviatedName = None # @"NSString"
        self.athletes = None # @"NSArray"
        self.awayLosses = None # @"NSString"
        self.awayWins = None # @"NSString"
        self.clinchedQualificationPosition = None # @"NSNumber"
        self.conferencePosition = None # @"NSNumber"
        self.gamesBehind = None # @"NSString"
        self.groupName = None # @"NSString"
        self.groupPosition = None # @"NSNumber"
        self.groupPositionDescription = None # @"NSString"
        self.homeLosses = None # @"NSString"
        self.homeWins = None # @"NSString"
        self.location = None # @"NSString"
        self.losses = None # @"NSString"
        self.news = None # @"NSArray"
        self.overtimeLosses = None # @"NSString"
        self.points = None # @"NSString"
        self.pointsAgainst = None # @"NSString"
        self.pointsFor = None # @"NSString"
        self.primaryColor = None # @"NSNumber"
        self.qualificationPosition = None # @"NSString"
        self.rankings = None # @"NSArray"
        self.secondaryColor = None # @"NSNumber"
        self.statistics = None # @"NSArray"
        self.streakNumber = None # @"NSString"
        self.streakType = None # @"NSString"
        self.ties = None # @"NSString"
        self.venueLocation = None # @"NSString"
        self.venueName = None # @"NSString"
        self.winPercentage = None # @"NSString"
        self.wins = None # @"NSString"

    def to_plist(self):
        self.add_property('abbreviatedName')
        self.add_property('athletes')
        self.add_property('awayLosses')
        self.add_property('awayWins')
        self.add_property('clinchedQualificationPosition')
        self.add_property('conferencePosition')
        self.add_property('gamesBehind')
        self.add_property('groupName')
        self.add_property('groupPosition')
        self.add_property('groupPositionDescription')
        self.add_property('homeLosses')
        self.add_property('homeWins')
        self.add_property('location')
        self.add_property('losses')
        self.add_property('news')
        self.add_property('overtimeLosses')
        self.add_property('points')
        self.add_property('pointsAgainst')
        self.add_property('pointsFor')
        self.add_property('primaryColor')
        self.add_property('qualificationPosition')
        self.add_property('rankings')
        self.add_property('secondaryColor')
        self.add_property('statistics')
        self.add_property('streakNumber')
        self.add_property('streakType')
        self.add_property('ties')
        self.add_property('venueLocation')
        self.add_property('venueName')
        self.add_property('winPercentage')
        self.add_property('wins')
        return super(SportsTeam, self).to_plist()

class SportsTeamRank(AceObject):
    def __init__(self):
        super(SportsTeamRank, self).__init__("TeamRank", "com.apple.ace.sports")
        self.position = None # @"NSNumber"
        self.primary = None # @"NSNumber"
        self.source = None # @"NSString"

    def to_plist(self):
        self.add_property('position')
        self.add_property('primary')
        self.add_property('source')
        return super(SportsTeamRank, self).to_plist()

class SportsTeamSnippet(SportsSnippet):
    def __init__(self):
        super(SportsTeamSnippet, self).__init__("TeamSnippet", "com.apple.ace.sports")
        self.teams = None # @"NSArray"

    def to_plist(self):
        self.add_property('teams')
        return super(SportsTeamSnippet, self).to_plist()