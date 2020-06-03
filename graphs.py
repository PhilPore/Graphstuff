class AdjMatrix:
    
    def __init__(self):
        self.AdjMat ={}
        
    
    def appendUndir(self,source, dest):
        if source not in self.AdjMat.keys():
            self.AdjMat[source] = []
        if dest not in self.AdjMat.keys():
            self.AdjMat[dest] = []
        #print(self.AdjMat.keys)
        self.AdjMat[source].append(dest)
        self.AdjMat[source].sort()
        self.AdjMat[dest].append(source)
        self.AdjMat[dest].sort()

    def appenddir(self,source, dest):
        if source not in self.AdjMat.keys() and dest not in self.AdjMat.keys():
            self.AdjMat[source] = []
        self.AdjMat[source].append(dest)
        self.AdjMat[source].sort()


    def show_connect(self):
        for edge in sorted(self.AdjMat):
            for i in self.AdjMat[edge]:
                print("Edge {} connects to {}".format(edge, i))
class AdjentM:
    def __init__(self, vert):
        self.vert = vert
        self.AdjMat = [[0 for i in range(self.vert)] for j in range(self.vert)]
    def addUndirEdge(self, u, v):
        self.AdjMat[u][v] = 1
        self.AdjMat[v][u] = 1 
    
    def AdddirEdge(self, u, v):
        self.AdjMat[u][v] = 1
    

    def PrintGraph(self):
        for i in range(len(self.AdjMat)):
            print(self.AdjMat[i])
    def Relations(self):
        for i in range(len(self.AdjMat)):
            for j in range(len(self.AdjMat[i])):
                if self.AdjMat[i][j] == 1:
                    print("Vertice {} is connected to vertice {}".format(i,j))
        


#Adjancey list
class Node: #The node for our graph

    def __init__(self, name):
        self.name = name
        self.next = None
    
class SLL:
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0
    
    def push(self, val):
        if self.head == None:
            self.head = Node(val)
            self.tail = self.head
            self.size+=1
        else:
            temp = Node(val)
            temp.next = self.head
            self.head = temp
            self.size+=1
    

    def append(self,val):
        
        if self.head == None:
            self.push(val)
        else:
            
            temp = Node(val)
            self.tail.next = temp
            self.tail = temp
            self.tail.next = None
            self.size+=1

    


class AdjList:
    def __init__(self):
        self.Adjl ={}
    
    def AddEdge(self, u, v):
        if u not in self.Adjl.keys():
            self.Adjl[u] = SLL()
            self.Adjl[u].push(u)
        self.Adjl[u].append(v)
    def AddUnEdge(self, u, v):
        if u not in self.Adjl.keys():
            self.Adjl[u] = SLL()
            self.Adjl[u].push(u)
        if v not in self.Adjl.keys():
            self.Adjl[v] = SLL()
            self.Adjl[u].push(v)
        self.Adjl[u].append(v)
        self.Adjl[v].append(u)


    def printsho(self):
        for k in self.Adjl:
            j = self.Adjl[k].head
            while j != None:
                print(j.name, end ='->')
                j = j.next
            print("X")          
        

    


graph = AdjMatrix()
graph.appendUndir(1,2)
graph.appendUndir(1,3)
graph.appendUndir(1,4)
graph.appendUndir(4,2)
graph.appendUndir(4,3)
graph.show_connect()

AdjM = AdjentM(5)
AdjM.addUndirEdge(0,1)
AdjM.addUndirEdge(0,2)
AdjM.addUndirEdge(0,4)
AdjM.addUndirEdge(1,0)
AdjM.addUndirEdge(1,3)

AdjM.PrintGraph()

AdjM.Relations()


Ad = AdjList()
Ad.AddEdge('A','B')
Ad.AddEdge('A','C')
Ad.AddEdge('A','D')
Ad.AddEdge('B','A')
Ad.AddEdge('B','F')
Ad.AddEdge('C', 'W')

Ad.printsho()
        