""" This program implements a dynamic problem of Rod-Cutting
    We will be using a Bottom-up-Approach to solve the problem
"""

def Bottom_up_rod_cut(p,n):
    
    revenue_array = []
    
    revenue_array.append(0)
    #for i in range(n):
    #    revenue_array.append(0)
    #print revenue_array
    
    j = 0
    
    while(j!=n):
        
        local_sum = -9999
        
        i = 0
        
        while(i<=j):
            local_sum = max(local_sum,p[i]+revenue_array[j-i])
            i=i+1
        
        revenue_array.append(local_sum)
        
        j=j+1
        
    return revenue_array[n]
    

try:
    
    size = int(raw_input("\nEnter the integral length of rod\n"))
    
    if(size == 0):
        print "\n No rod to cut\n"
        exit(1)
    
    Pi = []
    #Pi.append(0)
    print "\nEnter the cost of length of rods\n"
    for i in range(size):
        print "\ncost of",i+1,"unit rod"
        Pi.append(int(raw_input()))
    print Pi
    maximum_revenue = Bottom_up_rod_cut(Pi,size)
    
    print "\n Maximum revenue =",maximum_revenue,"\n"
    
except ValueError:
    print "\nError: Enter integer values only\n"
    exit(0)
    
