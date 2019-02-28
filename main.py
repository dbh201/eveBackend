from flask import Flask,abort,jsonify
import mysql.connector
import http.client
import blueprints
import atexit

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
with app.app_context():
    import analyser_thread as athread
    athread.analyser = athread.Analyser()
    athread.analyser.start()
    atexit.register(athread.analyser.terminate())
    print(athread.analyser.regions)
blueprints.register_all(app)


@app.route('/')
def index():
    return 'This is a local REST endpoint for the SDE database.'

if __name__ == '__main__':
    app.run(debug=True)
