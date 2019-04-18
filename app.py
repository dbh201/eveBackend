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

class FlaskMT(Flask):
    def __init__(self):
        Flask.__init__(self,__name__)
        blueprints.register_all(self)
        self.start_all()
        atexit.register(self.stop_all)

    def stop_all(self):
        print("Stopping all threads...")
        if(self.analyser):
            if(self.analyser.is_alive()):    
                self.analyser.terminate()
                self.analyser.join(10)
            if(self.analyser.is_alive()):
                print("analyser timed out. :(")

        if(self.ESI.is_alive()):
            self.ESI.terminate()
            self.ESI.join(10)
        if(self.ESI.is_alive()):
            print("ESI timed out. :(")


    def start_all(self):
        self.ESI = esi.ESIConnection()
        self.ESI.start()
        self.analyser = None
        #self.analyser = analyser_thread.Analyser(self.ESI)
        #self.analyser.start()


# initialize app
app = FlaskMT()
CORS(app,origins="http://localhost:4200")

# app default routes
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

# MAIN THREAD
if __name__ == '__main__':
    try:
        app.run(debug=False,threaded=False)
    except KeyboardInterrupt:
        app.stop_all()
