from flask import Flask, render_template, request, session, redirect, url_for

import logging
import sys
import subprocess
import socket
import json
import requests

app = Flask(__name__)

logging.basicConfig(level=logging.DEBUG)  # Set the log level to DEBUG




#--------------------------------------------API Methods------------------------------------

cacheA={}
cacheW={}


def getIP(incoming):
    urlRequest = incoming.strip()  # Remove leading/trailing whitespace
    try:
        ipAddress = socket.gethostbyname(urlRequest)
    except socket.gaierror as e:
        print(f"Error resolving hostname: {e}")
        ipAddress = None  # Return None if hostname resolution fails
    return ipAddress


#getAddress helper method
def getAddress(incoming):
    #print(incoming)
    ipAddress= getIP(incoming)
    #print(ipAddress)
 

    #print(urlRequest)
    command="whois "
    whowho=subprocess.getstatusoutput(command+ipAddress)
    #print(whowho)
    for x in whowho[1].split("\n"):
        if x.startswith("Address"):
            street=x[8:].strip()
        if x.startswith("City"):
            city=x[5:].strip()
        if x.startswith("State"):
            state=x[10:].strip()
        if x.startswith("Postal"):
            zipC=x[11:].strip()
  
    address=[street, city, state, zipC];



    return (address)
def getWeather(incoming):


    ipAddress= getIP(incoming)
   
    addy = getAddress(ipAddress)

    geocodingApi="https://geocoding.geo.census.gov/geocoder/locations/address?street="+addy[0]+"&city="+addy[1]+"&state="+addy[2]+"&zip="+addy[3]+"&benchmark=Public_AR_Current&format=json"
    georesponse=requests.get(geocodingApi)
    js = json.loads(georesponse.text)
  
    outputx=js['result']['addressMatches'][0]['coordinates']['x']
    outputy=js['result']['addressMatches'][0]['coordinates']['y']
    lat=format(outputy)
    lon=format(outputx)
   
    
    # base API string for weather.gov
    weather_s = "https://api.weather.gov/points/"

    # use the commandline input and the weather_s to make API call
    response = requests.get(weather_s+lat+","+lon)

    # convert it to json
    js = json.loads(response.text)

    # find the forecast URL based on the API page
    forecast_URL = js['properties']['forecast']

    # call the API again to get theforecast
    final_response = requests.get(forecast_URL)

    #parse json
    js = json.loads(final_response.text)

    #print the forecast
    weather=(js['properties']['periods'][0]['detailedForecast'])

    return(weather)

def checkCache(cache, key):
    #check if the key exists in the dictionary and has a value 
    #if key is not in list, call getaddress
    if key in cache:
        print("This is cached information: ")
        return True
    else:
        return False

def addCache(cache, key, value):
    cache[key]=value

@app.route("/upper/<echo_string>")
def upper(echo_string):
    return(echo_string.upper())

@app.route("/callwhois")
def whois():
    s,o = subprocess.getstatusoutput("whois 8.8.8.8")
    return(o)


#---------------------Routes------------------------


@app.route('/')
def index():
    return render_template('/index.html')
    #return ("this is running on port: "+str(port))

@app.route('/login')
def login():
   
        return render_template('login.html')

@app.route('/about')
def about():
    return render_template('about.html')
@app.route('/address')
def address():
    return render_template('address_search.html')

@app.route("/address", methods=['GET', 'POST'])
def hostAddress():
    try:
        if request.method == 'POST':
            # Logic to handle form submission via POST request
            incomingHost = request.form['url']
        else:
            # Logic to handle GET request
            incomingHost = request.args.get('url', '')

        ipAddress = getIP(incomingHost)

        if checkCache(cacheA, incomingHost):
            address = cacheA[incomingHost]
        else:
            addy = getAddress(incomingHost)

            address=(addy[0]+" "+addy[1]+" "+addy[2]+" "+addy[3])
            addCache(cacheA, incomingHost, address)


        return render_template('address_output.html', url=incomingHost, address=address)

    except AttributeError as e:
        app.logger.error(f"AttributeError: {e}")
        return redirect(url_for('page_not_found'))
    except Exception as e:
        app.logger.error(f"Unhandled exception: {e}")
        return redirect(url_for('internal_server_error'))



@app.route('/weather', methods=['GET'])
def weather():
    return render_template('weather_search.html')


@app.route("/weather", methods=['GET', 'POST'])
def hostWeather():
    try:
        if request.method == 'POST':
            # Logic to handle form submission via POST request
            incomingHost = request.form['url']
        else:
            # Logic to handle GET request
            incomingHost = request.args.get('url', '')

        ipAddress = getIP(incomingHost)

        if checkCache(cacheW, incomingHost):
            weather = cacheW[incomingHost]
        else:
            weather = getWeather(ipAddress)
            addCache(cacheW, incomingHost, weather)

        return render_template('weather_output.html', url=incomingHost, weather=weather)

    except AttributeError as e:
        app.logger.error(f"AttributeError: {e}")
        return redirect(url_for('page_not_found'))
    except Exception as e:
        app.logger.error(f"Unhandled exception: {e}")
        return redirect(url_for('internal_server_error'))



'''

@app.route("/weather", methods=['GET', 'POST'])
def hostWeather():
    if request.method == 'POST':
        incomingHost = request.form.get('url', '')
        print("Incoming Host:", incomingHost)  # Debug statement
        if incomingHost:
            ipAddress = getIP(incomingHost)
            print("IP Address:", ipAddress)  # Debug statement

            if ipAddress:
                if checkCache(cacheW, incomingHost):
                    weather = cacheW[incomingHost]
                else:
                    weather = getWeather(incomingHost)
                    addCache(cacheW, incomingHost, weather)

                return render_template('weather_output.html', weather=weather, url=incomingHost)
            else:
                error_message = "Error: Unable to resolve hostname. Please provide a valid URL."
                return render_template('weather_search.html', error=error_message)
        else:
            error_message = "Error: Empty URL provided. Please provide a valid URL."
            return render_template('weather_search.html', error=error_message)
    else:
        return render_template('weather_search.html')

'''

#--------------------Error Handling----------------------------

# Custom 404 error handler
@app.errorhandler(404)
def page_not_found(e):
    return render_template('404_error.html'), 404

# Custom 500 error handler
@app.errorhandler(500)
def internal_server_error(e):
    return render_template('505_error.html'), 500







#---------------------SQL Stuff------------------------







#------------------End of Methods-----------------------

if __name__ == '__main__':
	#port=int(sys.argv[1])
	#app.run(host="0.0.0.0", port=port)
	app.run( host="0.0.0.0", port=9001)
