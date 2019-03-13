from time import time
import logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class AnalyserRegion():
    def init(self,rID,rName,rTypes):
        if not type(rID) == int:
            logger.error("Invalid rID: %s" % (str(rID)))
            return
        self.rID                = rID
        self.rName              = rName
        self.rTypes             = rTypes
        self.rBuys              = {}
        self.rLastBuysUpdate    = 0
        self.rSells             = {}
        self.rLastSellsUpdate   = 0
        self.rLastTypesUpdate   = 0

    def initByJSON(self,jsonInfo):
        if not type(jsonInfo) == dict:
            logger.error("Invalid initByJSON: %s" % (str(jsonInfo)))
            return
        self.rID                = jsonInfo['rID']
        self.rName              = jsonInfo['rName']
        self.rTypes             = jsonInfo['rTypes']
        self.rBuys              = jsonInfo['rBuys']
        self.rLastBuysUpdate    = jsonInfo['rLastBuysUpdate']
        self.rSells             = jsonInfo['rSells']
        self.rLastSellsUpdate   = jsonInfo['rLastSellsUpdate']
        self.rLastTypesUpdate   = jsonInfo['rLastTypesUpdate']

    def __init__(self,*args):
        if len(args) == 3:
            self.init( args[0], args[1], args[2] )
        elif len(args) == 1:
            self.init(jsonInfo)
        else:
            logger.error("Invalid init: %s" % (string(args)))
    def lowestSell(self,itemID):
        s=self.rSells[0]
        for i in self.rSells[1:]:
            if s < i['price']:
                s=i
        return s 

    def highestBuy(self,itemID):
        b=self.rBuys[0]
        for i in self.rBuys[1:]:
            if b > i['price']:
                b=i
        return b

    def setTypes(self,rTypes):
        self.rTypes=rTypes
        self.rLastTypesUpdate=time()

    def __eq__(self,other):
        if type(other) == int:
            return self.rID == other
        return self.rID == other.rID
    def __int__(self):
        return self.rID
    def __str__(self):
        return self.rName
