from flask import Flask,abort,jsonify
import mysql.connector
import http.client

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

    
@app.route('/api/item/toitemname/<int:itemID>', methods=['GET'])
def getItemName(itemID):
    return dbQuery('SELECT itemName FROM invNames WHERE itemID = %s ;',(str(itemID),))


@app.route('/api/item/toitemid/<string:itemName>', methods=['GET'])
def getItemID(itemName):
    return dbQuery('SELECT itemID FROM invNames WHERE itemName LIKE %s ;',(itemName,))
        

@app.route('/api/region/toregionid/<string:regionName>', methods=['GET'])
def getRegionID(regionName):
    return dbQuery('SELECT regionID FROM mapRegions WHERE regionName LIKE %s ;',(regionName,))

@app.route('/api/region/adjacentregions/<int:regionID>', methods=['GET'])
def getAdjacentRegions(regionID):
    return dbQuery('''
            SELECT t.regionID,t.regionName FROM mapRegions AS t
            JOIN mapRegionJumps AS j ON j.toRegionID = t.regionID
            JOIN mapRegions AS f ON j.fromRegionID = f.regionID
            WHERE f.regionID = %s ;
            ''',
            (str(regionID),)
            )

@app.route('/api/market/<int:regionID>/<int:itemID>', methods=['GET'])
def getItemPrices(regionID,itemID):
    
    esi.request('GET',ESI+'/markets/%i/orders/?datasource=tranquility&order_type=all&page=1&type_id=%i'%(regionID,itemID))
    a=esi.getresponse().read()
    return a

if __name__ == '__main__':
    app.run(debug=False)
