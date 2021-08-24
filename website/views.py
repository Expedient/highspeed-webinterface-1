from flask import Blueprint, render_template
import json

views = Blueprint("views", __name__)

@views.route("/")
@views.route("/home")
def home():
    highspeed = openjson('website/static/highspeed.json')
    
    if highspeed == 1:
        return render_template("base.html", data = 1)       
    else:
        return render_template("base.html", data = highspeed)
    
    
def openjson(filename):
    try:
        # Opening JSON file
        f = open(filename)
    except:
        print("Cant find highspeed.json")
    else:
        try:    
            # returns JSON object as a dictionary
            data = json.load(f)
            return data
        except:
            print("Cant load JSON file")
            # return 1 on error
            return 1
        finally:        
            #close file
            f.close()
        
   