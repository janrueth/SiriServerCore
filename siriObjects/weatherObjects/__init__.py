from siriObjects.baseObjects import AceObject, ClientBoundCommand, \
    ServerBoundCommand
from siriObjects.systemObjects import Location, DomainObject
from siriObjects.uiObjects import UISnippet


class WeatherBarometricPressure(AceObject):
    TrendSteadyValue = "Steady"
    TrendRisingValue = "Rising"
    TrendFallingValue = "Falling"
    def __init__(self):
        super(WeatherBarometricPressure, self).__init__("BarometricPressure", "com.apple.ace.weather")
        self.trend = None # @"NSString"
        self.value = None # @"NSString"

    def to_plist(self):
        self.add_property('trend')
        self.add_property('value')
        return super(WeatherBarometricPressure, self).to_plist()

class WeatherCondition(AceObject):
    ConditionCodeTornadoValue = "Tornado"
    ConditionCodeTropical_StormValue = "Tropical_Storm"
    ConditionCodeHurricaneValue = "Hurricane"
    ConditionCodeSevere_ThunderstormsValue = "Severe_Thunderstorms"
    ConditionCodeThunderstormsValue = "Thunderstorms"
    ConditionCodeMixedRainAndSnowValue = "MixedRainAndSnow"
    ConditionCodeMixedRainAndSleetValue = "MixedRainAndSleet"
    ConditionCodeMixedSnowAndSleetValue = "MixedSnowAndSleet"
    ConditionCodeFreezingDrizzleValue = "FreezingDrizzle"
    ConditionCodeDrizzleValue = "Drizzle"
    ConditionCodeFreezingRainValue = "FreezingRain"
    ConditionCodeShowersValue = "Showers"
    ConditionCodeShowers2Value = "Showers2"
    ConditionCodeSnowFlurriesValue = "SnowFlurries"
    ConditionCodeLightSnowShowersValue = "LightSnowShowers"
    ConditionCodeBlowingSnowValue = "BlowingSnow"
    ConditionCodeSnowValue = "Snow"
    ConditionCodeHailValue = "Hail"
    ConditionCodeSleetValue = "Sleet"
    ConditionCodeDustValue = "Dust"
    ConditionCodeFoggyValue = "Foggy"
    ConditionCodeHazeValue = "Haze"
    ConditionCodeSmokyValue = "Smoky"
    ConditionCodeBlusteryValue = "Blustery"
    ConditionCodeWindyValue = "Windy"
    ConditionCodeColdValue = "Cold"
    ConditionCodeCloudyValue = "Cloudy"
    ConditionCodeMostlyCloudyNightValue = "MostlyCloudyNight"
    ConditionCodeMostlyCloudyDayValue = "MostlyCloudyDay"
    ConditionCodePartlyCloudyNightValue = "PartlyCloudyNight"
    ConditionCodePartlyCloudyDayValue = "PartlyCloudyDay"
    ConditionCodeClearNightValue = "ClearNight"
    ConditionCodeSunnyValue = "Sunny"
    ConditionCodeFairNightValue = "FairNight"
    ConditionCodeFairDayValue = "FairDay"
    ConditionCodeMixedRainAndHailValue = "MixedRainAndHail"
    ConditionCodeHotValue = "Hot"
    ConditionCodeIsolatedThunderstormsValue = "IsolatedThunderstorms"
    ConditionCodeScatteredThunderstormsValue = "ScatteredThunderstorms"
    ConditionCodeScatteredThunderstorms2Value = "ScatteredThunderstorms2"
    ConditionCodeScatteredShowersValue = "ScatteredShowers"
    ConditionCodeHeavySnowValue = "HeavySnow"
    ConditionCodeScatteredSnowShowersValue = "ScatteredSnowShowers"
    ConditionCodeHeavySnow2Value = "HeavySnow2"
    ConditionCodePartlyCloudyValue = "PartlyCloudy"
    ConditionCodeThundershowersValue = "Thundershowers"
    ConditionCodeSnowShowersValue = "SnowShowers"
    ConditionCodeIsolatedThundershowersValue = "IsolatedThundershowers"
    ConditionCodeNotAvailableValue = "NotAvailable"
    
    ConditionCodeIndexTable = { 0: ConditionCodeTornadoValue,
                                1: ConditionCodeTropical_StormValue,
                                2: ConditionCodeHurricaneValue,
                                3: ConditionCodeSevere_ThunderstormsValue,
                                4: ConditionCodeThunderstormsValue,
                                5: ConditionCodeMixedRainAndSnowValue,
                                6: ConditionCodeMixedRainAndSleetValue,
                                7: ConditionCodeMixedSnowAndSleetValue,
                                8: ConditionCodeFreezingDrizzleValue,
                                9: ConditionCodeDrizzleValue,
                                10: ConditionCodeFreezingRainValue,
                                11: ConditionCodeShowersValue,
                                12: ConditionCodeShowers2Value,
                                13: ConditionCodeSnowFlurriesValue,
                                14: ConditionCodeLightSnowShowersValue,
                                15: ConditionCodeBlowingSnowValue,
                                16: ConditionCodeSnowValue,
                                17: ConditionCodeHailValue,
                                18: ConditionCodeSleetValue,
                                19: ConditionCodeDustValue,
                                20: ConditionCodeFoggyValue,
                                21: ConditionCodeHazeValue,
                                22: ConditionCodeSmokyValue,
                                23: ConditionCodeBlusteryValue,
                                24: ConditionCodeWindyValue,
                                25: ConditionCodeColdValue,
                                26: ConditionCodeCloudyValue,
                                27: ConditionCodeMostlyCloudyNightValue,
                                28: ConditionCodeMostlyCloudyDayValue,
                                29: ConditionCodePartlyCloudyNightValue,
                                30: ConditionCodePartlyCloudyDayValue,
                                31: ConditionCodeClearNightValue,
                                32: ConditionCodeSunnyValue,
                                33: ConditionCodeFairNightValue,
                                34: ConditionCodeFairDayValue,
                                35: ConditionCodeMixedRainAndHailValue,
                                36: ConditionCodeHotValue,
                                37: ConditionCodeIsolatedThunderstormsValue,
                                38: ConditionCodeScatteredThunderstormsValue,
                                39: ConditionCodeScatteredThunderstorms2Value,
                                40: ConditionCodeScatteredShowersValue,
                                41: ConditionCodeHeavySnowValue,
                                42: ConditionCodeScatteredSnowShowersValue,
                                43: ConditionCodeHeavySnow2Value,
                                44: ConditionCodePartlyCloudyValue,
                                45: ConditionCodeThundershowersValue,
                                46: ConditionCodeSnowShowersValue,
                                47: ConditionCodeIsolatedThundershowersValue,
                                3200: ConditionCodeNotAvailableValue
                            }
    def __init__(self):
        super(WeatherCondition, self).__init__("Condition", "com.apple.ace.weather")
        self.conditionCode = None # @"NSString"
        self.conditionCodeIndex = None # i

    def to_plist(self):
        self.add_property('conditionCode')
        self.add_property('conditionCodeIndex')
        return super(WeatherCondition, self).to_plist()

