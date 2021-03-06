from flask import Blueprint
from db import dbQuery

#####################
# /api/solarsystem/ #
#####################

_solarsystem = Blueprint('_solarSystem',__name__)
_prefix = '/solarsystem'

###
q_getSolarSystemIDBySolarSystemName='''
SELECT solarSystemID
FROM mapSolarSystems
WHERE solarSystemName LIKE %s ;
'''
@_solarsystem.route('/id/byname/<string:solarSystemName>', methods=['GET'])
def getSolarSystemIDBySolarSystemName(solarSystemName):
    return dbQuery( q_getSystemIDBySystemName, (solarSystemName,) )
###

###
q_getSolarSystemNameBySolarSystemID='''
SELECT solarSystemName
FROM mapSolarSystems
WHERE solarSystemID = %s ;
'''
@_solarsystem.route('/name/byid/<int:solarSystemID>', methods=['GET'])
def getSolarSystemNameBySolarSystemID(solarSystemID):
    return dbQuery( q_getSystemNameBySystemID, (str(solarSystemID),) )
###

###
q_getSolarSystemIDsByRegionID='''
SELECT solarSystemID
FROM mapSolarSystems
WHERE regionID = %s ;
'''
@_solarsystem.route('/ids/byregionid/<int:regionID>', methods=['GET'])
def getSolarSystemIDsByRegionID(regionID):
    return dbQuery( q_getSolarSystemIDsByRegionID, (str(regionID),) )
###

###
q_getSolarSystemIDsByRegionName='''
SELECT solarSystemID
FROM mapSolarSystems AS mss
JOIN mapRegions AS mr
ON mss.regionID = mr.regionID
WHERE mr.regionName LIKE %s ;
'''
@_solarsystem.route('/ids/byregionname/<string:regionName>', methods=['GET'])
def getSolarSystemIDsByRegionName():
    return dbQuery( q_getSolarSystemIDsByRegionName, (str(regionName),) )
###

q_getSolarSystemNamesByRegionID='''
SELECT solarSystemName
FROM mapSolarSystems
WHERE regionID = %s ;
'''
@_solarsystem.route('/names/byregionid/<int:regionID>', methods=['GET'])
def getSolarSystemNamesByRegionID(regionID):
    return dbQuery( q_getSolarSystemNamesByRegionID, (str(),) )
###

q_getSolarSystemNamesByRegionName='''
SELECT solarSystemName
FROM mapSolarSystems AS mss
JOIN mapRegions AS mr
ON mss.regionID = mr.regionID
WHERE mr.regionName LIKE %s ;
'''
@_solarsystem.route('/names/byregionname/<string:regionName>', methods=['GET'])
def getSolarSystemNamesByRegionName(regionName):
    return dbQuery( q_getSolarSystemNamesByRegionName, (str(regionName),) )
###

q_getSolarSystemsByRegionID='''
SELECT solarSystemName,solarSystemID
FROM mapSolarSystems AS mss
WHERE regionID = %s ;
'''
@_solarsystem.route('/byregionid/<int:regionID>', methods=['GET'])
def getSolarSystemsByRegionID(regionID):
    return dbQuery( q_getSolarSystemsByRegionID, (str(regionID),) )
###

q_getSolarSystemsByRegionName='''
SELECT solarSystemName,solarSystemID
FROM mapSolarSystems AS mss
JOIN mapRegions AS mr
ON mss.regionID = mr.regionID
WHERE mr.regionName LIKE %s ;
'''
@_solarsystem.route('/byregionname/<string:regionName>', methods=['GET'])
def getSolarSystemsByRegionName(regionName):
    return dbQuery( q_getSolarSystemsByRegionName, (str(regionName),) )
###


