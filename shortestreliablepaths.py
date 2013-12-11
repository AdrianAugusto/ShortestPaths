fileName = input("Please enter a filename with the extension: ")
k = input("Please enter maximum edges for the path to take: ")
source = input("Please enter the source vertex: ")
print("Shortest Reliable Paths Algorithm")
print("Integer k: {0} Source: {1}".format(k, source))
class vertex:
    def __init__(self, name, dist, pred):
        self.name = name
        self.dist = dist
        self.pred = pred

    def __lt__(self, other):
        if self.dist == -1:
            return False
        elif other.dist == -1 and self.dist == -1:
            return False
        elif self.dist < other.dist:
            return True
        else:
            return False

    def __gt__(self, other):
        if other.dist == -1 and self.dist == -1:
            return False
        elif self.dist != -1 and self.dist > other.dist:
            return True
        else:
            return False

    def __eq__(self, other):
        if self.name == other.name:
            return True
        else:
            return False

class edge:
    def __init__(self, u, v, weight):
        self.u = u
        self.v = v
        self.weight = weight

directed = False
with open(fileName, "r") as f:
    line = f.readline()
    if line[0] == "D":
        directed = True

    vertices = []
    edges = []
    #Initialize shortest paths to vertices as -1
    for line in f:
        lineList = line.split() #lineList contains [u, v, w]
        edgeObj = edge(lineList[0], lineList[1], int(lineList[2]))
        vertexU = None
        vertexV = None
            
        if lineList[0] == source:
            vertexU = vertex(lineList[0], 0, None)
        else:
            vertexU = vertex(lineList[0], -1, None)
                
        if vertexU not in vertices:
            vertices.append(vertexU)
                
        if lineList[1] == source:
            vertexV = vertex(lineList[0], 0, None)
        else:
            vertexV = vertex(lineList[1], -1, None)
            
        if vertexV not in vertices:
            vertices.append(vertexV)
        edgeObj = edge(vertexU, vertexV, int(lineList[2]))
        edges.append(edgeObj)

    iterations = 1 # Used for establishing the minimum weight
    mem = []
    vertexReceiver = vertices[:] #Used for appending vertices removed from "vertices"
    
    lengths = [] # The lengths of the shortest paths to the vertices
    for i in range(int(k)+1):
        lengths.append(-1)
    for i in range(len(vertices)):
        mem.append(lengths[:])
    #d(v, i) = min[d(u, i - 1) + w(u, v)] for all (u, v) in E
    while vertices != []:
        v = min(vertices)
        indexV = vertexReceiver.index(v)
        indexU = -1
        if v.name == source:
            mem[indexV][0] = 0
        minimum = -1 # Minimum weight path of length i for directed graphs
        minimumD = -1
        indexX = -1
        indexY = -1
        vertices.remove(v)
        for i in range(1, int(k)+1):
            firstMin = True # For assignment of first minimum to min
            for edge in edges:
                #print("Second for loop")
                if edge.v == v:
                    indexU = vertexReceiver.index(edge.u)
                    if firstMin == True and mem[indexU][i-1] != -1:
                        minimum = mem[indexU][i-1] + edge.weight
                        firstMin = False
                    elif firstMin == False and mem[indexU][i-1] != -1:
                        if mem[indexU][i-1] + edge.weight < minimum:
                            minimum = mem[indexU][i-1] + edge.weight
                            
                #if directed == False:
                #    print("Here!")
                #    firstMinD = True
                #    if edge.u == v:
                #        x = v #x is used for denoting edge (x, u) = (v, u)
                #        indexX = vertexReceiver.index(edge.v)
                #        indexU = vertexReceiver.index(edge.u)
                #        print("Edge: u={0} v={1}".format(v.name, edge.u.name))
                #        if firstMinD == True and mem[indexX][i-1] != -1:
                #            minimumD = mem[indexX][i-1] + edge.weight
                #            firstMinD = False
                #        if firstMinD == False and mem[indexX][i-1] != -1:
                #            if mem[indexX][i-1] + edge.weight < minimum:
                #                minimum = mem[indexX][i-1] + edge.weight
                #                print("Non firstMin: {0}".format(minimum))
                #    mem[indexU][i] = minimumD
            mem[indexV][i] = minimum
            #print("MinimumD: {0} for vertex {1}".format(minimum, v.name))
                
    #Determine minimum shortest paths of all veritices within k
    for vertex in vertexReceiver:
        firstShortestPath = True # For assignment of first shortest path to shortestpath
        shortestPath = -1
        for i in range(int(k)+1):
            tempMem = mem[vertexReceiver.index(vertex)][i]
            if firstShortestPath == True and tempMem != -1:
                shortestPath = tempMem
                firstShortestPath = False
            elif firstShortestPath == False and tempMem != -1:
                if tempMem < shortestPath:
                    shortestPath = tempMem
        print("NODE {0}: {1}".format(vertex.name, shortestPath))
    

print("End Shortest Reliable Paths Algorithm")
