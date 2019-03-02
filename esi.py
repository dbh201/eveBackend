import httpcache
import requests
import threading
from time import sleep

ESI_PROTO = "https://"
ESI_URL = "esi.evetech.net"
ESI_VERSION="/latest"

class ESIConnection(threading.Thread):

    def __init__(self):
        super(ESIConnection,self).__init__()
        from httpcache import CachingHTTPAdapter
        self.c = requests.Session()
        self.c.mount("https://", CachingHTTPAdapter(capacity=1000000))
        self.c.mount("http://", CachingHTTPAdapter(capacity=1000000))
        self.term = threading.Event()
        self.reqlist = []
        self.resplist = {}
        self.resplistlock = threading.Lock()
        self.nonce = 0
        self.reqlistlock = threading.Lock()

    def getNonce(self):
        self.nonce+=1
        return self.nonce

    def getJSONResp(self,req):
        r = [ req, threading.Event(), None ]

        self.reqlistlock.acquire()
        self.reqlist.append( r )
        self.reqlistlock.release()

        r[1].wait()
        return r[2]

    def processRequest(self,req):
        try:
            if not req[0] == '/':
                req = '/' + req
            req=ESI_PROTO+ESI_URL+ESI_VERSION+req
            resp = self.c.get(req)
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
                    i[2] = self.processRequest(i[0])
                    i[1].set()
                    sleep(0.2)
            else:
                sleep(0.2)
        print("ESI thread terminated.")

    def terminate(self):
        print("Asking ESI thread to terminate...")
        self.term.set()
