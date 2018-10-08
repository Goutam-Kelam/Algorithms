"""
    This inputs the graph to the Kruskal's Algorithm
"""

import cPickle as pkl

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
    
with open('input.pkl','wb') as fp:
    pkl.dump(input,fp)
