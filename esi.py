import httpcache
import requests
import threading
from time import sleep

ESI_PROTO = "https://"
ESI_URL = "esi.evetech.net"
ESI_VERSION = "/latest"

# ESI endpoints with params
# ( (<param_name>, <default_value>) )
# If default value is None, this parameter is required!

# {0} - region_id
ESI_MARKET_ORDERS = "/markets/%i/orders/"
ESI_MARKET_ORDERS_PARAMS = ( ('region_id', None), ('order_type', 'all'), ('page', 1), ('type_id', '') )

# {0} - region_id
ESI_MARKET_HISTORY = "/markets/%i/history/"
ESI_MARKET_HISTORY_PARAMS = ( ('region_id', None), ('type_id', None) )

# {0} - region_id
ESI_MARKET_TYPES="/markets/%i/types/"
ESI_MARKET_TYPES_PARAMS= (  ('region_id', None), ('page', 1) )

class ESIConnection(threading.Thread):

    def __init__(self):
        super(ESIConnection,self).__init__()
        from httpcache import CachingHTTPAdapter
        self.c = requests.Session()
        self.c.mount("https://", CachingHTTPAdapter(capacity=1000000))
        self.c.mount("http://", CachingHTTPAdapter(capacity=1000000))
        self.term = threading.Event()
        self.reqlist = []
        self.resplistlock = threading.Lock()
        self.nonce = 0
        self.reqlistlock = threading.Lock()

    def getBuyOrders(self,**kwargs):
        kwargs['order_type']='buy'
        for p in ESI_MARKET_ORDERS_PARAMS:
            if not p[0] in kwargs:
                if p[1] == None:
                    raise Exception("Required parameter missing: %s\nParams: %s" % (p,kwargs))
        return getJSONResp(self,ESI_MARKET_ORDERS % (regionID,),kwargs)
    def getJSONResp(self,req,params):
        r = [ req, params, threading.Event(), None ]

        self.reqlistlock.acquire()
        self.reqlist.append( r )
        self.reqlistlock.release()

        r[2].wait()
        return r[3]

    def processRequest(self,req,p):
        try:
            if not req[0] == '/':
                req = '/' + req
            req=ESI_PROTO+ESI_URL+ESI_VERSION+req
            resp = self.c.get(req,params=p)
            resp.raise_for_status()
            return resp.json()

        except requests.HTTPError as httpe:
            print("HTTPError on request %s:\n%s" 
                    % (req,str(httpe)))
            return []
        except ConnectionError as ce:
            print("ConnectionError on request %s:\n%s"
                    % (req,str(ce)))
            return []

        except ValueError as jde:
            print("ValueError on request %s:\n%s"
                    % (req, jde.msg))
            return []

    def run(self):
        while not self.term.is_set():
            if(len(self.reqlist)>0):
                for i in self.reqlist:
                    if self.term.is_set():
                        break
                    i[3] = self.processRequest(i[0],i[1])
                    i[2].set()
                    sleep(0.2)
            else:
                sleep(0.2)
        print("ESI thread terminated.")

    def terminate(self):
        print("Asking ESI thread to terminate...")
        self.term.set()
