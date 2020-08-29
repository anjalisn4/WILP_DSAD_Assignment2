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
import sys
class Vertex:
    def __init__(self, node):
        self.id = node
        self.adjacent = {}
        # Set distance to infinity for all nodes
        self.distance = sys.maxint
        # Mark all nodes unvisited        
        self.visited = False  
        # Predecessor
        self.previous = None

    def add_neighbor(self, neighbor, weight=0):
        self.adjacent[neighbor] = weight

    def get_connections(self):
        return self.adjacent.keys()  

    def get_id(self):
        return self.id

    def get_weight(self, neighbor):
        return self.adjacent[neighbor]

    def set_distance(self, dist):
        self.distance = dist

    def get_distance(self):
        return self.distance

    def set_previous(self, prev):
        self.previous = prev

    def set_visited(self):
        self.visited = True

    def __str__(self):
        return str(self.id) + ' adjacent: ' + str([x.id for x in self.adjacent])

class Graph:
    def __init__(self):
        self.vert_dict = {}
        self.num_vertices = 0

    def __iter__(self):
        return iter(self.vert_dict.values())

    def add_vertex(self, node):
        self.num_vertices = self.num_vertices + 1
        new_vertex = Vertex(node)
        self.vert_dict[node] = new_vertex
        return new_vertex

    def get_vertex(self, n):
        if n in self.vert_dict:
            return self.vert_dict[n]
        else:
            return None

    def add_edge(self, frm, to, cost = 0):
        if frm not in self.vert_dict:
            self.add_vertex(frm)
        if to not in self.vert_dict:
            self.add_vertex(to)

        self.vert_dict[frm].add_neighbor(self.vert_dict[to], cost)
        self.vert_dict[to].add_neighbor(self.vert_dict[frm], cost)

    def get_vertices(self):
        return self.vert_dict.keys()

    def set_previous(self, current):
        self.previous = current

    def get_previous(self, current):
        return self.previous

def shortest(v, path):
    ''' make shortest path from v.previous'''
    if v.previous:
        path.append(v.previous.get_id())
        shortest(v.previous, path)
    return

import heapq

def dijkstra(aGraph, start):
    print '''Dijkstra's shortest path'''
    # Set the distance for the start node to zero 
    start.set_distance(0)

    # Put tuple pair into the priority queue
    unvisited_queue = [(v.get_distance(),v) for v in aGraph]
    
    heapq.heapify(unvisited_queue)

    while len(unvisited_queue):
        # Pops a vertex with the smallest distance 
        uv = heapq.heappop(unvisited_queue)
        current = uv[1]
        current.set_visited()

        #for next in v.adjacent:
        for next in current.adjacent:
            # if visited, skip
            if next.visited:
                continue
            new_dist = current.get_distance() + current.get_weight(next)
            
            if new_dist < next.get_distance():
                next.set_distance(new_dist)
                next.set_previous(current)
                print 'updated : current = %s next = %s new_dist = %s' \
                        %(current.get_id(), next.get_id(), next.get_distance())
            else:
                print 'not updated : current = %s next = %s new_dist = %s' \
                        %(current.get_id(), next.get_id(), next.get_distance())
        # Rebuild heap
        # 1. Pop every item
        while len(unvisited_queue):
            heapq.heappop(unvisited_queue)
        # 2. Put all vertices not visited into the queue
        unvisited_queue = [(v.get_distance(),v) for v in aGraph if not v.visited]
        heapq.heapify(unvisited_queue)

class HospitalEmergency:

    # This function is called to get the shortest route
    def get_shortest_path(self,g):
        print ('Graph data:')
        for v in g:
            for w in v.get_connections():
                vid = v.get_id()
                wid = w.get_id()
                print ('( %s , %s, %3d)'  % ( vid, wid, v.get_weight(w)))    
        dijkstra(g, g.get_vertex(str(hospital_node.strip()))) 
        target = g.get_vertex(str(airport_node.strip()))
        path = [target.get_id()]
        shortest(target, path)
        shortest_path=path[::-1];
        print ('The shortest path : %s' %(path[::-1]))
        return shortest_path

    # This function is called to get the time taken for the ambulance to reach the airport
    def get_time_taken_to_reach_airport(self, distance):
        return 60*(float(distance)/80)

    # This is a helper function which returns the sequence of shortest path
    # if ['a','b','c'] is the shortest path, it returns [['a','b'],['b','c']]
    def get_path_sequence(self, shortest_path):
        shortest_path_sequence= []    
        for i in range(0, len(shortest_path)):
            current_node = shortest_path[i-1]
            next_node = shortest_path[i]   
            shortest_path_sequence.append([current_node,next_node])           
        shortest_path_sequence.pop(0)   
        return shortest_path_sequence

    # This is a helper function which returns the weight between 2 nodes
    def get_distance_between_nodes(self,from_node, to_node):
        distance=None;
        for v in g:
            for w in v.get_connections():
                vid = v.get_id()
                wid = w.get_id()
                if(vid == from_node and wid == to_node):
                    distance= v.get_weight(w)
                    break  
        return distance  

    # This function returns the shortest distance in kms, which the ambulance has to travel from hospital to airport.
    def get_shortest_distance(self, shortest_path):
        shortest_distance=0
        shortest_path_sequence= self.get_path_sequence(shortest_path)
        for i in shortest_path_sequence:
            distance_between_nodes =self.get_distance_between_nodes(i[0],i[1])
            shortest_distance += distance_between_nodes
        return shortest_distance

if __name__ == '__main__':
    hospitalEmergency = None
    inputs = open('inputPS11.txt', 'r')
    output = open('outputPS11.txt', 'w')
    STRING_CONCAT = "Shortest route from the hospital '%s' to reach the airport '%s' is %s\nand it has minimum travel distance %skm\nit will take %s minutes for the ambulance to reach the airport."
    vertices = []
    edges =[]
    for i in inputs:
        if 'Hospital Node' in i:
            itype, hospital_node = i.split(':')
        if 'Airport Node' in i:
            itype, airport_node = i.split(':')
        if '/' in i:
            edge = i.strip('\n').split('/')
            if edge[0].strip() not in vertices:
                vertices.append(edge[0].strip())
            if edge[1].strip() not in vertices:
                vertices.append(edge[1].strip())
            edges.append(edge)
    g = Graph() 
    for i in vertices:
        g.add_vertex(i)  
    for j in edges:
        g.add_edge(j[0].strip(),j[1].strip(),int(j[2].strip()))      

    hospitalEmergency = HospitalEmergency()
    shortest_path = hospitalEmergency.get_shortest_path(g)
    min_distance = str(hospitalEmergency.get_shortest_distance(shortest_path))
    time_taken =hospitalEmergency.get_time_taken_to_reach_airport(min_distance)
    output.write(STRING_CONCAT % (hospital_node.strip(),airport_node.strip(),shortest_path,min_distance,time_taken)) 