# Dijkstra's Algorithm in Python

class AdjNode:
    def __init__(self, data):
        self.vertex = data
        self.next = None


class NodeEgWt:
    def __init__(self, start, end, weight):
        self.start = start
        self.end = end
        self.weight = weight


class Graph:
    def __init__(self, vertices):
        self.V = vertices
        self.graph = [None] * self.V

    # Function to add an edge in an undirected graph
    def add_edge(self, src, dest):
        return

    def print_graph(self):
        for item in range(self.V):
            print("Adjacency list of vertex {}\n head".format(i), end="")
            temp = self.graph[item]
            while temp:
                print(" -> {}".format(temp.vertex), end="")
                temp = temp.next
            print(" \n")
    #End

if __name__ == '__main__':
    gvertices = []
    weightededges = []
    originating_point = "hospital node"
    destination_point = "airport node"
    found = 0
    shortest_path = []
    visited_node = []

    inputs = open('inputPS11.txt', 'r')
    output = open('outputPS11.txt', 'w')
    STRING_CONCAT = "%s >> %s\n"
    for i in inputs:
        i = str(i.lower())
        if originating_point in i:
            h, n = i.split(':')
            originating_point = n
        elif destination_point in i:
            h, n = i.split(':')
            destination_point = n
        else:
            r = i.split('/')
            s = r[0].strip()
            e = r[1].strip()
            w = int(r[2])
            if w < 0:
                print("Negative Weight not allowed")
                quit()
            Obj_rel = NodeEgWt(s, e, w)
            weightededges.append(Obj_rel)
            gvertices.append(s)
            gvertices.append(e)

    gvertices = set(gvertices)
    print("originating_point=", originating_point, "destination_point=", destination_point)
    print(len(gvertices), "Unique Node ", gvertices)
    graph = Graph(len(gvertices))
    for node in weightededges:
        print("start=", node.start, "end=", node.end, "Weight=", node.weight)
        graph.add_edge(node.start, node.end)
    #graph.print_graph()