class WeatherCurrentConditions(AceObject):
    MoonPhaseNEWValue = "NEW"
    MoonPhaseWAXING_CRESCENTValue = "WAXING_CRESCENT"
    MoonPhaseFIRST_QUARTERValue = "FIRST_QUARTER"
    MoonPhaseWAXING_GIBBOUSValue = "WAXING_GIBBOUS"
    MoonPhaseFULLValue = "FULL"
    MoonPhaseWANING_GIBBOUSValue = "WANING_GIBBOUS"
    MoonPhaseTHIRD_QUARTERValue = "THIRD_QUARTER"
    MoonPhaseWANING_CRESCENTValue = "WANING_CRESCENT"
    def __init__(self):
        super(WeatherCurrentConditions, self).__init__("CurrentConditions", "com.apple.ace.weather")
        self.barometricPressure = None # @"WeatherBarometricPressure"
        self.condition = None # @"WeatherCondition"
        self.dayOfWeek = None # @"NSNumber"
        self.dewPoint = None # @"NSString"
        self.feelsLike = None # @"NSString"
        self.heatIndex = None # @"NSString"
        self.moonPhase = None # @"NSString"
        self.percentHumidity = None # @"NSString"
        self.percentOfMoonFaceVisible = None # @"NSNumber"
        self.sunrise = None # @"NSString"
        self.sunset = None # @"NSString"
        self.temperature = None # @"NSString"
        self.timeOfObservation = None # @"NSString"
        self.timeZone = None # @"NSString"
        self.visibility = None # @"NSString"
        self.windChill = None # @"NSString"
        self.windSpeed = None # @"WeatherWindSpeed"

    def to_plist(self):
        self.add_property('barometricPressure')
        self.add_property('condition')
        self.add_property('dayOfWeek')
        self.add_property('dewPoint')
        self.add_property('feelsLike')
        self.add_property('heatIndex')
        self.add_property('moonPhase')
        self.add_property('percentHumidity')
        self.add_property('percentOfMoonFaceVisible')
        self.add_property('sunrise')
        self.add_property('sunset')
        self.add_property('temperature')
        self.add_property('timeOfObservation')
        self.add_property('timeZone')
        self.add_property('visibility')
        self.add_property('windChill')
        self.add_property('windSpeed')
        return super(WeatherCurrentConditions, self).to_plist()


