from flask import Blueprint
import http.client
from esi import ESI,ESI_VERSION
from region import getRegionIDByRegionName,getItemIDByItemName
API = http.client.HTTPSConnection("localhost")
# IMPORTANT NOTES:
# in the SDE, items (inventory items) information
# is in the invTypes table.

# objects (items in space, not in inventory) information
# is in the invItems table.
# invNames contains names for objects only

# invTypes contains all (most?) pertinent information on 
# inventory items

_market = Blueprint('_market',__name__)
_prefix = '/market'

###
@_market.route('/buys/<int:regionID>/<int:itemID>/<int:pageNum>', methods=['GET'])
def getMarketBuysByRegionIDItemID(regionID,itemID,pageNum):
    ESI.request('GET',ESI_VERSION+'/markets/%i/orders/?datasource=tranquility&order_type=buy&page=%i&type_id=%i'%(regionID,pageNum,itemID))
    a=ESI.getresponse().read()
    return a
###

###
@_market.route('/buys/<string:regionName>/<int:itemID>/<int:pageNum>', methods=['GET'])
def getMarketBuysByRegionNameItemID(regionName,itemID,pageNum):
    regionID=getRegionIDByRegionName(regionName).get_json()[0][0]
    ESI.request('GET',ESI_VERSION+'/markets/%i/orders/?datasource=tranquility&order_type=buy&page=%i&type_id=%i'%(regionID,pageNum,itemID))
    a=ESI.getresponse().read()
    return a
###

###
@_market.route('/buys/<string:regionName>/<int:itemID>/<int:pageNum>', methods=['GET'])
def getMarketBuysByRegionIDItemName(regionID,itemName,pageNum):
    itemID=getItemIDByItemName(itemName)
    ESI.request('GET',ESI_VERSION+'/markets/%i/orders/?datasource=tranquility&order_type=buy&page=%i&type_id=%i'%(rID,pageNum,itemID))
    a=ESI.getresponse().read()
    return a
###

###
@_market.route('/sells/<string:regionName>/<int:itemID>/<int:pageNum>', methods=['GET'])
def getMarketBuysByRegionNameItemName(regionName,itemName,pageNum):
    regionID=getRegionIDByRegionName(regionName).get_json()[0][0]
    itemID=getItemIDByItemName(itemName).get_json()[0][0]
    ESI.request('GET',ESI_VERSION+'/markets/%i/orders/?datasource=tranquility&order_type=sell&page=%i&type_id=%i'%(regionID,pageNum,itemID))
    a=ESI.getresponse().read()
    return a
###

###
@_market.route('/sells/<int:regionID>/<int:itemID>/<int:pageNum>', methods=['GET'])
def getMarketSellsByRegionIDItemID(regionID,itemID,pageNum):
    ESI.request('GET',ESI_VERSION+'/markets/%i/orders/?datasource=tranquility&order_type=sell&page=%i&type_id=%i'%(regionID,pageNum,itemID))
    a=ESI.getresponse().read()
    return a
###

###
@_market.route('/sells/<string:regionName>/<int:itemID>/<int:pageNum>', methods=['GET'])
def getMarketSellsByRegionNameItemID(regionName,itemID,pageNum):
    regionID=getRegionIDByRegionName(regionName).get_json()[0][0]
    ESI.request('GET',ESI_VERSION+'/markets/%i/orders/?datasource=tranquility&order_type=sell&page=%i&type_id=%i'%(regionID,pageNum,itemID))
    a=ESI.getresponse().read()
    return a
###

###
@_market.route('/sells/<string:regionName>/<int:itemID>/<int:pageNum>', methods=['GET'])
def getMarketSellsByRegionIDItemName(regionID,itemName,pageNum):
    itemID=getItemIDByItemName(itemName)
    ESI.request('GET',ESI_VERSION+'/markets/%i/orders/?datasource=tranquility&order_type=sell&page=%i&type_id=%i'%(rID,pageNum,itemID))
    a=ESI.getresponse().read()
    return a
###

###
@_market.route('/sells/<string:regionName>/<int:itemID>/<int:pageNum>', methods=['GET'])
def getMarketSellsByRegionNameItemName(regionName,itemName,pageNum):
    regionID=getRegionIDByRegionName(regionName).get_json()[0][0]
    itemID=getItemIDByItemName(itemName).get_json()[0][0]
    ESI.request('GET',ESI_VERSION+'/markets/%i/orders/?datasource=tranquility&order_type=sell&page=%i&type_id=%i'%(regionID,pageNum,itemID))
    a=ESI.getresponse().read()
    return a
###

if __name__ == '__main__':
    app.run(debug=False)

