from flask import Blueprint
from db import dbQuery

#############
# /api/item #
#############

_item = Blueprint('_item',__name__)
_prefix = '/api/item'

###
q_getItemNameByItemID='''
SELECT typeName 
FROM invTypes 
WHERE typeID = %s ;
'''
@_item.route('/name/byid/<int:itemID>', methods=['GET'])
def getItemNameByItemID(itemID):
    return dbQuery( q_getItemNameByItemID,(str(itemID),) )
###

###
q_getItemIDByItemName='''
SELECT typeID 
FROM invTypes 
WHERE typeName LIKE %s ;
'''
@_item.route('/id/byname/<string:itemName>', methods=['GET'])
def getItemIDByItemName(itemName):
    return dbQuery( q_getItemIDByItemName, (itemName,) )
###

###
q_getItemIDsByMarketGroupID='''
SELECT it.typeID
FROM invTypes AS it
JOIN invMarketGroups AS img
ON img.marketGroupID = it.marketGroupID
WHERE img.marketGroupID = %s ;
'''
@_item.route('/ids/bymarketgroupid/<int:marketGroupID>', methods=['GET'])
def getItemIDsByMarketGroupID(marketGroupID):
    return dbQuery( q_getItemIDsByMarketGroupID, (str(marketGroupID),) )
###

###
q_getItemIDsByMarketGroupName='''
SELECT it.typeID
FROM invTypes AS it
JOIN invMarketGroups AS img
ON img.marketGroupID = it.marketGroupID
WHERE img.marketGroupName LIKE %s ;
'''
@_item.route('/ids/bymarketgroupname/<string:marketGroupName>', methods=['GET'])
def getItemIDsByMarketGroupName(marketGroupName):
    return dbQuery( q_getItemIDsByMarketGroupName, (marketGroupName,) ) 
###

###
q_getItemNamesByMarketGroupID='''
SELECT it.typeName
FROM invTypes AS it
WHERE it.marketGroupID = %s ;
'''
@_item.route('/names/bymarketgroupid/<int:marketGroupID>', methods=['GET'])
def getItemNamesByMarketGroupID(marketGroupID):
    return dbQuery( q_getItemNamesByMarketGroupID, (str(marketGroupID),) )
###

###
q_getItemNamesByMarketGroupName='''
SELECT it.typeName
FROM invTypes AS it
JOIN invMarketGroups AS img
ON it.marketGroupID = img.marketGroupID
WHERE img.marketGroupName LIKE %s ;
'''
@_item.route('/names/bymarketgroupname/<string:marketGroupName>', methods=['GET'])
def getItemNamesByMarketGroupName(marketGroupName):
    return dbQuery( q_getItemNamesByMarketGroupName, (marketGroupName,) )
###

###
q_getItemsByMarketGroupID='''
SELECT it.typeID,it.typeName
FROM invTypes AS it
WHERE it.marketGroupID = %s ;
'''
@_item.route('/list/bymarketgroupid/<int:marketGroupID>', methods=['GET'])
def getItemsByMarketGroupID(marketGroupID):
    return dbQuery( q_getItemsByMarketGroupID, (str(marketGroupID),) ) 
###

###
q_getItemsByMarketGroupName='''
SELECT it.typeID,it.typeName
FROM invTypes AS it
JOIN invMarketGroups AS img
ON img.marketGroupID = it.marketGroupID
WHERE img.marketGroupName LIKE %s ;
'''
@_item.route('/list/bymarketgroupname/<string:marketGroupName>', methods=['GET'])
def getItemsByMarketGroupName(marketGroupName):
    return dbQuery( q_getItemsByMarketGroupName, (str(marketGroupID),) ) 
#############