class WeatherForecast(AceObject):
    def __init__(self, clazz="Forecast", group="com.apple.ace.weather"):
        super(WeatherForecast, self).__init__(clazz, group)
        self.chanceOfPrecipitation = None # @"NSNumber"
        self.condition = None # @"WeatherCondition"
        self.isUserRequested = None # @"NSNumber"
        self.timeIndex = None # @"NSNumber"

    def to_plist(self):
        self.add_property('chanceOfPrecipitation')
        self.add_property('condition')
        self.add_property('isUserRequested')
        self.add_property('timeIndex')
        return super(WeatherForecast, self).to_plist()


class WeatherDailyForecast(WeatherForecast):
    def __init__(self):
        super(WeatherDailyForecast, self).__init__("DailyForecast", "com.apple.ace.weather")
        self.highTemperature = None # @"NSNumber"
        self.lowTemperature = None # @"NSNumber"

    def to_plist(self):
        self.add_property('highTemperature')
        self.add_property('lowTemperature')
        return super(WeatherDailyForecast, self).to_plist()

class WeatherForecastSnippet(UISnippet):
    def __init__(self):
        super(WeatherForecastSnippet, self).__init__("ForecastSnippet", "com.apple.ace.weather")
        self.aceWeathers = None # @"NSArray"

    def to_plist(self):
        self.add_property('aceWeathers')
        return super(WeatherForecastSnippet, self).to_plist()

class WeatherHourlyForecast(WeatherForecast):
    def __init__(self):
        super(WeatherHourlyForecast, self).__init__("HourlyForecast", "com.apple.ace.weather")
        self.temperature = None # @"NSNumber"

    def to_plist(self):
        self.add_property('temperature')
        return super(WeatherHourlyForecast, self).to_plist()

class WeatherLocation(Location):
    def __init__(self):
        super(WeatherLocation, self).__init__(group="com.apple.ace.weather")
        self.locationId = None # @"NSString"

    def to_plist(self):
        self.add_property('locationId')
        return super(WeatherLocation, self).to_plist()

class WeatherLocationAdd(ClientBoundCommand):
    def __init__(self, refId):
        super(WeatherLocationAdd, self).__init__("LocationAdd", "com.apple.ace.weather", None, refId)
        self.targetAppId = None # @"NSURL"
        self.weatherLocation = None # @"WeatherLocation"

    def to_plist(self):
        self.add_property('targetAppId')
        self.add_property('weatherLocation')
        return super(WeatherLocationAdd, self).to_plist()

class WeatherLocationAddCompleted(ServerBoundCommand):
    classIdentifier = "LocationAddCompleted"
    groupIdentifier = "com.apple.ace.weather"
    
    ErrorAlreadyExistsValue = "AlreadyExists"
    ErrorMaxNumberExceededValue = "MaxNumberExceeded"
    def __init__(self, plist):
        self.error = None # @"NSString"
        self.weatherLocationId = None # @"NSURL"
        super(WeatherLocationAddCompleted, self).__init__(plist)

class WeatherLocationDelete(ClientBoundCommand):
    def __init__(self, refId):
        super(WeatherLocationDelete, self).__init__("LocationDelete", "com.apple.ace.weather", None, refId)
        self.targetAppId = None # @"NSURL"
        self.weatherLocation = None # @"WeatherLocation"

    def to_plist(self):
        self.add_property('targetAppId')
        self.add_property('weatherLocation')
        return super(WeatherLocationDelete, self).to_plist()

class WeatherLocationDeleteCompleted(ServerBoundCommand):
    classIdentifier = "LocationDeleteCompleted"
    groupIdentifier = "com.apple.ace.weather"
    def __init__(self, plist):
        self.refId = None # @"NSString"
        self.aceId = None # @"NSString"
        super(WeatherLocationDeleteCompleted, self).__init__(plist)

