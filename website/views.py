#!/usr/bin/python

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
    

@views.route("/del_int/<string:devicename>/<path:interfacename>")
def del_int(devicename, interfacename):
    highspeed = openjson('website/static/highspeed.json')

    try:
        if highspeed == 1:
            return render_template("base.html", data = 1)       
        
        if devicename in highspeed["devices"][0]:
            if interfacename in highspeed['devices'][0][devicename]:
                highspeed['devices'][0][devicename].remove(interfacename)
            else:
                return render_template("base.html", data = 1)   

            return render_template("base.html", data = highspeed, dev = devicename, interface = interfacename)
        else:
            #failed to find key or value
            return render_template("base.html", data = highspeed, dev = devicename, interface = interfacename)
    except:
        return render_template("base.html", data = 1)
    

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
        
   