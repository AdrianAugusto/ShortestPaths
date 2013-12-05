fileName = input("Please enter a filename with the extension: ")

class vertex:
    def __init__(self, name, dist, pred):
        self.name = name
        self.dist = dist
        self.pred = pred

    def __lt__(self, other):
        if self.dist == "infinity":
            return False
        elif other.dist == "infinity" and self.dist == "infinity":
            return False
        elif self.dist < other.dist:
            return True
        else:
            return False

    def __gt__(self, other):
        if other.dist == "infinity" and self.dist == "infinity":
            return False
        elif self.dist != "infinity" and self.dist > other.dist:
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
                vertexU = vertex(lineList[0], "infinity", None)
                
            if vertexU not in Q:
                Q.append(vertexU)
                
            if lineList[1] == "s" or lineList[1] == "S":
                vertexV = vertex(lineList[1], 0, None)
            else:
                vertexV = vertex(lineList[1], "infinity", None)
            
            if vertexV not in Q:
                Q.append(vertexV)
            edgeObj = edge(vertexU, vertexV, int(lineList[2]))
            print("EDGE: v={0} and u={1}".format(edgeObj.u.name, edgeObj.v.name))
            edges.append(edgeObj)
                
        while Q != []:
            u = min(Q)
            print(u.name)
            Q.remove(u)
            S.append(u)
            for edge in edges: 
                if edge.u == u:
                    #print("v={0} and u={1}".format(edge.u.name, edge.v.name))
                    #if edge.v in Q:
                    index = edges.index(edge)
                    if edge.v.dist == "infinity" or edge.v.dist > (u.dist + int(edge.weight)): #Relax
                        edge.v.dist = u.dist + int(edge.weight)
                        edge.v.pred = u
                        if edge.v in Q:
                            indexV = Q.index(edge.v)
                            Q[indexV].dist = u.dist + int(edge.weight)  #Relax
                            Q[indexV].pred = u
                            print("v={0}, dist={1}".format(Q[indexV].name, Q[indexV].dist))

        for v in S:
            print("v={0} and distance={1}".format(v.name, v.dist))

    else:
        print("This is an undirected graph")

    

    #for line in f:
    #   line

