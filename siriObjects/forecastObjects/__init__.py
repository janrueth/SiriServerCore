#Author: Sebastian Koch
from siriObjects.baseObjects import ClientBoundCommand, AceObject
import logging
class SiriForecastSnippet(AceObject):
    def __init__(self, aceWeathers=[]):
        logging.getLogger().warning("THIS OBJECT IS DEPRECATED AND WILL BE REMOVED IN FUTURE RELEASES, PLEASE USE THE WEATHER OBJECTS")
        super(SiriForecastSnippet, self).__init__("ForecastSnippet", "com.apple.ace.weather")
        self.aceWeathers = aceWeathers
      
    def to_plist(self):
        self.add_property('aceWeathers')
        return super(SiriForecastSnippet, self).to_plist()
        
class SiriForecastAceWeathers(AceObject):
    def __init__(self, currentConditions=None, dailyForecasts=None, hourlyForecasts=None, view="HOURLY", weatherLocation=None, extendedForecastUrl="http://m.yahoo.com/search?p=Frankfurt,+HE&.tsrc=appleww", units=None):
        logging.getLogger().warning("THIS OBJECT IS DEPRECATED AND WILL BE REMOVED IN FUTURE RELEASES, PLEASE USE THE WEATHER OBJECTS")
        super(SiriForecastAceWeathers, self).__init__("Object", "com.apple.ace.weather")
        self.currentConditions = currentConditions
        self.hourlyForecasts = hourlyForecasts
        self.dailyForecasts = dailyForecasts
        self.view = view
        self.weatherLocation = weatherLocation
        self.extendedForecastUrl = extendedForecastUrl
        self.units = units
 
    def to_plist(self):
        self.add_property('currentConditions')
        self.add_property('hourlyForecasts')
        self.add_property('dailyForecasts')
        self.add_property('view')
        self.add_property('weatherLocation')
        self.add_property('extendedForecastUrl')
        self.add_property('units')
        return super(SiriForecastAceWeathers, self).to_plist()
        
class SiriForecastAceWeathersHourlyForecast(AceObject):
    def __init__(self, chanceOfPrecipitation=0, isUserRequested=True,condition=None, temperature=0, timeIndex=20):
        logging.getLogger().warning("THIS OBJECT IS DEPRECATED AND WILL BE REMOVED IN FUTURE RELEASES, PLEASE USE THE WEATHER OBJECTS")
        super(SiriForecastAceWeathersHourlyForecast, self).__init__("HourlyForecast", "com.apple.ace.weather")
        self.chanceOfPrecipitation = chanceOfPrecipitation
        self.isUserRequested = isUserRequested
        self.condition = condition
        self.temperature = temperature
        self.timeIndex = timeIndex
 
    def to_plist(self):
        self.add_property('chanceOfPrecipitation')
        self.add_property('isUserRequested')
        self.add_property('condition')
        self.add_property('temperature')
        self.add_property('timeIndex')
        return super(SiriForecastAceWeathersHourlyForecast, self).to_plist()
        
class SiriForecastAceWeathersDailyForecast(AceObject):
    
    def __init__(self, chanceOfPerception=0, isUserRequested=True,condition=None, lowTemperature=0, highTemperature=0, timeIndex=1):
        logging.getLogger().warning("THIS OBJECT IS DEPRECATED AND WILL BE REMOVED IN FUTURE RELEASES, PLEASE USE THE WEATHER OBJECTS")
        super(SiriForecastAceWeathersDailyForecast, self).__init__("DailyForecast", "com.apple.ace.weather")
        self.chanceOfPerception = chanceOfPerception
        self.isUserRequested = isUserRequested
        self.condition = condition
        self.highTemperature = highTemperature
        self.lowTemperature = lowTemperature
        self.timeIndex = timeIndex
 
    def to_plist(self):
        self.add_property('chanceOfPerception')
        self.add_property('isUserRequested')
        self.add_property('condition')
        self.add_property('highTemperature')
        self.add_property('lowTemperature')
        self.add_property('timeIndex')
        return super(SiriForecastAceWeathersDailyForecast, self).to_plist()

