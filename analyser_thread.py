import threading
from esi import ESI_VERSION,ESI_URL
from region import getRegionIDByRegionName,getRegionNameByRegionID
from http.client import HTTPSConnection
from time import time,sleep
from analyser_region import AnalyserRegion

DEFAULT_REGION="Verge Vendor"

class Analyser(threading.Thread):
    def __init__(self):
        self.c = HTTPSConnection(ESI_URL)
        
        #list of AnalyserRegion
        self.regions=dict() #not sync'd yet
        rID=getRegionIDByRegionName(DEFAULT_REGION)
        self.regions[rID]=AnalyserRegion(rID,DEFAULT_REGION,[],0)

        self.updatePeriod=5*60
        self.term=False

    def addRegion(self,regionID):
        regionName=getRegionNameByRegionID(regionID)
        self.regions[regionID]=AnalyserRegion(
                regionID,
                regionName,
                [],
                0)

    def removeRegion(self,regionID):
        self.regions.pop(regionID)

    def updateAdjacentRegions(self):
        newRegions=getAdjacentRegionIDsByRegionID(self.regionID).get_json()
        for i in self.regions:
            if not i in newRegions:
                self.removeRegion(int(i))
        for i in newRegions:
            if not i in self.regions:
                self.addRegion(i)
                self.ESIGetBuys(i)

    def run(self):
        while not self.term:
            for region in self.regions:
                if region.rLastUpdate + self.updatePeriod < time():
                    self.ESIUpdateRelevantItems(int(region))

    def updateAllRelevantTypes(self):
        for i in self.regions:
            i.setTypes(self.ESIGetRelevantItems(int(i)))

    def ESIUpdateRelevantTypes(self,regionID):
        esiRelevant='/markets/%i/types/'
        self.c.request('GET',ESI_VERSION + (esiRelevant % (regionID)) )
        return self.c.getresponse().get_json()

    def ESIUpdateBuyOrders(self,regionID):
        return self.ESIUpdateOrders(regionID,"buy")

    def ESIUpdateSellOrders(self,regionID):
        return self.ESIUpdateOrders(regionID,"sell")

    def ESIUpdateOrders(self,regionID,order_type):
        for item in self.regions[regionID].rTypes:
            p=1
            while True:
                esiOrders='/markets/%i/orders/?datasource=tranquility&order_type=%s&page=1&type_id=%i'
                r = self.c.request('GET',ESI_VERSION+(esiOrders % (regionID,order_type,item))).get_json()
                if not self.regions[regionID].rBuys[item]:
                    self.regions[regionID].rBuys[item]=[]

                if len(r) == 0:
                    break
                self.regions[regionID].rBuys[item]+=r
                p+=1
