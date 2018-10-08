"""
        This program implements the Kruskal's Algorithm to find the minimum spanning tree
"""

import cPickle as pkl

parent = dict()
rank = dict()

def Make_Set(v):
    parent[v] = v
    rank[v] = 0
    
def Find_Set(v):
    if parent[v] <> v:
        parent[v] = Find_Set(parent[v])
    return parent[v]

def Union(u, v):
    root1 = Find_Set(u)
    root2 = Find_Set(v)
    if root1 <> root2:
        if rank[root1]>rank[root2]:
            parent[root2] = root1
        else:
            parent[root1] = root2
            if rank[root1] == rank[root2]:
                rank[root2]+=1
                
def Kruskal(Graph):
    for v in Graph['Vertices']:
        Make_Set(v)
    Edges = list(Graph['Edges'])
    Edges.sort()
    #print Edges
    A = set()       # A is the MST
    
    for edge in Edges:
        weight , u, v = edge
        if Find_Set(u) <> Find_Set(v):
            A.add(edge)
            Union(u,v)
            
    return  A


try:
    
    #with open('input.pkl','rb') as fp:
        #Graph = pkl.load(fp)
    Graph = {
                'Vertices':['A','B','C','D','E','F','G','H','I'],
                'Edges':set([
                                (4,'A','B'),
                                (8,'B','C'),
                                (7,'C','D'),
                                (9,'D','E'),
                                (8,'A','H'),
                                (1,'H','G'),
                                (2,'G','F'),
                                (10,'F','E'),
                                (11,'B','H'),
                                (7,'H','I'),
                                (2,'I','C'),
                                (6,'I','G'),
                                (4,'C','F'),
                                (14,'D','F')
                            ])
            }
        
    print "\n The graph -\n"
    print Graph
    
    print "\n MST using Kruskal's Algorithm - \n"
    MST =  Kruskal(Graph)
    # Sorting MST so that edges are in increasing order
    MST = list(MST)
    MST.sort()
    #print len(MST)
    
    cost = 0
    for i in range(len(MST)):
        cost+=MST[i][0]
        
    for i in MST:
        print i,
        print "\n"
    print "\nMinimum Cost = ",cost
    print "\n"
    
except ValueError:
    print "\n ERROR: Invalid Input\n"
    exit(0)
    
