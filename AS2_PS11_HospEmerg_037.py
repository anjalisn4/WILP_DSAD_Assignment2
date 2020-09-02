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

from collections import defaultdict

class Graph():
    def __init__(self):
        """
        self.edges is a dict of all possible next nodes
        e.g. {'X': ['A', 'B', 'C', 'E'], ...}
        self.weights has all the weights between two nodes,
        with the two nodes as a tuple as the key
        e.g. {('X', 'A'): 7, ('X', 'B'): 2, ...}
        """
        self.edges = defaultdict(list)
        self.weights = {}
    
    def add_edge(self, from_node, to_node, weight):
        # Note: assumes edges are bi-directional
        self.edges[from_node].append(to_node)
        self.edges[to_node].append(from_node)
        self.weights[(from_node, to_node)] = weight
        self.weights[(to_node, from_node)] = weight

    def get_weight(self,from_node, to_node):
        weight= None
        for key, value in self.weights.items():
            if (key[0]==from_node and key[1]==to_node):
                weight= value
                break
        return weight    

    # This function implements Dijkstra algorithm , is called to get the shortest route
def _dijkstra(graph, initial, end):
    # shortest paths is a dict of nodes
    # whose value is a tuple of (previous node, weight)
    short_paths = {initial: (None, 0)}
    current = initial
    _visited = set()
    
    while current != end:
        _visited.add(current)
        destinations = graph.edges[current]
        weight_to_current = short_paths[current][1]

        for next_node in destinations:
            weight = graph.weights[(current, next_node)] + weight_to_current
            if next_node not in short_paths:
                short_paths[next_node] = (current, weight)
            else:
                current_shortest_weight = short_paths[next_node][1]
                if current_shortest_weight > weight:
                    short_paths[next_node] = (current, weight)
        
        next_destinations = {node: short_paths[node] for node in short_paths if node not in _visited}
        if not next_destinations:
            return "Route Not Possible"
        # next node is the destination with the lowest weight
        current = min(next_destinations, key=lambda k: next_destinations[k][1])
    
    # Work back through destinations in shortest path
    path = []
    while current is not None:
        path.append(current)
        next_node = short_paths[current][0]
        current = next_node
    # Reverse path
    path = path[::-1]
    return path

class HospitalEmergency:

    # This function is called to get the time taken for the ambulance to reach the airport
    def get_time_taken_to_reach_airport(self, distance):
        time_in_seconds= 60*60*(float(distance)/80);
        minutes = time_in_seconds // 60
        hours = minutes // 60
        if hours == 0.0:
            return ("%02d:%02d" % (minutes, time_in_seconds % 60))
        else:
            return ("%02d:%02d:%02d" % (hours, minutes % 60, time_in_seconds % 60))


    # This is a helper function which returns the sequence of shortest path
    # if ['a','b','c'] is the shortest path, it returns [['a','b'],['b','c']]
    def get_path_sequence(self, shortest_path):
        shortest_path_sequence= []    
        for i in range(0, len(shortest_path)):
            current = shortest_path[i-1]
            next_node = shortest_path[i]   
            shortest_path_sequence.append([current,next_node])           
        shortest_path_sequence.pop(0)   
        return shortest_path_sequence

    # This function returns the shortest distance in kms, which the ambulance has to travel from hospital to airport.
    def get_shortest_distance(self, shortest_path):
        shortest_distance=0
        shortest_path_sequence= self.get_path_sequence(shortest_path)
        for i in shortest_path_sequence:
            distance_between_nodes =g.get_weight(i[0],i[1])
            shortest_distance += distance_between_nodes
        return shortest_distance

if __name__ == '__main__':    
    hospitalEmergency = None
    inputs = open('inputPS11.txt', 'r')
    output = open('outputPS11.txt', 'w')
    STRING_CONCAT = "Shortest route from the hospital '%s' to reach the airport '%s' is %s\nand it has minimum travel distance %skm\nit will take %s minutes for the ambulance to reach the airport."
    edges =[]
    for i in inputs:
        i= i.lower()
        if ('hospital node' in i):
            hospital_node=i.split(':')[1].strip()
        if ('airport node' in i):
            airport_node=i.split(':')[1].strip()
        if '/' in i:
            edge = i.strip('\n').split('/')
            if(int(edge[2].strip())<0):
                raise ValueError('Invalid weight provided. Negative weight is not allowed in the current design.')
            input_edge= (edge[0].strip(),edge[1].strip(),int(edge[2].strip()))
            edges.append(input_edge)
    g = Graph() 
    for edge in edges:
        g.add_edge(*edge)
    
    hospitalEmergency = HospitalEmergency()
    shortest_path = _dijkstra(g, str(hospital_node.strip()),str(airport_node.strip()))
    if(shortest_path == 'Route Not Possible'):
        raise ValueError("Route is not possible. Please provide a valid input")
    else:     
        min_distance = hospitalEmergency.get_shortest_distance(shortest_path)
        time_taken = hospitalEmergency.get_time_taken_to_reach_airport(min_distance)
        output.write(STRING_CONCAT % (hospital_node.strip(),airport_node.strip(),shortest_path,min_distance,time_taken))    
 