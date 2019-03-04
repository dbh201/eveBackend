from flask import Blueprint,jsonify
from flask import current_app as app
from item import getItemIDByItemName
from region import getRegionIDByRegionName
_analysis = Blueprint('_analysis',__name__)
_prefix = '/analysis'

@_analysis.route('/buyorders/<string:regionName>/<string:itemName>/')
def getBuyOrders(regionName,itemName):
    regionID=getRegionIDByRegionName(regionName).get_json()[0][0]
    itemID=getItemIDByItemName(itemName).get_json()[0][0]
    try:
        return jsonify(app.analyser.regions[regionID].rBuys[itemID])
    except KeyError:
        return "[" + str(regionID)+", " + str(itemID) + "] was not found"

@_analysis.route('/status/')
def getStatus():
    ret="""
    Current analyser status: <br/>
    <table style="border: 1px solid black">
    <tr>
    <th style="border: 1px solid black">Region</th>
    <th style="border: 1px solid black">Types</th>
    <th style="border: 1px solid black">Buy sync</th>
    <th style="border: 1px solid black">Sell sync</th>
    </tr>
    """
    for i in app.analyser.regions:
        lentypes = len(app.analyser.regions[i].rTypes)
        if lentypes == 0:
            lentypes = 1
        ret += '<th style="border: 1px solid black">'+app.analyser.regions[i].rName+"</th>"
        ret += '<th style="border: 1px solid black">'+str(len(app.analyser.regions[i].rTypes))+"</th>"
        buypcnt = len(app.analyser.regions[i].rBuys)/lentypes
        sellpcnt = len(app.analyser.regions[i].rSells)/lentypes
        ret += '<th style="border: 1px solid black">'+str(buypcnt)+"</th>"
        ret += '<th style="border: 1px solid black">'+str(sellpcnt)+"</th>"

    ret += "</table>"
    return ret

@_analysis.route('/sellorders/<string:regionName>/<string:itemName>/')
def getSellOrders(regionName,itemName):
    regionID=getRegionIDByRegionName(regionName).get_json()[0][0]
    itemID=getItemIDByItemName(itemName).get_json()[0][0]
    try:
        return jsonify(at.analyser.regions[regionID].rSells[itemID])
    except KeyError:
        return "[" + str(regionID)+", " + str(itemID) + "] was not found"
