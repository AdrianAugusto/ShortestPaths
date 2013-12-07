#NOTE: -1 means infinity

fileName = input("Please enter a filename with the extension: ")

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

with open(fileName, "r") as f:
    line = f.readline()
    if line[0] == "D":
        Q = []
        S = []
        edges = []
        for line in f:
            lineList = line.split() #lineList contains [u, v, w]
            edgeObj = edge(lineList[0], lineList[1], lineList[2])
            vertexU = None
            vertexV = None
            
            if lineList[0] == "s" or lineList[0] == "S":
                vertexU = vertex(lineList[0], 0, None)
            else:
                vertexU = vertex(lineList[0], -1, None)
                
            if vertexU not in Q:
                Q.append(vertexU)
                
            if lineList[1] == "s" or lineList[1] == "S":
                vertexV = vertex(lineList[1], 0, None)
            else:
                vertexV = vertex(lineList[1], -1, None)
            
            if vertexV not in Q:
                Q.append(vertexV)
            edgeObj = edge(vertexU, vertexV, int(lineList[2]))
            edges.append(edgeObj)
                
        while Q != []:
            u = min(Q)
            print(u.name)
            Q.remove(u)
            S.append(u)
            for edge in edges: 
                if edge.u == u:
                    vDist = None
                    if edge.v in Q:
                        vIndex = Q.index(edge.v)
                        vDist = Q[vIndex].dist
                        if vDist == -1 or (vDist > (u.dist + int(edge.weight))): #Relax
                            vIndex = Q.index(edge.v)
                            Q[vIndex].dist = u.dist + int(edge.weight)
                            Q[vIndex].pred = u

        for v in S:
            print("v={0} and distance={1}".format(v.name, v.dist))

    else:
        print("This is an undirected graph")

    

    #for line in f:
    #   line

