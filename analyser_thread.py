import threading
from esi import ESI_VERSION,ESI_URL
from region import getRegionIDByRegionName,getRegionNameByRegionID
from http.client import HTTPSConnection
from time import time,sleep
from analyser_region import AnalyserRegion

DEFAULT_REGION="Verge Vendor"

class Analyser(threading.Thread):
    def __init__(self):
        super(Analyser,self).__init__()
        self.c = HTTPSConnection(ESI_URL)
        
        #list of AnalyserRegion
        self.regions=dict() #not sync'd yet
        rID=getRegionIDByRegionName(DEFAULT_REGION).get_json()[0][0]
        self.regions[rID]=AnalyserRegion(rID,DEFAULT_REGION,[])

        self.updatePeriod=5*60
        self.typesUpdatePeriod=10*60
        self.lastTypesUpdate=0
        self.term=False

    def addRegion(self,regionID):
        regionName=getRegionNameByRegionID(regionID)
        self.regions[regionID]=AnalyserRegion(
                regionID,
                regionName,
                []
                )
    def terminate(self):
        self.term=True
        print("Asking the analyser thread to terminate")
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

    def run(self):
        print("Thread started.")
        print("Regions: %s" % (str(self.regions)))
        while not self.term:
            if(self.lastTypesUpdate + self.typesUpdatePeriod < time()):
                print("Updating type information for regions")
                self.updateAllRelevantTypes()
                self.lastTypesUpdate=time()
            for region in self.regions:
                print("Testing region %s" % (self.regions[region]))
                if(self.regions[region].rLastBuysUpdate + self.updatePeriod < time()):
                    print("Updating region buys %s" % (self.regions[region]))
                    self.ESIUpdateBuyOrders(region)
                    self.regions[region].rLastBuysUpdate=time() 

                    print("Updating region sells %s" % (self.regions[region]))
                    self.ESIUpdateSellOrders(region)
                    self.regions[region].rLastSellsUpdate=time() 
            sleep(1)
        print("Analyser thread terminated successfully")

    def updateAllRelevantTypes(self):
        for i in self.regions:
            self.regions[i].setTypes(self.ESIUpdateRelevantTypes(i))
            for t in self.regions[i].rTypes:
                self.regions[i].rBuys

    def ESIUpdateRelevantTypes(self,regionID):
        esiRelevant='/markets/%i/types/'
        print("Requesting type list for %s" % (regionID))
        self.c.request('GET',ESI_VERSION + (esiRelevant % (regionID)) )
        r=self.c.getresponse().read()
        print("Returned %s" % (r))
        return r

    def ESIUpdateBuyOrders(self,regionID):
        if not self.regions[regionID].rBuys:
            self.regions[regionID].rBuys={}
        for item in self.regions[regionID].rTypes:
            if not item in self.regions[regionID].rBuys:
                self.regions[regionID].rBuys[item]=[]
        return self.ESIUpdateOrders(regionID,"buy")

    def ESIUpdateSellOrders(self,regionID):
        if not self.regions[regionID].rSells:
            self.regions[regionID].rBuys={}
        for item in self.regions[regionID].rTypes:
            if not item in self.regions[regionID].rSells:
                self.regions[regionID].rSells=[]
        return self.ESIUpdateOrders(regionID,"sell")

    def ESIUpdateOrders(self,regionID,order_type):
        for item in self.regions[regionID].rTypes:
            p=1
            while True:
                esiOrders='/markets/%i/orders/?datasource=tranquility&order_type=%s&page=1&type_id=%i'
                self.c.request('GET',ESI_VERSION+(esiOrders % (regionID,order_type,item)))
                resp = self.c.getresponse()
                r=resp.read()
                if not resp.code == 200:
                    print("%s returned %i" % (esiOrders % (regionID,order_type,item),r.code))
                    break
                if len(r) == 0:
                    break
               
                self.regions[regionID].rBuys[item]+=r
                p+=1
global analyser
