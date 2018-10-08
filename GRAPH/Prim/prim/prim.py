"""
	This program implements the prims algorithm
"""

def Prim(Graph):
    # intializing Adjacent matrix
    """
    Adj_matrix = [[0]*(len(vertices))]*len(vertices)
      
    Edges = list(Graph['Edges'])
    
    
    for edge in Edges:
        weight , u, v = edge
        Adj_matrix[u][v] = weight
        Adj_matrix[v][u] = weight
    """    
    # initialize the MST and the set X
    T = set()
    X = set()
    
    # select an arbitrary vertex to begin with
    X.add(0)
    
    while len(X) != len(vertices):
        crossing = set()
        # for each element x in X, add the edge (x, k) to crossing if k is not in X
        for x in X:
            for k in range(len(vertices)):
                if k not in X and Graph[x][k] != 0:
                    crossing.add((x, k))
                    
        # find the edge with the smallest weight in crossing
        
        edge = sorted(crossing, key=lambda e:Graph[e[0]][e[1]])[0];
        # add this edge to T
        T.add(edge)
        # add the new vertex to X
        X.add(edge[1])

    # print the edges of the MST
    for edge in T:
        print edge



try:
       
    Graph= [ [0,  4,  0,  0,  0,  0,   0,  8,  0],
             [4,  0,  8,  0,  0,  0,   0, 11,  0],
             [0,  8,  0,  7,  0,  4,   0,  0,  2],
             [0,  0,  7,  0,  9, 14,   0,  0,  0],
             [0,  0,  0,  9,  0, 10,   0,  0,  0],
             [0,  0,  4, 14, 10,  0,   2,  0,  0],
             [0,  0,  0,  0,  0,  2,   0,  1,  6],
             [8, 11,  0,  0,  0,  0,   1,  0,  7],
             [0,  0,  2,  0,  0,  0,   6,  7,  0] ]

    vertices = [ 0, 1, 2, 3, 4, 5, 6, 7, 8 ]

    """    
    print "\n The graph -\n"
    print Graph
    """
    print "\n MST using Prim's Algorithm - \n"
    MST =  Prim(Graph)
    
    
    
    
    
except ValueError:
    print "\n ERROR: Invalid Input\n"
    exit(0)
