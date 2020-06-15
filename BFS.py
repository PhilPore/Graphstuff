from collections import deque
import copy
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

    


class Graph:
    def __init__(self):
        self.Adjl ={}
    
    def AddEdge(self, u, v=None):
        if u not in self.Adjl.keys():
            self.Adjl[u] = SLL()
            self.Adjl[u].push(u)
        if v not in self.Adjl.keys() and v !=None:
            self.Adjl[v] = SLL()
            self.Adjl[v].push(v)
        if v != None:
            self.Adjl[u].append(v)
   
    def AddUnEdge(self, u, v=None):
        if u not in self.Adjl.keys():
            self.Adjl[u] = SLL()
            self.Adjl[u].push(u)
        if v not in self.Adjl.keys() and v != None:
            self.Adjl[v] = SLL()
            self.Adjl[v].push(v)
        if v !=None:
            self.Adjl[u].append(v)
            self.Adjl[v].append(u)


    def printsho(self):
        for k in self.Adjl:
            j = self.Adjl[k].head
            while j != None:
                print(j.name, end ='->')
                j = j.next
            print("X")  
            
#just a standard bfs here
def BFS(graph,pos):
    frontier = deque([pos])
    explored = []
    
    
    while(frontier):
        node = frontier.popleft()
        #print("Popping: {}".format(node))
        if node not in explored:
            #print(node)
            getnode= graph.Adjl[node].head.next
            while getnode != None:
                #if getnode.name not in frontier:
                frontier.append(getnode.name)
                #print(getnode.name)
                getnode=getnode.next
                
            explored.append(node)
            #print(explored)
    return explored

#get the shortest path of nodes in a graph
def BFSpathto(graph, start, end):
    pred = [-1 for i in range(len(graph.Adjl))]
    frontier = deque([start])
    explored = []
    pred[start] = start
    #print("=")
    #print(pred[start])
    while(frontier):
        node = frontier.popleft()
        #print("Node is {}".format(node))
        #print("Popping: {}".format(node))
        if node == end:
            break
        if node not in explored:
            
            getnode= graph.Adjl[node].head.next
            while getnode != None:
                #if getnode.name not in frontier:
                if getnode.name not in explored:
                    #print(explored)
                    #print("{} | {}".format(node, getnode.name))
                    frontier.append(getnode.name)
                    if pred[getnode.name] == -1:
                        pred[getnode.name] = node
                    #print(pred)
                print(getnode.name)
                getnode=getnode.next
                
            explored.append(node)
            #print(explored)
    
    print(pred)
    crawl = end
    retrace = deque([crawl])
    while pred[crawl] != -1:
        if pred[crawl] == start:
            retrace.appendleft(pred[crawl])
            break
        retrace.appendleft(pred[crawl])
        crawl = pred[crawl]
    print(list(retrace))
    return list(retrace)
        
class Travers:
    def __init__(self,sr,sc,lvl,parents =[]):
        self.sr = sr
        self.sc = sc
        self.lvl = lvl
        self.parents = parents
    def __str__(self):
        return("{},{}\nLevel: {}\nParent {}".format(self.sr,self.sc,self.lvl,self.parents))
         

def BFSMaze(sr,sc,grph):
    dr = [-1,0,1,0]
    dc = [0,1,0,-1]
    crawl = []
    level = 0
    walk = Travers(sr,sc,level,[sr,sc])
    frontier = deque([walk])
    explored = []
    tracer = [[[-1,-1] for i in range(len(grph[0]))] for j in range(len(grph))]
    tracer[sr][sc] = [0,0]
    while(frontier):
        node = frontier.popleft()
        #print(node)
        
        if grph[node.sr][node.sc] == 'E':
            tracer[node.sr][node.sc] = node.parents
            print("Found with {} steps! {} {}".format(node.lvl,node.sr, node.sc))
            crawl = [node.sr,node.sc]
            #print(tracer[crawl[0]][crawl[1]])
            #print(tracer[1][3])
            break
        if [node.sr,node.sc] not in explored:
            for i in range(4):
                R = node.sr+dr[i]
                C = node.sc+dc[i]
                if R < 0 or C < 0:
                    continue
                if R >= len(grph) or C >= len(grph[0]):
                    continue
                if grph[R][C] == '#' or [R,C] in explored:
                    continue
                enq = Travers(R,C,node.lvl+1,[node.sr,node.sc])
                frontier.append(enq)
                #print(enq)
            
                tracer[R][C] = [node.sr,node.sc]
            explored.append([node.sr,node.sc])       
    #print(crawl)
    #print(explored)
    #for i in range(len(tracer)):
    #    print(tracer[i])
    #trav = []
    while crawl != [-1,-1]:
        if grph[crawl[0]][crawl[1]]=='S':
            for i in range(len(grph)):
                print(grph[i])
            return grph
        if grph[crawl[0]][crawl[1]] == 'E':
            crawl = tracer[crawl[0]][crawl[1]]
            continue
        grph[crawl[0]][crawl[1]] = '*'
        crawl = tracer[crawl[0]][crawl[1]]
   
    
    #print(walk.sr)
    '''
    tracer = [[[-1,-1] for i in range(len(grph[0]))] for j in range(len(grph))]
    tracer[sr][sc] = [0,0]
    for i in range(len(tracer)):
        print(tracer[i])
    '''
    





dung = [
    ['S','#','.','#','#'],
    ['.','.','.','.','.'],
    ['.','#','#','E','.'],
    ['.','.','.','.','.'],
    ['#','.','#','#','#']
]
graph = Graph()
graph.AddUnEdge(0,9)
graph.AddUnEdge(0,7)
graph.AddUnEdge(0,11)
graph.AddUnEdge(11,7)
graph.AddUnEdge(9,10)
graph.AddUnEdge(9,8)
graph.AddUnEdge(10,1)
graph.AddUnEdge(7,6)
graph.AddUnEdge(7,3)
graph.AddUnEdge(8,12)
graph.AddUnEdge(6,5)
graph.AddUnEdge(12,2)
graph.AddUnEdge(3,2)
graph.AddUnEdge(3,4)

#graph.printsho()
#exp = BFS(graph,0)
#print(exp)
#print(len(graph.Adjl))
#BFSpathto(graph, 0, 11)
x = BFSMaze(0,0,dung)
for i in range(len(x)):
    print(x[i])
