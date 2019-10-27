from flask import Flask, render_template, send_file, request, redirect
import pygeoj,json
import math, random, operator
from math import atan2
from functools import reduce
import subprocess
from twilio.twiml.messaging_response import MessagingResponse
from geopy.geocoders import Nominatim

poly=[]
#this is the initial data of the docid mapped with clinic
doclocations={'doc8': ['Mumbai, Maharashtra, India', 72.877426, 19.07609], 'doc9': ['Sagar, Karnataka, India', 75.040298, 14.16704], 'doc2': ['Goregaon, Mumbai, Maharashtra, India', 72.849998, 19.155001], 'doc3': ['Pindwara, Rajasthan, India', 73.055, 24.7945], 'doc0': ['Chittorgarh, Rajasthan, India', 74.629997, 24.879999], 'doc1': ['Ratnagiri, Maharashtra, India', 73.300003, 16.994444], 'doc6': ['Lucknow, Uttar Pradesh, India', 80.949997, 26.85], 'doc7': ['Delhi, the National Capital Territory of Delhi, India', 77.230003, 28.610001], 'doc4': ['Raipur, Chhattisgarh, India', 81.629997, 21.25], 'doc5': ['Gokak, Karnataka, India', 74.833298, 16.1667], 'doc21': ['Karaikal, Puducherry, India', 79.838005, 10.92544], 'doc20': ['Ranebennur, Karnataka, India', 75.621788, 14.623801], 'doc23': ['Chatrapur, Odisha, India', 84.986732, 19.354979], 'doc22': ['Belgaum, Karnataka, India', 74.498703, 15.852792], 'doc25': ['Bhubaneswar, Odisha, India', 85.824539, 20.296059], 'doc24': ['Suri, West Bengal, India', 87.52462, 23.905445], 'doc27': ['Jagadhri, Haryana, India', 77.299492, 30.172716], 'doc26': ['Mahuva, Gujarat, India', 71.771645, 21.105001], 'doc29': ['Bhusawal, Maharashtra, India', 75.801094, 21.045521], 'doc28': ['Barh, Bihar, India', 85.709091, 25.477585], 'doc38': ['Haringhata, West Bengal, India', 88.567406, 22.96051], 'doc49': ['Sambhal, Uttar Pradesh, India', 78.571762, 28.590361], 'doc39': ['Kushtagi, Karnataka, India', 76.192696, 15.756595], 'doc43': ['Ambernath, Maharashtra, India', 73.191948, 19.186354], 'doc42': ['Surajpur, Chhattisgarh, India', 82.87056, 23.223047], 'doc41': ['Orai, Uttar Pradesh, India', 79.450035, 25.989836], 'doc40': ['Jadugora, Jharkhand, India', 86.352882, 22.656015], 'doc47': ['Durg, Chhattisgarh, India', 81.28492, 21.190449], 'doc46': ['Vizianagaram, Andhra Pradesh, India', 83.395554, 18.106659], 'doc45': ['Jorapokhar, Jharkhand, India', 85.760651, 22.422455], 'doc44': ['Malerkotla, Punjab, India', 75.890121, 30.525005], 'doc48': ['Himmatnagar, Gujarat, India', 72.969818, 23.597969], 'doc18': ['Surendranagar, Gujarat, India', 71.637077, 22.728392], 'doc19': ['Thiruvalla, Kerala, India', 76.574059, 9.383452], 'doc30': ['Alipurduar, West Bengal, India', 89.5271, 26.49189], 'doc31': ['Kollam, Kerala, India', 76.614143, 8.893212], 'doc36': ['Harihar, Karnataka, India', 75.801094, 14.530457], 'doc37': ['Rasayani, Maharashtra, India', 73.176132, 18.901457], 'doc34': ['Mettur, Tamil Nadu, India', 77.800781, 11.786253], 'doc35': ['Huliyar, Karnataka, India', 76.540154, 13.583274], 'doc10': ['Jalpaiguri, West Bengal, India', 88.719391, 26.540457], 'doc11': ['Pakur, Jharkhand, India', 87.849251, 24.633568], 'doc12': ['Sardarshahar, Rajasthan, India', 74.493011, 28.440554], 'doc13': ['Sirohi, Rajasthan, India', 72.858894, 24.882618], 'doc14': ['Jaysingpur, Maharashtra, India', 74.556374, 16.779877], 'doc15': ['Ramanagara, Karnataka, India', 77.281296, 12.715035], 'doc16': ['Chikkaballapura, Karnataka, India', 77.727478, 13.432515], 'doc17': ['Channapatna, Karnataka, India', 77.208946, 12.651805], 'doc32': ['Medinipur, West Bengal, India', 87.321487, 22.430889], 'doc33': ['Patan, Gujarat, India', 72.126625, 23.849325]}
# populate={}
# counter=pygeoj.load(filepath="json/geo.geojson")
# for feature in counter['features']:
#     if feature['properties']['name'] not in populate:
#         populate[feature['properties']['name']]=1
#     else:
#         populate[feature['properties']['name']]+=1
      
app=Flask(__name__)

