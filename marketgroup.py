from flask import Blueprint
from db import dbQuery

####################
# /api/marketgroup #
####################

_marketGroup= Blueprint('_marketGroup', __name__)
_prefix='/api/marketgroup'

###
q_getMarketGroupIDByMarketGroupName='''
SELECT marketGroupID
FROM invMarketGroups
WHERE marketGroupName LIKE %s ;
'''
@_marketGroup.route('/id/byname/<string:marketGroupName>', methods=['GET'])
def getMarketGroupIDByMarketGroupName(marketGroupName):
    return dbQuery( q_getMarketGroupIDByMarketGroupName, (marketGroupName,) )
###

###
q_getMarketGroupIDByItemID='''
SELECT marketGroupID 
FROM invTypes 
WHERE typeID = %s ;
'''
@_marketGroup.route('/id/byitemid/<int:itemID>', methods=['GET'])
def getMarketGroupIDByItemID(itemID):
    return dbQuery( q_getMarketGroupIDByItemID, (str(itemID),) )
###

###
q_getMarketGroupIDByItemName='''
SELECT marketGroupID 
FROM invTypes 
WHERE typeName LIKE %s ;
'''
@_marketGroup.route('/id/byitemname/<string:itemName>', methods=['GET'])
def getMarketGroupIDByItemName(itemName):
    return dbQuery( q_getMarketGroupIDByItemName, (itemName,) )
###

###
q_getMarketGroupNameByMarketGroupID='''
SELECT marketGroupName
FROM invMarketGroups
WHERE marketGroupID = %s ;
'''
@_marketGroup.route('/name/byid/<int:marketGroupID>', methods=['GET'])
def getMarketGroupNameByMarketGroupID(marketGroupID):
    return dbQuery( q_getMarketGroupNameByMarketGroupID, (str(marketGroupID),) )
###

###
q_getMarketGroupNameByItemID='''
SELECT marketGroupName 
FROM invMarketGroups AS img 
JOIN invTypes AS it 
ON it.marketGroupID = img.marketGroupID
WHERE it.typeID = %s ;
'''
@_marketGroup.route('/name/byitemname/<string:itemName>', methods=['GET'])
def getMarketGroupNameByItemID(itemName):
    return dbQuery( q_getMarketGroupNameByItemName, (itemName,) )
###

###
q_getMarketGroupNameByItemName='''
SELECT marketGroupName
FROM invMarketGroups AS img
JOIN invTypes AS it
ON it.marketGroupID = img.marketGroupID
WHERE it.typeName LIKE %s ;
'''
@_marketGroup.route('/name/byitemname/<string:itemName>', methods=['GET'])
def getMarketGroupNameByItemName(itemName):
    return dbQuery( q_getMarketGroupNameByItemName, (itemName,) )
###

###
q_getMarketGroupByItemID='''
SELECT img.marketGroupID,img.marketGroupName
FROM invMarketGroups AS img
JOIN invTypes AS it
ON it.marketGroupID = img.marketGroupID
WHERE it.typeID = %s;
'''
@_marketGroup.route('/byitemid/<int:itemID>', methods=['GET'])
def getMarketGroupByItemID(itemID):
    return dbQuery( q_getMarketGroupByItemID, (str(itemID),) )
###

###
q_getMarketGroupByItemName='''
SELECT img.marketGroupID,img.marketGroupName
FROM invMarketGroups AS img
join invTypes AS it
on it.marketGroupID = img.marketGroupID
WHERE it.typeName LIKE %s ;
'''
@_marketGroup.route('/byitemname/<string:itemName>', methods=['GET'])
def getMarketGroupByItemName(itemName):
    return dbQuery( q_getMarketGroupByItemName, (itemName,) )
###