class SiriForecastAceWeathersWeatherLocation(AceObject):
    def __init__(self, locationId="20066682", countryCode="Germany", city="Frankfurt", stateCode = "Hesse"):
        logging.getLogger().warning("THIS OBJECT IS DEPRECATED AND WILL BE REMOVED IN FUTURE RELEASES, PLEASE USE THE WEATHER OBJECTS")
        super(SiriForecastAceWeathersWeatherLocation, self).__init__("Location", "com.apple.ace.weather")
        self.locationId = locationId
        self.countryCode = countryCode
        self.city = city
        self.stateCode = stateCode
 
    def to_plist(self):
        self.add_property('locationId')
        self.add_property('countryCode')
        self.add_property('city')
        self.add_property('stateCode')
        return super(SiriForecastAceWeathersWeatherLocation, self).to_plist()
        
        
class SiriForecastAceWeathersUnits(AceObject):
    def __init__(self, speedUnits="KPH", distanceUnits="Kilometers", temperatureUnits="Celsius", pressureUnits = "MB"):
        logging.getLogger().warning("THIS OBJECT IS DEPRECATED AND WILL BE REMOVED IN FUTURE RELEASES, PLEASE USE THE WEATHER OBJECTS")
        super(SiriForecastAceWeathersUnits, self).__init__("Units", "com.apple.ace.weather")
        self.speedUnits = speedUnits
        self.distanceUnits = distanceUnits
        self.temperatureUnits = temperatureUnits
        self.pressureUnits = pressureUnits
 
    def to_plist(self):
        self.add_property('speedUnits')
        self.add_property('distanceUnits')
        self.add_property('temperatureUnits')
        self.add_property('pressureUnits')
        return super(SiriForecastAceWeathersUnits, self).to_plist()
        
class SiriForecastAceWeathersCurrentConditions(AceObject):
    def __init__(self, feelsLike="0", dayOfWeek=6, timeOfObservation="18:00",barometricPressure=None, visibility="0", percentOfMoonFaceVisible=90, temperature = "0", sunrise="7:30", sunset="19:00", moonPhase="WAXING_GIBBOUS",percentHumidity="80", timeZone="Central European Time", dewPoint="0", condition=None, windChill="0", windSpeed=None,):
        logging.getLogger().warning("THIS OBJECT IS DEPRECATED AND WILL BE REMOVED IN FUTURE RELEASES, PLEASE USE THE WEATHER OBJECTS")
        super(SiriForecastAceWeathersCurrentConditions, self).__init__("CurrentConditions", "com.apple.ace.weather")
        self.feelsLike = feelsLike
        self.dayOfWeek = dayOfWeek
        self.timeOfObservation = timeOfObservation
        self.barometricPressure = barometricPressure
        self.visibility = visibility
        self.percentOfMoonFaceVisible = percentOfMoonFaceVisible
        self.temperature = temperature
        self.sunrise = sunrise
        self.sunset = sunset
        self.moonPhase = moonPhase
        self.percentHumidity = percentHumidity
        self.timeZone = timeZone
        self.dewPoint = dewPoint
        self.condition = condition
        self.windChill = windChill
        self.windSpeed = windSpeed


    def to_plist(self):
        self.add_property('feelsLike')
        self.add_property('dayOfWeek')
        self.add_property('timeOfObservation')
        self.add_property('barometricPressure')
        self.add_property('visibility')
        self.add_property('percentOfMoonFaceVisible')
        self.add_property('temperature')
        self.add_property('sunrise')
        self.add_property('sunset')
        self.add_property('moonPhase')
        self.add_property('percentHumidity')
        self.add_property('timeZone')
        self.add_property('dewPoint')
        self.add_property('condition')
        self.add_property('windChill')
        self.add_property('windSpeed')
        return super(SiriForecastAceWeathersCurrentConditions, self).to_plist()  
        
class SiriForecastAceWeathersConditions(AceObject):
    def __init__(self, conditionCode="Sunny", conditionCodeIndex=32):
        logging.getLogger().warning("THIS OBJECT IS DEPRECATED AND WILL BE REMOVED IN FUTURE RELEASES, PLEASE USE THE WEATHER OBJECTS")
        super(SiriForecastAceWeathersConditions, self).__init__("Condition", "com.apple.ace.weather")
        self.conditionCode = conditionCode
        self.conditionCodeIndex = conditionCodeIndex

 
    def to_plist(self):
        self.add_property('conditionCode')
        self.add_property('conditionCodeIndex')
        return super(SiriForecastAceWeathersConditions, self).to_plist() 