def geoFence(long,lat): #to generate points around the main point, so as to create the geofence
    global poly
    # global fencecount
    # print long,lat 
    python2_command="python3 genGeoCoords.py "+str(lat)+" "+str(long)
    process=subprocess.Popen(python2_command.split(),stdout=subprocess.PIPE)
    output,error=process.communicate()
    # print(output)

    sortedcor=output.splitlines()[0]
    # for dat in sortedcor:
        # print(dat)
    # print(sortedcor)
    # for val in sortedcor:
        # val[0]=float(val[0])
        # val[1]=float(val[1])
        # print(val)
    newsorted=sortedcor.replace('[','').replace(']','').replace(',','').split()
    # print(newsorted)
    finalcor=[]
    for dat in range(0,len(newsorted),2):
        finalcor.append([float(newsorted[dat]),float(newsorted[dat+1])])
    # print(finalcor)
    poly=finalcor
    # print(poly)
    geoAdd=pygeoj.load(filepath="json/geo.geojson")
    
    nameToAdd="fence"+str(random.uniform(0,1))
    geoAdd.add_feature(properties={"name":nameToAdd},
                         geometry={"type":"Polygon","coordinates":[finalcor]})
    geoAdd.add_all_bboxes()
    geoAdd.update_bbox()
    geoAdd.save("json/geo.geojson")
    
    
def checkfence():
    populate={}
    # testfile=pygeoj.load(filepath="json/geo.geojson")
    with open('json/geo.geojson') as f:
        testfile=json.load(f)
        f.close()
    for feature in testfile['features']:
        if feature['properties']['name'] not in populate:
            populate[feature['properties']['name']]=1
        else:
            populate[feature['properties']['name']]+=1
            if populate[feature['properties']['name']]>4: #exceeds the threshold
                geoCenter=feature['geometry']['coordinates']
                # print(geoCenter)
                if len(geoCenter)==2:
                    geoFence(geoCenter[0],geoCenter[1])
    

def checkInside(x,y,poly):
    # for val in ultimateFinalCoords:
    print(poly,x,y)
    num = len(poly)
    i = 0
    j = num - 1
    c = False
    
    for i in range(num):
        if ((poly[i][1] > y) != (poly[j][1] > y)) and \
                (x < poly[i][0] + (poly[j][0] - poly[i][0]) * (y - poly[i][1]) /
                                  (poly[j][1] - poly[i][1])):
            c = not c
        j = i
    return c
    
    

    
@app.after_request #for no caching
def set_response_headers(response):
    response.headers['Cache-Control'] = 'no-store'
    return response
    
@app.route("/",methods=['GET', 'POST'])
def index():
    return render_template("index.html")

@app.route('/points/') #to return the file 
def return_files_tut():
	try:
		return send_file('json/geo.geojson', attachment_filename='geo.geojson',cache_timeout=-1)
	except Exception as e:
		return str(e)

@app.route('/docportal/',methods=['POST','GET'])
def doc_gen():
    return render_template("doc2.html")

@app.route('/handle_data', methods=['POST'])
def handle_data():
    docID = request.form['docID']
    disease=request.form['disease']
    # print(docID, disease)
    content=doclocations[docID]
    # print(content)
    
    #to put the coordinates associated with the unique doc id to the geojson file for the azure heatmap
    testfile=pygeoj.load(filepath="json/geo.geojson")
    testfile.add_feature(properties={"name":str(content[0])},
                         geometry={"type":"Point","coordinates":[float(content[1]),float(content[2])]})
    testfile.add_all_bboxes()
    testfile.update_bbox()
    testfile.save("json/geo.geojson")
    checkfence()
    return render_template("doc2.html", content=content)

@app.route("/sms", methods=['GET', 'POST'])
def incoming_sms():
    """Send a dynamic reply to an incoming text message"""
    # Get the message the user sent our Twilio number
    body = request.values.get('Body', None)
    # print(body)
    # Start our TwiML response
    resp = MessagingResponse()
    msg=""
    global poly
    # Determine the right reply for this message
    if body == 'location':
        resp.message("Can you please send your nearest landmark!")
    elif body == 'update':
        resp.message("Can you re-enter your nearest location")
    else:
        geolocator = Nominatim(user_agent="aarogya")
        location = geolocator.geocode(body)
        # print len(poly)
        if location !=None:
            if len(poly)!=0:
                # print "inside here yay"
                insideGeofence=checkInside(location.longitude, location.latitude,poly)
                
                if insideGeofence:
                    msg+="Your address is at "+ str(location.address)+" and your approximate coordinates are "+str(location.latitude)+" "+str(location.longitude)
                    msg+="\nBEWARE!! YOU'RE NEAR A DENGUE PRONE AREA. \n HERE ARE SOME TIPS -\n1)Apply Odomos\n2)Don't let water remain in open spaces\n3)Wear Long Sleeve Shirts and Trousers\n For more information, head onto https://www.cdc.gov/dengue/prevention/index.html \n STAY SAFE! NAMASTE"
                    resp.message(msg)
                
                else:
                    msg+="Your address is at "+ str(location.address)+" and your approximate coordinates are "+str(location.latitude)+" "+str(location.longitude)
                    msg+="\nYou're not near to any disease prone area. STAY SAFE! NAMASTE"
                    resp.message(msg)
                    # print(location.address)
                    # print((location.latitude, location.longitude))
            else:
                msg+="Your address is at "+ str(location.address)+" and your approximate coordinates are "+str(location.latitude)+" "+str(location.longitude)
                msg+="\nYou're not near to any disease prone area. STAY SAFE! NAMASTE"
                resp.message(msg)
        
    return str(resp)

# @app.route("/sms", methods=['GET', 'POST'])
# def sms_reply():
#     """Respond to incoming calls with a simple text message."""
#     # Start our TwiML response
#     resp = MessagingResponse()

#     # Add a message
#     resp.message("The Robots are coming! Head for the hills!")

#     return str(resp)

if __name__=='__main__':
    app.run(debug=True,threaded=True)

