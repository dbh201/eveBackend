from flask import Blueprint,jsonify
from db import dbQuery
from item import getItemIDByItemName
from region import getRegionIDByRegionName
import analyser_thread  as at
_analysis = Blueprint('_analysis',__name__)
_prefix = '/analysis'

@_analysis.route('/buyorders/<string:regionName>/<string:itemName>/')
def getBuyOrders(regionName,itemName):
    regionID=getRegionIDByRegionName(regionName).get_json()[0][0]
    itemID=getItemIDByItemName(itemName).get_json()[0][0]
    try:
        return jsonify(at.analyser.regions[regionID].rBuys[itemID])
    except KeyError:
        return "[" + str(regionID)+", " + str(itemID) + "] was not found"
