from flask import Blueprint, render_template
import json

views = Blueprint("views", __name__)

@views.route("/")
@views.route("/home")
def home():
    highspeed = openjson('website/static/highspeed.json')
    
    return render_template("base.html", data = highspeed)
    
def openjson(filename):
    try:
        # Opening JSON file
        f = open(filename)
    except:
        print("Cant find highspeed.json")

    try:    
        # returns JSON object as a dictionary
        data = json.load(f)
    except:
        print("Cant load JSON file")
        
    #close file
    f.close()
    
    return data