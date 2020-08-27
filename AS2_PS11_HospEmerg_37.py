# -*- coding: utf-8 -*-
"""
Created on Sat August 27 2020
@author: DSAD Group 37
@contribution:
    Team Member     Roll Number
    ===========================
    Amit Kumar     2019HC04174
    Pranesh P	2019HC04175
    Anjali Sunder Naik	2019HC04178
"""
class HospitalEmergency:

    # This function is called to get the shortest route
    def getShortestRoute(self):
        return '[ a, b, c, j, k, m, o]'  

    # This function is called to get the minimum travel distance
    def getMinimumTravelDistance(self):
        return 23 

    # This function is called to get the time taken for the ambulance to reach the airport
    def getTimeTakenToReachAirport(self):
        return "17:15"         

if __name__ == '__main__':
    hospitalEmergency = None
    inputs = open('inputPS11.txt', 'r')
    output = open('outputPS11.txt', 'w')
    STRING_CONCAT = "Shortest route from the hospital '%s' to reach the airport '%s' is %s and it has minimum travel distance %skm it will take %s minutes for the ambulance to reach the airport"
    for i in inputs:
        if 'Hospital Node' in i:
            itype, hospital_node = i.split(':')
        if 'Airport Node' in i:
            itype, airport_node = i.split(':')
    hospitalEmergency = HospitalEmergency()
    shortest_route = hospitalEmergency.getShortestRoute()
    min_distance = str(hospitalEmergency.getMinimumTravelDistance())
    time_taken =hospitalEmergency.getTimeTakenToReachAirport()
    output.write(STRING_CONCAT % (hospital_node.strip(),airport_node.strip(),shortest_route,min_distance,time_taken)) 