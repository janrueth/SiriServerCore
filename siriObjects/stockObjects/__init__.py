from siriObjects.baseObjects import ClientBoundCommand, ServerBoundCommand
from siriObjects.systemObjects import DomainObject
from siriObjects.uiObjects import UISnippet


class StockAdd(ClientBoundCommand):
    def __init__(self, refId):
        super(StockAdd, self).__init__("Add", "com.apple.ace.stock", None, refId)
        self.targetAppId = None # @"NSURL"
        self.companyName = None # @"NSString"
        self.stockReferences = None # @"NSArray"
        self.stocks = None # @"NSArray"
        self.tickerSymbol = None # @"NSString"
    
    def to_plist(self):
        self.add_property('targetAppId')
        self.add_property('companyName')
        self.add_property('stockReferences')
        self.add_property('stocks')
        self.add_property('tickerSymbol')
        return super(StockAdd, self).to_plist()

class StockAddCompleted(ServerBoundCommand):
    classIdentifier = "AddCompleted"
    groupIdentifier = "com.apple.ace.stock"
    def __init__(self, plist):
        self.aceStock = None # @"SAStockObject"
        self.identifier = None # @"NSURL"
        self.results = None # @"NSArray"
        self.stockReferences = None # @"NSArray"
        self.stocks = None # @"NSArray"
        super(StockAddCompleted, self).__init__(plist)

class StockDelete(ClientBoundCommand):
    def __init__(self, refId):
        super(StockDelete, self).__init__("Delete", "com.apple.ace.stock", None, refId)
        self.targetAppId = None # @"NSURL"
        self.stocks = None # @"NSArray"

    def to_plist(self):
        self.add_property('targetAppId')
        self.add_property('stocks')
        return super(StockDelete, self).to_plist()

class StockDeleteCompleted(ServerBoundCommand):
    classIdentifier = "DeleteCompleted"
    groupIdentifier = "com.apple.ace.stock"
    def __init__(self, plist):
        self.results = None # @"NSArray"
        self.stocks = None # @"NSArray"
        super(StockDeleteCompleted, self).__init__(plist)

class StockNews(DomainObject):
    def __init__(self):
        super(StockNews, self).__init__("com.apple.ace.stock", clazz="News")
        self.timeStamp = None # @"NSDate"
        self.title = None # @"NSString"
        self.url = None # @"NSString"

    def to_plist(self):
        self.add_property('timeStamp')
        self.add_property('title')
        self.add_property('url')
        return super(StockNews, self).to_plist()

class StockObject(DomainObject):
    DisplayStyleDISPLAYValue = "DISPLAY"
    DisplayStyleCOMPAREValue = "COMPARE"
    
    def __init__(self):
        super(StockObject, self).__init__("com.apple.ace.stock")
        self.averageDailyVolume = None # @"NSNumber"
        self.change = None # @"NSNumber"
        self.changePercent = None # @"NSNumber"
        self.chartData = None # @"NSString"
        self.currency = None # @"NSString"
        self.displayStyle = None # @"NSString"
        self.dividendYield = None # @"NSNumber"
        self.earningsPerShare = None # @"NSNumber"
        self.exchange = None # @"NSString"
        self.high = None # @"NSNumber"
        self.link = None # @"NSString"
        self.low = None # @"NSNumber"
        self.marketCap = None # @"NSString"
        self.name = None # @"NSString"
        self.open = None # @"NSNumber"
        self.peRatio = None # @"NSNumber"
        self.prevClose = None # @"NSNumber"
        self.price = None # @"NSNumber"
        self.realTimeChange = None # @"NSNumber"
        self.realTimeChangePercent = None # @"NSNumber"
        self.realTimePrice = None # @"NSNumber"
        self.realTimeTS = None # @"NSNumber"
        self.requests = None # @"NSArray"
        self.status = None # @"NSNumber"
        self.stockNews = None # @"NSArray"
        self.symbol = None # @"NSString"
        self.timeStamp = None # @"NSNumber"
        self.volume = None # @"NSNumber"
        self.yearRange = None # @"NSString"

    def to_plist(self):
        self.add_property('averageDailyVolume')
        self.add_property('change')
        self.add_property('changePercent')
        self.add_property('chartData')
        self.add_property('currency')
        self.add_property('displayStyle')
        self.add_property('dividendYield')
        self.add_property('earningsPerShare')
        self.add_property('exchange')
        self.add_property('high')
        self.add_property('link')
        self.add_property('low')
        self.add_property('marketCap')
        self.add_property('name')
        self.add_property('open')
        self.add_property('peRatio')
        self.add_property('prevClose')
        self.add_property('price')
        self.add_property('realTimeChange')
        self.add_property('realTimeChangePercent')
        self.add_property('realTimePrice')
        self.add_property('realTimeTS')
        self.add_property('requests')
        self.add_property('status')
        self.add_property('stockNews')
        self.add_property('symbol')
        self.add_property('timeStamp')
        self.add_property('volume')
        self.add_property('yearRange')
        return super(StockObject, self).to_plist()

