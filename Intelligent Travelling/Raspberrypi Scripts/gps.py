import serial 
import pynmea2
import MySQLdb
import time as t
import requests

serialStream = serial.Serial("/dev/ttyAMA0",9600,timeout=0.5)
#db=MySQLdb.connect(host="db4free.net",user="bhure",passwd="123456789",db="latlon")
#cur=db.cursor()
print "connection established"
time=""
lat=""
lon=""
i=0
x=21.144453
y=79.054140
while True:
    try:
        sent=serialStream.readline()
        if sent.find('GGA')>0:
            data=pynmea2.parse(sent)
            time=data.timestamp
            lat=data.latitude        
            lon=data.longitude
            print "{time}: {lat}, {lon}".format(time=data.timestamp ,lat=data.latitude,lon=data.longitude)
            #cur.execute("update busroute set time=%s,lat=%s,lon=%s where srno=1",(time,lat,lon))
            #cur.execute("update busroute set lat=%s,lon=%s where srno=1",(lat,lon))
            #db.commit();
            #if lat=='None' or lon=='None':
            #print "match found"
            #lat=21.144453        
            #lon=79.054140
            #else:
            r=requests.post("http://59.95.137.3:80/sendValues",data={'a':lat,'b':lon})
            #print "did not match"
            #x=x+0.0001
            #y=y+0.0001
            #i=i+1
            #print "data sent "+str(i)+"times"
    except:
        print "error man"
        continue

