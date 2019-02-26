from flask import Flask,abort,jsonify
import mysql.connector
import http.client

# IMPORTANT NOTES:
# in the SDE, items (inventory items) information
# is in the invTypes table.

# objects (items in space, not in inventory) information
# is in the invItems table.
# invNames contains names for objects only

# invTypes contains all (most?) pertinent information on 
# inventory items

# this script will use the convention item (inventory) and object (space)
db = mysql.connector.connect(
    host='localhost',
    user='sdeuser',
    passwd='password123',
    database='sde'
    )

ESI_URL = "esi.evetech.net"
ESI="/latest"
esi = http.client.HTTPSConnection(ESI_URL)

c = db.cursor()
app = Flask(__name__)

@app.route('/')
def index():
    return 'This is a local REST endpoint for the SDE database.'

def dbQuery(query,params):
    try:
        c.execute(query,params)
        a = c.fetchone() 
    
        return jsonify(a) if a else jsonify([])
    except Exception as e:
        print("Error lols: %s" % (str(e)))
        return str(e)

# API layout:
# /api/(subject of request)/(data requested)/by(information provided)/



#############
# /api/item #
#############

###
q_getItemNameByItemID='''
SELECT typeName 
FROM invTypes 
WHERE typeID = %s ;
'''
@app.route('/api/item/name/byid/<int:itemID>', methods=['GET'])
def getItemNameByItemID(itemID):
    return dbQuery( q_getItemNameByItemID,(str(itemID),) )
###

###
q_getItemIDByItemName='''
SELECT typeID 
FROM invTypes 
WHERE typeName LIKE %s ;
'''
@app.route('/api/item/id/byname/<string:itemName>', methods=['GET'])
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
@app.route('/api/item/ids/bymarketgroupid/<int:marketGroupID>', methods=['GET'])
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
@app.route('/api/item/ids/bymarketgroupname/<string:marketGroupName>', methods=['GET'])
def getItemIDsByMarketGroupName(marketGroupName):
    return dbQuery( q_getItemIDsByMarketGroupName, (marketGroupName,) ) 
###

###
q_getItemNamesByMarketGroupID='''
SELECT it.typeName
FROM invTypes AS it
WHERE it.marketGroupID = %s ;
'''
@app.route('/api/item/names/bymarketgroupid/<int:marketGroupID>', methods=['GET'])
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
@app.route('/api/item/names/bymarketgroupname/<string:marketGroupName>', methods=['GET'])
def getItemNamesByMarketGroupName(marketGroupName):
    return dbQuery( q_getItemNamesByMarketGroupName, (marketGroupName,) )
###

###
q_getItemsByMarketGroupID='''
SELECT it.typeID,it.typeName
FROM invTypes AS it
WHERE it.marketGroupID = %s ;
'''
@app.route('/api/items/bymarketgroupid/<int:marketGroupID>', methods=['GET'])
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
@app.route('/api/items/bymarketgroupname/<string:marketGroupName>', methods=['GET'])
def getItemsByMarketGroupName(marketGroupName)
    return dbQuery( q_getItemsByMarketGroupName, (str(marketGroupID),) ) 
#############


####################
# /api/marketgroup #
####################

###
q_getMarketGroupIDByMarketGroupName='''
SELECT marketGroupID
FROM invMarketGroups
WHERE marketGroupName LIKE %s ;
'''
@app.route('/api/marketgroup/id/byname/<string:marketGroupName>', methods=['GET'])
def getMarketGroupIDByMarketGroupName(marketGroupName):
    return dbQuery( q_getMarketGroupIDByMarketGroupName, (marketGroupName,) )
###

###
q_getMarketGroupIDByItemID='''
SELECT marketGroupID 
FROM invTypes 
WHERE typeID = %s ;
'''
@app.route('/api/marketgroup/id/byitemid/<int:itemID>', methods=['GET'])
def getMarketGroupIDByItemID(itemID):
    return dbQuery( q_getMarketGroupIDByItemID, (str(itemID),) )
###

###
q_getMarketGroupIDByItemName='''
SELECT marketGroupID 
FROM invTypes 
WHERE typeName LIKE %s ;
'''
@app.route('/api/marketgroup/id/byitemname/<string:itemName>', methods=['GET'])
def getMarketGroupIDByItemName(itemName):
    return dbQuery( q_getMarketGroupIDByItemName, (itemName,) )
###

###
q_getMarketGroupNameByMarketGroupID='''
SELECT marketGroupName
FROM invMarketGroups
WHERE marketGroupID = %s ;
'''
@app.route('/api/marketgroup/name/byid/<int:marketGroupID>', methods=['GET'])
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
@app.route('/api/marketgroup/name/byitemname/<string:itemName>', methods=['GET'])
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
@app.route('/api/marketgroup/name/byitemname/<string:itemName>', methods=['GET'])
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
@app.route('/api/marketgroup/byitemid/<int:itemID>', methods=['GET'])
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
@app.route('/api/marketgroup/byitemname/<string:itemName>', methods=['GET'])
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
@app.route('/api/marketgroup/heirarchy/byitemid/<int:itemID>', methods=['GET'])
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
@app.route('/api/marketgroup/heirarchy/byitemname/<string:itemName>', methods=['GET'])
def getMarketGroupHeirarchyByItemName(itemName)
    return dbQuery( q_getMarketGroupIDHeirarchyByItemName, (itemName,) )
###

###
q_getMarketGroupHeirarchyByMarketGroupID='''
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
@app.route('/api/marketgroup/heirarchy/bymarketgroupid/<int:marketGroupID>')
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
@app.route('/api/marketgroup/heirarchy/bymarketgroupname/<string:marketGroupName>')
def getMarketGroupHeirarchyByMarketGroupName(marketGroupName):
    return dbQuery( q_getMarketGroupHeirarchyByMarketGroupName, (marketGroupName,) )
####################


###############
# /api/region #
###############

###
q_getRegionIDByRegionName='''
SELECT regionName
FROM mapRegions
WHERE regionID = %s ;
'''
@app.route('/api/region/name/byregionid/<int:regionID>', methods=['GET'])
def getRegionIDByRegionName(regionName):
    return dbQuery( q_getRegionIDByRegionName,(str(regionName,)) )
###

###
q_getAdjacentRegionIDsByRegionID='''
SELECT t.regionID,t.regionName 
FROM mapRegions AS t
JOIN mapRegionJumps AS j 
ON j.toRegionID = t.regionID
JOIN mapRegions AS f 
ON j.fromRegionID = f.regionID
WHERE f.regionID = %s ;
'''
@app.route('/api/region/adjacentregions/<int:regionID>', methods=['GET'])
def getAdjacentRegionIDsByRegionID):
    return dbQuery( q_getAdjacentRegionIDsByRegionID,str(regionID),) )
###

###

@app.route('/api/market/<int:regionID>/<int:itemID>', methods=['GET'])
def getItemPrices(regionID,itemID):
    esi.request('GET',ESI+'/markets/%i/orders/?datasource=tranquility&order_type=all&page=1&type_id=%i'%(regionID,itemID))
    a=esi.getresponse().read()
    return a
################

if __name__ == '__main__':
    app.run(debug=False)