###
q_getMarketGroupHeirarchyByItemID='''
WITH RECURSIVE cte AS ( 
 SELECT i.marketGroupID,i.marketGroupName,i.parentGroupID,it.typeID, 1 lvl 
 FROM invMarketGroups i 
 JOIN invTypes AS it 
 ON i.marketGroupID = it.marketGroupID 
 WHERE it.typeID = %s
 UNION ALL 
 SELECT p.marketGroupID,p.marketGroupName p.parentGroupID,i.typeID, lvl+1 
 FROM invMarketGroups p 
 LEFT JOIN invTypes i 
 ON p.marketGroupID = i.marketGroupID 
 INNER JOIN cte c 
 ON c.parentGroupID = p.marketGroupID 
 ) 
SELECT marketGroupID,marketGroupName,parentGroupID,lvl FROM cte ORDER BY lvl; 
'''
@_marketGroup.route('/heirarchy/byitemid/<int:itemID>', methods=['GET'])
def getMarketGroupHeirarchyByItemID(itemID):
    return dbQuery( q_getMarketGroupHeirarchyByItemID, (str(itemID),) )
###

###
q_getMarketGroupHeirarchyByItemName='''
WITH RECURSIVE cte AS ( 
 SELECT i.marketGroupID,i.parentGroupID,it.typeID, 1 lvl 
 FROM invMarketGroups i 
 JOIN invTypes AS it 
 ON i.marketGroupID = it.marketGroupID 
 WHERE it.typeName LIKE %s
 UNION ALL 
 SELECT p.marketGroupID, p.parentGroupID,i.typeID, lvl+1 
 FROM invMarketGroups p 
 LEFT JOIN invTypes i 
 ON p.marketGroupID = i.marketGroupID 
 INNER JOIN cte c 
 ON c.parentGroupID = p.marketGroupID 
 ) 
SELECT marketGroupID,marketGroupName,parentGroupID,lvl FROM cte ORDER BY lvl; 
'''
@_marketGroup.route('/heirarchy/byitemname/<string:itemName>', methods=['GET'])
def getMarketGroupHeirarchyByItemName(itemName):
    return dbQuery( q_getMarketGroupIDHeirarchyByItemName, (itemName,) )
###

###
q_getMarketGroupHeirarchyByMarketGroupID='''
WITH RECURSIVE cte AS ( 
 SELECT i.marketGroupID,i.marketGroupName,i.parentGroupID, 1 lvl 
 FROM invMarketGroups i 
 WHERE i.marketGroupID LIKE %s
 UNION ALL 
 SELECT p.marketGroupID,p.marketGroupName,p.parentGroupID, lvl+1 
 FROM invMarketGroups p 
 INNER JOIN cte c 
 ON c.parentGroupID = p.marketGroupID 
 ) 
SELECT marketGroupID,marketGroupName,parentGroupID,lvl FROM cte ORDER BY lvl; 
'''
@_marketGroup.route('/heirarchy/bymarketgroupid/<int:marketGroupID>')
def getMarketGroupHeirarchyByMarketGroupID(marketGroupID):
    return dbQuery( q_getMarketGroupHeirarchyByMarketGroupID, (str(marketGroupID),) )
###

###
q_getMarketGroupHeirarchyByMarketGroupName='''
WITH RECURSIVE cte AS ( 
 SELECT i.marketGroupID,i.marketGroupName,i.parentGroupID,it.typeID, 1 lvl 
 FROM invMarketGroups i 
 JOIN invTypes AS it 
 ON i.marketGroupID = it.marketGroupID 
 WHERE it.typeName LIKE %s
 UNION ALL 
 SELECT p.marketGroupID,p.marketGroupName,p.parentGroupID,i.typeID, lvl+1 
 FROM invMarketGroups p 
 LEFT JOIN invTypes i 
 ON p.marketGroupID = i.marketGroupID 
 INNER JOIN cte c 
 ON c.parentGroupID = p.marketGroupID 
 ) 
SELECT marketGroupID,marketGroupName,parentGroupID,lvl FROM cte ORDER BY lvl; 
'''
@_marketGroup.route('/heirarchy/bymarketgroupname/<string:marketGroupName>')
def getMarketGroupHeirarchyByMarketGroupName(marketGroupName):
    return dbQuery( q_getMarketGroupHeirarchyByMarketGroupName, (marketGroupName,) )
####################

