"""
    This program implements the Optimal Binary Search Tree
"""


def OBST(p,q,n):
    """
            Arguments 
        -------------------
        p : probabilities of finding actual items
        q : probabilities of failures
        n : Total number of items
        
            Returns
         ---------------
         e : A 2D list of expected cost for searching
         root : Root of the OBST cunstructed
         
    """
    # constructing 3 2D arrays 
    #--------------------------
    
    e = [[0 for i in range(n+2)] for j in range (n+1)]
    w = [[0 for i in range(n+2)] for j in range (n+1)]
    root = [[0 for i in range(n+1)] for j in range (n+1)]
    
    for i in range(1,n+1):
        e[i][i-1] = q[i-1]
        w[i][i-1] = q[i-1]
        
    for l in range(1,n+1):
        for i in range(1,n-l+1):
            j = i+l-1
            e[i][j] = 9999 # Assuming it as INFINITY
            w[i][j] = w[i][j-1] + p[j] + q[j]
            
            for r in range(i,j):
                t = e[i][r-1] + e[r+1][j] + w[i][j]
                
                if ( t< e[i][j]):
                    e[i][j] = t
                    root[i][j] = r
    return (e,root)

try:
    print "\nenter the probabilities for success --- pls let the 1st entry to be 0\n"
    p = [float(x) for x in raw_input().split()]
    print "\nenter the probabilities for failures\n"
    q = [float(x) for x in raw_input().split()]
    
    n = len(p)-1
    
    (cost,root) = OBST(p,q,n)
    
    print "\n the root is \n", root
    print "\n total cost =\n",cost

except ValueError:
    print "\nError: Invalid Input\n"
    exit(0)
    
