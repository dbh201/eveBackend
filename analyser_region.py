from time import time

class AnalyserRegion():
    def __init__(self,rID,rName,rTypes):
        self.rID=rID
        self.rName=rName
        self.rTypes=rTypes
        self.rBuys={}
        self.rSells={}
        self.rLastUpdate=0

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
        self.rLastUpdate=time()

    def __eq__(self,other):
        if type(other) == int:
            return self.rID == other
        return self.rID == other.rID
    def __int__(self):
        return self.rID
    def __str__(self):
        return self.rName