class StockReference(DomainObject):
    def __init__(self):
        super(StockReference, self).__init__("com.apple.ace.stock", clazz="Reference")
        self.companyName = None # @"NSString"
        self.symbol = None # @"NSString"

    def to_plist(self):
        self.add_property('companyName')
        self.add_property('symbol')
        return super(StockReference, self).to_plist()

class StockRequest(DomainObject):
    RequestTypeNAMEValue = "NAME"
    RequestTypeSYMBOLValue = "SYMBOL"
    RequestTypePRICEValue = "PRICE"
    RequestTypeCHANGEValue = "CHANGE"
    RequestTypeCHANGE_PERCENTValue = "CHANGE_PERCENT"
    RequestTypeOPENValue = "OPEN"
    RequestTypeHIGHValue = "HIGH"
    RequestTypeHIGH_52WEEKValue = "HIGH_52WEEK"
    RequestTypeLOWValue = "LOW"
    RequestTypeLOW_52WEEKValue = "LOW_52WEEK"
    RequestTypeRANGE_52WEEKValue = "RANGE_52WEEK"
    RequestTypeVOLUMEValue = "VOLUME"
    RequestTypeAVG_DAILY_VOLUMEValue = "AVG_DAILY_VOLUME"
    RequestTypeMARKET_CAPValue = "MARKET_CAP"
    RequestTypePE_RATIOValue = "PE_RATIO"
    RequestTypeDIVIDEND_YIELDValue = "DIVIDEND_YIELD"
    RequestTypeREALTIME_CHANGEValue = "REALTIME_CHANGE"
    RequestTypeREALTIME_CHANGE_PERCENTValue = "REALTIME_CHANGE_PERCENT"
    RequestTypeREALTIME_PRICEValue = "REALTIME_PRICE"
    RequestTypePREVIOUS_CLOSEValue = "PREVIOUS_CLOSE"
    RequestTypeCHARTValue = "CHART"
    RequestTypeYEAR_RANGEValue = "YEAR_RANGE"
    RequestTypeHISTORICAL_PRICEValue = "HISTORICAL_PRICE"
    RequestTypeSTOCK_RETURNValue = "STOCK_RETURN"
    RequestTypeNEWSValue = "NEWS"
    RequestTypeEARNINGS_PER_SHAREValue = "EARNINGS_PER_SHARE"
    
    def __init__(self):
        super(StockRequest, self).__init__("com.apple.ace.stock", clazz="Request")
        self.endDate = None # @"NSDate" -> python datetime.datetime
        self.requestType = None # @"NSString"
        self.startDate = None # @"NSDate" -> python datetime.datetime

    def to_plist(self):
        self.add_property('endDate')
        self.add_property('requestType')
        self.add_property('startDate')
        return super(StockRequest, self).to_plist()

class StockSearch(ClientBoundCommand):
    def __init__(self, refId):
        super(StockSearch, self).__init__("Search", "com.apple.ace.stock", None, refId)
        self.targetAppId = None # @"NSURL"
        self.companyNameList = None # @"NSArray"
        self.stockReferences = None # @"NSArray"

    def to_plist(self):
        self.add_property('targetAppId')
        self.add_property('companyNameList')
        self.add_property('stockReferences')
        return super(StockSearch, self).to_plist()

class StockSearchCompleted(ServerBoundCommand):
    classIdentifier = "SearchCompleted"
    groupIdentifier = "com.apple.ace.stock"
    def __init__(self, plist):
        self.stockList = None # @"NSArray"
        self.stockReferences = None # @"NSArray"
        super(StockSearchCompleted, self).__init__(plist)

class StockSnippet(UISnippet):
    def __init__(self):
        super(StockSnippet, self).__init__(group="com.apple.ace.stock")
        self.stocks = None # @"NSArray"

    def to_plist(self):
        self.add_property('stocks')
        return super(StockSnippet, self).to_plist()