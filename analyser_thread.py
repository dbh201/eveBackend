import threading
import esi
from region import getRegionIDByRegionName,getRegionNameByRegionID
from http.client import HTTPSConnection
from time import time,sleep
from time import sleep
from analyser_region import AnalyserRegion
import analyser_region_json as json

DEFAULT_REGION="Verge Vendor"

class Analyser(threading.Thread):
    def __init__(self,esicon):
        super(Analyser,self).__init__()
        self.c=esicon
        #list of AnalyserRegion
        try:
            self.loadState()
        except FileNotFoundError as ose:
            print(ose)
            print("Loading defaults...")
            self.regions=dict() #not sync'd yet
            rID=getRegionIDByRegionName(DEFAULT_REGION)[0][0]
            self.regions[rID]=AnalyserRegion(rID,DEFAULT_REGION,[])

        self.updatePeriod=5*60
        self.typesUpdatePeriod=10*60
        self.lastTypesUpdate=0
        self.term=threading.Event()
        self.suspend=threading.Event()
        self.suspend.set() # don't sync up until we're ready
        
    def addRegion(self,regionID):
        regionName=getRegionNameByRegionID(regionID)
        self.regions[regionID]=AnalyserRegion(
                regionID,
                regionName,
                []
                )

    def terminate(self):
        print("Asking the analyser thread to terminate...")
        self.term.set()
    def removeRegion(self,regionID):
        self.regions.pop(regionID)

    def saveState(self):
        fd=open('./analyser.json','w')
        json.dump(self.regions, fd, cls=json.RegionEncoder)
        fd.close()

    def loadState(self):
        fd=open('./analyser.json','r')
        regions_json=json.load(fd)
        for rid in regions_json:
            self.regions[rid]=AnalyserRegion(regions_json[rid])

    def updateAdjacentRegions(self):
        newRegions=getAdjacentRegionIDsByRegionID(self.regionID)
        for i in self.regions:
            if not i in newRegions:
                self.removeRegion(int(i))
        for i in newRegions:
            if not i in self.regions:
                self.addRegion(i)
    def pause(self):
        self.suspend.set()
    def resume(self):
        self.suspend.clear()
    def status(self):
        if self.suspend.is_set():
            return "Suspended"
        return "Active"
    def run(self):
        print("Thread started.")
        print("Regions: %s" % (str(self.regions)))
        while not self.term.is_set():
            if(self.suspend.is_set()):
                sleep(0.5)
                continue
            if(self.lastTypesUpdate + self.typesUpdatePeriod < time()):
                print("Updating type information for regions")
                self.updateAllRelevantTypes()
                self.lastTypesUpdate=time()
                for region in self.regions:
                    if(self.term.is_set()):
                        return
                    if(self.regions[region].rLastBuysUpdate + self.updatePeriod < time()):
                        print("Updating region buys %s" % (self.regions[region]))
                        self.ESIUpdateBuyOrders(region)
                        self.regions[region].rLastBuysUpdate=time() 

                        print("Updating region sells %s" % (self.regions[region]))
                        self.ESIUpdateSellOrders(region)
                        self.regions[region].rLastSellsUpdate=time() 
            sleep(1)
        print("Analyser thread terminated.")
        self.saveState()

    def updateAllRelevantTypes(self):
        for i in self.regions:
            if self.term.is_set():
                return
            self.regions[i].setTypes(self.ESIUpdateRelevantTypes(i))
            for t in self.regions[i].rTypes:
                self.regions[i].rBuys

    def ESIUpdateRelevantTypes(self,regionID):
        esiRelevant='/markets/%i/types/'
        print("Requesting type list for %s" % (regionID))
        r=self.c.getJSONResp( esiRelevant % (regionID) )
        print("Returned %s" % (r))
        return r

    def ESIUpdateBuyOrders(self,regionID):
        if not self.regions[regionID].rBuys:
            self.regions[regionID].rBuys={}
        return self.ESIUpdateOrders(regionID,"buy",self.regions[regionID].rBuys)

    def ESIUpdateSellOrders(self,regionID):
        if not self.regions[regionID].rSells:
            self.regions[regionID].rBuys={}
        return self.ESIUpdateOrders(regionID,"sell",self.regions[regionID].rSells)

    def ESIUpdateOrders(self,regionID,order_type,dest_dict):
        for item in self.regions[regionID].rTypes:
            if self.term.is_set():
                return
            print("Updating item %i for %s" % (item, self.regions[regionID]))
            p=1
            while not self.term.is_set():
                r=self.c.getBuyOrders(regionID,p,item)
                print("Retrieved page %i of length %i:\n%s" % (p,len(r),r))
                if len(r) == 0:
                    break
                if not item in dest_dict:
                    dest_dict[item]=[]
                dest_dict[item]+=r
                p+=1