class WeatherLocationSearch(ClientBoundCommand):
    def __init__(self, refId):
        super(WeatherLocationSearch, self).__init__("LocationSearch", "com.apple.ace.weather", None, refId)
        self.targetAppId = None # @"NSURL"
        self.identifier = None # @"NSURL"
        self.locationId = None # @"NSString"

    def to_plist(self):
        self.add_property('targetAppId')
        self.add_property('identifier')
        self.add_property('locationId')
        return super(WeatherLocationSearch, self).to_plist()

class WeatherLocationSearchCompleted(ServerBoundCommand):
    classIdentifier = "LocationSearchCompleted"
    groupIdentifier = "com.apple.ace.weather"
    def __init__(self, plist):
        self.weatherLocations = None # @"NSArray"
        super(WeatherLocationSearchCompleted, self).__init__(plist)

class WeatherLocationSnippet(UISnippet):
    def __init__(self):
        super(WeatherLocationSnippet, self).__init__("LocationSnippet", "com.apple.ace.weather")
        self.weatherLocations = None # @"NSArray"

    def to_plist(self):
        self.add_property('weatherLocations')
        return super(WeatherLocationSnippet, self).to_plist()

class WeatherObject(DomainObject):
    ViewDAILYValue = "DAILY"
    ViewHOURLYValue = "HOURLY"
    def __init__(self):
        super(WeatherObject, self).__init__("com.apple.ace.weather")
        self.currentConditions = None # @"WeatherCurrentConditions"
        self.dailyForecasts = None # @"NSArray"
        self.extendedForecastUrl = None # @"NSString"
        self.hourlyForecasts = None # @"NSArray"
        self.units = None # @"WeatherUnits"
        self.view = None # @"NSString"
        self.weatherLocation = None # @"WeatherLocation"

    def to_plist(self):
        self.add_property('currentConditions')
        self.add_property('dailyForecasts')
        self.add_property('extendedForecastUrl')
        self.add_property('hourlyForecasts')
        self.add_property('units')
        self.add_property('view')
        self.add_property('weatherLocation')
        return super(WeatherObject, self).to_plist()

class WeatherShowWeatherLocations(ClientBoundCommand):
    def __init__(self, refId):
        super(WeatherShowWeatherLocations, self).__init__("ShowWeatherLocations", "com.apple.ace.weather", None, refId)
        self.targetAppId = None # @"NSURL"

    def to_plist(self):
        self.add_property('targetAppId')
        return super(WeatherShowWeatherLocations, self).to_plist()

class WeatherShowWeatherLocationsCompleted(ServerBoundCommand):
    classIdentifier = "ShowWeatherLocationsCompleted"
    groupIdentifier = "com.apple.ace.weather"
    def __init__(self, plist):
        super(WeatherShowWeatherLocationsCompleted, self).__init__(plist)

class WeatherUnits(AceObject):
    DistanceUnitsFeetValue = "Feet"
    DistanceUnitsMilesValue = "Miles"
    DistanceUnitsMetersValue = "Meters"
    DistanceUnitsKilometersValue = "Kilometers"
    
    PressureUnitsINValue = "IN"
    PressureUnitsMBValue = "MB"
    
    SpeedUnitsMPHValue = "MPH"
    SpeedUnitsKPHValue = "KPH"
    
    TemperatureUnitsCelsiusValue = "Celsius"
    TemperatureUnitsFahrenheitValue = "Fahrenheit"
    def __init__(self):
        super(WeatherUnits, self).__init__("Units", "com.apple.ace.weather")
        self.distanceUnits = None # @"NSString"
        self.pressureUnits = None # @"NSString"
        self.speedUnits = None # @"NSString"
        self.temperatureUnits = None # @"NSString"

    def to_plist(self):
        self.add_property('distanceUnits')
        self.add_property('pressureUnits')
        self.add_property('speedUnits')
        self.add_property('temperatureUnits')
        return super(WeatherUnits, self).to_plist()

class WeatherWindSpeed(AceObject):
    DirectionNorthValue = "North"
    DirectionNorthEastValue = "NorthEast"
    DirectionEastValue = "East"
    DirectionSouthEastValue = "SouthEast"
    DirectionSouthValue = "South"
    DirectionSouthWestValue = "SouthWest"
    DirectionWestValue = "West"
    DirectionNorthWestValue = "NorthWest"
    def __init__(self):
        super(WeatherWindSpeed, self).__init__("WindSpeed", "com.apple.ace.weather")
        self.value = None # @"NSString"
        self.windDirection = None # @"NSString"
        self.windDirectionDegree = None # @"NSNumber"

    def to_plist(self):
        self.add_property('value')
        self.add_property('windDirection')
        self.add_property('windDirectionDegree')
        return super(WeatherWindSpeed, self).to_plist()