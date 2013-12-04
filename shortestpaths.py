fileName = input("Please enter a filename with the extension: ")

class vertex:
    def __init__(self, name, distance, pred):
        self.name = name
        self.distance = distance
        self.pred = pred

    def __lt__(self, other):
        if self.distance == "infinity":
            return False
        elif other.distance == "infinity" and self.distance == "infinity":
            return False
        elif self.distance < other.distance:
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
            edges.append(edgeObj)
            if edgeObj.u == "s" or edgeObj.u == "S":
                vertexObj = vertex(edgeObj.u, 0, None)
            else:
                vertexObj = vertex(edgeObj.u, "infinity", None)
                
            if vertexObj not in Q:
                Q.append(vertexObj)
                
            if edgeObj.v == "s" or edgeObj.v == "S":
                vertexObj = vertex(edgeObj.v, 0, None)
            else:
                vertexObj = vertex(edgeObj.v, "infinity", None)
            
            if vertexObj not in Q:
                Q.append(vertexObj)
                
        while Q != []:
            u = min(Q)
            print(u.name)
            Q.remove(u)
            S.append(u)

    else:
        print("This is an undirected graph")

    

    #for line in f:
    #   line

f.close()
