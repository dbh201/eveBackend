from importlib import reload
from flask import Flask,abort,jsonify,request
from flask_cors import CORS
import blueprints
import atexit
import esi
import analyser_thread

# IMPORTANT NOTES:
# in the SDE, items (inventory items) information
# is in the invTypes table.

# objects (items in space, not in inventory) information
# is in the invItems table.
# invNames contains names for objects only

# invTypes contains all (most?) pertinent information on 
# inventory items

# this script will use the convention item (inventory) and object (space)

def create_app():
    app = Flask(__name__)
    blueprints.register_all(app)

    def stop_all():
        print("Stopping all threads...")
        if(app.analyser):
            if(app.analyser.is_alive()):    
                app.analyser.terminate()
                app.analyser.join(10)
            if(app.analyser.is_alive()):
                print("analyser timed out. :(")

        if(app.ESI.is_alive()):
            app.ESI.terminate()
            app.ESI.join(10)
        if(app.ESI.is_alive()):
            print("ESI timed out. :(")


    def start_all():
        app.ESI = esi.ESIConnection()
        app.ESI.start()
        app.analyser = None
        #app.analyser = analyser_thread.Analyser(app.ESI)
        #app.analyser.start()

    start_all()
    atexit.register(stop_all)
    return app

app = create_app()
CORS(app,origins="http://localhost:4200")
@app.route('/')
def index():
    return "API Status:<br/>ESI Thread: %s, <br/>Analyser Thread: %s, %s" % (
    "Started" if app.ESI.is_alive() else "Stopped",
    "Started" if app.analyser.is_alive() else "Stopped",
    app.analyser.status() )

@app.route('/suspend')
def suspend():
    app.analyser.pause()
    return "Suspended analyser."
@app.route('/resume')
def resume():
    app.analyser.resume()
    return "Resumed analyser."
if __name__ == '__main__':
    app.run(debug=False,threaded=False)
