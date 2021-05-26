#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat May 22 16:59:56 2021

@author: Gibran  | The purpose of this script is to demonstrate proficiency with Python for an Alta3 certification.  
Course started on April 26th with Chad Feeser.

Make an API request to Https://api.nasa.gov and display the number of potentially hazardous asteroids, returns it in 
an easily read format.
"""

#Import third party requests library rather than urllib.
import requests

def main():
    #Create r which is our requests object.
    r = requests.get("https://api.nasa.gov/neo/rest/v1/feed?start_date=2015-09-07&end_date=2015-09-08&api_key=DEMO_KEY")

 
    # the .json() method will dump a JSON string into Pythonic data structures. 
    data = r.json()  #Convert Json to Pythonic dictionary

    #Set initial hazards to zero
    hazard= 0
    #For loop iterates through the dictionary for each date in near earth object.
    for date in data["near_earth_objects"]:
        #Iterate through each value under the date looking for "Is potentially hazardous"
        for dict in data["near_earth_objects"][date]:
            #Increment counter by one for each occurrence of "is_potentially_hazardous_asteroid"
            if "is_potentially_hazardous_asteroid":      
                hazard += 1

    #Print the total number of potentially hazardous asteroids
    print("The number of hazardous asteroids is: " + str(hazard))
   

main()

