#!/usr/bin/env python3

import pyowm
from pyowm.exceptions import OWMError

import sys, argparse
from datetime import datetime

import os
#os.environ['OPENWEATHER_API_KEY'] = 'aa1ab6974298fc6bf7303d6a22e073f9'
#os.environ['CITY_NAME'] = 'Honolulu'

def main(argv):
   parser = argparse.ArgumentParser()
   parser.add_argument('-k', required=False, metavar='your_api_key')
   parser.add_argument('-p', required=False, metavar='\"Some Place,US\"')
   args = parser.parse_args()

   api_key = str(os.environ['OPENWEATHER_API_KEY'])
   place = str(os.environ['CITY_NAME'])

   print ('Using key ' + api_key  + ' to query temperature in \"' + place  + '\"...' )   
   owm = pyowm.OWM(api_key) 
   try:
      observation = owm.weather_at_place(place)
   except OWMError as err:
      print (err)
      sys.exit(2)

   w = observation.get_weather()
   p = observation.get_location()
   print ( 'source=openweathermap ' + 'city=' + '"' + p.get_name() + '"' + ' description=' + '"' + str(w.get_status()) + '"' +  \
           ' temp=' + str(w.get_temperature('celsius')['temp']) +'C' +  ' humidity=' + str(w.get_humidity()) )


if __name__ == "__main__":
   main(sys.argv[1:])

