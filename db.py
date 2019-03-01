from json import dumps
import mysql.connector

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


c = db.cursor()
def dbQuery(query,params):
    try:
        c.execute(query,params)
        a = c.fetchall() 
    
        return a if a else []
    except Exception as e:
        print("dbQuery: %s" % (str(e)))
        return str(e)

