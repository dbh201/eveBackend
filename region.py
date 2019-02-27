from flask import Blueprint
from db import dbQuery

###############
# /api/region #
###############

_region = Blueprint('_region',__name__)
_prefix = '/api/region'

###
q_getRegionIDByRegionName='''
SELECT regionID
FROM mapRegions
WHERE regionName LIKE %s ;
'''
@_region.route('/id/byname/<string:regionName>', methods=['GET'])
def getRegionIDByRegionName(regionName):
    return dbQuery( q_getRegionIDByRegionName, (regionName,) )
###

###
q_getRegionNameByRegionID='''
SELECT regionName
FROM mapRegions
WHERE regionID = %s ;
'''
@_region.route('/name/byid/<int:regionID>', methods=['GET'])
def getRegionNameByRegionID(regionID):
    return dbQuery( q_getRegionNameByRegionID, (str(regionID),) )
###

###
q_getAdjacentRegionNamesByRegionName='''
SELECT t.regionName
FROM mapRegions f
JOIN mapRegionJumps j
ON f.regionID = j.fromRegionID
JOIN mapRegions t
ON t.regionID = j.toRegionID
WHERE f.regionName LIKE %s ;
'''
@_region.route('/adjacentnames/byname/<string:regionName>', methods=['GET'])
def getAdjacentRegionNamesByRegionName(regionName):
    return dbQuery( q_getAdjacentRegionNamesByRegionName, (regionName,) )
###

###
q_getAdjacentRegionNamesByRegionID='''
SELECT t.regionName
FROM mapRegions AS f
JOIN mapRegionJumps AS adj
ON f.regionID = adj.fromRegionID 
JOIN mapRegions AS t
ON t.regionID = adj.toRegionID
WHERE f.regionID = %s ;
'''
@_region.route('/adjacentnames/byid/<int:regionID>',  methods=['GET'])
def getAdjacentRegionNamesByRegionID(regionID):
    return dbQuery( q_getAdjacentRegionNamesByRegionID, (str(regionID),) )
###

###
q_getAdjacentRegionIDsByRegionName='''
SELECT adj.toRegionID
FROM mapRegionJumps AS adj
JOIN mapRegion f
ON f.regionID = adj.toRegionID
WHERE f.regionName LIKE %s ;
'''
def getAdjacentRegionIDsByRegionName(regionName):
    return dbQuery( q_getAdjacentRegionIDsByRegionName, (regionName,) )


q_getAdjacentRegionIDsByRegionID='''
SELECT adj.toRegionID
FROM mapRegionJumps AS adj
WHERE adj.fromRegionID = %s ;
'''
def getAdjacentRegionIDsByRegionID(regionID):
    return dbQuery( q_getAdjacentRegionIDsByRegionID, (str(regionID),) )

q_getAdjacentRegionsByRegionName='''
SELECT t.regionID,t.regionName
FROM mapRegions AS t
JOIN mapRegionJumps AS adj
ON t.regionID = adj.toRegionID
JOIN mapRegions AS f
ON f.regionID = adj.fromRegionID
WHERE f.regionName LIKE %s ;
'''
def getAdjacentRegionsByRegionName(regionName):
    return dbQuery( q_getAdjacentRegionsByRegionName, (regionName,) )

q_getAdjacentRegionsByRegionID='''
'''
def getAdjacentRegionsByRegionID(regionID):
    return dbQuery( q_getAdjacentRegionsByRegionID, (str(regionID),) )
