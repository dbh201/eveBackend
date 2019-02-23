from flask import Flask,abort,jsonify
import mysql.connector
import http.client

import marketgroup as mg
import item as it

# IMPORTANT NOTES:
# in the SDE, items (inventory items) information
# is in the invTypes table.

# objects (items in space, not in inventory) information
# is in the invItems table.
# invNames contains names for objects only

# invTypes contains all (most?) pertinent information on 
# inventory items

# this script will use the convention item (inventory) and object (space)

app = Flask(__name__)

app.register_blueprint(mg._marketGroup,url_prefix=mg._prefix)
app.register_blueprint(it._item,url_prefix=it._prefix)

@app.route('/')
def index():
    return 'This is a local REST endpoint for the SDE database.'
app

if __name__ == '__main__':
    app.run(debug=False)
