
*This folder consists of scripts written in python which were deployed in the raspberry pi for collecting the data from the sensor.


*Requirements
->Python 2.7.9
-> pip install pyserial
-> pip install pynmea2
-> pip install MySQLdb

*The gps.py is deployed in the pi and it calls the gps sensor through the pi's serial port and communicates with the sensor to find the latitude and longitude of its current location and the data obtained is saved in the pi.Further the data is posted to the webserver. 
