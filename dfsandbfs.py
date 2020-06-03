#Testing with graph traversal
from collections import deque

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
            self.Adjl[u].push(v)
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
        

#Set up adjacency list, or some kind of system to go through. 
# The one you made isn't the best; we could go with dicts, or just a list



#DFS
def DFS(graph, pos):
    frontier = deque([pos])
    explored = []
    
    
    while(frontier):
        node = frontier.popleft()
        #print("Popping: {}".format(node))
        if node not in explored:
            getnode= graph.Adjl[node].head.next
            while getnode != None:
                frontier.appendleft(getnode.name)
                #print(getnode.name)
                getnode=getnode.next
                
            explored.append(node)
    return explored
#BFS
#QEUEUEUEUEUEUEUEUEUEUEUEUEUEUEU EEEEEEEEE
def BFS(graph,pos):
    frontier = deque([pos])
    explored = []
    
    
    while(frontier):
        node = frontier.popleft()
        #print("Popping: {}".format(node))
        if node not in explored:
            getnode= graph.Adjl[node].head.next
            while getnode != None:
                frontier.append(getnode.name)
                #print(getnode.name)
                getnode=getnode.next
                
            explored.append(node)
    return explored


graph = Graph()
graph.AddEdge(0,1)
graph.AddEdge(0,3)
graph.AddEdge(3,5)
graph.AddEdge(5,6)
graph.AddEdge(5,7)
graph.AddEdge(6,8)
graph.AddEdge(7,8)
graph.AddEdge(1,2)
graph.AddEdge(1,4)
graph.AddEdge(4,9)
graph.AddEdge(9,10)
graph.AddEdge(11)
trav = DFS(graph,0)
graph.printsho()
print("DFS: {}".format(trav))
trav2 = BFS(graph,0)
print("BFS: {}".format(trav2))
